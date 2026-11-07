# Behebungsrunde 3 vor T4: nicht abgenommen — K2904/K3091 wieder nur 2 von 3 (Vergleichslast); die fünf Lücken der Python-Sonde sind für ihre Probenfälle geschlossen, aber das Review hat vier neue gemessen (Deckung: grobes Weißraum-Merkmal, Verfälschung je Funktion; Sonde: Iterator-Objekte, `__slots__`)

Stand 2026-09-24. **Biotop-Modellgeld 0,00 €** (`KASSE.md`). Kern-Commits **`d54bf2f`** (Runde 3, auf `6243377`) und
**`0aac612`** (Nachtrag: nur `tests/test_t3_python_annahmen.py`, §8). Stat `d54bf2f`: 21 files changed, 2329 insertions(+),
437 deletions(-) (`COMMIT-STAT.txt`, `KERN-COMMIT.patch.txt`; Nachtrag `COMMIT-2-STAT.txt`). Ein Reviewdurchgang (`REVIEW.md`, §10).

Auftrag (Philipp, 24.09., Entscheidungen Chat-Claude): (1) Deckung je Muster; (2) Gewinnschwelle der Nische „schnell“ in
beiden Richtungen nachmessen, nur im Rauschband um die Schwelle; (3) Methoden von Klassen beobachten, Instanzen aus den
Verträgen, Zustand von `self` vorher/nachher, Enthaltung nur für wirklich Unbeobachtbares, gezählt; (4) S1 nicht neu
versiegeln, jeder Gegenzeuge prüft zweierlei. Dazu die 13 Spezifikationen der Vorrunde (S-1 … S-13), jede mit Gegenprobe
durch den Laufweg, und die fünf Lücken der Python-Sonde je mit einem Fall, der vorher unentdeckt blieb oder Fehlalarm gab.

**Ergebnis:**
- **Gegenprobe K2904/K3091 wieder nur 2 von 3 — gemeldet, wie verlangt.** Die Nachmessung an der Gewinnschwelle ist
  gebaut und lief in 6 von 6 S2-Entscheidungen der Nachspiele wirklich. K3091 kippte trotzdem in Durchgang 2: erste
  Messung −12,7 %, Nachmessung −22,2 %, gepoolt −14,8 % gegen die Schwelle −15 % → abgelehnt. Über 9 gepaarte Messungen
  (Runde 2 und 3) liegt K3091 bei Median −17,0 % mit Spannweite −12,7 % … −22,2 %; 3 von 9 Einzelmessungen verfehlen die
  Schwelle. Nach Chat-Claudes Vorgabe liegt das an der Größe der Vergleichslast (§4).
- **Die fünf Lücken der Python-Sonde sind für ihre Probenfälle geschlossen, je mit einem Fall durch `aegis.pruefen` in der echten Kammer, am
  alten Code gemessen und am neuen** (§1): Generator, Nebenwirkung an der Eingabe und Funktion ohne Annotation kamen an
  `6243377` unentdeckt (0 zusätzliche Abweichungen); Mengenreihenfolge gab 36, `lru_cache` 16 weitere Fehlalarme. Am neuen
  Stand (`0aac612`): Generator 20, Nebenwirkung 36, Funktion ohne Annotation 32 Abweichungen, jeweils abgelehnt;
  Mengenreihenfolge und `lru_cache` 0 Abweichungen, überlebt. Zusicherungen der 17 Fälle: am neuen Code 17 von 17,
  am alten 1 von 17 (2 weitere brachen mit Fehler ab, weil es die Felder dort nicht gibt).
- **Methoden von Klassen** (Entscheidung 3) werden in Python beobachtet — Instanz aus dem Vertragstest, Zustand von
  `self` nach dem Aufruf, Methoden im Nenner. **In TypeScript nicht**: Klassen stehen dort weiter als gezählte Enthaltung
  „nicht eingewickelt (Klasse)“ (§2). T4 ist ein Python-Werk. Das Review fand auch in Python eine Lücke: Bei Klassen
  mit `__slots__` (auch `@dataclass(slots=True)`) wird der Zustand von `self` nicht verglichen (§10 Nr. 4).
- **Deckung je Muster** (Entscheidung 1) mit Verfälschungsprobe gebaut. **K2868 getrennt gemessen (2×2):** Die neue
  Deckungsregel allein lehnt ab (12 von 12 ungedeckt), der erweiterte Korpus allein nicht (40 von 40 nach alter Regel
  gedeckt). Mit beiden: abgelehnt, 40 von 40 ungedeckt, davon 20 mit Weißraum-Muster. Eine richtige Behebung mit einem
  Test je Muster kommt am Prüfwerk durch (§3). **Das Review hat zwei Lücken der Regel gemessen:** Ein Test mit doppeltem
  Leerzeichen deckt einen Rückschritt bei Tab und Zeilenumbruch — die K2868-Lage, der Kandidat überlebt —, und ein Test
  deckt mit einem Aufruf, den er nicht zusichert (§10 Nr. 1, 2). **Weitere Grenze:** Das Muster enthält auch Merkmale der nicht variierten
  Argumente — bei K2868 steht `null_zahl` in 40 von 40 Mustern (§3, Offen Nr. 2).
- **Gegenzeugen prüfen zweierlei** (Entscheidung 4, `kern/gegenzeugen.py`): Normalversion behoben, Ursprung nicht;
  K3044, beide Endstände und K2868 nicht behoben (Schwäche weg, Verhalten verändert). S1 ist nicht neu versiegelt,
  der Siegelordner unverändert (§5).
- **Bestätigungsmessung lief erstmals echt auf dem Laufweg** (echte Rissprobe, §7); in den Nachspielen trat weiter kein
  Laufzeitriss auf (0 von 10 Entscheidungen).
- **Volle Regression:** an `d54bf2f` 532 bestanden, 2 übersprungen, **1 fehlgeschlagen** (Sprachweichen-Register, §8);
  am Nachtrag `0aac612`: **533 bestanden, 2 übersprungen, 0 fehlgeschlagen**, Verdrahtungstest grün.
- **Verdichtung** läuft seit dem Gateway-Neustart (§0).
- **Review (ein Durchgang): 18 Befunde, 4 hoch, 5 mittel, 9 niedrig** (§10). Bestätigt: alle nachgerechneten Zahlen des
  Berichts; die alten Proben des Gutachtens 02 verhalten sich an HEAD in 14 von 14 Fallläufen wie spezifiziert. Die vier
  hohen Befunde sind in der Kammer gemessen; Code baue ich nach dem Review nicht mehr, sie stehen als Spezifikationen in
  `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`.
- **Zwei Sicherheitssperren bei mir** (§11, Wortlaut aus den gespeicherten Belegen): beide Male angehalten, nichts
  umgangen. Philipp gab für genau diesen Fall frei (nicht als Dauerregel); danach in einzelnen Schritten ausgeführt.
