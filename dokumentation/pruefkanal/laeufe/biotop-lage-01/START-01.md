# BIOTOP-LAGE-01 · Fassung 2 · START-01

| Feld | Wert |
|---|---|
| Kennung | BIOTOP-LAGE-01 |
| Fassung | 2. Auftragsdatei `BIOTOP-LAGE-01-Auftrag-v2.md`: 41.239 Bytes, SHA-256 `58ba8834b8c3ec08f8da2e18d3db056150c91c2841ed9aac349bcf2eba216b98`. Eingegangen am 25.09.2026 um 14:44:20 CEST (Beleg R4). |
| Fassung 1 | Auf HERMES-1 nie eingegangen, daher ist unter Fassung 1 nichts entstanden. Belege: R1 (im Dokumentenspeicher liegt nur Fassung 2) und R4 (in der Sitzungsdatenbank stammt die einzige Nachricht mit „BIOTOP-LAGE“ vom 25.09.2026 14:44:20 CEST). |
| Beginn dieses Auftrags | 25.09.2026 14:44:20 CEST (UTC+2) |
| Stichzeitpunkt | **Folgt nach Laufende**: Ende des Baus S1c (siehe „Laufender Lauf“) |
| Status | **IN ARBEIT** |
| Stand dieser Datei | 25.09.2026, etwa 15:05 CEST |

## Schritt 1: Ergebnis

- **Biotop gefunden unter `/root/biotop`** (git; R1).
  - HEAD ist `0c2f058d57f68b8891b535d6e00214172c82fefa` vom 24.09.2026 20:24:54 +0200, Autor „Hermes (Biotop)“, Nachricht „Vor T4, Runde 5: …“.
  - Nicht eingecheckt, Stand 14:57:44 CEST: 17 geänderte und 6 neue Dateien aus der Arbeit der Behebungsrunde 6 (R6). Das ist der Stand „Runde 6 in Arbeit“.
  - Weitere Kopien des Codes liegen unter `/root/biotop-t3/`, `/root/phase-4-vorbedingung-1/`, `/root/reparatur-01/` und in Testordnern. Es sind Sicherungen, Ausgangsstände und Testkopien früherer Aufträge, keine zweite Arbeitsinstanz (R1: 193 Fundstellen von `biotop/__main__.py`). Die Zuordnung folgt im Inventar I5.
- **Laufender Lauf:**
  - **Biotop-Lauf: nein.** Es läuft kein Prozess mit `biotop`, `pytest`, `kammer`, `vitest` oder `tsc`, 0 Container laufen, und die Kammer-Sperrdatei fehlt (R2).
  - **Anderer Biotop-Prozess: ja.** Seit 25.09.2026 12:51:42 CEST läuft der **Bau S1c der Behebungsrunde 6 vor T4**. Das ist ein Subagent von Hermes mit dem Bauauftrag `/root/biotop-vor-t4-06/BAU-S1C-UNBEOBACHTET.md`.
    - Er ändert Code und Tests in `/root/biotop` und legt lokale Tests in der Kammer an.
    - Laut Auftrag ruft er kein Modell auf und nutzt kein Netz.
    - Stand 14:57:44 CEST: 118 Werkzeugaufrufe, Spezifikation gebaut, der Bau der Teile A–D, E und F steht aus (R6).
  - **Erwartetes Ende: etwa 16:15 bis 17:45 CEST, spätestens gegen 18:25 CEST** (gerechnet).
    - Rechenweg: Bisher rund 96 Modellrunden in 126 min, also etwa 1,3 min je Runde (geschätzt nach dem Verhältnis beim Vorgänger S1b: 154 Runden auf 190 Werkzeugaufrufe).
    - Für den Rest sind 60 bis 120 Runden geschätzt. Die Obergrenze liegt bei 250 Runden (R6, `delegation.max_iterations: 250`).
- **Auslegung Hermes (Abschnitt 3):** S1c ist kein Lauf im Sinne der Kasse, aber „ein anderer Biotop-Prozess“, der `/root/biotop` ändert.
  - Ich behandle ihn wie einen laufenden Lauf: Er wird nicht angehalten, und sein Ende ist der Stichzeitpunkt.
  - Bis dahin bearbeite ich nur, was er nicht berührt: Verlauf, Masterprompt, Verfassungen, Entscheidungen, Glossar und Aufbau, alles lesend.
  - Prüfsummenliste VORHER, Sicherung und Inventare beginnen nach seinem Ende.
