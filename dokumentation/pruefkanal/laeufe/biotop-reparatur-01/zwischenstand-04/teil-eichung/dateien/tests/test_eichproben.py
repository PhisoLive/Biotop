"""Eichung: echte Kammerläufe, exakte Mechanismen und negative Kontrollen."""
from pathlib import Path
import inspect
import hashlib
import json
import os
import sqlite3
from copy import deepcopy

import pytest

from biotop.kern import datenbank, messgeraet
from biotop.organe import aegis, eichproben, kammer, vertraege, verfassung


@pytest.fixture
def werk(tmp_path):
    pfad = tmp_path / "werk"
    dateien = {
        "beispiel/__init__.py": "",
        "beispiel/lieferant/__init__.py": "from .rechnung import wert\n",
        "beispiel/lieferant/rechnung.py": (
            '"""Ein kleiner Lieferant im kopierten Prüfwerk."""\n'
            "def wert(zahl: float) -> float:\n"
            '    """Verdoppelt eine Zahl."""\n'
            "    ergebnis = zahl * 2\n"
            "    return ergebnis\n"
        ),
        "tests/test_lieferant.py": (
            "from beispiel.lieferant import wert\n\n"
            "def test_wert():\n"
            "    assert wert(2) == 4\n"
        ),
    }
    for rel, code in dateien.items():
        ziel = pfad / rel
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_text(code)
    return pfad


@pytest.fixture
def paar(werk, tmp_path):
    dateien = {
        "beispiel/abnehmer/__init__.py": "from .ausgabe import bericht\n",
        "beispiel/abnehmer/ausgabe.py": (
            "def bericht(zahl: float) -> float:\n"
            '    """Berichtet einen Zahlenwert."""\n'
            "    ergebnis = zahl + 1\n"
            "    return ergebnis\n"
        ),
        "tests/test_abnehmer.py": (
            "from beispiel.abnehmer import bericht\n\n"
            "def test_bericht():\n"
            "    assert bericht(2) == 3\n"
        ),
    }
    for rel, code in dateien.items():
        ziel = werk / rel
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_text(code)
    con = datenbank.verbinden(tmp_path / "paar.db")
    con.executescript(verfassung.SCHEMA)
    con.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status,mass) VALUES(1,1,0,'angelegt',NULL)")
    vertragsdatei = vertraege.einlegen(con, 1, werk, {("abnehmer", "lieferant"): (
        "from beispiel.lieferant import wert\n\n"
        "def test_grenzwert():\n"
        "    assert wert(2) == 4\n"
    )}, "isolierte Testfixture")[0]
    bereiche = ["abnehmer", "lieferant"]
    basis = messgeraet.messen(werk, bereiche, "beispiel", None)
    g = {"von_bereich": "abnehmer", "nach_bereich": "lieferant", "vertrag_pfad": vertragsdatei}
    yield con, werk, bereiche, basis, g
    con.close()


@pytest.mark.parametrize("gegenprobe", [False, True])
def test_nebenwirkung_braucht_gewinn_a_und_verlust_b(paar, gegenprobe):
    con, werk, bereiche, basis, g = paar
    e = eichproben._einzelprobe(con, 1, 1, werk, "beispiel", bereiche, [], basis, basis, None, {}, 0,
                               g, "nebenwirkung", gegenprobe)
    print("NEBENWIRKUNG", gegenprobe, e["bestanden"], e["grund"])
    assert e["ausgefuehrt"] is True and e["pruefbar"] is True
    assert e["bestanden"] is (not gegenprobe)
    m = e["belege"]["urteil"]["mass"]
    assert any(s.startswith("abnehmer.tests_fehlgeschlagen:") for s in m["pareto_besser"])
    assert any(s.startswith("lieferant.tests_fehlgeschlagen:") for s in m["pareto_schlechter"]) is (not gegenprobe)
    falsch = deepcopy(e["belege"])
    falsch["urteil"]["mass"]["pareto_besser"] = []
    assert eichproben._bestanden("nebenwirkung", falsch) is False


