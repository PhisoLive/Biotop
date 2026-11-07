# Biotop — Phase 1 „Das Skelett" — BERICHT

**Auftrag:** INFINITE-EVOLUTION-BIOTOP-Masterprompt v1, Abschnitt 8, Phase 1
**Auftraggeber:** Philipp Zöllisch · **Ausführung:** Hermes · **Prüfer:** Chat-Claude
**Zeitraum:** 2026-09-18 23:17 – 2026-09-19 00:25 CEST · **Status:** abgeschlossen, Tor 1 mit **8 von 9 Zeilen bestanden**, 1 Zeile (Nr. 2) teilweise: 4 von 5 Schwächen behoben — das ist die geforderte Mindestzahl, aber S2 (Leistungsbremse) bleibt offen und steht auf der Liste für danach.

Belegregeln: Jede Zahl mit Bezugsgröße. „Bestätigt durch Ausführung" nur mit Datei in `ausgaben/`. Eigene Entscheidungen von Hermes sind mit **[Entscheidung Hermes]** gekennzeichnet.

---

## 1. Tor 1 — Zeilen mit Ergebnis

| Nr | Zeile (Masterprompt 8, Phase 1) | Ergebnis | Bezugsgröße | Ausgabe |
|---|---|---|---|---|
| 1 | Landkarte: alle Bereiche, alle Straßen | **bestanden** | Bereiche 4 von 4; Straßen 13 von 13 (Hermes-Zählung per grep vor dem Lauf: 13) | `ausgaben/12-strassen-hermes-grep.txt`, `13-landkarte-kennzahlen.json`, `14-landkarte-inhalt.txt`, `45-tor-zeilen-1-bis-4.txt` |
| 2 | Schwächen ≥ 4 von 5 gefunden und in angenommenen Generationen behoben; Kernmaß gestiegen | **bestanden (Mindestmaß), S2 offen** | 4 von 5 (S1, S3, S4, S5); Kernmaß 39 → 51 | `45-tor-zeilen-1-bis-4.txt`, `46-versiegelte-liste-entsiegelt.md` (sha256 `35190807…`, `46-…-pruefsumme.txt`), `25-lauf2-gen1.json`, `28-lauf2-gen3.json`, `30-lauf2-gen5.json` |
| 3 | Kein Rückschritt in angenommenen Generationen | **bestanden** | 0 von 3 angenommenen Generationen (Gen 1, 3, 5) mit gesunkenem hartem Maß; Rohwerte je Bereich je Generation beigefügt | `45-tor-zeilen-1-bis-4.txt` (Abschnitt Zeile 3) |
| 4 | Halluzinationsprobe: sauberer Bereich unverändert | **bestanden** | 0 von 14 Kandidaten im Bereich `bericht` angenommen; `git diff gen0..gen5 -- lagerhaus/bericht` leer | `45-tor-zeilen-1-bis-4.txt` (Abschnitt Zeile 4) |
| 5 | Lazarus: jede angenommene Generation zurückgeholt, Prüfsumme stimmt | **bestanden** | 4 von 4 (Gen 0, 1, 3, 5); Negativprobe (manipulierte Datei) → Prüfsumme weicht ab | `40-tor-lazarus.txt` |
| 6 | Kasse: Budget 0,10 € → Abbruch **vor** dem ersten Modellaufruf der nächsten Generation | **bestanden** (2. Messung) | Lauf 5: Abbruch vor Generation 3, Protokoll #800, 0 Buchungen und 0 `modell.aufruf`-Zeilen danach; ausgegeben 0,0680 € von 0,10 € | `44-tor-kasse.txt`; erste Messung mit Mangel: `44a-tor-kasse-lauf4-abbruch-mitten-in-generation.txt` |
| 7 | Laut scheitern: Werk ohne Tests → „Messgerät fehlt", 0 Generationen | **bestanden** | 0 von 0 Testdateien erkannt → Status `messgeraet_fehlt`; 0 gestartete Generationen; 0 Modellaufrufe außer Ethik-Prüfung der Aufnahme | `41-tor-laut-scheitern.txt` (Protokoll #443, #444) |
| 8 | Kammer: Endlosschleife → Zeitlimit, Wirt unberührt | **bestanden** | Zeitlimit 10 s → rc 124 nach 15,0 s (10 s + 5 s Nachlauf), Container getötet, 0 Container übrig; Werk-Prüfsumme vorher = nachher; Ausbruchsversuch in `/werk` und Wirt-`/tmp` beide wirkungslos | `42-tor-kammer.txt` |
| 9 | Anmeldung: jede Route ohne Token → 401 | **bestanden** | 10 von 10 Routen (9 GET + POST /anmelden mit falschem Kennwort) → 401 ohne und mit falschem Token; unbekannter Pfad ohne Token → 401 | `43-tor-anmeldung.txt` |

