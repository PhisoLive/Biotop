# Lieferung EICH-4 — gültige Vertragszeugen

## Ergebnis und Umfang

**EICH-4 behoben und mit echten Kammerläufen geprüft.** Der konkrete benannte Vertrag scheitert positiv an der fehlenden Zusicherung im Verbraucher und besteht negativ nach der Lieferantenanpassung. Eine defekte, nicht eingesammelte oder fehlende Vertragsprobe ist nicht mehr durch eine gültige Messhülle als gültige Gegenprobe ausweisbar.

Genau diese Repositorydateien wurden geändert:

- `biotop/organe/eichproben.py`
- `tests/test_eichproben.py`
- neu: `tests/test_review_vertrag.py`

Vollständige Dateien: `dateien/`; ursprüngliche geänderte Dateien: `basis/`; vollständiger Patch: `AENDERUNGEN.diff`. Der Patch wurde an einer weiteren privaten Ausgangskopie mit `git apply --check` und anschließendem tatsächlichem Anwenden geprüft. Die angewandten Dateien sind bytegleich mit der getesteten Quelle. Kein Git-Repository war vorhanden; der Diff wurde deshalb deterministisch aus der gesicherten Ausgangskopie erstellt.

**Nicht geändert oder integriert:** `aegis.py`, `kammer.py`, `vorspann.py`, `lauf.py`, Kernmaß/Pareto, die anderen Probenmechaniken und deren bestehenden Testnamen. Keine Änderungen anderer Fixagenten, keine Integration ins Elternrepository. Die ausdrücklich auf Phase 4 verschobenen Themen wurden nicht bearbeitet. Pflichtvorspann/CLI und deren Freigaberoute bleiben Aufgabe der abschließenden Elternabnahme; diese Teillieferung behauptet dafür keine neue Ausführung.

## Reparatur

1. Der AST wählt weiterhin denselben vorhandenen eigenständig aufrufbaren Verbrauchertest. Statt nur Imports und Funktionsrumpf zu transplantieren, lädt der benannte Vertrag das vorhandene Testmodul mit `runpy.run_path` in einen eigenen Namensraum und ruft den ausgewählten Test auf. Modulkonstanten, Hilfsdefinitionen und Future-Imports bleiben erhalten; sie überschreiben keine Namen des ursprünglichen Vertragsmoduls. Ausgeführt wird ausschließlich innerhalb der originalen Kammer.
2. `_vertrag_vorbereiten` führt über **`aegis.junit_lauf`** sowohl den Verbraucher als auch die benannte Vertragsdatei direkt am Ausgang und am Kandidaten aus. Die Original-JUnit-Ergebnisse liegen in `basis_tests` und `kandidat_tests`; der Vertragsname ist derselbe wie im Originalurteil von Aegis.
3. `_vertrag_pruefbar` verlangt die konkreten vollständigen Zeugen. Positiv müssen Verbraucher und benannter Vertrag bestätigte Fehler am Verbraucherort mit der eingesetzten Zusicherung zeigen. Negativ müssen beide wirklich als bestanden vorliegen. Fehlende Pflichtfelder, fremder Fehlerort, Fixturefehler und fehlende Zieltests sperren die Prüfbarkeit. `_bestanden("vertrag", ...)` verwendet diese Zeugen zusätzlich zu den unveränderten Aegis-/Maßbedingungen; positiv und negativ durchlaufen weiterhin **dasselbe Bestehensprädikat**.
4. Ein Syntaxfehler im auszuwählenden Verbrauchertest wird ausdrücklich als nicht baubare Probe gemeldet. Der vorhandene Batterie-Fehlerpfad kann ihn damit als `pruefbar=false` abbilden, statt durch eine nicht behandelte AST-Ausnahme abzubrechen.

Kein Ersatz-JUnit-Parser, keine nachgebaute Aegis-Klassifikation, kein Ersatz-Pareto. Nicht unterstützte Fixturekontexte werden nicht „repariert“ oder als Gegenbeweis ausgegeben: Ohne gültige reale Zeugen bleiben sie unprüfbar.

## Echte Rot-/Grün-Belege

