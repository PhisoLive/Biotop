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
- 2026-09-24 05:35 Neuer Turn nach Iterationsgrenze (Zwischenmeldung an Philipp ging raus, NICHT geliefert).
  TEILLAUF-1 (3 bestehende VV-Testdateien) 103/103 grün — Stand VOR der Musteränderung. TEILLAUF-2 (tests/test_vor_t4_03.py,
  30) 15 rot: Prüfwerk ohne Bereichsordner (Bandit) → behoben (probewerk/werk/kern.py). TEILLAUF-3 (A/B/D, 17) 8 rot:
  A1/A2/D fängt ein Werkstest über Pareto (Fälle so bauen, dass kein Werkstest sie sieht); B: neue Testdateien müssen
  tests/test_werk_… heißen (Verfassung); A2-Gegenprobe xs[:]=sorted(xs) weicht bei Tupel im Fehlertyp ab (echte
  Abweichung → Gegenprobe falsch gebaut, ersetzt durch xs.sort(key=…)).
- Musteränderung (ungetestet): Muster = Merkmalsklassen ALLER vereinheitlichten Argumente (py wickeln/korpus, ts runner),
  wie im Aufzeichner. Deckung je MERKMAL gebaut (_merkmal_treffer). Nächstes: Testfälle umbauen, Teilläufe, Gegenzeugen-
  Doppelprüfung (organe/gegenzeugen.py), S-10 prüfen, echte Rissprobe, Commit, Regression+Nachspiele, Review, Bericht.
- 05:56 TEILLAUF-4 (vor_t4_03 + 3 VV-Dateien, nach Musteränderung): 129 passed, 4 failed (nur Gruppe B: normieren
  hatte Werkstest → Pareto; behoben: Werkstest test_normieren entfernt, B-nebenbei mit quadrat nur bei x==1).
  Gebaut: organe/gegenzeugen.py (doppelurteil, s1_aus_messung) + Tests F; s1/gegenzeugen_doppelt.py → GEGENZEUGEN-DOPPELT.txt
  (normalversion behoben=True, ursprung False, k3044/endstand38/37/k2868 False; Siegel unverändert) — Bezug leerzeichen
  danach auf K.faelle korrigiert (Harness zählt neu_ungleich_norm über alle Fälle) → im Job am Commit neu.
  eichproben._vertragsziel: nur Funktionen mit Verbrauchertest; test_eichproben: REF_PAAR ruft bericht (Umweg zurück),
  kurzbericht + 2 S-10-Tests. test_verdrahtung: Nachmessungen im Beleg (S-9). nachspiel/nachspiel_vor_t4_03.py (K2868 2×2).
  proben/rissprobe_echt.py (echte Rissprobe). COMMIT-NACHRICHT.txt, job_commit_regression.sh (noch NICHT gestartet),
  REVIEW-AUFTRAG.md geschrieben. TEILLAUF-5 (vor_t4_03+eichproben+verdrahtung+vorspann) läuft: proc_e8e36638904d.
- 06:10 TEILLAUF-5 (vor_t4_03+eichproben+verdrahtung+vorspann): 117 passed, 11 failed, 1 skipped. Ursachen:
  (1) Gruppe B: neue Testdateien eines Kandidaten heben das Kernmaß nicht („bestandene Tests zählen nicht“) → B umgestellt:
  Soll-Tests stehen IM WERK (an der Vorgeneration rot), Kandidat ändert nur die Quelle (_anlegen(extra), werk_extra).
  (2) eichproben 4×: REF_PAAR ruft jetzt bericht, _lahmlegen(alle) setzte `return None` → Last bricht (s += None) →
  „angeforderter Laufzeitnachweis fehlt“ = genau der Messausfall, den Runde 2 umgangen hatte → _lahmlegen typtreu
  (0/0.0/''/[] nach Annotation). (3) S-10-Gegenprobe: RuntimeError propagiert aus _einzelprobe → Test prüft jetzt
  _vertragsziel direkt (raises + Kontrolle kurzbericht). (4) test_verdrahtung: organe/gegenzeugen.py nie im Lauf gerufen
  → verschoben nach biotop/kern/gegenzeugen.py (Prüfwerkzeug, kein Lauforgan).
  Kette gestartet: bau/kette.sh (TEILLAUF-6 → bei grün job_commit_regression.sh). Danach: Review (delegate), BERICHT, KASSE,
  veroeffentlichen.py (fertig vorbereitet, Nachspielbündel 10).
