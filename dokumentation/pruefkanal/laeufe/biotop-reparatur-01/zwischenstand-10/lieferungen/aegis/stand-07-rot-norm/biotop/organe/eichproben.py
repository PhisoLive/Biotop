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
import hashlib
import sqlite3
import tempfile
import time
from contextlib import contextmanager
from pathlib import Path

from ..kern import protokoll
from ..kern.datenbank import lj, transaktion
from . import aegis, eichgegenstand, eichung, kammer, verfassung

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
    """Kleine AST-Eingriffe als Kontextdiff; keine künstliche Vollersetzung."""
    from difflib import unified_diff
    return "".join(unified_diff(alt.splitlines(keepends=True), neu.splitlines(keepends=True),
                                fromfile=f"a/{rel}", tofile=f"b/{rel}"))


def _neue_datei(rel: str, inhalt: str) -> str:
    n = inhalt.splitlines()
    return f"--- /dev/null\n+++ b/{rel}\n@@ -0,0 +1,{len(n)} @@\n" + "\n".join("+" + z for z in n) + "\n"


def _lahmlegen(pfad: Path, paket: str, bereich: str, alle: bool = False) -> tuple[str, str]:
    """Reale öffentliche Funktionen per AST wirkungslos machen (nur Privatfixture)."""
    funktionen = _funktionen(pfad, paket, bereich)
    if not funktionen:
        raise RuntimeError(f"Bereich {bereich} hat keine öffentliche Funktion — Probe nicht baubar")
    auswahl = funktionen if alle else funktionen[:1]
    quellen = {datei: datei.read_text() for datei, _ in auswahl}
    neu = {datei: text.splitlines() for datei, text in quellen.items()}
    beschreibung = []
    for datei, fn in reversed(auswahl):
        ziel = fn.body[0].end_lineno if ast.get_docstring(fn) is not None else fn.body[0].lineno - 1
        neu[datei].insert(ziel, " " * (fn.col_offset + 4) + "return None  # Eichprobe: Funktion wirkungslos")
        beschreibung.append(f"{datei.relative_to(pfad)}::{fn.name} liefert None")
    return ("".join(_diff(datei.relative_to(pfad).as_posix(), alt, "\n".join(neu[datei]) + "\n")
                    for datei, alt in quellen.items()), "; ".join(reversed(beschreibung)))


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
    """Meinung über eine VORHANDENE Funktion; niemals ein neuer Import am Ausgang.

    Nur eindeutig skalar aufrufbare freie Funktionen sind geeignet. Fehlt eine,
    wird die Probe als nicht baubar gemeldet, nicht auf eine andere Mechanik ersetzt.
    Der tatsächliche Assertion-/Normnachweis erfolgt anschließend in der Kammer.
    """
    for datei, fn in _funktionen(pfad, paket, bereich):
        argumente = fn.args.posonlyargs + fn.args.args
        importname, aufruf = fn.name, fn.name
        if fn.col_offset != 0:
            # Methoden nur an einer AST-belegt ohne Pflichtargumente baubaren
            # Klasse. Die Instanz entsteht ausschließlich im Kammer-Test.
            baum = ast.parse(datei.read_text())
            klasse = next((k for k in baum.body if isinstance(k, ast.ClassDef)
                           and any(isinstance(f, ast.FunctionDef) and f.lineno == fn.lineno for f in k.body)), None)
            if klasse is None or klasse.decorator_list or klasse.bases or not argumente or argumente[0].arg != "self":
                continue
            init = next((f for f in klasse.body if isinstance(f, ast.FunctionDef) and f.name == "__init__"), None)
            if init and (len(init.args.posonlyargs + init.args.args) - len(init.args.defaults) > 1
                         or any(d is None for d in init.args.kw_defaults)):
                continue
            argumente = argumente[1:]
            importname, aufruf = klasse.name, f"{klasse.name}().{fn.name}"
        if (fn.decorator_list or len(argumente) != 1
                or fn.args.vararg or fn.args.kwarg or fn.args.kwonlyargs):
            continue
        art = ast.unparse(argumente[0].annotation) if argumente[0].annotation else ""
        wert = {"float": "137.125", "int": "137", "str": "'eichprobe_eingabe'"}.get(art)
        if wert is None:
            continue
        quelle = datei.read_text()
        zeilen = quelle.splitlines()
        erstes = fn.body[0]
        ziel = erstes.end_lineno if ast.get_docstring(fn) is not None else erstes.lineno - 1
        einzug = " " * (fn.col_offset + 4)
        neu = zeilen[:ziel] + [f"{einzug}if {argumente[0].arg} == {wert}:",
                              f"{einzug}    return 'eichprobe_norm_neu'"] + zeilen[ziel:]
        rel_code = datei.relative_to(pfad).as_posix()
        modul = ".".join(datei.relative_to(pfad).with_suffix("").parts)
        if modul.endswith(".__init__"):
            modul = modul[:-9]
        rel_test = f"tests/test_{bereich}_eichprobe_norm.py"
        test = (f"from {modul} import {importname}\n\n"
                f"def test_{bereich}_eichprobe_norm():\n"
                f"    assert {aufruf}({wert}) == 'eichprobe_norm_neu'\n")
        return (_diff(rel_code, quelle, "\n".join(neu) + "\n") + _neue_datei(rel_test, test),
                rel_test, f"{rel_code}::{aufruf}({wert}): abweichende Rückgabe ohne Verweis")
    raise RuntimeError(f"Bereich {bereich}: keine skalar aufrufbare Funktion/Methode für Normprobe")


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


