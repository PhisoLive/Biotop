# Review Behebungsrunde 4 vor T4: ein Durchgang

Stand: 2026-09-24, gegen 16:35 Uhr. Das ist ein unabhängiger Reviewdurchgang nach `REVIEW-AUFTRAG.md`.

**Gegenstand**
- `BERICHT.md` in der Fassung von etwa 16:20 Uhr. Noch offen sind `‹URTEIL›`, `‹ERGEBNIS›`, `‹REVIEW›`, `‹SPERREN›` und `‹OFFEN›`. Geprüft sind die ausgefüllten Teile: §1–§9, §12 und §13.
- Commit `1d9a5aa` auf `0aac612` und Nachtrag `43b8fad` (HEAD, Arbeitsbaum sauber).
- Die Belege unter `/root/biotop-vor-t4-04/`.

**Wie geprüft**
- Kein Modellaufruf, kein Netz, kein Geld. Keine volle Regression, kein Verdrahtungstest.
- Kammerläufe: ein Skript mit 24 Fällen, 16:08–16:10 Uhr, gegen HEAD `43b8fad` in der echten Kammer `biotop-kammer:1`. Es startete erst nach dem Ende von `job_nachtrag.sh` (16:02:07 Uhr laut `JOB-NACHTRAG.txt`). `pgrep` fand um 16:08:23 Uhr keinen Job mehr; das Skript prüft das beim Start selbst noch einmal.
- Vorher habe ich nur gelesen und ohne Kammer gerechnet.
- `git status` von `/root/biotop` war vor und nach den Kammerläufen leer.
- Die Lauf-DB habe ich einmal geöffnet, nur lesend (`mode=ro`), und nur die Tabelle `eichung` der Läufe 37/38 gelesen.

**Kurzurteil**
- **Die Probenfälle der vier hohen Befunde aus Review 03 sind geschlossen.** Von 16 Originalfällen der Gutachtenproben habe ich 14 an `43b8fad` neu gefahren. Alle 14 verhalten sich wie spezifiziert.
- **Die Gegenproben der Entscheidungen 1, 3 und 4 sind erfüllt:**
  - Entscheidung 1: K2904 und K3091 überleben an Stufe 2 in je 3 von 3 Durchgängen, `planung`-Quote 0,376–0,455.
  - Entscheidung 3: K2868 wird abgelehnt. Die drei Randfälle sind gedeckt; ungedeckt bleiben 20 Weißraum-Beobachtungen und 4 Zahlform-Beobachtungen.
  - Entscheidung 4: `test_e4_*` durch `aegis.pruefen`.
- **Die Lückenklassen sind nicht geschlossen.** Zwei neue hohe Befunde, beide in der Kammer gemessen:
  - Nr. 1: Ein Test „hält fest“, ohne das Merkmal zu unterscheiden. Ein Vorgenerations-Test mit einer Idempotenz-Zusicherung deckt einen Tab-Rückschritt; der Kandidat **überlebt durch `aegis.pruefen`**.
  - Nr. 2: Bei Klassen mit `__slots__` und Vererbung wird der Zustand der Basisklassen-Slots nicht verglichen. Ergebnis: 0 statt 28 Abweichungen, tragfähig.
- **Mittlere Befunde:**
  - Verschleierte Slot-Namen (Nr. 3).
  - `csv.DictReader` legt den Verhaltensvergleich des ganzen Laufs still (Nr. 4).
  - Änderungen an Iterator-Objekten des Werks bleiben still (Nr. 5).
  - Die Kappe der Verfälschungsläufe führt zur Ablehnung statt zur Enthaltung (Nr. 6).
  - Die Torzeile „Schwächen“ hat keinen Aufrufer (Nr. 7).
  - Der Rückfall auf Stufe 1 wird nicht verweigert (Nr. 8).
  - Lastaufrufe gelten immer als gewöhnlich (Nr. 9).
  - `Path`-Rückgaben sind inhaltslos (Nr. 10).

## Befunde