- 06:17 GEGENZEUGEN-DOPPELT (Arbeitsbaum, alte Bezugsgröße 117732): normalversion True, ursprung False, 4 T3-Stände False,
  Siegel unverändert. TEILLAUF-6 Teil 1 (B+F) 12/12 grün; Teil 2 (eichproben/verdrahtung/vorspann) läuft in kette.sh
  (proc_44c574fa96c6), danach automatisch job_commit_regression.sh (+ neu: proben/vorher_6243377.py = dieselben A/B/D-
  Fälle am Code von 6243377 aus git archive → „vorher unentdeckt/Fehlalarm“ gemessen). veroeffentlichen.py: Quellen ergänzt.
  NÄCHSTES nach Job-Ende: BERICHT.md + KASSE.md schreiben, dann EIN Review (delegate, REVIEW-AUFTRAG.md fertig), dann
  einarbeiten (kein Code), veröffentlichen, Endmeldung.
- 07:39 Commit-Job fertig: Commit d54bf2f auf 6243377; Regression 532/2/1 (rot: test_t3_python_annahmen, Register
  GEPRUEFT fehlte für verhalten.py::vertraege_ausfuehren/params). Nachspiele: K2904 3/3 überlebt, K3091 2/3 (D2 gepoolt 0,852
  abgelehnt) → Gegenprobe 2 von 3, gemeldet (Vergleichslast); K2868 2×2: Regel allein lehnt ab, Korpus allein nicht.
  Rissprobe echt: bestätigt/abgelehnt, Gegenprobe überlebt. Gegenzeugen am Commit wie erwartet. VORHER-6243377: 17 Fälle.
  Nachtrag: Commit 0aac612 (nur test_t3_python_annahmen.py), Job job_commit_regression_nachtrag.sh läuft (proc_14c8d44e5cbb:
  Regression-2 + proben/nachher_head.py → NACHHER-HEAD). BERICHT.md geschrieben (Platzhalter ‹URTEIL› ‹NACHHER› ‹N1…N5›
  ‹REG2› ‹REVIEW› ‹SPERREN›), KASSE.md fertig. REVIEW gestartet: deleg_37933da8 (ein Durchgang, REVIEW-AUFTRAG.md).
  NÄCHSTES: Job-Ende → Platzhalter REG2/NACHHER füllen; Review-Ende → Befunde einarbeiten (kein Code), Proben kopieren nach
  review-proben/, veroeffentlichen.py (Bündel 10 Nachspiele), HTTPS-Prüfung, Endmeldung mit Abholadresse + Prüfsumme.
- 08:01 Nachtrag-Job fertig: Regression-2 an 0aac612 533/2/0 (JUnit 535, 0 Fehlschläge), Verdrahtung grün; biotop/
  unverändert ggü. d54bf2f. NACHHER-HEAD: 17 von 17 Zusicherungen halten (vorher 1 von 17, 2 Abbrüche). BERICHT gefüllt bis
  auf ‹REVIEW› ‹SPERREN› (Urteil: nicht abgenommen). Review deleg_37933da8 läuft.
- 08:50 Review fertig: REVIEW.md, 18 Befunde (4 hoch, 5 mittel, 9 niedrig), keine Sperre beim Prüfer, Proben unter
  /tmp/review-vor-t4-03/. ZWEI SICHERHEITSSPERREN BEI MIR (Linie 3, nicht umgangen, beide wörtlich in sperre/):
  (1) terminal: Kopie der Gutachterproben nach review-proben/ + Lesen des tirith-Logs → nichts kopiert
  (SPERRE-KOPIE-GUTACHTERPROBEN.txt); (2) execute_code: BERICHT-Abschluss (§10/§11 füllen, Grenzen aus dem Review, S-10
  als Organ, SPEZIFIKATIONEN R4-1…R4-19, zwei Einträge in veroeffentlichen.py) → nichts geschrieben (geprüft: 2 Platzhalter,
  keine SPEZIFIKATIONEN-Datei); Abschrift bau/bericht_abschluss_gesperrt.py, NICHT ausgeführt (SPERRE-2-BERICHT-ABSCHLUSS.txt).
  WARTET AUF PHILIPP: Freigabe beider Handlungen. Danach: Abschrift unverändert ausführen, Kopie der Proben, dann
  veroeffentlichen.py, HTTPS-Prüfung, Endmeldung mit Abholadresse + Prüfsumme. laeufe/biotop-vor-t4-03/ NICHT veröffentlicht.
- 09:0x Freigabe Philipp (nur dieser Fall): Schritte getrennt ausgeführt, ohne weitere Sperre: mkdir review-proben; cp -p
  der 17 Gutachterdateien; cmp 17 von 17 gleich; Wächter nachgesehen (2 Zwischenberichte 05:11 r113 und 05:19 r141, je
  HTTPS 5 von 5, kein kontext80/verdichtung); bau/abschluss_1_bericht.py → BERICHT.md fertig (451 Zeilen, 0 Platzhalter,
  Sperrwortlaut aus sperre/ gelesen); SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md (R4-1…R4-20); veroeffentlichen.py Quellen +
  Zwischenbericht-Links. tirith-Log NICHT ausgezählt (Philipp: weglassen). Keine Codeänderung. NÄCHSTES: veroeffentlichen.py.
