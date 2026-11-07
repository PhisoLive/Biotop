# Behebungsrunde vor T4: nicht abnahmereif — TS-Pfad gebaut; S1 an K2868 nicht sauber behoben, Verhaltensvergleich für Python fehlt, K2904/K3091 in 1 von 3 Durchgängen verschieden entschieden

Stand 2026-09-23, 22:30. **Biotop-Modellgeld 0,00 €** (`KASSE.md`). Kern-Commits **`58bd9f9`** (Vorbedingungen 1–11, Vorgänger
`f821707`) und **`330b4ec`** (Review-Befunde, 8 Dateien, +560/−47, `COMMIT2-STAT.txt`, `KERN-COMMIT2.patch.txt`). Ein
Reviewdurchgang (`REVIEW.md`) zu `58bd9f9`. Die Befunde sind in `330b4ec` eingearbeitet. Ein zweites Review gab es nicht,
nach der Regel „ein Review“. Diese Fassung ersetzt den Entwurf vom 18:18-Stand. Zurückgezogene Aussagen stehen in §8.

**Ich beantrage keine Abnahme als Vorbedingung für T4.** Drei Punkte sind nicht erfüllt:
1. **S1 an K2868 ist nach Philipps Maßstab nicht sauber behoben.** Mit Leerzeichen als Trenner rechnet der neue Parser
   jeden gültigen Ausdruck gleich: 0 Abweichungen in 93.320 Fällen, in denen der Vertrag eine Zahl liefert. Mit Tab oder
   Zeilenumbruch als Trenner weist er dagegen 12.206 von 16.166 Ausdrücken ab. Diese Ausdrücke rechnen die Vorgeneration
   und die versiegelte saubere Normalversion gleich (§2).
2. **Für T4 (Python) enthält sich der Verhaltensvergleich immer** (Review Nr. 8a). Die Tor-4-Zeile „Enthaltungen zählen
   nicht als bestanden“ ist damit für ein Python-Werk nicht erfüllbar. Alles in §1 gilt für den TypeScript-Pfad, soweit
   dort nicht anders vermerkt.
3. **Vorbedingung 1, Gegenprobe „K2904 und K3091 werden gleich entschieden“: gleich in 2 von 3 Durchgängen.**
   - Im Durchgang 2 am Commit `330b4ec` wurde K2904 abgelehnt: `eingang.laufzeit_ms` 3,078 > Grenze 2,985, gepaart
     gegen die Vorgeneration 2,514 × Toleranz 1,187.
   - `eingang` berührt der Kandidat nicht, und es importiert `planung` nicht.
   - In Durchgang 1 und 3 überleben beide (§4a).

**Ergebnis:**
- **Träger:**
  - `config.yaml` ist gesichert.
  - Grundwert jetzt `claude-opus-5-5` / `anthropic`. `agent.reasoning_effort: max` stand dort schon.
  - Im Anfragekörper einer echten Anfrage stehen `model: claude-opus-5-5`, `thinking: adaptive` und
    `output_config.effort: max`.
  - Die Verdichtungsroute antwortet wieder (§6).
- **Volle Regression am Commit `330b4ec`:** **475 bestanden, 2 übersprungen, 0 fehlgeschlagen, 0 Fehler**, 93 abgewählt (`integration`), 1267.94 s. JUnit: 477 Fälle, 0 fehlgeschlagen, 0 Fehler, 2 übersprungen (test_vier_paare_am_kopierten_pruefwerk: Private Werk-/DB-Kopie nicht angegeben; test_benannter_vertrag_am_kopierten_pruefwerk: Private Werk-/DB-Kopie nicht angegeben). Verdrahtungstest grün (4 von 4 Fällen in `test_verdrahtung.py`, der ganze Lauf 991 s; `VERDRAHTUNG-BELEG-REGRESSION2.json`). Arbeitsbaum vor und nach der Regression sauber (`git status` leer, `JOB-COMMIT2-REGRESSION.txt`). Zum Vergleich an `58bd9f9`: 451 bestanden, 2 übersprungen
- **Die 9 roten Spezifikationen aus `abschluss-03`:** Sie sind in beiden vollen Regressionen grün (an `330b4ec`: `test_t3_verhaltensvergleich.py` und `test_t3_masseichung.py` 34 von 34).
- **Gedächtnissperre-Test:** Er kann weiter rot werden, an der vorgesehenen Zusicherung (§3). Blind ist er gegen zweierlei:
  - den Verlust nur der Schreibstelle (die Lesestelle hält, wie beim Schwarm-2×2);
  - ein fehlendes TS-Kammerimage (dann 4 von 4 übersprungen).
- **Zwischenbericht-Wächter:** Er löst jetzt auch bei ≥ 80 % Kontext und bei der ersten gescheiterten Verdichtung aus.
  - Tests: 12 von 12 grün.
  - Gegenproben: 10 von 10 scheitern an der vorgesehenen Zusicherung.
  - Nachspiel an der gestorbenen Sitzung: Er hätte um 16:01 und um 16:48 ausgelöst. Der Rundenauslöser löste dort nie aus
    (höchste Runde 77 von 150, §5).
- **Nachspiele am Commit** (Review Nr. 7): 6 von 7 Fällen gleich entschieden wie im ersten Durchgang; Code-Stand im Beleg `330b4ec` mit sauberem Arbeitsbaum in 7 von 7; t3.db unverändert in 7 von 7 (`NACHSPIEL2-AM-COMMIT.txt`, `NACHSPIEL2-BELEGE.json`). Der abweichende Fall ist K2904, abgelehnt an einem Laufzeitriss im unberührten Bereich `eingang`. Ein dritter Durchgang (nur S2) ließ ihn überleben (§4a).

## 1. Vorbedingungen, Umsetzung und Nachweis (Stand `330b4ec`)

