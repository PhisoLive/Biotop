# INFINITE EVOLUTION — Das Biotop

**Übergabedokument und Masterprompt für Hermes**
Stand: 21.09.2026 · Fassung 7 · Auftraggeber: Philipp Zöllisch · Prüfer: Chat-Claude

**Änderungen gegenüber Fassung 6** (aus der Abnahme von Vorbedingung 1 und Philipps Richtungsentscheidung vom 21.09.2026):
- **Phase 4 ist neu gefasst: Breitentest an mehreren Testwerken statt einem großen echten Werk.** Grund: Philipps Entscheidung — das Biotop soll für jeden Anwendungszweck taugen und dafür in allen Bereichen geprüft sein. Das Handelssystem stand in den Fassungen 1 bis 6 als Phase-4-Werk, war aber eine nie bestätigte Vorentscheidung von Chat-Claude; alle darauf bezogenen Bezugsgrößen (237.000 Zeilen, 17 Dienste, 135 Testfehlschläge) sind gestrichen. **Fehler von Chat-Claude:** eine Vorentscheidung sechs Fassungen lang wie eine Entscheidung geführt.
- **Phase 5 neu: erstes echtes Werk**, ohne benanntes Werk — die Wahl trifft Philipp nach dem Breitentest, nach den Kriterien in Abschnitt 8.
- 2a: Zwei Grundsätze ergänzt (7: Ein Nachweis zählt nur, wenn er ausgeführt wurde. 8: Jede Probe braucht eine Gegenprobe, die fehlschlagen muss) und einer (9: Der Prüfaufwand muss zum Gegenstand passen).
- 3.6: Ausfall eines Verbundmitglieds zählt nie als Beitrag — mit Torzeile, weil die Regel noch nicht nachgewiesen ist (Opus hat eine große Eingabe mit `stop_reason: refusal`, Kategorie `cyber`, abgelehnt; HTTP 200 ohne Ausgabetext).
- 8: Vorbedingung 1 **abgenommen** (21.09.2026): Tor 2 Zeile 8 erfüllt mit 9,09 %, Artgedächtnis 3 von 5 Richtungen mit werkübergreifendem Verweis.
- 6: Kassenstand aus der Datenbank 8,64 € statt der aus Berichten summierten 7,82 € — die Datenbank ist die gültige Quelle.

**Änderungen gegenüber Fassung 5** (aus der Prüfung des Abschlussordners Phase-3-Nachlauf, Läufe 21–23):
- **Abschnitt 2a neu: sechs Grundsätze**, die aus wiederkehrenden Fehlerklassen gefasst wurden. Sie stehen vor den Organen, weil jeder von ihnen an mehr als einer Stelle greift.
- 3.7: Der **Ankläger nennt seine Behauptung vorab**; ist sie im Bereich schon aufgestellt, wird der Angriff gar nicht erst ausgeführt. Grund: Die bloße Anweisung, eine andere zu finden, senkte die größte Gruppe von 5 auf 1, aber nicht den Anteil unter 20 % — und **0 Aufrufe** antworteten mit „KEIN ANGRIFF", obwohl das ausdrücklich erlaubt ist. Die Rolle des Gegners erzeugt Zwangsbefunde; die Entscheidung wird dem Modell abgenommen, statt sie ihm anzutragen. Spart zusätzlich Aufrufe.
- 3.12: Der werkübergreifende Block des Artgedächtnisses bekommt einen **festen Mindestanteil an der Vorlage** (Vorgabe: die Hälfte der gezeigten Einträge, mindestens fünf, sofern vorhanden). Grund: Ein `logmuehle`-Lauf sah 13 fremde Muster und lieferte 2 von 5 Verweisen, ein `lagerhaus`-Lauf sah 3 und lieferte 0 — bei 17 Diensten verdrängt die Masse eigener Einträge fremde Muster allein durch Menge.
- 3.5: **Generation minus eins** ist vollständig beschrieben (Rauschmessung mit Ausreißerbehandlung, bereichsweise Sperre, Serienzähler mit Zeitraum-Deutung, die vier Proben am versiegelten Eichgegenstand, Fund-Neubewertung). Gemessene Kosten: 9 Kammerläufe, 4 Modellaufrufe, 0,0057 €, 44 s je Lauf.
- 3.5 neu: **Versiegelter Eichgegenstand** je Werk — ein Bereichspaar mit Vertrag, beim ersten Lauf gewählt, danach unverändert; bei Werken mit Betriebszweck muss der tragende Pfad ausdrücklich in den Regeln stehen, sonst wartet das Organ.
- 3.10: **Probensperre für alle drei Gedächtnisse**, erkannt am gesetzten Merkmal `ist_probe`, nicht am Namen.
- 8, Phase 3: Wertung **auf 8 von 11 korrigiert** — die Torzeile Projektgedächtnis ist erfüllt, nicht „teilweise": 0 von 3 strittigen Fällen sind durchgerutschte Wiederholungen; Hermes' Nachrechnung maß Token statt Ziele und hatte den Filter für verworfene Läufe nicht angewandt. Die Zahl des Organs war richtig.
- 8, Phase 2: Zeilen Nebenwirkung, Regression, Norm, Vertrag **wieder belegt** (4 von 4 mit gehärteten Proben); Zeile 8 bleibt gerissen, Zahl berichtigt auf 68,5 % (gemessen statt geschätzt).
- Anhang B neu: **Verfassung des Übungswerks `logmuehle`**, von Chat-Claude bestätigt.
- 6: Nachlauf gemessen 0,44 € von 10 €.
- 8, Phase 4: Auftrag ausgearbeitet — Vorbedingungen, Reihenfolge, Budget je Abschnitt, Tor 4 erweitert.

**Änderungen gegenüber Fassung 4** (aus der Prüfung des Abschlussordners Phase 3, Läufe 14–20):
- 3.12: Das **Artgedächtnis speichert Muster, keine Instanzen**. Zu jeder angenommenen Generation schreibt ein zusätzlicher Aufruf den abstrahierten Satz ohne Werk-, Datei- oder Funktionsnamen; nur diese Sätze werden werkübergreifend vorgelegt. Grund: 0 werkübergreifende Verweise bei 12 Richtungen in drei Läufen — das Modell übergeht zu Recht Sätze, die an seinem Werk nicht gelten. Die Torzeile bleibt unverändert; erzwungene Verweise wären Scheinbegründungen.
- 3.10: **Doppelungsschlüssel ist die Behauptung** (Ziel-Funktion + Zusicherung), nicht (Meldungsklasse, Ort). Der Anteil wird gegen die **erzeugten Angriffstests** ausgewiesen, nicht gegen Ablehnungen. Grund: Sechs Tests derselben Behauptung kamen einzeln ins Immunsystem und hielten einen Fehler am Leben; gemeldet waren 2,5 %, bei richtiger Bezugsgröße 10,9 %, bei der gemeinten Lesart 83,6 %.
- 3.5: **Rauschtoleranz wird gemessen, nicht gesetzt.** Vor jedem Lauf fünf Messungen am unveränderten Ausgang je Bereich; Toleranz = gemessene Spannweite + 10 Prozentpunkte, mindestens 15 %. Laufzeiten werden als Median aus drei Durchläufen gemessen. Grund: feste 15 % gegen 47 % Eigenrauschen bei `formeln` — Kandidaten starben an Rauschen. Fehler von Chat-Claude in Fassung 4.
- 3.12: **Gescheiterte Wege aus verworfenen Läufen zählen nicht** im Projektgedächtnis; es verwirft Kandidaten ohne Kammerlauf und ist damit Teil des Messgeräts. Grund: Lauf 18 begründete 12 von 13 Verwerfungen mit Lauf 16, dessen Ankläger als falsch erkannt war.
- 3.10: **Fund-Übernahme zwischen Läufen wiederholt die Norm-Prüfung mechanisch** (jeder offene Fund wird am neuen Ausgang in der Kammer nachgemessen), statt den alten Status zu übernehmen. Grund: sechs Normtests standen nach der Übernahme als Funde im Testbestand.
- 3.7: Pareto je Test gilt für Tests im Werk, Verträge und Verfassung; ein **neuer** Angriffstest, der an der Vorgeneration besteht und am Kandidaten fällt, tötet nur bei Absturz des Kandidaten oder bei explizitem Vertrags-/Verfassungsverweis — sonst offen, 0 Punkte, kein Kill. Grund: Lauf 16, der Ankläger schrieb den Fehler als Norm fest und tötete jede Behebung.
- 2, Satz 5 und 4: **Abbrüche nach Satz 2 sind vom Freigabe-Gate ausgenommen** — immer erlaubt, protokolliert. Grund: Hermes konnte Lauf 16 nicht stoppen und er lief weiter.
- 3.5: **Generation minus eins — Messgerät-Eichung vor jedem Lauf.** Nebenwirkungs-, Regressions-, Norm- und Vertragsprobe laufen als Vorspann jedes Laufs, nicht nur einmal als Abnahme. Grund: fünf von sieben Läufen in Phase 3 starben, weil das Messgerät erst im Lauf als kaputt auffiel; Kosten 1,41 € von 2,83 €.
- 9: **Zwischenbericht-Pflicht** — vor jedem Sitzungsende `ZWISCHENBERICHT.md` und `DATEIEN.txt` im Ordner; ein Ordner ohne Bericht gilt als nicht abgeliefert. Endmeldungen nennen die vollständige Abholadresse als ganze URL.
- 4: **Richtungswahl unter Vollmacht** bei Übungswerken (protokolliert); bei Werken mit Betriebszweck wählt Philipp.
- 8, Phase 2: Zeile 8 **rückwirkend gerissen** (Doppelungsanteil 83,6 % gegen Grenze 20 %) — Wertung **9 von 11**. Gebaut bleibt gebaut; die Zahl wird nicht verhandelt.
- 8, Phase 3: Wertung Chat-Claude **7 von 11** (in Übereinstimmung mit Hermes). Torzeilen für Jury und Archivierung umformuliert, Artgedächtnis-Zeile unverändert.
- 6: Phase 3 gemessen 2,83 €; Phase-4-Schätzung.

