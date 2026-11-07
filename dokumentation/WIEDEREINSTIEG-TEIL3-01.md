# BIOTOP-EINLAGERUNG-01 · WIEDEREINSTIEG · Teil 3 von 3 (Fassung 01)

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
3. **Regression mit Kammer** (Befehl der Runde 5, `/root/biotop-vor-t4-05/job_kette.sh` Z. 37–40; ohne Modellaufruf; Laufzeit in Runde 5: 2.457,93 s für 598 bestanden, 2 übersprungen, 93 abgewählt):
   ```bash
   mkdir -p /root/<auftrag>/tmp && cd /root/biotop
   env BIOTOP_KAMMER_IMAGE=biotop-kammer:ts1 BIOTOP_AUFTRAG_LAUF_AB=26 BIOTOP_AUFTRAG_BUDGET_EUR=10 \
       T3_VERDRAHTUNG_BELEG=/root/<auftrag>/VERDRAHTUNG-BELEG-REGRESSION.json TMPDIR=/root/<auftrag>/tmp \
       /root/biotop-t3/venv/bin/python -m pytest tests/ -q -m "not integration" -p no:cacheprovider -rfEs --durations=8 \
       --junitxml=/root/<auftrag>/REGRESSION.junit.xml > /root/<auftrag>/REGRESSION.txt 2>&1
   ```
   `TMPDIR` auf einen eigenen Ordner setzen (Entscheidung Hermes in der Probe): pytest räumt sonst ältere Ordner unter `/tmp/pytest-of-root/` weg, und die Kammer braucht einen Pfad, den der Docker-Dienst sieht.
4. **Dann der erste Auftrag nach Punkt 8.**

## 7. Wiederaufnahme, Weg B — neuer Server aus dem Laptop-Paket (leeres Ubuntu 24.04)

- **Fassung 01 dieser Datei** liegt im Archiv KOMPLETT und entstand vor der Wiederherstellungsprobe. Die Schritte von Weg B mit den Rohbelegen der Probe stehen in Fassung 02: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-einlagerung-01/WIEDEREINSTIEG-TEIL3-02.md
- Kurzfassung (gelesen, nicht ausgeführt): Archiv hochladen (`scp`), mit `sha256sum` prüfen, nach `/` entpacken (`pigz -dc … | tar --numeric-owner -C / -xpf -`), Docker und Python-Umgebungen einrichten, Kammer-Abbilder laden (`docker load -i /root/biotop-einlagerung/kammer-abbilder/biotop-kammer-1-und-ts1.docker-save.tar`), Geheimnisse von Hand eintragen (`/root/.hermes/.env`, `/root/.hermes/auth.json`), Hermes Agent v0.21.2 (Git `abf47063`) einrichten, Manifest vergleichen, Regression wie in Weg A.

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

## 10. Was Chat-Claude beim Wiedereinstieg zuerst bekommt

1. Einstiegsdatei: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-einlagerung-01/START-02.md
2. Diese Datei: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-einlagerung-01/WIEDEREINSTIEG-TEIL1-02.md, danach …TEIL2-02.md und …TEIL3-02.md
3. **Lesereihenfolge:** START-02 → WIEDEREINSTIEG Teil 1–3 → REGELN-02 (https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/REGELN-02.md) → EINLAGERUNG-BERICHT-01 → LAGE-TEIL1-01 (https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LAGE-TEIL1-01.md) → RUNDE6-DOKUMENTE-01/VERZEICHNIS.md → bei Bedarf die übrigen LAGE-Dateien nach START-03 (https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/START-03.md).
