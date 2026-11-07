# Review 03: abschluss-03 (T3 TypeScript) und Kern-Commit `f821707`

Ein Durchgang nach `REVIEW-AUFTRAG-03.md`, Stand 2026-09-23.

- **Geändert:** nur diese Datei. Hilfsskripte und ihre Ausgaben liegen unter `/tmp/review03/`.
- **Aufwand:** 0 Modellaufrufe, 0 Kammerläufe (erlaubt waren bis zu 3), 0 €.
- **Lauf-DB:** nur der Schnappschuss `/root/biotop-t3/schnappschuss-abschluss3/t3.db`, geöffnet mit `mode=ro`. Seine sha256 war vor und nach allen Lesungen gleich (`7a31b8a3…2b37`).
- **Sperren:** Die Ausführungsschicht hat einmal gesperrt, bei einer Selbstkontrolle dieser Datei (Wortlaut und Befehl in Abschnitt 4). Ich habe den Befehl weder umformuliert noch das gespeicherte Skript ausgeführt; diese eine Prüfung fehlt. Außerdem lief ein Lesebefehl länger als 600 s und wurde deshalb als Hintergrundprozess geführt. Er lief unverändert zu Ende; das ist keine Sperre.

**Ergebnis: 21 Befunde, davon 3 hoch, 9 mittel und 9 niedrig.**

- Die Zahlen des Berichts halten der Nachrechnung fast durchweg stand (Abschnitt 2: 50 Prüfpunkte).
- **Falsch** ist der Annahmegrund von K3091. **Irreführend** ist die Erklärung, warum der Verhaltensvergleich K3106 übersah.
- **Im Code** macht der Verhaltensvergleich aus „nichts beobachtet“ und aus „Sonde abgestürzt“ ein Urteil über den Kandidaten.

## 1. Befunde

