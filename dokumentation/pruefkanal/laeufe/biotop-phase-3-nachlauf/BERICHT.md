# Nachlauf zu Phase 3

**Auftraggeber:** Philipp Zöllisch · **Prüfer:** Chat-Claude · **Ausführung:** Hermes
**Grundlage:** INFINITE-EVOLUTION-BIOTOP-Masterprompt **Fassung 5** (19.09.2026), Abschnitt 8 „Nachlauf zu Phase 3"
**Budget:** 10 € hart · **verbraucht: 0,44 € (207 Modellaufrufe)** — Bezugsgröße: alle Läufe ab 21
**Stand:** 19.09.2026

---

## 0. Auftrag und Ergebnis in Kurzform

Neun Punkte, in der von Philipp gesetzten Reihenfolge. Alle neun abgearbeitet:

| # | Punkt | Ergebnis |
|---|---|---|
| 1 | Vier Eichproben am versiegelten Gegenstand | gebaut, 4 von 4 bestanden |
| 2 | Fund-Neubewertung als Organ | gebaut, 3 Fälle belegt |
| 3 | Gate-Ausnahme für Abbrüche | als **benannter Befehl** gebaut, 5 Fälle belegt |
| 4 | Doppelungsschlüssel auf die Behauptung, Tor 2 Zeile 8 neu messen | gebaut; **Zeile 8 bleibt gerissen** (68,5 % / 54,5 % gegen Grenze 20 %) |
| 5 | Artgedächtnis auf Muster, Torzeile erneut messen | gebaut; **Torzeile erfüllt** (2 von 5 Richtungen) |
| 6 | Archivierung nach der neuen Zeile | gebaut, Mechanikprüfung belegt |
| 7 | Projektgedächtnis-Differenz entscheiden | **0 von 3 Fällen durchgerutscht** — meine Nachrechnung war falsch |
| 8 | `logmuehle`-Verfassungsentwurf abdrucken | Abschnitt 9 dieses Berichts |
| 9 | Vier Tor-2-Probenzeilen nachmessen | **4 von 4 bestanden** |

Dazu vorgezogen (Festlegungen von Chat-Claude während der Arbeit): Median-Laufzeiten, gemessene
Rauschtoleranz mit bereichsweiser Sperre, Streuungsregel als Kernfunktion, versiegelter Eichgegenstand,
Probensperre für alle drei Gedächtnisse.

---

## 1. Was gebaut wurde

| Organ / Änderung | Datei | Wirkung |
|---|---|---|
| Generation minus eins, Teil 1 | `organe/eichung.py` | Rauschmessung je Bereich, bereichsweise Sperre, Aussetzer-Nachmessung, Serienzähler mit Zeitraum-Deutung, getrennte Eichkosten |
| Generation minus eins, Teil 2 | `organe/eichproben.py` | die vier Proben, mechanisch über den Syntaxbaum, Abrechnung je Probe |
| Versiegelter Eichgegenstand | `organe/eichgegenstand.py` | je Werk einmal gewählt, Verfassung vor Vertragsgröße, Befund bei Wegfall |
| Fund-Neubewertung | `organe/fundpruefung.py` | offene Funde am neuen Ausgang nachmessen, Übernahme erzwingt Neubewertung |
| Abbruch | `lauf.abbrechen`, CLI `biotop abbrechen`, `POST /laeufe/<id>/abbrechen` | Pflicht statt Freigabe, immer protokolliert |
| Doppelungsschlüssel | `aegis.behauptung` | Ziel-Funktion + Zusicherungsart aus dem Syntaxbaum |
| Ankläger-Vielfalt | `aegis.bisherige_behauptungen` | bisherige Behauptungen werden vor jedem Angriff vorgelegt |
| Artgedächtnis-Muster | `gedaechtnis.muster_bilden`, `art_text` | werkübergreifend nur abstrahierte Sätze |
| Median-Laufzeit, Streuungsregel | `kern/messgeraet.py` | Median aus drei Durchläufen; `streuung()` wirft bei falscher Ebene |
| Probensperre | `gedaechtnis.ist_probe` | am Merkmal `kandidaten.ist_probe`, nicht am Namen |
| Archivierung | `lauf.py` | Bezug sind Generationen, nicht angenommene Generationen |

