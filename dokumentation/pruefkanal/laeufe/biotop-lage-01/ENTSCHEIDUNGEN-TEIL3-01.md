# BIOTOP-LAGE-01 · Fassung 2 · `ENTSCHEIDUNGEN-TEIL3-01.md`

- **Inhalt:** FK15–FK19, FK21 · Entwurf A, Stück 3 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil A, Arbeitszeit 25.09.2026 16:10:47–17:47:01 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/entscheidungen/ENTSCHEIDUNGEN-TEIL3.md` · 20829 B · SHA-256 `2b89504a37c6fde2e08848634a0015398b484403b2ce6281d43caff885ca2f4a`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (9 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# ENTSCHEIDUNGEN — Teil 3 von 4: FK18 (stehende Arbeitsregeln außerhalb des Masterprompts)

Stand des Lesens: 25.09.2026, 16:10–17:30 CEST. Quellen, Kennzeichnung und Absender wie im Kopf von Teil 1. Die Nummern P-, V-, H-, W- und L- verweisen auf Teil 2 und Teil 4.

**Frage:** Welche Arbeitsregeln stehen außerhalb des Masterprompts, etwa aus `REGELN-nn.md`, aus Nachgängen oder aus Anweisungen? Je mit Quelle.

**Prüfung, ob eine Regel außerhalb liegt:**
- Die kennzeichnenden Wendungen jeder Regel sind in v7 und v8 gezählt (R101, Skript `a9_belegzaehlung.py`). „0“ heißt: Die Wendung steht in keiner der beiden Fassungen.
- Eine Suche nach Wendungen findet keine Umschreibungen. Auslegung Hermes: 0 heißt „nicht wörtlich übernommen“.

## 18.1 Quellen

| Quelle | Pfad | Änderungszeit (CEST) | Bytes | SHA-256 (R79 Z. 82–99) |
|---|---|---|---|---|
| Regeln im Gedächtnisordner | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/REGELN-01.md` | 20.09.2026 05:17:33 | 4.504 | `7de0078ce031bf2d34da73352a8be8cdf7a51cc3f017f750acc4acde9dba27b6` |
| Gedächtnis Hermes | `/root/.hermes/memories/MEMORY.md` | 23.09.2026 21:46:55 | 2.224 | `dddff83375bad37fd6cdf71b8d238d1de02a679bc8cb0f28a96bb02ef2ba2d67` |
| Nutzerprofil Hermes | `/root/.hermes/memories/USER.md` | 20.09.2026 21:15:41 | 1.289 | `fcff371c28e7f06406d20bf337f2e76b039a181125e9e00c019d1db9a05731aa` |
| Freigaberegel, Ablage aus T3 | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-01/MEMORY-Freigaberegel.md` | 21.09.2026 18:53:33 | 1.956 | `2fc3b66b3b29757a4d23f44ab45ac57f98daf615a407d58d41ced6ce0b456856` |
| Nachgänge zu Vorbedingung 1 | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG.md`, `NACHGANG-03.md`, `NACHGANG-04.md` | nicht erhoben | nicht erhoben | nicht erhoben |
| Anweisungen Philipps | `arbeit/lesen/philipp-ab-2026-09-18.md` (Zeile je id) | — | — | — |
| 4 Skills | siehe 18.6 | | | |

- **Nur Nummer 01 im Gedächtnisordner.** `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/` enthält REGELN-01, STAND-01, UNTERBAU-01 und Manifeste: 5 Dateien, alle vom 20.09.2026 05:17:33 CEST (R55).
- REGELN-01 Z. 41 (V19) verlangt „`REGELN` nach neuer Masterprompt-Fassung“. Seitdem kamen v7 (21.09.) und v8 (23.09.). Ein `REGELN-02.md` gibt es nicht → L-3.

## 18.2 REGELN-01 im Wortlaut