| Nr | Schwere | Befund | Beleg | Vorschlag |
|---|---|---|---|---|
| 1 | hoch | **K3091 wurde in Lauf 38 nicht für S2 angenommen, sondern für 2 Punkte der Fehlalarm-Regel.** Die 13er-Tabelle nennt als Annahmegrund „S2“. Aufgezeichnet ist „Nische schnell: Kernmaß −19 → −17“, ohne Laufzeitgewinn. Die paarweise Messung des Laufs ergab `planung` −11,2 %, also weniger als 15 %. Mit Eichung (Zuwachs 0) hätte dieselbe Messung zur Ablehnung geführt: durch ein Grenzmaß oder durch „Laufzeit nicht um ≥ 15 % gesunken“. K3091 ist damit derselbe Fall wie K2904 (Lauf 37: −18,4 %, Nachspiel: −13,7 %) und nicht dessen Gegenbeispiel. Dass K3091 im Nachspiel überlebt (3 von 3), hängt an der Einzelmessung: 3 von 4 Messungen liegen bei ≥ 15 %, 1 von 4 darunter. Zu stark sind deshalb: der Kopf („die vier echten Behebungen … angenommen“), §2 „Warum K2904 scheitert und K3091 nicht“, 4c und §7 („alle vier überleben“) sowie „5 von 13 … einziger Gewinn waren Punkte der stillgelegten Regel“. Nach dem Annahmegrund sind es 6 von 13. | Schnappschuss `protokoll` nr 23639 (`aegis.urteil` K3091): `zuwachs` 2, `laufzeit_gewinne` [], `sicherheit_gesunken_in` ['planung']. `kandidaten.masse` K3091: planung 9,270 → 8,236 ms. K2904 Urteil 21416: 9,418 → 7,690 ms (−18,4 %). Nachspiele K3091: −20,7 / −16,5 / −30,3 %. messgeraet.py:571-574. ABSCHLUSS-03.md:12, 89, 93-103, 114, 126-129, 217, 316 | Annahmegrund berichtigen. K3091 in §2 und §6 neben K2904 als messabhängigen Fall führen. Kopf, 4c und §7 abschwächen: „überleben das Nachspiel 4 von 4; K3091 nur, solange die Laufzeitmessung über 15 % liegt (Lauf: −11 %)“. Die Kategorie „nur Fehlalarm-Punkte“ mit 6 von 13 und mit ihrem Schnitt nennen. |
| 2 | hoch | **Der Verhaltensvergleich urteilt „keine Verhaltensabweichung“, auch wenn er keine Funktion des geänderten Moduls beobachtet hat.** K3106 (ohne Eichung): 7 Funktionen von `bericht/tabelle` waren eingewickelt, 0 davon wurden gerufen. Die 6 „Beobachtungen“ sind nur die Korpuszeilen. Trotzdem lautet das Ergebnis `geurteilt` und `tragfaehig`, und der Neutralzähler bucht „geurteilt“. `unbeobachtet` wird ausgegeben, aber nie gewertet. Folge: Jede Verhaltensänderung in einem Modul, das die Referenzlast nicht aufruft, besteht. Die Mehrheitsregel des Organs wird dabei mit Schweigen erfüllt. Die Erklärung des Berichts („die Referenzlast … enthält keine solche Tabelle“) passt nicht zum Beleg: Laut `unbeobachtet` (7 von 7) wurde keine Funktion des Moduls überhaupt aufgerufen, nicht nur keine mit leerer Tabelle. Gezählt wird dabei nur die äußere Aufrufebene; `verhalten.mjs` habe ich nicht im Einzelnen gelesen. Beobachtet wurden in anderen Nachspielen: K3240 1 von 7 Funktionen, K3030 2 von 7, K2934, K3121 und K3324 je 3 von 7 (darunter ist `spannweite` unbeobachtet, die Funktion aus 4d), K2868 7 von 10, K3044 1 von 1, K3091 4 von 4. | `nachspiel/l38_k3106_ohne_eichung.json`: `verhalten.beobachtungen` 6, `eingewickelt` 7, `unbeobachtet` 7, `grund_art` geurteilt, `neutralzaehler` art geurteilt. verhaltensvergleich.py:212-232 (Z. 220-223 bilden `unbeobachtet` nur für die Ausgabe). ABSCHLUSS-03.md:141, 311 | Fehlt die Beobachtung einer geänderten Funktion oder des ganzen Moduls, den Fall als neutral mit Grund `unbeobachtet` buchen, nicht als Beleg für Gleichheit (so verlangt es schon der eigene Docstring, Z. 48-49). „x von y Funktionen beobachtet“ in Urteil und Protokoll schreiben. §2 und §7 berichtigen. |
| 3 | hoch | **Stürzt die Sonde ab, wird der Kandidat abgelehnt, auch wenn der Fehler bei der Infrastruktur oder an der Vorgeneration liegt, und die Ablehnung landet im Projektgedächtnis.** (a) `beobachten` fängt `TypeScriptFehler` ab (Kammerabbruch, Zeitlimit, rc ≠ 0, beschädigter Transport) und liefert `art='infrastruktur'`. `pruefen` macht daraus `tragfaehig=False`, und `aegis.pruefen` lehnt ab („Verhaltensvergleich: Sonde … nicht ausführbar (infrastruktur)“). (b) Scheitert die Sonde schon an der Vorgeneration, gleich mit welcher `art`, wird ebenfalls der Kandidat abgelehnt, obwohl er dort gar nicht beteiligt ist. (c) Über `gedaechtnis.projekt_merken` geht die Ablehnung ins Projektgedächtnis. Ihre Grundklasse ist „sonst“, nicht „technisch“. Sie sperrt deshalb ähnliche spätere Kandidaten als „Wiederholung eines gescheiterten Wegs“. So wird aus einem ausgefallenen Messgerät ein Urteil über den Inhalt des Kandidaten und seiner Nachfolger. Am Kandidaten gilt auch ein Kammer-Zeitlimit ausdrücklich als Befund über den Kandidaten. Dieselbe Figur gibt es schon bei der Messung („Kammer (Vorgeneration): …“ → abgelehnt, aegis.py:829-831). Der Commit fügt eine weitere Stelle hinzu, statt die bereits unterschiedene `art` zu nutzen. Nicht ausgeführt; aus dem Code gelesen. | verhaltensvergleich.py:168-169, 200-211. typescript.py:42-55. aegis.py:829-831, 871-874. lauf.py:305-306. gedaechtnis.py:135-153, 238. ABSCHLUSS-03.md:38-39 | `art='infrastruktur'` und jedes Scheitern an der Vorgeneration als eigenen Ausgang behandeln: Lauf anhalten oder Kandidat zurückstellen, kein Eintrag ins Gedächtnis. Ein Zeitlimit am Kandidaten nur dann als Inhalt werten, wenn die Vorgeneration im selben Zeitlimit lief. Die Klasse in einem Zug fegen, die Messung eingeschlossen. Gegenprobe mit gestelltem Kammerabbruch. |
| 4 | mittel | **Das Nachspiel belegt „überlebt `aegis.pruefen`“; der Bericht schreibt „angenommen“.** Der Auftrag nennt die Funktion selbst „Annahmepfad“. Für die Ablehnungen genügt das, denn eine Ablehnung dort ist endgültig. Für „angenommen“ genügt es nicht. Nachgespielt wird nur `aegis.pruefen`. Nicht durchlaufen werden: die Vorprüfung durch das Projektgedächtnis, `_verhandeln` (K2868 wird direkt als `extra_code` übergeben), die Auswahl je Bereich samt Jury, die Generalprobe (mit eigenem 15-%-Nischenmaß auf einer weiteren Einzelmessung) und die Freigabe. Gestellt sind außerdem die Anbietergrenze (21 von 33 Fällen ohne Angriff), die Immuntests, die ausgeblendeten Generationen und die Eichung der Läufe vor dem Einbau; `vorspann.verlangen` wird umgangen. | nachspiel.py:147, 156-164, 177-182, 229-231. lauf.py:270-280, 290, 311-326, 361-367. ABSCHLUSS-03.md:12, 88-89 („K2868 angenommen“, „S2-Beschleunigung angenommen“) | „überlebt den Annahmepfad (`aegis.pruefen`)“ statt „angenommen“ schreiben. Die nicht nachgespielten Stufen in §2 unter „gestellt/ausgelassen“ aufzählen. |
| 5 | mittel | **Im Verhandlungspfad beendet eine Ablehnung durch den Verhaltensvergleich die Suche nach einer passenden Anpassung.** `paar_ok` prüft nur `vertrag_verletzt`, `pareto_schlechter` und `grenzen_gerissen`. Nach einer Ablehnung durch den Verhaltensvergleich sind alle drei leer, `paar_ok` ist also wahr. Die Schleife endet, die zweite Anpassung des Nachbarn wird nicht mehr geprüft, und das Protokoll schreibt `verhandlung.bestanden` an einen abgelehnten Kandidaten. „Bestanden ≠ angenommen“ ist bei Kernmaß-Ablehnungen so gewollt. Eine ungedeckte Verhaltensabweichung ist aber ein Mangel des Paars, wie eine Vertragsverletzung. Eine falsche Annahme entsteht nicht. Möglich ist eine falsche Ablehnung, weil eine verhaltensgleiche zweite Anpassung nie versucht wird. Nicht ausgeführt. | lauf.py:604, 611-620, 626-631. aegis.py:871-874 | `paar_ok` zusätzlich an `verhalten.tragfaehig` binden (nicht an „überlebt“, sonst ändert sich die gewollte Bedeutung). Test mit einer Ablehnung durch den Verhaltensvergleich im Verhandlungspfad. |
| 6 | mittel | **Der Verdrahtungstest belegt „aufgerufen“, nicht „wirkt im Generationslauf“.** (a) Die Pflichtkante `masseichung.anwenden ← aegis:pruefen` entsteht laut Code auch schon im Vorspann: `vorspann` reicht `tausch` mit `_masseichung` an `eichproben.proben` weiter, und das ruft `aegis.pruefen`. Die Kanten tragen keine Phase. Ein Lauf, in dem `_generation_koerper` die Eichung nicht mehr erreicht, bliebe also grün, solange die Eichproben laufen. Die Pflicht-Gegenprobe entfernt den Aufruf in `aegis.pruefen` selbst und trifft damit beide Phasen zugleich; sie kann diesen Fall nicht unterscheiden. (b) Kein Test verlangt, dass eine ungedeckte Abweichung über `aegis.pruefen` zur Ablehnung führt. Die Modultests prüfen nur `tragfaehig`. (c) Als „gerufen“ zählt jede Funktion, auch ein Kontextsetzer. Erster Aufruf ist z. B. `generation0.zaehlkontext_setzen` bzw. `gedaechtnis.zaehlkontext_setzen`; von `mentor` wird im ganzen Lauf 1 Funktion gerufen. (d) Ein Aufruf ist keine Wirkung. Ein `tausch` ohne `_masseichung` (etwa durch einen Fehler in `annahme_tausch`, also die Form des Lauf-38-Befunds) bliebe grün: `anwenden` wird dann mit `None` gerufen, und die Kante entsteht trotzdem. Im Drahtwerk ist `beta` der saubere Bereich (drahtwerk.py:92). `src/beta/wert.ts` enthält nur `halb` und `plus`, eine stillgelegte Regel ist also nicht zu erwarten. Dann kehrt `anwenden` sofort zurück (masseichung.py:112). Die Eichung steht nicht im Beleg; nicht ausgeführt. | vorspann.py:185-189. eichproben.py:507. aegis.py:834-836. drahtwerk.py:35-36, 92. masseichung.py:112. test_verdrahtung.py:57-76, 89-91, 250-254. `VERDRAHTUNG-BELEG-REGRESSION.json`: 254 Kanten, keine davon mit Phase. `git grep 'Verhaltensvergleich:' f821707 -- tests/`: 0 Treffer | Die Pflichtkanten an die Phase `lauf.generation` binden und dafür den Aufrufstapel mitschreiben. Im Drahtwerk eine Regel im sauberen Bereich anschlagen lassen und verlangen, dass sie im gespeicherten Maß der Generation stillgelegt ist. Gegenprobe „`annahme_tausch` ohne `_masseichung`“. Ein Test am Laufweg mit einer gestellten ungedeckten Abweichung, der die Ablehnung „Verhaltensvergleich:“ verlangt. |
| 7 | mittel | **§6 zählt Laufzeit-Grenzmaß-Ablehnungen nicht mit, die über das Projektgedächtnis weitergetragen wurden.** Gezählt wird nur ein Grund, der mit „Grenzmaß gerissen“ beginnt. „Wiederholung eines gescheiterten Wegs … damals: Grenzmaß gerissen: ….laufzeit_ms“ hat dieselbe Ursache, nur zeitlich verschoben. Lauf 38: 24 direkt + 17 über das Gedächtnis = 41 von 207 Ablehnungen. Nach dem gekürzten Grundtext lagen davon 34 nur außerhalb des eigenen Bereichs. Lauf 37: 19 + 2 = 21 von 139. Das Gedächtnis verstärkt also den Rauschbefund; der Bericht erwähnt das nicht. | zusatz_abschluss3.py:43. Schnappschuss `kandidaten` (lauf_id 38, status abgelehnt, Grund enthält „Grenzmaß gerissen“ und „.laufzeit_ms:“): 41 = 24 + 17. Lauf 37: 21 = 19 + 2. gedaechtnis.py:135-153 (Klasse „grenzmass“ sperrt) | §6 und §7 um den Weg über das Gedächtnis ergänzen, beide Zahlen mit Nenner. Frage für Philipp: Sollen Laufzeit-Grenzmaß-Ablehnungen überhaupt als gescheiterter Weg sperren? |
| 8 | mittel | **4e erklärt den Doppelungsanteil für nicht gemessen, ordnet aber die in NACHTRAG-02 veröffentlichte Zahl nicht ein.** NACHTRAG-02 §3 meldete für Lauf 37 „20 von 57 = 35,1 %, Schwelle gerissen“. Das ist die Ansage-Stufe. Nach der Lesart von 4e misst diese Zahl eine andere Stufe als die Torzeile. Das steht im Bericht weder als Rücknahme noch als Abgrenzung. Für Lauf 38 lässt sich die Ansage-Stufe messen: 29 von 91 Ansagen mit Behauptung = 31,9 % (107 Ansagen, davon 16 ohne Behauptung). | NACHTRAG-02.md:102-117. Schnappschuss `protokoll`, art `aegis.ansage`: Lauf 37 73/16/57/20 = 35,1 % (bestätigt), Lauf 38 107/16/91/29. ABSCHLUSS-03.md:231-237, 317 | In 4e beide Stufen mit Nenner nennen und festhalten, welche davon die Torzeile ist. Das Verhältnis zu NACHTRAG-02 ausdrücklich klären. |
| 9 | mittel | **Unbenannte Korrektur zu NACHTRAG-02: In Lauf 37 änderten 4, nicht 3 angenommene Generationen den sauberen Bereich.** Auch K2867 (Gen 3, Bereich `zahlen`, Paar mit K2868 für S1) ändert `src/zahlen/geld.ts`. 4d wertet Lauf 38 wie Lauf 37 aus („3 von 8“), berichtigt aber die Lauf-37-Zahl aus NACHTRAG-02 nicht. | Schnappschuss `kandidaten`, lauf_id 37, status angenommen, Diff mit `+++ b/src/zahlen/`: K2823, K2847, K2867, K2934, also 4 von 6 angenommenen Generationen ohne Gen 0. `nachspiel/k2868.json`: Modul `zahlen/geld`. NACHTRAG-02.md:17, 21-25 | Als Korrektur in abschluss-03 aufnehmen. K2867 einordnen (Vertragsanpassung zu S1). |
| 10 | mittel | **Aus dem LAUF38-BERICHT ist nur „deutlich besser als Lauf 37“ zurückgenommen.** Zwei Aussagen bleiben stehen. Erstens: „Das Messgerät trägt. Kernmaß halbiert und nochmals halbiert (−28 → −6)“. Dagegen steht: Bereinigt bewegten 7 von 8 angenommenen Generationen das Maß um 0, und 6 von 13 Annahmen ruhten allein auf Punkten der Fehlalarm-Regel (Nr. 1). Zweitens: „9 von 17 Generationen angenommen“. Dort ist Gen 0 im Zähler enthalten, im Nenner nicht; richtig ist 8 von 17, wie Z. 8-9 desselben Berichts selbst sagt. | LAUF38-BERICHT.md:8-9, 108-110. Schnappschuss `generationen` lauf_id 38. ABSCHLUSS-03.md:185-186 | Beide Aussagen ausdrücklich zurücknehmen bzw. berichtigen. |
| 11 | mittel | **4b beantwortet Auftrag (4) für 4 von 11 Punkten nicht, und „belegte bloße Umformung“ ist für K3324 zu stark.** K3045, K3212 und K3260 sind „nicht selbst gemessen“. Die Kammerprobe aus `zusatz_abschluss3.py` stand dafür bereit; sie wurde für K3106 benutzt und kostet 0 €. Der Beleg für K3324 ist der Verhaltensvergleich, und der beobachtete nur 3 von 7 Funktionen von `zahlen/statistik`. Nicht beobachtet wurden `spannweite`, `median`, `histogramm` und `gewichteterMittelwert`. | ABSCHLUSS-03.md:197-201. `nachspiel/l38_k3324_ohne_eichung.json`: `verhalten.unbeobachtet` 4 von 7 | Die drei Fälle mit derselben Kammerprobe messen. K3324 als „Umformung im beobachteten Teil (3 von 7 Funktionen)“ kennzeichnen. |
| 12 | mittel | **Die Nebenwirkungen der Eichung auf Schwarm und Ankläger sind nicht benannt.** Die Generalprobe speichert die geeichte Messung als Maß der Generation, ebenso `mass_einfrieren` für Gen 0. Daraus liest der Schwarm seine „statischen Befunde“ und der Ankläger seine Befundklassen. Stillgelegte Befunde fallen damit aus der Aufgabe des Schwarms und aus der Modellwahl heraus, denn das schwere Angriffsmodell wird nur bei Befundklassen gewählt. In Lauf 37 und 38 griff der Ankläger `zahlen` wegen `detect-object-injection` mit dem schweren Modell an (Nachspiel-Beleg K2934: Ansage an `anthropic/claude-sonnet-5`). Ein Lauf mit `f821707` greift dort mit dem leichten Modell an. Damit ändern sich Angriffsstärke und Kosten. Das Nachspiel bildet das nicht ab, weil seine Vorgeneration die ungeeichte Aufzeichnung ist. | lauf.py:102, 261, 349-351, 414-417. aegis.py:500-503, 532, 675, 726-727. nachspiel.py:185. `nachspiel/k2934.json`: `anbietergrenze` | Nebenwirkung in §1 benennen. Philipp entscheiden lassen, ob Befundklassen und Schwarm die rohe oder die geeichte Messung lesen. |
| 13 | niedrig | „`lauf.annahme_tausch` ist die einzige Stelle, die diesen Aufbau für den Lauf … herstellt“: Das stimmt nicht ganz. Der Vorspann gehört zum Lauf, baut den Aufbau für die Eichproben aber selbst, und die rufen ebenfalls `aegis.pruefen`. | vorspann.py:161-166, 186. eichproben.py:507. ABSCHLUSS-03.md:27-28 | „einzige Stelle für die Generationen und das Nachspiel; den Aufbau für die Eichproben baut der Vorspann selbst“ schreiben. |
| 14 | niedrig | „Echte Modellaufrufe: 0“ ist im Beleg eine fest eingetragene Konstante, keine Zählung. Die Aussage stützt sich tatsächlich auf die Netzsperre und die gestellte Grenze (33 von 33 Anfragen gingen an die Grenze). | nachspiel.py:71-85, 265. ABSCHLUSS-03.md:61 | „Netz gesperrt, gestellte Grenze“ schreiben oder die Kasse vor und nach dem Nachspiel zählen. |
| 15 | niedrig | Der Bericht nennt `NACHSPIEL-BELEGE.json` als Beleg, doch die Datei fehlt im Ordner. Sie entsteht erst beim Veröffentlichen. | ABSCHLUSS-03.md:80. abschluss03_veroeffentlichen.py:117. `ls abschluss3/NACHSPIEL-BELEGE.json`: No such file | Die Einzelbelege `nachspiel*/…json` nennen oder das Bündel vorher erzeugen. |
| 16 | niedrig | „Keiner der 33 Kandidaten“: Es sind 33 Fälle mit 16 verschiedenen Kandidaten. | 33 Belege, 16 verschiedene `kandidat`. ABSCHLUSS-03.md:71 | „keiner der 16 Kandidaten (33 Fälle)“ schreiben. |
| 17 | niedrig | In 2 von 16 Kandidaten weicht der Zustand im Nachspiel vom Zustand bei der Entscheidung ab. K3045: roh −28 → −27 (im Lauf −29 → −28). K2867+K2868: −20 → −16 (im Lauf −21 → −17). Beide Seiten liegen um +1 höher, der Zuwachs ist gleich. Vermutlich fehlt der Angriffstest, der im Lauf entstand und auf beiden Seiten fiel. Für K3045 steht dazu der Immuneintrag `aegis_k3045_zahlen` im Schnappschuss. Der Bericht nennt nur K3044 und K3240. | `nachspiel/l38_k3045.json`, `nachspiel/k2868.json`: `kernmass_*.kernmass_roh` gegen `grund_aufgezeichnet`. Schnappschuss `immunsystem` lauf_id 38 | Die Abweichung und ihre vermutete Ursache benennen. |
| 18 | niedrig | §1: „Jeder Aufruf einer exportierten Funktion … wird aufgezeichnet“ stimmt so nicht. Aufgezeichnet werden je Funktion die ersten 8 äußeren Aufrufe (KAPPE); verschachtelte Aufrufe werden nicht beobachtet. | verhaltensvergleich.py:37. verhalten-runner.mjs:110-112. ABSCHLUSS-03.md:30-31 | „die ersten 8 äußeren Aufrufe je Funktion“ schreiben. |
| 19 | niedrig | §5: Die Sperre „lautete am 22.09. und am 23.09. gleich“. Der Wortlaut vom 23.09. ist aber nicht wiedergegeben, und er unterscheidet sich mindestens im Skriptpfad. | SPERREN.md:18 (`blocked-1790137630-993130dd.sh`). ABSCHLUSS-03.md:272-277 | „gleich bis auf den Skriptpfad“ schreiben und beide Pfade nennen. |
| 20 | niedrig | `masseichung.anwenden` erkennt „schon geeicht“ nur am Marker und vergleicht die Eichung nicht. Eine Messung mit einer anderen Eichung bliebe still unverändert. Heute wirkt sich das nicht aus, weil es je Lauf nur eine Eichung gibt. | masseichung.py:112 | Den Marker mit der übergebenen Eichung vergleichen; bei Abweichung Fehler auslösen. |
| 21 | niedrig | Protokollfeld: `anwenden` bildet nur `sicherheit_punkte` je Bereich neu. Das Feld `kernmass` bleibt roh; im TS-Messgerät ist es die rohe F2-Summe. `mass.eingefroren` und `generation.ergebnis` schreiben es als `kernmass_f1` neben das geeichte `kernmass_f2`. Ein Leser des Protokolls sieht so zwei Kernmaße aus verschiedenen Zählungen, ohne Kennzeichnung. | masseichung.py:103-126. ts/messen.mjs:50. lauf.py:129, 234 | `kernmass` in `anwenden` mitführen oder im Protokoll als `kernmass_roh` kennzeichnen. |

