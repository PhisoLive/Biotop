# Auftrag BIOTOP-LAGE-01 · Fassung 2 — Biotop sichern und vollständig offenlegen

**Für:** Hermes auf HERMES-1 (dort liegt das Biotop) · **Von:** Chat-Claude im Auftrag von Philipp · **Entscheider:** Philipp · **Erstellt:** 25.09.2026

**Fassung 2 ersetzt Fassung 1.** Hast du Fassung 1 schon begonnen, verwirfst du nichts. Du führst `laeufe/biotop-lage-01/` mit der nächsten freien Nummer weiter und vermerkst in der Einstiegsdatei, was unter Fassung 1 entstanden ist.

**Verhältnis zum Masterprompt:** Dieser Auftrag ergänzt die gültige Fassung und ändert sie nicht. Widerspricht er ihr, gilt für diese Arbeit dieser Auftrag, und du schreibst den Widerspruch hin. Eine jüngere Anweisung Philipps geht beidem vor.

**Kennungen dieses Auftrags:** WS01–WS19 (Chat-Claudes Wissensstand), I1–I8 (Inventare), FK01–FK50 (Fragenkatalog), LU01 … (Lücken), R1 … (Rohbelege). Sie gehören nur zu diesem Auftrag. Verwechsle sie nicht mit Kennungen des Biotops, etwa Kernmaß F2, Befund S1, Bauteile A–C, Tore 1–4, Testwerke T3–T6, Generation 0 oder Masterprompt-Fassungen v1–v7. „Abschnitt n" meint immer diesen Auftrag; eine Stelle im Masterprompt heißt „Masterprompt Abschnitt n".

Lies den ganzen Auftrag, bevor du anfängst.

**Änderungsverzeichnis**
- Fassung 2 (25.09.2026): Der Zeitraum reicht ausdrücklich bis zum Stichzeitpunkt, weil bis zum 25.09. gearbeitet wurde. Neu sind:
  - Bestandsaufnahme mit Abgleich über unabhängige Quellen, Tagesbilanz und Quellenabdeckung (Abschnitt 5)
  - Fragenkatalog FK01–FK50 mit Zieldatei je Frage (Abschnitt 6), darunter Kurzlage, Entscheidungsregister, Soll-Ist-Abgleich, Verfassungen im Wortlaut, Fähigkeitsstand und Berichtigungen
  - Vollständigkeitsprüfung mit Antworttafel und Lückenliste (Abschnitt 7)
  - Rohlisten zum Nachrechnen, Wiederherstellungsanleitung, Umgang mit einem laufenden Lauf, Schlussmeldung in Teilen, eindeutige Kennungen, Weg für Nachfragen (Abschnitt 11)
- Fassung 1 (25.09.2026): erste Fassung.

---

## 0. Lage und Ziel

Der letzte Arbeitschat zwischen Philipp und Chat-Claude wurde abgebrochen. Chat-Claudes gesicherter Wissensstand endet am 21.09.2026 früh (Anhang). Am Biotop wurde danach bis zum 25.09.2026 weitergearbeitet. Alles aus dieser Zeit fehlt ihm.

**Stichzeitpunkt** ist der Beginn dieses Auftrags. Läuft zu Beginn ein Biotop-Lauf, ist der Stichzeitpunkt dessen Ende. Alles bis zum Stichzeitpunkt gehört lückenlos dazu.

Zwei Ziele, in dieser Reihenfolge:
1. **Sichern.** Der gesamte Stand des Biotops ist so gesichert, dass er nach einem Totalausfall wiederherstellbar ist. Das weist eine ausgeführte Wiederherstellungsprobe nach; eine Behauptung reicht nicht.
2. **Offenlegen.** Chat-Claude kennt danach den gesamten Stand bis zum Stichzeitpunkt: was geschah, was gilt, was entschieden ist, was gemessen ist, was offen ist und wie es laut Masterprompt weitergeht. Er braucht dafür keine Rückfrage an dich.

**Vollständigkeit wird nachgewiesen, nicht versichert.** Das geschieht auf zwei Wegen:
- Inventare aus unabhängigen Quellen werden gezählt und gegeneinander abgeglichen. Für jede Quelle steht fest, welchen Zeitraum sie abdeckt (Abschnitt 5).
- Eine Antworttafel zeigt für jede Frage dieses Auftrags, wo sie beantwortet ist (Abschnitt 7).

Was trotzdem offen bleibt, steht in der Lückenliste. Eine Lücke, die dort nicht steht, gilt als verschwiegen.

Dieser Auftrag baut nichts, repariert nichts und wertet keine Tore.

## 1. Vorentscheidungen von Chat-Claude

Diese Punkte hat Chat-Claude gesetzt; Philipp hat sie nicht bestätigt. Er kann jeden davon streichen oder ändern. Sie gelten nicht als seine Entscheidung.
- Umfang und Rangfolge der Sicherung wie in Abschnitt 4, einschließlich `/root/.hermes/` ohne Geheimnisdateien.
- Keine Änderung am Repository, auch kein Sicherungscommit. Das Archiv sichert auch nicht eingecheckte Dateien.
- Ein zweiter Sicherungsort wird nur benutzt, wenn er bereits eingerichtet und nicht öffentlich ist.
- Ein laufender Lauf wird nicht angehalten. Gesichert und gezählt wird nach seinem Ende.
- Die Chronik beginnt am 18.09.2026 mit dem Neuaufbau und ist ab dem 21.09.2026 lückenlos.
- Ordnername `laeufe/biotop-lage-01/`, Dateiaufteilung nach Abschnitt 8, Budget für bezahlte Modellaufrufe 0,00 €.

## 2. Harte Regeln

1. **Nur sichern, lesen, berichten.** Am Biotop änderst du nichts: nicht Code, Tests, Messgerät, Verfassungen, Gedächtnisse oder Masterprompt. Was dir auffällt, kommt in die offenen Punkte, nicht in den Code.
   - Du legst nur an drei Stellen etwas an: in `/root/sicherung/biotop-lage-01/`, im Abschlussordner und in `laeufe/gedaechtnis/`.
   - Sonst änderst du nichts, auch nicht Caddy, `robots.txt` oder die Website. Blockiert etwas den Abruf, meldest du es mit Vorschlag.
2. **Nichts löschen, nichts aufräumen, nichts überschreiben**, auch nicht, um Platz zu schaffen. Die Aufräumregel für Arbeitsdateien ruht während dieses Auftrags.
3. **Keine neuen Biotop-Läufe, keine bezahlten Modellaufrufe.**
   - Lokale Tests ohne Modellaufruf sind erlaubt. Ist unklar, ob ein Test ein Modell aufruft, führst du ihn nicht aus und schreibst den Grund hin.
   - Die Abfrage der OpenRouter-Nutzungsanzeige ist kein Modellaufruf und erlaubt.
   - Einen laufenden Lauf hältst du nicht an (Abschnitt 3).
