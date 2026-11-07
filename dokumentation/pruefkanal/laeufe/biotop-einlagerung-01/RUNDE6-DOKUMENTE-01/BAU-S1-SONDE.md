# Bauauftrag S1 (Runde 6, Entscheidungen 1, 2, 3, 7): Sonde und Verhaltensvergleich ohne stillen Durchlass

Du baust einen Teil der Behebungsrunde 6 vor T4 des Biotop-Projekts. Antworte und schreibe auf Deutsch. Du setzt NUR das
Folgende um, committest nichts und startest keine Hintergrundprozesse (nur Vordergrundbefehle ≤ 600 s).

## Umgebung
- Code `/root/biotop` (git, HEAD `0c2f058`, NICHT committen), Python `/root/biotop-t3/venv/bin/python`,
  Tests `cd /root/biotop && /root/biotop-t3/venv/bin/python -m pytest <datei> -q -p no:cacheprovider -rfE`.
  Echte Kammer (Docker, netzlos) ist erlaubt und nötig: `biotop.organe.kammer`, Image `biotop-kammer:1` (Python).
- Arbeitsordner `/root/biotop-vor-t4-06/` (Unterordner `bau/`), eigener Temp-Ordner `/tmp/r6-s1/` (setze `TMPDIR`).
- Parallel arbeiten zwei andere Bauende im selben Baum (Tor-4-Skript; Stufe-2-Eichphase in `vorspann.py`, `lauf.py`,
  `nachspiel.py`): fasse NUR deine Dateien an. Kein Modellaufruf, kein Netz.
- Lange oder mehrteilige Befehle als Skript unter `/tmp/r6-s1/`. Wird ein Befehl gesperrt (Sicherheitssperre,
  Freigabeabfrage), hältst du an und berichtest Befehl und Meldung wörtlich.

## Deine Dateien (nur diese)
`biotop/kern/py/verhalten.py`, `biotop/organe/verhaltensvergleich.py`, `biotop/organe/aegis.py` (nur die Behandlung der
Enthaltung des Verhaltensvergleichs), neu `tests/test_vor_t4_06.py`. Ältere Tests nur ändern, wenn sich die Spezifikation
geändert hat — jede Änderung mit Grund in `bau/S1-GEAENDERTE-TESTS.md`.

## Hintergrund (lies zuerst)
- Geltendes Review der Runde 5: `/root/biotop-vor-t4-05/REVIEW.md` (Befunde Nr. 1–5). Die Proben stehen in
  `/root/biotop-vor-t4-05/review-proben/kammerprobe05.py` (Fälle x3, x3k, x5, x5b, p24, p24b, p25, p26, a3x, f1, f2, d1;
  Ergebnisse an `0c2f058` in `kammerprobe05.out.txt`). Lokale blinde Arten: `review-proben/lokal_b.py` /
  `lokal_b.out.txt`. Rote Spezifikationen der Runde 5: `/root/biotop-vor-t4-05/spez/` (R6-1, R6-4).
- Bestehende Tests der Runden 4/5: `tests/test_vor_t4_04.py`, `tests/test_vor_t4_05.py`, `tests/test_vor_t4_03.py`
  (Hilfen `_pruefen`, `_diff`, `QUELLE`, `TEST_NORMIEREN`: Laufweg durch `aegis.pruefen` in der echten Kammer).

## Startregel für T4 (vorab gesetzt, Maßstab deines Baus)
„T4 beginnt, sobald das Review dieser Runde keinen stillen Durchlass mehr findet — jede bekannte Lücke muss eine gezählte
Enthaltung sein; Lücken, die sich nur enthalten, behebt T4 im Lauf.“ Wo du etwas nicht darstellen kannst: gezählte
Enthaltung mit Grund, nie „0 Abweichungen, tragfähig“, nie Deckung.