def test_nebenwirkung_gewinnt_auch_bei_rueckwirkung_von_b_auf_a(paar):
    con, werk, bereiche, _, g = paar
    rel = "beispiel/abnehmer/ausgabe.py"
    (werk / rel).write_text(
        "from beispiel.lieferant import wert\n"
        "def bericht(zahl: float):\n"
        "    return wert(zahl)\n"
        "def zusatz(zahl: float):\n"
        "    return zahl + 1\n"
    )
    (werk / "tests/test_abnehmer.py").write_text(
        "from beispiel.abnehmer.ausgabe import bericht, zusatz\n"
        "def test_bericht():\n    assert bericht(2) == 4\n"
        "def test_zusatz():\n    assert zusatz(2) == 3\n"
    )
    basis = messgeraet.messen(werk, bereiche, "beispiel", None)
    e = eichproben._einzelprobe(con, 1, 1, werk, "beispiel", bereiche, [], basis, basis, None, {}, 0,
                               g, "nebenwirkung", False)
    assert e["bestanden"] is True, e["belege"]["urteil"]["mass"]


@pytest.mark.parametrize("gegenprobe", [False, True])
def test_regression_nennt_einzeltest_trotz_ausgefuehrter_gruener_tests(paar, gegenprobe):
    con, werk, bereiche, basis, g = paar
    e = eichproben._einzelprobe(con, 1, 1, werk, "beispiel", bereiche, [], basis, basis, None, {}, 0,
                               g, "regression", gegenprobe)
    print("REGRESSION", gegenprobe, e["bestanden"], e["grund"])
    assert e["ausgefuehrt"] is True and e["pruefbar"] is True
    assert e["bestanden"] is (not gegenprobe)
    b = e["belege"]
    assert len(b["gruene_tests"]) >= 3
    assert all(b["kandidat_tests"][n]["ok"] for n in b["gruene_tests"])
    assert b["basis_tests"][b["regressionstest"]]["ok"] is True
    assert b["kandidat_tests"][b["regressionstest"]]["ok"] is gegenprobe
    falsch = deepcopy(b)
    falsch["urteil"]["mass"]["pareto_schlechter"] = ["lieferant.tests_fehlgeschlagen: 0 → 1"]
    assert eichproben._bestanden("regression", falsch) is False
    falsch = deepcopy(b)
    falsch["gruene_tests"] = []
    assert eichproben._bestanden("regression", falsch) is False


@pytest.mark.parametrize("gegenprobe", [False, True])
def test_vertrag_braucht_konkreten_bruch_und_ausgefuehrten_konsumenten(paar, gegenprobe):
    con, werk, bereiche, basis, g = paar
    e = eichproben._einzelprobe(con, 1, 1, werk, "beispiel", bereiche, [], basis, basis, None, {}, 0,
                               g, "vertrag", gegenprobe)
    print("VERTRAG", gegenprobe, e["bestanden"], e["grund"])
    assert e["ausgefuehrt"] is True and e["pruefbar"] is True
    assert e["bestanden"] is (not gegenprobe)
    b = e["belege"]
    assert b["basis_tests"][b["verbrauchertest"]]["ok"] is True
    assert b["kandidat_tests"][b["verbrauchertest"]]["ok"] is gegenprobe
    assert (b["vertragstest"] in b["urteil"]["vertrag_verletzt"]) is (not gegenprobe)
    falsch = deepcopy(b)
    falsch["urteil"]["vertrag_verletzt"] = ["test_vertrag_fremder.py::test_fremd"]
    assert eichproben._bestanden("vertrag", falsch) is False
    falsch = deepcopy(b)
    falsch["urteil"]["grund"] = "Diff nicht anwendbar"
    assert eichproben._bestanden("vertrag", falsch) is False


