# Behebungsrunde 5 vor T4: nicht abgenommen — die Gegenproben der Runde halten, aber an 0c2f058 sind zwei Messfehler derselben Klasse gemessen, die vor T4 behoben sein müssen (R6-1, R6-4)

Stand 2026-09-24. **Biotop-Modellgeld 0,00 €** (`KASSE.md`). Kern-Commit **`0c2f058`** auf `43b8fad` (`COMMIT-STAT.txt`,
`KERN-COMMIT.patch.txt`). Ein Reviewdurchgang (`REVIEW.md`, §11).

**Auftrag** (Philipp, 24.09., Entscheidungen Chat-Claude zum Review 04): „Runde 5 schließt Klassen, nicht Fälle.“
1. Vollständigkeitsprüfung nach jedem Erfassen eines Objekts; ein fehlendes Datenattribut ist eine gezählte Enthaltung;
   `os.PathLike` wird als Wert geführt.
2. Festhalten heißt: eine Zusicherung fällt.
3. Ein Sondenausfall trifft nur die betroffene Funktion; ersetzt werden nur echte Iteratoren.
4. Kappe der Verfälschungsläufe: zurückstellen mit Grund, gemessen in T4-Größe.
5. Verdrahtung über ein Register; das Tor-4-Skript ruft die Torzeile „Schwächen“; Normalvergleich einer Altlast über
   den Verhaltensvergleich.
6. Der Vorspann verweigert den Lauf ohne Stufe 2; die Stufe-2-Lasten werden bemessen, bis `eingang` nicht mehr sperrt.
7. Lastaufrufe tragen die Formmerkmale ihrer Eingabe.
8. Dieselbe Stufe für Eichproben, Toleranz und gespeicherte Maße; eigene Tests werden nach Testkennung einschließlich
   Parametrisierung ausgeschlossen; das Nachspiel läuft in der Regression als echter Durchlauf.

Vorweg (§0): Runde 4 war noch nicht veröffentlicht. Ihr Bericht ist aus den Belegen gefüllt und jetzt veröffentlicht.

**Ergebnis:**
- **Nicht abgenommen.** An `0c2f058` sind zwei Messfehler gemessen, die T4 gefährden; beide sind als rote
  Spezifikationen gefasst, keiner ist nachträglich gebaut (ein Review, keine Fix-Kaskade).
  - **R6-1 (Hinweis Philipp):** Bei unvollständiger Erfassung enthält sich der ganze Vergleich statt nur der betroffenen
    Beobachtung. Durch `aegis.pruefen` gemessen: Eine richtige Behebung plus eine unveränderte Funktion, die ein
    `StringIO` liefert, wird zurückgestellt; ohne diese Funktion überlebt sie (`spez/SPEZ-R6-LAUFWEG.txt`).
  - **R6-4 (eigener Befund nach dem Commit):** Ein Test mit `assert f(1) == 3` hält nichts fest. pytest meldet
    umgeschriebene Zusicherungen ohne Anführungszeichen ohne das Präfix „AssertionError:“, und die neue Regel verlangt es.
    Rot in 3 von 3 Fällen (Zahl, Liste, Wahrheitswert), die Gegenproben 2 von 2 grün (`spez/SPEZ-R6-4.txt`). Folge in
    der T4-Größen-Messung: Für 5 von 8 geänderten Funktionen hält kein Test
    fest.
- **Die Fälle aus Review 04 sind geschlossen** (Vorher/Nachher, 27 Fälle): 9 von 27 grün an `43b8fad`
  (Kontrollen und die schon gebaute 60-s-Grenze), 27 von 27 an `0c2f058`. Von den 18 roten Fällen scheitern
  15 am Verhalten und 3 an einer fehlenden Schnittstelle.
- **Gegenprobe Entscheidung 1 der Runde 4 an `0c2f058`:** K2904 überlebt in 3 von 3 Nachspielen (`planung`-Quote
  0,384 … 0,415), K3091 in 3 von 3
  (0,376 … 0,420), alle Gewinne klar. `eingang` war in
  0 von 6 Nachspielen gesperrt (Runde 4: 3 von 6). K2868 wird abgelehnt: 24 von 40
  Abweichungen ungedeckt (Weißraum und führende Null), 16 gedeckt, wie in Runde 4. 7 von 7 Belegen tragen den Commit
  `0c2f058`, sauberen Arbeitsbaum, unveränderte T3-DB und 0 Modellaufrufe.
- **Regression an `0c2f058`:** 598 bestanden, 2 übersprungen, 0 rot (JUnit 600 Fälle,
  0 Fehlschläge, 0 Fehler), 2458 s. Verdrahtung: 23 von 23
  Organen, Register 10 von 10 Kanten, Tor-4-Zeile „Schwächen“ an A1 doppelt geprüft und behoben, das Nachspiel im
  Verdrahtungstest urteilt wie der Lauf (überlebt, Stufe 2), 0,00 €.
- **Stufe 2, `eingang`:** Mit 240 Wiederholungen sperrte es in 0 von 8 Rauschmessungen (mit 60: 3 von 8); die Stichprobe
  dauert 170,5 statt 35,1 ms. 240 ist nach der Sperrzahl gewählt, nicht nach einer Regel der Dauer (R6-3, Offen Nr. 3).
- **Entscheidung 4 ist nicht belegt.** Gemessen ist der Bedarf eines breiten Kandidaten, 8 geänderte Funktionen:
  35 Verfälschungsläufe, bei Kappe 24 also 11 ausgelassen. Das Werk hat aber nur
  126 Zeilen, T4 dagegen 6.000–10.000. Das Urteil beider Messläufe ist wegen R6-4 nicht verwertbar.
- **Biotop-Modellgeld 0,00 €**; kein Lauf.

## 0. Abschluss der Runde 4

- Der Bericht der Runde 4 trug noch Platzhalter; im Prüfkanal lagen nur Zwischenberichte.
- Gefüllt per Skript (`bau/r4_bericht_fuellen.py`), die Sperrwortlaute nur aus den Belegdateien.
- Die Review-Proben liegen jetzt in `biotop-vor-t4-04/review-proben/` (13 Dateien), dazu die Spezifikationen R5-1 … R5-14.
- Veröffentlicht unter `laeufe/biotop-vor-t4-04`: 103 von 103 Dateien über HTTPS bytegleich, Ordnerprüfsumme
  `c02d0dce9ad5996215f0d723a006a4ae2c0495ab2e051a7d0a4d73e7988c3f12` (`bau/VEROEFFENTLICHUNG-R4.txt`).

