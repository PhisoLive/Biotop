# Übergabe: Behebungsrunde 2 vor T4 (Start 2026-09-23 ca. 22:50, Sitzung 20260923_194003_92313ee1)

## Auftrag (Philipp, 23.09., Entscheidungen Chat-Claude zu den fünf Fragen aus laeufe/biotop-vor-t4/)
(1) Weißraum gehört zur Tarifsprache, soweit die versiegelte Normalversion ihn rechnet → S1 an K2868 nicht sauber
    behoben (korrigiert T3-Befund; Prüfstein „K2868 muss bestehen“ war falsch). Dasselbe an K3044 (S1-Behebung Lauf 38)
    prüfen, Schwächenzählung Lauf 38 korrigieren, falls nötig.
(2) Python-Sonde vor T4, Torzeile bleibt (Grundsatz 11 für jede Sprache).
(3) Kein Wirkungskreis; jeder Laufzeitriss wird vor der Ablehnung einmal gepaart nachgemessen, nur ein bestätigter lehnt ab.
(4) Deckung je Abweichung (Grundsatz 11).   (5) Wächter je Turn (so gebaut).
Bauen: Python-Sonde im Umfang der TS-Sonde (einzeln, Folge, Alias, Mutation, Rücksetzung); Korpus aus den Verträgen mit
Randfällen UND Varianten der Eingabeform (TS und Python); Deckung je Abweichung; Bestätigungsmessung vor jeder
Laufzeitablehnung; gepaarte Messung mit fehlenden Werten ungültig (rote Spez spez/test_spez_laufzeit_gepaart_teilausfall.py
wird grün); die vier Gedächtnissperre-Tests ohne Kammerimage ROT statt übersprungen.
Gegenproben durch den Laufweg: K2868 mit erweitertem Korpus abgelehnt; K2904 und K3091 in 3 von 3 Durchgängen gleich;
an einem Python-Prüfwerk scheitert ein eingebauter Zwischenspeicher-Fehler.
Rahmen: kein Lauf, kein Modellgeld, ein Review, eigener Commit (auf 330b4ec), Abschlussordner laeufe/biotop-vor-t4-02/,
Endmeldung mit Abholadresse als ganze Zeile + Prüfsumme.

## Ausgang
- Repo /root/biotop, HEAD 330b4ec (Review-Befunde Runde 1), Arbeitsbaum sauber. Vorrunde: /root/biotop-vor-t4/
  (BERICHT.md, s1/ = S1-Harness für K2868, nachspiel_vor_t4.py, spez/, veroeffentlichen.py als Vorlage).
- Kammer: TS-Image biotop-kammer:ts1, Python-Image biotop-kammer:1. Nachspiele: NACHSPIEL_AUS=<ordner> python nachspiel_vor_t4.py <fall>.

## Stand
- (noch nichts gebaut)