@contextmanager
def _privat(con, pfad):
    """Jede Probe erhält eigene DB und eigenes Werk; keine Rückschreibverbindung."""
    if con.in_transaction:
        raise RuntimeError("Eichproben brauchen einen abgeschlossenen DB-Ausgang")
    with tempfile.TemporaryDirectory(prefix="eichprobe-") as ordner:
        wurzel = Path(ordner)
        werk = wurzel / "werk"
        kammer._kopie(pfad, werk)
        db = wurzel / "probe.db"
        kopie = sqlite3.connect(db, isolation_level=None)
        kopie.row_factory = sqlite3.Row
        try:
            con.backup(kopie)
            db.chmod(0o600)
            # Auch etwaige DB-interne Werkpfadleser dürfen nur die Kopie finden.
            kopie.execute("UPDATE werke SET pfad=? WHERE pfad=?", (str(werk), str(pfad)))
            yield kopie, werk
        finally:
            kopie.close()


def _vertrag_pruefbar(belege: dict, gegenprobe: bool) -> bool:
    """Ausführungszeugen des BENANNTEN Vertrags, nicht das negierte Gesamturteil.

    Die Klassifikation kommt ausschließlich aus Aegis' originalem JUnit-Lauf.
    Positiv müssen Vertrag UND Verbraucher an der eingesetzten Zusicherung im
    Verbraucher scheitern; negativ müssen beide tatsächlich bestanden sein.
    Sammel-/Fixturefehler, fehlende oder unvollständige Zeugen bleiben ungültig.
    """
    pfad = belege.get("vertragspfad")
    vertrag = belege.get("vertragstest")
    verbraucher = belege.get("verbrauchertest")
    ort = belege.get("verbraucherdatei")
    if not all(isinstance(x, str) and x for x in (pfad, vertrag, verbraucher, ort)):
        return False
    if not vertrag.startswith(Path(pfad).name + "::") or ort.startswith("tests/"):
        return False
    name = f"{Path(pfad).parent.as_posix()}/{vertrag}"
    basis, kandidat = belege.get("basis_tests"), belege.get("kandidat_tests")
    if not isinstance(basis, dict) or not isinstance(kandidat, dict):
        return False

    def bestanden(x):
        return (isinstance(x, dict) and x.get("ok") is True
                and x.get("bestaetigt") is False and x.get("meldung") == "")

    def zusicherung_fehlt(x):
        return (isinstance(x, dict) and x.get("ok") is False and x.get("bestaetigt") is True
                and x.get("ort") == ort and isinstance(x.get("meldung"), str)
                and "eichprobe_zusicherung" in x["meldung"])

    if not bestanden(basis.get(verbraucher)) or not all(bestanden(x) for x in basis.values()):
        return False
    erwartet = bestanden if gegenprobe else zusicherung_fehlt
    return (erwartet(kandidat.get(name)) and erwartet(kandidat.get(verbraucher))
            and all(isinstance(n, str) and not n.endswith("::*")
                    and (bestanden(x) or (not gegenprobe and zusicherung_fehlt(x)))
                    for n, x in kandidat.items()))


