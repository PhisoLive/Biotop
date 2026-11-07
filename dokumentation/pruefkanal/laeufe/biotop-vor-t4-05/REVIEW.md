# Review Behebungsrunde 5 vor T4: ein Durchgang

Stand: 2026-09-24, gegen 22:20 Uhr. Das ist ein unabhängiger Reviewdurchgang nach `REVIEW-AUFTRAG.md`.

**Schreibort, bitte zuerst lesen.** Diese Datei liegt unter `/tmp/review-vor-t4-05/REVIEW.md`, nicht unter
`/root/biotop-vor-t4-05/REVIEW.md`. Dort lag bei meinem Abschluss schon ein vollständiger Durchgang eines zweiten, parallel
gestarteten Prüfers: 22:03:48 Uhr, 229 Zeilen, Kopf „Stand gegen 22:00 Uhr“. Laut Hinweis des Schreibwerkzeugs ist das der
Geschwister-Subagent `sa-0-816c6469`.
- Ich habe seine Datei nicht überschrieben und nicht gelesen, nur Kopf und Gliederung, um den Urheber festzustellen.
- Zwei Durchgänge widersprechen der Regel „ein Review“. Welcher gilt, entscheidet der Auftraggeber.
- Beide Prüfer arbeiteten im selben Ordner `/tmp/review-vor-t4-05/` (siehe Schreibort-Nachweis, eigener Fehler).

**Gegenstand**
- **`BERICHT.md`:** Geprüft ist die Fassung mit Platzhaltern, gelesen um 20:35 Uhr. Die um 21:50 Uhr gefüllte Fassung
  (offen nur noch `‹REVIEW›` und `‹SPERREN›`) habe ich um 22:10 Uhr gelesen. Ihre Zahlen in §4, §6, §9 und „Ergebnis“
  habe ich gegen die Quellen gehalten.
- **Kern-Commit** `0c2f058` auf `43b8fad` (HEAD, Arbeitsbaum leer). `KERN-COMMIT.patch.txt` habe ich ganz gelesen
  (2173 Zeilen).
- **Belege** unter `/root/biotop-vor-t4-05/`, Vorrunde `/root/biotop-vor-t4-04/`.

**Wie geprüft**
- Kein Modellaufruf, kein Netz, kein Geld. Keine volle Regression, kein Verdrahtungstest.
- Solange `job_kette` lief (Ende 21:40:41 Uhr laut `JOB-KETTE.txt`), habe ich nur gelesen und ohne Kammer gerechnet:
  - `kan()` des Commits (`git show HEAD:…`) an 30 Python-Werten;
  - den TS-Kanon an 17 Werten mit dem lokalen Node 26.8.2.
- **Kammerläufe:** ein Skript, `kammerprobe05.py` (Vorlage `review-proben/kammerprobe.py`).
  - Lauf von 21:41:03 bis 21:48:02 Uhr in der echten Kammer `biotop-kammer:1` gegen HEAD `0c2f058`.
  - 36 Fälle: die 24 Fälle des Gutachtens 04 unverändert und 12 neue.
  - Das Skript prüft beim Start selbst `pgrep -f job_kette`.
  - `git status` war vorher und nachher leer, danach liefen 0 Container.
- Die Lauf-DB habe ich nicht geöffnet.

**Kurzurteil**
- **Die Fälle des Reviews 04 sind geschlossen.** 24 von 24 Proben des Gutachtens 04 verhalten sich an `0c2f058` wie
  spezifiziert:
  - x3 wird abgelehnt, `festhaltend` für `tab` ist leer;
  - p21 und p22 zeigen je 28 Abweichungen;
  - p18c und q1 haben keine stille Stelle mehr.
- **Die Zahlen des Berichts stimmen**, wo ich sie nachgerechnet habe. Eine Ausnahme ist ein gemischter Nenner (Nr. 9).
- **Das Urteil „nicht abgenommen“ teile ich.** Die eigenen Befunde R6-1 und R6-4 passen zu meinen Messungen.
- **Die Klassen sind nicht geschlossen.** Zu R6-1 und R6-4 kommen drei hohe Befunde, alle in der Kammer gemessen:
  - **Nr. 1:** Eine Typprüfung oder Tautologie im Test „hält `tab` fest“. Der Tab-Rückschritt überlebt **durch
    `aegis.pruefen`**.
  - **Nr. 2:** Die Vollständigkeitsprüfung ist selbst blind für Zustand in C-Typen. `StringIO` als Argument und eine
    `Decimal`-Unterklasse als Rückgabe ergeben wieder „0 Abweichungen, tragfähig“.
  - **Nr. 3:** Enthält sich die Funktion, die der Kandidat ändert, gilt das Urteil als tragfähig. Das betrifft den
    Sondenausfall heute und R6-1 in der Form, in der der Bericht sie vorsieht.
- **Mittel:** Ausnahmen nur nach Typ verglichen (Nr. 4); eine hängende Last legt alles still (Nr. 5); Fehlalarm-Auslöser
  breiter als das Beispiel von R6-1 (Nr. 6); Umfang des Registers (Nr. 7); der Zweig „verhaltensändernde Altlast“ im
  Tor-4-Skript (Nr. 8).
- **Niedrig:** Nr. 9–11.

## Befunde

