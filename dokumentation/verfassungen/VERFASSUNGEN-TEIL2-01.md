# BIOTOP-LAGE-01 · Fassung 2 · `VERFASSUNGEN-TEIL2-01.md`

- **Inhalt:** FK22 · Entwurf B, Stück 2 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil B, Arbeitszeit 25.09.2026 16:10:47–17:42:51 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/verfassungen/VERFASSUNGEN-TEIL2.md` · 27834 B · SHA-256 `0fd87be6b8ac6c6ce7220294ebbcb86d3f923c11a5a6c8dfbf30aefb06af8ea2`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (12 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# VERFASSUNGEN — Teil 2 von 4 (FK22) · Entwurf

Fortsetzung von Teil 1. Stand des Lesens, Verfahren, Belegregel und Lesehilfe stehen dort; dieselben Regeln gelten hier.

---

## 5. T3 `versandwerk` (TypeScript)

### 5.1 Werk
- Erstes Testwerk des Breitentests, TypeScript, fünf Bereiche: `eingang`, `tarife`, `planung`, `bericht`, `zahlen`.
- Kasse (Zweig T3, `/root/biotop-t3/t3.db`, R50): `werk_id` 23, Name `versandwerk-t3-02`, Läufe 26–38.
- Werkordner (R41): `/root/versandwerk-t3`, `/root/versandwerk-t3-02`, `/root/biotop/daten/werke/versandwerk-t3-02`. Umfang: `LAGE` (FK25).
- Die Verfassung nennt das Werk `versandwerk`, die Kasse `versandwerk-t3-02`: gleiches Werk, zwei Namen (Zuordnung in `INVENTAR`).
- Die Verfassungsdateien liegen nur im T3-Arbeitsordner und im Prüfkanal, nicht im Biotop-Baum `/root/biotop/verfassungen/` (R41, R93).

### 5.2 Wortlaut Revision 02 (geltend)
Quelle: `/root/biotop-t3/VERFASSUNG-T3-02.md` · 4418 Bytes · SHA-256 `5ece12d93dc760d6bfb834d7d1cd53e29065bd54d673e2381a23d50234f78a28` · Schluss-Zeilenumbruch: ja

````text
# Verfassung T3 — versandwerk (Revision 02)

Status: bestätigt mit drei Auflagen in Philipps Nachricht vom 21.09.2026; die Auflagen sind in den Sätzen 3, 4 und 8 eingearbeitet. Die konkrete Half-up-Rundungsregel ist eine Entscheidung von Hermes zur Umsetzung der Auflage 2. Nach Versiegelung dieser Revision ist keine weitere Verfassungsrückfrage erforderlich; sämtliche technischen Startbedingungen des Biotops bleiben verbindlich.

1. **Zweck:** `versandwerk` ist ein TypeScript-Übungswerk ohne Betriebszweck. Es prüft fiktive Sendungsdaten, berechnet Tarife, bündelt Sendungen und erstellt Berichte; es beauftragt keinen Versand, verarbeitet keine personenbezogenen Daten und verändert keine Dateien oder externen Systeme.
2. **Sicherheit:** Eingaben sind Daten, niemals Programme. Weder `eval` noch `Function` dürfen Eingabetext ausführen; auch indirekte Zugriffe auf globale Objekte und Prototype-Manipulation durch Eingaben sind unzulässig. Ungültige Eingaben werden ausdrücklich abgewiesen.
3. **Korrektheit:** Mengen und Gewichte sind endlich und nicht negativ, abgerechnete Geldbeträge werden in ganzen Cent geführt, Obergrenzen sind einschließlich. Sendungen werden genau einmal berücksichtigt; negative Rabatte, negative Endpreise und still verworfene Sendungen sind unzulässig. Der Endpreis jeder einzelnen Sendung wird nach Anwendung aller tariflichen Bestandteile, Zuschläge und Rabatte genau einmal auf den nächstgelegenen ganzen Cent gerundet; ein Rest von exakt einem halben Cent wird zum höheren Cent gerundet (Half-up für die zulässigen nichtnegativen Beträge). Bis zu dieser Stelle werden die Zwischenergebnisse exakt und ohne Rundung geführt. Sammel- und Berichtssummen entstehen ausschließlich durch Addition dieser bereits abgerechneten Sendungsendpreise, ohne erneute Rundung. Eine andere Rundungsrichtung, eine verschobene Rundungsstelle oder zusätzliche Zwischenrundung verletzt diesen Satz, auch wenn einzelne Endwerte zufällig übereinstimmen.
4. **Grenzen:** Die fünf Bereiche `eingang`, `tarife`, `planung`, `bericht` und `zahlen` verändern Eingabeobjekte nicht. `bericht` formatiert Ergebnisse, er berechnet keine Tarife nach. Grenzverträge dürfen nur zusammen mit der geprüften Anpassung beider Seiten geändert werden. Kein Bereich verändert `Object.prototype`, andere eingebaute Prototypen oder gemeinsam genutzte Standardwerte, auch nicht innerhalb des eigenen Bereichs und auch nicht vorübergehend. Eine Beeinflussung anderer Bereiche über solche geteilten Prototypen oder Standardwerte ist unzulässig; dieses Verbot gilt unabhängig davon, ob Eingabetext beteiligt ist.
5. **Tragender Pfad:** `bericht` verwendet `planung`, `planung` verwendet `tarife` und `eingang`, `tarife` verwendet `zahlen`; für den Eichgegenstand ist das Paar `planung` → `tarife` vorrangig. `zahlen` ist der saubere Vergleichsbereich.
6. **Maß und Tausch:** Es gilt das Kernmaß aus Abschnitt 3.5 Fassung 7, Pareto je Test und Bestwertbezug; Standardtausch: Laufzeit höchstens ×2 bei Kernmaßgewinn, sonstige Grenzmaße höchstens +25 Prozent, größte Funktion nach der 60-Zeilen-Regel. Ohne Kernmaßgewinn gilt die gemessene Rauschtoleranz. Sicherheitsgewinn erhält keine zusätzliche Ausnahme.
7. **Unzulässig:** vorhandene Tests löschen, überspringen oder abschwächen; Prüfwerkzeuge, deren Konfiguration oder Referenzlast manipulieren; Befunde durch Unterdrückungs-Kommentare statt durch Codebehebung beseitigen. Neue Tests dürfen nur nach dem paarweisen Ausführungsnachweis aufgenommen werden.
8. **Betrieb:** Jeder Werk-/Testlauf bleibt in der netzlosen Kammer. Die Übungswerk-Vollmacht gilt für dokumentierte Generationenfreigaben und Mentorwahl; sie ersetzt keine Bestätigung dieser Verfassung. Ablehnung, Zeitüberschreitung oder leere Antwort eines Verbundmodells werden als Ausfall gezählt und niemals als Beitrag, auch nicht bei HTTP 200 oder erfolgreichen Antworten anderer Mitglieder. Protokollabschluss und nutzbarer Beitrag werden getrennt geführt. Für dieses Testwerk ist mindestens ein echter oder ausdrücklich gestellter Ausfall im tatsächlich verwendeten Beitragspfad nachzuweisen und mit eigener Ausfallmeldung zu protokollieren (Tor 4, Fassung 7). Die Kasse führt den Ausfall nach belegtem Verbrauch; unbekannter Verbrauch wird nicht als null ausgewiesen. Der Auftrag endet an T3, nicht mit einem selbsttätigen T4-Start.
````

Kopien mit derselben SHA-256 im Prüfkanal (Teil 4 §11):
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-02/VERFASSUNG-T3.md` (Siegelordner);
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-01/VERFASSUNG-T3-02.md`;
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/uebernahme-01/VERFASSUNG-T3-02.md`.