**Änderungen gegenüber Fassung 3** (aus der Prüfung des Abschlussordners Phase 2, Läufe 11–13):
- 3.5: Grenzmaße messen gegen den **Bestwert des Laufs** (beste angenommene Generation je Maß), nicht gegen den Laufausgang; ohne Kernmaßgewinn nur Rauschtoleranz +15 %, mit Kernmaßgewinn Tauschregel (Vorgabe ×2). Grund: Gen 10 hob `formeln` gegenüber der Vorgeneration um ×5 und `preise` um ×3, regelkonform gegen den Ausgang. Fehler von Chat-Claude in Fassung 2/3.
- 3.5: Generation 0 — äquivalente Mutanten werden vor der Zählung mit Beleg aussortiert; Bezugsgröße „von n nicht-äquivalenten"; zwei Testbau-Durchläufe je blindem Mutanten. Grund: 2 von 3 ungefangenen Mutanten in Lauf 13 waren beweisbar äquivalent; der Testbau ist stochastisch (Lauf 12 fing 18, Lauf 13 17).
- 3.6: „KEIN VORSCHLAG" ist für die Bandit-Gewichtung neutral, kein Misserfolg. Grund: Ein ehrliches „nichts gefunden" wurde wie ein Fehlschlag gebucht — das züchtet Scheinvorschläge.
- 3.7: Norm-Regel gilt für **alle** Tests, die mit einem Kandidaten neu ins Spiel kommen (Ankläger-Tests und mitgebrachte Tests); Vertrags-/Verfassungsbezug nur durch expliziten Verweis (Vertragstest-Kennung oder Verfassungssatz-Nummer), nicht durch Wortüberdeckung. Grund: Lauf 12 zeigte die Lücke bei mitgebrachten Tests (Fehler von Chat-Claude in Fassung 3, zu eng formuliert); Wortüberdeckung ist manipulierbar.
- 3.10: Offene Funde werden nach 5 Generationen ohne Behebung archiviert (nicht gelöscht) und nicht mehr vorgelegt. Grund: 42 offene Ankläger-Meinungen kosteten je Kandidat einen Kammerlauf.
- 2, Satz 2 und 5: Jede Änderung am Messgerät während eines Laufs ist ein neuer Lauf — ohne Ermessen darüber, ob sie „Maßwirkung" hat. Grund: Zwei Korrekturen während Lauf 13 „ohne Maßwirkung", beurteilt vom Ausführenden.
- 9: Die Kandidatenaufschlüsselung eines Laufs muss auf die Gesamtzahl aufgehen; ein Bericht mit offener Differenz ist unvollständig. Grund: Lauf 13 wies 470 Kandidaten aus, die Zerlegung ergibt 469.
- 8, Phase 2: Wertung Chat-Claude **10 von 11** — Zeile 7 (Vertragsprobe „→ angenommen") nicht erfüllt: das Probenpaar bestand die Vertragsprüfung, brachte aber 0 Kernmaß und kam nie ins Werk; „angenommen" wurde zu „bestanden" umgedeutet. Zeile präzisiert (Probe mit Kernmaßgewinn), Nachprobe als Vorbedingung von Phase 3. Zeile 9 erfüllt wie geschrieben, aber von Chat-Claude falsch geschrieben — der gemeinte Nachweis (Schwarm bringt selbst eine Vertragsänderung durch) steht in Tor 4.
- 8, Phase 3: Tor 3 überarbeitet — zweites Übungswerk für das Artgedächtnis; Geschmacksgedächtnis mechanisch mit versiegelter Regel geprüft (Philipps echte Entscheidungen erst ab Phase 4); Oberfläche als Web-Oberfläche mit Anmeldung; Sättigungsmeldung am gesättigten `lagerhaus` messbar; Budget 15 €.
- 6: Phase 2 gemessen 1,91 € (Schätzung 2–8 € war zu hoch); Phase-3-Schätzung.

**Änderungen gegenüber Fassung 2** (aus der Prüfung des Abschlussordners Phase 1 Nachlauf, Läufe 6–10):
- 3.5: Pareto **je Test** statt je Zahl — ein Test, der an der Vorgeneration besteht und am Kandidaten fällt, tötet den Kandidaten unabhängig von jeder Summe. Grund: Lauf 7 nahm einen Kandidaten an, der eine Behebung rückgängig machte, weil drei neue Tests eine Regression aufwogen. Fehler von Chat-Claude in Fassung 2 (dort als Summe formuliert).
- 3.5: Grenzmaß „größte Funktion" absolut (Vorgabe 60 Zeilen) statt relativ +25 %. Grund: 11 von 35 Ablehnungen in Lauf 9 trafen Kandidaten, die zwei Zeilen Fehlerprüfung ergänzten. Fehler von Chat-Claude in Fassung 2.
- 3.7: Ein Angriffstest zählt als Nachweis einer Behebung nur, wenn die Vorgeneration dabei abstürzt oder Vertrag/Verfassung ihr Verhalten als falsch ausweisen; sonst bleibt er offen und bringt 0. Grund: Lauf 7, zweite Ursache — Ankläger-Tests schrieben das Fehlverhalten des Kandidaten als Norm fest.
- 3.10: Ins Werk kommen nur Immuntests, die der angenommene Kandidat besteht; offene Funde bleiben im Immunsystem und werden späteren Kandidaten paarweise vorgelegt. Grund: Lauf 6 endete mit 19 von 95 Tests rot. Dazu Doppelungsregel.
- 3.5: Verlaufskurve mit Endtestbestand ist Pflichtbestandteil jedes Abschlussordners, nicht nur für Lauf 2.
- 6: Nachlauf gemessen 1,79 € (542 Aufrufe); schwere Ankläger-Aufrufe 5 % der Aufrufe, 36 % der Kosten.
- 8, Phase 1: **bestanden, 9 von 9** (Lauf 9, 19.09.2026, 02:20). Phase 2 freigegeben; Tor 2 um Regressionsprobe, Norm-Probe, S2 und Doppelungsanteil ergänzt; Budget 10 €.
- 10: Hermes prüft vor Phase 2 den OpenRouter-Katalog auf aktuellere Schnellmodelle gleicher Hersteller zu gleichem oder niedrigerem Preis (Vorentscheidung Chat-Claude; die in Phase 1 genutzten Modelle stammen aus 2025).

**Änderungen gegenüber Fassung 1** (aus der Prüfung des Abschlussordners Phase 1, Lauf 2):
- 3.5: Kernmaß-Formel festgelegt — bestandene Tests zählen nicht, nur Fehlschläge zählen negativ, paarweise Messung; Grenzmaße statt Punkte für Leistung; „behoben heißt verschwunden" für Sicherheitsbefunde. Grund: In Lauf 2 stammten 10 von 12 Punkten Zuwachs aus hinzugefügten Tests, und eine Scheinlösung (`__builtins__` leeren vor `eval`) wurde als Behebung angenommen.
- 3.3: Verfassung auch für Übungswerke; Verfassung des Übungswerks `lagerhaus` im Anhang A.
- 3.6: Neuschreibungsregel für kleine Dateien gelockert (Kandidat K35 wurde zu Unrecht verworfen).
- 3.7: Ankläger erhält bei Sicherheitsbefunden die Befundklasse und muss deren bekannte Umgehungen angreifen.
- 4: Vollmacht für Übungswerke (Freigaben durch Hermes mit Protokoll; echte Werke nur durch Philipp).
- 6: Kostenschätzung korrigiert — gemessen 0,40 € statt geschätzt 20–60 € für das Übungswerk.
- 8, Phase 1: Tor-Zeile 2 präzisiert; Nachlauf (Lauf 3) als Bedingung für Phase 2 aufgenommen. Wertung Lauf 2 durch Chat-Claude: 7 von 9 Zeilen, nicht 8 von 9 — S1 nicht behoben.

---

## 0. Auftrag in drei Sätzen

Baue ein System, in das man ein Software-Werk hineinlegt (Quelltext beliebiger Art, als ZIP, Git-Adresse oder Ordner) und das dieses Werk in Generationen auf ein messbar höheres Niveau hebt — jeden Bereich einzeln, das Ganze stimmig. Nicht die KI entscheidet, ob etwas besser ist, sondern die Messung; die KI erzeugt Vorschläge, die Messung wählt aus. Das System verändert seinen eigenen Code niemals während es läuft; es hebt ausschließlich Werke, die Philipp hineinlegt.

---

## 1. Das Bild

Kein Werkzeug, sondern ein **Biotop**. Ein Werk wird hineingelegt und lebt dort: Es wird kartiert, bekommt eine Verfassung, wächst in Generationen, wird von einem Ankläger geprüft, kann jederzeit in einen früheren Zustand zurückkehren, erinnert sich an alles, was versucht wurde, und wird mit jedem Werk besser darin, das nächste zu heben.

Der Vorgänger dieses Vorhabens (das Projekt `infinite-evolution-ai` vom März 2026) hatte diese Begriffswelt bereits — Aegis, Genesis, Nexus, Schwarm, neuronales Gedächtnis, Lazarus, Entropie —, aber nur als Namen. Dieses Dokument gibt jedem Begriff eine Aufgabe, einen Eingang, einen Ausgang und eine Regel. Kein Begriff steht in der Oberfläche, hinter dem keine Wirkung liegt.

---

## 2. Die Verfassung des Biotops — unverhandelbar

Diese elf Sätze gelten für jede Zeile Code, die Hermes schreibt. Verstößt ein Bauteil gegen einen davon, ist das Bauteil falsch, nicht der Satz.

1. **Die Messung entscheidet, nie die KI.** Kein Modell beurteilt, ob sein eigener oder ein fremder Vorschlag besser ist. Es erzeugt, die Messung wählt.
2. **Das Maß steht vor der ersten Generation fest und wird danach nicht verhandelt.** Änderung nur durch Philipp, und dann beginnt ein neuer Lauf. Das gilt für das Messgerät ebenso (Fassung 4): Jede Änderung an Messskripten, Ankläger-Ablauf, Pareto-, Grenz- oder Nischenregeln während eines Laufs beendet diesen Lauf und beginnt einen neuen vom selben Ausgang — ohne Ermessen des Ausführenden darüber, ob die Änderung „Maßwirkung" hatte.
3. **Kein Bereich verbessert sich auf Kosten eines anderen.** Steigt A und fällt B, ist die Generation abgelehnt (Pareto-Regel).
4. **Das laufende Biotop verändert seinen eigenen Code nie.** Soll es sich selbst heben, wird eine Kopie als Werk eingelegt; Philipp entscheidet, ob die gehobene Kopie das neue Werkzeug wird.
5. **Jede angenommene Generation ist ein vollständiger, rückholbarer Schnappschuss** (Lazarus). Es gibt keinen Vorschlag, der das Werk unwiederbringlich verändert.
6. **Laut scheitern, nie still.** Eine Prüfung ohne Gegenstand (kein Test, keine Messung, kein Werk) meldet das und stoppt, statt zu bestehen.
7. **Jeder gefundene Fehler wird zu einem Test** (Immunisierung). Derselbe Fehler kann das Werk nie zweimal treffen.
8. **Die Kasse ist Teil des Kerns.** Ein Budget je Lauf, vor dem Start gesetzt; bei Erreichen Abbruch mit Meldung vor dem nächsten Modellaufruf — nie danach.
9. **Alle Gedächtnisse liegen dauerhaft auf dem Server**, nie im Arbeitsspeicher, und sie werden gelesen, nicht nur beschrieben.
10. **Kein Schalter, kein Wert, keine Phase in der Oberfläche ohne Wirkung dahinter.** Für jedes Bedienelement muss Hermes die Codestelle belegen, die es liest.
11. **Ethische Grenze:** Das Biotop hebt kein Werk, das schädlichen Zwecken dient (Rüstung, Kriegsgerät, Überwachung von Menschen, Betrug). Diese Prüfung ist Teil der Aufnahme und wird nicht vom Werk selbst beantwortet.

---

## 2a. Neun Grundsätze (Fassung 6, erweitert in Fassung 7)

Diese Sätze sind aus Fehlern gefasst, die in Phase 1 bis 3 mehrfach an verschiedenen Stellen auftraten. Sie stehen vor den Organen, weil jeder von ihnen an mehr als einem Organ greift; wer ein neues Organ baut, prüft es gegen diese neun.

1. **Ein fallender Test beweist eine Abweichung, nie ihre Richtung** — welche Seite recht hat, entscheidet nur ein Absturz oder ein Vertrag. (Lauf 16: Fallen am Kandidaten machte aus einem Normtest einen Fund. Nachlauf: Fallen am Ausgang hätte dasselbe getan, 9 von 20.)
2. **Für jede Pflicht muss es einen benannten Befehl geben.** Eine Pflicht, die nur über Notbehelfe erreichbar ist, wird entweder blockiert oder umgeht den Schutz. (Der Abbruch nach Satz 2 war nicht vom Gate gesperrt — es gab ihn schlicht nicht.)
3. **Streuung wird immer zwischen Messungen gebildet, nie innerhalb einer.** Der Median glättet innerhalb, die Streuung misst zwischen; wer beides auf derselben Ebene bildet, misst die Glättung statt der Sache. Gilt für jede Kennzahl über wiederholte Messungen.
4. **Eine Prüfung darf den geprüften Bestand nicht verändern.** Ihr Wirkungsbereich wird vorher eingegrenzt; was sie hinterlässt, wird vor der nächsten Messung zurückgenommen und protokolliert. (Probenabfall in den Gedächtnissen; eine Mechanikprüfung archivierte zwei echte Normtests mit.)
5. **Eine Nachrechnung muss dieselbe Ableitung verwenden wie das geprüfte Organ**, sonst misst sie etwas anderes und erzeugt eine Scheindifferenz. (Drei strittige Projektgedächtnis-Fälle, alle drei aus der Ableitung, keiner aus der Sache.)
6. **Prüfe die Sache, nicht ihre Erscheinung:** Behauptung statt Fundstelle, gesetztes Merkmal statt Name, Verfassung statt Vertragsgröße, Syntaxbaum statt Textanker. (Doppelungserkennung, Probenerkennung, Eichgegenstand, Eichproben — vier Organe, dieselbe Fehlerklasse.)
7. **Ein Nachweis zählt nur, wenn er ausgeführt wurde.** Übersprungen, abgebrochen, leer oder fehlend gilt als rot, nie als grün. (Die Norm-Eichprobe war wegen eines Feldnamens leer und meldete grün; ein Vertragszeuge galt als bestanden, weil sein Test übersprungen wurde; ein Review galt als erledigt, obwohl es ohne Urteil abbrach.)
8. **Jede Probe braucht eine Gegenprobe, die fehlschlagen muss.** Eine Prüfung, die nur bestehen kann, prüft nichts. Schlägt die Gegenprobe nicht fehl, ist die Probe kaputt, nicht das Werk — und die Gegenprobe muss an der vorgesehenen Zusicherung scheitern, nicht an einem Import- oder Infrastrukturfehler.
9. **Der Prüfaufwand muss zum Gegenstand passen.** Ab einem Punkt erzeugt jede zusätzliche Prüfebene mehr Fehler, als sie findet. (Zwei Reparaturrunden mit zwei Reviews, Fixagenten und Audits der Audits scheiterten; die dritte mit einem Reviewdurchgang gelang — der Unterschied war weniger Aufwand, nicht mehr. Der Abschlussordner fiel dabei von 2.450 auf 21 Dateien.)

Belegregeln für alle Berichte von Hermes: messen statt annehmen; „bestätigt durch Ausführung" nur mit beigefügter Ausgabe, sonst „gelesen, nicht ausgeführt"; jede Zahl mit Bezugsgröße (nicht „alle Tests grün", sondern „184 von 184"); Abgelesenes von Erwartetem unterscheiden; eigene Entscheidungen als eigene kennzeichnen.

---

## 3. Die Organe

Jedes Organ ist ein eigenes Modul mit klarer Schnittstelle. Reihenfolge entspricht dem Weg eines Werks durch das Biotop.

### 3.1 Aufnahme
**Aufgabe:** Ein Werk entgegennehmen (ZIP, Git-Adresse, Ordner), entpacken, Sprache(n) und Bauwerkzeuge erkennen, Abhängigkeiten installieren, prüfen, ob es baut und ob Tests vorhanden sind.
**Ausgang:** Aufnahmebericht mit Zahlen: Dateien, Zeilen je Sprache, Bereiche (erste Schätzung), Testdateien, Ergebnis des ersten Testlaufs (x von y bestanden), Ergebnis der ethischen Prüfung.
**Regel:** Ohne Tests oder ohne bauenden Zustand startet keine Generation; das Biotop meldet „Messgerät fehlt" und schlägt vor, mit Generation 0 (siehe 3.5) zu beginnen. Kein Fremdcode wird außerhalb der Ausführungskammer (3.13) ausgeführt.

### 3.2 Landkarte
**Aufgabe:** Das Werk in Zoomstufen kartieren, damit das Biotop das Ganze sieht, ohne alles auf einmal lesen zu müssen.
- Stufe 0: das Werk in einem Absatz.
- Stufe 1: die Bereiche (Module, Dienste, Schichten), je ein Absatz.
- Stufe 2: die Dateien je Bereich, je ein Satz.
- Stufe 3: die Funktionen, Signatur und Zweck.
- **Straßen:** Wer ruft wen? Wer hängt von wem ab? Als gerichteter Graph.
- **Verträge:** An jeder Grenze zwischen zwei Bereichen die Zusicherungen (Eingaben, Ausgaben, Nebenwirkungen, was sich nie ohne Absprache ändert). Wo das Werk keine expliziten Verträge hat, leitet die Landkarte sie aus dem Code ab und kennzeichnet sie als abgeleitet.
**Technik:** Syntaxbäume (z. B. tree-sitter) für Struktur und Aufrufe; Zusammenfassungen je Stufe durch ein Modell, in der Datenbank gespeichert, mit Prüfsumme der Quelldatei, damit veraltete Zusammenfassungen erkannt werden. Der bestehende Aktenschrank (Chunking + Stichwort- und Bedeutungssuche) wird Teil der Landkarte.
**Regel:** Die Landkarte ist die einzige Sicht des Schwarms auf das Werk. Ein Schwarm-Aufruf bekommt nie „das ganze Werk", sondern Stufe 0 + Stufe 1 + den Bereich, an dem er arbeitet, auf Stufe 3 + die Verträge an dessen Grenzen.

### 3.3 Verfassung des Werks
**Aufgabe:** Vor der ersten Veränderung mit Philipp festlegen: Was ist dieses Werk? Wofür ist es da? Für wen? Was darf nie passieren?
**Ablauf:** Das Biotop schlägt aus Landkarte und Aufnahmebericht einen Entwurf vor (5–15 Sätze). Philipp streicht, ergänzt, bestätigt. Erst dann ist sie gültig.
**Regel:** Jeder Vorschlag aus jedem Bereich wird gegen die Verfassung geprüft (durch den Ankläger, 3.7). Die Verfassung ändert nur Philipp.
**Übungswerke:** Auch ein Übungswerk hat eine Verfassung — ohne sie kann das Biotop nicht wissen, ob Sicherheit vor Geschwindigkeit geht (Lauf 2 hat genau daran einen richtigen Kandidaten verworfen). Für Übungswerke schreibt Chat-Claude die Verfassung; Philipp hat die Entscheidung delegiert. Die Verfassung des Übungswerks `lagerhaus` steht in Anhang A.
**Tauschregeln:** Eine Verfassung darf festlegen, was gegen was getauscht werden darf — z. B. „Laufzeit darf bis ×5 steigen, wenn dabei ein Sicherheitsbefund verschwindet". Ohne Tauschregel gelten die Vorgaben aus 3.5.

### 3.4 Mentor
**Aufgabe:** Die Richtung setzen, bevor gearbeitet wird. Nicht „was ist kaputt", sondern „was könnte dieses Werk werden".
**Ausgang:** 3–5 Entwicklungsrichtungen, je mit: Ertrag (welches Maß würde steigen), Risiko (welche Verträge und Bereiche werden berührt), Aufwandsschätzung in Generationen, und den Erfahrungen aus dem Artgedächtnis (3.12) zu ähnlichen Werken.
**Regel:** Philipp wählt die Richtung. Das Biotop kann eine Empfehlung mit Begründung geben, wählt aber nicht selbst. Jede Richtung wird als eigener Lauf mit eigenem Maß geführt.

### 3.5 Maß und Messgerät
**Aufgabe:** Festlegen, was „besser" heißt — und sicherstellen, dass das Messgerät das auch erkennt.
**Zwei Schichten:**
- **Harte Maße** entscheiden allein und automatisch. Sie zerfallen in drei Sorten:
  - **Kernmaß je Bereich** (Fassung 2; gilt für alle Werke ohne eigenes Klassenmaß): `−(fehlgeschlagene Tests) − 10·(Sicherheitsbefunde HIGH) − 3·(MEDIUM) − 1·(LOW) − (tote Funktionen)`. Höchstwert ist 0. **Bestandene Tests zählen nicht.** Ein Kandidat, der Tests hinzufügt, die überall bestehen, bringt 0 und wird als „unverändert" abgelehnt. Ein Immuntest, der einen echten Fehler beweist, schlägt an der Vorgeneration fehl und besteht am Kandidaten — die Behebung bringt +1, nicht der Test.
  - **Paarweise Messung:** Vorgeneration und Kandidat werden mit demselben Testbestand gemessen — dem des Kandidaten (einschließlich neuer Immuntests). Zuwachs ist die Differenz. Die Verlaufskurve eines Laufs wird am Laufende mit dem Endbestand aller Tests neu gerechnet, damit Generation 0 rückwirkend mit denselben Augen gesehen wird wie die letzte.
  - **Pareto-Maße** (dürfen im Wirkungskreis nie schlechter werden, sonst ist der Kandidat tot): Sicherheitspunkte, tote Funktionen, Bauen, Verträge — und **Tests je Test, nicht als Summe** (Fassung 3): Jeder einzelne Test, der an der Vorgeneration besteht und am Kandidaten fällt, ist eine Regression und tötet den Kandidaten, unabhängig davon, wie viele andere Fehlschläge er beseitigt oder wie viele neue Tests er mitbringt. Die Summe der Fehlschläge ist nur noch das Kernmaß, nie das Pareto-Kriterium.
  - **Grenzmaße** (keine Punkte; darüber ist der Kandidat tot): Laufzeit auf Referenzlast, Speicher, Bauzeit, größte Funktion, Zyklen. **Bezug ist der Bestwert des Laufs** (Fassung 4): je Maß und Bereich der beste Wert aller bisher angenommenen Generationen einschließlich Ausgang — nicht der Ausgang allein, sonst darf ein Kandidat einen früheren Gewinn wieder aufbrauchen. Regel: Ohne Kernmaßgewinn darf ein Kandidat kein Grenzmaß über Bestwert + Rauschtoleranz verschlechtern. **Die Rauschtoleranz wird gemessen, nicht gesetzt (Fassung 5):** Vor jedem Lauf misst das Biotop jedes Grenzmaß fünfmal am unveränderten Ausgang je Bereich; die Toleranz ist die gemessene Spannweite plus 10 Prozentpunkte, mindestens 15 %. Laufzeiten werden grundsätzlich als Median aus drei Durchläufen gemessen, nie als Einzelwert. Grund: Bei `formeln` betrug das Eigenrauschen 47 % gegen eine feste Toleranz von 15 % — Kandidaten starben am Messrauschen statt an Verschlechterung; bei `bericht` (7 % Rauschen) arbeitete dieselbe Grenze korrekt. Mit Kernmaßgewinn gilt die Tauschregel der Verfassung des Werks; Vorgabe ohne Angabe: Laufzeit bis ×2 des Bestwerts, Speicher/Bauzeit/Zyklen bis +25 %. **Größte Funktion absolut 60 Zeilen** (Fassung 3) — die relative Grenze +25 % gilt nur für Funktionen, die schon oberhalb von 60 Zeilen liegen. Leistung ist damit eine Grenze, kein Punkt — Geschwindigkeit kann Sicherheit nie aufwiegen, und Korrektheit kann Geschwindigkeit nur im Rahmen der Tauschregel kaufen.
  - **Verlaufskurve** (Fassung 3): Für jeden Lauf wird am Laufende jede angenommene Generation aus Lazarus geholt, mit dem Endtestbestand gemessen und als Kurve (Kernmaß je Generation, Zerlegung nach Fehlschlägen / Sicherheit / toten Funktionen) dem Abschlussordner beigefügt. Ohne Kurve ist ein Abschlussordner unvollständig.
  - **Nischenmaß:** Die Nische *Der Schnelle* wird an der Laufzeit gemessen; ihre Kandidaten werden nur angenommen, wenn das Kernmaß dabei gleich bleibt oder steigt.
  - **Klassenmaß:** Je Werkklasse kann die Verfassung ein Kernmaß setzen, das das obige ersetzt oder ergänzt (Beispiel: bei einem Werk, dessen Zweck eine messbare Zielgröße hat, tritt diese an die Stelle der Fehlschlagszählung).
  - **Behoben heißt verschwunden:** Eine Sicherheitsschwäche gilt erst als behoben, wenn der statische Befund verschwunden ist und die für diese Befundklasse bekannte Umgehung als Immuntest im Werk liegt. Ein Kandidat, der einen Befund entschärft, ohne ihn zu entfernen, kann angenommen werden, wenn er Fehlschläge beseitigt — die Schwäche zählt trotzdem als offen.
- **Weiche Maße** (Lesbarkeit, Eleganz, Nutzererlebnis) bewertet eine Jury aus mindestens drei Modellen verschiedener Anbieter mit Begründung — **nur** zwischen Kandidaten, die alle harten Maße bereits bestehen, und nur bei Einstimmigkeit. Weiche Maße beweisen nichts; sie brechen Gleichstände.
**Generation minus eins — das Messgerät eichen (Fassung 5, ausgebaut in Fassung 6):** Vor Generation 0 prüft das Biotop sich selbst. Fünf Teile, in dieser Reihenfolge:

1. **Rauschmessung je Bereich.** Fünf Messungen am unveränderten Ausgang, jede selbst ein Median aus drei Durchläufen (Grundsatz 3: die Streuung wird zwischen den fünf Messungen gebildet, nie innerhalb einer). Höchst- und Tiefstwert werden gestrichen, die Spannweite aus den mittleren drei gebildet, Toleranz = Spannweite + 10 Prozentpunkte, mindestens 15 %, **gedeckelt bei Faktor 2,0**. Ein Einzelwert über dem Fünffachen des Medians ist ein Maschinenaussetzer: verworfen, einmal nachgemessen, protokolliert. Getrimmt wird ab drei Werten, immer.
2. **Bereichsweise Sperre.** Bleibt die Toleranz eines Bereichs über 1,5, meldet das Biotop ein Messproblem und **überspringt diesen Bereich** — keine Kandidaten, Sperre mit Zahl im Bericht. Melden alle Bereiche ein Problem, startet der Lauf nicht. Ein gesperrter Bereich wird vor jedem weiteren Lauf neu gemessen. **Serienzähler:** Meldet derselbe Bereich dreimal, deutet der Befund je nach Zeitraum — drei Meldungen in einer Sitzung auf die Maschine, drei an verschiedenen Tagen auf die Referenzlast. Bei Deutung „Maschine" gilt der Vorbehalt für **alle** Laufzeit- und Grenzmaßzahlen dieses Zeitraums, auch die der nicht gesperrten Bereiche; er steht als eigene Berichtszeile und als Feld an der Messung.
3. **Die vier Proben am versiegelten Eichgegenstand** (siehe unten): Nebenwirkung, Regression, Norm, Vertrag. Besteht eine nicht, beginnt kein Lauf; der reparierte Stand ist ein neuer Lauf nach Satz 2.
4. **Fund-Neubewertung** aller übernommenen offenen Funde (3.10).
5. **Eichkosten getrennt ausweisen**, Kammerläufe und Modellaufrufe je Teil, nie in der Laufsumme. Gemessen an vier Bereichen: 9 Kammerläufe, 4 Modellaufrufe, 0,0057 €, 44 s. Die **Zahl** der Kammerläufe hängt nicht an der Bereichszahl — alle Bereiche werden zusammen gemessen; mit mehr Diensten wächst die Dauer, nicht die Zahl. Eine Hochrechnung auf ein größeres Werk ist eine erfundene Zahl; sie wird dort gemessen.

**Versiegelter Eichgegenstand (Fassung 6):** Jede Probe braucht einen Gegenstand — ein Bereichspaar mit Vertrag. Er wird **je Werk einmal gewählt und versiegelt**, beim ersten Lauf, mit Prüfsumme und Begründung; danach unverändert, damit jede Eichung mit jeder vergleichbar ist. Rangfolge der Wahl: **tragender Pfad der Verfassung, dann Vertragsgröße, dann alphabetisch** — denn eine Eichung an einem Nebenpfad übersieht Messgerätfehler im Kern. Bei Werken mit Betriebszweck muss der tragende Pfad **ausdrücklich in den Regeln des Werks stehen**; fehlt er, meldet das Organ das und wartet, statt ihn aus dem Verfassungstext abzuleiten (eine Wortstatistik findet, was oft zusammen genannt wird, nicht was trägt). Die Textableitung ist nur für Übungswerke zulässig. Fällt der Gegenstand durch eine Änderung des Werks weg, ist das ein Befund mit beiden Prüfsummen im Klartext und ein neuer versiegelter Gegenstand, protokolliert — nie ein stiller Wechsel. Gibt es kein Bereichspaar mit Vertrag, meldet das Organ das, statt still zu bestehen.

**Die Proben setzen mechanisch am Syntaxbaum an, nicht an Textankern** (Grundsatz 6) — sonst zielen sie nach jeder angenommenen Generation stillschweigend woanders hin, was in Phase 2 und 3 geschah und dort vier Torzeilen entwertet hat. Ihre Prüfbedingungen müssen den Grund des Bestehens prüfen, nicht nur das Bestehen: Im ersten Durchlauf standen vier „bestanden", drei davon aus falschen Gründen.

**Generation 0 — das Messgerät schärfen:** Bevor das Werk verbessert wird, prüft das Biotop, ob die Tests Fehler überhaupt bemerken. Es erzeugt Mutanten (eine Bedingung umgedreht, eine Grenze um eins verschoben, ein Rückgabewert vertauscht) und lässt die Tests laufen. Jeder Mutant, den kein Test fängt, ist ein blinder Fleck. Generation 0 evolutioniert dann die Tests, bis mindestens 80 von 100 Mutanten gefangen werden. Erst danach beginnt Generation 1.
**Äquivalente Mutanten (Fassung 4):** Ein Mutant, der das beobachtbare Verhalten nicht ändert, kann von keinem Test gefangen werden und zählt nicht. Äquivalenz wird **vor** der Zählung geprüft und belegt — Ausgabe auf der Referenzlast und auf allen vorhandenen Tests identisch, dazu eine Begründung am Code — nie nachträglich erklärt, um eine Quote zu erreichen. Die Bezugsgröße lautet „gefangen: x von n nicht-äquivalenten"; die aussortierten werden mit Beleg gelistet. Der Testbau ist stochastisch: je blindem Mutanten zwei Durchläufe, bevor er als ungefangen gilt.
**Regel:** Das Biotop schlägt das Maß vor, Philipp bestätigt, danach ist es eingefroren (Verfassungssatz 2). Das Messgerät selbst (Testläufer, Messskripte) liegt im unantastbaren Kern und wird nie vom Schwarm verändert — die Tests des Werks dagegen dürfen in Generation 0 evolutioniert werden, weil sie Teil des Werks sind.

### 3.6 Genesis — der Schwarm in Nischen
**Aufgabe:** Kandidaten erzeugen. Viele, verschieden, auch unerwartete.
**Nischen (mindestens vier, erweiterbar):**
- *Der Sichere* — Temperatur niedrig, Auftrag: Fehler beseitigen, Verträge härten, nichts Neues wagen.
- *Der Schnelle* — Auftrag: Laufzeit und Speicher.
- *Der Elegante* — Auftrag: weniger Code bei gleicher Funktion, klarere Struktur.
- *Der Wilde* — Temperatur hoch, Auftrag: Vorschläge, die niemand erwartet; darf Verträge in Frage stellen (der Ankläger fängt ihn).
Jede Nische hält ihre besten Kandidaten über Generationen hinweg am Leben, auch wenn eine andere Nische gerade vorn liegt (Population in Nischen nach dem MAP-Elites-Prinzip; Begründung: der am Ende beste Weg verläuft fast nie gerade).
**Modelle:** Mindestens zwei verschiedene Anbieter je Nische, weil verschiedene Modelle verschiedene blinde Flecken haben. Masse über tokenabgerechnete Schnellmodelle (siehe Abschnitt 6), Durchbrüche über schwere Modelle. Das Biotop führt Buch, welches Modell in welcher Nische bei welcher Werkklasse angenommene Kandidaten liefert, und gewichtet danach (Bandit-Verfahren). **Ausfall ist kein Beitrag (Fassung 7):** Fällt ein Modell des Verbunds aus — Ablehnung durch den Anbieter, Zeitüberschreitung, leere Antwort —, zählt das als Ausfall und nie als Beitrag, auch nicht bei HTTP 200 oder bei erfolgreicher Antwort der übrigen Mitglieder. Protokollabschluss und nutzbarer Beitrag sind zu trennen. Belegt ist dieses Verhalten noch nicht; es hat deshalb eine eigene Torzeile in Phase 4. Anlass: Ein Verbundmitglied lehnte eine große Code-Eingabe mit `stop_reason: refusal`, Kategorie `cyber`, ab und lieferte null Ausgabetokens bei HTTP 200. Bei großen Werken mit Netzwerk-, Schlüssel- oder Authentifizierungscode ist damit zu rechnen; der Verbund muss einen Ausfall tragen, ohne ihn zu verdecken.
**„KEIN VORSCHLAG" ist neutral (Fassung 4):** Eine Antwort, die ehrlich keinen Kandidaten liefert, wird weder als Erfolg noch als Misserfolg gebucht und zählt nicht als Wahl. Ein Modell darf nie dafür bestraft werden, dass es nichts erfindet.
**Ausgang:** Kandidaten als Änderungssätze (Diffs); jeder mit Begründung und der Angabe, welche Verträge er berührt. Ein Hunk über 60 % einer Datei gilt als Neuschreibung und wird abgelehnt — **außer** die Datei hat unter 100 Zeilen und alle Verträge an ihren Grenzen bleiben unverletzt; dann ist die Neuschreibung ein zulässiger Kandidat (Fassung 2; in Lauf 2 wurde ein sauberer Sicherheits-Kandidat an einer 68-Zeilen-Datei so verworfen).

### 3.7 Aegis — der Ankläger
**Aufgabe:** Jeden Kandidaten zu Fall bringen. Kein Berater, ein Gegner.
**Ablauf je Kandidat:**
1. Wirkungskreis bestimmen: alle Bereiche, die der Änderungssatz direkt oder über die Straßen der Landkarte berührt.
2. Verträge prüfen: Verletzt der Kandidat eine Zusicherung an einer Grenze?
3. Verfassung prüfen: Verstößt er gegen einen Satz der Werk-Verfassung?
4. Angriff: Ein Modell mit dem einzigen Auftrag, den Fehler, den Grenzfall, die Nebenwirkung zu finden — es wird nach gefundenen, durch Ausführung bestätigten Fehlern bewertet, nicht nach Bedenken. **Sicherheitsbefunde (Fassung 2):** Berührt der Kandidat eine Stelle mit statischem Sicherheitsbefund, erhält der Ankläger die Befundklasse (z. B. Bandit-Kennung mit Beschreibung) und muss die für diese Klasse bekannten Umgehungen als Angriffstests liefern — bei `eval`/`exec` also die Erreichbarkeit von Objektklassen über Introspektion, nicht nur den naiven Aufruf. Ein Kandidat, dessen „Behebung" einen dieser Angriffe nicht besteht, hat den Befund nicht behoben (3.5). Der Ankläger findet nur, was sein Modell kennt; deshalb wird der Angriff bei Sicherheitsbefunden mit einem schweren Modell gefahren, nicht mit einem Schnellmodell.
5. Ausführung in der Kammer: Bauen, alle Tests, alle harten Maße — für den geänderten Bereich **und** für jeden Bereich im Wirkungskreis.
**Regel:** Ein Kandidat, der irgendwo im Wirkungskreis ein hartes Maß senkt, ist tot. Ein vom Ankläger gefundener Fehler wird sofort zu einem Test (Immunisierung, 3.10) — auch wenn der Kandidat ohnehin verworfen wird.
**Der Ankläger nennt seine Behauptung vorab (Fassung 6):** Vor jedem Angriff gibt der Ankläger an, welche Behauptung er prüfen will (Ziel-Funktion plus Zusicherungsart, 3.10). Ist sie in diesem Bereich schon aufgestellt, wird der Angriff **gar nicht erst ausgeführt** — kein Testschreiben, kein Kammerlauf, kein Modellaufruf für die Ausführung. Ihm werden dazu seine bisherigen Behauptungen des Bereichs vorgelegt. Grund: Die bloße Anweisung, eine andere zu finden, senkte die größte Gruppe gleicher Behauptungen von 5 auf 1, aber den Doppelungsanteil nur von 63,6 auf 54,5 % — und **0 von allen Aufrufen** antworteten mit „KEIN ANGRIFF", obwohl die Anweisung das ausdrücklich erlaubt und beim Schwarm über 40 % der Aufrufe ehrlich nichts liefern. Die Rolle des Gegners erzeugt Zwangsbefunde; deshalb wird dem Modell die Entscheidung abgenommen, statt sie ihm anzutragen.

**Angriffstests sind keine Verträge (Fassung 3, erweitert in Fassung 4):** Ein Test, der an der Vorgeneration fällt und am Kandidaten besteht, gilt nur dann als Nachweis einer Behebung (+1 im Kernmaß), wenn mindestens eines zutrifft: (a) die Vorgeneration stürzt bei diesem Test mit einer Ausnahme im Werk ab; (b) ein Vertrag oder ein Satz der Werk-Verfassung weist das Verhalten der Vorgeneration als falsch aus, und der Test verweist auf diesen Vertrag oder Satz **durch explizite Kennung** (Vertragstest-Name oder Verfassungssatz-Nummer im Testnamen oder Docstring) — Wortüberdeckung mit einem Vertragstext genügt nicht, weil sie sich durch Vokabular erzeugen lässt. Trifft keines zu, kodiert der Test eine Meinung über das gewünschte Verhalten; er bleibt als „offen" im Immunsystem, bringt 0 und kommt nicht ins Werk. **Das gilt für jeden Test, der mit einem Kandidaten neu ins Spiel kommt** — Ankläger-Tests ebenso wie vom Kandidaten mitgebrachte Tests (Fassung 4; die Lücke bei mitgebrachten Tests zeigte Lauf 12). Grund: In Lauf 7 schrieben Angriffstests das Fehlverhalten eines Kandidaten als Norm fest und brachten ihm Punkte dafür. Das Werk ist gegen den Ankläger zu schützen, nicht nur gegen den Schwarm.

### 3.8 Nexus — die Generalprobe
**Aufgabe:** Das Ganze stimmig halten, während Bereiche einzeln wachsen.
**Ablauf einer Generation:**
1. Alle Bereiche wachsen gleichzeitig, jeder mit eigenem Schwarm, alle in der vom Mentor gesetzten Richtung.
2. Will ein Bereich eine Grenze (einen Vertrag) zum Nachbarn ändern, wird der Nachbar gefragt: Sein Schwarm erzeugt die Anpassung seiner Seite, der Ankläger prüft beide zusammen. Ohne bestandene Anpassung des Nachbarn keine Vertragsänderung.
3. Die je Bereich überlebenden Kandidaten werden zu einem Gesamtkandidaten zusammengesetzt.
4. Generalprobe: Bauen, alle Tests des ganzen Werks, alle harten Maße auf Werkebene, Verfassung, alle Verträge.
5. Pareto-Prüfung: Kein Maß irgendeines Bereichs darf gegenüber der letzten angenommenen Generation gesunken sein.
6. Bei Bestehen: Schnappschuss (Lazarus), Vorlage an Philipp zur Freigabe.
**Regel:** Eine Generation wird als Ganzes angenommen oder als Ganzes abgelehnt. Bei Ablehnung gehen die Erkenntnisse (welche Kombination scheiterte, warum) ins Projektgedächtnis, und die Generation wird mit diesem Wissen wiederholt — höchstens dreimal, dann Meldung an Philipp.

### 3.9 Lazarus
**Aufgabe:** Jede angenommene Generation ist ein vollständiger, rückholbarer Zustand.
**Technik:** Git-Tag je Generation plus Ablage des vollständigen Werks (Prüfsumme über alle Dateien) und des Maßstands. Rückkehr zu Generation n stellt Werk, Landkarte und Maß-Verlauf auf den Stand von n zurück.
**Regel:** Stellt sich in Generation n+k heraus, dass Generation n einen Fehler eingeführt hat, wird zu n-1 zurückgekehrt, der Fehler geht ins Immunsystem, und die Generationen n bis n+k werden mit dem neuen Test wiederholt. Nichts wird gelöscht; abgelehnte Linien bleiben im Archiv einsehbar.

### 3.10 Immunisierung
**Aufgabe:** Jeder Fehler — vom Ankläger gefunden, in der Generalprobe aufgetreten, von Philipp bei der Freigabe benannt — wird zu einem Test im Werk.
**Regel:** Zählung: n gefundene Fehler = n neue Tests, nachweisbar im Werk. Ein Fehler ohne zugehörigen Test ist ein Verstoß gegen Verfassungssatz 7.
**Ins Werk nur, was besteht (Fassung 3):** Ein Immuntest wird erst dann Teil des Werks, wenn der angenommene Kandidat ihn besteht. Ein Fund, den kein Kandidat besteht, bleibt als „offen" im Immunsystem, wird jedem späteren Kandidaten desselben Bereichs paarweise vorgelegt und wandert ins Werk, sobald ein angenommener Kandidat ihn besteht. Ein Werk darf nach keiner angenommenen Generation einen fehlschlagenden Test enthalten (Lauf 6 endete mit 19 von 95 rot, weil Satz 7 als „jeder Test ins Werk" umgesetzt war).
**Proben kommen in kein Gedächtnis (Fassung 6):** Probenkandidaten und ihre Ergebnisse werden von keinem der drei Gedächtnisse aufgenommen — ein eingeschleuster Regressionskandidat im Projektgedächtnis würde später echte Kandidaten sperren, ein Probenmuster im Artgedächtnis würde als Erfahrung an andere Werke weitergereicht. Die Sperre sitzt **in den Eintrittsstellen der Gedächtnisse**, nicht beim Aufrufer, und erkennt eine Probe am **gesetzten Merkmal** (`ist_probe`), das der Erzeuger beim Anlegen setzt — nicht an Nische oder Bereichsnamen (Grundsatz 6): Die Jury-Proben liefen unter eigenen Bereichsmarken und wären am Namen durchgerutscht. Name und Nische bleiben als zweiter Weg für Altbestand. Die Proben bleiben in der Datenbank und im Bericht sichtbar; nur die Gedächtnisse lesen sie nicht.

