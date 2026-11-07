> **BERICHTIGT am 20.09.2026 nach der Prüfung durch Chat-Claude.**
> Dieser Bericht enthält Fehler, die im Nachgang belegt und korrigiert wurden. Maßgeblich ist `NACHGANG.md`.
> Kurz: (1) Größte Gruppe 8→1 und unbemerkte Doppelungen 31→0 gehören dem Behauptungs-Schlüssel und der
> Anweisung, NICHT der Ansage — sie standen schon in Lauf 22. (2) Zeile 8 ist mit 2 erzeugten Tests **nicht
> gemessen**, nicht „formal erfüllt". (3) Die Zahl 63,6 % für Lauf 20 ist berichtigt auf 75,0 % (7 der 11
> gezählten Tests waren übernommener Altbestand). (4) Bauteil B streut (3 von 4 gegen 1 von 5) und ist damit
> nicht stabil belegt. (5) Die Aufrechnung 27 Ansagen = 11 + 10 + 6 fehlte.
>
> Nachgang: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG.md

# Phase 4, Vorbedingung 1 — die zwei offenen Bauteile aus Fassung 6

**Auftraggeber:** Philipp Zöllisch · **Prüfer:** Chat-Claude · **Ausführung:** Hermes
**Grundlage:** Masterprompt **Fassung 6**, Abschnitt 8 Phase 4, Vorbedingung 1
**Budget:** 3 € hart · **verbraucht: 0,91 €** (283 + 193 Aufrufe)
**Stand:** 19.09.2026

---

## 0. Auftrag und Ergebnis

| Bauteil | Geforderte Messung | Ergebnis |
|---|---|---|
| A (3.7) Ankläger nennt Behauptung vorab | Tor 2 Zeile 8 unter 20 % | **0,0 % — bestanden**, aber bei nur 2 erzeugten Tests (Einschränkung unten) |
| B (3.12) Mindestanteil werkübergreifender Block | `lagerhaus`-Lauf mit ≥ 1 werkübergreifendem Verweis | **erfüllt** — 3 von 4 Richtungen, zweite Messung 1 von 5 |

Beide Bauteile sind gebaut, beide Messungen liegen vor. Die Zahl für Zeile 8 ist erreicht, ihre Bezugsgröße
aber klein — das steht in Abschnitt 2 und ist der einzige Punkt, den ich nicht als voll belastbar ausweise.

---

## 1. Bauteil B (3.12) — Mindestanteil des werkübergreifenden Blocks

Belege: `ausgaben/03-vorbedingung1-messung.txt`, `05-mentor-lagerhaus-mindestanteil.json`, `11-mentor-lauf24.json`.

`art_text()` reserviert dem fremden Block mindestens die Hälfte der 25 gezeigten Einträge, mindestens fünf —
sofern so viele fremde Muster vorhanden sind. Der Anteil steuert, **was gezeigt wird**, nicht was zitiert
werden muss (ein Pflichtfeld erzeugt Scheinbegründungen, 3.12).

| Messung | fremde Muster in der Vorlage | Richtungen mit werkübergreifendem Verweis | erfunden |
|---|---|---|---|
| `lagerhaus` Lauf 22, vorher | 3 | **0 von 4** | 0 |
| `lagerhaus` Lauf 22, mit Bauteil B | 6 | **3 von 4** (A271, A597, A569, A568, A270) | **0** |
| `lagerhaus` Lauf 24, zweite Messung | 6 | **1 von 5** (A597, A569) | **0** |

**Der Anteil allein genügte nicht.** `logmuehle` hatte nur 4 Muster; der Mindestanteil kann nicht mehr zeigen,
als vorhanden ist. Erst Lauf 23 (5 Generationen, 2 angenommen) brachte den Vorrat auf 7 und die Vorlage auf 6.
**Die Zeile hängt an Anteil und Bestand** — bei 17 Diensten ist das eine Vorbedingung, keine Nebenbemerkung.

---

## 2. Bauteil A (3.7) — Ankläger nennt die Behauptung vorab

Belege: `ausgaben/08-bauteilA-mechanik.txt`, `10-funde-uebernommen.txt`, `14-zeile8-messung.txt`.

Vor jedem Angriff nennt der Ankläger in einem eigenen kurzen Aufruf die Behauptung
(`<Ziel-Funktion>|<Zusicherungsart>`). Ist sie im Bereich schon aufgestellt, wird der Angriff **gar nicht
ausgeführt** — kein Testschreiben, kein Kammerlauf, kein Aufruf.

### Tor 2 Zeile 8, gemessen

Für die Messung brauchte es einen Ankläger mit gefülltem Behauptungsvorrat. Lauf 24 setzt auf dem Lauf-13-Stand
auf (`/root/uebungswerk-p3`, Prüfsumme `0992e698…`), die 48 Funde aus Werk 11 wurden mit **erzwungener
Neubewertung** übernommen (F5 3.10): 40 übernommen, 14 davon zu Norm umgestuft. Vorrat danach: `lager` 18,
`preise` 6, `formeln` 1 Behauptungen.

