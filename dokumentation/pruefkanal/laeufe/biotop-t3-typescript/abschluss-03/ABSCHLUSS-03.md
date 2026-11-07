# T3 TypeScript — abschluss-03: **nicht abgenommen**

Stand 2026-09-23. Auftrag „Budget 10 € hart“: verbraucht **9,728638 € von 10,00 €** (2603 Buchungen, Läufe 26–38; §6).
Dieser Abschluss kostete 0,00 €: kein Modellaufruf, kein weiterer Lauf an T3. Kammerläufe (Docker, netzlos) kosten nichts.
Kern-Commit: **`f821707`**, Vorgänger `1cf2eb1` (Kern von Lauf 38), 13 Dateien, +1294/−63 (`KERN-COMMIT.patch.txt`).
Die Lauf-DB ist über einen Schnappschuss mit WAL gelesen (`SCHNAPPSCHUSS.txt`); das Original war vorher und nachher
prüfsummengleich. Nach einem Reviewdurchgang überarbeitet (`REVIEW-03.md`, 21 Befunde; Umgang in §9).

**Warum T3 nicht abgenommen ist**
- Die Halluzinationsprobe ist in Lauf 37 und in Lauf 38 gerissen.
- Tor 2 Zeile 8 und 3.10 F3 sind nicht gemessen bzw. nicht belegt.
- Die Abwehr gegen „schneller, aber falsch“ lief in keinem der beiden Läufe mit.

**Was seit `f821707` gilt**
- Die Abwehr ist eingehängt. Nachgespielt durch den Annahmepfad hätte sie in Lauf 38 alle 3 Änderungen am sauberen Bereich
  abgewiesen.
- Die 4 Änderungen, die versiegelte Schwächen beheben, kommen durch. Eine davon, die S2-Behebung, allerdings nur, solange
  eine **Einzelmessung** der Laufzeit über 15 % liegt (§2).
- Ein Lauf mit Abwehr hat nie stattgefunden. Was er insgesamt erreicht hätte, ist nicht gemessen.

**Entscheidungen von Chat-Claude (23.09.), umgesetzt**
- Sperre 3 wird nicht aufgelöst. S1–S5 sind selbst gemessen (§4c). Die Dateien des Unteragenten sind nicht verwendet.
- Laufzeit: Median mehrerer Messungen je Seite statt Einzelmessung, Schwelle unverändert. Das ist die erste Änderung vor
  T4, mit der Gegenprobe „K2904 und K3091 werden gleich entschieden“ (§10).

---

## 1. Einhängen — `verhaltensvergleich` und `masseichung` im Annahmepfad

Die Annahmefunktion ist `aegis.pruefen`. Ein Lauf ruft sie je Kandidat auf, aus `lauf._generation_koerper` und aus
`lauf._verhandeln`; im Vorspann rufen die Eichproben sie ebenfalls.

1. **Maßeichung.** Beide Seiten des Paars werden mit derselben Eichung bewertet (`masseichung.anwenden`), bevor das Maß
   urteilt.
   - Die Eichung entsteht im Vorspann: `masseichung.eichen` am sauberen Vergleichsbereich der Verfassung, versiegelt im
     Vorspann-Nachweis.
   - Regeln, die dort anschlagen, zählen nicht. Ihre Befunde bleiben als `sicherheit_stillgelegt` sichtbar.
   - Dieselbe Eichung gilt im eingefrorenen Ausgangsmaß und in der Generalprobe. Für Generationen und Nachspiel stellt
     `lauf.annahme_tausch` diesen Aufbau her; für die Eichproben baut ihn der Vorspann selbst.
   - **Nebenwirkung** (Review Nr. 12): Schwarm und Ankläger lesen ihre Befunde aus dem gespeicherten, jetzt geeichten Maß.
     Stillgelegte Befunde fallen damit aus der Aufgabe des Schwarms. Das schwere Angriffsmodell wird nur bei Befundklassen
     gewählt; in Lauf 37/38 griff es `zahlen` wegen `detect-object-injection` an (Beleg K2934: `anthropic/claude-sonnet-5`).
     Ob Schwarm und Befundklassen roh oder geeicht lesen sollen, entscheidet Philipp (§10).
2. **Verhaltensvergleich.** Er läuft für jeden Kandidaten, der das Maß besteht.
   - Vorgeneration und Kandidat durchlaufen in der Kammer dieselbe Sonde (`kern/ts/verhalten*.mjs`). Korpus ist die
     Referenzlast.
   - Je exportierter Funktion der geänderten Module zeichnet die Sonde die **ersten 8 äußeren Aufrufe** auf (`KAPPE`), je
     mit `@alias`, `@mutation` und `@nach_ruecksetzung`. Verschachtelte Aufrufe beobachtet sie nicht.
   - Jede Abweichung braucht einen deckenden Test. Er muss an der Vorgeneration fallen, am Kandidaten bestehen und die
     Funktion aufrufen. Ist eine Abweichung ungedeckt, wird der Kandidat abgelehnt.
   - **Grenzen, im Review gefunden und bestätigt:**
     - Ruft die Referenzlast keine Funktion eines geänderten Moduls, urteilt das Organ trotzdem „keine Abweichung“ statt
       sich zu enthalten (Nr. 2).
     - Fällt die Sonde aus, wird der Kandidat abgelehnt, und die Ablehnung geht ins Projektgedächtnis (Nr. 3).
     - Beides ist nicht behoben, sondern als rote Spezifikation Vorbedingung für T4 (§10). In den 33 Nachspielen trat ein
       Sondenausfall 0-mal ein.

**Tests**
- Die Tests habe ich **nach** dem Code geschrieben (eigener Fehler). Den Rot-Nachweis habe ich nachgeholt:
  - Organtests gegen `1cf2eb1`: 14 von 26 rot, das sind alle neuen. 12 von 26 bleiben grün, weil sie schon dort standen
    (`ROT-GEGEN-1cf2eb1-ENDSTAND.txt`).
