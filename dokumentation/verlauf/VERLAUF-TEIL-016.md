# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 016 von 054

- Einträge V0229 bis V0286. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0229 · 19.09.2026 20:16:24 CEST · Hermes-Zwischentext · Nachricht id 2249 · Sitzung `20260918_225920_3e614670` · 131 B

```text
Median-Messung und gemessene Toleranz stehen. Ich sichere den Stand und schreibe den ersten Zwischenbericht in den Nachlauf-Ordner.
```

### V0230 · 19.09.2026 20:16:38 CEST · Hermes · Nachricht id 2251 · Sitzung `20260918_225920_3e614670` · 1439 B

```text
Beide Regeln greifen nachweislich: 13,0 ms gegen Bestwert 10,0 reißt bei fester 15-%-Toleranz, bei gemessenen 47 % nicht.

Der Median-Effekt ist an deinem Beispiel sofort sichtbar — `formeln` maß roh [1,31 / 1,51 / 35,22] ms: das alte Minimum hätte 1,31 als Bestwert festgeschrieben und jeden späteren Kandidaten über 1,51 getötet; der Median nimmt 1,51.

**Nachlauf zu Phase 3, Stand:**
- **Punkt 8 (Median-Laufzeiten, F5 3.5): erledigt** — `messgeraet.py` nimmt den Median aus drei Durchläufen, die Rohwerte stehen als `laufzeit_roh` in jeder Messung. Das war bisher das Minimum.
- **Rauschtoleranz je Bereich: eingebaut** — `grenzen_f2` nimmt die gemessene Toleranz (Spannweite + 10 Prozentpunkte, mindestens 1,15); fehlt sie, greift der Rückfallwert und sagt das im Ablehnungsgrund. Die Messung selbst kommt als Teil von „Generation minus eins".
- Ordner `laeufe/biotop-phase-3-nachlauf/` ist angelegt. Commit `a41838c`.

Offen: Artgedächtnis auf Muster umstellen und beide Werke nachabstrahieren, Doppelungsschlüssel auf die Behauptung (dann Tor 2 Zeile 8 neu messen), Archivierung nach der neuen Zeile, Projektgedächtnis-Differenz an den drei strittigen Fällen, Generation minus eins und Fund-Neubewertung als Organe, Gate-Ausnahme für Abbrüche, Verfassungsentwurf abdrucken.

Kosten bisher: 0 € von 10 € (nur Codeänderungen, kein Modellaufruf). Zwischenbericht schreibe ich vor Sitzungsende in den Ordner.
```

### V0231 · 19.09.2026 20:29:29 CEST · Philipp · Nachricht id 2252 · Sitzung `20260918_225920_3e614670` · 836 B

```text
Der Rohwert 35,22 in [1,31 / 1,51 / 35,22] ist kein Rauschen, sondern ein Maschinenaussetzer, und er wirkt zweifach: Der Median fängt ihn beim Messwert ab, aber die Spannweite daraus setzt die Toleranz auf 2.600 % — ein Bereich, in dem danach jede echte Verschlechterung durchgeht. Festlegung (Chat-Claude, kommt in Fassung 6): Rauschmessung mit fünf Werten je Bereich, höchsten und niedrigsten streichen, Spannweite aus den mittleren drei; Toleranz bei Faktor 2,0 gedeckelt; ein Einzelwert über dem Fünffachen des Medians gilt als Aussetzer, wird verworfen und einmal nachgemessen, protokolliert; bleibt die Toleranz eines Bereichs über 1,5, meldet das Biotop ein Messproblem statt es als Toleranz hinzunehmen. Einbauen, bevor die erste Rauschmessung läuft — danach unverändert weiter mit den offenen Punkten des Nachlaufs.
```

### V0232 · 19.09.2026 20:29:43 CEST · Hermes-Zwischentext · Nachricht id 2253 · Sitzung `20260918_225920_3e614670` · 164 B

```text
Vier Regeln, die zusammengehören: getrimmte Spannweite, Deckel, Aussetzer-Erkennung, Meldeschwelle. Ich baue sie in den Kern, bevor die erste Rauschmessung läuft.
```

### V0233 · 19.09.2026 20:30:21 CEST · Hermes-Zwischentext · Nachricht id 2257 · Sitzung `20260918_225920_3e614670` · 88 B

```text
Jetzt gegen deinen Fall und die Grenzfälle prüfen, bevor ich sie an echte Werke lasse.
```

### V0234 · 19.09.2026 20:30:43 CEST · Hermes-Zwischentext · Nachricht id 2261 · Sitzung `20260918_225920_3e614670` · 59 B

```text
Drei Befunde, einer davon ein echter Fehler in meinem Code:
```

### V0235 · 19.09.2026 20:31:03 CEST · Hermes-Zwischentext · Nachricht id 2265 · Sitzung `20260918_225920_3e614670` · 110 B

```text
Alle sechs Fälle verhalten sich jetzt wie festgelegt. Ich sichere den Stand und schreibe den Zwischenbericht.
```

### V0236 · 19.09.2026 20:31:20 CEST · Hermes · Nachricht id 2267 · Sitzung `20260918_225920_3e614670` · 2090 B