| Nr | Schwere | Befund | Beleg (Datei:Zeile, Befehl, Messung) | Vorschlag |
|---|---|---|---|---|
| 1 | hoch | **Ein Test hält ein Merkmal fest, ohne es zu unterscheiden. Gemessen durch `aegis.pruefen`.** Als `fail` zählt jede Ausnahme in der call-Phase, nicht nur eine fallende Zusicherung. BERICHT §2 sagt dagegen: „‚Hält fest‘ heißt: die Zusicherung im Test fällt“. Das Verfälschungsobjekt (`Verfaelscht`, „gleich nichts“) löst eine Ausnahme aus, sobald Werkcode es weiterverarbeitet. **Probe x3:** Kandidat K2 gibt Text mit Tab unverändert zurück. Der Werkstest sichert zu: `normieren(normieren("a\tb c")) == normieren("a\tb c")` und `normieren("a b") == "a_b"`. Die übrigen Soll-Tests decken je eine Formvariante ab, keiner mit Tab. **Ergebnis: überlebt.** „Kernmaß −12 → −2 (+10)“, 52 Abweichungen, 0 ungedeckt, 6 von 6 Rückschritt-Beobachtungen gedeckt. `festhaltend …\|rueckgabe\|tab` enthält `test_normieren_x`. **Kontrolle x3k** (ohne die Idempotenz-Zeile): abgelehnt, 0 von 6 gedeckt. Die Idempotenz gilt an der Vorgeneration und am Rückschritt gleichermaßen. An der Vorgeneration fällt der Test nur an der Zeile „a b“. Gelesen, nicht gemessen: Ein verketteter Aufruf ganz ohne Zusicherung hielte `tab` ebenso fest. TypeScript verhält sich gleich (`deckung.mjs` übernimmt `t.state`). Das ist dieselbe Klasse wie Review 03 Nr. 2. | `/tmp/review-vor-t4-04/kammerprobe.py` (Fälle x3, x3k); `kammerprobe.out.txt:3-4`; `KAMMERPROBE.json`. Code: `KERN-COMMIT.patch.txt:556-561` (Plugin: `'fail' if report.outcome == 'failed'`), `biotop/kern/py/verhalten.py:142-153` (`Verfaelscht`) | Als „hält fest“ nur einen `AssertionError` mit Ort in der Testdatei zählen. Eine Ausnahme aus Werkcode unter Verfälschung ist `fehler`. Zusätzlich verlangen, dass an der Vorgeneration dieselbe Zusicherung (Zeile) fällt. Rote Spezifikationen: x3 und x3 ohne Zusicherung. Die Gegenproben von H1 und H2 müssen grün bleiben. |
| 2 | hoch | **`__slots__` mit Vererbung: Der Zustand der Basisklassen-Slots wird nicht verglichen.** Die Klasse aus Review 03 Nr. 4 ist damit nicht geschlossen. Die Beobachtung `>args` entsteht aus `kan()`. `kan()` liest nur `type(x).__slots__` der eigenen Klasse. `_felder` und `_slotnamen` gehen zwar über die MRO, gelten aber nur für Schnappschuss, Rücksetzen, Mutieren und Rezept. **Probe p22:** Basis mit `__slots__=('stand',)`, `Konto(Basis)` mit `__slots__=('name',)`; `buchen` ändert nur `self.stand`. Ergebnis: **0 Abweichungen, „1 von 1 beobachtet“, tragfähig.** Kontrolle p22k (der eigene Slot `name` wird geändert): 28 Abweichungen. Gelesen: Eine Unterklasse ohne `__slots__` über einer Slot-Basis hat ein `__dict__`; `kan()` liest dann nur `vars(x)`. Das ist dieselbe Lücke. BERICHT §2 („alle Slots der Klassenhierarchie“) trifft auf den Vergleich nicht zu. | `kammerprobe.out.txt:8-9`; `verhalten.py:115-119` (`kan`), `:395-410` (`_slotnamen`, `_felder`) | `kan()` soll die Felder über `_felder()` bilden (MRO, `__dict__` und Slots). p22 als rote Spezifikation, p22k als Kontrolle. |
| 3 | mittel | **Verschleierte Slot-Namen (`__slots__ = ('__stand',)`) sind unsichtbar.** `_slotnamen` liefert `__stand`, das Attribut heißt aber `_Konto__stand`. Folge: `_felder` ist `{}` (lokal gemessen), und `kan()` liefert an beiden Ständen `{'__stand': None}`. **Probe p21** (`buchen` ändert `self.__stand`): 0 Abweichungen, tragfähig. | `kammerprobe.out.txt:7`; `lokal_proben.out.txt:11` | Namen mit `__`-Präfix und ohne `__`-Suffix zu `_<Klasse>__name` auflösen, in `_slotnamen` und in `kan()`. p21 als rote Spezifikation. |
| 4 | mittel | **`csv.DictReader` wird weiter ersetzt. Der Lastabbruch stellt dann jeden Kandidaten des Laufs zurück.** `_iter_art` ersetzt Iteratoren der Module `builtins`, `itertools`, `collections`, `_collections` und `csv`. `csv.DictReader` ist eine Python-Klasse im Modul `csv` mit Attributen (`fieldnames`, `line_num`, `reader`); sie wird durch einen Generator ersetzt. `csv.reader` ist ein Typ aus `_csv` und bleibt stehen (lokal: `DictReader` → `iter`, `reader` → `objekt`). **Probe q1:** Die Last liest `r.fieldnames`. An der Vorgeneration ergibt das `korpus:last_m = Fehler:AttributeError` und damit `SondeAusgefallen` (seit `43b8fad`). Kontrolle q1k (`csv.reader`, `line_num`): 6 Abweichungen, Iterator-Objekt gezählt. Gelesen: `aegis.pruefen` stellt den Kandidaten dann zurück. Die neue Prüfung sieht alle `korpus:last_*`; der Ausfall trifft also jeden Kandidaten jedes Bereichs, nicht nur den betroffenen Bereich. R4-3 verlangt die Bedingung „während das Messgerät die Last fehlerfrei lief“; der Code prüft sie nicht, er setzt sie voraus. BERICHT §2 („nur Generatoren und eingebaute Iteratoren“) sagt mehr, als der Code tut. | `kammerprobe.out.txt:5-6`; `lokal_proben.out.txt:2-3`; `verhalten.py:288`; `KERN-COMMIT-2.patch.txt:45-53` | `csv` aus der Liste nehmen oder nur Typen ohne öffentliche Attribute ersetzen. Den Ausfall auf Kandidaten beschränken, deren Wirkungskreis den abbrechenden Bereich enthält. q1 als rote Spezifikation. |
| 5 | mittel | **Teil-Enthaltungen werden gezählt, ändern aber weder das Urteil noch den Nenner.** Ein Iterator-Objekt des Werks bleibt unverändert und wird nie ausgelesen. `__next__` umhüllt die Sonde nicht (Namen mit `_`). **Probe p18c:** Der Kandidat ändert nur die Elemente (`.upper()` in `__next__`). Ergebnis: 0 Abweichungen, „1 von 1 beobachtet“, tragfähig, `teilweise: iterator_objekt 48`. Kontrolle als Generator (p18ck): 40 Abweichungen. Ebenso p14 (Änderung ab Element 51): tragfähig, `iterator_gekappt 14`. Der Zähler steht nur im Beleg. | `kammerprobe.out.txt:10-11, 19` | Eine Funktion, deren Beobachtungen nur aus Teil-Enthaltungen bestehen, nicht als „beobachtet“ zählen. Oder die Elemente an einer Kopie auslesen (`copy.deepcopy`), wo das geht. p18c als rote Spezifikation. |
| 6 | mittel | **Die Kappe der Verfälschungsläufe führt zur Ablehnung statt zur Enthaltung.** R4-12 verlangt eine „gezählte Enthaltung“. Gebaut ist etwas anderes: Proben jenseits der 24 entfallen, ihre Abweichungen bleiben ungedeckt, und der Kandidat wird abgelehnt. Der Grund nennt die Kappe nicht; sie steht nur in `deckung_zaehlung.ausgelassen`. §12 Nr. 4 begründet das mit „nie gedeckt“. Die 24 ist geschätzt; gemessen ist nur K2868 (2 Läufe, 0 ausgelassen). Bei T4 (großes Werk, mehrere Merkmale je geänderter Funktion und Art) wird ein breiter Kandidat so ohne Messung abgelehnt. | `KERN-COMMIT.patch.txt:1362-1385, 1427-1441`; BERICHT §7 R4-12, §12 Nr. 4 | Ab der Kappe zurückstellen, mit Grund „Verfälschungskappe“ und gezählt. Mindestens den Grund nennen. Die Kappe an einem Kandidaten in T4-Größe messen. |
| 7 | mittel | **Die Torzeile „Schwächen“ ist gebaut, aber nichts ruft sie auf.** Außerhalb der Tests ruft nur `s1/torzeile_schwaechen_t3.py` sie auf, ein Tor-4-Skript gibt es nicht. „Verbindlich in der Torzeile“ (§5, R4-18) ist damit nicht erzwungen; so war es schon bei Review 03 Nr. 9b. Nach dem Masterprompt v8 hat T4 statt versiegelter Schwächen „eine unabhängig erhobene Altlastenliste“. Ohne Normalvergleich je Eintrag ergibt die Zeile dort 0 %, wie am T3-Werk (0 von 5). | `bash /tmp/review-vor-t4-04/grep1.sh`: in `biotop/` nur die Definition `biotop/kern/gegenzeugen.py:47`, in `pruefung/` kein Aufrufer; Masterprompt v8, Tor 4, Zeilen „Aufnahme“ und „Schwächen“ | Das Tor-4-Skript mit dieser Zeile anlegen und einen Wächtertest schreiben, der den Aufruf verlangt. Vor T4 festlegen, was der Normalvergleich einer Altlast ist (Offen Nr. 3 des Berichts). |
| 8 | mittel | **Fehlt die Stufe 2, misst der Lauf ohne Einspruch an Stufe 1.** `ref_lz = referenzlast_laufzeit or referenzlast` in `aegis.py` und `lauf.py`; der Vorspann setzt `laufzeit_stufe = 1` und misst weiter. Bei T4 (neues Werk) hängt Entscheidung 1 also daran, dass jemand `<werk>.stufe2.*` schreibt. Sonst entscheidet die Nische „schnell“ wieder an einer Last, an der K2904 und K3091 genau an der Schwelle lagen. Sichtbar ist das nur als `laufzeit_stufe: 1`. Auch die Verweigerung bei 60 s ist ungetestet: `test_s_vorspann_verweigert_zu_langsame_stufe2` prüft nur die Konstante `== 60`. | `biotop/organe/vorspann.py:163-178`; `biotop/lauf.py:392-394`; `KERN-COMMIT.patch.txt:1108-1111, 2024-2026` | Der Vorspann verweigert den Lauf ohne Stufe 2 oder verlangt eine ausdrückliche, protokollierte Freigabe. Dazu ein Test mit gestellter Kammerlaufdauer ≥ 60 s, der die Verweigerung prüft. |
| 9 | mittel | **Lastaufrufe haben immer das gewöhnliche Muster `[]`.** Das ist die Lesart des Berichts von Entscheidung 3. Folge: Zeigt nur ein Lastaufruf eine Abweichung, weil die Eingabe der Last Tab oder Zeilenumbruch trägt, dann deckt sie jeder Test, der die Funktion mit gewöhnlicher Eingabe festhält. Das ist die Lage aus Review 03 Nr. 1, nur über die Last statt über die Sonde. In x1 und K2868 fingen die Formvarianten der Sonde dieselbe Regression ab. Ohne passende Formvariante fängt sie niemand, etwa wenn nur lange, mehrzeilige Eingaben brechen. Entscheidung 3 spricht von den Veränderungen der Sonde; zu Lastaufrufen sagt sie nichts. Gelesen, nicht gemessen. | `KERN-COMMIT.patch.txt:381-383` (Python `kl=[]`), `:849` (TypeScript); BERICHT §3 | Philipp entscheiden lassen: Lastaufrufe mit den Formmerkmalen ihrer Eingabe führen oder gewöhnlich lassen. Probe dazu: Die Last ruft `normieren` mit einem langen mehrzeiligen Text, und der Kandidat bricht nur dort. |
| 10 | mittel | **`pathlib.Path` (relevant für T4): Rückgaben sind inhaltslos, Argumente gelten neu als veränderlich.** `kan(Path('x/y.txt'))` ergibt `{"__klasse": "PosixPath", "felder": {}}`, für jeden Pfad dasselbe. Gibt eine Funktion einen anderen Pfad zurück, bleibt das unsichtbar. Das ist vorbestehend und lokal gemessen. Neu seit `1d9a5aa`: `_instanz(Path)` ist wahr (wegen der Slots), und `_felder` hängt an Lazy-Caches. Vor dem Zugriff gibt es 1 Feld, nach `.name` bzw. `str()` 4 bis 5. Schnappschuss und Mutation bearbeiten damit Pfad-Interna; die Folgen habe ich nicht gemessen. | `lokal_proben2.out.txt:3-11`; `verhalten.py:117-119`, `_instanz` | `os.PathLike` als Wert kanonisieren (`os.fspath`) und vom Zustandsvergleich und von der Mutation ausnehmen. Probe: Eine Funktion gibt einen anderen Pfad zurück. |
| 11 | niedrig | **§2 sagt: „Jeder Befund … durch den Laufweg geprüft: `aegis.pruefen`“. Das gilt nicht für alle.** Durch `aegis.pruefen` laufen H1, H2 (x2) und E4. Am Organ laufen H3, H4, R4-5, R4-6 und R4-13 (`_organ` → `vv.pruefen`), außerdem R4-14 und R4-3 (Sonde gestellt). Der Fixture-Fall ruft `vv.deckende_aufrufe`. E3 und die Parität prüfen Modulfunktionen. | `KERN-COMMIT.patch.txt:1748-1776`; `KERN-COMMIT-2.patch.txt:68-90` | §2 nach Laufweg und Organ trennen. |
| 12 | niedrig | **Weitere Aussagen gehen über ihren Beleg hinaus.** (a) §1: „die Sonde … bleiben, wie sie waren“. Die Sonde wurde in dieser Runde stark geändert (`verhalten.py` 293 Zeilen im Diff); gleich geblieben ist nur, dass sie an Stufe 1 läuft. (b) §2: „Python und TypeScript rechnen gleich“. Belegt sind 19 von 19 Proben. Lokal weichen 2 von 14 weiteren ab: `"\ufeffa b"` ergibt in TS `rand_vorn`, in Python nicht; bei `"\x85a"` ist es umgekehrt. (c) §3 und §12 Nr. 2: „Randwerte … tragen kein Merkmal“. Sie tragen Formvarianten-Merkmale, wenn ihre Zeichen welche auslösen: `'Ä-1'` → `['gross']`, `'  '` → `doppelleer, rand_hinten, rand_vorn`. (d) §1: „quadratisch → linear“ ist gefolgert, nicht gemessen. (e) §12 Nr. 1: „Median 6,3 s → 9,9 s“. Gepoolt über je 12 Kammerläufe sind es 6,2 → 9,8 s; 6,3/9,9 ist das Mittel der beiden Einzelmediane. Der Faktor ≈ 1,6 stimmt. | `lokal_proben.out.txt:14-18, 22-27`; `proben/STUFE2-ZEITEN.txt:1-4, 7-10`; `COMMIT-STAT.txt:24` | Die Sätze genauer fassen. |
| 13 | niedrig | **„Zehnfache Eingabegröße je Bereich“ gilt für die Mengen, nicht für jeden Aufruf.** In allen 5 Bereichen ist die Hauptmenge zehnfach. In `last_zahlen` bleiben aber `verteilen(1001, [1, 2, 3])` und `prozent(1337, 12.5)` gleich groß. `last_tarife` wiederholt dieselben 150 Werte zehnmal (`j = i % 150`). Eine Verschlechterung in `verteilen` würde Stufe 2 nicht verstärken. | `KERN-COMMIT.patch.txt:637-649, 670-677` | Im Bericht nennen oder auch diese Aufrufe vergrößern. |
| 14 | niedrig | **Die Eichproben des Vorspanns messen die Laufzeit an Stufe 1, die Toleranz stammt aus Stufe 2.** `eichproben.py:525` ruft `aegis.pruefen` ohne `referenzlast_laufzeit`; der Vorspann übergibt `ref` (Stufe 1). Die Probe des Annahmepfads vor dem Lauf misst damit an einer anderen Last als der Lauf selbst. | `biotop/organe/eichproben.py:525`; `vorspann.py:203-204` | `referenzlast_laufzeit` durchreichen. |
| 15 | niedrig | **In den gespeicherten Maßen mischen sich die Stufen.** Die Einzelmessung `messgeraet.messen` läuft an Stufe 1: für Ausgang, gen0 und `mass` (`lauf.py:93, 201, 597, 788`) und in `aegis.py:1026-1027`. `laufzeit_einsetzen` überschreibt `laufzeit_ms` mit gepaarten Medianen aus Stufe 2. `laufzeit_ms` einer Generation stammt also je nach Fall aus Stufe 1 oder Stufe 2 (Faktor etwa 7 bis 38 je Bereich), ohne Kennzeichen am Wert. Die Entscheidung vergleicht gepaart und ist nicht betroffen. Kurven und Torzeilen über gespeicherte `laufzeit_ms` mischen aber, z. B. `pruefung/tor2.py:44` oder die T4-Zeile „Kein Rückschritt … einschließlich Laufzeit“. Gelesen. | `biotop/kern/messgeraet.py:709-723`; `proben/STUFE2-ZEITEN.txt` | Die Stufe je Messwert speichern oder Stufe-2-Werte in ein eigenes Feld schreiben. Das Tor-4-Skript liest nur Werte derselben Stufe. |
| 16 | niedrig | **`eigene_tests` rechnet mit Funktionsnamen, `behoben` mit pytest-IDs.** Bei parametrisierten Tests (`test_neu[1]`) greift der Ausschluss deshalb nicht. Lokal: `eigene_tests` liefert `{'test_p.py::test_neu'}`, `…[1]` fehlt. Heute ist das folgenlos, weil `nur_funktionen` parametrisierte Kandidatentests gar nicht aufnimmt (lokal → `None`). Das ist eine eigene, vorbestehende Lücke: Gültige parametrisierte Behebungstests kommen nie ins Werk. Der TS-Zweig (`typescript.testfunktionen`, ein Kammeraufruf je Datei und Stand) hat keinen Test und steht außerhalb des `try` um den Verhaltensvergleich (gelesen). | `lokal_proben.out.txt:19-21`; `lokal_proben2.out.txt:12-14`; `biotop/organe/aegis.py:358-385, 1112` | Einheitliche ID-Form (Parameter abschneiden). Einen TS-Fall für E4 ergänzen. |
| 17 | niedrig | **Koroutinen laufen beim Erzeugen in einer eigenen Schleife (gelesen, nicht gemessen).** Läuft beim Erzeugen keine Schleife, führt die Sonde die Koroutine sofort aus. Wartet der Aufrufer später in seiner eigenen Schleife auf sie und hängt sie an Objekten dieser Schleife (Queue, Event, Lock), ändert die Sonde das Verhalten. Der Aufruf in einer laufenden Schleife (p23) ist keine stille Stelle: Der Lastaufruf zählt als unvergleichbar, der Korpus sieht 14 Abweichungen. | `KERN-COMMIT.patch.txt:218-259`; `kammerprobe.out.txt:12` | Eine Probe mit einer schleifengebundenen Koroutine. Bei einem Fehler aus einer fremden Schleife enthalten statt ablehnen. |
| 18 | niedrig | **Das Nachspiel hat keinen Durchlauf in der Regression.** Der Wächtertest prüft nur statisch die Namensbindungen in `vorbereiten`. Genau diese Lücke ließ an `1d9a5aa` 7 von 7 Nachspielen abbrechen, bei grüner Regression (562/2/0). Das Nachspiel ist das Instrument aller Gegenproben dieser Runde. | `KERN-COMMIT-2.patch.txt:116-133`; `JOB-COMMIT-REGRESSION.txt:53`; `nachspiel/NACHSPIEL-D1..3.txt` | `vorbereiten` und `spielen` mit gestellter Kammer als schnellen Test in die Regression aufnehmen. |

