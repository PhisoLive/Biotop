# BIOTOP-LAGE-01 · Fassung 2 · START-02

| Feld | Wert |
|---|---|
| Kennung | BIOTOP-LAGE-01 |
| Fassung | 2. Auftragsdatei 41.239 B, SHA-256 `58ba8834b8c3ec08f8da2e18d3db056150c91c2841ed9aac349bcf2eba216b98`, gleich dem Original im Dokumentenspeicher (abgelesen, R171) |
| Stichzeitpunkt | **25.09.2026 17:29:59 CEST**: Ende des Baus S1c der Behebungsrunde 6 (Delegation `deleg_c88798ee`, begonnen 12:51:42, Endgrund `max_iterations`; abgelesen, R170) |
| Status | **IN ARBEIT** (Zwischenstand; gültig ist die höchste Nummer, START-01 bleibt unverändert) |
| Stand dieser Datei | 25.09.2026, etwa 19:30 CEST |
| Läuft ein Lauf? | Nein. 0 pytest-Prozesse, 0 Container, keine Kammer-Sperre. Seit dem Stichzeitpunkt sind 0 Einträge unter `/root/biotop` (ohne `.git/`) geändert (abgelesen, R156). |

## A. Weiterlauf ohne neue Nachricht (Nachsteuerung vom 25.09., 17:08)

**Warum nötig:** Ein Turn endet nach höchstens 150 Werkzeugrunden (`agent.max_turns: 150`, config.yaml Zeile 9; R113). Der nächste Turn beginnt nur mit einer neuen Nachricht in der Sitzung.

**So läuft es weiter:**
1. Vor dem Ende jedes Turns aktualisiere ich `/root/sicherung/biotop-lage-01/UEBERGABE.md`. Dann starte ich `/root/sicherung/biotop-lage-01/arbeit/wecker.sh <Sekunden> <Anlass>` als Hintergrundprozess mit Abschlussmeldung.
2. Endet der Wecker, legt das Gateway seine Abschlussmeldung als neue Nachricht in dieselbe Sitzung. Sie startet den nächsten Turn mit wieder 150 Runden.
   - Code: `gateway/run_notifications.py`, Zeilen 1762–1775.
   - Beleg: Seit dem 18.09. gab es in den Biotop-Sitzungen 45 solcher Abschlussmeldungen. Auf 41 von 45 antwortete Hermes binnen 120 s (abgelesen, R163 Teil 5). Die übrigen 4 von 45 sind nicht untersucht.
3. Ergebnisse von Subagenten kommen auf demselben Weg als eigene Nachricht. Im Zustellbuch stehen 30 Delegationen: 27 zugestellt, 2 verworfen (beide am 24.09., weil die Elternsitzung beendet war), 1 lief noch (R163 Teil 6). Um 19:04 war keine mehr offen (R170).
4. Jeder Turn endet nach spätestens etwa 100 Runden, also unter der Wächter-Schwelle von 110. Sonst legt der Zwischenbericht-Wächter einen Bericht in `laeufe/biotop-vor-t4-06/` an; nach der Rückstellung A3 zeigt er wieder dorthin.
5. Bis Meldung 2 bekommst du keine Nachricht mehr, außer an einer harten Linie.
   - Wecker-Turns enden mit der Antwort `[SILENT]`, und das Gateway stellt sie nicht zu (`gateway/response_filters.py` Zeilen 15 und 50–56, `gateway/run_turn.py` Zeilen 1767–1769). **Das ist noch nicht ausgeführt.** Die erste Anwendung ist der nächste Turn.
   - In Wecker-Turns steht kein Begleittext neben den Werkzeugaufrufen. Laut config.yaml (`display.interim_assistant_messages: true`) gehen Zwischentexte als eigene Nachrichten hinaus. In diesem Turn sind so Zwischentexte an dich gegangen; ihre Zahl folgt gemessen in Stand 03.
6. **Grenze:** Bleibt eine Wecker-Meldung aus (wie bei 4 von 45 ohne Antwort) oder wird die Sitzung zurückgesetzt statt verdichtet, steht die Arbeit bis zur nächsten Nachricht. Laut Nachsteuerung gilt dann jede Nachricht als „weiter“. Einstieg ist `UEBERGABE.md`, Abschnitt „Ablauf“.