„Laufweg“ heißt: Der Nachweis geht durch die Funktion, die ein Lauf ruft. „Modul“ heißt: Das Organ wurde isoliert
gerufen. Review Nr. 5 hat verlangt, das je Zeile auszuweisen. In der Spalte „Umsetzung“ steht zusätzlich
**Geltung** (TS/Python).

| Nr | Vorbedingung | Umsetzung, Geltung | Probe (Nachweisart) | Gegenprobe (Nachweisart) |
|---|---|---|---|---|
| 1 | Laufzeit gepaart | `messgeraet.laufzeit_gepaart`: B K, K B …, je Seite 5, Median; nur wo die Laufzeit entscheidet; Dauer jetzt protokolliert (`dauer_s`). **TS belegt; Python-Zweig: in der Kammer ausgeführt (Werk lagerhaus, Image biotop-kammer:1, `PYTHON-LAUFZEIT-PROBE.json`): gleicher Stand gegen gleichen Stand gültig, 5 je Seite, 4 von 4 Bereichen, Verhältnis 0,964–1,062, 13,0 s. **Gegenprobe blind:** Ein Kandidat mit Syntaxfehler in `lagerhaus/formeln/auswertung.py` ergibt `gueltig True`, aber `kandidat None` in 3 von 4 Bereichen (`NACHLESE.json`); `laufzeit_einsetzen` überspringt fehlende Werte still. Rote Spezifikation `spez/test_spez_laufzeit_gepaart_teilausfall.py`: an `330b4ec` 1 rot, Gegenprobe grün. Der Codeweg ist sprachneutral; für TS gelesen, nicht ausgeführt. Der erste Probelauf traf ein Modul, das die Referenzlast nicht lädt (`PYTHON-LAUFZEIT-PROBE-lauf1.*`)** | Laufweg, drei Durchgänge: K2904 überlebt in 2 von 3 (Durchgang 2 an `330b4ec` abgelehnt: `eingang` ×1,224, unberührter Bereich, §4a), K3091 in 3 von 3; `planung` −16 % bis −23 % | Modul: am alten Weg reißt K3121s Laufzeit (3,8216 × 1,219 = 4,6586 < 4,6609), gepaart nicht. **Die „Vorgeneration 4,80“ im Test ist ein gestellter Wert, keine Messung** (Review Nr. 10a). Gemessen im Nachspiel: `bericht` 3,9975 → 3,9712 ms. Echte Verschlechterung ×2 reißt. Gepaarte Generalprobe: kein Test |
| 2 | Verhaltensvergleich, Randfall-Korpus, x von y | Korpus aus den deklarierten Signaturen der Vorgeneration. Nach Review Nr. 1: „entfernt“ aus den Beobachtungen beider Seiten bestimmt, y aus Signaturen. **Nur TS; für Python immer Enthaltung** | Laufweg: K3106 abgelehnt, 8 von 8 ungedeckt, 5 von 7 beobachtet; K2934/K3121 je 25 von 25 | Laufweg: K3324 überlebt, 0 Abweichungen. Modul: `export const f = () =>` gilt nicht mehr als entfernt; eine wirklich entfernte Funktion wird ausgewiesen, eine Änderung an g bleibt ungedeckt (`test_review1_*`, gestellt nur `beobachten`). **Grenze: Deckung wirkt je Funktion, nicht je Abweichung (§2)** |
| 3 | Sondenausfall zurückstellen | drei Ausfallarten → `ZURUECKGESTELLT`. Nach Review Nr. 3: Überwiegen Zurückgestellte, ist die Generation „abgebrochen“ (nicht gemessen) statt „abgelehnt“; zweimal in Folge → Lauf „angehalten“ | Laufweg, `aegis.pruefen`: Sonde, Messausfall Vorgeneration, gepaarte Laufzeit, je zurückgestellt (`test_3_…`, `test_review4_*`). Gestellt sind die Kammer, das Messgerät (`messen`, `laufzeit_messen`) und das Modell; die frühere Formulierung „nur die Kammergrenze“ war zu stark. Laufweg `_generation_koerper`: abgebrochen, kein Eintrag in die Entropie, danach angehalten, 0 Bandit-Zeilen (`test_review3_*`) | Laufweg: Inhaltsbefund bleibt Ablehnung; alles gültig → geurteilt; echte Ablehnung bleibt „abgelehnt (0 von 1)“. Abbruch der Generalprobe: kein eigener Test. „Kein Gedächtnis“ ist in `test_review3` nicht zugesichert, `projekt_merken` war dort gestellt |
| 4 | `paar_ok` an Verhaltensvergleich | `lauf.paar_bestanden` | Laufweg `lauf._verhandeln`: nicht tragfähig → `verhandlung.gescheitert` (`test_review5_verhandlung_am_laufweg`) | Laufweg: tragfähig → `verhandlung.bestanden` |
| 5 | Maßeichung vergleicht Eichung | `masseichung.anwenden` | Modul (Spezifikation) | Modul: andere oder leere Eichung → Fehler |
| 6 | G0: Mehrheit je Durchlauf, tsc-Meldung, Typbau zwischen den Runden | `G0.messen`, `G0.rundenpruefung` (neu, Review Nr. 9). **Python:** pytest-rc außer 0/1 ist jetzt neutral (Review Nr. 8c) | Laufweg `lauf.generation0`: Typbau bricht → `LaufFehler` mit tsc-Zeile, Ergänzung zurückgenommen (`test_review9`) | Laufweg: Typbau baut → weiter. Modul: rc 2/5 neutral, rc 1 und Zeitlimit gefangen, rc 0 nicht (`test_review8c`, 5 Fälle) |
| 7 | Verdrahtungstest | Phase, Wirkung, Laufweg-Ablehnung | ganzer Lauf über die Befehlszeile, grün in beiden vollen Regressionen | rot: **wirkung** (früher „phase“ genannt; Review Nr. 6 — sie prüft die Wirkung, die Phasenbindung ist nur am Prüfwerkzeug belegt), **vv**, **beide** (2×2, §4 Vorfassung) |
| 8 | Kernmaß geeicht, roh gekennzeichnet | `masseichung.anwenden` | Modul | Modul. Die Protokollfelder `kernmass_f2_roh` liest kein Test |
| 9 | Behauptungen aller Angriffstests; Immunisierung TS | nach Review Nr. 2: Importe nach Bindungen zusammengeführt, Konflikt → neutral; Nr. 12: Kammerausfall wird weitergereicht, der Kandidat zurückgestellt | Laufweg `aegis.pruefen`: `behauptungen` = alle 2 erzeugten Tests, `behauptungen_treffer` getrennt (`test_review5_behauptungen…`). Kammer: erweiterte Importzeile → jede Bindung genau einmal, geurteilt 1 (`test_review2_*`) | Kammer: Namenskonflikt → nichts angehängt, neutral. Kammerausfall → weder syntaxfehler noch sonst gezählt. **Das zusammengeführte Ergebnis wird geparst, nicht unter node ausgeführt** |
| 10 | Gedächtnissperre nur berührt und gepaart | Schreibseite (`projekt_merken`) und seit Review Nr. 11 **Leseseite** (`_sperrt` in `wiederholung`/`gescheiterte_wege`) | Laufweg `projekt_merken` + `wiederholung`; `gescheiterte_wege` mit Altbestand | §3: 2×2 und Regelbruch |
| 11 | Erreichbarkeit, Verfall, `_beschleunigen`, Rohwerte | wie `58bd9f9` | Laufweg `anbieter.aufrufen` → `nischen.waehlen`: 3 Drosselungen → qwen in 0 von 15 Wahlen (`test_review5_drosselung…`). Laufweg `eichung.rauschmessung`: Rohwerte in Messreihenfolge | Laufweg: Ablehnung ist keine Drosselung → qwen bleibt wählbar. `werte` ist sortiert, die Rohwerte nicht |