### 5.3 Wortlaut Regeln (maschinenlesbarer Teil)
Quelle: `/root/biotop-t3/VERFASSUNG-T3-02.regeln.json` · 1398 Bytes · SHA-256 `e750eb4d5033442f842028c5b2fde5c403dedfcf9b2c05260091bc6c0269e54b` · Schluss-Zeilenumbruch: ja

````json
{
  "uebungswerk": true,
  "sprache": "TypeScript",
  "tragender_pfad": [["planung", "tarife"]],
  "tausch": {
    "laufzeit_faktor": 2.0,
    "laufzeit_faktor_bei_sicherheitsgewinn": 2.0,
    "sonst_faktor": 1.25,
    "groesste_funktion_absolut": 60
  },
  "verbotene_muster": ["eslint-disable", "@ts-ignore", "@ts-nocheck", ".skip(", ".todo(", ".only("],
  "einstiege": {
    "no-new-func": {
      "tarife": {
        "sprache": "TypeScript",
        "import": "import {ausdruck} from '../src/tarife/ausdruck.js';",
        "aufruf": "ausdruck({formel}, {gewicht:1,grund:2})",
        "fehler_import": "",
        "fehler": "Error"
      }
    },
    "security/detect-eval-with-expression": {
      "tarife": {
        "sprache": "TypeScript",
        "import": "import {ausdruck} from '../src/tarife/ausdruck.js';",
        "aufruf": "ausdruck({formel}, {gewicht:1,grund:2})",
        "fehler_import": "",
        "fehler": "Error"
      }
    }
  },
  "rundung": {"richtung":"half-up fuer nichtnegative Betraege", "stelle":"einmal am Endpreis je Sendung", "zwischenrechnung":"exakt, ungerundet", "sammelsumme":"Summe der abgerechneten Sendungsendpreise"},
  "verbundausfall": {"beitrag":false,"verbrauch":"belegt buchen, unbekannten Verbrauch sperren"},
  "herkunft": "Verfassung Revision 02, bestaetigt durch Philipp mit drei Auflagen; maschinenlesbare Umsetzung durch Hermes vor dem Lauf"
}
````

