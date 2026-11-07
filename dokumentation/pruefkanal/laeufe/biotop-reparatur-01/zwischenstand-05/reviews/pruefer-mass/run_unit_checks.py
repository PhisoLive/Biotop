"""Read-only review runner: selected unit checks only, no chambers/models/network."""
import os
import sys
from pathlib import Path

ROOT = Path('/root/reparatur-01/review-01')
OUT = ROOT / 'pruefer-mass'
TMP = OUT / 'tmp-unit'
TMP.mkdir(exist_ok=True)
os.environ['TMPDIR'] = str(TMP)
os.environ['BIOTOP_DB'] = str(TMP / 'unused-default.db')
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'repo'))

def no_external(*a, **kw):
    raise AssertionError('Reviewer guard: no chamber/model/network execution')

def audit(event, args):
    if event == 'subprocess.Popen':
        raise AssertionError('Reviewer guard: no subprocesses in selected unit checks')
sys.addaudithook(audit)

import socket
socket.socket.connect = no_external
socket.create_connection = no_external
from biotop import anbieter
from biotop.organe import kammer, aegis
kammer.ausfuehren = no_external
kammer._ausfuehren = no_external
anbieter.aufrufen = no_external
aegis.aufrufen = no_external

import pytest
os.chdir(ROOT / 'repo')
files = [
    'tests/test_kernmass_pareto.py',
    'tests/test_rauschmessung.py',
    'tests/test_ansage_aufnahme.py',
    'tests/test_doppelungsschluessel.py',
    'tests/test_artvorlage.py',
    'tests/test_vorspann.py',
]
if __name__ == '__main__':
    raise SystemExit(pytest.main(['-q', '-p', 'no:cacheprovider', '--basetemp', str(TMP / 'pytest'),
                                '--junitxml', str(OUT / 'unit-checks.xml'), *files]))