## B. Berichtigungen

**B1. Fundstellen von `biotop/__main__.py` in R1: 190, nicht 193** (abgelesen, R114).
- 193 ist die Zeilenzahl von `grep -c` über den ganzen Beleg.
  - 2 von 193 Zeilen stehen im Kopf des Belegs, im wörtlichen Skripttext.
  - 191 von 193 stehen in der Ausgabe. Davon ist 1 die Überschriftszeile des Skripts, 190 sind Fundstellen.
- Die 190 Fundstellen sind 190 verschiedene Pfade:

  | Ordner | Fundstellen |
  |---|---|
  | `/root/reparatur-01` | 176 von 190 |
  | `/root/reparatur-02` | 10 von 190 |
  | `/root/biotop-t3` | 2 von 190 |
  | `/root/biotop` | 1 von 190 (die Arbeitsinstanz) |
  | `/root/phase-4-vorbedingung-1` | 1 von 190 |

**B2. Nachrichten Philipps:** In der Zwischenmeldung um 16:55 habe ich 114 genannt. Das war der Stand bis 16:41:36, und darin war eine leere Datenbankzeile mitgezählt (id 7468 vom 20.09., 0 Zeichen). Richtig waren bis dahin 113 Nachrichten mit Text (R132). Bis zum Stichzeitpunkt sind es 114; die 114. ist die Nachsteuerung von 17:08:20 (R160). Maßgeblich ist Abschnitt C.

**B3. Ende von S1c:**
- START-01 schätzte „etwa 16:15 bis 17:45, spätestens gegen 18:25“. Tatsächlich endete S1c um 17:29:59 an der Iterationsgrenze.
- Sein Schlussbericht nennt zehn Tests `test_w_g_*`, die seit 17:25 im Baum rot sind: Für einen weiteren stillen Durchlass (G) steht die rote Spezifikation, der Code fehlt (R170).

## C. Nachrichten der Sitzungsdatenbank ohne Doppelzeilen, bis zum Stichzeitpunkt

**Quelle:** `/root/.hermes/state.db`, Tabelle `messages`, nur lesend gelesen. Zeitraum 18.09.2026 00:00:00 bis 25.09.2026 17:29:59 CEST. Alle Zahlen sind abgelesen aus R160; R160 ersetzt R115, R132 und R158 (R158 trug im Kopf fälschlich „v2“).

**Doppelzeile:** jede weitere Zeile mit gleicher Sitzung, Rolle, gleichem Zeitstempel und gleichem Wortlaut wie eine frühere Zeile. Die Werkzeugargumente zählen nicht mit, weil spätere Abschriften sie gekürzt tragen (377 von 378 Paaren; R131 Teil d).

| Stufe | Anzahl | Aufteilung |
|---|---|---|
| Datenbankzeilen im Zeitraum | 24.602 | tool 14.512 · assistant 9.636 · user 448 · session_meta 6 |
| Doppelzeilen | 2.044 von 24.602 | assistant 1.428 von 9.636 · tool 545 von 14.512 · user 71 von 448 |
| Nachrichten ohne Doppelzeilen | 22.558 von 24.602 (gerechnet 24.602 − 2.044) | tool 13.967 · assistant 8.208 · user 377 · session_meta 6 |
| davon mit Text (user oder assistant) | 1.455 von 22.558 | ohne Text: 7.129 von 8.208 assistant (reine Werkzeugaufrufe) und 1 von 377 user (id 7468) |
| davon in Biotop-Sitzungen | 1.440 von 1.455 | übrige 15 von 1.455: 8 CLI-Proben, 7 Antworten darauf |
| davon von Philipp | 114 von 1.440 | 20 von 114 eingelegte Dokumente; 44 von 114 ab dem 21.09. |

**Die 1.440 Biotop-Nachrichten mit Text nach Absender** (Summe 1.440):

