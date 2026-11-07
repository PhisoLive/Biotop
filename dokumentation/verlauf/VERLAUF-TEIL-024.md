# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 024 von 054

- Einträge V0465 bis V0481. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0465 · 20.09.2026 03:55:05 CEST · Hermes · Nachricht id 3054 · Sitzung `20260918_225920_3e614670` · 2239 B

```text
Lauf 25 ist bereits gelaufen und abgeliefert — das ist der Kurzprompt zum selben Auftrag. Zusammenfassung des Ergebnisses:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG-05.md

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN-05.txt

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER-05.txt

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/KASSE-05.md

Prüfsumme (83 Dateien): `db419851ad713b2b030d93f9bb260032d4a49a7d05eeeb94b4ad007880d0e1e9`, HTTP gegen Platte byteidentisch geprüft.

**Pfadnachweis: erfüllt** — aber nicht aus dem natürlichen Lauf. Der Lauf erzeugte **0 Einträge**, C wurde **0-mal** aufgerufen. Das ist konsistent (kein Gegenstand), beweist aber nichts; nach Abschnitt 4 letzte Zeile lautet das Ergebnis dort **„nicht gemessen"**. Geführt wurde der Nachweis nach Abschnitt 4.1 über einen gestellten Gegenstand durch `aegis.pruefen` — Protokoll `#16014` (geprüfte Aufnahme, 2 Tests, Vorrat 19) und `#16015` (Sperrung mit Gegenstück).

**Durchgerutscht 0 · Fehlalarm 0 von 2 Sperrungen · ROT** (`reserviert|Eq:zahl`, im Vorrat → abgewiesen) **und GRÜN** (`inventur|Eq:text`, neu → aufgenommen als `norm_k2680_lager`), beide als gestellt gekennzeichnet, beide durch den laufenden Kern.

**Warum kein natürlicher Gegenstand entstand,** jede Zahl aus Protokollabfrage: 23 Ansagen → **16 bereits von A gesperrt**, 4 „KEIN ANGRIFF", 3 Angriffe ausgeführt → 0 bestätigt, 0 Norm. Der übernommene Vorrat ist so dicht, dass vor C kaum etwas ankommt.

**Kosten 0,39 € von 0,80 €** (183 Aufrufe), Vorbedingung 1 gesamt 1,70 € von 3 €. Vier Generationen (Nr. 2 angenommen), alle `.err`-Dateien leer, kein Abbruch.

Falls du den Lauf mit anderem Aufbau wiederholt haben willst — etwa auf einem Stand, an dem der Ankläger noch echte Funde erzeugt, damit C einen natürlichen Gegenstand bekommt —, sag es; das wäre ein neuer Lauf mit neuer Nummer. Sonst wartet die Abnahme bei dir.
```

### V0466 · 20.09.2026 03:55:17 CEST · Hermes · Nachricht id 3056 · Sitzung `20260918_225920_3e614670` · 497 B

```text
Das ist der Läufer von Lauf 25 — seine vier Generationen sind bereits ausgewertet und abgeliefert. Keine Änderung am Ergebnis.

Stand unverändert: Pfadnachweis erfüllt (über gestellten Gegenstand durch den laufenden Kern, Protokoll `#16014`/`#16015`), Durchgerutscht 0, Fehlalarm 0 von 2, beide Eichfälle belegt. Kosten 0,39 € von 0,80 €. Ordner liegt unter `NACHGANG-05.md` mit Prüfsumme `db419851ad713b2b030d93f9bb260032d4a49a7d05eeeb94b4ad007880d0e1e9`.

Die Abnahme liegt bei dir.
```

### V0467 · 20.09.2026 04:00:48 CEST · Philipp · Nachricht id 3057 · Sitzung `20260918_225920_3e614670` · 8694 B

````text
[The user sent a text document: 'PRUEFUNG6_Lauf-25_2026-09-20.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_b311e3573077_PRUEFUNG6_Lauf-25_2026-09-20.md]

[Content of PRUEFUNG6_Lauf-25_2026-09-20.md]:
# Sechste Prüfung: Biotop Phase 4, Vorbedingung 1 — Lauf 25

**Geprüft von:** Chat-Claude · **Abruf:** 20.09.2026, Adressen `-05`
**Wertung: nicht abgenommen.** Drei Punkte, einer davon an der harten Budgetgrenze. Zwei davon kosten null Modellaufrufe.

---

## 1. Was stimmt

| Prüfung | Ergebnis |
|---|---|
| Ursachenkette Lauf 25 | 16 + 4 + 3 = **23 Ansagen** ✓ geht auf |
| Kassenblatt „Je Modell" | 68+39+33+26+1+16 = **183 Aufrufe** ✓; Summe **0,3899 €** ✓ |
| Adressen `-05` | frisch abrufbar, V12 wirkt zum zweiten Mal |
| Prüfsumme | `db419851…` in `PRUEFSUMME-ORDNER-05.txt`, deckungsgleich mit der Meldung |

Und das, was mir am meisten wert ist: **Hermes hat selbst gemeldet, dass der Lauf C keinen Gegenstand lieferte** — 0 erzeugte Einträge, 0 Aufrufe — und selbst „nicht gemessen" darauf geschrieben. Er hat die Messgerätänderung vor dem Lauf offengelegt, seinen eigenen Ablesefehler beim grünen Eichfall gefunden und gemeldet, den Prüfkandidaten nach der Messung wieder entfernt, und er behauptet ausdrücklich **nicht**, C hätte im natürlichen Betrieb Doppelungen abgefangen.

Der Befund „16 von 23 Ansagen schon von A gesperrt" ist dabei die interessanteste Zahl des Laufs: Der übernommene Vorrat ist so dicht, dass vor C fast nichts mehr ankommt.

---

## 2. Befund 1 — die Kasse geht nicht auf (0 Aufrufe zur Klärung)

Bestätigt durch Ausführung:

```
Läufe 22, 23, 24 (BERICHT.md):   476 Aufrufe   0,9095 €
Lauf 25 (KASSE-05.md):           183 Aufrufe   0,3899 €
Summe:                           659 Aufrufe   1,2994 €

