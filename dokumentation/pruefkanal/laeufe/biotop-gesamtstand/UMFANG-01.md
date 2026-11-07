# Umfang des gebauten Biotops — Messung 01

Stichtag des Dateibestands: 2026-09-20T04:43:06.119737+00:00. Quellstand `b42dc941e7fcb66632ba6a0e13b8df106a270a31`, Git-Arbeitsbaum sauber. Gezählt wird der Eigenbau, nicht das Gewicht seiner Git-Kopien, Werkarchive oder Python-Caches. Die Bestandsaufnahme selbst liegt außerhalb des Repositories.

## Eigenbau (vollständige, disjunkte Zerlegung)

| Gruppe | Dateien | physische Zeilen | Python-Dateien | Bytes |
|---|---:|---:|---:|---:|
| biotop | 35 | 6370 | 35 | 376721 |
| kammer | 1 | 4 | 0 | 152 |
| pruefung | 63 | 4446 | 54 | 293616 |
| verfassungen | 11 | 295 | 7 | 15921 |
| wurzel | 1 | 4 | 0 | 32 |
| **Summe** | **111** | **11119** | **96** | **686442** |

Zeilen = `splitlines()` einschließlich leerer Zeilen, Kommentare und letzter Zeile ohne Zeilenumbruch. Python-Schnitt separat: {'dateien': 96, 'physische_zeilen': 10881, 'codezeilen': 8517, 'dokumentationszeilen': 1336}. Codezeilen mittels Python-Tokenizer ohne reine Kommentare/Docstrings; keine Vermischung mit physischen Zeilen. `pygount` war nicht installiert; keine Installation am Wirt. Einzeldateien mit Hash in `ausgaben/03-dateien.json`, Symbole in `04-symbole.json`.

## Organe und eigene Tests

- **18 Organmodule** in `biotop/organe/` (ohne `__init__.py`). Die **15 Organabschnitte 3.1–3.15** des Masterprompts sind eine andere Gliederung: Maß/Kasse liegen im Kern, Nexus in `lauf.py`, Oberfläche außerhalb `organe/`; Eichung und Gedächtnisse haben zusätzliche/geteilte Module. Nicht 18 vollständig erfüllte Soll-Organe behaupten.
- **0 pytest-Testfälle gesammelt** in den beiden Eigenprogramm-Verzeichnissen `biotop/` und `pruefung/`; Exit 5, `no tests collected`. Beleg: `16-eigene-tests-sammlung-02.json`. Das ist kein grüner Testlauf, sondern das gemessene Fehlen einer nach pytest-Konvention auffindbaren Eigen-Testsuite.
- `pruefung/`: **54 Python-Skripte in 63 Dateien**, darunter historische Laufsteuerungen, Auswertungen und gestellte Mechanikproben. **5 echte AST-assert-Anweisungen** in drei Skripten; das ist weder eine Fallzahl noch eine Erfolgsquote. Viele Prüfungen vergleichen/manipulieren Werte oder drucken Erwartungen ohne assert. Tests als erzeugter Quelltext in Strings werden von dieser AST-Zählung bewusst nicht als ausgeführte Tests gezählt.
- **31 test_-Funktionen mit 52 assert-Anweisungen in 7 Vertragsdateien** unter `verfassungen/`; sie testen die zwei Übungswerke, nicht das Biotop. Nicht zu eigenen Biotop-Regressionstests umetikettiert.
- Bestehendes Skript `rauschregeln_pruefen.py` neu ausgeführt: **7 von 7 eingetragenen Beispielen ausgegeben**, Exit 0. Das Skript enthält keine assert-Prüfung; deshalb keine Behauptung „7 Tests bestanden“. Rohwerte, Resultate und Solltexte liegen in `17-rauschbeispiele-ausfuehrung-02.json`.
- Die erste Testsammlung und erste Beispielausführung scheiterten an einem Mount unter `/root` für den unprivilegierten Kammernutzer (Exit 4 bzw. 2). Wiederholung unter `/quelle` behob den Aufbaufehler. Beide Fehlversuche bleiben beigefügt; keine Biotop-Quelldatei wurde dafür geändert.

## Gesamter lokaler Verzeichnisbestand

| Disjunkte Kategorie | Dateien | Bytes |
|---|---:|---:|
| Git-Interna (einschließlich Werk-Git) | 2270 | 2250692 |
| Git-verfolgter Eigenbau | 111 | 686442 |
| Python-/Pytest-Caches | 33 | 483000 |
| Biotop-Datenbank mit WAL/SHM | 3 | 29691904 |
| Lazarus-Archive | 70 | 878541 |
| Werkdateien (ohne Git/Caches) | 729 | 954396 |
| **Summe** | **3216** | **34944975** |

Bezugsgröße: alle regulären Dateien unter `/root/biotop`, ohne Symlinks; 0 Lesefehler. Git-intern enthält ausdrücklich auch die Git-Verzeichnisse der kopierten Werke. Die Werkdateien sind Kopien/Generationen und kein zusätzlicher Biotop-Quellcode. Keine Addition von komprimiertem Archiv und entpacktem Inhalt zum Eigenbau.

## Datenbank

- Hauptdatei: **29659136 Bytes** = 28,285 MiB. WAL 0 Bytes, SHM 32768 Bytes; zusammen 29691904 Bytes. Logische Dateilänge nicht mit belegten Blöcken verwechseln.
- **27 Tabellen**, `integrity_check = ok`; 7241 Seiten zu 4096 Bytes, davon 4 freie Seiten.
- Fachbestand: 22 Werkeinträge (Kopien zweier Übungswerkfamilien, nicht so viele unabhängige Werkarten), 25 Läufe, 144 Generationseinträge inklusive Ausgangs-/Proben-/Abbruchzuständen, 2679 Kandidateneinträge einschließlich Proben.
- 4070 Kassenbuchungen; 16030 Protokollzeilen. Die originale Funktion `protokoll.pruefen` bestätigt die Hashkette für **16030 von 16030 Zeilen**; dies ist Manipulationserkennung, keine technische Unveränderlichkeit.
- Vollständige Tabellen-Zerlegung: `02-datenbank.json`. Keine öffentliche SQLite-Komplettkopie: Benutzer-/Token-Tabellen enthalten schutzbedürftige Anmeldedaten. Fachliche Rohdaten und gezielte Abfragen sind beigelegt. In der veröffentlichten Protokollkopie sind Anmeldeinhalte entfernt; ihre gesamte Hashkette ist deshalb nicht aus dieser bereinigten Kopie neu berechenbar. Die oben genannte Prüfung lief gegen die unveränderte private Sicherung.
