# Auftrag BIOTOP-EINLAGERUNG-01 — Biotop anhalten, vollständig sichern, abholbereit machen, Wiedereinstieg vorbereiten

**Für:** Hermes auf HERMES-1 · **Von:** Chat-Claude im Auftrag von Philipp · **Entscheider:** Philipp · **Erstellt:** 25.09.2026

**Grundlage:** BIOTOP-LAGE-01, abgeschlossen mit START-03 (25.09.2026 21:09:29 CEST). Was dort erhoben ist, übernimmst du. Du erhebst es nicht neu.

**Verhältnis zum Masterprompt:** Fassung 8 bleibt gültig und unverändert. Dieser Auftrag setzt die Arbeit am Biotop aus. Er baut nichts und entscheidet nichts über den Inhalt des Biotops.

**Kennungen dieses Auftrags:** Rohbelege heißen EB1, EB2 … Sie sind nicht zu verwechseln mit den R-Nummern aus BIOTOP-LAGE-01 oder mit Kennungen des Biotops (S1, T3, F2, M2(b), R6-1, v8). P1–P20 und C1–C11 sind die Fragen aus BIOTOP-LAGE-01 (LAGE-TEIL1, FK47). „Abschnitt n" meint immer diesen Auftrag.

Lies den ganzen Auftrag, bevor du anfängst.

---

## 0. Entscheidung Philipps und Ziel

Philipp, 25.09.2026, wörtlich:
> „ich möchte das Projekt zunächst anhalten alles absichern und vorbereiten damit ich das gesamte Projekt inklusive Dokumentation später vom Server herunterladen. ich werde das Projekt später wieder voll aufnehmen möchte es aber jetzt anhalten und absichern abschliesen damit ich jetzt lagern kann und später perfekt wieder einsteigen kann"

Zur Ablage außerhalb des Servers: „Ich hole es auf meinen Laptop".

Vier Ziele:
1. **Stillstand.** Am Biotop läuft nichts mehr, und nichts wird weitergebaut, bis Philipp die Wiederaufnahme ausdrücklich beauftragt. Kein Mechanismus darf die Arbeit von selbst wieder aufnehmen: kein Wecker, kein Zeitgeber, kein Subagent und keine Arbeitsregel.
2. **Vollständig gesichert.** Ein Paket enthält alles, was zum Biotop gehört: Code mit der ganzen Geschichte, alle Daten und Datenbanken, alle Werke, alle Belege und die ganze Dokumentation. Es ist nachweislich wiederherstellbar, und der wiederhergestellte Stand ist nachweislich lauffähig.
3. **Abholbereit.** Philipp lädt das Paket per `scp` auf seinen Laptop und prüft es dort mit einer einzigen Prüfzeile.
4. **Wiedereinstieg.** Ein Dokument erlaubt einem Leser ohne Vorwissen, den Stand zu verstehen und die Arbeit genau dort fortzusetzen, wo sie ruht. Dieser Leser kann Philipp sein, Chat-Claude oder ein frischer Hermes.

## 1. Entscheidungen, die mit diesem Auftrag gelten

- **P1 — Verdichtungen:** Sie zählen nicht gegen das Budget von 0,00 €. Sie sind Betriebskosten und werden getrennt ausgewiesen. *Vorentscheidung Chat-Claude; gilt mit dem Absenden durch Philipp.*
- **P2 — Datei mit Philipps Telegram-Kennung** (`laeufe/biotop-lage-01/zwischenbericht-20260925-163807-r114/ZWISCHENBERICHT.md`):
  - Du legst im selben Ordner eine geschwärzte Kopie an: `ZWISCHENBERICHT-GESCHWAERZT-01.md`, die Kennung ersetzt durch `[GESCHWÄRZT]`.
  - Das Original verschiebst du aus dem Prüfkanal nach `/root/biotop-einlagerung/entfernt-aus-pruefkanal/`.
  - Damit ist die Entfernung aus dem Prüfkanal ausdrücklich erlaubt. Gelöscht wird nichts.
  - *Vorentscheidung Chat-Claude; gilt mit dem Absenden durch Philipp.*
