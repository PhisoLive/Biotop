"""KOPIE für Review vor T4-03 (Pfade /tmp/review-vor-t4-03, pgrep breiter), Original: Review vor T4-02 — Organ-Proben (nicht Laufweg) an der echten Kammer, nach Ende von job_commit_regression.sh.
Python-Sonde (biotop-kammer:1) und TS-Deckungsaufzeichner (biotop-kammer:ts1) über verhaltensvergleich.pruefen.
Nur Werke unter /tmp/review-vor-t4-03/werke; kein Modell, kein Netz, keine Lauf-DB. Aufruf: python -B sondenprobe.py"""
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
from biotop.kern import messgeraet  # noqa: E402
from biotop.organe import kammer  # noqa: E402
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

GIT_VORHER = subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True, text=True).stdout
B = Path('/tmp/review-vor-t4-03/werke')
shutil.rmtree(B, ignore_errors=True)
aus = {}
FELDER = ('sprache', 'geurteilt', 'tragfaehig', 'grund_art', 'beobachtete_funktionen', 'anzahl_abweichungen',
          'nicht_eingewickelt', 'randfaelle', 'formvarianten', 'gedeckt', 'deckung_zaehlung')


def festhalten(name, r, t0):
    e = {k: r.get(k) for k in FELDER}
    e['ungedeckt'] = (r.get('ungedeckt') or [])[:6]
    e['werte'] = dict(list((r.get('werte') or {}).items())[:3])
    e['grund'] = str(r.get('grund'))[:200]
    e['kurz_traegt_nicht_eingewickelt'] = 'nicht_eingewickelt' in vv.kurz(r)
    e['dauer_s'] = round(time.monotonic() - t0, 1)
    aus[name] = e
    print(name, json.dumps(e, ensure_ascii=False)[:1100], flush=True)


def py_fall(name, quelle, neu, last, tests=None, behoben=()):
    kammer.IMAGE = 'biotop-kammer:1'
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
    festhalten(name, r, t0)


def ts_fall(name, quelle, neu, test):
    kammer.IMAGE = 'biotop-kammer:ts1'
    w = B / name
    (w / 'src' / 'm').mkdir(parents=True)
    (w / 'tests').mkdir()
    (w / 'package.json').write_text('{"type":"module"}')
    (w / 'src' / 'm' / 'a.ts').write_text(quelle)
    ref = "import { f } from './dist/m/a.js';\nexport function last_m() { for (let i = 0; i < 100; i++) f('z'); }\n"
    code, tests = {'src/m/a.ts': neu}, {'tests/test_m_deckung.test.ts': test}
    t0 = time.monotonic()
    r = vv.pruefen(w, code, ref, ['m'], lambda abw: vv.deckende_aufrufe(w, code, tests, {'test_m_deckung.test.ts::test_m_deckt_a'}))
    festhalten(name, r, t0)


# P0 Kontrolle: die Sonde sieht eine Rückgabeänderung (Probe kann ausschlagen)
py_fall('p0_kontrolle', "def f(x: str) -> str:\n    return x\n", "def f(x: str) -> str:\n    return x.upper()\n",
        "from paket.m.a import f\nf('z')")
# P1 Generator: Ausgabe geändert (range(n) → range(n+1))
py_fall('p1_generator', "def zahlen(n: int):\n    yield from range(n)\n", "def zahlen(n: int):\n    yield from range(n + 1)\n",
        "from paket.m.a import zahlen\nlist(zahlen(3))")
# P2 Nebenwirkung an der Eingabe: sortiert in place, jetzt absteigend; Rückgabe None
py_fall('p2_inplace', "def sortiere(xs: list[int]) -> None:\n    xs.sort()\n",
        "def sortiere(xs: list[int]) -> None:\n    xs.sort(reverse=True)\n", "from paket.m.a import sortiere\nsortiere([3, 1, 2])")
# P3 Methode geändert, daneben eine unveränderte Modulfunktion
KL = "class Rechner:\n    def doppelt(self, x: int) -> int:\n        return {} * x\n\n\ndef version() -> str:\n    return '1'\n"
py_fall('p3_methode', KL.format(2), KL.format(3), "from paket.m.a import Rechner, version\nRechner().doppelt(2)\nversion()")
# P4 ohne Typannotation, nicht von der Last gerufen (Hilfsfunktion)
py_fall('p4_ohne_annotation', "def verbinde(a, b):\n    return a.strip() + b\n", "def verbinde(a, b):\n    return a.strip().upper() + b\n",
        "pass")
# P5 Mengenreihenfolge über zwei Kammerprozesse; der Kandidat ändert nur eins() ohne Verhaltensänderung
MG = "def woerter(s: str) -> list:\n    return list(set(s.split()))\n\n\ndef eins() -> int:\n    return {}\n"
for i in (1, 2):
    py_fall(f'p5_mengenfolge_{i}', MG.format('1'), MG.format('0 + 1'),
            "from paket.m.a import woerter\nwoerter('alpha beta gamma delta epsilon zeta eta theta')")
# P6 Beifang-Deckung: der Test hält nur g fest, ruft f('a') nebenbei ohne Zusicherung
FG = "def f(x: str) -> str:\n    return {}\n\n\ndef g(x: int) -> int:\n    return {}\n"
py_fall('p6_beifang', FG.format('x', 'x'), FG.format('x.upper()', 'x + 1'), "from paket.m.a import f\nf('z')",
        tests={'tests/test_m.py': "from paket.m.a import f, g\n\n\ndef test_g_neu():\n    f('a')\n    assert g(1) == 2\n"},
        behoben=['test_m.py::test_g_neu'])
# P7/P8 TS-Deckungsaufzeichner: export function (Kontrolle) gegen export const (gleiche Änderung, gleicher Test)
TEST = ("import { test, expect } from 'vitest';\nimport { f } from '../src/m/a.js';\n\n"
        "test('test_m_deckt_a', () => {\n  expect(f('a')).toBe('A');\n});\n")
ts_fall('p7_ts_export_function', "export function f(x: string): string {\n  return x;\n}\n",
        "export function f(x: string): string {\n  return x.toUpperCase();\n}\n", TEST)
ts_fall('p8_ts_export_const', "export const f = (x: string): string => x;\n",
        "export const f = (x: string): string => x.toUpperCase();\n", TEST)
# P9 laufzeitrisse: Bereichsname mit Bindestrich (reine Funktion)
aus['p9_laufzeitrisse'] = {
    'planung': messgeraet.laufzeitrisse({'grenzen_gerissen': ['planung.laufzeit_ms: 12.000 > Grenze 10.000 (x)']}),
    'daten-import': messgeraet.laufzeitrisse({'grenzen_gerissen': ['daten-import.laufzeit_ms: 12.000 > Grenze 10.000 (x)']})}
print('p9_laufzeitrisse', aus['p9_laufzeitrisse'])
GIT_NACHHER = subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True, text=True).stdout
aus['_meta'] = {'git_status_gleich': GIT_VORHER == GIT_NACHHER, 'git_status': GIT_NACHHER[:500], 'modellaufrufe': 0}
print('git status /root/biotop vorher == nachher:', GIT_VORHER == GIT_NACHHER, repr(GIT_NACHHER[:300]))
Path('/tmp/review-vor-t4-03/SONDENPROBE-HEAD.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
