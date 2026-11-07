# Unabhängige Reparaturprüfung – Kernmaß, Rauschen, A/C und B

**Nicht bestanden (`passed=false`). Zwei neue/regressierte Logikfehler verbleiben.**
Keine neuen Sicherheitsbefunde im geprüften Umfang. Es wurde nichts implementiert und weder Original noch Review-Repository verändert.

## Maßstab und Prüfgrenze

Geprüft: vollständiger bereitgestellter `AENDERUNGEN.diff`, `STATIK.json` und Quellkontext unter
`/root/reparatur-01/review-01/repo`.

Die ausdrückliche Korrektur des Prüfprompts wurde berücksichtigt: **Toleranz = 1 + getrimmte Spannweite + 0.10**, Untergrenze **1.15**, Deckel **2.00**, **>1.5 Bereich sperren**. Die zurückgenommene Formel `1+2s` wurde nicht verwendet. Pareto je Test und die bestehende Mindestquote wurden nicht neu definiert.

Es liefen ausschließlich isolierte Unit-Prüfungen: keine Docker-/Kammerläufe, keine Modelle, kein Netz, keine produktive DB oder produktiven Werke. Quellcode und reale Entscheidungsfunktionen wurden geladen; Timing-/Modellgrenzen der Repros sind explizite Doubles. Die gesetzten Timingzahlen sind **keine real gemessenen Laufzeiten**. Alle Schreibwirkungen der Repros blieben in privaten Fixtures bzw. In-Memory-DBs. TMPDIR lag außerhalb der Werk-Quellen.

## MASS-01 · P1 – Rauschsperre übersieht verhandelte Wirkung

**Fehlgeschlagen:** Ein verhandeltes Paar wird vorgelegt und in die Privatfixture geschrieben, obwohl eine seiner Anpassungen einen rauschgesperrten Bereich erreicht.

**Neue Fehlerstelle:** `/root/reparatur-01/review-01/repo/biotop/lauf.py:325-330`.
Weitere neue Anteile: `biotop/lauf.py:533-542`, `biotop/kern/messgeraet.py:432` und `:463-465`.
Unveränderter, für die Regression relevanter Kontext: `biotop/organe/aegis.py:518-525` und `biotop/lauf.py:568-583`.

Minimales Drei-Bereichs-Szenario:
- Straßen: `alpha → beta`, `gamma → beta`; nur `gamma` ist gesperrt.
- `alpha` handelt eine Anpassung in `beta` aus. Beide Diffs bleiben im jeweils eigenen Bereich; der Befund hängt nicht an einem verbotenen bereichsfremden Schwarmdiff.
- Der Kandidat gewinnt ein Kernmaß in `alpha`. Der reale Anklagepfad speichert aber weiterhin nur `[alpha]` als Wirkungskreis.
- Die eigene Ableitung `landkarte.wirkungskreis('beta', kanten)` ergibt `[alpha, beta, gamma]`.
- Die neue Generalprobe vereinigt nur die unvollständigen gespeicherten Kreise. Gleichzeitig entfällt die Zeitprüfung für `gamma`; deshalb wird dessen Sperre nicht durchgesetzt.

**Ausführung:** `status=vorgelegt`, Kandidat in der privaten DB `angenommen`, `beta`-Datei verändert. Gegenkontrolle: Wenn zusätzlich der direkte Nachbar `beta` gesperrt wird, folgt `abgelehnt`, ohne Dateiänderung. Eine unabhängige Zweibereichskontrolle erlaubt die Änderung korrekt, wenn der gesperrte Bereich wirklich unberührt bleibt.

**Regressionsbeleg:** Der aus dem bereitgestellten Diff exakt im Speicher rekonstruierte alte Maßverbraucher lehnt dieselben gesetzten Grenzdaten ab: `gamma.laufzeit_ms: 10000.0 > Grenze 200.0`. Der neue liefert `ok=true`, `grenzen_gerissen=[]`. Beanstandet wird diese neue Kombination – nicht isoliert die ältere Herkunft des unvollständigen Wirkungskreises.

**Testlücke:** `tests/test_vorspann.py:318-346` ersetzt die Einzelprüfung und setzt bereits einen Kreis `[alpha]`; `:349-360` prüft nur den direkt gesperrten Nachbarn. Ein erlaubter Nachbar mit gesperrtem Abhängigen fehlt.

**Minimale Korrekturrichtung:** Kreis aus allen tatsächlich übernommenen Änderungen einschließlich Nachbaranpassungen ableiten und transitiv erweitern. Bestehende Sperre anwenden, ohne die Rauschgrenze oder Pareto zu ändern.

Reproduktion (aktuell Assertion-Fehler):
```sh
/root/reparatur-01/venv/bin/python -B -m pytest -q -p no:cacheprovider /root/reparatur-01/review-01/pruefer-mass/test_review_contracts.py::test_negotiated_adaptation_must_block_its_blocked_dependents
```

