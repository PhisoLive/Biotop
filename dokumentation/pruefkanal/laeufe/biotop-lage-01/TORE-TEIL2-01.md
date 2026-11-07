# BIOTOP-LAGE-01 · Fassung 2 · `TORE-TEIL2-01.md`

- **Inhalt:** FK24, FK27–FK29 · Entwurf C, Stück 2 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil C, Arbeitszeit 25.09.2026 16:10:47–17:22:12 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/tore/TORE-TEIL2.md` · 20115 B · SHA-256 `42f2487b470a547ece1659f373a75e709076b4bfdf2ffcf296f52e599fd851d7`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (8 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# TORE — Teil 2 von 4: FK24, Tafel aller Torzeilen

Stand des Lesens 25.09.2026, 16:11–17:00 CEST. Lesehilfe und Wortlaute: Teil 1. Keine Torwertung.
Spalten: Grenze (aus dem Wortlaut, Teil 1) · letzter Messwert mit Bezugsgröße, abgelesen (a), sonst gekennzeichnet ·
Quelle · Datum. Chat-Claudes Wertungen stehen je Tor im Abschnitt dahinter (§2–§7) und nur als Zitat.

## 1. Tafel

**Tor 1** — Werk `lagerhaus`. Letzte Messung im Phase-1-Nachlauf: Lauf 9, Kasse Lauf 10; „erledigt … 19.09.2026 02:20“
(v8 Z. 372). In v2 Z. 254 hieß dieser Nachlauf „Lauf 3“.
Quelle Q1 = `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/BERICHT.md` §1 (Auszug in R31 §2).

| Zeile | Grenze | letzter Messwert (a) | Hermes-Ergebnis |
|---|---|---|---|
| 1.1 Landkarte | 4 von 4 Bereichen; n von n Straßen | 4 von 4 Bereichen; 13 von 13 Straßen (Hermes-Zählung aus Phase 1) | bestanden |
| 1.2 Schwächen | ≥ 4 von 5 behoben; Kernmaß gestiegen | 4 von 5 (S1, S3, S4, S5; S2 offen); Kernmaß F2 −5 → 0; S1: bandit B307 3 → 0 Punkte, Befundklassen-Immuntest 6 von 6 bestanden | bestanden |
| 1.3 Kein Rückschritt | 0 von n | 0 von 4 angenommenen Generationen (1, 2, 5, 6) | bestanden |
| 1.4 Halluzinationsprobe | 0 | 0 von 12 Kandidaten in `bericht` angenommen | bestanden |
| 1.5 Lazarus | n von n | im Nachlauf nicht neu gemessen, Prüfsumme `lazarus.py` vorher = nachher; Messwert aus Phase 1 NICHT GELESEN | gilt weiter |
| 1.6 Kasse | Abbruch vor dem nächsten Modellaufruf | Lauf 10: Abbruch vor Generation 2, Protokoll #2623; danach 0 Buchungen, 0 `modell.aufruf` | neu gemessen, bestanden |
| 1.7 Laut scheitern | 0 Generationen | nicht neu gemessen (`aufnahme.py` unverändert) | gilt weiter |
| 1.8 Kammer | gescheitert, Wirt unberührt | nicht neu gemessen (`kammer.py` unverändert) | gilt weiter |
| 1.9 Anmeldung | jede Route → 401 | nicht neu gemessen (`anmeldung.py`, `dienst.py` unverändert); jüngere Messung an der Oberfläche: Zeile 3.9 | gilt weiter |

**Tor 2** — Werk `lagerhaus`, Lauf 13, 19.09.2026. Quelle Q2 = `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/BERICHT.md` §1 (Auszug R31 §2).

| Zeile | Grenze | letzter Messwert | Quelle |
|---|---|---|---|
| 2.1 Nischen | 4 aktiv, je ≥ 2 Anbieter; Gewichte nach 10 Generationen | 4 von 4 Nischen, je 4 von 4 Herstellern; Gewichte nach 14 Generationen; 235 `bandit.wahl`-Zeilen (a) | Q2 |
| 2.2 Generation 0 | ≥ 16 von 20 nach Generation 0 | vorher 16 von 20; nachher 17 von 20 (Lauf 12: 18 von 20); #7 und #19 äquivalent (a) | Q2 |
| 2.3 S2 | Kriterium der versiegelten Liste (Soll ≥ 50 %); Kernmaß nicht gesunken | `last_lager` 139,5 → 5,2 ms (−96 %); F2 0 → 0 (a) | Q2 |
| 2.4 Nebenwirkung | 0 von 1; Bericht nennt B | K1016: 0 von 1, nennt `bericht` (a). Jüngere Messungen derselben Probe als Eichprobe: Teil 3 §5 | Q2 |
| 2.5 Regression | 0 von 1; Einzeltest genannt | K1017: 0 von 1, Einzeltests genannt (a). Jüngere Messungen: wie 2.4 | Q2 |
| 2.6 Norm | offen, 0 Punkte, nicht im Werk | K1018 verworfen, nicht im Werk; in Lauf 12 rot (a). Nachlauf, Lauf 22: „0 Punkte, nicht im Werk“; am 20.09. zurückgenommen (§3). Jüngere Messungen: wie 2.4 | Q2; Nachlauf §2 |
| 2.7 Vertrag | ohne Anpassung abgelehnt; mit Anpassung angenommen **und im Werk** | ohne: K1019/K1020 abgelehnt; mit: Paar K1157/K1158 Verhandlung bestanden (#7251), nicht im Werk (a). Nachgeholt als Zeile 3.1 | Q2 |
| 2.8 Immunisierung, Doppelung | Anteil < 20 % der erzeugten Tests; 0 rote Tests | Lauf 13: 68,5 % (54 erzeugte Tests, 27 Behauptungen, größte Gruppe 8); gemeldet hatte Phase 2 „237 Angriffstests, 6 Doppelungen = **2,5 %**“; rote Tests nach 0 von 8 angenommenen Generationen (a). Nachlauf: Lauf 20 63,6 %, Lauf 22 54,5 % (je 11 erzeugte Tests). Jüngere Messungen: VB1-a, T3-7 | Phase-3-Nachlauf §5 (R31 §2); Q2 |
| 2.9 Verhandlung | ≥ 1 | 1 bestanden (#7251, durch die eingeschleuste Probe); 4 begonnen, 3 gescheitert (a) | Q2 |
| 2.10 Verlaufskurve | beigefügt | 8 angenommene Generationen, Endtestbestand 21 Dateien (a) | Q2 |
| 2.11 Modellwahl | am Katalog belegt | Katalog am 19.09. geprüft; Rauchtest je Modell (Lauf 11) (a) | Q2 |

**Tor 3** — Phase 3: Läufe 16–20, Werke `lagerhaus` und `logmuehle`, 19.09.2026. Nachlauf: Läufe 21–23, 19./20.09.
Quellen: Q3 = `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/BERICHT.md` (Zeilen angegeben); v8 = `dok/2026-09-23_155353_…-v8.md`.

| Zeile | Grenze | letzter Messwert | Quelle |
|---|---|---|---|
| 3.1 Nachprobe | Fall ohne Nachbar abgelehnt; Paar angenommen und im Werk | 2 von 2 korrekt abgelehnt; 1 von 1 angenommen und im Werk (K1164/K1165, #7500, Lauf 16 Generation 3; 103 von 103 Tests grün) (a) | Q3 Z. 54–64 |
| 3.2 Projektgedächtnis | 0 Wiederholungen von n | Lauf 20: 9 Kandidaten ohne Kammerlauf als Wiederholung verworfen (von 172 Kandidaten, davon 48 abgelehnt); Nachrechnung Hermes: 2 von 187 gescheiterten Wegen aus Lauf 13, 1 von 44 aus Lauf 16 (a) | Q3 Z. 66–77 |
| 3.3 Artgedächtnis | ≥ 1 Richtung mit benanntem Eintrag | Phase 3: 0 von 4, 0 von 4, 0 von 4 Richtungen (Läufe 18, 19, 20), 0 erfunden (a). Nachlauf: „2 von 5 Richtungen“ (a, v8 Z. 410). Datenbestand je Mentor-Aufruf: Teil 4 §3 | Q3 Z. 79–92; v8 |
| 3.4 Mentor | ≥ 3 Richtungen je Werk, Pflichtfelder | 5 Aufrufe (Läufe 16–20), je 4 bis 5 Richtungen; Pflichtfelder in allen vollständig (a) | Q3 Z. 94–99 |
| 3.5 Entropie | Sättigung spätestens nach Generation 6, Selbstende | `lagerhaus` Lauf 20: nach Generation 5, Status `gesaettigt`; `logmuehle` Lauf 17: nach Generation 8 (a) | Q3 Z. 101–107 |
| 3.6 Jury | 1 echter einstimmiger Fall; Uneinigkeit gestellt | 3 einstimmige Fälle aus echten Läufen; gestellte Gegenstimme → `gewinner: None` (#12361); gestellte Zielkonflikte: 5 von 5 einstimmig (a) | Q3 Z. 109–118 |
| 3.7 Geschmack | ≥ 7 von 10 | 10 von 10 (Mechanikprüfung) (a) | Q3 Z. 120–126 |
| 3.8 Archivierung | archiviert / gesamt, sonst Mechanikprüfung | Phase 3: 0 Archivierungen. Nachlauf: „hätten 4 von 5 Läufen archiviert; Mechanikprüfung belegt“ (a, v8 Z. 410) | Q3 Z. 128–135; v8 |
| 3.9 Oberfläche | jedes Element mit Stelle; 401 | 18 von 18 Routen → 401; 18 von 18 Bedienelemente mit Pfad und Zeile (a) | Q3 Z. 137–142 |
| 3.10 Aufschlüsselung | geht auf | Lauf 20: 172 geht auf; Lauf 17: 245; Lauf 13: 470 (a) | Q3 Z. 144–152 |
| 3.11 Verlaufskurven | beigefügt | Kurven `logmuehle` (Lauf 17) und `lagerhaus` (Läufe 16, 18–20) (a) | Q3 Z. 154–170 |

**Vorbedingung 1** (Phase 4, Werk `lagerhaus`). Zweiter Durchgang: Lauf 26, 20.09. 19:31:54–20:16:10 UTC (R63 VB1 §J);
enger Nachtrag 20./21.09. Quelle Q4 = `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-02/TORZEILEN.json`.

| Punkt | Grenze | letzter Messwert (a) | Quelle |
|---|---|---|---|
| VB1-a Tor 2 Zeile 8 | < 20 %; „ungemessen“ unter 20 erzeugten Tests (Teil 1 §5) | vorher 1 von 11 = 9,09 %; nachher, mit ausgeführtem K2689, 1 von 11 = 9,09 % ((g) 1 : 11 = 0,0909) | Q4 |
| VB1-b Artgedächtnis | ≥ 1 werkübergreifender Verweis | 3 von 5 Richtungen (Mentor-Aufruf Lauf 26; Datenbank: Teil 4 §3) | Q4 |
| VB1-c Reviewdurchgang | vollständig | `review_abgeschlossen` true, `review_bestanden` true | Q4 |
| VB1-d K2689 | ausgeführt; Gegenproben scheitern | korrigierte Ausführungen 2 von 2 bestanden; gültig fehlgeschlagene Gegenproben 2 von 2 | Q4 |

Im selben Beleg: `gesamtfreigabe_biotop` false. Die Wertungen des ersten Durchgangs (Läufe 24–25, Bauteile A, B, C)
stehen in §5.

**T3** — Werk `versandwerk` (TypeScript), Tor 4 nach v7, Läufe 37 und 38. Quellen: Q5 =
`https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-01/ABSCHLUSSBERICHT.md`; Q6 = `…/abschluss-02/NACHTRAG-02.md`; Q7 =
`…/abschluss-03/ABSCHLUSS-03.md` (Stand 23.09.).

| Zeile (v7) | Grenze | letzter Messwert | Quelle |
|---|---|---|---|
| T3-1 Aufnahme | gebaut, Bau- und Testlauf, versiegelte Schwächen | NICHT GELESEN (Teil C hat den Aufnahmebeleg von T3 nicht gelesen) | — |
| T3-2 Generation minus eins | 4 von 4 Proben, 4 von 4 Gegenproben scheitern | Werte in Teil 3 §5 | Q6 §5; R69; R73 |
| T3-3 Generation 0 | ≥ 80 von 100 | Lauf 37: 93 von 100 (arithmetik 11 von 11, boolesch 2 von 2, vergleich 21 von 22, zahlengrenze 59 von 65); das Typsieb verwarf 28 von 128 geprüften Mutanten; zwei Durchläufe mit je 100 von 100 neutral („nicht gemessen“, Q7 §5; Neutralzähler `generation0._testlauf` 400 von 600 geurteilt, Q5 Z. 74). Lauf 38: „83 → 93 von 100“ (a) | Q5 Z. 49–65; Q7 Z. 300–325 |
| T3-4 Schwächen | ≥ 80 % | Lauf 37: 3 von 5 = 60 % (Q6 §2). Lauf 38: gemeldet 4 von 5 = 80 % (Q7 §4c); berichtigt auf 3 von 5 = 60 %, S1 an K3044 nicht sauber behoben (`https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-02/BERICHT.md` Z. 98). Mit doppelter Prüfung, der Regel für künftige Werke: 0 von 5 in beiden Läufen, „Das ist eine Feststellung, keine Neubewertung von T3“ (`…/biotop-vor-t4-04/BERICHT.md` Z. 170–178) (a) | wie genannt |
| T3-5 Kein Rückschritt | 0 von n | Lauf 37: 0 in drei Kernmaßfeldern; die Laufzeit steigt 11-mal unterhalb der Rauschtoleranz (Q6 Z. 241). Lauf 38: NICHT GEFUNDEN (a) | Q6 |
| T3-6 Halluzinationsprobe | 0 Änderungen im Vergleichsbereich `zahlen` ohne Maßgewinn | Lauf 37: „In Lauf 37 waren es **4 von 6**, nicht 3“ (Q7 Z. 244, Korrektur zu NACHTRAG-02); Lauf 38: „3 von 8 angenommenen Generationen änderten den sauberen Bereich“ (Q7 Z. 238) (a) | Q7 §4d |
| T3-7 Doppelungsanteil | < 20 % der erzeugten Tests | nach der VB1-Methode nicht gemessen: Lauf 37 nicht rekonstruierbar; Lauf 38 Behauptung nur bei 9 von 87 aufgezeichnet, 0 Doppelungen unter den 9. Diagnosen: Ansagefilter 20 von 57 = 35,1 % (Lauf 37), 29 von 91 = 31,9 % (Lauf 38); Aufnahmesperre C: Teil 4 §1 (a) | Q7 Z. 252–262 |
| T3-8 Sättigung oder Budget | dokumentiert | Lauf 37: Status `gesaettigt`, Grund „In dieser Richtung gesättigt: Generationen 6–10, Verbesserung 0.00 % …“ (R63 T3 §J). Lauf 38: Status `bereit`, `beendet_am` leer (R63); Endgrund NICHT GEFUNDEN (a) | R63 |
| T3-9 Verbundausfall | ≥ 1 echter oder gestellter Ausfall | 114 echte Ausfälle (Läufe 29, 30, 35 je 1; Lauf 36: 75; Lauf 37: 36), je `beitraege=0` (a) | Q5 Z. 81–84 |
| T3-10 Reviewdurchgang | einer | REVIEW-03: 21 Befunde (3 hoch, 9 mittel, 9 niedrig) (a) | R69 §1 |
| T3-v8-9 Immunisierung TS | 0 Fälle = nicht belegt | `aegis._anhaengen` 0 von 0 in Lauf 37 und Lauf 38; Lauf 38: 0 von 11 Immuneinträgen als Datei im Endstand (a) | Q5 Z. 75; Q7 §4f |
| T3-v8-10 Neutralzähler | > Hälfte je Durchlauf | Lauf 37: `aegis.behauptung` 56 von 56, `gedaechtnis.aenderungsziel` 203 von 285, `generation0._testlauf` 400 von 600, `aegis._anhaengen` 0 von 0. Lauf 38: 51 von 51, 328 von 430, 400 von 400, 0 von 0; `verhaltensvergleich` 0 von 0, nicht eingehängt (a) | Q5 Z. 70–79; Q7 §4h |

**Tor 4 nach v8** (T4, Python): **kein Messwert**, T4 nicht begonnen.
- Stand laut `/root/biotop-vor-t4-06/UEBERGABE.md` (letzter Eintrag 12:55): Runde 6 läuft; Startregel für T4 in Z. 21–22.
- Das Tor-4-Skript berechnete in Runde 5 nur „Schwächen“, die übrigen Zeilen als „nicht berechnet“
  (`https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-05/BERICHT.md` §5, R31). Runde 6 baut alle Zeilen (UEBERGABE Z. 59–62).
- Verdrahtungs-Vorprüfung am Drahtwerk, 25.09. 10:19: „tor4 Schwächen 1 von 1“ (UEBERGABE Z. 208). Das Drahtwerk ist ein
  Prüfwerk der Regression, kein Testwerk; keine T4-Messung.

**Tor 5:** keine Zeile (Teil 1 §8).

## 2. Tor 1 — Wertungen
- v8 Z. 370 (gleichlautend ab v2 Z. 252): „**Stand Phase 1 nach Lauf 2 (Wertung Chat-Claude, 19.09.2026):** 7 von 9
  Zeilen bestanden. Zeile 2 nicht bestanden — S1 (`eval`) durch `__builtins__`-Leerung nur entschärft, Befund B307
  weiterhin vorhanden, …; damit 3 von 5 behoben. Zeile 3 formal bestanden, aber unter einer Formel, die Tests statt Werk
  belohnte. …“
- v8 Z. 372 (gleichlautend ab v3 Z. 269): „**Nachlauf zu Tor 1 — erledigt (Lauf 9, …, 19.09.2026 02:20):** Tor 1 **9 von 9
  bestanden**, geprüft durch Chat-Claude am Bericht (Summen nachgerechnet, Kurve Lauf 2 nachvollzogen). …“
- Begleitsatz am Ende von v3 (`dok/2026-09-19_022342_…-v3.md` Z. 347): „Tor 1 ist mit 9 von 9 abgenommen, Phase 1
  abgeschlossen …“

## 3. Tor 2 — Wertungen und Festlegungen (chronologisch)
- v4 Z. 302: „**Stand Phase 2 nach Lauf 13 (Wertung Chat-Claude, 19.09.2026):** **10 von 11.** Zeile 7 nicht erfüllt — das
  Probenpaar K1157/K1158 bestand die Vertragsprüfung, brachte 0 Kernmaß und wurde nach 3.5 verworfen; „angenommen" war
  zu „bestanden" umgedeutet. Alle übrigen Zeilen bestanden; Zeile 9 erfüllt wie geschrieben.“
- v5 Z. 17: „8, Phase 2: Zeile 8 **rückwirkend gerissen** (Doppelungsanteil 83,6 % gegen Grenze 20 %) — Wertung
  **9 von 11**. Gebaut bleibt gebaut; die Zahl wird nicht verhandelt.“
- PH Z. 124 (19.09. 22:56:23): „Zahl korrigiert übernommen: 68,5 % gemessen statt 83,6 % geschätzt, Zeile 8 bleibt
  gerissen, Grenze bleibt bei 20 %.“
- PH Z. 127 (19.09. 23:39:45): „… Bezugsgröße dazuschreiben, Zeile bleibt gerissen, Grenze bleibt.“
- v8 Z. 390 (gleichlautend v6 Z. 364, „Stand Fassung 6“): „**9 von 11.** … **Zeile 8 gerissen:** Doppelungsanteil **68,5 %**
  … gegen eine Grenze von 20 %; der ursprünglich gemeldete Wert von 2,5 % war gegen 240 Ablehnungen statt gegen 54
  erzeugte Tests gerechnet und prüfte die Fundstelle statt der Behauptung. … **Die Zeilen Nebenwirkung, Regression, Norm
  und Vertrag galten zwischenzeitlich als ungeprüft** … und sind im Nachlauf zu Phase 3 mit gehärteten Proben **wieder
  belegt, 4 von 4**.“
- PH Z. 317 (20.09. 15:28:25): „Wertungen, die ich zurücknehme: die Norm-Zeile aus Tor 2 und „4 von 4 bestanden" aus dem
  Nachlauf waren ein leerer Durchlauf (masse statt mass, norm=[]); die Zahlen aus den Läufen 22 und 23 stehen wegen des
  Satz-2-Verstoßes unter Vorbehalt, darunter die 54,5 %.“
- PH Z. 341 (20.09. 21:14:38): „Reparatur 02 abgenommen — alle vier Torzeilen erfüllt, Batterie beweisbar unverändert …“
  Die vier Torzeilen der Reparatur sind die vier Eichproben mit Gegenproben (Teil 3 §1).
- Zeile 8 danach: Tafel §1, Zeilen VB1-a und T3-7; Wertungen dazu in §5 und §6.
- Widerspruch: v8 Z. 390 enthält die Rücknahme vom 20.09. nicht (Teil 4 §5, W4).

## 4. Tor 3 — Wertungen
- PH Z. 74 (19.09. 19:28:40): „… Vorläufige Wertung: Artgedächtnis-Zeile nicht erfüllt (0 werkübergreifende Verweise von
  12 Richtungen — das Gedächtnis speichert Instanzen, übertragbar wären Muster; …“
- v5 Z. 343: „**Stand Phase 3 nach Lauf 20 (Wertung Chat-Claude, 19.09.2026, in Übereinstimmung mit Hermes):** **7 von 11
  voll, 2 teilweise, 2 nicht belegt.** Erfüllt: Nachprobe Zeile 7, Mentor, Entropie, Geschmacksmechanik, Oberfläche,
  Zerlegungen, Kurven beider Werke. Teilweise: Projektgedächtnis (…) und Jury (…).“
- v5 Z. 406 (Begleitsatz): „Phase 3 ist mit 7 von 11 abgenommen, deine Wertung war richtig …“
- PH Z. 136 (20.09. 00:55:54): „Nachlauf abgenommen, alle neun Punkte geprüft … Wertungen korrigiert: Phase 3 auf 8 von
  11 (Projektgedächtnis erfüllt — 0 von 3 Fällen durchgerutscht, deine Nachrechnung maß Token statt Ziele, das Organ hatte
  recht) …“
- v8 Z. 410 (gleichlautend v6 Z. 384, „Stand Fassung 6“): „**8 von 11 voll, 1 teilweise, 2 im Nachlauf erledigt.** …
  Teilweise: Jury (…). Im Nachlauf erledigt: **Artgedächtnis** (…) und **Archivierung** (…).“
- Vorbehalt: PH Z. 317 (20.09.) stellt die Läufe 22 und 23 des Nachlaufs unter Vorbehalt (§3).

## 5. Vorbedingung 1 — Wertungen (chronologisch)
**Erster Durchgang** (Läufe 24 und 25, Bauteile A, B, C), Dokumente in `dok/`:
- PRUEFUNG (20.09. 01:47:55) Z. 5: „**Wertung:** Bauteil A gebaut und mechanisch belegt, Wirkung auf Zeile 8 **nicht
  gemessen**. Bauteil B gebaut, Wirkung **nicht stabil belegt**.“
- PRUEFUNG2 (02:01:47) Z. 4: „**Wertung: noch nicht abgenommen.**“
- PRUEFUNG3 (02:25:43) Z. 4: „**Wertung: nicht abgenommen** — diesmal nicht wegen der Inhalte, sondern weil sie an der
  Abholadresse nicht liegen.“
- PRUEFUNG4 (02:46:30) Z. 4: „**Wertung: Vorbedingung 1 nicht erfüllt.** …“
- PRUEFUNG6 (04:00:48) Z. 4: „**Wertung: nicht abgenommen.** …“
- ABNAHME (04:50:16) Z. 4: „**Wertung: ABGENOMMEN.** Alle Punkte des Freigabetors aus Prüfung 6 sind belegt.“
- Danach die Bestandsaufnahme; PH Z. 317 (20.09. 15:28:25): „… deine Entscheidung, Vorbedingung 1 nicht zu starten, war
  richtig.“

**Zweiter Durchgang** (Lauf 26):
- PH Z. 353 (20.09. 22:55:04): „Wertung: nicht abgenommen, ich folge dir — beide Zahlen sind erreicht (9,09 % und 3 von
  5), aber das Review ist ohne Urteil abgebrochen und K2689 wurde nie ausgeführt; …“
- PH Z. 356 (21.09. 00:07:30): „Vorbedingung 1 abgenommen. K2689 ist richtig repariert — … Quote 9,09 % bei
  unveränderten elf Testidentitäten: Tor 2 Zeile 8 ist damit erfüllt, nach drei Runden, in denen sie gerissen war.“
- v8 Z. 18: „8: Vorbedingung 1 **abgenommen** (21.09.2026): Tor 2 Zeile 8 erfüllt mit 9,09 %, Artgedächtnis 3 von 5
  Richtungen mit werkübergreifendem Verweis.“

**Später:**
- Hermes, HP Z. 2800 (Meldung 22.09. 15:25:05): „Die 9,09 % aus Vorbedingung 1 („1 von 11") kann ich keiner Bezugsgröße
  zuordnen; in der Aufnahmesperre finde ich beidseitig 0 von 0.“
- PH Z. 428 (22.09. 15:32:32): „… die 35,1 % sind die Sperrquote des Ansagefilters, eine Diagnose, keine Torzeile, und mein
  Vergleich mit den 9,09 % war falsch, weil er zwei verschiedene Größen verglich. Such die Berechnung der 9,09 % im
  Abschlussordner von Vorbedingung 1; findest du sie nicht, miss Lauf 26 mit derselben Methode wie T3 — weicht das
  Ergebnis ab, ist die Abnahme von Tor 2 Zeile 8 wieder offen, und das gehört so in den Bericht.“
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-03/NACHTRAG-6-TOR2ZEILE8.txt` Z. 14: „Python Vorbedingung 1 Lauf 26: 1 von 11
  = 9,09 % (aus TORZEILEN.json)“. Für T3 Lauf 37 nennt dieselbe Datei als Nenner „0“ und „ANTEIL: nicht bestimmbar“.