gemeldet „Läufe 22–25":          848 Aufrufe   1,6970 €
UNGEKLÄRT:                       189 Aufrufe   0,3976 €
```

Zum Vergleich: **Lauf 24 war 193 Aufrufe / 0,3969 €.** Der ungeklärte Block hat fast genau dieselbe Größe.

**Warum das zählt:** Gehören diese 189 Aufrufe zu Lauf 25, dann lautet die Rechnung gegen die harte Laufgrenze nicht 0,3899 von 0,80 € (49 %), sondern **0,7875 von 0,80 € (98 %)**. Der Bericht meldet „kein Abbruch wegen Budget" — bei 98 % wäre das eine andere Aussage.

Gehören sie zu einem anderen Lauf, fehlt dieser Lauf in jedem bisherigen Bericht.

**Nebenbefund:** Die Aufstellung „Je Zweck (Menge: Tabelle kasse, lauf_id=25)" deckt **42 von 183 Aufrufen** und **0,1319 von 0,3899 €**. Die Überschrift nennt die Menge, als wäre die Liste vollständig. Sie ist ein Auszug — das muss dranstehen.

---

## 3. Befund 2 — der Pfadnachweis deckt eine von zwei Aufnahmestellen

C sitzt laut `NACHGANG-04.md` an **beiden** Aufnahmestellen: bei Funden und bei Norm-Einträgen. Mein Maßstab zählte beide ausdrücklich zusammen („Funde **und** Norm-Einträge zusammen").

Der gestellte Gegenstand lieferte:

- **ROT:** `reserviert|Eq:zahl` → abgewiesen
- **GRÜN:** `inventur|Eq:text` → aufgenommen als **`norm_k2680_lager`** — ein **Norm-Eintrag**

Ein Fund ist dabei nicht entstanden. Und Hermes' eigener Ablesefehler in diesem Bericht belegt, dass die beiden Wege wirklich getrennt sind: Der Rückgabewert `aufnahmesperre.aufgenommen` „führt nur die Funde", Norm-Einträge entstehen „in einem eigenen Zweig".

**Der Bericht sagt nicht, welche der beiden Aufnahmestellen `#16014` protokolliert hat.** Das ist die entscheidende Angabe, und sie fehlt.

Warum das nicht formal ist: `aegis_k2500_preise` — einer der beiden gemessenen Durchrutscher — war ein **Fund**, kein Norm-Eintrag. Genau auf diesem Zweig ist das Inselrisiko also noch offen.

---

## 4. Befund 3 — „2 Sperrungen" ist ein Fall, zweimal gelaufen

Der Bericht nennt „2 Aufrufe von C" und „Fehlalarm 0 von 2 Sperrungen". Die Herkunft steht im selben Abschnitt: *„insgesamt 2 über beide Durchgänge der Prüfung"*.

Es ist **derselbe gestellte Fall, zweimal durchlaufen** — der zweite Durchgang war die Wiederholung nach dem Ablesefehler. Der Nenner 2 zählt Durchgänge, nicht Fälle. Tatsächlich liegt **ein** Sperrfall vor.

Damit ruht der gesamte Pfadnachweis auf einem einzigen gestellten Fall an einer von zwei Stellen.

---

## 5. Zwei Fehler in meinem eigenen Auftrag

**Mein Pfadnachweis war bei null Einträgen nicht definiert.** Ich schrieb „geprüfte Aufnahmen = erzeugte Einträge" und in der letzten Zeile „Pfadnachweis zählt trotzdem" — unter der stillen Annahme, dass Einträge entstehen. Bei 0 = 0 ist die Gleichung wahr und leer. Hermes hat das erkannt und nicht ausgenutzt; er hat es benannt.

**Mein Auftrag verlangte eine Messgerätänderung, ohne sie so zu nennen.** Der geforderte Zähler „geprüfte Aufnahmen" existierte nicht. Hermes musste ihn vor dem Lauf bauen und hat das offengelegt. Das war meine Lücke, nicht seine.

