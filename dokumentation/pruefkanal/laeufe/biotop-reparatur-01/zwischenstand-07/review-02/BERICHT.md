# Kernabschlussreview — nicht freigegeben

**`passed=false`: ein belegter Kernfehler, keine Sicherheitsbefunde.** Die vier ausdrücklich zurückgestellten Lücken sind nicht Ursache dieser Entscheidung und bleiben unverändert offen.

## Blocker KERN-EICH4-SKIP (P1)

Ein **übersprungener benannter Vertragszeuge** wird als ausgeführte, bestandene Gegenkontrolle anerkannt:

1. Eigenes lokales pytest-Fixture: Verbraucher und alter Vertrag bestehen; `test_eichprobe_vertrag_neue_zusicherung` wird vor seinem Rumpf übersprungen.
2. Echtes JUnit enthält `<skipped …>`. Der unveränderte Parser in `biotop/organe/aegis.py:89–95` macht daraus `ok=true, bestaetigt=false, meldung=""`.
3. `biotop/organe/eichproben.py:230–245` akzeptiert das als tatsächlich bestandenen benannten Vertrag. Das direkte Soll-Assertion schlägt fehl.
4. Original-`_einzelprobe` liefert an einer **expliziten Maß-Unit-Grenze** ebenfalls `ausgefuehrt=true, pruefbar=true, bestanden=false` (`:464–471`). Ein gekennzeichneter Verbraucher-Replay aus dieser Zeile und sieben gespeicherten Elternzeilen passiert `_vollstaendig` und `_qualitaet` mit 4/4.

**Beweisgrenze:** Der minimale Fehlernachweis braucht keine Maß-Doubles: Originalbauer → reales lokales pytest → Originalparser → Originalgültigkeitsprädikat. Die zusätzliche Fortleitung benutzt gestellte Maßwerte und einen zusammengesetzten Verbraucher-Replay, **keine frisch ausgeführte Docker-Gesamtbatterie**. Die kaputte Fixture zählt hier als Fehlernachweis, nicht als erfolgreiche Negativkontrolle. Generiertes `runpy.run_path` wurde auf dem Host ausdrücklich gesperrt und nicht ausgeführt.

### Exakter Repro

```sh
PYTHONPATH=/root/reparatur-01/review-02/pruefer-kern/guard:/root/reparatur-01/review-02/pruefer-kern/arbeitskopie \
PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
TMPDIR=/root/reparatur-01/review-02/pruefer-kern/tmp \
BIOTOP_DB=/root/reparatur-01/review-02/pruefer-kern/tmp/unused.db \
/root/reparatur-01/venv/bin/python /root/reparatur-01/review-02/pruefer-kern/repro_skip_vertragszeuge.py
```

Ist: Exit 1, `AssertionError: Skipped named contract is incorrectly accepted as executed/passing negative control`. Neue Ausführung legt einen neuen `repro-skip-N`-Ordner an; vorhandene Rohdaten bleiben erhalten. Entscheidende Belege:

- `repro-skip/result.json`, `repro-skip/call-2/junit.xml`: minimaler direkter Nachweis.
- `repro-skip-2/result.json`, `repro-skip-2/call-4/junit.xml`: Wiederholung und Originalproduzent an markierter Messgrenze.
- `skip-repro-expanded.execution.json`, `.stdout.txt`, `.stderr.txt`: vollständiger Aufruf und Ausgaben.

Abhilfe: Ausführung/Skipstatus aus JUnit erhalten; ein übersprungener Pflichtzeuge ist nicht bestanden. Skip/xfail neben setup/aufruf/sammlung/fehlend bis zum Gültigkeitsverbraucher testen. Keine Schwelle ändern.

## Positiv verifiziert — getrennt vom Blocker

| Prüfpunkt | Nachgerechneter / ausgeführter Befund | Beleg |
|---|---|---|
| Eltern-Gesamtsuite 48 | 188 ausgeführte Tests; 0 Fehler, 0 Fehlschläge, 0 Skips; 243 Rohkammern mit eindeutigen Containerkennungen | `belegabgleich.json`, `elternbelege/48-*` |
| Reale vier Paare 48 | 4 gültige positive True-Prädikate und 4 gültige False-Gegenprädikate; 38 Kammern, 0 Modellaufrufe | `belegabgleich.json` |
| Benannter Vertrag in diesen konkreten Paaren | Positiv benannter Bruch im Verbraucher, negativ benannter Vertrag und Verbraucher tatsächlich bestanden; kein Skip des Pflichtzeugen im Roh-JUnit | `belegabgleich.json` |
| Kernmaß/Pareto-Eigentests | 15 auffindbare Fälle vor nachrangigen Tests; Originalausführung grün | `core-unit.xml`, Eltern-Reihenfolge im Abgleich |
| Unabhängige Empfindlichkeit | Falsche Belohnung grüner Tests: 3/15 rot; entfernte Einzelregression: 1/15 rot | `sensitivity-*.xml`, Rohstdout |
| Abgegrenzte eigene Tests | 37/37 grün | `core-unit.xml` |
| Gen0-Freigaberoute, kontrolliert | 2/2 grün: ungültige Batterie stoppt vor Gen0-Rumpf; gültige Batterie erreicht den Originaleingang | `gen0-route.xml`, `gen0-route-*.json` |
| Reale private -1-CLI 49 | Exit 0; 83 Kammern; gespeicherter Nachweis, stdout und Nachweishash stimmen überein; Gen0-Nachweis als verwendbar belegt | `cli-belegabgleich.json`, `elternbelege/49-*` |
| Reale fehlende-Nachweis-Sperren 50 | gen0/mass/generation jeweils Exit 1 vor Kammeraufruf: 3/3 verweigert | `cli-belegabgleich.json`, `elternbelege/50-*` |

