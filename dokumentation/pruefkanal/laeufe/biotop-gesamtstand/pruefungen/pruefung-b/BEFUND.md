# Biotop – kritische Teilprüfung B gegen Masterprompt Fassung 6

## Ergebnis

Substantielle Mechanik ist gebaut und historisch benutzt; der aktuelle Schwerpunktstand ist gegenüber F6 nicht vollständig konform. Besonders Start-Gates, Norm-Eichung, Status-/Bestandsisolation, Gedächtnislesepfade und spätere C-Integration bleiben mangelhaft.

**25 Befunde** (19 hoch, 6 mittel). Das ist eine Befundliste, **keine Tor-/Phasenwertung**.

**Wesentliche Ergebnisse:**
- Der Pflichtvorspann „Generation minus eins“ ist als Organe und Prüfscripts gebaut, aber kein verbindliches Start-Gate des produktiven CLI-Laufs (B-02/B-03).
- Die Norm-Eichprobe meldete historisch grün aus dem falschen Grund; aktuell prüft sie einen nicht gelieferten Rückgabeschlüssel (B-04).
- Satz 2 ist für den Anklägerwechsel unter Lauf 22 und den Wechsel der Ansagehistorie unter Lauf 23 durch reale Protokollzeiten/Payloads belegt – nicht nur durch Commits (B-01).
- A/B kamen nach dem historischen v6-Ausgang; C ist eine spätere, als F7 bezeichnete Erweiterung. Ihr vorhandener Pfadnachweis ersetzt keinen natürlichen Laufnachweis. C kann die eigene frische Ansage als Doppelung sperren (B-11).
- Drei Gedächtnistabellen sind nicht bloß Platzhalter, ihre Lesewirkung und die Abtrennung von Simulation sind jedoch unvollständig (B-13 bis B-15).
- Das alte Oberfläche-Prüfscript überschreibt das reale Konto und stellt Konto/Tokens nicht zurück. Es wurde nur gelesen, nicht ausgeführt (B-22).

## Beweis- und Ausführungsgrenze

- Repository: `/root/biotop`; HEAD `b42dc941e7fcb66632ba6a0e13b8df106a270a31`; Arbeitsbaum erneut sauber gelesen.
- Soll: `/root/.hermes/cache/documents/doc_8d640daa6c3c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md` (470 Zeilen).
- DB: `/root/gesamtstand-01/bestand.db` ausschließlich `mode=ro&immutable=1`; unveränderte SHA-256 `711b2bbdca478f7f0de941a88cc51e72c46c9c7a20a3a908065f42861520fe14`.
- Aktueller Kopienbestand: 25 Laufzeilen, 4070 Kassenzeilen, 16030 Protokollzeilen. Historischer Bestand, kein heutiger Lauf.
- Keine Repository-/DB-Änderungen, keine Biotop-Imports, keine Tests oder produktive CLI, kein HTTP-/OpenRouter-/zusätzlicher Modellaufruf und keine Installation durch diese Prüfung.
- Der übergebene aktuelle Bestandsbefund nennt **0 Biotop-Prozesse; Web nicht gestartet**. Ich habe keinen solchen Prozess gestartet. Datenbankstatus wie `bereit` oder ein historisch verbliebenes `laeuft` beweist keinen Prozessbetrieb.
- „Historisch belegt“ heißt Protokollnummer + Zeit + Payload; alle übrigen Defektfolgen sind **gelesen, nicht neu ausgeführt**. Die Kernprüfung von Messgerät/Kasse/Sandbox wird separat geführt.
- Das Aufrufprotokoll enthält Metadaten, aber keine vollständigen Modellprompts. Die genaue B-Vorlage lässt sich daraus nicht rückwirkend rekonstruieren.
- Das user-owned Skill `biotop-phase-bauen` wurde nicht verändert; ältere dortige Phasenangaben wurden nicht zum Sollmaßstab dieser v6-Prüfung gemacht.

## Quellstand und Historie auseinanderhalten

- Historischer v6-Ausgang: `7c73d403c18755dda26655c78ac7290c446d9f45`. Darin fehlen `_ansage`, `aufnahmesperre` und `fremd_min` (Git-Blobs lesend geprüft).
- A/B-Folgecommit: `7bc112beac11110e22047ccaeaf7c4981efdaafe`; C-Folgecommit: `19498ad5808c5b63c534a8bac844a6824fe306a2`. Commitzeit ist nur Indiz für Entstehung, nicht erster Ausführungspunkt.
- **Nexus fehlt nicht.** Er liegt in `biotop/lauf.py` (`_generation_koerper`, `_verhandeln`, `freigabe`), nicht in einer Datei namens `nexus.py`.
- `pruefung/funde_neubewerten.py` ist ein weiter vorhandenes historisches Prüfschema; der aktuelle Organpfad liegt in `biotop/organe/fundpruefung.py`. Die beiden werden unten ausdrücklich getrennt.

## Zusatzfrage Satz 2: weiterverwendete IDs 22/23

Alle folgenden Zeiten sind UTC (`Z`); die JSON-Belege bewahren die originalen `+00:00`-Zeitstempel.

| Lauf | Früher Abschnitt | Später Abschnitt | Belastbare Aussage |
|---|---|---|---|
| 22 | Freeze #12517 20:58:03.553; Gen 1–4 bis #13232 21:22:12.328, keine Ansageereignisse | Gen 5 #14248 22:46:02.011; A-Ansage #14305 22:46:45.372, `ausgefuehrt=true` | Derselbe Lauf und Ausgang 0, aber geänderter Anklägerablauf; kein neuer Freeze dazwischen. |
| 23 | #13398 22:22:14.925 und #13442 22:23:21.047: `extern_filtern\|raises:ValueError` zweimal ausgeführt, `bisherige=0`; auch weitere Wiederholungen | Gen 5 #14066 22:37:19.798; #14086 meldet Vorrat 3; #14160 22:39:02.179 sperrt die bekannte `nach_zeit\|raises:FilterFehler` mit Vorrat 8 | Nicht bloß erstmaliger Einbau vor Gen 1, sondern geänderte Historien-/Sperrwirkung zwischen Generationen desselben Laufs. |

**Kasse bestätigt die zeitliche Trennung**, nicht allein die Ursache:
| Lauf / Abschnitt | Kassenzeilen | ID-Spanne | Zeitspanne UTC |
|---|---:|---|---|
| 22 / vor_A_B | 189 | 3204–3411 | 2026-09-19T20:57:43.944+00:00 bis 2026-09-19T21:32:31.038+00:00 |
| 22 / nach_A_B | 44 | 3651–3694 | 2026-09-19T22:45:33.314+00:00 bis 2026-09-19T22:53:52.942+00:00 |
| 23 / vor_A_B | 18 | 3412–3429 | 2026-09-19T21:32:58.296+00:00 bis 2026-09-19T21:33:52.526+00:00 |
| 23 / nach_A_B | 221 | 3430–3650 | 2026-09-19T22:21:04.659+00:00 bis 2026-09-19T22:39:47.646+00:00 |