| Nr | Schwere | Befund | Beleg (Datei:Zeile, Befehl, Messung) | Vorschlag |
|---|---|---|---|---|
| 1 | hoch | **Ein Test hält ein Merkmal weiterhin fest, ohne es zu unterscheiden. Gemessen durch `aegis.pruefen`.** Entscheidung 2 ist wörtlich gebaut: Nur eine fallende Zusicherung in der Testdatei hält fest. Die Klasse aus Review 04 Nr. 1 ist damit aber nicht geschlossen. Das Verfälschungsobjekt ist „gleich nichts, auch sich selbst nicht“ und kein `str`, darum fällt jede Zusicherung, die den Wert überhaupt berührt. **Probe x5:** Kandidat K2 gibt Text mit Tab unverändert zurück. Der Werkstest trägt `assert isinstance(normieren("a\tb c"), str)` neben `assert normieren("a b") == "a_b"`. Ergebnis: **überlebt**, „Kernmaß −12 → −2 (+10)“, 52 Abweichungen, 0 ungedeckt, 6 von 6 Rückschritt-Beobachtungen gedeckt; `festhaltend …\|rueckgabe\|tab` = `[test_normieren_x]`. **Probe x5b:** dieselbe Lage mit der Tautologie `assert normieren("a\tb c") == normieren("a\tb c")`, ebenfalls überlebt. **Kontrolle x3k** (ohne die Zeile): abgelehnt, 6 ungedeckt. Beide Zeilen gelten an Vorgeneration und Rückschritt gleichermaßen. **Gefolgert** aus `VORPROBE-E2b`: x5 und x5b halten nur fest, weil ihre pytest-Meldung ein Zitat `'a\tb c'` enthält und das Präfix „AssertionError:“ deshalb stehen bleibt. Nach der Behebung von R6-4 hielte auch `assert isinstance(f(1), int)` fest; R6-4 allein erweitert die Lücke also. **TypeScript** (gelesen): `expect(typeof f(x)).toBe('string')` und `expect(f(x)).toBe(f(x))` fallen am Verfälschungsobjekt ebenso, `toEqual` dagegen nicht. | `kammerprobe05.out.txt:1-2` (x5, x5b), `:15` (x3k); `KAMMERPROBE05.json`; Code: `KERN-COMMIT.patch.txt:491-501` (`_zusicherung_faellt`), `biotop/kern/py/verhalten.py:222` (`Verfaelscht`), `biotop/kern/ts/deck-setup.mjs:9`; `proben/VORPROBE-E2b.txt` | „Hält fest“ neu fassen: Der Test fällt, wenn an den Aufrufen mit dem Merkmal der Wert der **Vorgeneration** statt des Kandidatenwerts eingesetzt wird, also Rückspiel statt eines Werts, der nichts gleicht. Dann bestehen Typprüfung und Tautologie und halten nichts fest. Mindestens die zweite Hälfte des Vorschlags aus Review 04 Nr. 1 umsetzen: Dieselbe Zusicherungszeile muss auch an der Vorgeneration fallen. Zusammen mit R6-4 bauen. Rote Spezifikationen x5 und x5b. Gegenprobe: Ein Test, der das neue Tab-Verhalten ausdrücklich zusichert, deckt weiterhin. |
| 2 | hoch | **Die Vollständigkeitsprüfung ist selbst blind für Zustand in C-Typen; es kommt wieder „0 Abweichungen, tragfähig“ heraus.** `_pruefen_vollstaendig` vergleicht mit `object.__getstate__`. Das liefert für ein Objekt mit leerem `__dict__` `None`, und der C-Zustand (Puffer, Wert, Elemente) gehört nie dazu. Objekte mit `__dict__` fängt `kan()` im Instanz-Zweig ab (`felder: {}`), bevor die Regel „nur Standarddarstellung mit Adresse → unvollständig“ greifen kann. **Kammer:** p24b: Eine Funktion schreibt in einen übergebenen `io.StringIO`, der Kandidat schreibt anderen Text. Ergebnis: 0 Abweichungen, tragfähig, „1 von 1 beobachtet“. p25: `netto(5)` gibt eine `Decimal`-Unterklasse zurück, 10 statt 15. Ergebnis: 0 Abweichungen, tragfähig. **Lokal:** Paare mit verschiedenem Zustand, gleicher Form und ohne Meldung; blind sind 11 Arten. 8 davon tragen C-Zustand: Unterklassen von `Decimal`, `date`, `deque`, `StringIO`, `array`, dazu `memoryview`, `weakref` (Ziel) und `defaultdict` (Fabrik). 3 fallen unter die im Bericht genannte Grenze „Closures, Klassenattribute“: Deskriptor mit Zustand außerhalb der Instanz, Property über einer Closure, `functools.partial`. Kontrollen: 4 von 4 gesehen. Von den 6 Python-Arten des Prüfauftrags sind 4 blind (Deskriptoren, Closure-Properties, C-Typen, WeakRefs); gesehen werden eigenes `__getstate__` und `__slots__` mit `__dict__`. **Der Bericht sagt mehr, als belegt ist:** §13 Nr. 2 nennt `object.__getstate__` „Pythons eigenen Kopierzustand“; `copy` liest aber `__reduce_ex__(4)`, und das trägt diesen Zustand. §1 nennt als Grenze „C-Erweiterungen mit eigener Darstellung ohne Adresse“. Gerade die sind nicht blind (lokal wird `Decimal('1.5')` gesehen); blind ist C-Zustand hinter einem `__dict__`. | `kammerprobe05.out.txt:4-5` (p24b, p25); `lokal_b.py`, `lokal_b.out.txt:2-12` (blind), `:15-18` (Kontrollen); Code: `KERN-COMMIT.patch.txt:98-126` (`_zustand_unabhaengig`, `_pruefen_vollstaendig`), `:213-231` (Instanz-Zweig vor der Adress-Regel) | Als unabhängige Aufzählung das Kopierprotokoll nehmen: `__reduce_ex__(4)` (Argumente, Zustand, Elemente) kanonisch vergleichen. Trägt es etwas, das `kan()` nicht darstellt, oder wirft es (`memoryview`, `weakref`), ist das „unvollständig“. Rote Spezifikationen p24b und p25. Kontrollen: `Decimal` und eine Klasse mit `__slots__` und `__dict__` bleiben gesehen. |
| 3 | hoch | **Enthält sich die geänderte Funktion, gilt das Urteil als bestanden.** Probe a3x: Der Kandidat ändert genau `naechste`, die Funktion mit Sondenausfall (Zählerlast wie in `test_a3`). Ergebnis: geurteilt, tragfähig, „keine Verhaltensabweichung (1 von 2 Funktionen beobachtet)“; `naechste` enthält sich. Durch `aegis.pruefen` gelesen: Es gibt kein `enthaltung`, das Urteil ist tragfähig, also `ueberlebt` (bei Kernmaßgewinn), und der Neutralzähler bucht „geurteilt“. Das widerspricht Masterprompt v8, Tor 4: „Enthaltungen zählen nicht als bestanden“. Außerdem verfälscht es die Quote „geurteilt“, an der Torzeilen hängen. Der TS-Weg ist gleich gebaut: Alle Funktionen der abbrechenden Last enthalten sich (gelesen). **Folge für R6-1:** Der Bericht sieht vor: „Enthalten muss sich nur die betroffene Beobachtung; der übrige Vergleich urteilt“ (§1). So gebaut, überträgt sich diese Lücke auf jede unvollständig erfasste Funktion. p24 (geänderte `StringIO`-Rückgabe) enthält sich heute richtig; danach ginge er als „unbeobachtet, tragfähig“ durch. | `kammerprobe05.out.txt:7` (a3x), `:3` (p24); Code: `KERN-COMMIT.patch.txt:1331-1336, 1384-1392` (Enthaltung je Funktion), `:1213-1221` (`aegis`: Neutralzähler, Enthaltung), `:1425-1427` (`unbeobachtet` → tragfähig); `bau/MASTERPROMPT-V8-TOR4.txt:10, 13` | Eine Regel für Sondenausfall und R6-1 zugleich: Enthält sich eine Funktion, die der Kandidat ändert (Diff oder Wirkungskreis), enthält sich das Urteil: zurückstellen, gezählt. Enthält sich nur unveränderter Code, urteilt der Rest. Rote Spezifikationen a3x und p24 (zu R6-1). Gegenproben: `test_a3_sondenausfall…` sowie f1 und f2 (Nr. 6). |
| 4 | mittel | **Ausnahmen werden nur nach ihrem Typ verglichen.** Eine geworfene Ausnahme ergibt die Beobachtung `Fehler:ValueError`. Meldung und Attribute fehlen, und auf diesem Weg gibt es keine Vollständigkeitsprüfung. **Kammer p26:** `pruefe(-1)` wirft `ValueError('PLZ ungültig')` bzw. `ValueError('Ort ungültig')`. Ergebnis: 0 Abweichungen, tragfähig. Eine zurückgegebene Ausnahme führt `kan()` im Ausnahme-Zweig, noch vor jeder Prüfung: Die Meldung wird auf 200 Zeichen gekürzt, Attribute werden nicht erfasst. Lokal ergeben ein verschiedenes `e.feld` und Meldungen, die sich erst nach Zeichen 200 unterscheiden, jeweils dieselbe Form. §1 sagt „die Darstellung ungekürzt“, und der Code-Kommentar sagt „nichts fällt still weg“. Das gilt für `repr` und Bytes, nicht für Ausnahmen. | `kammerprobe05.out.txt:6`; `lokal_b.out.txt:13-14, 19`; `biotop/kern/py/verhalten.py:178` (`meldung…[:200]`), `:454` (`wert`: nur `'Fehler:' + Typ`) | Geworfene und zurückgegebene Ausnahmen über `kan()` führen, mit Argumenten und `__dict__` und ohne Kürzung (`knapp()` kürzt mit Prüfsumme). Adressen wie bisher tilgen. Rote Spezifikation p26. Gegenprobe: gleiche Meldung → tragfähig. |
| 5 | mittel | **Eine Last, die unter der Sonde hängt statt abzubrechen, legt den ganzen Kandidaten still.** Probe d1: Die Last nimmt ein Element aus einer `queue.Queue`. Die Sonde ruft `hole` mehrfach auf, und der zweite Aufruf blockiert. Ergebnis: Kammer-Zeitlimit 240 s, „`SondeAusgefallen` … (infrastruktur): Zeitlimit“, 245 s. Das ist ein Messgerätausfall für jeden Kandidaten, der das Modul berührt. Entscheidung 3 ist nur für Abbrüche gebaut: Die Eingrenzung beginnt erst nach einem Abbruch. Weder `_im_kind` noch `_vorlage_befehl` haben eine Frist (`os.read` und `os.waitpid` warten unbegrenzt, gelesen). Ein hängender Versuch in der Halbierung liefe ebenso ins Zeitlimit. Die Zahl der Versuche ist nur gerechnet: 2 + bis zu 6 · (1 + 2·log₂ n) Lastläufe. | `kammerprobe05.out.txt:36` (d1); Code: `KERN-COMMIT.patch.txt:512-534` (`_im_kind`), `:548-579` (Halbierung), `:605-617` (`_vorlage_befehl`) | Jede Bereichslast und jeden Versuch mit einer Frist fahren (`signal.alarm` im Kind). Läuft die Frist ab, zählt das als Abbruch und wird eingegrenzt wie ein Abbruch. Eine Gesamtfrist für die Eingrenzung; wird sie überschritten, enthalten sich die Lastfunktionen, gezählt. Rote Spezifikation d1. |
| 6 | mittel | **Fehlalarme der Vollständigkeitsprüfung: mehr Auslöser als im Beispiel von R6-1, auf den Übungswerken aber keiner.** Solange sich das ganze Urteil enthält (R6-1 offen), stellt ein unverändertes, schwer erfassbares Objekt jeden Kandidaten des Moduls zurück. Gemessen jeweils mit einem gleichwertigen Kandidaten (`2 * x` → `x + x`): **f1:** Ein Objekt hält `iter(text.split())` in einem Attribut (Zerleger-Muster). Ergebnis: Enthaltung für 3 unveränderte Funktionen, darunter jede Methode des Objekts (über `self` in `>args`). **f2:** Eine unveränderte Funktion liefert einen Generator mit 1.500 Elementen. Ergebnis: Enthaltung („gekappt“). Lokal zusätzlich: eine Verkettung tiefer als 12 Ebenen (14 Knoten) und ein `map`- oder Generator-Objekt in einem Behälter. **Nenner:** An den beiden Python-Übungswerken ist an der Vorgeneration keine Funktion unvollständig erfasst: `lagerhaus` 0 von 42, `logmuehle` 0 von 24 Funktionen mit Inhalt, alle 5 Korpusläufe `ok`. Für T4 (6.000–10.000 Zeilen) ist die Rate nicht gemessen. | `kammerprobe05.out.txt:8-9` (f1, f2), `:10-11` (w1 `lagerhaus`, w2 `logmuehle`); `lokal_b.out.txt:20-25` | f1 und f2 als Gegenproben zu R6-1 aufnehmen (unverändert → geurteilt). Vor dem T4-Lauf die Sonde einmal an der Vorgeneration des T4-Werks fahren und die unvollständig erfassten Funktionen je Modul zählen (derselbe Aufruf wie bei w1 und w2). |
| 7 | mittel | **Das Register enthält 10 Funktionen, nicht „jede Funktion, deren Aufruf der Entwurf verlangt“.** Eingetragen sind 4 Kanten des Annahmepfads, 4 des Vorspanns und 2 des Tor-4-Skripts. Es fehlen Aufrufe, die Masterprompt v8 verlangt: die Verhandlung (Vorbedingung 4), der Neutralzähler, die Immunisierung, die Doppelungs-Behauptung aller Angriffstests und Generation 0 (Tor-4-Zeilen, Vorbedingungen 6 und 9). Sie hängen nur an der Modulprüfung „Organ irgendwo gerufen“, also an genau der Prüfung, die Lauf 38 nicht fing. Im Verdrahtungsbeleg ruft kein Rahmen `lauf._verhandeln` die Funktion `aegis.pruefen`. Die 3 `aegis.pruefen`-Kanten unter 497 kommen aus `_generation_koerper`, `nachspiel.spielen` und `eichproben._einzelprobe`. | `KERN-COMMIT.patch.txt:769-790` (`VERLANGT`); `bau/MASTERPROMPT-V8-TOR4.txt:6, 10-13, 34, 36, 39`; `VERDRAHTUNG-BELEG-REGRESSION.json` (`kanten`, gelesen mit `verdrahtung_lesen.py`) | Das Register aus den Tor-4-Zeilen und den Vorbedingungen ableiten, je eine Kante mit Aufrufer und Phase. Mit R6-2 (jede berechenbare Tor-4-Zeile) jede Zeilenfunktion eintragen. Der Verdrahtungstest sollte eine Verhandlung auslösen. |
| 8 | mittel | **Der Zweig „verhaltensändernde Altlast mit unabhängigem Test“ ist ungetestet und praktisch nicht erreichbar (gelesen).** `normalvergleich` führt den unabhängigen Test nie aus. Es zählt nur Einträge in `gedeckt`, deren deckende Tests in der Liste stehen. Dabei passen die Kennungen nicht zusammen: In `gedeckt` stehen Kennungen der Form `test_x.py::test_y` (gemessen in x5: `test_werk_normieren_x.py::test_normieren_x`). Die Liste verlangt `datei::name`, der Gegenzeuge verlangt Pfade unter `tests/`; ein Eintrag `tests/test_x.py::test_y` träfe also nie. Außerdem deckt der Test nur, wenn er während des Laufs im Werk lag und an der Vorgeneration fiel. `erlaubt` gilt über alle Altlasten, nicht je Altlast. Kein Test trägt `verhaltensaendernd: true`; das Drahtwerk prüft nur den Zweig ohne Verhaltensänderung (A1). Für T4 hängt die Torzeile „Schwächen“ an diesem Zweig, sobald eine Altlast Verhalten ändern soll. | `KERN-COMMIT.patch.txt:1580-1608` (`normalvergleich`), `:1543-1557` (`liste_lesen`), `:1663-1670` (A1); `grep -rn` in `tests/`: kein `verhaltensaendernd: True` (`quellen2.sh`) | Den unabhängigen Test am Endstand ausführen (muss bestehen) und am Ausgangsstand (muss fallen). Kennungen vereinheitlichen, `erlaubt` je Altlast bilden. Dazu ein Unit- oder Drahtwerk-Fall: verhaltensändernde Altlast mit Test → behoben; ohne Test → nicht beurteilbar. |
| 9 | niedrig | **§6 mischt bei den Vergleichswerten die Nenner.** Beispiel: „`zahlen` 18,9 ms (Spannweite 0,05 … 0,39, 0 Sperren in 24 Messungen)“. Median und Spannweite stammen aus n = 40 Werten, also aus 8 Rauschmessungen (`STUFE2-EINGANG-DAUER.txt`); die Sperren aus 24. Über alle 24 Messungen der Eichung gerechnet: `zahlen` Median 19,0 ms, relative Spannweite 0,04 … 0,70; `tarife` 0,04 … 1,42; `bericht` 0,02 … 0,20; `planung` Median 347,0 ms. Die Folgerung „die Dauer allein erklärt die Sperren nicht“ bleibt richtig: 0 Sperren in 24. | `letzte.out.txt:6-9` (aus `proben/STUFE2-EICHUNG.jsonl`, 24 Zeilen); `proben/STUFE2-EINGANG-DAUER.txt` | Je Zahl den Nenner nennen oder alle 24 Messungen nehmen. |
| 10 | niedrig | **TS-Kanon: blinde Stellen und Fehlalarme** (lokal mit Node 26.8.2, nicht mit der Node-Fassung der Kammer). **Blind:** Zustand in einer Closure, privater Zustand über `WeakMap` sowie zusätzliche eigene Felder an Unterklassen von `Map`, `Array`, `Date` und `Error`. Diese Zweige rufen `vollstaendig()` nicht auf, während Python Unterklassen mit eigenen Attributen prüft. Private Felder (`#s`) werden erkannt. **Fehlalarm** (Enthaltung für gewöhnliche Werte): `URLSearchParams`, `Headers`, `AbortController` und `TextEncoder`, weil die Quelltext-Regel `#`-Felder in Nodes eigenen Klassen findet; außerdem `Intl.NumberFormat` und Objekte mit Symbol-Schlüssel. §1 nennt nur Closures und die Erkennung privater Felder am Quelltext. | `lokal_ts.mjs`, `lokal_ts.out.txt:1-17`; `KERN-COMMIT.patch.txt:848-893` | Vor T5: `vollstaendig()` auch in den Zweigen `Map`, `Set`, `Array`, `Date` und `Error` aufrufen. Eingebaute Klassen von Node als Werte führen (`toString`, `href`), statt sie als private Felder zu werten. |
| 11 | niedrig | **Mit `ITER_KAPPE` 1000 liest die Sonde zwanzigmal so weit voraus (gerechnet, nicht gemessen).** Jeder Aufruf eines langen oder endlosen Generators wird jetzt bis Element 1.001 gelesen statt bis 51, und das je Aufruf mehrfach (Muster-Varianten, Kopienprobe). Ein Generator mit Nebenwirkung je Element (Datei, Zähler, Protokoll) führt sie entsprechend öfter und früher aus. Bei f2 (1.500 ganze Zahlen) dauerte der Organlauf 1,5 s. An T4-Lasten sind die Kosten nicht gemessen. | `KERN-COMMIT.patch.txt:73-76`; `kammerprobe05.out.txt:9` | Die Kappe an der Zahl der Elemente ausrichten, die der Aufrufer tatsächlich liest, oder an einer T4-Last messen. |