- **P3 — Runde 6:** Sie wird nicht fortgesetzt; das Biotop wird im jetzigen Stand eingelagert. Wie Runde 6 und die Startregel für T4 weitergehen, entscheidet Philipp bei der Wiederaufnahme. *Entscheidung Philipp.*
- **P4 — Ablage 2:** Philipps Laptop, per `scp`. *Entscheidung Philipp.*
- **C5 — beantwortet von Chat-Claude:** Es gelten v8 Z. 131 (Grundsatz 14) und Z. 464 (Vorbedingung 1 für T4). Die Laufzeit wird also gepaart in derselben Sitzung gemessen, mit dem Median mehrerer Messungen je Seite, und nie gegen ein historisches Minimum. Z. 176 ist älterer Wortlaut und wird in Fassung 9 angeglichen.
- **Alle übrigen Fragen** bleiben offen und gehören in den Wiedereinstieg (Abschnitt 5, Punkt 4). Das sind P5–P20 sowie C1–C4 und C6–C11.

**Vorentscheidungen von Chat-Claude zu diesem Auftrag.** Philipp hat sie nicht einzeln bestätigt und kann jede streichen:
- Der nicht eingecheckte Stand der Runde 6 wird auf einem eigenen Zweig festgeschrieben. Der bisherige Stand bleibt auf `0c2f058` (Schritt 2).
- Die Docker-Abbilder der Kammer kommen mit `docker save` ins Paket.
- Im wiederhergestellten Stand läuft die Regression mit Kammer. Container, Kopien und Arbeitsordner dieser Probe entfernst du danach wieder.
- Es gibt zwei Archive: ein vollständiges und ein kleines, das nur die Dokumentation enthält.

## 2. Harte Regeln

1. **Nicht weiterbauen, nicht reparieren.** Am Biotop änderst du nichts: nicht Code, Tests, Messgerät, Verfassungen, Werke, Kasse oder Gedächtnisse. Erlaubt sind nur:
   - der Sicherungscommit auf dem eigenen Zweig (Schritt 2);
   - die Stillstandsvermerke (Schritt 1);
   - alles unter `/root/biotop-einlagerung/`;
   - der Abschlussordner;
   - die Gedächtnisdateien;
   - P2.
2. **Nichts löschen, nichts überschreiben.** Es gibt zwei Ausnahmen:
   - die Verschiebung aus P2;
   - Container, Kopien und Arbeitsordner, die du selbst für die Probe anlegst. Die entfernst du am Ende und belegst es.
3. **Keine Biotop-Läufe, keine bezahlten Modellaufrufe.** Die Regression der Probe ruft kein Modell, wie die Regressionen der Behebungsrunden. Ist das für einen Test unklar, wählst du ihn ab und führst ihn auf. Verdichtungen: siehe P1.
4. **Kein Geheimnis und keine Kundendaten in den Prüfkanal oder in eine Meldung.**
   - Geheimnisdateien kommen nicht in die Archive: `.env`, `auth.json`, Schlüsseldateien, `/root/w7/07-codex-token.txt` und gleichartige Dateien.
   - Die Wiederherstellungsanleitung nennt von ihnen nur Namen und Zielpfad.
   - Die Archive liegen nie im Prüfkanal.
5. **Nachweis am Ergebnis.**
   - „Ausgeführt" schreibst du nur mit Rohbeleg: EB-Nummer, Befehl und vollständige Ausgabe. Ohne Rohbeleg heißt es „gelesen, nicht ausgeführt".
   - Jede Zahl trägt Bezugsgröße und Quelle und ist als abgelesen oder gerechnet gekennzeichnet.
   - Laut scheitern: `NICHT GEFUNDEN`, `NICHT AUSGEFÜHRT` oder `UNBEKANNT`, nie weglassen.
   - Auslegungen, Entscheidungen und Vorschläge kennzeichnest du als „Auslegung Hermes", „Entscheidung Hermes" und „Vorschlag Hermes".
   - Wortlaut vor Zusammenfassung.
