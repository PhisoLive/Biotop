"""Review vor T4-04 — Probe x4 (Laufweg aegis.pruefen, echte Kammer, HEAD): Lesart „Randwerte tragen kein Merkmal“.
Kandidat: richtige Behebung („ “ → „_“, Weißraum wie Leerzeichen) UND verdeckter Rückschritt: lange Eingaben (≥ 40 Zeichen)
werfen ValueError. Tests je Formvariante wie die H1-Gegenprobe, aber OHNE den Test mit langer Eingabe — kein Test ruft
normieren mit einer langen Eingabe. Frage: ist die Randfall-Abweichung an 'x'×40 gedeckt (Muster [])?
x4k Kontrolle: derselbe Kandidat ohne den Rückschritt (nur die richtige Behebung)."""
import importlib.util
import json
import os
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
spec = importlib.util.spec_from_file_location('vh', '/root/biotop/biotop/kern/py/verhalten.py')
vh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vh)
print('Randlisten str:', [l for l in vh.argumentlisten(['str'], None)][:8])
TESTDATEI = Path('/root/biotop/tests/test_vor_t4_03.py')
text = TESTDATEI.read_text()
ns = {'__name__': 'x4probe', '__file__': str(TESTDATEI)}
exec(compile(text[:text.index('# ================================================================ F. Entscheidung 4')],
             'test_vor_t4_03.py (A–E, nur gelesen)', 'exec'), ns)
from biotop.organe import verhaltensvergleich as vv  # noqa: E402


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
ALT = '    return " ".join(text.split())\n'
RICHTIG = '    return "_".join(text.split())\n'
K4 = '    if len(text) >= 40:\n        raise ValueError("zu lang")\n    return "_".join(text.split())\n'
FAELLE = {"gewoehnlich": ("a b", "a_b"), "rand": (" a b ", "a_b"), "gross": ("A B", "A_B"), "zahlform": ("a 01 2.50", "a_01_2.50"),
          "nichtascii": ("Ä ö", "Ä_ö"), "tab": ("a\tb", "a_b"), "lf": ("a\nb", "a_b"), "crlf": ("a\r\nb", "a_b"),
          "nbsp": ("a\u00a0b", "a_b"), "doppelt": ("a  b", "a_b")}
TESTS = {f"tests/test_werk_normieren_{n}.py": T.format(name=n, eingabe=e, erwartet=x) for n, (e, x) in FAELLE.items()}
aus = {'head': subprocess.run(['git', '-C', '/root/biotop', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()}
for name, koerper in (('x4_lange_eingabe_wirft', K4), ('x4k_kontrolle_nur_behebung', RICHTIG)):
    neu = QUELLE.replace(ALT, koerper)
    assert neu != QUELLE
    mp = Monkeypatch()
    letzte = {}
    orig = vv.vergleichen

    def fang(alt, neu_, gedeckt, _o=orig):
        letzte.update(alt=dict(alt), neu=dict(neu_), gedeckt=set(gedeckt))
        return _o(alt, neu_, gedeckt)
    t0 = time.monotonic()
    with tempfile.TemporaryDirectory(dir=str(R / 'tmp')) as d:
        try:
            mp.setattr(vv, 'vergleichen', fang)
            u, v = ns['_pruefen'](Path(d), mp, ns['_diff'](QUELLE, neu), nische="sicher", werk_extra=TESTS)
        finally:
            mp.undo()
    a, n, g = letzte.get('alt', {}), letzte.get('neu', {}), letzte.get('gedeckt', set())
    abw = [k for k in sorted(set(a) | set(n)) if a.get(k) != n.get(k)]
    rueck = [k for k in abw if str(n.get(k, '')).startswith('Fehler:ValueError')]
    e = {'status': u.get('status'), 'grund': str(u.get('grund'))[:200], 'abweichungen': len(abw),
         'rueckschritt': rueck, 'rueckschritt_gedeckt': {k: (v.get('gedeckt') or {}).get(k) for k in rueck},
         'rueckschritt_eingaben': {k: str((v.get('eingaben') or {}).get(k))[:80] for k in rueck[:3]},
         'muster_rueckschritt': sorted({s for s in (v.get('ungedeckt_aufschluesselung') or {})}),
         'dauer_s': round(time.monotonic() - t0, 1)}
    aus[name] = e
    print(name, json.dumps(e, ensure_ascii=False)[:1400], flush=True)
aus['git_status'] = subprocess.run(['git', '-C', '/root/biotop', 'status', '--porcelain'], capture_output=True, text=True).stdout
(R / 'X4PROBE.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
print('git_status leer:', aus['git_status'] == '')
