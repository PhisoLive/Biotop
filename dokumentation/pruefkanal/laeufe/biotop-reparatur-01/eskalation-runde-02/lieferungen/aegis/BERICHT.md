# Eigentümerlieferung — zweite und letzte Nachbesserungsrunde

**Eigentümerteil grün: 36 ausgeführte Tests, 0 Fehlschläge, 0 Fehler, 0 Skips.** Keine Integration, keine Commits, keine Gesamtabnahme des parallelen Kernfixes. Die abschließende Entscheidung bleibt beim Parent/Philipp.

## Repariert

1. **KERN-EICH4-SKIP:** `aegis.junit_lauf` erhält `<skipped>` einschließlich pytest-xfail als `ok=False`, `bestaetigt=False`, `uebersprungen=True` samt Grund. Der originale `_vertrag_pruefbar` lehnt den benannten unausgeführten Vertragszeugen dadurch ab. Die tatsächliche Passroute bleibt gültig.
2. **Fassung-7-Ergänzung, derselbe Kernleser:** Kammer-Timeout und nicht erfolgreicher Kammerabschluss sperren auch bei vorhandenem grünem Rest-JUnit. Zusätzlich wird ein abnormaler Exit des inneren pytest-Prozesses weitergegeben; der äußere Treiber kann ihn nicht mehr mit Exit 0 verdecken. Regulär abgeschlossene pytest-Läufe mit Testerfolg oder Testfehlschlag bleiben klassifizierbar.
3. **Weiterleitung in der Norm-Gegenprobe:** Eine spätere gültige Messung ohne Normtest ersetzte bislang das zuvor verlangte Vorher-/Nachher-Zeugenpaar. Reale skip-/xfail-/fehlend-Repros waren rot. `_einzelprobe` verlangt jetzt den bestätigten Vorher-Fehlschlag und den tatsächlichen Nachher-Erfolg des benannten Normtests. Die unveränderte erfolgreiche Gegenroute bleibt grün.

Keine Änderung an Kernmaßformeln, Pareto-Schwellen, Verträgen oder Messgerätequellen. Die vier Phase-4-Lücken bleiben offen: Wirkungskreis/transitive Folgen; Vertragsaustausch Vorspann→Freeze; NaN/Null-Rauschen; Gen0-Erfolgsbindung am Maß-Freeze.

## TDD und tatsächliche Rohbelege

Alle folgenden Angaben wurden aus JUnit, `execution.json` und `kammer.json` programmgesteuert abgeglichen; Zusammenfassung in `AUSWERTUNG.json`. Jeder Laufordner enthält vollständiges stdout/stderr, pytest-JUnit, Aufruf/Umgebung/Quellhashes sowie Kammer-Rohdaten. JUnit der inneren Kammer ist zusätzlich einzeln extrahiert, soweit erzeugt.

| Lauf unter `laeufe/` | pytest-Ergebnis | Kammerläufe | Aussage |
|---|---:|---:|---|
| `01-rot-skip` | 1 rot | 9 | Exaktes `_vertrag_pruefbar`-Assertion vor Produktänderung |
| `02-rot-xfail-pass` | 1 rot, 1 grün | 18 | xfail gleicher Defekt; echte Pass-/Qualitätsroute bereits grün |
| `03-gruen-fokussiert` | 24 grün | 69 | Erste Skipkorrektur; Bestand der Vertrags- und Kernmaßtests |
| `04-rot-rest-junit` | 2 rot, 5 grün | 6 | Echter Kammer-Exit/Timeout trotz grünem JUnit |
| `05-rot-innerer-abbruch` | 1 rot | 1 | Echter pytest-Abbruch nach JUnit-Erzeugung |
| `06-rot-abbruchmatrix` | 3 rot, 5 grün | 7 | Stabiler Abbruch-Treiber; saubere Route und fehlende/leere Belege bleiben korrekt |
| `07-gruen-abbruch-rot-norm` | 3 rot, 9 grün | 27 | Abbruchkorrektur grün; Norm-Zeugenlücke direkt rot |
| `08-gruen-eigentuemer` | **36 grün** | **96** | Vollständiger abschließender Eigentümerlauf |