---

## 2. Was gebaut wurde

Verzeichnis `/root/biotop` (Archiv `biotop/biotop-fea114b.tar.gz`, 2.583 Zeilen Python in 21 Dateien; git-Commit `fea114b`). Nur Standardbibliothek plus Docker; kein Framework.

| Organ / Kernteil | Datei | Was es tut |
|---|---|---|
| Datenbank (SQLite, WAL, Transaktionen) | `biotop/kern/datenbank.py` | 14 Tabellen: werke, laeufe, generationen, kandidaten, protokoll, kasse, landkarte, strassen, vertraege, immunsystem, benutzer, tokens, lazarus |
| Protokoll (unveränderlich, fortlaufend, Hash-Kette) | `biotop/kern/protokoll.py` | jede Zeile trägt SHA-256 der Vorzeile; `protokoll-pruefen` → Kette in Ordnung, 800 von 800 Zeilen (`ausgaben/47-protokoll-kette.json`) |
| Kasse | `biotop/kern/kasse.py` | Preistabelle (USD/Mio Token, OpenRouter-Katalog 18.09.2026, Kurs 1,08 fest **[Entscheidung Hermes]**), `vorpruefung()` vor **jedem** Aufruf (Zeile 65), `generation_vorpruefung()` vor jeder Generation (Zeile 148), Buchung aus der tatsächlichen `usage`-Antwort |
| Anbieterschicht (ein Port, Adapter) | `biotop/anbieter/__init__.py` | `aufrufen()` (Zeile 104) ist der einzige Weg zu einem Modell: Kasse → Protokoll → Aufruf → Buchung → Protokoll. Adapter: OpenRouter. Schwere Modelle des bestehenden Teams: Port vorhanden, in Phase 1 kein Aufruf nötig (kein Mentor, keine Jury) |
| Ausführungskammer | `biotop/organe/kammer.py` | Docker `biotop-kammer:1` (python:3.12-slim + pytest, bandit, vulture; unprivilegierter Benutzer): `--network none`, `--memory 512m`, `--cpus 1`, `--pids-limit 256`, `--read-only`, `--cap-drop ALL`, Kopie des Werks je Lauf, danach verworfen; Zeitlimit → Kill + rc 124 |
| Messgerät (harte Maße) | `biotop/kern/messgeraet.py`, `kern/referenzlast/lagerhaus.py` | je Bereich: tests_bestanden/fehlgeschlagen (junit), sicherheit_punkte (bandit HIGH 10/MEDIUM 3/LOW 1), tote_funktionen (vulture ≥ 60 %), laufzeit_ms (Referenzlast, min aus 3), groesste_funktion; Werk: zyklen, bauzeit_ms. Kernmaß **[Entscheidung Hermes, Philipp zu bestätigen]**: Σ(tests_bestanden − tests_fehlgeschlagen − 3·sicherheit_punkte − tote_funktionen). Toleranzen **[Entscheidung Hermes]**: laufzeit ±15 % (Kammer-Rauschen gemessen: 24,5–26,3 ms bei unverändertem Code), groesste_funktion +25 %, alles andere 0 % |
| Aufnahme | `biotop/organe/aufnahme.py` | ZIP / Git / Ordner; Zählung Dateien, Zeilen je Sprache, Testdateien; erster Testlauf in der Kammer; ethische Prüfung (Stichworte + 1 Modellurteil, das Werk beantwortet die Frage nicht); `MessgeraetFehlt` (Zeile 175) bei 0 Tests oder nicht bauend |
| Landkarte | `biotop/organe/landkarte.py` | Stufe 3 aus `ast` (39 Funktionen), Stufe 2/1/0 durch `gemini-2.5-flash-lite` mit Prüfsumme je Quelldatei (zweiter Aufbau: 0 Modellaufrufe, `13b-…`), Straßen als Import-Graph (13 Kanten), Verträge: 19 aus Docstrings + 34 abgeleitet aus Signaturen, gekennzeichnet; `sicht()` = Stufe 0 + Stufe 1 + Stufe 3 des Bereichs + Verträge der Nachbarn; `wirkungskreis()` (Zeile 112) = transitive Rück-Abhängige |
| Genesis (1 Nische, 2 Hersteller) | `biotop/organe/genesis.py` | Nische „Der Sichere" (T = 0,2) mit `openai/gpt-4.1-mini` und `google/gemini-2.5-flash`; Ausgang: unified diff + Begründung + berührte Verträge; Diffs auf fremde Dateien werden vor der Anklage verworfen; Liste gescheiterter Wege des Laufs wird mitgegeben |
| Diff-Werk | `biotop/kern/diffwerk.py` | deterministische Anwendung von Modell-Diffs (Hunks werden über den Kontext gesucht, nicht über die Zähler); Hunk > 60 % der Datei = Neuschreibung → abgelehnt (3.6) |
| Aegis (Schritte 1, 4, 5) | `biotop/organe/aegis.py` | Wirkungskreis; Angriff (`gemini-2.5-flash` liefert Tests, gewertet nur nach Ausführung: AssertionError oder Ausnahme im Werk zählt, Test-eigene Fehler zählen nicht); Ausführung: Messung mit Kandidat in der Kammer, Pareto über Wirkungskreis (Zeile 281/283). Mitgebrachte Tests zählen nur, wenn sie am Ausgangszustand fehlschlagen und am Kandidaten bestehen. Jeder bestätigte Fehler → Immunsystem |
| Nexus (vereinfacht für Phase 1) | `biotop/lauf.py` | je Bereich Schwarm → Ankläger; bester Überlebender je Bereich (größter Kernmaß-Zuwachs); Zusammensetzen; Generalprobe (ganzes Werk); Pareto (Zeile 200/205); Schnappschuss; Vorlage zur Freigabe; Ablehnung → Lazarus-Rückkehr |
| Lazarus | `biotop/organe/lazarus.py` | git-Tag `lauf<n>-gen<k>` + tar.gz + SHA-256 über sortierte `pfad:sha256`-Liste; `rueckkehr()` in Werk oder Prüfziel |
| Anmeldung | `biotop/kern/anmeldung.py`, `biotop/dienst.py` | PBKDF2 (200.000 Runden), Token als SHA-256 gespeichert; Dienst auf 127.0.0.1:8642; `_benutzer()` wird vor **jeder** Routenauflösung geprüft (dienst.py Zeile 71, 86) — kein Schalter |
| Befehlszeile | `biotop/__main__.py` | `lauf anlegen`, `einlegen`, `kartieren`, `mass`, `generation`, `freigabe`, `lazarus`, `kasse`, `protokoll`, `protokoll-pruefen`, `benutzer` |

