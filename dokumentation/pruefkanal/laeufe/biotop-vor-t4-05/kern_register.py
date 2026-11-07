"""Register der verlangten Aufrufe (Behebungsrunde 5 vor T4, Entscheidung Chat-Claude 5, 24.09.2026).

Zum dritten Mal war etwas gebaut und nie gerufen (Lauf 38: verhaltensvergleich und masseichung; Review 04 Nr. 7: die
Torzeile „Schwächen“). Jede Funktion, deren Aufruf der Entwurf verlangt, steht hier — mit dem Aufrufer und der
Laufphase, in der sie laufen muss. Der Verdrahtungstest (tests/test_verdrahtung.py) fährt einen ganzen Lauf über die
Befehlszeile und verlangt jeden Eintrag als Aufrufkante „funktion ← aufrufer @ phase“; ein Eintrag ohne Kante macht
die Regression rot. Zusätzlich muss jedes Organmodul unter biotop/organe/ gerufen werden (Organliste aus dem
Verzeichnis, eigene Prüfung im selben Test).

Form je Eintrag: (funktion, aufrufer, phase, grund)
- funktion: „modul.name“ — Modul als Kurzname (Organ oder Kernmodul, siehe MODULE), wie der Aufzeichner die Kante
  schreibt;
- aufrufer: „paket.modul:funktion“ — der erste Rahmen außerhalb des Moduls der Funktion;
- phase: der Befehlsschritt des Laufs (vorspann, gen0, mass, generation, freigabe, tor4).
"""
from __future__ import annotations

# Kurzname → Modul, dessen Funktionen der Verdrahtungstest zusätzlich zu den Organen aufzeichnet.
MODULE = {
    "gegenzeugen": "biotop.kern.gegenzeugen",
    "tor4": "biotop.tor4",
    "messgeraet": "biotop.kern.messgeraet",
}

VERLANGT: tuple[tuple[str, str, str, str], ...] = (
    ("aegis.pruefen", "biotop.lauf:_generation_koerper", "generation",
     "Annahmepfad: jeder Kandidat durch den Ankläger"),
    ("masseichung.anwenden", "biotop.organe.aegis:pruefen", "generation",
     "Maßeichung im Annahmepfad (Befund Lauf 38)"),
    ("verhaltensvergleich.pruefen", "biotop.organe.aegis:pruefen", "generation",
     "Verhaltensvergleich im Annahmepfad (Befund Lauf 38, Tor 4 Zeile Verhaltensvergleich)"),
    ("messgeraet.laufzeit_gepaart", "biotop.organe.aegis:pruefen", "generation",
     "Laufzeit gepaart gemessen (Grundsatz 14, Vorbedingung 1)"),
    ("eichung.rauschmessung", "biotop.organe.vorspann:_ausfuehren", "vorspann",
     "Rauschmessung mit Sperren je Bereich (Generation minus eins)"),
    ("eichung.laufzeit_einmal", "biotop.organe.vorspann:_ausfuehren", "vorspann",
     "Rauschmessung an der Vergleichslast Stufe 2 mit dem Instrument der gepaarten Messung (Entscheidungen 1 und 6)"),
    ("masseichung.eichen", "biotop.organe.vorspann:_ausfuehren", "vorspann",
     "Maßeichung am sauberen Vergleichsbereich (Generation minus eins)"),
    ("eichproben.proben", "biotop.organe.vorspann:_ausfuehren", "vorspann",
     "4 Proben und 4 Gegenproben (Generation minus eins)"),
    ("tor4.ausfuehren", "biotop.__main__:main", "tor4",
     "Tor-4-Skript über die Befehlszeile (Entscheidung 5)"),
    ("gegenzeugen.torzeile_schwaechen", "biotop.tor4:ausfuehren", "tor4",
     "Torzeile „Schwächen“ mit doppelter Prüfung, verbindlich in der Torzeile (Entscheidung 5, Review 04 Nr. 7)"),
)


def kante(eintrag: tuple[str, str, str, str]) -> str:
    funktion, aufrufer, phase, _ = eintrag
    return f"{funktion} ← {aufrufer} @ {phase}"


def fehlend(kanten: set[str], verlangt=VERLANGT) -> list[str]:
    """Einträge ohne passende Aufrufkante (Aufrufer UND Phase müssen stimmen; anderswo gerufen zählt nicht)."""
    return sorted(kante(e) for e in verlangt if kante(e) not in kanten)