## 1. Vollständigkeitsprüfung (Entscheidung 1)

**Umsetzung (Python, `kern/py/verhalten.py`).** `kan()` erfasst jetzt alle Datenattribute eines Objekts: `__dict__` und
die Slots der ganzen Klassenhierarchie. Die Slots liest sie über die Member-Deskriptoren der in Python definierten
Klassen, also unter ihren gespeicherten Namen, verschleierte Namen (`_Konto__stand`) eingeschlossen. Nach jedem Erfassen
prüft `_pruefen_vollstaendig` die Erfassung gegen eine unabhängige Aufzählung: `object.__getstate__`, den Zustand, den
Python selbst zum Kopieren liest. Als unvollständig zählen außerdem:
- ein Iterator-Objekt des Werks (seine Elemente werden nicht gelesen);
- ein nach `ITER_KAPPE` gekappter Iterator;
- ein Iterator innerhalb der Beobachtung;
- ein Objekt, das nur die Standarddarstellung mit Adresse hat;
- ein Objekt jenseits der Tiefe 12;
- Unterklassen von `str`, `int`, `list`, `dict` usw., die eigene Attribute tragen.

Die Funktion steht dann in `unvollstaendig` mit ihrem Grund.

Weitere Änderungen an `kan()`:
- `os.PathLike` wird über `os.fspath` als Wert geführt. Als Argument gilt ein Pfad nicht mehr als veränderlich: kein
  Schnappschuss und keine Mutation seiner Zwischenspeicher mehr.
- Bytes werden ganz geführt (vorher 400 Zeichen), die Darstellung ungekürzt (vorher 200 Zeichen); `knapp()` kürzt den
  ganzen Text mit Prüfsumme.
- `deque` und `object()` werden als Wert geführt.
- Beispiele (`pack`/`unpack`) führen auch Slots.

**TypeScript (`kern/ts/kanon.mjs`, `verhalten-runner.mjs`).** Nach dem Erfassen eines Objekts prüft der Kanon, ob etwas
fehlt, das `Object.keys` nicht liefert:
- nicht aufzählbare Eigenschaften und Symbol-Eigenschaften;
- private Felder (`#x`), erkannt an einer Felddeklaration im Quelltext der Klasse;
- eingebaute Objekte ohne erfassbare Schlüssel.

`RegExp`, `URL`, `ArrayBuffer` und typisierte Arrays sind Werte. Der Runner meldet jede solche Lücke als
`unvollstaendig`. `ITER_KAPPE` ist in beiden Sprachen von 50 auf 1000 gestiegen (§14 Nr. 3).

**Urteil (`organe/verhaltensvergleich.py`, `aegis.py`).**
- Eine unvollständig erfasste Funktion (an Vorgeneration oder Kandidat) zählt nicht als beobachtet. Ihre Enthaltung
  steht mit Grund in `enthaltungen`.
- Wäre das Urteil sonst tragfähig, enthält sich der Verhaltensvergleich (`grund_art: unvollstaendig_erfasst`), und
  `aegis.pruefen` stellt den Kandidaten zurück. Gezählt wird das im Neutralzähler; es gibt keine Annahme und keinen
  Gedächtniseintrag.
- Ein Urteil mit ungedeckter Abweichung bleibt eine Ablehnung.
- „0 Abweichungen, tragfähig“ ist bei unvollständiger Erfassung also nicht mehr möglich.

**Gegenproben** (Fälle aus Review 04, am Organ `verhaltensvergleich.pruefen` in der echten Kammer; `test_v1_*`):

| Review 04 | Fall | an `43b8fad` | an `0c2f058` | Gegenprobe |
|---|---|---|---|---|
| Nr. 2 | p22: Basisklasse mit Slot, `buchen` ändert ihn | 0 Abweichungen, tragfähig | abgelehnt, `>args`-Abweichungen, vollständig erfasst | p22k (eigener Slot): abgelehnt; umgeschrieben (gleiche Wirkung): 0 Abweichungen, tragfähig |
| Nr. 3 | p21: verschleierter Slot `__stand` | 0 Abweichungen, tragfähig | abgelehnt, vollständig erfasst | wie oben |
| Nr. 5 | p18c: Elemente eines Iterator-Objekts geändert | 0 Abweichungen, tragfähig | Enthaltung „unvollständig erfasst“ (`leser`) | p18ck als Generator: geurteilt, abgelehnt |
| Nr. 5 | Iterator-Kappe (Änderung jenseits der Kappe) | tragfähig | Enthaltung „gekappt“ | — |
| Nr. 10 | `ablage()` liefert einen anderen Pfad | inhaltslos, tragfähig | abgelehnt, vollständig erfasst | derselbe Pfad: tragfähig |

Die Werte der Spalte „an `43b8fad`“ stammen aus Review 04 bzw. aus Vorher/Nachher (§9).

- **Nachweisart:** Die Fälle sind Organ-Nachweise. Durch `aegis.pruefen` belegt sind der Zweig „Enthaltung →
  zurückgestellt“ (§4, gleicher Zweig) und ein unbeabsichtigter Fall in `TEILLAUF-1`: `zahlen` gekappt, zurückgestellt.
- **Grenzen, gelesen:** Weiter blind bleibt Zustand außerhalb der Datenattribute, also Closures, Klassenattribute,
  globale Modulvariablen und C-Erweiterungen mit eigener Darstellung ohne Adresse. In TypeScript werden private Felder
  nur an der Felddeklaration im Quelltext erkannt, Closures gar nicht.
- **Befund gegen den eigenen Bau (Philipp, 24.09.):** Die Enthaltung gilt hier für das ganze Urteil. Das widerspricht
  Entscheidung 3 und schafft denselben Totalausfall wie Review 04 Nr. 4: Ein einziges schwer erfassbares Objekt in einem
  geänderten Modul — etwa eine unveränderte Funktion, die ein Datei-Objekt liefert — stellt jeden Kandidaten zurück, der
  dieses Modul berührt, auch wenn er die Funktion nicht geändert hat.
  - Enthalten muss sich nur die betroffene Beobachtung; der übrige Vergleich urteilt.
  - Nach „ein Review, keine Fix-Kaskade“ ist das nicht mehr in diese Runde gebaut, sondern als **rote Spezifikation vor
    T4** gefasst (R6-1, `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`).
  - Belegt an `0c2f058` (`spez/SPEZ-R6-UNIT.txt`): Am Organ mit gestellter Sonde enthält sich der ganze Vergleich
    (`unvollstaendig_erfasst`), obwohl nur die unveränderte Funktion `g` schwer erfassbar ist und keine Beobachtung
    abweicht. Die zwei Gegenproben sind grün: ohne schwer erfassbares Objekt geurteilt; eine echte ungedeckte Abweichung
    lehnt weiter ab.
  - Laufweg-Fassung durch `aegis.pruefen` (`spez/test_spez_r6_laufweg.py`, echte Kammer): rot an `0c2f058` (`spez/SPEZ-R6-LAUFWEG.txt`, 1 rot, 1 grün): Mit `puffer` wird der Kandidat zurückgestellt, „Verhaltensvergleich enthält sich … unvollständig erfasst (probewerk.werk.kern:puffer: StringIO: Iterator-Objekt …) … (8 von 9 Funktionen beobachtet)“. Die Gegenprobe ohne `puffer` überlebt.

