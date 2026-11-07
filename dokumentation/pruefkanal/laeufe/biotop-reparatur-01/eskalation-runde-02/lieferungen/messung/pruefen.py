"""Lokaler, offline ausgeführter TDD-Belegtreiber; keine Produktintegration."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent
REPO = BASE.parent / "repo"
label, *args = sys.argv[1:]
ziel = BASE / "roh" / label
ziel.mkdir(parents=True, exist_ok=False)
env = dict(os.environ, PYTHONPATH=str(REPO) + os.pathsep + str(BASE), PYTHONDONTWRITEBYTECODE="1",
           TMPDIR=str(BASE.parent / "tmp"), MESSNACHWEIS_BELEGE=str(ziel / "kammer"), KAMMER_GESAMT=str(ziel / "kammer-gesamt"))
cmd = ["/root/reparatur-01/venv/bin/python", "-m", "pytest", "-p", "belege_plugin", *args,
       "--junitxml=" + str(ziel / "junit.xml")]
for name in ("biotop/kern/messgeraet.py", "tests/test_messnachweise.py"):
    p = ziel / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes((REPO / name).read_bytes())
t0 = time.time()
p = subprocess.run(cmd, cwd=REPO, env=env, capture_output=True, text=True)
(ziel / "stdout.txt").write_text(p.stdout)
(ziel / "stderr.txt").write_text(p.stderr)
junit = ET.parse(ziel / "junit.xml").getroot() if (ziel / "junit.xml").exists() else None
cases = list(junit.iter("testcase")) if junit is not None else []
summary = {"label": label, "befehl": cmd, "env": {k: env[k] for k in ("PYTHONPATH", "PYTHONDONTWRITEBYTECODE", "TMPDIR")},
           "rc": p.returncode, "start_epoch": t0, "dauer_s": time.time() - t0,
           "tests": len(cases), "failure": sum(x.find("failure") is not None for x in cases),
           "error": sum(x.find("error") is not None for x in cases),
           "skipped": sum(x.find("skipped") is not None for x in cases),
           "kammerlaeufe": sum(len(json.loads(f.read_text())["kammer"]) for f in (ziel / "kammer-gesamt").glob("*.json")),
           "modellaufrufe": 0, "modellkosten_eur": 0,
           "sha256": {name: hashlib.sha256((REPO / name).read_bytes()).hexdigest() for name in ("biotop/kern/messgeraet.py", "tests/test_messnachweise.py")}}
(ziel / "lauf.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(p.stdout)
print(p.stderr)
print(json.dumps(summary, ensure_ascii=False))
sys.exit(p.returncode)
