# BIOTOP-LAGE-01 · Fassung 2 · `VERLAUF-TEIL2-01.md` (FK11) · Teil 2 von 10

- **Einträge:** V039–V096 (21.09. 05:40 bis 21.09. 12:09).
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST. Alle Zeiten CEST.
- **Übersicht, Menge und Regeln:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL1-01.md

---
### V039 · 21.09. 05:40:05 CEST · Hermes-Zwischentext · Nachricht id 10259 · Sitzung `20260921_015554_e79a4a0f` · 175 B

```text
Stand bestätigt. Die 100 typgültigen Mutanten sind versiegelt (238 erzeugt, 128 typgeprüft, 28 typungültig verworfen, 129 Kammerläufe, 869 s). Jetzt der technische Start.
```

### V040 · 21.09. 05:42:59 CEST · Hermes-Zwischentext · Nachricht id 10293 · Sitzung `20260921_015554_e79a4a0f` · 326 B

*Wiederholung von V031* (gleicher Absender, gleicher Wortlaut).

### V041 · 21.09. 05:42:59 CEST · Hermes · Nachricht id 10402 · Sitzung `20260921_015554_e79a4a0f` · 83 B

*Wiederholung von V032* (gleicher Absender, gleicher Wortlaut).

### V042 · 21.09. 05:42:59 CEST · Hermes · Nachricht id 10404 · Sitzung `20260921_015554_e79a4a0f` · 83 B

*Wiederholung von V032* (gleicher Absender, gleicher Wortlaut).

### V043 · 21.09. 05:42:59 CEST · Hermes · Nachricht id 10406 · Sitzung `20260921_015554_e79a4a0f` · 83 B

*Wiederholung von V032* (gleicher Absender, gleicher Wortlaut).

### V044 · 21.09. 05:42:59 CEST · Hermes · Nachricht id 10408 · Sitzung `20260921_015554_e79a4a0f` · 83 B

*Wiederholung von V032* (gleicher Absender, gleicher Wortlaut).

### V045 · 21.09. 05:44:50 CEST · Hermes · Nachricht id 10435 · Sitzung `20260921_015554_e79a4a0f` · 262 B

```text
Lauf 26 läuft: Werk aufgenommen (werk_id 23, 2 467 TS-Zeilen, 182/182 Tests grün, Kernmaß −28), Verfassung-02 unverändert eingelegt, Kartierung im Hintergrund. Kasse bisher 0,00014 € von 10 €.

Ich melde mich, sobald Kartierung und Vorspann durch sind.
```

### V046 · 21.09. 05:46:47 CEST · Hermes · Nachricht id 10442 · Sitzung `20260921_015554_e79a4a0f` · 247 B

```text
Kartierung fertig: 5 Bereiche, 24 Dateien, 143 Funktionen, 143 Verträge, 76 Straßen — 31 Modellaufrufe für 0,0071 €. Vorspann (Rauschmessung + vier Eichproben mit Gegenproben) läuft jetzt im Hintergrund; das ist der längste Einzelschritt.
```

### V047 · 21.09. 05:47:06 CEST · Hermes-Zwischentext · Nachricht id 10444 · Sitzung `20260921_015554_e79a4a0f` · 194 B

```text
Vorspann rot — und zwar an der richtigen Stelle: der Kern verlangt eingelegte Verträge, die ich vor dem Vorspann nicht eingelegt habe. Die Regel "keine Nacheichung" sperrt Lauf 26 endgültig.
```

### V048 · 21.09. 05:48:04 CEST · Hermes-Zwischentext · Nachricht id 10456 · Sitzung `20260921_015554_e79a4a0f` · 210 B

```text
Mein Ablauffehler, nicht der des Kerns: Verträge müssen **vor** den Vorspann. Der Kern hat korrekt gesperrt und verweigert die Nacheichung — Lauf 26 bleibt tot, ich lege Lauf 27 in richtiger Reihenfolge an.
```

### V049 · 21.09. 05:48:49 CEST · Hermes · Nachricht id 10460 · Sitzung `20260921_015554_e79a4a0f` · 882 B

```text
**Lauf 26 ist gescheitert — mein Fehler, sauber gemeldet.**

Was passiert ist: Der Vorspann bricht mit „Verträge fehlen" ab. Ich hatte `biotop vertraege` nicht eingelegt, bevor ich den Vorspann startete. Der Kern verlangt die vier expliziten Bereichsverträge in der DB (`vertraege_explizit` für werk_id 23: 0 Einträge) und weigert sich, nachträglich zu eichen — genau die Satz-2-Regel „neues Messgerät verlangt neuen Lauf, keine Nacheichung".

Kosten Lauf 26: 0,0071 € (31 Modellaufrufe Kartierung) + 0,00014 € Ethikprüfung. Die zählen gegen das 10-€-Budget, auch wenn der Lauf tot ist — Verbrauch bleibt Verbrauch.

**Lauf 27 läuft jetzt in richtiger Reihenfolge:** anlegen → einlegen (182/182 Tests, baut) → Verfassung-02 → 4 Verträge eingelegt → Kartierung + Vorspann im Hintergrund. Verfassung-02 ist bytegleich dieselbe Datei, nicht angefasst.
```

### V050 · 21.09. 06:01:35 CEST · Hermes-Zwischentext · Nachricht id 10467 · Sitzung `20260921_015554_e79a4a0f` · 338 B

```text
Ursache gefunden, gemessen: Die Referenzlast von `bericht` (0,61–1,52 ms) und `planung` (1,36–2,51 ms) ist zu kurz — bei solchen Mikrolaufzeiten ist das Eigenrauschen 42–44 %. Der Kern nennt das selbst „unstete Referenzlast". Ich senke die Schwelle 1,5 **nicht**, ich behebe die Ursache: die Referenzlast muss lang genug messen.
```

