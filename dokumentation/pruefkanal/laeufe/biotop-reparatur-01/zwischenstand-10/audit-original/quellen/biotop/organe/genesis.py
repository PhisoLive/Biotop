"""Organ 3.6: Genesis — der Schwarm. Phase 1: eine Nische („Der Sichere“),
zwei Anbieter (Hersteller) über OpenRouter.

Ausgang: Kandidaten als Änderungssätze (unified diff), nie ganze Dateien;
jeder mit Begründung und der Angabe, welche Verträge er berührt.
Der Schwarm sieht nur die Landkarten-Sicht + die Quelldateien seines
Bereichs + die Liste der gescheiterten Wege (Projektgedächtnis).
"""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from ..anbieter import AnbieterFehler, aufrufen
from ..kern import protokoll
from ..kern.datenbank import j, lj
from . import landkarte, nischen

NISCHEN = nischen.NISCHEN

SYSTEM = """Du bist ein Mitglied eines Schwarms, das ein Software-Werk in kleinen, messbaren Schritten hebt.
Du bekommst: die Landkarte des Werks, den Quelltext EINES Bereichs, die harten Maße, die Verträge, und die Liste bereits gescheiterter Wege.
Du lieferst GENAU EINEN Vorschlag als unified diff (git-Format, Pfade relativ zur Werkwurzel, mit a/ und b/ Präfix), der nur Dateien deines Bereichs ändert.
Ein Diff besteht aus Hunks mit 2–3 Kontextzeilen. Eine Datei unter 100 Zeilen darfst du vollständig neu schreiben (ein Hunk, der alles ersetzt); größere Dateien nur in kleinen Hunks.

So wird gemessen (Maß Fassung 2 — nichts anderes zählt):
- Kernmaß je Bereich = −(fehlgeschlagene Tests) − (Sicherheitspunkte: bandit HIGH 10, MEDIUM 3, LOW 1) − (tote Funktionen). Höchstwert 0. BESTANDENE TESTS ZÄHLEN NICHT. Ein Vorschlag, der nur Tests hinzufügt, bringt 0 und wird abgelehnt.
- Vorgeneration und dein Vorschlag werden mit DEMSELBEN Testbestand gemessen (deinem). Behebst du einen Fehler oder Vertragsbruch, liefere in einer NEUEN Datei tests/test_<bereich>_<thema>.py einen Test mit, der an der Vorgeneration FEHLSCHLÄGT und mit deiner Änderung BESTEHT — dann zählt die Behebung +1. Vorhandene Tests niemals ändern oder entfernen.
- Ein Sicherheitsbefund gilt erst als behoben, wenn bandit ihn nicht mehr meldet UND die bekannten Umgehungen (bei eval/exec: Introspektion über ().__class__.__base__.__subclasses__(), __globals__, Format-Strings, Ausdrucks-Explosion) abgewiesen werden. Leere __builtins__ sind KEINE Behebung. eval/exec muss verschwinden (z. B. ast-basierter Auswerter mit Whitelist der Knotentypen und Tiefen-/Größenbegrenzung).
- Grenzmaße (kein Punkt, nur Grenze gegen den Ausgangszustand): Laufzeit auf der Referenzlast darf bis ×2 steigen, bis ×5 wenn dabei ein Sicherheitsbefund im Bereich verschwindet; größte Funktion +25 %.
- Pareto: fehlgeschlagene Tests, Sicherheitspunkte, tote Funktionen dürfen nirgends steigen — auch nicht in Nachbarbereichen.
- Verfassung des Werks (wird mitgegeben) bricht jede andere Erwägung; # nosec oder Werkzeug-Konfiguration statt Code ist ein Verstoß.
Wenn du im Bereich nichts findest, was ein Maß messbar hebt, antworte mit genau: KEIN VORSCHLAG — und einem Satz Begründung. Das ist eine gute Antwort; ein erfundener Vorschlag nicht.

Antwortformat (strikt):
BEGRÜNDUNG: <2–4 Sätze: was, warum, welches Maß steigt>
VERTRÄGE: <welche Verträge berührt werden, oder „keine“>
DIFF:
```diff
<unified diff>
```
"""


