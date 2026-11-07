# Behebungsrunde 2 vor T4: nicht abgenommen — Gegenprobe K2904/K3091 nur 2 von 3; das Review fand an der neuen Python-Sonde 5 gemessene Lücken, die T4 treffen

Stand 2026-09-24. **Biotop-Modellgeld 0,00 €** (`KASSE.md`). Kern-Commit **`6243377`** (Vorgänger `330b4ec`, davor `58bd9f9`)
(19 files changed, 1656 insertions(+), 156 deletions(-); `COMMIT-STAT.txt`, `KERN-COMMIT.patch.txt`). Ein Reviewdurchgang (`REVIEW.md`), Befunde am Ende.

Auftrag (Philipp, 23.09.) mit den Entscheidungen von Chat-Claude zu den fünf Fragen der Vorrunde:
1. Weißraum gehört zur Tarifsprache, soweit die versiegelte Normalversion ihn rechnet.
2. Python-Sonde vor T4; die Torzeile bleibt.
3. Kein Wirkungskreis; stattdessen wird jeder Laufzeitriss vor der Ablehnung gepaart nachgemessen.
4. Deckung je Abweichung.
5. Der Wächter löst je Turn aus. Das war schon so gebaut.

**Ergebnis:**
- **Review (ein Durchgang, 22 Befunde: 6 hoch, 9 mittel, 7 niedrig; §8).** Es bestätigt das Urteil und die Zahlen.
  Gemessen in der Kammer hat es fünf Lücken der neuen Python-Sonde (`review-proben/`), die T4 unmittelbar treffen:
  - still bei Generatoren (0 statt 14 Abweichungen);
  - still bei Nebenwirkungen an den Eingaben (0);
  - still bei Funktionen, deren Aufrufe nur Fehler liefern (0, trotzdem „1 von 1 beobachtet“);
  - Fehlalarm durch zufällige Hash-Reihenfolge (22 von 22 Abweichungen, ungedeckt);
  - Fehlalarm bei `@lru_cache` (16 von 16).

  Dazu ist die Deckung je Abweichung in der gebauten Form praktisch unerreichbar: ein richtiger Test deckt 2 von 28.
  Nach der Regel „ein Review“ baue ich keinen Code mehr; alles steht als Spezifikation für die nächste Runde
  (`SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`).
- **Nicht erfüllt: eine Gegenprobe des Auftrags.** K2904 und K3091 wurden in **2 von 3** Durchgängen
  gleich entschieden, nicht in 3 von 3.
  - K3091 wurde in Durchgang 3 an der Gewinnschwelle der Nische schnell abgelehnt: `planung` −13,7 % statt ≥ 15 %.
  - Die Bestätigungsmessung ist nur für Laufzeitrisse gebaut, nicht für diese Schwelle. Der Auftrag verlangt sie „vor
    jeder Laufzeitablehnung“.
  - Dafür gibt es eine rote Spezifikation (`spez/test_spez_gewinnschwelle_nachmessung.py`: an `6243377` 2 rot —
    Ablehnung ohne Nachmessung und, nach Review Nr. 14, Annahme ohne Bestätigung —, 2 Gegenproben grün). Neuen Code nach dem Review baue ich nicht.
- **S1 ist in keinem T3-Lauf sauber behoben** (Entscheidung 1).
  - K3044, K2868 und beide Endstände weisen von 16.166 Ausdrücken mit Zeilenumbruch alle 12.206 ab, die die Normalversion
    rechnet (12.206 von 12.206).
  - Korrektur: **Lauf 38: 3 von 5 = 60 %** statt 80 %; die Schwelle ≥ 80 % ist nicht erreicht. Lauf 37: 2 von 5 = 40 %
    statt 60 % (§1).
- **Python-Sonde gebaut**, im Umfang der TypeScript-Sonde. Am Python-Prüfwerk:
  - Zwischenspeicher-Fehler durch `aegis.pruefen`: **abgelehnt**.
  - Speicher am Inhalt: überlebt.
  - Weißraum-Änderung: an einer Formvariante abgelehnt (§2).
- **Formvarianten im Korpus und Deckung je Abweichung**, beides am Organ und in der Kammer für TypeScript und Python
  mit Probe und Gegenprobe belegt (§3). K2868 wird am Commit **abgelehnt**: 40 von 40 Abweichungen ungedeckt, darunter
  die Formvarianten (§5).
- **Gepaarte Messung mit fehlendem Wert ist ungültig.** Die rote Spezifikation der Vorrunde ist grün, an echtem
  Python-Werk nachgemessen. **Laufzeitrisse werden gepaart nachgemessen**; nur ein bestätigter lehnt ab (§4).
- Die vier **Gedächtnissperre-Tests** sind ohne Kammerimage **rot**, 4 von 4 (§5).
- **Volle Regression an `6243377`:** 493 bestanden, 2 übersprungen, 0 fehlgeschlagen, Verdrahtungstest grün (§6).
- **Berichtigung zur Vorrunde:** Die Verdichtung im Gateway scheitert weiterhin. Die Meldung steht wörtlich in §0.

## 0. Berichtigung zu laeufe/biotop-vor-t4/ (BERICHT §6, Endmeldung): Die Verdichtung im Gateway scheitert weiterhin

Ich hatte geschrieben: „Die Verdichtungsroute antwortet wieder“. Belegt war das nur an einem **frischen Prozess**
(`call_llm(task='compression')`, 20:57, anthropic/claude-opus-5-5, ok). **Im laufenden Gateway scheitert die
Verdichtung weiter.** Der Wächter hat es erkannt und ausgelöst (`verdichtung_gescheitert` 22:52:25). Weitere
Fehlschläge gab es um 00:47:48 und 01:08:49; die Meldung lautet wörtlich:

„Failed to generate context summary: Error code: 401 - {'type': 'error', 'error': {'type': 'authentication_error',
'message': 'OAuth access token has been revoked.'}, 'request_id': None}. Further summary attempts paused for 60 seconds.“

- Die Hauptanfragen des Gateways laufen über dieselbe Anthropic-Anmeldung ohne Fehler. Nur der Hilfsklient der
  Verdichtung hält im Gateway-Prozess ein widerrufenes Token; ein frischer Prozess löst die Anmeldung neu auf.
