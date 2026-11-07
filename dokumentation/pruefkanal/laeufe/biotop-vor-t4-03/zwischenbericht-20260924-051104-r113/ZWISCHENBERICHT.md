# Zwischenbericht — automatisch ausgelöst (biotop-vor-t4-03)

Ausgelöst 2026-09-24T05:11:04+02:00 vom Zwischenbericht-Wächter (Cron, ohne Modell). Sitzung `20260923_194003_92313ee1`, Werkzeugrunde **113 von 150** (Schwelle 110).
Anlass: Werkzeugrunde 113 von 150.
Regel (Philipp, 23.09.2026): Zwischenbericht spätestens bei 120 von 150 Aufrufen — ausgelöst, nicht erinnert.
Die Übergabedateien sind der zuletzt vom Agenten geschriebene Stand; alle übrigen Abschnitte sind in diesem Augenblick mechanisch gelesen.

## Auftrag dieses Turns (Nachricht 15369, 2026-09-24T02:14:45+02:00)

```
Richtig nicht abgenommen, und die Lücken der Python-Sonde gehören zu den wichtigsten Befunden vor T4. Entscheidungen Chat-Claude: (1) Deckung je Muster (deine Option 1) — je Eingabe ist zu fein, ein richtiger Test deckt 2 von 28; je Funktion zu grob, dahinter lag die Weißraum-Lücke. Gegenproben: K2868 scheitert am ungedeckten Weißraum-Muster; eine richtige Behebung mit einem Test je Muster kommt durch; K2868 wird einmal nur mit erweitertem Korpus und einmal nur mit neuer Deckungsregel gemessen, damit getrennt ist, was was bewirkt. (2) Gewinnschwelle der Nische „schnell" in beiden Richtungen nachmessen, nur innerhalb der Rauschtoleranz um die Schwelle; Gegenprobe K2904/K3091 drei von drei gleich — kippt es trotzdem, meld es, dann liegt es an der Größe der Vergleichslast. (3) Methoden von Klassen vor T4 beobachten, Instanzen aus den Verträgen, Zustand von self vor und nach dem Aufruf verglichen; Enthaltung nur für wirklich Unbeobachtbares, gezählt. (4) S1 nicht neu versiegeln — nach der Messung ändert man kein Kriterium; für jedes künftige Testwerk prüft jeder Gegenzeuge zweierlei: Schwäche weg und gültiges Verhalten gegen die Normalversion unverändert. Auftrag Behebungsrunde 3: deine 13 Spezifikationen aus SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md plus diese vier Entscheidungen, jede mit Gegenprobe durch den Laufweg; die fünf Lücken der Python-Sonde je mit einem Fall, der vorher unentdeckt blieb oder Fehlalarm gab. Der Reviewer ist an dieselbe Regel gebunden wie du: bei einer Sicherheitssperre anhalten und melden, nie auf anderem Weg lesen. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, Abschlussordner laeufe/biotop-vor-t4-03/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.Richtig nicht abgenommen, und die Lücken der Python-Sonde gehören zu den wichtigsten Befunden vor T4. Entscheidungen Chat-Claude: (1) Deckung je Muster (deine Option 1) — je Eingabe ist zu fein, ein richtiger Test deckt 2 von 28; je Funktion zu grob, dahinter lag die Weißraum-Lücke. Gegenproben: K2868 scheitert am ungedeckten Weißraum-Muster; eine richtige Behebung mit einem Test je Muster kommt durch; K2868 wird einmal nur mit erweitertem Korpus und einmal nur mit neuer Deckungsregel gemessen, damit getrennt ist, was was bewirkt. (2) Gewinnschwelle der Nische „schnell" in beiden Richtungen nachmessen, nur innerhalb der Rauschtoleranz um die Schwelle; Gegenprobe K2904/K3091 drei von drei gleich — kippt es trotzdem, meld es, dann liegt es an der Größe der Vergleichslast. (3) Methoden von Klassen vor T4 beobachten, Instanzen aus den Verträgen, Zustand von self vor und nach dem Aufruf verglichen; Enthaltung nur für wirklich Unbeobachtbares, gezählt. (4) S1 nicht neu versiegeln — nach der Messung ändert man kein Kriterium; für jedes künftige Testwerk prüft jeder Gegenzeuge zweierlei: Schwäche weg und gültiges Verhalten gegen die Normalversion unverändert. Auftrag Behebungsrunde 3: deine 13 Spezifikationen aus SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md plus diese vier Entsc
```

