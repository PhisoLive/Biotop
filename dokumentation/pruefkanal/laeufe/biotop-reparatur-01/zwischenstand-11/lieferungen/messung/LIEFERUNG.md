# Lieferung – Messgerät, Fassung 7, Fixrunde 2

**Die lokale Kern-Eigensuite ist grün; die breitere Integrationsprüfung ist wegen einer alten Gültigkeitserwartung nicht grün.** Dies ist der zugeteilte Dateiteil derselben zweiten und letzten automatischen Runde, keine zusätzliche Runde und keine Freigabe des gesamten Biotops.

## Geändert

Ausschließlich im zugeteilten Repository:

- `biotop/kern/messgeraet.py`: konkrete JUnit-/Kammer-/Scanner-/Messresultatleser abgesichert.
- `tests/test_messnachweise.py`: neu, **60 ausgeführte Eigen-Testfälle**, davon **45 mit echtem Kammerlauf** und **15 Unit-Fälle** an den originalen Übergaben/Urteilsfunktionen.

Vollständige übernehmbare Dateien stehen unter `dateien/`; `AENDERUNGEN.diff` vergleicht gegen das anhand von `QUELLEN.json` bestätigte eigene Ausgangsmodul. Kein Commit und keine Integration. Von 126 inventarisierten vorhandenen Dateien blieben 125 bytegleich; nur das erlaubte Messgerät wurde geändert. Kein vorhandener Test wurde editiert.

## Ergebnis der Nachweisreparatur

- Skipped/xfail, fehlendes oder leeres JUnit, Sammlungsausfall und Teilabbruch gelten nicht mehr als vollständiger Messnachweis. Ein kleiner Begleitbeleg **aus demselben pytest-Subprozess** unterscheidet gesammelte, aufgerufene und abgeschlossene Fälle. Insbesondere bleibt ein vollständig ausgeführter Testfehlschlag mit pytest rc1 gültiger Inhalt; rc1 wird nicht pauschal als Infrastrukturfehler verworfen.
- Jede vor dem Lauf erwartete `test_*.py` unter `tests/` muss beitragen, einschließlich Unterordnern. Eine leere Pflichtdatei neben einem grünen Nachbarn reicht nicht. Abgewählte Tests und ein nachträglich entfernter JUnit-Fehlschlag werden gesperrt. Gutpaare mit ausgefüllter identischer Pflichtdatei wurden ausgeführt.
- Bandit-/Vulture-Störungen erzeugen kein scheinbares Sicherheit0/Tote0 mehr. Die gestellten Scannerantworten wurden tatsächlich über Scanner-Subprozesse in den Original-Messpfad eingespeist. Saubere installierte Scanner, echte Befunde und gültige nicht scoring-relevante Vulture-Befunde bleiben messbar. Reguläre leere Vulture-stdout bei beendetem rc0 ist kein fehlender Nachweis.
- Ein Messmarker allein reicht bei abgebrochener Kammer oder fehlenden angeforderten Bereichen/Werk-Pflichtfeldern nicht. Die äußeren rc-/Marker-Fälle sind ausdrücklich **Unit-Doubles**, nicht behauptete reale OOM-/Kill-Versuche.
- Fehlende Einzeltestlisten lassen Pareto nicht mehr grün werden. Die Liste wird auch nicht mehr bei 100 Fehlschlägen abgeschnitten. Tatsächlich ausgeführte Klassen-Tests werden anhand des bestellten JUnit-Dateifeldes statt des Klassen-Endstücks korrekt zugeordnet.
- Eine **bestellte** Referenzlast benötigt ihr Ergebnis. Ohne bestellte Referenzlast bleibt `laufzeit_ms=None` zulässig. Keine Rausch-, Kernmaß-, Sicherheits- oder Grenzschwelle wurde geändert.

`BEFUNDE.json` enthält 16 untersuchte Lesestellen-Gruppen, jeweils mit Kernpfadbezug, Urteil, Negativtest, Gegenroute, Belegart und Grenzen. Es unterscheidet behobene Funde von bloßen Lesebefunden; keine Behauptung allgemeiner Prüferkorrektheit.

## Ausgeführte Prüfungen

| Beleg | Reale Ausgabe | Einordnung |
|---|---|---|
| `roh/31-final/junit.xml` | **106 bestanden, 0 Fehler, 0 skipped**; 45 echte Kammeraufrufe | 60 neue Fälle plus unveränderte Kernmaß-/Pareto-/Rausch-Eigen-Tests |
| `roh/28-original-replay/junit.xml` und `roh/30-original-gutpaare/junit.xml` | Originalmodul: **48 fehlgeschlagen, 12 bestanden** über dieselben 60 eigenen Fälle | Zusätzliche Baseline-Reproduktion; 48 fehlende Erwartungen, nicht „48 unabhängige Bugs“ |
| `roh/27-lokale-regression/junit.xml` | **129 bestanden, 1 fehlgeschlagen, 2 skipped**; 237 echte Kammeraufrufe | Breitere Eichproben-/Vertragsintegration; kein grüner Gesamtbeleg |

