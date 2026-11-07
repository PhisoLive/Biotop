# BIOTOP-LAGE-01 · Fassung 2 · `CHRONIK-TEIL3-01.md`

- **Inhalt:** FK10, FK12, FK20 · Entwurf F, Stück 3 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil F, Arbeitszeit 25.09.2026 16:10:47–18:11:01 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/chronik/CHRONIK-TEIL3.md` · 16622 B · SHA-256 `8f1242222994422d6c5a5e577a5f7de82f6a3acbd601e62321a0c91c1b682f39`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (0 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# CHRONIK — Teil 3 von 3: FK20 Budgets, Verbrauch und Kostengrenze im Code

BIOTOP-LAGE-01 Fassung 2 · Entwurfsteil F · Lesestand 25.09.2026, 16:10–18:10 CEST. Kennungen: Teil 1.

## Bezug und Rechenweg

- **Verbrauch:** Summe `kosten_eur` der Tabelle `kasse`, gerechnet je Lauf (R64 §1–3, R102).
  - Jeder Lauf ist aus genau einem Datenbankzweig gezählt: STAMM für die Läufe 1–25, VB1 und R02 für ihren Lauf 26, T3 für die Läufe 26–38.
  - Der gemeinsame Altbestand (4.070 Buchungen, 8,639305 €) steht in allen vier Zweigen gleich und zählt nur einmal (R102 §4).
- **Grenze:** Wortlaut aus Masterprompt, Auftrag oder Nachricht; die Quelle steht je Zeile.
- **Offen** = Grenze − Verbrauch (gerechnet).
- **Rundung:** Beträge mit sechs Stellen aus der Kasse. Berichtswerte mit vier Stellen sind ausdrücklich als „Bericht" gekennzeichnet.
- **Kasse gegen Nutzungsanzeige von OpenRouter** (Auftrag §5 Nr. 6): steht in KASSE und INVENTAR. Wo dasselbe Konto außerhalb des Biotops genutzt wurde, steht hier nur der Hinweis.

**Gesamt ohne Doppelzählung** (R64 §2, gerechnet): 6.919 Buchungen, **18,814735 €**. Davon:
- STAMM (Läufe 1–25): 4.070 Buchungen, 8,639305 €
- VB1-26: 246 Buchungen, 0,446792 €
- R02-26: 0 Buchungen, 0,000000 €
- T3 (Läufe 26–38): 2.603 Buchungen, 9,728638 €

**Seit dem 21.09. 00:00 CEST** (für FK01 Nr. 10):
- 2.603 Buchungen und 9,728638 €, alle aus den T3-Läufen 26–38.
- Erste Buchung 21.09. 05:44:13, letzte 22.09. 21:26:08.
- STAMM, VB1 und R02 haben keine Buchung nach dem 20.09. 22:16:10 (R64 §1).

## B. Budgettafel je Phase und Auftrag

| Nr | Phase / Auftrag | Grenze (Wortlaut, Quelle) | Läufe | Verbrauch (Kasse, gerechnet) | Offen | Bericht und Abweichung |
|---|---|---|---|---|---|---|
| B01 | Phase 1 | „Budget Phase 1: 30 €, hart" (Philipp 659, 18.09. 23:16) | L1–L5 | 236 Buchungen, 0,403061 € | 29,596939 € | `phase-1/KASSE.md`: 236 Aufrufe, 0,4031 € — gleich |
| B02 | Nachlauf Phase 1 | „Budget 5 €, hart" (v2 Z. 259) | L6–L10 | 542, 1,790338 € | 3,209662 € | `phase-1-nachlauf/KASSE.md`: 542, 1,7903 € — gleich |
| B03 | Phase 2 | „Budget Phase 2 gesamt 10 €, hart" (v3 Z. 221, 274) | L11–L13 | 1.199, 1,906480 € | 8,093520 € | Bericht 1.190, 1,9050 €; Unterschied 9 Buchungen, 0,001476 € = spätere Buchungen auf L13 (Teil 2, Anm. 5) |
| B04 | Phase 3 | „Budget 15 €, hart, einschließlich Nachprobe" (v4 Z. 309) | L14–L20 | 1.245, 2,842396 € | 12,157604 € | Bericht 1.225, 2,8269 € (18,8 %); Unterschied 20, 0,015473 € = spätere Buchungen auf L16–L20 |
| B05 | Nachlauf Phase 3 | „Budget 10 €, hart" (v5 Z. 352; Philipp 2234) | Bericht „Läufe ab 21" bis 20.09. 00:00:28 | 207, 0,436701 € (L22: 189 / 0,397763; L23: 18 / 0,038938; L21: 0) | 9,563299 € | Bericht 207, 0,4367 € — gleich; dazu 29 Buchungen, 0,016949 € auf alten Lauf-IDs im selben Zeitraum (in B03/B04 gezählt) |
| B06 | Phase 4, Vorbedingung 1 (Bauteile A/B, C) | „Budget 3 €" (v6 Z. 393); „Budget 3 € hart" (Philipp 2798) | L22 (Fortsetzung), L23, L24, L25 | Lesart A (L22–L25 ganz): 848, 1,697029 €. Lesart B (V20, ohne erste Etappe L22): 659, 1,299266 € | A: 1,302971 €; B: 1,700734 € | geführt „rund 1,299 € von 3 €, frei rund 1,701 €" (V20, R31); Widersprüche X01–X03 |
| B07 | Lauf 25 (in B06) | „Budget: 0,80 € hart für diesen Lauf" (Lauf-25-Auftrag, Kopf) | L25 | 183, 0,389929 € (48,7 %) | 0,410071 € | Bericht 183, 0,3899 € — gleich |
| B08 | Gesamtstand | „Budget 1 €" (Philipp 3429) | — | 0 neue Buchungen | 1,00 € | `gesamtstand/KASSE.md`: „0 neue Biotop-Kassenbuchungen … 4070 / 4070" |
| B09 | Reparatur 01 | „Budget 5 € hart" (Philipp 4317) | — | 0 | 5,00 € | Kassenblätter und Zwischenberichte der Zwischenstände (R64 §6): durchgehend „0 neue Biotop-Buchungen" bzw. „0 € von 5,00 €" |
| B10 | Reparatur 02 | „Budget 5 € hart" (Philipp 7732) | R02-26 | 0 | 5,00 € | `reparatur-02/KASSE.md`: „0.00 EUR von 5,00 EUR" |
| B11 | Vorbedingung 1 nach Reparatur 02 | „Budget 3 € hart" (Philipp 7913, 8110) | VB1-26 | 246, 0,446792 € | 2,553208 € | `phase-4-einstieg…/KASSE.md`: 246, 0,446792 € — gleich |
| B12 | Nachtrag Vorbedingung 1 | „Budget 2 € hart" (Philipp 8461) | — | 0 | 2,00 € | ebd.: „0 neue Biotop-Modellbuchungen, 0 EUR (damaliges Budget 2 EUR)" |
| B13 | Trägernachweis W4 | ANTWORT_W1-W4 §2: „Ein Aufruf, nicht mehr … Getrennt verbucht" | — | nicht in der Biotop-Kasse | UNBEKANNT | 3215: „Keine Wiederholung. Kosten unbekannt"; Anmeldelage ist nicht Gegenstand (Auftrag §2 Nr. 15) |
| B14 | T3 (Testwerk `versandwerk`) | „Budget 10 € hart" (Philipp 9106); „je Testwerk 10 €, hart" (v7 Z. 437, v8 Z. 454) | T3-26–T3-38 | 2.603, 9,728638 € | 0,271362 € | `abschluss-03/ABSCHLUSS-03.md`: „9,728638 € von 10,00 € (2603 Buchungen, Läufe 26–38)" — gleich. Stand nach L37: 5,477008 €, Rest 4,522992 € (Philipp 11434: „Restbudget 4,52 €") |
| B15 | T3 Nachtrag abschluss-02 | „Budget für den Nachtrag 1 € hart" (Philipp 11301) | — | 0 | 1,00 € | `abschluss-02/NACHTRAG-02.md`: „verbraucht: 0,00 €" |
| B16 | T3 abschluss-03 | kein eigenes Budget gefunden; „Kein weiterer Lauf an T3" (11575) | — | 0 | — | ABSCHLUSS-03: „Dieser Abschluss kostete 0,00 €" |
| B17 | Behebungsrunden 1–6 vor T4 | „Kein Lauf, kein Modellgeld" (Philipp 14000, 14624, 15154, 15992, 16482, 16901) | — | 0 Buchungen in allen Zweigen seit 22.09. 21:26:08 | — | KASSE.md der Runden 1–5: „Biotop-Modellgeld 0,00 €"; Runde 6 laut Übergabe „Modellkosten 0,00 €" (Verdrahtungstest). Hermes' eigene Tokens stehen nicht in der Biotop-Kasse (KASSE.md Runden 3–5) |
| B18 | Träger und Verdichtung (kein Biotop-Budget) | Philipp 17217: „die Kosten je Verdichtung nennen" | — | nicht in der Biotop-Kasse | — | Die Übergabe Runde 6 (01:15) nennt eine Verdichtung über denselben OpenRouter-Zugang mit Betrag. Das ist wichtig für den Abgleich mit der OpenRouter-Anzeige (→ KASSE, INVENTAR) und wird hier nicht beziffert |
| B19 | BIOTOP-LAGE-01 | „Budget für bezahlte Modellaufrufe 0,00 €" (Auftrag §1) | — | 0 Buchungen bis 16:58 CEST (R102: STAMM 4.070, WAL 0 Bytes) | 0,00 € | Hermes trägt den Endstand nach |
| B20 | T4, T5, T6 (Breitentest) | „je Testwerk 10 €, hart" (v8 Z. 454; Schätzungen T4 5–15 €, T5 1–4 €, T6 2–6 €) | — | 0, nicht begonnen | je 10,00 € | — |
| B21 | Phase 4 alt: Aufnahme und Landkarte, Generation minus eins am Handelssystem | „Aufnahme und Landkarte 20 €, Generation minus eins 5 €" (v6 Z. 298, 396) | — | 0 | — | entfallen mit Fassung 7: Handelssystem gestrichen (P25) |
| B22 | Phase 5 (erstes echtes Werk) | „nicht schätzbar … Budget je Abschnitt setzt Philipp nach dem Kostenvoranschlag" (v8 Z. 326) | — | 0 | keine Grenze gesetzt | — |

**Rahmen aus Fassung 1:** „Budget je Lauf (Vorschlag für Phasen 1–3 zusammen: 150 €; Phase 4 gesondert nach Kostenvoranschlag der Kasse)" (v1 Z. 279, wortgleich bis v8 Z. 513).
- Die Phasen 1–3 samt Nachläufen haben nach B01–B05 zusammen 7,379 € verbraucht (gerechnet 0,403061 + 1,790338 + 1,906480 + 2,842396 + 0,436701 = 7,378976 €; ohne die Vorbedingung 1).

**Laufbudgets (`laeufe.budget_eur`)** stehen je Lauf in der Lauftafel (Teil 2).
- In T3 trägt jeder Lauf 10,0, also das Auftragsbudget.
- Die Grenze des Auftrags wirkt über `BIOTOP_AUFTRAG_BUDGET_EUR` (Abschnitt „Kostengrenze im Code").

## Verbrauch je Werk (R64 §4, ohne Doppelzählung)

| Werk | Läufe | Buchungen | Kosten € | Grenze |
|---|---|---|---|---|
| `lagerhaus` (Übungswerk, alle Laufkopien) | L1, L2, L4–L10, L12–L16, L18–L22, L24, L25, VB1-26, R02-26 | 3.755 | 7,695211 | kein Werkbudget; Grenzen je Phase (B01–B07, B10, B11) |
| `logmuehle` (Übungswerk) | L17, L23 | 554 | 1,389441 | über B04, B05/B06 |
| `versandwerk` (T3) | T3-26–T3-38 | 2.603 | 9,728638 | 10 € hart (B14) |
| ohne Werk | L3, L11 | 7 | 0,001444 | über B01, B03 |
| **Summe** | 40 Laufdatensätze | 6.919 | 18,814734 (Rundung gegen 18,814735) | — |

## Ausfallklärungen mit Höchstfall (T3, R102 §3)

- **Kassenzeilen `zweck='ausfall.hoechstfall'`:** 115 Zeilen, 0,462024 € (gerechnet). Sie sind in B14 enthalten.
  - Je Lauf: T3-29, T3-30, T3-35 je 1 Zeile / 0,0028 €; T3-36 75 / 0,332297 €; T3-37 36 / 0,112645 €; T3-38 1 / 0,008682 €.
  - Automatisch geklärt: 112; von Hand: 3 (T3-29, -30, -35).
- **Abgleich:** `abschluss-01` nennt für die Läufe 26–37 „Darin 0,4533 € Ausfallklärungen". Gerechnet 0,453342 € — gleich.

## Kostengrenze im Code — wo und wie

Gelesen: `biotop/kern/kasse.py` (16.536 Bytes, sha256 `228dc1a662cce5e7…`). Der Arbeitsbaum ist gleich HEAD (R64 §7). Die Fundstellen stehen auch in R31 §5. Dazu gelesen: `biotop/lauf.py`, `biotop/anbieter/__init__.py`, `biotop/__main__.py` und die T3-Laufskripte (nur gelesen, nicht ausgeführt).

1. **Laufbudget `budget_eur`.**
   - Es wird beim Anlegen gesetzt: `biotop lauf anlegen --budget <€>`. `--budget` ist Pflicht (`__main__.py` Z. 48).
   - `lauf.anlegen` schreibt es in `laeufe.budget_eur` und ins Protokoll `lauf.angelegt` (`lauf.py` Z. 49–56).
2. **Vorprüfung vor jedem Modellaufruf.**
   - Der einzige Weg zu einem Modell ist `anbieter.aufrufen`, Docstring: „Einziger Weg zu einem Modell. Kasse vor dem Aufruf, Buchung danach." (`anbieter/__init__.py` Z. 191–198).
   - Es ruft `kasse.vorpruefung` mit den geschätzten Eingabetoken und `max_tokens` als Höchstfall der Ausgabe.
   - `vorpruefung` (Z. 116–172) prüft in dieser Reihenfolge:
     - a) **Auftragsgrenze scharf?** `auftragsgrenze_verlangen()` (Z. 70–86). Fehlt `BIOTOP_AUFTRAG_LAUF_AB` oder `BIOTOP_AUFTRAG_BUDGET_EUR` oder steht einer auf null, gibt es `AuftragsgrenzeFehlt` und keinen Aufruf. Meldung: „Null ist keine Grenze, sondern eine fehlende Grenze — ohne sie startet kein Lauf". Eingebaut am 21.09. (C028–C030; Commit `18f78f1`, 21.09. 13:10 „Startsperre ohne scharfe Auftragsgrenze").
     - b) **Offener Anbieterausfall** mit unbekanntem Verbrauch: Genau einer je Vorprüfung wird automatisch mit dem Höchstfall gebucht, also der vollen Reservierung (Z. 124–143; `ausfall_klaeren` Z. 175–218). Commit `5b4066f`, 21.09. 20:25 (C036).
     - c) **Auftragsbudget:** Summe aller Buchungen mit `lauf_id >= BIOTOP_AUFTRAG_LAUF_AB` plus Schätzung größer als `BIOTOP_AUFTRAG_BUDGET_EUR`. Dann Protokoll `kasse.abbruch` „AUFTRAGSBUDGET erschöpft — Aufruf NICHT ausgeführt", Laufstatus `abgebrochen`, `BudgetErschoepft` (Z. 146–154).
     - d) **Laufbudget:** bisheriger Verbrauch des Laufs plus Schätzung größer als `budget_eur`. Dann `kasse.abbruch` „Budget erschöpft — Aufruf NICHT ausgeführt" (Z. 155–171).
3. **Kostenvoranschlag je Generation.**
   - Vor jeder Generation ruft `lauf.py` Z. 236 `kasse.generation_vorpruefung` (Z. 294–313).
   - Ist der bisherige Verbrauch plus die teuerste bisherige Generation größer als das Laufbudget, folgt `kasse.abbruch` „Budget reicht nicht für Generation n — kein Modellaufruf ausgeführt".
   - Gelesen, nicht ausgeführt: Der Voranschlag prüft nur das Laufbudget, nicht das Auftragsbudget. Solange noch keine Generation Kosten hat (Voranschlag 0), sperrt er nicht.
4. **Preise und Kurs gehören zum Kern.**
   - `PREISE_USD_JE_MIO` (Z. 23–43) und `USD_JE_EUR = 1.08` (Z. 20); Kommentar: „Beides ändert nur Philipp".
   - Für ein Modell ohne Preis wirft `kosten_eur` einen `KeyError` (Z. 90–91).
5. **Wo die Auftragsgrenze gesetzt wird.** Nicht in einer Konfigurationsdatei, sondern als Umgebungsvariable im Laufskript. Beispiele (gelesen):
   - `/root/biotop-t3/lauf38_evolution.sh` Z. 9–10: `BIOTOP_AUFTRAG_LAUF_AB=26`, `BIOTOP_AUFTRAG_BUDGET_EUR=10`.
   - Phase-3-Skripte (Sicherungskopien unter `/root/biotop-t3/arbeitsstand-sicherung/pruefung/`): `…LAUF_AB=14 …BUDGET_EUR=15`.
   - Dazu setzen die T3-Evolutionsskripte einen **Halt im Skript**, der vor jeder Generation prüft:
     - `GRENZE=9.30` in `lauf31_evolution.sh` bis `lauf37_evolution.sh`, Z. 14;
     - `GRENZE=9.60 # Restbudget 4,52 EUR; Halt vor dem Ueberschreiten der 10-EUR-Auftragsgrenze.` in `lauf38_evolution.sh` Z. 14;
     - Meldung Z. 35: „HALT: Budgetgrenze $GRENZE EUR erreicht ($V EUR). Kein weiterer Modellaufruf."
