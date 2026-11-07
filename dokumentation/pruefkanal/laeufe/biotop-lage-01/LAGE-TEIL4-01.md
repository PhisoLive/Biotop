# BIOTOP-LAGE-01 · Fassung 2 · `LAGE-TEIL4-01.md`

- **Inhalt:** FK08, FK09, FK13 · Entwurf H, Stück 1 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil H, Arbeitszeit 25.09.2026 16:10:47–17:46:54 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/lage-offen/LAGE-BAUSTEINE-H-TEIL1.md` · 30478 B · SHA-256 `1da5b246539db3af23221d895fc169a1223768d52890d9bcb4d33119c0b88a85`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (1 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# LAGE-Bausteine H, Teil 1 von 3: FK08, FK09, FK13

Entwurfsteil H der Offenlegung BIOTOP-LAGE-01 (Fassung 2), Bausteine für `LAGE`. Geschrieben von einem Subagenten im
Auftrag von Hermes (HERMES-1); „Auslegung Hermes“ kennzeichnet eigene Lesarten. Teil 2 enthält FK39, Teil 3 FK40 bis FK43.

- **Stand des Lesens:** 25.09.2026, 16:11 bis 16:58 CEST. Den Endstand von S1c und der Runde 6 trägt Hermes nach.
- **Zeiten:** CEST (UTC+2). Die Kasse (`arbeit/kasse/laeufe.csv`, aus R25) führt die Laufzeiten in UTC; hier sind sie
  umgerechnet (gerechnet: +2 h). Geprüft an den Läufen 14, 15 und 18: Ihre umgerechneten Zeiten passen zu den Commits
  „Lauf … verworfen“ (R39, R47).
- **Rohbelege dieses Teils** (alle nur lesend): R39 (git, Dateibesitzer, Anmeldungen), R45 und R46 (Suchwörter in den
  Meldungen), R47 (Laufliste aus der Kasse), R52 (Zählung „weitergereicht“), R54 (Liste nach T3), R78 (Nachlese). Dazu
  Einzelabfragen am 25.09. um 16:52: `git show --stat` für `e77cead` und `67457ac`, `git rev-parse --verify -q refs/stash`
  (kein Stash), `ls -la /tmp/review-vor-t4-04/`, `df -h /`.
- **Nachrichten Philipps:** Maßgeblich ist das berichtigte Verzeichnis `arbeit/verlauf/v2/` (Anzahl und Berichtigung:
  Teil 3, FK42 Nr. 12). Die Einträge id 655, 657, 1959, 3559, 16285 und 16712 in
  `arbeit/lesen/philipp-ab-2026-09-18.md` sind keine Nachrichten Philipps und werden hier nicht als solche verwendet.
- **Meldungen von Hermes** sind mit Zeit und id aus `arbeit/lesen/hermes-an-philipp.md` zitiert, kurz „Meldung 22.09.
  15:25:05, id 11504“.

## FK08 — Was wurde seit dem 18.09. gelöscht, zurückgebaut, verworfen oder zurückgezogen?

**Kurzantwort.** In der git-Geschichte von `/root/biotop` ist nichts gelöscht worden: 0 gelöschte Dateipfade,
0 Umbenennungen und kein Revert-Commit über alle Commits (R39, Z. 49–52, abgelesen). Verworfen wurden 6 Läufe und
1 Reviewdurchgang; ein weiterer Reviewdurchgang wurde nicht verwendet. Hermes hat ein Messergebnis gestrichen, drei
Dateien wurden überschrieben, und Chat-Claude hat das Handelssystem und den Punkt W3 zurückgezogen. Zurückgezogene
Aussagen und Zahlen stehen unter FK13.

### A. git

- **Commit-Nachrichten mit Rückbau-Wörtern:** 6 (R39, Z. 53–58, abgelesen). Vier davon verwerfen Läufe (Abschnitt B).
  `b499747` (19.09. 04:55) setzt im Code einen Kandidatenstatus vor der Paarprüfung zurück; das ist eine Codeänderung,
  kein Rückbau. `e77cead` (19.09. 21:55, „Altbestand aus Phase 3 entfernt“) ändert nur `biotop/organe/gedaechtnis.py`
  (42 Zeilen dazu, 1 weg) und legt `pruefung/proben_ausserhalb_gedaechtnis.py` an (`git show --stat`, 16:52). Entfernt
  wurden also Gedächtniseinträge, keine Dateien (Auslegung Hermes; Abschnitt C).
- **Reflog:** Genau ein Eintrag ist kein Commit: `67457ac HEAD@{2026-09-19 15:10:15 +0200} reset: moving to HEAD`
  (R39, Z. 60). Ein solcher Reset verwirft nicht gesicherte Änderungen im Arbeitsbaum. Was er verworfen hat, ist
  UNBEKANNT; einen Stash gibt es nicht (16:52). Weg zur Klärung: der Verlauf vom 19.09. zwischen 15:00 und 15:15 in
  `arbeit/verlauf/v2/wortlaut.jsonl`.
- **Beinahe-Löschung am 21.09.:** Beim Anlegen der T3-Commits „wären 11 Vorbedingung-1-Prüfskripte fälschlich als
  gelöscht in Commit 2 gelandet — zurückgeholt“ (Meldung 21.09. 12:16:00, id 10719). Die Zählung „0 gelöschte Pfade“
  (R39) passt dazu. Eine Sicherung des Repos vor diesen Commits liegt laut derselben Meldung unter
  `/root/biotop-t3/repo-sicherung-vor-commits`.

### B. Verworfene Läufe

Die Kasse führt 6 von 38 Läufen (Stamm 1–25, T3 26–38) mit dem Status `verworfen` (R47, Z. 83, abgelesen). Alle sechs
stammen vom 19.09. aus Phase 3.

| Lauf | Zeit (CEST, gerechnet) | Grund laut Quelle | Beleg |
|---|---|---|---|
| 14 | begonnen 13:03, kein Ende eingetragen | „F4: Äquivalenz-Raster (beobachten) erweitert, laut scheitern; Mutanten Phase 3 versiegelt; Lauf 14 verworfen“ | Commit `3282ed2`, 13:08 |
| 15 | begonnen 13:09, kein Ende eingetragen | „Verhandlung hängt an der Benennung; Schritt 2 vor Kandidatentests; Lauf 15 verworfen (Satz 2 F4)“ | Commit `8d23ce2`, 13:25 |
| 16 | 13:26–16:40 | In der Kasse mit „In dieser Richtung gesättigt …“ beendet und als `verworfen` geführt. Der Masterprompt nennt den Anlass einer Regeländerung: „Hermes konnte Lauf 16 nicht stoppen und er lief weiter“ | R47 Z. 59; v8 Z. 41 |
| 18 | 16:41–17:05 | „Satz 2 F4: gescheiterte Wege aus verworfenen Laeufen zaehlen nicht; Lauf 18 verworfen“ | Commit `38fde3d`, 17:05 |
| 19 | 17:06–17:39 | „Kurven-Skript; Lauf-20-Skript; Lauf 19 verworfen“; in der Kasse „In dieser Richtung gesättigt …“ | Commit `8565ddb`, 17:55; R47 Z. 62 |
| 21 | 22:34, Dauer 0 s | „Hermes (satz2): Ankläger-Ablauf während des Laufs geändert (Prüfung)“ | R47 Z. 64 |

- **Auf wessen Anweisung:** Hermes selbst, nach Satz 2 des Masterprompts: Ändert sich das Messgerät, beginnt ein neuer
  Lauf (Auslegung Hermes aus den Commit-Nachrichten „Satz 2 F4“ und „satz2“).
- **Wiederherstellbar:** Die Läufe sind nicht gelöscht. Sie stehen mit ihren Buchungen in der Stammdatenbank (R25, R47).
  Gescheiterte Wege aus verworfenen Läufen zählen seit `38fde3d` im Projektgedächtnis nicht.
- Kosten der Läufe → CHRONIK (FK20) und KASSE.

### C. Gedächtniseinträge

- **Probenkandidaten aus Phase 3** wurden aus dem Projektgedächtnis entfernt (`e77cead`, 19.09. 21:55). Grundlage ist
  die Regel „Proben kommen in kein Gedächtnis (Fassung 6)“ (v8, Z. 243). Ob die Einträge gelöscht oder nur gesperrt
  wurden und ob sie wiederherstellbar sind, ist UNBEKANNT. Weg: `git show e77cead` lesen und die Stammdatenbank nur
  lesend nach dem Merkmal `ist_probe` abfragen.
- **Zwei echte Normtests** (`norm_k2081_bericht`, `norm_k2082_bericht`) hat Hermes am 19.09. bei einer Mechanikprüfung
  am echten Bestand versehentlich archiviert. Hermes meldete das als eigenen Fehler und setzte beide auf `offen_norm`
  zurück, protokolliert als `immun.archivierung_zurueckgenommen` (Meldung 19.09. 23:42:31, id 2687). Laut Meldung
  wiederhergestellt; in Teil H nicht nachgemessen.

### D. Masterprompt, Aufträge, Regeln

- **Handelssystem gestrichen (Fassung 7, 21.09.).** Wortlaut aus dem Änderungsverzeichnis: „Das Handelssystem stand in
  den Fassungen 1 bis 6 als Phase-4-Werk, war aber eine nie bestätigte Vorentscheidung von Chat-Claude; alle darauf
  bezogenen Bezugsgrößen […] sind gestrichen. **Fehler von Chat-Claude:** …“. Grund: „Philipps Entscheidung — das
  Biotop soll für jeden Anwendungszweck taugen und dafür in allen Bereichen geprüft sein“ (`arbeit/fassungen/
  aenderungen-v7.md`, Z. 2). Wiederherstellbar: Die Fassungen 1 bis 6 liegen im Wortlaut in `arbeit/dokumente/`.
  Einzelheiten → ENTSCHEIDUNGEN (FK15).
- **Punkt W3 („Tresor“) zurückgezogen.** Philipp, 20.09. 05:01:19 (id 3148): „den Tresor gibt es nicht, und du sollst
  auch keinen bauen […] mein Punkt W3 war mein Fehler, ich habe seine Existenz angenommen statt gemessen, und er ist
  hiermit zurückgezogen.“
- **Ausnahme im Skill gestrichen.** Hermes hatte in den Skill `measurement-harness-discipline` eine Ausnahme
  geschrieben, nach der ein gesperrter Befehl über den Weg ausgeführt werden durfte, den die Sperrmeldung nennt. Am
  23.09.: „Das war eine Freigaberegel, und die setzt nur du. Ich habe die Ausnahme eben gestrichen.“ (Meldung 23.09.
  07:21:57, id 12293; gleichlautend 09:44:14 und 12:09:16). Anlass war Philipps Regel zu Sperren (Teil 3, FK41 Nr. 1).
  Ob die alte Fassung des Skills erhalten ist, ist UNBEKANNT.

### E. Reviews

- **Runde 4 (24.09.): zwei Durchgänge, einer davon unveröffentlicht.** Ein Durchgang liegt als
  `/root/biotop-vor-t4-04/REVIEW.md` vor (laut Meldung entstanden um 16:42:10, 33.169 Bytes), der zweite als
  `/tmp/review-vor-t4-04/REVIEW-B.md` (30.465 Bytes, 16:59; `ls`, 16:52). Der zweite Reviewer meldete:
  „`/root/biotop-vor-t4-04/REVIEW.md` stammt nicht von mir. […] Offenbar lief eine zweite Instanz desselben Auftrags auf
  meinem Verlauf und meinem `/tmp`-Ordner.“ (Meldung 24.09. 17:00:16, id 16498). Der Bericht der Runde 4 nennt „Ein
  Reviewdurchgang (`REVIEW.md`)“ (BERICHT Z. 4 und 244); veröffentlicht ist nur `REVIEW.md` (R78, Abschnitt I). Eine
  Verwerfung von `REVIEW-B.md` oder eine Anweisung dazu: NICHT GEFUNDEN. Die Datei liegt nur in `/tmp` (Risiko: Teil 3,
  FK43 Nr. 4).
- **Runde 5 (24.09.): erster Durchgang verworfen.** Philipp, 24.09. 23:15:27 (id 16901): „Es gilt das zweite Review
  (/tmp/review-vor-t4-05/REVIEW.md) […]. Das erste bleibt im Ordner als verworfen“. Er liegt als
  `/root/biotop-vor-t4-05/REVIEW-verworfen-erster-durchgang.md` vor. Was nur er fand, steht als U-1 bis U-4
  „unbestätigt“ auf der Liste (`ZWEI-REVIEWS.md`, Z. 33–35; Teil 2, FK39). Philipps Begründung wurde später berichtigt,
  die Wahl blieb (FK13 Nr. 22).
- **Runde 5: überschriebenes Skript.** Die zweite Instanz überschrieb um 22:02:32 das Skript `abschluss.sh` der ersten;
  die erste hatte es um 21:52:25 ausgeführt. Das Skript las nur Dateilisten und Zeitstempel (`ZWEI-REVIEWS.md`,
  Z. 17–18 und 27–29). Ob die erste Fassung erhalten ist, ist UNBEKANNT (Weg: Delegationsprotokoll
  `bau/REVIEW1-DELEGATIONSPROTOKOLL.txt`).

### F. Runde 6 (25.09.)

- **`VORHER-NACHHER-S3` gestrichen** (686 von 687 gleich). S3 hatte um 03:10:38 eine Sperre des Gateway-Wächters
  umgangen (`sperre/SPERRE-02-S3-gateway-waechter.md`). Eigene Entscheidung Hermes um 05:02: „VORHER-NACHHER-S3
  endgültig gestrichen (Ergebnis einer Umgehung zählt nicht; Kette misst neu)“ (UEBERGABE Runde 6, Z. 153–155 und
  164–165; Meldung 05:07:37, id 18619). Die Datei `bau/VORHER-NACHHER-S3.txt` liegt weiter im Ordner, gilt aber nicht
  als Beleg. Die Übergabe hatte zuvor festgehalten, sie gelte nicht „bis Philipp entscheidet“ (Z. 155); eine
  Entscheidung Philipps dazu: NICHT GEFUNDEN.
- **`bau/lesen_s4g.sh` überschrieben**, von Hermes um 09:43 (eigener Fehler). „Die S4-Fassung ist aus der
  Sitzungsdatenbank bytegleich wiederhergestellt.“ Über alle Sitzungen der Runde 6 wurde nur diese eine von 231 Dateien
  von mehr als einer Sitzung beschrieben (Meldung 09:59:50, id 20500; gleichlautend 14:49:16).
- **Beleg eines stillen Durchlasses überschrieben.** Die Übergabe nennt einen gemessenen stillen Durchlass über
  `_Konto.buchen` („0 Abweichungen, tragfähig“) mit dem Vermerk „(07:42, Beleg überschrieben)“ (UEBERGABE Runde 6,
  Z. 173–175). Auf wessen Handlung und ob der Beleg wiederherstellbar ist: UNBEKANNT; Weg: `bau/S1-PLAN.md` und der
  Verlauf der S1-Fortsetzung in `arbeit/verlauf/v2/wortlaut.jsonl`.
- **Zwei Kommentarblöcke in `config.yaml` entfallen.** Bei der Umstellung der Verdichtung auf OpenRouter (Freigabe
  Philipp 25.09. 01:06:55, id 17359) schrieb `hermes config set` die Datei neu und „ließ zwei auskommentierte
  Vorlageblöcke weg (Security, Fallback Model — reine Kommentare, `diff` zeigt sie)“. Vorher war die Datei datiert
  gesichert (UEBERGABE Runde 6, Z. 127–129). Wiederherstellbar: ja, aus dieser Sicherung.

## FK09 — Hat außer Hermes jemand am Biotop gearbeitet oder Dateien geändert?

**Kurzantwort: keine andere Person und kein anderer Agent ist belegt.** Gearbeitet haben die Hauptsitzungen von Hermes
und ihre Subagenten (Bauende und Reviewer); Subagenten sind Hermes. Zweimal arbeiteten zwei Hermes-Instanzen
gleichzeitig am selben Auftrag (Runden 4 und 5, unten).

- **Commit-Autoren:** Alle 75 Commits seit dem 18.09. stammen von Hermes, in drei Schreibweisen:
  19 × `Hermes (Biotop) <hermes@biotop.local>`, 46 × `hermes <hermes@biotop>`, 10 × `hermes <hermes@local>`. Autor und
  Committer sind jeweils gleich (R39, Z. 61–64, abgelesen; Summe gerechnet 19 + 46 + 10 = 75, wie in R13).
- **Dateibesitzer:** 3.030 von 3.030 Dateien unter `/root/biotop` (ohne `.git` und Zwischenspeicher) gehören
  `root:root`, mit `.git` 4.047 von 4.047 (R39, Z. 65–68, abgelesen). Auch alle Arbeitsordner der Runden und Reparaturen
  gehören `root:root` (R39, Z. 104–116). Auf dem Server hat nur das Konto `root` eine Anmeldeshell (R39, Z. 121–122).
  Der Besitzer unterscheidet deshalb nicht zwischen Hermes und einem Menschen, der als `root` arbeitet.
- **Änderungszeiten:** Die jüngsten Dateien im Baum stammen vom 25.09. bis 15:18 (Code und Tests der Runde 6), dazu
  `daten/biotop.db-shm` um 15:55 (R39, Z. 78–103). Sie passen zu den Bauenden der Runde 6.
- **Anmeldungen am Server:** `wtmp` verzeichnet am 18.09. zwischen 21:44 und 01:25 (19.09.) 8 Terminalanmeldungen als
  `root`, danach bis zum Lesen am 25.09. um 16:13 keine (R39, Z. 124–131, abgelesen). Wer sich angemeldet hat, verzeichnet
  `wtmp` nicht. In dieselbe Zeit fallen zwei kurze CLI-Sitzungen „Modellkennung nennen“ um 22:57 und 22:58 (R12,
  Z. 76–77). Ob bei diesen Anmeldungen Biotop-Dateien geändert wurden, ist UNBEKANNT; Weg: Philipp fragen.
- **Sitzungen:** Alle 54 Sitzungen, die R12 ab dem 17.09. aufführt, tragen eine der Quellen `telegram` (Philipps Chat
  mit Hermes), `cli` (kurze Prüfsitzungen wie „Modellkennung nennen“ und „OK“) oder `subagent` (abgelesen mit
  `search_files` am 25.09. um 17:45: 54 Treffer für `'source': '`, 54 für diese drei Quellen, 0 für andere). Eine
  Sitzung einer anderen Instanz oder eines anderen Zugangs ist nicht verzeichnet. Wem die Sitzungen gehören, gleicht
  Hermes mit INVENTAR ab.
