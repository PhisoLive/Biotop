# BIOTOP-LAGE-01 · Fassung 2 · `INVENTAR-TEIL1-01.md`

- **Inhalt:** Abschnitt 5 · Entwurf I, Stück 1 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Skript `entwurf/inventar/inventar.py` (Subagent Teil I), ausgeführt von Hermes zum Stichzeitpunkt (R191). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/inventar/lauf-stich-v3/INVENTAR-TEIL1.md` · 22164 B · SHA-256 `4588edd92f4aabab3343320208a00c789cfbc78f4db49df7d5db5f734e7dcff4`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (63 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Dieser Lauf zählt nach dem Verzeichnis v3 (Grenze < 17:30:00) und nimmt nur Zeilen bis 17:29:59,000 auf. Deshalb bleibt eine Zeile draußen: der Schlussbericht von S1c (id 25141, 17:29:59 und Bruchteile). Die Zeile id 7468 ohne Text ist dagegen mitgezählt. **I2 = 1.455 Zeilen** heißt also: 1.456 Zeilen von v3 minus id 25141. **START-02 Abschnitt C** nennt ebenfalls 1.455, aber für „Nachrichten mit Text“: 1.456 minus id 7468. Die Zahl ist gleich, die Mengen unterscheiden sich um genau diese zwei Zeilen (R197, R198). Gleiches gilt für die Biotop-Zeilen: 1.440 hier gegenüber 1.440 in START-02 C, bei 1.441 Biotop-Zeilen in v3. Philipp hat hier 115 Zeilen, davon 44 ab 21.09.; mit Text sind es 114, davon 44 ab 21.09. Endstand der Runde 6 zum Stich: LAGE-TEIL1-01.md.

---
> INVENTAR Teil 1 von 3 (INVENTAR-TEIL1.md … INVENTAR-TEIL3.md)

# INVENTAR — Bestandsaufnahme und Abgleich (BIOTOP-LAGE-01 Fassung 2, Abschnitt 5)

Entwurf Teil I. Erzeugt von `/root/sicherung/biotop-lage-01/entwurf/inventar/inventar.py` (SHA-256 `9f893d92e15ada5c959feb273020ce29b626cb5ccab586112b44c5d7325df02b`), Aufruf `python3 /root/sicherung/biotop-lage-01/entwurf/inventar/inventar.py --stich 2026-09-25T17:29:59+02:00 --aus /root/sicherung/biotop-lage-01/entwurf/inventar/lauf-stich-v3 --verlauf v3 --git-status /root/sicherung/biotop-lage-01/tmp/git-status-stich.txt --auftrag-beginn 2026-09-25T14:44:20+02:00`.
Lesebeginn 2026-09-25 19:45:06 CEST · Stichzeitpunkt 2026-09-25 17:29:59 CEST · alle Zeiten CEST (UTC+2), Rohzeiten der Kasse in UTC. Jede Zahl ist *abgelesen* (Quelle genannt) oder *gerechnet* (Rechenweg genannt). Adressen im Prüfkanal: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/<ordner>/`. Kosten je Lauf stehen nur in `KASSE`, Budgets in `CHRONIK` (FK20), Umfang je Werk in `LAGE` (FK25), Torzeilen in `TORE`, Fassungen in `ENTSCHEIDUNGEN` (FK15).


## 1. Quellen und Quellenabdeckung

Lesezeitpunkte: verlauf 2026-09-25 19:45:06, git 2026-09-25 19:45:06, kasse 2026-09-25 19:45:07, pruefkanal 2026-09-25 19:45:12, i4 2026-09-25 19:45:17, dateien 2026-09-25 19:45:18, weitere_kassen 2026-09-25 19:45:22. *abgelesen* (Uhr des Servers)