- Volle Regression: **404 bestanden, 2 übersprungen, 93 abgewählt** (891 s; `REGRESSION-ABSCHLUSS3.txt`).
  - Gelaufen am Arbeitsbaum, der unverändert als `f821707` committet wurde (`VOR-REVIEW.txt`: `git status` leer).
  - Gesammelt 390 → 406 (`JOB4-SAMMLUNG-EICHPFAD.txt`).
- Eichpfad T3 mit 4 echten Paaren in der Kammer: 4 von 4 nach dem Einbau und erneut 4 von 4 am Commit
  (`EICHPFAD-COMMIT.txt`).

## 2. Gegenproben durch den Annahmepfad

**Werkzeug.** `biotop/nachspiel.py` ruft `aegis.pruefen` mit den Bausteinen aus `lauf.generation()`: `annahme_tausch`,
`bestwert_des_laufs`, `letzte_angenommene`, `_referenzlast`.
- Gearbeitet wird an einer Kopie der Lauf-DB, in der die Generationen ab dem Kandidaten ausgeblendet sind.
- Die Vorgeneration kommt aus dem Lazarus-Archiv. Ihre Prüfsumme stimmte mit der DB in 33 von 33 Fällen.
- Original-DB unverändert: 33 von 33. Netz im Prozess gesperrt; alle 33 Anbieteranfragen gingen an eine gestellte Grenze.
  12 davon beantwortete sie aus der Aufzeichnung („KEIN ANGRIFF“), 21 brach sie mit benannter Meldung ab.
- 33 Fälle mit 16 Kandidaten; je Fall ein vorab festgelegter Durchgang. Serie 1 lief neben eigenen Kammerproben, ihre
  Laufzeiten sind gestört (eigener Fehler). Alle späteren Fälle liefen mit 0 fremden Containern.
- Einzelbelege: `NACHSPIEL-BELEGE.json`. Übersicht: `AUSWERTUNG-ABSCHLUSS3.txt`, Abschnitt A.

**Was das Nachspiel nicht nachbildet** (Review Nr. 4). Es belegt „überlebt `aegis.pruefen`“, nicht „angenommen“.
- Nicht durchlaufen werden:
  - die Vorprüfung durch das Projektgedächtnis;
  - `_verhandeln` (das Paar K2867+K2868 geht direkt als `extra_code` hinein);
  - die Auswahl je Bereich samt Jury;
  - die Generalprobe (mit eigener Laufzeitmessung) und die Freigabe.
- Gestellt sind:
  - die Anbietergrenze;
  - die Immuntests, genau die, die das aufgezeichnete Urteil vorlegte;
  - die Eichung der Läufe vor dem Einbau: gebildet aus der versiegelten Vorspann-Messung, 2 Regeln geprüft, 1 stillgelegt.
- In 2 von 16 Kandidaten weicht der nachgespielte Zustand um +1 auf beiden Seiten ab, bei unverändertem Zuwachs: K3045 und
  das Paar K2867+K2868 (Nr. 17). Vermutete Ursache ist der im Lauf erzeugte Angriffstest, der dem Nachspiel fehlt.

| Vorgabe | Ergebnis am Annahmepfad | erfüllt |
|---|---|---|
| K2934 abgelehnt | abgelehnt 2 von 2, durch den Verhaltensvergleich: 8 von 8 Abweichungen ungedeckt (`quantil#0…7@mutation`) | ja |
| K3121 abgelehnt | abgelehnt 3 von 3: in 2 von 3 durch den Verhaltensvergleich (8 von 8 ungedeckt), in 1 von 3 vorher durch ein Laufzeit-Grenzmaß | ja |
| Gegenprobe: ohne Vergleich müssen beide überleben | K3121 überlebt 2 von 2; K2934 1 von 2 (Grenzmaß `eingang` 3,157 > 2,739 ms, Bereich unberührt) | teilweise |
| K2868 angenommen | Paar K2867+K2868 überlebt 2 von 2, 0 Abweichungen; geeicht Kernmaß −10 → 0 | ja (überlebt den Annahmepfad) |
| S2-Beschleunigung angenommen | dieselbe Änderung zweimal (je +6/−8 in `src/planung/pruefen.ts`, Duplikatprüfung über ein Set): K3091 überlebt 3 von 3, K2904 0 von 2 | **nein, nicht belastbar** |
| Kernmaß ohne `detect-object-injection` | Regel in 0 von 27 geeichten Maßen gezählt, in 27 von 27 als stillgelegt ausgewiesen; ohne Eichung in 6 von 6 gezählt | ja |

**S2: warum „nicht belastbar“** (Review Nr. 1, korrigiert). Beide Kandidaten tragen dieselbe S2-Behebung. Im Lauf wurden
beide für Punkte der Fehlalarm-Regel angenommen (`planung.sicherheit` 2 → 0):
- K2904 (Lauf 37) bei −18,4 %.
- K3091 (Lauf 38) bei **−11,2 %**, ohne Laufzeitgewinn (Urteil 23639: `laufzeit_gewinne` leer).

Mit Eichung bleibt ein Kernmaß-Zuwachs von 0. Die Nische „schnell“ verlangt dann ≥ 15 % aus **einer** Messung je Seite:
- K3091 lag im Nachspiel bei −21 %, −17 % und −30 %, im Lauf bei −11 %.
- K2904 lag bei gestört (Serie 1) und −13,7 %.

Ob die Behebung durchkommt, hängt also an der Einzelmessung. Die Schwelle bleibt. Entschieden ist: Median mehrerer
Messungen je Seite vor T4, mit der Gegenprobe, dass K2904 und K3091 gleich entschieden werden.