```text
Rauschregeln eingebaut und in sechs Fällen selbstgeprüft (`ausgaben/01-rauschregeln-selbstpruefung.txt`), bevor eine echte Rauschmessung läuft. Commit `ab3a47f`.

**Dein Fall, jetzt durchgerechnet:** [1,31 / 1,51 / 35,22 / 1,40 / 1,45] → Median 1,45, **35,22 als Aussetzer verworfen** (> 5× Median), `nachmessen: true` protokolliert, getrimmte Spannweite 3,6 % → **Toleranz 1,15** statt der 2.600 %, die der ungetrimmte Wert ergeben hätte.

**Ein Fehler in meinem ersten Einbau, gefunden durch die Selbstprüfung:** Ich hatte das Streichen von Höchst- und Tiefstwert an „mindestens 5 Werte" gebunden — nach dem Abzug eines Aussetzers waren es nur noch 4, und der Trimm fiel still aus. Dadurch floss der 1,31-Ausreißer voll ein (Toleranz 1,253 statt 1,15). Korrigiert: getrimmt wird ab 3 Werten, immer.

**Die anderen fünf Fälle:**
- stabiler Bereich [7,90 … 8,46] → Spannweite 2 %, Toleranz 1,15, keine Meldung
- echtes Eigenrauschen 26 % → Toleranz 1,36, unter der Meldeschwelle, keine Meldung
- zwei Aussetzer [38 / 40] → beide verworfen, `nachmessen`
- Spannweite 60 % → Toleranz 1,70, **Messproblem gemeldet**
- Spannweite 200 % → **Deckel 2,0** greift, Messproblem gemeldet

Die Werte stehen als Konstanten im Kern (`RAUSCH_MESSUNGEN=5`, `RAUSCH_DECKEL=2.0`, `RAUSCH_MELDESCHWELLE=1.5`, `RAUSCH_AUSSETZER=5.0`, `RAUSCH_ZUSCHLAG=0.10`) und sind als Fassung-6-Festlegung von dir gekennzeichnet.

Eine Rückfrage, bevor ich „Generation minus eins" verdrahte: Wenn ein Bereich ein Messproblem meldet — soll der Lauf **gar nicht starten** (wie bei einer nicht bestandenen Probe, Satz 6 „laut scheitern") oder mit dem Deckel 2,0 und ausgewiesener Meldung weiterlaufen? Ich würde nicht starten; eine Toleranz über 1,5 macht jede Grenzmaßaussage des Laufs wertlos. Sag Bescheid — bis dahin arbeite ich an den übrigen Nachlaufpunkten weiter.

Zwischenbericht liegt im Ordner (`laeufe/biotop-phase-3-nachlauf/`, 2 Dateien, Prüfsumme `8283373132ea14d2ddd60f327744dabedd297d830ab58d5842f3750f90f32d1c`). Kosten: 0 € von 10 €, bisher kein Modellaufruf.
```

### V0237 · 19.09.2026 20:34:23 CEST · Philipp · Nachricht id 2268 · Sitzung `20260918_225920_3e614670` · 873 B

```text
Nicht starten — aber bereichsweise, nicht für das ganze Werk: Meldet ein Bereich ein Messproblem (Toleranz über 1,5), wird dieser Bereich übersprungen, seine Kandidaten werden nicht erzeugt, und die Sperre steht mit Zahl im Bericht („Bereich X übersprungen, Toleranz 1,7"); melden alle Bereiche ein Problem, startet der Lauf gar nicht. Ein gesperrter Bereich wird vor jedem weiteren Lauf neu gemessen, und meldet derselbe Bereich dreimal hintereinander, ist das ein Befund über seine Referenzlast, nicht über die Maschine, und gehört so in den Bericht. Dein Trimm-Fund (Schutz fiel nach Abzug eines Aussetzers still aus, weil nur noch 4 Werte übrig waren) ist genau der Fall, für den „Generation minus eins" da ist — gefunden vor der ersten echten Messung statt nach fünf verworfenen Läufen; kommt so in Fassung 6. Weiter mit den offenen Nachlaufpunkten.
```

### V0238 · 19.09.2026 20:34:39 CEST · Hermes-Zwischentext · Nachricht id 2269 · Sitzung `20260918_225920_3e614670` · 109 B

```text
Bereichsweise Sperre mit Zähler über Läufe hinweg — ich baue sie als Teil von „Generation minus eins".
```

### V0239 · 19.09.2026 20:35:29 CEST · Hermes-Zwischentext · Nachricht id 2273 · Sitzung `20260918_225920_3e614670` · 85 B

```text
Die Serien-Berechnung ist verworren — ich vereinfache sie, sonst zählt sie falsch.
```

### V0240 · 19.09.2026 20:35:49 CEST · Hermes-Zwischentext · Nachricht id 2275 · Sitzung `20260918_225920_3e614670` · 98 B

```text
Jetzt gegen eine echte Kammer prüfen, mit einer absichtlich unsteten Referenzlast als Gegenprobe.
```

### V0241 · 19.09.2026 20:37:13 CEST · Hermes-Zwischentext · Nachricht id 2281 · Sitzung `20260918_225920_3e614670` · 163 B

```text
Fall D ist nicht eingetreten — die Zufallslast war in dem Durchgang zu zahm. Ich messe ihn mit einer sicher unsteten Last nach, statt das Ergebnis schönzureden.
```

### V0242 · 19.09.2026 20:37:43 CEST · Hermes-Zwischentext · Nachricht id 2285 · Sitzung `20260918_225920_3e614670` · 237 B

```text
Der Fall D scheitert an meiner Probe, nicht am Organ: Die Median-Regel glättet die Schwankung schon **innerhalb** einer Messung (3 Läufe je Messwert), deshalb kamen fünf stabile Werte heraus. Ich muss zwischen den Messungen variieren.
```

### V0243 · 19.09.2026 20:38:24 CEST · Hermes · Nachricht id 2291 · Sitzung `20260918_225920_3e614670` · 2516 B

