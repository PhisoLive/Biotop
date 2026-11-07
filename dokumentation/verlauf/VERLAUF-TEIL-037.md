# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 037 von 054

- Einträge V0753 bis V0815. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0753 · 22.09.2026 14:56:20 CEST · Hermes-Zwischentext · Nachricht id 11322 · Sitzung `20260921_015554_e79a4a0f` · 77 B

```text
3 von 5 behoben — 60 %, Schwelle 80 % gerissen. Jetzt Torzeilen 3, 4 und 5.
```

### V0754 · 22.09.2026 14:56:36 CEST · Hermes-Zwischentext · Nachricht id 11326 · Sitzung `20260921_015554_e79a4a0f` · 150 B

```text
Wichtiger Widerspruch: `eingang` zeigt in **keiner** angenommenen Generation Testfehler — die „3 → 0" aus Gen 8 stimmt so nicht. Ich kläre das.
```

### V0755 · 22.09.2026 14:57:43 CEST · Hermes-Zwischentext · Nachricht id 11330 · Sitzung `20260921_015554_e79a4a0f` · 212 B

```text
Jetzt ist die Herkunft geklärt: Der Kandidat brachte **drei eigene neue Tests** mit, die am unveränderten Code fielen — „3 → 0" ist eine Messung gegen den Kandidatenstand, kein vorher bestehender Schaden.
```

### V0756 · 22.09.2026 14:57:47 CEST · Hermes-Zwischentext · Nachricht id 11332 · Sitzung `20260921_015554_e79a4a0f` · 44 B

```text
Jetzt die Skills, bevor ich veröffentliche.
```

### V0757 · 22.09.2026 14:58:35 CEST · Hermes-Zwischentext · Nachricht id 11338 · Sitzung `20260921_015554_e79a4a0f` · 91 B

```text
Ich habe eine Dublette erzeugt — Zeile 59 und 61 sagen dasselbe. Ich führe sie zusammen.
```

### V0758 · 22.09.2026 14:59:06 CEST · Hermes-Zwischentext · Nachricht id 11342 · Sitzung `20260921_015554_e79a4a0f` · 97 B

```text
Dublette bereinigt, beide Skill-Ergänzungen sitzen. Jetzt der Reviewdurchgang für den Nachtrag.
```

### V0759 · 22.09.2026 14:59:19 CEST · Hermes · Nachricht id 11348 · Sitzung `20260921_015554_e79a4a0f` · 1945 B

```text
Die fünf Torzeilen sind gemessen — das Ergebnis ist unbequem:

**Drei gerissen, eine nicht belegt, zwei gehalten.**

1. **Halluzinationsprobe gerissen.** `zahlen` war sauber — die versiegelten Kriterien nennen dort keine Schwäche. Alle acht Punkte kamen von `security/detect-object-injection`, und die drei Generationen ersetzten `arr[i]` durch `arr.at(i)`: in der Kammer gemessen identisches Verhalten, Tests durchgehend 29/29. Das Kernmaß stieg um 7 Punkte, ohne dass etwas besser wurde.
2. **Versiegelte Schwächen 3 von 5 = 60 %**, Schwelle 80 % gerissen. S1, S2, S4 behoben (S2 deutlich: 25440 → 320 Zugriffe bei n=160), S3 und S5 unverändert offen.
3. **Doppelungsanteil 20 von 57 = 35,1 %**, Schwelle 20 % gerissen. An `aegis._anhaengen` hängt die Maßzeile „Immunisierung 3.10 F3" — 0 von 0 Fällen, für TypeScript nicht belegt, weil der Kern je Angriff eine eigene Datei anlegt.
4. **Kein Rückschritt: 0** über alle sieben angenommenen Generationen. Die drei Testfehler in `eingang` kamen nicht aus dem Werk: Kandidat 2971 brachte drei eigene neue Tests mit, die am unveränderten Code fielen — `statistik()` nahm `NaN` als Gewicht an.
5. **Eichung Lauf 37 bestanden:** 0 Sperren, 4/4 Proben, 4/4 Gegenproben.

**Korrektur übernommen:** „eine Fehlerklasse in zwei Bauarten" erklärt 3 von 11 gescheiterten Läufen (31, 32, 36), nicht alle — 27/28 starben am Rauschen, 29/30/35 an Ausfällen ohne Klärungsweg, 26 an meinem Ablauffehler.

**Skills ergänzt:** In `defect-class-sweep.md` ein Abschnitt, dass die Weiche selbst der Fehler sein kann und eine aus einer Sprache gezogene Musterliste nur die syntaktische Hälfte abdeckt. In `SKILL.md` die zweite Hälfte der Enthaltungsregel: jede Enthaltung zählen, Schwelle vorher setzen, null Fälle sind keine Mehrheit. Dabei hatte ich eine Dublette erzeugt — zusammengeführt.

Nachtrag-Verbrauch **0,00 €** (keine Modellaufrufe). Ein Reviewdurchgang läuft.
```

### V0760 · 22.09.2026 15:15:11 CEST · Philipp · Nachricht id 11434 · Sitzung `20260921_015554_e79a4a0f` · 1579 B

