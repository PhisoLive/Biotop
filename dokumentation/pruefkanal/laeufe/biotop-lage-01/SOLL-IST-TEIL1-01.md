# BIOTOP-LAGE-01 · Fassung 2 · `SOLL-IST-TEIL1-01.md`

- **Inhalt:** FK30 · Entwurf E, Stück 1 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil E, Arbeitszeit 25.09.2026 16:10:47–18:55:32 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/soll-ist/SOLL-IST-TEIL1.md` · 27887 B · SHA-256 `841a8694677ce607a7b146a9f48730fa8f414da036ec3af68fb6f5451646b38d`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (12 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# SOLL-IST — Abgleich gegen Masterprompt Fassung 8 (FK30) · Teil 1 von 4

**Entwurf Teil E der Offenlegung BIOTOP-LAGE-01 Fassung 2**, geschrieben im Namen von Hermes. Die Nummer `-01` vergibt Hermes beim Veröffentlichen.

- **Soll:** `arbeit/dokumente/2026-09-23_155353_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md`, 551 Zeilen (Fassung 8 vom 23.09.2026; Pfad relativ zu `/root/sicherung/biotop-lage-01/`). Jede Angabe „Z.“ ist eine Zeilennummer dieser Datei.
- **Ist, Zeitpunkt des Lesens:** 25.09.2026, 16:05 bis 18:30 CEST.
  - Biotop-Kern: HEAD `0c2f058` vom 24.09.2026 20:24 CEST, abgelesen um 17:56 CEST (R150). Die Code-Stellen habe ich im Arbeitsbaum `/root/biotop` zwischen 16:27 und 18:20 CEST gelesen. S1c baut gleichzeitig im Baum. Ob der Arbeitsbaum von `0c2f058` abwich, ist nicht erhoben: `git status` ist nach Regel 2 nicht erlaubt.
  - Den Endstand von S1c und der Runde 6 trägt Hermes nach. Davon hängen ab: MP0.1, MPK.2, MP8.38, MP8.42, MP8.58 bis MP8.70 und MP9.1 bis MP9.7. Sie beschreiben den Stand gegen 18:00 CEST.
- **Teile:** Teil 1 enthält Kopf, Lesart, die zwei Stellen aus dem Änderungsverzeichnis von v8 und die Abschnitte 0 bis 3.7. Teil 2 enthält 3.8 bis 7 und aus Abschnitt 8 die Phasen 1 bis 3. Teil 3 enthält aus Abschnitt 8 die Phasen 4 und 5, außerdem die Abschnitte 9, 10 und die Anhänge. Teil 4 enthält die UNKLAR-Liste für FK47, die Lücken, die Widersprüche und den Prüfbeleg.

## Zählung je Status (gerechnet)

Gezählt über alle Einträge der Teile 1 bis 3 mit dem Prüfskript `e13_pruefen.py`; den Rohbeleg nennt Teil 4, Abschnitt 4.

| Status | Einträge |
|---|---|
| BELEGT | 117 von 196 |
| TEILWEISE | 37 von 196 |
| OFFEN | 2 von 196 |
| NICHT BEGONNEN | 24 von 196 |
| ABGEWICHEN | 0 von 196 |
| ENTFALLEN | 1 von 196 |
| UNKLAR | 15 von 196 |

Rechenweg: 117 + 37 + 2 + 24 + 0 + 1 + 15 = 196 Einträge. Je Teil: 56 in Teil 1, 84 in Teil 2, 56 in Teil 3; 56 + 84 + 56 = 196.

- Die Einträge `NICHT BEGONNEN` sind Tor 4 je Testwerk (15, MP8.43 bis MP8.57), die Testwerke T4 bis T6 (3, MP8.38 bis MP8.40) und Phase 5 (6, MP8.71 bis MP8.76); 15 + 3 + 6 = 24.
- `ABGEWICHEN` kommt nicht vor, weil ich zu keiner Abweichung die Entscheidung gefunden habe, die dieser Status verlangt. Abweichungen ohne belegte Entscheidung stehen als `UNKLAR`, etwa MP6.2 und MP7.1 bis MP7.5 (Auslegung Hermes).

## Lesart (Auslegung Hermes)

1. **Was ein Eintrag ist.** Aufgenommen ist jede Stelle von v8, die eine Lieferung, eine Vorbedingung, eine Torzeile, eine Pflichtdatei oder eine Regel mit prüfbarem Ergebnis verlangt.
   - Nicht aufgenommen: Begründungen, die „Stand“-Absätze mit Wertungen Chat-Claudes, Kostenschätzungen und Kann-Bestimmungen (Klassenmaß Z. 179; „z. B. tree-sitter“ Z. 154).
   - Die Grundsätze 2a sind nur dort eigene Einträge, wo sie selbst eine Lieferung nennen (MP2a.1, MP2a.2). Sonst sind sie über die Vorbedingungen für T4 abgebildet.
   - Aus dem Änderungsverzeichnis (Z. 6–78) sind zwei Stellen aufgenommen: die Streichung des Handelssystems (Z. 14) und die Zwischenbericht-Pflicht (Z. 43), weil diese im Hauptteil fehlt.
2. **Kennung:** `MP<Abschnitt>.<laufende Nummer>`. Die Abschnittsnummern stehen so da wie in v8, also 2a und 3.1 bis 3.15. Anhang A heißt `MPA`, Anhang B `MPB`. Die zwei Stellen aus dem Änderungsverzeichnis am Kopf von v8 (vor Abschnitt 0, ohne Nummer) heißen `MPK`.
3. **Status ist Zuordnung zum Beleg, keine Torwertung** (Regel 2.9).
   - Bei einer Torzeile heißt `BELEGT` nur, dass eine Messung vorliegt. Messwert, Grenze und Wertung stehen in `TORE` (Teil C). Ob die Zeile besteht, wertet Chat-Claude.
   - `OFFEN` heißt: verlangt, aber nicht gebaut oder nicht geliefert. `NICHT BEGONNEN` heißt: Das Werk oder die Phase, an der die Forderung hängt, hat noch nicht begonnen.
4. **Tor 4 (Fassung 8) gilt je Testwerk.** T3 lief vor Fassung 8, wurde nach dem Wortlaut von Fassung 7 gemessen und ist nicht abgenommen (Z. 456). Er „zählt nicht zur Sättigung des Breitentests“ (Z. 461).
   - Die Tor-4-Zeilen stehen deshalb mit dem Blick auf T4 als `NICHT BEGONNEN`.
   - Zu jeder Zeile steht als Hinweis der T3-Stand mit Verweis auf `TORE`.
5. **„Anbieter“** je Nische (Z. 206, 312, 379) lese ich als „Hersteller“. Alle Modellaufrufe laufen über den einen Anbieter OpenRouter (R103). Grundlage ist Philipp am 18.09.: „OpenRouter mit zwei verschiedenen Herstellern für die Masse“ (`PH` Z. 20).
6. **Zahlen** in der Tabelle sind abgelesen aus der genannten Quelle, sofern nicht „gerechnet“ dabei steht.
   - Kosten, Budgets und Buchungszahlen stehen in `CHRONIK` (FK20) und `KASSE`, Torwerte in `TORE`, der Umfang der Werke in `LAGE` (FK25), die Fassungen in `ENTSCHEIDUNGEN` (FK15).
   - Hier steht nur, was die Zuordnung braucht.
7. **Code-Stellen** sind als Text gelesen, nicht ausgeführt, soweit nicht ein Bericht die Ausführung belegt.

## Kürzel der Quellen

| Kürzel | Datei |
|---|---|
| `P1B` | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/BERICHT.md` |
| `P1N` | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/BERICHT.md` |
| `P2B` | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/BERICHT.md` |
| `P3B` | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/BERICHT.md` |
| `P3N` | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/BERICHT.md` |
| `VB1B` | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/BERICHT.md` |
| `T3A` | `/root/biotop-t3/ABSCHLUSSBERICHT.md`; byte-gleich mit `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-01/ABSCHLUSSBERICHT.md` (R150) |
| `R1B` … `R5B` | `/root/biotop-vor-t4/BERICHT.md`, `/root/biotop-vor-t4-02/BERICHT.md` … `-05/BERICHT.md`; byte-gleich mit `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/BERICHT.md` … `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-05/BERICHT.md` (R150) |
| `R6U` | `/root/biotop-vor-t4-06/UEBERGABE.md` (Runde 6, läuft). Im Prüfkanal liegt die Datei nicht (R150). |
| `PH` | `arbeit/lesen/philipp-ab-2026-09-18.md` (Nachrichten Philipps, geschwärzt) |
| `HP` | `arbeit/lesen/hermes-an-philipp.md` (Meldungen von Hermes) |
| Code | `/root/biotop/biotop/…`, gelesen im Arbeitsbaum (siehe Kopf) |
| R66 … R157 | Rohbelege der Erhebung dieses Teils: `rohbelege/R0066.txt` usw. Die Skripte liegen in `entwurf/soll-ist/e1…e12*.py`, alle nur lesend. Den Prüfbeleg (Skript `e13_pruefen.py`) nennt Teil 4, Abschnitt 4. |

Die Rohbelege dieses Teils:

| Beleg | Inhalt |
|---|---|
| R66 | Maß-Bestätigung und Freigabe je Lauf, aus `arbeit/kasse/laeufe.csv` |
| R67 | Pflichtbestandteile nach Abschnitt 9 je Ordner, aus `arbeit/inventar/i3.json` |
| R76 | Belegstellen im Code |
| R77 | Belegstellen in den Berichten |
| R83 | Geschmack, Kontingent, Protokollarten, aus STAMM und T3 |
| R99 | Verfassungsdateien mit SHA-256 |
| R100 | Freigaben, Mentorwahl und Maß je Lauf |
| R103 | schwere Modelle, Spalten, lagerhaus-Regeln |
| R111 | T3-Freigaben im Wortlaut und ihr Zeitabstand |
| R126 | `_beschleunigen`, Verfall, Vorgänger-Namen, Geschmack je Lauf |
| R150 | Gleichheit der Arbeitskopien mit dem Prüfkanal; git log |
| R157 | Mentor- und Jury-Aufrufe je Laufgruppe; Protokollarten `mentor.*` und `jury.*` |

**Abweichung beim Erheben (FK41):** R83, R100, R103, R111, R126 und R157 haben `/root/biotop-t3/t3.db` mit bloßem `?mode=ro` geöffnet, wie es die Regeln damals erlaubten. Nach Befund R164 von Hermes schreibt das die Datei `t3.db-shm`. R157 begann um 18:14:31 CEST, zur selben Sekunde wie die dort festgestellte Änderung an `t3.db-shm`. Die Zweig-Datenbank VB1 haben meine Skripte nicht geöffnet; aus dem Ordner VB1 lasen sie nur die zwei Verfassungsdateien (R99, R103). STAMM wurde nur mit `mode=ro&immutable=1` und leerer `-wal` geöffnet.

## Kopf von v8 — Änderungsverzeichnis (ohne Abschnittsnummer)

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MPK.1 | 14 | „Das Handelssystem stand in den Fassungen 1 bis 6 als Phase-4-Werk, war aber eine nie bestätigte Vorentscheidung von Chat-Claude; alle darauf bezogenen Bezugsgrößen (237.000 Zeilen, 17 Dienste, 135 Testfehlschläge) sind gestrichen.“ | ENTFALLEN | Entscheidung Philipps vom 21.09.2026 (v8 Z. 13–14). Übermittelt in `PH` Z. 371: „Das Handelssystem ist als Phase-4-Werk gestrichen“. Damit entfällt auch die zuvor angekündigte „Vorbedingung 2 — die Verfassung des Handelssystems“ (`PH` Z. 280). |
| MPK.2 | 43 | „vor jedem Sitzungsende `ZWISCHENBERICHT.md` und `DATEIEN.txt` im Ordner; ein Ordner ohne Bericht gilt als nicht abgeliefert. Endmeldungen nennen die vollständige Abholadresse als ganze URL.“ | TEILWEISE | Die Pflicht steht nur im Änderungsverzeichnis, nicht in Abschnitt 9 (Lücke, Teil 4). Im Prüfkanal (R67) fehlen `BERICHT*.md` und `ZWISCHENBERICHT*.md` zugleich nur in `biotop-lage-01` (dieser Auftrag, läuft). `DATEIEN*.txt` fehlt in `biotop-lage-01` und `biotop-vor-t4-06` (Runde 6, läuft). Ob jede Endmeldung die ganze URL nennt, ist nicht geprüft (siehe MP9.7). |

## Abschnitt 0 — Auftrag in drei Sätzen

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP0.1 | 84 | „Baue ein System, in das man ein Software-Werk hineinlegt … und das dieses Werk in Generationen auf ein messbar höheres Niveau hebt“ | TEILWEISE | Die Phasen 1 bis 3 sind gewertet (Z. 372, 390, 410). Phase 4 läuft: T3 ist nicht abgenommen (Z. 456), Runde 6 vor T4 läuft (`R6U`). Phase 5 ist nicht begonnen. Es fehlen die Abnahme des Breitentests und das erste echte Werk (MP8.57, MP8.71). |

## Abschnitt 1 — Das Bild

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP1.1 | 92 | „Kein Begriff steht in der Oberfläche, hinter dem keine Wirkung liegt.“ | BELEGT | Die Oberfläche hat 18 Bedienelemente, jedes mit Codestelle (`P3B` Z. 41, Tor 3 Zeile 9 `P3B` Z. 137). Das ist der Stand von Phase 3. Spätere Änderungen an `oberflaeche.py` sind nicht nachgeprüft. |

## Abschnitt 2 — Verfassung des Biotops

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP2.1 | 100 | „Die Messung entscheidet, nie die KI.“ | BELEGT | Der Freigabegrund im T3-Protokoll lautet „Messung entscheidet, kein Modellurteil.“ (R111). Angenommen wird über Kernmaß und Pareto (MP3.5.1–MP3.5.3). |
| MP2.2 | 101 | „Das Maß steht vor der ersten Generation fest und wird danach nicht verhandelt.“ … „Jede Änderung an Messskripten, Ankläger-Ablauf, Pareto-, Grenz- oder Nischenregeln während eines Laufs beendet diesen Lauf“ | BELEGT | Mit Status `verworfen` stehen die Läufe 14, 15, 16, 18, 19 und 21 in der Kasse (R66). Die ersten fünf gehören zu Phase 3, passend zu v8 Z. 320 („fünf nach Satz 2 verworfene Läufe“); Lauf 21 gehört zum Nachlauf zu Phase 3 (Läufe 21–23, Z. 412). Der Code verweigert ein zweites `eichen` für denselben Lauf (`organe/stufe2.py:22`, R126). |
| MP2.3 | 102 | „Kein Bereich verbessert sich auf Kosten eines anderen.“ | BELEGT | Nebenwirkungsprobe Tor 2 (`P2B` Z. 19). Mit gehärteten Proben wieder belegt in `P3N` Abschnitt 2 (Z. 50 ff.). |
| MP2.4 | 103 | „Das laufende Biotop verändert seinen eigenen Code nie.“ | BELEGT | Kandidaten sind Diffs am Werk (`kern/diffwerk.py`) und laufen in der Kammer (MP3.13.1). Der Biotop-Code ändert sich nur durch Commits von Hermes zwischen den Läufen (R13). Gelesen, nicht ausgeführt. |
| MP2.5 | 104 | „Jede angenommene Generation ist ein vollständiger, rückholbarer Schnappschuss“ | BELEGT | Tor 1 Lazarus (`P1B`; `P1N` Z. 21 „gilt weiter“). |
| MP2.6 | 105 | „Laut scheitern, nie still.“ | BELEGT | Tor 1 „Laut scheitern“ (`P1N` Z. 23). |
| MP2.7 | 106 | „Jeder gefundene Fehler wird zu einem Test (Immunisierung). Derselbe Fehler kann das Werk nie zweimal treffen.“ | TEILWEISE | Auf dem Python-Pfad belegt: Tor 2 Immunisierung (`P2B` Z. 23). Auf dem TypeScript-Pfad fehlt der Beleg: T3 „Nicht belegt: Immunisierung“ (Z. 460). Der Bau steht in MP8.66. |
| MP2.8 | 107 | „Ein Budget je Lauf, vor dem Start gesetzt; bei Erreichen Abbruch mit Meldung vor dem nächsten Modellaufruf — nie danach.“ | BELEGT | Tor 1 Kasse (`P1N` Z. 22). Die Vorprüfung vor jedem Aufruf steht in `kern/kasse.py:116`, aufgerufen aus `anbieter/__init__.py:198` (R76). T3 meldete „Budgetgrenze nie scharf“ (Z. 461). Die Behebung („bucht den HÖCHSTFALL“, `kasse.py:183`, R76) ist gelesen, nicht ausgeführt. |
| MP2.9 | 108 | „Alle Gedächtnisse liegen dauerhaft auf dem Server, nie im Arbeitsspeicher, und sie werden gelesen, nicht nur beschrieben.“ | BELEGT | Die Tabellen `projektgedaechtnis`, `artgedaechtnis` und `geschmack` stehen in STAMM und T3 (R83). `P3B` Z. 36: „alle vor jeder Generation gelesen“. |
| MP2.10 | 109 | „Für jedes Bedienelement muss Hermes die Codestelle belegen, die es liest.“ | BELEGT | Wie MP1.1 (`P3B` Z. 41, Z. 137). |
| MP2.11 | 110 | „Diese Prüfung ist Teil der Aufnahme und wird nicht vom Werk selbst beantwortet.“ | BELEGT | `organe/aufnahme.py:25` (`ETHIK_WOERTER`) und `:92` (`_ethik`), R76. Beschrieben in `P1B` Z. 39. |

## Abschnitt 2a — Vierzehn Grundsätze

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP2a.1 | 116 | „wer ein neues Organ baut, prüft es gegen diese vierzehn“ | TEILWEISE | Die Prüfung gegen die Grundsätze 1–6 steht in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/GRUNDSAETZE-2a-01.md`, Kopf „Die sechs Grundsätze gegen meinen eigenen Code“, Maßstab Fassung 6. Eine Prüfung der Organe gegen die Grundsätze 7–14: NICHT GEFUNDEN. Gesucht habe ich in allen `BERICHT.md` unter `/root` (0 Treffer). Es fehlt die Prüfung gegen die Grundsätze 7–14. |
| MP2a.2 | 129 | „Der Verdrahtungstest in jeder Regression fährt einen ganzen Lauf und wird rot, wenn ein Organ nie oder nicht aus der vorgeschriebenen Stelle gerufen wird.“ | TEILWEISE | Gebaut und grün in den vollen Regressionen der Runde 1 (`R1B` Z. 55). Dort steht aber: „die Phasenbindung ist nur am Prüfwerkzeug belegt“. Siehe MP8.64. |

