# BIOTOP-LAGE-01 · Fassung 2 · `LAGE-TEIL2-01.md`

- **Inhalt:** Abgleich des Wissensstands WS01–WS19; FK23, FK25, FK26, FK44, FK45 · Entwurf G, Stück 1 von 2
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil G, Arbeitszeit 25.09.2026 16:10:47–18:16:10 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/lage-werke/LAGE-BAUSTEINE-G-TEIL1.md` · 27694 B · SHA-256 `06790973731a91a785f3da85f7c17cdc0d8adf21e33a6b25df2f34e384a3ba7a`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (14 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# LAGE-Bausteine G, Teil 1: Abgleich des Wissensstands WS01–WS19

Entwurf für `LAGE` (BIOTOP-LAGE-01 Fassung 2). Geschrieben von einem Subagenten im Auftrag von Hermes (HERMES-1).
Stand des Lesens: 25.09.2026, 16:11 bis 17:35 CEST. Den Endstand von S1c und der Runde 6 trägt Hermes nach.
Teil 2 (`LAGE-BAUSTEINE-G-TEIL2.md`) enthält die Bausteine FK23, FK25, FK26, FK44 und FK45.

## Lesehilfe

- **Maßstab:** Chat-Claudes Wissensstand ist der 21.09.2026, 02:16 CEST.
  - `VERALTET`: Der Punkt wurde nach 02:16 überholt. Der neue Stand steht dabei.
  - `FALSCH`: Der Punkt stimmte schon um 02:16 nicht. Der richtige Stand steht dabei.
  - `GILT` oder `UNBEKANNT`: Einschränkungen stehen dabei.
- **Quellen:**
  - `v8` ist die gültige Masterprompt-Fassung 8: `arbeit/dokumente/2026-09-23_155353_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md`. „v8 Z. n“ ist die Zeile darin.
  - Nachrichten stehen mit Datum, Uhrzeit (CEST) und id aus dem berichtigten Verzeichnis `arbeit/verlauf/v2/wortlaut.jsonl` da. Der Absender ist Philipp, wenn nichts anderes steht. Viele seiner Nachrichten tragen Entscheidungen Chat-Claudes.
  - `R<n>` sind Rohbelege unter `rohbelege/R<nnnn>.txt`. Der Prüfkanal steht als `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/…`.
- **Zahlen:** Zahlen, die der Auftrag anderen Dateien zuweist, stehen hier nicht noch einmal.
  - Torzeilen und Messgerätfehler stehen in `TORE`.
  - Kosten und Budgets stehen in `CHRONIK` (FK20) und `KASSE`.
  - Fassungen stehen in `ENTSCHEIDUNGEN` (FK15), Verfassungen in `VERFASSUNGEN`.
  - Zahlen im zitierten Wortlaut Chat-Claudes oder einer Quelle bleiben stehen.
- **Auslegungen:** Eigene Lesarten sind als „Auslegung Hermes“ gekennzeichnet.

## Übersicht

| Punkt | Gegenstand | Markierung |
|---|---|---|
| WS01 | gültige Fassung | VERALTET |
| WS02 | Zielbild, Selbstevolution, Rollen | GILT (sinngemäß, zwei Wendungen ohne Quelle) |
| WS03 | Kernmaß | GILT |
| WS04 | Phase 1 | GILT |
| WS05 | Phase 2 | GILT (Widerspruch zur Norm-Zeile offen) |
| WS06 | Phase 3 und Nachlauf | GILT (mit Einschränkung vom 20.09.) |
| WS07 | Vorbedingung 1 | GILT (unvollständig) |
| WS08 | Bauteile A, B, C | GILT |
| WS09 | Aufnahmesperre C im natürlichen Betrieb | VERALTET |
| WS10 | Abweichungsquote Ansage↔Ausführung | FALSCH |
| WS11 | Tor 2 Zeile 8 und Artgedächtnis | GILT (mit Einschränkungen) |
| WS12 | Handelssystem gestrichen | GILT |
| WS13 | Phase 4 als Breitentest | GILT |
| WS14 | Sättigungsregel | GILT |
| WS15 | Phase 5 | GILT |
| WS16 | Grundsätze | VERALTET |
| WS17 | Freigabe | VERALTET |
| WS18 | Ablieferung | GILT (Einhaltung UNBEKANNT) |
| WS19 | Ablageorte | teils GILT, Kasse FALSCH |

Zählung (gerechnet aus der Tafel): 14 von 19 Punkten `GILT`, einschließlich WS19 mit einem falschen Teil. 4 Punkte sind `VERALTET` (WS01, WS09, WS16, WS17), 1 Punkt ist `FALSCH` (WS10), 0 sind `UNBEKANNT`.

---

### WS01 — Gültige Fassung

*Stand Chat-Claude:* Gültig ist Fassung 7 vom 21.09.2026, v1 bis v6 sind ersetzt. Jede Fassung trägt oben ein Änderungsverzeichnis.

**VERALTET.** Seit dem 23.09.2026 um 15:53:53 CEST gilt Fassung 8. Philipp legte sie als Dokument in den Chat (id 13998). Zwei Sekunden später schrieb er (id 14000, 15:53:55):
> „Lies INFINITE-EVOLUTION-BIOTOP-Masterprompt-v8.md vollständig, Fassung 7 ist ersetzt; neu sind die Grundsätze 10 bis 14, Tor 4 und die Vorbedingungen für T4 in Abschnitt 8.“

v8 beginnt mit „Änderungen gegenüber Fassung 7 (aus T3 `versandwerk`, Läufe 26–38, `abschluss-03`, nicht abgenommen)“. Darunter führt v8 die älteren Verzeichnisse weiter (v8 Z. 7–81). Als eigene Dateien liegen Änderungsverzeichnisse für v2 bis v8 vor: `arbeit/fassungen/aenderungen-v2.md` bis `-v8.md`, 7 Dateien, abgelesen. Für v1, die Ursprungsfassung, gibt es keine. Die Fassungsliste mit Prüfsummen steht in `ENTSCHEIDUNGEN` (FK15).

### WS02 — Zielbild, Selbstevolution, Rollen

*Stand Chat-Claude:*
- Das Biotop versteht jedes Werk von A bis Z und hebt es als Ganzes. Jeder Bereich wird einzeln bearbeitet, das Ganze passt harmonisch zusammen.
- Es erkennt, wenn etwas schon bestmöglich ist, und halluziniert nicht.
- Selbstevolution ist ausgeschlossen.
- Hermes führt aus, Chat-Claude prüft, Philipp entscheidet.

**GILT sinngemäß.**

1. **Zielbild.** v8 Z. 84 (Abschnitt 0):
   > „Baue ein System, in das man ein Software-Werk hineinlegt (Quelltext beliebiger Art, als ZIP, Git-Adresse oder Ordner) und das dieses Werk in Generationen auf ein messbar höheres Niveau hebt — jeden Bereich einzeln, das Ganze stimmig.“
   - Die Wendungen „von A bis Z“ und „bestmöglich“ stehen in keiner der Fassungen v1 bis v8 (je 0 Treffer, R120 Abschnitt a).
   - Auch in `arbeit/lesen/philipp-ab-2026-09-18.md` gibt es dafür 0 Treffer (Suche nach „A bis Z“, „bestmöglich“, „harmonisch“, „halluziniert nicht“).
   - Seit Fassung 7 schränkt v8 Z. 418 den Anspruch ein:
     > „Keine endliche Zahl von Testwerken beweist, dass das nächste funktioniert. Erreichbar ist belegte Breite: In welchen Arten von Werken trägt das Biotop nachweislich? Eine Behauptung über alle Werke wird nie aufgestellt, auch nicht nach dem letzten Testwerk.“
2. **Erkennen und nicht halluzinieren.** Zwei Organe tragen diesen Anspruch.
   - Die Entropie mit Sättigungsmeldung (v8 Abschnitt 3.11).
   - Die Halluzinationsprobe: in Tor 1 und in Tor 4, dort „streng“ (v8 Z. 442).
   - Die Ergebnisse dieser Proben stehen in `TORE`.
3. **Selbstevolution.** v8 Z. 84:
   > „Das System verändert seinen eigenen Code niemals während es läuft; es hebt ausschließlich Werke, die Philipp hineinlegt.“

   Verfassungssatz 4, v8 Z. 103:
   > „Das laufende Biotop verändert seinen eigenen Code nie. Soll es sich selbst heben, wird eine Kopie als Werk eingelegt; Philipp entscheidet, ob die gehobene Kopie das neue Werkzeug wird.“
4. **Rollen.** Kopf der Berichte, zum Beispiel `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/BERICHT.md` Z. 13: „Auftraggeber: Philipp Zöllisch · Prüfer: Chat-Claude · Ausführung: Hermes“. Ergänzung: Philipp hat Entscheidungen delegiert.
   - **An Chat-Claude**, v8 Z. 161: „Für Übungswerke schreibt Chat-Claude die Verfassung; Philipp hat die Entscheidung delegiert.“ Viele Aufträge tragen den Vermerk „Entscheidungen Chat-Claude“.
   - **An Hermes:** die Vollmacht (siehe WS17) und die Arbeitsregel vom 23.09.2026 08:25:31 (id 12450): „Philipp gibt dir so viel Verantwortung wie möglich — Weiterarbeiten ist der Normalfall, Anhalten die Ausnahme.“

### WS03 — Kernmaß

*Stand Chat-Claude:* Bestandene Tests zählen nicht, nur Fehlschläge zählen negativ. Leistung ist eine Grenze, kein Punktwert.

**GILT.**
- v8 Z. 173:
  > „Kernmaß je Bereich (Fassung 2; gilt für alle Werke ohne eigenes Klassenmaß): `−(fehlgeschlagene Tests) − 10·(Sicherheitsbefunde HIGH) − 3·(MEDIUM) − 1·(LOW) − (tote Funktionen)`. Höchstwert ist 0. Bestandene Tests zählen nicht.“
- v8 Z. 176:
  > „Grenzmaße (keine Punkte; darüber ist der Kandidat tot): Laufzeit auf Referenzlast, Speicher, Bauzeit, größte Funktion, Zyklen.“
- Neu seit v8 sind zwei Grundsätze (v8 Z. 127, 131):
  - Grundsatz 10: Jede Prüferregel wird vor dem Lauf am sauberen Vergleichsbereich geeicht. „Schwarm wie Ankläger lesen das geeichte Maß.“
  - Grundsatz 14: Laufzeit wird gepaart gemessen, nie gegen ein historisches Minimum.
- Ein Klassenmaß je Werkklasse ist möglich (v8 Z. 179).

### WS04 — Phase 1

*Stand Chat-Claude:* Tor 1 wurde nach dem Nachlauf (Lauf 9) mit 9 von 9 abgenommen.

**GILT.**
- v8 Z. 372:
  > „Nachlauf zu Tor 1 — erledigt (Lauf 9, Abschlussordner `laeufe/biotop-phase-1-nachlauf/`, 19.09.2026 02:20): Tor 1 **9 von 9 bestanden**, geprüft durch Chat-Claude am Bericht … **Phase 1 ist abgeschlossen; Phase 2 ist freigegeben.**“
- Abnahme in Philipps Nachricht vom 19.09.2026 02:23:42 (id 997): „Tor 1 ist mit 9 von 9 abgenommen, Phase 1 abgeschlossen“.
- Die Torzeilen stehen in `TORE`.

### WS05 — Phase 2

*Stand Chat-Claude:*
- Ordner `laeufe/biotop-phase-2/`.
- Vier Nischen, vier Hersteller über OpenRouter.
- Kostenangabe, dazu die rückwirkende Wertung 9 von 11.

**GILT, mit einem offenen Widerspruch.**
1. **Wertung.** v8 Z. 390: „Stand Phase 2 nach Lauf 13 (Wertung Chat-Claude, Stand Fassung 6): **9 von 11.**“
2. **Hersteller.** `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/BERICHT.md` Z. 16: „4 von 4 Nischen, je 4 von 4 Herstellern genutzt (openai, google, deepseek, qwen)“.
3. **Kosten.** Die Kostenangabe aus WS05 steht wörtlich in v8 Z. 390. Die Nachrechnung steht in `KASSE`.
4. **Vorgeschichte der Wertung.**
   - Zuerst hieß es „Phase 2 ist mit 10 von 11 gewertet“ (id 1393, 19.09.2026 12:39:25).
   - Mit Fassung 6 wurde die Wertung berichtigt (id 2798, 20.09.2026 00:55:54): „Wertungen korrigiert: … Phase 2 Zeile 8 auf 68,5 % berichtigt, Probenzeilen wieder belegt“.
5. **Widerspruch.**
   - v8 Z. 390 führt weiter, die Proben seien „im Nachlauf zu Phase 3 mit gehärteten Proben **wieder belegt, 4 von 4**“.
   - Am 20.09.2026 um 15:28:25 (id 4317) nahm Chat-Claude aber zurück: „die Norm-Zeile aus Tor 2 und „4 von 4 bestanden“ aus dem Nachlauf waren ein leerer Durchlauf (masse statt mass, norm=[])“.
   - Ob Reparatur 01 oder 02 die Norm-Zeile neu belegt hat, habe ich nicht geprüft. Das gehört in `TORE`.
6. **Lauf 26.** Die spätere Messung von Zeile 8 an Lauf 26 ändert die Phase-2-Wertung nicht: „Die jetzigen 1 von 11 ändern diesen historischen Lauf nicht und erteilen keine neue Gesamtwertung 11/11.“ (`https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-01/UEBERGABE-PHASE-4.md` Z. 89).

### WS06 — Phase 3 und Nachlauf

*Stand Chat-Claude:*
- Phase 3 mit Kostenangabe, Wertung 8 von 11.
- Der Nachlauf (Kostenangabe) ist abgenommen, neun von neun Punkten sind erledigt.

**GILT, mit einer Einschränkung, die schon vor 02:16 bestand.**
1. **Phase 3.** v8 Z. 410: „Stand Phase 3 (Wertung Chat-Claude, Stand Fassung 6): **8 von 11 voll, 1 teilweise, 2 im Nachlauf erledigt.**“
   - Philipp schrieb am 19.09.2026 um 20:14:46 (id 2234): „Phase 3 ist abgeschlossen, keine Nachfragen.“
   - Phase 3 arbeitete an beiden Übungswerken, `logmuehle` und dem gesättigten `lagerhaus` (v8 Z. 395–396).
2. **Nachlauf.** v8 Z. 412: „Nachlauf zu Phase 3 — erledigt (Läufe 21–23, Abschlussordner `laeufe/biotop-phase-3-nachlauf/`, …): Alle neun Punkte abgearbeitet, geprüft durch Chat-Claude am Bericht.“
   - Abnahme: id 2798 (20.09.2026 00:55:54): „Nachlauf abgenommen, alle neun Punkte geprüft“.
   - Die Kostenangaben aus WS06 stehen in v8 Z. 410 und 412. Die Nachrechnung steht in `KASSE`.
3. **Einschränkung.** Am 20.09.2026 um 15:28:25 (id 4317) nahm Chat-Claude einen Teil zurück, und zwar zusätzlich zur Rücknahme, die unter WS05 zitiert ist: „die Zahlen aus den Läufen 22 und 23 stehen wegen des Satz-2-Verstoßes unter Vorbehalt, darunter die 54,5 %.“
   - Die Läufe 22 und 23 gehören laut v8 Z. 412 zum Nachlauf.
   - Fassung 7 und Fassung 8 führen den Nachlauf trotzdem unverändert als „erledigt“.

### WS07 — Vorbedingung 1

*Stand Chat-Claude:* Vorbedingung 1 wurde am 20.09.2026 abgenommen, mit den Läufen 22 bis 25, Aufruf- und Kostenzahlen.

**GILT als Ereignis, ist aber schon zum Stand 02:16 unvollständig.** Vorbedingung 1 wurde zweimal abgenommen.
1. **Erste Abnahme am 20.09.** Das Dokument `arbeit/dokumente/2026-09-20_045016_ABNAHME_Vorbedingung-1_2026-09-20.md` (Chat-Claude) nennt die Zahlen aus WS07:
   > „Wertung: ABGENOMMEN. … Geltungsbereich ist eng — Abschnitt 4 gehört zwingend zur Abnahme dazu.“
2. **Zwischenschritte.**
   - Die Bestandsaufnahme (id 4317, 20.09. 15:28:25) stellte die Zahlen der Läufe 22 und 23 unter Vorbehalt.
   - Es folgten Reparatur 01 und Reparatur 02. Reparatur 02 wurde am 20.09. um 21:14:38 abgenommen (id 7913).
   - In derselben Nachricht kam der neue Auftrag: „Nächster Auftrag: Vorbedingung 1 aus Masterprompt Fassung 6 — die zwei offenen Bauteile fertigstellen … und am Übungswerk messen“.
3. **Zweiter Durchgang (Lauf 26).**
   - Erst hieß es „Wertung: nicht abgenommen“ (id 8461, 20.09. 22:55:04).
   - Dann hieß es „Vorbedingung 1 abgenommen.“ (id 8749, 21.09.2026 00:07:30).
   - Ordner: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-02/`.
