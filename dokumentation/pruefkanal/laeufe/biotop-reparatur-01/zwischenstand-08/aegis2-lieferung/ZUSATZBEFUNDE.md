# Ergänzung innerhalb Nachbesserung 02 / Fassung 7

**Reproduziert, Eigentümer dieser Lieferung:**

- `aegis.junit_lauf`: realer Docker-Exit 7 bzw. Timeout 124 nach erzeugtem grünem JUnit wurde als `ok=True` gewertet. `laeufe/04-rot-rest-junit` und `06-rot-abbruchmatrix`: direkte Fehlerassertions.
- Zusätzlich innerer pytest-Abbruch `os._exit(7)` in `pytest_sessionfinish` nach geschriebener JUnit-Datei: äußerer Lauf maskierte den Code als 0, Parser meldete Erfolg. `laeufe/05-rot-innerer-abbruch`: direkt rot; Parser/Treiberkorrektur inzwischen grün in `07-gruen-abbruch-rot-norm`.
- `_einzelprobe(..., name='norm', gegenprobe=True)`: Vorher-/Nachher-JUnit mit skip, xfail oder entferntem benannten Normtest; spätere echte Messung ist gültig, weil die Norm-Gegenprobe ohne Normtest misst. Die Originalzeile gibt trotzdem `pruefbar=True, bestanden=False`. `laeufe/07-gruen-abbruch-rot-norm`: drei neue Rotfälle, echte Passroute bleibt grün. Minimaler Pflichtpaarcheck in Eichproben anschließend grün in `laeufe/08-gruen-eigentuemer`, inklusive Qualitätsverbraucher und erfolgreicher Gegenroute.

**Zusammenspiel mit zweitem Arbeiter / Parent-Inventar, keine dortige Änderung:**

- `aegis.py:722-728` (Stand nach Parserergänzung; Verschiebung möglich) übernimmt Testdateien/Immuntests und Vertragsdateien allein aufgrund ihrer Abwesenheit aus `mess['werk']['tests_fehlgeschlagen_liste']`. Die vorgeschaltete `mess['gueltig']`-Kontrolle muss deshalb auch nicht ausgeführte bzw. fehlende erwartete Testdateien sperren. Nur ein global nichtleeres JUnit genügt nicht, wenn eine Pflichtdatei leer bleibt, während eine andere besteht. **Lesebefund, hier noch kein separater Annahme-Repro, kein eigenmächtiger Schnittstellenwechsel.** Bitte mit dem Messgeräteigentümer abgleichen.
- Zweite Skip-Parserstelle sowie fehlendes/leeres Mess-JUnit und Messung mit `rc!=0` gehören laut Parent zum zweiten Arbeiter; hier nicht geändert.
- Kein Bezug zur Rückholung der vier ausdrücklich offenen Phase-4-Mechanismen.
