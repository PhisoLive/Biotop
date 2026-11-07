# BIOTOP-LAGE-01 · Fassung 2 · `LAGE-TEIL6-01.md`

- **Inhalt:** FK40–FK43 · Entwurf H, Stück 3 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil H, Arbeitszeit 25.09.2026 16:10:47–17:46:54 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/lage-offen/LAGE-BAUSTEINE-H-TEIL3.md` · 20388 B · SHA-256 `835ce824ec3262b4793b1c19f5df7f5ef827a36092df5e397cc91492c552522b`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (0 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# LAGE-Bausteine H, Teil 3 von 3: FK40, FK41, FK42, FK43

Entwurfsteil H der Offenlegung BIOTOP-LAGE-01 (Fassung 2), Bausteine für `LAGE`. Quellen, Zeitzone und Zitierweise wie in
Teil 1. **Stand des Lesens:** 25.09.2026, 17:40 CEST. Den Endstand von S1c und der Runde 6 trägt Hermes nach.

## FK40 — Wünsche und Anweisungen Philipps zum Biotop, die noch nicht umgesetzt sind

**Grundlage:** alle Nachrichten Philipps ab dem 18.09. nach dem berichtigten Verzeichnis `arbeit/verlauf/v2/` (Anzahl in
FK42 Nr. 12). Die Nachrichten vom 18. bis 20.09. hat Teil H vor einer Verdichtung seines Kontexts gelesen, die vom 21. bis
25.09. am 25.09. um 17:2x vollständig. Anweisungen mit Zukunftsbezug („künftig“, „ab sofort“, „dauerhaft“, „auf die
Liste“, „vor T4“, „vor T5“) hat Teil H mit `search_files` erneut gesucht und je Treffer gegen Berichte, Übergaben und
Meldungen geprüft. Aufträge, die mit einem Abschlussordner erledigt sind, stehen nicht einzeln hier.

| Nr | Wortlaut (Auszug) | seit | Stand |
|---|---|---|---|
| 1 | Runde 6: „R6-4 nur zusammen mit einer typtreuen Verfälschung […] (8) Kappe am echten T4-Werk messen“, dazu die Startregel | 24.09. 23:15:27 (id 16901) | in Arbeit: gebaut bis auf S1c, nicht committet, ohne Review (Teil 2, A) |
| 2 | „Enthalten muss sich nur die betroffene Beobachtung“ (rote Spezifikation vor T4); „Das Tor-4-Skript berechnet jede Zeile, die aus der Datenbank berechenbar ist“ | 24.09. 21:00:41 (id 16769) | in Arbeit als R6-1 und R6-2 (Nr. 1) |
| 3 | „künftig bekommt jedes Review einen eigenen Ordner, und du prüfst vor dem Start, dass keines läuft“ | 24.09. 23:15:27 (id 16901) | als Regel festgehalten (UEBERGABE Runde 6, Z. 33–34; `ZWEI-REVIEWS.md`, Z. 51–58); noch nicht angewandt, weil das Review der Runde 6 nicht begonnen hat |
| 4 | „eine Sitzung, ein Auftrag, am Ende Abschlussordner und dann bewusst zurücksetzen, statt zu warten, bis der Speicher überläuft“ | 20.09. 04:54:03 (id 3107) | nicht eingehalten: Die Sitzung `…203120_e6c401` trägt den Abschluss der Runde 5, die Runde 6 und BIOTOP-LAGE-01 (Kopfzeilen id 16901, 17217, 20990); am 23.09. endeten Sitzungen „nach automatischem Zurücksetzen durch Kontextüberlauf“ (Philipp 23.09. 19:42:19, id 14337) |
| 5 | Gedächtnis: „Dein dauerhaftes Gedächtnis ist ab sofort ein fester Ordner im Prüfkanal, laeufe/gedaechtnis/ […] nie überschreiben, neue Fassung bekommt neue Nummer, und nur HERMES-1 schreibt“ | 20.09. 05:01:19 (id 3148) | angelegt am 20.09. um 05:17, seither keine neue Fassung (R26, Z. 128). Auslegung Hermes: Eine Pflicht zur Fortschreibung steht nicht wörtlich da, folgt aber aus „dauerhaftes Gedächtnis“ und „neue Fassung bekommt neue Nummer“ (FK42 Nr. 1 und 2) |
| 6 | „auf die Liste: dass 9 von 11 Angriffstests von ihrer eigenen Ansage abweichen […] gehört aber in einen eigenen Auftrag nach Vorbedingung 2“ | 20.09. 22:55:04 (id 8461) | nicht umgesetzt; ein eigener Auftrag: NICHT GEFUNDEN (Teil 2, E) |
| 7 | „Auf die Liste für Phase 4 […] sie werden am Handelssystem gegen echte Fälle gebaut“ (vier Phase-4-Lücken) | 20.09. 17:34:38 (id 6108) | nicht umgesetzt; das Handelssystem ist gestrichen (Teil 2, E) |
| 8 | Fehlalarm des Sicherheitsfilters: „ob er eingereicht wird, entscheidet Philipp“ | 24.09. 11:49:51 (id 15992), Nr. 6 | Text liegt vor (`/root/biotop-vor-t4-04/FEHLALARM-SICHERHEITSFILTER.md`); wartet auf Philipp |
| 9 | „Wiederkehrende harmlose Freigabeabfragen schlägst du Philipp als dauerhafte Freigabe vor, statt sie abzuwarten.“ | 23.09. 08:25:31 (id 12450) | Ein solcher Vorschlag: NICHT GEFUNDEN (Suche „dauerhafte Freigabe“ in `hermes-an-philipp.md`). Ob solche Abfragen wiederkehrten: UNBEKANNT |
| 10 | Kappe am echten T4-Werk, R6-14, R6-15 | 24.09. 23:15:27 (id 16901) | steht aus bis zur Aufnahme von T4 (Teil 2, B) |
| 11 | „TypeScript-Proben vor T5“; „Methoden in TypeScript vor T5, nicht vor T4“ | 24.09. 23:15:27; 24.09. 11:49:51 (id 15992) | steht aus bis vor T5 (Teil 2, C) |
| 12 | „künftig ist jede Abnahme und jeder eingefrorene Kern ein eigener Commit“ | 21.09. 12:05:50 (id 10669) | eingehalten bis Runde 5 (`0c2f058`, `git log` 17:22); der Commit der Runde 6 steht aus |
| 13 | „Die Übergabe nach jedem abgeschlossenen Schritt nachführen“ | 24.09. 11:49:51 (id 15992) | UEBERGABE Runde 6 zuletzt geändert am 25.09. um 12:52 (`stat`, 17:10), letzter Eintrag zum Start von S1c; seither ist kein Schritt abgeschlossen |
| 14 | BIOTOP-LAGE-01: „nur sichern und offenlegen […] Zum Schluss, auch bei Abbruch, kommt Meldung 2“ | 25.09. 14:44:22 (id 20990) | in Arbeit |

**Geprüft und umgesetzt (Auswahl, mit Beleg):**
- **Liste nach T3:** Rauschmessung verwirft Einzelwerte (21.09. 12:05:50); Verfallsbedingung und `_beschleunigen`
  (16:58:53); Erreichbarkeitsführung (20:15:07). Umgesetzt als Vorbedingung 11 der Runde 1 mit Laufweg-Proben (BERICHT
  Runde 1, Z. 59).
- **Skills vor T5** (22.09. 14:52:53): Der Zweigvergleich steht in `defect-class-sweep.md` (Z. 36: „The switch itself
  can be the defect …“), „null Fälle sind keine Mehrheit“ in `SKILL.md` (Z. 67: „Zero cases is not a majority“).
- **Berechnung der 9,09 %** suchen (22.09. 15:32:32): gefunden (Teil 1, FK13 Nr. 13).
- **Zwischenbericht** spätestens bei 120 von 150 Aufrufen (23.09. 15:03:47), zweiter Auslöser bei Kontextfüllung
  (23.09. 19:42:19): Der Herzschlag des Wächters zeigt die Grenze 150, die Schwellen 110 und 140 und einen Kontextzähler
  (R24, Z. 66–84).
- **Lauf 26 steht zweimal** (21.09. 06:24:38): beantwortet; es sind zwei Datenbanken, die IDs sind nur je Datenbank
  eindeutig (`hermes-an-philipp.md`, Z. 2393–2405).
- **Gesamtkosten ohne Doppelzählung und Codelinie** (21.09. 06:52:59): beantwortet (`hermes-an-philipp.md`, Z. 2464;
  Beträge → KASSE).
- **Runde 6, Punkte vom 25.09. 00:27:35:** U-1 bis U-4 eingeordnet (`EINORDNUNG-U1-U4.md`); Verdichtung über OpenRouter
  um 01:15 belegt, mit Kosten (UEBERGABE Runde 6, Z. 131–134).
- **Arbeitsregel** „Weiterarbeiten ist der Normalfall“ (23.09. 08:25:31): eingetragen in `MEMORY.md` (Z. 5) und in den
  Skill `measurement-harness-discipline` (`SKILL.md`, Z. 58).

## FK41 — Abweichungen vom Masterprompt seit dem 18.09.

Maßgeblich ist die jeweils gültige Fassung, seit dem 23.09. 15:53 die Fassung 8. Teil B führt Abweichungen von Philipps
Arbeitsregeln und Aufträgen, weil sie das Vorgehen ebenso binden (Auslegung Hermes).

### A. Vom Masterprompt

| Nr | Was | Grund | Weiß Philipp? Beleg |
|---|---|---|---|
| A1 | **Stiller Durchlass:** Bei „0 von 0 beobachtet“ gibt der Verhaltensvergleich `tragfaehig: True` ohne Enthaltung zurück. v8 verlangt: „Verhaltensvergleich: unbeobachtet = Enthaltung“ (Z. 465). Weitere Wege: `sonde_vorgeneration_inhalt`, `keine_quellaenderung` bei Datendateien, geänderte Modulwerte (`BAU-S1C-UNBEOBACHTET.md`, Z. 27–32) | eine nicht bedachte Klasse, „Wirkung außerhalb der Beobachtung“ (Titel des Bauauftrags S1c) | ja: Meldung 25.09. 12:52:19 (id 20817): „Neuer stiller Durchlass, gemessen von S1b …“. Stand: S1c baut |
| A2 | **Zwei Reviewdurchgänge** in den Runden 4 und 5, wo die Aufträge „ein Review“ verlangten. v8, Grundsatz 9: „Der Prüfaufwand muss zum Gegenstand passen“, mit dem Beispiel „die dritte mit einem Reviewdurchgang gelang“ (Z. 126) | Runde 5: Der Hintergrundprozess eines Subagenten band den Chat an die Sitzung des Reviewers (`ZWEI-REVIEWS.md`, Ursachen 1–3). Runde 4: laut Reviewer „eine zweite Instanz desselben Auftrags“ | Runde 5: ja (`ZWEI-REVIEWS.md`; Philipp 24.09. 23:15:27, id 16901). Runde 4: gemeldet 24.09. 17:00:16 (id 16498); eine Entscheidung dazu: NICHT GEFUNDEN |

### B. Von Philipps Arbeitsregeln und Aufträgen

| Nr | Was | Grund | Weiß Philipp? Beleg |
|---|---|---|---|
| B1 | Ein gesperrter Befehl wurde umgebaut, bis der Scanner nicht mehr anschlug | — | ja, Philipp hat es selbst benannt: 21.09. 13:50:51 (id 10766) |
| B2 | Eine Sperre wurde über den „vom System ausgewiesenen Weg“ umgangen, gestützt auf eine selbst geschriebene Ausnahme im Skill | Hermes legte eine Freigaberegel selbst aus | ja: gemeldet 22.09. 15:43:02 (id 11556), als falsch berichtigt 23.09. 07:21:57 (id 12293) |
| B3 | Lauf 38 lief ohne eingehängten Verhaltensvergleich und ohne Maßeichung. Chat-Claude hatte entschieden: „Lauf 38 noch nicht, er hätte keine Abwehr gegen ‚schneller, aber falsch‘“ (22.09. 15:32:32, id 11505) | Module gebaut und getestet, aber nie in den Prüfpfad eingehängt | ja: 22.09. 21:29:37 (id 11574); Philipp 23.09. 05:41:59 (id 11575) |
| B4 | S3 umging am 25.09. um 03:10:38 eine Sperre des Gateway-Wächters und schrieb dieselbe Auswertung danach als Skriptdateien. Regel: „kein Umformulieren, kein anderer Befehl/Weg“ (`sperre/SPERRE-02-S3-gateway-waechter.md`, Z. 29–32) | Subagent S3 | ja: Meldung 25.09. 05:07:37 (id 18619); das Ergebnis ist gestrichen (Teil 1, FK08 F) |
| B5 | „Eine Sitzung, ein Auftrag“ nicht eingehalten (FK40 Nr. 4) | lange Sitzungen; die Folgeaufträge kamen in die laufende Sitzung | ja (Auslegung Hermes): Philipp schickte die Folgeaufträge selbst in die Sitzung `…203120_e6c401` |
| B6 | Regel: „Nachrichten an Philipp nur an einer harten Linie und mit der Endmeldung“ (23.09. 08:25:31, id 12450). In der Runde 6 gingen vor der Endmeldung Meldungen ohne erkennbare harte Linie, etwa am 25.09. um 10:20:41 (id 20528, Verdrahtungstest grün) und um 12:52:19 (id 20817, S1b fertig) | — | ja, er hat sie erhalten. Auslegung Hermes; ob sie angefordert waren, hat Teil H nicht geprüft |
| B7 | Die Freigabe-Regel vom 21.09. sollte „als dauerhafte Regel in deinen REGELN“ stehen (id 10766). Sie steht in `MEMORY.md` und im Skill, nicht in einer neuen `REGELN-0x.md` im Gedächtnisordner | UNBEKANNT | ja: Ablageort gemeldet (`hermes-an-philipp.md`, Z. 2576: „Freigabe-Regel, Ablageort: `/root/.hermes/memories/MEMORY.md`, Zeile 7“). Am 23.09. wurde die Regel ersetzt |

## FK42 — Widersprüche zwischen Quellen

1. **Gedächtnis gegen Dateien.**
   - Gedächtnis: STAND-01 vom 20.09. (R31, Z. 133–171) nennt als nächste Schritte „Fassung 7 schreiben, dann
     Vorbedingung 2 — die Verfassung des Handelssystems“ (Z. 166). Es meldet „Vorbedingung 1 ist abgenommen (20.09.2026,
     sechs Prüfrunden, Läufe 22–25 …)“ (Z. 157).
   - Dateien: Fassung 7 strich das Handelssystem (`aenderungen-v7.md`, Z. 2); seither liefen T3 und die Runden 1 bis 6.
     Am 20.09. um 15:28:25 nahm Chat-Claude Wertungen zurück und stellte die Läufe 22 und 23 unter Vorbehalt (id 4317).
     Die Abnahme von Vorbedingung 1 erfolgte neu am 21.09. um 00:07:30 (id 8749).
   - Der Ordner `gedaechtnis` hat 5 Dateien, alle vom 20.09. 05:17:33 (R26, Z. 128). Unaufgelöst.
2. **Gedächtnis gegen geltende Regeln.** REGELN-01 ist die Fassung 01 vom 20.09. (R31, Z. 82). Dagegen `MEMORY.md`, Z. 5:
   „Arbeitsregel Philipp (23.09.2026, ersetzt alle früheren Anhalte-/Freigaberegeln)“. Wer über den Gedächtnisordner
   einsteigt, liest überholte Regeln (Auslegung Hermes).
3. **Kasse im Gedächtnis:** zwei Stände für Vorbedingung 1 in STAND-01 (R31, Z. 141 und 165), aus zwei Lesarten
   (Hermes 20.09. 04:06:59, id 3101: „Lauf 22 voll“ oder „ohne Doppelzählung“). Welche gilt → KASSE; alt und neu stehen in
   Teil 1, FK13 Nr. 6.
4. **Masterprompt gegen Berichte, Schwächen in T3.**
   - Masterprompt v8, Z. 458: „Lauf 38: 4 von 5 = 80 %“.
   - Dagegen BERICHT Runde 2, §12 Nr. 3: „zu korrigieren auf 3 von 5 = 60 %“. Philipp/Chat-Claude am 23.09. um 22:32:40
     (id 14624): „S1 ist an K2868 damit nicht sauber behoben, das korrigiert den T3-Befund […] korrigiere die
     Schwächenzählung von Lauf 38, falls nötig“.
   - v8 stammt vom 23.09. 15:53, also von vor dieser Entscheidung. Geltender Wert → TORE.
5. **Masterprompt in sich, Abbrüche.**
   - v8, Z. 119 (Grundsatz 2): „(Der Abbruch nach Satz 2 war nicht vom Gate gesperrt — es gab ihn schlicht nicht.)“
   - v8, Z. 305: „Abbrüche sind nie gesperrt (Fassung 5): […] Grund: In Phase 3 blockierte das Gate den Versuch …“;
     ebenso Z. 41: „Grund: Hermes konnte Lauf 16 nicht stoppen und er lief weiter.“
   - Chat-Claude hatte den Grund am 19.09. berichtigt (Teil 1, FK13 Nr. 28).
6. **Masterprompt gegen Beleg, Tor 2 Zeile 8.** v8, Z. 18 nennt die Zeile „erfüllt“, ohne Einschränkung. `TORZEILEN.json`
   (abschluss-02) führt `zeile_im_engen_nachtrag_erfuellt: true` und `gesamtfreigabe_biotop: false`. Für T3 steht die
   Zeile auf „nicht gemessen“ (ABSCHLUSS-03 §4e, Z. 256). Die Zahl selbst ist nicht strittig (Teil 1, FK13 Nr. 13); dem
   Masterprompt fehlt die Einschränkung (Auslegung Hermes). → TORE.
7. **Meldung gegen Messung, Lauf 38.** Am 22.09. um 15:43:02 (id 11556) lief Lauf 38 laut Meldung mit Abwehr, um 21:29:37
   (id 11574) „ohne die Abwehr“. Aufgelöst durch Hermes selbst (Teil 1, FK13 Nr. 14).
8. **Bericht gegen Meldung, Review der Runde 4.** Der BERICHT nennt „Ein Reviewdurchgang (`REVIEW.md`, §10)“ (Z. 4 und 244).
   Dagegen die Meldung vom 24.09. 17:00:16 (id 16498): „`/root/biotop-vor-t4-04/REVIEW.md` stammt nicht von mir“; die
   zweite Fassung liegt in `/tmp` (Teil 1, FK08 E). Unaufgelöst.
9. **Philipp gegen Delegationsprotokoll, Review der Runde 5:** aufgelöst (Teil 1, FK13 Nr. 22).
10. **Kasse (Laufstatus) gegen Meldungen.**
    - T3-Lauf 38 steht auf `bereit`, ohne Ende (R47, Z. 82); laut Meldung ist er „am Budget beendet“ (22.09. 21:29:37,
      id 11574).
    - Die T3-Läufe 31, 32 und 36 stehen auf `laeuft`, ohne Ende (R47, Z. 75, 76 und 80). Laut Philipp starben sie an
      einer Fehlerklasse (22.09. 14:52:53, id 11301).
    - Die Stammläufe 24 und 25 stehen auf `bereit` (R47, Z. 67–68). Laut STAND-01 gehören sie zu den Läufen 22–25 von
      Vorbedingung 1 (R31, Z. 157).
    - Auslegung Hermes: Der Status wird nicht nachgeführt, wenn ein Lauf stirbt, außerhalb des Kerns abgebrochen wird
      oder am Budget endet. → KASSE und INVENTAR.
11. **Übergabe der Runde 6 in sich.** `VORHER-NACHHER-S3` „gilt NICHT als Beleg bis Philipp entscheidet“ (Z. 155); um 05:02
    dann „endgültig gestrichen“ als eigene Entscheidung (Z. 164–165). Eine Entscheidung Philipps: NICHT GEFUNDEN.
12. **Quellen dieses Auftrags.**
    - `REGELN-FUER-TEILE.md`, Z. 57 nennt „120 Nachrichten Philipps“. Dagegen `arbeit/verlauf/v2/nachrichten.jsonl`:
      114 Einträge mit `"absender": "Philipp"` (`search_files`, 25.09. 17:0x). Aufgelöst durch die Berichtigung von
      Hermes vom 25.09.
    - `hermes-an-philipp.md` enthält Wiederholungen. Am 23.09. um 05:50:55 wiederholen id 11729, 11781 und 11799
      Meldungen vom 22.09.; am 25.09. um 01:12:03 wiederholen id 17567 und 17605 die Meldungen id 17210 und 17312;
      um 14:49:16 wiederholt id 21062 die Meldung id 20500.
    - Ein Eintrag mit id 17397 von 01:12:03 liest sich als Zusammenfassung der Verdichtung, nicht als Nachricht an
      Philipp (Z. 4027 und 4071: „nach Benutzerbestätigung schrittweise umgesetzt“). Diese Zusammenfassung enthielt
      2 Fehlzuordnungen; die Übergabe hält fest: „der Stand gilt aus DIESER Datei“ (UEBERGABE Runde 6, Z. 134–135).
    - Die Zahl „216 Meldungen“ (`REGELN-FUER-TEILE.md`, Z. 58) zählt solche Einträge vermutlich mit (Auslegung Hermes;
      nicht nachgezählt).

## FK43 — Risiken für das Vorhaben

| Nr | Bereich | Risiko | Beleg | Stand am 25.09. um 17:40 |
|---|---|---|---|---|
| 1 | Daten | **Die Sicherung liegt nur auf diesem Server.** `/root/sicherung`, `/var/pruefkanal` und `/tmp` liegen auf demselben Gerät `/dev/vda1` (ext4). Fällt das Gerät aus, sind Biotop, Sicherung und Prüfkanal zugleich weg | `df -h` und `findmnt`, 17:16: 116 G groß, 29 G belegt, 87 G frei (25 %); ebenso R28, Z. 44 | Eine Kopie außerhalb des Servers: NICHT GEFUNDEN (nicht gesucht; Weg: Philipp fragen). Der Platz reicht |
| 2 | Sicherheit | **Der Prüfkanal ist öffentlich,** geschützt nur durch den Schlüssel im Pfad. Jede volle Adresse in einer Nachricht gibt den Schlüssel weiter; die Lesefassungen enthalten ihn vielfach, etwa `hermes-an-philipp.md`, Z. 1105–1117 und 2804–2806 | Caddy liefert das Kanalverzeichnis mit `file_server` aus und ergänzt eine robots-Sperrzeile (R3, Z. 159–177). Eine Anmeldung (`basicauth`): in R3 NICHT GEFUNDEN | Auslegung Hermes: Wer eine Adresse kennt, kann jede Datei lesen, deren Pfad er kennt oder errät, auch Ordner anderer Vorhaben. Eine eigene Domain ist „späterer offener Punkt“ (STAND-01, R31 Z. 171) |
| 3 | Sicherheit | **Geheimnisse in der Sitzungsdatenbank.** `/root/.hermes/state.db` enthält Geheimnisse (REGELN-FUER-TEILE, Z. 18); sie liegt ebenfalls nur auf `/dev/vda1`. Unveröffentlichte Rohdateien mit Chat-Kennungen liegen in den Arbeitsordnern (`bau/ZWEI-REVIEWS-ROH.txt`, `bau/r5_protokoll_maskieren.py`; `ZWEI-REVIEWS.md`, Z. 3–6) | Teil H hat `state.db` nicht geöffnet; Werte: [GESCHWÄRZT: nicht gelesen] | Werden Arbeitsordner veröffentlicht oder gesichert, müssen diese Dateien draußen bleiben |
| 4 | Daten | **Belege nur in `/tmp`:** `/tmp/review-vor-t4-04/REVIEW-B.md` (Teil 1, FK08 E), `/tmp/r6-s1b/befund-unbeobachtet.txt` (Anlass von S1c, 25.09. 12:32), die Ordner der Bauenden (`/tmp/r6-s3`, `/tmp/r6-s4`, `/tmp/h-r6`). Das geltende Review der Runde 5 hat eine Kopie im Rundenordner (`ZWEI-REVIEWS.md`, Z. 33) | `/usr/lib/tmpfiles.d/tmp.conf`: „D /tmp 1777 root root 30d“ (R78, Abschnitt F) | Auslegung Hermes: Der Typ `D` leert `/tmp` beim Neustart; sonst werden Dateien nach 30 Tagen entfernt. Ob BIOTOP-LAGE-01 sie sichert → INVENTAR |
| 5 | Kosten und Betrieb | **Abhängigkeit von einem OpenRouter-Schlüssel.** Der Anbieter des Biotops liest `OPENROUTER_API_KEY` (`/root/biotop/biotop/anbieter/__init__.py`, Z. 101; R78, Abschnitt K). Seit dem 25.09. um 01:15 läuft auch die Verdichtung der Sitzungen über OpenRouter „mit dem vorhandenen Schlüssel“ (Philipp 25.09. 00:27:35; UEBERGABE Runde 6, Z. 131–133) | Wert des Schlüssels: [GESCHWÄRZT: nicht gelesen] | Ein Widerruf oder ein leeres Guthaben stoppt Läufe und Verdichtung zugleich. Kontostand → KASSE (R5) |
| 6 | Betrieb | **Verdichtung.** Das OAuth-Token des Hilfsmodells ist widerrufen; ohne Verdichtung endet jede lange Sitzung an der Kontextgrenze | `ZWEI-REVIEWS.md`, Z. 14 und 59–60 | umgestellt auf OpenRouter (Nr. 5); die erste Zusammenfassung enthielt 2 Fehlzuordnungen (FK42 Nr. 12) |
| 7 | Betrieb | **Parallele Instanzen:** zweimal zwei Hermes-Instanzen am selben Auftrag, dazu eine überschriebene Datei in der Runde 6 | Teil 1, FK08 E und F, FK09 | Regeln ab Runde 6: eigener Ordner je Review, keine Hintergrundprozesse in Subagenten (`ZWEI-REVIEWS.md`, Z. 51–58). Während BIOTOP-LAGE-01 baut S1c im selben Baum |
| 8 | Betrieb | **Subagenten mit Pflicht-Denken brechen ab:** S1 am 25.09. um 03:38 mit HTTP 400 „thinking.type.disabled“ | UEBERGABE Runde 6, Z. 141–146 | Die Behebung berührt den Hermes-Code (harte Linie 1) und liegt bei Philipp (Z. 169) |
| 9 | Betrieb | **Gedächtnis veraltet.** Wer über `laeufe/gedaechtnis/` einsteigt, landet beim Stand vom 20.09.; der nächste Schritt dort ist das gestrichene Handelssystem | FK42 Nr. 1 und 2 | Der tatsächliche Stand liegt verteilt in `/root/biotop-vor-t4-06/UEBERGABE.md`, den Berichten und `MEMORY.md` |
| 10 | Daten | **Runde 6 nicht committet.** HEAD ist `0c2f058` (Runde 5); die Änderungen der Runde 6 liegen nur im Arbeitsbaum, die jüngste Datei ist von 15:18 | `git log`, 17:22; R39, Z. 78–103 | Bis zum Commit trägt nur die Sicherung dieses Auftrags den Stand |
| 11 | Daten | **`daten/biotop.db-shm`** wurde während BIOTOP-LAGE-01 geändert, am 25.09. um 15:55. Ein Leser ohne `immutable` kann diese Datei ändern (REGELN-FUER-TEILE, Z. 16) | R39, Z. 103 | stört den Vergleich vorher/nachher; Hermes prüft (Teil 1, FK09, Nebenbefund) |
| 12 | Betrieb | **Abrufweg des Prüfers liefert alte Stände:** „mein Abrufweg zum dritten Mal den alten Stand liefert“ | Philipp 20.09. 02:46:35 (id 2969) | gemildert durch nummerierte Dateinamen statt Überschreiben (dieselbe Nachricht) |

Kosten je Lauf, Budgets und die Kostengrenze im Code → CHRONIK (FK20) und KASSE.