Die späteren 44 Kassenzeilen von Lauf 22 enthalten auch den Mechaniknachgang nach der Sättigung; sie sind nicht sämtlich Generation-5-Aufrufe. Lauf 23 hat vor dem ersten normalen Generationsstart bereits 18 ältere Aufnahme-/Kartierungs-/Mentoraufrufe. **Der stärkere Satz-2-Beleg liegt in den Generation-/Ansagepayloads, nicht in diesen Summen.** B selbst ist über Quellstand und Mentor-Ausgang, nicht über gespeicherte Vorlagentexte belegbar.

## Sechs Grundsätze 2a – ausdrücklich geprüft

| Grundsatz / Sollzeile | Urteil | Konkrete Begründung |
|---|---|---|
| 2a.1 / MP6:103 | verletzt / unvollstaendig | Aktuelle Neubewertung konserviert unbelegte offene Funde; Aegis prüft Existenz einer Kennung, nicht deren inhaltliche Tragfähigkeit. Alte Norm→Fund-Logik separat historisch bezeichnet. (B-07, B-08, B-09, B-10) |
| 2a.2 / MP6:104 | teilweise erfuellt | Benannter CLI-Abbruch ist vorhanden. Pflichtvorspann besitzt keinen verbindlichen CLI-Startpfad; HTTP-Abbruch ist defekt. Keine Behauptung, abbrechen fehle insgesamt. (B-02, B-03, B-21) |
| 2a.3 / MP6:105 | im gelesenen Organaufbau erfuellt, Gesamtfreigabe ausstehend | eichung sammelt fünf getrennte messgeraet.messen-Aufrufe und übergibt diese Werte an streuung; ebene!=zwischen wird dort abgewiesen. Damit ist die Schichtung zwischen Messungen gebaut. Grenzfälle der numerischen Ableitung und Messgeräteintegrität prüft der andere Kernprüfer; hier kein Test und keine neue Messung. Die Einbindung/Sperrwirkung ist hiervon getrennt mangelhaft. (B-02, B-03) |
| 2a.4 / MP6:106 | verletzt | Probenreste können den normalen Immun-/Ansagevorrat verändern. Historisches Web-Prüfscript ersetzt das echte Konto und lässt Tokens stehen. Die dokumentierte Archivierungs-Miträumung ist historisch und wurde teilweise zurückgenommen. (B-06, B-12, B-22) |
| 2a.5 / MP6:107 | teilweise erfuellt, relevante Ableitungsdifferenzen | Projektgedächtnis-Nachprüfung verwendet mittlerweile zentrale Ableitungen; Fundpruefung teilt _nennt_vertrag. Ausführungs-/Absturzklassifikation und Altscript-Regex weichen aber von Aegis ab. (B-07, B-08, B-09) |
| 2a.6 / MP6:108 | teilweise erfuellt, mehrfach durchbrochen | ist_probe-Sperren der drei Gedächtnisse, Behauptungsschlüssel und ausdrücklicher tragender_pfad sind vorhanden. Eichproben lesen aber einen falschen Schlüssel bzw. Textgründe, Entropie filtert am Namen, C verwechselt eigene Ansage und vorhandenen Test, der Eichgegenstand wird auf einen Datei-Hash reduziert. (B-04, B-05, B-06, B-10, B-11, B-24, B-25) |

## Gebaut versus historisch ausgeführt

### Nexus / Freigabe / Verhandlung
- **Gebaut:** Implementiert in lauf.py, nicht als nexus.py. Vollständiges Messen, Auswahl, Vorlage, Freigabe und Nachbaraufrufe sind reale Funktionen.
- **Historisch:** 116 generation.ergebnis, 48 freigabe.frei, 49 verhandlung.begonnen, 32 verhandlung.paar, 8 verhandlung.bestanden, 41 verhandlung.gescheitert. Kein freigabe.abgelehnt.
- **Grenze:** Ereigniszählungen, keine neu ausgeführten Funktionsprüfungen; Verhandlung.bestanden ist nicht automatisch Annahme.

### Aegis / A / C
- **Gebaut:** Angriff, Testausführung, Normklassifikation, Ansagesperre A; später Aufnahmesperre C.
- **Historisch:** 2608 aegis.urteil; 90 aegis.ansage. C: 6 immun.aufnahme_geprueft-Ereignisse insgesamt; Lauf 25 hat vor gestellten Pfadproben 0. Frühe C-Mechanikereignisse wurden vor Einbau des Aufrufzählers protokolliert.
- **Grenze:** A fehlt im ursprünglichen v6-Quellstand; C bezeichnet sich als F7. Gestellte K2680-Pfade sind nicht natürlicher Modellbetrieb.

### Genesis / Nischen
- **Gebaut:** Vier Nischen, je zwei verschiedene Hersteller per Thompson-Auswahl; Elite wird gespeichert und im nächsten Schwarm-Prompt gezeigt.
- **Historisch:** 2633 schwarm.kandidat- und 1168 bandit.wahl-Ereignisse.
- **Grenze:** Kandidatenereignisse sind nicht gleich aktueller Kandidatentabellenzahl; direkte Proben-/Nachbarinserts existieren. Bandit-Erfolg ist Überleben, nicht Annahme.

### Drei Gedächtnisse
- **Gebaut:** Dauerhafte Tabellen; Projektwiederholung als Sperre; Artmuster-Erzeugung; Naive-Bayes-Geschmacksvorhersage; drei Probe-Eintrittssperren.
- **Historisch:** Aktueller Bestand: 686 Projekt-, 699 Art-, 35 Geschmackszeilen; letztere 15 Hermes-Freigabezeilen und 20 P1-Simulationszeilen. 128 gedaechtnis.wiederholung; 20 Musterfehler.
- **Grenze:** Keine direkten ist_probe-Treffer in diesen drei Tabellen bei der gelesenen Zuordnung; das beweist nicht die Sauberkeit des separaten Immunsystems. Art-/Geschmack-Lesewirkung ist unvollständig.

### Mentor / Jury / Entropie
- **Gebaut:** Richtungserzeugung/-wahl, Dreierjury und Sättigungsberechnung sind vorhanden.
- **Historisch:** 13 Mentor-Datensätze und 11 Wahlereignisse; 7 Juryzeilen, davon 4 mit Nicht-Probenpaaren und 3 mit Proben; 43 Entropieereignisse und 6 Sättigungsmeldungen.
- **Grenze:** Mechanikproben der Jury sind getrennt von natürlichen Gleichständen. Kein aktueller Prozessbetrieb aus diesen historischen Zahlen ableitbar.

### Eichung / Eichproben / Eichgegenstand
- **Gebaut:** Eigene Organfunktionen und separate Scripts; nicht automatisch verpflichtend in mass/gen0/generation.
- **Historisch:** 10 eichung.rauschmessung; 17 Eichproben-Einzelereignisse und 4 Abschlüsse; 16 Versiegelungs-, 3 Wegfall- und 1 Wartesignale. Im aktuellen DB-Stand 25 Eichzeilen und 2 Siegelzeilen.
- **Grenze:** Append-only-Protokoll und später bereinigter Tabellenbestand sind verschiedene Bezugsgrößen. Vier grüne Normproben sind wegen B-04 kein bestandener Normnachweis.

### Fund-Neubewertung
- **Gebaut:** fundpruefung mit Ausführung + Verweisprüfung; alte separate Neubewertungs-/Übernahmescripte bleiben vorhanden.
- **Historisch:** 6 immun.neubewertet-Ereignisse: ein Altscript-kompatibles Payloadschema, fünf Organ-Payloads; darunter ein Organereignis mit 0 geprüften Funden.
- **Grenze:** Eine Nullobjekt-Meldung ist kein Nachweis der Klassifikation. Historisches Norm→offen bei #12472 nicht als heutige aktive Logik ausgeben.

