# BIOTOP-LAGE-01 · Fassung 2 · `SOLL-IST-TEIL2-01.md`

- **Inhalt:** FK30 · Entwurf E, Stück 2 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil E, Arbeitszeit 25.09.2026 16:10:47–18:55:32 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/soll-ist/SOLL-IST-TEIL2.md` · 30410 B · SHA-256 `98e9fc42cf5baec62c612ab192fe6cd4c8bf65a446af0b71d116df08bbbd9fa5`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (0 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# SOLL-IST — Abgleich gegen Masterprompt Fassung 8 (FK30) · Teil 2 von 4

Umfang dieses Teils: Abschnitte 3.8 bis 7, dazu aus Abschnitt 8 die Phasen 1 bis 3. Kürzel, Lesart und Zählung stehen in Teil 1. „Z.“ ist die Zeilennummer in v8. Stand des Lesens: 25.09.2026, 16:05 bis 18:30 CEST.

## Abschnitt 3.8 — Nexus, die Generalprobe

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.8.1 | 227 | „Will ein Bereich eine Grenze (einen Vertrag) zum Nachbarn ändern, wird der Nachbar gefragt“ … „Ohne bestandene Anpassung des Nachbarn keine Vertragsänderung.“ | BELEGT | Vertragsprobe und Verhandlung in Tor 2 (`P2B` Z. 22, Z. 24); Nachprobe in Phase 3 (`P3B` Z. 54). Am Laufweg `lauf._verhandeln` mit `paar_ok` (`R1B` Z. 52). |
| MP3.8.2 | 229–231 | „Generalprobe: Bauen, alle Tests des ganzen Werks, alle harten Maße auf Werkebene, Verfassung, alle Verträge.“ … „Bei Bestehen: Schnappschuss (Lazarus), Vorlage an Philipp zur Freigabe.“ | BELEGT | Jede Protokollzeile `freigabe.frei` nennt das Ergebnis der Generalprobe mit Pareto- und Grenzprüfung (R83). Einen Lazarus-Schnappschuss je angenommener Generation legt `organe/lazarus.py:54–74` an. Zur Vorlage siehe MP4.4 bis MP4.6. |
| MP3.8.3 | 232 | „Eine Generation wird als Ganzes angenommen oder als Ganzes abgelehnt.“ … „und die Generation wird mit diesem Wissen wiederholt — höchstens dreimal, dann Meldung an Philipp.“ | UNKLAR | Angenommen wird als Ganzes: Der Status steht je Generation (`lauf.py:582`). Abgelehnte Wege gehen ins Projektgedächtnis (`lauf.py:305–314`). Bei einer Ablehnung setzt `lauf.generation` den Lauf auf `bereit` und misst die Entropie (`lauf.py:258–259`, `:269–273`); einen Zähler für Wiederholungen gibt es dort nicht. Eine Regel „höchstens dreimal, dann Meldung an Philipp“ habe ich NICHT GEFUNDEN. Das Wort `dreimal` steht nur in `organe/eichung.py:11`, dort beim Serienzähler (R76). Weg zur Klärung: Befehlszeile (`__main__.py`) und `tor4.py` auf eine Wiederholungsgrenze lesen. Frage an Chat-Claude: Ersetzt die Sättigungsmeldung (3.11) diese Regel? |

## Abschnitt 3.9 — Lazarus

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.9.1 | 236 | „Git-Tag je Generation plus Ablage des vollständigen Werks (Prüfsumme über alle Dateien) und des Maßstands.“ | BELEGT | `organe/lazarus.py:54–74` legt Tag, Archiv, Prüfsumme und Maße in der Tabelle `lazarus` ab. Tor 1 Lazarus (`P1N` Z. 21). |
| MP3.9.2 | 236 | „Rückkehr zu Generation n stellt Werk, Landkarte und Maß-Verlauf auf den Stand von n zurück.“ | TEILWEISE | Das Werk kehrt über `git checkout` des Tags zurück (`lazarus.py:92`), die Maße des Schnappschusses werden zurückgegeben (`lazarus.py:110`). Die Landkarte wird nicht zurückgestellt: `lazarus.py:98` markiert die Stufen 0 bis 2 als `veraltet`. Es fehlt also das Zurückstellen der Landkarte. Auslegung Hermes: Ein Neuaufbau aus dem zurückgestellten Werk ergäbe wieder den Stand n; das habe ich nicht geprüft. Alles gelesen, nicht ausgeführt. |
| MP3.9.3 | 237 | „wird zu n-1 zurückgekehrt, der Fehler geht ins Immunsystem, und die Generationen n bis n+k werden mit dem neuen Test wiederholt. Nichts wird gelöscht“ | UNKLAR | Die Rückkehr ist gebaut (`lazarus.rueckkehr`); gerufen wird sie bei einer Ablehnung (`lauf.py:598`). Einen Ablauf, der die Generationen n bis n+k wiederholt, habe ich NICHT GEFUNDEN. Ob der Fall je eintrat: UNBEKANNT. Weg zur Klärung: `lazarus.py` und die Aufrufer lesen, die Protokollarten `lazarus.*` zählen. |

## Abschnitt 3.10 — Immunisierung

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.10.1 | 240–241 | „Jeder Fehler — vom Ankläger gefunden, in der Generalprobe aufgetreten, von Philipp bei der Freigabe benannt — wird zu einem Test im Werk.“ … „Zählung: n gefundene Fehler = n neue Tests, nachweisbar im Werk.“ | TEILWEISE | Auf dem Python-Pfad belegt: Tor 2 Immunisierung (`P2B` Z. 23). Auf dem TypeScript-Pfad fehlt der Beleg: T3 „Nicht belegt: Immunisierung“ (Z. 460); der Bau steht in MP8.66. Von Philipp benannte Fehler: Es gab keine Ablehnung im Protokoll (MP4.4). |
| MP3.10.2 | 242 | „Ein Immuntest wird erst dann Teil des Werks, wenn der angenommene Kandidat ihn besteht.“ … „Ein Werk darf nach keiner angenommenen Generation einen fehlschlagenden Test enthalten“ | BELEGT | `P2B` Z. 23: Die Messung der roten Tests nach angenommenen Generationen liegt vor; der Wert steht in `TORE`. |
| MP3.10.3 | 243 | „Probenkandidaten und ihre Ergebnisse werden von keinem der drei Gedächtnisse aufgenommen“ … „erkennt eine Probe am gesetzten Merkmal (`ist_probe`)“ | BELEGT | Gebaut im Nachlauf zu Phase 3, dort „Probensperre am Merkmal“ (Z. 412). Das Feld `ist_probe` steht in `kern/datenbank.py:35`, die Prüfung in `organe/aegis.py:809–810` (R76). |
| MP3.10.4 | 245 | „Der Schlüssel ist die Behauptung — Ziel-Funktion plus Zusicherung —, nicht die Fundstelle.“ … „Der Doppelungsanteil wird gegen die vom Ankläger erzeugten Tests ausgewiesen“ | BELEGT | Gebaut im Nachlauf zu Phase 3, dort „Doppelungsschlüssel auf die Behauptung“ (Z. 412; `P3N` Abschnitt 5). Gemessen in Vorbedingung 1 (Z. 18); der Wert steht in `TORE`. |
| MP3.10.5 | 246 | „Offene Funde werden beim Übergang in einen neuen Lauf nicht mit ihrem alten Status übernommen, sondern mechanisch neu bewertet“ | BELEGT | `P3N` Abschnitt 3 (Z. 83): „Fund-Neubewertung als Organ“. |
| MP3.10.6 | 247 | „Ein offener Fund, den nach fünf Generationen kein Kandidat besteht, wird archiviert“ | BELEGT | `P3N` Abschnitt 7 (Z. 192); Tor 3 Archivierung (MP8.33). |

## Abschnitt 3.11 — Entropie

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.11.1 | 251–252 | „Je Generation zwei Zahlen“ … „Bringen fünf aufeinanderfolgende Generationen zusammen weniger als 0,5 % Verbesserung des Kernmaßes, meldet das Biotop“ | BELEGT | Tor 3 Entropie (`P3B` Z. 101). Nach jeder Freigabe laufen `entropie.messen` und `entropie.pruefen_und_beenden` (`lauf.py:590–591`). In T3 hat Lauf 37 den Status `gesaettigt` (R66). |

## Abschnitt 3.12 — Die drei Gedächtnisse

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.12.1 | 255 | „Alle drei dauerhaft in der Datenbank, alle drei werden vor jeder Generation gelesen.“ | BELEGT | Wie MP2.9. |
| MP3.12.2 | 256 | „Der Schwarm bekommt vor jeder Generation die Liste der gescheiterten Wege dieses Werks“ … „Gescheiterte Wege aus verworfenen Läufen zählen nicht“ | BELEGT | `lauf.py:305–314`: Wiederholt ein Kandidat einen gescheiterten Weg, wird er ohne Kammerlauf verworfen; Protokollart `gedaechtnis.wiederholung`. Tor 3 Projektgedächtnis (MP8.27). Die Leseseite sperrt nur bei berührtem Bereich und gepaarter Messung (`R1B` Z. 58). |
| MP3.12.3 | 257 | „Es speichert Muster, keine Instanzen“ … „Zu jeder angenommenen Generation schreibt ein zusätzlicher Aufruf den abstrahierten Satz“ | BELEGT | `P3N` Abschnitt 6 (Z. 158). |
| MP3.12.4 | 257 | „Der werkübergreifende Block belegt mindestens die Hälfte der gezeigten Einträge, mindestens fünf, sofern so viele fremde Muster vorhanden sind.“ | BELEGT | `organe/gedaechtnis.py:462` (R76); Bauteil B (`VB1B` Z. 25, Z. 32). |
| MP3.12.5 | 258 | „Geschmacksgedächtnis (Philipp): jede Freigabe, jede Ablehnung, jede Begründung. Ab 20 Entscheidungen wird daraus ein Vorhersagemodell“ … „und legt es ihm mit der Vorlage bei.“ | TEILWEISE | Gebaut: `geschmack_merken` bei Freigabe und bei Ablehnung (`lauf.py:589`, `:596`), die Vorhersage in der Vorlage (`dienst.py:166`, R76) und die Mechanikprüfung von Tor 3 (MP8.32). Es fehlen Philipps Entscheidungen. Von Philipp stammen 0 von 35 Einträgen in STAMM und 0 von 65 in T3. Gerechnet aus R83: 7 + 15 + 5 + 8 = 35, dazu `versandwerk` 30, also 65. Das Feld `von` nennt nur „Hermes unter Vollmacht …“, „Simulation P1“ und „Hermes“ (R83). Dass es mehr Einträge als Freigaben gibt, erklärt der Code: `geschmack_merken` schreibt je Freigabe einen Eintrag je Bereich (`lauf.py:588–589`). Nach v8 beginnt das echte Geschmacksgedächtnis erst in Phase 5 (Z. 491). |

## Abschnitt 3.13 — Ausführungskammer

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.13.1 | 261–262 | „Jeder Bau, jeder Testlauf, jede Messung läuft in einem abgeschotteten Container (Docker)“ … „Fremdcode wird nie auf dem Wirtsystem ausgeführt.“ | BELEGT | Tor 1 Kammer (`P1N` Z. 24); `kammer/Dockerfile` und `kammer/typescript` (R76). |

## Abschnitt 3.14 — Kasse

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.14.1 | 265 | „Jeden Modellaufruf zählen (Anbieter, Modell, Eingabe- und Ausgabetoken, Kosten nach hinterlegter Preistabelle) und gegen das Laufbudget führen.“ | BELEGT | Die Tabelle `kasse` hat die Spalten `anbieter`, `modell`, `tokens_ein`, `tokens_aus`, `kosten_eur` und `zweck` (R83). |
| MP3.14.2 | 266 | „Vor jedem Modellaufruf wird geprüft, ob der Aufruf das Budget überschreiten würde; wenn ja, Abbruch des Laufs mit Meldung und Abschlussordner.“ | BELEGT | Wie MP2.8. Den Abbruch protokolliert `kasse.abbruch` (`kern/kasse.py:149`, `:157`; R76). |
| MP3.14.3 | 266 | „Der Kostenstand ist in der Oberfläche immer sichtbar.“ | BELEGT | `oberflaeche.py:101` zeigt Ausgegebenes, Budget, Aufrufe, Token und Kontingent-Aufrufe. Gelesen, nicht ausgeführt. |
| MP3.14.4 | 266 | „Abo-Kontingente (Modelle ohne Tokenabrechnung) werden getrennt gezählt und mit eigener Grenze geführt.“ | TEILWEISE | Getrennt gezählt wird über die Spalte `kontingent` (`kern/kasse.py:240–248`, Summe in `:100` und `:112`). Eine eigene Grenze für Kontingent-Aufrufe habe ich NICHT GEFUNDEN; die Treffer zu `kontingent` in `kasse.py` stehen in Z. 100, 112, 240, 242, 246, 248 und 271. Buchungen mit `kontingent=1` gibt es 0, in STAMM wie in T3 (R83). `P1B` Z. 111: „Abo-Kontingent-Zähler ist vorhanden (`kasse.kontingent`), aber ohne Adapter für die schweren Modelle des Teams.“ |

## Abschnitt 3.15 — Oberfläche

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP3.15.1 | 269 | „Philipp sieht: das Werk und seine Landkarte; die Verfassung; das eingefrorene Maß; den Verlauf aller Maße über die Generationen (als Kurven)“ … „die Entropie; die Kasse; das Archiv (Lazarus).“ | BELEGT | Tor 3 Oberfläche (`P3B` Z. 137); 18 Bedienelemente (`P3B` Z. 41). Die Geschmacksvorhersage steht in der Vorlage (`dienst.py:166`). Stand Phase 3. |
| MP3.15.2 | 270 | „Jedes Bedienelement liest oder schreibt eine Stelle im Kern — belegt durch Hermes je Element mit Dateipfad und Zeile. Keine Phasenanzeige, die nicht dem tatsächlichen Zustand entspricht.“ | BELEGT | Wie MP1.1. Die Phasenanzeige habe ich nicht eigens geprüft. |

## Abschnitt 4 — Ablauf eines Laufs

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP4.1 | 278 | „Verfassung → Entwurf, Philipp bestätigt.“ | BELEGT | Wie MP3.3.1. |
| MP4.2 | 280 | „Maß → Vorschlag, Philipp bestätigt, eingefroren.“ | TEILWEISE | Wie MP3.5.17. |
| MP4.3 | 281 | „Mentor → Richtungen, Philipp wählt.“ | UNKLAR | In STAMM gibt es 11 Protokollzeilen `mentor.gewaehlt`, alle mit Vollmacht, in den Läufen 16 bis 25 (R100). In T3 (Läufe 26–38) gibt es keine: 0 Zeilen `mentor.richtungen` und `mentor.gewaehlt` mit `lauf_id` ≥ 26, 0 Buchungen `schwer.mentor` in diesen Läufen, keine Zeile der Tabelle `mentor` ab Lauf 26 (R157). Das Feld `richtung` ist leer (R66). In T3 lief also kein Mentor. Wessen Entscheidung das war: NICHT GEFUNDEN. Tor 4 hat keine Mentor-Zeile. |
| MP4.4 | 283 | „Freigabe → Philipp gibt frei oder lehnt ab; Ablehnung mit Grund → Immunisierung + Geschmacksgedächtnis.“ | TEILWEISE | Freigaben stehen als Protokollart `freigabe.frei` im Protokoll (R83, R100). Der Ablehnungsweg ist gebaut (`lauf.py:595–605`: Geschmack, Rückkehr über Lazarus, Protokollart `freigabe.abgelehnt`), wurde aber nie ausgeführt: Unter den Protokollarten `freigabe*` gibt es in STAMM und T3 nur `freigabe.frei` (R83, R126). Die Übergabe einer Ablehnung an die Immunisierung habe ich in `lauf.py:595–605` nicht gefunden. |
| MP4.5 | 287 | „Philipp gibt jede Generation frei. Vollautomatik über mehrere Generationen kommt erst, wenn das Messgerät über mindestens drei Werke ohne einen einzigen unbemerkten Rückschritt gearbeitet hat — und dann nur auf Philipps Satz.“ | UNKLAR | In T3 kam jede Freigabe 0,21 bis 0,28 s nach der Protokollzeile `generation.ergebnis`, gegeben von Hermes, immer mit demselben Grundtext (R111; die Zahl der Freigaben steht in MP4.6). Philipps Nachricht zu T3: „danach ist der evolutionäre Lauf freigegeben, ohne weitere Rückfrage“ (`PH` Z. 377). Frage FK47: Ist das eine Freigabe unter Vollmacht (MP4.6) oder Vollautomatik im Sinn von Z. 287? |
| MP4.6 | 288 | „Hermes gibt Generationen frei und wählt die Richtung des Mentors, protokolliert je Entscheidung die Begründung (`freigabe.frei`, `mentor.gewaehlt`, Vollmacht als Grund genannt)“ … „Für jedes Werk mit Betriebszweck gibt ausschließlich Philipp frei und wählt die Richtung“ | TEILWEISE | Zeilen `freigabe.frei`, die „Vollmacht“ nennen: in STAMM 41 von 48 (R100). Die 7 ohne stammen aus Lauf 2 (3 Zeilen) und den Kassenproben der Läufe 4 und 5 (je 2); diese Läufe begannen am 18.09.2026 (R66). In T3 (Läufe 26–38) 18 von 18 (R100, R111). `mentor.gewaehlt` gibt es in T3 nicht (MP4.3). Ein Werk mit Betriebszweck gab es bisher nicht. Es fehlt `mentor.gewaehlt` für T3. |

## Abschnitt 5 — Der unantastbare Kern

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP5.1 | 294–301 | „Diese Teile darf nur Philipp ändern; kein Schwarm, kein Kandidat, keine Generation hat Schreibzugriff“ | TEILWEISE | Der Schreibschutz beruht auf einer Pfadprüfung im Code, nicht auf dem Betriebssystem (`P1B` Z. 91). Das Protokoll ist über eine Hash-Kette verkettet (Spalten `hash_vor` und `hash`, R83). Es fehlt die technische Trennung (MP5.2). |
| MP5.2 | 303 | „Technisch: eigener Prozess, eigene Datenbank-Rolle mit ausschließlichem Schreibrecht, keine Schreibpfade aus Schwarm oder Kammer hinein.“ | OFFEN | `kern/datenbank.py:4–5`: „Phase 1: eine Datei, ein Prozess. Rollentrennung (eigener Kern-Prozess mit ausschließlichem Schreibrecht) steht auf der Liste für danach.“ (R76). Ebenso `P1B` Z. 91. Der Punkt steht seit Phase 1 auf der Liste für danach. Eine Entscheidung, ihn zu streichen: NICHT GEFUNDEN. |
| MP5.3 | 305 | „Ein Abbruch nach Satz 2 (Messgerätänderung) oder nach dem Budget ist eine Pflicht, keine Freigabe. Das Freigabe-Gate darf ihn nicht blockieren; er ist immer erlaubt und wird protokolliert.“ | BELEGT | `P3N` Abschnitt 4 (Z. 104): „Abbruch als benannter Befehl“. |

## Abschnitt 6 — Modelle und Kosten

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP6.1 | 312 | „Masse (Schwarm-Kandidaten, Ankläger-Angriffe, Zusammenfassungen der Landkarte): tokenabgerechnete Schnellmodelle über OpenRouter — mindestens zwei Anbieter. Nie über Abo-Kontingente“ | BELEGT | Alle Buchungen in STAMM und T3 laufen über den Anbieter `openrouter` (R103); keine über ein Kontingent (MP3.14.4). Die Schnellmodelle stammen von den Herstellern google, openai, deepseek und qwen (R83). |
| MP6.2 | 313 | „Schwere Aufrufe (Mentor, Verfassungsentwurf, Jury-Endurteil, Anklägerbericht an Philipp): die schweren Modelle des bestehenden Teams, gezählt gegen eine eigene Kontingentgrenze in der Kasse.“ | UNKLAR | Ist: Die schweren Aufrufe laufen tokenabgerechnet über OpenRouter mit `anthropic/claude-sonnet-4.5` und `anthropic/claude-sonnet-5` (R103), nicht über ein Kontingent (MP3.14.4). Die Jury läuft über Schnellmodelle (Kassenzwecke `jury.*`, R157). Philipp am 18.09.: „schwere Aufrufe über das bestehende Team“ (`PH` Z. 20). Eine Entscheidung für den Weg über OpenRouter: NICHT GEFUNDEN. Gesucht habe ich nach „Kontingent“ und „bestehende Team“ in `PH` und `HP`. |
| MP6.3 | 314 | „Die Anbieterschicht ist austauschbar (ein Port, mehrere Adapter)“ | TEILWEISE | Port: `anbieter.aufrufen` ist der einzige Weg zu einem Modell (`P1B` Z. 36). Adapter gibt es nur für OpenRouter; `biotop/anbieter/` enthält nur `__init__.py` (R99). Es fehlt ein zweiter Adapter. |
| MP6.4 | 327 | „Die Kasse setzt sie als Vorschlag; Philipp bestätigt das Budget vor jedem Lauf.“ | UNKLAR | Philipp setzt Budgets je Auftrag (Phase 1: `PH` Z. 20; T3: `PH` Z. 371). In T3 trug jeder der 13 Läufe das volle Budget des Testwerks als eigenes Laufbudget (R66; die Beträge stehen in `CHRONIK`). Eine Bestätigung je Lauf: NICHT GEFUNDEN. Frage FK47: Gilt ein Budget je Auftrag als Bestätigung „vor jedem Lauf“? |

## Abschnitt 7 — Was aus dem Vorgängerprojekt bleibt

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP7.1 | 334 | „Der Server-Torwächter (Express: Request-IDs, strikte CORS-Liste, Helmet, Rate-Limits, Body-Limits, Sanitizing, Fehlerhandler, Redaction im Protokoll, Kill-Switch, Zod-validierte Umgebung).“ … „eine echte Anmeldung (Benutzer, Kennwort, Token-Ausgabe) existiert; alle Routen sind geschützt, nicht nur `/api/admin`.“ | UNKLAR | Den Vorgänger gibt es auf der Maschine nicht: „Kein Vorgängerprojekt `infinite-evolution-ai` auf dieser Maschine.“ (`HP` Z. 21, 18.09.). Das Biotop ist ein Neubau in Python. Zu Express, Helmet und CORS gibt es keinen passenden Treffer; die 3 Treffer des Musters betreffen andere Wörter (R76). Die verlangten Änderungen sind erfüllt: Anmeldung mit Token und 401 ohne Token (`dienst.py:4`, `:95`, `:99`; MP8.11). Frage FK47: Gilt „Übernehmen“ in Abschnitt 7 noch? |
| MP7.2 | 335 | „Der Aktenschrank (Chunking mit Überlappung, Stichwort- plus Bedeutungssuche, Cosinus-Vergleich) → wird Teil der Landkarte.“ | UNKLAR | Die Funktion fehlt in der Landkarte (MP3.2.4, OFFEN). Unklar ist, ob die Übernahme aus dem Vorgänger noch verlangt ist, denn den Vorgänger gibt es auf der Maschine nicht (`HP` Z. 21). Frage wie MP7.1. |
| MP7.3 | 336 | „Prüf- und Bauabläufe (CI, Lint, Prettier, Vitest, Playwright, gitleaks, CodeQL, Dependabot).“ | UNKLAR | Im Biotop-Baum NICHT GEFUNDEN: kein `.github`, kein `.gitlab-ci.yml`, kein `.pre-commit-config.yaml`, kein `.gitleaks.toml`. Die Wörter „gitleaks“, „codeql“ und „dependabot“ kommen im Code nicht vor (R76). Frage wie MP7.1. |
| MP7.4 | 337 | „Die Fehlerklassen und das Protokollsystem (`AppError`, `normalizeError`, Logger mit Redaction).“ | UNKLAR | Ein Protokoll mit Hash-Kette ist vorhanden (R83). Zur Schwärzung im Protokoll: „redact“, „schwaerz“, „schwärz“ und „maskier“ kommen im Code nicht vor. Frage wie MP7.1. |
| MP7.5 | 338 | „Die Anbieterschicht (Port `IGenAIProvider`, Adapter je Anbieter).“ | UNKLAR | Der Port ist in Python neu gebaut (MP6.3). Frage wie MP7.1. |
| MP7.6 | 341 | „JSON-Datei als Datenbank → SQLite (mindestens) mit Transaktionen“ | BELEGT | SQLite-Datenbanken STAMM und T3 (R83); Transaktionen über `transaktion(con)` (`lauf.py:581`, `:599`). |
| MP7.7 | 342 | „Sitzungsgedächtnis im Arbeitsspeicher → die drei Gedächtnisse in der Datenbank.“ | BELEGT | Wie MP2.9. |
| MP7.8 | 345 | „Alle nicht erreichbaren Komponenten (gemessen: 51 Dateien, 4.310 Zeilen), darunter MemoryCore, AgentMindMap, NeuralNexus, GamificationOverlay, SynapticChat, HolographicHUD, QuantumPreview, QuantumKernel, EntropyAtom, SingularityStrategy, StrategyFactory, SwarmAgents in ihrer jetzigen Form.“ | BELEGT | Keiner dieser Namen und auch nicht `sanitizer` kommt unter `/root/biotop` vor (R126, Suche c). Der Vorgänger wurde nie übernommen (`HP` Z. 21). |
| MP7.9 | 346 | „Sicherheitsprüfung wird ein hartes Maß (statische Analyse, Abhängigkeitsprüfung), keine Vorab-Zensur.“ | TEILWEISE | Die statische Analyse ist Teil des Kernmaßes: `sicherheit_punkte` aus bandit (`P1B` Z. 38), Befundklassen für TypeScript (`kern/befundklassen.py:103`, `:130`; R76). Eine Abhängigkeitsprüfung habe ich NICHT GEFUNDEN: „pip-audit“, „npm audit“, „safety“ und „osv-scanner“ kommen im Code nicht vor. |
| MP7.10 | 347 | „Die Schalter „Sicherheitsmodus" und „Freigabepflicht" als Prompt-Text. Freigabe ist ein Kernmechanismus (Abschnitt 4, Schritt 8), kein Text.“ | BELEGT | Die Freigabe ist als Mechanismus mit Protokoll gebaut (`lauf.py:580–605`). Nach den Schaltern selbst habe ich nicht gesucht; der Vorgänger wurde nie übernommen (`HP` Z. 21). |
| MP7.11 | 348 | „Alle `.env`-Dateien mit echten Schlüsseln. Geheimnisse ausschließlich über Umgebungsvariablen des Servers; gitleaks im CI-Pflichtlauf; Paket-Skripte, die ein Archiv erzeugen, schließen `.env*`, `node_modules`, `dist`, `coverage`, `.tools` aus“ | TEILWEISE | Im Biotop-Baum gibt es keine Datei `.env*` (R99). Wie das Biotop den Schlüssel erhält, habe ich nicht geprüft. gitleaks im CI: NICHT GEFUNDEN, denn es gibt kein CI (R76). Die Ausschlüsse der Archivskripte habe ich nicht geprüft. |

## Abschnitt 8 — Phase 1, das Skelett

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP8.1 | 357 | „Aufnahme, Landkarte (Stufen 0–3, Straßen; Verträge nur abgeleitet), harte Maße, ein Schwarm (eine Nische, zwei Anbieter), Ankläger (Schritte 1, 4, 5), Ausführungskammer, Lazarus, Kasse, Protokoll, Anmeldung, Datenbank.“ | BELEGT | Die gebauten Organe stehen in `P1B` Z. 35–39. Phase 1 ist abgeschlossen (Z. 372). |
| MP8.2 | 358 | „Hermes baut ein Werk mit drei Bereichen (~800–1.200 Zeilen, mit Tests) und baut fünf bekannte Schwächen ein“ … „Die Liste der fünf liegt versiegelt außerhalb der Reichweite des Biotops. Ein vierter, bereits sauberer Bereich dient als Halluzinationsprobe.“ | BELEGT | Das Werk `lagerhaus` (`P1B` Z. 49). Die versiegelte Liste liegt entsiegelt als `46-versiegelte-liste-entsiegelt.md` vor (`P1B` Z. 16). Den Umfang nennt `LAGE`. |
| MP8.3 | 360 | „Landkarte: alle Bereiche erkannt (4 von 4); alle Straßen erfasst“ | BELEGT | `P1N` Z. 17. |
| MP8.4 | 361 | „Schwächen: mindestens 4 von 5 gefunden und in angenommenen Generationen behoben; Kernmaß gestiegen (Zahl vorher/nachher).“ | BELEGT | `P1N` Z. 18. |
| MP8.5 | 362 | „Kein Rückschritt: In 0 von n angenommenen Generationen ist irgendein hartes Maß gesunken.“ | BELEGT | `P1N` Z. 19. |
| MP8.6 | 363 | „Halluzinationsprobe: Im sauberen Bereich 0 angenommene Änderungen, die kein Maß heben.“ | BELEGT | `P1N` Z. 20. |
| MP8.7 | 364 | „Lazarus: Jede angenommene Generation einmal zurückgeholt; Prüfsumme des Werks stimmt (n von n).“ | BELEGT | Tor-Tabelle in `P1B`; `P1N` Z. 21: „gilt weiter“. |
| MP8.8 | 365 | „Kasse: Budget auf 0,10 € gesetzt → Abbruch mit Meldung vor dem ersten Modellaufruf der nächsten Generation (Protokollzeile beigefügt).“ | BELEGT | `P1N` Z. 22. |
| MP8.9 | 366 | „Laut scheitern: Werk ohne Tests eingelegt → Meldung „Messgerät fehlt", 0 gestartete Generationen.“ | BELEGT | `P1N` Z. 23. |
| MP8.10 | 367 | „Kammer: Ein Kandidat mit Endlosschleife → nach Zeitlimit als gescheitert gewertet, Wirt unberührt.“ | BELEGT | `P1N` Z. 24. |
| MP8.11 | 368 | „Anmeldung: Jede Route ohne Token → HTTP 401 (Liste aller Routen mit Ergebnis).“ | BELEGT | `P1N` Z. 25; `P3B` Z. 139. |

## Abschnitt 8 — Phase 2, der Schwarm

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP8.12 | 375 | „Vier Nischen, Bandit-Gewichtung, Generation 0 (Mutanten), Verträge explizit, Ankläger vollständig (Schritte 2 und 3, Norm-Regel 3.7), Nexus mit Verhandlung, Generalprobe und Pareto je Test“ … „Verlaufskurve je Lauf, Grenzmaß „größte Funktion" absolut.“ | BELEGT | Tor-Tabelle in `P2B` Z. 16–26, der Bau in Z. 51. Phase 2 ist gewertet (Z. 390). |
| MP8.13 | 375 | „Vor dem ersten Lauf: OpenRouter-Katalog auf aktuellere Schnellmodelle gleicher Hersteller zu gleichem oder niedrigerem Preis prüfen und die Wahl mit Preisen belegen.“ | BELEGT | `P2B` Z. 26. |
| MP8.14 | 379 | „Nischen: 4 aktiv, je mindestens 2 Anbieter; Bandit-Gewichte nach 10 Generationen protokolliert.“ | BELEGT | `P2B` Z. 16. |
| MP8.15 | 380 | „Generation 0: Hermes baut 20 Mutanten in das Übungswerk; das Biotop meldet, welche die Tests nicht fangen (Zahl); nach Generation 0 werden mindestens 16 von 20 gefangen.“ | BELEGT | `P2B` Z. 17. |
| MP8.16 | 381 | „S2 (Leistungsbremse) behoben nach dem Kriterium der versiegelten Liste, gemessen an der Referenzlast (Zahl vorher/nachher)“ | BELEGT | `P2B` Z. 18. |
| MP8.17 | 382 | „Nebenwirkungsprobe: Hermes schleust einen Kandidaten ein, der Bereich A messbar hebt und Bereich B messbar senkt → 0 von 1 angenommen, Anklägerbericht nennt B.“ | BELEGT | `P2B` Z. 19; mit gehärteten Proben in `P3N` Abschnitt 2; Reparatur 02 (siehe MP8.19). |
| MP8.18 | 383 | „Regressionsprobe (Fassung 3, aus Lauf 7): Hermes schleust einen Kandidaten ein, der eine frühere Behebung rückgängig macht und drei neue bestandene Tests mitbringt → 0 von 1 angenommen“ | BELEGT | `P2B` Z. 20; `P3N` Abschnitt 2. |
| MP8.19 | 384 | „Norm-Probe (Fassung 3, aus Lauf 7): Hermes schleust einen Angriffstest ein, der an der Vorgeneration fällt, am Kandidaten besteht, ohne Absturz und ohne Vertrags-/Verfassungsbezug → bleibt „offen", 0 Punkte, nicht im Werk.“ | BELEGT | `P2B` Z. 21. Chat-Claude nahm die Norm-Zeile und „4 von 4“ aus dem Nachlauf später zurück: „ein leerer Durchlauf (masse statt mass, norm=[])“ (`PH` Z. 317). Die vier Eichproben wurden in Reparatur 02 neu belegt: „alle vier Torzeilen erfüllt“ (`PH` Z. 341). v8 Z. 390 erwähnt das nicht (Widerspruch W-E3 in Teil 4). |
| MP8.20 | 385 | „Vertragsprobe: Änderung an einer Grenze ohne Anpassung des Nachbarn → abgelehnt; mit Anpassung → angenommen und im Werk (je 1 Fall).“ | BELEGT | `P2B` Z. 22; Nachprobe in Phase 3 (MP8.24). |
| MP8.21 | 386 | „Immunisierung: n bestätigte Fehler = n Tests im Werk (Liste mit Dateipfaden); Doppelungsanteil ausgewiesen und unter 20 % der vom Ankläger erzeugten Tests“ | BELEGT | `P2B` Z. 23; die berichtigte Messung (Z. 390) und die Messung in Vorbedingung 1 (Z. 18). Die Werte stehen in `TORE`. |
| MP8.22 | 387 | „Verhandlung: mindestens 1 Generation, in der zwei Bereiche eine Vertragsänderung gemeinsam bestanden haben, protokolliert.“ | BELEGT | `P2B` Z. 24. |
| MP8.23 | 388 | „Verlaufskurve des Hauptlaufs mit Endtestbestand beigefügt (3.5).“ | BELEGT | `P2B` Z. 25. |
| MP8.24 | 392 | „Vertragsprobe nach der präzisierten Zeile — ein Paar aus Vertragsänderung und dadurch ermöglichter Fehlerbehebung, Kernmaß > 0, angenommen und im Werk“ … „Dazu die Kandidatenaufschlüsselung von Lauf 13 auf 470 aufgehen lassen oder die Differenz benennen.“ | BELEGT | `P3B` Z. 54: die Nachprobe als erste Torzeile des Berichts. `P3B` Z. 152: „470 geht auf“. |

## Abschnitt 8 — Phase 3, Gedächtnis, Mentor, Oberfläche

| Kennung | Z. | Wortlaut (v8) | Status | Beleg · Fehlendes · Entscheidung |
|---|---|---|---|---|
| MP8.25 | 395 | „Drei Gedächtnisse (3.12), Mentor (3.4), Entropie mit Sättigungsmeldung (3.11), weiche Maße mit Jury (3.5), Archivierung offener Funde (3.10), Oberfläche (3.15) als Web-Oberfläche hinter der Anmeldung, vom Tablet bedienbar. Dazu ein zweites Übungswerk anderer Bauart als `lagerhaus`“ | BELEGT | Bau in `P3B` Z. 36 und Z. 41. Tablet: `oberflaeche.py:5`, `:34` (R76). Das zweite Übungswerk ist `logmuehle`, seine Verfassung steht in Anhang B (MPB.1). |
| MP8.26 | 399 | „Nachprobe Zeile 7 aus Phase 2 bestanden (siehe oben).“ | BELEGT | Wie MP8.24. |
| MP8.27 | 400 | „Projektgedächtnis: Ein zweiter Lauf am ersten Übungswerk wiederholt 0 der im ersten Lauf gescheiterten Wege“ | BELEGT | `P3B` Z. 66; neu bewertet in Fassung 6 (Z. 410). |
| MP8.28 | 401 | „Artgedächtnis: Nach Läufen an beiden Übungswerken liefert der Mentor bei einem dritten Lauf mindestens eine Richtung, die ausdrücklich auf einen Eintrag aus dem Artgedächtnis verweist (Eintrag benannt).“ | BELEGT | `P3B` Z. 79; `P3N` Abschnitt 6; `VB1B` Z. 25. |
| MP8.29 | 402 | „Mentor: ≥ 3 Richtungen je Werk, je mit Ertrag (welches Maß), Risiko (welche Verträge/Bereiche), Aufwand in Generationen, berührten Bereichen.“ | BELEGT | `P3B` Z. 94. |
| MP8.30 | 403 | „Entropie: Am gesättigten `lagerhaus` (Kernmaß 0) erscheint die Sättigungsmeldung spätestens nach Generation 6“ | BELEGT | `P3B` Z. 101. |
| MP8.31 | 404 | „Jury: Zwischen zwei Kandidaten, die alle harten Maße bestehen und gleiches Kernmaß haben, entscheidet die Jury aus mindestens drei Modellen verschiedener Hersteller“ | BELEGT | `P3B` Z. 109. Chat-Claudes Wertung (Z. 410) steht in `TORE`. |
| MP8.32 | 405 | „Geschmacksgedächtnis, Mechanik (Fassung 4): Philipps echte Entscheidungen gibt es erst ab Phase 4.“ … „Ausdrücklich gekennzeichnet als Mechanikprüfung, nicht als Nachweis über Philipps Geschmack.“ | BELEGT | `P3B` Z. 120, Z. 125. Zu „ab Phase 4“ siehe Widerspruch W-E5 in Teil 4. |
| MP8.33 | 406 | „Archivierung: Offene Funde nach 5 Generationen archiviert“ | BELEGT | `P3B` Z. 128; `P3N` Abschnitt 7. |
| MP8.34 | 407 | „Oberfläche: Für jedes Bedienelement Dateipfad und Zeile der Stelle, die es liest oder schreibt (vollständige Liste; ein Element ohne Stelle = Tor nicht bestanden); Zugriff nur mit Anmeldung (Aufruf ohne Token → 401, belegt); Kostenstand und Kurve sichtbar.“ | BELEGT | `P3B` Z. 137, Z. 139. |
| MP8.35 | 408 | „Kandidatenaufschlüsselung jedes Laufs geht auf die Gesamtzahl auf (Abschnitt 9).“ | BELEGT | `P3B` Z. 144–152. |

*Fortsetzung in Teil 3.*
