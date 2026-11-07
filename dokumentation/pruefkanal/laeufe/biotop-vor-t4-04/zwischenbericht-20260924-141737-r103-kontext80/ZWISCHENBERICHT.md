# Zwischenbericht — automatisch ausgelöst (biotop-vor-t4-04)

Ausgelöst 2026-09-24T14:17:37+02:00 vom Zwischenbericht-Wächter (Cron, ohne Modell). Sitzung `20260923_194003_92313ee1`, Werkzeugrunde **103 von 150** (Schwelle –).
Anlass: Kontextfüllung 82.0 % (820496 von 1000000 Token, anthropic/claude-opus-5-5, Stand 2026-09-24T14:17:11+02:00; Schwelle 80 %).
Regel (Philipp, 23.09.2026): Zwischenbericht spätestens bei 120 von 150 Aufrufen — ausgelöst, nicht erinnert.
Die Übergabedateien sind der zuletzt vom Agenten geschriebene Stand; alle übrigen Abschnitte sind in diesem Augenblick mechanisch gelesen.

## Auftrag dieses Turns (Nachricht 15992, 2026-09-24T11:49:51+02:00)

```
Sauber veröffentlicht, und die getrennten Schritte liefen ohne Sperre. Entscheidungen Chat-Claude zu deinen sechs Punkten: (1) Vergleichslast: zweite Stufe mit zehnfacher Eingabegröße je Bereich, ein Kammerlauf bleibt unter einer Minute; an ihr misst die Nische „schnell" den Gewinn und jede Nische ihre Laufzeitgrenze; Gegenprobe im Nachspiel: K2904 und K3091 drei von drei gleich; T3s Ergebnisse bleiben unverändert. (2) Die vier hohen Befunde vor T4; jede Formvariante, die die Sonde erzeugt, ist ein eigenes Merkmal — Weißraum also je Zeichen. (3) Merkmale von Argumenten, die die Sonde nicht verändert hat, gehören nicht zum Muster; Gegenprobe: Die Abweichungen bei ungültigen Eingaben von K2868 sind gedeckt, die Weißraum-Muster bleiben ungedeckt. (4) Tests, die der Kandidat selbst mitbringt, decken nicht — ein Vorschlag beglaubigt seine eigene Änderung nie; decken dürfen Tests der Vorgeneration, aus Generation 0, vom Ankläger und die versiegelten Gegenzeugen; Gegenprobe: Ein Kandidat mit Rückschritt und eigenem Test, der genau diesen Rückschritt zusichert, wird abgelehnt. (5) Methoden in TypeScript vor T5, nicht vor T4; die doppelte Gegenzeugen-Prüfung ist verbindlich in der Torzeile „Schwächen", nicht im Annahmepfad. (6) Den Fehlalarm als sachlichen Text mit Befehlsmuster und Sperrwortlaut in den Abschlussordner legen, ohne Projektinterna; ob er eingereicht wird, entscheidet Philipp. Auftrag Runde 4: diese sechs Punkte plus aus R4-1 bis R4-20 alles, was T4 gefährden würde — der Rest mit Begründung auf die Liste. Die Übergabe nach jedem abgeschlossenen Schritt nachführen, damit die Zwischenberichte nicht veralten. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, laeufe/biotop-vor-t4-04/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

## Übergabe (vom Agenten gepflegt)

- `/root/biotop-vor-t4-04/UEBERGABE.md` — Stand 2026-09-24T14:09:33+02:00, als eigene Datei im Ordner

## Letzte Äußerungen des Agenten in diesem Turn (neueste zuletzt)

- 2026-09-24T14:09:46+02:00: Runde 4 ist noch nicht fertig und nicht geliefert. Commit `1d9a5aa` liegt auf `0aac612`. Die volle Regression läuft, danach im selben Job die Nachspiele und der Vorher/Nachher-Vergleich; anschließend startet automatisch ein Nachtrag. **Gebaut** - **Vergleichslast Stufe 2:** Jeder Bereich läuft mit zehnfacher Eingabegröße, Stufe 1 bleibt unverändert. - Ein Kammerlauf dauert jetzt 8,6 bis 11,7 s, alle 12 von 12 Läufen unter 60 s. - Die `planung`-Quote sinkt dort auf etwa 0,40. An Stufe 1 lag sie direkt an der Schwelle 0,85: bei K3091 mit 0,839 knapp darunter, bei K2904 mit 0,851 knapp darüber. - Die erste Fassung der Last überschritt den Wertebereich des Werks. Das ist korrigiert und belegt. - **Die vier hohen Review-Befunde:** - Jede Formvariante ist ein eigenes Merkmal, in Python und TypeScript nachweislich gleich gerechnet. - Die Verfälschungsprobe gilt je Merkmal. Fixture-Fehler zählen nicht mehr als Festhalten. - Nur echte Generatoren werden ersetzt. - Klassen mit `__slots__` werden jetzt verglichen. - Der Lastabbruch unter der Sonde folgt im Nachtrag. - **Muster:** zählen nur Merkmale, die die Sonde selbst verändert hat. - **Eigene Tests des Kandidaten decken nicht mehr.** Lieg

## Repositories

`/root/biotop`:
```
1d9a5aa Vor T4, Runde 4: Vergleichslast Stufe 2, Merkmale je Formvariante, Verfälschung je Merkmal, eigene Tests decken nicht
0aac612 Vor T4, Runde 3, Nachtrag: Sprachweichen-Register für die neuen Teile der Python-Sonde
d54bf2f Vor T4, Runde 3: Python-Sonde ohne die fünf Lücken, Deckung je Muster, Methoden, Gewinnschwelle nachgemessen
(Arbeitsbaum sauber)
```

## Seit Turnbeginn geänderte Dateien (neueste zuerst)

- 2026-09-24T14:09:33+02:00           0 B  sha256 e3b0c44298fc1c14…  `/root/biotop-vor-t4-04/bau/KETTE-NACHTRAG.txt`
- 2026-09-24T14:09:33+02:00        8248 B  sha256 c4049e31c917f346…  `/root/biotop-vor-t4-04/UEBERGABE.md`
- 2026-09-24T14:09:32+02:00         455 B  sha256 e65e0cc603a5da3e…  `/root/biotop-vor-t4-04/bau/kette_nachtrag.sh`
- 2026-09-24T14:09:22+02:00        5355 B  sha256 3c395a182eb40371…  `/root/biotop-vor-t4-04/bau/r4_nachtrag.py`
- 2026-09-24T14:09:22+02:00         759 B  sha256 160d9598bb2a71b0…  `/root/biotop-vor-t4-04/COMMIT-NACHRICHT-2.txt`
- 2026-09-24T14:09:22+02:00        2116 B  sha256 5ed4f95c630cd844…  `/root/biotop-vor-t4-04/job_nachtrag.sh`
- 2026-09-24T14:07:19+02:00         378 B  sha256 3dd0acda9844f5e6…  `/root/biotop-vor-t4-04/REGRESSION.txt`
- 2026-09-24T14:07:08+02:00        4890 B  sha256 a1e8e3fc37fd4554…  `/root/biotop-vor-t4-04/BERICHT.md`
- 2026-09-24T14:06:14+02:00        3734 B  sha256 0287b8b33ff3b8cf…  `/root/biotop-vor-t4-04/bau/r4_nachtrag_lastabbruch.py`
- 2026-09-24T14:04:24+02:00         280 B  sha256 950a0d442c8095b6…  `/root/biotop-vor-t4-04/proben/SPION-GEWINN.txt`
- 2026-09-24T14:04:24+02:00         113 B  sha256 3b999712621e9ea9…  `/root/biotop-vor-t4-04/proben/SPION-GEWINN-PYTEST.txt`
- 2026-09-24T14:04:24+02:00         121 B  sha256 13c1d98f6be8628e…  `/root/biotop-vor-t4-04/proben/SPION-GEWINN.jsonl`
- 2026-09-24T14:04:19+02:00        1154 B  sha256 74147a783e210a5b…  `/root/biotop-vor-t4-04/proben/spion_gewinn.py`
- 2026-09-24T14:04:19+02:00         768 B  sha256 2c3f9ea5af15a321…  `/root/biotop-vor-t4-04/proben/spion_gewinn.sh`
- 2026-09-24T14:03:08+02:00        2102 B  sha256 45cfde8170252caf…  `/root/biotop-vor-t4-04/sperre/FORMATSPERRE-1.txt`
- 2026-09-24T14:02:39+02:00         619 B  sha256 7d13c1085af91887…  `/root/biotop-vor-t4-04/sperre/formatsperre-1-befehl.sh`
- 2026-09-24T14:02:32+02:00        2678 B  sha256 a8ad39352282c875…  `/root/biotop-vor-t4-04/JOB-COMMIT-REGRESSION.txt`
- 2026-09-24T14:02:32+02:00      129205 B  sha256 1678c87a24cb7542…  `/root/biotop-vor-t4-04/KERN-COMMIT.patch.txt`
- 2026-09-24T14:02:32+02:00        3195 B  sha256 ae2ed2723c6bc1b6…  `/root/biotop-vor-t4-04/COMMIT-STAT.txt`
- 2026-09-24T14:02:32+02:00          73 B  sha256 5b022129c7558c98…  `/root/biotop-vor-t4-04/bau/KETTE.txt`
- 2026-09-24T14:02:32+02:00         225 B  sha256 74db4f5c4b4e8fd4…  `/root/biotop-vor-t4-04/bau/TEILLAUF-4.txt`
- 2026-09-24T14:01:58+02:00        1151 B  sha256 58ef9be7f8cd392f…  `/root/biotop-vor-t4-04/KASSE.md`
- 2026-09-24T14:01:39+02:00         965 B  sha256 b9523cb872676312…  `/root/biotop-vor-t4-04/bau/kette.sh`
- 2026-09-24T14:01:27+02:00       32541 B  sha256 9672cd5404bcfc31…  `/root/biotop/tests/test_vor_t4_03.py`
- 2026-09-24T14:01:23+02:00        2816 B  sha256 48ee0fbea48eb93b…  `/root/biotop-vor-t4-04/bau/r4_fix2_tests.py`
- 2026-09-24T14:01:01+02:00        3246 B  sha256 c33f746123f80600…  `/root/biotop-vor-t4-04/bau/TEILLAUF-3.txt`
- 2026-09-24T13:42:39+02:00        6469 B  sha256 8fab2fb065a70b98…  `/root/biotop-vor-t4-04/REVIEW-AUFTRAG.md`
- 2026-09-24T13:39:08+02:00        2039 B  sha256 5deb5d68b10ba568…  `/root/biotop-vor-t4-04/COMMIT-NACHRICHT.txt`
- 2026-09-24T13:35:47+02:00        2856 B  sha256 cbe8996bd72b2284…  `/root/biotop-vor-t4-04/proben/vorher_nachher.py`
- 2026-09-24T13:35:47+02:00        2897 B  sha256 b3443f9e3064ac78…  `/root/biotop-vor-t4-04/job_commit_regression.sh`
- 2026-09-24T13:35:07+02:00       27057 B  sha256 1eb1ef260eeeb5be…  `/root/biotop/tests/test_vor_t4_04.py`
- 2026-09-24T13:34:20+02:00         115 B  sha256 4128107991270a88…  `/root/biotop-vor-t4-04/bau/TEILLAUF-2.txt`
- 2026-09-24T13:34:00+02:00        4966 B  sha256 b1b52ebb43ba4487…  `/root/biotop-vor-t4-04/nachspiel/nachspiel_vor_t4_04.py`
- 2026-09-24T13:33:42+02:00       42606 B  sha256 997af7f6666c1ff7…  `/root/biotop/biotop/organe/verhaltensvergleich.py`
- 2026-09-24T13:33:38+02:00        4559 B  sha256 967a8ddf16239eb5…  `/root/biotop-vor-t4-04/bau/r4_fix1.py`
- 2026-09-24T13:32:00+02:00        3811 B  sha256 d011cd6cb38ff10c…  `/root/biotop-vor-t4-04/FEHLALARM-SICHERHEITSFILTER.md`
- 2026-09-24T13:31:44+02:00        1469 B  sha256 86b1e2a4646a6ec7…  `/root/biotop-vor-t4-04/bau/TEILLAUF-1.txt`
- 2026-09-24T13:31:34+02:00         585 B  sha256 9df089ec3c4a6cd4…  `/root/biotop-vor-t4-04/s1/TORZEILE-SCHWAECHEN-T3.txt`
- 2026-09-24T13:31:34+02:00        1951 B  sha256 756b449025c0d4b9…  `/root/biotop-vor-t4-04/s1/TORZEILE-SCHWAECHEN-T3.json`
- 2026-09-24T13:31:34+02:00        2539 B  sha256 13d0d2ea942f0f0c…  `/root/biotop-vor-t4-04/s1/torzeile_schwaechen_t3.py`
- 2026-09-24T13:31:18+02:00        5702 B  sha256 516419cdf6cd1ab6…  `/root/biotop/biotop/kern/gegenzeugen.py`
- 2026-09-24T13:31:18+02:00       18256 B  sha256 0f8bf616c657f2c2…  `/root/biotop/biotop/nachspiel.py`
- 2026-09-24T13:31:13+02:00        5717 B  sha256 b3236479354d1b98…  `/root/biotop-vor-t4-04/bau/r4_nachspiel_torzeile.py`
- 2026-09-24T13:28:06+02:00       21421 B  sha256 47f1a6f4b5840652…  `/root/biotop/biotop/kern/ts/verhalten-runner.mjs`
- 2026-09-24T13:28:06+02:00       62290 B  sha256 9a49c4fa74cd9c9a…  `/root/biotop/biotop/kern/py/verhalten.py`
- 2026-09-24T13:28:01+02:00        5144 B  sha256 d289727a96e30540…  `/root/biotop-vor-t4-04/bau/r4_muster.py`
- 2026-09-24T13:24:41+02:00       15643 B  sha256 d6f239c48651b386…  `/root/biotop/tests/test_t3_verhaltensvergleich.py`
- 2026-09-24T13:24:41+02:00       19226 B  sha256 de0954067398bb58…  `/root/biotop/tests/test_vor_t4_02.py`
- 2026-09-24T13:24:10+02:00       61597 B  sha256 6f91e7bdc90ff4ab…  `/root/biotop/biotop/lauf.py`
- 2026-09-24T13:24:10+02:00       52285 B  sha256 b3d1a32b0db6cdcd…  `/root/biotop/biotop/kern/messgeraet.py`
- 2026-09-24T13:24:10+02:00       73136 B  sha256 f16d707dc89b2319…  `/root/biotop/biotop/organe/aegis.py`
- 2026-09-24T13:24:07+02:00       22957 B  sha256 5fca6f32397c9e81…  `/root/biotop-vor-t4-04/bau/r4_deckung.py`
- 2026-09-24T13:18:07+02:00        2232 B  sha256 6770bad3857251b8…  `/root/biotop/biotop/kern/ts/deckung.mjs`
- 2026-09-24T13:18:07+02:00        2254 B  sha256 bb39d462eafecb3d…  `/root/biotop/biotop/kern/ts/deck-setup.mjs`
- 2026-09-24T13:18:07+02:00        4840 B  sha256 03540d2f64dcf138…  `/root/biotop/biotop/kern/ts/kanon.mjs`
- 2026-09-24T13:18:03+02:00        9891 B  sha256 d362802d98bcd72e…  `/root/biotop-vor-t4-04/bau/r4_sonde_ts.py`
- 2026-09-24T13:17:25+02:00       17000 B  sha256 03f36d5c9d3efab3…  `/root/biotop/biotop/organe/eichung.py`
- 2026-09-24T13:17:09+02:00       17834 B  sha256 3c95eac82e5477d3…  `/root/biotop/biotop/organe/vorspann.py`
- 2026-09-24T13:17:06+02:00       13086 B  sha256 a47f007cd1f7cebf…  `/root/biotop-vor-t4-04/bau/r4_stufe2.py`
- 2026-09-24T13:08:53+02:00       20290 B  sha256 0ad276fa31ba215f…  `/root/biotop-vor-t4-04/bau/r4_sonde_py.py`
- … 6 weitere

## Laufende Prozesse (Auszug)

```
 817038     950 /usr/bin/bash -lic set +m; bash /root/biotop-vor-t4-04/bau/kette.sh > /root/biotop-vor-t4-04/bau/KETTE.txt 2>&1; echo rc=$?; tail -16 /root/biotop-vor-t4-04/bau/KETTE.txt
 817055     950 bash /root/biotop-vor-t4-04/bau/kette.sh
 821005     905 bash /root/biotop-vor-t4-04/job_commit_regression.sh
 821033     905 /root/biotop-t3/venv/bin/python -m pytest tests/ -q -m not integration -p no:cacheprovider -rfEs --durations=8 --junitxml=/root/biotop-vor-t4-04/REGRESSION.junit.xml
 851131     484 /usr/bin/bash -lic set +m; bash /root/biotop-vor-t4-04/bau/kette_nachtrag.sh > /root/biotop-vor-t4-04/bau/KETTE-NACHTRAG.txt 2>&1; echo rc=$?; tail -12 /root/biotop-vor-t4-04/bau/KETTE
 851148     484 bash /root/biotop-vor-t4-04/bau/kette_nachtrag.sh
 863714       3 docker run --rm --name biotop-f2f53f2970a2 --network none --memory 512m --memory-swap 512m --cpus 1 --pids-limit 256 --read-only --tmpfs /tmp:rw,size=64m --security-opt no-new-privileg
 863777       2 node /opt/biotop-ts/node_modules/typescript/bin/tsc --pretty false --project /tmp/ts-bau.json
```