### Alle 13 Annahmen von Lauf 38, nachgespielt mit Abwehr (`NACHSPIEL-LAUF38.txt`)

| Gen | Bereich | Kandidat (Nische) | Grundlage der Annahme in Lauf 38 | mit Abwehr | entschieden durch |
|---|---|---|---|---|---|
| 1 | bericht | K3030 (elegant) | echter Gewinn: tote Funktion 1 → 0 (behebt S4) | überlebt | Kernmaß −11 → −10 |
| 1 | tarife | K3044 (wild) | echter Gewinn: `no-new-func` 10 → 0, Testfehler 3 → 0 (behebt S1) | überlebt | Kernmaß −14 → −1 |
| 1 | zahlen | K3045 (sicher) | nur Fehlalarm-Regel: `zahlen` 8 → 7 | abgelehnt | Grenzmaß Laufzeit `eingang`; geeichter Zuwachs 0 |
| 4 | planung | K3091 (schnell) | nur Fehlalarm-Regel: `planung` 2 → 0; Laufzeit −11,2 % (behebt S2) | überlebt | `planung` −30 %, Einzelmessung |
| 4 | tarife | K3096 (schnell) | nur Laufzeit: `bericht` −22 % (Diff ändert nur `tarife`) | abgelehnt | Grenzmaß `tarife` 6,69 > 5,94 ms |
| 5 | bericht | K3106 (wild) | nur Fehlalarm-Regel: `bericht` 4 → 1 | abgelehnt | Kernmaß unverändert |
| 5 | zahlen | K3121 (schnell) | nur Laufzeit: `zahlen` −66 % (Cache-Fehler) | abgelehnt | Grenzmaß `bericht` (0,05 % darüber) und `tarife`; in den Gegenproben 2 von 2 durch den Verhaltensvergleich |
| 9 | eingang | K3186 (schnell) | nur Laufzeit: `eingang` −26 % | abgelehnt | Grenzmaß `tarife`, `zahlen` |
| 10 | tarife | K3212 (sicher) | nur Fehlalarm-Regel: `tarife` 3 → 1 | abgelehnt | Grenzmaß; geeichter Zuwachs 0 |
| 12 | eingang | K3240 (wild) | echter Gewinn: Testfehler 2 → 0 (behebt S3) | überlebt | Kernmaß −2 → 0 |
| 12 | planung | K3242 (schnell) | nur Laufzeit: `planung` −26 % | abgelehnt | Grenzmaß `tarife` 6,41 > 5,94 ms |
| 13 | tarife | K3260 (elegant) | nur Fehlalarm-Regel: `tarife` 1 → 0 | abgelehnt | Kernmaß unverändert |
| 16 | zahlen | K3324 (elegant) | nur Fehlalarm-Regel: `zahlen` 7 → 5 | abgelehnt | Kernmaß unverändert |

**Grundlage der Annahme in Lauf 38:** echter Kernmaßgewinn 3, nur Punkte der Fehlalarm-Regel 6, nur Laufzeit 4 (3 + 6 + 4 = 13).

**Mit Abwehr:**
- 4 von 13 überleben, genau die 4 Behebungen S1–S4. Bei K3091 hängt das an der Einzelmessung.
- 5 von 13 weist die Eichung deterministisch ab: geeichter Zuwachs 0 und keine Laufzeitnische.
- 1 von 13 ist der Cache-Fehler K3121.
- 3 von 13 (K3096, K3186, K3242) entschied ein Laufzeit-Grenzmaß, das sie im Lauf bestanden hatten. Das ist unabhängig von
  der Abwehr (§7).
- Zusammen: 4 + 5 + 1 + 3 = 13.

**Blinder Fleck, K3106.** Ohne Eichung überlebt K3106 mit „0 Abweichungen“ (`NACHSPIEL-OHNE-EICHUNG.txt`), obwohl eine gezielte
Kammerprobe 3 von 50 veränderte Beobachtungen fand: `tabellenbreiten` liefert für Tabellen aus leeren Zellen `[]` statt
`[0,0]` bzw. `[0]` (`ZUSATZ-ABSCHLUSS3.txt`). Ursache laut Beleg: Die Referenzlast ruft **keine** der 7 eingewickelten
Funktionen von `bericht/tabelle` auf, beobachtet sind also 0 von 7. Das Organ urteilte trotzdem (Review Nr. 2). Dasselbe
gilt für K3212 und K3260: beobachtet sind dort nur die 6 Korpuszeilen.

## 3. Verdrahtungsnachweis als Regressionstest

`tests/test_verdrahtung.py` mit `tests/drahtwerk.py` fährt einen ganzen Lauf über die Befehlszeile: `lauf anlegen` → … →
`generation` → `freigabe`.
- Das Prüfwerk ist das kleinste TypeScript-Werk. Die Kammer ist echt, die Anbietergrenze gestellt (0 €), das Netz gesperrt.
- Jede Funktion jedes Moduls unter `biotop/organe/` wird aufgezeichnet. Die Organliste kommt aus dem Verzeichnis.
- Der Test verlangt zwei Dinge:
  1. Jedes Organ wird gerufen.
  2. `masseichung.anwenden` und `verhaltensvergleich.pruefen` werden aus `aegis.pruefen` gerufen.
- Er ist **nicht** als `integration` markiert und läuft in jeder Standard-Regression mit (etwa 11 min). Ohne Kammer wird er rot.