---

## 2. Punkt 1 und 9 — die vier Eichproben, zugleich Nachmessung der Tor-2-Zeilen

Beleg: `ausgaben/10-eichproben-vorspann.txt`, `15-vorspann-lauf22.txt`.

Die Proben setzen am versiegelten Eichgegenstand an (`bericht→preise`, Vertrag
`tests/vertraege/test_vertrag_bericht_preise.py`, Prüfsumme `10cb7f5d18560887`) und bauen ihre Eingriffe
**mechanisch aus dem Syntaxbaum** — das war die Ursache, warum die Proben in Phase 2/3 nach jeder angenommenen
Generation stillschweigend woanders hinzielten.

| Probe | Ergebnis | Modellaufrufe | € | Kammerlauf | Dauer |
|---|---|---|---|---|---|
| nebenwirkung | abgelehnt, nennt `bericht` | 1 | 0,0015 | 1 | 8 s |
| regression | gefallener Einzeltest benannt | 1 | 0,0016 | 1 | 10 s |
| norm | 0 Punkte, nicht im Werk | 1 | 0,0009 | 1 | 8 s |
| vertrag | `Vertrag verletzt (Schritt 2)` | 1 | 0,0017 | 1 | 6 s |
| **Summe** | **4 von 4 bestanden** | **4** | **0,0057** | **4** | **31 s** |

**Die vier Tor-2-Zeilen (Nebenwirkung, Regression, Norm, Vertrag) sind damit wieder belegt.** Sie galten nach
Philipps Festlegung als ungeprüft, weil die alten Proben über Textanker zielten und ihre Prüfbedingungen zu
lasch waren.

**Eigener Fehler, vor der Meldung gefunden:** Im ersten Durchlauf standen vier „bestanden" — drei davon aus
falschen Gründen (Namensschema für Testdateien verletzt, Vertragsprobe als „Diff ändert nichts" abgelehnt, zu
lasche Prüfbedingungen). Alle drei behoben, danach bestehen die Proben aus den richtigen Gründen.

**Kostenfrage vor Phase 4, beantwortet:** Der vollständige Vorspann kostet **9 Kammerläufe, 4 Modellaufrufe,
0,0057 €, 44 s** (Rauschmessung 5 Kammerläufe, vier Proben je 1, Fundprüfung je Fund 1). Die **Zahl** der
Kammerläufe hängt nicht an der Bereichszahl — alle Bereiche werden je Lauf zusammen gemessen; mit 17 Diensten
wächst die **Dauer je Lauf**, nicht ihre Zahl. Eine lineare Hochrechnung auf 17 Dienste wäre eine erfundene
Zahl; die Dauer ist am dortigen Werk zu messen.

---

## 3. Punkt 2 — Fund-Neubewertung als Organ

Beleg: `ausgaben/11-fundpruefung-organ.txt`.

`fundpruefung.bewerten()` führt jeden offenen Fund am neuen Ausgang in der Kammer aus; `uebernehmen()` erzwingt
die Neubewertung bei jeder Übernahme zwischen Werken. Das Organ benutzt **die Ankläger-Logik selbst**
(`aegis._nennt_vertrag`) statt eines eigenen Verweis-Regex — zwei Wahrheitsbegriffe für dieselbe Frage sind
genau die Fehlerklasse, die die Regel behebt.

Gemessen: Fund, der am Ausgang fällt und den Vertrag nennt → bleibt Fund. Fund, der besteht, ohne Absturz und
ohne Verweis → wird Norm. K1165 (`im_werk`) bleibt unberührt.

**Eigener Fehler, durch den Lauf aufgedeckt:** Meine erste Regelfassung lautete „besteht → Norm, sonst Fund".
Damit wurden **9 von 20** Normtests zu Funden hochgestuft, nur weil sie am Ausgang fallen — und hätten über
Pareto je Test wieder Behebungen töten können. Das ist Lauf 16 von der anderen Seite. Korrigiert nach dem
Grundsatz, den Chat-Claude daraus für Fassung 6 gefasst hat: **Ein fallender Test beweist eine Abweichung, nie
ihre Richtung — welche Seite recht hat, entscheidet nur ein Absturz oder ein Vertrag.** Nach der Korrektur:
1 von 28 neu eingestuft, nämlich der gestellte Prüffall.

