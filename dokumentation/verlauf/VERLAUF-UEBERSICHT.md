# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop seit dem 18.09.2026 · Übersicht

- **Quelle:** `/root/.hermes/state.db`, nur lesend (`mode=ro`), Tabellen `sessions` und `messages`.
- **Zeitraum:** 18.09.2026 00:00:00 CEST bis 26.09.2026 01:10:52 CEST (Zeitpunkt des Auszugs).
- **Biotop-Sitzungen:** die Kette ab `20260918_205818_3767d1c9` (Masterprompt v1) über `parent_session_id`: 60 Sitzungen. Andere Sitzungen gehören zu anderen Vorhaben und bleiben draußen.
- **Aufgenommen (Auslegung Hermes, wie BIOTOP-LAGE-01 FK48 Nr. 3):** Nachrichten Philipps (auch Texte in Chat-Claudes Stimme aus Philipps Konto und eingelegte Dokumente), Antworten von Hermes und Zwischentexte von Hermes (Text neben einem Werkzeugaufruf). Die Zuordnung „Philipp/System“ folgt dem Nachrichtenanfang (Systemkennungen wie `[CONTEXT COMPACTION`, `[ASYNC DELEGATION`, `[STILL IN PROGRESS`).
- **Schwärzung:** jedes Schlüsselmuster und jeder Wert aus `.env` (≥ 8 Zeichen) und `auth.json` (≥ 12 Zeichen) (Werkzeug `geheimnis.py` aus BIOTOP-LAGE-01), ersetzt durch `[GESCHWÄRZT: …]`.
- **Doppelzeilen:** Nach Verdichtungen steht dieselbe Nachricht mehrfach in der Datenbank; zusammengefasst nach (Sitzung, Rolle, Zeitstempel, Inhalt).

## Zählung (abgelesen aus dem Auszug)

- Aufgenommen: **1016** Nachrichten = Hermes 245 + Hermes-Zwischentext 652 + Philipp 119.
- Geschwärzt: 27 Stellen in 14 Nachrichten.
- Nicht aufgenommen (Nachrichten ohne Doppelzeilen): Hermes→Subagent: 133; Subagent: 63; Subagent-Zwischentext: 159; System-Delegationsergebnis: 29; System-Hintergrundprozess: 51; System-Hinweis: 27; System-Verdichtung: 24; andere Sitzungen (nicht Biotop): 15; reiner Werkzeugaufruf ohne Text: 7725.
- Werkzeugausgaben (Rolle `tool`) im Zeitraum, alle Sitzungen: 15956 Zeilen, nicht aufgenommen.

## Je Tag

| Tag | Philipp | Hermes | Hermes-Zwischentext |
|---|---|---|---|
| 18.09. | 5 | 5 | 12 |
| 19.09. | 26 | 36 | 273 |
| 20.09. | 40 | 57 | 95 |
| 21.09. | 22 | 49 | 112 |
| 22.09. | 3 | 8 | 50 |
| 23.09. | 8 | 19 | 60 |
| 24.09. | 6 | 26 | 37 |
| 25.09. | 9 | 43 | 13 |
| 26.09. | 0 | 2 | 0 |

## Teile