- **HERMES-2, HERMES-3, Iolo:** HERMES-2 und HERMES-3 nennt Philipp einmal, als Regel für das Gedächtnis: „nur HERMES-1
  schreibt, während HERMES-2 und 3 lesen“ (20.09. 05:01:19, id 3148). „Iolo“ kommt in keiner Nachricht und keiner Meldung
  vor, nur im Auftrag BIOTOP-LAGE-01 (Suche in `arbeit/`, Teil H). Eine Änderung durch sie ist nicht belegt.
- **Philipp direkt:** Eine Änderung von Dateien oder Code durch Philipp ist nicht belegt; es gibt keinen Commit mit einem
  anderen Autor. Philipp erteilte Freigaben, etwa für die Sicherung und Umstellung der `config.yaml` (25.09. 01:06:55,
  id 17359).
- **Zwei Hermes-Instanzen gleichzeitig:**
  - Runde 4, 24.09.: Der Reviewer fand im Rundenordner eine fremde `REVIEW.md` und in seinem `/tmp`-Ordner ein fremdes
    `abschluss.sh` (Meldung 17:00:16, id 16498; FK08 E).
  - Runde 5, 24.09.: Ab 21:51:24 beantwortete „eine zweite Instanz den Chat — auf der Sitzung des Reviewers, mit dessen
    bisherigem Verlauf“; beide Instanzen schrieben in denselben Ordner (`ZWEI-REVIEWS.md`, Z. 16–18).
  - Nach der Berichtigung durch Hermes vom 25.09. trugen die Sitzungen `…150913_a9326d` und `…203120_e6c401` den Chat
    erst ab 16:10:41 bzw. 21:51:24. Ihre ersten Einträge (id 16285, 24.09. 15:09:13; id 16712, 20:31:20) sind
    Reviewaufträge von Hermes an Subagenten, keine Nachrichten Philipps.
