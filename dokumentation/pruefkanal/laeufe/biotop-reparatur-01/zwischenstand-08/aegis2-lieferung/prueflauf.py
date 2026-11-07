"""Fokussierter pytest-Lauf mit unveränderten Kammer-Rohbelegen; kein Modellzugriff."""
from contextlib import redirect_stdout, redirect_stderr
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch
import hashlib
import json
import os
import re
import runpy
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT / 'repo'
TMP = ROOT / 'tmp'
OUT = ROOT / 'lieferung' / 'laeufe' / sys.argv[1]
OUT.mkdir(parents=True, exist_ok=False)
assert Path.cwd() == REPO
assert os.environ['PYTHONPATH'] == str(REPO)
assert os.environ['PYTHONDONTWRITEBYTECODE'] == '1'
assert os.environ['PYTEST_DISABLE_PLUGIN_AUTOLOAD'] == '1'
assert Path(os.environ['TMPDIR']) == TMP
assert not TMP.is_relative_to(REPO)
os.environ['BIOTOP_VERTRAGSBELEGE'] = str(OUT / 'vertragszeilen')

from biotop import anbieter
from biotop.organe import aegis, eichproben, kammer
import pytest

assert Path(aegis.__file__).is_relative_to(REPO)
assert Path(eichproben.__file__).is_relative_to(REPO)
blocks = []


def gesperrt(*args, **kwargs):
    blocks.append('Anbieter oder Host-runpy angefordert')
    raise AssertionError(blocks[-1])


def audit(event, args):
    if event == 'socket.connect':
        blocks.append('Netz gesperrt')
        raise AssertionError(blocks[-1])
    if event == 'sqlite3.connect':
        path = str(args[0])
        if path != ':memory:' and not Path(path).resolve().is_relative_to(TMP):
            blocks.append('DB außerhalb Privat-TMP gesperrt')
            raise AssertionError(blocks[-1])


sys.addaudithook(audit)
args = ['-v', '-s', '--tb=short', f'--junitxml={OUT / "junit.xml"}',
        f'--basetemp={TMP / sys.argv[1]}', *sys.argv[2:]]
meta = dict(command=[sys.executable, str(Path(__file__).resolve()), *sys.argv[1:]],
            pytest_args=args, cwd=str(Path.cwd()), started=datetime.now(timezone.utc).isoformat(),
            environment={k: os.environ[k] for k in ('PYTHONPATH', 'PYTHONDONTWRITEBYTECODE',
                'PYTEST_DISABLE_PLUGIN_AUTOLOAD', 'TMPDIR', 'BIOTOP_DB', 'BIOTOP_VERTRAGSBELEGE')},
            source_sha256={p: hashlib.sha256((REPO / p).read_bytes()).hexdigest()
                           for p in ('biotop/organe/aegis.py', 'biotop/organe/eichproben.py',
                                     'tests/test_review_vertrag.py', 'tests/test_junit_zeugen.py')
                           if (REPO / p).exists()})
start = time.monotonic()
with (OUT / 'stdout.txt').open('w') as stdout, (OUT / 'stderr.txt').open('w') as stderr:
    with redirect_stdout(stdout), redirect_stderr(stderr), kammer.zaehlung() as calls:
        with patch.object(anbieter, '_schluessel', gesperrt), patch.object(runpy, 'run_path', gesperrt):
            rc = int(pytest.main(args))
meta.update(exit_code=rc, duration_s=time.monotonic() - start,
            finished=datetime.now(timezone.utc).isoformat(), kammerlaeufe=len(calls),
            unique_containers=len({c['container'] for c in calls}), blocked_attempts=blocks)
(OUT / 'execution.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
(OUT / 'kammer.json').write_text(json.dumps(calls, ensure_ascii=False, indent=2) + '\n')
for i, call in enumerate(calls, 1):
    case = OUT / 'kammer' / f'{i:03d}-{call["container"]}'
    case.mkdir(parents=True)
    (case / 'stdout.txt').write_text(call['stdout'])
    (case / 'stderr.txt').write_text(call['stderr'])
    (case / 'execution.json').write_text(json.dumps({k: v for k, v in call.items()
                                                   if k not in ('stdout', 'stderr')}, indent=2) + '\n')
    match = re.search(r'@@J@@(.*)@@E@@', call['stdout'], re.S)
    if match:
        (case / 'junit.xml').write_text(match.group(1))
print(json.dumps(meta, ensure_ascii=False, indent=2))
print((OUT / 'stdout.txt').read_text())
if (OUT / 'stderr.txt').stat().st_size:
    print('STDERR:', (OUT / 'stderr.txt').read_text())
sys.exit(rc)
