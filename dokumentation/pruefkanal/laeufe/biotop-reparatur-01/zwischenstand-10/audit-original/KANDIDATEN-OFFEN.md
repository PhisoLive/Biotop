# Offene Kandidaten und unvollständige Suchzuordnung

Diese Liste enthält **keine bestätigten Befunde**. Kein zusätzlicher Reparaturauftrag.

- **C01 / M03** `biotop/kern/messgeraet.py:113-127` — kernpfad: Fehlende/unlesbar syntaktische Teilabdeckung kann 0 größte Funktion/0 Tests liefern. Bauprobe fängt manche Syntaxfälle, nicht sämtliche unimportierten Module; noch keine isolierte Ausführungsprüfung.
- **C02 / A07** `biotop/organe/aegis.py:489-516` — kernpfad: Ob Kernaufrufer Sonderpfad fälschlich als frisch geprüft akzeptiert, nicht komplett bewiesen; _verhandeln setzt kid zurück.
- **C03 / P03** `pruefung/archivierung_pruefen.py:57-94` — ausserhalb_kern: Archiv-Alterszählung, gestellter Fund und lokale Regelkopie; Nachlauf-Kammerfreiheit nur aus Filterabfrage abgeleitet, keine Kammerausführung (offener Prüfkandidat).
- **C04 / P05** `pruefung/aufnahmesperre_pruefen.py:67-106` — ausserhalb_kern: Direkter Aufnahmesperrenaufruf/Zeugenlisten; Teilkriterien Fehlalarm/Durchrutscher ohne Mindestpopulation, rote/grüne Fälle separat angezeigt.
- **C05 / P32** `pruefung/proben_tor2.py:63-174` — ausserhalb_kern: Mehrere Aegis-Leser: Nichtüberleben=Abweisung, Norm-Dateiabwesenheit, Vertragsnot-list=bestanden; letztere nach frühem Abbruch außen bestätigt.
- **C06 / P33** `pruefung/rauschprobe_lauf19.py:10-25` — ausserhalb_kern: Fünf Messgeräteaufrufe/Referenzzeitvergleich; gueltig nicht gelesen, None typischerweise Formatfehler; numerische Provenienz offen, historische Ausgabe.
- **C07 / P39** `pruefung/tor3.py:19-99` — ausserhalb_kern: Historische DB/Mess-/Jury-/Entropieberichte; fehlende _testbestand/_dateien ->[] kann Kammerfreiheit vortäuschen, extern ungeprüft.
- **C08 / M14** `biotop/kern/messgeraet.py:168-192` — kernpfad: Fehlende Verzeichnisse vs echte leere Importmenge lokal nicht unterscheidbar; Annahmepfad nicht separat bewiesen.

Zusätzlich bleiben **45 der 661 breiten Kandidatenzeilen** in der Feinzuordnung offen. Diese Zahl ist keine Leser- oder Fehlerzahl. Vollständige Liste samt Originalcode in `SUCHTREFFER-ZUORDNUNG.json`, Status `Feinzuordnung_offen`.

| Datei | Noch nicht einzeln zugeordnete Quellzeilen |
|---|---|
| `biotop/kern/messgeraet.py` | 40, 197, 199, 201, 260 |
| `biotop/organe/aegis.py` | 40, 413 |
| `biotop/organe/aufnahme.py` | 24, 31, 173, 175 |
| `biotop/organe/eichproben.py` | 195, 429 |
| `biotop/organe/eichung.py` | 42 |
| `biotop/organe/fundpruefung.py` | 53 |
| `biotop/organe/generation0.py` | 203, 205, 209 |
| `biotop/organe/genesis.py` | 29 |
| `biotop/organe/kammer.py` | 25, 26, 27, 36, 43, 47, 52, 54 |
| `biotop/organe/lazarus.py` | 25, 41, 49 |
| `biotop/organe/mentor.py` | 29 |
| `biotop/organe/vorspann.py` | 52 |
| `pruefung/aufnahmesperre_pruefen.py` | 23, 34 |
| `pruefung/nachgang_n2_n3.py` | 96 |
| `tests/test_eichproben.py` | 16, 42, 71 |
| `tests/test_review_vertrag.py` | 18 |
| `tests/test_vorspann.py` | 12, 31, 32, 33, 34, 56 |