Die Regeln liegen **nicht** im Siegelordner `verfassung-02`. Dort stehen nur `VERFASSUNG-T3.md`, `BESTAETIGUNG.md`, `ZWISCHENBERICHT.md`, `DATEIEN.txt`, `MANIFEST.sha256` und `PRUEFSUMME-ORDNER.txt` (Verzeichnisliste im Rohbeleg von `b8_einsetzen.py`).
- Kopien der Regeln: `abschluss-01` und `uebernahme-01` (Teil 4 §11).
- Änderungszeit der Regeldatei: 21.09. 05:04:33 CEST, also nach der Versiegelung von `verfassung-02` (03:42:22) und vor der ersten Einlegung (05:44:40) (R81, R93, R50).
- Das Feld `herkunft` lautet „Verfassung Revision 02, bestaetigt durch Philipp mit drei Auflagen; maschinenlesbare Umsetzung durch Hermes vor dem Lauf“.

### 5.4 Wortlaut Entwurf 01 (ersetzt durch Revision 02)
Quelle: `/root/biotop-t3/VERFASSUNG-T3-ENTWURF.md` · 2498 Bytes · SHA-256 `d048a77e9faf2e24ae1a8145510d1b8c2f2957747b519d100c14e0ed0a4e0ac0` · Schluss-Zeilenumbruch: ja

````text
# Verfassung T3 — versandwerk (Entwurf Hermes)

Status: zur Bestätigung durch Philipp oder den von ihm beauftragten Chat-Claude; keine vorweggenommene Freigabe.

1. **Zweck:** `versandwerk` ist ein TypeScript-Übungswerk ohne Betriebszweck. Es prüft fiktive Sendungsdaten, berechnet Tarife, bündelt Sendungen und erstellt Berichte; es beauftragt keinen Versand, verarbeitet keine personenbezogenen Daten und verändert keine Dateien oder externen Systeme.
2. **Sicherheit:** Eingaben sind Daten, niemals Programme. Weder `eval` noch `Function` dürfen Eingabetext ausführen; auch indirekte Zugriffe auf globale Objekte und Prototype-Manipulation durch Eingaben sind unzulässig. Ungültige Eingaben werden ausdrücklich abgewiesen.
3. **Korrektheit:** Mengen und Gewichte sind endlich und nicht negativ, Geldbeträge werden in ganzen Cent geführt, Obergrenzen sind einschließlich. Sendungen werden genau einmal berücksichtigt; negative Rabatte, negative Endpreise und still verworfene Sendungen sind unzulässig.
4. **Grenzen:** Die fünf Bereiche `eingang`, `tarife`, `planung`, `bericht` und `zahlen` verändern Eingabeobjekte nicht. `bericht` formatiert Ergebnisse, er berechnet keine Tarife nach. Grenzverträge dürfen nur zusammen mit der geprüften Anpassung beider Seiten geändert werden.
5. **Tragender Pfad:** `bericht` verwendet `planung`, `planung` verwendet `tarife` und `eingang`, `tarife` verwendet `zahlen`; für den Eichgegenstand ist das Paar `planung` → `tarife` vorrangig. `zahlen` ist der saubere Vergleichsbereich.
6. **Maß und Tausch:** Es gilt das Kernmaß aus Abschnitt 3.5 Fassung 7, Pareto je Test und Bestwertbezug; Standardtausch: Laufzeit höchstens ×2 bei Kernmaßgewinn, sonstige Grenzmaße höchstens +25 Prozent, größte Funktion nach der 60-Zeilen-Regel. Ohne Kernmaßgewinn gilt die gemessene Rauschtoleranz. Sicherheitsgewinn erhält keine zusätzliche Ausnahme.
7. **Unzulässig:** vorhandene Tests löschen, überspringen oder abschwächen; Prüfwerkzeuge, deren Konfiguration oder Referenzlast manipulieren; Befunde durch Unterdrückungs-Kommentare statt durch Codebehebung beseitigen. Neue Tests dürfen nur nach dem paarweisen Ausführungsnachweis aufgenommen werden.
8. **Betrieb:** Jeder Werk-/Testlauf bleibt in der netzlosen Kammer. Die Übungswerk-Vollmacht gilt für dokumentierte Generationenfreigaben und Mentorwahl; sie ersetzt keine Bestätigung dieser Verfassung. Der Auftrag endet an T3, nicht mit einem selbsttätigen T4-Start.
````