## 2. Geprüft und bestätigt

Zeichen: ✓ = gegen die Quelle nachgerechnet oder nachgezählt. ✓* = bestätigt, mit Einschränkung (Verweis auf den Befund). „gelesen“ = nur aus dem Beleg gelesen, nicht nachgemessen.

**Stand: 50 Prüfpunkte.** 40 sind ohne Einschränkung bestätigt, 10 mit Einschränkung (✓*). Keine nachgerechnete Zahl weicht vom Bericht ab; ausgenommen ist der Annahmegrund von K3091 in Punkt 23.

**A. Zahlen aus DB-Schnappschuss und Belegen (13)**

1. ✓ Kasse Läufe 26–38: 2603 Buchungen, 9,728637 €.
2. ✓ 4a, alle vier Zeilen: −28/−14/14, −11/0/11, −28/−6/22, −11/0 ab Gen 1/11. Bereinigt 0 in 7 von 7 Generationen nach Gen 1.
3. ✓ 4b: Sicherheitspunkte 27 → 6 = 10 + 11. Gen 0 hat 17 Punkte der Regel. Je Kandidat 1+2+3+2+1+2 = 11. Aufteilung 2+3+2+4 = 11.
4. ✓ gelesen: 4c S1–S5 mit 3 von 5 bzw. 4 von 5; S2 1560/6320/25440 → 80/160/320 (`S1S5-ABSCHLUSS3.txt`).
5. ✓ 4d: 3 von 8 angenommenen Generationen ändern `src/zahlen/` (K3045, K3121, K3324).
6. ✓ 4e: 306 Urteile, 61 mit Angriff, 87 Angriffstests, 9 Behauptungen, 0 Doppelungen.
7. ✓ 4f: 11 Einträge (10 archiviert, 1 `offen_norm`). 0 von 11 liegen im Endstand; im Lazarus-Archiv `lauf38-gen16` sind es 2 Immundateien. `_anhaengen` 0 Fälle.
8. ✓ 4g, Lauf 38: Vorspann-Ausgang 182 → 207 → 213; 17 von 100 blind, 10 neue Tests, danach 93 von 100 gefangen. Lauf 37: in Runde 1 und 2 je 0 von 100 gefangen, 200 neutral `typbau_nicht_bestanden`, 93 neue Tests, 440 bzw. 445. Lauf 38: 400 von 400 geurteilt. `generation0.py` ist zwischen `8c7dcdc` und `1cf2eb1` bytegleich.
9. ✓ 4h: 51/51, 400/400, 328/430 (102 neutral), 0/0, 0/0.
10. ✓ Lauf 38: 8 von 17 Generationen angenommen (ohne Gen 0).
11. ✓* §6: 19 von 139 (12 nur außerhalb) und 24 von 207 (17 nur außerhalb) gelten für die direkte Zählung; ohne den Weg über das Gedächtnis unvollständig (Nr. 7).
12. ✓ §7: 45 von 139 (42 + 3) und 56 von 207 (55 + 1).
13. ✓ K3121 knappster Fall: 3,821627 × 1,219 = 4,658563 < 4,660907, also 0,05 % darüber. Die Meldung rundet auf „4.7“.