| Absender | Anzahl |
|---|---|
| Zwischentext von Hermes | 643 |
| Antwort von Hermes | 217 |
| Zwischentext eines Subagenten | 158 |
| Auftrag von Hermes an einen Subagenten | 131 |
| Philipp | 114 |
| Bericht eines Subagenten | 54 |
| Meldung eines Hintergrundprozesses | 50 |
| Systemhinweis | 26 |
| Delegationsergebnis | 26 |
| Verdichtung | 21 |

**Philipps 114 Nachrichten je Tag** (Summe 114): 18.09.: 5 · 19.09.: 26 · 20.09.: 39 · 21.09.: 22 · 22.09.: 3 · 23.09.: 8 · 24.09.: 6 · 25.09.: 5. Davon wiederholen 4 von 114 einen früheren Wortlaut; 110 Wortlaute sind verschieden.

**Zählung nach Telegram-Nachrichten** (Auslegung Hermes):
- Ein Dokument mit Begleittext ist bei Telegram eine Nachricht, steht in der Datenbank aber in zwei Zeilen.
- Auf 12 von 20 Dokumentzeilen folgt binnen 10 s eine Textzeile Philipps in derselben Sitzung. So gezählt sind es 102 Nachrichten (gerechnet 114 − 12).
- Eine Telegram-Nachrichtennummer tragen nur 9 von 114 Zeilen. Nach Nummern lässt sich deshalb nicht zählen.

## D. Abweichungen dieses Auftrags (Beitrag zu FK41) mit Rückstellung

**Suche:** Über das ganze Wurzeldateisystem habe ich alles gesucht, was seit Auftragsbeginn (14:44:20) angelegt oder geändert wurde (Änderungs- oder Statuszeit). Ergebnis: 1.751 Einträge, davon 888 an den drei erlaubten Stellen und 863 außerhalb (R159). Jeder der 863 Einträge ist einer Ursache zugeordnet (R164):

| Ursache | Einträge |
|---|---|
| Abweichungen dieses Auftrags (A1, A2, A3, A5) | 6 |
| Nebenwirkung des Lesens von Datenbanken (A6) | 14 |
| Bau S1c und Runde 6, alle bis zum Stichzeitpunkt | 648 |
| Betrieb von Hermes (Protokolle, Cron-Takt, Zwischenspeicher, Subagenten) | 173 |
| System (Journal, Protokolle, systemd) | 18 |
| Anlegen der erlaubten Ordner | 3 |
| Testnebenwirkung von S1c: `/root/biotop-t3/BEFUNDKLASSE-TS.json` um 17:06:22, geschrieben von `tests/test_t3_befundklasse.py` | 1 |
| **Summe** | **863** |

Je Abweichung stehen unten Anlass, Rückstellung und die Antwort auf „Weiß Philipp davon?“.

**A1: Skript `/root/.hermes/scripts/biotop_lage01_meldung1.py`**, angelegt am 25.09. um 15:10:32 für Meldung 1.
- Rückstellung um 18:03:20: nach `/root/sicherung/biotop-lage-01/rueckstellung/` verschoben, nicht gelöscht. SHA-256 vorher = nachher = `c7d769efbbc3b0e9c8a55232e9a2b7c671e42c3da5f076983617acef474fd4e4`.
- `/root/.hermes/scripts` hat danach 4 Dateien, davon 0 seit Auftragsbeginn neu oder geändert (R151).
- Weiß Philipp davon: ja.

**A2: Cron-Job `b11464763130` „BIOTOP-LAGE-01 Meldung 1“** (Einmaljob ohne Agent), angelegt und ausgeführt 15:12:04–05, zugestellt 15:13:04 (R32, R33).
- Rückstellung um 17:57:00 mit `cronjob_manage remove`. Danach steht er nicht mehr in `jobs.json` (R151). Dieser Aufruf lief ohne Rohbeleg; er steht in der Sitzungsdatenbank (R164).
- Nebenwirkung 1: Das Werkzeug löschte dabei den Ausgabeordner des Jobs (1 Datei). Eine Kopie lag vorher in `rueckstellung/`, SHA-256 `844858be53139a2baf5251bef4b3b520e3e4e07bc6f36a481ef3d1c9685a794d` (R148).
- Nebenwirkung 2: Beim Entfernen entstand `/usr/local/lib/hermes-agent/cron/__pycache__/notepad.cpython-312.pyc` (8.687 B). Ich habe sie nicht zurückgestellt, weil ein Löschen im Programmordner von Hermes ein weiterer Eingriff wäre.
- Die Protokollzeilen in `executions.db` und `deliveries.db` bleiben als Nachweis.
- Weiß Philipp davon: ja.