## 2. Festhalten heißt fallende Zusicherung (Entscheidung 2)

**Umsetzung.**
- **Python:** Der Aufzeichner wertet einen Testfehlschlag nur dann als `fail`, wenn der pytest-Bericht eine fallende
  Zusicherung in der Testdatei selbst meldet: Absturzstelle (`reprcrash.path`) ist die Testdatei, Meldung
  `AssertionError…` oder `Failed…` (`pytest.raises` ohne Ausnahme, `pytest.fail`). Jede andere Ausnahme ist `fehler`
  und hält nichts fest, auch ein `assert` im Werkcode oder eine Ausnahme aus Werkcode, dem ein verfälschter Wert
  gereicht wurde.
- **Vorprobe** (`proben/VORPROBE-E2.txt`, lokal und in der Kammer mit pytest 8.3.3): 5 von 5 Fehlschlagarten melden
  Stelle und Art wie angenommen.
- **TypeScript (`deckung.mjs`):** `fail` nur, wenn alle Fehler `AssertionError` sind und die erste Werkstelle im Stapel
  unter `tests/` liegt.

**Probe (x3, durch `aegis.pruefen`):** Die Idempotenz-Zusicherung `normieren(normieren("a\tb c")) == normieren("a\tb c")`
hielt an `43b8fad` das Merkmal `tab` fest, der Tab-Rückschritt überlebte (Review 04 Nr. 1). An `0c2f058` wird er
abgelehnt; `festhaltend` für `tab` ist leer.
- **Gegenprobe x3k** (ohne die Zeile): abgelehnt.
- **Modul:** `test_f2_zusicherung_faellt_am_ort_und_an_der_art` mit den gemessenen Meldungen (6 Fälle).
- **TypeScript:** Der positive Fall (Zusicherung fällt → hält fest) ist durch den vorhandenen Test
  `test_deckungsaufzeichner_in_der_kammer_je_abweichung[ts-True]` belegt. Einen TypeScript-Fall „Werk-Ausnahme hält
  nicht fest“ gibt es nicht (Offen Nr. 3).


**Befund nach dem Commit (R6-4, eigener Befund):** Die Regel erkennt umgeschriebene Zusicherungen ohne einfache
Anführungszeichen nicht.
- Ursache: pytest kürzt dort „AssertionError: “ aus der Meldung weg (`ExceptionInfo._striptext`). Gemessen in pytest
  8.3.3 in der Kammer und 9.1.1 lokal (`proben/VORPROBE-E2b.txt`).
- `assert f(1) == 3`, `assert f(1) == [3, 2, 1]` und `assert f(1)` halten deshalb nichts fest. `assert f(1) == 'a_b'`
  hält fest.
- `VORPROBE-E2` hatte nur Zusicherungen mit Text geprüft; das war eine zu enge Stichprobe (§14 Nr. 9).
- Die rote Spezifikation `spez/test_spez_r6_4.py` führt echtes pytest aus und prüft `_zusicherung_faellt` des Commits:
  rot in 3 von 3 Fällen (Zahl, Liste, Wahrheitswert); grün in 2 von 2 Gegenproben (Text hält, Werk-Ausnahme hält nicht).
- Folge: Für Werke, deren Tests Zahlen oder Listen zusichern — T4 ist ein Python-Werk —, wird jede Abweichung, die nur
  solche Tests decken, abgelehnt statt gedeckt. Die T4-Größen-Messung zeigt das (§4).

## 3. Sondenausfall nur der betroffenen Funktion (Entscheidung 3)

**Umsetzung (Python).**
1. Vor jeder Bereichslast legt die Sonde eine Vorlage an: einen Kindprozess (`os.fork`) mit dem Zustand vor der Last.
2. Bricht die Last unter der Sonde ab, prüft die Vorlage in eigenen Kindprozessen, ob die Last ohne jeden Eingriff der
   Sonde läuft.
3. Wenn ja, sucht sie per Halbierung die Funktion, deren Einwicklung allein den Abbruch auslöst. Das sind etwa
   1 + 2·log₂ n Lastläufe je Auslöser, höchstens sechs Auslöser.
4. Die gefundene Funktion steht in `sonde_ausfall` und wird durchlässig (keine Beobachtung, kein Eingriff).
5. Der Wirt beobachtet die Vorgeneration danach frisch, mit denselben durchlässigen Funktionen auf beiden Seiten. Die
   Beobachtungen der Funktion fallen auf beiden Seiten weg, ihre Enthaltung heißt „Sondenausfall: …“, und der Lauf geht
   weiter.

Sonderfälle:
- Bricht die Last auch ohne Sonde ab, ist das Verhalten des Werks (`last_ohne_sonde`) und wird wie bisher beobachtet.
- Scheitert die Eingrenzung, enthalten sich alle Funktionen dieser Last. Das wird nie als Verhalten des Werks gewertet.

**TypeScript.** Die Sonde grenzt nicht selbst ein: Bricht eine Last an der Vorgeneration ab, enthalten sich die
Funktionen, die diese Last rief (`last_aufrufe`). Ohne diese Angabe bleibt es beim Messgerätausfall wie in Runde 4.

**Nur echte Iteratoren.** Ausgelesen und ersetzt werden nur:
- Generatoren;
- Iteratoren aus `builtins`, `itertools` und `collections` ohne öffentliche Datenattribute, außer `groupby`, dessen
  Gruppen am Ausgangsiterator hängen.

`csv` steht nicht mehr in der Liste. `csv.DictReader` bleibt also ein Objekt und wird als Iterator-Objekt unvollständig
erfasst (§1).

