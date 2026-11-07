# BIOTOP-LAGE-01 · Fassung 2 · `VERFASSUNGEN-TEIL3-01.md`

- **Inhalt:** FK22 · Entwurf B, Stück 3 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil B, Arbeitszeit 25.09.2026 16:10:47–17:42:51 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/verfassungen/VERFASSUNGEN-TEIL3.md` · 7861 B · SHA-256 `24361557faaaf33dc2b45a1d4f071ebe4f01d5b97d796154b72fd401d40b3eb8`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (0 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# VERFASSUNGEN — Teil 3 von 4 (FK22) · Entwurf

Fortsetzung von Teil 2. Stand des Lesens, Verfahren, Belegregel und Lesehilfe stehen in Teil 1; dieselben Regeln gelten hier.

---

## 9. Kasse: Verfassungszeilen je Zweig (R50)

| Zweig | Datei | Zeilen `verfassung_werk` von Werken in `werke` | Werke ohne Zeile | Protokollzeilen `verfassung.eingelegt` | letzte Einlegung (CEST) |
|---|---|---|---|---|---|
| STAMM | `/root/biotop/daten/biotop.db` | 18 von 22 | `werk_id` 1–4 | 18 | 20.09. 03:13:48 (`werk_id` 22) |
| VB1 | `/root/phase-4-vorbedingung-1/privat/biotop.db` | 19 von 23 | `werk_id` 1–4 | 19 | 20.09. 21:32:13 (`werk_id` 23 `lagerhaus-vorbedingung1-26`) |
| R02 | `/root/reparatur-02/privat-cli/privat.db` | 18 von 22 | `werk_id` 1–4 | 18 | 20.09. 03:13:48 (`werk_id` 22) |
| T3 | `/root/biotop-t3/t3.db` | 19 von 23 | `werk_id` 1–4 | 31 | 22.09. 15:43:15 (`werk_id` 23 `versandwerk-t3-02`) |

Zeiten: Die Kasse führt UTC; hier umgerechnet auf CEST (+2 h).

Hinweise:
- **Nur die letzte Einlegung je Werk bleibt.** `INSERT OR REPLACE` überschreibt frühere Einlegungen desselben Werks (`verfassung.py` Z. 28). Die Geschichte steht nur im Protokoll.
  - Das Protokoll führt `quelle`, `saetze`, `tausch`, `uebungswerk`, `von` und `werk_id`, aber weder Text noch Prüfsumme (Z. 30–31).
  - T3: 13 Einlegungen (gerechnet 31 − 18 = 13, 21.09. 05:44:40 bis 22.09. 15:43:15), erhalten ist nur die letzte.
  - Dass alle 13 denselben Text hatten, ist nur mittelbar belegt: Die Änderungszeiten der Dateien liegen vor der ersten Einlegung (R81), und alle 13 Protokollzeilen nennen dieselbe Quelle und dieselben Tauschwerte (R50). Siehe Lücke L6.
- **Das Feld `saetze` zählt Zeilen, nicht Sätze:** `text.count("\n") + 1` (Z. 30).
  - Werte: `lagerhaus` 8 und `logmuehle` 8 bei je 6 nummerierten Sätzen plus Kopfzeile; T3 Revision 02: 13 bei 8 nummerierten Sätzen.
  - Hermes schrieb am 19.09. 19:36:52 „8 Sätze“ (Teil 1 §4.5, Punkt 3). *Auslegung Hermes:* wohl aus diesem Feld übernommen; Kandidat für die Berichtigungen (FK13).
- **Zwei Schreibweisen der Quelle:** Bei `werk_id` 21 und 22 (STAMM, VB1, R02, T3) ist `quelle` relativ, `verfassungen/lagerhaus.md + verfassungen/lagerhaus.regeln.json`, sonst absolut.
- **Nummern mit verschiedener Bedeutung je Zweig** (R50):
  - `werk_id` 23 ist in VB1 `lagerhaus-vorbedingung1-26` (Lauf 26), in T3 `versandwerk-t3-02` (Läufe 26–38).
  - In R02 hängt Lauf 26 an `werk_id` 22 (`lagerhaus-c-25`).
  - Welche Verfassung für „Lauf 26“ galt, hängt also am Zweig: VB1 und R02 `lagerhaus`, T3 Revision 02. Die Zuordnungstafel steht in `INVENTAR`.

---

## 10. Widersprüche, Lücken, Fragen (Vorschläge für `LAGE` FK42/FK47 und die Lückenliste)

### Widersprüche (je mit beiden Belegen)
- **W1 `logmuehle` — Bestätigung vor der Bestätigung.**
  - Kasse STAMM `eingelegt_von`:
    - `werk_id` 15, 19.09. 13:55:53: „Hermes (Entwurf, Masterprompt v4 Phase 3; Chat-Claude bestätigt am Bericht)“;
    - `werk_id` 20, 19.09. 23:33:14: „Hermes (Entwurf, Chat-Claude bestaetigt am Bericht)“ (R50).
  - Dagegen Hermes am 19.09. 19:36:52 (id 2233): „… ich habe ihn nur verwiesen statt abgedruckt — damit konntest du ihn nicht bestätigen.“ Die Bestätigung kam erst mit Masterprompt v6 (20.09. 00:18:44) und der Nachricht vom 20.09. 00:55:54.
  - *Auslegung Hermes:* Das Feld beschreibt den vorgesehenen Weg aus Masterprompt v4, nicht einen erfolgten Schritt.
- **W2 `logmuehle` — Anhang B gegen die bestätigte Datei.** Anhang B (v6–v8) nennt als bestätigt die Datei mit Prüfsumme `0ce7f865…`. Diese Datei und das Zitat im Nachlaufbericht enthalten in Satz 1 „Es ist ein Übungswerk ohne Betriebszweck“, Anhang B schreibt „Übungswerk ohne Betriebszweck“ (R71). Welche Fassung gilt: Frage F3.
- **W3 T3 — wer bestätigt hat.**
  - Kasse T3 `eingelegt_von` „Philipp“ (13 von 13 Protokollzeilen) und Laufskripte `--von Philipp`.
  - Dagegen `ZWISCHENBERICHT` in `verfassung-entwurf-01`: „Philipp hat am 21.09.2026 entschieden: Chat-Claude bestätigt die Verfassung nach Abschnitt 3.3.“ Und Philipps Konto am 21.09. 05:38:33: „Chat-Claude hat sie geprüft“.
  - `BESTAETIGUNG.md`: „durch Philipp übermittelt“.
  - Frage F2.
- **W4 `lagerhaus` — „Gilt für Lauf 3“.**
  - Anhang A, Kopfzeile (v2–v8): „Gilt für Lauf 3 und alle weiteren Läufe am Übungswerk.“
  - Dagegen die Kasse STAMM (R50):
    - Lauf 3 trägt keine `werk_id`.
    - Die Läufe 4 und 5 liefen an Werken ohne Verfassungszeile (`werk_id` 3, 4); diese Werke wurden am 19.09. 00:04:53 und 00:11:48 aufgenommen.
    - Die erste Einlegung war am 19.09. 00:48:45 (`werk_id` 5).
  - *Auslegung Hermes:* Die Zeitfolge erklärt das. Masterprompt v2 kam am 19.09. um 00:36:30 in den Chat, nach der Aufnahme der Werke 3 und 4 (00:04:53 und 00:11:48). Die Beginnzeiten der Läufe 3–5 stehen in `CHRONIK`.
- **W5 Satzzahl.** Hermes meldete am 19.09. 19:36:52 für `logmuehle.md` „8 Sätze“; die Datei hat 6 nummerierte Sätze plus Kopfzeile (Teil 1 §4.2). *Auslegung Hermes:* Die 8 stammt vermutlich aus dem Kassenfeld `saetze`, das Zeilen zählt (§9). Nicht belegt.

### Lücken (Vorschlag für die Lückenliste; Kennung vergibt Hermes)
- **L1 Delegation für Übungswerke.** Belegt ist sie nur im Masterprompt (v2–v8, 3.3). Eine Nachricht Philipps, die sie erteilt, liegt in keiner Quelle ab dem 18.09. vor. Schließen durch: Philipp.
- **L2 Quelle „Philipp hat am 21.09.2026 entschieden: Chat-Claude bestätigt die Verfassung“** (Teil 2 §5.5, Punkt 2): NICHT GEFUNDEN. Schließen durch: Hermes mit einer gezielten Suche in der Sitzungsdatenbank über die geschwärzten Wege (R12/R14/R19/R22) oder Philipp.
- **L3 Regeldateien ohne Bestätigung** (`lagerhaus`, `logmuehle`, T3). Sie enthalten Werte, die im Text nicht stehen. Beispiele: `sonst_faktor` 1.25; Einstiege; `rundung`; `verbundausfall`; `tragender_pfad`; die Musterliste `"skips ="` und `"[bandit]"`. Schließen durch: Chat-Claude oder Philipp (Frage F4).
- **L4 T3-Regeldatei nicht im Siegelordner** `verfassung-02`; geändert nach der Versiegelung (Teil 2 §5.3). Schließen durch: Chat-Claude (Prüfung der Regeln gegen Revision 02).
- **L5 Die ältere `drahtwerk`-Variante und 17 weitere `drahtwerk`-Kopien liegen als Datei nur in `/tmp`** (gerechnet: 8 Text- und 9 Regelkopien). Das Verzeichnis ist flüchtig und nicht im Sicherungsumfang nach Abschnitt 4. Die Kopien sind gleich mit Teil 2 §6.2 und §6.3 (R81; Liste in Teil 4 §11). Schließen durch: Hermes, Entscheidung, ob `/tmp` mitgesichert wird.
- **L6 Frühere Einlegungen nicht byteweise belegt.** Die Kasse hält nur die letzte je Werk, das Protokoll keine Prüfsumme (§9). Schließen: nicht mehr möglich. Mittelbarer Beleg über Änderungszeiten und Quelle.

### Fragen (Vorschlag für FK47)
- **F1 an Philipp:** Wer schreibt und wer bestätigt die Verfassungen der Testwerke T4–T6? Masterprompt 3.3 regelt Übungswerke („schreibt Chat-Claude“, Delegation) und Werke allgemein („Philipp … bestätigt“), Phase 5 das echte Werk („schreibt Philipp“); Phase 4 schweigt. T3 schrieb Hermes. Philipps Konto am 21.09. 02:14:40 (id 9106) sagt nur zum Bau: „Stattdessen Breitentest an mehreren Testwerken, die du selbst baust (Entscheidung Philipps)“.
- **F2 an Philipp:** Ist die T3-Bestätigung vom 21.09. als Ihre oder als Chat-Claudes zu führen (W3)?
- **F3 an Chat-Claude:** Gilt Anhang B im Wortlaut der bestätigten Datei `0ce7f865…` (mit „Es ist ein“) oder im Wortlaut des Masterprompts (W2)?
- **F4 an Chat-Claude:** Sollen die maschinenlesbaren Regeln eigens bestätigt werden (L3, L4)?
- **F5 an Chat-Claude:** Soll die T3-Verfassung wie `lagerhaus` (A) und `logmuehle` (B) als Anhang in den Masterprompt? Masterprompt v8 vom 23.09. hat nur die Anhänge A und B (Teil 1 §3.4, §4.4).