**Doppelungen (Fassung 5):** Je bestätigtem Fehler kommt ein Test ins Werk; weitere Tests, die **dieselbe Behauptung** aufstellen, sind Doppelungen und werden nicht übernommen. **Der Schlüssel ist die Behauptung — Ziel-Funktion plus Zusicherung —, nicht die Fundstelle.** Die frühere Prüfung auf (Meldungsklasse, Ort) versagt, weil jeder Test in seiner eigenen Datei eine eigene Zeile hat und damit nie „derselbe Ort" ist; sechs Tests derselben Behauptung kamen so einzeln ins Immunsystem und hielten einen Fehler am Leben. Der Doppelungsanteil wird gegen die **vom Ankläger erzeugten Tests** ausgewiesen, nicht gegen die Ablehnungen des Laufs (Bezugsgrößenfehler in Phase 2: gemeldet 2,5 %, richtig 10,9 % bei gleicher Lesart, 83,6 % bei dieser).
**Fund-Übernahme zwischen Läufen (Fassung 5):** Offene Funde werden beim Übergang in einen neuen Lauf nicht mit ihrem alten Status übernommen, sondern **mechanisch neu bewertet**: jeder Fund wird am neuen Ausgang in der Kammer ausgeführt und nach 3.7 eingestuft (fällt er, ohne Absturz und ohne Vertragsverweis? → Norm, nicht Fund). Grund: sechs Normtests standen nach einer blinden Übernahme als Funde im Testbestand und töteten jede Behebung.
**Archivierung offener Funde (Fassung 5):** Ein offener Fund, den nach fünf **Generationen** kein Kandidat besteht, wird archiviert — Bezug sind Generationen, nicht angenommene Generationen, sonst tritt der Fall an einem gesättigten Werk nie ein. Er bleibt in der Datenbank einsehbar, wird aber späteren Kandidaten nicht mehr vorgelegt und kostet keinen Kammerlauf mehr. Der Mentor (3.4) sieht das Archiv und kann daraus Richtungen ableiten.