## Abschnitt 3.1 — Aufnahme

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.1.1 | 142–143 | „Ein Werk entgegennehmen (ZIP, Git-Adresse, Ordner), entpacken, Sprache(n) und Bauwerkzeuge erkennen“ … „Aufnahmebericht mit Zahlen“ | BELEGT | `organe/aufnahme.py:13`, `:40` und `:43–44` behandeln ZIP und `git clone` (R76). `P1B` Z. 39 beschreibt Zählung, ersten Testlauf in der Kammer und ethische Prüfung. |
| MP3.1.2 | 144 | „Ohne Tests oder ohne bauenden Zustand startet keine Generation“ | BELEGT | Tor 1 „Laut scheitern“ (`P1N` Z. 23); `MessgeraetFehlt` (`P1B` Z. 39). |

## Abschnitt 3.2 — Landkarte

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.2.1 | 147 | „Das Werk in Zoomstufen kartieren, damit das Biotop das Ganze sieht, ohne alles auf einmal lesen zu müssen.“ | TEILWEISE | Die Tabelle `landkarte` hat die Spalten `stufe`, `pruefsumme` und `herkunft` (R103). Tor 1 Landkarte (`P1N` Z. 17). Die Zoomstufen sind nicht an einem Werk belegt, das nicht in einen Aufruf passt. v8 Z. 426: „bisher nie nötig — beide Übungswerke passten ganz in einen Aufruf“. Das prüft erst T4. |
| MP3.2.2 | 153 | „An jeder Grenze zwischen zwei Bereichen die Zusicherungen“ … „kennzeichnet sie als abgeleitet“ | BELEGT | Die Tabellen `vertraege` und `vertraege_explizit` (R83). Die Ordner `verfassungen/vertraege-lagerhaus` und `vertraege-logmuehle` (R76). Vertragsprobe Tor 2 (`P2B` Z. 22). |
| MP3.2.3 | 154 | „Zusammenfassungen je Stufe durch ein Modell, in der Datenbank gespeichert, mit Prüfsumme der Quelldatei, damit veraltete Zusammenfassungen erkannt werden.“ | TEILWEISE | Die Spalte `pruefsumme` in `landkarte` ist vorhanden (R103). Ob veraltete Zusammenfassungen erkannt werden, ist NICHT AUSGEFÜHRT und nicht gelesen. |
| MP3.2.4 | 154 | „Der bestehende Aktenschrank (Chunking + Stichwort- und Bedeutungssuche) wird Teil der Landkarte.“ | OFFEN | Im Code NICHT GEFUNDEN: Das Muster `aktenschrank\|embedding\|cosinus\|cosine` trifft 0 Zeilen in 48 `.py`-Dateien (R76). Den Vorgänger gibt es auf der Maschine nicht; siehe MP7.1. |
| MP3.2.5 | 155 | „Ein Schwarm-Aufruf bekommt nie“ … „sondern Stufe 0 + Stufe 1 + den Bereich, an dem er arbeitet, auf Stufe 3 + die Verträge an dessen Grenzen.“ | BELEGT | `organe/landkarte.py:248–269`, Funktion `sicht`. Ihr Docstring: „Die einzige Sicht des Schwarms: Stufe 0 + Stufe 1 (alle) + Stufe 3 des Bereichs + Verträge des Bereichs und seiner Nachbarn.“ Gerufen wird sie aus `organe/genesis.py:126`. Gelesen, nicht ausgeführt. Ob die Sicht bei einem Werk trägt, das nicht in einen Aufruf passt, prüft erst T4 (Z. 426). |