---

## 4. Punkt 3 — Abbruch als benannter Befehl

Beleg: `ausgaben/12-abbruch-nie-gesperrt.txt`.

**Korrektur an der Diagnose aus Phase 3:** Das Freigabe-Gate hat den Abbruch nie geprüft — es gab **keinen
Abbruch-Befehl**. Ich musste mit `pkill` und Ad-hoc-SQL arbeiten, und *diese* Muster blockierte das
Werkzeug-Gate, zu Recht. Die Lehre ist nicht „weniger Gate", sondern: **Für jede Pflicht muss es einen
benannten Befehl geben** — eine Pflicht, die nur über Notbehelfe erreichbar ist, wird entweder blockiert oder
umgeht den Schutz.

Fünf Fälle gemessen: laufender Lauf → `verworfen`, offene Generation geschlossen; der verworfene Lauf sperrt
danach **0** Kandidaten im Projektgedächtnis; zweiter Abbruch → keine Ausnahme, protokolliert; `art='budget'`
→ `abgebrochen` statt `verworfen`; `POST /laeufe/1/abbrechen` ohne Token → **HTTP 401** (am laufenden Dienst
gemessen, Gegenprobe Freigabe ebenfalls 401).

---

## 5. Punkt 4 — Doppelungsschlüssel und Tor 2 Zeile 8

Belege: `ausgaben/13-doppelungen-behauptung.txt`, `14-behauptungen-nachgetragen.txt`, `18-anklaeger-vielfalt.txt`.

`aegis.behauptung(code, testname)` bildet den Schlüssel aus dem Syntaxbaum: **aufgerufene Werk-Funktion +
Zusicherungsart** (`raises:<Ausnahme>` oder Vergleichsoperator plus Form der erwarteten Seite), **ohne** den
Zahlenwert. Er steht im `ursprung` jedes Funds; 284 Alteinträge wurden nachgetragen.

**Die sechs Tests der Phase-3-Falle** (`Katalog.wert` liefert Staffel- statt Grundpreis) fallen jetzt auf
**eine** Behauptung `Staffel|Eq:zahl`. Fünf davon wären nie einzeln ins Immunsystem gekommen.

**Tor 2 Zeile 8, neu gemessen — gerissen:**

| Lauf | erzeugte Tests | Behauptungen | erkannt/verworfen | unbemerkt aufgenommen | größte Gruppe | Anteil |
|---|---|---|---|---|---|---|
| 13 (Phase 2) | 54 | 27 | 6 | 31 | 8 | **68,5 %** |
| 20 (vor Umstellung) | 11 | 4 | 0 | 7 | 5 | **63,6 %** |
| 22 (Anweisung aktiv) | 11 | 5 | **6** | **0** | **1** | **54,5 %** |

**Bezugsgröße, ohne die die Zahlen irreführen (Vorgabe Philipp):** Die Prozentzahlen vor und nach dem
Schlüsselwechsel zählen nicht dieselbe Menge. Vor dem Wechsel wanderten Wiederholungen **unbemerkt** ins
Immunsystem; nach dem Wechsel werden sie **erkannt und verworfen**. „63,6 → 54,5" liest sich als kleine
Verbesserung und verfehlt die Sache: In Lauf 22 wurden 6 von 11 abgefangen, und die größte Gruppe gleicher
Behauptung fiel von 5 auf 1.

Die 83,6 % aus meinem Phase-3-Bericht waren eine Heuristik; mit dem gebauten Schlüssel sind es **68,5 %**.
Die Wertung „Zeile 8 gerissen" bleibt, die Zahl ist berichtigt. **Grenze bleibt bei 20 %.**

**Ankläger-Anweisung (Fassung 6):** Dem Ankläger werden vor jedem Angriff seine bisherigen Behauptungen des
Bereichs vorgelegt, mit dem Auftrag, eine andere zu finden — Text im ohnehin fälligen Aufruf, keine
Zusatzkosten. Sie wirkt teilweise (größte Gruppe 5 → 1), hebt den Anteil aber nicht unter 20 %.
**0 Aufrufe** antworteten mit „KEIN ANGRIFF", obwohl die Anweisung das ausdrücklich erlaubt — das Modell
liefert lieber eine Wiederholung als nichts. Nach Philipps Festlegung ist das ein Befund über die Modelle,
keine Einladung, die Grenze zu senken.

