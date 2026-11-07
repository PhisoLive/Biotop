# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 017 von 054

- Einträge V0287 bis V0351. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0287 · 19.09.2026 21:59:07 CEST · Hermes · Nachricht id 2451 · Sitzung `20260918_225920_3e614670` · 1654 B

```text
Härtung eingebaut und belegt (`ausgaben/09-probenmerkmal-statt-name.txt`).

**Das Feld:** `kandidaten.ist_probe` (Spalte ergänzt, Schema aktualisiert). Alle vier Erzeuger setzen es beim Anlegen — `lauf.py` (Einschleusung im Lauf), `proben_tor2.py`, `jury_probe.py`, `verhandlungsprobe.py`. `ist_probe()` prüft zuerst das Merkmal; Nische und Bereichsname bleiben als zweiter Weg für Altbestand, ausdrücklich als Notnagel gekennzeichnet.

**Der entscheidende Nachweis** — Probe unter einem Namensschema, das der Namensweg *nicht* kennt (`nische='eichung_vorspann_v2'`, Bereich `preise`):
- mit `ist_probe=1`: gesperrt, Zuwachs 0
- derselbe Kandidat mit `ist_probe=0`: **durchgerutscht**, Zuwachs 1

Damit ist gezeigt, dass die Sperre am Merkmal hängt und nicht am Namen — und zugleich, dass die alte Bauweise diese Probe verfehlt hätte. Altbestand (`nische='probe'`, Feld 0) fängt der zweite Weg weiterhin; ein echter Kandidat wird normal aufgenommen.

**Altbestand markiert:** 29 Kandidaten aus Phase 2/3 nachträglich auf `ist_probe=1` gesetzt, protokolliert (`kandidaten.probe_markiert`). Gegenprobe: 0 Proben ohne Merkmal, 0 echte Kandidaten fälschlich markiert — der Namensweg wird also derzeit von keinem Eintrag mehr gebraucht.

Es ist dieselbe Fehlerklasse wie bei der Doppelungserkennung, die du benannt hast: Prüfe die Sache (gesetztes Merkmal, Behauptung), nicht ihre Erscheinung (Name, Fundstelle).

Zwischenbericht im Ordner (10 Dateien, Prüfsumme `f648a7dcc9736c760cdc4dbc233269b13f634a7ee98b7e1f782f7195a9bfeaf2`), Kosten 0 € von 10 €.

Jetzt die vier Proben am versiegelten Gegenstand, Modellaufrufe je Probe einzeln.
```

### V0288 · 19.09.2026 22:07:08 CEST · Philipp · Nachricht id 2452 · Sitzung `20260918_225920_3e614670` · 995 B

```text
Der Nachweis ist sauber — derselbe Kandidat mit und ohne Merkmal unter einem Namensschema, das der alte Weg nicht kennt; und dass nach der Altbestandsmarkierung kein Eintrag mehr den Namensweg braucht, macht ihn zum leerlaufenden Notnagel, wie gewollt. Ab hier keine weiteren Härtungen mehr vor den Proben: Die sieben Nachlaufpunkte stehen noch fast vollständig aus, und was mir jetzt noch auffällt, sammle ich für Fassung 6, statt es einzeln nachzuschieben. Arbeite die Punkte in dieser Reihenfolge ab: vier Proben am versiegelten Gegenstand (Modellaufrufe je Probe einzeln), Fund-Neubewertung als Organ, Gate-Ausnahme für Abbrüche, Doppelungsschlüssel auf die Behauptung mit Neumessung von Tor 2 Zeile 8, Artgedächtnis auf Muster mit Nachabstraktion beider Werke und erneuter Messung der Torzeile, Archivierung nach der neuen Zeile, Projektgedächtnis-Differenz an den drei strittigen Fällen, Verfassungsentwurf abdrucken. Zwischenbericht vor jedem Sitzungsende, Budget 10 € hart.
```

### V0289 · 19.09.2026 22:07:18 CEST · Hermes-Zwischentext · Nachricht id 2453 · Sitzung `20260918_225920_3e614670` · 131 B

```text
Verstanden — keine Härtungen mehr, die sieben Punkte in deiner Reihenfolge. Punkt 1: die vier Proben am versiegelten Gegenstand.
```

### V0290 · 19.09.2026 22:09:14 CEST · Hermes-Zwischentext · Nachricht id 2455 · Sitzung `20260918_225920_3e614670` · 113 B

```text
Jetzt der Vorspann selbst. Ich baue die vier Proben mechanisch am versiegelten Gegenstand, mit Zählung je Probe.
```

### V0291 · 19.09.2026 22:09:45 CEST · Hermes-Zwischentext · Nachricht id 2461 · Sitzung `20260918_225920_3e614670` · 82 B

```text
Eine tote Zeile aus einem Zwischenstand — die zweite Zuweisung war die richtige.
```

### V0292 · 19.09.2026 22:10:06 CEST · Hermes-Zwischentext · Nachricht id 2465 · Sitzung `20260918_225920_3e614670` · 141 B

```text
Nur die erste Probe ist echt bestanden — die anderen drei bestehen aus falschen Gründen. Das melde ich so, statt „4 von 4" zu schreiben.
```

### V0293 · 19.09.2026 22:10:12 CEST · Hermes-Zwischentext · Nachricht id 2467 · Sitzung `20260918_225920_3e614670` · 179 B

```text
Drei Baufehler bei mir, nicht im Messgerät: Neue Testdateien werden als „vorhandene Testdatei geändert" gewertet, und mein Vertrags-Diff kam nicht an. Ich prüfe die Ursachen.
```

### V0294 · 19.09.2026 22:10:33 CEST · Hermes-Zwischentext · Nachricht id 2473 · Sitzung `20260918_225920_3e614670` · 160 B