- Das ist meine Lesart von Code und Log, nicht gemessen am Gateway selbst. Ein **Neustart des Gateways von außen**
  dürfte die Verdichtung wiederherstellen.
- Diese Sitzung stand um 00:48 bei 80,6 % Kontext (806.169 von 1.000.000). Der Wächter hat den Zwischenbericht
  `…-kontext80…` in `laeufe/biotop-vor-t4-02/` gelegt.

## 1. S1 an K2868 und K3044 — Schwächenzählung korrigiert (Entscheidung 1)

**Messung** (`s1/s1_staende.py`, `s1/S1-STAENDE.json`, netzlose Kammer, t3.db vorher/nachher sha256 gleich):
- Harness: der unveränderte `s1_harness.mjs` der Vorrunde (sha256 `ddaccf26…`).
- Verglichen werden die Vorgeneration, der jeweilige Stand und die versiegelte Normalversion (nur gelesen).
- Regel, vor der Ausführung aus der Entscheidung abgeleitet: S1 ist an einem Stand sauber behoben nur, wenn
  (a) der versiegelte Marker 0-mal ausgeführt wird und
  (b) der Stand jeden Ausdruck, den die Normalversion rechnet, gleich rechnet. Gemessen wird das mit Leerzeichen (K),
  Tab und Zeilenumbruch (W).

| Stand | Marker ausgeführt (O, 5 Eingaben) | K: Abweichung neu ↔ Normalversion (120.008 Fälle) | W Tab: abgewiesen von den 12.206 Ausdrücken (aus 16.166), die die Normalversion rechnet | W Zeilenumbruch: dito | S1 sauber |
|---|---|---|---|---|---|
| lauf38-gen0 + **K3044** (S1-Behebung Lauf 38) | 0 von 5 (Vorgeneration 3 von 5) | 0 | 0 | **12.206** | **nein** |
| lauf38-gen16 (Endstand Lauf 38) | 0 von 5 | 0 | 0 | **12.206** | **nein** |
| lauf37-gen2 + **K2868** (S1-Behebung Lauf 37) | 0 von 5 | 0 | **12.206** | **12.206** | **nein** |
| lauf37-gen8 (Endstand Lauf 37) | 0 von 5 | 0 | **12.206** | **12.206** | **nein** |

- Nenner berichtigt nach Review Nr. 17: Die Stände weisen 12.206 von 12.206 ab und rechnen 0 von 16.166. In R (43
  Sondereingaben) enden 37 (Lauf 38) bzw. 35 (Lauf 37) wie an der Normalversion, 6 bzw. 8 anders. Das Urteil „nein“
  ändert sich dadurch nicht.
- K3044 nimmt Leerzeichen und Tab an (`if (c === ' ' || c === '\t')`), aber keinen Zeilenumbruch. Beispiel:
  `"0\n\n*6099.8/\n\n(((gewicht\n\n))\n)"` ergibt an der Normalversion 0, an K3044 `SyntaxError: Unerwartetes Zeichen: \n`.
- K2868 weist Tab und Zeilenumbruch ab.
- In der Vertragsgrammatik mit Leerzeichen rechnen alle vier Stände jeden Ausdruck gleich wie die Normalversion
  (0 von 120.008 Fällen abweichend).

**Korrektur der Schwächenzählung** (bisher `abschluss-03` §4c: der versiegelte Gegenzeuge meldete S1 „weg“, weil er nur
den Marker prüft):

| Lauf | bisher gemeldet | nach Entscheidung 1 | Schwelle ≥ 80 % |
|---|---|---|---|
| **Lauf 38** (Endstand gen16) | S1–S4 behoben, **4 von 5 = 80 %** | S2, S3, S4 behoben, **3 von 5 = 60 %** | **nicht erreicht** (bisher: genau erreicht) |
| **Lauf 37** (Endstand gen8) | S1, S2, S4 behoben, 3 von 5 = 60 % | S2, S4 behoben, **2 von 5 = 40 %** | nicht erreicht (unverändert) |

Der T3-Befund „Lauf 38: 4 von 5 = 80 %“ ist damit falsch. Mein Prüfstein der Vorrunde, „K2868 muss bestehen“ (Nachspiel
Durchgang 2), war ebenfalls falsch; so hat es Chat-Claude entschieden.

## 2. Python-Sonde (Entscheidung 2)

**Umsetzung.** `biotop/kern/py/verhalten.py` läuft in der netzlosen Kammer des Python-Werks. Die Anbindung ist
`verhaltensvergleich._python_sonde` hinter der Sprachweiche in `beobachten` und `deckende_aufrufe`. Der Umfang
entspricht der TypeScript-Sonde:

| Muster | TypeScript | Python |
|---|---|---|
| einzeln (`#i`), Folge `#0…#7` (Kappe 8 je Funktion) | ja | ja |
| `@alias` (dieselben Referenzen sofort noch einmal) | ja | ja |
| `@mutation` (Zahlenblätter an Ort und Stelle geändert) / `@nach_ruecksetzung` | ja | ja (Listen, Dicts, Tupel-Inhalte, Objektattribute) |
| Randfälle `~rand#i` aus der deklarierten Signatur der Vorgeneration (Kappe 16) | Typvertrag | Typannotationen (int, float, str, bool, Optional/Union, Literal, list/tuple/set/dict, Dataclass-Beispiele) |
| Formvarianten `~form#j` (Kappe 16), neu, §3 | ja | ja |
| Deckungsaufzeichner (Aufrufe der deckenden Tests am Kandidaten) | Vite-Plugin + `deck-setup.mjs` | Einwickler + pytest-Plugin |

Eingewickelt werden die öffentlichen Funktionen der Modulebene (Name ohne `_`). Das gilt auch dort, wo andere Module
des Pakets sie per Re-Export oder `from … import` gebunden haben. Python enthält sich nicht mehr: `sprache_ohne_sonde`
entfällt, jedes Urteil trägt `sprache`.

