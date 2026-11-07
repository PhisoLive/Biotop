# Zeilenweiser F6-Abgleich

`MASTERPROMPT-ZEILEN-01.csv` enthält **470 von 470 physischen Originalzeilen**, jeweils ungekürzt mit Bewertung und Befundzuordnung. Leerzeilen, Überschriften, Änderungshistorie, Schätzungen und zukünftige Torforderungen sind ausdrücklich von laufzeitfähigen Codeanforderungen getrennt. `24-zeilenabdeckung.json` prüft eindeutige Zeilen und fehlende Nummern.

Die Codeabweichungen stehen nicht nur in einem Matrixhäkchen: `ABWEICHUNGEN-01.md` nennt für jede Gruppe den Mechanismus und die Originalcodezeilen. Der unveränderte Quellstand ist beigelegt. Die zwei Einzelprüfungen bleiben vollständig einsehbar, einschließlich aufgehobener Kritik und Risiken. Keine additive „60 Fehler“-Schlagzeile aus überlappenden Befunden.

## Versionsgrenze

Untersucht ist der heutige Quellstand `b42dc941e7fcb66632ba6a0e13b8df106a270a31`. Gegen den archivierten F6-Ausgangspunkt `7c73d403c18755dda26655c78ac7290c446d9f45` sind 17 Dateien verändert (1815 eingefügte, 23 entfernte Zeilen laut Git; nicht gleich physischer Größenunterschied). Nur zwei davon sind produktive Organmodule: `aegis.py` und `gedaechtnis.py`. Die anderen sind Prüfscripte. Quelle: `18-historischer-codevergleich.json`, vollständiger Diff im Prüfungsanhang A.

Deshalb gilt F6 als verlangter Solltext, aber nicht als Beschreibung des heutigen Ist-Stands: Ansage und Mindestanteil wurden später gebaut, ebenso eine zusätzliche Aufnahmesperre C. Aktuelle C-Lücken werden als spätere Lücken ausgewiesen, nicht dem früheren F6-Code untergeschoben. Die historischen Läufe 1–23 werden separat gerechnet, Lauf 24/25 nicht hineingemischt.

## Grenze des Versprechens „jede Abweichung“

Der Solltext wurde vollständig zeilenweise abgeglichen, der produktive Python-Quellstand vollständig in den kombinierten Leseabdeckungen erfasst. Alle gefundenen Abweichungen sind aufgeführt. Eine endliche Codeprüfung kann nicht beweisen, dass kein weiterer Fehler existiert. Statische Risiken sind keine ausgeführten Gegenfälle; heutige Abnahmegrenzen wurden nicht herabgesetzt.
