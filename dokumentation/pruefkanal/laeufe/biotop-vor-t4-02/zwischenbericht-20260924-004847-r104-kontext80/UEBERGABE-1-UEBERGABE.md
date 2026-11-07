# Übergabe: Behebungsrunde 2 vor T4 (Stand 2026-09-24 ca. 00:30, Sitzung 20260923_194003_92313ee1)

## Auftrag (Philipp, 23.09., Entscheidungen Chat-Claude zu den fünf Fragen aus laeufe/biotop-vor-t4/)
(1) Weißraum gehört zur Tarifsprache, soweit die versiegelte Normalversion ihn rechnet → S1 an K2868 nicht sauber
    behoben; dasselbe an K3044 prüfen, Schwächenzählung Lauf 38 korrigieren. (2) Python-Sonde vor T4, Torzeile bleibt.
(3) Jeder Laufzeitriss einmal gepaart nachmessen, nur bestätigter lehnt ab. (4) Deckung je Abweichung. (5) Wächter je Turn.
Gegenproben durch den Laufweg: K2868 mit erweitertem Korpus abgelehnt; K2904/K3091 3 von 3 gleich; Python-Prüfwerk:
Zwischenspeicher-Fehler scheitert. Kein Lauf, kein Modellgeld, ein Review, eigener Commit auf 330b4ec,
Abschlussordner laeufe/biotop-vor-t4-02/, Endmeldung mit Abholadresse + Prüfsumme.

## Erledigt (gemessen)
- S1 (s1/S1-STAENDE.json): an K3044, Endstand 38, Endstand 37, K2868 je Marker 0 von 3, K-Korpus 0 Abweichungen
  bei 93.320 Fällen mit Wert; aber Zeilenumbruch: 12.206 von 16.166 abgewiesen, die Normalversion rechnet (Lauf 38:
  Tab ok, nur \n; Lauf 37: Tab und \n). → S1 in keinem Lauf sauber behoben: Lauf 38 3 von 5 = 60 % (statt 80 %,
  Schwelle ≥ 80 % nicht erreicht), Lauf 37 2 von 5 = 40 % (statt 60 %).
- Code (Arbeitsbaum, NICHT committet): kern/py/verhalten.py (Python-Sonde); kern/ts/{kanon,deckung,deck-setup,
  vitest.deck.config}.mjs, Formvarianten + Eingabe je Muster in verhalten-runner.mjs; organe/verhaltensvergleich.py
  (Python, Deckung je Abweichung über aufgezeichnete Eingabe+Ergebnis am Kandidaten); aegis.py (Deckung, Nachmessung);
  kern/messgeraet.py (fehlender Wert = ungültig, laufzeit_bestaetigen); lauf.py (Generalprobe Nachmessung);
  tests/conftest.py (fail statt skip); tests/speicherwerk.py, tests/test_vor_t4_02.py; geänderte ältere Tests:
  test_t3_verhaltensvergleich (3), test_eichproben (REF_PAAR), test_vorspann (Laufzeit gestellt),
  test_t3_python_annahmen (GEPRUEFT +2 Einträge für kern/py/verhalten.py).
- Voller Lauf am Arbeitsbaum ohne Verdrahtung (bau/ERSTLAUF-ALLE.txt): 11 rot → alle 11 behandelt (Ursachen in
  BERICHT-Entwurf). Teillauf danach: 1 rot (vier Paare, Vertragsprobe: Referenzlast rief bericht) → REF_PAAR geändert.

## Stand 00:45 (Runde ~101 von 150, Kontext 67,5 %)
- Commit **6243377** auf 330b4ec (19 Dateien). Job `job_commit_regression.sh` (proc_72cfe583df40) läuft: volle
  Regression → REGRESSION.txt/.junit.xml, dann Nachspiele d1 (s2_k2904 s2_k3091 k2868), d2, d3 (s2_*), dann
  py/python_laufzeit_teilausfall.py → py/PYTHON-LAUFZEIT-TEILAUSFALL.json.
- BERICHT.md: Abschnitte 1–4, 7, 9–12 geschrieben; offen ‹URTEIL› ‹STAT› ‹ERGEBNIS› ‹TEILAUSFALL› ‹K2868› ‹S2DREI›
  ‹PYZWISCHEN› ‹REGRESSION› ‹REVIEW›.
- Review: Auftrag REVIEW-AUFTRAG.md, Delegation gestartet (Ergebnis → REVIEW.md).
- Sperre ohne Image: sperre/OHNE-IMAGE.txt (4 von 4 rot, mit ts1 4 grün).

## Nächste Schritte
1. Nach Job-Ende: Platzhalter aus REGRESSION*, nachspiel-d1..3, py/PYTHON-LAUFZEIT-TEILAUSFALL.json füllen.
2. Nach Review: Befunde nachmessen, Tabelle §8 (Umgang), Code-Befunde → rote Spezifikationen (kein neuer Code).
3. veroeffentlichen.py aus /root/biotop-vor-t4/veroeffentlichen.py ableiten (BASIS laeufe/biotop-vor-t4-02), veröffentlichen.
4. Endmeldung: Urteil zuerst, BERICHT.md- und DATEIEN.txt-URL je als ganze Zeile, Ordnerprüfsumme.