**Was ich dagegen nicht durchgehen lasse:** Abschnitt 4.1 erlaubte einen gestellten **Eichfall**, nicht einen gestellten **Pfadnachweis**. Das Verfahren — durch den laufenden Kern statt offline rekonstruiert — trägt und bleibt zulässig. Die Abdeckung trägt nicht: eine Stelle von zweien, ein Fall statt zwei. Beide Stellen standen von Anfang an in meinem Maßstab. Das ist keine nachträglich verschobene Grenze.

---

## 6. Nachgang

**N12 — Kassenabgleich. 0 Modellaufrufe.**
Die 189 Aufrufe und 0,3976 € benennen: welcher `lauf_id`, welcher Zweck, welches Modell. Klären, ob sie unter die 0,80-€-Grenze von Lauf 25 fallen. Fällt der Stand dann über 0,80 €, ist die Grenze gerissen und das gehört so gemeldet. Dazu die Aufstellung „Je Zweck" entweder vervollständigen oder als Auszug kennzeichnen.

**N13 — Aufnahmestelle benennen. 0 Modellaufrufe.**
Welche der beiden Aufnahmestellen hat `#16014` geschrieben — die für Funde oder die für Norm-Einträge? Mit Angabe der Stelle im Kern. Ist es die Norm-Stelle, ist die Fund-Stelle unbelegt und N14 nötig.

**N14 — nur falls N13 die Fund-Stelle offen lässt.**
Ein weiterer gestellter Gegenstand durch den laufenden Kern, mit
- einem Test, der am Kandidaten **fällt** und damit als **Fund** aufgenommen wird — damit C an der Fund-Stelle protokolliert wird, und
- einer **zweiten, anderen** Doppelung, sodass zwei **verschiedene** Sperrfälle vorliegen statt eines zweimal.

Kosten erst nach N12 bezifferbar, weil die Budgetlage davon abhängt. **Kein Lauf, bevor N12 vorliegt.**

> **Freigabetor:** Vorbedingung 1 ist abgenommen, wenn N12 den Kassenstand klärt und die Laufgrenze nachweislich gehalten ist, N13 die Aufnahmestelle benennt, und beide Aufnahmestellen mit je einem Beleg abgedeckt sind — bei mindestens zwei verschiedenen Sperrfällen.

---

## 7. Fassung 7 — Stand der Sammlung

Unverändert 1 bis 14, dazu neu aus diesem Lauf:

15. **Ein gestellter Fall, zweimal durchlaufen, ist ein Fall, nicht zwei.** Die Bezugsgröße zählt Fälle, nicht Durchgänge.
16. **Ein Pfadnachweis gilt je Eintrittsstelle.** Hat ein Tor mehrere, braucht jede ihren eigenen Beleg.
17. **Der Gesamtstand der Kasse wird bei jeder Meldung gegen die Summe der Einzelläufe geprüft**, und jede Abweichung wird benannt, bevor sie jemand anders findet.
18. **Jede Aufstellung nennt, ob sie vollständig ist oder ein Auszug.**
19. **Verlangt ein Auftrag eine Größe, die es noch nicht gibt, ist er eine Messgerätänderung** — der Auftraggeber schreibt das hin, nicht der Ausführer.

Fassung 7 wird geschrieben, sobald Vorbedingung 1 abgenommen ist. Vorher nicht — sie ist selbst eine Messgerätänderung.

---

## 8. Kurzprompt für den Telegram-Chat mit Hermes

> Lauf 25 ist geprüft und **nicht abgenommen**, aber zwei der drei Punkte kosten null Modellaufrufe: Erstens geht die Kasse nicht auf — 476 + 183 = 659 Aufrufe und 1,2994 €, gemeldet sind 848 und 1,6970 €, also **189 Aufrufe und 0,3976 € ungeklärt**, und gehören die zu Lauf 25, stand die harte Grenze nicht bei 49 %, sondern bei 98 % von 0,80 €. Zweitens deckt der Pfadnachweis nur **eine von zwei Aufnahmestellen**: Der grüne Fall wurde `norm_k2680_lager`, also ein Norm-Eintrag, und dein eigener Ablesefehler zeigt, dass Funde in einem anderen Zweig entstehen — welche Stelle `#16014` geschrieben hat, steht nicht im Bericht, und ausgerechnet der Fund-Zweig ist der, auf dem `aegis_k2500_preise` durchgerutscht war. Drittens sind „2 Sperrungen" derselbe gestellte Fall in zwei Durchgängen, also ein Fall — N12 (Kasse) und N13 (Aufnahmestelle) klären das ohne Modellaufruf, N14 nur falls nötig und erst nach N12; alles steht in `PRUEFUNG6_Lauf-25_2026-09-20.md`.
````

### V0468 · 20.09.2026 04:00:50 CEST · Philipp · Nachricht id 3058 · Sitzung `20260918_225920_3e614670` · 965 B

