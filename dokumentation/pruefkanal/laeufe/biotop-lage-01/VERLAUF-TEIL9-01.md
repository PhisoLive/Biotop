# BIOTOP-LAGE-01 · Fassung 2 · `VERLAUF-TEIL9-01.md` (FK11) · Teil 9 von 10

- **Einträge:** V386–V410 (24.09. 20:07 bis 25.09. 01:16).
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST. Alle Zeiten CEST.
- **Übersicht, Menge und Regeln:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL1-01.md

---
### V386 · 24.09. 20:07:38 CEST · Hermes-Zwischentext · Nachricht id 16690 · Sitzung `20260924_150913_a9326d` · 163 B

```text
Der Verdrahtungstest läuft noch (in Runde 4 dauerte er rund 17 Minuten, jetzt kommen Nachspiel und Tor 4 dazu). Ich bereite derweil die Füllung des Berichts vor.
```

### V387 · 24.09. 20:11:48 CEST · Hermes-Zwischentext · Nachricht id 16695 · Sitzung `20260924_150913_a9326d` · 94 B

```text
Der Verdrahtungstest läuft seit 24 Minuten und ist aktiv (Kammer arbeitet). Ich warte weiter.
```

### V388 · 24.09. 20:19:00 CEST · Hermes-Zwischentext · Nachricht id 16699 · Sitzung `20260924_150913_a9326d` · 116 B

```text
Verdrahtungstest grün (6 von 6, 28:39 min, mit Register, Tor-4-Skript und Nachspiel-Durchlauf). Teillauf 3b läuft.
```

### V389 · 24.09. 20:25:19 CEST · Hermes-Zwischentext · Nachricht id 16702 · Sitzung `20260924_150913_a9326d` · 137 B

```text
Commit `0c2f058` steht (Teillauf 3: 6 + 132 grün, Vorprobe K2904 überlebt). Jetzt das Berichtgerüst und dann der eine Reviewdurchgang.
```

### V390 · 24.09. 20:31:20 CEST · Hermes-Zwischentext · Nachricht id 16710 · Sitzung `20260924_150913_a9326d` · 82 B

```text
Jetzt der eine Reviewdurchgang (Subagent, wartet mit Kammerläufen auf die Kette).
```

### V391 · 24.09. 20:31:43 CEST · Hermes · Nachricht id 16729 · Sitzung `20260924_150913_a9326d` · 2367 B

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

### V392 · 24.09. 20:32:17 CEST · Hermes · Nachricht id 16735 · Sitzung `20260924_150913_a9326d` · 264 B

```text
Nichts Neues: Die beiden Meldungen gehören zu Teillauf 1 und 2, die schon ausgewertet und behoben sind. Die Kette an `0c2f058` steckt noch in der vollen Regression, der Reviewdurchgang läuft. Sobald beide fertig sind, melde ich mich mit Bericht und Abholadresse.
```

### V393 · 24.09. 21:00:41 CEST · Philipp · Nachricht id 16769 · Sitzung `20260924_150913_a9326d` · 801 B

```text
Kein Eingriff in den laufenden Job, nur zwei Punkte für den Bericht: (1) Die Abweichung „bei unvollständiger Erfassung enthält sich der ganze Vergleich" widerspricht Entscheidung 3 und schafft denselben Totalausfall wie Review-Nr. 4 — ein einziges schwer erfassbares Objekt stellt jeden Kandidaten zurück; als rote Spezifikation vor T4: Enthalten muss sich nur die betroffene Beobachtung. (2) Für eingang an Stufe 2 die Stichprobendauer bei 60 und bei 240 Wiederholungen — mein Auftrag „bis eingang nicht mehr sperrt" war ein Fehler, er richtet die Last nach dem Ergebnis; nur die Dauer zeigt, ob 240 nach Maß gewählt ist. Und auf die Liste vor T4: Das Tor-4-Skript berechnet jede Zeile, die aus der Datenbank berechenbar ist — die meisten Berichtsfehler in T3 waren Torzeilen von Han
```

### V394 · 24.09. 21:06:55 CEST · Hermes-Zwischentext · Nachricht id 16784 · Sitzung `20260924_150913_a9326d` · 141 B

```text
Beide Spezifikationen sind rot an `0c2f058`, beide Gegenproben grün (2 von 2). Jetzt trage ich die drei Punkte in Bericht und Übergabe ein.
```