### V051 · 21.09. 06:02:38 CEST · Hermes-Zwischentext · Nachricht id 10479 · Sitzung `20260921_015554_e79a4a0f` · 285 B

```text
Ursache ist die Referenzlast selbst, nicht die Maschine: `bericht` und `planung` messen 0,6–2,5 ms — in dieser Größenordnung ist Timer-Jitter größer als das Signal. Ich vergrößere die Last (Kern, nicht Werk) und messe das Rauschen isoliert nach, bevor ein neuer Lauf startet.
```

### V052 · 21.09. 06:03:07 CEST · Hermes · Nachricht id 10485 · Sitzung `20260921_015554_e79a4a0f` · 1119 B

```text
**Lauf 27 gescheitert — Ursache gemessen, Schwelle bleibt.**

Der Vorspann sperrt `bericht` und `planung`: Eigenrauschen 44 % bzw. 42 % über den mittleren 3 von 5 Werten, Toleranz 1,54 / 1,52 über der Meldeschwelle 1,5. Rohwerte: bericht 0,61–1,52 ms, planung 1,36–2,51 ms. Bei solchen Mikrolaufzeiten ist Timer-Jitter größer als das Signal — der Kern nennt das korrekt „unstete Referenzlast". Dadurch fielen Nebenwirkungsprobe und alle vier Gegenproben aus (nur 3 von 4 Positivproben bestanden, gefordert sind 4).

Was ich **nicht** tue: die 1,5 anheben. Was ich tue: die Ursache beheben — die Referenzlast (Kern, nicht Werk) wiederholt die Bereichslasten jetzt so oft, dass jede Messung in den Bereich einiger zehn Millisekunden kommt. `beobachten()` bleibt klein und unverändert, damit das Verhaltensraster dasselbe misst wie vorher.

Die Rauschvorprobe läuft — dieselbe Messung wie im Vorspann, aber ohne Lauf und ohne DB, damit ich kein drittes Mal einen Lauf verbrenne, bevor die Zahl stimmt.

Kosten bisher: 0,0073 € von 10 € (Läufe 26+27, beide gescheitert; Verbrauch bleibt Verbrauch).
```

### V053 · 21.09. 06:05:20 CEST · Hermes-Zwischentext · Nachricht id 10489 · Sitzung `20260921_015554_e79a4a0f` · 197 B

```text
Alle fünf Bereiche unter der unveränderten Schwelle 1,5: bericht 1,263 (vorher 1,539), planung 1,163 (vorher 1,524), eingang 1,231, tarife 1,191, zahlen 1,367. Null Sperren. Lauf 28 kann starten.
```

### V054 · 21.09. 06:07:12 CEST · Hermes · Nachricht id 10493 · Sitzung `20260921_015554_e79a4a0f` · 688 B

```text
**Rauschvorprobe bestanden, Schwelle 1,5 unverändert.**

Toleranzen nach der Referenzlast-Korrektur (5 Messungen, 5 Kammerläufe, 127 s):
- bericht 1,263 — vorher 1,539 (gesperrt)
- planung 1,163 — vorher 1,524 (gesperrt)
- eingang 1,231, tarife 1,191, zahlen 1,367 — alle vorher schon frei
- **0 von 5 Bereichen gesperrt**

Grund der Besserung ist gemessen, nicht behauptet: die Medianlaufzeiten stiegen von 0,6–2,5 ms auf 3,6–18,1 ms, dadurch fällt der Timer-Jitter relativ weg. Referenzlast-SHA256 `5f597b68…`.

Lauf 28 ist angelegt und vollständig vorbereitet (Werk 182/182, Verfassung-02, 4 Verträge, Kartierung 0 Modellaufrufe dank Gedächtnis); der Vorspann läuft.
```

### V055 · 21.09. 06:19:43 CEST · Hermes-Zwischentext · Nachricht id 10503 · Sitzung `20260921_015554_e79a4a0f` · 120 B

```text
Vorprobe grün, Lauf 28 rot — und das ist die wichtigere Information: die Messung selbst streut zwischen Durchläufen.
```

### V056 · 21.09. 06:20:28 CEST · Hermes-Zwischentext · Nachricht id 10507 · Sitzung `20260921_015554_e79a4a0f` · 179 B

```text
Rot bestätigt, und die Rohwerte zeigen den Grund direkt: `[0,98 / 0,28 / 0,12]` ms — der erste Aufruf ist achtmal langsamer als der dritte. Das ist JIT-Aufwärmung im Messwert.
```

### V057 · 21.09. 06:21:25 CEST · Hermes · Nachricht id 10513 · Sitzung `20260921_015554_e79a4a0f` · 1543 B

```text
**Lauf 28 gescheitert — und der Fehlschlag hat die eigentliche Ursache offengelegt.**

Die Vorprobe war grün (0 Sperren), Lauf 28 sperrte `bericht` (1,837) und `zahlen` (1,87) — also andere Bereiche als Lauf 27 (`bericht`, `planung`). Eine Messung, die bei jedem Durchlauf andere Bereiche sperrt, misst nicht das Werk, sondern sich selbst. Meine Vorprobe war damit kein Nachweis, sondern ein glücklicher Einzeldurchlauf; das nehme ich zurück.

Gemessene Ursache: Der Referenz-Runner nahm **3** Messwerte, den ersten davon ohne jede Aufwärmung. Rohwerte aus dem Beleg: `[0,98 / 0,28 / 0,12]` ms — der erste Aufruf ist 8× langsamer als der dritte, weil JIT-Übersetzung und Erstallokation im Messwert landen. Genau dieser eine Ausreißer treibt die getrimmte Spannweite über 1,5, und welcher Bereich es trifft, ist Zufall.

Behoben (Kern, `referenz-runner.mjs`): erst alle Bereiche 3× aufwärmen, dann 5 Messwerte je Bereich, Median aus fünf statt aus drei. Schwelle 1,5 unverändert, Rauschregeln unverändert.

Belegt durch Ausführung: Test `test_t3_referenzwarmup.py` zählt die tatsächlichen Referenzaufrufe im Container — vorher rot (3 statt 5 Messwerte, keine Aufwärmung), nach der Änderung grün, 1 passed in 24,83 s.

Drei aufeinanderfolgende Rauschvorproben laufen jetzt. Nur wenn **alle drei** null Sperren zeigen, lege ich Lauf 29 an — eine einzelne grüne Messung hat sich als nicht tragfähig erwiesen.

Kosten unverändert 0,0073 € von 10 € (Kartierungen 28 liefen ohne Modellaufrufe aus dem Gedächtnis).
```