- **Zwischenbericht-Wächter:** zwei Zwischenberichte in dieser Runde (Werkzeugrunde 113 und 141 von 150), beide HTTPS
  bytegleich 5 von 5; kein Auslöser an Kontextfüllung oder Verdichtung (§11).

## 0. Verdichtung

Seit dem Gateway-Neustart um 02:14:04 zwei erfolgreiche Verdichtungen dieser Sitzung: 02:14:47–02:15:47 (532 → 163
Nachrichten) und 05:08:28–05:10:02 (375 → 215 Nachrichten, `anthropic (claude-opus-5-5)`, `logs/agent.log`). Die letzte
gescheiterte Verdichtung („401 … OAuth access token has been revoked“) war um 02:09:19, vor dem Neustart; danach keine.

## 1. Die fünf Lücken der Python-Sonde — je ein Fall, vorher und nachher gemessen

**Prüfwerk** `probewerk` (in `tests/test_vor_t4_03.py`): Funktionen `zahlen` (Generator), `sortiere` (an Ort und Stelle),
`verbinde` (ohne Annotation, nicht von der Last gerufen), `woerter` (`list(set(…))`), `quadrat`, `normieren`, Klasse
`Konto` (Methode `buchen`, Eigenschaft `doppelt`), Vertragstest `tests/vertraege/test_vertrag_werk.py`. Jeder Fall läuft
durch `aegis.pruefen` in der echten Kammer `biotop-kammer:1` (Messgerät, Bandit, Vulture, pytest, Sonde, Aufzeichner);
gestellt sind nur das Modell (KEIN ANGRIFF) und die Laufzeitmessung (Kandidat 20 % schneller, damit er den Vergleich
erreicht). Die Änderungen sind so gebaut, dass kein Werkstest sie sieht (nur die Last bzw. der Korpus).

**Vorher:** dieselben Testfunktionen am Code von `6243377` (`git archive`, `proben/vorher_6243377.py`,
`VORHER-6243377.txt/.json`). **Nachher:** am Commit (Regression) und dieselbe Auswertung am Code von HEAD
(`proben/nachher_head.py`, `NACHHER-HEAD.txt/.json`).

An `6243377` gab jeder Fall am Prüfwerk **36 Abweichungen an `woerter`** — Fehlalarme der Mengenreihenfolge (Lücke 4),
auch im verhaltensgleichen Fall. Ob eine Änderung gesehen wurde, zeigt deshalb der Zuwachs über diese 36 („+0“ = die
Gesamtzahl war dieselbe wie im verhaltensgleichen Fall). Iteratoren werden bis zum 50. Element verglichen (Kappe N = 50);
darüber hinaus ist eine Änderung unsichtbar (Review Nr. 16). Zusicherungen der 17 Testfälle (Gruppen A, B, D): am alten Code
1 von 17 (die Gegenprobe „falscher Cache wird abgelehnt“), 2 Abbrüche, weil das Urteil dort Felder nicht hat
(`instabil`, `ungedeckt_aufschluesselung`); am neuen Code 17 von 17 (`VORHER-6243377.txt`, `NACHHER-HEAD.txt`).

| Lücke | Fall | an `6243377` | an `0aac612` | Gegenprobe (an `0aac612`) |
|---|---|---|---|---|
| 1 Generator | `zahlen` liefert ab n = 5 andere Elemente | 36 Abweichungen = +0: **unentdeckt** | **abgelehnt**, 20 Abweichungen (u. a. `zahlen#0`), 8 von 8 beobachtet | gleiche Ausgabe anders geschrieben → überlebt, 0 Abweichungen |
| 2 Nebenwirkung an der Eingabe | `sortiere` ab 4 Elementen absteigend | +0: **unentdeckt** | **abgelehnt**, 36 Abweichungen am Argumentzustand (`sortiere#0>args` …) | `xs.sort(key=…)` → überlebt, 0 |
| 3 nur Fehleraufrufe | `verbinde` (ohne Annotation) ändert `.upper()` | +0: **unentdeckt** | **abgelehnt**, 32 Abweichungen an `verbinde` (tastender Korpus) | am Organ: Funktion mit nur Fehlerbeobachtungen zählt nicht als beobachtet („1 von 2“, Enthaltung „nur Fehler“) |
| 4 Hash-Reihenfolge | verhaltensgleicher Kandidat (`x ** 2` statt `x * x`) | **36 Fehlalarme, abgelehnt** | **überlebt**, 0 Abweichungen (Hashsaat 0) | am Organ: schwankende Vorgeneration → Enthaltung `instabil`, keine Abweichung |
| 5 `lru_cache` | `@functools.lru_cache` auf `quadrat` | 52 = 36 + **16 Fehlalarme, abgelehnt** | **überlebt**, 0 Abweichungen, `quadrat` eingewickelt | Zwischenspeicher an `id(xs)` → abgelehnt „Verhaltensvergleich“ |

Umgesetzt (`kern/py/verhalten.py`): (1) Iteratoren und Generatoren werden bis zu einer Kappe ausgelesen und elementweise
verglichen, der Aufrufer bekommt die Elemente zurück; (2) nach jedem Aufruf wird der Zustand der veränderlichen Argumente
als eigene Beobachtung `…>args` festgehalten; (3) als beobachtet zählt eine Funktion nur mit mindestens einem fehlerfreien,
inhaltlichen Ergebnis auf beiden Seiten; der Korpus tastet Parameter ohne Annotation mit `'a b'`, 1, 0, `[]`, `None`;
(4) `PYTHONHASHSEED=0` für Sonde und Aufzeichner, und die Vorgeneration wird zweimal beobachtet — was dabei schwankt, ist
Enthaltung; (5) aufrufbare Objekte mit `__wrapped__` werden eingewickelt (die Hülle ruft das dekorierte Objekt, der
Zwischenspeicher bleibt wirksam).

**Grenzen nach dem Review** (gemessen vom Prüfer an HEAD, `REVIEW.md`; seine Proben und Ausgaben liegen im Ordner als
`review_*`):
- Nr. 3: Die Behebung von Lücke 1 ersetzt **jedes** zurückgegebene Iterator-Objekt durch einen Generator. Greift die Last
  auf ein Attribut des echten Objekts zu, bricht sie unter der Sonde auf beiden Seiten still ab; eine spätere Änderung
  bleibt unsichtbar (0 Abweichungen statt 6, tragfähig). Eine neue stille Stelle.
- Nr. 4: Bei `__slots__`-Klassen fehlt der Vergleich des Zustands nach dem Aufruf (0 statt 28 Abweichungen) — Lücke 2 ist
  für diese Klassen offen.