### 3.11 Entropie — Sättigungsmeldung
**Aufgabe:** Ehrlich sagen, wenn es in einer Richtung nicht mehr weitergeht.
**Messung:** Je Generation zwei Zahlen — die Verbesserung des Kernmaßes gegenüber der Vorgeneration in Prozent, und die Verschiedenheit der Schwarmvorschläge (Anteil der Kandidaten, die sich in weniger als 10 % der geänderten Zeilen unterscheiden).
**Regel:** Bringen fünf aufeinanderfolgende Generationen zusammen weniger als 0,5 % Verbesserung des Kernmaßes, meldet das Biotop: *„In dieser Richtung gesättigt: Generationen x–y, Verbesserung z %. Weiter nur mit anderer Richtung (zurück zum Mentor) oder anderem Maß (neuer Lauf)."* Es sagt nie „perfekt". Es sagt, wo es weitergeht.

### 3.12 Die drei Gedächtnisse
Alle drei dauerhaft in der Datenbank, alle drei werden vor jeder Generation gelesen.
- **Projektgedächtnis** (je Werk): jede Generation, jeder Kandidat, jedes Ergebnis, jede Ablehnung mit Grund. Der Schwarm bekommt vor jeder Generation die Liste der gescheiterten Wege dieses Werks und den Auftrag, sie nicht zu wiederholen. **Gescheiterte Wege aus verworfenen Läufen zählen nicht (Fassung 5)** — das Projektgedächtnis verwirft Kandidaten ohne Kammerlauf und ist damit Teil des Messgeräts; ein nach Satz 2 verworfener Lauf darf keine Kandidaten sperren. Grund: Lauf 18 begründete 12 von 13 Verwerfungen mit Ablehnungen aus Lauf 16, dessen Ankläger als falsch erkannt war.
- **Artgedächtnis** (über alle Werke): **Es speichert Muster, keine Instanzen (Fassung 5).** Zu jeder angenommenen Generation schreibt ein zusätzlicher Aufruf den abstrahierten Satz — was getan wurde und warum es wirkte, **ohne Werk-, Datei- oder Funktionsnamen**: nicht „in `logmuehle` bekam `filtern()` einen Index", sondern „wiederholtes Durchsuchen durch eine mitgeführte Struktur ersetzen, wenn dieselbe Menge mehrfach gelesen wird". Nur diese Muster werden werkübergreifend vorgelegt, zusammen mit der Werkklasse, bei der sie gewirkt haben, und dem erreichten Maßgewinn; die Instanz bleibt als Beleg daneben, wird aber nicht als Vorlage gezeigt. Grund: Instanzen gelten am fremden Werk nicht, und das Modell übergeht sie zu Recht — gemessen 0 werkübergreifende Verweise bei 12 Richtungen. Der Mentor liest die Muster für seine Richtungen, der Schwarm für seine Vorschläge. Das ist die Evolution des Biotops selbst — ohne dass es seinen Code ändert. **Ein werkübergreifender Verweis wird nie erzwungen:** Ein Pflichtfeld erzeugt Scheinbegründungen, und die sind schlimmer als keine Verweise. **Stattdessen ein Mindestanteil an der Vorlage (Fassung 6):** Der werkübergreifende Block belegt mindestens die Hälfte der gezeigten Einträge, mindestens fünf, sofern so viele fremde Muster vorhanden sind. Grund: Ein `logmuehle`-Lauf sah 13 fremde Muster und lieferte 2 von 5 Richtungen mit Verweis, ein `lagerhaus`-Lauf sah 3 und lieferte 0 — die Zeile hängt also auch an der Zahl der gezeigten Muster, und bei 17 Diensten verdrängt die Masse eigener Einträge die fremden allein durch Menge. Der Anteil steuert, was gezeigt wird, nicht was zitiert werden muss.
- **Geschmacksgedächtnis** (Philipp): jede Freigabe, jede Ablehnung, jede Begründung. Ab 20 Entscheidungen wird daraus ein Vorhersagemodell, das die Jury (3.5) bei weichen Maßen ergänzt. Es ersetzt Philipp nie; es sagt vorher, was er wahrscheinlich entscheidet, und legt es ihm mit der Vorlage bei.

