# Originalaudit: Nachweisleser, zweite/letzte Runde

## Ergebnis vorweg

Maßstab F7, vorrangig gegenüber dem alten letzten Auftragssatz: **Ein Nachweis zählt nur, wenn ausgeführt; skipped/abgebrochen/leer/fehlend rot statt grün.** Reparaturscope ausschließlich benannter Kernpfad und seine Ergebnisleser.

**126/126 inventarisierte Dateien gelesen; keine Implementierung und keine Ausführung von Biotop, Prüfskripten, Docker, Netz oder Modellen.** Die Dateilesung ist vollständig, der **Vollständigkeitsbeweis aller semantischen Lesestellen ist nicht erbracht**: 8 konkrete Kandidaten und 45 breite Quellzeilen ohne abgeschlossene Feinzuordnung bleiben ausdrücklich offen. Daraus folgt keine Entwarnung und kein neuer Reparaturzyklus.

Besonders für den aktuellen Kernpfad relevant, jenseits der bereits benannten Standardparser:

| Befund | Originalstelle | Präziser zusätzlicher Lesemechanismus |
|---|---|---|
| B03 / A06 | `biotop/organe/aegis.py:716-722` | Test-/Immun- und Vertragsdateiaufnahme allein nach Abwesenheit in der Fehlerdateiliste. Ein global nichtleeres JUnit reicht nicht: Jede aufgenommene Pflichtdatei braucht ihren Ausführungsbeleg. Dem Messarbeiter zugeordnet laut Parent/ZUSATZBEFUNDE. |
| B10 / EP04 | `biotop/organe/eichproben.py:454-472` | Normgegenprobe bleibt prüfbar, wenn ihre Pflichtzeugen fehlen/skipped sind, solange eine spätere Messhülle gültig ist. Negative Wahrheit ist dann kein ausgeführter negativer Zeuge. Laut Nachlieferung bereits Aegis-Teil; nicht hier als repariert verifiziert. |
| B07 / G02 | `biotop/organe/generation0.py:125-135,151-174` | `AEQ (\w+)` liest `keine` statt `keine-beobachtung`; der Abbruchschutz vergleicht den ungekürzten Marker. Auch der ausgegebene Beobachtungszähler n wird nicht gelesen; n=0 kann als identische Beobachtung dienen. |
| B11 / L08 | `biotop/lauf.py:634-644` | Gesamter Original-Gegenlauf scheitert: nur in stdout namentlich gefundene neue Tests werden entfernt; fehlt eine solche Zuordnung, wird die Folgeprüfung fortgesetzt. |
| B12 / L09 | `biotop/lauf.py:610-624,646-659` | Leere Mutanten-/nichtäquivalente Population erzeugt Anteilziel0 und `erreicht=True` aus0≥0. Das ist nicht die separate P4-Freeze-Lücke. |
| B08/B09 | `biotop/lauf.py:556,580` | Leere Nachbar-ID-Liste bzw fehlendes Paarmaß führen zu Bestätigung/Paar bestanden. Enge Ergebnisgrenze, **keine** Wirkungskreis-/Transitivitätsreparatur. |

Diese Zuordnung ist Inventarbefund, **keine Erweiterung des Reparaturauftrags**. Gen0 ist konkret über `lauf.generation0 → generation0.ergebnis → vorspann.verlangen(phase='mass') → mass_einfrieren` Vorstufe der Freigaberoute; daraus folgt kein allgemeiner Mutationssystem-Review.

## Nenner und Originalbasis

| Disjunkte Gruppe | Dateien |
|---|---:|
| Produkt | 36 |
| Prüfskripte | 63 |
| Eigentests | 11 |
| Vertragsfixtures | 7 |
| Konfiguration/Dokumente | 9 |
| **Gesamt, eindeutige Pfade** | **126** |

`ORIGINALBASIS-VERGLEICH.json` bestätigt programmatisch: alle Inventarpfade aus `QUELLEN.json`, die private Auditkopie und `/root/reparatur-01/review-02/repo` haben die ursprünglichen SHA-256-Werte; keine Abweichung bei126 Dateien. Maßgeblich bleibt dieser Originalstand, **nicht** der inzwischen integrierte Parent.

