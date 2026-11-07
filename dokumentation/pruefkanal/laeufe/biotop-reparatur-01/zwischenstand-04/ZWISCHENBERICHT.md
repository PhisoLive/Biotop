# Reparatur01 — Zwischenstand04, 2026-09-20T14:51:48.962521+00:00

**Die vier echten Gegenproben sind im zusammengeführten Elternstand ausgeführt: vier von vier absichtlich falsch, bei vier von vier positiven Treffern.** Alle acht Fälle sind ausgeführt und prüfbar. Das unabhängige Abschlussreview läuft noch; deshalb weiterhin kein abgeschlossener Reparaturauftrag und keine Freigabe zur nächsten natürlichen Messung.

## Priorität und Nachweis
- Die ersten 15 von 180 ausgeführten Eigen-Tests betreffen Kernmaß/Pareto. Die tatsächliche JUnit-Reihenfolge wurde geprüft, nicht aus Dateinamen vermutet.
- 180 von 180 Eigen-Tests bestanden, 0 übersprungen; Rohausgabe40. Diese Grünzahl ersetzt nicht die Probeempfindlichkeit. Die früheren drei Gegenmutanten bleiben ein eigener Nachweis.
- Die vier Eichpaare liefen zuerst separat im integrierten Stand39, erneut in der Gesamtsuite40, schließlich durch die echte CLI41 samt realer Rauschmessung und Fundneubewertung. Derselbe Prüfer wertet positive und negative Eingaben aus. **Normgegenprobe hat norm=[] und expliziten Zuwachs0, bleibt trotzdem falsch.** EICHPROBEN.md nennt jeden Grund und Mechanikbeleg.
- Der frühere immer-sperrende Vorspann ist ersetzt. Die reale private CLI41 endet mit Exit0; ihr versiegelter Nachweis lässt das gen0-Eingangstor passieren. Sperr-/Stufenfolgetests bleiben separat als Unit-/Subprozessnachweise. Generation0 und Evolution wurden hier nicht gestartet.
- Rauschmessung41: 0 von 4 Bereichen gesperrt; alle Werte im Rohbeleg. Kein Grenzwert abgesenkt, kein Wiederholen bis Grün.
- Schutz41: 5 von 5 Vorher-/Nachher-Vergleichen unverändert, darunter produktive DB und produktives Werk. Die Entwicklungsquellen im /root/biotop-Arbeitsbaum sind dagegen absichtlich repariert; kein pauschaler Unverändert-Anspruch.

## A/B/C und historische Gültigkeit
Bestands-Replay42 nach sämtlichen Integrationen ist bytegleich mit34. Es bleibt ein Replay, keine neue natürliche Wirkungsmessung. Der B-Halbanteil wird nur soweit fremde Muster verfügbar sind beansprucht; im Lagerhaus nicht als erreichte absolute Halbquote dargestellt. STATUS-GUELTIGKEIT.md und die vollständigen Teilberichte unterscheiden gültige Beobachtungen, Rücknahmen und Vorbehalte. Alte Normwertungen und die Satz2-Vorbehalte der Läufe22/23 bleiben unverändert zurückgenommen bzw. vorbehalten. Lauf24/25 werden nicht nachträglich umgeschrieben oder weitergeführt.

## Fehler und Grenzen dieser Integration
Der vollständige Aegis-Teilpatch ließ sich wegen der bereits integrierten A/C-Kontextargumente nicht unverändert anwenden. Drei begrenzte Probeoption-Hunks wurden zusammengeführt; Kandidaten-/Ansagekontext bleibt im normalen Zweig erhalten. Eigen-Test37 scheiterte korrekt an der fehlenden Option,38 besteht. Beide Ausgaben bleiben erhalten.
Ein NUL-Zeichen im neuen lokalen Review-Vorbereitungsskript wurde durch den Syntaxcheck entdeckt und vor Ausführung entfernt; ein erster Patchversuch passte nicht, anschließender vollständiger korrigierter Schreibvorgang und Ausführung erfolgreich. Keine Produktmessung daraus abgeleitet. Ein von mir fehlerhaft formulierter Rauschformelsatz im Reviewerprompt wurde sofort auf die tatsächliche F6-Formel korrigiert (1+getrimmte Spannweite+0,10; mindestens1,15; >1,5 sperren). Keine Produktregel dafür verändert.

## Noch offen
1. Unabhängige Reviews der integrierten Eichung/Vorspann- und Maß/A/C/B-Änderungen; Befunde prüfen und jetzt beheben, falls bestätigt.
2. Erforderliche Nachtests nach eventuellen Korrekturen, endgültiger Quellabschluss und finale Versiegelung.
3. Eine nächste natürliche Messung ausschließlich in frischer Sitzung und mit neuen Lauf-IDs. Die gestattete gemeinsame Elternsitzung gilt nur für diesen Reparaturauftrag.

## Kasse und Abholung
0 neue Biotop-Buchungen, 0 € Modellkosten von5,00 € hartem Budget. Hermes-Abokennzeichnung und Beweisgrenze, Kammeraufwand und historische Buchungen werden in KASSE.md/.json getrennt geführt.
Alte Zwischenstände bleiben bytegleich erhalten. Teilberichte sind ursprüngliche Belege, keine widersprüchlichen heutigen Abschlussbehauptungen; aktuelle Einordnung steht hier.

Bericht: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-04/ZWISCHENBERICHT.md
Dateiliste: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-04/DATEIEN.txt
Manifest: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-04/MANIFEST.sha256
Prüfsumme: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-04/PRUEFSUMME-ORDNER.txt
Kasse: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-04/KASSE.md
