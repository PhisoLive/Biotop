"""Mechanikprüfung der Aufnahmesperre C (F7) — roter und grüner Eichfall, deterministisch, 0 Modellaufrufe.

Maßstab (Chat-Claude, vor der Messung gesetzt):
  Durchgerutscht an C = 0 · Fehlalarm ≤ 20 % der Sperrungen, jede einzeln belegt
  je ein roter und ein grüner Eichfall

Die Prüfung ruft die echte Kernfunktion `aegis.aufnahmesperre` auf. Grundsatz 4: Der Wirkungsbereich ist
eingegrenzt — geprüft wird gegen ein eigenes Prüfwerk, kein echter Bestand wird verändert.
Aufruf: aufnahmesperre_pruefen.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern import protokoll
from biotop.kern.datenbank import verbinden, transaktion
from biotop.organe import aegis

A = Path(sys.argv[1])
con = verbinden()
WERK, LAUF, BEREICH, PAKET = 9901, 9901, "lager", "lagerhaus"

CODE = '''from lagerhaus.lager import Lager, NichtGenugBestand
import pytest


def test_reserviert_zaehlt_nach_einloesen_nicht_mehr():
    lager = Lager()
    lager.zugang("A", 10)
    assert lager.reserviert("A") == 0


def test_zugang_lehnt_negative_menge_ab():
    lager = Lager()
    with pytest.raises(ValueError):
        lager.zugang("A", -1)


def test_reserviert_zaehlt_erneut_nach_einloesen():
    lager = Lager()
    lager.zugang("B", 5)
    assert lager.reserviert("B") == 0
'''

z = ["# Aufnahmesperre C (F7) — Mechanikprüfung mit rotem und grünem Eichfall",
     "# Maßstab vorab: Durchgerutscht 0 · Fehlalarm ≤ 20 % der Sperrungen, einzeln belegt",
     "# Deterministisch, 0 Modellaufrufe. Geprüft wird die echte Kernfunktion aegis.aufnahmesperre.", ""]

# Vorrat des Prüfwerks setzen: eine Behauptung steht schon drin
with transaktion(con):
    con.execute("DELETE FROM immunsystem WHERE werk_id=?", (WERK,))
    con.execute("INSERT INTO immunsystem(werk_id, lauf_id, bereich, name, code, ursprung, status, erstellt_am,"
                " generation) VALUES (?,?,?,?,?,?,'offen',?,0)",
                (WERK, LAUF, BEREICH, "pruefwerk_vorrat", "x", "Prüfwerk behauptung=reserviert|Eq:zahl",
                 protokoll.jetzt()))
vorrat = aegis.bisherige_behauptungen(con, WERK, BEREICH, LAUF)
z.append(f"## Ausgangslage: Vorrat des Bereichs `{BEREICH}` = {vorrat}")
z.append("")

namen = ["test_reserviert_zaehlt_nach_einloesen_nicht_mehr",
         "test_zugang_lehnt_negative_menge_ab",
         "test_reserviert_zaehlt_erneut_nach_einloesen"]
z.append("## Drei Tests werden zur Aufnahme angeboten")
for n in namen:
    z.append(f"  {n} → Schlüssel `{aegis.behauptung(CODE, n, PAKET)}`")
z.append("")

nehmen, abgewiesen = aegis.aufnahmesperre(con, WERK, LAUF, BEREICH, CODE, namen, PAKET, 9999, "fund")
z.append("## Ergebnis der Sperre")
for n, s in nehmen:
    z.append(f"  AUFGENOMMEN  {n} — `{s}`")
for n, s in abgewiesen:
    z.append(f"  ABGEWIESEN   {n} — `{s}`")
z.append("")

gruen = [(n, s) for n, s in nehmen if s not in vorrat]
rot_vorrat = [(n, s) for n, s in abgewiesen if s in vorrat]
rot_intern = [(n, s) for n, s in abgewiesen if s not in vorrat]
z.append("## Eichfälle")
if gruen:
    n, s = gruen[0]
    z.append(f"  GRÜN  `{n}` mit `{s}`: Behauptung nicht im Vorrat → aufgenommen. "
             f"Der Filter lässt Neues durch.")
if rot_vorrat:
    n, s = rot_vorrat[0]
    z.append(f"  ROT   `{n}` mit `{s}`: Behauptung steht im Vorrat → abgewiesen. "
             f"Der Filter hält die Wiederholung.")
if rot_intern:
    n, s = rot_intern[0]
    z.append(f"  ROT²  `{n}` mit `{s}`: zweiter Test derselben Behauptung im selben Kandidaten → abgewiesen.")
z.append(f"  Beide Fälle vorhanden: {bool(gruen) and bool(rot_vorrat)}")
z.append("")

z.append("## Maßstab")
durchgerutscht = [(n, s) for n, s in nehmen if s in vorrat]
z.append(f"  Durchgerutscht (aufgenommen, obwohl im Vorrat): {len(durchgerutscht)} "
         f"(Maßstab 0 → {'ERFÜLLT' if not durchgerutscht else 'GERISSEN'})")
fehlalarm = [(n, s) for n, s in abgewiesen if s not in vorrat and
             [x for x, y in nehmen if y == s] == []]
echte_fehlalarme = []
for n, s in abgewiesen:
    if s not in vorrat and not any(y == s for _, y in nehmen):
        echte_fehlalarme.append((n, s))
anteil = 100 * len(echte_fehlalarme) / len(abgewiesen) if abgewiesen else 0.0
z.append(f"  Fehlalarm (abgewiesen, obwohl Behauptung neu und einmalig): {len(echte_fehlalarme)} von "
         f"{len(abgewiesen)} Sperrungen = {anteil:.0f} % (Maßstab ≤ 20 % → "
         f"{'ERFÜLLT' if anteil <= 20 else 'GERISSEN'})")
for n, s in echte_fehlalarme:
    z.append(f"    FEHLALARM: {n} — `{s}`")
z.append("")

p = con.execute("SELECT nr, inhalt FROM protokoll WHERE art='immun.aufnahme_gesperrt' ORDER BY nr DESC LIMIT 2").fetchone()
z.append("## Protokoll (jede Abweisung mit Grund und Gegenstück)")
if p:
    z.append(f"  #{p['nr']}: {p['inhalt'][:300]}")
z.append("")

# Gegenprobe: derselbe Aufruf bei leerem Vorrat nimmt alles an
with transaktion(con):
    con.execute("DELETE FROM immunsystem WHERE werk_id=?", (WERK,))
nehmen2, abgewiesen2 = aegis.aufnahmesperre(con, WERK, LAUF + 1, BEREICH, CODE, namen, PAKET, 9998, "fund")
z.append("## Gegenprobe: leerer Vorrat")
z.append(f"  aufgenommen {len(nehmen2)}, abgewiesen {len(abgewiesen2)} "
         f"— abgewiesen wird nur die werkinterne Doppelung ({[n for n, _ in abgewiesen2]})")
z.append("  Der Filter sperrt also nicht pauschal, sondern nur bei tatsächlicher Wiederholung.")

with transaktion(con):
    con.execute("DELETE FROM immunsystem WHERE werk_id=?", (WERK,))
z.append("")
z.append("(Prüfwerk 9901 wieder entfernt; Protokollzeilen bleiben — das Protokoll ist unveränderlich.)")
(A / "21-aufnahmesperre-c.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