```text
Unbequem gemessen und ohne Abschwächung gemeldet — genau so. Die Halluzinationsprobe hat getan, wofür sie gebaut ist: Sie hat gefangen, dass das Biotop die Messung optimiert statt den Code. Wertung Chat-Claude: T3 nicht abgenommen. Nach Review und Versiegelung von abschluss-02 zuerst die Frage, die das ehrliche Ergebnis bestimmt: Stammen auch die Sicherheitsminderungen in tarife (13 → 9) und planung (2 → 0) aus derselben Regel? Für jede angenommene Sicherheitsminderung: Regel, Codeänderung, Verhalten in der Kammer gleich oder verändert — und daraus das Kernmaß von Lauf 37 ohne die Punkte, die nur den Prüfer zufriedenstellten. Dann drei Kernänderungen in einem Zug: (1) Maßeichung am sauberen Bereich — vor jedem Lauf jede Prüferregel am Vergleichsbereich messen; schlägt eine Regel dort an, wo laut Verfassung keine Schwäche liegt, zählt sie nicht zum Kernmaß — dieselbe Figur wie die Rauschmessung, angewandt auf die Maße selbst, mit Gegenprobe. (2) Doppelungsanteil: die Ursache finden, warum er in TypeScript bei 35 % liegt, wo Python in Vorbedingung 1 auf 9 % kam, und beheben — die Grenze bleibt 20 %. (3) Immunisierungszähler auf den TypeScript-Pfad, dorthin, wo der Kern je Angriff eine Datei anlegt. Dann Lauf 38 mit demselben Werk, denselben versiegelten Schwächen, derselben Verfassung — und ohne jede Änderung am Schwarm oder an seinen Aufgaben, die Wissen über S3 und S5 tragen könnte. Restbudget 4,52 €; reicht es nicht bis zur Sättigung, ist der Budgetabbruch ein zulässiges, dokumentiertes Ende. Ein Reviewdurchgang.
```

### V0761 · 22.09.2026 15:15:51 CEST · Hermes-Zwischentext · Nachricht id 11443 · Sitzung `20260921_015554_e79a4a0f` · 156 B · 2 gleiche Zeilen zusammengefasst

```text
Entscheidender Unterschied: In `tarife` verschwand **`no-new-func`** — das ist S1, die echte versiegelte Schwäche. Ich prüfe den Code und das Verhalten.
```

### V0762 · 22.09.2026 15:15:59 CEST · Hermes-Zwischentext · Nachricht id 11447 · Sitzung `20260921_015554_e79a4a0f` · 181 B · 2 gleiche Zeilen zusammengefasst

```text
Der Grund nennt `tarife.sicherheit_punkte: 13 → 9`, der Diff ändert aber nur `zahlen/geld.ts` — die Tarife-Änderung kam aus der Verhandlung. Ich hole den Anpassungskandidaten.
```

### V0763 · 22.09.2026 15:16:21 CEST · Hermes-Zwischentext · Nachricht id 11449 · Sitzung `20260921_015554_e79a4a0f` · 168 B · 2 gleiche Zeilen zusammengefasst

```text
Das ist der echte Fund: `new Function(...)` wurde durch einen vollständigen Parser ersetzt — S1 wirklich behoben, nicht umformuliert. Jetzt die Kernmaß-Bereinigung.
```

### V0764 · 22.09.2026 15:16:53 CEST · Hermes-Zwischentext · Nachricht id 11453 · Sitzung `20260921_015554_e79a4a0f` · 178 B · 2 gleiche Zeilen zusammengefasst

```text
Das bereinigte Bild ist klarer als das gemeldete: Kernmaß **−11 → 0**, ein vollständiger Gewinn — S1 (10 Punkte) und die tote Funktion S4. Jetzt die drei Kernänderungen.
```

### V0765 · 22.09.2026 15:17:42 CEST · Hermes-Zwischentext · Nachricht id 11459 · Sitzung `20260921_015554_e79a4a0f` · 104 B · 2 gleiche Zeilen zusammengefasst

```text
Maßeichung steht. Jetzt Kernänderung 2 — die Ursache des Doppelungsanteils, bevor ich etwas ändere.
```

### V0766 · 22.09.2026 15:17:56 CEST · Hermes-Zwischentext · Nachricht id 11465 · Sitzung `20260921_015554_e79a4a0f` · 154 B · 2 gleiche Zeilen zusammengefasst

```text
Entscheidender Befund: Python liegt bei **43,5 %**, nicht bei 9 % — TypeScript ist mit 35,1 % sogar *besser*. Die Prämisse der Aufgabe trifft nicht zu.
```

### V0767 · 22.09.2026 15:18:42 CEST · Hermes-Zwischentext · Nachricht id 11481 · Sitzung `20260921_015554_e79a4a0f` · 100 B · 2 gleiche Zeilen zusammengefasst

```text
Null von null auf beiden Seiten — die Zahl steht woanders. Ich halte hier an, statt weiterzuraten.
```

### V0768 · 22.09.2026 15:18:58 CEST · Hermes · Nachricht id 11483 · Sitzung `20260921_015554_e79a4a0f` · 2308 B · 2 gleiche Zeilen zusammengefasst