```text
„Generation minus eins", Teil 1 steht und ist an echten Kammerläufen geprüft (`ausgaben/02-…`, `03-…`).

**Fall A — echtes Werk, echte Referenzlast:** 0 von 4 Bereichen gesperrt. Toleranzen bericht 1,15 (Spannweite 4 %), formeln 1,21 (11 %), lager 1,15 (5 %), preise 1,15 (3 %). Zum Vergleich: In Phase 3 hatte ich bei `formeln` 47 % gemessen — mit Median-Messung und getrimmter Spannweite sind es 11 %. Ein großer Teil dessen, was ich damals „Eigenrauschen" nannte, war die Minimum-Regel plus Aussetzer.

**Fall B — Referenzlast von `preise` absichtlich unstet:** 2 von 4 gesperrt, der Lauf startet trotzdem. `preise` übersprungen mit Toleranz 2,00 (Spannweite 109 %, Werte [16,82 / 63,6 / 132,79 / 133,05 / 138,1]), `bericht` mitgerissen mit 1,59 — plausibel, weil `bericht` über `preise` rechnet. `formeln` (1,38) und `lager` (1,18) arbeiten weiter, ihre Toleranzen gehen in den Lauf.

**Fall C — Serienzähler:** Messung 2 → Serie 2, kein Befund; Messung 3 → Serie 3, **Befund über die Referenzlast** mit der von dir verlangten Unterscheidung im Klartext („Befund über die REFERENZLAST von `preise`, nicht über die Maschine").

**Fall D — einziger Bereich gesperrt → Lauf startet nicht:** bestanden, mit Protokollzeile `eichung.lauf_startet_nicht`.

**Ein Fehler in meiner Probe, nicht im Organ** — und er ist lehrreich: Mein erster Fall D ließ jeden zweiten *Einzelaufruf* 150 ms warten und ergab fünf **stabile** Werte, Toleranz 1,20, keine Sperre. Ursache: Der Median aus drei Durchläufen glättet Schwankungen innerhalb einer Messung — genau seine Aufgabe. Unstetigkeit wird nur sichtbar, wenn sich ganze Messungen unterscheiden. Nach Umstellung auf den Messungs-Index: Werte [12,61 / 13,14 / 13,24 / 20,56 / 22,38], Spannweite 56 %, Toleranz 1,67, gesperrt. Beide Regeln greifen also ineinander — der Median darf die Rauschmessung nicht blind machen, und tut es hier nicht, weil sie über fünf getrennte Messungen geht.

Konstanten im Kern, als deine Festlegung gekennzeichnet: `RAUSCH_MESSUNGEN=5`, `RAUSCH_DECKEL=2.0`, `RAUSCH_MELDESCHWELLE=1.5`, `RAUSCH_AUSSETZER=5.0`, `SPERR_MELDUNGEN_BIS_BEFUND=3`. Sperren werden in der Tabelle `eichung` je Werk und Bereich geführt, damit der Zähler über Läufe hinweg trägt.

Zwischenbericht im Ordner, 4 Dateien, Prüfsumme `6f5347b38fcc779699e370946818ee4f92a674d3b4270b0c185e0fdc3bf4537f`. Kosten weiterhin 0 € von 10 €.

Weiter mit Teil 2 (die vier Eichproben als Vorspann) und den übrigen Nachlaufpunkten.
```

### V0244 · 19.09.2026 21:21:10 CEST · Philipp · Nachricht id 2292 · Sitzung `20260918_225920_3e614670` · 943 B

```text
Fall A ist der Kern: Die 47 % waren nie Eigenrauschen — mit Median und getrimmter Spannweite sind es 11 %; meine Fassung-5-Begründung war gegen eine verfälschte Messung gesetzt, der Fehler lag eine Ebene tiefer, und das gehört so in den Nachlaufbericht (Zahl alt/neu, Ursache benannt). Aus deinem Fall-D-Fund wird eine allgemeine Regel für Fassung 6: Streuung wird immer zwischen Messungen gebildet, nie innerhalb einer — der Median glättet innerhalb, die Streuung misst zwischen, und wer beides auf derselben Ebene bildet, misst die Glättung statt der Sache; das gilt für jede Kennzahl, die das Biotop über wiederholte Messungen bildet, nicht nur für die Rauschmessung. Dazu eine Präzisierung am Serienzähler: Der Befund nennt den Zeitraum der drei Meldungen mit, weil drei Läufe in einer Sitzung auf die Maschine deuten und drei an verschiedenen Tagen auf die Referenzlast. Weiter mit Teil 2 und den übrigen Nachlaufpunkten.
```

### V0245 · 19.09.2026 21:21:24 CEST · Hermes-Zwischentext · Nachricht id 2293 · Sitzung `20260918_225920_3e614670` · 98 B

```text
Beide Punkte gehören in den Code, nicht nur in den Bericht. Zuerst der Zeitraum am Serienzähler.
```

### V0246 · 19.09.2026 21:21:57 CEST · Hermes-Zwischentext · Nachricht id 2299 · Sitzung `20260918_225920_3e614670` · 135 B

```text
Jetzt die allgemeine Regel als Kernfunktion — Streuung wird nur zwischen Messungen gebildet, mit eingebauter Sperre gegen den Fehler.
```

### V0247 · 19.09.2026 21:22:16 CEST · Hermes-Zwischentext · Nachricht id 2303 · Sitzung `20260918_225920_3e614670` · 127 B

```text
Jetzt die Rauschmessung auf die gemeinsame Funktion umstellen, damit es nur eine Stelle gibt, und die Zeitraum-Deutung prüfen.
```

### V0248 · 19.09.2026 21:22:56 CEST · Hermes-Zwischentext · Nachricht id 2309 · Sitzung `20260918_225920_3e614670` · 103 B

```text
Beide Deutungen greifen bei identischen Rauschwerten — der Unterschied kommt allein aus dem Zeitraum.
```

### V0249 · 19.09.2026 21:23:11 CEST · Hermes · Nachricht id 2311 · Sitzung `20260918_225920_3e614670` · 1934 B