**Übungswerk `lagerhaus`** (`werk/uebungswerk-ausgang.tar.gz`, 856 Zeilen Python, 4 Bereiche, 50 Tests): `formeln` (Rabattformeln), `preise` (Katalog, Staffeln, Rabatt, Währung → formeln), `lager` (Bestand aus Journal, Reservierungen), `bericht` (Auswertung → lager, preise; **sauber**). Fünf Schwächen versiegelt in `/root/versiegelt/SCHWAECHEN-uebungswerk.md` (außerhalb des Biotops, mode 600), SHA-256 vor dem Lauf `35190807279aa713746a3f19eee6f9629aa77a6f7bd6d7139d2dd3695c639c8e`, entsiegelte Kopie in `ausgaben/46-…`.

---

## 3. Was gemessen wurde — Hauptlauf (Lauf 2)

| Generation | Status | Kernmaß | Tests | Was angenommen wurde |
|---|---|---|---|---|
| 0 | Ausgangszustand | 39 | 50 von 50 | — |
| 1 | angenommen | 41 | 50 von 50 | preise: 2 tote Funktionen entfernt (S4) — gemini-2.5-flash |
| 2 | abgelehnt | — | — | 0 von 8 Kandidaten überlebt |
| 3 | angenommen | 49 | 58 von 58 | formeln: `__builtins__` leer (S1); lager: Reservierung beim Einlösen reduziert (S3); preise: Staffel `>=` (S5); 5 Immuntest-Dateien (8 Testfunktionen) aus dem Ankläger |
| 4 | abgelehnt | — | — | 0 von 8 |
| 5 | angenommen | 51 | 60 von 60 | preise: Typprüfung `stueckpreis` + 2 Tests (kein Schwächenbezug; Maß stieg, Verträge unverletzt) |
| 6 | abgelehnt | — | — | 0 von 8 |
| 7 | abgelehnt | — | — | 0 von 8 |