Alle Angaben sind aus den ausgeführten pytest-JUnit-Dateien und `kammer.zaehlung` übernommen. Rohes stdout, stderr, Rückgabecode, Befehle, Quellhash und jeder Kammer-Rohbeleg bleiben erhalten.

| Versuch | Ergebnis | Kammerläufe | Aussage |
|---|---:|---:|---|
| `01-konstante-rot` | 1 fehlgeschlagen, rc=1 | 6 | Beide geklonten Verträge fallen mit `NameError: EINGABE`; die Gegenprobe besteht den Vertrag nicht. |
| `02-konstante-gruen` | 1 bestanden, rc=0 | 6 | Derselbe Test: konkreter Vertragsbruch im Werk positiv, konkreter Vertrag bestanden negativ. |
| `03-pruefbar-rot` | 1 fehlgeschlagen, rc=1 | 9 | Gültige Messhülle kaschiert einen echten Setupfehler nur des Vertrags; altes `pruefbar=true`. |
| `04-pruefbar-gruen` | 4 bestanden, rc=0 | 25 | Defekter Vertrag unprüfbar; normales Vertragspaar weiterhin gültig. |
| `05-vertrag-abnahme` | 9 bestanden, rc=0 | 70 | Konstanten/Helfer/Namensräume, Fehler-/Fehlzeugenfälle und Vertragspaar am Bestandswerk. |
| `06-syntax-rot` | 1 fehlgeschlagen, rc=1 | 0 | Nicht behandelter Syntaxfehler im Testklon-Eingang. |
| `07-syntax-gruen` | 1 bestanden, rc=0 | 0 | Explizit unbaubar; kein vermeintlich ausgeführter Mechaniktest. |
| `08-regression-gruen` | **44 bestanden, rc=0** | **243** | Kernmaß/Pareto zuerst, gesamte `test_eichproben.py`, gesamte `test_review_vertrag.py`; keine ausgelassenen Fälle. |
| `09-zeugenmutant-rot` | 3 fehlgeschlagen, rc=1 | 19 | Wegwerfquellkopie mit absichtlich ausgeschalteter Zeugenvalidierung: Charakterisierungstests treffen die fehlenden Zeugen/Pflichtfelder. |
| `10-zeugenmutant-gegenkontrolle-gruen` | 3 bestanden, rc=0 | 19 | Dieselben Tests an unveränderter echter Reparaturquelle wieder grün. |

Die Zusatzfälle nach dem jeweiligen Fix sind als Charakterisierungen ausgewiesen, nicht als vorgelagerte TDD-Rotfälle. Der absichtliche Mutant liegt nur im privaten Teilordner und gehört nicht zum Patch. Die Entwicklungs-Rotläufe und der Mutant sind erwartete Testfehlschläge, keine bestandenen negativen Mechanikkontrollen. Alle stderr-Dateien der äußeren pytest-Läufe wurden geprüft und sind leer; die absichtlich erzeugten inneren Test-/Sammelfehler stehen unverändert in den Kammer-Rohbelegen.

## Vier echte Paare am kopierten Bestandswerk

Quelle: `ausgaben/08-vierpaare-bestand.json`. Werk-ID **22**, privater neuer Testlauf; der natürliche Lauf 25 wurde weder fortgesetzt noch neu gestartet.

Versiegelter Gegenstand: `bericht → lager`, `tests/vertraege/test_vertrag_bericht_lager.py`.

Vertragssumme: `b69270558c12328906acf851cc12a66f617c0fc27b4818d52432671538a4bc6c`.

| Probe | Positiv: prüfbar / Prädikat | Gegenprobe: prüfbar / Prädikat | Kammerläufe positiv / negativ |
|---|---|---|---|
| nebenwirkung | true / true | true / false | 2 / 2 |
| regression | true / true | true / false | 7 / 7 |
| norm | true / true | true / false | 8 / 4 |
| vertrag | true / true | true / false | 4 / 4 |

Damit sind alle vier Positivproben und alle vier ausgeführten, prüfbaren falschen Gegenprädikate durch die vorhandene Batterie bestätigt. Die Normprobe und die anderen Paare wurden weder umbenannt noch gelockert.

