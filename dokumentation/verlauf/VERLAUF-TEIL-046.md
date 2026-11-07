# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 046 von 054

- Einträge V0914 bis V0949. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0914 · 24.09.2026 16:42:27 CEST · Hermes · Nachricht id 16481 · Sitzung `20260924_150913_a9326d` · 3090 B

```text
Der Reviewdurchgang ist fertig und liegt in `/root/biotop-vor-t4-04/REVIEW.md`. Urteil: Die vier hohen Befunde aus Review 03 sind für ihre Probenfälle geschlossen, aber nicht als Fehlerklasse. Es gibt 18 neue Befunde: 2 hoch, 8 mittel, 8 niedrig.

**Was hält**
- Ich habe 14 von 16 Proben aus Gutachten 03 gegen `43b8fad` neu gefahren. Alle 14 verhalten sich wie verlangt.
- Die Gegenprobe zu Entscheidung 1 hält: K2904 und K3091 überleben an Stufe 2 je 3 von 3 Mal. Die `planung`-Quote liegt bei 0,376–0,455.
- Die Gegenprobe zu Entscheidung 3 hält: K2868 wird abgelehnt. 16 von 40 Abweichungen sind gedeckt, darunter die drei ungültigen Randfälle. Ungedeckt bleiben 20 Weißraum- und 4 Zahlform-Abweichungen.
- Die Gegenprobe zu Entscheidung 4 hält, geprüft durch `aegis.pruefen`.
- Die Zahlen des Berichts stimmen, soweit ich sie nachgerechnet habe, mit ihren Quellen überein. Einzige Abweichung: Der Median der Kammerlaufzeiten ist gepoolt 6,2 → 9,8 s statt 6,3 → 9,9 s.

**Hohe Befunde (in der Kammer gemessen)**
1. **Ein Test „hält fest“, ohne das Merkmal zu prüfen.** Es zählt jede Ausnahme im Testlauf, nicht nur eine fallende Zusicherung. Beispiel: Ein Test sichert nur zu, dass zweimaliges Normieren dasselbe ergibt wie einmaliges. Mit ihm überlebt ein Kandidat mit Tab-Rückschritt (x3). Ohne diesen Test wird er abgelehnt.
2. **`__slots__` mit Vererbung bleibt still.** Ändert ein Kandidat nur einen Slot der Basisklasse, findet die Prüfung 0 Abweichungen und nennt das Urteil tragfähig. Ändert er einen Slot der eigenen Klasse, sind es 28 Abweichungen (p22).

**Mittlere Befunde**
- Verschleierte Slot-Namen (`__x`) sind ebenfalls unsichtbar.
- `csv.DictReader` wird weiter ersetzt. Liest die Referenzlast ein Attribut davon (gemessen: `fieldnames`), fällt die Sonde aus, und laut Code wird dann jeder Kandidat des ganzen Laufs zurückgestellt.
- Ändert ein Kandidat nur die Elemente eines Iterator-Objekts, bleibt das still; es wird nur als Teil-Enthaltung gezählt.
- Die Kappe von 24 Verfälschungsläufen führt zur Ablehnung. R4-12 verlangte eine Enthaltung.
- Die Torzeile „Schwächen“ wird nirgends aufgerufen.
- Fehlt die Stufe-2-Last, misst der Lauf ohne Einspruch an Stufe 1 weiter.
- Lastaufrufe gelten immer als gewöhnliches Muster.
- `Path`-Rückgaben sehen für die Sonde alle gleich aus.

Für T4 gefährlich sind Nr. 1, 2, 4, 6, 7, 8 und 10.

**Nicht geprüft:** die JUnit-Zahlen und die Verdrahtungsbelege aus §8, `KASSE.md`, die TypeScript-Zweige, und Generalprobe und Verhandlung an Stufe 2 nur gelesen.

**Sperren:** Ein mehrteiliger Einzeiler von mir löste eine Freigabeabfrage der Sicherheitsprüfung aus. Du hast sie freigegeben, der Befehl lief, brach dann aber an einem Fehler in meinem eigenen Skript ab. Ich habe ihn nicht wiederholt. Befehl und Meldung stehen wörtlich in der Datei, die betroffenen Daten unter „Nicht geprüft“.

Außer `REVIEW.md` habe ich nur unter `/tmp/review-vor-t4-04/` geschrieben. `git status` von `/root/biotop` war vorher und nachher leer.

MEDIA:/root/biotop-vor-t4-04/REVIEW.md
```

### V0915 · 24.09.2026 16:48:07 CEST · Philipp · Nachricht id 16482 · Sitzung `20260924_150913_a9326d` · 2257 B

