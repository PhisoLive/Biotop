# Review Behebungsrunde 3 vor T4: ein Durchgang

Stand 2026-09-24, 08:25. Prüfer: unabhängiger Reviewdurchgang nach `REVIEW-AUFTRAG.md`. Geprüft wurde `BERICHT.md` in der
Fassung von 08:01:11. Offen waren dort noch `‹REVIEW›` und `‹SPERREN›`; `‹NACHHER›` und `‹REG2›` waren schon gefüllt.
Commits: `d54bf2f` (Vorgänger `6243377`) und `0aac612` (HEAD, Arbeitsbaum sauber). Belege liegen unter
`/root/biotop-vor-t4-03/`.

Kein Modellaufruf, kein Netz, kein Geld. Keine volle Regression, kein Verdrahtungstest. Meine Kammerläufe begannen um
08:11, nachdem `job_commit_regression_nachtrag.sh` um 07:59 geendet hatte (Prüfung mit `pgrep` bzw. `ps` → 0 Treffer).
Die Proben liefen in der echten Kammer (`biotop-kammer:1`, für p7/p8 `biotop-kammer:ts1`) gegen den Code von HEAD, an
eigenen Werken unter `/tmp/review-vor-t4-03/`. `git status` von `/root/biotop` war vorher und nachher leer (in 5 von 5
Probenskripten festgehalten).

**Kurzurteil:** Die fünf Lücken aus Gutachten 02 sind für ihre Probenfälle geschlossen: 14 von 14 Fallläufe der alten
Proben verhalten sich an HEAD wie spezifiziert. Die Zahlen des Berichts stimmen mit ihren Quellen überein, soweit ich sie
nachgerechnet habe (Liste unten). Die Deckung je Muster hat aber zwei gemessene Lücken im Laufweg durch `aegis.pruefen`:
- Ein einzelnes Merkmal `weissraum` für Tab, Zeilenumbruch und doppeltes Leerzeichen lässt genau die K2868-Lage durch
  (Nr. 1).
- Die Verfälschungsprobe gilt je Funktion und nicht je Aufruf. Ein Test deckt deshalb auch mit einem Aufruf, den er
  nicht zusichert (Nr. 2).

Dazu kommen zwei neue stille Stellen der Sonde:
- Zurückgegebene Iterator-Objekte werden ersetzt (Nr. 3).
- Bei `__slots__`-Klassen wird der Zustand von `self` nicht verglichen (Nr. 4).

## Befunde

