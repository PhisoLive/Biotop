# Kernlieferung – zweite und letzte automatische Runde

**Die beiden gelieferten Kernleser sind korrigiert und lokal geprüft. Die Außensuche wurde nach der Scope-Reduktion abgebrochen; dies ist keine Entwarnung für Gen0, Aufnahme, Legacy-Skripte oder das Gesamtbiotop.**

## Nur diese Dateien integrieren

- `dateien/biotop/organe/fundpruefung.py`
- `dateien/biotop/lauf.py` – ausschließlich Ergebnisleser in `_verhandeln`, kein Wirkungskreis-/Transitivitätsumbau.
- `dateien/tests/test_nachweis_verbraucher.py`

Der gemeinsame Patch ist **`KERN.diff`**. `quarantaene/` darf **nicht** integriert werden. `SCOPEPRUEFUNG.json` vergleicht sämtliche Dateien mit dem Ausgang: nur diese drei Dateien geändert; `lauf.py` außerhalb `_verhandeln` AST-identisch; Gen0 vollständig auf Ausgang zurückgesetzt; Aufnahme und Legacy unverändert. Keine Commits und keine Integration in den Parent-Stand.

## Erreicht

**Fund-Neubewertung / Pflichtvorspann.** Ein nicht ausgeführter, übersprungener, leerer, unvollständiger oder abgebrochener Fundlauf bricht laut ab, statt ein boolesches Inhaltsurteil zu erzeugen. Der Kammer-Wrapper transportiert den inneren pytest-Status; JUnit und alle benannten Testfunktionen müssen vorhanden sein. Der unveränderte Vorspann fängt die Ausnahme, schreibt `gescheitert`, erzeugt keinen Freigabenachweis und erreicht die Proben nicht. Ausgeführte Assertion-/Produktfehler bleiben klassifizierbar. Ein tatsächlich abgefragter leerer Fundbestand bleibt dagegen legitim.

**Verhandlung / Kernmaß-Pareto.** Fehlendes oder unvollständiges `u2.mass` sowie fehlende Vertrags-/Pareto-/Grenzergebnisse ergeben kein `verhandlung_bestanden`. Ein vollständiges Ergebnis ohne Kernmaßgewinn bleibt als bestandene Vertragsanpassung möglich: `mass.ok=False` wird nicht pauschal zum Verhandlungsverbot.

Die Fund-Gutkontrollen und ungültigen realen Werkfixtures laufen ausschließlich in der Docker-Kammer. Verhandlungsprüfungen verwenden den echten Kernmaßentscheid auf ausdrücklich gestellten Messwerten mit gekennzeichnetem Aegis-/Hersteller-I/O. Der Vorspann-Gatetest führt die Fundprüfung real aus, ersetzt aber übrige Eichstufen ausdrücklich durch Unit-Doubles; er ist **keine** echte Gesamteichung.

## Rohbelege und TDD

Alle Angaben sind aus `LAEUFE.json` und den jeweiligen JUnit-Dateien berechnet. „Rot“ bezeichnet erwartete Regressionsfehlschläge der Eigensuite, nicht übersprungene Eigentests.

| Belegordner unter `belege/` | Bestanden | Fehlgeschlagen | Echte Kammeraufrufe | Einordnung |
|---|---:|---:|---:|---|
| `01-fund-rot` | 3 | 12 | 4 | Vor Fund-Produktänderung |
| `02-fund-gruen` | 15 | 0 | 4 | Nach Fund-Produktänderung |
| `03-gen0-fang-rot` | 1 | 13 | 6 | Außenfall, vor Teilfix |
| `04-gen0-fang-gruen` | 14 | 0 | 6 | Teilfix anschließend quarantänisiert, **nicht erledigt** |
| `05-verhandlung-rot` | 4 | 15 | 0 | Vor Verhandlungs-Produktänderung |
| `06-verhandlung-gruen` | 19 | 0 | 0 | Nach Verhandlungs-Produktänderung |
| `07-pflichtvorspann-kernbezug` | 1 | 2 | 2 | Harnessfehler: Unit-Quellbindung enthielt `bereiche` nicht |
| `08-pflichtvorspann-kernbezug` | 3 | 0 | 2 | Nur Fixture korrigiert, kein weiterer Produktfix |
| `09-kern-eigensuite` | 43 | 0 | 12 | Gesamte neue Kern-Eigensuite |
| `10-kern-ruecklauf` | 123 | 0 | 12 | Neue Suite + bestehende Kernmaß-/Pareto-/Vorspann-/Reihenfolgetests |
| `11-kern-abschluss` | 123 | 0 | 12 | Gleicher Rücklauf, zusätzlich globale Kammerzählung |

