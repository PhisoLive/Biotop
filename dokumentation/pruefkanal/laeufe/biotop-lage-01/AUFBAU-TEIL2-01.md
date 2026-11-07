# BIOTOP-LAGE-01 · Fassung 2 · `AUFBAU-TEIL2-01.md`

- **Inhalt:** FK31–FK38 · Entwurf D, Stück 2 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil D, Arbeitszeit 25.09.2026 16:10:47–17:49:11 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/aufbau/AUFBAU-TEIL2.md` · 20841 B · SHA-256 `bd48262e23e182e0e1182d6a79a8ebd61b09603f59f7e9a2dfaccfdc5a31fcc2`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (0 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# AUFBAU — Teil 2 von 3 (FK33, FK34, FK35)

Bezugsstand, Lesezeitpunkt und Abkürzungen: siehe `AUFBAU-TEIL1.md` (Kopf). Jede Code-Zahl gilt für Stand `0c2f058`. Die Datenbanken wurden am 25.09.2026 zwischen 16:13 und 16:50 CEST gelesen:
- STAMM mit `mode=ro&immutable=1`; `-wal` hatte 0 Bytes (R40 §7).
- alle anderen mit `mode=ro`.

Kosten in Euro stehen nicht hier, sondern in KASSE und CHRONIK (FK20).

---

## FK33 — Modelle über OpenRouter: Kennung und Rolle

**Weg zu jedem Modell:**
- Einziger Weg ist `anbieter.aufrufen()` über `OpenRouterAdapter`, den einzigen Adapter. Die Kasse prüft vor dem Aufruf und bucht danach (Kopf von `anbieter/__init__.py`, R38).
- Denken:
  - Bei `google/gemini-3*` setzt der Adapter `reasoning.effort = "minimal"`.
  - Bei allen anderen Modellen gilt `reasoning.enabled = False` (anbieter/__init__.py:136–144, R43).

### Konfiguriert zum Stand 0c2f058 (abgelesen, R40 §3, R43 §1)
| Rolle | Modellkennung(en) | Stelle im Code | Zweck in der Kasse |
|---|---|---|---|
| Schwarm, alle vier Nischen: Pool von vier Herstellern; je Nische und Generation 2 verschiedene per Thompson-Stichprobe | `openai/gpt-5.6-luna`, `google/gemini-3.5-flash-lite`, `deepseek/deepseek-v4.1-flash`, `qwen/qwen3.8-flash` | nischen.py:24–29, 106–118; genesis.py:153 | `schwarm.<nische>.<bereich>.gen<n>` |
| Generation 0, Testbau für blinde Mutanten (Nische „sicher“, 2 Hersteller, 2 Durchläufe) | derselbe Pool | generation0.py:381–383, 426–429 | `generation0.testbau.<bereich>` |
| Ankläger: Ansage und Angriff | `google/gemini-3.5-flash-lite` | aegis.py:33, 655–658, 718–720 | `aegis.ansage.<bereich>`, `aegis.angriff.<bereich>` |
| Ankläger, wenn der Bereich einen statischen Sicherheitsbefund trägt: Ansage **und** Angriff | `anthropic/claude-sonnet-5` | aegis.py:34, 688–696 | Ansage: `aegis.ansage.<bereich>` (**ohne** `schwer.`); Angriff: `schwer.aegis.angriff.<bereich>` |
| Mentor | `anthropic/claude-sonnet-5` | mentor.py:24, 69 | `schwer.mentor` |
| Landkarte, Zusammenfassungen je Stufe | `google/gemini-3.1-flash-lite` | landkarte.py:25, 205–207 | Präfix `landkarte` |
| Aufnahme, ethische Prüfung | `openai/gpt-5.6-luna` | aufnahme.py:28, 107–113 | `aufnahme.ethik` |
| Artgedächtnis, Muster je angenommener Generation | `openai/gpt-5.6-luna` | gedaechtnis.py:331, 351–353 | `gedaechtnis.muster.<kategorie>` |
| Jury (drei Juroren) | `openai/gpt-5.6-luna`, `google/gemini-3.5-flash-lite`, `deepseek/deepseek-v4.1-flash` | jury.py:19, 47 | `jury.<bereich>.gen<n>` |

**Rolle je Nische:**
- Keine Nische hat ein festes Modell. Jede zieht aus demselben Pool; die Bandit-Gewichte entscheiden.
- Die Nischen unterscheiden sich in Auftrag, Temperatur und Ziel (nischen.py:31–57, Wortlaut gekürzt):

| Nische | Temperatur | Ziel | Auftrag (Wortlaut, gekürzt) |
|---|---|---|---|
| sicher | 0,2 | kernmass | „Beseitige Fehler, Vertragsverletzungen und Sicherheitsbefunde; härte Verträge; wage nichts Neues; verändere keine öffentliche Signatur.“ |
| schnell | 0,3 | laufzeit | „Senke die Laufzeit auf der Referenzlast … angenommen, wenn die Laufzeit des Bereichs um mindestens 15 % sinkt und das Kernmaß gleich bleibt oder steigt.“ |
| elegant | 0,4 | kernmass | „weniger Code bei gleicher Funktion … reine Umformung ohne Maßgewinn wird abgelehnt — dann antworte lieber KEIN VORSCHLAG.“ |
| wild | 0,9 | kernmass | „Schlage vor, was niemand erwartet … Du darfst Verträge in Frage stellen …“ |

**Preistabelle** `PREISE_USD_JE_MIO` (kasse.py:23–43):
- Quelle laut Kommentar: `openrouter.ai/api/v1/models` vom 18.09.2026, ergänzt durch die Katalogprüfung vom 19.09.2026.
- Kurs: `USD_JE_EUR = 1.08` (kasse.py:20, „Entscheidung Hermes, 18.09.2026“).
- 16 Einträge (abgelesen, R43 §1). Einteilung gerechnet: Preistabelle gegen die Rollen oben und gegen die Modelle aller vier Kassenzweige (R43 §2).
  - **Mit Rolle am Commit (6)**, USD je Mio. Token Eingabe/Ausgabe:
    - `openai/gpt-5.6-luna` 0,20/1,20
    - `google/gemini-3.5-flash-lite` 0,30/2,50
    - `google/gemini-3.1-flash-lite` 0,25/1,50
    - `deepseek/deepseek-v4.1-flash` 0,15/0,60
    - `qwen/qwen3.8-flash` 0,15/0,47
    - `anthropic/claude-sonnet-5` 2,00/10,00
  - **Früher gebucht, am Commit ohne Rolle (4):** `openai/gpt-4.1-mini`, `google/gemini-2.5-flash`, `google/gemini-2.5-flash-lite`, `anthropic/claude-sonnet-4.5`.
  - **In keinem Zweig je gebucht (6):** `deepseek/deepseek-chat-v3.1`, `qwen/qwen3-coder`, `mistralai/mistral-small-3.2-24b-instruct`, `openai/gpt-4o-mini`, `openai/gpt-5-mini`, `anthropic/claude-haiku-4.5`.

### In der Kasse benutzt (abgelesen, R43 §2–3, R75 §1)
Tabelle: Buchungen je Modell und Zweck-Präfix (erstes Glied von `zweck`). Zweige:
- STAMM (Läufe 1–25);
- VB1 = STAMM + Lauf 26 (Vorbedingung 1), mit denselben 10 Modellen;
- R02 = STAMM;
- T3 = STAMM + Läufe 26–38 (die Spalte unten zählt nur `lauf_id ≥ 26`).

| Modell | STAMM (Läufe 1–25) | T3, nur Läufe 26–38 |
|---|---|---|
| `anthropic/claude-sonnet-4.5` | schwer 27 | — |
| `anthropic/claude-sonnet-5` | schwer 30 (mentor 15, aegis 15), phase2 1 | aegis 168 (alle `aegis.ansage`), schwer 95 (alle `schwer.aegis`) |
| `deepseek/deepseek-v4.1-flash` | schwarm 527, generation0 10, jury 6, phase2 1 | schwarm 454, generation0 333, jury 4 |
| `google/gemini-2.5-flash` | aegis 251, schwarm 181 | — |
| `google/gemini-2.5-flash-lite` | landkarte 128 | — |
| `google/gemini-3.1-flash-lite` | landkarte 208, phase2 2 | landkarte 30 |
| `google/gemini-3.5-flash-lite` | aegis 665, schwarm 577, generation0 20, jury 7, phase2 2 | schwarm 214, aegis 110, generation0 76, jury 4 |
| `openai/gpt-4.1-mini` | schwarm 181, aufnahme 10 | — |
| `openai/gpt-5.6-luna` | schwarm 643, gedaechtnis 24, generation0 13, aufnahme 13, jury 7, phase2 1 | schwarm 454, generation0 142, gedaechtnis 30, aufnahme 13, jury 4 |
| `qwen/qwen3.8-flash` | schwarm 524, generation0 10, phase2 1 | schwarm 298, ausfall 115, generation0 59 |

**Zweck-Präfixe ohne Organ im Code:**
- `phase2` ist der Rauchtest der Modellwahl vor Phase 2, Läufe 11 (6 Buchungen) und 12 (2 Buchungen), zusammen 8 (R75 §1).
- `ausfall` hat den Zweck `ausfall.hoechstfall`, gebucht von `kasse.ausfall_klaeren` (kasse.py:175–213).

**Die Nischen in der Kasse** (Buchungen `schwarm.<nische>.…` je Modell; abgelesen, R98 §1). Reihenfolge je Zeile: luna / gemini-3.5 / deepseek / qwen.

| Nische | STAMM (Läufe 1–25) | T3, Läufe 26–38 |
|---|---|---|
| sicher | 159 / 194 / 152 / 137, dazu `gemini-2.5-flash` 181 und `gpt-4.1-mini` 181 (Phase 1: eine Nische, zwei Anbieter) | 97 / 55 / 205 / 88 |
| schnell | 170 / 127 / 113 / 135 | 127 / 44 / 78 / 80 |
| elegant | 164 / 132 / 133 / 115 | 115 / 62 / 69 / 76 |
| wild | 150 / 124 / 129 / 137 | 115 / 53 / 102 / 54 |
| Summe | 2.633 | 1.420 |

**Kandidaten mit Status `angenommen` je Nische und Modell** (Proben mit `ist_probe=1` nicht mitgezählt; abgelesen, R98 §2):
- STAMM:
  - sicher 42 (gemini-2.5-flash 25, gpt-4.1-mini 13, deepseek 2, gemini-3.5 1, qwen 1, luna 0)
  - schnell 24 (qwen 8, luna 6, gemini-3.5 6, deepseek 4)
  - elegant 1 (luna)
  - wild 3 (qwen 2, deepseek 1)
- T3, Läufe 26–38:
  - sicher 6 (deepseek 3, qwen 3)
  - schnell 12 (qwen 8, deepseek 4)
  - elegant 6 (qwen 5, gemini-3.5 1)
  - wild 6 (deepseek 4, qwen 2)
  - `gpt-5.6-luna` hier 0 angenommene von 183 Kandidaten (gerechnet 110 + 3 + 56 + 14, R98 §2).
- Die Summen je Nische sind gerechnet.

**Befunde zu den Rollen (gelesen):**
1. **Bandit der Nische „sicher“:**
   - Die Bandit-Tabelle der Nische „sicher“ bucht auch den Testbau der Generation 0. Dort gilt als Erfolg „besteht am Original und fängt den Mutanten“ (generation0.py:398, 454; R112 §2).
   - Die Schwarm-Kandidaten bucht lauf.py:317 (Erfolg = „ueberlebt“).
   - Im T3-Zweig steht für sicher/deepseek: 373 Versuche, 202 Erfolge (R98 §3), bei 41 Schwarm-Kandidaten.
   - Widerspruch zum Kopf von nischen.py (Erfolg = „Kandidat überlebt den Ankläger“) → Teil 3, W2.
2. **Schwere Aufrufe ohne `schwer.`-Präfix:**
   - Die Ansage läuft bei Sicherheitsbefund mit dem schweren Modell, wird aber unter `aegis.ansage.*` gebucht, also ohne `schwer.`.
   - Anzahl in den T3-Läufen 26–38: Tabelle oben, Spalte T3, `aegis` (R75 §1).
   - Wer schwere Aufrufe am Präfix `schwer.` zählt (kasse.py:33–34: „Eigene Zählung: zweck-Präfix "schwer."“), übersieht sie → Teil 3, W3.
3. **Mentor in T3:** In den Läufen 26–38 gibt es keine Buchung `schwer.mentor` (R75 §1: `anthropic/claude-sonnet-5` nur mit `aegis.ansage` und `schwer.aegis`).
4. **Abweichungen von MP v8 Abschnitt 6** (Z.311–314; Wertung → SOLL-IST):
   - Schwere Aufrufe laufen tokenabgerechnet über OpenRouter („weil der Anthropic-Träger des Teams unangetastet bleibt (Vorgabe Philipp 18.09.2026)“, kasse.py:33–34), nicht über ein Abo-Kontingent.
   - Die Spalte `kontingent` im T3-Zweig: 0 in 6.558 Buchungen, leer in 115 (R75 §1). Die Summe ist die Gesamtzahl der Buchungen des Zweigs.
   - Die Jury besteht aus drei Schnellmodellen (jury.py:19). Das Soll nennt ein „Jury-Endurteil“ als schweren Aufruf.
   - „Verfassungsentwurf“ und „Anklägerbericht an Philipp“ haben keinen Modellaufruf im Code: NICHT GEFUNDEN. Laut Kopf von verfassung.py wird die Verfassung eingelegt, nicht entworfen.

---

## FK34 — Einen Lauf starten und auswerten

### Aufruf
- **Form:** In allen Laufskripten `python3 -m biotop <befehl> …` mit `PYTHONPATH=/root/biotop`, zum Beispiel `pruefung/generationen.sh:3`, `pruefung/lauf7.sh:4–13` (R40 §2).
  - Der Kopf von `__main__.py` schreibt `biotop <befehl>`.
  - Ob ein Programm `biotop` installiert ist: NICHT GEPRÜFT.
- **Ausgabe:** JSON auf stdout. Bei `LaufFehler`, `VorspannFehler` oder `BudgetErschoepft` erscheint „ABBRUCH: …“ auf stderr, Exit-Code 1 (`__main__.py:160–162`).
- **Sperren vor dem Lauf:**
  - `vorspann.verlangen` verweigert jeden Eingang ohne versiegelten Vorspann-Nachweis und protokolliert die Verweigerung (vorspann.py:243–249).
  - Welche Befehle `verlangen` rufen: NICHT EINZELN GELESEN. Laut `__main__.py:6` steht der Vorspann vor gen0 und mass.
  - Die Kasse verweigert jeden Modellaufruf, solange die Auftragsgrenze nicht gesetzt ist (kasse.py:70ff., gerufen in `vorpruefung`, kasse.py:123).

### Unterbefehle
24 Unterbefehle, abgelesen aus `__main__.py:40–66` (R40 §1). Reihenfolge nach dem Kopf von `tests/test_verdrahtung.py`, README.md und `__main__.py:6`.

| Schritt | Befehl | Eingaben |
|---|---|---|
| 1 | `lauf anlegen --budget <€>` | Laufbudget |
| 2 | `einlegen <lauf> <name> <quelle>` | Werkordner; Kopie nach `daten/werke/<name>` |
| 3 | `verfassung <lauf> <text.md> <regeln.json> --von <wer>` | z. B. `verfassungen/lagerhaus.md` und `lagerhaus.regeln.json` |
| 4 | `vertraege <lauf> <verzeichnis> --von <wer>` | Dateien `test_vertrag_<A>_<B>.<py|ts>` |
| 5 | `kartieren <lauf>` | keine (Landkarte, Modellaufrufe) |
| 6 | `vorspann <lauf>` | keine; Generation minus eins „vor gen0 und mass“ (`__main__.py:6`) |
| 7 | `gen0 <lauf> [--mutanten <json>] [--ziel 0.8]` | z. B. `/root/versiegelt/MUTANTEN-phase2.json` (`pruefung/lauf_p2.sh:11`) |
| 8 | `mass <lauf> --bestaetigt-von "<Text>"` | Bestätigung als Freitext |
| 9 | `mentor <lauf>`; `richtung <lauf> <name> --von <wer>` | nur mit Mentor |
| 10 | `generation <lauf> [--einschleusen <json>]` | Proben-Kandidaten `[{bereich, diff, begruendung, vertraege, probe}]` |
| 11 | `freigabe <lauf> <nr> frei|ablehnen --grund … --von …` | nach jeder vorgelegten Generation (Freigabe-Gate) |
| 12 | `kurve <lauf> [--testbestand-von-lauf n]`; `entropie <lauf>` | Auswertung |
| 13 | `tor4 <lauf> --altlasten <liste.json>` | nur T4 |

**Jederzeit verfügbar:**
- `abbrechen <lauf> --grund … --von … [--art satz2|budget|philipp|sonst]`
- `kasse [<lauf>]`
- `protokoll [--ab N] [--art X] [--limit 200]`, `protokoll-pruefen`
- `lazarus liste|rueckkehr <lauf> [nr] [--ziel PFAD]`
- `gedaechtnis import|art|projekt|geschmack [lauf] [--bereich]`
- `benutzer <name>`
- `dienst [--port 8642] [--host 127.0.0.1]`
- `oberflaeche-belege`

**Zählung** (gerechnet): 15 Befehle im Ablauf (lauf, einlegen, verfassung, vertraege, kartieren, vorspann, gen0, mass, mentor, richtung, generation, freigabe, kurve, entropie, tor4) + 9 jederzeit verfügbare = 24.

**Nicht am Commit:** Der volle Verdrahtungslauf der Runde 6 kennt einen Schritt `stufe2` zwischen kartieren und vorspann (`/root/biotop-vor-t4-06/bau/hermes/H-VOLL-AUSWERTUNG.txt` Z.47). Er gehört zum Arbeitsstand der Runde 6; am Commit gibt es keinen Unterbefehl dafür (R40 §1).

### Eingaben aus der Umgebung (abgelesen, R40 §2, R65 §1, R112 §3)
| Variable | Wirkung | Vorgabe | Stelle |
|---|---|---|---|
| `BIOTOP_DB` | Pfad der Datenbank | `/root/biotop/daten/biotop.db` | datenbank.py:16 |
| `BIOTOP_AUFTRAG_LAUF_AB` | erster Lauf, der zum Auftragsbudget zählt | 0: Start verweigert (`AuftragsgrenzeFehlt`) | kasse.py:47, 70ff. |
| `BIOTOP_AUFTRAG_BUDGET_EUR` | hartes Budget über alle Läufe ab `LAUF_AB` | 0: Start verweigert | kasse.py:48 |
| `BIOTOP_KAMMER_IMAGE` | Kammer-Abbild | `biotop-kammer:1`; für TypeScript `biotop-kammer:ts1` | kammer.py:25; Kopf typescript.py |
| `BIOTOP_KAMMER_ZEITLIMIT` | Zeitlimit je Kammerlauf (s) | 120 | kammer.py:26 |
| `BIOTOP_KAMMER_SPEICHER` | Speicherlimit | `512m` | kammer.py:27 |
| `BIOTOP_KENNWORT` | Kennwort für `benutzer <name>` | leer | `__main__.py:157` |
| `OPENROUTER_API_KEY` | Schlüssel des Anbieters; fehlt er, wird `/root/.hermes/.env` gelesen | — | anbieter/__init__.py:75–84, 101; Wert [GESCHWÄRZT: /root/.hermes/.env] |
| `PYTHONHASHSEED` | von der Python-Sonde selbst gesetzt | — | kern/py/verhalten.py:37–38 |
| nur Tests: `BIOTOP_EICHWERK`, `BIOTOP_EICHDB`, `BIOTOP_EICHWERK_ID`, `BIOTOP_EICHBELEG`, `TMPDIR` | Bestandsabnahme an privaten Kopien | ohne sie wird der Test übersprungen | README.md (R112 §3) |

**Beispiele aus Skripten:**
- `pruefung/generationen.sh:3` setzt `BIOTOP_AUFTRAG_LAUF_AB=${BIOTOP_AUFTRAG_LAUF_AB:-14}` (R40 §2).
- Die T3-Skripte setzen `export BIOTOP_DB=/root/biotop-t3/t3.db`: `/root/biotop-t3/lauf32_kette.sh:6`, `lauf34_kette.sh:6`, `lauf37_kette.sh:6`, `lauf38_evolution.sh:7` (R75 §5).

### Wohin Ergebnisse, Protokolle und Kosten gehen
| Was | Wohin | Stelle |
|---|---|---|
| Läufe, Generationen, Kandidaten, Maße, Urteile, Gedächtnisse | Tabellen der Datenbank unter `BIOTOP_DB` | datenbank.py:16 |
| aufgenommenes Werk | `/root/biotop/daten/werke/<name>`, Pfad fest im Code | aufnahme.py:21 |
| Schnappschüsse | Git-Tag im Werk und `/root/biotop/daten/lazarus/lauf<n>-gen<m>.tar.gz`, Pfad fest im Code | lazarus.py:24 |
| Protokoll | Tabelle `protokoll` (Hashkette); lesen mit `protokoll`, prüfen mit `protokoll-pruefen` | protokoll.py |
| Kosten | Tabelle `kasse` je Modellaufruf, Tabelle `eichkosten` für den Vorspann; `kasse <lauf>` gibt `bericht_md` aus | kasse.py:238, 253; eichung.py |
| Befehlsausgaben | stdout; die Laufskripte leiten nach `$A/<präfix>….json` um, also in den `ausgaben/`-Ordner des Auftrags | pruefung/*.sh (R40 §2) |
| Abschlussordner | stellt Hermes zusammen und legt ihn in den Prüfkanal | MP v8 Abschnitt 9, Z.497–505 |

**Datenbankzweige** (Pfade laut REGELN-FUER-TEILE):
- STAMM: `/root/biotop/daten/biotop.db`
- VB1: `/root/phase-4-vorbedingung-1/privat/biotop.db`. Die Lazarus-Archive des Laufs 26 liegen dort in `…/privat/lazarus/` (R104 §3), nicht unter dem im Code festen Pfad. Lauf 26 lief also mit einem anderen Code-Stand.
- R02: `/root/reparatur-02/privat-cli/privat.db`
- T3: `/root/biotop-t3/t3.db`

### Schema der Kasse (Wortlaut aus `sqlite_master`, STAMM; R40 §7)
```sql
CREATE TABLE kasse (
  id INTEGER PRIMARY KEY, lauf_id INTEGER, zeit TEXT, anbieter TEXT,
  modell TEXT, tokens_ein INTEGER, tokens_aus INTEGER, kosten_eur REAL,
  zweck TEXT, kontingent INTEGER, protokoll_nr INTEGER);