def _bestanden(name: str, belege: dict) -> bool:
    """Belege der ORIGINALEN Ableitungen verlangen; kein eigenes Ersatz-Pareto."""
    u = belege.get("urteil", {})
    m = u.get("mass")
    messung = belege.get("messung", {})
    if (not isinstance(m, dict) or not m or not messung.get("gueltig")
            or not (messung.get("_basis_paar") or {}).get("gueltig")):
        return False
    if name == "nebenwirkung":
        a, b = belege["gewinnbereich"], belege["verlustbereich"]
        return all((u.get("status") == "abgelehnt", m.get("ok") is False,
                    any(s.startswith(a + ".tests_fehlgeschlagen:") for s in m.get("pareto_besser", [])),
                    any(s.startswith(b + ".tests_fehlgeschlagen:") for s in m.get("pareto_schlechter", [])),
                    b in u.get("grund", "")))
    if name == "regression":
        n = belege["regressionstest"]
        massname = n.split("/")[-1]
        gruene = belege.get("gruene_tests", [])
        return all((u.get("status") == "abgelehnt", m.get("ok") is False,
                    belege["basis_tests"].get(n, {}).get("ok") is True,
                    belege["kandidat_tests"].get(n, {}).get("ok") is False,
                    belege["kandidat_tests"].get(n, {}).get("bestaetigt") is True,
                    any(s.startswith("Regression je Test") and massname in s
                        for s in m.get("pareto_schlechter", [])),
                    len(gruene) >= 3,
                    all(belege["kandidat_tests"][g]["ok"] and belege["basis_tests"][g]["ok"]
                        for g in gruene)))
    if name == "vertrag":
        if not _vertrag_pruefbar(belege, gegenprobe=False):
            return False
        n = belege["verbrauchertest"]
        x = belege["kandidat_tests"].get(n, {})
        return all((u.get("status") == "abgelehnt", m.get("ok") is False,
                    belege["vertragstest"] in u.get("vertrag_verletzt", []),
                    u.get("grund", "").startswith("Vertrag verletzt (Schritt 2):"),
                    belege["vertragstest"] in u.get("grund", ""),
                    belege["basis_tests"].get(n, {}).get("ok") is True,
                    x.get("ok") is False, x.get("bestaetigt") is True,
                    x.get("ort") == belege["verbraucherdatei"],
                    "eichprobe_zusicherung" in x.get("meldung", "")))
    if name == "norm":
        n = belege["testname"]
        vorher = belege.get("basis_tests", {}).get(f"{belege['testpfad']}::{n}", {})
        nachher = belege.get("kandidat_tests", {}).get(f"{belege['testpfad']}::{n}", {})
        norm = u.get("norm", [])
        return all((
            vorher.get("ok") is False, vorher.get("bestaetigt") is True,
            vorher.get("meldung", "").startswith(("AssertionError", "assert")),
            not vorher.get("ort", "").startswith(belege["paket"] + "/"),
            nachher.get("ok") is True, belege.get("ohne_verweis") is True,
            n in norm or f"{belege['testpfad']}::{n}" in norm,
            any(z["status"] == "offen_norm" and f"def {n}(" in z["code"]
                for z in belege.get("normeintraege", [])),
            "zuwachs" in m and m["zuwachs"] == 0,
            # Geprüft wird die Normklassifikation, nicht die separat geeichte
            # Laufzeitgrenze. Deren Befund bleibt im unveränderten Originalurteil.
            u.get("status") == "abgelehnt", not m.get("pareto_schlechter"),
            not u.get("vertrag_verletzt"), not u.get("verfassung_verstoesse"),
            "_dateien" in messung and not any(n in code for p, code in messung["_dateien"].items()
                                              if p.startswith("tests/")),
            belege.get("werk_test_vorhanden") is False,
        ))
    return False


