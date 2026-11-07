# Prüfauftrag: ein Reviewdurchgang für abschluss-03 (T3 TypeScript, Biotop)

Du bist ein unabhängiger Prüfer. Du prüfst einen Bericht und die Codeänderung dahinter — du setzt nichts um, du reparierst nichts.
Antworte und schreibe auf Deutsch. Genau ein Durchgang: lesen, nachmessen, Befunde aufschreiben, fertig.

## Gegenstand
1. Berichtsentwurf: `/root/biotop-t3/abschluss3/ABSCHLUSS-03.md`
2. Kern-Commit `f821707`: `git -C /root/biotop show f821707` (die vorherige Kernversion ist `1cf2eb1`;
   `git -C /root/biotop diff 1cf2eb1 f821707`). Belege am Commit-Stand: `REGRESSION-ABSCHLUSS3.txt`, `VOR-REVIEW.txt`,
   `JOB4.txt`, `EICHPFAD-COMMIT.txt`, `ROT-GEGEN-1cf2eb1-ENDSTAND.txt`, `VERDRAHTUNG-PFLICHT-GEGENPROBE.txt/.json`,
   `VERDRAHTUNG-BELEG-REGRESSION.json`, `COMMIT-KERN.txt`.
3. Belege: `/root/biotop-t3/abschluss3/` — insbesondere `AUSWERTUNG-ABSCHLUSS3.txt/.json`, `NACHSPIEL-*.txt`, `nachspiel/*.json`,
   `nachspiel-serie1/*.json`, `S1S5-ABSCHLUSS3.*`, `ZUSATZ-ABSCHLUSS3.*`, `VERDRAHTUNG-*`, `REGRESSION-ABSCHLUSS3.txt`,
   `EICHPFAD-NACH-EINBAU.txt`, `ROT-GEGEN-1cf2eb1.txt`, `SCHNAPPSCHUSS.txt`, `SPERREN.md` und die Skripte daneben.
4. Lauf-Datenbank: Schnappschuss `/root/biotop-t3/schnappschuss-abschluss3/t3.db` — NUR mit
   `sqlite3.connect('file:…?mode=ro', uri=True)` öffnen. Nicht `immutable=1` (übergeht die WAL), nie schreibend.
5. Werkstände: Lazarus-Archive `/root/biotop/daten/lazarus/lauf3{7,8}-gen*.tar.gz` (nur nach /tmp entpacken).

## Der Auftrag, den der Bericht erfüllen soll (Wortlaut des Auftraggebers)
„(1) verhaltensvergleich und masseichung in den Annahmepfad einhängen. (2) Gegenproben durch genau die Funktion, die ein Lauf zur
Annahme ruft, mit den aufgezeichneten Kandidaten und Lazarus-Ständen: K2934 und K3121 müssen abgelehnt werden, K2868 und die
S2-Beschleunigung angenommen, und das vom Annahmepfad berechnete Kernmaß darf detect-object-injection nicht mehr zählen.
(3) Verdrahtungsnachweis als Regressionstest: Für jedes Organ unter biotop/organe/ belegt ein Nachspiel durch den Annahmepfad, dass
es aufgerufen wurde — ein Organ, das existiert und nie gerufen wird, macht die Regression rot. (4) Lauf 38 bereinigt auswerten wie
Lauf 37: Kernmaß ohne die Fehlalarm-Regel, welche Sicherheitsminderungen bloße Umformungen waren, S1 bis S5 nach „behoben heißt
verschwunden", Halluzinationsprobe, Doppelungsanteil mit der Methode aus Vorbedingung 1, Immunisierung auf dem TypeScript-Pfad —
und warum der Testbestand in Lauf 38 bei 207 beginnt statt bei 182. (5) Die Blockmeldung „unparsbare Payload" im Wortlaut. Dann
Abschlussbericht T3 als abschluss-03: nicht abgenommen, alle Befunde, alle Behebungen mit Nachweis am Laufweg."

