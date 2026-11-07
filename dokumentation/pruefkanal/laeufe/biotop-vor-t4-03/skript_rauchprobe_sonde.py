"""Rauchprobe der neuen Python-Sonde direkt in der Kammer (biotop-kammer:1): ein Kleinstwerk mit Funktion, Generator,
in-place-Funktion, lru_cache, Klasse mit Methode/Eigenschaft, Mengenausgabe; Modus beobachten und deckung.
Nur Diagnose während des Baus (kein Beleg), Ausgabe auf stdout."""
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.organe import kammer  # noqa: E402

kammer.IMAGE = 'biotop-kammer:1'
W = Path('/tmp/r3-rauch/werk')
shutil.rmtree(W.parent, ignore_errors=True)
(W / 'paket' / 'm').mkdir(parents=True)
(W / 'tests' / 'vertraege').mkdir(parents=True)
(W / 'paket' / '__init__.py').write_text('')
(W / 'paket' / 'm' / '__init__.py').write_text('')
(W / 'paket' / 'm' / 'a.py').write_text('''import functools


def f(x: str, gross: bool = False) -> str:
    return x.upper() if gross else x


def zahlen(n: int):
    yield from range(n)


def sortiere(xs: list[int]) -> None:
    xs.sort()


@functools.lru_cache(maxsize=None)
def quadrat(x: int) -> int:
    return x * x


def woerter(s: str) -> list:
    return list(set(s.split()))


def verbinde(a, b):
    return a.strip() + b


class Konto:
    def __init__(self, stand: int):
        self.stand = stand

    def buchen(self, betrag: int) -> int:
        self.stand += betrag
        return self.stand

    @property
    def doppelt(self) -> int:
        return self.stand * 2
''')
(W / 'tests' / 'vertraege' / 'test_vertrag_m.py').write_text('''from paket.m.a import Konto


def test_konto():
    assert Konto(10).buchen(5) == 15
''')
(W / 'tests' / 'test_m.py').write_text('''from paket.m.a import f, Konto


def test_f():
    assert f('a') == 'a'


def test_konto():
    k = Konto(3)
    assert k.buchen(1) == 4
''')
REF = '''import sys
sys.path.insert(0, '/werk')


def last_m():
    from paket.m.a import f, zahlen, sortiere, quadrat, woerter, Konto
    f('z')
    list(zahlen(3))
    sortiere([3, 1, 2])
    for i in range(20):
        quadrat(i % 5)
    woerter('alpha beta gamma delta')
    Konto(1).buchen(2)
'''
sonde = Path('/root/biotop/biotop/kern/py/verhalten.py').read_text()


def lauf(anfrage):
    e = kammer.ausfuehren(W, ['python', '_messgeraet/verhalten.py', '_messgeraet/anfrage.json'], zeitlimit_s=120,
                          dateien={'_messgeraet/verhalten.py': sonde, '_messgeraet/referenzlast.py': REF,
                                   '_messgeraet/anfrage.json': json.dumps(anfrage)})
    m = re.search(r'@@VV@@(.*)@@ENDE@@', e.stdout or '', re.S)
    if not m:
        print('KEIN ERGEBNIS rc', e.rc, (e.stderr or '')[-2000:])
        return None
    return json.loads(m.group(1))


d = lauf({'modus': 'beobachten', 'module': ['paket.m.a'], 'bereiche': ['m'], 'kappe': 8})
if d:
    print('gueltig', d.get('gueltig'), d.get('grund', '')[:500])
    print('hashsaat', d.get('hashsaat'), 'vertragslauf', d.get('vertragslauf'), 'instanzen', d.get('instanzen'))
    print('eingewickelt', d.get('eingewickelt'), 'nicht', d.get('nicht_eingewickelt'))
    print('signaturen', d.get('signaturen'))
    print('inhalt', d.get('inhalt'))
    print('konstruktion', d.get('konstruktion'))
    b = d.get('beobachtungen') or {}
    print('beobachtungen', len(b), 'kopien', len(d.get('kopien') or {}), list((d.get('kopien') or {}).items())[:4])
    for k in sorted(b):
        if any(x in k for x in ('zahlen#0', 'sortiere#0', 'quadrat#0', 'Konto.buchen#0', 'Konto.doppelt~rand#0',
                                'verbinde~rand#0', 'verbinde~form#0', '__init__~instanz', 'woerter#0')):
            print(' ', k, '=', b[k][:100], '| muster', (d.get('muster') or {}).get(k))
    print('form', sorted(k for k in b if '~form#' in k and '@' not in k and '>' not in k)[:12])
    print('muster-arten', sorted({x for v in (d.get('muster') or {}).values() for x in v}))
dk = lauf({'modus': 'deckung', 'module': ['paket.m.a'], 'testdateien': ['tests/test_m.py']})
if dk:
    print('deckung gueltig', dk.get('gueltig'), dk.get('rc'), dk.get('zustand'), dk.get('aufrufe'))
dv = lauf({'modus': 'deckung', 'module': ['paket.m.a'], 'testdateien': ['tests/test_m.py'],
           'verfaelschen': {'f': 'paket.m.a:f', 'art': 'rueckgabe'}})
if dv:
    print('verfaelscht', dv.get('gueltig'), dv.get('zustand'))
dz = lauf({'modus': 'deckung', 'module': ['paket.m.a'], 'testdateien': ['tests/test_m.py'],
           'verfaelschen': {'f': 'paket.m.a:Konto.buchen', 'art': 'zustand'}})
if dz:
    print('verfaelscht zustand', dz.get('gueltig'), dz.get('zustand'))