Kopie mit derselben SHA-256: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/VERFASSUNG-T3-ENTWURF.md`.

**Unterschied 01 → 02**, Wortlaut aus `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-02/ZWISCHENBERICHT.md` (2.243 Bytes, SHA-256 `2ca41d0a95ade8a153babea1afb25351b998c035a69bb5d7a6f9cb8348c05ac8`):
> „Die Textprüfung ergab: Genau die Sätze 3, 4 und 8 geändert; fünf von fünf übrigen Sätzen bytegleich, darin Satz 6 unverändert. Der Titel und der Bestätigungskopf wurden aktualisiert. `verfassung-entwurf-01` bleibt unverändert. Der engere Sicherheitstausch in Satz 6 ist die bestätigte Entscheidung von Hermes, keine Auslassung.“

Das Veröffentlichungsskript `/root/biotop-t3/verfassung02_veroeffentlichen.py` Z. 7–11 prüft dies mit `assert` (gelesen, nicht ausgeführt).

### 5.5 Bestätigung — Belege, zeitlich geordnet (CEST)

Nachrichten aus Philipps Konto nach `arbeit/lesen/philipp-ab-2026-09-18.md`, Meldungen von Hermes nach `arbeit/lesen/hermes-an-philipp.md`; beide geschwärzt.

1. **21.09. 02:14:40, Philipps Konto** (id 9106, Z. 371): Auftrag T3. Zur Verfassung sagt er nichts; die Suche nach „erfassung“ in dieser Nachricht ergibt 0 Treffer.
2. **21.09. 02:25:10:** Entwurf 01 auf der Platte (Änderungszeit, R81). Veröffentlicht um 02:27:58 in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/` (R93).
   - Der Statuskopf des Entwurfs lautet: „Status: zur Bestätigung durch Philipp oder den von ihm beauftragten Chat-Claude; keine vorweggenommene Freigabe.“
   - Im beiliegenden `ZWISCHENBERICHT.md` (1.831 Bytes, SHA-256 `8576ec0cefc18cc6e701d905c61994ce48583f206070adf3d6aea4da82708c9d`) steht: „Philipp hat am 21.09.2026 entschieden: Chat-Claude bestätigt die Verfassung nach Abschnitt 3.3.“ und „**Status: Entwurf, noch nicht bestätigt.** Keine stellvertretende Bestätigung durch Hermes.“
   - **Die Quelle dieser Entscheidung ist NICHT GEFUNDEN.** Die Suche nach „bestätigt die Verfassung“ und „Verfassung nach Abschnitt 3.3“ in `arbeit/verlauf/wortlaut.jsonl` ergibt 0 Treffer.
   - *Auslegung Hermes:* Mögliche Grundlage ist Masterprompt v7, 3.3, „Für Übungswerke schreibt Chat-Claude die Verfassung; Philipp hat die Entscheidung delegiert.“ Revision 02 nennt T3 in Satz 1 ein „TypeScript-Übungswerk“, die Regeln setzen `"uebungswerk": true`. Nicht belegt.
