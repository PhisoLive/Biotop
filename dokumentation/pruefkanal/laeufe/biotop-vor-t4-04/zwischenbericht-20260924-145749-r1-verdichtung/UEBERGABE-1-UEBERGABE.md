# Übergabe: Behebungsrunde 4 vor T4 (begonnen 2026-09-24 ~09:25, Sitzung 20260923_194003_92313ee1)

## Auftrag (Philipp, 24.09., Entscheidungen Chat-Claude zu den sechs offenen Punkten aus laeufe/biotop-vor-t4-03 §14)
1. Vergleichslast: zweite Stufe mit zehnfacher Eingabegröße je Bereich, ein Kammerlauf < 1 min; an ihr misst die Nische
   „schnell" den Gewinn und jede Nische ihre Laufzeitgrenze. Gegenprobe im Nachspiel: K2904 und K3091 3 von 3 gleich.
   T3s Ergebnisse bleiben unverändert.
2. Die vier hohen Review-Befunde vor T4 (R4-1…R4-4); jede Formvariante der Sonde = eigenes Merkmal (Weißraum je Zeichen).
3. Merkmale nicht veränderter Argumente gehören nicht zum Muster. Gegenprobe: Abweichungen bei ungültigen Eingaben von
   K2868 gedeckt, Weißraum-Muster ungedeckt.
4. Vom Kandidaten mitgebrachte Tests decken nicht; decken dürfen Tests der Vorgeneration, aus Generation 0, vom Ankläger
   und die versiegelten Gegenzeugen. Gegenprobe: Kandidat mit Rückschritt + eigenem Test, der genau ihn zusichert → abgelehnt.
5. TS-Methoden vor T5 (nicht vor T4) → Liste. Doppelte Gegenzeugen-Prüfung verbindlich in der Torzeile „Schwächen",
   nicht im Annahmepfad.
6. Fehlalarm des Sicherheitsfilters als sachlicher Text (Befehlsmuster + Sperrwortlaut, ohne Projektinterna) in den
   Abschlussordner; Einreichung entscheidet Philipp.
+ aus R4-1…R4-20 alles, was T4 gefährden würde; der Rest mit Begründung auf die Liste.
+ Übergabe nach JEDEM abgeschlossenen Schritt nachführen (Zwischenberichte!).
Kein Lauf, kein Modellgeld, ein Review, eigener Commit, laeufe/biotop-vor-t4-04/, Endmeldung (Abholadresse ganze Zeile + Prüfsumme).

## Ausgang
- Kern-Commit 0aac612 (Code = d54bf2f), Arbeitsbaum sauber; Regression dort 533/2/0.
- Vorrunde: /root/biotop-vor-t4-03/ (BERICHT, REVIEW, SPEZIFIKATIONEN R4-1…R4-20, review-proben/).
- Lehre: ein Schritt je Befehl; Sperrwortlaut nur aus Belegdateien übernehmen (Skill audit-channel-delivery).

## Stand (neueste zuletzt)
- Beginn: Arbeitsordner angelegt, auftrag.json → biotop-vor-t4-04.
- 13:24 Stufe 2 der Vergleichslast: biotop/kern/referenzlast/versandwerk-t3-02.stufe2.mjs (10× Eingabegröße, Werte
  im gültigen Bereich; erste Fassung warf RangeError → proben/STUFE2-ZEITEN-erste-fassung.*). Gemessen (proben/
  STUFE2-ZEITEN.txt): Kammerlauf Stufe 2 8,6–11,7 s (< 60 s); planung-Quote Stufe 1 ≈ 0,84–0,85, Stufe 2 ≈ 0,40–0,42
  (Gewinn skaliert mit der Eingabe). Eingebaut (bau/r4_stufe2.py, 22 Ersetzungen): lauf._referenzlast(stufe=2),
  vorspann Rauschmessung an Stufe 2 (eichung.laufzeit_einmal, Kammerlauf-Dauer, Grenze 60 s), aegis/lauf/nachspiel
  gepaart+Nachmessungen an Stufe 2 (referenzlast_laufzeit, tausch['_referenzlast_laufzeit']), laufzeit_stufe im Urteil.
