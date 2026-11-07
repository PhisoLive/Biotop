# Review Behebungsrunde 5 vor T4: ein Durchgang

Stand: 2026-09-24, gegen 22:00 Uhr. Ein unabhängiger Reviewdurchgang nach `REVIEW-AUFTRAG.md`.

**Gegenstand**
- **`BERICHT.md`:** Geprüft ist die Fassung mit Platzhaltern, gelesen gegen 20:40 Uhr. Offen waren `‹URTEIL›`, `‹ERGEBNIS›`, `‹T4›`, `‹REGRESSION›`, `‹NACHSPIEL›`, `‹VORHER_NACHHER›`, `‹REVIEW›`, `‹SPERREN›` und `‹OFFEN›`.
  - Die um 21:50 Uhr per Skript gefüllte Fassung trägt nur noch `‹REVIEW›` und `‹SPERREN›`. Davon habe ich nur drei Stellen gegen die Quellen gehalten: §4 „Messung in T4-Größe“, §9 (Regression, Nachspiele, Vorher/Nachher) und die ersten Zeilen von „Ergebnis“ (R6-1, R6-4).
- **Kern-Commit** `0c2f058` auf `43b8fad` (HEAD, Arbeitsbaum leer). `KERN-COMMIT.patch.txt` habe ich ganz gelesen (2173 Zeilen).
- **Belege** unter `/root/biotop-vor-t4-05/`; die Liste steht unter „Geprüft und bestätigt“.

**Wie geprüft**
- Kein Modellaufruf, kein Netz, kein Geld. Keine volle Regression, kein Verdrahtungstest.
- **Solange `job_kette` lief** (bis 21:40:41 Uhr laut `JOB-KETTE.txt`), habe ich nur gelesen und ohne Kammer gerechnet:
  - `lokal_b.py`: `kan()` der Python-Sonde an HEAD, gelesen aus `git show`;
  - `lokal_ts.mjs`: der TS-Kanon an HEAD, mit Node v26.8.2 außerhalb der Kammer.
- **Kammerläufe:** ein Skript, `kammerprobe05.py`. Es ist eine Kopie von `review-proben/kammerprobe.py`, erweitert um 12 neue Fälle.
  - 21:41:03–21:48:02 Uhr, 36 Fälle, echte Kammer `biotop-kammer:1`, HEAD `0c2f058`.
  - Das Skript bricht ab, wenn `pgrep -f job_kette` einen Prozess findet.
  - `git status` war vorher und nachher leer; danach liefen 0 Container.
- Zum Schluss eine lokale pytest-Probe ohne Kammer (`e2b_probe.py`, pytest 9.1.1 im venv).
- Die Lauf-DB habe ich nicht geöffnet; für diese Prüfung war sie nicht nötig.

**Kurzurteil**
- **Die Fälle des Reviews 04 sind geschlossen.** Ich habe alle 24 Proben des Gutachtens 04 an `0c2f058` neu gefahren.
  - Die 5 damaligen stillen Stellen bzw. Ausfälle (x3, q1, p21, p22, p18c) verhalten sich jetzt wie spezifiziert, und p14 ist sichtbar.
  - Keiner der 24 Fälle zeigt eine neue stille Stelle.
- **Die Zahlen stimmen mit ihren Quellen überein:** Regression, Verdrahtung (Register 10 von 10, Tor-4-Zeile, Nachspiel), Nachspiele N1–N3, Vorher/Nachher, Stufe-2-Eichung und T4-Messung (Einzelheiten unter „Geprüft und bestätigt“).
- **Die Klassen sind nicht geschlossen.** Drei hohe Befunde, zwei davon in der Kammer gemessen:
  - **Nr. 1:** Eine `isinstance`-Zusicherung oder ein Selbstvergleich hält `tab` fest, ohne ihn zu unterscheiden. Der Tab-Rückschritt **überlebt durch `aegis.pruefen`**.
  - **Nr. 2:** Umgekehrt hält ein gewöhnliches `assert f(1) == 3` nichts fest. Das deckt sich mit R6-4 des Auftragnehmers; ich habe es unabhängig gemessen (3 von 5 Formen).
  - **Nr. 3:** Die Vollständigkeitsprüfung ist selbst blind für Zustand in C-Typen, im TS-Kanon für Array, Map, Set, Error und Date. In der Kammer ergab das **0 Abweichungen, tragfähig** (p24b, p25).
- **Mittlere Befunde:**
  - Fehlalarm: eine unveränderte Funktion stellt das ganze Urteil zurück (Nr. 4).
  - Eine geänderte Funktion im Sondenausfall bleibt tragfähig (Nr. 5).
  - Geworfene Ausnahmen werden nur mit ihrem Typ verglichen (Nr. 6).
  - Eine hängende Last führt nach 240 s zum Messgerätausfall (Nr. 7).
  - Die T4-Messung belegt Entscheidung 4 nicht (Nr. 8).
  - Im Tor-4-Skript hat der Zweig für verhaltensändernde Altlasten keinen Test (Nr. 9).

## Befunde