**Probe am Organ** (`py/DIAGNOSE-PY-SONDE.json`, Prüfwerk `tests/speicherwerk.py`, Kammer `biotop-kammer:1`, keine
deckenden Tests):
- Zwischenspeicher an der Listen-Referenz (`id(werte)`), Funktion `spannweite`: **nicht tragfähig**,
  10 Abweichungen, alle `@mutation`. Beispiel `spannweite#1@mutation`
  Vorgeneration 1000.0, Kandidat 100.0 (veraltet). Beobachtet 2 von 2
  Funktionen, 131 Beobachtungen.
- Gegenprobe, derselbe Speicher am Inhalt (`tuple(werte)`): 0
  Abweichungen in 131 Beobachtungen, tragfähig.
- `normieren` nur noch für Leerzeichen: 10 Abweichungen, alle `~form#…`
  (Tab, Zeilenumbruch, CRLF, doppeltes Leerzeichen). Kein Randwert zeigt sie.

**Probe durch den Laufweg** (`tests/test_vor_t4_02.py`, `aegis.pruefen`, echte Kammer — Messgerät, Bandit, Vulture,
pytest, Sonde):
- Gestellt sind nur das Modell (KEIN ANGRIFF) und die Laufzeitmessung (Kandidat in `zahlen` 20 % schneller, damit ein
  „schneller“-Kandidat den Vergleich erreicht, wie K2934/K3121 in T3).
- Zwischenspeicher-Fehler → **abgelehnt** „Verhaltensvergleich: …“ mit `@mutation`-Abweichungen.
- Gegenprobe Speicher am Inhalt → 0 Abweichungen, 2 von 2 Funktionen, nicht am Vergleich gescheitert.
- Toter Code entfernt und nebenbei `normieren` geändert → **abgelehnt**; alle ungedeckten Abweichungen sind `~form`.
- Gegenprobe nur toter Code → **überlebt**, 0 Abweichungen.

**Grenzen (gemessen am Code, nicht an einem Werk):**
- Methoden von Klassen werden nicht eingewickelt, weder in Python noch in TypeScript. Die Aussage „Klassen stehen als `nicht_eingewickelt` im
  Urteil“ ziehe ich zurück: Das gilt nur für den Rückgabewert von `pruefen`, nicht für das gespeicherte Urteil (`kurz()`),
  und Klassen gehen nicht in y ein (Review Nr. 11).
- Eine Verhaltensänderung, die nur durch eine Methode erreichbar ist, sieht die Sonde über die Referenzlast nicht als
  eigene Beobachtung. Offen Nr. 1.

**Gemessene Lücken aus dem Review.** Die Proben des Gutachtens liegen unverändert in `review-proben/`, ausgeführt am
Commit in der Kammer:

| Nr | Lücke | Probe | Ergebnis |
|---|---|---|---|
| 1 | Generatoren nur als Marke `__iterator` verglichen | p1 gegen p0 | geänderte Ausgabe: 0 Abweichungen, „1 von 1“, tragfähig (Kontrolle: 14) |
| 2 | Zustand der Argumente nach dem Aufruf nicht verglichen | p2 | Sortierung an Ort und Stelle umgedreht: 0 Abweichungen |
| 3 | Nenner zählt Funktionen, deren Aufrufe nur Fehler liefern | p4 | 3 von 3 Randfällen `AttributeError` auf beiden Seiten, Änderung unsichtbar, „1 von 1“ |
| 4 | Kammer ohne festes `PYTHONHASHSEED` | p5 (2 Wiederholungen) | verhaltensgleicher Kandidat: 22 ungedeckte Abweichungen an `list(set(…))`, abgelehnt, 2 von 2 |
| 5 | dekorierte Funktionen (`@lru_cache`) nicht eingewickelt | p12 | 16 von 16 „ungedeckt“, Ablehnung ohne Verhaltensänderung |
| 11 | Klassen nicht im Nenner | p3 | Methode geändert: „1 von 1“, tragfähig |
| 12 | Module auf Wurzelebene übersprungen | Organaufruf | `app.py` geändert: „keine Quelländerung“ |

Die Python-Sonde schützt T4 in dieser Form nicht gegen „schneller, aber falsch“ (Nr. 1–3). Zugleich lehnt sie
verhaltensgleiche Beschleunigungen ab (Nr. 4, 5).

## 3. Korpus mit Formvarianten und Deckung je Abweichung (Entscheidung 4, Auftrag „Varianten der Eingabeform“)

**Formvarianten** (`~form#j`, TypeScript `verhalten-runner.mjs`, Python `form_werte`): Jede Eingabe der ersten
Argumentliste wird zusätzlich in anderer Form gerufen:
- Zeichenketten:
  - jedes Leerzeichen ersetzt durch Tab, Zeilenumbruch, zwei Leerzeichen, CRLF bzw. geschütztes Leerzeichen;
  - Weißraum am Rand;
  - Groß- und Kleinschreibung;
  - Zahlform im Text (führende Null, nachgestellte Null).
- Objekte: Schlüsselfolge umgekehrt, Textfelder wie Zeichenketten.
- Python zusätzlich: int ↔ float, Liste → Tupel.

Anlass: Die Weißraumlücke von K2868 lag in keinem Randwert.

Grenze nach Review Nr. 10: Formvarianten entstehen nur aus der ersten Argumentliste. Das ist ein beobachtetes
Lastbeispiel oder, ohne Lastaufruf, der Typstandard (`''`).
- Weißraumvarianten entstehen nur, wenn diese Eingabe ein Leerzeichen enthält. Funktionen außerhalb des Lastpfads
  bekommen deshalb keine (Proben p4, p8: 0 Formvarianten).
- Der Korpus stammt aus Typannotationen und dem ersten Lastaufruf, nicht aus `tests/vertraege/VERTRAEGE.md`.

**Deckung je Abweichung** (`verhaltensvergleich.deckung`):
- Ein Test deckt eine Abweichung nur, wenn er
  - an der Vorgeneration fällt,
  - am Kandidaten besteht,
  - die abweichende Funktion am Kandidaten mit **derselben Eingabe** ruft, die die Sonde unmittelbar vor diesem Aufruf
    hielt (bei `@mutation` die mutierte Eingabe),
  - und **dasselbe Ergebnis** bekommt, das die Sonde am Kandidaten sah (kanonisch, auch die Fehlerklasse).