## Antworten auf die Prüfpunkte

**a) Auftragspunkte, getrennt nach Laufweg und Modul/Organ**

Zeichen: ✓ = erfüllt, ✗ = nicht erfüllt.

1. **Stufe 2**
   - Laufweg: ✓ N1–N3 über `nachspiel.spielen` → `aegis.pruefen`, 7 von 7 Fällen, `laufzeit_stufe` = 2. ✓ `test_s_stufe2_wird_im_annahmepfad_genutzt`. Generalprobe und Verhandlung habe ich nur gelesen (`lauf.py:392-394, 690-691`). Der Beleg `SPION` zeigt nur, dass `gewinn_bestaetigen` erreicht wird, nicht an welcher Stufe.
   - Modul: ✓ `test_s_stufe2_suche…`. Die 60-s-Grenze ist nur als Konstante getestet (Nr. 8).
   - Gegenprobe: ✓ 3 von 3 je Kandidat.
   - „T3 unverändert“:
     - ✓ Die Stufe-1-Datei steht in keinem der beiden Commits.
     - ✓ Die Sonde und `beobachten()` laufen an Stufe 1: `aegis.py:1118-1120` übergibt `referenzlast`.
     - ✓ Die T3-DB hat in 7 von 7 N-Belegen vorher und nachher dieselbe Prüfsumme.
     - ✗ Der Code der Sonde hat sich geändert. Ein heutiges Nachspiel eines T3-Kandidaten urteilt deshalb anders; bei K2868 sind jetzt 16 Beobachtungen gedeckt statt 0. Das ist so gewollt, aber §1 sagt etwas anderes (Nr. 12a).
