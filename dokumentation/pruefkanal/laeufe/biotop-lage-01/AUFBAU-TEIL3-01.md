# BIOTOP-LAGE-01 · Fassung 2 · `AUFBAU-TEIL3-01.md`

- **Inhalt:** FK31–FK38 · Entwurf D, Stück 3 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil D, Arbeitszeit 25.09.2026 16:10:47–17:49:11 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/aufbau/AUFBAU-TEIL3.md` · 23848 B · SHA-256 `c6fb7e224fdb1abf1312dac5c3d09b096e21dfc80ea00d0602dc4d912aeeb839`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (33 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# AUFBAU — Teil 3 von 3 (FK36, FK37, FK38; Lücken und Widersprüche aus Teil D)

Bezugsstand, Lesezeitpunkt und Abkürzungen: siehe `AUFBAU-TEIL1.md` (Kopf).

**Umgebung** gelesen am 25.09.2026:
- 14:49 CEST: R2 (Prozesse, Dienste, Ports) und R3 (Prüfkanal)
- 16:15 CEST: R48 (Versionen, Abbilder)
- 16:22 CEST: R65

**Stichzeitpunkt:** Den Endstand der Runde 6 trägt Hermes nach.

---

## FK36 — Umgebung

### Sprachversionen (abgelesen, R48, 25.09.2026 16:15:19 CEST)
| Befehl | Ausgabe | Bemerkung |
|---|---|---|
| `python3 --version` | Python 3.12.3 | Wirt |
| `node --version` | v26.8.2 | `which node` zeigt `/root/.hermes/node/bin/node`: die Node-Installation von Hermes, nicht die des Biotops |
| `/opt/node22/bin/node --version` | v22.14.0 | Node 22 auf dem Wirt |
| `/root/biotop-t3/venv/bin/python --version` | Python 3.12.3 | T3-venv: pytest 9.1.1, pluggy 1.6.0, iniconfig 2.3.0, packaging 26.3, pygments 2.21.0 (Metadatenordner) |

`requirements-test.txt` am Commit: `pytest==9.1.1` (R34 E).

**In der Kammer** (Wortlaut der Dockerfiles am Commit, R40 §5; Versionen laut `package-lock.json`, R104 §1):
- `kammer/Dockerfile`:
  - `FROM python:3.12-slim`
  - `pip install … pytest==8.3.3 bandit==1.7.10 vulture==2.13`
  - Benutzer `kammer` (uid 10001), `WORKDIR /werk`
- `kammer/typescript/Dockerfile`:
  - Werkzeugstufe `FROM node:22-bookworm-slim@sha256:48e4b67d85f8…` mit `npm ci`
  - Endstufe `FROM biotop-kammer:1` mit Node-Binärdatei und `/opt/biotop-ts`
- TypeScript-Werkzeuge: typescript 5.7.3, vitest 2.1.8, eslint 9.17.0, typescript-eslint 8.18.2 (package.json), eslint-plugin-security 3.0.1, knip 5.41.1, tsx 4.19.2.
- Genaue Versionen im Abbild: Node in `biotop-kammer:ts1` und Python in `python:3.12-slim` sind **UNBEKANNT**.
  - Grund: Erlaubt war nur `docker images`.
  - Weg: Hermes liest `docker image inspect` oder das Bauprotokoll des Abbilds.
- **Eigene Abweichung** (Vermerk auch in `STAND.md`): R48 enthält neben den erlaubten Befehlen `docker --version`, `which node`, `/opt/node22/bin/node --version`, `ss -ltn` und `ls` der venv-Metadaten.
  - Alle lesen nur.
  - `docker --version` verstößt gegen den Wortlaut „nur `docker images`“.

### Docker (R48; Erstellzeiten R30 §4)
Docker 29.1.3, build 29.1.3-0ubuntu3~24.04.2.

| Abbild | ID | Plattenbedarf | erstellt |
|---|---|---|---|
| `biotop-kammer:1` | ce7bbe944118 | 231 MB | 18.09.2026 23:26:54 +0200 |
| `biotop-kammer:ts1` | 212e6212cd16 | 535 MB | 21.09.2026 02:47:15 +0200 |
| `node:22-bookworm-slim` | 48e4b67d85f8 | 329 MB | 19.09.2026 02:48:56 +0200 |
| `python:3.12-slim` | 78387bc3881b | 190 MB | 01.09.2026 02:12:40 +0200 |

- **Nutzung:** Jeder Bau, Testlauf und jede Messung läuft in der Kammer: `--network none`, eigene Werkkopie, Zeit- und Speicherlimit, unprivilegierter Benutzer, read-only-Wurzel, PID-Limit (Kopf kammer.py).
- **Container:** 0 laufend (R2, 14:49:28 CEST).
- **Kammer-Sperrdatei** `/tmp/biotop-kammer-exklusiv`:
  - fehlte um 14:49 (R2), 16:15 (R48) und 16:22 CEST (R65);
  - wird für exklusive Zeitmessungen gesetzt (`H-VOLL-AUSWERTUNG.txt` Z.2).

### Dienste und Zeitgeber (R2, 14:49 CEST; R4)
- **Biotop:**
  - kein systemd-Dienst, kein Zeitgeber, kein Prozess. R2 fand keinen Prozess mit biotop, pytest, kammer, vitest oder tsc im Befehl.
  - Unter den systemd-Diensten trägt keiner „biotop“ im Namen.
  - Von den 29 Zeitgebern gehört keiner zum Biotop.
  - root hat keine crontab (R2 Z.74).
- **Hermes-Zeitgeber** (`/root/.hermes/cron/jobs.json`, R2 Z.123–125):
  - `zwischenbericht-waechter`:
    - läuft jede Minute, aktiv, Skript `zwischenbericht_waechter.py`, 1.415 Ausführungen;
    - legt Zwischenberichte unter `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/<auftrag>/zwischenbericht-…` ab (R4).
  - `Endmeldung Runde 5 (vor T4)`: einmalig, ausgeführt am 24.09.2026 um 23:54:23, abgeschlossen.
- **Der Biotop-Dienst** läuft nur, wenn ihn jemand mit `biotop dienst` startet. Für die Torprüfung startet ihn `pruefung/tor1.py:100` selbst.

### Belegte Ports (R2, `ss -ltnp`, 14:49 CEST)
| Port | Bindung | Prozess | gehört zum Biotop |
|---|---|---|---|
| 22 | 0.0.0.0 und [::] | sshd | nein |
| 80, 443 | * | caddy | nein; liefert den Prüfkanal und die Website |
| 2019 | 127.0.0.1 | caddy (Verwaltung) | nein |
| 3000 | 127.0.0.1 | next-server | nein (Website, anderes Vorhaben) |
| 53 | 127.0.0.53, 127.0.0.54 | systemd-resolve | nein |
| 38493 | 127.0.0.1 | containerd | Unterbau von Docker |
| 8642 | — | — | Vorgabe des Biotop-Dienstes; frei um 14:49 (R2) und 16:15 CEST (R48) |

### Öffentlich erreichbar?
- **Prüfkanal: ja.**
  - Adresse: `https://milieulux-reinigung-muenchen.de/_akte/<schlüssel>/laeufe/…`, geschrieben als `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/…`.
  - Caddy liefert statisch aus `/var/pruefkanal/oeffentlich` (`/etc/caddy/Caddyfile` Z.114–168, R3).
  - Es gibt kein Inhaltsverzeichnis (Z.167: „/_akte/ allein verraet keinen Schluessel“).
  - Erreichbar sind die Abschlussordner und `gedaechtnis/` (FK38).