### CLI / Dienst / Oberfläche
- **Gebaut:** CLI-Befehle; HTTP-Authentisierung und Routen; HTML-Dashboard samt Freigabe/Richtungswahl.
- **Historisch:** Anmelde-/Tokenereignisse belegen historische API-Nutzung. Quelltext des Tor3-Prüfscripts vorhanden.
- **Grenze:** Keine neue CLI-, HTTP- oder Browserprüfung. Laut übergebenem Bestandsbefund laufen derzeit weder Biotop-Prozess noch Web-Dienst. Codebau ist kein heutiger Betrieb.

## Einzelbefunde

### B-01 · HOCH · Satz 2: Anklägerablauf wurde unter weiterbenutzten Lauf-IDs geändert
**Stand:** `historische_Ausfuehrung_und_aktuelle_Schutzluecke` · **Soll:** MP6:86, MP6:195

**Quelle:** `/root/biotop/biotop/lauf.py:133–166`; `/root/biotop/biotop/organe/aegis.py:302–331`; `/root/biotop/biotop/organe/aegis.py:392–420`

**Mechanik:** Es gibt beim Start einer Generation keinen Abgleich einer eingefrorenen Messgeräte-/Anklägerrevision. Für Lauf 22 belegen die Ereignisse Generationen 1–4 ohne Ansagephase, danach Generation 5 mit Ansage unter derselben ID und demselben Ausgang 0. In Lauf 23 wurde die zunächst unvollständige Ansagesperre zwischen Generation 4 und 5 wirksam geändert: vorher wiederholte Ansagen trotz bisherige=0; danach Vorrat aus bisherigen Ansagen und echte Sperrung. Es geht um den Anklägerablauf, nicht um eine bloße Commit-Zeit.

**Folge:** Die Kurven und Ablehnungen dieser IDs sind kein Nachweis eines durchgehend unveränderten Messgeräts. A/B dürfen weder dem ursprünglichen v6-Commit noch den gesamten IDs 22/23 pauschal zugeschrieben werden.

**Ausführungsbeleg / Grenze:** Historisch belegt, nicht heute ausgeführt: Lauf 22 Gen 4 Ende #13232 2026-09-19T21:22:12.328Z; Gen 5 Start #14248 22:46:02.011Z; erste A-Ansage #14305 22:46:45.372Z. Nur ein mass.eingefroren (#12517). Lauf 23 #13398 und #13442 nennen extern_filtern|raises:ValueError zweimal ausgefuehrt=true, bisherige=0; #13773 wiederholt nach_zeit|raises:FilterFehler; #14086 nennt bisherige=3, #14160 sperrt nach_zeit|raises:FilterFehler mit bisherige=8. Gen 5 beginnt unter derselben ID #14066. B-spezifische Vorlage ist im Aufrufprotokoll nicht gespeichert: verbesserte Mentor-Verweise allein beweisen die genaue Vorlage nicht.

### B-02 · HOCH · Generation minus eins ist gebaut, aber kein verpflichtender Laufpfad
**Stand:** `aktuelle_Logik` · **Soll:** MP6:159–169, MP6:104, MP6:222

**Quelle:** `/root/biotop/biotop/lauf.py:80–115`; `/root/biotop/biotop/lauf.py:133–166`; `/root/biotop/biotop/lauf.py:557–616`; `/root/biotop/biotop/__main__.py:34–61`; `/root/biotop/pruefung/vorspann.py:16–55`

**Mechanik:** Die produktiven Befehle mass, gen0 und generation rufen weder eichung.rauschmessung noch eichproben.proben, eichgegenstand.sichern oder fundpruefung.bewerten auf und prüfen keinen Eichabschluss. mass setzt unmittelbar bereit und schreibt Generation 0. vorspann.py ist ein separat aufrufbares Prüfschema; es erwartet schon einen eingefrorenen Lauf, führt Fund-Neubewertung vor den vier Proben aus (umgekehrt zu F6) und druckt Lauf startet, ohne den Laufstatus zu sperren oder Eichwerte in laeufe.mass zu übernehmen. Ein benannter CLI-Befehl für den gesamten obligatorischen Vorspann fehlt.

**Folge:** Eine lauf_startet=False-Meldung bzw. eine bestandene Einzelprobe ist kein verbindliches Start-Gate. Proben und Neubewertung können ausgelassen werden; Generation 0 und normale Generationen bleiben erreichbar.

**Ausführungsbeleg / Grenze:** Eichung wurde historisch ausgeführt, aber über Prüfaufrufe: #12517 friert Lauf 22 ein, erst danach #12518 Rauschmessung, #12520 Neubewertung und #12544 Probenabschluss. Lauf 23 besitzt einen Freeze und Generationen, aber keinen ihm zugeordneten Eichprobenabschluss. Separate Organereignisse beweisen die Implementierung der Hauptpfadpflicht nicht.

### B-03 · HOCH · Bereichssperre und Maschinen-Vorbehalt erreichen die Generation nicht
**Stand:** `aktuelle_Logik` · **Soll:** MP6:162, MP6:104

**Quelle:** `/root/biotop/biotop/organe/eichung.py:153–217`; `/root/biotop/biotop/lauf.py:147–166`; `/root/biotop/biotop/lauf.py:203–212`

**Mechanik:** eichung erzeugt toleranz, gesperrt und bei Maschinenserie vorbehalt_zeitraum. generation arbeitet jedoch alle mass.bereiche ab; _generation_koerper hat keinen Filter für gesperrte Bereiche. Die Kalibrierung wird weder geladen noch an aktuelle Messungen gekoppelt. Die detaillierte Deutung steht nur im Rückgabeobjekt; das Protokoll der Rauschmessung speichert aus dem Bereichsobjekt nur eine reduzierte Auswahl ohne serie_zeitraum/serie_deutung/vorbehalt_zeitraum.

**Folge:** Ein gesperrter Bereich kann weiterhin Kandidaten erhalten. Der geforderte eigene Vorbehalt an allen betroffenen Laufzeitmessungen ist nicht automatisch wirksam.

**Ausführungsbeleg / Grenze:** Organ-Meldungen und Sperren liegen in der DB vor; daraus folgt nicht, dass eine produktive Generation die Sperre respektiert hat. Kein solcher positiver Pfadnachweis festgestellt.

### B-04 · HOCH · Norm-Eichprobe besteht wegen falschem Rückgabeschlüssel ohne Normnachweis
**Stand:** `aktuelle_Logik` · **Soll:** MP6:90, MP6:108, MP6:169, MP6:197

**Quelle:** `/root/biotop/biotop/organe/eichproben.py:115–124`; `/root/biotop/biotop/organe/eichproben.py:157–169`; `/root/biotop/biotop/organe/eichproben.py:185–191`; `/root/biotop/biotop/organe/aegis.py:474–482`