```text
Beide Festlegungen sind im Code, nicht nur im Bericht.

**Streuungsregel als Kernfunktion** (`messgeraet.streuung`): bildet Streuung ausschließlich über wiederholte Messungen; `ebene="innerhalb"` wirft eine Ausnahme mit Begründung, statt still eine falsche Zahl zu liefern. Die Rauschmessung ruft jetzt diese eine Stelle auf, damit es keine zweite Rechenweise gibt. Die Begründung im Docstring nennt den Fund am Fall D: 150 ms je Einzelaufruf → fünf stabile Werte, Toleranz 1,20; dieselbe Verzögerung zwischen Messungen → Spannweite 56 %, Sperre.

**Serienzähler mit Zeitraum**, geprüft an identischen Rauschwerten [10,0 / 10,2 / 16,0 / 17,0 / 17,5], Toleranz 1,77 in beiden Fällen:
- drei Meldungen innerhalb einer Sitzung (321 Minuten, 1 Tag) → **Deutung Maschine**, mit dem Zusatz „vor einem Befund über den Bereich an einem anderen Tag nachmessen"
- drei Meldungen an drei Tagen (17./18./19.09.) → **Deutung Referenzlast**, „sie misst etwas Unstetes, unabhängig vom Zustand der Maschine"

Der Zeitraum wird in der Meldung ausgeschrieben (von/bis, Tage bzw. Minuten) und als `serie_deutung` gespeichert. Beleg: `ausgaben/04-serienzaehler-zeitraum.txt`.

**Für den Nachlaufbericht notiert, wie von dir verlangt:** `formeln` Eigenrauschen **alt 47 % (Phase 3) → neu 11 %**, Ursache: die Einzelmessung nahm das Minimum aus drei Durchläufen statt des Medians, und ein Maschinenaussetzer (35,22 ms gegen Median 1,45) ging ungetrimmt in die Spannweite. Die Fassung-5-Begründung stand damit gegen eine verfälschte Messung; der Fehler lag eine Ebene tiefer. Die Regel selbst bleibt richtig — sie wird jetzt nur auf sauberen Zahlen gebildet.

Commit steht, Zwischenbericht im Ordner (5 Dateien, Prüfsumme `a8bcd2b2f2a920965e01ddca2c102258463507ddc1d12b242740d52914073539`), Kosten weiterhin 0 € von 10 €.

Weiter mit Teil 2: die vier Eichproben als Vorspann jedes Laufs, danach Artgedächtnis auf Muster.
```

### V0250 · 19.09.2026 21:31:13 CEST · Philipp · Nachricht id 2312 · Sitzung `20260918_225920_3e614670` · 659 B

```text
Die Kernfunktion mit Ausnahme statt Vorschrift ist schärfer als meine Festlegung — eine Rechenstelle, ein unmöglicher Verstoß; genau so gehört es gebaut. Eine Ergänzung zur Deutung „Maschine", ein Satz in der Meldung, kein neuer Einbau: Deutet der Serienzähler auf die Maschine, gilt der Vorbehalt für alle Laufzeitmessungen dieses Zeitraums, nicht nur für die gesperrten Bereiche — eine unruhige Maschine verfälscht jede Grenzmaßzahl, die dabei entsteht, und der Bericht muss das aussprechen statt es auf den einen Bereich zu begrenzen. Sonst unverändert weiter: Teil 2 mit den vier Eichproben als Vorspann, danach Artgedächtnis auf Muster.
```

### V0251 · 19.09.2026 21:31:26 CEST · Hermes-Zwischentext · Nachricht id 2313 · Sitzung `20260918_225920_3e614670` · 95 B

```text
Richtig — die Maschine ist nicht bereichsweise unruhig. Der Vorbehalt gehört in die Meldung.
```

### V0252 · 19.09.2026 21:31:34 CEST · Hermes-Zwischentext · Nachricht id 2315 · Sitzung `20260918_225920_3e614670` · 113 B

```text
Der Vorbehalt muss auch als Feld heraus, damit der Bericht ihn nicht übersehen kann — nicht nur im Fließtext.
```

### V0253 · 19.09.2026 21:32:10 CEST · Hermes-Zwischentext · Nachricht id 2321 · Sitzung `20260918_225920_3e614670` · 133 B

```text
Der Vorbehalt steht jetzt als eigene Berichtszeile — auch wenn `lager` nicht gesperrt war, gilt er sichtbar für dessen Zahlen mit.
```

### V0254 · 19.09.2026 21:32:20 CEST · Hermes · Nachricht id 2323 · Sitzung `20260918_225920_3e614670` · 1252 B

```text
Ergänzung eingebaut, Commit `679e99d`.

Bei Deutung „Maschine" trägt die Meldung jetzt den Vorbehalt im Klartext, und `text()` zieht ihn als **eigene Berichtszeile** heraus — belegt an einem Fall mit gesperrtem `preise` und ungesperrtem `lager`:

> Bereich preise ÜBERSPRUNGEN, Toleranz 1.77 … ← BEFUND ÜBER DIE MASCHINE
> Bereich lager: Toleranz 1.15 (Spannweite 3 %, Median 5.1 ms)
> Vorbehalt: Zwischen 2026-09-19T14:02 und 2026-09-19T19:23 war die Maschine unruhig (3 Sperrmeldungen in Folge in einer Sitzung). Jede Laufzeit- und Grenzmaßzahl aus diesem Zeitraum steht unter Vorbehalt — auch die der nicht gesperrten Bereiche.

Der Vorbehalt liegt zusätzlich als Feld `vorbehalt_zeitraum` (von/bis, Geltungsbereich, Satz) in der Messung, damit er nicht nur im Fließtext hängt; mehrere gesperrte Bereiche desselben Zeitraums erzeugen eine Zeile, nicht drei. Die Sperrmarkierung unterscheidet jetzt sichtbar „← BEFUND ÜBER DIE MASCHINE" von „← BEFUND ÜBER DIE REFERENZLAST".

Beleg aktualisiert in `ausgaben/04-serienzaehler-zeitraum.txt` (beide Fälle, identische Rauschwerte, nur der Zeitraum unterscheidet sie).

Weiter mit Teil 2: die vier Eichproben (Nebenwirkung, Regression, Norm, Vertrag) als Vorspann jedes Laufs.
```

