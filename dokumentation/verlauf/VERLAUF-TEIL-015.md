# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 015 von 054

- Einträge V0223 bis V0228. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0223 · 19.09.2026 19:35:53 CEST · Philipp · Nachricht id 2232 · Sitzung `20260918_225920_3e614670` · 65170 B · Stück 2 von 2

```text
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
- Phase 4 (Handelssystem, ~237.000 Zeilen, 17 Dienste): Schätzung 50–300 € je Lauf, dominiert von Generation 0 und von schweren Ankläger-Aufrufen bei Sicherheitsbefunden. Budget je Lauf vor dem Start durch Philipp.
- Mittelgroßes Werk (10 Bereiche, ~30.000 Zeilen): Schätzung 10–60 € je Lauf.
- Handelssystem (17 Dienste, ~237.000 Zeilen Python): Schätzung 50–300 € je Lauf, plus Generation 0 gesondert, weil das Messgerät dort zuerst repariert werden muss.
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

**Stand Phase 2 nach Lauf 13 (Wertung Chat-Claude, Stand Fassung 5):** **9 von 11.** Zeile 7 nicht erfüllt — das Probenpaar K1157/K1158 bestand die Vertragsprüfung, brachte 0 Kernmaß und wurde nach 3.5 verworfen; „angenommen" war zu „bestanden" umgedeutet (in der Nachprobe zu Phase 3 nachgeholt und bestanden). **Zeile 8 rückwirkend gerissen:** Der gemeldete Doppelungsanteil von 2,5 % war gegen 240 Ablehnungen statt gegen 55 erzeugte Tests gerechnet und prüfte die Fundstelle statt der Behauptung; mit richtiger Bezugsgröße 10,9 %, mit der gemeinten Lesart 83,6 % gegen eine Grenze von 20 %. Die Grenze wird nicht verschoben; der Bau bleibt, die Zahl wird berichtigt. Alle übrigen Zeilen bestanden. Gehobenes Werk: Lauf 13 Generation 13, 99 von 99 Tests, Kernmaß 0, `lager` 140 → 5 ms. Kosten 1,91 € von 10 €.

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

**Stand Phase 3 nach Lauf 20 (Wertung Chat-Claude, 19.09.2026, in Übereinstimmung mit Hermes):** **7 von 11 voll, 2 teilweise, 2 nicht belegt.** Erfüllt: Nachprobe Zeile 7, Mentor, Entropie, Geschmacksmechanik, Oberfläche, Zerlegungen, Kurven beider Werke. Teilweise: Projektgedächtnis (Biotop-Sicht 0 durchgerutschte Wiederholungen, Hermes' gröbere Nachrechnung findet 2 von 187 und 1 von 44 — Differenz offen, nicht wegerklärt) und Jury (einstimmiger Fall belegt, Uneinigkeit nur gestellt). Nicht belegt: Artgedächtnis (0 werkübergreifende Verweise bei 12 Richtungen) und Archivierung (kein Fund erlebte 5 angenommene Generationen). Ergebnisse: `logmuehle` von Kernmaß −13 auf 0 mit allen drei versiegelten Schwächen behoben — bei der Sicherheitslücke hat der Schwarm den Subprozess ganz entfernt statt ihn abzusichern, am Maß gemessen besser als die erwartete Lösung; `lagerhaus` Sättigung nach Generation 5 mit Selbstbeendigung, `formeln` 132 → 1,3 ms. Kosten 2,83 € von 15 €. Drei Messgerätfehler, fünf verworfene Läufe, alle protokolliert. Der `logmuehle`-Verfassungsentwurf lag dem Bericht nicht bei und ist **nicht bestätigt**.

**Nachlauf zu Phase 3 (Vorbedingung für Phase 4):**
- Artgedächtnis auf Muster umstellen (3.12 Fassung 5), die vorhandenen Einträge beider Werke einmalig nachabstrahieren, dann die Torzeile erneut messen: ein Lauf am `lagerhaus` nach einem Lauf am `logmuehle`, Verweise getrennt ausgewiesen (werkübergreifend / eigenes Werk / erfunden). Zeile erfüllt bei ≥ 1 werkübergreifendem Verweis ohne Pflichtfeldzwang.
- Archivierung nach der umformulierten Zeile messen (5 Generationen, notfalls Mechanikprüfung an einem erzeugten Fund).
- Doppelungserkennung auf die Behauptung umstellen (3.10 Fassung 5), Anteil an den erzeugten Tests je Lauf ausweisen; Tor 2 Zeile 8 an einem Lauf neu messen — unter 20 %.
- Projektgedächtnis-Differenz schließen: beide Ableitungen (Hunk-Köpfe und angewandter Diff) auf denselben Kandidatensatz anwenden und die 3 strittigen Fälle einzeln entscheiden.
- Rauschmessung, Median-Laufzeiten, Generation minus eins, Fund-Neubewertung als Organ, Gate-Ausnahme für Abbrüche einbauen (Fassung 5).
- `logmuehle`-Verfassungsentwurf im Bericht abdrucken, damit Chat-Claude ihn bestätigen kann.
- Budget 10 €, hart. Abschlussordner `laeufe/biotop-phase-3-nachlauf/`.

### Phase 4 — Erstes echtes Werk
**Werk:** Das KI-Handelssystem (~237.000 Zeilen Python, 17 Dienste). Begründung der Wahl: das schärfste Kernmaß, das es gibt (Ertrag auf historischen Testdaten mit Verlustgrenze ist eine Zahl, über die niemand streitet), und das Werk, an dem die Landkarte zwingend ist.
**Besonderheiten:** Das Werk hat derzeit 135 reproduzierbare Testfehlschläge und Risikomodule, die nicht im Orderpfad liegen — Generation 0 wird dort lang und ist der eigentliche erste Ertrag. Verfassung des Werks enthält die harten Grenzen: gesetzliche Hebelgrenzen je Anlageklasse, Tagesverlustgrenze, Ausschluss von Rüstung und schädlichen Geschäftsfeldern, kein echter Handel ohne bestandenes Bewertungssystem, Demokonto zuerst. **Freigaben ausschließlich durch Philipp** (Abschnitt 4) — hier beginnt das echte Geschmacksgedächtnis.
**Tor 4:**
- Generation 0: Testfehlschläge von 135 auf 0; Mutantenfang ≥ 80 von 100 nicht-äquivalenten.
- Verfassung: Risikomodule nachweislich im Orderpfad (Eintrittspunkte gezählt, je Tor ein roter und ein grüner Eichfall mit Ausgabe).
- Kernmaß: Ertrag auf Testdaten gestiegen (Zahl vorher/nachher), Verlustgrenze in 0 von n Testtagen verletzt.
- Kein Rückschritt in irgendeinem Bereich über alle angenommenen Generationen.
- Verhandlung durch den Schwarm (Fassung 4): mindestens 1 von n vom Schwarm ausgelöste Vertragsänderungen bestanden **und** angenommen, ohne eingeschleuste Probe.
- Sättigungsmeldung oder Budgetabbruch dokumentiert — der Lauf endet nie still.

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

*Ende des Dokuments. Fassung 5, 19.09.2026 (nach Phase 3). Fassungen 1 bis 4 sind durch diese Fassung ersetzt; die jeweils höchste Fassung gilt. Fortschreibung als Fassung 6 bei grundlegenden neuen Erkenntnissen.*


Phase 3 ist mit 7 von 11 abgenommen, deine Wertung war richtig — lies INFINITE-EVOLUTION-BIOTOP-Masterprompt-v5.md vollständig, Fassung 4 ist ersetzt. Deine sechs Vorschläge sind drin, drei anders gelöst: Das Artgedächtnis wird auf Muster umgestellt statt die Torzeile abzuschwächen (kein Pflichtfeld für Verweise), die Rauschtoleranz wird vor jedem Lauf gemessen, und die vier Proben laufen ab jetzt als „Generation minus eins" vor jedem Lauf. Auftrag: Nachlauf zu Phase 3 nach Abschnitt 8 — Artgedächtnis umstellen und Einträge beider Werke nachabstrahieren, Doppelungsschlüssel auf die Behauptung, Archivierung nach der neuen Zeile, Projektgedächtnis-Differenz an den drei strittigen Fällen entscheiden, Generation minus eins und Fund-Neubewertung als Organ einbauen, Gate-Ausnahme für Abbrüche, logmuehle-Verfassungsentwurf im Bericht abdrucken; Budget 10 € hart, Abschlussordner laeufe/biotop-phase-3-nachlauf/, Endmeldung mit vollständiger Abholadresse als ganze URL und Prüfsumme.
```

