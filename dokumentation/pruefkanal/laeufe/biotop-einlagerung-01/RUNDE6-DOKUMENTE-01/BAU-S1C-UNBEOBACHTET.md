# Bauauftrag S1c (Runde 6): nie „tragfähig“ ohne Beobachtung — die Klasse „Wirkung außerhalb der Beobachtung“

Du baust einen Teil der Behebungsrunde 6 vor T4 des Biotop-Projekts. Antworte und schreibe auf Deutsch. Vor dir haben
S1, die S1-Fortsetzung und S1b am Verhaltensvergleich gebaut. Ihr Stand und ihre Überlegungen stehen in
`/root/biotop-vor-t4-06/bau/S1-UMSETZUNG.md`, `bau/S1B-PLAN.md` und `bau/S1-PLAN.md`. Lies zuerst `S1-UMSETZUNG.md` und
die Abschnitte zu M2(b) in `S1B-PLAN.md`.

## Anlass (gemessen von S1b, 25.09. 12:32, `/tmp/r6-s1b/befund-unbeobachtet.txt`)
- **Messung:** Ein Kandidat ändert nur ein Konstantenmodul (`probewerk/werk/konst.py`, `RATE = 19` → `7`), das die
  unveränderte Funktion `brutto` eines anderen Moduls liest.
- **Ergebnis:** Der Verhaltensvergleich gibt `grund_art` `unbeobachtet` („0 von 0“) und `tragfaehig: True` zurück, ohne
  `enthaltung`. `aegis.pruefen` lässt den Kandidaten `ueberlebt`. Das ist ein stiller Durchlass.

## Maßstab
- **Startregel für T4** (vorab gesetzt von Philipp): „T4 beginnt, sobald das Review dieser Runde keinen stillen
  Durchlass mehr findet — jede bekannte Lücke muss eine gezählte Enthaltung sein; Lücken, die sich nur enthalten, behebt
  T4 im Lauf.“
- **Vorbedingung 2** (Masterprompt v8): „unbeobachtet = Enthaltung“.
- **Entscheidung 3** (Chat-Claude): „Enthält sich eine geänderte Funktion, wird der Kandidat zurückgestellt“.
- **Folge:** Du schließt die **Klasse**, nicht den Fall. Der Verhaltensvergleich sagt „tragfähig“ nur über
  beobachtetes Verhalten. Jede vom Kandidaten geänderte Stelle, deren Wirkung die Sonde nicht beobachtet, ist eine
  gezählte Enthaltung (`enthaltung: True`) und führt zu `zurueckgestellt`. Nie „tragfähig“ ohne Beobachtung.

## Teil 1 — die Klasse schließen (je Punkt Probe und Gegenprobe)
Grundlage sind die Rückgabewege in `biotop/organe/verhaltensvergleich.py::pruefen` (gelesen von Hermes).

| Nr | Weg | Heute | Soll |
|---|---|---|---|
| A | `grund_art` `unbeobachtet`: keine Abweichung, 0 von y beobachtet | tragfähig, ohne Enthaltung → angenommen | Enthaltung → zurückgestellt |
| B | `grund_art` `sonde_vorgeneration_inhalt`: Vorgeneration mit Inhalt nicht beobachtbar | tragfähig, ohne Enthaltung → angenommen, ohne jeden Vergleich | Enthaltung → zurückgestellt |
| C | geänderte **Modulwerte** (Modulebene außerhalb von Funktions- und Klassendefinitionen) eines geänderten Moduls M, gelesen **außerhalb** beobachteter Funktionen | still, sobald sonst irgendetwas beobachtet ist (gemischter Fall) | Enthaltung → zurückgestellt |
| D | geänderte Dateien im **Quellpaket**, die keine Quellmodule sind (Daten- und Konfigurationsdateien, die das Werk zur Laufzeit lesen kann) | `keine_quellaenderung` bzw. still | Enthaltung → zurückgestellt |

**Einzelheiten:**
- **C, Python (Syntaxbaum):**
  - Geändert sind Namen, die auf Modulebene gebunden werden (Zuweisung, annotierte und erweiterte Zuweisung, Import,
    `global`-Ziele) und deren Anweisung sich unterscheidet, dazu neue und entfernte Namen.
  - Leser außerhalb von M sind: ein anderes Quellmodul, das N über `from M import N`, `from M import *` oder `M.N`
    bzw. einen Alias nennt; außerdem die Referenzlast.
  - Leser in M erfasst schon M2(b), denn ein geänderter Modulrest macht alle Funktionen von M direkt geändert.
  - Ein Modulrest ohne zuordenbaren Namen (Aufruf oder `if`/`for`/`try` auf Modulebene) führt zur Enthaltung.
    Ausgenommen sind der Modul-Docstring und ein `if __name__ == "__main__":`-Block, der beim Import nicht läuft.
    Beide Ausnahmen brauchen je eine Gegenprobe.