def _quelltext(werk: Path, paket: str, bereich: str) -> str:
    teile = []
    for d in sorted((werk / paket / bereich).rglob("*.py")):
        rel = d.relative_to(werk)
        teile.append(f"### {rel}\n```python\n{d.read_text()}\n```")
    tests = werk / "tests" / f"test_{bereich}.py"
    if tests.exists():
        teile.append(f"### {tests.relative_to(werk)} (nur lesen)\n```python\n{tests.read_text()}\n```")
    return "\n\n".join(teile)


def _parsen(text: str) -> dict | None:
    if "KEIN VORSCHLAG" in text[:400]:
        return None
    m = re.search(r"```diff\s*\n(.*?)```", text, re.S)
    if not m:
        m = re.search(r"(^diff --git .*|^--- a/.*)", text, re.S | re.M)
        diff = m.group(1) if m else ""
    else:
        diff = m.group(1)
    if not diff.strip() or "+++ " not in diff:
        return None
    beg = re.search(r"BEGRÜNDUNG:\s*(.+?)(?:\nVERTRÄGE:|\nDIFF:|$)", text, re.S)
    vt = re.search(r"VERTRÄGE:\s*(.+?)(?:\nDIFF:|$)", text, re.S)
    return {"diff": diff.strip() + "\n", "begruendung": (beg.group(1).strip() if beg else "")[:1000],
            "vertraege": (vt.group(1).strip() if vt else "")[:500]}


def dateien_im_diff(diff: str) -> list[str]:
    return sorted(set(re.findall(r"^\+\+\+ b/(\S+)", diff, re.M)) | set(re.findall(r"^diff --git a/(\S+) b/", diff, re.M)))


def gescheiterte_wege(con: sqlite3.Connection, lauf_id: int, bereich: str) -> list[str]:
    out = []
    for z in con.execute("SELECT generation, begruendung, grund FROM kandidaten WHERE lauf_id=? AND bereich=? AND status='abgelehnt' AND grund NOT LIKE 'Diff nicht anwendbar%' ORDER BY id DESC LIMIT 12",
                         (lauf_id, bereich)):
        out.append(f"Gen {z['generation']}: {z['begruendung'][:200]} → abgelehnt: {z['grund'][:200]}")
    return out


