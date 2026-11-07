"""Python-Prüfwerk „speicherwerk“ (Behebungsrunde 2 vor T4): kleinstes Python-Werk, an dem die Python-Sonde des
Verhaltensvergleichs durch den Annahmepfad (aegis.pruefen) geprüft wird — Gegenprobe des Auftrags: „an einem
Python-Prüfwerk scheitert ein eingebauter Zwischenspeicher-Fehler“.

- speicherwerk/zahlen/statistik.py: `summe(werte)`, `spannweite(werte)` — rein, sortieren eine Kopie.
- speicherwerk/text/format.py: `normieren(text)` — Weißraumfolgen (auch Tab/Zeilenumbruch) zu einem Leerzeichen.
- Referenzlast: last_zahlen/last_text (Arbeit im Bereich einiger Millisekunden), beobachten() als Raster.
- Kandidat ZWISCHENSPEICHER (Nische schnell): `spannweite` merkt sich das Ergebnis an der REFERENZ der Liste
  (id(werte)) — nach einer Änderung an Ort und Stelle liefert sie das alte Ergebnis (T3-Muster K2934/K3121: 8 statt 80).
  Gegenprobe: derselbe Speicher, aber am INHALT (tuple(werte)) — verhaltensgleich.
- Kandidat WEISSRAUM: `normieren` nur noch für Leerzeichen — Tab und Zeilenumbruch bleiben stehen (T3-Muster K2868).
  Kein Test und keine Referenzlast nutzt Tab: nur die Formvarianten des Korpus sehen es.
Kein Modell, keine Netzwirkung; die Kammer ist das Python-Image biotop-kammer:1.
"""
from __future__ import annotations

import difflib

PAKET = "speicherwerk"
STATISTIK = '''"""Kleine Statistik über Zahlenlisten."""


def summe(werte: list[float]) -> float:
    """Summe aller Werte (leere Liste: 0)."""
    s = 0.0
    for w in werte:
        s += w
    return s


def spannweite(werte: list[float]) -> float:
    """Größter minus kleinster Wert (leere Liste: 0). Die Eingabe bleibt unverändert."""
    if not werte:
        return 0.0
    geordnet = sorted(werte)
    return geordnet[-1] - geordnet[0]
'''
FORMAT = '''"""Textnormierung."""


def normieren(text: str) -> str:
    """Weißraumfolgen (Leerzeichen, Tab, Zeilenumbruch) werden zu einem Leerzeichen, Ränder entfernt."""
    return " ".join(text.split())


def _alt_normieren(text: str) -> str:
    """Frühere Fassung, nirgends mehr aufgerufen (toter Code — Vulture zählt ihn)."""
    return text.strip()
'''
TESTS_ZAHLEN = '''from speicherwerk.zahlen.statistik import spannweite, summe


def test_zahlen_summe():
    assert summe([1.0, 2.0, 3.5]) == 6.5


def test_zahlen_spannweite():
    assert spannweite([4.0, 1.0, 9.0]) == 8.0
'''
TESTS_TEXT = '''from speicherwerk.text.format import normieren


def test_text_normieren():
    assert normieren("  a   b  ") == "a b"
'''
REFERENZLAST = '''# Referenzlast für das Prüfwerk „speicherwerk“ (Kern, Messgerät).
import sys
sys.path.insert(0, "/werk")


def last_zahlen():
    from speicherwerk.zahlen.statistik import spannweite, summe
    werte = [float((i * 37) % 101) for i in range(400)]
    for _ in range(40):
        summe(werte)
        spannweite(werte)


def last_text():
    from speicherwerk.text.format import normieren
    for i in range(400):
        normieren("  wort   " * (1 + i % 5))


def beobachten():
    from speicherwerk.zahlen.statistik import spannweite, summe
    from speicherwerk.text.format import normieren
    return {"summe": summe([1.0, 2.0]), "spannweite": spannweite([3.0, 1.0]), "normieren": normieren(" a  b ")}
'''
DATEIEN = {
    "pyproject.toml": '[project]\nname = "speicherwerk"\nversion = "0.1.0"\n',
    "README.md": "# speicherwerk\n\nPrüfwerk ohne Betriebszweck für den Verhaltensvergleich (Python).\n",
    "speicherwerk/__init__.py": "",
    "speicherwerk/zahlen/__init__.py": "",
    "speicherwerk/zahlen/statistik.py": STATISTIK,
    "speicherwerk/text/__init__.py": "",
    "speicherwerk/text/format.py": FORMAT,
    "tests/test_zahlen.py": TESTS_ZAHLEN,
    "tests/test_text.py": TESTS_TEXT,
}