Rot bedeutet jeweils eine fehlgeschlagene Soll-Assertion am beschriebenen Defekt, keine Sammlungspanne des Eigentests. Alte Belege wurden nicht umgeschrieben. Zwischenstände liegen zusätzlich unter `stand-03-gruen/` und `stand-07-rot-norm/`.

**Auffindbare Eigentests:**

- `tests/test_review_vertrag.py::test_test_eigener_fehler_ist_keine_pruefbare_vertragsgegenprobe[skip|xfail]`: originaler Vertragsbauer → echte Docker-JUnit → Originalparser → `_vertrag_pruefbar` → originale `_einzelprobe` → `_vollstaendig`/`_qualitaet`.
- `tests/test_review_vertrag.py::test_modulhelfer_und_konstanten_bleiben_im_eigenen_namensraum`: echte Vertrags-Passkontrolle und gültige Gegenroute; kein Immer-falsch-Fix.
- `tests/test_review_vertrag.py::test_normgegenprobe_braucht_ausgefuehrtes_zeugenpaar[skip|xfail|fehlend|pass]`: echte Norm-Gegenprobe samt Qualitätsverbraucher.
- `tests/test_junit_zeugen.py`: echter sauberer Kammerabschluss, äußerer Exitfehler, Timeout, innerer pytest-Abbruch; leeres JUnit, fehlende Testdatei, fehlendes JUnit, leere Anforderung. Letztere liefert keinen Erfolgszeugen und führt keine Kammer aus.
- Die vorhandenen 15 Kernmaß-/Paretofälle wurden unverändert ausgeführt, vor nachrangigen Tests.

**Beweisgrenze:** Die Organ-/Parser-/Maßpfade liefen an eigenen kleinen Fixtures in der vorhandenen Docker-Kammer, nicht an Maß-Doubles. Die Abbruchtests verändern ausschließlich den eigenen Testtreiber bzw. dessen Fixture-Hook; Ergebnis, rc und JUnit sind real, nicht gestellt. Die nachgeschaltete Qualitätskontrolle ist ausdrücklich eine Verbraucher-Unit-Prüfung aus sieben gestellten Flags plus einer realen Organzeile — keine frisch ausgeführte Gesamtbatterie aus vier Paaren. Dort beweisen sowohl Ablehnung als auch Annahme die Anschlussroute.

## Geänderte Quellen und Integrität

Vollständige Dateien liegen unter `dateien/`:

- `biotop/organe/aegis.py`: 12 hinzugefügte, 4 entfernte Zeilen.
- `biotop/organe/eichproben.py`: 7 hinzugefügte Zeilen.
- `tests/test_review_vertrag.py`: 73 hinzugefügte, 4 entfernte Zeilen.
- `tests/test_junit_zeugen.py`: neue Datei, 96 Zeilen.

`DATEIMANIFEST.json` enthält Größen, Zeilenzahlen und Vorher-/Nachher-SHA256. `AENDERUNGEN.diff` wurde mit `git apply --check` gegen isolierte Vorherdateien geprüft, Exit 0 (`DIFF-PRUEFUNG.json`). Kein Git-Commit oder Einspielen in ein Elternrepo.

Vergleich gegen `ELTERN-AUSGANG.json`: **123 andere Ausgangsdateien identisch** in SHA256, Größe und mtime_ns; genau drei vorhandene erlaubte Dateien geändert, genau eine erlaubte Datei hinzugefügt, keine entfernt. `START-VERGLEICH.json` und `QUELLEN-VERGLEICH.json` enthalten den Abgleich. Kein Reviewartefakt wurde ausgeführt oder geändert.

## Grenzen und offene Übergabe