```text
Gefunden: Testdateien müssen `tests/test_<bereich>_*.py` heißen — meine Probennamen verletzen das Schema. Das ist mein Baufehler, nicht der des Messgeräts.
```

### V0295 · 19.09.2026 22:11:03 CEST · Hermes-Zwischentext · Nachricht id 2477 · Sitzung `20260918_225920_3e614670` · 173 B

```text
Die Vertragsprobe ändert nur die Vertragsdatei — für den Ankläger ist das „nichts". Ich baue sie als echte Grenzänderung: A fordert etwas von B, das B nicht liefert.
```

### V0296 · 19.09.2026 22:11:11 CEST · Hermes-Zwischentext · Nachricht id 2479 · Sitzung `20260918_225920_3e614670` · 113 B

```text
Die Regressionsprobe muss noch echt prüfen: Der gefallene *Einzeltest* muss benannt sein, nicht irgendein Grund.
```

### V0297 · 19.09.2026 22:11:21 CEST · Hermes-Zwischentext · Nachricht id 2481 · Sitzung `20260918_225920_3e614670` · 95 B

```text
Die Norm-Probe prüft ebenfalls zu lasch (`zuwachs=None` gilt als bestanden). Ich schärfe sie.
```

### V0298 · 19.09.2026 22:12:09 CEST · Hermes-Zwischentext · Nachricht id 2485 · Sitzung `20260918_225920_3e614670` · 121 B

```text
Jetzt bestehen alle vier aus den richtigen Gründen — jede mit eigenem Kandidaten, Kammerlauf, Modellaufruf und Kosten.
```

### V0299 · 19.09.2026 22:12:31 CEST · Hermes-Zwischentext · Nachricht id 2487 · Sitzung `20260918_225920_3e614670` · 193 B

```text
Zwei Fehler in meiner Abrechnung: Die Kammerläufe summieren über Wiederholungen des Prüfskripts, und die Modellaufrufe zeigen 0, weil die Ankläger-Aufrufe nicht den Zweck `eichung.` tragen.
```

### V0300 · 19.09.2026 22:13:28 CEST · Hermes-Zwischentext · Nachricht id 2493 · Sitzung `20260918_225920_3e614670` · 113 B

```text
Die Abrechnung stimmt jetzt mit den Einzelzahlen überein: 4 Proben, 4 Kammerläufe, 4 Modellaufrufe, 0,0055 €.
```

### V0301 · 19.09.2026 22:13:45 CEST · Hermes · Nachricht id 2495 · Sitzung `20260918_225920_3e614670` · 2204 B

```text
**Punkt 1 von 8 erledigt: die vier Eichproben am versiegelten Gegenstand** (`organe/eichproben.py`, Beleg `ausgaben/10-eichproben-vorspann.txt`).

Gegenstand: `bericht→preise`, Vertrag `test_vertrag_bericht_preise.py`, Prüfsumme `10cb7f5d18560887`. Alle vier bestanden, jede mit eigenem Kandidaten und eigener Abrechnung:

| Probe | Ergebnis | Modellaufrufe | € | Kammerlauf | Dauer |
|---|---|---|---|---|---|
| nebenwirkung | bestanden — abgelehnt, nennt `bericht` | 1 | 0,0015 | 1 | 8 s |
| regression | bestanden — Einzeltest benannt (`test_bericht.py::test_lagerwert_ge…`) | 1 | 0,0015 | 1 | 10 s |
| norm | bestanden — 0 Punkte, nicht im Werk | 1 | 0,0009 | 1 | 8 s |
| vertrag | bestanden — `Vertrag verletzt (Schritt 2)` | 1 | 0,0017 | 1 | 6 s |
| **Summe** | | **4** | **0,0055** | **4** | **32 s** |

Die Eingriffe werden **mechanisch aus dem Syntaxbaum** gebaut, nicht aus Textankern — das war die Ursache, warum die Proben in Phase 2/3 nach jeder angenommenen Generation stillschweigend woanders hinzielten. Alle vier Probenkandidaten tragen `ist_probe=1`, nachgeprüft: 0 Einträge in einem Gedächtnis.

**Drei Baufehler bei mir, gefunden und behoben, bevor ich sie als bestanden gemeldet hätte** — im ersten Durchlauf standen vier „bestanden", aber drei aus falschen Gründen:
- Regression und Norm scheiterten am Namensschema für Testdateien (`tests/test_<bereich>_*.py`), nicht an der Sache; die Prüfbedingungen waren zudem so lasch, dass sie das akzeptierten.
- Die Vertragsprobe änderte nur die Vertragsdatei → „Diff ändert nichts". Jetzt fordert der Vertrag eine Funktion vom Nachbarn, der Konsument nutzt sie, der Lieferant wird bewusst nicht angepasst — und genau das fällt auf.
- Die Abrechnung zeigte 0 Modellaufrufe (Ankläger-Aufrufe tragen ihren eigenen Zweck) und summierte Kammerläufe über wiederholte Skriptläufe. Jetzt misst der Aufrufer den Kassenstand vor/nach jeder Probe, und ein Eintrag desselben Teils wird ersetzt statt ergänzt.

Zwischenbericht im Ordner (11 Dateien, Prüfsumme `43e90b2c87c4d692deec228345d94c0bb5e0a160081d27123f67f39b75c781b5`). Kosten: 0,0055 € von 10 €.

Weiter mit Punkt 2: Fund-Neubewertung als Organ.
```

### V0302 · 19.09.2026 22:17:05 CEST · Philipp · Nachricht id 2496 · Sitzung `20260918_225920_3e614670` · 1006 B

