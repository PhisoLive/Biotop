# Pflichtvorspann — Teil-Lieferung

**Implementiert und isoliert geprüft: 70/70 Tests grün, keine Fehler/Skips.** Derselbe Stand nach tatsächlicher Patchanwendung in zweiter Kopie nochmals 70/70 grün. Kein echter Acht-Proben-Abnahmenachweis: dafür ist die frische integrierte Elternsitzung zuständig. Keine bezahlten Biotop-Modelle oder produktiven Läufe gestartet.

## Patch (genau sechs Dateien)

`biotop/organe/vorspann.py`, `biotop/lauf.py`, `biotop/__main__.py`, `pruefung/vorspann.py`, `tests/test_vorspann.py`, `tests/test_vorspann_cli.py`.

Patch:
/root/reparatur-01/teil-vorspann/vorspann.patch

SHA256: `fcc8c80d02a913e821c8d55d1c724602fc2094258ae33ba9283e53202fb80669`

Dateiprüfsummen:
/root/reparatur-01/teil-vorspann/DATEIEN-SHA256.txt

Schnittstelle und Grenzen:
/root/reparatur-01/teil-vorspann/SCHNITTSTELLE.md

## Erreicht

- Ein Kernpfad für CLI/Wrapper. Vorspann vor gen0/Freeze; echte Organaufrufe im Produktivpfad, keine immer-sperrende Stubfunktion. Nachweis nur bei vier ausgeführten/prüfbaren positiven und vier ausgeführten/prüfbaren negativen Kontrollen. Fehlversuch verbraucht die Lauf-ID.
- Hashbindung aller Biotop-Python-Dateien, Dockerfile und tatsächlicher Image-ID, Verfassung/Referenzlast/Werk, Rohdaten/Qualität/Rauschen. Nachweis und eingefrorenes Maß an hashverkettetes Protokoll gebunden. Nachkorrektur und Wieder-Eichen gesperrt.
- gen0/mass/generation verlangen den Nachweis; kein mass-Überschreiben/gen0 nach Freeze. Rauschwerte tatsächlich an Maßpfad weitergegeben; gesperrte Bereiche/Verhandlungsnachbarn übersprungen und belegt. Generalprobe vereinigt tatsächliche Wirkungskreise, Pareto prüft alle Bereiche.
- CLI-Verweigerung Exit 1; echte Fehler-Subprozesse zusätzlich netz-/kammergesperrt. Erfolgs-/Probe-Messwerte der Tests sind ausdrücklich kontrollierte Unit-Fixtures, keine echte Eichung.

## Belege

33 echte pytest-Aufrufe, je unverändertes stdout/stderr plus Aufruf-/Quellhash-Metadaten, zusammen 99 Rohdateien:
/root/reparatur-01/teil-vorspann/ausgaben/

Abschluss:
/root/reparatur-01/teil-vorspann/ausgaben/32-abschluss.stdout.txt
/root/reparatur-01/teil-vorspann/ausgaben/33-patch-anwendung.stdout.txt
/root/reparatur-01/teil-vorspann/TEST-ERGEBNIS.json
/root/reparatur-01/teil-vorspann/patch-anwendung.json
/root/reparatur-01/teil-vorspann/final-junit.xml
/root/reparatur-01/teil-vorspann/patch-junit.xml

Rot→Grün: 01→02, 03→04, 05→06, 07→08, 09/10→11, 12→13, 14→15, 17→18, 20→21, 22→23, 24→25, 26→27, 28→29, 30→31. 16/19 enthalten zusätzlich Testharnessfehler; deren korrigierte, berechtigte Rots sind 17/20. Nichts davon als echte Eichkampagne ausgegeben.

## Integrität / verbleibende Grenzen

116 anfänglich kopierte Quelldateien vor/nach SHA-geprüft. Original-Abweichungen in `.gitignore`, `messgeraet.py`, `eichung.py`, `tests/conftest.py` stammen aus parallel sichtbaren Elternänderungen; keine der sechs Lieferdateien im Original wurde durch diesen Teilagenten geschrieben. Kopie: sechs eigene Lieferdateien plus zwei unverändert übernommene Eltern-Abhängigkeiten. Die Eltern-Dateien sind nicht im Patch; die neue Eltern-Testreihenfolge wurde nicht importiert.

/root/reparatur-01/teil-vorspann/integritaet.json
/root/reparatur-01/teil-vorspann/original-before.json
/root/reparatur-01/teil-vorspann/original-after.json
/root/reparatur-01/teil-vorspann/copy-before.json
/root/reparatur-01/teil-vorspann/copy-after.json
/root/reparatur-01/teil-vorspann/parent-imports.json

Keine Änderung von Lauf24/25. Die gesonderte Gen0-≥80%-Qualitätsfrage bleibt unverändert; nur abgeschlossener gen0-Schritt wird vor Freeze verlangt. Aktuelle Eichproben-API gelesen (`pruefbar` sowie private Kostenrückgabe), aber die Agent1-Dateien nicht als unfertigen Stand importiert. Reale kombinierte vier-plus-vier Eichung und Elternreview stehen aus. Ist der feste Eichgegenstand selbst im gesperrten Wirkungskreis, wird seine Sperre nicht zur Grünherstellung umgangen.
