# BIOTOP-LAGE-01 · Fassung 2 · `CHRONIK-TEIL2-01.md`

- **Inhalt:** FK10, FK12, FK20 · Entwurf F, Stück 2 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil F, Arbeitszeit 25.09.2026 16:10:47–18:11:01 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/chronik/CHRONIK-TEIL2.md` · 24880 B · SHA-256 `965045736c0d3c006525b4a26f2d3f3e2a12b68727b57ef710de25862e2e277f`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (1 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# CHRONIK — Teil 2 von 3: Lauftafel und Abgleich zu FK10; FK12 Prüfungen Chat-Claudes

BIOTOP-LAGE-01 Fassung 2 · Entwurfsteil F · Lesestand 25.09.2026, 16:10–18:10 CEST. Kennungen und Lesehinweise: Teil 1.

## FK10 (Fortsetzung): Lauftafel — jeder Lauf eine Zeile

Quellen: R64 §1 (je Zweig und Lauf gerechnet, Summe `kosten_eur`, sechs Stellen); Status und Budget aus der Tabelle `laeufe` (R25); Beginn in CEST umgerechnet.
Zweige (REGELN): STAMM `/root/biotop/daten/biotop.db` (Läufe 1–25), VB1 `/root/phase-4-vorbedingung-1/privat/biotop.db`, R02 `/root/reparatur-02/privat-cli/privat.db`, T3 `/root/biotop-t3/t3.db` (Läufe 26–38).
Ohne Doppelzählung wird jeder Lauf aus genau einem Zweig gezählt. Der Altbestand (4.070 Buchungen, IDs bis 4.070) ist in allen vier Zweigen gleich (R102 §4).

| Lauf | Zweig | Werk (werk_id) | Laufbudget € | Status (DB) | Beginn | Buchungen | Kosten € | Zeile | Ordner `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/…` |
|---|---|---|---|---|---|---|---|---|---|
| L1 | STAMM | lagerhaus (1) | 30.0 | abgebrochen | 18.09. 23:40:42 | 27 | 0.024193 | C001 | biotop-phase-1/ |
| L2 | STAMM | lagerhaus (1) | 30.0 | bereit | 18.09. 23:44:49 | 100 | 0.216594 | C001 | biotop-phase-1/ |
| L3 | STAMM | — | 1.0 | gestoppt | 19.09. 00:04:12 | 1 | 0.000187 | C001 | biotop-phase-1/ |
| L4 | STAMM | lagerhaus-kasse (3) | 0.1 | abgebrochen | 19.09. 00:04:51 | 62 | 0.094108 | C001 | biotop-phase-1/ |
| L5 | STAMM | lagerhaus-kasse2 (4) | 0.1 | abgebrochen | 19.09. 00:11:45 | 46 | 0.067978 | C001 | biotop-phase-1/ |
| L6 | STAMM | lagerhaus-nachlauf (5) | 5.0 | abgebrochen | 19.09. 00:48:35 | 178 | 0.746327 | C002 | biotop-phase-1-nachlauf/ |
| L7 | STAMM | lagerhaus-nachlauf2 (6) | 3.0 | abgebrochen | 19.09. 01:20:20 | 88 | 0.217395 | C002 | biotop-phase-1-nachlauf/ |
| L8 | STAMM | lagerhaus-nachlauf8 (7) | 2.0 | abgebrochen | 19.09. 01:33:13 | 136 | 0.408594 | C002 | biotop-phase-1-nachlauf/ |
| L9 | STAMM | lagerhaus-nachlauf9 (8) | 2.0 | beendet | 19.09. 01:53:36 | 108 | 0.323255 | C002 | biotop-phase-1-nachlauf/ |
| L10 | STAMM | lagerhaus-kasse3 (9) | 0.1 | abgebrochen | 19.09. 02:09:20 | 32 | 0.094767 | C002 | biotop-phase-1-nachlauf/ |
| L11 | STAMM | — | 0.05 | angelegt | 19.09. 02:28:44 | 6 | 0.001257 | C003 | biotop-phase-2/ |
| L12 | STAMM | lagerhaus-p2 (10) | 10.0 | abgebrochen | 19.09. 02:41:55 | 480 | 0.758462 | C003 | biotop-phase-2/ |
| L13 | STAMM | lagerhaus-p2-13 (11) | 8.0 | beendet | 19.09. 03:47:07 | 713 | 1.146760 | C003 | biotop-phase-2/ |
| L14 | STAMM | lagerhaus-p3-14 (12) | 1.0 | verworfen | 19.09. 13:03:07 | 17 | 0.003546 | C004 | biotop-phase-3/ |
| L15 | STAMM | lagerhaus-p3-15 (13) | 1.0 | verworfen | 19.09. 13:09:10 | 28 | 0.011853 | C004 | biotop-phase-3/ |
| L16 | STAMM | lagerhaus-p3-16 (14) | 3.0 | verworfen | 19.09. 13:26:06 | 264 | 0.596412 | C004 | biotop-phase-3/ |
| L17 | STAMM | logmuehle-17 (15) | 3.0 | gesaettigt | 19.09. 13:55:34 | 315 | 0.995827 | C004 | biotop-phase-3/ |
| L18 | STAMM | lagerhaus-p3-18 (16) | 3.0 | verworfen | 19.09. 16:41:03 | 156 | 0.340069 | C004 | biotop-phase-3/ |
| L19 | STAMM | lagerhaus-p3-19 (17) | 3.0 | verworfen | 19.09. 17:06:18 | 221 | 0.457615 | C004 | biotop-phase-3/ |
| L20 | STAMM | lagerhaus-p3-20 (18) | 3.0 | gesaettigt | 19.09. 17:40:05 | 244 | 0.437074 | C004 | biotop-phase-3/ |
| L21 | STAMM | lagerhaus-p3-20 (18) | 1.0 | verworfen | 19.09. 22:34:21 | **0** | 0.000000 | C005 | biotop-phase-3-nachlauf/ |
| L22 | STAMM | lagerhaus-p3-22 (19) | 3.0 | gesaettigt | 19.09. 22:57:41 | 233 | 0.516608 | C005, C006 | biotop-phase-3-nachlauf/, biotop-phase-4-vorbedingung-1/ |
| L23 | STAMM | logmuehle-23 (20) | 2.0 | gesaettigt | 19.09. 23:32:55 | 239 | 0.393614 | C005, C006 | wie L22 |
| L24 | STAMM | lagerhaus-zeile8-24 (21) | 1.5 | bereit | 20.09. 00:57:49 | 193 | 0.396878 | C006 | biotop-phase-4-vorbedingung-1/ |
| L25 | STAMM | lagerhaus-c-25 (22) | 0.8 | bereit | 20.09. 03:13:30 | 183 | 0.389929 | C008 | biotop-phase-4-vorbedingung-1/ |
| VB1-26 | VB1 | lagerhaus-vorbedingung1-26 (23) | 3.0 | gesaettigt | 20.09. 21:31:54 | 246 | 0.446792 | C016 | biotop-phase-4-vorbedingung-1/nach-reparatur-02/ |
| R02-26 | R02 | lagerhaus-c-25 (22, Pfad `/root/reparatur-02/privat-cli/werk`) | 0.0 | kartiert | 20.09. 20:42:07 | **0** | 0.000000 | C015 | biotop-reparatur-02/ |
| T3-26 | T3 | versandwerk-t3-02 (23) | 10.0 | kartiert | 21.09. 05:43:38 | 31 | 0.007099 | C025 | biotop-t3-typescript/ |
| T3-27 | T3 | versandwerk-t3-02 (23) | 10.0 | kartiert | 21.09. 05:48:08 | 1 | 0.000137 | C025 | biotop-t3-typescript/ |
| T3-28 | T3 | versandwerk-t3-02 (23) | 10.0 | kartiert | 21.09. 06:05:27 | 1 | 0.000138 | C025 | biotop-t3-typescript/ |
| T3-29 | T3 | versandwerk-t3-02 (23) | 10.0 | kartiert | 21.09. 06:35:14 | 4 | 0.005917 | C027 | biotop-t3-typescript/ |
| T3-30 | T3 | versandwerk-t3-02 (23) | 10.0 | kartiert | 21.09. 07:34:47 | 4 | 0.005989 | C027 | biotop-t3-typescript/ |
| T3-31 | T3 | versandwerk-t3-02 (23) | 10.0 | laeuft | 21.09. 13:11:04 | 107 | 0.127728 | C028–C030 | biotop-t3-typescript/ |
| T3-32 | T3 | versandwerk-t3-02 (23) | 10.0 | laeuft | 21.09. 15:19:35 | 246 | 1.072688 | C030, C031 | biotop-t3-typescript/ |
| T3-33 | T3 | versandwerk-t3-02 (23) | 10.0 | kartiert | 21.09. 18:23:15 | 1 | 0.000136 | C031, C033 | biotop-t3-typescript/ |
| T3-34 | T3 | versandwerk-t3-02 (23) | 10.0 | kartiert | 21.09. 18:45:51 | 1 | 0.000141 | C033, C035 | biotop-t3-typescript/ |
| T3-35 | T3 | versandwerk-t3-02 (23) | 10.0 | kartiert | 21.09. 19:15:24 | 3 | 0.003841 | C035 | biotop-t3-typescript/ |
| T3-36 | T3 | versandwerk-t3-02 (23) | 10.0 | laeuft | 21.09. 20:25:59 | 326 | 1.186430 | C036 | biotop-t3-typescript/ |
| T3-37 | T3 | versandwerk-t3-02 (23) | 10.0 | gesaettigt | 22.09. 00:21:06 | 895 | 3.066764 | C036 | biotop-t3-typescript/abschluss-01/ |
| T3-38 | T3 | versandwerk-t3-02 (23) | 10.0 | bereit | 22.09. 15:42:49 | 983 | 4.251629 | C039 | biotop-t3-typescript/abschluss-03/ |

**Anmerkungen zur Lauftafel** (keine Wertung):
1. **Nummernkreis.** Die Laufnummern 1–38 sind lückenlos: 1–25 im STAMM, 26–38 im Zweig T3. Nummer 26 ist dreimal vergeben: VB1, R02 und T3 zählen unabhängig weiter.
   - Hermes' Meldung 10525 (21.09. 06:26:33) nennt „zwei Datenbanken"; R02 fehlt dort.
   - Dieselbe Meldung gibt Zeiten in UTC ohne Zone an. Für Lauf 27 nennt sie „04:05:27"; das ist der Beginn von Lauf 28. Die DB führt `2026-09-21T03:48:08` UTC (R25 Z. 210).
2. **Ohne Kassenzeile: 2 von 40 Laufdatensätzen.**
   - L21: verworfen in derselben Sekunde, in der er angelegt wurde; Grund „Hermes (satz2): Ankläger-Ablauf während …" (R25).
   - R02-26: Pflichtvorspann-CLI am privaten Bestand; `biotop-reparatur-02/CLI.json` nennt `lauf_id` 26.
3. **Ohne Ordner: 0 von 40.**
   - L27 und L34 werden in den `*.md` der Ebenen 1–2 nicht als „Lauf 27/34" genannt (R30 §3).
   - Sie stehen aber als Zeilen der Kassentabelle in `biotop-t3-typescript/abschluss-01/ABSCHLUSSBERICHT.md` (Z. 101, 108) und in `uebernahme-01/ZWISCHENBERICHT.md` (Z. 25, 40).
4. **Status in der DB gegen Meldungen** (Widerspruch mit beiden Belegen):
   - T3-31, T3-32, T3-36 stehen auf `laeuft`; gemeldet „starb" (10829, 10945, 11207).
   - T3-38 steht auf `bereit`; gemeldet „am Budget beendet" (11574). Er endete am Halt des Laufskripts bei 9,60 €, nicht an der Kasse im Kern (Teil 3).
   - L2, L24, L25 stehen auf `bereit`; ihre Aufträge sind abgeschlossen (C001, C006, C008).
   - In allen sieben Fällen ist `beendet_am` leer (R25).
5. **Spätere Buchungen.** Einige Buchungen tragen eine Zeit nach der Endmeldung ihres Auftrags (R64 §3, R102 §1):
   - L13: 9 Buchungen, 0,001476 €, Zweck `gedaechtnis`, 19.09. 23 Uhr.
   - L16–L19: 9 Buchungen, 0,001457 €, `gedaechtnis`, 23 Uhr.
   - L20: 10 Buchungen, 0,013912 €, `aegis.angriff`, 22 Uhr; dazu 1 Buchung, 0,000104 €, `gedaechtnis`.
   - Das sind zusammen 29 Buchungen und 0,016949 € (gerechnet). Sie fallen in die Zeit des Nachlaufs zu Phase 3, laufen aber auf alten Lauf-IDs (`biotop-gesamtstand/LAEUFE-01.md`: „Nachabstraktion auf alten Lauf-IDs …"). Budgetfolge: Teil 3, B05.
6. **Zeitschnitt der Läufe 22 und 23** (R64 §3, Schnitt 20.09. 00:00:28 CEST):
   - L22: 189 Buchungen vorher, 44 danach.
   - L23: 18 vorher, 221 danach.
   - Die Fortsetzungen liegen vor dem Kurzauftrag 2798 (00:55:54, Teil 1 C006).

## Abgleich zu FK10 (Auftrag Abschnitt 5 Nr. 1, 2, 4)

| Gegenstand | Anzahl | zugeordnet | erklärt | offen |
|---|---|---|---|---|
| Laufdatensätze (STAMM 25, VB1 1, R02 1, T3 13) | 40 | 40 mit Chronikzeile, 40 mit Ordner | 2 ohne Kassenzeile (Anm. 2); Nr. 26 dreifach (Anm. 1) | 0 |
| Abschlussordner `biotop-*` und `gedaechtnis` (R26) | 20 | 20 | — | 0 |
| Nachrichten Philipps ab 18.09. (v2) | 114 | 114 (71 in C001–C017, 43 in C018–C060) | 6 Einträge der Lesedatei sind nicht von Philipp (Teil 1) | 0 |
| Erstaufträge Hermes→Subagent | 38 (20 vor, 18 ab 21.09.) | 38 | 61 weitere Blöcke sind Nachsteuerungen, Wiederholungen nach Verdichtung und Grenzmeldungen (R44: 97 Blöcke; 16285 und 16712 kommen aus v2 dazu) | 0 |

**Ordner → Zeile:**
- `phase-1` → C001 · `phase-1-nachlauf` → C002 · `phase-2` → C003 · `phase-3` → C004 · `phase-3-nachlauf` → C005
- `phase-4-vorbedingung-1` → C006–C010, C016–C018 · `wiedereinstieg-2026-09-20-01` → C011 · `gedaechtnis` → C011
- `gesamtstand` → C013 · `reparatur-01` → C014 · `reparatur-02` → C015 · `phase-4-einstieg-20260921-01` → C020
- `t3-typescript` → C022–C042 · `vor-t4` → C043, C044 · `vor-t4-02` → C045 · `vor-t4-03` → C046, C047 · `vor-t4-04` → C048 · `vor-t4-05` → C049–C051
- `vor-t4-06` (nur Zwischenberichte) → C051–C059 · `lage-01` → C060

**Status der Aufträge** (Nr. 4): Jede Zeile C001–C060 trägt einen Status. Offen sind C059 (S1c) und C060 (dieser Auftrag). Teilweise sind C011 (W4), C012 (W6) und C055 (S1-Fortsetzung).

## FK12: Wertungen und Prüfungen Chat-Claudes seit dem 18.09.

**Quellen:**
- Die Dokumente vom 20.09. mit SHA-256 in R57.
- Texte Chat-Claudes in Philipps Nachrichten und im Kurzprompt der Fassungen v2–v5.
- Mit * markierte Zeilen nennen Chat-Claude nicht ausdrücklich. Sie sind nach Ich-Form und Inhalt als seine Texte eingeordnet (Auslegung Hermes: Philipp leitet Chat-Claudes Texte weiter, R29 §2 „Kurzprompt für den Telegram-Chat").
- „Hermes tat" verweist auf die Chronikzeile.
- Die Wertungen stehen hier im Wortlaut-Kern. TORE (FK24, Spalte „Chat-Claudes Wertung") verweist auf die P-Nummern, statt sie zu wiederholen.

| Nr | Datum · id | Gegenstand | Ergebnis (Wortlaut-Kern) | Hermes tat |
|---|---|---|---|---|
| P01 | 19.09. 00:36 · 831 (v2, Kurzprompt Z. 331) | Phase 1, Lauf 2 | „Wertung Chat-Claude zu Lauf 2: Tor 1 steht bei 7 von 9, S1 ist nicht behoben" (Bericht: 8 von 9) | Nachlauf, Läufe 6–10 (C002) |
| P02 | 19.09. 02:23 · 997 (v3 Z. 347)* | Nachlauf Phase 1 | „Tor 1 ist mit 9 von 9 abgenommen, Phase 1 abgeschlossen" | Phase 2 (C003) |
| P03 | 19.09. 12:39 · 1393 (v4 Z. 374)* | Phase 2 | „Phase 2 ist mit 10 von 11 gewertet — Zeile 7 verlangt ‚angenommen und im Werk'" | Nachprobe in Phase 3 (C004) |
| P04 | 19.09. 18:08 · 2135* | Phase 3, laufend | Doppelungserkennung prüft „Meldungsklasse und Ort statt der Behauptung" — Befund, Korrektur erst in Fassung 5 | in den Bericht, Lauf 20 zu Ende (C004) |
| P05 | 19.09. 19:28 · 2231 | Phase 3, Teil 2 | „Vorläufige Wertung: Artgedächtnis-Zeile nicht erfüllt …, Tor 2 Zeile 8 rückwirkend gerissen (Doppelungsanteil 83,6 % …) — Phase 2 sinkt auf 9 von 11" | Teil 1 erneut gesendet (2233); Zahl später berichtigt (W02) |
| P06 | 19.09. 19:35 · 2232 (v5 Z. 406) | Phase 3 | „Phase 3 ist mit 7 von 11 abgenommen, deine Wertung war richtig" | Nachlauf (C005) |
| P07 | 19.09. 20:14 · 2234* | Bericht Phase 3, Teil 1 | „stimmt Zahl für Zahl mit dem Bericht überein … Phase 3 ist abgeschlossen" | weiter mit dem Nachlauf |
| P08 | 19.09. 20:29–23:55 · 2252 … 2688 | Nachlauf-Zwischenmeldungen | 16 Festlegungen, meist gekennzeichnet „(Chat-Claude, Fassung 6)"; 22:36 „Deine Korrektur trifft mich … das Gate hatte recht"; 22:56 „68,5 % gemessen statt 83,6 % geschätzt" | je Festlegung eingebaut und belegt (R44, 20:16–23:42) |
| P09 | 20.09. 00:55 · 2798 | Nachlauf Phase 3 | „Nachlauf abgenommen"; „Phase 3 auf 8 von 11 (Projektgedächtnis erfüllt — … deine Nachrechnung maß Token statt Ziele, das Organ hatte recht)"; Phase 2 Zeile 8 auf 68,5 % | Vorbedingung 1 (C006) |
| P10 | 20.09. 01:47 · 2844/2846 (PRUEFUNG, `842383d1…`) | Vorbedingung 1, BERICHT | „Ergebnis: Vorbedingung 1 nicht abgenommen"; Befunde F1–F7; Maß Filtergüte statt 0,0 % | N1–N6 (2901); BERICHT mit Berichtigungsvermerk (R30) |
| P11 | 20.09. 02:01 · 2902/2903 (PRUEFUNG2, `ad26f5ff…`) | Nachgang | „noch nicht abgenommen"; „Generation 6 des Lauf-23-Fortsetzungslaufs ist gescheitert" | N7–N9 (2934); Befund zurückgenommen (W09) |
| P12 | 20.09. 02:25 · 2935/2963 (PRUEFUNG3, `a7ac1686…`) | N7–N9, Abholadresse | „nicht abgenommen — … weil sie an der Abholadresse nicht liegen"; offen N10 | Server geprüft (2966, W03); N10 dreht das Ergebnis, kein Abnahmeantrag (2962) |
| P13 | 20.09. 02:46 · 2967/2969 (PRUEFUNG4, `d899daff…`) | N10, N11, Abrufweg | „Vorbedingung 1 nicht erfüllt … gestützt auf seine Meldung, nicht auf eigene Ausführung"; V12 nummerierte Dateinamen; Sperre C im Kern statt V9 | V12, V9, C gebaut (3004) |
| P14 | 20.09. 03:12 · 3005 (Lauf-25-Auftrag, `07f3f519…`) | Auftrag mit vorab gesetztem Maßstab (Pfadnachweis) | kein Prüfergebnis; Grundlage „Prüfung 5" NICHT GEFUNDEN | Lauf 25 (C008) |
| P15 | 20.09. 04:00 · 3057/3058 (PRUEFUNG6, `060090b0…`) | Lauf 25 | „nicht abgenommen"; Kasse geht nicht auf (659 gegen 848 Aufrufe, 0,3976 €); Pfadnachweis an einer von zwei Stellen; „2 Sperrungen" sind ein Fall | N12–N14 (3101); Lücke aufgelöst über die Einzelzeile Lauf 22 (Teil 3, X01) |
| P16 | 20.09. 04:50 · 3102/3104 (ABNAHME, `8a5a470f…`) | Vorbedingung 1 | „Wertung: ABGENOMMEN", Geltungsbereich eng; Kassenstand Lesart A; Verzeichnis für Fassung 7 | Wiedereinstieg (C011) |
| P17 | 20.09. 05:04 · 3159/3161 (ANTWORT_W1-W4) | W1–W4 | W4-Widerspruch als eigener Fehler; „Weg 2" mit vier Auflagen; W2: „die 0,0002 € sind keine Abweichung, sondern Rundung"; V20 „rund 1,299 €" | W1, W2 erledigt; Rundung widerlegt (W01) |
| P18 | 20.09. 05:25 · 3217/3218, 3219/3223 (PRUEFUNG_Wiedereinstieg, `55b23bc0…`) | Gedächtnisordner, Trägernachweis | „Ablieferung geprüft und tragfähig"; „meine Rundungserklärung war falsch"; W5 (Anmeldelage, nicht Gegenstand), W6 | W6 offen (3338); Vermutung zu W6 widersprochen (W04) |
| P19 | 20.09. 15:28 · 4317 | Gesamtstand | „Bestandsaufnahme abgenommen und geprüft"; zurückgenommen: Norm-Zeile Tor 2 und „4 von 4 bestanden" (leerer Durchlauf); Läufe 22/23 unter Vorbehalt | Reparatur 01 (C014) |
| P20 | 20.09. 16:12 · 5205 | Reparatur, Zwischenstand | „Zwischenstand geprüft, Richtung stimmt" | Reihenfolge geändert (C014) |
| P21 | 20.09. 18:21 · 6462 | Skip-Fehler | „Geprüft, Fehler sauber reproduziert"; Satz „Ein Nachweis zählt nur, wenn er ausgeführt wurde" | zweite und letzte Runde, Eskalation (7731) |
| P22 | 20.09. 21:14 · 7913* | Reparatur 02 | „Reparatur 02 abgenommen — alle vier Torzeilen erfüllt" | Vorbedingung 1 neu (C016) |
| P23 | 20.09. 22:55 · 8461 | VB1-Lauf 26 | „Wertung: nicht abgenommen, ich folge dir" — Review ohne Urteil abgebrochen, K2689 nie ausgeführt | enger Nachtrag (C017) |
| P24 | 21.09. 00:07 · 8749* | Nachtrag | „Vorbedingung 1 abgenommen" mit 9,09 %: „Tor 2 Zeile 8 ist damit erfüllt" | Übergabe (C018); Bezugsgröße später nicht belegbar (W05) |
| P25 | 21.09. 02:14 · 9106* | Phase 4 | „Das Handelssystem ist als Phase-4-Werk gestrichen: Es war eine nie bestätigte Vorentscheidung von mir" | T3 (C022) |
| P26 | 21.09. 03:35 · 9696, 10252* | Verfassungsentwurf T3 | „Verfassung bestätigt mit drei Auflagen" | verfassung-02 (C024) |
| P27 | 21.09. 05:38 · 10256, 10258 | verfassung-02 | „Chat-Claude hat sie geprüft, alle drei Auflagen korrekt" | T3-Lauf 26 (C025) |
| P28 | 21.09. 06:24 · 10514* | Läufe 27/28 | drei Zahlen widersprechen sich; Median aus drei Werten | „Ihr Medianeinwand ist richtig, meine Erklärung war falsch" (Meldung 10525) |
| P29 | 21.09. 06:52 · 10550* | Vorspann Lauf 29 | „Vorspann bestanden — der erste Beleg, dass das Messgerät außerhalb von Python trägt"; „die genannten Teile ergeben 84" | Lauf 29 (C027) |
| P30 | 21.09. 12:05 · 10669 | Anhalten nach Lauf 30 | „Richtig angehalten — drei Vorentscheidungen von Chat-Claude" | Commits, Lauf 31 (C028) |
| P31 | 21.09. 13:01, 13:50 · 10720, 10766* | Commits; Umgang mit dem Block | „Commits sauber"; „die Reaktion darauf war falsch" | Regel übernommen, Gegenproben (C030) |
| P32 | 21.09. 15:57–20:15 · 10830*, 10946*, 11013*, 11033, 11135 | Läufe 31–35 | „Richtig behandelt"; „Erste echte Verbesserungen"; „Klasse statt Stelle, genau richtig"; „Unbequem und richtig gemessen"; „Richtig angehalten" | Läufe 32–36 (C031–C036) |
| P33 | 22.09. 14:52 · 11301 | T3 abschluss-01 | „Wertung Chat-Claude: nicht abgenommen, weil fünf Torzeilen aus Tor 4 im Bericht fehlen" | abschluss-02 (C037) |
| P34 | 22.09. 15:15 · 11434 | abschluss-02 | „Wertung Chat-Claude: T3 nicht abgenommen"; Doppelungsanteil 35 % gegen 9 % in Python | Kernänderung 2 angehalten (W05) |
| P35 | 22.09. 15:32 · 11505 | Review-Befund K2934 | „der wichtigste des ganzen Projekts"; „mein Vergleich mit den 9,09 % war falsch"; Aufnahmesperre „null von null" prüfen | drei Punkte, Lauf 38 (C039); W06 |
| P36 | 23.09. 05:41 · 11575* | Lauf 38 | „Unbequem und richtig gemeldet — und der Fehler ist auch meiner … Kein weiterer Lauf an T3" | abschluss-03 (C040–C042) |
| P37 | 23.09. 15:03 · 13912 | Sperre 3, Laufzeit-Grenzmaß | zwei Entscheidungen Chat-Claudes | in abschluss-03 (C042) |
| P38 | 23.09. 15:53 · 14000* | abschluss-03 | „T3 sauber abgeschlossen — abschluss-03 ist der gründlichste Bericht bisher" (T3 bleibt „nicht abgenommen") | Runde 1 vor T4 (C043) |
| P39 | 23.09. 22:32 · 14624 | Runde 1 | „Richtig, nicht abgenommen"; „mein Prüfstein ‚K2868 muss bestehen' war falsch" | Runde 2 (C045) |
| P40 | 24.09. 02:14 · 15154 | Runde 2 | „Richtig nicht abgenommen" | Runde 3 (C046) |
| P41 | 24.09. 11:38 · 15962* | Anhalten an Sperren | „Richtig angehalten" | Veröffentlichung Runde 3 (C047) |
| P42 | 24.09. 11:49 · 15992 | Runde 3 | „Sauber veröffentlicht" | Runde 4 (C048) |
| P43 | 24.09. 16:48 · 16482 | Runde 4 und Review 04 | „geschlossen für die Probenfälle, nicht als Fehlerklasse"; Entscheidungen Chat-Claudes | Runde 5 (C049) |
| P44 | 24.09. 21:00 · 16769* | Runde 5, laufend | Abweichung „widerspricht Entscheidung 3"; „mein Auftrag ‚bis eingang nicht mehr sperrt' war ein Fehler" | rote Spezifikation R6-1 (C050) |
| P45 | 24.09. 23:15 · 16901 | Runde 5, zwei Reviews | „Es gilt das zweite Review … beim ersten ist nicht auszuschließen, dass es das überschriebene Skript ausgeführt hat" | Begründung widersprochen (W07), Runde 6 |
| P46 | 25.09. 00:27 · 17217* | Abschluss Runde 5 | „Runde 5 sauber abgeschlossen … mein Grund für die Wahl des zweiten war falsch, die Wahl bleibt" | U-1 bis U-4 eingeordnet (C052) |

Nach dem 25.09. 00:27 ist bis zum Lesezeitpunkt keine weitere Wertung Chat-Claudes angekommen: Philipps Nachrichten 17359, 20987 und 20990 enthalten keine.

### Befunde Chat-Claudes, die Hermes für falsch hält oder hielt — je mit beiden Belegen

| Nr | Befund Chat-Claudes | Beleg Hermes | Stand |
|---|---|---|---|
| W01 | ANTWORT_W1-W4 §3: „0,5166 − 0,1190 = 0,3976 … gemessen 0,3978 … keine Abweichung, sondern Rundung" (P17) | 3215: „Die Erklärung ‚nur Rundung' stimmt nicht; die alte Fortsetzungszahl war falsch"; REGELN-01 zu Regel 26: „Die konkrete Rundungsbegründung im Begleitbrief wurde von Hermes anhand der Rohdaten widerlegt" (R31 Z. 125) | Chat-Claude: „meine Rundungserklärung war falsch" (P18). Kassenzahlen: Teil 3, X01–X03 |
| W02 | 2231: „Doppelungsanteil 83,6 %" (P05) | 2563 (19.09. 22:38:16, Z. 676): „Die 83,6 % aus meinem Phase-3-Bericht waren eine Heuristik; mit dem gebauten Schlüssel sind es 68,5 %". Die Zahl stammte aus Hermes' eigener Meldung 2230 (19:26:48, Z. 394): „mit deiner Lesart steigt der Phase-2-Anteil von gemeldeten 2,5 % auf 83,6 %" | von Chat-Claude übernommen (2564, 2798) |
| W03 | PRUEFUNG3: N7–N9 „liegen nicht an der Abholadresse" (P12) | 2966: „der Server liefert den aktuellen Stand … Ein Zwischenspeicher liegt nicht auf meiner Seite" | Chat-Claude bestätigt, dass sein Abrufweg den alten Stand liefert (2969), Folge: V12 |
| W04 | PRUEFUNG_Wiedereinstieg Z. 16: „Die Differenz von 5 sind vermutlich die Listen- und Prüfsummendateien beider Ordner." | 3338 (20.09. 05:57:03, Z. 1211): „Chat-Claudes Vermutung … stimmt aber nicht: davon gibt es 12 (10 im Vorbedingungsordner, 2 im Gedächtnisordner)"; W6 bleibt offen | offen, keine Antwort Chat-Claudes gefunden |
| W05 | 11434: Doppelungsanteil in TypeScript 35 % gegen 9 % in Python, „Ursache finden … und beheben" (P34) | 11483 (Z. 2778): „Die Prämisse trifft nicht zu" — Ansagen-Ebene Python 43,5 % (10 von 23), TypeScript 35,1 % (20 von 57); die 9,09 % keiner Bezugsgröße zuzuordnen | Chat-Claude: „mein Vergleich mit den 9,09 % war falsch" (P35) |
| W06 | 11505: Aufnahmesperre „null von null in beiden Läufen" (P35; die Zahl stammte aus Hermes' eigener Meldung 11483) | 11556 (Z. 2825): „die Vermutung trifft nicht zu … 13 Prüfungen, 14 Tests, 2 Sperren in Lauf 37. Mein ‚0 von 0' war ein Auswertungsfehler" | von Hermes berichtigt; keine weitere Stellungnahme gefunden |
| W07 | 16901: erstes Review verworfen, weil „nicht auszuschließen, dass es das überschriebene Skript ausgeführt hat" (P45) | 17210: „Laut Delegationsprotokoll hat das erste Review das überschriebene Skript nicht mehr ausgeführt"; `ZWEI-REVIEWS.md` Z. 27–29 | Chat-Claude: „mein Grund … war falsch, die Wahl bleibt" (P46) |
| W08 | P01 (Tor 1 „7 von 9") gegen Bericht Phase 1 („8 von 9", R30) | keine ausdrückliche Gegenrede gefunden | durch P02 überholt (9 von 9) |
| W09 | PRUEFUNG2: „Generation 6 … ist gescheitert" (P11) | N7 (2934): nie begonnen, Aufruf nach Sättigung abgewiesen | Chat-Claude: „meine Überlesung" (2963) |

Nicht aufgenommen sind Suchtreffer zur Träger- und Anmeldelage, etwa zur Kontextgrenze eines Trägermodells und zur Verdichtung (Meldungen Z. 1225, 2138, 3282 ff.). Sie sind nicht Gegenstand (Auftrag §2 Nr. 15).

**Offene Zuordnung:** id 1959 (19.09. 16:39) zählt in `v2` als Systemhinweis. Nach den Vermerken „[System note …]" und „[Note: model was just switched …]" folgt aber ein Auftragstext („Wiedereinstieg nach Modellwechsel: Prüfe zuerst mit ps …"). Ob er von Philipp oder Chat-Claude stammt, ist UNBEKANNT. Weg: Philipp fragen oder das Gateway-Protokoll dieser Minute lesen. Die Zählung 114 bleibt davon unberührt, solange Hermes' Einordnung gilt.

### Reviews durch Hermes-Subagenten (keine Prüfungen Chat-Claudes, getrennt geführt)

Diese Reviews sind Arbeiten ohne Lauf. Sie stehen in den Chronikzeilen der Runden; die Befunde gehören nach TORE und LAGE. Hier nur Bestand und Gültigkeit (R128):

| Runde | Datei (Arbeitsordner = Prüfkanal, gleiche SHA-256) | Bytes | sha256 (16) | Stand |
|---|---|---|---|---|
| 1 | `biotop-vor-t4/REVIEW.md` | 21.150 | `caf4744dc4193c60` | ein Durchgang (C043) |
| 2 | `biotop-vor-t4-02/REVIEW.md` | 30.546 | `e8d972c8c34b41ed` | ein Durchgang (C045) |
| 3 | `biotop-vor-t4-03/REVIEW.md` | 26.159 | `acbd3440f30182ca` | ein Durchgang (C046) |
| 4 | `biotop-vor-t4-04/REVIEW.md` (Fassung A) | 33.169 | `2f5b01050d91bf95` | im Bericht §10: „18 Befunde: 2 hoch, 8 mittel, 8 niedrig" |
| 4 | `/tmp/review-vor-t4-04/REVIEW-B.md` (Fassung B, nicht im Prüfkanal) | 30.465 | `f265ea09a0b6dad1` | 19 Befunde (16498); Hermes' Frage „Du musst entscheiden, welche Fassung gilt" — Entscheidung NICHT GEFUNDEN |
| 5 | `biotop-vor-t4-05/REVIEW.md` (zweiter Durchgang, gilt nach P45) | 32.029 | `f66c7b6aaef14975` | identisch mit `/tmp/review-vor-t4-05/REVIEW.md` |
| 5 | `…-05/REVIEW-verworfen-erster-durchgang.md` | 31.508 | `c2af48debecf7f31` | verworfen, `ZWEI-REVIEWS.md` (5.704 Bytes) |
| 6 | — | — | — | kein Review zum Lesezeitpunkt |

Die Reviews der T3-Abschlüsse, der Reparaturen und von VB1 stehen nur als Subagentenaufträge in Teil 1 (C013–C017, C036, C037, C042). Einzelne Befunde sind nicht aufgenommen, weil FK12 nach Prüfungen Chat-Claudes fragt.
