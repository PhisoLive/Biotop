# Prüfauftrag: ein Reviewdurchgang für die Behebungsrunde 4 vor T4 (Biotop)

Du bist ein unabhängiger Prüfer. Du prüfst einen Bericht und die Codeänderung dahinter. Du setzt nichts um und
reparierst nichts. Antworte und schreibe auf Deutsch. Genau ein Durchgang: lesen, nachmessen, Befunde aufschreiben, fertig.

## Gegenstand
1. **Bericht:** `/root/biotop-vor-t4-04/BERICHT.md`. Solange er Platzhalter `‹…›` trägt, prüfst du die ausgefüllten
   Teile. Die Rohbelege liegen daneben.
2. **Kern-Commits:** `1d9a5aa` (Runde 4, Vorgänger `0aac612`) und `43b8fad` (Nachtrag: Nachspiel repariert — an
   `1d9a5aa` brachen alle Nachspiele ab —, Lastabbruch unter der Sonde, Torzeile-Tests). `git -C /root/biotop log
   --oneline -4`; `COMMIT-STAT.txt`, `KERN-COMMIT.patch.txt`, `COMMIT-2-STAT.txt`, `KERN-COMMIT-2.patch.txt`.
3. **Belege:** `/root/biotop-vor-t4-04/`, darin:
   - `bau/` (Umbauskripte `r4_*.py`, Teilläufe `TEILLAUF-*.txt`, `KETTE.txt`)
   - `proben/` (`STUFE2-ZEITEN*` — Stufe 1 gegen Stufe 2, auch die gescheiterte erste Fassung; `VORHER-0aac612.*`,
     `NACHHER-HEAD.*` — dieselben neuen Testfälle am alten und am neuen Code)
   - `nachspiel/` (`NACHSPIEL-D1..3.txt` am Commit `1d9a5aa` — alle abgebrochen, ein Befund; `NACHSPIEL-N1..3.txt`,
     `n1..n3/*.json` am Nachtrag `43b8fad` — die Gegenprobe; `PROBE-ARBEITSBAUM.txt`, eine Vorprobe)
   - `s1/` (`TORZEILE-SCHWAECHEN-T3*.txt/.json`)
   - `FEHLALARM-SICHERHEITSFILTER.md`, `JOB-COMMIT-REGRESSION.txt`, `REGRESSION.*`, `VERDRAHTUNG-BELEG-REGRESSION.json`
     (an `1d9a5aa`); `JOB-NACHTRAG.txt`, `REGRESSION-2.*`, `VERDRAHTUNG-BELEG-REGRESSION-2.json` (am Nachtrag; laufen
     eventuell noch während deiner Prüfung)
   - `sperre/` (eine Formatsperre, gespeichertes Skript unverändert ausgeführt)
4. **Vorrunde:** `/root/biotop-vor-t4-03/` — `REVIEW.md` (18 Befunde), `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md` (R4-1 …
   R4-20), `review-proben/` (Proben des Gutachtens 03: `deckprobe.py`, `sondenprobe3.py`, `sondenprobe4.py` u. a.).
5. **Auftrag** (Philipp, 24.09., Entscheidungen Chat-Claude):
   1. **Vergleichslast:** zweite Stufe mit zehnfacher Eingabegröße je Bereich, ein Kammerlauf bleibt unter einer Minute;
      an ihr misst die Nische „schnell“ den Gewinn und jede Nische ihre Laufzeitgrenze. Gegenprobe im Nachspiel:
      K2904 und K3091 drei von drei gleich. T3s Ergebnisse bleiben unverändert.
   2. **Die vier hohen Befunde des Reviews 03 vor T4;** jede Formvariante, die die Sonde erzeugt, ist ein eigenes
      Merkmal (Weißraum je Zeichen).
   3. **Merkmale nicht veränderter Argumente gehören nicht zum Muster.** Gegenprobe: die Abweichungen bei ungültigen
      Eingaben von K2868 sind gedeckt, die Weißraum-Muster bleiben ungedeckt.
   4. **Tests, die der Kandidat selbst mitbringt, decken nicht;** decken dürfen Tests der Vorgeneration, aus
      Generation 0, vom Ankläger und die versiegelten Gegenzeugen. Gegenprobe: ein Kandidat mit Rückschritt und eigenem
      Test, der genau diesen Rückschritt zusichert, wird abgelehnt.
   5. **Methoden in TypeScript vor T5** (nicht vor T4); **doppelte Gegenzeugen-Prüfung verbindlich in der Torzeile
      „Schwächen“**, nicht im Annahmepfad.
   6. **Fehlalarm** als sachlicher Text mit Befehlsmuster und Sperrwortlaut in den Abschlussordner, ohne Projektinterna.
   Dazu: aus R4-1 … R4-20 alles, was T4 gefährden würde; der Rest mit Begründung auf die Liste. Die Übergabe nach jedem
   abgeschlossenen Schritt nachführen. Kein Lauf, kein Modellgeld.