**Spezifischer Vertragszeuge in beiden Fällen:**

`tests/vertraege/test_vertrag_bericht_lager.py::test_eichprobe_vertrag_neue_zusicherung`

- Positiv: `ok=false`, `bestaetigt=true`, `AttributeError: module 'lagerhaus.lager' has no attribute 'eichprobe_zusicherung'`, Ort `lagerhaus/bericht/auswertung.py`. Der gesonderte Verbraucher `tests/test_bericht.py::test_lagerwert_leer` zeigt denselben bestätigten Werkfehler; sein Ausgang besteht. Aegis nennt exakt diesen Vertrag in `vertrag_verletzt` und im Schritt-2-Grund.
- Gegenprobe: derselbe Vertrag und derselbe Verbraucher haben `ok=true`, leere Fehlermeldung; `vertrag_verletzt=[]`. Das unveränderte Gesamt-Bestehensprädikat ist false. Das Originalurteil darf dabei wegen fehlenden Kernmaßgewinns ablehnen — entscheidend ist der belegte verschwundene Vertragsbruch, nicht eine globale Annahme.

Die weiteren absichtlich ungültigen Setup-, Aufruf-, Sammel- und fehlenden Zieltestfälle werden ausdrücklich **nicht** zu diesen vier gültigen Gegenproben gezählt.

## Zählung, Kosten und Isolation

- Gesamter dokumentierter Entwicklungs-/Prüfumfang: **397 Kammerläufe**, einschließlich Rotläufen, Wiederholungen und Mutant. Davon **206 JUnit-Zeugenläufe**, **191 übrige Kammerläufe**. Das sind nicht 397 Batterien und nicht 397 pytest-Fälle.
- Letzter breiter Eigentestlauf `08`: **243 Kammerläufe**.
- Darin enthaltene vollständige Bestandsbatterie: **38 Kammerläufe**, davon **22 JUnit-Zeugenläufe** und **16 übrige Kammerläufe**. Diese Teilmenge wird nicht nochmals zum Gesamtverbrauch addiert.
- Vertrags-Zielpaar innerhalb dieser Batterie: die obigen **4 + 4** Kammerläufe; je Seite sind die direkten Ausgangs-/Kandidatenzeugen und die Originalmessungen enthalten.
- **0 bezahlte Biotop-Aufrufe, 0 EUR Biotop-Modellkosten**, keine Modellversuche. Keine Aussage über externe Infrastrukturkosten. Hartes Auftragsbudget nicht belastet.

Gezählt wurde ausschließlich am originalen `kammer.zaehlung`; alle äußeren Containerkennungen über sämtliche Versuche sind eindeutig. Die Zuordnung „JUnit-Zeugenlauf“ bezeichnet reale `_messgeraet/lauf.py`-Aufrufe einschließlich der originalen inneren Aegis-Zeugen, nicht eine geschätzte Zahl aus Probenbezeichnungen.

Verwendet wurden `/root/reparatur-01/venv/bin/python` und das vorhandene Image `biotop-kammer:1` mit ID `sha256:ce7bbe9441182aea532f147defd99ca757a95d4cb3ff7c3f5c5d9a64965643ee`; Image vorher/nachher identisch, kein Build. Docker-Kammern weiterhin ohne Netz. Der Host-Guard sperrt Netz und Modellaufrufe, fremde Datenbanken und Writes außerhalb dieses Teilordners; Docker-Mounts müssen unter dessen TMPDIR liegen. `PYTHONPATH`, importiertes `eichproben.__file__`, DB-Pfad, CWD und TMPDIR werden vor jedem Lauf hart geprüft und im Rohbeleg ausgegeben.

Eigene Ausgangsquellen:

- Werkquelle nur gelesen: `/root/reparatur-01/teil-eichung/werk-lauf25-kopie`
- Eigene Werk-Kopie: `/root/reparatur-01/nachbesserung-01/vertrag/werk-lauf25-kopie`
- DB-Quelle nur per SQLite-Backup aus `mode=ro`: `/root/reparatur-01/ausgang.db`
- Eigene DB und zusätzliche Sicherung: `/root/reparatur-01/nachbesserung-01/vertrag/privat.db`, `/root/reparatur-01/nachbesserung-01/vertrag/privat-sicherung.db`

