# BIOTOP-LAGE-01 · Fassung 2 · `SICHERUNG-TEIL1-01.md` (Abschnitt 4)

- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST. Verfasser: Hermes. Alle Zeiten CEST.
- **Rohbelege:** Die Nummern R… stehen in den ROHBELEGE-Dateien dieses Ordners, die Liste steht in DATEIEN-03.txt.
- **Werkzeug:** `/root/sicherung/biotop-lage-01/arbeit/sich.py`. Selbsttests an erfundenen Bäumen: R70, R176, R179. Ablauf der Schritte 1–11: `arbeit/s6_sicherung.py`, ein Rohbeleg je Schritt, 19:41:32–19:45:53, rc 0.

## 1. Ergebnis in Kürze

| Nachweis | Ergebnis | Beleg |
|---|---|---|
| Archiv | `biotop-sicherung-2026-09-25-01.tar.gz`, **790.821.244 B**, SHA-256 `03340fdbece5cc4254b54d285b36b1d9640eaa590649f9e1007b95fa2881af73` | R189 |
| Einträge im Archiv | 111.440 laut `tar -t` = 111.440 laut Manifest (33.800 Verzeichnisse, 75.214 Dateien, 2.426 Verweise, 0 Sonderdateien), 3.385.003.245 B Dateiinhalt | R189 |
| `PRAGMA integrity_check` | **3.004 von 3.004** Datenbankkopien „ok“, 0 nicht ok, 0 fehlen | R187 |
| Wiederherstellungsprobe | entpackt 111.440 Einträge, davon 75.214 Dateien, gegen gepackt 111.440 und 75.214. Nur gepackt 0, nur entpackt 0, verschieden 0: **Unterschied leer** | R190 |
| Gegenprobe | Byte 0 von `root/biotop/README.md` in einer Kopie geändert (0x23 → 0x22). Gemeldet wird **genau diese Datei**, verschieden 1, sonst 0: **angeschlagen** | R192 |
| Tests im entpackten Stand | abgeschottet, ohne Modellaufruf: 953 gesammelt, 748 bestanden, 203 nicht bestanden, 2 übersprungen, 93 abgewählt. An den Originalen hat sich nichts geändert (0 Einträge nach der Marke) | R196, R203, R204; Abschnitt 5 |
| `/root/biotop` ohne `.git/` vorher gegen nachher | VORHER 18:14:02 und NACHHER 20:13:30: je **3.153 Dateien**, 40.030.538 B. Die Listen sind byte-gleich (SHA-256 der Liste `e67011b931cbb8f386716da020d4723470f29715b8fcda8cf2768f232428dfb6`): **Unterschied leer** | R156, R205; Abschnitt 6 |
| Ablage 2 | **keine eingerichtet**, die Sicherung liegt nur auf diesem Server | R36; Abschnitt 7 |

## 2. Umfang in Rangfolge, Platz, Repository-Stand

- **Platz vorher (R177):** Umfang 79.597 Dateien, 3,23 GiB, frei 86,6 GiB. Es reichte für alles. Kein Teil fehlt wegen Platz.
  - Die Zahl 79.597 enthält noch die Begleitdateien `-wal`/`-shm`. Die Sicherung ersetzt sie durch Backup-Kopien (4.382 Stück, siehe Tafel).
  - 75.214 + 4.382 = 79.596. Eine Datei Unterschied ist nicht aufgeklärt (Lücke, VOLLSTAENDIGKEIT).
- **Repository-Stand (R156, R191):**
  - HEAD `0c2f058`.
  - 25 nicht eingecheckte Einträge (`git --no-optional-locks status --short`), Liste in `tmp/git-status-stich.txt` und in INVENTAR (I6).
  - Nichts wurde eingecheckt oder verändert.

