# Zwischenbericht — automatisch ausgelöst (biotop-vor-t4-02)

Ausgelöst 2026-09-24T00:48:47+02:00 vom Zwischenbericht-Wächter (Cron, ohne Modell). Sitzung `20260923_194003_92313ee1`, Werkzeugrunde **104 von 150** (Schwelle –).
Anlass: Kontextfüllung 80.6 % (806169 von 1000000 Token, anthropic/claude-opus-5-5, Stand 2026-09-24T00:48:02+02:00; Schwelle 80 %).
Regel (Philipp, 23.09.2026): Zwischenbericht spätestens bei 120 von 150 Aufrufen — ausgelöst, nicht erinnert.
Die Übergabedateien sind der zuletzt vom Agenten geschriebene Stand; alle übrigen Abschnitte sind in diesem Augenblick mechanisch gelesen.

## Auftrag dieses Turns (Nachricht 14624, 2026-09-23T22:32:40+02:00)

```
Richtig, nicht abgenommen — und die fehlende Python-Sonde ist der wichtigste Fund: T4 wäre gegen „schneller, aber falsch" ungeschützt gewesen. Entscheidungen Chat-Claude zu deinen fünf Fragen: (1) Weißraum gehört zur Tarifsprache, soweit die versiegelte Normalversion ihn rechnet — S1 ist an K2868 damit nicht sauber behoben, das korrigiert den T3-Befund, und mein Prüfstein „K2868 muss bestehen" war falsch; prüf dasselbe an K3044, der S1-Behebung aus Lauf 38, und korrigiere die Schwächenzählung von Lauf 38, falls nötig. (2) Python-Sonde vor T4, die Torzeile bleibt — Grundsatz 11 gilt für jede Sprache. (3) Kein Wirkungskreis, der selbst noch nicht verlässlich ist; stattdessen wird jeder Laufzeitriss vor der Ablehnung einmal gepaart nachgemessen, und nur ein bestätigter Riss lehnt ab. (4) Deckung je Abweichung, wie Grundsatz 11 es sagt. (5) Wächter je Turn. Auftrag Behebungsrunde 2 vor T4: Python-Sonde im selben Umfang wie die TypeScript-Sonde (einzeln, Folge, Alias, Mutation, Rücksetzung); Korpus aus den Verträgen mit Randfällen und Varianten der Eingabeform — die Weißraumlücke zeigt, dass Randwerte allein nicht reichen; Deckung je Abweichung; Bestätigungsmessung vor jeder Laufzeitablehnung; eine gepaarte Messung mit fehlenden Werten ist ungültig, deine rote Spezifikation wird grün; die vier Gedächtnissperre-Tests werden ohne Kammerimage rot statt übersprungen. Gegenproben durch den Laufweg: K2868 wird mit dem erweiterten Korpus abgelehnt; K2904 und K3091 werden in drei von drei Durchgängen gleich entschieden; an einem Python-Prüfwerk scheitert ein eingebauter Zwischenspeicher-Fehler. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, Abschlussordner laeufe/biotop-vor-t4-02/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

## Übergabe (vom Agenten gepflegt)

- `/root/biotop-vor-t4-02/UEBERGABE.md` — Stand 2026-09-24T00:38:00+02:00, als eigene Datei im Ordner

## Letzte Äußerungen des Agenten in diesem Turn (neueste zuletzt)

- 2026-09-23T23:53:57+02:00: Jetzt der erste echte Kammerlauf der Python-Sonde am Prüfwerk, direkt über `verhaltensvergleich.pruefen` (Diagnose vor den Laufweg-Tests).
- 2026-09-24T00:18:47+02:00: Während die Vorprüfung läuft: der Bericht wird vorbereitet (mit Platzhaltern), dazu die Übergabe.
- 2026-09-24T00:29:27+02:00: Alle 18 Laufweg- und Kammertests grün. Jetzt Gegenprobe der vier Gedächtnissperre-Tests ohne Image, dann Commit und volle Regression.
- 2026-09-24T00:31:07+02:00: Commit `6243377` steht; die volle Regression läuft (~25 min), danach drei Nachspiel-Durchgänge. Inzwischen der Prüfauftrag für das eine Review.
- 2026-09-24T00:38:48+02:00: Commit `6243377` steht. Die volle Regression mit anschließend drei Nachspiel-Durchgängen läuft im Hintergrund (`proc_72cfe583df40`), das Review ebenfalls (`deleg_ce891021`). Beide melden sich, wenn sie fertig sind; dann fülle ich die Platzhalter in `BERICHT.md` und veröffentliche nach `laeufe/biotop-vor-t4-02/`.

## Repositories

`/root/biotop`:
```
6243377 Vor T4, Runde 2: Python-Sonde, Deckung je Abweichung, Formvarianten, bestätigte Laufzeitrisse
330b4ec Vor T4: Review-Befunde eingearbeitet (ein Reviewdurchgang zu 58bd9f9)
58bd9f9 Vor T4: Behebungsrunde — Vorbedingungen 1–11 aus Masterprompt Fassung 8
(Arbeitsbaum sauber)
```

## Seit Turnbeginn geänderte Dateien (neueste zuerst)

- 2026-09-24T00:38:44+02:00         964 B  sha256 dbdd72540162d2af…  `/root/biotop-vor-t4-02/KASSE.md`
- 2026-09-24T00:38:37+02:00        7642 B  sha256 2957476b6ed30ab8…  `/root/biotop-vor-t4-02/veroeffentlichen.py`
- 2026-09-24T00:38:00+02:00        3471 B  sha256 80dceb12f041a256…  `/root/biotop-vor-t4-02/UEBERGABE.md`
- 2026-09-24T00:38:00+02:00       18849 B  sha256 be58ffc599cd3e76…  `/root/biotop-vor-t4-02/BERICHT.md`
- 2026-09-24T00:34:40+02:00         376 B  sha256 bb4e94cca3e86dea…  `/root/biotop-vor-t4-02/REGRESSION.txt`
- 2026-09-24T00:31:07+02:00        5310 B  sha256 6c66cc130822f39e…  `/root/biotop-vor-t4-02/REVIEW-AUFTRAG.md`
- 2026-09-24T00:30:17+02:00        2255 B  sha256 24841da3fdcfcacc…  `/root/biotop-vor-t4-02/JOB-COMMIT-REGRESSION.txt`
- 2026-09-24T00:30:17+02:00      124756 B  sha256 3f18cc38a5726c7f…  `/root/biotop-vor-t4-02/KERN-COMMIT.patch.txt`
- 2026-09-24T00:30:17+02:00        3087 B  sha256 0f722834b41ea2ac…  `/root/biotop-vor-t4-02/COMMIT-STAT.txt`
- 2026-09-24T00:30:13+02:00        2388 B  sha256 3297f26887220b7b…  `/root/biotop-vor-t4-02/job_commit_regression.sh`
- 2026-09-24T00:30:13+02:00        2398 B  sha256 cf147c9b14aba7b7…  `/root/biotop-vor-t4-02/COMMIT-NACHRICHT.txt`
- 2026-09-24T00:30:13+02:00        1654 B  sha256 a3d791c4b3767266…  `/root/biotop-vor-t4-02/py/python_laufzeit_teilausfall.py`
- 2026-09-24T00:29:45+02:00        1310 B  sha256 377dd71bf372fc77…  `/root/biotop-vor-t4-02/sperre/OHNE-IMAGE.txt`
- 2026-09-24T00:28:37+02:00       17055 B  sha256 11812bb0af4985df…  `/root/biotop/tests/test_vor_t4_02.py`
- 2026-09-24T00:28:01+02:00       23673 B  sha256 58a4e2fb7d5ffe69…  `/root/biotop/biotop/organe/verhaltensvergleich.py`
- 2026-09-24T00:28:01+02:00       28356 B  sha256 6890e5d986377395…  `/root/biotop/biotop/kern/py/verhalten.py`
- 2026-09-24T00:28:01+02:00        1922 B  sha256 29f947e8a4c941d5…  `/root/biotop/biotop/kern/ts/deckung.mjs`
- 2026-09-24T00:28:01+02:00        1788 B  sha256 193fc17f8cae3a83…  `/root/biotop/biotop/kern/ts/vitest.deck.config.mjs`
- 2026-09-24T00:28:01+02:00        1204 B  sha256 0c3f54563ca36fc3…  `/root/biotop/biotop/kern/ts/deck-setup.mjs`
- 2026-09-24T00:27:56+02:00        3197 B  sha256 98b4f01f9f8a18b3…  `/root/biotop-vor-t4-02/bau/deckungsprobe_anhang.py`
- 2026-09-24T00:27:56+02:00        9445 B  sha256 58a7dea856d7fa9a…  `/root/biotop-vor-t4-02/bau/aufzeichner_haerten.py`
- 2026-09-24T00:24:48+02:00        2821 B  sha256 e913efaca617e448…  `/root/biotop-vor-t4-02/bau/VORPRUEFUNG.txt`
- 2026-09-24T00:24:48+02:00       13597 B  sha256 e611b64854d161c9…  `/root/biotop-vor-t4-02/bau/nachspiel-vorab/k2868.json`
- 2026-09-24T00:22:30+02:00        3021 B  sha256 29823cda7d35267e…  `/root/biotop-vor-t4-02/bau/VV-KAMMERPROBE-arbeitsbaum.json`
- 2026-09-24T00:18:38+02:00         986 B  sha256 a1ef197872bde6cb…  `/root/biotop-vor-t4-02/bau/vorpruefung.sh`
- 2026-09-24T00:18:38+02:00        2425 B  sha256 d937f7757841e188…  `/root/biotop-vor-t4-02/bau/vv_kammerprobe_02.py`
- 2026-09-24T00:18:30+02:00       23243 B  sha256 d36ec8f60af8122e…  `/root/biotop/tests/test_eichproben.py`
- 2026-09-24T00:15:39+02:00        2497 B  sha256 6d157f4a14592f0b…  `/root/biotop-vor-t4-02/bau/diagnose_eichproben.py`
- 2026-09-24T00:14:36+02:00         553 B  sha256 50d41f14ac076645…  `/root/biotop-vor-t4-02/bau/TEILLAUF-2.txt`
- 2026-09-24T00:11:23+02:00       24932 B  sha256 8220c6c4f0d3221b…  `/root/biotop/tests/test_vorspann.py`
- 2026-09-24T00:11:23+02:00       10914 B  sha256 0bb7b6976bab7b12…  `/root/biotop/tests/test_t3_python_annahmen.py`
- 2026-09-24T00:06:24+02:00        4942 B  sha256 e62167450e263876…  `/root/biotop-vor-t4-02/bau/ERSTLAUF-ALLE.txt`
- 2026-09-24T00:02:50+02:00        6930 B  sha256 25e05b09f5dc2987…  `/root/biotop/tests/speicherwerk.py`
- 2026-09-24T00:00:49+02:00         751 B  sha256 5fd53dea55acab35…  `/root/biotop-vor-t4-02/bau/ERSTLAUF.txt`
- 2026-09-23T23:57:54+02:00       14256 B  sha256 1bb94ef81ec1f92d…  `/root/biotop/tests/test_t3_verhaltensvergleich.py`
- 2026-09-23T23:54:03+02:00        3239 B  sha256 95b7b918c917c133…  `/root/biotop-vor-t4-02/py/DIAGNOSE-PY-SONDE.txt`
- 2026-09-23T23:54:03+02:00        7015 B  sha256 911bb49d5feb889a…  `/root/biotop-vor-t4-02/py/DIAGNOSE-PY-SONDE.json`
- 2026-09-23T23:53:57+02:00        1865 B  sha256 18aa5d4571c5a05e…  `/root/biotop-vor-t4-02/py/diagnose_py_sonde.py`
- 2026-09-23T23:53:08+02:00        3620 B  sha256 db02d6050302acc9…  `/root/biotop-vor-t4-02/bau/deckung_umbau_organ.py`
- 2026-09-23T23:52:51+02:00       14948 B  sha256 580c358352f90b77…  `/root/biotop/biotop/kern/ts/verhalten-runner.mjs`
- 2026-09-23T23:52:51+02:00        1963 B  sha256 4569997222f58e3a…  `/root/biotop/biotop/kern/ts/kanon.mjs`
- 2026-09-23T23:52:46+02:00       12026 B  sha256 bc4fc041659219b6…  `/root/biotop-vor-t4-02/bau/deckung_umbau.py`
- 2026-09-23T23:49:08+02:00        3127 B  sha256 8e7ada59f0457478…  `/root/biotop/tests/conftest.py`
- 2026-09-23T23:49:08+02:00       58894 B  sha256 92c796b12ea5b8cc…  `/root/biotop/biotop/lauf.py`
- 2026-09-23T23:49:08+02:00       67616 B  sha256 51372a9e67d80239…  `/root/biotop/biotop/organe/aegis.py`
- 2026-09-23T23:49:08+02:00       44971 B  sha256 a6f990817009bd0d…  `/root/biotop/biotop/kern/messgeraet.py`
- 2026-09-23T23:49:03+02:00       13740 B  sha256 ef68603b127b22f0…  `/root/biotop-vor-t4-02/bau/laufzeit_umbau.py`
- 2026-09-23T23:43:57+02:00       17060 B  sha256 a863774180a63ed2…  `/root/biotop-vor-t4-02/bau/vv_umbau.py`
- 2026-09-23T23:38:43+02:00        4177 B  sha256 25058ee175c818a8…  `/root/biotop/biotop/kern/ts/verhalten.mjs`
- 2026-09-23T23:38:43+02:00        2190 B  sha256 67fbce947aa62004…  `/root/biotop/biotop/kern/ts/main.mjs`
- 2026-09-23T23:38:39+02:00       10709 B  sha256 b84374f7f9c501e7…  `/root/biotop-vor-t4-02/bau/ts_seite.py`
- 2026-09-23T23:04:31+02:00         689 B  sha256 157a64fa04d093a7…  `/root/biotop-vor-t4-02/s1/S1-STAENDE.txt`
- 2026-09-23T23:04:31+02:00       11298 B  sha256 23d8a0e4ec1e68b2…  `/root/biotop-vor-t4-02/s1/S1-STAENDE.json`
- 2026-09-23T23:03:58+02:00        5530 B  sha256 97a36dd22c4dbe36…  `/root/biotop-vor-t4-02/s1/s1_staende.py`

## Laufende Prozesse (Auszug)

```
 315835    1111 /usr/bin/bash -lic set +m; cd /root/biotop-vor-t4-02 && bash job_commit_regression.sh > JOB-COMMIT-REGRESSION.txt 2>&1
 315881    1110 /root/biotop-t3/venv/bin/python -m pytest tests/ -q -m not integration -p no:cacheprovider -rfEs --durations=8 --junitxml=/root/biotop-vor-t4-02/REGRESSION.junit.xml
 360985       9 docker run --rm --name biotop-7359b53973fc --network none --memory 512m --memory-swap 512m --cpus 1 --pids-limit 256 --read-only --tmpfs /tmp:rw,size=64m --security-opt no-new-privileg
 361123       2 node /opt/biotop-ts/node_modules/knip/bin/knip.js --no-gitignore --tsConfig /tmp/ts-bau.json --config _messgeraet/ts/knip.json --reporter json --include files,exports,nsExports,types,c
```