3. **21.09. 03:15:37, Hermes** (id 9547, Z. 2232): „Werk- und Adapterbau laufen weiter; die Verfassung liegt Chat-Claude vollständig im Prüfkanal vor, und der evolutionäre Lauf bleibt bis zu seiner Bestätigung gesperrt.“
4. **21.09. 03:32:41, Philipps Konto** (id 9686, Z. 374): „Die Abholadresse des Verfassungsentwurfs fehlt weiterhin — schick sie als ganze URL in eigener Zeile (laeufe/biotop-t3-typescript/verfassung-entwurf-01/, mit DATEIEN.txt und Prüfsumme). Ohne sie kann Chat-Claude nichts bestätigen, und der evolutionäre Lauf bleibt gesperrt. Bau, Eichung und Integrationsnachweis von versandwerk laufen davon unabhängig weiter.“
5. **21.09. 03:34:30, Hermes** (id 9694): nennt die vollständigen Adressen, darunter `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/VERFASSUNG-T3-ENTWURF.md`.
6. **21.09. 03:35:35, Philipps Konto** (id 9696, Z. 377), Wortlaut vollständig. Am 21.09. um 05:14:24 kam derselbe Text noch einmal (id 10252, Z. 380).
   > Verfassung bestätigt mit drei Auflagen, die vor dem Lauf einzuarbeiten und als verfassung-02 zu versiegeln sind — danach ist der evolutionäre Lauf freigegeben, ohne weitere Rückfrage. Der Entwurf ist an der entscheidenden Stelle besser als die Vorgänger: Satz 2 nennt die TypeScript-eigenen Wege (Function, globale Objekte, Prototype) statt die Python-Verfassung zu übersetzen. Auflage 1 zu Satz 4: Ergänze das Verbot geteilter Veränderung — kein Bereich verändert Object.prototype, eingebaute Prototypen oder gemeinsam genutzte Standardwerte, auch nicht innerhalb des eigenen Bereichs; Satz 2 deckt nur den Eingabeweg, und ein Bereich, der einen anderen über einen geteilten Prototyp still beeinflusst, ist genau die Nebenwirkung über Bereichsgrenzen, die Tor 4 fangen soll. Auflage 2 zu Satz 3: „Ganze Cent" legt die Einheit fest, nicht die Richtung — setz das Rundungsverfahren fest (welche Richtung, an welcher Stelle der Rechnung, und dass Zwischenergebnisse nicht mehrfach gerundet werden); ohne diese Festlegung kann jede Generation anders runden und jedes Mal „korrekt" sein, und genau daran ist der lagerhaus-Vertrag über Staffel- und Grundpreis gescheitert. Auflage 3 zu Satz 8: Nimm den Verbundausfall auf — Ablehnung, Zeitüberschreitung oder leere Antwort eines Modells zählt als Ausfall und nie als Beitrag, belegt an mindestens einem echten oder gestellten Ausfall in diesem Testwerk (Tor 4, Fassung 7). Satz 6 ohne Sicherheits-Tauschregel bleibt wie von dir gewählt — strenger als bei lagerhaus und logmuehle, konsistent begründet, das ist deine Entscheidung und sie steht.

   Wortgleich gebunden in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-02/BESTAETIGUNG.md` (1.878 Bytes, SHA-256 `ba786254cccd23f67cc358f7993e40208a8cb57fcf09b2a9abd6bd25b64a547b`). Dort steht darüber: „Die folgende Bestätigung wurde im Telegram-Auftrag vom 21.09.2026 durch Philipp übermittelt. Sie wird als vorliegende Verfassungsbestätigung mit Auflagen gebunden; kein eigener neuer Review durch Hermes wird damit behauptet.“
7. **21.09. 03:40:41:** Revision 02 auf der Platte. Versiegelt um 03:42:22 in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-02/` (R81, R93).
   - Ordnerprüfsumme `b6cd20338db3eea15cf9d6009aa02e4d50ca537626ceb87f255df79329ccce2e` über `MANIFEST.sha256`.
   - Die Abrufprobe von Hermes in `/root/biotop-t3/VERFASSUNG-02-HTTPS.json`: 6 von 6 Dateien mit HTTP 200 und bytegleich.
8. **21.09. 05:38:33, Philipps Konto** (id 10256, Z. 383; Wiederholung 05:39:09, id 10258): „Verfassung-02 ist bestätigt und versiegelt, nicht mehr anfassen — Chat-Claude hat sie geprüft, alle drei Auflagen korrekt, besonders der Schlusssatz der Rundungsregel. …“
9. **21.09. 05:44:40:** erste Einlegung in die T3-Kasse (Protokoll-Nr. 16035), `von` „Philipp“ (R50).
   - Hermes meldet um 05:44:50 (id 10435, Z. 2309): „… Verfassung-02 unverändert eingelegt …“.
   - Die Laufskripte `/root/biotop-t3/lauf30_kette.sh` bis `lauf38_kette.sh` (9 Dateien) enthalten wörtlich `biotop verfassung $L $D/VERFASSUNG-T3-02.md $D/VERFASSUNG-T3-02.regeln.json --von Philipp` (gelesen, nicht ausgeführt).
   - Für die Läufe 26–29 gibt es nur die Ausgaben `/root/biotop-t3/lauf-03-verfassung.txt` und `lauf27-03-…` bis `lauf29-03-verfassung.txt`. Ihr Inhalt ist `{"werk_id": 23, "eingelegt": true}`. Dieselbe SHA-256 tragen 14 Dateien (R41): 13 im T3-Ordner sowie `/root/phase-4-vorbedingung-1/belege/04-verfassung.stdout.txt`. Dort ist `werk_id` 23 aber Zweig VB1, also `lagerhaus-vorbedingung1-26` (§9).