| Quelle | abgedeckter Zeitraum | Umfang | Einschränkung |
|---|---|---|---|
| Nachrichtenverzeichnis (Sitzungsdatenbank, Auszug `arbeit/verlauf/v3/nachrichten.jsonl`) | 2026-09-18 20:59:08 bis 2026-09-25 18:14:01 (Erzeugung der Datei) | 1456 Nachrichten user/assistant mit Text, Dubletten zusammengefasst; ab 18.09. 00:00 | Werkzeugausgaben nicht einzeln; Auszug endet mit seiner Erzeugung |
| Kasse STAMM `/root/biotop/daten/biotop.db` (mode=ro&immutable=1, -wal vorher 0 / nachher 0 Bytes) | Buchungen 2026-09-18 23:40:44 bis 2026-09-20 03:43:33; Protokoll 2026-09-18 23:40:42 bis 2026-09-20 04:04:59 | 25 Läufe, 4070 Buchungen, 16030 Protokollzeilen | Datei zuletzt geändert 2026-09-20 04:05:13 |
| Kasse VB1 `/root/phase-4-vorbedingung-1/privat/biotop.db` (Kopie von Datei und -wal (4140632 Bytes) unter tmp/, Original unberührt, -wal vorher 4140632 / nachher 4140632 Bytes) | Buchungen 2026-09-18 23:40:44 bis 2026-09-20 22:16:10; Protokoll 2026-09-18 23:40:42 bis 2026-09-20 22:16:10 | 26 Läufe, 4316 Buchungen, 17051 Protokollzeilen | Datei zuletzt geändert 2026-09-20 22:08:28 |
| Kasse R02 `/root/reparatur-02/privat-cli/privat.db` (mode=ro&immutable=1, -wal vorher 0 / nachher 0 Bytes) | Buchungen 2026-09-18 23:40:44 bis 2026-09-20 03:43:33; Protokoll 2026-09-18 23:40:42 bis 2026-09-20 20:44:07 | 26 Läufe, 4070 Buchungen, 16034 Protokollzeilen | Datei zuletzt geändert 2026-09-20 20:44:08 |
| Kasse T3 `/root/biotop-t3/t3.db` (Kopie von Datei und -wal (13221112 Bytes) unter tmp/, Original unberührt, -wal vorher 13221112 / nachher 13221112 Bytes) | Buchungen 2026-09-18 23:40:44 bis 2026-09-22 21:26:08; Protokoll 2026-09-18 23:40:42 bis 2026-09-22 21:26:11 | 38 Läufe, 6673 Buchungen, 26448 Protokollzeilen | Datei zuletzt geändert 2026-09-22 21:16:34 |
| git `/root/biotop` (alle Zweige) | 2026-09-19 00:19:32 bis 2026-09-25 19:45:06 (Lesen) | 75 Commits seit 18.09. | nur Eingechecktes; Arbeitsstand über --git-status |
| Prüfkanal `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-*`, `gedaechtnis` | 2026-09-18 23:18:12 bis 2026-09-25 19:32:02 (Datei-mtime) | 20 Ordner | mtime zeigt nur die letzte Änderung einer Datei |
| Dateisystem `/root/biotop` (mtime) | ab 21.09. bis 2026-09-25 19:45:18 | 202 Dateien geändert | frühere Änderungen derselben Datei unsichtbar |
| OpenRouter-Nutzungsanzeige (`arbeit/OR-STAND.jsonl`, Abfragen durch Hermes) | 2026-09-25 14:54:17, 2026-09-25 18:04:50 | 2 Abfragen | nur Summen je UTC-Tag/-Woche/-Monat zum Abfragezeitpunkt |
| Weitere Kassen-Datenbanken unter `/root` (Suche `*.db`, Tiefe ≤ 5) | Lesen 2026-09-25 19:45:22 | 407 Dateien mit Tabelle kasse, davon 22 mit Zeilen; Zeilen in keinem der vier Zweige: 0 (0.0000 €) | nicht geöffnet 0 (Baum /root/biotop mit -wal > 0), Lesefehler 0; ohne .hermes, sicherung, node_modules, .git, venv — Liste `LISTEN`, Abschnitt 7 |
| Chronik (Teil F) | CHRONIK-TEIL1.md, CHRONIK-TEIL2.md, CHRONIK-TEIL3.md | 136 Zeilen C… |  |

