# Außerhalb Kern — bestätigt offen

19 benannte Leserorte in 14 Dateien; davon 11 historische Prüfdateien und 8 weitere Produktleserorte. Keine Fehleranzahl des gesamten Biotops. Alle Einträge sind offen für einen eigenen Folgeauftrag; kein Quarantäne-Teilfix gilt als Erledigung. Bestätigungsart und Originalquelltext stehen pro Eintrag in JSON.

## B05:O01 — Positive Text-/Messmarker werden trotz fehlendem Laufabschluss verwertet

`biotop/organe/aufnahme.py:133–160` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: Ausgabe enthält erwartete positive Tokens, während rc/zeitlimit nicht hinreichend an die Wertung gebunden sind
- Grenze: Versiegelte Kerneingrenzung02: Aufnahme/Gen0-Produzenten und leere Herstellerantwort nicht integrieren; kein Durchgriff auf P4-Freeze-Erfolgsbindung.
- Originalbeleg: audit/LESESTELLEN.json, O01; SHA 07962eaf683821cc36c2d2177254fc92019219a20f22eb47048a8f556a24a312.

## B05:P11 — Positive Text-/Messmarker werden trotz fehlendem Laufabschluss verwertet

`pruefung/funde_neubewerten.py:23–43` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: Ausgabe enthält erwartete positive Tokens, während rc/zeitlimit nicht hinreichend an die Wertung gebunden sind
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P11; SHA f440849193d804545cacd537dffff6735c670f6d3b408533ddf89003503489fa.

## B05:P37 — Positive Text-/Messmarker werden trotz fehlendem Laufabschluss verwertet

`pruefung/tor1_f2.py:24–71` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: Ausgabe enthält erwartete positive Tokens, während rc/zeitlimit nicht hinreichend an die Wertung gebunden sind
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P37; SHA 8a12748e174e8f742857b0be21633934a07fad2e180e609573d29b490e9484dd.

## B06:G01 — Beliebiger Fehlerexit zählt als gefangener Mutant

`biotop/organe/generation0.py:108–113` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: rc!=0 wird in Erfolg der negativen Kontrollprobe umgedeutet
- Grenze: Versiegelte Kerneingrenzung02: Aufnahme/Gen0-Produzenten und leere Herstellerantwort nicht integrieren; kein Durchgriff auf P4-Freeze-Erfolgsbindung.
- Originalbeleg: audit/LESESTELLEN.json, G01; SHA f18e98e98977adf0010aa6cf10b7a353d1f77c99a8b855033f9ae3fb86edde8f.

## B06:G03 — Beliebiger Fehlerexit zählt als gefangener Mutant

`biotop/organe/generation0.py:180–200` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: rc!=0 wird in Erfolg der negativen Kontrollprobe umgedeutet
- Grenze: Versiegelte Kerneingrenzung02: Aufnahme/Gen0-Produzenten und leere Herstellerantwort nicht integrieren; kein Durchgriff auf P4-Freeze-Erfolgsbindung.
- Originalbeleg: audit/LESESTELLEN.json, G03; SHA f18e98e98977adf0010aa6cf10b7a353d1f77c99a8b855033f9ae3fb86edde8f.

## B06:G04 — Beliebiger Fehlerexit zählt als gefangener Mutant

`biotop/organe/generation0.py:243–255` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: rc!=0 wird in Erfolg der negativen Kontrollprobe umgedeutet
- Grenze: Versiegelte Kerneingrenzung02: Aufnahme/Gen0-Produzenten und leere Herstellerantwort nicht integrieren; kein Durchgriff auf P4-Freeze-Erfolgsbindung.
- Originalbeleg: audit/LESESTELLEN.json, G04; SHA f18e98e98977adf0010aa6cf10b7a353d1f77c99a8b855033f9ae3fb86edde8f.

## B07:G02 — Keine Äquivalenzbeobachtung wird als identischer Beobachtungsnachweis gelesen

`biotop/organe/generation0.py:151–174` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: Äquivalenz wird ohne nichtleere Beobachtungspopulation behauptet: abgeschnittener Fehlmarker oder ignorierter n=0-Zähler
- Grenze: Versiegelte Kerneingrenzung02: Aufnahme/Gen0-Produzenten und leere Herstellerantwort nicht integrieren; kein Durchgriff auf P4-Freeze-Erfolgsbindung.
- Originalbeleg: audit/LESESTELLEN.json, G02; SHA f18e98e98977adf0010aa6cf10b7a353d1f77c99a8b855033f9ae3fb86edde8f.

## B08:L06 — Leere Nachbarantwortliste zählt als einstimmige Bestätigung

`biotop/lauf.py:554–560` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: all(ids) wird ohne Existenz eines ausgeführten Antwort-/Prüfobjekts ausgewertet
- Grenze: Versiegelte Kerneingrenzung02: Aufnahme/Gen0-Produzenten und leere Herstellerantwort nicht integrieren; kein Durchgriff auf P4-Freeze-Erfolgsbindung.
- Originalbeleg: audit/LESESTELLEN.json, L06; SHA d00993cdbac4f9f686c0582f36ff118225f0efab7e2f7c73f797de75d68cecd2.

## B09:P41 — Fehlendes Paarmaß/Vertragsergebnis zählt als bestanden

