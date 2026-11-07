# Zwischenbericht / Abschluss W1–W2–W4 — Fassung 01
Stand: 2026-09-20T03:17:33.347176+00:00 · Ausführung: Hermes, Schreibrolle HERMES-1 laut Auftrag.

## Wichtigster Befund und Abbruch
**Trägernachweis fehlgeschlagen, W4 nicht vollständig erfüllt.** Die CLI-Voreinstellung nennt `claude-fable-5.1`, Anbieter `anthropic`; die reale HTTP-Anfrage zielte auf `claude-fable-5-1`. Die API lieferte HTTP 429 statt einer Modellantwort. Ein weiterer POST-Versuch wurde vor dem Netz gesperrt. Nach 240 Sekunden brach der Wrapper mit Timeout ab. Kein zweiter Modelltest; keine Änderung von Modell, Anbieter, Authentifizierung oder Gateway.

**Unterschied der Betriebswege:** Datenbankzeile `20260920_045023_5299d50d` führt die Telegram-Sitzung als `gpt-6-astra`; der CLI-Test ist die getrennte Sitzung `20260920_050847_fa0691`. Ein neuer CLI-Aufruf belegt nicht rückwirkend das Modell einer bereits laufenden Telegram-Sitzung. Es gibt keinen zurückgemeldeten erfolgreichen Träger, den man als identisch oder abweichend freigeben könnte. Die Modellkennung der Telegram-Sitzung ist Sitzungsmetadatum, kein durch diesen Test gewonnenes API-Ergebnis.

## W1 — erledigt
Fassung 6 unverändert veröffentlicht. Quelle: `doc_8d640daa6c3c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md`. SHA-256: `effefeec0fe2ea0621d4fdca0f27bdd3dae981fd289f1e0b5d56da5aca81aefd`. HTTP-Abruf wurde byteweise mit der Originaldatei verglichen; Ausgabe in `belege/ABRUF-VOR-VERSIEGELUNG-01.json`. Kein v7-Text erfunden oder v6-Inhalt verändert.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6-01.md

## W2 — Vorabrechnung gefunden; Ursache berichtigt
Das alte Phase-3-Nachlauf-Kassenblatt enthält 189 Aufrufe für Lauf 22 zu 0,3978 €. Diese Zahl war in meiner ersten Meldung **gelesen**, nicht frisch gemessen. Die beigefügte Datenbankabfrage bestätigt sie nun: 189 von 233 Kassenzeilen des Laufs 22 ergeben 0.39776329629629626276 €. Etappengrenze: Kassen-ID 3411 (Mentor, Zeitfenster im Nachlauf); Fortsetzung beginnt bei ID 3651. Grenzzeilen und alle Einzelbuchungen der betrachteten Läufe sind beigelegt.

**Die Erklärung „nur Rundung“ ist nicht belegt und passt nicht zu den Rohdaten.** Die 44 von 233 Fortsetzungszeilen ergeben 0,11884500925925925 €, auf vier Stellen 0,1188 €, nicht die früher gemeldeten 0,1190 €. Zwei korrekt auf vier Nachkommastellen gerundete Eingangswerte erklären eine Differenz von 0,0002 € nicht: ihre gemeinsame maximale Rundungsunsicherheit beträgt 0,0001 €. Die angebotene Gegenprobe beginnt außerdem bei 0,51665, das kaufmännisch auf 0,5167 rundet, nicht auf 0,5166. Ursache der alten 0,1190 bleibt ungeklärt; wegen des kleinen W2-Auftrags keine weitere historische Rekonstruktion.

V20 bleibt als **Entscheidung des Auftraggebers** dokumentiert: rund 1,299 € von 3 €, frei rund 1,701 €. Aus den Rohbuchungen ergibt die gesetzte Abgrenzung (nur erste Etappe Lauf 22 abziehen): 659 von 848 betrachteten Kassenzeilen, 1.29926597222222211151 €, frei 1.70073402777777788849 €. Diese langen Dezimalwerte sind Rechenbelege aus gespeicherten REAL-Werten, keine behauptete Genauigkeit der Rechnung des Anbieters. Auf vier Nachkommastellen wären es 1,2993 € und 1,7007 €, nicht 1,2992 € und 1,7008 €. Der geführte Stand auf drei Stellen ist unverändert.