def test_vier_paare_ohne_freeze_und_ohne_spuren_im_original(paar):
    con, werk, bereiche, basis, _ = paar
    vor_db = list(con.iterdump())
    vor_werk = {p.relative_to(werk).as_posix(): p.read_bytes() for p in werk.rglob("*") if p.is_file()}
    with kammer.zaehlung() as zaehler:
        e = eichproben.proben(con, 1, 1, werk, "beispiel", bereiche, [], basis, basis, None, {})
    assert set(e["proben"]) == set(e["gegenproben"]) == set(eichproben.PROBEN)
    assert e["bestanden"] is True
    for name in eichproben.PROBEN:
        assert e["proben"][name]["ausgefuehrt"] and e["proben"][name]["pruefbar"]
        assert e["proben"][name]["bestanden"] is True
        assert e["gegenproben"][name]["ausgefuehrt"] and e["gegenproben"][name]["pruefbar"]
        assert e["gegenproben"][name]["bestanden"] is False
    assert e["kosten"]["kammerlaeufe"] == len(zaehler)
    zeilen = eichproben.text(e)
    assert sum("Gegenprobe" in z for z in zeilen) == 4
    assert any(f"{len(zaehler)} Kammerläufe" in z for z in zeilen)
    print("VIER PAARE", [(n, e["proben"][n]["bestanden"], e["gegenproben"][n]["bestanden"]) for n in eichproben.PROBEN], e["kosten"])
    falsch = deepcopy(e)
    falsch["gegenproben"].pop("norm")
    assert eichproben._vollstaendig(falsch["proben"], falsch["gegenproben"]) is False
    falsch = deepcopy(e)
    falsch["gegenproben"]["norm"]["pruefbar"] = False
    assert eichproben._vollstaendig(falsch["proben"], falsch["gegenproben"]) is False
    assert list(con.iterdump()) == vor_db
    assert {p.relative_to(werk).as_posix(): p.read_bytes() for p in werk.rglob("*") if p.is_file()} == vor_werk


def test_unbaubare_probe_bleibt_ungeprueft_statt_erwuenscht_falsch(paar):
    con, werk, bereiche, basis, _ = paar
    p = werk / "beispiel/lieferant/rechnung.py"
    p.write_text(p.read_text().replace("zahl: float", "zahl: object"))
    vor_db = list(con.iterdump())
    with kammer.zaehlung() as zaehler:
        e = eichproben.proben(con, 1, 1, werk, "beispiel", bereiche, [], basis, basis, None, {})
    assert e["bestanden"] is False
    assert e["gegenproben"]["norm"]["pruefbar"] is False
    assert e["gegenproben"]["norm"]["ausgefuehrt"] is False
    assert e["gegenproben"]["norm"]["fehlerart"] == "RuntimeError"
    assert e["kosten"]["kammerlaeufe"] == len(zaehler)
    assert list(con.iterdump()) == vor_db


def test_fehlender_gegenstand_ist_keine_bestandene_gegenprobe(paar):
    con, werk, bereiche, basis, g = paar
    (werk / g["vertrag_pfad"]).unlink()
    vor_db = list(con.iterdump())
    e = eichproben.proben(con, 1, 1, werk, "beispiel", bereiche, [], basis, basis, None, {})
    assert list(con.iterdump()) == vor_db, "Selbst Versiegelungsnebenwirkungen müssen isoliert bleiben"
    assert e["bestanden"] is False and e["lauf_startet"] is False
    assert set(e["gegenproben"]) == set(eichproben.PROBEN)
    assert not any(p["ausgefuehrt"] or p["pruefbar"] for p in e["gegenproben"].values())


