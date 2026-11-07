# T3 TypeScript — Nachtrag 02: die fünf fehlenden Torzeilen

Der Abschlussbericht (`abschluss-01`) wurde nicht abgenommen, weil fünf Torzeilen aus
Tor 4 fehlten. Dieser Nachtrag liefert sie aus der vorhandenen Datenbank und den
versiegelten Gegenzeugen — **kein neuer Lauf**, kein Modellaufruf.

Stand: 2026-09-22. Budget für den Nachtrag: 1 € hart, verbraucht: **0,00 €**.

Dieser Text ist nach einem Reviewdurchgang korrigiert. Die Befunde stehen am Ende; einer
davon kippt die ursprüngliche Schlussfolgerung von Abschnitt 1 und ist dort eingearbeitet.

---

## 1. Halluzinationsprobe: `zahlen` — die Probe ist **gerissen**, und zwar doppelt

Die Verfassung nennt `zahlen` als sauberen Vergleichsbereich. Dort meldete der Prüfer
acht Sicherheitspunkte, und drei angenommene Generationen änderten den Bereich.

**Was die drei Generationen tatsächlich änderten:**

| Gen | Kandidat | Zweck laut Annahmegrund | Änderung im Code | Verhalten |
|---|---|---|---|---|
| 1 | K2823 | `zahlen.sicherheit_punkte` 8 → 5 | `arr[i]` → `arr.at(i)`, Index in lokale Variable | **unverändert** |
| 2 | K2847 | `zahlen.sicherheit_punkte` 5 → 1 | dieselbe Umformung an weiteren Stellen | **unverändert** |
| 6 | K2934 | `zahlen.laufzeit_ms` 2,73 → 1,39 ms (−49 %) | **WeakMap-Sortiercache in `geordnet()`** | **verändert — fehlerhaft** |

**Welche Prüferregel sie zufriedenstellten:** bei Gen 1 und 2 ausnahmslos
`security/detect-object-injection` (ESLint, LOW, 1 Punkt je Fund). Alle acht
Ausgangspunkte stammten aus dieser einen Regel. Gen 6 war kein Sicherheits-, sondern ein
Laufzeitkandidat der Nische „schnell".

### Gen 1 und 2: Fehlalarme, folgenlos umgeformt

1. **Die versiegelten Kriterien nennen keine Schwäche in `zahlen`.** S1 und S5 liegen in
   `tarife`, S2 in `planung`, S3 in `eingang`, S4 in `bericht`; der Fixture-Patch berührt
   kein `src/zahlen/`.
2. **Die Regel meldet jeden variablen Index**, unabhängig von der Herkunft. In `zahlen`
   sind alle Indizes Schleifenzähler über eigene, bereits geprüfte Arrays.
3. **Die Umformung ändert kein Verhalten.** In der Kammer gemessen: `a[i]` und `a.at(i)`
   liefern für `i=0`, `i=2` und außerhalb der Grenzen identische Werte; sie unterscheiden
   sich nur bei negativem Index, der in `zahlen` allein in `spannweite()` vorkommt.

Das Kernmaß stieg über Gen 1 und 2 um 7 Punkte, ohne dass etwas besser wurde.

### Gen 6: ein eingebauter Fehler im sauberen Bereich

Kandidat K2934 führte einen `WeakMap`-Cache ein, der sortierte Kopien an der
**Array-Referenz** festmacht und nur die **Länge** gegenprüft. Wird derselbe Array in
place geändert, liefert `geordnet()` das veraltete Ergebnis.

Am **echten Werk** in der Kammer gemessen, Ausgang gegen Endstand:

| Aufruf | Ausgang (ohne Cache) | Endstand (mit Cache) | erwartet |
|---|---|---|---|
| `quantil(werte, 1)` nach Mutation desselben Arrays | **300** | **3** | 300 |
| `spannweite(werte)` nach Mutation | **80** | **8** | 80 |