- **Entscheidung Hermes:** Nach dem Ende von S1c ruht die Behebungsrunde 6 bis zum Abschluss dieses Auftrags: kein Commit, kein weiterer Bau (Regel 2.1; Abschnitt 0: „baut nichts, repariert nichts“).
- **Zeitgeber und Cron-Jobs** (R2, R4):
  - **Hermes-Zeitgeber `26fbb1513a1a`** („zwischenbericht-waechter“) läuft jede Minute, ohne Modellaufruf.
    - Bei ≥ 80 % Kontext, bei einer Verdichtung oder bei 110 bzw. 140 Runden legt er einen Zwischenbericht unter `laeufe/biotop-vor-t4-06/` an; bisher 4 (R4).
    - Er wird nicht angehalten (Vorentscheidung 1: nichts anhalten; Regel 2.2: nichts überschreiben). Entsteht während dieses Auftrags ein neuer Zwischenbericht, wird er im Inventar I3 gezählt.
  - **Hermes-Zeitgeber `5825fd644daa`** (Endmeldung Runde 5): einmalig, erledigt am 24.09.2026 23:54:23 CEST.
  - **systemd:** 29 Zeitgeber, keiner gehört zum Biotop. Sie gehören zu Website, Server und System (R4). Eine root-crontab gibt es nicht.
- **Abrufstelle unverändert:** `/var/pruefkanal/oeffentlich/_akte/<kennung>/laeufe/`, ausgeliefert von Caddy (R3). Dort liegen 18 Ordner mit `biotop-` im Namen und `gedaechtnis/`. Die Zählung und Zuordnung folgt in I3.
- **OpenRouter-Nutzungsanzeige** um 14:54:17 CEST, abgelesen (R5): 20,536052277 USD verbraucht über die Lebenszeit des Schlüssels, davon heute 0,30761925 USD.
  - Das ist der Ausgangswert für die Kosten dieses Auftrags. Dazu gehören auch die Verdichtungen dieser Sitzung über denselben Schlüssel, die Philipp am 25.09. so festgelegt hat. Sie werden getrennt ausgewiesen.

## Plan in fünf Zeilen
1. Schritt 1 ist erledigt: Biotop gefunden, Prozesslage geprüft (R1–R6), Ordner und START-01 angelegt, Meldung 1 folgt.
2. Bis zum Ende von S1c, nur lesend: Masterprompt, Verfassungen, Entscheidungen, Verlauf, Aufbau und Glossar im Wortlaut (FK11, FK14–FK22, FK31–FK38, FK50).
3. Nach dem Ende von S1c (Stichzeitpunkt):
   - Prüfsummenliste VORHER, dann Sicherung nach Abschnitt 4 in `/root/sicherung/biotop-lage-01/`;
   - Datenbanken per `.backup` mit `integrity_check`;
   - Archiv, Wiederherstellungsprobe mit Gegenprobe, Wiederherstellungsanleitung.
4. Inventare I1–I8 mit Abgleich, Tagesbilanz vom 18.09. bis zum Stichzeitpunkt, Gegenprobe; Abgleich Kasse gegen OpenRouter.
5. Abschluss:
   - Fragenkatalog FK01–FK50 und WS01–WS19 in die Dateien nach Abschnitt 8, Vollständigkeitsprüfung mit Lückenliste;
   - Prüfsummenliste NACHHER, Geheimnissuche mit Gegenprobe, Gedächtnis `STAND-02.md`;
   - Abrufprobe, Meldung 2.

## Dateien dieses Standes
- Ordner: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/
- Diese Datei: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/START-01.md
- Rohbelege R1 bis R6 (Befehl wörtlich, vollständige Ausgabe):
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ROHBELEGE-TEIL1-01.txt
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ROHBELEGE-TEIL2-01.txt
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ROHBELEGE-TEIL3-01.txt
- Größen und SHA-256 folgen mit der nächsten Einstiegsdatei in `DATEIEN-NN.txt` und `PRUEFSUMME-ORDNER-NN.txt`. Diese Datei kann ihre eigene Prüfsumme nicht enthalten; sie steht in Meldung 1.

## Gedächtnis (neueste Dateien in `laeufe/gedaechtnis/`, Stand 20.09.2026 05:17:33 CEST, R4)
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/STAND-01.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/REGELN-01.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/UNTERBAU-01.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/DATEIEN-01.txt
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/PRUEFSUMME-ORDNER-01.txt

## Lesereihenfolge
Noch nichts zu lesen außer dieser Datei und den Rohbelegen. Die abschließende Einstiegsdatei nennt die Reihenfolge.