- Der Bestandsfall `test_benannter_vertrag_am_kopierten_pruefwerk` wurde ausdrücklich **deselektiert, nicht als bestanden gerechnet**. Weder die freigegebene Bestands-DB/Werkkopie noch produktive DB/Werke wurden hier benötigt oder gelesen. Vollsuite, Bestands-/CLI-/Freigabeabnahme übernimmt der Parent.
- Messgerät und andere Leser gehören dem zweiten Arbeiter/Parent. Keine globale Suchvollständigkeit behauptet; tatsächlich gelesener bzw. ungeprüfter Umfang steht in `LESENUMFANG.json`.
- `ZUSATZBEFUNDE.md` benennt den Lesebefund am Aegis-Aufnahmepfad: Abwesenheit einer Testdatei aus der Fehlerliste ist allein kein Ausführungsbeleg. Abgleich mit dem Messgeräteigentümer erforderlich; hier kein separater Annahme-Repro, kein behaupteter Fix. Die 63 nichtproduktiv laufenden Prüfskripte wurden nicht repariert.
- `BESTAETIGT-OFFEN.json` grenzt eigene bestätigte Fälle und bloße Lesebefunde ab. Keine breite Zusatzreparatur und keine dritte Runde.

## Kosten und Kammerzählung

**233 tatsächliche Kammerläufe mit 233 eindeutigen Containerkennungen**, einschließlich aller roten Versuche und Wiederholungen; darunter 4 absichtlich ausgelöste Timeout-Kontrollen. Keine eigenen Container verblieben beim abschließenden Abgleich. Die 96 Kammern des letzten Laufs sind eine Teilmenge, keine zusätzlichen Kosten außerhalb dieses Nenners.

**0 Biotop-Modellaufrufe, 0 EUR Biotop-Modellbuchungen** in den 42 protokollierten privaten Organzeilen; keine bezahlten Biotop-/Netzaufrufe. Anbieterzugriff und Netzwerk waren im Prüfprozess gesperrt; Docker-Kammern liefen ohne Netz. Host-runpy war gesperrt. PYTHONDONTWRITEBYTECODE=1, PYTEST_DISABLE_PLUGIN_AUTOLOAD=1, explizites PYTHONPATH auf dieses Repo, TMPDIR außerhalb der rekursiv kopierten Fixtures.

Budgetvorgabe: 5 EUR gesamt, Biotop-Modelle 0. **Träger- und Host-/CPU-Kosten wurden nicht monetär gemessen.** Deshalb weder eine gemessene Gesamt-0 noch eine numerisch belegte Einhaltung des vollständigen 5-EUR-Budgets behauptet. Details: `KOSTEN.json`.

## Werkzeugprobleme ohne Produktwirkung

Ein erster Testpatch scheiterte atomar an einer nicht eindeutigen Stelle; kein Quellwrite daraus. Die erste Diff-Trockenprüfung scheiterte an fehlender Git-Metadatenzeile für die neue Datei (`DIFF-PRUEFUNG-01-FEHLER.json`); der korrigierte Lieferdiff ist geprüft. Die erwarteten roten pytest-Läufe und absichtlichen Abbrüche bleiben vollständig in der Kosten-/Belegzählung.

## Abholung

Lieferordner: `/root/reparatur-01/nachbesserung-02/lieferung/`

- Bericht: `/root/reparatur-01/nachbesserung-02/lieferung/BERICHT.md`
- Quellenmanifest: `/root/reparatur-01/nachbesserung-02/lieferung/DATEIMANIFEST.json`
- Artefaktindex: `/root/reparatur-01/nachbesserung-02/lieferung/DATEIEN.txt`
- SHA-Liste: `/root/reparatur-01/nachbesserung-02/lieferung/SHA256SUMS`
- SHA der SHA-Liste: `/root/reparatur-01/nachbesserung-02/lieferung/MANIFEST.sha256`
- Kosten: `/root/reparatur-01/nachbesserung-02/lieferung/KOSTEN.json`