4. **Datum in den Fassungen.** v8 übernimmt aus dem Änderungsverzeichnis von v7: „8: Vorbedingung 1 **abgenommen** (21.09.2026): Tor 2 Zeile 8 erfüllt mit 9,09 %, Artgedächtnis 3 von 5 Richtungen mit werkübergreifendem Verweis.“ Lauf 26 kommt in den Zahlen von WS07 nicht vor. Seine Kosten stehen in `KASSE`.
5. **Überschneidung.**
   - v8 Z. 412 rechnet die Läufe 21–23 dem Phase-3-Nachlauf zu.
   - Die Abnahme vom 20.09. rechnet die Läufe 22–25 der Vorbedingung 1 zu.
   - Die Läufe 22 und 23 stehen also in beiden. Das ist zu klären in `CHRONIK` und `KASSE`.

### WS08 — Bauteile A, B und C

*Stand Chat-Claude:* Bauteil A spart Aufrufe, verhindert aber keine Doppelungen. Bauteil B zeigt Streuung statt Wirkung. Deshalb wurde die Aufnahmesperre C gebaut.

**GILT.**
- Wortlaut im Gedächtnis `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/STAND-01.md` vom 20.09.2026, 05:17 CEST (R31):
  - „Bauteil A (Ankläger sagt die Behauptung vorab an) spart Aufrufe und verhindert Zwangsbefunde — es verhindert **keine** Doppelungen. Es sperrt, was angesagt wird, nicht was geschrieben wird.“
  - „Bauteil B (Mindestanteil werkübergreifender Block) zeigt **Streuung statt Wirkung**“
  - „Aufnahmesperre C wurde deshalb neu gebaut, war im Plan nicht vorgesehen: deterministisch, im Kern, an beiden Aufnahmestellen“
