# UEBERGABE BIOTOP-LAGE-01 · Fassung 2 (Arbeitsstand für einen Nachfolger)

**Auftrag:** `/root/sicherung/biotop-lage-01/auftrag/BIOTOP-LAGE-01-Auftrag-v2.md`, SHA-256 `58ba8834…6b98`, gleich dem Original im Dokumentenspeicher (R16).

**Nur sichern, lesen, berichten.**
- Am Biotop nichts ändern, nichts löschen, nichts überschreiben, keine bezahlten Modellaufrufe.
- Etwas anlegen nur an drei Stellen: `/root/sicherung/biotop-lage-01/`, Abschlussordner `laeufe/biotop-lage-01/` und `laeufe/gedaechtnis/`.

## Werkzeuge (in `/root/sicherung/biotop-lage-01/arbeit/`)
- `rb.py "<Titel>" "<Befehl>" [<Anzeige>]`: Rohbeleg `rohbelege/R000n.txt`, exklusiv nummeriert. Enthält Befehl, Skriptinhalt und vollständige Ausgabe.
- `rb_buendeln.py <NN> <von> <bis>`: bündelt Rohbelege nach `ausgabe/ROHBELEGE-TEILk-NN.txt`, je ≤ 40.000 Bytes.
- `fuellen.py <vorlage> <ziel>`: ersetzt `{BASIS}` und `{LAEUFE}` durch volle Adressen.
- `pk.py <name> …`: veröffentlicht exklusiv nach `laeufe/biotop-lage-01/` und prüft den Abruf. `pk.py --abruf …` prüft nur.
- `geheimnis.py <pfad>`: Geheimnissuche nach Muster und nach Werten aus `.env`/`auth.json` (ab 8 Zeichen).
- `or_stand.py <marke>`: OpenRouter-Nutzungsanzeige, kein Modellaufruf.
- `verlauf_extrakt.py`: erzeugt `arbeit/verlauf/wortlaut.jsonl` (geschwärzt) und `nachrichten.jsonl` (ohne Inhalt) ab 18.09.
- `f12_philipp.py` und `f13_lesen.py`: Lesefassungen in `arbeit/lesen/`.

## Stand (25.09.2026, CEST)
- **14:44:20** Auftrag eingegangen. **14:49–15:05** Schritt 1 (R1–R6):
  - Biotop unter `/root/biotop`.
  - Kein Biotop-Lauf. Es läuft der Bau S1c der Runde 6 (Subagent `deleg_c88798ee` / `sa-0-d3ed819f`, seit 12:51:42).
- **15:09** Ordner `laeufe/biotop-lage-01/` angelegt; `START-01.md` (`e31c4f5d…158c`) und `ROHBELEGE-TEIL1..3-01` veröffentlicht (R10).
- **15:12:05** Meldung 1 per Einmal-Job `b11464763130` ausgelöst; im Zustellbuch um 15:13:04 als `delivered` verbucht (R32, R33).
- **15:12–15:58** Quellen erhoben (R11–R31):
  - Fundorte, Sitzungsdatenbank, git, Dokumente v1–v8;
  - Kassen aller Zweige, Abschlussordner;
  - Nachrichtenverzeichnis ab 18.09. in `arbeit/verlauf/` und `arbeit/lesen/`;
  - Platz und Geheimnisdateien (R28), Fakten (R30, R31).
- **16:05** Acht Entwurfs-Subagenten gestartet (`deleg_bbbc3cef`, nur lesend, Ordner `entwurf/<teil>/`):

  | Subagent | Teil |
  |---|---|
  | `sa-0-a7f3cf17` | A ENTSCHEIDUNGEN |
  | `sa-1-240d5ba4` | B VERFASSUNGEN |
  | `sa-2-47d9971d` | C TORE |
  | `sa-3-8bba1866` | D AUFBAU + GLOSSAR |
  | `sa-4-bebee69e` | E SOLL-IST |
  | `sa-5-dcae7dfb` | F CHRONIK |
  | `sa-6-cacf4392` | G LAGE-Werke/WS |
  | `sa-7-ce3c6b70` | H LAGE-Offen |

  Regeln: `entwurf/REGELN-FUER-TEILE.md`; Aufträge: `entwurf/AUFTRAG-*.md`.