```text
Runde 4 hat den wichtigsten Punkt geschafft: K2904 und K3091 an der größeren Last drei von drei gleich, weit von der Schwelle. Aber das Review sagt es selbst — geschlossen für die Probenfälle, nicht als Fehlerklasse. Runde 5 schließt Klassen, nicht Fälle; Entscheidungen Chat-Claude: (1) Vollständigkeitsprüfung: Nach jedem Erfassen eines Objekts wird geprüft, ob alle Datenattribute erfasst sind; fehlt eines, ist das eine gezählte Enthaltung, nie „0 Abweichungen, tragfähig". Die Fälle aus Review-Nr. 2, 3, 5 und 10 sind die Gegenproben; os.PathLike wird über os.fspath als Wert geführt. (2) Festhalten heißt fallende Zusicherung, keine beliebige Ausnahme (Nr. 1). (3) Ein Sondenausfall trifft nur die betroffene Funktion — ihre Beobachtungen enthalten sich, der Lauf geht weiter (Nr. 4); ersetzt werden nur echte Iteratoren, keine Objekte mit Attributen. (4) Kappe der Verfälschungsläufe: zurückstellen mit Grund und gezählt, gemessen an einem Kandidaten in T4-Größe (Nr. 6). (5) Verdrahtung über ein Register: Jede Funktion, deren Aufruf der Entwurf verlangt — Organe, Torzeilen, das Tor-4-Skript —, steht in einem Register, und der Verdrahtungstest verlangt jeden Eintrag im echten Lauf; das Tor-4-Skript wird gebaut und ruft die Torzeile „Schwächen" (Nr. 7) — zum dritten Mal war etwas gebaut und nie gerufen. Für T4 gilt als Normalvergleich einer Altlast das Verhalten der Vorgeneration über den Verhaltensvergleich; eine verhaltensändernde Altlast braucht einen unabhängigen Test aus der Altlastenliste. (6) Der Vorspann verweigert den Lauf ohne Stufe 2, mit Test bei gestellter Dauer über 60 s (Nr. 8); Stufe-2-Lasten werden wie Stufe 1 bemessen und geeicht, bis eingang nicht mehr sperrt. (7) Lastaufrufe tragen die Formmerkmale ihrer Eingabe (Nr. 9). (8) Aus den niedrigen: dieselbe Stufe für Eichproben, Toleranz und gespeicherte Maße (Nr. 14, 15); Ausschluss eigener Tests nach Testkennung einschließlich Parametrisierung (Nr. 16) — sonst unterläuft ein parametrisierter Test Entscheidung 4; das Nachspiel als echter Durchlauf in der Regression (Nr. 18). Kein Lauf, kein Modellgeld, ein Review, eigener Commit, laeufe/biotop-vor-t4-05/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

### V0916 · 24.09.2026 16:56:56 CEST · Hermes-Zwischentext · Nachricht id 16487 · Sitzung `20260924_150913_a9326d` · 95 B

```text
Ich beginne Runde 5: Arbeitsordner, Übergabe und Wächter zuerst, dann gezielt den Code lesen.
```

### V0917 · 24.09.2026 17:00:16 CEST · Hermes · Nachricht id 16498 · Sitzung `20260924_150913_a9326d` · 3756 B

```text
Mein Durchgang ist fertig, aber `/root/biotop-vor-t4-04/REVIEW.md` stammt nicht von mir. Die Datei entstand um 16:42:10 (33.169 Bytes), während ich prüfte. Ihr Kopf beschreibt meinen eigenen Kammerlauf von 16:08–16:10 als ihren. Außerdem lag in meinem Ordner ein fremdes `abschluss.sh` (16:22). Offenbar lief eine zweite Instanz desselben Auftrags auf meinem Verlauf und meinem `/tmp`-Ordner. Ich habe die fremde Datei nicht überschrieben, weil das ihr Ergebnis unwiderruflich gelöscht hätte. Meine Fassung liegt deshalb in `/tmp/review-vor-t4-04/REVIEW-B.md` (sha256 `f265ea09…2f5e`).

**Du musst entscheiden, welche Fassung gilt.** Beide stützen sich auf denselben Kammerlauf und sind darin nicht unabhängig. Nur meine Fassung enthält die Probe x4 (Befund Nr. 1).

**Befunde: 19 in meiner Fassung, davon 3 hoch, 8 mittel, 8 niedrig.** Die vier hohen Befunde aus Review 03 sind für ihre Probenfälle geschlossen: Ich habe 14 der 16 alten Fallläufe gegen `43b8fad` wiederholt, alle verhalten sich wie spezifiziert. Die Gegenproben des Auftrags halten: K2904 und K3091 werden in 3 von 3 Durchgängen gleich entschieden, K2868 mit 16 gedeckten und 24 ungedeckten Abweichungen abgelehnt, E4 abgelehnt.

**Die wichtigsten 5 Befunde:**
1. **Hoch:** Ein Kandidat, dessen Rückschritt nur bei Eingaben ab 40 Zeichen greift (`ValueError`), überlebt `aegis.pruefen` (Probe x4). Grund ist die Lesart „Randwerte tragen kein Merkmal“: Randfall-Abweichungen haben damit das gewöhnliche Muster, und das deckt jeder festhaltende Test, auch ohne lange Eingabe.
2. **Hoch:** „Hält fest“ misst nicht, ob die Zusicherung fällt. Eine Eigenschafts-Zusicherung wie `normieren(normieren(x)) == normieren(x)` mit Tab zählt als festhaltend, obwohl der Rückschritt sie erfüllt. Der Kandidat überlebt, 6 von 6 Rückschritt-Beobachtungen gelten als gedeckt (Probe x3).
3. **Hoch:** `__slots__` sind nur für flache Klassen geschlossen. Ändert eine Methode einen geerbten Slot (p22) oder einen verschleierten `__x`-Slot (p21), gibt es 0 Abweichungen und das Urteil lautet „tragfähig“. Die Kontrollen zeigen 28 Abweichungen.
4. **Mittel:** Die Stufe 2 ist nicht in jedem Bereich zehnfach, sondern in 4 von 5. `tarife` ruft dieselben 150 Eingaben nur zehnmal auf. Außerdem gibt es die Stufe 2 nur für das T3-Werk: Jedes andere Werk fällt beim Laufstart ohne Warnung auf Stufe 1 zurück, und dieser Zweig läuft in keinem Test.
5. **Mittel:** Die Torzeile „Schwächen“ hat außer Tests und Belegskript keinen Aufrufer und ist damit nicht verbindlich verdrahtet. Für T4 lässt sie sich so nicht anwenden: Der Masterprompt sieht dort eine Altlastenliste ohne Normalversion vor, also wäre jede Altlast „nicht beurteilbar“ und die Zeile stünde immer bei 0 %.

