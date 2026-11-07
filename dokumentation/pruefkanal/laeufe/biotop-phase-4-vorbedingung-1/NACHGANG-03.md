# Phase 4, Vorbedingung 1 — Nachgang N1 bis N11

> Enthält drei Nachgänge: N1–N6 (Prüfung 1), N7–N9 (Prüfung 2), N10–N11 (Prüfung 3).
> Widersprüche zwischen den Abschnitten sind berichtigt; maßgeblich ist jeweils der spätere.

**Auftraggeber:** Philipp Zöllisch · **Prüfer:** Chat-Claude · **Ausführung:** Hermes
**Grundlage:** Prüfbericht `PRUEFUNG_Vorbedingung-1_2026-09-20.md`, Nachgangsauftrag N1–N6
**Budget:** 3 € hart · **verbraucht: 0,91 €** (unverändert — der Nachgang kostete **0 Modellaufrufe**)
**Stand:** 20.09.2026

---

## N6 — Adressen (zuerst, weil ohne sie nichts prüfbar ist)

Bericht:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/BERICHT.md

Dateiliste mit Prüfsumme je Datei:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN.txt

Ordnerprüfsumme:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER.txt

Kassenblatt:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/KASSE.md

Ab sofort nennt jeder Abschlussbericht diese vier Adressen als ganze URL in eigener Zeile. Der Befund F7 war
berechtigt: Eine Prüfsumme, die von außen nicht nachrechenbar ist, ist Zierde.

---

## Die Prüfung in einem Satz

**F1 trifft zu, F2 war eine Lücke im Bericht, F3 trifft zu, F4 trifft zu, F5 ist aufgelöst, F6 trifft zu,
F7 ist behoben.** Dazu ein Fehler, den die Prüfung nicht gefunden hat und den ich beim Nachrechnen selbst
gefunden habe (Abschnitt N1, Nebenbefund).

---

## N1 — Zuordnung berichtigt

Beleg: `ausgaben/17-nachgang-n1-zuordnung.txt`.

Drei Bauteile sind zu unterscheiden, nicht zwei:
- **S** = Behauptungs-Schlüssel (Doppelungen werden überhaupt erkannt) — ab Lauf 22
- **W** = Anweisung an den Ankläger (bisherige Behauptungen im Angriffsprompt) — ab Lauf 22
- **A** = Ansage vorab mit Sperre (Angriff wird nicht ausgeführt) — ab Lauf 23/24

| Lauf | S | W | A | erzeugte Tests | größte Gruppe | unbemerkte Doppelungen | vom Ankläger verworfen | Ansagen |
|---|---|---|---|---|---|---|---|---|
| 13 | | | | 54 | 8 | 31 | 6 | 0 |
| 20 | | | | 4 | 4 | 3 | 0 | 0 |
| 22 | x | x | | 10 | **1** | **0** | 6 | 7 |
| 24 | x | x | x | 2 | 1 | 0 | 0 | 27 |

**Größte Gruppe 8 → 1 und unbemerkte Doppelungen 31 → 0 gehören S und W, nicht A.** Beide Werte standen in
Lauf 22 ohne die Ansage. Meine Meldung führte sie als Beleg für Bauteil A — das war falsch.

**Bauteil A allein zuzurechnen ist:**
- 10 von 27 Ansagen abgewiesen, der Angriff lief gar nicht (vorher gab es diesen Mechanismus nicht)
- 18 von 65 Ansagen mit „KEIN ANGRIFF" über die Läufe 22–24 — vorher **0 von allen Aufrufen**
- Fehlalarm 0 von 10, Durchgerutscht 0 (N3)

Der Unterschied: S und W sorgen dafür, dass Wiederholungen **erkannt und beim Urteil verworfen** werden;
A sorgt dafür, dass sie **gar nicht erst erzeugt** werden. Nur A spart Aufrufe und Kammerläufe.

### Nebenbefund — ein Fehler, den die Prüfung nicht gefunden hat

Meine Meldung wies für **Lauf 20** „11 erzeugte Tests, 63,6 %" aus. 7 der 11 waren übernommener Altbestand aus
Werk 18 (Generation 0). Richtig: **4 erzeugte Tests, 3 unbemerkte Doppelungen = 75,0 %**. Das ist dieselbe
Fehlerklasse wie bei Lauf 24 (dort 41 statt 2) — ich habe sie beim ersten Mal nur an einer Stelle korrigiert
statt an allen. Die Richtung der Aussage ändert sich nicht (Zeile 8 war gerissen und bleibt es), aber die Zahl
**63,6 % im Phase-3-Nachlaufbericht ist hiermit berichtigt auf 75,0 %**.