### V058 · 21.09. 06:24:38 CEST · Philipp · Nachricht id 10514 · Sitzung `20260921_015554_e79a4a0f` · 984 B

```text
Bevor die drei Vorproben zählen, belege, dass Vorprobe und Lauf denselben Messweg nutzen — dieselbe Referenzlast (Prüfsumme), denselben Runner, dieselbe Aufrufkette. Drei Zahlen widersprechen sich: dein Ziel „einige zehn Millisekunden", die Vorprobe mit Medianen von 3,6–18,1 ms, und Lauf 28 mit Rohwerten von 0,12–0,98 ms; wenn die korrigierte Last nur in der Vorprobe ankam, ist das die Ursache, und drei grüne Vorproben auf einem anderen Weg beweisen nichts über Lauf 29 (Grundsatz 5). Erkläre außerdem, warum ein einzelner Ausreißer einen Median aus drei Werten bewegt haben soll — aus [0,98 / 0,28 / 0,12] wird 0,28, der erste Wert fällt heraus; war auch der mittlere Wert noch nicht aufgewärmt? Und weiterhin offen: Lauf 26 steht zweimal, als gesättigter Beleglauf von Vorbedingung 1 und als erster T3-Versuch — alle Läufe ab 24 mit ID, werk_id, Anlagezeit und Status aus der Datenbank. Budget, Schwelle und Rauschregeln unverändert, ein Reviewdurchgang.
```

### V059 · 21.09. 06:25:25 CEST · Hermes-Zwischentext · Nachricht id 10515 · Sitzung `20260921_015554_e79a4a0f` · 79 B

```text
Drei berechtigte Einwände. Ich messe sie nacheinander, statt zu argumentieren.
```

### V060 · 21.09. 06:25:56 CEST · Hermes-Zwischentext · Nachricht id 10519 · Sitzung `20260921_015554_e79a4a0f` · 36 B

```text
Drei Befunde, zwei davon gegen mich.
```

### V061 · 21.09. 06:26:04 CEST · Hermes-Zwischentext · Nachricht id 10523 · Sitzung `20260921_015554_e79a4a0f` · 71 B

```text
Jetzt ist die Sache belegt, und meine Erklärung von vorhin war falsch.
```

### V062 · 21.09. 06:26:33 CEST · Hermes · Nachricht id 10525 · Sitzung `20260921_015554_e79a4a0f` · 4554 B

