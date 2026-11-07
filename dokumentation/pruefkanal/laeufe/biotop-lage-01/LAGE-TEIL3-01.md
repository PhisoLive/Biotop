# BIOTOP-LAGE-01 · Fassung 2 · `LAGE-TEIL3-01.md`

- **Inhalt:** Abgleich des Wissensstands WS01–WS19; FK23, FK25, FK26, FK44, FK45 · Entwurf G, Stück 2 von 2
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil G, Arbeitszeit 25.09.2026 16:10:47–18:16:10 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/lage-werke/LAGE-BAUSTEINE-G-TEIL2.md` · 33101 B · SHA-256 `5fb27c1f10dc08d63abca86a1385cec1cf5dc8c6bb5163dcb475907405d0722d`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (24 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# LAGE-Bausteine G, Teil 2: FK23, FK25, FK26, FK44, FK45

Entwurf für `LAGE` (BIOTOP-LAGE-01 Fassung 2). Geschrieben von einem Subagenten im Auftrag von Hermes (HERMES-1).
Stand des Lesens: 25.09.2026, 16:11 bis 17:45 CEST. Den Endstand von S1c und der Runde 6 trägt Hermes nach.

## Lesehilfe

Es gilt die Lesehilfe des Abgleichs WS01–WS19 (`LAGE-BAUSTEINE-G-TEIL1.md`). Kurz:
- `v8 Z. n` ist Zeile n der gültigen Masterprompt-Fassung 8: `arbeit/dokumente/2026-09-23_155353_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md`.
- `id n` ist eine Nachricht aus dem berichtigten Verzeichnis `arbeit/verlauf/v2/wortlaut.jsonl`. Der Absender ist Philipp, wenn nichts anderes steht. Zeiten sind in CEST.
- `R<n>` ist ein Rohbeleg. `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` steht für die Adresse der Läufe im Prüfkanal.
- **Datenbankzweige:**
  - STAMM: `/root/biotop/daten/biotop.db`
  - VB1: `/root/phase-4-vorbedingung-1/privat/biotop.db`
  - R02: `/root/reparatur-02/privat-cli/privat.db`
  - T3: `/root/biotop-t3/t3.db`
- **Zahlen, die in andere Dateien gehören, stehen hier nicht:**
  - Torzeilen und Messgerätfehler stehen in `TORE`.
  - Kosten und Budgets stehen in `CHRONIK` (FK20) und `KASSE`.
  - Verfassungen stehen in `VERFASSUNGEN`.

---

## FK23 — Stand jeder Phase

**Stufen:**
- Es gibt fünf Stufen: nicht begonnen, läuft, abgenommen, eng abgenommen, gescheitert.
- „Abgenommen“ steht nur da, wo eine Abnahme durch Chat-Claude oder Philipp belegt ist.
- Wo der Wortlaut der Quellen zu keiner Stufe passt, steht der Wortlaut da. Die Zuordnung ist dann als Auslegung Hermes gekennzeichnet.
- Die Lauf-Bereiche stammen aus den Köpfen der Änderungsverzeichnisse `arbeit/fassungen/aenderungen-v2.md` bis `-v7.md`, aus der Abnahme vom 20.09. und aus den Datenbankzweigen (R87, R153).

| Abschnitt | Stufe | Datum und Beleg | Abschlussordner |
|---|---|---|---|
| Phase 1 „Das Skelett“ (Lauf 2; Nachlauf Läufe 6–10) | **abgenommen** | Die Abnahme folgte auf den Nachlauf: „Tor 1 ist mit 9 von 9 abgenommen, Phase 1 abgeschlossen“ (id 997, 19.09.2026 02:23:42). v8 Z. 372: „geprüft durch Chat-Claude am Bericht … Phase 1 ist abgeschlossen; Phase 2 ist freigegeben.“ | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/`, `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/` |
| Phase 2 „Der Schwarm“ (Läufe 11–13) | **abgeschlossen und gewertet**; ein Abnahmewort ist NICHT GEFUNDEN | „Phase 2 ist mit 10 von 11 gewertet“ (id 1393, 19.09.2026 12:39:25). Mit Fassung 6 berichtigt auf „9 von 11“ (v8 Z. 390; id 2798, 20.09.2026 00:55:54). | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/` |
| Phase 3 „Gedächtnis, Mentor, Oberfläche“ (Läufe 14–20) | **abgeschlossen und gewertet** | „Phase 3 ist abgeschlossen, keine Nachfragen.“ (id 2234, 19.09.2026 20:14:46). Wertung: „8 von 11 voll, 1 teilweise, 2 im Nachlauf erledigt“ (v8 Z. 410). | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/` |
| Nachlauf zu Phase 3 (Läufe 21–23) | **abgenommen**, danach teilweise unter Vorbehalt | „Nachlauf abgenommen, alle neun Punkte geprüft“ (id 2798, 20.09.2026 00:55:54). Vorbehalt am 20.09.2026 15:28:25 (id 4317) für die Läufe 22 und 23 und für die Norm-Zeile; Wortlaut im Abgleich WS05 und WS06. | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/` |
| Vorbedingung 1 aus Phase 4, erster Durchgang (Läufe 22–25) | **eng abgenommen** | Dokument Chat-Claudes `arbeit/dokumente/2026-09-20_045016_ABNAHME_Vorbedingung-1_2026-09-20.md`: „Wertung: ABGENOMMEN. … Geltungsbereich ist eng“. Philipp übermittelte es am 20.09.2026 um 04:50 (id 3102, 3104). | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/` (Nachgänge `NACHGANG-03` bis `-06`) |
| Bestandsaufnahme, 20.09. | **abgenommen** | „Bestandsaufnahme abgenommen und geprüft“ (id 4317, 20.09.2026 15:28:25). | Auslegung Hermes nach der Zeit: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/` |
| Reparatur 01 | **gescheitert** (Auslegung Hermes) | Grundsatz 9, v8 Z. 126: „Zwei Reparaturrunden mit zwei Reviews, Fixagenten und Audits der Audits scheiterten; die dritte mit einem Reviewdurchgang gelang“. | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/` |
| Reparatur 02 | **abgenommen** | „Reparatur 02 abgenommen — alle vier Torzeilen erfüllt“ (id 7913, 20.09.2026 21:14:38). | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/` |
| Vorbedingung 1, zweiter Durchgang (Lauf 26, Zweig VB1) | **abgenommen** | Erst „Wertung: nicht abgenommen“ (id 8461, 20.09.2026 22:55:04), dann „Vorbedingung 1 abgenommen.“ (id 8749, 21.09.2026 00:07:30). | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-01/` (nicht abgenommen) und `…/abschluss-02/` (abgenommen) |
| Vorbedingung 2 aus Fassung 6 (Verfassung des Handelssystems) | **entfallen** | Fassung 7 strich das Handelssystem (id 9106, 21.09.2026 02:14:40; v8 Z. 14). | — |
| Phase 4 „Der Breitentest“ | **läuft** | Sie begann mit dem Auftrag für T3 (id 9106, 21.09.2026 02:14:40). | je Testwerk ein eigener Ordner |
| T3 `versandwerk` (Läufe 26–38, Zweig T3) | **abgeschlossen, nicht abgenommen**. Nächste Stufe: gescheitert (Auslegung Hermes) | „Wertung Chat-Claude: T3 nicht abgenommen.“ (id 11434, 22.09.2026 15:15:11). „Kein weiterer Lauf an T3, die Grenze war hart.“ (id 11575, 23.09.2026 05:41:59). Kopf von ABSCHLUSS-03 (23.09.): „nicht abgenommen“. „T3 sauber abgeschlossen“ (id 14000, 23.09.2026 15:53:55). Einschränkung: v8 Z. 434 nennt neue Messgerätfehler ausdrücklich „kein Scheitern“. | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/` mit `abschluss-01/`, `abschluss-02/`, `abschluss-03/` (Änderungszeiten 22.09. 06:57, 22.09. 15:24, 23.09. 15:47; R120) |
| Behebungsrunde 1 vor T4 | **nicht abgenommen** | Kopf des Berichts: „nicht abnahmereif“. „Richtig, nicht abgenommen“ (id 14624, 23.09.2026 22:32:40). | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/` |
| Behebungsrunde 2 | **nicht abgenommen** | Kopf: „nicht abgenommen“. „Richtig nicht abgenommen“ (id 15154, 24.09.2026 02:14:45). | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-02/` |
| Behebungsrunde 3 | **nicht abgenommen** | Kopf: „nicht abgenommen“. Es folgte „Sauber veröffentlicht“ und der Auftrag für Runde 4 (id 15992, 24.09.2026 11:49:51). | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-03/` |
| Behebungsrunde 4 | **kein Abnahmewort** | Kopf: „Gegenproben der Entscheidungen 1, 3 und 4 erfüllt; … für ihre Probenfälle geschlossen, die Fehlerklassen nicht“. „Aber das Review sagt es selbst — geschlossen für die Probenfälle, nicht als Fehlerklasse.“ (id 16482, 24.09.2026 16:48:07) | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-04/` |
| Behebungsrunde 5 | **nicht abgenommen** | Kopf: „nicht abgenommen“. „Runde 5 sauber abgeschlossen“ (id 17217, 25.09.2026 00:27:35). | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-05/` |
| Behebungsrunde 6 | **läuft** | Im Prüfkanal liegen nur vier Zwischenberichte vom 25.09., 00:06 bis 01:12 (R26). Arbeitsstand: `/root/biotop-vor-t4-06/UEBERGABE.md`, Änderungszeit 25.09.2026 12:52:04. Der letzte Eintrag, um 12:55, endet mit „S1c gestartet“. | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-06/` (nur Zwischenberichte) |
| T4, T5, T6 | **nicht begonnen** | Es gibt kein Werk (Baustein FK25). Die Bedingung für den Start von T4 steht in id 16901 (Baustein FK44). | — |
| T7, T8 | **nicht begonnen**, nur bei Bedarf | Sie kommen nur dazu, wenn die Sättigungsregel es verlangt (v8 Z. 452). | — |
| Phase 5 „Erstes echtes Werk“ | **nicht begonnen** | „Werk: noch nicht bestimmt.“ (v8 Z. 480) | — |
| weitere Phasen | **keine in v8** | Abschnitt 8 von v8 endet mit Phase 5. „Phase 6“ hat 0 Treffer in v8 (R130 Abschnitt e). | — |

**Kurzfassung:**
- Abgenommen mit Beleg sind:
  - Phase 1 samt Nachlauf,
  - der Nachlauf zu Phase 3 (später teilweise unter Vorbehalt),
  - Vorbedingung 1 (am 20.09. eng, am 21.09. nach Lauf 26),
  - die Bestandsaufnahme,
  - Reparatur 02.
- Phase 2 und Phase 3 sind abgeschlossen und gewertet. Ein Abnahmewort habe ich für sie nicht gefunden.
- Kein Testwerk des Breitentests und keine Behebungsrunde vor T4 ist abgenommen.

Weitere Ordner ohne Phasenrang sind `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/`, `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-einstieg-20260921-01/` und `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/` (R26). Ihren Inhalt habe ich nicht gelesen.

---

## FK25 — Werke

**Zählweise:**
- Die Zahlen sind mit find, wc und grep nur lesend gezählt, Stand 25.09.2026 16:27 CEST (R74, Skript `entwurf/lage-werke/g1_werke_umfang.sh`).
- „Dateien“ sind alle Dateien ohne `.git`, `node_modules`, `__pycache__`, `.pytest_cache`, `.mypy_cache`, `dist` und `coverage`.
- „Quelle“ sind Dateien `*.py`, `*.ts`, `*.js` und `*.mjs` außerhalb von `tests/`. „Tests“ sind dieselben Endungen in `tests/`.
- „Testfunktionen“ sind Zeilen `def test_…` in Python. In TypeScript sind es Zeilen, die mit `it(` oder `test(` beginnen.
- Das Ergebnis der Läufe steht hier nur als Status. Die Torzeilen stehen in `TORE`.

### `lagerhaus` — Übungswerk 1 (Phasen 1 bis 3, Vorbedingung 1)

- **Art.**
  - Wortlaut v8 Anhang A, Satz 1: „Ein Rabatt- und Lagerrechner für Verkaufsberichte. … Es ist ein Übungswerk ohne Betriebszweck.“
  - Python mit pytest. Vier Bereiche: `formeln`, `preise`, `lager`, `bericht` (Anhang A, Satz 4).
  - Vorgabe für Phase 1 (v8 Z. 358): „Hermes baut ein Werk mit drei Bereichen (~800–1.200 Zeilen, mit Tests) … Ein vierter, bereits sauberer Bereich dient als Halluzinationsprobe.“
- **Neue Art?** Nein. Es ist das Ausgangswerk. v8 Z. 416 zählt es mit `logmuehle` als „zwei Werke derselben Art“.
- **Pfad.**
  - Ausgang: `/root/uebungswerk` (git, Ordner-Änderungszeit 18.09.2026 23:26:44).
  - Eingelegt: `/root/biotop/daten/werke/lagerhaus`, Werk-id 1, aufgenommen am 18.09.2026 um 23:44:52 CEST (R31).
- **Umfang am Ausgang:** 19 Dateien. Quelle: 12 Dateien mit 508 Zeilen. Tests: 4 Dateien mit 348 Zeilen. 50 Testfunktionen (R74).
  - v8 Z. 416 nennt „`lagerhaus` (856 Zeilen)“. Gerechnet: 508 + 348 = 856. Das ist Quelle und Tests zusammen.
- **Umfang am letzten Stand:**
  - Lauf 26 im Zweig VB1: `/root/phase-4-vorbedingung-1/privat/werke/lagerhaus-vorbedingung1-26`. 43 Dateien. Quelle: 12 Dateien mit 757 Zeilen. Tests: 28 Dateien mit 790 Zeilen. 104 Testfunktionen.
  - Lauf 25 im Stamm: `/root/biotop/daten/werke/lagerhaus-c-25`. 41 Dateien. Quelle: 12 Dateien mit 721 Zeilen. Tests: 26 Dateien mit 766 Zeilen. 100 Testfunktionen.
- **Verfassung:** ja, v8 Anhang A: „Geschrieben von Chat-Claude (Philipp hat die Entscheidung delegiert). Gilt für Lauf 3 und alle weiteren Läufe am Übungswerk.“ Einzelheiten in `VERFASSUNGEN`.
- **Läufe im Stamm:** 22 der 25 Stamm-Läufe (R153; die übrigen: zwei an `logmuehle`, Lauf 11 ohne Werk). Status laut Datenbank:
  - 8 abgebrochen (Läufe 1, 4, 5, 6, 7, 8, 10, 12);
  - 6 verworfen (14, 15, 16, 18, 19, 21);
  - 3 „bereit“ ohne Endzeit (2, 24, 25);
  - 2 beendet (9, 13);
  - 2 gesättigt (20, 22);
  - 1 gestoppt: Lauf 3 mit „Messgerät fehlt“ am Probewerk `lagerhaus-ohne-tests`. Die Werk-id ist in der Laufzeile leer.
  - Summe: 8 + 6 + 3 + 2 + 2 + 1 = 22 (gerechnet).
- **Läufe in anderen Zweigen:** Lauf 26 im Zweig VB1 ist „gesaettigt“. Lauf 26 im Zweig R02 steht auf „kartiert“, ohne Generation (R87).

### `logmuehle` — Übungswerk 2 (Phase 3 und Nachlauf)

- **Art.**
  - Wortlaut v8 Anhang B, Satz 1: „Ein Befehlszeilenwerkzeug, das Zugriffsprotokolle im Common Log Format liest, … Übungswerk ohne Betriebszweck“.
  - Python mit pytest. Vier Bereiche: `lesen`, `filtern`, `zaehlen`, `ausgabe` (Anhang B, Satz 4).
- **Neue Art?**
  - Für Phase 3 wurde es als „zweites Übungswerk anderer Bauart als `lagerhaus`“ verlangt (v8 Z. 395), damit das Artgedächtnis etwas zu vergleichen hat.
  - Für den Breitentest ist es keine neue Art. v8 Z. 416: „beide Python, beide pytest, beide klein, beide aus Hermes' Feder, beide reine Ablauflogik ohne Oberfläche und ohne Zustand.“
- **Pfad.**
  - Ausgang: `/root/uebungswerk2` (git).
  - Eingelegt: `/root/biotop/daten/werke/logmuehle-17` (Werk-id 15) und `…/logmuehle-23` (Werk-id 20).
- **Umfang am Ausgang:** 18 Dateien. Quelle: 12 Dateien mit 482 Zeilen. Tests: 4 Dateien mit 303 Zeilen. 39 Testfunktionen (R74).
  - v8 Z. 416 nennt „`logmuehle` (482 Zeilen)“. Das ist nur die Quelle; mit Tests wären es 785 Zeilen (gerechnet).
  - Die beiden Zeilenzahlen in v8 Z. 416 haben also verschiedene Bezugsgrößen: bei `lagerhaus` Quelle und Tests, bei `logmuehle` nur die Quelle.
- **Umfang am letzten Stand:** `logmuehle-23`: 26 Dateien. Quelle: 12 Dateien mit 551 Zeilen. Tests: 11 Dateien mit 482 Zeilen. 59 Testfunktionen.
- **Verfassung:** ja, v8 Anhang B: „Entwurf Hermes, **von Chat-Claude bestätigt** (19.09.2026, am Nachlaufbericht Abschnitt 9 …)“. Philipp schrieb am 20.09.2026 um 00:55:54 (id 2798): „logmuehle-Verfassung bestätigt als Anhang B“. Einzelheiten in `VERFASSUNGEN`.
- **Läufe:** 17 und 23 im Stamm, beide „gesaettigt“ (R153).
- **Ergebnis**, v8 Z. 410: „`logmuehle` von Kernmaß −13 auf 0 mit allen drei versiegelten Schwächen behoben — bei der Sicherheitslücke hat der Schwarm den Subprozess ganz entfernt statt ihn abzusichern“.

### T3 `versandwerk` — erstes Testwerk des Breitentests

- **Art und neue Art.**
  - v8 Z. 424: „**T3 — andere Sprache und andere Werkzeugkette.** TypeScript oder JavaScript, ~1.500–2.500 Zeilen, 4–5 Bereiche, eigene Testsammlung (vitest oder jest), eigenes statisches Prüfwerkzeug.“
  - Ist-Stand: Vitest (`vitest.config.ts`). Fünf Bereiche unter `src/`: `bericht`, `eingang`, `planung`, `tarife`, `zahlen` (R108).
  - `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/MESSGERAETFEHLER.md` Z. 3: „Neue Art: TypeScript/Vitest.“
- **Pfad.**
  - Ausgang: `/root/versandwerk-t3-02`.
  - Daneben liegt `/root/versandwerk-t3`. Beide Ordner haben die Änderungszeit 21.09.2026 02:47:53. `versandwerk-t3` steht in keiner Werktabelle; seine Rolle ist UNBEKANNT.
  - Eingelegt: `/root/biotop/daten/werke/versandwerk-t3-02`, Werk-id 23 im Zweig T3 (R87).
- **Umfang (R74).**
  - `/root/versandwerk-t3`: 39 Dateien. Quelle: 25 Dateien mit 1.576 Zeilen. Tests: 9 Dateien mit 785 Zeilen. 174 Testfunktionen.
  - `/root/versandwerk-t3-02`: 41 Dateien. Quelle: 25 Dateien mit 1.605 Zeilen. Tests: 11 Dateien mit 862 Zeilen. 182 Testfunktionen.
    - Das passt zum Ausgangsbestand in ABSCHLUSS-03 §4g: „Warum der Testbestand in Lauf 38 bei 207 beginnt statt bei 182“.
  - Eingelegte Kopie, Endstand: 55 Dateien. Quelle: 25 Dateien mit 1.829 Zeilen. Tests: 24 Dateien mit 1.202 Zeilen. 213 Testfunktionen.
    - Das passt zu ABSCHLUSS-03 §4f: „Testbestand 207 → 213“.
- **Verfassung:** ja.
  - Entwurf: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/`. Versiegelt: `…/verfassung-02/`.
  - id 10252, 21.09.2026 05:14:24: „Verfassung bestätigt mit drei Auflagen, die vor dem Lauf einzuarbeiten und als verfassung-02 zu versiegeln sind — danach ist der evolutionäre Lauf freigegeben, ohne weitere Rückfrage.“
  - Einzelheiten in `VERFASSUNGEN`.
- **Läufe:** 26 bis 38 im Zweig T3, alle an Werk-id 23 (R87). Status laut Datenbank:
  - 8 „kartiert“ ohne Endzeit (26–30, 33–35);
  - 3 „laeuft“ ohne Endzeit (31, 32, 36);
  - 1 „gesaettigt“ (37);
  - 1 „bereit“ (38).
  - v8 Z. 457: „13 Läufe (26–38); elf endeten ohne Abnahme an fünf Ursachen, zwei liefen bis Sättigung beziehungsweise Budget.“
- **Ergebnis:** nicht abgenommen (`abschluss-03`). Die Torzeilen stehen in `TORE`.
- **Auffälligkeit:** Die Werkzeile trägt `aufgenommen_am` 22.09.2026 15:43:15 CEST. Das liegt nach dem Beginn der Läufe 26 bis 37, die ab 21.09. 05:43 CEST liefen. Lauf 38 begann am 22.09. um 15:42:49 CEST (R87).
  - Auslegung Hermes: Die Zeile wurde bei der Aufnahme für Lauf 38 neu geschrieben.

### T4, T5, T6

- **T4: NICHT GEFUNDEN.** Es gibt kein Werk.
  - Die Suche nach Ordnern unter `/root` bis Tiefe 2 mit t4, t5 oder t6 im Namen fand nur die sechs Arbeitsordner der Behebungsrunden, `/root/biotop-vor-t4` bis `/root/biotop-vor-t4-06` (R74 Abschnitt G).
  - `/root/biotop-vor-t4-06/UEBERGABE.md` Z. 66: „Messskript für die Aufnahme von T4 vorbereiten, nicht messen (kein T4-Werk)“.
  - Vorgabe v8 Z. 426: „Python, ~6.000–10.000 Zeilen, 8–12 Bereiche, **ohne vorhandene Testsammlung** …“.
  - Größenprobe der Runde 5: Das erzeugte Probewerk `grosswerk` hat 6 Module, 30 Funktionen und 126 Zeilen (`/root/biotop-vor-t4-05/proben/T4-GROESSE.txt` Z. 1). Es diente der Kappe der Verfälschungsläufe, „gemessen an einem Kandidaten in T4-Größe“ (id 16482, Punkt 4).
  - Danach entschied Chat-Claude (id 16901, 24.09.2026 23:15:27, Punkt 8): „Kappe am echten T4-Werk messen“.
- **T5 und T6: NICHT GEFUNDEN**, nicht begonnen. Die Vorgaben stehen in v8 Z. 428 und Z. 430.
- **Verfassung:** keine.

### Prüfwerke der Behebungsrunden (Testgegenstände)

- **Was sie sind:** Module der Eigen-Testsuite in `/root/biotop/tests/` erzeugen diese Werke für Tests.
  - Sie stehen in keiner Werktabelle (R31, R87) und haben keinen eigenen Abschlussordner.
  - Auslegung Hermes: Es sind keine Werke im Sinne des Masterprompts.
- **Umfang:** Gezählt sind nur die Erzeuger. Der Umfang der erzeugten Werke ist NICHT AUSGEFÜHRT, weil man dafür Biotop-Code ausführen müsste.

1. **Drahtwerk.** `/root/biotop/tests/drahtwerk.py`, 233 Zeilen, Änderungszeit 25.09.2026 09:28:54 (R74).
   - Kopf: „Drahtwerk: kleinstes TypeScript-Werk, an dem ein ganzer Lauf jedes Organ erreicht.“ (R130 Abschnitt h).
   - Bereiche `alpha` und `beta`. Sechs Dateien nach den Pfadangaben im Erzeuger:
     - `src/alpha/liste.ts`, `src/beta/wert.ts`;
     - `tests/test_alpha.test.ts`, `tests/test_altlast_a1.test.ts`, `tests/test_beta.test.ts`;
     - `tests/vertraege/test_vertrag_alpha_beta.test.ts`.
   - Genutzt von `test_verdrahtung.py` und `test_vor_t4_02.py`.
   - Runde 6 fuhr am 25.09. den vollen Verdrahtungstest damit („Eichphase Drahtwerk: versiegelt …“, UEBERGABE Runde 6, Eintrag 10:19).
2. **Speicherwerk.** `/root/biotop/tests/speicherwerk.py`, 187 Zeilen, Änderungszeit 24.09.2026 00:02:50.
   - Kopf: „Python-Prüfwerk „speicherwerk“ (Behebungsrunde 2 vor T4): kleinstes Python-Werk, an dem die Python-Sonde des Verhaltensvergleichs durch den Annahmepfad (aegis.pruefen) geprüft wird“.
   - Zwei Quelldateien (`speicherwerk/zahlen/statistik.py`, `speicherwerk/text/format.py`) und zwei Testdateien.
3. **probewerk.** Wird in `/root/biotop/tests/test_vor_t4_03.py` erzeugt: Z. 33 „Prüfwerk „probewerk“ (Python) und Laufweg“, Z. 34 `PAKET = "probewerk"`, README-Text „Prüfwerk ohne Betriebszweck.“ Es wird auch in `test_vor_t4_05.py` genutzt.
4. **grosswerk.** Größenprobe der Runde 5. Beschrieben unter T4.

### Kopien, zusammengefasst und gezählt

- **Werktabellen** (R31, R87, R153):
  - STAMM hat 22 Einträge: 20 `lagerhaus…` und 2 `logmuehle…`. Unter den 20 `lagerhaus`-Einträgen sind das Ausgangswerk, das Probewerk ohne Tests (Status `messgeraet_fehlt`) und 18 Kopien für einzelne Läufe (gerechnet 20 − 2).
  - VB1 hat 23 Einträge: zusätzlich `lagerhaus-vorbedingung1-26`.
  - R02 hat 22 Einträge. Dort zeigt Eintrag 22 `lagerhaus-c-25` auf `/root/reparatur-02/privat-cli/werk`.
  - T3 hat 23 Einträge: zusätzlich `versandwerk-t3-02`.
  - Die Werk-id 23 ist zweimal vergeben: in VB1 und in T3.
- **Werkordner auf der Platte** unter `/root`, bis Tiefe 6, ohne `/root/.hermes` und `/root/sicherung` (R108): 58 `lagerhaus`-Ordner, 5 `logmuehle`-Ordner, 4 `versandwerk`-Ordner, zusammen 67 (gerechnet).
  - Die 58 `lagerhaus`-Ordner verteilen sich so:
    - 7 Arbeitsordner `/root/uebungswerk*`;
    - 20 in `/root/biotop/daten/werke/`;
    - 20 in der Sicherung `/root/biotop-t3/repo-sicherung-vor-commits/daten/werke/`;
    - 4 unter `/root/phase-4-vorbedingung-1/`;
    - 6 unter `/root/reparatur-01/`;
    - 1 unter `/root/reparatur-02/`.
  - Inhaltsgleich nach der Baumprüfsumme (R74) sind:
    - `/root/uebungswerk-p2` und `lagerhaus-nachlauf9`;
    - `/root/uebungswerk-p3`, `lagerhaus-p2-13` und `lagerhaus-p3-14`;
    - `/root/uebungswerk-p3c` und `lagerhaus-p3-18`;
    - `/root/uebungswerk-p3d` und `lagerhaus-p3-19`;
    - `/root/uebungswerk-nachlauf`, `lagerhaus-p3-20` und `lagerhaus-p3-22`;
    - die Werkquelle in VB1 und das Werk in R02.
- **Schnappschüsse (Lazarus).** In `/root/biotop/daten/lazarus` liegen 93 Archive (R108). 70 gehören zu Stamm-Läufen, 23 zu den T3-Läufen 31, 32, 36, 37 und 38 (gerechnet).
  - Je Lauf ist die Zahl der Archive gleich der Zahl der angenommenen Generationen in der Datenbank. Verglichen wurden 27 von 27 Läufen mit angenommenen Generationen (R108 gegen R153 und R87, gerechnet).
  - Archive des VB1-Laufs 26 habe ich nicht gesucht.

---

## FK26 — Sättigungsregel

**Wortlaut, v8 Z. 452:**
> „**Abnahme des Breitentests — die Sättigungsregel (Entscheidung Chat-Claude, 21.09.2026):** Philipp hat die Zahl der Testwerke offengelassen. Eine feste Zahl wäre willkürlich; deshalb entscheidet dasselbe Prinzip, nach dem das Biotop selbst aufhört: **Der Breitentest ist abgeschlossen, wenn zwei aufeinanderfolgende Testwerke neuer Art durchlaufen, ohne einen neuen Messgerätfehler zu erzeugen.** Erzeugt T3 noch Fehler und T4 und T5 keine mehr, ist nach T5 Schluss; erzeugen alle vier weiterhin Fehler, kommen T7 und T8 dazu — Hermes schlägt die nächste ungeprüfte Dimension vor, Philipp entscheidet. Die Zahl wird nicht vorher festgelegt und nachher nicht verhandelt.“

**Zusatz in v8 Z. 461:** „T3 zählt nicht zur Sättigung des Breitentests.“

**Begriff „neuer Messgerätfehler“:** Hermes hat ihn am Beginn von T3 festgelegt, in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/MESSGERAETFEHLER.md` Z. 3:
> „Ein neuer Messgerätfehler ist eine erstmals an T3 belegte falsche Messung, falsche Zulassung oder fehlende erforderliche Ausführung im Kernpfad. … Behobene T3-Funde bleiben für die werkweise Sättigungsregel T3-Funde; Wiederholungsläufe sind keine neuen Werkarten.“

**Folge der Werke neuer Art:**

| Nr. | Werk | neue Art | neuer Messgerätfehler | Beleg |
|---|---|---|---|---|
| 1 | T3 `versandwerk` | TypeScript/Vitest | **ja** | v8 Z. 461 „Gefundene Messgerätfehler: …“. Die Liste steht in `TORE` (FK27). |
| 2 | T4 | Größe, fremder Stil, ohne Tests, Altlasten | — (nicht begonnen) | Baustein FK25 |
| 3 | T5 | Oberfläche | — (nicht begonnen) | v8 Z. 428 |
| 4 | T6 | Zustand und Außenwelt | — (nicht begonnen) | v8 Z. 430 |

**Zählung.**
- Aufeinanderfolgende Werke neuer Art ohne neuen Messgerätfehler: **0**. Verlangt sind 2.
- Gerechnet: T3 erzeugte neue Fehler, und kein weiteres Werk neuer Art ist gelaufen. Stand 25.09.2026 17:45 CEST.
- Auslegung Hermes zu „T3 zählt nicht“: T3 kann keines der zwei Werke ohne neuen Fehler sein. Nach dem Beispiel im Wortlaut ist der Breitentest frühestens nach T5 abgeschlossen.

**Behebungsrunden.**
- Die sechs Behebungsrunden vor T4 fanden an Prüfwerken und in Reviews weitere Messfehler. Beispiel, Kopf des Berichts der Runde 5: „an 0c2f058 sind zwei Messfehler derselben Klasse gemessen“.
- Die Prüfwerke sind keine Werke neuer Art.
- Auslegung Hermes nach MESSGERAETFEHLER.md: Diese Funde bringen die Zählung weder voran noch setzen sie sie zurück.
- Ob sie T3 zugerechnet werden, sagt keine Quelle (UNBEKANNT).

**Vor dem Breitentest.**
- v8 Z. 416: „Jedes Mal, wenn eine neue Werkart dazukam, traten sofort neue Messgerätfehler auf.“ Das bezieht sich auf `logmuehle` in Phase 3 (v8 Z. 410); die Zahl steht in `TORE`.
- Diese Werke zählen nicht für die Sättigungsregel. Die Regel gilt für Testwerke des Breitentests.

**Abgrenzung.** Die Sättigungsregel ist nicht die Sättigungsmeldung eines Laufs. Die Sättigungsmeldung gehört zur Entropie (v8 Abschnitt 3.11); ihr entspricht der Status „gesaettigt“ in den Datenbanken.

---

## FK44 — Was steht laut gültigem Masterprompt als Nächstes an?

Als Nächstes steht nach v8 der Abschluss der **Behebungsrunde vor T4** an, danach **T4**.

**v8 Z. 432:** „**Reihenfolge:** T3, T4, T5, T6 — vom größten Bruch zum kleinsten. Jedes Werk ist ein eigener Auftrag mit eigenem Abschlussordner.“

**v8 Z. 463–476, Wortlaut:**
> „**Vorbedingungen für T4 (Reihenfolge, je mit Gegenprobe durch den Laufweg):**
> 1. Laufzeit gepaart: Vorgeneration und Kandidat in derselben Sitzung, Median mehrerer Messungen je Seite; kein historisches Minimum als Bezug (Grundsatz 14). Gegenprobe: K2904 und K3091, dieselbe Änderung, werden gleich entschieden. Grenzanzeige ohne irreführende Rundung.
> 2. Verhaltensvergleich: unbeobachtet = Enthaltung; „x von y beobachtet“ in Urteil und Protokoll; Korpus aus den Verträgen erzeugt, mit Randfällen (leer, einzeln, Grenzwert), sodass jede exportierte Funktion eines geänderten Moduls gerufen wird. Gegenprobe: K3106 wird erkannt.
> 3. Sondenausfall: anhalten oder zurückstellen, keine Ablehnung, kein Gedächtniseintrag.
> 4. Verhandlung: `paar_ok` an die Tragfähigkeit des Verhaltensvergleichs binden.
> 5. Maßeichung: `anwenden` vergleicht die Eichung selbst, nicht nur ihren Marker.
> 6. Generation 0: Mehrheitsregel je Durchlauf; `tsc`-Meldung gespeichert; die Prüfung zwischen den Runden baut den Typbau mit.
> 7. Verdrahtungstest: Pflichtkanten an die Phase der Generationen gebunden; im Prüfwerk schlägt eine Regel im sauberen Bereich an; ein Laufweg-Test verlangt die Ablehnung einer ungedeckten Abweichung.
> 8. Protokoll: Kernmaß geeicht geführt, roh gekennzeichnet.
> 9. Doppelung: Behauptung für **alle** erzeugten Angriffstests protokollieren. Immunisierung auf dem TypeScript-Pfad bauen.
> 10. Projektgedächtnis: Ein Laufzeit-Grenzmaß sperrt einen Weg nur, wenn der Kandidat den Bereich berührt hat und die gepaarte Messung die Verschlechterung bestätigt; Risse in unberührten Bereichen nie.
> 11. Aus der Liste nach T3: Erreichbarkeitsführung für gedrosselte Anbieter; Verfallsbedingung der Ausnahmeliste des Python-Wächters; `_beschleunigen` entfernen; Einzelwerte der Rauschmessung speichern.
>
> Die roten Spezifikationen aus `abschluss-03` (9 Tests, am Commit `f821707` 9 von 9 rot) sind Teil dieser Vorbedingungen. Die Behebungsrunde kostet kein Modellgeld; sie endet mit voller Regression, eigenem Commit, einem Review und einem Abschlussordner.“

**Auftrag dazu.** id 14000, 23.09.2026 15:53:55: „Auftrag: die Behebungsrunde vor T4 — die elf Vorbedingungen in der dort genannten Reihenfolge, einschließlich der vier Messfragen, die Chat-Claude entschieden hat …“

**Stand gegenüber v8.**
- v8 sieht eine einzige Behebungsrunde vor. Bis zum Lesen sind fünf Runden abgeschlossen; die sechste läuft (Baustein FK23).
- Die Bedingung für den Start von T4 steht nicht in v8. Sie steht in einer Nachricht Philipps mit Entscheidungen Chat-Claudes (id 16901, 24.09.2026 23:15:27, Punkt 8):
  > „Kappe am echten T4-Werk messen; TypeScript-Proben vor T5. Regel für den Start von T4, vorab gesetzt: T4 beginnt, sobald das Review dieser Runde keinen stillen Durchlass mehr findet — jede bekannte Lücke muss eine gezählte Enthaltung sein; Lücken, die sich nur enthalten, behebt T4 im Lauf.“
- Ergänzt am 25.09.2026 um 00:27:35 (id 17217):
  > „Ordne U-1 bis U-4 nach der Startregel ein — ist einer davon ein stiller Durchlass, also eine Lücke, die falsches Verhalten ohne Enthaltung durchlässt, dann gehört er mit Gegenprobe in diese Runde; die übrigen bleiben auf der Liste.“

Den Vorschlag von Hermes für den nächsten Schritt enthält FK46, getrennt von diesem Baustein.

---

## FK45 — Restweg laut Masterprompt bis zum Ende des Vorhabens

**Allgemeine Entscheidungen Philipps**, v8 Abschnitt 10:
- „Budget je Lauf (… Phase 4 gesondert nach Kostenvoranschlag der Kasse)“;
- die Schnellmodelle;
- die Stelle des Abschlussordners;
- „Die Verfassung jedes Werks und das Maß jedes Laufs — bei Vorlage.“

Dazu v8 Z. 196: „Das Biotop schlägt das Maß vor, Philipp bestätigt, danach ist es eingefroren“.

### Die Schritte in Reihenfolge

1. **Behebungsrunde vor T4 abschließen**, derzeit Runde 6.
   - **Inhalt:** v8 Z. 463–476, siehe Baustein FK44.
   - **Vorbedingung:** Nach der Startregel (id 16901) findet das Review der Runde keinen stillen Durchlass mehr.
   - **Philipp entscheidet:** v8 verlangt hier keine Entscheidung Philipps. In der Praxis kamen Wertung und nächster Auftrag je Runde als Nachricht Philipps mit „Entscheidungen Chat-Claude“.
2. **T4 — Größe, fremder Stil, fehlende Tests, echte Altlasten.**
   - **Inhalt:** v8 Z. 426: „Hermes erzeugt es über ein anderes Modell als sein eigenes, damit Stil und Struktur nicht seine sind.“
   - **Vorbedingungen:**
     - die Vorbedingungen für T4;
     - Tor 4 je Testwerk (v8 Z. 436–450). Bei T4 gilt statt versiegelter Schwächen „eine unabhängig erhobene Altlastenliste mit Bezugsgröße“ (Z. 437);
     - das Budget je Testwerk (v8 Z. 454; Betrag in `KASSE`).
   - **Philipp entscheidet:**
     - Verfassung und Maß nach Abschnitt 10. Für Übungswerke ist die Verfassung an Chat-Claude delegiert (v8 Z. 161). Die Verfassung von T3 wurde durch eine Nachricht Philipps bestätigt (id 10252).
     - Budget „nach Kostenvoranschlag der Kasse“ (Abschnitt 10). Das steht neben dem festen Betrag in Z. 454.
     - Wer das „andere Modell“ für die Erzeugung wählt, sagt v8 nicht (UNBEKANNT).
     - Freigaben: Nach Auslegung Hermes gibt Hermes unter der Vollmacht frei, weil das Werk ohne Betriebszweck ist und von Hermes erzeugt wird (siehe Abgleich WS17).
3. **T5 — Werk mit Oberfläche** (v8 Z. 428).
   - **Vorbedingungen:**
     - „TypeScript-Proben vor T5“ (id 16901, Punkt 8);
     - „Methoden in TypeScript vor T5, nicht vor T4“ (id 15992, Punkt 5).
   - **Philipp entscheidet:** wie bei T4.
4. **T6 — Zustand und Außenwelt** (v8 Z. 430).
   - **Vorbedingungen:** keine eigenen in v8.
   - **Philipp entscheidet:** wie bei T4.
   - Nach jedem Testwerk wird die Sättigungsregel geprüft. Frühester Schluss ist nach T5 (Baustein FK26).
5. **T7, T8 und weitere**, nur wenn die Regel nach T6 nicht erfüllt ist (v8 Z. 452).
   - **Philipp entscheidet:** „Hermes schlägt die nächste ungeprüfte Dimension vor, Philipp entscheidet.“
6. **Abschluss des Breitentests.**
   - **Vorbedingung:** zwei aufeinanderfolgende Testwerke neuer Art ohne neuen Messgerätfehler (v8 Z. 452).
   - **Philipp entscheidet:** Wer den Abschluss erklärt, nennt v8 nicht (UNBEKANNT). Die Regel selbst ist als „Entscheidung Chat-Claude“ gekennzeichnet, und die Zahl der Testwerke „wird … nachher nicht verhandelt“.
7. **Phase 5 — Erstes echtes Werk** (v8 Z. 478–493).
   - **Vorbedingungen:**
     - Der Breitentest ist abgeschlossen.
     - Das Werk erfüllt die fünf Kriterien (Z. 481–485).
     - Die vier Vorbedingungen von Z. 488–491 sind erfüllt: Verfassung mit tragendem Pfad; Aufnahme und Landkarte als eigener Abschnitt; Generation minus eins und Generation 0 als eigene Abschnitte; Freigaben nur durch Philipp.
   - **Philipp entscheidet:**
     - Er wählt das Werk (Z. 480).
     - Er schreibt die Verfassung (Z. 488: „schreibt Philipp; Hermes legt einen Entwurf vor“).
     - Er setzt das Budget je Abschnitt nach dem Kostenvoranschlag aus Aufnahme und Landkarte (v8 Z. 326).
     - Er gibt jede Generation frei (Z. 491).
     - Er wählt die Richtung des Mentors (v8 Z. 167: „Philipp wählt die Richtung“).
   - **Tor 5:** „wird gesetzt, wenn das Werk feststeht“ (Z. 493). Von wem, sagt v8 nicht (UNBEKANNT).
8. **Nach Phase 5.** v8 nennt keine weitere Phase und kein Ende des Vorhabens.
   - „Phase 6“, „Ende des Vorhabens“ und „nach Phase 5“ haben 0 Treffer in v8 (R130 Abschnitt e).
   - Schluss von v8 (Z. 551): „Fortschreibung als Fassung 9 bei grundlegenden neuen Erkenntnissen.“
   - Verfassungssatz 4 (Z. 103) lässt eine Selbsthebung nur als eingelegte Kopie zu; „Philipp entscheidet, ob die gehobene Kopie das neue Werkzeug wird.“
   - **Ende des Vorhabens: UNBEKANNT**, weil es nicht festgelegt ist. Weg zur Klärung: Frage an Philipp oder Chat-Claude, oder eine künftige Fassung 9.

### Kandidaten für Phase 5

- **In v8:** keiner. Z. 480: „**Werk: noch nicht bestimmt.** Die Wahl trifft Philipp nach dem Breitentest.“
- **In den Nachrichten:** keiner.
  - Gesucht wurde nach „Phase 5“, „erstes echtes Werk“ und seinen Beugungen im ganzen berichtigten Verzeichnis `arbeit/verlauf/v2/wortlaut.jsonl`. Ergebnis: 33 Treffer (R106).
  - Alle Treffer stehen in drei Arten von Texten:
    - in Masterprompt-Texten: in v1 bis v6 „Phase 4 — Erstes echtes Werk“ mit dem Handelssystem, in v7 und v8 „noch nicht bestimmt“;
    - in einer Zusammenfassung von Hermes (id 9867);
    - im LAGE-Auftrag selbst (id 20987).
  - In `arbeit/lesen/hermes-an-philipp.md` hat „Phase 5“ 0 Treffer.
- **Früher genannt:** In v1 bis v6 stand das KI-Handelssystem als erstes echtes Werk, damals in Phase 4. Es war nach v8 Z. 14 „eine nie bestätigte Vorentscheidung von Chat-Claude“ und ist seit dem 21.09.2026 gestrichen. Als Kandidat für Phase 5 hat es niemand genannt.
- **Stand am 25.09.2026 um 17:45 CEST:** kein Kandidat genannt, keine Wahl getroffen.