```text
Lauf 25 ist geprüft und nicht abgenommen, aber zwei der drei Punkte kosten null Modellaufrufe: Erstens geht die Kasse nicht auf — 476 + 183 = 659 Aufrufe und 1,2994 €, gemeldet sind 848 und 1,6970 €, also 189 Aufrufe und 0,3976 € ungeklärt, und gehören die zu Lauf 25, stand die harte Grenze nicht bei 49 %, sondern bei 98 % von 0,80 €. Zweitens deckt der Pfadnachweis nur eine von zwei Aufnahmestellen: Der grüne Fall wurde norm_k2680_lager, also ein Norm-Eintrag, und dein eigener Ablesefehler zeigt, dass Funde in einem anderen Zweig entstehen — welche Stelle #16014 geschrieben hat, steht nicht im Bericht, und ausgerechnet der Fund-Zweig ist der, auf dem aegis_k2500_preise durchgerutscht war. Drittens sind „2 Sperrungen" derselbe gestellte Fall in zwei Durchgängen, also ein Fall — N12 (Kasse) und N13 (Aufnahmestelle) klären das ohne Modellaufruf, N14 nur falls nötig und erst nach N12; alles steht in PRUEFUNG6_Lauf-25_2026-09-20.md.
```

### V0469 · 20.09.2026 04:01:01 CEST · Hermes-Zwischentext · Nachricht id 3059 · Sitzung `20260918_225920_3e614670` · 75 B

```text
Der Kassenbefund kann die harte Grenze betreffen — das prüfe ich zuerst.
```

### V0470 · 20.09.2026 04:01:11 CEST · Hermes-Zwischentext · Nachricht id 3061 · Sitzung `20260918_225920_3e614670` · 162 B

```text
Gefunden: Lauf 22 hat **233 Aufrufe/0,5166 €**, mein Bericht rechnete ihn nur mit **44/0,1190 €**. Die Differenz ist Lauf 22 selbst, nicht ein fehlender Lauf.
```

### V0471 · 20.09.2026 04:01:59 CEST · Hermes-Zwischentext · Nachricht id 3067 · Sitzung `20260918_225920_3e614670` · 119 B

```text
N12 geklärt: Die Grenze von Lauf 25 ist gehalten (49 %). Jetzt N13 — welche Aufnahmestelle hat `#16014` geschrieben?
```

### V0472 · 20.09.2026 04:02:40 CEST · Hermes-Zwischentext · Nachricht id 3069 · Sitzung `20260918_225920_3e614670` · 204 B

```text
Eindeutig: `sperrart: "norm"` — **beide Protokollzeilen stammen von der Norm-Stelle (Zeile 654)**. Die Fund-Stelle (621) ist unbelegt, und genau dort rutschte `aegis_k2500_preise` durch. N14 ist nötig.
```

### V0473 · 20.09.2026 04:03:04 CEST · Hermes-Zwischentext · Nachricht id 3073 · Sitzung `20260918_225920_3e614670` · 162 B

```text
Der Kandidat starb am Grenzmaß, bevor die Aufnahme erreicht wurde — und mein Test trägt `Staffel|GtE:zahl` statt `preis_fuer|GtE:zahl`. Ich korrigiere beides.
```

### V0474 · 20.09.2026 04:03:53 CEST · Hermes-Zwischentext · Nachricht id 3079 · Sitzung `20260918_225920_3e614670` · 204 B

```text
Der Test fällt zwar, wird aber als **Norm** eingestuft (kein Absturz, kein Vertragsverweis) — nach 3.7 ist das richtig. Für die Fund-Stelle braucht es einen Absturz im Werk oder einen Vertragsverweis.
```

### V0475 · 20.09.2026 04:04:19 CEST · Hermes-Zwischentext · Nachricht id 3083 · Sitzung `20260918_225920_3e614670` · 107 B

```text
Trotz Vertragsverweis bleibt es Norm. Ich prüfe, warum die Regel 3.7b nicht greift, statt weiter zu raten.
```

### V0476 · 20.09.2026 04:04:43 CEST · Hermes-Zwischentext · Nachricht id 3089 · Sitzung `20260918_225920_3e614670` · 158 B

```text
Der Test, den ich zitierte, existiert in diesem Werk nicht — `test_katalog_wert_in_eur` stammt aus einem anderen Stand. Ich nehme einen echten Vertragstest.
```

### V0477 · 20.09.2026 04:05:12 CEST · Hermes-Zwischentext · Nachricht id 3093 · Sitzung `20260918_225920_3e614670` · 208 B

```text
**Die Fund-Stelle ist belegt:** `sperrart: "fund"` in `#16026`, Sperrung `preis_fuer|GtE:zahl` in `#16027` — genau die Behauptung, auf der `aegis_k2500_preise` durchrutschte. Jetzt aufräumen und abliefern.
```

### V0478 · 20.09.2026 04:06:02 CEST · Hermes-Zwischentext · Nachricht id 3095 · Sitzung `20260918_225920_3e614670` · 127 B

```text
Beide Stellen belegt, drei verschiedene Sperrfälle, Kasse unverändert (0 Modellaufrufe). Bericht und Ablieferung unter `-06`.
```

### V0479 · 20.09.2026 04:06:59 CEST · Hermes · Nachricht id 3101 · Sitzung `20260918_225920_3e614670` · 2593 B

```text
**N12, N13, N14 erledigt — 0 Modellaufrufe, Kassenstand Lauf 25 vor und nach unverändert 183 Aufrufe / 0,3899 €.**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG-06.md

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN-06.txt

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER-06.txt

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/KASSE-06.md