| Nr | Schwere | Befund | Beleg (Datei:Zeile, Befehl, Messung) | Vorschlag |
|---|---|---|---|---|
| 1 | hoch | **Ein Test mit doppeltem Leerzeichen deckt eine Tab-/Zeilenumbruch-Regression, also die K2868-Lage.** `klassen_von` fasst doppeltes Leerzeichen, `\t`, `\n`, `\r`, NBSP usw. in *ein* Merkmal `weissraum`. Die Formvarianten der Sonde tragen dieses Merkmal ebenfalls. Nach der Lesart „je Merkmal“ deckt jeder festhaltende Test mit irgendeinem Weißraum jedes Weißraum-Muster. Messung durch `aegis.pruefen`: Der Kandidat ändert `normieren` beabsichtigt (`" "` → `"_"`) und wirft zusätzlich bei Tab/LF `ValueError`. Die Soll-Tests je Muster enthalten keinen Tab/LF, aber einen Test `normieren("a  b")`. Ergebnis: **überlebt**, 52 von 52 Abweichungen gedeckt, darunter 14 von 14 Beobachtungen `Fehler:ValueError`. Kontrolle ohne den Doppel-Leerzeichen-Test: abgelehnt, 0 von 14 gedeckt. Auftragspunkt 1 („K2868 scheitert am ungedeckten Weißraum-Muster“) hängt damit an der zufälligen Testauswahl. | `kern/py/verhalten.py:180` (`any(c in WEISS …) or '  ' in x`), `kern/ts/kanon.mjs:65` (gleich); `organe/verhaltensvergleich.py:216-233`; `/tmp/review-vor-t4-03/deckprobe.py`, `DECKPROBE.json` Fälle `x1…` / `x1k…` | Merkmale feiner fassen: je Weißraumzeichen (`tab`, `zeilenumbruch`, `cr`, `nbsp`, `doppelleer`), passend zu den Formvarianten. Für den nächsten Auftrag x1 als rote Spezifikation durch den Laufweg. |
| 2 | hoch | **Ein Test deckt, ohne festzuhalten.** Die Verfälschungsprobe verfälscht *jeden* Aufruf von `f` (je Paar Funktion/Art). Als festhaltend zählt ein Test, sobald er dabei fällt. Welche seiner Aufrufe das Merkmal liefern, spielt keine Rolle. Messung durch `aegis.pruefen`: Der Kandidat gibt Text mit Tab unverändert zurück. Ein Test ruft `normieren("a\tb c")` ohne Zusicherung und sichert nur `normieren("a b") == "a_b"` zu. Ergebnis: **überlebt**, 6 von 6 Regressionsbeobachtungen gedeckt. Kontrolle ohne den Tab-Aufruf: abgelehnt, 0 von 6. Gelesen, nicht gemessen: Ein Fehler in Setup oder Fixture zählt ebenfalls als `fail`. Eine Fixture, die das Ergebnis von `f` weiterverwendet, macht also jeden Test, der sie nutzt, zum „festhaltenden“ Test. Genau das sollte Review 02 Nr. 8 ausschließen. | `organe/verhaltensvergleich.py:236-248, 278-279, 367-370`; `kern/py/verhalten.py:549-563, 1173-1174`; `DECKPROBE.json` Fälle `x2…` / `x2k…` | Nur Aufrufe mit dem Muster der Abweichung verfälschen (`verfaelschen` mit `klassen`), nur Fehlschläge in der `call`-Phase werten und die Klassen je Test und Funktion im Urteil ablegen. |
| 3 | hoch | **Neue stille Stelle aus der Behebung von Lücke 1: Die Sonde ersetzt zurückgegebene Iterator-Objekte durch einen Generator.** `wert()` liest jedes Objekt mit `__next__` aus und gibt dem Werk `_weiter(…)` zurück. Attribute und Methoden des echten Objekts gehen dabei verloren. Messung: Die Last liest `r.nummer` des zurückgegebenen `Leser`. Unter der Sonde endet die Last auf beiden Seiten mit `AttributeError` (`korpus:last_m` = `Fehler:AttributeError`). Alle späteren Lastaufrufe fehlen still. Die Änderung an `doppel(3)` bleibt unentdeckt: 0 Abweichungen, „2 von 2 beobachtet“, tragfähig. Kontrolle ohne den Attributzugriff: 6 Abweichungen, abgelehnt. Gelesen, nicht gemessen: Betroffen sind Dateiobjekte, `csv.reader` (`line_num`) und `sqlite3.Cursor` (`fetchall`, `description`). Liefert nur eine Seite ein solches Objekt, bricht die Last nur dort ab. Die dort fehlenden Beobachtungen zählen dann als Abweichungen: Fehlalarm. Ein Lastabbruch unter der Sonde erzeugt kein Signal (weder Enthaltung noch Messgerätausfall). | `kern/py/verhalten.py:249-293`; `/tmp/review-vor-t4-03/sondenprobe3.py`, `SONDENPROBE-3.json` `p18…` / `p18b…` (inkl. `roh_vorgeneration`) | Nur echte Generatoren ersetzen (`inspect.isgenerator`), andere Iteratoren unverändert durchreichen und als Enthaltung „Iterator-Objekt“ zählen. `korpus:*` = Fehler unter der Sonde, während das Messgerät die Last fehlerfrei lief: Messgerätausfall. |
| 4 | hoch | **Der Zustand von `self` (und von Argumenten) wird bei Klassen mit `__slots__` nicht verglichen**, auch nicht bei `@dataclass(slots=True)`. `_veraenderlich` und `_instanz` verlangen `__dict__`. Es entsteht keine `>args`-Beobachtung und keine Enthaltung. Messung: Methode `buchen` ändert nur `self.stand` (Rückgabe `None`), die Last ruft sie. Ergebnis: 0 Abweichungen, „1 von 1 beobachtet“, tragfähig (p19 `__slots__`, p20 `dataclass(slots=True)`). Kontrolle ohne `__slots__`: 28 Abweichungen, abgelehnt. Entscheidung 3 („Zustand von `self` vor und nach dem Aufruf verglichen“) ist für diese Klassen nicht erfüllt. | `kern/py/verhalten.py:304-311, 402-408` (dagegen kann `kan()` Slots schon, `:114-116`); `/tmp/review-vor-t4-03/sondenprobe4.py`, `SONDENPROBE-4.json` | `_veraenderlich`, `schnappschuss`, `zuruecksetzen` und `_stoeren` auf Slot-Objekte erweitern. p19/p20 als rote Spezifikation. |
| 5 | mittel | **Die Aussage „Die fünf Lücken der Python-Sonde sind geschlossen“ (Ergebnis, §1) ist stärker als der Beleg.** Belegt ist sie je Lücke mit einem Fall; meine Wiederholung der Proben von Gutachten 02 bestätigt das (14 von 14). Für die Lückenklassen gilt sie nicht vollständig: Lücke 2 bleibt bei Slot-Objekten offen (Nr. 4). Die Iterator-Behandlung aus Lücke 1 erzeugt eine neue stille Stelle (Nr. 3). Lücke 3 selbst ist geschlossen: Eine Funktion mit nur Fehlerbeobachtungen zählt als Enthaltung. Bei Klassen ohne Vertrag bleibt eine geänderte Methode aber genau deshalb unentdeckt, weil die Instanz aus der Signatur unbrauchbar ist (Nr. 6). Koroutinen sind nur Enthaltung (Nr. 7). | BERICHT.md:19-24, 67-73; Nr. 3, 4, 6, 7 | Im Bericht auf „je Lücke der Probenfall geschlossen“ zurücknehmen und die Grenzen nennen. |
| 6 | mittel | **Klasse ohne Vertrag und ohne Konstruktion in der Last: Die Instanz aus der Signatur nimmt nur die erste Argumentliste.** Für einen unannotierten Parameter ist das `'a b'`. Wirft danach jede Methode, heißt die Enthaltung „nur Fehler oder nicht vergleichbar“, und das Urteil bleibt tragfähig. Messung: `Zaehler(start)` (ohne Annotation), Methode `weiter` geändert, von der Last nicht gerufen. Ergebnis: 0 Abweichungen, „1 von 2“, tragfähig, Instanz `signatur`. Kontrolle `start: int`: 4 Abweichungen, abgelehnt. Das ist keine „wirklich unbeobachtbare“ Stelle (Entscheidung 3). Der Grund verschleiert, dass die Instanz zwar gebaut wurde, aber unbrauchbar ist. | `kern/py/verhalten.py:813-832`; `organe/verhaltensvergleich.py:439-448`; `SONDENPROBE-3.json` `p16…` / `p16b…` | Weitere Argumentlisten versuchen (UNTYPISIERT, Randlisten), bis ein Methodenaufruf inhaltlich ist. Eigener Enthaltungsgrund „Instanz ohne inhaltlichen Aufruf“. |
| 7 | mittel | **Asynchrone Funktionen: gezählte Enthaltung, aber das Urteil bleibt „tragfähig“.** Ändert der Kandidat nur `async def hole`, lautet das Urteil: 0 Abweichungen, „1 von 2“, geurteilt, tragfähig, Enthaltung „unvergleichbar (asynchron)“. S-1 erlaubt für Koroutinen die Enthaltung je Funktion als Alternative; formal ist S-1 damit erfüllt. §6 (S-1) nennt aber nur Generatoren, und §1/§2 erwähnen die `async`-Enthaltung nicht. Eine Koroutine lässt sich in der Sonde mit einer eigenen Ereignisschleife beobachten, ist also nicht „wirklich unbeobachtbar“ im Sinn von Entscheidung 3. Ist die einzige geänderte Funktion asynchron, bleibt das Urteil trotzdem „tragfähig“. | `kern/py/verhalten.py:249-276`; `organe/verhaltensvergleich.py:442-443, 590-605`; `SONDENPROBE-3.json` `p13_async`; SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md S-1 | Koroutinen mit `asyncio.run` in der Sonde ausführen. Sonst: Ist eine *geänderte* Funktion unbeobachtet, enthält sich das Urteil, statt „tragfähig“ zu sein. |
| 8 | mittel | **K2868: Nicht belegt ist, woran die Deckung scheiterte.** 40 von 40 Mustern tragen `null_zahl` aus dem Kontextwert `gewicht: 0`. Die Verfälschungsprobe lief 0-mal, und die Klassen der 3 aufgezeichneten Testaufrufe stehen nicht im Beleg. Ob Weißraum oder nur `null_zahl` fehlte, ist offen. Zusammen mit Nr. 1 gilt: Eine K2868-artige Behebung mit einem einzigen festhaltenden Test mit doppeltem Leerzeichen und `gewicht: 0` wäre nach der Regel gedeckt. Der Bericht (§3, Offen Nr. 2) nennt die `null_zahl`-Grenze selbst; der Zusammenhang mit Nr. 1 fehlt. | `nachspiel/d1/k2868.json` (`deckung_zaehlung` {tests 3, aufrufe 3, verfaelschungen 0}, `eingaben`, `ungedeckt_aufschluesselung`); BERICHT.md §3 | Klassen je Test und Funktion in `deckung_zaehlung` schreiben. K2868 mit einem gestellten deckenden Test je Muster nachspielen (mit und ohne doppeltes Leerzeichen). |
| 9 | mittel | **Lücken gegenüber dem Auftrag, im Bericht offen geführt:** (a) Punkt 3: Methoden in TypeScript nicht gebaut (Offen 3). (b) Punkt 4: `doppelurteil` ist ein Werkzeug, das kein Organ aufruft. Für „jedes künftige Testwerk“ ist die Doppelprüfung nicht erzwungen (Offen 4). (c) Punkt 2: Die Gewinn-Nachmessung der Generalprobe (`lauf.py:417-441`) wurde nie ausgeführt: 0 von 16 Urteilen in beiden Verdrahtungsbelegen mit Nachmessung (Offen 6). (d) Punkt 2 Gegenprobe gescheitert, 2 von 3 (richtig gemeldet). | BERICHT.md §2, §5, §14; `VERDRAHTUNG-BELEG-REGRESSION(-2).json` `nachmessungen` 16/16 mit Feldern, 0 mit Ergebnis | Nicht als Behebung werten; als offene Punkte vor T4 stehen lassen. |
| 10 | niedrig | **S-10 ist als „Laufweg (`_einzelprobe`)“ ausgewiesen, der Test ruft aber `eichproben._einzelprobe` direkt.** Im Lauf wirkt `vorspann.py:187` → `eichproben.proben`. Das ist ein Organ-Nachweis mit echter Kammer, kein Laufweg-Nachweis. | BERICHT.md §6 Zeile S-10; `tests/test_eichproben.py` (neue Tests `test_s10_*`, Diff) | In §6 als „Organ“ führen, oder eine Probe durch `eichproben.proben` bzw. den Vorspann ergänzen. |
| 11 | niedrig | **Der Annahmegrund nennt einen Gewinn, den die Nachmessung nicht bestätigt hat.** Bei `bestaetigt` bleibt die erste Messung Grundlage. K2904 D1: Grund „bericht −20 %; planung −16 %“. Die Nachmessung bestätigte nur `planung` (bericht 0,916 = −8,4 %). K2904 ändert `bericht` nicht, die −20 % sind Rauschen auf einem Bereich von ≈ 4–5 ms. Umgekehrt nimmt „klar unter dem Band“ (unter 0,739 bzw. 0,697) auf *jedem* Bereich des Wirkungskreises ohne Nachmessung an. Das ist so beauftragt, bleibt bei dieser Streuung aber ein Einfallstor. | `kern/messgeraet.py:778-781, 790-793`; `nachspiel/d1/s2_k2904.json` (`gewinn_nachmessung.erste` bericht 0,8021, `zweite` 0,9158); NACHSPIEL-D1.txt | Nur bestätigte Bereiche als Gewinn führen. Rauschen je Bereich im Bericht zeigen. |
| 12 | niedrig | **Ungültige Gewinn-Nachmessung: Der Zweig ist gebaut, aber ungetestet.** In `aegis.py:1029-1030` (zurückstellen) und `lauf.py:428-433` (Messgerätausfall) ist er vorhanden. Kein Test in `tests/` nennt „Gewinn-Nachmessung“. `test_c_*` (6) und die Spezifikation (4) messen nur gültige Nachmessungen. | `grep -rn 'Gewinn-Nachmessung' tests/*.py` → 0 Treffer | Einen Fall `test_c` mit ungültiger zweiter Messung ergänzen (Erwartung: zurückgestellt). |
| 13 | niedrig | **Veraltete Kommentare im Annahmepfad.** `aegis.py:1021-1023` sagt „widersprechen sich die Messungen, weder Annahme noch Ablehnung (zurückgestellt)“; der Code poolt und entscheidet (`:1031-1035`). `aegis.py:1061-1062` beschreibt noch die Regel „mit derselben Eingabe“ aus Runde 2. | gelesen | Kommentare an den Code angleichen. |
| 14 | niedrig | **Die Zusicherung im Verdrahtungstest prüft nur, dass die Schlüssel vorhanden sind.** `aegis.py:778-779` schreibt beide Felder immer, auch als `None`. Dass die Nachmessung im Lauf je wirkt, schützt der Test nicht (Offen 6). | `tests/test_verdrahtung.py` (Diff, neue Zusicherung `schluessel == [...]`); Belege: 0 von 16 | In der Verdrahtungslast einen Kandidaten im Band stellen und `gewinn` ≠ `None` verlangen. |
| 15 | niedrig | **Verfälschungsproben ohne Obergrenze.** Je Kandidat laufen 1 Aufzeichnerlauf und dazu \|bedarf\| Läufe, mit \|bedarf\| ≤ 2 × (Zahl der abweichenden Funktionen und Methoden mit passendem Test). Jeder Lauf ist ein voller pytest-Lauf der deckenden Dateien mit bis zu 240 s Zeitlimit. Gemessen: 0 (K2868), 1 (x1, x2, p7, p8, p10), 2 (p6). Es gibt keine Kappe, kein Zeitbudget und keine Zählung im Bericht. Mit Methoden im Nenner wächst \|bedarf\| mit der Zahl geänderter Methoden. | `organe/verhaltensvergleich.py:236-248, 285-294, 317-331, 367-370`; `DECKPROBE.json`, `SONDENPROBE-HEAD.json` `deckung_zaehlung.verfaelschungen` | Kappe mit gezählter Enthaltung. Zahl der Kammerläufe je Kandidat im Urteil. |
| 16 | niedrig | **Iterator-Kappe 50:** Eine Änderung ab dem 51. Element ist unsichtbar, die Funktion gilt trotzdem als beobachtet (p14: 0 Abweichungen, „1 von 1“). S-1 erlaubte „erste N“; der Bericht schreibt aber nur „bis zu einer Kappe“, ohne N. | `kern/py/verhalten.py:57, 277-293`; `SONDENPROBE-3.json` `p14…` | N im Bericht nennen; `mehr` als Teil-Enthaltung zählen. |
| 17 | niedrig | **Muster und Klassen sind je Sprache dieselbe Rechnung, mit einer Ausnahme:** Die Sonde fügt bei Formvarianten die Formart unbedingt hinzu, der Aufzeichner rechnet nur `klassen_von`. Erzeugt `klassen_von` die Formart für denselben Wert nicht (z. B. `schluesselfolge`, wenn die Umkehrung sortierte Schlüssel ergibt), kann kein Test dieses Muster decken. Das wäre ein Fehlalarm. Gelesen, nicht gemessen. Außerdem gelesen: `beobachtet` (x von y) zählt aus `inhalt` und berücksichtigt `instabil` nicht. Eine Funktion, deren Beobachtungen alle schwanken, gilt als beobachtet. | `kern/py/verhalten.py:515, 565, 1129-1131`; `kern/ts/verhalten-runner.mjs:327, 334, 362, 368`, `deck-setup.mjs:29`; `organe/verhaltensvergleich.py:509-511, 552-553` | Formart nur ergänzen, wenn `klassen_von` sie für den Wert liefert. Instabile Funktionen aus `beobachtet` nehmen. |
| 18 | niedrig | **`bau/TEILLAUF-1.txt` enthält nur zwei Fortschrittszeilen, ohne Kopf, Befehl und Ergebnis.** Was lief und mit welchem Nenner, ist nicht belegt. Der Satz „15 von 30 … im ersten Teillauf“ (§13) stimmt mit `TEILLAUF-2.txt` überein (15 FAILED, 30 Fälle). | `bau/TEILLAUF-1.txt` (160 Bytes); `bau/TEILLAUF-2.txt` | In §13 die Datei richtig benennen; TEILLAUF-1 als unvollständig kennzeichnen. |

