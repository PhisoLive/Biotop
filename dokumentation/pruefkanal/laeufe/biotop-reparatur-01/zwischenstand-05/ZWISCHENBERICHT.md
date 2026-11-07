# Reparatur01 — Zwischenstand05: Abschlussreview fehlgeschlagen

**Keine Abnahme und keine Freigabe für eine natürliche Messung.** 2026-09-20T15:20:53.444443+00:00

Die beiden unabhängigen Reviews sind zurück und beide passed=false. Ihre 6 Logikbefund-IDs verteilen sich auf 5 Mechanismen. Ich habe ihre Zusatztests gegen den aktuellen Elterncode wiederholt: **7 von 16 fehlgeschlagen, 9 von 16 bestanden**. Die Fehler sind echte Erwartungsverletzungen, keine fehlgeschlagene Testcollection. Ausgänge43/44 und jede Assertion liegen unter elternpruefung/.

## Wieder offene Abnahmepunkte

1. Vertragsgegenprobe: Modulabhängigkeiten gehen im Testklon verloren; der benannte Vertrag kann auch im Gegenfall selbst kaputt sein. Das andere Bool-Ergebnis reicht nicht. Die frühere allgemeine Abnahmeeinordnung ist zurückgenommen, nicht die historische Ausführung gelöscht (KORREKTUR-01.md).
2. Wirkungskreis: tatsächliche zusätzliche Diffziele und transitive Folgen verhandelter Nachbaränderungen fehlen. Die Rauschsperre lässt so Änderungen in gesperrten Bereichen passieren. EICH-1 und MASS-01 sind zwei reproduzierte Zugänge zum selben Grundproblem.
3. Gen0-Gate: eine Vorstufe mit erreicht=false genügt derzeit allein durch ihren Ergebnisdatensatz für den Maß-Freeze. Benötigt wird ein tatsächlicher konsistenter Erfolg.
4. Eichgegenstandsbindung: Vertragsaustausch nach Vorspann wird vor Gen0/Freeze nicht erkannt.
5. Ungültige Rauschwerte: Null/NaN propagieren global; der gesunde Nachbar samt Bereichs-/Kostenbelegen geht verloren, statt nur den defekten Bereich zu sperren.

Die Wertevalidierung wird nicht zurückgenommen, die Rausch-/Pareto-/Abnahmeschwellen werden nicht gesenkt. A/C+B-Bestands-Replays und historische Gültigkeitsbilanz bleiben eigene, bereits gelieferte Belegarten; ein fehlender neuer Reviewbefund dazu ist kein Ersatz für die offenen Reparaturteile.

## Laufende Arbeit — ausdrücklich noch kein Ergebnis

Erster Review-Nachbesserungszyklus, deleg_16dbf49d: drei neue Fix-Kontexte, jeweils isolierte Quellkopie und feste Dateizuständigkeit. Vorstufenbindung, Wirkungskreis/Collector und Vertragszeugen werden mit eigenem Rot/Grün bearbeitet. Keine bezahlten Biotop-Modelle; keine produktiven DB-/Werkwrites. Der Elterncode ist seit Vorbereitung in 125 von 125 Quellvergleichen unverändert. Keine Änderung eines Fixagenten wurde bislang integriert oder als bestanden gewertet.

## Noch offen vor Abschluss

- Sämtliche sechs Befund-IDs beheben und Parentregressionen grün nachweisen; beide Wirkungskreiswege einzeln behalten.
- Vertragszeugen direkt positiv/negativ prüfen, danach alle vier echten Eichpaare mit gültigen Zeugen im integrierten Code und vollständigen Rohbelegen wiederholen.
- Gesamtsuite mit Kernmaß/Pareto zuerst, echte private CLI-Abnahme und Bestandsvergleich nach Integration; keine natürliche Evolution.
- Erneutes unabhängiges fail-closed Review, danach endgültiger Quellabschluss, Kasse und versiegelter Abschlussordner. Nach zwei gescheiterten Fix-/Reviewzyklen wird eskaliert statt endlos weitergepatcht.
- Die nächste natürliche Messung bleibt einer frischen Sitzung mit neuen Lauf-IDs vorbehalten.

## Kasse und Beweisgrenzen

0 neue Biotop-Kassenbuchungen seit ID4070, 0 € belegte Biotop-Modellkosten von 5,00 € hartem Budget. Trägersitzungen und fehlende monetäre CPU-/Abokostenmessung stehen separat in KASSE.md/.json. Der produktive DB-Inhalt ist seit CLI41 im vollständigen Dump unverändert. Die Repros sind Unit-/lokale Fixtureprüfungen, keine Kammerabnahme oder natürliche Messung. Keine Geld-/Laufzeitzahlen aus Test-Doubles werden als reale Verbrauchsmessung ausgegeben.

Bericht:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-05/ZWISCHENBERICHT.md
Dateiliste:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-05/DATEIEN.txt
Manifest:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-05/MANIFEST.sha256
Ordnerprüfsumme:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-05/PRUEFSUMME-ORDNER.txt
Kasse:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-05/KASSE.md
Voriger versiegelter Stand:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-04/DATEIEN.txt
