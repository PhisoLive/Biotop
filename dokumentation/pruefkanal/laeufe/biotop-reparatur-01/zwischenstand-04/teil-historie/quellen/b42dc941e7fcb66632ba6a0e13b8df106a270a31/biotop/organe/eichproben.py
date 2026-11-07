"""Organ „Generation minus eins", Teil 2 — die vier Eichproben als Vorspann jedes Laufs (Fassung 5, 3.5).

Die Proben setzen am VERSIEGELTEN EICHGEGENSTAND an (organe/eichgegenstand.py): einem Bereichspaar mit Vertrag,
das je Werk einmal gewählt und danach unverändert bleibt. Ihre Eingriffe werden mechanisch aus dem Syntaxbaum
gebaut, nicht aus Textankern — in Phase 2/3 zielten die Proben nach jeder angenommenen Generation stillschweigend
woanders hin, weil die Anker verschoben waren.

Die vier Proben (Tor 2, jetzt Vorspann):
  nebenwirkung  — hebt Bereich A messbar, senkt Bereich B messbar  → muss abgelehnt werden, Bericht nennt B
  regression    — macht eine Behebung rückgängig und bringt grüne Tests mit → muss abgelehnt werden,
                  der gefallene EINZELTEST muss benannt sein
  norm          — bringt einen Test mit, der an der Vorgeneration fällt, am Kandidaten besteht, ohne Absturz und
                  ohne Vertragsverweis → bleibt „offen", 0 Punkte, nicht im Werk
  vertrag       — ändert den Vertrag ohne Anpassung des Nachbarn → muss abgelehnt werden

Besteht eine Probe nicht, beginnt kein Lauf (Satz 6). Jede Probe wird einzeln abgerechnet: Kammerläufe,
Modellaufrufe und Kosten je Probe (Festlegung Chat-Claude, Fassung 6).
Alle Probenkandidaten tragen `ist_probe=1` und kommen damit in kein Gedächtnis.
"""
from __future__ import annotations

import ast
import sqlite3
import time
from pathlib import Path

from ..kern import protokoll
from ..kern.datenbank import transaktion
from . import aegis, eichgegenstand, eichung

PROBEN = ("nebenwirkung", "regression", "norm", "vertrag")


# ---------------------------------------------------------------- Bausteine (mechanisch, über den Syntaxbaum)
def _funktionen(pfad: Path, paket: str, bereich: str) -> list[tuple[Path, ast.FunctionDef]]:
    """Alle Funktionen eines Bereichs mit ihrer Datei — Reihenfolge deterministisch (Datei, Zeile)."""
    aus = []
    wurzel = pfad / paket / bereich
    for datei in sorted(wurzel.rglob("*.py")):
        try:
            baum = ast.parse(datei.read_text())
        except SyntaxError:
            continue
        for k in ast.walk(baum):
            if isinstance(k, ast.FunctionDef) and not k.name.startswith("_"):
                aus.append((datei, k))
    return sorted(aus, key=lambda x: (str(x[0]), x[1].lineno))


def _diff(rel: str, alt: str, neu: str) -> str:
    """Vollständiger Datei-Diff (kein Kontextabgleich nötig — der Diffwerk-Teil wendet ihn als Ersetzung an)."""
    a = alt.splitlines(); n = neu.splitlines()
    kopf = f"--- a/{rel}\n+++ b/{rel}\n@@ -1,{len(a)} +1,{len(n)} @@\n"
    return kopf + "\n".join(["-" + z for z in a] + ["+" + z for z in n]) + "\n"


def _neue_datei(rel: str, inhalt: str) -> str:
    n = inhalt.splitlines()
    return f"--- /dev/null\n+++ b/{rel}\n@@ -0,0 +1,{len(n)} @@\n" + "\n".join("+" + z for z in n) + "\n"


def _lahmlegen(pfad: Path, paket: str, bereich: str) -> tuple[str, str]:
    """Erste öffentliche Funktion des Bereichs wirkungslos machen → bestehende Tests des Bereichs fallen.
    Rückgabe: (Diff, Beschreibung). Mechanisch über den Syntaxbaum, kein Textanker."""
    for datei, fn in _funktionen(pfad, paket, bereich):
        quelle = datei.read_text()
        zeilen = quelle.splitlines()
        einzug = " " * (fn.col_offset + 4)
        # nach der Signatur (und einem etwaigen Docstring) ein `return None` einsetzen
        ziel = fn.body[0].lineno - 1
        if isinstance(fn.body[0], ast.Expr) and isinstance(getattr(fn.body[0], "value", None), ast.Constant) \
                and isinstance(fn.body[0].value.value, str):
            ziel = (fn.body[0].end_lineno or fn.body[0].lineno)
        neu = zeilen[:ziel] + [f"{einzug}return None  # Eichprobe: Funktion wirkungslos"] + zeilen[ziel:]
        rel = str(datei.relative_to(pfad))
        return _diff(rel, quelle, "\n".join(neu) + "\n"), f"{rel}::{fn.name} liefert None"
    raise RuntimeError(f"Bereich {bereich} hat keine öffentliche Funktion — Probe nicht baubar")


