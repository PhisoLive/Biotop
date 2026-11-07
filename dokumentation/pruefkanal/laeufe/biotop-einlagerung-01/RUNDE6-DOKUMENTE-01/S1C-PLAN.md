# S1c — Plan und Stand (fortlaufend)

Verbindlich: `BAU-S1C-UNBEOBACHTET.md`. Hintergrund: `bau/S1-UMSETZUNG.md`, `bau/S1B-PLAN.md` (M2(b)), `bau/S1-PLAN.md`.
Temp: `/tmp/r6-s1c` (TMPDIR), `T3_EICH_BELEGE=/tmp/r6-s1c/eichbelege`. Python `/root/biotop-t3/venv/bin/python`,
Tests aus `/root/biotop`. Kein Commit, kein Modellaufruf, kein Netz, keine Hintergrundprozesse, Aufrufe < 400 s.
Neue Dateien in `bau/` nur `S1C-`/`r6_s1c_`, exklusiv (`open(p, "x")`). `bau/hermes/` tabu.
Kammer-Sperre `/tmp/biotop-kammer-exklusiv` vor jedem Kammerstück prüfen.

Sperrregel: Wird ein Befehl gesperrt oder läuft eine Freigabeabfrage ab, wartet genau diese Handlung — nicht
umformulieren, nicht aufteilen, nicht als Skriptdatei neu schreiben, kein anderer Weg. Befehl + Meldung wörtlich hier.
Ausnahme Formatsperre: gespeichertes Skript unverändert ausführen, wenn reine Lese-/Testhandlung (wörtlich melden).
**Sperren bisher:** keine.

## Stand beim Start (12:52, gemessen)
- HEAD 0c2f058; `/tmp/biotop-kammer-exklusiv` existiert nicht.
- sha256: verhaltensvergleich.py `761b9a7c…`, verhalten.py `c4071c40…`, aegis.py `71af8ce7…`, test_vor_t4_06.py
  `80feee35…`, test_vor_t4_05.py `1983452f…`, test_vor_t4_04.py `788db3c6…`, test_vor_t4_03.py `9672cd54…`,
  test_vor_t4_02.py `de095406…`, test_t3_verhaltensvergleich.py `d6f239c4…`, test_t3_python_annahmen.py `03a5aff7…`
  (= Stand nach S1b laut `bau/S1-UMSETZUNG.md`).

## Schritte (Reihenfolge)
1. [ ] Lesen: vv.pruefen (alle Rückgabewege), betroffene_funktionen, _syntaxbaum, _m2b_enthaltungen, _gedeckt,
       _nennungen_ausserhalb; aegis (Enthaltung); test_vor_t4_06.py (Hilfen, test_m2_*); t3_verhaltensvergleich
       (unbeobachtet, sonde_vorgeneration_inhalt); Befund S1b `/tmp/r6-s1b/befund-unbeobachtet.txt`; SPERRE-04-AUSGABE.
2. [ ] Kopien: `/tmp/r6-s1c/bau` (git archive HEAD + Arbeitsstand der Runde 6), `/tmp/r6-s1c/vorher` (0c2f058).
3. [ ] Spezifikation `test_w_*` (A, B, C py, C ts, D, E, F; Proben + Gegenproben) → Anhang an 06 (Kopie, dann Baum).
4. [ ] Vorher: am Baum (nach S1b) und an 0c2f058; anhängen an `bau/S1-VORHER-0c2f058.txt`, Einordnung in
       `bau/S1-VORHER-EINORDNUNG.md`.
5. [ ] Bau je Teil `bau/r6_s1c_<teil>.py` (alles oder nichts, zwei Lesungen): an der Kopie, Tests, dann Baum.
6. [ ] Ältere Tests mit Grund anpassen (`bau/S1-GEAENDERTE-TESTS.md`).
7. [ ] Kosten `bau/S1C-KOSTEN.txt` (lagerhaus, logmuehle, uebungswerk-p2, versandwerk-t3-02).
8. [ ] Teillauf Durchgang 5 (`bau/TEILLAUF-S1.txt`), Stücke 1–9 + t3_verhaltensvergleich + t3_python_annahmen.
9. [ ] `bau/S1-UMSETZUNG.md` ergänzen (S1c), Kopie = Baum, Schlussbericht.

## Protokoll
- 13:21 Schritt 1 (Lesen) und 2 (Kopien) erledigt. Kopien (`/tmp/r6-s1c/kopie_anlegen.sh`): `/tmp/r6-s1c/bau` = git
  archive HEAD + alle 23 Dateien aus `git status --untracked-files=all` (bytegleich, sha je Datei im Aufruf);
  `/tmp/r6-s1c/vorher` = git archive 0c2f058. Kammer-Sperre: keine.

