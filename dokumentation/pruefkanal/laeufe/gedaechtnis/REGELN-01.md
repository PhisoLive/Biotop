# Regeln — Fassung 01 · 2026-09-20T03:17:33.347176+00:00
Herkunft: Abschnitt 5 des Wiedereinstiegsbriefs, ergänzt um die vom Auftraggeber mitgeteilten Entscheidungen. Kein von Hermes erfundener Masterprompt v7.
Nur HERMES-1 schreibt; HERMES-2/HERMES-3 lesen.

Kurzfassung. Die vollständige Sammlung steht im Änderungsverzeichnis Fassung 7.

**Belege**
- Keine Zahl aus dem Gedächtnis. Jede Zahl aus einer Protokollabfrage, die Abfrage beigelegt.
- Jede Zahl nennt ihre Menge im Satz daneben — was genau gezählt wurde, mit Nenner.
- Die Herkunft steht dabei: laufender Lauf, gestellte Prüfung oder Rekonstruktion.
- „Bestätigt durch Ausführung" nur mit beigefügter Ausgabe, sonst „gelesen, nicht ausgeführt".
- Eine berichtigte Zahl braucht ihre eigenen Eichfälle.
- Jede Aufstellung nennt, ob sie vollständig ist oder ein Auszug.

**Maßstäbe**
- Ein Maßstab wird vor der Messung gesetzt und danach nicht verhandelt. Eine Grenze wird nie verschoben, damit etwas durchgeht.
- Laut scheitern, nie still. Eine Prüfung ohne Gegenstand meldet das, statt zu bestehen.
- Eine Sperre ohne Sperrung meldet „nicht gemessen", nicht „bestanden".
- Ein Sperrbauteil wird am Zustrom gemessen, nie am Rest.
- Je Tor ein roter und ein grüner Eichfall.

**Läufe und Kasse**
- Jede Messgerätänderung erzwingt einen neuen Lauf. Während eines Laufs wird nichts am Messgerät geändert.
- Abbrüche und abgewiesene Aufrufe erscheinen im Bericht **und** im Kassenblatt. Ein folgenloser Abbruch ist erlaubt, ein verschwiegener nicht.
- `.err`-Dateien nach jedem Lauf durchsehen, den Befund nennen — auch wenn sie leer sind.
- Der Gesamtstand wird gegen die Summe der Einzelläufe geprüft, jede Abweichung benannt.
- Ein Aufruf trägt genau eine Lauf- und Abschnittszuordnung.

**Ablieferung**
- Keine Datei überschreiben. Nummerierte Namen, jede Adresse einmal.
- Melden und Abliefern sind ein Vorgang: erst hochladen, dann Dateiliste und Prüfsumme neu schreiben, dann melden.
- Jeder Bericht nennt Bericht, Dateiliste, Ordnerprüfsumme und Kassenblatt als ganze URL in eigener Zeile.
- Abgeliefert wird **auch bei Abbruch**. Ein Abschlussordner ohne Ergebnis ist ein Ergebnis; eine Meldung ohne Ordner ist keines.

**Rollen**
- Hermes führt aus. Chat-Claude ist Auftraggeber, Prüfer und Korrektiv. **Philipp entscheidet und gibt ab Phase 4 allein frei.**

## Ergänzungen nach dem Wiedereinstieg
- **V17:** Eine Sitzung, ein Auftrag; erst Abschlussordner liefern, dann bewusst zurücksetzen. Neuer Auftrag in frischer Sitzung.
- **V18, durch V19 präzisiert:** Dauerhaftes Wissen liegt im Gedächtnisordner und Abschlussordner, nicht im Sitzungskontext.
- **V19:** `laeufe/gedaechtnis/` ist die einzige dauerhafte fachliche Gedächtnisablage. Kein Obsidian-Tresor. Nummerierte Dateien nie überschreiben. `STAND` nach jedem Auftrag, `REGELN` nach neuer Masterprompt-Fassung, `UNTERBAU` bei Maschinenänderung. Diese Initialfassung enthält die ausdrücklich übermittelten Ergänzungen, auch vor dem Ausschreiben von v7.
- **V20:** Kassenabgrenzung gemäß Auftraggeber umgestellt; Zahlen ausschließlich im verlinkten Kassenblatt führen, keine zweite laufende Buchhaltung im Regelwerk.
- **Fassung-7-Ergänzung 25 (Auftraggeber):** Der Auftraggeber prüft, ob eine verlangte Abfrage etwas kostet, bevor er sie in eine Liste mit „0 Modellaufrufe“ schreibt.
- **Fassung-7-Ergänzung 26 (Auftraggeber):** Eine abgeleitete Zahl trägt nie mehr Genauigkeit als ihre Eingangswerte. Steht eine gemessene Zahl daneben, gilt die gemessene. Die konkrete Rundungsbegründung im Begleitbrief wurde von Hermes anhand der Rohdaten widerlegt; die Regel wird dadurch nicht aufgehoben.
- **Trägernachweis:** einmalig freigegebener kurzer Modelltest, separat verbuchen, Ausgabe wörtlich mit Datum dokumentieren. Keine Wiederholung außer bei Trägerwechsel oder Abweichungsverdacht und passender Freigabe. Abweichung zuerst melden; keine eigenmächtige Modelländerung. Ein fehlgeschlagener Test ist kein Trägernachweis. Der CLI-Test beweist nicht das Modell einer anderen, laufenden Sitzung.
- **Schutz des Unterbaus:** Nur Pfade, Konfigurationsschlüssel und Anmelde-Metadaten veröffentlichen. Keine Passwörter, API-Schlüssel, OAuth-/Sitzungstokens oder vollständigen Auth-Dateien in den Prüfkanal legen.

Bericht mit offenen Punkten und Quellen:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/ZWISCHENBERICHT.md
