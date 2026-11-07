"""Gezielter pytest-Lauf mit originaler Kammerzählung und unveränderten Rohbelegen."""
import contextlib
import hashlib
import json
import os
from pathlib import Path
import sys
import time

import pytest
from biotop.organe import eichproben, kammer
from biotop import anbieter

ROOT = Path('/root/reparatur-01/nachbesserung-01/vertrag')
SOURCE = Path(os.environ.get('EICH_TESTREPO', str(ROOT / 'repo'))).resolve()
assert SOURCE.is_relative_to(ROOT)
assert Path.cwd() == SOURCE
assert Path(eichproben.__file__) == SOURCE / 'biotop/organe/eichproben.py'
assert Path(os.environ['TMPDIR']) == ROOT / 'tmp'
assert Path(os.environ['BIOTOP_DB']).is_relative_to(ROOT)
assert os.environ['PYTHONPATH'] == f'{ROOT}/guard:{SOURCE}'
assert kammer.IMAGE == 'biotop-kammer:1'

label, *tests = sys.argv[1:]
out = ROOT / 'ausgaben' / label
assert not out.with_suffix('.json').exists(), 'Rohbelege nicht überschreiben'
os.environ['BIOTOP_VERTRAGSBELEGE'] = str(out) + '-zeugen'
paid = []

def verboten(*a, **kw):
    paid.append(str(kw.get('zweck', '')))
    raise AssertionError('Bezahlter Biotop-Aufruf verboten')

anbieter.aufrufen = verboten
# Bereits importierte Referenzen sind dieselbe verbotene Grenze, keine Ersatzurteile.
for module in list(sys.modules.values()):
    if getattr(module, '__name__', '').startswith('biotop.') and hasattr(module, 'aufrufen'):
        module.aufrufen = verboten

rows = []
class Ledger:
    offset = 0
    def pytest_runtest_logreport(self, report):
        rows.append(dict(nodeid=report.nodeid, phase=report.when, outcome=report.outcome,
                         kammer_start=self.offset, kammer_ende=len(calls), kammerlaeufe=len(calls)-self.offset))
        self.offset = len(calls)

t0 = time.monotonic()
args = ['-vv', '-s', '-p', 'no:cacheprovider', *tests,
        f'--basetemp={ROOT}/tmp/{label}', f'--junitxml={out}.xml']
with kammer.zaehlung() as calls, open(str(out)+'.stdout.txt', 'w') as stdout, open(str(out)+'.stderr.txt', 'w') as stderr:
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        print('PRIVATER RUNNER', json.dumps(dict(cwd=str(Path.cwd()), PYTHONPATH=os.environ['PYTHONPATH'],
              TMPDIR=os.environ['TMPDIR'], BIOTOP_DB=os.environ['BIOTOP_DB'], importiert=eichproben.__file__,
              image=kammer.IMAGE, argv=args)))
        rc = int(pytest.main(args, plugins=[Ledger()]))
result = dict(label=label, rc=rc, argv=args, cwd=str(Path.cwd()), dauer_s=time.monotonic()-t0,
              kammerlaeufe=len(calls), kammer=calls, phasen=rows, bezahlte_versuche=paid, kosten_eur=0,
              quell_sha256=hashlib.sha256(Path(eichproben.__file__).read_bytes()).hexdigest())
Path(str(out)+'.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ('kammer','phasen')}, ensure_ascii=False))
print('ERGEBNISSE', [(r['nodeid'], r['outcome']) for r in rows if r['phase']=='call'])
sys.exit(rc)