### V0224 · 19.09.2026 19:36:52 CEST · Hermes · Nachricht id 2233 · Sitzung `20260918_225920_3e614670` · 6319 B

```text
**Teil 1 von 2 — Phase 3, Tor-3-Zeilen im Einzelnen**

Abholadresse, vollständig und unverlinkt, in eigener Zeile:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/BERICHT.md

Prüfsumme des Ordners (SHA-256 über DATEIEN.txt, 198 Dateien): `a2b2cee98ecdea5724bc8969721f41ea5b44ffdb037bc3427489cc9ee6f737fb`

**1. Nachprobe Zeile 7 — erfüllt.** Lauf 16, Generationen 1–3, als echte Generation gelaufen. Fehler durch Ausführung belegt (`bericht.lagerwert` summierte 100 USD als 100,00 statt 92,59 EUR). Fall 1a (Vertragsdatei geändert, Vertrag nicht benannt) und Fall 1b (ohne Nachbar-Anpassung): **2 von 2 korrekt abgelehnt**. Fall 2: K1164 benennt und ändert den Vertrag, der Schwarm von `preise` liefert K1165, Paar bestanden (Protokoll #7500), Kernmaß −2 → 0, **Generation 3 angenommen und im Werk** — Lazarus-Tag `lauf16-gen3`, 103 von 103 Tests, `lagerwert` = 192,59. **1 von 1.** Datei: `14-nachprobe-z7-ergebnis.txt`

**2. Projektgedächtnis — teilweise.** Lauf 20 verwarf **9 Kandidaten** als Wiederholung ohne Kammerlauf; Bezugsgröße 172 Kandidaten, davon 48 Ablehnungen — 9 der 48 kosteten keinen Kammerlauf. Meine unabhängige Nachrechnung findet **2 von 187** gescheiterten Wegen aus Lauf 13, die trotzdem ausgeführt wurden (Ähnlichkeit 1,00 und 0,81), und **1 von 44** aus Lauf 16 (0,58). Ursache der Differenz, offen ausgewiesen: meine Ableitung der berührten Funktionen (Hunk-Köpfe) ist gröber als die des Biotops (angewandter Diff). Gefordert sind 0. Dateien: `60-tor3-projektgedaechtnis.txt`, `60-…-gegen-lauf13.txt`

**3. Mentor — erfüllt.** 5 Aufrufe (Läufe 16, 17, 18, 19, 20), je **4–5 Richtungen** (gefordert ≥ 3 je Werk). Pflichtfelder Ertrag / Risiko / Aufwand in Generationen / berührte Bereiche mechanisch geprüft: **in allen Richtungen aller 5 Aufrufe vollständig**. Dateien: `40-`, `81-`, `90-`, `100-mentor-*.json`

**4. Entropie — erfüllt.** `lagerhaus` (Lauf 20, Kernmaß 0 = Höchstwert): Sättigung **nach Generation 5**, gefordert war spätestens 6 — „Generationen 1–5, Verbesserung 0,00 % (Schwelle 0,5 %), Kernmaß 0 = Höchstwert, Doppelgänger-Anteil 12 %. Weiter nur mit anderer Richtung — zurück zum Mentor." Der Lauf hat sich **selbst beendet** (Status `gesaettigt`), der Läufer brach ab. `logmuehle` (Lauf 17): nach Generation 8, Fenster 4–8, 0,00 %, Doppelgänger 9 %. Dateien: `63-entropie-lauf20.json`, `63-entropie-lauf17.json`

**5. Jury — zur Hälfte.** Einstimmiger Fall belegt: **3 Fälle aus echten Läufen** (Lauf 17 Gen 2 `zaehlen`, Lauf 17 Gen 3 `filtern`, Lauf 20 Gen 1 `preise`), je drei Juroren dreier Hersteller (openai, google, deepseek), je drei ausformulierte Begründungen im Protokoll. Fall ohne Einstimmigkeit **nicht mit echtem Dissens**: **5 von 5 einstimmig**, auch bei zwei von mir gestellten Zielkonflikten (kurz+dicht gegen lang+explizit; Kürze gegen Fehlermeldungsqualität). Mechanik mit **gestellter Gegenstimme** belegt: `einstimmig false`, `gewinner None`, Protokoll #12361 — ausdrücklich als gestellt gekennzeichnet. Dateien: `61-`, `95-`, `96-tor3-jury*.txt`

**6. Geschmacksgedächtnis (Mechanik) — erfüllt.** Versiegelte Regel P1, Prüfsumme `eed64ca5…` vor dem Lauf hinterlegt (`02-versiegelt-pruefsummen-vorher.txt`). 30 Entscheidungen nach der Regel an echten Kandidaten aus Lauf 13, aus den ersten 20 gelernt, von den restlichen **10 von 10** richtig vorhergesagt (gefordert ≥ 7). Ausdrücklich Mechanikprüfung, kein Nachweis über deinen Geschmack. Datei: `21-tor3-geschmack.txt`

**7. Oberfläche — erfüllt.** **18 von 18** Routen ohne Token → HTTP 401, vollständige Liste mit Ergebnis je Route. **18 von 18** Bedienelemente mit Dateipfad **und Zeilennummer** der lesenden/schreibenden Stelle (z. B. `kosten-stand → GET /laeufe/<id>/kasse → biotop/kern/kasse.py:31`), kein Element ohne Stelle. Kostenstand und Verlaufskurve nach Anmeldung über die Routen sichtbar. Dateien: `70-tor3-oberflaeche.txt`, `70-…-belege.json`

**8. Kandidatenaufschlüsselung — erfüllt.** Lauf 20: **172 = 48 abgelehnt + 1 angenommen + 3 erzeugt + 107 leer + 4 probe + 5 überlebt + 4 verhandlung**; Ablehnungen 48 = 10 Kernmaß unverändert + 10 Diff nicht anwendbar + 9 Pareto/Regression + 9 Wiederholung + 5 Grenzmaß + 3 sonst + 2 Nische schnell. Lauf 17: **245 = 69 + 5 + 3 + 156 + 11 + 1**; Ablehnungen 69 = 27 + 16 + 9 + 8 + 5 + 2 + 2. Beide gehen auf, Kategorien unverändert aus Phase 2. Lauf 13 (Phase 2) geht auf 470 auf; die fehlende Eins war K1159. Datei: `65-tor3-zerlegungen.txt`

**9. Verlaufskurven beider Werke — erfüllt.** `logmuehle` (Lauf 17): Kernmaß −13 → 0, Tests 56 → 62; Laufzeiten am Ende ausgabe 10,25 / filtern 24,71 / lesen 14,83 / zaehlen 11,00 ms. `lagerhaus` (Läufe 16, 18, 19, 20; verworfene Läufe markiert, weil ihr Schnappschuss Ausgang des nächsten war): Kernmaß durchgehend 0, Tests 101 → **104**, `formeln` 132,28 → **1,26 ms** (−99 %), `preise` 91,58 → **12,89 ms** (−86 %). Dateien: `kurve-lagerhaus.svg/.txt`, `kurve-logmuehle.svg/.txt`

---

Fassung 5 gelesen, vollständig; Fassung 4 ist ersetzt. Deine drei anderen Lösungen sind schärfer als meine Vorschläge — besonders, dass die Artgedächtnis-Zeile stehen bleibt und stattdessen das Gedächtnis umgebaut wird; ein Pflichtfeld hätte Scheinbegründungen erzeugt.

Ein Fehler von mir, den v5 aufdeckt: Der `logmuehle`-Verfassungsentwurf **lag dem Bericht nicht bei**. Er existiert (`verfassungen/logmuehle.md`, 8 Sätze), ich habe ihn nur verwiesen statt abgedruckt — damit konntest du ihn nicht bestätigen. Kommt in den Nachlaufbericht, vollständig im Text.

**Nachlauf zu Phase 3** nach Abschnitt 8, Budget 10 € hart, Ordner `laeufe/biotop-phase-3-nachlauf/`, sieben Punkte: Artgedächtnis auf Muster umstellen und beide Werke nachabstrahieren (dann Torzeile erneut messen), Doppelungsschlüssel auf die Behauptung und Tor 2 Zeile 8 neu messen, Archivierung nach der neuen Zeile, Projektgedächtnis-Differenz an den drei strittigen Fällen entscheiden, Generation minus eins und Fund-Neubewertung als Organe, Gate-Ausnahme für Abbrüche, Verfassungsentwurf abdrucken. Zwischenbericht-Pflicht vor jedem Sitzungsende ist gesetzt.

Ich fange an und melde mich beim ersten Zwischenstand.
```