- Die Adresse in der letzten Zeile ist auf `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` umgestellt; sonst ist der Text unverändert.
- Der Text wurde per Skript eingesetzt und gegengeprüft (R146: 41 von 41 nichtleeren Zeilen).

> # Regeln — Fassung 01 · 2026-09-20T03:17:33.347176+00:00
> Herkunft: Abschnitt 5 des Wiedereinstiegsbriefs, ergänzt um die vom Auftraggeber mitgeteilten Entscheidungen. Kein von Hermes erfundener Masterprompt v7.
> Nur HERMES-1 schreibt; HERMES-2/HERMES-3 lesen.
>
> Kurzfassung. Die vollständige Sammlung steht im Änderungsverzeichnis Fassung 7.
>
> **Belege**
> - Keine Zahl aus dem Gedächtnis. Jede Zahl aus einer Protokollabfrage, die Abfrage beigelegt.
> - Jede Zahl nennt ihre Menge im Satz daneben — was genau gezählt wurde, mit Nenner.
> - Die Herkunft steht dabei: laufender Lauf, gestellte Prüfung oder Rekonstruktion.
> - „Bestätigt durch Ausführung" nur mit beigefügter Ausgabe, sonst „gelesen, nicht ausgeführt".
> - Eine berichtigte Zahl braucht ihre eigenen Eichfälle.
> - Jede Aufstellung nennt, ob sie vollständig ist oder ein Auszug.
>
> **Maßstäbe**
> - Ein Maßstab wird vor der Messung gesetzt und danach nicht verhandelt. Eine Grenze wird nie verschoben, damit etwas durchgeht.
> - Laut scheitern, nie still. Eine Prüfung ohne Gegenstand meldet das, statt zu bestehen.
> - Eine Sperre ohne Sperrung meldet „nicht gemessen", nicht „bestanden".
> - Ein Sperrbauteil wird am Zustrom gemessen, nie am Rest.
> - Je Tor ein roter und ein grüner Eichfall.
>
> **Läufe und Kasse**
> - Jede Messgerätänderung erzwingt einen neuen Lauf. Während eines Laufs wird nichts am Messgerät geändert.
> - Abbrüche und abgewiesene Aufrufe erscheinen im Bericht **und** im Kassenblatt. Ein folgenloser Abbruch ist erlaubt, ein verschwiegener nicht.
> - `.err`-Dateien nach jedem Lauf durchsehen, den Befund nennen — auch wenn sie leer sind.
> - Der Gesamtstand wird gegen die Summe der Einzelläufe geprüft, jede Abweichung benannt.
> - Ein Aufruf trägt genau eine Lauf- und Abschnittszuordnung.
>
> **Ablieferung**
> - Keine Datei überschreiben. Nummerierte Namen, jede Adresse einmal.
> - Melden und Abliefern sind ein Vorgang: erst hochladen, dann Dateiliste und Prüfsumme neu schreiben, dann melden.
> - Jeder Bericht nennt Bericht, Dateiliste, Ordnerprüfsumme und Kassenblatt als ganze URL in eigener Zeile.
> - Abgeliefert wird **auch bei Abbruch**. Ein Abschlussordner ohne Ergebnis ist ein Ergebnis; eine Meldung ohne Ordner ist keines.
>
> **Rollen**
> - Hermes führt aus. Chat-Claude ist Auftraggeber, Prüfer und Korrektiv. **Philipp entscheidet und gibt ab Phase 4 allein frei.**
>
> ## Ergänzungen nach dem Wiedereinstieg
> - **V17:** Eine Sitzung, ein Auftrag; erst Abschlussordner liefern, dann bewusst zurücksetzen. Neuer Auftrag in frischer Sitzung.
> - **V18, durch V19 präzisiert:** Dauerhaftes Wissen liegt im Gedächtnisordner und Abschlussordner, nicht im Sitzungskontext.
> - **V19:** `laeufe/gedaechtnis/` ist die einzige dauerhafte fachliche Gedächtnisablage. Kein Obsidian-Tresor. Nummerierte Dateien nie überschreiben. `STAND` nach jedem Auftrag, `REGELN` nach neuer Masterprompt-Fassung, `UNTERBAU` bei Maschinenänderung. Diese Initialfassung enthält die ausdrücklich übermittelten Ergänzungen, auch vor dem Ausschreiben von v7.
> - **V20:** Kassenabgrenzung gemäß Auftraggeber umgestellt; Zahlen ausschließlich im verlinkten Kassenblatt führen, keine zweite laufende Buchhaltung im Regelwerk.
> - **Fassung-7-Ergänzung 25 (Auftraggeber):** Der Auftraggeber prüft, ob eine verlangte Abfrage etwas kostet, bevor er sie in eine Liste mit „0 Modellaufrufe“ schreibt.
> - **Fassung-7-Ergänzung 26 (Auftraggeber):** Eine abgeleitete Zahl trägt nie mehr Genauigkeit als ihre Eingangswerte. Steht eine gemessene Zahl daneben, gilt die gemessene. Die konkrete Rundungsbegründung im Begleitbrief wurde von Hermes anhand der Rohdaten widerlegt; die Regel wird dadurch nicht aufgehoben.
> - **Trägernachweis:** einmalig freigegebener kurzer Modelltest, separat verbuchen, Ausgabe wörtlich mit Datum dokumentieren. Keine Wiederholung außer bei Trägerwechsel oder Abweichungsverdacht und passender Freigabe. Abweichung zuerst melden; keine eigenmächtige Modelländerung. Ein fehlgeschlagener Test ist kein Trägernachweis. Der CLI-Test beweist nicht das Modell einer anderen, laufenden Sitzung.
> - **Schutz des Unterbaus:** Nur Pfade, Konfigurationsschlüssel und Anmelde-Metadaten veröffentlichen. Keine Passwörter, API-Schlüssel, OAuth-/Sitzungstokens oder vollständigen Auth-Dateien in den Prüfkanal legen.
>
> Bericht mit offenen Punkten und Quellen:
> https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/ZWISCHENBERICHT.md