**Proben (Organ, echte Kammer; `test_a3_*`):**
- **Zählerlast:** Die Last verlässt sich darauf, dass `naechste()` zweimal hintereinander um eins zählt. Die Sonde ruft
  jede Funktion mehrfach auf, darum bricht die Last unter der Sonde ab. An `43b8fad` war das ein Messgerätausfall für
  den ganzen Kandidaten. An `0c2f058` enthält sich `naechste` („Sondenausfall“), und die Änderung an `doppel(3)` wird
  gesehen.
- **Gegenprobe:** Bricht die Last auch ohne Sonde ab, gibt es keinen Sondenausfall; `doppel` wird gesehen.
- **q1 (`DictReader`, Review 04 Nr. 4):** Die Last liest `fieldnames` und läuft; `doppel` wird gesehen, `lies` ist
  unvollständig erfasst.
- **TypeScript-Weg:** ohne eigene Probe (Offen Nr. 3).

## 4. Kappe der Verfälschungsläufe (Entscheidung 4)

**Umsetzung.** Hängt jede ungedeckte Abweichung an einer Verfälschungsprobe, die die Kappe ausgelassen hat, enthält sich
der Verhaltensvergleich (`grund_art: verfaelschungskappe`). Der Grund nennt Zahl und Kappe. `aegis.pruefen` stellt den
Kandidaten zurück, gezählt im Neutralzähler. Bleibt auch nur eine Abweichung ohne ausgelassene Probe ungedeckt, lehnt er
ab wie bisher.

**Probe (durch `aegis.pruefen`, `test_k4_*`):**
- Richtige Behebung mit Tests je Formvariante, Kappe 2: zurückgestellt, Grund „… ausgelassenen Verfälschungsproben
  (Kappe 2 …)“, `ausgelassen` > 0.
- Mit Kappe 24: überlebt.
- **Gegenprobe:** Ohne passenden Test lehnt er auch mit Kappe 2 ab.

**Messung in T4-Größe** (`proben/T4-GROESSE.txt`, `proben/t4_groesse.py`):
- **Aufbau:** Ein Python-Prüfwerk aus 6 Modulen mit 30 Funktionen
  (126 Zeilen). Der Kandidat ändert 8 Funktionen in einem Zug; für jede
  bringt das Werk Soll-Tests je Formvariante mit, die an der Vorgeneration rot sind.
- **Messung durch `aegis.pruefen`** in der echten Kammer (Modell und Laufzeit gestellt), einmal mit Kappe 24 und einmal
  ohne:
  - Kappe 24: Bedarf 35 Verfälschungsläufe, davon 24 gelaufen und
    11 ausgelassen; 30 Kammerläufe, 30,3 s;
    Urteil abgelehnt.
  - Ohne Kappe: 35 Verfälschungsläufe, 41 Kammerläufe,
    42,9 s; Urteil abgelehnt.
  - Beide Male 324 Abweichungen, „15 von 15 beobachtet“.
- **Nicht verwertbar für die Kappe.** Die Diagnose (`proben/T4-DIAGNOSE.txt`, ohne Kappe) zeigt: Für
  5 von 8 geänderten Funktionen (m0:m0_f2, m0:m0_f4, m1:m1_f1, m2:m2_f2, m2:m2_f4), die Zahlen und Listen
  liefern, hält kein Test fest. Deren Tests sind Zusicherungen ohne Anführungszeichen (R6-4). Dass mit Kappe 24 abgelehnt
  statt zurückgestellt wird, liegt an diesen Abweichungen, die ohnehin ungedeckt bleiben, nicht an der Kappe.
- **Belastbar ist nur der Bedarf:** 35 Verfälschungsläufe für einen Kandidaten mit
  8 geänderten Funktionen, etwa 1 s je Lauf in diesem kleinen Werk. Ein T4-Werk hat
  6.000–10.000 Zeilen und längere Testläufe; die Kappe ist dort erneut zu messen, nach R6-4 und am echten T4-Werk
  (Offen Nr. 4). **„Gemessen an einem Kandidaten in T4-Größe“ ist damit nicht erfüllt**, nur die Breite des Kandidaten
  ist nachgebildet.

## 5. Register und Tor-4-Skript (Entscheidung 5)

**Register (`kern/register.py`).** Zehn Einträge, je Funktion mit Aufrufer und Laufphase:
- Annahmepfad: `aegis.pruefen`, `masseichung.anwenden`, `verhaltensvergleich.pruefen`, `messgeraet.laufzeit_gepaart`;
- Vorspann: `eichung.rauschmessung`, `eichung.laufzeit_einmal`, `masseichung.eichen`, `eichproben.proben`;
- `tor4.ausfuehren` aus der Befehlszeile;
- `gegenzeugen.torzeile_schwaechen` aus dem Tor-4-Skript.

Der Verdrahtungstest zeichnet zusätzlich die Kernmodule des Registers auf (`gegenzeugen`, `tor4`, `messgeraet`). Er
verlangt jede Kante `funktion ← aufrufer @ phase` im echten Lauf über die Befehlszeile; gerufen von anderswo oder in
einer anderen Phase zählt nicht. Die Gegenproben des Werkzeugs laufen als Unit (`test_register_*`, 2 Tests):
- fehlende Kante: gemeldet;
- falsche Phase: gemeldet;
- falscher Aufrufer: gemeldet;
- richtige Kante: nicht gemeldet.

**Tor-4-Skript (`biotop/tor4.py`, Befehl `biotop tor4 <lauf> --altlasten <liste.json>`).** Das Skript berechnet die
Torzeile „Schwächen“ mit doppelter Prüfung je Altlast:
- **(a) Schwäche weg:** Der Gegenzeuge der Altlast (ein Test aus der Liste) läuft in der Kammer am Endstand. Der Endstand
  ist die letzte angenommene Generation, aus Lazarus mit Prüfsumme wiederhergestellt.
- **(b) Normalvergleich für T4:** das Verhalten der Vorgeneration über den Verhaltensvergleich. Dazu dienen die
  aufgezeichneten Urteile aller angenommenen Kandidaten, die den Bereich der Altlast berühren.
  - Jede Abweichung zählt als verändert, außer sie ist durch einen unabhängigen Test aus der Altlastenliste gedeckt.
  - Eine verhaltensändernde Altlast ohne solchen Test ist nicht beurteilbar, also nie behoben.
