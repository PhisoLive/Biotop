# Übergabe: Behebungsrunde 3 vor T4 (begonnen 2026-09-24 02:20, Sitzung 20260923_194003_92313ee1)

## Auftrag (Philipp, 24.09., Entscheidungen Chat-Claude zu den vier offenen Fragen aus laeufe/biotop-vor-t4-02/BERICHT.md §12)
Wortlaut steht in der Sitzung; Kern:
- (1) Deckung je MUSTER (Option 1). Gegenproben: K2868 scheitert am ungedeckten Weißraum-Muster; eine richtige Behebung
  mit einem Test je Muster kommt durch; K2868 einmal NUR mit erweitertem Korpus, einmal NUR mit neuer Deckungsregel.
- (2) Gewinnschwelle Nische schnell in beiden Richtungen nachmessen, nur innerhalb der Rauschtoleranz um die Schwelle;
  Gegenprobe K2904/K3091 3 von 3 gleich — kippt es trotzdem: melden (dann Größe der Vergleichslast).
- (3) Methoden von Klassen vor T4 beobachten, Instanzen aus den Verträgen, Zustand von self vor/nach verglichen;
  Enthaltung nur für wirklich Unbeobachtbares, gezählt.
- (4) S1 NICHT neu versiegeln; für jedes künftige Testwerk prüft jeder Gegenzeuge zweierlei: Schwäche weg UND gültiges
  Verhalten gegen die Normalversion unverändert.
- Plus die 13 Spezifikationen aus /root/biotop-vor-t4-02/SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md, jede mit Gegenprobe
  durch den Laufweg; die fünf Lücken der Python-Sonde (Generator, in-place, nur-Fehler, Hash-Reihenfolge, lru_cache)
  je mit einem Fall, der vorher unentdeckt blieb oder Fehlalarm gab.
- Reviewer an dieselbe Regel gebunden: Sicherheitssperre → anhalten und melden, nie auf anderem Weg lesen.
- Kein Lauf, kein Modellgeld, ein Review, eigener Commit, Abschlussordner laeufe/biotop-vor-t4-03/, Endmeldung mit
  Abholadresse als ganze Zeile und Prüfsumme.

## Ausgang
- Kern-Commit 6243377 (Runde 2), Arbeitsbaum sauber. Regression dort 493/2/0.
- Arbeitsordner /root/biotop-vor-t4-03/ (bau/, spez/, proben/, nachspiel/, sperre/).
- Proben des Gutachtens Runde 2: /root/biotop-vor-t4-02/review-proben/ (sondenprobe.py, sondenprobe2.py).

## Stand
- 02:20 Beginn. Gateway neu gestartet (02:14:04); Verdichtung lief 02:14:47–02:15:47 erfolgreich (532→163 Nachrichten).
- 03:40 Kern umgebaut (NICHT committet, HEAD 6243377): kern/py/verhalten.py (Methoden/Eigenschaften, Instanzen aus
  Verträgen, >args-Zustand, Kopienprobe, Iterator, inhalt-Zählung, Hashsaat 0, Muster je Beobachtung, Deckung per
  Klassen + Verfälschung, Modus erreichbarkeit, korpus_erweitert-Schalter); organe/verhaltensvergleich.py neu (Deckung je
  Muster + Verfälschung + zustandsabhängig nicht deckbar, Vorgeneration 2× → instabil, x von y nur inhaltlich, Wurzel-
  module, Zeitlimit 2× = Inhalt, Aufzeichner blind = Ausfall, erreicht(), Aufschlüsselung, deckungsregel-Schalter);
  kern/ts: einwickeln.mjs NEU (AST, export const), kanon.mjs klassenVon, verhalten-runner.mjs (Muster, >args, Kopien,
  Iterator, inhalt), deck-setup.mjs (Klassen, Verfälschung), vitest.deck.config.mjs (createRequire!);
  messgeraet: laufzeit_risse-Liste, gewinn_band/gewinn_bestaetigen; aegis: gewinn-Nachmessung, vv_optionen;
  lauf.py Generalprobe gewinn; eichproben: _vertragsziel (S-10); nachspiel: vv_optionen + Nachmessungen im Beleg.
- Rauchproben grün: bau/rauchprobe_sonde.py (Py), bau/rauchprobe_ts.py (TS).
- OFFEN: gewinn_bestaetigen bei Widerspruch → gepoolt entscheiden (statt unentschieden); Tests anpassen
  (test_t3_verhaltensvergleich deckung-Signatur, test_vor_t4_02 Deckung/args); neue tests/test_vor_t4_03.py (5 Lücken,
  Entscheidungen 1–4, S-1…S-12); Doppelprüfung Gegenzeuge (Entscheidung 4) als vv.gegen_normalversion + Skript;
  Commit + volle Regression + Nachspiele (K2868 getrennt, K2904/K3091 ×3, erzwungene Rissprobe); Review; Veröffentlichung.