| Nr | Schwere | Befund | Beleg (Datei:Zeile, Befehl, Messung) | Vorschlag |
|---|---|---|---|---|
| 1 | hoch | **Eine fallende Zusicherung hält weiter fest, ohne das Merkmal zu unterscheiden. Gemessen durch `aegis.pruefen`.** Die Regel aus Entscheidung 2 prüft Ort und Art der fallenden Zusicherung, nicht aber, ob sie das Verhalten unterscheidet. Das Verfälschungsobjekt `Verfaelscht` ist ungleich allem, auch sich selbst, und es ist kein `str`. Jede Zusicherung, die das Ergebnis mit sich selbst vergleicht oder nur den Typ prüft, fällt deshalb in der Testdatei. **x5:** K2 gibt Tab-Text unverändert zurück. Der Werkstest sichert `assert isinstance(normieren("a\tb c"), str)` und `assert normieren("a b") == "a_b"` zu; die Soll-Tests sind dieselben wie in x3. **x5b:** Der Werkstest sichert stattdessen `assert normieren("a\tb c") == normieren("a\tb c")` zu. **Ergebnis: beide überlebt.** „Kernmaß −12 → −2 (+10)“, 52 Abweichungen, 0 ungedeckt, 6 von 6 Tab-Rückschritt-Beobachtungen gedeckt; `festhaltend normieren\|rueckgabe\|tab` = `[test_normieren_x]`. Beide Zusicherungen gelten an der Vorgeneration und am Rückschritt gleichermaßen. x3 selbst ist geschlossen: abgelehnt, `festhaltend` für `tab` leer. In TypeScript ist es gleich (gelesen): `expect(typeof f(x)).toBe('string')` fällt am Verfälschungsobjekt. | `/tmp/review-vor-t4-05/kammerprobe05.py` (Fälle x5, x5b, x3, x3k); `kammerprobe05.out.txt:1-2, 14-15`; `KAMMERPROBE05.json`; `verhalten.py` (HEAD) Z. 222 ff. (`Verfaelscht`); `KERN-COMMIT.patch.txt:491-501, 672-679`; `biotop/kern/ts/deck-setup.mjs:9` | Festhalten nur zählen, wenn **dieselbe Zusicherungszeile** an der Vorgeneration unverfälscht fällt und unter Verfälschung am Kandidaten fällt; das war schon der Vorschlag zu Review 04 Nr. 1 und ist nicht gebaut. Alternativ mit einem typgleichen, anderen Wert verfälschen statt mit „gleich nichts“. x5 und x5b als rote Spezifikationen, x3k als Kontrolle. |
| 2 | hoch | **Gewöhnliche Zusicherungen halten nichts fest.** Das ist die Gegenrichtung von Nr. 1 und deckt sich mit R6-4 des Auftragnehmers (BERICHT-Fassung 21:50); ich habe es unabhängig gemessen. pytest streicht „AssertionError: “ aus `reprcrash.message`, wenn die Meldung keine Anführungszeichen enthält; `_zusicherung_faellt` verlangt aber dieses Präfix. **Lokal gemessen** (pytest 9.1.1, Regel aus HEAD): `assert f(1) == 3` (Meldung `'assert 2 == 3 …'`), `assert [f(1)] == [3]` und `assert f(1) > 5` halten **nicht** fest, 3 von 5 Formen. Mit Anführungszeichen (`'2' == 'drei'`) oder mit eigener Meldung halten sie fest, 2 von 5. `VORPROBE-E2` prüfte 5 Formen, alle mit Anführungszeichen oder eigener Meldung. §2 („5 von 5 … wie angenommen“) belegt die Regel deshalb für den häufigsten Fall nicht. **Folge:** Richtige Behebungen mit Zahl- oder Listentests werden abgelehnt. In `T4-GROESSE` bleiben 168 von 324 Abweichungen auch ohne Kappe ungedeckt. | `/tmp/review-vor-t4-05/e2b_probe.py`, `e2b_probe.out.txt:1-6`; `proben/VORPROBE-E2.txt`, `proben/vorprobe_e2.sh`; `KERN-COMMIT.patch.txt:496-501`; `proben/T4-GROESSE.txt:3` | Die Art am Ausnahmetyp bestimmen: `call.excinfo` in `pytest_runtest_makereport`, `AssertionError` oder `Failed`. Den Ort weiter an der Absturzstelle prüfen. Die Vorprobe um Zahl, Liste, Vergleich und Wahrheitswert erweitern und in der Kammer fahren (pytest 8.3.3). |
| 3 | hoch | **Die Vollständigkeitsprüfung ist selbst blind für Zustand, den `object.__getstate__` nicht kennt. „0 Abweichungen, tragfähig“ bleibt möglich.** Kammer, am Organ `verhaltensvergleich.pruefen`: **p24b:** `schreibe(puffer, n)` schreibt `'x'*n` bzw. `'y'*n` in ein `io.StringIO`-Argument. Ergebnis: geurteilt, **tragfähig, 0 Abweichungen, „1 von 1 beobachtet“, keine Enthaltung.** **p25:** `netto(5)` gibt `Betrag(10)` bzw. `Betrag(15)` zurück (`class Betrag(Decimal)`). Ergebnis: dasselbe. **Ursache:** `_instanz` greift, sobald ein (auch leeres) `__dict__` da ist. `felder` ist dann `{}`, und auch `object.__getstate__` liefert nichts: Der C-Zustand fehlt in beiden Aufzählungen, und die Prüfungen auf Darstellung und Iterator werden übersprungen. Dasselbe `StringIO` zählt als Rückgabe als „Iterator-Objekt, unvollständig“ (p24: Enthaltung), als Argument oder Attribut aber als „vollständig, `felder: {}`“. **Lokal**, `kan()` an HEAD: 13 von 13 Paaren mit verschiedenem Zustand bleiben blind und ohne Meldung: Unterklassen von `Decimal`, `date`, `deque`, `StringIO` und `array`; ein Deskriptor mit Zustand außerhalb der Instanz; eine Property über Closure; `memoryview`; das Ziel einer `weakref`; die Fabrik eines `defaultdict`; die Argumente eines `partial`; ein Attribut einer Ausnahme; eine Ausnahmemeldung ab Zeichen 200. Die Kontrollen sehen 4 von 4. **TypeScript**, lokal an `kanon.mjs` (HEAD): 6 von 6 blind: Closure, private Daten in einer WeakMap, Unterklassen von `Map`, `Error` und `Date` mit eigenem Feld, ein Array mit Zusatzfeld. `vollstaendig()` läuft nur im allgemeinen Zweig; Array, Map, Set, Error und Date werden nie geprüft. Der Bericht (§1 „Grenzen“) nennt davon nur Closures und C-Erweiterungen „mit eigener Darstellung ohne Adresse“. | `kammerprobe05.out.txt:3-5` (p24, p24b, p25); `/tmp/review-vor-t4-05/lokal_b.py` → `lokal_b.out.txt:2-18`; `lokal_ts.mjs` → `lokal_ts.out.txt:1-8`; `KERN-COMMIT.patch.txt:98-127, 213-233, 854-893` | Als unabhängige Aufzählung zusätzlich den Zustand aus `__reduce_ex__(4)` heranziehen; er enthält den C-Zustand von Decimal, date, deque, StringIO und array. Oder jedes Objekt mit einer C-Basis außer `object` als „C-Zustand nicht erfasst“ enthalten lassen. Ausnahmen mit `args` und `__dict__` führen, die Meldung ungekürzt. In TypeScript `vollstaendig()` auch auf Array (Schlüssel außer den Indizes) sowie Map, Set, Error und Date (eigene Schlüssel) anwenden. p24b, p25 und die TS-Unterklassen von `Error` und `Map` als rote Spezifikationen. |
| 4 | mittel | **Fehlalarm: eine gewöhnliche, unveränderte Funktion stellt das ganze Urteil zurück.** Der Bericht nennt die Klasse als Offen Nr. 1 bzw. R6-1; hier kommen weitere Arten und eine Gegenrechnung an echten Werken dazu. **Kammer, f1:** Ein Objekt hat ein Listeniterator-Attribut (`self._teile = iter(...)`); der Kandidat ändert nur `doppel`, verhaltensgleich (`2 * x` → `x + x`). Ergebnis: Enthaltung „unvollständig erfasst“ für 3 unveränderte Funktionen (`Zerleger.__init__`, `Zerleger.weiter`, `zerleger`) und damit zurückgestellt. **Kammer, f2:** Die Last liest einen Generator mit 1.500 Elementen, der Kandidat macht dieselbe verhaltensgleiche Änderung. Ergebnis: Enthaltung „gekappt“. **Lokal:** 5 von 12 gewöhnlichen Python-Werten lösen eine Enthaltung aus: ein Objekt mit Listeniterator, ein dict mit `map`, ein Tupel mit Generator, eine verkettete Liste der Tiefe 14 und eine verschachtelte Liste der Tiefe 14. In TypeScript sind es 6 von 9: `URLSearchParams`, `Headers`, `AbortController` und `TextEncoder` (gemeldet als „private Felder“), `Intl.NumberFormat` und ein Objekt mit Symbol-Schlüssel. **Gegenrechnung an echten Werken:** Die Sonde an der Vorgeneration von `lagerhaus` (7 Module, 42 Funktionen mit Inhalt) und von `logmuehle` (7 Module, 24 Funktionen) findet 0 von 42 bzw. 0 von 24 Funktionen unvollständig, 0 Sondenausfälle, alle Lasten `ok`. An diesen beiden Werken stellt die Enthaltung also nicht massenhaft zurück. | `kammerprobe05.out.txt:8-9` (f1, f2), `:10-11` (w1 lagerhaus, w2 logmuehle); `lokal_b.out.txt:20-31`; `lokal_ts.out.txt:9-17`; `KERN-COMMIT.patch.txt:1415-1424` | Das ganze Urteil nur dann zurückstellen, wenn eine unvollständig erfasste Funktion im Diff oder Wirkungskreis des Kandidaten liegt. Sonst enthalten sich nur ihre Beobachtungen, gezählt. Die Tiefengrenze 12 an rekursiven Strukturen prüfen. Vor T4 dieselbe Gegenrechnung an der Vorgeneration des T4-Werks fahren. |
| 5 | mittel | **Ändert der Kandidat genau die Funktion mit Sondenausfall, bleibt das Urteil „0 Abweichungen, tragfähig“.** **Kammer, a3x:** dieselbe Zählerlast wie in `test_a3`; der Kandidat ändert `naechste` (`return _n[0] - 1`). `naechste` enthält sich mit „Sondenausfall“. Das Urteil ist geurteilt, **tragfähig, 0 Abweichungen, „1 von 2 beobachtet“, `enthaltung` leer.** `aegis.pruefen` stellt nur bei `vv["enthaltung"]` zurück; der Kandidat überlebt also, wenn das Kernmaß ihn trägt (gelesen). Die geänderte Funktion wird so nie verglichen. Das widerspricht dem Grundsatz von Entscheidung 1: nie tragfähig, wenn etwas fehlt. Den Sondenausfall lösen gerade nicht idempotente Funktionen aus, etwa Zähler oder Zwischenspeicher; T3 riss an zwei fehlerhaften Zwischenspeichern. | `kammerprobe05.out.txt:7`; `KERN-COMMIT.patch.txt:1331-1336, 1384-1392, 1217-1221`; `bau/MASTERPROMPT-V8-TOR4.txt:10, 27` | Liegt die Funktion mit Sondenausfall im Diff des Kandidaten, enthält sich das Urteil (zurückstellen, gezählt). Philipp entscheiden lassen. a3x als rote Spezifikation. |
| 6 | mittel | **Geworfene Ausnahmen werden nur mit ihrem Typ verglichen (vorbestehend).** `wert()` liefert für eine Ausnahme `Fehler:<Typ>`; Meldung und Attribute fehlen. **Kammer, p26:** `pruefe(-1)` wirft `ValueError('PLZ ungültig')` bzw. `ValueError('Ort ungültig')`. Ergebnis: geurteilt, **tragfähig, 0 Abweichungen.** TypeScript verhält sich gleich (`'Fehler:' + constructor.name`, gelesen). Bei einem T4-Werk mit Eingabeprüfung gehören die Meldungen zum Verhalten; der Bericht sagt dazu nichts. | `kammerprobe05.out.txt:6`; `lokal_b.out.txt:19`; `verhalten.py` (HEAD) Z. 452-454; `KERN-COMMIT.patch.txt:930-931` | Meldung (Adressen maskiert, über `knapp`) und `__dict__` der Ausnahme in die Beobachtung aufnehmen, oder das Fehlen als gezählte Teil-Enthaltung führen. Philipp entscheiden lassen. |
| 7 | mittel | **Eine hängende Last ist kein Ausfall einer Funktion, sondern ein Messgerätausfall nach 240 s.** **Kammer, d1:** Die Last legt ein Element in eine `queue.Queue` und ruft `hole(0)`. Die Sonde ruft `hole` mehrfach auf, und der zweite `Q.get()` blockiert. Ergebnis nach 245 s: `SondeAusgefallen … Zeitlimit 240s überschritten`, für den ganzen Kandidaten. Jede Prüfung beobachtet die Vorgeneration neu; es träfe also jeden Kandidaten des Laufs (gelesen). Außerdem gelesen, nicht gemessen: Die Eingrenzung hat keine Frist je Kindprozess (`_im_kind` und `_vorlage_befehl` lesen bis EOF). Ihr Aufwand beträgt bis zu 2 + 6·(1 + 2·log₂ n) Lastläufe und fällt für jeden Kandidaten neu an. `os.fork` in einem Werk mit Threads kann im Kind verklemmen. | `kammerprobe05.out.txt:36` (d1); `KERN-COMMIT.patch.txt:512-534, 548-579, 605-617, 620-657, 1292-1299` | Lastläufe unter der Sonde mit eigener Frist fahren (z. B. `signal.alarm` im Kind) und eine Fristüberschreitung wie einen Abbruch eingrenzen. Ein Zeitbudget der Halbierung gegen das Kammerlimit rechnen; wird es überschritten, enthalten sich alle Funktionen der Last. d1 als rote Spezifikation. |
| 8 | mittel | **Die „Messung in T4-Größe“ belegt Entscheidung 4 nicht.** Das Prüfwerk hat 6 Module, 30 Funktionen und 126 Zeilen. Eine T4-Größe ist nirgends festgelegt; der Masterprompt setzt T4 nur „wegen Größe“ teurer an. **Mit Kappe 24:** Bedarf 35, davon 24 gelaufen und 11 ausgelassen; abgelehnt, 216 von 324 ungedeckt. **Ohne Kappe:** 35 gelaufen; abgelehnt, 168 von 324 ungedeckt. Der Enthaltungszweig von Entscheidung 4 tritt nicht ein, weil 168 Abweichungen auch ohne Kappe ungedeckt bleiben. Die Ursache ist Nr. 2: Zahl- und Listentests halten nicht fest. Die Kappe spart hier 11 Kammerläufe bzw. 12,6 s. | `proben/T4-GROESSE.txt:1-3`; `proben/t4_groesse.py:25, 59-65`; `bau/MASTERPROMPT-V8-TOR4.txt:21` | Nach der Behebung von Nr. 2 wiederholen: mit einem Kandidaten, dessen Tests festhalten, an einem Werk der erwarteten T4-Größe. Berichten, ob Enthaltung, Ablehnung oder Annahme eintritt und wie viele Proben ausgelassen werden. |
| 9 | mittel | **Tor-4-Skript: Der Zweig „eine verhaltensändernde Altlast braucht einen unabhängigen Test“ hat keinen Test.** Im Laufweg liegt nur A1: nicht verhaltensändernd, der Gegenzeuge prüft den Quelltext statisch. Kein Test setzt `verhaltensaendernd: True` oder ruft `tor4.normalvergleich` direkt auf. Gelesen: **(a)** `erlaubt` fasst die unabhängigen Tests **aller** Altlasten zusammen; ein Test von A2 deckt also auch Abweichungen für A1. **(b)** `gedeckt` führt Testkennungen als `datei::name` mit Dateinamen ohne Pfad (z. B. `test_werk_normieren_lf.py::test_normieren_lf`), der Gegenzeuge verlangt dagegen `tests/…`. Eine Liste mit `tests/test_x.py::name` träfe nie, und die Altlast bliebe „verändert“. **(c)** Das Skript berechnet 1 von 13 Tor-4-Zeilen; 12 stehen als „nicht berechnet“ da (Offen Nr. 2 des Berichts). | `KERN-COMMIT.patch.txt:1534-1536, 1580-1608`; `tests/drahtwerk.py` (A1, `verhaltensaendernd: False`); `bash /tmp/review-vor-t4-05/quellen2.sh` (Suche nach `verhaltensaendernd … True`, `normalvergleich(`: kein Treffer in `tests/`); `kammerprobe05.out.txt:1` (Kennungsform) | Je einen Unit- und Laufweg-Fall mit verhaltensändernder Altlast, mit und ohne unabhängigen Test. Die Form der Kennung normalisieren und `erlaubt` je Altlast bilden. |
| 10 | niedrig | **Aussagen, die stärker sind als ihr Beleg.** **(a)** §1: „‚0 Abweichungen, tragfähig‘ ist bei unvollständiger Erfassung also nicht mehr möglich“. Das gilt nur, wenn die Unvollständigkeit erkannt wird (Nr. 3). **(b)** §1 und Code: „Darstellung ungekürzt … nichts fällt still weg“. Ausnahmemeldungen sind weiter auf 200 Zeichen gekürzt, und geworfene Ausnahmen werden nur mit ihrem Typ geführt (Nr. 6). **(c)** §2 „Vorprobe: 5 von 5“ (Nr. 2). **(d)** §4 „Messung in T4-Größe“ (Nr. 8). **(e)** §8: „jedes Aegis-Urteil mit Laufzeitmessung trägt Stufe 2“. Belegt ist das an 3 von 16 Aegis-Urteilen des Verdrahtungslaufs; die übrigen 13 tragen weder Stufe noch Laufzeitwert, und die Zusicherung filtert `None`. **(f)** Entscheidung 3 ist nur am Organ belegt (`test_a3_*`, meine Fälle q1, a3x und d1), nicht durch `aegis.pruefen`. | `verhalten.py` (HEAD) Z. 178 (`[:200]`); `lokal_b.out.txt:14`; `KERN-COMMIT.patch.txt:1801-1803`; `VERDRAHTUNG-BELEG-REGRESSION.json` (`nachmessungen`, ausgewertet mit `quellen6.sh`) | Die Sätze mit Nenner und Nachweisart fassen. |
| 11 | niedrig | **Entscheidung 7 macht Lastaufrufe deutlich strenger, und dafür gibt es keine Gegenprobe.** Der Lastaufruf `normieren("  wort   wort  ")` trägt jetzt 4 Merkmale: `doppelleer`, `klein`, `rand_hinten` und `rand_vorn`. In x2 sind 16 von 36 ungedeckten Beobachtungen solche Lastaufrufe. Eine richtige Behebung braucht für jedes Merkmal jeder Lasteingabe einen festhaltenden Test; `klein` trägt jeder kleingeschriebene Text. Eine Gegenprobe mit einem Test, der einen Lastaufruf deckt, fehlt; §14 Nr. 5 nennt das selbst. An K2904, K3091 und K2868 ändert sich nichts: N1–N3 entscheiden wie in Runde 4. | `kammerprobe05.out.txt:13` (x2, `… \| rueckgabe/last`: 16); `KERN-COMMIT.patch.txt:457-461, 1001-1010` | Die Gegenprobe nachholen. Die Lasteingaben des T4-Werks bewusst wählen und ihre Merkmale je Last dokumentieren. |
| 12 | niedrig | **Die TypeScript-Wege der Entscheidungen 1–3 haben keine Kammerprobe.** Festhalten und Ausfall je Funktion sind in TypeScript nur gelesen bzw. vom Bericht als offen genannt (Offen Nr. 3). Die TS-Vollständigkeitsprüfung lief im Laufweg nur an der Gegenprobe K2904 (Vorprobe und N1–N3: je 4 von 4 beobachtet). Gelesen: Der TS-Weg kennt kein `last_ohne_sonde`; bei jedem Lastabbruch an der Vorgeneration enthalten sich alle Funktionen, die die Last rief. | `KERN-COMMIT.patch.txt:809-821, 918-923, 1014-1023, 1306-1320`; BERICHT §2, §3 | Vor T4 je eine TS-Kammerprobe für Entscheidung 2 (Werk-Ausnahme, x5-Analog) und für Entscheidung 3. |