- Nr. 7: Koroutinen bleiben Enthaltung „unvergleichbar (asynchron)“, das Urteil trotzdem tragfähig.
Die Aussage „die fünf Lücken sind geschlossen“ gilt deshalb nur für ihre Probenfälle, nicht für die Lückenklassen.

## 2. Methoden von Klassen (Entscheidung 3)

- **Python:** öffentliche Klassen der geänderten Module; Methoden, Klassen- und statische Methoden, Eigenschaften werden
  eingewickelt und gehen in den Nenner ein. **Instanzen aus den Verträgen:** Die Sonde führt auf beiden Seiten an derselben
  Stelle die Vertragstests des Werks aus (`tests/vertraege/test_*.py`) und zeichnet den ersten Konstruktoraufruf je Klasse
  als Rezept auf; die Vorgeneration liefert das Rezept, der Kandidat baut daraus dieselbe Instanz. Rückfall: Rezept aus dem
  Zustand eines Lastobjekts, dann die Signatur von `__init__`. Die Herkunft steht im Urteil (`instanzen`: `vertrag`,
  `last_zustand`, …). **Zustand von `self`:** `self` ist das erste Argument; sein Zustand nach dem Aufruf ist Teil von `>args`.
  Keine Instanz herstellbar → Enthaltung „keine Instanz (…)“, gezählt.
- **Grenzen nach dem Review:** `__slots__`-Klassen ohne Zustandsvergleich (Nr. 4); eine Klasse ohne Vertrag mit
  unannotiertem Konstruktor bekommt aus der Signatur eine unbrauchbare Instanz — jede Methode wirft, die Enthaltung heißt
  „nur Fehler“, eine geänderte Methode bleibt still (Nr. 6: 0 statt 4 Abweichungen). Das ist keine „wirklich
  unbeobachtbare“ Stelle im Sinn der Entscheidung.
- **Laufweg** (`test_d_*`, an `0aac612`): Methode `buchen` nur bei `betrag == 2` geändert (Werkstest und Vertrag sehen es
  nicht) → abgelehnt, 80 Abweichungen an `Konto.buchen`, Instanz aus dem Vertrag (`instanzen`: `vertrag`); Gegenprobe gleich
  umgeschrieben → überlebt, 0 Abweichungen, 8 von 8 beobachtet (6 Funktionen + `buchen` + `doppelt`); Rückgabe gleich, nur
  `self` danach anders → abgelehnt, 56 Abweichungen an `Konto.buchen…>args`. An `6243377`: +0 Abweichungen in allen drei
  Fällen, Nenner 6 von 6 (keine Methode im Nenner).
- **TypeScript: nicht gebaut.** `einwickeln.mjs` führt Klassen als „nicht eingewickelt (Klasse)“ — gezählte Enthaltung im
  Nenner, nicht beobachtet. Das ist keine „wirklich unbeobachtbare“ Stelle; Offen Nr. 3.

## 3. Deckung je Muster (Entscheidung 1)

**Regel** (`verhaltensvergleich.deckung`): Muster einer Beobachtung = die Merkmalsklassen ihrer Eingabe (`weissraum`,
`randweissraum`, `gross`, `klein`, `zahlform`, `lang`, `leer`, `nichtascii`, `null`, `null_zahl`, `negativ`, `zahltyp`,
`behaelter`, `schluesselfolge`, …; leer = gewöhnliche Eingabe), berechnet über **alle** vereinheitlichten Argumente
(`bind`/`apply_defaults`) — auf beiden Seiten dieselbe Rechnung (Sonde und Aufzeichner der deckenden Tests). Eine
Abweichung von `f` ist gedeckt, wenn
1. ein Test, der an der Vorgeneration fällt und am Kandidaten besteht, `f` am Kandidaten aufgezeichnet ruft,
2. **jedes Merkmal** des Musters von mindestens einem solchen Test getroffen wird (eigene Lesart, §12 Nr. 1), und
3. der Test **fällt, wenn der Aufzeichner das Ergebnis von `f` verfälscht** (bzw. den Argumentzustand bei `>args`) —
   ein Kammerlauf je betroffener Funktion und Art.
Nicht deckbar: Abweichungen, deren Ergebnis am Kandidaten an Referenz oder verborgenem Zustand hängt (Kopienprobe).
Ein deckender Test, der ein geändertes Modul lädt und im Aufzeichnerlauf keinen Aufruf zeigt, ist Messgerätausfall.

**Laufweg am Prüfwerk** (`test_b_*`, Soll-Tests im Werk, an der Vorgeneration rot, Kandidat ändert `normieren`):
| Fall | an HEAD | an `6243377` |
|---|---|---|
| richtige Behebung, ein Test je Muster (8 Tests) | **überlebt**, 52 von 52 Abweichungen gedeckt (Kernmaß −10 → −2) | abgelehnt: 72 von 72 ungedeckt, 0 gedeckt (8 Tests, 8 aufgezeichnete Aufrufe) |
| dieselbe Behebung ohne Tests für Weißraum | **abgelehnt**, 46 von 52 ungedeckt, alle mit `weissraum` im Muster | abgelehnt, 72 von 72 ungedeckt |
| Test ruft `normieren` nur, ohne festzuhalten | **deckt nicht**: 52 von 58 ungedeckt, keine `normieren`-Abweichung gedeckt | deckte: 24 von 78 gedeckt, darunter `normieren#0` durch diesen Test |
| Gegenprobe: derselbe Test hält fest | **deckt**: 2 von 58 ungedeckt (`normieren~form#8` samt `@alias`) | — |

**K2868, getrennt gemessen** (Nachspiel am Commit `d54bf2f`, Durchgang 1, `nachspiel/d1/k2868*.json`):
| Korpus | Deckungsregel | Abweichungen | ungedeckt | Urteil |
|---|---|---|---|---|
| alt | je Funktion (wie `330b4ec`) | 12 | 0 | überlebt |
| erweitert | je Funktion | 40 | 0 | überlebt |
| alt | **je Muster** | 12 | **12** | **abgelehnt** |
| erweitert | **je Muster** | 40 | **40** | **abgelehnt** |

- Die Ablehnung bewirkt die **Deckungsregel**, nicht der Korpus. Der Korpus bringt 28 Abweichungen hinzu (Formvarianten).
- Aufschlüsselung der 40: 20 mit `weissraum` (16 `weissraum`, 4 `randweissraum+weissraum`), 8 weitere Formvarianten
  (`gross`, `zahlform`), 12 Randfälle `~rand#2/#4/#5` (beabsichtigte Behebung, `'a'` → SyntaxError). „K2868 scheitert am
  ungedeckten Weißraum-Muster“: ja, aber nicht nur daran.