```text
Dass die Proben über Textanker zielten und nach jeder angenommenen Generation woanders hintrafen, ist ein Befund über Tor 2, nicht nur über den Vorspann — zusammen mit den zu laschen Prüfbedingungen heißt das, dass die Probenzeilen aus Phase 2 möglicherweise nie das geprüft haben, was sie behaupten; es erklärt auch, warum die Norm-Lücke aus Lauf 16 trotz Normprobe durchkam. Deshalb ein neunter Punkt im Nachlauf, direkt bei Punkt 4 mitzunehmen: Tor 2, Zeilen Nebenwirkung, Regression, Norm und Vertrag mit den gehärteten Proben einmal nachmessen — vier Proben kosten 0,0055 € und 32 s, das ist der billigste Weg, diese Zeilen wieder belegt zu haben; bis dahin gelten sie als ungeprüft. Dass du den ersten Durchlauf mit vier „bestanden" nicht gemeldet, sondern die Gründe geprüft hast, ist der wichtigste Teil der Runde. Die Kostenfrage vor Phase 4 ist beantwortet: 4 Modellaufrufe, 4 Kammerläufe, 0,0055 € je Lauf, davon wächst auf 17 Diensten nur die Dauer. Weiter mit Punkt 2.
```

### V0303 · 19.09.2026 22:17:17 CEST · Hermes-Zwischentext · Nachricht id 2497 · Sitzung `20260918_225920_3e614670` · 235 B

```text
Notiert: Tor-2-Zeilen Nebenwirkung, Regression, Norm, Vertrag gelten bis zur Nachmessung als ungeprüft — kommt bei Punkt 4 mit.

Punkt 2: Fund-Neubewertung als Organ. Bisher ist das ein Prüfskript, das ich von Hand aufrufen musste.
```

### V0304 · 19.09.2026 22:17:27 CEST · Hermes-Zwischentext · Nachricht id 2499 · Sitzung `20260918_225920_3e614670` · 175 B

```text
Das Skript hat zwei Schwächen: Es hat einen eigenen Verweis-Regex statt der Ankläger-Logik, und die Absturz-Erkennung ist grob. Als Organ muss es dieselbe Wahrheit benutzen.
```

### V0305 · 19.09.2026 22:19:02 CEST · Hermes-Zwischentext · Nachricht id 2509 · Sitzung `20260918_225920_3e614670` · 187 B

```text
Die beiden Kernfälle sitzen — aber neun Normtests wurden zu `offen` hochgestuft, weil sie am Ausgang *fallen*. Das ist ein Fehler in meiner Regel: Fallen allein macht noch keinen Fund.
```

### V0306 · 19.09.2026 22:19:40 CEST · Hermes-Zwischentext · Nachricht id 2513 · Sitzung `20260918_225920_3e614670` · 118 B

```text
Jetzt stimmt es: **1 von 28** neu eingestuft statt 10 — nur der gestellte Fall, die 20 Normtests bleiben unberührt.
```

### V0307 · 19.09.2026 22:19:55 CEST · Hermes · Nachricht id 2515 · Sitzung `20260918_225920_3e614670` · 1723 B

```text
**Punkt 2 erledigt: Fund-Neubewertung als Organ** (`organe/fundpruefung.py`, Beleg `ausgaben/11-fundpruefung-organ.txt`).

Zwei Dinge anders als im Prüfskript aus Phase 3:
- Es benutzt **die Ankläger-Logik selbst** (`aegis._nennt_vertrag`) statt eines eigenen Verweis-Regex. Zwei Wahrheitsbegriffe für dieselbe Frage sind genau die Fehlerklasse, die diese Regel behebt.
- `uebernehmen()` erzwingt die Neubewertung: Funde zwischen Werken zu übertragen, ohne sie nachzumessen, geht nicht mehr — das war mein Fehler in Lauf 19.

**Geprüft an echten Kammerläufen**, zwei gestellte Funde am Werk 18:
- fällt am Ausgang, nennt den Vertrag → **bleibt Fund** ✓
- besteht am Ausgang, kein Verweis, kein Absturz → **wird Norm** ✓
- K1165 (in Lauf 20 behoben, Status `im_werk`) bleibt unberührt — die Neubewertung fasst nur offene Funde an.

**Ein Fehler in meiner ersten Regelfassung, durch den Lauf aufgedeckt:** Ich hatte „besteht → Norm, sonst Fund" geschrieben. Damit wurden **9 von 20** Normtests zu Funden hochgestuft, nur weil sie am Ausgang fallen. Fallen allein macht keinen Fund — ein Test, der ohne Absturz und ohne Vertragsbezug fällt, kodiert eine Meinung über gewünschtes Verhalten (genau 3.7). Sonst würde jeder Normtest, den eine spätere Generation ins Fallen bringt, stillschweigend zum Fund und könnte per Pareto Behebungen töten — dieselbe Falle wie in Lauf 16, nur von der anderen Seite. Nach der Korrektur: **1 von 28** neu eingestuft, nämlich der gestellte Fall.

Zwischenbericht im Ordner (12 Dateien, Prüfsumme `e605b010fb715600763e56946215c6c4faf7fbe37b3cb8d64d707296bcd73fe8`), Kosten 0,0055 € von 10 €.

Weiter mit Punkt 3: Gate-Ausnahme für Abbrüche nach Satz 2.
```

### V0308 · 19.09.2026 22:32:26 CEST · Philipp · Nachricht id 2516 · Sitzung `20260918_225920_3e614670` · 774 B

