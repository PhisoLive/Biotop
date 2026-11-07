# BIOTOP-LAGE-01 · Fassung 2 · `TORE-TEIL3-01.md`

- **Inhalt:** FK24, FK27–FK29 · Entwurf C, Stück 3 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil C, Arbeitszeit 25.09.2026 16:10:47–17:22:12 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/tore/TORE-TEIL3.md` · 22165 B · SHA-256 `7fe3c1bd815f3c8b4210850acb2e0e2b5f8da29f61fd18d7a96e332e54afc51a`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (2 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# TORE — Teil 3 von 4: FK27, Messgerätfehler seit dem 18.09.2026

Stand des Lesens 25.09.2026, 16:11–17:05 CEST. Lesehilfe: Teil 1. Keine Torwertung. Q1–Q7 wie in Teil 2 §1
(Q3 = Phase-3-Bericht, Q5–Q7 = T3-Abschlüsse 01–03).

**Abgrenzung (Definition aus der Quelle)**
- `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/MESSGERAETFEHLER.md` Z. 3: „Ein neuer Messgerätfehler ist eine erstmals an T3 belegte
  falsche Messung, falsche Zulassung oder fehlende erforderliche Ausführung im Kernpfad.“
- Diese Definition gilt hier für alle Werke.
- Aufgenommen sind Befunde, die die Quelle selbst als Messgerät-, Mess- oder Instrumentfehler, als Review-Befund einer
  Behebungsrunde oder als Spezifikation führt.
- Fehler in Hermes' eigenen Auswertungen stehen getrennt in §6.
- Kennungen sind unverändert übernommen. „—“ heißt: die Quelle vergibt keine Kennung.

**Spalten der Tafeln**
- **beh.** = behoben laut jüngster gelesener Quelle: ja / nein / offen (Runde 6 läuft) / Liste (bewusst auf die Liste gesetzt) /
  NICHT ERHOBEN.
- **Eichf.** = an einem gestellten Fall, einer Probe mit Gegenprobe oder einer roten Spezifikation nachgewiesen: ja / nein /
  NICHT ERHOBEN.

## 1. Phasen 1–3, Nachlauf, Bestandsaufnahme, Reparatur (18.–20.09.)

| Kennung | Werk, Lauf | Beschreibung (Quelle) | beh. | Eichf. |
|---|---|---|---|---|
| — (3 Funde) | `lagerhaus`, Läufe 6, 7 | „Pareto je Test, Angriffstests sind keine Verträge, nur bestandene Immuntests ins Werk“; dazu das Grenzmaß „größte Funktion“, korrigiert auf 60 Zeilen absolut (v3 Z. 347, Begleitsatz) | ja, laut v3 | NICHT ERHOBEN |
| — | `lagerhaus`, Lauf 12 | Die Norm-Probe war rot: Der Test wäre ins Werk gekommen. „Messgerät korrigiert, Lauf 13“ | ja | ja: Norm-Probe K1018 in Lauf 13 (Teil 2, Zeile 2.6) |
| — (3 Funde) | Phase 2 | „KEIN VORSCHLAG neutral, äquivalente Mutanten vorab belegt, offene Funde archivieren“; dazu das Grenzmaß auf den Bestwert des Laufs und die Norm-Regel auf alle neuen Tests mit explizitem Verweis (v4 Z. 374) | ja, laut v4 | NICHT ERHOBEN |
| — | Phase 2, Lauf 13 | Doppelungsanteil gemeldet mit 2,5 %: gerechnet „gegen 240 Ablehnungen statt gegen 54 erzeugte Tests“, die Fundstelle geprüft statt der Behauptung (v8 Z. 390). Nachgemessen mit dem Behauptungsschlüssel: 68,5 % (Phase-3-Nachlauf §5) | ja (Schlüssel gebaut) | ja: „Phase-3-Falle“, 6 Tests → 1 Behauptung (Nachlauf §5) |
| — | `lagerhaus`, Lauf 16 | „Ankläger schrieb den Fehler als Norm fest“: Der Vertragsverweis wurde nur bei Tests geprüft, die an der Vorgeneration fallen. Der Test tötete jede Behebung über Pareto je Test (Q3 §6) | ja: Korrektur nach Wortlaut Philipp | NICHT ERHOBEN |
| — | `lagerhaus`, Lauf 18 | „Das Projektgedächtnis zitierte einen verworfenen Lauf“: 12 von 13 Wiederholungs-Verwerfungen verwiesen auf Lauf 16 (Q3 §6) | ja: verworfene Läufe zählen nicht | NICHT ERHOBEN |
| — | `lagerhaus`, Lauf 19 | „Sechs Normtests standen als Funde im Testbestand“: 6 von 7 übernommenen offenen Funden waren Norm (Q3 §6) | ja: Fund-Neubewertung (später als Organ) | nein: Nachweis am echten Lauf 20, Generation 1 |
| — | Lauf 16, Generation 5 | „Vierter Fehler, ohne Messwirkung“: `lauf_id` doppelt im Protokoll (Q3 §6) | ja | — |
| — | Lauf 19, Rauschprobe | `formeln` rauschte um 47 % bei einer Toleranz von 15 % (Q3 §6) | ja: Rauschtoleranz wird gemessen (Nachlauf) | NICHT ERHOBEN |
| — | Nachlauf zu Phase 3, Lauf 22 | „Im ersten Durchlauf … vier „bestanden" — drei davon aus falschen Gründen“ (Phase-3-Nachlauf §2, R31) | ja, laut Nachlauf; aber siehe A11/B-04 | ja: 4 von 4 Proben am versiegelten Gegenstand |
| — | Proben Phase 2/3 | „die alten Proben zielten über Textanker und trafen nach jeder angenommenen Generation woanders hin“ (v8 Z. 390) | ja: Eingriffe aus dem Syntaxbaum (Nachlauf §2) | ja |
| A01 … A33, B-01 … B-24, C01, C02 | Quellstand `b42dc94`, Stichtag 20.09. | Bestandsaufnahme `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/`: „49 redaktionelle Befundgruppen“ (BERICHT Z. 9). Mess-bezogen nach Überschrift: A08, A10–A21, A25, A27, A32, A33, B-04, B-09, B-24 (ABWEICHUNGEN-01, Überschriften) | je Gruppe NICHT ERHOBEN, Ausnahmen in den drei folgenden Zeilen | NICHT ERHOBEN |
| A11 = B-04 | Nachlauf, Lauf 22 | „Norm-Eichprobe besteht wegen falschem Rückgabeschlüssel ohne Normnachweis“ (`masse` statt `mass`, `norm=[]`, `zuwachs=None`) (ABWEICHUNGEN-01 Z. 143–158) | ja: Reparatur 02 abgenommen, „alle vier Torzeilen erfüllt“ (PH Z. 341) | ja: 4 Eichproben mit 4 Gegenproben |
| A08 | Stichtag 20.09. | „Generation minus eins und Generation 0 sind keine erzwungenen Startvoraussetzungen“ | Pflichtvorspann: Kern von Reparatur 01 (PH Z. 323); Nachweis NICHT GELESEN | NICHT ERHOBEN |
| A33 | Stichtag 20.09. | „Späteres F7-Bauteil C kann einen neuen Fund wegen seiner eigenen vorherigen Ansage sperren“ | Auslegung Hermes: ja. Parameter `eigene_ansage_nr` an `aufnahmesperre`, eingeführt in `bb8eb0f` (21.09. 12:08:57 +0200, R97); er liegt vor allen T3-Kernständen ab `e259e9f` „Kernstand vor Lauf 31“ (R105). Code: `aegis.py:998–999`. Ein Beleg „A33 behoben“ ist NICHT GEFUNDEN | NICHT ERHOBEN |
| KERN-01 | Reparatur 01, reale Bestandsbatterie | „Reale Bestandsbatterie und echte Pflichtvorspann-CLI scheitern. Nur1/4 gültige Positivtreffer;4/4 gültige falsche Gegenzeugen.“ (Wortlaut ohne Leerzeichen wie in der Quelle, `…/biotop-reparatur-01/eskalation-runde-02/pruefscripte/runde2_paket.py` Z. 95) | ja: „KERN-01 ist richtig gelöst“ (PH Z. 341, 20.09. 21:14) | ja: Batterie mit 305 IDs unverändert (PH Z. 341) |
| KERN-02, KERN-03 | Reparatur 01, synthetisch | kollidierende Klassen-Testidentitäten im Pareto-Vergleich; testinterner NameError ohne Ortsnachweis als Werkabsturz gewertet („an ausdrücklich synthetischen … Grenzen belegt“, `…/eskalation-runde-02/ZWISCHENBERICHT.md` Z. 38) | NICHT ERHOBEN | synthetisch belegt |
| — | Reparatur 01 | Ein ignorierter Skip-Status wurde als Nachweis gelesen; „Zweimal wird die Abwesenheit eines Fehlschlags als Nachweis gelesen“ (PH Z. 326). Suche nach derselben Stelle: „661 Kandidatenzeilen über 126 Dateien“ (PH Z. 329) | Kernpfad: ja (Reparatur 02 abgenommen); außerhalb: „bestätigt offen“ auf einer Liste (PH Z. 329) | NICHT ERHOBEN |

## 2. Vorbedingung 1 (20./21.09.) und T3 (21.–23.09.)

| Kennung | Werk, Lauf | Beschreibung (Quelle) | beh. | Eichf. |
|---|---|---|---|---|
| V9 | VB1, Lauf 26 | Ansage und Ausführung weichen ab in „9 von 11 Angriffstests“; „das entwertet die Vorab-Ansage als Filter und ist zum fünften Mal dieselbe Fehlerklasse (geprüft wird die Ankündigung, nicht die Sache)“ (PH Z. 353; TORZEILEN.json) | nein: „in_diesem_nachtrag_bearbeitet“ false; eigener Auftrag NICHT GEFUNDEN | — |
| — | `versandwerk`, Läufe 26–36 | „Elf Läufe endeten ohne Abnahme (26 bis 36) … Zehn davon an einem Instrumentfehler, einer — Lauf 26 — an meinem eigenen Ablauffehler“ (Q5 Z. 144–146) | Einzelstand je Lauf NICHT GELESEN | NICHT ERHOBEN |
| — (Liste v8) | T3 | v8 Z. 461: „Gefundene Messgerätfehler: Referenzlast zu kurz, keine Aufwärmung, Median aus drei, Ausfall-Blockade, Budgetgrenze nie scharf, sofortiger Ausfall bei Drosselung, Typsieb verzerrt die Mutanten, Inhaltsbefund als Absturz (zwei Bauarten, zwölf Stellen), Neutralrückgaben ungezählt, Maß optimierbar ohne Sache, „schneller aber falsch", Organe nicht verdrahtet, Laufzeit-Minimum, „nicht gemessen" als „nichts gefunden".“ Das sind 14 Einträge (g) | je Eintrag: die folgenden Zeilen | |
| Bauart 1, Bauart 2 | T3, bis Lauf 36 | „Inhaltsbefund als Absturz“: Bauart 1 an 4 Stellen, Bauart 2 an 8 Stellen, zusammen (g) 12 (Q5 Z. 148–161) | ja: an einer Stelle im Adapter; 1 Stelle wirft absichtlich | NICHT ERHOBEN |
| — | T3 | „Neutralrückgaben ungezählt“ | ja: Neutralzähler (`d6e6f8c`, R105; Q5 Z. 165) | NICHT ERHOBEN; belegt am echten Lauf 37 (Q5 Z. 67–79) |
| — | T3 | „sofortiger Ausfall bei Drosselung“ | ja: Wiederholung nach 2 s und nach 8 s (Q5 Z. 91–94) | NICHT ERHOBEN; belegt an 111 echten Ausfällen (Q5 Z. 86–94) |
| — | T3 | Referenzlast zu kurz; keine Aufwärmung; Median aus drei; Ausfall-Blockade; Budgetgrenze nie scharf | NICHT GELESEN | NICHT ERHOBEN |
| — | T3, Lauf 37 | „Typsieb verzerrt die Mutanten“: 28 von 128 geprüften Mutanten verworfen (Q5 Z. 60–65) | nein: offen („Offene Punkte für nach T3“ Nr. 5, Q5 Z. 188); v8 Tor 4 Zeile 3 verlangt die Verteilung | — |
| — | T3, Läufe 37, 38 | „Maß optimierbar ohne Sache“: Fehlalarmregel `detect-object-injection` (Q6 „Kernmaß ohne die Fehlalarm-Regel“; Q7 §4a) | Maßeichung eingehängt in `f821707` (Q7 §1); Vorbedingung 5 und 8 in Runde 1 | Runde 1: nur am Modul (vor-t4 BERICHT Z. 53) |
| — | T3, Läufe 37 (K2934) und 38 (K3121) | „schneller aber falsch“: Verhaltensvergleich fehlte im Annahmepfad (Q7 Z. 12–19; PH Z. 428, 431) | TS: eingehängt `f821707`; Python: Sonde ab Runde 2; weiter Runden 2–6 (§3) | ja: Nachspiel durch den Annahmepfad (Q7 §2) |
| — | T3 | „Organe nicht verdrahtet“ | ja: Verdrahtungstest (Q7 §3) | ja: Regressionstest |
| — | T3, Lauf 37 | „Laufzeit-Minimum“; Laufzeit-Grenzmaße entscheiden nach Rauschen (Q7 §7) | Median, später gepaart (Vorbedingung 1 in Runde 1) | ja: K2904/K3091 gleich entschieden erst in Runde 4 („drei von drei gleich“, PH Z. 467) und in Runde 5 (je 3 von 3, vor-t4-05 BERICHT Z. 35–37) |
| — | T3, Lauf 37 | „nicht gemessen“ als „nichts gefunden“: zwei Durchläufe von Generation 0 mit je 100 von 100 neutral (Q7 §5) | Vorbedingung 6 in Runde 1 | ja: Nachstellung 5 Mutanten (Q7 Z. 309–315); Laufweg (vor-t4 BERICHT Z. 54) |
| Nr. 1–21 | T3, REVIEW-03 | 21 Befunde: 3 hoch, 9 mittel, 9 niedrig (R69 §1). „Code-Befunde des Reviews nicht in T3 behoben, sondern als rote Spezifikation für T4“ (Q7, Eigene Entscheidung 5) | über Runde 1 (Vorbedingungen 1–11) | rote Spezifikationen |
| — | T3, Lauf 38 | Behauptung nur für Treffer aufgezeichnet: 9 von 87; die Torzeile Doppelung ist nicht messbar (Q7 §4e) | ja: `aegis.py:991–993` „Behauptung für ALLE erzeugten Angriffstests“ (Vorbedingung 9) | ja: Laufweg `aegis.pruefen` (vor-t4 BERICHT Z. 57) |
| — | T3 | Immunisierung auf dem TS-Pfad: `_anhaengen` 0 von 0 (Q7 §4f) | Vorbedingung 9 („3.10 F3“) in Runde 1 | Kammer (vor-t4 BERICHT Z. 57) |
| — | T3, Lauf 38 | Schwäche S1 am Gegenzeugen „weg“, gegen die Normalversion aber verändert (Weißraum); am Kandidaten K3044 alle 12.206 Ausdrücke mit Zeilenumbruch abgewiesen (vor-t4-02 BERICHT Z. 93–101) | Zählung berichtigt; die doppelte Prüfung gilt für künftige Werke (R4-18, Runde 4) | ja: Harness S1 |

## 3. Behebungsrunden vor T4 (23.–25.09.)

Alle Runden ohne Lauf und ohne Modellgeld. Befundzahlen je Review: R69 §1.

| Runde, Ordner | Kern | Befunde | Ergebnis laut Titel | Übergang |
|---|---|---|---|---|
| 1 `biotop-vor-t4` | `58bd9f9` (PH Z. 446), `330b4ec` (BERICHT §1) | 11 Vorbedingungen (BERICHT §1, Z. 47–59); REVIEW 15 Befunde: 2 hoch, 9 mittel, 4 niedrig | „nicht abnahmereif — TS-Pfad gebaut; S1 an K2868 nicht sauber behoben, Verhaltensvergleich für Python fehlt, K2904/K3091 in 1 von 3 Durchgängen verschieden entschieden“ | Entscheidungen (1)–(5), PH Z. 452 |
| 2 `biotop-vor-t4-02` | NICHT GELESEN | REVIEW 22 Befunde: 6 hoch, 9 mittel, 7 niedrig; „5 gemessene Lücken“ der Python-Sonde | „nicht abgenommen — Gegenprobe K2904/K3091 nur 2 von 3; …“ | S-1 … S-13 |
| 3 `biotop-vor-t4-03` | NICHT GELESEN | REVIEW 18 Befunde: 4 hoch, 5 mittel, 9 niedrig; „vier neue gemessen“ | „nicht abgenommen — K2904/K3091 wieder nur 2 von 3 (Vergleichslast); die fünf Lücken der Python-Sonde sind für ihre Probenfälle geschlossen …“ | R4-1 … R4-20 |
| 4 `biotop-vor-t4-04` | `1d9a5aa`, Nachtrag `43b8fad` (vor-t4-04 BERICHT Z. 95; Commit-Zeile im Zwischenbericht, R51) | REVIEW 18 Befunde: 2 hoch, 8 mittel, 8 niedrig | „Gegenproben der Entscheidungen 1, 3 und 4 erfüllt; die vier hohen Befunde sind für ihre Probenfälle geschlossen, die Fehlerklassen nicht (Review: 2 neue hohe Befunde, an Runde 5)“ | R5-1 … R5-14 |
| 5 `biotop-vor-t4-05` | `0c2f058` | REVIEW 11 Befunde: 3 hoch, 5 mittel, 3 niedrig; verworfener erster Durchgang 12 | „nicht abgenommen — … zwei Messfehler derselben Klasse …, die vor T4 behoben sein müssen (R6-1, R6-4)“ | R6-1 … R6-15, U-1 … U-4 |
| 6 `biotop-vor-t4-06` | kein Commit (Stand 12:55) | Befund S1 und Befund S1b: je ein gemessener stiller Durchlass (UEBERGABE Z. 173–174, 220–221) | läuft; Endstand trägt Hermes nach | S1c läuft |

**Stand je Kennung** (abgelesen aus der Tafel der jeweils folgenden Runde):

**S-1 … S-13** (Runde 2 → 3, `biotop-vor-t4-03/BERICHT.md` Z. 227–239)
- gebaut: S-1 … S-6 und S-8 … S-12 (11);
- S-7 gemessen (2×2);
- S-13: Entscheidungen, von Chat-Claude getroffen.
- Nachweisart (Spalte 5 der Tafel):
  - Laufweg bei S-1, S-3 (Lücke 3), S-4, S-5 und S-6 (Python); S-2 Laufweg für Python, für TS nur Rauchprobe;
  - Nachspiel bei S-7 und S-8; S-9 Laufweg gestellt und Nachspiel echt;
  - Organ bei S-10 (mit echter Kammer) und S-12 („nur Organ“); S-11 Unit.
- Offen blieb der Laufweg-Beleg für S-12 und S-3 (Wurzelmodul): R4-19, auf der Liste.

**R4-1 … R4-20** (Runde 3 → 4, `biotop-vor-t4-04/BERICHT.md` Z. 195–214)
- gebaut 16: R4-1 … R4-6, R4-8, R4-9, R4-10, R4-12 … R4-16, R4-18, R4-20;
- teilweise 1: R4-7;
- gemessen 1: R4-11;
- Liste 2: R4-17 (TS-Methoden, vor T5) und R4-19.
- Summe (g) 16 + 1 + 1 + 2 = 20.

**R5-1 … R5-14** (Runde 4 → 5, `biotop-vor-t4-04/SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md` Z. 11–24)
- R5-1 … R5-13 sind den Entscheidungen 1–8 zugeordnet; R5-14 „nicht entschieden: Liste“.
- Runde 5: „Die Fälle aus Review 04 sind geschlossen (Vorher/Nachher, 27 Fälle): 9 von 27 grün an `43b8fad` …, 27 von 27 an
  `0c2f058`“ (BERICHT Z. 32–34).
- Ein Stand je R5-Kennung ist NICHT ERHOBEN; die Fälle sind nach Review-Nr. geführt.

**R6-1 … R6-15** (Runde 5 → 6)
- Stand: offen, Runde 6 nicht abgeschlossen.
- Rote Spezifikation an `0c2f058`: R6-1, R6-2, R6-4 (BERICHT Z. 22–31; SPEZ Z. 9–12).
- Teilläufe Runde 6 (UEBERGABE):
  - S1: vorher 57 von 74 rot; Durchgang 3 288 von 288 grün, Stück 9 fehlt (Z. 170–173);
  - S2: 62 + 16 + 1 grün (Z. 151–153);
  - S3: 121 + 4 grün; VORHER-NACHHER-S3 gestrichen, weil es aus einer Sperrumgehung stammt (Z. 153–156, 164);
  - S4: vorher 26 rot, 10 grün (Z. 185–186);
  - M2(b): `test_m2_*` vorher 19 von 28 rot an `0c2f058`, nachher 28 von 28 (Z. 213–216).
- Voller Verdrahtungstest 8 von 8, Register 68 von 68 Kanten: ausdrücklich „Vorprüfung, nicht … Beleg der Runde“ (Z. 202–210).

**U-1 … U-4**
- „0 von 4 stille Durchlässe, alle bleiben auf der Liste“ (UEBERGABE Z. 103–104; `EINORDNUNG-U1-U4.md`).

**Stille Durchlässe in Runde 6**
- Befund S1: `_Konto.buchen` → „0 Abweichungen, tragfähig“. Führt zu M2(b); gebaut, nicht committet.
- Befund S1b: nur ein Konstantenmodul geändert → „0 von 0“, tragfähig. Führt zu S1c, Wege A–D.
- Hermes zählte drei Wege mit `tragfaehig: True` ohne Beobachtung oder Enthaltung, dazu einen gemischten Fall (Z. 225–231).
- Stand: offen.

## 4. Zuordnung der Nummernkreise

| Nummernkreis | Bedeutung | wird zu | Quelle |
|---|---|---|---|
| Review Runde 1, Nr. 1–15 | Befunde Review vor-t4 | in BERICHT §1 genannt: Nr. 1, 2, 3, 4, 5, 6, 8c, 9, 10a, 11, 12; Rest NICHT ERHOBEN | vor-t4 BERICHT Z. 47–59 |
| Review Runde 2, Nr. 1–22 | Befunde Review vor-t4-02 | S-1 … S-13; „Lücke 1–5“ der Python-Sonde = S-1 … S-5 | vor-t4-03 BERICHT Z. 227–231 |
| S-1 … S-13 | Spezifikationen für Runde 3 | Runde 3 (Stand in §3) | vor-t4-02 SPEZ Z. 13–25 |
| Review Runde 3, Nr. 1–18 | Befunde Review vor-t4-03 | R4-1 = Nr. 1, R4-2 = 2, R4-3 = 3, R4-4 = 4, R4-5 = 6, R4-6 = 7, R4-7 = 8, R4-8 = 11, R4-9 = 12, R4-10 = 13, R4-11 = 9c und 14, R4-12 = 15, R4-13 = 16, R4-14 = 17; R4-15 … R4-20 aus dem Bericht | vor-t4-03 SPEZ Z. 10–29 |
| Review Runde 4, Nr. 1–18 | Befunde Review vor-t4-04 | R5-1 … R5-10 = Nr. 1–10; R5-11 = 14, 15; R5-12 = 16; R5-13 = 18; R5-14 = 17 | vor-t4-04 SPEZ Z. 11–24 |
| Entscheidungen 1–8 (Runde 5) | Chat-Claude, 24.09. | E1: R5-2, R5-3, R5-5, R5-10; E2: R5-1; E3: R5-4; E4: R5-6; E5: R5-7; E6: R5-8; E7: R5-9; E8: R5-11 … R5-13 | vor-t4-04 SPEZ, Spalte 5 |
| Review Runde 5, Nr. 1–11 | geltendes Review 05 | R6-6 = Nr. 1, R6-7 = 2, R6-8 = 3 und 6, R6-9 = 4, R6-10 = 5, R6-11 = 7, R6-12 = 8, R6-13 = 10, R6-14 = 6, R6-15 = 11 | vor-t4-05 SPEZ Z. 9–23 |
| R6-1 … R6-5 | aus Hinweisen und Offenen Punkten | R6-1: Hinweis Philipp, Bezug Review 04 Nr. 4 (Spalte 2); R6-2: Philipp 24.09.; R6-3: Philipp 24.09. (Offen Nr. 5); R6-4: eigener Befund nach dem Commit (BERICHT Z. 27), Offen Nr. 1; R6-5: Offen Nr. 4, Spalte 5 nennt „Entscheidung 4“ (der Runde 5) | vor-t4-05 SPEZ Z. 9–13; PH Z. 473 |
| erster Durchgang Review 05, Nr. 1–12 | verworfen | U-1 = Nr. 7, U-2 = 11, U-3 = 12, U-4 = 10(e) | vor-t4-05 SPEZ Z. 29–32 |
| Entscheidungen 1–8 (Runde 6) | Chat-Claude, 24.09. | E1: R6-4 + R6-6; E2: R6-7; E3: R6-1 + R6-8 + R6-10; E4: R6-3; E5: R6-2 + R6-12; E6: R6-11; E7: R6-9; E8: R6-5, R6-13 … R6-15 | UEBERGABE Z. 7–20; SPEZ Spalte 5 (Auslegung Hermes, wo die SPEZ die Entscheidung nicht nennt) |
| Bauteile S1, S2, S3, S4, S1b, S1c (Runde 6) | Teilaufträge an Subagenten | S1: E1, E2, E3, E7; S2: E5; S3: E4; S4: E6; S1b: M2(b); S1c: Wege A–F | UEBERGABE Z. 87–100, 178–183, 225–231 |
| M1, M2(a), M2(b) | Nachsteuerungen im Bau S1 | M1: „E2-Nachtrag, nur verhalten.py“; M2: „E3-Nachtrag 2, verhaltensvergleich.py“, (a) Besitzerregel; M2(b): unbeobachtet → Enthaltung | `bau/S1-PLAN.md` Z. 464–510; UEBERGABE Z. 178–181 |
| Befund S1, Befund S1b | stille Durchlässe | → M2(b) bzw. → S1c | UEBERGABE Z. 173, 220 |
| Vorbedingungen 1–11 (Runde 1) | aus v8 Abschnitt 8 | Liste 1–9 in ABSCHLUSS-03 §10 plus Nr. 10 (Gedächtnissperre) und Nr. 11 (Erreichbarkeit …) | vor-t4 BERICHT §1 |

**Kennungskollisionen, nur benannt:**
- „S1“ steht für drei Dinge: die Schwäche S1 der Werke (T3: `tarife`), das Bauteil S1 in Runde 6 und „Befund S1“.
- S-1 … S-13 sind dagegen Spezifikationen.
- Der Auftrag BIOTOP-LAGE-01 hat eigene Kennungen (WS, FK, LU, R).

## 5. Stand der Eichung „Generation minus eins“ vor dem letzten Lauf

**Was sie ist.** v8 Z. 182, wörtlich: „Vor Generation 0 prüft das Biotop sich selbst. Fünf Teile, in dieser Reihenfolge:“
1. Rauschmessung je Bereich;
2. bereichsweise Sperre;
3. die vier Proben am versiegelten Eichgegenstand: Nebenwirkung, Regression, Norm, Vertrag;
4. Fund-Neubewertung;
5. Eichkosten getrennt ausweisen.

Seit v7: jede Probe mit Gegenprobe, die fehlschlagen muss (Tor 4 Zeile 2, Teil 1 §6).

**Letzter Lauf.** Lauf 38 (T3, `versandwerk`), begonnen 2026-09-22T13:42:49Z (R63 T3 §J). Die höchste Lauf-id in STAMM
ist 25, in VB1 26 (R63 §J); R02 wurde nicht abgefragt. Seit dem 23.09. gab es keinen Lauf (Behebungsrunden ohne Lauf).

**Eichung vor Lauf 38** (Datenbank T3, `?mode=ro`)

| Teil | Messwert (a) | Quelle |
|---|---|---|
| Vorspann-Nachweis | Status `bestanden`, Protokoll #22635, `nachweis_sha256` 6c66ebd1… | R63 T3 §H |
| Rauschmessung | 5 Bereiche, erstellt 2026-09-22T13:46:29Z; Toleranz bericht 1,219, eingang 1,15, planung 1,216, tarife 1,15, zahlen 1,186; gesperrt 0 von 5 | R69 §4 |
| vier Proben | nebenwirkung, norm, regression, vertrag je `ausgefuehrt` true, `bestanden` true | R73 §1 |
| vier Gegenproben | je `ausgefuehrt` true, `bestanden` false (gescheitert, wie verlangt); `lauf_startet` true | R73 §1 |
| Eichgegenstand | id 3, `nach_bereich` `tarife`, Vertrag `tests/vertraege/test_vertrag_planung_tarife.test.ts`, versiegelt 2026-09-21T03:51:56Z; Begründung „liegt auf dem von der Verfassung als tragend benannten Pfad …“. Der Ausgangsbereich ist in R69 abgeschnitten und NICHT ABGELESEN; der Vertragsname nennt `planung_tarife` | R69 §4 |
| Eichkosten | im Nachweis unter dem Schlüssel `kosten`, nicht ausgelesen; Beträge gehören in KASSE | R73 |

Die Proben von Lauf 37 haben dieselben Befundtexte (R73 §1). Nachtrag 02 §5 wertet die Eichung von Lauf 37 als „gehalten“
(Teil 2, T3-2).

**Einschränkungen aus späteren Quellen, nur benannt**
- Die Norm-Probe war bis Reparatur 02 ein leerer Durchlauf (A11 = B-04, §1).
- Die Stufe-2-Last gab es vor Lauf 38 nicht. In Runde 5 verweigert der Vorspann ohne Stufe 2 (vor-t4-05 BERICHT §6).
- Die Stufe-2-Eichphase ist ein Bauteil von Runde 6 (S3). Sie ist nur am Drahtwerk gelaufen: versiegelt nach 8
  Kammerläufen, Spannweite alpha 0,108, beta 0,039 (UEBERGABE Z. 205–206). Das ist eine Vorprüfung, keine Eichung an einem
  Werk.
- Eine Eichung am T4-Werk hat nicht stattgefunden (T4 nicht begonnen).

## 6. Fehler in Hermes' eigenen Auswertungen (getrennt, nicht in §1–§3 gezählt)

- VB1 BERICHT Z. 113: „ein **Messfehler in meiner eigenen Auswertung**, vor der Meldung korrigiert“.
- NACHGANG-03 Z. 120: „eigener Messfehler in der ersten Fassung dieser Prüfung“ (gegen den Endstand geprüft).
- Phase 3, Zeile 2: Die Nachrechnung „maß Token statt Ziele“ (PH Z. 136).
- Phase 3 schätzte den Doppelungsanteil mit 83,6 %; gemessen wurden 68,5 % (Nachlauf §5).
- VB1: Review-Zeitlimit von 180 s; K2689 wurde nie ausgeführt (PH Z. 353).
- T3 (Q7, „Eigene Fehler“):
  - Die Datenbank wurde mit `immutable=1` gelesen; dabei fehlten 190 Protokollzeilen und 49 Kassenzeilen (Q7 Z. 495).
  - „Gegenproben gegen das Modul geführt statt durch den Laufweg“.
  - „Tor 2 Zeile 8 messbar gemacht“ war zu stark formuliert.
- Diese Offenlegung liest STAMM mit `immutable=1` nur bei einer -wal-Datei von 0 Bytes (geprüft vor und nach jeder
  Abfrage: R58, R63, R69). VB1 und T3 liest sie mit `mode=ro`; dabei wird die -wal-Datei mitgelesen.