- **16:24** Selbsttest des Sicherungswerkzeugs `arbeit/sich.py` an einem erfundenen Baum, grün (R70):
  - Auslassungen (.env, auth.json, node_modules, __pycache__, -wal) greifen;
  - DB-Backup mit gefüllter -wal: 500 von 500 Zeilen, Original unverändert;
  - integrity_check 2 von 2 ok;
  - Probe: Unterschied leer;
  - Gegenprobe: genau 1 Datei gemeldet;
  - Vergleichsgegenprobe: genau 1 Eintrag.
- **16:27 SPERRE-01** (`sperren/SPERRE-01.md`): Der Gateway-Lebenszyklus-Wächter sperrte eine lesende Zählung über `arbeit/verlauf/wortlaut.jsonl` und R22.
  - Nicht nachgeholt; die Zahlen liegen in R19, R22 und R23 vor.
  - Vorsorge: Wortlaut-Dateien nie als Argument auf der Befehlszeile nennen. Alle Subagenten sind per steer informiert.
- **16:30** Subagent I INVENTAR gestartet (`deleg_69c683dc` / `sa-0-484a7bad`). Er baut `entwurf/inventar/inventar.py` (I1–I8, Abgleiche 1–9, Tagesbilanz, Gegenprobe, KASSE/LISTEN). Hermes führt es nach dem Stichzeitpunkt erneut aus.

## Entscheidungen Hermes (bisher)
- **S1c wie einen laufenden Lauf behandeln:** Er wird nicht angehalten; Stichzeitpunkt ist sein Ende. Danach ruht Runde 6: kein Commit, kein weiterer Bau.
- **Zwischenbericht-Wächter `26fbb1513a1a`: umgestellt um 15:41** (R24).
  - `auftrag.json` zeigt auf `biotop-lage-01`; die alte Datei ist gesichert als `auftrag.json.vor-biotop-lage-01`.
  - Grund: Ein automatischer Zwischenbericht gehört zum laufenden Auftrag. Unter `biotop-vor-t4-06` würde er einen fremden, ruhenden Ordner beschreiben.
  - Die Datei liegt in `/root/.hermes/`, also außerhalb des Biotops. **Nach Abschluss zurückstellen**, wenn Runde 6 weiterläuft.
- **Geheimnissuche:**
  - Großgeschriebene Variablennamen aus `auth.json` sind Bezeichnungen, kein Geheimnis.
  - Werte aus `.env` werden ab 8 Zeichen gesucht, damit auch Chat- und Benutzerkennungen erfasst sind.
- **Datenbanken im Baum** (`/root/biotop/daten/biotop.db`, WAL 0 Bytes): nur mit `immutable=1` lesen, damit `-shm` im Baum unberührt bleibt.
- **`git status`** nur mit `--no-optional-locks`, damit der Index nicht geschrieben wird.

## Nächste Schritte
1. **Warten auf S1c** (Ende = Stichzeitpunkt) und auf die acht Entwurfsteile. Ihre Ergebnisse kommen als eigene Nachrichten.
2. **Nach dem Ende von S1c:**
   - VORHER-Prüfsummen (`s2_vorher.py`); Repository-Stand;
   - Sicherung (`s2_*`-Skripte): Datenbanken per Backup mit `integrity_check`, Zwischenkopie, Manifest, Archiv;
   - Wiederherstellungsprobe und Gegenprobe; Prüfung auf Ablage 2.
3. Inventare I1–I8 mit Abgleich, Tagesbilanz und Gegenprobe; `KASSE-01.csv`, `LISTEN-01.txt`.
4. Entwurfsteile prüfen und einsetzen: `LAGE` (FK01–FK07, FK47–FK49 selbst), dann `VERLAUF`, `MASTERPROMPT-GUELTIG`, `VOLLSTAENDIGKEIT`.
5. **Zum Schluss:**
   - NACHHER-Prüfsummen; Geheimnissuche mit Gegenprobe;
   - `gedaechtnis/STAND-02.md`;
   - START-Endfassung, `DATEIEN`, `PRUEFSUMME`, `ABRUFPROBE`;
   - Meldung 2 mit START, LAGE und VOLLSTAENDIGKEIT als Anhang.
