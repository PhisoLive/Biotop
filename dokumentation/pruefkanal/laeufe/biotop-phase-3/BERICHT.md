# Phase 3 — Gedächtnis, Mentor, Oberfläche

**Auftraggeber:** Philipp Zöllisch · **Prüfer:** Chat-Claude · **Ausführung:** Hermes
**Grundlage:** INFINITE-EVOLUTION-BIOTOP-Masterprompt **Fassung 4** (19.09.2026), Abschnitt 8 Phase 3
**Budget:** 15 € hart · **verbraucht: 2,83 € (1.225 Modellaufrufe)** — Bezugsgröße: alle Läufe ab 14, gezählt in `kasse`
**Stand:** 19.09.2026

---

## 0. Vorbemerkung zur Belegführung

Jede Zahl in diesem Bericht stammt aus der Datenbank `daten/biotop.db` oder aus einer Datei in `ausgaben/`; die
jeweilige Datei steht in Klammern. Wo ich etwas entschieden habe, steht „**Entscheidung Hermes**". Wo eine Zeile
nicht erfüllt ist, steht das als erster Satz der Zeile, nicht am Ende.

**Drei Dinge vorweg, die den Bericht prägen:**

1. **Fünf Läufe wurden nach Verfassungssatz 2 verworfen** (14, 15, 16, 18, 19). Satz 2 in Fassung 4 lautet: jede
   Messgerätänderung ist ein neuer Lauf. Ich habe während Phase 3 dreimal am Messgerät einen Fehler gefunden und
   korrigiert — jedes Mal endete der laufende Lauf. Das ist kein Unfall, sondern die Regel bei der Arbeit; die
   Gründe stehen einzeln in Abschnitt 6 und je als Protokollzeile `lauf.verworfen` in der Datenbank.
2. **Der tragende Vertrag `bericht→preise` stammt von mir, nicht von Philipp.** Der Vertragstest
   `test_vertrag_bericht_preise::test_katalog_wert_in_eur` (Zusicherung: `Katalog.wert` liefert Grundpreis × Menge in
   EUR) wurde in der Nachprobe zu Zeile 7 von mir geschrieben und vom Biotop unter „VERTRÄGE" angenommen. Er ist die
   Grundlage, an der später der K1165-Fehler als echter Fund erkannt wurde. Philipp hat ihn nicht bestätigt.
   **Entscheidung Hermes, ausdrücklich kennzeichnungspflichtig.**
3. **Die Richtungswahl für beide Übungswerke habe ich getroffen** (Vollmacht Abschnitt 4, Vorgabe Philipp vom
   19.09.2026), je mit Protokollzeile `mentor.gewaehlt`. Der Mentor empfiehlt, gewählt habe ich.

---

## 1. Was gebaut wurde

| Organ | Datei | Wirkung |
|---|---|---|
| Drei Gedächtnisse (3.12) | `biotop/organe/gedaechtnis.py` | Projekt-, Art-, Geschmacksgedächtnis; alle in der Datenbank, alle vor jeder Generation gelesen |
| Mentor (3.4) | `biotop/organe/mentor.py` | 3–5 Richtungen je Lauf, schwerer Aufruf, Verweise mechanisch geprüft |
| Entropie (3.11) | `biotop/organe/entropie.py` | Sättigungsmeldung mit Bezugsgröße; der Lauf endet von selbst |
| Jury (3.5) | `biotop/organe/jury.py` | drei Modelle dreier Hersteller, nur bei Gleichstand aller harten Maße |
| Archivierung (3.10) | `biotop/lauf.py` | offene Funde nach 5 angenommenen Generationen ins Archiv |
| Web-Oberfläche (3.15) | `biotop/oberflaeche.py`, `biotop/dienst.py` | eine Seite hinter der Anmeldung, 18 Bedienelemente, je mit Codestelle |
| Zweites Übungswerk | `/root/uebungswerk2` → `werk/logmuehle-1.0.0.tar.gz` | `logmuehle`, Befehlszeilenwerkzeug für Zugriffsprotokolle, 4 Bereiche, 482 Zeilen, 42 Tests, 3 versiegelte Schwächen |

