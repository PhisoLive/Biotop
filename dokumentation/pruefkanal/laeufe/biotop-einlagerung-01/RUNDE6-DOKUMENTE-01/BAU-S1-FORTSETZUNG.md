# Fortsetzung Bau S1 (Runde 6) nach technischem Abbruch

Du setzt den Bauauftrag `/root/biotop-vor-t4-06/BAU-S1-SONDE.md` fort. Er gilt unverändert. Dazu gelten die zwei
Nachsteuerungen unten (wörtlich), die der erste Bauende während seines Laufs erhielt. Antworte und schreibe auf Deutsch.
Warum der erste Bauende abbrach, steht in `/root/biotop-vor-t4-06/S1-ABBRUCH.md` (lies das zuerst, es ändert deine
Arbeitsweise).

## Stand (gemessen 25.09. 03:45)
- **Schritt 1 ist erledigt: die roten Spezifikationen.**
  - `/root/biotop/tests/test_vor_t4_06.py`: 27 Testfunktionen, 63 Fälle, sha256 `79c08dc7d3b7def3…`, geschrieben 02:48.
  - Vorher an `0c2f058`: `bau/S1-VORHER-0c2f058.txt`, zusammen 47 von 63 Fällen rot.
    - Gruppe a (ohne Hänger): 43 rot, 16 grün, 4 abgewählt, 130 s.
    - Gruppe b (Hänger/Fristen): 4 rot, 59 abgewählt, 322 s.
  - Kopie des Stands `0c2f058` mit den Spezifikationen: `/tmp/r6-s1/vorher/`, Skript `/tmp/r6-s1/vorher.sh a|b`.
  - Lokale Proben: `/tmp/r6-s1/probe_py.py` und `probe_flags.py` (welche Typen C-Typen sind).
- **Schritte 2–5 sind nicht begonnen.** `biotop/kern/py/verhalten.py`, `biotop/organe/verhaltensvergleich.py` und
  `biotop/organe/aegis.py` sind unverändert gegen HEAD. Es gibt keine Einordnung des Vorher-Ergebnisses, keinen Plan und
  keine Liste geänderter Tests.
- **Andere Bauende im selben Baum `/root/biotop` (nicht anfassen):**
  - S3 ist fertig: neu `biotop/organe/stufe2.py` und `tests/test_stufe2_eichphase.py`; geändert `biotop/organe/vorspann.py`,
    `biotop/lauf.py`, `biotop/nachspiel.py`, `tests/test_vorspann.py`; in `tests/test_vor_t4_05.py` nur `test_s6_*`.
  - S2 läuft: `biotop/tor4.py`, neu `tests/test_tor4_zeilen.py`.
  - In `tests/test_vor_t4_05.py` gehören dir `test_v1_*`, `test_f2_*`, `test_a3_*`, `test_k4_*`, `test_l7_*` und
    `test_e8_*`, soweit sich ihre Spezifikation ändert.

## Zuerst: Einordnung des Vorher-Ergebnisses
Schreibe `bau/S1-VORHER-EINORDNUNG.md` und ordne jeden der 63 Fälle einer von drei Arten zu:
- rot an seiner Zusicherung;
- rot, weil die neue Schnittstelle fehlt (welche);
- grün als Gegenprobe.

Jede grüne Probe und jede rote Gegenprobe ist ein Fehler der Spezifikation. Berichtige sie und lass für die geänderten
Fälle den Vorher-Lauf an `0c2f058` erneut laufen; das Ergebnis hängst du an `bau/S1-VORHER-0c2f058.txt` an. Prüfe
außerdem, dass die Nachsteuerungen (a) und (b) als Spezifikation abgedeckt sind. Vermutlich sind sie es durch
`test_b3_kind_der_eingrenzung_mit_frist_der_elternseite`,
`test_b3_eingrenzung_mit_verklemmten_kindern_ist_gescheitert_nie_werkverhalten` und
`test_b3_ts_lastabbruch_trifft_betroffene_oder_unveraenderte_funktion`. Danach folgen die Schritte 2–5 aus
`BAU-S1-SONDE.md`.