- **C, TypeScript (ohne Parser):** dieselbe Regel, soweit sie verlässlich bestimmbar ist.
  - Exportierte `const/let/var`-Deklarationen, deren Text sich ändert.
  - Leser über `import { N } from '…/m.js'` in anderen Modulen; `import type` und reine Typnamen sind ausgenommen.
  - Was sich so nicht verlässlich bestimmen lässt, ist bei TypeScript eine gezählte Enthaltung, nie still.
- **D:** Das Quellpaket ist bei Python jedes Verzeichnis, in dem ein Quellmodul des Werks liegt, samt Unterverzeichnissen;
  bei TypeScript ist es `src/`. Keine Enthaltung auslösen Dateien außerhalb davon (`README`, `docs/`, `tests/`) und
  Werkzeugdateien an der Wurzel; diese werden wie bisher gezählt.
- **Sprachunabhängig:** A, B und D gelten für beide Sprachen.

## Teil 2 — zwei Fehlalarme von M2(b) (von S1b gemeldet, Nr. 4 seines Schlussberichts)
| Nr | Heute | Soll |
|---|---|---|
| E | Jede **neue** öffentliche Funktion stellt zurück, weil sie an der Vorgeneration nicht beobachtet ist. | Eine Funktion, die es an der Vorgeneration nicht gibt, gilt als beobachtet, wenn der Kandidat eine Beobachtung von ihr hat. Ihre Wirkung auf das bestehende Verhalten läuft über geänderte, also selbst geprüfte, Aufruferinnen. Ist sie am Kandidaten nicht beobachtet, gilt M2(b) wie bisher. |
| F | Eine Funktion, die sich selbst ruft, gilt als Zyklus und damit als nicht gedeckt. | Ein Selbstaufruf zählt nicht als Aufruferin. Gegenseitige Rekursion bleibt „nicht gedeckt“. |

## Spezifikationen und Nachweis
- **Ablage:** anhängen an `tests/test_vor_t4_06.py`, Präfix `test_w_`. Wo das Organ im Annahmepfad wirkt, läuft der Fall
  durch `aegis.pruefen` in der echten Kammer, wie die `test_m2_*`.
- **Mindestfälle** je mit Soll:
  - A: `konst` (Befund S1b) → zurückgestellt. Gegenprobe: dieselbe Änderung plus ein Test, der sie festhält, und eine
    beobachtete Funktion, die die Konstante liest → geurteilt.
  - B: Vorgeneration mit Inhalt nicht beobachtbar → zurückgestellt.
  - C: gemischter Fall, Konstante außerhalb gelesen, dazu eine beobachtete geänderte Funktion → zurückgestellt.
    Gegenproben: nur innerhalb von M gelesen und beobachtet → geurteilt; Docstring; `__main__`-Block.
  - C, TypeScript: am Organ mit gestellter Sonde, wie `test_b3_ts_*`.
  - D: Datendatei im Quellpaket → zurückgestellt. Gegenprobe: `README.md` → geurteilt.
  - E: neue öffentliche Funktion, am Kandidaten beobachtet → geurteilt. Probe: neue Funktion, nirgends beobachtet →
    wie M2(b).
  - F: privater, selbstrekursiver Helfer einer beobachteten Funktion → gedeckt, geurteilt. Probe: gegenseitige
    Rekursion → Enthaltung.
- **Vorher** am aktuellen Baum (nach S1b) und an `0c2f058`: Proben rot an ihrer Zusicherung, Gegenproben grün. Anhängen
  an `bau/S1-VORHER-0c2f058.txt`, einordnen in `bau/S1-VORHER-EINORDNUNG.md`.
- **Bau:** `bau/r6_s1c_<teil>.py`, je Teil ein Skript, alles oder nichts mit zwei Lesungen. Erst an einer eigenen Kopie
  (`/tmp/r6-s1c/bau`), dann am Baum. Danach die Dateien von Kopie und Baum vergleichen.