2. **Die vier hohen Befunde**
   - Laufweg: H1 und H2 sowie meine Proben x1, x1k, x2, x2k.
   - Organ: H3 und H4 sowie meine Proben p18, p18b, p19, p19b, p20.
   - Die Probenfälle sind geschlossen, die Klassen nicht (Nr. 1–5).
3. **Muster**
   - Modul: `test_e3` ruft `_muster_von` direkt.
   - Laufweg: K2868 in N1, 1 von 1 Fall, abgelehnt wie verlangt.
4. **Eigene Tests**
   - Laufweg: `test_e4_*`, 2 Fälle durch `aegis.pruefen`.
   - Modul: `test_e4_eigene_tests_am_organ`.
   - Für TypeScript gibt es keinen Fall (Nr. 16).
5. **Torzeile und TS-Methoden**
   - Die Torzeile ist nur als Modul belegt: 4 Unit-Fälle und das s1-Skript. Sie hat keinen Aufrufer (Nr. 7).
   - Die TS-Methoden stehen auf der Liste; das ist begründet.
6. **Fehlalarm**
   - Die Datei ist vorhanden, ihre Gliederung habe ich geprüft (siehe unten).

Scheitern die Gegenproben an der vorgesehenen Zusicherung? An `0aac612` scheitern 13 der 17 roten Fälle an ihrer Zusicherung. Die übrigen 4 scheitern an einer fehlenden Schnittstelle: `test_e3`, `test_e4_eigene_tests_am_organ` und die Parität mit `AttributeError`, der Fixture-Fall mit `TypeError`. Für diese 4 ist „vorher rot“ kein Verhaltensnachweis (`proben/VORHER-0aac612.txt`).