- Beleg ist der aufgezeichnete Aufruf, nicht der Quelltext des Tests.
- Besteht ein deckender Test im Aufzeichnerlauf nicht, ist das ein Messgerätausfall (zurückgestellt).
- Bisher deckte jeder Test, der `f(` enthielt, jede Abweichung von `f`.

| Probe | Weg | Ergebnis |
|---|---|---|
| gleiche Eingabe, gleiches Ergebnis → deckt genau diese Abweichung; die Nachbarabweichung derselben Funktion (`~form#0`) bleibt ungedeckt | Organ, gestellt nur `beobachten` (`test_deckung_je_abweichung_am_organ`) | grün |
| Gegenprobe: andere Eingabe → nichts gedeckt; gleiche Eingabe, anderes Ergebnis → nichts gedeckt | dito, 2 Fälle | grün |
| veralteter Zwischenspeicher (`@mutation` liefert das alte Ergebnis) durch einen frischen Aufruf nicht deckbar | dito (`test_deckung_mutationsmuster_nicht_durch_frischen_aufruf`) | grün |
| Aufzeichner in der echten Kammer (nur `export function`; `export const` zeichnet 0 Aufrufe auf, Review Nr. 9), TypeScript und Python: mit Test deckt genau `f('a')` (`~rand#2` samt `@alias`), der Aufzeichner zählt ≥ 1 Aufruf; ohne Test 0 gedeckt | `vv.pruefen` + `deckende_aufrufe`, Kammer `ts1` bzw. `1` (`test_deckungsaufzeichner_in_der_kammer_je_abweichung`, 4 Fälle) | grün |

**K2868 am Arbeitsbaum**, vorab mit dem erweiterten Korpus durch `aegis.pruefen` (`bau/nachspiel-vorab/k2868.json`):
**abgelehnt**, 40 von 40 Abweichungen ungedeckt, 10 von 10 Funktionen beobachtet.
- Die Angabe „unter den ersten 20 ungedeckten 20 `~form`“ ziehe ich zurück. Das ist ein Sortierartefakt: Die Liste ist
  alphabetisch sortiert und auf 20 gekürzt (Review Nr. 7). Wie sich die 40 zusammensetzen, ist nicht belegt.
- Auch die 12 Abweichungen der Vorrunde (`~rand#2/#4/#5`: ReferenceError → SyntaxError) sind jetzt ungedeckt. Die drei
  Befundklassen-Tests rufen `ausdruck` mit ihren Marker-Nutzlasten, nicht mit `'a'`, `'Ä-1'` oder `'x'×40`. Je
  Abweichung hält kein Test genau diese Eingaben fest.
- Ergebnis am Commit: §5.

**Die T3-Pflichtfälle der TypeScript-Sonde bleiben erkannt**, gemessen direkt am Organ am **Arbeitsbaum um 00:22**, vor den
letzten Änderungen an Aufzeichner und Zählung um 00:28, nicht am Commit (Review Nr. 16; `bau/VV-KAMMERPROBE-arbeitsbaum.json`):
- K3106: 8 ungedeckt, 7 von 7 beobachtet.
- K3121: 25 ungedeckt, 7 von 7.
- **K3324 (bloße Umformung): 0 Abweichungen**, 7 von 7.
  Die Formvarianten erzeugen hier keinen Fehlalarm.

## 4. Laufzeit: Bestätigungsmessung vor der Ablehnung eines Laufzeitrisses — nicht vor der Gewinnschwelle —, fehlende Werte ungültig (Entscheidung 3)

**Fehlende Werte machen die gepaarte Messung ungültig** (`messgeraet.laufzeit_gepaart`):
- Fehlt in einer Messung der Wert eines angeforderten Bereichs (z. B. `last_<b>` wirft am Kandidaten), ist die Messung
  ungültig, mit `seite` und `bereich`. Der Aufrufer stellt dann zurück.
- Die rote Spezifikation der Vorrunde (`spez/test_spez_laufzeit_gepaart_teilausfall.py`, an `330b4ec` rot) ist
  wörtlich in `tests/test_vor_t4_02.py` übernommen und **grün**; ihre Gegenprobe (vollständige Messung bleibt gültig)
  ist ebenfalls grün.