def _diff(rel: str, alt: str, neu: str) -> str:
    return "".join(difflib.unified_diff(alt.splitlines(True), neu.splitlines(True), f"a/{rel}", f"b/{rel}"))


def zwischenspeicher_falsch() -> str:
    """spannweite merkt sich das Ergebnis an der Referenz der Liste — veraltet nach Änderung an Ort und Stelle."""
    neu = STATISTIK.replace('''def spannweite(werte: list[float]) -> float:
    """Größter minus kleinster Wert (leere Liste: 0). Die Eingabe bleibt unverändert."""
    if not werte:
        return 0.0
    geordnet = sorted(werte)
    return geordnet[-1] - geordnet[0]
''', '''_SPEICHER: dict[int, float] = {}


def spannweite(werte: list[float]) -> float:
    """Größter minus kleinster Wert (leere Liste: 0). Die Eingabe bleibt unverändert."""
    schluessel = id(werte)
    if schluessel in _SPEICHER:
        return _SPEICHER[schluessel]
    if not werte:
        return 0.0
    ergebnis = max(werte) - min(werte)
    _SPEICHER[schluessel] = ergebnis
    return ergebnis
''')
    assert neu != STATISTIK
    return _diff("speicherwerk/zahlen/statistik.py", STATISTIK, neu)


def zwischenspeicher_richtig() -> str:
    """Gegenprobe: Speicher am INHALT der Liste — verhaltensgleich."""
    neu = STATISTIK.replace('''def spannweite(werte: list[float]) -> float:
    """Größter minus kleinster Wert (leere Liste: 0). Die Eingabe bleibt unverändert."""
    if not werte:
        return 0.0
    geordnet = sorted(werte)
    return geordnet[-1] - geordnet[0]
''', '''_SPEICHER: dict[tuple, float] = {}


def spannweite(werte: list[float]) -> float:
    """Größter minus kleinster Wert (leere Liste: 0). Die Eingabe bleibt unverändert."""
    schluessel = tuple(werte)
    if schluessel in _SPEICHER:
        return _SPEICHER[schluessel]
    ergebnis = (max(werte) - min(werte)) if werte else 0.0
    _SPEICHER[schluessel] = ergebnis
    return ergebnis
''')
    assert neu != STATISTIK
    return _diff("speicherwerk/zahlen/statistik.py", STATISTIK, neu)


_TOT = '''

def _alt_normieren(text: str) -> str:
    """Frühere Fassung, nirgends mehr aufgerufen (toter Code — Vulture zählt ihn)."""
    return text.strip()
'''


def toter_code_entfernt() -> str:
    """Nur der tote Code entfällt (Kernmaß +1) — verhaltensgleich (Gegenprobe)."""
    neu = FORMAT.replace(_TOT, "\n")
    assert neu != FORMAT
    return _diff("speicherwerk/text/format.py", FORMAT, neu)


def weissraum_falsch() -> str:
    """Toten Code entfernt (Kernmaß +1) UND normieren nur noch für Leerzeichen — Tab und Zeilenumbruch bleiben stehen
    (T3-Muster K2868). Kein Test und keine Referenzlast nutzt Tab; nur die Formvarianten des Korpus sehen es."""
    neu = FORMAT.replace(_TOT, "\n").replace('    return " ".join(text.split())\n',
                                             '    return " ".join(t for t in text.split(" ") if t)\n')
    assert neu != FORMAT and "_alt_normieren" not in neu
    return _diff("speicherwerk/text/format.py", FORMAT, neu)


def anlegen(ziel) -> None:
    from pathlib import Path
    ziel = Path(ziel)
    for rel, inhalt in DATEIEN.items():
        p = ziel / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(inhalt)