- Eine Nachmessung von Lauf 26 mit der T3-Methode ist NICHT GEFUNDEN. Gesucht: „9,09“ im T3-Ordner, 3 Treffer, keiner
  davon eine Nachmessung; ABSCHLUSS-03 §4e nennt Lauf 26 nicht. Offen, Weg in Teil 4 §4 (Lücke 1).

## 6. T3 — Wertungen
- PH Z. 422 (22.09. 14:52:53): „T3 durchgelaufen, Zahlen nachgerechnet und stimmig — … Wertung Chat-Claude: nicht
  abgenommen, weil fünf Torzeilen aus Tor 4 im Bericht fehlen; …“
- PH Z. 425 (22.09. 15:15:11): „… Die Halluzinationsprobe hat getan, wofür sie gebaut ist: Sie hat gefangen, dass das
  Biotop die Messung optimiert statt den Code. Wertung Chat-Claude: T3 nicht abgenommen. …“
- PH Z. 443 (23.09. 15:53:55): „T3 sauber abgeschlossen — abschluss-03 ist der gründlichste Bericht bisher. …“
- v8 Z. 10: „**Fehler von Chat-Claude in T3, benannt:** (1) die Abwehr für wirksam erklärt, weil Gegenproben gegen das
  Modul liefen statt durch den Lauf; (2) die Sperrquote der Aufnahmesperre (14 %) als erfüllte Doppelungs-Torzeile
  bestätigt — sie ist eine Diagnose; (3) den Doppelungsvergleich 35 % gegen 9 % auf zwei verschiedene Größen gestützt; …“
- PH Z. 452 (23.09. 22:32:40): „(1) Weißraum gehört zur Tarifsprache, soweit die versiegelte Normalversion ihn rechnet —
  S1 ist an K2868 damit nicht sauber behoben, das korrigiert den T3-Befund, und mein Prüfstein „K2868 muss bestehen" war
  falsch; prüf dasselbe an K3044, der S1-Behebung aus Lauf 38, und korrigiere die Schwächenzählung von Lauf 38, falls
  nötig.“
- PH Z. 455 (24.09. 02:14:45): „(4) S1 nicht neu versiegeln — nach der Messung ändert man kein Kriterium; …“
- Hermes-Ergebnis: Titel von Q7 „T3 TypeScript — abschluss-03: **nicht abgenommen**“; Gründe in Q7 Z. 9–12.
- v8 Z. 461: „… T3 zählt nicht zur Sättigung des Breitentests.“

## 7. Tor 4 (v8) und Tor 5
Es gibt keine Messung und keine Wertung. Die Vorbedingungen für T4 sind in Teil 3 (FK27) aufgeführt, soweit sie
Messgerätfehler betreffen.