def _norm_vorbereiten(db, werk, werk_id, paket, bereich, gegenprobe):
    diff, testpfad, beschreibung = _normtest(werk, paket, bereich)
    dateien = aegis.kandidat_dateien(werk, diff)
    if dateien is None or any(c is None for c in dateien.values()):
        raise RuntimeError(aegis.diff_grund(werk, diff) or "Normdiff ungültig")
    testcode = dateien[testpfad]
    testname = f"test_{bereich}_eichprobe_norm"
    belege = {"paket": paket, "testpfad": testpfad, "testname": testname,
              "basis_tests": aegis.junit_lauf(werk, paket, {testpfad: testcode}, [testpfad]),
              "kandidat_tests": aegis.junit_lauf(werk, paket, dateien, [testpfad]),
              "ohne_verweis": not aegis._nennt_vertrag(testcode, testname, verfassung.lesen(db, werk_id),
                                                      db, werk_id, bereich)}
    # Gleiche Änderung, gleiche Zeugen, aber kein Normtest im Anklagepfad.
    if gegenprobe:
        diff = "".join(_diff(p, (werk / p).read_text(), code)
                       for p, code in dateien.items() if not p.startswith("tests/"))
    return diff, beschreibung, belege, None if gegenprobe else testcode


def _nebenwirkung_vorbereiten(werk, paket, a, b, gegenprobe):
    """Bekannten Defekt in A NUR im privaten Ausgang setzen; Kandidat behebt ihn.

    B wird erst am Kandidaten geschädigt. Damit messen Originaltests einen echten
    Gewinn in A und Verlust in B statt einer behaupteten Beschleunigung.
    """
    defekt, beschreibung_a = _lahmlegen(werk, paket, a, alle=True)
    geaendert = aegis.kandidat_dateien(werk, defekt)
    if not geaendert:
        raise RuntimeError("Ausgangsdefekt A nicht anwendbar")
    wiederherstellen = ""
    for p, code in geaendert.items():
        original = (werk / p).read_text()
        wiederherstellen += _diff(p, code, original)
        (werk / p).write_text(code)
    schaden_b, beschreibung_b = _lahmlegen(werk, paket, b)
    return (wiederherstellen + ("" if gegenprobe else schaden_b),
            f"A={a}: behebt privaten Ausgangsdefekt ({beschreibung_a}); "
            f"B={b}: {'unverändert (Gegenprobe)' if gegenprobe else beschreibung_b}",
            {"gewinnbereich": a, "verlustbereich": b, "basis_eingriff": geaendert}, None)


def _regression_vorbereiten(werk, paket, a, b, gegenprobe):
    diff, beschreibung, belege, _ = _nebenwirkung_vorbereiten(werk, paket, a, b, gegenprobe)
    gruen_diff, gruen_text = _gruene_tests(a)
    gruen = aegis.kandidat_dateien(werk, gruen_diff)
    testdateien = sorted(p.relative_to(werk).as_posix() for p in (werk / "tests").glob("test_*.py")
                        if p.name == f"test_{b}.py" or p.name.startswith(f"test_{b}_"))
    if not testdateien:
        raise RuntimeError(f"Keine Bereichstests für {b}: Regression nicht prüfbar")
    basis_tests = aegis.junit_lauf(werk, paket, gruen, testdateien + list(gruen))
    schaden, _ = _lahmlegen(werk, paket, b)
    schaden_tests = aegis.junit_lauf(werk, paket, aegis.kandidat_dateien(werk, schaden), testdateien)
    faelle = sorted(n for n, x in schaden_tests.items()
                    if not x["ok"] and x["bestaetigt"] and basis_tests.get(n, {}).get("ok"))
    if not faelle:
        raise RuntimeError(f"Kein bestätigter Einzeltest fällt durch den Eingriff in {b}")
    diff += gruen_diff
    kandidat_tests = aegis.junit_lauf(werk, paket, aegis.kandidat_dateien(werk, diff), testdateien + list(gruen))
    belege.update(regressionstest=faelle[0], basis_tests=basis_tests, kandidat_tests=kandidat_tests,
                  gruene_tests=sorted(n for n in kandidat_tests if n.split("::")[0] in gruen and not n.endswith("::*")))
    return diff, beschreibung + "; " + gruen_text, belege, None