| Nachweis | Stand | Ergebnis |
|---|---|---|
| grün | `f821707`, in der vollen Regression | 23 von 23 Organen gerufen; beide Pflichtkanten aus `aegis.pruefen`; 254 Aufrufkanten; 0 € (`VERDRAHTUNG-BELEG-REGRESSION.json`) |
| rot | `1cf2eb1` | „Organ existiert und wird im Lauf nie gerufen: ['masseichung', 'verhaltensvergleich'] (gerufen 21 von 23)“ |
| rot | `masseichung.anwenden` in `aegis.pruefen` abgeklemmt | „['masseichung.anwenden'] wird nicht aus biotop.organe.aegis:pruefen gerufen“, bei 23 von 23 gerufenen Organen; `anwenden` weiter aus `lauf:_generation_koerper` und `lauf:mass_einfrieren` (`VERDRAHTUNG-PFLICHT-GEGENPROBE.*`) |
| Prüfwerkzeug | ohne Kammer | 3 von 3 Gegenproben grün |

**Grenzen** (Review Nr. 6). Der Test belegt **Aufruf, nicht Wirkung**:
- Die Kanten tragen keine Phase. Die Pflichtkante entsteht schon im Vorspann, über die Eichproben. Ein Lauf, dessen
  Generationen die Eichung nicht mehr erreichen, bliebe grün.
- Im Drahtwerk schlägt keine Regel im sauberen Bereich an. `anwenden` kehrt dort sofort zurück.
- Kein Test verlangt am Laufweg die Ablehnung einer ungedeckten Abweichung.

Die Wirkung belegen die Nachspiele (§2), aber nicht als Regressionstest. Nachschärfen ist Vorbedingung für T4 (§10).

## 4. Lauf 38 bereinigt, ausgewertet wie Lauf 37

### 4a. Kernmaß ohne die Fehlalarm-Regel

| | Gen 0 | Endstand | Gewinn |
|---|---|---|---|
| Lauf 37 gemeldet / bereinigt | −28 / −11 | −14 / **0** (Gen 8) | 14 / 11 |
| Lauf 38 gemeldet / bereinigt | −28 / −11 | −6 / **0** (Gen 16; 0 schon ab Gen 1) | 22 / 11 |

- Der echte Gewinn von Lauf 38 liegt ganz in Gen 1: K3044 (10) und K3030 (1).
- Bereinigt bewegten die 7 angenommenen Generationen danach das Maß um 0.

**Zurückgenommen aus dem LAUF38-BERICHT vom 22.09.** (Review Nr. 10):
- „deutlich besser als Lauf 37“: Bereinigt enden beide Läufe bei 0.
- „Das Messgerät trägt. Kernmaß halbiert und nochmals halbiert“: Die Halbierungen nach Gen 1 sind entfernte Fehlalarme.
- „9 von 17 Generationen angenommen“ zählte Gen 0 mit. Richtig ist 8 von 17.

### 4b. Sicherheitsminderungen — welche waren bloße Umformungen?

Sicherheitspunkte 27 → 6, also 21 = 10 (`no-new-func`, S1) + 11 (`detect-object-injection`). Eigene Messung
(`UMFORMUNG-LAUF38.txt`), je Kandidat gegen seine Vorgeneration:
- (i) Verhaltensvergleich, dieselbe Sonde wie im Annahmepfad;
- (ii) Randfallsonde: jede exportierte Funktion der geänderten Module mit denselben 30 festen Argumentlisten, samt Zustand der
  Argumente danach.

| Kandidat | Punkte (Regel) | Verhaltensvergleich | Randfallsonde | Einordnung |
|---|---|---|---|---|
| K3091 | 2 | 0 Abweichungen, 3 von 3 Nachspielen | — | Nebenwirkung der echten Behebung S2 |
| K3106 | 3 | 0 Abweichungen, aber nur Korpus beobachtet | 0 von 421 | Umformung **mit** Verhaltensänderung: gezielte Probe 3 von 50 (§2) |
| K3045 | 1 | 0 von 230 Beobachtungen | 0 von 962 | keine Abweichung gefunden |
| K3212 | 2 | nur Korpus (6) beobachtet | 0 von 301 | keine Abweichung gefunden |
| K3260 | 1 | nur Korpus (6) beobachtet | 0 von 301 | keine Abweichung gefunden |
| K3324 | 2 | 0 von 102 Beobachtungen | 0 von 421 | keine Abweichung gefunden |

Die 11 Punkte teilen sich so auf: 2 als Nebenwirkung einer echten Behebung, 3 durch eine Umformung mit Verhaltensänderung,
6 ohne gefundene Abweichung. Summe 11.
- Die 6 sind **bloße Umformungen, soweit die Eingaben reichen**. Dieselbe Randfallsonde fand auch bei K3106 nichts (0 von 421),
  wo die gezielte Probe eine Änderung zeigt. „Keine Abweichung gefunden“ ist also so stark wie die Auswahl der Eingaben.

### 4c. S1–S5 nach „behoben heißt verschwunden“

Selbst gemessen mit dem versiegelten Gegenzeugen in der netzlosen Kammer (`S1S5-ABSCHLUSS3.*`, `S1S5-ZUORDNUNG.*`). Jeder Stand
wurde vorher gegen die DB-Prüfsumme geprüft.

| Stand | S1 | S2 (Zugriffe n=40/80/160) | S3 | S4 | S5 | behoben |
|---|---|---|---|---|---|---|
| Ausgang und lauf38-gen0 | verletzt | 1560/6320/25440 | verletzt | verletzt | verletzt | 0 von 5 |
| lauf38-gen1 | weg | verletzt | verletzt | weg | verletzt | 2 von 5 |
| lauf38-gen4 und -gen10 | weg | weg (80/160/320) | verletzt | weg | verletzt | 3 von 5 |
| lauf38-gen12 und -gen16 | weg | weg | **weg** | weg | verletzt | **4 von 5 = 80 %** |
| Lauf 37, Endstand gen8 | weg | weg | verletzt | weg | verletzt | 3 von 5 = 60 % |

