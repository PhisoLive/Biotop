"""Review vor T4-04 — lokale Rechenproben ohne Kammer (nur lesen, nichts unter /root/biotop schreiben).
1) Welche Iterator-Typen ersetzt _iter_art ('iter') bzw. lässt es stehen ('objekt')?
2) __slots__ mit Namensverschleierung (__x): sieht _felder den Zustand?
3) Merkmale Python gegen TypeScript an Zeichen außerhalb der Paritätsprobe.
4) eigene_tests: parametrisierte Tests des Kandidaten (Test-ID mit [..]).
"""
import csv
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
os.environ['TMPDIR'] = '/tmp/review-vor-t4-04/tmp'
tempfile.tempdir = '/tmp/review-vor-t4-04/tmp'
sys.path.insert(0, '/root/biotop')
KERN = Path('/root/biotop/biotop/kern')
spec = importlib.util.spec_from_file_location('vh', KERN / 'py/verhalten.py')
vh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vh)

print('== 1 _iter_art')
proben = {
    'csv.reader': csv.reader(io.StringIO('a,b\n1,2\n')),
    'csv.DictReader': csv.DictReader(io.StringIO('a,b\n1,2\n')),
    'map': map(str, [1]), 'zip': zip([1], [2]), 'enumerate': enumerate([1]),
    'generator': (x for x in [1]), 'io.StringIO': io.StringIO('a\nb\n'),
    'itertools.count': __import__('itertools').count(),
}
for n, v in proben.items():
    print(f'  {n:16} modul={type(v).__module__:12} art={vh._iter_art(v)!s:7} attribute={[a for a in ("fieldnames", "line_num", "reader") if hasattr(v, a)]}')

print('== 2 __slots__ mit Namensverschleierung')
ns = {}
exec("class Konto:\n    __slots__ = ('__stand',)\n    def __init__(self, s):\n        self.__stand = s\n"
     "    def buchen(self, b):\n        self.__stand += b\n", ns)
k = ns['Konto'](1)
print('  _slotnamen =', vh._slotnamen(k), '| _felder =', vh._felder(k), '| echte Slots =', [s for s in dir(k) if 'stand' in s])
ns2 = {}
exec("class Konto:\n    __slots__ = ('stand',)\n    def __init__(self, s):\n        self.stand = s\n", ns2)
print('  Kontrolle ohne __: _felder =', vh._felder(ns2['Konto'](1)))
from fractions import Fraction  # noqa: E402
print('  Fraction: _instanz =', vh._instanz(Fraction(3, 4)), '_felder =', vh._felder(Fraction(3, 4)))

print('== 3 Merkmale Python gegen TypeScript')
extra = ['\ufeffa b', 'a\x1cb', '\x85a', 'a\u200bb', 'a\u2009b', '\u3000a', 'a\x0bb', 'İ', 'ß', 'ǅ', 'a\u1680b', 'a 0.10', '007', '1.0']
py = [sorted(vh._text_merkmale(s)) for s in extra]
skript = ("import {textMerkmale} from " + json.dumps(str(KERN / 'ts/kanon.mjs')) + ";\n"
          "const p = JSON.parse(process.argv[1]);\nconsole.log(JSON.stringify(p.map(s => [...textMerkmale(s)].sort())));\n")
r = subprocess.run(['node', '--input-type=module', '-e', skript, json.dumps(extra)], capture_output=True, text=True, timeout=60)
ts = json.loads(r.stdout) if r.returncode == 0 else None
print('  node rc', r.returncode, r.stderr[-300:])
diff = {repr(extra[i]): (py[i], ts[i]) for i in range(len(extra)) if ts and py[i] != ts[i]}
print(f'  verschieden: {len(diff)} von {len(extra)}')
for k2, v in diff.items():
    print('   ', k2, 'py=', v[0], 'ts=', v[1])

print('== 4 eigene_tests und parametrisierte Tests')
from biotop.organe import aegis  # noqa: E402
with tempfile.TemporaryDirectory() as d:
    w = Path(d)
    (w / 'tests').mkdir()
    neu = "import pytest\n\n\n@pytest.mark.parametrize('x', [1, 2])\ndef test_neu(x):\n    assert x\n"
    e = aegis.eigene_tests(w, {'tests/test_p.py': neu}, {})
    print('  eigene_tests =', sorted(e), '| pytest-ID der Fälle wäre test_p.py::test_neu[1], test_p.py::test_neu[2]')
    print('  test_p.py::test_neu[1] ausgeschlossen:', 'test_p.py::test_neu[1]' in e)
print('== 5 _muster_von: Randwerte des veränderten Arguments')
grund = ['a b']
for rand in (['Ä-1'], [''], ['x' * 40], ['a\tb'], ['  ']):
    print(f'  {rand!r:12} klassen_von={sorted(vh.klassen_von([vh.unpack(rand[0])]))} muster={vh._muster_von(rand, grund, "rand")}')
