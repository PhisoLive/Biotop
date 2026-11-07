# BIOTOP-LAGE-01 · Fassung 2 · `TORE-TEIL1-01.md`

- **Inhalt:** FK24, FK27–FK29 · Entwurf C, Stück 1 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil C, Arbeitszeit 25.09.2026 16:10:47–17:22:12 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/tore/TORE-TEIL1.md` · 17782 B · SHA-256 `513ca8c15f155076a2329bf0a8ba5718970173b58441944bc375a030ddb51fd6`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (1 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# TORE — Teil 1 von 4: Wortlaute der Torzeilen (zu FK24)

Entwurf Teil C der Offenlegung BIOTOP-LAGE-01 Fassung 2, geschrieben im Namen von Hermes.
**Stand des Lesens: 25.09.2026, 16:11–17:00 CEST.** Den Endstand von S1c und Runde 6 trägt Hermes nach.

**Aufteilung**
- Teil 1: Wortlaute.
- Teil 2: FK24, Tafel aller Torzeilen mit Messwert, Grenze, Bezugsgröße, Quelle, Datum und Chat-Claudes Wertung.
- Teil 3: FK27, Messgerätfehler, Zuordnung der Nummernkreise, Eichung vor dem letzten Lauf.
- Teil 4: FK28 (Aufnahmesperre C, Abweichungsquote) und FK29 (Art- und Projektgedächtnis), dazu Lücken und Widersprüche.

**Lesehilfe (gilt für alle vier Teile)**
- Keine Torwertung (Regel 2.9). „Hermes-Ergebnis“ ist das Ergebniswort des jeweiligen Berichts, keine Wertung dieser
  Offenlegung. Chat-Claudes Wertungen stehen nur als Zitat mit Fundstelle.
- (a) abgelesen, (g) gerechnet, mit Rechenweg.
- Fundstellen:
  - `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/…` = Prüfkanal;
  - `dok/…` = `arbeit/dokumente/…`;
  - `PH Z. n` = `arbeit/lesen/philipp-ab-2026-09-18.md`, Zeile n;
  - `HP Z. n` = `arbeit/lesen/hermes-an-philipp.md`, Zeile n;
  - R<n> = Rohbeleg `rohbelege/R0<n>.txt`.
- Uhrzeiten der Nachrichten wie im Nachrichtenkopf (CEST); Uhrzeiten aus Datenbanken in UTC, so gekennzeichnet.
- Das Datum jeder Fassung steht in `ENTSCHEIDUNGEN` (FK15), Kosten und Budgets in `CHRONIK` (FK20) und `KASSE`.
- Kennungen wie S1, T3, K2868 sind Biotop-Kennungen, keine Kennungen dieses Auftrags.

**Quelle der Wortlaute:** R37. Das Skript `tore/c1_wortlaute.py` liest aus jeder Fassung v1–v8 den Block „**Tor n**“ bis
zur ersten Leerzeile; jede Zeile mit „- “ ist eine Torzeile (Ergebnis auch in `tore/wortlaute.json`). Maßgeblich sind die
Fassung zur Zeit der Messung und v8. Sind beide gleich, steht der Wortlaut einmal.

## 1. Zeilenzahl der Tore je Fassung (a, R37 §1)

| Tor | v1 | v2 | v3 | v4 | v5 | v6 | v7 | v8 |
|---|---|---|---|---|---|---|---|---|
| 1 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| 2 | 6 | 6 | 10 | 10 | 10 | 10 | 10 | 10 |
| 3 | 6 | 6 | 6 | 10 | 10 | 10 | 10 | 10 |
| 4 | 5 | 5 | 5 | 6 | 6 | 11 | 10 („je Testwerk“) | 14 („je Testwerk (Fassung 8)“) |
| 5 | — | — | — | — | — | — | ein Satz, keine Zeile | ein Satz, keine Zeile |

Die Berichte und Chat-Claudes Wertungen zählen Tor 2 und Tor 3 mit je 11 Zeilen. Die elfte Zeile steht jeweils nicht im
Tor-Block (§3, §4).

## 2. Tor 1 — Wortlaut v8 (gleich v2–v7)

Gemessen unter v1 (Phase 1) und v2 (Nachlauf).
1. Landkarte: alle Bereiche erkannt (4 von 4); alle Straßen erfasst (Bezugsgröße: Hermes zählt sie vor dem Lauf, das Biotop muss n von n finden).
2. Schwächen: mindestens 4 von 5 gefunden und in angenommenen Generationen behoben; Kernmaß gestiegen (Zahl vorher/nachher). **Behoben** heißt: der versiegelte Befund tritt nicht mehr ein; bei der Sicherheitslücke zusätzlich nach 3.5 „behoben heißt verschwunden" (statischer Befund weg, Umgehung als Immuntest im Werk).
3. Kein Rückschritt: In 0 von n angenommenen Generationen ist irgendein hartes Maß gesunken.
4. Halluzinationsprobe: Im sauberen Bereich 0 angenommene Änderungen, die kein Maß heben.
5. Lazarus: Jede angenommene Generation einmal zurückgeholt; Prüfsumme des Werks stimmt (n von n).
6. Kasse: Budget auf 0,10 € gesetzt → Abbruch mit Meldung **vor** dem ersten Modellaufruf der nächsten Generation (Protokollzeile beigefügt).
7. Laut scheitern: Werk ohne Tests eingelegt → Meldung „Messgerät fehlt", 0 gestartete Generationen.
8. Kammer: Ein Kandidat mit Endlosschleife → nach Zeitlimit als gescheitert gewertet, Wirt unberührt.
9. Anmeldung: Jede Route ohne Token → HTTP 401 (Liste aller Routen mit Ergebnis).

**Abweichung v1, Zeile 2:** „Schwächen: mindestens 4 von 5 gefunden und in angenommenen Generationen behoben; Kernmaß
gestiegen (Zahl vorher/nachher).“ Der Satz „**Behoben** heißt …“ fehlt.

## 3. Tor 2 — Wortlaut v8

Gemessen unter v3 (Phase 2, Lauf 13).
1. Nischen: 4 aktiv, je mindestens 2 Anbieter; Bandit-Gewichte nach 10 Generationen protokolliert.
2. Generation 0: Hermes baut 20 Mutanten in das Übungswerk; das Biotop meldet, welche die Tests nicht fangen (Zahl); nach Generation 0 werden mindestens 16 von 20 gefangen.
3. S2 (Leistungsbremse) behoben nach dem Kriterium der versiegelten Liste, gemessen an der Referenzlast (Zahl vorher/nachher); Kernmaß dabei unverändert oder gestiegen (Nischenmaß 3.5).
4. Nebenwirkungsprobe: Hermes schleust einen Kandidaten ein, der Bereich A messbar hebt und Bereich B messbar senkt → 0 von 1 angenommen, Anklägerbericht nennt B.
5. Regressionsprobe (Fassung 3, aus Lauf 7): Hermes schleust einen Kandidaten ein, der eine frühere Behebung rückgängig macht und drei neue bestandene Tests mitbringt → 0 von 1 angenommen; das Protokoll nennt den gefallenen Einzeltest.
6. Norm-Probe (Fassung 3, aus Lauf 7): Hermes schleust einen Angriffstest ein, der an der Vorgeneration fällt, am Kandidaten besteht, ohne Absturz und ohne Vertrags-/Verfassungsbezug → bleibt „offen", 0 Punkte, nicht im Werk.
7. Vertragsprobe: Änderung an einer Grenze ohne Anpassung des Nachbarn → abgelehnt; mit Anpassung → **angenommen und im Werk** (je 1 Fall). Die Probe muss so gebaut sein, dass die Vertragsänderung eine Fehlerbehebung ermöglicht und das Paar Kernmaß bringt — sonst kann es nach 3.5 nicht angenommen werden, und die Zeile ist unerfüllbar (Fassung 4).
8. Immunisierung: n bestätigte Fehler = n Tests im Werk (Liste mit Dateipfaden); Doppelungsanteil ausgewiesen und unter 20 % **der vom Ankläger erzeugten Tests** (Fassung 5: Bezugsgröße und Schlüssel nach 3.10); nach keiner angenommenen Generation ein fehlschlagender Test im Werk (0 von n).
9. Verhandlung: mindestens 1 Generation, in der zwei Bereiche eine Vertragsänderung gemeinsam bestanden haben, protokolliert. (Fassung 4: Diese Zeile prüft nur den Mechanismus; die eingeschleuste Vertragsprobe erfüllt sie. Der Nachweis, dass der **Schwarm selbst** eine sinnvolle Vertragsänderung durchbringt, ist am Übungswerk nicht erzwingbar — dort gibt es keine Schnittstelle, die sich ändern sollte — und steht in Tor 4.)
10. Verlaufskurve des Hauptlaufs mit Endtestbestand beigefügt (3.5).

**Wortlaut v3, soweit abweichend** (Zeilen 1–6 und 10 gleich v8):
- 7: „Vertragsprobe: Änderung an einer Grenze ohne Anpassung des Nachbarn → abgelehnt; mit Anpassung → angenommen (je 1 Fall).“
- 8: „Immunisierung: n bestätigte Fehler = n Tests im Werk (Liste mit Dateipfaden); Doppelungsanteil ausgewiesen und unter 20 % aller Angriffstests; nach keiner angenommenen Generation ein fehlschlagender Test im Werk (0 von n).“
- 9: „Verhandlung: mindestens 1 Generation, in der zwei Bereiche eine Vertragsänderung gemeinsam bestanden haben, protokolliert.“

**Zeile 11 der Berichte: „Modellwahl am OpenRouter-Katalog belegt“.** Sie steht nicht im Tor-2-Block. Herkunft: der
Begleitsatz am Ende von v3 (`dok/2026-09-19_022342_…-v3.md` Z. 347, gekürzt in R73 §2): „… Auftrag: Phase 2 „Der
Schwarm" nach Abschnitt 8, Ausgang Lauf 9 Generation 6 mit Verfassung Anhang A, vorher Modellwahl …“. Auslegung Hermes:
Daraus stammt die elfte Zeile; ein ausdrücklicher Satz dazu ist NICHT GEFUNDEN.

## 4. Tor 3 — Wortlaut v8 (gleich v5–v7)

Gemessen unter v4 (Phase 3, Läufe 16–20) und v5 (Nachlauf, Läufe 21–23).
1. Nachprobe Zeile 7 aus Phase 2 bestanden (siehe oben).
2. Projektgedächtnis: Ein zweiter Lauf am ersten Übungswerk wiederholt 0 der im ersten Lauf gescheiterten Wege (Vergleich der Kandidaten beider Läufe nach Bereich und Änderungsziel; Zahl der Wiederholungen von n gescheiterten Wegen).
3. Artgedächtnis: Nach Läufen an beiden Übungswerken liefert der Mentor bei einem dritten Lauf mindestens eine Richtung, die ausdrücklich auf einen Eintrag aus dem Artgedächtnis verweist (Eintrag benannt).
4. Mentor: ≥ 3 Richtungen je Werk, je mit Ertrag (welches Maß), Risiko (welche Verträge/Bereiche), Aufwand in Generationen, berührten Bereichen.
5. Entropie: Am gesättigten `lagerhaus` (Kernmaß 0) erscheint die Sättigungsmeldung spätestens nach Generation 6 mit Bezugsgröße (Generationen x–y, Verbesserung z %, Verschiedenheitsanteil); der Lauf endet daraufhin von selbst und nennt den Weg zurück zum Mentor.
6. Jury: Zwischen zwei Kandidaten, die alle harten Maße bestehen und gleiches Kernmaß haben, entscheidet die Jury aus mindestens drei Modellen verschiedener Hersteller; Beleg: 1 Fall aus einem echten Lauf mit drei Begründungen und nachgewiesener Einstimmigkeit. **Die Uneinigkeit wird als Mechanikprüfung belegt (Fassung 5)** — gestellte Gegenstimme, Ergebnis „kein Urteil", ausdrücklich als gestellt gekennzeichnet; echter Modelldissens ist nicht erzwingbar (5 von 5 Fällen einstimmig, auch bei gestellten Zielkonflikten).
7. Geschmacksgedächtnis, Mechanik (Fassung 4): Philipps echte Entscheidungen gibt es erst ab Phase 4. Prüfung mit versiegelter Regel — Hermes hinterlegt vor dem Lauf eine Entscheidungsregel (versiegelt, Prüfsumme), erzeugt danach 30 Freigaben/Ablehnungen nach dieser Regel; das Gedächtnis lernt aus den ersten 20 und sagt von den restlichen 10 mindestens 7 richtig voraus. Ausdrücklich gekennzeichnet als Mechanikprüfung, nicht als Nachweis über Philipps Geschmack.
8. Archivierung: Offene Funde nach 5 **Generationen** archiviert (Fassung 5; Zahl archiviert / gesamt), 0 archivierte Funde in Kammerläufen danach. Tritt der Fall in keinem Lauf ein, wird er an einem eigens erzeugten offenen Fund geprüft und als Mechanikprüfung gekennzeichnet — eine Prüfung ohne Gegenstand besteht nicht, sie meldet.
9. Oberfläche: Für jedes Bedienelement Dateipfad und Zeile der Stelle, die es liest oder schreibt (vollständige Liste; ein Element ohne Stelle = Tor nicht bestanden); Zugriff nur mit Anmeldung (Aufruf ohne Token → 401, belegt); Kostenstand und Kurve sichtbar.
10. Kandidatenaufschlüsselung jedes Laufs geht auf die Gesamtzahl auf (Abschnitt 9).

**Wortlaut v4, soweit abweichend** (Zeilen 1–5, 7, 9, 10 gleich v8):
- 6: „Jury: Zwischen zwei Kandidaten, die alle harten Maße bestehen und gleiches Kernmaß haben, entscheidet die Jury aus mindestens drei Modellen verschiedener Hersteller; Beleg: 1 Fall mit drei Begründungen, Einstimmigkeit nachgewiesen; 1 Fall ohne Einstimmigkeit → kein Urteil, protokolliert.“
- 8: „Archivierung: Offene Funde nach 5 Generationen archiviert (Zahl archiviert / gesamt), 0 archivierte Funde in Kammerläufen danach.“

**Zeile 11 der Berichte: „Verlaufskurven beider Werke“.** Sie steht nicht im Tor-3-Block. v4 Z. 23 (R73 §2): „3.5:
Verlaufskurve mit Endtestbestand ist Pflichtbestandteil jedes Abschlussordners, nicht nur für Lauf 2.“ v5 Z. 343 zählt
„Kurven beider Werke“ zu den erfüllten Zeilen.

## 5. Vorbedingung 1 (Phase 4) — Wortlaut v6

`dok/2026-09-20_001844_…-v6.md` Z. 393 (Budgetangabe weggelassen, siehe CHRONIK):
> 1. **Zwei offene Bauteile aus Fassung 6 fertigstellen:** Ankläger nennt Behauptung vorab (3.7) und Mindestanteil des
> werkübergreifenden Blocks (3.12). Beide am Übungswerk messen, bevor das echte Werk angefasst wird: Tor 2 Zeile 8 unter
> 20 %, und ein `lagerhaus`-Lauf mit ≥ 1 werkübergreifendem Verweis (bisher 0, weil nur 3 fremde Muster gezeigt wurden).

Vorab gesetzte Messgrenze, wörtlich in `dok/…PRUEFUNG2_Vorbedingung-1…` Z. 114: „**Zeile 8 gilt als ungemessen**,
solange der Nenner unter 20 erzeugten Tests liegt — Grenze hiermit vorab gesetzt“. Dieselbe Grenze steht in PRUEFUNG3
Z. 108, PRUEFUNG4 Z. 134 („… unterhalb von 20 erzeugten Funden, und sie gehört zu C, nicht zu A“) und ABNAHME Z. 123
(alle vom 20.09.). In v7 und v8 ist sie NICHT GEFUNDEN (Suche nach „20 erzeugten“, „unterhalb von 20“).

Freigabetore des ersten Durchgangs, wörtlich:
- PRUEFUNG4 Z. 124: „Vorbedingung 1 ist abgenommen, wenn Durchgerutscht an C null ist, der Fehlalarm belegt unter der
  Grenze liegt, beide Eichfälle vorliegen und der Ordner unter **nummerierten** Adressen abrufbar ist.“
- PRUEFUNG6 Z. 98: „Vorbedingung 1 ist abgenommen, wenn N12 den Kassenstand klärt und die Laufgrenze nachweislich gehalten
  ist, N13 die Aufnahmestelle benennt, und beide Aufnahmestellen mit je einem Beleg abgedeckt sind — bei mindestens zwei
  verschiedenen Sperrfällen.“

Enger Nachtrag des zweiten Durchgangs, wörtlich PH Z. 353 (20.09. 22:55:04): „(1) einen vollständigen Reviewdurchgang zu
Ende führen, Zeitlimit vorher großzügig setzen und vor dem Start prüfen, nicht während; (2) K2689 zur Ausführung bringen,
Anteil danach erneut ausweisen — bleibt er unter 20 %, ist die Zeile erfüllt, steigt er darüber, gilt das gemessene
Ergebnis ohne Umdeutung.“

## 6. Tor 4 an T3 — Wortlaut v7 („Tor 4 — je Testwerk“)

T3 (`versandwerk`, TypeScript) lief unter v7. Die Nummern stimmen nicht mit v8 überein.
1. Aufnahme: Werk gebaut, Bau- und Testlauf, versiegelte Schwächen hinterlegt (bei T4 stattdessen eine unabhängig erhobene Liste der Altlasten mit Bezugsgröße).
2. Generation minus eins: Rauschmessung mit Sperren je Bereich, Eichgegenstand gewählt und versiegelt, 4 von 4 Proben bestanden **und 4 von 4 Gegenproben an der vorgesehenen Zusicherung fehlgeschlagen** (Grundsatz 8), Eichkosten getrennt ausgewiesen.
3. Generation 0: Mutantenfang ≥ 80 von 100 nicht-äquivalenten, äquivalente vorab mit Beleg aussortiert. Bei T4 zusätzlich: die Testsammlung wird erst erzeugt — Zahl der Tests vorher/nachher.
4. Schwächen: ≥ 80 % der versiegelten Schwächen behoben nach „behoben heißt verschwunden" (3.5); bei T4 stattdessen Kernmaß vorher/nachher an der Altlastenliste.
5. Kein Rückschritt: 0 von n angenommenen Generationen mit gesunkenem hartem Maß.
6. Halluzinationsprobe: im unveränderten Vergleichsbereich 0 angenommene Änderungen ohne Maßgewinn.
7. Doppelungsanteil unter 20 % der vom Ankläger erzeugten Tests.
8. Sättigung oder Budgetabbruch dokumentiert — der Lauf endet nie still.
9. Verbundausfall (Fassung 7): Fällt ein Modell des Verbunds aus (Ablehnung, Zeitüberschreitung, leere Antwort), wird das als Ausfall gezählt und **nie als Beitrag**; belegt an mindestens einem echten oder gestellten Ausfall je Testwerk, mit der Ausfallmeldung im Protokoll.
10. Ein Reviewdurchgang; Abschlussordner trägt die Torzeilen, nicht jede Zwischenstufe.

## 7. Tor 4 — Wortlaut v8 („Tor 4 — je Testwerk (Fassung 8)“), für T4 und folgende

1. Aufnahme: Werk gebaut, Bau- und Testlauf, versiegelte Schwächen mit Gegenzeugen hinterlegt (bei T4 stattdessen eine unabhängig erhobene Altlastenliste mit Bezugsgröße).
2. Generation minus eins: Rauschmessung mit Sperren je Bereich; **Maßeichung am sauberen Vergleichsbereich**, stillgelegte Regeln mit Befundzahl ausgewiesen; Eichgegenstand versiegelt; 4 von 4 Proben bestanden und 4 von 4 Gegenproben an der vorgesehenen Zusicherung gescheitert; Eichkosten getrennt.
3. Generation 0: Mutantenfang ≥ 80 von 100 nicht-äquivalenten, **je Art ausgewiesen**, mit der Verteilung dessen, was vorab verworfen wurde (Typsieb); kein Durchlauf, in dem überwiegend neutral geurteilt wurde, geht in die Zahl ein (Grundsatz 13).
4. Schwächen: ≥ 80 % der versiegelten Schwächen behoben nach „behoben heißt verschwunden"; je Schwäche der behebende Kandidat und **der Grund, aus dem er angenommen wurde** — eine Behebung, die nur über Fehlalarmpunkte oder eine Einzelmessung durchkam, zählt als nicht belastbar.
5. Kein Rückschritt: 0 von n angenommenen Generationen mit gesunkenem hartem Maß, **je Maßfeld einschließlich Laufzeit**, gepaart gemessen (Grundsatz 14).
6. **Halluzinationsprobe (streng):** Der saubere Vergleichsbereich bleibt unberührt. Jede angenommene Änderung dort lässt die Probe reißen, es sei denn, sie behebt nachweislich einen Fehler, belegt durch einen Test, der vorher fällt und nachher besteht. (Der Wortlaut von Fassung 7, „keine Änderung ohne Maßgewinn", ließ Fehlalarmbereinigung und einen fehlerhaften Zwischenspeicher durch, weil beide einen gemessenen Gewinn hatten.)
7. **Verhaltensvergleich:** jede angenommene Generation hat ihn durchlaufen; je Urteil „x von y Funktionen beobachtet"; Enthaltungen zählen nicht als bestanden; ein Sondenausfall ist ein Messgerätausfall, keine Ablehnung des Kandidaten und kein Eintrag ins Gedächtnis.
8. **Doppelungsanteil unter 20 %,** gemessen nach der Methode aus Vorbedingung 1: alle erzeugten Angriffstests, geurteilt nach ihrer geschriebenen Behauptung. Ansagefilter und Aufnahmesperre werden als Diagnosen mitgeführt, sind aber nicht die Torzeile.
9. Immunisierung (3.10 F3): für die Sprache des Werks auf dem tatsächlichen Pfad gezählt; 0 Fälle heißt nicht belegt.
10. Neutralzähler: jedes Organ mit Nenner; eine Torzeile, die an einem Organ hängt, gilt nur, wenn es in mehr als der Hälfte seiner Fälle geurteilt hat — **je Durchlauf, nicht über die Summe**.
11. Verbundausfall: als Ausfall gezählt, nie als Beitrag; belegt an mindestens einem echten oder gestellten Ausfall.
12. **Verdrahtung:** volle Regression einschließlich Verdrahtungstest grün am Kernstand des Laufs (Grundsatz 12).
13. Sättigung oder Budgetabbruch dokumentiert — der Lauf endet nie still.
14. Ein Reviewdurchgang; Abschlussordner trägt die Torzeilen. Zwischenbericht spätestens bei 120 von 150 Aufrufen einer Sitzung, mechanisch ausgelöst.

Tor 4 in v6 (Handelssystem, 11 Zeilen) ist durch v7 ersetzt; Wortlaut vollständig in R37 §4.

## 8. Tor 5 — Wortlaut v7 = v8

„**Tor 5** wird gesetzt, wenn das Werk feststeht — Kernmaß, harte Grenzen und Bezugsgrößen hängen am Werk und werden
nicht vorher erfunden.“ Es gibt keine Torzeile und keinen Messwert.