- **`null_zahl` steht in 40 von 40 Mustern** — es stammt aus einem Argument, das in allen 40 abweichenden Aufrufen 0 ist,
  nicht aus der variierten Stelle. Für kein Muster wurde jedes Merkmal von einem der drei deckenden Tests getroffen; die
  Verfälschungsprobe lief deshalb 0-mal. Welches Merkmal jeweils fehlte, steht nicht im Beleg (die Klassen der
  aufgezeichneten Aufrufe werden nicht gespeichert). Nach der Regel müsste ein deckender Test für ein Weißraum-Muster
  von K2868 auch dieses Argument mit 0 rufen. Gezeigt ist „richtige Behebung kommt durch“ nur an einer **einstelligen**
  Funktion (`normieren`). Offen Nr. 2.

## 4. Gewinnschwelle der Nische „schnell“ in beiden Richtungen (Entscheidung 2)

**Regel** (`messgeraet.gewinn_band`, `gewinn_bestaetigen`, Einbau in `aegis.pruefen` und `lauf._generation_koerper`):
Entscheidet der Laufzeitgewinn allein (Kernmaß gleich), wird nachgemessen, wenn die erste gepaarte Messung eines Bereichs
im Band [0,85 ÷ t; 0,85 · t] liegt, t = gemessene Rauschtoleranz des Bereichs (Rückfall 1,2). Klar darunter (Gewinn) oder
alle klar darüber (kein Gewinn): keine Nachmessung. Beide einig: bestätigt. Uneinig: der Median über beide Messungen
(2 × 5 Werte je Seite) entscheidet („gepoolt“, eigene Entscheidung, §12 Nr. 2). Nachmessung ungültig: zurückgestellt.
- Laufweg mit gestellter Messung (`test_c_*`, 6 Fälle, beide Richtungen, im Band und klar außerhalb): grün.
- Rote Spezifikation der Vorrunde (`spez/test_spez_gewinnschwelle_nachmessung.py`, unverändert kopiert): an `6243377`
  2 von 4 rot, am Arbeitsbaum vor dem Commit **4 von 4 grün** (`SPEZ-GEWINNSCHWELLE-am-arbeitsbaum.txt`).

**Nachspiele K2904/K3091 am Commit `d54bf2f`** (`NACHSPIEL-D1..3.txt`, `nachspiel/d1..d3/`; `planung` = Quote
Kandidat/Vorgeneration, Median aus 5 je Seite; Band je Bereich aus der Rauschtoleranz des Laufs):
| Fall | D | erste | Nachmessung | Ergebnis | Urteil |
|---|---|---|---|---|---|
| K2904 | 1 | 0,838 | 0,742 | bestätigt | überlebt |
| K2904 | 2 | 0,820 | 0,803 | bestätigt | überlebt |
| K2904 | 3 | 0,819 | 0,792 | bestätigt | überlebt |
| K3091 | 1 | 0,837 | 0,818 | bestätigt | überlebt |
| K3091 | 2 | 0,873 | 0,778 | gepoolt **0,852** | **abgelehnt** |
| K3091 | 3 | 0,789 | 0,853 | gepoolt 0,803 | überlebt |

**Gleich entschieden in 2 von 3 Durchgängen — Gegenprobe gescheitert; gemeldet wie verlangt.**
- 6 von 6 S2-Entscheidungen wurden nachgemessen (alle erste Messungen lagen im Band; K2904-Band `planung` 0,725 … 0,996,
  K3091 0,699 … 1,034). 4 bestätigt, 2 uneinig → gepoolt.
- K3091 über alle 9 gepaarten Messungen (Runde 2: 3, Runde 3: 6): Median 0,830 (−17,0 %), Mittel 0,825, Standardabweichung
  0,035, Spannweite 0,778 … 0,873; **3 von 9 über 0,85.** K2904: Median 0,815, Standardabweichung 0,028, 0 von 9 über 0,85.
- K3091 D2, `planung` gepoolt (10 je Seite): Vorgeneration Median 9,61 ms, Standardabweichung der Einzelwerte 0,64 ms
  (6,6 %); Kandidat 8,19 ms, 0,62 ms (7,6 %).
- Die Standardabweichung der Quote über die 9 gepaarten Messungen (0,035, also 3,5 Punkte) ist größer als der Abstand des
  typischen Gewinns zur Schwelle (2 Punkte). Rechnung, nicht gemessen: Das Poolen zweier Messungen senkt sie um etwa √2 auf
  ≈ 2,5 Punkte — immer noch mehr als der Abstand.
- Einordnung nach Chat-Claude: Es liegt an der **Größe der Vergleichslast** (≈ 9,5 ms je Messung für `planung`). Nicht
  gebaut: größere Last — Offen Nr. 1.

## 5. Gegenzeugen prüfen zweierlei (Entscheidung 4)

`kern/gegenzeugen.py`: `doppelurteil(schwaeche, normal)` — behoben nur, wenn (a) die Schwäche weg ist UND (b) das
Verhalten gegen die Normalversion unverändert ist, beides gemessen und nicht leer; eine gemessene gescheiterte Prüfung →
nicht behoben; fehlt eine → nicht beurteilbar, nie „behoben“. `s1_aus_messung` liest dieselben Größen wie das Kriterium der
Vorrunde, je Teil mit eigenem Bezug. S1 ist **nicht** neu versiegelt; das versiegelte Skript ist unverändert.

Am Commit (`GEGENZEUGEN-DOPPELT-am-commit.txt`, Kammer `biotop-kammer:ts1`, Harness `s1_harness.mjs` der Vorrunde,
Siegelordner sha256 vorher = nachher):
| Stand | (a) Schwäche | (b) gegen Normalversion (Leerzeichen / Zeilenumbruch / Tab) | behoben | Herkunft |
|---|---|---|---|---|
| Normalversion (Gegenprobe) | weg | 0 von 120.008 / 0 von 12.206 / 0 von 12.206 | **ja** | gemessen |
| Ursprung (Gegenprobe) | **da** | 86 von 120.008 / 0 / 0 | nein | gemessen |
| K3044 | weg | 0 / **12.206 von 12.206** / 0 | nein | Messung Runde 2 |
| Endstand Lauf 38 | weg | 0 / 12.206 / 0 | nein | Messung Runde 2 |
| Endstand Lauf 37 | weg | 0 / 12.206 / 12.206 | nein | Messung Runde 2 |
| K2868 | weg | 0 / 12.206 / 12.206 | nein | Messung Runde 2 |

Laufweg: keiner — Gegenzeugen laufen wie in T3 außerhalb des Laufs (private Bauverifikation). Nicht erzwungen: Kein
Organ ruft die Doppelprüfung bei der Aufnahme eines künftigen Testwerks auf (Offen Nr. 4).

## 6. Die 13 Spezifikationen

