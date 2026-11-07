# Spezifikationen für den nächsten Auftrag (aus der Behebungsrunde 4 vor T4, Review 04)

Stand: HEAD `43b8fad` (Runde 4 + Nachtrag). Nach der Regel „ein Review, keine Fix-Kaskade“ wurde nach dem Review kein
Code mehr gebaut. Die Befunde sind in der Kammer gemessen (Proben unter `review-proben/`, Kammerläufe gegen `43b8fad`).
Philipp hat am 24.09. entschieden (Entscheidungen Chat-Claude zu Runde 5). Danach ist jede Zeile unten einer
Entscheidung zugeordnet. Erster Schritt der Runde 5: jede Probe als pytest-Spezifikation fassen, rot an `43b8fad`, mit
grüner Gegenprobe.

| Nr | Spezifikation | Beleg an `43b8fad` | Gegenprobe | Runde 5 |
|---|---|---|---|---|
| R5-1 | Festhalten heißt fallende Zusicherung: Eine Ausnahme aus Werkcode unter Verfälschung hält nichts fest | Review 04 Nr. 1: x3 überlebt, 6 von 6 Tab-Beobachtungen gedeckt über `normieren(normieren(t)) == normieren(t)` | x3k ohne diese Zeile: abgelehnt | Entscheidung 2 |
| R5-2 | Slots der Basisklassen im Zustandsvergleich (`kan`) | Nr. 2: p22 0 Abweichungen, tragfähig | p22k (eigener Slot): 28 | Entscheidung 1 |
| R5-3 | Verschleierte Slot-Namen (`__x`) | Nr. 3: p21 0 Abweichungen, tragfähig | p19 (unverschleiert): 28 | Entscheidung 1 |
| R5-4 | `csv.DictReader` nicht ersetzen; ein Lastabbruch trifft nur die betroffene Funktion | Nr. 4: q1 `SondeAusgefallen` für den ganzen Kandidaten | q1k (`csv.reader`): 6 Abweichungen | Entscheidung 3 |
| R5-5 | Elemente eines Iterator-Objekts und Iterator-Kappe: nie „0 Abweichungen, tragfähig“ | Nr. 5: p18c 0, `teilweise` 48; p14 0, `iterator_gekappt` 14 | p18ck (Generator): 40 | Entscheidung 1 |
| R5-6 | Verfälschungskappe: zurückstellen mit Grund, gezählt; an einem Kandidaten in T4-Größe gemessen | Nr. 6: gelesen (Ablehnung ohne Grund) | — | Entscheidung 4 |
| R5-7 | Register der verlangten Aufrufe, Tor-4-Skript ruft die Torzeile „Schwächen“ | Nr. 7: kein Aufrufer | — | Entscheidung 5 |
| R5-8 | Vorspann verweigert ohne Stufe 2; Test mit gestellter Dauer > 60 s; Stufe 2 bemessen, bis `eingang` nicht sperrt | Nr. 8: gelesen; Nachspiele: `eingang` gesperrt in 3 von 6 | — | Entscheidung 6 |
| R5-9 | Lastaufrufe tragen die Formmerkmale ihrer Eingabe | Nr. 9: gelesen | — | Entscheidung 7 |
| R5-10 | `os.PathLike` als Wert über `os.fspath` | Nr. 10: lokal, `kan(Path)` inhaltslos | — | Entscheidung 1 |
| R5-11 | Eichproben, Toleranz und gespeicherte Maße an derselben Stufe | Nr. 14, 15: gelesen | — | Entscheidung 8 |
| R5-12 | Ausschluss eigener Tests nach Testkennung einschließlich Parametrisierung | Nr. 16: lokal (`test_neu[1]` nicht ausgeschlossen) | — | Entscheidung 8 |
| R5-13 | Nachspiel als echter Durchlauf in der Regression | Nr. 18: 7 von 7 Nachspielen an `1d9a5aa` abgebrochen, Regression grün | — | Entscheidung 8 |
| R5-14 | Koroutine, die an Objekte einer fremden Ereignisschleife gebunden ist | Nr. 17: gelesen | — | nicht entschieden: Liste |

Berichtigungen ohne Code (Review 04 Nr. 11, 12, 13): Die betreffenden Aussagen sind im BERICHT §10 berichtigt.