---

## 6. Punkt 5 — Artgedächtnis speichert Muster

Belege: `ausgaben/19-muster-nachabstraktion.txt`, `23-artgedaechtnis-muster-messung.txt`.

`muster_bilden()` abstrahiert jede angenommene Änderung zu einem Satz **ohne Werk-, Datei- und
Funktionsnamen**; `art_text()` zeigt werkübergreifend nur Muster, die Instanz bleibt als Beleg in der
Datenbank. Nachabstraktion beider Werke: **18 Muster** aus 19 angenommenen Einträgen, 1 als nicht übertragbar
gemeldet, Kosten **0,003 €**.

Beispiel: aus „`Katalog.wert` nutzte `stueckpreis(menge)` statt `grundpreis`" wird „Bei der Katalogbewertung
den unveränderten Grundpreis verwenden, wenn Mengenrabatte ausdrücklich nicht berücksichtigt werden sollen."

**Torzeile, erneut gemessen:**

| Lauf | Richtungen mit werkübergreifendem Verweis | erfundene Kennungen |
|---|---|---|
| 16, 17, 18, 19, 20, 22 (Instanzen) | **0** von je 4–5 | 0 |
| **23 (`logmuehle`, Muster)** | **2 von 5** — A132, A359, A249, A6, A141 | **0** |

**Torzeile Artgedächtnis: erfüllt.** Zwei Richtungen zitieren Muster aus `lagerhaus`.

**Was die Messung zusätzlich zeigt:** Mein erster Messlauf war Lauf 22 am `lagerhaus` — dort wieder 0 von 4.
Grund: Ein `lagerhaus`-Lauf sieht **3** fremde Muster, ein `logmuehle`-Lauf **13**. Die Zeile hängt also auch
an der Zahl verfügbarer fremder Muster. Chat-Claude hat daraus für Fassung 6 einen festen Mindestanteil des
werkübergreifenden Blocks an der Vorlage festgelegt — bei 17 Diensten verdrängt die Masse eigener Einträge
fremde Muster sonst allein durch Menge.

**Zwei eigene Fehler:** Ich hatte den Anbieter geraten (`openai` statt `openrouter`); 19 Abstürze wurden als
„nicht übertragbar" gezählt und hätten fast als Ergebnis gegolten — ein Aufruffehler wird jetzt geworfen statt
als inhaltliches Urteil verbucht. Und: `CREATE TABLE IF NOT EXISTS` ergänzt keine Spalten an bestehenden
Tabellen; die Muster-Spalten werden per `ALTER TABLE` nachgezogen.

---

## 7. Punkt 6 — Archivierung nach Generationen

Beleg: `ausgaben/24-archivierung-neue-zeile.txt`.

| Lauf | Generationen | davon angenommen | alte Zählung | neue Zählung |
|---|---|---|---|---|
| 16 | 8 | 2 | erreicht 5 nie | erreicht 5 |
| 17 | 7 | 4 | nie | erreicht 5 |
| 19 | 5 | 1 | nie | erreicht 5 |
| 20 | 5 | 1 | nie | erreicht 5 |
| 22 | 4 | 0 | nie | nein |

Vier von fünf Läufen hätten nach neuer Zählung archiviert, nach alter **kein einziger** — das ist der Grund
für die 0 Archivierungen in Phase 3. Mechanikprüfung an einem erzeugten Fund: nach 3 und 4 Generationen offen,
nach 5 archiviert; archivierte Funde werden nicht mehr vorgelegt, bleiben aber einsehbar.

**Eigener Fehler, korrigiert und protokolliert:** Die Mechanikprüfung löste die echte Regel am echten Bestand
aus und archivierte **zwei echte Normtests** mit. Beide zurückgesetzt (`immun.archivierung_zurueckgenommen`).
Chat-Claude hat daraus mit dem Probenabfall zusammen einen Satz für Fassung 6 gefasst: **Eine Prüfung darf den
geprüften Bestand nicht verändern — ihr Wirkungsbereich wird vorher eingegrenzt, und was sie hinterlässt, wird
vor der nächsten Messung zurückgenommen und protokolliert.**