**Weitere Abgrenzung offen:** Das alte Kassenblatt enthält auch 18 Aufrufe von Lauf 23 zu 0,0389 €. V20 zieht nur die erste Etappe von Lauf 22 ab; die Zugehörigkeit dieser Lauf-23-Zeilen wurde hier nicht neu geschnitten. Deshalb ist 1,299 € der V20-Stand, kein Nachweis einer vollständig doppelzählungsfreien auftragsübergreifenden Buchhaltung.

## W4 — Dateien geliefert, Ausführungsnachweis offen
`STAND-01.md`, `REGELN-01.md`, `UNTERBAU-01.md` liegen im festen Gedächtnisordner. W3 ist zurückgezogen; es wurde kein Obsidian-Tresor angelegt. V17–V20 und die nachgereichten Regeln 25/26 sind dort mit Herkunft vermerkt. Nur die vom Auftrag verlangte Schreibrolle HERMES-1 wurde benutzt; andere Profile wurden nicht verändert.

HTTP-Fehler, leere stdout/stderr-Dateien, fehlende Verbrauchsdatei, Timeout und Datenbank-Kostenfelder sind offengelegt. „Am Erzeugnis belegt“ gilt allein für den zurückgegebenen Fehler; **nicht** für einen erfolgreichen Modellnamen.

## Kasse
Keine neuen Biotop-Aufrufe: Der Vorher-/Nachher-Abgleich umfasst denselben Bestand von 4070 Kassenzeilen, höchste ID 4070, Summe 8,639304768518517 €. Der zusätzliche CLI-Test steht getrennt im Kassenblatt: ein zugelassener HTTP-Modell-POST, abgewiesen mit 429; ein weiterer POST-Versuch vor dem Netz gesperrt. Die Sitzungsdatenbank enthält für den Test keine Kostenangabe (`null`), und `--usage-file` wurde wegen des Abbruchs nicht geschrieben. **Kosten unbekannt, nicht als 0 € ausgegeben.** Die Datenbankzählung von 0 API-Aufrufen ist kein Ersatz für den beobachteten HTTP-Versuch.

## Eigene Fehler und Grenzen
- W1-Adresse zunächst trotz erfolgter Bereitstellung nicht im Meldetext genannt; inzwischen nachgeliefert.
- Erste Aussage zu 0,3978 € präzisiert: zunächst Altbericht gelesen; erst später aus DB bestätigt.
- Timeout im Nachweis-Wrapper nicht abgefangen; Abschlussmetadaten fehlten deshalb. `ABBRUCH-01.json` ist ein ausdrücklich rekonstruierter Nachtrag aus der tatsächlichen Fehlermeldung, keine vorgetäuschte reguläre Ausgabe.
- W2-Zeitbedarf überschritt die beabsichtigte Kurzprüfung; eine weitere Untersuchung der historischen Fehlzahl wurde beendet.
- `.err` des Tests vollständig gelesen: leer. Der Fehler steht in HTTP-Antwort und Wrapper-Timeout, nicht in `.err`.

## Offen / nächste Entscheidung
1. Trägerordnung zwischen Telegram-Sitzung und CLI ausdrücklich festlegen; keine Änderung durch Hermes in diesem Auftrag.
2. Erfolgreichen Trägernachweis erst nach neuer Freigabe und Klärung des 429-Fehlers versuchen; keine automatische Wiederholung.
3. Tatsächliche Kosten des abgewiesenen Tests sind unbekannt; separat nachtragen, falls ein Anbieterbeleg vorliegt.
4. Herkunft der alten 0,1190 € und die bereits im Nachlauf gebuchten Lauf-23-Zeilen bleiben offen.
5. Fassung 7 durch Chat-Claude; danach Vorbedingung 2, Verfassung des Handelssystems, Freigabe allein Philipp. Kein Lauf gestartet.
6. Eigene Domain für den Prüfkanal später; derzeit weiter auf der Kundenseite.
7. Bewusster Sitzungsreset: in Telegram `/new`; hier nicht als bereits erfolgt behauptet. Kein weiterer Auftrag in dieser Sitzung.

## Abholadressen
Bericht:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/ZWISCHENBERICHT.md

Dateiliste:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/DATEIEN-01.txt

Ordnerprüfsumme:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/PRUEFSUMME-ORDNER-01.txt

Kassenblatt:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/KASSE-01.md

Gedächtnisstand:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/STAND-01.md

Gedächtnisregeln:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/REGELN-01.md

Gedächtnisunterbau:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/UNTERBAU-01.md

Gedächtnisdateiliste:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/DATEIEN-01.txt

Gedächtnisprüfsumme:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/PRUEFSUMME-ORDNER-01.txt
