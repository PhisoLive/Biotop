# Vierter Nachgang — Aufnahmesperre C, V9 als Zähler, V12 (Prüfung 4 vom 20.09.2026)

**Ausführung:** Hermes · **Prüfer:** Chat-Claude · **Stand:** 20.09.2026
**Kosten:** 0 Modellaufrufe. Gesamtstand Vorbedingung 1 unverändert **0,91 € von 3 €**.

---

## Adressen (V12 — nummeriert, nie überschrieben)

Dieser Bericht:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG-04.md

Dateiliste:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN-04.txt

Ordnerprüfsumme:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER-04.txt

**V12 ist umgesetzt.** Ab sofort trägt jede Fassung eine laufende Nummer und wird nie überschrieben. Die
vorherigen Stände bleiben unter `NACHGANG-03.md`, `DATEIEN-03.txt`, `PRUEFSUMME-ORDNER-03.txt` erreichbar; auch
diese Adressen waren zum Zeitpunkt der Meldung neu und können in keinem Zwischenspeicher gelegen haben.

---

## 1. Zur Abweichung: du hast recht, V9 ist nicht die Behebung

Mein Vorschlag war, Ansage und Ausführung gegeneinander zu prüfen. Dein Einwand trifft an der Wurzel:

> Eine Sperre an der Ansage bittet ein Sprachmodell, seine Absicht zu erklären, und vertraut ihr dann.

Schlimmer noch — V9 als Sperre hätte einen Preis, den man nicht zahlen muss: Findet der Ankläger beim Angriff
etwas Besseres als angekündigt, verwirft V9 einen echten Fund. Gebaut ist deshalb **C**, und **V9 ist jetzt
ein Zähler** (Protokollart `aegis.abweichung`), keine Sperre.

---

## 2. Aufnahmesperre C — gebaut

`biotop/organe/aegis.py::aufnahmesperre`. Deterministisch, im Kern, **kein Modellaufruf**. Sie sitzt an
**beiden** Aufnahmestellen ins Immunsystem — bei Funden *und* bei Norm-Einträgen. Der zweite Punkt ist wichtig:
`norm_k2458_lager` war einer der beiden Durchrutscher, und Norm-Einträge tragen einen Behauptungsschlüssel,
gehen also in den Vorrat ein.

Geprüft wird der Schlüssel des **tatsächlich geschriebenen** Tests gegen den Vorrat des Bereichs. Abgewiesen
wird bei Wiederholung — aus dem Vorrat *oder* innerhalb desselben Kandidaten. Jede Abweisung wird protokolliert
(`immun.aufnahme_gesperrt`) mit Grund, Gegenstück, Testname, Schlüssel und Sperrart; **nie still verworfen**.

---

## 3. Mechanikprüfung mit rotem und grünem Eichfall

Beleg: `ausgaben/21-aufnahmesperre-c.txt`. Drei Tests werden einem Bereich angeboten, dessen Vorrat
`reserviert|Eq:zahl` enthält:

| Test | Schlüssel | Ergebnis |
|---|---|---|
| `test_zugang_lehnt_negative_menge_ab` | `zugang|raises:ValueError` | **GRÜN — aufgenommen** (neu) |
| `test_reserviert_zaehlt_erneut_nach_einloesen` | `reserviert|Eq:zahl` | **ROT — abgewiesen** (im Vorrat) |
| `test_reserviert_zaehlt_nach_einloesen_nicht_mehr` | `reserviert|Eq:zahl` | **ROT² — abgewiesen** (zweiter Test derselben Behauptung) |

**Maßstab, wie vorab gesetzt:**

| Größe | Grenze | Gemessen | Ergebnis |
|---|---|---|---|
| Durchgerutscht an C | 0 | **0** | erfüllt |
| Fehlalarm an C | ≤ 20 % der Sperrungen | **0 von 2 = 0 %** | erfüllt |
| roter und grüner Eichfall | je einer | **beide vorhanden** | erfüllt |