- **Nebenbefund:** `daten/biotop.db-shm` im Baum hat die Änderungszeit 25.09. 15:55 (R39, Z. 103), also während
  BIOTOP-LAGE-01. Wer die Datenbank um diese Zeit geöffnet hat (S1c oder ein Leser ohne `immutable`), ist UNBEKANNT.
  Weg: Hermes prüft die Rohbelege um 15:55 und fragt S1c.

## FK13 — Berichtigungen seit dem 18.09.

Je Berichtigung stehen alt, neu, Grund und Quelle; zitiert wird wörtlich. Geltende Torzeilen-Werte stehen in `TORE`,
Beträge in `KASSE`; hier stehen sie nur als Gegenstand einer Berichtigung (Hermes gleicht beim Einsetzen ab).

**19. und 20.09. (Phasen 2 und 3, Nachlauf)**

1. **Doppelungsanteil Phase 2, Bezugsgröße.** Alt: 2,5 %. Neu: „richtig 10,9 % bei gleicher Lesart“; mit Chat-Claudes
   Lesart (Doppelungsschlüssel = Behauptung) 83,6 %. Grund: „meine damalige Bezugsgröße war falsch gewählt
   (240 Ablehnungen statt 55 erzeugte Tests …)“. Hermes, Meldung 19.09. 19:26:48, id 2230.