def _beschleunigen(pfad: Path, paket: str, bereich: str) -> tuple[str, str]:
    """Eine reine Funktion des Bereichs mit einem Merkspeicher versehen → Laufzeit sinkt messbar."""
    for datei, fn in _funktionen(pfad, paket, bereich):
        if fn.args.args and not any(a.arg == "self" for a in fn.args.args):
            quelle = datei.read_text()
            zeilen = quelle.splitlines()
            speicher = f"_eichprobe_speicher_{fn.name}"
            einzug = " " * (fn.col_offset + 4)
            args = ", ".join(a.arg for a in fn.args.args)
            ziel = fn.body[0].lineno - 1
            if isinstance(fn.body[0], ast.Expr) and isinstance(getattr(fn.body[0], "value", None), ast.Constant) \
                    and isinstance(fn.body[0].value.value, str):
                ziel = (fn.body[0].end_lineno or fn.body[0].lineno)
            kopf = [f"{einzug}_s = {speicher}",
                    f"{einzug}try:",
                    f"{einzug}    _k = ({args},)",
                    f"{einzug}    if _k in _s:",
                    f"{einzug}        return _s[_k]",
                    f"{einzug}except TypeError:",
                    f"{einzug}    _k = None"]
            rumpf = zeilen[ziel:]
            # Rückgaben durch Merken ersetzen: nur die erste Ebene, sonst zu invasiv
            neu = zeilen[:ziel] + kopf + rumpf
            neu = [f"{speicher} = {{}}", ""] + neu
            rel = str(datei.relative_to(pfad))
            return _diff(rel, quelle, "\n".join(neu) + "\n"), f"{rel}::{fn.name} bekommt einen Merkspeicher"
    raise RuntimeError(f"Bereich {bereich} hat keine geeignete Funktion — Probe nicht baubar")


def _gruene_tests(bereich: str, n: int = 3) -> tuple[str, str]:
    rel = f"tests/test_{bereich}_eichprobe_gruen.py"
    inhalt = "".join("\n".join([f"def test_{bereich}_eichprobe_gruen_{i}():", "    assert True", ""]) for i in range(n))
    return _neue_datei(rel, inhalt), f"{n} grüne Tests in {rel}"


def _normtest(pfad: Path, paket: str, bereich: str) -> tuple[str, str, str]:
    """Test, der an der Vorgeneration FÄLLT und am Kandidaten BESTEHT — ohne Absturz, ohne Vertragsverweis.
    Der Kandidat setzt dafür eine neue Funktion, der Test prüft sie. Reine Meinung über gewünschtes Verhalten."""
    rel_code = f"{paket}/{bereich}/_eichprobe_norm.py"
    code = "def eichprobe_kennzeichen():\n    return 'norm'\n"
    rel_test = f"tests/test_{bereich}_eichprobe_norm.py"
    test = (f"from {paket}.{bereich}._eichprobe_norm import eichprobe_kennzeichen\n\n\n"
            f"def test_{bereich}_eichprobe_norm():\n"
            f"    assert eichprobe_kennzeichen() == 'norm'\n")
    return _neue_datei(rel_code, code) + _neue_datei(rel_test, test), rel_test, "neue Funktion + Test darauf"


# ---------------------------------------------------------------- Ablauf
def _einschleusen(con, lauf_id: int, generation: int, bereich: str, diff: str, begruendung: str,
                  vertraege: str, name: str) -> int:
    with transaktion(con):
        cur = con.execute("INSERT INTO kandidaten(lauf_id, generation, bereich, nische, anbieter, modell, diff,"
                          " begruendung, status, grund, erstellt_am, vertraege, ist_probe)"
                          " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,1)",
                          (lauf_id, generation, bereich, "probe", "hermes", f"hermes/eichprobe-{name}", diff,
                           begruendung, "erzeugt", "", protokoll.jetzt(), vertraege))
    protokoll.schreiben(con, "eichprobe.eingeschleust", lauf_id=lauf_id, kandidat=cur.lastrowid, probe=name,
                        bereich=bereich, ist_probe=True)
    return cur.lastrowid


