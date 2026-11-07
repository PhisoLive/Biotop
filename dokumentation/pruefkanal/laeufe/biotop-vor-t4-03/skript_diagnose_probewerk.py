"""Diagnose: warum bricht messgeraet.messen am probewerk (tests/test_vor_t4_03.py) mit rc=1 ab? (Bau-Diagnose)"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, '/root/biotop')
sys.path.insert(0, '/root/biotop/tests')
from biotop.kern import messgeraet
from biotop.organe import kammer
import test_vor_t4_03 as t

kammer.IMAGE = 'biotop-kammer:1'
with tempfile.TemporaryDirectory() as d:
    w = Path(d) / 'werk'
    t._anlegen(w)
    orig = kammer.ausfuehren

    def zeigen(*a, **k):
        r = orig(*a, **k)
        print('RC', r.rc, 'STDOUT', (r.stdout or '')[-1500:], 'STDERR', (r.stderr or '')[-2500:])
        return r
    kammer.ausfuehren = zeigen
    messgeraet.kammer.ausfuehren = zeigen
    try:
        b = messgeraet.messen(w, ['werk'], t.PAKET, t.REFERENZLAST)
        print('GUELTIG', b.get('gueltig'), b.get('grund'))
    except Exception as e:  # noqa: BLE001
        print('FEHLER', repr(e)[:2000])