```text
Die drei Vorproben laufen noch (zwei fertig, dritte in Arbeit). Ich lasse sie laufen, aber sie zählen erst, wenn der Messweg identisch belegt ist — dazu die Antworten:

## 1. Messweg: identisch in der Kette, aber Lauf 27 lief auf alter Last

**Belegt (`BELEG-MESSWEG.txt`):**
- Referenzlast: `_referenzlast()` des Laufs und die Vorprobendatei liefern **denselben** SHA256 `5f597b68…`. Identisch: ja.
- Aufrufkette: Vorprobe → `messgeraet.messen(werk, bereiche, 'src', ref)`. Lauf → `vorspann._ausfuehren` → `eichung.rauschmessung` → `eichung._messen_einmal` → **dieselbe** `messgeraet.messen(...)`. `RAUSCH_MESSUNGEN` = 5 auf beiden Wegen.
- Runner/Instrument in Lauf 27 **und** 28 bytegleich: Runner `1f4a806c…`, referenz.mjs `9fa01f51…`, messen.mjs `d37adce8…`.

**Aber:** Lauf 27 lief auf Referenzlast `469197a4…` (die alte, kurze), Lauf 28 auf `5f597b68…` (die korrigierte). Ihr Verdacht trifft zu — nur in die andere Richtung als vermutet: die korrigierte Last kam in Lauf 28 sehr wohl an.

## 2. Die drei Zahlen widersprechen sich nicht — ich hatte den falschen Beleg zitiert

Die echten Rohwerte aus den Läufen (`BELEG-ROHWERTE.txt`):

- **Lauf 27** (alte Last): bericht `[3,27 / 0,65 / 0,53]`, planung `[1,78 / 1,25 / 1,48]` ms
- **Lauf 28** (neue Last): bericht `[60,43 / 10,54 / 8,27]`, planung `[77,22 / 11,14 / 9,51]`, tarife `[16,65 / 14,74 / 47,59]` ms

Die Werte 0,12–0,98 ms, die ich als „Lauf 28" zitiert habe, stammen **nicht** aus Lauf 28 — sie kommen aus meinem eigenen Warmup-Test mit seiner Mini-Last. Das war ein Beleg-Verwechsler von mir; die Aussage „Lauf 28 mit Rohwerten von 0,12–0,98 ms" ziehe ich zurück.

## 3. Ihr Medianeinwand ist richtig, meine Erklärung war falsch

Sie haben recht: aus `[0,98 / 0,28 / 0,12]` wird 0,28, der erste Wert fällt heraus. Ein einzelner erster Ausreißer bewegt den Median aus drei Werten **nicht**. Meine Erklärung „der erste Aufruf treibt die Spannweite über 1,5" war falsch.

Was die echten Zahlen zeigen: In Lauf 28 ist der Ausreißer **nicht** immer der erste. Bei `tarife` lautet die Folge `[16,65 / 14,74 / 47,59]` — der Ausreißer ist der **dritte** Wert, der Median wird 16,65 statt 14,74. Das ist kein Aufwärmeffekt, sondern Störung während des Laufs (GC oder Fremdlast auf der Maschine). Der Median aus drei Werten schützt nur gegen **einen** Ausreißer an einer Randposition; trifft die Störung die Mitte oder kommen zwei, geht sie durch — und über fünf Durchläufe hinweg streut dann der Median selbst, was genau die beobachtete Toleranz 1,837/1,87 erzeugt.

Die Aufwärmung bleibt trotzdem richtig (0,98 → 0,12 ms ist belegt), aber sie ist **nicht** die Ursache der Sperren in Lauf 28. Der Wechsel von 3 auf 5 Messwerte adressiert die echte Ursache — ob er reicht, ist unbewiesen, solange ich nur Vorproben habe.

## 4. Läufe ab 24 — Lauf 26 steht zweimal, weil es zwei Datenbanken sind

Aus `/root/biotop-t3/t3.db` (T3-Auftrag):
- Lauf 24 | werk 21 lagerhaus-zeile8-24 | bereit | 2026-09-19 22:57:49 | Budget 1,50 €
- Lauf 25 | werk 22 lagerhaus-c-25 | bereit | 2026-09-20 01:13:30 | Budget 0,80 €
- **Lauf 26** | werk 23 versandwerk-t3-02 | kartiert | 2026-09-21 03:43:38 | Budget 10 € — Vorspann gescheitert (Verträge fehlten)
- **Lauf 27** | werk 23 | kartiert | 04:05:27 | 10 € — Vorspann gescheitert (Rauschen)
- **Lauf 28** | werk 23 | kartiert | 2026-09-21 04:05:27 | 10 € — Vorspann gescheitert (Rauschen)

Aus `/root/phase-4-vorbedingung-1/privat/biotop.db` (Vorbedingung 1, eigene DB):
- **Lauf 26** | werk 23 lagerhaus-vorbedingung1-26 | **gesaettigt** | 2026-09-20 19:31:54 → 20:16:10 | Budget 3 €

Die Doppelung ist echt und harmlos: zwei getrennte Datenbanken vergeben ID 26 unabhängig, und beide haben zufällig auch werk_id 23 — aber für **verschiedene** Werke (`versandwerk-t3-02` gegen `lagerhaus-vorbedingung1-26`). Die IDs sind nur innerhalb ihrer DB eindeutig. Künftig nenne ich bei jeder Lauf-ID die Datenbank dazu.

## Wie ich weitermache

Die drei Vorproben allein sind nach Ihrem Grundsatz 5 kein Beleg für Lauf 29 — sie laufen zwar über dieselbe `messgeraet.messen`-Kette, aber der Vorspann macht mehr als nur messen. Ich ändere den Nachweis: statt drei Vorproben messe ich die Rauschmessung **über den Kernpfad selbst** (`eichung.rauschmessung` in einer Wegwerf-DB), dreimal hintereinander. Das ist derselbe Code, den Lauf 29 ausführt, nur ohne Lauf zu verbrauchen.

Budget unverändert 0,0073 € von 10 €, Schwelle 1,5 und Rauschregeln unangetastet.
```

### V063 · 21.09. 06:27:57 CEST · Hermes-Zwischentext · Nachricht id 10527 · Sitzung `20260921_015554_e79a4a0f` · 168 B

```text
Drei Vorproben grün (0 Sperren, max. Toleranz 1,422). Aber wie gesagt: das ist noch nicht der Kernpfad. Jetzt der Nachweis über denselben Code, den Lauf 29 ausführt.
```

### V064 · 21.09. 06:28:30 CEST · Hermes · Nachricht id 10534 · Sitzung `20260921_015554_e79a4a0f` · 1211 B

```text
Die drei Vorproben sind grün — 0 Sperren, Toleranzen 1,15–1,422, alle unter der unveränderten Schwelle 1,5:

| Durchlauf | bericht | eingang | planung | tarife | zahlen |
|---|---|---|---|---|---|
| 1 | 1,262 | 1,165 | 1,150 | 1,259 | 1,168 |
| 2 | 1,291 | 1,219 | 1,206 | 1,150 | 1,150 |
| 3 | 1,179 | 1,422 | 1,180 | 1,150 | 1,202 |

Sie zählen aber nach Ihrem Einwand nicht als Freigabe: sie rufen `messgeraet.messen` direkt, der Vorspann ruft `eichung.rauschmessung` — die zusätzlich Aussetzer-Nachmessung, Sperrlogik, Vorgeschichte und Protokollierung enthält. Deshalb läuft jetzt derselbe Nachweis über **genau die Funktion**, die Lauf 29 ausführen wird, dreimal, in einer Wegwerf-Datenbank. Nur wenn der dreimal null Sperren liefert, lege ich Lauf 29 an.

Ergänzend zum Messweg, was der Beleg zeigt: Runner und Instrument waren in Lauf 27 und 28 bytegleich (`1f4a806c…`), die Referenzlast unterschied sich (27: `469197a4…` alt, 28: `5f597b68…` korrigiert). Die korrigierte Last kam also im Lauf an — die Sperren in Lauf 28 haben eine andere Ursache als die Lastgröße, nämlich Störungen mitten in der Messreihe (`tarife [16,65 / 14,74 / 47,59]`, Ausreißer an dritter Position).
```

### V065 · 21.09. 06:35:07 CEST · Hermes-Zwischentext · Nachricht id 10536 · Sitzung `20260921_015554_e79a4a0f` · 166 B

```text
Kernpfad-Nachweis grün: 3 von 3 Durchläufen über `eichung.rauschmessung`, 0 Sperren, höchste Toleranz 1,336 bei unveränderter Schwelle 1,5. Lauf 29 kann starten.
```