Im Abschlusslauf: **123 ausgeführte Eigentests bestanden, keine Fehler und keine übersprungenen Eigentests**; darin die **43 neuen Fälle**. Der globale Kammerzähler erfasst **12 tatsächliche Aufrufe** und stimmt mit der fallbezogenen Erfassung überein. Über alle dokumentierten Versuche: **60 tatsächliche Kammeraufrufe**, davon **48 Kernarbeit** und **12 quarantänisierte Gen0-Arbeit**. Wiederholungen und Harnessfehler sind enthalten, I/O-Doubles nicht. **47** aus tatsächlich aufgezeichneten Kammerausgaben extrahierte JUnit-Rohdateien liegen jeweils in `kammer-junit/`; bei Läufen ohne erzeugtes JUnit wurde keines erfunden.

Jeder Versuch enthält `aufruf.json` mit exaktem Befehl/Arbeitsverzeichnis/Umgebung/Rückgabecode, `stdout.txt`, `stderr.txt`, `junit.xml` und fallbezogene `kammer.jsonl`. `11-kern-abschluss/gesamt-kammer.json` erfasst zusätzlich den gesamten pytest-Prozess. Der Ursprungstest ohne JUnit bleibt mit seinem echten stdout erhalten.

## Grenzen und offene Befunde

- `BEFUNDE.json` trennt reparierte Kernleser, ausgeführt bestätigte Außenfälle und nur am Quelltext bestätigte offene Stellen. Gen0-Fang wurde vor der Scope-Reduktion reproduziert; der Teilfix samt damaliger Testsuite bleibt unter `quarantaene/gen0-nichtintegrierbar/` gesichert. Gen0-Äquivalenz/Testbau, Aufnahme und Legacy wurden nicht weiter repariert oder an Produktion ausgeführt.
- `_verhandeln` mit `all(ids)` über leere Herstellerantworten bleibt gemäß letzter Steuerung **offen**. P4-Wirkungskreis/Transitivität, Vertragsaustausch, Collector- und Maß-Freeze-Themen wurden nicht bearbeitet.
- Keine zusätzliche Aegis-Schnittstelle angenommen. Die Parent-Schnittstelle wurde gezielt gelesen; Aegis und Messgerät wurden weder geändert noch in diese Lieferung kopiert. Die bestehende `_nennt_vertrag`-Schnittstelle bleibt unverändert.
- Keine Änderung am Vorspann zur Invaliditätsfortleitung notwendig. Seine bestehende nachgelagerte Fund-Kostenbuchung wird bei Exception nicht erreicht; die unabhängige tatsächliche Kammerzählung dieser Lieferung enthält solche Aufrufe dennoch. Keine Kostenbuchungsreparatur behauptet.
- Der vorliegende Checkout besitzt kein `.git`; Diff und Scopeprüfung beruhen deshalb auf gesicherten Ausgangsdateien und SHA-256, nicht auf erfundener Git-Historie.
- Kein Netz-/Modellbetrieb; keine produktive Datenbank oder produktiven Werke verwendet. `TMPDIR` liegt außerhalb der Eigenwerke, `PYTHONDONTWRITEBYTECODE=1`, eigenes `PYTHONPATH`. Aufnahme-WERKE wird in den Fixtures vor Laufaufrufen auf einen privaten Pfad gesetzt.
- Integrierte Vollsuite, gemeinsame vier Eichproben und echte `-1`-CLI bleiben beim Parent. Der lokale Rücklauf ersetzt diese Integrationsprüfung nicht; nach dieser zweiten/letzten Runde liegt die Entscheidung bei Philipp.

## Ablage

Gesamte Lieferung: `/root/reparatur-01/nachbesserung-02/verbraucher/lieferung/`

Kernpatch: `/root/reparatur-01/nachbesserung-02/verbraucher/lieferung/KERN.diff`

Dateimanifest: `/root/reparatur-01/nachbesserung-02/verbraucher/lieferung/DATEIEN.txt`

SHA-Manifest: `/root/reparatur-01/nachbesserung-02/verbraucher/lieferung/SHA256SUMS`

Befunde: `/root/reparatur-01/nachbesserung-02/verbraucher/lieferung/BEFUNDE.json`

Kammerzählung: `/root/reparatur-01/nachbesserung-02/verbraucher/lieferung/KAMMERZAEHLUNG.json`