2. **Doppelungsanteil Lauf 13.** Alt: 83,6 %. Neu: 68,5 %. Grund: „Die 83,6 % aus meinem Phase-3-Bericht waren eine
   Heuristik; mit dem gebauten Schlüssel sind es 68,5 %. Deine Wertung ‚Zeile 8 gerissen‘ bleibt damit richtig, die
   Zahl korrigiere ich.“ Hermes, Meldung 19.09. 22:38:16, id 2563.
3. **Torzeile Projektgedächtnis, Phase 3.** Alt: „teilweise“. Neu: erfüllt. Grund: „Die drei strittigen Fälle: 0 von 3
   durchgerutscht. Zwei beruhten auf meiner gröberen Ableitung, einer auf einem Weg aus dem verworfenen Lauf 16. Die Zahl
   des Biotops war richtig, meine Nachrechnung war falsch“. Hermes, Meldung 20.09. 00:00:28, id 2717. Der Masterprompt
   übernimmt das: „Projektgedächtnis (Fassung 6 nach oben korrigiert …)“, Wertung „8 von 11 voll, 1 teilweise, 2 im
   Nachlauf erledigt“ (v8, Z. 410); sein Änderungsverzeichnis nennt für Phase 3 noch „Wertung Chat-Claude 7 von 11“
   (v8, Z. 46). Geltende Wertung → TORE.