```text
Ich halte an. Der Doppelungsanteil ist nicht das, wofür ich ihn gehalten habe, und weiterzusuchen hieße raten.

**Zwei der drei Kernänderungen sind fertig, die dritte steht auf einer Prämisse, die die Messung nicht stützt.**

**Befund zur Frage, die das Ergebnis bestimmt — `tarife` und `planung` sind nicht derselbe Fall wie `zahlen`:**

| Bereich | Regel | Codeänderung | Verhalten |
|---|---|---|---|
| zahlen 8→1 | nur `detect-object-injection` | `arr[i]` → `arr.at(i)` | **gleich** (in Kammer gemessen) |
| planung 2→0 | nur `detect-object-injection` | dieselbe Umformung | **gleich** |
| tarife 13→9 | **`no-new-func`, 10 Punkte HIGH** | `new Function(...)` → vollständiger Tokenizer und Parser | **verändert** — S1 echt behoben |

**Kernmaß ohne die Fehlalarm-Regel: −11 → 0.** Gemeldet waren −28 → −14. Von 14 Punkten Gewinn sind **11 echt** (S1 mit 10 Punkten, tote Funktion S4 mit 1) und 3 Fehlalarm-Bereinigung. Das bereinigte Bild ist stärker als das gemeldete: aus −11 wird eine glatte Null.

**Kernänderung 1 fertig:** `biotop/organe/masseichung.py` — jede Prüferregel wird am sauberen Vergleichsbereich gemessen; schlägt sie dort an, zählt sie nicht zum Kernmaß, bleibt aber sichtbar. 6 Tests grün, mit Gegenprobe (eine Regel, die nur außerhalb anschlägt, bleibt in Kraft) und mit Fehler statt Stillschweigen bei falsch benanntem Bereich.

**Kernänderung 2 — die Prämisse trifft nicht zu.** Auf der Ansagen-Ebene liegt Python bei **43,5 %** (10 von 23), TypeScript bei 35,1 % (20 von 57) — TypeScript ist besser, nicht schlechter. Die 9,09 % aus Vorbedingung 1 sind „1 von 11" und messen etwas anderes; in der Aufnahmesperre finde ich in beiden Läufen 0 von 0, das Feld `doppelungen` ist in allen 160 Urteilen leer. Ich kann die Bezugsgröße der 9,09 % nicht belegen und habe keine Ursache gefunden, die zu beheben wäre — eine Änderung wäre hier blind.

**Frage an Sie:** Soll ich die Bezugsgröße der 9,09 % aus Vorbedingung 1 rekonstruieren (kostet Zeit, kein Budget), oder Lauf 38 mit Kernänderung 1 und 3 starten und die Doppelungsfrage offen dokumentieren? Kernänderung 3 (Immunisierungszähler auf den TS-Pfad) baue ich in beiden Fällen.

Restbudget unverändert **4,52 €** — der Nachtrag hat bisher 0,00 € gekostet.
```

### V0769 · 22.09.2026 15:22:14 CEST · Hermes-Zwischentext · Nachricht id 11490 · Sitzung `20260921_015554_e79a4a0f` · 118 B · 2 gleiche Zeilen zusammengefasst

```text
Der Review kippt meine zentrale Schlussfolgerung. Ich prüfe den Cache-Befund selbst nach, bevor ich etwas übernehme.
```

### V0770 · 22.09.2026 15:22:31 CEST · Hermes-Zwischentext · Nachricht id 11492 · Sitzung `20260921_015554_e79a4a0f` · 111 B · 2 gleiche Zeilen zusammengefasst

```text
Bestätigt — ein WeakMap-Cache auf Array-Referenz, der nur die Länge prüft. Ich messe das Verhalten selbst.
```

### V0771 · 22.09.2026 15:22:59 CEST · Hermes-Zwischentext · Nachricht id 11496 · Sitzung `20260921_015554_e79a4a0f` · 160 B · 2 gleiche Zeilen zusammengefasst

```text
Am echten Werk bestätigt: Der Endstand liefert **3 statt 300** und **8 statt 80**. Das ist ein eingebauter Fehler, kein Fehlalarm — und er entstand in Gen 6.
```

### V0772 · 22.09.2026 15:24:15 CEST · Hermes-Zwischentext · Nachricht id 11498 · Sitzung `20260921_015554_e79a4a0f` · 137 B · 2 gleiche Zeilen zusammengefasst

```text
Alle drei schweren Befunde bestätigt. Ich korrigiere den Nachtrag — die Halluzinationsprobe hat mehr gefangen, als ich gemeldet hatte.
```

### V0773 · 22.09.2026 15:25:05 CEST · Hermes · Nachricht id 11504 · Sitzung `20260921_015554_e79a4a0f` · 2420 B · 2 gleiche Zeilen zusammengefasst

```text
**Der Review hat meine zentrale Schlussfolgerung gekippt — zu Recht.**

Ich hatte gemeldet, alle `zahlen`-Änderungen seien folgenlose Umformungen. Das stimmt für Gen 1 und 2. **Gen 6 ist etwas anderes:** Kandidat K2934 baute einen WeakMap-Sortiercache ein, der an der Array-Referenz hängt und nur die Länge prüft. Am echten Werk in der Kammer gemessen, Ausgang gegen Endstand:

| Aufruf nach Mutation desselben Arrays | Ausgang | Endstand | erwartet |
|---|---|---|---|
| `quantil(werte, 1)` | 300 | **3** | 300 |
| `spannweite(werte)` | 80 | **8** | 80 |

Der Lauf hat im sauberen Vergleichsbereich einen **echten Fehler eingebaut** — angenommen für 49 % Laufzeitgewinn, ohne dass ein einziger Test ihn prüft (`zahlen.tests_gesamt` bleibt konstant 29; die von Kandidaten mitgelieferten Testdateien sind im Endstand gar nicht vorhanden). Die Halluzinationsprobe hat also mehr gefangen als gemeldet.

Zehn weitere Befunde übernommen, darunter zwei schwere: Der Nachweis-Hash gehörte zu Lauf 35 statt 37 (`33b75628…`), und „5 neue Tests aus Angriffen" war doppelt falsch — 2 aus Angriffen, 3 aus einem Kandidatendiff.

**Zur Frage aus Ihrer Aufgabe:** `tarife` 13→9 ist **nicht** derselbe Fall. Dort verschwand `no-new-func` (10 Punkte, HIGH) — S1, durch einen vollständigen Parser ersetzt. `planung` 2→0 dagegen ist derselbe Fehlalarm wie `zahlen`. **Kernmaß bereinigt: −11 → 0** statt gemeldet −28 → −14; von 14 Punkten Gewinn sind 11 echt.

**Kernänderung 1 fertig** (`masseichung.py`, 6 Tests mit Gegenprobe). **Kernänderung 2 halte ich an:** Die Prämisse trifft nicht zu — auf der Ansagen-Ebene liegt Python bei 43,5 %, TypeScript bei 35,1 %, also besser. Die 9,09 % aus Vorbedingung 1 („1 von 11") kann ich keiner Bezugsgröße zuordnen; in der Aufnahmesperre finde ich beidseitig 0 von 0. Ohne belegte Ursache wäre jede Änderung blind.

abschluss-02, 23 von 23 Dateien HTTPS-bytegleich:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-02/NACHTRAG-02.md

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-02/DATEIEN.txt

Ordnerprüfsumme: `abd2849e0d6b1c6fa23e2f566de9b2db6fec2bc4d0a78553736bc6be2f059318`

Restbudget **4,52 €**, Nachtrag 0,00 €. Soll ich die 9,09 % rekonstruieren oder Lauf 38 mit Kernänderung 1 und 3 starten?
```