### V0255 · 19.09.2026 21:34:33 CEST · Philipp · Nachricht id 2324 · Sitzung `20260918_225920_3e614670` · 841 B

```text
Antwort von hermes 

Zwei Festlegungen zum Vorspann, bevor du ihn verdrahtest (Chat-Claude, kommt in Fassung 6) — falls schon eingebaut, nur Commit und Beleg zurückmelden: Erstens braucht jede Eichprobe einen Gegenstand, ein Bereichspaar mit Vertrag, und der wird je Werk einmal gewählt und versiegelt, beim ersten Lauf, danach unverändert; sonst misst jede Eichung etwas anderes und ist mit der vorigen nicht vergleichbar. Fällt das Paar durch eine Änderung des Werks weg, ist das ein Befund und ein neuer versiegelter Gegenstand, protokolliert. Zweitens werden die Eichkosten je Lauf im Bericht getrennt ausgewiesen, Kammerläufe und Modellaufrufe einzeln, nicht in der Gesamtsumme — vier Proben vor jedem Lauf sind auf vier Bereichen billig und auf siebzehn Diensten möglicherweise nicht, und diese Zahl brauche ich vor Phase 4.
```

### V0256 · 19.09.2026 21:34:43 CEST · Hermes-Zwischentext · Nachricht id 2325 · Sitzung `20260918_225920_3e614670` · 148 B

```text
Teil 2 ist noch nicht verdrahtet — beide Festlegungen kommen also direkt in den Bau. Ich sehe mir zuerst an, woran die vier Proben bisher hängen.
```

### V0257 · 19.09.2026 21:35:56 CEST · Hermes-Zwischentext · Nachricht id 2327 · Sitzung `20260918_225920_3e614670` · 104 B

```text
Noch nicht gebaut — beide Festlegungen gehen direkt in den Bau ein. Zuerst der versiegelte Gegenstand.
```

### V0258 · 19.09.2026 21:36:14 CEST · Hermes-Zwischentext · Nachricht id 2329 · Sitzung `20260918_225920_3e614670` · 131 B

```text
Jetzt die Kostentrennung — Eichkosten müssen an der Quelle eigene Zwecke tragen, sonst sind sie nachträglich nicht separierbar.
```

### V0259 · 19.09.2026 21:36:41 CEST · Hermes-Zwischentext · Nachricht id 2331 · Sitzung `20260918_225920_3e614670` · 147 B

```text
Die kumulative Kassenabfrage ist fehleranfällig (MAX über Teile). Ich mache sie zu einer Differenz je Teil — sonst stimmt die Aufteilung nicht.
```

### V0260 · 19.09.2026 21:36:51 CEST · Hermes-Zwischentext · Nachricht id 2333 · Sitzung `20260918_225920_3e614670` · 91 B

```text
Jetzt die Rauschmessung mit Kostenbuchung verbinden und alles an einem echten Werk prüfen.
```

### V0261 · 19.09.2026 21:38:21 CEST · Hermes-Zwischentext · Nachricht id 2351 · Sitzung `20260918_225920_3e614670` · 91 B

```text
Die Hochrechnung ist falsch — ich korrigiere sie, bevor die Zahl in einen Bericht gerät.
```

### V0262 · 19.09.2026 21:38:59 CEST · Hermes · Nachricht id 2355 · Sitzung `20260918_225920_3e614670` · 2150 B

```text
Beide Festlegungen sind gebaut und geprüft (`ausgaben/05-eichgegenstand-und-kosten.txt`), noch bevor der Vorspann verdrahtet war — sie gingen also direkt in den Bau ein.

**(1) Versiegelter Eichgegenstand** (`organe/eichgegenstand.py`), an `lagerhaus` geprüft:
- Erster Lauf wählt deterministisch: **bericht→preise**, Vertrag `tests/vertraege/test_vertrag_bericht_preise.py`, Prüfsumme `10cb7f5d18560887`, Begründung mitgeschrieben („umfangreichster expliziter Vertrag, 49 Zeilen, von 3 Bereichspaaren mit Vertrag").
- Zweiter Lauf am unveränderten Werk: **derselbe Gegenstand, keine Neuwahl** (`unveraendert`, `neu: False`).
- Vertrag geändert → **Befund** mit beiden Prüfsummen im Klartext, alter Gegenstand abgelöst, neuer versiegelt, Protokollzeile `eichgegenstand.weggefallen`. Nie stiller Wechsel.
- Gibt es kein Bereichspaar mit Vertrag, meldet das Organ `eichgegenstand.fehlt` statt still zu bestehen (Satz 6).

**(2) Eichkosten getrennt** (`eichung.kosten_buchen/kosten/kosten_text`): eigene Tabelle `eichkosten`, je Teil Kammerläufe, Modellaufrufe, €, Dauer; Modellaufrufe der Eichung tragen den Zweck-Vorsatz `eichung.` und sind damit auch in `KASSE.md` trennbar. Gebucht wird je Teil die Differenz, damit sich die Teile zur Summe addieren. Gemessen an 4 Bereichen: **5 Kammerläufe, 0 Modellaufrufe, 0,0000 €, 14 s** (2,8 s je Kammerlauf).

**Eine Korrektur an meiner eigenen Ausgabe:** Mein erster Entwurf rechnete „× 17 Dienste = 21 Kammerläufe, 1 Minute" hoch. Das ist falsch — die Rauschmessung misst **alle Bereiche in einem Kammerlauf**; es bleiben fünf Läufe, egal ob vier oder siebzehn Bereiche. Mit der Bereichszahl wächst die **Dauer je Lauf**, nicht ihre Zahl. Die Zeile nennt jetzt die Dauer je Kammerlauf und sagt ausdrücklich, dass die Phase-4-Zahl am dortigen Werk zu messen und nicht von hier hochzurechnen ist. Die Zahl, die du vor Phase 4 brauchst, liefere ich also gemessen — sobald die vier Proben im Vorspann laufen, mit ihren Kammerläufen und Modellaufrufen einzeln.

Commit steht. Kosten weiterhin 0 € von 10 €. Als Nächstes die vier Proben selbst am versiegelten Gegenstand.
```

