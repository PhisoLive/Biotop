# Prüfauftrag: ein Reviewdurchgang für die Behebungsrunde 3 vor T4 (Biotop)

Du bist ein unabhängiger Prüfer. Du prüfst einen Bericht und die Codeänderung dahinter. Du setzt nichts um und
reparierst nichts. Antworte und schreibe auf Deutsch. Genau ein Durchgang: lesen, nachmessen, Befunde aufschreiben, fertig.

## Gegenstand
1. **Bericht:** `/root/biotop-vor-t4-03/BERICHT.md`. Solange er Platzhalter `‹…›` trägt, prüfst du die ausgefüllten
   Teile. Die Rohbelege liegen daneben.
2. **Kern-Commits:** `d54bf2f` (Runde 3, Vorgänger `6243377`) und `0aac612` (Nachtrag, nur
   `tests/test_t3_python_annahmen.py`; `git -C /root/biotop log --oneline -4`). `COMMIT-STAT.txt`, `KERN-COMMIT.patch.txt`,
   `COMMIT-2-STAT.txt`, `KERN-COMMIT-2.patch.txt` im Arbeitsordner.
3. **Belege:** `/root/biotop-vor-t4-03/`, darin:
   - `bau/` (Rauchproben, Teilläufe TEILLAUF-1 … -6 mit ihren Fehlschlägen, `KETTE.txt`)
   - `proben/VORHER-6243377.*` (die Fälle der Gruppen A/B/D am Code von `6243377` aus `git archive`) und
     `proben/NACHHER-HEAD.*` (dieselben am Code von HEAD — entsteht im Nachtrag-Job, eventuell erst während deiner Prüfung)
   - `s1/` (Doppelprüfung der Gegenzeugen, `GEGENZEUGEN-DOPPELT*.txt/.json`)
   - `proben/` (echte Rissprobe `RISSPROBE-ECHT.*`)
   - `spez/` (rote Spezifikation Gewinnschwelle aus Runde 2, am neuen Stand)
   - `nachspiel/` (`NACHSPIEL-D1..3.txt`, `d1..d3/*.json`)
   - `JOB-COMMIT-REGRESSION.txt`, `REGRESSION.*`, `VERDRAHTUNG-BELEG-REGRESSION.json` (an `d54bf2f`: 1 rot)
   - `JOB-NACHTRAG.txt`, `REGRESSION-2.*`, `VERDRAHTUNG-BELEG-REGRESSION-2.json` (am Nachtrag; laufen eventuell noch)
4. **Vorrunde:** `/root/biotop-vor-t4-02/` — `REVIEW.md` (22 Befunde), `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md` (S-1 … S-13),
   `review-proben/` (Proben des Gutachtens 02: `sondenprobe.py`, `sondenprobe2.py`, Ausgaben `SONDENPROBE*.txt/.json`).
5. **Auftrag** (Philipp, 24.09., Entscheidungen Chat-Claude):
   1. **Deckung je Muster** (nicht je Eingabe, nicht je Funktion). Gegenproben: K2868 scheitert am ungedeckten
      Weißraum-Muster; eine richtige Behebung mit einem Test je Muster kommt durch; K2868 einmal nur mit erweitertem
      Korpus und einmal nur mit neuer Deckungsregel gemessen, damit getrennt ist, was was bewirkt.
   2. **Gewinnschwelle der Nische „schnell“ in beiden Richtungen nachmessen,** nur innerhalb der Rauschtoleranz um die
      Schwelle. Gegenprobe: K2904/K3091 in drei von drei Durchgängen gleich — kippt es trotzdem, wird es gemeldet
      (dann liegt es an der Größe der Vergleichslast).
   3. **Methoden von Klassen beobachten,** Instanzen aus den Verträgen, Zustand von `self` vor und nach dem Aufruf
      verglichen; Enthaltung nur für wirklich Unbeobachtbares, gezählt.
   4. **S1 nicht neu versiegeln;** für jedes künftige Testwerk prüft jeder Gegenzeuge zweierlei: Schwäche weg UND
      gültiges Verhalten gegen die Normalversion unverändert.
   5. Die 13 Spezifikationen S-1 … S-13, jede mit Gegenprobe durch den Laufweg; die fünf Lücken der Python-Sonde
      (Generator, Mutation an Ort und Stelle, nur Fehleraufrufe, Hash-Reihenfolge, `lru_cache`) je mit einem Fall, der
      an `6243377` unentdeckt blieb oder Fehlalarm gab.

   Kein Lauf, kein Modellgeld.
6. **Masterprompt** Fassung 8 (Grundsätze 1–14, Abschnitt 8 Tor 4):
   `/root/.hermes/cache/documents/doc_6640d9a3854f_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md`.
7. **Lauf-DB** (nur für Nachrechnungen): `/root/biotop-t3/schnappschuss-abschluss3/t3.db`. Öffne sie NUR mit
   `sqlite3.connect('file:…?mode=ro', uri=True)`, nie mit `immutable=1`, nie schreibend. Versiegeltes unter
   `/root/versiegelt/` darfst du lesen, nicht ändern.