6. **Ablieferung wie in BIOTOP-LAGE-01:**
   - nummerierte Dateien, die nie überschrieben werden;
   - jede Adresse vollständig und wörtlich ausgeschrieben;
   - höchstens 40 KB je Datei;
   - vor jeder Veröffentlichung eine Geheimnissuche mit Gegenprobe;
   - eine Abrufprobe über jede Adresse.
7. **Weiterarbeiten statt anhalten**, bis dieser Auftrag abgeschlossen ist.
   - Dafür nutzt du denselben Weiterlauf wie in BIOTOP-LAGE-01, mit Zwischenständen als neue Einstiegsdateien.
   - Der einzige Grund anzuhalten: Das Biotop ist nicht in dem Stand, den BIOTOP-LAGE-01 beschreibt.
   - Nach Meldung 2 besteht kein Weiterlauf-Mechanismus mehr, der das Biotop betrifft.
8. **Nicht Gegenstand** ist deine eigene Modell- und Anmeldelage.
9. Alle Zeitangaben tragen Datum, Uhrzeit und Zeitzone.

## 3. Schritte

**Schritt 1 — Stillstand herstellen, Ordner anlegen, melden**
- **Stillstand prüfen, mit Rohbeleg:**
  - Läuft etwas mit Biotop-Bezug? Geprüft werden Prozesse, Container, Subagenten, Wecker, Zeitgeber und Cron-Jobs.
  - Läuft doch etwas, hältst du es an (Philipps Entscheidung P3) und belegst es.
- **Stillstandsvermerk:** eine neue Zeile in `/root/.hermes/memories/MEMORY.md`, dieselbe später in `laeufe/gedaechtnis/STAND-03.md`. Wortlaut:
  > „Biotop eingelagert am <Datum> (BIOTOP-EINLAGERUNG-01). Keine Arbeit am Biotop, keine Subagenten und keine Wecker dafür, bis Philipp ausdrücklich die Wiederaufnahme beauftragt. Einstieg: WIEDEREINSTIEG im Abschlussordner laeufe/biotop-einlagerung-01/."
- **Zwischenbericht-Wächter:** Du stellst `auftrag.json` für die Dauer dieses Auftrags auf diesen Auftrag um. Die alte Fassung sicherst du vorher.
- **Abschlussordner:** `laeufe/biotop-einlagerung-01/` im Prüfkanal anlegen, darin sofort `START-01.md` mit Kennung, Beginn, Status `IN ARBEIT` und dem Plan in fünf Zeilen. Danach Meldung 1 (Abschnitt 7).
- **Arbeitsordner**, nicht öffentlich: `/root/biotop-einlagerung/`.

**Schritt 2 — Git festschreiben**
- **Jedes Git-Repository mit Biotop-Bezug:** HEAD, Zweige, Markierungen und `git status` festhalten (EB). Dazu gehört mindestens `/root/biotop`; die weiteren entnimmst du der Fundstellenliste aus BIOTOP-LAGE-01 (AUFBAU FK38, INVENTAR I4 und I5).
- **In `/root/biotop`:**
  1. Markierung `runde-5` auf `0c2f058` setzen, falls es sie noch nicht gibt.
  2. Neuen Zweig `einlagerung/runde-6-stand` ab `0c2f058` anlegen.
  3. Vor dem Commit eine Geheimnissuche über die 25 nicht eingecheckten Einträge; kein Geheimnis darf in den Commit.
  4. Auf dem neuen Zweig ein Commit mit genau diesen 25 Einträgen. Nachricht:
     > „Einlagerung: Stand Runde 6 unfertig — S1c Teile A–F gebaut, Befund G nur als rote Spezifikation (10 rote test_w_g_*), kein Review, kein Bericht. Nicht abgenommen."
  5. Markierung `eingelagert-<JJJJMMTT>` auf diesen Commit.
  6. Der neue Zweig bleibt ausgecheckt. Der Zweig, auf dem `0c2f058` liegt, bleibt unverändert.
  7. **Beleg:** Der Arbeitsbaum ist nach dem Commit unverändert. Dafür bildest du eine Prüfsummenliste ohne `.git/` vor und nach dem Commit: gleiche Anzahl, Unterschied leer. Bezugsgröße ist die Liste VORHER aus BIOTOP-LAGE-01 (R156, 3.153 Dateien).