def _kassenstand(con, lauf_id: int) -> tuple[int, float]:
    z = con.execute("SELECT COUNT(*) n, COALESCE(SUM(kosten_eur),0) c FROM kasse WHERE lauf_id=?", (lauf_id,)).fetchone()
    return z["n"], z["c"]


def proben(con: sqlite3.Connection, lauf_id: int, werk_id: int, pfad: Path, paket: str, bereiche: list[str],
           bstrassen, basis: dict, ausgang: dict, ref: str | None, tausch: dict, generation: int = 0) -> dict:
    """Die vier Proben am versiegelten Gegenstand. Rückgabe mit Ergebnis und Abrechnung je Probe."""
    g = eichgegenstand.sichern(con, werk_id, lauf_id, pfad)
    if not g.get("gegenstand"):
        return {"bestanden": False, "grund": g.get("befund") or "kein Eichgegenstand", "gegenstand": None,
                "proben": {}, "lauf_startet": False}
    geg = g["gegenstand"]
    A, B = geg["von_bereich"], geg["nach_bereich"]      # A = Konsument, B = Lieferant des Vertrags
    ergebnisse: dict = {}

    def lauf_probe(name: str, bereich: str, diff: str, begruendung: str, vertraege: str, pruefung) -> dict:
        t0 = time.time()
        n0, c0 = _kassenstand(con, lauf_id)
        kid = _einschleusen(con, lauf_id, generation, bereich, diff, begruendung, vertraege, name)
        u = aegis.pruefen(con, lauf_id, werk_id, kid, pfad, paket, bereiche, bstrassen, basis, ausgang, ref, tausch)
        n1, c1 = _kassenstand(con, lauf_id)
        ok, befund = pruefung(u)
        e = {"kandidat": kid, "bestanden": ok, "befund": befund, "status": u.get("status"),
             "grund": (u.get("grund") or "")[:300], "modellaufrufe": n1 - n0, "kosten_eur": round(c1 - c0, 6),
             "kammerlaeufe": 1, "dauer_s": round(time.time() - t0, 1)}
        eichung.kosten_buchen(con, lauf_id, werk_id, f"probe.{name}", 1, time.time() - t0,
                              modellaufrufe=n1 - n0, kosten_eur=c1 - c0)
        protokoll.schreiben(con, "eichprobe.ergebnis", lauf_id=lauf_id, probe=name, **{k: v for k, v in e.items()})
        ergebnisse[name] = e
        return e

    # --- 1. Nebenwirkung: B schneller, A kaputt → muss abgelehnt werden und A nennen
    d_a, t_a = _lahmlegen(pfad, paket, A)
    lauf_probe("nebenwirkung", A, d_a, f"Eichprobe Nebenwirkung: {t_a} (Bereich {A} fällt)", "keine",
               lambda u: ((u.get("status") != "ueberlebt" and A in (u.get("grund") or "")),
                          f"abgelehnt und nennt {A}: {(u.get('grund') or '')[:160]}"))

    # --- 2. Regression: dieselbe Verschlechterung, aber mit drei grünen Tests → Einzeltest muss benannt sein
    d_g, t_g = _gruene_tests(A)
    lauf_probe("regression", A, d_a + d_g, f"Eichprobe Regression: {t_a} plus {t_g}", "keine",
               lambda u: ("Regression je Test" in (u.get("grund") or "") and "::" in (u.get("grund") or ""),
                          f"gefallener Einzeltest benannt: {(u.get('grund') or '')[:160]}"))

    # --- 3. Norm: Test ohne Absturz und ohne Vertragsverweis → offen, 0 Punkte, nicht im Werk
    d_n, rel_test, t_n = _normtest(pfad, paket, B)
    lauf_probe("norm", B, d_n, f"Eichprobe Norm: {t_n}", "keine",
               lambda u: (int((u.get("masse") or {}).get("zuwachs") or 0) == 0
                          and rel_test.split("/")[-1] not in str((u.get("masse") or {}).get("_testbestand") or []),
                          f"0 Punkte und nicht im Werk: zuwachs={(u.get('masse') or {}).get('zuwachs')}, "
                          f"norm={u.get('norm')}, Status {u.get('status')}"))

    # --- 4. Vertrag: Grenze ändern, Nachbar NICHT anpassen → abgelehnt
    # Die Vertragsdatei allein genügt dem Ankläger nicht („Diff ändert nichts"): Eine Grenzänderung besteht aus
    # der neuen Zusicherung IM VERTRAG und ihrer Nutzung im Konsumenten. Der Lieferant B wird bewusst nicht
    # angepasst — genau das muss auffallen.
    vertrag_rel = geg["vertrag_pfad"]
    alt_v = (pfad / vertrag_rel).read_text()
    neu_v = alt_v + (f"\n\ndef test_eichprobe_vertrag_neue_zusicherung():\n"
                     f"    \"\"\"Eichprobe: {A} verlangt von {B} die Funktion eichprobe_zusicherung().\"\"\"\n"
                     f"    from {paket}.{B} import eichprobe_zusicherung\n"
                     f"    assert eichprobe_zusicherung() == 'da'\n")
    # Konsument A nutzt die neue Zusicherung — der Lieferant B hat sie nicht.
    datei_a, fn_a = _funktionen(pfad, paket, A)[0]
    quelle_a = datei_a.read_text()
    neu_a = quelle_a.replace(f"def {fn_a.name}",
                             f"def _eichprobe_nutzt_zusicherung():\n"
                             f"    from {paket}.{B} import eichprobe_zusicherung\n"
                             f"    return eichprobe_zusicherung()\n\n\ndef {fn_a.name}", 1)
    d_v = _diff(vertrag_rel, alt_v, neu_v) + _diff(str(datei_a.relative_to(pfad)), quelle_a, neu_a)
    lauf_probe("vertrag", A, d_v,
               f"Eichprobe Vertrag: {vertrag_rel} fordert {B}.eichprobe_zusicherung(), {A} nutzt sie, "
               f"Nachbar {B} NICHT angepasst", f"{vertrag_rel}",
               lambda u: (u.get("status") != "ueberlebt",
                          f"abgelehnt: {(u.get('grund') or '')[:160]}"))

    alle_ok = all(e["bestanden"] for e in ergebnisse.values())
    protokoll.schreiben(con, "eichprobe.abschluss", lauf_id=lauf_id, werk_id=werk_id, bestanden=alle_ok,
                        gegenstand=f"{A}→{B}", vertrag=vertrag_rel,
                        je_probe={k: {"bestanden": v["bestanden"], "modellaufrufe": v["modellaufrufe"],
                                      "kosten_eur": v["kosten_eur"]} for k, v in ergebnisse.items()},
                        regel="Fassung 5 3.5: Besteht eine Probe nicht, beginnt kein Lauf (Satz 6)")
    return {"bestanden": alle_ok, "gegenstand": geg, "proben": ergebnisse, "lauf_startet": alle_ok,
            "grund": None if alle_ok else "mindestens eine Eichprobe nicht bestanden"}