---

## 8. Punkt 7 — die drei strittigen Fälle, entschieden

Beleg: `ausgaben/25-projektgedaechtnis-differenz.txt`. Beide Ableitungen wurden auf denselben Kandidatensatz
angewandt: **A** = Hunk-Köpfe (meine Nachrechnung), **B** = angewandter Diff (das Biotop).

- **K2032 — keine Wiederholung.** A ordnet `lagerwert` zu, weil die Funktion im Hunk-Kopf steht; geändert wurde
  `bewegungsbericht`. Kein gemeinsames geändertes Ziel mit dem Weg K952. Die Ähnlichkeit von 1,00 stammt aus
  den Token der hinzugefügten Zeilen, nicht aus dem Ziel.
- **K2035 — keine Wiederholung.** Gleiche Lage gegen K882.
- **K2056 — Wiederholung nach beiden Ableitungen, aber zu Recht ausgeführt:** Der Weg K1344 stammt aus Lauf 16,
  und Lauf 16 ist verworfen. Nach F5 3.12 zählen dessen Wege nicht mehr — gemessen: von 91 sichtbaren Wegen für
  `bericht` stammen **0** aus Lauf 16 und 57 aus Lauf 13. Meine Nachrechnung hatte den Filter nicht angewandt.

**Ergebnis: 0 von 3 strittigen Fällen sind durchgerutschte Wiederholungen.** Die Zahl des Biotops war richtig,
meine Nachrechnung war falsch. **Die Torzeile Projektgedächtnis aus Phase 3 ist damit erfüllt, nicht
„teilweise"** — sie war es schon damals; die Unsicherheit stammte allein aus meiner Nachrechnung.

**Lehre (Fassung 6):** Eine Nachrechnung muss dieselbe Ableitung verwenden wie das geprüfte Organ, sonst misst
sie etwas anderes und erzeugt eine Scheindifferenz.

---

## 9. Punkt 8 — Verfassungsentwurf `logmuehle` (zur Bestätigung durch Chat-Claude)

Der Entwurf lag dem Phase-3-Bericht nicht bei — mein Versäumnis; er war nur verwiesen, nicht abgedruckt.
Datei: `verfassungen/logmuehle.md`, Prüfsumme `0ce7f8651ae70ad0783cb6caa8f54b9ebbcf789b5e6b116d6df6fb63242bc803`
(Regeln: `bce33200a57d77e5a9254e0da271c38c9ce23404506cc6cfb0bf902e5051b0c8`), Kopien in
`ausgaben/26-verfassungsentwurf-logmuehle.md` und `…regeln.json`.

> **Verfassung des Übungswerks „logmuehle"** — Entwurf Hermes (Masterprompt v4 Abschnitt 8 Phase 3;
> Chat-Claude bestätigt am Bericht). Ändert nur Philipp.
>
> 1. **Was es ist:** Ein Befehlszeilenwerkzeug, das Zugriffsprotokolle im Common Log Format liest, nach Zeit,
>    Status und Pfad filtert, Kennzahlen bildet und sie als Text, CSV oder JSON ausgibt. Es ist ein Übungswerk
>    ohne Betriebszweck; es verarbeitet nur Dateien, die der Aufrufer nennt.
> 2. **Sicherheit vor Bequemlichkeit:** Kein Bereich reicht Eingaben des Aufrufers an eine Shell weiter oder
>    führt sie als Programmcode aus; externe Werkzeuge werden nur als Argumentliste ohne Shell gestartet. Ein
>    Sicherheitsbefund wiegt mehr als jede Laufzeit. Tauschregel: Die Laufzeit auf der Referenzlast darf bis
>    ×3 gegenüber dem Bestwert des Laufs steigen, wenn dabei ein statischer Sicherheitsbefund verschwindet;
>    sonst gilt ×2.
> 3. **Korrektheit der Zählung:** Jeder gelesene Eintrag wird genau einmal gezählt; unlesbare Zeilen werden
>    gezählt und gemeldet, nie verschluckt; Zeitfenster sind an beiden Enden einschließlich; Zeiten sind
>    zeitzonenbewusst und werden nach UTC normalisiert; Perzentile folgen dem nächsten Rang.
> 4. **Grenzen sind Verträge:** Die Schnittstellen zwischen `lesen`, `filtern`, `zaehlen` und `ausgabe` ändern
>    sich nur, wenn beide Seiten in derselben Generation angepasst und gemeinsam geprüft werden.
> 5. **`ausgabe` ist Darstellung, keine Logik:** Der Bereich rechnet nichts nach, was `zaehlen` liefert; er
>    formatiert und setzt Rückgabecodes.
> 6. **Was nie passieren darf:** Ein Kandidat, der Tests entfernt oder abschwächt, um einen Fehlschlag zu
>    beseitigen; ein Kandidat, der einen Sicherheitsbefund durch Ausnahmeregel im Prüfwerkzeug (`# nosec`,
>    Konfiguration) zum Verschwinden bringt statt durch Code; ein Kandidat, der Dateien außerhalb der
>    genannten Protokolldatei liest oder schreibt.