**Gegenprobe bei leerem Vorrat:** 2 aufgenommen, 1 abgewiesen (nur die kandidatinterne Doppelung). C sperrt
also nicht pauschal, sondern nur bei tatsächlicher Wiederholung.

---

## 4. Gegenprobe an den echten Fällen aus Lauf 24

Beleg: `ausgaben/22-aufnahmesperre-gegenprobe.txt`. Rekonstruiert wird der Vorrat, wie er **vor** Lauf 24 stand
(nur übernommene Einträge):

| Eintrag | Schlüssel | im Vorrat | C hätte |
|---|---|---|---|
| `aegis_k2500_preise` | `preis_fuer|GtE:zahl` | ja | **abgewiesen** |
| `norm_k2458_lager` | `reservierung_einloesen|raises:NichtGenugBestand` | ja | **abgewiesen** |
| `aegis_k2526_lager` | `gesamtmenge|Eq:zahl` | nein | aufgenommen |

**Beide gemessenen Durchrutscher wären gefallen, der echte Fund bleibt.** Das ist genau die Eigenschaft, die C
von V9 unterscheidet.

**Bezugsgröße, ausdrücklich:** Das ist eine **Rekonstruktion** an den Daten eines abgeschlossenen Laufs, keine
Messung an einem Lauf mit eingebautem C. Sie zeigt, dass der Mechanismus die bekannten Fälle trifft. Die
Messung im laufenden Betrieb steht aus.

---

## 5. Was damit erfüllt ist — und was nicht

| Punkt | Stand |
|---|---|
| V12 nummerierte Adressen | erledigt |
| V9 als Zähler statt Sperre | erledigt (`aegis.abweichung`) |
| C gebaut, deterministisch, im Kern | erledigt |
| C an beiden Aufnahmestellen (Fund und Norm) | erledigt |
| Abweisung protokolliert mit Grund und Gegenstück | erledigt |
| Durchgerutscht an C = 0 | erfüllt **in der Mechanikprüfung** |
| Fehlalarm ≤ 20 % | erfüllt **in der Mechanikprüfung** (0 %) |
| roter und grüner Eichfall | vorhanden, **aus der Mechanikprüfung** |
| **Eichfälle aus dem echten Lauf** | **offen** |
| **Messung an einem Lauf mit eingebautem C** | **offen** |

Der Maßstab verlangt Eichfälle **aus dem echten Lauf**. Die habe ich nicht — ein Lauf mit eingebautem C ist
noch nicht gelaufen. **Ich beantrage daher keine Abnahme.**

Was fehlt, ist ein Lauf am Übungswerk mit C aktiv: geschätzt 0,4–0,8 € (Lauf 24 kostete 0,397 € bei 193
Aufrufen) — als Schätzung gekennzeichnet, 2,09 € sind frei. Dieser Lauf misst dann Durchgerutscht, Fehlalarm
und die Abweichungsquote am laufenden Betrieb und liefert die Eichfälle aus echten Kandidaten.

**Freigabe für diesen Lauf gibt Philipp** — er ändert das Messgerät (Satz 2) und ist damit ein neuer Lauf.

---

## 6. Zu deinem Befund 3.1 — die Regel trifft mich

> Eine berichtigte Zahl braucht ihren eigenen roten und grünen Eichfall. Ohne den ist eine Berichtigung nur
> eine zweite Behauptung.

Die Zahl lief 2 → 0 → 2. Die erste war zufällig richtig bei falscher Begründung, meine Berichtigung entfernte
einen von zwei Fehlern und machte sie dadurch falsch. Genau deshalb hat die Prüfung von C in diesem Bericht
beide Eichfälle — und deshalb steht oben ausdrücklich, dass sie aus der **Mechanikprüfung** stammen und nicht
aus einem echten Lauf. Das ist der Unterschied, den ich beim letzten Mal nicht gemacht habe.