### V395 · 24.09. 21:08:23 CEST · Hermes · Nachricht id 16793 · Sitzung `20260924_150913_a9326d` · 2659 B

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

### V396 · 24.09. 21:50:08 CEST · Hermes-Zwischentext · Nachricht id 16863 · Sitzung `20260924_150913_a9326d` · 184 B

```text
The fourth "API" hit is a false match: the `SondeAusgefallen` message quotes `AttributeError` from the load. I classify by exception type at the start of the message, not by substring.
```

### V397 · 24.09. 21:51:18 CEST · Hermes · Nachricht id 16871 · Sitzung `20260924_150913_a9326d` · 3071 B

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

### V398 · 24.09. 22:04:07 CEST · Hermes · Nachricht id 16889 · Sitzung `20260924_203120_e6c401` · 3701 B

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

### V399 · 24.09. 22:24:36 CEST · Hermes · Nachricht id 16900 · Sitzung `20260924_203120_e6c401` · 2683 B

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

### V400 · 24.09. 23:15:27 CEST · Philipp · Nachricht id 16901 · Sitzung `20260924_203120_e6c401` · 2448 B

```text
Zuerst Runde 5 abschließen: Es gilt das zweite Review (/tmp/review-vor-t4-05/REVIEW.md) — seine Messungen sind nachweislich eigene; beim ersten ist nicht auszuschließen, dass es das überschriebene Skript ausgeführt hat. Das erste bleibt im Ordner als verworfen; was nur es fand, kommt als unbestätigt auf die Liste. Erklär im Bericht, wie zwei Reviews entstehen konnten; künftig bekommt jedes Review einen eigenen Ordner, und du prüfst vor dem Start, dass keines läuft. Dann §11 und §12 füllen, veröffentlichen, Endmeldung. Dann Runde 6 — Entscheidungen Chat-Claude: (1) R6-4 nur zusammen mit einer typtreuen Verfälschung: verfälscht wird mit einem Wert desselben Typs und anderen Inhalts, nie mit einem Objekt, das beim Weiterrechnen wirft; ein Test hält nur fest, wenn seine Zusicherung am geänderten Wert fällt (Review-Nr. 1, Proben x5 und x5b). (2) Undurchsichtige Objekte: Zustand aus C-Typen wird über eine bekannte Darstellung erfasst (etwa getvalue, str, pickle), sonst ist die Beobachtung eine gezählte Enthaltung — nie „0 Abweichungen" (Nr. 2, p24b, p25). (3) R6-1 zusammen mit der Lücke aus Nr. 3: Enthält sich eine geänderte Funktion, wird der Kandidat zurückgestellt; enthalten sich nur unveränderte, wird am Rest geurteilt — meine Entscheidung 3 ließ das offen. Dasselbe für eine hängende Last: Zeitgrenze je Funktion, nicht je Kandidat. (4) Stufe-2-Last (R6-3): in einer eigenen Eichphase so bemessen, dass die Spannweite über acht Messungen unter 0,25 liegt, bei mindestens 10 ms je Stichprobe, dann versiegelt; die Rauschmessung im Vorspann bleibt getrennt und darf sperren — keine reine Dauerregel, denn zahlen läuft mit 19 ms ruhig, eingang mit 35 ms nicht. (5) Tor-4-Skript (R6-2): jede Zeile berechnet, die drei nicht aus der Datenbank berechenbaren aus ihren Belegdateien; der Zweig für verhaltensändernde Altlasten muss erreichbar sein. (6) Register vollständig, einschließlich Verhandlung. (7) Ausnahmen nach Typ und Inhalt vergleichen. (8) Kappe am echten T4-Werk messen; TypeScript-Proben vor T5. Regel für den Start von T4, vorab gesetzt: T4 beginnt, sobald das Review dieser Runde keinen stillen Durchlass mehr findet — jede bekannte Lücke muss eine gezählte Enthaltung sein; Lücken, die sich nur enthalten, behebt T4 im Lauf. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, laeufe/biotop-vor-t4-06/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

### V401 · 25.09. 00:24:43 CEST · Hermes · Nachricht id 17210 · Sitzung `20260924_203120_e6c401` · 2536 B

```text
Runde 5 ist abgeschlossen und veröffentlicht; die Endmeldung ging um 23:54 raus. Nicht abgenommen, aber jetzt vollständig: 139 von 139 Dateien über HTTPS bytegleich, Ordnerprüfsumme `0c82b7046709378be6710048ec07b3cff8097e850e5bc59ceb19a0fb48efdf6b`. Die Abholadresse steht in der Endmeldung.