### V0774 · 22.09.2026 15:32:32 CEST · Philipp · Nachricht id 11505 · Sitzung `20260921_015554_e79a4a0f` · 1696 B · 3 gleiche Zeilen zusammengefasst

```text
Der Review-Befund zu K2934 ist der wichtigste des ganzen Projekts — gut, dass du ihn am echten Werk nachgemessen hast, statt ihn zu übernehmen. Entscheidung Chat-Claude: Lauf 38 noch nicht, er hätte keine Abwehr gegen „schneller, aber falsch". Vorher, in einem Zug: (1) Verhaltensvergleich alt gegen neu für jeden Kandidaten — dieselben Eingaben an Vorgeneration und Kandidat, ausdrücklich auch als Folgen (aufrufen, Eingabe an Ort und Stelle ändern, erneut aufrufen) und mit Aliasen; jede Abweichung muss durch einen Test gedeckt sein, den die Vorgeneration nicht besteht und der Kandidat besteht, sonst Ablehnung. Gegenproben aus dem echten Lauf: K2934 muss scheitern, K2868 (S1) und die S2-Beschleunigung müssen bestehen. (2) Doppelungsanteil auf der Ebene, die die Torzeile nennt — erzeugte Angriffstests, geurteilt nach ihrer tatsächlichen Behauptung, nicht nach der Ansage; die 35,1 % sind die Sperrquote des Ansagefilters, eine Diagnose, keine Torzeile, und mein Vergleich mit den 9,09 % war falsch, weil er zwei verschiedene Größen verglich. Such die Berechnung der 9,09 % im Abschlussordner von Vorbedingung 1; findest du sie nicht, miss Lauf 26 mit derselben Methode wie T3 — weicht das Ergebnis ab, ist die Abnahme von Tor 2 Zeile 8 wieder offen, und das gehört so in den Bericht. (3) Aufnahmesperre: null von null in beiden Läufen — prüfe, ob sie überhaupt läuft und auf welchem Pfad; liegt sie wie _anhaengen auf dem Python-Weg, gehört sie zusammen mit dem Immunisierungszähler auf den TypeScript-Pfad. Dann volle Regression, Kern einfrieren, Lauf 38 mit demselben Werk und denselben versiegelten Schwächen. Restbudget 4,52 € hart, ein Reviewdurchgang.
```

### V0775 · 22.09.2026 15:32:58 CEST · Hermes-Zwischentext · Nachricht id 11506 · Sitzung `20260921_015554_e79a4a0f` · 84 B · 2 gleiche Zeilen zusammengefasst

```text
Drei Aufgaben, alle mit Messung vor Änderung. Ich beginne mit den beiden Diagnosen.
```

### V0776 · 22.09.2026 15:33:31 CEST · Hermes-Zwischentext · Nachricht id 11510 · Sitzung `20260921_015554_e79a4a0f` · 195 B · 2 gleiche Zeilen zusammengefasst

```text
Die Aufnahmesperre **läuft** und liegt nicht auf dem Python-Weg: 13 Prüfungen, 14 Tests, **2 gesperrt** in T3. Mein früheres „0 von 0" war ein Auswertungsfehler — ich las das falsche Feld.
```

### V0777 · 22.09.2026 15:33:46 CEST · Hermes-Zwischentext · Nachricht id 11514 · Sitzung `20260921_015554_e79a4a0f` · 91 B · 2 gleiche Zeilen zusammengefasst

```text
**14,29 % — die Torzeile ist eingehalten.** Jetzt die 9,09-Berechnung aus TORZEILEN.json.
```

### V0778 · 22.09.2026 15:33:59 CEST · Hermes-Zwischentext · Nachricht id 11518 · Sitzung `20260921_015554_e79a4a0f` · 145 B · 2 gleiche Zeilen zusammengefasst

```text
Die Methode ist gefunden: Nenner sind **erzeugte Angriffstests**, beurteilt nach ihrer tatsächlich geschriebenen Behauptung. Ich messe T3 damit.
```

### V0779 · 22.09.2026 15:34:41 CEST · Hermes-Zwischentext · Nachricht id 11524 · Sitzung `20260921_015554_e79a4a0f` · 105 B · 2 gleiche Zeilen zusammengefasst

```text
Null erzeugte Angriffstests bei 2 gesperrten — ein Widerspruch. Ich prüfe, wo die Behauptungen stehen.
```

### V0780 · 22.09.2026 15:34:49 CEST · Hermes-Zwischentext · Nachricht id 11526 · Sitzung `20260921_015554_e79a4a0f` · 180 B · 2 gleiche Zeilen zusammengefasst

```text
Gefunden: `behauptungen` wird bei 0 von 210 Urteilen protokolliert, obwohl 42 Angriffe liefen. Die Tor-2-Zeile-8-Zahl ist für T3 **nicht rekonstruierbar** — die Rohdaten fehlen.
```

### V0781 · 22.09.2026 15:35:14 CEST · Hermes-Zwischentext · Nachricht id 11528 · Sitzung `20260921_015554_e79a4a0f` · 204 B · 2 gleiche Zeilen zusammengefasst

