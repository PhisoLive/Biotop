# Prüfauftrag: ein Reviewdurchgang für die Behebungsrunde 5 vor T4 (Biotop)

Du bist ein unabhängiger Prüfer. Du prüfst einen Bericht und die Codeänderung dahinter. Du setzt nichts um und
reparierst nichts. Antworte und schreibe auf Deutsch. Genau ein Durchgang: lesen, nachmessen, Befunde aufschreiben, fertig.

## Gegenstand
1. **Bericht:** `/root/biotop-vor-t4-05/BERICHT.md`. Solange er Platzhalter `‹…›` trägt, prüfst du die ausgefüllten
   Teile. Die Rohbelege liegen daneben.
2. **Kern-Commit:** HEAD von `/root/biotop` (Vorgänger `43b8fad`); `git -C /root/biotop log --oneline -3`;
   `COMMIT-STAT.txt`, `KERN-COMMIT.patch.txt`. Umbauskripte `bau/r5_*.py` (alles-oder-nichts, Protokolle `bau/R5-*.txt`).
3. **Belege:** `/root/biotop-vor-t4-05/`, darin `bau/` (Teilläufe `TEILLAUF-*.txt`, Lesedateien), `proben/`
   (`STUFE2-EICHUNG.*` — Bemessung der eingang-Last; `VORPROBE-E2.txt`, `VORPROBE-ZUSTAND.txt`; `VORHER-43b8fad.*`,
   `NACHHER-HEAD.*`; `T4-GROESSE.txt`), `nachspiel/` (`NACHSPIEL-N1..3.txt`, `n1..n3/*.json`, `VORPROBE-ARBEITSBAUM.txt`),
   `JOB-KETTE.txt`, `REGRESSION.*`, `VERDRAHTUNG-BELEG-*.json`, `KASSE.md`. Einige laufen eventuell noch.
4. **Vorrunde:** `/root/biotop-vor-t4-04/` — `REVIEW.md` (18 Befunde), `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md` (R5-1 …
   R5-14), `review-proben/` (`kammerprobe.py`, `x4probe.py`, `lokal_proben*.py` u. a.).
5. **Auftrag** (Philipp, 24.09., Entscheidungen Chat-Claude zum Review 04; „Runde 5 schließt Klassen, nicht Fälle“):
   1. **Vollständigkeitsprüfung:** Nach jedem Erfassen eines Objekts wird geprüft, ob alle Datenattribute erfasst sind;
      fehlt eines, ist das eine gezählte Enthaltung, nie „0 Abweichungen, tragfähig“. Die Fälle aus Review-Nr. 2, 3, 5 und
      10 sind die Gegenproben; `os.PathLike` wird über `os.fspath` als Wert geführt.
   2. **Festhalten heißt fallende Zusicherung**, keine beliebige Ausnahme (Nr. 1).
   3. **Ein Sondenausfall trifft nur die betroffene Funktion** — ihre Beobachtungen enthalten sich, der Lauf geht weiter
      (Nr. 4); ersetzt werden nur echte Iteratoren, keine Objekte mit Attributen.
   4. **Kappe der Verfälschungsläufe:** zurückstellen mit Grund und gezählt, gemessen an einem Kandidaten in T4-Größe
      (Nr. 6).
   5. **Verdrahtung über ein Register:** Jede Funktion, deren Aufruf der Entwurf verlangt — Organe, Torzeilen, das
      Tor-4-Skript —, steht in einem Register, und der Verdrahtungstest verlangt jeden Eintrag im echten Lauf; das
      Tor-4-Skript wird gebaut und ruft die Torzeile „Schwächen“ (Nr. 7). Für T4 gilt als Normalvergleich einer Altlast
      das Verhalten der Vorgeneration über den Verhaltensvergleich; eine verhaltensändernde Altlast braucht einen
      unabhängigen Test aus der Altlastenliste.
   6. **Der Vorspann verweigert den Lauf ohne Stufe 2**, mit Test bei gestellter Dauer über 60 s (Nr. 8);
      Stufe-2-Lasten werden wie Stufe 1 bemessen und geeicht, bis `eingang` nicht mehr sperrt.
   7. **Lastaufrufe tragen die Formmerkmale ihrer Eingabe** (Nr. 9).
   8. **Aus den niedrigen:** dieselbe Stufe für Eichproben, Toleranz und gespeicherte Maße (Nr. 14, 15); Ausschluss
      eigener Tests nach Testkennung einschließlich Parametrisierung (Nr. 16); das Nachspiel als echter Durchlauf in der
      Regression (Nr. 18).
   Kein Lauf, kein Modellgeld, ein Review, eigener Commit.
6. **Masterprompt** Fassung 8, Tor 4: `bau/MASTERPROMPT-V8-TOR4.txt` (aus der Sitzungsdatenbank gelesen; die frühere
   Cache-Datei existiert nicht mehr).