## Antworten auf die Prüfpunkte

**a) Auftragspunkte, getrennt nach Modul, Organ und Laufweg**

Zeichen: ✓ = erfüllt, ✗ = nicht erfüllt.

1. **Vollständigkeitsprüfung**
   - Modul: lokal (`lokal_b`).
   - Organ: `test_v1_*` (10 Fälle, grün in der Regression). Dazu meine Kammerläufe p21, p22, p22k, p18c, p18ck und p14: 6 von 6 wie spezifiziert.
   - Laufweg: nur der Zweig „Enthaltung → zurückgestellt“, über `test_k4` und den unbeabsichtigten Fall in `TEILLAUF-1`.
   - Fälle ✓, Klasse ✗ (Nr. 3, 4, 6).
2. **Festhalten**
   - Modul: `test_f2_zusicherung_…` (6 Fälle).
   - Laufweg: `test_f2_idempotenz` (2 Fälle), dazu meine Fälle x3, x3k, x5 und x5b (4 Fälle, durch `aegis.pruefen`).
   - Fall x3 ✓, Klasse ✗ (Nr. 1, 2).
3. **Ausfall je Funktion**
   - Organ: `test_a3_*` (3 Fälle), dazu q1, a3x und d1.
   - Laufweg: kein Nachweis durch `aegis.pruefen`.
   - Die Fälle (Zählerlast, q1) sind ✓. Die Klasse ist nur teilweise geschlossen, ✗ für hängende Lasten (Nr. 7) und für geänderte Funktionen (Nr. 5).
   - Ersetzt werden nur echte Iteratoren ✓: `DictReader` bleibt ein Objekt (q1), `groupby` ist ausgenommen.