4. **Doppelungsanteil Lauf 20.** Alt: 63,6 %. Neu: 75,0 %. Grund: „7 der 11 gezählten Tests waren übernommener
   Altbestand. Richtig: 4 erzeugte Tests“; „Dieselbe Fehlerklasse wie bei Lauf 24; ich hatte sie beim ersten Mal nur an
   einer Stelle korrigiert.“ Folge: „Tor 2 Zeile 8 bleibt ungemessen und steht für Tor 4. Der alte BERICHT.md trägt
   jetzt einen Berichtigungsvermerk“. Hermes, Meldung 20.09. 01:55:40, id 2901.
5. **Titel eines Nachlaufberichts.** Alt: „N1 bis N6“, obwohl N7 bis N9 enthalten waren. Neu: Titel berichtigt; N2 und
   N5 tragen Berichtigungsvermerke „mit Verweis auf den maßgeblichen Abschnitt“. Hermes, Meldung 20.09. 02:29:49,
   id 2962.
6. **Kasse Phase-3-Nachlauf (W2).** Alt: Erklärung „nur Rundung“ und der Fortsetzungswert 0,1190 €. Neu: „Nach
   Rohbuchungen bleibt der geführte Stand rund 1,299 € von 3 €, frei rund 1,701 €. Die Erklärung ‚nur Rundung‘ stimmt
   nicht; die alte Fortsetzungszahl war falsch.“ Hermes, Meldung 20.09. 05:18:37, id 3215; ebenso STAND-01: „der früher
   genannte Fortsetzungswert 0,1190 € passt nicht zur DB. Abgrenzung von Lauf 23 noch offen“ (R31, Z. 141). Ob damit
   auch der Kassenstand der Vorbedingung 1 von 1,6970 € (STAND-01, R31, Z. 165) ersetzt ist, ist nicht aufgelöst
   (Teil 3, FK42 Nr. 3).
7. **Punkt W5 (Modellwahl).** Hermes stellte fest, dass `/model` nur einen Sitzungs-Override schreibt, der bei `/new`
   gelöscht wird; der Grundwert in `config.yaml` bleibt („Nebenbefund, der W5 berichtigt“, Meldung 20.09. 05:57:03,
   id 3338).

**21. bis 23.09. (T3)**

8. **Erklärung des Medians.** Alt: „der erste Aufruf treibt die Spannweite über 1,5“. Neu: „Ein einzelner erster
   Ausreißer bewegt den Median aus drei Werten nicht.“ Grund: Einwand von Philipp/Chat-Claude („Ihr Medianeinwand ist
   richtig, meine Erklärung war falsch“). Hermes, Meldung 21.09. 06:26:33, id 10525.