**A3: `/root/.hermes/zwischenbericht/auftrag.json`**, am 15:41:33 auf diesen Auftrag umgestellt (R24).
- Rückstellung um 17:47:32 aus der gesicherten Fassung. SHA-256 danach `e6b91328fed4470f531fbe8a1c27ca3dbead9de9cc90a43d958b6ebc3737cb9f`, gleich dem Stand vor dem Auftrag (R148).
- Der Stand während des Auftrags liegt als `rueckstellung/auftrag.json.stand-biotop-lage-01`.
- Weiß Philipp davon: ja (Zwischenmeldung 16:55).

**A4: Philipps Telegram-Kennung im Abschlussordner**, eine Folge von A3.
- Der Wächter legte um 16:38:07 den Ordner `zwischenbericht-20260925-163807-r114/` an. Dessen `ZWISCHENBERICHT.md` enthält in Zeile 12 Philipps Telegram-Kennung aus der Herkunftszeile der Nachricht, also einen Wert aus `.env` (R125).
- Maßnahme um 18:03:20: Abruf gesperrt (Rechte 640 → 600, HTTP 200 → 403). Der Inhalt ist unverändert, SHA-256 `c96667d256604f8ec0c72a16141f048e66f4b915aa64db49fa7470d015f23df0` (R151).
- Abrufe laut Caddy (R170): 5 um 16:38:07 durch die Abrufprobe des Wächters selbst (Python-urllib), 6 um 18:03:20–21 durch meine Prüfung (curl), sonst keine.
- Rücknahme der Sperre: `chmod 640` auf dieselbe Datei.
- **Löschen oder Freigeben entscheidet Philipp**, weil Regel 2.2 mir das Löschen verbietet. Solange die Datei im Ordner liegt, ist Punkt 7 aus Abschnitt 10 nicht erfüllt.
- Weiß Philipp davon: nein.

**A5: `git status` ohne Schutz vor Indexsperre** (eigener Fehler).
- Um 17:50:15 lief `git status` in `/root/biotop` ohne `--no-optional-locks`, als einfacher Terminalbefehl ohne Rohbeleg.
- Wirkung: Nur die Änderungszeit des Ordners `/root/biotop/.git` ist neu (17:50:15). `.git/index` ist unverändert (Änderungszeit 24.09. 20:24:54, 0 gestagte Änderungen; R161).
- Nicht zurückstellbar.
- Weiß Philipp davon: nein.

**A6: `-shm`-Dateien neben gelesenen Datenbanken** (eigener Fehler und Fehler von Subagenten).
- Ursache: Öffnen mit `mode=ro` ohne `immutable=1` schreibt die `-shm`-Datei neben der Datenbank.
- Betroffen sind 7 Datenbanken. In 7 von 7 wurde die `-shm` neu geschrieben. Die `-wal`-Dateien haben in 7 von 7 nur eine neue Statuszeit; ihr Inhalt ist unverändert, denn ihre Änderungszeit liegt vor dem Auftrag (R163 Teil 4).

  | Zeit | Datenbank | Verursacher |
  |---|---|---|
  | 15:20:18–19 | `/root/biotop-t3/schnappschuss-abschluss3/t3.db`, `/root/biotop-t3/repo-sicherung-vor-commits/daten/biotop.db`, `/root/gesamtstand-01/bestand.db` | Hermes (R18) |
  | 15:55:06 | `/root/biotop/daten/biotop.db-shm`: **im Biotop-Baum und vor der Liste VORHER** (18:14:02); VORHER enthält diesen Stand | Hermes (R31) |
  | 16:58:22 | `/root/reparatur-02/privat-cli/privat.db` | Teil F (zeitgleich, R164) |
  | 17:43:13 | `/root/phase-4-vorbedingung-1/privat/biotop.db` | Teil I (zeitgleich, R164) |
  | 18:14:31 | `/root/biotop-t3/t3.db` | Teil E (zeitgleich, R164) |

