"""NACHHER-Messung (Kopie von vorher_6243377.py, nur Ausgabedatei/Kennung geändert): dieselben Fälle am Code von HEAD;
ursprünglich: Vorher-Messung am Code von 6243377 (Auftrag Runde 3: „die fünf Lücken der Python-Sonde je mit
einem Fall, der vorher unentdeckt blieb oder Fehlalarm gab“ — hier wird gemessen, dass es genau diese Fälle waren).

Ausgeführt werden die Tests der Gruppen A (fünf Lücken), D (Methoden) und B (Deckung je Muster) aus
tests/test_vor_t4_03.py — Prüfwerk, Diffs, Last und Ablauf (_pruefen: aegis.pruefen, echte Kammer biotop-kammer:1,
gestellt nur Modell und Laufzeitmessung) aus der Testdatei des NEUEN Commits, der Code (biotop/) aus `git archive 6243377`
(nur gelesen). Abschnitt F der Testdatei bleibt außen vor (braucht kern/gegenzeugen.py, das es an 6243377 nicht gibt).
Je Fall: Urteil an 6243377 (Status, Grund, Abweichungen, beobachtet) und ob die Zusicherung des neuen Tests dort hält.
Kein Modellaufruf. Aufruf: python vorher_6243377.py <Verzeichnis mit git archive 6243377>
"""
import json
import sys
import tempfile
import time
from pathlib import Path

ALT = Path(sys.argv[1]).resolve()
assert (ALT / 'biotop' / 'organe' / 'aegis.py').is_file(), ALT
sys.path.insert(0, str(ALT))
import biotop  # noqa: E402

assert Path(biotop.__file__).resolve().is_relative_to(ALT), biotop.__file__
TESTDATEI = Path('/root/biotop/tests/test_vor_t4_03.py')
text = TESTDATEI.read_text()
MARKE = '# ================================================================ F. Entscheidung 4'
assert text.count(MARKE) == 1
ns = {'__name__': 'vorher_6243377', '__file__': str(TESTDATEI)}
exec(compile(text[:text.index(MARKE)], 'test_vor_t4_03.py (Abschnitte A–E)', 'exec'), ns)
from biotop.organe import aegis, verhaltensvergleich  # noqa: E402

assert Path(aegis.__file__).resolve().is_relative_to(ALT) and Path(verhaltensvergleich.__file__).resolve().is_relative_to(ALT)
assert Path(ns['aegis'].__file__).resolve().is_relative_to(ALT)


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


urteile = []
original = ns['_pruefen']


def _pruefen(*a, **k):
    u, v = original(*a, **k)
    urteile.append((u, v))
    return u, v


ns['_pruefen'] = _pruefen
namen = [n for n in ns if n.startswith(('test_a', 'test_d', 'test_b')) and callable(ns[n])]
aus = {'_meta': {'code': sys.argv[2] if len(sys.argv) > 2 else 'HEAD (git archive)', 'code_pfad': str(ALT), 'testdatei': str(TESTDATEI),
                 'kammer': 'biotop-kammer:1', 'modellaufrufe': 0, 'faelle': []}}
for name in namen:
    params = [{}] if name != 'test_b_test_der_nur_nebenbei_ruft_deckt_nicht' else [{'haelt_fest': False}, {'haelt_fest': True}]
    for p in params:
        urteile.clear()
        mp = Monkeypatch()
        t0 = time.monotonic()
        with tempfile.TemporaryDirectory() as d:
            try:
                ns[name](Path(d), mp, **p)
                ausgang = 'Zusicherung hält'
            except AssertionError as e:
                ausgang = 'Zusicherung verletzt: ' + str(e)[:400]
            except Exception as e:  # noqa: BLE001 — ein Fehler ist ein Befund, kein stilles Weiter
                ausgang = f'Fehler {type(e).__name__}: {e}'[:500]
            finally:
                mp.undo()
        fall = name + (f"[haelt_fest={p['haelt_fest']}]" if p else '')
        rec = {'fall': fall, 'am_code_6243377': ausgang, 'dauer_s': round(time.monotonic() - t0, 1)}
        if urteile:
            u, v = urteile[-1]
            rec.update(status=u.get('status'), grund=(u.get('grund') or '')[:400], vv_grund_art=v.get('grund_art'),
                       abweichungen=v.get('anzahl_abweichungen'), beobachtet=v.get('beobachtete_funktionen'),
                       ungedeckt=(v.get('ungedeckt') or [])[:8], aufschluesselung=v.get('ungedeckt_aufschluesselung'),
                       enthaltungen=v.get('enthaltungen'), instanzen=v.get('instanzen'), hashsaat=v.get('hashsaat'))
        aus['_meta']['faelle'].append(fall)
        aus[fall] = rec
        print(f"{fall:72} {str(rec.get('status')):10} abw={rec.get('abweichungen')!s:5} beob={rec.get('beobachtet')!s:9} "
              f"| {ausgang[:110]} | {rec.get('grund', '')[:160]}", flush=True)
Path(__file__).with_name('NACHHER-HEAD.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1))
print(f"{len(aus['_meta']['faelle'])} Fälle am Code {aus['_meta']['code']}")