**Telegram-Kette (Biotop ja):** 10 Sitzungen mit Nachrichten, also 9 Sitzungswechsel (Zurücksetzung oder Umschaltung) — *abgelesen* aus dem Verzeichnis; Endgrund aus R12 (Stand 25.09. 15:12), soweit dort geführt.

| Sitzung | erste Nachricht | letzte Nachricht | Nachrichten | davon Philipp | erster Absender | Endgrund (R12) |
|---|---|---|---|---|---|---|
| 20260918_205818_3767d1c9 | 2026-09-18 20:59:08 | 2026-09-18 21:08:09 | 2 | 1 | Philipp | session_reset |
| 20260918_223638_04e4469a | 2026-09-18 22:43:27 | 2026-09-18 22:59:08 | 4 | 2 | Philipp | session_reset |
| 20260918_225920_3e614670 | 2026-09-18 22:59:45 | 2026-09-20 04:50:18 | 489 | 44 | Philipp | session_reset |
| 20260920_045023_5299d50d | 2026-09-20 04:54:01 | 2026-09-20 05:18:37 | 7 | 5 | Philipp | session_reset |
| 20260920_052507_2f047335 | 2026-09-20 05:25:16 | 2026-09-20 06:10:44 | 10 | 6 | Philipp | session_reset |
| 20260920_063003_896e94ff | 2026-09-20 06:40:15 | 2026-09-21 01:54:14 | 102 | 16 | Philipp | session_reset |
| 20260921_015554_e79a4a0f | 2026-09-21 01:56:17 | 2026-09-23 19:30:51 | 353 | 27 | Philipp | session_reset |
| 20260923_194003_92313ee1 | 2026-09-23 19:42:19 | 2026-09-24 16:10:36 | 57 | 6 | Philipp | session_switch |
| 20260924_150913_a9326d | 2026-09-24 15:09:13 | 2026-09-24 21:51:18 | 37 | 2 | Hermes→Subagent | session_switch |
| 20260924_203120_e6c401 | 2026-09-24 20:31:20 | 2026-09-25 17:20:52 | 39 | 6 | Hermes→Subagent | — |

Hinweis: 2 Sitzungen der Kette beginnen mit einem Auftrag Hermes→Subagent (Berichtigung Hermes: Reviewaufträge an Review-Subagenten) und führen danach Nachrichten Philipps (Spalte „davon Philipp“) — sie gehören zur Kette (*abgelesen*).

**Verdichtungen:** 21 Verdichtungsmeldungen in 5 Sitzungen (*abgelesen*, Absender System-Verdichtung). R14: active 0 compacted 0: 4199; active 0 compacted 1: 6811; active 1 compacted 0: 10197; active 0 compacted 0: 1519; active 0 compacted 1: 567; active 1 compacted 0: 761 — verdichtete Nachrichten bleiben als Zeilen erhalten (R14), das Verzeichnis führt sie.

**Längste Pausen zwischen zwei Biotop-Nachrichten** (*gerechnet*): 2026-09-22 21:29:37 – 2026-09-23 05:41:59 (8.2 h); 2026-09-22 06:57:19 – 2026-09-22 14:52:53 (7.9 h); 2026-09-20 07:52:50 – 2026-09-20 15:28:25 (7.6 h); 2026-09-19 05:37:13 – 2026-09-19 12:39:25 (7.0 h); 2026-09-22 00:21:20 – 2026-09-22 06:29:08 (6.1 h). Eine Pause ist keine Lücke der Quelle: Die Sitzungsdatenbank führt jede Nachricht; in einer Pause wurde nichts geschrieben.

**Spannen 18.09. 00:00 bis Stich ohne Quelle:** keine — die Sitzungsdatenbank führt Nachrichten ab 14.09. lückenlos (R12), Kasse und git sind bis zum Lesezeitpunkt gelesen. *gerechnet* (Vereinigung der Zeiträume oben)
- Nachrichten nach dem Stich im Verzeichnis: 1 (nicht gezählt).