def _vertrag_vorbereiten(werk, paket, a, b, vertrag_pfad, gegenprobe):
    datei, fn = next((d, f) for d, f in _funktionen(werk, paket, a) if f.col_offset == 0)
    quelle = datei.read_text()
    zeilen = quelle.splitlines()
    ziel = fn.body[0].end_lineno if ast.get_docstring(fn) is not None else fn.body[0].lineno - 1
    neu = zeilen[:ziel] + [f"    from {paket} import {b} as _eichlieferant",
                          "    if _eichlieferant.eichprobe_zusicherung() != 'da':",
                          "        raise ValueError('eichprobe_zusicherung fehlt')"] + zeilen[ziel:]
    rel = datei.relative_to(werk).as_posix()
    diff = _diff(rel, quelle, "\n".join(neu) + "\n")
    # Den vorhandenen Test im eigenen Modulkontext aufrufen: Konstanten,
    # Helfer und Imports gehören zu seiner Ausführung. Ein AST-Fragment aus
    # Imports + Funktion verliert diese Voraussetzungen; globale Namen aus
    # dem Verbrauchermodul dürfen auch nicht den alten Vertrag überschreiben.
    testpfad = f"tests/test_{a}.py"
    try:
        baum = ast.parse((werk / testpfad).read_text())
    except SyntaxError as fehler:
        raise RuntimeError(f"Verbrauchertest {testpfad}: Syntaxfehler — Vertragsprobe nicht baubar") from fehler
    test = next((k for k in baum.body if isinstance(k, ast.FunctionDef) and k.name.startswith("test_")
                 and not k.args.args and not k.args.posonlyargs and not k.args.kwonlyargs and not k.decorator_list
                 and any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == fn.name
                         for n in ast.walk(k))), None)
    if test is None:
        raise RuntimeError(f"Kein eigenständig ausführbarer Test für {rel}::{fn.name}")
    verbrauchertest = f"{testpfad}::{test.name}"
    vertragstest = "test_eichprobe_vertrag_neue_zusicherung"
    zusatz = (f"def {vertragstest}():\n"
              "    import runpy\n"
              f"    verbraucher = runpy.run_path({testpfad!r})\n"
              f"    verbraucher[{test.name!r}]()\n"
              f"    from {paket}.{b} import eichprobe_zusicherung\n"
              "    assert eichprobe_zusicherung() == 'da'\n")
    alt_vertrag = (werk / vertrag_pfad).read_text()
    diff += _diff(vertrag_pfad, alt_vertrag, alt_vertrag.rstrip() + "\n\n" + zusatz)
    if gegenprobe:
        lieferant = f"{paket}/{b}/__init__.py"
        alt = (werk / lieferant).read_text()
        diff += _diff(lieferant, alt, alt.rstrip() + "\n\n"
                      "def eichprobe_zusicherung():\n    return 'da'\n")
    dateien = aegis.kandidat_dateien(werk, diff)
    belege = {"verbrauchertest": verbrauchertest, "verbraucherdatei": rel, "vertragspfad": vertrag_pfad,
              "vertragstest": f"{Path(vertrag_pfad).name}::{vertragstest}",
              "basis_tests": aegis.junit_lauf(werk, paket, {}, [testpfad, vertrag_pfad]),
              "kandidat_tests": aegis.junit_lauf(werk, paket, dateien, [testpfad, vertrag_pfad])}
    return (diff, f"{vertrag_pfad}: {a}.{fn.name} fordert {b}.eichprobe_zusicherung(); "
            f"Lieferant {'angepasst (Gegenprobe)' if gegenprobe else 'NICHT angepasst'}", belege, None)