| Nr | Inhalt | Stand | Gegenprobe | Weg |
|---|---|---|---|---|
| S-1 | Generator-Ausgaben vergleichen | gebaut | Lücke 1 | Laufweg (Kammer) |
| S-2 | Argumentzustand nach dem Aufruf | gebaut (Py, TS) | Lücke 2 | Laufweg Py; TS nur Rauchprobe (`bau/rauchprobe_ts.py`) |
| S-3 | beobachtet nur inhaltlich; Klassen/Wurzelmodule in y; `nicht_eingewickelt` im Urteil | gebaut | Lücke 3; Wurzelmodul | Laufweg (Lücke 3), Organ (Zählung, Wurzelmodul) |
| S-4 | `PYTHONHASHSEED`; Vorgeneration zweimal | gebaut | Lücke 4; `instabil` | Laufweg, Organ |
| S-5 | `__wrapped__` einwickeln | gebaut | Lücke 5; falscher Cache | Laufweg |
| S-6 | `bind`/`apply_defaults`; TS `export const`; Verfälschungsprobe | gebaut | Nebenbei-Test deckt nicht / hält fest deckt | Laufweg Py; TS `export const` nur Rauchprobe |
| S-7 | K2868 getrennt | gemessen (2×2) | §3 | Nachspiel |
| S-8 | Formvarianten auch aus Randwerten mit Leerzeichen; „ohne Formvariante x von y“ | gebaut | K2868: 25 Formvarianten, ohne Formvariante 8 von 10 (reine Zahlfunktionen) | Nachspiel |
| S-9 | Gewinnschwelle beidseitig; `laufzeitrisse` als Liste; Nachmessung in Beleg und Nachspiel | gebaut | `test_c_*`, Spez 4 von 4, `test_s9_*` | Laufweg gestellt; Nachspiel echt (6 von 6); Verdrahtungsbeleg: Felder in 16 von 16 Urteilen, Nachmessung in 0 von 16 |
| S-10 | Vertragsprobe mit Last, die A ruft | gebaut; `REF_PAAR`-Umgehung zurückgenommen | Last erreicht alle Funktionen → benannter Prüffehler | Organ mit echter Kammer (`eichproben._einzelprobe`), nicht Laufweg (berichtigt nach Review Nr. 10); Gegenprobe am Organ |
| S-11 | `test_vorspann`: Anforderungsliste nicht leer | gebaut | — (Zusicherung selbst) | Unit |
| S-12 | Zeitlimit 2× am Kandidaten = Befund; blinder Aufzeichner = Ausfall | gebaut | einmaliges Zeitlimit → wiederholt; nicht blind → lehnt ab | **nur Organ** (Sonde gestellt) |
| S-13 | Entscheidungen | von Chat-Claude getroffen | — | — |

## 7. Echte Rissprobe (Bestätigungsmessung auf dem Laufweg)

`proben/rissprobe_echt.py` am Commit `d54bf2f` (sauber), Python-Prüfwerk, `aegis.pruefen`, echte Kammer, echte Laufzeit;
gestellt nur das Modell:
- Kandidat entfernt toten Code und verlangsamt `quadrat` → erste gepaarte Messung `werk` 765,1 ms gegen 0,094 ms, Riss;
  **Nachmessung lief wirklich** (2 gepaarte Messungen), bestätigt 772,2 ms gegen 0,085 ms → abgelehnt „Grenzmaß gerissen“.
- Gegenprobe ohne Verlangsamung → kein Riss, 1 gepaarte Messung, überlebt (Kernmaß −3 → −2).
- Grenze: ein grober Riss (Faktor ≈ 8.200 in der ersten, ≈ 9.100 in der Nachmessung). Das Verhalten nahe der Grenze ist nur mit gestellter Messung belegt.

## 8. Volle Regression und Verdrahtung

**An `d54bf2f`** (`REGRESSION.txt`, JUnit `REGRESSION.junit.xml.txt`): **532 bestanden, 2 übersprungen, 1 fehlgeschlagen**,
93 abgewählt (`integration`), 1507 s; JUnit 535 Fälle, 1 Fehlschlag, 0 Fehler. `tests/test_vor_t4_03.py`: 38 von 38 grün.
- Rot: `test_t3_python_annahmen.py::test_keine_ungeschuetzte_python_annahme_im_kern` — „verhalten.py:803
  vertraege_ausfuehren() ['pytest-auswertung'] … verhalten.py:660 params() ['python-ast'] — ungeschützt gerufen“. Beide
  neuen Funktionen laufen nur in der Kammer eines Python-Werks hinter den Weichen in `verhaltensvergleich.py`; es fehlten
  die Einträge im Register `GEPRUEFT`. Die Teilläufe vor dem Commit hatten diese Datei nicht enthalten (eigener Fehler, §13).
- **Nachtrag `0aac612`:** zwei Einträge ergänzt, die veralteten Zeilennachweise der beiden vorhandenen berichtigt (Review 02
  Nr. 18); `biotop/` unverändert gegenüber `d54bf2f`. Neuer Commit statt Änderung — keine umgeschriebene Geschichte.
- **Volle Regression am Nachtrag `0aac612`** (`REGRESSION-2.txt`, JUnit `REGRESSION-2.junit.xml.txt`): **533 bestanden,
  2 übersprungen, 0 fehlgeschlagen**, 93 abgewählt, 1491 s; JUnit 535 Fälle, 0 Fehlschläge, 0 Fehler. Übersprungen dieselben 2
  wie an `6243377` (private Werk-/DB-Kopie nicht angegeben). `git status` vorher und nachher leer, 0 fremde Container.
  Verdrahtungstest grün: 23 von 23 Organen, 0,00 €, 16 Aegis-Urteile mit Nachmessungsfeldern, in 0 davon eine Nachmessung
  (`VERDRAHTUNG-BELEG-REGRESSION-2.json`).
- **Verdrahtungstest** an `d54bf2f` grün: 23 von 23 Organen gerufen, 0,00 € Modellkosten; neu im Beleg: Nachmessungsfelder
  je Aegis-Urteil — 16 Urteile, in 0 davon eine Nachmessung (kein Riss, kein Gewinn im Band).

## 9. Geänderte ältere Tests

