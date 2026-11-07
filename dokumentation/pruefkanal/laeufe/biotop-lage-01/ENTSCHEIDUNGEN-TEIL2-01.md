# BIOTOP-LAGE-01 · Fassung 2 · `ENTSCHEIDUNGEN-TEIL2-01.md`

- **Inhalt:** FK15–FK19, FK21 · Entwurf A, Stück 2 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil A, Arbeitszeit 25.09.2026 16:10:47–17:47:01 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/entscheidungen/ENTSCHEIDUNGEN-TEIL2.md` · 26444 B · SHA-256 `423e0fb80dcec1e61d1830883fd29470c3af1cbded344a48ff2d4b23fd40e8b6`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (4 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# ENTSCHEIDUNGEN — Teil 2 von 4: FK16, FK17

Stand des Lesens: 25.09.2026, 16:10–17:30 CEST. Quellen, Kennzeichnung und Absender wie im Kopf von Teil 1.
Die Kurzform „id n“ meint die Nachrichten-id in `arbeit/verlauf/v2/nachrichten.jsonl`. Den Wortlaut dazu gibt `arbeit/lesen/philipp-ab-2026-09-18.md`; die vier dort gekürzten Nachrichten 15154, 16482, 16769 und 16901 stehen ganz in R35.

---

## FK16 — Änderungen und Anweisungen nach v8, die in keiner Fassung stehen

**Bezug:** v8 ist am 23.09.2026 um 15:53:53 CEST eingegangen (FK15).

**Gegenstand:** Nach v8 hat Philipp 14 Nachrichten geschickt, 13 Texte und ein Dokument (*gerechnet*):
- Die Lesefassung hat ab Z. 439 17 Kopfzeilen.
- Davon abgezogen: id 13998 (das ist v8 selbst) sowie id 16285 und 16712 (nicht von Philipp).

**Prüfung am Wortlaut von v8:**
- Gelesen: v8 Z. 1–40, 96–137, 274–333 und 410–551.
- Kennzeichnende Wendungen gezählt mit `search_files` und R101 (Skript `a9_belegzaehlung.py`). „0“ heißt: Die Wendung steht nicht in v8.

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

**Weitere Punkte aus dem Teilauftrag:**
- **Zuschnitt der Behebungsrunden.** v8 kennt nur „die Behebungsrunde“ im Singular (Z. 476; „Behebungsrunde“ hat 1 Treffer, R101).
  - Tatsächlich gab es 6 Runden, jede durch eine eigene Nachricht beauftragt: Runde 1 = N-1, Runde 2 = N-3, Runde 3 = N-4, Runde 4 = N-6, Runde 5 = N-7, Runde 6 = N-9.
  - Zahl, Schnitt und Inhalt der Runden 2 bis 6 stehen in keiner Fassung.
  - Auslegung Hermes: Die Runden vollziehen v8 Z. 463–476 in sechs Schritten, erweitert um N-3 bis N-10.
- **Arbeitsregel „Weiterarbeiten ist der Normalfall“ (23.09. 08:25:31, id 12450).**
  - Sie kam **vor** v8 und fällt damit nicht unter FK16 im engen Sinn.
  - Sie steht aber in keiner Fassung: „Normalfall“, „harte Linie“ und „Formatsperre“ haben in v8 je 0 Treffer. → FK18.
- **Gegenprobe der Methode:** id 13912 (23.09. 15:03:47, kurz vor v8) verlangt den Median mehrerer Messungen und den Zwischenbericht „spätestens bei 120 von 150 Aufrufen“. Beides steht in v8 (Z. 464 und Z. 450), die Methode findet also Übernommenes.

---

## FK17 — Entscheidungsregister seit 18.09.

**Urheber, streng getrennt nach dem Wortlaut:**
- **P (Philipp):** Er entscheidet selbst, in erster Person, oder der Text sagt ausdrücklich „Philipp …“ oder „Entscheidung Philipps“. Viele dieser Texte hat Chat-Claude formuliert und Philipp geschickt; das steht beim Eintrag.
- **D (an Chat-Claude delegiert):** Philipp überträgt die Entscheidung ausdrücklich.
- **V (Vorentscheidung Chat-Claude):** Chat-Claude entscheidet, erkennbar an „Entscheidung(en) Chat-Claude“, „(Chat-Claude, Fassung 6)“ oder erster Person mit Bezug auf Chat-Claudes eigene Fehler. Philipp leitet nur weiter.
- **H (Entscheidung Hermes).**

**Bestätigung** einer V-Entscheidung gilt als belegt, wenn Philipp sie in eigenen Worten bestätigt oder wenn sie in einer Fassung steht, die Philipp übergeben hat. Diese zweite Form heißt hier „mittelbar“. Eine bloße Weiterleitung zählt nicht als Bestätigung.

**Das Register ist ein Auszug:**
- Aufgenommen sind alle Nachrichten Philipps mit Entscheidungs-, Freigabe- oder Regelmarke (Suche `search_files`: 21 Trefferzeilen) und die Stellen „delegiert“ und „Vorentscheidung“ in den Fassungen.
- Dazu die Abschnitte „Eigene Entscheidungen“ in 10 Berichten und in Arbeitsdateien von Runde 6 (R62). R61 fand Treffer in 48 Dateien; nicht jede ist einzeln aufgenommen → Lücke L-10.

### 17.1 Philipp (P)

| Nr | Datum (CEST), Quelle | Entscheidung (Wortlaut, gekürzt) | Beleg der Urheberschaft | Status |
|---|---|---|---|---|
| P-1 | 18.09. (Auftrag) | Maß „laut Masterprompt 3.5 harte Maße“ | nur im Datenbankprotokoll: `mass.eingefroren` mit „bestaetigt_von=Philipp (Auftrag 18.09.2026: Maß laut Masterprompt 3.5 harte Maße; Kernmaß-Formel Entscheidung Hermes)“ (R91 Z. 58). Die Nachricht selbst ist nicht einzeln geprüft | ersetzt durch v2 3.5 |
| P-2 | 19.09., Protokoll `mentor.gewaehlt` | „Vorgabe Philipp 19.09.2026: Vollmacht deckt die Richtungswahl“ | nur im Protokoll (R91 Z. 67 und 69). Die Nachricht ist **NICHT GEFUNDEN** (nicht gezielt gesucht) | gilt, aufgenommen in v5 §4 (v8 Z. 44 und 288) |
| P-3 | 18.–23.09., ids 629, 831, 997, 1393, 2232, 2718, 9105, 13998 | Übergabe der Fassungen v1 bis v8 | Kopf jeder Fassung: „Auftraggeber: Philipp Zöllisch · Prüfer: Chat-Claude“ (R30) | v8 gilt; v1 bis v7 sind ersetzt |
| P-4 | 20.09. 03:54:44, id 3053 | „Philipp hat Lauf 25 freigegeben: lagerhaus auf dem Lauf-13-Stand …, vier Generationen, C eingebaut, 0,80 € harte Grenze …“ | dritte Person. Auftragskopf: „Freigabe erteilt: 20.09.2026“ (`arbeit/dokumente/2026-09-20_031233_MASTERPROMPT_Lauf-25_Aufnahmesperre-C.md` Z. 3) | erledigt |
| P-5 | 20.09. 20:10:36, id 7732 | „Philipp hat den engen Folgeauftrag freigegeben — mit einer Verfahrensgrenze …: ein Reviewdurchgang, keine Fixagenten-Kaskade, kein Audit der Audits, kein Elternrepro …“ | dritte Person | gilt als stehende Regel (FK18) |
| P-6 | 21.09. 02:14:40, id 9106, und v7 | Breitentest statt Handelssystem. Die Testwerke baut Hermes selbst („Entscheidung Philipps“). v7: „Philipps Richtungsentscheidung vom 21.09.2026“ | Text von Chat-Claude („Vorentscheidung von mir“). Eine Äußerung Philipps in eigenen Worten ist im Verlauf **NICHT GEFUNDEN** → L-9 | gilt (v8 Z. 14 und 420) |
| P-7 | 21.09. 03:35:35, id 9696; gleicher Text 05:14:24, id 10252 | „Verfassung bestätigt mit drei Auflagen … danach ist der evolutionäre Lauf freigegeben, ohne weitere Rückfrage.“ (T3 `versandwerk`) | Die Bestätigung selbst ist in Chat-Claudes Stimme formuliert. `BESTAETIGUNG.md` Z. 3: „durch Philipp übermittelt“. Im Protokoll 13 × `verfassung.eingelegt` mit „von=Philipp“ (R91 Z. 115) | gilt (verfassung-02) |
| P-8 | 21.09. 13:50:51, id 10766 | „Ab sofort, als dauerhafte Regel in deinen REGELN: Eine abgelehnte oder abgelaufene Freigabe wird nie durch Umformulieren, einen anderen Befehl oder einen anderen Weg umgangen, sondern neu angefordert oder mit Meldung angehalten; Freigaberegeln setzt nur Philipp.“ | Text von Chat-Claude; die Regel gehört Philipp („setzt nur Philipp“) | aufgegangen in P-9, Linie 3. Frühere Ablage: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-01/MEMORY-Freigaberegel.md` Z. 7 (SHA-256 `2fc3b66b…`, R79) |
| P-9 | 23.09. 08:25:31, id 12450 | „Philipp gibt dir so viel Verantwortung wie möglich — Weiterarbeiten ist der Normalfall, Anhalten die Ausnahme. Diese Regel, von Philipp gesetzt, ersetzt deine eben verschärfte Zeile …“; drei harte Linien, Formatsperre | ausdrücklich „von Philipp gesetzt“ | gilt; Wortlaut und Ablage in FK18. Umfang von „ersetzt“ → W-3 |
| P-10 | 23.09. 19:42:19, id 14337 und 14340 | Träger „Claude Opus 5.5“, Denkstufe max als Grundwert | „von Philipp festgelegt“ bzw. „Philipp hat den Träger … gestellt“ | gilt (N-2) |
| P-11 | 24.09. 11:38:00, id 15962 | Einzelfreigabe „für genau diesen Fall …, nicht als Dauerregel“ | ausdrücklich | erledigt (N-5) |
| P-12 | 24.09. 11:49:51, id 15992 (6) | Die Einreichung des Fehlalarm-Texts „entscheidet Philipp“ | Vorbehalt Philipps | **offen**. Eine Entscheidung ist NICHT GEFUNDEN (FK21) |
| P-13 | 25.09. 00:27:35, id 17217 | „Philipp legt fest: Die Verdichtung der Sitzungen läuft künftig über OpenRouter …“ | nur bedingt eingeleitet (N-10) → W-4 | gilt, umgesetzt |
| P-14 | 25.09. 01:06:55, id 17359 | „(a) — ich gebe die Sicherung frei.“ | erste Person | erledigt |
| P-15 | 25.09. 14:44:22, id 20990 | Auftrag BIOTOP-LAGE-01 Fassung 2; „ersetzt Fassung 1“ | erste Person („schick mir“) | gilt |

