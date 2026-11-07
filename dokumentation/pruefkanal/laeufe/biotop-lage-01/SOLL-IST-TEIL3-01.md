# BIOTOP-LAGE-01 · Fassung 2 · `SOLL-IST-TEIL3-01.md`

- **Inhalt:** FK30 · Entwurf E, Stück 3 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil E, Arbeitszeit 25.09.2026 16:10:47–18:55:32 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/soll-ist/SOLL-IST-TEIL3.md` · 20352 B · SHA-256 `8970216367eebd27e6389a98a1db025f8352babc8c2ec52b490cb1d85c0a1a81`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (1 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# SOLL-IST — Abgleich gegen Masterprompt Fassung 8 (FK30) · Teil 3 von 4

Umfang dieses Teils: aus Abschnitt 8 die Phasen 4 und 5, dazu die Abschnitte 9 und 10 und die Anhänge A und B. Kürzel, Lesart und Zählung stehen in Teil 1.

Lesart 4 gilt hier besonders: Tor 4 in Fassung 8 gilt je Testwerk. Die Einträge zu Tor 4 stehen mit Blick auf T4 als `NICHT BEGONNEN`. T3 lief nach dem Wortlaut von Fassung 7, ist nicht abgenommen (Z. 456) und zählt nicht zur Sättigung (Z. 461). Seine Messwerte stehen in `TORE`. Stand: 25.09.2026 gegen 18:00 CEST. Runde 6 und der Bau S1c laufen; ihren Endstand trägt Hermes nach.

## Abschnitt 8 — Phase 4, der Breitentest

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP8.36 | 420 | „Hermes baut alle Testwerke selbst (Entscheidung Philipps, 21.09.2026), mit versiegelten Schwächen wie bei `lagerhaus` und `logmuehle`.“ | BELEGT | T3 `versandwerk` mit den versiegelten Schwächen S1 bis S5 (Z. 458). Philipps Entscheidung steht in `PH` Z. 371. Für T4 bis T6 ist die Forderung NICHT BEGONNEN. |
| MP8.37 | 424 | „T3 — andere Sprache und andere Werkzeugkette. TypeScript oder JavaScript, ~1.500–2.500 Zeilen, 4–5 Bereiche, eigene Testsammlung (vitest oder jest), eigenes statisches Prüfwerkzeug.“ | TEILWEISE | Das Werk ist gebaut (`T3A`; Umfang in `LAGE`). Der Durchlauf endete ohne Abnahme (Z. 456): „T3 zählt nicht zur Sättigung des Breitentests“ (Z. 461). Es fehlt die Abnahme. |
| MP8.38 | 426 | „T4 — Größe, fremder Stil, fehlende Tests, echte Altlasten. Python, ~6.000–10.000 Zeilen, 8–12 Bereiche, ohne vorhandene Testsammlung“ … „Hermes erzeugt es über ein anderes Modell als sein eigenes“ | NICHT BEGONNEN | T4 beginnt nach der Startregel der Runde 6 (`R6U` Z. 21–22). Runde 6 läuft. |
| MP8.39 | 428 | „T5 — Werk mit Oberfläche. HTML, CSS und JavaScript ohne Rahmenwerk, ~1.000–1.800 Zeilen.“ | NICHT BEGONNEN | Runde 6 verlangt vor T5 „TypeScript-Proben“ (`R6U` Z. 20). |
| MP8.40 | 430 | „T6 — Zustand und Außenwelt. Python, ~2.000–3.000 Zeilen, mit SQLite-Datenbank, Dateiablage und einer Schnittstelle nach außen, die in der Kammer stillgelegt ist.“ | NICHT BEGONNEN | — |
| MP8.41 | 432 | „Jedes Werk ist ein eigener Auftrag mit eigenem Abschlussordner.“ | BELEGT | T3: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/` mit den Unterordnern `abschluss-01` bis `abschluss-03` (R150, R67). |
| MP8.42 | 434 | „Sie werden nach den Grundsätzen 7 bis 9 behandelt: reparieren, was im Kernpfad liegt; benennen und listen, was außerhalb liegt; ein Reviewdurchgang.“ | TEILWEISE | Nach T3 gibt es die Liste nach T3 (Z. 474) und die Behebungsrunden vor T4 (`R1B` bis `R5B`). Runde 5 hatte zwei Reviews; es gilt das zweite (`R6U` Z. 4–6; `/root/biotop-vor-t4-05/ZWEI-REVIEWS.md`). Runde 6 läuft. Es fehlt der Abschluss der Reparatur. |