### V0225 · 19.09.2026 20:14:46 CEST · Philipp · Nachricht id 2234 · Sitzung `20260918_225920_3e614670` · 595 B

```text
Teil 1 stimmt Zahl für Zahl mit dem Bericht überein, den ich selbst geholt habe — Phase 3 ist abgeschlossen, keine Nachfragen. Ein Punkt fehlt in deiner Aufzählung der Nachlaufarbeiten: Laufzeiten werden ab Fassung 5 als Median aus drei Durchläufen gemessen, nie als Einzelwert (3.5) — das ist eine eigene Regel neben der Rauschmessung, die in „Generation minus eins" steckt, und ohne sie sterben Kandidaten weiter am Messrauschen statt an der Sache. Sonst unverändert: sieben Punkte, Budget 10 € hart, Ordner laeufe/biotop-phase-3-nachlauf/, Zwischenbericht vor jedem Sitzungsende.
```

### V0226 · 19.09.2026 20:15:00 CEST · Hermes-Zwischentext · Nachricht id 2235 · Sitzung `20260918_225920_3e614670` · 280 B

```text
Richtig, das ist eine eigene Regel — mein Messgerät nimmt derzeit das **Minimum** aus drei Läufen, nicht den Median. Das ist genau die Stelle, an der Ausreißer nach unten den Bestwert künstlich drücken und spätere Kandidaten am Rauschen sterben lässt. Ich fange damit an.
```

### V0227 · 19.09.2026 20:15:16 CEST · Hermes-Zwischentext · Nachricht id 2239 · Sitzung `20260918_225920_3e614670` · 129 B

```text
Jetzt prüfe ich, ob es weitere Stellen gibt, die Laufzeiten per Minimum zusammenfassen (Zeilen 309/314 aus der früheren Suche).
```

### V0228 · 19.09.2026 20:16:15 CEST · Hermes-Zwischentext · Nachricht id 2247 · Sitzung `20260918_225920_3e614670` · 77 B

```text
Jetzt die gemessene Rauschtoleranz je Bereich (F5 3.5) statt der festen 15 %.
```