### 17.2 An Chat-Claude delegiert (D)

- **D-1 Verfassung der Übungswerke.**
  - v8 Z. 161: „Für Übungswerke schreibt Chat-Claude die Verfassung; Philipp hat die Entscheidung delegiert.“
  - v8 Z. 522 (Anhang A `lagerhaus`): „Geschrieben von Chat-Claude (Philipp hat die Entscheidung delegiert). … Ändert nur Philipp.“
  - v8 Z. 538 (Anhang B `logmuehle`): „Entwurf Hermes, **von Chat-Claude bestätigt** (19.09.2026 …)“.
  - **Status:** gilt.
  - **Beleg der Delegation:** Sie steht nur im Text der Fassungen, seit v2 („3.3: Verfassung auch für Übungswerke“). Nach „delegier…“ gesucht in Philipps Nachrichten, v7, v8, ABNAHME und WIEDEREINSTIEG (R68 Abschnitt 3): nur v7 Z. 149 und 483 sowie v8 Z. 161 und 522. Eine Nachricht Philipps mit der Delegation ist **NICHT GEFUNDEN** → L-8.
- Eine weitere ausdrückliche Delegation ist nicht gefunden.
- „Philipp hat die Zahl der Testwerke offengelassen“ (v8 Z. 452) ist keine Delegation; siehe V-3.

