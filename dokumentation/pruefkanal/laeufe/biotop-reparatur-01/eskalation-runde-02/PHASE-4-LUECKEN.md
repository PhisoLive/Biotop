# Phase 4 — vier zurückgestellte echte Lücken

Auftraggeberentscheidung 2026-09-20T15:40:52.015433+00:00. Alle Einträge sind **offen**, nicht widerlegt oder repariert. Sie werden am Handelssystem anhand echter Fälle bearbeitet, nicht weiter im jetzigen Auftrag gegen zusätzliche konstruierte Fälle.

## P4-01 — Wirkungskreis mit transitiven Folgen
Befund-IDs: EICH-1, MASS-01
Tatsächlich angewandte Zusatzdateien und verhandelte Anpassungen erweitern den gespeicherten Wirkungskreis nicht vollständig; ein betroffener gesperrter Bereich kann dadurch geschrieben werden.
Prüfziel: Am Handelssystem tatsächliche Dateiänderungen und transitive Abhängigkeiten inklusive Verhandlung gegen reale Fälle prüfen; unbetroffene gesperrte Bereiche nicht pauschal zum globalen Stopp machen.
Status: offen; auf ausdrücklichen Auftraggeberentscheid zurückgestellt, nicht behoben

## P4-02 — Vertragsaustausch zwischen Vorspann und Freeze
Befund-IDs: EICH-3
Ein nach Vorspann ersetzter Eichvertrag invalidiert den historischen Nachweis an späteren Vorstufeneingängen nicht.
Prüfziel: Aktuelle Vertragsidentität und Bytes mit dem versiegelten Gegenstand binden; legitime spätere Vertragsentwicklung gesondert behandeln.
Status: offen; auf ausdrücklichen Auftraggeberentscheid zurückgestellt, nicht behoben

## P4-03 — NaN/Null in Rauschwerten
Befund-IDs: MASS-02
Der Collector lässt eine ValueError aus einem ungültigen Bereich global propagieren; gesunde Bereiche und Arbeitsbelege gehen mit verloren.
Prüfziel: Ungültige Werte nur bereichsweise sperren, Roh- und Verbrauchsbelege erhalten; keine Freigabe über Rückfallwerte und keine Schwellenänderung.
Status: offen; auf ausdrücklichen Auftraggeberentscheid zurückgestellt, nicht behoben

## P4-04 — Vorstufenbindung beim Maß-Freeze
Befund-IDs: EICH-2
Ein gespeichertes generation0.ergebnis kann trotz erreicht=false als ausreichende Freeze-Vorstufe gelten.
Prüfziel: Vor Freeze tatsächlich erfolgreichen, konsistenten Vorstufenbeleg verlangen; aktuelle Fehlversuche nicht durch älteren Erfolg verdecken.
Status: offen; auf ausdrücklichen Auftraggeberentscheid zurückgestellt, nicht behoben

## Erhaltene Belege
Originale Eichungsreview-Befunde:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-05/reviews/pruefer-eichung/REVIEW.json
Originale Maßreview-Befunde:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-05/reviews/pruefer-mass/ERGEBNIS.json
Eltern-Reproduktionen mit Einzeltests/Assertionfehlern:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-05/ELTERN-REPRODUKTION.json

## Abgrenzung
Vier Einträge, fünf Reviewer-Befund-IDs: EICH-1 und MASS-01 sind zwei Zugänge zur gemeinsamen Wirkungskreislücke. EICH-4 ist nicht zurückgestellt; er bleibt der offene Blocker der Vertragsgegenprobe im Kernauftrag. Die bisherigen roten Repros werden nicht grün umetikettiert.
Die Aussage „vier Bereiche und 856 Zeilen“ stammt vom Auftraggeber. Daraus wird keine gemessene Unmöglichkeit dieser Fehler abgeleitet. Die bewusste Eingrenzung des Abschlussgegenstands wird umgesetzt, nicht als technische Entwarnung ausgegeben.