- **Weitere Repositorys** mit nicht eingecheckten Änderungen: dasselbe Verfahren, jeweils ein eigener Zweig, kein Eingriff in den bestehenden Zweig.

**Schritt 3 — Vergängliches dauerhaft machen**

Du kopierst, statt zu verschieben, und vergleichst jede Datei per Prüfsumme.
- **Biotop-Belege in `/tmp`** kopierst du nach `/root/biotop-einlagerung/tmp-belege/`. Mindestens `/tmp/review-vor-t4-04/`, `/tmp/review-vor-t4-05/`, `/tmp/r6-*` und `/tmp/h-r6`. Grund: `/tmp` wird beim Neustart geleert (LAGE-TEIL6, FK43 Nr. 4).
- **Biotop-Einträge aus Hermes' Zwischenspeichern** kopierst du nach `/root/biotop-einlagerung/hermes-zwischenspeicher/`. Das sind die Delegationsprotokolle (`/root/.hermes/cache/delegation/`) und die eingelegten Dokumente (`/root/.hermes/cache/documents/`).
- **Arbeitsdokumente der Runde 6**, bisher unveröffentlicht, veröffentlichst du zusätzlich geschwärzt im Abschlussordner:
  - `/root/biotop-vor-t4-06/UEBERGABE.md`
  - `BAU-S1C-UNBEOBACHTET.md`
  - `bau/S1C-PLAN.md`
  - den Schlussbericht von S1c
  - die Spezifikationen der Runde

**Schritt 4 — Dokumentation zusammenstellen** (Ordner `/root/biotop-einlagerung/paket/dokumentation/`)
- **`WIEDEREINSTIEG`** nach Abschnitt 5. Du schreibst ihn selbst. Hilfsagenten dürfen zuarbeiten, aber jede Zahl prüfst du gegen BIOTOP-LAGE-01 oder einen Rohbeleg.
- **`INHALT`:** ein Verzeichnis beider Archive. Jeder Eintrag der obersten zwei Ebenen steht mit Zweck, Größe und Anzahl der Dateien da.
- **Masterprompt und Verfassungen:** Fassungen v1 bis v8 im Wortlaut mit ihren Änderungsverzeichnissen, dazu alle Verfassungen im Wortlaut.
- **Prüfkanal:** Kopien aller Biotop-Ordner (`laeufe/biotop-*` und `laeufe/gedaechtnis/`), einschließlich BIOTOP-LAGE-01 mit Rohbelegen.
- **Verlauf:** der Verlauf Philipp ↔ Hermes zum Biotop seit dem 18.09. im Wortlaut. Geheimnisse sind geschwärzt, Inhalte anderer Vorhaben bleiben draußen.
- **Umgebung:**
  - Betriebssystem, Python- und Node-Versionen;
  - `pip freeze` je Umgebung und die Sperrdateien;
  - die Docker-Abbilder der Kammer mit Kennung und Bauweg;
  - die Version von Hermes Agent und die Liste der Skills.
- **Gedächtnis:** Beide Dateien kommen auch nach `laeufe/gedaechtnis/`.
  - `REGELN-02.md` enthält die geltenden Regeln: v8, die Arbeitsregel vom 23.09., die stehenden Arbeitsregeln aus ENTSCHEIDUNGEN FK18 und die Entscheidungen dieses Auftrags.
  - `STAND-03.md` enthält Einlagerung, Stillstandsvermerk und den Verweis auf WIEDEREINSTIEG.
- **Geheimnissuche mit Gegenprobe** über den ganzen Ordner `dokumentation/`. Er muss geheimnisfrei sein, weil Philipp ihn auch auf dem Tablet öffnet.