**Zuordnung.** Die Kriterien legen die Bereiche fest: S1 `tarife`, S2 `planung`, S3 `eingang`, S4 `bericht`. In der Generation,
in der die Schwäche verschwand, änderte je genau ein Kandidat diesen Bereich:
- S1: K3044 (Gen 1);
- S4: K3030 (Gen 1);
- S2: K3091 (Gen 4);
- S3: K3240 (Gen 12).

Lauf 38 erreicht die Schwelle ≥ 80 % genau. S5 (Grenze beim Mengenrabatt) bleibt in beiden Läufen offen. Alle vier
behebenden Kandidaten überleben das Nachspiel mit Abwehr; K3091 nur messabhängig (§2).

### 4d. Halluzinationsprobe `zahlen`: gerissen

- **Lauf 38:** 3 von 8 angenommenen Generationen änderten den sauberen Bereich:
  - K3045: 1 Fehlalarmpunkt;
  - K3121: Cache über Modulvariablen, `spannweite` liefert nach Mutation 8 statt 80 (`NACHTRAG-7-K3121.txt`);
  - K3324: 2 Fehlalarmpunkte.

  Mit Abwehr weist der Annahmepfad alle drei ab.
- **Korrektur zu NACHTRAG-02** (Review Nr. 9): In Lauf 37 waren es **4 von 6**, nicht 3. Auch K2867 (Gen 3, Vertragsanpassung
  im Paar mit K2868 für S1) änderte `src/zahlen/geld.ts`. Der Verhaltensvergleich am Paar fand 0 Abweichungen, bei laut
  Review 7 von 10 beobachteten Funktionen.

### 4e. Doppelungsanteil: Torzeile nicht gemessen, drei Stufen unterschieden

Nachgezählt in `NACHZAEHLUNG-ABSCHLUSS3.txt`.

| Stufe | Lauf 37 | Lauf 38 | Rolle |
|---|---|---|---|
| Ansagefilter: Ansagen mit Behauptung, die gesperrt wurden | 20 von 57 = 35,1 % | 29 von 91 = 31,9 % | Diagnose |
| Aufnahmesperre C: zur Aufnahme geprüfte Tests, als Doppelung gesperrt | 2 von 14 = 14,3 % | 5 von 17 = 29,4 % | Diagnose |
| VB1-Methode: alle erzeugten Angriffstests nach geschriebener Behauptung | nicht rekonstruierbar | Behauptung nur bei 9 von 87 aufgezeichnet (nur Treffer), 0 Doppelungen unter den 9 | **Torzeile: nicht gemessen** |

- Die 35,1 % in NACHTRAG-02 sind die Stufe des Ansagefilters, keine Torzeile. NACHTRAG-6 nannte stattdessen die Aufnahmesperre C
  die Torzeile. Nach der festgelegten Definition (VB1: erzeugte Angriffstests nach geschriebener Behauptung) sind beide nur
  Diagnosen.
- Nach der Lesart von NACHTRAG-6 wäre Lauf 38 mit 29,4 % über 20 % gerissen.
- **Korrektur:** `1cf2eb1` hieß „Tor 2 Zeile 8 messbar machen“. Messbar wurde nur die Treffer-Teilmenge (9 von 87).

### 4f. Immunisierung auf dem TypeScript-Pfad: nicht belegt

- Lauf 38 legte 11 Immuneinträge an: 10 archiviert, 1 `offen_norm`. Als Datei im Endstand liegen **0 von 11**.
- `aegis._anhaengen` hatte **0 Fälle**. Null Fälle sind keine Mehrheit.
- Im Endstand liegen 2 Immundateien: der Fund K2897 aus Lauf 37 und ein Befundklassen-Test.
  - lauf38-gen0 enthält außer den 12 Ursprungsdateien nur die 10 Dateien aus Generation 0. Beide Immundateien kamen also während
    Lauf 38 hinzu.
  - Testbestand 207 → 213 = +6: `bericht` +1, `eingang` +2, `tarife` +3.

### 4g. Warum der Testbestand in Lauf 38 bei 207 beginnt statt bei 182

- Generation 0 läuft **vor** dem Einfrieren des Maßes und schreibt Tests für blinde Mutanten ins Werk.
- **Lauf 38:** 17 von 100 Mutanten blind, für 10 davon Tests (10 Dateien). 182 + 25 = **207**.
- **Lauf 37:** 182 + 258 = **440** aus 93 Dateien. Die Ursache ist ein Messgerätbefund (§5).

### 4h. Neutralzähler Lauf 38

| Organ | geurteilt | trägt seine Torzeile? |
|---|---|---|
| `aegis.behauptung` | 51 von 51 | ja |
| `generation0._testlauf` | 400 von 400 | ja |
| `gedaechtnis.aenderungsziel` | 328 von 430 (102 neutral: `diff_nicht_anwendbar`) | ja |
| `aegis._anhaengen` | 0 von 0 | nein |
| `verhaltensvergleich` | 0 von 0 (in Lauf 38 nicht eingehängt) | nein |

Seit `f821707` zählt der Verhaltensvergleich auch unbeobachtete Module als „geurteilt“ (Review Nr. 2). Sein Zähler wäre in
einem neuen Lauf überzeichnet, bis Vorbedingung 2 umgesetzt ist.

## 5. Messgerätbefund: ein Durchlauf, in dem jeder Fall neutral ausgeht, heißt „nicht gemessen“

**Der Schluss vom 23.09. vormittags ist an der Ursache bestätigt** (`GEN0-URSACHE.txt`).

**Code.** `generation0._testlauf` baut je Mutant zuerst den Typbau: `tsc` über `src/` **und** `tests/`. Besteht er nicht, bucht
es „neutral, `typbau_nicht_bestanden`“ und gibt „nicht gefangen“ zurück. `G0.messen` zählt das als blind; `lauf.generation0`
schreibt dann Tests für alle als blind gezählten Mutanten.