@pytest.mark.skipif(not os.environ.get("BIOTOP_EICHWERK"), reason="Private Werk-/DB-Kopie nicht angegeben")
def test_vier_paare_am_kopierten_pruefwerk(tmp_path):
    quelle = Path(os.environ["BIOTOP_EICHWERK"])
    dbquelle = Path(os.environ["BIOTOP_EICHDB"])
    # Dieser Abnahmetest arbeitet ausschließlich mit vorher angelegten Privatkopien.
    assert str(quelle.resolve()).startswith("/root/reparatur-01/")
    assert str(dbquelle.resolve()).startswith("/root/reparatur-01/")
    original_db_hash = hashlib.sha256(dbquelle.read_bytes()).hexdigest()
    werk = tmp_path / "werk"
    kammer._kopie(quelle, werk)
    con = sqlite3.connect(tmp_path / "privat.db", isolation_level=None)
    con.row_factory = sqlite3.Row
    with sqlite3.connect(f"file:{dbquelle}?mode=ro", uri=True) as original:
        original.backup(con)
    werk_id = int(os.environ.get("BIOTOP_EICHWERK_ID", "22"))
    con.execute("UPDATE werke SET pfad=? WHERE id=?", (str(werk), werk_id))
    lauf_id = con.execute("SELECT COALESCE(MAX(id),0)+1 FROM laeufe").fetchone()[0]
    con.execute("INSERT INTO laeufe(id,werk_id,status,budget_eur,mass) VALUES(?,?,'angelegt',0,NULL)", (lauf_id, werk_id))
    bereiche = sorted(p.name for p in (werk / "lagerhaus").iterdir() if p.is_dir() and (p / "__init__.py").exists())
    regeln = verfassung.lesen(con, werk_id)["regeln"]
    ref = Path("biotop/kern/referenzlast/lagerhaus.py").read_text()
    basis = messgeraet.messen(werk, bereiche, "lagerhaus", ref)
    assert basis["gueltig"]
    vor_db = hashlib.sha256("\n".join(con.iterdump()).encode()).hexdigest()
    vor_werk = {p.relative_to(werk).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in werk.rglob("*") if p.is_file()}
    with kammer.zaehlung() as zaehler:
        e = eichproben.proben(con, lauf_id, werk_id, werk, "lagerhaus", bereiche,
                             [("bericht", "preise"), ("bericht", "lager"), ("preise", "formeln")],
                             basis, basis, ref, regeln.get("tausch", {}))
    e["abnahme"] = {"werkquelle": str(quelle), "quell_db_sha256": original_db_hash,
                    "privater_lauf": lauf_id, "original_lauf_nicht_fortgesetzt": True,
                    "basis": basis, "werk_sha256_vor": vor_werk,
                    "werk_sha256_nach": {p.relative_to(werk).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in werk.rglob("*") if p.is_file()},
                    "db_sha256_vor": vor_db, "db_sha256_nach": hashlib.sha256("\n".join(con.iterdump()).encode()).hexdigest()}
    ziel = Path(os.environ["BIOTOP_EICHBELEG"])
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(json.dumps(e, ensure_ascii=False, indent=2))
    for name in eichproben.PROBEN:
        for gruppe in ("proben", "gegenproben"):
            z = e[gruppe][name]
            print("ECHTES WERK", name, gruppe, z["bestanden"], z["pruefbar"], z["grund"])
            print("MASS", z["belege"].get("urteil", {}).get("mass"))
    assert e["kosten"]["kammerlaeufe"] == len(zaehler)
    assert e["bestanden"] is True, str(ziel)
    assert e["abnahme"]["werk_sha256_vor"] == e["abnahme"]["werk_sha256_nach"]
    assert e["abnahme"]["db_sha256_vor"] == e["abnahme"]["db_sha256_nach"]
    assert hashlib.sha256(dbquelle.read_bytes()).hexdigest() == original_db_hash
    con.close()


def test_norm_aendert_vorhandene_funktion_statt_importfehler(werk):
    diff, rel_test, _ = eichproben._normtest(werk, "beispiel", "lieferant")
    dateien = aegis.kandidat_dateien(werk, diff)
    assert dateien is not None
    basis = aegis.junit_lauf(werk, "beispiel", {rel_test: dateien[rel_test]}, [rel_test])
    kandidat = aegis.junit_lauf(werk, "beispiel", dateien, [rel_test])
    print("NORM BASIS", basis, "NORM KANDIDAT", kandidat)
    echte_tests = [x for n, x in basis.items() if not n.endswith("::*")]
    assert len(echte_tests) == 1
    assert echte_tests[0]["bestaetigt"] is True, "Norm braucht eine Assertion, keinen Importfehler"
    assert echte_tests[0]["meldung"].startswith(("AssertionError", "assert"))
    assert not echte_tests[0].get("ort", "").startswith("beispiel/")
    assert all(x["ok"] for x in kandidat.values())
    assert all((werk / p).is_file() for p in dateien if not p.startswith("tests/"))
    assert not (werk / rel_test).exists()