- Rückstellung ist nicht möglich, weil der frühere Inhalt der `-shm` unbekannt ist. Datenbanken und `-wal` sind unverändert.
- Ab jetzt gilt: nur `immutable=1` oder das Öffnen einer Kopie. Teil E hat den Hinweis bekommen; die übrigen Teile waren schon beendet.
- Weiß Philipp davon: nein.

**A7: Änderungen an Skills, Ursache UNBEKANNT.**
- Um 17:01:22–17:02:06 wurden 4 Skills unter `/root/.hermes/skills/software-development/` geändert und 18 Sicherungskopien in `/root/.hermes/.curator_backups/` angelegt.
- Nach 14:44:20 gab es keinen `skill_manage`-Aufruf dieses Auftrags. Der letzte (14:49:16) ist eine Abschrift des Aufrufs von 12:52:04, entstanden bei einer Verdichtung (R169).
- Das Kurator-Protokoll zeigt für diese Minute nichts (R163 Teil 1).
- Weg zur Klärung: Protokolle der Skillpflege von Hermes lesen. Das Biotop ist nicht betroffen.

**A8: Freigabeabfrage an dich um 18:46:59** (keine Sperre).
- Der Sicherheitsscan verlangte eine Freigabe für einen lesenden Befehl mit `grep … | python3` („[HIGH] Pipe to interpreter“).
- Die automatische Prüfung scheiterte, weil die Anthropic-Anmeldung der Hilfsprüfung widerrufen ist (R169 Teil b). Deshalb ging die Abfrage an dich, und du hast freigegeben.
- Solche Auswertungen laufen sonst als Skriptdatei über `rb.py`; der Einzelbefehl war eine Abkürzung.

## E. Kosten (OpenRouter)

- **Zählerstand des Schlüssels:** 20,536052277 USD um 14:54:17 (R5), 20,929947777 USD um 18:04:50 (R152). Unterschied: **0,3938955 USD** (gerechnet).
- **Ursache:** Im selben Zeitraum liefen 12 Verdichtungen über OpenRouter (`google/gemini-3.6-flash`): 2 in der Hauptsitzung und je 1 in 10 Subagenten-Sitzungen dieses Auftrags (abgelesen im agent.log, R164). Das ergibt 0,0328 USD je Verdichtung (gerechnet 0,3938955 / 12). Die Zuordnung stützt sich auf eine Quelle. Andere Nutzung von OpenRouter im Zeitraum: 0 Zeilen im agent.log (R169).
- **Bezahlte Modellaufrufe für das Biotop** (Läufe, Tests): 0.
- **Auslegung Hermes (FK48):** Die Verdichtung läuft nach Philipps Festlegung vom 25.09. über OpenRouter; ohne sie bricht die Sitzung ab. Ich zähle sie deshalb nicht als bezahlten Modellaufruf im Sinne von Regel 3 und weise sie getrennt aus. Das Soll in Meldung 2 ist 0,00.
- **Frage an Philipp (FK47):** Gilt das Budget von 0,00 € auch für Verdichtungen?
- **Eigene Entscheidung bis zur Antwort:** Ich starte keine weiteren Subagenten, denn 10 von 12 Verdichtungen fielen in Subagenten-Sitzungen an.

## F. Was ist `/root/versehentlich`?

