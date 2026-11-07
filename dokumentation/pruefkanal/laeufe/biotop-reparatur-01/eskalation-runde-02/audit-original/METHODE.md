# Wiederverwendbare Methode: begrenztes lesendes Nachweisleser-Audit

- Ein disjunktes Eingabeinventar mit Hashes einfrieren; bei parallel laufender Integration auf eine bytegleiche Originalkopie wechseln. Den Vergleich gegen das Inventar rechnen, nicht behaupten.
- Jede Inventardatei lesen und genau einmal erfassen. Leere Dateien sind gelesene Nichtleser, keine ausgeführten Prüfungen.
- Semantische Einheiten über Eingabeherkunft, konkreten Aufruf/Datenfluss und wirkendes Prädikat bestimmen. Regexzeilen separat zählen; sie ersetzen weder Leser- noch Fehlerzählung.
- Eingebettete Programme und Shell-Python ebenso verfolgen wie Imports, Wrapper und Ergebnisweiterleitungen.
- Abwesenheit eines Fehlers nur bei nachgewiesener Ausführung und vollständiger erwarteter Population akzeptieren. Leere gültige Fehlermengen sind legitim; fehlende Tests, abgebrochene Läufe und ausgelassene Pflichtzeugen nicht.
- Vor einem all([])-Befund den Produzenten prüfen: negative Ersatzzeugen können den lokal vacuösen Zustand im realen Datenfluss unerreichbar machen.
- Ein Probegegenprädikat muss an den beabsichtigten ausgeführten Zeugen gebunden sein. Ein beliebiger Fehler oder ein negativer Gesamtstatus ist kein gültiger roter Kontrollfall.
- Historische Berichts-/Kostenanzeigen von wirkenden Abnahmeentscheidungen trennen. Außenbefunde bleiben mit Quelle und Minimalzustand bestätigt offen, ohne Reparaturumfang zu erzeugen.
- Alte überlappende Mechanismen separat offenhalten. Ein Guard für Ausführung repariert keine falsche Bereichsauswahl, Vertragsschwächung, komplette Numerikstrecke oder nachgelagerte Freigabebindung.
- Den tatsächlichen Suchabschluss messen: Dateilesung, semantische Blöcke, Kandidaten und offene Feinzuordnungen separat ausweisen. Keine Restmenge als Null oder erledigt etikettieren.
- Nur Auditmetadaten validieren, wenn Ausführung untersagt ist. Parser-/Biotop-Testgrün darf nicht aus einem erfolgreichen Inventarvalidator abgeleitet werden.

Diese Methode wurde wegen des Schreibbereichs ausschließlich hier dokumentiert; keine Änderung an aktiven Skills/Profilen/Produktquellen.