**Anmerkung zur Wirksamkeit:** Satz 2 wurde vom Werk anders erfüllt als erwartet — der Schwarm entfernte den
Subprozess ganz, statt ihn abzusichern. Satz 6 ist mechanisch verdrahtet (`verbotene_muster` in
`logmuehle.regeln.json`), Satz 2 über die Tauschregel (`laufzeit_faktor_bei_sicherheitsgewinn: 3.0`).

---

## 10. Kosten

| Lauf | Aufrufe | € |
|---|---|---|
| 22 (`lagerhaus`, 4 Generationen + Vorspann) | 189 | 0,3978 |
| 23 (`logmuehle`, Aufnahme + Mentor) | 18 | 0,0389 |
| **Summe ab Lauf 21** | **207** | **0,4367** |

Budget 10 € — **4,4 % verbraucht**. Größter Posten: `schwer.mentor` 3 Aufrufe, 0,0957 €.
Eichkosten **getrennt ausgewiesen** (nicht in der Laufsumme): Lauf 22 → 9 Kammerläufe, 4 Modellaufrufe,
0,0057 €, 44 s. Nachabstraktion des Artgedächtnisses: 19 Aufrufe, 0,003 €.

---

## 11. Was offen bleibt

- **Tor 2 Zeile 8 bleibt gerissen** (54,5 % gegen 20 %). Nächster Schritt für Fassung 6, von Chat-Claude
  bestätigt: Der Ankläger nennt seine Behauptung vorab; bei Wiederholung wird der Angriff gar nicht erst
  ausgeführt — das spart zusätzlich Aufrufe.
- **Werkübergreifender Mindestanteil** im Artgedächtnis-Block (Fassung 6) — noch nicht gebaut.
- Die Läufe 22 und 23 stehen auf `bereit` und sind nicht zu Ende geführt; sie waren Messläufe, keine
  Hebungsläufe.
- `pruefung/funde_neubewerten.py` (Phase-3-Skript) ist durch `organe/fundpruefung.py` abgelöst, aber noch
  nicht entfernt.

---

## 12. Sätze für Fassung 6 (aus diesem Nachlauf, von Chat-Claude gefasst)

1. Ein fallender Test beweist eine Abweichung, nie ihre Richtung — welche Seite recht hat, entscheidet nur ein
   Absturz oder ein Vertrag.
2. Für jede Pflicht muss es einen benannten Befehl geben; eine Pflicht, die nur über Notbehelfe erreichbar ist,
   wird entweder blockiert oder umgeht den Schutz.
3. Streuung wird immer zwischen Messungen gebildet, nie innerhalb einer.
4. Eine Prüfung darf den geprüften Bestand nicht verändern — Wirkungsbereich vorher eingrenzen, Hinterlassenes
   vor der nächsten Messung zurücknehmen und protokollieren.
5. Eine Nachrechnung muss dieselbe Ableitung verwenden wie das geprüfte Organ.
6. Prüfe die Sache, nicht ihre Erscheinung: Behauptung statt Fundstelle, gesetztes Merkmal statt Name,
   Verfassung statt Vertragsgröße.