- Seit v8 gilt für Tor 4 (v8 Z. 444): „Ansagefilter und Aufnahmesperre werden als Diagnosen mitgeführt, sind aber nicht die Torzeile.“
- Zur Wirkung der Ansage siehe WS10.

### WS09 — Aufnahmesperre C im natürlichen Betrieb

*Stand Chat-Claude:* C hat im natürlichen Betrieb nie eine Doppelung abgefangen. Alle Belege waren gestellte Fälle (Stand 20.09.).

**VERALTET.**
1. **Bis 02:16 galt der Punkt.** Auch der zweite Durchgang von Vorbedingung 1 meldete: „Aufnahmesperre C: 3 dokumentierte Aufnahmekontrollereignisse; keine natürliche Sperrung belegt.“ (`https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-01/ERGEBNIS-DETAIL.md` Z. 29).
2. **Neuer Stand.** In den T3-Läufen 37 und 38 sperrte C laut der Nachzählung in `abschluss-03` Tests als Doppelung (`https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-03/ABSCHLUSS-03.md` §4e).
   - Das wird als Diagnose geführt, nicht als Torzeile. Die Werte stehen in `TORE`.
   - Ob diese Sperrungen ohne gestellte Gegenstände entstanden, habe ich nicht nachgeprüft.
3. **Widerspruch.**
   - Philipps Nachricht vom 22.09.2026 15:32:32 (id 11505) sagt: „Aufnahmesperre: null von null in beiden Läufen“.
   - ABSCHLUSS-03 §4e vom 23.09. nennt für Lauf 37 einen Wert ungleich null.
   - Welche Läufe id 11505 meint, ist offen. Das ist zu klären in `TORE`.

