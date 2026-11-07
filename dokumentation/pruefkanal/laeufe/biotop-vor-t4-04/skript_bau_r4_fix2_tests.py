"""Behebungsrunde 4 vor T4 — test_vor_t4_03 Gruppe B an die Entscheidung 2 anpassen (TEILLAUF-3: 3 rot). Die Runde-3-
Fälle setzten ein gemeinsames Merkmal `weissraum` voraus; mit „jede Formvariante ist ein eigenes Merkmal“ braucht eine
richtige Behebung einen Test je Formvariante, die die Sonde zeigt (Tab, Zeilenumbruch, CRLF, NBSP, doppelt …). Das ist
Spezifikationsänderung, keine zugedeckte Regression; jede Stelle trägt eine Notiz. Alles-oder-nichts.
"""
import py_compile
from pathlib import Path

T = Path('/root/biotop/tests/test_vor_t4_03.py')
t = T.read_text()
ops = [
('''    # Jeder Test fällt an der Vorgeneration (dort " " statt "_") und besteht am Kandidaten; je Muster einer.
    faelle = {"gewoehnlich": ("a b", "a_b"), "weissraum": ("a\\tb\\nc", "a_b_c"), "rand": (" a b ", "a_b"),
              "gross": ("A B", "A_B"), "lang": ("x " * 25, "_".join(["x"] * 25)),
              "zahlform": ("a 01 2.50", "a_01_2.50"), "nichtascii": ("Ä ö", "Ä_ö"), "doppelt": ("a  b", "a_b")}''',
 '''    # Jeder Test fällt an der Vorgeneration (dort " " statt "_") und besteht am Kandidaten; je Muster einer.
    # Geändert in Runde 4 (Entscheidung 2: jede Formvariante ein eigenes Merkmal): Tab, Zeilenumbruch, CRLF und NBSP
    # je ein eigener Test statt eines gemeinsamen Weißraum-Tests.
    faelle = {"gewoehnlich": ("a b", "a_b"), "tab": ("a\\tb", "a_b"), "zeilenumbruch": ("a\\nb", "a_b"),
              "crlf": ("a\\r\\nb", "a_b"), "nbsp": ("a\\u00a0b", "a_b"), "rand": (" a b ", "a_b"),
              "gross": ("A B", "A_B"), "lang": ("x " * 25, "_".join(["x"] * 25)),
              "zahlform": ("a 01 2.50", "a_01_2.50"), "nichtascii": ("Ä ö", "Ä_ö"), "doppelt": ("a  b", "a_b")}'''),
('''    assert v["ungedeckt"] and all("weissraum" in s for s in v["ungedeckt_aufschluesselung"]), v["ungedeckt_aufschluesselung"]''',
 '''    # Geändert in Runde 4 (Entscheidung 2): die ungedeckten Muster sind die einzelnen Weißraum-Formvarianten.
    weiss = {"tab", "zeilenumbruch", "crlf", "cr", "nbsp", "doppelleer", "weissraum_sonst"}
    assert v["ungedeckt"] and all(set(s.split(" | ")[1].split("+")) & weiss for s in v["ungedeckt_aufschluesselung"]), \\
        v["ungedeckt_aufschluesselung"]'''),
('''    halter = festhaltend.get("probewerk.werk.kern:normieren|rueckgabe") or []''',
 '''    # Geändert in Runde 4 (Verfälschung je Merkmal): der Schlüssel trägt das Merkmal; '' = gewöhnliches Muster.
    halter = festhaltend.get("probewerk.werk.kern:normieren|rueckgabe|") or []'''),
]
fehl = [(a[:60], t.count(a)) for a, b in ops if t.count(a) != 1]
if fehl:
    raise SystemExit(f'Anker fehlen, nichts geschrieben: {fehl}')
for a, b in ops:
    t = t.replace(a, b)
T.write_text(t)
py_compile.compile(str(T), doraise=True)
print('test_vor_t4_03 Gruppe B: 3 von 3 Ersetzungen')
