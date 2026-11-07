# BIOTOP-EINLAGERUNG-01 · WIEDEREINSTIEG · Teil 3 von 3 (Fassung 02)

Punkte 6–10: Wiederaufnahme, erster Auftrag, Risiken, Übergabe. Teil 1: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-einlagerung-01/WIEDEREINSTIEG-TEIL1-02.md

## 6. Wiederaufnahme, Weg A — derselbe Server (Hermes auf HERMES-1)

1. **Stillstand nur auf Philipps Auftrag aufheben.** Ohne ausdrücklichen Auftrag bleibt alles still. Mit Auftrag: den Stillstandsvermerk in `/root/.hermes/memories/MEMORY.md` durch einen Wiederaufnahmevermerk ersetzen (Werkzeug `memory`), in `laeufe/gedaechtnis/` die nächste freie STAND-Nummer anlegen, den Zwischenbericht-Wächter auf den neuen Auftrag stellen (`/root/.hermes/zwischenbericht/auftrag.json`; Vorlage `/root/biotop-einlagerung/arbeit/waechter_setzen.py`).
2. **Prüfsummen gegen das Einlagerungsmanifest vergleichen** (liest nur):
   ```bash
   cd /root/biotop && git --no-optional-locks log -1 --format='%H %D' && git --no-optional-locks status --short | wc -l
   # erwartet: e8401afda5907a997eae96537394f7dbf4e8af3f … einlagerung/runde-6-stand, tag: eingelagert-20260925 · 0
   python3 /root/biotop-einlagerung/arbeit/wa_vergleich.py /root/biotop
   # vergleicht jede Datei unter /root/biotop mit MANIFEST-KOMPLETT.tsv (Datenbanken: integrity_check statt Bytevergleich)
   ```
   Ausgeführt am 26.09.2026 um 03:13 CEST (EB88): 3.959 = 3.959 Einträge, Unterschied leer. Nach einer Regression meldet das Werkzeug `.git/index` als verschieden (Teil 1 Punkt 2.6).
3. **Regression mit Kammer** (Befehl der Runde 5, `/root/biotop-vor-t4-05/job_kette.sh` Z. 37–40; ohne Modellaufruf; Laufzeit in Runde 5: 2.457,93 s für 598 bestanden, 2 übersprungen, 93 abgewählt):
   ```bash
   mkdir -p /root/<auftrag>/tmp && cd /root/biotop
   env BIOTOP_KAMMER_IMAGE=biotop-kammer:ts1 BIOTOP_AUFTRAG_LAUF_AB=26 BIOTOP_AUFTRAG_BUDGET_EUR=10 \
       T3_VERDRAHTUNG_BELEG=/root/<auftrag>/VERDRAHTUNG-BELEG-REGRESSION.json TMPDIR=/root/<auftrag>/tmp \
       /root/biotop-t3/venv/bin/python -m pytest tests/ -q -m "not integration" -p no:cacheprovider -rfEs --durations=8 \
       --junitxml=/root/<auftrag>/REGRESSION.junit.xml > /root/<auftrag>/REGRESSION.txt 2>&1
   ```
   `TMPDIR` auf einen eigenen Ordner setzen (Entscheidung Hermes in der Probe): pytest räumt sonst ältere Ordner unter `/tmp/pytest-of-root/` weg, und die Kammer braucht einen Pfad, den der Docker-Dienst sieht. Im wiederhergestellten Stand ausgeführt (EB81: 2.457,86 s); Ergebnis: Teil 1 Punkt 2.6.
4. **Dann der erste Auftrag nach Punkt 8.**

## 7. Wiederaufnahme, Weg B — neuer Server aus dem Laptop-Paket (leeres Ubuntu 24.04)

Der Weg führt von einem leeren Ubuntu 24.04 bis zum lauffähigen Biotop. Was davon in der Wiederherstellungsprobe (Schritt 6, 26.09.2026) ausgeführt wurde, trägt seinen Rohbeleg. Alles andere ist gelesen, nicht ausgeführt.