Weitere mittlere Befunde:
- Die Stufe-2-Last von `eingang` wird in 3 von 7 Rauschmessungen gesperrt; an Stufe 1 in den Läufen 37/38 in keinem der 10 Bereiche.
- In den gespeicherten Maßen mischen sich Werte von Stufe 1 und Stufe 2.
- Wird ein zurückgegebenes Iterator-Objekt geändert, bleibt das unsichtbar, und das Urteil lautet trotzdem „tragfähig“.
- `csv.DictReader` wird ersetzt; jeder Kandidat eines solchen Werks wird zurückgestellt.

**Sperren:** keine.

**Schreibort-Nachweis:**
- Ich habe nur unter `/tmp/review-vor-t4-04/` geschrieben: `REVIEW-B.md`, die Proben- und Suchskripte mit ihren Ausgaben (`kammerprobe.py`, `x4probe.py`, `KAMMERPROBE.json`, `X4PROBE.json` u. a.), `werke/` mit 54 Probenwerk-Dateien und `tmp/` (am Ende leer). Die vollständige Liste steht in `REVIEW-B.md`.
- Unter `/root/` habe ich nichts geschrieben; `git status` von `/root/biotop` war am Ende leer.
- Die Lauf-DB war nur mit `mode=ro` geöffnet. Am Ende lief kein Container mehr.
```

### V0918 · 24.09.2026 17:11:04 CEST · Hermes-Zwischentext · Nachricht id 16506 · Sitzung `20260924_150913_a9326d` · 85 B

```text
Schritt 0: Runde 4 abschließen. Zuerst die Review-Proben kopieren (eigener Schritt).
```

### V0919 · 24.09.2026 17:19:52 CEST · Hermes-Zwischentext · Nachricht id 16517 · Sitzung `20260924_150913_a9326d` · 82 B

```text
Bericht 4 ist gefüllt. Jetzt die Veröffentlichung von Runde 4 (eigener Schritt).
```

### V0920 · 24.09.2026 17:28:23 CEST · Hermes-Zwischentext · Nachricht id 16534 · Sitzung `20260924_150913_a9326d` · 60 B

```text
Ich lese jetzt gebündelt die Stellen, die Runde 5 berührt.
```

### V0921 · 24.09.2026 18:38:23 CEST · Hermes-Zwischentext · Nachricht id 16585 · Sitzung `20260924_150913_a9326d` · 75 B

```text
Eichung läuft im Hintergrund. Ich lese die letzten Anker für die Patches.
```

### V0922 · 24.09.2026 19:00:50 CEST · Hermes-Zwischentext · Nachricht id 16596 · Sitzung `20260924_150913_a9326d` · 173 B

```text
Die Vorprobe bestätigt die Regel für E2 (Absturzstelle = Testdatei, Meldung `AssertionError`/`Failed`), lokal und in der Kammer. Jetzt das Patchskript (alles-oder-nichts).
```

### V0923 · 24.09.2026 19:03:47 CEST · Hermes-Zwischentext · Nachricht id 16603 · Sitzung `20260924_150913_a9326d` · 135 B

```text
Die Vorproben stehen (Stufe 2: `eingang` mit W 240 in 0 von 8 Rauschmessungen gesperrt, mit W 60 in 3 von 8). Jetzt den Umbau anwenden.
```

### V0924 · 24.09.2026 19:04:00 CEST · Hermes-Zwischentext · Nachricht id 16608 · Sitzung `20260924_150913_a9326d` · 123 B

```text
Umbau angewandt (61 Ersetzungen in 10 Dateien). Jetzt der Diff der Signaturen und Importe gegen HEAD sowie ein Syntaxcheck.
```

### V0925 · 24.09.2026 19:08:58 CEST · Hermes-Zwischentext · Nachricht id 16611 · Sitzung `20260924_150913_a9326d` · 82 B

```text
Umbau Teil 1 steht, Syntax sauber. Jetzt Tor-4-Skript und Register (neue Dateien).
```

### V0926 · 24.09.2026 19:12:30 CEST · Hermes-Zwischentext · Nachricht id 16619 · Sitzung `20260924_150913_a9326d` · 115 B

```text
Jetzt die Tests: Drahtwerk um Stufe 2 und Altlastenliste erweitern, Verdrahtungstest um Register und Tor-4-Schritt.
```

### V0927 · 24.09.2026 19:20:59 CEST · Hermes-Zwischentext · Nachricht id 16625 · Sitzung `20260924_150913_a9326d` · 68 B

```text
Jetzt die neue Testdatei mit Proben und Gegenproben je Entscheidung.
```

### V0928 · 24.09.2026 19:21:08 CEST · Hermes-Zwischentext · Nachricht id 16627 · Sitzung `20260924_150913_a9326d` · 115 B

```text
Die Pyright-Meldungen betreffen nur Typannahmen, nicht die Laufzeit. Erster Teillauf über die neue Datei (Kammer).
```

### V0929 · 24.09.2026 19:21:17 CEST · Hermes-Zwischentext · Nachricht id 16630 · Sitzung `20260924_150913_a9326d` · 170 B

```text
Während der Teillauf läuft, bereite ich die zweite Hälfte vor: den Nachspiel-Durchlauf in der Regression (Entscheidung 8, Review-Nr. 18) und die Messung in T4-Größe.
```

### V0930 · 24.09.2026 19:33:19 CEST · Hermes-Zwischentext · Nachricht id 16649 · Sitzung `20260924_150913_a9326d` · 194 B

```text
Die gestellten Sonden in älteren Tests nehmen `**k` an, `transparent` passt also. Jetzt ein breiter Teillauf mit allen Sonden-, Aegis- und Wächter-Tests (ohne Verdrahtung), als Hintergrundjob.
```

### V0931 · 24.09.2026 19:34:05 CEST · Hermes-Zwischentext · Nachricht id 16656 · Sitzung `20260924_150913_a9326d` · 111 B

```text
Während Teillauf 2 läuft, schreibe ich die Messung in T4-Größe (Entscheidung 4) als eigenständiges Skript.
```

### V0932 · 24.09.2026 19:35:22 CEST · Hermes-Zwischentext · Nachricht id 16666 · Sitzung `20260924_150913_a9326d` · 58 B

```text
Warte auf Teillauf 2 (breite Regression ohne Verdrahtung).
```

### V0933 · 24.09.2026 19:42:33 CEST · Hermes-Zwischentext · Nachricht id 16670 · Sitzung `20260924_150913_a9326d` · 55 B

```text
Bis 72 % ohne einen Fehlschlag. Ich warte auf das Ende.
```

### V0934 · 24.09.2026 19:52:40 CEST · Hermes-Zwischentext · Nachricht id 16683 · Sitzung `20260924_150913_a9326d` · 95 B

```text
Die Kette läuft (Verdrahtungstest). Ich schreibe inzwischen `KASSE.md` und das Berichtgerüst.
```

### V0935 · 24.09.2026 20:07:38 CEST · Hermes-Zwischentext · Nachricht id 16690 · Sitzung `20260924_150913_a9326d` · 163 B

```text
Der Verdrahtungstest läuft noch (in Runde 4 dauerte er rund 17 Minuten, jetzt kommen Nachspiel und Tor 4 dazu). Ich bereite derweil die Füllung des Berichts vor.
```

### V0936 · 24.09.2026 20:11:48 CEST · Hermes-Zwischentext · Nachricht id 16695 · Sitzung `20260924_150913_a9326d` · 94 B

```text
Der Verdrahtungstest läuft seit 24 Minuten und ist aktiv (Kammer arbeitet). Ich warte weiter.
```

### V0937 · 24.09.2026 20:19:00 CEST · Hermes-Zwischentext · Nachricht id 16699 · Sitzung `20260924_150913_a9326d` · 116 B

```text
Verdrahtungstest grün (6 von 6, 28:39 min, mit Register, Tor-4-Skript und Nachspiel-Durchlauf). Teillauf 3b läuft.
```

### V0938 · 24.09.2026 20:25:19 CEST · Hermes-Zwischentext · Nachricht id 16702 · Sitzung `20260924_150913_a9326d` · 137 B

```text
Commit `0c2f058` steht (Teillauf 3: 6 + 132 grün, Vorprobe K2904 überlebt). Jetzt das Berichtgerüst und dann der eine Reviewdurchgang.
```

### V0939 · 24.09.2026 20:31:20 CEST · Hermes-Zwischentext · Nachricht id 16710 · Sitzung `20260924_150913_a9326d` · 82 B

```text
Jetzt der eine Reviewdurchgang (Subagent, wartet mit Kammerläufen auf die Kette).
```

### V0940 · 24.09.2026 20:31:43 CEST · Hermes · Nachricht id 16729 · Sitzung `20260924_150913_a9326d` · 2367 B

```text
Runde 5 ist gebaut und als `0c2f058` committet, aber noch nicht abgenommen und nicht geliefert. Regression, Nachspiele, Vorher/Nachher und die Messung in T4-Größe laufen noch als Hintergrundjob; der eine Reviewdurchgang ist gestartet.

