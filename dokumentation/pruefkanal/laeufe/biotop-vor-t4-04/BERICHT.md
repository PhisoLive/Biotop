# Behebungsrunde 4 vor T4: Gegenproben der Entscheidungen 1, 3 und 4 erfüllt; die vier hohen Befunde sind für ihre Probenfälle geschlossen, die Fehlerklassen nicht (Review: 2 neue hohe Befunde, an Runde 5)

Stand 2026-09-24. **Biotop-Modellgeld 0,00 €** (`KASSE.md`). Kern-Commit **`1d9a5aa`** (Runde 4; 18 files changed, 1112 insertions(+), 134 deletions(-)) und Nachtrag **`43b8fad`** (3 files changed, 83 insertions(+), 3 deletions(-); `COMMIT-2-STAT.txt`, `KERN-COMMIT-2.patch.txt`) auf `0aac612` (`COMMIT-STAT.txt`,
`KERN-COMMIT.patch.txt`). Ein Reviewdurchgang (`REVIEW.md`, §10).

Auftrag (Philipp, 24.09., Entscheidungen Chat-Claude zu den sechs offenen Punkten aus `laeufe/biotop-vor-t4-03` §14):
(1) Vergleichslast Stufe 2 mit zehnfacher Eingabegröße, Kammerlauf unter einer Minute, an ihr Gewinn und Laufzeitgrenze
jeder Nische, Gegenprobe K2904/K3091 drei von drei, T3s Ergebnisse unverändert; (2) die vier hohen Befunde vor T4, jede
Formvariante ein eigenes Merkmal; (3) Merkmale nicht veränderter Argumente gehören nicht zum Muster, Gegenprobe K2868;
(4) vom Kandidaten mitgebrachte Tests decken nicht, Gegenprobe Rückschritt mit eigenem Test; (5) TypeScript-Methoden vor
T5, doppelte Gegenzeugen-Prüfung verbindlich in der Torzeile „Schwächen“; (6) der Fehlalarm als sachlicher Text. Dazu
aus R4-1 … R4-20 alles, was T4 gefährden würde, der Rest mit Begründung auf die Liste.

**Ergebnis:**
- **Entscheidung 1 (Stufe 2):** 12 von 12 Kammerläufen der Stufe 2 unter 60 s (längster 11,7 s). K2904 und K3091
  überleben an Stufe 2 in je 3 von 3 Durchgängen (N1–N3 am Nachtrag `43b8fad`), `planung`-Quote 0,376–0,455, alle
  „klar“ unter dem Band. Aber: `eingang` war in 3 von 6 Stufe-2-Nachspielen gesperrt (Offen Nr. 2).
- **Entscheidung 2 (vier hohe Befunde):** die 23 neuen Testfälle 6 von 23 grün an `0aac612`, 23 von 23 an `1d9a5aa`; das
  Review fuhr 14 von 16 Originalproben an `43b8fad` neu, 14 von 14 wie spezifiziert. **Nicht geschlossen sind die
  Klassen:** ein Test hält ein Merkmal fest, ohne es zu unterscheiden (Review Nr. 1, gemessen durch `aegis.pruefen`:
  Kandidat überlebt), und `__slots__` mit Vererbung bleibt still (Nr. 2: 0 statt 28 Abweichungen).
- **Entscheidung 3 (Muster):** K2868 abgelehnt, 16 von 40 Abweichungen gedeckt (die ungültigen Eingaben), 24 ungedeckt
  (20 Weißraum, 4 führende Null).
- **Entscheidung 4 (eigene Tests):** der Kandidat mit Rückschritt und eigenem Test wird abgelehnt (an `0aac612`
  überlebte er).
- **Entscheidung 5:** Torzeile „Schwächen“ gebaut; am T3-Werk 0 von 5 nach doppelter Prüfung (Feststellung). Sie hat
  keinen Aufrufer (Review Nr. 7). TS-Methoden auf der Liste (vor T5).
- **Entscheidung 6:** `FEHLALARM-SICHERHEITSFILTER.md` im Ordner.
- **Regression:** `1d9a5aa` 562 bestanden / 2 übersprungen / 0 rot; `43b8fad` 569 / 2 / 0. Verdrahtung 23 von 23
  Organen, 0,00 €. Nachspiele am Commit `1d9a5aa`: 7 von 7 abgebrochen (eigener Fehler, §13 Nr. 1), im Nachtrag
  behoben.
- **Biotop-Modellgeld 0,00 €.**

## 1. Vergleichslast Stufe 2 (Entscheidung 1)

**Bau.** `biotop/kern/referenzlast/versandwerk-t3-02.stufe2.mjs`: dieselben fünf Bereichslasten wie Stufe 1, je Bereich
zehnmal so viele Elemente je Aufruf (Sendungen 90 → 900 bzw. 33 → 330, Tarifschleife 150 → 1.500, Zahlenliste
100 → 1.000), gleiche Wiederholungszahlen. Die Werte bleiben im gültigen Wertebereich der Stufe 1. Stufe 1
(`versandwerk-t3-02.mjs`) ist unverändert — T3s Ergebnisse, die Sonde und das Verhaltensraster `beobachten()` bleiben,
wie sie waren.
- `lauf._referenzlast(…, stufe=2)`; `aegis.pruefen(…, referenzlast_laufzeit=…)`: gepaarte Messung, Riss-Nachmessung und
  Gewinn-Nachmessung an Stufe 2, auch in der Verhandlung und in der Generalprobe (`lauf._generation_koerper`); die Stufe
  steht im Urteil (`laufzeit_stufe`). Fehlt einem Werk die Stufe 2, gilt Stufe 1 — dann steht 1 im Urteil.