def _einzelprobe(con, lauf_id, werk_id, pfad, paket, bereiche, bstrassen, basis, ausgang, ref, tausch,
                 generation, gegenstand, name, gegenprobe=False):
    """Eine vollständig ausgeführte Positiv- oder Gegenprobe an isoliertem Bestand."""
    t0 = time.monotonic()
    with _privat(con, pfad) as (db, werk), kammer.zaehlung() as aufrufe:
        n0, c0 = _kassenstand(db, lauf_id)
        a, b = gegenstand["von_bereich"], gegenstand["nach_bereich"]
        if name == "norm":
            bereich = b
            diff, beschreibung, belege, angriff = _norm_vorbereiten(db, werk, werk_id, paket, b, gegenprobe)
        elif name == "nebenwirkung":
            bereich = a
            diff, beschreibung, belege, angriff = _nebenwirkung_vorbereiten(werk, paket, a, b, gegenprobe)
        elif name == "regression":
            bereich = a
            diff, beschreibung, belege, angriff = _regression_vorbereiten(werk, paket, a, b, gegenprobe)
        elif name == "vertrag":
            bereich = a
            diff, beschreibung, belege, angriff = _vertrag_vorbereiten(
                werk, paket, a, b, gegenstand["vertrag_pfad"], gegenprobe)
        else:
            raise ValueError(f"Noch keine Probe gebaut: {name}")
        dateien = aegis.kandidat_dateien(werk, diff)
        if not dateien:
            raise RuntimeError(aegis.diff_grund(werk, diff) or "kein anwendbarer Probediff")
        kid = _einschleusen(db, lauf_id, generation, bereich, diff, beschreibung,
                           gegenstand["vertrag_pfad"] if name == "vertrag" else "keine", name)
        belege["zielpruefsummen"] = {p: hashlib.sha256((werk / p).read_bytes()).hexdigest()
                                     for p in dateien if (werk / p).exists()}
        u = aegis.pruefen(db, lauf_id, werk_id, kid, werk, paket, bereiche, bstrassen, basis, ausgang, ref, tausch,
                          probe_ohne_modell=True, probe_angriff=angriff)
        messung = lj(db.execute("SELECT masse FROM kandidaten WHERE id=?", (kid,)).fetchone()[0]) or {}
        belege.update(urteil=u, messung=messung)
        if name == "norm":
            belege.update(werk_test_vorhanden=(werk / belege["testpfad"]).exists(),
                          normeintraege=[dict(z) for z in db.execute(
                              "SELECT name,status,code,ursprung FROM immunsystem WHERE name=?",
                              (f"norm_k{kid}_{bereich}",))])
        n1, c1 = _kassenstand(db, lauf_id)
        pruefbar = bool(messung.get("gueltig") and (messung.get("_basis_paar") or {}).get("gueltig"))
        if name == "vertrag":
            pruefbar = pruefbar and _vertrag_pruefbar(belege, gegenprobe)
        return {"kandidat": kid, "ausgefuehrt": bool(aufrufe), "pruefbar": pruefbar,
                "bestanden": _bestanden(name, belege), "belege": belege, "status": u["status"],
                "grund": u["grund"], "befund": beschreibung, "gegenprobe": gegenprobe, "diff": diff,
                "modellaufrufe": n1 - n0, "kosten_eur": round(c1 - c0, 6),
                "kammerlaeufe": len(aufrufe), "kammer": list(aufrufe),
                "dauer_s": round(time.monotonic() - t0, 3)}


def _leer(grund):
    return {"kandidat": None, "ausgefuehrt": False, "pruefbar": False, "bestanden": False,
            "grund": grund, "befund": grund, "belege": {}, "modellaufrufe": 0,
            "kosten_eur": 0.0, "kammerlaeufe": 0, "dauer_s": 0.0}


def _vollstaendig(positive, gegenproben):
    return (set(positive) == set(gegenproben) == set(PROBEN)
            and all(p.get("ausgefuehrt") is True and p.get("pruefbar") is True
                    and p.get("bestanden") is True for p in positive.values())
            and all(p.get("ausgefuehrt") is True and p.get("pruefbar") is True
                    and p.get("bestanden") is False for p in gegenproben.values()))