**b) Stufe 2**
- **Eingabegröße:** Die Mengen sind in 5 von 5 Bereichen zehnfach. Ausnahmen siehe Nr. 13.
- **Kammerlauf < 60 s:** 12 von 12 Läufen in `STUFE2-ZEITEN`, der längste mit 11,7 s. Dazu 7 von 7 Rauschmessungen in den Nachspielen; ihr jeweils längster Kammerlauf dauerte 10,6 bis 11,5 s.
- **Rauschen und Gewinn an derselben Stufe:** ja.
  - Im Vorspann: `ref2` mit `eichung.laufzeit_einmal` → `messgeraet.laufzeit_messen`, dasselbe Instrument wie die gepaarte Messung.
  - Im Nachspiel: 7 von 7 Belegen „an Stufe 2 gemessen“.
- **Gesperrte Bereiche:** nicht still (`gesperrte_bereiche` in `tausch` und im Beleg), aber häufiger. `eingang` war in 3 von 6 Stufe-2-Nachspielen gesperrt. An Stufe 1 war in den Läufen 37/38 keine von 10 Bereichsmessungen gesperrt (Tabelle `eichung`, `eingang` 2,34–3,08 ms).
- **Rückfall auf Stufe 1:** wird vermerkt, aber nicht verweigert (Nr. 8).