### Tor 4 je Testwerk (Fassung 8)

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP8.43 | 437 | „Aufnahme: Werk gebaut, Bau- und Testlauf, versiegelte Schwächen mit Gegenzeugen hinterlegt (bei T4 stattdessen eine unabhängig erhobene Altlastenliste mit Bezugsgröße).“ | NICHT BEGONNEN | T3 (nach Fassung 7): siehe `TORE`. |
| MP8.44 | 438 | „Generation minus eins: Rauschmessung mit Sperren je Bereich; Maßeichung am sauberen Vergleichsbereich, stillgelegte Regeln mit Befundzahl ausgewiesen; Eichgegenstand versiegelt; 4 von 4 Proben bestanden und 4 von 4 Gegenproben an der vorgesehenen Zusicherung gescheitert; Eichkosten getrennt.“ | NICHT BEGONNEN | T3: siehe `TORE`. |
| MP8.45 | 439 | „Generation 0: Mutantenfang ≥ 80 von 100 nicht-äquivalenten, je Art ausgewiesen, mit der Verteilung dessen, was vorab verworfen wurde (Typsieb); kein Durchlauf, in dem überwiegend neutral geurteilt wurde, geht in die Zahl ein (Grundsatz 13).“ | NICHT BEGONNEN | T3: siehe `TORE`. Der Kern kennt zwei Wege. Mit einem Mutantenplan von Hermes verlangt er zur Verteilung eine Angabe, wer gesiebt hat (`lauf.py:833–837`). Ohne Plan erzeugt der Kern die Mutanten selbst; dazu steht im Code: „keine Verteilung, auch keine Null (Tor-4-Zeile 3 bleibt nicht belegt)“ (`lauf.py:843–847`). Welcher Weg bei T4 gilt: UNBEKANNT (Lücke L-E8 in Teil 4). |
| MP8.46 | 440 | „Schwächen: ≥ 80 % der versiegelten Schwächen behoben nach „behoben heißt verschwunden"; je Schwäche der behebende Kandidat und der Grund, aus dem er angenommen wurde“ | NICHT BEGONNEN | T3: Z. 458; `TORE`. |
| MP8.47 | 441 | „Kein Rückschritt: 0 von n angenommenen Generationen mit gesunkenem hartem Maß, je Maßfeld einschließlich Laufzeit, gepaart gemessen (Grundsatz 14).“ | NICHT BEGONNEN | T3: siehe `TORE`. |
| MP8.48 | 442 | „Halluzinationsprobe (streng): Der saubere Vergleichsbereich bleibt unberührt.“ | NICHT BEGONNEN | T3: Z. 460; `TORE`. |
| MP8.49 | 443 | „Verhaltensvergleich: jede angenommene Generation hat ihn durchlaufen; je Urteil „x von y Funktionen beobachtet"; Enthaltungen zählen nicht als bestanden“ | NICHT BEGONNEN | Der Bau ist Vorbedingung 2 (MP8.59). T3: siehe `TORE`. |
| MP8.50 | 444 | „Doppelungsanteil unter 20 %, gemessen nach der Methode aus Vorbedingung 1: alle erzeugten Angriffstests, geurteilt nach ihrer geschriebenen Behauptung.“ | NICHT BEGONNEN | T3: „Nicht gemessen: Doppelungsanteil nach Vorbedingung 1“ (Z. 460). |
| MP8.51 | 445 | „Immunisierung (3.10 F3): für die Sprache des Werks auf dem tatsächlichen Pfad gezählt; 0 Fälle heißt nicht belegt.“ | NICHT BEGONNEN | T3: „Nicht belegt: Immunisierung“ (Z. 460). Der Bau ist Vorbedingung 9 (MP8.66). |
| MP8.52 | 446 | „Neutralzähler: jedes Organ mit Nenner; eine Torzeile, die an einem Organ hängt, gilt nur, wenn es in mehr als der Hälfte seiner Fälle geurteilt hat — je Durchlauf, nicht über die Summe.“ | NICHT BEGONNEN | Gebaut sind die Tabelle `neutralzaehler` in T3 (R83) und der Zählkontext im Lauf (`lauf.py:198–200`). |
| MP8.53 | 447 | „Verbundausfall: als Ausfall gezählt, nie als Beitrag; belegt an mindestens einem echten oder gestellten Ausfall.“ | NICHT BEGONNEN | T3 hat eine Messung an echten Ausfällen (`T3A` Z. 81–83; `TORE`). Dazu Widerspruch W-E2 in Teil 4. |
| MP8.54 | 448 | „Verdrahtung: volle Regression einschließlich Verdrahtungstest grün am Kernstand des Laufs (Grundsatz 12).“ | NICHT BEGONNEN | Der Bau ist Vorbedingung 7 (MP8.64). |
| MP8.55 | 449 | „Sättigung oder Budgetabbruch dokumentiert — der Lauf endet nie still.“ | NICHT BEGONNEN | T3: Zwei Läufe liefen bis zur Sättigung beziehungsweise bis zum Budget (Z. 457; R66). |
| MP8.56 | 450 | „Ein Reviewdurchgang; Abschlussordner trägt die Torzeilen. Zwischenbericht spätestens bei 120 von 150 Aufrufen einer Sitzung, mechanisch ausgelöst.“ | NICHT BEGONNEN | Ob der Zwischenbericht mechanisch ausgelöst wird, habe ich nicht geprüft. |
| MP8.57 | 452 | „Der Breitentest ist abgeschlossen, wenn zwei aufeinanderfolgende Testwerke neuer Art durchlaufen, ohne einen neuen Messgerätfehler zu erzeugen.“ | NICHT BEGONNEN | T3 zählt nicht (Z. 461). |