- **Dienst und Oberfläche: nein.**
  - Vorgabebindung `127.0.0.1:8642` (`__main__.py:65`; dienst.py:233, 241). `0.0.0.0` kommt im Code am Commit nicht vor (R112 §1).
  - Mit `--host` ließe sich eine andere Bindung wählen (`__main__.py:65`).
  - Caddy leitet 8642 nicht weiter: Die Caddyfile enthält „8642“ nicht, der einzige `reverse_proxy` zeigt auf 127.0.0.1:3000 (R65 §9).
  - Zum Lesezeitpunkt lief kein Dienst auf 8642.
  - Eine Adresse für die Bedienung vom Tablet (MP v8 Z.395) gibt es damit nicht → SOLL-IST.

---

## FK37 — Fähigkeitsstand
- **Maßstab:** „nachweislich“ heißt, ein Abschlussordner belegt die Fähigkeit an einem Lauf.
- **Wertungen und Torzeilen:** TORE. Die Zuordnung Lauf → Ordner stammt aus R30 §3.
- **Lauf 26 zweimal vergeben:**
  - Lauf 26 im Zweig VB1 = Vorbedingung 1.
  - Lauf 26 im Zweig T3 = erster T3-Lauf.
  - Beleg: unten, W9.

### Was das Biotop nachweislich kann
| Fähigkeit | Lauf (Werk) | Abschlussordner | Beleg |
|---|---|---|---|
| Python-Werk aufnehmen, kartieren, hart messen; versiegelte Schwächen finden und beheben (S1 nach „behoben heißt verschwunden“); Kassenabbruch, Lazarus-Rückkehr, Kammer-Zeitlimit, 401 ohne Token | Läufe 1–5 (Phase 1), 6–10 (Nachlauf; „Lauf 3“ des Masterprompts = DB-Lauf 9); Übungswerk `lagerhaus` | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/`, `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/` | MP v8 Z.370–372; R30 Z.94, 100–101 |
| vier Nischen mit Bandit, Generation 0 mit Mutanten, explizite Verträge, Verhandlung am Probenpaar, Pareto je Test; S2 (Leistungsbremse) behoben. Nicht dabei: Tor 2 Zeile 8 (Immunisierung, Doppelungsanteil) gerissen → TORE | Lauf 13 (Hauptlauf), Läufe 11–12 (Vorläufe); `lagerhaus` | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/` | MP v8 Z.390; R30 Z.107 |
| drei Gedächtnisse, Mentor, Entropie mit Selbstbeendigung, Jury (echter einstimmiger Fall), Web-Oberfläche hinter Anmeldung; zweites Übungswerk `logmuehle`, alle drei versiegelten Schwächen behoben | Läufe 14–20; `logmuehle` in Lauf 17 | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/` | MP v8 Z.410; Phase-3-BERICHT Z.137–170 |
| Generation minus eins: Rauschmessung, Sperre je Bereich, vier Proben am versiegelten Eichgegenstand, Fund-Neubewertung; Abbruch als Befehl; Artgedächtnis mit Mustern | Läufe 21–23 | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/` | MP v8 Z.412 |
| Ansage-Sperre (Bauteil A), werkübergreifender Block (Bauteil B), Aufnahmesperre C; Vorbedingung 1 am 21.09. abgenommen, darunter Tor 2 Zeile 8 (Doppelungsanteil; Zahl → TORE) | Läufe 24, 25 (STAMM) und 26 (VB1, natürlich gesättigt nach Generation 5); Zuordnung nach Nennung, Einzelheiten → CHRONIK | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/`; Reparaturen dazwischen: `…/biotop-reparatur-01/`, `…/biotop-reparatur-02/` | MP v8 Z.18, Z.323; R30 §3 und Z.133–135 |
| TypeScript-Werk `versandwerk` bearbeiten: Aufnahme, Kammer `ts1`, Mutanten, S1–S4 echt behoben (S5 offen; S2 in Lauf 38 „nicht belastbar“) | Läufe 26–38 (Zweig T3), zuletzt 37 und 38 | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/` mit `abschluss-03/` | MP v8 Z.456–461 |
| jedes Organ und jeder Registereintrag wird in einem ganzen Lauf gerufen (Verdrahtung) | kein DB-Lauf: Verdrahtungstest am Drahtwerk, Regression an `0c2f058`; Runde 5 als Ganzes nicht abgenommen | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-05/` | BERICHT Runde 5 Z.41–42; R30 Z.199 |

### Was es noch nicht kann oder was nicht belegt ist
1. **Kein Lauf seit Lauf 38** (T3, 22.09.2026).
   - Die Behebungsrunden 1–5 vor T4 melden je „Biotop-Modellgeld 0,00 €“ (R30 Z.176–200).
   - Ihre Wirkung ist nur in Tests, Gegenproben, Nachspielen aufgezeichneter Kandidaten aus den Läufen 37 und 38 und im Verdrahtungslauf belegt, nicht an einem Werk.
   - Keine der Runden 1–5 ist abgenommen. Wortlaut der Köpfe: „nicht abnahmereif“ (Runde 1), „nicht abgenommen“ (Runden 2, 3, 5), „die Fehlerklassen nicht“ (Runde 4) (R30 Z.175, 181, 187, 193, 199).
2. **T4 nicht begonnen.**
   - Startregel: „sobald das Review dieser Runde keinen stillen Durchlass mehr findet“ (UEBERGABE Runde 6 Z.21–22).
   - Runde 6 ist offen: S1c schrieb um 16:40 CEST noch in den Baum (`S1C-BAU-C.txt` Z.16).
3. **T5, T6 und Phase 5 nicht begonnen.** Für Phase 5 ist kein Werk gewählt (MP v8 Z.428–432, Z.480).
4. **T3 nicht abgenommen** (MP v8 Z.456–460):
   - Halluzinationsprobe gerissen;
   - Doppelungsanteil nach der Methode aus Vorbedingung 1 nicht gemessen;
   - Immunisierung auf dem TypeScript-Pfad nicht belegt;
   - S5 offen.
5. **Echte Uneinigkeit der Jury** nie beobachtet; die Uneinigkeit ist nur gestellt geprüft (MP v8 Z.404, Z.410).
6. **Geschmacksgedächtnis nur als Mechanik:**
   - In allen drei Zweigen beginnt `freigabe_grund` in 0 Generationen mit „Philipp“: 0 von 144 (STAMM), 0 von 150 (VB1), 0 von 184 (T3) (R72 §2).
   - Alle Freigaben stammen von Hermes unter Vollmacht oder stellvertretend.
7. **Kein Werk mit Betriebszweck bearbeitet.** Dort gibt nur Philipp frei (lauf.py:560–562).
8. **Verbundausfall** laut MP v8 Z.206 „noch nicht belegt“. Stand der Torzeile: TORE.
9. **Vertragsänderung durch den Schwarm selbst:**
   - Am Übungswerk nicht erzwingbar; sie steht in Tor 4 (MP v8 Z.387).
   - Im Verdrahtungslauf der Runde 6 wurde eine Verhandlung begonnen, das Paar aber durch den Verhaltensvergleich abgelehnt (H-VOLL-AUSWERTUNG Z.28).
10. **Nicht gebaut:**
    - Kern als eigener Prozess mit eigener Schreibrolle (datenbank.py:4–5).
    - tree-sitter und „Aktenschrank“ in der Landkarte (landkarte.py:3–4; „aktenschrank“ hat 0 Treffer im Code, R75 §2).
    - Speicher als Grenzmaß (messgeraet.py:21).
    - Verfassungsentwurf durch ein Modell (Kopf verfassung.py).
11. **Abo-Kontingent getrennt zählen:** nicht in Gebrauch; die Spalte `kontingent` ist nie größer als 0 (Teil 2, FK33, Befund 4).
12. **Oberfläche von außen:** Es gibt keine Adresse (FK36).
13. **Mentor im TypeScript-Pfad:** in den Läufen 26–38 nicht gebucht (Teil 2, FK33, Befund 3).
14. **Vollautomatik über mehrere Generationen:** erst, wenn das Messgerät über drei Werke ohne unbemerkten Rückschritt gearbeitet hat, und nur auf Philipps Satz (MP v8 Z.287).

---

## FK38 — Fundstellen
`https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` steht für den öffentlichen Prüfkanal. Arbeitsordner unter `/root` sind nicht öffentlich.

**Code**
- **Repository:** `/root/biotop` (git).
  - Stand der Runde 5: HEAD `0c2f058`.
  - Der Arbeitsbaum ist durch Runde 6 verändert (FK31).
  - Geschichte: 75 Commits (R13).
- **Code-Archive in Abschlussordnern:** Laut MP v8 Z.503 enthält jeder Ordner `biotop/`. Ob das zutrifft: NICHT GEPRÜFT (→ INVENTAR).

**Werke**
- **Quellordner:** `/root/uebungswerk`, `/root/uebungswerk-nachlauf`, `/root/uebungswerk-p2`, `-p3`, `-p3b`, `-p3c`, `-p3d`, `/root/uebungswerk2` (R65 §10).
  - Zuordnung laut Laufskripten (R40 §2):
    - `lauf7.sh:7` → `/root/uebungswerk`
    - `lauf_nachlauf.sh:7` → `-nachlauf`
    - `lauf_p2.sh:6` → `-p2`
    - `lauf_p3_anlegen.sh:7` → `-p3`
    - `lauf_p3_lauf18.sh:7`, `lauf_p3_lauf19.sh:7` → `-p3c`
    - `lauf_p3_lauf20.sh:7` → `-p3d`
- **Aufgenommene Kopien:** `/root/biotop/daten/werke/` mit 23 Einträgen, darunter `lagerhaus-*`, `logmuehle-17`, `logmuehle-23`, `versandwerk-t3-02` (R65 §11).
- **Lazarus-Archive:**
  - `/root/biotop/daten/lazarus/` mit 93 Dateien (R65 §11).
  - Das passt zu den Tabellen, gerechnet: 70 Zeilen der STAMM-Tabelle `lazarus` + 23 Archive der T3-Läufe 31 (1), 32 (3), 36 (3), 37 (7), 38 (9) = 93 = Zeilen der T3-Tabelle `lazarus` (R40 §7, R75 §4).
  - Die T3-Läufe 26–30 und 33–35 haben kein Archiv.
  - VB1: `/root/phase-4-vorbedingung-1/privat/lazarus/`, Lauf 26, Generationen 0, 1 und 3 (R104 §3).
- **Versiegelte Schwächen und Mutanten:** `/root/versiegelt/`, darunter `MUTANTEN-phase2.json` und `MUTANTEN-phase3.json` (genannt in `lauf_p2.sh:11`, `lauf_p3_anlegen.sh:12`; ob die Dateien vorhanden sind: NICHT GEPRÜFT). Der Inhalt ist versiegelt und wurde nicht gelesen.
- **Prüfwerk des Verdrahtungstests:** `tests/drahtwerk.py`.

**Verfassungen**
- **Übungswerke (am Commit):**
  - `verfassungen/lagerhaus.md` mit `lagerhaus.regeln.json`
  - `verfassungen/logmuehle.md` mit `logmuehle.regeln.json`
  - Verträge: `verfassungen/vertraege-lagerhaus/`, `vertraege-logmuehle/`
  - Wortlaut auch in MP v8 Anhang A (Z.520) und Anhang B (Z.536).
- **T3:** `/root/biotop-t3/VERFASSUNG-T3-02.md`, `VERFASSUNG-T3-ENTWURF.md` (R72 §4).
- **In der Datenbank:** Tabelle `verfassung_werk`.
- **Verfassung des Biotops:** MP v8 Abschnitt 2 (Z.96–110).

**Masterprompts**
- **Wortlaut v1–v8 aus der Sitzungsdatenbank:** `/root/sicherung/biotop-lage-01/arbeit/dokumente/<Zeit>_INFINITE-EVOLUTION-BIOTOP-Masterprompt-vN.md` (R17).
- **Kopien auf der Platte** (R17, R11):
  - v6:
    - `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6-01.md`
    - `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/quellen/MASTERPROMPT-FASSUNG-6.md`
    - `/root/phase-4-vorbedingung-1/uebergabe-quellen/MASTERPROMPT-FASSUNG-6.md`
  - v7: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/MASTERPROMPT-v7.md`
  - v8 nur als Tor-4-Auszug:
    - `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-05/MASTERPROMPT-V8-TOR4.txt`
    - `/root/biotop-vor-t4-05/bau/MASTERPROMPT-V8-TOR4.txt` (R11 Z.39–40)
  - Übrige Fassungen: ENTSCHEIDUNGEN (FK15).