7. **Lauf-DB** (nur für Nachrechnungen): `/root/biotop-t3/schnappschuss-abschluss3/t3.db`. Öffne sie NUR mit
   `sqlite3.connect('file:…?mode=ro', uri=True)`, nie mit `immutable=1`, nie schreibend. `/root/versiegelt/` nur lesen.

## Was du prüfst
a) **Jeder Auftragspunkt (1–8):** gebaut wie verlangt? Gegenprobe vorhanden, durch den Laufweg (`aegis.pruefen`,
   `lauf._generation_koerper`, Nachspiel, Verdrahtungstest), scheitert sie an der vorgesehenen Zusicherung? Modul-,
   Organ- und Laufweg-Nachweise getrennt. Schließt der Bau die **Klasse** oder nur die Fälle des Reviews 04?
b) **Vollständigkeitsprüfung (1):** Suche Objektarten, bei denen die unabhängige Aufzählung (`object.__getstate__`, im
   TS-Kanon die Eigenschaftsprüfung) selbst blind ist, so dass wieder „0 Abweichungen, tragfähig“ herauskommt —
   eigenes `__getstate__`, Deskriptoren, Properties mit Zustand in Closures, C-Erweiterungstypen, WeakRefs,
   `__slots__` mit `__dict__`, TS-Klassen mit Gettern/privaten Feldern/Closures. Und umgekehrt Fehlalarme: gewöhnliche
   Werte, die jetzt eine Enthaltung auslösen (Enthaltung ist Zurückstellung — kann sie T4-Kandidaten massenhaft
   zurückstellen?).
c) **Festhalten (2):** kann ein Test weiterhin festhalten, ohne das Merkmal zu unterscheiden (z. B. `assert` im Test auf
   ein Folgeergebnis, `pytest.raises` um Werkcode)? Python und TS gleich?
d) **Ausfall je Funktion (3):** Eingrenzung per `os.fork` in der Kammer — Zustandslecks, Zeitlimit (Halbierung),
   Kindprozesse, Ergebnis bei nicht eingrenzbarem Auslöser; TS-Weg (nur Liste der gerufenen Funktionen).
e) **Proben des Gutachtens 04 gegen den neuen Commit** (`review-proben/kammerprobe.py`, Kopien unter deinem
   /tmp-Ordner anpassen): x1–x3, q1, p13–p23. Geschlossen? Neue stille Stellen oder Fehlalarme?
f) **Zahlen gegen ihre Quelle, mit Nenner:** Stufe-2-Eichung, Nachspiele (K2904/K3091 × 3, K2868), Vorher/Nachher,
   T4-Größe, Teilläufe, Regression, Verdrahtung (Register n von n, Tor-4-Zeile, Nachspiel im Verdrahtungstest).
g) **Geänderte ältere Tests:** Spezifikationsänderung oder zugedeckte Regression?
h) **Aussagen, die stärker sind als ihr Beleg,** und **Lücken gegenüber dem Auftrag.**

## Harte Regeln
- Kein Modellaufruf, kein Netz, kein Geld.
- Schreibe NUR `/root/biotop-vor-t4-05/REVIEW.md` und eigene Dateien unter `/tmp/review-vor-t4-05/` (setze `TMPDIR` in
  diesen Ordner). Nichts anderes.
- Kammerläufe (Docker) sind erlaubt, aber keine, solange `job_kette` läuft (`pgrep -f job_kette`). Bis dahin lesen und
  rechnen.
- Keine volle Regression und kein Verdrahtungstest (laufen im Job).
- **Sperren:** Wird ein Befehl blockiert (Sicherheitssperre, Freigabeabfrage, Formatsperre), hältst du mit genau diesem
  Schritt an und berichtest ihn wörtlich mit Befehl und Meldung. Nicht umformulieren, keinen anderen Weg, dieselben
  Daten nicht auf anderem Weg lesen. Was dadurch ungeprüft bleibt, steht unter „Nicht geprüft“. Ein Schritt je Befehl
  (Kopieren, Lesen, Ausführen getrennt), lange oder mehrteilige Befehle als Skript unter `/tmp/review-vor-t4-05/`.
- Budget: etwa 70–80 Werkzeugaufrufe. Danach schreibst du den erreichten Stand.

## Ausgabe (`REVIEW.md`)
- Tabelle `Nr | Schwere (hoch/mittel/niedrig) | Befund | Beleg (Datei:Zeile, Befehl, Messung) | Vorschlag`.
- „Geprüft und bestätigt“ mit Bezugsgrößen (x von y).
- „Nicht geprüft“ mit Grund.
- „Sperren“: jede Sperre wörtlich, oder „keine“.
- Schreibort-Nachweis: alle Dateien, die du geschrieben hast.