**Einordnung** (Auslegung Hermes):
- Geprüft hat laut der Nachricht vom 05:38:33 Chat-Claude; übermittelt hat es Philipps Konto.
- Ob Philipp selbst inhaltlich zugestimmt hat, ist **UNBEKANNT**. Die Nachrichten aus Philipps Konto sprechen in dieser Zeit mit der Stimme Chat-Claudes. Beispiel 21.09. 02:14:40: „Es war eine nie bestätigte Vorentscheidung von mir“; laut Masterprompt v7 Änderungsverzeichnis war das eine Vorentscheidung Chat-Claudes.
- Kasse und Laufskripte führen „Philipp“ als Bestätiger. Widerspruch: Teil 3 §10, W3.
- Revision 02 ist nach dem Wortlaut der Bestätigung die bestätigte und versiegelte Fassung.
- Die konkrete Half-up-Regel in Satz 3 ist laut Statuskopf eine „Entscheidung von Hermes zur Umsetzung der Auflage 2“. Die Nachricht vom 05:38:33 hebt „besonders der Schlusssatz der Rundungsregel“ hervor.
- Die Regeldatei ist nicht Gegenstand der Bestätigung.

---

## 6. `drahtwerk` (Prüfgegenstand, kein Testwerk des Breitentests)

### 6.1 Werk
- Aus dem Kopf von `/root/biotop/tests/drahtwerk.py` (Z. 1): „Drahtwerk: kleinstes TypeScript-Werk, an dem ein ganzer Lauf jedes Organ erreicht.“
- `anlegen(ziel)` (Z. 213–233) schreibt daraus `VERFASSUNG.md` und `VERFASSUNG.regeln.json`.
- Der Verdrahtungstest `/root/biotop/tests/test_verdrahtung.py` legt die Verfassung mit `--von Verdrahtungsnachweis` in eine Test-Kasse ein (Z. 365). Die Suche in den Kassenzweigen STAMM, VB1, R02 und T3 findet keine drahtwerk-Zeile (R50).
- Der gültige Masterprompt v8 nennt `drahtwerk` nicht; die Suche ergibt 0 Treffer. *Auslegung Hermes:* Prüfgegenstand, kein Testwerk nach Abschnitt 8, Phase 4.
- git (R81, R93): Die Datei entstand in Commit `f821707` (23.09. 13:59:41) und wurde in `58bd9f9` (23.09. 17:32:34) und `0c2f058` (24.09. 20:24:54) geändert.
  - Die Konstanten `VERFASSUNG` und `REGELN` sind in allen drei Commits, im Arbeitsbaum und in beiden Prüfkanal-Kopien gleich.
  - Prüfkanal-Kopien: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/drahtwerk.py` und `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-03/drahtwerk.py`.
  - Die Bauskripte der Runde 6 (`/root/biotop-vor-t4-06/bau/r6_s4_drahtwerk*.py`) enthalten keine eigene Verfassung.
- Stand der Datei beim Lesen: 16.319 Bytes, SHA-256 `0b1246a89113087ae2cb237e31f91449da19589054677d65159084b133b73777` (R81). Der Baum wird von S1c bearbeitet; der Endstand folgt durch Hermes.

### 6.2 Wortlaut (Text, wie `anlegen()` ihn schreibt)
Quelle: Konstante `VERFASSUNG` in `/root/biotop/tests/drahtwerk.py` Z. 139–146 (per `ast` gelesen), so wie `anlegen()` sie als `VERFASSUNG.md` schreibt · 520 Bytes · SHA-256 `13677832e59fcfef89fce35eed4ca0124de5fe595425714f002c5b44fdd576ec` · Schluss-Zeilenumbruch: ja

````text
# Verfassung drahtwerk (Prüfwerk ohne Betriebszweck)

1. **Zweck:** Das Werk summiert Zahlenlisten; es dient nur dem Verdrahtungsnachweis des Biotops.
2. **Sicherheit:** Eingaben sind Daten; kein Code wird aus Eingaben ausgeführt.
3. **Korrektheit:** `summen` erhöht jeden Wert um genau eins; `gesamt` addiert über `plus`; `halb` halbiert exakt.
4. **Grenzen:** `alpha` verwendet `beta`; der Grenzvertrag steht in tests/vertraege.
5. **Tragender Pfad:** `alpha` → `beta`. `beta` ist der saubere Vergleichsbereich.
````

### 6.3 Wortlaut (Regeln, wie `anlegen()` sie schreibt: `json.dumps(REGELN, ensure_ascii=False, indent=1)`, Z. 229)
Quelle: Konstante `REGELN` in `/root/biotop/tests/drahtwerk.py` Z. 148–151 (per `ast` gelesen), so wie `anlegen()` sie als `VERFASSUNG.regeln.json` schreibt: `json.dumps(REGELN, ensure_ascii=False, indent=1)` · 340 Bytes · SHA-256 `1bb6f77ccf4da46a85ad171b183d03113a25cc237c799638d90de31524bb963d` · Schluss-Zeilenumbruch: nein

````json
{
 "uebungswerk": true,
 "sprache": "TypeScript",
 "tragender_pfad": [
  [
   "alpha",
   "beta"
  ]
 ],
 "tausch": {
  "laufzeit_faktor": 2.0,
  "laufzeit_faktor_bei_sicherheitsgewinn": 2.0,
  "sonst_faktor": 1.25,
  "groesste_funktion_absolut": 60
 },
 "verbotene_muster": [
  ".skip(",
  ".todo(",
  "eslint-disable",
  "@ts-ignore"
 ]
}
````

### 6.4 Ältere Variante, nur in `/tmp`
Quelle: `/tmp/drahtwerk-probe/VERFASSUNG.md` · 489 Bytes · SHA-256 `4630f6e3d6661d3576d720350989feb4e28909eb9e4f9c87233ca8cb4ef46ba4` · Schluss-Zeilenumbruch: ja

````text
# Verfassung drahtwerk (Prüfwerk ohne Betriebszweck)

1. **Zweck:** Das Werk summiert Zahlenlisten; es dient nur dem Verdrahtungsnachweis des Biotops.
2. **Sicherheit:** Eingaben sind Daten; kein Code wird aus Eingaben ausgeführt.
3. **Korrektheit:** `summen` erhöht jeden Wert um genau eins; `halb` halbiert exakt.
4. **Grenzen:** `alpha` verwendet `beta`; der Grenzvertrag steht in tests/vertraege.
5. **Tragender Pfad:** `alpha` → `beta`. `beta` ist der saubere Vergleichsbereich.
````

- Unterschied zu §6.2: In Satz 3 fehlt „`gesamt` addiert über `plus`;“.
- Nicht in git: Schon der erste Commit `f821707` trägt die Fassung aus §6.2 (R81). Änderungszeit 23.09. 11:18:04 (Rohbeleg von `b8_einsetzen.py`); die Regeldatei daneben ist gleich mit §6.3.
- *Auslegung Hermes:* Zwischenstand vor dem ersten Commit, von einer Probe in `/tmp` zurückgelassen.

### 6.5 Bestätigung
- **Nie bestätigt.** Eine Bestätigung ist nicht belegt:
  - Suche nach „drahtwerk“ zusammen mit „Verfassung“ in `arbeit/lesen/*`: 0 Treffer;
  - in keinem Kassenzweig eine Zeile;
  - im Testcode nur `--von Verdrahtungsnachweis`.
- Die Regeln setzen `"uebungswerk": true`. Damit gilt im Test die Übungswerk-Vollmacht für Freigaben (Teil 1 §2, Befund 2).

### 6.6 Keine Verfassungen: Testattrappen
Tests im Biotop-Baum legen kurze Verfassungstexte in temporäre Kassen ein (R93, per `ast` gelesen, nicht ausgeführt). Sie gehören zu keinem Werk. Aufgeführt sind sie, damit nichts fehlt:
- `test_t3_befundklasse.py:18`: Text `'2. Keine Eingabeausführung'`, von `'Hermes'`.
- `test_t3_eichpfad.py:20`: liest `/root/biotop-t3/VERFASSUNG-T3-02.md` (§5.2) mit eigenen Regeln `{'uebungswerk': True, 'tragender_pfad': [['planung','tarife']]}`, von `'bestätigter Prüfgegenstand'`.
- `test_tor4_zeilen.py:511`: Text ``'Das Werk rechnet.\n`beta` ist der saubere Vergleichsbereich.\n'``, von `'test'`.
- `test_vor_t4_04.py:266` und `test_vor_t4_05.py:308`: `VERFASSUNG = {'text': '1. Zweck: Prüfwerk ohne Betriebszweck.\n2. Sicherheit: Eingaben sind Daten.\n', 'regeln': {}}`.
- `test_vorspann.py:55`: Text `'alpha nutzt beta; Satz 2: Messgerät bleibt fest.'`, von `'Eigen-Test'`.

---

## 7. Handelssystem (am 21.09. als Phase-4-Werk gestrichen)

- **Verfassung: NICHT GEFUNDEN, nie geschrieben.**
  - Keine Datei trägt „andelssystem“ im Namen (Dateinamensuche mit `search_files` unter `/root`: 0 Treffer).
  - Die Kassen enthalten keinen Verfassungstext außer den Dateien aus §3–§6 (R50: 0 unbekannte Texte).
  - Die 10 Dateien im Prüfkanal mit „Orderpfad“ sind nach ihren Namen Übergaben (3), Review-Aufträge (2), Zwischenberichte (2), Auftragsregeln (1) und Masterprompt-Kopien (2). Keine davon ist eine Verfassung. Gelesen wurde davon nur Abschnitt (f) der Übergabe `abschluss-01`.
- **Soll-Wortlaut Masterprompt v6**, Phase 4, Vorbedingung 2 (Dokumentkopie `2026-09-20_001844_…-v6.md` Z. 394): „2. **Verfassung des Werks** — schreibt Philipp, Hermes legt einen Entwurf vor. Sie enthält mindestens: gesetzliche Hebelgrenzen je Anlageklasse, Tagesverlustgrenze, Ausschluss schädlicher Geschäftsfelder (Rüstung ausdrücklich), kein echter Handel ohne bestandenes Bewertungssystem, Demokonto zuerst, und den **tragenden Pfad** für den Eichgegenstand (3.5: der Orderpfad mit Risikomodulen und Verlustgrenze) — ohne diesen Eintrag wartet das Organ und der Lauf beginnt nicht.“
- **Stand bis zur Streichung:**
  - Hermes am 20.09. 01:31:11 (id 2841, Z. 834): „Nächster Schritt wäre Vorbedingung 2: Verfassung des Handelssystems — die schreibt Philipp, ich lege einen Entwurf vor, der den tragenden Pfad für den Eichgegenstand benennen muss.“
  - Übergabe `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-01/UEBERGABE-PHASE-4.md` (32.268 Bytes, SHA-256 `00a46e857745088b0ccb5dbebe1ca74885e04622ba7992f4eab73dcfd0666b6f`), Abschnitt (f): eine Anforderungsliste, keine Verfassung.
  - Philipps Konto am 21.09. 01:19:00 und 01:56:17 (Z. 362, 365): „Der nächste fachliche Schritt ist Vorbedingung 2, die Verfassung des Handelssystems, die Philipp schreibt …“
- **Gestrichen:**
  - Philipps Konto am 21.09. 02:14:40 (id 9106, Z. 371): „Das Handelssystem ist als Phase-4-Werk gestrichen: Es war eine nie bestätigte Vorentscheidung von mir, und alle Bezugsgrößen daraus (…) sind ungültig.“
  - Masterprompt v7, Änderungsverzeichnis (Z. 7): „Das Handelssystem stand in den Fassungen 1 bis 6 als Phase-4-Werk, war aber eine nie bestätigte Vorentscheidung von Chat-Claude; alle darauf bezogenen Bezugsgrößen (…) sind gestrichen.“
  - Die ausgelassenen Zahlen stehen in `ENTSCHEIDUNGEN` (FK17).

---

## 8. T4, T5, T6

- **NICHT GEFUNDEN, noch nicht gebaut** (Stand des Lesens, R81):
  - Auf der obersten Ebene von `/root` tragen nur die sechs Ordner der Behebungsrunden `biotop-vor-t4` … `biotop-vor-t4-06` „t4“ im Namen; keiner trägt „t5“ oder „t6“.
  - `/root/biotop/daten/werke/` enthält kein T4-, T5- oder T6-Werk.
  - In der T3-Kasse ist `werk_id` 23 das letzte Werk (R50).
  - Im Prüfkanal gibt es nur die Ordner `biotop-vor-t4*`.
- Masterprompt v8, Phase 4: „**Vorbedingungen für T4 (Reihenfolge, je mit Gegenprobe durch den Laufweg):** …“ (Z. 463). Das sind Vorbedingungen der Behebungsrunden, kein gebautes Werk.
- Übergabe Runde 6, `/root/biotop-vor-t4-06/UEBERGABE.md`:
  - Z. 21–22: „**Startregel T4 (vorab gesetzt):** T4 beginnt, sobald das Review dieser Runde keinen stillen Durchlass mehr findet — jede bekannte Lücke muss eine gezählte Enthaltung sein; Lücken, die sich nur enthalten, behebt T4 im Lauf.“
  - Z. 66: „… Messskript für die Aufnahme von T4 vorbereiten, nicht messen (kein T4-Werk) …“.
- Wer die Verfassung eines Testwerks schreibt und bestätigt, regelt der Masterprompt nicht (Teil 1 §2, Befund 7; Frage F1 in Teil 3 §10).

---
