# Bauauftrag S3 (Runde 6, Entscheidung 4): Eichphase der Stufe-2-Last, versiegelt

Du baust einen Teil der Behebungsrunde 6 vor T4 des Biotop-Projekts. Antworte und schreibe auf Deutsch. Du setzt NUR das
Folgende um, committest nichts und startest keine Hintergrundprozesse (nur Vordergrundbefehle ≤ 600 s).

## Umgebung
- Code `/root/biotop` (git, HEAD `0c2f058`, NICHT committen), Python `/root/biotop-t3/venv/bin/python`,
  Tests `cd /root/biotop && /root/biotop-t3/venv/bin/python -m pytest <datei> -q -p no:cacheprovider -rfE`.
- Arbeitsordner `/root/biotop-vor-t4-06/` (Unterordner `bau/`), eigener Temp-Ordner `/tmp/r6-s3/` (setze `TMPDIR`).
- Parallel arbeiten zwei andere Bauende im selben Baum: fasse NUR deine Dateien an (unten). Kein Modellaufruf, kein Netz.
  Keine Laufzeitmessungen in der Kammer (die fahre ich später allein); deine Tests stellen die Messung.
- Lange oder mehrteilige Befehle als Skript unter `/tmp/r6-s3/`. Wird ein Befehl gesperrt, hältst du an und berichtest
  Befehl und Meldung wörtlich.

## Deine Dateien (nur diese)
- neu `biotop/organe/stufe2.py`; `biotop/organe/vorspann.py`; `biotop/lauf.py` (nur die Stellen der Stufe-2-Last:
  `mass_einfrieren`, `generation`, `kurve_nachrechnen`, `_referenzlast`-Nutzung); `biotop/nachspiel.py` (nur Stufe 2);
  neu `tests/test_stufe2_eichphase.py`; `tests/test_vorspann.py` und in `tests/test_vor_t4_05.py` nur die Tests
  `test_s6_*` (anpassen, wenn der Vorspann jetzt ein Siegel verlangt — jede Anpassung mit Grund in deiner Liste).
- Nicht anfassen: `biotop/__main__.py` (Befehl `biotop stufe2 <lauf>` verdrahte ich), `tests/drahtwerk.py`,
  `tests/test_verdrahtung.py`, `biotop/kern/py/*`, `biotop/organe/verhaltensvergleich.py`, `biotop/organe/aegis.py`.

## Auftrag (Entscheidung Chat-Claude 4, 24.09.)
„Stufe-2-Last (R6-3): in einer eigenen Eichphase so bemessen, dass die Spannweite über acht Messungen unter 0,25 liegt,
bei mindestens 10 ms je Stichprobe, dann versiegelt; die Rauschmessung im Vorspann bleibt getrennt und darf sperren —
keine reine Dauerregel, denn `zahlen` läuft mit 19 ms ruhig, `eingang` mit 35 ms nicht.“
Hintergrund: `/root/biotop-vor-t4-05/BERICHT.md` §6 und `proben/STUFE2-EICHUNG.*` (W 60 sperrte `eingang` in 3 von 8).