**Kasse**
- **Datenbanken** mit den Tabellen `kasse` und `eichkosten`:
  - STAMM `/root/biotop/daten/biotop.db`
  - VB1 `/root/phase-4-vorbedingung-1/privat/biotop.db`
  - R02 `/root/reparatur-02/privat-cli/privat.db`
  - T3 `/root/biotop-t3/t3.db`
- **`KASSE.md` je Auftrag:**
  - in den Arbeitsordnern: `/root/biotop-vor-t4/KASSE.md` bis `/root/biotop-vor-t4-05/KASSE.md` und `/root/biotop-einstieg-20260921-0122/KASSE.md` (R72 §4);
  - im Prüfkanal: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/<ordner>/KASSE.md` (MP v8 Z.504).

**Gedächtnis**
- **Des Biotops:** Tabellen `artgedaechtnis`, `projektgedaechtnis`, `geschmack` in jeder Datenbank.
- **Hermes' Gedächtnis im Prüfkanal:** `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/` mit 5 Dateien vom 20.09.2026 05:17:33 (R26 Z.128); Wortlaut REGELN-01/STAND-01 in R31.

**Abschlussordner** (Bestand R26; Läufe nach MP v8 Z.317–324, Berichtsköpfen R30 §2 und Nennung R30 §3)
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/`: Läufe 1–5
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/`: Läufe 6–10
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/`: Läufe 11–13
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/`: Läufe 14–20
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/`: Läufe 21–23
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/`: Bestandsaufnahme vom 20.09., kein Lauf
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/`: Wiedereinstieg vom 20.09., kein Lauf
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/`: Läufe 24–26, mit `NACHGANG.md`, `NACHGANG-06.md` und `nach-reparatur-02/`
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/`, `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/`: Reparaturen vom 20.09.
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-einstieg-20260921-01/`: lesender Einstieg vom 21.09., kein Lauf
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/` mit `abschluss-03/`: T3, Läufe 26–38
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/`, `-02/`, `-03/`, `-04/`, `-05/`: Behebungsrunden 1–5, kein Lauf
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-06/`: Runde 6; 20 Dateien in 4 Unterordnern, geschrieben am 25.09. zwischen 00:06 und 01:12 CEST (R26 Z.120), darunter Zwischenberichte des Wächters (R4 Z.122–124)
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/`: diese Offenlegung

**Hermes' Planungs- und Tafeldateien** (R72 §4, R65 §12)
- **Runde 6 (laufend), `/root/biotop-vor-t4-06/`:**
  - `UEBERGABE.md`: Tafel mit Auftrag, Plan und „Stand (neueste zuletzt)“.
  - Bauaufträge: `BAU-S1-SONDE.md`, `BAU-S1-FORTSETZUNG.md`, `BAU-S1B-M2B.md`, `BAU-S1C-UNBEOBACHTET.md`, `BAU-S2-TOR4.md`, `BAU-S3-STUFE2.md`, `BAU-S4-VERDRAHTUNG.md`.
  - Weitere: `EINORDNUNG-U1-U4.md`, `S1-ABBRUCH.md`, `VERDICHTUNG-OPENROUTER.md`.
  - `bau/`: Teilläufe und Belege; jüngste Datei `S1C-PLAN.md`, 16:14:01 CEST.
  - `bau/hermes/`: eigene Dateien von Hermes, darunter `H-VOLL-AUSWERTUNG.txt`, `H-NACHARBEIT.md`.
  - `sperre/`: Sperren der Runde.
- **Runden 1–5**, `/root/biotop-vor-t4/` sowie `-02/` bis `-05/`:
  - je `UEBERGABE.md`, `BERICHT.md`, `REVIEW.md`, `REVIEW-AUFTRAG*.md`, `KASSE.md`;
  - ab `-02/` zusätzlich `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`;
  - dazu `-04/FEHLALARM-SICHERHEITSFILTER.md`, `-05/REVIEW-verworfen-erster-durchgang.md`, `-05/ZWEI-REVIEWS.md`.
- **T3:**
  - `/root/biotop-t3/`: `ABSCHLUSSBERICHT.md`, `ARBEITSTEILUNG.md`, `LAUF38-BERICHT.md`, `NACHTRAG-02.md`, `PRUEFPLAN-START.md`, `STAND-ARBEIT.md`, `ZWISCHENBERICHT-UEBERNAHME.md`, `ZWISCHENBERICHT-VORSPANN.md`; Laufskripte, z. B. `lauf32_kette.sh`, `lauf34_kette.sh`, `lauf37_kette.sh`, `lauf38_evolution.sh` (R75 §5).
  - `/root/biotop-t3/abschluss3/`: `ABSCHLUSS-03.md`, `REVIEW-03.md`, `REVIEW-AUFTRAG-03.md`, `SPERREN.md`, `UEBERGABE.md`.
- **Vorbedingung 1**, `/root/phase-4-vorbedingung-1/`: `UEBERGABE-PHASE-4.md`, `ERGEBNIS-DETAIL.md`, `MESSPLAN.md`, `AUFTRAG-REGELN.md`, `SITZUNGSWECHSEL.md`.
- **Reparaturen und Einstieg:**
  - `/root/reparatur-01/INTEGRATIONSENTSCHEIDUNG-RUNDE2.md`
  - `/root/reparatur-02/`: ohne `.md` auf der obersten Ebene
  - `/root/biotop-einstieg-20260921-0122/`: `ZWISCHENBERICHT.md`, `KASSE.md`
- **Zwischenbericht-Wächter:** `/root/.hermes/scripts/zwischenbericht_waechter.py` mit der Auftragstafel `/root/.hermes/zwischenbericht/auftrag.json` (R4).
- **Diese Offenlegung:** `/root/sicherung/biotop-lage-01/`; Teil D in `entwurf/aufbau/` (`STAND.md`, Belegskripte `d1_*` bis `d14_*`).

---

## Lücken und Widersprüche aus Teil D (Vorschlag für die Lückenliste)

### Widersprüche (jeweils beide Belege)
- **W1 Dienst:**
  - Der Kopf von dienst.py sagt „nur lesend in Phase 1“ und nennt 10 Routen (R38).
  - `ROUTEN` am Commit hat 19 Einträge, darunter 4 POST-Routen: anmelden, abbrechen, freigabe, richtung (R90 §7).
  - Tor 3 meldete „18 von 18 Routen ohne Token → 401“ (Phase-3-BERICHT Z.139).
  - `GET /` liefert ohne Token die Seite (dienst.py:146–148, R104 §4). Ob die Zahl 18 `GET /` ausnimmt oder eine Route später dazukam: NICHT GEPRÜFT.
- **W2 Bandit:**
  - Der Kopf von nischen.py sagt: Erfolg = „Kandidat überlebt den Ankläger“ (R38).
  - generation0.py:398, 454 bucht in der Nische „sicher“ den Testbau als Erfolg, wenn der Test „besteht und fängt“ (R112 §2).
  - Zahlen: Teil 2, FK33, Befund 1 (R98 §2–3).
- **W3 Präfix `schwer.`:**
  - kasse.py:33–34: „Eigene Zählung: zweck-Präfix "schwer."“.
  - Die Ansage mit schwerem Modell wird als `aegis.ansage.*` gebucht (aegis.py:655–658, 688–696). Anzahl in den T3-Läufen 26–38: Teil 2, FK33, Tabelle „In der Kasse benutzt“ (R75 §1).
- **W4 Kern:**
  - MP v8 Z.303: „eigener Prozess, eigene Datenbank-Rolle mit ausschließlichem Schreibrecht“.
  - datenbank.py:4–5: „ein Prozess. Rollentrennung … steht auf der Liste für danach“.
- **W5 Landkarte:**
  - MP v8 Z.154: tree-sitter; „Der bestehende Aktenschrank … wird Teil der Landkarte“.
  - landkarte.py:3–4: Python `ast`, tree-sitter „auf der Liste für danach“. „aktenschrank“ hat 0 Treffer (R75 §2).
- **W6 Grenzmaß Speicher:**
  - MP v8 Z.176 nennt Speicher als Grenzmaß.
  - messgeraet.py:21: „Speicher: nicht gemessen (Liste für danach)“ (R65 §3).
- **W7 Schwere Aufrufe und Jury:**
  - MP v8 Z.313 (Fassung vom 23.09.): schwere Modelle des Teams mit eigener Kontingentgrenze; Jury-Endurteil als schwerer Aufruf.
  - kasse.py:33–34: tokenabgerechnet über OpenRouter („Vorgabe Philipp 18.09.2026“); jury.py:19: drei Schnellmodelle; `kontingent` nie größer als 0 (Teil 2, FK33, Befund 4).
- **W8 Befehlszeile:**
  - Der Kopf von `__main__.py` nennt 14 Befehlszeilen (Z.3–16).
  - Der Parser kennt alle Unterbefehle aus FK34 (Teil 2; `__main__.py` Z.40–66). Es fehlen gerechnet 10: verfassung, vertraege, kurve, mentor, richtung, gedaechtnis, entropie, dienst, oberflaeche-belege, protokoll-pruefen.
- **W9 Lauf 26 zweimal vergeben:**
  - VB1: „+ Lauf 26“ als Vorbedingung 1, am 20.09.2026 (MP v8 Z.323).
  - T3: „13 Läufe (26–38)“ (MP v8 Z.457).
  - Gerechnet (die Buchungszahlen je Zweig gehören nach KASSE und stehen hier nur als Rechenweg):
    - T3-Kasse 6.673 − STAMM 4.070 = 2.603 Buchungen (R43 §2). Das entspricht „2603 Buchungen, Läufe 26–38“ in abschluss-03 (R30 Z.170).
    - VB1-Kasse 4.316 − 4.070 = 246 Buchungen für den VB1-Lauf 26, zuletzt am 20.09. um 20:16 UTC. Die T3-Läufe beginnen am 21.09. (R43 §2).
  - Es sind also zwei verschiedene Läufe mit derselben Nummer in zwei Zweigen.
- **W10 Lazarus-Pfad:**
  - lazarus.py:24 legt `/root/biotop/daten/lazarus` fest (R65 §2).
  - Die VB1-Archive des Laufs 26 liegen unter `/root/phase-4-vorbedingung-1/privat/lazarus/` (R104 §3).
  - Das ist kein Widerspruch im Code: Lauf 26 lief mit einem anderen Code-Stand.

### Lücken (Vorschlag)
- **L-D1 Masterprompt v8:**
  - Fehlt: v8 vollständig auf der Platte und im Prüfkanal. Es gibt ihn nur aus der Sitzungsdatenbank; auf der Platte liegt nur der Tor-4-Auszug (R17 Z.197–212, R11 Z.39–40).
  - Schließen: Hermes veröffentlicht den Wortlaut in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/`.