CREATE TABLE eichkosten (
        id INTEGER PRIMARY KEY, lauf_id INTEGER, werk_id INTEGER, teil TEXT, kammerlaeufe INTEGER,
        modellaufrufe INTEGER, kosten_eur REAL, dauer_s REAL, erstellt_am TEXT);
```
- **Tabellen in STAMM (27):** artgedaechtnis, bandit, benutzer, eichgegenstand, eichkosten, eichung, eliten, entropie, generationen, geschmack, immunsystem, jury, kandidaten, kasse, laeufe, landkarte, lazarus, mentor, mutanten, projektgedaechtnis, protokoll, strassen, tokens, verfassung_werk, vertraege, vertraege_explizit, werke.
- **T3 zusätzlich:** `neutralzaehler` mit Index `neutralzaehler_lauf` und `vorspann_nachweise`, also 29 Tabellen.
- In den übrigen T3-Tabellen fand R40 §7 keine abweichende `CREATE`-Anweisung.
- Wortlaut aller `CREATE`-Anweisungen und Zeilen je Tabelle: R40 §7.

---

## FK35 — Tests

### Anzahl je Art (Stand 0c2f058)
- **Einteilung:** von Hermes nach Dateinamen (Auslegung Hermes).
- **Gezählt:** die Definitionen `def test…` je Datei, gerechnet aus `git show` (R72 §1, R34 D).

| Art | Dateien | Testfunktionen | davon mit `pytest.mark.integration` |
|---|---|---|---|
| T3-Tests: Sprachnaht, Organe, Wächter (`tests/test_t3_*.py`) | 37 | 156 | 8 |
| Spezifikationen und Gegenproben der Behebungsrunden vor T4 (`tests/test_vor_t4*.py`) | 5 | 128 | 0 |
| Vorspann, Eichproben, Rauschmessung | 4 | 54 | 0 |
| Messgerät und Nachweise (messnachweise, nachweis_verbraucher, junit_zeugen, kernmass_pareto, testreihenfolge) | 5 | 48 | 25 |
| TypeScript-Adapter mit echter Kammer | 1 | 18 | 18 |
| Ankläger, Doppelung, Artgedächtnis (ansage_aufnahme, doppelungsschluessel, artvorlage) | 3 | 16 | 0 |
| Verdrahtung: ganzer Lauf über die Befehlszeile, echte Kammer | 1 | 6 | 0 |
| Review-Vertrag | 1 | 6 | 0 |
| **Summe `tests/`** | **57** | **432** | **51** |
| Werk-Verträge der Übungswerke (`verfassungen/vertraege-*`; laufen am Werk, nicht am Biotop) | 7 | 31 | 0 |
| **Summe am Commit** | **64** | **463** | **51** |

**Zählweise:**
- Die Spalte „integration“ zählt Vorkommen des Markers, nicht Testfälle.
- `parametrize` vervielfacht Testfunktionen zu Testfällen: Die Regression der Runde 5 sammelte in `tests/` 693 Fälle (gerechnet 598 + 2 + 93, `REGRESSION.txt` Z.22).

**`pytest.ini`** (Wortlaut, R34 E):
- `testpaths = tests`
- `addopts = -ra --strict-markers -p no:cacheprovider`
- Marker: `integration: führt echte Kammerläufe aus; benötigt Docker und biotop-kammer:1`

**Weitere Merkmale:**
- Der Verdrahtungstest trägt keinen Marker. Er läuft also in jeder Regression mit, und zwar mit echter Kammer („Kammer: echt (Docker, netzlos, Image biotop-kammer:ts1)“, Kopf von test_verdrahtung.py, R65 §6).
- Hilfsdateien ohne Tests: `conftest.py`, `drahtwerk.py`, `speicherwerk.py`.
- `pruefung/` wird nicht gesammelt.
- Laut README ist das Netz im Testprozess gesperrt; Eigen-Tests erzeugen keine Modellkosten (R112 §3).

### Letzter lokaler Testlauf
1. **Letzte volle Regression am Commit:** `/root/biotop-vor-t4-05/REGRESSION.txt`, Dateizeit 24.09.2026 21:05:52 +0200 (R104 §2).
   - Ergebnis, Wortlaut Z.22: „598 passed, 2 skipped, 93 deselected in 2457.93s (0:40:57)“.
   - Übersprungen (Z.20–21): `tests/test_eichproben.py:280` und `tests/test_review_vertrag.py:229`, jeweils „Private Werk-/DB-Kopie nicht angegeben“.
   - Abgewählt: 93 Fälle mit Marker `integration` (BERICHT Runde 5 Z.409–410), darunter `test_t3_eichpfad` („lief in Runde 5 nicht“, `/root/biotop-vor-t4-06/UEBERGABE.md` Z.176–177).
   - Längster Fall: `test_verdrahtung.py::test_jedes_organ_wird_im_lauf_aufgerufen` mit 1.727,22 s (Z.11).
   - Laut Bericht Runde 5 (Z.41–42, 405–411):
     - JUnit: 600 Fälle, 0 Fehlschläge, 0 Fehler.
     - Verdrahtung: 23 von 23 Organen, Register 10 von 10, 0,00 €.
     - `git status` vorher und nachher leer.
2. **Jüngster belegter Lauf im Arbeitsstand der Runde 6** (nicht am Commit): voller Verdrahtungstest am 25.09.2026 von 09:58:33 bis 10:19:40 CEST (`/root/biotop-vor-t4-06/bau/hermes/H-VOLL-AUSWERTUNG.txt`).
   - Kopie: „git archive HEAD (0c2f058) … darüber jede geänderte und neue Datei aus git status — kopiert 21“, `baum_sauber False` (Z.4–5).
   - Ergebnis: „8 passed in 1266.53s“ (Z.24).
   - Register: 68 von 68 Einträgen als Kante, 10 gezählte Ausnahmen; nie gerufen: 0 (Z.26–27).
   - Modellkosten 0,0 (Z.46).
   - Hermes stuft ihn ein als „VORPRÜFUNG von S4 (Stand ohne M2(b)) … gilt als Vorprüfung, nicht als Beleg der Runde“ (UEBERGABE Runde 6 Z.201, 209–210).
   - **Danach nur Teilläufe:**
     - Durchgang 4 „379 von 380 grün (1 rot: Wächter …)“ (Z.216).
     - Nachdem Hermes den Wächter behoben hatte: 5 von 5 (Z.222–224).
   - Zum Lesezeitpunkt lief S1c noch (Durchgang 5). Seinen Endstand trägt Hermes nach.
3. **In diesem Teil:** keine Tests ausgeführt (NICHT AUSGEFÜHRT, harte Regel 2).