**B. Nachspiele: 33 Belege nachgezählt (15)**

14. ✓ 33 Fälle (9 in Serie 1, 24 danach) mit 16 Kandidaten, 0 Fälle mit Fehler.
15. ✓ Anbietergrenze: 33 Anfragen, davon 12 aus der Aufzeichnung beantwortet und 21 abgebrochen.
16. ✓ Lazarus-Prüfsumme stimmt in 33 von 33. Die Quell-DB-Prüfsumme ist vor und nach gleich in 33 von 33. Die Referenzlast ist in 33 von 33 dieselbe wie im Lauf.
17. ✓ `detect-object-injection`: in 0 von 27 geeichten Fällen gezählt (weder bei Kandidat noch bei Vorgeneration), in 27 von 27 als stillgelegt ausgewiesen. Ohne Eichung in 6 von 6 gezählt.
18. ✓ K2934: 2 von 2 abgelehnt; 8 von 8 Abweichungen ungedeckt (`quantil#0–7@mutation`); 102 Beobachtungen.
19. ✓ K3121: 3 von 3 abgelehnt (2 durch den Verhaltensvergleich, 1 durch ein Grenzmaß). Ohne Verhaltensvergleich überlebt 2 von 2 (−66 %, −64 %).
20. ✓ K2934 ohne Verhaltensvergleich: überlebt 1 von 2; `eingang` 3,157 > 2,739 ms (2,307312 × 1,187).
21. ✓ Paar K2867+K2868: überlebt 2 von 2; geeicht −10 → 0.
22. ✓ K3091: überlebt 3 von 3. K2904: überlebt 0 von 2, ohne Eichung 2 von 2. Lauf 37 maß −18,4 %.
23. ✓* 13er-Tabelle: Ergebnis und entscheidender Grund stimmen in 13 von 13 Zeilen, der Annahmegrund in 12 von 13 (K3091 falsch, Nr. 1).
24. ✓* Aufteilung 4 + 5 + 1 + 3 = 13 geht auf; der Schnitt ist fraglich (Nr. 1).
25. ✓* Zusatzfälle K3106 und K3324: überleben mit 0 Abweichungen. Die Ursache bei K3106 ist irreführend erklärt (Nr. 2).
26. ✓ In 8 von 33 Fällen entschied ein Laufzeit-Grenzmaß; alle 8 Kandidaten hatten im Lauf überlebt.
27. ✓ In 11 von 29 Fällen mit eingeschaltetem Verhaltensvergleich gab es kein Verhaltensurteil.
28. ✓ 0 fremde Container in 24 von 24 Belegen nach Serie 1. In den 9 Belegen von Serie 1 fehlt das Feld.