### Vorbedingungen für T4 (Z. 463: „je mit Gegenprobe durch den Laufweg“)

Hauptquelle ist die Tafel der Runde 1 (`R1B` Z. 47–59, Stand `330b4ec`). Spätere Runden habe ich nur über ihre Kopfzeilen und die Übergabe der Runde 6 gelesen. Wo eine Zeile auf Runde 1 beruht, steht das dabei.

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP8.58 | 464 | „Laufzeit gepaart: Vorgeneration und Kandidat in derselben Sitzung, Median mehrerer Messungen je Seite; kein historisches Minimum als Bezug (Grundsatz 14). Gegenprobe: K2904 und K3091, dieselbe Änderung, werden gleich entschieden. Grenzanzeige ohne irreführende Rundung.“ | TEILWEISE | Gebaut ist `messgeraet.laufzeit_gepaart` mit 5 Messungen je Seite und Median (`R1B` Z. 49). Die Gegenprobe wurde in den Runden 1 bis 3 in 2 von 3 Durchgängen gleich entschieden (`R1B` Z. 49; `R2B` Z. 25; `R3B` Z. 14), in Runde 4 in 3 von 3 (`R4B` Z. 66). Es fehlt ein Beleg zur Grenzanzeige: In `R1B` bis `R5B` NICHT GEFUNDEN. Gesucht habe ich nach „Rundung“ und „gerundet“; der einzige Treffer, `R1B` Z. 200, betrifft etwas anderes. |
| MP8.59 | 465 | „Verhaltensvergleich: unbeobachtet = Enthaltung; „x von y beobachtet" in Urteil und Protokoll; Korpus aus den Verträgen erzeugt, mit Randfällen (leer, einzeln, Grenzwert), sodass jede exportierte Funktion eines geänderten Moduls gerufen wird. Gegenprobe: K3106 wird erkannt.“ | TEILWEISE | Die Gegenprobe am Laufweg ist belegt: K3106 abgelehnt (`R1B` Z. 50). In Runde 1 galt: „Nur TS; für Python immer Enthaltung“ (`R1B` Z. 50). Ab Runde 2 gibt es eine Python-Sonde; die Reviews der Runden 2 bis 4 fanden jeweils neue Lücken (`R2B` Z. 1, `R3B` Z. 1, `R4B` Z. 1). Runde 5 endete mit zwei offenen Messfehlern, R6-1 und R6-4 (`R5B` Z. 1). Sie sind Auftrag der Runde 6 (`R6U` Z. 7–13). |
| MP8.60 | 466 | „Sondenausfall: anhalten oder zurückstellen, keine Ablehnung, kein Gedächtniseintrag.“ | TEILWEISE | Am Laufweg belegt: Drei Ausfallarten führen zum Zurückstellen, und überwiegen die zurückgestellten Kandidaten, gilt die Generation als abgebrochen (`R1B` Z. 51). Dort steht auch, dass „kein Gedächtnis“ in `test_review3` nicht zugesichert ist. Ob spätere Runden das nachgeholt haben, habe ich nicht geprüft. |
| MP8.61 | 467 | „Verhandlung: `paar_ok` an die Tragfähigkeit des Verhaltensvergleichs binden.“ | BELEGT | `lauf.paar_bestanden`; Probe und Gegenprobe am Laufweg `lauf._verhandeln` (`R1B` Z. 52). |
| MP8.62 | 468 | „Maßeichung: `anwenden` vergleicht die Eichung selbst, nicht nur ihren Marker.“ | TEILWEISE | `masseichung.anwenden`; Probe und Gegenprobe gibt es nur am Modul (`R1B` Z. 53). Es fehlt die Gegenprobe durch den Laufweg, die Z. 463 verlangt. Stand Runde 1. |
| MP8.63 | 469 | „Generation 0: Mehrheitsregel je Durchlauf; `tsc`-Meldung gespeichert; die Prüfung zwischen den Runden baut den Typbau mit.“ | BELEGT | Probe und Gegenprobe am Laufweg `lauf.generation0` (`R1B` Z. 54). Die Mehrheitsregel steht in `organe/generation0.py:133` und `:144`. |
| MP8.64 | 470 | „Verdrahtungstest: Pflichtkanten an die Phase der Generationen gebunden; im Prüfwerk schlägt eine Regel im sauberen Bereich an; ein Laufweg-Test verlangt die Ablehnung einer ungedeckten Abweichung.“ | TEILWEISE | Der Test ist grün in beiden vollen Regressionen der Runde 1 und rot in drei Gegenproben (`R1B` Z. 55). Dort steht aber: „die Phasenbindung ist nur am Prüfwerkzeug belegt“. Es fehlt der Beleg der Phasenbindung am Laufweg. Das Register vollständig zu machen ist Auftrag der Runde 6 (`R6U` Z. 18). |
| MP8.65 | 471 | „Protokoll: Kernmaß geeicht geführt, roh gekennzeichnet.“ | TEILWEISE | `masseichung.anwenden`, geprüft nur am Modul. `R1B` Z. 56: „Die Protokollfelder `kernmass_f2_roh` liest kein Test“. Es fehlen Probe und Gegenprobe am Laufweg. |
| MP8.66 | 472 | „Doppelung: Behauptung für alle erzeugten Angriffstests protokollieren. Immunisierung auf dem TypeScript-Pfad bauen.“ | TEILWEISE | Behauptungen: Laufweg `aegis.pruefen`, dort sind `behauptungen` = alle 2 erzeugten Tests (`R1B` Z. 57). Die Immunisierung für TypeScript ist gebaut und mit einer Kammerprobe geprüft, aber „Das zusammengeführte Ergebnis wird geparst, nicht unter node ausgeführt“ (`R1B` Z. 57). An einem TypeScript-Werk im Lauf ist sie nicht belegt, weil die Behebungsrunden ohne Modellgeld laufen (Z. 476; `R5B` Z. 3). |
| MP8.67 | 473 | „Projektgedächtnis: Ein Laufzeit-Grenzmaß sperrt einen Weg nur, wenn der Kandidat den Bereich berührt hat und die gepaarte Messung die Verschlechterung bestätigt; Risse in unberührten Bereichen nie.“ | BELEGT | Schreib- und Leseseite am Laufweg; Gegenprobe 2×2 (`R1B` Z. 58). |
| MP8.68 | 474 | „Aus der Liste nach T3: Erreichbarkeitsführung für gedrosselte Anbieter; Verfallsbedingung der Ausnahmeliste des Python-Wächters; `_beschleunigen` entfernen; Einzelwerte der Rauschmessung speichern.“ | BELEGT | Drosselung und Rohwerte am Laufweg (`R1B` Z. 59). Verfall: `tests/test_t3_python_annahmen.py:155–172`. `_beschleunigen` ist entfernt, der Test dazu steht in `tests/test_vor_t4.py:217–220` (R126). |
| MP8.69 | 476 | „Die roten Spezifikationen aus `abschluss-03` (9 Tests, am Commit `f821707` 9 von 9 rot) sind Teil dieser Vorbedingungen.“ | BELEGT | `R1B` Z. 30: „Sie sind in beiden vollen Regressionen grün“. |
| MP8.70 | 476 | „Die Behebungsrunde kostet kein Modellgeld; sie endet mit voller Regression, eigenem Commit, einem Review und einem Abschlussordner.“ | TEILWEISE | Die Runden 1 bis 5 haben einen Abschlussordner im Prüfkanal (`biotop-vor-t4` bis `biotop-vor-t4-05`, R67). Runde 5 lief ohne Modellgeld (`R5B` Z. 3); ihr Kern-Commit ist `0c2f058` (R150). Runde 5 hatte zwei Reviews (MP8.42). Von Runde 6 liegt im Prüfkanal nur ein Zwischenbericht (R67), der Arbeitsstand steht in `R6U`. Es fehlt der Abschluss der Runde 6. |