**Runde 4 nachgeliefert:** Der Bericht der Runde 4 hatte noch Platzhalter und lag nicht im Prüfkanal. Er ist jetzt aus den Belegen gefüllt und veröffentlicht, 103 von 103 Dateien über HTTPS bytegleich:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-04/BERICHT.md
Ordnerprüfsumme: `c02d0dce9ad5996215f0d723a006a4ae2c0495ab2e051a7d0a4d73e7988c3f12`

**Stand vor dem Commit:**
- **Teilläufe:** Der Verdrahtungstest ist grün (6 von 6), jetzt mit Register (10 Einträge), Tor-4-Schritt und einem echten Nachspiel-Durchlauf. Die neuen und berührten Testdateien sind 132 von 132 grün. Ein Nachspiel K2904 am Arbeitsbaum hat überlebt. Der breite Teillauf über alle übrigen Testdateien hatte 1 von 594 Fällen rot, einen eigenen Testfehler; er ist behoben und die Datei im Teillauf danach grün.
- **Stufe 2, `eingang`:** Mit 60 Wiederholungen sperrte die Rauschmessung `eingang` in 3 von 8 Messungen, mit 240 in 0 von 8; der längste Kammerlauf dauerte 12,3 s. Gewählt sind 240.
- **Die acht Entscheidungen sind gebaut**, je mit Gegenprobe. Zwei Abweichungen vom Wortlaut:
  - Bei unvollständiger Erfassung enthält sich der ganze Verhaltensvergleich und der Kandidat wird zurückgestellt, auch wenn er die betroffene Funktion nicht geändert hat.
  - Die Iterator-Kappe liegt jetzt bei 1000 statt 50. Mit 50 riss die Sonde die Kappe mit ihren eigenen Testeingaben und enthielt sich dann selbst.

