# BIOTOP-LAGE-01 · Fassung 2 · `VERFASSUNGEN-TEIL1-01.md`

- **Inhalt:** FK22 · Entwurf B, Stück 1 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil B, Arbeitszeit 25.09.2026 16:10:47–17:42:51 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/verfassungen/VERFASSUNGEN-TEIL1.md` · 28642 B · SHA-256 `87a8670ae0fe8e93c5ad77aa2d674ed6afebcf8450baeb6902dca02d5814cd01`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (3 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# VERFASSUNGEN — Teil 1 von 4 (FK22) · Entwurf

**Kennung:** BIOTOP-LAGE-01 · Fassung 2 · Entwurfsteil B für `VERFASSUNGEN-NN.md` (die Nummer vergibt Hermes beim Veröffentlichen).
**Stand des Lesens:** 25.09.2026, 16:11 bis 25.09.2026 17:39 (CEST, UTC+2). Der Bau S1c lief währenddessen. Den Endstand nach S1c und Runde 6 trägt Hermes nach.
**Verfahren:** Es wurde nur gelesen. Keine Verfassung, keine Kasse und kein Code wurde verändert, kein Biotop-Code ausgeführt. Datenbanken wurden nur lesend geöffnet: STAMM mit `mode=ro&immutable=1`, bei 0 Bytes in `biotop.db-wal` vor und nach dem Zugriff; die übrigen mit `mode=ro` (R49, R50).
**Aufteilung:**
- Teil 1: Übersicht, Befunde, `lagerhaus`, `logmuehle`.
- Teil 2: T3 `versandwerk`, `drahtwerk`, Handelssystem, T4–T6.
- Teil 3: Kasse, Widersprüche, Lücken, Fragen.
- Teil 4: alle Fundorte je SHA-256 (maschinell erzeugt) und Rückprobe.

**Belegregel dieses Teils:**
- Zahlen sind *abgelesen*, wenn nicht „gerechnet“ dabeisteht; die Quelle steht jeweils dahinter.
- Rohbelege liegen in `/root/sicherung/biotop-lage-01/rohbelege/R00nn.txt`: R41 (Suche nach Name und Inhalt), R42 (Gruppierung), R49/R50 (Kassen), R71 (Masterprompt-Anhänge), R81 (`drahtwerk`, T4–T6, Zeitstempel), R93 (git, Prüfkanal, Testattrappen) sowie die Rohbelege der Skripte `b8_einsetzen.py` und `b9_rueckprobe.py` (Nummern in Teil 4 §12).
- Prüfkanal-Adressen stehen als `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/…`.

**Lesehilfe Wortlaut:**
- Jeder Wortlaut steht in einem Block zwischen zwei Zeilen aus vier Backticks. Die Zeile „Quelle“ davor nennt Pfad, Bytes, SHA-256 und den Schluss-Zeilenumbruch.
- So entsteht das Original: die Zeilen zwischen den Zäunen mit `\n` verbinden; steht „Schluss-Zeilenumbruch: ja“, ein `\n` anhängen.
- Jeder Block ist gegen das Original geprüft: beim Schreiben durch `b8_einsetzen.py` und danach unabhängig durch `b9_rueckprobe.py`. Ergebnis in Teil 4 §12.
- Die Blöcke hat ein Skript byteweise aus den Originalen eingesetzt, nicht abgetippt.

---

## 1. Übersichtstafel

| Werk | Art | Verfassung | bestätigt von (Beleg) | Pfad | SHA-256 (16) |
|---|---|---|---|---|---|
| `lagerhaus` | Übungswerk (Phasen 1–3, Vorbedingung 1) | ja, Text | Chat-Claude als Verfasser unter Delegation Philipps (Masterprompt 3.3 und Anhang A); keine gesonderte Bestätigung durch Philipp gefunden (§3.5) | `/root/biotop/verfassungen/lagerhaus.md` | `326e26163f74d982` |
| `lagerhaus` | ″ | ja, Regeln | nicht gesondert bestätigt; maschinenlesbare Umsetzung durch Hermes (§3.5) | `/root/biotop/verfassungen/lagerhaus.regeln.json` | `34d67f36719395b6` |
| `lagerhaus` (Zweig VB1) | ″ | ja, Regeln in anderer Schreibweise, JSON-gleich | wie oben; Kasse: „Hermes: unverändert bestätigter Anhang A, Übungswerk-Vollmacht“ | `/root/phase-4-vorbedingung-1/privat/verfassung.regeln.json` | `74e9d337f7ecf17d` |
| `logmuehle` | Übungswerk (Phase 3) | ja, Text | Entwurf Hermes; Chat-Claude bestätigt am Nachlaufbericht, gemeldet in der Nachricht aus Philipps Konto vom 20.09. 00:55:54 (§4.5) | `/root/biotop/verfassungen/logmuehle.md` | `0ce7f8651ae70ad0` |
| `logmuehle` | ″ | ja, Regeln | mitgebunden über die Prüfsumme `bce33200…` in Anhang B; keine eigene Bestätigung (§4.5) | `/root/biotop/verfassungen/logmuehle.regeln.json` | `bce33200a57d77e5` |
| T3 `versandwerk` (Kasse: `versandwerk-t3-02`) | Testwerk des Breitentests (TypeScript) | ja, Revision 02 | Bestätigung mit drei Auflagen (21.09. 03:35:35) und „Verfassung-02 ist bestätigt … Chat-Claude hat sie geprüft“ (21.09. 05:38:33), beide aus Philipps Konto; Kasse: „Philipp“ (Teil 2 §5.5) | `/root/biotop-t3/VERFASSUNG-T3-02.md` | `5ece12d93dc760d6` |
| T3 | ″ | ja, Regeln | nicht bestätigt; Umsetzung durch Hermes nach Revision 02, nicht im Siegelordner `verfassung-02` (Teil 2 §5.5) | `/root/biotop-t3/VERFASSUNG-T3-02.regeln.json` | `e750eb4d5033442f` |
| T3 | ″ | Entwurf 01, ersetzt | mit drei Auflagen bestätigt, danach durch Revision 02 ersetzt | `/root/biotop-t3/VERFASSUNG-T3-ENTWURF.md` | `d048a77e9faf2e24` |
| T4 | Testwerk des Breitentests | **NICHT GEFUNDEN**, noch nicht gebaut | — | — | — |
| T5 | Testwerk des Breitentests | **NICHT GEFUNDEN**, noch nicht gebaut | — | — | — |
| T6 | Testwerk des Breitentests | **NICHT GEFUNDEN**, noch nicht gebaut | — | — | — |
| `drahtwerk` | Prüfgegenstand (Verdrahtungstest, kein Testwerk des Breitentests) | ja, Konstante `VERFASSUNG` im Testcode | nie bestätigt, kein Beleg gefunden (Teil 2 §6.5) | `/root/biotop/tests/drahtwerk.py` Z. 139–146 | `13677832e59fcfef` |
| `drahtwerk` | ″ | ja, Konstante `REGELN` | nie bestätigt | `/root/biotop/tests/drahtwerk.py` Z. 148–151 | `1bb6f77ccf4da46a` |
| Handelssystem | echtes Werk; am 21.09. als Phase-4-Werk **gestrichen** | **NICHT GEFUNDEN**, nie geschrieben | — | — | — |

Die SHA-256 der Konstanten bezieht sich auf die Datei, die `anlegen()` daraus erzeugt: `VERFASSUNG.md` aus dem Zeichenkettenwert, `VERFASSUNG.regeln.json` als `json.dumps(REGELN, ensure_ascii=False, indent=1)` (Teil 2 §6).

---

## 2. Befunde

1. **Ablage und Bestätigungsfeld.** Das Biotop führt die geltende Verfassung eines Werks in der Kasse, Tabelle `verfassung_werk`.
   - Spalten: `werk_id`, `text`, `regeln`, `quelle`, `eingelegt_am`, `eingelegt_von`.
   - Eingelegt wird mit `biotop verfassung <lauf> <text.md> <regeln.json> --von <Name>`, als `INSERT OR REPLACE` je `werk_id`. Dazu entsteht eine Protokollzeile `verfassung.eingelegt`.
   - Ein Bestätigungsfeld gibt es nicht. `eingelegt_von` ist Freitext aus `--von` und wird nicht geprüft.
   - Belege: `/root/biotop/biotop/organe/verfassung.py` Z. 18–31; `/root/biotop/biotop/__main__.py` Z. 68 und 127–131. Gelesen, nicht ausgeführt.
2. **Ohne Verfassung kein Maß.** `lauf.py` bricht ab, wenn die Verfassung fehlt: „Verfassung des Werks fehlt (3.3 F2) — vor dem Maß einlegen …“ (`/root/biotop/biotop/lauf.py` Z. 108–110).
   - Die Übungswerk-Vollmacht für Freigaben hängt am Feld `regeln.uebungswerk` (Z. 575–578). Wer freigibt, steht in `ENTSCHEIDUNGEN` (FK19).
   - Gelesen, nicht ausgeführt.
3. **Kasse gegen Dateien.** In allen vier Kassenzweigen (STAMM, VB1, R02, T3) gleicht jeder Verfassungstext byteweise und jede Regel als JSON einer Datei aus §3–§5 (R50).
   - Texte ohne passende Datei: 0; Regeln ohne passende Datei: 0.
   - Zeilen je Zweig: Teil 3 §9.
4. **Verschiedene Verfassungen.** Es gibt vier Werke mit Verfassung: `lagerhaus`, `logmuehle`, T3 und `drahtwerk`.
   - Verschiedene Textinhalte: 6 (gerechnet: je einer für `lagerhaus` und `logmuehle`, zwei für T3 mit Entwurf 01 und Revision 02, zwei für `drahtwerk` mit einer älteren Variante nur in `/tmp`).
   - Verschiedene Regeldateien: 5 nach Bytes, 4 nach JSON-Inhalt (gerechnet; `lagerhaus` liegt in zwei Schreibweisen vor).
   - Nachweis: R42, R50, R81.
5. **Masterprompt-Anhänge gegen Dateien** (R71, satzweise nach Entfernen von `**` und Backticks):
   - Anhang A und `lagerhaus.md`: Sätze 1–6 gleich.
   - Anhang B und `logmuehle.md`: Sätze 2–6 gleich. In Satz 1 fehlt dem Anhang „Es ist ein“ vor „Übungswerk ohne Betriebszweck“.
   - Die Kopfzeilen weichen jeweils ab (Wortlaut in §3.4 und §4.4).
6. **Läufe an Werken ohne Verfassungszeile.** Im STAMM haben die Werke 1–4 keine Zeile: `lagerhaus`, `lagerhaus-ohne-tests`, `lagerhaus-kasse`, `lagerhaus-kasse2`.
   - Läufe an diesen Werken: 1 und 2 (Werk 1), 4 (Werk 3), 5 (Werk 4). Läufe 3 und 11 tragen keine `werk_id` (R50).
   - Die Verfassungspflicht kam mit Masterprompt Fassung 2, im Chat am 19.09. 00:36:30. Die erste Einlegung erfolgte am 19.09. 00:48:45 (Protokoll-Nr. 838, R50).
   - Die Chronik der Läufe steht in `CHRONIK` (FK10).
7. **Wer schreibt, wer bestätigt** — Wortlaut Masterprompt v8, Abschnitt 3.3:
   - „**Ablauf:** Das Biotop schlägt aus Landkarte und Aufnahmebericht einen Entwurf vor (5–15 Sätze). Philipp streicht, ergänzt, bestätigt. Erst dann ist sie gültig.“
   - „**Regel:** … Die Verfassung ändert nur Philipp.“
   - „**Übungswerke:** … Für Übungswerke schreibt Chat-Claude die Verfassung; Philipp hat die Entscheidung delegiert.“
   - Abschnitt 8 Phase 5, Vorbedingung 1: „**Verfassung des Werks** — schreibt Philipp; Hermes legt einen Entwurf vor.“
   - Abschnitt 8 Phase 4 nennt keine Verfassung: Die Suche nach „erfassung“ findet dort keinen Treffer (Dokumentkopie `arbeit/dokumente/2026-09-23_155353_…-v8.md`, Z. 414–476).
   - Für Testwerke ist also nicht geregelt, wer schreibt und wer bestätigt. Frage dazu in Teil 3 §10.

---

## 3. `lagerhaus`

### 3.1 Werk
- Übungswerk, Python, versiegelte Schwächen S1–S5; es trägt die Phasen 1–3 und Vorbedingung 1. Umfang: `LAGE` (FK25).
- Kassenzeilen mit dieser Verfassung (R50):
  - STAMM: 16 Werkzeilen, `werk_id` 5–14, 16–19, 21 und 22 (Namen `lagerhaus-*`).
  - VB1: zusätzlich `werk_id` 23 (`lagerhaus-vorbedingung1-26`).
- Maßgebliche Datei: `/root/biotop/verfassungen/lagerhaus.md`.
  - In git seit Commit `0d80f78` (19.09. 01:19:56, Autor `hermes <hermes@local>`, „Nachlauf: Maß F2, Verfassung, Befundklassen, …“).
  - Blob an HEAD `0c2f058` bytegleich mit der Platte (R93).
  - Änderungszeit der Datei: 19.09. 00:46:48 (R81).

### 3.2 Wortlaut (Text)
Quelle: `/root/biotop/verfassungen/lagerhaus.md` · 1506 Bytes · SHA-256 `326e26163f74d9822961d2569e17188d4fde381dc866c565909a2df32861ba14` · Schluss-Zeilenumbruch: ja

````text
Verfassung des Übungswerks „lagerhaus" — Masterprompt v2, Anhang A (Chat-Claude; Philipp hat delegiert)
1. Was es ist: Ein Rabatt- und Lagerrechner für Verkaufsberichte. Es rechnet Preise mit Staffeln und Rabatten, führt Bestand aus einem Journal mit Reservierungen und erzeugt daraus Auswertungen. Es ist ein Übungswerk ohne Betriebszweck.
2. Sicherheit vor Geschwindigkeit: Kein Bereich darf Eingaben als Programmcode ausführen — weder mit eval/exec noch mit eingeschränkten Namensräumen. Ein Sicherheitsbefund wiegt mehr als jede Laufzeit. Tauschregel: Die Laufzeit auf der Referenzlast darf bis ×5 gegenüber dem Ausgangszustand steigen, wenn dabei ein statischer Sicherheitsbefund verschwindet; sonst gilt ×2.
3. Korrektheit vor allem anderen: Kein Bestand unter null; keine Reservierung, die nach dem Einlösen weiter zählt; keine negativen Rabatte; Staffelgrenzen sind inklusiv („ab 10 Stück" gilt bei 10).
4. Grenzen sind Verträge: Die Schnittstellen zwischen formeln, preise, lager und bericht ändern sich nur, wenn beide Seiten in derselben Generation angepasst und gemeinsam geprüft werden.
5. bericht ist Ausgabe, keine Logik: Der Bereich rechnet nichts selbst nach, was preise oder lager liefern; er formatiert.
6. Was nie passieren darf: Ein Kandidat, der Tests entfernt oder abschwächt, um einen Fehlschlag zu beseitigen; ein Kandidat, der einen Sicherheitsbefund durch Ausnahmeregel im Prüfwerkzeug (# nosec, Konfiguration) zum Verschwinden bringt statt durch Code.
````

### 3.3 Wortlaut (Regeln)
Quelle: `/root/biotop/verfassungen/lagerhaus.regeln.json` · 806 Bytes · SHA-256 `34d67f36719395b6cff4c9bed88b8b506ae525943aa7c84682b7c0167ad27abc` · Schluss-Zeilenumbruch: ja

````json
{
  "uebungswerk": true,
  "quelle": "Masterprompt v2 Anhang A, Satz 2 (Tauschregel) und Satz 6 (verbotene Muster)",
  "tausch": {"laufzeit_faktor": 2.0, "laufzeit_faktor_bei_sicherheitsgewinn": 5.0, "sonst_faktor": 1.25},
  "verbotene_muster": ["# nosec", "#nosec", "noqa: S", "[bandit]", "skips ="],
  "einstiege": {
    "B307": {"formeln": {"import": "from lagerhaus.formeln import auswerten", "aufruf": "auswerten({formel}, 1, 1.0, 1.0)",
                          "fehler_import": "from lagerhaus.formeln import FormelFehler", "fehler": "FormelFehler"}},
    "B102": {"formeln": {"import": "from lagerhaus.formeln import auswerten", "aufruf": "auswerten({formel}, 1, 1.0, 1.0)",
                          "fehler_import": "from lagerhaus.formeln import FormelFehler", "fehler": "FormelFehler"}}
  }
}
````

Dieselben Regeln liegen im Zweig VB1 in einer anderen Schreibweise vor: eine Zeile, ohne Schluss-Zeilenumbruch, JSON-gleich (R50).
- Eingelegt für `werk_id` 23 am 20.09. 21:32:13 (Protokoll-Nr. 16068, R50).
- Die Textkopie `/root/phase-4-vorbedingung-1/privat/verfassung.md` ist bytegleich mit §3.2 (SHA-256 `326e26163f74d9822961d2569e17188d4fde381dc866c565909a2df32861ba14`).

Quelle: `/root/phase-4-vorbedingung-1/privat/verfassung.regeln.json` · 729 Bytes · SHA-256 `74e9d337f7ecf17d84fd6c66e05eeb68e2486b7cc96b900400a1b0becb14fe72` · Schluss-Zeilenumbruch: nein

````json
{"uebungswerk": true, "quelle": "Masterprompt v2 Anhang A, Satz 2 (Tauschregel) und Satz 6 (verbotene Muster)", "tausch": {"laufzeit_faktor": 2.0, "laufzeit_faktor_bei_sicherheitsgewinn": 5.0, "sonst_faktor": 1.25}, "verbotene_muster": ["# nosec", "#nosec", "noqa: S", "[bandit]", "skips ="], "einstiege": {"B307": {"formeln": {"import": "from lagerhaus.formeln import auswerten", "aufruf": "auswerten({formel}, 1, 1.0, 1.0)", "fehler_import": "from lagerhaus.formeln import FormelFehler", "fehler": "FormelFehler"}}, "B102": {"formeln": {"import": "from lagerhaus.formeln import auswerten", "aufruf": "auswerten({formel}, 1, 1.0, 1.0)", "fehler_import": "from lagerhaus.formeln import FormelFehler", "fehler": "FormelFehler"}}}}
````

Werte in den Regeln, die der Text nicht nennt:
- `sonst_faktor` 1.25;
- die Einstiege für die Befundklassen B307 und B102;
- die Musterliste `"# nosec"`, `"#nosec"`, `"noqa: S"`, `"[bandit]"`, `"skips ="`. Der Text nennt in Satz 6 nur „`# nosec`, Konfiguration“.

