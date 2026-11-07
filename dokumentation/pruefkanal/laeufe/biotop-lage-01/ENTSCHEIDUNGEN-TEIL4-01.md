# BIOTOP-LAGE-01 · Fassung 2 · `ENTSCHEIDUNGEN-TEIL4-01.md`

- **Inhalt:** FK15–FK19, FK21 · Entwurf A, Stück 4 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil A, Arbeitszeit 25.09.2026 16:10:47–17:47:01 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/entscheidungen/ENTSCHEIDUNGEN-TEIL4.md` · 19014 B · SHA-256 `64b5b020196b699453fcf9d98160cc8d2ccdf04779bec4f4307b4560f0b023c8`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (3 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# ENTSCHEIDUNGEN — Teil 4 von 4: FK19, FK21, Lücken, Widersprüche

Stand des Lesens: 25.09.2026, 16:10–17:30 CEST. Quellen, Kennzeichnung und Absender wie im Kopf von Teil 1. Die Nummern P-, V-, H-, A-, N- verweisen auf Teil 2 und Teil 3.

---

## FK19 — Freigaben

**Frage:** Wer gibt was frei, bei Übungswerken, bei Testwerken des Breitentests und bei echten Werken? Wortlaut der gültigen Stelle.

### 19.1 Wortlaut der gültigen Fassung v8

**§4 „Ablauf eines Laufs“, v8 Z. 280–283:**

> 5. **Maß** → Vorschlag, Philipp bestätigt, eingefroren.
> 6. **Mentor** → Richtungen, Philipp wählt.
> …
> 8. **Freigabe** → Philipp gibt frei oder lehnt ab; Ablehnung mit Grund → Immunisierung + Geschmacksgedächtnis.

**§4, v8 Z. 287–288:**

> Philipp gibt jede Generation frei. Vollautomatik über mehrere Generationen kommt erst, wenn das Messgerät über mindestens drei Werke ohne einen einzigen unbemerkten Rückschritt gearbeitet hat — und dann nur auf Philipps Satz.
> **Vollmacht für Übungswerke (Fassung 2, erweitert in Fassung 5):** Für Werke ohne Betriebszweck, die Hermes selbst erzeugt hat, gilt eine schriftliche Vollmacht: Hermes gibt Generationen frei **und wählt die Richtung des Mentors**, protokolliert je Entscheidung die Begründung (`freigabe.frei`, `mentor.gewaehlt`, Vollmacht als Grund genannt), und Chat-Claude prüft alles am Abschlussordner. Für jedes Werk mit Betriebszweck gibt ausschließlich Philipp frei und wählt die Richtung; eine stellvertretende Freigabe dort ist ein Verstoß, kein Ermessen.

**§8 Phase 4 „Herkunft der Werke“, v8 Z. 420:**

> **Herkunft der Werke:** Hermes baut alle Testwerke selbst (Entscheidung Philipps, 21.09.2026), mit versiegelten Schwächen wie bei `lagerhaus` und `logmuehle`. Ausnahme in T4, siehe dort.

**§8 T4, v8 Z. 426, Auszug:** „Hermes erzeugt es über ein anderes Modell als sein eigenes, damit Stil und Struktur nicht seine sind.“

**§8 Phase 5, Vorbedingung 4, v8 Z. 491:**

> 4. **Freigaben ausschließlich durch Philipp**; die Vollmacht für Übungswerke gilt hier nicht. Hier beginnt das echte Geschmacksgedächtnis.

**§10, v8 Z. 516:** „Die Verfassung jedes Werks und das Maß jedes Laufs — bei Vorlage.“

**Außerhalb des Masterprompts**, `REGELN-01.md` Z. 36 (20.09.): „**Philipp entscheidet und gibt ab Phase 4 allein frei.**“ → W-7.

**Übersicht nach dem Wortlaut:**

| Werkart | Wer gibt Generationen frei | Wer wählt die Richtung | Stelle |
|---|---|---|---|
| Übungswerke (`lagerhaus`, `logmuehle`; ohne Betriebszweck, von Hermes erzeugt) | Hermes unter Vollmacht, protokolliert; Chat-Claude prüft am Abschlussordner | Hermes unter Vollmacht | Z. 288 Satz 1 |
| Testwerke des Breitentests (T3–T6) | keine eigene Stelle; siehe WS17 in 19.3 | wie Freigabe | Z. 288, 420, 426 |
| Werke mit Betriebszweck | ausschließlich Philipp; eine stellvertretende Freigabe ist ein Verstoß | Philipp | Z. 288 Satz 2 |
| echte Werke (Phase 5) | ausschließlich Philipp; die Vollmacht gilt nicht | Philipp | Z. 491 |

### 19.2 Tatsächliche Freigaben

- **Quelle:** Datenbankzweige, nur lesend (R59 und R91, beide 25.09. 16:18–16:40 CEST). STAMM wurde mit `immutable=1` geöffnet, bei 0 Bytes WAL-Datei.
- **Zeiten:** in der Datenbank UTC, hier in CEST umgerechnet (+2 h, *gerechnet*).

| Zweig | Generationen gesamt | davon mit Freigabe | Protokoll `freigabe.frei` | durch Hermes | durch Philipp |
|---|---|---|---|---|---|
| STAMM | 144 | 48 | 48 | 48 von 48 | 0 von 48 |
| VB1 | 150 | 50 | 50 | 50 von 50 | 0 von 50 |
| R02 | 144 | 48 | 48 | 48 von 48 | 0 von 48 |
| T3 | 184 | 66 | 66 | 66 von 66 | 0 von 66 |

**Die 48 Freigaben im STAMM** (je Zeile laut R59 Z. 81–100; Summe *gerechnet*):

| Art (Grund bis zum ersten Doppelpunkt) | Anzahl | Läufe | Zeitraum (CEST) | Galt eine Vollmacht? |
|---|---|---|---|---|
| „Hermes (stellvertretend, Übungswerk Phase 1 — eigene Entscheidung, im Bericht gekennzeichnet)“ und „Hermes (stellvertretend, eigene Entscheidung)“ | 1 + 2 = 3 | 2 | 18.09. 23:50:16–23:58:38 | nein: v2 mit der Vollmacht kam am 19.09. um 00:36:30 |
| „Hermes (Kassenprobe)“ | 2 + 2 = 4 | 4, 5 | 19.09. 00:07:20–00:16:27 | nein, ebenfalls vor v2 |
| „Hermes unter Vollmacht Abschnitt 4 F2 …“ | 6 + 3 + 3 + 4 + 1 = 17 | 6–10 | 19.09. 00:54:37–02:12:40 | ja |
| „Hermes unter Vollmacht Abschnitt 4 (Masterprompt v3 …)“ | 4 + 7 = 11 | 12, 13 | 19.09. 02:54:33–05:16:51 | ja |
| „Hermes (Vollmacht Abschnitt 4, Übungswerk)“ und „… (Masterprompt v4 …)“ | 1 + 12 = 13 | 16–25 | 19.09. 13:31:37 – 20.09. 03:35:50 | ja |
| **Summe** | **48** | | | 41 von 48 unter Vollmacht |

**Die übrigen Zweige:**
- **VB1** enthält die 48 aus STAMM und zusätzlich 2 Freigaben „Hermes unter Übungswerk-Vollmacht“ in Lauf 26 (`lagerhaus-vorbedingung1-26`), 20.09. 21:45:15–21:59:11 CEST.
- **T3** enthält die 48 aus STAMM und zusätzlich 18 Freigaben „Hermes“ an `versandwerk-t3-02`, Läufe 32–38, 21.09. 17:37:46 – 22.09. 21:16:34 CEST.
  - Grund, 18-mal wortgleich (R31 Z. 483): „Hermes: Uebungswerk ohne Betriebszweck; Freigabe unter dokumentierter Vollmacht Abschnitt 4 F2, Verfassung regeln.uebungswerk=true. Messung entscheidet, kein Modellurteil.“
  - Protokoll dazu: 18 × „von=Hermes ; vollmacht=Vollmacht Abschnitt 4 F2 (Übungswerk ohne Betriebszweck, Verfassung regeln.uebungswerk=true)“ (R91 Z. 124).
- **Spalte `laeufe.freigabe`:** leer in allen Zweigen für die Läufe 20–38 (R79 §3). Freigaben stehen nur je Generation.

**Weitere Urheberangaben im Protokoll** (R91):
- **Richtung (`mentor.gewaehlt`):** 11 Einträge im STAMM, alle „von=Hermes (Vollmacht Abschnitt 4 …)“; im VB1 12, im T3 11.
  - Für die T3-Läufe 26–38 gibt es damit 0 Einträge (*gerechnet*: T3 11 − STAMM 11). Ob in T3 eine Richtung gewählt wurde: UNBEKANNT → L-7.
- **Verfassung (`verfassung.eingelegt`):** Im T3 steht 13 × „von=Philipp“ mit der Quelle `/root/biotop-t3/VERFASSUNG-T3-02.md` (R91 Z. 115).

### 19.3 Abgleich mit dem Wortlaut (Auslegung Hermes)

1. **Übungswerke, Läufe 6–26, 43 Freigaben** (41 im STAMM und 2 in Lauf 26, *gerechnet*).
   - Sie decken sich mit Z. 288 und liegen alle nach dem Eingang von v2.
   - Der Grund nennt bis Lauf 25 „Masterprompt v4“, auch nach dem Eingang von v5 und v6. Der Wortlaut der Vollmacht zur Freigabe ist seit v2 unverändert; v5 hat nur die Richtungswahl ergänzt. Deshalb ohne Folge.
2. **Läufe 2, 4 und 5, 7 Freigaben vor der Vollmacht.**
   - Damals galt v1 §4 Z. 155: „**Freigabe** → Philipp gibt frei oder lehnt ab“. Eine Vollmacht gab es nicht.
   - Hermes hat die 3 Freigaben in Lauf 2 als eigene Entscheidung gekennzeichnet (Phase-1-Bericht §4 Nr. 4, H-2). Eine nachträgliche Bestätigung durch Philipp ist NICHT GEFUNDEN → L-6.
   - Die Kassenproben in Lauf 4 und 5 sind nicht als Ausnahme begründet → L-6.
3. **T3 `versandwerk`, 18 Freigaben.** Beide Bedingungen von Z. 288 (v7 Z. 276 wortgleich) sind erfüllt:
   - Ohne Betriebszweck: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-02/VERFASSUNG-T3.md` Z. 5, „`versandwerk` ist ein TypeScript-Übungswerk ohne Betriebszweck“.
   - Von Hermes erzeugt: P-6, v8 Z. 420.
   - Satz 8 derselben Verfassung (Z. 12) nennt die Vollmacht ausdrücklich: „Die Übungswerk-Vollmacht gilt für dokumentierte Generationenfreigaben und Mentorwahl; sie ersetzt keine Bestätigung dieser Verfassung.“ Diese Verfassung ist bestätigt (P-7).
   - Die Freigaben passen damit zu v7 und v8, **nicht aber zu `REGELN-01.md` Z. 36** („gibt ab Phase 4 allein frei“; T3 gehört zu Phase 4) → W-7.
   - Z. 36 stammt vom 20.09. Damals war Phase 4 noch das Handelssystem (V-1; v6 Z. 390 „Freigaben ausschließlich durch Philipp“). Mit v7 wurde das zurückgezogen, REGELN-01 aber nicht nachgeführt (L-3).