`pruefung/verhandlungsprobe.py:57–75` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: not dict.get(...) mit None/{} macht Nichtprüfung zur leeren gültigen Fehlermenge
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P41; SHA cf85cf5d39145fcd23ee81f470fbd0d183de967d5005645cd43db79df1077c85.

## B09:P46 — Fehlendes Paarmaß/Vertragsergebnis zählt als bestanden

`pruefung/proben_tor2.py:196–215` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: not dict.get(...) mit None/{} macht Nichtprüfung zur leeren gültigen Fehlermenge
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P46; SHA c750f9d6ceed4f7fe20d7678c99cebf4dbd55156959b79a4ba513c5c9f52ec69.

## B11:L08 — Gen0-Original-Gegenlauf wird nach Fehler ohne Testzuordnung fortgesetzt

`biotop/lauf.py:634–644` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: Fehlerexit bewirkt nur dateinamengestützte Bereinigung statt verbindlichen Abbruch/Nachweis
- Grenze: Versiegelte Kerneingrenzung02: Aufnahme/Gen0-Produzenten und leere Herstellerantwort nicht integrieren; kein Durchgriff auf P4-Freeze-Erfolgsbindung.
- Originalbeleg: audit/LESESTELLEN.json, L08; SHA d00993cdbac4f9f686c0582f36ff118225f0efab7e2f7c73f797de75d68cecd2.

## B12:L09 — Gen0-Ziel erreicht bei leerer nichtäquivalenter Population

`biotop/lauf.py:646–659` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: Anteilziel wird mit Nenner0 zu Ziel0 und gefangen>=ziel erlaubt 0>=0
- Grenze: Versiegelte Kerneingrenzung02: Aufnahme/Gen0-Produzenten und leere Herstellerantwort nicht integrieren; kein Durchgriff auf P4-Freeze-Erfolgsbindung.
- Originalbeleg: audit/LESESTELLEN.json, L09; SHA d00993cdbac4f9f686c0582f36ff118225f0efab7e2f7c73f797de75d68cecd2.

## B13:P02 — Leere Prüfpoulation erfüllt historisches lokales Gütekriterium

`pruefung/anklaeger_vielfalt.py:34–54` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: Leerer Nenner/Fehlerlisten ergeben BESTANDEN/ERFÜLLT ohne vorhandenen Prüfumfang
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P02; SHA 495b2f5494053acb7b6c12f1838b4e2a826db1c5fa4e5a867eb08398fa8e6bd8.

## B13:P29 — Leere Prüfpoulation erfüllt historisches lokales Gütekriterium

`pruefung/nachgang_n2_n3.py:117–168` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: Leerer Nenner/Fehlerlisten ergeben BESTANDEN/ERFÜLLT ohne vorhandenen Prüfumfang
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P29; SHA 6e15cc6301298fb7ba2bed3290f270510af91598f2cd6d0b175628727cfb9b27.

## B13:P27 — Leere Prüfpoulation erfüllt historisches lokales Gütekriterium

`pruefung/nachgang_n10.py:49–99` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: Leerer Nenner/Fehlerlisten ergeben BESTANDEN/ERFÜLLT ohne vorhandenen Prüfumfang
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P27; SHA ee1a249f47a625fa1f8a17a11d3a1c4d48a37ad56d1304cdb1d186b947e9bbc5.

## B14:P16 — Nicht ausgeführte Durchrutscherprüfung wird als gemessen ausgegeben

`pruefung/lauf25_auswertung.py:37–108` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: Leere Ergebnisliste bleibt durch for/pass unverändert und wird als berechneter Nullbefund etikettiert
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P16; SHA 23649a8229beccf2991bc01b0fcea01dd6a277eac08a508f4f96188b7c4b6581.

## B15:P08 — Fehlmessung kann historische negative Eichkontrolle erfüllen

`pruefung/eichung_falld.py:34–41` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: not lauf_startet wird ohne Nachweis der beabsichtigten Rauschursache als bestanden gewertet
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P08; SHA 45fe97d0678493fe3e482fdfc276800ac77f3541528cd777923fc582622d0cd8.

## B15:P09 — Fehlmessung kann historische negative Eichkontrolle erfüllen

`pruefung/eichung_pruefen.py:19–50` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: not lauf_startet wird ohne Nachweis der beabsichtigten Rauschursache als bestanden gewertet
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P09; SHA 287d4795bab9016e91e448084c38cb4ba9312e07ec052cb35f682739309ceee3.

## B16:P38 — Historische rote-Testzählung verdeckt nicht ausgeführte Tests

`pruefung/tor2.py:39–112` (Originalstand)

- Status: **bestätigt offen**, nicht repariert.
- Bestätigung: statisch bestätigter Quell-Kontrollfluss; kein von diesem Elternabgleich ausgeführter Biotop-Fall
- Mechanismus: rc0 wird bei Rotzählung wie vollständige Testausführung behandelt
- Grenze: Historischer Parallelprüfer ohne Rückfluss in aktuellen Pflichtvorspann
- Originalbeleg: audit/LESESTELLEN.json, P38; SHA 5395ddd65e65366440c534b27ef1de3b8d1a8aed41d3d3a529a725fd71ce614b.

Die vier bestehenden P4-Mechanismen bleiben eine separate offene Liste. Acht semantische Originalkandidaten und45 breite Quellzeilen sind weiterhin ungeklärt; außerdem steht der Aufnahmestart-Hinweis des Verbraucherteils getrennt, nicht als bestätigter Fehler. Keine Vollständigkeitsentwarnung.