### V066 · 21.09. 06:37:01 CEST · Hermes · Nachricht id 10540 · Sitzung `20260921_015554_e79a4a0f` · 805 B

```text
**Kernpfad-Nachweis bestanden** — diesmal auf dem Weg, den Lauf 29 tatsächlich geht (`eichung.rauschmessung`, nicht `messgeraet.messen` direkt):

| Durchlauf | bericht | eingang | planung | tarife | zahlen | gesperrt |
|---|---|---|---|---|---|---|
| 1 | 1,150 | 1,202 | 1,191 | 1,150 | 1,184 | keine |
| 2 | 1,263 | 1,273 | 1,336 | 1,159 | 1,200 | keine |
| 3 | 1,223 | 1,168 | 1,249 | 1,232 | 1,174 | keine |

3 von 3 Durchläufen frei, höchste Toleranz 1,336 von 1,5 — Reserve 0,164. Je 131/129/128 s, 5 Messungen pro Durchlauf. Referenzlast `5f597b68…`, Runner `b22ea89e…` (mit Aufwärmung), beide identisch mit dem, was der Lauf lädt.

Lauf 29 (DB `/root/biotop-t3/t3.db`) ist vorbereitet: Werk 182/182, Verfassung-02 unverändert, 4 Verträge, Kartierung 0 Modellaufrufe. Vorspann läuft.
```

### V067 · 21.09. 06:48:18 CEST · Hermes-Zwischentext · Nachricht id 10542 · Sitzung `20260921_015554_e79a4a0f` · 127 B

```text
Vorspann bestanden: 4 positive Proben, 4 negative Gegenproben, Nachweis `fb182da6…`, 85 Kammerläufe, 0 Modellaufrufe, 0 €.
```

### V068 · 21.09. 06:48:45 CEST · Hermes · Nachricht id 10549 · Sitzung `20260921_015554_e79a4a0f` · 979 B

```text
**Vorspann Lauf 29 bestanden** (DB `/root/biotop-t3/t3.db`).

- Qualität: **4 von 4 positiven Proben** getroffen, **4 von 4 Gegenproben** prüfbar negativ — genau das, was Lauf 27 und 28 verfehlt haben
- Rauschmessung: 0 Sperren, `lauf_startet: true`
- Nachweis-SHA256 `fb182da6fbe442b5e4266692b30fc040035eaa987cdc578a30ca1c35081ca081`
- Aufwand: 85 Kammerläufe, **0 Modellaufrufe, 0,00 €**, 660 s — davon Rauschmessung 5 Läufe/129 s, Proben 48 Läufe, Gegenproben 31 Läufe

Vor Generation 0 habe ich den Mutantenbezug geprüft: alle **12 von 12** betroffenen Quelldateien sind zwischen `/root/versandwerk-t3-02` und dem eingelegten Werk bytegleich, alle 100 Mutanten typgeprüft, Liste `b35a6ea8…` (65 Zahlengrenze, 22 Vergleich, 11 Arithmetik, 2 boolesch).

Generation 0 läuft jetzt mit diesen 100 Mutanten.

Verbrauch: **0,0075 € von 10 €** — Lauf 26: 0,0071 €, Läufe 27/28/29 je 0,0001 € (nur Ethikprüfung; Kartierungen kamen aus dem Artgedächtnis).
```

### V069 · 21.09. 06:52:59 CEST · Philipp · Nachricht id 10550 · Sitzung `20260921_015554_e79a4a0f` · 977 B

```text
Vorspann bestanden — der erste Beleg, dass das Messgerät außerhalb von Python trägt. Ab jetzt keine Zwischenmeldungen: Lauf 29 nach Tor 4 bis zum Abschluss durcharbeiten und nur mit der Endmeldung kommen; Ausnahme Budgetstopp, Kernfehler oder Sitzungsende, dann Zwischenbericht in den Prüfkanal. In den Bericht, zusätzlich zu den Torzeilen: Fangquote je Mutantenart samt Verteilung der 28 typungültigen — 65 von 100 an Zahlengrenzen deutet darauf, dass der Typprüfer Operator-Mutanten aussiebt, dann misst Generation 0 in TypeScript schief; die 85 Vorspann-Kammerläufe aufgeschlüsselt, die genannten Teile ergeben 84; und für Lauf 28 die Ursache je gesperrtem Bereich — bericht zeigt einen noch nicht aufgewärmten Mittelwert, tarife war nicht gesperrt, für zahlen fehlen Rohwerte. Vor T4 zu klären: Gesamtkosten über alle drei Datenbankzweige ohne Doppelzählung des Stamms, und ob die T3-Kernänderungen in der Codelinie liegen, auf der T4 und T5 aufbauen.
```

### V070 · 21.09. 06:55:33 CEST · Hermes-Zwischentext · Nachricht id 10559 · Sitzung `20260921_015554_e79a4a0f` · 156 B

```text
Wichtiger Befund: der Typprüfer siebt Vergleichs-Mutanten zu 54 % aus. Philipps Verdacht trifft zu. Ich sammle die restlichen Belege, während gen0 läuft.
```

### V071 · 21.09. 06:57:45 CEST · Hermes · Nachricht id 10579 · Sitzung `20260921_015554_e79a4a0f` · 2087 B