4. **Kappe**
   - Laufweg: `test_k4_*` (3 Fälle, durch `aegis.pruefen`) ✓.
   - Die T4-Messung liegt vor, sagt aber nichts über die Enthaltung (Nr. 8).
5. **Register und Tor-4-Skript**
   - Laufweg: 2 von 2 Verdrahtungsläufen (`TEILLAUF-3a`, Regression). Register 10 von 10; A1 doppelt behoben; Nachspiel = Aufzeichnung ✓.
   - Unit: `test_register_*` (2 Fälle).
   - Der verhaltensändernde Zweig ist ungetestet ✗ (Nr. 9).
6. **Vorspann und Stufe 2**
   - Unit: `test_s6_*` (4 Fälle) ✓.
   - Laufweg: Im Verdrahtungslauf läuft der Vorspann mit Stufe 2 (rc 0) ✓.
   - Die Bemessung stimmt ✓. In den Nachspielen war `eingang` in 0 von 6 Fällen gesperrt ✓ (Runde 4: 3 von 6).
7. **Formmerkmale der Lastaufrufe**
   - Laufweg: `test_l7` ✓.
   - Gegenprobe fehlt ✗ (Nr. 11).
8. **Dieselbe Stufe, eigene Tests, Nachspiel**
   - Dieselbe Stufe ✓: Unit durch `aegis.pruefen`; im Verdrahtungslauf tragen 3 von 16 Urteilen die Stufe.
   - Eigene Tests nach Kennung ✓: Laufweg `test_e8` (2 Fälle), Unit 5 Kennungen; für TypeScript nur die Unit.
   - Nachspiel in der Regression ✓, in 2 von 2 Läufen.