## Abschnitt 3.3 — Verfassung des Werks

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.3.1 | 158–159 | „Vor der ersten Veränderung mit Philipp festlegen“ … „Philipp streicht, ergänzt, bestätigt. Erst dann ist sie gültig.“ | BELEGT | `lagerhaus`: Anhang A, von Philipp delegiert (Z. 161). `logmuehle`: Anhang B, bestätigt. `versandwerk` (T3): `PH` Z. 377 „Verfassung bestätigt mit drei Auflagen“. Die Dateien mit SHA-256 stehen in R99. Den Wortlaut enthält `VERFASSUNGEN` (FK22). |
| MP3.3.2 | 161 | „Für Übungswerke schreibt Chat-Claude die Verfassung; Philipp hat die Entscheidung delegiert.“ | BELEGT | `verfassungen/lagerhaus.md` ist gleich der Kopie im Zweig VB1, SHA-256 `326e2616…` (R99). `lagerhaus.regeln.json` unterscheidet sich in den Bytes, hat aber keinen abweichenden Schlüssel oder Wert (R99, R103). |
| MP3.3.3 | 162 | „Eine Verfassung darf festlegen, was gegen was getauscht werden darf“ … „Ohne Tauschregel gelten die Vorgaben aus 3.5.“ | BELEGT | `kern/messgeraet.py:494–501`, `grenzen_f2(…, tausch)` (R76). In `logmuehle` gilt `tausch.laufzeit_faktor_bei_sicherheitsgewinn` = 3.0 (R99). Das Maßfeld der Läufe nennt „Tauschregel Anhang A Satz 2“ (R66). |