## Antworten auf die Prüfpunkte

**a) Auftragspunkte, getrennt nach Modul, Organ und Laufweg**
1. **Vollständigkeitsprüfung:** gebaut (Python und TS).
   - Organ: 9 Fälle `test_v1_*`.
   - Laufweg: nur der Zweig „Enthaltung → zurückgestellt“ (`test_k4[2]`, Spezifikation R6-1).
   - Die Fälle aus Review 04 sind geschlossen, 5 von 5 (Nr. 2, 3, 5 mit zwei Fällen, 10).
   - Die Klasse ist offen: Nr. 2 und 4. Fehlalarme: Nr. 6. Folgefehler: Nr. 3.
2. **Festhalten:** gebaut.
   - Modul: 6 Meldungsfälle.
   - Laufweg: `test_f2_…[True]` scheitert an `43b8fad` an der Status-Zusicherung („ueberlebt“ statt „abgelehnt“), wie
     vorgesehen.
   - Die Klasse ist offen (Nr. 1), dazu R6-4 aus dem Bericht.
3. **Ausfall je Funktion:** gebaut (Python mit Eingrenzung, TS mit der Liste der gerufenen Funktionen).
   - Organ: 3 Fälle `test_a3_*`; an `43b8fad` rot durch `SondeAusgefallen`.
   - Laufweg: kein Nachweis.
   - Offen: Nr. 3 und Nr. 5. TS ohne Probe (steht im Bericht).