| Datei | Änderung | Grund |
|---|---|---|
| `test_t3_verhaltensvergleich.py`, `test_vor_t4.py`, `test_vor_t4_02.py` | gestellte Kammer antwortet je Stand statt je Aufruf (`je_stand`, 15 Stellen) | die Vorgeneration wird jetzt zweimal beobachtet (S-4); eine Folge je Aufruf hätte die zweite Beobachtung der Vorgeneration mit dem Kandidaten beantwortet |
| dito | Deckungstests auf die Muster-Regel (Klassen + `haelt`) umgestellt; die Gegenprobe „ohne passenden Test leer“ hat jetzt ein gesetztes Muster und eine Kontrolle | Entscheidung 1; die alte Gegenprobe lief ohne Muster und prüfte nichts |
| `test_vor_t4_02.py` | Kammerprobe des Aufzeichners: deckt Lastaufruf und `f('a')`, nicht die Weißraum-Formen | Entscheidung 1 |
| `test_eichproben.py` | `REF_PAAR` ruft `bericht` wieder (Runde-2-Umgehung zurückgenommen); zweite Funktion `kurzbericht` mit Test; zwei S-10-Tests | S-10, Review 02 Nr. 15 |
| `test_vorspann.py` | Zusicherung: Anforderungsliste im Fall `nur_gesperrtes_rauschen` nicht leer | S-11 |
| `test_verdrahtung.py` | Nachmessungsfelder im Beleg und als Zusicherung | S-9 |
| `test_t3_python_annahmen.py` (Nachtrag) | 2 Register-Einträge, 2 Zeilennachweise berichtigt | §8 |

Dazu im Organ `eichproben.py`: Der private Ausgangsdefekt der Nebenwirkungsprobe liefert statt `None` einen typtreuen
Nullwert (0, 0.0, '' … nach Annotation). Mit `None` brach jede Referenzlast ab, die ein Ergebnis von A weiterverwendet —
genau der Messausfall, den `REF_PAAR` in Runde 2 umging. Die Gegenproben der Eichproben bleiben rot, wo sie rot sein müssen
(`test_vier_paare…`: 4 von 4 Gegenproben „nicht bestanden“).

## 10. Reviewdurchgang

Ein Durchgang (`REVIEW.md`, Auftrag `REVIEW-AUFTRAG.md`), 07:39–08:36, Kammerproben erst nach dem Ende des
Nachtrag-Jobs (ab 08:11). Ergebnis: **18 Befunde, 4 hoch, 5 mittel, 9 niedrig**; keine Sperre beim Prüfer; Schreibort nur
`REVIEW.md` und `/tmp/review-vor-t4-03/`; `git status` vorher und nachher leer.
- Bestätigt: alle nachgerechneten Zahlen (Regressionen an `d54bf2f` und `0aac612`, Vorher/Nachher 17 Fälle, K2868 2×2,
  Gewinn-Tabelle und K3091-Statistik, Rissprobe, Gegenzeugen, Kasse); „2 von 3“ richtig gemeldet; keine verdeckte
  Regression in den geänderten älteren Tests; die Proben des Gutachtens 02 an HEAD: 14 von 14 wie spezifiziert.
- Bei jedem hohen Befund habe ich in den Ausgaben des Prüfers Urteil und Abweichungszahl von Probe und Kontrolle
  nachgesehen, bevor ich ihn übernahm: x1 überlebt / x1k abgelehnt, x2 überlebt / x2k abgelehnt (`DECKPROBE.json`);
  p18 tragfähig mit 0 / p18b 6 Abweichungen (`SONDENPROBE-3.json`); p19 und p20 tragfähig mit 0 / p19b 28
  (`SONDENPROBE-4.json`). Feinere Zahlen (etwa „14 von 14 gedeckt“) sind die des Prüfers.
- Seine Proben und Ausgaben liegen im Ordner als `review_*` (17 von 17 Dateien kopiert, alle bytegleich mit den
  Originalen unter `/tmp/review-vor-t4-03/`; nicht kopiert: `diffs/` und die Probenwerke `werke*/`, die die Skripte selbst
  erzeugen).
- Nach „ein Review, keine Fix-Kaskade“ baue ich keinen Code mehr: Code-Befunde → `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`
  (R4-1 … R4-14); Aussagen-Befunde → hier berichtigt.

| Nr | Schwere | Befund (kurz) | Umgang |
|---|---|---|---|
| 1 | hoch | Ein Merkmal `weissraum` für Tab, Zeilenumbruch, doppeltes Leerzeichen: ein Test mit doppeltem Leerzeichen deckt eine Tab-/LF-Regression, der Kandidat überlebt (Kontrolle ohne den Test: abgelehnt) | übernommen (x1/x1k); Ergebnis und §3 ergänzt; R4-1 |
| 2 | hoch | Verfälschung je Funktion statt je Aufruf: ein nicht zugesicherter Tab-Aufruf neben einem zugesicherten `normieren("a b")` deckt 6 von 6 | übernommen (x2/x2k); R4-2 |
| 3 | hoch | Iterator-Objekte werden durch Generatoren ersetzt: Last bricht still ab, Änderung unsichtbar | übernommen (p18/p18b); §1; R4-3 |
| 4 | hoch | `__slots__` / `dataclass(slots=True)`: Zustand von `self` nicht verglichen (0 statt 28) | übernommen (p19/p20); §1, §2; R4-4 |
| 5 | mittel | „die fünf Lücken sind geschlossen“ stärker als der Beleg | berichtigt: Titel, Ergebnis, §1 („für ihre Probenfälle“) |
| 6 | mittel | Klasse ohne Vertrag, unannotierter Konstruktor: unbrauchbare Instanz, geänderte Methode still | übernommen (p16/p16b); §2; R4-5 |
| 7 | mittel | Koroutinen: Enthaltung, Urteil trotzdem tragfähig | übernommen (p13); §1; R4-6 |
| 8 | mittel | K2868: woran die Deckung scheiterte (Weißraum oder `null_zahl`), ist nicht belegt | übernommen; §3 nennt die Grenze bereits; R4-7 |
| 9 | mittel | Lücken gegen den Auftrag: TS-Methoden, Doppelprüfung nicht erzwungen, Gewinn-Nachmessung der Generalprobe nie ausgeführt, 2 von 3 | bestätigt, offen (§14) |
| 10 | niedrig | S-10 ist Organ-, nicht Laufweg-Nachweis | §6 berichtigt |
| 11 | niedrig | Annahmegrund nennt einen Gewinn, den die Nachmessung nicht bestätigt (K2904 D1 `bericht`) | übernommen; R4-8 |
| 12 | niedrig | Zweig „Gewinn-Nachmessung ungültig“ ungetestet | übernommen; R4-9 |
| 13 | niedrig | veraltete Kommentare in `aegis.py` (Gewinn uneinig; Deckung „dieselbe Eingabe“) | übernommen; R4-10 |
| 14 | niedrig | Verdrahtungszusicherung prüft nur, dass die Schlüssel da sind | übernommen; R4-11 |
| 15 | niedrig | Verfälschungsproben ohne Obergrenze und ohne Zählung im Urteil | übernommen; R4-12 |
| 16 | niedrig | Iterator-Kappe 50 nicht genannt, Rest unsichtbar | §1 nennt N = 50; R4-13 |
| 17 | niedrig | Formart nur in der Sonde, nicht im Aufzeichner; instabile Funktionen zählen als beobachtet | übernommen (gelesen, nicht gemessen); R4-14 |
| 18 | niedrig | `TEILLAUF-1.txt` unvollständig; §13 nannte den falschen Teillauf | §13 berichtigt |