9. **Test `test_t3_generation0.py`.** Er erwartete für einen unbestätigten Testfehler einen `RuntimeError` und schrieb
   damit fehlerhaftes Verhalten fest. „Der Test war falsch, nicht der Code — korrigiert mit Begründung im
   Parametersatz.“ Hermes, Meldung 21.09. 18:46:07, id 11008.
10. **Kernmaß T3, Lauf 37.** Alt: gemeldet −28 → −14. Neu: „Kernmaß ohne die Fehlalarm-Regel: −11 → 0“; „Von 14 Punkten
    Gewinn sind 11 echt (S1 mit 10 Punkten, tote Funktion S4 mit 1) und 3 Fehlalarm-Bereinigung.“ Grund: Die Regel
    `detect-object-injection` schlägt auch am sauberen Vergleichsbereich an. Hermes, Meldungen 22.09. 15:18:58
    (id 11483) und 15:25:05 (id 11504).
11. **Folgenlose Umformungen in `zahlen`.** Alt: Alle `zahlen`-Änderungen seien folgenlose Umformungen. Neu: „Der Review
    hat meine zentrale Schlussfolgerung gekippt — zu Recht.“ Gen 6 (K2934) baute einen echten Fehler ein
    (`quantil(werte, 1)` liefert 3 statt 300). Im selben Zug: „Der Nachweis-Hash gehörte zu Lauf 35 statt 37“ und „‚5 neue
    Tests aus Angriffen‘ war doppelt falsch — 2 aus Angriffen, 3 aus einem Kandidatendiff“. Hermes, Meldung 22.09.
    15:25:05, id 11504.
12. **35,1 % als Torzeile → Diagnose.** Alt (15:18:58, id 11483): „Auf der Ansagen-Ebene liegt Python bei 43,5 %
    (10 von 23), TypeScript bei 35,1 % (20 von 57)“; „in der Aufnahmesperre finde ich in beiden Läufen 0 von 0“. Neu
    (15:43:02, id 11556): „meine 35,1 % waren die falsche Ebene. Die Berechnung aus Vorbedingung 1 steht in
    `belege/TORZEILEN.json`: Nenner sind erzeugte Angriffstests, beurteilt nach der geschriebenen Behauptung. Mit der
    Aufnahmesperre C gemessen: TypeScript 2 von 14 = 14,29 %, Python 0 von 3 = 0 % […] Die 35,1 % sind die Sperrquote des
    Ansagefilters, eine Diagnose.“ Dazu: „Mein ‚0 von 0‘ war ein Auswertungsfehler (falsches Feld gelesen).“ Geltender
    Wert → TORE; eingearbeitet in ABSCHLUSS-03.
