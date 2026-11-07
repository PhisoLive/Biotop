**Es gilt der zweite Reviewdurchgang** (`REVIEW.md`, bytegleich mit `/tmp/review-vor-t4-05/REVIEW.md`, sha256
`f66c7b6a…`). Der erste bleibt als `REVIEW-verworfen-erster-durchgang.md` im Ordner (Entscheidung Philipp, 24.09.). Wie
zwei Durchgänge entstanden, steht in `ZWEI-REVIEWS.md`; kurz:
- Die Hauptsitzung war am Kontextrand, jede Verdichtung scheiterte (Token des Hilfsmodells widerrufen).
- Der Reviewer startete seine Kammerprobe als Hintergrundprozess mit Abschlussmeldung. Die Meldung lief in den Chat und
  band ihn um 21:51:24 an die Sitzung des Reviewers; die Hauptsitzung endete.
- Ab da arbeiteten zwei Instanzen mit demselben Verlauf im selben Ordner: der ursprüngliche Reviewer (schrieb 22:03:48
  `REVIEW.md`) und die Chat-Instanz (fand die Datei vor, schrieb ihren Durchgang nach `/tmp/review-vor-t4-05/REVIEW.md`).
- Beide Durchgänge stützen sich auf dieselben Kammermessungen (36 Fälle, 21:41–21:48, vor der Teilung). Laut
  Delegationsprotokoll führte der erste Durchgang das überschriebene Skript nicht aus; die Wahl des zweiten bleibt davon
  unberührt.
- **Ab Runde 6:** jedes Review in einem eigenen, neuen Ordner; vor dem Start geprüft, dass keines läuft; Reviewer starten
  keine Hintergrundprozesse.

**Befunde des geltenden Durchgangs und Umgang** (Entscheidungen Chat-Claude vom 24.09. zu Runde 6; Spezifikationen in
`SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`):

| Nr | Schwere | Befund | Umgang |
|---|---|---|---|
| 1 | hoch | Typprüfung oder Tautologie im Test hält `tab` fest; der Tab-Rückschritt überlebt `aegis.pruefen` (x5, x5b) | Runde 6, Entscheidung (1): typtreue Verfälschung, zusammen mit R6-4 (R6-6) |
| 2 | hoch | Die Vollständigkeitsprüfung ist blind für Zustand in C-Typen: „0 Abweichungen, tragfähig“ (p24b, p25; lokal 11 Arten) | Entscheidung (2): bekannte Darstellung oder gezählte Enthaltung (R6-7) |
| 3 | hoch | Enthält sich die geänderte Funktion (Sondenausfall), gilt das Urteil als tragfähig (a3x); dieselbe Lücke in R6-1 | Entscheidung (3): geänderte Funktion enthält sich → zurückgestellt; nur unveränderte → Urteil am Rest (R6-1, R6-8) |
| 4 | mittel | Ausnahmen nur nach Typ verglichen, Meldung auf 200 Zeichen gekürzt (p26) | Entscheidung (7): Typ und Inhalt (R6-9) |
| 5 | mittel | Eine hängende Last legt den Kandidaten still (d1, 245 s) | Entscheidung (3): Zeitgrenze je Funktion (R6-10) |
| 6 | mittel | Fehlalarm-Auslöser (f1, f2); an `lagerhaus` und `logmuehle` 0 von 66 Funktionen | f1, f2 als Gegenproben zu R6-1; Zählung an der Vorgeneration des T4-Werks bei der Aufnahme (R6-14) |
| 7 | mittel | Register mit 10 Einträgen; Verhandlung und weitere verlangte Aufrufe fehlen | Entscheidung (6): Register vollständig, Verhandlung im Verdrahtungslauf (R6-11) |
| 8 | mittel | Zweig „verhaltensändernde Altlast“ im Tor-4-Skript unerreichbar (Kennungen, `erlaubt` über alle Altlasten, kein Test) | Entscheidung (5) (R6-2 erweitert, R6-12) |
| 9 | niedrig | §6 mischt die Nenner (Median und Spannweite aus 8 Rauschmessungen, Sperren aus 24) | in §6 berichtigt (hier nachgerechnet: über 24 Messungen `zahlen` 19,0 ms, 0,04 … 0,70) |
| 10 | niedrig | TS-Kanon: 6 blinde Arten, 6 Fehlalarm-Arten (lokal) | Entscheidung (8): vor T5, mit TS-Proben (R6-13) |
| 11 | niedrig | `ITER_KAPPE` 1000 liest zwanzigmal so weit voraus (gerechnet) | auf der Liste: an der T4-Last messen (R6-15) |

**Nur im verworfenen ersten Durchgang, unbestätigt** (auf der Liste als U-1 … U-4, ohne eigene Nachprüfung):
- U-1: `os.fork` in einem Werk mit laufenden Threads kann das Kind der Eingrenzung verklemmen (gelesen).
- U-2: Lastaufrufe tragen seit Entscheidung 7 auch `klein`/`gross`; in x2 sind 16 von 36 ungedeckten Beobachtungen
  Lastaufrufe — eine richtige Behebung braucht für jedes Merkmal jeder Lasteingabe einen festhaltenden Test (Überstrenge).
- U-3: Der TS-Weg prüft nicht „ohne Sonde“ (`last_ohne_sonde`): ein Lastabbruch, der Werkverhalten ist, wird dort zur
  Enthaltung (gelesen).
- U-4: Die Stufen-Zusicherung im Verdrahtungstest filtert `None`; ein Urteil mit Messung ohne Stufe fiele nicht auf
  (gelesen).