### V0263 · 19.09.2026 21:46:30 CEST · Philipp · Nachricht id 2356 · Sitzung `20260918_225920_3e614670` · 860 B

```text
Die Selbstkorrektur ist der wichtigste Teil der Meldung — du hast eine Hochrechnung zurückgenommen, die zu deinen Gunsten hätte gelesen werden können; so gehört es. Eine Präzisierung zur Wahl des Eichgegenstands (Chat-Claude, Fassung 6): Bei Werken mit Verfassung wird das Bereichspaar bevorzugt, das auf dem von der Verfassung als tragend benannten Pfad liegt; die Vertragsgröße entscheidet erst danach. Grund: Bei siebzehn Diensten ist der umfangreichste Vertrag nicht automatisch der aussagekräftigste, und eine Eichung an einem Nebenpfad übersieht Messgerätfehler im Kern — beim Handelssystem ist das der Orderpfad mit Risikomodulen und Verlustgrenze. Die Begründung wird ohnehin mitgeschrieben, dann steht dieser Grund dort mit drin. Weiter mit den vier Proben am versiegelten Gegenstand; die Modellaufrufe je Probe bitte einzeln ausweisen.
```

### V0264 · 19.09.2026 21:46:54 CEST · Hermes-Zwischentext · Nachricht id 2357 · Sitzung `20260918_225920_3e614670` · 117 B

```text
Verfassung zuerst, Vertragsgröße danach — ich sehe mir an, was von der Verfassung mechanisch auswertbar vorliegt.
```

### V0265 · 19.09.2026 21:47:20 CEST · Hermes-Zwischentext · Nachricht id 2361 · Sitzung `20260918_225920_3e614670` · 155 B

```text
Die Verfassung liegt als Text mit nummerierten Sätzen vor — ich mache den tragenden Pfad mechanisch auswertbar, mit expliziter Angabe als erster Quelle.
```

### V0266 · 19.09.2026 21:47:25 CEST · Hermes-Zwischentext · Nachricht id 2363 · Sitzung `20260918_225920_3e614670` · 77 B

```text
Der Patch hat die `lesen`-Signatur verschluckt — ich stelle sie wieder her.
```

### V0267 · 19.09.2026 21:47:39 CEST · Hermes-Zwischentext · Nachricht id 2365 · Sitzung `20260918_225920_3e614670` · 75 B

```text
Jetzt die Wahlregel selbst: Verfassung zuerst, Vertragsgröße erst danach.
```

### V0268 · 19.09.2026 21:48:25 CEST · Hermes-Zwischentext · Nachricht id 2373 · Sitzung `20260918_225920_3e614670` · 174 B

```text
Am `lagerhaus` fällt die Wahl auf dasselbe Paar wie zuvor — das beweist die Regel noch nicht. Ich prüfe den Fall, in dem die Verfassung auf den *kleinsten* Vertrag zeigt.
```

### V0269 · 19.09.2026 21:48:43 CEST · Hermes-Zwischentext · Nachricht id 2377 · Sitzung `20260918_225920_3e614670` · 148 B

```text
Die Gegenprobe beweist die Rangfolge: Bei ausdrücklicher Nennung wird `preise→formeln` (39 Zeilen) gegen `bericht→preise` (49 Zeilen) gewählt.
```

### V0270 · 19.09.2026 21:48:57 CEST · Hermes · Nachricht id 2379 · Sitzung `20260918_225920_3e614670` · 1857 B

```text
Präzisierung eingebaut und belegt (`ausgaben/06-eichgegenstand-verfassung-vor-groesse.txt`).

**Rangfolge jetzt:** tragender Pfad der Verfassung → dann Vertragsgröße → dann alphabetisch. Zwei Quellen für „tragend", beide benannt, nie geraten:
1. **Ausdrücklich** in den Regeln des Werks: `{"tragender_pfad": [["a","b"], …]}` — das ist der Weg für das Handelssystem (Orderpfad mit Risikomodulen und Verlustgrenze).
2. **Abgeleitet** aus dem Verfassungstext: Ein Paar gilt als tragend, wenn beide Bereiche in *einem* Satz gemeinsam genannt werden, gewichtet nach der Zahl solcher Sätze. Bei `lagerhaus` ergibt das bericht→lager 2, bericht→preise 2, preise→formeln 1.
3. Nennt die Verfassung nichts, entscheidet die Vertragsgröße — und die Begründung sagt genau das.

**Die Gegenprobe war nötig**, weil am `lagerhaus` das größte und das tragende Paar zufällig dasselbe sind — die Regel wäre dort nicht nachweisbar gewesen. Mit ausdrücklichem `tragender_pfad` auf `preise→formeln` (39 Zeilen, der **kleinste** Vertrag) wählt das Organ dieses Paar gegen `bericht→preise` (49 Zeilen): **Verfassung schlägt Vertragsgröße: True**. Danach habe ich die Regeln des Werks wiederhergestellt und den echten Gegenstand neu versiegelt.

Die Begründung wird wie zuvor mitgeschrieben und enthält den Grund im Klartext („weil eine Eichung an einem Nebenpfad Messgerätfehler im Kern übersieht"); das Protokoll `eichgegenstand.versiegelt` führt zusätzlich alle Kandidatenpaare mit Zeilenzahl **und** Tragend-Gewicht, damit die Wahl nachvollziehbar ist.

Zwischenbericht im Ordner (7 Dateien, Prüfsumme `c49f7b90c499303a973918816c3ab7ab1aa9f79d1a7da069c28182fe79052513`), Kosten weiterhin 0 € von 10 €.

Als Nächstes die vier Proben am versiegelten Gegenstand — Modellaufrufe je Probe einzeln ausgewiesen, wie verlangt.
```