## 2. K2868 und S1 — geklärt (Punkt 1 des Auftrags)

**Frage:** K2868 wurde im ersten Nachspieldurchgang mit 12 ungedeckten Abweichungen in `tarife/ausdruck` abgelehnt.
Wertet der neue Parser gültige Ausdrücke anders aus als die Vorgeneration?

**Messung:** `s1/s1_klaerung.py` und `s1/s1_harness.mjs`, netzlose Kammer, kein Modell. Drei Stände:
- Vorgeneration: `lauf37-gen2`, Prüfsumme gegen die Lauf-DB.
- Kandidat: Vorgeneration plus Diff K2868, abgeleitet über `aegis.kandidat_dateien` wie im Organ.
- Versiegelte Normalversion von `ausdruck.ts`: nur gelesen, nur in der Kammer-Wegwerfkopie, nicht ins Werk gelangt.

Vor der Ausführung festgelegt:
- **Gültig** heißt: ein Ausdruck aus der Grammatik des Grenzvertrags (`tests/vertraege/VERTRAEGE.md` Z. 22).
- **Regel:** Gibt es dort eine Abweichung alt↔neu, ist S1 nicht sauber behoben.

Die t3.db war vor und nach der Messung gleich (sha256). Lauf 1 und Lauf 2 ergaben dieselben Zahlen.

| Korpus | Umfang | Ergebnis |
|---|---|---|
| K: Grammatik, Leerzeichen als Trenner (8 Vertragsbeispiele + 20.000 Zufallsausdrücke, Keim 20260923, je 6 Kontexte) | 120.008 Fälle, 1–112 Zeichen | **0 Abweichungen in 93.320 von 93.320 Fällen**, in denen der Vertrag eine Zahl liefert. 86 Abweichungen in den übrigen 26.688 Fällen, die der Vertrag abweist, alle derselben Art: Division durch null in einem Teilausdruck (Beispiel `gewicht/(5074/gewicht - gewicht)` bei gewicht 0). Die Vorgeneration rechnet dort über ∞ zu 0 weiter und verletzt damit den Vertrag (86 von 86). Der Kandidat weist mit `RangeError` ab. Kandidat gegen Vertrag: 0 von 120.008 abweichend. Kandidat gegen Normalversion: 0 von 120.008 abweichend |
| W: dieselben Ausdrücke, jedes Leerzeichen ersetzt durch Tab bzw. Zeilenumbruch. **Nachträglich ergänzt, nach Sicht von R; nicht Teil der vorab festgelegten Regel** | je 16.166 Ausdrücke | Die Vorgeneration liefert 12.216 Zahlen, die Normalversion 12.206, **der Kandidat 0**. In **12.206 von 16.166** Fällen weist der Kandidat ab, während Vorgeneration und Normalversion dieselbe Zahl liefern (`Unerwartetes Zeichen: \t`) |
| R: Schreibweisen außerhalb der Grammatik | 43 Eingaben | alt = neu in 12 von 43. Der Kandidat verhält sich in 35 von 43 wie die Normalversion. Die 8 übrigen: Vorzeichen `-0`, `--1`, `- -1`, `-(1-2)` nimmt der Kandidat an wie die Vorgeneration, die Normalversion weist sie ab. Weißraum `\t`, `\n`, `\r\n` und NBSP weist der Kandidat ab, die Normalversion nimmt ihn an |
| O: die Eingaben des Organs, mit globalem Marker | 5 Randfälle | `''` und `' '`: alle drei Stände `RangeError` (Länge). `'a'`, `'Ä-1'`, `'x'×40`: Die **Vorgeneration führt den Text als Programm aus**, 3 von 3 Markerzugriffen. Kandidat und Normalversion greifen 0 von 3 Mal zu. Ohne Marker (so ruft die Sonde) wirft alt `ReferenceError`, neu `SyntaxError`. Das sind die 3 × 4 Aufrufmuster = 12 Abweichungen des Organs |