## Antworten auf die Prüfpunkte (Kurzfassung)

**a) Auftragspunkte, getrennt nach Modul- und Laufweg-Nachweis**

| Punkt | Laufweg (`aegis.pruefen`, echte Kammer) | Nachspiel | nur Organ / Unit |
|---|---|---|---|
| 1 Deckung je Muster | `test_b_*` (4 Fälle); meine x1/x2 (Nr. 1, 2) | K2868 2×2 | `test_deckung_je_muster_am_organ` |
| 2 Gewinnschwelle | `test_c_*` 6 Fälle (Laufzeit gestellt) | 6 von 6 echt nachgemessen, 2 von 3 gleich | Generalprobe: nur gelesen |
| 3 Methoden | `test_d_*` 3 Fälle (Python) | — | TS: nicht gebaut |
| 4 Gegenzeugen | kein Laufweg (Werkzeug) | — | `test_f_*` (Unit), Messung am Commit |
| 5 S-1…S-13 | S-1, S-2 (Py), S-3 (Lücke 3), S-4 (Lücke 4), S-5, S-6 (Py) | S-7, S-8, S-9 (Nachmessung) | **Ganz nur Organ/Unit:** S-10 (Organ mit Kammer, Nr. 10), S-11 (Unit), S-12 (Organ, Sonde gestellt). **Teilweise nur Organ/Unit:** S-3 Wurzelmodul (Organ ohne Kammer), S-4 `instabil` (Organ, gestellt), S-9 `laufzeitrisse` als Liste (Unit), S-2/S-6 in TS (Rauchprobe des Auftragnehmers, meine Organprobe p7/p8). S-13: Entscheidungen, keine Probe |