**C. Commit und Belege am Commit-Stand (10)**

29. ✓ 13 Dateien, +1294/−63 (`git show --stat`).
30. ✓ gelesen: Regression 404 bestanden, 2 übersprungen, 93 abgewählt, 891 s. Für `1cf2eb1` laut Commit-Text 388/2.
31. ✓ Testsammlung 390 → 406; je Datei 6 → 10, 8 → 16, 0 → 4.
32. ✓ gelesen: Organtests gegen `1cf2eb1` 14 von 26 rot, 12 grün. Die beiden ROT-Dateien unterscheiden sich nur in der Laufzeitzeile (0,48 s gegen 0,21 s).
33. ✓ gelesen: Eichpfad 4 von 4, zweimal (512 s und 500 s).
34. ✓ gelesen: Zeitfolge 13:12 → 13:40; danach `git status` leer.
35. ✓ gelesen: Verdrahtung grün, 23 von 23; 254 Kanten; beide Pflichtkanten aus `aegis:pruefen`; 0 €; 1 Jury-Entscheidung.
36. ✓ gelesen: rot gegen `1cf2eb1` mit 21 von 23; es fehlen `masseichung` und `verhaltensvergleich` (Teststand vor der Pflicht).
37. ✓ gelesen: Die Pflicht-Gegenprobe ist rot mit genau der Pflichtmeldung; 23 von 23 gerufen; 673 s.
38. ✓ Prüfwerkzeug: Gegenproben 3 von 3. Die Organliste kommt aus dem Verzeichnis (23 Module). Der Test ist nicht als `integration` markiert; ohne Kammer greift `pytest.fail`.