### WS10 — Abweichungsquote Ansage↔Ausführung

*Stand Chat-Claude:* Die Quote ist ungemessen (Stand 20.09.).

**FALSCH zum Stand 21.09. 02:16.** Der Punkt stimmte am Morgen des 20.09. und war am Abend desselben Tages überholt.
1. **Am Morgen des 20.09.**
   - Die Abnahme §4 sagt: „Abweichungsquote Ansage ↔ Ausführung: **0 Zeilen**, ungemessen“.
   - `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG-05.md` §5 sagt: „**Nicht gemessen**, keine Grenze verletzt — die Quote bleibt offen.“
2. **Richtiger Stand um 02:16.** Im zweiten Durchgang (Lauf 26, 20.09. abends) wurde gezählt: „9 von 11 weichen von ihrer Ansage ab. Kein solcher Fall wird aus dem Nenner entfernt.“ (`…/nach-reparatur-02/abschluss-01/BERICHT.md` Z. 31).
   - Philipps Nachricht vom 20.09. um 22:55:04 (id 8461) greift das auf:
     > „dass 9 von 11 Angriffstests von ihrer eigenen Ansage abweichen — das entwertet die Vorab-Ansage als Filter und ist zum fünften Mal dieselbe Fehlerklasse (geprüft wird die Ankündigung, nicht die Sache), gehört aber in einen eigenen Auftrag nach Vorbedingung 2.“
   - Vorbedingung 2 ist mit Fassung 7 entfallen (siehe WS12). Einen eigenen Auftrag dazu habe ich nicht gefunden.