Die Gegenproben scheitern jeweils an der vorgesehenen Zusicherung: 17 von 17 Zusicherungen halten an `0aac612`, 1 von 17
an `6243377` (`NACHHER-HEAD.txt`, `VORHER-6243377.txt`).

**b) Proben des Gutachtens 02 gegen HEAD** (`SONDENPROBE-HEAD*.json`), alt → neu:

| Probe | vorher | an HEAD |
|---|---|---|
| p1 Generator | 0 | 10 Abweichungen |
| p2 Nebenwirkung | 0 | 12 `>args` |
| p3 Methode | „1 von 1“, 0 | „2 von 2“, 12 |
| p4 ohne Annotation | 0 | 32 |
| p5 Mengenfolge | 22 Fehlalarme (2 von 2) | 0 (2 von 2) |
| p12 `lru_cache` | 16 von 16 | 0, eingewickelt |
| p6 Beifang | deckte `f` | `f` nicht mehr (festhaltend `[]`), `g` je Muster 6 |
| p7 TS function | 2 von 28 gedeckt | 22 von 46 |
| p8 TS `export const` | 0 Aufrufe | wie p7 |
| p9 | `daten-import` → `[]` | `['daten-import']` |
| p10 / p10b | 0 vs 2 gedeckt | 10 = 10 |