**Aufzeichnung, Lauf 37, je Durchlauf:**

| Durchlauf | geurteilt | neutral | protokolliert als |
|---|---|---|---|
| vorher | 100 | 0 | 83 gefangen, 17 blind |
| nach Runde 1 (8 neue Testdateien) | 0 | **100** (`typbau_nicht_bestanden`) | **„gefangen 0, blind 100“** |
| nach Runde 2 | 0 | **100** | **„gefangen 0, blind 100“** |
| nach Runde 3 und Abschluss | 100 | 0 | 93 gefangen |

**Nachstellung am Messweg.** `G0.messen` an einer Kopie von lauf38-gen0 mit 5 aufgezeichneten Mutanten:

| Zustand | Ergebnis |
|---|---|
| sauber | 5 von 5 gefangen, 5 geurteilt |
| plus eine Testdatei, die unter Vitest besteht, aber den Typbau bricht (TS2322) | **0 von 5 gefangen, 5 blind, 5 neutral `typbau_nicht_bestanden`** |
| Datei wieder entfernt | 5 von 5 |

Die Prüfung zwischen den Runden (`typescript.testlauf`, Vitest) bestand mit derselben Datei: 208 Fälle, alle grün. Sie kann einen
Typbaubruch nicht erkennen.

**Folgen in Lauf 37:**
- Zwei Durchläufe maßen nichts und wurden als „nichts gefangen“ verbucht.
- Generation 0 schrieb daraufhin Tests für alle 100 statt für die 17 blinden Mutanten: 93 statt 10 Dateien, Testbestand 440
  statt 207.
- Generation 0 kostete 291 Buchungen und 0,255778 €. In Lauf 38 waren es 67 Buchungen und 0,068102 €, bei gleichem Code von
  `generation0.py` und gleichem Ergebnis (83 → 93 von 100). Den Unterschied schreibe ich der Fehlmessung zu *(abgeleitet)*.

**Nicht rekonstruierbar:** welche Datei den Typbau brach. 200 von 200 Neutralfällen tragen keine `tsc`-Meldung.

**Regel:** Ein Durchlauf mit überwiegend neutralen Fällen heißt „nicht gemessen“ und darf keine Entscheidung auslösen. Umsetzung
ist Vorbedingung 6 für T4 (§10).

## 6. Kasse: die 49 wegen der WAL übersehenen Zeilen

Nachgezählt am Schnappschuss (`NACHZAEHLUNG-ABSCHLUSS3.txt`, Abschnitt 1):

| Lesung | Buchungen Läufe 26–38 | Summe |
|---|---|---|
| ohne WAL (`immutable=1`, mein Lesefehler) | 2554 | 9,483126 € |
| nur in der WAL | **49** (ids 6625–6673) | **0,245512 €** |
| mit WAL (Schnappschuss) | 2603 | **9,728638 €** |

- **Die 49 Zeilen sind in 9,7286 € enthalten:** 2554 + 49 = 2603 und 9,483126 + 0,245512 = 9,728638 €.
- 0 Zeilen der Lesung ohne WAL fehlen im Schnappschuss oder lauten dort anders.
- Alle 49 gehören zu Lauf 38 (19:16:41–19:26:08 UTC, nach der Freigabe von Gen 16 um 19:16:34, also Gen 17): Schwarm 42,
  Ankläger 4, schweres Modell 3.
- **Harte Grenze eingehalten:** 9,728638 € von 10,00 €, Rest 0,271362 €.
  - Die Kasse prüft die 10 € vor jedem Modellaufruf (`kasse.vorpruefung`).
  - Die Laufkette hielt an ihrer eigenen Haltegrenze von 9,60 €. Diese prüfte sie zwischen den Generationen: vor Gen 17
    standen 9,483126 €, danach 9,728638 € („HALT: Budgetgrenze 9.60 EUR erreicht (9.728638 EUR)“).
- Die Summe der gerundeten Teilbeträge je Lauf ist 9,728637 €, die gerundete Gesamtsumme 9,728638 €. Das ist Rundung.

## 7. Laufzeit-Grenzmaße entscheiden nach Rauschen

**Mechanismus.**
- Die Grenze ist *Bestwert × Rauschtoleranz*.
- Der Bestwert ist das Minimum über alle angenommenen Generationen; jede Annahme kann den Bezug nur senken.
- Die Toleranz stammt aus 5 Messungen des unveränderten Werks.
- Jede Seite wird einmal gemessen.

**Gemessen:**
- Im Nachspiel entschied ein Laufzeit-Grenzmaß in 8 von 33 Fällen. Alle 8 Kandidaten hatten es im Lauf bestanden.
- In den Läufen (Review Nr. 7):

  | Lauf | Laufzeit-Grenzmaß als Ablehnungsgrund | direkt | über das Projektgedächtnis | nur in fremden Bereichen gerissen |
  |---|---|---|---|---|
  | 37 | **21 von 139 Ablehnungen** | 19 | 2 | 13 |
  | 38 | **41 von 207 Ablehnungen** | 24 | 17 | 34 |

  „Über das Projektgedächtnis“ heißt: gesperrt als „Wiederholung eines gescheiterten Wegs“, der damals an einem
  Laufzeit-Grenzmaß scheiterte.
- Knappster Fall, K3121: `bericht` 4,660907 ms gegen die Grenze 4,658563 ms, 0,05 % darüber. Die Meldung rundet die Grenze
  auf „4.7“ und liest sich wie „4,66 > 4,7“ — ein Anzeigefehler.

**Entschieden:** Median mehrerer Messungen je Seite, Schwelle unverändert, vor T4.

**Offen für Philipp:**
- das Minimum als Bezug;
- ob Laufzeit-Grenzmaß-Ablehnungen im Projektgedächtnis als gescheiterter Weg sperren sollen.

