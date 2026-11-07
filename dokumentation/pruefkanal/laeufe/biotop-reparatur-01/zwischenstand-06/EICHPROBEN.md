# Vier echte Eichpaare nach EICH-4

Quelle: ausgaben/49-vorspann-kernabschluss.json, Nachweisergebnis.eichproben; Kammer-Rohbelege daneben. Eingeschleuste mechanische Kontrollen am kopierten echten Bestandswerk, keine natürlichen Modellkandidaten.

## nebenwirkung
proben: ausgeführt=True, prüfbar=True, Bestehensprädikat=True; 2 gezählte Kammern.
Vertrag verletzt (Schritt 2): test_vertrag_bericht_lager.py::test_artikel_sortiert_nur_positiver_bestand, test_vertrag_bericht_lager.py::test_bestand_nie_negativ_entnahme_ganz_oder_gar_nicht, test_vertrag_bericht_lager.py::test_eingeloeste_reservierung_zaehlt_nicht_weiter, test_vertrag_bericht_lager.py::test_journal_fortlaufend_und_unveraenderlich, test_vertrag_bericht_lager.py::test_verfuegbar_ist_bestand_minus_reserviert
gegenproben: ausgeführt=True, prüfbar=True, Bestehensprädikat=False; 2 gezählte Kammern.
Kernmaß -6 → 0 (+6): bericht.tests_fehlgeschlagen: 6 → 0

## regression
proben: ausgeführt=True, prüfbar=True, Bestehensprädikat=True; 7 gezählte Kammern.
Vertrag verletzt (Schritt 2): test_vertrag_bericht_lager.py::test_artikel_sortiert_nur_positiver_bestand, test_vertrag_bericht_lager.py::test_bestand_nie_negativ_entnahme_ganz_oder_gar_nicht, test_vertrag_bericht_lager.py::test_eingeloeste_reservierung_zaehlt_nicht_weiter, test_vertrag_bericht_lager.py::test_journal_fortlaufend_und_unveraenderlich, test_vertrag_bericht_lager.py::test_verfuegbar_ist_bestand_minus_reserviert
gegenproben: ausgeführt=True, prüfbar=True, Bestehensprädikat=False; 7 gezählte Kammern.
Kernmaß -6 → 0 (+6): bericht.tests_fehlgeschlagen: 6 → 0

## norm
proben: ausgeführt=True, prüfbar=True, Bestehensprädikat=True; 8 gezählte Kammern.
Kernmaß unverändert (-20 → -20); bestandene Tests zählen nicht
Normklassifikation=["test_lager_eichprobe_norm"]; mass.zuwachs=0; Test aufgenommen=False.
gegenproben: ausgeführt=True, prüfbar=True, Bestehensprädikat=False; 4 gezählte Kammern.
Kernmaß unverändert (-20 → -20); bestandene Tests zählen nicht
Normklassifikation=[]; mass.zuwachs=0; Test aufgenommen=False.

## vertrag
proben: ausgeführt=True, prüfbar=True, Bestehensprädikat=True; 4 gezählte Kammern.
Vertrag verletzt (Schritt 2): test_vertrag_bericht_lager.py::test_eichprobe_vertrag_neue_zusicherung
Benannter Vertrag: tests/vertraege/test_vertrag_bericht_lager.py::test_eichprobe_vertrag_neue_zusicherung
Direkter Vertragszeuge: {"bestaetigt": true, "meldung": "AttributeError: module 'lagerhaus.lager' has no attribute 'eichprobe_zusicherung'", "ok": false, "ort": "lagerhaus/bericht/auswertung.py"}
Direkter Verbraucherzeuge: {"bestaetigt": true, "meldung": "AttributeError: module 'lagerhaus.lager' has no attribute 'eichprobe_zusicherung'", "ok": false, "ort": "lagerhaus/bericht/auswertung.py"}
gegenproben: ausgeführt=True, prüfbar=True, Bestehensprädikat=False; 4 gezählte Kammern.
Kernmaß unverändert (0 → 0); bestandene Tests zählen nicht
Benannter Vertrag: tests/vertraege/test_vertrag_bericht_lager.py::test_eichprobe_vertrag_neue_zusicherung
Direkter Vertragszeuge: {"bestaetigt": false, "meldung": "", "ok": true}
Direkter Verbraucherzeuge: {"bestaetigt": false, "meldung": "", "ok": true}

## Gültigkeitsgrenze
Vier positive Treffer und vier falsche Gegenprädikate, sämtliche Fälle ausgeführt und prüfbar. Die Vertragsgegenprobe besteht jetzt den konkret benannten Vertrag und den Verbraucher; sie ist nicht bloß durch irgendeinen anderen falschen Teil des Aggregats falsch. Dass das Gesamturteil mangels Kernmaßgewinn ablehnt, ersetzt oder schwächt diese konkrete Vertragsaussage nicht.
Die vorherigen Test-eigenen NameError-Fälle bleiben als gescheiterte Entwicklungstests dokumentiert (46 rot,47 grün); sie werden nicht zu den gültigen Gegenproben gezählt.