### 17.3 Vorentscheidungen Chat-Claude (V)

Die Spalte „Bestätigt?“ folgt der Regel oben. **Fett** markiert sind Vorentscheidungen, die nie bestätigt wurden, aber wie eine Entscheidung geführt werden.

| Nr | Datum (CEST), Quelle | Vorentscheidung (Wortlaut, gekürzt) | Bestätigt von Philipp? (Beleg) | Status |
|---|---|---|---|---|
| **V-1** | v1 bis v6; id 9017 (21.09. 01:19:00), id 9072 (01:56:17) | Handelssystem als Werk für Phase 4. v6 Z. 390: „**Freigaben ausschließlich durch Philipp** … dessen Verfassung Philipp schreibt“. id 9072: „Vorbedingung 2, die Verfassung des Handelssystems, die Philipp schreibt“ | **Nein.** Änderungsverzeichnis v7: „war aber eine nie bestätigte Vorentscheidung von Chat-Claude … **Fehler von Chat-Claude:** eine Vorentscheidung sechs Fassungen lang wie eine Entscheidung geführt.“ | zurückgezogen am 21.09. um 02:14 (v7); ersetzt durch P-6 |
| **V-2** | seit v3 §10 (Änderungsverzeichnis v3, letzte Zeile; v8 Z. 69) | „Hermes prüft vor Phase 2 den OpenRouter-Katalog auf aktuellere Schnellmodelle … (Vorentscheidung Chat-Claude …)“ | **Nein**, NICHT GEFUNDEN. Steht unverändert bis v8 | steht in jeder Fassung ab v3; ob umgesetzt, ist nicht geprüft |
| **V-3** | v7 und v8 Z. 452 | „Abnahme des Breitentests — die Sättigungsregel (Entscheidung Chat-Claude, 21.09.2026): Philipp hat die Zahl der Testwerke offengelassen. … Der Breitentest ist abgeschlossen, wenn zwei aufeinanderfolgende Testwerke neuer Art durchlaufen, ohne einen neuen Messgerätfehler zu erzeugen.“ | **Nur mittelbar** (v7 und v8 übergeben). id 9106 leitet weiter: „Abnahme nach der Sättigungsregel in Abschnitt 8“. Eine Delegation ist nicht belegt | gilt als Abnahmeregel |
| V-4 | v8 Z. 9; id 14000 | „vier offene Messfragen von Chat-Claude entschieden (gepaarte Laufzeit statt Minimum, Gedächtnissperre nur bei berührtem Bereich, Schwarm und Ankläger lesen geeicht, Korpus aus den Verträgen mit Randfällen)“ | mittelbar (v8) | gilt |
| **V-5** | 21.09. 12:05:50, id 10669 | „drei Vorentscheidungen von Chat-Claude. Erstens einchecken … künftig ist jede Abnahme und jeder eingefrorene Kern ein eigener Commit. Zweitens den offenen Ausfall aus Lauf 30 mit dem Höchstfall klären. Drittens Wiederholung ja … nur bei Fehlern, die der Anbieter ausdrücklich als wiederholbar kennzeichnet …“; Startsperre bei fehlenden Budgetvariablen | **Nein.** Selbst als Vorentscheidung bezeichnet; eine Bestätigung ist NICHT GEFUNDEN. id 10720 setzt sie voraus | umgesetzt. „Eigener Commit“ wird als stehende Regel geführt (Skill measurement-harness-discipline Z. 51; jeder Auftrag vor T4 enthält „eigener Commit“) |
| V-6 | 19.09. 21:46–22:56, ids 2356, 2380, 2398, 2424, 2564 | Präzisierungen „(Chat-Claude, Fassung 6)“: Eichgegenstand auf dem tragenden Pfad; Wortstatistik nur für Übungswerke; Proben in keines der Gedächtnisse; Merkmal `ist_probe`; „der Ankläger geändert, nicht die Grenze“ | mittelbar (v6, übergeben 20.09. 00:18:44) | gilt (Änderungsverzeichnis v6) |
| V-7 | 22.09. 14:52:53, id 11301; 15:15:11, id 11434; 15:32:32, id 11505 | „Wertung Chat-Claude: nicht abgenommen“; „Entscheidung Chat-Claude: Lauf 38 noch nicht …“; „Skills vor T5: … Zweigvergleich … jede Enthaltung zählen, null Fälle sind keine Mehrheit“ | nein, nur weitergeleitet | erledigt. Die Skills sind geändert (`measurement-harness-discipline/references/defect-class-sweep.md` Z. 36; `SKILL.md` Z. 65) |
| V-8 | 23.09. 05:41:59, id 11575 | „Kein weiterer Lauf an T3, die Grenze war hart.“ („der Fehler ist auch meiner“) | nein | erledigt (abschluss-03) |
| V-9 | 23.09. 15:03:47, id 13912 | „Zwei Entscheidungen von Chat-Claude …: Sperre 3: nicht auflösen … Laufzeit-Grenzmaß: … Median mehrerer Messungen je Seite …“; „Dauerhaft: Zwischenbericht … spätestens bei 120 von 150 Aufrufen“ | mittelbar (v8 Z. 450 und 464) | gilt |
| V-10 | 23.09. 22:32:40, id 14624 | Entscheidungen (1) bis (5), N-3 | nein, nur weitergeleitet | umgesetzt; (4) ersetzt durch V-11 (1) |
| V-11 | 24.09. 02:14:45, id 15154 | Entscheidungen (1) bis (4), N-4 | nein | umgesetzt |
| V-12 | 24.09. 11:49:51, id 15992 | Entscheidungen (1) bis (6), N-6 | nein | umgesetzt; (6) offen (P-12) |
| V-13 | 24.09. 16:48:07, id 16482 | Entscheidungen (1) bis (8), N-7 | nein | umgesetzt; Teil von (6) zurückgezogen (V-14), ersetzt durch V-15 (4) |
| V-14 | 24.09. 21:00:41, id 16769 | N-8, ohne Marke, in Chat-Claudes Stimme („mein Auftrag … war ein Fehler“) | nein | übernommen als R6-1 bis R6-3. Hermes führt es als „(Philipp, 24.09.)“ → W-5 |
| **V-15** | 24.09. 23:15:27, id 16901 | Wahl des Reviews („Es gilt das zweite Review“), Review je eigener Ordner, Runde 6 (1) bis (8) und die **Startregel für T4, „vorab gesetzt“** (Wortlaut in N-9) | **Nein**, nur weitergeleitet. id 17217 bestätigt die Review-Wahl in derselben Stimme: „mein Grund für die Wahl des zweiten war falsch, die Wahl bleibt“ | Runde 6 in Arbeit. Hermes wendet die Startregel als Maßstab an (`BAU-S1B-M2B.md` Z. 29–32) |
| V-16 | 25.09. 00:27:35, id 17217 Z. 1 | U-1 bis U-4 nach der Startregel einordnen | nein. Hermes führt es als „Auftrag (Philipp, 25.09.)“ (`EINORDNUNG-U1-U4.md` Z. 3) → W-5 | erledigt |
| **V-17** | 20.09. 02:46:30 (PRUEFUNG4) und 04:50:16 (ABNAHME) | Sammlung „Änderungsverzeichnis für Fassung 7“ mit 24 Punkten in A bis E (`arbeit/dokumente/2026-09-20_045016_ABNAHME_Vorbedingung-1_2026-09-20.md` Z. 115–156; dort Z. 117: „Gib mir Fassung 6, und ich schreibe Fassung 7 aus.“). Darin V12, „Keine Datei wird überschrieben — nummerierte Dateinamen“ (PRUEFUNG4 Z. 35: „V12 — die Behebung, meine Entscheidung“; Z. 140) | **Nein.** Eine Bestätigung in Philipps eigenen Worten ist NICHT GEFUNDEN. Nicht in v7 übernommen (Änderungsverzeichnis v7, FK15). Trotzdem als Regeln geführt: `REGELN-01.md` Z. 5–33, „vom Auftraggeber mitgeteilt“ (Z. 2); Auftraggeber ist dort Chat-Claude (Z. 36) → W-9 | wird befolgt (FK18); 9 der 24 Punkte stehen nirgends als Regel → L-5 |

