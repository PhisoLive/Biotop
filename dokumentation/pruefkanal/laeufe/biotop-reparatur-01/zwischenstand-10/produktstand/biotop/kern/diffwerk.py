"""Kern: Diff-Anwendung — tolerant gegenüber falschen Hunk-Zählern.

Modelle liefern häufig unified diffs mit falschen `@@ -a,b +c,d @@`-Zählern.
Hier wird ein Hunk als (alter Block, neuer Block) gelesen und der alte Block
im Text gesucht — erst exakt, dann mit abgeschnittenem Weißraum am
Zeilenende. Das ist deterministisch; kein Modell beurteilt etwas.

Regel (3.6 Fassung 2): Ein Hunk, dessen alter Block mehr als 60 % der Datei
ersetzt, ist eine Neuschreibung und wird abgelehnt — AUSSER die Datei hat unter
100 Zeilen; dann ist die Neuschreibung ein zulässiger Kandidat (die Verträge
prüft der Ankläger paarweise).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

NEUSCHREIBUNG_ANTEIL = 0.60
NEUSCHREIBUNG_KLEINE_DATEI = 100  # Zeilen; darunter ist Neuschreibung erlaubt (3.6 F2)


class DiffFehler(ValueError):
    pass


@dataclass
class Hunk:
    alt: list[str] = field(default_factory=list)
    neu: list[str] = field(default_factory=list)


@dataclass
class DateiDiff:
    pfad: str
    hunks: list[Hunk]
    neu_angelegt: bool = False
    geloescht: bool = False


def parsen(diff: str) -> list[DateiDiff]:
    dateien: list[DateiDiff] = []
    aktuell: DateiDiff | None = None
    hunk: Hunk | None = None
    for zeile in diff.splitlines():
        if zeile.startswith("diff --git"):
            continue
        if zeile.startswith("--- "):
            quelle = zeile[4:].strip()
            aktuell = DateiDiff(pfad="", hunks=[], neu_angelegt=(quelle == "/dev/null"))
            hunk = None
            continue
        if zeile.startswith("+++ "):
            ziel = zeile[4:].strip()
            if aktuell is None:
                aktuell = DateiDiff(pfad="", hunks=[])
            if ziel == "/dev/null":
                aktuell.geloescht = True
            else:
                aktuell.pfad = re.sub(r"^[ab]/", "", ziel.split("\t")[0])
            dateien.append(aktuell)
            continue
        if zeile.startswith("@@"):
            if aktuell is None:
                raise DiffFehler("Hunk ohne Datei")
            hunk = Hunk()
            aktuell.hunks.append(hunk)
            continue
        if hunk is None:
            continue
        if zeile.startswith("+"):
            hunk.neu.append(zeile[1:])
        elif zeile.startswith("-"):
            hunk.alt.append(zeile[1:])
        elif zeile.startswith("\\"):
            continue
        else:
            inhalt = zeile[1:] if zeile.startswith(" ") else zeile
            hunk.alt.append(inhalt)
            hunk.neu.append(inhalt)
    for d in dateien:
        if not d.pfad and not d.geloescht:
            raise DiffFehler("Datei ohne Zielpfad")
    return dateien


def _finden(zeilen: list[str], block: list[str], ab: int) -> int:
    n = len(block)
    if n == 0:
        return -1
    for i in range(ab, len(zeilen) - n + 1):
        if zeilen[i:i + n] == block:
            return i
    r = [z.rstrip() for z in block]
    for i in range(ab, len(zeilen) - n + 1):
        if [z.rstrip() for z in zeilen[i:i + n]] == r:
            return i
    return -1


def anwenden(text: str | None, d: DateiDiff) -> str | None:
    """Wendet einen Datei-Diff auf `text` an. Rückgabe: neuer Text (None = gelöscht)."""
    if d.geloescht:
        return None
    if text is None:
        if not d.neu_angelegt and any(h.alt for h in d.hunks):
            raise DiffFehler(f"{d.pfad}: Datei fehlt")
        return "\n".join(z for h in d.hunks for z in h.neu) + "\n"
    zeilen = text.split("\n")
    if zeilen and zeilen[-1] == "":
        zeilen.pop()
    gesamt = max(1, len(zeilen))
    pos = 0
    for h in d.hunks:
        if len(h.alt) / gesamt > NEUSCHREIBUNG_ANTEIL and len(h.alt) > 20 and gesamt >= NEUSCHREIBUNG_KLEINE_DATEI:
            raise DiffFehler(f"{d.pfad}: Hunk ersetzt {len(h.alt)} von {gesamt} Zeilen — Neuschreibung einer Datei ≥ {NEUSCHREIBUNG_KLEINE_DATEI} Zeilen, nicht erlaubt")
        if not h.alt:
            # reines Einfügen ohne Kontext: am Ende anhängen
            zeilen[len(zeilen):] = h.neu
            continue
        i = _finden(zeilen, h.alt, pos)
        if i < 0:
            i = _finden(zeilen, h.alt, 0)
        if i < 0:
            raise DiffFehler(f"{d.pfad}: Kontext nicht gefunden: {h.alt[0][:60]!r} …")
        zeilen[i:i + len(h.alt)] = h.neu
        pos = i + len(h.neu)
    return "\n".join(zeilen) + "\n"