- Das Ergebnis steht im Protokoll (`tor4.schwaechen`).
- Die übrigen Zeilen von Tor 4 berechnet das Skript nicht; es nennt sie als „nicht berechnet“ und nie als erfüllt.
- **Auf der Liste vor T4 (Philipp, 24.09.):** Das Tor-4-Skript berechnet jede Zeile, die aus der Datenbank berechenbar
  ist; die meisten Berichtsfehler in T3 waren Torzeilen von Hand. Gefasst als rote Spezifikation R6-2
  (`spez/test_spez_r6_unit.py`, rot an `0c2f058`). Neben „Schwächen“ sind nach meiner Einteilung 10 der übrigen 13
  Zeilen aus der Datenbank berechenbar (je Zeile im nächsten Auftrag nachzuweisen):
  - Generation minus eins, Generation 0, Kein Rückschritt, Halluzinationsprobe;
  - Verhaltensvergleich, Doppelungsanteil, Immunisierung, Neutralzähler;
  - Verbundausfall, Sättigung oder Budgetabbruch.
  Nicht aus der Datenbank berechenbar sind Aufnahme (Werk und Altlastenliste prüfen), Verdrahtung (Regression),
  Reviewdurchgang und Zwischenbericht.

**Laufweg (Verdrahtungstest):**
- Nach der Freigabe läuft `biotop tor4 1 --altlasten ALTLASTEN.json`. Das Drahtwerk trägt eine Altlast A1: toter Code in
  `alpha`, den der Schwarm im Lauf entfernt.
- Zugesichert: A1 ist weg und das Verhalten unverändert (beide Prüfungen gemessen), die Zeile meldet A1 als behoben, und
  das Register hat 10 von 10 Kanten.
- Grün in `TEILLAUF-3a` (6 von 6, 1719 s) und in der Regression (§9).

## 6. Vorspann und Stufe 2 (Entscheidung 6)

- **Umsetzung:** Fehlt die Vergleichslast Stufe 2, verweigert der Vorspann den Lauf vor jeder Messung: „Vergleichslast
  Stufe 2 fehlt …“. Einen stillen Rückfall auf Stufe 1 gibt es im Vorspann nicht mehr. Die Grenze von 60 s je
  Kammerlauf bleibt.
- **Proben (Unit, `test_s6_*`):**
  - ohne Stufe 2: verweigert, keine Messung;
  - gestellter Kammerlauf von 61 s: verweigert;
  - Gegenprobe mit 59 s: der Vorspann läuft und trägt `laufzeit_stufe` 2.

**Bemessung der `eingang`-Last** (`proben/STUFE2-EICHUNG.txt/.jsonl`, `proben/stufe2_eichung.py`):
- Instrument: dieselbe Regel wie im Vorspann (`eichung.rauschmessung` mit `eichung.laufzeit_einmal`).
- Ort: die Vorgenerationen von K2904 (Lauf 37) und K3091 (Lauf 38), Code-Kopie `43b8fad`.
- Ablauf: je Variante 4 Rauschmessungen je Vorgeneration, also 8; die Varianten liefen abwechselnd.
- Die T3-DB war vorher und nachher gleich.

| `eingang`-Wiederholungen | Rauschmessungen mit Sperre | größte Toleranz `eingang` | längster Kammerlauf |
|---|---|---|---|
| 60 (Stand Runde 4) | 3 von 8 | 1,884 | 11,6 s |
| **240** (gewählt) | **0 von 8** | 1,155 | 12,3 s |
| 480 | 0 von 8 | 1,208 | 13,7 s |

**Auftragsfehler, benannt (Philipp, 24.09.):** „bemessen, bis `eingang` nicht mehr sperrt“ richtet die Last nach dem
Ergebnis. Ob 240 nach Maß gewählt ist, zeigt nur die Dauer der Stichprobe. Also die Stichprobendauer je Variante: ein
Wert ist der Median aus fünf Durchläufen der `eingang`-Last in einem Kammerlauf, je Rauschmessung fünf Werte, je
Variante 8 Rauschmessungen, also 40 Werte (`proben/STUFE2-EINGANG-DAUER.txt`, aus `STUFE2-EICHUNG.jsonl`):

| `eingang`-Wiederholungen | Stichprobendauer: Median (Spanne), n = 40 | relative Spannweite je Rauschmessung | Sperren |
|---|---|---|---|
| 60 (Stand Runde 4) | 35,1 ms (29,3 … 71,2 ms) | 0,53 … 0,92 | 3 von 8 |
| **240** (gewählt) | **170,5 ms** (141,3 … 189,1 ms) | 0,05 … 0,21 | 0 von 8 |
| 480 | 317,1 ms (299,1 … 364,5 ms) | 0,03 … 0,19 | 0 von 8 |

Zum Vergleich, ebenfalls Stufe 2 und unverändert:
- `zahlen` 18,9 ms (Spannweite 0,05 … 0,39, 0 Sperren in 24 Messungen);
- `tarife` 96,0 ms (0,06 … 1,42 — ein Ausreißer, 0 Sperren);
- `bericht` 100,5 ms;
- `planung` 346,0 ms.

Stufe 1 (Rauschmessung der Läufe 37/38, `t3.db` nur gelesen): `eingang` 2,41 bzw. 2,86 ms, die übrigen Bereiche 2,9 bis
12,1 ms.

**Einordnung, gerechnet, nicht als Regel gemessen:**
- Mit 60 Wiederholungen war die `eingang`-Stichprobe an Stufe 2 mit 35 ms die kürzeste neben `zahlen` und streute am
  stärksten.
- 240 Wiederholungen heben sie auf 170 ms, in dieselbe Größenordnung wie `bericht` und `tarife`.
- Die Last steigt also mit ihrer Dauer, und die Spannweite fällt mit ihr, von 0,53 … 0,92 auf 0,05 … 0,21.
- Ein Maß „nach Dauer“ gibt es im Kern aber nicht. Stufe 1 wählte die Wiederholungen „gemessen“ bis „einige zehn
  Millisekunden“ (Kopf der Stufe-1-Last); an dieser Formulierung gemessen hätten auch 60 Wiederholungen (35 ms) gereicht.
- `zahlen` sperrt mit 18,9 ms nicht; die Dauer allein erklärt die Sperren also nicht.
- **Damit ist 240 nicht nach Maß gewählt, sondern nach der Sperrzahl.** Die einzige festgeschriebene Regel ist die der
  Stufe 1 („einige zehn Millisekunden“), und nach ihr hätten schon 60 Wiederholungen gereicht. Eine vorab festgelegte
  Regel nach Dauer, für jede Bereichslast gleich, fehlt. Sie ist R6-3; den Wert entscheidet Philipp (Offen Nr. 5). Die
  Nachspiele dieser Runde laufen mit 240.

Ob `eingang` an `0c2f058` in den Nachspielen noch sperrt, zeigt §9.

## 7. Formmerkmale der Lastaufrufe (Entscheidung 7)