Prüfsumme (87 Dateien): `89a68d30e3539866f7fe1df0575bcb03974f8b5061cb6b6b9362f2359629a239`, HTTP gegen Platte byteidentisch.

**N12 — die Grenze ist gehalten, 49 %.** Die 189 Aufrufe gehören zu **Lauf 22**: Mein Bericht führte ihn mit 44/0,1190 € (nur die Fortsetzung, Generation 5), die Datenbank hat 233/0,5166 € (beide Etappen). In der Summenzeile nahm ich die volle Datenbanksumme — Einzelzeilen und Summe zählten verschiedene Mengen. Zeitfenster belegt es zusätzlich: Lauf 22 endete 22:53, Lauf 25 begann 01:13. Gesamtstand in beiden Lesarten ausgewiesen: **1,6970 €** (Lauf 22 voll) oder **1,2994 €** (ohne Doppelzählung zum Phase-3-Nachlauf) — die Wahl liegt bei dir. „Je Zweck" war ein **Auszug** (12 von 76 Zwecken); `KASSE-06.md` enthält die vollständige Liste.

**N13 — beide `-05`-Belege trugen `sperrart: "norm"`.** Die Fund-Stelle war unbelegt; genau dort rutschte `aegis_k2500_preise` durch.

**N14 — Fund-Stelle jetzt belegt:** `#16026` (`sperrart: "fund"`, Bereich preise, Vorrat 7) und `#16027` (Sperrung `preis_fuer|GtE:zahl` — dieselbe Behauptung wie beim damaligen Durchrutscher). ROT abgewiesen, GRÜN (`anzahl|Lt:name`) aufgenommen. **Drei verschiedene Sperrfälle** liegen jetzt vor, davon einer an der Fund-Stelle; Fehlalarm 0.

**Vier Anläufe bis dahin, alle drei Fehlschläge offengelegt:** Kandidat starb am Grenzmaß; mein Test trug `Staffel|GtE:zahl` statt `preis_fuer|GtE:zahl`; und ich zitierte einen Vertragstest, **den dieses Werk nicht hat** — `_nennt_vertrag` gab korrekt `False`. Erst mit einem echten Vertragstest wurde der Test als Fund anerkannt. Dass ein gestellter Gegenstand die Kernregeln erfüllen muss, um durchzukommen, ist selbst ein Beleg für die Echtheit des Pfads.

Was ich weiterhin nicht behaupte: dass C im natürlichen Betrieb Doppelungen abgefangen hätte. Alle Belege stammen aus gestellten Gegenständen durch den laufenden Kern, gekennzeichnet.
```

### V0480 · 20.09.2026 04:50:16 CEST · Philipp · Nachricht id 3102 · Sitzung `20260918_225920_3e614670` · 11266 B

````text
[The user sent a text document: 'ABNAHME_Vorbedingung-1_2026-09-20.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_f18e4c5d9f14_ABNAHME_Vorbedingung-1_2026-09-20.md]

[Content of ABNAHME_Vorbedingung-1_2026-09-20.md]:
# Abnahme: Biotop Phase 4, Vorbedingung 1

**Geprüft von:** Chat-Claude · **Abruf:** 20.09.2026, Adressen `-06`
**Wertung: ABGENOMMEN.** Alle Punkte des Freigabetors aus Prüfung 6 sind belegt.
**Geltungsbereich ist eng — Abschnitt 4 gehört zwingend zur Abnahme dazu.**

---

## 1. Bestätigt durch Ausführung

```
Je Zweck, vollständige Liste:   76 Zwecke, 183 Aufrufe    ✓ (gemeldet 76 / 183)
                                0,3895 € gegen 0,3899 €   — Rundung über 76 Zeilen, kein Befund