@pytest.mark.parametrize("gegenprobe", [False, True])
def test_normmechanik_bleibt_getrennt_vom_tatsaechlichen_laufzeitbefund(werk, tmp_path, gegenprobe):
    con = datenbank.verbinden(tmp_path / "normzeit.db")
    ref = ("import sys, time\nsys.path.insert(0, '/werk')\nfrom beispiel.lieferant import wert\n"
           "def last_lieferant():\n"
           "    time.sleep(0.04 if wert(137.125) == 'eichprobe_norm_neu' else 0.01)\n")
    basis = messgeraet.messen(werk, ["lieferant"], "beispiel", ref)
    e = eichproben._einzelprobe(con, 1, 1, werk, "beispiel", ["lieferant"], [], basis, basis, ref, {}, 0,
                               {"von_bereich": "abnehmer", "nach_bereich": "lieferant"}, "norm", gegenprobe)
    print("NORM MIT ECHTEM ZEITBEFUND", gegenprobe, e["grund"])
    assert e["belege"]["urteil"]["mass"]["grenzen_gerissen"]
    assert e["belege"]["urteil"]["mass"]["zuwachs"] == 0
    assert e["bestanden"] is (not gegenprobe)
    con.close()


def test_norm_erreicht_vorhandene_methode_ohne_paarwechsel(werk):
    (werk / "beispiel/lieferant/__init__.py").write_text("from .rechnung import Rechner\n")
    (werk / "beispiel/lieferant/rechnung.py").write_text(
        "class Rechner:\n"
        "    def __init__(self, start=0):\n"
        "        self.start = start\n"
        "    def wert(self, zahl: float):\n"
        "        return self.start + zahl\n"
    )
    diff, testpfad, _ = eichproben._normtest(werk, "beispiel", "lieferant")
    dateien = aegis.kandidat_dateien(werk, diff)
    basis = aegis.junit_lauf(werk, "beispiel", {testpfad: dateien[testpfad]}, [testpfad])
    kandidat = aegis.junit_lauf(werk, "beispiel", dateien, [testpfad])
    assert len(basis) == len(kandidat) == 1
    assert next(iter(basis.values()))["meldung"].startswith(("AssertionError", "assert"))
    assert all(x["ok"] for x in kandidat.values())


def test_kleiner_eingriff_in_grosse_datei_ist_keine_neuschreibung(werk):
    rel = "beispiel/lieferant/rechnung.py"
    alt = (werk / rel).read_text() + "\n".join(f"# Eichzeile {n}" for n in range(130)) + "\n"
    (werk / rel).write_text(alt)
    neu = alt.replace("zahl * 2", "zahl * 3")
    diff = eichproben._diff(rel, alt, neu)
    dateien = aegis.kandidat_dateien(werk, diff)
    assert dateien is not None, aegis.diff_grund(werk, diff)
    assert dateien[rel] == neu


@pytest.mark.parametrize("ist_probe", [False, True])
def test_reine_probeoption_ist_markiert_und_erreicht_originale_norm(werk, tmp_path, ist_probe):
    assert "probe_ohne_modell" in inspect.signature(aegis.pruefen).parameters, "Explizite, geschützte Probeoption fehlt"
    con = datenbank.verbinden(tmp_path / "probe.db")
    diff, rel_test, _ = eichproben._normtest(werk, "beispiel", "lieferant")
    dateien = aegis.kandidat_dateien(werk, diff)
    kid = eichproben._einschleusen(con, 1, 0, "lieferant", diff, "Norm-Eichung", "keine", "norm")
    if not ist_probe:
        con.execute("UPDATE kandidaten SET ist_probe=0 WHERE id=?", (kid,))
        with pytest.raises(ValueError, match="ist_probe"):
            aegis.pruefen(con, 1, 1, kid, werk, "beispiel", ["lieferant"], [], {}, {}, None, {},
                          probe_ohne_modell=True)
        con.close()
        return
    basis = messgeraet.messen(werk, ["lieferant"], "beispiel", None)
    u = aegis.pruefen(con, 1, 1, kid, werk, "beispiel", ["lieferant"], [], basis, basis, None, {},
                      probe_ohne_modell=True, probe_angriff=dateien[rel_test])
    print("REINE NORM", u)
    assert u["norm"]
    assert isinstance(u["mass"], dict) and u["mass"]["zuwachs"] == 0
    immun = con.execute("SELECT status,code FROM immunsystem").fetchall()
    assert len(immun) == 1 and immun[0]["status"] == "offen_norm"
    assert "test_lieferant_eichprobe_norm" in immun[0]["code"]
    m = datenbank.lj(con.execute("SELECT masse FROM kandidaten WHERE id=?", (kid,)).fetchone()[0])
    assert rel_test not in m["_dateien"]
    assert con.execute("SELECT COUNT(*) FROM kasse").fetchone()[0] == 0
    con.close()