- Sonde Python (bau/r4_sonde_py.py, 26 Ersetzungen): Merkmale je Formvariante (_text_merkmale), Muster nur aus
  veränderten Argumenten (_muster_von; Lastaufrufe []), Verfälschung je Merkmal + Fixture-Fehler≠fail, nur Generatoren/
  Standard-Iteratoren ersetzen (Iterator-Objekt gezählt), __slots__ (_felder/_felder_setzen), instanz_erproben
  (signatur_erprobt / signatur_ohne_inhalt), Koroutinen mit eigener Schleife, teilweise-Zähler.
- Sonde TS (bau/r4_sonde_ts.py, 12 Ersetzungen): textMerkmale, musterVon, Verfälschung je Merkmal, Hook-Fehler≠fail,
  nur Generatoren, teilweise.
- Deckung/Annahme (bau/r4_deckung.py, 26 Ersetzungen): _merkmal_treffer mit haelt je Merkmal, Bedarf (f,art,merkmal),
  VERFAELSCHUNG_KAPPE 24 (gezählt), klassen_je_test im Beleg, instabile Funktionen nicht beobachtet, teilweise im Urteil;
  aegis.eigene_tests (Entscheidung 4: neue/geänderte Tests des Kandidaten decken nicht); gewinne_beschraenken (R4-8);
  Kommentare (R4-10); Generalprobe nur bestätigte Gewinne.
- NICHT committet (HEAD 0aac612). NÄCHSTES: Tests anpassen/neu (tests/test_vor_t4_04.py: 4 hohe Befunde je Probe+Kontrolle
  aus review-proben 03, Entscheidungen 1–4 Gegenproben, R4-9 ungültige Gewinn-Nachmessung, R4-11 Verdrahtung), Teilläufe,
  Torzeile Schwächen (pruefung/torzeile_schwaechen.py + kern/gegenzeugen), Fehlalarm-Text, Kette→Commit/Regression/Nachspiele.
- 13:32 Muster-Nachtrag (bau/r4_muster.py): Muster = eingeführte Formvarianten-Merkmale (FORM_MERKMALE), Randwerte ohne
  Merkmal — beide Sprachen. Tests: t3_verhaltensvergleich/vor_t4_02 auf haelt je Merkmal + 'tab' umgestellt; NEU
  tests/test_vor_t4_04.py (31 Tests: H1–H4, E3, E4, R4-5/6/8/9/13/14, Stufe 2) — TEILLAUF-1 läuft (proc_5bb5abf53b10).
  Nachspiel an Stufe 2 misst die Rauschtoleranz selbst an der Vorgeneration (bau/r4_nachspiel_torzeile.py);
  kern/gegenzeugen.torzeile_schwaechen (Entscheidung 5, verbindlich in der Torzeile). s1/torzeile_schwaechen_t3.py:
  T3 Lauf 38 nach doppelter Prüfung 0 von 5 (S1 Verhalten verändert; S2–S4 nicht beurteilbar: Normal-Vergleich
  für S2–S5 nie gemessen; S5 da) — nur Gegenzeuge 4 von 5. Das ist eine Feststellung, keine Neubewertung von T3.
- 13:35 TEILLAUF-1 (test_vor_t4_04, 28): 26/2 — r414 (instabil_fn als Name statt modul:funktion) und E4 (eigener Test ohne
  Normbezug kam nie in den Testbestand) → bau/r4_fix1.py; TEILLAUF-2 (r414+e4): 6/6 grün. Paritätstest Merkmale Py↔TS
  ergänzt. FEHLALARM-SICHERHEITSFILTER.md geschrieben (ohne Projektinterna). nachspiel/nachspiel_vor_t4_04.py (K2904,
  K3091, K2868; Stufe 2, Rauschmessung im Nachspiel an Stufe 2). TEILLAUF-3 (16 Dateien, breit, inkl. Wächter-Tests) läuft.
  NÄCHSTES: Befunde aus TEILLAUF-3 beheben; REVIEW-AUFTRAG/BERICHT/KASSE/COMMIT-NACHRICHT/job (Nachspiele D1–D3,
  Vorher/Nachher für H1–H4 an 0aac612, Torzeile) schreiben; dann Kette.