Rohbelege:
- `/root/reparatur-01/review-01/pruefer-mass/negotiation-raw.json` – `cases[0]` enthält Diffs, Mess-Doubles, Entscheidungsprotokoll, DB-Rücklese und Dateistände.
- `/root/reparatur-01/review-01/pruefer-mass/negotiation.stdout.txt`
- `/root/reparatur-01/review-01/pruefer-mass/baseline-comparison.json` – Abschnitt `negotiation`.
- `/root/reparatur-01/review-01/pruefer-mass/repro-raw.json` – ergänzende Scope-/Unberührt-Kontrollen.

## MASS-02 · P2 – Ungültiger Bereich verwirft die ganze Kalibrierung

**Fehlgeschlagen:** Die neue Wertevalidierung wird nicht bereichsweise abgefangen. Ein ungültiger Bereich verhindert auch die Nutzung gültiger Nachbarbereiche und deren Kalibrier-/Verbrauchsbeleg.

**Neue Fehlerstelle:** `/root/reparatur-01/review-01/repo/biotop/kern/messgeraet.py:352-354`.
Aufruferkontext: `biotop/organe/eichung.py:124-150` und `:192-218`.
Neuer verbindlicher Gate-Pfad: `biotop/organe/vorspann.py:115-122`, `:151-152`.

Minimaler Input am Collector: fünfmal `{alpha: 0.0, beta: 100.0}`; dieselbe Auswirkung mit `NaN` statt `0.0`. Nullwerte können aus der bestehenden Rundung sehr kurzer Laufzeiten entstehen. Ungültige Werte **dürfen nicht freigegeben werden**; erwartet ist die Sperre von `alpha` bei Erhalt von `beta` mit Toleranz `1.15`.

**Ausführung:** Nach fünf Aufrufen des Mess-Doubles propagiert `ValueError`; keine Rückgabe, `eichung_rows=[]`, `eichkosten_rows=[]`. Der verbindliche Vorspann erklärt dadurch den gesamten Versuch für gescheitert. Bei der Gegenkontrolle mit `alpha=None` funktioniert die gewünschte Bereichstrennung bereits: `gesperrt=['alpha']`, `toleranz={'beta':1.15}`, `lauf_startet=true`.

Das ist ein neu eingeführter Ausnahmeeffekt, kein Einwand gegen die strengere Wertevalidierung. Der alte Rechner akzeptierte Null fälschlich; diese alte Freigabe soll ausdrücklich **nicht** wiederhergestellt werden.

**Testlücke:** `tests/test_rauschmessung.py:15-18` erwartet nur die Ausnahme des Zahlenhelfers. `tests/test_vorspann.py:144-160` verändert ein bereits fertig gemocktes Gesamtergebnis, ohne den mehrbereichigen Collector auszuführen.

**Minimale Korrekturrichtung:** Ungültigkeit pro Bereich in einen gesperrten Beleg überführen, andere Bereiche weiter auswerten, verbrauchte Arbeit/Rohdaten auch bei Fehlern sichern. Kein Fallback für den ungültigen Bereich.

Reproduktion (aktuell beide parametrisierten Fälle rot):
```sh
/root/reparatur-01/venv/bin/python -B -m pytest -q -p no:cacheprovider /root/reparatur-01/review-01/pruefer-mass/test_review_contracts.py::test_invalid_area_must_not_discard_valid_other_area
```

Rohbelege:
- `/root/reparatur-01/review-01/pruefer-mass/repro-raw.json` – `invalid_area_cases`.
- `/root/reparatur-01/review-01/pruefer-mass/repro.stdout.txt`
- `/root/reparatur-01/review-01/pruefer-mass/reviewer-contracts.stdout.txt`

## Bestandene Prüfung und tatsächliche Testempfindlichkeit

Die vorhandenen ausgewählten Eigen-Tests: **152 bestanden**, 0 Fehlerassertionen, 0 Infrastruktur-/Setupfehler, 0 übersprungen. Das ist kein Vollsuite- oder Docker-Nachweis.

| Modul | Ausgeführte Fälle |
|---|---:|
| `tests.test_ansage_aufnahme` | 21 |
| `tests.test_artvorlage` | 12 |
| `tests.test_doppelungsschluessel` | 9 |
| `tests.test_kernmass_pareto` | 15 |
| `tests.test_rauschmessung` | 31 |
| `tests.test_vorspann` | 64 |