**c) Deckung**
- Merkmale je Formvariante: ✓ (16 `FORM_MERKMALE`).
- Muster = eingeführte Merkmale: ✓ (E3, K2868).
- Verfälschung je Merkmal: ✓ für x2.
- Kann ein Test decken, ohne das Merkmal festzuhalten? Ja, gemessen (Nr. 1).
- Fixture-Fehler: ✓, belegt am Organ.
- Kann ein Kandidat über einen geänderten Vorgenerations-Test decken? Nein. Er kann einen vorhandenen Test nicht ändern (`aegis.py:903-905` lehnt nach Anhang A Satz 6 ab), und `eigene_tests` erfasst geänderte Tests zusätzlich.
- Vertragsdateien des Kandidaten: in `eigene_tests` enthalten ✓.
- Tests aus der Anpassung des Nachbarn (`extra_code`): Sie liegen nicht an der Vorgeneration und können deshalb nicht in `behoben` gelangen (gelesen).
- Python und TypeScript: gleich bis auf 2 Sonderzeichen (Nr. 12b). Die TS-Zweige ohne eigene Probe stehen unter „Nicht geprüft“.

**d) Proben des Gutachtens 03 gegen `43b8fad`**

Von 16 Originalfällen habe ich 14 neu gefahren: aus `deckprobe` 4 von 4, aus `sondenprobe3` 7 von 9 (ohne p15, p17b), aus `sondenprobe4` 3 von 3. Alle 14 verhalten sich wie spezifiziert:

| Fall | Ergebnis an `43b8fad` |
|---|---|
| x1 | abgelehnt, 0 von 14 `ValueError`-Beobachtungen gedeckt |
| x1k | abgelehnt |
| x2 | abgelehnt, 0 von 6 gedeckt; festhaltend für `tab` leer |
| x2k | abgelehnt |
| p13 | 16 Abweichungen |
| p14 | tragfähig, Kappe gezählt (14) |
| p16, p16b | je 4 Abweichungen, Instanz `signatur_erprobt` |
| p17 | 1 Abweichung (`@mutation`), wie in Runde 3 |
| p18, p18b | je 6 Abweichungen |
| p19, p19b, p20 | je 28 Abweichungen |

Dazu 10 neue Fälle:
- Stille Stellen: p21, p22, p18c.
- Messgerätausfall: q1.
- Deckungslücke: x3.
- Kontrollen wie erwartet: x3k, q1k, p22k, p18ck.
- p23 (Koroutine in laufender Schleife): keine stille Stelle.

**e) Zahlen:** siehe „Geprüft und bestätigt“.

**f) Geänderte ältere Tests:** In 3 von 3 Dateien handelt es sich um Spezifikationsänderungen:
- Merkmal `tab` statt `weissraum`.
- Der Schlüssel der Verfälschungstabelle trägt das Merkmal.
- Die richtige Behebung braucht je einen Test für Tab, Zeilenumbruch, CRLF und NBSP.

Jede Gegenprobe bleibt erhalten; die neue Zusicherung in `test_b_gegenprobe…` ist gleich stark wie die alte. Eine Lockerung habe ich nicht gefunden. Der Nachtrag ändert keine älteren Tests.

**g) Aussagen und Lücken**
- Aussagen, die über ihren Beleg hinausgehen: Nr. 1, 2, 4, 11, 12. Lücken gegenüber dem Auftrag: Nr. 7, 8.
- Die Liste im Bericht:
  - R4-17 (vor T5) und R4-19 (fehlender Laufweg-Beleg) sind begründet und gefährden T4 nach meiner Lesart nicht.
  - Zwei Zeilen mit „gebaut“ sind nur teilweise gebaut: R4-12 (Kappe → Ablehnung, Nr. 6) und R4-18 (kein Aufrufer, Nr. 7).
  - R4-3, R4-4 und R4-13 sind für ihre Probenfälle gebaut, die Klassen aber nicht geschlossen (Nr. 2–5).
- Für T4 gefährlich sind die Nr. 1, 2, 4, 6, 7, 8 und 10.

## Geprüft und bestätigt