- **Review:** `REVIEW.md` ist jetzt der zweite Durchgang. Der erste liegt als `REVIEW-verworfen-erster-durchgang.md` im Ordner. Was nur er fand, steht als U-1 bis U-4 „unbestätigt“ auf der Liste.
- **Wie zwei Reviews entstanden** (`ZWEI-REVIEWS.md`): Der Reviewer startete seine Kammerprobe als Hintergrundprozess mit Abschlussmeldung. Die Meldung band den Chat um 21:51 an seine Sitzung. Die Hauptsitzung endete, weil die Verdichtung am widerrufenen Token scheiterte. Danach arbeiteten zwei Instanzen mit demselben Verlauf im selben Ordner.
- **Korrektur zur Begründung:** Laut Delegationsprotokoll hat das erste Review das überschriebene Skript nicht mehr ausgeführt, und die Kammermessungen stammen von vor der Teilung. Die Wahl des zweiten ändert das nicht.
- **Ab Runde 6:** eigener Ordner je Review, vor dem Start prüfen, dass keines läuft, keine Hintergrundprozesse in Subagenten.
- **Bericht:** §11 (Umgang je Befund, R6-6 bis R6-15) und §12 (keine Sperren) sind gefüllt, der gemischte Nenner in §6 ist berichtigt.

**Runde 6 läuft, noch nichts gebaut oder gemessen.** Drei Teile bauen parallel in getrennten Dateien, der Wiedereinstieg steht in `/root/biotop-vor-t4-06/UEBERGABE.md`:
- **S1** (Entscheidungen 1, 2, 3, 7): typtreue Verfälschung zusammen mit R6-4, Erfassung undurchsichtiger C-Objekte, Enthaltung je Funktion mit Rückstellung bei geänderter Funktion, Zeitgrenze je Funktion, Ausnahmen nach Typ und Inhalt. Zuerst die roten Spezifikationen gegen `0c2f058`.
- **S2** (Entscheidung 5): Das Tor-4-Skript berechnet alle 14 Zeilen, und der Zweig für verhaltensändernde Altlasten wird erreichbar.
- **S3** (Entscheidung 4): eigene, versiegelte Eichphase für die Stufe-2-Last; ohne Siegel verweigert der Vorspann.

Danach baue ich das vollständige Register mit einer echten Verhandlung im Verdrahtungslauf (Entscheidung 6). Dann folgen Commit, Regression, Nachspiele, ein Review und die Veröffentlichung unter `laeufe/biotop-vor-t4-06/`.