**Antwort:**
- **Die 12 Abweichungen betreffen nur ungültige Eingaben** (unbekannte Bezeichner). An genau diesen Eingaben ist S1
  behoben, auch nach dem versiegelten Kriterium („abweisen ohne Markerzugriff“: 0 von 3).
- **Der Parser wertet gültige Ausdrücke dennoch anders aus: Mit Tab oder Zeilenumbruch als Trenner weist er ab.** Der
  Vertrag nennt Weißraum nicht. Die saubere Normalversion des Werkautors nimmt ihn an. Nach Philipps Kriterium ist S1 an
  K2868 damit **nicht sauber behoben**.
- Meine Einordnung „gültig“ stützt sich für Weißraum auf die Normalversion, nicht auf den Vertrag. Wird Weißraum außer dem
  Leerzeichen als außerhalb der Tarifsprache entschieden, gilt der Teil „nur ungültige Eingaben“ (Offen Nr. 1).

**Deckende Tests je Abweichung (Grundsatz 11):**
- Gebaut in `s1/s1_deckung.py`, ausgeführt mit dem Testläufer des Biotops (Vitest, Kammer), an allen drei Ständen.
- **4 von 4 deckend:** Sie fallen an der Vorgeneration und bestehen am Kandidaten. Es sind 3 Tests für `~rand#2/#4/#5`
  (Marker 0, ausdrücklich abgewiesen) und 1 Test für die Division durch null.
- Die Referenz besteht alle.
- Die **Weißraum-Spezifikation** ist grün an Vorgeneration und Referenz und **rot am Kandidaten**. Sie ist die rote
  Spezifikation dieser ungedeckten Abweichung, Text in `S1-DECKUNG.json`. Sie ist nicht im Baum, siehe Eigene Entscheidung 7.

**Befund am Organ, messbar erst durch diese Klärung:**
- Im zweiten Durchgang deckten die 3 Befundklassen-Tests die 12 Abweichungen, weil `verhaltensvergleich.deckung` **je
  Funktion** deckt: Jeder Test, der `ausdruck(` ruft, an der Vorgeneration fällt und am Kandidaten besteht, deckt jede
  Abweichung von `ausdruck`.
- Gestellte Probe: Eine konstruierte Abweichung `ausdruck~rand#9` gilt durch dieselben 3 Tests als gedeckt. Die
  Abweichungsschlüssel sind gestellt, die Tests echt erzeugt.
- Der Randfall-Korpus enthält für `string` die Werte `''`, `'a'`, `' '`, `'Ä-1'` und `'x'×40`, aber keinen Weißraum außer
  dem Leerzeichen.
- Folge: Der Verhaltensvergleich hätte K2868 auch dann bestehen lassen, wenn er die Weißraum-Abweichung gesehen hätte.
  Grundsatz 11 („jede Abweichung braucht einen deckenden Test“) ist damit nicht wörtlich umgesetzt.

## 3. Gedächtnissperre-Test — Gegenprobe (Punkt 2 des Auftrags)

**Was sich nach dem Review geändert hat:**
- `test_10_sperre_am_laufweg_projekt_merken_und_wiederholung` bekam die Vorrichtung `ts_kammer` (Review Nr. 13). Ohne das
  TS-Kammerimage wird er jetzt übersprungen statt rot.
- Die Regel wirkt seit Review Nr. 11 an zwei Stellen, beim Schreiben und beim Lesen.

**Messung** (`sperre/sperre_gegenprobe.py`):
- Je Variante eine Kopie des Arbeitsbaums mit genau einem Eingriff.
- `PYTHONPATH` zeigt auf die Kopie. Die geladene `gedaechtnis.py` stammt je Variante nachweislich aus der Kopie.
- Gelaufen sind 4 Zeilen `test_10` und `test_review11`.

| Variante | Ergebnis (5 Fälle) | Wo rot |
|---|---|---|
| unverändert | 5 grün | — |
| Schreibstelle aus (`projekt_merken` klassifiziert nicht mehr) | **5 grün — allein blind** | Die Lesestelle hält |
| Lesestelle aus (`_sperrt` → immer sperren) | 1 rot | nur `test_review11` (`gescheiterte_wege` liefert den Altbestand-Laufzeitriss); `test_10` bleibt grün, weil die Schreibstelle hält |
| beide aus | 3 rot | `test_10` in den Zeilen „tarife unberührt“ und „planung berührt, nicht gepaart“ an **`assert (w is not None) is sperrt`**, dazu `test_review11` |
| Regel sperrt immer (`laufzeit_sperrt` → True) | 3 rot | dieselben zwei Zeilen an derselben Zusicherung, dazu `test_review11` |
| Regel sperrt nie | 2 rot | `test_10` Zeile „berührt und gepaart bestätigt“ an derselben Zusicherung, dazu `test_review11` |
| ohne TS-Image (`biotop-kammer:1`) | **4 übersprungen**, 1 grün | Kein Rot möglich |

**Antwort:**
- Der geänderte Test kann weiter rot werden, an der vorgesehenen Zusicherung: bei einem Fehler der Regel selbst und beim
  Verlust beider Stellen.
- Den Verlust nur der Schreibstelle erkennt kein Test. Die Lesestelle deckt ihn ab.
- Den Verlust nur der Lesestelle erkennt nur `test_review11`.
- Ohne `BIOTOP_KAMMER_IMAGE=biotop-kammer:ts1` prüft `test_10` nichts. Die Regressionsjobs setzen ts1.
- Ob `test_10` in der Regression wirklich lief: In der Regression an `330b4ec` liefen 4 von 4 Fällen von `test_10_sperre_am_laufweg…` und bestanden; übersprungen 0 (Image ts1 gesetzt)

## 4. Umgang mit den Review-Befunden