## 2. I1 Läufe

Quellen: Tabellen `laeufe`, `kasse`, `werke`, `protokoll` (art `lauf.%`) der Zweige STAMM, VB1, R02, T3; Abfragen: `SELECT id, werk_id, budget_eur, status, begonnen_am, beendet_am, grund, mass, richtung, freigabe FROM laeufe`, `SELECT * FROM kasse`, `SELECT nr, zeit, art, json_extract(inhalt,'$.lauf_id') … FROM protokoll WHERE art LIKE 'lauf.%'`. Zeitpunkt 2026-09-25 19:45:07.
**Entdoppelung (Regel, Auslegung Hermes):** Ein Lauf ist das Paar (Laufnummer, begonnen_am); dieselbe Nummer mit anderem Beginn ist ein anderer Lauf (Kennung `<Zweig des ersten Vorkommens>/<Nummer>`). Eine Kassenzeile zählt einmal, wenn sie in mehreren Zweigen mit allen Spalten gleich ist. Beleg der Regel: gleiche id, anderer Inhalt — STAMM↔VB1: 0 von 4070 gemeinsamen ids; STAMM↔R02: 0 von 4070 gemeinsamen ids; STAMM↔T3: 0 von 4070 gemeinsamen ids; VB1↔R02: 0 von 4070 gemeinsamen ids; VB1↔T3: 246 von 4316 gemeinsamen ids; R02↔T3: 0 von 4070 gemeinsamen ids (*gerechnet*); eine Entdoppelung nur nach id wäre also falsch. Kassenzeilen, die zu verschiedenen Läufen gehören würden: 0.
**Anzahl:** 40 Läufe (*gerechnet*, Paare), Laufnummern 1–38; Kasse 6919 verschiedene Buchungen aus 19129 Zeilen der vier Zweige (*gerechnet*). Aufrufe = Buchungen des Laufs; Kosten je Lauf → `KASSE-TEIL1.csv`. Ergebnisort und Zuordnungsart aus Abgleich 1.

| Zweig | Läufe | Buchungen | davon auch in anderen Zweigen | nur in diesem Zweig | Summe kosten_eur (Zweig) |
|---|---|---|---|---|---|
| STAMM | 25 | 4070 | 4070 | 0 | 8.6393 |
| VB1 | 26 | 4316 | 4070 | 246 | 9.0861 |
| R02 | 26 | 4070 | 4070 | 0 | 8.6393 |
| T3 | 38 | 6673 | 4070 | 2603 | 18.3679 |

*abgelesen* (Zweig), *gerechnet* (Entdoppelung). Die Summe der Kasse ohne Doppelzählung steht in I8.