Offen für dich: Das Token für die Verdichtung ist widerrufen (401). Ohne Verdichtung endet jede lange Sitzung an der Kontextgrenze; meine liegt bei etwa 54 %. Empfehlung: neu anmelden (`hermes model`) oder einen Ersatzanbieter für die Verdichtung eintragen.
```

### V402 · 25.09. 00:27:35 CEST · Philipp · Nachricht id 17217 · Sitzung `20260924_203120_e6c401` · 800 B

```text
Runde 5 sauber abgeschlossen, und die Aufklärung der zwei Reviews ist gründlich — mein Grund für die Wahl des zweiten war falsch, die Wahl bleibt. Ein Punkt für Runde 6: Ordne U-1 bis U-4 nach der Startregel ein — ist einer davon ein stiller Durchlass, also eine Lücke, die falsches Verhalten ohne Enthaltung durchlässt, dann gehört er mit Gegenprobe in diese Runde; die übrigen bleiben auf der Liste. Die drei Teile bauen weiter wie geplant.
Wenn du dich für den Ersatzanbieter entscheidest, häng diesen Satz an: Philipp legt fest: Die Verdichtung der Sitzungen läuft künftig über OpenRouter mit dem vorhandenen Schlüssel statt über die widerrufene Anmeldung — vorher config.yaml datiert sichern, danach mit einer echten Verdichtung belegen und die Kosten je Verdichtung nennen.
```

### V403 · 25.09. 00:43:57 CEST · Hermes · Nachricht id 17312 · Sitzung `20260924_203120_e6c401` · 2760 B

````text
Die Umstellung der Verdichtung auf OpenRouter ist gleich beim ersten Schritt gesperrt worden. `config.yaml` ist unverändert, und in diesem Ablauf habe ich nichts weiter getan, bis du antwortest.

**Sperre** (Beleg `sperre/SPERRE-01-config-sichern.txt`). Befehl, wörtlich:
```
cp -p /root/.hermes/config.yaml "/root/.hermes/config.yaml.$(date +%Y%m%d-%H%M%S).vor-openrouter-verdichtung" && ls -la /root/.hermes/config.yaml* && sha256sum /root/.hermes/config.yaml /root/.hermes/config.yaml.*.vor-openrouter-verdichtung
```
Meldung, wörtlich:
> BLOCKED: Command timed out without user response. The user has NOT consented to this action. Do NOT retry this command, do NOT rephrase it, and do NOT attempt the same outcome via a different command. Stop the current workflow and wait for the user to respond before taking any further destructive or irreversible action. Silence is not consent.

- **Einordnung:** Freigabeabfrage, ohne Antwort abgelaufen. Der Befehl lief nicht, es gibt keine Sicherung. Die Abfrage des OpenRouter-Kontos habe ich nicht gestartet.
- **Eigener Fehler:** Ich habe einen mehrteiligen Einzeiler mit Datumsersetzung geschrieben statt getrennter Schritte.

**Entscheidung 1 (Freigabe):**
- (a) Du gibst die Sicherung frei (empfohlen). Ich gehe dann in einzelnen Schritten vor:
  1. Sicherung mit festem Namen `config.yaml.20260925-vor-openrouter-verdichtung`.
  2. `hermes config set` für Anbieter und Modell der Verdichtung.
  3. Kontostand vorher und nachher, dazu eine echte Verdichtung dieser Sitzung, belegt im Protokoll.
  4. Kosten je Verdichtung.
- (b) Du legst die Sicherung selbst an, und ich beginne bei Schritt 2.

**U-1 bis U-4** (`EINORDNUNG-U1-U4.md`): Keiner der vier ist ein stiller Durchlass, alle bleiben auf der Liste. Die Einordnung beruht auf gelesenem Code von `0c2f058`; gemessen ist nichts.
- **U-1:** Das hängende Kind führt heute nach 240 s zu einem Messgerätausfall; der Kandidat wird zurückgestellt, also laut. Die Frist für die Eingrenzung, die die Elternseite durchsetzt, gehört zu Entscheidung 3. Ich habe S1 nachgesteuert, sie mitzubauen.
- **U-2:** Macht die Prüfung zu streng. Das ergibt Fehlalarme, nie eine Annahme.
- **U-3:** Führt zu einer Enthaltung zu viel, nicht zu einem Durchlass. Gehört zu TypeScript, also vor T5.
- **U-4:** Betrifft nur die fehlende Stufenangabe an gespeicherten Maßen, kein Kandidat kommt dadurch durch. Für die Torzeile „Kein Rückschritt“ habe ich S2 nachgesteuert: Werte ohne Stufe 2 gelten dort als „nicht belegt“.

**Runde 6:** S1 (Sonde und Vergleich), S2 (Tor-4-Skript) und S3 (Stufe-2-Eichphase) bauen weiter; von keinem liegt bisher ein Ergebnis vor. S1 hat zusätzlich eine Unit-Gegenprobe für den TypeScript-Weg von Entscheidung 3 bekommen.
````

### V404 · 25.09. 01:06:55 CEST · Philipp · Nachricht id 17359 · Sitzung `20260924_203120_e6c401` · 151 B

```text
(a) — ich gebe die Sicherung frei. Geh in einzelnen Schritten vor wie beschrieben; ich bestätige die Freigabeabfragen sofort, sobald sie erscheinen.
```

### V405 · 25.09. 01:12:03 CEST · Hermes · Nachricht id 17397 · Sitzung `20260924_203120_e6c401` · 11472 B

*Nicht abgedruckt:* Verdichtungszusammenfassung, ein Systemtext mit Kontextmarken und keine Nachricht an Philipp (R208). Der Wortlaut steht in der Sitzungsdatenbank, die gesichert ist (SICHERUNG).

### V406 · 25.09. 01:12:03 CEST · Hermes-Zwischentext · Nachricht id 17445 · Sitzung `20260924_203120_e6c401` · 3701 B

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

### V407 · 25.09. 01:12:03 CEST · Hermes · Nachricht id 17455 · Sitzung `20260924_203120_e6c401` · 2683 B

*Wiederholung von V399* (gleicher Absender, gleicher Wortlaut).

### V408 · 25.09. 01:12:03 CEST · Hermes · Nachricht id 17567 · Sitzung `20260924_203120_e6c401` · 2536 B

*Wiederholung von V401* (gleicher Absender, gleicher Wortlaut).

### V409 · 25.09. 01:12:03 CEST · Hermes · Nachricht id 17605 · Sitzung `20260924_203120_e6c401` · 2760 B

*Wiederholung von V403* (gleicher Absender, gleicher Wortlaut).

### V410 · 25.09. 01:16:52 CEST · Hermes · Nachricht id 17669 · Sitzung `20260924_203120_e6c401` · 2708 B

```text
Die Verdichtung läuft jetzt über OpenRouter mit dem vorhandenen Schlüssel. Eine echte Verdichtung dieser Sitzung belegt das, und sie kostete **0,0318 USD** (1 von 1 Verdichtung gemessen). Der Bericht steht in `/root/biotop-vor-t4-06/VERDICHTUNG-OPENROUTER.md`.