```text
Generation 0 läuft seit 9 Minuten mit 100 Mutanten. Ich arbeite ab jetzt ohne Zwischenmeldungen durch. Der Zwischenbericht mit den vier angeforderten Belegen liegt bereit, falls Budget, Kernfehler oder Sitzungsende dazwischenkommen.

Die Kurzfassung der vier Punkte, weil sie Ihre Entscheidungen berühren:

**85 Kammerläufe:** Ihre 84 waren richtig gezählt — mir fehlte die Zeile `fundpruefung` mit 0 Läufen, die ich beim Abschreiben übersprungen hatte. Einzelposten summieren sich auf 85, Nachweis meldet 85, Differenz 0.

**Typsieb — Ihr Verdacht bestätigt sich:** Vergleichs-Mutanten werden zu **54 %** (26 von 48) vom Typprüfer verworfen, Zahlengrenzen zu **0 %** (0 von 65). Die Auswahl verschiebt sich dadurch: Zahlengrenzen 54,2 % in der erzeugten Population gegen 65 % in den gewählten 100, Vergleiche 32,4 % gegen 22 %. Generation 0 misst in TypeScript also tatsächlich an einer verzerrten Population. Die Fangquote kommt je Art getrennt in die Endmeldung, eine Gesamtquote nur mit dieser Einschränkung.

**Lauf 28:** Gesperrt waren bericht und zahlen — tarife nicht; meine frühere Nennung nehme ich zurück. Rohwerte der Rauschmessungen existieren nicht: gespeichert werden nur die fünf Mediane, die Einzelwerte je Messung werden verworfen. Für bericht *und* zahlen kann ich die Aufwärmungsthese daher nicht belegen. Was die Basismessung zeigt: bei bericht steht der Ausreißer an erster Stelle (7,3×), bei zahlen ist der erste Wert nur 1,4× über dem kleinsten — dort trägt Aufwärmung die Erklärung nicht.

**Kosten und Codelinie:** Ohne Doppelzählung des Stamms **9,0936 €** gesamt (naive Addition wäre 26,3722 € gewesen; 4070 Stammbuchungen à 8,6393 € liegen in allen drei Zweigen identisch). T3-Anteil 0,0075 €. Lauf 29 läuft auf `/root/biotop`, Git `main`, HEAD `b42dc941` — dieselbe Linie wie Vorbedingung 1. **Die T3-Änderungen sind dort nicht eingecheckt: 20 geändert, 11 neu.** Wenn T4 und T5 darauf aufbauen sollen, muss das eingecheckt werden; ich habe es nicht getan, das ist Ihre Entscheidung über die gemeinsame Linie.
```

### V072 · 21.09. 07:24:03 CEST · Hermes-Zwischentext · Nachricht id 10583 · Sitzung `20260921_015554_e79a4a0f` · 258 B

```text
Generation 0 abgebrochen — und zwar durch **einen echten Anbieterausfall**: qwen HTTP 429, klassifiziert als `ausfallart: infrastruktur`, `beitraege: 0`. Das ist genau der Fall, den Auflage 3 verlangt. Ich prüfe, ob der Abbruch korrekt ist oder zu streng.
```

### V073 · 21.09. 07:24:44 CEST · Hermes-Zwischentext · Nachricht id 10589 · Sitzung `20260921_015554_e79a4a0f` · 242 B

```text
Der Abbruch ist inhaltlich korrekt — aber er hinterlässt einen Deadlock: `verbrauch_bekannt: False` sperrt **jeden** weiteren Aufruf des gesamten Auftrags, dauerhaft, ohne Klärungsweg. Ich kläre den Verbrauch, statt die Regel zu lockern.
```

### V074 · 21.09. 07:25:26 CEST · Hermes-Zwischentext · Nachricht id 10599 · Sitzung `20260921_015554_e79a4a0f` · 173 B

```text
Der Anbieter beziffert den Tagesverbrauch: **0,0115498 $**. Jetzt der Abgleich gegen die Kasse — nur wenn beide übereinstimmen, ist der Ausfall als verbrauchsfrei belegt.
```

### V075 · 21.09. 07:26:03 CEST · Hermes-Zwischentext · Nachricht id 10603 · Sitzung `20260921_015554_e79a4a0f` · 171 B

```text
Die Differenz ist 0,000219 USD — nicht null. Meine Schwelle von 0,0005 war willkürlich; so eine Grenze setze ich nicht selbst. Ich hole die exakte Abrechnung je Aufruf.
```

### V076 · 21.09. 07:26:48 CEST · Hermes-Zwischentext · Nachricht id 10607 · Sitzung `20260921_015554_e79a4a0f` · 194 B

```text
The activity endpoint needs a management key. Instead of guessing, I check the price table against the anbieter's published prices — that decides whether 0,000219 der Ausfall ist oder Rundung.
```

### V077 · 21.09. 07:27:46 CEST · Hermes-Zwischentext · Nachricht id 10615 · Sitzung `20260921_015554_e79a4a0f` · 190 B

```text
Der Rest entspricht 33 % eines Prompts — das ist ein Indiz, kein Beweis. Ich senke die Regel nicht, sondern gebe ihr einen Klärungsweg, der den Zweifel **zu Lasten des Budgets** auflöst.
```

### V078 · 21.09. 07:27:59 CEST · Hermes-Zwischentext · Nachricht id 10619 · Sitzung `20260921_015554_e79a4a0f` · 88 B

```text
Rot wie erwartet — die Sperre selbst wirkt bereits (1 passed), der Klärungsweg fehlt.
```

### V079 · 21.09. 07:28:23 CEST · Hermes-Zwischentext · Nachricht id 10623 · Sitzung `20260921_015554_e79a4a0f` · 100 B

```text
Der Linter meldet einen echten Fehler: `art` kollidiert mit dem Parameter von `protokoll.schreiben`.
```

### V080 · 21.09. 07:28:46 CEST · Hermes-Zwischentext · Nachricht id 10630 · Sitzung `20260921_015554_e79a4a0f` · 157 B

```text
Die Buchung erfolgt, aber `vorpruefung` kennt die Klärung nicht — sie prüft nur `modell.ausfall`. Die Sperre muss die geklärten Fälle berücksichtigen.
```

### V081 · 21.09. 07:29:23 CEST · Hermes-Zwischentext · Nachricht id 10638 · Sitzung `20260921_015554_e79a4a0f` · 92 B

```text
49 Tests grün, keine Regression. Jetzt die Klärung des echten Ausfalls in der Auftrags-DB.
```

