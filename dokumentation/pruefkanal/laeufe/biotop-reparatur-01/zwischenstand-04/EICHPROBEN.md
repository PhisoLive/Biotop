# Vier echte Probenpaare im integrierten Stand

Hauptbeleg: ../ausgaben/41-vorspann-echt.stdout.txt und ../ausgaben/41-vorspann-echt.json; volle Rohdaten/Kammerausgaben daneben. Eingeschleuste mechanische Eichfixtures an einer Kopie des echten Werks, keine natürlich generierten Kandidaten. Lauf26 existiert nur privat.

## nebenwirkung
Positiv: ausgeführt=True, prüfbar=True, Bestehensprädikat=True; Gegenprobe: ausgeführt=True, prüfbar=True, dasselbe Prädikat=False.

Positives Originalurteil: Vertrag verletzt (Schritt 2): test_vertrag_bericht_lager.py::test_artikel_sortiert_nur_positiver_bestand, test_vertrag_bericht_lager.py::test_bestand_nie_negativ_entnahme_ganz_oder_gar_nicht, test_vertrag_bericht_lager.py::test_eingeloeste_reservierung_zaehlt_nicht_weiter, test_vertrag_bericht_lager.py::test_journal_fortlaufend_und_unveraenderlich, test_vertrag_bericht_lager.py::test_verfuegbar_ist_bestand_minus_reserviert
Gegenfall-Originalurteil: Kernmaß -6 → 0 (+6): bericht.tests_fehlgeschlagen: 6 → 0

Gewinnbeleg: ['bericht.tests_fehlgeschlagen: 6 → 5']; Schadenbeleg: ['lager.tests_fehlgeschlagen: 0 → 27', 'Regression je Test (bestand an der Vorgeneration, fällt am Kandidaten): test_bericht.py::test_lagerwert_veraendert_nichts, test_lager.py::test_entnehmen, test_lager.py::test_entnehmen_genau_alles, test_lager.py::test_entnehmen_zu_viel_bucht_nichts, test_lager.py::test_freigeben, test_lager.py::test_inventur_und_gesamt …'].

## regression
Positiv: ausgeführt=True, prüfbar=True, Bestehensprädikat=True; Gegenprobe: ausgeführt=True, prüfbar=True, dasselbe Prädikat=False.

Positives Originalurteil: Vertrag verletzt (Schritt 2): test_vertrag_bericht_lager.py::test_artikel_sortiert_nur_positiver_bestand, test_vertrag_bericht_lager.py::test_bestand_nie_negativ_entnahme_ganz_oder_gar_nicht, test_vertrag_bericht_lager.py::test_eingeloeste_reservierung_zaehlt_nicht_weiter, test_vertrag_bericht_lager.py::test_journal_fortlaufend_und_unveraenderlich, test_vertrag_bericht_lager.py::test_verfuegbar_ist_bestand_minus_reserviert
Gegenfall-Originalurteil: Kernmaß -6 → 0 (+6): bericht.tests_fehlgeschlagen: 6 → 0

Gefallener Einzeltest: tests/test_lager.py::test_entnehmen. Zusatztests: ['tests/test_bericht_eichprobe_gruen.py::test_bericht_eichprobe_gruen_0', 'tests/test_bericht_eichprobe_gruen.py::test_bericht_eichprobe_gruen_1', 'tests/test_bericht_eichprobe_gruen.py::test_bericht_eichprobe_gruen_2']. Pareto nennt ihn: ['lager.tests_fehlgeschlagen: 0 → 27', 'Regression je Test (bestand an der Vorgeneration, fällt am Kandidaten): test_bericht.py::test_lagerwert_veraendert_nichts, test_lager.py::test_entnehmen, test_lager.py::test_entnehmen_genau_alles, test_lager.py::test_entnehmen_zu_viel_bucht_nichts, test_lager.py::test_freigeben, test_lager.py::test_inventur_und_gesamt …'].

## norm
Positiv: ausgeführt=True, prüfbar=True, Bestehensprädikat=True; Gegenprobe: ausgeführt=True, prüfbar=True, dasselbe Prädikat=False.

Positives Originalurteil: Kernmaß unverändert (-20 → -20); bestandene Tests zählen nicht
Gegenfall-Originalurteil: Kernmaß unverändert (-20 → -20); bestandene Tests zählen nicht

Positiv: norm=['test_lager_eichprobe_norm']; mass.zuwachs=0; offene Normeinträge=['norm_k2680_lager']; Normtest im tatsächlichen Werk=False.
Gegenfall: norm=[]; mass.zuwachs=0; offene Normeinträge=[]; Normtest im tatsächlichen Werk=False.
Beide Fälle besitzen ausdrücklich gemessenen Nullzuwachs. Nur der Positivfall erreicht die Normklassifikation und Nichtaufnahme; die leere Normliste im Gegenfall reicht nicht zum Bestehen.

## vertrag
Positiv: ausgeführt=True, prüfbar=True, Bestehensprädikat=True; Gegenprobe: ausgeführt=True, prüfbar=True, dasselbe Prädikat=False.

Positives Originalurteil: Vertrag verletzt (Schritt 2): test_vertrag_bericht_lager.py::test_eichprobe_vertrag_neue_zusicherung
Gegenfall-Originalurteil: Kernmaß unverändert (0 → 0); bestandene Tests zählen nicht

Konkreter Vertragstest: test_vertrag_bericht_lager.py::test_eichprobe_vertrag_neue_zusicherung; ausgeführter Verbraucher: tests/test_bericht.py::test_lagerwert_leer.

## Zählgrenzen
Vier von vier positive Treffer, vier von vier absichtlich falsche Gegenprädikate; acht von acht ausgeführt und prüfbar. Keine Infrastrukturverweigerung wird als Gegenbeleg gezählt. Ein Gegenfall darf dennoch aus einem anderen Grund insgesamt abgelehnt werden. Sämtliche Zeit-/Pareto-/Vertragsgründe bleiben erhalten.
Die isolierte Teilabnahme wurde in 39 und 40 erneut im Elternstand ausgeführt. Maßgeblich für den ganzen CLI-Vorspann ist 41 mit davor ausgeführter Rauschmessung und Fundneubewertung. Wiederholte Batterieausführungen sind keine zusätzlichen unterschiedlichen Eichproben.
