# BIOTOP-LAGE-01 · Fassung 2 · `GLOSSAR-TEIL2-01.md` (FK50, Nachtrag Hermes)

- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST. Verfasser: Hermes.
- **Warum dieser Nachtrag:** Die Prüfung nach Abschnitt 7.3 (R215) fand 32 Begriffe aus einer Prüfliste von 78 Fachbegriffen in LAGE und TORE, die in GLOSSAR-TEIL1-01.md fehlen. Hier stehen sie, dazu Begriffe aus LAGE-TEIL1-01.md. Nicht aufgenommen sind drei Begriffe mit 0 Treffern in LAGE und TORE (Laufbudget, Höchstfall, Verfälschungskappe) und drei, die in TEIL1 schon unter anderem Namen stehen:
  - „Neutralrückgabe“ → „Neutralzähler“;
  - „rote Spezifikation“ → „Spezifikation (rote)“;
  - „Gedächtnis (Hermes)“ → Eintrag „Gedächtnis“ unten.
- **Kennzeichnung:** „Erklärung Hermes“ heißt: Die Bedeutung ist aus dem Gebrauch in den genannten Stellen abgeleitet. Eine Definition im Wortlaut gibt es dort nicht.
- **Glossar Teil 1:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/GLOSSAR-TEIL1-01.md