Kandidaten gesamt Lauf 2: 56; angenommen 5 (in 3 Generationen); 1 überlebte den Ankläger, wurde aber nicht gewählt (K31, preise, Gen 3 — K32 hob das Maß stärker); abgelehnt 50. Gründe der Ablehnung (gezählt aus Tabelle `kandidaten`): „kein hartes Maß gestiegen" 23, „hartes Maß gesunken" 12, „Diff nicht anwendbar / Neuschreibung" 10, „Diff berührt fremde Dateien" 3, „Ankläger: führt Fehler ein" 2. Detail je Kandidat: `GET /laeufe/2/kandidaten` in `biotop/biotop.db`, Tabelle `kandidaten`.

**Kosten Hauptlauf 2:** 0,2166 € in 100 Aufrufen (Budget 30 €). **Alle Läufe zusammen:** 236 Aufrufe, 0,4031 € nach Preistabelle; OpenRouter-Konto meldet 0,4316 USD = 0,3996 € (`ausgaben/49-openrouter-gegenprobe.txt`; Abweichung 0,9 %, Kurs). Details `KASSE.md`.

**Was der Ankläger geleistet hat (bestätigt durch Ausführung):** 6 Immuntest-Dateien mit 10 Testfunktionen im Werk (Tests 50 → 60), alle aus Angriffstests, die am Ausgangszustand fehlschlugen und am Kandidaten bestehen — darunter `auswerten("__import__('os').system(...)")` → `FormelFehler`, `reserviert()` nach `reservierung_einloesen()`, `preis_fuer('A1', 10)` bei Staffel ab 10. 3 frühe Angriffe (Lauf 1/2 Gen 1) wurden als **fehlerhaft verworfen** (Tests riefen nicht existierende Methoden `Journal.buche`, `Katalog.add`): Protokoll `immun.verworfen` **[Entscheidung Hermes]** — danach Regel geschärft (nur AssertionError oder Ausnahme im Werk zählt).

---

## 4. Eigene Entscheidungen von Hermes (Konfiguration, keine Architektur)