```text
Ursache gefunden: `fertig()` schreibt `doppelungen`, aber **nicht** `behauptungen` — das Feld entsteht erst später in der Funktion und landet nie im Protokoll. Ich behebe alle drei Punkte in einem Zug.
```

### V0782 · 22.09.2026 15:36:26 CEST · Hermes-Zwischentext · Nachricht id 11534 · Sitzung `20260921_015554_e79a4a0f` · 94 B · 2 gleiche Zeilen zusammengefasst

```text
Logik steht. Jetzt die Gegenprobe am echten Lauf: K2934 muss scheitern, K2868 und S2 bestehen.
```

### V0783 · 22.09.2026 15:37:14 CEST · Hermes-Zwischentext · Nachricht id 11538 · Sitzung `20260921_015554_e79a4a0f` · 169 B · 2 gleiche Zeilen zusammengefasst

```text
Alle drei Gegenproben bestanden — die Sonde fängt K2934 an vier Stellen, lässt S1 und S2 durch. Jetzt Punkt 3: Behauptungen protokollieren und Immunisierungszähler.
```

### V0784 · 22.09.2026 15:37:29 CEST · Hermes-Zwischentext · Nachricht id 11542 · Sitzung `20260921_015554_e79a4a0f` · 124 B · 2 gleiche Zeilen zusammengefasst

```text
Blockiert — der Befehl wurde als unparsbare Payload abgewiesen. Ich umgehe das nicht, sondern nutze den ausgewiesenen Weg.
```

### V0785 · 22.09.2026 15:37:54 CEST · Hermes-Zwischentext · Nachricht id 11544 · Sitzung `20260921_015554_e79a4a0f` · 131 B · 2 gleiche Zeilen zusammengefasst

```text
`fertig()` ist eine Closure über `urteil` — mein Patch liest die Felder also korrekt zum Aufrufzeitpunkt. Jetzt der Test dafür.
```

### V0786 · 22.09.2026 15:43:02 CEST · Hermes · Nachricht id 11556 · Sitzung `20260921_015554_e79a4a0f` · 1867 B · 2 gleiche Zeilen zusammengefasst

```text
**Alle drei Punkte erledigt, Lauf 38 läuft.**

**(1) Verhaltensvergleich** — die Sonde ruft jede Funktion dreifach: einzeln, nach Mutation derselben Referenz, über ein Alias. Genau das fängt Cache-Fehler, die ein Einzelaufruf nie sieht. Gegenproben **am echten Lauf**, nicht am Fixture:

- **K2934 wird abgelehnt** — 4 von 4 Abweichungen ungedeckt: `quantil@alias` 300→3, `quantil@nach_mutation` 300→3, `spannweite` je 200→2
- **K2868 (S1) besteht** — 0 Abweichungen, `new Function` durch Parser ersetzt
- **S2-Beschleunigung besteht** — 0 Abweichungen, reine Laufzeit

**(2) Tor 2 Zeile 8 — meine 35,1 % waren die falsche Ebene.** Die Berechnung aus Vorbedingung 1 steht in `belege/TORZEILEN.json`: Nenner sind erzeugte Angriffstests, beurteilt nach der **geschriebenen** Behauptung. Mit der Aufnahmesperre C gemessen: **TypeScript 2 von 14 = 14,29 %**, Python 0 von 3 = 0 % — beide unter 20 %, die Torzeile ist eingehalten. Die 35,1 % sind die Sperrquote des Ansagefilters, eine Diagnose.

Für TypeScript war die Zahl bisher gar nicht rekonstruierbar: `aegis.urteil` trug in **0 von 210** Einträgen die geschriebenen Behauptungen, obwohl 42 Angriffe liefen. Ursache war, dass `fertig()` `doppelungen` schrieb, aber nicht `behauptungen` und `aufnahmesperre` — beide stehen jetzt im Protokoll.

**(3) Aufnahmesperre — die Vermutung trifft nicht zu.** Sie liegt nicht auf dem Python-Weg: 13 Prüfungen, 14 Tests, 2 Sperren in Lauf 37. Mein „0 von 0" war ein Auswertungsfehler (falsches Feld gelesen). Kein Umbau nötig, nur Protokollierung.

18 neue Tests, Regression **388 bestanden, 2 übersprungen**. Kern `1cf2eb1`. Verbrauch 5,477 € von 10, Budgetgrenze im Skript auf 9,60 € gesetzt.

Ein Befehl wurde unterwegs als unparsbare Payload blockiert; ich habe ihn über den vom System ausgewiesenen Weg ausgeführt, nicht umformuliert.
```

### V0787 · 22.09.2026 21:26:46 CEST · Hermes-Zwischentext · Nachricht id 11558 · Sitzung `20260921_015554_e79a4a0f` · 145 B · 2 gleiche Zeilen zusammengefasst

```text
Lauf 38 am Budget gestoppt — das vorab genannte zulässige Ende. Jetzt die Abschlussmessung; Modellaufrufe sind ausgeschlossen (0,27 € Rest).
```

### V0788 · 22.09.2026 21:27:06 CEST · Hermes-Zwischentext · Nachricht id 11560 · Sitzung `20260921_015554_e79a4a0f` · 165 B · 2 gleiche Zeilen zusammengefasst

```text
Kernmaß −28 → **−6**, deutlich besser als Lauf 37. Aber zuerst die entscheidende Frage: Wurde der Verhaltensvergleich überhaupt in den Prüfpfad eingehängt?
```

### V0789 · 22.09.2026 21:27:19 CEST · Hermes-Zwischentext · Nachricht id 11562 · Sitzung `20260921_015554_e79a4a0f` · 168 B · 2 gleiche Zeilen zusammengefasst

```text
Gravierender Befund über meine eigene Arbeit: **Beide Module sind gebaut und getestet, aber nirgends eingehängt.** Lauf 38 lief ohne die Abwehr. Ich messe die Folgen.
```