## Abschnitt 3.4 — Mentor

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.4.1 | 166 | „3–5 Entwicklungsrichtungen, je mit: Ertrag (welches Maß würde steigen), Risiko“ | BELEGT | Tor 3 Mentor (`P3B` Z. 94). `organe/mentor.py:84` prüft `anzahl_ok` mit 3 bis 5 Richtungen (R76). |
| MP3.4.2 | 167 | „Philipp wählt die Richtung. Das Biotop kann eine Empfehlung mit Begründung geben, wählt aber nicht selbst.“ | UNKLAR | Siehe MP4.3: In den T3-Läufen gibt es keine Protokollzeile `mentor.gewaehlt`. |

## Abschnitt 3.5 — Maß und Messgerät

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.5.1 | 173 | „Kernmaß je Bereich“ … „Bestandene Tests zählen nicht.“ | BELEGT | Das Kernmaß F2 steht im Protokollfeld `kernmass_f2` jeder Freigabe (R83, R111). Tor 1 im Nachlauf (`P1N` Z. 18). |
| MP3.5.2 | 174 | „Vorgeneration und Kandidat werden mit demselben Testbestand gemessen“ … „Die Verlaufskurve eines Laufs wird am Laufende mit dem Endbestand aller Tests neu gerechnet“ | BELEGT | Befehl `kurve` mit `--testbestand-von-lauf` (`__main__.py:71` und `:144–145`, R76). Kurve Tor 2 (`P2B` Z. 25). |
| MP3.5.3 | 175 | „Jeder einzelne Test, der an der Vorgeneration besteht und am Kandidaten fällt, ist eine Regression und tötet den Kandidaten“ | BELEGT | Regressionsprobe Tor 2 (`P2B` Z. 20). Mit gehärteten Proben wieder belegt (`P3N` Z. 50 ff.). |
| MP3.5.4 | 176 | „Bezug ist der Bestwert des Laufs“ … „Laufzeiten werden grundsätzlich als Median aus drei Durchläufen gemessen, nie als Einzelwert.“ | UNKLAR | **v8 widerspricht sich.** Grundsatz 14 (Z. 131) lautet „nie gegen ein historisches Minimum … je Seite der Median mehrerer Messungen“, ebenso die Vorbedingung T4 Nr. 1 (Z. 464). Z. 461 zählt „Median aus drei“ zu den gefundenen Messgerätfehlern. Gebaut ist `messgeraet.laufzeit_gepaart` mit Median über je 5 Messungen je Seite (`R1B` Z. 49). Welche Stelle gilt, steht als Frage in FK47. |
| MP3.5.5 | 176 | „Die Rauschtoleranz wird gemessen, nicht gesetzt“ … „die Toleranz ist die gemessene Spannweite plus 10 Prozentpunkte, mindestens 15 %“ | BELEGT | Im Nachlauf zu Phase 3 gebaut (Z. 412 „gemessene Rauschtoleranz“; `P3N` Abschnitt 1, Z. 32). Die Einzelwerte werden gespeichert (`R1B` Z. 59). |
| MP3.5.6 | 176 | „Größte Funktion absolut 60 Zeilen“ | BELEGT | Das Maßfeld der Läufe ab Lauf 12 nennt „groesste_funktion absolut 60“ (R66). |
| MP3.5.7 | 177 | „Ohne Kurve ist ein Abschlussordner unvollständig.“ | TEILWEISE | Kurven liegen vor für Phase 2 (`P2B` Z. 25) und Phase 3 (`P3B` Z. 154). Für T3 NICHT GEFUNDEN: Unter `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/` gibt es keinen Dateinamen `*urve*`, das Wort „Kurve“ steht dort nur in `MASTERPROMPT-v7.md`. Unter `/root/biotop-t3` liegt nur `pruefung/kurve.py` in zwei Sicherungsordnern (R103). Es fehlt die Verlaufskurve T3, oder ihr Fundort ist anders benannt. |
| MP3.5.8 | 178 | „Die Nische Der Schnelle wird an der Laufzeit gemessen“ | BELEGT | Tor 2 S2 (`P2B` Z. 18). |
| MP3.5.9 | 180 | „Eine Sicherheitsschwäche gilt erst als behoben, wenn der statische Befund verschwunden ist und die für diese Befundklasse bekannte Umgehung als Immuntest im Werk liegt.“ | BELEGT | Tor 1 Zeile 2, S1 (`P1N` Z. 18). |
| MP3.5.10 | 181 | „bewertet eine Jury aus mindestens drei Modellen verschiedener Anbieter mit Begründung“ | BELEGT | Tor 3 Jury (`P3B` Z. 109; die Wertung steht in `TORE`). `lauf.py:358–359` ruft die Jury bei Gleichstand (R76). |
| MP3.5.11 | 182 | „Vor Generation 0 prüft das Biotop sich selbst. Fünf Teile, in dieser Reihenfolge“ | BELEGT | Gebaut im Nachlauf zu Phase 3 (Z. 412, `P3N` Z. 32–50). Die Tabellen `eichung`, `eichkosten` und `eichgegenstand` stehen in beiden Datenbanken, `vorspann_nachweise` nur in T3 (R83). Der Serienzähler steht in `organe/eichung.py:11` (R76). |
| MP3.5.12 | 188 | „Eichkosten getrennt ausweisen, Kammerläufe und Modellaufrufe je Teil, nie in der Laufsumme.“ | BELEGT | Tabelle `eichkosten` (R83). Die Buchung geschieht über `eichung.kosten_buchen` (`organe/stufe2.py:299`, R126). Die Beträge stehen in `CHRONIK`. |
| MP3.5.13 | 190 | „Er wird je Werk einmal gewählt und versiegelt, beim ersten Lauf, mit Prüfsumme und Begründung“ … „Bei Werken mit Betriebszweck muss der tragende Pfad ausdrücklich in den Regeln des Werks stehen“ | BELEGT | `P3N` Abschnitt 2 (Z. 50). Die Prüfskripte `pruefung/eichgegenstand_betriebszweck.py` und `eichgegenstand_verfassung.py` (R76). Die Präzisierung Chat-Claudes steht in `PH` Z. 100 und Z. 103. |
| MP3.5.14 | 192 | „Die Proben setzen mechanisch am Syntaxbaum an, nicht an Textankern“ | BELEGT | Reparatur 02 ist abgenommen. Philipps Nachricht (`PH` Z. 341): „fünf Eichfunktionen AST-unverändert“. Den Ordner `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/` gibt es; eine `BERICHT.md` enthält er nicht (R67). |
| MP3.5.15 | 194 | „Generation 0 evolutioniert dann die Tests, bis mindestens 80 von 100 Mutanten gefangen werden.“ | BELEGT | Tor 2 Generation 0 (`P2B` Z. 17). Die Messung aus T3 steht in `TORE`. |
| MP3.5.16 | 195 | „Äquivalenz wird vor der Zählung geprüft und belegt“ … „je blindem Mutanten zwei Durchläufe, bevor er als ungefangen gilt“ | BELEGT | `organe/generation0.py:236–275` enthält `aequivalenz_pruefen` und schreibt die Protokollart `generation0.aequivalenz`. `:380` lautet „je blindem Mutanten zwei Durchläufe (je 2 Hersteller)“. Gelesen, nicht ausgeführt. |
| MP3.5.17 | 196 | „Das Biotop schlägt das Maß vor, Philipp bestätigt, danach ist es eingefroren“ | TEILWEISE | Das Feld „bestätigt von“ des Maßes (R66). Philipp ist genannt bei 21 Läufen: Lauf 1; den Läufen 6–9 und 12–22 mit „Masterprompt vN Abschnitt 3.5 (Philipp, 19.09.2026)“; allen 5 T3-Läufen mit eingefrorenem Maß (31, 32, 36, 37, 38; R66, R100). Die Läufe 10, 23 und 24 nennen die Fassung ohne Namen, Lauf 25 den „Masterprompt Lauf 25“; die Läufe 3 und 11 haben kein eingefrorenes Maß. Keine Bestätigung Philipps haben: Lauf 2 „Vorschlag Hermes 18.09.2026 (Bestätigung Philipp offen …)“; Läufe 4 und 5 „Hermes (Kassenprobe)“; Lauf 26 (Zweig VB1) „Hermes unter Übungswerk-Vollmacht“. Es fehlt Philipps Bestätigung für diese 4 Läufe. Frage FK47: Deckt die Vollmacht die Maßbestätigung? |