**D. Code (d): aus dem Code gelesen, nicht ausgeführt (10)**

39. ✓ `aegis.pruefen` eicht beide Seiten vor `urteil_f2` (aegis.py:834-837).
40. ✓ Der Verhaltensvergleich läuft nur nach bestandenem Maß. Die Protokollfelder `verhalten` und `masseichung_stillgelegt` sind vorhanden (aegis.py:636-639, 856-875).
41. ✓* Der Neutralzähler bucht jeden Fall des Verhaltensvergleichs; wie aussagekräftig das ist, siehe Nr. 2.
42. ✓* Im Verhandlungspfad geht `extra_code` in `code` ein und damit in die vom Verhaltensvergleich geprüften Module (Beleg K2868: `tarife/ausdruck` + `zahlen/geld`). Zum Folgefehler siehe Nr. 5.
43. ✓ Die Generalprobe eicht beide Seiten; `mass_einfrieren` eicht; der Vorspann bildet die Eichung und versiegelt sie (lauf.py:99-103, 348-351; vorspann.py:185-186).
44. ✓* `anwenden` ist über den Marker idempotent (Einschränkung Nr. 20).
45. ✓ Grenzmaße nach der Eichung: Kernmaßgewinn und `sicherheit_gesunken` werden aus geeichten Werten gebildet (messgeraet.py:546-550). Der Satz im Bericht Z. 97-98 stimmt.
46. ✓ Die Eichung berührt den Bestwert nicht: `bestwerte` liest nur Laufzeit, größte Funktion, Zyklen und Bauzeit (messgeraet.py:471-491). `kernmass_f2` wird immer aus den Bereichen neu gebildet (messgeraet.py:349-350).
47. ✓ Das Messgerät ist zwischen `1cf2eb1` und `f821707` unverändert (`git diff` leer für messgeraet.py, typescript.py, ts/messen.mjs, kammer.py).
48. ✓* Das Nachspiel ruft `aegis.pruefen` mit `annahme_tausch`, `bestwert_des_laufs`, `letzte_angenommene` und `_referenzlast`, bei gesperrtem Netz. Grenzen siehe Nr. 4 und 17.

