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

## Stand 01:15 (Kontext > 80 %, Verdichtung scheitert im Gateway — 401 widerrufen; Neustart von außen nötig)
- Commit 6243377, volle Regression 493/2/0, Verdrahtung grün. Nachspiele d1–d3 am Commit: K2868 abgelehnt (40 von 40
  ungedeckt, ~form); K2904 3 von 3 überlebt; K3091 2 von 3 (d3 an Gewinnschwelle −13,7 % abgelehnt) → Gegenprobe
  „3 von 3 gleich“ GESCHEITERT → rote Spezifikation spez/test_spez_gewinnschwelle_nachmessung.py (an 6243377 rot).
- BERICHT.md fertig bis auf ‹REVIEW› (§8). Urteil: nicht abgenommen.
- Review läuft (deleg_ce891021 → REVIEW.md).

## Nächste Schritte (fresh session: nur diese)
1. REVIEW.md lesen; §8 als Tabelle Nr | Schwere | Befund | Umgang (Code-Befunde → rote Spezifikation, kein neuer Code).
2. `cd /root/biotop-vor-t4-02 && python3 veroeffentlichen.py` (bricht ab bei Platzhaltern; Ziel enthält nur
   zwischenbericht-*-Ordner).
3. Endmeldung: „nicht abgenommen …“, BERICHT.md- und DATEIEN.txt-URL je ganze Zeile, PRUEFSUMME-ORDNER, dazu der Satz
   an Philipp: Gateway-Neustart von außen, weil die Verdichtung am widerrufenen Token scheitert (Wortlaut BERICHT §0).
