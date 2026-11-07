"""Review vor T4-03 — Laufweg-Proben der Deckung je Muster durch aegis.pruefen (echte Kammer biotop-kammer:1, gestellt
nur Modell und Laufzeit — derselbe Ablauf wie tests/test_vor_t4_03.py::_pruefen, Prüfwerk `probewerk`, Code von HEAD).
x1  Kandidat: normieren mit beabsichtigter Änderung (" " → "_") UND verdecktem Rückschritt (Tab/Zeilenumbruch →
    ValueError, die K2868-Lage). Soll-Tests im Werk je Muster OHNE Tab/Zeilenumbruch, aber mit doppeltem Leerzeichen.
x1k Kontrolle: dieselben Tests ohne den Test mit doppeltem Leerzeichen.
x2  Kandidat: " " → "_", verdeckt: Text mit Tab kommt unverändert zurück. Ein Test ruft normieren("a\\tb c") OHNE
    Zusicherung und sichert nur normieren("a b") zu; übrige Soll-Tests ohne Weißraum-Eingabe.
x2k Kontrolle: derselbe Test ohne den Tab-Aufruf.
Kein Modell, kein Netz. Nichts wird unter /root/biotop geschrieben (sys.dont_write_bytecode, tmp unter /tmp/review-vor-t4-03)."""
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.dont_write_bytecode = True
if subprocess.run(['pgrep', '-f', 'job_commit_regression'], capture_output=True, text=True).stdout.strip():
    sys.exit('job_commit_regression läuft — keine Kammerläufe')
sys.path.insert(0, '/root/biotop')
TESTDATEI = Path('/root/biotop/tests/test_vor_t4_03.py')
text = TESTDATEI.read_text()
MARKE = '# ================================================================ F. Entscheidung 4'
ns = {'__name__': 'deckprobe', '__file__': str(TESTDATEI)}
exec(compile(text[:text.index(MARKE)], 'test_vor_t4_03.py (A–E, nur gelesen)', 'exec'), ns)
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

GIT_VORHER = subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True, text=True).stdout


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
    t = {k: v for k, v in tests_aus({k: v for k, v in FAELLE.items() if k != "gewoehnlich"}).items()}
    koerper = ('    normieren("a\\tb c")\n' if mit_tab else '') + '    assert normieren("a b") == "a_b"\n'
    t["tests/test_werk_normieren_x.py"] = "from probewerk.werk.kern import normieren\n\n\ndef test_normieren_x():\n" + koerper
    return t


PROBEN = {
    'x1_doppeltes_leerzeichen_deckt_tab_und_lf': (K1, tests_aus({**FAELLE, "doppelt": ("a  b", "a_b")})),
    'x1k_kontrolle_ohne_doppelt': (K1, tests_aus(FAELLE)),
    'x2_tab_nur_gerufen_nicht_zugesichert': (K2, x2_tests(True)),
    'x2k_kontrolle_ohne_tab_aufruf': (K2, x2_tests(False)),
}
aus = {}
for name, (koerper, tests) in PROBEN.items():
    neu = QUELLE.replace(ALT_ZEILE, koerper)
    assert neu != QUELLE
    mp = Monkeypatch()
    letzte = {}
    orig_vergleichen = vv.vergleichen

    def fang(alt, neu_, gedeckt, _o=orig_vergleichen):
        letzte.update(alt=dict(alt), neu=dict(neu_), gedeckt=set(gedeckt))
        return _o(alt, neu_, gedeckt)
    t0 = time.monotonic()
    with tempfile.TemporaryDirectory(dir='/tmp/review-vor-t4-03/tmp') as d:
        try:
            mp.setattr(vv, 'vergleichen', fang)
            u, v = ns['_pruefen'](Path(d), mp, ns['_diff'](QUELLE, neu), nische="sicher", werk_extra=tests)
        finally:
            mp.undo()
    a, n, g = letzte.get('alt', {}), letzte.get('neu', {}), letzte.get('gedeckt', set())
    abw = [k for k in sorted(set(a) | set(n)) if a.get(k) != n.get(k)]
    # verdeckter Rückschritt: Beobachtungen, deren Eingabe Tab/LF enthält (K1: ValueError am Kandidaten; K2: Text unverändert)
    rueck = [k for k in abw if (k.startswith('probewerk.werk.kern:normieren')
                                and (str(n.get(k, '')).startswith('Fehler:ValueError')
                                     or (koerper is K2 and '\\t' in str(n.get(k, '')))))]
    e = {'status': u.get('status'), 'grund': str(u.get('grund'))[:240], 'abweichungen': len(abw),
         'ungedeckt': len(v.get('ungedeckt_alle') or v.get('ungedeckt') or []),
         'rueckschritt_beobachtungen': len(rueck), 'rueckschritt_davon_gedeckt': sum(1 for k in rueck if k in g),
         'rueckschritt_beispiele': {k: [a.get(k), n.get(k), (v.get('gedeckt') or {}).get(k)] for k in rueck[:4]},
         'deckung_zaehlung': v.get('deckung_zaehlung'), 'ungedeckt_aufschluesselung': v.get('ungedeckt_aufschluesselung'),
         'tests': sorted(tests), 'dauer_s': round(time.monotonic() - t0, 1)}
    aus[name] = e
    print(name, json.dumps(e, ensure_ascii=False)[:2200], flush=True)
GIT_NACHHER = subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True, text=True).stdout
aus['_meta'] = {'git_status_gleich': GIT_VORHER == GIT_NACHHER, 'git_status': GIT_NACHHER[:300], 'modellaufrufe': 0,
                'head': subprocess.run(['git', '-C', '/root/biotop', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()}
print('meta', aus['_meta'])
Path('/tmp/review-vor-t4-03/DECKPROBE.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
