"""Fassung 7: ausgeführte Nachweise statt Abwesenheit von Fehlern.

Produkt-MESSSKRIPT, Werk-Tests und Scanner laufen ausschließlich in der Kammer.
Die optionale Belegablage erfasst echte Kammerzähler einschließlich Fehlversuchen.
"""
import hashlib
import json
import os
from pathlib import Path
import re

import pytest

from biotop.kern import messgeraet as M
from biotop.organe import kammer


GUTER_TEST = '''from pathlib import Path
from demo.alpha import wert

def test_wert():
    Path('/tmp/ausgefuehrt').write_text('test_wert')
    assert wert() == 1
'''


@pytest.fixture
def messen_werk(tmp_path, request):
    werk = tmp_path / "werk"
    (werk / "demo" / "alpha").mkdir(parents=True)
    (werk / "tests").mkdir()
    (werk / "demo" / "__init__.py").write_text("")
    (werk / "demo" / "alpha" / "__init__.py").write_text("def wert():\n    return 1\n")
    belege = []

    def messen(test=GUTER_TEST, dateien=None, ref=None, bereiche=None):
        (werk / "tests" / "test_alpha.py").write_text(test)
        # Nur Belegtransport: exakt das aktuelle Produkt-MESSSKRIPT ausführen,
        # anschließend JUnit und wirkliche Ausführungsmarker sichtbar halten.
        huelle = ("from pathlib import Path\nscript = " + repr(M.MESSSKRIPT) + "\ntry:\n    exec(script)\nfinally:\n"
                  "    print('@@PYTEST_RC@@' + str(globals().get('ergebnis', {}).get('werk', {}).get('pytest_rc')))\n"
                  "    for p in ['/tmp/junit.xml', '/tmp/junit-vor-eingriff.xml', '/tmp/ausgefuehrt', '/tmp/scanner-aufrufe']:\n"
                  "        f = Path(p)\n"
                  "        print('@@ROHDATEI@@' + p + ':' + (f.read_text() if f.exists() else '<fehlt>'))\n")
        extra = {"_messgeraet/messen.py": huelle, **(dateien or {})}
        with kammer.zaehlung() as aufrufe:
            ergebnis = M.messen(werk, bereiche or ["alpha"], "demo", ref, dateien=extra)
        belege.append({"test": test, "dateien": dateien or {}, "referenzlast": ref,
                       "ergebnis": ergebnis, "kammer": aufrufe})
        assert len(aufrufe) == 1, "kein ausgeführter Kammerlauf"
        return ergebnis, aufrufe[0]

    yield messen
    if os.environ.get("MESSNACHWEIS_BELEGE"):
        ziel = Path(os.environ["MESSNACHWEIS_BELEGE"])
        ziel.mkdir(parents=True, exist_ok=True)
        name = hashlib.sha256(request.node.nodeid.encode()).hexdigest()
        (ziel / (name + ".json")).write_text(json.dumps({"nodeid": request.node.nodeid,
            "versuche": belege, "kammer": [k for b in belege for k in b["kammer"]]}, indent=2))


def messausgabe(roh):
    m = re.search(r"@@MESSUNG@@(.*)@@ENDE@@", roh["stdout"], re.S)
    return json.loads(m.group(1)) if m else None


@pytest.mark.integration
@pytest.mark.parametrize("skip", ["@pytest.mark.skip(reason='keine Ausfuehrung')", "@pytest.mark.xfail(reason='nicht ausgefuehrt', run=False)"])
def test_skipped_junit_ist_keine_gueltige_messung(messen_werk, skip):
    test = GUTER_TEST.replace("def test_wert():", skip + "\ndef test_wert():")
    m, roh = messen_werk("import pytest\n" + test)
    assert "@@PYTEST_RC@@0" in roh["stdout"] and "<skipped" in roh["stdout"]
    assert "@@ROHDATEI@@/tmp/ausgefuehrt:<fehlt>" in roh["stdout"]
    assert m["gueltig"] is False, m
    assert "kernmass" not in m


@pytest.mark.integration
@pytest.mark.parametrize("erwartet", [1, 2])
def test_ausgefuehrter_erfolg_und_fehlschlag_bleiben_messbar(messen_werk, erwartet):
    m, roh = messen_werk(GUTER_TEST.replace("wert() == 1", f"wert() == {erwartet}"))
    assert m["gueltig"] is True, m
    assert "@@ROHDATEI@@/tmp/ausgefuehrt:test_wert" in roh["stdout"]
    assert "<testcase " in roh["stdout"] and "<skipped" not in roh["stdout"]
    assert m["werk"]["pytest_rc"] == (0 if erwartet == 1 else 1)
    b = m["bereiche"]["alpha"]
    assert b["tests_gesamt"] == 1
    assert b["tests_bestanden"] == (1 if erwartet == 1 else 0)
    assert b["tests_fehlgeschlagen"] == (0 if erwartet == 1 else 1)
    assert bool(m["werk"]["tests_fehlgeschlagen_liste"]) is (erwartet != 1)
    assert b["sicherheit_punkte"] == 0 and b["tote_funktionen"] == 0