- **Commits:** `git log` zeigt `43b8fad` → `1d9a5aa` → `0aac612`. `COMMIT-STAT` nennt 18 Dateien, `COMMIT-2-STAT` 3. `versandwerk-t3-02.mjs` steht in keinem der beiden Commits. Der sha256 der Stufe-2-Datei an HEAD (`9814e717…`) ist gleich `ref2_sha256` in `STUFE2-ZEITEN.json`; die Zeiten wurden also an derselben Datei gemessen.
- **Stufe-2-Zeiten (§1):**
  - Tabelle: 8 von 8 Werten bestätigt.
  - „12 von 12 unter 60 s, längster 11,7 s“ bestätigt.
  - „rund 45 Punkte unter der Schwelle“ bestätigt (0,85 − 0,40).
- **Gegenprobe Entscheidung 1 (N1–N3):**
  - 7 von 7 Belegen: Code-Stand `43b8fad`, Arbeitsbaum sauber, 0 Modellaufrufe, Stufe 2, T3-DB mit gleicher Prüfsumme.
  - K2904 überlebt in 3 von 3 Durchgängen, K3091 in 3 von 3.
  - `planung`-Quoten: 6 von 6 wie in der Tabelle in §1 (0,376/0,392; 0,454/0,455; 0,429/0,414), alle „klar“.
  - Band 0,715 … 1,011 bestätigt (0,85/1,189 und 0,85 × 1,189 bei N2 K2904).
  - `eingang` gesperrt in 3 von 6 Fällen: N1 K2904, N2 K2904, N3 K3091.
  - K3091 N3: erste Messung in `tarife` ×1,158 und in `zahlen` ×1,236, gegen die Toleranzen 1,15 und 1,16.
  - „Nur bestätigte Gewinne“ im Grund: 2 von 2 Fällen (N2 K2904, N3 K3091).
- **D1–D3 an `1d9a5aa`:** 7 von 7 Nachspielen abgebrochen (`AttributeError`); das ist richtig berichtet.
- **K2868 (N1, §3), 6 von 6 Angaben bestätigt:**
  - abgelehnt;
  - 40 Abweichungen, davon 24 ungedeckt (20 Weißraum, 4 `zahlform_null_vorn`) und 16 gedeckt (`rand#2`, `#5`, `#6` und `form#8`, je 4);
  - die deckenden Tests sind die 3 Befundklassen-Tests des Anklägers, mit den Klassen `gross` und `lang`;
  - 2 Verfälschungsläufe, 0 ausgelassen;
  - `eigene_tests_ausgeschlossen` ist leer.
- **Vorher/Nachher:**
  - 6 von 23 Fällen grün an `0aac612`, 23 von 23 an `1d9a5aa`.
  - Die 23 Fälle nachgezählt: H 12, E3 1, E4 3, R4-5 2, R4-6 2, R4-13 1, R4-14 1, Parität 1.
  - Die Tabellenzeilen in §2 und §4 stimmen mit `VORHER-0aac612.txt` überein, zum Beispiel „Kernmaß −13 → −2 (+11)“.
- **Torzeile am T3-Werk (§5):** 2 von 2 Zeilen stimmen mit `s1/TORZEILE-SCHWAECHEN-T3-am-commit.txt` überein.
- **Regression aus den `.txt`-Dateien, 2 von 2 Läufen:**
  - `1d9a5aa`: 562 bestanden, 2 übersprungen, 0 fehlgeschlagen, 93 abgewählt, 1627,90 s.
  - `43b8fad`: 569 bestanden, 2 übersprungen, 0 fehlgeschlagen, 1656,90 s.
  - Die Differenz von 7 sind die neuen Tests des Nachtrags (2 + 4 + 1). `test_vor_t4_04` hat 36 Fälle (29 + 7), aus dem Diff nachgezählt.
  - Teillauf 5: 64 bestanden.
- **R4-11 (`SPION-GEWINN.txt`):** 1 Aufruf aus `lauf._generation_koerper`, `ergebnis: bestaetigt`, `gewinn: false`.
- **Geänderte ältere Tests:** 3 von 3 Dateien im Diff gelesen (siehe f).
- **Fehlalarm-Text:** 6 Abschnitte. Die Suche nach 7 Projektbegriffen (biotop, versandwerk, aegis, K2xxx, chat-claude, philipp, Lauf 37/38) ergab 0 Treffer.
- **Laufweg der Stufe 2 (gelesen):**
  - `aegis.pruefen`: gepaarte Messung, Riss- und Gewinn-Nachmessung mit `ref_lz`.
  - `lauf._generation_koerper`: 3 Aufrufe mit `ref_lz`.
  - `_verhandeln` gibt `referenzlast_laufzeit` weiter.
  - Die Stufe-2-Last steht im Quellen-Siegel (`vorspann.py:63`).

## Nicht geprüft

- **JUnit-Zahlen und Verdrahtungsbelege aus §8** (564 bzw. 571 Fälle, 23 von 23 Organen, 0,00 €): Mein Leseversuch löste eine Freigabeabfrage aus (siehe „Sperren“) und scheiterte danach an einem eigenen Skriptfehler (`TypeError`). Ich habe ihn nicht wiederholt.
- **Nicht gelesen:** `KASSE.md`, der Endstand von `UEBERGABE.md`, `TEILLAUF-1..4`, `KETTE*.txt`, `bau/r4_*.py` und `sperre/`.
- **Nachspiel-Belege:** Die DB-Prüfsumme habe ich in 7 von 15 Belegen geprüft (n1–n3), in den übrigen 8 nicht (d1–d3, Vorprobe). Ebenfalls nicht geprüft: die Nachmessungswerte von K3091 N3 (×1,055 bzw. ×0,968) und die Angabe „Runde 3: 0 von 10 mit Riss“.
- **Inhalt des Fehlalarm-Texts:** nur Gliederung und die Begriffssuche.
- **TypeScript:** Verfälschung je Merkmal, Fehler in Aufbau-/Abbau-Haken und `eigene_tests` über `typescript.testfunktionen` habe ich nicht mit einer eigenen Probe geprüft. Die Parität habe ich an 14 Zusatzproben gerechnet.
- **Generalprobe und Verhandlung an Stufe 2:** nur gelesen, ein Lauf war nicht erlaubt. Die Verweigerung bei 60 s habe ich nicht ausgeführt.
- **Nicht neu gefahren:** p15 und p17b. Nicht als eigene Probe gefahren: der verkettete Aufruf ohne Zusicherung (Nr. 1), das Lastaufruf-Muster (Nr. 9), die `Path`-Rückgabe (Nr. 10), `itertools.groupby` und eine schleifengebundene Koroutine (Nr. 17).
- **Dateien, die während meiner Prüfung neu entstanden,** habe ich nicht gelesen: `nachspiel/AUSWERTUNG-NACHTRAG.txt`, `EINZELHEITEN.txt`, `proben/FUEHRENDE-NULL.*`, `LESEN-NACHFRAGEN.*`, `veroeffentlichen.py`.
- **Masterprompt v8:** nur den Tor-4-Abschnitt per Suche.