**Abgleich mit v7 und v8 (R101 Teil 2):**
- **Nur 1 von 20 Wendungen aus REGELN-01 steht in v7 oder v8:** „Laut scheitern“, Verfassungssatz 6 (v8 Z. 105 und 366).
- **Die übrigen 19 stehen in keiner der beiden Fassungen** (*gerechnet* 20 − 1). Darunter:
  - „Protokollabfrage“ (Z. 8), „Menge im Satz“ (Z. 9), „Kassenblatt“ (Z. 24), „.err“ (Z. 25), „Summe der Einzelläufe“ (Z. 26)
  - „Melden und Abliefern“ (Z. 31), „ganze URL in eigener Zeile“ (Z. 32), „ab Phase 4 allein frei“ (Z. 36)
  - V17 „ein Auftrag“ (Z. 39), V19 „gedaechtnis“ (Z. 41), Ergänzung 25 „etwas kostet“ (Z. 43), Ergänzung 26 „abgeleitete Zahl“ (Z. 44)
- **Herkunft** nach Z. 2: „Abschnitt 5 des Wiedereinstiegsbriefs, ergänzt um die vom Auftraggeber mitgeteilten Entscheidungen“. Auftraggeber ist dort Chat-Claude (Z. 36). Die Regeln sind damit Vorentscheidungen Chat-Claudes (V-17), die Hermes als Regeln führt.
- **Verweis ins Leere:** Z. 5 verweist für die „vollständige Sammlung“ auf das „Änderungsverzeichnis Fassung 7“. Gemeint ist ABNAHME §7 mit 24 Punkten. v7 hat diese Sammlung nicht übernommen → W-2.
- **9 von 24 Punkten der Sammlung** stehen nach Wendung weder in REGELN-01 noch in v7, v8 oder MEMORY.md (R101): Nr. 1–4, 7 („Pfadnachweis je Eintrittsstelle“), 8 („Filtergüte“), 13 („zweimal durchlaufen“), 23 und 24 → L-5.