## Arbeitsweise (verbindlich, wegen des Abbruchs)
1. **Plane nie den ganzen Umbau in einem Denkschritt.** Schreibe Plan und Zwischenüberlegungen fortlaufend nach
   `bau/S1-PLAN.md`.
   - Je Entscheidung ein eigenes Bauskript, in dieser Reihenfolge: `bau/r6_s1_e7.py` (Ausnahmen), `bau/r6_s1_e1.py`
     (Verfälschung und R6-4), `bau/r6_s1_e2.py` (undurchsichtige Objekte), `bau/r6_s1_e3.py` (Enthaltung je Funktion
     und Frist).
   - Nach jedem Skript laufen die zugehörigen Spezifikationen, dann kommt das nächste.
   - Ist eine Überlegung größer als eine Bildschirmseite, gehört sie in die Plan-Datei, nicht in den Kopf.
2. **Keine Hintergrundprozesse:** kein `background`, kein `notify`. Alles läuft im Vordergrund; lange Testläufe teilst
   du in Stücke unter 600 s, wie in `vorher.sh a|b`.
3. **Befehle mit Heredoc, Pipes oder mehreren Teilen** schreibst du als Skriptdatei und führst die aus. Jede Sperre oder
   Freigabeabfrage meldest du wörtlich (Befehl und Meldung) und hältst an dieser Stelle an. Nie umformulieren, nie einen
   anderen Weg nehmen.
4. **Arbeitskopien und Bauskripte:** `TMPDIR=/tmp/r6-s1`, Arbeitskopien dort. Die Bauskripte arbeiten alles oder nichts,
   mit zwei Lesungen: Anker prüfen, dann `--trocken`, dann unmittelbar vor dem Schreiben neu lesen, neu prüfen und
   schreiben. Tests führst du aus `/root/biotop` heraus aus (`pytest.ini` dort) mit `/root/biotop-t3/venv/bin/python`.
5. **Kein Commit, kein Modellaufruf, kein Netz.** Die Kammer (docker) ist für die Spezifikationen erlaubt.

## Nachsteuerungen an den ersten Bauenden (wörtlich)
„Hinweis zu geteilten Dateien: tests/test_vor_t4_05.py wird von zwei Bauenden geändert — S1 (Sonde: test_v1_*,
test_f2_*, test_a3_*, test_k4_*, test_l7_*, test_e8_*, soweit die Spezifikation sich ändert) und S3 (Stufe 2: nur
test_s6_*). Dort nur gezielte Ersetzungen einzelner Testfunktionen (patch-Werkzeug oder Skript mit Anker), nie die ganze
Datei neu schreiben, und unmittelbar vor jedem Schreiben neu lesen. Jede Änderung mit Grund in deiner Liste geänderter
Tests.“

„Zwei Ergänzungen zu Entscheidung 3 (Philipp, 24.09.): (a) Die Frist in der Eingrenzung (Kindprozesse per os.fork) muss
auch von der Elternseite durchgesetzt werden: Lesen der Pipe mit Zeitgrenze (select/poll), danach Kind mit SIGKILL
beenden und waitpid — ein Kind, das in C-Code verklemmt (fork in einem Werk mit laufenden Threads, Liste U-1), darf die
Sonde nicht bis zum Kammerlimit anhalten; Ergebnis dann wie „Eingrenzung gescheitert“ (gezählte Enthaltung der
Lastfunktionen), nie als Werkverhalten. (b) In tests/test_vor_t4_06.py zusätzlich eine Unit-Gegenprobe am Organ mit
gestellter Sonde für den TypeScript-Weg: Bereichslast bricht an der Vorgeneration ab, last_aufrufe enthält eine Funktion
eines vom Kandidaten geänderten Moduls → zurückgestellt (Enthaltung, betroffene Funktion); enthält sie nur Funktionen
unveränderter Module → geurteilt am Rest. Keine TS-Kammerprobe (die ist vor T5).“

## Lieferung
Wie in `BAU-S1-SONDE.md`, Abschnitt „Rote Spezifikationen und Lieferung“, Schritte 2–5, dazu
`bau/S1-VORHER-EINORDNUNG.md` und `bau/S1-PLAN.md`. Der Schlussbericht (deine letzte Antwort) nennt:
- geänderte Dateien;
- Vorher (x von y rot an `0c2f058`, nach Arten);
- Teststand x von y;
- offene Punkte und Sperren (wörtlich).