**E. Frühere Aussagen (2)**

49. ✓* NACHTRAG-02 §3: 20 von 57 = 35,1 % nachgerechnet; die Einordnung fehlt (Nr. 8).
50. ✓* LAUF38-BERICHT: „deutlich besser“ ist zurückgenommen, anderes nicht (Nr. 10).

## 3. Nicht geprüft

- **Keine eigenen Kammerläufe (0 von 3):**
  - kein Nachspiel wiederholt;
  - Verdrahtungstest, Regression und Organtests nicht selbst gefahren;
  - S1–S5 nicht selbst gemessen;
  - K3106 (3 von 50) sowie K3045, K3212 und K3260 nicht nachgemessen.

  Die Punkte 4 und 30–37 beruhen auf gelesenen Belegen. Die Befunde 3, 5 und 6(d) sind aus dem Code gelesen und nicht mit einer gestellten Gegenprobe ausgeführt.
- `REGRESSION-ABSCHLUSS3.junit.xml`: nicht je Testfall ausgewertet; ebenso wenig die Vollständigkeit der Sammlung je Datei gegen die Laufberichte.
- `KERN-COMMIT.patch.txt`: nicht bytegleich gegen `git show f821707` geprüft.
- `kern/ts/verhalten.mjs` (Einwickeln der Module): nicht im Einzelnen gelesen, nur `verhalten-runner.mjs`.
- Modultests `test_t3_masseichung.py` und `test_t3_verhaltensvergleich.py`: nur per Suche gelesen, nicht vollständig.
- Eichung „2 Regeln geprüft, 1 stillgelegt, 8 Funde in `zahlen`“: aus `AUSWERTUNG-ABSCHLUSS3.txt` gelesen, nicht mit `masseichung.eichen` nachgerechnet.
- 4g „10 Dateien, 25 Fälle“: nur die Differenz 207 − 182 = 25 geprüft, nicht die Aufteilung.
- `NACHTRAG-7-K3121.txt` („`spannweite` 8 statt 80“): nicht gelesen.
- §5 Sperren:
  - nur gegen `SPERREN.md` geprüft;
  - die gespeicherten Skripte liegen unter `/root/.hermes/cache/` und durften nicht gelesen werden.