**Vom Prüfer nicht geprüft, von mir gelesen (nicht gemessen):** Vom Kandidaten mitgebrachte Tests gehen in den
Testbestand (`aegis.py:873`), die Basismessung läuft mit ihm (`:985`), und `behoben` (`:1059`) enthält damit auch diese
Tests — sie können decken. Ein Kandidat kann Nr. 1 und 2 also selbst ausnutzen, indem er einen passenden Test mitbringt.

## 11. Sperren im Wortlaut

Zwei Sicherheitssperren bei mir, beide beim Abschluss nach dem Review. Wortlaut aus den gespeicherten Belegen
(`SPERRE-KOPIE-GUTACHTERPROBEN.txt`, `SPERRE-2-BERICHT-ABSCHLUSS.txt`), nicht aus einem neuen Befehl.

**Sperre 1** — Werkzeug `terminal`, gegen 08:40. Zweck: die Proben des Prüfers in den Abschlussordner kopieren, jede
Kopie prüfen und das Protokoll der Ausführungsschicht auszählen. Befehl:
```bash
mkdir -p /root/biotop-vor-t4-03/review-proben && cd /tmp/review-vor-t4-03 && for f in *.py *.json *.txt *.sh; do cp -p "$f" /root/biotop-vor-t4-03/review-proben/; done; cd /root/biotop-vor-t4-03/review-proben && ls | wc -l && for f in *; do [ "$(sha256sum < $f)" = "$(sha256sum < /tmp/review-vor-t4-03/$f)" ] || echo "ABWEICHUNG $f"; done; echo "kopien geprueft"; /root/biotop-t3/venv/bin/python - <<'EOF'
import json, collections
from pathlib import Path
p = Path('/root/.local/share/tirith/log.jsonl')
zeilen = p.read_text(errors='replace').splitlines()
print('eintraege', len(zeilen))
probe = None
for z in reversed(zeilen):
    try:
        probe = json.loads(z); break
    except Exception:
        pass
print('schluessel', sorted(probe)[:20] if isinstance(probe, dict) else type(probe))
EOF
```
Meldung:
> Blocked: command or referenced script cannot restart, stop, or uninstall the gateway from inside the gateway process. The gateway would kill this command before it could complete (SIGTERM propagates to child processes). Run `hermes gateway restart` from a separate shell outside the running gateway.

**Sperre 2** — Werkzeug `execute_code`, kurz nach 08:44. Zweck: diesen Bericht abschließen (§10, §11, Berichtigungen
nach dem Review), die Spezifikationen anlegen und die Quellenliste des Veröffentlichungsskripts ergänzen. Der Befehl
war das Skript; seine unveränderte Abschrift ist `skript_bericht_abschluss_gesperrt.py` (nicht ausgeführt). Meldung:
> Blocked: cannot restart or stop the gateway from inside the gateway process. The gateway would kill this script before it could complete (SIGTERM propagates to child processes). Run the lifecycle command from a shell outside the gateway.

**Einordnung:** beide Male Sicherheitsfilter, harte Linie 3. Keiner der Befehle ruft den Dienstprozess auf. Vermuteter
Auslöser von Sperre 2 (nicht geprüft): Das Skript zitierte die Meldung von Sperre 1. Den Auslöser von Sperre 1 kenne
ich nicht. Nicht umgangen: kein Umformulieren, kein Teilbefehl, kein anderes Werkzeug. Nachgesehen um 08:44:08 bzw.
danach: nichts kopiert, nichts geschrieben. Mein Fehler: zweimal unabhängige Handlungen in einem Befehl gebündelt.

**Freigabe Philipp** (für genau diesen Fall, nicht als Dauerregel): die Schritte getrennt, den Wortlaut der Sperren aus
den gespeicherten Dateien übernehmen, das Auszählen des Protokolls der Ausführungsschicht weglassen; sperrt ein
einzelner Schritt, anhalten. Danach als einzelne Schritte, bis zu diesem Bericht ohne weitere Sperre:
1. `mkdir -p` des Ordners für die Proben;
2. `cp -p` der 17 Dateien (Proben, Ausgaben, Skript `lauf_proben.sh`);
3. Prüfung der Kopien mit `cmp`: 17 von 17 bytegleich;
4. Wächter nachgesehen (unten), nur gelesen;
5. dieser Bericht (`skript_abschluss_1_bericht.py`; Wortlaut der Sperren aus den Belegen gelesen);
6. `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md` (Datei geschrieben);
7. Quellenliste des Veröffentlichungsskripts ergänzt (Datei bearbeitet);
8. Veröffentlichung. Ihr Ergebnis (HTTPS bytegleich, Ordnerprüfsumme) steht in `PRUEFSUMME-ORDNER.txt` und in der
   Endmeldung, nicht hier.
Das Protokoll der Ausführungsschicht ist nicht ausgezählt.

**Beim Prüfer:** keine Sperre (`REVIEW.md` → „Sperren: keine“). Er meldet eine Änderung am Protokoll der
Ausführungsschicht, nicht von ihm geschrieben.

**Freigabeabfragen** in dieser Runde: keine außer der Freigabe oben.

**Zwischenbericht-Wächter in dieser Runde** (`~/.hermes/zwischenbericht/ausgeloest.json`: 2 von 8 Einträgen fallen in
diese Runde; die Ordner im Prüfkanal nachgesehen):
- 05:11:04, Werkzeugrunde 113 von 150 (Schwelle 110): `laeufe/biotop-vor-t4-03/zwischenbericht-20260924-051104-r113/`,
  5 Dateien, HTTPS bytegleich 5 von 5, Ordnerprüfsumme `084e8a7e5b6d8b63976e86edb87ace79c31d644c1f825f9e27895a7e64bca8f7`.
- 05:19:06, Werkzeugrunde 141 von 150 (Schwelle 140): `laeufe/biotop-vor-t4-03/zwischenbericht-20260924-051906-r141/`,
  5 Dateien, HTTPS bytegleich 5 von 5, Ordnerprüfsumme `e083ddbd17bde85f4e449eb619fa634cae5a06d098b463ac55512556667a52c1`.
- Beide im ersten Turn dieser Runde, der danach an der Iterationsgrenze (150) endete. Beide tragen eine Übergabe von
  3.647 Byte — so groß war `UEBERGABE.md` im Stand 03:40; sie war zu diesem Zeitpunkt anderthalb Stunden alt (§13).
- Kein Auslöser „Kontextfüllung ≥ 80 %“ und keiner „Verdichtung gescheitert“: Die Verdichtungen um 02:14 und 05:08
  gelangen (§0); vor der um 05:08 stand die Sitzung bei ≈ 505.000 von 1.000.000 Token (`logs/agent.log`).