## 8. Sperren im Wortlaut (`SPERREN.md`, 5 Einträge)

Die Formatsperre „unparsbare Payload“ lautete in allen drei Fällen gleich **bis auf den Skriptpfad**. Wortlaut vom 22.09.:

```
BLOCKED (hardline): command parser limit or malformed executable payload. This command is on the unconditional blocklist and cannot be executed via the agent — not even with --yolo, /yolo, approvals.mode=off, or cron approve mode. If you genuinely need to run it, run it yourself in a terminal outside the agent. RECOVERY: this block fires on oversized/unparseable inline command payloads (heredocs, giant one-liners), not on the operation itself. Your command was saved to /root/.hermes/cache/blocked-scripts/blocked-1790084242-98c4bf6b.sh — review it, then run: terminal(command="bash /root/.hermes/cache/blocked-scripts/blocked-1790084242-98c4bf6b.sh"). Do not retry inline.
```

1. **22.09.**, `blocked-1790084242-98c4bf6b.sh`: lesender `grep`. Damals ausgeführt, bevor es eine Regel dafür gab; das war
   nicht regelkonform.
2. **23.09.**, `blocked-1790137630-993130dd.sh`: lesender `grep`/`ls`. Nach Philipps Regel geprüft und unverändert ausgeführt.
3. **23.09.**, Sicherheitsfilter des Gateways (harte Linie 3). Nicht umgangen. Nach Entscheidung von Chat-Claude nicht aufgelöst;
   nicht mehr nötig.
4. **23.09.** Formatprüfung, von der Ausführungsschicht selbst freigegeben.
5. **23.09.**, im Review, `blocked-1790168621-64f4802c.sh`: die Selbstkontrolle des Prüfers, nur `grep`/`sha256sum`/`ls`. Der
   Prüfer hielt an wie beauftragt. Ich habe das Skript geprüft und nach Philipps Regel unverändert ausgeführt. Ergebnis:
   21 Befunde (3/9/9) und 50 Prüfpunkte (10 mit Einschränkung) bestätigen die von Hand gezählten Zahlen des Prüfers.

## 9. Reviewdurchgang und Umgang mit den Befunden

Ein Durchgang (`REVIEW-AUFTRAG-03.md`, `REVIEW-03.md`), ohne Modell- und Kammerläufe: 21 Befunde (3 hoch, 9 mittel, 9 niedrig),
50 Prüfpunkte nachgerechnet. Keine nachgerechnete Zahl wich ab, außer dem Annahmegrund von K3091.

| Nr | Schwere | Befund (kurz) | Umgang |
|---|---|---|---|
| 1 | hoch | K3091 wurde für Fehlalarmpunkte angenommen (−11,2 %), nicht für S2 | berichtigt (§2, §4c); T4-Vorbedingung 1 |
| 2 | hoch | Verhaltensvergleich urteilt ohne Beobachtung (K3106: 0 von 7) | bestätigt, §2 berichtigt; T4-Vorbedingung 2, Spezifikation rot |
| 3 | hoch | Sondenausfall → Ablehnung und Eintrag ins Projektgedächtnis | bestätigt aus Code, in 0 von 33 Nachspielen eingetreten; T4-Vorbedingung 3, Spezifikation rot |
| 4 | mittel | „angenommen“ statt „überlebt `aegis.pruefen`“ | Wortlaut geändert, ausgelassene Stufen aufgezählt (§2) |
| 5 | mittel | Verhandlung: Ablehnung durch den Vergleich beendet die Suche als „bestanden“ | T4-Vorbedingung 4, Spezifikation rot |
| 6 | mittel | Verdrahtungstest belegt Aufruf, nicht Wirkung, ohne Phase | Grenzen benannt (§3); T4-Vorbedingung 7 |
| 7 | mittel | Laufzeit-Grenzmaß über das Gedächtnis nicht gezählt | nachgezählt (§7): 21 von 139, 41 von 207 |
| 8 | mittel | Doppelung: 35,1 % aus NACHTRAG-02 nicht eingeordnet | drei Stufen (§4e) |
| 9 | mittel | Lauf 37: 4 von 6 Generationen änderten `zahlen`, nicht 3 | Korrektur (§4d) |
| 10 | mittel | LAUF38-BERICHT: zwei weitere Aussagen stehen noch | zurückgenommen (§4a) |
| 11 | mittel | 4b für 4 von 11 Punkten nicht gemessen | nachgemessen (§4b), mit Grenze der Sonde |
| 12 | mittel | Eichung wirkt auf Schwarm und Modellwahl des Anklägers | benannt (§1); Frage an Philipp |
| 13–19 | niedrig | Wortlaut: `annahme_tausch`, „Modellaufrufe 0“, Belegbündel, 16 Kandidaten, Zustandsabweichung +1, `KAPPE`, Skriptpfad der Sperre | berichtigt |
| 20 | niedrig | `anwenden` erkennt eine andere Eichung nicht | T4-Vorbedingung 5, Spezifikation rot |
| 21 | niedrig | Protokollfeld `kernmass` roh neben geeichtem `kernmass_f2` | T4-Vorbedingung 8 |

*Eigene Entscheidung:* Die Code-Befunde behebe ich **nicht** in T3.
- Grund: Eine Änderung nach dem einzigen Reviewdurchgang wäre ungeprüfter Code in der Lieferung, und T3 hat keinen Lauf mehr.
- Stattdessen liegen sie als **rote Spezifikation** vor: 9 Tests, am Commit `f821707` 9 von 9 rot (`T4-SPEZIFIKATION-ROT.txt`,
  `test_t4_*.py`).
- Das Repository steht wieder auf dem reviewten Stand: `git status` leer, Prüfsummen gleich `f821707`.

## 10. Vorbedingungen für T4 (Reihenfolge)

