# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 008 von 054

- Einträge V0090 bis V0090. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0090 · 19.09.2026 12:39:25 CEST · Philipp · Nachricht id 1393 · Sitzung `20260918_225920_3e614670` · 56053 B · Stück 1 von 2

```text
[Replying to: "Phase 2 „Der Schwarm" abgeschlossen. Abschlussordner liegt im Prüfkanal.

Abholadresse:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/BERICHT.md

Prüfsumme des Ordners (SHA-256 über DATEIEN.txt, 122 Dateien, von außen gegengeprüft):
6b1e7f6a3e27a8830008f787c2e1fdddb62df90237555828767ea7e5d2b277a7

Tor 2: 11 von 11 (Hauptlauf 13, 14 Generationen, 7 angenommen):
- Nischen: 4 aktiv, je 4 von 4 Herstellern; Bandit-Gewichte nach 14 Generationen, 235 Wahlen protokolliert
- Generation 0: 20 versiegelte Mutanten, 16 → 17 von 20 gefangen (2 der 3 Restlichen sind äquivalente Mutanten, kein Test kann sie fangen — im Bericht begründet)
- S2 behoben: last_lager 139,5 → 5,2 ms (−96 %, Kriterium ≥ 50 % vorab versiegelt), Journal führt inkrementelle Summen; Kernmaß 0 → 0
- Nebenwirkungsprobe 0 von 1, Bericht nennt bericht; Regressionsprobe 0 von 1, gefallener Einzeltest genannt; Norm-Probe: Test 0 Punkte, nicht im Werk; Vertragsprobe: ohne Nachbar abgelehnt, mit Nachbar Vertrag bestanden
- Immunisierung: 6 Fehler = 6 neue Tests, Doppelungen 2,5 %, 0 von 8 angenommenen Generationen mit rotem Test (99 von 99 am Ende)
- Verhandlung: 1 bestanden (Protokoll #7251) — ehrlich: durch die eingeschleuste Probe, nicht durch den Schwarm; der Schwarm löste 4 aus, keine bestand
- Verlaufskurve mit Endtestbestand beigefügt; Modellwahl am Katalog belegt (gpt-5.6-luna, gemini-3.5-flash-lite, deepseek-v4.1-flash, qwen3.8-flash — alle 2026, gleicher oder niedrigerer Preis)

Was schiefging und behoben wurde: Lauf 12 (Vorlauf, 10 Generationen) zeigte über die Norm-Probe, dass die Norm-Regel nur Ankläger-Tests traf, nicht mitgebrachte — korrigiert, neuer Lauf 13 vom selben Ausgang. Zwei weitere Biotop-Fehler ohne Maßwirkung protokolliert (Verhandlungs-Paarprüfung, Gen-0-Prompt).

Kosten: 1,91 € von 10 € (1.190 Aufrufe); Lauf 13 allein 1,15 € für 14 Generationen mit 32 Kandidaten je Generation. Schwere Aufrufe: 0 — kein Sicherheitsbefund mehr im Werk.

Für Fassung 4 (Abschnitt 8 des Berichts): Grenzmaß gegen Ausgang ließ in Gen 10 einen 5-fachen Laufzeitanstieg gegen die Vorgeneration zu (regelkonform, aber diskussionswürdig); Bandit wertet „KEIN VORSCHLAG" als Misserfolg; äquivalente Mutanten in der Bezugsgröße."]

[The user sent a text document: 'INFINITE-EVOLUTION-BIOTOP-Masterprompt-v4.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_b31bd88baae3_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v4.md]

[Content of INFINITE-EVOLUTION-BIOTOP-Masterprompt-v4.md]:
# INFINITE EVOLUTION — Das Biotop

**Übergabedokument und Masterprompt für Hermes**
Stand: 19.09.2026 (nach Phase 2) · Fassung 4 · Auftraggeber: Philipp Zöllisch · Prüfer: Chat-Claude

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
  - **Grenzmaße** (keine Punkte; darüber ist der Kandidat tot): Laufzeit auf Referenzlast, Speicher, Bauzeit, größte Funktion, Zyklen. **Bezug ist der Bestwert des Laufs** (Fassung 4): je Maß und Bereich der beste Wert aller bisher angenommenen Generationen einschließlich Ausgang — nicht der Ausgang allein, sonst darf ein Kandidat einen früheren Gewinn wieder aufbrauchen. Regel: Ohne Kernmaßgewinn darf ein Kandidat kein Grenzmaß über Bestwert + 15 % (Rauschtoleranz) verschlechtern. Mit Kernmaßgewinn gilt die Tauschregel der Verfassung des Werks; Vorgabe ohne Angabe: Laufzeit bis ×2 des Bestwerts, Speicher/Bauzeit/Zyklen bis +25 %. **Größte Funktion absolut 60 Zeilen** (Fassung 3) — die relative Grenze +25 % gilt nur für Funktionen, die schon oberhalb von 60 Zeilen liegen. Leistung ist damit eine Grenze, kein Punkt — Geschwindigkeit kann Sicherheit nie aufwiegen, und Korrektheit kann Geschwindigkeit nur im Rahmen der Tauschregel kaufen.
  - **Verlaufskurve** (Fassung 3): Für jeden Lauf wird am Laufende jede angenommene Generation aus Lazarus geholt, mit dem Endtestbestand gemessen und als Kurve (Kernmaß je Generation, Zerlegung nach Fehlschlägen / Sicherheit / toten Funktionen) dem Abschlussordner beigefügt. Ohne Kurve ist ein Abschlussordner unvollständig.
  - **Nischenmaß:** Die Nische *Der Schnelle* wird an der Laufzeit gemessen; ihre Kandidaten werden nur angenommen, wenn das Kernmaß dabei gleich bleibt oder steigt.
  - **Klassenmaß:** Je Werkklasse kann die Verfassung ein Kernmaß setzen, das das obige ersetzt oder ergänzt (beim Handelssystem: Ertrag auf historischen Testdaten bei eingehaltener Verlustgrenze).
  - **Behoben heißt verschwunden:** Eine Sicherheitsschwäche gilt erst als behoben, wenn der statische Befund verschwunden ist und die für diese Befundklasse bekannte Umgehung als Immuntest im Werk liegt. Ein Kandidat, der einen Befund entschärft, ohne ihn zu entfernen, kann angenommen werden, wenn er Fehlschläge beseitigt — die Schwäche zählt trotzdem als offen.
- **Weiche Maße** (Lesbarkeit, Eleganz, Nutzererlebnis) bewertet eine Jury aus mindestens drei Modellen verschiedener Anbieter mit Begründung — **nur** zwischen Kandidaten, die alle harten Maße bereits bestehen, und nur bei Einstimmigkeit. Weiche Maße beweisen nichts; sie brechen Gleichstände.
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
**Doppelungen (Fassung 3):** Je bestätigtem Fehler kommt ein Test ins Werk; weitere Tests, die denselben Fehler beweisen (gleiche Ausnahme oder gleiche Zusicherung an derselben Stelle), werden als Doppelung gekennzeichnet und nicht übernommen. Der Anteil gekennzeichneter Doppelungen an allen Angriffstests wird je Lauf ausgewiesen.
**Archivierung offener Funde (Fassung 4):** Ein offener Fund, den nach fünf Generationen kein angenommener Kandidat besteht, wird archiviert — er bleibt in der Datenbank einsehbar, wird aber späteren Kandidaten nicht mehr vorgelegt und kostet keinen Kammerlauf mehr. Der Mentor (3.4) sieht das Archiv und kann daraus Richtungen ableiten.

### 3.11 Entropie — Sättigungsmeldung
**Aufgabe:** Ehrlich sagen, wenn es in einer Richtung nicht mehr weitergeht.
**Messung:** Je Generation zwei Zahlen — die Verbesserung des Kernmaßes gegenüber der Vorgeneration in Prozent, und die Verschiedenheit der Schwarmvorschläge (Anteil der Kandidaten, die sich in weniger als 10 % der geänderten Zeilen unterscheiden).
**Regel:** Bringen fünf aufeinanderfolgende Generationen zusammen weniger als 0,5 % Verbesserung des Kernmaßes, meldet das Biotop: *„In dieser Richtung gesättigt: Generationen x–y, Verbesserung z %. Weiter nur mit anderer Richtung (zurück zum Mentor) oder anderem Maß (neuer Lauf)."* Es sagt nie „perfekt". Es sagt, wo es weitergeht.

### 3.12 Die drei Gedächtnisse
Alle drei dauerhaft in der Datenbank, alle drei werden vor jeder Generation gelesen.
- **Projektgedächtnis** (je Werk): jede Generation, jeder Kandidat, jedes Ergebnis, jede Ablehnung mit Grund. Der Schwarm bekommt vor jeder Generation die Liste der gescheiterten Wege dieses Werks und den Auftrag, sie nicht zu wiederholen.
- **Artgedächtnis** (über alle Werke): welche Art von Änderung bei welcher Werkklasse (Sprache, Größe, Bauart) angenommen wurde und was sie brachte. Der Mentor liest es für seine Richtungen, der Schwarm für seine Vorschläge. Das ist die Evolution des Biotops selbst — ohne dass es seinen Code ändert.
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
**Vollmacht für Übungswerke (Fassung 2):** Für Werke ohne Betriebszweck, die Hermes selbst erzeugt hat, gilt eine schriftliche Vollmacht: Hermes gibt Generationen frei, protokolliert je Freigabe die Begründung (`freigabe.frei`, Vollmacht als Grund genannt), und Chat-Claude prüft alle Freigaben am Abschlussordner. Für jedes Werk mit Betriebszweck gibt ausschließlich Philipp frei; eine stellvertretende Freigabe dort ist ein Verstoß, kein Ermessen.

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

---

## 6. Modelle und Kosten

**Rollenverteilung (Vorgabe; Hermes verdrahtet):**
- *Masse* (Schwarm-Kandidaten, Ankläger-Angriffe, Zusammenfassungen der Landkarte): tokenabgerechnete Schnellmodelle über OpenRouter — mindestens zwei Anbieter. Nie über Abo-Kontingente, weil ein Lauf Hunderte bis Tausende Aufrufe macht und ein Wochenkontingent in Stunden leeren würde.
- *Schwere Aufrufe* (Mentor, Verfassungsentwurf, Jury-Endurteil, Anklägerbericht an Philipp): die schweren Modelle des bestehenden Teams, gezählt gegen eine eigene Kontingentgrenze in der Kasse.
- Die Anbieterschicht ist austauschbar (ein Port, mehrere Adapter), wie im Vorgängerprojekt bereits angelegt.

**Kostenschätzung** (Schätzung; Bezugsgröße: ein Lauf mit 20 Generationen; Preise nach Schnellmodell-Klasse ≈ 0,3 $/Mio. Eingabe- und 2,5 $/Mio. Ausgabetoken angenommen; je Kandidat ≈ 20.000 Eingabe- und 4.000 Ausgabetoken):
- Übungswerk (4 Bereiche, 856 Zeilen), Phase 1 mit einer Nische: **gemessen 0,40 €** für 5 Läufe, 236 Aufrufe (Fassung 1 hatte 20–60 € geschätzt — Faktor 50 zu hoch, weil die Sicht auf einen Bereich viel kleiner ist als 20.000 Token und Phase 1 nur eine Nische hatte).
```