- Die Abholadressen der beiden `DATEIEN.txt` stehen als ganze Zeilen in `DATEIEN.txt` dieses Ordners.

## 12. Eigene Entscheidungen

1. **Deckung je Merkmal gelesen:** Ein Muster gilt als gedeckt, wenn jedes seiner Merkmale von einem festhaltenden Test
   getroffen wird, nicht nur von einem einzigen Aufruf mit allen Merkmalen zugleich. Grund: Die Formvarianten der Sonde
   variieren je ein Merkmal; alle Merkmale in einem Aufruf zu verlangen, käme der verworfenen Regel „je Eingabe“ nahe.
   Risiko: Zwei Tests mit je einem Merkmal decken ein Muster, das keiner als Ganzes prüft.
2. **Uneinige Gewinnmessungen: gepoolter Median** über beide gepaarten Messungen. Sonst bliebe ein Grenzfall unentschieden;
   die größere Stichprobe liegt dort, wo das Rauschen entscheidet. Festgelegt vor den Nachspielen.
3. **Band = 0,85 ÷ t … 0,85 · t** mit der gemessenen Rauschtoleranz t des Bereichs.
4. **Muster über alle Argumente** (nicht nur die variierten Stellen), damit Lastbeobachtungen ihr Weißraum-Merkmal tragen.
   Folge: Merkmale nicht variierter Argumente werden mitverlangt (§3, `null_zahl`).
5. **`kern/gegenzeugen.py` statt `organe/`:** Der Verdrahtungstest verlangt für jedes Organ einen Aufruf im Lauf; die
   Gegenzeugen sind wie in T3 private Bauverifikation außerhalb des Laufs.
6. **Typtreuer Ausgangsdefekt** in der Nebenwirkungsprobe (§9).
7. **Vorher/Nachher an denselben Testfunktionen:** Die Fälle der Lücken wurden am alten Code aus `git archive 6243377`
   ausgeführt, statt eigene Altfälle zu bauen — dieselben Diffs, dieselbe Last, derselbe Ablauf.
8. **Zwischenberichte des Wächters in `DATEIEN.txt`:** Sie liegen im selben Ordner, sind aber eigene Lieferungen mit
   eigener Prüfsumme; `DATEIEN.txt` nennt ihre Abholadressen, das Manifest dieses Ordners umfasst sie nicht.
9. **Nachtrag-Commit `0aac612`** statt Änderung von `d54bf2f`, und die Regression danach noch einmal voll: Die Geschichte
   bleibt unverändert, und die Zahl 533/2/0 gehört zu genau dem Stand, der jetzt HEAD ist.

## 13. Eigene Fehler in dieser Runde

- **`TEILLAUF-1.txt` ist unvollständig:** mit doppeltem `-q` ohne Kopf, Befehl und Zusammenfassung; belegt sind nur 103
  Fortschrittspunkte und rc 0 (Review Nr. 18).
- **Prüfwerk ohne Bereichsordner:** 15 von 30 neuen Tests brachen im zweiten Teillauf (`TEILLAUF-2.txt`) bei der Basismessung ab (Bandit:
  „No such file or directory“). Behoben (`bau/DIAGNOSE-PROBEWERK.txt`).
- **Fälle, die ein Werkstest schon fing:** Generator, Sortierung und Methode wurden zuerst über das Pareto-Maß abgelehnt,
  nicht vom Vergleich; die Deckungsfälle scheiterten an der Verfassung (Testdateinamen) und am Kernmaß (neue Tests eines
  Kandidaten zählen nicht). Die Fälle sind so umgebaut, dass nur die Sonde sie sehen kann (`TEILLAUF-3` … `-5`).
- **Gegenprobe falsch gebaut:** `xs[:] = sorted(xs)` weicht bei einem Tupel im Fehlertyp ab — eine echte Abweichung. Ersetzt.
- **Bezugsgröße der Gegenzeugen:** zuerst „x von 117.732“ mit dem gültigen statt dem vollen Nenner für Leerzeichen;
  berichtigt vor der Messung am Commit, jetzt je Teil „x von y“.
- **Register nicht im Teillauf:** `test_t3_python_annahmen.py` fehlte in den Teilläufen; die Regression am Commit fand es (§8).
- **Zwischenmeldung nach der Iterationsgrenze** war richtig als „nicht geliefert“ gekennzeichnet; die Übergabe war dort
  aber zwei Stunden alt — und in den beiden Zwischenberichten des Wächters (05:11, 05:19) anderthalb Stunden (§11).
- **Zwei Sicherheitssperren durch gebündelte Befehle** (§11).

## 14. Offen für Philipp

1. **Vergleichslast für die Gewinnschwelle vergrößern** (Entscheidung 2, §4): K3091 liegt 2 Punkte von der Schwelle, die
   Streuung einer 5er-Messung bei ≈ 6,5 %. Ohne größere Last bleibt „3 von 3 gleich“ für diesen Kandidaten Zufall.
2. **Muster und nicht variierte Argumente** (§3): Sollen Merkmale von Argumenten, die die Sonde nicht variiert hat, zum
   Muster gehören? Bei K2868 verlangt jedes der 40 Muster `null_zahl`. Ohne sie verlören Lastbeobachtungen ihr
   Weißraum-Merkmal nicht, wenn nur die Grundliste ausgenommen wird — das wäre eine Regeländerung nach der Messung und
   braucht Eure Entscheidung.
3. **Methoden in TypeScript** (§2): nicht gebaut.
4. **Doppelprüfung erzwingen** (§5): Wo soll sie für künftige Testwerke laufen — bei der Versiegelung, bei der Aufnahme?
5. **S-12 und S-3 (Wurzelmodul) nur am Organ belegt**, nicht durch den Laufweg (§6).
6. **Generalprobe:** Die Gewinn-Nachmessung in `lauf._generation_koerper` ist gelesen, nicht ausgeführt (0 von 16
   Urteilen im Verdrahtungslauf mit Nachmessung).
7. **Die vier hohen Review-Befunde vor T4 beheben** (R4-1 … R4-4): Mit ihnen lässt die Deckung je Muster die K2868-Lage
   durch, sobald ein Kandidat einen Test mit doppeltem Leerzeichen mitbringt, und die Sonde schweigt bei Iterator-Objekten
   und `__slots__`-Klassen. Dazu eine Frage: Soll `weissraum` je Zeichen getrennt werden (Tab, Zeilenumbruch, CR, NBSP,
   doppeltes Leerzeichen), passend zu den Formvarianten?
8. **Sicherheitssperre des Filters für den Dienstprozess auf Befehle ohne Bezug dazu** (Runde 2 beim Prüfer, Runde 3
   zweimal bei mir): als Fehlalarm melden, oder gibt es eine Regel, die ich kennen muss?