- **L-D2 Versionen in den Kammer-Abbildern:**
  - Fehlt: Node in `biotop-kammer:ts1` und Python in `python:3.12-slim`. Grund: nur `docker images` war erlaubt.
  - Schließen: Hermes mit `docker image inspect`.
- **L-D3 Arbeitsstand der Runde 6:**
  - Fehlt: Der nicht eingecheckte Stand ist nicht gezählt, der Endstand von S1c offen.
  - Schließen: Hermes.
- **L-D4 Volle Regression mit Integrationstests:**
  - Fehlt: Die letzte volle Regression wählte die Integrationsfälle ab (Zahl: FK35), darunter `test_t3_eichpfad`. Ein Lauf aller gesammelten Fälle am Commit: NICHT GEFUNDEN.
  - Schließen: Hermes, in der Kette der Runde 6.
- **L-D5 Freigabe über den Dienst:**
  - Fehlt: Welchen Wert `von` erhält `POST /laeufe/<id>/freigabe`? Das entscheidet, ob eine Freigabe über die Oberfläche als „Philipp“ gebucht wird. NICHT GELESEN.
  - Schließen: Hermes liest dienst.py.
- **L-D6 T3-Läufe ohne Archiv:**
  - Fehlt: Für die T3-Läufe 26–30 und 33–35 gibt es kein Lazarus-Archiv, auch keine Tabellenzeile (FK38, gerechnet). Ob diese Läufe vor dem Maß endeten: NICHT GEPRÜFT.
  - Schließen: CHRONIK oder Hermes.
- **L-D7 Leere `kontingent`-Werte:**
  - Fehlt: Im T3-Zweig ist die Zahl der Buchungen ohne `kontingent` gleich der Zahl mit Zweck `ausfall.hoechstfall` (Teil 2, FK33; R75 §1). Ob es dieselben Zeilen sind: NICHT GEPRÜFT.
  - Schließen: Hermes, eine Abfrage mit `mode=ro`.
- **L-D8 Tests je Modul:**
  - 11 von 44 Python-Modulen unter `biotop/` (ohne leere `__init__.py`) spricht keine Testdatei direkt an (R80 §1): dienst, anmeldung, befundklassen, diffwerk, py/verhalten, referenzlast/lagerhaus, referenzlast/logmuehle, oberflaeche, eichproben_ts, entropie, tor4.
  - Eine Messung der Testabdeckung: NICHT GEFUNDEN.
  - Schließen: Hermes. Die Wertung gehört nach SOLL-IST.
