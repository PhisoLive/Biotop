"""Kernmaß/Pareto werden auch bei umgekehrter Dateiauswahl zuerst geprüft."""
from pathlib import Path
import os
import subprocess
import sys


def test_kernmass_und_pareto_kommen_vor_rauschen():
    repo = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(repo)
    r = subprocess.run([sys.executable, "-m", "pytest", "--collect-only", "-q",
                        "tests/test_rauschmessung.py", "tests/test_kernmass_pareto.py"],
                       cwd=repo, env=env, text=True, capture_output=True, timeout=30)
    assert r.returncode == 0, r.stdout + r.stderr
    ids = [s for s in r.stdout.splitlines() if s.startswith("tests/") and "::" in s]
    kern = [i for i, s in enumerate(ids) if s.startswith("tests/test_kernmass_pareto.py::")]
    rauschen = [i for i, s in enumerate(ids) if s.startswith("tests/test_rauschmessung.py::")]
    assert kern and rauschen
    assert max(kern) < min(rauschen), ids
