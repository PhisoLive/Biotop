# BIOTOP-EINLAGERUNG-01 · WIEDEREINSTIEG · Teil 2 von 3 (Fassung 01)

Punkte 4–5: offene Entscheidungen und Lücken. Teil 1: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-einlagerung-01/WIEDEREINSTIEG-TEIL1-02.md

## 4. Offene Entscheidungen — als Erstes bei der Wiederaufnahme

### 4.1 Runde 6 und die Startregel für T4 (P3: entscheidet Philipp bei der Wiederaufnahme)

**Vorschlag Chat-Claude** (Auftrag BIOTOP-EINLAGERUNG-01, Abschnitt 5 Punkt 4, Wortlaut):

> „G schließen oder als gezählte Enthaltung führen, danach ein Review. Findet es wieder einen stillen Durchlass, wird er gezählte Enthaltung, und T4 startet ohne Runde 7. Begründung: sechs Runden statt einer, und jede fand eine neue Klasse. Neue Blindstellen zu finden ist die Aufgabe des Breitentests.“

Was dafür schon vorliegt: die Festlegung des Baus von G in `bau/S1C-PLAN.md` (Punkt 2.3), die 10 roten Spezifikationen `test_w_g_*` samt 5 Gegenproben im Commit `e8401af`, der Plan des Hermes aus LAGE FK46 (LAGE-TEIL1 Z. 173–185).

### 4.2 Fragen aus BIOTOP-LAGE-01 (LAGE-TEIL1 FK47, Wortlaut)

P1–P4 und C5 sind mit dem Auftrag BIOTOP-EINLAGERUNG-01 entschieden (REGELN-02 Abschnitt 4). Offen sind:

**An Philipp: P5–P20**

| Nr | Frage | Quelle |
|---|---|---|
| P5 | Gilt die Übungswerk-Vollmacht für T4, das ein anderes Modell erzeugt (v8 Z. 426 gegen Z. 288 und Z. 420)? | ENTSCHEIDUNGEN-TEIL4 FK19 |
| P6 | Wer schreibt und bestätigt die Verfassungen von T4–T6? | VERFASSUNGEN F1 |
| P7 | Ist die T3-Bestätigung als deine oder als Chat-Claudes zu führen? | VERFASSUNGEN F2 |
| P8 | Einreichung des Fehlalarm-Texts (P-12) | ENTSCHEIDUNGEN P-12 |
| P9 | T3 lief ohne Mentor und ohne Richtungswahl. Wer hat das entschieden, und gilt v8 Z. 167 und Z. 281 für Testwerke? | SOLL-IST U-E1 |
| P10 | Schwere Aufrufe laufen über OpenRouter statt über das Team-Kontingent. Ist das so gewollt? | SOLL-IST U-E6 |
| P11 | Gilt das Budget je Auftrag als Bestätigung „vor jedem Lauf“? | SOLL-IST U-E7 |
| P12 | Deckt die Vollmacht auch die Bestätigung des Maßes (VB1, Lauf 26)? | SOLL-IST FK47 (a) |
| P13 | Was folgt nach Phase 5? Wer setzt Tor 5, wer erklärt den Breitentest für abgeschlossen, wer wählt das Modell für T4? | LAGE-TEIL3 |
| P14 | Mit welcher Nachricht hast du die Delegation für Übungswerke erteilt? | VERFASSUNGEN L1 |
| P15 | Woher stammt „Philipp hat am 21.09. entschieden: Chat-Claude bestätigt die Verfassung …“? | VERFASSUNGEN L2 |
| P16 | Wo liegt „Prüfung 5 vom 20.09.“? (`GEDAECHTNIS_Hermes_2026-09-20.md`, das CHRONIK als NICHT GEFUNDEN führt, liegt im Prüfkanal: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/quellen/doc_c8bde0a20a81_GEDAECHTNIS_Hermes_2026-09-20.md, INVENTAR I4) | CHRONIK |
| P17 | Wer hat sich am 18.09. achtmal als root am Terminal angemeldet? | LAGE-TEIL4 |
| P18 | Wer schrieb den Auftragstext in id 1959 (19.09. 16:39)? | CHRONIK |
| P19 | Ist VORHER-NACHHER-S3 endgültig gestrichen? | LAGE-TEIL6 FK42 |
| P20 | Vorschlag nach deiner Regel vom 23.09.: Lesende Auswertungen mit `grep … \| python3` als dauerhafte Freigabe? Anlass A8 | A8 |

