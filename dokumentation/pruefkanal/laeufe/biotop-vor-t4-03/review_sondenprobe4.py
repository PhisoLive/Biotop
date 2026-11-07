"""Review vor T4-03 — Organ-Probe Zustand von self bei Klassen mit __slots__ (echte Kammer biotop-kammer:1, Code HEAD).
p19  Klasse mit __slots__: Methode ändert nur den Zustand von self (Rückgabe None), Last ruft sie.
p19b Kontrolle: dieselbe Klasse ohne __slots__.
p20  @dataclass(slots=True): dieselbe Änderung.
Kein Modell, kein Netz. Nur Werke unter /tmp/review-vor-t4-03/werke4."""
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, '/root/biotop')
if subprocess.run(['pgrep', '-f', 'job_commit_regression'], capture_output=True, text=True).stdout.strip():
    sys.exit('job_commit_regression läuft — keine Kammerläufe')
from biotop.organe import kammer  # noqa: E402
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

kammer.IMAGE = 'biotop-kammer:1'
GIT_VORHER = subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True, text=True).stdout
B = Path('/tmp/review-vor-t4-03/werke4')
shutil.rmtree(B, ignore_errors=True)
aus = {}


def fall(name, quelle, neu, last):
    w = B / name
    (w / 'paket' / 'm').mkdir(parents=True)
    (w / 'tests').mkdir()
    (w / 'paket' / '__init__.py').write_text('')
    (w / 'paket' / 'm' / '__init__.py').write_text('')
    (w / 'paket' / 'm' / 'a.py').write_text(quelle)
    ref = "import sys\nsys.path.insert(0, '/werk')\n\n\ndef last_m():\n" + ''.join('    ' + z + '\n' for z in last.splitlines())
    code = {'paket/m/a.py': neu}
    t0 = time.monotonic()
    r = vv.pruefen(w, code, ref, ['m'], {'tests': [], 'aufrufe': []})
    e = {k: r.get(k) for k in ('geurteilt', 'tragfaehig', 'grund_art', 'beobachtete_funktionen', 'anzahl_abweichungen',
                               'enthaltungen', 'instanzen', 'nicht_eingewickelt', 'randfaelle', 'formvarianten')}
    e['ungedeckt'] = (r.get('ungedeckt') or [])[:6]
    e['werte'] = dict(list((r.get('werte') or {}).items())[:3])
    e['grund'] = str(r.get('grund'))[:220]
    e['dauer_s'] = round(time.monotonic() - t0, 1)
    aus[name] = e
    print(name, json.dumps(e, ensure_ascii=False)[:1400], flush=True)


KS = ("class Konto:\n{slots}    def __init__(self, stand: int):\n        self.stand = stand\n\n"
      "    def buchen(self, b: int) -> None:\n        self.stand += {faktor}b\n")
LAST = "from paket.m.a import Konto\nk = Konto(1)\nk.buchen(2)\nk.buchen(3)"
fall('p19_slots_nur_zustand', KS.format(slots="    __slots__ = ('stand',)\n\n", faktor=''),
     KS.format(slots="    __slots__ = ('stand',)\n\n", faktor='2 * '), LAST)
fall('p19b_kontrolle_ohne_slots', KS.format(slots='', faktor=''), KS.format(slots='', faktor='2 * '), LAST)
DC = ("import dataclasses\n\n\n@dataclasses.dataclass(slots=True)\nclass Konto:\n    stand: int\n\n"
      "    def buchen(self, b: int) -> None:\n        self.stand += {faktor}b\n")
fall('p20_dataclass_slots', DC.format(faktor=''), DC.format(faktor='2 * '), LAST)
GIT_NACHHER = subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True, text=True).stdout
aus['_meta'] = {'git_status_gleich': GIT_VORHER == GIT_NACHHER, 'git_status': GIT_NACHHER[:300], 'modellaufrufe': 0}
print('meta', aus['_meta'])
Path('/tmp/review-vor-t4-03/SONDENPROBE-4.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