- Vorspann: die Rauschmessung misst an Stufe 2 mit demselben Instrument wie die gepaarte Messung
  (`eichung.laufzeit_einmal`), misst die Dauer jedes Kammerlaufs und verweigert den Lauf, wenn einer 60 s erreicht.
- Nachspiel: die Läufe 37/38 lagen vor der Stufe 2; ihr Vorspann trägt die Rauschmessung der Stufe 1. Das Nachspiel
  misst die Rauschtoleranz deshalb an Stufe 2 selbst (fünf Kammerläufe an der Vorgeneration, dieselbe Regel) und
  schreibt die Herkunft in den Beleg.

**Gemessen** (`proben/STUFE2-ZEITEN.txt/.json`, an den Vorgenerationen und Kandidaten K2904/K3091, je Stand und Stufe
3 Kammerläufe, T3-DB vorher = nachher):
| | Kammerlauf Stufe 1 (n = 6) | Kammerlauf Stufe 2 (n = 6) | `planung` Quote Stufe 1 | `planung` Quote Stufe 2 |
|---|---|---|---|---|
| K2904 | 6,0 … 6,8 s | 8,9 … 11,7 s (Median 10,1) | 0,851 | 0,399 |
| K3091 | 5,8 … 6,3 s | 8,6 … 11,1 s (Median 9,7) | 0,839 | 0,420 |
- Jeder Kammerlauf der Stufe 2 bleibt unter 60 s (12 von 12, längster 11,7 s).
- Die S2-Behebung ist eine Laufzeitordnung (quadratisch → linear): ihr Gewinn wächst mit der Eingabe. An Stufe 1 lag
  die `planung`-Quote in dieser Messung genau an der Schwelle 0,85 (K3091 0,839, K2904 0,851 — also einmal knapp
  darunter, einmal knapp darüber), an Stufe 2 bei ≈ 0,40, rund 45 Punkte unter ihr. Das ist der Mechanismus, der
  „drei von drei“ tragen soll.
- Erste Fassung der Stufe 2 gescheitert: `skalar(i * 100)` mit i bis 1.500 riss den Wertebereich des Werks
  („RangeError: Gewicht ausserhalb 0..30000“, an beiden Ständen, `proben/STUFE2-ZEITEN-erste-fassung.*`). Korrigiert:
  zehnfache Menge, gleiche Werte.

**Gegenprobe im Nachspiel** (am Nachtrag-Commit, drei Durchgänge):
**Gegenprobe erfüllt: K2904 und K3091 in 3 von 3 Durchgängen gleich entschieden** (beide überlebt in N1, N2, N3;
`nachspiel/NACHSPIEL-N1..3.txt`, `n1..n3/*.json`, am Nachtrag `43b8fad`, Arbeitsbaum sauber in 7 von 7 Belegen).
Die Nachspiele am Commit `1d9a5aa` (D1–D3) brachen alle ab, ohne Urteil — ein eigener Fehler, §13 Nr. 1.

| Durchgang | K2904: `planung` Quote (Stufe 2) | Urteil | K3091: `planung` Quote (Stufe 2) | Urteil |
|---|---|---|---|---|
| N1 | 0,376 | überlebt | 0,392 | überlebt |
| N2 | 0,454 | überlebt | 0,455 | überlebt |
| N3 | 0,429 | überlebt | 0,414 | überlebt |

- Alle sechs Gewinne liegen **klar** unter dem Band (Band für `planung` 0,715 … 1,011 je nach gemessener Toleranz) — keine
  Gewinn-Nachmessung nötig. Zum Vergleich Runde 3 an Stufe 1: K3091 lag in 3 von 9 gepaarten Messungen über 0,85.
- Die Rauschtoleranz maß jedes Nachspiel selbst an Stufe 2 (fünf Kammerläufe an der Vorgeneration, längster 11,5 s;
  §1). Dabei wurde **`eingang` in 3 von 6 S2-Nachspielen gesperrt** (K2904 N1, N2; K3091 N3): Die Stufe-2-Last von
  `eingang` streut stark (in `STUFE2-ZEITEN` Spannweite bis 0,53). K2904/K3091 ändern `eingang` nicht; für einen
  Kandidaten in `eingang` wäre der Bereich gesperrt. Offen Nr. 2.
- **Die Bestätigungsmessung wirkte erstmals in einem Nachspiel wirklich:** K3091 N3 riss an Stufe 2 in `tarife`
  (×1,158 gegen Toleranz 1,15) und `zahlen` (×1,236 gegen 1,16) — zwei Bereiche, die der Kandidat nicht berührt. Die
  gepaarte Nachmessung bestätigte keinen der beiden Risse (×1,055 bzw. ×0,968); der Kandidat überlebte. Ohne sie wäre
  er am Rauschen abgelehnt worden (Runde 3: 0 von 10 Nachspiel-Entscheidungen mit Riss).