## Was du prüfst
a) **Jede Zahl gegen ihre Quelle.** Rechne nach (DB-Schnappschuss, Beleg-JSON). Jede Zahl braucht eine Bezugsgröße („x von y").
   Summen müssen aufgehen; Kategorien dürfen zwischen Abschnitten nicht anders geschnitten sein.
b) **„Am Laufweg" wirklich am Laufweg?** Lies `biotop/nachspiel.py` und `abschluss3/nachspiel_gegenproben.py`: Ruft das Nachspiel
   `aegis.pruefen` mit dem Aufbau, den `lauf.generation()` herstellt, oder baut es etwas nach? Was ist gestellt (Anbietergrenze,
   Immuntests, ausgeblendete Generationen), und schwächt das eine Aussage des Berichts?
c) **Kann der Verdrahtungstest rot werden?** `tests/test_verdrahtung.py`: Belegen die Rot-Nachweise (gegen `1cf2eb1`, Pflicht-
   Gegenprobe) wirklich die Aussage? Gibt es ein Organ, das nur formal „gerufen" wird (z. B. über eine Hilfsfunktion), ohne dass
   seine Entscheidung wirkt?
d) **Codeprüfung des Commits:** Fehler im Einhängen — z. B. Verhaltensvergleich im Verhandlungs-/Partnerpfad
   (`lauf._verhandeln` → `aegis.pruefen` mit `extra_code`), beide Seiten des Paars geeicht, Idempotenz von `masseichung.anwenden`,
   was geschieht, wenn die Sonde abstürzt (Inhalt oder Infrastruktur?), Neutralzähler, Protokollfelder, Grenzmaße nach der
   Eichung, Bestwert/Ausgangsmaß konsistent geeicht.
e) **Widersprüche** im Bericht, zwischen Bericht und Belegen, und gegenüber früheren Aussagen (`/root/biotop-t3/NACHTRAG-02.md`,
   `/root/biotop-t3/LAUF38-BERICHT.md`) — sind alle Korrekturen benannt?
f) **Lücken gegenüber dem Auftrag** (Punkte 1–5 oben) und Aussagen, die stärker formuliert sind als ihr Beleg.

## Regeln (hart)
- Keine Modellaufrufe an Anbieter (OpenRouter o. ä.), kein Netz. Kammerläufe (Docker, netzlos) sind erlaubt, wenn du eine Zahl
  selbst nachmessen musst; sie kosten nichts. Dann aber nicht parallel zu anderen Kammerläufen.
- Nichts ändern, löschen oder überschreiben — außer deiner eigenen Ausgabedatei (unten). Keine Git-Schreibbefehle.
  `/root/versiegelt/` nur lesen. Keine Webseite und keine Serverdienste anfassen.
- Den Ordner `/root/biotop-t3/abschluss3/lauf38/` und Delegations-Transkripte unter `/root/.hermes/cache/` NICHT verwenden
  (dort ist eine Sperrfrage offen).
- Blockiert die Ausführungsschicht einen deiner Befehle: nicht umformulieren und nicht umgehen; die Meldung wörtlich in dein
  Review schreiben und ohne diese Prüfung weitermachen.
- Lange Befehle als Skriptdatei unter `/tmp/review03/` schreiben und ausführen.

## Umfang
Höchstens etwa 80 Werkzeugaufrufe. Priorität: (a) Zahlen, (d) Codeprüfung, (b), (c), dann der Rest. Kommst du an die Grenze,
schreibe REVIEW-03.md mit dem erreichten Stand und führe Ungeprüftes unter „Nicht geprüft“ auf. Kammerläufe nur, wenn eine
Zahl ohne sie nicht prüfbar ist (höchstens 3).

## Ausgabe
Schreibe `/root/biotop-t3/abschluss3/REVIEW-03.md`:
1. Tabelle der Befunde: Nr | Schwere (hoch/mittel/niedrig) | Befund | Beleg (Datei:Zeile, Abfrage, Messwert) | Vorschlag
2. „Geprüft und bestätigt": was du nachgerechnet hast, jeweils mit Nenner (x von y Zahlen/Aussagen).
3. „Nicht geprüft": was du aus Zeitgründen ausgelassen hast.
Gib am Ende denselben Inhalt als Antwort aus.