4. **Echte Werke, Phase 5:** Bisher gibt es keins, also keine Freigabe. Ein Verstoß gegen Z. 491 ist nicht möglich.
5. **Werke mit Betriebszweck:** keins im Biotop (Werke → `LAGE`, FK25). 0 stellvertretende Freigaben dort.

**Antwort auf Chat-Claudes Frage WS17** („gilt das auch für die Testwerke des Breitentests?“):
- **Wortlaut:** v8 hat keinen Satz, der die Testwerke in der Freigaberegel nennt. Maßgeblich sind die Bedingungen der Vollmacht in Z. 288: „Für Werke ohne Betriebszweck, die Hermes selbst erzeugt hat …“. Dazu Z. 420: „Hermes baut alle Testwerke selbst (Entscheidung Philipps, 21.09.2026) … Ausnahme in T4, siehe dort.“ Dazu Z. 491: Nur für das erste echte Werk „gilt [die Vollmacht] hier nicht“.
- **Auslegung Hermes:**
  - **Ja** für jedes Testwerk ohne Betriebszweck, das Hermes selbst gebaut hat. Belegt und angewandt an T3: 18 von 18 Freigaben unter Vollmacht, Verfassung Satz 8 bestätigt. Nach dem Plan in v8 Z. 424–430 gilt dasselbe für T5 und T6.
  - **Offen für T4:** Hermes „erzeugt es über ein anderes Modell als sein eigenes“ (Z. 426), und Z. 420 nennt T4 eine Ausnahme bei der Herkunft. Ob T4 noch „von Hermes selbst erzeugt“ ist, entscheidet der Wortlaut nicht.
  - **Gegenstimme:** REGELN-01 Z. 36.
  - **Weg zur Klärung:** Philipp entscheidet vor T4 in einem Satz; das gehört in die nächste Fassung.