- Annahmegrund nur mit bestätigten Gewinnen (R4-8): K2904 N2 und K3091 N3 nennen nur `planung` („nur bestätigte
  Gewinne“); `bericht` lag dort im Band.
- Datenbank vorher = nachher in 15 von 15 Nachspiel-Belegen dieser Runde (d1–d3, Vorprobe, n1–n3;
  `nachspiel/EINZELHEITEN.txt`).

## 2. Die vier hohen Befunde des Reviews 03 (Entscheidung 2)

Jeder Befund ist als Test gefasst (`tests/test_vor_t4_04.py`, Gruppe H) und durch den Laufweg geprüft: `aegis.pruefen`
in der echten Kammer, gestellt sind nur das Modell und die Laufzeit. **Vorher/Nachher:** dieselben 23 Testfälle
(Gruppen H, E3, E4, R4-5/6/13/14 und die Paritätsprobe) am Code von `0aac612` und am Code von `1d9a5aa`, beide aus
`git archive`, die Tests jeweils aus dem neuen Commit (`proben/VORHER-0aac612.*`, `NACHHER-HEAD.*`).
**An `0aac612` waren 6 von 23 grün, an `1d9a5aa` 23 von 23.**

| Befund Review 03 | Fall | an `0aac612` | an `1d9a5aa` | Gegenprobe |
|---|---|---|---|---|
| Nr. 1 (hoch): gemeinsames Merkmal `weissraum` | x1: Tab/Zeilenumbruch werfen, ein Test mit doppeltem Leerzeichen | **überlebt** | abgelehnt, ungedeckt u. a. `tab` | Tests je Formvariante, richtige Behebung: überlebt |
| Nr. 2 (hoch): Verfälschung je Funktion | x2: ein Tab-Aufruf ohne Zusicherung neben `normieren("a b") == "a_b"` | **überlebt** | abgelehnt; der Test hält `tab` nicht fest | mit Zusicherung: der Test fällt am Kandidaten (Werkstest fängt es) |
| Nr. 2, Fixture | eine Fixture sichert `f` zu, der Test nicht | rot (die Verfälschung kannte kein Merkmal: `TypeError … haelt() takes 2 positional arguments but 3 were given`) | Fixture-Fehler hält nichts fest | dieselbe Zusicherung im Test: hält fest |
| Nr. 3 (hoch): Iterator-Objekt ersetzt | p18: die Last liest `r.nummer` | **tragfähig, 0 Abw.** | abgelehnt, `doppel` gesehen, Iterator-Objekt gezählt | p18b ohne Attribut: gesehen |
| Nr. 4 (hoch): `__slots__` | p19, p20: `buchen` ändert nur `self` | **tragfähig, 0 Abw.** | abgelehnt an `…>args` | ohne `__slots__`: abgelehnt; umgeschrieben: 0 Abweichungen |

Umgesetzt (`kern/py/verhalten.py`, `kern/ts/kanon.mjs`, `verhalten-runner.mjs`, `deck-setup.mjs`, `deckung.mjs`,
`organe/verhaltensvergleich.py`):
- **Merkmal je Formvariante** (Entscheidung 2): `tab`, `zeilenumbruch`, `cr`, `crlf`, `nbsp`, `weissraum_sonst`,
  `doppelleer`, `rand_vorn`, `rand_hinten`, `gross`, `klein`, `zahlform_null_vorn`, `zahlform_null_hinten`, dazu
  `zahltyp`, `behaelter`, `schluesselfolge`. Python und TypeScript rechnen gleich; der Paritätstest vergleicht 19 Proben
  in beiden Sprachen: 19 von 19 gleich.
- **Verfälschung je Merkmal:** Der Aufzeichner verfälscht nur Aufrufe, deren Eingabe das Merkmal trägt. Beim gewöhnlichen
  Muster sind es alle Aufrufe. „Hält fest“ heißt: die Zusicherung im Test fällt. Ein Fehler in Aufbau oder Abbau
  (Fixture, `beforeEach`) oder ein Skip ist `fehler`, nicht `fail`.
- **Iteratoren:** Nur Generatoren und eingebaute Iteratoren werden ausgelesen und ersetzt. Ein Iterator-Objekt des Werks
  bleibt unverändert und ist als Teil-Enthaltung gezählt (`teilweise`). Im Nachtrag kommt dazu: Bricht eine Bereichslast
  unter der Sonde an der Vorgeneration ab, ist das ein Messgerätausfall statt einer stillen Lücke.
- **`__slots__`:** Der Zustand eines Objekts umfasst `__dict__` und alle Slots der Klassenhierarchie (Schnappschuss,
  Rücksetzen, Mutieren, Instanzrezept).

## 3. Muster nur aus veränderten Argumenten (Entscheidung 3)

**Regel:** Das Muster einer Beobachtung sind die Formvarianten-Merkmale, die die Veränderung der Sonde an einem Argument
einführt: die Merkmale danach minus die Merkmale davor, nur an den veränderten Argumenten
(`kern/py/verhalten.py::_muster_von`, `verhalten-runner.mjs::musterVon`). Lastaufrufe und die Grundliste haben das
gewöhnliche Muster `[]`. Randwerte wie leer, `None`, lang oder nicht-ASCII sind keine Formvarianten und tragen kein
Merkmal (eigene Lesart der Entscheidungen 2 und 3, §12 Nr. 2).
- Am Organ (`test_e3_*`): Die Tab-Formvariante von `ausdruck('grund + gewicht * 2', {gewicht: 0, …})` hat das Muster
  `['tab']` statt `null_zahl` aus dem unveränderten `gewicht`. Der Randwert `'a'` ist gewöhnlich. Gegenprobe: eine
  Umformung, die an einem Argument, das schon Tab trägt, kein neues Merkmal einführt, hat das Muster `[]`.
