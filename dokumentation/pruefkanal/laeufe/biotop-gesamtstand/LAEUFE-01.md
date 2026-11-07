# Läufe 1 bis 23 — vollständige Tabelle und Kostenabgleich

Status und Werkname sind der heutige DB-Eintrag, nicht eine nachträgliche Glättung des Berichtsstatus. `bereit` heißt nicht „läuft als Prozess“; `NULL` bedeutet nicht erfasst. Die Bestandsaufnahme hat keinen Lauf angelegt.

Historisch = rekonstruierter damaliger Berichtsschnitt (je Lauf die ursprünglich genannte Zahl frühester Buchungen nach ID). Für Phase 2 sind 1190 von 1190 Original-IDs abgeglichen; für die späteren Übersichts-Kassenblätter ist dies eine Rekonstruktion, keine historische DB-Sicherung. Sämtliche fünf Abschnittskosten stimmen damit auf vier Nachkommastellen. Heute = alle aktuell auf derselben Lauf-ID gebuchten Beträge.

| Lauf | Werk (DB) | Status (DB) | Buchungen historisch / heute | historisch € | heute € | später € |
|---:|---|---|---:|---:|---:|---:|
| 1 | lagerhaus | abgebrochen | 27 / 27 | 0,024193 | 0,024193 | 0,000000 |
| 2 | lagerhaus | bereit | 100 / 100 | 0,216594 | 0,216594 | 0,000000 |
| 3 | NULL — kein Werk zugeordnet | gestoppt | 1 / 1 | 0,000187 | 0,000187 | 0,000000 |
| 4 | lagerhaus-kasse | abgebrochen | 62 / 62 | 0,094108 | 0,094108 | 0,000000 |
| 5 | lagerhaus-kasse2 | abgebrochen | 46 / 46 | 0,067978 | 0,067978 | 0,000000 |
| 6 | lagerhaus-nachlauf | abgebrochen | 178 / 178 | 0,746327 | 0,746327 | 0,000000 |
| 7 | lagerhaus-nachlauf2 | abgebrochen | 88 / 88 | 0,217395 | 0,217395 | 0,000000 |
| 8 | lagerhaus-nachlauf8 | abgebrochen | 136 / 136 | 0,408594 | 0,408594 | 0,000000 |
| 9 | lagerhaus-nachlauf9 | beendet | 108 / 108 | 0,323255 | 0,323255 | 0,000000 |
| 10 | lagerhaus-kasse3 | abgebrochen | 32 / 32 | 0,094767 | 0,094767 | 0,000000 |
| 11 | NULL — kein Werk zugeordnet | angelegt | 6 / 6 | 0,001257 | 0,001257 | 0,000000 |
| 12 | lagerhaus-p2 | abgebrochen | 480 / 480 | 0,758462 | 0,758462 | 0,000000 |
| 13 | lagerhaus-p2-13 | beendet | 704 / 713 | 1,145284 | 1,146760 | 0,001476 |
| 14 | lagerhaus-p3-14 | verworfen | 17 / 17 | 0,003546 | 0,003546 | 0,000000 |
| 15 | lagerhaus-p3-15 | verworfen | 28 / 28 | 0,011853 | 0,011853 | 0,000000 |
| 16 | lagerhaus-p3-16 | verworfen | 263 / 264 | 0,596283 | 0,596412 | 0,000128 |
| 17 | logmuehle-17 | gesaettigt | 310 / 315 | 0,994877 | 0,995827 | 0,000950 |
| 18 | lagerhaus-p3-18 | verworfen | 154 / 156 | 0,339812 | 0,340069 | 0,000258 |
| 19 | lagerhaus-p3-19 | verworfen | 220 / 221 | 0,457494 | 0,457615 | 0,000121 |
| 20 | lagerhaus-p3-20 | gesaettigt | 233 / 244 | 0,423058 | 0,437074 | 0,014016 |
| 21 | lagerhaus-p3-20 | verworfen | 0 / 0 | 0,000000 | 0,000000 | 0,000000 |
| 22 | lagerhaus-p3-22 | gesaettigt | 189 / 233 | 0,397763 | 0,516608 | 0,118845 |
| 23 | logmuehle-23 | gesaettigt | 18 / 239 | 0,038938 | 0,393614 | 0,354676 |
| **Summe 23 von 23** | | | **3400 / 3694** | **7,362027** | **7,852498** | **0,490471** |
Rundungsabgleich historisch: Summe der sichtbaren Einzelzeilen 7,362025 €; ungerundet 7,362027175926 €; sichtbare Summe minus ungerundete Summe -0,000002175926 €.
Rundungsabgleich heute: Summe der sichtbaren Einzelzeilen 7,852495 €; ungerundet 7,852498092593 €; sichtbare Summe minus ungerundete Summe -0,000003092593 €.
Rundungsabgleich später: Summe der sichtbaren Einzelzeilen 0,490470 €; ungerundet 0,490470916667 €; sichtbare Summe minus ungerundete Summe -0,000000916667 €.