**Mechanik:** Die Prüflambda liest u[masse], Aegis liefert aber u[mass]. Damit werden Zuwachs und Testbestand durch leere Defaults ersetzt: int(... or 0)==0 und Datei nicht in [] sind unabhängig vom tatsächlichen Anklägerurteil wahr. Zusätzlich importiert die Probe ein erst im Kandidaten angelegtes Modul; sie erzeugt am Ausgang einen Import-/Sammlungsfehler und nicht sicher eine gerichtete Assertion. Der offene Normeintrag und der echte Werkbestand werden nicht geprüft.

**Folge:** Grün für Norm ist hier eine Scheinaussage; ein falscher oder gar nicht erreichter Normpfad kann die Vorbedingung passieren.

**Ausführungsbeleg / Grenze:** Historisch konkret: #12538 (Lauf 22, K2083, 2026-09-19T20:59:09.321Z) bestanden=true, norm=[], zuwachs=None; wirklicher Grund: Pareto verletzt: preise.tote_funktionen: 0 → 1. Gleichartig #12440/#12465. #12418 war sogar bereits an einer Verfassungsvorprüfung gescheitert und meldete dennoch bestanden=true.

### B-05 · HOCH · Weitere Eichproben prüfen Ersatzgegenstände oder falsche Ablehnungsgründe
**Stand:** `aktuelle_Logik` · **Soll:** MP6:108, MP6:169, MP6:203

**Quelle:** `/root/biotop/biotop/organe/eichproben.py:157–177`; `/root/biotop/biotop/organe/eichproben.py:193–215`

**Mechanik:** Nebenwirkung wird als B schneller/A kaputt kommentiert, aber tatsächlich wird nur A lahmgelegt; die Bedingung verlangt lediglich Ablehnung und A als Text im Grund. Vertrag wird direkt durch aegis.pruefen geprüft, nicht durch Nexus-Verhandlung; jedes Nicht-ueberlebt genügt. Die Konsumentenergänzung wird trotz AST-Auswahl per quelle.replace("def <name>",...) eingefügt und nur als zusätzliche Funktion definiert, ohne deren Benutzung sicherzustellen.

**Folge:** Diese Proben beweisen weder den Bereichstausch noch den vollständigen Vertrags-Nachbarpfad; syntaktische/anderweitige Ablehnungen können die Torzeile fälschlich grün machen.

**Ausführungsbeleg / Grenze:** Vier Eichprobenabschlüsse und Einzelurteile sind historisch vorhanden; eine solche Ausgabe ist kein Ersatz für die in F6 geforderten Gründe. Kein neuer Probelauf durchgeführt.

### B-06 · HOCH · Proben werden aus drei Gedächtnissen gefiltert, nicht aus allen wirksamen Prüfbeständen
**Stand:** `aktuelle_Logik` · **Soll:** MP6:106, MP6:219

**Quelle:** `/root/biotop/biotop/organe/eichproben.py:128–138`; `/root/biotop/biotop/organe/eichproben.py:157–223`; `/root/biotop/biotop/organe/aegis.py:631–668`; `/root/biotop/biotop/organe/aegis.py:302–331`; `/root/biotop/pruefung/lauf25_pfadnachweis.py:79–102`; `/root/biotop/pruefung/nachgang_n13_n14.py:103–121`

**Mechanik:** Die Probenerzeuger setzen ist_probe, Aegis schreibt neue Fund-/Normtests und Ansagen aber ohne entsprechende Bereichsisolierung in den normalen Immunsystem-/Protokollvorrat. Die drei Gedächtnis-Eintrittsstellen schützen ihre Tabellen, nicht die Aegis-Aufnahmestellen. Eichproben räumen diese Nebenwirkungen nicht in finally zurück. Wiederaufnahmen aus anderen Werken kopieren solche Funde ebenfalls.

**Folge:** Prüfmaterial kann spätere Kandidaten messen, Angriffe sperren oder über Werk-Kopien weiterwandern, auch wenn die drei Gedächtnistabellen inzwischen sauber sind.

**Ausführungsbeleg / Grenze:** DB-Join findet 21 noch vorhandene Immunsystem-Einträge mit direkt zuordenbarem ist_probe=1-Kandidaten. Für Lauf 22 stehen z.B. IDs 285–287 (norm_k2081_bericht, aegis_k2082_bericht, norm_k2082_bericht) weiterhin im Bestand. Die drei eigentlichen Gedächtnistabellen haben in der getrennten direkten Probe-Zuordnung keine Treffer. C-Pfadproben #16010–16030 sind ausdrücklich gestellte Fälle, nicht natürlicher Schwarmbetrieb.

### B-07 · HOCH · Fund-Neubewertung konserviert unbegründete offene Funde
**Stand:** `aktuelle_Logik` · **Soll:** MP6:103, MP6:107, MP6:222

**Quelle:** `/root/biotop/biotop/organe/fundpruefung.py:55–77`

**Mechanik:** Für einen am neuen Ausgang fallenden Test ohne Werkabsturz und ohne gültigen Verweis übernimmt Zeile 74 bei bisherigem status=offen wieder offen. F6 Zeile 222 verlangt in genau diesem Fall Norm. Das Vermeiden der früheren Norm→Fund-Beförderung ist eine sinnvolle Korrektur, die neue Logik korrigiert aber einen bereits falsch offenen Fund nicht.

**Folge:** Eine alte Fehlklassifikation wird trotz mechanischer Nachmessung in den neuen Testbestand übernommen und kann echte Behebungen blockieren.