**Schritte, je ein Befehl:**
1. **Sicherung:** `config.yaml.20260925-vor-openrouter-verdichtung` angelegt. Die Freigabeabfrage erschien, und du hast sie bestätigt. Beide Dateien haben dieselbe sha256 (`fab40377…`).
2. **Umstellung:** `hermes config set` für `auxiliary.compression.provider openrouter` und `auxiliary.compression.model google/gemini-3.6-flash`. Dabei kam keine Abfrage.
3. **Vergleich mit der Sicherung:** Aus 155 Einstellungen wurden 157. Neu sind genau die zwei gesetzten, keine wurde geändert oder entfernt.
   - Nebenwirkung: `hermes config set` schreibt die Datei neu. Dabei fielen 38 reine Kommentarzeilen weg, auskommentierte Vorlagen ohne Wirkung. Sie stehen in der Sicherung.
4. **Echte Verdichtung:** Hermes hat diese Sitzung um 01:11:28–01:12:04 selbst verdichtet.
   - `agent.log`, wörtlich: „Auxiliary compression: using openrouter (google/gemini-3.6-flash)“. Die Verdichtung wurde übernommen, ohne Rückfall auf einen anderen Weg.
   - Laut Anbieter sank die Eingabe von 612.326 auf 78.607 Token.
5. **Kosten:** Der Zähler des Schlüssels stieg von 20,196649527 auf 20,228433027 USD, also 0,0317835 USD.
   - Vorher stand er 2 min still, danach 1 min.
   - Zwischen 01:11 und 01:15 nennen nur die 2 Protokollzeilen dieser Verdichtung OpenRouter.

**Eigene Entscheidung, Modell Gemini 3.6 Flash:** Hermes nutzt es selbst als Verdichtungsmodell auf seinem Nous-Weg. Es hat 1 Mio. Token Kontext und kostet 0,75 USD je Mio. Token Eingabe und 3,75 USD je Mio. Token Ausgabe. Vor dem Widerruf verdichtete Claude Opus 5. Ein Claude-Modell über OpenRouter wäre ein einzelner Befehl, kostet aber mehr je Token; gemessen habe ich das nicht.

**Güte der Zusammenfassung:** Die erste Zusammenfassung hat zwei Dinge falsch zugeordnet.
- Deine Freigabe erscheint als „Sicherung für Runde 6“ statt als Sicherung von `config.yaml`.
- U-1 bis U-4 stehen als offen da, obwohl die Einordnung erledigt war.

Verloren ging nichts, weil der jüngere Verlauf wörtlich blieb und der Stand in `UEBERGABE.md` steht. Ob das am Modell liegt, sagt ein einzelner Fall nicht.

**Rückweg:** Die Sicherung zurückkopieren; sie stellt den alten Stand bytegleich wieder her.

Die drei Teile S1 bis S3 der Runde 6 laufen noch; es liegt noch kein Ergebnis vor. In der Hermes-Anleitung habe ich zwei Hinweise ergänzt: Das Verdichtungsmodell wird unter `auxiliary` eingestellt, und `hermes config set` entfernt Kommentarzeilen.
```