`kurz()` trägt jetzt `nicht_eingewickelt`. Alle 5 Lücken sind für diese Fälle geschlossen.

Neue Fälle an HEAD: Stille Stellen in p13 (async, Nr. 7), p14 (Kappe, Nr. 16), p16 (Nr. 6), p18 (Nr. 3), p19/p20
(Nr. 4). Erkannt wurden p15 (veränderlicher Standardwert, 17 Abweichungen) und p17/p17b (Eigenschaft ohne Vertrag, 1
bzw. 4 Abweichungen; die multiplikative Änderung an der Signatur-Instanz mit 0 nur über `@mutation`).

**c) Deckung**
- **Dieselbe Rechnung?** Ja, je Sprache. Python rechnet `klassen_von(_gebunden(...))` an 3 Stellen, TS
  `klassenVon(args)` an 4 Stellen. Ausnahme ist die Formart (Nr. 17).
- **Ist „je Merkmal“ mit „ein Test je Muster“ vereinbar?** Nicht streng. Zwei Tests mit je einem Merkmal decken ein
  Muster, das keiner prüft. Zusammen mit dem groben `weissraum` ist die Lücke gemessen (Nr. 1).
- **Kann ein Test decken, ohne festzuhalten?** Ja (Nr. 2).
- **Kann die Verfälschungsprobe unauffällig fehlschlagen?** Nach der permissiven Seite ja: Fixture oder anderer Aufruf
  (Nr. 2). Nach der strengen Seite nur mit Ablehnung: Erreicht die Verfälschung den Aufruf nicht, bleibt die Abweichung
  ungedeckt. Ein Ausfall des Aufzeichners ist laut (`SondeAusgefallen`, `verhaltensvergleich.py:329-330`).