- **Gegenprobe K2868** (Nachspiel am Commit): **erfüllt** (N1, `nachspiel/n1/k2868.json`): abgelehnt, **24 von 40 Abweichungen ungedeckt, 16 gedeckt**.
  - Gedeckt (16): die drei Randfälle mit ungültigen Bezeichnern (`~rand#2`, `#5`, `#6`, je mit `@alias`, `@mutation`,
    `@nach_ruecksetzung`: 12) und die Großschreibungs-Formvariante (`~form#8`: 4). Die deckenden Tests sind die drei
    Befundklassen-Tests des Anklägers (`test_umgehung_0…2`); sie rufen `ausdruck` mit Klassen `gross`, `lang` und halten
    das Ergebnis fest (Verfälschungsprobe gewöhnlich und `gross`: 3 von 3 fallen). In Runde 3 waren diese 16 ungedeckt,
    weil jedes Muster `null_zahl` aus dem unveränderten `gewicht: 0` trug.
  - **Ungedeckt (24): 20 Weißraum-Formvarianten** — Tab, Zeilenumbruch, CRLF, NBSP und Rand mit Tab/Zeilenumbruch, je 4 —
    **und 4 mit führender Null** (`zahlform_null_vorn`, `~form#7`). Gelesen, nicht ausgeführt
    (`proben/LESEN-NACHFRAGEN.txt`): die Normalversion erkennt Zahlen mit `\d+(?:\.\d+)?`, nimmt eine führende Null
    also an; der S1-Harness führt „führende Null“ (`007`, `08.5`, `00`) als eigene Kategorie seiner Sondereingaben.
    Welche Werte die Vorgeneration und K2868 für `~form#7` liefern, steht nicht im Beleg (`werte` trägt die ersten 10
    Abweichungen). Diese 4 sind also eine weitere, nicht auf Weißraum beschränkte Abweichung von K2868, die kein Test
    deckt — kein Widerspruch zur Gegenprobe, aber ihr Inhalt ist nicht belegt (Offen Nr. 4).
  - Kein Test des Kandidaten war beteiligt (`eigene_tests_ausgeschlossen`: leer).

## 4. Eigene Tests decken nicht (Entscheidung 4)

**Regel** (`aegis.eigene_tests`): Tests, die der Kandidat neu mitbringt oder deren Quelltext er gegenüber der
Vorgeneration ändert, decken nicht. Das gilt für Testdateien und Vertragsdateien seines Diffs, in Python per Syntaxbaum
(auch Methoden von Testklassen), in TypeScript über den Syntaxbaum der Kammer. Decken dürfen weiterhin Tests der
Vorgeneration einschließlich Generation 0, die Immun- und Befundklassen-Tests des Anklägers und die versiegelten
Gegenzeugen. Die ausgeschlossenen Tests stehen im Urteil (`eigene_tests_ausgeschlossen`).
- **Gegenprobe durch `aegis.pruefen`** (`test_e4_*`): Der Kandidat bricht Tab (wirft `ValueError`) und bringt einen
  eigenen Test mit, der genau diesen Rückschritt zusichert. Der Test ist gültig nach der Norm-Regel (Verweis auf
  Verfassung Satz 2), kommt also in den Testbestand, fällt an der Vorgeneration und besteht am Kandidaten. Ergebnis:
  **abgelehnt**, alle ungedeckten Abweichungen tragen `tab`, der Test steht als ausgeschlossen im Urteil. An `0aac612`
  überlebte derselbe Kandidat („Kernmaß −13 → −2 (+11)“).
- Kontrolle: Derselbe Test liegt schon in der Vorgeneration. Dann deckt er, der Kandidat überlebt. Nur die Herkunft des
  Tests unterscheidet die beiden Fälle.

## 5. Torzeile „Schwächen“ und TypeScript-Methoden (Entscheidung 5)

- **Torzeile „Schwächen“** (`kern/gegenzeugen.torzeile_schwaechen`): Eine versiegelte Schwäche zählt nur als behoben,
  wenn beide Prüfungen gemessen sind und halten: Schwäche weg und Verhalten gegen die Normalversion unverändert. Nicht
  beurteilbar zählt nie als behoben, null Schwächen sind nicht erfüllt. Die Prüfung ist verbindlich in der Torzeile, nicht
  im Annahmepfad. Vier Fälle im Nachtrag (`test_torzeile_schwaechen_verlangt_beide_pruefungen`): 80 % erfüllt; eine
  Schwäche mit verändertem Normalverhalten kippt die Zeile auf 3 von 5; nicht beurteilbar kippt sie ebenso; leer ist
  nicht erfüllt.