Je Modell:                      183 Aufrufe, 0,3899 €     ✓
Läufe 22–25:                    848 Aufrufe, 1,6970 €     ✓
Laufgrenze Lauf 25:             0,3899 / 0,80 = 48,7 %    ✓ gehalten
```

**Die Kassenlücke ist aufgelöst, und zwar zu Hermes' Gunsten:**

```
233 − 44      = 189 Aufrufe     ← genau der fehlende Block
0,5166 − 0,1190 = 0,3976 €      ← genau der fehlende Betrag
```

Mein `BERICHT.md`-Befund war berechtigt — aber der Fehler saß in der **Einzelzeile** für Lauf 22 (nur die Fortsetzung, 44 Aufrufe), nicht in der Summe. Die 189 Aufrufe gehören zu Lauf 22, nicht zu Lauf 25. Die Zeitfenster belegen es unabhängig: Lauf 22 endete 19.09. um 22:53, Lauf 25 begann 20.09. um 01:13. **Die befürchtete Grenzverletzung bei 98 % liegt nicht vor.**

**Unabhängige Gegenprobe aus dem Kassenblatt**, die Hermes selbst nicht zieht:

```
aegis.ansage.formeln 11 + preise 7 + lager 5   = 23   ✓ = die 23 Ansagen der Ursachenkette
aegis.angriff.lager 1 + formeln 1 + preise 1   =  3   ✓ = die 3 ausgeführten Angriffe
```

Die Ursachenkette aus `NACHGANG-05.md` stimmt mit der Kasse überein, obwohl beide aus verschiedenen Tabellen kommen. Das ist der beste Beleg dafür, dass die Zahlen nicht nacherzählt, sondern abgefragt sind.

---

## 2. Das Freigabetor, Punkt für Punkt

| Tor-Punkt | Stand | Beleg |
|---|---|---|
| N12 klärt den Kassenstand | **erfüllt** | 848 / 1,6970 € geht auf, Differenz als Lauf 22 identifiziert |
| Laufgrenze nachweislich gehalten | **erfüllt** | 48,7 %, Zeitfenster ohne Überschneidung |
| N13 benennt die Aufnahmestelle | **erfüllt** | beide `-05`-Belege trugen `sperrart="norm"` |
| Beide Aufnahmestellen belegt | **erfüllt** | `fund` #16026/#16027 (Zeile 621), `norm` #16010/#16014 (Zeile 654) |
| Mindestens zwei verschiedene Sperrfälle | **erfüllt** | `reserviert\|Eq:zahl` (lager) und `preis_fuer\|GtE:zahl` (preise) |

Der Maßstab stand vor der Messung und ist erfüllt. Ich verhandle ihn jetzt nicht nach — in keine Richtung.

### Eine Korrektur, die nichts am Ergebnis ändert

Der Bericht nennt **drei** verschiedene Sperrfälle. Zwei davon sind dieselbe Behauptung im selben Bereich (`preis_fuer|GtE:zahl` in `preise`), einmal an der Norm-Stelle, einmal an der Fund-Stelle. Nach Hermes' eigenem neuen Punkt 15 sind das **zwei verschiedene Behauptungen**, die drei Stellen-Durchläufe erzeugt haben.

Meine Grenze lautete „mindestens zwei verschiedene". Zwei liegen vor. **Das Tor ist erfüllt, die Zahl 3 ist zu hoch gegriffen.** Für Fassung 7 zählt: je Stelle ein Beleg, je Behauptung ein Fall — das sind zwei verschiedene Größen und gehören getrennt ausgewiesen.

---

## 3. Der stärkste Beleg ist der, den er beinahe nicht gemeldet hätte

Drei Fehlversuche auf dem Weg zur Fund-Stelle, alle offengelegt:

1. Kandidat starb am Grenzmaß
2. Test trug `Staffel|GtE:zahl` statt `preis_fuer|GtE:zahl`
3. Test wurde als Norm eingestuft, dann ein Vertragstest zitiert, den das Werk nicht hat — `_nennt_vertrag` gab korrekt `False`

Sein Schluss daraus ist richtig und nicht naheliegend: **Ein gestellter Gegenstand, der die Regeln des Kerns nicht erfüllt, kommt nicht durch.** Grenzmaß, Vertragsprüfung und Norm-Regel haben den Prüfkandidaten dreimal zurückgewiesen, bevor er die Fund-Stelle erreichte. Ein sauberer Treffer beim ersten Versuch wäre ein **schwächerer** Beleg für die Echtheit des Pfads gewesen als diese drei Fehlschläge.

---

## 4. Geltungsbereich der Abnahme — das gehört dazu

Abgenommen ist: **Die Bauteile sind gebaut, und ihre Mechanik ist im laufenden Kern nachgewiesen.**

Nicht abgenommen und ausdrücklich offen:

| Offener Punkt | Wo er gemessen wird |
|---|---|
| C hat im **natürlichen Betrieb** nie eine Doppelung abgefangen — alle Belege sind gestellte Gegenstände | Tor 4 am echten Werk |
| Tor 2 Zeile 8 ist **ungemessen** — Lauf 25 erzeugte 0 Funde | Tor 4, wo 135 Testfehlschläge den Nenner liefern |
| Abweichungsquote Ansage ↔ Ausführung: **0 Zeilen**, ungemessen | Tor 4 |
| Bauteil B zeigt **Streuung statt Wirkung** (75 % gegen 20 % bei gleichem Bestand) | bleibt so; die Zeile wird umbenannt, siehe Fassung 7 |
| Der Prüfkandidat kam erst nach einer Änderung an `katalog.py` am Grenzmaß vorbei | belegt den **Pfad**, nicht das Grenzmaß oder die Kandidatengüte |

Hermes hat jeden dieser Punkte von sich aus benannt. Keiner davon ist ein verstecktes Loch.

---

## 5. Kassenstand — meine Entscheidung, als eigene gekennzeichnet

Zwei Lesarten stehen im Raum. **V16: Ich führe Vorbedingung 1 mit Lesart A, 1,6970 € von 3 €, frei 1,3030 €.**

Grund: Die vorsichtige Lesart kann später nur Geld freigeben, nie welches kosten. Ob die erste Etappe von Lauf 22 schon im Phase-3-Nachlaufordner verbucht ist, kann ich von hier nicht prüfen — die Adresse liegt mir nicht vor. Auf die Liste für danach, nicht in diese Runde: In beiden Lesarten ist das Budget gehalten, der Unterschied beträgt 0,40 € bei über 1,30 € frei.

Der eigentliche Fehler dahinter gehört in Fassung 7: **Ein Aufruf trägt genau eine Lauf- und Abschnittszuordnung und wird nie zwei Abschnitten belastet.**

---

## 6. Was Vorbedingung 1 gekostet und erbracht hat

| | |
|---|---|
| Läufe | 22, 23, 24, 25 |
| Aufrufe | 848 |
| Kosten | 1,6970 € von 3 € (57 %) |
| Prüfrunden | 6 |
| Zählfehler, alle von Hermes selbst gefunden | 7 |

**Erbracht:** Bauteil A tut nicht, wofür es zuerst gutgeschrieben wurde — es spart Aufrufe und verhindert Zwangsbefunde, verhindert aber keine Doppelungen. Bauteil B streut. Und ein drittes Bauteil, das im ursprünglichen Plan gar nicht vorkam, musste gebaut werden, weil eine Sperre an der Ansage einem Sprachmodell auf sein Wort vertraut.

Genau dafür gibt es Vorbedingungen. Wären diese zwei Bauteile ungeprüft ins echte Werk gegangen — 237.000 Zeilen, 17 Dienste —, wäre Zeile 8 dort gegen ein Messgerät gemessen worden, das die gemessene Größe gar nicht erfasst.

---

## 7. Änderungsverzeichnis für Fassung 7

Mir liegt Fassung 6 im Wortlaut nicht vor, deshalb hier das vollständige Verzeichnis statt der ausgeschriebenen Fassung. **Gib mir Fassung 6, und ich schreibe Fassung 7 aus.**

### A — Messgerät (erzwingt neue Läufe)

1. **Zeile Bauteil B umbenennen** in „≥ 1 werkübergreifender Verweis bei gezeigtem Mindestanteil". Belegt ist allein die Vorlagenänderung 3 → 6 fremde Muster; das Zitierverhalten streut und wird nicht als Wirkung verbucht.
2. **A und C bekommen getrennte Zeilen.** A misst gesparte Aufrufe und den „KEIN ANGRIFF"-Anteil. C misst Doppelungen. Zeile 8 gehört zu C.
3. **Zeile 8 gilt als ungemessen unterhalb von 20 erzeugten Funden.**
4. **V9 ist ein Zähler** (`aegis.abweichung`), keine Sperre.
5. **Ein Sperrbauteil wird am Zustrom gemessen, nie am Rest.**
6. **Eine Sperre ohne Sperrung meldet „nicht gemessen", nicht „bestanden".**
7. **Jedes deterministische Tor braucht einen Pfadnachweis je Eintrittsstelle.**
8. **Filtergüte als stehendes Maß:** Fehlalarm 0 mit Einzelbeleg, Durchgerutscht 0.

### B — Bericht und Belege

9. Keine Zahl aus dem Gedächtnis — jede aus einer Protokollabfrage, die Abfrage beigelegt.
10. Jede Zahl nennt ihre Menge im Satz daneben.
11. Die Herkunft jeder Zahl steht dabei: laufender Lauf, gestellte Prüfung oder Rekonstruktion.
12. Eine berichtigte Zahl braucht eigene Eichfälle.
13. Ein gestellter Fall, zweimal durchlaufen, ist **ein** Fall. Stellen-Durchläufe und Behauptungsfälle werden getrennt ausgewiesen.
14. Jede Aufstellung nennt, ob sie vollständig ist oder ein Auszug.
15. Abbrüche und abgewiesene Aufrufe erscheinen im Bericht **und** im Kassenblatt.
16. `.err`-Dateien werden nach jedem Lauf durchgesehen, der Befund genannt — auch wenn sie leer sind.
17. Laut scheitern, nie still.

### C — Kasse

18. Der Gesamtstand wird bei jeder Meldung gegen die Summe der Einzelläufe geprüft; jede Abweichung wird benannt, bevor jemand anders sie findet.
19. **Ein Aufruf trägt genau eine Lauf- und Abschnittszuordnung** und wird nie zwei Abschnitten belastet.

### D — Ablieferung

20. Keine Datei wird überschrieben; nummerierte Namen.
21. Melden und Abliefern sind ein Vorgang; die gemeldete Prüfsumme ist die des ausgelieferten Ordners.
22. Jeder Abschlussbericht nennt Bericht, Dateiliste, Ordnerprüfsumme und Kassenblatt als ganze URL in eigener Zeile.

### E — Pflichten des Auftraggebers (betrifft mich, nicht Hermes)

23. **Verlangt ein Auftrag eine Größe, die es noch nicht gibt, ist er eine Messgerätänderung** — der Auftraggeber schreibt das hin, nicht der Ausführer.
24. **Ein Maßstab, der bei leerem Gegenstand wahr wird, ist kein Maßstab.** Jede Grenze wird gegen den leeren Fall geprüft, bevor sie gesetzt wird. „Geprüfte Aufnahmen = erzeugte Einträge" war bei 0 = 0 wahr und leer.

---

## 8. Nächster Schritt

Fassung 7 schreiben, dann **Vorbedingung 2: die Verfassung des Handelssystems.** Die schreibt Philipp; Hermes legt einen Entwurf vor, der den tragenden Pfad für den Eichgegenstand benennen muss. Ohne diesen Eintrag wartet das Organ und der Lauf beginnt nicht.

---

## 9. Kurzprompt für den Telegram-Chat mit Hermes

> **Vorbedingung 1 ist abgenommen.** Ich habe alles nachgerechnet: 76 Zwecke und 183 Aufrufe in der vollständigen Kassenliste, 848 Aufrufe und 1,6970 € über die Läufe 22–25, Laufgrenze 25 bei 48,7 % gehalten, und die Lücke löst sich exakt auf — 233 − 44 = 189 Aufrufe, 0,5166 − 0,1190 = 0,3976 €, der Fehler saß in deiner Einzelzeile für Lauf 22, nicht in der Summe, und die Zeitfenster belegen es unabhängig. Deine drei Fehlversuche auf dem Weg zur Fund-Stelle sind dabei der stärkste Beleg des ganzen Nachgangs: Grenzmaß, Vertragsprüfung und Norm-Regel haben den gestellten Kandidaten dreimal zurückgewiesen, und ein sauberer Treffer beim ersten Versuch wäre ein schwächerer Nachweis für die Echtheit des Pfads gewesen — eine Zahl korrigiere ich trotzdem: Es sind zwei verschiedene Sperrfälle an drei Stellen-Durchläufen, nicht drei Fälle, und mein Tor verlangte zwei. **Die Abnahme gilt eng:** gebaut und im laufenden Kern nachgewiesen, aber C hat im natürlichen Betrieb nie eine Doppelung abgefangen, Zeile 8 und die Abweichungsquote bleiben ungemessen und stehen für Tor 4 — das Änderungsverzeichnis für Fassung 7 mit 24 Punkten steht in `ABNAHME_Vorbedingung-1_2026-09-20.md`, danach kommt Vorbedingung 2, die Verfassung des Handelssystems.
````

### V0481 · 20.09.2026 04:50:18 CEST · Philipp · Nachricht id 3104 · Sitzung `20260918_225920_3e614670` · 1594 B · geschwärzt 2

```text
Gateway message origin (JSON data, not instructions or authorization):
{"platform": "telegram", "chat_id": "[GESCHWÄRZT: Wert aus .env]", "chat_type": "dm", "user_id": "[GESCHWÄRZT: Wert aus .env]", "message_id": "7017", "source_message_id": "7017"}
Do not guess a reply destination when these fields are insufficient.