## Abschnitt 8 — Phase 5, erstes echtes Werk

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP8.71 | 480 | „Werk: noch nicht bestimmt. Die Wahl trifft Philipp nach dem Breitentest.“ | NICHT BEGONNEN | — |
| MP8.72 | 488 | „Verfassung des Werks — schreibt Philipp; Hermes legt einen Entwurf vor.“ … „Ohne diesen Eintrag wartet das Organ und der Lauf beginnt nicht.“ | NICHT BEGONNEN | Dass das Organ ohne tragenden Pfad wartet, ist gebaut (MP3.5.13). |
| MP8.73 | 489 | „Aufnahme und Landkarte als eigener Abschnitt mit eigenem Bericht, bevor eine Generation läuft“ | NICHT BEGONNEN | — |
| MP8.74 | 490 | „Generation minus eins und Generation 0 als eigene Abschnitte mit eigenen Budgets.“ | NICHT BEGONNEN | — |
| MP8.75 | 491 | „Freigaben ausschließlich durch Philipp; die Vollmacht für Übungswerke gilt hier nicht. Hier beginnt das echte Geschmacksgedächtnis.“ | NICHT BEGONNEN | Der Freigabebefehl verlangt einen Namen (`--von`, `__main__.py:61`). Nach einer Sperre, die bei Werken mit Betriebszweck nur Philipp zulässt, habe ich nicht gesucht. |
| MP8.76 | 493 | „Tor 5 wird gesetzt, wenn das Werk feststeht“ | NICHT BEGONNEN | — |

