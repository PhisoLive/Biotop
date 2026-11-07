# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 019 von 054

- Einträge V0359 bis V0359. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0359 · 20.09.2026 00:18:44 CEST · Philipp · Nachricht id 2718 · Sitzung `20260918_225920_3e614670` · 79266 B · Stück 1 von 3

```text
[The user sent a text document: 'INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_8d640daa6c3c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md]

[Content of INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md]:
# INFINITE EVOLUTION — Das Biotop

**Übergabedokument und Masterprompt für Hermes**
Stand: 19.09.2026 (nach dem Nachlauf zu Phase 3) · Fassung 6 · Auftraggeber: Philipp Zöllisch · Prüfer: Chat-Claude

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

## 2a. Sechs Grundsätze (Fassung 6)

Diese Sätze sind aus Fehlern gefasst, die in Phase 1 bis 3 mehrfach an verschiedenen Stellen auftraten. Sie stehen vor den Organen, weil jeder von ihnen an mehr als einem Organ greift; wer ein neues Organ baut, prüft es gegen diese sechs.

1. **Ein fallender Test beweist eine Abweichung, nie ihre Richtung** — welche Seite recht hat, entscheidet nur ein Absturz oder ein Vertrag. (Lauf 16: Fallen am Kandidaten machte aus einem Normtest einen Fund. Nachlauf: Fallen am Ausgang hätte dasselbe getan, 9 von 20.)
2. **Für jede Pflicht muss es einen benannten Befehl geben.** Eine Pflicht, die nur über Notbehelfe erreichbar ist, wird entweder blockiert oder umgeht den Schutz. (Der Abbruch nach Satz 2 war nicht vom Gate gesperrt — es gab ihn schlicht nicht.)
3. **Streuung wird immer zwischen Messungen gebildet, nie innerhalb einer.** Der Median glättet innerhalb, die Streuung misst zwischen; wer beides auf derselben Ebene bildet, misst die Glättung statt der Sache. Gilt für jede Kennzahl über wiederholte Messungen.
4. **Eine Prüfung darf den geprüften Bestand nicht verändern.** Ihr Wirkungsbereich wird vorher eingegrenzt; was sie hinterlässt, wird vor der nächsten Messung zurückgenommen und protokolliert. (Probenabfall in den Gedächtnissen; eine Mechanikprüfung archivierte zwei echte Normtests mit.)
5. **Eine Nachrechnung muss dieselbe Ableitung verwenden wie das geprüfte Organ**, sonst misst sie etwas anderes und erzeugt eine Scheindifferenz. (Drei strittige Projektgedächtnis-Fälle, alle drei aus der Ableitung, keiner aus der Sache.)
6. **Prüfe die Sache, nicht ihre Erscheinung:** Behauptung statt Fundstelle, gesetztes Merkmal statt Name, Verfassung statt Vertragsgröße, Syntaxbaum statt Textanker. (Doppelungserkennung, Probenerkennung, Eichgegenstand, Eichproben — vier Organe, dieselbe Fehlerklasse.)

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
  - **Klassenmaß:** Je Werkklasse kann die Verfassung ein Kernmaß setzen, das das obige ersetzt oder ergänzt (beim Handelssystem: Ertrag auf historischen Testdaten bei eingehaltener Verlustgrenze).
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
**Modelle:** Mindestens zwei verschiedene Anbieter je Nische, weil verschiedene Modelle verschiedene blinde Flecken haben. Masse über tokenabgerechnete Schnellmodelle (siehe Abschnitt 6), Durchbrüche über schwere Modelle. Das Biotop führt Buch, welches Modell in welcher Nische bei welcher Werkklasse angenommene Kandidaten liefert, und gewichtet danach (Bandit-Verfahren). **„KEIN VORSCHLAG" ist neutral (Fassung 4):** Eine Antwort, die ehrlich keinen Kandidaten liefert, wird weder als Erfolg noch als Misserfolg gebucht und zählt nicht als Wahl. Ein Modell darf nie dafür bestraft werden, dass es nichts erfindet.
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

```

