# T3 — Lauf 38: Budgetabbruch, und ein Befund über meine eigene Arbeit

Stand: 2026-09-22. Lauf 38 endete am Budget — das vorab genannte zulässige Ende.
Verbrauch **9,7286 € von 10,00 €**, 2603 Modellaufrufe.

## Das Ergebnis von Lauf 38

**Kernmaß −28 → −6**, deutlich besser als Lauf 37 (dort −14). Acht angenommene
Generationen (ohne Gen 0), neun abgelehnte.

| Gen | Status | Messung |
|---|---|---|
| 1 | angenommen | `bericht.tote_funktionen` 1→0; `tarife.tests_fehlgeschlagen` 3→0; Sicherheit sinkt |
| 4 | angenommen | `planung.sicherheit_punkte` 2→0 |
| 5 | angenommen | `bericht.sicherheit_punkte` 4→1 |
| 9 | angenommen | `eingang` Laufzeit 2,79 → 2,25 ms |
| 10 | angenommen | `tarife.sicherheit_punkte` 3→1 |
| 12 | angenommen | `eingang.tests_fehlgeschlagen` 2→0 |
| 13 | angenommen | `tarife.sicherheit_punkte` 1→0 |
| 16 | angenommen | `zahlen.sicherheit_punkte` 7→5 |
| 2,3,6,7,8,11,14,15,17 | abgelehnt | kein Kandidat überlebte den Ankläger |

Kernmaß-Verlauf: −28 → −16 → −14 → −11 → −9 → −8 → **−6**. Sicherheitspunkte 27 → 6,
tote Funktionen 1 → 0, Testfehler durchgehend 0, Testbestand 207 → 213.

## Der Befund: die Abwehr lief nicht

**Ich habe den Verhaltensvergleich und die Maßeichung gebaut, getestet, committet — und
nicht in den Prüfpfad eingehängt.** Gemessen:

```
grep -rn "verhaltensvergleich" biotop/ --include=*.py  → nur die Moduldatei selbst
grep -rn "masseichung"         biotop/ --include=*.py  → nur die Moduldatei selbst
```

Lauf 38 lief damit **ohne** die Abwehr, die ihn schützen sollte. 18 Tests waren grün,
drei Gegenproben am echten Lauf 37 bestanden — und keine dieser Prüfungen stellte die
Frage, ob das Modul jemals gerufen wird. Genau der Fehler, den ich beim Neutralzähler
schon einmal gemacht und dort ausdrücklich festgehalten hatte: *proving a call site can
book is not proving the run books*.

### Was das gekostet hat

Kandidat **K3121** (Gen 5, `zahlen`, Annahmegrund „zahlen.laufzeit_ms 2,86 → 0,98 ms,
−66 %") baute **denselben Fehlertyp erneut ein** — diesmal nicht als WeakMap, sondern als
Single-Entry-Cache über Modulvariablen:

```ts
let letzteQuelle: readonly number[] | null = null;
let letzteLaenge = -1;
let letzteSortiert: number[] = [];

function geordnet(werte: readonly number[]): number[] {
  if (werte === letzteQuelle && werte.length === letzteLaenge) {
    return letzteSortiert;          // identische Referenz + gleiche Länge = Treffer
  }
  ...
}
```

Am Endstand gemessen: `spannweite` liefert nach Mutation desselben Arrays **8 statt 80**.
(`quantil` ist zufällig korrekt, weil eine spätere Generation den Cache-Schlüssel wieder
verschob — nicht, weil der Fehler behoben wurde.)

### Die Sonde hätte ihn gefangen

Nachgeholt gegen die Lazarus-Stände Gen 4 und Gen 5:

| Beobachtung | vor K3121 | nach K3121 |
|---|---|---|
| `quantil@einzeln` | 3 | 3 |
| `quantil@nach_mutation` | **300** | **3** |
| `quantil@alias` | **300** | **3** |
| `spannweite@einzeln` | 2 | 2 |
| `spannweite@nach_mutation` | **200** | **2** |
| `spannweite@alias` | **200** | **2** |

4 von 4 Abweichungen ungedeckt → **tragfähig: False**. Der Kandidat wäre abgelehnt
worden. Der Einzelaufruf bleibt in beiden Ständen gleich — nur die Folge- und
Alias-Muster zeigen den Fehler, genau wie gebaut.

Beleg: `NACHTRAG-7-K3121.txt`, `NACHTRAG-7-K3121.json`.

## Neutralzähler Lauf 38

| Organ | geurteilt | neutral | Anteil |
|---|---|---|---|
| `aegis.behauptung` | 51 | 0 | 100 % |
| `gedaechtnis.aenderungsziel` | 328 | 102 (`diff_nicht_anwendbar`) | 76,3 % |
| `generation0._testlauf` | 400 | 0 | 100 % |

Alle drei über der Hälfte; die Torzeilen tragen.

## Kasse

| | Aufrufe | EUR |
|---|---|---|
| Lauf 38 | 983 | 4,2516 |
| **Auftrag gesamt (26–38)** | **2603** | **9,7286 von 10,00** |

Restbudget **0,2714 €**. Ein weiterer Evolutionslauf ist damit ausgeschlossen: Lauf 38
verbrauchte 4,25 € für 17 Generationen, eine einzelne Generation kostet im Mittel 0,25 €.

## Was daraus folgt

Der Lauf zeigt zwei Dinge gleichzeitig:

1. **Das Messgerät trägt.** Kernmaß halbiert und nochmals halbiert (−28 → −6), 9 von 17
   Generationen angenommen, alle Ablehnungen mit Begründung, Neutralzähler über der
   Schwelle.
2. **Die Abwehr gegen „schneller, aber falsch" fehlt weiterhin im Lauf.** Sie existiert
   als geprüftes Modul, ist aber nicht angeschlossen. Der Fehlertyp wurde in Lauf 38
   ein zweites Mal eingebaut, in neuer Form, und wieder nicht bemerkt.

Der zweite Punkt ist kein Argument gegen die Abwehr, sondern für sie — und zugleich ein
Beleg dafür, dass ein grüner Testlauf über ein Modul nichts darüber sagt, ob das Modul
im Betrieb erreicht wird. Diese Lehre steht bereits in
`measurement-harness-discipline/SKILL.md`; ich habe sie geschrieben und im selben Auftrag
erneut verletzt.

## Offen

- **Einhängen von `verhaltensvergleich` und `masseichung` in `aegis.pruefen`**, mit
  Nachweis, dass sie im Lauf gerufen werden (Zähler wie beim Neutralzähler), nicht nur
  mit Modultests.
- Der Cache-Fehler in `zahlen/statistik.ts::geordnet()` steht im Endstand von Lauf 38.
- Restbudget 0,2714 € reicht für keinen weiteren Evolutionslauf.
