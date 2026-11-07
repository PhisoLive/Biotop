# Abnahme Eichung 01 — vier Positivproben und vier echte Gegenproben

**Erfüllt am kopierten Werk: vier ausgeführte, prüfbare Positivprädikate True und vier ausgeführte, prüfbare Gegenprädikate False. Eigener pytest: 21 bestanden, 0 Fehler/Fehlschläge/Skips (215.138 s).**

Alle acht Eingaben liefen durch dieselbe `aegis.pruefen`-Implementierung mit derselben `_bestanden(name, belege)`-Auswertung. Der Prüfer erhält keinen Gegenproben-Schalter; dieser verändert ausschließlich die Eingabe. Originale Aegis-/Maß-/Pareto-/Vertragsableitungen wurden verwendet, keine Ersatzbewertungen. Feste mechanische Angriffe statt Netzmodellen.

## Ausgeführte End-to-End-Paare

| Kennung in BELEGE.json | ausgeführt | prüfbar | Bestehensprädikat | Kammern |
|---|---|---|---|---|
| proben.nebenwirkung | True | True | True | 2 |
| gegenproben.nebenwirkung | True | True | False | 2 |
| proben.regression | True | True | True | 7 |
| gegenproben.regression | True | True | False | 7 |
| proben.norm | True | True | True | 8 |
| gegenproben.norm | True | True | False | 4 |
| proben.vertrag | True | True | True | 4 |
| gegenproben.vertrag | True | True | False | 4 |

- **Nebenwirkung:** echter A-Gewinn `['bericht.tests_fehlgeschlagen: 6 → 5']` und B-Verlust `['lager.tests_fehlgeschlagen: 0 → 27']`. A-Ausgangsdefekte wurden nur in der privaten Kopie gesetzt, am Kandidaten behoben; B wurde dort geschädigt. Gegenprobe behebt A ohne B-Schaden und ergibt False.
- **Regression:** originaler Einzeltest `tests/test_lager.py::test_entnehmen` wechselt von grün auf bestätigt rot; zusätzlich 3 tatsächlich ausgeführte grüne Tests. Der Original-Pareto-Beleg nennt diesen Einzeltest ausdrücklich. Gegenprobe lässt B unverändert, führt dieselben grünen Zusatztests aus und ergibt False. Die Zusatztests werden vom originalen Aegis als schon an der Basis grün korrekt nicht als Gewinn gezählt.
- **Norm:** `lagerhaus/lager/bestand.py::Lager().bestand('eichprobe_eingabe'): abweichende Rückgabe ohne Verweis`. Basis `AssertionError: assert 0 == 'eichprobe_norm_neu'
 +  where 0 = bestand('eichprobe_eingabe')
 +    where bestand = <lagerhaus.lager.bestand.Lager object at 0x775b2a5e0b00>.bestand
 +      where <lagerhaus.lager.bestand.Lager object at 0x775b2a5e0b00> = Lager()`; Fehlerort `tests/test_lager_eichprobe_norm.py`, nicht im Werk. Kandidat-Zeuge besteht. Kein aufgelöster Vertragsverweis. Originaler Normeintrag `['norm_k2680_lager:offen_norm']`, explizites `mass.zuwachs=0`, keine Aufnahme des Normtests in `_dateien` oder tatsächliches Werk. **Die echte Gegenprobe hat ebenfalls Maß/Zuwachs 0 und dieselbe echte Verhaltensänderung, erreicht aber keinen Aegis-Normpfad: `norm=[]`, kein Normeintrag, daher False.** Das fängt genau den alten falsch-grünen Fallback.
- **Vertrag:** `test_vertrag_bericht_lager.py::test_eichprobe_vertrag_neue_zusicherung` wird original als verletzt benannt. Der reale Konsumententest `tests/test_bericht.py::test_lagerwert_leer` fällt in `lagerhaus/bericht/auswertung.py` beim tatsächlichen Aufruf der fehlenden Lieferantenzusicherung. Gegenprobe implementiert diese Zusicherung im Lieferanten; derselbe Konsument und Vertrag bestehen, Gegenprädikat False. Nicht bloß irgendeine Ablehnung.

Bei Nebenwirkung/Regression nennt der obere Aegis-Grund zusätzlich die gerissenen Verträge. Entscheidend sind hier die ebenfalls tatsächlich erzeugten spezifischen `mass.pareto_besser`/`mass.pareto_schlechter`-Belege, nicht die pauschale Ablehnung. Bei Vertrag wird die genaue Vertragskennung verlangt.

## Herkunft, Isolation, Kosten

