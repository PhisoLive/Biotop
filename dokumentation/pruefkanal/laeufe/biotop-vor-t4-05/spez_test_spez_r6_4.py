"""R6-4 (eigener Befund nach der Kette, 24.09.): „Festhalten = fallende Zusicherung“ (Entscheidung 2) erkennt umgeschriebene
asserts ohne einfache Anführungszeichen nicht. pytest kürzt dort „AssertionError: “ aus reprcrash.message weg
(ExceptionInfo._striptext, wenn repr(e) mit "AssertionError('assert " beginnt) — gemessen in pytest 8.3.3 (Kammer) und
9.1.1 (proben/VORPROBE-E2b.txt). `_zusicherung_faellt` verlangt das Präfix: ein Test `assert f(1) == 3` hält nichts fest,
jede Abweichung, die nur er decken kann, bleibt ungedeckt — der Kandidat wird abgelehnt (T4-DIAGNOSE: 0 festhaltende
Tests für 5 von 8 geänderten Funktionen). Die Probe führt echtes pytest im Unterprozess aus (derselbe Mechanismus wie die
Sonde) und prüft `_zusicherung_faellt` aus dem Commit an jedem Bericht.
ROT an 0c2f058: zahl, liste, wahrheitswert. GRÜN (Gegenproben): text (mit Anführungszeichen), werk_ausnahme (nicht)."""
import importlib.util
import json
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

VH = Path("/root/biotop/biotop/kern/py/verhalten.py")
WERK = textwrap.dedent('''
    class V:
        def __eq__(self, o):
            return False

        def __bool__(self):
            return False

        def __repr__(self):
            return '<verfälscht>'


    def f(x):
        return V()


    def g(x):
        return x.strip()
''')
TESTS = textwrap.dedent('''
    from werk import f, g


    def test_zahl():
        assert f(1) == 3


    def test_liste():
        assert f(1) == [3, 2, 1]


    def test_wahrheitswert():
        assert f(1)


    def test_text():
        assert f(1) == 'a_b'


    def test_werk_ausnahme():
        assert g(f(1)) == 'a'
''')
PLUGIN = textwrap.dedent('''
    import importlib.util, json, os, sys
    sys.path.insert(0, os.path.dirname(__file__))
    spec = importlib.util.spec_from_file_location("vh", os.environ["VH_PFAD"])
    vh = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(vh)
    ERG = {}


    def pytest_runtest_logreport(report):
        if report.when == "call" and report.outcome == "failed":
            datei = report.nodeid.partition("::")[0]
            ERG[report.nodeid.split("::")[-1]] = vh._zusicherung_faellt(report, datei)


    def pytest_sessionfinish(session):
        with open(os.path.join(os.path.dirname(__file__), "erg.json"), "w") as fh:
            json.dump(ERG, fh)
''')


@pytest.fixture(scope="module")
def ergebnis(tmp_path_factory):
    d = tmp_path_factory.mktemp("e2b")
    (d / "tests").mkdir()
    (d / "werk.py").write_text(WERK)
    (d / "tests" / "test_arten.py").write_text(TESTS)
    (d / "conftest.py").write_text(PLUGIN)
    import os
    subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=no", "-o", "addopts=", "tests"],
                   cwd=d, capture_output=True, text=True, env={**os.environ, "VH_PFAD": str(VH), "PYTHONHASHSEED": "0"})
    return json.loads((d / "erg.json").read_text())


@pytest.mark.parametrize("fall,haelt", [("zahl", True), ("liste", True), ("wahrheitswert", True), ("text", True),
                                        ("werk_ausnahme", False)])
def test_r6_4_zusicherung_ohne_anfuehrungszeichen_haelt_fest(ergebnis, fall, haelt):
    assert f"test_{fall}" in ergebnis, ergebnis
    assert ergebnis[f"test_{fall}"] is haelt, (fall, ergebnis)