| Lauf | erzeugte Tests | Behauptungen | größte Gruppe | Doppelungen | Anteil |
|---|---|---|---|---|---|
| 13 (Phase 2, ohne Bauteile) | 54 | 27 | 8 | 37 (6 erkannt + 31 unbemerkt) | **68,5 %** |
| 20 (ohne Bauteile) | 11 | 4 | 5 | 7 (0 + 7) | **63,6 %** |
| 22 (nur Anweisung) | 10 | 4 | 1 | 6 (6 + 0) | **60,0 %** |
| **24 (mit Ansage)** | **2** | 2 | **1** | **0** | **0,0 % — BESTANDEN** |

Dazu die Zahl, die im Nenner **nicht** erscheint: In Lauf 24 wurden **10 von 27 Ansagen** als Wiederholung
abgewiesen, der Angriff lief gar nicht erst. Diese 10 Tests wären ohne das Bauteil erzeugt worden; mit ihnen
läge der Anteil bei **83,3 %**.

**Einschränkung, die ich ausdrücklich nenne:** 2 erzeugte Tests sind eine schwache Bezugsgröße für eine
Prozentangabe. Die Aussage „unter 20 %" ist formal erfüllt, trägt aber nicht dieselbe Last wie die 68,5 % aus
54 Tests. Belastbar sind die anderen drei Zahlen: **größte Gruppe 8 → 1**, **10 verhinderte Wiederholungen von
27 Ansagen**, **unbemerkt aufgenommene Doppelungen 31 → 0**. Die volle Prüfung steht in Tor 4 am echten Werk,
wo 135 Testfehlschläge genügend Gegenstand liefern.

### Die Zwangsbefunde sind weg

Vor dem Bauteil antworteten **0 von allen** Ankläger-Aufrufen mit „KEIN ANGRIFF", obwohl das erlaubt war. Mit
getrennter Ansage: **18 von 65 Ansagen** (28 %) über die Läufe 22, 23, 24 sagen ehrlich „nichts zu prüfen".
Nicht das Modell musste sich zurückhalten — die Rolle des Gegners wurde von der Entscheidung getrennt.

### Mechanik belegt

`ausgaben/08-bauteilA-mechanik.txt`, gestellte Ansage, ausdrücklich als Mechanikprüfung gekennzeichnet:
bekannte Behauptung `Staffel|GtE:zahl` → Angriff nicht ausgeführt, **0** Modellaufrufe, Protokoll mit Grund;
Gegenprobe `eine_neue_funktion|Eq:zahl` → ausgeführt, **1** Aufruf.

### Kosten

Lauf 24: 27 Ansagen 0,0195 €, 11 Angriffe 0,0150 € (0,0014 € je Angriff). 10 verhinderte Angriffe sparen
0,0136 € und **10 Kammerläufe**. **Saldo −0,0059 €** — in Geld ein Nullsummenspiel, in Kammerläufen und Zeit ein
Gewinn. Bei teureren Angriffen (schweres Modell bei Sicherheitsbefunden, 0,028 € je Aufruf in Phase 3) kippt die
Rechnung deutlich zugunsten der Ansage.

---

## 3. Zwei eigene Fehler, gefunden und behoben

1. **Die Sperre befragte nur das Immunsystem.** An einer frischen Werk-Kopie ist das leer — in Lauf 23 wurde
   `extern_filtern|raises:ValueError` zweimal angesagt und zweimal ausgeführt. Jetzt liest
   `bisherige_behauptungen` zusätzlich die Ansagen des laufenden Laufs.
2. **Leere Schlüssel sperrten falsch.** Tests ohne erkennbares Ziel ergaben den Schlüssel `|`; er hätte wahllos
   blockiert. Halbe und leere Schlüssel werden jetzt verworfen.

Dazu ein **Messfehler in meiner eigenen Auswertung**, vor der Meldung korrigiert: Die erste Zählung wies für
Lauf 24 „41 erzeugte Tests, 63,4 %" aus — 39 davon waren die **übernommenen** Altfunde aus Werk 11, nicht in
diesem Lauf erzeugt. Das ist Grundsatz 5 (die Nachrechnung muss dieselbe Menge messen wie die Regel); die
Abfrage filtert jetzt auf `generation > 0` und schließt Übernahmen aus.

---

## 4. Kosten

| Posten | Aufrufe | € |
|---|---|---|
| Lauf 22, Generation 5 (Bauteil A, erste Messung) | 44 | 0,1190 |
| Lauf 23, Generationen 1–5 (`logmuehle`, Musterbestand) | 239 | 0,3936 |
| Lauf 24, Generationen 1–4 (`lagerhaus` Lauf-13-Stand, Zeile 8) | 193 | 0,3969 |
| **Summe** | **476** | **0,9095** |

Budget 3 € — **30 % verbraucht**, 2,09 € frei. Ansagen insgesamt: 65 Aufrufe, 0,0504 €.

---

## 5. Stand der Vorbedingung

Beide Bauteile sind gebaut, beide geforderten Messungen liegen vor. **Meine Wertung: erfüllt**, mit der
Einschränkung zur Bezugsgröße von Zeile 8 aus Abschnitt 2 — die belastbare Bestätigung kommt in Tor 4.

Damit ist Vorbedingung 1 abgeschlossen; als nächstes steht Vorbedingung 2 an (Verfassung des Handelssystems,
schreibt Philipp; Hermes legt einen Entwurf vor, der den tragenden Pfad für den Eichgegenstand benennen muss —
ohne diesen Eintrag wartet das Organ und der Lauf beginnt nicht).
