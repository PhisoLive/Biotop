"""Fassung 7: ausgeführte Nachweise statt Abwesenheit von Fehlern.

Produkt-MESSSKRIPT, Werk-Tests und Scanner laufen ausschließlich in der Kammer.
Die optionale Belegablage erfasst echte Kammerzähler einschließlich Fehlversuchen.
"""
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
        huelle = ("from pathlib import Path\ntry:\n    exec(" + repr(M.MESSSKRIPT) + ")\nfinally:\n"
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
        name = re.sub(r"[^a-zA-Z0-9_.-]", "_", request.node.nodeid)
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