- 13:52 Geschrieben: proben/vorher_nachher.py (neue Fälle am Code 0aac612 und HEAD per git archive, Tests aus HEAD),
  job_commit_regression.sh (Commit → Regression → Nachspiele D1–D3 → Vorher/Nachher → Torzeile), COMMIT-NACHRICHT.txt,
  REVIEW-AUFTRAG.md. TEILLAUF-3 (16 Dateien) läuft noch (proc_26fcbdcdfef7), bisher 3 F im Bereich 20–41 %.
  NÄCHSTES: Fehlschläge aus TEILLAUF-3 lesen/beheben → kette.sh (TEILLAUF-4 gezielt → Job) → BERICHT/KASSE → Review.
- 14:01 TEILLAUF-3 (16 Dateien, 351 Fälle): 347 grün, 1 übersprungen, 3 rot — alle in test_vor_t4_03 Gruppe B (setzten ein
  gemeinsames Merkmal `weissraum` voraus; Entscheidung 2 macht Tab/LF/CRLF/NBSP eigen) → bau/r4_fix2_tests.py
  (Spezifikationsänderung mit Notiz je Stelle). Kette gestartet (bau/kette.sh: TEILLAUF-4 = test_vor_t4_03 -k test_b_ +
  ganze test_vor_t4_04 → bei grün job_commit_regression.sh). NÄCHSTES: während der Kette BERICHT-Gerüst + KASSE schreiben.
- 14:03 Kette: TEILLAUF-4 grün (4 von 4 — Achtung: -k "test_b_" galt für BEIDE Dateien, test_vor_t4_04 lief darin NICHT;
  voll grün war es in TEILLAUF-3; eigener Fehler, im Bericht nennen). Commit 1d9a5aa auf 0aac612; job_commit_regression.sh
  läuft (Regression → Nachspiele → Vorher/Nachher → Torzeile). FORMATSPERRE-1 (lesender Sammelbefehl) → gespeichertes Skript
  unverändert ausgeführt (Regel), Beleg sperre/FORMATSPERRE-1.txt + formatsperre-1-befehl.sh. KASSE.md mit Platzhaltern.
- 14:06 Probe R4-11 (proben/spion_gewinn.sh): ein vorhandener Test (test_vorspann generalprobe, nur_gesperrtes_rauschen)
  erreicht gewinn_bestaetigen in lauf._generation_koerper: 1 Aufruf, Ergebnis 'bestaetigt' (gestellte Laufzeit).
  Vorbereitet, NICHT angewandt (Job läuft auf dem Arbeitsbaum!): bau/r4_nachtrag_lastabbruch.py (R4-3 zweiter Teil:
  korpus:last_* = Fehler an der Vorgeneration → SondeAusgefallen; 2 Tests). NACH Job-Ende: anwenden, gezielt testen,
  Nachtrag-Commit + Regression-2, dann Review (REVIEW-AUFTRAG auf zwei Commits anpassen), BERICHT füllen, veröffentlichen.
- 14:09 Nachtrag vorbereitet: bau/r4_nachtrag.py (R4-3 zweiter Teil + 4 Torzeile-Tests), job_nachtrag.sh (Teillauf 5 →
  Nachtrag-Commit → Regression-2 → Nachspiel D4), COMMIT-NACHRICHT-2.txt. bau/kette_nachtrag.sh wartet auf das Ende des
  Commit-Jobs und startet dann den Nachtrag (proc im Hintergrund). BERICHT.md Gerüst mit Platzhaltern (§1 geschrieben).
  NÄCHSTES: nach beiden Jobs BERICHT füllen (Nachspiele D1–D4, Vorher/Nachher, Regression 1+2, Torzeile), Review starten.