### V082 · 21.09. 07:29:34 CEST · Hermes-Zwischentext · Nachricht id 10642 · Sitzung `20260921_015554_e79a4a0f` · 141 B

```text
Wichtiger Nebenbefund: `AUFTRAG_LAUF_AB = 0`, `AUFTRAG_BUDGET_EUR = 0.0` — die harte 10-€-Auftragsgrenze ist gar nicht scharf geschaltet.
```

### V083 · 21.09. 07:29:42 CEST · Hermes-Zwischentext · Nachricht id 10644 · Sitzung `20260921_015554_e79a4a0f` · 186 B

```text
Die 10-€-Grenze war nie scharf — sie hängt an Umgebungsvariablen, die ich nie gesetzt hatte. Bisher unkritisch (0,0087 € verbraucht), aber vor dem Evolutionslauf muss sie greifen.
```

### V084 · 21.09. 07:30:01 CEST · Hermes-Zwischentext · Nachricht id 10648 · Sitzung `20260921_015554_e79a4a0f` · 126 B

```text
Die Grenze ist scharf: 0,013291 € von 10 €. Jetzt Generation 0 neu starten — mit scharfem Budget und geklärtem Ausfall.
```

### V085 · 21.09. 07:30:23 CEST · Hermes · Nachricht id 10652 · Sitzung `20260921_015554_e79a4a0f` · 2047 B

```text
Kernfehler-Ausnahme — deshalb diese Meldung. Zwei Befunde, beide sind Instrumentfehler, nicht Werkbefunde:

**1. Der Verbundausfall aus Auflage 3 ist eingetreten — echt, nicht gestellt.** qwen/qwen3.8-flash lieferte HTTP 429, klassifiziert als `ausfallart: infrastruktur`, `beitraege: 0`. Die Regel griff korrekt. Sie hinterließ aber einen Deadlock: `verbrauch_bekannt: False` sperrt jeden weiteren Aufruf des gesamten Auftrags, dauerhaft, ohne Klärungsweg.

Ich habe den Verbrauch beim Anbieter geklärt statt die Regel zu lockern: Tagesverbrauch 0,0115498 USD gegen nachgerechnete 0,01133035 USD der 36 gebuchten Aufrufe — Rest 0,00021945 USD, das sind 1463 qwen-Eingabetokens oder 33 % eines vollen Prompts desselben Zwecks. Ein abgewiesener 429-Aufruf überträgt ganz oder gar nicht, der Rest ist also nicht als Prompt erklärbar, sondern Abrechnungsabweichung (1,94 % über 36 Posten). **Bewiesen verbrauchsfrei ist das nicht** — deshalb buche ich den Höchstfall: die volle Reservierung 0,0028 € als tatsächlichen Verbrauch. Zweifel zu Lasten des Budgets.

Neu im Kern: `kasse.ausfall_klaeren()` — bucht den Höchstfall, klärt genau einen Ausfall, gibt andere nicht frei, wird ohne passenden Ausfall abgewiesen, und kann das Budget sprengen (dann bricht der Lauf ab, wie vorgesehen). 5 Tests, vorher 4 rot, jetzt grün; 49 Tests im Umfeld ohne Regression.

**2. Die 10-€-Auftragsgrenze war nie scharf.** `AUFTRAG_LAUF_AB=0`, `AUFTRAG_BUDGET_EUR=0.0` — sie hängt an Umgebungsvariablen, die ich nie gesetzt hatte. Geprüft wurde bisher nur das Einzellauf-Budget. Folgenlos gewesen (0,0133 € verbraucht), aber vor dem Evolutionslauf hätte es die harte Grenze unwirksam gemacht. Jetzt gesetzt: `BIOTOP_AUFTRAG_LAUF_AB=26`, `BIOTOP_AUFTRAG_BUDGET_EUR=10`, verifiziert — Auftragsverbrauch 0,013291 € von 10 €.

Nebenbefund aus dem abgebrochenen gen0: **83 von 100 Mutanten fängt der Testbestand bereits vorher.** Generation 0 läuft neu, mit scharfem Budget. Ab jetzt wieder ohne Zwischenmeldung bis zur Endmeldung.
```

### V086 · 21.09. 07:34:43 CEST · Hermes-Zwischentext · Nachricht id 10656 · Sitzung `20260921_015554_e79a4a0f` · 95 B

```text
301 passed, 2 skipped — Kern stabil. Ab jetzt keine Kernänderung mehr; Lauf 30 läuft durch.
```

### V087 · 21.09. 07:34:52 CEST · Hermes · Nachricht id 10660 · Sitzung `20260921_015554_e79a4a0f` · 572 B

```text
Kernfehler-Ausnahme, kurz: Lauf 29 ist gestorben, weil meine Kasse-Reparatur die Instrumentbindung gebrochen hat — der Vorspann-Nachweis versiegelt `kasse.py`, und ich habe die Datei nach dem Vorspann geändert. Die Sperre „Messgerät verändert, keine Nacheichung" hat exakt so gegriffen, wie sie soll.

Vor dem Neustart: volle Regression **301 passed, 2 skipped** (die zwei sind die bekannten, die eine private Werkkopie brauchen). Der Kern ist ab jetzt eingefroren; Lauf 30 läuft die vollständige Kette bis zum Maß durch und bricht bei der ersten roten Stufe ab.
```

### V088 · 21.09. 08:23:05 CEST · Hermes-Zwischentext · Nachricht id 10664 · Sitzung `20260921_015554_e79a4a0f` · 199 B

```text
Dasselbe Modell, derselbe 429 — und die Meldung sagt ausdrücklich „retry shortly". Ein explizit wiederholbarer Fehler darf nicht sofort als Ausfall zählen; das ist eine echte Lücke im Adapter.
```

### V089 · 21.09. 08:28:24 CEST · Hermes · Nachricht id 10668 · Sitzung `20260921_015554_e79a4a0f` · 1674 B