**An Chat-Claude: C1–C4 und C6–C11**

| Nr | Frage | Quelle |
|---|---|---|
| C1 | Welche Review-Fassung der Runde 4 gilt: `REVIEW.md` oder `REVIEW-B.md`? | CHRONIK; LAGE-TEIL4 |
| C2 | Gilt Anhang B im Wortlaut der Datei `0ce7f865…` oder im Wortlaut des Masterprompts? | VERFASSUNGEN F3 |
| C3 | Sollen die Regeldateien eigens bestätigt werden? | VERFASSUNGEN F4 |
| C4 | Soll die T3-Verfassung als Anhang in den Masterprompt? | VERFASSUNGEN F5 |
| C6 | „höchstens dreimal, dann Meldung an Philipp“ ist im Code nicht gefunden. Soll das gebaut werden? | SOLL-IST U-E3 |
| C7 | Die T3-Freigaben kamen Sekundenbruchteile nach der Generation. Ist das eine Freigabe unter Vollmacht oder Vollautomatik (v8 Z. 287)? | SOLL-IST U-E5 |
| C8 | Gilt „Übernehmen“ aus dem Vorgänger (Abschnitt 7) noch? | SOLL-IST U-E8 |
| C9 | W6: 35 gegen 40 Dateien | CHRONIK |
| C10 | Aufnahme von N-1 bis N-12 in Fassung 9 | ENTSCHEIDUNGEN-TEIL2 FK16 |
| C11 | Die Messgrenze „ungemessen unter 20 Tests“ steht nicht in v7/v8. Wird VB1 Lauf 26 nach T3-Methode nachgemessen? | TORE L1, L2 |

### 4.3 Kandidaten für Fassung 9

**N-1 bis N-12** — Änderungen und Anweisungen nach v8, die in keiner Fassung stehen (LAGE ENTSCHEIDUNGEN-TEIL2 FK16, Tafel im Wortlaut):