## Was du prüfst
a) **Jeder Auftragspunkt (1–5):** Ist er gebaut wie verlangt? Ist die Gegenprobe vorhanden, geht sie durch den Laufweg
   (`aegis.pruefen`, `lauf._generation_koerper`, Nachspiel) und scheitert sie an der vorgesehenen Zusicherung? Weise
   Modul- und Laufweg-Nachweise getrennt aus. Welche der 13 Spezifikationen sind nur am Organ belegt?

b) **Die fünf Lücken der Python-Sonde:** Fahre die Proben des Gutachtens 02 (`review-proben/sondenprobe*.py`, Fälle p1,
   p2, p4, p5, p12 und die übrigen) gegen den NEUEN Commit. Welche sind jetzt geschlossen, welche nicht? Suche neue
   Stellen, an denen die Sonde still schweigt oder Fehlalarm gibt (Methoden, Eigenschaften, Klassen ohne Vertrag,
   asynchrone Funktionen, Iteratoren, die nicht enden, veränderliche Standardwerte).

c) **Deckung je Muster** (`deckung`, `_merkmal_treffer`, `verfaelschungsbedarf`, `deckende_aufrufe`, Aufzeichner in
   `kern/py/verhalten.py` und `kern/ts/deck-setup.mjs`):
   - Sind die Muster der Sonde und die Klassen des Aufzeichners dieselbe Rechnung (beide Sprachen)?
   - Die Lesart „je Merkmal“ (jedes Merkmal eines Musters von irgendeinem festhaltenden Test getroffen) ist eine
     eigene Festlegung. Ist sie mit „ein Test je Muster“ vereinbar, oder öffnet sie eine Lücke?
   - Kann ein Test decken, ohne festzuhalten? Kann die Verfälschungsprobe fehlschlagen, ohne dass es auffällt?
   - Wie viele Kammerläufe kostet die Verfälschungsprobe je Kandidat, und ist das begrenzt?

d) **Gewinn-Nachmessung** (`messgeraet.gewinn_band`, `gewinn_bestaetigen`, Einbau in `aegis.pruefen` und in der
   Generalprobe `lauf.py`): Band, Richtung, gepoolter Median bei Widerspruch (eigene Entscheidung), ungültige
   Nachmessung. Ist das Ergebnis der drei Nachspieldurchgänge K2904/K3091 richtig berichtet?

e) **Zahlen gegen ihre Quelle, mit Nenner:** Teilläufe, Regression, Nachspiele (K2868 in vier Fassungen, 2×2),
   Rissprobe, Gegenzeugen-Doppelprüfung.

f) **Geänderte ältere Tests:** Ist jede Änderung eine Spezifikationsänderung, oder deckt eine davon eine Regression zu?
   Betroffen: `test_t3_verhaltensvergleich`, `test_vor_t4`, `test_vor_t4_02` (gestellte Kammer je Stand, Deckungstests),
   `test_eichproben` (REF_PAAR zurückgenommen, zweite Funktion `kurzbericht`), `test_vorspann` (S-11),
   `test_verdrahtung` (Nachmessungen im Beleg).

g) **Aussagen, die stärker sind als ihr Beleg,** und **Lücken gegenüber dem Auftrag.**

## Harte Regeln
- Kein Modellaufruf, kein Netz, kein Geld.
- Schreibe NUR `/root/biotop-vor-t4-03/REVIEW.md` und eigene Dateien unter `/tmp/review-vor-t4-03/`. Nichts anderes,
  auch keine Probedateien an anderen Orten.
- Kammerläufe (Docker) sind erlaubt, aber keine, solange `job_commit_regression.sh` läuft. Prüfe das mit
  `pgrep -f job_commit_regression.sh`. Warte, oder beschränke dich auf Lesen und Rechnen.
- Führe keine volle Regression und keinen Verdrahtungstest aus. Beides läuft im Job.
- **Sperren:** Wird ein Befehl blockiert (Sicherheitssperre, Freigabeabfrage, Formatsperre), hältst du mit genau
  diesem Schritt an und berichtest ihn wörtlich mit Befehl und Meldung. Du formulierst ihn nicht um, suchst keinen
  anderen Weg und liest dieselben Daten nicht auf anderem Weg. Was du dadurch nicht prüfen kannst, steht unter
  „Nicht geprüft“. Dieselbe Regel gilt für den Auftragnehmer.
- Lange Befehle legst du als Skripte unter `/tmp/review-vor-t4-03/` ab und führst das gespeicherte Skript aus.
- Budget: etwa 70–80 Werkzeugaufrufe. Danach schreibst du den erreichten Stand.

## Ausgabe (`REVIEW.md`)
- Tabelle `Nr | Schwere (hoch/mittel/niedrig) | Befund | Beleg (Datei:Zeile, Befehl, Messung) | Vorschlag`.
- „Geprüft und bestätigt“ mit Bezugsgrößen (x von y).
- „Nicht geprüft“ mit Grund.
- „Sperren“: jede Sperre wörtlich, oder „keine“.
- Schreibort-Nachweis: alle Dateien, die du geschrieben hast.