Die 36 Pythonquellsummen aus Suite 48 und die 37 Instrumentquellsummen einschließlich Dockerfile aus CLI 49 stimmen mit dem geprüften Snapshot überein. Aufzeichnungen wurden anhand Containerkennungen verbunden, nicht nach Reihenfolge geraten. Keine Implementiererlieferung wurde als Beweis benutzt.

Der alte EICH-4-Konstantenverlust ist durch den Modulkontextaufruf statt fragmentarischem AST-Klon adressiert (`eichproben.py:386–420`). Die zugehörigen echten Eltern-Kammertests für Konstante/Helfer/Namensraum bestehen. Der jetzige Blocker betrifft die weiterhin falsche **Ausführungsvalidität** eines übersprungenen Zeugen; er erklärt nicht die vorhandenen grünen Paare nachträglich für ungültig.

Gen0 selbst wurde im Elternbeleg 49 nicht ausgeführt; der Nachweis für seinen Eingang wurde verwendet. Der zusätzlich ausgeführte Reviewer-Gen0-Pfad ist ausdrücklich ein Gate-Unit-Test mit kontrollierter Eichung und Mutantenmessung. **Keine Aussage zur zurückgestellten Gen0-Erfolgswertbindung beim späteren Freeze.**

## Unverändert offen und außerhalb dieser Abnahme

- P4-01 / EICH-1, MASS-01: Wirkungskreis mit transitiven Folgen.
- P4-02 / EICH-3: Vertragsaustausch zwischen Vorspann und Freeze.
- P4-03 / MASS-02: NaN/Null-Collector.
- P4-04 / EICH-2: Gen0-Erfolgs-/Vorstufenbindung beim Maß-Freeze.

Keine neuen Repros dieser Mechanismen, kein Umdeuten auf grün und keine technische Entwarnung aufgrund der Werkgröße. Maßgeblich ist der wörtliche Auftraggeberentscheid samt `AUFTRAGSGRENZE.md`; genaue Fundstellen stehen in `REVIEW.json`.

## Integrität, Kosten und Grenzen

- Geprüftes Repo: `/root/reparatur-01/review-02/repo`.
- 126 Dateien / 137 Einträge einschließlich Verzeichnissen: SHA-256, mtime_ns, Größe, Typ und Pfadbestand vor/nach identisch (`quellzustand-vergleich.json`).
- Nur Reviewer-Arbeitskopie und eigene Ergebnis-/Tempordner beschrieben; keine Integration, keine Produktionsdatenbank oder produktiven Werke gelesen/geschrieben.
- Reviewer: **0 Dockeraufrufe, 0 bezahlte Modellaufrufe**; Netz und externe DB-Ziele in den Prüfläufen gesperrt.
- `STATIK.json`-Treffer `token`: ContextVar-Rücksetztoken (`kammer.py:96–107`), kein Secret.
- Zwei Sensitivitätsmutationen waren nur prozesslokal; geprüfte Quelle und Schwellen unverändert.
- Ein anfänglicher Shell-Quotingfehler beim Snapshot-Einzeiler verursachte SyntaxError vor Ausführung; anschließend wurde der erfolgreiche Snapshotlauf als Skript ausgeführt. Kein Produktbefund daraus.

## Lieferung

Ergebnisordner: `/root/reparatur-01/review-02/pruefer-kern/`

- `REVIEW.json`: maschinenlesbare fail-closed Entscheidung, genaue Stellen und Repros.
- `BERICHT.md`: dieser Kurzbericht.
- `DATEIEN.txt`: vollständiger Artefaktindex ohne flüchtige Arbeits-/Tempkopien.
- `SHA256SUMS`: SHA-256 aller indexierten Artefakte.
- `MANIFEST.sha256`: Prüfsumme des SHA-Manifests.
- `KOSTEN.json`: Grenzen und Reviewer-Verbrauch; keine synthetischen Biotop-Kosten als reale Messung.

Die SHA-Liste schließt die ausdrücklich getrennten Arbeitskopien und pytest-Tempbestände aus; Repro-Fixtures, JUnit, Rohoutputs, Aufrufe und unveränderte Kopien der benannten Elternbelege sind enthalten.