4. **Kein Geheimnis und keine Kundendaten in den Prüfkanal.** Geheimnisse sind API-Schlüssel, Kennwörter, Token, private Schlüssel und die Inhalte von `.env` und `auth.json`. Sie stehen in keiner Datei des Abschlussordners und in keiner Meldung. An ihrer Stelle steht `[GESCHWÄRZT]` mit Fundort. Inhalte anderer Vorhaben aus der Sitzungsdatenbank bleiben draußen.
5. **Nie überschreiben.** Jede Datei im Abschlussordner trägt eine Nummer (`-01`). Ein neuer Stand bekommt die nächste Nummer, gültig ist die höchste. Grund: Chat-Claudes Abrufweg liefert überschriebene Dateien im alten Stand.
6. **Nachweis am Ergebnis.**
   - „Ausgeführt" schreibst du nur mit Rohbeleg: Befehl und vollständige Ausgabe in `ROHBELEGE`, Verweis R1, R2 … Ohne Rohbeleg heißt es „gelesen, nicht ausgeführt".
   - Zahlen statt Adjektive. Jede Zahl trägt Bezugsgröße und Quelle.
   - Jede Zahl ist gekennzeichnet als *abgelesen* (Datei oder Befehl) oder *gerechnet* (mit Rechenweg).
7. **Vollständigkeit über Mengen.** Jede Menge zählst du aus jeder Quelle, die sie führt, und gleichst die Zählungen ab: Läufe, Aufträge, Meldungen, Fassungen, Werke, Abschlussordner, Commits und Kosten. Jede Abweichung wird erklärt oder kommt in die Lückenliste. Eine Zahl aus nur einer Quelle trägt den Vermerk „eine Quelle".
8. **Laut scheitern.** Was du nicht findest, nicht prüfen kannst oder nicht weißt, steht als `NICHT GEFUNDEN`, `NICHT AUSGEFÜHRT` oder `UNBEKANNT` da. Nichts davon wird weggelassen. Eine Prüfung ohne Gegenstand meldet das, statt zu bestehen.
9. **Keine Wertung, keine Umdeutung.** Du wertest keine Tore und deutest keinen Maßstab um. Je Torzeile lieferst du Messwert, Grenze, Bezugsgröße, Quelle und Datum. Die Wertung macht Chat-Claude, entscheiden tut Philipp.
10. **Quelle vor Gedächtnis.** Belege kommen aus Dateien, Protokollen, der Kasse `biotop.db`, der Sitzungsdatenbank, git und dem Prüfkanal. Was du nur erinnerst, kennzeichnest du mit „erinnert, nicht an Datei belegt".
11. **Kennungen bleiben.** Bestehende Kennungen für Läufe, offene Punkte, Befunde und Fassungen übernimmst du unverändert. Neue bekommen neue Kennungen im selben Schema. Gibt es für dieselbe Sache mehrere Nummernkreise, lieferst du eine Zuordnungstafel.
12. **Auslegungen kennzeichnen.** Musst du eine Stelle auslegen, ob in diesem Auftrag, im Masterprompt oder in früheren Aufträgen, schreibst du „Auslegung Hermes" und deine Lesart hin.
13. **Wortlaut vor Zusammenfassung.** Bei Masterprompt, Verfassungen, Entscheidungen und Aufträgen lieferst du den Wortlaut. Eine Zusammenfassung ersetzt ihn nicht.
14. **Weiterarbeiten statt anhalten.** Du hältst für keine Frage an; Fragen sammelst du in FK47.
    - Entscheidungen im Rahmen dieses Auftrags triffst du selbst, kennzeichnest sie als „Entscheidung Hermes" und arbeitest weiter.
    - Vorschläge kennzeichnest du als „Vorschlag Hermes". Sie gelten nicht als Entscheidung.
    - Der einzige Grund anzuhalten: Schritt 1 findet das Biotop nicht.
15. **Nicht Gegenstand** ist deine eigene Modell- und Anmeldelage. Du wertest sie nicht aus, berichtest sie nicht und änderst sie nicht. `/root/.hermes/` wird trotzdem mitgesichert (Abschnitt 4).
16. Alle Zeitangaben tragen Datum, Uhrzeit und Zeitzone.

## 3. Reihenfolge