`NACHAUDIT-ORIGINAL.json` dokumentiert die vier gesondert beobachteten Aegis-Dateien: Änderungen an `aegis.py`, `eichproben.py`, `test_review_vertrag.py` sowie die neue `tests/test_junit_zeugen.py`. Die drei ursprünglichen Einträge bleiben Originaleinträge; die neue Datei vergrößert den Nenner nicht. Es wurden nur die neuen Hashes beobachtet, **kein** Patchabschlussreview und keine Testausführung vorgenommen.

Die Ergänzung `/root/reparatur-01/nachbesserung-02/lieferung/ZUSATZBEFUNDE.md:9-13` ist zusätzlich gelesen: Dateiaufnahme bleibt dem Messarbeiter zugeordnet; dort ausdrücklich nur Lesebefund und noch kein separater Annahme-Repro. Deren Repro-/Grünaussagen sind Fremdlieferung, nicht Ergebnisse dieses Audits.

## Tatsächlich erreichte Abdeckung

- 74 Dateien mit entsprechender Logik; 52 gelesen ohne entsprechenden Resultatleser.
- **145 semantische Leserblöcke**: 86 Kern-/Folge-/Anzeigeleser, 14 Kern-Eigentestblöcke und 45 historische Außenblöcke. Ein Block ist ein zusammengehörender Ergebnisverbrauch, nicht jede `.get`-Zeile und nicht jeder Regexfund.
- **16 deduplizierte bestätigte Fehlmechanismen**: 12 mit Kernort, 6 mit Außenort; zwei Mechanismen besitzen beides, also nicht addieren. Bestätigung heißt statischer, quellenbelegter Fehlmechanismus, nicht behaupteter externer Betriebsfall.
- **11 bestätigte Außenorte in 11 Dateien** separat in `AUSSERHALB-KERN-BESTAETIGT-OFFEN.json/.md`. Insbesondere `funde_neubewerten.py:29`, `verhandlungsprobe.py:71`, `proben_tor2.py:209` sind nach dem neuen Scope **bestätigt offen für eigenen Auftrag**, keine Fixpflicht hier.
- Von661 breiten Kandidatenzeilen: 488 einem Block zugeordnet, 87 Kommentar/Dokumentation/Import, 41 über begründet nicht relevante Dateien eingeordnet, **45 Feinzuordnungen offen**. Das sind keine Befundzahlen.
- Eingebettete `MESSSKRIPT`, Aegis-Pytest-Treiber, `_AEQUIVALENZ_SKRIPT`, Python in Shellstartern sowie Alias-/Weiterleitungspfade wurden mitgelesen. `pruefung/vorspann.py` ist die wichtige Ausnahme im Skriptverzeichnis: aktueller Kernwrapper, kein historischer Parallelprüfpfad.

**Begrenzung:** Die Liste dokumentiert tatsächlich gelesene Quellstellen und ihre direkten Ergebnisflüsse; sie ist keine Abwesenheitsgarantie für ungeprüfte Daten, dynamische Aufrufe, alle Schema-/Trunkierungsvarianten oder weitere externe Werk-/DBzustände. Keine Suche wurde als erfolgreich bewiesen, nur weil sie keinen Fehler meldete. Die offenen Mengen stehen maschinenlesbar, nicht verborgen in einer Nullsumme.

## Richtige Schutzgrenzen und Abgrenzungen