1. **Prüfkanal-Stelle:** bestehender Kanal `/var/pruefkanal/…/laeufe/biotop-phase-1/` (von Philipp bestätigt).
2. **Kernmaß-Formel** und **Toleranzen** (s. o.). Philipp soll das Maß bestätigen oder ändern; danach neuer Lauf (Verfassungssatz 2).
3. **Modelle:** Masse `openai/gpt-4.1-mini` + `google/gemini-2.5-flash` (zwei Hersteller, Schwarm); Angriff `google/gemini-2.5-flash`; Landkarte `google/gemini-2.5-flash-lite`; Ethik `openai/gpt-4.1-mini`. Philipp kann in `genesis.NISCHEN`, `aegis.MODELL_ANGRIFF`, `landkarte.MODELL_ZUSAMMENFASSUNG` ändern.
4. **Freigaben im Hauptlauf** hat Hermes stellvertretend erteilt (3 Generationen, je mit Begründung im Protokoll `freigabe.frei`), weil Philipp nicht am Terminal war. Im echten Betrieb gibt Philipp frei; der Mechanismus (`freigabe`) ist derselbe.
5. **Lauf 1 abgebrochen und Lauf 2 gestartet**, weil zwei Mängel im Biotop selbst behoben wurden (Diff-Werk ersetzte git-apply; Toleranz groesste_funktion) — das ist eine Maßänderung, also neuer Lauf (Verfassungssatz 2). Beide Läufe sind in der Datenbank.
6. **Kassenprobe zweimal gemessen** (`44a`, `44`): Messung 1 zeigte, dass die Vorprüfung je Aufruf zwar vor dem überschreitenden Aufruf abbrach (kein Cent über Budget), aber erst mitten in Generation 4. Die Torzeile verlangt Abbruch vor dem **ersten** Aufruf der nächsten Generation → `generation_vorpruefung` ergänzt (Voranschlag = teuerste bisherige Generation). Messung 2 belegt die Zeile.
7. **Biotop-Code wurde von Hermes geändert, nie vom Biotop** — alle Änderungen während der Läufe waren Fehlerbehebungen durch Hermes am Kern, protokolliert (`lauf.abgebrochen` #80, `immun.verworfen`), git-Historie in `/root/biotop`. Das laufende Biotop hat keinen Schreibpfad auf seinen eigenen Code (Kandidaten dürfen nur `lagerhaus/<bereich>/` und `tests/test_<bereich>_*` berühren, geprüft in `genesis.py` und `aegis.py`).

---

## 5. Verstöße, Grenzen, Ehrlichkeit

- **S2 (Leistungsbremse) nicht behoben.** 14 Kandidaten im Bereich `lager`; die Nische „Der Sichere" schlägt Fehlerbehebung vor, keine Beschleunigung. Ein Kandidat (K35, formeln, ast-basierter Auswerter) verschlechterte die Laufzeit um 290 % und wurde zu Recht abgelehnt. Die Nische „Der Schnelle" ist Phase 2.
- **S1 nur zur Hälfte im Maß sichtbar:** `__builtins__: {}` schließt `__import__`/`eval` (3 Immuntests beweisen es), aber bandit meldet B307 weiterhin (3 Punkte unverändert). Ein Kandidat mit `ast`-Auswerter würde das Maß senken — kam als Neuschreibung (68 von 68 Zeilen) und wurde abgelehnt (3× derselbe Weg von gpt-4.1-mini trotz Liste gescheiterter Wege).
- **Angriffstests des Anklägers sind teilweise redundant** (K29 und K30 prüfen dasselbe; K31 und K32 ebenso): 10 Testfunktionen für 4 Fehler. Satz 7 („n Fehler = n Tests") ist erfüllt in der Richtung ≥, nicht =. Dedup-Regel: Liste für danach.
- **Rollentrennung des Kerns** (eigener Prozess, eigene DB-Rolle, Abschnitt 5): in Phase 1 **nicht** umgesetzt; Kern und Organe laufen im selben Prozess, Schutz ist Code-Disziplin (Pfadprüfung), nicht Betriebssystem. Liste für danach.
- **tree-sitter nicht verwendet**, `ast` reicht für Python-Werke; für Phase 4 (Python) ausreichend, für gemischte Werke nachzurüsten.
- **Laufzeitmessung rauscht** (Kammer, geteilte CPU): 3 Kandidaten im sauberen Bereich wurden mit „laufzeit gesunken" abgelehnt, obwohl sie den Code kaum berührten — konservativ richtig (Pareto), aber Messrauschen > 15 % kommt vor. Mehr Wiederholungen oder cgroup-Pinning: Liste für danach.
- **Ethikprüfung** ist ein Stichwortfilter plus ein Modellurteil auf README + Dateiliste — sie fängt offensichtliche Fälle, keine verschleierten.
- **Zeile 9 prüft den Dienst auf 127.0.0.1**, nicht hinter Caddy; der Dienst ist bewusst nicht öffentlich.
- Ein Biotop-Fehler (NameError nach Refactor) brach Lauf 5 Gen 1 vor dem ersten Aufruf ab; behoben, Eintrag entfernt, in `44-tor-kasse.txt` dokumentiert.

---

## 6. Liste für danach (Phase 2+, nicht in Phase 1 gefordert)

1. Nischen „Der Schnelle", „Der Elegante", „Der Wilde"; Bandit-Gewichtung je Modell/Nische/Werkklasse.
2. Generation 0 (Mutanten) — die Basis ist da (Messgerät + Kammer + junit-Auswertung).
3. Verträge explizit; Ankläger Schritte 2/3; Nexus-Verhandlung an Grenzen.
4. Kern als eigener Prozess mit eigener DB-Rolle.
5. Immuntest-Dedup (gleicher Fehler → ein Test); Angriffstests mit Fehlerklassifikation.
6. Laufzeitmessung stabilisieren (5 Läufe, Median, CPU-Pinning).
7. Landkarte: tree-sitter für Nicht-Python; Aufruf-Kanten (Funktion→Funktion) zusätzlich zu Import-Kanten.
8. Diff-Werk: Modelle liefern 11 von 56 Diffs unbrauchbar (falsche Zähler, Neuschreibungen) — Prompt-Beispiel und Retry mit Fehlermeldung ans Modell.
9. Drei Gedächtnisse (Projekt: Tabelle `kandidaten` liefert bereits die gescheiterten Wege; Art- und Geschmacksgedächtnis fehlen), Mentor, Entropie, Jury, Oberfläche.
10. Abo-Kontingent-Zähler ist vorhanden (`kasse.kontingent`), aber ohne Adapter für die schweren Modelle des Teams.

---

## 7. Inhalt dieses Ordners

- `BERICHT.md` — dieses Dokument
- `KASSE.md` — alle 236 Modellaufrufe, Summen je Lauf/Modell/Zweck
- `ausgaben/` — 30 Rohausgaben (00–49), darunter das vollständige Protokoll (800 Zeilen, Hash-Kette geprüft)
- `werk/` — Ausgangswerk, gehobenes Werk (Lauf 2 Gen 5 mit git-Tags), Lazarus-Archive Gen 0/1/3/5
- `biotop/` — Biotop-Code (Commit fea114b), Datenbank (alle Gedächtnisse), `PRUEFSUMMEN.txt`
- Prüfsumme des gesamten Ordners: `PRUEFSUMME-ORDNER.txt` (SHA-256 über die sortierte Liste aller Datei-Prüfsummen, ohne diese Datei selbst)

Abholadresse: `https://milieulux-reinigung-muenchen.de/_akte/<schlüssel>/laeufe/biotop-phase-1/` — Verzeichnisse haben kein Listing; Einstieg über `BERICHT.md`, `KASSE.md`, `DATEIEN.txt`.
