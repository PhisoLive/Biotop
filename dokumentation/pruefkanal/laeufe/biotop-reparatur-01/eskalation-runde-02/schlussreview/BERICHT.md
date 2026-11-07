# Unabhängiger Schlussbefund – review-03

**NICHT BESTANDEN.** Die zweite und letzte Reparaturrunde erreicht die enge Abnahme nicht. Die aktuelle Vollsuite enthält zwei Fehlschläge; der reale aktuelle Pflichtvorspann endet ohne Gen0-Freigabe. Keine weitere automatische Reparaturrunde wurde begonnen.

## Prüfgrenze und Integrität

Ein lesender unabhängiger Durchgang: zuerst vollständiger Diff und Statik, anschließend Quellpfade und Elternrohbelege. Kein Import oder Start von `/root/biotop`, kein Docker, Werk-, DB-, Anbieter- oder Netzstart; keine Installation, Subdelegation oder Produktänderung. Nur deklarierte synthetische Parser-/Verbraucherkontrollen im Prüferordner wurden ausgeführt.

Alle **129 Quellen** stimmen vor und nach der Prüfung in SHA256, Größe und mtime_ns mit `QUELLHASHES.json` überein. Der Diff nennt **9 Pfade**; die **111 Pythondateien** sind AST-parsebar. Das ersetzt keine Funktionsabnahme. Die Elternmetadaten binden jeweils **36 Produktquellhashes**; bei 59–63 stimmen diese mit der aktuellen Kopie überein. 58 enthält erwartungsgemäß den älteren Stand von Messgerät, Lauf und Fundprüfung. Diese Produktquellbindung wird nicht als Hashbeleg für sämtliche Testdateien ausgegeben.

## Nachgezählte Ausführungsbelege

| Elternbeleg | Exit | JUnit-Fälle | Bestanden | Fehlgeschlagen | Error / Skip | Kammern / eindeutige Container |
|---|---:|---:|---:|---:|---:|---:|
| 58 – Leser Rot | 1 | 103 | 21 | 82 | 0 / 0 | 57 / 57 |
| 59 – Leser Grün | 0 | 103 | 103 | 0 | 0 / 0 | 57 / 57 |
| 60 – Vertragsintegration | 1 | 6 | 3 | 3 | 0 / 0 | 54 / 54 |
| 61 – Vertragsintegration Grün | 0 | 6 | 6 | 0 | 0 / 0 | 54 / 54 |
| 62 – aktuelle Vollsuite | 1 | 305 | 303 | 2 | 0 / 0 | 345 / 345 |
| 63 – aktuelle reale -1-CLI | 1 | kein JUnit-Suitelauf | — | — | — | 83 / 83 |

Zähler aus XML-Testcases und Containerkennungen berechnet, gegen deklarierte Summen geprüft. Insgesamt **650 unterschiedliche Elterncontainer** in diesem Belegausschnitt; keine Hochrechnung und keine Doppelzählung eingebetteter Batteriezeilen. Die Nichtnull-Exits einzelner innerer Kammern sind nicht pauschal fehlgeschlagene Eigentests: einige gehören zu absichtlichen Negativkontrollen.

60→61 ist **kein weiterer Produktfix**: Die gebundenen Produktquellen sind gleich. In 60 verlangen die Fälle setup/skip/xfail irrtümlich eine gültige Messhülle. Die aktuelle Testfassung verlangt dort gemäß F7 Ungültigkeit; eine tatsächlich ausgeführte Call-Ausnahme bleibt dagegen zunächst ein Inhaltsresultat. Die grünen Teilprüfungen aus 59/61 heben das rote Gesamtergebnis aus 62/63 nicht auf.

## KERN-01 – integrierte Eichbatterie nicht funktionsfähig

**Blockierende Abnahmeverfehlung.** Sowohl in 62 als auch in 63:

| Probe | Positiv: ausgeführt / prüfbar / bestanden | Gegenprobe: ausgeführt / prüfbar / bestanden |
|---|---|---|
| Nebenwirkung | ja / nein / nein | ja / ja / nein |
| Regression | ja / nein / nein | ja / ja / nein |
| Norm | ja / ja / ja | ja / ja / nein |
| Vertrag | ja / nein / nein | ja / ja / nein |