```text
I've stopped. The test run was blocked, so I won't retry it or work around it.

Where things stand right now:

**Lauf 30 is red at gen0** — same cause as Lauf 29: qwen/qwen3.8-flash returned HTTP 429 ("temporarily rate-limited upstream, please retry shortly"), the adapter counted it immediately as a Verbundausfall, and the unresolved-consumption rule locked the whole Auftrag.

**What I was in the middle of:** writing a test (`tests/test_t3_anbieter_wiederholung.py`, already on disk, not yet run) for what I consider a real instrument gap — an error the provider itself labels as retryable shouldn't count as an Ausfall until it has actually been retried. Ablehnung and leere Antwort would stay non-retried, since those are decisions, not disruptions.

**What I have not done:** no change to `biotop/anbieter/__init__.py`, no rerun, no further Lauf.

Two things need your decision before I touch anything else:

1. **Is the retry change in scope?** It modifies the Kern again after I had declared it frozen, which by Satz 2 kills Lauf 30 and forces Lauf 31. The alternative is to leave the adapter as is and accept that any upstream throttling of a single model stops the Auftrag.

2. **Lauf 30's Ausfall is still unresolved** (Protokoll #16168, Aufruf #16167, reservation 0,0028 €). I can clear it the same way as the previous one — booking the Höchstfall against the budget — but that only helps if the retry question is settled first, otherwise the next gen0 hits the same 429.

Verbrauch stands at 0,0133 € of 10 €. Vorspann of Lauf 30 passed (Nachweis `a0cd7718…`), and gen0 measured 83 of 100 Mutanten already caught before any new test was built.
```

### V090 · 21.09. 12:05:50 CEST · Philipp · Nachricht id 10669 · Sitzung `20260921_015554_e79a4a0f` · 1422 B

```text
Richtig angehalten — drei Vorentscheidungen von Chat-Claude. Erstens einchecken, jetzt, vor jeder weiteren Änderung: Lässt sich der abgenommene Stand aus Vorbedingung 1 noch vom T3-Stand trennen, zuerst ihn als eigenen Commit, gegen das Übergabe-Manifest geprüft, sonst ein Commit mit ehrlicher Beschreibung; künftig ist jede Abnahme und jeder eingefrorene Kern ein eigener Commit. Zweitens den offenen Ausfall aus Lauf 30 mit dem Höchstfall klären. Drittens Wiederholung ja, als Messgerätkorrektur aus T3: nur bei Fehlern, die der Anbieter ausdrücklich als wiederholbar kennzeichnet, mit vorher festgelegter Höchstzahl und Wartezeit, danach Ausfall wie bisher; eine Ablehnung wird nie wiederholt, eine Zeitüberschreitung bleibt Ausfall nach Satz 8, jeder Versuch wird protokolliert und gebucht, und die Gegenprobe zeigt, dass ein Fehler ohne Wiederholungshinweis sofort als Ausfall zählt. Im selben Zug, damit nur Lauf 30 stirbt: Die Auftragsgrenze verweigert den Start, wenn die Budgetvariablen fehlen oder null sind — null als „keine Grenze" ist dieselbe Fehlerklasse wie die leere Norm-Eichprobe, und das Setzen der Variablen behebt nur diesen einen Fall. Danach volle Regression, Kern einfrieren, Lauf 31 nach Tor 4 bis zum Ende, ohne Zwischenmeldungen und auf Deutsch. Auf die Liste für danach, nicht jetzt: Die Rauschmessung verwirft ihre Einzelwerte, damit bleibt jede Sperre undiagnostizierbar.
```

### V091 · 21.09. 12:06:25 CEST · Hermes-Zwischentext · Nachricht id 10670 · Sitzung `20260921_015554_e79a4a0f` · 153 B

```text
Drei Vorentscheidungen verstanden. Ich beginne mit dem Einchecken — und prüfe zuerst, ob sich der Vorbedingung-1-Stand überhaupt noch trennen lässt.
```

### V092 · 21.09. 12:07:14 CEST · Hermes-Zwischentext · Nachricht id 10678 · Sitzung `20260921_015554_e79a4a0f` · 201 B

```text
Nicht trennbar auf den ersten Blick — aber der abgenommene Stand liegt als Dateien vor. Ich prüfe, ob er gegen das Übergabe-Manifest verifizierbar ist; dann sind doch zwei saubere Commits möglich.
```

### V093 · 21.09. 12:08:04 CEST · Hermes-Zwischentext · Nachricht id 10684 · Sitzung `20260921_015554_e79a4a0f` · 248 B

```text
Mein Prüfkriterium war falsch: Das Archiv ist der **vollständige** Stand (140 Dateien, SHA bytegleich), `ausgang/` nur ein Auszug davon — alle 104 gemeinsamen Dateien sind bytegleich. Der abgenommene Stand ist damit verifiziert rekonstruierbar.
```

### V094 · 21.09. 12:08:33 CEST · Hermes-Zwischentext · Nachricht id 10688 · Sitzung `20260921_015554_e79a4a0f` · 140 B

```text
Trennung ist möglich: Das Archiv enthält HEAD vollständig (0 Dateien nur in HEAD) plus 11 geänderte und 29 neue. Ich setze zwei Commits.
```

### V095 · 21.09. 12:08:51 CEST · Hermes-Zwischentext · Nachricht id 10694 · Sitzung `20260921_015554_e79a4a0f` · 128 B

```text
Commit fehlgeschlagen (Git-Identität fehlt), aber der Arbeitsstand kam unverändert zurück — 175 von 175 Dateien bytegleich.
```

### V096 · 21.09. 12:09:04 CEST · Hermes-Zwischentext · Nachricht id 10698 · Sitzung `20260921_015554_e79a4a0f` · 113 B

```text
Commit 1 sitzt: `bb8eb0f`, 49 Dateien, Arbeitsstand unverändert zurückgeholt. Jetzt Commit 2 für den T3-Zubau.
```