**b) Vollständigkeitsprüfung:** blind (Nr. 3) bzw. Fehlalarm (Nr. 4).
- **Massenhaftes Zurückstellen:** An 2 von 2 vorhandenen Python-Werken ist 0 von 66 Funktionen unvollständig. An einem Werk mit Datei-, Strom- oder Iterator-Objekten stellt aber jeder Kandidat eines betroffenen Moduls zurück.

**c) Festhalten:**
- Ja, es kann weiter ohne Unterscheidung festgehalten werden (Nr. 1, gemessen).
- Umgekehrt hält der häufigste Test nichts fest (Nr. 2).
- `pytest.raises` um Werkcode habe ich nicht gemessen.
- Python und TypeScript folgen demselben Mechanismus (gelesen).

**d) Ausfall je Funktion**
- **Zustandslecks:** Der Elternprozess beobachtet die Vorgeneration danach frisch, mit denselben durchlässigen Funktionen auf beiden Seiten (gelesen).
- **Kindprozesse:** `os._exit(0)`; die Vorlage endet bei EOF (gelesen).
- **Nicht eingrenzbar:** Dann enthalten sich alle Funktionen der Last (gelesen).
- **Zeitlimit:** Einen Hänger fängt die Eingrenzung nicht (Nr. 7).
- **Geänderte Funktion:** Nr. 5.
- **TypeScript:** nur die Liste der gerufenen Funktionen, ohne Prüfung „ohne Sonde“ (Nr. 12).