def text(e: dict) -> list[str]:
    if not e.get("gegenstand"):
        return [f"Eichproben: NICHT GELAUFEN — {e.get('grund')}"]
    g = e["gegenstand"]
    z = [f"Eichproben am versiegelten Gegenstand {g['von_bereich']}→{g['nach_bereich']} "
         f"(Vertrag `{g['vertrag_pfad']}`, Prüfsumme {g['vertrag_pruefsumme'][:16]}):"]
    for name in PROBEN:
        p = e["proben"].get(name)
        if not p:
            z.append(f"  {name:<13} NICHT GELAUFEN")
            continue
        z.append(f"  {name:<13} {'bestanden' if p['bestanden'] else 'NICHT BESTANDEN'} | K{p['kandidat']} "
                 f"| {p['modellaufrufe']:>2} Modellaufrufe | {p['kosten_eur']:.4f} € | {p['kammerlaeufe']} Kammerlauf "
                 f"| {p['dauer_s']:.0f} s")
        z.append(f"                {p['befund']}")
    n = sum(p["modellaufrufe"] for p in e["proben"].values())
    c = sum(p["kosten_eur"] for p in e["proben"].values())
    z.append(f"  SUMME Vorspann: {len(e['proben'])} Proben, {n} Modellaufrufe, {c:.4f} €, "
             f"{sum(p['kammerlaeufe'] for p in e['proben'].values())} Kammerläufe, "
             f"{sum(p['dauer_s'] for p in e['proben'].values()):.0f} s")
    if not e["bestanden"]:
        z.append("  LAUF STARTET NICHT: mindestens eine Eichprobe nicht bestanden (Satz 6).")
    return z