## 18.3 Nachgänge

- **Suche:** `search_files` in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG*.md` am 25.09. gegen 17:00 CEST, Muster „Ab sofort|künftig|gilt ab|stehende Regel|dauerhaft|Entscheidung Hermes|eigene Entscheidung“. Ergebnis: 3 Treffer in 3 Dateien.
- **Nur ein Auszug:** Nachgänge anderer Ordner sind nicht durchsucht → L-13.

| Regel (Wortlaut) | Quelle | Steht es in v7 oder v8? | Urheber |
|---|---|---|---|
| „Ab sofort nennt jeder Abschlussbericht diese vier Adressen als ganze URL in eigener Zeile.“ | `NACHGANG.md` Z. 31 und `NACHGANG-03.md` Z. 31 | nein („ganze URL in eigener Zeile“: 0) | Hermes setzt Punkt 22 der Sammlung V-17 um |
| „**V12 ist umgesetzt.** Ab sofort trägt jede Fassung eine laufende Nummer und wird nie überschrieben.“ | `NACHGANG-04.md` Z. 22 | nein („überschreiben“: 0) | Hermes setzt V12 um. V12 ist Chat-Claudes Entscheidung, PRUEFUNG4 vom 20.09. Z. 35: „V12 — die Behebung, meine Entscheidung“ |

## 18.4 Stehende Anweisungen aus dem Chat

**Arbeitsregel vom 23.09.2026 08:25:31, id 12450, im Wortlaut** (`arbeit/lesen/philipp-ab-2026-09-18.md` Z. 434; Urheber: Philipp, P-9):

> Philipp gibt dir so viel Verantwortung wie möglich — Weiterarbeiten ist der Normalfall, Anhalten die Ausnahme. Diese Regel, von Philipp gesetzt, ersetzt deine eben verschärfte Zeile; trag sie so in MEMORY.md und in die Skill ein. Entscheide selbst, was im Rahmen von Masterprompt, Verfassung und Budget liegt — Torgrenzen und Verfassungen bleiben unantastbar —, kennzeichne es als deine Entscheidung und begründe es im Bericht. Anhalten nur an drei harten Linien: (1) Unumkehrbares — Daten löschen oder überschreiben, versiegelte Ordner ändern, Git-Geschichte umschreiben, alles, was die MilieuLux-Webseite oder andere Dienste auf dem Server berührt; (2) Geld über das gesetzte Budget; (3) Sicherheitsmechanismen — eine nicht erteilte Freigabe, einen Sicherheitsfilter oder eine Modellablehnung umgehst du nie, weder durch Umformulieren noch über einen anderen Befehl oder ein anderes Modell. Anhalten heißt: Diese eine Handlung wartet, alle unabhängige Arbeit läuft weiter. Formatsperre („command parser limit or malformed executable payload") mit dem gespeicherten Skript als genanntem Ausweg: Führ das Skript unverändert aus, lesend wie schreibend — aber nur, wenn es ohne das Formatproblem jede andere Prüfung bestanden hätte; enthält es etwas, das eine Freigabe oder den Sicherheitsprüfer auslösen würde, gilt Linie 3. Vorbeugend lange Befehle von vornherein als Skriptdatei schreiben. Melden: jede Sperre wörtlich mit Befehl und deiner Einordnung, jede eigene Entscheidung mit Begründung — gesammelt in Bericht und Endmeldung; Nachrichten an Philipp nur an einer harten Linie und mit der Endmeldung. Wiederkehrende harmlose Freigabeabfragen schlägst du Philipp als dauerhafte Freigabe vor, statt sie abzuwarten. Dann weiter mit den Punkten 1 bis 5.

- **Steht es in v8?** Nein: „Normalfall“, „harte Linie“ und „Formatsperre“ haben je 0 Treffer (R101).
- **Abgelegt in:** MEMORY.md Z. 5, gekürzt und mit Zusatz (→ W-3); Skill `measurement-harness-discipline` Z. 58; Skill `biotop-phase-bauen` Z. 53.
- **Status:** gilt.

**Weitere stehende Anweisungen** („Wortlaut“ gekürzt mit „…“):

| Nr | Regel (Wortlaut) | Datum, id, Urheber | Steht es in v8? | Abgelegt in | Status |
|---|---|---|---|---|---|
| A-1 | „ein Reviewdurchgang, keine Fixagenten-Kaskade, kein Audit der Audits, kein Elternrepro für Befunde, die du selbst am Elterncode reproduzieren kannst“ | 20.09. 20:10:36, id 7732, P-5 | teilweise: „Ein Reviewdurchgang“ (Z. 450) und Grundsatz 9 „Der Prüfaufwand muss zum Gegenstand passen“ (seit v7). Der Rest nicht | USER.md Z. 5; `audit-channel-delivery` Z. 30 | gilt |
| A-2 | „künftig ist jede Abnahme und jeder eingefrorene Kern ein eigener Commit“ | 21.09. 12:05:50, id 10669, V-5 (nicht bestätigt) | nein; Z. 476 sagt „eigenem Commit“ nur für die Behebungsrunde | `measurement-harness-discipline` Z. 51 | wird befolgt |
| A-3 | „Eine abgelehnte oder abgelaufene Freigabe wird nie durch Umformulieren, einen anderen Befehl oder einen anderen Weg umgangen, sondern neu angefordert oder mit Meldung angehalten; Freigaberegeln setzt nur Philipp.“ | 21.09. 13:50:51, id 10766, P-8 | nein | `…/abschluss-01/MEMORY-Freigaberegel.md` Z. 7; heute MEMORY.md Z. 5, Linie 3 | aufgegangen in der Arbeitsregel |
| A-4 | „Stell den Träger dauerhaft auf Claude Opus 5.5 mit Denkstufe max — als Grundwert in config.yaml, nicht nur per /model …“ | 23.09. 19:42:19, id 14337, P-10 | nein | `config.yaml` (`model.default`; vor-t4 §10 Nr. 1) | gilt |
| A-5 | „Der Reviewer ist an dieselbe Regel gebunden wie du: bei einer Sicherheitssperre anhalten und melden, nie auf anderem Weg lesen.“ | 24.09. 02:14:45, id 15154, V-11 | nein | NICHT GEFUNDEN | gilt (Auslegung Hermes: stehend wegen „dieselbe Regel“) |
| A-6 | „Die Übergabe nach jedem abgeschlossenen Schritt nachführen, damit die Zwischenberichte nicht veralten.“ | 24.09. 11:49:51, id 15992, V-12 | nein | MEMORY.md Z. 7 („auftrag.json + UEBERGABE.md aktuell halten“) | gilt |
| A-7 | „künftig bekommt jedes Review einen eigenen Ordner, und du prüfst vor dem Start, dass keines läuft.“ | 24.09. 23:15:27, id 16901, V-15 | nein („eigenen Ordner“: 0) | `audit-channel-delivery` Z. 30 und 36 | gilt |
| A-8 | Startregel für T4 (Wortlaut in Teil 2, N-9) | 24.09. 23:15:27, id 16901, V-15 | nein | `/root/biotop-vor-t4-06/BAU-S1B-M2B.md` Z. 30–31; `audit-channel-delivery` Z. 36 | gilt bis zum Start von T4 |
| A-9 | „Die Verdichtung der Sitzungen läuft künftig über OpenRouter mit dem vorhandenen Schlüssel …“ | 25.09. 00:27:35, id 17217, P-13 | nein | `config.yaml` `auxiliary.compression.*` (VERDICHTUNG-OPENROUTER.md Z. 8) | gilt; → W-4 |
| A-10 | „Dauerhaft: Zwischenbericht in den Prüfkanal spätestens bei 120 von 150 Aufrufen einer Sitzung — nicht erinnern, sondern auslösen …“ | 23.09. 15:03:47, id 13912, V-9 | **ja**, v8 Z. 450 | MEMORY.md Z. 7, mit Schwellen 110/140 (H-7) | gilt |

**Keine stehende Regel:** Die Einzelfreigabe vom 24.09. 11:38:00 (id 15962) ist ausdrücklich „nicht als Dauerregel“ erteilt.

## 18.5 MEMORY.md und USER.md im Wortlaut (Biotop-Teil)

- **Umfang:** Auslegung Hermes: Alle 4 Einträge in MEMORY.md und alle 4 Einträge in USER.md betreffen das Biotop; sie stehen deshalb ganz da. Einträge sind durch „§“ getrennt.
- **Änderungen am Text:** Die Prüfkanal-Adresse ist durch `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` ersetzt. Den Telegram-Namen Philipps in USER.md Z. 1 habe ich vorsorglich geschwärzt.
- Beide Texte wurden per Skript eingesetzt und gegengeprüft (R146: je 7 von 7 nichtleeren Zeilen).

**MEMORY.md**

> Skill 'biotop-phase-bauen' (software-development) is user-owned, not curator-managed: autonomous patches are refused. Lessons from Biotop sessions can only be written after `hermes curator adopt biotop-phase-bauen` — offer that before spending a review pass on patches.
> §
> Dauerhaftes fachliches Gedächtnis (V19) liegt im Prüfkanal: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/ — nummerierte STAND-, REGELN-, UNTERBAU-Dateien plus Manifeste; kein Obsidian-Tresor. Nur HERMES-1 schreibt, HERMES-2/3 lesen. V17: eine Sitzung, ein Auftrag; Abschlussordner vor bewusstem Reset.
> §
> Arbeitsregel Philipp (23.09.2026, ersetzt alle früheren Anhalte-/Freigaberegeln): Weiterarbeiten ist Normalfall, Anhalten Ausnahme. Hermes entscheidet selbst im Rahmen von Masterprompt, Verfassung, Budget (Torgrenzen/Verfassungen unantastbar), gekennzeichnet und begründet im Bericht. Anhalten nur an drei harten Linien: (1) Unumkehrbares: Daten löschen/überschreiben, versiegelte Ordner ändern, Git-Geschichte umschreiben, MilieuLux-Webseite/andere Serverdienste berühren; (2) Geld über Budget; (3) nicht erteilte Freigabe, Sicherheitsfilter, Modellablehnung nie umgehen – kein Umformulieren, kein anderer Befehl/Weg/Modell (Beispiel: PYTHONPATH= durch cd ersetzen). Anhalten = nur diese Handlung wartet, Unabhängiges läuft weiter. Formatsperre „command parser limit or malformed executable payload“: gespeichertes Skript unverändert ausführen, wenn es sonst jede Prüfung bestanden hätte, sonst Linie 3; lange Befehle vorab als Skriptdatei. Jede Sperre wörtlich mit Befehl und Einordnung, jede eigene Entscheidung begründet in Bericht und Endmeldung; Nachrichten an Philipp nur an harter Linie und mit Endmeldung. Wiederkehrende harmlose Freigabeabfragen als dauerhafte Freigabe vorschlagen.
> §
> Prüfkanal-Lieferung: Verzeichnisse nicht abrufbar — jede Abholadresse als volle Datei-URL in eigener Zeile (…/DATEIEN.txt). Zwischenbericht-Wächter-Cron 26fbb1513a1a (~/.hermes/scripts/zwischenbericht_waechter.py): 110/140 von 150 Runden, ≥80 % Kontext, erste gescheiterte Verdichtung (je Turn); auftrag.json + UEBERGABE.md aktuell halten, auch vor Sitzungsende.

- **Z. 5 weicht von Philipps Wortlaut ab.** Der Zusatz „(23.09.2026, ersetzt alle früheren Anhalte-/Freigaberegeln)“ ist weiter gefasst als „ersetzt deine eben verschärfte Zeile“ → W-3.
- **Z. 7 setzt andere Schwellen** als v8 Z. 450: „110/140 von 150 Runden“ statt „spätestens bei 120 von 150 Aufrufen“ (eigene Entscheidung H-7).

**USER.md**

> User is Philipp Zöllisch (Telegram [GESCHWÄRZT: USER.md Z. 1, Anzeigename]), Auftraggeber of the INFINITE EVOLUTION „Biotop" project; a separate reviewer ("Chat-Claude") audits delivered folders, not chat messages. Communicates in German; expects German naming in code, files and reports.
> §
> User's evidence standard (applies to every report): measure, don't assume; every number with Bezugsgröße ("x von y"); "bestätigt durch Ausführung" only with attached output; mark own decisions as own; a failed line is reported as failed; no silent differences in breakdowns (sums must reconcile, categories not re-cut between reports). Corrects Hermes sharply and precisely when a claim wasn't measured.
> §
> User's standing procedure for every task: one review, no fix-agent cascade, audit-of-audits or duplicate parent repros; gate-bearing evidence only. Deliverables: Prüfkanal folder + checksum; ZWISCHENBERICHT.md, DATEIEN.txt, DB costs/open items before every session end (no report = not delivered). Hard task budgets; halt before overspending. Rule changes during measurements require Philipp's decision.
> §
> Values self-correction over polish: praises retracted claims that would have flattered Hermes, admits own errors, never lowers a threshold when a measurement fails it — the cause gets changed, not the bar.

## 18.6 Skills (nur Verweis)

| Skill | Pfad | Bytes, Änderungszeit (CEST), SHA-256 (R79) | Zweck (Z. 3, wörtlich) | Regeln Philipps darin (Zeilen laut R79 §2) |
|---|---|---|---|---|
| biotop-phase-bauen | `/root/.hermes/skills/software-development/biotop-phase-bauen/SKILL.md` | 14.307; 25.09. 12:52:04; `f1defae43b6759ef244d48c037f9c540ec2c8872071848de12940f439e531176` | „Use when building a Biotop phase; Tor lines, Prüfkanal.“ | Z. 53: Formatsperre („Regel Philipp 23.09.“). Laut MEMORY.md Z. 1 ist der Skill „user-owned“ |
| audit-channel-delivery | `…/audit-channel-delivery/SKILL.md` | 18.104; 25.09. 10:15:59; `99c3d1617d28becc197e00caa3af99577517426f0257d16bd5b028dd616b19b0` | „Use when delivering work to the audit channel (Prüfkanal).“ | Z. 30: „the user's standing rule: one review, no fix-agent cascade, no audit of audits“ (A-1, A-7); Z. 36: zwei Reviews, Startregel (A-8); Z. 39: Endmeldung; Z. 50: gesperrtes Skript; Z. 52: Fehlalarm-Bericht |
| measurement-harness-discipline | `…/measurement-harness-discipline/SKILL.md` | 89.573; 25.09. 10:15:59; `f6211e3fbfaa2b640a00a26937af3085d335d6407685286f7334cc999f58802e` | „Use when a measured number gates a decision.“ | Z. 58: „Owner's rule (Philipp, 23.09.2026)“ (Arbeitsregel); Z. 29: Last nach vorab festem Kriterium (N-8); Z. 51: eigener Commit (A-2); Z. 65 und `references/defect-class-sweep.md` Z. 36: Enthaltungen zählen, Weiche (V-7) |
| delegated-build-orchestration | `…/delegated-build-orchestration/SKILL.md` | 6.867; 25.09. 10:15:59; `e953ba5772d61038b0ca103f195a5b3591e83148b8a2c4dba2430391903463e0` | „Use when splitting a build across parallel subagents.“ | Eine ausdrückliche Regel Philipps ist NICHT GEFUNDEN; Z. 14, 16 und 38 beschreiben die Arbeitsweise |
