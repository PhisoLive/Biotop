# BIOTOP-EINLAGERUNG-01 · INHALT-01 · Verzeichnis der Archive (Fassung 01, vor dem Packen)

- **Erstellt:** 26.09.2026 02:02:53 CEST von `arbeit/s5_inhalt01.py` (gezählt, nicht geschätzt).
- **Geltung:** Diese Fassung liegt im Archiv KOMPLETT. Sie zählt KOMPLETT aus dem Zwischenstand vor dem Packen; nicht mitgezählt sind
  diese Datei selbst und `MANIFEST-KOMPLETT.tsv` (entstehen danach). DOKUMENTATION ist nach Plan gezählt: Es wird erst nach der
  Wiederherstellungsprobe gepackt und enthält dann zusätzlich WIEDEREINSTIEG Fassung 02 und INHALT-02. **Gültig ist INHALT-02**
  (Abschlussordner und Archiv DOKUMENTATION) mit Bytes und SHA-256 beider Archive.
- **Pfade** im Archiv KOMPLETT sind relativ zu `/`: `root/biotop` entpackt nach `/root/biotop`. Einträge der dritten Ebene sind für
  `root/sicherung`, `usr/local` und `root/biotop-einlagerung` zusätzlich aufgeführt. „Dateien“ zählt reguläre Dateien; Verweise getrennt.
- **Ausgelassen** (je Datei im Protokoll `root/biotop-einlagerung/paket/protokoll-stufe-*.txt`, Grund je Zeile): Geheimnisdateien
  (nur Pfad), Abhängigkeits- und Zwischenspeicherordner, Datenbank-Begleitdateien (Inhalt steckt in der Backup-Kopie), das alte
  Archiv aus BIOTOP-LAGE-01 und dessen Reproduktionskopien, Laufzeitinstallationen unter `/root/.hermes` (node, lsp, bin).

### Archiv KOMPLETT (biotop-einlagerung-20260925-komplett.tar.gz)

Gesamt (gezählt über den Baum `/root/biotop-einlagerung/stufe`. ohne nichts): 3.579.658.905 Bytes in 87.291 Dateien, dazu 2432 Verweise.