| Lauf | Zweige | Beginn | Ende | Status | Werk | Aufrufe | Protokoll | Ergebnisort | Zuordnung |
|---|---|---|---|---|---|---|---|---|---|
| STAMM/1 | SVRT | 18.09. 23:40 | 18.09. 23:44 | abgebrochen | lagerhaus | 27 | abgebrochen,angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/ | Nennung + Zeitfenster |
| STAMM/2 | SVRT | 18.09. 23:44 | — | bereit | lagerhaus | 100 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/ | Nennung + Zeitfenster |
| STAMM/3 | SVRT | 19.09. 00:04 | 19.09. 00:04 | gestoppt |  | 1 | angelegt,gestoppt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/ | Nennung + Zeitfenster |
| STAMM/4 | SVRT | 19.09. 00:04 | — | abgebrochen | lagerhaus-kasse | 62 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/ | Nennung + Zeitfenster |
| STAMM/5 | SVRT | 19.09. 00:11 | 19.09. 00:16 | abgebrochen | lagerhaus-kasse2 | 46 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/ | Nennung + Zeitfenster |
| STAMM/6 | SVRT | 19.09. 00:48 | 19.09. 01:19 | abgebrochen | lagerhaus-nachlauf | 178 | abgebrochen,angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/ | Nennung + Zeitfenster |
| STAMM/7 | SVRT | 19.09. 01:20 | 19.09. 01:32 | abgebrochen | lagerhaus-nachlauf2 | 88 | abgebrochen,angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/ | Nennung + Zeitfenster |
| STAMM/8 | SVRT | 19.09. 01:33 | 19.09. 01:53 | abgebrochen | lagerhaus-nachlauf8 | 136 | abgebrochen,angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/ | Nennung + Zeitfenster |
| STAMM/9 | SVRT | 19.09. 01:53 | 19.09. 02:08 | beendet | lagerhaus-nachlauf9 | 108 | angelegt,beendet | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/ | Nennung + Zeitfenster |
| STAMM/10 | SVRT | 19.09. 02:09 | 19.09. 02:12 | abgebrochen | lagerhaus-kasse3 | 32 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/ | Nennung + Zeitfenster |
| STAMM/11 | SVRT | 19.09. 02:28 | — | angelegt |  | 6 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/ | Nennung + Zeitfenster |
| STAMM/12 | SVRT | 19.09. 02:41 | 19.09. 03:46 | abgebrochen | lagerhaus-p2 | 480 | abgebrochen,angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/ | Nennung + Zeitfenster |
| STAMM/13 | SVRT | 19.09. 03:47 | 19.09. 05:25 | beendet | lagerhaus-p2-13 | 713 | angelegt,beendet | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/ | Nennung + Zeitfenster |
| STAMM/14 | SVRT | 19.09. 13:03 | — | verworfen | lagerhaus-p3-14 | 17 | angelegt,verworfen | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/ | Nennung + Zeitfenster |
| STAMM/15 | SVRT | 19.09. 13:09 | — | verworfen | lagerhaus-p3-15 | 28 | angelegt,verworfen | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/ | Nennung + Zeitfenster |
| STAMM/16 | SVRT | 19.09. 13:26 | 19.09. 16:40 | verworfen | lagerhaus-p3-16 | 264 | angelegt,verworfen | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/ | Nennung + Zeitfenster |
| STAMM/17 | SVRT | 19.09. 13:55 | 19.09. 15:54 | gesaettigt | logmuehle-17 | 315 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/ | Nennung + Zeitfenster |
| STAMM/18 | SVRT | 19.09. 16:41 | 19.09. 17:05 | verworfen | lagerhaus-p3-18 | 156 | angelegt,verworfen | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/ | Nennung + Zeitfenster |
| STAMM/19 | SVRT | 19.09. 17:06 | 19.09. 17:39 | verworfen | lagerhaus-p3-19 | 221 | angelegt,verworfen | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/ | Nennung + Zeitfenster |
| STAMM/20 | SVRT | 19.09. 17:40 | 19.09. 18:23 | gesaettigt | lagerhaus-p3-20 | 244 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/ | Nennung + Zeitfenster |
| STAMM/21 | SVRT | 19.09. 22:34 | 19.09. 22:34 | verworfen | lagerhaus-p3-20 | 0 | — | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/ | Nennung + Zeitfenster |
| STAMM/22 | SVRT | 19.09. 22:57 | 20.09. 00:50 | gesaettigt | lagerhaus-p3-22 | 233 | abgebrochen,angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/ | Nennung + Zeitfenster |
| STAMM/23 | SVRT | 19.09. 23:32 | 20.09. 00:39 | gesaettigt | logmuehle-23 | 239 | abgebrochen,angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/ | Nennung + Zeitfenster |
| STAMM/24 | SVRT | 20.09. 00:57 | — | bereit | lagerhaus-zeile8-24 | 193 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/ | Nennung + Zeitfenster |
| STAMM/25 | SVRT | 20.09. 03:13 | — | bereit | lagerhaus-c-25 | 183 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/ | Nennung + Zeitfenster |
| R02/26 | R | 20.09. 20:42 | — | kartiert | lagerhaus-c-25 | 0 | — | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/ | Zweig-Arbeitsordner |
| VB1/26 | V | 20.09. 21:31 | 20.09. 22:16 | gesaettigt | lagerhaus-vorbedingung1-26 | 246 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/ | Zweig-Arbeitsordner + Nennung |
| T3/26 | T | 21.09. 05:43 | — | kartiert | versandwerk-t3-02 | 31 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/27 | T | 21.09. 05:48 | — | kartiert | versandwerk-t3-02 | 1 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/28 | T | 21.09. 06:05 | — | kartiert | versandwerk-t3-02 | 1 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/29 | T | 21.09. 06:35 | — | kartiert | versandwerk-t3-02 | 4 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/30 | T | 21.09. 07:34 | — | kartiert | versandwerk-t3-02 | 4 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/31 | T | 21.09. 13:11 | — | laeuft | versandwerk-t3-02 | 107 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/32 | T | 21.09. 15:19 | — | laeuft | versandwerk-t3-02 | 246 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/33 | T | 21.09. 18:23 | — | kartiert | versandwerk-t3-02 | 1 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/34 | T | 21.09. 18:45 | — | kartiert | versandwerk-t3-02 | 1 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/35 | T | 21.09. 19:15 | — | kartiert | versandwerk-t3-02 | 3 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/36 | T | 21.09. 20:25 | — | laeuft | versandwerk-t3-02 | 326 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/37 | T | 22.09. 00:21 | 22.09. 06:29 | gesaettigt | versandwerk-t3-02 | 895 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |
| T3/38 | T | 22.09. 15:42 | — | bereit | versandwerk-t3-02 | 983 | angelegt | https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | Zweig-Arbeitsordner + Nennung |