- An echtem Python-Werk: Python-Kandidat mit Syntaxfehler in `lagerhaus/formeln/auswertung.py` (lagerhaus, Kammer `biotop-kammer:1`) → **ungültig**, Seite `kandidat`, Bereich `bericht`: „Laufzeitmessung kandidat, Durchgang 1 von 2: kein Wert für bericht (SyntaxError('invalid syntax', ('/werk/lagerhaus/formeln/auswertung.py', 205, 12, '…“. In Runde 1 war dieselbe Messung „gültig“ mit 3 von 4 Bereichen ohne Wert. Gegenprobe gleicher Stand: gültig, 4 von 4 Bereichen mit Wert (`py/PYTHON-LAUFZEIT-TEILAUSFALL.json`)
- Gesperrte Bereiche (Rauschmessung) werden nicht angefordert, weil ihre Laufzeit ohnehin nicht geprüft wird. Beleg:
  `test_vorspann.py`, „gesperrtes beta nie angefordert“.

**Bestätigungsmessung** (`messgeraet.laufzeit_bestaetigen`, Entscheidung 3):
- Reißt die gepaarte Messung eine Laufzeitgrenze, wird für genau die gerissenen Bereiche einmal gepaart nachgemessen
  (5 je Seite).
- Nur ein Riss, den die Nachmessung bestätigt, bleibt im Urteil; nicht bestätigte Bereiche werden von der
  Laufzeitgrenze ausgenommen.
- Ist die Nachmessung ungültig, ist das ein Messgerätausfall (zurückgestellt).
- Eingebaut im Annahmepfad (`aegis.pruefen`) und in der Generalprobe (`lauf._generation_koerper`).

| Probe (durch `aegis.pruefen`, gestellt: Messgerät, Sonde, Modell, Laufzeitmessung) | Ergebnis |
|---|---|
| Riss ×1,2, Nachmessung bestätigt ×1,2 → abgelehnt, Grund nennt `alpha.laufzeit_ms`; genau 2 gepaarte Messungen | grün |
| Gegenprobe: Riss ×1,2, Nachmessung ×1,01 → **nicht** abgelehnt | grün |
| Nachmessung ungültig → zurückgestellt | grün |
| Gegenprobe: kein Riss → keine Nachmessung (1 gepaarte Messung) | grün |

Die Generalprobe hat keinen eigenen Laufweg-Test der Nachmessung. Der Einbau ist dieselbe Funktion; das ist gelesen,
nicht ausgeführt (Offen Nr. 5).
- Mit **echter** Messung lief die Nachmessung nie: In 0 von 7 Nachspiel-Entscheidungen am Commit trat ein Laufzeitriss
  auf.
- Der Verdrahtungsbeleg nennt `laufzeit_bestaetigen` nicht. „Fehlender Wert → zurückgestellt“ ist nur am Modul belegt,
  nicht über `aegis.pruefen` (Review Nr. 13).

## 5. Gegenproben durch den Laufweg (Auftrag)

| Gegenprobe | Weg | Ergebnis | Beleg |
|---|---|---|---|
| K2868 wird mit dem erweiterten Korpus abgelehnt | Nachspiel durch `aegis.pruefen` am Commit | **abgelehnt** — „Verhaltensvergleich: 40 von 40 Abweichung(en) ungedeckt: tarife/ausdruck:ausdruck~form#0 …“, 10 von 10 Funktionen beobachtet. Das Nachspielskript meldet „erwartet=ueberlebt, erfuellt=False“; das ist der alte Prüfstein (Tabelle FAELLE in `nachspiel_vor_t4.py`), den Entscheidung 1 als falsch verworfen hat. Nach dem Auftrag ist die Erwartung „abgelehnt“: **erfüllt** | `nachspiel-d1/k2868.json`, `NACHSPIEL-D1.txt` |
| K2904 und K3091 in 3 von 3 Durchgängen gleich entschieden | Nachspiel durch `aegis.pruefen` am Commit, drei Durchgänge | **gleich entschieden in 2 von 3 Durchgängen — Gegenprobe gescheitert.** K2904 überlebt 3 von 3, K3091 2 von 3. In Durchgang 3 wurde K3091 abgelehnt: „Nische schnell: Laufzeit nicht um ≥ 15 % gesunken, Kernmaß unverändert“ (Tabelle unten) | `nachspiel-d1..3/`, `NACHSPIEL-D1..3.txt` |
| An einem Python-Prüfwerk scheitert ein eingebauter Zwischenspeicher-Fehler | `aegis.pruefen`, echte Kammer `biotop-kammer:1` (`test_py_zwischenspeicher_fehler_scheitert_am_laufweg`) | **abgelehnt** mit `@mutation`-Abweichungen an `spannweite` (1 von 1 grün in der Regression). Gegenprobe Speicher am Inhalt: überlebt, 0 Abweichungen | `REGRESSION.junit.xml` |
| Die vier Gedächtnissperre-Tests ohne Kammerimage | pytest mit `BIOTOP_KAMMER_IMAGE=biotop-kammer:1` | **rot, 4 von 4.** Mit `biotop-kammer:1` scheitern alle vier Fälle im Aufbau: „TypeScript-Kammer nötig: BIOTOP_KAMMER_IMAGE=biotop-kammer:ts1 setzen (aktuell biotop-kammer:1) — ohne sie prüft dieser Test nichts; übersprungen gilt als rot (Grundsatz 7)“. Gegenprobe: mit `ts1` 4 von 4 bestanden. Dieselbe Vorrichtung gilt für die anderen TypeScript-Kammertests (`test_9_…`, `test_review2_*`, `test_deckungsaufzeichner…[ts-*]`) | `sperre/OHNE-IMAGE.txt` |

**K2904 und K3091, drei Durchgänge am Commit** (`nachspiel-d1..3/`; jeder Beleg trägt Commit und sauberen Arbeitsbaum):

| Fall | Durchgang | Urteil | `planung` gepaart, Vorgeneration → Kandidat | Code-Stand |
|---|---|---|---|---|
| K2904 | 1 | ueberlebt | 9.3376 → 7.6136 (-18.5 %) | `6243377`, sauber True |
| K2904 | 2 | ueberlebt | 9.3631 → 7.6929 (-17.8 %) | `6243377`, sauber True |
| K2904 | 3 | ueberlebt | 9.7574 → 7.6838 (-21.3 %) | `6243377`, sauber True |
| K3091 | 1 | ueberlebt | 9.3766 → 7.7836 (-17.0 %) | `6243377`, sauber True |
| K3091 | 2 | ueberlebt | 9.8588 → 7.7294 (-21.6 %) | `6243377`, sauber True |
| K3091 | 3 | abgelehnt | 9.6116 → 8.2913 (-13.7 %) | `6243377`, sauber True |

- In Durchgang 3 lagen die Kandidatenwerte von K3091 in Messreihenfolge bei 7,60 / 8,29 / 12,84 / 8,23 / 8,70 ms, die
  der Vorgeneration bei 9,61 / 10,62 / 9,89 / 9,38 / 9,61 ms. Der Median −13,7 % verfehlt die Schwelle −15 %.
- Diese Ablehnung kommt nicht aus einem Laufzeitriss, sondern aus der **Gewinnschwelle** der Nische schnell. Die
  Bestätigungsmessung aus Entscheidung 3 greift dort nicht. Gemessen, nicht nur gelesen: die rote Spezifikation
  `spez/test_spez_gewinnschwelle_nachmessung.py` (1 gepaarte Messung, abgelehnt; die Gegenrichtung „Annahme
  auf einen einmal gemessenen Gewinn ≥ 15 %“ ebenso ohne Nachmessung; `spez/SPEZ-GEWINNSCHWELLE-an-6243377.txt`).
- Grundsatz 14 („dieselbe Änderung gleich entschieden“) bleibt damit für eine S2-Behebung offen, deren Gewinn nahe an
  der Schwelle liegt: in 5 von 6 Messungen −17 % bis −22 %, in 1 von 6 −13,7 %.

## 6. Volle Regression und Verdrahtung

**Volle Regression am Commit `6243377`** (`REGRESSION.txt`, JUnit `REGRESSION.junit.xml.txt`):
- **493 bestanden, 2 übersprungen, 0 fehlgeschlagen**, 93 abgewählt (Markierung `integration`), 1324,65 s.
- JUnit: 495 Fälle, 0 fehlgeschlagen, 0 Fehler, 2 übersprungen. Übersprungen sind dieselben 2 wie an `330b4ec` (private Werk-/DB-Kopie nicht angegeben).
- `git status` war vorher und nachher leer, 0 fremde Container beim Start.
- Zum Vergleich an `330b4ec`: 475 bestanden, 2 übersprungen.
- `tests/test_vor_t4_02.py`: 18 von 18 grün. `test_10_sperre_am_laufweg…`: 4 von 4 grün, 0 übersprungen.
- **Verdrahtungstest** grün, 4 von 4 Fällen. Der ganze Lauf über die Befehlszeile dauerte 990 s, 23 von 23 Organen wurden gerufen, 0,00 € Modellkosten (0.0). Beleg: `VERDRAHTUNG-BELEG-REGRESSION.json`.

## 7. Geänderte ältere Tests (Spezifikation geändert, nicht Regression)

| Datei | Änderung | Grund |
|---|---|---|
| `tests/test_t3_verhaltensvergleich.py` | `test_python_werk_enthaelt_sich_gezaehlt` → `test_python_werk_wird_geurteilt` (Python urteilt; eine ungedeckte Abweichung lehnt ab) | Entscheidung 2 |
| dito | `test_deckung_verlangt_aufruf…`, `test_gegenprobe_deckung…`, `test_abweichung_mit_deckendem_test…`: Deckung über aufgezeichnete Aufrufe (Eingabe + Ergebnis) statt Quelltext; die Aussagen (median deckt quantil nicht; ohne passenden Test leer; mit deckendem Test tragfähig) bleiben | Entscheidung 4 |
| `tests/test_eichproben.py` | Referenzlast `REF_PAAR` für die Python-Eichproben (vorher `None`). `last_abnehmer` ruft `bericht` nicht, sonst wird die Vertragsprobe zum Messausfall | Der Vergleich braucht für Python wie für TypeScript eine Referenzlast; ohne sie ist er ein Messgerätausfall (Vorbedingung 3). **Grenze (Review Nr. 15):** Ruft die Last eines echten Werks die erste Funktion von A, ist die Vertragsprobe im Python-Lauf nicht prüfbar; die Last ist so gewählt, dass sie das umgeht |
| `tests/test_vorspann.py` | Generalprobe-Unit-Test: gepaarte Laufzeit gestellt (alpha gleich schnell) + „gesperrtes beta nie angefordert“ | Die Messung lief bisher ungestellt in einer echten Kammer gegen eine Unit-Last ohne `last_alpha`; der fehlende Wert wurde still übergangen. Genau das behebt die Runde. Die neue Zusicherung ist im Fall `nachbarfehler` leer wahr (Review Nr. 19) |
| `tests/test_t3_python_annahmen.py` | `GEPRUEFT` + 2 Einträge (`kern/py/verhalten.py::signaturen_lesen`, `::main`) mit Zeilennachweis der Weiche | Die Python-Sonde läuft nur in der Kammer eines Python-Werks, hinter `ist_typescript` in `verhaltensvergleich.py`. Die Zeilenangaben der Einträge sind veraltet: richtig ist nur `:195`; `_python_sonde` steht in Z. 217, die Weiche in Z. 246 (Review Nr. 18) |
| `tests/conftest.py` | `ts_kammer`: `pytest.fail` statt `pytest.skip` | Auftrag |

## 8. Reviewdurchgang und Umgang mit den Befunden

Ein Durchgang (`REVIEW.md`, Auftrag `REVIEW-AUFTRAG.md`). Ergebnis: **22 Befunde, 6 hoch, 9 mittel, 7 niedrig**.
- Bestätigt sind das Urteil, die S1-Zuordnung, die Schwächenzählung, die Nachspiel- und Regressionszahlen und die
  Kasse (`REVIEW.md` → „Geprüft und bestätigt“).
- Die Gutachterproben liegen unverändert in `review-proben/` (13 Kammerläufe nach Jobende, `git status` vorher und
  nachher leer).
- Jeden Befund habe ich an den Proben bzw. am Code nachgesehen, bevor ich ihn übernahm.
- Nach der Regel „ein Review, keine Fix-Kaskade“ baue ich keinen Code mehr. Code-Befunde werden Spezifikationen für
  die nächste Runde (`SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`).

| Nr | Schwere | Befund (kurz) | Umgang |
|---|---|---|---|
| 1 | hoch | Generatoren nur als `__iterator` verglichen: geänderte Ausgabe 0 Abweichungen | übernommen (Probe p1 gelesen). Spezifikation S-1; Offen Nr. 6 |
| 2 | hoch | Nebenwirkungen an den Eingaben nicht verglichen (in-place-Sortierung: 0) | übernommen (p2). S-2 |
| 3 | hoch | „x von y“ zählt Funktionen mit nur Fehleraufrufen als beobachtet | übernommen (p4). S-3 |
| 4 | hoch | kein `PYTHONHASHSEED`: 22 Fehlalarme, Ablehnung, 2 von 2 | übernommen (p5). S-4 |
| 5 | hoch | `@lru_cache` nicht eingewickelt: 16 von 16 „ungedeckt“, Ablehnung | übernommen (p12). S-5 |
| 6 | hoch | Deckung „dieselbe Eingabe je Muster“ praktisch unerreichbar (2 von 28) | übernommen (p7), Entscheidung 2 berichtigt. Offen Nr. 7 |
| 7 | mittel | Gegenprobe K2868 trennt Korpus nicht von Deckungsregel; „20 `~form`“ ist ein Sortierartefakt | Aussage zurückgezogen (§3). Getrennte Gegenprobe: S-7 |
| 8 | mittel | Ein Test deckt Abweichungen, die er nicht zusichert | übernommen (p6), §10 Nr. 2 berichtigt. S-6 |
| 9 | mittel | Deckung verloren bei Standardparametern und `export const` (0 Aufrufe) | übernommen (p10/p10b, p8). S-6 |
| 10 | mittel | Formvarianten nur aus dem ersten Lastbeispiel mit Leerzeichen; Korpus nicht aus `VERTRAEGE.md` | übernommen, §3 um die Grenze ergänzt. S-8 |
| 11 | mittel | Klassen nicht im Nenner; `nicht_eingewickelt` nicht im gespeicherten Urteil | übernommen, Aussage in §2 zurückgezogen. S-3 |
| 12 | mittel | Python-Module auf Wurzelebene übersprungen | übernommen. S-3 |
| 13 | mittel | Nachmessung nie mit echter Messung gelaufen, nicht im Verdrahtungsbeleg | übernommen (§4). S-9 |
| 14 | mittel | §4-Überschrift zu stark; Gegenrichtung (Annahme ohne Bestätigung) fehlt | Überschrift berichtigt. Rote Spezifikation um die Gegenrichtung erweitert und am Commit ausgeführt: **2 von 4 rot, beide Gegenproben grün**. Im Mechanismus gilt der Befund, in der Einordnung nicht: Philipps Auftrag sagt „vor jeder Laufzeitablehnung“ (§11) |
| 15 | mittel | `REF_PAAR` umgeht den Messausfall der Vertragsprobe | übernommen, §7 nennt die Grenze. S-10 |
| 16 | niedrig | TS-Pflichtfälle nicht am Commit gemessen | Aussage berichtigt (§3) |
| 17 | niedrig | S1-Nenner gemischt, R nicht genannt | berichtigt (§1) |
| 18 | niedrig | veraltete Zeilennachweise in `GEPRUEFT` | im Bericht vermerkt (§7); Korrektur im Code im nächsten Auftrag |
| 19 | niedrig | neue Zusicherung in `test_vorspann` teils leer wahr | vermerkt (§7). S-11 |
| 20 | niedrig | `laufzeitrisse` erkennt nur `\w`-Bereichsnamen | übernommen (p9). S-9 |
| 21 | niedrig | Zeitlimit am Kandidaten gilt als Messgerätausfall statt Inhaltsbefund | offen, nur gelesen. S-12 |
| 22 | niedrig | Einwickeln/Aufzeichnen: Tabellen, `partial`, xdist, eigene vitest-Konfiguration | offen, nur gelesen. S-12 |

**Sperren und Abweichungen des Reviewers, wörtlich in `REVIEW.md`:**
- eine Formatsperre („command parser limit or malformed executable payload“); das gespeicherte Skript hat er nicht
  ausgeführt;
- eine Sicherheitssperre („cannot restart, stop, or uninstall the gateway …“) auf ein nur lesendes Skript `r6.sh`.

Er hat danach **Teile derselben Daten auf anderem Weg gelesen** (`read_file`, `execute_code`) und das selbst als Verstoß
gegen „keinen anderen Weg suchen“ gemeldet. Einordnung: ein Verstoß gegen Linie 3. Er ist beim Reviewer geschehen,
gemeldet und nicht wiederholbar. Gelesen hat er nur Dateien, die im Ordner ohnehin veröffentlicht werden. Ich übernehme
aus diesem Teil keine Zahl, die nicht auch aus den veröffentlichten Belegen folgt. Der Auslöser in `r6.sh` ist
ungeklärt; das Skript enthält kein Wort zu Gateway, Neustart oder Stopp.

Eine Datei liegt außerhalb seines Schreibbereichs (`/tmp/rv02-32t8nzkt/app.py`, 35 Bytes). Sie bleibt liegen; Löschen
wäre eine eigene Handlung ohne Auftrag.

## 9. Sperren im Wortlaut

Kein Block der Ausführungsschicht in diesem Auftrag. Drei Befehle markierte der Sicherheitsscan; **der Nutzer gab sie
frei** (Einordnung: Freigabeabfrage):
- „[HIGH] Nested executable body could not be resolved …“ — `docker run … python -c …` und `node -e …` (Versionen der
  Kammerimages lesen);
- zweimal „[HIGH] Pipe to interpreter: cat | python3 …“ — `herzschlag.json` lesen.

Vorschlag: Lesebefehle über eine Pipe in einen Interpreter nicht dauerhaft freigeben. Ich lese künftig erst in eine
Datei.

Weitere Freigaben in der zweiten Hälfte: `cat | python3` auf `herzschlag.json` und `docker run … python -c` in der Kammer
— vom Nutzer freigegeben, kein Block. Die Sperren des Reviewers stehen in §8.

## 10. Eigene Entscheidungen

1. **Regel „S1 sauber“** (§1): Marker 0-mal ausgeführt und jeder Ausdruck, den die Normalversion rechnet, gleich
   gerechnet. Gemessen mit Leerzeichen, Tab und Zeilenumbruch, weil das die Formen sind, die die Entscheidung („soweit
   die Normalversion ihn rechnet“) sichtbar macht. Andere Weißraumzeichen (CRLF, NBSP) sind nur in R gemessen.
2. **Deckung verlangt dieselbe Eingabe und dasselbe Ergebnis.** Folge: Ein veralteter Zwischenspeicher ist nie
   deckbar. Das ist gewollt.
   - Berichtigt nach Review Nr. 6 und 8: Die Regel ist strenger als Grundsatz 11. Sie prüft zudem nicht, ob der Test das
     Ergebnis zusichert; ein Test, der `f('a')` nur nebenbei ruft, deckt mit.
   - Gemessen: Ein richtiger Test deckt 2 von 28 Abweichungen.
   - Die Entscheidung gehört Philipp (Offen Nr. 2).
3. **Beleg durch aufgezeichnete Aufrufe statt Quelltext**, und ein deckender Test, der im Aufzeichnerlauf nicht
   besteht, ist ein Messgerätausfall. Ohne diese Bedingung könnte das Instrument das Verhalten verändern und trotzdem
   urteilen.
4. **Nachmessung nur der gerissenen Bereiche, einmal, 5 je Seite.** Bestätigt heißt: Die zweite gepaarte Messung reißt
   dieselbe Grenze. Bei „nicht bestätigt“ bleibt die erste gepaarte Messung Grundlage des übrigen Urteils (Gewinne,
   Nischenmaß).
5. **Gesperrte Bereiche fordert die gepaarte Messung nicht an.** Sonst hätte ein dort fehlender Wert die ganze Messung
   ungültig gemacht, obwohl sie dort nichts entscheidet.
6. **Formvarianten mit Kappe 16 je Funktion** und nur für die erste Argumentliste. Das hält die Kammerzeit klein. Nicht
   gemessen ist, ob Varianten späterer Argumentlisten weitere Abweichungen fänden.
7. **Python-Eichproben mit eigener Referenzlast** (`REF_PAAR`). Im Lauf reicht der Vorspann die Last des Werks durch.

## 11. Eigene Fehler in diesem Auftrag

- **Umbauskript `deckung_umbau.py` brach mitten ab.** Ein Anker für den Organteil existierte nicht mehr, TS- und
  Python-Teil waren schon geschrieben. Den Organteil habe ich mit `deckung_umbau_organ.py` nachgezogen; alle drei Teile
  sind durch die Kammertests belegt.
- **`REF_PAAR` stand zuerst in der Fixture** (IndentationError beim Sammeln), und in der ersten Fassung rief die Last
  `bericht`. Damit wurde die Vertragsprobe zum Messausfall (`bau/diagnose_eichproben.py`). Beides ist behoben.
- **Erster voller Lauf am Arbeitsbaum: 11 rot** (`bau/ERSTLAUF-ALLE.txt`), darunter mein eigener Test, der ein nicht
  vorhandenes Hilfsmodul importierte. Alle 11 sind vor dem Commit behandelt, jeder mit Ursache in §7 bzw. hier.
- **Der Wächter meldete Kontextfüllung 67,5 % bei Runde 99.** Die Arbeit lief darum in mehreren Turns weiter; die
  Übergabe ist jeweils aktualisiert.

- **Prüfauftrag des Reviews ungenau.** Er gab Punkt 3 als Entscheidung 3 wieder („jeder Laufzeitriss“), nicht in
  Philipps Wortlaut („Bestätigungsmessung vor jeder Laufzeitablehnung“). Das Review hielt die Gewinnschwelle deshalb für
  eine Frage der Überschrift. Nach Philipps Wortlaut ist sie eine Lücke gegen den Auftrag.
- **Aussagen, die ich zurückziehe (Review):**
  - „20 `~form` und 0 `~rand`“: Sortierartefakt;
  - „Klassen stehen als `nicht_eingewickelt` im Urteil“;
  - „gemessen mit dem Stand, der committet wurde“ (TS-Pflichtfälle);
  - die Nenner in §1 (Marker 0 von 3; 12.206 von 16.166).

## 12. Offen für Philipp

1. **Methoden von Klassen beobachtet keine der beiden Sonden** (nur Funktionen der Modulebene bzw. `export function`).
   T4 ist ein fremdes Python-Werk mit 6.000–10.000 Zeilen, Klassen sind dort wahrscheinlich. Zu entscheiden: vor T4
   bauen, oder als benannte Grenze mit Enthaltung führen.
2. **Deckung je Abweichung macht echte Behebungen schwer deckbar.** Ein Test deckt nur, was er mit genau der Eingabe
   der Sonde festhält; Schwarm und Ankläger kennen diese Eingaben nicht.
   - Gemessen an K2868: Die drei Befundklassen-Tests decken jetzt keine der Abweichungen mehr, auch nicht die
     beabsichtigte Behebung `'a'` → SyntaxError.
   - Vorschlag zur Entscheidung: die ungedeckten Eingaben dem Ankläger oder dem Kandidaten als Auftrag zurückgeben
     („Test für `ausdruck('a')` fehlt“), statt nur abzulehnen.
3. **T3-Stand im Masterprompt:** „Lauf 38: 4 von 5 = 80 %“ ist nach Entscheidung 1 zu korrigieren auf 3 von 5 = 60 %
   (Lauf 37: 2 von 5 = 40 %). Das versiegelte Kriterium S1 (`KRITERIEN-v1.md`) prüft nur den Marker; eine neue
   Versiegelung mit Weißraum wäre Eure Entscheidung.
4. **K3044 akzeptiert Tab, K2868 nicht.** Beide weisen den Zeilenumbruch ab. Sollen Tab und Zeilenumbruch gleich
   behandelt werden, oder gilt die Normalversion Zeichen für Zeichen?
5. Die Nachmessung in der Generalprobe hat keinen eigenen Laufweg-Test (§4).
6. **Die Python-Sonde vor T4 nachbessern** (Review Nr. 1–5, 11, 12; §2). Ohne das ist T4 gegen „schneller, aber falsch“
   bei Generatoren, Nebenwirkungen an Eingaben und nicht annotierten Funktionen weiter ungeschützt. Zugleich würde die
   Sonde verhaltensgleiche Beschleunigungen ablehnen (Hash-Reihenfolge, `@lru_cache`).
7. **Deckungsregel** (Review Nr. 6): Gilt „dieselbe Eingabe und dasselbe Ergebnis je Muster“? Gemessen deckt ein
   richtiger Test damit 2 von 28 Abweichungen. Behebungen auf dem Lastpfad sind so praktisch nicht annehmbar; das
   gefährdet die Torzeile „Schwächen ≥ 80 %“.
   - Alternativen: Deckung je Eingabe ohne Muster, oder eine Verfälschungsprobe (der Test muss fallen, wenn das
     aufgezeichnete Ergebnis verfälscht wird).
8. **Gewinnschwelle der Nische schnell:** in beiden Richtungen bestätigen (vor Ablehnung und vor Annahme)? Das ist Teil
   von Grundsatz 14; es gibt dazu zwei rote Spezifikationen.