- **Am T3-Werk angewandt** (`s1/TORZEILE-SCHWAECHEN-T3-am-commit.txt`, nur gelesene Messungen, nichts neu versiegelt):
  | Stand | nur versiegelter Gegenzeuge (Schwäche weg) | doppelte Prüfung | nicht beurteilbar |
  |---|---|---|---|
  | Endstand Lauf 38 | 4 von 5 (S1–S4) | **0 von 5** | S2, S3, S4 |
  | Endstand Lauf 37 | 3 von 5 (S1, S2, S4) | **0 von 5** | S2, S4 |
  S1 ist in beiden Läufen gemessen nicht behoben (Verhalten verändert, 12.206 von 12.206 Ausdrücke mit Zeilenumbruch
  abgewiesen). Für S2–S5 wurde das Normalverhalten gegen die Normalversion nie gemessen; es gibt keinen Harness wie für
  S1. Diese Schwächen sind deshalb nicht beurteilbar. **Das ist eine Feststellung, keine Neubewertung von T3:** Die
  Regel gilt nach Entscheidung 5 für künftige Testwerke. Für jedes künftige Testwerk braucht jede versiegelte Schwäche
  deshalb einen eigenen Normalvergleich (Offen Nr. 3).
- **Methoden von Klassen in TypeScript:** vor T5, nicht vor T4 (Entscheidung 5). Nicht gebaut, auf der Liste (§7, R4-17).

## 6. Fehlalarm des Sicherheitsfilters (Entscheidung 6)

`FEHLALARM-SICHERHEITSFILTER.md`: drei Fälle (Prüfer Runde 2; zweimal bei mir in Runde 3), Befehlsmuster mit neutralen
Platzhaltern, Sperrwortlaut, was für einen Fehlalarm spricht (die getrennten Schritte liefen ohne Sperre), Vermutung zum
Auslöser (als Vermutung gekennzeichnet), Bitte an den Hersteller. Keine Projektinterna. Ob er eingereicht wird,
entscheidet Philipp.

## 7. R4-1 … R4-20: gebaut oder auf der Liste

Maßstab: Gefährdet der Punkt T4 (Python-Werk, 6.000–10.000 Zeilen, ohne Testsammlung, gewachsene Altlasten)?

| Nr | Inhalt | Stand | Begründung |
|---|---|---|---|
| R4-1 | Merkmale je Formvariante | **gebaut** (Entscheidung 2) | Befund hoch; ließ die K2868-Lage durch |
| R4-2 | Verfälschung je Merkmal, nur `call`-Phase | **gebaut** | Befund hoch |
| R4-3 | nur Generatoren ersetzen; Lastabbruch unter der Sonde = Ausfall | **gebaut** (zweiter Teil im Nachtrag) | Befund hoch; stille Stelle |
| R4-4 | `__slots__` | **gebaut** | Befund hoch; T4 hat Klassen |
| R4-5 | Instanz aus der Signatur erproben | **gebaut** | T4 hat keine Tests, also wenige Vertragsrezepte: Klassen hängen an der Signatur |
| R4-6 | Koroutinen | **gebaut** (eigene Ereignisschleife) | still und doch „tragfähig“ |
| R4-7 | K2868 mit gestelltem deckendem Test je Muster | **teilweise**: Klassen je Test im Beleg; die Entscheidung-3-Gegenprobe am Nachspiel (§3). Kein eigener gestellter Test je Muster an K2868 | T3-Nachweis, gefährdet T4 nicht |
| R4-8 | Annahmegrund nur mit bestätigten Gewinnen | **gebaut** | gering, aber Belegtreue |
| R4-9 | Test: ungültige Gewinn-Nachmessung | **gebaut** (`test_r49_*`, zurückgestellt; Gegenprobe) | ungetesteter Zweig |
| R4-10 | Kommentare in `aegis.py` | **gebaut** | Lesbarkeit |
| R4-11 | Generalprobe: Gewinn-Nachmessung einmal wirklich ausführen | **gemessen**: ein vorhandener Test (`test_vorspann`, `nur_gesperrtes_rauschen`) erreicht `gewinn_bestaetigen` in `lauf._generation_koerper` — 1 Aufruf, Ergebnis `bestaetigt` (gestellte Laufzeit; `proben/SPION-GEWINN.txt`). Die Verdrahtungslast selbst ist unverändert | Nachweis des Weges, ohne den Verdrahtungstest umzubauen |
| R4-12 | Kappe der Verfälschungsläufe | **gebaut** (24 je Kandidat, Rest gezählt) | T4 ist groß: ohne Kappe unbegrenzte Kammerzeit |
| R4-13 | Iterator-Kappe gezählt | **gebaut** | stille Teil-Enthaltung |
| R4-14 | instabile Funktionen nicht beobachtet; Formart nur, wenn `klassen_von` sie liefert | **gebaut** (zweiter Teil gegenstandslos: das Muster rechnet jetzt nur `klassen_von`) | Nenner-Treue |
| R4-15 | Vergleichslast vergrößern | **gebaut** (Entscheidung 1, Stufe 2) | Gegenprobe 3 von 3 |
| R4-16 | Muster ohne nicht veränderte Argumente | **gebaut** (Entscheidung 3) | |
| R4-17 | Methoden in TypeScript | **Liste** | Entscheidung 5: vor T5; T4 ist Python |
| R4-18 | Doppelprüfung verbindlich | **gebaut** in der Torzeile (Entscheidung 5); Normalvergleich je Schwäche ist Aufgabe des Testwerk-Baus (Offen Nr. 3) | |
| R4-19 | S-12 und S-3 (Wurzelmodul) durch den Laufweg | **Liste** | beide sind am Organ belegt und liegen im selben Aufruf von `verhaltensvergleich.pruefen`, den `aegis.pruefen` ruft; kein T4-Risiko, nur ein fehlender Laufweg-Beleg |
| R4-20 | eigene Tests decken nicht | **gebaut** (Entscheidung 4) | |

