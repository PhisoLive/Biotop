"""Review vor T4-05 — lokale Probe zu Entscheidung 2 (ohne Kammer): Was liefert pytest als reprcrash.message für
gewöhnliche Zusicherungen ohne Anführungszeichen, und was sagt die Regel am Stand HEAD (_zusicherung_faellt)?"""
import os
import subprocess
import sys
from pathlib import Path

D = Path('/tmp/review-vor-t4-05/e2b')
(D / 'tests').mkdir(parents=True, exist_ok=True)
(D / 'conftest.py').write_text(
    "import importlib.util, os\n"
    "spec = importlib.util.spec_from_file_location('vh', '/tmp/review-vor-t4-05/verhalten_head.py')\n"
    "vh = importlib.util.module_from_spec(spec); spec.loader.exec_module(vh)\n\n\n"
    "def pytest_runtest_logreport(report):\n"
    "    if report.when == 'call' and report.outcome == 'failed':\n"
    "        c = report.longrepr.reprcrash\n"
    "        datei = report.nodeid.split('::')[0]\n"
    "        print(f\"\\n@@ {report.nodeid.split('::')[-1]} | path={os.path.basename(str(c.path))} | \"\n"
    "              f\"msg={str(c.message)[:40]!r} | haelt_fest={vh._zusicherung_faellt(report, datei)}\")\n")
(D / 'tests' / 'test_formen.py').write_text(
    "def f(x):\n    return x + 1\n\n\n"
    "def test_zahl():\n    assert f(1) == 3\n\n\n"
    "def test_liste():\n    assert [f(1)] == [3]\n\n\n"
    "def test_wahr():\n    assert f(1) > 5\n\n\n"
    "def test_text_mit_anfuehrung():\n    assert str(f(1)) == 'drei'\n\n\n"
    "def test_mit_meldung():\n    assert f(1) == 3, 'zwei statt drei'\n")
p = subprocess.run([sys.executable, '-m', 'pytest', '-q', '-s', '-p', 'no:cacheprovider', 'tests'], cwd=D,
                   capture_output=True, text=True, env={**os.environ, 'TMPDIR': '/tmp/review-vor-t4-05'})
print('\n'.join(z for z in p.stdout.splitlines() if z.startswith('@@') or 'passed' in z or 'failed' in z))
v = subprocess.run([sys.executable, '-m', 'pytest', '--version'], capture_output=True, text=True)
print((v.stdout + v.stderr).strip())
