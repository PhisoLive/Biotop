"""Füllt die Platzhalter im BERICHT der Behebungsrunde 4 (Nachtrag in der Sitzung der Runde 5).
Sperrwortlaute werden nur aus ihren Belegdateien gelesen (sperre/FORMATSPERRE-1.txt, REVIEW.md Abschnitt „Sperren“).
Zahlen stammen aus den Belegen (REVIEW.md „Geprüft und bestätigt“, NACHSPIEL-N1..3, REGRESSION*.txt)."""
import re
from pathlib import Path

A = Path('/root/biotop-vor-t4-04')
b = (A / 'BERICHT.md').read_text()
review = (A / 'REVIEW.md').read_text()
sperre1 = (A / 'sperre/FORMATSPERRE-1.txt').read_text()

# Belegprüfung der Kernzahlen (Abbruch, wenn eine Quelle nicht passt)
reg1 = (A / 'REGRESSION.txt').read_text().strip().splitlines()[-1]
reg2 = (A / 'REGRESSION-2.txt').read_text().strip().splitlines()[-1]
assert reg1.startswith('562 passed, 2 skipped') and reg2.startswith('569 passed, 2 skipped'), (reg1, reg2)
n = ''.join((A / f'nachspiel/NACHSPIEL-N{i}.txt').read_text() for i in (1, 2, 3))
assert n.count('erfuellt=True') == 7 and n.count('erfuellt=False') == 0, 'Nachspiele N1–N3'

URTEIL = ('Gegenproben der Entscheidungen 1, 3 und 4 erfüllt; die vier hohen Befunde sind für ihre Probenfälle '
          'geschlossen, die Fehlerklassen nicht (Review: 2 neue hohe Befunde, an Runde 5)')

ERGEBNIS = """- **Entscheidung 1 (Stufe 2):** 12 von 12 Kammerläufen der Stufe 2 unter 60 s (längster 11,7 s). K2904 und K3091
  überleben an Stufe 2 in je 3 von 3 Durchgängen (N1–N3 am Nachtrag `43b8fad`), `planung`-Quote 0,376–0,455, alle
  „klar“ unter dem Band. Aber: `eingang` war in 3 von 6 Stufe-2-Nachspielen gesperrt (Offen Nr. 2).
- **Entscheidung 2 (vier hohe Befunde):** die 23 neuen Testfälle 6 von 23 grün an `0aac612`, 23 von 23 an `1d9a5aa`; das
  Review fuhr 14 von 16 Originalproben an `43b8fad` neu, 14 von 14 wie spezifiziert. **Nicht geschlossen sind die
  Klassen:** ein Test hält ein Merkmal fest, ohne es zu unterscheiden (Review Nr. 1, gemessen durch `aegis.pruefen`:
  Kandidat überlebt), und `__slots__` mit Vererbung bleibt still (Nr. 2: 0 statt 28 Abweichungen).
- **Entscheidung 3 (Muster):** K2868 abgelehnt, 16 von 40 Abweichungen gedeckt (die ungültigen Eingaben), 24 ungedeckt
  (20 Weißraum, 4 führende Null).
- **Entscheidung 4 (eigene Tests):** der Kandidat mit Rückschritt und eigenem Test wird abgelehnt (an `0aac612`
  überlebte er).
- **Entscheidung 5:** Torzeile „Schwächen“ gebaut; am T3-Werk 0 von 5 nach doppelter Prüfung (Feststellung). Sie hat
  keinen Aufrufer (Review Nr. 7). TS-Methoden auf der Liste (vor T5).
- **Entscheidung 6:** `FEHLALARM-SICHERHEITSFILTER.md` im Ordner.
- **Regression:** `1d9a5aa` 562 bestanden / 2 übersprungen / 0 rot; `43b8fad` 569 / 2 / 0. Verdrahtung 23 von 23
  Organen, 0,00 €. Nachspiele am Commit `1d9a5aa`: 7 von 7 abgebrochen (eigener Fehler, §13 Nr. 1), im Nachtrag
  behoben.
- **Biotop-Modellgeld 0,00 €.**"""