*Auslegung Hermes:* Diese Werte hat Hermes aus Masterprompt 3.5 (Grenzmaß +25 %) und aus dem Befundklassen-Katalog umgesetzt. So beschreibt es der Bericht `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/BERICHT.md` Z. 39: „Anhang A eingelegt (Text + maschinenlesbare Regeln: Tauschregel, verbotene Muster, Einstiege für Befundklassen, `uebungswerk=true`)“.

### 3.4 Wortlaut im gültigen Masterprompt (Fassung 8, Anhang A)
Quelle: `/root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-23_155353_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md`, Zeilen 520–529 · 1652 Bytes · SHA-256 `2639327bb1179d19544996720886a5f06d80926c627b8b56cacf3333d3ae6560` · Schluss-Zeilenumbruch: ja

````text
## Anhang A — Verfassung des Übungswerks `lagerhaus`

Geschrieben von Chat-Claude (Philipp hat die Entscheidung delegiert). Gilt für Lauf 3 und alle weiteren Läufe am Übungswerk. Ändert nur Philipp.

1. **Was es ist:** Ein Rabatt- und Lagerrechner für Verkaufsberichte. Es rechnet Preise mit Staffeln und Rabatten, führt Bestand aus einem Journal mit Reservierungen und erzeugt daraus Auswertungen. Es ist ein Übungswerk ohne Betriebszweck.
2. **Sicherheit vor Geschwindigkeit:** Kein Bereich darf Eingaben als Programmcode ausführen — weder mit `eval`/`exec` noch mit eingeschränkten Namensräumen. Ein Sicherheitsbefund wiegt mehr als jede Laufzeit. Tauschregel: Die Laufzeit auf der Referenzlast darf bis **×5** gegenüber dem Ausgangszustand steigen, wenn dabei ein statischer Sicherheitsbefund verschwindet; sonst gilt ×2.
3. **Korrektheit vor allem anderen:** Kein Bestand unter null; keine Reservierung, die nach dem Einlösen weiter zählt; keine negativen Rabatte; Staffelgrenzen sind inklusiv („ab 10 Stück" gilt bei 10).
4. **Grenzen sind Verträge:** Die Schnittstellen zwischen `formeln`, `preise`, `lager` und `bericht` ändern sich nur, wenn beide Seiten in derselben Generation angepasst und gemeinsam geprüft werden.
5. **`bericht` ist Ausgabe, keine Logik:** Der Bereich rechnet nichts selbst nach, was `preise` oder `lager` liefern; er formatiert.
6. **Was nie passieren darf:** Ein Kandidat, der Tests entfernt oder abschwächt, um einen Fehlschlag zu beseitigen; ein Kandidat, der einen Sicherheitsbefund durch Ausnahmeregel im Prüfwerkzeug (`# nosec`, Konfiguration) zum Verschwinden bringt statt durch Code.
````

Anhang A in allen Fassungen (R71, satzweiser Vergleich):
- Kopfzeile und Sätze 1–6 sind in v2 bis v8 gleich; es gibt keine Abweichung.
- Die Abschnittsprüfsummen unterscheiden sich trotzdem: v2–v5 je 1.657 Bytes, SHA-256 `1350f516…`; v6–v8 je 1.652 Bytes, SHA-256 `2639327b…`.
  - Ursache ist die Abgrenzung im Skript `b4_anhaenge.py` (von „## Anhang A“ bis vor die nächste „## “-Überschrift, Trennzeilen am Schluss entfernt).
  - In v2–v5 ist Anhang A der letzte Abschnitt. Dort bleibt die Trennzeile „---“ vor „*Ende des Dokuments*“ stehen und wird mitgezählt.
- In v1 gibt es keinen Anhang A.
- Der Block oben ist genau die Zeilen 520–529 der Dokumentkopie von v8. Originalpfad und SHA-256 der Fassung: `MASTERPROMPT-GUELTIG` (FK14).

### 3.5 Bestätigung — Belege
- **Masterprompt v2, 3.3** (im Chat 19.09. 00:36:30, von Philipps Konto hochgeladen; `philipp-ab-2026-09-18.md` Z. 22–23; Dokumentkopie Z. 75): „Für Übungswerke schreibt Chat-Claude die Verfassung; Philipp hat die Entscheidung delegiert. Die Verfassung des Übungswerks `lagerhaus` steht in Anhang A.“ Der Wortlaut steht gleich in v8 (Z. 161).
- **Änderungsverzeichnis v2** (`arbeit/fassungen/aenderungen-v2.md` Z. 3): „- 3.3: Verfassung auch für Übungswerke; Verfassung des Übungswerks `lagerhaus` im Anhang A.“
- **Kopfzeile Anhang A** (§3.4): „Geschrieben von Chat-Claude (Philipp hat die Entscheidung delegiert). Gilt für Lauf 3 und alle weiteren Läufe am Übungswerk. Ändert nur Philipp.“
- **Kasse, `eingelegt_von`** (R50):
  - „Chat-Claude (Anhang A, Masterprompt v2), eingelegt durch Hermes“: `werk_id` 5–8.
  - „Chat-Claude (Anhang A)“: 9, 21, 22.
  - „Chat-Claude (Anhang A, Masterprompt v3), eingelegt durch Hermes“: 10, 11.
  - „Chat-Claude (Anhang A, Masterprompt v4), eingelegt durch Hermes“: 12–14, 16–19.
  - „Hermes: unverändert bestätigter Anhang A, Übungswerk-Vollmacht“: VB1 23.
- **Nachricht Philipps**, die Anhang A gesondert bestätigt: **keine gefunden**. Die Suchen nach „Anhang A“ und „delegier“ in `arbeit/lesen/philipp-ab-2026-09-18.md` ergaben 0 Treffer.
- Die **Delegation** selbst steht nur im Masterprompt. Eine Nachricht, mit der Philipp sie erteilt, liegt in keiner Quelle ab dem 18.09. vor: **UNBEKANNT** (Lücke, Teil 3 §10).
  - Gegenprobe über alle Absender in `arbeit/verlauf/wortlaut.jsonl` (`search_files` nach „delegier“, abgelesen): 21 Nachrichten. 8 kommen aus Philipps Konto: die hochgeladenen Masterprompt-Fassungen v2 (id 831), v3 (997), v4 (1393), v5 (2232), v6 (2718), v7 (9105) und v8 (13998) sowie der Auftrag BIOTOP-LAGE-01 v2 (20987). Die übrigen 13 tragen den Absender „System-Verdichtung“.
- **Regeldatei:** Eine Bestätigung durch Chat-Claude oder Philipp wurde nicht gefunden.
- **Einordnung** (Auslegung Hermes): Urheber ist Chat-Claude, unter der im Masterprompt festgehaltenen Delegation Philipps. Für das Entscheidungsregister (FK17) ist das die Kategorie „an Chat-Claude delegiert“. Die Regeln sind eine Umsetzung durch Hermes, unbestätigt.

---

## 4. `logmuehle`

### 4.1 Werk
- Zweites Übungswerk, Python, Phase 3; Befehlszeilenwerkzeug für Zugriffsprotokolle. Umfang: `LAGE` (FK25).
- Kassenzeilen (R50): STAMM `werk_id` 15 (`logmuehle-17`) und 20 (`logmuehle-23`).
- Maßgebliche Datei: `/root/biotop/verfassungen/logmuehle.md`.
  - In git seit Commit `791aae5` (19.09. 13:54:43, „Phase 3: Gedächtnisse, Mentor, Entropie, Jury, Web-Oberfläche, Referenzlast logmuehle, Befundklasse B602“).
  - Blob an HEAD bytegleich (R93). Änderungszeit 19.09. 13:38:36, Regeln 13:39:25 (R81).

### 4.2 Wortlaut (Text)
Quelle: `/root/biotop/verfassungen/logmuehle.md` · 1841 Bytes · SHA-256 `0ce7f8651ae70ad0783cb6caa8f54b9ebbcf789b5e6b116d6df6fb63242bc803` · Schluss-Zeilenumbruch: ja

````text
Verfassung des Übungswerks „logmuehle" — Entwurf Hermes (Masterprompt v4 Abschnitt 8 Phase 3; Chat-Claude bestätigt am Bericht). Ändert nur Philipp.
1. Was es ist: Ein Befehlszeilenwerkzeug, das Zugriffsprotokolle im Common Log Format liest, nach Zeit, Status und Pfad filtert, Kennzahlen bildet und sie als Text, CSV oder JSON ausgibt. Es ist ein Übungswerk ohne Betriebszweck; es verarbeitet nur Dateien, die der Aufrufer nennt.
2. Sicherheit vor Bequemlichkeit: Kein Bereich reicht Eingaben des Aufrufers an eine Shell weiter oder führt sie als Programmcode aus; externe Werkzeuge werden nur als Argumentliste ohne Shell gestartet. Ein Sicherheitsbefund wiegt mehr als jede Laufzeit. Tauschregel: Die Laufzeit auf der Referenzlast darf bis ×3 gegenüber dem Bestwert des Laufs steigen, wenn dabei ein statischer Sicherheitsbefund verschwindet; sonst gilt ×2.
3. Korrektheit der Zählung: Jeder gelesene Eintrag wird genau einmal gezählt; unlesbare Zeilen werden gezählt und gemeldet, nie verschluckt; Zeitfenster sind an beiden Enden einschließlich; Zeiten sind zeitzonenbewusst und werden nach UTC normalisiert; Perzentile folgen dem nächsten Rang.
4. Grenzen sind Verträge: Die Schnittstellen zwischen lesen, filtern, zaehlen und ausgabe ändern sich nur, wenn beide Seiten in derselben Generation angepasst und gemeinsam geprüft werden.
5. ausgabe ist Darstellung, keine Logik: Der Bereich rechnet nichts nach, was zaehlen liefert; er formatiert und setzt Rückgabecodes.
6. Was nie passieren darf: Ein Kandidat, der Tests entfernt oder abschwächt, um einen Fehlschlag zu beseitigen; ein Kandidat, der einen Sicherheitsbefund durch Ausnahmeregel im Prüfwerkzeug (# nosec, Konfiguration) zum Verschwinden bringt statt durch Code; ein Kandidat, der Dateien außerhalb der genannten Protokolldatei liest oder schreibt.
````

### 4.3 Wortlaut (Regeln)
Quelle: `/root/biotop/verfassungen/logmuehle.regeln.json` · 691 Bytes · SHA-256 `bce33200a57d77e5a9254e0da271c38c9ce23404506cc6cfb0bf902e5051b0c8` · Schluss-Zeilenumbruch: ja

````json
{
  "uebungswerk": true,
  "quelle": "Verfassung logmuehle (Entwurf Hermes, Masterprompt v4 Phase 3), Satz 2 (Tauschregel) und Satz 6 (verbotene Muster)",
  "tausch": {"laufzeit_faktor": 2.0, "laufzeit_faktor_bei_sicherheitsgewinn": 3.0, "sonst_faktor": 1.25},
  "verbotene_muster": ["# nosec", "#nosec", "noqa: S", "[bandit]", "skips ="],
  "einstiege": {
    "B602": {"filtern": {"import": "from logmuehle.filtern import extern_filtern\nfrom logmuehle.lesen import zeile_lesen", "aufruf": "extern_filtern([zeile_lesen('h - - [19/Sep/2026:10:00:00 +0000] \"GET /a HTTP/1.1\" 200 1')], {befehl}, zeitlimit_s=10)",
                          "fehler_import": "", "fehler": "Exception"}}
  }
}
````

### 4.4 Wortlaut im gültigen Masterprompt (Fassung 8, Anhang B)
Quelle: `/root/sicherung/biotop-lage-01/arbeit/dokumente/2026-09-23_155353_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md`, Zeilen 536–547 · 2262 Bytes · SHA-256 `7d23f013a52700c33ea48e22dd2219bf4577bf408a21e1081d961b434ad64cfd` · Schluss-Zeilenumbruch: ja

````text
## Anhang B — Verfassung des Übungswerks `logmuehle`

Entwurf Hermes, **von Chat-Claude bestätigt** (19.09.2026, am Nachlaufbericht Abschnitt 9; Prüfsumme der Datei `0ce7f865…`, Regeln `bce33200…`). Gilt für alle Läufe am Übungswerk `logmuehle`. Ändert nur Philipp.

1. **Was es ist:** Ein Befehlszeilenwerkzeug, das Zugriffsprotokolle im Common Log Format liest, nach Zeit, Status und Pfad filtert, Kennzahlen bildet und sie als Text, CSV oder JSON ausgibt. Übungswerk ohne Betriebszweck; es verarbeitet nur Dateien, die der Aufrufer nennt.
2. **Sicherheit vor Bequemlichkeit:** Kein Bereich reicht Eingaben des Aufrufers an eine Shell weiter oder führt sie als Programmcode aus; externe Werkzeuge werden nur als Argumentliste ohne Shell gestartet. Ein Sicherheitsbefund wiegt mehr als jede Laufzeit. Tauschregel: Die Laufzeit auf der Referenzlast darf bis ×3 gegenüber dem Bestwert des Laufs steigen, wenn dabei ein statischer Sicherheitsbefund verschwindet; sonst gilt ×2.
3. **Korrektheit der Zählung:** Jeder gelesene Eintrag wird genau einmal gezählt; unlesbare Zeilen werden gezählt und gemeldet, nie verschluckt; Zeitfenster sind an beiden Enden einschließlich; Zeiten sind zeitzonenbewusst und werden nach UTC normalisiert; Perzentile folgen dem nächsten Rang.
4. **Grenzen sind Verträge:** Die Schnittstellen zwischen `lesen`, `filtern`, `zaehlen` und `ausgabe` ändern sich nur, wenn beide Seiten in derselben Generation angepasst und gemeinsam geprüft werden.
5. **`ausgabe` ist Darstellung, keine Logik:** Der Bereich rechnet nichts nach, was `zaehlen` liefert; er formatiert und setzt Rückgabecodes.
6. **Was nie passieren darf:** Ein Kandidat, der Tests entfernt oder abschwächt, um einen Fehlschlag zu beseitigen; ein Kandidat, der einen Sicherheitsbefund durch Ausnahmeregel im Prüfwerkzeug (`# nosec`, Konfiguration) zum Verschwinden bringt statt durch Code; ein Kandidat, der Dateien außerhalb der genannten Protokolldatei liest oder schreibt.

Satz 2 wurde vom Schwarm anders erfüllt als erwartet — der Subprozess wurde ganz entfernt statt abgesichert; am Maß gemessen besser. Satz 6 ist mechanisch verdrahtet (`verbotene_muster`), Satz 2 über die Tauschregel (`laufzeit_faktor_bei_sicherheitsgewinn: 3.0`).
````

Anhang B in allen Fassungen (R71):
- v6, v7 und v8 sind gleich: 2.267 Bytes, SHA-256 `6075ef3c…` (Abgrenzung wie bei Anhang A).
- Vor v6 gibt es keinen Anhang B.
- Gegen die Datei (§4.2) fehlt in Satz 1 „Es ist ein“ vor „Übungswerk ohne Betriebszweck“. Die Sätze 2–6 sind gleich, sobald die Auszeichnung entfernt ist.
- Der Anhang nennt als Prüfsummen `0ce7f865…` für die Datei und `bce33200…` für die Regeln. Beide gleichen den heutigen Dateien (§1).
- Der Block oben ist genau die Zeilen 536–547 der Dokumentkopie von v8.

### 4.5 Bestätigung — Belege, zeitlich geordnet (CEST)
1. **Masterprompt v4**, im Chat 19.09. 12:39:25; Abschnitt 8 Phase 3 (Dokumentkopie Z. 307): „Für das zweite Übungswerk schreibt Hermes den Verfassungsentwurf, Chat-Claude bestätigt ihn am Bericht.“
2. **Einlegung** `werk_id` 15 am 19.09. 13:55:53 (Protokoll-Nr. 7547, R50) mit `eingelegt_von` „Hermes (Entwurf, Masterprompt v4 Phase 3; Chat-Claude bestätigt am Bericht)“.
3. **Hermes an Philipp**, 19.09. 19:36:52 (id 2233; `arbeit/lesen/hermes-an-philipp.md` Z. 427): „Ein Fehler von mir, den v5 aufdeckt: Der `logmuehle`-Verfassungsentwurf **lag dem Bericht nicht bei**. Er existiert (`verfassungen/logmuehle.md`, 8 Sätze), ich habe ihn nur verwiesen statt abgedruckt — damit konntest du ihn nicht bestätigen. Kommt in den Nachlaufbericht, vollständig im Text.“
4. **Einlegung** `werk_id` 20 am 19.09. 23:33:14 (Protokoll-Nr. 13334) mit `eingelegt_von` „Hermes (Entwurf, Chat-Claude bestaetigt am Bericht)“.
5. **Nachlaufbericht** `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/BERICHT.md`, Abschnitt „9. Punkt 8 — Verfassungsentwurf `logmuehle` (zur Bestätigung durch Chat-Claude)“.
   - Datei: 18.916 Bytes, SHA-256 `999a0c48…`, Änderungszeit 19.09. 23:59:31 (R71, R93); Commit `7c73d40` um 23:59:59 („… Verfassungsentwurf abgedruckt; Abschlussbericht Nachlauf“, R13).
   - Der Abschnitt nennt die Prüfsummen `0ce7f865…` und `bce33200…` und gibt den Text wörtlich als Zitat wieder.
   - Abgleich mit §4.2 als Sichtvergleich mit `read_file` an der Ausgabe von R71, nicht maschinell. Nach Entfernen von `**`, Backticks, Zitatzeichen `> ` und Zeilenumbrüchen sind Kopfzeile und Sätze 1–6 gleich. Satz 1 enthält „Es ist ein Übungswerk“ wie die Datei, anders als Anhang B.
   - Grund für den Sichtvergleich: Nach dem Hinweis von Hermes vom 25.09. werden Berichte im Prüfkanal nicht mehr im Terminal gelesen.
6. **Masterprompt v6**, im Chat 20.09. 00:18:44. Änderungsverzeichnis (`aenderungen-v6.md` Z. 10): „- Anhang B neu: **Verfassung des Übungswerks `logmuehle`**, von Chat-Claude bestätigt.“ Dazu die Kopfzeile von Anhang B (§4.4).
7. **Nachricht aus Philipps Konto**, 20.09. 00:55:54 (id 2798; `philipp-ab-2026-09-18.md` Z. 136), Auszug: „Nachlauf abgenommen, alle neun Punkte geprüft — … logmuehle-Verfassung bestätigt als Anhang B.“

**Einordnung** (Auslegung Hermes):
- Bestätigt hat Chat-Claude am Nachlaufbericht, so wie Masterprompt v4 es für das zweite Übungswerk vorgab.
- Die Regeln sind über ihre Prüfsumme in Anhang B mitgebunden; eine eigene Bestätigung der Regeln gibt es nicht.
- Die Kassenfelder aus Punkt 2 und 4 nennen „Chat-Claude bestätigt am Bericht“ schon vor der Bestätigung (Punkt 3: „damit konntest du ihn nicht bestätigen“). Die Läufe 17 und 23 liefen an einer zu diesem Zeitpunkt unbestätigten Verfassung. Widerspruch: Teil 3 §10.