- **Kosten:** Nr. 15 (unbegrenzt).

**d) Gewinn-Nachmessung**
- Band, Richtungen und Poolen sind wie beschrieben gebaut (`messgeraet.py:738-810`).
- Die 6 Nachspielentscheidungen folgen aus den gespeicherten Quoten: 6 von 6 nachvollzogen.
- Das Ergebnis K2904 3 von 3 und K3091 2 von 3 ist richtig berichtet.
- Die Nachmessung wird in beiden Richtungen und nur im Band ausgelöst. Den Fall „ungültig“ prüft kein Test (Nr. 12).
- Kommentar und Code widersprechen sich (Nr. 13). Der Annahmegrund enthält einen unbestätigten Bereich (Nr. 11).

**f) Geänderte ältere Tests:** keine verdeckte Regression gefunden.
- `je_stand` ist durch S-4 (zweite Beobachtung) erzwungen.
- Die Deckungstests behalten je eine negative Kontrolle; die frühere, leere Gegenprobe hat jetzt ein Muster.
- `REF_PAAR` ruft `bericht` wieder, mit Gegenprobe „nicht baubar“.
- S-11 ist in `test_vorspann` zugesichert.
- `test_verdrahtung` ist schwach (Nr. 14).
- Der Nachtrag (Register) ist berichtigt: 8 von 8 Zeilennachweise stimmen an HEAD (`verhaltensvergleich.py:319, 376,
  406, 426`; `verhalten.py:651, 668, 681, 1186`).