### V0271 · 19.09.2026 21:50:22 CEST · Philipp · Nachricht id 2380 · Sitzung `20260918_225920_3e614670` · 764 B

```text
Die Gegenprobe war der richtige Schritt — am lagerhaus fallen größtes und tragendes Paar zusammen, die Regel wäre ungeprüft durchgegangen. Eine Einschränkung zur zweiten Quelle (Chat-Claude, Fassung 6): Die Ableitung aus dem Verfassungstext ist eine Wortstatistik — sie findet, was oft zusammen genannt wird, nicht was trägt — und gilt deshalb nur für Übungswerke. Bei Werken mit Betriebszweck muss der tragende Pfad ausdrücklich in den Regeln des Werks stehen; fehlt er dort, meldet das Organ das und wartet, statt abzuleiten (wie beim fehlenden Bereichspaar). Beim Handelssystem setzt Philipp ihn in der Verfassung, zusammen mit Verlustgrenze und Hebelgrenzen. Weiter mit den vier Proben am versiegelten Gegenstand, Modellaufrufe je Probe einzeln.
```

### V0272 · 19.09.2026 21:50:52 CEST · Hermes-Zwischentext · Nachricht id 2381 · Sitzung `20260918_225920_3e614670` · 149 B

```text
Klar — eine Wortstatistik darf nicht über den Orderpfad entscheiden. Die Regeln tragen bereits das Kennzeichen `uebungswerk`, daran hänge ich es.
```

### V0273 · 19.09.2026 21:51:03 CEST · Hermes-Zwischentext · Nachricht id 2383 · Sitzung `20260918_225920_3e614670` · 106 B

```text
Jetzt muss `sichern` beim Vermerk anhalten statt zu wählen — sonst bleibt die Einschränkung folgenlos.
```

### V0274 · 19.09.2026 21:51:54 CEST · Hermes-Zwischentext · Nachricht id 2395 · Sitzung `20260918_225920_3e614670` · 47 B

```text
Alle drei Fälle verhalten sich wie festgelegt.
```

### V0275 · 19.09.2026 21:52:03 CEST · Hermes · Nachricht id 2397 · Sitzung `20260918_225920_3e614670` · 1151 B

```text
Einschränkung eingebaut und in drei Fällen belegt (`ausgaben/07-tragender-pfad-nur-uebungswerk.txt`):

- **Übungswerk** (`uebungswerk: true`) → Ableitung zulässig, Gegenstand versiegelt; die Herkunft sagt jetzt ausdrücklich „nur zulässig bei Übungswerken; Wortstatistik".
- **Werk mit Betriebszweck ohne `tragender_pfad`** → kein Gegenstand, `wartet: True`, Protokollzeile `eichgegenstand.wartet` mit der erwarteten Ergänzung im Klartext („Regeln des Werks um `tragender_pfad` ergänzen — beim Handelssystem der Orderpfad mit Risikomodulen und Verlustgrenze; setzt Philipp") und der Liste der Paare, die *nicht* gewählt wurden.
- **Werk mit Betriebszweck mit `tragender_pfad`** → wählt `preise→formeln` aus der Verfassung.

Das Warten ist nicht nur ein Vermerk: `sichern()` gibt keinen Gegenstand zurück, damit kann der Vorspann nicht starten — dieselbe Logik wie beim fehlenden Bereichspaar.

Zwischenbericht im Ordner (8 Dateien, Prüfsumme `8080753f23f7b5ea572616cde1d4897b5a43571ff00eb327195ccac15230afd0`), Kosten 0 € von 10 €.

Jetzt die vier Proben am versiegelten Gegenstand, mit Modellaufrufen je Probe einzeln.
```

### V0276 · 19.09.2026 21:53:16 CEST · Philipp · Nachricht id 2398 · Sitzung `20260918_225920_3e614670` · 942 B

```text
Dass sichern() ohne Gegenstand nichts zurückgibt und der Vorspann damit gar nicht starten kann, ist die richtige Bauweise — ein übersehbarer Vermerk hätte nichts getaugt. Eine Festlegung, bevor die Proben laufen (Chat-Claude, Fassung 6): Probenkandidaten und ihre Ergebnisse kommen in keines der drei Gedächtnisse — nicht ins Projektgedächtnis, wo ein eingeschleuster Regressionskandidat später echte Kandidaten sperren würde, nicht ins Artgedächtnis, wo ein Probenmuster als Erfahrung an andere Werke weitergereicht würde, nicht ins Geschmacksgedächtnis. In Phase 2 genügte die Kennzeichnung nische='probe', weil es noch keine Gedächtnisse gab; jetzt läuft der Vorspann vor jedem Lauf, und damit fiele bei jedem Lauf neuer Probenabfall hinein. Die Proben bleiben in der Datenbank und im Bericht sichtbar, nur die Gedächtnisse lesen sie nicht. Dann die vier Proben am versiegelten Gegenstand, Modellaufrufe je Probe einzeln.
```

### V0277 · 19.09.2026 21:53:24 CEST · Hermes-Zwischentext · Nachricht id 2399 · Sitzung `20260918_225920_3e614670` · 162 B

```text
Bevor Proben laufen, muss die Sperre stehen — sonst schreibt der erste Vorspann schon Abfall hinein. Ich sehe nach, wo Kandidaten in die Gedächtnisse fließen.
```