### 3.13 Ausführungskammer
**Aufgabe:** Jeder Bau, jeder Testlauf, jede Messung läuft in einem abgeschotteten Container (Docker): kein Netzzugang außer zu den Modellanbietern, eigenes Dateisystem je Kandidat, Zeit- und Speicherlimit, nach dem Lauf verworfen.
**Regel:** Fremdcode wird nie auf dem Wirtsystem ausgeführt. Ein Kandidat, der das Limit der Kammer reißt, gilt als gescheitert.

### 3.14 Kasse
**Aufgabe:** Jeden Modellaufruf zählen (Anbieter, Modell, Eingabe- und Ausgabetoken, Kosten nach hinterlegter Preistabelle) und gegen das Laufbudget führen.
**Regel:** Vor jedem Modellaufruf wird geprüft, ob der Aufruf das Budget überschreiten würde; wenn ja, Abbruch des Laufs mit Meldung und Abschlussordner. Der Kostenstand ist in der Oberfläche immer sichtbar. Abo-Kontingente (Modelle ohne Tokenabrechnung) werden getrennt gezählt und mit eigener Grenze geführt.

### 3.15 Oberfläche
**Aufgabe:** Philipp sieht: das Werk und seine Landkarte; die Verfassung; das eingefrorene Maß; den Verlauf aller Maße über die Generationen (als Kurven); die aktuelle Generation mit Kandidaten je Nische; die Vorlage zur Freigabe mit Diff, Maß-Vergleich, Anklägerbericht und Geschmacksvorhersage; die Entropie; die Kasse; das Archiv (Lazarus).
**Regel:** Jedes Bedienelement liest oder schreibt eine Stelle im Kern — belegt durch Hermes je Element mit Dateipfad und Zeile. Keine Phasenanzeige, die nicht dem tatsächlichen Zustand entspricht.

---

## 4. Ablauf eines Laufs

1. **Werk hineinlegen** → Aufnahmebericht, ethische Prüfung.
2. **Landkarte bauen** → Zoomstufen, Straßen, Verträge.
3. **Verfassung** → Entwurf, Philipp bestätigt.
4. **Generation 0** → Mutanten, blinde Flecken, Tests evolutionieren bis ≥ 80/100 gefangen.
5. **Maß** → Vorschlag, Philipp bestätigt, eingefroren.
6. **Mentor** → Richtungen, Philipp wählt.
7. **Generation n** → je Bereich Schwarm → Ankläger → Bereichsmaße; Nexus: Verhandlung, Zusammensetzen, Generalprobe, Pareto → Schnappschuss.
8. **Freigabe** → Philipp gibt frei oder lehnt ab; Ablehnung mit Grund → Immunisierung + Geschmacksgedächtnis.
9. **Entropie** → weiter oder Sättigungsmeldung.
10. **Abschluss** → Abschlussordner (Abschnitt 9).

Philipp gibt jede Generation frei. Vollautomatik über mehrere Generationen kommt erst, wenn das Messgerät über mindestens drei Werke ohne einen einzigen unbemerkten Rückschritt gearbeitet hat — und dann nur auf Philipps Satz.
**Vollmacht für Übungswerke (Fassung 2, erweitert in Fassung 5):** Für Werke ohne Betriebszweck, die Hermes selbst erzeugt hat, gilt eine schriftliche Vollmacht: Hermes gibt Generationen frei **und wählt die Richtung des Mentors**, protokolliert je Entscheidung die Begründung (`freigabe.frei`, `mentor.gewaehlt`, Vollmacht als Grund genannt), und Chat-Claude prüft alles am Abschlussordner. Für jedes Werk mit Betriebszweck gibt ausschließlich Philipp frei und wählt die Richtung; eine stellvertretende Freigabe dort ist ein Verstoß, kein Ermessen.

---

## 5. Der unantastbare Kern

Diese Teile darf nur Philipp ändern; kein Schwarm, kein Kandidat, keine Generation hat Schreibzugriff:
- das Messgerät (Testläufer, Messskripte, Preistabelle der Kasse)
- das eingefrorene Maß eines laufenden Laufs
- die Verfassung des Biotops (Abschnitt 2) und die Verfassung des Werks
- Lazarus (Archiv und Rückkehr)
- die Kasse und ihr Budget
- das Protokoll (jeder Aufruf, jedes Ergebnis, unveränderlich, fortlaufend nummeriert)
- der Code des Biotops selbst (Verfassungssatz 4)

Technisch: eigener Prozess, eigene Datenbank-Rolle mit ausschließlichem Schreibrecht, keine Schreibpfade aus Schwarm oder Kammer hinein.

**Abbrüche sind nie gesperrt (Fassung 5):** Ein Abbruch nach Satz 2 (Messgerätänderung) oder nach dem Budget ist eine Pflicht, keine Freigabe. Das Freigabe-Gate darf ihn nicht blockieren; er ist immer erlaubt und wird protokolliert. Grund: In Phase 3 blockierte das Gate den Versuch, einen als falsch erkannten Lauf zu stoppen — der Lauf lief weiter und kostete, bis jemand antwortete.

---

## 6. Modelle und Kosten

**Rollenverteilung (Vorgabe; Hermes verdrahtet):**
- *Masse* (Schwarm-Kandidaten, Ankläger-Angriffe, Zusammenfassungen der Landkarte): tokenabgerechnete Schnellmodelle über OpenRouter — mindestens zwei Anbieter. Nie über Abo-Kontingente, weil ein Lauf Hunderte bis Tausende Aufrufe macht und ein Wochenkontingent in Stunden leeren würde.
- *Schwere Aufrufe* (Mentor, Verfassungsentwurf, Jury-Endurteil, Anklägerbericht an Philipp): die schweren Modelle des bestehenden Teams, gezählt gegen eine eigene Kontingentgrenze in der Kasse.
- Die Anbieterschicht ist austauschbar (ein Port, mehrere Adapter), wie im Vorgängerprojekt bereits angelegt.

