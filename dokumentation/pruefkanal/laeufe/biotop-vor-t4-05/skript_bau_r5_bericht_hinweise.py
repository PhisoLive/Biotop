"""Hinweise Philipp (24.09., während der Kette) in den Bericht der Runde 5 einarbeiten — nur Text, kein Code.
(1) Enthaltung des ganzen Vergleichs widerspricht Entscheidung 3 → Umgang in §1, §13 Nr. 1, rote Spezifikation R6-1.
(2) Stichprobendauer eingang Stufe 2 → §6 (Tabelle aus proben/STUFE2-EINGANG-DAUER.txt), Auftragsfehler benannt.
(3) Tor-4-Skript berechnet jede aus der DB berechenbare Zeile → §5, R6-2 (Liste vor T4)."""
from pathlib import Path

A = Path('/root/biotop-vor-t4-05')
p = A / 'BERICHT.md'
b = p.read_text()
dauer = (A / 'proben' / 'STUFE2-EINGANG-DAUER.txt').read_text()
for s in ('eingang W60_ist : Einzelwerte Median 35.1 ms', 'eingang W240    : Einzelwerte Median 170.5 ms',
          'eingang W480    : Einzelwerte Median 317.1 ms', 'Stufe 1, Lauf 37, eingang : Median 2.86 ms',
          'Stufe 1, Lauf 38, eingang : Median 2.41 ms', 'bericht  (Stufe 2, unverändert): Einzelwerte Median 100.5 ms',
          'zahlen   (Stufe 2, unverändert): Einzelwerte Median 18.9 ms', 'relative Spannweite je Messung 0.53 … 0.92',
          'relative Spannweite je Messung 0.05 … 0.21'):
    assert s in dauer, f'Beleg fehlt: {s}'