**Schritt 5 — Packen**
- **Archiv KOMPLETT:** `biotop-einlagerung-<JJJJMMTT>-komplett.tar.gz`. Es enthält:
  - `/root/biotop` samt `.git/`, mit dem neuen Zweig und den Markierungen;
  - jeden weiteren Ort mit Biotop-Bezug nach der Fundstellenliste. Mindestens `/root/biotop-t3`, `/root/biotop-vor-t4` bis `/root/biotop-vor-t4-06`, `/root/phase-4-vorbedingung-1`, `/root/reparatur-01`, `/root/reparatur-02`, `/root/uebungswerk*`, `/root/versandwerk-t3`, `/root/versandwerk-t3-02` und `/root/sicherung/biotop-lage-01`, dieses ohne das alte Archiv;
  - alle Datenbanken, gesichert über die Backup-API und je mit `integrity_check`; die Kopien liegen am selben Pfad wie das Original;
  - `/root/.hermes/` ohne Geheimnisdateien;
  - `tmp-belege/`, `hermes-zwischenspeicher/` und `dokumentation/`;
  - die Docker-Abbilder der Kammer (`docker save`). Sind sie größer als 3 GB, kommen sie als eigene Datei mit eigener Prüfsumme neben KOMPLETT;
  - ein Manifest mit der SHA-256 jeder Datei.
  - Draußen bleiben Abhängigkeitsordner (`node_modules`, `.venv`, `venv`, Zwischenspeicher). Die Sperrdateien kommen mit.
- **Archiv DOKUMENTATION:** `biotop-einlagerung-<JJJJMMTT>-dokumentation.tar.gz`, nur `dokumentation/`, mit eigenem Manifest.
- **`SHA256SUMS-<JJJJMMTT>.txt`:** Name, Bytes und SHA-256 jedes Archivs.
- **Abgleich mit der Fundstellenliste:** Jede Fundstelle aus BIOTOP-LAGE-01 ist im Paket oder mit Grund ausgelassen; du gibst das als x von y an.
- **Ablage:** `/root/biotop-einlagerung/archiv/`, Rechte 600, nie im Prüfkanal. Das alte Archiv aus BIOTOP-LAGE-01 bleibt unverändert liegen.

**Schritt 6 — Wiederherstellen und laufen lassen (Probe)**
1. **Vorher:** Prüfsummenliste von `/root/biotop` und allen Biotop-Datenbanken. Nach der Probe muss sie gleich sein; die Probe darf das Original nicht berühren.
2. **Entpacken:** KOMPLETT in ein leeres Verzeichnis unter `/root/biotop-einlagerung/probe/`. Das Manifest wird gegen den entpackten Stand verglichen: Anzahl beider Seiten angeben, Unterschied leer.
3. **Gegenprobe:** In einer Kopie genau ein Byte ändern. Der Vergleich muss genau diese Datei melden.
4. **Datenbanken:** `integrity_check` jeder entpackten Datenbank ergibt `ok`.
5. **Git:** Im entpackten Repository stehen `runde-5`, `eingelagert-<JJJJMMTT>` und der Zweig `einlagerung/runde-6-stand`, und `git status` ist sauber.
6. **Regression mit Kammer** im entpackten Stand. Du nutzt denselben Befehl wie die Regression der Runde 5 (`biotop-vor-t4-05/REGRESSION.txt`) und lädst die Kammer-Abbilder aus dem Archiv.
   - **Maßstab, vorab gesetzt:** Rot sein dürfen nur die 10 roten Proben `test_w_g_*` (Befund G).
   - Jeden weiteren roten Test führst du einzeln auf und wiederholst ihn in einer zweiten Arbeitskopie, die du direkt aus `/root/biotop` kopierst.
     - Ist er dort auch rot, ist er ein Befund des Stands, kein Fehler der Wiederherstellung.
     - Ist er nur im entpackten Stand rot, ist die Wiederherstellung nicht lauffähig. Das meldest du laut.
   - Die Regression ruft kein Modell. Dauer und Ergebnis kommen als Rohbeleg dazu.
   - Stößt die Probe auf absolute Pfade, die ins Original zeigen, brichst du sie ab und meldest es als Befund für den Wiedereinstieg.
7. **Nachher:**
   - Die Prüfsummenliste aus Punkt 1 erneut bilden; der Unterschied muss leer sein.
   - Probeordner, Kopien und Container entfernen und das belegen.

**Schritt 7 — Abholung vorbereiten**