**Ausführungsbeleg / Grenze:** Die historischen Neubewertungen sind belegt (#12472, #12473, #14477, #15273). Die #12472-Ausgabe mit Norm→offen ist ein früherer Stand, NICHT die heutige Zeile 74: der aktuelle Stand konserviert und befördert Normtests ohne Nachweis nicht. Aus dem reduzierten Protokoll ist die Zahl heutiger offener Fälle ohne Nachweis nicht sicher ableitbar.

### B-08 · HOCH · Neubewertung prüft Absturz und Erfolg anders als Aegis
**Stand:** `aktuelle_Logik` · **Soll:** MP6:103, MP6:107, MP6:108, MP6:222

**Quelle:** `/root/biotop/biotop/organe/fundpruefung.py:34–43`; `/root/biotop/biotop/organe/fundpruefung.py:55–77`; `/root/biotop/biotop/organe/aegis.py:75–107`; `/root/biotop/biotop/organe/aegis.py:591–605`

**Mechanik:** Das neue Organ teilt zwar _nennt_vertrag mit Aegis, bestimmt besteht/Absturz aber durch Substrings in stdout+stderr für die gesamte Testdatei. Es prüft weder Returncode noch JUnit-Fehlerort im Werk. Ein ImportError oder Test-eigener TypeError kann als Werkabsturz zählen; ein AssertionError irgendwo kann umgekehrt einen zusätzlichen Werkabsturz verdecken. Mehrere Tests pro Datei erhalten gemeinsam einen Status und any(Verweis) reicht für die ganze Datei.

**Folge:** Nachrechnung und geprüftes Organ besitzen weiterhin unterschiedliche Ableitungen; ein unbrauchbarer Test kann als Fund weitergeführt werden. Ein geteiltes Verweis-Prädikat allein erfüllt 2a5 nicht vollständig.

**Ausführungsbeleg / Grenze:** Gelesen, nicht ausgeführt; kein einzelner Fehlfall aus dem DB-Protokoll zugeordnet.

### B-09 · MITTEL · Altes funde_neubewerten.py bleibt eine abweichende historische Prüflogik
**Stand:** `historisches_aufrufbares_Pruefscript` · **Soll:** MP6:103, MP6:106, MP6:107, MP6:108, MP6:197, MP6:222

**Quelle:** `/root/biotop/pruefung/funde_neubewerten.py:17–43`; `/root/biotop/biotop/organe/fundpruefung.py:55–74`; `/root/biotop/biotop/organe/aegis.py:185–227`

**Mechanik:** Das Altscript scannt nur status=offen, sucht Verweise mit einem eigenen Regex irgendwo im gesamten Code und löst keine Vertrags-/Satzkennung auf. Sein Regex akzeptiert z.B. bloßen Vertragstext außerhalb des Testnamens/Docstrings, kann nicht vorhandene Kennungen anerkennen und kennt nur eine enge Schreibweise für Verfassung. Erfolg/Absturz kommen aus Ausgabetext statt Fehlerort. Mit --schreiben ändert es normale Immunsystemzeilen dauerhaft; keine Bestandskopie oder Rücknahme. Es ist kein Aufrufziel von CLI mass/generation und nicht die heutige Fundpruefung.

**Folge:** Alte Ausgaben dieses Scripts dürfen nicht als Nachweis der aktuellen gemeinsamen Ableitung zitiert werden; erneutes Aufrufen mit --schreiben wäre eine Bestandsmigration, keine neutrale Prüfung.

**Ausführungsbeleg / Grenze:** #11417 am 2026-09-19T15:39:16.728Z protokolliert sechs Änderungen mit dem exakt vom Altscript erzeugten Payloadschema anzahl/namen/regel. Das belegt den historischen Neubewertungsvorgang, nicht forensisch den Prozessnamen des Aufrufers. Spätere Organereignisse verwenden geprueft/kammerlaeufe/aenderungen. Script wurde in dieser Prüfung nur gelesen.

### B-10 · HOCH · Expliziter Vertragsname wird mit inhaltlichem Recht gleichgesetzt
**Stand:** `aktuelle_Logik` · **Soll:** MP6:103, MP6:108, MP6:197

**Quelle:** `/root/biotop/biotop/organe/aegis.py:185–227`; `/root/biotop/biotop/organe/aegis.py:591–607`; `/root/biotop/pruefung/nachgang_n13_n14.py:70–93`

**Mechanik:** _nennt_vertrag verifiziert nur, dass eine genannte Datei, ein Testname oder eine Satznummer existiert, und liefert True. Es prüft nicht, dass deren Zusicherung die Erwartung des neuen Tests trägt. Das N14-Script fordert unter vorhandenen Vertragskennungen preis_fuer(...) >= 999.0 bzw. anzahl() < -1, während der Kandidat nur einen Kommentar ergänzt. Ein existierender Name verwandelt dadurch eine frei erfundene Erwartung in einen Fund.

**Folge:** 2a1 bleibt materiell offen: ausdrücklich benannt ist notwendig, aber nicht hinreichend für „Vertrag weist das Verhalten als falsch aus“. Dies ist kein natürlich gefundener Fehler.

**Ausführungsbeleg / Grenze:** Der gestellte N14-Pfad ist historisch belegt: #16025 noch Norm; #16026 bis #16030 anschließend Fundpfad mit Modellkennzeichnung hermes/gestellt-n14, immun.gefunden #16029. #16028 führt den tatsächlich berechneten grünen Schlüssel anzahl|Lt:name (nicht die Kommentarbehauptung Lt:zahl). Diese Prüfung hat den Pfad nicht erneut ausgeführt.

### B-11 · HOCH · Späteres C sperrt die eigene frische Ansage als vermeintliche Doppelung
**Stand:** `spaetere_C_Erweiterung_aktuelle_Logik` · **Soll:** MP6:91, MP6:194, MP6:195, MP6:221

**Quelle:** `/root/biotop/biotop/organe/aegis.py:325–331`; `/root/biotop/biotop/organe/aegis.py:394–420`; `/root/biotop/biotop/organe/aegis.py:442–462`; `/root/biotop/biotop/organe/aegis.py:619–668`; `/root/biotop/pruefung/lauf25_pfadnachweis.py:95–102`; `/root/biotop/pruefung/nachgang_n13_n14.py:115–121`

**Mechanik:** A schreibt die neue Ansage vor dem Angriff als ausgefuehrt=true ins Protokoll. C lädt danach genau diese Protokollansagen in seinen Vorrat und hat weder Kandidatenkennung noch Ausschluss der aktuellen Ansage. Wenn der erste gültige Test tatsächlich die angekündigte Behauptung prüft, liegt sein Schlüssel daher bereits im Vorrat und C weist ihn ab. Neu, aber anders als angesagt, kann dagegen passieren. Die gestellten Pfadproben ersetzen _angriff komplett und schreiben keine echte vorlaufende Ansage; sie prüfen diese Wechselwirkung nicht.

**Folge:** Das als F7 bezeichnete Zusatzteil kann neue bestätigte Fehler trotz Immunisierungspflicht verwerfen. Es darf nicht als bereits vollständig geprüfte Verbesserung des F6-Standes ausgegeben werden.

**Ausführungsbeleg / Grenze:** Nur statischer Integrationsbefund, keine neue Ausführung. Die DB enthält C-Prüfereignisse für Prüfwerk-IDs sowie K2680 in gestellten Pfaden; Lauf 25 selbst hatte vor den Pfadproben keinen normalen C-Aufruf. Die tatsächliche Fehlerrate dieser Selbstsperre ist daraus nicht messbar.

### B-12 · HOCH · Archivierung liegt weiterhin hinter erfolgreicher Generalprobe
**Stand:** `aktuelle_Logik` · **Soll:** MP6:223

**Quelle:** `/root/biotop/biotop/lauf.py:175–190`; `/root/biotop/biotop/lauf.py:274–275`; `/root/biotop/biotop/lauf.py:309–350`; `/root/biotop/biotop/organe/aegis.py:528–529`

**Mechanik:** Der Zähler benutzt zwar alle Generationen, die Archivierungsschleife wird aber nur erreicht, nachdem ein Gesamtkandidat die Generalprobe bestanden hat und ins Werk geschrieben wurde. Frühere returns bei keinem Überlebenden oder Generalprobenfehler umgehen sie. Zusätzlich bleiben in solchen Generationen neu gefundene Tests status=gefunden, während die Archivierung nur offen/offen_norm auswählt.

**Folge:** Am gesättigten Werk ohne angenommene Generation archiviert das Organ weiterhin nicht nach fünf Generationen. Genau die in F6 beschriebene Fehlerklasse besteht als Aufrufstellenfehler fort.

**Ausführungsbeleg / Grenze:** Es gibt genau ein immun.archiviert-Ereignis (#13340), ausdrücklich mechanikpruefung=true, anschließend #13341 Rücknahme zweier mitgetroffener Normtests. In Lauf 22 bestehen noch Probe-Funde aus Gen 0 trotz fünf Folgegenerationen. Das beweist keinen natürlichen Archivierungserfolg.

### B-13 · HOCH · Artgedächtnis und Geschmack werden nicht vor jeder Generation gelesen
**Stand:** `aktuelle_Logik` · **Soll:** MP6:231–234, MP6:183

**Quelle:** `/root/biotop/biotop/organe/genesis.py:87–120`; `/root/biotop/biotop/organe/landkarte.py:230–255`; `/root/biotop/biotop/organe/mentor.py:59–67`; `/root/biotop/biotop/organe/jury.py:38–55`; `/root/biotop/biotop/dienst.py:161–166`

**Mechanik:** Der Schwarmauftrag liest Projektwege, Elite, Verfassung, offene Funde und Mentor-Richtung; er liest weder art_text noch Geschmack. landkarte.sicht ergänzt diese beiden ebenfalls nicht. art_text wird beim expliziten Mentoraufruf gelesen, die Geschmacksvorhersage in der Web-Vorlage/CLI, nicht durch die Jury und nicht im Generationsanfang. Die drei Gedächtnisse sind dauerhaft vorhanden, aber ihre geforderte Lesewirkung ist nicht vollständig verbunden.

**Folge:** Abstrahierte werkübergreifende Muster erreichen den Schwarm nicht als Vorlage; ein fehlender Musterverweis ist daher nicht nur Modellverhalten. Die Geschmacksvorhersage ergänzt die Jury nicht wie gefordert.

**Ausführungsbeleg / Grenze:** Mentor-/Geschmacks-/Juryereignisse sind belegt, aber das Aufrufprotokoll speichert keine vollständigen System-/Nutzerprompts. Der statische Callgraph zeigt die aktuelle Leselücke; es wird nicht behauptet, die Tabellen seien unbenutzt.

### B-14 · MITTEL · Bauteil B unterschreitet die Hälfte und begrenzt fremde Muster vor dem Filter
**Stand:** `aktuelle_Logik` · **Soll:** MP6:233

**Quelle:** `/root/biotop/biotop/organe/gedaechtnis.py:368–392`

**Mechanik:** Bei GEZEIGT=25 nutzt fremd_min die Ganzzahldivision 25//2. Sind ausreichend eigene und fremde Einträge vorhanden, werden 13 eigene und 12 fremde gezeigt: 12/25=48 %, nicht mindestens die Hälfte. Ferner werden zunächst nur die letzten 200 angenommenen Einträge insgesamt gelesen und erst danach fremde Muster herausgefiltert; genügend vorhandene fremde Muster jenseits dieses Fensters können unsichtbar bleiben.

**Folge:** Die Mengenregel von F6 ist auch im später gebauten B nicht für jeden Bestand erfüllt. Die Mindest-vier/fünf-Verweisausgaben eines Mentors beweisen keine korrekte Mindestvorlage.

**Ausführungsbeleg / Grenze:** Deterministische Rechnung am gelesenen Ausdruck, keine Organ-Ausführung. Historisch #14246 enthält drei Richtungen mit werkübergreifendem Verweis; das belegt den Mentor-Ausgang, nicht die 50%-Invariante.

### B-15 · HOCH · Geschmack mischt Simulation und Hermes-Freigaben in Philipps Modell
**Stand:** `aktuelle_Logik` · **Soll:** MP6:234, MP6:264

**Quelle:** `/root/biotop/biotop/organe/gedaechtnis.py:427–439`; `/root/biotop/biotop/organe/gedaechtnis.py:490–511`; `/root/biotop/biotop/lauf.py:416–424`; `/root/biotop/pruefung/tor3_geschmack.py:1–20`; `/root/biotop/biotop/dienst.py:164–166`

**Mechanik:** geschmack_merken speichert jede gewählte Kandidaten-ID einer Freigabe als eigene Entscheidung. geschmack_modell ohne quelle filtert weder nach echter Person noch nach Simulationsherkunft; der Web-Aufruf lässt quelle weg. Die Schwelle len(rows)>=20 zählt Kandidatenzeilen, nicht unabhängige Freigabeentscheidungen. Simulation P1 und Hermes-Vollmacht können so Philipps angeblichen Geschmack trainieren.

**Folge:** Eine sichtbare Geschmacksvorhersage ist kein Nachweis eines aus mindestens zwanzig echten Philipp-Entscheidungen gelernten Modells.

**Ausführungsbeleg / Grenze:** DB: 15 Zeilen quelle=freigabe von Hermes unter Vollmacht, 20 Zeilen quelle=regel_P1 von Simulation P1; keine als solche belegten echten Philipp-Freigaben in dieser Tabelle. Die P1-Prüfung ist als Mechanikversuch zu würdigen, nicht als persönliches Lernen.

### B-16 · MITTEL · Bandit belohnt Überleben statt Annahme und lernt nur pro Lauf
**Stand:** `aktuelle_Logik` · **Soll:** MP6:183

**Quelle:** `/root/biotop/biotop/organe/nischen.py:60–89`; `/root/biotop/biotop/lauf.py:235–246`; `/root/biotop/biotop/organe/genesis.py:116–120`

**Mechanik:** Der Schlüssel der Bandittabelle ist (lauf_id,nische,hersteller), nicht Werkklasse. Gebucht wird unmittelbar nach Aegis mit erfolg=(status==ueberlebt), bevor Bereichswahl, Generalprobe und Freigabe feststehen. Nicht gewählte oder später verworfene Kandidaten bleiben Erfolge; beim neuen Lauf beginnt ein neuer Gewichtsbestand. KEIN VORSCHLAG wird dagegen korrekt nicht gebucht.

**Folge:** Die Herstellergewichtung optimiert einen anderen Erfolg und überträgt keinen Erfahrungsvorteil zwischen gleichartigen Werken. Vier Nischen, verschiedene Hersteller und Eliten sind dennoch echte vorhandene Mechanik.

**Ausführungsbeleg / Grenze:** bandit.wahl und bandit-/eliten-Tabellen belegen historischen Einsatz. Die Bewertung als angenommener Kandidat ist aus der Mechanik nicht ableitbar; es wird nicht behauptet, Bandit fehle.

### B-17 · HOCH · Mentor-Richtung ist weder Startpflicht noch eigener unveränderter Lauf
**Stand:** `aktuelle_Logik` · **Soll:** MP6:142, MP6:143, MP6:144, MP6:202, MP6:257

**Quelle:** `/root/biotop/biotop/lauf.py:140–166`; `/root/biotop/biotop/organe/mentor.py:80–104`; `/root/biotop/biotop/organe/mentor.py:107–135`

**Mechanik:** generation prüft bereit/laeuft und offene Freigabe, nicht eine gewählte Richtung. richtung_text liefert bei fehlender Wahl einen leeren String. waehlen überschreibt laeufe.richtung an derselben ID auch nach Generationen; es legt keinen neuen Lauf und kein neues Maß an. Der Mentor berechnet anzahl_ok, Pflichtfelder und erfundene Verweise, speichert/returniert aber auch negative Prüfergebnisse, ohne zu stoppen.

**Folge:** Arbeiten ohne Richtungswahl und Richtungswechsel im selben Lauf bleiben möglich. Der 3–5-Richtungen-Vertrag ist nur protokollierte Diagnose, kein Gate.

**Ausführungsbeleg / Grenze:** Kein ungültiges Mentor-Richtungsformat in den vorhandenen Protokollprüfungen gefunden. Historisch wurde Lauf 22 jedoch zweimal gewählt (#12548 und #14247) bei identischer Lauf-ID; das ist eine belegte Nachwahl, kein Beweis einer grundlegend anderen Zielrichtung.

### B-18 · HOCH · Verhandlung kann leere Prüfwerte als bestanden werten und mehrere Nachbarn verlieren
**Stand:** `aktuelle_Logik` · **Soll:** MP6:90, MP6:203

**Quelle:** `/root/biotop/biotop/lauf.py:495–550`; `/root/biotop/biotop/organe/aegis.py:474–519`

**Mechanik:** paar_ok verlangt nur leere vertrag_verletzt/pareto_schlechter/grenzen_gerissen. Vorzeitige Aegis-Ablehnungen (z.B. Verfassung, Diff) haben dieselben leeren Defaultfelder und mass=None und können daher als bestandene Verhandlung protokolliert werden. Bei mehreren Nachbarn wird anp jeweils allein als extra_code geprüft; extra.update sammelt Anpassungen, das gesammelte extra wird aber nie erneut übergeben oder endgültig genutzt. Das letzte u2 und dessen _dateien können frühere Nachbaranpassungen ersetzen. Bei einseitig_ok gilt außerdem all(...) über leere ids als Bestätigung ohne tatsächliche Nachbarantwort.

**Folge:** Bestandene Verhandlung bedeutet nicht zwingend bestandene vollständige Anpassung aller Nachbarn; die spätere Gesamtauswahl kann eine nicht vollständig geprüfte Kombination erhalten.

**Ausführungsbeleg / Grenze:** Früherer Cachefehler ist historisch #6488 dokumentiert und in aktuellen Zeilen 529–531 korrigiert. Dieser Bericht gibt den alten Cachefehler nicht als weiterhin vorhandenen Hauptfehler aus. Die hier beschriebenen neuen Randfälle sind nur gelesen, nicht ausgeführt.

### B-19 · HOCH · Nexus hat keinen vollständigen Kombinations-/Wiederholungspfad
**Stand:** `aktuelle_Logik` · **Soll:** MP6:205, MP6:208, MP6:232

**Quelle:** `/root/biotop/biotop/lauf.py:277–313`; `/root/biotop/biotop/lauf.py:248–252`; `/root/biotop/biotop/lauf.py:133–162`; `/root/biotop/biotop/organe/aegis.py:503–517`

**Mechanik:** Das Zusammenführen setzt Dateien mit dateien[p]=inhalt zusammen (letzter Schreiber gewinnt); kollidierende Nachbar- oder Testdateien werden nicht als Konflikt gemeldet. Die Generalprobe misst zwar das ganze Werk und Verträge, ruft aber die Werkverfassung nicht für den finalen Verbund auf. extra_code des Nachbarn liegt in Aegis zudem nicht im an verfassung.mechanisch_pruefen übergebenen dateien-Dict. Bei Generalprobenablehnung werden Kandidaten erst nach den Gedächtnisaufrufen auf abgelehnt gesetzt; Kombination und Grund werden nicht ins Projektgedächtnis eingespeist. Es gibt keinen bis zu dreimaligen Wiederholungszähler für die Generation, sondern MAX(nummer)+1.

**Folge:** Das Ganze wird tatsächlich gemessen, aber nicht mit dem vollständigen geforderten Verfassungs-/Lern-/Retry-Protokoll. Nexus ist vorhanden in lauf.py, nicht fehlend wegen fehlender nexus.py-Datei.

**Ausführungsbeleg / Grenze:** 116 generation.ergebnis-Ereignisse belegen den historischen Hauptpfad. Aus diesen Erfolgs-/Fehlerzeilen allein folgt keine Erfüllung der Kombinationspflicht.

### B-20 · HOCH · Ablehnung erzeugt keinen Fehlertest und hinterlässt inkonsistente Begleitstände
**Stand:** `aktuelle_Logik` · **Soll:** MP6:89, MP6:91, MP6:212, MP6:213, MP6:216, MP6:259

**Quelle:** `/root/biotop/biotop/lauf.py:324–350`; `/root/biotop/biotop/lauf.py:423–434`; `/root/biotop/biotop/organe/lazarus.py:83–110`

**Mechanik:** Bei menschlicher Ablehnung werden Geschmack gespeichert, Git zurückgesetzt und Generations-/Kandidatenstatus geändert, aber kein Immuntest erzeugt und keine Wiederholungslinie geplant. Bereits vor Freigabe angelegte angenommene Artmuster und Immunsystem-im_werk/Archivstatus werden nicht zurückgesetzt. Lazarus markiert Landkarte nur veraltet statt sie wiederherzustellen; dessen stimmt=False ist ein Rückgabewert, kein Stop. Eine automatische Rückkehr n-1 mit erneutem Durchlaufen der betroffenen Generationen bei später entdecktem Fehler fehlt.

**Folge:** Der geforderte vollständige rückholbare Biotop-Zustand und die Immunisierung bei Ablehnung sind nicht durch den aktuellen Freigabepfad gedeckt.

**Ausführungsbeleg / Grenze:** 48 freigabe.frei und fünf lazarus.rueckkehr-Ereignisse sind vorhanden; kein freigabe.abgelehnt-Ereignis. Damit ist dieser Ablehnungszweig hier gebaut/gelesen, nicht historisch ausgeführt belegt.

### B-21 · HOCH · Web-Abbruch ruft eine nicht existierende Methode auf
**Stand:** `aktuelle_Logik` · **Soll:** MP6:104, MP6:94, MP6:246

**Quelle:** `/root/biotop/biotop/dienst.py:81–112`; `/root/biotop/biotop/__main__.py:42–43`; `/root/biotop/biotop/__main__.py:80–81`

**Mechanik:** POST /laeufe/<id>/abbrechen liest den JSON-Body bereits in Zeile 100, ruft dann vor dem try nochmals self._json() auf. Die Klasse definiert _json_body, aber keine _json. Der benannte Endpunkt scheitert deshalb vor L.abbrechen. Der CLI-Befehl abbrechen ist demgegenüber tatsächlich vorhanden und angebunden.

**Folge:** Eine Pflicht ist zwar über CLI erreichbar, ihr gebauter HTTP-Pfad ist aber nicht funktionsfähig. Eine reine Route-ohne-Token-Prüfung würde den Fehler nicht erreichen.

**Ausführungsbeleg / Grenze:** Statischer Befund; kein HTTP-Aufruf und kein laufender Dienst in dieser Prüfung. Vorhandene lauf.abgebrochen-Ereignisse beweisen nicht diesen HTTP-Pfad.

### B-22 · HOCH · Historisches Oberfläche-Prüfscript überschreibt ein echtes Konto ohne Wiederherstellung
**Stand:** `historisches_aufrufbares_Pruefscript` · **Soll:** MP6:106

**Quelle:** `/root/biotop/pruefung/tor3_oberflaeche.py:16–21`; `/root/biotop/pruefung/tor3_oberflaeche.py:65–66`; `/root/biotop/pruefung/tor3_oberflaeche.py:77–90`; `/root/biotop/biotop/kern/anmeldung.py:21–41`

**Mechanik:** Das Script verbindet sich ohne Prüf-DB-Override mit dem normalen Bestand und legt unter dem bestehenden Benutzer philipp ein zufälliges Prüfkennwort an. benutzer_anlegen benutzt INSERT OR REPLACE: Salz/Hash werden ersetzt. Anmeldung erzeugt zusätzlich einen gültigen Token-Datensatz. finally beendet nur den Prüfserver; Konto und Tokens werden nicht gesichert/zurückgestellt. Die Freigabeprobe ruft zudem ungeprüft die echte Freigaberoute auf und verlässt sich darauf, dass keine Generation vorliegt.

**Folge:** Ein erneuter Aufruf wäre keine bestandsneutrale Prüfung und könnte den Benutzerzugang überschreiben bzw. eine wartende Generation freigeben. Das ist ein historisch aufrufbares Prüfschema, KEIN heute laufender Angriff.

**Ausführungsbeleg / Grenze:** Gelesen, nicht ausgeführt. Anmeldeereignisse #7504–#7509 zeigen historisch Benutzeranlage und Tokens im einschlägigen Zeitraum; sie belegen allein weder die Hashwerte noch eindeutig den Scriptprozess. Keine Zugangsdaten oder Tokenwerte wurden aus der DB ausgelesen oder in den Bericht kopiert.

### B-23 · MITTEL · Web-Vorlage zeigt keinen vollständigen Anklägerbericht und nicht alle Maßkurven
**Stand:** `aktuelle_Logik` · **Soll:** MP6:94, MP6:245, MP6:246

**Quelle:** `/root/biotop/biotop/dienst.py:153–168`; `/root/biotop/biotop/organe/aegis.py:479–491`; `/root/biotop/biotop/oberflaeche.py:104–124`; `/root/biotop/biotop/oberflaeche.py:133–136`

**Mechanik:** Dienst.vorlage sucht angriff, norm, tests_neu usw. im Kandidatenfeld masse. Aegis.fertig schreibt dort nur Messwerte plus _dateien/_basis_paar/_urteil_f2; die ausführliche Anklage steht im Protokoll, nicht in diesen masse-Feldern. Der ausgegebene anklaeger-Block bleibt so gewöhnlich leer. Die Kurve zeichnet nur Gesamtkernmaß und Bereichslaufzeit, nicht alle harten Maße; die Landkarte zeigt Stufe 0/1, für Stufe 2/3 nur eine Anzahl.

**Folge:** Die Elemente sind nicht bloß Namen: reale JSON-Routen und Darstellung sind vorhanden. Ihre Inhalte decken jedoch den F6-Vorlagen- und Kurvenumfang nicht ab. Oberfläche-Prüfungen auf HTTP 200 oder vorhandene Schlüssel genügen nicht.

**Ausführungsbeleg / Grenze:** Historische Login-/Routentests belegen Teilfunktion, keinen visuellen Vollständigkeitsnachweis. Hier wurde weder Browser noch Dienst gestartet.

### B-24 · MITTEL · Entropie misst Mengen von Textzeilen und filtert Proben am Namen
**Stand:** `aktuelle_Logik` · **Soll:** MP6:90, MP6:108, MP6:227

**Quelle:** `/root/biotop/biotop/organe/entropie.py:25–44`; `/root/biotop/biotop/organe/entropie.py:77–102`

**Mechanik:** Die Diversität bildet set(diff-Zeilen), verliert also Wiederholungszahl und Reihenfolge. Kandidaten mit unterschiedlichen Häufigkeiten derselben geänderten Zeile können als identisch erscheinen. Die SQL-Auswahl kennt nur nische!=probe, nicht ist_probe; markierte Jury-/Pfadproben mit anderer Nische können eingehen. Ein Fenster ohne Kandidaten mit Diff erhält anteil=0.0 statt einer expliziten Nicht-Bestimmbarkeit. Die Sättigungsmeldung selbst beendet den Lauf tatsächlich.

**Folge:** Der ausgewiesene Doppelgänger-Anteil ist eine Textmengenheuristik, kein vollständiger Nachweis der verlangten geänderten-Zeilen-Differenz. Probe-Markierungen werden an dieser Messstelle nicht beachtet.

**Ausführungsbeleg / Grenze:** 43 entropie.generation und sechs entropie.saettigung-Ereignisse sind vorhanden. Das belegt die Meldefunktion, nicht die Messgenauigkeit dieser Diversitätsheuristik.

### B-25 · MITTEL · Eichgegenstand prüft bei Wiederverwendung nur die Vertragsdatei
**Stand:** `aktuelle_Logik` · **Soll:** MP6:90, MP6:108, MP6:167

**Quelle:** `/root/biotop/biotop/organe/eichgegenstand.py:65–95`; `/root/biotop/biotop/organe/eichgegenstand.py:111–125`; `/root/biotop/biotop/organe/eichgegenstand.py:149–171`

**Mechanik:** Bei vorhandenem Siegel reichen Existenz und unveränderte Prüfsumme der Vertragsdatei für geprueft=unveraendert. Ob die Bereiche noch existieren, das Paar noch zur DB-Vertragsmenge gehört oder der tragende Pfad der aktuellen Verfassung weiterhin passt, wird nicht geprüft. Beim ersten Siegel kann ein ausdrücklich gesetzter, aber in paare nicht vorhandener tragender Pfad außerdem auf Vertragsgröße zurückfallen. Bei vollständig fehlender Verfassung liefert _tragende_paare keinen FEHLT_AUSDRUECKLICH-Stop.

**Folge:** Die ausdrückliche tragender_pfad-Sperre für normale Werke ist vorhanden, ihre Umgehungsfälle lassen aber einen ungeeigneten/weggefallenen Gegenstand als versiegelt weiterleben. Ein unveränderter Datei-Hash ist nicht der ganze Gegenstand.

**Ausführungsbeleg / Grenze:** 16 Versiegelungsereignisse, drei Wegfallereignisse und ein Wartesignal liegen historisch vor; die Tabelle enthält zwei aktive Siegel für reale Prüfwerke. Kein neuer Siegel-/Wegfallversuch vorgenommen.

## Leseumfang und Ergebnisartefakte

Vollständig gelesen: 18 Schwerpunktmodule und 33 relevante historische Prüfscripts; dazu die im Manifest benannten Kernabhängigkeiten. Die Zeilenbereiche stehen in `leseumfang.json`. Das ist kein pauschaler Vollständigkeitsanspruch für den gesamten übrigen Repository-Kern.

- `befund.json`: strukturierter deutscher Befund, Soll- und Quellzeilen, 2a-Prüfung, Versions-/Ausführungsgrenzen.
- `BEFUND.md`: diese lesbare Fassung.
- `belegstellen-protokoll.json`: nachgelesene referenzierte Ereignisse und Lauf22/23-Chronologie.
- `beweise-detail.json`: Neubewertungen, Normproben, C-Pfade, Probe-Fundbestand, Kassenblöcke.
- `db-befund-rohdaten.json`, `protokoll-auswahl.json`, `zusatz-historie.json`: ergänzende lesend erhobene Tabellen-/Ereignisdaten.
- `leseumfang.json`: Dateipfade und gelesene Bereiche.
- `PRUEFUNG-DER-ARTEFAKTE.json`: Konsistenzprüfung der Berichtsstruktur/Belegbereiche, keine Biotop-Tests.

## Nicht behauptet

Keine neue Tor-Freigabe, kein Laufversuch, keine neue Modellleistung, kein Echtbetrieb eines Dienstes, kein Nachweis gegen alle Randfälle und keine nachträgliche Gleichsetzung fehlerhafter Altprüfscripts mit aktueller produktiver Logik.