- **Umsetzung:** Der Lastaufruf trägt die Formvarianten-Merkmale seiner eigenen Eingabe, in Python (`wickeln`) wie in
  TypeScript (`__vvAufzeichnen`). Vorher galten Lastaufrufe immer als gewöhnlich.
- **Folge:** Eine Abweichung an einem Lastaufruf mit Tab-Eingabe braucht einen Test, der `tab` festhält. Ebenso trägt
  ein kleingeschriebener Text `klein` und ein Text mit Großbuchstaben `gross`. Die Deckung der Lastaufrufe ist damit
  strenger als in Runde 4.
- **Probe (durch `aegis.pruefen`, `test_l7_*`):**
  - Die Last ruft `normieren("wort\twort wort")`, der Kandidat gibt Tab-Text unverändert zurück, und die Tests enthalten
    keinen Tab: abgelehnt.
  - Die ungedeckten Lastabweichungen tragen `tab`.
  - An `43b8fad` deckte der gewöhnliche Test sie (Vorher/Nachher §9).
  - Eine Gegenprobe mit deckendem Tab-Test gibt es für Lastaufrufe nicht, nur für die Formvarianten (H1-Gegenprobe der
    Runde 4). Das ist eine Lücke (§14 Nr. 5).

## 8. Stufe, eigene Tests, Nachspiel (Entscheidung 8)

**Dieselbe Stufe (Review 04 Nr. 14, 15).** An der Stufe der Laufzeitgrenze, also Stufe 2, messen jetzt:
- Ausgangsmessung und Eichproben des Vorspanns (`tausch['_referenzlast_laufzeit']`);
- das eingefrorene Ausgangsmaß (`mass_einfrieren`);
- die Generalprobe;
- die Einzelmessung in `aegis.pruefen`;
- `kurve_nachrechnen`.

Gespeicherte Maße und Maß tragen `laufzeit_stufe`. Das Nachspiel übernimmt die Rauschmessung der Stufe 2 aus dem
Nachweis, wenn dieser sie trägt (neue Läufe); für die Läufe 37/38 misst es sie wie bisher selbst.
- **Unit durch `aegis.pruefen`** (gestellte Messung): beide Messungen erhalten die Stufe-2-Last, das gespeicherte Maß
  trägt `laufzeit_stufe` 2.
- **Laufweg:** Der Verdrahtungstest sichert zu, dass jedes Aegis-Urteil mit Laufzeitmessung Stufe 2 trägt.

**Eigene Tests nach Testkennung (Review 04 Nr. 16).**
- `aegis.ist_eigener_test` schließt eine ausgeführte Kennung aus, wenn sie zu einem eigenen Test des Kandidaten gehört:
  - Python `datei::name[p]` → `datei::name`;
  - TypeScript `test.each` → Vorlage `%s`/`$wert`.
- Dazu nimmt der Ankläger parametrisierte Kandidatentests jetzt auf (Norm-Regel am Funktionsnamen). Vorher verwarf er
  sie still (`nur_funktionen` → `None`); der Ausschluss nach Kennung wäre sonst ohne Gegenstand gewesen.
- **Probe (durch `aegis.pruefen`):** Tab-Rückschritt mit eigenem parametrisiertem Test, der genau ihn zusichert (Verweis
  auf Verfassung Satz 2): abgelehnt, `…[tab]` steht unter `eigene_tests_ausgeschlossen`.
- **Gegenprobe:** Ausschluss nur nach exakter Kennung (Stand `43b8fad`) — derselbe Test deckt den eigenen Rückschritt,
  der Kandidat überlebt.
- **Unit:** 5 Kennungsfälle.

**Nachspiel in der Regression (Review 04 Nr. 18).** Der Verdrahtungstest spielt den gewählten Kandidaten seines eigenen
Laufs durch `nachspiel.vorbereiten`/`spielen` nach. Zugesichert: Urteil = aufgezeichnetes Urteil = überlebt, Stufe 2.
An `1d9a5aa` brachen alle Nachspiele ab, während die Regression grün war.

## 9. Teilläufe, Regression, Nachspiele, Vorher/Nachher

**Teilläufe am Arbeitsbaum** (`bau/TEILLAUF-*.txt`):

| Teillauf | Umfang | Ergebnis |
|---|---|---|
| `TEILLAUF-1` | `test_vor_t4_05`, 27 Fälle, vor `r5_bau4/5` | 25 bestanden, 2 rot (§14 Nr. 3) |
| `TEILLAUF-2` | alle Testdateien außer `test_verdrahtung`, ohne `integration` | 591 bestanden, 2 übersprungen, 1 rot, 93 abgewählt, 725 s (§14 Nr. 4) |
| `TEILLAUF-3a` | `test_verdrahtung` | 6 von 6 bestanden, 1719 s |
| `TEILLAUF-3b` | `test_vor_t4_05`, `test_vor_t4_04`, `test_t3_python_annahmen`, `test_vorspann` | 132 von 132 bestanden, 237 s |
| Vorprobe | Nachspiel K2904 am Arbeitsbaum | überlebt (`nachspiel/VORPROBE-ARBEITSBAUM.txt`) |

**Volle Regression am Commit** (`REGRESSION.txt`, `.junit.xml`, `VERDRAHTUNG-BELEG-REGRESSION.json`):
| Stand | bestanden | übersprungen | fehlgeschlagen | JUnit (Fälle / Fehlschläge / Fehler) | Dauer | Verdrahtung |
|---|---|---|---|---|---|---|
| `0c2f058` | 598 | 2 | 0 | 600 / 0 / 0 | 2458 s | grün: 23 von 23 Organen, Register 10 von 10, 0,00 € |

- Übersprungen sind dieselben 2 Fälle wie in den Vorrunden (private Werk-/DB-Kopie nicht angegeben); 93 Fälle
  sind abgewählt (`integration`). `tests/test_vor_t4_05.py`: 27 von 27 grün. `git status`
  war vorher und nachher leer.
- **Verdrahtungsbeleg:**
  - Tor-4-Zeile: „Schwächen: 1 von 1 behoben nach doppelter Prüfung (Schwäche weg UND Verhalten gegen die Normalversion unverändert) = 100 %, Schwelle 80 % — erfüllt“.
  - Nachspiel des gewählten Kandidaten K1: ueberlebt, aufgezeichnet
    ueberlebt, Stufe 2,
    15 Kammerläufe.
  - Aegis-Urteile: 3 mit Laufzeitmessung, alle an Stufe 2; 13 endeten vor der
    Laufzeitmessung.