4. **Kappe:** gebaut.
   - Laufweg: 3 Fälle `test_k4_*` durch `aegis.pruefen`; an `43b8fad` scheitert `[2]` an der Status-Zusicherung.
   - „In T4-Größe gemessen“ ist nicht erfüllt. Das sagt der Bericht selbst, und ich bestätige es.
5. **Register und Tor-4-Skript:** gebaut.
   - Modul: 2 Gegenproben zum Register.
   - Laufweg: Verdrahtungstest mit Register 10 von 10 und A1 doppelt geprüft.
   - Offen: Nr. 7 und Nr. 8.
6. **Vorspann ohne Stufe 2:** gebaut.
   - Unit: 4 Fälle `test_s6_*`. Die Verweigerung bei 61 s war schon an `43b8fad` grün: Die Grenze stammt aus Runde 4 und
     war bis dahin ungetestet.
   - Laufweg: Der Vorspann des Verdrahtungstests läuft an Stufe 2.
   - Die Last ist nach der Sperrzahl bemessen (steht im Bericht, R6-3).
7. **Formmerkmale der Lastaufrufe:** gebaut.
   - Laufweg: `test_l7`, an `43b8fad` rot an der Zusicherung.
   - Die Gegenprobe fehlt (steht im Bericht).
8. **Stufe, eigene Tests, Nachspiel:** gebaut.
   - Stufe: Unit durch `aegis.pruefen` mit gestellter Messung; im Verdrahtungstest tragen 3 von 3 Urteilen mit Stufe den
     Wert 2.
   - Eigene Tests: 2 Laufweg-Fälle, 5 Kennungen als Unit.
   - Nachspiel: läuft im Verdrahtungstest; K1 urteilt wie aufgezeichnet.