## Übergabe (vom Agenten gepflegt)

- `/root/biotop-vor-t4-03/UEBERGABE.md` — Stand 2026-09-24T04:55:29+02:00, als eigene Datei im Ordner

## Letzte Äußerungen des Agenten in diesem Turn (neueste zuletzt)

- 2026-09-24T02:20:51+02:00: Jetzt den Code der Sonde neu lesen (die Zusammenfassung trägt ihn nicht).
- 2026-09-24T03:31:25+02:00: Umfang ist groß; ich schreibe zuerst die Python-Sonde neu (eigene Datei aus Runde 2, daher Vollersatz statt Ankerpatches), dann Host-Seite, TS-Seite, Messgerät.
- 2026-09-24T04:36:34+02:00: Jetzt die TS-Seite (Runner, Aufzeichner, Kanon) im selben Umfang.
- 2026-09-24T05:05:12+02:00: Teillauf grün (rc 0, 103 Fälle). Jetzt die Laufweg-Tests der Runde 3: fünf Lücken, Entscheidungen 1–4, Spezifikationen.

## Repositories

`/root/biotop`:
```
6243377 Vor T4, Runde 2: Python-Sonde, Deckung je Abweichung, Formvarianten, bestätigte Laufzeitrisse
330b4ec Vor T4: Review-Befunde eingearbeitet (ein Reviewdurchgang zu 58bd9f9)
58bd9f9 Vor T4: Behebungsrunde — Vorbedingungen 1–11 aus Masterprompt Fassung 8
M biotop/kern/messgeraet.py
 M biotop/kern/py/verhalten.py
 M biotop/kern/ts/deck-setup.mjs
 M biotop/kern/ts/kanon.mjs
 M biotop/kern/ts/verhalten-runner.mjs
 M biotop/kern/ts/verhalten.mjs
 M biotop/kern/ts/vitest.deck.config.mjs
 M biotop/lauf.py
 M biotop/nachspiel.py
 M biotop/organe/aegis.py
 M biotop/organe/eichproben.py
 M biotop/organe/verhaltensvergleich.py
 M tests/test_t3_verhaltensvergleich.py
 M tests/test_vor_t4.py
 M tests/test_vor_t4_02.py
 M tests/test_vorspann.py
?? biotop/kern/ts/einwickeln.mjs
?? tests/test_vor_t4_03.py
```

## Seit Turnbeginn geänderte Dateien (neueste zuerst)