Du schreibst `ABHOLANLEITUNG` fertig ausgefüllt für die Windows-PowerShell auf Philipps Laptop. Sie kommt in den Abschlussordner und nach `dokumentation/`. Außen stehen einfache Anführungszeichen, weil die PowerShell verschachtelte Anführungszeichen verschluckt.
1. **Zielordner anlegen:** `New-Item -ItemType Directory -Force 'C:\Biotop-Lager' | Out-Null`
2. **Herunterladen:** je Archiv und für `SHA256SUMS` ein `scp`-Befehl mit der aktuellen Serveradresse und dem vollständigen Pfad. Dazu je eine Ausweichzeile über den Domainnamen, falls die geliehene IP-Adresse gewechselt hat.
3. **Prüfen:** je Archiv die Prüfzeile `(Get-FileHash '<Pfad>' -Algorithm SHA256).Hash -eq '<SHA-256>'`. Sie muss `True` ausgeben.
4. **Größe und Dauer:** Größe je Archiv und geschätzte Dauer, als Schätzung gekennzeichnet.
5. **Bei Abbruch:** den Befehl wiederholen; die Prüfzeile entscheidet.
6. **Hinweis zur Lagerung:** KOMPLETT enthält die Sitzungsdatenbank und damit womöglich eingefügte Geheimnisse. Es gehört auf einen verschlüsselten Datenträger.

**Schritt 8 — Abschließen**
- **P2 umsetzen.** Abrufprobe: Die alte Adresse liefert 404, die geschwärzte Kopie 200.
- **Gedächtnis:** `STAND-03.md` und `REGELN-02.md` in `laeufe/gedaechtnis/`, mit neuen Manifesten.
- **Wächter vom Biotop lösen:** `auftrag.json` sichern und so setzen, dass kein Zwischenbericht mehr in einen Biotop-Ordner geht. Mit Beleg.
- **Letzte Stillstandsprüfung** wie in Schritt 1, nach allem anderen. Ergebnis: 0 Prozesse, 0 Container, 0 Subagenten, 0 Wecker und 0 Zeitgeber mit Biotop-Bezug.
- **Abschlussordner fertigstellen**, in dieser Reihenfolge: Geheimnissuche, Einstiegsdatei, `DATEIEN`, `PRUEFSUMME-ORDNER`, Abrufprobe, Meldung 2.

**Nach der Abholung:** Schickt dir Philipp „Abgeholt, Prüfsumme gleich" oder die Ausgabe der Prüfzeile, legst du `laeufe/gedaechtnis/STAND-04.md` an. Inhalt: Laptop-Kopie vorhanden, Datum, SHA-256. Mehr tust du dann nicht.

## 4. Abschlussordner `laeufe/biotop-einlagerung-01/`

| Datei | Inhalt |
|---|---|
| `START-NN.md` | Kennung, Status (`EINGELAGERT` / `TEILWEISE` / `ABGEBROCHEN`), Lage in fünf Sätzen, was vom Maßstab (Abschnitt 6) nicht erfüllt ist, Lesereihenfolge, jede Datei mit vollständiger Adresse, Bytes und SHA-256 |
| `WIEDEREINSTIEG-NN.md` | Abschnitt 5, bei Bedarf in Teilen |
| `ABHOLANLEITUNG-NN.md` | Schritt 7 |
| `SHA256SUMS-NN.txt` | Name, Bytes und SHA-256 jedes Archivs |
| `EINLAGERUNG-BERICHT-NN.md` | Schritte 1–8 mit Belegen: Stillstand, Git, Vergängliches, Vollständigkeit, Paket, Probe, Regression, P2, Wächter, Kosten |
| `INHALT-NN.md` | Verzeichnis beider Archive |
| `RUNDE6-DOKUMENTE-NN/…` | geschwärzte Arbeitsdokumente der Runde 6 (Schritt 3) |
| `ROHBELEGE-NN.txt` · `DATEIEN-NN.txt` · `PRUEFSUMME-ORDNER-NN.txt` · `ABRUFPROBE-NN.txt` | wie in BIOTOP-LAGE-01 |

## 5. WIEDEREINSTIEG — Pflichtinhalt

Du schreibst ihn für einen Leser, der nur diese Datei hat. Jede Zahl trägt ihre Quelle.