---

## FK21 — Fristen und Zusagen zum Biotop

**Suche:**
- **Wo und wonach:** Philipps Nachrichten und Hermes' Meldungen (`arbeit/lesen/hermes-an-philipp.md`), mit den Mustern „Frist“, „spätestens“, „morgen“, „heute Abend/Nacht/noch“, „zusag“, „Zusage“, „verspreche“, „vor T3–T6“, „nach T3–T6“, „bis zum/zur/morgen/heute/<Uhrzeit>/<Datum>/Ende“ (R68 §2, lief am 25.09. um 16:23 CEST vor dem Hinweis zu SPERRE-01). Dazu die Fassungen v1–v8 per `search_files`, Muster „Frist|spätestens|bis zum“.
- **Trefferzeilen:** 22 in `philipp-ab-2026-09-18.md`. Davon stammen 2 aus Reviewaufträgen von Hermes (ids 16285 und 16712), bleiben also 20 von Philipp (*gerechnet*). In `hermes-an-philipp.md` 24 Trefferzeilen.
- **Ergebnis: Eine Frist mit Kalenderdatum oder Uhrzeit gibt es keine.** Weder Philipp noch Chat-Claude noch Hermes hat ein Biotop-Ergebnis bis zu einem Datum zugesagt. Alle Fristen sind Reihenfolgebedingungen („vor T4“, „vor T5“, „nach T3“) oder Zusagen für den Einzelfall.
- **Nicht aufgenommen:** Treffer, die keine Frist sind, etwa Torzeilen wie „spätestens nach Generation 6“ (v8 Z. 403) oder „bis zum Abschluss durcharbeiten“ (id 10550).