## Abschnitt 3.6 — Genesis

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.6.1 | 200–205 | „Nischen (mindestens vier, erweiterbar)“ … „Population in Nischen nach dem MAP-Elites-Prinzip“ | BELEGT | Tor 2 Nischen (`P2B` Z. 16). Tabelle `eliten` (R83). |
| MP3.6.2 | 206 | „Mindestens zwei verschiedene Anbieter je Nische“ … „und gewichtet danach (Bandit-Verfahren).“ | BELEGT | `P2B` Z. 16 (vier Hersteller je Nische) und Z. 51 (Bandit). Tabelle `bandit` (R83). „Anbieter“ lese ich als Hersteller (Lesart 5). |
| MP3.6.3 | 206 | „Fällt ein Modell des Verbunds aus — Ablehnung durch den Anbieter, Zeitüberschreitung, leere Antwort —, zählt das als Ausfall und nie als Beitrag“ | BELEGT | Echte Ausfälle mit `beitraege=0` (`T3A` Z. 81–83; die Zahl steht in `TORE`). Code: `anbieter/__init__.py:25` und `:41–44` (R76). |
| MP3.6.4 | 207 | „Eine Antwort, die ehrlich keinen Kandidaten liefert, wird weder als Erfolg noch als Misserfolg gebucht und zählt nicht als Wahl.“ | BELEGT | `lauf.py:329–332`: Der Bandit bucht nur, wenn der Kandidat nicht den Status „leer“ („KEIN VORSCHLAG“) oder „zurückgestellt“ hat. Das eingefrorene Maß trägt `"bandit_kein_vorschlag": "neutral (3.6 F4)"` (`lauf.py:127`). Erkannt wird die Antwort in `organe/genesis.py:85` und `:103`. Gelesen, nicht ausgeführt. |
| MP3.6.5 | 208 | „Kandidaten als Änderungssätze (Diffs); jeder mit Begründung und der Angabe, welche Verträge er berührt. Ein Hunk über 60 % einer Datei gilt als Neuschreibung und wird abgelehnt“ | BELEGT | `kern/diffwerk.py:9–20` und `:116`: Neuschreibung abgelehnt, erlaubt bei Dateien unter 100 Zeilen. Gelesen, nicht ausgeführt. |