## Entscheidung 1 — typtreue Verfälschung, zusammen mit R6-4
Wortlaut: „R6-4 nur zusammen mit einer typtreuen Verfälschung: verfälscht wird mit einem Wert desselben Typs und anderen
Inhalts, nie mit einem Objekt, das beim Weiterrechnen wirft; ein Test hält nur fest, wenn seine Zusicherung am geänderten
Wert fällt (Review-Nr. 1, Proben x5 und x5b).“
- `verhalten.py`, `deck_wickeln` (Art `rueckgabe`) und `_stoeren` (Art `zustand`): statt `Verfaelscht()` ein
  **typtreuer anderer Wert** `g(v)`, deterministisch: bool → `not v`; int → `v + 1`; float → `v + 1.0` (NaN/Inf → `0.0`,
  sonst sicherstellen, dass er sich unterscheidet); complex → `v + 1`; str → letztes Zeichen mit `chr(ord(c) ^ 1)`
  (Länge bleibt; leer → `'x'`); bytes/bytearray analog am letzten Byte; list/tuple (auch Unterklassen, namedtuple) →
  Kopie mit verfälschtem letztem verfälschbaren Element; dict → Kopie mit verfälschtem letztem Wert; set/frozenset →
  ein Element durch sein `g` ersetzt; Decimal/Fraction → `+ 1`; date/datetime → `+ 1 Tag`; `os.PathLike` → gleicher Typ,
  Name verändert; Instanzen von Python-Klassen/Dataclasses → `copy.copy` mit einem typtreu verfälschten Datenfeld. `None`,
  leere Behälter ohne Elementtyp und alles andere: **nicht verfälschbar**.
- **Weiterrechnen ohne Doppelverfälschung:** Jeder ausgegebene verfälschte Wert wird registriert (verfälscht → Original).
  Bekommt die verfälschte Funktion einen registrierten verfälschten Wert als Argument, rechnet sie mit dem Original
  (`g(f(original))`). So bleibt eine idempotente Funktion unter Verfälschung idempotent: x3 (Idempotenz-Zusicherung) darf
  nicht festhalten, x5 (`isinstance`) und x5b (Tautologie) ebenso nicht; ein Test, der den Wert zusichert, hält fest.
- **Nicht verfälschbare Aufrufe** zählt der Aufzeichner je Probe (`nicht_verfaelschbar`). Fällt ein Test in dieser Probe,
  hält er fest; fällt er nicht und gab es nicht verfälschbare Aufrufe, ist die Probe **unentschieden**.
  `verhaltensvergleich`: eine ungedeckte Abweichung, die nur an unentschiedenen oder (Kappe) ausgelassenen Proben hängt,
  ist eine Enthaltung (`grund_art` `verfaelschung_unvollstaendig` bzw. wie bisher `verfaelschungskappe`), gezählt; jede
  andere ungedeckte Abweichung lehnt ab wie bisher.
- **R6-4 (Festhalten am Ausnahmetyp):** Im Plugin des Aufzeichners einen `pytest_runtest_makereport`-Hookwrapper, der
  `call.excinfo.type` am Bericht festhält; „fällt“ heißt: Typ ist `AssertionError` (oder Unterklasse) oder pytests
  `Failed` (`pytest.fail.Exception`), UND die Absturzstelle (`reprcrash.path`) ist die Testdatei. Nicht mehr am
  Meldungstext (pytest streicht „AssertionError:“ bei Meldungen ohne Anführungszeichen: `assert f(1) == 3` hielt nichts
  fest). Fallback ohne Typ (alte Aufrufer, gestellte Berichte): Meldung beginnt mit `AssertionError`, `Failed` oder
  `assert `. Hängt ein Test unter Verfälschung (Frist, siehe Entscheidung 3), ist er `fehler`.
- TypeScript (`deck-setup.mjs`, `deckung.mjs`) NICHT ändern: TS-Proben und TS-Umbau sind vor T5 (Entscheidung 8, R6-13).

## Entscheidung 2 — undurchsichtige Objekte
Wortlaut: „Zustand aus C-Typen wird über eine bekannte Darstellung erfasst (etwa getvalue, str, pickle), sonst ist die
Beobachtung eine gezählte Enthaltung — nie ‚0 Abweichungen‘ (Nr. 2, p24b, p25).“
- `kan()`: Objekte, deren Klassenhierarchie eine C-Basis außer `object` hat (nicht `Py_TPFLAGS_HEAPTYPE`, etwa
  `_io.StringIO`, `decimal.Decimal`, `datetime.date`, `collections.deque`, `array.array`), bekommen zusätzlich zu ihren
  Datenattributen den C-Zustand: `io.StringIO/BytesIO` → `getvalue()` und `tell()`; sonst `__reduce_ex__(4)` (Argumente
  und Zustand kanonisch, Iteratoren darin als Liste). Wirft das oder liefert es keinen Inhalt → `fehlend` (gezählte
  Enthaltung „C-Zustand nicht darstellbar“).
