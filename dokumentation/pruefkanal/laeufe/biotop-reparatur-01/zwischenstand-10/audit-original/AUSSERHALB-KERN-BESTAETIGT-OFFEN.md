# Außerhalb Kern — bestätigt offen

6 deduplizierte Mechanismen an 11 Leserorten in 11 historischen Prüfdateien. **Eigener späterer Auftrag; keine Fixpflicht dieser zweiten/letzten Runde.**

Bestätigt ist der statische Fehlmechanismus, nicht sein Vorkommen in einer unbekannten aktuellen DB. Kein Skript wurde ausgeführt. Offene Verdachte stehen ausschließlich in KANDIDATEN-OFFEN.json.

## B05 — Positive Text-/Messmarker werden trotz fehlendem Laufabschluss verwertet
- `pruefung/funde_neubewerten.py:23-43`
- `pruefung/tor1_f2.py:24-71`
- Mechanismus: Ausgabe enthält erwartete positive Tokens, während rc/zeitlimit nicht hinreichend an die Wertung gebunden sind
- Minimalzustand: Reststdout mit "1 passed" und rc7/124; oder vollständiger @@MESSUNG@@-Marker und rc7.
- Schluss: Fundleser besteht=True, Aufnahme zählt positive Tests trotz Abbruch (Status ist Aufnahme, NICHT behauptet alles grün); messen setzt gueltig=True sofern kein explizites Zeitlimit und Marker vorhanden. Tor1-F2 akzeptiert positive Tokens ähnlich.
- Grenze: Messen sperrt explizites zeitlimitTrue und fehlenden Marker; Original Aufnahme sperrt echten Gesamtwert0.

## B09 — Fehlendes Paarmaß/Vertragsergebnis zählt als bestanden
- `pruefung/verhandlungsprobe.py:57-75`
- `pruefung/proben_tor2.py:196-215`
- Mechanismus: not dict.get(...) mit None/{} macht Nichtprüfung zur leeren gültigen Fehlermenge
- Minimalzustand: u2={status:abgelehnt,mass:None,vertrag_verletzt:[]} nach frühem Prüfabbruch.
- Schluss: L580 paar_ok=True; historische Skripte melden Vertrag bestanden, obwohl Status daneben abgelehnt sein kann.
- Grenze: Kein Schluss, dass gesamte Generation dadurch zwingend angenommen wird: nachgelagerte Status-/Generalprobegates existieren. Fehler ist konkretes Paar-/Vertragsbestanden-Urteil.

## B13 — Leere Prüfpoulation erfüllt historisches lokales Gütekriterium
- `pruefung/anklaeger_vielfalt.py:34-54`
- `pruefung/nachgang_n2_n3.py:117-168`
- `pruefung/nachgang_n10.py:49-99`
- Mechanismus: Leerer Nenner/Fehlerlisten ergeben BESTANDEN/ERFÜLLT ohne vorhandenen Prüfumfang
- Minimalzustand: Keine passenden historischen Tests/Ansagen/Sperrungen; Fehlerlisten leer.
- Schluss: max(1,N) bzw not(fehlalarm/durch) führt zur positiven lokalen Ergebniszeile.
- Grenze: Berichte können daneben fehlende Farbzeugen nennen; bestätigt ist falsches Teilurteil, nicht gesamte Berichtabnahme. Aktuelle DB nie gelesen.

## B14 — Nicht ausgeführte Durchrutscherprüfung wird als gemessen ausgegeben
- `pruefung/lauf25_auswertung.py:37-108`
- Mechanismus: Leere Ergebnisliste bleibt durch for/pass unverändert und wird als berechneter Nullbefund etikettiert
- Minimalzustand: erzeugt enthält mindestens einen Eintrag.
- Schluss: durch=[]; for e in erzeugt: pass; Ausgabe 0vonN gemessen.
- Grenze: 0=0-Pfadnachweis Z50-54 ist ausdrücklich korrekt gesperrt. Kein eigener neuer Reparaturauftrag.

## B15 — Fehlmessung kann historische negative Eichkontrolle erfüllen
- `pruefung/eichung_falld.py:34-41`
- `pruefung/eichung_pruefen.py:19-50`
- Mechanismus: not lauf_startet wird ohne Nachweis der beabsichtigten Rauschursache als bestanden gewertet
- Minimalzustand: Einziger Bereich liefert keine verwertbaren Messungen statt absichtlich schwankender ausgeführter Messungen.
- Schluss: rauschmessung sperrt Bereich/lauf_startet=False; historischer FallD meldet bestanden bzw gewünschtes True.
- Grenze: Produkt-Vorspann prüft Messqualität zusätzlich; Außenfall ist nicht das aktuelle Gate.

## B16 — Historische rote-Testzählung verdeckt nicht ausgeführte Tests
- `pruefung/tor2.py:39-112`
- Mechanismus: rc0 wird bei Rotzählung wie vollständige Testausführung behandelt
- Minimalzustand: Eine angenommene Generation hat pytest-rc0 bei nur skipped-Testcases.
- Schluss: sum(rc!=0)=0; Ausgabe meldet0 rote Testläufe, fehlender Ausführungsnachweis nicht kenntlich.
- Grenze: Reine Statistik "0 Fehlerexits" wäre legitim; Überschrift beansprucht dagegen nach jeder Generation Testnachweis. Teilberichtsfehler, keine aktuelle Produktfreigabe.