| Nr | Was | Bis wann | Von wem | Quelle | Stand beim Lesen |
|---|---|---|---|---|---|
| F-1 | Vorbedingungen für T4 (v8 Z. 463–476) einschließlich der roten Spezifikationen R6-1 bis R6-4 | vor T4 | Hermes (Auftrag V-4, V-14, V-15) | v8 Z. 463; ids 14000, 16769, 16901 | offen; Runde 6 in Arbeit |
| F-2 | Start von T4 nach der Startregel | „sobald das Review dieser Runde keinen stillen Durchlass mehr findet“ | V-15 | id 16901 | offen |
| F-3 | Methoden in TypeScript; TypeScript-Proben zu den Entscheidungen 2 und 3 | vor T5 | V-12 (5), V-15 (8); Hermes am 24.09. 21:51:18 („5. TypeScript-Proben … erst vor T5 (T4 ist Python)“) und 25.09. 00:43:57 („U-3: … Gehört zu TypeScript, also vor T5“) | ids 15992, 16901; R68 §2 | offen |
| F-4 | „Skills vor T5“: Zweigvergleich in `defect-class-sweep.md`; „jede Enthaltung zählen, null Fälle sind keine Mehrheit“ | vor T5 | V-7 | id 11301 | beide Stellen vorhanden (`references/defect-class-sweep.md` Z. 36; `SKILL.md` Z. 65); wann geschrieben, ist nicht geprüft |
| F-5 | „Liste nach T3“: Erreichbarkeitsführung, Verfallsbedingung der Ausnahmeliste, `_beschleunigen` entfernen, Einzelwerte der Rauschmessung speichern | nach T3; v8 zieht sie vor T4 (Vorbedingung 11, Z. 474) | Chat-Claude; Hermes führt die Liste | ids 10669, 10903, 11135; v8 Z. 474 | offen, Teil von F-1 |
| F-6 | Zwischenbericht in den Prüfkanal | „spätestens bei 120 von 150 Aufrufen einer Sitzung“ | V-9 | id 13912; v8 Z. 450 | gilt; umgesetzt mit 110/140 (H-7) |
| F-7 | Freigabeabfragen bestätigen | „sofort, sobald sie erscheinen“ | Philipp | id 17359 | erledigt (VERDICHTUNG-OPENROUTER.md Z. 16) |
| F-8 | Einen gesperrten Einzelschritt „führt Philipp … von außen aus“ | im Sperrfall | Philipp | id 15962 | nicht eingetreten (id 15992) |
| F-9 | Braucht es einen Neustart des Gateways: „sag es Philipp in einem Satz, er startet ihn von außen“ | im Bedarfsfall | Philipp | id 14337 | UNBEKANNT, ob eingetreten. Weg: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/BERICHT.md` §1 lesen |
| F-10 | Ob der Fehlalarm-Text eingereicht wird | keine Frist | Philipp entscheidet | id 15992 (6) | offen (P-12) |
| F-11 | Frist für die Eingrenzung bei hängender Last. Hermes: „Ich habe S1 nachgesteuert, sie mitzubauen.“ | Runde 6 | Hermes | `hermes-an-philipp.md`, 25.09. 00:43:57 (R68 §2) | offen, Bau in Arbeit |
| F-12 | Offenlegung BIOTOP-LAGE-01: „sofort Meldung 1“, „zum Schluss, auch bei Abbruch, … Meldung 2“ | Stichzeitpunkt | Philipp an Hermes | id 20990 | offen |
| F-13 | Ende des Baus S1c, erwartet „25.09. zwischen etwa 16:15 und 18:25 CEST“ | 25.09.2026 | Erwartung Hermes, keine Zusage | `entwurf/REGELN-FUER-TEILE.md` Z. 40 | offen; `/tmp/biotop-kammer-exklusiv` bestand um 17:12 CEST nicht |

---

## Lücken (Vorschlag für die Lückenliste)

| Nr | Lücke | Beleg | Weg zur Schließung |
|---|---|---|---|
| L-1 | Von v8, der gültigen Fassung, gibt es außerhalb der Sitzungsdatenbank keine vollständige Kopie, nur den Tor-4-Auszug (48 von 49 Zeilen wörtlich) | R53 §4 | Kopie mit SHA-256 in `MASTERPROMPT-GUELTIG` (FK14) |
| L-2 | Für v1 bis v5 gibt es keine Plattenkopie im Prüfkanal; außerhalb nicht gesucht | FK15.3 | Suche über `/root` und `/tmp` nach Ende von S1c |
| L-3 | `REGELN-02` fehlt. V19 verlangt „`REGELN` nach neuer Masterprompt-Fassung“; seitdem kamen v7 und v8 | R55; REGELN-01 Z. 41 | Hermes schreibt REGELN-02 aus v8 und FK18 |
| L-4 | `STAND` fehlt nach jedem Auftrag seit dem 20.09. Es gibt nur STAND-01, danach kamen unter anderem T3 und die Runden vor T4 1 bis 5 | R55; REGELN-01 Z. 41 | STAND-02 |
| L-5 | 9 von 24 Punkten der Sammlung für Fassung 7 stehen nach Wendung weder in REGELN-01 noch in v7, v8 oder MEMORY.md (Nr. 1–4, 7, 8, 13, 23, 24) | R101 Teil 2 | Philipp oder Chat-Claude entscheiden, ob sie gelten; Aufnahme in die nächste Fassung |
| L-6 | 7 Freigaben vor der Vollmacht (Läufe 2, 4, 5); eine nachträgliche Bestätigung ist nicht gefunden | R59; FK19.3 | Nachricht vom 18./19.09. gezielt suchen |
| L-7 | `mentor.gewaehlt` für die T3-Läufe 26–38: 0 Einträge. Ob eine Richtung gewählt wurde, ist UNBEKANNT | R91 | T3-Protokoll nach `mentor.*` je Lauf abfragen |
| L-8 | Die Delegation der Verfassung für Übungswerke an Chat-Claude steht nur in den Fassungen; die Nachricht Philipps ist nicht gefunden | R68 §3 | Verlauf vor dem 19.09. 00:36 lesen (ab v2 belegt) |
| L-9 | Philipps Richtungsentscheidung vom 21.09. (Breitentest, Testwerke selbst bauen) ist nur als Wiedergabe Chat-Claudes belegt | id 9106; v7/v8 | Frage an Philipp, oder den Chat Philipps mit Chat-Claude beilegen |
| L-10 | Das Register der Entscheidungen Hermes ist ein Auszug: Treffer in 48 Dateien (R61), einzeln ausgewertet 10 Berichte und 7 Arbeitsdateien von Runde 6 (R62). Phase 3, Phase-3-Nachlauf sowie T3 abschluss-01 und -02 fehlen | R61, R62 | Auswertung der übrigen Dateien |
| L-11 | Die Nachricht mit der „Vorgabe Philipp 19.09.2026: Vollmacht deckt die Richtungswahl“ ist nicht gezielt gesucht | R91 Z. 67 | Suche in `arbeit/verlauf/v2/wortlaut.jsonl` |
| L-12 | Vorentscheidung V-2 (OpenRouter-Katalog prüfen): ob umgesetzt, ist nicht geprüft | v8 Z. 69 | Phase-2-Bericht lesen |
| L-13 | Nachgänge außerhalb von `biotop-phase-4-vorbedingung-1` sind nicht nach Regeln durchsucht | FK18.3 | Suche `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/*/NACHGANG*.md` |
| L-14 | Die Bestätigung der 17 Vertragstests aus Phase 2 durch Philipp oder Chat-Claude ist nicht gefunden (H-5) | Phase-2-Bericht §6 Nr. 6 | Suche im Verlauf vom 19.09. |

## Widersprüche zwischen Quellen

| Nr | Quelle A | Quelle B | Einordnung |
|---|---|---|---|
| W-1 | Lesefassung: v7 „86026 Bytes“ (Z. 368), v8 „95174 Bytes“ (Z. 440) | R15 und R17: 85.728 und 94.876 Bytes, SHA-256 geprüft | Unterschied je 298 Bytes (*gerechnet*). Es gelten R15 und R17. Ursache nicht geprüft; Auslegung Hermes: Hülle der Dokumentnachricht |
| W-2 | `REGELN-01.md` Z. 5: „Die vollständige Sammlung steht im Änderungsverzeichnis Fassung 7.“ | `aenderungen-v7.md`: 7 Zeilen, ohne die Sammlung. Die 24 Punkte stehen in ABNAHME §7 | offen (L-5) |
| W-3 | id 12450: „Diese Regel … ersetzt deine eben verschärfte Zeile“ | MEMORY.md Z. 5: „(23.09.2026, ersetzt alle früheren Anhalte-/Freigaberegeln)“ | Die Ablage ist weiter gefasst als der Wortlaut. Auslegung Hermes: Die Linien der Arbeitsregel enthalten A-3; eine Regel ist dadurch nicht entfallen. Der Zusatz sollte an den Wortlaut angepasst werden |
| W-4 | id 17217: „Wenn du dich für den Ersatzanbieter entscheidest, häng diesen Satz an: Philipp legt fest: …“ | `VERDICHTUNG-OPENROUTER.md` Z. 3: „Festlegung Philipp, wörtlich: …“, ohne die Bedingung | Der Vordersatz ist eine Anweisung Chat-Claudes an Philipp. Auslegung Hermes: Mit dem Absenden hat Philipp festgelegt |
| W-5 | Hermes führt Texte in Chat-Claudes Stimme als Philipps: vor-t4-05 BERICHT §13 Nr. 1 „(Philipp, 24.09.)“; `EINORDNUNG-U1-U4.md` Z. 3 „Auftrag (Philipp, 25.09.)“; T3-Protokoll 13 × `verfassung.eingelegt` „von=Philipp“ | Wortlaut der Nachrichten ids 16769 und 17217 („mein Auftrag … war ein Fehler“) und der Bestätigung P-7: Chat-Claude | Absender ist Philipp, Urheber des Wortlauts Chat-Claude. Maßgeblich ist die Trennung in FK17 |
| W-6 | v8 Z. 458: „Echt behoben: S1 (Ausführung von Eingabetext → eigener Parser)“ | id 14624 (23.09. 22:32, nach v8): „S1 ist an K2868 damit nicht sauber behoben, das korrigiert den T3-Befund“ | Die spätere Vorentscheidung steht in keiner Fassung (FK16 N-3) |
| W-7 | `REGELN-01.md` Z. 36: „Philipp … gibt ab Phase 4 allein frei.“ | v7 Z. 276 und v8 Z. 288 (Vollmacht); T3: 18 von 18 Freigaben durch Hermes in Phase 4 (R59) | REGELN-01 ist veraltet (L-3); FK19.3 Nr. 3 |
| W-8 | v1 Satz 2 und v8 Z. 280: „Maß → Vorschlag, Philipp bestätigt, eingefroren“ | STAMM-Protokoll `mass.eingefroren`: „Vorschlag Hermes 18.09.2026 (Bestätigung Philipp offen …)“ (R91 Z. 59) | Historisch, Lauf 2. Ersetzt durch v2 und v3 (H-1) |
| W-9 | Kopf jeder Fassung: „Auftraggeber: Philipp Zöllisch · Prüfer: Chat-Claude“ (R30) | `REGELN-01.md` Z. 36: „Chat-Claude ist Auftraggeber, Prüfer und Korrektiv.“ | Die Rollen sind verschieden benannt; die Herkunft der REGELN-01 („vom Auftraggeber mitgeteilt“) bleibt damit unklar |
| W-10 | `entwurf/REGELN-FUER-TEILE.md` Z. 57: „120 Nachrichten Philipps“ | `arbeit/verlauf/v2/nachrichten.jsonl`: 114 (Berichtigung Hermes, R84, R85, R88, R89) | Aufgelöst: Es gilt 114 |