**Noch offen:**
- **Belege für Entscheidung 3 (TypeScript):** Das Enthalten nur der betroffenen Funktionen hat in TypeScript keine eigene Probe.
- **Belege für Entscheidung 2 (TypeScript):** Dass eine Ausnahme aus Werkcode nichts festhält, ist nur in Python geprüft.
- **Lastaufrufe (Entscheidung 7):** Es fehlt eine Gegenprobe mit einem deckenden Test.
- **Tor-4-Skript:** Es berechnet nur die Zeile „Schwächen“, die übrigen Tor-4-Zeilen stehen dort als „nicht berechnet“.

Die Übergabe ist in `/root/biotop-vor-t4-05/UEBERGABE.md` nachgeführt. Wenn Job und Review fertig sind, fülle ich den Bericht, arbeite die Befunde ein und veröffentliche die Runde.
```

### V0941 · 24.09.2026 20:32:17 CEST · Hermes · Nachricht id 16735 · Sitzung `20260924_150913_a9326d` · 264 B

```text
Nichts Neues: Die beiden Meldungen gehören zu Teillauf 1 und 2, die schon ausgewertet und behoben sind. Die Kette an `0c2f058` steckt noch in der vollen Regression, der Reviewdurchgang läuft. Sobald beide fertig sind, melde ich mich mit Bericht und Abholadresse.
```

### V0942 · 24.09.2026 21:00:41 CEST · Philipp · Nachricht id 16769 · Sitzung `20260924_150913_a9326d` · 801 B

```text
Kein Eingriff in den laufenden Job, nur zwei Punkte für den Bericht: (1) Die Abweichung „bei unvollständiger Erfassung enthält sich der ganze Vergleich" widerspricht Entscheidung 3 und schafft denselben Totalausfall wie Review-Nr. 4 — ein einziges schwer erfassbares Objekt stellt jeden Kandidaten zurück; als rote Spezifikation vor T4: Enthalten muss sich nur die betroffene Beobachtung. (2) Für eingang an Stufe 2 die Stichprobendauer bei 60 und bei 240 Wiederholungen — mein Auftrag „bis eingang nicht mehr sperrt" war ein Fehler, er richtet die Last nach dem Ergebnis; nur die Dauer zeigt, ob 240 nach Maß gewählt ist. Und auf die Liste vor T4: Das Tor-4-Skript berechnet jede Zeile, die aus der Datenbank berechenbar ist — die meisten Berichtsfehler in T3 waren Torzeilen von Han
```

### V0943 · 24.09.2026 21:06:55 CEST · Hermes-Zwischentext · Nachricht id 16784 · Sitzung `20260924_150913_a9326d` · 141 B

```text
Beide Spezifikationen sind rot an `0c2f058`, beide Gegenproben grün (2 von 2). Jetzt trage ich die drei Punkte in Bericht und Übergabe ein.
```

### V0944 · 24.09.2026 21:08:23 CEST · Hermes · Nachricht id 16793 · Sitzung `20260924_150913_a9326d` · 2659 B

```text
Alle drei Punkte stehen im Bericht; in den laufenden Job habe ich nicht eingegriffen. Ich habe nur ohne Kammer gelesen, gerechnet und einen Unit-Test von 0,09 s laufen lassen.

**1. Enthaltung des ganzen Vergleichs → rote Spezifikation R6-1 vor T4**
- Du hast recht. Im Bericht steht §13 Nr. 1 jetzt als falsche Entscheidung und §14 Nr. 7 als eigener Fehler. Ich hatte das Risiko nur als offen notiert, statt es gegen Entscheidung 3 zu prüfen.
- Am Organ ist die Spezifikation an `0c2f058` rot: Der ganze Vergleich enthält sich, obwohl nur die unveränderte Funktion `g` schwer erfassbar ist und nichts abweicht. Die beiden Gegenproben sind grün: Ohne das Objekt wird geurteilt (2 von 2 beobachtet), und eine echte ungedeckte Abweichung lehnt weiter ab.
- Eine Fassung durch `aegis.pruefen` ist vorbereitet: die richtige `normieren`-Behebung plus eine unveränderte Funktion, die ein `StringIO` liefert. Sie läuft erst, wenn der Job fertig ist.

**2. Stichprobendauer `eingang`, Stufe 2** (je 40 Werte aus derselben Eichung)
- 60 Wiederholungen: Median 35,1 ms (29,3 … 71,2), Spannweite je Rauschmessung 0,53 … 0,92, gesperrt in 3 von 8.
- 240 Wiederholungen: 170,5 ms (141,3 … 189,1), Spannweite 0,05 … 0,21, gesperrt in 0 von 8.
- 480 Wiederholungen: 317,1 ms, gesperrt in 0 von 8.
- Zum Vergleich: `zahlen` braucht an Stufe 2 nur 18,9 ms und sperrt in keiner Messung. An Stufe 1 lag `eingang` bei 2,4 … 2,9 ms.
- **Ergebnis: 240 ist nicht nach Maß gewählt, sondern nach der Sperrzahl.** Nach der einzigen festgeschriebenen Regel („einige zehn Millisekunden“, aus Stufe 1) hätten schon 60 gereicht. `zahlen` zeigt außerdem, dass die Dauer allein die Sperren nicht erklärt.
- Eine vorab festgelegte Dauerregel ist jetzt R6-3. Den Wert entscheidest du (Offen Nr. 5). Die Nachspiele dieser Runde laufen noch mit 240.