**b) Vollständigkeitsprüfung:** Nr. 2, 4, 6 und 10.
- In der Kammer blind: p24b, p25, p26.
- Richtig enthalten: p24, p18c und bei q1 die Funktion `lies`.
- Lokal: 11 blinde Arten (Nr. 2) und 2 bei Ausnahmen (Nr. 4).
- TS lokal: 6 blinde Arten und 6 Arten mit Fehlalarm.
- **Massenhaftes Zurückstellen?** Auf `lagerhaus` und `logmuehle` ist keine von 66 Funktionen betroffen. Auslöser sind
  Iterator-Attribute, lange Generatoren, Tiefe über 12 und Datei- oder `StringIO`-Rückgaben. Für T4 muss das vorab
  gemessen werden (Nr. 6).

**c) Festhalten:** Nr. 1.
- Python: Typprüfung und Tautologie halten fest, gemessen in der Kammer.
- `pytest.raises` um Werkcode habe ich nicht gefahren.
- TS, gelesen: gleiche Lage bei `typeof` und `toBe`, nicht bei `toEqual`.

**d) Ausfall je Funktion**
- **Zustandslecks:** Die Eingrenzung forkt aus dem Zustand vor der Last. Danach beobachtet der Wirt die Vorgeneration
  frisch, mit denselben durchlässigen Funktionen (gelesen). Ein Leck aus dem abgebrochenen Lauf erreicht das Urteil so
  nicht. Nicht abgedeckt sind Dateisystem-Nebenwirkungen, denn Fork teilt das Dateisystem (gelesen).