| Begriff | Bedeutung in einem Satz | Fundstelle |
|---|---|---|
| Abweichungsquote (Ansage↔Ausführung) | Der Anteil der Angriffstests, deren Ausführung von der vorab angesagten Behauptung des Anklägers abweicht; gemessen in VB1 mit 9 von 11 und im T3-Zähler V9 mit 19 von 20 Zeilen, ohne eigene Torzeile. | TORE-TEIL4 FK28; Auftrag §6 FK28 |
| Aufwärmung | Ein Vorlauf vor einer Laufzeitmessung, der selbst nicht zählt; „keine Aufwärmung“ zählt v8 zu den Messgerätfehlern aus T3 (Erklärung Hermes). | v8 Z. 461; TORE-TEIL3 §2 |
| Befund G | Ein stiller Durchlass, den S1c am Ende von Runde 6 gemessen hat: Eine geänderte Funktion schreibt in ein fremdes Modul oder ruft dort Schreibendes, und aegis urteilt „überlebt“ ohne Enthaltung. Offen, nur als rote Spezifikation `test_w_g_*`. | R175; LAGE-TEIL1 „Endstand Runde 6“ |
| Bestandsaufnahme | Der Auftrag vom 20.09., der den Gesamtstand des Biotops mit 49 Befundgruppen (A01–A33, B-01–B-24, C01, C02) aufnahm; laut id 4317 abgenommen. | LAGE-TEIL3 FK23; TORE-TEIL3 §1 |
| eng abgenommen | Eine Abnahme mit ausdrücklich begrenztem Geltungsbereich, etwa Vorbedingung 1, Läufe 22–25: „ABGENOMMEN … Geltungsbereich ist eng“. | LAGE-TEIL3 FK23; Auftrag §6 FK23 |
| Fehlalarm | Ein Befund des Messgeräts oder einer Regel, der keinen echten Fehler zeigt, etwa die Regel `detect-object-injection`; M2(b) hatte in Runde 6 zwei Fehlalarme (E, F). | TORE-TEIL3 §2; R175 |
| `detect-object-injection` | Eine Regel des Sicherheitsprüfers im T3-Maß, die bei Objektzugriffen anschlägt; nach Q6/Q7 machte sie das Maß „optimierbar ohne Sache“ und wurde deshalb geeicht. | TORE-TEIL3 §2 |
| Gedächtnis (Hermes) | Hermes' dauerhafte Ablage im Prüfkanal `laeufe/gedaechtnis/` (STAND-nn, REGELN-nn, UNTERBAU-nn); nur HERMES-1 schreibt dorthin, zuletzt STAND-01 am 20.09., jetzt STAND-02. | Auftrag Anhang WS19; LAGE-TEIL2 |
| Grosswerk | Ein erzeugtes Probewerk der Runde 5 in T4-Größe: 6 Module, 30 Funktionen, 126 Zeilen. Daran wurde die Kappe der Verfälschungsläufe gemessen. | LAGE-TEIL3 FK25 |
| Harness | Das Prüfgerüst, das einen Kandidaten mit festen Eingaben ausführt und vergleicht, etwa „Harness S1“ bei der doppelten Prüfung der Schwäche S1 (Erklärung Hermes). | TORE-TEIL3 §2 |
| Inhaltsbefund (als Absturz) | Ein Messgerätfehler aus T3: Das Messgerät wertete einen inhaltlichen Fehler des Werks als Absturz des Laufs, in zwei Bauarten an 12 Stellen. | TORE-TEIL3 §2; v8 Z. 461 |
| Laufweg | Ein Beleg, der durch den echten Ablauf eines Laufs geht (Organe wie im Lauf verdrahtet), im Unterschied zu einem Test nur am Modul oder Organ. | TORE-TEIL3 §2–§3; LAGE-TEIL3 |
| M2(b) | Die Regel aus Runde 6: Ist eine direkt geänderte Einheit nicht beobachtet, stellt der Verhaltensvergleich zurück. Gebaut von S1b, von S1c um E (neue Funktionen) und F (Selbstaufruf) ergänzt. | R175; CHRONIK C057 |
| Messgrenze | Eine vorab gesetzte Untergrenze, unter der eine Torzeile als „ungemessen“ gilt, zum Beispiel „ungemessen unterhalb von 20 erzeugten Tests“ vom 20.09. Sie steht nicht in v7 oder v8. | TORE-TEIL1; TORE-TEIL4 L2, W5 |
| Nachsteuerung | Eine Nachricht von Chat-Claude, die Philipp während eines laufenden Auftrags weiterleitet und die den Auftrag ergänzt, hier am 25.09. um 17:08:20 (id 24300). | START-02 A |
| Probewerk | Ein Werk, das nur für Proben erzeugt wird und keinen Betriebszweck hat, etwa `probewerk` in `tests/test_vor_t4_03.py` oder `lagerhaus-ohne-tests`. | LAGE-TEIL3 FK25 |
| R02 | Der Kassenzweig der Reparatur 02: eine Kopie des Stamms nach Lauf 25 mit eigenem Lauf 26 (Pflichtvorspann, 0 €). | INVENTAR-TEIL2 Abgleich 2, 8 |
| Rohbeleg | Die Aufzeichnung eines ausgeführten Befehls dieses Auftrags mit Wortlaut und vollständiger Ausgabe, nummeriert R1, R2 …, erzeugt von `arbeit/rb.py`. | Auftrag §8; ROHBELEGE-VERZEICHNIS-03.txt |
| Selbstevolution | Das Biotop bearbeitet sich selbst; ausgeschlossen, außer Philipp legt es als Werk ein. | Auftrag Anhang WS02; LAGE-TEIL2 |
| Speicherwerk | Ein Prüfwerk in `tests/speicherwerk.py` (187 Zeilen) für Proben am Zwischenspeicher-Verhalten (Erklärung Hermes nach Name und Nutzung). | LAGE-TEIL3 FK25 |
| STAMM | Der Hauptzweig der Kasse `/root/biotop/daten/biotop.db` mit den Läufen 1–25; VB1, R02 und T3 sind Kopien davon nach Lauf 25. | INVENTAR-TEIL2 Abgleich 2 |
| Stichzeitpunkt | Der Zeitpunkt, auf den sich Sicherung und Offenlegung beziehen: 25.09.2026 17:29:59 CEST, das Ende des Baus S1c. | START-02; LAGE-TEIL1 |
| Übergabe | Die Datei `UEBERGABE.md` eines Arbeitsordners mit Stand und nächsten Schritten, damit ein Nachfolger oder ein späterer Turn weiterarbeiten kann. | LAGE-TEIL4, TEIL6 |
| VB1 | Der Kassenzweig der Vorbedingung 1 aus Phase 4 (`/root/phase-4-vorbedingung-1/privat/biotop.db`), eine Kopie des Stamms nach Lauf 25 mit eigenem Lauf 26. | INVENTAR-TEIL2 Abgleich 2, 8 |
| Verdichtung | Das automatische Zusammenfassen einer langen Sitzung durch Hermes, damit sie weiterlaufen kann; seit 25.09. um 00:27 über OpenRouter, mit Kosten. | ENTSCHEIDUNGEN P-13; START-02 E |
| Vorentscheidung | Eine Entscheidung, die Chat-Claude vorab trifft und die Philipp bestätigen soll; nie bestätigte Vorentscheidungen führt das Register gesondert. | ENTSCHEIDUNGEN-TEIL2 §17.3; Auftrag FK17 |
| Wächter (Zwischenbericht-Wächter) | Ein Cron-Job von Hermes, der jede Minute die Runden eines Turns zählt und bei 110 und 140 von 150 einen Zwischenbericht in den Prüfkanal schreibt. | START-02 D (A3); LAGE-TEIL1 FK07 |
| Weißraum | Leerzeichen, Tabulatoren und Zeilenumbrüche im Code; eine Formvariante, an der die Schwäche S1 und Proben der Runden 2–6 hängen. | TORE-TEIL3 §2; GLOSSAR-TEIL1 „Formvariante“ |
| Zielbild | Das Ziel des Biotops: Es versteht jedes eingelegte Werk von A bis Z, hebt es als Ganzes auf die nächste Stufe und erkennt, wenn etwas schon bestmöglich ist. | Auftrag Anhang WS02; LAGE-TEIL2 |
| Zweig (Kassenzweig) | Eine eigene Kopie der Kasse mit eigener Laufzählung: STAMM, VB1, R02 und T3. Die Laufnummer allein ist deshalb keine eindeutige Kennung. | INVENTAR-TEIL2 Abgleich 2, 8 |