- Eine Darstellung, die eine Adresse trägt (`_ADRESSE`), ist kein Inhalt: `memoryview` → `tobytes()`, `weakref` → Ziel
  (`ref()`), sonst `__reduce_ex__(4)`, sonst `fehlend`.
- Funktionen/Klassen als Wert: statt `'__fn'` für alle dieselbe Form `{'__fn': 'modul:qualname'}` (auch `int` vs. `list`
  als `default_factory`); `functools.partial` → Funktion, `args`, `keywords`.
- Öffentliche `property`s und Daten-Deskriptoren reiner Python-Klassen: Wert lesen (unter der Sonde bereits `TIEFE > 0`,
  der Getter wird nicht beobachtet); wirft er → `'__fehler:Typ'` als Wert. Deckt den Deskriptor mit Zustand außerhalb der
  Instanz und die Property über einer Closure (lokal blind in Review 05 Nr. 2) ab.
- Nachweis mit p24b, p25 (Kammer, am Organ) und den 11 blinden Arten aus `lokal_b.out.txt` (lokal, `kan` direkt): jede
  gesehen oder gezählte Enthaltung, keine blind. Kontrollen: gewöhnliche Werte (`lagerhaus`-artige Dataclasses, dict,
  list, Decimal) ohne Enthaltung.

## Entscheidung 3 — Enthaltung je Funktion; geänderte Funktion stellt zurück; Zeitgrenze je Funktion
Wortlaut: „R6-1 zusammen mit der Lücke aus Nr. 3: Enthält sich eine geänderte Funktion, wird der Kandidat
zurückgestellt; enthalten sich nur unveränderte, wird am Rest geurteilt. Dasselbe für eine hängende Last: Zeitgrenze je
Funktion, nicht je Kandidat.“
- `verhaltensvergleich`: **betroffene Funktionen** aus dem Syntaxbaum Vorgeneration gegen Kandidat je geändertem Modul:
  geändert = eigener Knoten verschieden (`ast.dump` ohne Positionen), neu oder entfernt; Modulebene außer Funktions- und
  Klassendefinitionen geändert → alle Funktionen des Moduls; Klassenkörper außer Methoden geändert → alle Methoden der
  Klasse; dazu transitiv jede Funktion, deren Körper einen Namen einer betroffenen Funktion nennt (auch private Helfer —
  sonst verbirgt eine unvollständig erfasste unveränderte Aufruferin die Änderung eines privaten Helfers). Namen wie in
  den Beobachtungen (`modul:f`, `modul:Klasse.m`, `modul:Klasse.__init__`). TypeScript: alle Funktionen geänderter
  Module gelten als betroffen.
- Enthaltung (unvollständig erfasst, Sondenausfall, Zeitgrenze) einer **betroffenen** Funktion → der Vergleich enthält
  sich (`enthaltung: True`, `grund_art` `betroffene_funktion_enthaelt_sich`, Grund nennt die Funktionen) →
  `aegis.pruefen` stellt zurück (gezählt, wie heute). Enthaltungen nur **unbetroffener** Funktionen: gezählte
  Enthaltungen im Urteil, geurteilt wird am Rest (keine Enthaltung des ganzen Vergleichs mehr — R6-1). Eine ungedeckte
  Abweichung lehnt immer ab.
- **Zeitgrenze:** in der Sonde jeder beobachtete Aufruf (`wert`) mit einer Frist (5 s, `signal.setitimer`, verschachtelt
  sauber: Stapel von Fristen), jede Bereichslast mit 60 s; läuft eine Frist ab → Ausnahme `Zeitgrenze` (eigene Klasse),
  der Aufruf zählt als `zeitgrenze[funktion]` und die Funktion enthält sich („Zeitgrenze überschritten“); eine Last über
  60 s zählt als Abbruch und wird eingegrenzt wie ein Abbruch (auch in den Kindprozessen der Eingrenzung, je Kind eine
  Frist). Probe d1 (hängende `queue.Queue`) muss danach geurteilt oder gezählt enthalten sein, kein Messgerätausfall.
