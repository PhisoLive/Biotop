"""KOPIE für Review vor T4-03 (Pfade /tmp/review-vor-t4-03, pgrep breiter), Original: Review vor T4-02 — Organ-Proben Teil 2 (echte Kammer biotop-kammer:1, nach Jobende). Kein Modell, kein Netz.
p10: Deckung bei Standardparameter (Test ruft f('a'), Sonde ruft f('a', False)) — Kontrolle p10b ruft f('a', False).
p12: Kandidat setzt @functools.lru_cache auf eine reine Funktion (Verhalten gleich)."""
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, '/root/biotop')
if subprocess.run(['pgrep', '-f', 'job_commit_regression'], capture_output=True, text=True).stdout.strip():
    sys.exit('job_commit_regression.sh läuft — keine Kammerläufe')
from biotop.organe import kammer  # noqa: E402
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

kammer.IMAGE = 'biotop-kammer:1'
GIT_VORHER = subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True, text=True).stdout
B = Path('/tmp/review-vor-t4-03/werke2')
shutil.rmtree(B, ignore_errors=True)
aus = {}


def fall(name, quelle, neu, last, tests=None, behoben=()):
    w = B / name
    (w / 'paket' / 'm').mkdir(parents=True)
    (w / 'tests').mkdir()
    (w / 'paket' / '__init__.py').write_text('')
    (w / 'paket' / 'm' / '__init__.py').write_text('')
    (w / 'paket' / 'm' / 'a.py').write_text(quelle)
    ref = "import sys\nsys.path.insert(0, '/werk')\n\n\ndef last_m():\n" + ''.join('    ' + z + '\n' for z in last.splitlines())
    code = {'paket/m/a.py': neu}
    t0 = time.monotonic()
    if tests:
        r = vv.pruefen(w, code, ref, ['m'], lambda abw: vv.deckende_aufrufe(w, code, tests, set(behoben)))
    else:
        r = vv.pruefen(w, code, ref, ['m'], {'tests': [], 'aufrufe': []})
    e = {k: r.get(k) for k in ('geurteilt', 'tragfaehig', 'beobachtete_funktionen', 'anzahl_abweichungen', 'gedeckt',
                               'deckung_zaehlung', 'eingewickelt')}
    e['ungedeckt'] = (r.get('ungedeckt') or [])[:8]
    e['werte'] = dict(list((r.get('werte') or {}).items())[:3])
    e['eingaben'] = dict(list((r.get('eingaben') or {}).items())[:3])
    e['grund'] = str(r.get('grund'))[:220]
    e['dauer_s'] = round(time.monotonic() - t0, 1)
    aus[name] = e
    print(name, json.dumps(e, ensure_ascii=False)[:1300], flush=True)


Q = "def f(x: str, gross: bool = False) -> str:\n    return x.upper() if gross else x\n"
N = "def f(x: str, gross: bool = False) -> str:\n    return (x.upper() if gross else x) + '!'\n"
fall('p10_standardparameter', Q, N, "from paket.m.a import f\nf('z')",
     tests={'tests/test_m.py': "from paket.m.a import f\n\n\ndef test_f_neu():\n    assert f('a') == 'a!'\n"},
     behoben=['test_m.py::test_f_neu'])
fall('p10b_kontrolle_voll', Q, N, "from paket.m.a import f\nf('z')",
     tests={'tests/test_m.py': "from paket.m.a import f\n\n\ndef test_f_neu():\n    assert f('a', False) == 'a!'\n"},
     behoben=['test_m.py::test_f_neu'])
fall('p12_lru_cache', "def quadrat(x: int) -> int:\n    return x * x\n",
     "import functools\n\n\n@functools.lru_cache(maxsize=None)\ndef quadrat(x: int) -> int:\n    return x * x\n",
     "from paket.m.a import quadrat\nfor i in range(50):\n    quadrat(i % 5)")
GIT_NACHHER = subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True, text=True).stdout
print('git status /root/biotop vorher == nachher:', GIT_VORHER == GIT_NACHHER, repr(GIT_NACHHER[:300]))
Path('/tmp/review-vor-t4-03/SONDENPROBE-HEAD-2.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