Der Bereich `zahlen` ist am Endstand also **nicht sauber, sondern fehlerhaft** — und der
Fehler wurde vom Lauf selbst eingebaut, angenommen für einen Laufzeitgewinn von 49 %.

Kein einziger Test im Werk prüft den Cache: `zahlen.tests_gesamt` bleibt über alle sieben
angenommenen Generationen konstant bei 29. Die von den Kandidaten K2847 und K2867
mitgelieferten Testdateien (`test_zahlen_sicherheit_verfassung.test.ts`,
`test_zahlen_verteilen_verfassung.test.ts`) sind im Endstand **nicht vorhanden**. Die
Konstanz „29/29 bestanden" belegt daher nicht, dass die Tests die Änderungen mitgetragen
haben, sondern dass die mitgelieferten Tests nicht ins Werk kamen.

**Urteil: Die Probe ist gerissen.** `zahlen` war nach der Bauakte nicht präpariert — was
laut derselben Bauakte („Schwächenzahl 5 ist kein Beweis anderer Fehlerfreiheit") keine
Zusicherung von Fehlerfreiheit ist. Der Lauf hat dort zuerst acht Fehlalarme folgenlos
wegoptimiert und dann einen echten Fehler eingebaut. Beides ist Optimierung der Messung
statt des Codes; der zweite Fall ist der schwerere.

Belege: `NACHTRAG-1-HALLUZINATION.txt`, `NACHTRAG-1B-FEHLALARM.txt`, `NACHTRAG-5-CACHE.txt`.

---

## 2. Versiegelte Schwächen: **3 von 5 behoben = 60 %, Schwelle 80 % gerissen**

Maßstab „behoben heißt verschwunden": Der versiegelte Gegenzeuge muss am Endstand
`verletzt=false` melden, wo er am Ausgang `true` meldete. Beide Stände in derselben
netzlosen Kammer gemessen.

| ID | Schwäche | Ausgang | Endstand | Urteil |
|---|---|---|---|---|
| S1 | Eingabetextausführung (`new Function`) im Tarifausdruck | verletzt | abgewiesen, Marker 0 | **behoben** |
| S2 | Leistungsbremse O(n²) in der Planung | 1560/6320/25440 Zugriffe | 80/160/320 Zugriffe | **behoben** |
| S3 | Eingabemutation: Quellarray wird sortiert | `[CC,AA,BB]` → `[AA,BB,CC]` | unverändert verletzt | offen |
| S4 | Toter Code in `bericht` | 1 Deklaration | 0 Deklarationen | **behoben** |
| S5 | Inklusive/exklusive Grenze beim Mengenrabatt | `[1000,1000,900]` statt `[1000,900,900]` | unverändert verletzt | offen |

**3 von 5 = 60 %.** Die Torschwelle von 80 % ist **nicht erreicht**.

S1 ist der deutlichste Treffer und keine Umformung: `new Function(...)` wurde durch einen
vollständigen Tokenizer und Parser ersetzt (K2868, Verhandlung zu K2867). S2 fällt von
quadratisch (n=160 → 25440 Zugriffe) auf linear (n=160 → 320).

Belege: `NACHTRAG-2-SCHWAECHEN.txt`, `NACHTRAG-2-SCHWAECHEN.json`.

---

## 3. Doppelungsanteil der Angriffstests: **35,1 %, Schwelle 20 % gerissen**

Dies ist **nicht** der Doppelgänger-Anteil der Vorschläge (0 %, steht in der
Sättigungsmeldung). Gemessen wird, wie oft ein Ankläger eine Behauptung ankündigte, die
im selben Bereich bereits aufgestellt war — der Angriff wird dann ohne Kammerlauf gesperrt.

- Ansagen gesamt: **73**, davon ohne Behauptung („KEIN ANGRIFF"): 16
- Nenner (Ansagen mit Behauptung): **57** — eine Ansage ohne Behauptung kann nicht doppelt
  sein und gehört nicht in den Nenner
- davon Doppelung: **20**
- **Anteil: 20 von 57 = 35,1 %** — Schwelle 20 % **gerissen** (auch bei 20/73 = 27,4 %)

**Einschränkung:** Die Doppelungen verteilen sich sehr ungleich — `tarife` trägt 12 der 20
bei nur 17 Ansagen, `zahlen` 5, `bericht` 2, `planung` 1, `eingang` 0. Der Anteil misst
damit eher die Erschöpfung des `tarife`-Behauptungsraums als eine gleichmäßige Eigenschaft
des Anklägers.

### Welche Torzeile an `aegis._anhaengen` hängt

`_anhaengen` fügt neue Testfunktionen an eine **bestehende** Testdatei an. Daran hängt die
Maßzeile **„Immunisierung: 3.10 F3 (nur bestandene, Doppelungen gekennzeichnet)"**.

Für TypeScript legt der Kern stattdessen je Angriff eine eigene Datei an, sodass
`_anhaengen` nie gerufen wird: **0 von 0 Fällen**. Null Fälle sind keine Mehrheit —
**diese Torzeile ist für TypeScript nicht belegt.**

Tatsächlich ins Werk gelangt sind in Lauf 37 **5 neue Tests**: 2 angriffserzeugte
Immuntests in `tarife` (`aegis_k2840_tarife`, `aegis_k2841_tarife`, Gen 6) und 3 aus dem
Kandidatendiff von K2971 in `eingang` (Gen 8). Der Testbestand steigt entsprechend
440 → 442 → 445.

---

## 4. Kein Rückschritt je angenommener Generation: **0 in den drei Kernmaßfeldern**

Geprüft über alle sieben angenommenen Generationen, je Bereich, für
`tests_fehlgeschlagen`, `sicherheit_punkte` und `tote_funktionen`:

| Gen | Kernmaß | bericht | eingang | planung | tarife | zahlen |
|---|---|---|---|---|---|---|
| 0 | −28 | 4/0/1 | 0/0/0 | 2/0/0 | 13/0/0 | 8/0/0 |
| 1 | −24 | 4/0/0 | 0/0/0 | 2/0/0 | 13/0/0 | 5/0/0 |
| 2 | −20 | 4/0/0 | 0/0/0 | 2/0/0 | 13/0/0 | 1/0/0 |
| 3 | −16 | 4/0/0 | 0/0/0 | 2/0/0 | 9/0/0 | 1/0/0 |
| 5 | −14 | 4/0/0 | 0/0/0 | 0/0/0 | 9/0/0 | 1/0/0 |
| 6 | −14 | 4/0/0 | 0/0/0 | 0/0/0 | 9/0/0 | 1/0/0 |
| 8 | −14 | 4/0/0 | 0/0/0 | 0/0/0 | 9/0/0 | 1/0/0 |

(je Bereich: Sicherheitspunkte / Testfehler / tote Funktionen)

**Einschränkung:** `laufzeit_ms` ist ebenfalls ein Maßfeld — es trägt die Annahmegründe
von Gen 5 und Gen 6 — und wurde hier **nicht** geprüft. Nachgemessen: die Laufzeit steigt
an **11 Stellen** (z. B. Gen 2 → 3 `planung` 9,97 → 11,29 ms). Alle 11 liegen unter der
Rauschtoleranz ihres Bereichs; das größte Verhältnis ist 1,172 bei Toleranz 1,187. Die
Torzeile kippt dadurch nicht, aber „je Maßfeld" war zu weit formuliert.

### Woher die drei fehlschlagenden Tests in `eingang` kamen

**Sie bestanden nie im Werk.** In keiner angenommenen Generation zeigt `eingang` einen
Testfehler — Gen 0 bis 6 durchgehend 133/133, Gen 8 dann 136/136.

Kandidat K2971 lieferte **fünf** Testfunktionen in `test_eingang_statistik_endlichkeit.test.ts`
mit. Davon fielen **drei** am unveränderten Code (`statistik()` akzeptierte `NaN` als
Gewicht); die anderen zwei bestanden bereits an der Vorgeneration und wurden vom Kern
ausdrücklich verworfen („besteht schon an der Vorgeneration — zählt nicht"). Die „3" im
Annahmegrund ist also die Zahl der **fallenden mitgelieferten** Tests, kein vorher
bestehender Schaden im Werk.

---

## 5. Eichung von Lauf 37: **bestanden**

**Rauschmessung:** 0 von 5 Bereichen gesperrt, `lauf_startet: true`.

| Bereich | Toleranz | die fünf Messwerte (ms) |
|---|---|---|
| bericht | 1,150 | 4,01 / 4,16 / 4,17 / 4,18 / 4,64 |
| eingang | 1,187 | 2,34 / 2,75 / 2,86 / 2,99 / 3,08 |
| planung | 1,172 | 9,08 / 9,09 / 9,65 / 9,75 / 11,37 |
| tarife | 1,150 | 11,35 / 11,65 / 11,65 / 11,86 / 12,46 |
| zahlen | 1,150 | 2,83 / 2,85 / 2,87 / 2,91 / 3,10 |

Alle unter der unveränderten Meldeschwelle 1,5.

**Proben: 4 von 4** — nebenwirkung, norm, regression, vertrag, je `ausgefuehrt=true`,
`pruefbar=true`, `bestanden=true`. **Gegenproben: 4 von 4** — dieselben vier, je
`bestanden=false`.

Gesamturteil des Vorspanns: **bestanden**, Nachweis
`33b756282f1dafd8c585e8332f3bb7854a39ba9f86d3e771909d4086fd00c825`.

---

## Kernmaß ohne die Fehlalarm-Regel

Wird `security/detect-object-injection` nicht gezählt — die Regel, die im sauberen
Vergleichsbereich anschlägt, wo die Bauakte keine Schwäche nennt:

| | gemeldet | bereinigt |
|---|---|---|
| Gen 0 | −28 | **−11** |
| Gen 8 | −14 | **0** |
| Gewinn | 14 | **11** |

Von 14 gemeldeten Punkten Gewinn sind **11 echt** (S1 mit 10 Punkten `no-new-func`, tote
Funktion S4 mit 1) und **3 Fehlalarm-Bereinigung**. Das bereinigte Bild ist in der Sache
stärker als das gemeldete — es zeigt aber auch, dass der Lauf für 3 Punkte Arbeit
aufgewendet hat, die nichts verbesserte, und in derselben Datei einen Fehler einbaute.

Beleg: `NACHTRAG-3-KERNMASS.txt`, `NACHTRAG-3-REGELN.txt`.

---

## Korrektur: „eine Fehlerklasse in zwei Bauarten"

Die Formulierung im Abschlussbericht war zu weit. Die elf Läufe starben an **fünf
verschiedenen Ursachen**:

| Ursache | Läufe | Anzahl |
|---|---|---|
| Ablauffehler (Verträge nicht eingelegt) | 26 | 1 |
| Rauschen über der Meldeschwelle | 27, 28 | 2 |
| Anbieterausfall ohne Klärungsweg | 29, 30, 35 | 3 |
| **Fehlerklasse Inhalt-als-Abbruch** | 31, 32, 36 | **3** |
| von mir angehalten (Kernänderung nötig) | 33, 34 | 2 |

Die Fehlerklasse erklärt **3 von 11** gescheiterten Läufen. Sie bleibt der wichtigste
Einzelbefund, weil sie an zwölf Codestellen saß — aber sie war nicht die einzige Ursache.

---

## Zusammenfassung der fünf Torzeilen

| # | Torzeile | Ergebnis | Schwelle | Urteil |
|---|---|---|---|---|
| 1 | Halluzinationsprobe `zahlen` | 8 Fehlalarme folgenlos umgeformt **plus ein eingebauter Cache-Fehler** | sauberer Bereich bleibt unberührt | **gerissen** |
| 2 | Versiegelte Schwächen behoben | 3 von 5 = 60 % | ≥ 80 % | **gerissen** |
| 3 | Doppelungsanteil Angriffstests | 20 von 57 = 35,1 % | ≤ 20 % | **gerissen** |
| 3b | Immunisierung (3.10 F3) an `_anhaengen` | 0 von 0 Fällen | Mehrheit geurteilt | **nicht belegt** |
| 4 | Kein Rückschritt je angenommener Generation | 0 in drei Feldern; Laufzeit steigt 11× unter Rauschtoleranz | 0 | **gehalten, mit Einschränkung** |
| 5 | Eichung Lauf 37 | 0 Sperren, 4/4 Proben, 4/4 Gegenproben | alle | **gehalten** |

Drei Torzeilen gerissen, eine nicht belegt, zwei gehalten.

---

## Reviewdurchgang

Ein Prüfer las den Nachtrag gegen Datenbank, versiegelte Kriterien, beide Werkbäume und
eine eigene Laufzeitprobe, ohne etwas zu ändern. **Elf Befunde, alle nachgemessen und
übernommen:**

| Schwere | Befund | Korrektur |
|---|---|---|
| hoch | Gen 6 war keine folgenlose Umformung, sondern ein WeakMap-Cache, der `quantil` 3 statt 300 liefern lässt | Abschnitt 1 neu geschrieben; ich habe den Befund am echten Werk nachgemessen und bestätigt |
| hoch | Nachweis-Hash gehörte zu Lauf 35, nicht 37 | `33b75628…` statt `0dce3e8f…` |
| hoch | „5 neue Tests aus Angriffen übernommen" — Herkunft und Zahl falsch | 2 aus Angriffen (tarife), 3 aus Kandidatendiff (eingang) |
| mittel | K2971 lieferte fünf Tests, nicht drei — drei davon fielen | unterschieden |
| mittel | „Der Bereich war nach der Bauakte sauber" ist ein Umkehrschluss, den die Bauakte verbietet | umformuliert: nicht präpariert ≠ fehlerfrei |
| mittel | Gen-6-Zeile trug „—" statt des Urhebers K2934 und nannte den Zweck falsch | Kandidat und Laufzeitzweck ergänzt |
| mittel | Testdateien der angenommenen `zahlen`-Kandidaten fehlen im Endstand | ergänzt: „29/29" belegt nicht, was ihm zugeschrieben wurde |
| niedrig | „vier Ursachen" über fünf Tabellenzeilen | fünf |
| niedrig | `laufzeit_ms` als Maßfeld ungeprüft | Einschränkung mit 11 Stellen und Toleranzvergleich ergänzt |
| niedrig | Doppelungsanteil ohne Aufschlüsselung je Bereich | ergänzt |
| niedrig | Zähler `aegis.behauptung` 56 gegen 57 Ansagen unerklärt | offen benannt, siehe unten |

**Offen:** Die Differenz zwischen 57 Ansagen mit Behauptung (Protokoll) und 56 Einträgen
im Neutralzähler ist nicht geklärt. Sie stellt die Torzeile nicht in Frage — bei 56 wie
bei 57 liegt der Anteil geurteilter Fälle über der Hälfte —, zeigt aber, dass zwei Zähler
für dieselbe Größe auseinanderlaufen.

Der erste Befund wiegt am schwersten: Meine ursprüngliche Schlussfolgerung „der Schwarm
behob die Punkte mit einer Umformung ohne Verhaltensänderung" war für zwei von drei
Generationen richtig und für die dritte falsch. Die Halluzinationsprobe hat damit mehr
gefangen, als ich gemeldet hatte.