Ein Durchgang (`REVIEW.md`, 15 Befunde: 2 hoch, 9 mittel, 4 niedrig). Jeder Befund wurde vor der Übernahme am Code
nachgemessen. Eingearbeitet in `330b4ec`, jeder mit Probe und Gegenprobe in `tests/test_vor_t4.py`.

| Nr | Schwere | Befund (kurz) | Umgang |
|---|---|---|---|
| 1 | hoch | Pfeil-Export gilt als entfernt → verhaltensgleiche Kandidaten abgelehnt | behoben (Beobachtungen beider Seiten, y aus Signaturen); `test_review1_*` Modul, gestellt nur die Kammer. **Offen:** Gegenprobe mit Pfeil-Export im Drahtwerk nicht gebaut |
| 2 | hoch | TS-Anhängen: doppelte Bindung, als geurteilt gezählt | behoben (Bindungen zusammengeführt, Konflikt neutral); `test_review2_*` in der Kammer. Nicht unter node ausgeführt |
| 3 | mittel | Zurückgestellte zählen als nicht überlebt → Sättigung statt Halt | behoben (`_messgeraet_ausfall`: abgebrochen, zweimal → angehalten); `test_review3_*` Laufweg |
| 4 | mittel | Nr. 3 nur 1 von 3 Ausfallarten am Laufweg; Formulierung zu stark | 2 Ausfallarten ergänzt (`test_review4_*`), Formulierung in §1 berichtigt. **Offen:** Generalprobe-Abbruch ohne Test |
| 5 | mittel | Modul- statt Laufweg-Nachweise | Nachweisart je Zeile in §1; Laufweg-Tests für Nr. 4, 9, 11 ergänzt. **Offen:** gepaarte Generalprobe, Protokollfelder Nr. 8 |
| 6 | mittel | Gegenprobe „phase“ prüft die Wirkung | umbenannt in „wirkung“ (§1). Die Phasenbindung ist nur am Prüfwerkzeug belegt |
| 7 | mittel | Nachspiele nicht an `58bd9f9` gebunden | Nachspiel-Skript schreibt jetzt Commit und Arbeitsbaumstatus. Alle 7 Fälle an `330b4ec` wiederholt: K2904 abgelehnt (vorher ueberlebt; Abweichungen 0 → None, ungedeckt 0 → 0, beobachtet 4 von 4 → None, planung gepaart 9.9849 → 8.1887 ms (-18 %); Erwartung NICHT erfüllt); K3091 ueberlebt (vorher ueberlebt; Abweichungen 0 → 0, ungedeckt 0 → 0, beobachtet 4 von 4 → 4 von 4, planung gepaart 9.5170 → 7.9893 ms (-16 %); Erwartung erfüllt); K3106 abgelehnt (vorher abgelehnt; Abweichungen 8 → 8, ungedeckt 8 → 8, beobachtet 5 von 7 → 7 von 7; Erwartung erfüllt); K3324 ueberlebt (vorher ueberlebt; Abweichungen 0 → 0, ungedeckt 0 → 0, beobachtet 7 von 7 → 7 von 7; Erwartung erfüllt); K2934 abgelehnt (vorher abgelehnt; Abweichungen 25 → 25, ungedeckt 20 → 20, beobachtet 7 von 7 → 7 von 7; Erwartung erfüllt); K3121 abgelehnt (vorher abgelehnt; Abweichungen 25 → 25, ungedeckt 20 → 20, beobachtet 7 von 7 → 7 von 7; Erwartung erfüllt); K2867+2868 ueberlebt (vorher ueberlebt; Abweichungen 12 → 12, ungedeckt 0 → 0, beobachtet 9 von 10 → 10 von 10; Erwartung erfüllt) |
| 8 | mittel | Python (T4): (a) Verhaltensvergleich enthält sich immer; (b) gepaarte Laufzeit Python nie ausgeführt; (c) G0-rc | (c) behoben (`test_review8c`). (b) einmal in der Kammer ausgeführt: in der Kammer ausgeführt (Werk lagerhaus, Image biotop-kammer:1, `PYTHON-LAUFZEIT-PROBE.json`): gleicher Stand gegen gleichen Stand gültig, 5 je Seite, 4 von 4 Bereichen, Verhältnis 0,964–1,062, 13,0 s. **Gegenprobe blind:** Ein Kandidat mit Syntaxfehler in `lagerhaus/formeln/auswertung.py` ergibt `gueltig True`, aber `kandidat None` in 3 von 4 Bereichen (`NACHLESE.json`); `laufzeit_einsetzen` überspringt fehlende Werte still. Rote Spezifikation `spez/test_spez_laufzeit_gepaart_teilausfall.py`: an `330b4ec` 1 rot, Gegenprobe grün. Der Codeweg ist sprachneutral; für TS gelesen, nicht ausgeführt. Der erste Probelauf traf ein Modul, das die Referenzlast nicht lädt (`PYTHON-LAUFZEIT-PROBE-lauf1.*`). **(a) offen, Entscheidung Philipp** (Offen Nr. 3) |
| 9 | mittel | Typbau zwischen den Runden ohne Probe | `G0.rundenpruefung`, `test_review9` durch `lauf.generation0` (2 Fälle) |
| 10 | mittel | „4,80“ gestellt; „~1 min“ ohne Beleg | (a) in §1 als gestellt gekennzeichnet; (b) `dauer_s` wird protokolliert, gemessen: gepaarte Messung 59–62 s je Kandidat (Median 60 s, 7 von 7 Nachspielen mit gepaarter Messung) |
| 11 | mittel | alte Laufzeiteinträge sperren weiter (141 von 141) | Leseseite `_sperrt`; `test_review11`; §3 |
| 12 | niedrig | Kammerausfall als Syntaxfehler gezählt | behoben, `test_review12` |
| 13 | niedrig | Tests hängen am Image ts1 ohne Hinweis | `ts_kammer` überspringt mit Grund. Folge in §3 (übersprungen statt rot) |
| 14 | niedrig | zwei Tests prüfen Quelltext | unverändert; sie gelten ausdrücklich als Strukturtests, die Wirkung belegen die Nachspiele |
| 15 | niedrig | unerreichbare Zeile | entfernt |