- Eingefrorener Biotop-Quellstand: `b42dc941e7fcb66632ba6a0e13b8df106a270a31` (git archive, keine daten/ oder .git-Kopie). Nur vier geänderte Dateien im Diff.
- Werkquelle: `/root/reparatur-01/teil-eichung/werk-lauf25-kopie`, zuvor aus dem in der privaten SQLite-Sicherung zu Lauf 25 verzeichneten Pfad kopiert. Bereichspaar `bericht→lager`; Vertrags-SHA256 `b69270558c12328906acf851cc12a66f617c0fc27b4818d52432671538a4bc6c`. Kein stiller Wechsel auf ein anderes Paar.
- Laufkennung 26 existiert nur in der Test-DB-Kopie, mit NULL-Maß und Budget 0. Ursprüngliche Läufe 24/25 wurden nicht fortgesetzt. Werk- und vollständiger privater DB-Bestand vor/nach `proben` identisch (Hashbelege unter `BELEGE.json.abnahme`). Auch die gelesene vertrauliche DB-Sicherung blieb unverändert. Keine Datenbank im Lieferpaket.
- **Batterie:** 38 tatsächliche, über eindeutige Containerkennungen abgeglichene Kammeraufrufe; 0 Modellaufrufe; 0.000000 EUR Modellkosten; 72.203 s. Jede Zeile ist in KOSTEN.csv und mit RC/stdout/stderr in BELEGE.json belegt. Eingangsmessung und andere pytest-/TDD-Läufe gehören nicht in diese Batteriezahl; deren Gesamtkammerzahl wird nicht behauptet.

## Rot/Grün und Grenzen

- Reale Erstbelege und zugehörige Ausgaben: 01→02 Normimport; 03→04 Kontextdiff; 05→06 geschützte reine Probeoption; 07→08 tatsächlicher Kammerzähler; 09→10 Normprädikat/Gegenprobe; 11→12 Nebenwirkung; 13→14 Regression; 15→16 Vertrag; 17→18 Isolation/vier Paare; 20→21 Normmethode; 22→23 A-Gewinn trotz Rückwirkung; 25→26 Norm-/Zeittrennung; 27→28 Fehlerkennzeichnung/Textausgabe. Exakte pytest-Ergebniszeilen stehen in ROT-GRUEN.csv, nicht nachträglich erfundene Sollausgaben.
- Der erste Echtwerkversuch 19 scheiterte an fehlender frei aufrufbarer Skalarfunktion im versiegelten Bereich lager. Die vorhandene Methode Lager.bestand wurde daraufhin unterstützt (roter Methodentest 20). 21 blieb als Gesamtabnahme rot: Rückwirkung des B-Schadens auf A sowie ein zusätzlich strenger Zeitgrenz-Check im Normprädikat. Diese roten Versuche bleiben rot und sind keine Abnahme. Ausgabe 24 war ein fehlerhafter Referenzlast-Testaufbau ohne /werk im Suchpfad; erst 25 ist der gültige rote Beleg für die Zeittrennung.
- Alte produktive Norm-Zeilen (einschließlich des im Gutachten genannten K2083) werden weder verändert noch nachträglich als gut erklärt. Abnahme ist ausschließlich der neu ausgeführte Stand 28.
- Laufzeitbefunde bleiben transparent im Originalurteil. Die Batterie kalibriert weder Rauschtoleranz noch erklärt sie alle Zeitgrenzen für gesund; das separate Eltern-Gate bleibt erforderlich. Im endgültigen Vertrags-Positivfall liegt zusätzlich ein preise-Laufzeitgrenzbefund vor; die Norm-Endzeile besitzt keinen solchen Zusatzbefund. Die Normmechanik wurde zusätzlich mit einer echten, absichtlich gerissenen Zeitgrenze positiv/negativ geprüft.
- Der aktuelle A/C-Elternstand wurde nicht als identisch vorausgesetzt und hier nicht mitgetestet. Aegis nur über die drei klar abgegrenzten Probeoption-Hunks integrieren; aktuelle Ansage-/C-Weiterleitung bewahren. Danach unabhängige Eltern-Abnahme.

## Lieferdateien

- `dateien/`: vollständige vier geänderte Dateien; Aegis ist die Referenzfassung gegen die eingefrorene Basis, keine Copy-over-Empfehlung.
- `AENDERUNGEN.diff`, `AEGIS-PROBEOPTION.diff`: vollständiger Git-Diff und isolierter Aegis-Anteil.
- `BELEGE.json`, `PYTEST.xml`, `KOSTEN.csv`, `ROT-GRUEN.csv`, `rot-gruen/`: tatsächliche Messungen und Rohprotokolle.
- `INTEGRATION.md`: kompatible Signatur, Rückgabefelder, Zusammenführung und ausgeführter Prüfbefehl.
- `DATEIEN.txt`, `PRUEFSUMMEN.sha256`: erlaubnislistenbasierter vollständiger Dateinachweis; ausdrücklich keine SQLite- oder Zugangsdaten.
