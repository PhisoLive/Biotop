# Integrationsentscheidung des Parents — zweite und letzte Runde

## Vertrags-Eigentest, keine Produktnachbesserung

Die Messgerätlieferung meldete einen bereits ausgeführten Integrationskonflikt: `test_review_vertrag.py` verlangte eine gültige Messhülle, obwohl der Testkörper am Setup nicht lief. Der spätere Aegis-Teststand ergänzt Skip/xfail, sodass derselbe Widerspruch dort ebenfalls auftritt.

Parent-Beleg `ausgaben/60-vertragszeugen-integration.{txt,xml,json}` reproduziert **3 von 6 Fällen fehlgeschlagen**: setup, skip, xfail, jeweils ausschließlich an `messung.gueltig is True`. Die Gegenprobe war in allen drei Fällen bereits korrekt nicht prüfbar; dies war keine falsch-grüne Produktfreigabe.

**Eigene Integrationsentscheidung, unmittelbar aus der bereits beauftragten F7-Regel:** Die Tests verlangen jetzt ausdrücklich `gueltig=False` und das Fehlen eines Kernmaßes für Setup/Skip/xfail/Sammelabbruch. Ein tatsächlich ausgeführter Call-Fehler bleibt gültiger Inhalt. Im Fall eines manuell entfernten benannten Vertrags bleibt die verbleibende Messung gültig, während der gezielte Zeugenprüfer die fehlende Vertragskontrolle sperrt. Keine Assertion auf `pruefbar=False`, `bestanden=False`, spezifische Skipzeugen oder Batteriesperre wurde entfernt. Keine Schwelle oder Produktdatei für diese Anpassung verändert.

Parent-Beleg `ausgaben/61-vertragszeugen-integration-gruen.{txt,xml,json}`: dieselben **6 von 6 Fällen bestanden**, keine Errors/Skips. Die vorherige Testfassung bleibt bytegenau in der Aegis-Lieferung mit ihrem ursprünglichen Manifest erhalten. Das ist eine explizite Erwartungsanpassung zur Integration zweier Teile derselben Runde, kein behaupteter weiterer Produkt-TDD-Zyklus. Die unabhängige Schlussnachprüfung muss diese Entscheidung mitprüfen.

## Scope des Inventaraudits ist nicht die Integrationsallowlist

Das reine Originalaudit nennt auch Gen0, Aufnahme und Anzeigen `kernpfad`, weil es einen breiten mittelbaren Datenfluss zur Laufsteuerung beschreibt. Diese Bezeichnung hebt die versiegelte engere Auftragseingrenzung02 **nicht** auf. Der Parent erhält die Originalklassifikation unverändert und liefert daneben eine explizite Reparaturzuordnung.

Nicht integriert: Aufnahme; Gen0-Mutantenfang, Äquivalenz und Testbau; leere Herstellerantwort (`all(ids)`); Gen0-Originalgegenlauf und leere Zielpopulation; historische Parallelprüfer. Ihre bestätigten Originalmechanismen bleiben benannt offen und werden nicht durch die engere Einordnung erledigt. Die vier bestehenden P4-Mechanismen bleiben separat erhalten. Sollte eine konkrete Schlussnachprüfung einen unmittelbaren Durchgriff auf die beauftragten Kernkriterien belegen, wird er als Restfehler an Philipp eskaliert, nicht in einer dritten automatischen Runde repariert.

Die Originalabdeckung bleibt ausdrücklich **126 gelesene Dateien von 126 inventarisierten**, **145 dokumentierte Leserblöcke**, **8 offene semantische Kandidaten**, **45 von 661 breite Quellzeilen ohne abgeschlossene Feinzuordnung**. Dies sind unterschiedliche Nenner, keine vollständige semantische Entwarnung.