## 4a. Nachlese nach dem Commit-Job (Befunde aus den Nachspielen am Commit)

**K2904 und K3091 in drei Durchgängen** (dieselbe S2-Behebung, Lauf 37 bzw. 38):

| Durchgang | Code-Stand | K2904 | K3091 | K2904 `eingang` gepaart (Vorgeneration → Kandidat) |
|---|---|---|---|---|
| 1 (`nachspiel/`) | `58bd9f9`-Arbeitsbaum (Review Nr. 7) | überlebt | überlebt | ×1,096 |
| 2 (`nachspiel2/`) | `330b4ec`, sauber | **abgelehnt**: `eingang.laufzeit_ms: 3.078 > Grenze 2.985 (Vorgeneration gepaart, Median aus 5 2.514 × 1.187 …)` | überlebt | ×1,224. Kandidatenwerte in Messreihenfolge 2,44 / 2,44 / 3,08 / 3,27 / 4,26 ms, Vorgeneration 2,51 / 2,43 / 2,89 / 2,52 / 2,35 ms |
| 3 (`nachspiel3/`, nur S2) | `330b4ec`, sauber | überlebt | überlebt | ×1,012 |

- **Gemessen:** K2904 ändert nur `src/planung/pruefen.ts`. `src/eingang/*` importiert nur `../zahlen/pruefen.js`.
  Der Riss liegt also in einem Bereich außerhalb des Wirkungskreises.
- Die Grenze gilt für jeden Bereich, nicht nur für berührte. Die gepaarte Messung macht solche Risse seltener, aber nicht
  unmöglich.
- **Nicht gemessen:** die Ursache des Anstiegs innerhalb der Kandidatenreihe (die Maschine oder etwas anderes).
- Zwei weit auseinanderliegende Werte in drei Durchgängen belegen eine Streuung, keinen Effekt.
- Der Gedächtniseintrag dieser Ablehnung sperrt nicht (unberührt, Regel Nr. 10).

**Restrauschen unberührter Bereiche** (`NACHLESE.json`, Verhältnis Kandidat/Vorgeneration gepaart):
- Durchgang 1: 31 Vergleiche aus 8 Belegen; 1 über 1,10; 0 über 1,15; größter Wert ×1,127.
- Durchgang 2: 28 Vergleiche aus 7 Belegen; 1 über 1,15 (K2904 `eingang`, ×1,224).
- Das Review zählte für Durchgang 1 34 Vergleiche aus 9 Zeilen. Den Unterschied zu meinen 31 aus 8 habe ich nicht
  aufgeklärt; meine Ableitung steht in `nachlese.py`.

**Gepaarte Laufzeit, Teilausfall:** siehe Nr. 1 in §1. Fehlt einer Seite ein Wert, bleibt die Messung „gültig“, und der
Bereich wird still am Einzelwert entschieden. Rote Spezifikation liegt im Ordner (`spez/`).

## 5. Zwischenbericht-Wächter: zweiter Auslöser (Kontext 80 %, gescheiterte Verdichtung)

**Anlass:** Die Sitzung `20260921_015554_e79a4a0f` starb am 23.09. um 19:35:07 an „prompt is too long: 1001191 tokens >
1000000 maximum“. Die Verdichtung war seit 16:00:39 wiederholt gescheitert (401, widerrufene Anmeldung). Das Rundenlimit
griff nie.

