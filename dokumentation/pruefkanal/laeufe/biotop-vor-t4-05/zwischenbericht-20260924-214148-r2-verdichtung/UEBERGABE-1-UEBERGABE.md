# Übergabe: Behebungsrunde 5 vor T4 (begonnen 2026-09-24 ~17:05)

## Auftrag (Philipp, 24.09., Entscheidungen Chat-Claude zum Review 04; „Runde 5 schließt Klassen, nicht Fälle“)
1. **Vollständigkeitsprüfung:** nach jedem Erfassen eines Objekts prüfen, ob alle Datenattribute erfasst sind; fehlt
   eines → gezählte Enthaltung, nie „0 Abweichungen, tragfähig“. Gegenproben: Review-04 Nr. 2 (Slots-Vererbung), 3
   (verschleierte Slots), 5 (Iterator-Objekt-Elemente, Kappe), 10 (Path). os.PathLike über os.fspath als Wert.
2. **Festhalten = fallende Zusicherung**, keine beliebige Ausnahme (Nr. 1, Probe x3).
3. **Sondenausfall trifft nur die betroffene Funktion** — ihre Beobachtungen enthalten sich, der Lauf geht weiter (Nr. 4);
   ersetzt werden nur echte Iteratoren, keine Objekte mit Attributen (csv.DictReader).
4. **Kappe der Verfälschungsläufe:** zurückstellen mit Grund, gezählt; gemessen an einem Kandidaten in T4-Größe (Nr. 6).
5. **Verdrahtung über ein Register:** jede Funktion, deren Aufruf der Entwurf verlangt (Organe, Torzeilen, Tor-4-Skript)
   steht im Register; der Verdrahtungstest verlangt jeden Eintrag im echten Lauf. Tor-4-Skript bauen, ruft Torzeile
   „Schwächen“ (Nr. 7). T4: Normalvergleich einer Altlast = Verhalten der Vorgeneration über den Verhaltensvergleich;
   eine verhaltensändernde Altlast braucht einen unabhängigen Test aus der Altlastenliste.
6. **Vorspann verweigert ohne Stufe 2**, Test mit gestellter Dauer > 60 s (Nr. 8); Stufe-2-Lasten wie Stufe 1 bemessen und
   geeicht, bis `eingang` nicht mehr sperrt.
7. **Lastaufrufe tragen die Formmerkmale ihrer Eingabe** (Nr. 9).
8. Niedrige: dieselbe Stufe für Eichproben, Toleranz, gespeicherte Maße (Nr. 14, 15); Ausschluss eigener Tests nach
   Testkennung inkl. Parametrisierung (Nr. 16); Nachspiel als echter Durchlauf in der Regression (Nr. 18).
Kein Lauf, kein Modellgeld, ein Review, eigener Commit, laeufe/biotop-vor-t4-05/, Endmeldung (Abholadresse ganze Zeile +
Prüfsumme). Übergabe nach JEDEM abgeschlossenen Schritt nachführen.

## Ausgang
- HEAD `43b8fad` (Runde 4 + Nachtrag), Arbeitsbaum sauber; Regression dort 569/2/0 (REGRESSION-2.txt, Runde 4).
- Review 04: /root/biotop-vor-t4-04/REVIEW.md (18 Befunde), Proben /tmp/review-vor-t4-04/ (kammerprobe.py, x4probe.py …).
- **Runde 4 war NICHT veröffentlicht** (BERICHT mit Platzhaltern; im Kanal nur Zwischenberichte). Schritt 0 unten.

## Plan (Reihenfolge)
0. Runde 4 abschließen: Review-Proben nach biotop-vor-t4-04/review-proben/, SPEZIFIKATIONEN (Review-Befunde → R5), BERICHT
   füllen (Skript, Sperrwortlaut nur aus Belegdatei), veroeffentlichen.py ergänzen, ausführen.