**e) Proben des Gutachtens 04 gegen `0c2f058`**

24 von 24 neu gefahren. Die Werte an `43b8fad` stammen aus Review 04.

| Fall | an `43b8fad` | an `0c2f058` |
|---|---|---|
| x1 / x1k | abgelehnt, 0 von 14 gedeckt / abgelehnt | abgelehnt, 0 von 14 gedeckt / abgelehnt |
| x2 / x2k | abgelehnt, 0 von 6 / abgelehnt | abgelehnt, 0 von 6, `festhaltend` für `tab` leer / abgelehnt |
| **x3** / x3k | **überlebt**, 6 von 6 gedeckt / abgelehnt | **abgelehnt**, 0 von 6 gedeckt / abgelehnt |
| **q1** / q1k | **SondeAusgefallen** / 6 Abweichungen | **geurteilt, 6 Abweichungen**, `lies` unvollständig / 6 Abweichungen, `lies` unvollständig |
| p13, p16, p16b, p17, p23 | 16, 4, 4, 1, 14 | 16, 4, 4, 1, 14 |
| **p14** | tragfähig, gekappt (14) | **14 Abweichungen**, `zaehle` unvollständig (Kappe 1000) |
| p18 / p18b / p18ck | 6 / 6 / 40 | 6 / 6 / 40 (`leser` jeweils unvollständig) |
| **p18c** | **0, tragfähig** | **Enthaltung „unvollständig erfasst“** |
| p19 / p19b / p20 / p22k | je 28 | je 28 |
| **p21** / **p22** | **0, tragfähig** | **28** / **28** |

