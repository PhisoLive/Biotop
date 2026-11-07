"""F7-Verbraucher: echte Eigenfixture-Kammerläufe + markierte Status-I/O-Doubles.

Kein Werkcode auf dem Host, keine produktiven Werke/DBs und keine Modellaufrufe.
Die Kammerzählung erfasst nur echte kammer.ausfuehren-Aufrufe, nicht I/O-Doubles.
"""
import json
import os
from pathlib import Path
from types import SimpleNamespace
import xml.etree.ElementTree as ET

import pytest

from biotop.kern import datenbank
from biotop.organe import fundpruefung as F, generation0 as G, kammer

EINS = "def test_eins():\n    assert 2 + 2 == 4\n"
ZWEI = EINS + "\ndef test_zwei():\n    assert 3 + 3 == 6\n"
SKIP = EINS + "\ndef test_zwei():\n    import pytest\n    pytest.skip('absichtlich nicht ausgeführt')\n"


@pytest.fixture(autouse=True)
def rohbelege(request):
    with kammer.zaehlung() as aufrufe:
        yield
    ziel = os.environ.get("NACHWEIS_BELEGE")
    if ziel:
        with (Path(ziel) / "kammer.jsonl").open("a") as f:
            for e in aufrufe:
                f.write(json.dumps({"test": request.node.nodeid, **e}, ensure_ascii=False) + "\n")
    print("ECHTE_KAMMERLAEUFE", request.node.nodeid, len(aufrufe))


@pytest.fixture
def eigenwerk(tmp_path):
    werk = tmp_path / "eigenwerk"
    (werk / "paket" / "alpha").mkdir(parents=True)
    (werk / "paket" / "__init__.py").write_text("")
    (werk / "paket" / "alpha" / "__init__.py").write_text("from .quelle import wert\n")
    (werk / "paket" / "alpha" / "quelle.py").write_text("def wert():\n    return 4\n")
    (werk / "tests").mkdir()
    (werk / "tests" / "test_alpha.py").write_text("from paket.alpha import wert\ndef test_wert():\n    assert wert() == 4\n")
    return werk


def io_ergebnis(status="gut", datei="tests/test_neubewertung_probe.py"):
    """Gestelltes Kammer-I/O, KEIN ausgeführter Werk-/JUnit-Nachweis."""
    root = ET.Element("testsuites")
    suite = ET.SubElement(root, "testsuite")
    for name in ("test_eins", "test_zwei"):
        if status in ("leer", "fehlender_test") and (status == "leer" or name == "test_zwei"):
            continue
        tc = ET.SubElement(suite, "testcase", classname=datei[:-3].replace("/", "."), name=name)
        if name == "test_zwei" and status in ("skip", "xfail", "error", "rot"):
            tag = {"skip": "skipped", "xfail": "skipped", "error": "error", "rot": "failure"}[status]
            ET.SubElement(tc, tag, message="AssertionError" if status == "rot" else status)
    xml = ET.tostring(root, encoding="unicode")
    summary = {"skip": "1 passed, 1 skipped", "xfail": "1 passed, 1 xfailed", "error": "1 passed, 1 error",
               "leer": "0 passed", "fehlender_test": "1 passed", "rot": "1 passed, 1 failed"}.get(status, "2 passed")
    stdout = summary + "\n@@NACHWEIS@@" + xml + "@@ENDE@@\n"
    if status == "fehlend":
        stdout = "2 passed\n"
    if status == "kaputtes_xml":
        stdout = "2 passed\n@@NACHWEIS@@<testsuites>@@ENDE@@\n"
    rc = {"abbruch": 124, "prozessfehler": 2, "rot": 1, "error": 1}.get(status, 0)
    return kammer.Ergebnis(rc, stdout, "", 0.0, status in ("abbruch", "zeitlimit_trotz_rc0"), "IO-DOUBLE")


def io_installieren(monkeypatch, ergebnis):
    def lauf(*args, **kwargs):
        print("KAMMER_IO_DOUBLE", json.dumps(ergebnis.__dict__, ensure_ascii=False))
        return ergebnis
    monkeypatch.setattr(kammer, "ausfuehren", lauf)


@pytest.mark.parametrize("status", ["skip", "xfail", "abbruch", "prozessfehler", "zeitlimit_trotz_rc0",
                                   "leer", "fehlend", "fehlender_test", "kaputtes_xml", "error"])