- 2026-09-24T05:11:04+02:00          15 B  sha256 04a2b659de251059…  `/root/biotop-vor-t4-03/bau/TEILLAUF-2.txt`
- 2026-09-24T05:10:46+02:00       52896 B  sha256 071fd78b9e8be547…  `/root/biotop/biotop/kern/py/verhalten.py`
- 2026-09-24T05:08:28+02:00       25207 B  sha256 d1a04e135c424443…  `/root/biotop/tests/test_vorspann.py`
- 2026-09-24T05:08:28+02:00       27676 B  sha256 c30afcd2e6f3beaf…  `/root/biotop/tests/test_vor_t4_03.py`
- 2026-09-24T05:08:28+02:00       51411 B  sha256 d78c00e522bef1f5…  `/root/biotop/biotop/kern/messgeraet.py`
- 2026-09-24T05:03:31+02:00         160 B  sha256 51e313688c5e7bfd…  `/root/biotop-vor-t4-03/bau/TEILLAUF-1.txt`
- 2026-09-24T05:02:03+02:00       19109 B  sha256 6727c4f8eeb83608…  `/root/biotop/tests/test_vor_t4_02.py`
- 2026-09-24T05:02:03+02:00       15454 B  sha256 501daf04980e5f39…  `/root/biotop/tests/test_t3_verhaltensvergleich.py`
- 2026-09-24T04:59:11+02:00       48644 B  sha256 043a6da6609506c9…  `/root/biotop/tests/test_vor_t4.py`
- 2026-09-24T04:55:57+02:00       60373 B  sha256 3ae78ffe829856b0…  `/root/biotop/biotop/lauf.py`
- 2026-09-24T04:55:57+02:00       69687 B  sha256 50ef7df4923704d2…  `/root/biotop/biotop/organe/aegis.py`
- 2026-09-24T04:55:29+02:00        3647 B  sha256 5eb78b8ac53be854…  `/root/biotop-vor-t4-03/UEBERGABE.md`
- 2026-09-24T04:53:40+02:00        1698 B  sha256 ef1c92309bf834ba…  `/root/biotop/biotop/kern/ts/vitest.deck.config.mjs`
- 2026-09-24T04:53:27+02:00        1629 B  sha256 a491ed0bbafc8e11…  `/root/biotop-vor-t4-03/bau/diagnose_deck_ts.py`
- 2026-09-24T04:53:04+02:00        2679 B  sha256 1912b2dee0746a3b…  `/root/biotop-vor-t4-03/bau/rauchprobe_ts.py`
- 2026-09-24T04:52:52+02:00       37799 B  sha256 e4df989159ff6a43…  `/root/biotop/biotop/organe/verhaltensvergleich.py`
- 2026-09-24T04:49:58+02:00       16565 B  sha256 f7eeeb884fe50776…  `/root/biotop/biotop/nachspiel.py`
- 2026-09-24T04:49:31+02:00       35966 B  sha256 5d3e70d6a3ed6c51…  `/root/biotop/biotop/organe/eichproben.py`
- 2026-09-24T04:39:46+02:00        2000 B  sha256 44cd0e156e75109d…  `/root/biotop/biotop/kern/ts/deck-setup.mjs`
- 2026-09-24T04:39:29+02:00        3893 B  sha256 e5d35e5a34253033…  `/root/biotop/biotop/kern/ts/verhalten.mjs`
- 2026-09-24T04:39:13+02:00        4305 B  sha256 4d08d845c30dd1b8…  `/root/biotop/biotop/kern/ts/einwickeln.mjs`
- 2026-09-24T04:37:40+02:00       18961 B  sha256 08b93baa3996acb2…  `/root/biotop/biotop/kern/ts/verhalten-runner.mjs`
- 2026-09-24T04:36:34+02:00        4072 B  sha256 a3a16a388f81046d…  `/root/biotop/biotop/kern/ts/kanon.mjs`
- 2026-09-24T04:18:06+02:00        4507 B  sha256 160161335a3d66e3…  `/root/biotop-vor-t4-03/bau/rauchprobe_sonde.py`
- 2026-09-24T03:31:25+02:00       28356 B  sha256 6890e5d986377395…  `/root/biotop-vor-t4-03/bau/verhalten.py.vor-runde3`

## Laufende Prozesse (Auszug)

```
 412012      14 /usr/bin/bash -lic set +m; cd /root/biotop && BIOTOP_KAMMER_IMAGE=biotop-kammer:ts1 timeout 900 /root/biotop-t3/venv/bin/python -m pytest tests/test_vor_t4_03.py -q -p no:cacheprovider
 412025      14 timeout 900 /root/biotop-t3/venv/bin/python -m pytest tests/test_vor_t4_03.py -q -p no:cacheprovider --tb=short -q
 412026      14 /root/biotop-t3/venv/bin/python -m pytest tests/test_vor_t4_03.py -q -p no:cacheprovider --tb=short -q
 413055       0 docker run --rm --name biotop-b8774511bd05 --network none --memory 512m --memory-swap 512m --cpus 1 --pids-limit 256 --read-only --tmpfs /tmp:rw,size=64m --security-opt no-new-privileg
```