Damit nur **1 von 4 gültigen Positivtreffern**, aber **4 von 4 gültigen falschen Gegenzeugen**. Jede Batterie enthält nachgezählt **38 Kammern**. Gegenzeugen werden nicht aus dem Wort „abgelehnt“ abgeleitet: Nebenwirkung/Regression haben keine entsprechende Pareto-Verletzung, Norm keine Normaufnahme, und der Vertragsgegenzeuge besteht am benannten Vertrag und Verbraucher ohne Vertragsverletzung. Laufzeit-Grenzbefunde bleiben gesonderte Originalbefunde.

Die Vertragsursache ist konkret belegt: `eichproben.py:376–420` baut den Aufruf der nicht vorhandenen `lagerhaus.lager.eichprobe_zusicherung` ein. Die aktuelle Rohmessung enthält **6 ausgeführte Fehlschläge und 95 Erfolge** sowie `bericht.laufzeit_ms=null` mit `AttributeError("module 'lagerhaus.lager' has no attribute 'eichprobe_zusicherung'")`. Der absichtliche Vertragsbruch trifft auch die bestellte Referenzlast. `messgeraet.py:273–280` verwirft die Messung; `aegis.py:706–719` bricht vor dem Kernmaß-/Vertragsurteil ab. `eichproben.py:464–475,488–493` kann dadurch kein vollständiges gültiges Paar liefern. Belegt durch Container **biotop-f1adc0ee8961** (62) und **biotop-eaed9bccec9b** (63), jeweils `proben.vertrag.kammer[3]`.

Bei Nebenwirkung/Regression belegen die erhaltenen Begleitlisten **96 Call- und 100 Teardown-Berichte**. Ohne Call bleiben:
- `tests/test_bericht.py::test_bewegungsbericht`
- `tests/test_bericht.py::test_lagerwert_gesamt`
- `tests/test_bericht.py::test_lagerwert_veraendert_nichts`
- `tests/test_bericht.py::test_textbericht_zeilen`

Container: **biotop-4f7d98c6e56f**, **biotop-3021f1723b4e** (62), **biotop-a28e9df1fb0c**, **biotop-364d23e72acc** (63). Die genaue vorhergehende Ausnahme bleibt **offen**: `kammer.py:82` begrenzt stderr auf die letzten 20000 Zeichen; der Anfang der Fehlermeldung ist abgeschnitten. Daraus wird weder eine bestimmte Fixtureursache noch ein konkreter Werkfehler erfunden. F7 muss diese nicht vollständig ausgeführten Nachweise weiterhin ablehnen.

Aktuelle fehlgeschlagene Eigentests: `tests/test_eichproben.py:267` und `tests/test_review_vertrag.py:270`, identifiziert im JUnit von 62. Die CLI von 63 hat leere stdout und stderr `ABBRUCH: Vorspann Lauf 26: proben: nicht genau vier ausgeführte, prüfbare Kontrollen mit Sollurteil True …`. Gespeichert sind `status=gescheitert`, `nachweis_sha256=null`, `gen0_nachweis_verwendbar=false`.

**Nicht verwechseln:** Die sichere Verweigerung ist kein Fehler des Gates, aber auch kein funktionierender erfolgreicher Pflichtvorspann. Die erfolgreiche aktuelle reale Route bis zur Gen0-Eingangsfreigabe fehlt. Erfolgreiche CLI-/Gate-Units ersetzen Messungen/Proben kontrolliert (`tests/test_vorspann.py:13–56`, `test_vorspann_cli.py:15–22`). Der Eingangscheck selbst steht vor der Gen0-Arbeit (`lauf.py:611`); die internen Gen0-Mechanismen sind nicht Prüfauftrag.

## KERN-02 – Einzeltestregression durch kollidierende IDs übersehen

**Bestätigter Logikfehler an der synthetischen Parser-/Entscheidergrenze.** `messgeraet.py:125,133` reduziert IDs auf Dateibasisname und Testname. Verschiedene Klassenmethoden `TestA.test_wert` und `TestB.test_wert` kollidieren. `pareto_f2` vergleicht diese Schlüssel anschließend als Mengen (`:359–367`).

Die Kontrolle führt den originalen Parser-AST und die reinen originalen Maßfunktionen aus, ohne Projektimport: Basisfehler in TestA.test_wert und TestC.test_alt; Kandidatenfehler neu in TestB.test_wert. Ergebnis **Kernmaß −2→−1, keine Pareto-Verschlechterung, ok=true**. Bei denselben Messzahlen mit eindeutigen Klassen-IDs erkennt derselbe Entscheider die neue Regression und liefert **ok=false**. Der vorhandene Testklassen-Eigentest überprüft nur eine einzelne Klasse, nicht diese Kollision.