| Nr | Datum (CEST), id | Anweisung (Wortlaut, gekürzt mit „…“) | Steht es in v8? | Stand |
|---|---|---|---|---|
| N-1 | 23.09. 15:53:55, id 14000 | „Auftrag: die Behebungsrunde vor T4 — die elf Vorbedingungen in der dort genannten Reihenfolge … Kein Lauf, kein Modellgeld; volle Regression mit Verdrahtungstest, eigener Commit, ein Review, Abschlussordner laeufe/biotop-vor-t4/ …“ | Ja, bis auf den Ordner: v8 Z. 463–476 („Die Behebungsrunde kostet kein Modellgeld; sie endet mit voller Regression, eigenem Commit, einem Review und einem Abschlussordner.“) | Vollzug von v8, Runde 1 |
| N-2 | 23.09. 19:42:19, id 14337; wiederholt 19:49:24, id 14340 | „Stell den Träger dauerhaft auf Claude Opus 5.5 mit Denkstufe max — als Grundwert in config.yaml …“; „Der Zwischenbericht-Wächter zählt nur Aufrufe … ergänze einen zweiten Auslöser bei 80 % Kontextfüllung und bei der ersten gescheiterten Verdichtung, mit Gegenprobe.“ Dazu Klärung zu K2868 und eine Gegenprobe für den Test zur Gedächtnissperre | Nein: „Opus 5.5“, „Denkstufe“, „Träger“ und „Kontextfüllung“ je 0 | umgesetzt (`https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/BERICHT.md` §10 Nr. 1 und 4; MEMORY.md Z. 7) |
| N-3 | 23.09. 22:32:40, id 14624 | „Entscheidungen Chat-Claude zu deinen fünf Fragen: (1) … S1 ist an K2868 damit nicht sauber behoben, das korrigiert den T3-Befund … (2) Python-Sonde vor T4, die Torzeile bleibt … (3) … jeder Laufzeitriss vor der Ablehnung einmal gepaart nachgemessen … (4) Deckung je Abweichung, wie Grundsatz 11 es sagt. (5) Wächter je Turn.“ Dazu Auftrag Runde 2, Ordner -02 | Nein, außer (4); das steht in v8 Grundsatz 11 (Z. 128). „Python-Sonde“: 0. Die Korrektur zu S1 widerspricht v8 Z. 458 („Echt behoben: S1 …“) → W-6 | umgesetzt in Runde 2; (4) ersetzt durch N-4 (1) |
| N-4 | 24.09. 02:14:45, id 15154 | „Entscheidungen Chat-Claude: (1) Deckung je Muster … (2) Gewinnschwelle der Nische „schnell" in beiden Richtungen nachmessen … (3) Methoden von Klassen vor T4 beobachten … (4) S1 nicht neu versiegeln …“; „Der Reviewer ist an dieselbe Regel gebunden wie du: bei einer Sicherheitssperre anhalten und melden, nie auf anderem Weg lesen.“ Runde 3, Ordner -03 | Nein: „je Muster“, „Deckung je“ und „Methoden“ je 0 | umgesetzt in Runde 3. Die Nachricht enthält ihren Text zweimal hintereinander (3.434 Zeichen, R35) |
| N-5 | 24.09. 11:38:00, id 15962 | „Philipp gibt für genau diesen Fall frei, nicht als Dauerregel: Trenn die gebündelten Schritte in einzelne Befehle … Sperrt danach noch ein einzelner Schritt, halt an; dann führt Philipp ihn von außen aus. … Keine Codeänderung mehr in dieser Runde.“ | Nein; v8 regelt keine Befehlsfreigaben | erledigt (id 15992: „die getrennten Schritte liefen ohne Sperre“) |
| N-6 | 24.09. 11:49:51, id 15992 | „Entscheidungen Chat-Claude zu deinen sechs Punkten: (1) Vergleichslast: zweite Stufe mit zehnfacher Eingabegröße je Bereich … (2) … Weißraum also je Zeichen. (3) Merkmale von Argumenten, die die Sonde nicht verändert hat, gehören nicht zum Muster … (4) Tests, die der Kandidat selbst mitbringt, decken nicht … (5) Methoden in TypeScript vor T5 … (6) … ob er eingereicht wird, entscheidet Philipp.“ Außerdem: „Die Übergabe nach jedem abgeschlossenen Schritt nachführen …“ Runde 4, Ordner -04 | Nein: „Vergleichslast“ und „beglaubigt“ je 0 | umgesetzt in Runde 4; (6) ist offen (FK21) |
| N-7 | 24.09. 16:48:07, id 16482 | „Runde 5 schließt Klassen, nicht Fälle; Entscheidungen Chat-Claude: (1) Vollständigkeitsprüfung … (5) Verdrahtung über ein Register … das Tor-4-Skript wird gebaut … (6) Der Vorspann verweigert den Lauf ohne Stufe 2 …; Stufe-2-Lasten werden wie Stufe 1 bemessen und geeicht, bis eingang nicht mehr sperrt. … (8) Aus den niedrigen …“ | Nein: „Register“, „Tor-4-Skript“ und „Stufe-2“ je 0 | umgesetzt in Runde 5. Der Halbsatz „bis eingang nicht mehr sperrt“ aus (6) ist zurückgezogen (N-8) und ersetzt durch N-9 (4) |
| N-8 | 24.09. 21:00:41, id 16769 | „Kein Eingriff in den laufenden Job … als rote Spezifikation vor T4: Enthalten muss sich nur die betroffene Beobachtung. (2) … mein Auftrag „bis eingang nicht mehr sperrt" war ein Fehler … Und auf die Liste vor T4: Das Tor-4-Skript berechnet jede Zeile, die aus der Datenbank berechenbar ist …“ Der Text endet schon in der Quelle mit „Torzeilen von Han“ (R35) | Nein | übernommen als R6-1 bis R6-3 in Runde 6 |
| N-9 | 24.09. 23:15:27, id 16901 | „Es gilt das zweite Review … Das erste bleibt im Ordner als verworfen … künftig bekommt jedes Review einen eigenen Ordner, und du prüfst vor dem Start, dass keines läuft.“ Runde 6 mit „Entscheidungen Chat-Claude“: (1) typtreue Verfälschung, (2) Zustand aus C-Typen über eine bekannte Darstellung, (3) R6-1 und „Zeitgrenze je Funktion, nicht je Kandidat“, (4) Stufe-2-Last in eigener Eichphase, (5) Tor-4-Skript: jede Zeile, (6) Register vollständig, (7) Ausnahmen nach Typ und Inhalt, (8) Kappe am echten T4-Werk; TypeScript-Proben vor T5. **Startregel**, wörtlich: „Regel für den Start von T4, vorab gesetzt: T4 beginnt, sobald das Review dieser Runde keinen stillen Durchlass mehr findet — jede bekannte Lücke muss eine gezählte Enthaltung sein; Lücken, die sich nur enthalten, behebt T4 im Lauf.“ | Nein: „typtreu“, „C-Typen“, „Startregel“, „stillen Durchlass“ und „eigenen Ordner“ je 0. Auslegung Hermes: Die Startregel fügt den Vorbedingungen in v8 Z. 463–476 eine Bedingung hinzu. Lücken, die sich nur enthalten, verschiebt sie in den T4-Lauf | Runde 6 in Arbeit. Stand: `/root/biotop-vor-t4-06/UEBERGABE.md`, geändert 25.09. 12:52:04 CEST |
| N-10 | 25.09. 00:27:35, id 17217 | „Ordne U-1 bis U-4 nach der Startregel ein — ist einer davon ein stiller Durchlass …, dann gehört er mit Gegenprobe in diese Runde; die übrigen bleiben auf der Liste.“ Danach, eingeleitet mit „Wenn du dich für den Ersatzanbieter entscheidest, häng diesen Satz an:“: „Philipp legt fest: Die Verdichtung der Sitzungen läuft künftig über OpenRouter mit dem vorhandenen Schlüssel statt über die widerrufene Anmeldung — vorher config.yaml datiert sichern, danach mit einer echten Verdichtung belegen und die Kosten je Verdichtung nennen.“ | Nein: „Verdichtung“ 0 | beides umgesetzt: `/root/biotop-vor-t4-06/EINORDNUNG-U1-U4.md` (25.09. 00:43:44 CEST) und `VERDICHTUNG-OPENROUTER.md` (Umstellung 25.09. 01:08–01:14 CEST; Kosten → `KASSE`) |
| N-11 | 25.09. 01:06:55, id 17359 | „(a) — ich gebe die Sicherung frei. Geh in einzelnen Schritten vor wie beschrieben; ich bestätige die Freigabeabfragen sofort, sobald sie erscheinen.“ | Nein; Einzelfreigabe | erledigt (VERDICHTUNG-OPENROUTER.md Z. 14–17) |
| N-12 | 25.09. 14:44:20, id 20987 (Dokument); 14:44:22, id 20990 | „Neuer Auftrag BIOTOP-LAGE-01 Fassung 2 … nur sichern und offenlegen, Stand bis zum Stichzeitpunkt, am Biotop nichts ändern, nichts löschen, keine bezahlten Modellaufrufe.“ | Nein; betrifft die Offenlegung | gilt |