## Geprüft und bestätigt

- **Commits:** `git log --oneline -4` wie im Auftrag. `biotop/` ist zwischen `d54bf2f` und `0aac612` unverändert
  (`JOB-NACHTRAG.txt`, leerer Diff). Der Nachtrag ändert 1 von 1 Dateien (`tests/test_t3_python_annahmen.py`, +16/−5).
- **Regression `d54bf2f`:** 532 bestanden, 2 übersprungen, 1 fehlgeschlagen, 93 abgewählt, 1507 s. JUnit: 535 Fälle,
  1 Fehlschlag, 0 Fehler, 2 übersprungen. `test_vor_t4_03`: 38 von 38 grün.
- **Regression `0aac612`:** 533 bestanden, 2 übersprungen, 0 fehlgeschlagen, 1491 s. JUnit: 535, 0, 0.
  `test_t3_python_annahmen`: 5 von 5 grün.
- **Verdrahtung:** beide Belege 23 von 23 Organe, 0,0 €, 16 von 16 Urteile mit Feldern, 0 von 16 mit Nachmessung
  (2 von 2 Belegen).
- **Vorher/Nachher (§1, 17 Fälle):**
  - Vorher: 1 von 17 Zusicherungen, 2 Abbrüche (`KeyError 'instabil'`, `'ungedeckt_aufschluesselung'`). Jeder
    Kammerfall hat 36 `woerter`-Abweichungen, `lru_cache` 52 = 36 + 16.
  - Nachher: 17 von 17. Generator 20, Nebenwirkung 36, `verbinde` 32, `woerter`/`lru_cache` 0; Instanz `vertrag`,
    Hashsaat `0` in 15 von 15 Kammerfällen.
  - Zeilen §1: 5 von 5 bestätigt. Laufweg-Tabelle §3: 4 von 4 bestätigt (52/52 überlebt; 46 von 52; 52 von 58;
    2 von 58; vorher 72 von 72 bzw. 24 von 78).
- **K2868 2×2:** 4 von 4 Zellen bestätigt (12/0/überlebt, 40/0/überlebt, 12/12/abgelehnt, 40/40/abgelehnt).
  - Aufschlüsselung: 7 Klassen, Summe 40; 20 mit `weissraum`; `null_zahl` in 40 von 40.
  - S-8: 25 Formvarianten, ohne Formvariante 8 von 10.
  - `deckung_zaehlung`: 3 Tests, 3 Aufrufe, 0 Verfälschungen.
- **Gewinn (§4):**
  - Tabelle 6 von 6 Zeilen bestätigt. Bänder: K2904 `planung` 0,7253…0,9962, K3091 0,699…1,0336.
  - K3091 über 9 Messungen: Median 0,8301, Mittel 0,8248, s = 0,0351, Spanne 0,7779…0,8726, 3 von 9 über 0,85.
  - K2904: Median 0,8154, s = 0,0282, 0 von 9 über 0,85.
  - D2 gepoolt: s = 0,636 ms (6,6 %) bzw. 0,620 ms (7,6 %).
  - Die √2-Rechnung ist richtig und als Rechnung gekennzeichnet.
- **Rissprobe (§7):** 765,06 ms gegen 0,0935 ms, danach 772,15 ms gegen 0,0847 ms; 2 gepaarte Messungen, abgelehnt.
  Gegenprobe: 1 gepaarte Messung, −3 → −2, überlebt. Faktor ≈ 8.200 (erste Messung) bzw. ≈ 9.100 (Nachmessung); der
  Bericht sagt „× 9.000“.