**Kostenschätzung** (Schätzung; Bezugsgröße: ein Lauf mit 20 Generationen; Preise nach Schnellmodell-Klasse ≈ 0,3 $/Mio. Eingabe- und 2,5 $/Mio. Ausgabetoken angenommen; je Kandidat ≈ 20.000 Eingabe- und 4.000 Ausgabetoken):
- Übungswerk (4 Bereiche, 856 Zeilen), Phase 1 mit einer Nische: **gemessen 0,40 €** für 5 Läufe, 236 Aufrufe (Fassung 1 hatte 20–60 € geschätzt — Faktor 50 zu hoch, weil die Sicht auf einen Bereich viel kleiner ist als 20.000 Token und Phase 1 nur eine Nische hatte).
- Übungswerk, Phase 1 Nachlauf (Läufe 6–10, eine Nische, schwerer Ankläger): **gemessen 1,79 €** für 542 Aufrufe; davon 27 schwere Aufrufe (5 %) = 0,65 € (36 %). Ein einzelner Lauf mit einer Nische und schwerem Ankläger: gemessen 0,3–0,75 €.
- Übungswerk, Phase 2 (vier Nischen, voller Ankläger, Generation 0): **gemessen 1,91 €** für drei Läufe, 1.190 Aufrufe; Hauptlauf 1,15 € für 14 Generationen mit 32 Kandidaten je Generation, 0 schwere Aufrufe (Schätzung 2–8 € war zu hoch).
- Phase 3 (zwei Übungswerke, Mentor, Jury, Sättigung, Oberfläche): **gemessen 2,83 €** für sieben Läufe, 1.225 Aufrufe (Schätzung 3–10 € traf). Davon 1,41 € für fünf nach Satz 2 verworfene Läufe und 0,74 € für 24 schwere Aufrufe (15 Ankläger-Eskalationen bei einem Sicherheitsbefund, 9 Mentor).
- **Gesamtstand aus der Datenbank (21.09.2026): 8,64 € über alle Aufträge** (4.070 Buchungen). Die aus Berichten summierten 7,82 € waren zu niedrig — gerundete Abschnittsbeträge statt Einzelbuchungen; die Datenbank ist die gültige Quelle.
- Vorbedingung 1 (Lauf 26, natürlich gesättigt nach Generation 5): gemessen 0,45 € von 3 €; enger Nachtrag 0,00 € von 2 €.
- Nachlauf zu Phase 3 (Läufe 21–23): **gemessen 0,44 €** von 10 €, 207 Aufrufe; Vorspann je Lauf 9 Kammerläufe, 4 Modellaufrufe, 0,0057 €, 44 s; Nachabstraktion des Artgedächtnisses 19 Aufrufe, 0,003 €.
- Mittelgroßes Werk (10 Bereiche, ~30.000 Zeilen): Schätzung 10–60 € je Lauf.
- Phase 5 (erstes echtes Werk): nicht schätzbar, solange das Werk nicht feststeht; Budget je Abschnitt setzt Philipp nach dem Kostenvoranschlag aus Aufnahme und Landkarte.
Alle Schätzungen ab Phase 2 werden an der Messung von Phase 2 nachgeführt. Die Kasse setzt sie als Vorschlag; Philipp bestätigt das Budget vor jedem Lauf.

---

## 7. Was aus dem Vorgängerprojekt bleibt

**Übernehmen (geprüft, funktioniert):**
- Der Server-Torwächter (Express: Request-IDs, strikte CORS-Liste, Helmet, Rate-Limits, Body-Limits, Sanitizing, Fehlerhandler, Redaction im Protokoll, Kill-Switch, Zod-validierte Umgebung). Änderung: Anmeldezwang fest verdrahtet, nicht abschaltbar; eine echte Anmeldung (Benutzer, Kennwort, Token-Ausgabe) existiert; **alle** Routen sind geschützt, nicht nur `/api/admin`.
- Der Aktenschrank (Chunking mit Überlappung, Stichwort- plus Bedeutungssuche, Cosinus-Vergleich) → wird Teil der Landkarte. Änderung: Embeddings für alle Abschnitte, nicht nur die ersten zehn je Dokument; Index statt linearer Suche ab 10.000 Abschnitten.
- Prüf- und Bauabläufe (CI, Lint, Prettier, Vitest, Playwright, gitleaks, CodeQL, Dependabot).
- Die Fehlerklassen und das Protokollsystem (`AppError`, `normalizeError`, Logger mit Redaction).
- Die Anbieterschicht (Port `IGenAIProvider`, Adapter je Anbieter).

**Ersetzen:**
- JSON-Datei als Datenbank → SQLite (mindestens) mit Transaktionen; bei Mehrbenutzerbetrieb Postgres.
- Sitzungsgedächtnis im Arbeitsspeicher → die drei Gedächtnisse in der Datenbank.

**Streichen (ohne Ersatz):**
- Alle nicht erreichbaren Komponenten (gemessen: 51 Dateien, 4.310 Zeilen), darunter MemoryCore, AgentMindMap, NeuralNexus, GamificationOverlay, SynapticChat, HolographicHUD, QuantumPreview, QuantumKernel, EntropyAtom, SingularityStrategy, StrategyFactory, SwarmAgents in ihrer jetzigen Form.
- Der regelbasierte Sicherheitsscanner mit Code-Umschreibung (`sanitizer.ts`): Ein Biotop verändert kein Werk außerhalb einer Generation. Sicherheitsprüfung wird ein hartes Maß (statische Analyse, Abhängigkeitsprüfung), keine Vorab-Zensur.
- Die Schalter „Sicherheitsmodus" und „Freigabepflicht" als Prompt-Text. Freigabe ist ein Kernmechanismus (Abschnitt 4, Schritt 8), kein Text.
- Alle `.env`-Dateien mit echten Schlüsseln. Geheimnisse ausschließlich über Umgebungsvariablen des Servers; gitleaks im CI-Pflichtlauf; Paket-Skripte, die ein Archiv erzeugen, schließen `.env*`, `node_modules`, `dist`, `coverage`, `.tools` aus (der Vorgänger wurde mit echten Schlüsseln verschickt).

---

## 8. Bauphasen mit Abnahmetoren

Jede Phase ist ein eigener Hermes-Auftrag mit eigenem Abschlussordner. Ein Tor gilt als bestanden, wenn **jede** Zeile mit beigefügter Ausgabe belegt ist. Eine Phase beginnt erst, wenn das Tor der vorherigen bestanden ist. Neue Funde während einer Phase gehen auf die Liste für danach, außer sie gefährden das laufende Tor.

### Phase 1 — Das Skelett
**Bauen:** Aufnahme, Landkarte (Stufen 0–3, Straßen; Verträge nur abgeleitet), harte Maße, ein Schwarm (eine Nische, zwei Anbieter), Ankläger (Schritte 1, 4, 5), Ausführungskammer, Lazarus, Kasse, Protokoll, Anmeldung, Datenbank. Keine Oberfläche außer einer Befehlszeile.
**Übungswerk:** Hermes baut ein Werk mit drei Bereichen (~800–1.200 Zeilen, mit Tests) und baut **fünf bekannte Schwächen** ein (je eine: Sicherheitslücke, Leistungsbremse, Vertragsverletzung, toter Code, fehlerhafte Randbedingung). Die Liste der fünf liegt versiegelt außerhalb der Reichweite des Biotops. Ein vierter, bereits sauberer Bereich dient als Halluzinationsprobe.
**Tor 1 (alle Zeilen mit Ausgabe):**
- Landkarte: alle Bereiche erkannt (4 von 4); alle Straßen erfasst (Bezugsgröße: Hermes zählt sie vor dem Lauf, das Biotop muss n von n finden).
- Schwächen: mindestens 4 von 5 gefunden und in angenommenen Generationen behoben; Kernmaß gestiegen (Zahl vorher/nachher). **Behoben** heißt: der versiegelte Befund tritt nicht mehr ein; bei der Sicherheitslücke zusätzlich nach 3.5 „behoben heißt verschwunden" (statischer Befund weg, Umgehung als Immuntest im Werk).
- Kein Rückschritt: In 0 von n angenommenen Generationen ist irgendein hartes Maß gesunken.
- Halluzinationsprobe: Im sauberen Bereich 0 angenommene Änderungen, die kein Maß heben.
- Lazarus: Jede angenommene Generation einmal zurückgeholt; Prüfsumme des Werks stimmt (n von n).
- Kasse: Budget auf 0,10 € gesetzt → Abbruch mit Meldung **vor** dem ersten Modellaufruf der nächsten Generation (Protokollzeile beigefügt).
- Laut scheitern: Werk ohne Tests eingelegt → Meldung „Messgerät fehlt", 0 gestartete Generationen.
- Kammer: Ein Kandidat mit Endlosschleife → nach Zeitlimit als gescheitert gewertet, Wirt unberührt.
- Anmeldung: Jede Route ohne Token → HTTP 401 (Liste aller Routen mit Ergebnis).

**Stand Phase 1 nach Lauf 2 (Wertung Chat-Claude, 19.09.2026):** 7 von 9 Zeilen bestanden. Zeile 2 nicht bestanden — S1 (`eval`) durch `__builtins__`-Leerung nur entschärft, Befund B307 weiterhin vorhanden, Umgehung über Objektintrospektion ausgeführt und bestätigt (162 erreichbare Klassen); damit 3 von 5 behoben. Zeile 3 formal bestanden, aber unter einer Formel, die Tests statt Werk belohnte. Alle übrigen Zeilen bestanden und bleiben gültig.

**Nachlauf zu Tor 1 — erledigt (Lauf 9, Abschlussordner `laeufe/biotop-phase-1-nachlauf/`, 19.09.2026 02:20):** Tor 1 **9 von 9 bestanden**, geprüft durch Chat-Claude am Bericht (Summen nachgerechnet, Kurve Lauf 2 nachvollzogen). S1 behoben nach „behoben heißt verschwunden": `eval` ersetzt durch Baum-Auswerter mit Knoten-Weißliste, Bandit 3 → 0, sechs Umgehungsklassen als Immuntest 6 von 6 abgewiesen, Laufzeit 69 → 84 ms (+22 %). S2 offen (keine Geschwindigkeits-Nische in Phase 1). Kernmaß F2 am Endwerk 0 = Höchstwert. Drei abgebrochene Läufe (6–8) deckten die Messgerät-Funde auf, die in Fassung 3 eingearbeitet sind. Kosten 1,79 € von 5 €. **Phase 1 ist abgeschlossen; Phase 2 ist freigegeben.**

### Phase 2 — Der Schwarm
**Bauen:** Vier Nischen, Bandit-Gewichtung, Generation 0 (Mutanten), Verträge explizit, Ankläger vollständig (Schritte 2 und 3, Norm-Regel 3.7), Nexus mit Verhandlung, Generalprobe und Pareto je Test, Immunisierung nach 3.10 Fassung 3 (nur bestandene Tests, offene Funde, Doppelungen), Verlaufskurve je Lauf, Grenzmaß „größte Funktion" absolut. Vor dem ersten Lauf: OpenRouter-Katalog auf aktuellere Schnellmodelle gleicher Hersteller zu gleichem oder niedrigerem Preis prüfen und die Wahl mit Preisen belegen.
**Ausgang:** Übungswerk `lagerhaus` im Zustand Lauf 9 Generation 6 (S1, S3, S4, S5 behoben, S2 offen), Verfassung Anhang A.
**Budget:** 10 €, hart.
**Tor 2:**
- Nischen: 4 aktiv, je mindestens 2 Anbieter; Bandit-Gewichte nach 10 Generationen protokolliert.
- Generation 0: Hermes baut 20 Mutanten in das Übungswerk; das Biotop meldet, welche die Tests nicht fangen (Zahl); nach Generation 0 werden mindestens 16 von 20 gefangen.
- S2 (Leistungsbremse) behoben nach dem Kriterium der versiegelten Liste, gemessen an der Referenzlast (Zahl vorher/nachher); Kernmaß dabei unverändert oder gestiegen (Nischenmaß 3.5).
- Nebenwirkungsprobe: Hermes schleust einen Kandidaten ein, der Bereich A messbar hebt und Bereich B messbar senkt → 0 von 1 angenommen, Anklägerbericht nennt B.
- Regressionsprobe (Fassung 3, aus Lauf 7): Hermes schleust einen Kandidaten ein, der eine frühere Behebung rückgängig macht und drei neue bestandene Tests mitbringt → 0 von 1 angenommen; das Protokoll nennt den gefallenen Einzeltest.
- Norm-Probe (Fassung 3, aus Lauf 7): Hermes schleust einen Angriffstest ein, der an der Vorgeneration fällt, am Kandidaten besteht, ohne Absturz und ohne Vertrags-/Verfassungsbezug → bleibt „offen", 0 Punkte, nicht im Werk.
- Vertragsprobe: Änderung an einer Grenze ohne Anpassung des Nachbarn → abgelehnt; mit Anpassung → **angenommen und im Werk** (je 1 Fall). Die Probe muss so gebaut sein, dass die Vertragsänderung eine Fehlerbehebung ermöglicht und das Paar Kernmaß bringt — sonst kann es nach 3.5 nicht angenommen werden, und die Zeile ist unerfüllbar (Fassung 4).
- Immunisierung: n bestätigte Fehler = n Tests im Werk (Liste mit Dateipfaden); Doppelungsanteil ausgewiesen und unter 20 % **der vom Ankläger erzeugten Tests** (Fassung 5: Bezugsgröße und Schlüssel nach 3.10); nach keiner angenommenen Generation ein fehlschlagender Test im Werk (0 von n).
- Verhandlung: mindestens 1 Generation, in der zwei Bereiche eine Vertragsänderung gemeinsam bestanden haben, protokolliert. (Fassung 4: Diese Zeile prüft nur den Mechanismus; die eingeschleuste Vertragsprobe erfüllt sie. Der Nachweis, dass der **Schwarm selbst** eine sinnvolle Vertragsänderung durchbringt, ist am Übungswerk nicht erzwingbar — dort gibt es keine Schnittstelle, die sich ändern sollte — und steht in Tor 4.)
- Verlaufskurve des Hauptlaufs mit Endtestbestand beigefügt (3.5).

