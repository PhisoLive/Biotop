"""Review vor T4-03 — neue Organ-Proben der Python-Sonde (echte Kammer biotop-kammer:1) über verhaltensvergleich.pruefen
am Code von HEAD (/root/biotop). Gesucht: Stellen, an denen die Sonde still schweigt oder Fehlalarm gibt.
p13 async | p14 Iterator ohne Ende | p15 veränderlicher Standardwert (Kandidat führt ihn ein) | p16/p16b Klasse ohne
Vertrag, Konstruktor ohne/mit Annotation | p17/p17b Eigenschaft einer Klasse ohne Vertrag | p18/p18b zurückgegebenes
Iterator-Objekt (Sonde ersetzt es durch einen Generator). Kein Modell, kein Netz, keine Lauf-DB.
Nur Werke unter /tmp/review-vor-t4-03/werke3. Aufruf: python -B sondenprobe3.py"""
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
B = Path('/tmp/review-vor-t4-03/werke3')
shutil.rmtree(B, ignore_errors=True)
aus = {}
FELDER = ('geurteilt', 'tragfaehig', 'grund_art', 'beobachtete_funktionen', 'anzahl_abweichungen', 'enthaltungen',
          'enthaltungen_zaehlung', 'instanzen', 'nicht_eingewickelt', 'randfaelle', 'formvarianten', 'instabil', 'hashsaat')


def fall(name, quelle, neu, last, roh=False):
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
    e = {k: r.get(k) for k in FELDER}
    e['ungedeckt'] = (r.get('ungedeckt') or [])[:6]
    e['werte'] = dict(list((r.get('werte') or {}).items())[:3])
    e['grund'] = str(r.get('grund'))[:220]
    if roh:
        # Rohbeobachtung der Vorgeneration: Ergebnis der Referenzlast selbst (korpus:last_m) und Aufrufzähler
        b = vv.beobachten(w, {}, ref, ['paket.m.a'], ['m'])
        e['roh_vorgeneration'] = {'korpus:last_m': (b.get('beobachtungen') or {}).get('korpus:last_m'),
                                  'aufgerufen': b.get('aufgerufen'), 'erreicht': b.get('erreicht')}
    e['dauer_s'] = round(time.monotonic() - t0, 1)
    aus[name] = e
    print(name, json.dumps(e, ensure_ascii=False)[:1500], flush=True)


# p13 asynchrone Funktion: Rückgabe geändert; daneben eine gewöhnliche Funktion
AS = "async def hole(x: int) -> int:\n    return x + {}\n\n\ndef eins() -> int:\n    return 1\n"
fall('p13_async', AS.format(1), AS.format(2), "import asyncio\nfrom paket.m.a import hole, eins\nasyncio.run(hole(3))\neins()")
# p14 Iterator ohne Ende: Änderung erst nach dem 60. Element
IT = ("def zaehle(start: int):\n    n = start\n    while True:\n        yield n\n        n += {}\n")
fall('p14_endloser_iterator', IT.format('1'), IT.format('1 if n < start + 60 else 2'),
     "from itertools import islice\nfrom paket.m.a import zaehle\nlist(islice(zaehle(0), 100))")
# p15 veränderlicher Standardwert: der Kandidat führt einen geteilten Speicher ein (Fehler ab dem 2. Aufruf)
fall('p15_veraenderlicher_standardwert',
     "def sammle(x: int, acc: list | None = None) -> list:\n    acc = [] if acc is None else acc\n    acc.append(x)\n    return acc\n",
     "def sammle(x: int, acc: list | None = None, _speicher=[]) -> list:\n    acc = _speicher if acc is None else acc\n"
     "    acc.append(x)\n    return acc\n",
     "from paket.m.a import sammle\nsammle(1)\nsammle(2)\nsammle(3)")
# p16 Klasse ohne Vertrag, Konstruktor ohne Annotation, von der Last nicht gerufen; Methode geändert
KU = ("class Zaehler:\n    def __init__(self, start{ann}):\n        self.start = start\n\n    def weiter(self) -> int:\n"
      "        return self.start + {d}\n\n\ndef eins() -> int:\n    return 1\n")
fall('p16_klasse_ohne_vertrag_untypisiert', KU.format(ann='', d=1), KU.format(ann='', d=2), "from paket.m.a import eins\neins()")
fall('p16b_kontrolle_typisiert', KU.format(ann=': int', d=1), KU.format(ann=': int', d=2), "from paket.m.a import eins\neins()")
# p17 Eigenschaft einer Klasse ohne Vertrag (Instanz aus der Signatur): multiplikative bzw. additive Änderung
KP = ("class Konto:\n    def __init__(self, stand: int):\n        self.stand = stand\n\n    @property\n    def doppelt(self) -> int:\n"
      "        return {}\n\n\ndef eins() -> int:\n    return 1\n")
fall('p17_eigenschaft_multiplikativ', KP.format('self.stand * 2'), KP.format('self.stand * 3'), "from paket.m.a import eins\neins()")
fall('p17b_kontrolle_additiv', KP.format('self.stand * 2'), KP.format('self.stand * 2 + 1'), "from paket.m.a import eins\neins()")
# p18 zurückgegebenes Iterator-Objekt mit Attribut; die Last liest das Attribut, dann doppel(3) (nur dort geändert)
LS = ("class Leser:\n    def __init__(self, text: str):\n        self.teile = text.split()\n        self.nummer = 0\n\n"
      "    def __iter__(self):\n        return self\n\n    def __next__(self) -> str:\n        if self.nummer >= len(self.teile):\n"
      "            raise StopIteration\n        self.nummer += 1\n        return self.teile[self.nummer - 1]\n\n\n"
      "def leser(text: str) -> 'Leser':\n    return Leser(text)\n\n\ndef doppel(x: int) -> int:\n    return {}\n")
fall('p18_iterator_objekt_ersetzt', LS.format('2 * x'), LS.format('2 * x + (1 if x == 3 else 0)'),
     "from paket.m.a import leser, doppel\nr = leser('a b c')\nnext(r)\nn = r.nummer\ndoppel(3)", roh=True)
fall('p18b_kontrolle_ohne_attribut', LS.format('2 * x'), LS.format('2 * x + (1 if x == 3 else 0)'),
     "from paket.m.a import leser, doppel\nr = leser('a b c')\nnext(r)\ndoppel(3)", roh=True)
GIT_NACHHER = subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True, text=True).stdout
aus['_meta'] = {'git_status_gleich': GIT_VORHER == GIT_NACHHER, 'git_status': GIT_NACHHER[:300], 'modellaufrufe': 0,
                'head': subprocess.run(['git', '-C', '/root/biotop', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()}
print('meta', aus['_meta'])
Path('/tmp/review-vor-t4-03/SONDENPROBE-3.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