- **Kernmaß/Pareto:** Bestandene Tests geben keine F2-Punkte. Einzelregression trotz sinkender Fehlersumme wird erkannt, gemeinsame Altfehler bleiben unterschieden. Keine neue F2-/Pareto-Regression gefunden.
- **Rauschen:** Korrigierter F6-Standard, Vollständigkeit, ungerundete Aussetzeridentität, begrenztes Nachmessen und gemessene statt fester Toleranz sind in den vorhandenen Unitfällen empfindlich. Die beiden obigen Integrationsfälle fehlen.
- **A/C:** Nur die aktuelle Ansagezeile wird ausgenommen. Historische/fremde und aufgenommene gleichschlüsselige Einträge bleiben erhalten; Fund- und Normzweig sind abgedeckt. Vollständiger Vorrat statt Prompt-/Abfragefenster wird geprüft.
- **B:** Fremdpopulation wird vor einem Gesamtfenster ausgewählt; im 25er-Fenster greift die aufgerundete halbe Quote soweit tatsächlich verfügbar. Die Tests lesen dargestellte IDs gegen ihren gespeicherten synthetischen Vorrat zurück, einschließlich knapper und älterer Vorräte. Kein neuer B-Fehler gefunden; kein Produktionsbestands-Replay behauptet.

Zusätzlich wurden **8 gezielte Fehlervarianten nur im Prozessspeicher** eingeschaltet. Jede wird durch mindestens eine inhaltliche Testassertion erkannt; keine Sammlung-/Setupfehler. Diese absichtlich roten Mutationsläufe sind nicht als Produktfehler gezählt.

| Mutant | Ausgeführt | Erwartet rot | Setupfehler |
|---|---:|---:|---:|
| `erase_history_by_key` | 8 | 8 | 0 |
| `foreign_global_window` | 12 | 2 | 0 |
| `foreign_quota_floor` | 12 | 5 | 0 |
| `ignore_measured_tolerance` | 4 | 2 | 0 |
| `kernmass_rewards_passes` | 15 | 3 | 0 |
| `pareto_aggregate_only` | 15 | 1 | 0 |
| `rounded_outlier_identity` | 3 | 3 | 0 |
| `self_announcement_not_exempt` | 2 | 2 | 0 |

Die unabhängigen Zusatztests gegen den **unveränderten Reparaturstand** ergeben dagegen **3 fehlgeschlagen, 2 bestanden**. Ein roter Fall belegt MASS-01, zwei Wertevarianten belegen MASS-02; beide Positivkontrollen bestehen.

Rohdaten und Kommandos:
- `/root/reparatur-01/review-01/pruefer-mass/test-summary.json`
- `/root/reparatur-01/review-01/pruefer-mass/unit-checks.xml`
- `/root/reparatur-01/review-01/pruefer-mass/unit-checks.stdout.txt`
- `/root/reparatur-01/review-01/pruefer-mass/reviewer-contracts.xml`
- `/root/reparatur-01/review-01/pruefer-mass/reviewer-contracts.stdout.txt`
- `/root/reparatur-01/review-01/pruefer-mass/check_sensitivity.py` (je Modus eigene XML-/stdout-/stderr-Datei)
- `/root/reparatur-01/review-01/pruefer-mass/run_unit_checks.py`
- `/root/reparatur-01/review-01/pruefer-mass/repro_mass.py`
- `/root/reparatur-01/review-01/pruefer-mass/repro_negotiation.py`
- `/root/reparatur-01/review-01/pruefer-mass/compare_baseline.py`

## Sicherheits-Scan und Abgrenzung

Der einzige Treffer aus `STATIK.json`, `biotop/organe/kammer.py:103`, ist **kein Secret**: `token` ist das Rücksetz-Token eines `ContextVar`, korrekt im `finally` bei Zeile 107 zurückgesetzt. `security_concerns=[]`.

Unveränderte alte fachliche Eigenschaften wurden nicht als neue Reparaturfehler ausgegeben. Insbesondere zeigt das Rohmaterial weiterhin die alte `bool→float`-Koercion im Collector; sie wird hier nicht als neue Regression gezählt. Ebenso gilt die alte Wirkungskreisableitung nur als Kontext für die belegte **neue** Freigaberegression.

## Unverändertheitsnachweis und Dateien

**125 von 125 Dateien** der Reviewkopie sind nach Inhalt, Größe und mtime unverändert; sämtliche **125 Quellhashes** passen zum bereitgestellten Manifest. Keine Implementierung, kein git stash/reset/commit. Die Prüfprogramme legen nur eigene Artefakte und private Fixtures im Prüferverzeichnis an.

- Ergebnis-JSON: `/root/reparatur-01/review-01/pruefer-mass/ERGEBNIS.json`
- Deutscher Bericht: `/root/reparatur-01/review-01/pruefer-mass/BERICHT.md`
- Vorher: `/root/reparatur-01/review-01/pruefer-mass/repo-vorher.json`
- Nachher: `/root/reparatur-01/review-01/pruefer-mass/repo-nachher.json`
- Vergleich: `/root/reparatur-01/review-01/pruefer-mass/unveraendert.json`
- Vollständige Artefaktliste mit Prüfsummen: `/root/reparatur-01/review-01/pruefer-mass/MANIFEST.json`
- Prüfsummenliste: `/root/reparatur-01/review-01/pruefer-mass/SHA256SUMS`

**Freigabe bleibt verweigert, bis MASS-01 und MASS-02 behoben und die Zusatzfälle samt Positivkontrollen erneut ausgeführt sind.**