**3. Tor-4-Skript → R6-2 auf der Liste vor T4**
- Die Spezifikation ist an `0c2f058` rot: Das Skript berechnet nur „Schwächen“.
- Nach meiner Einteilung sind 10 der übrigen 13 Zeilen aus der Datenbank berechenbar. Nicht berechenbar sind Aufnahme, Verdrahtung und Reviewdurchgang/Zwischenbericht. Die Einteilung ist im nächsten Auftrag Zeile für Zeile nachzuweisen.

Deine Nachricht endet mitten im Wort („von Han…“); ich habe „von Hand“ gelesen. Falls danach noch etwas kam, ist es nicht angekommen.

Die Regression an `0c2f058` läuft noch, der Reviewdurchgang ebenfalls. Danach fülle ich den Bericht und veröffentliche.

Dateien in `/root/biotop-vor-t4-05/`:
- `spez/test_spez_r6_unit.py`
- `spez/SPEZ-R6-UNIT.txt`
- `proben/STUFE2-EINGANG-DAUER.txt`
- `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`
```

### V0945 · 24.09.2026 21:50:08 CEST · Hermes-Zwischentext · Nachricht id 16863 · Sitzung `20260924_150913_a9326d` · 184 B

```text
The fourth "API" hit is a false match: the `SondeAusgefallen` message quotes `AttributeError` from the load. I classify by exception type at the start of the message, not by substring.
```

### V0946 · 24.09.2026 21:51:18 CEST · Hermes · Nachricht id 16871 · Sitzung `20260924_150913_a9326d` · 3071 B

```text
Runde 5 ist **nicht abgenommen**. An `0c2f058` sind zwei Messfehler gemessen, die T4 gefährden. Beide sind als rote Spezifikation vor T4 gefasst und nicht nachträglich gebaut.

1. **R6-1, dein Hinweis, jetzt auch durch den Laufweg rot.** Eine richtige Behebung plus eine *unveränderte* Funktion, die ein `StringIO` liefert: Der Kandidat wird zurückgestellt, weil sich der ganze Vergleich enthält. Ohne diese Funktion überlebt er.
2. **R6-4, neuer eigener Befund.** Ein Test wie `assert f(1) == 3` hält nichts fest. pytest meldet solche Zusicherungen ohne das Präfix „AssertionError:“ (gemessen mit pytest 8.3.3 in der Kammer und 9.1.1 lokal), und die Regel aus Entscheidung 2 verlangt genau dieses Präfix.
   - Die Spezifikation führt echtes pytest aus: rot in 3 von 3 Fällen (Zahl, Liste, Wahrheitswert); die 2 Gegenproben (Text hält fest, Werk-Ausnahme nicht) sind grün.
   - Folge: In der T4-Größen-Messung hält für 5 von 8 geänderten Funktionen kein Test fest.
   - Meine Vorprobe hatte nur Zusicherungen mit Text geprüft. Das steht als eigener Fehler im Bericht.

**Was hält, gemessen an `0c2f058`:**
- **Nachspiele:** K2904 und K3091 überleben je 3 von 3 (`planung`-Quote 0,376 … 0,420, alle Gewinne klar). `eingang` war in 0 von 6 Nachspielen gesperrt, in Runde 4 in 3 von 6. K2868 wird abgelehnt, 20 von 40 Abweichungen ungedeckt.
- **Regression:** 598 bestanden, 2 übersprungen, 0 rot. Die Verdrahtung ist grün:
  - 23 von 23 Organen gerufen, 10 von 10 Registerkanten im echten Lauf;
  - Tor-4-Zeile „Schwächen“: Altlast A1 doppelt geprüft und behoben;
  - das Nachspiel im Verdrahtungstest urteilt wie der Lauf; 0,00 € Modellgeld.
- **Vorher/Nachher:** Die 27 neuen Fälle waren an `43b8fad` 9 von 27 grün, an `0c2f058` sind sie 27 von 27. 3 der 18 roten Fälle scheiterten an einer fehlenden Schnittstelle, nicht am Verhalten.
- **Entscheidung 4 ist nicht erfüllt.** Gemessen ist nur der Bedarf eines breiten Kandidaten: 35 Verfälschungsläufe, bei Kappe 24 also 11 ausgelassen. Das Werk hat aber nur 126 Zeilen, und das Urteil ist wegen R6-4 nicht verwertbar. Neu zu messen am echten T4-Werk (R6-5).

**Zu entscheiden, im Bericht als Offen 1–5 mit Optionen:**
1. R6-4 vor T4 bauen? Empfohlen: ja, zusammen mit R6-1 und R6-2.
2. Die Einteilung der 10 aus der Datenbank berechenbaren Tor-4-Zeilen (R6-2).
3. Maß der Stufe-2-Last: empfohlen eine Mindestdauer der Stichprobe, z. B. 100 ms Median. `zahlen` (18,9 ms) und `tarife` (96,0 ms) wären dann neu zu bemessen.
4. Die Kappe neu am echten T4-Werk messen.
5. TypeScript-Proben für die Entscheidungen 2 und 3 erst vor T5 (T4 ist Python).