## 8. Volle Regression und Verdrahtung

| Stand | bestanden | übersprungen | fehlgeschlagen | JUnit (Fälle / Fehlschläge / Fehler) | Dauer | Verdrahtung |
|---|---|---|---|---|---|---|
| `1d9a5aa` (`REGRESSION.txt`) | 562 | 2 | 0 | 564 / 0 / 0 | 1628 s | grün, 23 von 23 Organen, 0,00 € |
| `43b8fad` (`REGRESSION-2.txt`) | **569** | 2 | **0** | 571 / 0 / 0 | 1657 s | grün, 23 von 23 Organen, 0,00 € |

- Übersprungen sind dieselben 2 wie in den Vorrunden (private Werk-/DB-Kopie nicht angegeben); 93 abgewählt
  (`integration`). `tests/test_vor_t4_04.py` am Nachtrag: 36 von 36 grün. `git status` vorher und nachher leer.
- **Die Regression an `1d9a5aa` war grün, obwohl das Nachspiel kaputt war:** Sie enthält kein Nachspiel. Der Nachtrag
  hält die Stelle mit einem Wächtertest fest (`test_nachspiel_vorbereiten_import_ueberschreibt_keine_variable`, mit
  Gegenprobe an der fehlerhaften Fassung); der eigentliche Beleg sind die Nachspiele N1–N3.
- Teilläufe vor den Commits: `TEILLAUF-1` 26/2 (zwei eigene Fehler, §13), `TEILLAUF-2` 6/6, `TEILLAUF-3` 347 grün,
  1 übersprungen, 3 rot von 351 (Runde-3-Tests mit dem alten Merkmal, §9), `TEILLAUF-4` 4/4, `TEILLAUF-5` 64/64.

## 9. Geänderte ältere Tests

| Datei | Änderung | Grund |
|---|---|---|
| `test_t3_verhaltensvergleich.py` | `haelt` je (Funktion, Art, Merkmal) statt (Funktion, Art) | Verfälschung je Merkmal (Review 03 Nr. 2) |
| `test_vor_t4_02.py` | Organ-Deckungsfall mit Merkmal `tab` statt `weissraum` | Entscheidung 2 |
| `test_vor_t4_03.py`, Gruppe B | eine richtige Behebung braucht einen Test je Weißraum-Formvariante (Tab, Zeilenumbruch, CRLF, NBSP); die Gegenprobe erwartet die einzelnen Merkmale; der Schlüssel der Verfälschungstabelle trägt das Merkmal | Entscheidung 2, Verfälschung je Merkmal |

Jede Stelle trägt eine Notiz im Test. Keine Zusicherung ist gelockert. Die Runde-3-Fälle verlangen jetzt mehr Tests, nicht
weniger.

## 10. Reviewdurchgang

Ein Reviewdurchgang (`REVIEW.md`; Proben unter `review-proben/`, 24 Kammerfälle und 2 Probenläufe gegen `43b8fad`). 18 Befunde: 2 hoch, 8 mittel, 8 niedrig. Nach der Regel „ein Review, keine Fix-Kaskade“ wurde danach kein Code gebaut; die Befunde sind als Spezifikationen R5-1 … R5-14 gefasst (`SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`). Philipp hat sie am 24.09. entschieden (Runde 5). Dieser Abschnitt, §11 und §14 sind in der Sitzung der Runde 5 nachgetragen.