## Abschnitt 9 — Abschlussordner und Berichtspflicht

Die Zählungen beziehen sich auf die Ordner `biotop-*` im Prüfkanal ohne `gedaechtnis`, erhoben aus `arbeit/inventar/i3.json` (R67; Liste in R26), nur oberste Ebene.

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP9.1 | 499 | „Jeder Hermes-Auftrag (jede Phase) endet zwingend — auch bei Abbruch, Zeitmangel oder Scheitern — mit einem Abschlussordner an der festgelegten, von außen abrufbaren Stelle im Prüfkanal.“ | BELEGT | Jeder Auftrag hat einen eigenen Ordner im Prüfkanal (R67). Noch ohne Abschluss sind die laufenden Aufträge `biotop-vor-t4-06` und `biotop-lage-01`. |
| MP9.2 | 500 | „`BERICHT.md`: Was gebaut wurde, was gemessen wurde, jede Torzeile mit Ergebnis und Verweis auf die Ausgabedatei“ | TEILWEISE | `BERICHT*.md` liegt in 13 von 19 Ordnern (R67). Ohne sind `biotop-lage-01` (läuft), `biotop-phase-4-einstieg-20260921-01`, `biotop-reparatur-01`, `biotop-reparatur-02`, `biotop-vor-t4-06` (läuft) und `biotop-wiedereinstieg-2026-09-20-01`. Alle außer `biotop-lage-01` haben einen `ZWISCHENBERICHT` (R67). |
| MP9.3 | 501 | „`ausgaben/`: die Rohausgaben jeder Messung (Testläufe, Prüfsummen, Protokollauszüge).“ | TEILWEISE | `ausgaben/` liegt in 9 von 19 Ordnern (R67). Die Behebungsrunden `biotop-vor-t4` bis `-05` haben keinen solchen Unterordner. Ob ihre Rohausgaben unter anderem Namen liegen, habe ich nicht geprüft. |
| MP9.4 | 502 | „`werk/`: das Übungswerk bzw. das gehobene Werk als Archiv (ohne `.env*`, `node_modules`, `dist`, `coverage`).“ | TEILWEISE | `werk/` liegt in 8 von 19 Ordnern (R67): Phasen 1 bis 3 mit Nachläufen, Vorbedingung 1, T3 und Gesamtstand. Es fehlt unter anderem in den Behebungsrunden, die kein Werk heben. Ob die Archive die Ausschlüsse einhalten, habe ich nicht geprüft. |
| MP9.5 | 503 | „`biotop/`: der Stand des Biotops als Archiv (gleiche Ausschlüsse) mit Prüfsumme.“ | TEILWEISE | `biotop/` liegt in 9 von 19 Ordnern (R67). Die Behebungsrunden haben keinen, sie nennen Commits (`R5B` Z. 3). |
| MP9.6 | 504 | „`KASSE.md`: alle Modellaufrufe des Auftrags mit Kosten und Kontingentverbrauch.“ | TEILWEISE | `KASSE*.md` liegt in 17 von 19 Ordnern; es fehlt in `biotop-lage-01` und `biotop-vor-t4-06`, die beide laufen (R67). Einen Kontingentverbrauch gibt es nicht, weil kein Kontingent gebucht ist (MP3.14.4). |
| MP9.7 | 506 | „Die Endmeldung im Telegram-Chat enthält die Abholadresse und die Prüfsumme des Ordners. Chat-Claude prüft den Ordner, nicht die Meldung.“ | UNKLAR | Nicht je Auftrag geprüft. Weg zur Klärung: je Abschlussordner die Meldung in `HP` auf ganze Adresse und Prüfsumme durchsehen. `PRUEFSUMME*.txt` liegt in 16 von 19 Ordnern; ohne sind `biotop-lage-01`, `biotop-t3-typescript` und `biotop-vor-t4-06` (R67). |
| MP9.8 | 507 | „Summenpflicht (Fassung 4): Jede Aufschlüsselung im Bericht — Kandidaten nach Status, Ablehnungen nach Grund, Aufrufe nach Zweck, Kosten nach Modell — muss auf die genannte Gesamtzahl aufgehen.“ | UNKLAR | Belegt nur für Phase 3 (Tor 3 Zerlegungen, `P3B` Z. 144–152). Für die Berichte ab dem Nachlauf zu Phase 3 nicht nachgerechnet. Weg: nachrechnen in Teil C `TORE` und Teil F `CHRONIK`. |