**Fassung-9-Lücken der Lückenliste** (LAGE VOLLSTAENDIGKEIT-TEIL2, Zeilen mit „Fassung 9“, Wortlaut):

| LU | Lücke | warum | schließt | wer |
|---|---|---|---|---|
| LU04 | 9 von 24 Punkten der Sammlung für Fassung 7 stehen nirgends als Regel (A L-5) | nicht übernommen | Aufnahme in Fassung 9 | C |
| LU21 | Die Messgrenze „ungemessen unter 20 Tests“ steht nicht in v7/v8 (C L2) | nicht übernommen | Fassung 9 (C11) | C |
| LU28 | Die 11. Zeile von Tor 2 und Tor 3 steht nicht im Tor-Block von v8 (C L9) | nicht übernommen | Fassung 9 | C |
| LU37 | Die Zwischenbericht-Pflicht steht nur im Änderungsverzeichnis, nicht in Abschnitt 9 (E L-E1) | Aufbau von v8 | Fassung 9 | C |
| LU57 | Die Startregel für T4 (id 16901) steht nur in einer Nachricht, nicht im Masterprompt (G) | nach v8 gesetzt | Fassung 9 (C10) | C |
| LU58 | v8 sieht eine Behebungsrunde vor T4 vor; es sind sechs, keine abgenommen (G) | Befunde je Runde | Fassung 9 oder Entscheidung (C10) | C |
| LU71 | Masterprompt v8 nicht nachgeführt: Lauf 38 „4 von 5“, Tor 2 Zeile 8 ohne „enger Nachtrag“, zwei Gründe für die Abbruchregel (H) | keine Fassung 9 | Fassung 9 (C10) | C |