```text
Dein Fund in der ersten Regelfassung ist Lauf 16 von der anderen Seite: Dort machte Fallen am Kandidaten aus einem Normtest einen Fund, hier hätte Fallen am Ausgang dasselbe getan — 9 von 20 hochgestuft, und über Pareto hätten sie wieder Behebungen töten können. Das ist nach Doppelungserkennung (Ort statt Behauptung) und Probenerkennung (Name statt Merkmal) das dritte Auftreten derselben Denkfigur; für Fassung 6 führe ich sie als eigenen Satz: Ein fallender Test beweist eine Abweichung, nie ihre Richtung — welche Seite recht hat, entscheidet nur ein Absturz oder ein Vertrag. Ankläger-Logik aufrufen statt zweiten Regex und uebernehmen() mit erzwungener Neubewertung sind beide richtig gebaut. Weiter mit Punkt 3, dann 4 bis 9 in der gesetzten Reihenfolge.
```

### V0309 · 19.09.2026 22:32:43 CEST · Hermes-Zwischentext · Nachricht id 2517 · Sitzung `20260918_225920_3e614670` · 155 B

```text
Der Satz trifft es genau — ich schreibe ihn an die drei Stellen, an denen die Denkfigur zuschlug, damit er beim nächsten Anfassen dasteht. Dann Punkt 3.
```

### V0310 · 19.09.2026 22:32:49 CEST · Hermes-Zwischentext · Nachricht id 2519 · Sitzung `20260918_225920_3e614670` · 118 B

```text
Jetzt Punkt 3: Gate-Ausnahme für Abbrüche. Zuerst sehe ich nach, was das Gate in Phase 3 tatsächlich blockiert hat.
```

### V0311 · 19.09.2026 22:33:06 CEST · Hermes-Zwischentext · Nachricht id 2521 · Sitzung `20260918_225920_3e614670` · 181 B

```text
Das eigentliche Problem war: Es gab **keinen** Abbruch-Befehl. Ich musste in Phase 3 mit `pkill` und Ad-hoc-SQL arbeiten — und genau diese Muster hat das Gate blockiert, zu Recht.
```

### V0312 · 19.09.2026 22:33:35 CEST · Hermes-Zwischentext · Nachricht id 2525 · Sitzung `20260918_225920_3e614670` · 79 B

```text
Jetzt CLI und Web-Route, damit der Abbruch ohne Umweg über SQL erreichbar ist.
```

### V0313 · 19.09.2026 22:34:28 CEST · Hermes-Zwischentext · Nachricht id 2533 · Sitzung `20260918_225920_3e614670` · 133 B

```text
Derselbe Kollisionsfehler wie bei `gedaechtnis.wiederholung` in Phase 3 — `art` ist ein Parameter von `protokoll.schreiben` selbst.
```

### V0314 · 19.09.2026 22:34:39 CEST · Hermes-Zwischentext · Nachricht id 2537 · Sitzung `20260918_225920_3e614670` · 80 B

```text
Fall 5 ist nur halb belegt — ich starte den Dienst und messe die 401 wirklich.
```

### V0315 · 19.09.2026 22:35:19 CEST · Hermes · Nachricht id 2543 · Sitzung `20260918_225920_3e614670` · 2041 B

```text
**Punkt 3 erledigt: Gate-Ausnahme für Abbrüche** (Beleg `ausgaben/12-abbruch-nie-gesperrt.txt`).

Beim Bauen zeigte sich, dass die Diagnose aus Phase 3 nicht ganz stimmte: Das Freigabe-Gate hat den Abbruch nie geprüft — es gab schlicht **keinen Abbruch-Befehl**. Ich musste mit `pkill` und Ad-hoc-SQL arbeiten, und *diese* Muster hat das Werkzeug-Gate blockiert, zu Recht. Die Lehre ist also nicht „weniger Gate", sondern: Für eine Pflicht muss es einen benannten, harmlosen Befehl geben, der nicht wie ein Massenlöschen aussieht. Das steht so im Docstring.

**Gebaut:** `lauf.abbrechen(lauf, grund, von, art)`, CLI `biotop abbrechen … --art satz2|budget|philipp|sonst`, Route `POST /laeufe/<id>/abbrechen`.

**Fünf Fälle gemessen:**
- laufender Lauf mit offener Generation → Status `verworfen`, Generation geschlossen, Protokoll `lauf.abgebrochen`
- der verworfene Lauf sperrt danach **0** Kandidaten im Projektgedächtnis (1 Eintrag vorhanden, 0 sichtbar)
- zweiter Abbruch → keine Ausnahme, Hinweis „war bereits beendet", trotzdem protokolliert
- `art='budget'` → Status `abgebrochen` statt `verworfen`, Ablehnungen bleiben gültig
- `POST /laeufe/1/abbrechen` ohne Token → **HTTP 401**, am laufenden Dienst gemessen; Gegenprobe Freigabe ebenfalls 401

Der Abbruch ist damit *erreichbar*, ohne die Anmeldung zu umgehen — das Gate schützt weiterhin, blockiert aber keine Pflicht mehr.

**Dein Satz für Fassung 6** steht als Grundsatz im Code (`fundpruefung.py`), an der Stelle, wo die Denkfigur zum dritten Mal auftrat: *Ein fallender Test beweist eine Abweichung, nie ihre Richtung — welche Seite recht hat, entscheidet nur ein Absturz oder ein Vertrag.* Mit dem Hinweis, dass Lauf 16 derselbe Fehler von der anderen Seite war.

Zwischenbericht im Ordner (13 Dateien, Prüfsumme `055ed00a2411144920a9d7a5d5342e39187f1b8216b07348de42000a132a8ccf`), Kosten 0,0055 € von 10 €.

Weiter mit Punkt 4: Doppelungsschlüssel auf die Behauptung, Tor 2 Zeile 8 neu messen, dazu die Nachmessung der vier Probenzeilen.
```

### V0316 · 19.09.2026 22:36:12 CEST · Philipp · Nachricht id 2544 · Sitzung `20260918_225920_3e614670` · 836 B