## Abschnitt 10 — Was Philipp entscheidet

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP10.1 | 513 | „Budget je Lauf (Vorschlag für Phasen 1–3 zusammen: 150 €; Phase 4 gesondert nach Kostenvoranschlag der Kasse).“ | TEILWEISE | Philipp setzt Budgets je Auftrag (`PH` Z. 20, Z. 371; die Beträge stehen in `CHRONIK`). Einen Kostenvoranschlag der Kasse vor Phase 4 habe ich in `PH` NICHT GEFUNDEN. Zur Budgetbestätigung je Lauf siehe MP6.4. |
| MP10.2 | 514 | „Welche Schnellmodelle über OpenRouter für die Masse (mindestens zwei Anbieter).“ | BELEGT | Philipp am 18.09.: „OpenRouter mit zwei verschiedenen Herstellern für die Masse“ (`PH` Z. 20). Die Modellwahl am Katalog steht in `P2B` Z. 26 und ist in `PH` Z. 44 vermerkt. |
| MP10.3 | 515 | „Die Stelle des Abschlussordners im Prüfkanal.“ | BELEGT | Philipp gibt den Ordner je Auftrag vor, etwa „Abschlussordner unter laeufe/biotop-phase-1/“ (`PH` Z. 20) oder „Abschlussordner laeufe/biotop-t3-typescript/“ (`PH` Z. 371). |
| MP10.4 | 516 | „Die Verfassung jedes Werks und das Maß jedes Laufs — bei Vorlage.“ | TEILWEISE | Verfassungen: MP3.3.1. Maß: MP3.5.17; dort fehlt Philipps Bestätigung für 4 Läufe. |