**Nachspiele am Commit** (`nachspiel/NACHSPIEL-N1..3.txt`, `n1..n3/*.json`):
**Gegenprobe Entscheidung 1 (Runde 4) an `0c2f058`: K2904 und K3091 in 3 von 3 Durchgängen gleich entschieden**,
beide überlebt. 7 von 7 Belegen tragen den Commit `0c2f058`, sauberen Arbeitsbaum, unveränderte T3-DB und 0 Modellaufrufe.

| Durchgang | Kandidat | `planung` Quote (Stufe 2) | Urteil | Gewinn | gesperrt |
|---|---|---|---|---|---|
| N1 | K2904 | 0,407 | ueberlebt | klar | — |
| N1 | K3091 | 0,376 | ueberlebt | klar | — |
| N2 | K2904 | 0,384 | ueberlebt | klar | — |
| N2 | K3091 | 0,403 | ueberlebt | klar | — |
| N3 | K2904 | 0,415 | ueberlebt | klar | — |
| N3 | K3091 | 0,420 | ueberlebt | klar | — |

- `eingang` war in 0 von 6 Nachspielen gesperrt (Runde 4 mit 60 Wiederholungen: 3 von 6).
- **K2868 (N1):** abgelehnt, 24 von 40 Abweichungen ungedeckt, 16 gedeckt — wie in Runde 4.
  Ungedeckt: `crlf` 4, `nbsp` 4, `rand_hinten+rand_vorn+tab+zeilenumbruch` 4, `tab` 4, `zahlform_null_vorn` 4, `zeilenumbruch` 4.

**Vorher/Nachher** (`proben/VORHER-43b8fad.*`, `NACHHER-HEAD.*`): dieselben 27 Fälle von `test_vor_t4_05` am Code von
`43b8fad` und von `0c2f058`, beide aus `git archive`, die Tests jeweils aus dem neuen Commit:
**9 von 27 grün an `43b8fad`, 27 von 27 an `0c2f058`.**
- Die 9 an `43b8fad` grünen Fälle sind die Kontrollen, dazu die 60-s-Grenze des Vorspanns: Sie war schon
  in Runde 4 gebaut, aber ungetestet.
- Von den 18 roten Fällen scheitern 15 am Verhalten (Zusicherung oder
  Sondenausfall).
- 3 scheitern an einer fehlenden Schnittstelle (`test_e8_ist_eigener_test_nach_kennung`, `test_e8_parametrisierter_eigener_test_deckt_nicht[exakt-ueberlebt]`, `test_f2_zusicherung_faellt_am_ort_und_an_der_art`); für diese 3 ist
  „vorher rot“ kein Verhaltensnachweis.

## 10. Geänderte ältere Tests

| Datei | Änderung | Grund |
|---|---|---|
| `tests/drahtwerk.py` | Stufe-2-Last (alpha zehnfach, beta wie Stufe 1) und eine Altlastenliste mit einer Altlast | Entscheidung 6: ohne Stufe 2 verweigert der Vorspann; Entscheidung 5: das Tor-4-Skript braucht eine Liste |
| `tests/test_verdrahtung.py` | Kernmodule des Registers aufgezeichnet, Schritt `tor4`, Nachspiel des gewählten Kandidaten; neue Zusicherungen: Register n von n, A1 doppelt behoben, Laufzeit an Stufe 2, Nachspiel = Lauf | Entscheidungen 5, 6 und 8 |

- Keine Zusicherung ist gelockert; beide Dateien verlangen jetzt mehr.
- `test_vor_t4_04.py` ist unverändert. Sein Fall `test_r413_iterator_kappe_ist_gezaehlt` (Änderung ab Element 60)
  bleibt grün, weil `zaehle` endlos ist und damit auch die Kappe 1000 erreicht.

## 11. Reviewdurchgang

‹REVIEW›

## 12. Sperren im Wortlaut

‹SPERREN›

## 13. Eigene Entscheidungen

1. **Enthaltung des ganzen Urteils bei unvollständiger Erfassung**, nur wenn das Urteil sonst tragfähig wäre (Eine
   Ablehnung wegen einer ungedeckten Abweichung bleibt eine Ablehnung.). **Diese Entscheidung war falsch** (Philipp,
   24.09.):
   - Sie widerspricht Entscheidung 3 und schafft denselben Totalausfall wie Review 04 Nr. 4.
   - Richtig ist: Nur die betroffene Beobachtung enthält sich.
   - Als rote Spezifikation R6-1 vor T4 gefasst, am Organ belegt (§1), nicht mehr in dieser Runde gebaut (ein Review,
     keine Fix-Kaskade).
2. **Die unabhängige Aufzählung ist `object.__getstate__`**, Pythons eigener Kopierzustand, und keine zweite eigene
   Liste. Eine eigene zweite Aufzählung hätte dieselben blinden Stellen wie die erste.
3. **Festhalten in Python am pytest-Bericht** (Absturzstelle und Meldung). Das ist vor dem Bau gemessen
   (`VORPROBE-E2`), nicht angenommen.
4. **Eingrenzung per `os.fork` aus dem Zustand vor der Last.** Ein erster Entwurf wiederholte die Last im selben
   Prozess und erbte den vom ersten Lauf veränderten Modulzustand (§14 Nr. 2).
   - Halbierung statt ein Lauf je Funktion, wegen des Kammer-Zeitlimits von 240 s.
   - Scheitert die Eingrenzung, enthalten sich alle Funktionen der Last; das wird nie als Werkverhalten gewertet.
5. **`ITER_KAPPE` 1000.** Mit 50 riss der eigene Randfall-Korpus (Zahl 100) die Kappe an linearen Generatoren, und die
   Sonde enthielt sich an ihren eigenen Eingaben (`TEILLAUF-1`).
6. **Kappe:** Enthaltung nur, wenn jede ungedeckte Abweichung an einer ausgelassenen Probe hängt.
7. **Register:** Aufrufer und Phase müssen stimmen. Die Kernmodule `gegenzeugen`, `tor4` und `messgeraet` werden
   zusätzlich zu den Organen aufgezeichnet.
8. **Normalvergleich einer Altlast:**
   - Alle angenommenen Kandidaten mit der Altlast im Bereich oder Wirkungskreis zählen.
   - Jede Abweichung zählt als verändert, außer ein unabhängiger Test der Liste deckt sie. Auch eine Abweichung, die ein
     anderer Test deckt, zählt; das ist streng; so gelesen steht es im Wortlaut der Entscheidung 5 („einen unabhängigen Test aus der Altlastenliste“).