- **Ein leeres Verzeichnis** (0 Einträge, auch keine versteckten), angelegt am **23.08.2026 um 05:43:24 CEST** und seitdem unverändert: Geburt, Änderung und Statusänderung sind gleich (R116).
- Es ist 26 Tage älter als der Neuaufbau des Biotops (18.09.) und älter als die Sitzungsdatenbank (älteste Nachricht 14.09., 00:42:13).
- **Herkunft:** In der Shell-Chronik `/root/.bash_history` (1.543 Zeilen, ohne Zeitmarken) steht in Zeile 102 `mkdir -p /root/versehentlich` und in Zeile 103 `mv /opt/hermes/eingang/DATEINAME /root/versehentlich/`. „DATEINAME“ ist wörtlich so geschrieben, ein Platzhalter statt eines echten Namens (R116, R149). Der `mv` hat nichts verschoben: Das Verzeichnis ist leer, und seine Änderungszeit ist die Anlagezeit. `/opt/hermes` gibt es heute nicht (R121, R149).
- **Umgebung in der Chronik** (Zeilen 92–112, nur Befehlsnamen): `ps`, `systemctl`, `rm`, `ls`, `find`, `journalctl`, `dig`, `grep`, also Serververwaltung. 0 von 1.543 Zeilen enthalten „biotop“ oder „pytest“. Die Befehle von Hermes stehen nicht in dieser Chronik; sie wurde zuletzt am 19.09. um 01:25:15 geändert (R171).
- **Bezug zum Biotop: keiner gefunden.**
  - Der genaue Pfad steht in 0 Dateien des Biotop-Baums, in 0 Biotop-Ordnern des Prüfkanals und in 0 Arbeitsordnern (R149).
  - In der Sitzungsdatenbank nennt ihn vor diesem Auftrag 1 Werkzeugaufruf (16.09., 23:24:00, id 603). Das war eine lesende Prüfung einer Pfadliste; der Pfad war dort nicht Ziel von `mkdir`, `mv`, `rm` oder `cp` (R131 Teil b).
- **Auslegung Hermes:** Jemand wollte eine versehentlich in den Eingang von Hermes gelegte Datei beiseitelegen und hat dazu eine Anleitung mit Platzhalter abgeschrieben. Wer die Zeilen eingegeben hat, zeigt die Chronik nicht.
- Das Verzeichnis gehört nicht zum Biotop und liegt nicht im Umfang der Sicherung (Abschnitt 4). Es wird unter FK49 geführt.

## G. `biotop/organe/stufe2.py` und `tests/test_tor4_zeilen.py` gehören zu Runde 6, nicht zu Runde 5

**Nicht eingecheckt:** 0 von 75 Commits berühren eine der beiden Dateien. Im Stand `0c2f058` fehlen beide (R117, R156).

**Beide entstanden nach dem Commit der Runde 5** (24.09., 20:24:54) und nach Beginn der Runde 6 (24.09., etwa 23:45 laut Übergabe der Runde 6):
- **`stufe2.py`:** im Biotop-Baum geboren am 25.09. um 03:24:45 (23.931 B, SHA-256 `e42f974af546b8ff14858a23dcfdc9ceac6db5e283a6e347a1da200bc3e64464`).
  - Bytegleich mit `/root/biotop-vor-t4-06/bau/r6_s3_neu/biotop/organe/stufe2.py`, geboren um 03:14:57. Das ist das Bauergebnis des Subagenten S3 der Runde 6 (Bauauftrag `BAU-S3-STUFE2.md`, Sitzung `20260925_001805_f0fcb7`; R154 Teil d, R171).
  - In derselben Sekunde kamen `nachspiel.py`, `tests/test_vorspann.py` und `tests/test_stufe2_eichphase.py` in den Baum (R161).
- **`test_tor4_zeilen.py`:** im Biotop-Baum geboren am 25.09. um 04:34:22, zuletzt geändert um 04:41:34 (48.585 B, SHA-256 `9f512c55fea5d8d9d4ab57513cde9e832873dd25e74c3b602997eaffdcf56df0`).
  - Bytegleich mit `/root/biotop-vor-t4-06/bau/r6_s2_neu/tests/test_tor4_zeilen.py`. Das ist das Bauergebnis des Subagenten S2 der Runde 6 (Bauauftrag `BAU-S2-TOR4.md`, Sitzung `20260925_001805_512a27`; R154, R171).
  - `biotop/tor4.py` bekam in derselben Sekunde seine Änderung der Runde 6 (R161).

