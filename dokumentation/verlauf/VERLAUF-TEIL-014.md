# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 014 von 054

- Einträge V0223 bis V0223. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0223 · 19.09.2026 19:35:53 CEST · Philipp · Nachricht id 2232 · Sitzung `20260918_225920_3e614670` · 65170 B · Stück 1 von 2

```text
[The user sent a text document: 'INFINITE-EVOLUTION-BIOTOP-Masterprompt-v5.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_bef1d4cc25fa_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v5.md]

[Content of INFINITE-EVOLUTION-BIOTOP-Masterprompt-v5.md]:
# INFINITE EVOLUTION — Das Biotop

**Übergabedokument und Masterprompt für Hermes**
Stand: 19.09.2026 (nach Phase 3) · Fassung 5 · Auftraggeber: Philipp Zöllisch · Prüfer: Chat-Claude

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
**Generation minus eins — das Messgerät eichen (Fassung 5):** Vor Generation 0 prüft das Biotop sich selbst. Die vier Proben aus Tor 2 laufen als Vorspann jedes Laufs, nicht nur einmal als Abnahme: Nebenwirkungsprobe (hebt A, senkt B → tot), Regressionsprobe (Behebung rückgängig plus grüne Tests → tot, gefallener Einzeltest genannt), Norm-Probe (Test ohne Absturz und ohne Vertragsverweis → offen, 0 Punkte, kein Kill, nicht im Werk) und Vertragsprobe (ohne Nachbar abgelehnt, mit Nachbar angenommen). Dazu die Rauschmessung (oben) und die Neubewertung aller übernommenen offenen Funde (3.10). Besteht eine Probe nicht, beginnt kein Lauf — das Messgerät wird repariert, und der reparierte Stand ist ein neuer Lauf nach Satz 2. Grund: In Phase 3 starben fünf von sieben Läufen, weil das Messgerät erst im Lauf als kaputt auffiel; die Proben existierten längst und hätten den Fehler vorher gefunden. Kosten der Eichung: wenige Kammerläufe, gemessen deutlich unter den 1,41 €, die die verworfenen Läufe kosteten.

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
- **Artgedächtnis** (über alle Werke): **Es speichert Muster, keine Instanzen (Fassung 5).** Zu jeder angenommenen Generation schreibt ein zusätzlicher Aufruf den abstrahierten Satz — was getan wurde und warum es wirkte, **ohne Werk-, Datei- oder Funktionsnamen**: nicht „in `logmuehle` bekam `filtern()` einen Index", sondern „wiederholtes Durchsuchen durch eine mitgeführte Struktur ersetzen, wenn dieselbe Menge mehrfach gelesen wird". Nur diese Muster werden werkübergreifend vorgelegt, zusammen mit der Werkklasse, bei der sie gewirkt haben, und dem erreichten Maßgewinn; die Instanz bleibt als Beleg daneben, wird aber nicht als Vorlage gezeigt. Grund: Instanzen gelten am fremden Werk nicht, und das Modell übergeht sie zu Recht — gemessen 0 werkübergreifende Verweise bei 12 Richtungen. Der Mentor liest die Muster für seine Richtungen, der Schwarm für seine Vorschläge. Das ist die Evolution des Biotops selbst — ohne dass es seinen Code ändert. **Ein werkübergreifender Verweis wird nie erzwungen:** Ein Pflichtfeld erzeugt Scheinbegründungen, und die sind schlimmer als keine Verweise.
- **Geschmacksgedächtnis** (Philipp): jede Freigabe, jede Ablehnung, jede Begründung. Ab 20 Entscheidungen wird daraus ein Vorhersagemodell, das die Jury (3.5) bei weichen Maßen ergänzt. Es ersetzt Philipp nie; es sagt vorher, was er wahrscheinlich entscheidet, und legt es ihm mit der Vorlage bei.

### 3.13 Ausführungskammer
```