Dazu aus diesem Auftrag: C5 (v8 Z. 176 an Z. 131/464 angleichen).

## 5. Offene Lücken

**Lückenliste:** LAGE VOLLSTAENDIGKEIT-TEIL2-01.md, https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL2-01.md (im Paket unter `dokumentation/pruefkanal/laeufe/biotop-lage-01/`). Zählung dort (Wortlaut):

- **Zählung (R220):** 92 vergebene Nummern.
  - 86 haben eine Zuständigkeit (je Zeile die erstgenannte Stelle): Hermes 44, Philipp 21, Chat-Claude 21.
  - 6 haben keine („–“), der Grund steht je Zeile:
    - nicht mehr schließbar: LU18, LU27, LU70, LU95;
    - mittelbar geprüft bzw. Zahlen liegen vor: LU19, LU88.

**Durch diesen Auftrag berührt** (Auslegung Hermes; die Liste selbst ist nicht geändert): LU02 (REGELN-02 geschrieben), LU03 (STAND-03), LU48 (Übergabe der Runde 6 veröffentlicht, RUNDE6-DOKUMENTE-01), LU80 (Datei aus A4: P2 umgesetzt), LU79/LU90 (Ablage 2 = Laptop; geschlossen, sobald Philipp „Abgeholt, Prüfsumme gleich“ meldet), LU89 (Regression mit Kammer im wiederhergestellten Stand, Teil 1 Punkt 2.6), LU93 (Hermes-Agent-Quelle jetzt in KOMPLETT; Caddy- und Prüfkanal-Konfiguration weiterhin nicht, siehe Teil 3 Punkt 9).

**Die zehn Lücken, die den nächsten Schritt am stärksten berühren** (Auswahl und Reihenfolge: Auslegung Hermes; Zeilen im Wortlaut, danach der Grund):