1. **Was das Biotop ist:**
   - das Zielbild im Wortlaut (v8, Abschnitt 0);
   - die Verfassungssätze;
   - die Rollen: Hermes führt aus, Chat-Claude prüft, Philipp entscheidet.
2. **Stand bei der Einlagerung:**
   - Phase, Werke und das Ergebnis von T3;
   - die Behebungsrunden 1–6 mit Status;
   - Runde 6 im Einzelnen: S1–S4, S1b, S1c mit den Teilen A–F, Befund G;
   - Zweig, Commit und Markierungen;
   - Kasse und Kosten;
   - die roten Tests, je mit Grund.
3. **Was gilt:**
   - Masterprompt v8, mit Pfad im Paket;
   - die Startregel für T4 im Wortlaut (id 16901);
   - REGELN-02;
   - das Entscheidungsregister, mit Pfad.
4. **Offene Entscheidungen, als Erstes bei der Wiederaufnahme:**
   - **Runde 6 und die Startregel für T4.** Dazu steht, gekennzeichnet als Vorschlag Chat-Claude:
     > „G schließen oder als gezählte Enthaltung führen, danach ein Review. Findet es wieder einen stillen Durchlass, wird er gezählte Enthaltung, und T4 startet ohne Runde 7. Begründung: sechs Runden statt einer, und jede fand eine neue Klasse. Neue Blindstellen zu finden ist die Aufgabe des Breitentests."
   - **Fragen aus BIOTOP-LAGE-01:** P5–P20 an Philipp sowie C1–C4 und C6–C11 an Chat-Claude, im Wortlaut mit Quelle.
   - **Kandidaten für Fassung 9:** N-1 bis N-12 und die Fassung-9-Lücken der Lückenliste.
5. **Offene Lücken:**
   - der Verweis auf die Lückenliste (86 offen);
   - darunter die zehn Lücken, die den nächsten Schritt am stärksten berühren, je mit Grund.
6. **Wiederaufnahme, Weg A — derselbe Server.** Die Schritte in Reihenfolge, mit Befehlen:
   1. Den Stillstandsvermerk nur auf Philipps Auftrag aufheben.
   2. Die Prüfsummen gegen das Einlagerungsmanifest vergleichen.
   3. Die Regression mit Kammer laufen lassen.
   4. Dann folgt der erste Auftrag nach Punkt 8.
7. **Wiederaufnahme, Weg B — neuer Server aus dem Laptop-Paket.** Von einem leeren Ubuntu 24.04 bis zum lauffähigen Biotop:
   - das Archiv vom Laptop hochladen (`scp`) und entpacken;
   - Abhängigkeiten einrichten und die Docker-Abbilder laden;
   - die Geheimnisse von Hand eintragen, hier nur mit Name und Zielpfad genannt;
   - Hermes Agent in der gesicherten Version einrichten;
   - den Prüfkanal einrichten (optional);
   - Nachweis durch Manifestvergleich und Regression.
   - Was du davon in Schritt 6 ausgeführt hast, trägt einen Rohbeleg. Der Rest heißt „gelesen, nicht ausgeführt".
8. **Erster Auftrag nach dem Wiedereinstieg** (Vorschlag Hermes): Umfang, Reihenfolge und Maßstab.
9. **Risiken:**
   - Geheimnisse in der Sitzungsdatenbank;
   - die geliehene, womöglich wechselnde IP-Adresse;
   - der Prüfkanal ist über den Pfadschlüssel öffentlich;
   - veraltete Einträge in `laeufe/gedaechtnis/` aus der Zeit vor REGELN-02;
   - `/tmp` wird beim Neustart geleert.
10. **Was Chat-Claude beim Wiedereinstieg zuerst bekommt:** die Adressen dieser Datei und der Einstiegsdatei, dazu die Lesereihenfolge.

## 6. Maßstab — woran Chat-Claude prüft

Der Maßstab ist vor der Arbeit gesetzt und wird danach nicht verhandelt.