6. **Gemessene Wirkung** (Protokoll `kasse.abbruch`, R102 §3): 3 Einträge, in allen vier Zweigen dieselben.
   - #652: L4, Aufrufprüfung, „Budget erschöpft — Aufruf NICHT ausgeführt".
   - #800: L5, „Budget reicht nicht für Generation 3".
   - #2623: L10, „… Generation 2".
   - Alle drei sind Kassenproben mit 0,10 € (Tor 1 Zeile 6).
   - Kein Abbruch am Auftragsbudget in keinem Zweig. Kein `kasse.abbruch` in den T3-Läufen.
   - Auslegung Hermes (aus dem Code gelesen): Das Laufbudget von 10,0 je T3-Lauf band nie, weil es je Lauf gilt und der teuerste T3-Lauf 4,251629 € kostete. Bindend waren das Auftragsbudget im Kern (10 €) und der Halt im Skript.
   - T3-38 endete am Halt des Skripts: „standen 9,483126 €, danach 9,728638 € (‚HALT: Budgetgrenze 9.60 EUR erreicht (9.728638 EUR)')" (ABSCHLUSS-03). Die Prüfung liegt vor jeder Generation; die letzte Generation begann unter 9,60 € und endete bei 9,728638 €. Die harte Grenze von 10 € wurde nicht erreicht.
7. **Frühere Befunde zur Grenze, nur Verweis** (Wertung in TORE und LAGE, FK43):
   - `biotop-gesamtstand/ABWEICHUNGEN-01.md` A22 (20.09.): „Budgetvorprüfung ist keine obere Kostengrenze und reserviert keine parallelen Aufrufe".
   - `ORGANBETRIEB-01.md` 3.14: „Budgetautomat in Fehlerpfaden unvollständig".
   - Beide beschreiben den Stand vom 20.09. `kasse.py` wurde danach dreimal geändert: `e259e9f`, `18f78f1`, `5b4066f`, alle am 21.09. (R64 §7).

## Widersprüche Kasse gegen gemeldete Zahlen — beide Belege, keine Wertung

| Nr | Gemeldet | Kasse (gerechnet) | Erklärung laut Quellen |
|---|---|---|---|
| X01 | STAND-01: „Kassenstand Vorbedingung 1: 1,6970 € von 3 €, frei 1,3030 € (Lesart A, vorsichtig geführt)" (R31 Z. 165), dort als „HISTORISCH … ersetzt" markiert (Z. 155). Gegen REGELN-01 V20 und STAND-01 W2: „rund 1,299 € von 3 €, frei rund 1,701 €" (R31 Z. 123, 141) | L22–L25: 848, 1,697029 €. Ohne die erste Etappe von L22 (189, 0,397763 €): 659, 1,299266 € | Abgrenzung: Die erste Etappe von L22 ist im Nachlauf Phase 3 (B05) verbucht; ANTWORT §3 V20 stellt um. Beide Zahlen sind aus der Kasse nachzurechnen |
| X02 | Lesart B „1,2994 €" (`KASSE-06.md`, `NACHGANG-06.md`); ANTWORT §3 „1,2992 € von 3 €, frei 1,7008 €"; Fortsetzung von L22 „0,1190" (`KASSE.md` VB1, PRUEFUNG §1: „0,1190 + 0,3936 + 0,3969 = 0,9095 € ✓") | Fortsetzung L22: 44, 0,118845 € (≈ 0,1188). Lesart B 1,299266 € (≈ 1,2993) | 3215: „die alte Fortsetzungszahl war falsch"; W01 in Teil 2. Drei Viertstellenwerte (1,2994 / 1,2992 / 1,2993) für dieselbe Abgrenzung |
| X03 | ANTWORT §3: „0,5166 − 0,1190 = 0,3976 … gemessen 0,3978 … Rundung" | L22 ganz 0,516608 €, Fortsetzung 0,118845 €, Differenz 0,397763 € (≈ 0,3978) | Die Differenz entsteht aus 0,1190 statt 0,1188, nicht aus Rundung (3215; REGELN-01 zu Regel 26) |
| X04 | Nachlauf Phase 3: 207 / 0,4367 € (Bezug „Läufe ab 21") und VB1 Lesart B: 659 / 1,2993 € — zusammen 866 Buchungen | L21–L25 haben 848 Buchungen, 1,697029 € | 18 Buchungen / 0,038938 € von L23 vor 20.09. 00:00:28 (Aufnahme 1, Landkarte 16, `schwer.mentor` 1; R102 §2) stehen in beiden Summen. STAND-01: „Abgrenzung von Lauf 23 noch offen" (R31 Z. 141). Ohne Doppelzählung: Nachlauf 207 / 0,436701 € + VB1 641 / 1,260328 €, oder Nachlauf 189 / 0,397763 € + VB1 659 / 1,299266 € |
| X05 | Philipp 3429: „Summe gegen meine Rechnung von 7,37 €" (Läufe 1–23) | L1–L23: 7,852498 € (8,639305 − 0,396878 − 0,389929) | 3815: „7,37 € stimmt als Summe der gerundeten Abschnittsbeträge; heute stehen auf denselben Lauf-IDs 7,852498 €". Mit zwei Stellen: 0,40 + 1,79 + 1,91 + 2,83 + 0,44 = 7,37 €; mit vier Stellen 7,3620 €; Rest 0,4905 € = L22/L23 nach 00:00:28 (0,473521 €) + spätere Buchungen auf alten IDs (0,016949 €) + Rundung |
| X06 | Phase 2: 1.190 / 1,9050 €; Phase 3: 1.225 / 2,8269 € | 1.199 / 1,906480 €; 1.245 / 2,842396 € | spätere Buchungen (B03, B04; Teil 2, Anm. 5) |

Keine Abweichung zwischen Kasse und Bericht bei B01, B02, B07, B11, B14 (T3: 5,4770 € nach L37 und 9,728638 € nach L38 sind gleich).