**Was der Commit `0c2f058` meint:**
- **„Tor-4-Skript“** ist `biotop/tor4.py`. Die Datei ist im Commit neu angelegt (Blob `69ac47c`); die Testdatei ist nicht gemeint (R117).
- **„Stufe 2 überall“** meint die Entscheidungen 6 und 8 der Runde 5, eingebaut in bestehende Dateien. `git grep -c "Stufe 2"` auf dem Commit findet 57 Treffer in 13 Dateien, darunter `organe/vorspann.py` mit 10, `nachspiel.py` mit 7 und `tests/test_vor_t4_05.py` mit 10 (R117).
- **Frühere Nennungen von „stufe2.py“:** Die 4 Werkzeugaufrufe vor dem Commit (24.09., 13:17–16:07) betreffen `/root/biotop-vor-t4-04/bau/r4_stufe2.py`. Das ist ein Bauskript der Runde 4 mit 22 Ersetzungen in bestehenden Dateien (R131 Teil a).
- Der veröffentlichte Ordner der Runde 5 nennt keine der beiden Dateien (R117).

**Stand:** Beide gehören zur nicht eingecheckten Arbeit der Runde 6 (19 geänderte und 6 neue Dateien; R156) und stehen in der Liste VORHER. Runde 6 ruht seit dem Stichzeitpunkt (Entscheidung Hermes, START-01).

## H. Was fertig ist, was fehlt

**Fertig**, jeweils mit Rohbeleg:
- **Schritt 1** (R1–R6). Meldung 1 ist um 15:13:04 zugestellt (R32, R33).
- **Quellen erhoben:** Sitzungsdatenbank, Dokumente v1–v8, git, Kassen, Abschlussordner und Cron (R11–R31). Das Nachrichtenverzeichnis v3 reicht bis zum Stichzeitpunkt (R155).
- **Wortlaut des Masterprompts v8 (FK14):** 3 Teile, zusammengesetzt bytegleich zum Original (R95). Noch nicht veröffentlicht; er kommt als `MASTERPROMPT-GUELTIG`.
- **Prüfsummenliste VORHER** um 18:14:02: 3.153 Dateien, 40.030.538 B, SHA-256 der Liste `e67011b931cbb8f386716da020d4723470f29715b8fcda8cf2768f232428dfb6` (R156).
- **Entwürfe der Teile A–I:** 9 von 9 Subagenten haben ihren Teil geliefert, der letzte um 18:55. Die Entwürfe sind noch nicht von mir geprüft und nicht veröffentlicht.
- **Rückstellungen A1–A3** (R148, R151).

**Offen**, in dieser Reihenfolge:
1. Sicherung nach Abschnitt 4 mit Wiederherstellungsprobe und Gegenprobe. Danach Tests im wiederhergestellten Stand, abgeschottet ohne Netz (Probe der Abschottung: R94).
2. Inventar I1–I8 zum Stichzeitpunkt mit Abgleich, Tagesbilanz und Gegenprobe; dazu `KASSE` und `LISTEN`.
3. Entwürfe prüfen und einsetzen. `LAGE` (FK01–FK07 und FK47–FK49 schreibe ich selbst), `VERLAUF` (FK11), `MASTERPROMPT-GUELTIG`, `SICHERUNG`, `VOLLSTAENDIGKEIT` mit Lückenliste.
4. Liste NACHHER, Geheimnissuche mit Gegenprobe, `gedaechtnis/STAND-02.md`, abschließende Einstiegsdatei, `DATEIEN`, `PRUEFSUMME`, `ABRUFPROBE`, Meldung 2.

**Schon bekannte Lücken:**
- **Befehle ohne Rohbeleg:** Einzelne Anzeige- und Prüfbefehle liefen als einfache Terminalbefehle außerhalb von `rb.py` (Beispiele: A2, A5). Wortlaut und Ausgabe stehen in der Sitzungsdatenbank. Anzahl und Liste folgen in `VOLLSTAENDIGKEIT`.
- **SPERRE-01** (16:27): Der Lebenszyklus-Wächter sperrte eine lesende Zählung. Sie ist nicht nachgeholt; ihre Zahlen liegen in R19, R22 und R23 vor. Der Wortlaut folgt als Datei.

## I. Abschnitt 10: Stand je Punkt