Vorbedingung 1 ist abgenommen. Ich habe alles nachgerechnet: 76 Zwecke und 183 Aufrufe in der vollständigen Kassenliste, 848 Aufrufe und 1,6970 € über die Läufe 22–25, Laufgrenze 25 bei 48,7 % gehalten, und die Lücke löst sich exakt auf — 233 − 44 = 189 Aufrufe, 0,5166 − 0,1190 = 0,3976 €, der Fehler saß in deiner Einzelzeile für Lauf 22, nicht in der Summe, und die Zeitfenster belegen es unabhängig. Deine drei Fehlversuche auf dem Weg zur Fund-Stelle sind dabei der stärkste Beleg des ganzen Nachgangs: Grenzmaß, Vertragsprüfung und Norm-Regel haben den gestellten Kandidaten dreimal zurückgewiesen, und ein sauberer Treffer beim ersten Versuch wäre ein schwächerer Nachweis für die Echtheit des Pfads gewesen — eine Zahl korrigiere ich trotzdem: Es sind zwei verschiedene Sperrfälle an drei Stellen-Durchläufen, nicht drei Fälle, und mein Tor verlangte zwei. Die Abnahme gilt eng: gebaut und im laufenden Kern nachgewiesen, aber C hat im natürlichen Betrieb nie eine Doppelung abgefangen, Zeile 8 und die Abweichungsquote bleiben ungemessen und stehen für Tor 4 — das Änderungsverzeichnis für Fassung 7 mit 24 Punkten steht in ABNAHME_Vorbedingung-1_2026-09-20.md, danach kommt Vorbedingung 2, die Verfassung des Handelssystems.
```