- **Zeitlimit:** Nr. 5, gemessen an einer hängenden Last. Die Halbierung ist nur gerechnet.
- **Kindprozesse:** `os._exit` und `waitpid` sind vorhanden, eine Frist nicht (gelesen).
- **Nicht eingrenzbarer Auslöser:** Alle Funktionen der Last enthalten sich. Ohne gerufene Funktion bleibt es bei
  `SondeAusgefallen` (gelesen).
- **TS-Weg:** nur die Liste der gerufenen Funktionen; Nr. 3 gilt dort ebenso.

**e) Proben des Gutachtens 04 an `0c2f058`:**
- 24 von 24 verhalten sich wie spezifiziert (Liste unter „Geprüft und bestätigt“).
- Neue stille Stellen: p24b, p25, p26 (Nr. 2, 4), a3x (Nr. 3), x5 und x5b (Nr. 1).
- Neue Fehlalarme: f1 und f2 (Nr. 6).
- Neuer Totalausfall: d1 (Nr. 5).

**f) Zahlen:** siehe „Geprüft und bestätigt“. Abweichung nur bei Nr. 9.

**g) Geänderte ältere Tests:**
- 2 von 2 geänderten Testdateien sind nur ergänzt; keine Zusicherung ist gelockert.
- `test_vor_t4_04.py` ist unverändert. Sein Fall `test_r413…` bleibt grün, weil `zaehle` endlos ist; das habe ich
  bestätigt. p14 zeigt jetzt 14 Abweichungen.
- Eine zugedeckte Regression habe ich nicht gefunden.

**h) Aussagen und Lücken**
- **Stärker als der Beleg:**
  - §1: „Standarddarstellung mit Adresse“ und die Grenze „C-Erweiterungen mit eigener Darstellung ohne Adresse“;
    §13 Nr. 2: „Kopierzustand“ (alle Nr. 2);
  - §1: „ungekürzt“ (Nr. 4);
  - §3: „trifft nur die betroffene Funktion“ (Nr. 3, 5);
  - „jede Funktion“ im Register nach Entscheidung 5 (Nr. 7).
- **Lücken gegenüber dem Auftrag:**
  - Im Bericht selbst genannt: Entscheidung 4 in T4-Größe, die Gegenprobe zu Entscheidung 7, TS-Proben zu Entscheidung 2
    und 3.
  - Nicht genannt: Nr. 7 und Nr. 8.
- **Für T4 gefährlich:** Nr. 1, 2 und 3 sowie R6-1 und R6-4; außerdem Nr. 5, 6 und 8.

## Geprüft und bestätigt

- **Commit:**
  - `git log` zeigt `0c2f058` → `43b8fad` → `1d9a5aa`.
  - `COMMIT-STAT` nennt 17 Dateien, +1279/−120.
  - Im Commit stehen drei Testdateien: `drahtwerk.py`, `test_verdrahtung.py` und neu `test_vor_t4_05.py`.
    `test_vor_t4_04.py` ist nicht darunter.