**Umsetzung** (`~/.hermes/scripts/zwischenbericht_waechter.py`; Sicherung `*.vor-kontext-20260923-212241`):
- **Kontextfüllung:** Eingabetoken der letzten Modellanfrage der Sitzung (`agent.log`, „API call #n … in=“) geteilt durch
  das Kontextfenster des Modells (models.dev-Zwischenspeicher). Entschieden wird am ungerundeten Anteil; ist die Grenze
  unbekannt, gibt es keinen Auslöser, und der Herzschlag zeigt das.
- **Verdichtung:** Telemetriezeile dieser Sitzung mit `failure_class`/`aborted` (außer `lock_contended`) oder „Context
  compression failed“, jeweils seit Turnbeginn.
- Je Sitzung und Turn genau einmal. Der Ordner heißt `…-r<n>-kontext80` bzw. `-verdichtung`, und der Anlass steht im Bericht.
- `--jetzt` wirkt jetzt auch auf Nachrichten und Logzeilen, damit sich ein früherer Zeitpunkt nachspielen lässt.

**Proben:**
- `test_waechter.py`: 12 von 12 grün (`waechter/TESTS-NEU.txt`). Die 6 alten Tests sind grün; 2 ihrer Zusicherungen
  wurden angepasst (§7).
- **Gegenproben 10 von 10** (`waechter/GEGENPROBEN.json`): je eine Kopie mit genau einem Ausschalter. Jede scheitert an
  der vorab benannten Zusicherung:
  - Schwelle aus;
  - `>` statt `>=`;
  - mehrfach je Turn (Kontext und Verdichtung);
  - fremde Sitzung (Kontext und Verdichtung);
  - vor Turnbeginn;
  - Verdichtung aus;
  - Sperrkonflikt gilt als Scheitern;
  - beendete Sitzung im Nachspiel.
- **Nachspiel an den echten Daten der gestorbenen Sitzung** (`waechter/NACHSPIEL-ECHTE-SITZUNG.json`):
  - minütlich 15:54–19:35, 222 Takte;
  - state.db nur gelesen;
  - Prüfkanal-Attrappe unter /tmp;
  - der echte Wächterzustand blieb unberührt.

  | Zeit | Auslöser |
  |---|---|
  | 16:01 | Verdichtung gescheitert (16:00:39, `summary_generation_aborted`, „OAuth access token has been revoked.“) |
  | 16:48 | Kontext 80,6 % (805.516 von 1.000.000) |
  | 18:34, 19:08, 19:16, 19:25 | erneut, je in einem neuen Turn (die Hintergrundmeldungen um 18:33, 19:07 und 19:15 beginnen einen Turn) |

  Die höchste Runde eines Turns war 77 von 150, der alte Auslöser hätte also nie gefeuert.
- **Eigener Fehler, vom Nachspiel gefunden und vor der Lieferung behoben:** Die erste Fassung las auch die
  Verdichtungssperre aus `state.db`. Diese Spalte trägt den Endstand. Im Nachspiel löste 19:21 an einer Sperre „bis
  19:30:29“ aus, die erst der Fehlschlag um 19:29:29 schrieb. Die Spalte ist entfernt, es gilt nur noch das Log.
- **Zeitplan ruft die neue Fassung:** `herzschlag.json` von 21:35:55 hat Elternprozess `cron.scheduler` und führt das
  neue Feld `kontext` (358.116 von 1.000.000 für diese Sitzung).

## 6. Träger und Verdichtung

| Stufe | Beleg (`traeger/TRAEGER-BELEG.json`) |
|---|---|
| Datei | Sicherung `config.yaml.vor-opus55-20260923-201806` (sha256 `90ce5087…`). Geändert sind 2 Zeilen: `model.default` astra-opus-max → **claude-opus-5-5**, `provider` moa → **anthropic**. `agent.reasoning_effort: max` stand schon so und ist unverändert |
| Auflöser im Prozess | `resolve_reasoning_config` → `{enabled: true, effort: max}`. Klemme `_thinking_kwargs` für claude-opus-5-5 → `thinking adaptive`, `output_config.effort max` (nicht herabgestuft). Gateway-Auflöser: `_resolve_gateway_model` → claude-opus-5-5 |
| **Anfragekörper** | frischer Prozess `hermes chat -q … --oneshot` ohne Modell- und Denkstufen-Schalter, `HERMES_DUMP_REQUESTS=1`, Dump `preflight` (sha256 `04978857…`): **`model: claude-opus-5-5`, `thinking: {type: adaptive}`, `output_config: {effort: max}`**, `max_tokens` 128000. Die Anfrage wurde angenommen (Antwort „BELEG“, rc 0). Das URL-Feld des Dumps ist eine Beschriftung des Dump-Helfers; das Anthropic-Messages-Format zeigen die Felder `system`, `thinking` und `output_config` |
| Gateway | Kein eigener Dump. Laut Code liest das Gateway `config.yaml` je Turn (`_resolve_gateway_model`, `_load_reasoning_config`) — gelesen, nicht gemessen. **Ein Neustart ist nach dieser Lesart nicht nötig.** Der laufende Chat trägt zusätzlich Philipps persistierten `/model`-Override (dasselbe Modell). Jede Gateway-Anfrage seit 19:49 ist im Log `model=claude-opus-5-5 provider=anthropic` |
| **Verdichtung** | echte Anfrage über die Route des Verdichters (`call_llm`, task `compression`) → **anthropic / claude-opus-5-5, Antwort in 3,5 s**. Im Gateway seit dem Neustart 19:47: 0 Anmeldefehler in `errors.log`; Hilfsaufrufe über dieselbe Anmeldung (approval) um 19:52, 20:37 und 21:19. Eine echte Verdichtung ist seit dem Neustart nicht angefallen (Schwelle 500.000 Token, Stand 358.116). Letzte gescheiterte Verdichtung, 19:29:29, wörtlich: „Error code: 401 - {'type': 'error', 'error': {'type': 'authentication_error', 'message': 'OAuth access token has been revoked.'}, 'request_id': None}“ |

Die Anfrage um 19:45:55 (nach dem Zurücksetzen, vor dem `/model`) lief über moa/astra-opus-max und endete mit
„HTTP 429: The usage limit has been reached“ (resets_at 27.09. 04:54). Deshalb gehört der Grundwert in die Datei.

## 7. Geänderte ältere Tests (Spezifikation geändert, nicht Regression)

- `tests/test_vor_t4.py::test_10_…` und `test_9_…`: + Vorrichtung `ts_kammer` (Review Nr. 13). Ohne ts1 übersprungen
  statt rot (§3).
- `~/.hermes/zwischenbericht/test_waechter.py`:
  - `test_vorhandener_ordner…`: `--jetzt` liegt jetzt nach den geschriebenen Nachrichten, weil `--jetzt` Nachrichten
    filtert.
  - `test_neuer_turn…`: Der Herzschlag führt zusätzlich `kontext` und `verdichtung_gescheitert`; zugesichert werden nur
    noch `sitzung` und `runden`.

## 8. Zurückgezogene oder berichtigte Aussagen des 18:18-Entwurfs

- „Alle elf Vorbedingungen sind gebaut“ → gebaut für den TypeScript-Pfad. Für Python fehlt der Verhaltensvergleich
  (Nr. 2), und der Python-Zweig von Nr. 1 ist nur einmal ausgeführt.
- „Offen aus dem Auftrag: nach meiner Prüfung nichts“ → zurückgezogen (§2, Nr. 8a).
- „Gestellt ist nur die Kammergrenze“ (Nr. 3) → gestellt waren Kammer, Messgerät und Modell.
- „Vorgeneration 4,80“ → ein gestellter Testwert, keine Messung.
- „K2868 Durchgang 2 überlebt, 12 von 12 gedeckt“ → stimmt als Ausgabe des Organs. Die Deckung gilt aber je Funktion,
  und der Kandidat ändert gültiges Verhalten (§2).

## 9. Sperren im Wortlaut

- `terminal` mit `nohup … &`: „Foreground command uses shell-level background wrappers (nohup/disown/setsid). Re-send
  WITHOUT the wrapper as terminal(command="<cmd>", background=true, notify_on_complete=true) …“
  - Einordnung: Formatvorgabe der Ausführungsschicht, kein Sicherheitsurteil.
  - Umgang: derselbe Befehl ohne `nohup`, als verfolgter Hintergrundprozess, wie die Meldung verlangt.
- Drei Befehle wurden vom Sicherheitsscan markiert („[HIGH] Pipe to interpreter …“ bzw. „Nested executable body could not
  be resolved …“) und **von der Smart-Approval freigegeben**. Es waren Lesebefehle (Sitzungsindex, Modellkatalog,
  Cron-Liste). Kein Block.
- Zwei Aufrufe über 600 s hat die Ausführungsschicht als Hintergrundprozess gestartet. Kein Block.

## 10. Eigene Entscheidungen

1. **`model.default` in `config.yaml` gesetzt.** Philipp hatte per `/model` umgestellt. Dieser Override gilt nur für die
   Unterhaltung und ging beim Zurücksetzen um 19:35 verloren; gemessen an der 429-Anfrage um 19:45:55. Die Sicherung
   liegt daneben.
2. **Beleg am frischen CLI-Prozess statt am Gateway.** Ein Gateway-Dump bräuchte `HERMES_DUMP_REQUESTS=1` in `.env`. Das
   wirkt ab dem nächsten Turn und schreibt jede Anfrage samt Verlauf auf die Platte. Nicht ungefragt.
3. **Maßstab „gültig“ in §2.** Es gilt die Vertragsgrammatik. Wo der Vertrag schweigt (Weißraum), entscheidet die
   versiegelte Normalversion, die nur gelesen wurde. Das Weißraum-Korpus W ist nach Sicht von R ergänzt und so
   gekennzeichnet.
4. **Wächter: je Turn einmal.** Nicht einmal je Sitzung, weil ein Zwischenbericht den Stand des Turns zeigt. Ergebnis in
   der gestorbenen Sitzung: 6 Berichte in 3½ h. Weitere Festlegungen:
   - `lock_contended` ist kein Scheitern.
   - Die Kontextfüllung kommt aus dem Log, weil `state.db` keine laufende Kontextgröße führt.
5. **Review-Befunde als Code, ohne zweites Review.** Der Auftrag verlangt ihren eigenen Commit. Nach der Regel „ein
   Review“ belegen ihn Tests, Gegenproben und die volle Regression.
6. **5 Messungen je Seite, „Laufzeit nur wo sie entscheidet“, Befundklassen je geändertem Bereich.** Diese Entscheidungen
   gelten unverändert wie im Entwurf (Punkte 1–7 dort).
7. **Die Weißraum-Spezifikation ist nicht in `/root/biotop/tests` eingecheckt.** Commit und Regression waren gelaufen,
   und ein roter Test hätte die Regression rot gemacht. Sie liegt als Text für den nächsten Auftrag im Ordner. Dasselbe
   gilt für `spez/test_spez_laufzeit_gepaart_teilausfall.py`.
8. **Dritter Durchgang für K2904 und K3091.** Er ist eine Wiederholungsmessung nach einem Ausreißer. Durchgang 2 bleibt als
   gescheiterte Zeile stehen, und alle drei Werte sind berichtet.
9. **Keinen neuen Code nach dem Review für K2904 und den Teilausfall.** Beides wäre neuer, ungeprüfter Code nach dem einen
   Reviewdurchgang. Der Teilausfall ist deshalb eine rote Spezifikation, und die Laufzeitgrenze außerhalb des
   Wirkungskreises ist eine Frage an Philipp.

## 11. Eigene Fehler in diesem Auftrag

- **Wächter, erste Fassung:**
  - Sie las die Verdichtungssperre aus `state.db`. Beim Nachspiel löste das einen Bericht vor dem Fehlschlag aus, den die
    Spalte meldete. Behoben.
  - Der Rückgabewert hing am Wort „gescheitert“. Die neuen Tests fielen daran. Behoben.
- **Python-Gegenprobe, erster Lauf:** Sie brach ein Modul, das die Referenzlast gar nicht lädt, und war damit blind. Erst
  der zweite Lauf und die Nachlese zeigten den Teilausfall.
- **Platzhalter zu früh gefüllt:** Das Skript `platzhalter_fuellen.py` lief vor dem zweiten Python-Lauf. Der Text ist von
  Hand durch den gemessenen ersetzt.

## 12. Offen für Philipp

1. **S1/Tarifsprache:** Gehört Weißraum außer dem Leerzeichen zur Sprache? Der Vertrag schweigt, die Normalversion nimmt
   ihn an. Davon hängt ab, ob S1 in T3 (Lauf 37) als sauber behoben gilt.
2. **Verhaltensvergleich, Deckung je Funktion statt je Abweichung, und Randfall-Korpus ohne Weißraumvarianten** (§2).
   Die Weißraum-Spezifikation ist das rote Beispiel.
3. **T4 ist Python, der Verhaltensvergleich enthält sich dort immer.** Zu entscheiden: vor T4 eine Python-Sonde bauen,
   oder die Torzeile anpassen.
4. Wächter: je Turn oder je Sitzung einmal?
5. Gateway-Dump als Beleg am Gateway selbst (Eigene Entscheidung 2): gewünscht?
6. Aus dem Entwurf: Bauzeit gepaart messen? Auslegung „Korpus aus den Verträgen“ bestätigen.
7. **Laufzeitgrenze außerhalb des Wirkungskreises** (K2904, Durchgang 2). Zur Wahl:
   - die Grenzprüfung der Laufzeit auf berührte Bereiche und ihre Abhängigen beschränken;
   - einen Riss vor der Ablehnung einmal gepaart bestätigen;
   - beides.

   Das ist eine Änderung der Regel und damit Philipps Entscheidung.
8. Teilausfall der gepaarten Messung beheben: rote Spezifikation `spez/test_spez_laufzeit_gepaart_teilausfall.py`.
