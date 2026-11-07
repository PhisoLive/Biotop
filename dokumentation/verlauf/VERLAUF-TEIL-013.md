# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 013 von 054

- Einträge V0221 bis V0222. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0221 · 19.09.2026 19:26:48 CEST · Hermes · Nachricht id 2230 · Sitzung `20260918_225920_3e614670` · 6103 B

```text
**Phase 3 „Gedächtnis, Mentor, Oberfläche" abgeschlossen.** Abschlussordner liegt im Prüfkanal, von außen abrufbar (HTTP 200 geprüft).

**Abholadresse (vollständig):**
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/BERICHT.md

**Prüfsumme des Ordners** (SHA-256 über DATEIEN.txt, 198 Dateien):
`a2b2cee98ecdea5724bc8969721f41ea5b44ffdb037bc3427489cc9ee6f737fb`

Weitere Einstiegspunkte im selben Ordner: `PRUEFSUMME-ORDNER.txt`, `DATEIEN.txt`, `KASSE.md`, `ausgaben/` (167 Rohausgaben), `werk/`, `biotop/`.

Zur Abweichung von deinem Stand: 174 Dateien / `3b48ecec…` war der Zwischenbericht bei Lauf 20 Gen 2. Beim Versiegeln kamen Bericht, Kassenblatt, Archive und die restlichen Ausgaben dazu, `ZWISCHENBERICHT.md` wurde durch `BERICHT.md` ersetzt — daher 198 Dateien und die neue Prüfsumme. Am Ordner ist seither nichts geändert; zuletzt nachgerechnet ergibt er unverändert `a2b2cee9…`.

**Tor 3 — meine Wertung: 7 von 11 voll, 2 teilweise, 2 nicht belegt**

*Erfüllt (7):*
- **Nachprobe Zeile 7** — Lauf 16 Gen 1–3: 2 von 2 Fällen korrekt abgelehnt (Vertrag nicht benannt / ohne Nachbar), 1 von 1 bestanden, **angenommen und im Werk** (Tag `lauf16-gen3`, 103 von 103 Tests, Kernmaß −2 → 0). `14-nachprobe-z7-ergebnis.txt`
- **Mentor** — 5 Aufrufe (Läufe 16, 17, 18, 19, 20), je 4–5 Richtungen (gefordert ≥ 3 je Werk); Pflichtfelder Ertrag/Risiko/Aufwand/Bereiche in **allen Richtungen aller 5 Aufrufe** vollständig. `40-`, `81-`, `90-`, `100-mentor-*.json`
- **Entropie** — `lagerhaus` Lauf 20: Sättigung **nach Generation 5** (gefordert: spätestens 6), Fenster 1–5, Verbesserung 0,00 % bei Schwelle 0,5 %, Doppelgänger 12 %, Lauf beendet sich selbst und verweist zurück zum Mentor. `logmuehle` Lauf 17: nach Gen 8, Fenster 4–8, 0,00 %, 9 %. `63-entropie-lauf20/17.json`
- **Geschmacksgedächtnis (Mechanik)** — versiegelte Regel P1 (`eed64ca5…`, vor dem Lauf hinterlegt), 30 Entscheidungen, 20 gelernt, **10 von 10** richtig vorhergesagt (gefordert ≥ 7). Ausdrücklich Mechanikprüfung, kein Nachweis über deinen Geschmack. `21-tor3-geschmack.txt`
- **Oberfläche** — **18 von 18** Routen ohne Token → 401; **18 von 18** Bedienelemente mit Dateipfad *und* Zeilennummer; Kostenstand und Kurve nach Anmeldung sichtbar. `70-tor3-oberflaeche.txt`
- **Zerlegung** — Lauf 20: 172 = 48 abgelehnt + 1 angenommen + 3 erzeugt + 107 leer + 4 probe + 5 überlebt + 4 verhandlung. Lauf 17: 245 = 69 + 5 + 3 + 156 + 11 + 1. Beide gehen auf; Kategorien unverändert aus Phase 2. `65-tor3-zerlegungen.txt`
- **Kurven beider Werke** — `logmuehle`: Kernmaß −13 → 0, Tests 56 → 62. `lagerhaus`: Kernmaß durchgehend 0, Tests 101 → 104, `formeln` 132,28 → 1,26 ms (−99 %), `preise` 91,58 → 12,89 ms (−86 %). `kurve-logmuehle.*`, `kurve-lagerhaus.*`

*Teilweise (2):*
- **Projektgedächtnis** — im Lauf 20 wurden **9 Kandidaten** als Wiederholung erkannt und ohne Kammerlauf verworfen (von 48 Ablehnungen bei 172 Kandidaten). Meine unabhängige Nachrechnung findet aber **2 von 187** gescheiterten Wegen aus Lauf 13, die trotzdem ausgeführt wurden (Ähnlichkeit 1,00 und 0,81), und 1 von 44 aus Lauf 16. Ursache der Differenz: meine Ableitung der berührten Funktionen (Hunk-Köpfe) ist gröber als die des Biotops (angewandter Diff). Gefordert sind 0 — deshalb nicht voll gewertet. `60-tor3-projektgedaechtnis*.txt`
- **Jury** — einstimmiger Fall belegt, **3 Fälle** aus echten Läufen mit je 3 Begründungen dreier Hersteller. Der Fall *ohne* Einstimmigkeit **nicht mit echtem Dissens**: 5 von 5 Fällen einstimmig, auch bei zwei von mir gestellten Zielkonflikten. Die Mechanik (Uneinigkeit → kein Urteil) ist mit **gestellter Gegenstimme** belegt: `einstimmig false`, `gewinner None`, Protokoll #12361. `61-`, `95-`, `96-tor3-jury*.txt`

*Nicht belegt (2):*
- **Artgedächtnis** — **0 werkübergreifende Verweise** bei je 4 Richtungen in drei aufeinanderfolgenden Läufen nach beiden Werken (18, 19, 20). Verweise auf das eigene Werk: 10 / 4 / 9. Erfundene Kennungen: 0. Das Gedächtnis ist gefüllt (89 `logmuehle`-Einträge, 5 davon angenommen) und wird vorgelegt (Block „ANDERE WERKE", 25 Einträge, angenommene zuerst) — das Modell zitiert trotzdem das eigene Werk.
- **Archivierung** — **0 Archivierungen**; kein offener Fund erlebte 5 angenommene Generationen (Lauf 20 hatte 1 angenommene, Lauf 17 deren 5, aber der einzige echte Fund wurde in Lauf 20 Gen 1 sofort behoben). Nicht künstlich herbeigeführt. `62-tor3-archivierung.txt`

**Satz 7:** K1165 (Bestandsbewertung zum Staffelpreis statt Grundpreis) als Immuntest eingelegt und in **Lauf 20 Gen 1 behoben** — `preise.tests_fehlgeschlagen` 1 → 0, Test im Werk, 104 von 104 grün in der Kammer.

**Was schiefging:** drei Messgerät-Fehler, fünf verworfene Läufe (14, 15, 16, 18, 19), je mit Protokollzeile `lauf.verworfen`. Der Ankläger buchte einen Test, der den Fehler als Norm festschrieb, als Fund; das Projektgedächtnis zitierte einen verworfenen Lauf; sechs Normtests standen als Funde im Testbestand (mein Fehler beim Übertragen zwischen Läufen).

**Endkosten: 2,8269 € von 15 € (18,8 %), 1.225 Aufrufe.** Je Lauf: 14 → 0,0035 · 15 → 0,0119 · 16 → 0,5963 · 17 → 0,9949 · 18 → 0,3398 · 19 → 0,4575 · 20 → 0,4231. Schwere Aufrufe 24 (0,739 €): davon 15 Ankläger im Bereich `filtern` (0,419 €) und 9 Mentor (0,320 €). Die verworfenen Läufe kosteten 1,41 € — die Hälfte der Phase, der Preis von Satz 2.

**Für Fassung 5** (Abschnitt 8 des Berichts): Doppelungsschlüssel auf die Behauptung umstellen — mit deiner Lesart steigt der Phase-2-Anteil von gemeldeten 2,5 % auf 83,6 %, und meine damalige Bezugsgröße war falsch gewählt (240 Ablehnungen statt 55 erzeugte Tests; richtig 10,9 % bei gleicher Lesart); Grenzmaß-Toleranz aus einer Rauschmessung ableiten (`formeln` rauscht 47 % bei 15 % Toleranz); Artgedächtnis-, Jury- und Archivierungszeile umformulieren; Fund-Übernahme zwischen Läufen muss die Norm-Prüfung mechanisch wiederholen.
```

### V0222 · 19.09.2026 19:28:40 CEST · Philipp · Nachricht id 2231 · Sitzung `20260918_225920_3e614670` · 803 B

```text
Hier kam nur Teil 2 von 2 an — schick Teil 1 noch einmal (Nachprobe, Projektgedächtnis, Mentor, Entropie, Jury, Oberfläche, Geschmack, Kandidatenaufschlüsselung, Kurven) und dazu die vollständige Abholadresse als ganze URL mit Schlüssel in einer eigenen Zeile, unverlinkt; ohne sie kann Chat-Claude den Ordner nicht öffnen. Vorläufige Wertung: Artgedächtnis-Zeile nicht erfüllt (0 werkübergreifende Verweise von 12 Richtungen — das Gedächtnis speichert Instanzen, übertragbar wären Muster; Umbau kommt in Fassung 5), Archivierungszeile ohne Gegenstand und damit ungemessen, Tor 2 Zeile 8 rückwirkend gerissen (Doppelungsanteil 83,6 % gegen die Grenze von 20 % — Phase 2 sinkt auf 9 von 11). Am versiegelten Ordner nichts ändern; die Befunde gehören in Fassung 5, nicht in den Code.
```