| Teil (Rang) | Inhalt | Dateien | Datenbanken (Backup) | Verweise | Bytes | ausgelassen | Beleg |
|---|---|---|---|---|---|---|---|
| 1 | `/root/biotop` samt `.git/` | 3.922 | 1 | 0 | 38.871.595 | 6 `__pycache__`, 2 Begleitdateien | R181 |
| 2 | Aufträge, Masterprompt-Fassungen, Arbeits- und Werkordner unter `/root` | 30.812 | 2.171 | 1.479 | 1.743.180.319 | 114 Ordner (Zwischenspeicher, `venv`), 4.342 Begleitdateien, 1 Geheimnisdatei | R182 |
| 2b | Arbeits- und Reviewordner in `/tmp` (werden beim Neustart geleert) | 22.208 | 823 | 941 | 635.317.018 | 224 Ordner, 38 Begleitdateien | R183 |
| 3 | Biotop-Ordner im Prüfkanal und `laeufe/gedaechtnis/` | 11.340 | 4 | 0 | 173.282.930 | — | R184 |
| 4 | Sitzungsdatenbank `/root/.hermes/state.db` | 0 | 1 | 0 | 433.643.520 | — | R185 |
| 5 | Rest von `/root/.hermes` | 3.928 | 4 | 6 | 360.707.863 | 5 Ordner, 3 Geheimnisdateien, 2 Sockets, `state.db` (steht in Teil 4) | R186 |
| **Summe** | | **72.210** | **3.004** | **2.426** | **3.385.003.245** | | gerechnet; gleich dem Manifest (R189) |

- 72.210 Dateien + 3.004 Datenbankkopien = 75.214 Dateien im Manifest.
- Welche Wurzeln jeder Teil hat, steht mit jeder Auslassung in den Protokollen `sicherung/protokoll-stufe-*.txt`, im Archiv enthalten.
- Die SQLite-Dateien im Umfang sind nach ihrer Magie gefunden, ohne sie zu öffnen: 3.004 (R180).

## 3. Datenbanken und Geheimnisse

- **Datenbanken:** Keine wurde als laufende Datei kopiert. Jede ist über Pythons `Connection.backup` gesichert. `sqlite3` gibt es auf dem Server nicht (R36).
  - Die Kopie steht im Archiv am Pfad der Datenbank. Die `-wal`/`-shm` daneben sind nicht mitgepackt, ihr Inhalt steckt in der Kopie.
  - Zum Lesen sind die Datenbanken mit `mode=ro&immutable=1` oder als Kopie geöffnet. Grund: A6 in START-02 D.
- **Geheimnisdateien, nicht im Archiv, nur mit Pfad:**
  - `/root/.hermes/.env`: Schlüssel und Kennungen von Hermes, darunter `OPENROUTER_API_KEY`. Das Biotop liest diesen Namen, wenn die Umgebung ihn nicht setzt (`biotop/anbieter/__init__.py` Z. 75–84).
  - `/root/.hermes/auth.json`: Anmeldedaten der Anbieter von Hermes.
  - `/root/.hermes/.env.sicherung-2026-09-18`: ältere Sicherungskopie von `.env`.
  - `/root/w7/07-codex-token.txt`: enthält 4 Werte aus `auth.json` (R178). Deshalb wird die Datei wie eine Geheimnisdatei behandelt (Entscheidung Hermes, FK49). Für das Biotop ist sie nicht nötig.
- **Vertraulich:** Das Archiv kann eingefügte Geheimnisse aus der Sitzungsdatenbank enthalten. Es liegt nur unter `/root/sicherung/biotop-lage-01/`, nie im Prüfkanal.

## 4. Wiederherstellungsanleitung (leerer Server → lauffähiges Biotop)

Nach Abschnitt 4.9 ist jeder Schritt gekennzeichnet: **ausgeführt** (mit Rohbeleg, im entpackten Stand) oder **gelesen, nicht ausgeführt**.

1. **Grundpakete:** Ubuntu mit Python 3.12.3, Docker, `uv` 0.12.13, Node 22 (`/opt/node22`, v22.14.0), `tar`, `pigz` (Versionen: R194, R36). *Gelesen, nicht ausgeführt.*
2. **Archiv entpacken:** `mkdir -p /root/sicherung/biotop-lage-01 && tar -xzf biotop-sicherung-2026-09-25-01.tar.gz -C /`. Die Pfade im Archiv beginnen mit `root/…`, `tmp/…` und `var/pruefkanal/…`. *Ausgeführt* in ein leeres Verzeichnis statt `/` (R190, Unterschied leer).
3. **Geheimnisse von Hand ergänzen** (nur Name und Zielpfad):
   - `/root/.hermes/.env` mit `OPENROUTER_API_KEY` und den Kennungen des Gateways;
   - `/root/.hermes/auth.json`.
   - Ohne sie laufen Tests und Werkzeuge, aber keine Modellaufrufe und kein Gateway. *Gelesen, nicht ausgeführt.*