## Bau
1. `stufe2.eichen(con, lauf_id, *, messen_einmal=None, runden_max=5, messungen=8) -> dict`:
   - Vorlage: die Stufe-2-Datei des Werks (`lauf._referenzlast(werk_name, paket, 2)`). Sie trägt genau eine
     **W-Zeile** mit den Wiederholungen je Bereich: TypeScript `const W = { a: 1, b: 2 };`, Python `W = {'a': 1, 'b': 2}`.
     Fehlt sie oder fehlt ein Bereich des Maßes darin: laut scheitern (`Stufe2Fehler`).
   - Je Runde `messungen` (8) Kammerläufe mit `eichung.laufzeit_einmal` (dasselbe Instrument wie die Rauschmessung; ein
     Kammerlauf liefert alle Bereiche), je Kammerlauf die Dauer messen.
   - Kriterium je Bereich: (max − min) / Median < 0,25 über die 8 Werte UND jeder Wert ≥ 10 ms. Erfüllt ein Bereich es
     nicht: seine Wiederholungen verdoppeln (W-Zeile neu schreiben), nächste Runde nur mit geänderter Last neu messen
     (alle Bereiche, weil ein Kammerlauf alle misst; erfüllte Bereiche behalten ihr W).
   - Ein Kammerlauf ≥ 60 s (Grenze `vorspann.STUFE2_KAMMERLAUF_S`) oder mehr als `runden_max` Runden: laut scheitern.
   - Erfolg: **versiegeln** — neue Tabelle `stufe2_siegel(lauf_id INTEGER PRIMARY KEY, werk_id, text, sha256, w_json,
     messungen_json, erstellt_am)`, Protokoll `stufe2.versiegelt` (sha256, W, je Bereich Median/Spannweite/Minimum,
     Runden, Kammerläufe), Eichkosten über `eichung.kosten_buchen(…, 'stufe2', …, modellaufrufe=0, kosten_eur=0.0)`.
     Ein zweites `eichen` für denselben Lauf verweigert (Siegel ist fest; Verfassungssatz 2: neues Messgerät = neuer Lauf).
   - Rückgabe: Siegel samt Messwerten (JSON-fähig).
2. `stufe2.lesen(con, lauf_id) -> str | None` (versiegelter Text) und `stufe2.siegel(con, lauf_id) -> dict | None`.
3. `vorspann._ausfuehren`: die Vergleichslast Stufe 2 ist die **versiegelte** Last; ohne Siegel verweigert der Vorspann vor
   jeder Messung („Stufe-2-Last nicht geeicht und versiegelt — zuerst `biotop stufe2 <lauf>`“). Die Rauschmessung an
   Stufe 2 bleibt wie heute (5 Kammerläufe, darf sperren), die 60-s-Grenze bleibt. Der Nachweis trägt `stufe2_sha256`.
4. `lauf.py`: `generation` setzt `tausch["_referenzlast_laufzeit"]` aus dem Siegel (Lauf mit Siegel), `mass_einfrieren`
   und `kurve_nachrechnen` ebenso; ohne Siegel (alte Läufe) bleibt es beim bisherigen Verhalten (Datei).
5. `nachspiel.py`: trägt die Quell-DB ein Siegel für den Lauf, gilt die versiegelte Last; sonst wie bisher die Datei.
6. Für die Befehlszeile brauche ich nur `stufe2.eichen(con, lauf_id)` mit JSON-fähiger Rückgabe.

## Tests (`tests/test_stufe2_eichphase.py`, Messung gestellt, ohne Kammer)
- Kriterium: ruhiger Bereich bleibt, unruhiger (Spannweite ≥ 0,25) wird verdoppelt, zu kurzer (< 10 ms) wird verdoppelt,
  bis beide erfüllt; Siegel mit sha256 und W; zweites `eichen` verweigert.
- Kammerlauf ≥ 60 s → scheitert; `runden_max` überschritten → scheitert; W-Zeile fehlt → scheitert.
- Vorspann ohne Siegel verweigert, mit Siegel läuft er und misst die Rauschmessung an der versiegelten Last.
- `generation` nutzt die versiegelte Last (gestellter Aufruf, wie die vorhandenen Unit-Tests in `tests/test_vorspann.py`).

## Lieferung
- Umbau als alles-oder-nichts-Skript `bau/r6_s3_stufe2.py` (bricht ohne Schreiben ab, wenn ein Anker fehlt; Protokoll
  `bau/R6-S3-STUFE2.txt`).
- Testlauf `tests/test_stufe2_eichphase.py tests/test_vorspann.py` und `tests/test_vor_t4_05.py -k test_s6` (getrennte
  Aufrufe), Ausgabe nach `bau/TEILLAUF-S3.txt` (ein `-q`, `-rfE`).
- Liste geänderter älterer Tests mit Grund: `bau/S3-GEAENDERTE-TESTS.md`.
- Schlussbericht (deine letzte Antwort): geänderte Dateien, Teststand x von y, offene Punkte, Sperren (oder „keine“).