**Zweites Übungswerk (Entscheidung Hermes):** `logmuehle` liest Zugriffsprotokolle im Common Log Format und wertet
sie aus — Bereiche `lesen`, `filtern`, `zaehlen`, `ausgabe`. Andere Bauart als `lagerhaus` (Dateiverarbeitung und
Befehlszeile statt Bestandsführung). Verfassungsentwurf: `verfassungen/logmuehle.md` — **von mir geschrieben,
Chat-Claude bestätigt am Bericht** (so vom Masterprompt vorgesehen). Drei Schwächen vor dem ersten Lauf versiegelt
(`SCHWAECHEN-logmuehle.md`, Prüfsumme in `ausgaben/02-versiegelt-pruefsummen-vorher.txt`).

---

## 2. Tor 3 — elf Zeilen

### Zeile 1 — Nachprobe Zeile 7 aus Phase 2: **bestanden**
Datei: `ausgaben/14-nachprobe-z7-ergebnis.txt`.
Als echte Generation gelaufen (Lauf 16, Generationen 1–3), nicht als Skript-Simulation. Der Fehler war durch
Ausführung belegt: `bericht.lagerwert` summierte Fremdwährung ungerechnet (100 USD → 100,00 statt 92,59 EUR).
- Fall 1a (Vertragsdatei geändert, Vertrag nicht benannt) → abgelehnt; Fall 1b (ohne Nachbar-Anpassung) → abgelehnt
  an der Regression. **2 von 2 korrekt abgelehnt.**
- Fall 2: K1164 benennt den Vertrag und ändert ihn, der Schwarm des Nachbarn `preise` liefert K1165, das Paar besteht
  (Protokoll #7500), Kernmaß −2 → 0, **Generation 3 angenommen und im Werk** (Lazarus-Tag `lauf16-gen3`,
  103 von 103 Tests grün, `lagerwert` = 192,59). **1 von 1.**
- Diese drei Generationen liefen unter dem damaligen Messgerätstand (Commit `ccb55d2`) und bleiben gültig; Lauf 16
  wurde erst danach verworfen. Sie werden hier als eigener Lauf mit ihrem Messgerätstand ausgewiesen.

### Zeile 2 — Projektgedächtnis: **teilweise belegt, mit offener Differenz**
Datei: `ausgaben/60-tor3-projektgedaechtnis.txt` (gegen Lauf 13), `…-gegen-lauf13.txt` (gegen Lauf 16).
Gefordert: ein zweiter Lauf am ersten Übungswerk wiederholt 0 der im ersten Lauf gescheiterten Wege.
- Im Lauf: **9 Kandidaten** wurden in Lauf 20 vom Projektgedächtnis als Wiederholung erkannt und **ohne Kammerlauf
  verworfen** (Protokollart `gedaechtnis.wiederholung`). Bezugsgröße: 172 Kandidaten des Laufs, davon 48 abgelehnt —
  9 der 48 Ablehnungen kosteten keinen Kammerlauf.
- Meine unabhängige Nachrechnung findet **2 von 187** gescheiterten Wegen aus Lauf 13, die trotzdem ausgeführt wurden
  (K2032 Ähnlichkeit 1,00, K2035 Ähnlichkeit 0,81), und **1 von 44** aus Lauf 16 (K2056, Ähnlichkeit 0,58).
- **Differenz offen und nicht wegerklärt:** Meine Nachrechnung leitet die berührten Funktionen aus den Hunk-Köpfen des
  Diffs ab, das Biotop aus dem tatsächlich angewandten Diff. Die gröbere Ableitung findet mehr Treffer. Die Zeile
  verlangt „0 Wiederholungen"; gemessen sind es je nach Ableitung 0 (Biotop-Sicht: alle erkannten wurden verworfen)
  oder 2 von 187 (meine Sicht). **Ich werte die Zeile nicht als voll erfüllt.**