## Abschnitt 3.7 — Aegis, der Ankläger

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.7.1 | 213–217 | „Wirkungskreis bestimmen: alle Bereiche, die der Änderungssatz direkt oder über die Straßen der Landkarte berührt.“ … „Ausführung in der Kammer: Bauen, alle Tests, alle harten Maße“ | BELEGT | Die Proben zu Nebenwirkung, Regression, Norm und Vertrag in Tor 2 (`P2B` Z. 19–22), wieder belegt in `P3N` Abschnitt 2. |
| MP3.7.2 | 216 | „muss die für diese Klasse bekannten Umgehungen als Angriffstests liefern“ … „deshalb wird der Angriff bei Sicherheitsbefunden mit einem schweren Modell gefahren, nicht mit einem Schnellmodell.“ | BELEGT | Die Kassenzwecke `schwer.aegis.angriff.*` laufen über `anthropic/claude-sonnet-4.5` und `-5` (R103). Umgehungen bei S1 (`P1N` Z. 18). |
| MP3.7.3 | 218 | „Ein vom Ankläger gefundener Fehler wird sofort zu einem Test (Immunisierung, 3.10) — auch wenn der Kandidat ohnehin verworfen wird.“ | BELEGT | Tabelle `immunsystem` (R83). Tor 2 Immunisierung (`P2B` Z. 23). |
| MP3.7.4 | 219 | „Vor jedem Angriff gibt der Ankläger an, welche Behauptung er prüfen will“ … „wird der Angriff gar nicht erst ausgeführt“ | BELEGT | Bauteil A (`VB1B` Z. 24 und Z. 52). Im Register `aegis._ansage` (`kern/register.py:171–172`, R76). In T3 gibt es die Kassenzwecke `aegis.ansage.*` (R103). |
| MP3.7.5 | 221 | „Das gilt für jeden Test, der mit einem Kandidaten neu ins Spiel kommt“ | BELEGT | Norm-Probe Tor 2 (`P2B` Z. 21); `P3N` Abschnitt 2. |

*Fortsetzung in Teil 2.*