- **Teilläufe, 4 von 4 wie in §9:**
  - `TEILLAUF-1`: 25 bestanden, 2 rot. Grund: `zahlen` bei 50 gekappt → Enthaltung, passt zu §14 Nr. 3.
  - `TEILLAUF-2`: 591 bestanden, 2 übersprungen, 1 rot, 93 abgewählt, 724,99 s.
  - `TEILLAUF-3a`: 6 von 6, 1719,08 s.
  - `TEILLAUF-3b`: 132 von 132, 236,82 s.
- **Regression:**
  - 598 bestanden, 2 übersprungen, 0 rot, 93 abgewählt, 2457,93 s.
  - JUnit: 600 Fälle, 0 Fehlschläge, 0 Fehler, 2 übersprungen. Darin `test_vor_t4_05` mit 27 und `test_verdrahtung`
    mit 6 Fällen.
- **Verdrahtungsbeleg der Regression:**
  - 23 von 23 Organen gerufen.
  - Register: 10 Einträge, `fehlend` leer; alle 10 Kanten einzeln in der Kantenliste gefunden.
  - 10 von 10 Befehlsschritten mit rc 0.
  - Die Tor-4-Zeile steht wörtlich wie in §9. Bei A1 sind `schwaeche_weg`, `normal_unveraendert` und `behoben` je wahr.
  - Nachspiel K1: `ueberlebt` wie aufgezeichnet, Stufe 2, 15 Kammerläufe, 0 Modellaufrufe.
  - `modellkosten_eur` 0,0.
  - 16 Aegis-Urteile: 3 tragen Stufe 2, 13 keine Stufe, weil sie vorher endeten. Das stimmt mit §9 überein.
- **Nachspiele, 7 von 7 Belegen** (N1: 3, N2: 2, N3: 2):
  - Commit `0c2f058` und sauberer Arbeitsbaum beim Import und nach dem Fall.
  - `quelle_db_sha256` vorher gleich nachher.
  - 0 Modellaufrufe, Stufe 2, `gesperrte_bereiche` leer.
- **Nachspiel-Ergebnisse:**
  - K2904 überlebt in 3 von 3, K3091 in 3 von 3; Gewinn in 6 von 6 „klar“.
  - `planung`-Quoten, 6 von 6 nachgerechnet: 0,407; 0,376; 0,384; 0,403; 0,415; 0,420.
  - K2868: abgelehnt, 40 Abweichungen. Davon 24 ungedeckt in 6 Gruppen zu je 4, wie in §9 aufgezählt, und 16 gedeckt.
    3 deckende Tests, 2 Verfälschungsläufe, 0 ausgelassen.
  - Vorprobe am Arbeitsbaum: K2904 überlebt.
- **Vorher/Nachher:**
  - 9 von 27 grün an `43b8fad`, 27 von 27 an `0c2f058`.
  - Die 18 roten Fälle nachgezählt: 15 scheitern am Verhalten, davon 3 durch `SondeAusgefallen`; 3 an einer fehlenden
    Schnittstelle (`AttributeError`). Das stimmt mit §9 überein.
- **Stufe-2-Eichung:**
  - 24 Messungen.
  - Tabelle in §6: 12 von 12 Werten bestätigt (Sperren 3/0/0 von 8, größte Toleranz 1,884/1,155/1,208, längster
    Kammerlauf 11,6/12,3/13,7 s).
  - Übrige Bereiche: 0 Sperren in 4 × 24 Messungen.
  - Dauertabelle: 12 von 12 Werten bestätigt (Median, Spanne, relative Spannweite, Sperren).
  - „t3.db unverändert: True“.
- **T4-Größe:**
  - 6 Module, 30 Funktionen, 126 Zeilen, 8 geändert.
  - Kappe 24: Bedarf 35, davon 24 gelaufen und 11 ausgelassen; 30 Kammerläufe, 30,3 s; abgelehnt.
  - Ohne Kappe: 35 Verfälschungsläufe, 41 Kammerläufe, 42,9 s; abgelehnt.
  - 324 Abweichungen, „15 von 15“ beobachtet.
  - „5 von 8 geänderten Funktionen liefern Zahlen oder Listen“: aus der Auswahl in `t4_groesse.py` nachgerechnet
    (3 Text, 3 Zahl, 2 Liste).
- **Spezifikationen und Vorproben:**
  - `SPEZ-R6-4`: 3 rot, 2 grün. `SPEZ-R6-LAUFWEG`: 1 rot, 1 grün. `SPEZ-R6-UNIT`: 2 rot, 2 grün.
  - `VORPROBE-E2`: 5 von 5 Arten, lokal und in der Kammer (pytest 8.3.3).
  - `VORPROBE-E2b`: Zahl und Liste ohne Präfix, Text mit Präfix; lokal (pytest 9.1.1) und in der Kammer (pytest 8.3.3).
- **Veröffentlichung der Runde 4:** Ordnerprüfsumme `c02d0dce…`, `fehler` leer, Webseite 200 (Ende von
  `VEROEFFENTLICHUNG-R4.txt`).