**Was noch fehlt:**
- Der Bericht ist aus den Belegen gefüllt; offen sind nur §11 (Review) und §12 (Sperren).
- Der Reviewdurchgang läuft noch. Er hat seinen Prüfauftrag vor R6-1 (Laufweg) und R6-4 bekommen und kennt diese beiden Befunde nicht.
- Das Veröffentlichungsskript ist vorbereitet. Wenn das Review da ist, arbeite ich die Befunde ein, veröffentliche und schicke die Endmeldung mit Abholadresse und Prüfsumme.
```

### V0947 · 24.09.2026 22:04:07 CEST · Hermes · Nachricht id 16889 · Sitzung `20260924_203120_e6c401` · 3701 B

```text
Der Reviewdurchgang ist fertig und steht in `/root/biotop-vor-t4-05/REVIEW.md`: 12 Befunde, davon 3 hoch, 6 mittel und 3 niedrig. Keine Sperre.

**Ergebnis:** Die Fälle aus Review 04 sind geschlossen, die Klassen aber nicht.
- **Fälle:** Alle 24 Proben des Gutachtens 04 habe ich an `0c2f058` neu gefahren. Die damaligen stillen Stellen x3, q1, p21, p22 und p18c verhalten sich jetzt wie spezifiziert, p14 wird sichtbar, und unter den 24 zeigt sich keine neue stille Stelle.
- **Zahlen:** Regression (598 bestanden, 2 übersprungen, 0 fehlgeschlagen), Verdrahtung (Register 10 von 10, Tor-4-Zeile, Nachspiel in 2 von 2 Belegen), Nachspiele (7 von 7 wie erwartet, `eingang` in 0 von 6 gesperrt), Vorher/Nachher (9 → 27 von 27), Stufe-2-Eichung und T4-Messung stimmen mit ihren Quellen überein.

**Hohe Befunde:**
1. **Festhalten ohne Unterscheidung (x5, x5b):** Eine `isinstance`-Zusicherung oder ein Selbstvergleich hält `tab` fest. Dadurch überlebt ein Tab-Rückschritt `aegis.pruefen`, gemessen in der Kammer mit 6 von 6 Beobachtungen gedeckt.
2. **Gewöhnliche `assert f(1) == 3` halten nichts fest:** 3 von 5 Formen, lokal gemessen mit pytest 9.1.1, noch nicht in der Kammer. Das deckt sich mit R6-4 des Auftragnehmers. Es ist auch der Grund, warum die T4-Messung Entscheidung 4 nicht belegen kann.
3. **Die Vollständigkeitsprüfung ist selbst blind:** Zustand in C-Typen sieht sie nicht, z. B. StringIO als Argument (p24b) oder eine Decimal-Unterklasse (p25). Beides ergibt in der Kammer „0 Abweichungen, tragfähig“. Lokal bleiben 13 von 13 Python-Paaren mit verschiedenem Zustand ohne Meldung. Im TS-Kanon sind 6 von 6 blind, weil Array, Map, Set, Error und Date gar nicht geprüft werden.

**Mittlere Befunde:**
4. **Fehlalarm:** Eine unveränderte Funktion stellt das ganze Urteil zurück (f1, f2). An `lagerhaus` und `logmuehle` war allerdings 0 von 66 Funktionen unvollständig erfasst.
5. **Sondenausfall einer geänderten Funktion:** Ändert der Kandidat genau diese Funktion, bleibt das Urteil tragfähig (a3x).
6. **Geworfene Ausnahmen:** Sie werden nur mit ihrem Typ verglichen; eine geänderte Meldung bleibt unsichtbar (p26).
7. **Hängende Last:** Sie führt nach 240 s zum Messgerätausfall für den ganzen Kandidaten (d1); die Eingrenzung hat keine Frist.
8. **T4-Messung:** Sie belegt Entscheidung 4 nicht; der Enthaltungszweig tritt nicht ein, und die Größe (126 Zeilen) ist nirgends als T4-Größe festgelegt.
9. **Tor-4-Skript:** Der Zweig für verhaltensändernde Altlasten hat keinen Test. Gelesen: Die Kennungsformen passen nicht zusammen, und die unabhängigen Tests aller Altlasten werden zusammengefasst.

**Nicht geprüft:** vor allem die um 21:50 gefüllte Berichtsfassung außer §4, §9 und dem Anfang von „Ergebnis“, dazu `spez/*`, TypeScript in der Kammer und Nr. 2 mit pytest 8.3.3. Ob sich meine Kammerläufe (21:41–21:48, nach Ende von `job_kette`) mit `job_nach_kette.sh` des Auftragnehmers überschnitten, habe ich nicht geprüft; meine Proben messen keine Zeiten.

**Hinweis:** Die erste Fassung meines Warteskripts lief in das 420-s-Limit des Werkzeugaufrufs. Das war keine Sperre; danach habe ich mit kürzerer Schleife gewartet.

**Dateien:**
- geschrieben: nur `/root/biotop-vor-t4-05/REVIEW.md`, dazu Skripte, Probenwerke und Ausgaben unter `/tmp/review-vor-t4-05/` (`tmp/` am Ende leer).
- Die wichtigsten Belege sind `kammerprobe05.py`, `kammerprobe05.out.txt` und `KAMMERPROBE05.json` (36 Fälle), `lokal_b.*`, `lokal_ts.*` und `e2b_probe.*`.
- Kein Modellaufruf und kein Netz; die Lauf-DB habe ich nicht geöffnet. `git status` von `/root/biotop` war vorher und nachher leer, am Ende liefen 0 Container.

Etwa 68 Werkzeugaufrufe.
```

### V0948 · 24.09.2026 22:24:36 CEST · Hermes · Nachricht id 16900 · Sitzung `20260924_203120_e6c401` · 2683 B

```text
I've finished the review but did not write it to `/root/biotop-vor-t4-05/REVIEW.md`. That file already held a complete review from a second reviewer started in parallel (22:03:48, 229 lines, subagent `sa-0-816c6469`). Overwriting it would have destroyed that review, so mine is here:

`/tmp/review-vor-t4-05/REVIEW.md`

Two reviews break the "one review" rule, so you need to pick one. If you pick mine, copying it to `/root/biotop-vor-t4-05/REVIEW.md` is one step. I didn't read the other reviewer's text.

**Verdict:** I agree with "nicht abgenommen". All 24 probes from Review 04 behave as specified against `0c2f058`. The report's numbers hold wherever I recalculated them, and its own findings R6-1 and R6-4 match my measurements. But the classes of error are not closed. I found three high-severity problems, all measured in the real chamber:
1. **A test still counts as "holding" a feature it doesn't distinguish.** With `assert isinstance(normieren("a\tb c"), str)` or a self-comparison in the test, the tab regression passes `aegis.pruefen` (probes x5 and x5b). Fixing R6-4 on its own would widen this gap, so the two need to be built together.
2. **The completeness check is itself blind to state held in C types.** A `StringIO` argument (p24b) and a `Decimal` subclass return value (p25) again give "0 Abweichungen, tragfähig". Locally, 11 kinds of object are blind.
3. **If the one function the candidate changed abstains, the verdict still counts as passed** (probe a3x, sensor failure). R6-1 as the report plans it would carry this gap over to every incompletely captured function.

**Medium and low:**
- Exceptions are compared by type only (p26).
- A load that hangs under the probe hits the 240 s limit and knocks out the whole candidate (d1).
- More false alarms than R6-1's example, but none on the two practice codebases: 0 of 42 functions in `lagerhaus`, 0 of 24 in `logmuehle`.
- The register has only 10 entries; the negotiation step (Verhandlung) isn't registered.
- In the Tor-4 script, the branch for a behaviour-changing legacy item is effectively unreachable.
- Three low findings: a mixed denominator in §6, gaps and false alarms in the TypeScript canon, and the cost of `ITER_KAPPE` 1000.

**Mistake of mine:** Both reviewers used the same `/tmp/review-vor-t4-05/` folder. At about 22:02 I overwrote the other reviewer's `abschluss.sh` without reading it; the tool only warned me after the write, and its content is lost. The files `bericht_neu.sh`, `e2b*` and `__pycache__` in that folder are theirs.

No blocks, no model calls, no network. Nothing written under `/root/`. `git status` was empty before and after, and no containers were left running.
```

### V0949 · 24.09.2026 23:15:27 CEST · Philipp · Nachricht id 16901 · Sitzung `20260924_203120_e6c401` · 2448 B · 2 gleiche Zeilen zusammengefasst

```text
Zuerst Runde 5 abschließen: Es gilt das zweite Review (/tmp/review-vor-t4-05/REVIEW.md) — seine Messungen sind nachweislich eigene; beim ersten ist nicht auszuschließen, dass es das überschriebene Skript ausgeführt hat. Das erste bleibt im Ordner als verworfen; was nur es fand, kommt als unbestätigt auf die Liste. Erklär im Bericht, wie zwei Reviews entstehen konnten; künftig bekommt jedes Review einen eigenen Ordner, und du prüfst vor dem Start, dass keines läuft. Dann §11 und §12 füllen, veröffentlichen, Endmeldung. Dann Runde 6 — Entscheidungen Chat-Claude: (1) R6-4 nur zusammen mit einer typtreuen Verfälschung: verfälscht wird mit einem Wert desselben Typs und anderen Inhalts, nie mit einem Objekt, das beim Weiterrechnen wirft; ein Test hält nur fest, wenn seine Zusicherung am geänderten Wert fällt (Review-Nr. 1, Proben x5 und x5b). (2) Undurchsichtige Objekte: Zustand aus C-Typen wird über eine bekannte Darstellung erfasst (etwa getvalue, str, pickle), sonst ist die Beobachtung eine gezählte Enthaltung — nie „0 Abweichungen" (Nr. 2, p24b, p25). (3) R6-1 zusammen mit der Lücke aus Nr. 3: Enthält sich eine geänderte Funktion, wird der Kandidat zurückgestellt; enthalten sich nur unveränderte, wird am Rest geurteilt — meine Entscheidung 3 ließ das offen. Dasselbe für eine hängende Last: Zeitgrenze je Funktion, nicht je Kandidat. (4) Stufe-2-Last (R6-3): in einer eigenen Eichphase so bemessen, dass die Spannweite über acht Messungen unter 0,25 liegt, bei mindestens 10 ms je Stichprobe, dann versiegelt; die Rauschmessung im Vorspann bleibt getrennt und darf sperren — keine reine Dauerregel, denn zahlen läuft mit 19 ms ruhig, eingang mit 35 ms nicht. (5) Tor-4-Skript (R6-2): jede Zeile berechnet, die drei nicht aus der Datenbank berechenbaren aus ihren Belegdateien; der Zweig für verhaltensändernde Altlasten muss erreichbar sein. (6) Register vollständig, einschließlich Verhandlung. (7) Ausnahmen nach Typ und Inhalt vergleichen. (8) Kappe am echten T4-Werk messen; TypeScript-Proben vor T5. Regel für den Start von T4, vorab gesetzt: T4 beginnt, sobald das Review dieser Runde keinen stillen Durchlass mehr findet — jede bekannte Lücke muss eine gezählte Enthaltung sein; Lücken, die sich nur enthalten, behebt T4 im Lauf. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, laeufe/biotop-vor-t4-06/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