---

## N2 — Lauf 24 vollständig aufgerechnet

Beleg: `ausgaben/15-nachgang-n2-n3.txt`.

```
Ansagen gesamt:                  27
  Angriff ausgeführt:            11
  abgewiesen (Wiederholung):     10
  KEIN ANGRIFF:                   6
  Summe: 11 + 10 + 6 = 27  → geht auf
```

**Die sechs vermissten Ansagen** (F2, erste Lücke): Ansagen ohne Behauptung, vom Ankläger mit „KEIN ANGRIFF"
beantwortet. Protokollnummern `#14627, #14657, #14874, #14896, #15071, #15083`. In meiner Meldung standen sie
unter „KEIN ANGRIFF", in der Rechnung 27 − 10 = 17 fehlten sie — mein Fehler.

**Warum 11 Angriffe nur 2 Tests erzeugten** (F2, zweite Lücke): Ein Angriff erzeugt nur dann einen Immuntest,
wenn sein Test am Kandidaten **fällt** und die Norm-Regel ihn als Fund anerkennt. Das ist der gewollte Ablauf,
stand aber nicht im Bericht; der Befund war berechtigt.

> **BERICHTIGT in N8:** Die hier ursprünglich genannte Aufrechnung („9 Urteile: 1 bestätigt, 1 Norm,
> 7 ohne Bestätigung") war unvollständig — sie erklärte die Differenz zwischen 11 Angriffen und 9 Urteilen
> nicht. Maßgeblich ist N8: 11 Ansagen → 11 Angriffsaufrufe, drei davon in einem Sammelurteil,
> Aufrechnung 1 bestätigt + 1 Behebungsnachweis + 1 Norm + 6 ohne Bestätigung = 9.

---

## N3 — Filtergüte, Maßstab vorab gesetzt

Beleg: `ausgaben/15-nachgang-n2-n3.txt`. Maßstab von Chat-Claude **vor** der Messung gesetzt:
Fehlalarm 0 von 10, Durchgerutscht 0. Bezugsgröße: alle 27 Ansagen.

**Fehlalarm: 0 von 10 — erfüllt.** Alle zehn abgewiesenen Ansagen nannten eine Behauptung, die zum Zeitpunkt
der Ansage im Vorrat stand: sechs aus der Übernahme, vier aus einer früheren Ansage desselben Laufs. Jeder Fall
einzeln aufgeführt mit Protokollnummer.

**Durchgerutscht: 0 — erfüllt.** Beide in Lauf 24 erzeugten Tests trugen zum Ansagezeitpunkt eine neue
Behauptung.

**Achtung, eigener Messfehler in der ersten Fassung dieser Prüfung:** Ich habe zuerst gegen den **Endstand**
des Vorrats geprüft und 2 Durchrutscher gemeldet. Der erzeugte Test trägt seinen eigenen Schlüssel im Ursprung
— wer den Endstand nimmt, findet jeden Test als „schon vorhanden" und misst sich selbst. Das ist Grundsatz 5
(die Nachrechnung muss dieselbe Ableitung verwenden wie das Organ). Korrigiert: Vergleich gegen den Vorrat
**zum Ansagezeitpunkt**.

**Roter und grüner Eichfall, beide aus dem echten Lauf** (nicht gestellt):
- **GRÜN** `#14533` formeln/`auswerten|Eq:` — neue Behauptung bei 1 vorhandenen → Angriff **ausgeführt**
- **ROT** `#14557` formeln/`auswerten|Eq:` — dieselbe Behauptung, jetzt bei 2 vorhandenen → Angriff **gesperrt**

Beide Fälle betreffen dieselbe Behauptung im selben Bereich, einmal vor und einmal nach ihrer Aufnahme in den
Vorrat. Das ist der schärfste Beleg, den der Lauf hergibt.

### Zusatzbefund: der Ankläger hält sich nicht immer an seine Ansage

**1 von 2** erzeugten Tests weicht ab: Ansage `#15027` lautete `aufnehmen|raises:ValueError`, geschrieben wurde
ein Test über `preis_fuer|GtE:zahl`. Die Sperre prüft die **angesagte** Behauptung; weicht der Ankläger danach
ab, greift sie nicht. **Das ist eine echte Lücke im Bauteil** — Ansage und Ausführung werden nicht gegeneinander
geprüft. Eine Behebung wäre eine Messgerätänderung und damit ein neuer Lauf (Satz 2); sie gehört nach
Abschnitt 6 des Prüfberichts ausdrücklich **nicht** in diesen Nachgang und steht als offener Punkt für
Fassung 7.

---

## N4 — Zahlenabgleich aufgelöst

Beleg: `ausgaben/16-nachgang-n4-n5.txt`.

```
Werk 11 (Quelle): 49 Einträge = 39 offen + 1 offen_norm + 6 im_werk + 3 gefunden
  davon Ankläger-Tests: 48          ← die „48" meiner Meldung
  übernahmefähig (offen + offen_norm): 40   ← die „40"
Werk 21 (Ziel): 43 Einträge = 40 übernommene + 3 in Lauf 24 erzeugte  ✓
Vorrat wie die Sperre ihn sieht: bericht 0 + formeln 1 + lager 19 + preise 6 = 26
```

**Die Differenz ist keine Rechenlücke, sondern eine unklare Bezugsgröße in meiner Meldung.** „48 Funde",
„40 übernommen" und „25 Behauptungen" sind drei verschiedene Mengen: Ankläger-Tests des Quellwerks,
übernommene Einträge, verschiedene Behauptungsschlüssel. Die Rechnung „40 − 14 = 26 erwartet" trägt nicht:
Die 14 Norm-Umstufungen ändern den Status, nicht die Zahl der Einträge, und Norm-Einträge tragen ebenfalls
einen Schlüssel. Der Vorrat ist von 25 auf 26 gestiegen, weil Lauf 24 selbst Schlüssel hinzugefügt hat.

---

## N5 — Bauteil B erklärt

Beleg: `ausgaben/16-nachgang-n4-n5.txt`.

| Protokoll | Lauf | Richtungen mit Verweis | Kennungen | erfunden |
|---|---|---|---|---|
| #12547 | 22 | 0 von 4 | — | 0 |
| #13296 | 22 | 0 von 4 | — | 0 |
| #14246 | 22 | **3 von 4** | A271, A597, A569, A568, A270 | 0 |
| #14480 | 24 | **1 von 5** | A597, A569 | 0 |

**Befund ohne Beschönigung: 75 % und 20 % bei gleichem Bestand belegen keine stabile Wirkung.** Die Zahl
schwankt mit dem Modellaufruf. Was das Bauteil nachweislich tut, ist die **Vorlage** zu ändern: fremde Muster
3 → 6. Was der Mentor daraus macht, streut.

Belegt über drei Messungen an zwei Werken: vor dem Bauteil **0 von 4 bzw. 5** in **neun** Mentor-Aufrufen
(`#7565, #7568, #7576, #9900, #9903, #10532, #11463, #12547, #13296`, Läufe 16–22); nach dem Bauteil
**3 von 4** (`#14246`, Lauf 22), **2 von 5** (`#13339`, Lauf 23), **1 von 5** (`#14480`, Lauf 24) — in allen
drei mindestens ein Verweis, in allen **0 erfundene Kennungen**. (In der ersten Fassung stand hier „sechs
aufeinanderfolgende Mentor-Aufrufe" ohne Protokollnummern; berichtigt in N9.)

**Zur Zeile selbst — Entscheidung liegt bei Philipp.** Die Zeile heißt „Mindestanteil", misst aber „≥ 1
werkübergreifender Verweis". Der Name verspricht mehr als die Messung. Entweder
**(a)** umbenennen in „≥ 1 werkübergreifender Verweis bei gezeigtem Mindestanteil" — dann ist sie mit 3 von 3
Messungen erfüllt; oder **(b)** den Anteil der Richtungen messen — dann braucht sie eine Grenze und mehr als
drei Messungen, um Streuung von Wirkung zu trennen.
Ich empfehle **(a)**: Der Anteil steuert die Vorlage, nicht das Zitierverhalten; ein Zitierzwang erzeugt
Scheinbegründungen (3.12).

---

## Was jetzt gilt — meine Wertung

| Punkt | Stand |
|---|---|
| N1 Zuordnung berichtigt | erledigt, mit zusätzlichem Eigenbefund |
| N2 Lauf 24 aufgerechnet | erledigt, 27 = 11 + 10 + 6 |
| N3 Filtergüte | **Fehlalarm 0 von 10, Durchgerutscht 0** — Maßstab erfüllt; roter und grüner Eichfall aus dem echten Lauf |
| N4 Zahlenabgleich | aufgelöst |
| N5 Bauteil B | erklärt; Streuung benannt, Zeilenname zur Entscheidung vorgelegt |
| N6 Adressen | erledigt |

**Tor 2 Zeile 8 ist weiterhin nicht gemessen** — die Prüfung hat recht: 2 erzeugte Tests lösen eine
20-%-Grenze nicht auf. Die Zeile bleibt für Tor 4 am echten Werk stehen. Für Vorbedingung 1 ist die Filtergüte
das Maß, und die ist erfüllt.

**Offen für Fassung 7:** Ansage und Ausführung gegeneinander prüfen (1 von 2 Tests wich von der eigenen Ansage
ab). Das ist eine Messgerätänderung und braucht einen eigenen Lauf.

---

## Kosten

Der Nachgang kostete **0 Modellaufrufe**. Stand unverändert: **0,9095 € von 3 €** (476 Aufrufe), 2,09 € frei.


---

# Zweiter Nachgang — N7, N8, N9 (Prüfung 2 vom 20.09.2026)

**0 Modellaufrufe.** Beleg: `ausgaben/18-nachgang-n7-n9.txt`.

## N7 — Der Abbruch, der in keinem Bericht stand

Inhalt von `ausgaben/04g6-gen6.err`, vollständig:

```
ABBRUCH: Lauf 23 ist im Zustand gesaettigt, nicht bereit
```

**Frage 1 — woran ist Generation 6 gescheitert?** Sie ist nicht gescheitert und hat nie begonnen. Der Läufer war
auf die Generationen 5 bis 8 angesetzt. Nach Generation 5 meldete die Entropie Sättigung und beendete den Lauf
(Status `gesaettigt`, Generationen 1–5, Verbesserung 0,00 %). Der Aufruf für Generation 6 traf auf einen
beendeten Lauf und wurde vom Kern abgewiesen — die gewollte Schutzregel. Kein Kandidat, kein Kammerlauf, kein
Modellaufruf. In der Datenbank gibt es keine Generation 6, auch keine abgebrochene:
`[(0, angenommen), (1, angenommen), (2, abgelehnt), (3, abgelehnt), (4, abgelehnt), (5, angenommen)]`.

**Frage 2 — war der Musterbestand vollständig?** Ja. Die angenommenen Generationen sind 1 und 5, beide haben
ihr Muster geschrieben (Generation 1: 2 Muster, Generation 5: 1 Muster). Generation 5 war **vollständig
verarbeitet**, der abgewiesene Aufruf lag danach. Die Bauteil-B-Messung mit 6 fremden Mustern stand auf
vollständigem Bestand.

**Frage 3 — warum stand er in keinem Bericht?** Zwei Ursachen, beide bei mir:
1. Der Läufer schreibt die Abbruchmeldung nur in die `.err`-Datei und sein Log. Der Kern protokolliert die
   Sättigung, aber nicht den abgewiesenen Folgeaufruf. Ich habe für den Bericht die Datenbank gelesen — dort
   stand kein Abbruch, weil keiner war.
2. **Ich habe die `.err`-Dateien nach dem Lauf nicht durchgesehen.** Hätte ich es getan, wäre die Zeile
   aufgefallen und hätte in den Bericht gehört, auch als folgenloser Abbruch.

„Laut scheitern, nie still" gilt auch für einen Abbruch ohne Folgen. Die Lücke liegt im Meldeverhalten, nicht
im Messgerät — Fassung 7, Punkt 6 der Prüfliste.

## N8 — Die Differenz 11 zu 9

**Es fehlt kein Angriff.** 11 Ansagen mit `ausgefuehrt=true` führten zu 11 Angriffs-Modellaufrufen, eins zu
eins nachgewiesen: `#14502→#14503 · #14533→#14534 · #14661→#14662 · #14690→#14691 · #14704→#14705 ·
#14772→#14773 · #14849→#14850 · #15002→#15003 · #15027→#15028 · #15143→#15144 · #15162→#15163`.

Es gibt nur **9 Urteile mit Angriffsabschnitt**, weil drei Angriffe (`#14662`, `#14691`, `#14705`) in **ein
gemeinsames Urteil** `#14707` münden: Der Ankläger prüft einen Kandidaten über seinen ganzen Wirkungskreis
(3.7 Schritt 1) und greift jeden berührten Bereich einzeln an — das Urteil wird je Kandidat geschrieben, nicht
je Bereich. 11 − 2 = 9. Die Rechnung geht auf.

Ergebnis der 9 Urteile, einzeln: `#15006` 1 Test bestätigt → `aegis_k2500_preise` · `#15147` Fund
`aegis_k2526_lager` (Behebung nachgewiesen) · `#14776` 1 Test als Norm · sechs weitere ohne Bestätigung
(Angriffstest bestand am Kandidaten). **1 + 1 + 1 + 6 = 9 ✓**

**Mein Fehler war doppelt:** Erst nannte ich 11 und rechnete 9 auf, ohne die Differenz zu erklären. Dann
erklärte ich sie in diesem Nachgang zunächst falsch („zwei Angriffe ohne Urteil"), weil mein Zuordnungsskript
Urteile der Reihe nach vergab. Erst der Abgleich Ansage → Modellaufruf → Urteil zeigt die Sache. Grundsatz 5,
zum dritten Mal in diesem Abschnitt.

## N9 — Die Messung „2 von 5"

**Protokoll `#13339`, Lauf 23**, Verweise `A132, A359, A249, A6, A141`, 0 erfunden. Sie stammt aus dem
**Nachlauf zu Phase 3** (Beleg dort: `ausgaben/23-artgedaechtnis-muster-messung.txt`) und gehört zu einem
anderen Abschlussordner. Im Nachgangsbericht stand sie in der Prosa ohne Protokollnummer und ohne Tabellenzeile
— der Befund trifft zu, hiermit nachgereicht.

Vollständige Liste aller **zwölf** Mentor-Messungen mit Protokollnummer steht in
`ausgaben/18-nachgang-n7-n9.txt`. Exakt gezählt:

- **9 Messungen ohne werkübergreifenden Verweis:** `#7565` (L16), `#7568` (L17), `#7576` (L16), `#9900` (L18),
  `#9903` (L18), `#10532` (L19), `#11463` (L20), `#12547` (L22), `#13296` (L22). Zwei davon (`#7565`, `#7568`)
  stammen aus der Zeit vor der getrennten Auswertung und tragen kein Zählfeld.
- **3 Messungen mit werkübergreifendem Verweis, alle nach dem Bauteil:** `#13339` (L23) 2 von 5, `#14246` (L22)
  3 von 4, `#14480` (L24) 1 von 5.

Meine Prosa sprach von „sechs aufeinanderfolgenden Mentor-Aufrufen" — es sind **neun** Messungen ohne Verweis.
Dritte ungenaue Zahl in diesem Abschnitt, gleiche Ursache: gezählt aus dem Gedächtnis statt aus dem Protokoll.

## Zu V8 und V9

**V8 (Zeile umbenennen, Auflage):** angenommen. Belegt ist allein die Vorlagenänderung 3 → 6 fremde Muster;
das Zitierverhalten des Mentors streut und wird nicht als Wirkung verbucht.

**V9 (Ansage gegen Ausführung vor der Zeile-8-Messung):** angenommen, und der Einwand ist zwingend — wenn der
Ankläger bei 1 von 2 Tests von seiner Ansage abweicht, sperrt das Bauteil auf eine Behauptung, die mit dem
geschriebenen Test nichts zu tun hat. Eine Zeile-8-Messung darauf wäre wertlos. Die Prüfung gehört vor Tor 4.


---

# Dritter Nachgang — N10, N11 und Auflage A (Prüfung 3 vom 20.09.2026)

**0 Modellaufrufe.** Belege: `ausgaben/19-nachgang-n10.txt`, `ausgaben/20-fremdbeleg-13339-artgedaechtnis-muster.txt`.

## Zur Ablieferung (Auflage A) — was ich prüfen konnte

Der Prüfbericht meldet: `DATEIEN.txt` mit 54 Zeilen und Prüfsumme `c5b53d54…`, `NACHGANG.md` ohne N7–N9.
Auf dem Server liegt und wird ausgeliefert:

```
DATEIEN.txt:            55 Zeilen, SHA-256 54dc6b3fbe4585fb29ad2837c1cf8afa2a6abac043d811a1debfe363b3895ace
PRUEFSUMME-ORDNER.txt:  "SHA-256 ueber DATEIEN.txt (55 Dateien): 54dc6b3f…"
ausgaben/18-nachgang-n7-n9.txt: vorhanden, 5902 Byte
HTTP-Header:            cache-control: no-store, no-cache, must-revalidate
```

Der Abruf über HTTP liefert denselben Stand wie die Platte — ich kann den gemeldeten Unterschied auf meiner
Seite nicht reproduzieren. Wahrscheinlich hat ein Zwischenspeicher auf dem Abrufweg eine ältere Kopie geliefert.

**Ein echter Mangel war es trotzdem, und er lag bei mir:** Der Titel lautete weiterhin „Nachgang N1 bis N6",
obwohl N7–N9 im Dokument standen. Wer den Titel liest, schließt auf den Inhalt. Berichtigt.
Ebenso berichtigt: N2 und N5 trugen noch ihre alten, inzwischen widerrufenen Fassungen — jetzt mit
Berichtigungsvermerk und Verweis auf den maßgeblichen Abschnitt, damit nicht zwei Wahrheiten im Ordner stehen.

## N10 — Zwei oder drei? **Drei Einträge, zwei Funde — und der Maßstab ist gerissen**

Lauf 24 hat **drei** Immunsystem-Einträge erzeugt:

| Eintrag | Art | Schlüssel im Ursprung | Behauptung |
|---|---|---|---|
| `aegis_k2500_preise` | Fund | ja | `preis_fuer|GtE:zahl` |
| `aegis_k2526_lager` | Fund | ja | `gesamtmenge|Eq:zahl` |
| `norm_k2458_lager` | **Norm** (0 Punkte, nicht im Werk) | **nein** | `reservierung_einloesen|raises:NichtGenugBestand` |

**Zeile 8: Bezugsgröße bleibt 2.** Die Zeile misst den Anteil unter den vom Ankläger *erzeugten Tests*, also
unter den Funden. Ein Norm-Eintrag ist kein erzeugter Fund, sondern ein verworfener Test.

**Durchgerutscht: über alle drei neu gemessen — Ergebnis 2, Maßstab GERISSEN.**

Beide Behauptungen standen bereits im übernommenen Vorrat aus Werk 11, und für **keine von beiden gab es eine
Ansage** in Lauf 24:
- `aegis_k2500_preise` (`preis_fuer|GtE:zahl`) entstand aus einem Angriff, der `aufnehmen|raises:ValueError`
  angekündigt hatte (Ansage `#15027`).
- `norm_k2458_lager` (`reservierung_einloesen|raises:NichtGenugBestand`) entstand ohne Ansage dieser Behauptung.

**Berichtigung meiner Messung in N3:** Dort stand Durchgerutscht = 0. Ich hatte nur geprüft, ob ein Test die
**eigene** Ansage wiederholt, und den Fall übersehen, dass er eine **andere vorhandene** Behauptung wiederholt.
Richtig ist **Durchgerutscht = 2**.

**Damit ist der Maßstab zur Hälfte gerissen:** Fehlalarm 0 von 10 erfüllt, Durchgerutscht 2 statt 0.
Das Bauteil sperrt zuverlässig, **was angesagt wird** — aber nicht, **was geschrieben wird**. Die Ursache ist
dieselbe wie beim Zusatzbefund in N3: Der Ankläger weicht von seiner Ansage ab, und die Sperre sieht die
geschriebene Behauptung nie.

**Folge:** V9 („Ansage gegen Ausführung prüfen") ist nicht nur Vorbedingung für Tor 4, sondern die Behebung
genau dieses Befunds. Solange sie fehlt, ist die Filtergüte des Bauteils nicht erfüllt.

## N11 — Beleg `#13339` im Ordner

Der Beleg der Messung „2 von 5" liegt jetzt im versiegelten Ordner:
`ausgaben/20-fremdbeleg-13339-artgedaechtnis-muster.txt` (Kopie aus dem Phase-3-Nachlauf).
Die Fremdadresse, vollständig:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/ausgaben/23-artgedaechtnis-muster-messung.txt

## Meine Wertung nach diesem Nachgang

Vorbedingung 1 ist **nicht erfüllt**. Nicht wegen der Ablieferung, sondern in der Sache: Der von Chat-Claude
gesetzte Maßstab verlangt Fehlalarm 0 **und** Durchgerutscht 0. Gemessen sind 0 und **2**.

Ich beantrage keine Abnahme. Der nächste Schritt ist V9 — Ansage gegen Ausführung prüfen — und danach die
Filtergüte neu messen. Das ist eine Messgerätänderung und damit ein neuer Lauf (Satz 2).