ERS = []
ERS.append(('''- **Fehlalarm-Risiko:** Die Enthaltung gilt für das ganze Urteil. Eine unvollständig erfasste Funktion eines geänderten
  Moduls stellt den Kandidaten auch dann zurück, wenn er sie nicht geändert hat (Offen Nr. 1).
''', '''- **Befund gegen den eigenen Bau (Philipp, 24.09.):** Die Enthaltung gilt hier für das ganze Urteil. Das widerspricht
  Entscheidung 3 und schafft denselben Totalausfall wie Review 04 Nr. 4: Ein einziges schwer erfassbares Objekt in einem
  geänderten Modul — etwa eine unveränderte Funktion, die ein Datei-Objekt liefert — stellt jeden Kandidaten zurück, der
  dieses Modul berührt, auch wenn er die Funktion nicht geändert hat.
  - Enthalten muss sich nur die betroffene Beobachtung; der übrige Vergleich urteilt.
  - Nach „ein Review, keine Fix-Kaskade“ ist das nicht mehr in diese Runde gebaut, sondern als **rote Spezifikation vor
    T4** gefasst (R6-1, `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`).
  - Belegt an `0c2f058` (`spez/SPEZ-R6-UNIT.txt`): Am Organ mit gestellter Sonde enthält sich der ganze Vergleich
    (`unvollstaendig_erfasst`), obwohl nur die unveränderte Funktion `g` schwer erfassbar ist und keine Beobachtung
    abweicht. Die zwei Gegenproben sind grün: ohne schwer erfassbares Objekt geurteilt; eine echte ungedeckte Abweichung
    lehnt weiter ab.
  - Laufweg-Fassung durch `aegis.pruefen` (`spez/test_spez_r6_laufweg.py`, echte Kammer): ‹R6_LAUFWEG›
'''))
ERS.append(('''Gewählt ist 240, die kleinste gemessene Variante ohne Sperre. Die übrigen Bereiche sperrten in 0 von 24 Messungen.
Ob `eingang` an `0c2f058` in den Nachspielen noch sperrt, zeigt §9.
''', '''**Auftragsfehler, benannt (Philipp, 24.09.):** „bemessen, bis `eingang` nicht mehr sperrt“ richtet die Last nach dem
Ergebnis. Ob 240 nach Maß gewählt ist, zeigt nur die Dauer der Stichprobe. Also die Stichprobendauer je Variante: ein
Wert ist der Median aus fünf Durchläufen der `eingang`-Last in einem Kammerlauf, je Rauschmessung fünf Werte, je
Variante 8 Rauschmessungen, also 40 Werte (`proben/STUFE2-EINGANG-DAUER.txt`, aus `STUFE2-EICHUNG.jsonl`):

| `eingang`-Wiederholungen | Stichprobendauer: Median (Spanne), n = 40 | relative Spannweite je Rauschmessung | Sperren |
|---|---|---|---|
| 60 (Stand Runde 4) | 35,1 ms (29,3 … 71,2 ms) | 0,53 … 0,92 | 3 von 8 |
| **240** (gewählt) | **170,5 ms** (141,3 … 189,1 ms) | 0,05 … 0,21 | 0 von 8 |
| 480 | 317,1 ms (299,1 … 364,5 ms) | 0,03 … 0,19 | 0 von 8 |

Zum Vergleich, ebenfalls Stufe 2 und unverändert:
- `zahlen` 18,9 ms (Spannweite 0,05 … 0,39, 0 Sperren in 24 Messungen);
- `tarife` 96,0 ms (0,06 … 1,42 — ein Ausreißer, 0 Sperren);
- `bericht` 100,5 ms;
- `planung` 346,0 ms.

Stufe 1 (Rauschmessung der Läufe 37/38, `t3.db` nur gelesen): `eingang` 2,41 bzw. 2,86 ms, die übrigen Bereiche 2,9 bis
12,1 ms.

**Einordnung, gerechnet, nicht als Regel gemessen:**
- Mit 60 Wiederholungen war die `eingang`-Stichprobe an Stufe 2 mit 35 ms die kürzeste neben `zahlen` und streute am
  stärksten.
- 240 Wiederholungen heben sie auf 170 ms, in dieselbe Größenordnung wie `bericht` und `tarife`.
- Die Last steigt also mit ihrer Dauer, und die Spannweite fällt mit ihr, von 0,53 … 0,92 auf 0,05 … 0,21.
- Ein Maß „nach Dauer“ gibt es im Kern aber nicht. Stufe 1 wählte die Wiederholungen „gemessen“ bis „einige zehn
  Millisekunden“ (Kopf der Stufe-1-Last); an dieser Formulierung gemessen hätten auch 60 Wiederholungen (35 ms) gereicht.
- `zahlen` sperrt mit 18,9 ms nicht; die Dauer allein erklärt die Sperren also nicht.
- Ob 240 nach Maß gewählt ist, bleibt deshalb eine Entscheidung (Offen Nr. 5). Die gemessene Stichprobendauer steht
  hiermit neben der Sperrzahl.

Ob `eingang` an `0c2f058` in den Nachspielen noch sperrt, zeigt §9.
'''))
ERS.append(('''- Die übrigen Zeilen von Tor 4 berechnet das Skript nicht; es nennt sie als „nicht berechnet“ und nie als erfüllt
  (Offen Nr. 2).
''', '''- Die übrigen Zeilen von Tor 4 berechnet das Skript nicht; es nennt sie als „nicht berechnet“ und nie als erfüllt.
- **Auf der Liste vor T4 (Philipp, 24.09.):** Das Tor-4-Skript berechnet jede Zeile, die aus der Datenbank berechenbar
  ist; die meisten Berichtsfehler in T3 waren Torzeilen von Hand. Gefasst als rote Spezifikation R6-2
  (`spez/test_spez_r6_unit.py`, rot an `0c2f058`). Aus der Datenbank berechenbar sind 10 von 14 Zeilen:
  - Generation minus eins, Generation 0, Kein Rückschritt, Halluzinationsprobe;
  - Verhaltensvergleich, Doppelungsanteil, Immunisierung, Neutralzähler;
  - Verbundausfall, Sättigung oder Budgetabbruch.
  Nicht aus der Datenbank berechenbar sind Aufnahme (Werk und Altlastenliste prüfen), Verdrahtung (Regression),
  Reviewdurchgang und Zwischenbericht.
'''))
ERS.append(('''1. **Enthaltung des ganzen Urteils bei unvollständiger Erfassung**, nur wenn das Urteil sonst tragfähig wäre.
   - Grund: Entscheidung 1 verbietet „0 Abweichungen, tragfähig“, solange ein Datenattribut fehlt.
   - Eine Ablehnung wegen einer ungedeckten Abweichung bleibt eine Ablehnung.
   - Beide Seiten zählen.
   - Folge für T4: Offen Nr. 1.
''', '''1. **Enthaltung des ganzen Urteils bei unvollständiger Erfassung**, nur wenn das Urteil sonst tragfähig wäre (Eine
   Ablehnung wegen einer ungedeckten Abweichung bleibt eine Ablehnung.). **Diese Entscheidung war falsch** (Philipp,
   24.09.):
   - Sie widerspricht Entscheidung 3 und schafft denselben Totalausfall wie Review 04 Nr. 4.
   - Richtig ist: Nur die betroffene Beobachtung enthält sich.
   - Als rote Spezifikation R6-1 vor T4 gefasst, am Organ belegt (§1), nicht mehr in dieser Runde gebaut (ein Review,
     keine Fix-Kaskade).
'''))
ERS.append(('''6. **`proben/t4_groesse.py` hätte in der ersten Fassung nicht gebaut** (Bereich `werk` fehlte als Unterpaket). Korrigiert
   vor seinem Lauf in der Kette (`bau/r5_t4_fix.py`).
''', '''6. **`proben/t4_groesse.py` hätte in der ersten Fassung nicht gebaut** (Bereich `werk` fehlte als Unterpaket). Korrigiert
   vor seinem Lauf in der Kette (`bau/r5_t4_fix.py`).
7. **Die Enthaltung des ganzen Vergleichs (§13 Nr. 1) war ein Entwurfsfehler.** Ich hatte das Risiko in §1 als „Offen“
   notiert, statt es gegen Entscheidung 3 zu prüfen. Es ist dieselbe Figur, die Review 04 Nr. 4 als Befund führte:
   ein Einzelfall legt den ganzen Vergleich still.
8. **Die Stufe-2-Last habe ich nach der Sperrzahl gewählt, nicht nach der Stichprobendauer.** Die Dauer stand in
   `STUFE2-EICHUNG.jsonl`, ich habe sie aber erst auf Nachfrage ausgewertet (§6).
'''))
for alt, neu in ERS:
    assert b.count(alt) == 1, alt[:80]
for alt, neu in ERS:
    b = b.replace(alt, neu)
p.write_text(b)
print('BERICHT: 5 Stellen ergänzt; Platzhalter:', sorted({x.split('›')[0] for x in b.split('‹')[1:]}))