| Datei | Einträge | Bytes |
|---|---|---|
| VERLAUF-TEIL-001.md | V0001–V0006 | 30320 |
| VERLAUF-TEIL-002.md | V0007–V0028 | 37193 |
| VERLAUF-TEIL-003.md | V0029–V0029 | 2398 |
| VERLAUF-TEIL-004.md | V0030–V0030 | 36811 |
| VERLAUF-TEIL-005.md | V0030–V0053 | 10282 |
| VERLAUF-TEIL-006.md | V0054–V0054 | 36916 |
| VERLAUF-TEIL-007.md | V0054–V0089 | 19533 |
| VERLAUF-TEIL-008.md | V0090–V0090 | 36704 |
| VERLAUF-TEIL-009.md | V0090–V0091 | 20458 |
| VERLAUF-TEIL-010.md | V0092–V0092 | 36786 |
| VERLAUF-TEIL-011.md | V0092–V0161 | 35324 |
| VERLAUF-TEIL-012.md | V0162–V0220 | 34885 |
| VERLAUF-TEIL-013.md | V0221–V0222 | 7462 |
| VERLAUF-TEIL-014.md | V0223–V0223 | 36858 |
| VERLAUF-TEIL-015.md | V0223–V0228 | 37294 |
| VERLAUF-TEIL-016.md | V0229–V0286 | 36818 |
| VERLAUF-TEIL-017.md | V0287–V0351 | 35663 |
| VERLAUF-TEIL-018.md | V0352–V0358 | 7171 |
| VERLAUF-TEIL-019.md | V0359–V0359 | 36425 |
| VERLAUF-TEIL-020.md | V0359–V0359 | 36898 |
| VERLAUF-TEIL-021.md | V0359–V0405 | 37325 |
| VERLAUF-TEIL-022.md | V0406–V0438 | 35927 |
| VERLAUF-TEIL-023.md | V0439–V0464 | 36017 |
| VERLAUF-TEIL-024.md | V0465–V0481 | 32051 |
| VERLAUF-TEIL-025.md | V0482–V0490 | 33363 |
| VERLAUF-TEIL-026.md | V0491–V0499 | 23392 |
| VERLAUF-TEIL-027.md | V0500–V0516 | 36226 |
| VERLAUF-TEIL-028.md | V0517–V0544 | 36214 |
| VERLAUF-TEIL-029.md | V0545–V0562 | 24723 |
| VERLAUF-TEIL-030.md | V0563–V0563 | 36814 |
| VERLAUF-TEIL-031.md | V0563–V0563 | 36537 |
| VERLAUF-TEIL-032.md | V0563–V0575 | 23406 |
| VERLAUF-TEIL-033.md | V0576–V0576 | 36909 |
| VERLAUF-TEIL-034.md | V0576–V0630 | 37433 |
| VERLAUF-TEIL-035.md | V0631–V0692 | 36631 |
| VERLAUF-TEIL-036.md | V0693–V0752 | 37488 |
| VERLAUF-TEIL-037.md | V0753–V0815 | 37409 |
| VERLAUF-TEIL-038.md | V0816–V0847 | 36552 |
| VERLAUF-TEIL-039.md | V0848–V0853 | 6588 |
| VERLAUF-TEIL-040.md | V0854–V0854 | 35944 |
| VERLAUF-TEIL-041.md | V0854–V0854 | 36863 |
| VERLAUF-TEIL-042.md | V0854–V0876 | 34771 |
| VERLAUF-TEIL-043.md | V0877–V0888 | 20874 |
| VERLAUF-TEIL-044.md | V0889–V0901 | 37080 |
| VERLAUF-TEIL-045.md | V0902–V0913 | 34572 |
| VERLAUF-TEIL-046.md | V0914–V0949 | 35238 |
| VERLAUF-TEIL-047.md | V0950–V0961 | 36679 |
| VERLAUF-TEIL-048.md | V0962–V0966 | 13872 |
| VERLAUF-TEIL-049.md | V0967–V0967 | 36959 |
| VERLAUF-TEIL-050.md | V0967–V0993 | 35353 |
| VERLAUF-TEIL-051.md | V0994–V1003 | 34680 |
| VERLAUF-TEIL-052.md | V1004–V1012 | 34229 |
| VERLAUF-TEIL-053.md | V1013–V1015 | 27273 |
| VERLAUF-TEIL-054.md | V1016–V1016 | 16911 |

Weitere Dateien: `VERLAUF-VERZEICHNIS.tsv` (jede Nachricht mit Teil), `verlauf.jsonl` (maschinenlesbar, geschwärzt).