- Lazarus-Archive von Lauf 37: nicht entpackt; Lauf 38 nur `gen16` gelistet.
- `abschluss03_veroeffentlichen.py`: nur auf die Belegbündelung geprüft.
- Maschinelle Selbstkontrolle dieser Datei (Zeilen je Schweregrad, Zahl der ✓-Punkte, sha256): gesperrt, siehe Abschnitt 4. Die Zahlen oben (21 Befunde = 3 + 9 + 9; 50 Prüfpunkte, davon 10 mit ✓*) habe ich beim Schreiben von Hand gezählt, nicht maschinell nachgezählt.

## 4. Sperre der Ausführungsschicht (wörtlich)

Befehl, wörtlich (eine Selbstkontrolle, rein lesend):

```
f=/root/biotop-t3/abschluss3/REVIEW-03.md; grep -c "^| [0-9]* | \(hoch\|mittel\|niedrig\) |" $f; for s in hoch mittel niedrig; do echo "$s: $(grep -c "^| [0-9]* | $s |" $f)"; done; grep -c "^[0-9]*\. ✓" $f; grep -c "^[0-9]*\. ✓\*" $f; sha256sum $f; ls -la /root/biotop-t3/abschluss3/ | wc -l
```

Meldung, wörtlich:

```
BLOCKED (hardline): command parser limit or malformed executable payload. This command is on the unconditional blocklist and cannot be executed via the agent — not even with --yolo, /yolo, approvals.mode=off, or cron approve mode. If you genuinely need to run it, run it yourself in a terminal outside the agent. RECOVERY: this block fires on oversized/unparseable inline command payloads (heredocs, giant one-liners), not on the operation itself. Your command was saved to /root/.hermes/cache/blocked-scripts/blocked-1790168621-64f4802c.sh — review it, then run: terminal(command="bash /root/.hermes/cache/blocked-scripts/blocked-1790168621-64f4802c.sh"). Do not retry inline.
```

Umgang: Der Auftrag verlangt, nicht umzuformulieren und nicht auszuweichen. Ich habe den Befehl deshalb nicht umformuliert und auch nicht anders ausgeführt. Das gespeicherte Skript unter `/root/.hermes/cache/` habe ich weder gelesen noch ausgeführt, denn dieser Ordner ist für diesen Durchgang gesperrt. Die Prüfung fehlt; sie steht unter „Nicht geprüft“.

## Anhang: kurze Antworten auf die Prüffragen a–f

- **a) Zahlen:** Siehe Abschnitt 2. Falsch ist der Annahmegrund von K3091 samt der Kategorie, die daran hängt (Nr. 1). §6 ist unvollständig (Nr. 7).
- **b) Am Laufweg?** Ja für die Annahmefunktion selbst: `aegis.pruefen` wird mit den Bausteinen aus `lauf.generation()` gerufen, nicht nachgebaut.
  - Nachgebaut bzw. gestellt sind: der DB-Zustand (ausgeblendete Generationen und Immuneinträge), die Eichung der Läufe vor dem Einbau, die Übergabe des Partners, die Anbietergrenze (21 von 33 ohne Angriff) und die Immuntests.
  - Das schwächt die Aussage „angenommen“ (Nr. 4) und den Zustand in 2 von 16 Kandidaten (Nr. 17). Die Nebenwirkung der Eichung auf die Modellwahl bildet das Nachspiel nicht ab (Nr. 12).
  - Das Messgerät ist gegenüber dem Lauf-Kern unverändert (Punkt 47).
- **c) Kann der Verdrahtungstest rot werden?** Ja, beide Rot-Nachweise sind belegt. Er belegt aber „gerufen“, nicht „wirkt im Generationslauf“. Ein Aufruf mit leerer Eichung bleibt grün (Nr. 6).
- **d) Codeprüfung:** Nr. 2, 3, 5, 12, 20 und 21. Bestätigt sind die Punkte 39–48.
- **e) Widersprüche und Korrekturen:** Nr. 8, 9, 10 und 19.
- **f) Lücken und zu starke Aussagen:**
  - zu Auftrag (2): Nr. 4;
  - zu Auftrag (3): Nr. 6;
  - zu Auftrag (4): Nr. 11;
  - zu starke Aussagen: Nr. 1, 2, 11 und 14.