def junit_eingriff(anweisung):
    return ("from pathlib import Path\nimport pytest\n"
            "@pytest.hookimpl(hookwrapper=True, tryfirst=True)\n"
            "def pytest_sessionfinish(session, exitstatus):\n"
            "    yield\n"
            "    p = Path('/tmp/junit.xml')\n"
            "    Path('/tmp/junit-vor-eingriff.xml').write_text(p.read_text())\n"
            "    " + anweisung + "\n")


@pytest.mark.integration
@pytest.mark.parametrize("anweisung", ["p.unlink()", "p.write_text('<testsuites/>')"])
def test_fehlendes_oder_leeres_junit_ist_rot(messen_werk, anweisung):
    m, roh = messen_werk(dateien={"tests/conftest.py": junit_eingriff(anweisung)})
    assert "@@PYTEST_RC@@0" in roh["stdout"]
    assert "@@ROHDATEI@@/tmp/junit-vor-eingriff.xml:<?xml" in roh["stdout"]
    assert "@@ROHDATEI@@/tmp/ausgefuehrt:test_wert" in roh["stdout"]
    assert m["gueltig"] is False, m


@pytest.mark.integration
@pytest.mark.parametrize("test,pytest_rc", [("", 5), ("raise RuntimeError('Sammlung abgebrochen')\n", 2),
    (GUTER_TEST + "\ndef test_z_abbruch():\n    raise KeyboardInterrupt()\n", 2),
    ("import os\nos._exit(0)\n", 0)])
def test_leer_oder_abgebrochen_ist_keine_messung(messen_werk, test, pytest_rc):
    m, roh = messen_werk(test)
    assert f"@@PYTEST_RC@@{pytest_rc}" in roh["stdout"]
    assert m["gueltig"] is False, m


@pytest.mark.integration
@pytest.mark.parametrize("art", ["maxfail", "exit1", "setupfehler", "sammlungsfehler"])
def test_teilabbruch_mit_pytest_rc1_bleibt_rot(messen_werk, art):
    dateien = {}
    if art == "maxfail":
        test = GUTER_TEST.replace("wert() == 1", "wert() == 2") + "\ndef test_z_nie():\n    assert True\n"
        dateien["pytest.ini"] = "[pytest]\naddopts = --maxfail=1\n"
    elif art == "exit1":
        test = GUTER_TEST + "\ndef test_z_nie():\n    import pytest\n    pytest.exit('Abbruch', returncode=1)\n"
    elif art == "setupfehler":
        test = GUTER_TEST
        dateien["tests/conftest.py"] = "import pytest\n@pytest.fixture(autouse=True)\ndef kaputt():\n    raise RuntimeError('Setup, Testkoerper nie ausgefuehrt')\n"
    else:
        test = GUTER_TEST
        dateien["pytest.ini"] = "[pytest]\naddopts = --continue-on-collection-errors\n"
        dateien["tests/test_alpha_kaputt.py"] = "raise RuntimeError('Sammlungsfehler')\n"
    m, roh = messen_werk(test, dateien)
    assert "@@PYTEST_RC@@1" in roh["stdout"]
    assert "<testcase " in roh["stdout"]
    assert m["gueltig"] is False, m


def scanner_double(modul, rc, out):
    """Gestellte Ausgabe, aber durch den echten Scanner-Subprozess eingespeist."""
    return {modul + ".py": "from pathlib import Path\nimport sys\n"
            f"with Path('/tmp/scanner-aufrufe').open('a') as f: f.write({modul!r} + ':' + repr(sys.argv) + '\\n')\n"
            f"print({out!r})\nsys.exit({rc})\n"}


_BANDIT_LEER = {"results": [], "errors": [], "metrics": {"_totals": {"loc": 2}, "demo/alpha/__init__.py": {"loc": 2}}}


@pytest.mark.integration
@pytest.mark.parametrize("rc,out", [(2, ""), (0, ""), (0, "kein JSON"), (0, "{}"),
    (2, json.dumps(_BANDIT_LEER)),
    (0, json.dumps({**_BANDIT_LEER, "errors": [{"filename": "demo/alpha", "reason": "abgebrochen"}]})),
    (0, json.dumps({**_BANDIT_LEER, "metrics": {}}))], ids=["rc2-leer", "rc0-leer", "kaputt", "feld-fehlt", "rc2", "scanfehler", "nichts-gescannt"])