**Schritt 1 — Anlegen und melden, vor allem anderen**
- Prüfe, dass das Biotop unter `/root/biotop` liegt. Liegt es woanders, ermittelst du den Pfad und schreibst ihn hin. Findest du es gar nicht, meldest du das sofort und hältst an. Dann ist der Auftrag bei der falschen Instanz angekommen.
- Stelle fest, ob gerade ein Biotop-Lauf oder ein anderer Biotop-Prozess läuft (Prozesse, Zeitgeber, Cron-Jobs): was, seit wann, erwartetes Ende. Das Ergebnis kommt als Rohbeleg dazu.
- Lege den Abschlussordner `laeufe/biotop-lage-01/` an der festen Abrufstelle im Prüfkanal an, dort, wo alle bisherigen Biotop-Ordner liegen. Stand 20.09.: `/var/pruefkanal/oeffentlich/_akte/<kennung>/laeufe/`. Ist die Abrufstelle umgezogen, nimmst du die gültige und schreibst sie hin.
- Lade sofort die Einstiegsdatei hoch, `START-01.md` oder die nächste freie Nummer. Sie enthält Kennung, Fassung 2, Stichzeitpunkt (oder „folgt nach Laufende"), Status `IN ARBEIT`, laufender Lauf ja/nein und den Plan in fünf Zeilen. Danach schickst du Meldung 1 (Abschnitt 9).
- Arbeitsverzeichnis und Ablage der Sicherung ist `/root/sicherung/biotop-lage-01/`.

**Läuft ein Lauf, hältst du ihn nicht an.** Bis zu seinem Ende arbeitest du an dem, was er nicht berührt: Verlauf im Wortlaut, Masterprompt, Verfassungen, Entscheidungen, Glossar, Aufbau. Die Prüfsummenliste VORHER, die Sicherung und die Inventare beginnen erst nach seinem Ende. Sein Ende ist der Stichzeitpunkt; du trägst ihn in der nächsten Einstiegsdatei nach. Endet er nicht in dieser Sitzung, gilt die Regel für Zwischenstände.

**Schritt 2 — Sichern** nach Abschnitt 4. Zuerst kommt die Prüfsummenliste VORHER: SHA-256 jeder Datei unter `/root/biotop` ohne `.git/`, mit Dateianzahl, als Rohbeleg. Sie beweist am Ende, dass du nichts verändert hast.

**Schritt 3 — Bestandsaufnahme und Abgleich** nach Abschnitt 5.

**Schritt 4 — Offenlegen:** Fragenkatalog nach Abschnitt 6, Dateien nach Abschnitt 8.

**Schritt 5 — Vollständigkeitsprüfung** nach Abschnitt 7.

**Schritt 6 — Abschließen**
- Prüfsummenliste NACHHER über dieselbe Menge. Der Unterschied zu VORHER muss leer sein. Schreib die Dateianzahl beider Listen hin. Ist der Unterschied nicht leer, erklärst du jede Abweichung einzeln.
- Geheimnissuche mit Gegenprobe (Abschnitt 8).
- Danach die abschließende Einstiegsdatei mit der höchsten Nummer, zuletzt `DATEIEN-NN.txt` und `PRUEFSUMME-ORDNER-NN.txt`.
- Den neuen Stand trägst du in dein Gedächtnis ein: `laeufe/gedaechtnis/STAND-nn.md` mit der nächsten freien Nummer und einem Verweis auf den Abschlussordner.
- Abrufprobe (Abschnitt 8). Ihre Ausgabe lädst du als `ABRUFPROBE-NN.txt` hoch.
- Meldung 2 (Abschnitt 9).

**Zwischenstände.** Vor jedem Sitzungsende, jeder längeren Pause und bei jedem Abbruch lädst du eine neue Einstiegsdatei mit der nächsten Nummer hoch. Sie sagt, was fertig ist, was fehlt und wo du stehst. Dazu schickst du Meldung 2 mit Status `TEILWEISE` oder `ABGEBROCHEN`. Ein Abbruch ohne abrufbaren Stand ist das schwerste Versagen dieses Auftrags.

## 4. Sichern

**Umfang in Rangfolge.** Reicht der Platz nicht für alles, sicherst du von oben nach unten und meldest, was fehlt.
1. `/root/biotop` vollständig samt `.git/`: Quelltext, Tests, Messgerät, Konfiguration, Verfassungen, Art- und Projektgedächtnis, Protokolle, Kasse `daten/biotop.db`. Abhängigkeitsordner (`node_modules`, `.venv`, Zwischenspeicher) bleiben draußen. Alle Sperr- und Anforderungsdateien kommen mit, damit die Abhängigkeiten wiederherstellbar sind.
2. Alle Masterprompt-Fassungen bis zur gültigen und alle weiteren Auftragsdateien zum Biotop, wo immer sie liegen.
3. Alle Biotop-Ordner im Prüfkanal (`laeufe/biotop-*`) und `laeufe/gedaechtnis/`.
4. Die Sitzungsdatenbank `/root/.hermes/state.db`.
5. Den Rest von `/root/.hermes/` ohne Geheimnisdateien.

**Vorgehen**
1. Plattenplatz vorher messen (`df -h`, Größe jedes Umfangsteils), als Rohbeleg.
2. Repository-Stand festhalten, nicht verändern: `git log -1`, `git status --short` und die Zahl der nicht eingecheckten Dateien, als Rohbeleg.
3. Datenbanken nie als laufende Datei kopieren.
   - Sichere sie mit `sqlite3 <db> ".backup '<ziel>'"` oder mit Pythons `Connection.backup`.
   - Prüfe jede Kopie mit `PRAGMA integrity_check`. Das Ergebnis `ok` kommt als Rohbeleg dazu.
   - Im Archiv ersetzen diese Kopien die Datenbankdateien am selben Pfad.
4. Archiv `biotop-sicherung-<JJJJ-MM-TT>-01.tar.gz` mit `tar` packen (zip ist auf dem Server nicht installiert).
   - Geheimnisdateien (`.env`, `auth.json`, Schlüsseldateien) kommen nicht hinein.
   - Im Bericht führst du sie nur mit Pfad, ohne Inhalt, damit man sie bei einer Wiederherstellung von Hand ergänzen kann.
   - Größe und SHA-256 des Archivs festhalten.
5. Das Archiv gilt trotzdem als vertraulich, weil die Sitzungsdatenbank eingefügte Geheimnisse enthalten kann. Es kommt nie in den Prüfkanal und an keinen öffentlichen Ort.
6. **Wiederherstellungsprobe:**
   - Beim Packen erzeugst du eine Prüfsummenliste aller eingepackten Dateien (Manifest).
   - Dann entpackst du das Archiv in ein leeres Verzeichnis, bildest dieselbe Liste über den entpackten Stand und vergleichst. Schreib die Dateianzahl beider Seiten hin. Der Unterschied muss leer sein.
   - Wie du einen in sich stimmigen Stand zum Packen erzeugst, entscheidest du selbst (Entscheidung Hermes). Der Nachweis ist der Vergleich.
   - Lokale Tests ohne Modellaufruf führst du im entpackten Stand aus, falls es welche gibt.
7. **Gegenprobe:** In einer Kopie des entpackten Stands änderst du genau ein Byte einer Datei und lässt denselben Vergleich laufen. Er muss genau diese eine Datei melden. Schlägt er nicht an, ist der Vergleich wertlos, und du meldest das.
8. **Ablage:**
   - Ablage 1 ist `/root/sicherung/biotop-lage-01/`, außerhalb jedes öffentlich erreichbaren Verzeichnisses.
   - Ablage 2 ist ein zweiter, vom Server unabhängiger Ort. Du nutzt ihn nur, wenn er bereits eingerichtet und nicht öffentlich ist.
   - Ist keiner eingerichtet: keine neuen Konten, nichts Öffentliches, nichts improvisieren. Du trägst stattdessen den offenen Punkt „Sicherung liegt nur auf diesem Server" mit Vorschlag Hermes ein. Philipp entscheidet.
9. **Wiederherstellungsanleitung** in `SICHERUNG`:
   - die Befehle in Reihenfolge, von einem leeren Server bis zum lauffähigen Biotop
   - die Geheimnisse, die von Hand ergänzt werden müssen, nur mit Namen und Zielpfad, nie mit Inhalt
   - Was du davon im entpackten Stand ausgeführt hast, trägt einen Rohbeleg. Der Rest heißt „gelesen, nicht ausgeführt".

## 5. Bestandsaufnahme und Abgleich (→ `INVENTAR`, Rohlisten in `KASSE` und `LISTEN`)

Erst zählen, dann berichten. Jedes Inventar nennt Quelle, Befehl, Zeitpunkt und Anzahl.

| Inventar | Inhalt | Quellen |
|---|---|---|
| I1 Läufe | jeder Lauf seit dem ersten des Biotops: Kennung, Beginn, Ende, Werk, Phase, Aufrufe, Kosten, Ergebnisort | Kasse `biotop.db`, Protokolle, Prüfkanal |
| I2 Aufträge und Meldungen | jede Nachricht zum Biotop seit dem 18.09.: Zeitpunkt, Absender, Art (Auftrag, Anweisung, Meldung, Frage) | Sitzungsdatenbank, Auftragsdateien auf der Platte |
| I3 Abschlussordner | jeder Biotop-Ordner unter `laeufe/`: Name, Dateianzahl, Entstehungszeit, zugehöriger Lauf oder Auftrag | Prüfkanal |
| I4 Fassungen und Auftragsdateien | jede Masterprompt-Fassung und jede Auftragsdatei zum Biotop: Pfad, Datum, Größe, SHA-256 — gesucht nach Dateiname und nach Inhalt | Dateisystem |
| I5 Werke | jedes Werk (Übungs-, Test-, echtes Werk): Pfad, Art, Umfang | Dateisystem, Kasse |
| I6 Commits und Änderungen | jeder Commit seit dem 18.09. in `/root/biotop`: Kennung, Zeitpunkt, Autor, Nachricht; dazu Markierungen, Zweige, nicht Eingechecktes; jede seit dem 21.09. geänderte Datei mit Zeitpunkt und Größe | git, Dateisystem |
| I7 Gedächtnis | jede Datei in `laeufe/gedaechtnis/` mit Nummer und Datum | Prüfkanal |
| I8 Kosten | Kosten je Lauf und je Tag | Kasse, Nutzungsanzeige von OpenRouter |

**Quellenabdeckung.** Für jede Quelle steht fest, welchen Zeitraum sie lückenlos abdeckt, etwa ab wann die Sitzungsdatenbank Nachrichten führt und ob Sitzungen zurückgesetzt wurden. Ein Zeitraum zwischen dem 18.09. und dem Stichzeitpunkt, den keine Quelle abdeckt, ist eine Lücke und kommt in die Lückenliste.

**Abgleich.** Jede Abweichung wird an Ort und Stelle erklärt oder kommt in die Lückenliste (Abschnitt 7).
1. Jeder Lauf aus I1 hat eine Zeile in der Chronik und einen Abschlussordner aus I3. Fehlt einer davon, steht eine Erklärung da. Jeder Ordner aus I3 gehört zu einem Lauf oder Auftrag.
2. Die Laufnummern sind lückenlos vom ersten bis zum letzten Lauf. Jede fehlende Nummer ist erklärt.
3. Die Fassungen sind lückenlos von v1 bis zur gültigen. Jede fehlende steht als `NICHT GEFUNDEN` da. Jede Fassung, auf die irgendwo verwiesen wird, existiert.
4. Jeder Auftrag aus I2 hat einen Status: erledigt, teilweise, offen, zurückgezogen oder ersetzt.
5. Jeder Commit und jede geänderte Datei aus I6 gehört zu einem Auftrag oder Lauf der Chronik.
6. **Kosten:** Die Summe der Kasse steht gegen die Nutzungsanzeige von OpenRouter. Die Differenz in € wird erklärt, etwa durch Nutzung desselben Schlüssels außerhalb des Biotops. Ist die Anzeige nicht abrufbar, steht `QUELLE FEHLT`.
7. **Tagesbilanz** vom 18.09.2026 bis zum Stichzeitpunkt, je Tag: Aufträge, Läufe, Meldungen, Commits, Kosten. Jede Zahl kommt aus jeder Quelle, die sie führt. Ein Tag ohne Tätigkeit steht mit 0 da, aber nur, wenn eine Quelle ihn abdeckt. Sonst steht `NICHT ABGEDECKT` da.
8. **Nummernkreise:** Hat dieselbe Sache mehrere Kennungen, etwa Kassen-Kennung, Laufnummer und Ordnername, lieferst du eine Zuordnungstafel.
9. **Gegenprobe:** In einer Kopie der Inventare fügst du einen erfundenen Lauf und einen erfundenen Ordner ein. Der Abgleich muss genau diese beiden als unzugeordnet melden. Rohbeleg.

**Rohlisten zum Nachrechnen:**
- `KASSE-NN.csv`: Export der Kassentabellen mit Kopfzeile, Trennzeichen Semikolon, Zahlen mit Dezimalpunkt, ohne Geheimnisse.
- `LISTEN-NN.txt`: Laufnummern, Ordner im Prüfkanal, das Nachrichtenverzeichnis der Sitzungsdatenbank (Zeitpunkt, Absender, Sitzung, Einordnung „Biotop ja/nein", ohne Inhalt), Commits und geänderte Dateien.

## 6. Fragenkatalog

Jede Frage beantwortest du unter ihrer Kennung in der genannten Datei. Keine wird übersprungen. Gibt es nichts, steht „keine" mit Beleg. Weißt du es nicht, steht `UNBEKANNT` mit Grund.

**A — Kurzlage und aktueller Stand**
- **FK01** (`LAGE`) Kurzlage in zwölf Zeilen, je ein Satz mit Verweis auf die belegende Stelle:
  1. gültige Masterprompt-Fassung und seit wann
  2. Phase und Schritt zum Stichzeitpunkt
  3. Testwerke des Breitentests: gebaut, gelaufen
  4. Werke neuer Art, die zuletzt hintereinander keinen neuen Messgerätfehler erzeugt haben (die Regel verlangt zwei)
  5. Messgerätfehler seit dem 21.09., davon behoben und belegt
  6. natürliche Fänge der Aufnahmesperre C
  7. Abweichungsquote Ansage↔Ausführung: gemessen ja/nein, Wert
  8. Entscheidungen Philipps seit dem 21.09.: Anzahl und Verweis
  9. Werk für Phase 5 gewählt ja/nein
  10. Kosten seit dem 21.09., gegen welche Budgets
  11. was in Arbeit ist und was auf Chat-Claude oder Philipp wartet
  12. Abbrüche, Rückschritte, Löschungen oder Befunde, die frühere Abnahmen in Frage stellen
- **FK02** (`LAGE`) Was ist vom 21.09.2026 bis zum Stichzeitpunkt am Biotop geschehen? Höchstens zehn Sätze; Einzelheiten stehen in `CHRONIK`.
- **FK03** (`LAGE`) Die letzte Tätigkeit am Biotop vor diesem Auftrag: Zeitpunkt, was, auf wessen Auftrag.
- **FK04** (`LAGE`) Der letzte Auftrag zum Biotop: Datei oder Wortlaut, von wem, wann. Was davon ist erledigt, was nicht?
- **FK05** (`LAGE`) Was ist angefangen und nicht beendet? Wo steht es, was fehlt?
- **FK06** (`LAGE`) Was wartet auf Chat-Claude (Prüfung) oder auf Philipp (Entscheidung, Freigabe)? Je Punkt: was genau, seit wann.
- **FK07** (`LAGE`) Lief zu Beginn dieses Auftrags etwas, etwa ein Lauf, Prozess, Zeitgeber oder Cron-Job? Was, seit wann, wann beendet.
- **FK08** (`LAGE`) Was wurde seit dem 18.09. gelöscht, zurückgebaut, verworfen oder zurückgezogen? Je Fall: was, wann, warum, auf wessen Anweisung, und ob es wiederherstellbar ist.
- **FK09** (`LAGE`) Hat außer dir jemand am Biotop gearbeitet oder Dateien geändert, etwa HERMES-2, HERMES-3, Iolo oder Philipp direkt? Belege: Commit-Autor, Zeitstempel, Sitzungen.

**B — Verlauf**
- **FK10** (`CHRONIK`) Chronik: jeder Auftrag, jede Anweisung und jeder Lauf seit dem 18.09., lückenlos ab dem 21.09. Je Zeile:
  - Nummer und Zeitpunkt
  - Auftrag: Datei oder Kurzfassung, von wem
  - Ergebnis in einem Satz
  - Kosten und gegen welches Budget
  - vollständige Adresse des Abschlussordners
  - Status
- **FK11** (`VERLAUF`) Jeder Auftrag an dich und jede deiner Meldungen zum Biotop seit dem 21.09. im Wortlaut, zeitlich geordnet, mit Zeitpunkt und Absender. Geheimnisse sind geschwärzt, Inhalte anderer Vorhaben bleiben draußen. Was als Datei im Prüfkanal liegt, steht hier nur als Verweis mit vollständiger Adresse und SHA-256.
- **FK12** (`CHRONIK`) Jede Wertung oder Prüfung von Chat-Claude, die seit dem 18.09. bei dir angekommen ist: Datum, Gegenstand, Ergebnis und was du daraufhin getan hast. Dazu jeder Befund von Chat-Claude, den du für falsch hältst, mit Beleg.
- **FK13** (`LAGE`) Berichtigungen: jede Zahl oder Aussage, die seit dem 18.09. gemeldet und später berichtigt wurde, von dir oder durch Chat-Claude. Je Berichtigung: alt, neu, Grund.

**C — Regelwerk und Entscheidungen**
- **FK14** (`MASTERPROMPT-GUELTIG`) Welche Fassung gilt, seit wann? Ihr vollständiger, unveränderter Wortlaut, dazu Originalpfad und SHA-256 von Original und Kopie.
- **FK15** (`ENTSCHEIDUNGEN`) Fassungsverzeichnis von v1 bis zur gültigen: Datum, Pfad, SHA-256 und das Änderungsverzeichnis jeder Fassung im Wortlaut.
- **FK16** (`ENTSCHEIDUNGEN`) Jede Änderung oder Anweisung nach der gültigen Fassung, die noch in keiner Fassung steht.
- **FK17** (`ENTSCHEIDUNGEN`) Entscheidungsregister seit dem 18.09. Jede Entscheidung mit:
  - Datum
  - Wortlaut oder Kurzfassung
  - Urheber: Philipp, an Chat-Claude delegiert, Vorentscheidung Chat-Claude oder Entscheidung Hermes
  - bei einer Vorentscheidung: von Philipp bestätigt ja/nein, mit Beleg
  - Status: gilt, zurückgezogen oder ersetzt
  - Quelle

  Ausdrücklich darin: jede Vorentscheidung, die nie bestätigt wurde, aber wie eine Entscheidung geführt wird.
- **FK18** (`ENTSCHEIDUNGEN`) Stehende Arbeitsregeln außerhalb des Masterprompts, etwa aus `REGELN-nn.md`, aus Nachgängen oder aus Anweisungen, je mit Quelle.
- **FK19** (`ENTSCHEIDUNGEN`) Freigaben: Wer gibt was frei, bei Übungswerken, bei Testwerken des Breitentests und bei echten Werken? Wortlaut der gültigen Stelle.
- **FK20** (`CHRONIK`) Budgets je Phase und Werk: Grenze, verbraucht, offen. Wo und wie setzt das Biotop die Kostengrenze durch (Stelle im Code oder in der Konfiguration)?
- **FK21** (`ENTSCHEIDUNGEN`) Fristen und Zusagen zum Biotop: was, bis wann, von wem.
- **FK22** (`VERFASSUNGEN`) Der Wortlaut jeder Verfassung (`lagerhaus`, `logmuehle`, jedes Testwerk), mit Pfad, SHA-256 und wer sie bestätigt hat. Fehlt eine, steht sie als `NICHT GEFUNDEN` da.

**D — Ergebnisse, Tore, Messgerät**
- **FK23** (`LAGE`) Stand jeder Phase: nicht begonnen, läuft, abgenommen, eng abgenommen oder gescheitert. Mit Datum und Abschlussordner.
- **FK24** (`TORE`) Tafel aller Torzeilen aller Phasen: Wortlaut der Zeile, Grenze, letzter Messwert, Bezugsgröße, Quelle, Datum und Chat-Claudes Wertung, falls vorhanden.
- **FK25** (`LAGE`) Je Werk (`lagerhaus`, `logmuehle`, T3, T4, T5, T6 und jedes weitere):
  - Art, und warum es als „neuer Art" gilt
  - Pfad
  - Umfang: Dateien, Zeilen, Tests
  - Verfassung ja/nein, von wem bestätigt
  - Läufe und Ergebnis
- **FK26** (`LAGE`) Sättigungsregel: die Folge der Werke neuer Art mit „neuer Messgerätfehler ja/nein" und die Zahl der aufeinanderfolgenden Werke ohne neuen Fehler.
- **FK27** (`TORE`) Jeder seit dem 18.09. gefundene Messgerätfehler: Kennung, Werk, Lauf, Beschreibung, behoben ja/nein, an einem Eichfall nachgewiesen ja/nein. Dazu der Stand der Eichung („Generation minus eins") vor dem letzten Lauf.
- **FK28** (`TORE`) Aufnahmesperre C: natürliche Fänge, Anzahl mit Bezugsgröße. Abweichungsquote Ansage↔Ausführung: gemessen ja/nein, Wert.
- **FK29** (`TORE`) Art- und Projektgedächtnis: Zahl der Einträge je Werk, belegte Richtungen von wie vielen, letzter Nachweis.
- **FK30** (`SOLL-IST`) Soll-Ist-Abgleich gegen die gültige Fassung: jede ausdrücklich verlangte Lieferung, jede Vorbedingung und jedes Tor, mit Kennung (Masterprompt-Abschnitt und laufende Nummer) und genau einem Status:
  - `BELEGT`, mit Verweis auf den Beleg
  - `TEILWEISE`, mit dem, was fehlt
  - `OFFEN` oder `NICHT BEGONNEN`
  - `ABGEWICHEN`, mit der Art der Abweichung und wessen Entscheidung
  - `ENTFALLEN`, mit wessen Entscheidung
  - `UNKLAR`; der Punkt steht zusätzlich in FK47

**E — Technik**
- **FK31** (`AUFBAU`) Verzeichnisbaum bis Tiefe 3 ohne Abhängigkeitsordner; Sprachen und Zeilen je Bauteil.
- **FK32** (`AUFBAU`) Jedes Bauteil in ein bis zwei Sätzen: Zweck, Ort, Schnittstelle und wie es geprüft wird. Das gilt für Kern, Schwarm und Nischen, Ankläger, Aufnahmesperre C, Artgedächtnis, Projektgedächtnis, Mentor, Oberfläche, Messgerät, Freigabe-Gate und alle weiteren.
- **FK33** (`AUFBAU`) Modelle, die das Biotop über OpenRouter nutzt: genaue Kennung und Rolle je Nische.
- **FK34** (`AUFBAU`) Einen Lauf starten und auswerten: Befehle, Eingaben, und wohin Ergebnisse, Protokolle und Kosten geschrieben werden. Dazu das Schema der Kasse.
- **FK35** (`AUFBAU`) Tests: Anzahl je Art; letzter lokaler Testlauf mit Ergebnis.
- **FK36** (`AUFBAU`) Umgebung: Sprachversionen, Docker-Nutzung, Dienste und Zeitgeber des Biotops, belegte Ports. Ist ein Teil öffentlich erreichbar? Wenn ja: welche Adresse, und was ist darüber erreichbar.
- **FK37** (`AUFBAU`) Fähigkeitsstand: was das Biotop zum Stichzeitpunkt nachweislich kann, je Fähigkeit mit dem Lauf, der es zeigt. Dazu, was es noch nicht kann.
- **FK38** (`AUFBAU`) Fundstellen: jedes wichtige Stück mit Pfad und, falls öffentlich, vollständiger Adresse. Dazu gehören Code, Werke, Verfassungen, Masterprompts, Kasse, Gedächtnis, Abschlussordner und deine eigenen Planungs- und Tafeldateien.

**F — Offenes und Risiken**
- **FK39** (`LAGE`) Offene Punkte, je mit:
  - Kennung und was
  - Beleg
  - Folge, falls er offen bleibt
  - blockiert den nächsten Schritt ja/nein
  - wie oft er schon mit „blockiert nicht" weitergereicht wurde
- **FK40** (`LAGE`) Wünsche und Anweisungen Philipps zum Biotop, die noch nicht umgesetzt sind: Wortlaut oder Fundstelle, seit wann, Stand.
- **FK41** (`LAGE`) Abweichungen vom Masterprompt seit dem 18.09.: was, Grund, weiß Philipp davon ja/nein.
- **FK42** (`LAGE`) Widersprüche zwischen Quellen, je mit beiden Belegen: Gedächtnis gegen Dateien, Meldungen gegen Messungen, Kasse gegen Prüfkanal.
- **FK43** (`LAGE`) Risiken für das Vorhaben bei Kosten, Daten, Betrieb und Sicherheit, je mit Beleg.

**G — Weiterer Weg**
- **FK44** (`LAGE`) Was steht laut gültigem Masterprompt als Nächstes an? Mit Zitat der Stelle.
- **FK45** (`LAGE`) Restweg laut Masterprompt bis zum Ende des Vorhabens: verbleibende Phasen und Tore in Reihenfolge. Je Schritt die Vorbedingungen und was Philipp dafür entscheiden muss. Dazu Kandidaten für Phase 5, falls schon genannt: von wem, Stand.
- **FK46** (`LAGE`) Vorschlag Hermes für den nächsten Schritt, getrennt von FK44.

**H — Offener Teil**
- **FK47** (`LAGE`) Fragen an Philipp und Fragen an Chat-Claude: alles, was dir unklar ist oder eine Entscheidung braucht. Gesammelt statt angehalten.
- **FK48** (`LAGE`) Auslegungen: jede Stelle in Masterprompt, früheren Aufträgen oder diesem Auftrag, die du auslegen musstest, und wie du sie ausgelegt hast.
- **FK49** (`LAGE`) Alles Weitere, was für das Verständnis des Stands wichtig ist, ausdrücklich auch das, wonach Chat-Claude nicht zu fragen wusste. Im Zweifel aufnehmen; Geheimnisse ausgenommen.
- **FK50** (`GLOSSAR`) Jeder Fachbegriff des Biotops aus Masterprompt, Code und Berichten, mit Bedeutung in einem Satz und Fundstelle. Mindestens jeder Begriff, der in `LAGE` und `TORE` vorkommt, und diese: Werk, Übungswerk, Testwerk, Verfassung, Lauf, Nachlauf, Nachgang, Tor, Torzeile, Messgerät, Messgerätfehler, Eichfall, Nische, Hersteller, Ankläger, Mentor, Organ, Aufnahmesperre C, Doppelung, Doppelungsschlüssel, Doppelungsanteil, Artgedächtnis, Projektgedächtnis, Richtung, Generation minus eins, Generation 0, Immuntest, Angriffstest, Vertragsprobe, Zwangsbefund, Pareto je Test, Norm-Regel, Rauschtoleranz, werkübergreifender Block, „KEIN VORSCHLAG", Freigabe-Gate, Sättigungsregel, Kasse.

**Abgleich des Wissensstands** (`LAGE`): Jeden Punkt WS01–WS19 aus dem Anhang markierst du mit `GILT`, `VERALTET` (mit neuem Stand), `FALSCH` (mit richtigem Stand) oder `UNBEKANNT`. Zu jedem Punkt gehört eine Quelle.

## 7. Vollständigkeitsprüfung (→ `VOLLSTAENDIGKEIT`)

Bevor du abschließt:
1. **Antworttafel:** Für jede Frage FK01–FK50 und jeden Punkt WS01–WS19 steht da, in welcher Datei und welchem Abschnitt er beantwortet ist. Sonst steht `UNBEKANNT` mit Grund und dem, was die Lücke schließen würde. Darunter die Zählung: beantwortet x von 69, `UNBEKANNT` y.
2. **Abgleichergebnis** aus Abschnitt 5: je Abgleich die Zahl der zugeordneten, erklärten und offenen Einträge, die Quellenabdeckung je Quelle und das Ergebnis der Gegenprobe.
3. **Glossarprüfung:** Jeder Fachbegriff aus `LAGE` und `TORE` steht im `GLOSSAR`. Anzahl der Begriffe, Anzahl der fehlenden.
4. **Lückenliste:** jede verbleibende Lücke mit Kennung (LU01, LU02 …). Je Lücke: was fehlt, warum, was sie schließen würde und wer sie schließen kann (Hermes, Philipp oder Chat-Claude). Eine Lücke, die nicht hier steht, gilt als verschwiegen.

## 8. Abschlussordner

Ort: `laeufe/biotop-lage-01/` im Prüfkanal. NN ist die laufende Nummer, beginnend bei 01.
- Alle Dateien sind reines Markdown, Text oder CSV, UTF-8 und ohne Anmeldung per HTTPS abrufbar.
- Jede Datei ist höchstens 40 KB groß. Größeres teilst du auf (`LAGE-TEIL1-01.md`, `LAGE-TEIL2-01.md` …).
- `LAGE` schreibst du für einen Leser, der nur diese Datei hat.

| Datei | Inhalt |
|---|---|
| `START-NN.md` | Kennung, Fassung, Stichzeitpunkt, Uhrzeit, Status `VOLLSTÄNDIG` / `TEILWEISE` / `ABGEBROCHEN`; Lage in fünf Sätzen; Zählung der Antworttafel; was von Abschnitt 10 nicht erfüllt ist; Lesereihenfolge für Chat-Claude; jede Datei des Ordners mit vollständiger Adresse, Größe und SHA-256; die vollständigen Adressen der neuesten Dateien in `laeufe/gedaechtnis/` |
| `LAGE-NN.md` | Abgleich des Wissensstands; FK01–FK09, FK13, FK23, FK25, FK26, FK39–FK49 |
| `CHRONIK-NN.md` | FK10, FK12, FK20 |
| `VERLAUF-NN.md` | FK11 |
| `MASTERPROMPT-GUELTIG-NN.md` | FK14 |
| `ENTSCHEIDUNGEN-NN.md` | FK15–FK19, FK21 |
| `VERFASSUNGEN-NN.md` | FK22 |
| `TORE-NN.md` | FK24, FK27–FK29 |
| `SOLL-IST-NN.md` | FK30 |
| `AUFBAU-NN.md` | FK31–FK38 |
| `GLOSSAR-NN.md` | FK50 |
| `INVENTAR-NN.md` | Abschnitt 5 |
| `KASSE-NN.csv` · `LISTEN-NN.txt` | Rohlisten aus Abschnitt 5 |
| `SICHERUNG-NN.md` | Abschnitt 4 mit allen Nachweisen, der Wiederherstellungsanleitung und dem Vorher/Nachher-Vergleich |
| `VOLLSTAENDIGKEIT-NN.md` | Abschnitt 7 |
| `ROHBELEGE-NN.txt` | jeder ausgeführte Befehl mit vollständiger Ausgabe, nummeriert R1, R2 … |
| `DATEIEN-NN.txt` · `PRUEFSUMME-ORDNER-NN.txt` | Dateiliste mit Größen · SHA-256 je Datei |
| `ABRUFPROBE-NN.txt` | Ausgabe der Abrufprobe; die einzige Datei, die nach der Prüfsummenliste entsteht |

Regeln:
- **Adressen immer vollständig und wörtlich** (`https://…`), nie relativ und nie nur als Linktext. Chat-Claudes Abrufwerkzeug öffnet nur Adressen, die wörtlich vor ihm stehen.
- Jede Zahl steht an genau einer Stelle; andere Dateien verweisen darauf.
- **Geheimnissuche** über jede Datei des Ordners, bevor die abschließende Einstiegsdatei entsteht.
  - Gegenprobe: Eine Testdatei in `/root/sicherung/biotop-lage-01/` mit einem erfundenen Schlüssel im OpenRouter-Muster muss gefunden werden.
  - Suche und Gegenprobe kommen als Rohbeleg dazu.
- **Abrufprobe** vor Meldung 2:
  - Jede Adresse wird von außen über HTTPS abgerufen. Festgehalten werden Statuscode, Bytes und SHA-256 gegen die Datei.
  - Die ausgelieferte `robots.txt` muss die Adressen für ein regeltreues Abrufwerkzeug erlauben.
  - Gegenprobe: Eine absichtlich falsche Adresse im selben Ordner muss 404 liefern.

## 9. Meldungen an Philipp (Telegram)

**Meldung 1** — sofort nach Schritt 1:
```
BIOTOP-LAGE-01 Fassung 2 BEGONNEN · <Datum Uhrzeit Zone>
Stichzeitpunkt: <Datum Uhrzeit Zone> | folgt nach Laufende: <Lauf, seit wann, erwartetes Ende>
Ordner: <vollständige Adresse>
Einstieg: <vollständige Adresse der START-Datei>
```

**Meldung 2** — zum Schluss, auch bei Abbruch oder Zeitmangel:
```
BIOTOP-LAGE-01 Fassung 2 <VOLLSTÄNDIG | TEILWEISE | ABGEBROCHEN> · <Datum Uhrzeit Zone>
Stichzeitpunkt: <Datum Uhrzeit Zone>
Einstieg: <vollständige Adresse der neuesten START-NN.md> · SHA-256 <Wert>
<jede weitere Datei des Ordners mit vollständiger Adresse, eine je Zeile>
<je Biotop-Abschlussordner seit dem 21.09. seine Hauptdatei (Bericht oder Einstieg) mit vollständiger Adresse, eine je Zeile>
Antworttafel: <x> von 69 beantwortet · UNBEKANNT <y> · Lücken <z> · offene Punkte <n>
Wiederherstellung: Unterschied leer ja/nein · Gegenprobe angeschlagen ja/nein
Abrufprobe: <x> von <y> Adressen mit 200 und passender Prüfsumme · robots.txt erlaubt ja/nein
OpenRouter-Kosten dieses Auftrags: <€> (Soll 0,00)
```

Ist Meldung 2 länger als 3500 Zeichen, teilst du sie in 2a, 2b … Jede Teilmeldung trägt Kennung und Teilnummer, und keine Adresse wird zerschnitten. An die letzte Teilmeldung hängst du `START-NN.md`, `LAGE-NN.md` (bei Aufteilung alle Teile) und `VOLLSTAENDIGKEIT-NN.md` als Dateien. Das ist der zweite Weg, falls ein Abruf scheitert. Jede Meldung schickst du genau einmal; alles Weitere steht im Ordner.

## 10. Maßstab — woran Chat-Claude prüft

Der Maßstab ist vor der Arbeit gesetzt und wird danach nicht verhandelt:
1. Aus Meldung 2 ist jede Datei des Ordners abrufbar und lesbar.
2. Die Antworttafel ist vollständig: alle 50 Fragen und 19 Punkte des Wissensstands sind mit Fundstelle beantwortet. Jedes `UNBEKANNT` hat einen Grund und einen Weg zur Schließung.
3. Der Abgleich hat keine unerklärte Abweichung:
   - Die Laufnummern sind lückenlos, oder jede Lücke ist erklärt.
   - Die Fassungen von v1 bis zur gültigen sind vollständig oder als `NICHT GEFUNDEN` geführt.
   - Jeder Commit und jede geänderte Datei seit dem 21.09. ist zugeordnet.
   - Die Kosten der Kasse sind gegen OpenRouter abgeglichen, oder `QUELLE FEHLT` steht da.
   - Die Gegenprobe des Abgleichs hat angeschlagen.
4. Die Tagesbilanz vom 18.09. bis zum Stichzeitpunkt ist vollständig: jeder Tag mit Zahl oder `NICHT ABGEDECKT`, jede nicht abgedeckte Spanne in der Lückenliste.
5. Das Entscheidungsregister trennt die Urheber. Unbestätigte Vorentscheidungen sind als solche geführt.
6. Die Wiederherstellungsprobe ist ausgeführt: Dateianzahl beidseitig gleich, Unterschied leer, Gegenprobe angeschlagen, `integrity_check` = `ok`. Alles mit Rohbeleg.
7. Im Ordner steht kein Geheimnis. Suche und Gegenprobe sind beigefügt.
8. `/root/biotop` ohne `.git/` ist vorher und nachher prüfsummengleich.
9. Der Wortlaut von Masterprompt und Verfassungen ist vollständig; die SHA-256 von Kopie und Original sind gleich.
10. Jeder Fachbegriff aus `LAGE` und `TORE` steht im `GLOSSAR`.
11. Jede Zahl hat Bezugsgröße und Quelle; jedes „ausgeführt" hat einen Rohbeleg.

Was davon nicht erfüllt ist, steht oben in der Einstiegsdatei und wird nicht verschwiegen.

## 11. Nachfragen

Hat Chat-Claude nach dem Lesen Fragen, schickt Philipp sie dir als `NACHFRAGE-NN`. Du antwortest im selben Ordner in `ANTWORT-NN.md` mit der nächsten freien Nummer, nach denselben Regeln, und meldest die vollständige Adresse. Ziel dieses Auftrags ist, dass keine Nachfrage nötig wird.

---

## Anhang — Chat-Claudes Wissensstand (WS01–WS19)

Stand 21.09.2026 früh, letzter gesicherter Eintrag 02:16 Uhr MESZ. Seitdem wurde bis zum 25.09. weitergearbeitet; jeder Punkt kann überholt sein. Markiere jeden mit `GILT`, `VERALTET`, `FALSCH` oder `UNBEKANNT`, jeweils mit Quelle.

- **WS01** Gültig ist Masterprompt Fassung 7 (`INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md`, 21.09.2026). v1 bis v6 sind ersetzt. Jede Fassung trägt oben ein Änderungsverzeichnis.
- **WS02** Zielbild, Selbstevolution und Rollen:
  - Das Biotop versteht jedes eingelegte Werk von A bis Z und hebt es als Ganzes auf die nächste Stufe. Jeder Bereich wird einzeln bearbeitet, das Ganze muss harmonisch zusammenpassen.
  - Es erkennt, wenn etwas schon bestmöglich ist, und halluziniert nicht.
  - Selbstevolution ist ausgeschlossen: Das Biotop bearbeitet sich nur selbst, wenn Philipp es als Werk einlegt.
  - Rollen: Hermes führt aus, Chat-Claude prüft, Philipp entscheidet.
- **WS03** Kernmaß F2: Bestandene Tests zählen nicht, nur Fehlschläge zählen negativ. Leistung ist eine Grenze, kein Punktwert.
- **WS04** Phase 1 „Das Skelett" am Übungswerk `lagerhaus`: Tor 1 wurde nach dem Nachlauf (Lauf 9, `laeufe/biotop-phase-1-nachlauf/`) mit 9 von 9 abgenommen.
- **WS05** Phase 2 „Der Schwarm" (`laeufe/biotop-phase-2/`): vier Nischen, vier Hersteller über OpenRouter, 1,91 € von 10 €. Chat-Claudes Wertung rückwirkend: 9 von 11.
- **WS06** Phase 3 „Gedächtnis, Mentor, Oberfläche" (`laeufe/biotop-phase-3/`, Übungswerk `logmuehle`, 2,83 € von 15 €): Wertung 8 von 11. Der Nachlauf (`laeufe/biotop-phase-3-nachlauf/`, 0,44 € von 10 €) ist abgenommen, neun von neun Punkten erledigt.
- **WS07** Vorbedingung 1 (`laeufe/biotop-phase-4-vorbedingung-1/`) wurde am 20.09.2026 abgenommen: Läufe 22 bis 25, 848 Aufrufe, 1,6970 € von 3 €.
- **WS08** Bauteil A (der Ankläger sagt die Behauptung vorab an) spart Aufrufe, verhindert aber keine Doppelungen. Bauteil B zeigt Streuung statt Wirkung. Deshalb wurde die deterministische Aufnahmesperre C im Kern gebaut.
- **WS09** Die Aufnahmesperre C hat im natürlichen Betrieb nie eine Doppelung abgefangen; alle Belege waren gestellte Fälle (Stand 20.09.).
- **WS10** Die Abweichungsquote Ansage↔Ausführung ist ungemessen (Stand 20.09.).
- **WS11** Tor 2 Zeile 8 ist erfüllt (9,09 %). Das Artgedächtnis ist in 3 von 5 Richtungen belegt.
- **WS12** Das KI-Handelssystem ist seit 21.09. als Werk für Phase 4 gestrichen. Alle daran hängenden Bezugsgrößen sind ungültig.
- **WS13** Phase 4 ist der Breitentest an Werken neuer Art, die du selbst baust: T3 TypeScript, T4 groß/fremder Stil/ohne Tests, T5 Oberfläche, T6 Zustand und Außenwelt.
- **WS14** Phase 4 wird nach der Sättigungsregel abgenommen: Sie ist fertig, wenn zwei aufeinanderfolgende Werke neuer Art keinen neuen Messgerätfehler mehr erzeugen.
- **WS15** Phase 5 ist das erste echte Werk und hat noch kein Werk. Philipp wählt es nach dem Breitentest. Kriterien:
  - Es steht still.
  - Es hat oder bekommt Tests.
  - Sein Maß ist klar.
  - Ein Fehlschlag ist nicht teuer.
  - Seine Art ist im Breitentest belegt.
- **WS16** Masterprompt Abschnitt 2a hat neun Grundsätze; 7 bis 9 kamen mit Fassung 7:
  - Grundsatz 7: Ein Nachweis zählt nur, wenn er ausgeführt wurde.
  - Grundsatz 8: Jede Probe braucht eine Gegenprobe, die fehlschlagen muss.
  - Grundsatz 9: Der Prüfaufwand muss zum Gegenstand passen.
- **WS17** Freigabe: Nach Stand 20.09. gibt ab Phase 4 ausschließlich Philipp frei; die Vollmacht für Übungswerke gilt dort nicht. Chat-Claude ist unklar, ob das auch für die Testwerke des Breitentests gilt. Zitiere dazu den Wortlaut der gültigen Fassung.
- **WS18** Ablieferung: nummerierte Dateinamen, die nie überschrieben werden, etwa `NACHGANG-04.md`, `DATEIEN-04.txt` und `PRUEFSUMME-ORDNER-04.txt`.
- **WS19** Ablageorte:
  - Der Biotop-Code liegt unter `/root/biotop`, die Kasse unter `/root/biotop/daten/biotop.db`.
  - Die Biotop-Ordner liegen unter `laeufe/<auftrag>/` im Prüfkanal.
  - Dein Gedächtnis liegt unter `laeufe/gedaechtnis/` (`STAND-nn.md`, `REGELN-nn.md`, `UNTERBAU-nn.md`). Nur HERMES-1 schreibt dorthin.