**Stand Phase 2 nach Lauf 13 (Wertung Chat-Claude, Stand Fassung 6):** **9 von 11.** Zeile 7 nicht erfüllt — das Probenpaar K1157/K1158 bestand die Vertragsprüfung, brachte 0 Kernmaß und wurde nach 3.5 verworfen; „angenommen" war zu „bestanden" umgedeutet (in der Nachprobe zu Phase 3 nachgeholt und bestanden). **Zeile 8 gerissen:** Doppelungsanteil **68,5 %** (Fassung 6: gemessen mit dem gebauten Behauptungs-Schlüssel, nicht mehr geschätzt) gegen eine Grenze von 20 %; der ursprünglich gemeldete Wert von 2,5 % war gegen 240 Ablehnungen statt gegen 54 erzeugte Tests gerechnet und prüfte die Fundstelle statt der Behauptung. Die Grenze wird nicht verschoben; der Bau bleibt, die Zahl wird berichtigt. **Die Zeilen Nebenwirkung, Regression, Norm und Vertrag galten zwischenzeitlich als ungeprüft** (die alten Proben zielten über Textanker und trafen nach jeder angenommenen Generation woanders hin) und sind im Nachlauf zu Phase 3 mit gehärteten Proben **wieder belegt, 4 von 4**. Alle übrigen Zeilen bestanden. Gehobenes Werk: Lauf 13 Generation 13, 99 von 99 Tests, Kernmaß 0, `lager` 140 → 5 ms. Kosten 1,91 € von 10 €.

**Nachprobe zu Zeile 7 (Vorbedingung für den Bau von Phase 3):** Vertragsprobe nach der präzisierten Zeile — ein Paar aus Vertragsänderung und dadurch ermöglichter Fehlerbehebung, Kernmaß > 0, angenommen und im Werk; Gegenfall ohne Nachbar abgelehnt. Ausgang: Lauf 13 Generation 13. Budget 1 €, im Phase-3-Budget enthalten. Ergebnis als erste Zeile des Phase-3-Berichts; erst danach beginnt der Bau. Dazu die Kandidatenaufschlüsselung von Lauf 13 auf 470 aufgehen lassen oder die Differenz benennen.

### Phase 3 — Gedächtnis, Mentor, Oberfläche
**Bauen:** Drei Gedächtnisse (3.12), Mentor (3.4), Entropie mit Sättigungsmeldung (3.11), weiche Maße mit Jury (3.5), Archivierung offener Funde (3.10), Oberfläche (3.15) als Web-Oberfläche hinter der Anmeldung, vom Tablet bedienbar. Dazu ein **zweites Übungswerk** anderer Bauart als `lagerhaus` (Hermes wählt; z. B. eine kleine HTTP-Schnittstelle oder ein Befehlszeilenwerkzeug mit Dateiverarbeitung; Python; 3–4 Bereiche; mit Tests; 3 versiegelte Schwächen), damit das Artgedächtnis überhaupt etwas zu vergleichen hat. Für das zweite Übungswerk schreibt Hermes den Verfassungsentwurf, Chat-Claude bestätigt ihn am Bericht.
**Ausgang `lagerhaus`:** Lauf 13 Generation 13 (Kernmaß 0 in allen Bereichen — das Werk ist am Höchstwert; die Sättigungsmeldung muss das erkennen).
**Budget:** 15 €, hart, einschließlich Nachprobe.
**Tor 3:**
- Nachprobe Zeile 7 aus Phase 2 bestanden (siehe oben).
- Projektgedächtnis: Ein zweiter Lauf am ersten Übungswerk wiederholt 0 der im ersten Lauf gescheiterten Wege (Vergleich der Kandidaten beider Läufe nach Bereich und Änderungsziel; Zahl der Wiederholungen von n gescheiterten Wegen).
- Artgedächtnis: Nach Läufen an beiden Übungswerken liefert der Mentor bei einem dritten Lauf mindestens eine Richtung, die ausdrücklich auf einen Eintrag aus dem Artgedächtnis verweist (Eintrag benannt).
- Mentor: ≥ 3 Richtungen je Werk, je mit Ertrag (welches Maß), Risiko (welche Verträge/Bereiche), Aufwand in Generationen, berührten Bereichen.
- Entropie: Am gesättigten `lagerhaus` (Kernmaß 0) erscheint die Sättigungsmeldung spätestens nach Generation 6 mit Bezugsgröße (Generationen x–y, Verbesserung z %, Verschiedenheitsanteil); der Lauf endet daraufhin von selbst und nennt den Weg zurück zum Mentor.
- Jury: Zwischen zwei Kandidaten, die alle harten Maße bestehen und gleiches Kernmaß haben, entscheidet die Jury aus mindestens drei Modellen verschiedener Hersteller; Beleg: 1 Fall aus einem echten Lauf mit drei Begründungen und nachgewiesener Einstimmigkeit. **Die Uneinigkeit wird als Mechanikprüfung belegt (Fassung 5)** — gestellte Gegenstimme, Ergebnis „kein Urteil", ausdrücklich als gestellt gekennzeichnet; echter Modelldissens ist nicht erzwingbar (5 von 5 Fällen einstimmig, auch bei gestellten Zielkonflikten).
- Geschmacksgedächtnis, Mechanik (Fassung 4): Philipps echte Entscheidungen gibt es erst ab Phase 4. Prüfung mit versiegelter Regel — Hermes hinterlegt vor dem Lauf eine Entscheidungsregel (versiegelt, Prüfsumme), erzeugt danach 30 Freigaben/Ablehnungen nach dieser Regel; das Gedächtnis lernt aus den ersten 20 und sagt von den restlichen 10 mindestens 7 richtig voraus. Ausdrücklich gekennzeichnet als Mechanikprüfung, nicht als Nachweis über Philipps Geschmack.
- Archivierung: Offene Funde nach 5 **Generationen** archiviert (Fassung 5; Zahl archiviert / gesamt), 0 archivierte Funde in Kammerläufen danach. Tritt der Fall in keinem Lauf ein, wird er an einem eigens erzeugten offenen Fund geprüft und als Mechanikprüfung gekennzeichnet — eine Prüfung ohne Gegenstand besteht nicht, sie meldet.
- Oberfläche: Für jedes Bedienelement Dateipfad und Zeile der Stelle, die es liest oder schreibt (vollständige Liste; ein Element ohne Stelle = Tor nicht bestanden); Zugriff nur mit Anmeldung (Aufruf ohne Token → 401, belegt); Kostenstand und Kurve sichtbar.
- Kandidatenaufschlüsselung jedes Laufs geht auf die Gesamtzahl auf (Abschnitt 9).