Beleg: `UNIT-GRENZE.json` samt synthetischen Eingabe-XMLs. **Kein echter JUnit-, pytest-, Werk- oder Kammerlauf** und keine Behauptung, dass dieser Fall bereits im Elternbestand auftrat.

## KERN-03 – testinterne Ausnahme wird zum Werkabsturz

**Bestätigter Klassifikationsfehler an der synthetischen Verbrauchergrenze.** `fundpruefung.py:75–77` prüft nur die Wörter `Error`/`Exception` und das Fehlen von `AssertionError`, nicht den Fehlerort. Ein ausschließlich aus `tests/test_neubewertung_probe.py` stammender `NameError` ergibt im originalen `_ausfuehren` dennoch `absturz_im_werk=true`.

`bewerten` kann damit ohne Vertragsbezug `offen_norm` zu `offen` aufwerten (`:95–111`); dieser Leser liegt direkt im Pflichtvorspann (`vorspann.py:157`). Die falsche Flag-Ausgabe ist separat ausgeführt, die Statusfolge statisch belegt. Kein echter Fund wurde verändert; eine solche reale Eltern-Umstufung wird **nicht** behauptet. Die synthetische I/O-Grenze ist in `UNIT-GRENZE.json` ausdrücklich ausgewiesen. Aus bloßer Ausnahme wird hier unzulässig eine konkrete Fehlursache abgeleitet.

## Sicherheits- und Leserbewertung

Keine bestätigte Sicherheitslücke aus den zwei Regexverdachten: `exec` transportiert das konstante Messskript in die Kammer; `eval('1')` ist die absichtliche Bandit-Testfixture. Das ist keine allgemeine Sicherheitsfreigabe.

Gelesene direkte Verbraucher: Messung/Kernmaß/Pareto, Aegis-JUnit und Paarurteil, `_einzelprobe`/`_vollstaendig`, Fundprüfung, `lauf._verhandeln`-Maßleser, Vorspann-Qualität/Versiegelung, CLI und Gen0-Eingang. Fehlende Maßpflichtlisten werden in der Verhandlung nicht mehr durch leere Defaults zu Erfolg. Aus den geprüften Fällen wird kein lückenloses F7-Zertifikat für beliebige Programme abgeleitet.

## Abgrenzung, Verbrauch, Lieferung

Werkaufnahme, Gen0-interner Mutantenbau, Legacy-Prüfskriptreparaturen und P4-01 bis P4-04 bleiben ausdrücklich außerhalb. Die vier dokumentierten P4-Lücken werden weder geschlossen noch als neue Reparaturpflicht eröffnet.

Eigene neue Kammerläufe **0**, Werk-/DB-Starts **0**, externe Modell-/Anbieter-/Netz-API-Aufrufe **0**, entsprechende eigene externe API-Kosten **0 €**. **Träger-/Reviewmodell-/Hostkosten nicht gemessen**, keine Nullbehauptung. Für 63 stimmen die gebuchten **83 Kammern** mit den Rohkennungen überein: Rauschen 5, Fundprüfung 39, Ausgang 1, Batterie 38. Eltern-Modellbuchungen in 63: leere Liste; die Batterien melden jeweils 0 Modellaufrufe und 0 Modellkosten. Keine Umdeutung zu kostenlosen Trägerkosten.

Ein Prüflauf `python3 -B /root/reparatur-01/review-03/pruefer/PRUEFUNG.py` endete **Exit 0** und hat Rohzähler, Quellintegrität und die zwei explizit synthetischen Logikbefunde bestätigt. Exit 0 dieses Prüfskripts bedeutet **nicht** Produktabnahme. Hilfsabfragen hatten zuvor einen deduplizierten Dateilese-/KeyError und einen Syntaxfehler; beide führten zu keiner Produktaktion und wurden nicht als Belege verwendet.

Artefakte und vollständige Adressen stehen in `DATEIEN.txt`, Prüfsummen in `SHA256SUMS` (ohne Selbsthash). Keine Implementierung, keine Auto-Fixes, keine dritte Reparaturrunde. **An Parent zur Eskalation zurückgegeben; keine Abschlussfreigabe.**