def test_fund_verweigert_nicht_ausgefuehrten_nachweis(monkeypatch, eigenwerk, status):
    io_installieren(monkeypatch, io_ergebnis(status))
    with pytest.raises(RuntimeError, match="Nachweis"):
        F._ausfuehren(eigenwerk, "probe", ZWEI)


@pytest.mark.integration
@pytest.mark.parametrize("code,besteht,absturz", [
    (ZWEI, True, False),
    ("def test_eins():\n    assert False\n", False, False),
    ("from paket.alpha import wert\ndef test_eins():\n    wert()\n", False, True),
])
def test_fund_ausgefuehrte_gegenrouten(eigenwerk, code, besteht, absturz):
    if absturz:
        (eigenwerk / "paket/alpha/quelle.py").write_text("def wert():\n    raise ValueError('Produktfehler')\n")
    assert F._ausfuehren(eigenwerk, "probe", code)[:2] == (besteht, absturz)


@pytest.mark.integration
def test_fund_echter_skip_ist_kein_bestandener_fundtest(eigenwerk):
    with pytest.raises(RuntimeError, match="Nachweis"):
        F._ausfuehren(eigenwerk, "probe", SKIP)


def test_fund_abbruch_mit_vertragsverweis_wird_nicht_zum_fund(monkeypatch, eigenwerk, tmp_path):
    con = datenbank.verbinden(tmp_path / "fund.db")
    con.execute("INSERT INTO immunsystem(werk_id, name, bereich, code, status) VALUES(1, 'probe', 'alpha', ?, 'offen_norm')", (ZWEI,))
    monkeypatch.setattr(F.verfassung, "lesen", lambda *a: {})
    monkeypatch.setattr(F.aegis, "_nennt_vertrag", lambda *a: True)
    io_installieren(monkeypatch, io_ergebnis("prozessfehler"))
    try:
        with pytest.raises(RuntimeError, match="Nachweis"):
            F.bewerten(con, 1, 1, eigenwerk)
        assert con.execute("SELECT status FROM immunsystem").fetchone()[0] == "offen_norm"
    finally:
        con.close()


def mutant(code="def wert():\n    return 5\n"):
    return dict(datei="paket/alpha/quelle.py", zeile=2, art="grenze", beschreibung="4 → 5", code=code)


@pytest.mark.parametrize("status", ["skip", "xfail", "abbruch", "prozessfehler", "zeitlimit_trotz_rc0",
                                   "leer", "fehlend", "kaputtes_xml", "error"])
def test_gen0_fang_braucht_ausgefuehrten_test(monkeypatch, eigenwerk, status):
    io_installieren(monkeypatch, io_ergebnis(status))
    with pytest.raises(RuntimeError, match="Nachweis"):
        G._testlauf(eigenwerk, {mutant()["datei"]: mutant()["code"]})


@pytest.mark.integration
@pytest.mark.parametrize("code", [SKIP, "", "raise ImportError('Sammelfehler')\n",
    EINS + "\ndef test_zwei():\n    import pytest\n    pytest.exit('Abbruch', returncode=2)\n"])
def test_gen0_fang_echte_nichtausfuehrung(eigenwerk, code):
    (eigenwerk / "tests/test_alpha.py").write_text(code)
    with pytest.raises(RuntimeError, match="Nachweis"):
        G._testlauf(eigenwerk, {})


@pytest.mark.integration
def test_gen0_fang_ausgefuehrte_gegenrouten(eigenwerk, tmp_path):
    con = datenbank.verbinden(tmp_path / "mutanten.db")
    try:
        m = mutant()
        r = G.messen(con, 1, 1, eigenwerk, [m], "vorher")
        assert r["gefangen"] == 1 and r["blind"] == []
        zeile = con.execute("SELECT gefangen_vorher, gefangen_von FROM mutanten").fetchone()
        assert zeile[0] == 1 and "test_wert" in zeile[1]
        m["code"] = "def wert():\n    return 4\n"
        r = G.messen(con, 1, 1, eigenwerk, [m], "nachher")
        assert r["gefangen"] == 0 and r["blind"] == [m]
        assert con.execute("SELECT gefangen_nachher FROM mutanten").fetchone()[0] == 0
    finally:
        con.close()
