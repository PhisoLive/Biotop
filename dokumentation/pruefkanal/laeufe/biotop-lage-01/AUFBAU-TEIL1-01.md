# BIOTOP-LAGE-01 · Fassung 2 · `AUFBAU-TEIL1-01.md`

- **Inhalt:** FK31–FK38 · Entwurf D, Stück 1 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil D, Arbeitszeit 25.09.2026 16:10:47–17:49:11 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/aufbau/AUFBAU-TEIL1.md` · 28298 B · SHA-256 `453bab1f497c574f4fd05d7e598bc2c470c7e61f7fc96ccf4cf5a2b533419a7d`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (0 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# AUFBAU — Teil 1 von 3 (FK31, FK32)

Entwurf Teil D der Offenlegung BIOTOP-LAGE-01 Fassung 2, geschrieben im Auftrag von Hermes (HERMES-1). Teil 2: FK33–FK35 (`AUFBAU-TEIL2.md`), Teil 3: FK36–FK38 mit Lücken und Widersprüchen (`AUFBAU-TEIL3.md`).

**Bezugsstand für jede Zahl zum Code: Commit `0c2f058`** (`0c2f058d57f68b8891b535d6e00214172c82fefa`, 24.09.2026 20:24:54 +0200, „Vor T4, Runde 5 …“; R34 A). Gezählt nur lesend mit `git ls-tree`, `git show`, `git cat-file`: kein Checkout, kein Import von Biotop-Code.
- **Lesezeitpunkt:** 25.09.2026, 16:12–17:21 CEST (R34 16:12, R40 16:13, R43 16:14, R48 16:15, R56 16:17, R65 16:22, R72 16:26, R75 16:27, R80 16:33, R90 16:43, R98 16:49, R104 17:02, R112 17:20).
- **Arbeitsstand der Runde 6 ist nicht gezählt.** Der Baum `/root/biotop` weicht vom Commit ab: S1c schrieb um 16:40:47 CEST in `biotop/organe/verhaltensvergleich.py` (`/root/biotop-vor-t4-06/bau/S1C-BAU-C.txt` Z.16–23). Den Endstand trägt Hermes nach.
- **Zeilen** heißt: physische Zeilen je Datei, also Zeilenumbrüche einschließlich Leer- und Kommentarzeilen (`d1_code.py`, Wortlaut in R34 Z.59–62).
- Pfade ohne Wurzel sind relativ zu `/root/biotop` am Commit. **MP v8** = `/root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-23_155353_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md` (Wortlaut aus der Sitzungsdatenbank, R17). „Z.“ = Zeile, „Kopf“ = Modul-Docstring (R38).
- **Zahlen aus anderen Teilen:**
  - Kosten und Budgets → CHRONIK (FK20), KASSE
  - Torzeilen, Messgerätfehler → TORE
  - Umfang je Werk → LAGE (FK25)
  - Fassungen → ENTSCHEIDUNGEN (FK15)

---

## FK31 — Verzeichnisbaum, Sprachen, Zeilen

**Umfang am Commit** (abgelesen, R34 A):
- 1.850.710 Bytes; 0 binäre Dateien.
- Dateien und Zeilen: Summenzeile der Sprachtabelle unten.

**Nicht im Commit:**
- Nach `.gitignore` (R34 E): `daten/` (Datenbank, Werke, Lazarus-Archive), `__pycache__/`, `*.pyc`, `.env*`, `.venv/`, `.pytest_cache/`.
- Abhängigkeitsordner (`node_modules`, `venv`) sind nicht eingecheckt.

### Baum bis Tiefe 3
Abgelesen aus R34 B. Angegeben sind [Dateien, Zeilen] je Ordner und (Zeilen) je Datei.
```
.gitignore (6) · README.md (47) · pytest.ini (6) · requirements-test.txt (1)
biotop/ [69, 14.221]
  __init__.py (0) · __main__.py (166) · dienst.py (245) · lauf.py (854) · nachspiel.py (298)
  oberflaeche.py (172) · tor4.py (145)
  anbieter/ [1, 246]    __init__.py (246)
  kern/ [37, 5.581]     __init__.py (0) · anmeldung.py (50) · befundklassen.py (158) · datenbank.py (101)
                        diffwerk.py (128) · gegenzeugen.py (79) · kasse.py (313) · messgeraet.py (878)
                        protokoll.py (57) · register.py (56) · sprachprofil.py (38) · typescript.py (185)
                        py/ [1, 1.769] · referenzlast/ [4, 454] · ts/ [20, 1.315]
  organe/ [24, 6.514]   __init__.py (0) · aegis.py (1.174) · aufnahme.py (196) · eichgegenstand.py (199)
                        eichproben.py (634) · eichproben_ts.py (122) · eichung.py (267) · entropie.py (103)
                        fundpruefung.py (193) · gedaechtnis.py (595) · generation0.py (469) · genesis.py (185)
                        jury.py (62) · kammer.py (124) · landkarte.py (273) · lazarus.py (110)
                        masseichung.py (186) · mentor.py (136) · neutralzaehler.py (99) · nischen.py (161)
                        verfassung.py (69) · verhaltensvergleich.py (754) · vertraege.py (85) · vorspann.py (318)