```text
Deine Korrektur trifft mich: Ich hatte „vom Gate blockiert" aus deiner Phase-3-Meldung übernommen und daraus eine Ausnahmeregel gebaut, ohne nachzusehen, was genau blockiert wurde — das Gate hatte recht, es fehlte der Befehl. Der Satz für Fassung 6 lautet deshalb nicht „Abbrüche sind ausgenommen", sondern: Für jede Pflicht muss es einen benannten Befehl geben — eine Pflicht, die nur über Notbehelfe erreichbar ist, wird entweder blockiert oder umgeht den Schutz, und beides verschwindet, sobald der Weg vorgesehen ist. Die Route mit 401 ohne Token ist die richtige Auflösung. Inhaltlich am wichtigsten in deinem Beleg: Der verworfene Lauf sperrt danach 0 Kandidaten im Projektgedächtnis — damit ist die Fassung-5-Regel am Ergebnis belegt, nicht nur im Code. Weiter mit Punkt 4 samt Nachmessung der vier Probenzeilen.
```

### V0317 · 19.09.2026 22:36:17 CEST · Hermes-Zwischentext · Nachricht id 2545 · Sitzung `20260918_225920_3e614670` · 122 B

```text
Punkt 4: Doppelungsschlüssel auf die Behauptung. Zuerst sehe ich mir die Stelle an, die (Meldungsklasse, Ort) vergleicht.
```

### V0318 · 19.09.2026 22:36:47 CEST · Hermes-Zwischentext · Nachricht id 2547 · Sitzung `20260918_225920_3e614670` · 130 B

```text
Ich baue den Schlüssel als Behauptung: aufgerufene Werk-Funktion plus normierte Zusicherung, beides aus dem Syntaxbaum des Tests.
```

### V0319 · 19.09.2026 22:36:55 CEST · Hermes-Zwischentext · Nachricht id 2549 · Sitzung `20260918_225920_3e614670` · 75 B

```text
Eine tote Schleife ist beim Schreiben stehengeblieben — die entferne ich.
```

### V0320 · 19.09.2026 22:36:59 CEST · Hermes-Zwischentext · Nachricht id 2551 · Sitzung `20260918_225920_3e614670` · 96 B

```text
Jetzt die Aufrufstelle: Sie muss den Testcode übergeben und den Schlüssel im Ursprung ablegen.
```

### V0321 · 19.09.2026 22:37:45 CEST · Hermes-Zwischentext · Nachricht id 2557 · Sitzung `20260918_225920_3e614670` · 109 B

```text
Jetzt Tor 2 Zeile 8 neu messen — mit dem neuen Schlüssel an den echten Ankläger-Tests aus Lauf 13 und 20.
```

### V0322 · 19.09.2026 22:38:01 CEST · Hermes-Zwischentext · Nachricht id 2561 · Sitzung `20260918_225920_3e614670` · 152 B

```text
Der Schlüssel arbeitet, aber Zeile 8 reißt in beiden Läufen — 68,5 % und 63,6 % gegen die Grenze von 20 %. Das melde ich, statt es zu beschönigen.
```

### V0323 · 19.09.2026 22:38:16 CEST · Hermes · Nachricht id 2563 · Sitzung `20260918_225920_3e614670` · 2000 B

```text
**Punkt 4a erledigt: Doppelungsschlüssel ist die Behauptung** (`aegis.behauptung`, Beleg `ausgaben/13-doppelungen-behauptung.txt`).

Der Schlüssel wird aus dem Syntaxbaum gebildet: aufgerufene Werk-Funktion plus Zusicherungsart (`raises:<Ausnahme>` oder Vergleichsoperator plus Form der erwarteten Seite) — **ohne** den Zahlenwert. Er wird beim Fund in den `ursprung` geschrieben, damit spätere Kandidaten dagegen prüfen können.

**Teil A — die Phase-3-Falle:** Die sechs Tests, die `Katalog.wert` als Staffelpreis festschrieben, fallen jetzt auf **eine** Behauptung (`Staffel|Eq:zahl`, 20 Vorkommen über alle Werk-Kopien). Mit diesem Schlüssel wären fünf davon nie einzeln ins Immunsystem gekommen — und der K1165-Fehler hätte keine fünf Wächter gehabt.

**Tor 2 Zeile 8, neu gemessen — gerissen, in beiden Läufen:**

| Lauf | erzeugte Tests | alter Schlüssel | neuer Schlüssel | Anteil | Grenze 20 % |
|---|---|---|---|---|---|
| 13 (Phase 2) | 54 | 6 Doppelungen = 11,1 % | 27 Behauptungen unter 48 → +31 | **68,5 %** | gerissen |
| 20 (jüngster) | 11 | 0 = 0,0 % | 4 Behauptungen unter 11 → +7 | **63,6 %** | gerissen |

Die 83,6 % aus meinem Phase-3-Bericht waren eine Heuristik; mit dem gebauten Schlüssel sind es **68,5 %**. Deine Wertung „Zeile 8 gerissen" bleibt damit richtig, die Zahl korrigiere ich.

**Was die Zahl bedeutet:** Sie misst die Vielfalt des **Anklägers**, nicht das Werk. Größte Gruppen in Lauf 13: `lager/reserviert|Eq:zahl` 8 Tests, `lager/bestand|Eq:zahl` 7, `preise/Staffel|GtE:zahl` 5. Der Ankläger schreibt also immer wieder dieselbe Zusicherung mit anderen Zahlen. Die 20-%-Grenze ist mit dem jetzigen Ankläger nicht erreichbar — ob die Grenze oder der Ankläger zu ändern ist, ist eine Entscheidung für Fassung 6; ich halte den Befund fest und ändere nichts eigenmächtig.

Noch offen in Punkt 4: die Nachmessung der vier Probenzeilen (Nebenwirkung, Regression, Norm, Vertrag) mit den gehärteten Proben — die laufen jetzt.
```