Zweige: S = STAMM, V = VB1, R = R02, T = T3. „Protokoll“: Ereignisse `lauf.*` des Laufs (entdoppelt).
- Läufe mit abweichenden Feldern zwischen Zweigen: 0.
- Läufe ohne Ende mit Status laeuft/bereit/kartiert/angelegt: 17 von 40: STAMM/2 (bereit, letzte Buchung 19.09. 00:02), STAMM/11 (angelegt, letzte Buchung 19.09. 02:28), STAMM/24 (bereit, letzte Buchung 20.09. 01:25), STAMM/25 (bereit, letzte Buchung 20.09. 03:43), R02/26 (kartiert, letzte Buchung —), T3/26 (kartiert, letzte Buchung 21.09. 05:46), T3/27 (kartiert, letzte Buchung 21.09. 05:48), T3/28 (kartiert, letzte Buchung 21.09. 06:05), T3/29 (kartiert, letzte Buchung 21.09. 07:29), T3/30 (kartiert, letzte Buchung 21.09. 12:09), T3/31 (laeuft, letzte Buchung 21.09. 15:09), T3/32 (laeuft, letzte Buchung 21.09. 18:16), T3/33 (kartiert, letzte Buchung 21.09. 18:23), T3/34 (kartiert, letzte Buchung 21.09. 18:46), T3/35 (kartiert, letzte Buchung 21.09. 20:07), T3/36 (laeuft, letzte Buchung 22.09. 00:12), T3/38 (bereit, letzte Buchung 22.09. 21:26) (*abgelesen*).

## 3. I2 Aufträge und Meldungen

Quelle: `/root/sicherung/biotop-lage-01/arbeit/verlauf/v3/nachrichten.jsonl` (ohne Inhalt) und `wortlaut.jsonl` (geschwärzt, nur zur Einordnung gelesen), erzeugt 2026-09-25 18:14:01; Einordnung Absender und Biotop ja/nein durch `arbeit/verlauf_extrakt.py` (Auslegung Hermes, steht dort). Zeitpunkt 2026-09-25 19:45:06.
**Anzahl:** 1455 Nachrichten bis zum Stich, davon Biotop ja 1440, nein 15 (*abgelesen*). Beginn BIOTOP-LAGE-01 (erste Nachricht mit der Kennung): 2026-09-25 14:44:20.