| Nr | Schwere | Befund | Umgang |
|---|---|---|---|
| 1 | hoch | Ein Test hält ein Merkmal fest, ohne es zu unterscheiden. Gemessen durch `aegis.pruefen`. | Runde 5, Entscheidung 2 (Festhalten = fallende Zusicherung) |
| 2 | hoch | `__slots__` mit Vererbung: Der Zustand der Basisklassen-Slots wird nicht verglichen. | Runde 5, Entscheidung 1 (Vollständigkeitsprüfung; Gegenprobe) |
| 3 | mittel | Verschleierte Slot-Namen (`__slots__ = ('__stand',)`) sind unsichtbar. | Runde 5, Entscheidung 1 (Gegenprobe) |
| 4 | mittel | `csv.DictReader` wird weiter ersetzt. Der Lastabbruch stellt dann jeden Kandidaten des Laufs zurück. | Runde 5, Entscheidung 3 (Ausfall nur der betroffenen Funktion; nur echte Iteratoren ersetzen) |
| 5 | mittel | Teil-Enthaltungen werden gezählt, ändern aber weder das Urteil noch den Nenner. | Runde 5, Entscheidung 1 (Gegenprobe) |
| 6 | mittel | Die Kappe der Verfälschungsläufe führt zur Ablehnung statt zur Enthaltung. | Runde 5, Entscheidung 4 (zurückstellen mit Grund, gezählt; Messung in T4-Größe) |
| 7 | mittel | Die Torzeile „Schwächen“ ist gebaut, aber nichts ruft sie auf. | Runde 5, Entscheidung 5 (Register, Tor-4-Skript) |
| 8 | mittel | Fehlt die Stufe 2, misst der Lauf ohne Einspruch an Stufe 1. | Runde 5, Entscheidung 6 (Vorspann verweigert ohne Stufe 2) |
| 9 | mittel | Lastaufrufe haben immer das gewöhnliche Muster `[]`. | Runde 5, Entscheidung 7 (Formmerkmale der Lasteingabe) |
| 10 | mittel | `pathlib.Path` (relevant für T4): Rückgaben sind inhaltslos, Argumente gelten neu als veränderlich. | Runde 5, Entscheidung 1 (`os.fspath`) |
| 11 | niedrig | §2 sagt: „Jeder Befund … durch den Laufweg geprüft: `aegis.pruefen`“. Das gilt nicht für alle. | hier berichtigt: H3, H4, R4-5, R4-6, R4-13 sind Organ-Nachweise (`vv.pruefen`), nicht Laufweg; Laufweg sind H1, H2, E4 |
| 12 | niedrig | Weitere Aussagen gehen über ihren Beleg hinaus. | hier berichtigt: (a) die Sonde wurde geändert, gleich blieb nur ihre Last (Stufe 1); (b) Parität 19 von 19 Proben, 2 von 14 weiteren weichen ab (Runde 5); (c) Randwerte tragen Formmerkmale, wenn ihre Zeichen sie auslösen; (d) „quadratisch → linear“ ist gefolgert; (e) Median gepoolt 6,2 → 9,8 s |
| 13 | niedrig | „Zehnfache Eingabegröße je Bereich“ gilt für die Mengen, nicht für jeden Aufruf. | Runde 5, Entscheidung 6 (Stufe-2-Lasten bemessen) |
| 14 | niedrig | Die Eichproben des Vorspanns messen die Laufzeit an Stufe 1, die Toleranz stammt aus Stufe 2. | Runde 5, Entscheidung 8 |
| 15 | niedrig | In den gespeicherten Maßen mischen sich die Stufen. | Runde 5, Entscheidung 8 |
| 16 | niedrig | `eigene_tests` rechnet mit Funktionsnamen, `behoben` mit pytest-IDs. | Runde 5, Entscheidung 8 |
| 17 | niedrig | Koroutinen laufen beim Erzeugen in einer eigenen Schleife (gelesen, nicht gemessen). | Liste (nicht entschieden; SPEZIFIKATIONEN R5-14) |
| 18 | niedrig | Das Nachspiel hat keinen Durchlauf in der Regression. | Runde 5, Entscheidung 8 |

## 11. Sperren im Wortlaut

**1. Formatsperre (Auftragnehmer, 14:05)** — Beleg `sperre/FORMATSPERRE-1.txt` (wörtlich aus der Datei):

> Formatsperre in der Behebungsrunde 4 vor T4 — wörtlich, Einordnung, Handlung
> ===========================================================================
>
> Zeit: 2026-09-24, etwa 14:05. Werkzeug: terminal (Hermes).
>
> Befehl: ein nur lesender Sammelbefehl, der den Stand der Kette, des Teillaufs 4 und des Commit-Jobs anzeigen sollte
> (cat, tail, echo, pgrep -af, git log, grep). Die Ausführungsschicht hat ihn unverändert gespeichert; die Kopie liegt
> hier daneben als formatsperre-1-befehl.sh (bytegleich).
>
> Meldung (wörtlich):
> ------------------
> BLOCKED (hardline): command parser limit or malformed executable payload. This command is on the unconditional blocklist and cannot be executed via the agent — not even with --yolo, /yolo, approvals.mode=off, or cron approve mode. If you genuinely need to run it, run it yourself in a terminal outside the agent. RECOVERY: this block fires on oversized/unparseable inline command payloads (heredocs, giant one-liners), not on the operation itself. Your command was saved to /root/.hermes/cache/blocked-scripts/blocked-1790251359-f3cb81be.sh — review it, then run: terminal(command="bash /root/.hermes/cache/blocked-scripts/blocked-1790251359-f3cb81be.sh"). Do not retry inline.
>
> Einordnung und Handlung:
> -----------------------
> - Formatsperre, kein Sicherheitsurteil (Arbeitsregel Philipp 23.09.2026: „gespeichertes Skript unverändert ausführen,
>   wenn es sonst jede Prüfung bestanden hätte, sonst Linie 3“).
> - Geprüft: das gespeicherte Skript enthält nur lesende Befehle (cat, tail, echo, pgrep, git log, grep) auf Dateien des
>   Arbeitsordners und des Repositorys; nichts, was eine Freigabe oder die Sicherheitsprüfung auslösen würde.
> - Handlung: das gespeicherte Skript unverändert ausgeführt (`bash /root/.hermes/cache/blocked-scripts/blocked-1790251359-f3cb81be.sh`),
>   nicht umformuliert, nicht neu eingegeben. Ergebnis: Kette grün, Commit-Job läuft, Commit 1d9a5aa.
> - Ursache vermutlich: der Befehl enthielt `pgrep -af "job_commit_regression.sh"` und mehrere Dateinamen mit Punkten in
>   einer langen Zeile — nicht geprüft.

**2. Freigabeabfrage im Reviewdurchgang** — aus `REVIEW.md`, Abschnitt „Sperren“ (wörtlich):

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

## 12. Eigene Entscheidungen