- **Gegenzeugen (§5):** 6 von 6 Zeilen bestätigt; `siegel_unveraendert` true.
- **KASSE:**
  - 10 von 10 Nachspiel-Belege haben `quelle_db_sha256_vorher` = `…nachher` und `modellaufrufe_echt` 0.
  - Codestand `d54bf2f` sauber in 10 von 10.
  - `spez`-Kopie unverändert, 4 von 4 grün am Arbeitsbaum.
- **Proben des Gutachtens 02 an HEAD:** 14 von 14 Fallläufe plus p9 wie spezifiziert (Abschnitt b).
- **`git status` von `/root/biotop`:** leer vor und nach meinen 5 Probenskripten. Die Originale unter
  `/root/biotop-vor-t4-02/review-proben/` sind unverändert (nur gelesen, Kopien angepasst).

## Nicht geprüft

- **§0 Verdichtung** (`logs/agent.log`): außerhalb der Prüfpunkte a–g.
- **Lauf-DB `t3.db`:** nicht geöffnet. Keine Nachrechnung brauchte sie; die Nachspiel-Belege tragen die Werte und die
  sha-Kontrolle.
- **Wirkt die Generalprobe (`lauf._generation_koerper`)?** Nur gelesen. Ausführen würde einen Lauf bzw. den
  Verdrahtungstest verlangen, und den verbietet der Auftrag.
- **Mitgebrachte Kandidatentests als deckende Tests:** Ob vom Kandidaten mitgebrachte Tests zu den deckenden Tests
  gehören, ist nicht geprüft. Davon hängt ab, ob der Schwarm Nr. 1/2 selbst ausnutzen kann. `aegis.py:1059-1065` ist
  gelesen, die Herkunft von `testbestand` nicht verfolgt.
- **TypeScript:** `>args`, `async`/`__promise` und Klassen nicht eigens geprüft, nur p7/p8.
- **Nachspiel-, Rissproben- und Gegenzeugen-Skripte:** nicht im Einzelnen gelesen, nur ihre Ausgaben.
- **Typtreuer Ausgangsdefekt in `eichproben.py`:** nur im Diff gelesen, keine eigene Probe.
- **`je_stand`:** Nachgesehen habe ich die Stellen im Diff von 3 Dateien. Die Zählung „15 Stellen“ ist nicht
  nachgezählt.
- **Volle Regression und Verdrahtungstest:** nicht selbst ausgeführt (Auftrag); die Job-Ergebnisse sind gelesen.

## Sperren

keine

## Schreibort-Nachweis

- `/root/biotop-vor-t4-03/REVIEW.md` (diese Datei). Sonst nichts unter `/root/`.
- Unter `/tmp/review-vor-t4-03/`:
  - **Probenkopien:** `sondenprobe.py` und `sondenprobe2.py` (Kopien der Proben von Gutachten 02, nur Pfade/`pgrep`
    angepasst).
  - **Eigene Proben:** `sondenprobe3.py`, `sondenprobe4.py`, `deckprobe.py`, `lauf_proben.sh`.
  - **Ausgaben:** `sondenprobe.out.txt`, `sondenprobe2.out.txt`, `sondenprobe3.out.txt`, `sondenprobe4.out.txt`,
    `deckprobe.out.txt`, `LAUF-PROBEN.txt`, `SONDENPROBE-HEAD.json`, `SONDENPROBE-HEAD-2.json`, `SONDENPROBE-3.json`,
    `SONDENPROBE-4.json`, `DECKPROBE.json`.
  - **`diffs/`:** 21 Dateien, der Kern-Commit je Datei zerlegt.
  - **Probenwerke:** `werke/` (28 Dateien), `werke2/` (9), `werke3/` (27), `werke4/` (9).
  - **`tmp/`:** TMPDIR der Probenläufe, danach leer.
- Die Kammerläufe gingen über `biotop.organe.kammer` (Docker, netzlos). Nach den Läufen gab es keine verbliebenen
  Einträge in `/tmp` außerhalb von `/tmp/review-vor-t4-03/` (Prüfung mit `find /tmp -maxdepth 2 -newermt …`). Die
  Änderungszeit von `/tmp` selbst ist neuer; ein kurzlebiger Eintrag wurde also angelegt und wieder entfernt.
- Außerhalb meines Zugriffs: `find /root -newer …` zeigt neben `REVIEW.md` noch `/root/.local/share/tirith/log.jsonl`
  und `log.jsonl.head`. Das ist das Protokoll der Ausführungsschicht (Befehlsprüfung), nicht von mir geschrieben.
  `git status` von `/root/biotop` ist am Ende leer (0 Zeilen).