3. **T3.** Für T3 gibt es keine solche Zahl. In den Berichten unter `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/` enthält keine Zeile zugleich „Ansage“ und „Abweich“ (0 Zeilen, R120 Abschnitt f).

### WS11 — Tor 2 Zeile 8 und Artgedächtnis

*Stand Chat-Claude:* Tor 2 Zeile 8 ist erfüllt (9,09 %). Das Artgedächtnis ist in 3 von 5 Richtungen belegt.

**GILT als Wertung der Vorbedingung 1 an Lauf 26, mit Einschränkungen.**
1. **Wertung.** id 8749 (21.09.2026 00:07:30): „Quote 9,09 % bei unveränderten elf Testidentitäten: Tor 2 Zeile 8 ist damit erfüllt, nach drei Runden, in denen sie gerissen war.“
2. **Grundlage.** Die Datei `TORZEILEN.json` des zweiten Durchgangs. Sie ist zitiert in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-03/NACHTRAG-6-TOR2ZEILE8.txt` Z. 14: „Python Vorbedingung 1 Lauf 26: 1 von 11 = 9,09 % (aus TORZEILEN.json)“.
3. **Prüfaufforderung vom 22.09.** (id 11505, 15:32:32):
   > „mein Vergleich mit den 9,09 % war falsch, weil er zwei verschiedene Größen verglich. Such die Berechnung der 9,09 % im Abschlussordner von Vorbedingung 1; findest du sie nicht, miss Lauf 26 mit derselben Methode wie T3 — weicht das Ergebnis ab, ist die Abnahme von Tor 2 Zeile 8 wieder offen“

   Die Berechnung wurde gefunden (NACHTRAG-6). Eine Wiedereröffnung habe ich nicht gefunden.
4. **Einschränkungen.**
   1. Die Bezugsgröße sind elf erzeugte Angriffstests in einem einzigen Lauf am Übungswerk.
   2. Für Phase 2 bleibt die Zeile historisch gerissen (siehe WS05).
   3. An T3 ist die Torzeile nicht gemessen (ABSCHLUSS-03 §4e: „**Torzeile: nicht gemessen**“). Für Lauf 37 war die Methode aus Vorbedingung 1 „nicht rekonstruierbar“, für Lauf 38 wurde die Behauptung „nur bei 9 von 87 aufgezeichnet“. Im Gedächtnis `STAND-01.md` (20.09.) hieß es noch: „Tor 2 Zeile 8 ist **ungemessen**“ (R31).
   4. Der Phase-3-Nachlauf maß die Zeile an den Läufen 13, 20 und 22, jeweils über der Grenze (`https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/BERICHT.md` Z. 136–138). Der Wert für Lauf 20 wurde später berichtigt (Kopf von `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/BERICHT.md` Z. 5). Der Wert für Lauf 22 steht unter Vorbehalt (id 4317). Die Werte stehen in `TORE`.
5. **Artgedächtnis.** `…/nach-reparatur-02/abschluss-01/ERGEBNIS-DETAIL.md` Z. 81:
   > „Die originale Mentorantwort aus genau einem Aufruf (# 16093) nennt in 3 von 5 Richtungen fremde Muster. Alle fremden Einträge stammen von logmuehle, die eigenen von lagerhaus.“

   Dieselbe Angabe steht im Änderungsverzeichnis von v7 und wurde in v8 übernommen.

### WS12 — Handelssystem gestrichen

*Stand Chat-Claude:* Das Handelssystem ist seit dem 21.09. als Phase-4-Werk gestrichen. Alle Bezugsgrößen daraus sind ungültig.

**GILT.**
- v8 Z. 14:
  > „Das Handelssystem stand in den Fassungen 1 bis 6 als Phase-4-Werk, war aber eine nie bestätigte Vorentscheidung von Chat-Claude; alle darauf bezogenen Bezugsgrößen (237.000 Zeilen, 17 Dienste, 135 Testfehlschläge) sind gestrichen.“
- Mitteilung an Hermes: id 9106, 21.09.2026 02:14:40.
- **Rest:** Das Gedächtnis `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/STAND-01.md` nennt noch als nächsten Schritt „Vorbedingung 2 — die Verfassung des Handelssystems“ (R31). Es ist die einzige Fassung, vom 20.09. 05:17:33 (siehe WS19).

### WS13 — Phase 4 als Breitentest

*Stand Chat-Claude:* Breitentest an Werken neuer Art, die Hermes selbst baut: T3 TypeScript, T4 groß, fremder Stil, ohne Tests, T5 Oberfläche, T6 Zustand und Außenwelt.

**GILT.**
- v8 Z. 420: „Herkunft der Werke: Hermes baut alle Testwerke selbst (Entscheidung Philipps, 21.09.2026), mit versiegelten Schwächen wie bei `lagerhaus` und `logmuehle`. Ausnahme in T4, siehe dort.“
- Zu T4, v8 Z. 426: „Hermes erzeugt es über ein anderes Modell als sein eigenes, damit Stil und Struktur nicht seine sind.“
- v8 Z. 432: „Reihenfolge: T3, T4, T5, T6 — vom größten Bruch zum kleinsten. Jedes Werk ist ein eigener Auftrag mit eigenem Abschlussordner.“
- Neu in v8 sind „Tor 4 — je Testwerk (Fassung 8)“ und die „Vorbedingungen für T4“ (v8 Z. 436–476).
- Den Stand der Testwerke beschreiben die Bausteine FK23 und FK25.

### WS14 — Sättigungsregel

*Stand Chat-Claude:* Phase 4 ist fertig, wenn zwei aufeinanderfolgende Werke neuer Art keinen neuen Messgerätfehler erzeugen.

**GILT.**
- v8 Z. 452: „**Der Breitentest ist abgeschlossen, wenn zwei aufeinanderfolgende Testwerke neuer Art durchlaufen, ohne einen neuen Messgerätfehler zu erzeugen.**“
- Neu in v8 Z. 461: „T3 zählt nicht zur Sättigung des Breitentests.“
- Die Anwendung beschreibt der Baustein FK26.

### WS15 — Phase 5

*Stand Chat-Claude:* Phase 5 ist das erste echte Werk und hat noch kein Werk. Philipp wählt es nach dem Breitentest nach fünf Kriterien.

**GILT.**
- v8 Z. 480: „**Werk: noch nicht bestimmt.** Die Wahl trifft Philipp nach dem Breitentest.“
- Die fünf Kriterien stehen in v8 Z. 481–485 inhaltsgleich mit WS15. Das zweite lautet dort: „Es hat Tests, oder es lässt sich welche bauen.“
- Einen Kandidaten nennt keine Quelle. Das belegt der Baustein FK45.

### WS16 — Grundsätze

*Stand Chat-Claude:* Abschnitt 2a hat neun Grundsätze. Die Grundsätze 7 bis 9 kamen mit Fassung 7.

**VERALTET.** v8 Z. 114 hat die Überschrift „## 2a. Vierzehn Grundsätze (Fassung 6, erweitert in Fassung 7 und 8)“.
- Die Grundsätze 7 bis 9 stehen in v8 Z. 124–126 wie in WS16.
- Mit v8 kamen am 23.09. die Grundsätze 10 bis 14 dazu. Kernsätze im Wortlaut (v8 Z. 127–131):
  - 10: „Der Schwarm optimiert das Maß, nicht die Sache.“
  - 11: „Schneller ist nur besser, wenn das Verhalten nachweislich gleich bleibt“
  - 12: „Ein Organ zählt nur, wenn der Lauf es aufruft.“
  - 13: „Ein Durchlauf, in dem überwiegend nichts geurteilt wurde, heißt „nicht gemessen“, nie „nichts gefunden“.“
  - 14: „Laufzeit wird gepaart und robust verglichen, nie gegen ein historisches Minimum.“

### WS17 — Freigabe

*Stand Chat-Claude:* Nach Stand 20.09. gibt ab Phase 4 ausschließlich Philipp frei. Die Vollmacht für Übungswerke gilt dort nicht. Unklar ist, ob das auch für die Testwerke gilt.

**VERALTET** (Auslegung Hermes zur Markierung). Fassung 7 ging am 21.09. um 02:14:34 ein, zwei Minuten vor Chat-Claudes Stand. Streng nach der Zeitregel wäre der Punkt also `FALSCH`. WS17 beschreibt aber ausdrücklich den Stand 20.09.
1. **Stand 20.09.** In Fassung 6 war Phase 4 das Handelssystem. v6 Z. 390: „**Freigaben ausschließlich durch Philipp** (Abschnitt 4) — hier beginnt das echte Geschmacksgedächtnis, und die Vollmacht für Übungswerke gilt nicht.“ Seit Fassung 7 steht diese Regel bei Phase 5.
2. **Wortlaut v8, Abschnitt 4** (Z. 288):
   > „**Vollmacht für Übungswerke (Fassung 2, erweitert in Fassung 5):** Für Werke ohne Betriebszweck, die Hermes selbst erzeugt hat, gilt eine schriftliche Vollmacht: Hermes gibt Generationen frei **und wählt die Richtung des Mentors**, protokolliert je Entscheidung die Begründung (`freigabe.frei`, `mentor.gewaehlt`, Vollmacht als Grund genannt), und Chat-Claude prüft alles am Abschlussordner. Für jedes Werk mit Betriebszweck gibt ausschließlich Philipp frei und wählt die Richtung; eine stellvertretende Freigabe dort ist ein Verstoß, kein Ermessen.“
3. **Wortlaut v8, Phase 5, Vorbedingung 4** (Z. 491):
   > „**Freigaben ausschließlich durch Philipp**; die Vollmacht für Übungswerke gilt hier nicht. Hier beginnt das echte Geschmacksgedächtnis.“
4. **Kern** (Auslegung Hermes). Die Vollmacht knüpft an „Werke ohne Betriebszweck, die Hermes selbst erzeugt hat“ an, nicht an das Wort „Übungswerk“.
   - Die Testwerke T3 bis T6 erfüllen beides. T4 erzeugt Hermes über ein anderes Modell (siehe WS13).
   - Damit gilt die Vollmacht im Breitentest.
   - Ausschließlich Philipp gibt ab Phase 5 frei, außerdem bei jedem Werk mit Betriebszweck.
5. **Praxis in T3.**
   - 18 Generationen der T3-Datenbank tragen diesen Freigabegrund: „Hermes: Uebungswerk ohne Betriebszweck; Freigabe unter dokumentierter Vollmacht Abschnitt 4 F2, Verfassung regeln.uebungswerk=true. Messung entscheidet, kein Modellurteil.“ (R31, abgelesen).
   - Die in R31 sichtbaren Freigabezeiten der T3-Datenbank liegen am 22.09.2026. Die Liste in R31 ist gekürzt. Welchen Läufen die 18 Generationen gehören, habe ich nicht erhoben.
6. **Widerspruch in v8.**
   - Z. 405 (Tor 3, Text aus Fassung 4): „Philipps echte Entscheidungen gibt es erst ab Phase 4.“
   - Z. 491 sagt für Phase 5: „Hier beginnt das echte Geschmacksgedächtnis.“
   - Ausführlich behandelt das `ENTSCHEIDUNGEN` (FK19, Teil A).

### WS18 — Ablieferung

*Stand Chat-Claude:* Nummerierte Dateinamen, die nie überschrieben werden.

**GILT. Die Einhaltung ist UNBEKANNT.** Die Regel steht im Gedächtnis, nicht im Masterprompt.
1. **Wortlaut.**
   - REGELN-01, V19 (R31 Z. 122): „Nummerierte Dateien nie überschreiben.“
   - STAND-01: „Ablieferungsweg: Dateien werden **nie überschrieben**. Nummerierte Namen, jede Adresse einmal. Überschriebene Dateien kommen im Chat nur im alten Stand an.“
   - In v8 gibt es für „überschrieben“ 0 Treffer (R130 Abschnitt e).
2. **Praxis.**
   - Der Ordner der Vorbedingung 1 trägt `NACHGANG-03` bis `-06`, `DATEIEN-03` bis `-06` und `PRUEFSUMME-ORDNER-03` bis `-06` (R26).
   - Seit T3 wird je Lieferung ein neuer Unterordner oder Ordner angelegt, darin meist Dateien ohne Nummer wie `BERICHT.md` oder `DATEIEN.txt`. Beispiele: `abschluss-01` bis `-03` und `laeufe/biotop-vor-t4/` bis `-06/` (R26).
3. **Einhaltung.** Ob Dateien überschrieben wurden, lässt sich aus Dateizeiten nicht belegen. Weg zur Klärung: Prüfsummenlisten der Lieferungen gegen den heutigen Bestand vergleichen (`INVENTAR`).

### WS19 — Ablageorte

*Stand Chat-Claude:*
- Code unter `/root/biotop`, Kasse unter `/root/biotop/daten/biotop.db`.
- Die Ordner liegen unter `laeufe/<auftrag>/`.
- Das Gedächtnis liegt unter `laeufe/gedaechtnis/`, und nur HERMES-1 schreibt dorthin.

1. **Code: GILT.**
   - Der Stamm ist `/root/biotop` (git).
   - Daneben gibt es den T3-Arbeitsordner `/root/biotop-t3/` und die Arbeitsordner der Behebungsrunden `/root/biotop-vor-t4*`.
2. **Kasse: FALSCH.** Schon um 02:16 lag die Kasse in drei Datenbankzweigen, seit T3 in vier (R87, R31):
   - STAMM `/root/biotop/daten/biotop.db` mit den Läufen 1–25;
   - VB1 `/root/phase-4-vorbedingung-1/privat/biotop.db` mit zusätzlichem Lauf 26, begonnen am 20.09. um 21:31 CEST;
   - R02 `/root/reparatur-02/privat-cli/privat.db`;
   - T3 `/root/biotop-t3/t3.db` mit den Läufen 26–38, der erste begonnen am 21.09. um 05:43 CEST.

   Die Lauf-Nummer 26 ist in den Zweigen dreifach vergeben, die Werk-id 23 zweifach (Baustein FK25). Die Kassenzahlen stehen in `KASSE`.
3. **Prüfkanal: GILT.** Unter `laeufe/` liegen 19 Ordner `biotop-*` und der Ordner `gedaechtnis`, zusammen 20 (R26, Stand 25.09. 15:43).
4. **Gedächtnis: GILT als Ort und als Schreibrolle.** STAND-01: „Schreibrolle: HERMES-1 (Auftrag); HERMES-2 und HERMES-3 lesen nur.“
   - Das Gedächtnis wurde seit dem 20.09.2026 05:17:33 aber nicht fortgeschrieben. Es gibt nur die Fassung 01: 5 Dateien mit derselben Änderungszeit (R120 Abschnitt e).
   - REGELN-01, V19 verlangt: „`STAND` nach jedem Auftrag, `REGELN` nach neuer Masterprompt-Fassung“. Seither kamen zwei Fassungen (v7, v8) und mehrere Aufträge.