### V0790 · 22.09.2026 21:27:39 CEST · Hermes-Zwischentext · Nachricht id 11564 · Sitzung `20260921_015554_e79a4a0f` · 112 B · 2 gleiche Zeilen zusammengefasst

```text
Teilbefund: `quantil` jetzt korrekt (300), `spannweite` weiterhin falsch (8 statt 80). Ich sehe mir den Code an.
```

### V0791 · 22.09.2026 21:28:01 CEST · Hermes-Zwischentext · Nachricht id 11566 · Sitzung `20260921_015554_e79a4a0f` · 145 B · 2 gleiche Zeilen zusammengefasst

```text
Der Cache ist wieder da — in anderer Form (Modulvariablen statt WeakMap). Ich finde den Urheber und prüfe, ob meine Sonde ihn gefangen hätte.
```

### V0792 · 22.09.2026 21:29:21 CEST · Hermes-Zwischentext · Nachricht id 11572 · Sitzung `20260921_015554_e79a4a0f` · 147 B · 2 gleiche Zeilen zusammengefasst

```text
Belegt: Die Sonde hätte K3121 an vier Stellen abgelehnt. Der Fehler liegt nicht in der Abwehr, sondern darin, dass ich sie nie angeschlossen habe.
```

### V0793 · 22.09.2026 21:29:37 CEST · Hermes · Nachricht id 11574 · Sitzung `20260921_015554_e79a4a0f` · 1933 B · 2 gleiche Zeilen zusammengefasst

```text
**Lauf 38 am Budget beendet — mit einem Befund über meine eigene Arbeit, der schwerer wiegt als das Laufergebnis.**

**Das Ergebnis:** Kernmaß **−28 → −6** (Lauf 37: −14), acht angenommene Generationen, Sicherheitspunkte 27 → 6, tote Funktionen 1 → 0, Testbestand 207 → 213. Alle drei Neutralzähler über der Schwelle. Verbrauch 9,7286 € von 10, Halt bei der gesetzten Grenze — das vorab genannte zulässige Ende.

**Der Befund:** Ich habe `verhaltensvergleich` und `masseichung` gebaut, getestet, committet — und **nie in den Prüfpfad eingehängt**. `grep` findet beide Namen nur in ihren eigenen Moduldateien. Lauf 38 lief ohne die Abwehr.

Die Folge ist messbar: Kandidat **K3121** (Gen 5, „zahlen.laufzeit_ms −66 %") baute denselben Fehlertyp erneut ein — diesmal als Modulvariablen-Cache statt WeakMap. `spannweite` liefert am Endstand nach Mutation desselben Arrays **8 statt 80**.

Nachgeholt gegen die Lazarus-Stände Gen 4 und Gen 5: Die Sonde hätte K3121 **an vier von vier Beobachtungen abgelehnt** (`quantil@nach_mutation` 300→3, `quantil@alias` 300→3, `spannweite` je 200→2). Der Einzelaufruf bleibt in beiden Ständen gleich — nur Folge und Alias zeigen den Fehler, genau wie gebaut.

18 grüne Tests und drei bestandene Gegenproben am echten Lauf 37 haben nicht eine einzige Frage danach gestellt, ob das Modul jemals gerufen wird. Das ist derselbe Fehler, den ich beim Neutralzähler gemacht, behoben und als Regel in `measurement-harness-discipline/SKILL.md` geschrieben habe: *proving a call site can book is not proving the run books*. Ich habe die Regel geschrieben und im selben Auftrag erneut verletzt.

**Restbudget 0,2714 €** — eine Generation kostet im Mittel 0,25 €, ein weiterer Evolutionslauf ist ausgeschlossen. Das Einhängen beider Module ist eine Kernänderung ohne Modellaufrufe; ich kann sie mit Nachweis durchführen, aber nicht mehr im Lauf erproben.
```

### V0794 · 23.09.2026 05:41:59 CEST · Philipp · Nachricht id 11575 · Sitzung `20260921_015554_e79a4a0f` · 1541 B · 2 gleiche Zeilen zusammengefasst

```text
Unbequem und richtig gemeldet — und der Fehler ist auch meiner: Ich habe die Abwehr für wirksam erklärt, weil die Gegenproben gegen das Modul liefen, ohne zu verlangen, dass sie durch den Lauf gehen. Kein weiterer Lauf an T3, die Grenze war hart. Zum Abschluss, ohne Modellaufrufe: (1) verhaltensvergleich und masseichung in den Annahmepfad einhängen. (2) Gegenproben durch genau die Funktion, die ein Lauf zur Annahme ruft, mit den aufgezeichneten Kandidaten und Lazarus-Ständen: K2934 und K3121 müssen abgelehnt werden, K2868 und die S2-Beschleunigung angenommen, und das vom Annahmepfad berechnete Kernmaß darf detect-object-injection nicht mehr zählen. (3) Verdrahtungsnachweis als Regressionstest: Für jedes Organ unter biotop/organe/ belegt ein Nachspiel durch den Annahmepfad, dass es aufgerufen wurde — ein Organ, das existiert und nie gerufen wird, macht die Regression rot. Das ist die Antwort darauf, dass die geschriebene Regel zweimal nicht gereicht hat. (4) Lauf 38 bereinigt auswerten wie Lauf 37: Kernmaß ohne die Fehlalarm-Regel, welche Sicherheitsminderungen bloße Umformungen waren, S1 bis S5 nach „behoben heißt verschwunden", Halluzinationsprobe, Doppelungsanteil mit der Methode aus Vorbedingung 1, Immunisierung auf dem TypeScript-Pfad — und warum der Testbestand in Lauf 38 bei 207 beginnt statt bei 182. (5) Die Blockmeldung „unparsbare Payload" im Wortlaut. Dann Abschlussbericht T3 als abschluss-03: nicht abgenommen, alle Befunde, alle Behebungen mit Nachweis am Laufweg. Ein Reviewdurchgang.
```