1. **Stufe 2 ist dieselbe Last mit zehnfacher Menge, nicht zehnfachen Werten.** Die erste Fassung vergrößerte auch
   Werte (`skalar(i * 100)`) und riss den Wertebereich des Werks. Die Wiederholungszahlen blieben gleich. So steigt die
   Kammerzeit nur um den Faktor ≈ 1,6 (Median 6,3 s → 9,9 s), und alle 12 von 12 Kammerläufen bleiben unter 60 s.
2. **Merkmal = Formvariante; Randwerte tragen keins.** Entscheidung 2 nennt die Formvarianten. Leer, `None`, lang und
   nicht-ASCII sind Randwerte des Korpus, keine Formvarianten; ihre Abweichungen haben das gewöhnliche Muster. Folge: Ein
   Test, der die Funktion festhält, deckt sie ohne passenden Randwert. Die Merkmale `lang`, `leer`, `null_zahl` rechnet
   `klassen_von` weiter, sie gehen aber nicht ins Muster.
3. **Die Rauschmessung im Nachspiel misst an Stufe 2 neu.** Die Läufe 37/38 tragen nur Toleranzen der Stufe 1.
   Toleranzen einer anderen Last auf Stufe 2 anzuwenden, hätte die Grenzmaße verfälscht. Das Nachspiel verhält sich
   jetzt wie ein Lauf mit dem neuen Instrument.
4. **Kappe der Verfälschungsläufe: 24 je Kandidat.** Die Obergrenze ist gezählt: Ausgelassene Proben lassen ihre
   Abweichungen ungedeckt, nie gedeckt. Die Zahl ist eine Schätzung: 5 Formvarianten-Merkmale × wenige geänderte
   Funktionen. Gemessen wurde an K2868: 2 Verfälschungsläufe, 0 ausgelassen.
5. **Eigene Tests = neu oder im Quelltext geändert**, je Testfunktion. Einen unveränderten Test aus einer Datei, die der
   Kandidat erweitert, zählt die Regel nicht als eigenen Test; er gehört zur Vorgeneration.
6. **Nachtrag-Commit statt Änderung von `1d9a5aa`.** Die Geschichte bleibt unverändert; die Nachspiele an `1d9a5aa`
   bleiben als abgebrochene Belege im Ordner.
7. **Die Torzeile am T3-Werk ist eine Feststellung**, keine Neubewertung von T3. Entscheidung 5 gilt für künftige
   Testwerke. Die alte Zahl 4 von 5 stand nur auf dem versiegelten Gegenzeugen; das steht daneben.

## 13. Eigene Fehler

1. **Nachspiel in `1d9a5aa` kaputt:** Ein Import in `nachspiel.vorbereiten` überschrieb die Maßeichung des Falls. 7 von 7
   Nachspielen der Durchgänge D1–D3 brachen ohne Urteil ab. Die volle Regression war grün, weil sie kein Nachspiel enthält.
   Behoben im Nachtrag `43b8fad` mit einem Wächtertest samt Gegenprobe; die Gegenprobe lief dann an N1–N3.
2. **Teillauf vor dem Commit filterte die neue Testdatei heraus:** `-k "test_b_"` galt für beide Dateien.
   `test_vor_t4_04.py` lief darin nicht. Voll grün war sie zuvor in `TEILLAUF-3` und danach in beiden Regressionen.
3. **`TEILLAUF-1` hatte 2 rote Fälle, beide eigene Fehler.**
   - Die instabilen Funktionen standen als Name statt als `modul:funktion` im Vergleich; damit griff die Regel nie.
   - Der E4-Testfall brachte einen Test ohne Normbezug mit. Der kam gar nicht erst in den Testbestand, der Fall prüfte also
     nichts.
4. **Erste Fassung der Stufe 2 riss den Wertebereich** (§12 Nr. 1).
5. **Formatsperre** durch einen langen lesenden Sammelbefehl (§11). Das gespeicherte Skript lief unverändert.
6. **Die Kette zum Nachtrag musste gestoppt werden:** Der Nachtrag war schon angewandt, als der Nachspiel-Befund kam; er
   wurde samt Nachspiel-Behebung in einem neuen Job committet (`bau/KETTE-NACHTRAG-gestoppt.txt`).

## 14. Offen für Philipp

1. **Die Befunde des Reviews 04:** am 24.09. entschieden (Runde 5, Entscheidungen 1–8).
2. **`eingang` an Stufe 2 gesperrt in 3 von 6 Nachspielen:** entschieden (Runde 5, Entscheidung 6: die Stufe-2-Lasten
   werden wie Stufe 1 bemessen und geeicht, bis `eingang` nicht mehr sperrt).
3. **Normalvergleich je Schwäche:** entschieden (Runde 5, Entscheidung 5: für T4 gilt das Verhalten der Vorgeneration
   über den Verhaltensvergleich; eine verhaltensändernde Altlast braucht einen unabhängigen Test aus der
   Altlastenliste).
4. **K2868, führende Null (`~form#7`, 4 ungedeckte Abweichungen):** Die Werte stehen nicht im Beleg. Runde 5 schreibt
   sie ins Nachspiel. Danach ist zu klären, ob `007` eine gültige Zahl ist (die Normalversion nimmt sie an). Wenn ja,
   ist das ein weiterer Rückschritt von K2868.