1. **Laufzeit: Median mehrerer Messungen je Seite** (Entscheidung Chat-Claude), Schwelle unverändert. Gegenprobe: K2904 und
   K3091, dieselbe Änderung, werden gleich entschieden. Dazu die Anzeige der Grenze ohne irreführende Rundung.
2. Verhaltensvergleich: Ein unbeobachtetes Modul ist eine Enthaltung, kein Urteil. „x von y Funktionen beobachtet“ in Urteil
   und Protokoll.
3. Sondenausfall: bei `infrastruktur` oder Scheitern an der Vorgeneration anhalten bzw. zurückstellen, kein Eintrag ins
   Gedächtnis.
4. `paar_ok` in der Verhandlung an die Tragfähigkeit des Verhaltensvergleichs binden.
5. `masseichung.anwenden` vergleicht die Eichung, statt nur den Marker zu prüfen.
6. Generation 0: Ein Durchlauf mit überwiegend neutralen Fällen ist „nicht gemessen“. Die `tsc`-Meldung wird gespeichert. Die
   Prüfung zwischen den Runden baut auch den Typbau.
7. Verdrahtungstest: Pflichtkanten an die Phase `lauf.generation` binden. Im Drahtwerk eine Regel im sauberen Bereich
   anschlagen lassen. Ein Laufweg-Test verlangt die Ablehnung einer ungedeckten Abweichung.
8. Protokoll: `kernmass` geeicht mitführen oder als roh kennzeichnen.
9. Tor 2 Zeile 8: Behauptung für **alle** erzeugten Angriffstests protokollieren. 3.10 F3: Immunisierung auf dem
   TypeScript-Pfad bauen.

**Offen für Philipp:**
- Bestwert als Minimum;
- Laufzeit-Grenzmaß-Ablehnungen im Projektgedächtnis;
- Schwarm und Befundklassen roh oder geeicht;
- Korpus des Verhaltensvergleichs über die Referenzlast hinaus (K3106).

**Weiter offen aus der Liste nach T3:**
- Erreichbarkeitsführung;
- Verfallsbedingung der Ausnahmeliste des Python-Wächters;
- `_beschleunigen` entfernen;
- Rauschrohwerte speichern.

## 11. Dauerregel Zwischenbericht: ausgelöst, nicht erinnert

Regel (Philipp, 23.09.): Zwischenbericht spätestens bei 120 von 150 Aufrufen einer Sitzung.

- **Wächter** `zwischenbericht_waechter.py`, als Cron-Job `26fbb1513a1a`: minütlich, ohne Modell.
  - Er zählt die Werkzeugrunden seit der letzten echten Nutzernachricht. Genau diese Größe begrenzt `agent.max_turns` (150).
    Gemessen: 111 + 39 = 150 bis zur Abbruchmeldung am Vormittag.
  - Er löst bei 110 und 140 aus. 110 statt 120, damit der Bericht trotz des Minutentakts spätestens bei 120 liegt.
  - Ausgelöst wird ein neuer Prüfkanal-Ordner mit Auftrag, Übergabedatei, letzten Äußerungen, Git-Stand, geänderten Dateien,
    `DATEIEN.txt` mit vollen URLs und Prüfsumme; danach eine HTTPS-Prüfung. Bestehende Ordner werden nie überschrieben.
- **Tests:** 6 von 6 grün (`WAECHTER-TESTS.txt`, `test_waechter.py`). Gegenproben:
  - unter der Schwelle still;
  - je Schwelle genau einmal;
  - die Fortsetzung nach einer Kontextverdichtung zählt weiter;
  - ein neuer Auftrag zählt neu;
  - Kindsitzungen zählen nicht;
  - ein vorhandener Ordner führt zu Fehler und Exit 1, nicht zu Überschreiben.
- **Am echten Weg belegt:**
  - Ein Zwischenbericht wurde von Hand ausgelöst: HTTPS bytegleich 5 von 5 (`WAECHTER-SOFORT.txt`).
  - Der Zeitplan ruft den Wächter wirklich auf: Der Herzschlag trägt als Elternprozess `cron.scheduler`, der Lauf ist als
    `completed` verbucht.

## Eigene Entscheidungen (mit Begründung)

1. Verdrahtungstest in der Standard-Regression. Nur so macht ein nie gerufenes Organ jede Regression rot.
2. Sauberer Vergleichsbereich aus dem wörtlichen Satz der versiegelten Verfassung, ohne die Verfassung anzufassen.
3. Verhaltensvergleich erst nach bestandenem Maß. Das spart Kammerläufe; Folge: 11 von 29 Nachspielen mit eingeschaltetem
   Vergleich bekamen kein Verhaltensurteil.
4. Im Nachspiel keine erfundenen Angriffe.
5. Code-Befunde des Reviews nicht in T3 behoben, sondern als rote Spezifikation für T4 (§9).
6. Sperren 2 und 5 nach Philipps Regel unverändert ausgeführt.
7. Wächter-Schwellen 110/140 statt 120, wegen des Minutentakts. Zustellung nur lokal; Fehler gehen in diesen Chat.

## Eigene Fehler in diesem Auftrag

- Abwehr gebaut, getestet und committet, aber nicht eingehängt.
- Gegenproben gegen das Modul geführt statt durch den Laufweg.
- Tests nach dem Code geschrieben. Serie 1 neben eigenen Zeitproben laufen lassen.
- DB mit `immutable=1` gelesen (190 Protokollzeilen, 49 Kassenzeilen fehlten).
- Zu starke Formulierungen: „Tor 2 Zeile 8 messbar gemacht“, „Lauf 38 deutlich besser“, „S2-Beschleunigung angenommen“.
- Kein Zwischenbericht vor dem Rundenlimit am Vormittag. Daraus folgt der Wächter (§11).