def erzeugen(con: sqlite3.Connection, lauf_id: int, werk_id: int, generation: int, werk: Path, paket: str,
             bereich: str, masse: dict, nische: str = "sicher", befunde: list | None = None,
             referenzlast: str | None = None, vertraege_text: str = "") -> list[int]:
    """Erzeugt Kandidaten für einen Bereich: zwei per Bandit gewählte Hersteller der Nische.
    Rückgabe: Kandidaten-IDs (auch „kein Vorschlag“ wird als Kandidat mit Status 'leer' geführt)."""
    n = NISCHEN[nische]
    sicht = landkarte.sicht(con, werk_id, paket, bereich)
    quelle = _quelltext(werk, paket, bereich)
    from . import gedaechtnis as _G, mentor as _M
    wege = gescheiterte_wege(con, lauf_id, bereich)
    wege_werk = _G.gescheiterte_wege_text(con, werk_id, bereich)  # 3.12 Projektgedächtnis über alle Läufe des Werks
    richtung = _M.richtung_text(con, lauf_id)  # 3.4 Mentor
    from . import verfassung as _V
    verf = _V.lesen(con, werk_id)
    verf_text = ("VERFASSUNG DES WERKS:\n" + verf["text"] + "\n\n") if verf else ""
    el = nischen.elite(con, lauf_id, nische, bereich)
    elite_text = (f"\n\nELITE DEINER NISCHE IN DIESEM BEREICH (bester bisheriger Überlebender, Gen {el['generation']}, Zuwachs {el['zuwachs']}):\n"
                  f"{el['begruendung'][:300]}\n```diff\n{el['diff'][:2500]}\n```\nBaue darauf auf oder schlage etwas Besseres vor.") if el else ""
    last_text = (f"\n\nREFERENZLAST (so wird die Laufzeit gemessen; Funktion last_{bereich}):\n```python\n{referenzlast}\n```") if (referenzlast and n["ziel"] == "laufzeit") else ""
    vt_text = (f"\n\nEXPLIZITE VERTRÄGE AN DEN GRENZEN DIESES BEREICHS (Änderung nur mit Nachbar, unter VERTRÄGE nennen):\n{vertraege_text}") if vertraege_text else ""
    offene = [dict(z) for z in con.execute("SELECT name, code FROM immunsystem WHERE werk_id=? AND bereich=? AND status IN ('gefunden','offen')", (werk_id, bereich))]
    offen_text = ("\n\nOFFENE FUNDE DES IMMUNSYSTEMS IN DIESEM BEREICH (diese Tests schlagen derzeit fehl; sie werden deinem Vorschlag paarweise mitgegeben — eine Behebung zählt +1):\n"
                  + "\n".join(f"- tests/test_{bereich}_immun_{o['name']}.py:\n```python\n{o['code'][:1500]}\n```" for o in offene)) if offene else ""
    nutzer = (f"{n['auftrag']}{richtung}\n\n{verf_text}LANDKARTE:\n{sicht}{vt_text}\n\nHARTE MASSE DES BEREICHS {bereich} (aktuell): {j(masse)}\n"
              f"Statische Befunde im Bereich: {j(befunde)}{offen_text}{last_text}{elite_text}\n\n"
              f"BEREITS GESCHEITERTE WEGE IN DIESEM LAUF (nicht wiederholen):\n" + ("\n".join(wege) if wege else "keine") +
              f"\n\nPROJEKTGEDÄCHTNIS — GESCHEITERTE WEGE AN DIESEM WERK AUS ALLEN LÄUFEN (nicht wiederholen; eine Wiederholung wird ohne Prüfung verworfen):\n{wege_werk}" +
              f"\n\nQUELLTEXT DES BEREICHS {bereich}:\n{quelle}")
    ids = []
    for hersteller, modell in nischen.waehlen(con, lauf_id, nische):
        anbieter = "openrouter"
        try:
            a = aufrufen(con, lauf_id, anbieter, modell, SYSTEM, nutzer, zweck=f"schwarm.{nische}.{bereich}.gen{generation}",
                         max_tokens=3500, temperatur=n["temperatur"])
        except AnbieterFehler as e:
            protokoll.schreiben(con, "schwarm.fehler", lauf_id=lauf_id, bereich=bereich, modell=modell, fehler=str(e)[:300])
            continue
        k = _parsen(a.text)
        hersteller = modell.split("/")[0]
        if k is None:
            status, diff, beg, vt = "leer", "", a.text.strip()[:400], ""
        else:
            status, diff, beg, vt = "erzeugt", k["diff"], k["begruendung"], k["vertraege"]
            fremd = [f for f in dateien_im_diff(diff) if not (f.startswith(f"{paket}/{bereich}/") or f.startswith(f"tests/test_{bereich}_")
                                                              or (f.startswith("tests/vertraege/test_vertrag_") and f"_{bereich}" in f[len("tests/vertraege/test_vertrag"):]))]
            if fremd:
                status, beg = "abgelehnt", beg
                grund = f"Diff berührt fremde Dateien: {fremd}"
            else:
                grund = ""
        cur = con.execute(
            "INSERT INTO kandidaten(lauf_id, generation, bereich, nische, anbieter, modell, diff, begruendung, status, grund, erstellt_am, vertraege) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (lauf_id, generation, bereich, nische, f"{anbieter}/{hersteller}", modell, diff, beg, status,
             grund if status == "abgelehnt" else ("kein Vorschlag" if status == "leer" else ""), protokoll.jetzt(), vt))
        ids.append(cur.lastrowid)
        protokoll.schreiben(con, "schwarm.kandidat", lauf_id=lauf_id, generation=generation, bereich=bereich, nische=nische,
                            modell=modell, kandidat=cur.lastrowid, status=status, dateien=dateien_im_diff(diff), vertraege=vt[:200])
    return ids
