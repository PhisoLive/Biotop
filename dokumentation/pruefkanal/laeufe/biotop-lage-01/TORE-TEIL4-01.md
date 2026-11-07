# BIOTOP-LAGE-01 · Fassung 2 · `TORE-TEIL4-01.md`

- **Inhalt:** FK24, FK27–FK29 · Entwurf C, Stück 4 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil C, Arbeitszeit 25.09.2026 16:10:47–17:22:12 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/tore/TORE-TEIL4.md` · 18118 B · SHA-256 `90db8e0e23ce59d7bf284fb8486581eae1b6f714d9594d0dbf77623c8d0cf454`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (0 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# TORE — Teil 4 von 4: FK28, FK29, Lücken und Widersprüche

Stand des Lesens: 25.09.2026, 16:11–17:10 CEST. Die Lesehilfe steht in Teil 1, Q1–Q7 in Teil 2 §1. Dieser Teil enthält
keine Torwertung.

**Datenbankzugriff**
- Alle Abfragen stehen wörtlich in den Rohbelegen: Skript `tore/c5_fk28_fk29.py` in R63, `tore/c6_ergaenzung.py` in R69, `tore/c7_ergaenzung2.py` in R73.
- STAMM (`/root/biotop/daten/biotop.db`) wurde nur mit `?mode=ro&immutable=1` geöffnet. Die -wal-Datei hatte vor und nach
  jeder Abfrage 0 Bytes (R58, R63, R69).
- VB1 (`/root/phase-4-vorbedingung-1/privat/biotop.db`) und T3 (`/root/biotop-t3/t3.db`) wurden mit `?mode=ro` geöffnet.
  Die -wal-Dateien hatten 4.140.632 bzw. 13.221.112 Bytes, vorher und nachher gleich (R63). Der Zweig R02 wurde für FK28
  und FK29 nicht abgefragt.
- Zeitstempel aus der Datenbank sind UTC.

## 1. FK28 — Aufnahmesperre C

**Was sie ist.** Code im heutigen Arbeitsbaum, `biotop/organe/aegis.py:997–1002`, gelesen am 25.09. gegen 16:50:
„# Aufnahmesperre C (F7): der Schlüssel des GESCHRIEBENEN Tests gegen den Vorrat, vor der Aufnahme.“ Es gibt zwei
Aufnahmestellen, `fund` und `norm` (ABNAHME vom 20.09., Z. 45–46).

**Stand 20.09., im Wortlaut**
- ABNAHME Z. 79: „C hat im **natürlichen Betrieb** nie eine Doppelung abgefangen — alle Belege sind gestellte Gegenstände
  | Tor 4 am echten Werk“.
- WIEDEREINSTIEG (`dok/2026-09-20_045401_…`) Z. 61: „**Die Abnahme gilt eng.** C hat im natürlichen Betrieb **nie** eine
  Doppelung abgefangen. Alle Belege stammen aus gestellten Gegenständen, die durch den laufenden Kern gingen.“
- MASTERPROMPT_Lauf-25 Z. 67: „Der Unterschied, auf den es ankommt, ist nicht „natürlich gegen gestellt", sondern **„durch
  den laufenden Pfad gegen offline rekonstruiert"**.“

**Abfragen** (R63 §A und §B, wörtlich):
- `SELECT nr, zeit, inhalt FROM protokoll WHERE art='immun.aufnahme_gesperrt' ORDER BY nr`
- je Sperrung `SELECT ist_probe, generation, nische, status FROM kandidaten WHERE id=?`
- `SELECT inhalt FROM protokoll WHERE art='immun.aufnahme_geprueft'` (je Lauf summiert über das Feld `anzahl`)

**Ergebnis je Lauf** (abgelesen; T3 enthält die Zeilen von STAMM bis Lauf 25, VB1 ebenso):

| Zweig | Lauf | geprüfte Tests | gesperrt | Einordnung | Beleg für die Einordnung |
|---|---|---|---|---|---|
| STAMM, VB1, T3 | 9901 | keine Zeile `aufnahme_geprueft` | 2 (#15227, #15228) | gestellt | Kandidat 9999 steht nicht in `kandidaten`; Lauf 9901 steht nicht in `laeufe` (höchste ids: STAMM 25, 24, 23; T3 38, 37, 36; R63 §J) |
| STAMM, VB1, T3 | 9902 | 1 | 1 (#15229) | gestellt | Kandidat 9998 wie oben |
| STAMM, VB1, T3 | 25 („Lauf C“) | 9 | 5 (#16011, #16015, #16020, #16023, #16027) | gestellt | Testnamen `test_rot_wiederholt_vorhandene_behauptung`, `test_rot2_preis_fuer_wiederholte_behauptung`; ABNAHME Z. 79; Kandidat 2680 ist in STAMM entfernt (dort ist 2679 die höchste id, R69 §4) |
| VB1 | 26 | 3 | 0 | natürlich, 0 Fänge | — |
| T3 | 32 | 8 | 1 (#16946, K2690) | natürlich | `ist_probe` 0, Generation 1, Nische `schnell` |
| T3 | 36 | 4 | 1 (#18149, K2743) | natürlich | `ist_probe` 0, Generation 1, `sicher` |
| T3 | 37 | 14 | 2 (#20745 K2840, #21446 K2906) | natürlich | `ist_probe` 0, Generationen 2 und 5 |
| T3 | 38 | 17 | 5 (#22983 K3036, #23044 K3043, #23638 K3091, #25807 K3283, #26082 K3307) | natürlich | `ist_probe` 0, Generationen 1, 1, 4, 14, 16 |

**Zusammengezählt**
- Gestellte Fänge: 8 Sperrungen in den Läufen 9901, 9902 und 25 (g: 2 + 1 + 5).
- Natürliche Fänge bis 20.09. (Stamm): 0.
- VB1 Lauf 26: 0 natürliche Fänge von 3 geprüften Tests.
- T3 Läufe 32–38: 9 natürliche Fänge von 43 geprüften Tests (g: 1 + 1 + 2 + 5 = 9; 8 + 4 + 14 + 17 = 43).
- Die 9 natürlichen Fänge in T3 im Einzelnen:
  - Sperrart: 8 `norm`, 1 `fund` (#25807).
  - Grund: 8 × „bereits im Vorrat des Bereichs“, 1 × „zweiter Test derselben Behauptung in diesem Kandidaten“ (#26082).

**Einordnung „natürlich“ (Auslegung Hermes).** Als natürlich gilt eine Sperrung, die im laufenden Lauf an einem Kandidaten
des Schwarms entstand. Merkmale: `ist_probe` 0, Generation ≥ 1, eine Nische des Schwarms, kein gestellter Testname.

Grenzen dieser Einordnung:
- **Kennungsvergabe:** Der Kandidat 2680 ist in VB1 und T3 ein anderer Kandidat (VB1: Lauf 26; T3: Lauf 31; R69 §4). Die
  Kandidatenfelder, die R63 §A für die Lauf-25-Zeilen in VB1 und T3 zeigt, gehören deshalb nicht zu den Sperrungen von
  Lauf 25. Die Einordnung von Lauf 25 stützt sich nicht auf sie.
- **Echtheit der Doppelung:** Ob die gesperrte Behauptung inhaltlich eine Doppelung des Vorrats ist, wurde NICHT GEPRÜFT.
  Weg: den Vorrat des Bereichs zur Zeit der Sperrung aus `immunsystem` und `aegis.ansage` abfragen.
- **Eigene Ansage (A33):** Auslegung Hermes: Die Selbstsperre an der eigenen Ansage ist über den Parameter
  `eigene_ansage_nr` behoben (`bb8eb0f`, 21.09. 12:08:57 +0200, R97). Dieser Stand liegt vor allen T3-Kernständen ab
  `e259e9f` (R105), also vor den Läufen 32–38. Ob einer der 9 Fänge eine Selbstsperre ist, wurde NICHT GEPRÜFT.
- **Läufe ohne Abnahme:** Die Läufe 32 und 36 gehören zu den elf T3-Läufen „ohne Abnahme“ (Q5 Z. 144).

**Wie die Berichte die T3-Werte deuten** (ABSCHLUSS-03 §4e):
- Die Aufnahmesperre C ist eine „Diagnose“: Lauf 37 2 von 14 = 14,3 %, Lauf 38 5 von 17 = 29,4 %. Das stimmt mit der
  Datenbank überein.
- „NACHTRAG-6 nannte stattdessen die Aufnahmesperre C die Torzeile.“
- Chat-Claude (v8 Z. 10): „(2) die Sperrquote der Aufnahmesperre (14 %) als erfüllte Doppelungs-Torzeile bestätigt — sie
  ist eine Diagnose“.
- In v8 Tor 4, Zeile 8 steht: „Ansagefilter und Aufnahmesperre werden als Diagnosen mitgeführt, sind aber nicht die
  Torzeile.“

## 2. FK28 — Abweichungsquote zwischen Ansage und Ausführung (V9)

**Regel, im Wortlaut**
- PRUEFUNG4 (20.09.) Z. 101: „**V9 bleibt, aber als Messung, nicht als Tor:** Die Abweichungsquote Ansage ↔ Ausführung
  wird gezählt und berichtet. Sie sagt etwas über die Verlässlichkeit des Anklägers. Sie ist kein Sperrmechanismus.“
- PRUEFUNG4 Z. 120: „| Abweichungsquote Ansage ↔ Ausführung | **gezählt, keine Grenze** | Diagnostisch. …“
- In v7 und v8 ist dafür keine Torzeile gefunden. Die Suche nach „Abweichungsquote“ in v8 ergab 0 Treffer.

**Gemessen: ja.** Die Werte:

| Quelle | Lauf | Wert | Bezugsgröße |
|---|---|---|---|
| PRUEFUNG3 Z. 60 (20.09.): „Der Zusatzbefund zur Ansage-Abweichung nennt „1 von 2"“ | erster VB1-Durchgang | 1 von 2 | NICHT ERHOBEN |
| TORZEILEN.json (Q4), `ansageabweichung_eigener_auftrag_nach_vorbedingung2` | VB1 Lauf 26 | 9 von 11 | 11 = Nenner laut Beleg; die Grundlage steht in ERGEBNIS-DETAIL.md, NICHT GELESEN |
| V9-Zähler `aegis.abweichung`, STAMM und VB1 | 25 | 1 von 1 Zeilen mit `abweichung` true | Zählerzeilen |
| V9-Zähler, VB1 | 26 | 0 Zeilen | — |
| V9-Zähler, T3 | 32 / 36 / 37 / 38 | 3 von 3 / 1 von 1 / 9 von 9 / 6 von 7 | Zählerzeilen |
| T3 Läufe 32–38 zusammen | | 19 von 20 (g: 3 + 1 + 9 + 6 = 19; 3 + 1 + 9 + 7 = 20) | Zählerzeilen |

Die Zählerwerte stammen aus der Abfrage `SELECT inhalt FROM protokoll WHERE art='aegis.abweichung'` (R63 §C).

**Bezugsgröße des Zählers (Auslegung Hermes).**
- Im heutigen Code schreibt `aegis.py:1003–1022` die Zeile `aegis.abweichung` nur, wenn aus dem Angriff ein Immuneintrag
  entsteht. Die Zeile steht innerhalb von `if gefunden:` und `if code_immun:`.
- Nenner des Zählers sind also die Angriffe mit aufgenommenem Fund, nicht alle Angriffe. Das erklärt, warum Lauf 26 keine
  Zählerzeile hat, der Bericht aber 9 von 11 nennt.
- Ob der Code zur Zeit der Läufe derselbe war, wurde NICHT GEPRÜFT. Weg: `git show <Kern des Laufs>:biotop/organe/aegis.py`.
- In den T3-Berichten und den Berichten `biotop-vor-t4*` kommt „Abweichungsquote“ nicht vor (0 Treffer, R73 §4).
  Berichtet ist sie für T3 nicht, nur gezählt.
- Philipp am 20.09. (PH Z. 353): „… dass 9 von 11 Angriffstests von ihrer eigenen Ansage abweichen — das entwertet die
  Vorab-Ansage als Filter …, gehört aber in einen eigenen Auftrag nach Vorbedingung 2.“ Dieser eigene Auftrag ist NICHT
  GEFUNDEN.

## 3. FK29 — Art- und Projektgedächtnis

**Abfragen** (R63 §E, §F, §G, wörtlich):
- Artgedächtnis: `SELECT werk, werkklasse, count(*), sum(CASE WHEN muster IS NOT NULL AND trim(muster)<>'' THEN 1 ELSE 0 END), count(DISTINCT lauf_id), min(erstellt_am), max(erstellt_am) FROM artgedaechtnis GROUP BY werk, werkklasse ORDER BY werk`
- Projektgedächtnis: `SELECT werk, count(*), count(DISTINCT lauf_id), min(lauf_id), max(lauf_id), min(erstellt_am), max(erstellt_am) FROM projektgedaechtnis GROUP BY werk ORDER BY werk`
- Mentor: `SELECT id, lauf_id, werk_id, erstellt_am, modell, richtungen FROM mentor ORDER BY id`. Werkübergreifend heißt:
  Das Feld `_verweise_werkuebergreifend` der Richtung ist nicht leer.

**Einträge je Werk** (abgelesen):

| Werk (Werkklasse) | Artgedächtnis: Einträge, davon mit Muster, Läufe | Projektgedächtnis: Einträge, Läufe | letzter Eintrag |
|---|---|---|---|
| `lagerhaus` (python/klein/bibliothek), STAMM und T3 | 569, 15, 8 | 587, Läufe 13–25 (8 verschiedene) | 2026-09-20T01:43:33Z |
| `lagerhaus`, VB1 | 639, 18, 9 | 650, Läufe 13–26 (9 verschiedene) | 2026-09-20T20:16:10Z |
| `logmuehle` (python/klein/bibliothek), alle Zweige | 130, 7, 2 | 99, Läufe 17–23 (2 verschiedene) | 2026-09-19T22:39:47Z |
| `versandwerk` (typescript/klein/bibliothek), nur T3 | 495, 28, 4 | 423, Läufe 32–38 (4 verschiedene) | 2026-09-22T19:26:11Z |
| Summe STAMM / VB1 / T3 | 699 / 769 / 1.194 | 686 / 749 / 1.109 | |

Rechnung (g):
- Artgedächtnis VB1 − STAMM = 639 − 569 = 70 Einträge `lagerhaus` aus Lauf 26.
- Artgedächtnis T3 = 569 + 130 + 495 = 1.194.
- Projektgedächtnis T3 = 587 + 99 + 423 = 1.109.
- T3 enthält die VB1-Einträge von Lauf 26 nicht.

Ergebnisse der Artgedächtnis-Einträge in T3: 1.053 abgelehnt, 54 angenommen, 87 überlebt (Summe 1.194).

**Verworfene Kandidaten ohne Kammerlauf** (Protokollart `gedaechtnis.wiederholung`, als Lauf: Anzahl):
- STAMM: 16: 21, 17: 17, 18: 13, 19: 18, 20: 9, 22: 18, 23: 3, 24: 11, 25: 18.
- VB1: dazu 26: 17.
- T3: dazu 32: 4, 36: 5, 37: 28, 38: 52.

**Belegte Richtungen (Mentor)**

| Aufruf (id) | Lauf, Werk | erstellt (UTC) | werkübergreifend | Verweise |
|---|---|---|---|---|
| 1–9 | Läufe 16–22, `lagerhaus` und `logmuehle` | 19.09. 12:00–21:32 | je 0 (4 oder 5 Richtungen je Aufruf) | — |
| 10 | 23, `logmuehle-23` | 19.09. 21:33:52 | 2 von 5 | A132, A141, A249, A359, A6 |
| 11 | 22, `lagerhaus-p3-22` | 19.09. 22:45:33 | 3 von 4 | A270, A271, A568, A569, A597 |
| 12 | 24, `lagerhaus-zeile8-24` | 19.09. 23:00:43 | 1 von 5 | A569, A597 |
| 13 | 25, `lagerhaus-c-25` | 20.09. 01:15:08 | 1 von 5 | A569, A597 |
| 14 (nur VB1) | 26, `lagerhaus-vorbedingung1-26` | 20.09. 19:36:38 | **3 von 5** | A270, A281, A568, A569, A597 |

- Über alle 14 Aufrufe in VB1 (g): 63 Richtungen, davon 10 mit werkübergreifendem Verweis.
  - Richtungen je Aufruf: 4+5+5+4+5+4+4+4+4+5+4+5+5+5 = 63.
  - Werkübergreifend: 2+3+1+1+3 = 10.
  - STAMM ohne id 14: 58 Richtungen, davon 7.
- **Letzter Nachweis:** Aufruf 14 in VB1, Lauf 26, 3 von 5. Das stimmt mit TORZEILEN.json (`richtungen_mit_fremdverweis`
  3, `richtungen` 5), mit PH Z. 353 („3 von 5“, 20.09.) und mit v8 Z. 18 („Artgedächtnis 3 von 5 Richtungen mit
  werkübergreifendem Verweis“, Abnahme 21.09.) überein.
- **T3:** Es gibt keinen Mentor-Aufruf. Die Tabelle `mentor` hat in T3 dieselben 13 Zeilen wie STAMM; `laeufe.richtung` ist
  für die Läufe 36–38 leer (R63 §G, §J). Ein Nachweis am Werk `versandwerk` ist NICHT VORHANDEN.
- **Erfundene Verweise:** Die gespeicherten Richtungen haben kein Feld dafür („erfunden Feld fehlt“ in 14 von 14
  Aufrufen). Aus der Datenbank ist die Zahl NICHT ERHEBBAR. Berichtet sind „0“ für Phase 3 (Q3 Z. 79–92) und „0 erfunden“
  für den Nachlauf (v8 Z. 410). Für VB1 NICHT GELESEN.
- **Vorbehalt:** Aufruf 11 hängt an Lauf 22. Die Zahlen der Läufe 22 und 23 stehen „wegen des Satz-2-Verstoßes unter
  Vorbehalt“ (PH Z. 317, 20.09.).

## 4. Lücken (Vorschlag für die Lückenliste)

1. **Nachmessung von Lauf 26 nach der T3-Methode**, verlangt in PH Z. 428 (22.09.): NICHT GEFUNDEN. ABSCHLUSS-03 nennt Lauf 26
   in §4e nicht. NACHTRAG-6 übernimmt „1 von 11“ aus TORZEILEN.json. Weg: Hermes fragt nach oder sucht in `abschluss-03/`
   (`NACHZAEHLUNG-ABSCHLUSS3.txt`).
2. **Die Grenze „ungemessen unter 20 erzeugten Tests“** (20.09., Teil 1 §5) steht nicht in v7 oder v8. Ob sie für den
   zweiten VB1-Durchgang galt, ist in den gelesenen Quellen nicht ausgesprochen (siehe W5).
3. **T3-Zeilen ohne Quelle:** Zeile 1 (Aufnahme) NICHT GELESEN; Lauf 38 „Kein Rückschritt“ NICHT GEFUNDEN; Endgrund von
   Lauf 38 NICHT GEFUNDEN (Status `bereit`, `beendet_am` leer). Weg: `biotop-t3-typescript/lauf38*`, `abschluss-02` §4.
4. **Fünf Messgerätfehler aus der v8-Liste** ohne gelesenen Einzelstand: Referenzlast zu kurz, keine Aufwärmung, Median aus
   drei, Ausfall-Blockade, Budgetgrenze nie scharf. Weg: `biotop-t3-typescript/uebernahme-01/ZWISCHENBERICHT.md` und die
   Lauf-Berichte 27–36.
5. **Einzelstand** der Befundgruppen A01–A33, B-01–B-24, C01, C02 (Bestandsaufnahme) und der Kennungen R5-1 … R5-14:
   NICHT ERHOBEN. Weg: die Abschlussordner von Reparatur 01 und 02 sowie die Vorher/Nachher-Tafel von Runde 5 mit den
   27 Fällen.
6. **Doppelte Kennungen in den Datenbankzweigen:**
   - „Lauf 26“ ist in VB1 der Lauf `lagerhaus-vorbedingung1-26` (20.09.), in T3 der erste T3-Lauf (Vorspann
     „gescheitert“, 2026-09-21T03:46:45Z; R63 T3 §H).
   - Werk-id 23 ist in VB1 `lagerhaus-vorbedingung1-26` (R63 VB1 §G), in T3 das Werk der Läufe 32–38 (R63 T3 §A, §J).
   - Der Kandidat 2680 ist in STAMM entfernt und in VB1 und T3 neu vergeben (R69 §4).
   - Das betrifft CHRONIK und LAGE.
7. **Eigener Auftrag zur Ansageabweichung** (PH Z. 353): NICHT GEFUNDEN.
8. **Erfundene Mentor-Verweise** werden nicht gespeichert (§3).
9. **Tor 2 und Tor 3 haben je eine elfte Zeile**, die nicht im Tor-Block des Masterprompts steht (Teil 1 §3, §4).
10. **Runde 6:** kein Commit, keine Regression, kein Review (Stand 12:55). Die Stufe-2-Eichphase ist nur am Drahtwerk
    gelaufen. Den Endstand trägt Hermes nach.

## 5. Widersprüche zwischen Quellen (mit beiden Belegen, ohne Auflösung durch diese Offenlegung)

- **W1 Aufnahmesperre „0 von 0“.**
  - Hermes am 22.09. 15:18:58 (HP Z. 2778): „in der Aufnahmesperre finde ich in beiden Läufen 0 von 0, das Feld
    `doppelungen` ist in allen 160 Urteilen leer“. Dasselbe 15:25:05 (HP Z. 2800), von Philipp übernommen in PH Z. 428.
  - Dagegen die T3-Datenbank: Lauf 37 mit 14 geprüften Tests und 2 Sperrungen, beide vor dieser Meldung
    (2026-09-22T01:46:16Z, 02:59:33Z; R63). ABSCHLUSS-03 §4e nennt ebenfalls „2 von 14“. VB1 Lauf 26: 3 geprüft, 0
    gesperrt (R63).
  - Auslegung Hermes: Die Meldung las das Urteilsfeld `doppelungen`, nicht die Protokollarten der Sperre.
- **W2 T3 Lauf 38, Schwächen.**
  - ABSCHLUSS-03 §4c (23.09.): „4 von 5 = 80 %“.
  - `biotop-vor-t4-02/BERICHT.md` Z. 98, 101: „3 von 5 = 60 %“ und „Der T3-Befund „Lauf 38: 4 von 5 = 80 %“ ist damit
    falsch“.
  - `biotop-vor-t4-04/BERICHT.md` Z. 173: doppelte Prüfung „0 von 5“, „keine Neubewertung von T3“.
- **W3 Phase 2, Zeile 8.**
  - Bericht Phase 2: „237 Angriffstests, 6 Doppelungen = **2,5 %**“.
  - v5 Z. 17: „83,6 %“.
  - Nachlauf §5 und v6/v8: „68,5 %“.
  - Die Quellen erklären die Reihe selbst (v8 Z. 390; Nachlauf §5).
  - Bezugsgröße der 2,5 % uneinheitlich:
    - Bericht Phase 2: „237 Angriffstests“;
    - v5 Z. 323: „gegen 240 Ablehnungen statt gegen 55 erzeugte Tests“;
    - v8 Z. 390: „… statt gegen 54 erzeugte Tests“;
    - Nachlauf §5: Lauf 13 mit 54 erzeugten Tests.
- **W4 Tor-2-Proben „wieder belegt, 4 von 4“.**
  - v8 Z. 29 und Z. 390 (23.09.): „wieder belegt (4 von 4 mit gehärteten Proben)“.
  - PH Z. 317 (20.09. 15:28:25): „Wertungen, die ich zurücknehme: die Norm-Zeile aus Tor 2 und „4 von 4 bestanden" aus dem
    Nachlauf waren ein leerer Durchlauf“.
  - Danach PH Z. 341 (20.09. 21:14:38): „Reparatur 02 abgenommen — alle vier Torzeilen erfüllt“.
  - v8 nennt weder die Rücknahme noch Reparatur 02 an dieser Stelle.
- **W5 Nenner von Tor 2 Zeile 8 in Vorbedingung 1.**
  - Messgrenze vom 20.09. (PRUEFUNG2 Z. 114, PRUEFUNG3 Z. 108, PRUEFUNG4 Z. 134, ABNAHME Z. 123): „ungemessen unterhalb von
    20 erzeugten Tests/Funden“.
  - Messwert der Abnahme vom 21.09.: Nenner 11 (TORZEILEN.json `anzahl` 11; PH Z. 356 „bei unveränderten elf
    Testidentitäten: Tor 2 Zeile 8 ist damit erfüllt“).
  - Keine Wertung; siehe Lücke 2.
- **W6 T3 Lauf 37, Halluzinationsprobe.** NACHTRAG-02 zählt 3 Änderungen im sauberen Bereich, ABSCHLUSS-03 Z. 244 „**4 von
  6**, nicht 3“ (K2867 nachgetragen).
- **W7 Welche Zahl ist die Torzeile „Doppelungsanteil“ in T3?**
  - NACHTRAG-02 §3: „35,1 %, Schwelle 20 % gerissen“ (Ansagefilter als Torzeile).
  - NACHTRAG-6: Aufnahmesperre C als Torzeile.
  - ABSCHLUSS-03 §4e: „Torzeile: nicht gemessen“, beide Werte sind Diagnosen.
  - Chat-Claude benennt in v8 Z. 10 zwei eigene Fehler dazu.
- **W8 Mentor in Phase 3.**
  - Phase-3-Bericht (Q3 §2 Zeile 3, ab Z. 79; Auszug R31 Z. 251–253): „0 werkübergreifende Verweise von 4 bzw. 4 bzw. 4
    Richtungen“ (Läufe 18, 19, 20).
  - Datenbank: für Lauf 18 zwei Aufrufe mit 4 und 5 Richtungen (ids 4, 5), alle mit 0 werkübergreifenden Verweisen (R63).
    Welcher der beiden Aufrufe im Bericht gezählt ist, ist NICHT ERHOBEN.
  - PH Z. 74: „0 werkübergreifende Verweise von 12 Richtungen“.
- **W9 Titel und Befund in T3 (`1cf2eb1`).**
  - Commit-Titel: „Tor 2 Zeile 8 messbar machen“ (R105).
  - ABSCHLUSS-03 Z. 262: „Messbar wurde nur die Treffer-Teilmenge (9 von 87).“