| Eintrag | Zweck | Bytes | Dateien |
|---|---|---|---|
| `root/` | Inhalte aus /root (Biotop. Arbeitsordner. Sicherung. Hermes. Einlagerung) | 3.335.014.092 | 74.338 (+2432 Verweise) |
| └ `root/.hermes/` | Hermes-Zuhause ohne Geheimnisdateien: state.db (Sitzungen). Skills. Gedächtnis. Cron. Protokolle. Skripte | 498.457.695 | 976 |
| └ `root/biotop/` | Biotop-Repository mit .git: Code. Tests. Verfassungen. daten/ (biotop.db. Werke. Lazarus); Zweig einlagerung/runde-6-stand | 39.225.212 | 3.959 |
| └ `root/biotop-einlagerung/` | Dieser Auftrag: Arbeitsskripte. Rohbelege. Belege aus /tmp. Zwischenspeicher. Dokumentation. Kammer-Abbilder | 949.876.612 | 34.948 (+941 Verweise) |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/UEBERGABE.md` | Übergabetafel des Auftrags | 7.726 | 1 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/arbeit/` | Skripte dieses Auftrags (eb.py. s2_git.py. s5_paket.py. wa_vergleich.py …) | 203.243 | 54 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/auftrag/` | Auftrag BIOTOP-EINLAGERUNG-01 im Wortlaut | 24.789 | 1 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/ausgabe/` | Abschlussordner-Dateien vor der Veröffentlichung | 268.033 | 21 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/entfernt-aus-pruefkanal/` | P2: Original der Datei mit Philipps Telegram-Kennung (aus dem Prüfkanal verschoben) | 11.021 | 1 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/hermes-zwischenspeicher/` | Delegationsprotokolle und eingelegte Dokumente mit Biotop-Bezug | 3.377.425 | 80 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/kammer-abbilder/` | Docker-Abbilder der Kammer (docker save biotop-kammer:1 und :ts1) | 124.908.915 | 2 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/meldungen/` | Meldungen an Philipp (Text. Sende-Merkdatei) | 845 | 2 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/paket/` | Dokumentation (dokumentation/). Paketprotokolle | 183.325.999 | 11.656 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/protokolle/` | Protokolle der Hintergrundketten | 66.141 | 4 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/pruefsummen/` | Prüfsummenlisten (Git-Festschreibung. Probe) | 1.774.924 | 14 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/rohbelege/` | Rohbelege EB1 … (Befehl und vollständige Ausgabe) | 764.182 | 54 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/sperren/` | Sperren und Sicherheitsprüfungen im Wortlaut | 1.649 | 2 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/tmp-belege/` | Biotop-Belege aus /tmp (Reviews. Bauordner der Runden). prüfsummengleich kopiert | 635.113.702 | 23.050 (+941 Verweise) |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/vorher/` | Sicherungskopien vor Änderungen (MEMORY.md. auftrag.json) | 2.772 | 3 |
| &nbsp;&nbsp;└ `root/biotop-einlagerung/vorlagen/` | (ohne Eintrag) | 25.246 | 3 |
| └ `root/biotop-einstieg-20260921-0122/` | Einstieg 21.09. (Zwischenbericht. Kasse) | 275.918 | 17 |
| └ `root/biotop-t3/` | T3-Arbeitsordner: t3.db (Kasse/Läufe T3). Laufskripte. Berichte. Verfassung T3. Sicherungs-Repos | 672.653.158 | 4.727 |
| └ `root/biotop-vor-t4/` | Behebungsrunde 1 vor T4: Übergabe. Bericht. Review. Kasse | 1.055.148 | 102 |
| └ `root/biotop-vor-t4-02/` | Behebungsrunde 2 vor T4 | 562.550 | 60 |
| └ `root/biotop-vor-t4-03/` | Behebungsrunde 3 vor T4 | 1.005.302 | 88 |
| └ `root/biotop-vor-t4-04/` | Behebungsrunde 4 vor T4 | 886.339 | 113 |
| └ `root/biotop-vor-t4-05/` | Behebungsrunde 5 vor T4 (Regressionsbefehl job_kette.sh. REGRESSION.txt) | 1.364.519 | 159 |
| └ `root/biotop-vor-t4-06/` | Behebungsrunde 6 (unfertig): Übergabe. Bauaufträge S1–S4. S1b. S1c. bau/ (S1C-PLAN.md) | 2.668.960 | 395 |
| └ `root/gesamtstand-01/` | Bestandsaufnahme 20.09. | 31.666.556 | 39 |
| └ `root/phase-4-vorbedingung-1/` | Vorbedingung 1 (Läufe 24–26. Zweig VB1): privat/biotop.db. Werke. Lazarus | 46.146.367 | 536 (+15 Verweise) |
| └ `root/reparatur-01/` | Reparatur 01 (20.09.) | 868.740.005 | 24.595 (+1340 Verweise) |
| └ `root/reparatur-02/` | Reparatur 02 (20.09.): privat-cli/privat.db | 111.127.844 | 1.596 (+124 Verweise) |
| └ `root/sicherung/` | Sicherung aus BIOTOP-LAGE-01 | 104.654.679 | 1.386 (+12 Verweise) |
| &nbsp;&nbsp;└ `root/sicherung/biotop-lage-01/` | BIOTOP-LAGE-01: Arbeitsordner. Ausgabe. Entwürfe. Rohbelege; ohne altes Archiv und Reproduktionskopien | 104.654.679 | 1.386 (+12 Verweise) |
| └ `root/traeger-umstellung-2026-09-20_22-32-03Z/` | Trägerumstellung 20.09. | 3.183.245 | 78 |
| └ `root/uebungswerk/` | Übungswerk lagerhaus (Ausgang. Lauf 7) | 67.147 | 69 |
| └ `root/uebungswerk-nachlauf/` | Übungswerk für den Nachlauf | 55.353 | 43 |
| └ `root/uebungswerk-p2/` | Übungswerk Phase 2 | 41.590 | 29 |
| └ `root/uebungswerk-p3/` | Übungswerk Phase 3 | 52.079 | 40 |
| └ `root/uebungswerk-p3b/` | Übungswerk Phase 3 (b) | 54.464 | 42 |
| └ `root/uebungswerk-p3c/` | Übungswerk Phase 3 (c. Läufe 18/19) | 54.337 | 42 |
| └ `root/uebungswerk-p3d/` | Übungswerk Phase 3 (d. Lauf 20) | 54.318 | 42 |
| └ `root/uebungswerk2/` | Übungswerk 2 (logmuehle. Quelle) | 70.336 | 67 |
| └ `root/versandwerk-t3/` | T3-Werk. erste Fassung (Rolle UNBEKANNT. LAGE FK25) | 97.367 | 39 |
| └ `root/versandwerk-t3-02/` | T3-Werk versandwerk (TypeScript). Ausgang | 103.423 | 41 |
| └ `root/versiegelt/` | Versiegelte Schwächen und Mutanten (Phase 2/3) | 515.808 | 40 |
| └ `root/w7/` | Arbeitsordner W7 (20.09.); ohne 07-codex-token.txt (Geheimnisdatei) | 46.727 | 42 |
| └ `root/wiedereinstieg-01/` | Wiedereinstieg 20.09. | 251.034 | 28 |
| `usr/` | Inhalte aus /usr (Hermes-Agent-Quelltext) | 244.644.813 | 12.953 |
| └ `usr/local/` | Hermes Agent unter /usr/local/lib/hermes-agent | 244.644.813 | 12.953 |
| &nbsp;&nbsp;└ `usr/local/lib/` | (ohne Eintrag) | 244.644.813 | 12.953 |


### Archiv DOKUMENTATION (biotop-einlagerung-20260925-dokumentation.tar.gz), Stand vor dem Packen

Gesamt (gezählt über den Baum `/root/biotop-einlagerung/paket`. ohne ['dbliste.json'. 'geheimsuche-befunde-20260926-020145.tsv'. 'protokoll-stufe-1-biotop.txt'. 'protokoll-stufe-2-arbeitsordner.txt'. 'protokoll-stufe-3-sicherung-lage-01.txt'. 'protokoll-stufe-4-hermes.txt'. 'protokoll-stufe-5-hermes-agent.txt'. 'protokoll-stufe-6-einlagerung.txt']): 185.497.421 Bytes in 11.664 Dateien.

| Eintrag | Zweck | Bytes | Dateien |
|---|---|---|---|
| `dokumentation/` | Dokumentation des Biotops (geheimnisfrei geprüft) | 183.325.999 | 11.656 |
| └ `dokumentation/WIEDEREINSTIEG-TEIL1-01.md` | Wiedereinstieg Fassung 01 (vor der Probe). Teil 1 | 17.580 | 1 |
| └ `dokumentation/WIEDEREINSTIEG-TEIL2-01.md` | Wiedereinstieg Fassung 01. Teil 2 | 17.486 | 1 |
| └ `dokumentation/WIEDEREINSTIEG-TEIL3-01.md` | Wiedereinstieg Fassung 01. Teil 3 | 7.359 | 1 |
| └ `dokumentation/auftraege/` | Aufträge BIOTOP-LAGE-01 (Fassung 2) und BIOTOP-EINLAGERUNG-01 | 66.028 | 2 |
| └ `dokumentation/dokumente/` | Eingelegte Prüf- und Abnahmedokumente Chat-Claudes (20.09.) und der LAGE-Auftrag | 113.564 | 9 |
| └ `dokumentation/gedaechtnis/` | REGELN-02 und STAND-03 (auch im Prüfkanal laeufe/gedaechtnis/) | 15.538 | 2 |
| └ `dokumentation/masterprompt/` | Masterprompt v1–v8 im Wortlaut mit Änderungsverzeichnissen und Bruchstücken | 509.418 | 18 |
| └ `dokumentation/pruefkanal/` | Kopien aller Biotop-Ordner des Prüfkanals (laeufe/biotop-*. gedaechtnis). geschwärzt geprüft | 178.862.455 | 11.535 |
| └ `dokumentation/umgebung/` | Umgebung: Betriebssystem. Python/Node. pip freeze. Sperrdateien. Kammer-Bauweg. Hermes. Skills | 160.894 | 13 |
| └ `dokumentation/verfassungen/` | Verfassungen im Wortlaut (Biotop-Repository. T3. LAGE-Auszüge) | 128.186 | 17 |
| └ `dokumentation/verlauf/` | Verlauf Philipp ↔ Hermes zum Biotop seit 18.09.2026 im Wortlaut (geschwärzt) | 3.427.491 | 57 |