def proben(con: sqlite3.Connection, lauf_id: int, werk_id: int, pfad: Path, paket: str, bereiche: list[str],
           bstrassen, basis: dict, ausgang: dict, ref: str | None, tausch: dict, generation: int = 0) -> dict:
    """Vier Paare, ohne Modelle, ohne vorausgesetzten Freeze und ohne Rückschreiben.

    `basis`/`ausgang` sind explizite Messungen; laeufe.mass darf NULL sein. Die
    Rückgabe ist der Beleg für den Aufrufer, kein selbst erteiltes Startrecht.
    Sämtliche Versiegelungs-, Anklage-, Immun- und Kostenwrites bleiben privat.
    """
    with _privat(con, pfad) as (db, werk):
        gegenstand = eichgegenstand.sichern(db, werk_id, lauf_id, werk)
        g = gegenstand.get("gegenstand")
        if not g:
            grund = gegenstand.get("befund") or "kein Eichgegenstand"
            return {"bestanden": False, "grund": grund, "gegenstand": None, "lauf_startet": False,
                    "proben": {n: _leer(grund) for n in PROBEN},
                    "gegenproben": {n: _leer(grund) for n in PROBEN},
                    "kosten": {"kammerlaeufe": 0, "modellaufrufe": 0, "kosten_eur": 0.0, "dauer_s": 0.0}}
        positive, negative = {}, {}
        for name in PROBEN:
            for ist_gegenprobe, ziel in ((False, positive), (True, negative)):
                t0 = time.monotonic()
                with kammer.zaehlung() as aufrufe:
                    try:
                        ziel[name] = _einzelprobe(db, lauf_id, werk_id, werk, paket, bereiche, bstrassen,
                                                 basis, ausgang, ref, tausch, generation, g, name, ist_gegenprobe)
                    except (RuntimeError, ValueError, StopIteration, OSError, sqlite3.Error) as fehler:
                        # Kein ausgeführtes Gegenprädikat: ein ausdrücklich
                        # ungeprüfter Infrastruktur-/Fixturebefund sperrt Gesamtgrün.
                        ziel[name] = {**_leer(str(fehler) or type(fehler).__name__),
                                      "fehlerart": type(fehler).__name__, "status": "prueffehler",
                                      "kammerlaeufe": len(aufrufe), "kammer": list(aufrufe),
                                      "dauer_s": round(time.monotonic() - t0, 3)}
        alle = list(positive.values()) + list(negative.values())
        kosten = {k: sum(p[k] for p in alle) for k in ("kammerlaeufe", "modellaufrufe", "kosten_eur", "dauer_s")}
        ok = _vollstaendig(positive, negative)
        return {"bestanden": ok, "gegenstand": g, "proben": positive, "gegenproben": negative,
                "lauf_startet": ok, "kosten": kosten,
                "grund": None if ok else "Vier Positivtreffer und vier prüfbare negative Gegenproben erforderlich"}


def text(e: dict) -> list[str]:
    if not e.get("gegenstand"):
        return [f"Eichproben: NICHT GELAUFEN — {e.get('grund')}"]
    g = e["gegenstand"]
    zeilen = [f"Eichproben {g['von_bereich']}→{g['nach_bereich']} "
              f"({g['vertrag_pfad']}, SHA256 {g['vertrag_pruefsumme']}):"]
    for name in PROBEN:
        for gruppe, titel in (("proben", "Positivprobe"), ("gegenproben", "Gegenprobe")):
            p = e.get(gruppe, {}).get(name, _leer("fehlende Zeile"))
            zeilen.append(f"  {titel} {name}: ausgeführt={p['ausgefuehrt']}, prüfbar={p['pruefbar']}, "
                          f"Bestehensprädikat={p['bestanden']} | {p['kammerlaeufe']} Kammerläufe | "
                          f"{p['modellaufrufe']} Modellaufrufe | {p['kosten_eur']:.6f} €")
            zeilen.append(f"    Originalurteil: {p['grund']}")
            b = p.get("belege", {})
            m = b.get("urteil", {}).get("mass") or {}
            if name in ("nebenwirkung", "regression"):
                zeilen.append(f"    Pareto besser: {m.get('pareto_besser')}; schlechter: {m.get('pareto_schlechter')}")
            elif name == "norm":
                zeilen.append(f"    Norm: {b.get('urteil', {}).get('norm')}; Zuwachs: {m.get('zuwachs')}; "
                              f"Normeinträge: {[z['name'] for z in b.get('normeintraege', [])]}")
    k = e["kosten"]
    zeilen.append(f"SUMME gesamte Batterie: {k['kammerlaeufe']} Kammerläufe, "
                  f"{k['modellaufrufe']} Modellaufrufe, {k['kosten_eur']:.6f} €, {k['dauer_s']:.3f} s")
    if not e["bestanden"]:
        zeilen.append("LAUF STARTET NICHT: Batterie unvollständig oder falsches Prädikat.")
    return zeilen