- **Proben des Gutachtens 04 an `0c2f058`: 24 von 24 gefahren, alle wie spezifiziert:**
  - x1 abgelehnt (0 von 14 gedeckt); x1k.
  - x2 abgelehnt (0 von 6 gedeckt, `festhaltend` leer); x2k.
  - x3 abgelehnt (`festhaltend` für `tab` leer); x3k.
  - q1 läuft durch: `doppel` mit 6 Abweichungen, `lies` enthält sich; q1k.
  - p21, p22, p22k, p19, p19b und p20 mit je 28 Abweichungen.
  - p18c enthält sich; p18ck mit 40 Abweichungen.
  - p18 und p18b mit je 6, p13 mit 16 Abweichungen.
  - p14 mit 14 Abweichungen (Kappe 1000; `zaehle` gekappt und gezählt).
  - p16 und p16b mit je 4, p17 mit 1, p23 mit 14 Abweichungen.
- **Geänderte ältere Tests:** 2 von 2 Dateien nur ergänzt; im Diff fehlt keine Zusicherung.
- **Kasse:** 0,00 € passt zur Verdrahtung (0,0) und zu 7 von 7 Nachspielen mit 0 Modellaufrufen.
- **R6-1 und R6-4** passen zu meinen Messungen:
  - p24 (geänderte `StringIO`-Rückgabe) enthält sich im Ganzen, f1 und f2 ebenso.
  - x5 und x5b halten fest, weil ihre Meldung ein Zitat enthält.

## Nicht geprüft

- **Teile der Fassung von 21:50 Uhr:**
  - §0 „103 von 103 Dateien“: nur das Ende des Belegs gelesen.
  - §5: die Einteilung der 13 Tor-4-Zeilen (R6-2).
  - §15.
  - `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md` der Runde 5.
  - Der Code der Tests in `spez/`; gelesen habe ich nur ihre Ergebnisdateien.
  - `AUSWERTUNG.*`, `JOB-NACH-KETTE.txt`, der Endstand von `KASSE.md` und `UEBERGABE.md`.
  - `T4-DIAGNOSE.txt` über die ersten 14 Zeilen hinaus.
  - Die Stufe-1-Angabe „übrige Bereiche 2,9 bis 12,1 ms“.
- **Die Lauf-DB** habe ich nicht geöffnet.
- **TypeScript:** keine Kammerprobe. Den Kanon habe ich nur lokal mit Node 26.8.2 gerechnet. Festhalten in TS und den
  TS-Weg von Entscheidung 3 habe ich nur gelesen.
- **Nicht als Probe gefahren:**
  - `pytest.raises` um Werkcode;
  - die Eingrenzung bei Lasten mit Threads oder mit Seiteneffekten im Dateisystem;
  - die Dauer der Halbierung an einer T4-Last;
  - ob der Drahtwerk-Lauf überhaupt eine Verhandlung auslöst;
  - p15 und p17b (nicht in der Vorlage).
- **Parallelbetrieb:** Ob der zweite Prüfer zwischen 21:41 und 21:48 Uhr Kammerläufe fuhr, habe ich nicht geprüft; die
  Container beim Start habe ich nicht gezählt. Meine Befunde sind Urteile, keine Zeiten. Nur d1 misst eine Frist, und die
  ist fest (240 s).
- **Den Reviewtext des zweiten Prüfers** habe ich nicht gelesen.

## Sperren

Keine.

Eine Zeitüberschreitung des Werkzeugs ist keine Sperre. Mein Warteskript `bash /tmp/review-vor-t4-05/warte.sh` (Warten
auf `job_kette`) brach nach 420 s ab. Ich habe es danach mit kürzerer Wartezeit wiederholt.

## Schreibort-Nachweis

**Unter `/root/`:** nichts. `/root/biotop-vor-t4-05/REVIEW.md` habe ich **nicht** geschrieben (siehe oben).

**Unter `/tmp/review-vor-t4-05/`** (TMPDIR der Läufe: `tmp/`, am Ende leer):
- **Lesende Skripte:** `status.sh`, `quellen1.sh` bis `quellen6.sh`, `belege1.sh` bis `belege3.sh`, `umgebung.sh`,
  `warte.sh`, `warte2.sh`, `wer.sh`, `abschluss.sh`, `verdrahtung_lesen.py`, `n_auswerten.py` mit `n_auswerten.out.txt`,
  `letzte.py` mit `letzte.out.txt`.
- **Kopien aus dem Commit:** `verhalten_head.py` und `kanon_head.mjs`, je aus `git show HEAD:…`.
- **Lokale Rechenproben:** `lokal_b.py` mit `lokal_b.out.txt`, `lokal_ts.mjs` mit `lokal_ts.out.txt`.
- **Kammerproben:** `kammerprobe05.py`, `kammerprobe05.out.txt`, `KAMMERPROBE05.json`.
- **Probenwerke:** `werke/`, 78 Dateien (26 Organfälle zu je 3 Dateien).
- **Diese Datei:** `REVIEW.md`.

**Eigener Fehler:** Die Datei `abschluss.sh` hatte der zweite Prüfer schon angelegt. Ich habe sie gegen 22:02 Uhr
überschrieben, ohne sie zu lesen; der Hinweis des Werkzeugs kam erst mit dem Schreiben. Sein Inhalt ist verloren.

**Nicht von mir** (im selben Ordner, nach Zeitstempel vom zweiten Prüfer): `bericht_neu.sh` (21:52 Uhr), `e2b/`,
`e2b_probe.py`, `e2b_probe.out.txt` und `__pycache__/` (alle 21:56 Uhr).

**Sonst:**
- Die Kammerläufe gingen über `biotop.organe.kammer` (netzlos). Am Ende liefen 0 Container.
- `git status` von `/root/biotop` war vor und nach meinen Läufen leer.
