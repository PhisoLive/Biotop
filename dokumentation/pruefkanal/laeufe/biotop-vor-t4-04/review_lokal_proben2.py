"""Review vor T4-04 — lokale Rechenproben 2 (ohne Kammer): pathlib-Slots vor/nach Gebrauch (Zustandsvergleich >args),
parametrisierte Kandidatentests in nur_funktionen/_nennt_vertrag, kan() von Path."""
import importlib.util
import os
import sys
import tempfile
from pathlib import Path, PurePosixPath

sys.dont_write_bytecode = True
os.environ['TMPDIR'] = '/tmp/review-vor-t4-04/tmp'
tempfile.tempdir = '/tmp/review-vor-t4-04/tmp'
sys.path.insert(0, '/root/biotop')
spec = importlib.util.spec_from_file_location('vh', '/root/biotop/biotop/kern/py/verhalten.py')
vh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vh)

print('python', sys.version.split()[0])
print('== pathlib: Zustand eines Path-Arguments nach p.name gegen nach str(p)')
a, b = Path('x/y.txt'), Path('x/y.txt')
print('  _instanz(Path)=', vh._instanz(a), '_veraenderlich=', vh._veraenderlich(a))
print('  vorher  a:', sorted(vh._felder(a)))
_ = a.name
_ = str(b)
print('  nach a.name :', sorted(vh._felder(a)))
print('  nach str(b) :', sorted(vh._felder(b)))
for n, o in (('a', a), ('b', b)):
    try:
        print(f'  text_von({n}) =', vh.text_von(o)[:160])
    except Exception as e:  # noqa: BLE001
        print(f'  text_von({n}) Fehler', type(e).__name__, e)
    try:
        print(f'  text_von(schnappschuss-felder {n}) =', vh.text_von(vh._felder(o))[:200])
    except Exception as e:  # noqa: BLE001
        print('   Fehler', type(e).__name__, e)
print('  PurePosixPath _instanz:', vh._instanz(PurePosixPath('a')))

print('== parametrisierter Kandidatentest: Aufnahme')
from biotop.organe import aegis  # noqa: E402
inhalt = ('import pytest\nfrom probewerk.werk.kern import normieren\n\n\n@pytest.mark.parametrize("x", ["a\\tb"])\n'
          'def test_werk_eigen(x):\n    assert normieren(None) == ""\n    with pytest.raises(ValueError):\n        normieren(x)\n')
for name in ('test_werk_eigen[a\\tb]', 'test_werk_eigen'):
    print(f'  nur_funktionen(behalten={{{name!r}}}) ->', 'None' if aegis.nur_funktionen(inhalt, {name}) is None else 'Code')