- Die Fälle sind geschlossen, und es gibt keine neue stille Stelle unter den 24.
- Die neuen stillen Stellen und Fehlalarme stammen aus meinen 12 neuen Fällen: Nr. 1, 3–7.

**f) Zahlen:** siehe „Geprüft und bestätigt“.

**g) Geänderte ältere Tests:** In 2 von 2 Dateien (`tests/drahtwerk.py`, `tests/test_verdrahtung.py`) handelt es sich um Spezifikationsänderungen. Beide Änderungen fügen nur hinzu; eine gelockerte Zusicherung habe ich nicht gefunden.
- `test_vor_t4_04.py` ist unverändert.
- `test_r413` bleibt aus dem genannten Grund grün: Mein p14-Lauf zählt `iterator_gekappt` weiter (14).
- Die Änderung an `test_v1_iterator_kappe` (neue Datei, vor dem Commit) passt zu meinem p14-Lauf. Mit der Kappe 1000 ist eine Änderung ab Element 60 sichtbar.

**h) Aussagen und Lücken**
- Aussagen, die über ihren Beleg hinausgehen: Nr. 2, 8, 10.
- Lücken gegenüber dem Auftrag: Nr. 9 (verhaltensändernder Zweig), Nr. 11 (Gegenprobe Lastaufruf), Nr. 12 (TypeScript). Das Register nennt von den Tor-4-Zeilen nur „Schwächen“, weil die übrigen 12 nicht gebaut sind.
- Für T4 gefährlich: Nr. 1, 2, 3, 5 und 7, dazu Nr. 4 je nach Werk.

## Geprüft und bestätigt

- **Commits:** `git log` zeigt `0c2f058` → `43b8fad` → `1d9a5aa`. `COMMIT-STAT` nennt 17 Dateien mit 1279 Einfügungen und 120 Löschungen. Der Arbeitsbaum war vor und nach meinen Läufen leer.
- **Stufe-2-Eichung** (`STUFE2-EICHUNG.txt`): 9 von 9 Tabellenwerten bestätigt:
  - W60: 3 von 8 gesperrt (K2904 r1, K3091 r0, K3091 r3), 1,884, 11,6 s;
  - W240: 0 von 8, 1,155, 12,3 s;
  - W480: 0 von 8, 1,208, 13,7 s.
  - „Übrige Bereiche 0 von 24“ bestätigt: In 24 von 24 Zeilen steht in `gesperrt` nur `eingang` oder nichts.
  - „t3.db unverändert: True“.
  - Der Commit trägt W 240, belegt durch `test_s6_stufe2_eingang_bemessen` (grün).
- **Teilläufe (§9):** 5 von 5 Zeilen bestätigt:
  - `TEILLAUF-1`: 25 bestanden, 2 rot, 124 s. Beide rot mit „zahlen … nach 50 Elementen gekappt“, wie §14 Nr. 3 sagt.
  - `TEILLAUF-2`: 591 bestanden, 2 übersprungen, 1 rot, 93 abgewählt, 724,99 s.
  - `TEILLAUF-3a`: 6 von 6, 1719,08 s.
  - `TEILLAUF-3b`: 132 von 132, 236,82 s.
  - Vorprobe K2904: überlebt.
- **Regression an `0c2f058`:**
  - 598 bestanden, 2 übersprungen, 0 fehlgeschlagen, 93 abgewählt, 2457,93 s.
  - JUnit: 600 Fälle, 0 failure, 0 error, 2 skipped.
  - `test_vor_t4_05` 27 von 27, `test_verdrahtung` 6 von 6.
  - Zuwachs gegenüber `43b8fad` (569 bestanden): 29 = 27 neue Fälle + 2 Registertests.
- **Verdrahtung, 2 von 2 Belegen** (`TEILLAUF3`, `REGRESSION`):
  - 23 von 23 Organen gerufen.
  - Register 10 von 10, `fehlend` leer. Die Kanten stehen mit Aufrufer und Phase in `kanten`, zum Beispiel `gegenzeugen.torzeile_schwaechen ← biotop.tor4:ausfuehren @ tor4`.
  - Tor-4-Zeile „1 von 1 behoben … erfüllt“; für A1 sind `schwaeche_weg` und `normal_unveraendert` wahr.
  - Nachspiel K1: `ueberlebt`, gleich der Aufzeichnung, Stufe 2, 15 Kammerläufe, 0 echte Modellaufrufe.
  - `modellkosten_eur` 0,0; 10 von 10 Schritten mit rc 0.
  - Stufe in den Aegis-Urteilen: 3 von 16 tragen Stufe 2, 13 tragen keine.
- **Nachspiele N1–N3:**
  - 7 von 7 Fällen wie erwartet: K2904 überlebt in 3 von 3 Durchgängen, K3091 in 3 von 3, K2868 wird abgelehnt (1 von 1).
  - Stufe 2 in 7 von 7. `eingang` gesperrt in 0 von 6 Stufe-2-Fällen.
  - `planung`-Quoten, aus `NACHSPIEL-N*.txt` gerechnet: N1 0,407 / 0,376, N2 0,384 / 0,403, N3 0,415 / 0,420 (K2904 / K3091). Die N3-Zeilen der Berichtstabelle habe ich nicht gesehen.
  - K2868 wie in Runde 4: 40 Abweichungen, davon 24 ungedeckt (6 Gruppen × 4) und 16 gedeckt; 3 deckende Tests, 2 Verfälschungsläufe, 0 ausgelassen; 9 von 10 beobachtet.
  - T3-DB-Prüfsumme vorher = nachher in 8 von 8 Belegen (n1–n3 und die Vorprobe); 0 echte Modellaufrufe in 8 von 8.
  - Start laut `JOB-KETTE.txt` in 3 von 3 Durchgängen an `HEAD=0c2f058`, mit 0 fremden Containern.
