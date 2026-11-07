# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 009 von 054

- Einträge V0090 bis V0091. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0090 · 19.09.2026 12:39:25 CEST · Philipp · Nachricht id 1393 · Sitzung `20260918_225920_3e614670` · 56053 B · Stück 2 von 2

```text
- Übungswerk, Phase 1 Nachlauf (Läufe 6–10, eine Nische, schwerer Ankläger): **gemessen 1,79 €** für 542 Aufrufe; davon 27 schwere Aufrufe (5 %) = 0,65 € (36 %). Ein einzelner Lauf mit einer Nische und schwerem Ankläger: gemessen 0,3–0,75 €.
- Übungswerk, Phase 2 (vier Nischen, voller Ankläger, Generation 0): **gemessen 1,91 €** für drei Läufe, 1.190 Aufrufe; Hauptlauf 1,15 € für 14 Generationen mit 32 Kandidaten je Generation, 0 schwere Aufrufe (Schätzung 2–8 € war zu hoch).
- Phase 3 (zwei Übungswerke, Mentor, Jury, Sättigung, Oberfläche): Schätzung 3–10 €; Budget 15 €, hart.
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
- Immunisierung: n bestätigte Fehler = n Tests im Werk (Liste mit Dateipfaden); Doppelungsanteil ausgewiesen und unter 20 % aller Angriffstests; nach keiner angenommenen Generation ein fehlschlagender Test im Werk (0 von n).
- Verhandlung: mindestens 1 Generation, in der zwei Bereiche eine Vertragsänderung gemeinsam bestanden haben, protokolliert. (Fassung 4: Diese Zeile prüft nur den Mechanismus; die eingeschleuste Vertragsprobe erfüllt sie. Der Nachweis, dass der **Schwarm selbst** eine sinnvolle Vertragsänderung durchbringt, ist am Übungswerk nicht erzwingbar — dort gibt es keine Schnittstelle, die sich ändern sollte — und steht in Tor 4.)
- Verlaufskurve des Hauptlaufs mit Endtestbestand beigefügt (3.5).

**Stand Phase 2 nach Lauf 13 (Wertung Chat-Claude, 19.09.2026):** **10 von 11.** Zeile 7 nicht erfüllt — das Probenpaar K1157/K1158 bestand die Vertragsprüfung, brachte 0 Kernmaß und wurde nach 3.5 verworfen; „angenommen" war zu „bestanden" umgedeutet. Alle übrigen Zeilen bestanden; Zeile 9 erfüllt wie geschrieben. Gehobenes Werk: Lauf 13 Generation 13, 99 von 99 Tests, Kernmaß 0, `lager` 140 → 5 ms. Kosten 1,91 € von 10 €.

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
- Jury: Zwischen zwei Kandidaten, die alle harten Maße bestehen und gleiches Kernmaß haben, entscheidet die Jury aus mindestens drei Modellen verschiedener Hersteller; Beleg: 1 Fall mit drei Begründungen, Einstimmigkeit nachgewiesen; 1 Fall ohne Einstimmigkeit → kein Urteil, protokolliert.
- Geschmacksgedächtnis, Mechanik (Fassung 4): Philipps echte Entscheidungen gibt es erst ab Phase 4. Prüfung mit versiegelter Regel — Hermes hinterlegt vor dem Lauf eine Entscheidungsregel (versiegelt, Prüfsumme), erzeugt danach 30 Freigaben/Ablehnungen nach dieser Regel; das Gedächtnis lernt aus den ersten 20 und sagt von den restlichen 10 mindestens 7 richtig voraus. Ausdrücklich gekennzeichnet als Mechanikprüfung, nicht als Nachweis über Philipps Geschmack.
- Archivierung: Offene Funde nach 5 Generationen archiviert (Zahl archiviert / gesamt), 0 archivierte Funde in Kammerläufen danach.
- Oberfläche: Für jedes Bedienelement Dateipfad und Zeile der Stelle, die es liest oder schreibt (vollständige Liste; ein Element ohne Stelle = Tor nicht bestanden); Zugriff nur mit Anmeldung (Aufruf ohne Token → 401, belegt); Kostenstand und Kurve sichtbar.
- Kandidatenaufschlüsselung jedes Laufs geht auf die Gesamtzahl auf (Abschnitt 9).

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

*Ende des Dokuments. Fassung 4, 19.09.2026 (nach Phase 2). Fassungen 1 bis 3 sind durch diese Fassung ersetzt; die jeweils höchste Fassung gilt. Fortschreibung als Fassung 5 bei grundlegenden neuen Erkenntnissen.*


Phase 2 ist mit 10 von 11 gewertet — Zeile 7 verlangt „angenommen und im Werk", das Probenpaar K1157/K1158 kam nie ins Werk; lies INFINITE-EVOLUTION-BIOTOP-Masterprompt-v4.md vollständig, Fassung 3 ist ersetzt, das Änderungsverzeichnis oben nimmt deine drei Funde auf (KEIN VORSCHLAG neutral, äquivalente Mutanten vorab belegt, offene Funde archivieren) und korrigiert das Grenzmaß auf den Bestwert des Laufs, die Norm-Regel auf alle neuen Tests mit explizitem Verweis, und Verfassungssatz 2 auf „jede Messgerätänderung ist ein neuer Lauf". Auftrag: zuerst die Nachprobe zu Zeile 7 nach Abschnitt 8 (Vertragsänderung mit dadurch ermöglichter Fehlerbehebung, Kernmaß > 0, im Werk; dazu die Zerlegung von Lauf 13 auf 470 aufgehen lassen), erst danach Phase 3 „Gedächtnis, Mentor, Oberfläche" mit zweitem Übungswerk und allen elf Torzeilen, Budget 15 € hart. Abschlussordner unter laeufe/biotop-phase-3/ mit Verlaufskurven beider Werke; Endmeldung mit Abholadresse und Prüfsumme.
```

### V0091 · 19.09.2026 12:42:22 CEST · Hermes-Zwischentext · Nachricht id 1246 · Sitzung `20260918_225920_3e614670` · 79 B

```text
Ich lese zuerst die Umgebung: Vorgängerprojekt, Schlüssel, Docker, Werkzeuge.
```