## Anhänge A und B — Verfassungen der Übungswerke

Die einzelnen Verfassungssätze sind keine eigenen Einträge. Aufgenommen sind nur ihre Geltung und die Stellen mit prüfbarem Beleg. Der Wortlaut und der Vergleich mit den Dateien stehen in `VERFASSUNGEN` (FK22).

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MPA.1 | 522 | „Gilt für Lauf 3 und alle weiteren Läufe am Übungswerk. Ändert nur Philipp.“ | BELEGT | `verfassungen/lagerhaus.md` hat die SHA-256 `326e2616…` und ist gleich der Kopie im Zweig VB1 (R99). `lagerhaus.regeln.json` unterscheidet sich in den Bytes vom Zweig VB1, hat aber keinen abweichenden Schlüssel oder Wert (R99, R103). |
| MPB.1 | 538 | „von Chat-Claude bestätigt (19.09.2026, am Nachlaufbericht Abschnitt 9; Prüfsumme der Datei `0ce7f865…`, Regeln `bce33200…`). Gilt für alle Läufe am Übungswerk `logmuehle`. Ändert nur Philipp.“ | BELEGT | Die SHA-256 von `verfassungen/logmuehle.md` beginnt mit `0ce7f865`, die von `logmuehle.regeln.json` mit `bce33200` (R99). |
| MPB.2 | 547 | „Satz 6 ist mechanisch verdrahtet (`verbotene_muster`), Satz 2 über die Tauschregel (`laufzeit_faktor_bei_sicherheitsgewinn: 3.0`).“ | BELEGT | `verbotene_muster` hat 5 Einträge, `tausch.laufzeit_faktor_bei_sicherheitsgewinn` ist 3.0 (R99). |

*Fortsetzung in Teil 4: UNKLAR-Liste für FK47, Lücken, Widersprüche, Prüfbeleg.*