- **Vorher/Nachher:**
  - 9 von 27 grün an `43b8fad`, 27 von 27 an `0c2f058`.
  - Von den 18 roten Fällen scheitern 3 an einer fehlenden Schnittstelle (`AttributeError`: `ist_eigener_test` 2-mal, `_zusicherung_faellt` 1-mal), 15 am Verhalten. Nachgezählt.
- **T4-Größe:** Alle Zahlen der gefüllten §4 stimmen mit `T4-GROESSE.txt` überein:
  - Werk: 6 Module, 30 Funktionen, 126 Zeilen, 8 Funktionen geändert.
  - Mit Kappe: Bedarf 35, 24 gelaufen, 11 ausgelassen, 30 Kammerläufe, 30,3 s.
  - Ohne Kappe: 35 gelaufen, 0 ausgelassen, 41 Kammerläufe, 42,9 s.
  - Beide abgelehnt.
- **Kasse:** Der Verdrahtungslauf kostete 0,0 €; in den Nachspielen gab es 0 Modellaufrufe. Meine eigenen Proben liefen mit gestellter Anbietergrenze (`aegis.aufrufen` in `test_vor_t4_03._pruefen`) in der netzlosen Kammer.

## Nicht geprüft

- **Die gefüllte Berichtsfassung von 21:50 Uhr**, außer den oben genannten Stellen. Nicht gelesen habe ich `spez/*` (R6-…), `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`, `AUSWERTUNG.json`, `JOB-NACH-KETTE.txt` und `veroeffentlichen.py`.
- **Code-Stand und sauberer Arbeitsbaum in den Nachspielbelegen:** Mein Skript las die falschen Schlüssel; die Belege heißen `code_stand_beim_import` und `code_stand_nach_fall`. Belegt ist nur der Start je Durchgang laut `JOB-KETTE.txt`.
- **TypeScript in der Kammer** (Entscheidungen 1–3 und 7): nur lokal am Kanon bzw. gelesen.
- **Nr. 2 in der Kammer** (pytest 8.3.3): nur lokal mit pytest 9.1.1 gemessen.
- **`pytest.raises` um Werkcode** unter Verfälschung.
- **Aufwand der Eingrenzung** in T4-Größe und `os.fork` bei laufenden Threads: nur gelesen.
- **TS-Eichproben** (`eichproben_ts.py`) an Stufe 2.
- **Gefüllte `KASSE.md`**; von `UEBERGABE.md` nur das Ende.
- **Möglicher Parallellauf:** Ob sich meine Kammerläufe (21:41–21:48 Uhr) mit `job_nach_kette.sh` des Auftragnehmers überschnitten, habe ich nicht geprüft. Dessen Dateien `spez/SPEZ-R6-*.txt` sind jünger als 20:40 Uhr. Meine Proben messen keine Zeiten.
- **Masterprompt v8:** nur der Tor-4-Auszug.
- **Lauf-DB:** nicht geöffnet.

## Sperren

Keine.

Hinweis: Ein eigenes Warteskript (`warte.sh`, erste Fassung) überschritt das Zeitlimit des Werkzeugaufrufs von 420 s. Das ist keine Sperre der Ausführungsschicht. Danach habe ich mit kürzerer Schleife gewartet.

## Schreibort-Nachweis

**Unter `/root/`:** nur `/root/biotop-vor-t4-05/REVIEW.md` (diese Datei).

**Unter `/tmp/review-vor-t4-05/`** (dort war auch `TMPDIR`):
- **Lesende Skripte:** `status.sh`, `quellen1.sh` bis `quellen6.sh`, `belege1.sh` bis `belege3.sh`, `umgebung.sh`, `bericht_neu.sh`, `warte.sh`, `warte2.sh`, `abschluss.sh`, `verdrahtung_lesen.py`, `n_auswerten.py` mit `n_auswerten.out.txt`.
- **Kopien aus `git show HEAD`:** `verhalten_head.py`, `kanon_head.mjs`.
- **Lokale Proben ohne Kammer:** `lokal_b.py` mit `lokal_b.out.txt`, `lokal_ts.mjs` mit `lokal_ts.out.txt`, `e2b_probe.py` mit `e2b_probe.out.txt`.
- **`e2b/`:** `conftest.py`, `tests/test_formen.py` und gegebenenfalls ein `__pycache__` von pytest.
- **Kammerprobe:** `kammerprobe05.py`, `kammerprobe05.out.txt`, `KAMMERPROBE05.json`, dazu `werke/` mit 78 Dateien in 26 Fällen.
- **`tmp/`:** am Ende leer.

**Nicht von mir:**
- Alle übrigen Dateien in `/root/biotop-vor-t4-05/`, unter anderem `spez/`, `AUSWERTUNG.json`, die gefüllte `BERICHT.md` und `nachspiel/n1`–`n3`.
- `/tmp/r5-*` der Kette.

**Sonst:**
- `git status` von `/root/biotop` war vorher und nachher leer.
- `/root/uebungswerk` und `/root/uebungswerk2` enthalten keine neueren Dateien; die Kammer las Kopien.
- Am Ende liefen 0 Container.