## Sperren

Eine Freigabeabfrage. Der Nutzer hat sie freigegeben, der Befehl lief. Ich habe diesen Schritt danach beendet und nicht wiederholt.

Befehl, wörtlich:

```
cd /tmp/review-vor-t4-04 && stat -c '%y %s %n' kammer_auswerten.py KAMMERPROBE.json && head -5 kammer_auswerten.py && python3 -c "
import json,xml.etree.ElementTree as ET
d=json.load(open('/root/biotop-vor-t4-04/VERDRAHTUNG-BELEG-REGRESSION-2.json'))
print('organe',len(d['organe']),'gerufen',d['gerufen'],'nie_gerufen',d['nie_gerufen'],'kosten',d['modellkosten_eur'],'nachmessungen',len(d.get('nachmessungen') or []))
r=ET.parse('/root/biotop-vor-t4-04/REGRESSION-2.junit.xml').getroot()
tc=list(r.iter('testcase'));print('junit2 faelle',len(tc),'failure',sum(t.find('failure') is not None for t in tc),'error',sum(t.find('error') is not None for t in tc),'skipped',sum(t.find('skipped') is not None for t in tc))
"
```

Meldung der Ausführungsschicht, wörtlich:

> Command required approval (Security scan — [HIGH] Nested executable body could not be resolved: The shell will execute a grouped, encoded, or dynamically selected value, but Tirith cannot prove the complete executable body. The command is blocked instead of trusting its benign-looking outer leader.; [HIGH] nested command analysis was incomplete: A destructive command may be hidden beyond Tirith's bounded nested-shell depth, lexical-candidate, input, or retained-body budget.) and was approved by the user.

- **Einordnung:** Freigabeabfrage der Sicherheitsprüfung, vom Nutzer freigegeben.
- **Ergebnis:** `stat` und `head` liefen. Danach brach `TypeError: object of type 'int' has no len()` aus meinem eigenen Python-Teil ab. Die Daten, die der Befehl lesen sollte, stehen unter „Nicht geprüft“.
- **Eigener Fehler:** Ein mehrteiliger Einzeiler verstößt gegen die Regel „lange Befehle als Skript“.

## Schreibort-Nachweis

**Unter `/root/`:** nur `/root/biotop-vor-t4-04/REVIEW.md` (diese Datei).

**Unter `/tmp/review-vor-t4-04/`** (TMPDIR der Läufe: `tmp/`, am Ende leer):
- **Lesende Skripte:** `status.sh`, `grep1.sh` bis `grep11.sh`, `warte.sh`, `abschluss.sh`, `db_eichung.py` (Lauf-DB, `mode=ro`).
- **Lokale Rechenproben ohne Kammer:** `lokal_proben.py` mit `lokal_proben.out.txt`, `lokal_proben2.py` mit `lokal_proben2.out.txt`.
- **Auswertung der N-Belege:** `n_auswerten.py` mit `n_auswerten.out.txt`.
- **Kammerproben:** `kammerprobe.py` (angepasste, zusammengeführte Kopie von `deckprobe.py`, `sondenprobe3.py` und `sondenprobe4.py` aus Gutachten 03, plus 10 neue Fälle), dazu `kammerprobe.out.txt` und `KAMMERPROBE.json`.
- **Probenwerke:** `werke/`, 54 Dateien (18 Organfälle mit je 3 Dateien).
- **`kammer_auswerten.py`** (16:17:01 Uhr): im unterbrochenen Zug geschrieben; seine Ausgabe ist nicht in diesen Bericht eingegangen.

**Nicht von mir:**
- Neue Dateien unter `/root/`, die `find -newer` außerdem zeigt: `/root/.local/share/tirith/log.jsonl`, `log.jsonl.head` und `/root/.local/state/tirith/sessions/…`. Das sind Protokolle der Ausführungsschicht.
- Die Dateien des Auftragnehmers in `/root/biotop-vor-t4-04/`.
- `t3.db-shm` hat den Zeitstempel 15:57:21 Uhr. Das fällt in den Nachspiel-Durchgang N3; mein lesender Zugriff war gegen 15:45 Uhr. `t3.db` und `t3.db-wal` tragen weiterhin den Stand vom 23.09.

**Sonst:**
- Die Kammerläufe gingen über `biotop.organe.kammer` (Docker, netzlos); am Ende liefen 0 Container.
- In `/tmp` sind auf oberster Ebene außer meinem Ordner nur Laufzeitdateien von Hermes neu.
- `git status` von `/root/biotop` war vorher und nachher leer.