1. **Stillstand:** Am Anfang und am Ende laufen 0 Prozesse, 0 Container, 0 Subagenten, 0 Wecker und 0 Zeitgeber mit Biotop-Bezug. Der Vermerk steht in MEMORY.md und STAND-03. Der Wächter ist vom Biotop gelöst.
2. **Git:** `runde-5` zeigt auf `0c2f058`. Der Commit auf `einlagerung/runde-6-stand` enthält genau die 25 Einträge. Der Arbeitsbaum ist vorher und nachher gleich. Der bestehende Zweig ist unverändert.
3. **Vergängliches:** Jede kopierte Datei ist prüfsummengleich. Die Anzahl steht je Quelle da.
4. **Vollständigkeit:** Jede Fundstelle aus BIOTOP-LAGE-01 ist im Paket oder mit Grund ausgelassen, angegeben als x von y.
5. **Archiv KOMPLETT:** Manifestvergleich leer, Anzahl beidseitig gleich, Gegenprobe angeschlagen, `integrity_check` aller Datenbanken `ok`.
6. **Lauffähig:** Die Regression mit Kammer lief im entpackten Stand. Rot sind nur die 10 `test_w_g_*`. Jeder andere rote Test ist an der zweiten Arbeitskopie geprüft und eingeordnet. `/root/biotop` ist vor und nach der Probe gleich.
7. **Dokumentation:** WIEDEREINSTIEG erfüllt Abschnitt 5, Punkt 1 bis 10. INHALT deckt beide Archive. `dokumentation/` ist geheimnisfrei.
8. **Abholung:** ABHOLANLEITUNG ist vollständig ausgefüllt. SHA256SUMS ist im Abschlussordner und in Meldung 2 gleich.
9. **Geheimnisse:** Keines steht im Prüfkanal oder in einer Meldung, und keine Geheimnisdatei liegt in einem Archiv. Suche und Gegenprobe sind beigefügt.
10. **P2:** Die alte Adresse liefert 404, die geschwärzte Kopie 200. Das Original liegt in der nicht öffentlichen Ablage.
11. **Kosten:** 0 Biotop-Buchungen. Die Verdichtungen sind getrennt ausgewiesen, mit OpenRouter-Stand vorher und nachher.
12. **Belege:** Jede Zahl hat Bezugsgröße und Quelle, jedes „ausgeführt" einen Rohbeleg.

Was davon nicht erfüllt ist, steht oben in der Einstiegsdatei.

## 7. Meldungen an Philipp (Telegram)

**Meldung 1** kommt nach Schritt 1: `BIOTOP-EINLAGERUNG-01 BEGONNEN · <Zeit>`, dazu die vollständigen Adressen von Ordner und Einstieg und die Angabe `Stillstand: ja/nein`.

**Meldung 2** kommt zum Schluss, auch bei Abbruch:
```
BIOTOP-EINLAGERUNG-01 <EINGELAGERT | TEILWEISE | ABGEBROCHEN> · <Zeit>
Einstieg: <Adresse START-NN.md> · SHA-256 <Wert>
Wiedereinstieg: <Adresse> · Abholanleitung: <Adresse>
KOMPLETT: <Name> · <Bytes> · SHA-256 <Wert>
DOKUMENTATION: <Name> · <Bytes> · SHA-256 <Wert>
Regression im entpackten Stand: <x von y grün · rot nur test_w_g_* ja/nein>
Stillstand: 0 Prozesse · 0 Wecker · 0 Zeitgeber · Wächter gelöst ja/nein
<jede weitere Datei des Abschlussordners mit vollständiger Adresse>
OpenRouter-Kosten dieses Auftrags (Verdichtungen): <USD>
```
- Ist Meldung 2 länger als 3500 Zeichen, schickst du sie in Teilen.
- An die letzte Teilmeldung hängst du `WIEDEREINSTIEG` (alle Teile), `ABHOLANLEITUNG` und `SHA256SUMS` als Dateien. So hat Philipp sie auch ohne Prüfkanal.
- Jede Meldung schickst du genau einmal.

## 8. Nachfragen

Wie in BIOTOP-LAGE-01: Hat Chat-Claude Fragen, schickt Philipp sie dir als `NACHFRAGE-NN`. Du antwortest in `ANTWORT-NN.md` im selben Ordner, mit der nächsten freien Nummer und vollständiger Adresse in der Meldung.