## Deine Rechnung 7,37 €

**Als Summe der fünf auf Cent gerundeten Abschnittsbeträge stimmt sie:** `0,40 + 1,79 + 1,91 + 2,83 + 0,44 = 7,37 €`. Aus den zugehörigen 3400 Rohbuchungen ergeben sich dagegen **7,362027175926 €**, auf Cent insgesamt gerundet 7,36 €. Unterschied zu 7,37 €: -0,007972824074 € (Rundung der Abschnitte vor Addition).

**Der heutige Bestand derselben Lauf-IDs ist eine andere Menge:** 3694 statt 3400 Buchungen, **7,852498092593 €**. Später auf alte Lauf-IDs gebucht: **294 Buchungen / 0,490470916667 €**. Differenz heute zu deiner Summe: **+0,482498092593 €**. Dies vollständig als Rundung abzutun wäre falsch.

| Abschnitt | historische Buchungen | historisch roh € | heute roh € | spätere Buchungen | später roh € |
|---|---:|---:|---:|---:|---:|
| Phase 1 | 236 | 0,403061481 | 0,403061481 | 0 | 0,000000000 |
| Nachlauf Phase 1 | 542 | 1,790337963 | 1,790337963 | 0 | 0,000000000 |
| Phase 2 | 1190 | 1,905003111 | 1,906479593 | 9 | 0,001476481 |
| Phase 3 | 1225 | 2,826923037 | 2,842396463 | 20 | 0,015473426 |
| Nachlauf Phase 3 | 207 | 0,436701583 | 0,910222593 | 265 | 0,473521009 |

Die späteren Mengen sind nach IDs vollständig in `13-spaetere-buchungen.json` aufgeführt. Gründe: Nachabstraktion auf alten Lauf-IDs (u. a. Lauf 13), nachträgliche Prüf-/Anklägeraufrufe auf Lauf 20, Fortsetzungen der Läufe 22 und 23 unter Vorbedingung 1. Die Tabelle stellt keine neue Abschnittszuordnung nach V20 auf und ändert kein bestehendes Budgetkonto.

## Abbrüche, offene Status und nicht gebuchte Anfragen

- Lauf 3: Aufnahme ohne Tests gestoppt, kein Werk in der Laufzeile. Lauf 11: Modell-Rauchtest, kein Werk und keine Generation. Lauf 21: gestellter Abbruch-/Verwerfungsfall, keine Kassenbuchung; nicht als Hebungslauf ausgeben.
- Lauf 2 bleibt in der Datenbank `bereit`, trotz abgeliefertem historischem Abschluss. Lauf 4 ist `abgebrochen`, hat aber einen Generationseintrag `laeuft` und kein `beendet_am`. Diese Inkonsistenzen sind nicht bereinigt worden, weil der Auftrag eine Bestandsaufnahme ist.
- Die vollständigen Abbruchgründe je Lauf stehen in `07-laeufe.json`; auch verworfene und erfolglose Läufe zählen kostenmäßig voll.
- Gesamte DB, **25** Lauf-IDs: 4080 protokollierte Modellanfragen = 4070 Buchungen + 8 protokollierte Fehler + 2 Anfragen ohne Antwort-/Fehlerabschluss. Letztere: Protokoll #1719 (Lauf 7), #7868 (Lauf 17). Ihre tatsächlichen Kosten sind aus dieser DB nicht bekannt; nicht still als kostenlos gebucht. „Buchungen“ in der Tabelle meint deshalb nicht sämtliche versuchten Netzwerkaufrufe.
- Die Kosten sind aus usage-Token und hinterlegten Preisen berechnet, keine geprüfte Anbieterrechnung. Die vielen Nachkommastellen dienen nur der nachvollziehbaren Summierung gespeicherter Werte, nicht einer Behauptung entsprechend genauer Abrechnung.

## Außerhalb der verlangten 23 Läufe (nicht in deren Summe)

- Lauf 24: `lagerhaus-zeile8-24`, Status `bereit`, 193 Buchungen, 0,396878000 €.
- Lauf 25: `lagerhaus-c-25`, Status `bereit`, 183 Buchungen, 0,389928676 €.

Gesamter heute gespeicherter Kassenbestand: **4070 Buchungen / 8,639304768519 €**. Keine der Buchungen gehört zur jetzigen lesenden Bestandsaufnahme.

Quellen: `06-kassenbuchungen.json`, `07-laeufe.json`, `12-kassenabgleich.json`, `13-spaetere-buchungen.json`, `19-belegpruefung.json`; Rechenskript `quellen/vertiefen.py`. Eichkosten sind im eigenen DB-Register zusätzlich dokumentiert, dürfen aber nicht pauschal ein zweites Mal addiert werden: ihre Modellantworten liegen auch in `kasse`. Ob sie in einem historischen Bericht tatsächlich herausgerechnet wurden, ist eine getrennte Abgrenzungsprüfung.