# Befunde des Reviews: Tabelle aus REVIEW.md (Nr, Schwere, erster fetter Satz), Umgang je Nr.
UMGANG = {
    1: 'Runde 5, Entscheidung 2 (Festhalten = fallende Zusicherung)',
    2: 'Runde 5, Entscheidung 1 (Vollständigkeitsprüfung; Gegenprobe)',
    3: 'Runde 5, Entscheidung 1 (Gegenprobe)',
    4: 'Runde 5, Entscheidung 3 (Ausfall nur der betroffenen Funktion; nur echte Iteratoren ersetzen)',
    5: 'Runde 5, Entscheidung 1 (Gegenprobe)',
    6: 'Runde 5, Entscheidung 4 (zurückstellen mit Grund, gezählt; Messung in T4-Größe)',
    7: 'Runde 5, Entscheidung 5 (Register, Tor-4-Skript)',
    8: 'Runde 5, Entscheidung 6 (Vorspann verweigert ohne Stufe 2)',
    9: 'Runde 5, Entscheidung 7 (Formmerkmale der Lasteingabe)',
    10: 'Runde 5, Entscheidung 1 (`os.fspath`)',
    11: 'hier berichtigt: H3, H4, R4-5, R4-6, R4-13 sind Organ-Nachweise (`vv.pruefen`), nicht Laufweg; Laufweg sind H1, H2, E4',
    12: 'hier berichtigt: (a) die Sonde wurde geändert, gleich blieb nur ihre Last (Stufe 1); (b) Parität 19 von 19 '
        'Proben, 2 von 14 weiteren weichen ab (Runde 5); (c) Randwerte tragen Formmerkmale, wenn ihre Zeichen sie '
        'auslösen; (d) „quadratisch → linear“ ist gefolgert; (e) Median gepoolt 6,2 → 9,8 s',
    13: 'Runde 5, Entscheidung 6 (Stufe-2-Lasten bemessen)',
    14: 'Runde 5, Entscheidung 8',
    15: 'Runde 5, Entscheidung 8',
    16: 'Runde 5, Entscheidung 8',
    17: 'Liste (nicht entschieden; SPEZIFIKATIONEN R5-14)',
    18: 'Runde 5, Entscheidung 8',
}
zeilen = []
for z in review.splitlines():
    m = re.match(r'^\| (\d+) \| (hoch|mittel|niedrig) \| \*\*(.+?)\*\*', z)
    if m:
        nr = int(m.group(1))
        zeilen.append(f'| {nr} | {m.group(2)} | {m.group(3)} | {UMGANG[nr]} |')
assert len(zeilen) == 18, len(zeilen)
REVIEW = ('Ein Reviewdurchgang (`REVIEW.md`; Proben unter `review-proben/`, 24 Kammerfälle und 2 Probenläufe gegen '
          '`43b8fad`). 18 Befunde: 2 hoch, 8 mittel, 8 niedrig. Nach der Regel „ein Review, keine Fix-Kaskade“ wurde '
          'danach kein Code gebaut; die Befunde sind als Spezifikationen R5-1 … R5-14 gefasst '
          '(`SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`). Philipp hat sie am 24.09. entschieden (Runde 5). Dieser '
          'Abschnitt, §11 und §14 sind in der Sitzung der Runde 5 nachgetragen.\n\n'
          '| Nr | Schwere | Befund | Umgang |\n|---|---|---|---|\n' + '\n'.join(zeilen))

teil = review.split('## Sperren', 1)[1].split('## Schreibort-Nachweis', 1)[0].strip()
SPERREN = ('**1. Formatsperre (Auftragnehmer, 14:05)** — Beleg `sperre/FORMATSPERRE-1.txt` (wörtlich aus der Datei):\n\n'
           + '\n'.join('> ' + z if z.strip() else '>' for z in sperre1.strip().splitlines())
           + '\n\n**2. Freigabeabfrage im Reviewdurchgang** — aus `REVIEW.md`, Abschnitt „Sperren“ (wörtlich):\n\n' + teil)

OFFEN = """1. **Die Befunde des Reviews 04:** am 24.09. entschieden (Runde 5, Entscheidungen 1–8).
2. **`eingang` an Stufe 2 gesperrt in 3 von 6 Nachspielen:** entschieden (Runde 5, Entscheidung 6: die Stufe-2-Lasten
   werden wie Stufe 1 bemessen und geeicht, bis `eingang` nicht mehr sperrt).
3. **Normalvergleich je Schwäche:** entschieden (Runde 5, Entscheidung 5: für T4 gilt das Verhalten der Vorgeneration
   über den Verhaltensvergleich; eine verhaltensändernde Altlast braucht einen unabhängigen Test aus der
   Altlastenliste).
4. **K2868, führende Null (`~form#7`, 4 ungedeckte Abweichungen):** Die Werte stehen nicht im Beleg. Runde 5 schreibt
   sie ins Nachspiel. Danach ist zu klären, ob `007` eine gültige Zahl ist (die Normalversion nimmt sie an). Wenn ja,
   ist das ein weiterer Rückschritt von K2868."""

for platz, wert in (('‹URTEIL›', URTEIL), ('‹ERGEBNIS›', ERGEBNIS), ('‹REVIEW›', REVIEW), ('‹SPERREN›', SPERREN),
                    ('‹OFFEN›', OFFEN)):
    assert b.count(platz) == 1, platz
    b = b.replace(platz, wert)
assert '‹' not in b
(A / 'BERICHT.md').write_text(b)
print('BERICHT gefüllt:', len(b), 'Zeichen; Review-Zeilen', len(zeilen))