Auslegung Hermes (mechanische Regel für „Art“): System-* und Subagent-Schlussberichte = Meldung; Hermes-/Subagent-Zwischentexte = Zwischentext (nur gezählt); Hermes→Subagent = Auftrag; Hermes an Philipp = Frage, wenn die letzte nicht leere Zeile mit „?“ endet, sonst Meldung; Philipp = Auftrag, wenn die Nachricht ein Dokument trägt („[The user sent a … document“ / „[Content of …]“) oder ohne vorangestellte Herkunftsdaten („Gateway message origin …“) und ohne Antwortzitat („[Replying to: …]“) mindestens 1.500 Bytes lang ist, sonst Frage (letzte Zeile endet mit „?“) oder Anweisung; CLI-Probe = Anweisung.

| Absender (Biotop ja) | Auftrag | Anweisung | Frage | Meldung | Zwischentext | Summe |
|---|---|---|---|---|---|---|
| Hermes | 0 | 0 | 8 | 209 | 0 | 217 |
| Hermes-Zwischentext | 0 | 0 | 0 | 0 | 643 | 643 |
| Hermes→Subagent | 131 | 0 | 0 | 0 | 0 | 131 |
| Philipp | 37 | 77 | 1 | 0 | 0 | 115 |
| Subagent | 0 | 0 | 0 | 53 | 0 | 53 |
| Subagent-Zwischentext | 0 | 0 | 0 | 0 | 158 | 158 |
| System-Delegationsergebnis | 0 | 0 | 0 | 26 | 0 | 26 |
| System-Hintergrundprozess | 0 | 0 | 0 | 50 | 0 | 50 |
| System-Hinweis | 0 | 0 | 0 | 26 | 0 | 26 |
| System-Verdichtung | 0 | 0 | 0 | 21 | 0 | 21 |

*gerechnet*: Zählung über das Verzeichnis. Die vollständige Liste (Zeit, Absender, Art, Sitzung, Biotop ja/nein, ohne Inhalt) steht in `LISTEN`, Abschnitt 3.

**Auftragsdateien auf der Platte:** 88 Fundorte, 52 verschiedene Inhalte (SHA-256) — Liste in I4. *gerechnet*

## 4. I3 Abschlussordner

Quelle: Prüfkanal `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/` (Verzeichnis gelesen mit os.walk), Zeitpunkt 2026-09-25 19:45:12. **Anzahl:** 20 Ordner (`biotop-*` und `gedaechtnis`); weitere Ordner anderer Vorhaben unter `laeufe/`: 90 (nur gezählt). *abgelesen*
Entstehung = älteste, letzte Änderung = jüngste Datei-mtime. „Läufe genannt“: Laufnummern, die in *.md/*.txt des Ordners oder in Dateipfaden stehen (Muster „Lauf n“, „Läufe n–m“, „lauf38“).

| Ordner | Dateien | Entstehung | letzte Änderung | Einstieg | zugehörig (Abgleich 1) |
|---|---|---|---|---|---|
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/ | 86 | 20.09. 06:42 | 20.09. 07:52 | BERICHT.md, ZWISCHENBERICHT.md | Nennung Nachricht 3429 (20.09. 06:40) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ | 174 | 25.09. 15:09 | 25.09. 19:32 | START-01.md, START-02.md, zwischenbericht-20260925-163807-r114/UEBERGABE-1-UEBERGABE.md … | Nennung Nachricht 20987 (25.09. 14:44) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/ | 49 | 18.09. 23:18 | 19.09. 00:22 | BERICHT.md | Läufe STAMM/1, STAMM/2, STAMM/3, STAMM/4, STAMM/5 |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/ | 135 | 19.09. 00:38 | 19.09. 02:16 | BERICHT.md | Läufe STAMM/6, STAMM/7, STAMM/8, STAMM/9, STAMM/10 |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/ | 124 | 19.09. 02:28 | 19.09. 05:36 | BERICHT.md | Läufe STAMM/11, STAMM/12, STAMM/13 |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/ | 200 | 19.09. 13:01 | 19.09. 18:31 | BERICHT.md | Läufe STAMM/14, STAMM/15, STAMM/16, STAMM/17, STAMM/18, STAMM/19, STAMM/20 |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/ | 54 | 19.09. 20:30 | 19.09. 23:59 | BERICHT.md | Läufe STAMM/21, STAMM/22, STAMM/23 |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-einstieg-20260921-01/ | 16 | 21.09. 01:51 | 21.09. 01:51 | ZWISCHENBERICHT.md | Nennung Nachricht 9071 (21.09. 01:54) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/ | 146 | 20.09. 00:20 | 21.09. 00:10 | BERICHT.md, NACHGANG-03.md, NACHGANG-04.md … | Läufe STAMM/24, STAMM/25, VB1/26 |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ | 9489 | 20.09. 15:31 | 20.09. 20:01 | ZWISCHENBERICHT-02.md, ZWISCHENBERICHT.md, auftragseingrenzung-01/ZWISCHENBERICHT.md … | Nennung Nachricht 4317 (20.09. 15:28) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/ | 21 | 20.09. 20:55 | 20.09. 20:55 | ZWISCHENBERICHT.md | Läufe R02/26 |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ | 231 | 21.09. 02:24 | 23.09. 15:47 | BERICHT.md, ZWISCHENBERICHT.md, abschluss-01/ABSCHLUSSBERICHT.md … | Läufe T3/26, T3/27, T3/28, T3/29, T3/30, T3/31, T3/32, T3/33, T3/34, T3/35, T3/36, T3/37, T3/38 |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/ | 98 | 23.09. 22:00 | 23.09. 22:27 | BERICHT.md, UEBERGABE.md, zwischenbericht-20260923-220002-r110/UEBERGABE-1-UEBERGABE.md … | Nennung Nachricht 14000 (23.09. 15:53) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-02/ | 79 | 23.09. 22:54 | 24.09. 02:10 | BERICHT.md, UEBERGABE.md, zwischenbericht-20260923-225416-r13-verdichtung/UEBERGABE-1-UEBERGABE.md … | Nennung Nachricht 14624 (23.09. 22:32) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-03/ | 100 | 24.09. 05:11 | 24.09. 11:56 | BERICHT.md, UEBERGABE.md, zwischenbericht-20260924-051104-r113/UEBERGABE-1-UEBERGABE.md … | Nennung Nachricht 15154 (24.09. 02:14) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-04/ | 123 | 24.09. 14:17 | 24.09. 17:19 | BERICHT.md, UEBERGABE.md, zwischenbericht-20260924-141737-r103-kontext80/UEBERGABE-1-UEBERGABE.md … | Nennung Nachricht 15992 (24.09. 11:49) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-05/ | 159 | 24.09. 20:33 | 24.09. 23:45 | BERICHT-vor-fuellen.md, BERICHT-vor-review.md, BERICHT.md … | Nennung Nachricht 16482 (24.09. 16:48) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-06/ | 20 | 25.09. 00:06 | 25.09. 01:12 | zwischenbericht-20260925-000624-r29-verdichtung/UEBERGABE-1-UEBERGABE.md, zwischenbericht-20260925-000624-r29-verdichtung/ZWISCHENBERICHT.md, zwischenbericht-20260925-002824-r0-verdichtung/UEBERGABE-1-UEBERGABE.md … | Nennung Nachricht 16901 (24.09. 23:15) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/ | 35 | 20.09. 05:01 | 20.09. 05:17 | ZWISCHENBERICHT.md | Nennung Nachricht 3215 (20.09. 05:18) |
| https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/ | 5 | 20.09. 05:17 | 20.09. 05:17 |  | Nennung Nachricht 3148 (20.09. 05:01) |