def test_kammerzaehlung_misst_auch_verschachtelte_aufrufe(werk):
    assert hasattr(kammer, "zaehlung"), "Kammerzählung fehlt; Konstante 1 ist kein Zähler"
    with kammer.zaehlung() as aussen:
        assert aussen == []
        with kammer.zaehlung() as innen:
            assert kammer.ausfuehren(werk, ["python", "-c", "print('erster')"]).rc == 0
        assert kammer.ausfuehren(werk, ["python", "-c", "print('zweiter')"]).rc == 0
    assert len(innen) == 1 and len(aussen) == 2
    assert len({z["container"] for z in aussen}) == 2
    assert [z["stdout"].strip() for z in aussen] == ["erster", "zweiter"]
    with kammer.zaehlung() as danach:
        assert danach == []


@pytest.mark.parametrize("gegenprobe", [False, True])
def test_norm_paar_schliesst_falsch_gruen_ohne_normpfad_aus(werk, tmp_path, gegenprobe):
    assert hasattr(eichproben, "_einzelprobe"), "Isolierte, beweisgebundene Probe fehlt"
    con = datenbank.verbinden(tmp_path / "original.db")
    vor_db = list(con.iterdump())
    vor_werk = {p.relative_to(werk).as_posix(): p.read_bytes() for p in werk.rglob("*") if p.is_file()}
    basis = messgeraet.messen(werk, ["lieferant"], "beispiel", None)
    with kammer.zaehlung() as zaehler:
        e = eichproben._einzelprobe(con, 1, 1, werk, "beispiel", ["lieferant"], [], basis, basis, None, {}, 0,
                                   {"von_bereich": "abnehmer", "nach_bereich": "lieferant"}, "norm", gegenprobe)
    print("NORM PAAR", gegenprobe, e["bestanden"], e["grund"], e["kammerlaeufe"])
    assert e["ausgefuehrt"] is True and e["pruefbar"] is True
    assert e["bestanden"] is (not gegenprobe)
    assert e["kammerlaeufe"] == len(zaehler) and len(zaehler) > 1
    assert e["modellaufrufe"] == 0 and e["kosten_eur"] == 0
    assert e["belege"]["urteil"]["mass"]["zuwachs"] == 0
    if gegenprobe:
        assert e["belege"]["urteil"]["norm"] == []
        assert e["belege"]["normeintraege"] == []
    else:
        for feld, wert in (("mass", None), ("mass", {}), ("norm", [])):
            falsch = deepcopy(e["belege"])
            falsch["urteil"][feld] = wert
            assert eichproben._bestanden("norm", falsch) is False
        falsch = deepcopy(e["belege"])
        falsch["normeintraege"] = []
        assert eichproben._bestanden("norm", falsch) is False
        falsch = deepcopy(e["belege"])
        falsch["werk_test_vorhanden"] = True
        assert eichproben._bestanden("norm", falsch) is False
    assert list(con.iterdump()) == vor_db
    assert {p.relative_to(werk).as_posix(): p.read_bytes() for p in werk.rglob("*") if p.is_file()} == vor_werk
    con.close()