- **Kosten** (`bau/S1C-KOSTEN.txt`), gemessen wie `bau/S1B-KOSTEN-M2B.txt`:
  - an `lagerhaus`, `logmuehle`, `uebungswerk-p2` und `/root/versandwerk-t3-02` (TypeScript);
  - je Werk: wie viele Module Modulwerte haben, die außerhalb gelesen werden, und was sich gegenüber S1b durch E/F
    ändert.
  - Nur berichten; die Regel ändert sich nicht, wenn die Zahl hoch ist.
- **Ältere Tests:** Ein älterer Test, der heute „tragfähig“ ohne Beobachtung zusichert (etwa
  `tests/test_t3_verhaltensvergleich.py` zu `unbeobachtet` und `sonde_vorgeneration_inhalt`), wird nur mit Grund
  angepasst. Die Gründe kommen in `bau/S1-GEAENDERTE-TESTS.md`.
- **Frühere Suche:** Die Liste der älteren Tests, die „ueberlebt“ erwarten, steht in
  `/root/biotop-vor-t4-06/sperre/SPERRE-04-AUSGABE.txt` (Suche von S1b, nach der Formatsperre ausgeführt).

## Teillauf (`bau/TEILLAUF-S1.txt`, Durchgang 5)
- **Stücke:** dieselben 1–9 wie `/tmp/r6-s1/teillauf.sh`, dazu `tests/test_t3_verhaltensvergleich.py` und
  `tests/test_t3_python_annahmen.py`.
- **Grenzen:** jedes Stück unter 400 s. Vor jedem Kammerstück prüfst du `/tmp/biotop-kammer-exklusiv`.
- **Ergebnis:** alles grün, oder jede Abweichung ist erklärt.

## Arbeitsweise (verbindlich)
- **Umgebung:** Python ist `/root/biotop-t3/venv/bin/python`; Tests laufen aus `/root/biotop` heraus.
  `TMPDIR=/tmp/r6-s1c`, `T3_EICH_BELEGE=/tmp/r6-s1c/eichbelege`.
- **Planen:** Plane nie den ganzen Umbau in einem Denkschritt. Plan und Stand stehen fortlaufend in `bau/S1C-PLAN.md`,
  so aktuell, dass ein Nachfolger übernehmen kann.
- **Laufzeiten:** keine Hintergrundprozesse; jeder Werkzeugaufruf unter 400 s.
- **Befehle:** Mehrteilige Befehle schreibst du von Anfang an als Skriptdatei.
- **Sperren:** Wird ein Befehl gesperrt oder läuft eine Freigabeabfrage ab, wartet genau diese Handlung. Nicht
  umformulieren, nicht aufteilen, nicht als Skriptdatei neu schreiben, kein anderer Weg. Befehl und Meldung trägst du
  wörtlich in den Plan und in den Schlussbericht ein.
- **Ausnahme, Formatsperre** („command parser limit or malformed executable payload“): Du führst das gespeicherte
  Skript unverändert aus, wenn es eine reine Lese- oder Testhandlung ist, die sonst jede Prüfung bestanden hätte. Das
  meldest du wörtlich (Regel Philipp 23.09.).
- **Neue Dateien in `bau/`:** nur mit dem Präfix `S1C-`/`r6_s1c_`, exklusiv angelegt. Die Dateien des Auftraggebers
  liegen unter `bau/hermes/` und sind tabu.
- **Verboten:** kein Commit, kein Modellaufruf, kein Netz.
- **Deine Dateien:**
  - `biotop/organe/verhaltensvergleich.py`, `biotop/kern/py/verhalten.py`, `biotop/kern/ts/*` (nur falls nötig);
  - `biotop/organe/aegis.py`, nur die Behandlung der Enthaltung;
  - `tests/test_vor_t4_06.py`, nur anhängen und patchen;
  - `tests/test_t3_verhaltensvergleich.py` und in `tests/test_vor_t4_0[2-5].py` nur Tests, deren Spezifikation sich
    ändert, jeweils mit Grund.
- **Andere Dateien:** Brauchst du eine Änderung anderswo, hältst du sie als offenen Punkt fest.

## Schlussbericht (deine letzte Antwort)
- geänderte Dateien mit sha256;
- Vorher der `test_w_*` (x von y rot, an beiden Ständen);
- Teststand Durchgang 5 (x von y);
- Kosten je Werk;
- offene Punkte;
- Sperren (wörtlich).
- Außerdem: Welche Wege von `verhaltensvergleich.pruefen` liefern nach deinem Bau noch `tragfaehig: True`? Je Weg mit
  Begründung, warum dort Verhalten beobachtet ist (Rückgabewege lesen und aufzählen).