4. **Python-Umgebung:** `uv venv /root/biotop-t3/venv --python 3.12`, dann `uv pip install --python /root/biotop-t3/venv/bin/python iniconfig==2.3.0 packaging==26.3 pluggy==1.6.0 pygments==2.21.0 pytest==9.1.1`. Die Pakete stehen in R194; `/root/biotop/requirements-test.txt` hat 14 B. *Gelesen, nicht ausgeführt.* Im Test (Schritt 6) war die Original-Umgebung schreibgeschützt eingehängt.
5. **Kammer-Abbilder:** `docker build -t biotop-kammer:1 /root/biotop/kammer` und `docker build -t biotop-kammer:ts1 /root/biotop/kammer/typescript`. Die Dockerfiles und `package-lock.json` sind im Archiv (R194). Grundabbilder sind `python:3.12-slim` (PYTHON_VERSION 3.12.14) und `node:22-bookworm-slim` (NODE_VERSION 22.23.2). *Gelesen, nicht ausgeführt.*
6. **Tests:** `cd /root/biotop && /root/biotop-t3/venv/bin/python -m pytest -m "not integration"`. *Ausgeführt*, abgeschottet (R196, Abschnitt 5). Mit Kammer und gesetzter Auftragsgrenze entspricht das der letzten vollen Regression: 598 bestanden, 2 übersprungen, 93 abgewählt, 2.458 s (`biotop-vor-t4-05/REGRESSION.txt`).
7. **Lauf:** Auftragsgrenze setzen (`BIOTOP_AUFTRAG_LAUF_AB`, `BIOTOP_AUFTRAG_BUDGET_EUR`), dann `PYTHONPATH=/root/biotop python3 -m biotop lauf anlegen --budget <€>` und die Schritte aus AUFBAU-TEIL2-01.md (FK34). *Gelesen, nicht ausgeführt*, weil es Modellaufrufe auslöst.
8. **Hermes selbst:** `/root/.hermes` (Teile 4 und 5) ist gesichert. Das Programm `/usr/local/lib/hermes-agent` und die Serverkonfiguration (`/etc/pruefkanal`, Caddy) liegen nicht im Umfang von Abschnitt 4. Sie gehören in die Lückenliste (VOLLSTAENDIGKEIT).

## 5. Tests im wiederhergestellten Stand (Abschnitt 4.6)

- **Aufbau** (`arbeit/s9_testlauf.sh`, `arbeit/ns_test.sh`, R196):
  - Kopie der vier Baumteile `biotop`, `biotop-t3`, `reparatur-01` und `versandwerk-t3-02` aus dem entpackten Stand: 33.175 Dateien.
  - Die Tests nutzen feste Pfade. Deshalb sind die Kopien in einem eigenen Mount-Namensraum über die Originalpfade gelegt.
  - Schreibgeschützt eingehängt waren `/`, `/boot`, `/boot/efi` und die Original-venv.
  - Netz nur `lo`, keine Verbindung nach außen. Docker nicht erreichbar. `/root/.hermes` leer, also kein Schlüssel.
  - Eine Probe vorher zeigte: Der Schreibschutz wirkt nur innen (R195).
- **Ergebnis:** `pytest -m "not integration"`, rc 1, 61 s.
  - 953 gesammelt: 748 bestanden, 187 fehlgeschlagen, 16 Fehler, 2 übersprungen, 93 abgewählt.
  - Nach der Marke sind **0** Originale geändert (R196).