### V0324 · 19.09.2026 22:56:23 CEST · Philipp · Nachricht id 2564 · Sitzung `20260918_225920_3e614670` · 903 B

```text
Zahl korrigiert übernommen: 68,5 % gemessen statt 83,6 % geschätzt, Zeile 8 bleibt gerissen, Grenze bleibt bei 20 %. Deine Deutung entscheidet die offene Frage — der Anteil misst die Vielfalt des Anklägers, nicht das Werk, und acht Tests mit derselben Zusicherung über lager/reserviert heißen, dass zwei Drittel seiner Aufrufe nichts Neues bringen und trotzdem kosten. Also wird der Ankläger geändert, nicht die Grenze (Chat-Claude, Fassung 6): Ihm werden vor jedem Angriff die Behauptungen vorgelegt, die er in diesem Bereich schon aufgestellt hat, mit dem Auftrag, eine andere zu finden — das ist Text im ohnehin fälligen Aufruf und kostet nichts extra. Wirkt es nicht, ist das ein Befund über die Modelle und keine Einladung, die Grenze zu senken; die Neumessung derselben Zahl zeigt es. Einbauen und in einem Lauf messen, zusammen mit der noch offenen Nachmessung der vier Probenzeilen.
```

### V0325 · 19.09.2026 22:56:34 CEST · Hermes-Zwischentext · Nachricht id 2565 · Sitzung `20260918_225920_3e614670` · 90 B

```text
Der Ankläger bekommt seine bisherigen Behauptungen vorgelegt. Ich sehe mir den Aufruf an.
```

### V0326 · 19.09.2026 22:57:18 CEST · Hermes-Zwischentext · Nachricht id 2571 · Sitzung `20260918_225920_3e614670` · 127 B

```text
Der Altbestand trägt den Schlüssel noch nicht im Ursprung — ohne Nachtrag sähe der Ankräger im Messlauf eine leere Liste.
```

### V0327 · 19.09.2026 22:57:34 CEST · Hermes-Zwischentext · Nachricht id 2575 · Sitzung `20260918_225920_3e614670` · 165 B

```text
Der Ankläger sieht jetzt seine bisherigen Behauptungen. Jetzt der Messlauf — er prüft beides zugleich: die vier Probenzeilen und die Wirkung der neuen Anweisung.
```

### V0328 · 19.09.2026 22:58:24 CEST · Hermes-Zwischentext · Nachricht id 2579 · Sitzung `20260918_225920_3e614670` · 159 B

```text
Lauf 22 liegt an. Jetzt der vollständige Vorspann — Rauschmessung, Eichgegenstand, vier Proben, Fund-Neubewertung — als Nachmessung der vier Tor-2-Zeilen.
```

### V0329 · 19.09.2026 22:59:26 CEST · Hermes-Zwischentext · Nachricht id 2583 · Sitzung `20260918_225920_3e614670` · 163 B

```text
Vorspann vollständig, vier Tor-2-Zeilen nachgemessen. Jetzt der Messlauf für die Ankläger-Anweisung — Generationen, in denen er neue Behauptungen finden muss.
```

### V0330 · 19.09.2026 23:26:57 CEST · Hermes-Zwischentext · Nachricht id 2595 · Sitzung `20260918_225920_3e614670` · 103 B

```text
Vier Generationen durch. Jetzt die entscheidende Frage: Hat die Anweisung den Doppelungsanteil gesenkt?
```

### V0331 · 19.09.2026 23:27:54 CEST · Hermes · Nachricht id 2603 · Sitzung `20260918_225920_3e614670` · 2243 B

```text
**Punkt 4 erledigt, mit einem Teilerfolg und einer offenen Frage.**

**Die vier Tor-2-Probenzeilen, nachgemessen** (`ausgaben/15-vorspann-lauf22.txt`, Lauf 22, gehärtete Proben am versiegelten Gegenstand): **4 von 4 bestanden** — Nebenwirkung (abgelehnt, nennt `bericht`), Regression (gefallener Einzeltest benannt), Norm (0 Punkte, nicht im Werk), Vertrag (`Vertrag verletzt (Schritt 2)`). Die Zeilen sind damit wieder belegt, diesmal mit Proben, die mechanisch am Syntaxbaum ansetzen statt an Textankern. Kosten: 4 Modellaufrufe, 0,0057 €, 31 s.

**Die Ankläger-Anweisung wirkt — aber nicht genug** (`ausgaben/18-anklaeger-vielfalt.txt`):

| Lauf | erzeugte Tests | Behauptungen | Doppelungsanteil |
|---|---|---|---|
| 13 (vorher) | 54 | 27 | 68,5 % |
| 20 (vorher) | 11 | 4 | 63,6 % |
| **22 (Anweisung aktiv)** | 11 | **5** | **54,5 %** |

Aufschlussreicher als die Gesamtzahl ist die Verteilung: In Lauf 20 gab es **0** vom Ankläger selbst verworfene Doppelungen und Gruppen von 5 und 4 gleichen Tests. In Lauf 22 wurden **6 von 11** als Doppelung erkannt und verworfen, und die größte Gruppe hat nur noch **1** Test — jede aufgenommene Behauptung ist verschieden. Der Anteil bleibt hoch, weil die Doppelungen jetzt *sichtbar* werden, statt unbemerkt ins Immunsystem zu wandern; das ist die Wirkung des neuen Schlüssels, nicht ein Versagen der Anweisung.

**Ehrlich zur Grenze:** 54,5 % gegen 20 % — Zeile 8 bleibt gerissen. Die Anweisung hat die Wiederholungen nicht verhindert, nur ihre Aufnahme. Bemerkenswert: **0 Aufrufe** mit „KEIN ANGRIFF" in beiden Läufen — das Modell liefert lieber eine Wiederholung als nichts, obwohl die Anweisung ausdrücklich sagt, dass „nichts gefunden" kein Fehlschlag ist. Das ist nach deiner Festlegung ein **Befund über die Modelle**, keine Einladung, die Grenze zu senken. Die Zahl steht; ob die nächste Stufe ein anderer Anklägeraufbau ist (z. B. Behauptung vorab nennen lassen und bei Wiederholung gar nicht erst ausführen), gehört in Fassung 6.

Kosten: 0,39 € von 10 € (Lauf 22 mit 4 Generationen). Zwischenbericht: 35 Dateien, Prüfsumme `f795d53235cf95f64db9e952aa943c0d22d6d841753e37763f340991cb96d100`.

Weiter mit Punkt 5: Artgedächtnis auf Muster umstellen.
```