def test_bandit_ohne_ausgefuehrten_scan_ist_nicht_sicherheit_null(messen_werk, rc, out):
    m, roh = messen_werk(dateien=scanner_double("bandit", rc, out))
    assert "@@ROHDATEI@@/tmp/scanner-aufrufe:bandit:" in roh["stdout"]
    assert "demo/alpha" in roh["stdout"]
    assert m["gueltig"] is False, m


@pytest.mark.integration
@pytest.mark.parametrize("modul", ["bandit", "vulture"])
def test_echte_scannerbefunde_bleiben_gueltige_negative_masse(messen_werk, modul):
    code = "def wert():\n    return eval('1')\n" if modul == "bandit" else "def wert():\n    return 1\ndef verwaist():\n    return 2\n"
    m, roh = messen_werk(dateien={"demo/alpha/__init__.py": code})
    assert m["gueltig"] is True, m
    assert "@@ROHDATEI@@/tmp/ausgefuehrt:test_wert" in roh["stdout"]
    b = m["bereiche"]["alpha"]
    if modul == "bandit":
        assert b["sicherheit_punkte"] > 0
        assert any(x["test"] == "B307" for x in b["sicherheit_befunde"])
    else:
        assert b["tote_funktionen"] == 1
        assert "verwaist" in b["tote_liste"][0]
    assert M.kernmass_f2(m) < 0


@pytest.mark.integration
@pytest.mark.parametrize("rc,out", [(1, ""), (2, ""), (3, ""), (0, "Scan abgebrochen"), (3, "Scan abgebrochen")])
def test_vulture_fehler_ist_nicht_tote_null(messen_werk, rc, out):
    m, roh = messen_werk(dateien=scanner_double("vulture", rc, out))
    assert "@@ROHDATEI@@/tmp/scanner-aufrufe:vulture:" in roh["stdout"]
    assert "demo/alpha" in roh["stdout"]
    assert m["gueltig"] is False, m


@pytest.mark.integration
def test_vulture_befund_anderer_art_bleibt_ausgefuehrte_null(messen_werk):
    code = "def wert():\n    nicht_benutzt = 10\n    return 1\n"
    m, roh = messen_werk(dateien={"demo/alpha/__init__.py": code})
    assert m["gueltig"] is True, m
    assert m["bereiche"]["alpha"]["tote_funktionen"] == 0
    assert "@@ROHDATEI@@/tmp/ausgefuehrt:test_wert" in roh["stdout"]


@pytest.mark.integration
def test_vulture_erkennt_unerreichbaren_code_ohne_funktionsbefund(messen_werk):
    m, roh = messen_werk(dateien={"demo/alpha/__init__.py": "def wert():\n    return 1\n    return 2\n"})
    assert m["gueltig"] is True, m
    assert m["bereiche"]["alpha"]["tote_funktionen"] == 0


def vollstaendige_ausgabe():
    """Deklarierter Unit-Double des Übertragungsformats, kein Ausführungsbeleg."""
    return {"bereiche": {"alpha": {"tests_bestanden": 1, "tests_fehlgeschlagen": 0,
        "tests_gesamt": 1, "sicherheit_punkte": 0, "tote_funktionen": 0, "groesste_funktion": 2}},
        "werk": {"baut": True, "pytest_rc": 0, "tests_fehlgeschlagen_liste": [], "bauzeit_ms": 20, "zyklen": 0}}


def uebertragung(monkeypatch, tmp_path, d, rc=0, zeitlimit=False, ref=None):
    stdout = "@@MESSUNG@@" + json.dumps(d) + "@@ENDE@@"
    monkeypatch.setattr(kammer, "ausfuehren", lambda *a, **k: kammer.Ergebnis(rc, stdout, "Unit-Double", 1., zeitlimit, "unit-kein-container"))
    return M.messen(tmp_path, ["alpha"], "demo", ref)


@pytest.mark.parametrize("rc", [1, 124, 137])
def test_abgebrochene_kammer_trotz_marker_ist_rot(monkeypatch, tmp_path, rc):
    m = uebertragung(monkeypatch, tmp_path, vollstaendige_ausgabe(), rc=rc)
    assert m["gueltig"] is False, m
    assert "kernmass" not in m


@pytest.mark.parametrize("fehlend", ["bereiche.alpha", "werk", "werk.baut", "werk.pytest_rc", "werk.tests_fehlgeschlagen_liste", "werk.zyklen", "werk.bauzeit_ms"])
def test_fehlende_pflichtmessung_im_marker_ist_rot(monkeypatch, tmp_path, fehlend):
    d = vollstaendige_ausgabe()
    keys = fehlend.split(".")
    z = d
    for key in keys[:-1]:
        z = z[key]
    del z[keys[-1]]
    m = uebertragung(monkeypatch, tmp_path, d)
    assert m["gueltig"] is False, m
    assert "kernmass" not in m