| LU | Lücke | warum | schließt | wer |
|---|---|---|---|---|
| LU29 | Runde 6 ohne Commit, volle Regression mit Kammer, Review und Bericht; Befund G offen (C L10, F) | S1c endete an der Grenze; Runde 6 ruht seit dem Stich | Weiterlauf nach Entscheidung (P3) | P |
| LU57 | Die Startregel für T4 (id 16901) steht nur in einer Nachricht, nicht im Masterprompt (G) | nach v8 gesetzt | Fassung 9 (C10) | C |
| LU58 | v8 sieht eine Behebungsrunde vor T4 vor; es sind sechs, keine abgenommen (G) | Befunde je Runde | Fassung 9 oder Entscheidung (C10) | C |
| LU91 | 2 `VorspannFehler` „Kernstand seit der Eichphase der Stufe 2 verändert“ in `tests/test_t3_bindung.py` (R203) | nicht untersucht | Test im Stand mit Kammer lesen und ausführen | H |
| LU44 | Keine Verteilung des Typsiebs, wenn der Kern Mutanten erzeugt; Tor-4-Zeile 3 hängt davon ab (E L-E8, C) | nicht gebaut | Bau vor T4 | H |
| LU20 | Nachmessung von VB1 Lauf 26 nach T3-Methode fehlt; davon hängt die Abnahme von Tor 2 Zeile 8 ab (C L1) | nicht beauftragt oder nicht gefunden | Messung ohne Modellaufruf oder Entscheidung (C11) | C |
| LU43 | Die Organe sind nicht gegen die Grundsätze 7–14 geprüft (E L-E7) | nur 1–6 geprüft | Prüfung | H |
| LU62 | Wie geht es nach Phase 5 weiter? Wer setzt Tor 5, wer erklärt den Breitentest für abgeschlossen, wer wählt das Modell für T4? (G) | v8 schweigt | Entscheidung (P13) | P |
| LU06 | T3 lief ohne Mentor und ohne Richtungswahl, 0 `mentor.gewaehlt` (A L-7, E L-E13) | nicht verlangt oder nicht gebaut | Entscheidung, ob v8 Z. 167/281 für Testwerke gilt (P9) | P |
| LU49 | Die Kasse führt den Laufstatus nicht nach: T3/31, /32, /36 „laeuft“, T3/38, STAMM 24 und 25 „bereit“, jeweils ohne Ende (F, H, I) | Status wird bei Abbruch nicht geschrieben | Datenpflege, braucht einen Auftrag (ändert das Biotop) | P |

Grund je Lücke:
1. **LU29** — Nach der Startregel ist T4 erst frei, wenn G geschlossen oder gezählte Enthaltung ist und ein Review keinen stillen Durchlass mehr findet. Commit (auf dem Einlagerungszweig) und eine Regression mit Kammer liegen jetzt vor; Review, Bericht und G fehlen.
2. **LU57** — Die Startregel steht nur in einer Nachricht (id 16901); die erste Entscheidung bei der Wiederaufnahme hängt an ihr.
3. **LU58** — Sechs Runden statt der einen in v8; genau darauf zielt der Vorschlag Chat-Claudes (4.1).
4. **LU91** — Die zwei `VorspannFehler` in `tests/test_t3_bindung.py` entscheiden, ob eine Regression als Beleg gilt; Ergebnis mit Kammer: Teil 1 Punkt 2.6.
5. **LU44** — Tor-4-Zeile 3 hängt an der Verteilung des Typsiebs; ohne Bau vor T4 ist die Zeile nicht messbar.
6. **LU20** — Tor 2 Zeile 8 (Vorbedingung 1) hängt an der Nachmessung; C11 ist offen.
7. **LU43** — Neue Organe sind gegen die Grundsätze 7–14 zu prüfen (v8 Z. 116); T4 prüft alle Organe zugleich.
8. **LU62** — Für T4 muss feststehen, wer das Modell wählt, das T4 erzeugt (P13).
9. **LU06** — Ob Mentor und Richtungswahl für Testwerke gelten, bestimmt die Laufgestalt von T4 (P9).
10. **LU49** — Die Kasse führt Läufe als „laeuft“/„bereit“ ohne Ende; das Tor-4-Skript rechnet Zeilen aus der Datenbank.