### V0332 · 19.09.2026 23:28:11 CEST · Hermes-Zwischentext · Nachricht id 2605 · Sitzung `20260918_225920_3e614670` · 127 B

```text
Lauf 22 bestätigt beendet (4 Generationen, alle abgelehnt) — Auswertung liegt schon vor. Punkt 5: Artgedächtnis auf Muster.
```

### V0333 · 19.09.2026 23:28:38 CEST · Hermes-Zwischentext · Nachricht id 2609 · Sitzung `20260918_225920_3e614670` · 74 B

```text
Jetzt der Abstraktionsaufruf und die Umstellung von `art_text` auf Muster.
```

### V0334 · 19.09.2026 23:29:00 CEST · Hermes-Zwischentext · Nachricht id 2615 · Sitzung `20260918_225920_3e614670` · 61 B

```text
Die alte Wertezeile ist stehengeblieben — ich entferne sie.
```

### V0335 · 19.09.2026 23:29:25 CEST · Hermes-Zwischentext · Nachricht id 2617 · Sitzung `20260918_225920_3e614670` · 95 B

```text
Jetzt `art_text`: werkübergreifend nur Muster, die Instanz bleibt als Beleg beim eigenen Werk.
```

### V0336 · 19.09.2026 23:29:43 CEST · Hermes-Zwischentext · Nachricht id 2619 · Sitzung `20260918_225920_3e614670` · 90 B

```text
Jetzt die Nachabstraktion beider Werke — 19 angenommene Änderungen bekommen ihr Muster.
```

### V0337 · 19.09.2026 23:29:58 CEST · Hermes-Zwischentext · Nachricht id 2623 · Sitzung `20260918_225920_3e614670` · 104 B

```text
Die Tabelle existiert schon — `CREATE TABLE IF NOT EXISTS` ergänzt keine Spalten. Ich trage sie nach.
```

### V0338 · 19.09.2026 23:30:50 CEST · Hermes-Zwischentext · Nachricht id 2639 · Sitzung `20260918_225920_3e614670` · 133 B

```text
0 von 19 und 0 Modellaufrufe — die Aufrufe kommen gar nicht durch. Ich prüfe die Ursache, statt „nicht übertragbar" zu glauben.
```

### V0339 · 19.09.2026 23:30:56 CEST · Hermes-Zwischentext · Nachricht id 2641 · Sitzung `20260918_225920_3e614670` · 89 B

```text
„Unbekannter Anbieter openai" — ich habe den Anbieternamen geraten statt nachzusehen.
```

### V0340 · 19.09.2026 23:31:17 CEST · Hermes-Zwischentext · Nachricht id 2645 · Sitzung `20260918_225920_3e614670` · 108 B

```text
Auch die stille Rückgabe war falsch: Ein Anbieterfehler ist kein „nicht übertragbar". Ich trenne beides.
```

### V0341 · 19.09.2026 23:31:59 CEST · Hermes-Zwischentext · Nachricht id 2649 · Sitzung `20260918_225920_3e614670` · 109 B

```text
18 Muster für 0,003 €. Jetzt die Torzeile erneut messen — ein Mentor-Aufruf mit Mustern statt Instanzen.
```

### V0342 · 19.09.2026 23:32:10 CEST · Hermes-Zwischentext · Nachricht id 2651 · Sitzung `20260918_225920_3e614670` · 122 B

```text
Der Block zeigt jetzt nur Muster. Messlauf: Mentor an einem `lagerhaus`-Lauf, nachdem `logmuehle` Muster beigesteuert hat.
```

### V0343 · 19.09.2026 23:32:41 CEST · Hermes-Zwischentext · Nachricht id 2653 · Sitzung `20260918_225920_3e614670` · 155 B

```text
Wieder 0 werkübergreifende Verweise — trotz Mustern. Der Ausgang ist `lagerhaus`, das eigene Projektgedächtnis ist riesig. Ich messe die Gegenrichtung.
```

### V0344 · 19.09.2026 23:32:55 CEST · Hermes-Zwischentext · Nachricht id 2655 · Sitzung `20260918_225920_3e614670` · 179 B

```text
Die Torzeile verlangt „nach Läufen an beiden Werken, bei einem dritten Lauf" — ein `logmuehle`-Lauf sieht 13 fremde Muster statt 3. Das ist die Richtung, die die Zeile meint.
```

### V0345 · 19.09.2026 23:34:10 CEST · Hermes-Zwischentext · Nachricht id 2659 · Sitzung `20260918_225920_3e614670` · 89 B

```text
**Die Torzeile Artgedächtnis ist erfüllt** — zum ersten Mal, nach drei Läufen mit 0.
```

### V0346 · 19.09.2026 23:34:39 CEST · Hermes · Nachricht id 2663 · Sitzung `20260918_225920_3e614670` · 2244 B