### V0795 · 23.09.2026 05:48:08 CEST · Hermes-Zwischentext · Nachricht id 11704 · Sitzung `20260921_015554_e79a4a0f` · 105 B · 2 gleiche Zeilen zusammengefasst

```text
Dieses Mal messe ich alles über den Laufweg selbst. Zuerst lese ich den Code, bevor ich etwas einhänge.
```

### V0796 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11715 · Sitzung `20260921_015554_e79a4a0f` · 118 B

```text
Der Review kippt meine zentrale Schlussfolgerung. Ich prüfe den Cache-Befund selbst nach, bevor ich etwas übernehme.
```

### V0797 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11717 · Sitzung `20260921_015554_e79a4a0f` · 111 B

```text
Bestätigt — ein WeakMap-Cache auf Array-Referenz, der nur die Länge prüft. Ich messe das Verhalten selbst.
```

### V0798 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11721 · Sitzung `20260921_015554_e79a4a0f` · 160 B

```text
Am echten Werk bestätigt: Der Endstand liefert **3 statt 300** und **8 statt 80**. Das ist ein eingebauter Fehler, kein Fehlalarm — und er entstand in Gen 6.
```

### V0799 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11723 · Sitzung `20260921_015554_e79a4a0f` · 137 B

```text
Alle drei schweren Befunde bestätigt. Ich korrigiere den Nachtrag — die Halluzinationsprobe hat mehr gefangen, als ich gemeldet hatte.
```

### V0800 · 23.09.2026 05:50:55 CEST · Hermes · Nachricht id 11729 · Sitzung `20260921_015554_e79a4a0f` · 2420 B

```text
**Der Review hat meine zentrale Schlussfolgerung gekippt — zu Recht.**

Ich hatte gemeldet, alle `zahlen`-Änderungen seien folgenlose Umformungen. Das stimmt für Gen 1 und 2. **Gen 6 ist etwas anderes:** Kandidat K2934 baute einen WeakMap-Sortiercache ein, der an der Array-Referenz hängt und nur die Länge prüft. Am echten Werk in der Kammer gemessen, Ausgang gegen Endstand:

| Aufruf nach Mutation desselben Arrays | Ausgang | Endstand | erwartet |
|---|---|---|---|
| `quantil(werte, 1)` | 300 | **3** | 300 |
| `spannweite(werte)` | 80 | **8** | 80 |

Der Lauf hat im sauberen Vergleichsbereich einen **echten Fehler eingebaut** — angenommen für 49 % Laufzeitgewinn, ohne dass ein einziger Test ihn prüft (`zahlen.tests_gesamt` bleibt konstant 29; die von Kandidaten mitgelieferten Testdateien sind im Endstand gar nicht vorhanden). Die Halluzinationsprobe hat also mehr gefangen als gemeldet.

Zehn weitere Befunde übernommen, darunter zwei schwere: Der Nachweis-Hash gehörte zu Lauf 35 statt 37 (`33b75628…`), und „5 neue Tests aus Angriffen" war doppelt falsch — 2 aus Angriffen, 3 aus einem Kandidatendiff.

**Zur Frage aus Ihrer Aufgabe:** `tarife` 13→9 ist **nicht** derselbe Fall. Dort verschwand `no-new-func` (10 Punkte, HIGH) — S1, durch einen vollständigen Parser ersetzt. `planung` 2→0 dagegen ist derselbe Fehlalarm wie `zahlen`. **Kernmaß bereinigt: −11 → 0** statt gemeldet −28 → −14; von 14 Punkten Gewinn sind 11 echt.

**Kernänderung 1 fertig** (`masseichung.py`, 6 Tests mit Gegenprobe). **Kernänderung 2 halte ich an:** Die Prämisse trifft nicht zu — auf der Ansagen-Ebene liegt Python bei 43,5 %, TypeScript bei 35,1 %, also besser. Die 9,09 % aus Vorbedingung 1 („1 von 11") kann ich keiner Bezugsgröße zuordnen; in der Aufnahmesperre finde ich beidseitig 0 von 0. Ohne belegte Ursache wäre jede Änderung blind.

abschluss-02, 23 von 23 Dateien HTTPS-bytegleich:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-02/NACHTRAG-02.md

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-02/DATEIEN.txt

Ordnerprüfsumme: `abd2849e0d6b1c6fa23e2f566de9b2db6fec2bc4d0a78553736bc6be2f059318`

Restbudget **4,52 €**, Nachtrag 0,00 €. Soll ich die 9,09 % rekonstruieren oder Lauf 38 mit Kernänderung 1 und 3 starten?
```

### V0801 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11731 · Sitzung `20260921_015554_e79a4a0f` · 84 B

```text
Drei Aufgaben, alle mit Messung vor Änderung. Ich beginne mit den beiden Diagnosen.
```

### V0802 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11735 · Sitzung `20260921_015554_e79a4a0f` · 195 B

```text
Die Aufnahmesperre **läuft** und liegt nicht auf dem Python-Weg: 13 Prüfungen, 14 Tests, **2 gesperrt** in T3. Mein früheres „0 von 0" war ein Auswertungsfehler — ich las das falsche Feld.
```

### V0803 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11739 · Sitzung `20260921_015554_e79a4a0f` · 91 B

```text
**14,29 % — die Torzeile ist eingehalten.** Jetzt die 9,09-Berechnung aus TORZEILEN.json.
```

### V0804 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11743 · Sitzung `20260921_015554_e79a4a0f` · 145 B