- **Ursachen der 203 nicht bestandenen Tests** (R203, R204; R201 ist berichtigt, siehe unten):
  - 97: der Docker-Dienst ist nicht erreichbar (Abschottung);
  - 83: ohne Ursache im Fehlertext, aber jeder zeigt einen Aufruf der Kammer. Dass die fehlende Kammer die Ursache ist, halte ich für wahrscheinlich; belegt ist es nicht (Auslegung Hermes);
  - 11: `test_w_g_*`, die roten Spezifikationen von S1c zu Befund G. S1c nannte 10;
  - 8: `AuftragsgrenzeFehlt`, weil die Umgebungsvariablen nicht gesetzt sind;
  - 2: `VorspannFehler` „Kernstand seit der Eichphase der Stufe 2 verändert“ in `tests/test_t3_bindung.py`. Das ist ein Befund zum Stand und kein Abschottungsgrund; nicht weiter untersucht (offener Punkt, LAGE);
  - 1: das Kammer-Abbild fehlt;
  - 1: `node` fehlt im Pfad.
  - Summe 203.
  - Nach Testdatei: 69 in `test_vor_t4_06.py`, nicht eingecheckt; 56 in geänderten Dateien; 78 in eingecheckten, unveränderten Dateien.
- **Eigener Fehler, berichtigt:** Die erste Auswertung (R201) ordnete 168 Fälle „Docker/Kammer“ zu. Ihr Muster traf aber schon das Wort „kammer“ im Code. Maßgeblich sind R203 und R204.
- **Abgrenzung:** Die Testbestände von S1c (Teillauf Durchgang 5: 457 von 457 grün) liefen mit echter Kammer. Dieser Lauf ohne Kammer bestätigt sie nicht und widerlegt sie nicht.

## 6. Vorher gegen nachher (`/root/biotop` ohne `.git/`)

- **VORHER:** R156, erhoben um 18:14:02, nach dem Stich. 3.153 Dateien, 40.030.538 B. Die Liste liegt in `pruefsummen/VORHER.txt` (416.235 B, SHA-256 `e67011b9…dfb6`).
- **NACHHER:** R205, um 20:13:30, nach dem letzten Schritt, der das Biotop hätte berühren können (Testlauf in der Kopie). 3.153 Dateien. Die Liste ist byte-gleich zu VORHER (`cmp`).
- **Ergebnis:** nur VORHER 0, nur NACHHER 0, Inhalt verschieden 0. Der Unterschied ist leer.
- **Vor VORHER, 15:55:06:** Ein Lesezugriff hat `daten/biotop.db-shm` neu geschrieben (A6 in START-02 D). VORHER enthält diesen Stand schon. Die Datenbank selbst und `-wal` sind unverändert.
- **Statischer Nebenbefund (R201):** Der entpackte Stand ohne `.git/` stimmt mit VORHER in 3.027 von 3.028 Dateien überein. Verschieden ist 1 Datei: `daten/biotop.db`, weil die Backup-Kopie byte-verschieden vom Original ist. Nur in VORHER stehen 125 Dateien: 123 Zwischenspeicher und 2 `-wal`/`-shm`. Beides ist nach den Auslassungsregeln so gewollt.
- **Kontrolle zum Schluss:** Eine zweite Liste `NACHHER2` entsteht unmittelbar vor der abschließenden Einstiegsdatei. Sie steht in START-03.

## 7. Ablage und offener Punkt

- **Ablage 1:** `/root/sicherung/biotop-lage-01/`, außerhalb jedes öffentlich erreichbaren Verzeichnisses.
- **Ablage 2:** keine eingerichtet (R36):
  - kein `rclone`, `restic` oder `borg`;
  - keine Zugangsdatei (`rclone.conf`, `.aws`, `.s3cfg`, `.ssh/config`);
  - eine einzige Platte `/dev/vda`.
- Nichts wurde improvisiert.
- **Offener Punkt: „Sicherung liegt nur auf diesem Server.“**
  - Vorschlag Hermes: Philipp holt das Archiv einmal über seinen eigenen Zugang auf ein Gerät außerhalb des Servers (790.821.244 B). Er prüft die SHA-256 oben und bewahrt das Archiv vertraulich auf.
  - Oder Philipp nennt einen bereits eingerichteten, nicht öffentlichen Ort.
  - Philipp entscheidet.
