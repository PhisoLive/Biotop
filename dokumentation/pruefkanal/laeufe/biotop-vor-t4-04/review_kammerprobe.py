"""Review vor T4-04 — Kammerproben gegen den neuen Commit (HEAD 43b8fad), echte Kammer biotop-kammer:1.
Teil A (Laufweg aegis.pruefen, wie review-proben/deckprobe.py des Gutachtens 03): x1, x2 (+ Kontrollen x1k, x2k);
  neu x3/x3k: Konsistenz-Zusicherung normieren(normieren(t)) == normieren(t) mit Tab — hält sie `tab` fest?
Teil B (Organ verhaltensvergleich.pruefen, wie sondenprobe3.py/sondenprobe4.py): p13..p20; neu p18c/p18ck (Elemente
  eines Iterator-Objekts des Werks geändert / Kontrolle Generator), q1/q1k (csv.DictReader mit Attribut / csv.reader),
  p21 (__slots__ mit Namensverschleierung), p22/p22k (__slots__ mit Vererbung: Basis-Slot / eigener Slot geändert),
  p23 (Koroutine in laufender Ereignisschleife).
Kein Modell, kein Netz. Werke und TMPDIR nur unter /tmp/review-vor-t4-04. Ergebnis: KAMMERPROBE.json (laufend)."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.dont_write_bytecode = True
R = Path('/tmp/review-vor-t4-04')
os.environ['TMPDIR'] = str(R / 'tmp')
tempfile.tempdir = str(R / 'tmp')
if subprocess.run(['pgrep', '-f', 'job_nachtrag|job_commit_regression'], capture_output=True, text=True).stdout.strip():
    sys.exit('Job läuft — keine Kammerläufe')
sys.path.insert(0, '/root/biotop')
TESTDATEI = Path('/root/biotop/tests/test_vor_t4_03.py')
text = TESTDATEI.read_text()
MARKE = '# ================================================================ F. Entscheidung 4'
ns = {'__name__': 'deckprobe', '__file__': str(TESTDATEI)}
exec(compile(text[:text.index(MARKE)], 'test_vor_t4_03.py (A–E, nur gelesen)', 'exec'), ns)
from biotop.organe import kammer  # noqa: E402
from biotop.organe import verhaltensvergleich as vv  # noqa: E402


def git(*a):
    return subprocess.run(['git', '-C', '/root/biotop', *a], capture_output=True, text=True).stdout.strip()


GIT_VORHER = git('status', '--porcelain')
AUS = R / 'KAMMERPROBE.json'
aus = {'_meta': {'head': git('rev-parse', '--short', 'HEAD'), 'git_status_vorher': GIT_VORHER, 'modellaufrufe': 0}}


def sichern():
    AUS.write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))


class Monkeypatch:
    def __init__(self):
        self.alt = []

    def setattr(self, ziel, name, wert):
        self.alt.append((ziel, name, getattr(ziel, name)))
        setattr(ziel, name, wert)

    def undo(self):
        for ziel, name, wert in reversed(self.alt):
            setattr(ziel, name, wert)
        self.alt.clear()


# ---------------------------------------------------------------- Teil A
QUELLE, T = ns['QUELLE'], ns['TEST_NORMIEREN']
ALT_ZEILE = '    return " ".join(text.split())\n'
K1 = ('    if "\\t" in text or "\\n" in text:\n        raise ValueError("Steuerzeichen")\n'
      '    return "_".join(text.split())\n')
K2 = '    if "\\t" in text:\n        return text\n    return "_".join(text.split())\n'
FAELLE = {"gewoehnlich": ("a b", "a_b"), "rand": (" a b ", "a_b"), "gross": ("A B", "A_B"),
          "lang": ("x " * 25, "_".join(["x"] * 25)), "zahlform": ("a 01 2.50", "a_01_2.50"), "nichtascii": ("Ä ö", "Ä_ö")}


def tests_aus(faelle):
    return {f"tests/test_werk_normieren_{n}.py": T.format(name=n, eingabe=e, erwartet=x) for n, (e, x) in faelle.items()}


def x2_tests(mit_tab):
    t = tests_aus({k: v for k, v in FAELLE.items() if k != "gewoehnlich"})
    koerper = ('    normieren("a\\tb c")\n' if mit_tab else '') + '    assert normieren("a b") == "a_b"\n'
    t["tests/test_werk_normieren_x.py"] = "from probewerk.werk.kern import normieren\n\n\ndef test_normieren_x():\n" + koerper
    return t


X3_BASIS = {k: v for k, v in FAELLE.items() if k != "gewoehnlich"}
X3_BASIS.update({"lf": ("a\nb", "a_b"), "crlf": ("a\r\nb", "a_b"), "nbsp": ("a\u00a0b", "a_b"), "doppelt": ("a  b", "a_b")})


def x3_tests(mit_idem):
    t = tests_aus(X3_BASIS)
    koerper = (('    assert normieren(normieren("a\\tb c")) == normieren("a\\tb c")\n' if mit_idem else '')
               + '    assert normieren("a b") == "a_b"\n')
    t["tests/test_werk_normieren_x.py"] = "from probewerk.werk.kern import normieren\n\n\ndef test_normieren_x():\n" + koerper
    return t


def a_fall(name, koerper, tests):
    neu = QUELLE.replace(ALT_ZEILE, koerper)
    assert neu != QUELLE
    mp = Monkeypatch()
    letzte = {}
    orig_vergleichen = vv.vergleichen

    def fang(alt, neu_, gedeckt, _o=orig_vergleichen):
        letzte.update(alt=dict(alt), neu=dict(neu_), gedeckt=set(gedeckt))
        return _o(alt, neu_, gedeckt)
    t0 = time.monotonic()
    try:
        with tempfile.TemporaryDirectory(dir=str(R / 'tmp')) as d:
            try:
                mp.setattr(vv, 'vergleichen', fang)
                u, v = ns['_pruefen'](Path(d), mp, ns['_diff'](QUELLE, neu), nische="sicher", werk_extra=tests)
            finally:
                mp.undo()
    except Exception as e:  # noqa: BLE001
        aus[name] = {'ausnahme': f'{type(e).__name__}: {e}'[:600], 'dauer_s': round(time.monotonic() - t0, 1)}
        print(name, aus[name], flush=True)
        sichern()
        return
    a, n, g = letzte.get('alt', {}), letzte.get('neu', {}), letzte.get('gedeckt', set())
    abw = [k for k in sorted(set(a) | set(n)) if a.get(k) != n.get(k)]
    rueck = [k for k in abw if (k.startswith('probewerk.werk.kern:normieren')
                                and (str(n.get(k, '')).startswith('Fehler:ValueError')
                                     or (koerper is K2 and '\\t' in str(n.get(k, '')))))]
    dz = v.get('deckung_zaehlung') or {}
    e = {'status': u.get('status'), 'grund': str(u.get('grund'))[:240], 'abweichungen': len(abw),
         'ungedeckt': len(v.get('ungedeckt_alle') or v.get('ungedeckt') or []),
         'rueckschritt_beobachtungen': len(rueck), 'rueckschritt_davon_gedeckt': sum(1 for k in rueck if k in g),
         'rueckschritt_gedeckt_durch': sorted({t for k in rueck for t in ((v.get('gedeckt') or {}).get(k) or [])})[:6],
         'festhaltend': dz.get('festhaltend'), 'verfaelschungen': dz.get('verfaelschungen'),
         'ungedeckt_aufschluesselung': v.get('ungedeckt_aufschluesselung'),
         'eigene_tests_ausgeschlossen': v.get('eigene_tests_ausgeschlossen'), 'dauer_s': round(time.monotonic() - t0, 1)}
    aus[name] = e
    print(name, json.dumps(e, ensure_ascii=False)[:1500], flush=True)
    sichern()


# ---------------------------------------------------------------- Teil B
B = R / 'werke'
shutil.rmtree(B, ignore_errors=True)
FELDER = ('geurteilt', 'tragfaehig', 'grund_art', 'beobachtete_funktionen', 'anzahl_abweichungen', 'enthaltungen',
          'instanzen', 'nicht_eingewickelt', 'teilweise', 'instabil')


def b_fall(name, quelle, neu, last, roh=False):
    kammer.IMAGE = 'biotop-kammer:1'
    w = B / name
    (w / 'paket' / 'm').mkdir(parents=True)
    (w / 'tests').mkdir()
    (w / 'paket' / '__init__.py').write_text('')
    (w / 'paket' / 'm' / '__init__.py').write_text('')
    (w / 'paket' / 'm' / 'a.py').write_text(quelle)
    ref = "import sys\nsys.path.insert(0, '/werk')\n\n\ndef last_m():\n" + ''.join('    ' + z + '\n' for z in last.splitlines())
    t0 = time.monotonic()
    e = {}
    try:
        r = vv.pruefen(w, {'paket/m/a.py': neu}, ref, ['m'], {'tests': [], 'aufrufe': []})
        e = {k: r.get(k) for k in FELDER}
        e['abweichungen'] = (r.get('abweichungen') or [])[:8]
        e['grund'] = str(r.get('grund'))[:220]
    except Exception as x:  # noqa: BLE001
        e['ausnahme'] = f'{type(x).__name__}: {x}'[:500]
    if roh:
        try:
            b = vv.beobachten(w, {}, ref, ['paket.m.a'], ['m'])
            e['roh_vorgeneration'] = {'korpus:last_m': (b.get('beobachtungen') or {}).get('korpus:last_m')}
        except Exception as x:  # noqa: BLE001
            e['roh_vorgeneration'] = f'{type(x).__name__}: {x}'[:200]
    e['dauer_s'] = round(time.monotonic() - t0, 1)
    aus[name] = e
    print(name, json.dumps(e, ensure_ascii=False, default=str)[:1300], flush=True)
    sichern()


LS = ("class Leser:\n    def __init__(self, text: str):\n        self.teile = text.split()\n        self.nummer = 0\n\n"
      "    def __iter__(self):\n        return self\n\n    def __next__(self) -> str:\n        if self.nummer >= len(self.teile):\n"
      "            raise StopIteration\n        self.nummer += 1\n        return self.teile[self.nummer - 1]\n\n\n"
      "def leser(text: str) -> 'Leser':\n    return Leser(text)\n\n\ndef doppel(x: int) -> int:\n    return {}\n")
LS2 = ("class Leser:\n    def __init__(self, text: str):\n        self.teile = text.split()\n        self.nummer = 0\n\n"
       "    def __iter__(self):\n        return self\n\n    def __next__(self) -> str:\n        if self.nummer >= len(self.teile):\n"
       "            raise StopIteration\n        self.nummer += 1\n        return self.teile[self.nummer - 1]{}\n\n\n"
       "def leser(text: str) -> 'Leser':\n    return Leser(text)\n")
GEN = "def leser(text: str):\n    for t in text.split():\n        yield t{}\n"
CSV = ("import csv\nimport io\n\n\ndef lies(text: str):\n    return csv.{}(io.StringIO(text))\n\n\n"
       "def doppel(x: int) -> int:\n    return {}\n")
KS = ("class Konto:\n{slots}    def __init__(self, stand: int):\n        self.stand = stand\n\n"
      "    def buchen(self, b: int) -> None:\n        self.stand += {faktor}b\n")
DC = ("import dataclasses\n\n\n@dataclasses.dataclass(slots=True)\nclass Konto:\n    stand: int\n\n"
      "    def buchen(self, b: int) -> None:\n        self.stand += {faktor}b\n")
KM = ("class Konto:\n    __slots__ = ('__stand',)\n\n    def __init__(self, stand: int):\n        self.__stand = stand\n\n"
      "    def buchen(self, b: int) -> None:\n        self.__stand += {}b\n")
KV = ("class Basis:\n    __slots__ = ('stand',)\n\n    def __init__(self, stand: int):\n        self.stand = stand\n\n\n"
      "class Konto(Basis):\n    __slots__ = ('name',)\n\n    def __init__(self, stand: int):\n        super().__init__(stand)\n"
      "        self.name = 'k'\n\n    def buchen(self, b: int) -> None:\n        {}\n")
LAST_K = "from paket.m.a import Konto\nk = Konto(1)\nk.buchen(2)\nk.buchen(3)"
AS = "async def hole(x: int) -> int:\n    return x + {}\n\n\ndef eins() -> int:\n    return 1\n"
IT = "def zaehle(start: int):\n    n = start\n    while True:\n        yield n\n        n += {}\n"
KU = ("class Zaehler:\n    def __init__(self, start{ann}):\n        self.start = start\n\n    def weiter(self) -> int:\n"
      "        return self.start + {d}\n\n\ndef eins() -> int:\n    return 1\n")
KP = ("class Konto:\n    def __init__(self, stand: int):\n        self.stand = stand\n\n    @property\n    def doppelt(self) -> int:\n"
      "        return {}\n\n\ndef eins() -> int:\n    return 1\n")

# Reihenfolge: das Wichtigste zuerst (Zeitgrenze des Aufrufs)
a_fall('x1_doppeltes_leerzeichen_deckt_tab_und_lf', K1, tests_aus({**FAELLE, "doppelt": ("a  b", "a_b")}))
a_fall('x2_tab_nur_gerufen_nicht_zugesichert', K2, x2_tests(True))
a_fall('x3_konsistenz_zusicherung_mit_tab', K2, x3_tests(True))
a_fall('x3k_kontrolle_ohne_konsistenz_zusicherung', K2, x3_tests(False))
b_fall('q1_csv_dictreader_attribut', CSV.format('DictReader', '2 * x'), CSV.format('DictReader', '2 * x + (1 if x == 3 else 0)'),
       "from paket.m.a import lies, doppel\nr = lies('a,b\\n1,2\\n')\nn = r.fieldnames\ndoppel(3)", roh=True)
b_fall('q1k_kontrolle_csv_reader', CSV.format('reader', '2 * x'), CSV.format('reader', '2 * x + (1 if x == 3 else 0)'),
       "from paket.m.a import lies, doppel\nr = lies('a,b\\n1,2\\n')\nnext(r)\nn = r.line_num\ndoppel(3)", roh=True)
b_fall('p21_slots_namensverschleierung', KM.format(''), KM.format('2 * '), LAST_K)
b_fall('p22_slots_vererbung_basis_slot', KV.format('self.stand += b'), KV.format('self.stand += 2 * b'), LAST_K)
b_fall('p22k_kontrolle_eigener_slot', KV.format("self.name += str(b)"), KV.format("self.name += str(2 * b)"), LAST_K)
b_fall('p18c_iterator_objekt_elemente_geaendert', LS2.format(''), LS2.format('.upper()'),
       "from paket.m.a import leser\nr = leser('a b c')\nx = list(r)")
b_fall('p18ck_kontrolle_generator', GEN.format(''), GEN.format('.upper()'), "from paket.m.a import leser\nx = list(leser('a b c'))")
b_fall('p23_koroutine_in_laufender_schleife', AS.format(1), AS.format(2),
       "import asyncio\nfrom paket.m.a import hole, eins\n\n\nasync def haupt():\n    return await hole(3)\n\n\nasyncio.run(haupt())\neins()")
b_fall('p18_iterator_objekt_ersetzt', LS.format('2 * x'), LS.format('2 * x + (1 if x == 3 else 0)'),
       "from paket.m.a import leser, doppel\nr = leser('a b c')\nnext(r)\nn = r.nummer\ndoppel(3)", roh=True)
b_fall('p18b_kontrolle_ohne_attribut', LS.format('2 * x'), LS.format('2 * x + (1 if x == 3 else 0)'),
       "from paket.m.a import leser, doppel\nr = leser('a b c')\nnext(r)\ndoppel(3)")
b_fall('p19_slots_nur_zustand', KS.format(slots="    __slots__ = ('stand',)\n\n", faktor=''),
       KS.format(slots="    __slots__ = ('stand',)\n\n", faktor='2 * '), LAST_K)
b_fall('p19b_kontrolle_ohne_slots', KS.format(slots='', faktor=''), KS.format(slots='', faktor='2 * '), LAST_K)
b_fall('p20_dataclass_slots', DC.format(faktor=''), DC.format(faktor='2 * '), LAST_K)
b_fall('p13_async', AS.format(1), AS.format(2), "import asyncio\nfrom paket.m.a import hole, eins\nasyncio.run(hole(3))\neins()")
b_fall('p14_endloser_iterator', IT.format('1'), IT.format('1 if n < start + 60 else 2'),
       "from itertools import islice\nfrom paket.m.a import zaehle\nlist(islice(zaehle(0), 100))")
b_fall('p16_klasse_ohne_vertrag_untypisiert', KU.format(ann='', d=1), KU.format(ann='', d=2), "from paket.m.a import eins\neins()")
b_fall('p16b_kontrolle_typisiert', KU.format(ann=': int', d=1), KU.format(ann=': int', d=2), "from paket.m.a import eins\neins()")
b_fall('p17_eigenschaft_multiplikativ', KP.format('self.stand * 2'), KP.format('self.stand * 3'), "from paket.m.a import eins\neins()")
a_fall('x1k_kontrolle_ohne_doppelt', K1, tests_aus(FAELLE))
a_fall('x2k_kontrolle_ohne_tab_aufruf', K2, x2_tests(False))
aus['_meta']['git_status_nachher'] = git('status', '--porcelain')
aus['_meta']['git_status_gleich'] = aus['_meta']['git_status_nachher'] == GIT_VORHER
sichern()
print('meta', aus['_meta'], flush=True)