| Punkt | Stand |
|---|---|
| 1 Abrufbarkeit aus Meldung 2 | offen |
| 2 Antworttafel | noch nicht gezählt |
| 3 Abgleich | offen |
| 4 Tagesbilanz | offen |
| 5 Entscheidungsregister | Entwurf liegt vor, ungeprüft |
| 6 Wiederherstellungsprobe | nicht ausgeführt; das Werkzeug ist im Selbsttest grün (R70) |
| 7 kein Geheimnis im Ordner | **nicht erfüllt**, solange die Datei aus A4 im Ordner liegt |
| 8 Liste vorher = Liste nachher | VORHER liegt vor, NACHHER ist offen; die Änderung von 15:55:06 liegt vor VORHER (A6) |
| 9 Wortlaut von Masterprompt und Verfassungen | v8 liegt vor (R95); Verfassungen im Entwurf B |
| 10 Glossar | Entwurf liegt vor |
| 11 Bezugsgröße je Zahl, Rohbeleg je „ausgeführt“ | offen; Befehle ohne Rohbeleg siehe H |

## J. Lesereihenfolge für diesen Zwischenstand

1. Diese Datei.
2. Die Rohbelege, auf die sie verweist: R1–R6 in Stand 01, R7–R171 in Stand 02. Die Adressen stehen in DATEIEN-02.txt (K).
3. START-01 für Schritt 1.

## K. Dateien des Ordners

- Jede Datei außer den Rohbelegen von Stand 02 steht unten mit Bytes und SHA-256.
- Die Rohbelege von Stand 02 sind zusammengefasst: Mit allen Adressen wäre diese Datei größer als 40 KB. Jede ihrer Adressen steht vollständig in DATEIEN-02.txt.
- DATEIEN-02.txt und PRUEFSUMME-ORDNER-02.txt entstehen nach dieser Datei. Sie enthalten Bytes und SHA-256 jeder Datei, auch dieser.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/DATEIEN-02.txt
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/PRUEFSUMME-ORDNER-02.txt

- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ROHBELEGE-TEIL1-01.txt · 25432 B · SHA-256 `5367071fec2fbee84851d5242bc35a3427ec3d032cd20c2de9543be02171687b`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ROHBELEGE-TEIL2-01.txt · 27478 B · SHA-256 `595dc921544719c4edaf9f8ffb3a7dbdea786c14044a22656214dba1d8ddde12`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/ROHBELEGE-TEIL3-01.txt · 26515 B · SHA-256 `4de5790a957b4ab39f4dd3dce54044c03ce3733f68e8047db70b3d3126a0160d`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/START-01.md · 7308 B · SHA-256 `e31c4f5d01f688baba16d4436b738c0223983fcedeeb40a8dda5176326d3158c`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/DATEIEN.txt · 543 B · SHA-256 `1f00ee85f4f732a72e3799f2773a770663ecb330bb5b4752f035e68a810fcfac`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/MANIFEST.sha256 · 254 B · SHA-256 `c6ac5b538264405cdd43c10fac7344bdd0d7d7b98c16743fb1cabdd8370641bf`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/PRUEFSUMME-ORDNER.txt · 65 B · SHA-256 `6e126595a0b93f0677cc10a6c1fd47181d3465cfe29e044be4b881565fc9b6ae`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/UEBERGABE-1-UEBERGABE.md · 5754 B · SHA-256 `ce7f985bbe7139bc2a1a52848b1ba81e7adeed61701772c0390d7370f15bbb6e`
- https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/ZWISCHENBERICHT.md · 11021 B · SHA-256 `c96667d256604f8ec0c72a16141f048e66f4b915aa64db49fa7470d015f23df0` · **Abruf gesperrt (HTTP 403), siehe A4**
- Rohbelege Stand 02: 162 Dateien, `ROHBELEGE-TEIL4-02.txt` bis `ROHBELEGE-TEIL165-02.txt` mit R7–R171; jede mit vollständiger Adresse, Bytes und SHA-256 in DATEIEN-02.txt und PRUEFSUMME-ORDNER-02.txt (Adressen oben)

## L. Gedächtnis: neueste Dateien in `laeufe/gedaechtnis/`

Seit Auftragsbeginn unverändert (R159):

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/STAND-01.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/REGELN-01.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/UNTERBAU-01.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/DATEIEN-01.txt
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/PRUEFSUMME-ORDNER-01.txt