**Integrationskollision:** `tests/test_review_vertrag.py:103`, Fall `[setup]`, verlangt weiterhin `messung.gueltig=True`, obwohl der Setup-Fehler den Testkörper verhindert. Beide originalen Probenrouten sind jetzt korrekt nicht prüfbar und die Messhülle ungültig. Diesen fremd zugeteilten Test habe ich nicht geändert. Begründung und nötige Parent-Anpassung stehen in `INTEGRATIONSHINWEIS.md`. Die zwei Skips betreffen nicht bereitgestellte private Werk-/DB-Kopien; sie zählen nicht als Nachweis. Die drei ergänzenden direkten Gutkontrollen wurden nach diesem breiteren Lauf in `30`/`31` geprüft.

Die TDD-Schritte sind separat erhalten: Tests zuerst, nachvollziehbares Rot, kleiner Fix, Grün. `VERSUCHE.json` enthält **31 Versuche** und **557 vollständig archivierte echte Kammer-Aufrufdatensätze**, ohne verschachtelte Doppelzählung. Hinzu kommt **ein aus JUnit/Traceback ableitbarer Lauf ohne vollständigen archivierten Kammerdatensatz**: Versuch `05` hatte einen zu langen Belegdateinamen. Nicht als gemessener Rohzähler addiert; vor dem betreffenden Produktfix in `06` vollständig wiederholt. Eine anfängliche eigene äußere/innere rc-Verwechslung (`02`) und eine zu enge Vulture-Formatprüfung (`14`) sind ebenfalls sichtbar erhalten, nicht weggeglättet.

`EIGENTESTS.json` verbindet die eigenen Fälle mit Original-/Finalstatus und Rohdateien. `KENNZAHLEN.json` enthält die programmgesteuerte Auszählung. Bei langen XML-Dateien transportiert die Fixture verlustfrei zlib/base64; die dekodierten Belege stehen zusätzlich unter `roh/ausgepackt/`.

## Reproduktion

Im zugeteilten Repository, ohne Netz/Modelle und ohne Installationen:

```sh
PYTHONPATH=/root/reparatur-01/nachbesserung-02/messung/repo \
PYTHONDONTWRITEBYTECODE=1 \
TMPDIR=/root/reparatur-01/nachbesserung-02/messung/tmp \
/root/reparatur-01/venv/bin/python -m pytest \
  tests/test_messnachweise.py tests/test_kernmass_pareto.py tests/test_rauschmessung.py -q
```

Für archivierte Wiederholungen mit neuem, noch nicht existierendem Label:

```sh
/root/reparatur-01/venv/bin/python /root/reparatur-01/nachbesserung-02/messung/lieferung/pruefen.py NEUES-LABEL tests/test_messnachweise.py -q
```

Das optionale `-p original_plugin` lädt ausschließlich `roh/messgeraet.original.py` aus dieser Lieferung statt des neuen Moduls; es schreibt nichts in den Repository-Quellstand. Deshalb unterscheidet `VERSUCHE.json` ausdrücklich Repository-Hash und tatsächlich ausgeführtes Modul. `packen.py` ist der interne, bereits ausgeführte Ableitungstreiber; nach Versiegelung nicht erneut über dieselben gelieferten Bytes laufen lassen.

## Grenzen und offen

- Kein Parent-/Produktionsbestand gelesen oder verändert. `QUELLEN.json` wurde mit der eigenen Kopie abgeglichen, nicht die Produktion erneut gehasht. TMPDIR liegt außerhalb rekursiv kopierter Werke. MESSSKRIPT und Werk-Testcode liefen nur in der netzlosen Kammer. **0 Modellaufrufe, 0 EUR Modellkosten**; keine Installation, kein Image-Neubau.
- P4 bleibt ausdrücklich offen: Wirkungskreis/Transitivität, Vertragsaustausch, NaN/Null-Rauschcollector und Gen0-Erfolgsbindung an Freeze. Keine Nebenreparatur.
- `vergleichen(...None...) -> gleich/nicht messbar` ist als Anzeige eingeordnet, nicht als reproduzierte Kernzulassung. Legacy-Prüfskripte wurden nicht bearbeitet. Nicht erschöpfend geprüft wurden beliebig manipulierte konsistente Protokolle, beliebige projektspezifische Testdiscovery, andere Scannerversionen und historische Bestwerte.
- Diese Lieferung deckt den exklusiven Messgerät-Dateiteil ab. Breitere Suche ist damit nicht als abgeschlossen oder fehlerfrei erklärt. **Endgültige vollständige Suite, aktualisierte Aegis-Integration, CLI und Entscheidung bleiben beim Parent/Philipp.** Historische 188/188 werden nicht umgeschrieben.

## Ablage

`/root/reparatur-01/nachbesserung-02/messung/lieferung/`

- Bericht: `LIEFERUNG.md`
- Inventar/Dateiliste: `MANIFEST.json`, `DATEIEN.txt`
- Prüfsummen: `SHA256SUMS`, `SHA256SUMS.sha256`
- Kosten: `KOSTEN.md`
- Quellen/Tests: `dateien/`, `AENDERUNGEN.diff`
- Befunde und Rohbelege: `BEFUNDE.json`, `VERSUCHE.json`, `EIGENTESTS.json`, `roh/`