**Quellschutz:** Das Vorher-/Nachher-Inventar umfasst 3272 Dateien unter `/root/biotop/`, der Werkquelle und der DB-Quelle. Alle Dateibytes und Größen sind unverändert. Die beiden privaten DB-Dateien sind ebenfalls bytegleich. Ein Metadatenbefund bleibt offen: Nur die mtime von `/root/biotop/daten/biotop.db-shm` änderte sich; ihr SHA256 und ihre Größe blieben gleich. Der Verursacher wurde nicht bestimmt. Deshalb wird ausdrücklich keine vollständige Metadaten-Unverändertheit behauptet. Der Prüfguard erlaubt keinerlei Verbindung zur produktiven DB. Beide Inventare und die exakten Vorher-/Nachher-Werte sind in der Lieferung enthalten.

## Wiederholung der gezielten Abnahme

Aus dem eigenen Repository, nicht aus einem produktiven Werk:

```sh
cd /root/reparatur-01/nachbesserung-01/vertrag/repo
PYTHONPATH=/root/reparatur-01/nachbesserung-01/vertrag/guard:/root/reparatur-01/nachbesserung-01/vertrag/repo \
TMPDIR=/root/reparatur-01/nachbesserung-01/vertrag/tmp \
BIOTOP_DB=/root/reparatur-01/nachbesserung-01/vertrag/privat.db \
BIOTOP_EICHWERK=/root/reparatur-01/nachbesserung-01/vertrag/werk-lauf25-kopie \
BIOTOP_EICHDB=/root/reparatur-01/nachbesserung-01/vertrag/privat.db \
BIOTOP_EICHWERK_ID=22 \
BIOTOP_EICHBELEG=/root/reparatur-01/nachbesserung-01/vertrag/ausgaben/WIEDERHOLUNG-batterie.json \
PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
/root/reparatur-01/venv/bin/python \
/root/reparatur-01/nachbesserung-01/vertrag/werkzeuge/pytest_belegen.py \
WIEDERHOLUNG tests/test_kernmass_pareto.py tests/test_eichproben.py tests/test_review_vertrag.py
```

Neuen Belegnamen verwenden; versiegelte Nachweise nicht überschreiben. Das ist die gezielte Eigentestmenge, nicht eine unkontrollierte gesamte Repository-Suite mit historischen Produktivpfaden.

## Vollständige Ablage

/root/reparatur-01/nachbesserung-01/vertrag/lieferung/LIEFERUNG.md

/root/reparatur-01/nachbesserung-01/vertrag/lieferung/AENDERUNGEN.diff

/root/reparatur-01/nachbesserung-01/vertrag/lieferung/BELEGE.json

/root/reparatur-01/nachbesserung-01/vertrag/lieferung/KOSTEN.csv

/root/reparatur-01/nachbesserung-01/vertrag/lieferung/DATEIEN.json

/root/reparatur-01/nachbesserung-01/vertrag/lieferung/PRUEFSUMMEN.sha256

/root/reparatur-01/nachbesserung-01/vertrag/lieferung/ausgaben/08-regression-gruen.xml

/root/reparatur-01/nachbesserung-01/vertrag/lieferung/ausgaben/08-vierpaare-bestand.json

/root/reparatur-01/nachbesserung-01/vertrag/EICH-4-fixpaket.tar.gz

/root/reparatur-01/nachbesserung-01/vertrag/EICH-4-fixpaket.tar.gz.sha256

Die vollständigen Rohbelege aller Versuche liegen unter `lieferung/ausgaben/`; `DATEIEN.json` nennt jeden Bestandteil mit vollständigem Pfad und Hash. Die allgemeine Verfahrensregel für isolierte Testmodulkontexte wurde ergänzend im bereits geladenen Agent-Skill `measurement-harness-discipline/references/self-check-battery.md` festgehalten; das ist keine Repositoryänderung und gehört nicht zum Patch.