- Nachweise: a3x (geänderte Funktion im Sondenausfall) → zurückgestellt; f1, f2 (nur unveränderte Funktionen schwer
  erfassbar, verhaltensgleicher Kandidat) → geurteilt, tragfähig; `/root/biotop-vor-t4-05/spez/test_spez_r6_laufweg.py`
  (StringIO-Funktion unverändert) → überlebt; eine geänderte Funktion, die ein `StringIO` liefert (p24) → zurückgestellt;
  privater Helfer geändert, Aufruferin unvollständig erfasst → zurückgestellt.

## Entscheidung 7 — Ausnahmen nach Typ und Inhalt
- `wert()`: eine geworfene Ausnahme wird mit Typ und Inhalt beobachtet (`args`, Datenattribute, Adressen getilgt,
  ungekürzt — `knapp()` kürzt mit Prüfsumme), nicht mehr nur `Fehler:<Typ>`. `kan()` für Ausnahmeobjekte ebenso (bisher
  Meldung auf 200 Zeichen gekürzt, Attribute fehlten). Der Korpus-Status `korpus:last_*` (`Fehler:<Typ>`) bleibt, wie er
  ist (der Wirt liest ihn).
- Nachweise: p26 (Meldung ‚PLZ …‘ vs. ‚Ort …‘) → Abweichung; gleiche Meldung → tragfähig.

## Rote Spezifikationen und Lieferung
1. **Zuerst** `tests/test_vor_t4_06.py`: je Entscheidung Probe und Gegenprobe (Laufweg durch `aegis.pruefen` wie
   `test_vor_t4_05.py`, wo ein Organ im Annahmepfad wirkt; sonst am Organ `verhaltensvergleich.pruefen` in der echten
   Kammer; lokale `kan`-Fälle als Unit). Mindestens: x5, x5b, x3 (bleibt abgelehnt), x3k; positive Kontrolle „richtige
   Behebung mit Tab-Test hält fest und überlebt“; R6-4 Zahl/Liste/Wahrheitswert (am Aufzeichner in der Kammer); p24b, p25;
   a3x, f1, f2, p24, privater Helfer; d1; p26 und Gegenprobe. Lass die Datei **vor** dem Bau gegen den Stand `0c2f058`
   laufen (Kopie per `git archive 0c2f058` nach `/tmp/r6-s1/vorher/`, Tests aus deinem Arbeitsbaum hineinkopieren, dort
   ausführen; Ausgabe `bau/S1-VORHER-0c2f058.txt`) — erwartet: jede Probe rot an ihrer Zusicherung, jede Gegenprobe grün.
2. Umbau als alles-oder-nichts-Skript(e) `bau/r6_s1_*.py` (bricht ohne Schreiben ab, wenn ein Anker fehlt; Protokoll
   `bau/R6-S1-*.txt`).
3. Teillauf am Arbeitsbaum: `tests/test_vor_t4_06.py`, `tests/test_vor_t4_05.py`, `tests/test_vor_t4_04.py`,
   `tests/test_vor_t4_03.py`, `tests/test_vor_t4_02.py`, `tests/test_t3_python_annahmen.py` und jede weitere Testdatei,
   die `verhalten.py` oder `verhaltensvergleich` nutzt (per `grep -l`), je Datei-Gruppe ein pytest-Aufruf mit einem `-q`
   und `-rfE`, Ausgabe `bau/TEILLAUF-S1.txt`. Alles grün, oder jede Abweichung erklärt.
4. `bau/S1-UMSETZUNG.md`: je Entscheidung Umsetzung, Nachweis (Test, Laufweg/Organ/Unit), Grenzen (was weiter blind
   bleibt, gelesen oder gemessen), geänderte ältere Tests mit Grund.
5. Schlussbericht (deine letzte Antwort): geänderte Dateien, Vorher (x von y rot an `0c2f058`), Teststand x von y,
   offene Punkte, Sperren (oder „keine“).