### Zeile 3 — Artgedächtnis: **nicht erfüllt**
Dateien: `ausgaben/81-mentor-lauf18.json`, `90-mentor-lauf19.json`, `100-mentor-lauf20.json`.
Gefordert: Nach Läufen an beiden Übungswerken verweist der Mentor bei einem dritten Lauf ausdrücklich auf einen
Eintrag des Artgedächtnisses (Eintrag benannt).
- Gemessen, in drei aufeinanderfolgenden Läufen nach beiden Werken: **0 werkübergreifende Verweise** von
  4 bzw. 4 bzw. 4 Richtungen. Verweise auf das **eigene** Werk (= Projektgedächtnis, nach Vorgabe Philipp getrennt
  gezählt): 10 (Lauf 18), 4 (Lauf 19), 9 (Lauf 20). **Erfundene Kennungen: 0** in allen drei Läufen.
- Das Artgedächtnis ist gefüllt und wird dem Mentor vorgelegt: 89 Einträge aus `logmuehle`, davon 5 angenommene;
  der Block „ANDERE WERKE" enthält 25 Einträge, angenommene zuerst (das habe ich nach dem ersten Fehlschlag
  umgestellt, weil zuvor nur Ablehnungen im Fenster standen — die Umstellung hat nichts geändert).
- **Befund:** Das Modell zitiert konsequent die Einträge des eigenen Werks, weil sie konkreter passen. Die Zeile
  misst eine Modelleigenschaft, nicht eine Mechanik. Für Fassung 5 vorgeschlagen: entweder den werkübergreifenden
  Verweis erzwingen (Pflichtfeld mit Mindestanzahl) oder die Zeile auf „das Artgedächtnis wird nachweislich
  vorgelegt und enthält Einträge anderer Werke" umstellen.

### Zeile 4 — Mentor: **erfüllt**
Dateien: `ausgaben/40-mentor-lauf16.json`, `81-`, `90-`, `100-`, Richtungen in `41-`, `82-`, `91-`, `101-`.
Fünf Mentor-Aufrufe (Läufe 16, 17, 18, 19, 20), je **4 bis 5 Richtungen** — gefordert sind ≥ 3 je Werk.
Pflichtfelder (Ertrag, Risiko, Aufwand in Generationen, berührte Bereiche) mechanisch geprüft: **in allen Richtungen
aller fünf Aufrufe vollständig** (`pruefung.pflichtfelder_ok` je Richtung `true`). Schwerer Aufruf
(`anthropic/claude-sonnet-5`): 24 Aufrufe, 0,74 € — das ist der größte Einzelposten der Phase.

### Zeile 5 — Entropie / Sättigung: **erfüllt**
Dateien: `ausgaben/63-entropie-lauf20.json`, `63-entropie-lauf17.json`.
- `lagerhaus` (Lauf 20, Kernmaß 0 = Höchstwert): Sättigungsmeldung **nach Generation 5** (gefordert: spätestens
  nach 6) — „Generationen 1–5, Verbesserung 0,00 % (Schwelle 0,5 %), Kernmaß 0 = Höchstwert, Doppelgänger-Anteil
  12 %. Weiter nur mit anderer Richtung — zurück zum Mentor." Der Lauf hat sich daraufhin **selbst beendet**
  (Status `gesaettigt`), der Läufer brach ab.
- `logmuehle` (Lauf 17): Sättigung nach Generation 8, Fenster 4–8, Verbesserung 0,00 %, Doppelgänger 9 %.

### Zeile 6 — Jury: **zur Hälfte belegt**
Dateien: `ausgaben/61-tor3-jury.txt`, `95-tor3-jury-uneinig2.txt`, `96-tor3-jury-mechanik.txt`.
- **Einstimmiger Fall mit drei Begründungen: belegt, 3 Fälle aus echten Läufen** (Lauf 17 Gen 2 `zaehlen`,
  Lauf 17 Gen 3 `filtern`, Lauf 20 Gen 1 `preise`), je drei Juroren dreier Hersteller (openai, google, deepseek),
  je drei ausformulierte Begründungen im Protokoll.