9. **Stufe-2-Last `eingang` mit 240 Wiederholungen** (gemessen). Im Drahtwerk ist nur `alpha` zehnfach. Geprüft wird dort
   die Verdrahtung der Stufe, nicht ihre Größe, und die Laufzeit des Verdrahtungstests bleibt bei ≈ 29 min.
10. **Parametrisierte Kandidatentests werden jetzt aufgenommen.** Ohne Aufnahme wäre der Ausschluss nach Kennung (Nr. 16)
    ohne Gegenstand.
11. **Das Tor-4-Skript berechnet nur die Zeile „Schwächen“**, die übrigen Zeilen stehen als „nicht berechnet“ im Ergebnis.

## 14. Eigene Fehler

1. **Der erste Aufruf von `bau/r5_bau.py` brach ab**: `ValueError` beim Entpacken eines Bereichsankers mit 3 statt 4
   Teilen, ein Fehler im Skript. Das Alles-oder-nichts-Prinzip hielt: nichts war geschrieben (`git status` vorher und
   nachher leer).
2. **Der erste Entwurf der Eingrenzung (`r5_bau.py`) hätte die Last im selben Prozess wiederholt** und den Modulzustand
   des ersten Laufs geerbt. Das fiel vor jedem Test beim Lesen auf und ist in `r5_bau2.py` durch `os.fork` ersetzt.
3. **`TEILLAUF-1`: 2 von 27 rot.** Die eigene Vollständigkeitsprüfung ließ die Sonde sich an ihrem eigenen Randfall-Korpus
   enthalten: `zahlen(100)` riss `ITER_KAPPE` 50. Behoben mit `r5_bau5.py` (Kappe 1000).
4. **`TEILLAUF-2`: 1 rot, ein eigener Testfehler.** `test_v1_iterator_kappe_nie_tragfaehig` setzte die alte Kappe voraus.
   Der Test liegt jetzt jenseits von 1000.
5. **Keine Gegenprobe mit deckendem Test für Lastaufrufe (§7)**, und keine TypeScript-Proben für die Entscheidungen 2 und
   3 (§2, §3).
6. **`proben/t4_groesse.py` hätte in der ersten Fassung nicht gebaut** (Bereich `werk` fehlte als Unterpaket). Korrigiert
   vor seinem Lauf in der Kette (`bau/r5_t4_fix.py`).
7. **Die Enthaltung des ganzen Vergleichs (§13 Nr. 1) war ein Entwurfsfehler.** Ich hatte das Risiko in §1 als „Offen“
   notiert, statt es gegen Entscheidung 3 zu prüfen. Es ist dieselbe Figur, die Review 04 Nr. 4 als Befund führte:
   ein Einzelfall legt den ganzen Vergleich still.
8. **Die Stufe-2-Last habe ich nach der Sperrzahl gewählt, nicht nach der Stichprobendauer.** Die Dauer stand in
   `STUFE2-EICHUNG.jsonl`, ich habe sie aber erst auf Nachfrage ausgewertet (§6).
9. **R6-4: Die Vorprobe zu Entscheidung 2 (`VORPROBE-E2`) prüfte nur Zusicherungen mit Text.** Dass pytest das Präfix
   bei Meldungen ohne Anführungszeichen wegkürzt, fiel erst nach dem Commit auf, und zwar an der T4-Größen-Messung.
   Rote Spezifikation R6-4; keine Nachbesserung nach dem Commit.
10. **„Gemessen an einem Kandidaten in T4-Größe“ (Entscheidung 4) ist nicht erfüllt.** Nachgebildet ist nur die Breite
    des Kandidaten, nicht die Größe des Werks (126 Zeilen statt 6.000–10.000). Das Urteil der Messung ist wegen R6-4 nicht
    verwertbar (§4).

## 15. Offen für Philipp

1. **R6-4 vor T4 bauen?** Ein Test, der eine Zahl, eine Liste oder einen Wahrheitswert zusichert, hält nach
   Entscheidung 2 nichts fest (pytest-Meldung ohne Präfix).
   - Optionen: (a) vor T4 zusammen mit R6-1 und R6-2 (empfohlen); (b) nach T4.
   - Gemessene Folge von (b): In der T4-Größen-Messung hält für 5 von 8
     geänderten Funktionen kein Test fest. Jede ihrer Abweichungen bleibt ungedeckt, der Kandidat wird abgelehnt — auch
     eine richtige Behebung mit Tests.
2. **Welche Tor-4-Zeilen berechnet das Skript (R6-2)?**
   - Optionen: (a) die 10 aus der Datenbank berechenbaren Zeilen, je mit Nachweis im nächsten Auftrag (empfohlen);
     (b) meine Einteilung zuerst von dir bestätigen lassen.
   - Folge von (b): ein Schritt mehr vor dem Bau.
3. **Maß der Stufe-2-Lasten (R6-3).**
   - Optionen: (a) eine vorab festgelegte Mindestdauer der Stichprobe je Bereichslast an Stufe 2, für alle Bereiche
     gleich, z. B. 100 ms Median (empfohlen); (b) die Regel der Stufe 1, „einige zehn Millisekunden“; (c) 240 belassen.
   - Gemessene Folge von (a) bei 100 ms: `eingang` mit 240 Wiederholungen (170,5 ms), `planung` (346,0 ms) und `bericht`
     (100,5 ms) erfüllen sie; `zahlen` (18,9 ms) und `tarife` (96,0 ms) wären neu zu bemessen. Der längste Kammerlauf
     lag bisher bei 12,3 s, weit unter 60 s.
   - Folge von (b): 60 Wiederholungen (35,1 ms) genügten, `eingang` sperrte damit aber in 3 von 8 Rauschmessungen.
   - Folge von (c): kein Maß, nur die Sperrzahl.
4. **Kappe der Verfälschungsläufe (Entscheidung 4) neu messen.**
   - Optionen: (a) nach R6-4 am echten T4-Werk vor dem Lauf, mit einem breiten gestellten Kandidaten (empfohlen);
     (b) am erweiterten Prüfwerk.
   - Gemessen bisher: Bedarf 35 Läufe bei 8 geänderten Funktionen in einem
     Werk mit 126 Zeilen; das Urteil war wegen R6-4 nicht verwertbar.
5. **TypeScript-Proben für die Entscheidungen 2 und 3.** Der TypeScript-Weg ist gebaut, aber ohne eigene Kammerprobe.
   - Optionen: (a) vor T5, zusammen mit den TS-Methoden (empfohlen, T4 ist Python); (b) vor T4.
   - Folge von (a): keine für T4.