6. **Masterprompt** Fassung 8 (Grundsätze 1–14, Abschnitt 8 Tor 4):
   `/root/.hermes/cache/documents/doc_6640d9a3854f_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md`.
7. **Lauf-DB** (nur für Nachrechnungen): `/root/biotop-t3/schnappschuss-abschluss3/t3.db`. Öffne sie NUR mit
   `sqlite3.connect('file:…?mode=ro', uri=True)`, nie mit `immutable=1`, nie schreibend. `/root/versiegelt/` nur lesen.

## Was du prüfst
a) **Jeder Auftragspunkt (1–6):** gebaut wie verlangt? Gegenprobe vorhanden, durch den Laufweg (`aegis.pruefen`,
   `lauf._generation_koerper`, Nachspiel), scheitert sie an der vorgesehenen Zusicherung? Modul- und Laufweg-Nachweise
   getrennt. Insbesondere: Ist „T3s Ergebnisse bleiben unverändert“ eingehalten (Stufe 1, Sonde, Verhaltensraster)?
b) **Stufe 2:** Ist die Last wirklich „zehnfache Eingabegröße“ in jedem Bereich? Kammerlauf < 60 s gemessen (mit
   Bezug)? Misst die Rauschmessung an derselben Stufe wie der Gewinn? Fallen gesperrte Bereiche oder Rückfälle still?
c) **Deckung** (Merkmale je Formvariante, Muster = eingeführte Merkmale, Verfälschung je Merkmal, Fixture-Fehler,
   eigene Tests): Suche Lücken wie in Review 03 Nr. 1/2 — kann ein Test decken, ohne das Merkmal festzuhalten? Kann ein
   Kandidat über einen Test der Vorgeneration, den er ändert, oder über Vertragsdateien decken? Gilt Python und TS gleich?
d) **Die vier hohen Befunde:** Fahre die Proben des Gutachtens 03 (`review-proben/deckprobe.py`, `sondenprobe3.py`,
   `sondenprobe4.py`) gegen den NEUEN Commit (Kopien unter deinem /tmp-Ordner anpassen). Geschlossen? Neue stille Stellen
   oder Fehlalarme (z. B. Iterator-Objekte, `__slots__` mit Vererbung, Koroutinen in laufender Schleife)?
e) **Zahlen gegen ihre Quelle, mit Nenner:** Stufe-2-Zeiten, Nachspiele (K2904/K3091 × 3, K2868), Vorher/Nachher,
   Torzeile, Regression.
f) **Geänderte ältere Tests:** Spezifikationsänderung oder zugedeckte Regression?
g) **Aussagen, die stärker sind als ihr Beleg,** und **Lücken gegenüber dem Auftrag**, einschließlich der Liste
   „auf die Liste gesetzt“ (R4-…): ist jede Zurückstellung begründet, und gefährdet eine davon T4 doch?

## Harte Regeln
- Kein Modellaufruf, kein Netz, kein Geld.
- Schreibe NUR `/root/biotop-vor-t4-04/REVIEW.md` und eigene Dateien unter `/tmp/review-vor-t4-04/` (setze `TMPDIR` in
  diesen Ordner). Nichts anderes.
- Kammerläufe (Docker) sind erlaubt, aber keine, solange `job_nachtrag.sh` läuft (`pgrep -f job_nachtrag`). Bis dahin
  lesen und rechnen.
- Keine volle Regression und kein Verdrahtungstest (laufen im Job).
- **Sperren:** Wird ein Befehl blockiert (Sicherheitssperre, Freigabeabfrage, Formatsperre), hältst du mit genau diesem
  Schritt an und berichtest ihn wörtlich mit Befehl und Meldung. Nicht umformulieren, keinen anderen Weg, dieselben
  Daten nicht auf anderem Weg lesen. Was dadurch ungeprüft bleibt, steht unter „Nicht geprüft“. Ein Schritt je Befehl
  (Kopieren, Lesen, Ausführen getrennt), lange Befehle als Skript unter `/tmp/review-vor-t4-04/`.
- Budget: etwa 70–80 Werkzeugaufrufe. Danach schreibst du den erreichten Stand.

## Ausgabe (`REVIEW.md`)
- Tabelle `Nr | Schwere (hoch/mittel/niedrig) | Befund | Beleg (Datei:Zeile, Befehl, Messung) | Vorschlag`.
- „Geprüft und bestätigt“ mit Bezugsgrößen (x von y).
- „Nicht geprüft“ mit Grund.
- „Sperren“: jede Sperre wörtlich, oder „keine“.
- Schreibort-Nachweis: alle Dateien, die du geschrieben hast.