## Festlegung S1c (13:30, vor dem Bau; Auslegungen als solche markiert, strenger, nie milder)
Rückgabewege von `pruefen` (gelesen, `761b9a7c…`): (1) `keine_quellaenderung` (kein Modul) tragfähig; (2) SondeAusgefallen
ohne Referenzlast; (3) `sonde_vorgeneration_inhalt` tragfähig; (4) `sonde_kandidat_zeitlimit` nicht tragfähig;
(5) `sonde_kandidat_inhalt` nicht tragfähig; (6) `verfaelschungskappe` Enthaltung; (7) `verfaelschung_unvollstaendig`
Enthaltung; (8) `betroffene_funktion_enthaelt_sich` Enthaltung; (9) `unbeobachtet` tragfähig; (10) `geurteilt`.
- A (Weg 9): `enthaltung: True`, `tragfaehig: False`, `grund_art` bleibt `unbeobachtet`; der Grund nennt auch C/D.
- B (Weg 3): `enthaltung: True`, `tragfaehig: False`, `grund_art` bleibt. Natürlicher Fall für aegis: Kandidat legt nur
  ein NEUES Modul an → an der Vorgeneration „Modul lädt nicht“ (art inhalt).
- D: vor Weg 1. Quellpaket Python = jedes Verzeichnis mit einem Quellmodul (Vorgeneration ∪ Kandidat) samt
  Unterverzeichnissen; Auslegung: die WURZEL (Wurzelmodule, Review 02 Nr. 12) zählt nur für Dateien direkt an der Wurzel,
  ohne README*/LICENSE*/CHANGELOG*/*.md/*.rst/Punktdateien/Werkzeugdateien (Prüfwerkzeug-Konfiguration aus
  verfassung + requirements*.txt, Makefile) — sonst wären tests/ und docs/ im Quellpaket (Widerspruch zum Auftrag).
  Ausgenommen immer: tests/, test/, docs/, _messgeraet/, versteckte, __pycache__. TypeScript: `src/`, jede Datei, die
  kein Quellmodul ist (auch `.d.ts`, `.json`, `.js`, `.tsx`). Gelöschte Dateien zählen. Außerhalb: gezählt (Feld).
  Nur D, keine Module → Enthaltung (`wirkung_ausserhalb_beobachtung`, ausgefuehrt False); mit Modulen → Liste
  `ausserhalb`, wirkt nur bei tragfähig (ungedeckte Abweichung lehnt weiter ab).
- C Python: je geändertem Modul Bindungen der Modulebene beider Stände (Assign/AnnAssign/AugAssign/Import/ImportFrom/
  Delete → Zielnamen; Ziel `X.a`/`X[i]` → X, wenn X in M lokal gebunden, sonst (importiertes Modul/Objekt, Aufruf) nicht
  zuordenbar; `global X` in einer Einheit → X, Anweisung = Form der Einheit). Geändert: Anweisungsliste verschieden, neu,
  entfernt; transitiv: Bindungsanweisung nennt geänderten Namen oder direkt geänderte Einheit (D) → Ziele geändert.
  Nicht zuordenbar (Ausdruck/Aufruf, if/for/while/try/with/assert/match, Sternimport) und verschieden → Enthaltung.
  Ausnahmen: Docstring (schon entfernt), `if __name__ == "__main__":` OHNE else (auch aus `rest` von E3/M2(b)
  genommen — läuft beim Import nicht); bloße Konstanten-Ausdrücke/pass ohne Wirkung.
  Leser außerhalb (Wörter wie `_nennungen_ausserhalb`, Kandidatenstand): anderes Quellmodul nennt N UND den letzten
  Namensteil von M (deckt from M import N, M.N, Alias), oder nennt M und hat einen Sternimport; die Referenzlast nennt N.
  → Enthaltung „Modulwert geändert, außerhalb gelesen (<Quelle>) — Wirkung nicht beobachtet“, Schlüssel `modul:N`.
- C′ (Auslegung S1c, nur wenn Zeit): Klassenwerte (Klassenkörper außer Methoden) analog, Leser = Wort des Attributs.
- C TypeScript (ohne Parser, Scanner mit Klammertiefe/Zeichenketten/Kommentaren): exportierte const/let/var je Name,
  Text verschieden/neu/entfernt, transitiv über Namen des Moduls; `let`/`var` (lebende Bindung) und nicht sicher
  zerlegbare Module → nicht verlässlich → Enthaltung, sobald außen gelesen. Leser: `import { N } from '…/m.js'` in
  anderen src-Modulen und der Referenzlast (ohne `import type`, ohne `type N`); `import * as`, `export * from`,
  dynamisches `import(` → Leser aller Werte (nicht verlässlich).
- E: X neu (nicht in alt.einheiten) und am Kandidaten mit Inhalt beobachtet (`in_[X]`, kein Ausfall/keine Zeitgrenze,
  nicht nur schwankend) → gilt als beobachtet (auch als deckende Aufruferin); Feld `neu_beobachtet`, in x und y.
  Ihre Beobachtungen sind am Kandidaten neu → Abweichungen → brauchen Deckung (sonst abgelehnt).
- F: `rufer[f]` ohne f selbst; gegenseitige Rekursion bleibt kleinster Fixpunkt → nicht gedeckt (Grund „Zyklus …“).
  Älterer Fall `test_m2_regel_gedeckt_am_organ[zyklus]` → Soll „gedeckt“ (Grund in S1-GEAENDERTE-TESTS.md).
- Reihenfolge der Enthaltungen in pruefen (nur bei tragfähig): E3/M2(b) (grund_art wie bisher) → A (nichts
  beobachtet) → C/D (`wirkung_ausserhalb_beobachtung`). Neue Felder `ausserhalb` (C/D), `neu_beobachtet`,
  `nicht_quelldateien_ausserhalb`; C/D auch in `enthaltungen` und `betroffene_enthaltungen`; `kurz` um die Felder.
- Offen zur Entscheidung nach Kosten: TypeScript-M2(b) (nicht beobachtete Funktion eines geänderten TS-Moduls ist heute
  gezählt, Urteil am Rest — stiller Durchlass der Klasse, Befund S1b Nr. 3).
- 13:45 Nachschärfung vor der Spezifikation (Auslegungen S1c, strenger):
  - D Wurzel: liegt an der Wurzel ein Quellmodul (Wurzelmodul), ist die Wurzel samt Unterverzeichnissen Quellpaket —
    ausgenommen tests/, test/, docs/, doc/, versteckte, _messgeraet/, __pycache__ und an der Wurzel README*/LICENSE*/
    CHANGELOG*/*.md/*.rst und Werkzeugdateien (pyproject.toml, setup.cfg, tox.ini, requirements*.txt, Makefile,
    MANIFEST.in, pytest.ini, mypy.ini, Werkzeug-.py) — wörtlich „samt Unterverzeichnissen“, nie milder.
  - C Python Leser im Modul bei `global`: ändert eine direkt geänderte Einheit einen Modulwert über `global`, ist der
    Modulrest gleich — die Einheiten von M, die den Namen nennen, kommen für M2(b) zu D (sonst stimmt „Leser in M
    erfasst schon M2(b)“ dort nicht).
  - C Python __main__-Ausnahme nur, wenn weder die Referenzlast noch ein Quellmodul `runpy`/`run_module`/`run_path`
    nennt; sonst Enthaltung `<__main__>`.
  - C TypeScript: Zerleger ohne Parser (Zeichenketten, Vorlagen, Kommentare, Regex-Literale, Klammertiefe); Anweisungen
    der obersten Ebene beginnen in Spalte 0 bei Tiefe 0. Arten: FUNK, KLASSE, TYP (interface/type/declare/import type/
    export type — keine Laufzeit), IMPORT (bindet Namen; Seiteneffekt-Import = frei), WERT (const/let/var/enum/export
    default; einfache Namen), EXPORTLISTE und alles andere = frei. Geänderter Wert N: exportiert und außen gelesen
    (import {N}, import * as, export * from, dynamisches import/require, Referenzlast über dist/) → Enthaltung; im
    Modul gelesen von einer nicht exportierten oder nicht beobachteten Funktion, einer Klasse oder der Modulebene →
    Enthaltung (ohne M2(b) für TypeScript nicht verlässlich bestimmbar). Nicht zerlegbar, Destrukturierung, mehrere
    Deklaratoren → Enthaltung, sobald geändert.
  - Spezifikation: Python-Regeln von C und D zusätzlich AM ORGAN (Sonde gestellt, Syntaxbaum echt) statt als
    Unit-Tests neuer Hilfsfunktionen — so sind Gegenproben auch an älteren Ständen grün.
- 14:05 Festlegung E/F und Klassen (nach Lesen der Sonde; Auslegungen S1c, strenger):
  - E: die Sonde ruft am Kandidaten den Korpus nur mit den Signaturen der Vorgeneration — eine neue Funktion wäre nie
    beobachtet (Fehlalarm bliebe). Darum verhalten.py: am Kandidaten zusätzlich Korpus (Randfälle, Formvarianten) für
    öffentliche Funktionen/Methoden, die die Vorgeneration nicht hat (`signaturen_neu`). Im Vergleich sind diese
    Korpusbeobachtungen kein Verhalten des bestehenden Codes (spiegelbildlich zu `entfernte_funktionen`): getrennt
    ausgewiesen (`neu_beobachtet`), keine Abweichung. Lastbeobachtungen neuer Funktionen bleiben Abweichungen.
    E gilt nur, wenn die neue Einheit (1) eine Funktion der Modulebene oder Methode einer neuen Klasse ist, (2) kein
    Quellmodul der Vorgeneration ihren Namen nennt (Wörter; sonst dynamischer Zugriff/Überschreiben), (3) nicht auf
    Modul-/Klassenebene genannt ist (auch kein weitergebender Dekorator), (4) am Kandidaten mit Inhalt beobachtet ist
    (keine Zeitgrenze, kein Ausfall, vollständig). Sonst M2(b) wie bisher. Neue Methoden bestehender Klassen: M2(b).
  - F: `rufer[f]` ohne f; gegenseitige Rekursion bleibt Zyklus (kleinster Fixpunkt).
  - C Python zusätzlich (Klasse schließen): Klassenwerte (Zuweisungen im Klassenkörper) wie Modulwerte, Leser = Wort
    des Attributs in anderen Modulen/Referenzlast; Einheiten von M, die K nennen, kommen bei geändertem Klassenrest zu
    D. Neue/entfernte Klasse oder geänderter Kopf mit Basis (außer eingebauten/typing/enum/abc), Schlüsselwort oder
    nicht harmlosem Dekorator, ebenso Funktion mit nicht harmlosem Dekorator neu/entfernt/Dekorator geändert →
    `<modulebene>` (Wirkung beim Import).
  - C TypeScript zusätzlich (TS hat kein M2(b)): geänderte Funktion ohne Beobachtung (exportiert und nicht beobachtet;
    nicht exportiert und nicht gedeckt), geänderte Klasse (die TS-Sonde wickelt Klassen nicht ein) → Enthaltung
    „betroffen, von der Sonde nicht beobachtet (TypeScript …)“.
- 14:28 Spezifikation gebaut (`bau/r6_s1c_spez.py` `ea7d7ffc…`, Werkzeug `bau/r6_s1c_werkzeug.py`, Protokoll
  `bau/S1C-BAU-SPEZ.txt`): 06 `80feee35…` → `7d3f0617…` — Sammelfehler („unexpected '{' in field name“ in
  `W_TS_RUMPF`); ~20 s später Nachtrag `bau/r6_s1c_spez_n1.py` (`5d490a84…`, erst Kopie + Sammeln, dann Baum):
  06 → `e47b5f16…` (Kopie = Baum), 168 Fälle gesammelt (102 + 66 `test_w_*` in 7 Funktionen: aegis 13, C-Py 15,
  D-Py 15, D gemischt 2, C-TS 13, A/B/D-TS 4, E/F 4). Lehre: vor dem Baum an der Kopie sammeln.
- NÄCHSTES: Vorher am Baum (Code nach S1b) und an 0c2f058 (`/tmp/r6-s1c/vorher`, 06 hineinkopiert), in Stücken < 400 s
  (aegis-Fälle getrennt), Ausgabe `/tmp/r6-s1c/w-vorher-<ort>-<teil>.txt`.
- 14:33–14:44 Nachträge Spezifikation n2 (`e_neu_unbeobachtet` war keine Probe), n3 (Gegenproben a_gegen/c_innen an
  0c2f058 rot aus vorbestehendem Grund: assert ohne Meldung hielt vor R6-4 nie fest → mit Meldung), n4 (e/f durch
  aegis: zusätzlich `neu_beobachtet`/`direkt_gedeckt`); 06 → `83bb277f…` (Kopie = Baum).
- 14:47 Vorher (Endstand Spezifikation, `/tmp/r6-s1c/w-vorher-{baum,vorher}-{organ,aegis1,aegis2}.txt`): 66 Fälle;
  Proben 36 — rot am Baum 36, an 0c2f058 36; Gegenproben 26 — rot 0/0; Wächter (E/F wie M2(b)) 4 — Baum 0, 0c2f058 4.
  Angehängt: `bau/S1-VORHER-0c2f058.txt` `e9d812f2…` → (siehe Protokoll unten), `bau/S1-VORHER-EINORDNUNG.md`.
- NÄCHSTES: Bau je Teil an der Kopie, in dieser Reihenfolge (je ein Skript, Tests nach jedem):
  1. `bau/r6_s1c_ab.py` (A, B: Enthaltung in pruefen; `kurz`),
  2. `bau/r6_s1c_d.py` (D: Quellpaket, `ausserhalb`, vor/nach Weg 1),
  3. `bau/r6_s1c_ef.py` (F: rufer ohne Selbst; E: neu beobachtet — vv + verhalten.py `signaturen_neu`),
  4. `bau/r6_s1c_c.py` (C Python: Modulwerte, `<modulebene>`, `<__main__>`, global → D; C TypeScript: Zerleger).
- 14:55 Bauplan (vor dem Code, gelesen: pruefen, _syntaxbaum, betroffene_funktionen, _m2b_enthaltungen, Sonde main/
  korpus_randfaelle/alle_wickeln/signaturen_lesen):
  - `r6_s1c_ab.py`: Weg 3 (B) und Weg 9 (A) → `tragfaehig False`, `enthaltung True` (grund_art bleibt); Kopf-Docstring;
    `kurz` + `ausserhalb`, `neu_beobachtet`, `nicht_quelldateien_ausserhalb`.
  - `r6_s1c_d.py`: `nicht_quelldateien(werk, code, python)` (Quellpaket wie Festlegung); vor Weg 1 Enthaltung
    `wirkung_ausserhalb_beobachtung`; `ausserhalb` (dict) in `extra`; neuer Rückgabeweg nach A: tragfähig und
    `ausserhalb` → Enthaltung. B-teilweise: geändertes, an der Vorgeneration vorhandenes Modul in `alt.nicht_ladbar`
    → `m:<ladbar>`.
  - `r6_s1c_ef.py`: F in `_m2b_enthaltungen` (rufer ohne sich selbst; Grund „Zyklus mit …“ bei gegenseitiger
    Rekursion); E in pruefen (`neu_beob`: Bedingungen der Festlegung 14:05), Korpusbeobachtungen neuer Funktionen aus
    dem Vergleich (Spiegel von `entfernt`), x/y; `beobachten(..., bekannt=)`; verhalten.py: am Kandidaten Korpus für
    Funktionen außerhalb von `bekannt` NACH dem übrigen Korpus (`signaturen_neu`).
  - `r6_s1c_c.py`: `_modulwerte` in `_syntaxbaum` (Bindungen, frei, Folge, __main__, global/Mutation in Einheiten,
    Klassenwerte/-köpfe, Dekoratoren), `rest` ohne __main__-Block; `_quelltexte` (Refaktor von
    `_nennungen_ausserhalb`, gleiche Rückgabe); `_c_python`, `_c_typescript` (Zerleger), Leser in M → D (vor M2(b)).
  - Vorher: Nachtrag n5 der Spezifikation (Mutation, Klassenwert/-kopf, frei liest geänderten Wert, Dekorator,
    B-teilweise, neues Modul mit E) VOR dem Bau von C/D.
- 15:13–15:19 Nachtrag n5 (`bau/r6_s1c_spez_n5.py`, 11 Fälle: C-Python-Auslegungen Mutation, Klassenwert, Klassenkopf,
  Anweisung ohne Namen liest geänderten Wert, Dekorator; B teilweise) und n6 (`r6_s1c_spez_n6.py`: B-teilweise-Probe
  korrigiert: `c` lädt an beiden Ständen nicht) → 06 `71cbdd53…` (Kopie = Baum), 179 Fälle (77 `test_w_*`).
  Vorher n5/n6 (`/tmp/r6-s1c/w-vorher-{baum,vorher}-n5.txt`): Baum 8 von 11 rot, 0c2f058 8 von 11 rot (6 C-Proben,
  B vorhanden, B neu (= E-Probe)); 3 Gegenproben grün an beiden. Noch nicht an die VORHER-Dateien angehängt (mit
  dem Schlussanhang).
- 15:25 Festlegung C Python (Einzelheiten, vor dem Bau): Bindungen der Modulebene je Name als Liste der Anweisungs-
  formen (Assign/AnnAssign/AugAssign/Delete/Import/TypeAlias; Ziel `X[i]`/`X.a` mit lokal gebundenem X (nicht Import)
  → X; sonst frei); Klassenwerte `K.a`, Klassenkopf `K`; Funktionen/Klassen als Namen nur neu/entfernt; frei = alle
  übrigen Anweisungen (ohne Konstanten-Ausdrücke, pass, Docstring, `__main__` ohne else); `deko` = Dekoratoren mit
  Wirkung beim Import (nicht harmlos; Klassen: auch Schlüsselwörter; harmlos zusätzlich dataclass, total_ordering,
  unique, final, runtime_checkable). Geändert: Form verschieden/neu/entfernt; + `global`-Ziele und Mutationsbasen
  (Zuweisungs-/del-Ziel `N[..]`/`N.a`, bekannte verändernde Methoden) eigen geänderter Einheiten, wenn N ein nicht
  importierter Modulname ist; transitiv über Bindungen. Frei verschieden oder frei liest Geändertes → `<modulebene>`;
  deko verschieden → `<modulebene>`; `__main__` verschieden und runpy/run_module/run_path/"-m" genannt → `<__main__>`.
  Leser außen: anderes Quellmodul nennt N und den letzten Namensteil von M, oder hat Sternimport aus M (liest alle);
  Referenzlast nennt N; `K.a`: nennt a. NEUE Namen: Leser in geänderten Modulen ausgenommen (ihr Lesen ist deren
  eigene Änderung). Leser in M (Einheiten, deren Lese-Wörter N enthalten; reine Schreibziele lesen nicht) → zu D.
- 15:34 Bau A/B an der Kopie (`bau/r6_s1c_ab.py` `3031322c…`, 6 Anker, Protokoll `bau/S1C-BAU-AB.txt`): vv
  `761b9a7c…` → `bfdb1ed2…`; t3_verhaltensvergleich `d6f239c4…` → `103f2e92…` (2 ältere Tests: unbeobachtet,
  sonde_vorgeneration_inhalt — Grund im Docstring). Kopie: test_w_abd a/b + t3-Fälle 7/7 grün (d_datei rot: D fehlt
  noch); aegis a_konst, a_gegen, b_neues_modul 3/3 grün (Kammer). Baum noch NICHT gebaut.
- NÄCHSTES: `bau/r6_s1c_d.py` (D + B-teilweise), dann E/F, dann C.
- 15:43 Bau D an der Kopie (`bau/r6_s1c_d.py` `df522833…`, 5 Anker; Nachtrag `bau/r6_s1c_d_n1.py` `22c3aab4…`: Wächter
  t3_python_annahmen meldete `werkzeugdateien()` ungeschützt — Aufruf jetzt direkt hinter der Weiche). vv (Kopie)
  `bfdb1ed2…` → `455b483f…` → `74f46a99…`. Kopie: test_w_d_*, test_w_abd, aegis d_daten/d_readme, Wächter 25/25;
  b_modul[vorhanden] grün, b_modul[neu] rot (E fehlt noch). Baum noch nicht gebaut.
- NÄCHSTES: `bau/r6_s1c_ef.py` (F in _m2b_enthaltungen; E: vv neu_beob + verhalten.py Korpus neuer Funktionen).
- 15:49 Bau E/F an der Kopie (`bau/r6_s1c_ef.py` `cb109aec…`, 12 Anker: vv `74f46a99…` → `e6de27a6…`, verhalten.py
  `c4071c40…` → `cbb88f42…`) und älterer Test (`bau/r6_s1c_ef_test.py` `babee0b1…`: `test_m2_regel_gedeckt_am_organ[zyklus]`
  Soll → gedeckt; 06 Kopie `71cbdd53…` → `e581edfa…`). Kopie: test_w_ef, b_modul, m2_regel*, m2_direkt*, Wächter
  27/27; aegis e_neu_*, f_* 4/4 (Kammer). Baum noch nicht gebaut.
- NÄCHSTES: `bau/r6_s1c_c.py` (C Python + C TypeScript) — größter Teil; Entwurf zuerst in /tmp/r6-s1c/c_entwurf.py.
- 16:00 Entwurf C (vor dem Code, Einzelheiten): Python — `_lese_worte` (Ladekontext, ohne Grundnamen reiner
  Schreibziele), `_schreibziele` (global, N[..]=, N.a=, del, verändernde Methoden), `_modulwerte` (werte/liest/frei/deko/
  main/importiert/stern/einheit_liest/einheit_schreibt/oben) in `_syntaxbaum` als Schlüssel `modulwerte`; `_c_python`:
  geändert = Formen verschieden ∪ Schreibziele direkt geänderter Einheiten (nur Modulnamen, nicht importiert) ∪
  transitiv; Leser außen: unverändertes Quellmodul nennt N und den letzten Namensteil von M (Klassenwert: nur das
  Attribut) oder Sternimport aus M; GEÄNDERTES Quellmodul nur, wenn eine seiner UNVERÄNDERTEN Anweisungen der obersten
  Ebene N nennt (sonst ist das Lesen dessen eigene, selbst geprüfte Änderung); Referenzlast nennt N. Leser in M → D.
  TypeScript — Zerleger (Zeichenketten, Vorlagen, Kommentare, Regex, Klammertiefe; Grenze: Zeilenanfang in Spalte 0
  bei Tiefe 0), Arten funk/klasse/wert/wertlet/unklar/import/typ/exportliste/reexport/frei; geändert je Name (Text ohne
  Kommentare, Weißraum verdichtet), transitiv, Schreibziele geänderter Funktionen (let/var-Zuweisung, verändernde
  Methoden); Leser außen über Importe (aufgelöster Pfad), `import * as`, `export … from`, dynamisch; Leser in M:
  beobachtete exportierte Funktion ok, gedeckter Helfer ok, sonst Enthaltung; geänderte Funktion: beobachtet (neu:
  am Kandidaten) oder gedeckter Helfer, sonst Enthaltung; geänderte Klasse → Enthaltung; frei geändert → `<modulebene>`.
- 16:20 Nachschärfung C (vor dem Code): (1) Leser außerhalb je ANWEISUNG der obersten Ebene des anderen Moduls B:
  Anweisung nennt N und (letzter Namensteil von M oder ein Alias von M in B) — deckt `from M import N`, `M.N`,
  `import p.M as X` + `X.N`; Sternimport aus M → jede Anweisung, die N nennt; Klassenwert `K.a`: nennt a. Referenzlast
  als eine Anweisung. So kein Fehlalarm für `import re` in M neben einem anderen Modul, das selbst `re` importiert.
  (2) Ausnahme geändertes Modul B: liest nur in Anweisungen, die der Kandidat in B geändert/neu hat → B prüft sie
  selbst (C, E3, M2(b)); eine unveränderte lesende Anweisung → Enthaltung. TypeScript ebenso (Importe je Anweisung).
  (3) Anweisung der Modulebene nur aus einem Namen oder einer Konstanten (`x`, `'use strict'`) ist frei von Wirkung
  (Ladefehler sähe die Sonde) — ältere Tests nutzen `'x'` als Platzhaltermodul. (4) TS: Importe binden Namen (ein
  geänderter Import ändert den Wert); Namensraum-Import liest nur exportierte Werte; Referenzlast über Importanalyse
  (`./dist/…`). (5) `rest` von E3/M2(b) bleibt unverändert (auch mit `__main__`) — nicht milder als S1b.
- 16:14 Bau C an der Kopie (`bau/r6_s1c_c.py` `f183a8a3…`, 5 Anker, Entwurf `/tmp/r6-s1c/c_entwurf.py`): vv (Kopie)
  `e6de27a6…` → `166c61fc…`. Kopie lokal: alle test_w_* am Organ (C-Py 15 + Nachtrag 9, D, C-TS 13, A/B/D-TS, E/F, B
  teilweise) + Wächter + t3_verhaltensvergleich: 89/89 grün.
- NÄCHSTES: Kopie mit Kammer: test_w_wirkung (13), 06 ganz (in Stücken), 05, 04, 03, 02, test_vor_t4; dann Kosten;
  dann Bau am Baum (alle Skripte in Reihenfolge: spez* sind schon am Baum; ab, d, d_n1, ef, ef_test, c).
- 16:15–16:29 Kopie mit Kammer (`/tmp/r6-s1c/kopie-*.txt`): test_w_wirkung (aegis) 13/13; 06 m2_+u2n_ 39/39; 06 Rest
  63/63; 05 27/27; 04 36/36; 03 36/38 → 2 ältere Gegenproben rot (`test_a4_gegenprobe_instabile_…`,
  `test_s12_gegenprobe_einmaliges_zeitlimit_…`: gestellte Sonde ohne `eingewickelt` → „0 von 0“ = A) → angepasst mit
  Grund (`bau/r6_s1c_tests03.py` `21c8142a…`, 03 Kopie `9672cd54…` → `707a5a7f…`), danach 5/5; 02 + test_vor_t4 +
  t3_python_annahmen + t3_verhaltensvergleich 108/108; verdrahtung (ohne ganzen Lauf) + tor4_zeilen 67/69 — 2 rot nur
  an der Kopie: `git rev-parse HEAD` in /tmp/r6-s1c/bau (git archive ohne .git) — Umgebung, am Baum im Teillauf.
- NÄCHSTES: Kosten `bau/S1C-KOSTEN.txt` (Kopie, 4 Werke), dann Bau am Baum.
- 16:35 Nachtrag C (`bau/r6_s1c_c_n1.py` `c28dbdc7…`): Leser außerhalb über aufgelöste Importpfade (vorher: gleicher
  letzter Namensteil `…bericht.auswertung`/`…formeln.auswertung` galt als Leser — Fehlalarm, gemessen an den Kosten).
  vv (Kopie) `166c61fc…` → `53e676da…`; Organ-Fälle wieder 89/89.
- 16:32–16:38 Kosten gemessen (`/tmp/r6-s1c/kosten_s1c.py`, `/tmp/r6-s1c/kosten-<werk>.{txt,json}`, Kopie nach S1c):
  lagerhaus 17,5 s, lagerhaus-p2 19,5 s, logmuehle 121,9 s, versandwerk-t3-02 13,7 s; alle rc=0, 0 Container.
- NÄCHSTES: `bau/S1C-KOSTEN.txt` schreiben; dann Bau am Baum (ab, d, d_n1, ef, ef_test, c, c_n1, tests03), Kopie = Baum.
- 16:39 `bau/S1C-KOSTEN.txt` neu (exklusiv, `2836f896…`; `/tmp/r6-s1c/kosten_schreiben.py`).
- 16:40 Bau am Baum (`/tmp/r6-s1c/baum_bauen.sh`, Protokolle `/tmp/r6-s1c/baum-<skript>.txt` und `bau/S1C-BAU-*.txt`):
  ab, d, d_n1, ef, ef_test, c, c_n1, tests03 — alle „ok“. Baum: vv `761b9a7c…` → `53e676da…`, verhalten.py `c4071c40…`
  → `cbb88f42…`, 06 `71cbdd53…` → `e581edfa…`, t3_vv `d6f239c4…` → `103f2e92…`, 03 `9672cd54…` → `707a5a7f…`. Kopie =
  Baum für alle 10 Dateien (aegis, 05, 04, 02, t3_python_annahmen unverändert). Keine Sperre.
- NÄCHSTES: Teillauf Durchgang 5 (`/tmp/r6-s1c/teillauf5.sh`, Stücke 1a/1b/1c, 2–9, dazu 6 = t3_python_annahmen +
  t3_verhaltensvergleich), Anhang an `bau/TEILLAUF-S1.txt`.
- 16:42–16:56 Teillauf Durchgang 5 am Baum (`/tmp/r6-s1c/teillauf5.sh`, Stücke 1a/1b/1c, 2–9; Sperre vor jedem Stück
  geprüft: keine): 457 von 457 grün, 0 rot, 1 abgewählt (ganzer Lauf in test_verdrahtung). 06: 179 von 179 (77 test_w_*).
  Zusammenfassung angehängt (`/tmp/r6-s1c/teillauf5_summe.py`): TEILLAUF-S1.txt `43b6bd65…` → `cf6ac3cf…`.
- NÄCHSTES: (1) Vorher n5/n6 an `bau/S1-VORHER-0c2f058.txt` + `S1-VORHER-EINORDNUNG.md` anhängen; (2)
  `bau/S1-GEAENDERTE-TESTS.md` Nachtrag S1c (t3_vv 2, 06 zyklus 1, 03 2); (3) `bau/S1-UMSETZUNG.md` Abschnitt S1c +
  verbleibende tragfähige Wege (pruefen gelesen); (4) Kopie = Baum Schlussprüfung; (5) Schlussbericht.
- 16:58 Vorher n5/n6 angehängt (`/tmp/r6-s1c/vorher_n5_anhaengen.py`): S1-VORHER-0c2f058.txt `b84ca19a…` →
  `7589363d…`, S1-VORHER-EINORDNUNG.md `e95bc36b…` → `481f55a9…`. Summe S1c: Proben 44/44 rot (Baum/0c2f058), Gegenproben
  0/0 von 29, Wächter 0/4.
- 17:01–17:07 Zusatz zum Teillauf (`/tmp/r6-s1c/zusatz.sh` z1–z3): 17 weitere aegis-Rufer außerhalb der Stücke 1–9 —
  166 von 168 grün, 2 übersprungen (skipif ohne BIOTOP_EICHWERK). TEILLAUF-S1.txt → `f2d347e2…`.
- 17:08 S1-GEAENDERTE-TESTS.md Nachtrag S1c (Nr. 7–11) `f61b8abf…` → `2d9c47ee…`.
- NÄCHSTES: Rückgabewege von `pruefen` am Endstand lesen (tragfähig True) → `bau/S1-UMSETZUNG.md` Abschnitt S1c;
  Schlussprüfung Kopie = Baum; Schlussbericht.
- 17:14 BEFUND beim Lesen der Rückgabewege (Restweg „geurteilt“), gemessen am Baum (aegis, Kammer;
  `/tmp/r6-s1c/befund_fremdschreiben.{py,sh}`, `/tmp/r6-s1c/befund-fremdschreiben.txt`): eine BEOBACHTETE, direkt
  geänderte Funktion `setze` (kern) schreibt in ein IMPORTIERTES Modul (`konst.RATE = 19` → `7`); das unveränderte
  `leser.brutto` liest den Wert → vv `geurteilt` „9 von 9 beobachtet“, `ausserhalb` {} → aegis `ueberlebt` — stiller
  Durchlass derselben Klasse (C erfasste Schreibziele nur für Namen, die M selbst bindet; Festlegung 15:25).
  Entscheidung (Maßstab: Klasse schließen, Skill: in derselben Runde bauen): Teil G =
  „geänderte Einheit schreibt in ein importiertes Objekt“ (Zuweisung/del/erweitert an `N.a`/`N[k]`, verändernde
  Methode `N.append(…)`, N im Modul durch Import gebunden; auch `global` eines importierten Namens) → Enthaltung
  `M:<schreibt:N>`. Spezifikation zuerst (n7), Vorher an Baum und 0c2f058, Bau an Kopie, dann Baum, Kosten je Werk.
  Nicht statisch bestimmbar und darum OFFEN (Bericht): Seiteneffekte über AUFRUFE in andere Module
  (`konst.setze_rate(7)`) und über Aliase (Parameter, die auf fremde Objekte zeigen) — die Sonde wickelt unveränderte
  Module nicht ein; Messung folgt.
- 17:18 Zweite Variante gemessen (`befund_fremdschreiben.sh ruft`, `/tmp/r6-s1c/befund-fremdschreiben-ruft.txt`):
  `setze` ruft `konst.setze_rate(7)` statt `(19)` (setze_rate schreibt `global RATE` in konst) → ebenfalls `ueberlebt`,
  geurteilt „9 von 9“. (Erster Lauf „schreibt“: `/tmp/r6-s1c/befund-fremdschreiben-schreibt-erstlauf.txt`.)
- 17:20 Festlegung Teil G (Auslegung S1c, strenger; dieselbe Klasse: Wirkung einer geänderten Funktion außerhalb
  der Beobachtung — die Sonde beobachtet Rückgabe und Argumentzustand, nicht Schreibzugriffe auf Modulzustand):
  - Python G1: eine direkt geänderte Einheit f von M verändert ein durch Import gebundenes Objekt N (Ziel `N.a`/`N[k]`,
    erweitert, del, verändernde Methode, `setattr/delattr(N, …)`) → Enthaltung `M:<schreibt:N>`; `global N` mit
    importiertem N bindet M.N neu → N geändert (C wie bisher); `globals()[…]`/`vars()[…]` → `M:<schreibt:globals()>`.
  - Python G2: „Schreiber“ = Einheit eines Quellmoduls, die Modulzustand schreibt (eigene Modulnamen, importierte
    Objekte, globals) oder (Wort, strenger als Aufruf) einen Schreiber ihres Moduls bzw. eines Moduls nennt, aus dem
    ihr Modul importiert — Fixpunkt über alle Quellmodule (Kandidatenstand). Nennt f einen Schreiber g ≠ f: g in M →
    die von g (transitiv in M) geschriebenen Namen von M gelten als geändert (C wie bisher); g in einem anderen Modul
    K → Enthaltung `M:<ruft:K:g>`.
  - TypeScript G: geänderte Funktion verändert ein importiertes Objekt (`_ts_schreibt` auf Import-Bindungen) →
    `m:<schreibt:N>`; nennt sie eine Funktion desselben Moduls, die wert/wertlet schreibt → deren Namen geändert;
    nennt sie eine importierte Funktion eines Moduls, deren Text dort Modulzustand schreibt → `m:<ruft:K:z>`.
  - Bleibt offen (Bericht): Wirkung über Dateien/Umgebung/Prozesse (E/A), Reflexion jenseits globals/setattr,
    Schreiben über Aliase (Parameter, die auf fremden Modulzustand zeigen, ohne Namen).
  - Reihenfolge: Spezifikation n7 (Organ: G1/G2 Python, G TS; aegis: befund „schreibt“ und „ruft“) → Vorher Baum und
    0c2f058 → Bau `bau/r6_s1c_g.py` an der Kopie → Tests → Kosten G je Werk → Baum → Teillauf-Nachlauf (Stücke, die
    vv nutzen).