1. **Leere gültige Fehlermenge ist legitim**, wenn die geforderte Population tatsächlich ausgeführt und vollständig erfasst wurde. Fehlende Population, skipped, Abbruch oder fehlender Pflichtzeuge sind nicht dasselbe.
2. Original-`aegis.junit_lauf:103-105` hat einen negativen Ersatzzeugen für fehlende angeforderte Dateien. Daher ist `tests/test_eichproben.py:286` mit lokalem `all(values)` **kein zusätzlich bestätigter leerer-JUnit-Fall** im Originaldatenfluss; sein Skiprisiko liegt im Parser. Der Verdacht wurde nicht fälschlich hochgezählt.
3. `_vollstaendig`, Pflichtvorspannqualität, Rausch-Finitheits-/Genau5-Prüfungen, Siegel-/Quellenbindung und die Freigabevoraussetzung `status=='vorgelegt'` sind konkrete vorhandene Schutzstellen. Sie erben aber die Wahrheit ihrer unteren Ausführungsbelege. Hashgleichheit ist kein Testpass.
4. Oberfläche, Dienst-JSON, Kosten, Kurven und Lernmerkmale sind ausdrücklich von grünen technischen Abnahmeentscheidungen getrennt. Ein Kostenwert0 ist nicht automatisch ein Nachweisfehler. Ebenso können0 optionale Funde legitim sein; die vier Eichzeugen sind hingegen Pflicht.
5. Die technischen Voraussetzungen von Aufnahme/Gen0 sind erfasst; die Inhalte von Sicherheits-/Ethikmodellantworten werden **nicht bewertet**.
6. Die Vertragsausführung und das Paarurteil werden von der Frage getrennt, ob alle fachlich erforderlichen Vertragspartner/Transitiven überhaupt in der Prüfung liegen.

## Test-/Schutzzuordnung, kein Abschlussreview

`KERN-NACHWEISZUORDNUNG.json` ordnet jeden dokumentierten Kernreader einer vorhandenen Testquelle, einem begründeten Quellschutz/Weiterleitungszweck oder einer **offenen** Nachweispflicht zu. Die ursprünglichen Tests wurden nur gelesen, nicht ausgeführt. Zugeteilter Fixarbeiter und berichtete grüne Fremdlieferung sind kein eigener ausgeführter Nachweis.

Vorhandene Unit-Fixtures für Maß/Gate, echte Kammerintegration auf privaten Testwerken und optional übersprungene Bestandsprüfungen sind in der Matrix getrennt. Parent muss für verbleibende Kernbefunde die aktuelle Testabdeckung bzw den nachweisbaren Durchgriff eines Produzentenschutzes zuordnen; dieses Audit setzt fehlende Zuordnung nicht auf grün. Für Außenfälle wird daraus kein neuer Umfang.

## Vier bestehende Phase-4-Mechanismen bleiben offen

Siehe `P4-BESTEHEND-OFFEN.json/.md`: Wirkungskreis/Transitivität; Vertragsaustausch; NaN/Null-Collector; Gen0-Erfolgsbindung beim Freeze. Ein Nichtausführungsschutz repariert weder die Auswahl der relevanten Bereiche noch den Vertragsinhalt noch die gesamte Numerik-/Freeze-Kette. Diese Punkte bleiben ausdrücklich offen, nicht erledigt und nicht pauschal scopeausgeschlossen.

## Dateien und Verifikation

- `DATEIPRUEFUNG.json`: genau126 Inventareinträge mit Hash, Lesestatus, Relevanz, Scope/Datenfluss, Matrixverweisen und offenen Zuordnungen.
- `LESESTELLEN.json`: Originaldatei/-zeile, Eingabeherkunft, Fehler-/Leerheits-/Ausführungsschutz, Urteil, vollständiger Quellbereich, Scope, Befund- und Nachweiszuordnung.
- `BEFUNDE.json`: deduplizierte Mechanismen, Kern-/Außenorte, statische Minimalzustände, Abgrenzungen.
- Außenliste, P4-Liste, `KANDIDATEN-OFFEN.json/.md`, `SUCHTREFFER-ZUORDNUNG.json`, `ABDECKUNG.json`, Kernzuordnung, Originalvergleich und nachAuditOriginal-Hashsnapshot ergänzen die Lieferung.
- `VALIDIERUNG.json` und `SHA256SUMS` prüfen Inventar/Referenzen/Quellzeilen/Originalhashes und Integrität des Berichtspakets. Sie belegen **nur das Auditpaket**, nicht reparierte Biotop-Funktionen.

Arbeitsstanddateien sind Zwischenprodukte, keine zusätzliche Ergebnislieferung. Ausschließlich unter `audit/` geschrieben. Zwei Fehler beim eigenen Berichtsbau (Containerform des Quellzustands und provisorische Testzeilen) sowie ein falscher Metadatenfeldname wurden vor der finalen Erstellung korrigiert; finale Quellen-/Referenzvalidierung ist maßgeblich. Keine Produktrepros, keine DB-/Werkänderung und keine verdeckte Fortsetzung alter Prüfscripte.