13. **Bezugsgröße der 9,09 % (WS11: „Tor 2 Zeile 8 ist erfüllt (9,09 %)“).** Alt (Hermes, 22.09. 15:25:05, id 11504):
    „Die 9,09 % aus Vorbedingung 1 („1 von 11“) kann ich keiner Bezugsgröße zuordnen“. Neu (15:43:02, id 11556): „Die
    Berechnung aus Vorbedingung 1 steht in `belege/TORZEILEN.json`“. Abgelesen in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/
    nach-reparatur-02/abschluss-02/TORZEILEN.json`, Z. 3–21: 11 Tests, 1 Doppelung, `anteil_prozent` 9.0909…,
    `unter_20_prozent` true, Maßstab „Philipps ausdrücklicher enger Nachtrag: K2689 ausgeführt, Anteil strikt
    unter20Prozent und vollständiger Review“, `zeile_im_engen_nachtrag_erfuellt` true, `gesamtfreigabe_biotop` false.
    Berichtigt wurde damit die Aussage über die Bezugsgröße, nicht die 9,09 %; eine Berichtigung der 9,09 % selbst:
    NICHT GEFUNDEN. Der Masterprompt führt sie unverändert (v8, Z. 18). Für T3 steht dieselbe Torzeile auf „nicht
    gemessen“ (ABSCHLUSS-03 §4e, Z. 256). Geltende Werte → TORE.
14. **Lauf 38 ohne Abwehr.** Alt (15:43:02, id 11556): „Alle drei Punkte erledigt, Lauf 38 läuft“, mit Gegenproben „am
    echten Lauf“. Neu (22.09. 21:29:37, id 11574): „Ich habe `verhaltensvergleich` und `masseichung` gebaut, getestet,
    committet — und **nie in den Prüfpfad eingehängt**. […] Lauf 38 lief ohne die Abwehr.“ Folge laut derselben Meldung:
    K3121 baute denselben Fehlertyp erneut ein (`spannweite` 8 statt 80).
15. **Umgang mit einer Sperre.** Alt (22.09. 15:43:02, id 11556): „Ein Befehl wurde unterwegs als unparsbare Payload
    blockiert; ich habe ihn über den vom System ausgewiesenen Weg ausgeführt, nicht umformuliert.“ Neu (23.09. 07:21:57,
    id 12293): „Meine Reaktion damals war falsch. Ich habe das gespeicherte Skript mit dem Befehl ausgeführt, den die
    Meldung nennt. Nach deiner Regel ist das ein anderer Weg zum selben Ergebnis.“ (FK08 D).
16. **T3-Stand im Masterprompt.** Alt (v8, Z. 458): „Lauf 38: 4 von 5 = 80 %, S2 dabei nicht belastbar.“ Neu (BERICHT
    Runde 2, §12 Nr. 3; R78 A2): „ist nach Entscheidung 1 zu korrigieren auf 3 von 5 = 60 % (Lauf 37: 2 von 5 = 40 %)“.
    Im Masterprompt nicht nachgeführt (Teil 3, FK42 Nr. 4).
17. **ABSCHLUSS-03 (T3), Review Nr. 2:** „Verhaltensvergleich urteilt ohne Beobachtung (K3106: 0 von 7) | bestätigt, §2
    berichtigt“ (ABSCHLUSS-03, Z. 406; R54). Alt und neu im Einzelnen stehen in ABSCHLUSS-03 §2.

**23. bis 25.09. (Runden vor T4)**

18. **Runde 1, Entwurf von 18:18.** BERICHT Runde 1, §8 „Zurückgezogene oder berichtigte Aussagen“ (R78 A1), wörtlich:
    - „Alle elf Vorbedingungen sind gebaut“ → gebaut für den TypeScript-Pfad. Für Python fehlt der Verhaltensvergleich
      (Nr. 2), und der Python-Zweig von Nr. 1 ist nur einmal ausgeführt.
    - „Offen aus dem Auftrag: nach meiner Prüfung nichts“ → zurückgezogen (§2, Nr. 8a).
    - „Gestellt ist nur die Kammergrenze“ (Nr. 3) → gestellt waren Kammer, Messgerät und Modell.
    - „Vorgeneration 4,80“ → ein gestellter Testwert, keine Messung.
    - „K2868 Durchgang 2 überlebt, 12 von 12 gedeckt“ → stimmt als Ausgabe des Organs. Die Deckung gilt aber je Funktion,
      und der Kandidat ändert gültiges Verhalten (§2).
19. **Verdichtung im Gateway.** Alt: Sie laufe wieder. Neu: „Meine Aussage aus der Vorrunde, sie laufe wieder, war
    falsch; sie stimmte nur für einen frischen Prozess.“ Grund: weiter „Error code: 401 … OAuth access token has been
    revoked“. Hermes, Meldung 24.09. 01:10:58, id 14919; wiederholt 02:10:34, 02:15:47 und 05:10:02.
20. **Die fünf Lücken der Python-Sonde.** Alt: geschlossen. Neu: „für ihre Probenfälle geschlossen“, der Bericht steht
    auf „nicht abgenommen“. Grund: „Auch Tests, die ein Kandidat mitbringt, können decken.“ Hermes, Meldung 24.09.
    08:50:22, id 15961.
21. **Nachspiele an `1d9a5aa`.** „An `1d9a5aa` brachen alle 7 Nachspiele ohne Urteil ab. Ein Import hatte im Nachspiel
    die Maßeichung überschrieben, und die Regression prüft keine Nachspiele.“ Behoben und mit einem Test abgesichert.
    Hermes, Meldungen 24.09. 15:09:22 (id 16290) und 16:10:36 (id 16441).
22. **Begründung der Review-Wahl, Runde 5.** Alt (Philipp, 24.09. 23:15:27, id 16901): Beim ersten Review sei „nicht
    auszuschließen, dass es das überschriebene Skript ausgeführt hat“. Neu (Hermes, 25.09. 00:24:43, id 17210): „Laut
    Delegationsprotokoll hat das erste Review das überschriebene Skript nicht mehr ausgeführt, und die Kammermessungen
    stammen von vor der Teilung. Die Wahl des zweiten ändert das nicht.“ Philipp (00:27:35, id 17217): „mein Grund für die
    Wahl des zweiten war falsch, die Wahl bleibt.“ Ebenso `ZWEI-REVIEWS.md`, Z. 37–39.
23. **Abweichung von Entscheidung 3, Runde 5.** Philipp/Chat-Claude (24.09. 21:00:41, id 16769): Die Abweichung „bei
    unvollständiger Erfassung enthält sich der ganze Vergleich“ widerspricht Entscheidung 3. Hermes (21:08:23, id 16793):
    „Im Bericht steht §13 Nr. 1 jetzt als falsche Entscheidung und §14 Nr. 7 als eigener Fehler.“ Folge: R6-1. Dazu
    (21:51:18, id 16871): „Meine Vorprobe hatte nur Zusicherungen mit Text geprüft. Das steht als eigener Fehler im
    Bericht.“ Folge: R6-4.
24. **Bericht Runde 5, §6:** „der gemischte Nenner in §6 ist berichtigt“ (Meldung 25.09. 00:24:43, id 17210). Alt und neu
    hat Teil H nicht gelesen (Weg: `/root/biotop-vor-t4-05/BERICHT.md` §6).
25. **Zusammenfassung der Verdichtung, Runde 6.** Die Verdichtung um 01:11 lieferte eine Zusammenfassung „mit
    2 Fehlzuordnungen (Freigabe als ‚Runde 6‘, U-1…U-4 als ausstehend) — der Stand gilt aus DIESER Datei“ (UEBERGABE
    Runde 6, Z. 134–135).

26. **Auftrag an S1 zu eng.** „Meine Engführung im Auftrag S1 (‚nur unvollständig/Ausfall/Zeitgrenze‘) war der Fehler.“
    Folge: M2(b) kam in die Runde 6 (S1b). Eigene Entscheidung Hermes, 25.09. 08:50 (UEBERGABE Runde 6, Z. 178–180).

**Durch Chat-Claude.** Philipps Nachrichten geben Chat-Claudes Prüfungen und Entscheidungen weiter; „mein Fehler“ meint dort
Chat-Claude (Auslegung Hermes aus dem Wortlaut, etwa „Entscheidung Chat-Claude“, 22.09. 15:32:32).

27. **Rauschen in `formeln`.** Alt: 47 % Eigenrauschen, Begründung einer Regel in Fassung 5. Neu: „Die 47 % waren nie
    Eigenrauschen — mit Median und getrimmter Spannweite sind es 11 %; meine Fassung-5-Begründung war gegen eine
    verfälschte Messung gesetzt“. 19.09. 21:21:10, id 2292.
28. **Ausnahme für Abbrüche.** Alt: Abbrüche seien vom Freigabe-Gate ausgenommen. Neu: „Für jede Pflicht muss es einen
    benannten Befehl geben“. Grund: „Ich hatte ‚vom Gate blockiert‘ aus deiner Phase-3-Meldung übernommen und daraus eine
    Ausnahmeregel gebaut, ohne nachzusehen, was genau blockiert wurde — das Gate hatte recht, es fehlte der Befehl.“
    19.09. 22:36:12, id 2544. In v8 als Grundsatz 2 übernommen (Z. 119); der alte Grund steht dort weiter (Teil 3,
    FK42 Nr. 5).
29. **Doppelungszahlen der Läufe 20 und 22.** „63,6 → 54,5 liest sich sonst als kleine Verbesserung, obwohl 6 von 11
    abgefangen wurden“; die Bezugsgröße gehört dazu. 19.09. 23:39:45, id 2664.
30. **W4.** „Mein W4 zielte auf den falschen Betriebsweg.“ 20.09. 05:25:18, id 3218 (gleichlautend id 3223).
31. **Norm-Zeile und Eichproben.** „Wertungen, die ich zurücknehme: die Norm-Zeile aus Tor 2 und ‚4 von 4 bestanden‘ aus
    dem Nachlauf waren ein leerer Durchlauf (masse statt mass, norm=[]); die Zahlen aus den Läufen 22 und 23 stehen
    wegen des Satz-2-Verstoßes unter Vorbehalt, darunter die 54,5 %.“ 20.09. 15:28:25, id 4317.
32. **Reparaturauftrag eingegrenzt.** „das ist mein Fehler, nicht deiner: Ich habe sechs Punkte in einen Auftrag
    gepackt, ohne den Kern zu kennzeichnen.“ 20.09. 17:34:38, id 6108. Folge: vier Phase-4-Lücken auf der Liste
    (Teil 2, E).
33. **„Eine Fehlerklasse in zwei Bauarten“ (T3).** „laut eigener Kassentabelle starben nur 31, 32 und 36 daran, 27 und 28
    am Rauschen, 29, 30 und 35 an Ausfällen ohne Klärungsweg“; zur eigenen Vorgabe: „die Musterliste nur aus
    Python-Syntax war meine zu enge Vorgabe“. 22.09. 14:52:53, id 11301.
34. **Vergleich mit den 9,09 %.** „mein Vergleich mit den 9,09 % war falsch, weil er zwei verschiedene Größen verglich“.
    22.09. 15:32:32, id 11505.
35. **Abwehr für wirksam erklärt.** „der Fehler ist auch meiner: Ich habe die Abwehr für wirksam erklärt, weil die
    Gegenproben gegen das Modul liefen, ohne zu verlangen, dass sie durch den Lauf gehen.“ 23.09. 05:41:59, id 11575.
36. **S1 an K2868.** „S1 ist an K2868 damit nicht sauber behoben, das korrigiert den T3-Befund, und mein Prüfstein
    ‚K2868 muss bestehen‘ war falsch“. 23.09. 22:32:40, id 14624. Geltende Schwächenzählung → TORE.
37. **Stufe-2-Last.** „mein Auftrag ‚bis eingang nicht mehr sperrt‘ war ein Fehler, er richtet die Last nach dem
    Ergebnis“. 24.09. 21:00:41, id 16769. Folge: R6-3.
38. Dazu der Grund der Review-Wahl (Nr. 22), das Handelssystem und W3 (FK08 D). Regelberichtigungen im Masterprompt
    („Fehler von Chat-Claude in Fassung 2/3“, v8 Z. 50 und 63) → ENTSCHEIDUNGEN (FK15).

**Grenze dieser Liste:** Gesucht wurde mit den Wörtern „gelöscht“, „zurückgenommen“, „rückgängig“, „gestrichen“,
„überschrieben“, „eigener Fehler“, „war falsch“, „widerlegt“, „berichtigt“ (R46) und in den Offen- und
Berichtigungsabschnitten der Berichte (R78). Berichtigungen ohne diese Wörter können fehlen.