1. Code lesen (gezielt), Tor-4-Abschnitt Masterprompt v8.
2. Rote Spezifikationen an 43b8fad (tests/test_vor_t4_05.py) aus den Review-Proben.
3. Bau je Entscheidung als alles-oder-nichts-Patchskript unter bau/ (r5_*.py).
4. Stufe-2-Eichung eingang (Messskript proben/), T4-großer Kandidat (proben/).
5. Teilläufe inkl. Wächter-Tests → Kette: Commit → Regression → Nachspiele (K2904/K3091 ×3, K2868) → Vorher/Nachher.
6. Ein Review (Subagent, REVIEW-AUFTRAG.md) → BERICHT → veröffentlichen → Endmeldung.

## Stand (neueste zuletzt)
- 17:05 Arbeitsordner angelegt. NÄCHSTES: Schritt 0.
- 17:20 Schritt 0 fertig: Runde 4 veröffentlicht (laeufe/biotop-vor-t4-04, 103 von 103 bytegleich, Ordnerprüfsumme
  c02d0dce9ad5996215f0d723a006a4ae2c0495ab2e051a7d0a4d73e7988c3f12, bau/VEROEFFENTLICHUNG-R4.txt). BERICHT 4 per Skript
  gefüllt (bau/r4_bericht_fuellen.py), SPEZIFIKATIONEN R5-1…R5-14, review-proben/ (13 Dateien). NÄCHSTES: Code lesen.
- 18:30 Gelesen (bau/LESEN4..9.txt); Masterprompt v8 Tor 4 aus state.db (bau/MASTERPROMPT-V8-TOR4.txt; die Cache-Datei
  existiert nicht mehr). Stufe-2-Eichung gemessen (proben/STUFE2-EICHUNG.*, an Kopie 43b8fad): eingang W 60 sperrt 3 von 8
  Rauschmessungen, W 240 0 von 8, W 480 0 von 8; längster Kammerlauf 12,3 s bzw. 13,7 s → W 240. Vorproben: VORPROBE-E2
  (reprcrash: Werk-Ausnahme → Werkdatei, lokal und Kammer pytest 8.3.3), VORPROBE-ZUSTAND (object.__getstate__ zählt
  Slots/Dict/verschleiert).
- 18:55 Umbau am Arbeitsbaum (NICHT committet): bau/r5_bau.py (61 Ersetzungen, 10 Dateien, bau/R5-BAU.txt) +
  bau/r5_bau2.py (4 Ersetzungen: Eingrenzung per os.fork aus unberührtem Zustand — eigener Befund: Wiederholungslauf im
  selben Prozess erbt Modulzustand; pack/unpack mit Slots; tor4-Wache). Neu: biotop/tor4.py, biotop/kern/register.py.
  py_compile/node --check ok (bau/NACH-BAU.txt). NÄCHSTES: drahtwerk Stufe 2 + Altlasten, test_verdrahtung (Register,
  tor4, Nachspiel), tests/test_vor_t4_05.py (rote Spezifikationen), Teilläufe.
- 19:40 Weitere Bauschritte (je alles-oder-nichts, Protokoll bau/R5-*.txt): r5_tests1 (drahtwerk Stufe 2 + ALTLASTEN,
  test_verdrahtung Register/tor4), r5_bau3 (Eingrenzung per Halbierung, Nachspiel nimmt Stufe-2-Rauschen aus Nachweis,
  kan deque/object), r5_bau4 (drahtwerk Stufe 2 nur alpha zehnfach; Nachspiel-Durchlauf im Verdrahtungstest; TS-Kanon
  Vollständigkeitsprüfung), r5_bau5 (ITER_KAPPE 50→1000 — Befund TEILLAUF-1: der eigene Randkorpus (Zahl 100) riss die
  Kappe an linearen Generatoren → Sonde enthielt sich selbst). NEU tests/test_vor_t4_05.py (27 Fälle).
  TEILLAUF-1 (nur test_vor_t4_05, VOR bau4/bau5): 25 grün, 2 rot (K4[24], E8[exakt]: Kappe-Enthaltung an zahlen).
  TEILLAUF-2 läuft (alle Testdateien außer test_verdrahtung, am Arbeitsbaum). NÄCHSTES: Ergebnis lesen, Befunde
  beheben; dann Verdrahtungstest einzeln; T4-Größen-Messung (Entscheidung 4); REVIEW-AUFTRAG, BERICHT-Gerüst, Kette.