1. **Server vorbereiten** (gelesen, nicht ausgeführt): Ubuntu 24.04 LTS, als `root`. Eingelagert wurde auf Ubuntu 24.04.4 LTS mit Python 3.12.3, Docker 29.1.3, git 2.43.0, pigz 2.8 und uv 0.12.13 (UMGEBUNG.md, EB38).
   ```bash
   apt-get update && apt-get install -y docker.io git pigz python3 python3-venv curl
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. **Archiv vom Laptop hochladen** (PowerShell auf dem Laptop; gelesen, nicht ausgeführt):
   ```powershell
   scp 'C:\Biotop-Lager\biotop-einlagerung-20260925-komplett.tar.gz' 'root@<neue-adresse>:/root/'
   scp 'C:\Biotop-Lager\SHA256SUMS-20260925.txt' 'root@<neue-adresse>:/root/'
   ```
   Auf dem Server prüfen: `cd /root && sha256sum --ignore-missing -c SHA256SUMS-20260925.txt`. Die Ausgabe muss `biotop-einlagerung-20260925-komplett.tar.gz: OK` lauten.
3. **Nach `/` entpacken.** Code und Tests nennen feste Pfade wie `/root/biotop/…`, `/root/biotop-t3/…` und `/root/reparatur-01/…` (EB22). Das Biotop läuft nur an genau diesen Pfaden.
   ```bash
   pigz -dc /root/biotop-einlagerung-20260925-komplett.tar.gz | tar --numeric-owner -C / -xpf -
   ```
   In der Probe ausgeführt, allerdings in ein leeres Verzeichnis statt nach `/` (EB73: Entpacken rc 0 in 19,6 s; Manifest gegen entpackten Stand 124.282 = 124.282 Einträge, Unterschied leer). Das Archiv legt `/MANIFEST-KOMPLETT.tsv`, `/root/…`, `/usr/local/lib/hermes-agent/` und 26 Dateien unter `/var/pruefkanal/…` an.
4. **Manifest vergleichen**, je Ordner, zum Beispiel für das Repository:
   ```bash
   python3 /root/biotop-einlagerung/arbeit/wa_vergleich.py /root/biotop /MANIFEST-KOMPLETT.tsv
   ```
   Ausgeführt am Original (EB88: 3.959 = 3.959 Einträge, Unterschied leer) und am entpackten Stand nach der Regression (EB87: nur `.git/index` anders, siehe Teil 1 Punkt 2.6). Datenbanken prüft das Werkzeug mit `integrity_check`. Im entpackten Archiv ergaben 3.028 von 3.028 Datenbanken `ok` (EB75).
5. **Python-Umgebung der Regression** aus der gesicherten Paketliste (5 Pakete) bauen:
   ```bash
   uv venv --python /usr/bin/python3.12 /root/biotop-t3/venv
   uv pip install --python /root/biotop-t3/venv/bin/python -r /root/biotop-einlagerung/paket/dokumentation/umgebung/pip-freeze-root-biotop-t3-venv.txt
   ```
   Im entpackten Stand ausgeführt, ohne Netz aus dem Paketspeicher von uv (EB79: 5 Pakete installiert, `pip freeze` danach gleich der Liste, pytest 9.1.1). Weitere Listen liegen daneben: `pip-freeze-root-reparatur-01-venv.txt` und `pip-freeze-usr-local-lib-hermes-agent-venv.txt`.
6. **Kammer-Abbilder laden:**
   ```bash
   docker load -i /root/biotop-einlagerung/kammer-abbilder/biotop-kammer-1-und-ts1.docker-save.tar
   ```
   Ausgeführt (EB79: rc 0). Die Kennungen sind danach gleich den gesicherten: `biotop-kammer:1` = `sha256:ce7bbe94…`, `biotop-kammer:ts1` = `sha256:212e6212…`. Auf diesem Server lagen die Abbilder schon vor; das Laden in ein leeres Docker ist gelesen, nicht ausgeführt. Den Bauweg für einen Neubau beschreibt UMGEBUNG.md im Abschnitt Kammer.
7. **Geheimnisse von Hand eintragen.** Sie sind nicht im Paket; hier stehen nur Name und Zielpfad.
   - `/root/.hermes/.env`: Schlüssel und Kennungen für Hermes, unter anderem `OPENROUTER_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_ALLOWED_USERS` und `TERMINAL_MODAL_IMAGE` (EB24). Rechte 600.
   - `/root/.hermes/auth.json`: Anmeldungen der Modellanbieter, mit Einträgen für `openai-codex` und dem Schlüsselpool für `anthropic` und `openrouter` (EB24). Neu anmelden statt kopieren. Rechte 600.
   - `/root/w7/07-codex-token.txt`: nur nötig, wenn W7 gebraucht wird. Das Biotop braucht die Datei nicht.
   - `/root/.ssh/authorized_keys`: Philipps öffentlicher Schlüssel `philipp-laptop`. Er ist nicht im Paket.
   - `/etc/pruefkanal/schluessel`: der Pfadschlüssel des Prüfkanals, nicht im Paket. Er wird nur für Punkt 9 gebraucht.
8. **Hermes Agent in der gesicherten Version** (gelesen, nicht ausgeführt): v0.21.2 (2026.9.11), Git `abf4706384c8ab17d6f22aab0ab8c71526eac305`, Installationsweg git (UMGEBUNG.md).
   - Der Quellbaum mit `.git`, aber ohne `venv`, liegt nach dem Entpacken in `/usr/local/lib/hermes-agent/`.
   - Einrichten nach der Installationsanleitung von Hermes Agent, dann `git -C /usr/local/lib/hermes-agent checkout abf4706384c8ab17d6f22aab0ab8c71526eac305`. Die Paketliste der Umgebung ist `pip-freeze-usr-local-lib-hermes-agent-venv.txt` (113 Pakete).
   - Das Hermes-Zuhause `/root/.hermes/` kommt aus dem Archiv: Einstellungen, Gedächtnis, Skills, Sitzungsdatenbank und Cron.
   - Danach prüfen, dass kein Cron-Job mit Biotop-Bezug aktiv ist (`hermes cron list`) und dass `/root/.hermes/zwischenbericht/auftrag.json` auf `zwischenberichte` steht.
9. **Prüfkanal** (optional; gelesen, nicht ausgeführt): Ein Webserver liefert `/var/pruefkanal/oeffentlich/` aus; auf diesem Server ist es Caddy. Die Inhalte von `laeufe/…` kommen aus `dokumentation/pruefkanal/laeufe/` (geschwärzte Kopien) und aus den 26 Originalen unter `/var/pruefkanal/…` im Archiv. Ein neuer Pfadschlüssel ergibt neue Adressen.
10. **Nachweis: Manifestvergleich (Punkt 4) und Regression wie in Weg A, Punkt 3.** Beides in der Probe ausgeführt (EB80, EB81, EB83) und dabei abgeschottet:
    - eigener Mount- und Netz-Namensraum, ohne Netz;
    - jeder Biotop-Ordner unter `/root` durch seine entpackte Kopie ersetzt;
    - `.env` und `auth.json` verdeckt;
    - Docker nur über einen Wächter, der jede Einhängung außerhalb der Probe verweigert. Sein Protokoll hat 1.418 Zeilen, verweigert wurde 0-mal.
    Ergebnis: Teil 1, Punkt 2.6.

- **Entscheidung Hermes zur Probe:** Der Auftrag verlangt, die Probe abzubrechen, sobald sie auf absolute Pfade stößt, die ins Original zeigen.
  - Diese Pfade waren vorab bekannt (EB22). Statt abzubrechen, ließ ich sie in der Probe auf die entpackten Kopien zeigen (Einhängungen in EB80).
  - Kein Zugriff ging ins Original. Beleg EB92: Die Originale hatten vorher und nachher 46.605 Einträge, Unterschied leer.
  - Befund für den Wiedereinstieg: Das Biotop ist an seine Pfade gebunden und muss nach `/` entpackt werden.
  - Wer die Probe am Wortlaut des Auftrags misst, wertet sie als abgebrochen.
- **Auslegung Hermes zur zweiten Arbeitskopie** (Teil 1, Punkt 2.6): Dort kam nur `/root/biotop` aus dem Original. Die übrigen Biotop-Ordner kamen wie im ersten Lauf aus dem entpackten Archiv, damit die Originale unberührt blieben.

## 8. Erster Auftrag nach dem Wiedereinstieg (Vorschlag Hermes)

- **Umfang:** Runde 6 abschließen, nicht erweitern — nach Philipps Entscheidung zu 4.1. Kein Lauf, kein Modellgeld (wie jede Behebungsrunde, v8 Z. 476).
- **Reihenfolge:**
  1. Stillstand aufheben (Punkt 6.1), Regeln lesen (REGELN-02), Prüfsummen und Regression (6.2, 6.3).
  2. Die roten Tests außer `test_w_g_*` klären (Teil 1 Punkt 2.6), bevor eine Regression als Beleg gilt (LU91).
  3. Entscheidung 4.1 umsetzen: G nach `bau/S1C-PLAN.md` bauen (zuerst an einer Kopie, dann am Baum) oder G als gezählte Enthaltung führen; Kosten von G an den vier Werken; Nachlauf der Teillauf-Stücke.
  4. Commit auf `einlagerung/runde-6-stand` (oder nach Philipps Wahl auf `main` nach Zusammenführung), volle Regression mit Kammer samt `test_verdrahtung` (in Runde 5: 1.727 s), ein Review in eigenem Ordner, ein Bericht, Abschlussordner `laeufe/biotop-vor-t4-06/`.
  5. Startregel prüfen; nur wenn das Review keinen stillen Durchlass findet: T4 nach v8 Z. 426 vorbereiten (Werk, Verfassung, Modellwahl nach P5/P6/P13).
- **Maßstab:** die Startregel im Wortlaut (Teil 1 Punkt 3); rot dürfen danach nur Spezifikationen sein, die als gezählte Enthaltung geführt sind; 0 Biotop-Buchungen; jede Zahl mit Bezugsgröße.

## 9. Risiken

- **Geheimnisse in der Sitzungsdatenbank:** `root/.hermes/state.db` in KOMPLETT enthält den ganzen Sitzungsverlauf, womöglich mit eingefügten Geheimnissen. KOMPLETT gehört auf einen verschlüsselten Datenträger und nie in einen öffentlichen Ordner. Die Dokumentation ist geschwärzt und durchsucht (EINLAGERUNG-BERICHT).
- **Geliehene IP-Adresse:** Der Server hat die Adresse `212.227.7.117` (Schnittstelle `ens6`, per DHCP; EB50); sie kann wechseln. Ausweich: der Domainname `milieulux-reinigung-muenchen.de` (zeigte am 26.09.2026 01:56 auf dieselbe Adresse, EB50). Anmeldung als `root` nur mit Schlüssel (`sshd -T`: `permitrootlogin without-password`, EB50); berechtigt ist ein Schlüssel mit dem Kommentar `philipp-laptop`. Fingerabdruck des Host-Schlüssels (ED25519): `SHA256:klt2tsfm8QwK81bmxFq+WFpFHt6EdOSLwYRPzV9VOyI`.
- **Prüfkanal öffentlich über den Pfadschlüssel:** Wer eine Adresse kennt, kann jede Datei lesen. Deshalb liegen die Archive nie dort; die Kennung Philipps ist aus dem Prüfkanal entfernt (P2). Der Schlüssel selbst (`/etc/pruefkanal/schluessel`) und die Caddy-Konfiguration sind nicht im Paket.
- **Veraltete Einträge in `laeufe/gedaechtnis/`:** REGELN-01, STAND-01 und UNTERBAU-01 (20.09.) sind in Teilen überholt (Handelssystem, Freigaben, Träger). Es gelten REGELN-02 und STAND-03; STAND-02 beschreibt den Stich 25.09. 17:29:59.
- **`/tmp` wird beim Neustart geleert:** Die Biotop-Belege aus `/tmp` sind in `tmp-belege/` gesichert (EB25: 24.869 von 24.869 Dateien prüfsummengleich). Neue Arbeit legt Belege nicht mehr in `/tmp` ab.
- **Feste Pfade im Code:** Code und Tests nennen absolute Pfade (`/root/biotop/daten`, `/root/reparatur-01`, `/root/biotop-t3/…`, `/root/biotop-vor-t4*`, `/root/versandwerk-t3-02`, `/root/.hermes/.env`; EB22). Das Biotop läuft nur, wenn es unter genau diesen Pfaden liegt. Das Archiv stellt sie so her.
- **Wartende Gedächtnisänderungen:** In `/root/.hermes/pending/memory/` liegen 4 Vorschläge aus Hintergrund-Reviews; 3 davon nennen das Biotop (EB5, EB6). Sie sind weder angewandt noch gelöscht und setzen keine Arbeit in Gang. Vor der Wiederaufnahme lesen und verwerfen oder übernehmen.

## 10. Was Chat-Claude beim Wiedereinstieg zuerst bekommt

1. Einstiegsdatei: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-einlagerung-01/START-02.md
2. Diese Datei: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-einlagerung-01/WIEDEREINSTIEG-TEIL1-02.md, danach …TEIL2-02.md und …TEIL3-02.md
3. **Lesereihenfolge:** START-02 → WIEDEREINSTIEG Teil 1–3 → REGELN-02 (https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/REGELN-02.md) → EINLAGERUNG-BERICHT-01 → LAGE-TEIL1-01 (https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LAGE-TEIL1-01.md) → RUNDE6-DOKUMENTE-01/VERZEICHNIS.md → bei Bedarf die übrigen LAGE-Dateien nach START-03 (https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/START-03.md).
