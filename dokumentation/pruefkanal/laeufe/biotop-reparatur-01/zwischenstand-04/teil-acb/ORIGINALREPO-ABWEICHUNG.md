# ACHTUNG Parent: Originalrepo während Teilauftrag verändert

Die Endprüfung des isolierten A/C/B-Agenten ist an der Originalrepo-Unveränderlichkeit gescheitert. Alle eigenen Produktionscode-Schreibaufrufe dieses Teilagenten zielten ausschließlich auf `/root/reparatur-01/teil-acb/repo/`. Es wird nichts im Original zurückgesetzt.

In `/root/biotop` sind gegenüber dem zu Beginn erhobenen SHA256/mtime/Größenmanifest verändert:
- `.gitignore`
- `biotop/kern/messgeraet.py`
- `biotop/lauf.py`
- `biotop/organe/eichung.py`

Zusätzlich ungetrackt laut Endprüfung: `README.md`, `biotop/organe/vorspann.py`, `pytest.ini`, `requirements-test.txt`, `tests/`.

Die Ursache/Urheberschaft ist aus dieser Prüfung nicht ableitbar. Bitte bei anderen Workstreams prüfen. Keine Erfolgsaussage „Originalrepo unverändert“ übernehmen. Die private Ausgangs-DB ist dagegen SHA256/Größe/mtime-identisch.

Der A/C/B-Diff wird ausdrücklich gegen die eingefrorene Git-Archive-Baseline b42dc941e7fcb66632ba6a0e13b8df106a270a31 erzeugt, NICHT gegen die inzwischen veränderte Original-Arbeitskopie. Die eingefrorenen Bestands-Replays sind hiervon nicht betroffen.

Beleg: `/root/reparatur-01/teil-acb/ausgaben/20-abschluss.txt`, `schutz-vorher.json` und die folgenden `schutz-nachher.json`/`schutz-ergebnis.json`.