- 19:50 TEILLAUF-2 (alle Testdateien außer test_verdrahtung, 594 Fälle): 591 grün, 2 übersprungen, 1 rot —
  test_v1_iterator_kappe_nie_tragfaehig (eigener Testfehler: mit ITER_KAPPE 1000 sah die Sonde die Änderung ab Element
  60 und lehnte ab statt sich zu enthalten; Test auf Änderung ab 1.100 umgestellt). job_kette.sh LÄUFT (JOB-KETTE.txt):
  Teillauf 3 (Verdrahtung + 05/04/python_annahmen/vorspann) → Vorprobe K2904 am Arbeitsbaum → Commit → Regression →
  Nachspiele N1–N3 → Vorher/Nachher (proben/vorher_nachher.py) → T4-Größe (proben/t4_groesse.py).
  NÄCHSTES: während der Kette REVIEW-AUFTRAG.md, BERICHT-Gerüst, KASSE.md; nach der Kette auswerten, Review starten.
- 20:20 REVIEW-AUFTRAG.md, KASSE.md (Platzhalter), auswertung.py geschrieben. TEILLAUF-3a (test_verdrahtung am
  Arbeitsbaum): 6 von 6 grün in 1719 s — Register, tor4 und Nachspiel-Durchlauf im echten Lauf. TEILLAUF-3b läuft, dann
  Vorprobe K2904 → Commit. NÄCHSTES: nach dem Commit (JOB-KETTE.txt „commit-rc“) den Review-Subagenten starten (wartet
  mit Kammerläufen auf job_kette), BERICHT-Gerüst schreiben.
- 20:45 COMMIT 0c2f058 auf 43b8fad (TEILLAUF-3a 6/6 in 1719 s, TEILLAUF-3b 132/132, Vorprobe K2904 überlebt). Kette läuft
  weiter: Regression (Start 20:24) → Nachspiele N1–N3 → Vorher/Nachher → T4-Größe (t4_groesse.py vor dem Lauf korrigiert:
  bau/r5_t4_fix.py). BERICHT.md-Gerüst geschrieben (§0–§14, Platzhalter ‹ERGEBNIS› ‹T4› ‹REGRESSION› ‹NACHSPIEL›
  ‹VORHER_NACHHER› ‹REVIEW› ‹SPERREN› ‹OFFEN› ‹URTEIL›), KASSE.md (‹VERDRAHTUNG_KOSTEN› ‹NACHSPIEL_DB›). EIN Review
  gestartet (delegate deleg_b1c00361, schreibt REVIEW.md, wartet mit Kammerläufen auf job_kette). NÄCHSTES: nach Kette
  `python3 auswertung.py` → Platzhalter füllen (Skript) → Review-Befunde einarbeiten → SPEZIFIKATIONEN → veröffentlichen.
- 21:15 Hinweise Philipp (kein Eingriff in den Job): (1) Enthaltung des ganzen Vergleichs widerspricht Entscheidung 3 →
  rote Spezifikation R6-1 vor T4 (spez/test_spez_r6_unit.py: rot an 0c2f058, 2 Gegenproben grün, spez/SPEZ-R6-UNIT.txt;
  Laufweg-Fassung spez/test_spez_r6_laufweg.py — NACH job_kette einmal laufen lassen, Ergebnis in ‹R6_LAUFWEG›);
  (2) Stichprobendauer eingang Stufe 2: 35,1 / 170,5 / 317,1 ms bei W 60/240/480 (proben/STUFE2-EINGANG-DAUER.txt),
  Auftragsfehler im Bericht benannt, Offen Nr. 5; (3) R6-2: Tor-4-Skript berechnet jede aus der DB berechenbare Zeile
  (10 von 14), vor T4. BERICHT §1/§5/§6/§13/§14 ergänzt (bau/r5_bericht_hinweise.py); SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md
  (R6-1…R6-3 + ‹REVIEW_SPEZ›). Offen-Liste beim Füllen: 1 R6-1 (Bau vor T4), 2 R6-2, 3 TS-Proben E2/E3, 4 Normalvergleich
  streng, 5 Maß der Stufe-2-Last nach Dauer.