**Stand Phase 3 (Wertung Chat-Claude, Stand Fassung 6):** **8 von 11 voll, 1 teilweise, 2 im Nachlauf erledigt.** Erfüllt: Nachprobe Zeile 7, **Projektgedächtnis** (Fassung 6 nach oben korrigiert — 0 von 3 strittigen Fällen sind durchgerutschte Wiederholungen; Hermes' Nachrechnung maß Token der hinzugefügten Zeilen statt der geänderten Ziele und hatte den Filter für verworfene Läufe nicht angewandt, die Zahl des Organs war richtig), Mentor, Entropie, Geschmacksmechanik, Oberfläche, Zerlegungen, Kurven beider Werke. Teilweise: Jury (einstimmiger Fall aus echten Läufen belegt, Uneinigkeit nur als gestellte Mechanikprüfung — echter Modelldissens ist nicht erzwingbar, 5 von 5 einstimmig auch bei gestellten Zielkonflikten). Im Nachlauf erledigt: **Artgedächtnis** (nach der Umstellung auf Muster 2 von 5 Richtungen mit werkübergreifendem Verweis, 0 erfunden) und **Archivierung** (nach dem Bezug auf Generationen hätten 4 von 5 Läufen archiviert; Mechanikprüfung belegt). Ergebnisse: `logmuehle` von Kernmaß −13 auf 0 mit allen drei versiegelten Schwächen behoben — bei der Sicherheitslücke hat der Schwarm den Subprozess ganz entfernt statt ihn abzusichern, am Maß gemessen besser als die erwartete Lösung; `lagerhaus` Sättigung nach Generation 5 mit Selbstbeendigung, `formeln` 132 → 1,3 ms. Kosten 2,83 € von 15 €. Drei Messgerätfehler, fünf verworfene Läufe, alle protokolliert. Der `logmuehle`-Verfassungsentwurf ist im Nachlauf abgedruckt und **bestätigt** (Anhang B).

**Nachlauf zu Phase 3 — erledigt** (Läufe 21–23, Abschlussordner `laeufe/biotop-phase-3-nachlauf/`, 0,44 € von 10 €): Alle neun Punkte abgearbeitet, geprüft durch Chat-Claude am Bericht. Gebaut: Generation minus eins in beiden Teilen, versiegelter Eichgegenstand, Fund-Neubewertung als Organ, Abbruch als benannter Befehl, Doppelungsschlüssel auf die Behauptung, Artgedächtnis-Muster, Probensperre am Merkmal, Archivierung nach Generationen, Median-Laufzeiten und gemessene Rauschtoleranz. Offen und in Fassung 6 eingearbeitet, aber **noch nicht gebaut**: Ankläger nennt Behauptung vorab (3.7), Mindestanteil des werkübergreifenden Blocks (3.12). Vier eigene Fehler von Hermes gefunden, bevor sie als Ergebnis galten; die sechs Grundsätze in Abschnitt 2a sind daraus gefasst.

### Phase 4 — Der Breitentest

**Zweck:** Das Biotop soll an jedem Werk arbeiten können, nicht nur an Python-Werken, die Hermes selbst geschrieben hat. Bisher kennt es zwei Werke derselben Art: `lagerhaus` (856 Zeilen) und `logmuehle` (482 Zeilen), beide Python, beide pytest, beide klein, beide aus Hermes' Feder, beide reine Ablauflogik ohne Oberfläche und ohne Zustand. Jedes Mal, wenn eine neue Werkart dazukam, traten sofort neue Messgerätfehler auf. Der Breitentest holt diese Fehler dort ein, wo sie nichts kosten — statt sie alle auf einmal an einem echten Werk zu treffen.

**Was universell heißt und was nicht (Fassung 7):** Keine endliche Zahl von Testwerken beweist, dass das nächste funktioniert. Erreichbar ist belegte Breite: In welchen Arten von Werken trägt das Biotop nachweislich? Eine Behauptung über alle Werke wird nie aufgestellt, auch nicht nach dem letzten Testwerk.

**Herkunft der Werke:** Hermes baut alle Testwerke selbst (Entscheidung Philipps, 21.09.2026), mit versiegelten Schwächen wie bei `lagerhaus` und `logmuehle`. Ausnahme in T4, siehe dort.

**Die vier Dimensionen, die bisher ungeprüft sind**, und das Werk, das sie abdeckt:

**T3 — andere Sprache und andere Werkzeugkette.** TypeScript oder JavaScript, ~1.500–2.500 Zeilen, 4–5 Bereiche, eigene Testsammlung (vitest oder jest), eigenes statisches Prüfwerkzeug. Betrifft: Syntaxbaum-Zerlegung, Mutantenerzeugung, Testläufer-Anbindung, Ergebnisleser (die JUnit-Parser, in denen bereits zwei Nachweislücken saßen), Sicherheitsprüfung ohne Bandit, Kammer mit anderer Laufzeitumgebung. **Das ist der größte Sprung und kommt zuerst**, weil er die meisten Organe berührt.

**T4 — Größe, fremder Stil, fehlende Tests, echte Altlasten.** Python, ~6.000–10.000 Zeilen, 8–12 Bereiche, **ohne vorhandene Testsammlung**, mit gewachsenen Altlasten (toter Code, Doppelungen, uneinheitliche Muster) statt nur versiegelter Einzelschwächen. Hermes erzeugt es über ein anderes Modell als sein eigenes, damit Stil und Struktur nicht seine sind. Betrifft: Landkarte in Zoomstufen (bisher nie nötig — beide Übungswerke passten ganz in einen Aufruf), Generation 0 mit echter Arbeit (bisher fing sie 40 von 40 und 42 von 42, weil die Werke bereits dicht getestet waren), Vertragsableitung an fremden Mustern, Kosten bei größerem Kontext.

**T5 — Werk mit Oberfläche.** HTML, CSS und JavaScript ohne Rahmenwerk, ~1.000–1.800 Zeilen. Betrifft: Was ist „besser", wenn Laufzeit fast nichts aussagt? Hier tragen zum ersten Mal die weichen Maße und die Jury die Entscheidung — bisher waren alle fünf Jury-Fälle einstimmig und die Uneinigkeit musste gestellt werden. Auch: Wie misst man ein Werk, das man ansehen muss?

**T6 — Zustand und Außenwelt.** Python, ~2.000–3.000 Zeilen, mit SQLite-Datenbank, Dateiablage und einer Schnittstelle nach außen, die in der Kammer stillgelegt ist. Betrifft: Kammer-Abschottung (kein Netz), Wiederholbarkeit der Messung bei Zustand, Referenzlast mit Vorbedingungen, und die bereichsweise Rauschmessung an einem Werk, dessen Laufzeit von Datenbankzugriffen abhängt.

**Reihenfolge:** T3, T4, T5, T6 — vom größten Bruch zum kleinsten. Jedes Werk ist ein eigener Auftrag mit eigenem Abschlussordner.

**Was nach jedem Testwerk zu erwarten ist:** Neue Messgerätfehler. Das ist der Zweck, kein Scheitern. Sie werden nach den Grundsätzen 7 bis 9 behandelt: reparieren, was im Kernpfad liegt; benennen und listen, was außerhalb liegt; ein Reviewdurchgang.

**Tor 4 — je Testwerk:**
- Aufnahme: Werk gebaut, Bau- und Testlauf, versiegelte Schwächen hinterlegt (bei T4 stattdessen eine unabhängig erhobene Liste der Altlasten mit Bezugsgröße).
- Generation minus eins: Rauschmessung mit Sperren je Bereich, Eichgegenstand gewählt und versiegelt, 4 von 4 Proben bestanden **und 4 von 4 Gegenproben an der vorgesehenen Zusicherung fehlgeschlagen** (Grundsatz 8), Eichkosten getrennt ausgewiesen.
- Generation 0: Mutantenfang ≥ 80 von 100 nicht-äquivalenten, äquivalente vorab mit Beleg aussortiert. Bei T4 zusätzlich: die Testsammlung wird erst erzeugt — Zahl der Tests vorher/nachher.
- Schwächen: ≥ 80 % der versiegelten Schwächen behoben nach „behoben heißt verschwunden" (3.5); bei T4 stattdessen Kernmaß vorher/nachher an der Altlastenliste.
- Kein Rückschritt: 0 von n angenommenen Generationen mit gesunkenem hartem Maß.
- Halluzinationsprobe: im unveränderten Vergleichsbereich 0 angenommene Änderungen ohne Maßgewinn.
- Doppelungsanteil unter 20 % der vom Ankläger erzeugten Tests.
- Sättigung oder Budgetabbruch dokumentiert — der Lauf endet nie still.
- Verbundausfall (Fassung 7): Fällt ein Modell des Verbunds aus (Ablehnung, Zeitüberschreitung, leere Antwort), wird das als Ausfall gezählt und **nie als Beitrag**; belegt an mindestens einem echten oder gestellten Ausfall je Testwerk, mit der Ausfallmeldung im Protokoll.
- Ein Reviewdurchgang; Abschlussordner trägt die Torzeilen, nicht jede Zwischenstufe.

**Abnahme des Breitentests — die Sättigungsregel (Entscheidung Chat-Claude, 21.09.2026):** Philipp hat die Zahl der Testwerke offengelassen. Eine feste Zahl wäre willkürlich; deshalb entscheidet dasselbe Prinzip, nach dem das Biotop selbst aufhört: **Der Breitentest ist abgeschlossen, wenn zwei aufeinanderfolgende Testwerke neuer Art durchlaufen, ohne einen neuen Messgerätfehler zu erzeugen.** Erzeugt T3 noch Fehler und T4 und T5 keine mehr, ist nach T5 Schluss; erzeugen alle vier weiterhin Fehler, kommen T7 und T8 dazu — Hermes schlägt die nächste ungeprüfte Dimension vor, Philipp entscheidet. Die Zahl wird nicht vorher festgelegt und nachher nicht verhandelt.

**Budget:** je Testwerk 10 €, hart. Schätzung nach den bisherigen Messungen: T3 und T5 je 1–4 €, T4 5–15 € wegen Größe und Generation 0, T6 2–6 €. Alle Zahlen sind Schätzungen und werden am Werk gemessen; die bisherigen Schätzungen von Chat-Claude lagen durchweg zu hoch.

### Phase 5 — Erstes echtes Werk

**Werk: noch nicht bestimmt.** Die Wahl trifft Philipp nach dem Breitentest. Kriterien, die sich aus Phase 1 bis 4 ergeben haben:
- **Es steht still.** Niemand baut parallel daran, solange das Biotop daran arbeitet — sonst ist das eingefrorene Maß am ersten Tag überholt, und weder Lazarus noch die Prüfsummen fangen das auf.
- **Es hat Tests, oder es lässt sich welche bauen.** Ohne Messgerät kein Lauf (Satz 6).
- **Sein Maß ist klar.** Je mehr vom Kernmaß auf harte Zahlen entfällt und je weniger auf Geschmack, desto belastbarer der Lauf.
- **Ein Fehlschlag ist nicht teuer.** Kein laufender Betrieb, keine Kunden, kein Geld im Spiel — beim ersten echten Werk noch nicht.
- **Seine Art ist im Breitentest belegt.** Ein Werk in einer Sprache oder Bauart, die das Biotop noch nie gesehen hat, ist kein erstes echtes Werk.

**Vorbedingungen, wenn das Werk gewählt ist:**
1. **Verfassung des Werks** — schreibt Philipp; Hermes legt einen Entwurf vor. Sie enthält, was das Werk ist, wofür es da ist, was nie passieren darf, die Tauschregeln und den **tragenden Pfad** für den Eichgegenstand (3.5). Ohne diesen Eintrag wartet das Organ und der Lauf beginnt nicht.
2. **Aufnahme und Landkarte** als eigener Abschnitt mit eigenem Bericht, bevor eine Generation läuft — hier zeigt sich, ob die Landkarte bei der Größe dieses Werks trägt.
3. **Generation minus eins** und **Generation 0** als eigene Abschnitte mit eigenen Budgets.
4. **Freigaben ausschließlich durch Philipp**; die Vollmacht für Übungswerke gilt hier nicht. Hier beginnt das echte Geschmacksgedächtnis.

**Tor 5** wird gesetzt, wenn das Werk feststeht — Kernmaß, harte Grenzen und Bezugsgrößen hängen am Werk und werden nicht vorher erfunden.

---

## 9. Abschlussordner und Berichtspflicht

Jeder Hermes-Auftrag (jede Phase) endet zwingend — auch bei Abbruch, Zeitmangel oder Scheitern — mit einem Abschlussordner an der festgelegten, von außen abrufbaren Stelle im Prüfkanal. Inhalt:
- `BERICHT.md`: Was gebaut wurde, was gemessen wurde, jede Torzeile mit Ergebnis und Verweis auf die Ausgabedatei; eigene Entscheidungen von Hermes gekennzeichnet; offene Punkte auf der Liste für danach.
- `ausgaben/`: die Rohausgaben jeder Messung (Testläufe, Prüfsummen, Protokollauszüge).
- `werk/`: das Übungswerk bzw. das gehobene Werk als Archiv (ohne `.env*`, `node_modules`, `dist`, `coverage`).
- `biotop/`: der Stand des Biotops als Archiv (gleiche Ausschlüsse) mit Prüfsumme.
- `KASSE.md`: alle Modellaufrufe des Auftrags mit Kosten und Kontingentverbrauch.

Die Endmeldung im Telegram-Chat enthält die Abholadresse und die Prüfsumme des Ordners. Chat-Claude prüft den Ordner, nicht die Meldung.
**Summenpflicht (Fassung 4):** Jede Aufschlüsselung im Bericht — Kandidaten nach Status, Ablehnungen nach Grund, Aufrufe nach Zweck, Kosten nach Modell — muss auf die genannte Gesamtzahl aufgehen. Geht sie nicht auf, nennt der Bericht die Differenz und ihre Ursache; ein Bericht mit stiller Differenz gilt als unvollständig.

---

## 10. Was Philipp entscheidet (Konfiguration, nicht Architektur)

- Budget je Lauf (Vorschlag für Phasen 1–3 zusammen: 150 €; Phase 4 gesondert nach Kostenvoranschlag der Kasse).
- Welche Schnellmodelle über OpenRouter für die Masse (mindestens zwei Anbieter).
- Die Stelle des Abschlussordners im Prüfkanal.
- Die Verfassung jedes Werks und das Maß jedes Laufs — bei Vorlage.

---

## Anhang A — Verfassung des Übungswerks `lagerhaus`

Geschrieben von Chat-Claude (Philipp hat die Entscheidung delegiert). Gilt für Lauf 3 und alle weiteren Läufe am Übungswerk. Ändert nur Philipp.

1. **Was es ist:** Ein Rabatt- und Lagerrechner für Verkaufsberichte. Es rechnet Preise mit Staffeln und Rabatten, führt Bestand aus einem Journal mit Reservierungen und erzeugt daraus Auswertungen. Es ist ein Übungswerk ohne Betriebszweck.
2. **Sicherheit vor Geschwindigkeit:** Kein Bereich darf Eingaben als Programmcode ausführen — weder mit `eval`/`exec` noch mit eingeschränkten Namensräumen. Ein Sicherheitsbefund wiegt mehr als jede Laufzeit. Tauschregel: Die Laufzeit auf der Referenzlast darf bis **×5** gegenüber dem Ausgangszustand steigen, wenn dabei ein statischer Sicherheitsbefund verschwindet; sonst gilt ×2.
3. **Korrektheit vor allem anderen:** Kein Bestand unter null; keine Reservierung, die nach dem Einlösen weiter zählt; keine negativen Rabatte; Staffelgrenzen sind inklusiv („ab 10 Stück" gilt bei 10).
4. **Grenzen sind Verträge:** Die Schnittstellen zwischen `formeln`, `preise`, `lager` und `bericht` ändern sich nur, wenn beide Seiten in derselben Generation angepasst und gemeinsam geprüft werden.
5. **`bericht` ist Ausgabe, keine Logik:** Der Bereich rechnet nichts selbst nach, was `preise` oder `lager` liefern; er formatiert.
6. **Was nie passieren darf:** Ein Kandidat, der Tests entfernt oder abschwächt, um einen Fehlschlag zu beseitigen; ein Kandidat, der einen Sicherheitsbefund durch Ausnahmeregel im Prüfwerkzeug (`# nosec`, Konfiguration) zum Verschwinden bringt statt durch Code.

---

---


## Anhang B — Verfassung des Übungswerks `logmuehle`

Entwurf Hermes, **von Chat-Claude bestätigt** (19.09.2026, am Nachlaufbericht Abschnitt 9; Prüfsumme der Datei `0ce7f865…`, Regeln `bce33200…`). Gilt für alle Läufe am Übungswerk `logmuehle`. Ändert nur Philipp.

1. **Was es ist:** Ein Befehlszeilenwerkzeug, das Zugriffsprotokolle im Common Log Format liest, nach Zeit, Status und Pfad filtert, Kennzahlen bildet und sie als Text, CSV oder JSON ausgibt. Übungswerk ohne Betriebszweck; es verarbeitet nur Dateien, die der Aufrufer nennt.
2. **Sicherheit vor Bequemlichkeit:** Kein Bereich reicht Eingaben des Aufrufers an eine Shell weiter oder führt sie als Programmcode aus; externe Werkzeuge werden nur als Argumentliste ohne Shell gestartet. Ein Sicherheitsbefund wiegt mehr als jede Laufzeit. Tauschregel: Die Laufzeit auf der Referenzlast darf bis ×3 gegenüber dem Bestwert des Laufs steigen, wenn dabei ein statischer Sicherheitsbefund verschwindet; sonst gilt ×2.
3. **Korrektheit der Zählung:** Jeder gelesene Eintrag wird genau einmal gezählt; unlesbare Zeilen werden gezählt und gemeldet, nie verschluckt; Zeitfenster sind an beiden Enden einschließlich; Zeiten sind zeitzonenbewusst und werden nach UTC normalisiert; Perzentile folgen dem nächsten Rang.
4. **Grenzen sind Verträge:** Die Schnittstellen zwischen `lesen`, `filtern`, `zaehlen` und `ausgabe` ändern sich nur, wenn beide Seiten in derselben Generation angepasst und gemeinsam geprüft werden.
5. **`ausgabe` ist Darstellung, keine Logik:** Der Bereich rechnet nichts nach, was `zaehlen` liefert; er formatiert und setzt Rückgabecodes.
6. **Was nie passieren darf:** Ein Kandidat, der Tests entfernt oder abschwächt, um einen Fehlschlag zu beseitigen; ein Kandidat, der einen Sicherheitsbefund durch Ausnahmeregel im Prüfwerkzeug (`# nosec`, Konfiguration) zum Verschwinden bringt statt durch Code; ein Kandidat, der Dateien außerhalb der genannten Protokolldatei liest oder schreibt.

Satz 2 wurde vom Schwarm anders erfüllt als erwartet — der Subprozess wurde ganz entfernt statt abgesichert; am Maß gemessen besser. Satz 6 ist mechanisch verdrahtet (`verbotene_muster`), Satz 2 über die Tauschregel (`laufzeit_faktor_bei_sicherheitsgewinn: 3.0`).

---

*Ende des Dokuments. Fassung 7, 21.09.2026. Fassungen 1 bis 6 sind durch diese Fassung ersetzt; die jeweils höchste Fassung gilt. Fortschreibung als Fassung 8 bei grundlegenden neuen Erkenntnissen.*