```text
Die Methode ist gefunden: Nenner sind **erzeugte Angriffstests**, beurteilt nach ihrer tatsächlich geschriebenen Behauptung. Ich messe T3 damit.
```

### V0805 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11749 · Sitzung `20260921_015554_e79a4a0f` · 105 B

```text
Null erzeugte Angriffstests bei 2 gesperrten — ein Widerspruch. Ich prüfe, wo die Behauptungen stehen.
```

### V0806 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11751 · Sitzung `20260921_015554_e79a4a0f` · 180 B

```text
Gefunden: `behauptungen` wird bei 0 von 210 Urteilen protokolliert, obwohl 42 Angriffe liefen. Die Tor-2-Zeile-8-Zahl ist für T3 **nicht rekonstruierbar** — die Rohdaten fehlen.
```

### V0807 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11753 · Sitzung `20260921_015554_e79a4a0f` · 204 B

```text
Ursache gefunden: `fertig()` schreibt `doppelungen`, aber **nicht** `behauptungen` — das Feld entsteht erst später in der Funktion und landet nie im Protokoll. Ich behebe alle drei Punkte in einem Zug.
```

### V0808 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11759 · Sitzung `20260921_015554_e79a4a0f` · 94 B

```text
Logik steht. Jetzt die Gegenprobe am echten Lauf: K2934 muss scheitern, K2868 und S2 bestehen.
```

### V0809 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11763 · Sitzung `20260921_015554_e79a4a0f` · 169 B

```text
Alle drei Gegenproben bestanden — die Sonde fängt K2934 an vier Stellen, lässt S1 und S2 durch. Jetzt Punkt 3: Behauptungen protokollieren und Immunisierungszähler.
```

### V0810 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11767 · Sitzung `20260921_015554_e79a4a0f` · 124 B

```text
Blockiert — der Befehl wurde als unparsbare Payload abgewiesen. Ich umgehe das nicht, sondern nutze den ausgewiesenen Weg.
```

### V0811 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11769 · Sitzung `20260921_015554_e79a4a0f` · 131 B

```text
`fertig()` ist eine Closure über `urteil` — mein Patch liest die Felder also korrekt zum Aufrufzeitpunkt. Jetzt der Test dafür.
```

### V0812 · 23.09.2026 05:50:55 CEST · Hermes · Nachricht id 11781 · Sitzung `20260921_015554_e79a4a0f` · 1867 B

```text
**Alle drei Punkte erledigt, Lauf 38 läuft.**

**(1) Verhaltensvergleich** — die Sonde ruft jede Funktion dreifach: einzeln, nach Mutation derselben Referenz, über ein Alias. Genau das fängt Cache-Fehler, die ein Einzelaufruf nie sieht. Gegenproben **am echten Lauf**, nicht am Fixture:

- **K2934 wird abgelehnt** — 4 von 4 Abweichungen ungedeckt: `quantil@alias` 300→3, `quantil@nach_mutation` 300→3, `spannweite` je 200→2
- **K2868 (S1) besteht** — 0 Abweichungen, `new Function` durch Parser ersetzt
- **S2-Beschleunigung besteht** — 0 Abweichungen, reine Laufzeit

**(2) Tor 2 Zeile 8 — meine 35,1 % waren die falsche Ebene.** Die Berechnung aus Vorbedingung 1 steht in `belege/TORZEILEN.json`: Nenner sind erzeugte Angriffstests, beurteilt nach der **geschriebenen** Behauptung. Mit der Aufnahmesperre C gemessen: **TypeScript 2 von 14 = 14,29 %**, Python 0 von 3 = 0 % — beide unter 20 %, die Torzeile ist eingehalten. Die 35,1 % sind die Sperrquote des Ansagefilters, eine Diagnose.

Für TypeScript war die Zahl bisher gar nicht rekonstruierbar: `aegis.urteil` trug in **0 von 210** Einträgen die geschriebenen Behauptungen, obwohl 42 Angriffe liefen. Ursache war, dass `fertig()` `doppelungen` schrieb, aber nicht `behauptungen` und `aufnahmesperre` — beide stehen jetzt im Protokoll.

**(3) Aufnahmesperre — die Vermutung trifft nicht zu.** Sie liegt nicht auf dem Python-Weg: 13 Prüfungen, 14 Tests, 2 Sperren in Lauf 37. Mein „0 von 0" war ein Auswertungsfehler (falsches Feld gelesen). Kein Umbau nötig, nur Protokollierung.

18 neue Tests, Regression **388 bestanden, 2 übersprungen**. Kern `1cf2eb1`. Verbrauch 5,477 € von 10, Budgetgrenze im Skript auf 9,60 € gesetzt.

Ein Befehl wurde unterwegs als unparsbare Payload blockiert; ich habe ihn über den vom System ausgewiesenen Weg ausgeführt, nicht umformuliert.
```

### V0813 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11783 · Sitzung `20260921_015554_e79a4a0f` · 145 B

```text
Lauf 38 am Budget gestoppt — das vorab genannte zulässige Ende. Jetzt die Abschlussmessung; Modellaufrufe sind ausgeschlossen (0,27 € Rest).
```

### V0814 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11785 · Sitzung `20260921_015554_e79a4a0f` · 165 B

```text
Kernmaß −28 → **−6**, deutlich besser als Lauf 37. Aber zuerst die entscheidende Frage: Wurde der Verhaltensvergleich überhaupt in den Prüfpfad eingehängt?
```

### V0815 · 23.09.2026 05:50:55 CEST · Hermes-Zwischentext · Nachricht id 11787 · Sitzung `20260921_015554_e79a4a0f` · 168 B

```text
Gravierender Befund über meine eigene Arbeit: **Beide Module sind gebaut und getestet, aber nirgends eingehängt.** Lauf 38 lief ohne die Abwehr. Ich messe die Folgen.
```