kammer/ [4, 3.675]      Dockerfile (4) · typescript/ [3, 3.671]
pruefung/ [63, 4.422]   54 Python-, 9 Shell-Skripte (Namen unten)
pruefung_vorbedingung1/ [11, 924]
tests/ [60, 8.750]      Testdateien und Hilfsdateien (Namen unten; Zahl je Art: FK35)
verfassungen/ [11, 295] lagerhaus.md (7) · lagerhaus.regeln.json (12) · logmuehle.md (7) · logmuehle.regeln.json (10)
                        vertraege-lagerhaus/ [3, 126] · vertraege-logmuehle/ [4, 133]
```
**Unter Tiefe 3** (R34 C3, R38 A1):
- `kern/py/verhalten.py` (1.769).
- `kern/referenzlast/`: `lagerhaus.py` (119), `logmuehle.py` (140), `versandwerk-t3-02.mjs` (106), `versandwerk-t3-02.stufe2.mjs` (89).
- `kern/ts/`: 20 `.mjs`-Dateien: ast, bau, deck-setup, deckung, einwickeln, eslint.config, kanon, main, messen, mutanten, referenz, referenz-runner, reporter, statik, testlauf, tests-ast, verhalten, verhalten-runner (435), vitest.config, vitest.deck.config.
- `kammer/typescript/`: `Dockerfile` (18), `package.json` (15), `package-lock.json` (3.638).

**`pruefung/`** (Prüfskripte von Hermes für Torzeilen, Nachgänge und Laufketten; R34 B), 63 Dateien:
- Python: abbruch_pruefen, anklaeger_vielfalt, archivierung_pruefen, aufnahmesperre_gegenprobe, aufnahmesperre_pruefen, bauteilA_mechanik, behauptungen_nachtragen, doppelungen_befund, doppelungen_neu, eichgegenstand_betriebszweck, eichgegenstand_pruefen, eichgegenstand_verfassung, eichproben_pruefen, eichung_falld, eichung_pruefen, eichung_zeitraum_pruefen, funde_neubewerten, funde_uebernehmen, fundpruefung_pruefen, jury_mechanik, jury_probe, kurve, lauf16/18/19_verwerfen, lauf25_auswertung, lauf25_pfadnachweis, muster_nachtragen, nachgang_n1, n2_n3, n4_n5, n7_n9, n10, n12, n13_n14, nachprobe_zeile7, proben_ausserhalb_gedaechtnis, proben_tor2, probenmerkmal_pruefen, projektgedaechtnis_differenz, rauschprobe_lauf19, rauschregeln_pruefen, schwaechen_pruefen, tor1, tor1_f2, tor2, tor3, tor3_geschmack, tor3_oberflaeche, verhandlungsprobe, vorbedingung1, vorspann, zeile8_messung, zwischenbericht.
- Shell: generationen, lauf7, lauf_nachlauf, lauf_p2, lauf_p3_anlegen, lauf_p3_lauf18, lauf_p3_lauf19, lauf_p3_lauf20, lauf_p3_werk2.

**`pruefung_vorbedingung1/`**: auswerten, bauteile_pruefen, bestand_erheben, lauf_kommando, liefern, messen, schlussdiagnose, uebergabe_schreiben, vorbereiten, zaehlen, zaehler_pruefen.

**`tests/`**:
- Hilfsdateien: `conftest.py` (67), `drahtwerk.py` (179), `speicherwerk.py` (187).
- Testdateien `test_*.py`: ansage_aufnahme, artvorlage, doppelungsschluessel, eichproben, junit_zeugen, kernmass_pareto, messnachweise, nachweis_verbraucher, rauschmessung, review_vertrag, die Reihe `test_t3_*`, testreihenfolge, typescript_adapter, verdrahtung, vor_t4, vor_t4_02 … _05, vorspann, vorspann_cli.
- Einteilung nach Art: FK35 (Teil 2).

### Sprachen gesamt (abgelesen, R34 C1)
| Sprache | Dateien | Zeilen |
|---|---|---|
| Python | 179 | 26.872 |
| JSON | 4 | 3.675 |
| JavaScript (`.mjs`) | 22 | 1.510 |
| Shell | 9 | 194 |
| Markdown | 3 | 61 |
| Dockerfile | 2 | 22 |
| git-Konfiguration, INI, Text | je 1 | 6, 6, 1 |
| **Summe** | **222** | **32.347** |

TypeScript-Quelltext liegt am Commit nicht im Baum. TypeScript kommt nur in den Werken vor; die Werkzeuge dafür stecken im Kammer-Abbild (FK36).

### Sprachen und Zeilen je Bauteil (abgelesen, R34 C2)
| Bauteil | Dateien, Zeilen | davon |
|---|---|---|
| Wurzel | 4, 60 | Markdown 1/47, git 1/6, INI 1/6, Text 1/1 |
| `biotop/` Paketwurzel | 7, 1.880 | Python |
| `biotop/anbieter/` | 1, 246 | Python |
| `biotop/kern/` | 37, 5.581 | Python 15/4.071, JavaScript 22/1.510 |
| `biotop/organe/` | 24, 6.514 | Python |
| `kammer/` | 4, 3.675 | JSON 2/3.653, Dockerfile 2/22 |
| `pruefung/` | 63, 4.422 | Python 54/4.228, Shell 9/194 |
| `pruefung_vorbedingung1/` | 11, 924 | Python |
| `tests/` | 60, 8.750 | Python |
| `verfassungen/` | 11, 295 | Python 7/259, JSON 2/22, Markdown 2/14 |

- **Gegenprobe:** Die vier `biotop/`-Zeilen der Tabelle ergeben zusammen die Ordnerzeile `biotop/` im Baum (gerechnet 7+1+37+24 Dateien, 1.880+246+5.581+6.514 Zeilen). Zeilen je Modul stehen im Baum oben.

---

## FK32 — Bauteile

**Form je Bauteil:** Zweck mit Schnittstelle, Ort und Prüfweise, gelesen am Commit (Kopf nach R38, Zeilen nach R40/R43/R65/R90).

**Prüfweise:**
- **Testdateien:** Zahl der Testdateien unter `tests/`, die das Modul importieren oder über den Modulnamen ansprechen. Gezählt wird per Textsuche am Commit (R80 §1). „0“ heißt: kein direkter Zugriff. Die Zahl sagt nichts über die Tiefe der Prüfung.
- **Pflichtkante:** Eintrag im Register `kern/register.py` (`VERLANGT`, 10 Einträge am Commit, R80 §2). Der Verdrahtungstest verlangt jeden Eintrag als Aufrufkante im echten Lauf. Zusätzlich muss jedes Modul unter `organe/` gerufen werden (Kopf von register.py).
- **Tor:** die Torzeile, die das Bauteil prüft. Ergebnisse stehen in TORE.

### Die zehn Pflichtbauteile, dazu Geschmacksgedächtnis und Bauteil A
- **Kern (unantastbarer Kern)**
  - *Ort:* `biotop/kern/` [37, 5.581].
  - *Soll:* Messgerät, eingefrorenes Maß, Verfassungen, Lazarus, Kasse, Protokoll, Biotop-Code (MP v8 Abschnitt 5, Z.294–301). Technisch als „eigener Prozess, eigene Datenbank-Rolle mit ausschließlichem Schreibrecht“ (Z.303).
  - *Ist:*
    - Kern ist ein Modulpaket im selben Prozess.
    - `kern/datenbank.py:4–5`: „Phase 1: eine Datei, ein Prozess. Rollentrennung (eigener Kern-Prozess mit ausschließlichem Schreibrecht) steht auf der Liste für danach.“
  - *Prüfweise:* je Kernmodul, siehe unten.
- **Schwarm (Genesis)**
  - *Ort:* `organe/genesis.py` (185).
  - *Zweck:* Erzeugt je Bereich, Nische und Generation Kandidaten als unified diff, mit Begründung und berührten Verträgen. Er sieht nur die Landkarten-Sicht, die Quelldateien des Bereichs und die gescheiterten Wege (Kopf).
  - *Schnittstelle:* `erzeugen(con, lauf_id, werk_id, generation, werk, paket, …)`, Kassenzweck `schwarm.<nische>.<bereich>.gen<n>` (genesis.py:153).
  - *Prüfweise:* 6 Testdateien.
- **Nischen**
  - *Ort:* `organe/nischen.py` (161).
  - *Zweck:* vier Nischen `sicher`, `schnell`, `elegant`, `wild` mit Temperatur 0,2/0,3/0,4/0,9 und Auftragstext (nischen.py:31–57), dazu ein Pool aus vier Herstellern (nischen.py:24–29).
  - *Schnittstelle:*
    - `waehlen()` zieht je Nische und Generation zwei verschiedene Hersteller per Thompson-Stichprobe aus Beta(Erfolge+1, Misserfolge+1).
    - `buchen()`, `gewichte()`.
    - Eliten je (Nische, Bereich) (Kopf).
    - Tabellen `bandit`, `eliten`.
  - *Prüfweise:* 2 Testdateien.
- **Ankläger (Aegis)**
  - *Ort:* `organe/aegis.py` (1.174).
  - *Zweck:*
    - Prüft jeden Kandidaten: Wirkungskreis, Verfassung (mechanisch), Verträge und einen Angriff durch ein Modell (erst die Ansage, dann bis zu 4 Tests).
    - Misst paarweise in der Kammer mit demselben Testbestand; der Zuwachs ist die Differenz des Kernmaßes F2 (Kopf).
    - Führt das Immunsystem (Tabelle `immunsystem`).
  - *Schnittstelle:* `pruefen(con, lauf_id, werk_id, kandidat_id, werk, paket, …)`.
  - *Prüfweise:*
    - 22 Testdateien.
    - Pflichtkante `aegis.pruefen ← biotop.lauf:_generation_koerper @ generation`.
    - Drei weitere Pflichtkanten gehen von `aegis:pruefen` aus.
- **Aufnahmesperre C**
  - *Ort:* `organe/aegis.py:732` `aufnahmesperre()`.
  - *Zweck:*
    - Prüft den Schlüssel (die Behauptung) des tatsächlich geschriebenen Tests gegen den Vorrat des Bereichs. Das geschieht deterministisch, ohne Modellaufruf, unmittelbar vor der Aufnahme ins Immunsystem.
    - Nur Wiederholungen werden abgewiesen, jede Abweisung wird protokolliert.
    - Quelle: aegis.py:734–749, Fassung 7, Entscheidung Chat-Claude 20.09.2026.
  - *Prüfweise:*
    - Mechanikprüfung `pruefung/aufnahmesperre_pruefen.py` mit rotem und grünem Eichfall; Maßstab „Durchgerutscht an C = 0 · Fehlalarm ≤ 20 % der Sperrungen“ (R90 §1).
    - Test `tests/test_ansage_aufnahme.py`.
    - Im Verdrahtungslauf der Runde 6 eine gezählte Ausnahme: nie gerufen, weil der Angriff im Prüfwerk nicht trifft (`/root/biotop-vor-t4-06/bau/hermes/H-VOLL-AUSWERTUNG.txt` Z.41).
- **Artgedächtnis**
  - *Ort:* `organe/gedaechtnis.py` (595).
  - *Zweck:* Werkübergreifend: je angenommenem Kandidaten ein Eintrag (Werkklasse, Nische, Kategorie, Bereichsrolle, Ertrag) und ein abstrahiertes Muster, das ein Modell schreibt (`muster_bilden`, gedaechtnis.py:331).
  - *Schnittstelle:*
    - `art_merken`, `art_lesen`, `art_text`, `art_import`.
    - Der werkübergreifende Block (Bauteil B) steht bei gedaechtnis.py:475 (R56).
    - Tabelle `artgedaechtnis`.
  - *Prüfweise:* 9 Testdateien für das ganze Modul, darunter `test_artvorlage.py`.
- **Projektgedächtnis**
  - *Ort:* `organe/gedaechtnis.py`.
  - *Zweck:*
    - Je Werk (Identität = Paketname) jeder gescheiterte Weg mit Bereich, Änderungsziel, Ansatz und Grund.
    - Eine mechanische Wiederholungsprüfung verwirft ohne Kammerlauf (`immun.wiederholung`), wenn die Jaccard-Ähnlichkeit der Token hinzugefügter Zeilen ≥ SCHWELLE ist (Kopf).
  - *Schnittstelle:* `projekt_merken`, `gescheiterte_wege`, `wiederholung`, `projekt_import`, Tabelle `projektgedaechtnis`.
  - *Prüfweise:* wie oben, dazu `pruefung/projektgedaechtnis_differenz.py`.
- **Geschmacksgedächtnis** (drittes Gedächtnis)
  - *Ort:* `organe/gedaechtnis.py`.
  - *Zweck:* jede Freigabe und Ablehnung mit Begründung und Merkmalen der Vorlage. Ab 20 Entscheidungen gibt es eine Naive-Bayes-Vorhersage (Kopf).
  - *Schnittstelle:* `geschmack_merken` (gerufen aus `lauf.freigabe`), `geschmack_vorhersage`, Tabelle `geschmack`.
  - *Prüfweise:* wie oben, dazu `pruefung/tor3_geschmack.py`.
- **Bauteil A (Ansage-Sperre des Anklägers)**
  - *Ort:* `organe/aegis.py:655–658` (Ansage-Aufruf), `693–711` (Entscheidung).
  - *Zweck:* Der Ankläger nennt seine Behauptung vorab. Steht sie im Bereich schon, wird der Angriff nicht ausgeführt, und es gibt keinen Angriffsaufruf und keinen Kammerlauf (aegis.py:693–708).
  - *Prüfweise:* `pruefung/bauteilA_mechanik.py`, eine Mechanikprüfung mit gestellter Ansage (R90 §2).
- **Mentor**
  - *Ort:* `organe/mentor.py` (136).
  - *Zweck:*
    - Schwerer Aufruf: 3–5 Richtungen mit Ertrag, Risiko, Aufwand, Bereichen und Verweis ins Artgedächtnis `[A<id>]`.
    - Mechanisch geprüft werden JSON-Form, Anzahl, Pflichtfelder und ob die Kennungen existieren (Kopf).
  - *Schnittstelle:* `richtungen()`, `waehlen()`, Befehle `mentor` und `richtung`, Tabelle `mentor`, Feld `laeufe.richtung`.
  - *Prüfweise:* 1 Testdatei (`test_t3_verbundausfall.py`).
- **Oberfläche**
  - *Ort:* `biotop/oberflaeche.py` (172), ausgeliefert über `biotop/dienst.py`.
  - *Zweck:* eine HTML-Seite hinter der Anmeldung, ohne Framework.
  - *Schnittstelle:*
    - `ELEMENTE` ordnet jedem von 18 Bedienelementen Methode, Route und Datei:Funktion zu (R80 §3).
    - Die 18 Elemente: anmelden, abmelden, lauf-wahl, werk-landkarte, verfassung, mass, kurve, generation-aktuell, vorlage, freigabe-frei, freigabe-ablehnen, entropie, kasse, archiv, mentor-richtungen, richtung-waehlen, immunsystem, protokoll (R90 §8).
    - `belege()` und Befehl `oberflaeche-belege`.
  - *Prüfweise:* 0 Testdateien; Prüfskripte `pruefung/tor3_oberflaeche.py` und `pruefung/tor1.py`; Tor 3, Zeile „Oberfläche“.
- **Messgerät**
  - *Ort:* `kern/messgeraet.py` (878), dazu die Sonden `kern/py/verhalten.py` und `kern/ts/*.mjs` sowie `kern/referenzlast/`.
  - *Zweck:*
    - Harte Maße je Bereich: Tests, Sicherheitspunkte (bandit), tote Funktionen (vulture), Laufzeit auf der Referenzlast, größte Funktion.
    - Harte Maße auf Werkebene: Zyklen, Bauzeit.
    - Daraus Kernmaß F2, Pareto je Test, Grenzmaße gegen den Bestwert, gepaarte Laufzeit, Gewinnband der Nische schnell (messgeraet.py:735–743).
    - Läuft nur in der Kammer (Kopf).
    - Speicher wird nicht gemessen (messgeraet.py:21: „Speicher: nicht gemessen (Liste für danach)“, R65).
  - *Prüfweise:* 14 Testdateien; Pflichtkante `messgeraet.laufzeit_gepaart ← aegis:pruefen @ generation`.
- **Freigabe-Gate**
  - *Ort:* `biotop/lauf.py:553–591` `freigabe()`, `lauf.py:200`, `lauf.py:516` `abbrechen()`.
  - *Zweck:*
    - Eine vorgelegte Generation wird erst mit `freigabe <lauf> <nr> frei` oder `ablehnen` entschieden. Bis dahin verweigert `generation()` die nächste Generation („Generation n wartet auf Freigabe durch Philipp“, lauf.py:200).
    - „frei“ ist nur zulässig, wenn der Text des Arguments `--von` mit „philipp“ beginnt oder die Werkverfassung `regeln.uebungswerk=true` trägt (lauf.py:560–563).
    - Das ist eine Textprüfung; an der Befehlszeile gibt es keine Anmeldung.
    - Ablehnung: Rückkehr über Lazarus, der Grund geht ins Geschmacksgedächtnis (lauf.py:580–591).
    - `abbrechen` ist nie gesperrt (MP v8 Z.305; `__main__.py:12`).
  - *Prüfweise:*
    - Testdateien zu `lauf` (10) und `pruefung/abbruch_pruefen.py`.
    - Dienst-Routen `POST /laeufe/<id>/freigabe` und `/abbrechen` mit Token.
    - Welchen Wert `von` über den Dienst erhält: NICHT GELESEN.

### Kernmodule
- **Datenbank**
  - *Ort:* `kern/datenbank.py` (101).
  - *Zweck:* SQLite, `verbinden()` und `transaktion()`. Der Pfad kommt aus `BIOTOP_DB`, Vorgabe `/root/biotop/daten/biotop.db` (datenbank.py:16).
  - *Prüfweise:* 31 Testdateien.
- **Protokoll**
  - *Ort:* `kern/protokoll.py` (57).
  - *Zweck:* fortlaufend nummeriert, jede Zeile trägt den Hash der Vorzeile.
  - *Schnittstelle:* `schreiben`, `pruefen`, `lesen`, Befehle `protokoll` und `protokoll-pruefen`.
  - *Prüfweise:* 14 Testdateien.
- **Kasse**
  - *Ort:* `kern/kasse.py` (313).
  - *Zweck:* Preistabelle (kasse.py:23–43) und fester Kurs `USD_JE_EUR` (kasse.py:20). `vorpruefung()` läuft vor jedem Aufruf, `buchen()` danach.
  - *Schnittstelle:*
    - `auftragsgrenze_verlangen()` (kasse.py:70, gerufen in `vorpruefung`, kasse.py:123).
    - `ausfall_klaeren` (kasse.py:175), `generation_vorpruefung`, `bericht_md`.
    - Befehl `kasse`.
  - *Prüfweise:* 6 Testdateien; Tor 1, Zeile „Kasse“.
- **Anmeldung**
  - *Ort:* `kern/anmeldung.py` (50).
  - *Zweck:* Benutzer mit Salz und Hash, dazu Token.
  - *Schnittstelle:* `benutzer_anlegen`, `anmelden`, `pruefen`, Befehl `benutzer`.
  - *Prüfweise:* 0 Testdateien; `pruefung/tor1.py:98–122` startet den Dienst auf 8642 und prüft 401 je Route.
- **Befundklassen**
  - *Ort:* `kern/befundklassen.py` (158).
  - *Zweck:* die bekannten Umgehungen je statischer Befundklasse als Immuntests, in Python und TypeScript („behoben heißt verschwunden“).
  - *Prüfweise:* 0 Testdateien direkt.
- **Diffwerk**
  - *Ort:* `kern/diffwerk.py` (128).
  - *Zweck:* wendet Modell-Diffs tolerant an. Ein Hunk über 60 % der Datei gilt als Neuschreibung und wird abgelehnt, außer die Datei hat unter 100 Zeilen (Kopf).
  - *Prüfweise:* 0 Testdateien direkt.
- **Gegenzeugen**
  - *Ort:* `kern/gegenzeugen.py` (79).
  - *Zweck:*
    - Doppelprüfung je Schwäche: (a) die Schwäche ist weg, (b) das gültige Verhalten ist gegen die Normalversion unverändert.
    - „Behoben“ nur, wenn beides gemessen ist und hält; fehlt eine Prüfung, ist das Ergebnis nicht beurteilbar.
  - *Prüfweise:* 2 Testdateien; Pflichtkante `gegenzeugen.torzeile_schwaechen ← tor4:ausfuehren @ tor4`.
- **Register**
  - *Ort:* `kern/register.py` (56).
  - *Zweck:* `VERLANGT` mit (Funktion, Aufrufer, Phase, Grund); `kante`, `fehlend`.
  - *Prüfweise:* `tests/test_verdrahtung.py`.
- **Sprachprofil**
  - *Ort:* `kern/sprachprofil.py` (38).
  - *Zweck:* erkennt TypeScript am Paket und an echten Quellen; liefert Endungen und Testdateien.
  - *Prüfweise:* 2 Testdateien.
- **TypeScript-Adapter**
  - *Ort:* `kern/typescript.py` (185) mit `kern/ts/` (20 `.mjs`).
  - *Zweck:* Struktur, Mutanten, Messung, Bau- und Testlauf für TS-Werke, nur in der Kammer mit `BIOTOP_KAMMER_IMAGE=biotop-kammer:ts1`.
  - *Prüfweise:* 16 Testdateien.
- **Verhaltenssonde Python**
  - *Ort:* `kern/py/verhalten.py` (1.769).
  - *Zweck:*
    - Läuft als Skript in der netzlosen Kammer.
    - Wickelt öffentliche Funktionen, Methoden und Eigenschaften der geänderten Module ein.
    - Beobachtet die Referenzlast mit Alias-, Mutations- und Rücksetzmustern (Kopf).
  - *Prüfweise:* wird nicht importiert (0); geprüft über die Tests des Verhaltensvergleichs.
- **Referenzlast**
  - *Ort:* `kern/referenzlast/` [4, 454].
  - *Zweck:* `last_<bereich>()` für die Laufzeit, `beobachten()` als Verhaltensraster. Stufe 2 arbeitet mit zehnfacher Eingabegröße (Kopf der `.stufe2.mjs`).

### Anbieter, Ablauf, Befehle
- **Anbieterschicht**
  - *Ort:* `anbieter/__init__.py` (246).
  - *Zweck:*
    - Einziger Weg zu einem Modell: `aufrufen()` fragt die Kasse vor dem Aufruf und bucht danach (Kopf).
    - Einziger Adapter: `OpenRouterAdapter`.
    - Schlüsselname `OPENROUTER_API_KEY` aus der Umgebung, sonst aus der Datei `/root/.hermes/.env` (anbieter/__init__.py:75–84, 101). Wert: [GESCHWÄRZT: /root/.hermes/.env].
  - *Prüfweise:* 5 Testdateien.
- **Lauf**
  - *Ort:* `biotop/lauf.py` (854).
  - *Zweck:*
    - Ablauf Aufnahme → Landkarte → Maß (eingefroren) → Generationen, je Generation: Schwarm → Ankläger → Zusammensetzen → Generalprobe → Pareto → Schnappschuss → Freigabe (Kopf).
    - Der Nexus steckt hier: Verhandlung `_verhandeln` (lauf.py:637), `annahme_tausch`, `bestwert_des_laufs`, `kurve_nachrechnen`.
  - *Prüfweise:* 10 Testdateien.
- **Befehlszeile**
  - *Ort:* `biotop/__main__.py` (166).
  - *Zweck:* Unterbefehle: FK34.
  - *Prüfweise:* `test_verdrahtung.py`, `test_vorspann_cli.py`.
- **Nachspiel**
  - *Ort:* `biotop/nachspiel.py` (298).
  - *Zweck:* spielt aufgezeichnete Kandidaten durch genau die Annahmefunktion `aegis.pruefen`, mit dem Aufbau aus `lauf.generation()` (Kopf).
  - *Prüfweise:* 1 Testdatei.
- **Tor-4-Skript**
  - *Ort:* `biotop/tor4.py` (145).
  - *Zweck:*
    - Torzeile „Schwächen“ für T4, je Altlast doppelt geprüft: Gegenzeuge am Endstand, Normalvergleich über den Verhaltensvergleich.
    - Die übrigen Torzeilen heißen „nicht berechnet“ (Kopf).
  - *Schnittstelle:* Befehl `tor4`.
  - *Prüfweise:* 0 Testdateien direkt; Pflichtkante `tor4.ausfuehren ← biotop.__main__:main @ tor4`.
- **Dienst**
  - *Ort:* `biotop/dienst.py` (245).
  - *Zweck:*
    - HTTP-Server auf `127.0.0.1:8642` als Vorgabe (dienst.py:233, 241) mit der Routenliste `ROUTEN` (R90 §7; Zahl → Teil 3, W1).
    - Anmeldezwang vor jeder Routenauflösung, ausgenommen `POST /anmelden` und `GET /` (liefert nur die Seite; dienst.py:144–151, R104 §4).
  - *Widerspruch im Modul:* Kopf und Routenliste passen nicht zusammen → Teil 3, W1.
  - *Prüfweise:* 0 Testdateien; `pruefung/tor1.py`, `pruefung/tor3_oberflaeche.py`.

### Organe (`biotop/organe/`)
- **Aufnahme**
  - *Ort:* `aufnahme.py` (196).
  - *Zweck:*
    - Kopiert das Werk nach `/root/biotop/daten/werke/<name>`; der Pfad ist fest (aufnahme.py:21).
    - Erster Testlauf in der Kammer, ethische Prüfung per Modell (aufnahme.py:107–113).
    - Ohne Tests oder Bau: „Messgerät fehlt“.
  - *Prüfweise:* 3 Testdateien; Tor 1, Zeile „Laut scheitern“.
- **Landkarte**
  - *Ort:* `landkarte.py` (273).
  - *Zweck:*
    - Stufen 0–3, Straßen, abgeleitete Verträge, Wirkungskreis.
    - Struktur aus Python-`ast` bzw. dem TS-Syntaxbaum; Zusammenfassungen je Stufe per Modell, mit Prüfsumme.
    - tree-sitter steht „auf der Liste für danach“ (landkarte.py:3–4).
  - *Prüfweise:* 4 Testdateien; Tor 1, Zeile „Landkarte“.
- **Verfassung des Werks**
  - *Ort:* `verfassung.py` (69).
  - *Zweck:* Die Verfassung wird eingelegt; das Biotop entwirft sie nicht (Kopf). `mechanisch_pruefen` prüft die mechanisch prüfbaren Sätze.
  - *Schnittstelle:* Befehl `verfassung`.
  - *Prüfweise:* 7 Testdateien.
- **Verträge**
  - *Ort:* `vertraege.py` (85).
  - *Zweck:*
    - Explizite Verträge als Tests `tests/vertraege/test_vertrag_<A>_<B>.py`, die paarweise mitlaufen.
    - Eine Verletzung tötet den Kandidaten, außer er hat den Vertrag benannt; dann folgt die Verhandlung (Kopf).
  - *Schnittstelle:* Befehl `vertraege`.
  - *Prüfweise:* 7 Testdateien.
- **Kammer**
  - *Ort:* `kammer.py` (124).
  - *Zweck:*
    - Jeder Bau, jeder Testlauf und jede Messung läuft in Docker mit `--network none`.
    - Je Kandidat eine eigene Werkkopie; Zeit- und Speicherlimit, unprivilegierter Benutzer, read-only-Wurzel, PID-Limit.
    - Wer das Limit reißt, ist gescheitert (rc 124) (Kopf).
  - *Prüfweise:* 22 Testdateien; Tor 1, Zeile „Kammer“.
- **Lazarus**
  - *Ort:* `lazarus.py` (110).
  - *Zweck:*
    - Je angenommener Generation ein Git-Tag im Werk-Repository und ein tar.gz-Archiv mit Prüfsumme unter `/root/biotop/daten/lazarus`; der Pfad ist fest (lazarus.py:24).
    - Eine Rückkehr markiert spätere Generationen als verworfen und löscht nichts.
  - *Schnittstelle:* Befehl `lazarus`.
  - *Prüfweise:* 1 Testdatei; Tor 1, Zeile „Lazarus“.
- **Generation 0**
  - *Ort:* `generation0.py` (469).
  - *Zweck:*
    - Mutanten aus dem Syntaxbaum; Fang mit dem aktuellen Testbestand.
    - Testbau für blinde Mutanten in Nische sicher, zwei Durchläufe.
    - Äquivalenz- und Rundenprüfung.
  - *Schnittstelle:* Befehl `gen0`.
  - *Prüfweise:* 10 Testdateien.
- **Vorspann (Generation minus eins)**
  - *Ort:* `vorspann.py` (318).
  - *Zweck:*
    - `ausfuehren` eicht vor gen0 und Maß und versiegelt den Nachweis (Tabelle `vorspann_nachweise`).
    - `verlangen` verweigert jeden Eingang ohne Nachweis und protokolliert das (vorspann.py:124–135, 243–249).
  - *Prüfweise:* 9 Testdateien; vier Pflichtkanten aus `vorspann:_ausfuehren`.
- **Eichung (Rauschmessung)**
  - *Ort:* `eichung.py` (267).
  - *Zweck:*
    - Fünf Werte je Bereich; ein Aussetzer über dem Fünffachen des Medians wird einmal nachgemessen.
    - Toleranz = getrimmte Spannweite + 10 Prozentpunkte, zwischen 1,15 und 2,0. Über 1,5 wird der Bereich gesperrt.
    - Eichkosten werden getrennt geführt (Kopf).
  - *Prüfweise:* 6 Testdateien.
- **Eichproben**
  - *Ort:* `eichproben.py` (634) und `eichproben_ts.py` (122).
  - *Zweck:* vier Proben (Nebenwirkung, Regression, Norm, Vertrag) am versiegelten Eichgegenstand; Probenkandidaten tragen `ist_probe=1` (Kopf).
  - *Prüfweise:* 7 bzw. 0 Testdateien.
- **Eichgegenstand**
  - *Ort:* `eichgegenstand.py` (199).
  - *Zweck:* ein je Werk einmal gewähltes, versiegeltes Bereichspaar mit Vertrag. Fällt es weg, ist das ein protokollierter Befund.
  - *Prüfweise:* 2 Testdateien.
- **Maßeichung**
  - *Ort:* `masseichung.py` (186).
  - *Zweck:* prüft jede Prüferregel am sauberen Vergleichsbereich. Schlägt sie dort an, wird sie stillgelegt und zählt nicht zum Kernmaß (Kopf).
  - *Prüfweise:* 2 Testdateien; Pflichtkanten `masseichung.eichen` (Vorspann) und `masseichung.anwenden` (Aegis).
- **Fundprüfung**
  - *Ort:* `fundpruefung.py` (193).
  - *Zweck:* bewertet übernommene offene Funde am neuen Ausgang mit der Logik des Anklägers neu (Norm statt Fund).
  - *Prüfweise:* 4 Testdateien.
- **Verhaltensvergleich**
  - *Ort:* `verhaltensvergleich.py` (754).
  - *Zweck:* vergleicht Vorgeneration und Kandidat über die Sonde. Jede Abweichung braucht einen deckenden Test, sonst wird der Kandidat abgelehnt.
  - *Schnittstelle:* `pruefen`, `deckung`, `SondeAusgefallen`.
  - *Prüfweise:* 6 Testdateien; Pflichtkante `verhaltensvergleich.pruefen ← aegis:pruefen`.
- **Neutralzähler**
  - *Ort:* `neutralzaehler.py` (99).
  - *Zweck:* zählt neutrale gegen geurteilte Ausgänge je Organ. `traegt_torzeile()` verlangt, dass mehr als die Hälfte geurteilt ist.
  - *Schnittstelle:* Tabelle `neutralzaehler` (nur im T3-Zweig, R40 §7).
  - *Prüfweise:* 3 Testdateien.
- **Entropie**
  - *Ort:* `entropie.py` (103).
  - *Zweck:* je Generation Verbesserung in Prozent und Doppelgänger-Anteil. Bringen fünf Generationen zusammen weniger als 0,5 %, tritt Sättigung ein und der Laufstatus wird `gesaettigt` (Kopf).
  - *Schnittstelle:* gerufen aus `lauf.freigabe` (R90 §6).
  - *Prüfweise:* 0 Testdateien direkt; Tor 3, Zeile „Entropie“.
- **Jury**
  - *Ort:* `jury.py` (62).
  - *Zweck:* entscheidet nur bei Gleichstand aller harten Maße; drei Modelle verschiedener Hersteller, nur einstimmig (Kopf).
  - *Prüfweise:* 1 Testdatei; `pruefung/jury_mechanik.py`, `pruefung/jury_probe.py`.

### Außerhalb von `biotop/`
- **Kammer-Abbilder:** `kammer/Dockerfile`, `kammer/typescript/` (FK36).
- **Prüfskripte:** `pruefung/`, `pruefung_vorbedingung1/`. Sie importieren Biotop-Code, zum Beispiel `sys.path.insert(0, "/root/biotop")` in `pruefung/aufnahmesperre_pruefen.py` (R90 §1). Sie laufen nicht im Lauf.
- **Werkverfassungen und -verträge:** `verfassungen/`.
- **Tests:** `tests/` (FK35).