```text
**Punkt 5 erledigt — die Artgedächtnis-Zeile ist erfüllt, zum ersten Mal** (`ausgaben/23-artgedaechtnis-muster-messung.txt`).

**Gebaut:** `muster_bilden()` abstrahiert jede angenommene Änderung zu einem Satz ohne Werk-, Datei- und Funktionsnamen — ein Masse-Aufruf je angenommener Generation. `art_text()` zeigt werkübergreifend **nur** Muster; die Instanz bleibt als Beleg in der Datenbank, aber nicht als Vorlage.

**Nachabstraktion beider Werke:** 19 angenommene Einträge, **18 Muster gebildet**, 1 vom Modell als nicht übertragbar gemeldet. Kosten: 19 Aufrufe, **0,003 €**. Beispiel — aus „`Katalog.wert` nutzte `stueckpreis(menge)`" wird „Bei der Katalogbewertung den unveränderten Grundpreis verwenden, wenn Mengenrabatte ausdrücklich nicht berücksichtigt werden sollen."

**Die Messung:**

| Lauf | Richtungen mit werkübergreifendem Verweis | erfunden |
|---|---|---|
| 16, 17, 18, 19, 20, 22 (Instanzen) | **0** von je 4–5 | 0 |
| **23 (logmuehle, Muster)** | **2 von 5** — A132, A359, A249, A6, A141 | **0** |

Zwei Richtungen zitieren Muster aus `lagerhaus`: „extern_filtern sicher und korrekt zugleich lösen" (A132) und „Laufzeit von lesen und filtern über Caching senken" (A359, A249, A6, A141).

**Ein Zwischenergebnis, das ich nicht unterschlage:** Mein erster Messlauf war Lauf 22 am `lagerhaus` — dort wieder **0 von 4**. Grund, gemessen: Ein `lagerhaus`-Lauf sieht nur **3** fremde Muster, ein `logmuehle`-Lauf **13**. Die Zeile hängt also nicht nur an der Form der Einträge, sondern auch an ihrer Zahl. Beide Messungen stehen im Beleg nebeneinander.

**Zwei eigene Fehler unterwegs:** Ich hatte den Anbieter geraten (`openai` statt `openrouter`) — 19 Abstürze wurden als „nicht übertragbar" gezählt und hätten fast als Ergebnis gegolten. Behoben, und ein Aufruffehler wird jetzt geworfen statt still als inhaltliches Urteil verbucht. Außerdem: `CREATE TABLE IF NOT EXISTS` ergänzt keine Spalten an bestehenden Tabellen — die Muster-Spalten werden jetzt per `ALTER TABLE` nachgezogen.

Kosten: 0,42 € von 10 €. Zwischenbericht: 44 Dateien, Prüfsumme `9e8b3b9f76704747d5e91f9a9d5dfa71a94cef083a198ccd1fb222e0a93bc495`.

Weiter mit Punkt 6: Archivierung nach der neuen Zeile.
```

### V0347 · 19.09.2026 23:39:45 CEST · Philipp · Nachricht id 2664 · Sitzung `20260918_225920_3e614670` · 959 B

```text
Zwei Punkte für den Bericht, bevor du weitermachst. Erstens: Die Doppelungszahlen vor und nach dem Schlüsselwechsel zählen nicht dieselbe Menge — in Lauf 20 wanderten Wiederholungen unbemerkt ins Immunsystem, in Lauf 22 werden sie erkannt und verworfen; 63,6 → 54,5 liest sich sonst als kleine Verbesserung, obwohl 6 von 11 abgefangen wurden und die größte Gruppe von 5 auf 1 fiel. Bezugsgröße dazuschreiben, Zeile bleibt gerissen, Grenze bleibt. Zweitens für Fassung 6, aus deinem Artgedächtnis-Befund: Der werkübergreifende Block bekommt einen festen Mindestanteil an der Vorlage — ein logmuehle-Lauf sieht 13 fremde Muster, ein lagerhaus-Lauf 3, und ein Werk mit 17 Diensten verdrängt fremde Muster sonst allein durch die Masse eigener. Dein Vorschlag zum Ankläger (Behauptung vorab nennen, bei Wiederholung gar nicht ausführen) ist der richtige nächste Schritt und spart zusätzlich Aufrufe — ebenfalls Fassung 6. Weiter mit Punkt 6.
```

### V0348 · 19.09.2026 23:40:05 CEST · Hermes-Zwischentext · Nachricht id 2665 · Sitzung `20260918_225920_3e614670` · 89 B

```text
Beide Punkte notiert. Die Bezugsgröße trage ich sofort in den Beleg nach, dann Punkt 6.
```

### V0349 · 19.09.2026 23:40:30 CEST · Hermes-Zwischentext · Nachricht id 2671 · Sitzung `20260918_225920_3e614670` · 139 B

```text
Bezugsgröße steht im Beleg. Jetzt Punkt 6: Archivierung nach der neuen Zeile — Bezug sind Generationen, nicht angenommene Generationen.
```

### V0350 · 19.09.2026 23:41:27 CEST · Hermes-Zwischentext · Nachricht id 2677 · Sitzung `20260918_225920_3e614670` · 122 B

```text
Lauf 22 hat 4 Generationen — die Archivierung greift ab 5. Ich messe an einem erzeugten Fund, wie die Zeile es zulässt.
```

### V0351 · 19.09.2026 23:41:50 CEST · Hermes-Zwischentext · Nachricht id 2681 · Sitzung `20260918_225920_3e614670` · 147 B

```text
Die Prüfung hat zwei **echte** Normtests mitarchiviert — ein Nebeneffekt meiner Mechanikprüfung, nicht ein Laufergebnis. Ich setze sie zurück.
```