### 17.4 Entscheidungen Hermes (H)

**Anzahl** der Punkte in den Abschnitten „Eigene Entscheidungen“ (R62):

| Bericht | Punkte |
|---|---|
| Phase 1 | 7 |
| Phase-1-Nachlauf | 7 |
| Phase 2 | 8 |
| Vorbedingung 1, `nach-reparatur-02/abschluss-01/MESSPLAN.md` | 4 |
| T3 abschluss-03 | 7 |
| vor-t4 | 9 |
| vor-t4-02 | 7 |
| vor-t4-03 | 9 |
| vor-t4-04 | 7 |
| vor-t4-05 | 11 |
| **Summe** | **76** (*gerechnet*) |

Dazu kommen 2 Punkte in `/root/biotop-vor-t4-06/VERDICHTUNG-OPENROUTER.md` und Einzelstellen aus Runde 6. Die Berichte zu Phase 3, zum Phase-3-Nachlauf und zu T3 abschluss-01 und -02 sind in R62 nicht erfasst → L-10.

**Einzeln aufgeführt** sind nur Entscheidungen mit Folgen für Status, Freigabe oder Regeln:

| Nr | Datum, Quelle | Entscheidung Hermes (Wortlaut, gekürzt) | Status |
|---|---|---|---|
| **H-1** | 18.09., `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/BERICHT.md` §4 Nr. 2; Protokoll | Kernmaß-Formel und Toleranzen, „Philipp soll das Maß bestätigen oder ändern“. Im Protokoll eingefroren als „Vorschlag Hermes 18.09.2026 (Bestätigung Philipp offen; Toleranz groesste_funktion 25 %)“ (R91 Z. 59) | **Nie bestätigt, als eingefrorenes Maß geführt**; ersetzt durch v2 und v3 (Kernmaß-Formel 3.5; größte Funktion absolut) |
| H-2 | 18.09., Phase 1 §4 Nr. 4 | Freigaben im Hauptlauf „stellvertretend erteilt (3 Generationen …), weil Philipp nicht am Terminal war“ | vor der Vollmacht (v2, 19.09. 00:36:30); eine nachträgliche Bestätigung ist NICHT GEFUNDEN (FK19) |
| H-3 | 19.09., Nachlauf §7 Nr. 1–2 | Pareto je Test; ins Werk nur bestandene Immuntests („Vorschlag für Fassung 3“) | übernommen in v3 (Änderungsverzeichnis v3) |
| H-4 | 19.09., Phase 2 §6 Nr. 3 | „Zwei Biotop-Fehler während Lauf 13 korrigiert, ohne Maßwirkung“ | zurückgewiesen durch v4 („ohne Ermessen darüber, ob sie „Maßwirkung" hat …“) |
| H-5 | 19.09., Phase 2 §6 Nr. 6 | Vertragstests (17) „von Hermes … abgeleitet — Philipp/Chat-Claude bestätigen sie bei Vorlage“ | eine Bestätigung ist NICHT GEFUNDEN; UNBEKANNT |
| H-6 | 21.09., `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-02/ZWISCHENBERICHT.md` Z. 5 und 8 | „Entscheidung Hermes: exakte Zwischenrechnung; Half-up auf ganze Cent genau einmal am Endpreis …“; „Der engere Sicherheitstausch in Satz 6 ist die bestätigte Entscheidung von Hermes“ | gilt (verfassung-02) |
| H-7 | 23.09., T3 abschluss-03 §Eigene Entscheidungen Nr. 7 | „Wächter-Schwellen 110/140 statt 120, wegen des Minutentakts.“ | gilt (MEMORY.md Z. 7) |
| H-8 | T3 `abschluss-03/SPERREN.md` Z. 13 | eigene Ausnahme in den Notizen: „nicht regelkonform (Freigaberegeln setzt nur Philipp)“ | zurückgezogen |
| H-9 | 23.09., vor-t4 §10 Nr. 1 und 9 | `model.default` in `config.yaml` gesetzt; die Laufzeitgrenze außerhalb des Wirkungskreises ist „eine Frage an Philipp“ | gilt; die Frage hat Chat-Claude beantwortet (id 14624 (3)) |
| H-10 | 24.09., vor-t4-05 §13 Nr. 1 | „Enthaltung des ganzen Urteils bei unvollständiger Erfassung“ | zurückgezogen („Diese Entscheidung war falsch“); ersetzt durch R6-1 |
| H-11 | 24.09., vor-t4-05 §13 Nr. 9 und 11 | Stufe-2-Last `eingang` mit 240 Wiederholungen; das Tor-4-Skript berechnet nur „Schwächen“ | ersetzt durch V-15 (4) und (5) |
| H-12 | 25.09., `/root/biotop-vor-t4-06/UEBERGABE.md` Z. 178; `BAU-S1B-M2B.md` Z. 29 | „Eigene Entscheidung: M2(b) in diese Runde“ (nach der Startregel); „Meine Engführung im Auftrag S1 … war der Fehler“ | gilt, Bau in Arbeit |
| H-13 | 25.09., UEBERGABE.md Z. 164; `sperre/SPERRE-02-S3-gateway-waechter.md` Z. 37 | `VORHER-NACHHER-S3` gestrichen: „auf dem umgangenen Weg entstanden … gelten nicht als Beleg“ | gilt |
| H-14 | 25.09., `BAU-S4-VERDRAHTUNG.md` Z. 134 | Weicht der Kernstand zwischen Eichphase und Vorspann ab, „**verweigert** der Vorspann“ | gilt, Bau in Arbeit |
| H-15 | 25.09., `S1-ABBRUCH.md` Z. 41; `sperre/SPERRE-04-S1b-formatsperre.md` Z. 16 | S1 wird als Fortsetzung neu gestartet; das gespeicherte Skript läuft nach der Formatsperre unverändert (Regel vom 23.09.) | gilt |
| H-16 | 25.09., VERDICHTUNG-OPENROUTER.md Z. 50–58 | Modell `google/gemini-3.6-flash` für die Verdichtung; „Gilt profilweit“ | gilt |
| H-17 | 23.09., MEMORY.md Z. 5 | Übertragung der Arbeitsregel mit dem Zusatz „ersetzt alle früheren Anhalte-/Freigaberegeln“ | → W-3 |