- **Fall ohne Einstimmigkeit: nicht mit echtem Dissens belegt.** Ich habe zwei Proben mit absichtlichem
  Zielkonflikt gestellt (kurz+dicht gegen lang+explizit; Kürze gegen Fehlermeldungsqualität) — **5 von 5 Fällen
  einstimmig**. Die Mechanik habe ich danach mit einer **gestellten Gegenstimme** geprüft: Ergebnis
  `einstimmig: false`, `gewinner: None` — kein Urteil, protokolliert (#12361). **Ausdrücklich gekennzeichnet:
  gestellte Uneinigkeit, kein echter Modelldissens.**

### Zeile 7 — Geschmacksgedächtnis (Mechanikprüfung): **erfüllt**
Dateien: `ausgaben/21-tor3-geschmack.txt`, versiegelte Regel `GESCHMACK-regel-P1.md`
(Prüfsumme `eed64ca5…` in `02-versiegelt-pruefsummen-vorher.txt`, vor dem Lauf hinterlegt).
30 Entscheidungen nach der versiegelten Regel P1 an echten Kandidaten aus Lauf 13 erzeugt, aus den ersten 20 gelernt,
von den restlichen 10 **10 richtig vorhergesagt** (gefordert: ≥ 7).
**Ausdrücklich: Mechanikprüfung, kein Nachweis über Philipps Geschmack** — Philipps echte Entscheidungen gibt es
erst ab Phase 4.

### Zeile 8 — Archivierung: **nicht eingetreten, Mechanik ungeprüft**
Datei: `ausgaben/62-tor3-archivierung.txt`.
Gefordert: offene Funde nach 5 Generationen archiviert (Zahl archiviert / gesamt), 0 archivierte Funde in
Kammerläufen danach.
- Gemessen: **0 Archivierungen** in allen Phase-3-Läufen. Grund, nachgeprüft: kein offener Fund hat fünf
  **angenommene** Generationen erlebt — Lauf 20 hatte 1 angenommene Generation, Lauf 17 deren 5, aber der einzige
  echte Fund (K1165) wurde in Lauf 20 Generation 1 sofort behoben.
- Die Zeile ist damit **nicht belegt**; ich habe sie nicht künstlich herbeigeführt.

### Zeile 9 — Oberfläche: **erfüllt**
Dateien: `ausgaben/70-tor3-oberflaeche.txt`, `70-tor3-oberflaeche-belege.json`.
- **18 von 18 Routen** ohne Token → HTTP 401 (vollständige Liste mit Ergebnis je Route).
- **18 von 18 Bedienelemente** mit Dateipfad **und Zeilennummer** der Stelle, die sie lesen oder schreiben
  (z. B. `kosten-stand → GET /laeufe/<id>/kasse → biotop/kern/kasse.py:31`). Kein Element ohne Stelle.
- Kostenstand und Verlaufskurve über die Routen sichtbar, nach Anmeldung mit Token geprüft.

### Zeile 10 — Kandidatenaufschlüsselung geht auf: **erfüllt**
Datei: `ausgaben/65-tor3-zerlegungen.txt`, dazu `00-lauf13-zerlegung-470.txt` für Phase 2.
- Lauf 20: **172 = 48 abgelehnt + 1 angenommen + 3 erzeugt + 107 leer + 4 probe + 5 überlebt + 4 verhandlung** → geht auf.
  Ablehnungen 48 = 10 Kernmaß unverändert + 10 Diff nicht anwendbar + 9 Pareto/Regression + 9 Wiederholung +
  5 Grenzmaß + 3 sonst + 2 Nische schnell ohne Gewinn.
- Lauf 17: **245 = 69 + 5 + 3 + 156 + 11 + 1** → geht auf. Ablehnungen 69 = 27 Diff nicht anwendbar +
  16 Wiederholung + 9 Kernmaß unverändert + 8 Nische schnell + 5 Pareto/Regression + 2 sonst + 2 Grenzmaß.
- Kategorien unverändert aus dem Phase-2-Bericht übernommen, keine Umschnitte (Vorgabe Philipp).
- Phase 2, Lauf 13: 470 geht auf; die zuvor fehlende Eins ist K1159, eine zweite, nie geprüfte Verhandlungs-Anpassung.

### Zeile 11 — Verlaufskurven beider Werke: **erfüllt**
Dateien: `ausgaben/kurve-lagerhaus.svg` / `.txt`, `ausgaben/kurve-logmuehle.svg` / `.txt`.

`logmuehle` (Lauf 17), Kernmaß F2 und Endtestbestand:

| Punkt | Kernmaß | Tests | ausgabe | filtern | lesen | zaehlen |
|---|---|---|---|---|---|---|
| L17G0 | −13 | 56 | 15,34 | 31,16 | 27,88 | 15,40 |
| L17G2 | −2 | 61 | 14,62 | 29,02 | 27,64 | 15,49 |
| L17G3 | 0 | 61 | 14,89 | 29,19 | 32,66 | 15,17 |
| L17G4 | 0 | 62 | 14,93 | 29,24 | 28,73 | 15,48 |
| L17G5 | 0 | 62 | 10,25 | 24,71 | 14,83 | 11,00 |

`lagerhaus` (Läufe 16, 18, 19, 20 — verworfene Läufe als solche markiert, weil ihr Schnappschuss jeweils Ausgang des
nächsten Laufs war): Kernmaß F2 durchgehend 0 (Höchstwert seit Phase 2), Tests 101 → **104**,
Laufzeiten `formeln` 132,28 → **1,26 ms** (−99 %), `preise` 91,58 → **12,89 ms** (−86 %), `bericht` 6,65 → 7,72,
`lager` 5,06 → 5,13.

---

## 3. Das zweite Übungswerk und seine drei versiegelten Schwächen

Vor dem ersten Lauf versiegelt (`SCHWAECHEN-logmuehle.md`), Prüfsumme vorher hinterlegt:

| Schwäche | Erwartung | Gemessen |
|---|---|---|
| W1 `filtern/extern.py`: Befehl über die Shell zusammengebaut | Sicherheitsbefund, muss verschwinden | **behoben**, Lauf 17 Gen 2/3: `filtern.sicherheit_punkte` **11 → 0**. Gemessen (`ausgaben/97-…`): im Endstand weder `shell=True` noch `subprocess.run` — das Werk hat den Subprozess **ganz entfernt** und einfache `grep`-Muster intern in Python nachgebildet, komplexe Befehle werden abgelehnt. Anders gelöst als von mir erwartet, aber am Maß gemessen besser |
| W2 `zaehlen/kennzahlen.py`: `perzentil` falsch an der Kante | Testfehlschlag, muss auf 0 | **behoben**, Lauf 17 Gen 2, `filtern.tests_fehlgeschlagen` 1 → 0; Endstand **62 von 62 Tests grün** |
| W3 `zaehlen/kennzahlen.py::_median_alt`: tote Funktion | tote Funktion, muss auf 0 | **behoben**, Lauf 17 Gen 2, `zaehlen.tote_funktionen` 1 → 0; `_median_alt` im Endstand nicht mehr vorhanden |

Alle drei Zeilen einzeln nachgemessen in `ausgaben/97-schwaechen-logmuehle-geprueft.txt` (Ausgang gegen Endstand,
mit Kammerlauf). **Korrektur an meiner eigenen Erwartung:** Der Testfehlschlag der versiegelten Schwäche W2 lag
gemessen im Bereich `filtern`, nicht in `zaehlen` — die Versiegelung hatte ihn `zaehlen` zugeordnet. Die
Schwäche selbst (`perzentil` an der Kante) wurde behoben, meine Bereichszuordnung in der Versiegelung war falsch.

**Generation 0 an `logmuehle`** (`ausgaben/35-generation0.json`): 42 Mutanten gesetzt, **0 äquivalente**,
**42 von 42 nicht-äquivalenten gefangen** (Ziel war 34), 0 zusätzliche Testrunden nötig — der mitgelieferte
Testbestand fing alle. Kernmaß-Ausgang: `filtern` −12, `zaehlen` −1, Summe −13 → am Ende **0 in allen vier Bereichen**.

---

## 4. Satz 7 — der Fund K1165 und wie er behoben wurde

In der Nachprobe zu Zeile 7 fiel mir auf, dass die dort angenommene Anpassung K1165 den **Staffelpreis** statt des
**Grundpreises** für die Bestandsbewertung verwendet — der Vertragstest hatte keinen Staffelfall. Nach Satz 7 („jeder
gefundene Fehler wird zu einem Test") habe ich den Fehler nicht vertagt, sondern als Immuntest ins Immunsystem gelegt
(`hermes_k1165_wert_grundpreis`, nennt den Vertrag ausdrücklich, fällt am Werk).

Der Weg zur Behebung führte durch zwei Messgerät-Fehler (Abschnitt 6). Behoben in **Lauf 20, Generation 1**:
`Katalog.wert` rechnet jetzt `artikel.grundpreis * menge`, `preise.tests_fehlgeschlagen` 1 → 0, der Immuntest liegt
im Werk (`tests/test_preise_immun_hermes_k1165_wert_grundpreis_w18.py`), Fund-Status `im_werk`,
**104 von 104 Tests grün** in der Kammer.

---

## 5. Befund: Die Doppelungserkennung erkennt die falsche Gleichheit

Datei: `ausgaben/94-befund-doppelungen.txt`. **Korrektur erst in Fassung 5** (Vorgabe Philipp) — der Code ist
unverändert.

Sechs Ankläger-Tests desselben Werks (K1191, K1195, K1200, K1201, K1296, K1374) behaupten dieselbe Sache über
dieselbe Funktion: `Katalog.wert` liefere den Staffelpreis. Sie kamen **einzeln** ins Immunsystem, weil die
Doppelungserkennung (3.10) als Schlüssel **(Meldungsklasse, Ort)** verwendet: alle melden `AssertionError`, aber
jeder in einer anderen Zeile seiner eigenen Testdatei — also nie „derselbe Ort". Die Regel meint die **Behauptung**,
geprüft wird die **Fundstelle**.

**Doppelungsanteil Lauf 13 (Phase 2) neu gerechnet** — Bezugsgröße 55 vom Ankläger erzeugte Tests
(49 aufgenommen + 6 verworfen):

| Lesart | Doppelungen | Anteil |
|---|---|---|
| gemeldet (Meldungsklasse+Ort), Bezug 240 Ablehnungen | 6 | **2,5 %** ← so stand es im Phase-2-Bericht |
| gemeldet, Bezug 55 erzeugte Tests | 6 | **10,9 %** |
| Lesart A (Ziel-Funktion + Zahlenwert) | 6 + 21 | **49,1 %** |
| Lesart B (Ziel-Funktion, = „gleiche Behauptung, gleiche Stelle") | 6 + 40 | **83,6 %** |

**Eigener Fehler, benannt:** Die 2,5 % im Phase-2-Bericht waren gegen die 240 Ablehnungen des Laufs gerechnet, nicht
gegen die erzeugten Tests. Das war eine irreführende Bezugsgröße; richtig sind 10,9 % bei gleicher Lesart.
Lesart A und B sind meine Auslegungen der Regel — die Regel selbst nennt nur „gleiche Ausnahme/Zusicherung an
derselben Stelle".

---

## 6. Was schiefging — drei Messgerät-Fehler, fünf verworfene Läufe

Alle fünf mit Protokollzeile `lauf.verworfen` in der Datenbank.

**Lauf 14** — Messgerät während des Laufs geändert. **Lauf 15** — Ankläger-Ablauf während des Laufs geändert
(Nachprobe Zeile 7). Beide vor jeder gemessenen Generation, ohne Ertrag.

**Lauf 16 — Ankläger schrieb den Fehler als Norm fest.** Der Ankläger erzeugte an K1191 einen Test, der
`Katalog.wert == Staffelpreis` behauptet — also genau den K1165-Fehler als Norm. Weil der Test *am Kandidaten* fiel,
wurde er als **Fund** gebucht und tötete anschließend jede Behebung per Pareto je Test (Generation 4 und 6: sechs
Behebungsversuche, alle an „Regression je Test" gescheitert). Regel F4 3.7 sagt „jeder neue Test", mein Ankläger
prüfte den Vertragsverweis aber nur bei Tests, die an der *Vorgeneration* fallen.
**Korrektur** (Wortlaut Philipp): Pareto je Test gilt für Tests im Werk, Verträge und Verfassung; ein neuer
Angriffstest, der an der Vorgeneration besteht und am Kandidaten fällt, tötet nur bei Absturz des Kandidaten oder bei
explizitem Vertrags-/Verfassungsverweis, sonst offen, 0 Punkte, kein Kill. K1191 auf `offen_norm` zurückgestuft.

**Lauf 18 — das Projektgedächtnis zitierte einen verworfenen Lauf.** In Generation 2 und 3 wurden **12 von 13**
Wiederholungs-Verwerfungen mit Verweis auf Lauf 16 begründet — also auf Ablehnungen, die ein als falsch erkannter
Ankläger erzeugt hatte. Das Projektgedächtnis ist Teil des Messgeräts: es verwirft Kandidaten ohne Kammerlauf.
**Korrektur:** gescheiterte Wege aus verworfenen Läufen zählen nicht mehr.

**Lauf 19 — sechs Normtests standen als Funde im Testbestand.** Beim Übertragen der offenen Funde aus den verworfenen
Läufen hatte ich die alten Stati blind mitgenommen. Ich habe daraufhin **alle** offenen Funde mechanisch in der
Kammer nachgemessen (`ausgaben/93-funde-neubewertung-werk17.txt`): **6 von 7** bestehen am Werk, stürzen nicht ab und
nennen keinen Vertrag → Norm. Nur K1165 fällt am Werk und nennt den Vertrag → echter Fund. Damit änderte sich der
gemessene Testbestand — Satz 2, neuer Lauf. In **Lauf 20** fiel der Fehler dann in der ersten Generation.

**Vierter Fehler, ohne Messwirkung:** `protokoll.schreiben` bekam in `gedaechtnis.wiederholung` den Schlüssel
`lauf_id` doppelt und brach Generation 5 von Lauf 16 ab (reine Protokollierung, kein Maß berührt; korrigiert,
Generation neu begonnen, protokolliert als `biotop.korrektur`).

**Nebenbefund aus der Rauschprobe** (`ausgaben/92-rauschprobe-lauf19.txt`): Fünf Messungen am unveränderten Werk
ergaben für `bericht.laufzeit_ms` 7,90–8,46 ms — die in Lauf 19 abgelehnten 12,10 und 14,78 ms waren also echte
Verschlechterung, das Grenzmaß arbeitete richtig. **Aber:** `formeln` rauschte im selben Versuch 1,66–2,44 ms, also
**47 %** bei einer Toleranz von 15 %. Bei kurzen Laufzeiten ist die feste Toleranz zu eng — für Fassung 5.

---

## 7. Kosten

| Lauf | Aufrufe | € |
|---|---|---|
| 14 (verworfen) | 17 | 0,0035 |
| 15 (verworfen) | 28 | 0,0119 |
| 16 (verworfen, enthält Nachprobe Z7) | 263 | 0,5963 |
| 17 (`logmuehle`, gesättigt) | 310 | 0,9949 |
| 18 (verworfen) | 154 | 0,3398 |
| 19 (verworfen) | 220 | 0,4575 |
| 20 (`lagerhaus`, gesättigt) | 233 | 0,4231 |
| **Summe ab Lauf 14** | **1.225** | **2,8269** |

Budget 15 € — **18,8 % verbraucht**. Schwere Aufrufe (`anthropic/claude-sonnet-5`): 24 Aufrufe, 0,739 €. Davon
**15 der Ankläger im Bereich `filtern`** (0,419 €, Sicherheitsbefund an `logmuehle` — Eskalation nach 3.7) und
**9 der Mentor** (0,320 €). Die verworfenen Läufe kosteten zusammen 1,41 €, also die Hälfte der Phase; das ist der
Preis von Satz 2. Modellanteile: gemini-3.5-flash-lite 0,895 €, sonnet-5 0,739 €, gpt-5.6-luna 0,483 €,
deepseek-v4.1-flash 0,377 €, qwen3.8-flash 0,311 €, gemini-3.1-flash-lite 0,023 € (Vollständiges Blatt: `KASSE.md`).

---

## 8. Für Fassung 5

1. **Doppelungserkennung**: Schlüssel muss die Behauptung sein (Ziel-Funktion + Zusicherung), nicht
   (Meldungsklasse, Ort). Siehe Abschnitt 5 — betrifft rückwirkend die Zahlen aus Phase 2.
2. **Grenzmaß-Toleranz bei kurzen Laufzeiten**: 15 % feste Toleranz ist zu eng, wenn das Eigenrauschen 47 % beträgt.
   Vorschlag: Toleranz aus einer Rauschmessung des Ausgangs ableiten statt fest zu setzen.
3. **Artgedächtnis-Zeile** (Tor 3): misst derzeit eine Modelleigenschaft, nicht eine Mechanik — entweder Pflichtfeld
   mit Mindestanzahl werkübergreifender Verweise oder Zeile umformulieren.
4. **Jury-Zeile**: „ein Fall ohne Einstimmigkeit" ist nicht erzwingbar, wenn die Juroren einig sind (5 von 5 einstimmig,
   auch bei gestelltem Zielkonflikt). Vorschlag: Mechanikprüfung ausdrücklich zulassen, wie bei Zeile 7.
5. **Archivierungs-Zeile**: setzt 5 angenommene Generationen mit durchgehend offenem Fund voraus — an einem
   gesättigten Werk tritt das nicht ein. Vorschlag: Bezug auf Generationen statt auf angenommene Generationen.
6. **Fund-Übernahme zwischen Läufen desselben Werks** sollte die Norm-Prüfung mechanisch wiederholen, statt den
   alten Status zu übernehmen (das war mein Fehler in Lauf 19, jetzt als Skript `pruefung/funde_neubewerten.py`
   vorhanden, aber nicht im Lauf verdrahtet).

---

## 9. Offene Punkte

- **Zeile 3 (Artgedächtnis) nicht erfüllt**, Zeile 2 (Projektgedächtnis) mit offener Differenz, Zeile 6 (Jury) nur
  zur Hälfte mit echtem Dissens, Zeile 8 (Archivierung) nicht eingetreten. **Gewertet: 7 von 11 voll, 2 teilweise,
  2 nicht belegt.**
- Der Verfassungsentwurf für `logmuehle` wartet auf Chat-Claudes Bestätigung am Bericht.
- `pruefung/funde_neubewerten.py` ist ein Prüfskript, kein Organ — die Neubewertung läuft nicht automatisch.
- Die zweite Verhandlungs-Anpassung K1159 aus Lauf 13 wurde nie geprüft (Phase-2-Altlast, unverändert offen).

---

## 10. Dateien

`ausgaben/` — 167 Rohausgaben, Präfixe: `0x` Vorbereitung und Versiegelung, `1x` Nachprobe Zeile 7, `2x`
Geschmacksgedächtnis, `3x` Aufnahme `logmuehle`, `4x`–`10x` Mentor/Richtungen/Generationen je Lauf, `6x` Tor-3-Zeilen,
`7x` Oberfläche, `9x` Befunde und Proben, `kurve-*` Verlaufskurven.
`werk/` — beide Übungswerke als Archiv (ohne `.env*`, `node_modules`, `dist`, `coverage`).
`biotop/` — der Stand des Biotops zum Berichtszeitpunkt.
`DATEIEN.txt` — vollständige Liste mit Prüfsumme je Datei.