### V0278 · 19.09.2026 21:53:46 CEST · Hermes-Zwischentext · Nachricht id 2403 · Sitzung `20260918_225920_3e614670` · 126 B

```text
Ich setze die Sperre an der Eintrittsstelle jedes Gedächtnisses — nicht beim Aufrufer, sonst wird sie irgendwann vergessen.
```

### V0279 · 19.09.2026 21:54:18 CEST · Hermes-Zwischentext · Nachricht id 2413 · Sitzung `20260918_225920_3e614670` · 104 B

```text
Jetzt die Leseseite prüfen — die Sperre nützt nichts, wenn Altbestand aus Phase 3 noch gelesen wird.
```

### V0280 · 19.09.2026 21:54:47 CEST · Hermes-Zwischentext · Nachricht id 2415 · Sitzung `20260918_225920_3e614670` · 149 B

```text
Zwei Probenkandidaten aus Phase 3 liegen bereits im Projektgedächtnis — genau der Abfall, den du meinst. Ich räume sie aus und prüfe die Sperre.
```

### V0281 · 19.09.2026 21:55:24 CEST · Hermes · Nachricht id 2423 · Sitzung `20260918_225920_3e614670` · 1562 B

```text
Sperre steht an allen drei Eintrittsstellen — in `projekt_merken`, `art_merken`, `geschmack_merken` selbst, nicht beim Aufrufer, damit sie nicht umgangen werden kann. Beleg: `ausgaben/08-proben-ausserhalb-gedaechtnis.txt`.

**Altbestand war schon da:** Zwei Probenkandidaten aus Phase 3 (K1162, K1163 aus der Nachprobe zu Zeile 7) lagen bereits im Projektgedächtnis — genau der Abfall, den du meinst, nur eben aus der Zeit, als es die Regel noch nicht gab. Entfernt und protokolliert (`gedaechtnis.probenabfall_entfernt`, mit Auflistung). Artgedächtnis und Geschmacksgedächtnis waren sauber (je 0).

**Sperre geprüft:** Derselbe Probenkandidat allen drei Gedächtnissen angeboten → Projektgedächtnis 495 → 495, Artgedächtnis 492 → 492, Geschmack 30 → 30, je eine Protokollzeile `gedaechtnis.probe_uebersprungen` mit Nische, Bereich und Grund.

**Gegenprobe:** Ein echter Kandidat (K2062, preise/wild) wird normal aufgenommen, 494 → 495 — die Sperre trifft nur Proben.

**Sichtbarkeit:** 29 Probenkandidaten stehen unverändert in `kandidaten` und bleiben im Bericht auffindbar; nur die Gedächtnisse lesen sie nicht.

Erkannt werden Proben an der Nische *oder* am Bereichsnamen (`probe…`) — die Jury-Proben liefen unter eigenen Bereichsmarken, die wären bei reiner Nischenprüfung durchgerutscht.

Zwischenbericht im Ordner (9 Dateien, Prüfsumme `108f8c22ca9c9b67a588b14d0af98449744277c23cf18a6410090e46ff37776b`), Kosten 0 € von 10 €.

Jetzt die vier Proben am versiegelten Gegenstand, Modellaufrufe je Probe einzeln ausgewiesen.
```

### V0282 · 19.09.2026 21:56:50 CEST · Philipp · Nachricht id 2424 · Sitzung `20260918_225920_3e614670` · 949 B

```text
Dass du den Altbestand nachgesehen und zwei Probenkandidaten aus dem Projektgedächtnis entfernt hast, statt die Sperre nur vorwärts wirken zu lassen, ist der wichtigste Teil — die Regel hatte schon Schaden angerichtet. Eine Härtung dazu (Chat-Claude, Fassung 6): Eine Probe wird an einem gesetzten Merkmal erkannt, nicht an ihrem Namen. Du schleust die Proben selbst ein, also setzt du beim Erzeugen ein Feld am Kandidaten (ist_probe), und die Sperre prüft dieses Feld; Nische und Bereichsname bleiben als zweiter Weg für Altbestand, sind aber nicht die Grundlage. Grund: Die Jury-Proben wären bei reiner Nischenprüfung durchgerutscht, weil sie unter eigenen Bereichsmarken liefen — dieselbe Fehlerklasse wie die Doppelungserkennung, die auf den Ort statt auf die Behauptung sah, und eine künftige Probe unter neuem Namensschema rutscht sonst wieder durch. Dann die vier Proben am versiegelten Gegenstand, Modellaufrufe je Probe einzeln.
```

### V0283 · 19.09.2026 21:57:00 CEST · Hermes-Zwischentext · Nachricht id 2425 · Sitzung `20260918_225920_3e614670` · 136 B

```text
Richtig — ein Merkmal, das der Erzeuger setzt, statt eines Namens, den ein späterer Einbau anders schreibt. Ich füge das Feld hinzu.
```

### V0284 · 19.09.2026 21:57:28 CEST · Hermes-Zwischentext · Nachricht id 2431 · Sitzung `20260918_225920_3e614670` · 105 B

```text
Die Sperrstellen müssen `ist_probe` mitlesen — `geschmack_merken` holt derzeit nur Nische und Bereich.
```

### V0285 · 19.09.2026 21:57:33 CEST · Hermes-Zwischentext · Nachricht id 2433 · Sitzung `20260918_225920_3e614670` · 83 B

```text
Jetzt die Erzeuger: Alle Stellen, die Proben einschleusen, müssen das Feld setzen.
```

### V0286 · 19.09.2026 21:58:29 CEST · Hermes-Zwischentext · Nachricht id 2443 · Sitzung `20260918_225920_3e614670` · 111 B

```text
Jetzt der entscheidende Nachweis: eine Probe unter einem **neuen** Namensschema, das der Namensweg nicht kennt.
```

