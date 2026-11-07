# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 022 von 054

- Einträge V0406 bis V0438. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0406 · 20.09.2026 01:52:36 CEST · Hermes-Zwischentext · Nachricht id 2879 · Sitzung `20260918_225920_3e614670` · 109 B

```text
Jetzt geht die Rechnung auf: 40 übernommen + 3 in Lauf 24 erzeugt = 43. Ich schreibe die Auflösung korrekt.
```

### V0407 · 20.09.2026 01:53:07 CEST · Hermes-Zwischentext · Nachricht id 2883 · Sitzung `20260918_225920_3e614670` · 80 B

```text
Jetzt N1 (Zuordnung berichtigen) und N6 (Adresse), dann der berichtigte Bericht.
```

### V0408 · 20.09.2026 01:53:24 CEST · Hermes-Zwischentext · Nachricht id 2887 · Sitzung `20260918_225920_3e614670` · 151 B

```text
Lauf 20 zeigt jetzt 4 statt 11 erzeugte Tests — die verschärfte Abfrage schließt dort Altbestand aus. Ich prüfe das, bevor es in den Bericht geht.
```

### V0409 · 20.09.2026 01:53:35 CEST · Hermes-Zwischentext · Nachricht id 2889 · Sitzung `20260918_225920_3e614670` · 197 B

```text
Bestätigt: 7 der 11 waren Altbestand aus Werk 18. Die korrigierte Zahl für Lauf 20 ist **4 erzeugte Tests, 3 Doppelungen = 75 %** — meine ursprünglichen 63,6 % waren ebenfalls falsch gezählt.
```

### V0410 · 20.09.2026 01:54:45 CEST · Hermes-Zwischentext · Nachricht id 2893 · Sitzung `20260918_225920_3e614670` · 66 B

```text
Jetzt der berichtigte Bericht mit N6 (Adressen in eigenen Zeilen).
```

### V0411 · 20.09.2026 01:54:59 CEST · Hermes-Zwischentext · Nachricht id 2895 · Sitzung `20260918_225920_3e614670` · 112 B

```text
Jetzt die berichtigten Zahlen auch im ursprünglichen BERICHT.md, sonst stehen zwei Wahrheiten im selben Ordner.
```

### V0412 · 20.09.2026 01:55:40 CEST · Hermes · Nachricht id 2901 · Sitzung `20260918_225920_3e614670` · 3207 B

```text
**Nachgang N1 bis N6 erledigt — 0 Modellaufrufe.** Die Prüfung hatte in allen sieben Befunden recht.

Nachgangsbericht:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG.md

Dateiliste (N6, jetzt abrufbar):

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN.txt

Ordnerprüfsumme:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER.txt

Prüfsumme (54 Dateien): `c5b53d54bf54be0cba4fac83dc3a09f83a004d94c2ddd6fac45a6e9e6c6f88eb`

**N1 — F1 trifft zu.** Größte Gruppe 8→1 und unbemerkte Doppelungen 31→0 standen bereits in Lauf 22, **ohne** die Ansage. Sie gehören dem Behauptungs-Schlüssel und der Anweisung. Bauteil A allein zuzurechnen: 10 von 27 abgewiesenen Ansagen, 18 von 65 „KEIN ANGRIFF" (vorher 0 von allen), Filtergüte.

**Dazu ein Fehler, den die Prüfung nicht gefunden hat:** Auch meine Zahl für Lauf 20 war falsch — 7 der 11 gezählten Tests waren übernommener Altbestand. Richtig: 4 erzeugte Tests, **75,0 %** statt 63,6 %. Dieselbe Fehlerklasse wie bei Lauf 24; ich hatte sie beim ersten Mal nur an einer Stelle korrigiert.

**N2 — 27 = 11 ausgeführt + 10 abgewiesen + 6 „KEIN ANGRIFF"**, geht auf. Die sechs Vermissten sind namentlich mit Protokollnummer benannt. Warum 11 Angriffe nur 2 Tests erzeugten: 1 bestätigt, 1 als Norm, **7 ohne Bestätigung** — ihr Test bestand am Kandidaten, fand also keinen Fehler.

**N3 — Maßstab erfüllt: Fehlalarm 0 von 10, Durchgerutscht 0.** Roter und grüner Eichfall aus dem echten Lauf, beide dieselbe Behauptung im selben Bereich: `#14533` neu → ausgeführt, `#14557` wiederholt → gesperrt.

**Auch hier ein eigener Messfehler, korrigiert:** Meine erste Fassung prüfte gegen den **Endstand** des Vorrats und meldete 2 Durchrutscher — der erzeugte Test trägt seinen eigenen Schlüssel, damit misst man sich selbst. Grundsatz 5. Gegen den Vorrat zum Ansagezeitpunkt: 0.

**Zusatzbefund:** 1 von 2 Tests wich von der **eigenen Ansage** ab (`aufnehmen|raises:ValueError` angesagt, `preis_fuer|GtE:zahl` geschrieben). Echte Lücke im Bauteil — Ansage und Ausführung werden nicht gegeneinander geprüft. Behebung ist Messgerätänderung, gehört nach Fassung 7, nicht in diesen Nachgang.

**N4 — aufgelöst.** 49 Einträge Werk 11 = 39 offen + 1 Norm + 6 im Werk + 3 gefunden; übernommen 40; Werk 21 hat 43 = 40 + 3 erzeugte. Die „48" waren Ankläger-Tests, nicht übernommene Einträge — drei verschiedene Mengen in meiner Meldung ohne Bezugsgröße.

**N5 — F6 trifft zu.** 3 von 4 gegen 1 von 5 bei gleichem Bestand belegt Streuung, keine Wirkung. Belegt ist nur: Vorlage 3 → 6 fremde Muster, und in allen drei Messungen danach ≥ 1 Verweis bei 0 erfundenen. Zur Zeile schlage ich (a) vor: umbenennen in „≥ 1 werkübergreifender Verweis bei gezeigtem Mindestanteil". Entscheidung liegt bei dir.

**Tor 2 Zeile 8 bleibt ungemessen** und steht für Tor 4. Der alte BERICHT.md trägt jetzt einen Berichtigungsvermerk, damit nicht zwei Wahrheiten im Ordner stehen.
```

### V0413 · 20.09.2026 02:01:47 CEST · Philipp · Nachricht id 2902 · Sitzung `20260918_225920_3e614670` · 8383 B

````text
[The user sent a text document: 'PRUEFUNG2_Vorbedingung-1_2026-09-20.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_cb2a4a165f94_PRUEFUNG2_Vorbedingung-1_2026-09-20.md]

[Content of PRUEFUNG2_Vorbedingung-1_2026-09-20.md]:
# Zweite Prüfung: Biotop Phase 4, Vorbedingung 1 — Nachgang

**Geprüft von:** Chat-Claude · **Gegenstand:** `NACHGANG.md`, `DATEIEN.txt`, `PRUEFSUMME-ORDNER.txt`, abgerufen 20.09.2026
**Wertung: noch nicht abgenommen.** Ein einziger Punkt fehlt — er kostet **0 Modellaufrufe**.

---

## 1. Prüfsumme — diesmal nachgerechnet, nicht gelesen

`DATEIEN.txt` wurde abgerufen, zeichengetreu nachgebaut und gehasht:

```
Soll (PRUEFSUMME-ORDNER.txt):  c5b53d54bf54be0cba4fac83dc3a09f83a004d94c2ddd6fac45a6e9e6c6f88eb
Ist  (selbst gerechnet):       c5b53d54bf54be0cba4fac83dc3a09f83a004d94c2ddd6fac45a6e9e6c6f88eb
Zeilen in DATEIEN.txt:         54  → stimmt mit der Angabe „54 Dateien"
```

**Bestätigt durch Ausführung.** F7 ist behoben, N6 wirkt.

Zwei Nebenergebnisse aus derselben Rechnung:

- **44 verschiedene Prüfsummen auf 54 Dateien.** Die einzige Dublette ist der Hash des leeren Strings (`e3b0c442…`, 11×). Es gibt also **keine zwei inhaltsgleichen Nutzdateien** im Ordner — keine versehentlichen Kopien.
- 10 der 11 `.err`-Dateien sind 0 Byte. Eine nicht. Daraus folgt Abschnitt 3.

---

## 2. Was der Nachgang richtig gemacht hat

| Punkt | Urteil |
|---|---|
| N1 Zuordnung | Richtig getrennt in S, W, A. Die Aufteilung ist schärfer als mein Befund — ich hatte zwei Bauteile unterschieden, es sind drei. |
| N2 Aufrechnung | 27 = 11 + 10 + 6, die sechs Vermissten mit Protokollnummer. Geht auf. |
| N3 Filtergüte | **Maßstab erfüllt: Fehlalarm 0 von 10, Durchgerutscht 0.** Roter und grüner Eichfall `#14533`/`#14557` — dieselbe Behauptung, einmal vor und einmal nach Aufnahme in den Vorrat. Das ist der beste Beleg des ganzen Laufs. |
| N3 Selbstkorrektur | Methodisch richtig: gegen den Endstand zu prüfen misst den Test an sich selbst. Der Vergleich gegen den Vorrat zum Ansagezeitpunkt ist die einzig richtige Ableitung. |
| N4 | Aufgelöst. 49 = 39 + 1 + 6 + 3 ✓, 43 = 40 + 3 ✓. Die Differenz war meine falsche Annahme, Norm-Umstufungen würden Einträge entfernen. Vorrat 25 → 26 durch Lauf 24 selbst. **Mein Befund F5 war in der Sache falsch, in der Sorge richtig: die Bezugsgröße fehlte.** |
| N5 | Ohne Beschönigung: 75 % gegen 20 % belegt Streuung, keine Wirkung. |
| Zusatzbefund | Die Ansage-Ausführung-Lücke hat Hermes selbst gefunden und gemeldet, obwohl sie sein eigenes Bauteil schwächt. Das ist der wertvollste Teil des Nachgangs. |

**Mein eigener Fehler:** Den Lauf-20-Befund habe ich übersehen. Ich hatte die Fehlerklasse benannt und Lauf 13 und 24 geprüft — aber nicht dieselbe Frage an Lauf 20 und 22 gestellt. Hermes hat sie gestellt. 63,6 % war falsch, richtig sind 75,0 % aus 4 erzeugten Tests.

---

## 3. Neuer Befund: ein Abbruch, der in keinem Bericht steht

Aus der Prüfsummenliste, ohne weiteren Abruf:

```
ausgaben/04g6-gen6.json   e3b0c442…   ← 0 Byte, leer
ausgaben/04g6-gen6.err    7f4610f5…   ← nicht leer
```

Bei **allen anderen** Generationen ist es umgekehrt: `.json` gefüllt, `.err` leer. Bei `04g6-gen6` ist das Muster genau invertiert.

**Generation 6 des Lauf-23-Fortsetzungslaufs ist gescheitert.** Sie hat kein Ergebnis geschrieben und eine Fehlerausgabe hinterlassen. Im Kassenblatt steht „Lauf 23, Generationen 1–5". Im Bericht steht sie gar nicht.

Warum das zählt:

1. Fassung 5 hält ausdrücklich fest, dass Abbrüche nicht vom Freigabe-Gate gesperrt werden — sie sind erlaubt. **Verschweigen ist nicht erlaubt.** Der Grundsatz lautet: laut scheitern, nie still.
2. **Lauf 23 ist die Grundlage von Bauteil B.** Er hat den Musterbestand von 4 auf 7 und die Vorlage auf 6 fremde Muster gebracht. Ist Generation 6 abgebrochen, ist offen, ob der Bestand zum Messzeitpunkt vollständig war.

Das ist keine Kleinigkeit im Zahlenwerk, sondern derselbe Grundsatz, für den das ganze Biotop gebaut wird.

---

## 4. Zwei Stellen, an denen die Belege die Aussage nicht tragen

### 4.1 N2 schließt nicht — 11 gegen 9

Der Abschnitt beginnt mit **11 ausgeführten Angriffen** und rechnet dann **9 Ankläger-Urteile** auf (1 bestätigt + 1 Norm + 7 ohne Bestätigung).

**Zwei ausgeführte Angriffe sind nicht aufgerechnet.** Dieselbe Fehlerklasse zum dritten Mal in diesem Lauf: eine Zahl wird genannt, die Aufrechnung zählt eine andere Menge.

### 4.2 N5 — Prosa nennt mehr Messungen, als die Tabelle zeigt

| | Prosa im Bericht | Belegtabelle |
|---|---|---|
| vor dem Bauteil | „0 von 4 in **sechs** aufeinanderfolgenden Mentor-Aufrufen (Läufe 16–22)" | **2** Zeilen (#12547, #13296) |
| nach dem Bauteil | „**3 von 4**, **2 von 5**, **1 von 5**" | **2** Zeilen (#14246, #14480) |

Die Messung **2 von 5** hat keine Protokollnummer und steht in keiner Tabelle. Die Wertung „mit 3 von 3 Messungen erfüllt" stützt sich auf eine Messung, die nicht belegt ist.

---

## 5. Entscheidungen — als meine gekennzeichnet

**V8 — Zeile Bauteil B: Weg (a), mit Auflage.** Umbenennen in „≥ 1 werkübergreifender Verweis bei gezeigtem Mindestanteil". Hermes' Begründung trägt: ein Zitierzwang erzeugt Scheinbegründungen. **Auflage:** Belegt ist allein die Vorlagenänderung 3 → 6 fremde Muster. Das Zitierverhalten des Mentors streut und wird **nicht** als Wirkung des Bauteils verbucht. Philipp kann das überstimmen.

**V9 — Die Ansage-Ausführung-Lücke ist kein „später"-Punkt, sondern Vorbedingung für Tor 4.** Hermes stellt sie korrekt nach Fassung 7 zurück und zitiert dabei richtig meinen Abschnitt 6. Aber: In Tor 4 soll Zeile 8 gemessen werden. Wenn der Ankläger von seiner eigenen Ansage abweicht — bei 1 von 2 Tests —, dann sperrt das Bauteil auf eine Behauptung, die mit dem geschriebenen Test nichts zu tun hat. Zeile 8 misst dann erneut nichts Belastbares. **Die Prüfung Ansage gegen Ausführung muss vor der Zeile-8-Messung stehen, nicht danach.**

---

## 6. Auflage N7 — 0 Modellaufrufe

**N7 — Den Abbruch offenlegen.** Inhalt von `ausgaben/04g6-gen6.err` in den Nachgangsbericht aufnehmen. Drei Fragen beantworten:

1. Woran ist Generation 6 gescheitert?
2. War der Musterbestand (7 Muster, Vorlage 6 fremde) zum Zeitpunkt der Bauteil-B-Messung **vollständig**, oder hat der Abbruch ihn abgeschnitten?
3. Warum erscheint der Abbruch weder im Bericht noch im Kassenblatt? Wenn das Meldeverhalten eine Lücke hat, gehört sie in Fassung 7.

**N8 — Die zwei fehlenden Angriffe.** 11 ausgeführt, 9 aufgerechnet. Die restlichen zwei mit Protokollnummer und Ausgang benennen.

**N9 — Die Messung „2 von 5".** Protokollnummer und Lauf nennen, oder die Aussage auf zwei belegte Messungen zurücknehmen.

> **Freigabetor:** Vorbedingung 1 ist abgenommen, sobald N7, N8 und N9 vorliegen. Alle drei kosten **0 Modellaufrufe**. Vorbedingung 2 startet danach.

---

## 7. Fassung 7 — was sich bis jetzt angesammelt hat

Damit nichts verloren geht. Die Fassung selbst wird geschrieben, wenn N7–N9 durch sind:

1. **Ansage gegen Ausführung prüfen** (V9 — Vorbedingung für Tor 4, nicht danach)
2. **Zeile Bauteil B umbenennen** (V8)
3. **Zeile 8 gilt als ungemessen**, solange der Nenner unter 20 erzeugten Tests liegt — Grenze hiermit vorab gesetzt
4. **Filtergüte als stehendes Maß für Sperrbauteile**: Fehlalarm und Durchgerutscht, gemessen an den Ansagen, nicht am Rest
5. **Jede Zahl im Bericht nennt ihre Bezugsgröße** — dreimal in einem einzigen Lauf gerissen (Lauf 20, Lauf 24, N2)
6. **Abbrüche erscheinen im Bericht und im Kassenblatt**, auch wenn sie folgenlos waren

---

## 8. Kurzprompt für den Telegram-Chat mit Hermes

> Prüfsumme `c5b53d54…` habe ich selbst nachgerechnet — sie stimmt, 54 Zeilen, keine zwei inhaltsgleichen Nutzdateien, N6 wirkt. Vorbedingung 1 ist trotzdem noch nicht abgenommen: In `ausgaben/04g6-gen6.json` stehen 0 Byte, während `04g6-gen6.err` gefüllt ist — Generation 6 des Lauf-23-Fortsetzungslaufs ist gescheitert und steht weder im Bericht noch im Kassenblatt, obwohl Lauf 23 die Grundlage von Bauteil B ist. Die drei Auflagen N7 bis N9 stehen in `PRUEFUNG2_Vorbedingung-1_2026-09-20.md`, kosten zusammen 0 Modellaufrufe, und Vorbedingung 2 startet, sobald sie vorliegen.
````

### V0414 · 20.09.2026 02:01:48 CEST · Philipp · Nachricht id 2903 · Sitzung `20260918_225920_3e614670` · 578 B

```text
Prüfsumme c5b53d54… habe ich selbst nachgerechnet — sie stimmt, 54 Zeilen, keine zwei inhaltsgleichen Nutzdateien, N6 wirkt. Vorbedingung 1 ist trotzdem noch nicht abgenommen: In ausgaben/04g6-gen6.json stehen 0 Byte, während 04g6-gen6.err gefüllt ist — Generation 6 des Lauf-23-Fortsetzungslaufs ist gescheitert und steht weder im Bericht noch im Kassenblatt, obwohl Lauf 23 die Grundlage von Bauteil B ist. Die drei Auflagen N7 bis N9 stehen in PRUEFUNG2_Vorbedingung-1_2026-09-20.md, kosten zusammen 0 Modellaufrufe, und Vorbedingung 2 startet, sobald sie vorliegen.
```

### V0415 · 20.09.2026 02:02:05 CEST · Hermes-Zwischentext · Nachricht id 2904 · Sitzung `20260918_225920_3e614670` · 77 B

```text
Der Abbruch-Befund sitzt. Ich sehe zuerst nach, was in der Fehlerdatei steht.
```

### V0416 · 20.09.2026 02:02:18 CEST · Hermes-Zwischentext · Nachricht id 2906 · Sitzung `20260918_225920_3e614670` · 183 B

```text
Kein Absturz: Der Lauf hat sich nach Generation 5 **gesättigt** und die Schleife brach sauber ab. Ich prüfe, ob das in der Datenbank steht und ob der Musterbestand vollständig ist.
```

### V0417 · 20.09.2026 02:03:06 CEST · Hermes-Zwischentext · Nachricht id 2908 · Sitzung `20260918_225920_3e614670` · 192 B

```text
Wichtig: **Generation 5 wurde angenommen und lieferte ihr Muster** — der Bestand war zum Messzeitpunkt vollständig. Jetzt N8 und N9: die zwei fehlenden Angriffe und die Messung „2 von 5".
```

### V0418 · 20.09.2026 02:03:30 CEST · Hermes-Zwischentext · Nachricht id 2912 · Sitzung `20260918_225920_3e614670` · 145 B

```text
Die zwei fehlenden Angriffe sind identifiziert: `#15143` und `#15162`. Ich prüfe, was mit ihnen geschah, statt drei Möglichkeiten aufzuzählen.
```

### V0419 · 20.09.2026 02:03:53 CEST · Hermes-Zwischentext · Nachricht id 2914 · Sitzung `20260918_225920_3e614670` · 169 B

```text
Gefunden: Beide Angriffe **liefen und erzeugten Urteile** (#15147, #15165) — mein Zuordnungsalgorithmus hat sie falsch gepaart, weil er Urteile der Reihe nach vergibt.
```

### V0420 · 20.09.2026 02:04:03 CEST · Hermes-Zwischentext · Nachricht id 2916 · Sitzung `20260918_225920_3e614670` · 67 B

```text
Die Aufrechnung „1+1+1+8 = 11" muss ich prüfen, nicht behaupten.
```

### V0421 · 20.09.2026 02:04:15 CEST · Hermes-Zwischentext · Nachricht id 2918 · Sitzung `20260918_225920_3e614670` · 123 B

```text
Neun Urteile, nicht elf — zwei ausgeführte Angriffe schrieben **kein** Urteil mit Angriffsabschnitt. Ich prüfe, welche.
```

### V0422 · 20.09.2026 02:04:28 CEST · Hermes-Zwischentext · Nachricht id 2920 · Sitzung `20260918_225920_3e614670` · 141 B

```text
Sauber: **11 Ansagen → 11 Angriffsaufrufe**, eins zu eins. Zwei davon schrieben kein Urteil mit Angriffsabschnitt — ich sehe nach, warum.
```

### V0423 · 20.09.2026 02:04:57 CEST · Hermes-Zwischentext · Nachricht id 2922 · Sitzung `20260918_225920_3e614670` · 206 B

```text
Jetzt ist es eindeutig: Drei Angriffe (#14662, #14691, #14705) laufen auf **ein** gemeinsames Urteil #14707 — mehrere Bereiche im Wirkungskreis desselben Kandidaten. Ich schreibe die geprüfte Erklärung.
```

### V0424 · 20.09.2026 02:05:39 CEST · Hermes-Zwischentext · Nachricht id 2926 · Sitzung `20260918_225920_3e614670` · 87 B

```text
Alle drei Auflagen beantwortet. Jetzt in den Nachgangsbericht aufnehmen und versiegeln.
```

### V0425 · 20.09.2026 02:05:54 CEST · Hermes-Zwischentext · Nachricht id 2928 · Sitzung `20260918_225920_3e614670` · 105 B

```text
Die Zahl „sechs Messungen" habe ich in der Ergänzung wieder ungenau geschrieben. Ich zähle sie exakt.
```

### V0426 · 20.09.2026 02:06:42 CEST · Hermes · Nachricht id 2934 · Sitzung `20260918_225920_3e614670` · 2866 B

```text
**N7, N8, N9 erledigt — 0 Modellaufrufe.**

Nachgangsbericht (beide Nachgänge):

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG.md

Dateiliste:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN.txt

Ordnerprüfsumme:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER.txt

Prüfsumme (55 Dateien): `54dc6b3fbe4585fb29ad2837c1cf8afa2a6abac043d811a1debfe363b3895ace`

**N7 — der Abbruch.** Inhalt der Datei: `ABBRUCH: Lauf 23 ist im Zustand gesaettigt, nicht bereit`. Generation 6 ist **nicht gescheitert und hat nie begonnen**: Nach Generation 5 meldete die Entropie Sättigung, der Läufer war aber auf 5–8 angesetzt; der Folgeaufruf traf auf einen beendeten Lauf und wurde vom Kern abgewiesen. In der Datenbank gibt es keine Generation 6. **Der Musterbestand war vollständig** — die angenommenen Generationen 1 und 5 haben ihre Muster geschrieben (2 + 1), Generation 5 war fertig verarbeitet, der abgewiesene Aufruf lag danach.

Warum er nirgends stand: Der Läufer schreibt die Meldung nur in `.err` und sein Log, der Kern protokolliert nur die Sättigung — und **ich habe die `.err`-Dateien nach dem Lauf nicht durchgesehen**. „Laut scheitern, nie still" gilt auch für folgenlose Abbrüche; gehört in Fassung 7.

**N8 — es fehlt kein Angriff.** 11 Ansagen → **11 Angriffsaufrufe**, eins zu eins nachgewiesen. Es gibt nur 9 Urteile, weil drei Angriffe (`#14662, #14691, #14705`) in **ein gemeinsames Urteil** `#14707` münden: Der Ankläger greift jeden Bereich im Wirkungskreis einzeln an, schreibt das Urteil aber je Kandidat. 11 − 2 = 9. Aufrechnung: 1 bestätigt + 1 Behebungsnachweis + 1 Norm + 6 ohne Bestätigung = 9.

**Mein Fehler war doppelt:** erst die unerklärte Differenz, dann eine **falsche erste Erklärung** in diesem Nachgang („zwei Angriffe ohne Urteil") — mein Zuordnungsskript vergab Urteile der Reihe nach. Erst der Abgleich Ansage → Modellaufruf → Urteil zeigt die Sache.

**N9 — „2 von 5" ist `#13339`, Lauf 23**, aus dem Phase-3-Nachlauf, also einem anderen Ordner. Beim exakten Nachzählen fand ich eine **dritte ungenaue Zahl**: Meine Prosa sprach von „sechs Mentor-Aufrufen ohne Verweis" — es sind **neun** (`#7565` bis `#13296`). Dieselbe Ursache wie zweimal zuvor: aus dem Gedächtnis gezählt statt aus dem Protokoll.

**V8 und V9 angenommen.** V9 ist zwingend: Weicht der Ankläger bei 1 von 2 Tests von seiner Ansage ab, sperrt das Bauteil auf eine Behauptung, die mit dem geschriebenen Test nichts zu tun hat — eine Zeile-8-Messung darauf wäre wertlos. Die Prüfung Ansage gegen Ausführung gehört vor Tor 4.

Kosten unverändert: 0,91 € von 3 €.
```

### V0427 · 20.09.2026 02:25:43 CEST · Philipp · Nachricht id 2935 · Sitzung `20260918_225920_3e614670` · 8687 B

````text
[The user sent a text document: 'PRUEFUNG3_Vorbedingung-1_2026-09-20.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_01d32651bd5b_PRUEFUNG3_Vorbedingung-1_2026-09-20.md]

[Content of PRUEFUNG3_Vorbedingung-1_2026-09-20.md]:
# Dritte Prüfung: Biotop Phase 4, Vorbedingung 1 — N7 bis N9

**Geprüft von:** Chat-Claude · **Abruf:** 20.09.2026, alle vier Adressen
**Wertung: nicht abgenommen** — diesmal nicht wegen der Inhalte, sondern weil sie an der Abholadresse nicht liegen.

---

## 1. Der harte Befund, bestätigt durch Ausführung

Gemeldet wurde: 55 Dateien, Prüfsumme `54dc6b3fbe4585fb29ad2837c1cf8afa2a6abac043d811a1debfe363b3895ace`, Nachgangsbericht mit beiden Nachgängen.

Abgerufen und nachgerechnet wurde:

```
DATEIEN.txt jetzt vs. DATEIEN.txt beim letzten Abruf:  IDENTISCH, Byte für Byte
Zeilen:                                                 54   (nicht 55)
SHA-256 des jetzigen Abrufs:  c5b53d54bf54be0cba4fac83dc3a09f83a004d94c2ddd6fac45a6e9e6c6f88eb
gemeldet:                     54dc6b3fbe4585fb29ad2837c1cf8afa2a6abac043d811a1debfe363b3895ace
Belegdatei zu N7/N8/N9 in der Liste:                    0 Treffer
```

Dazu:

- `PRUEFSUMME-ORDNER.txt` nennt weiterhin **54 Dateien** und `c5b53d54…` — nicht die gemeldete Summe.
- `NACHGANG.md` trägt weiterhin den Titel **„Nachgang N1 bis N6"**. Kein N7, kein N8, kein N9. Sein Hash steht unverändert bei `1c2f2146…`.
- N2 steht dort noch in der **alten, inzwischen selbst widerrufenen** Fassung („7 Angriffe brachten keine Bestätigung"). N5 nennt weiter „sechs Mentor-Aufrufe" statt neun und listet `#13339` nicht.

Alle vier ausgelieferten Dateien sind untereinander stimmig — auf dem **alten** Stand. Die Arbeit aus N7 bis N9 existiert nur in der Chatnachricht.

**Zwei Erklärungen sind möglich:** die Dateien wurden nicht hochgeladen, oder eine Zwischenspeicherung liefert durchgängig den alten Stand. Ich kann das von außen nicht unterscheiden — beides ist aber derselbe Mangel gegenüber der stehenden Regel: Philipp und ich müssen das Ergebnis online nachsehen können, **ohne auf die Meldung angewiesen zu sein**. Genau das geht gerade nicht.

Das ist kein Verschieben der Grenze. Mein Freigabetor lautete: „abgenommen, sobald N7, N8 und N9 **vorliegen**." Vorliegen heißt an der Abholadresse.

---

## 2. Mein eigener Fehler — N7 korrigiert mich zu Recht

Ich hatte geschrieben: **„Generation 6 ist gescheitert."** Das war eine Überlesung.

Die Daten trugen nur: `04g6-gen6.json` hat 0 Byte, `04g6-gen6.err` ist gefüllt — also *ein Aufruf hinterließ eine Meldung und kein Ergebnis*. Daraus „eine Generation ist gescheitert" zu machen, war Erwartetes statt Abgelesenes. Richtig ist: Generation 6 hat nie begonnen, der Lauf war bei Sättigung schon beendet, der Folgeaufruf wurde abgewiesen.

Der Befund war richtig, meine Etikette darauf war falsch.

**Was ich aus meinen Daten bestätigen kann:** In der Dateiliste gibt es für Lauf 23 genau zwei Freigabedateien — `02g1-gen1-freigabe.json` und `04g5-gen5-freigabe.json`. Das deckt sich exakt mit „Generationen 1 und 5 angenommen" und mit dem Musterzuwachs 2 + 1 = 3, der den Vorrat von 4 auf 7 bringt. **N7 ist damit aus vorhandenen Belegen gestützt.**

Nicht bestätigen konnte ich den zitierten Dateiinhalt: Der Satz allein ergibt weder mit noch ohne Zeilenumbruch den Hash `7f4610f5…`. Das widerlegt nichts — die Datei enthält vermutlich noch einen Zeitstempel. Prüfbar wird es, sobald der Beleg im Ordner liegt.

---

## 3. N8 schließt die alte Lücke und öffnet eine neue

Die Auflösung trägt: 11 Ansagen → 11 Angriffsaufrufe, drei davon (`#14662`, `#14691`, `#14705`) münden in ein gemeinsames Urteil `#14707`. 11 − 2 = 9 Urteile. Sauber.

Die neue Aufrechnung lautet aber: **1 bestätigt + 1 Behebungsnachweis + 1 Norm + 6 ohne Bestätigung**. Damit sind es **drei** erzeugte Einträge, nicht zwei.

Das deckt sich mit N4, wo bereits stand: *„Werk 21: 43 = 40 übernommene + **3 in Lauf 24 erzeugte**"*. Aber:

- Die Zeile-8-Tabelle rechnet mit **2 erzeugten Tests**.
- N3 misst Durchgerutscht ausdrücklich über **„beide in Lauf 24 erzeugten Tests"**.
- Der Zusatzbefund zur Ansage-Abweichung nennt **„1 von 2"**.

**Wenn es drei Einträge sind, wurde mein Maßstab über zwei von drei gemessen.** Das betrifft Durchgerutscht = 0 unmittelbar — und Durchgerutscht war die Hälfte des Maßstabs, an dem Vorbedingung 1 hängt.

Das ist keine neue Forderung von mir. Es ist die Folge von N8s eigener Berichtigung.

---

## 4. N9 — der Beleg liegt außerhalb des versiegelten Ordners

`#13339` ist benannt, liegt aber im Phase-3-Nachlaufordner. Die Ordnerprüfsumme deckt ihn nicht ab. Eine der drei Messungen, auf die sich die Wertung von Bauteil B stützt, ist damit nicht Teil des versiegelten Belegs.

Die Selbstberichtigung „sechs Mentor-Aufrufe → neun" ist richtig und gehört in `NACHGANG.md`, wo bis jetzt noch sechs steht.

---

## 5. Das Muster, das jetzt zählbar ist

Aus dem Gedächtnis gezählt statt aus dem Protokoll — **fünfmal in einer einzigen Vorbedingung**:

| # | Stelle | falsch | richtig | gefunden von |
|---|---|---|---|---|
| 1 | Lauf 24, erzeugte Tests | 41 | 2 | Hermes |
| 2 | Lauf 20, erzeugte Tests | 11 | 4 | Hermes |
| 3 | N3, Durchgerutscht | 2 | 0 | Hermes |
| 4 | N8, erste Erklärung | „2 Angriffe ohne Urteil" | Sammelurteil | Hermes |
| 5 | N5, Mentor-Aufrufe | 6 | 9 | Hermes |

Alle fünf hat er selbst gefunden. Das spricht für die Nachprüfung und **gegen den ersten Durchgang**. Die Regel für Fassung 7 ist damit schärfer zu fassen als „Bezugsgröße nennen": **Keine Zahl geht in einen Bericht, die nicht aus einer Protokollabfrage stammt. Erinnerung ist keine Quelle.**

---

## 6. Auflagen

**A — Ablieferung.** N7 bis N9 an die Abholadresse bringen: `NACHGANG.md` erweitern, Belegdatei beilegen, `DATEIEN.txt` und `PRUEFSUMME-ORDNER.txt` neu schreiben. Die gemeldete Prüfsumme muss die des **ausgelieferten** Ordners sein. Dabei N2 und N5 im Bericht auf den berichtigten Stand bringen, damit nicht zwei Wahrheiten im Ordner stehen.

**N10 — Zwei oder drei?** Wie viele Einträge hat Lauf 24 erzeugt, und welche tragen einen Behauptungsschlüssel? Trägt der Behebungsnachweis einen, ist Durchgerutscht über **alle drei** neu zu messen. Trägt er keinen, ist das mit Begründung festzuhalten und die Zeile-8-Bezugsgröße bleibt 2.

**N11 — `#13339`.** In den Ordner kopieren oder die vollständige Fremdadresse in `NACHGANG.md` nennen, sodass die Messung von außen prüfbar ist.

> **Freigabetor, unverändert im Maßstab:** Vorbedingung 1 ist abgenommen, wenn der Ordner N7 bis N9 trägt, die gemeldete Prüfsumme zum ausgelieferten Ordner passt, und N10 beantwortet ist. Kosten: **0 Modellaufrufe**, sofern N10 „kein Schlüssel" ergibt. Ergibt es „Schlüssel", ist die Nachmessung ebenfalls eine Protokollabfrage, also weiterhin 0 Aufrufe.

---

## 7. Fassung 7 — Stand der Sammlung

1. Ansage gegen Ausführung prüfen (V9, Vorbedingung für Tor 4)
2. Zeile Bauteil B umbenennen (V8)
3. Zeile 8 gilt als ungemessen unterhalb von 20 erzeugten Tests
4. Filtergüte als stehendes Maß für Sperrbauteile
5. **Keine Zahl aus dem Gedächtnis — jede Zahl kommt aus einer Protokollabfrage** (fünf Vorfälle, Abschnitt 5)
6. Abbrüche und abgewiesene Aufrufe erscheinen im Bericht und im Kassenblatt
7. `.err`-Dateien werden nach jedem Lauf durchgesehen (aus N7)
8. **Melden und Abliefern sind ein Vorgang:** erst hochladen, dann Dateiliste und Prüfsumme neu schreiben, dann melden — die gemeldete Summe ist die des ausgelieferten Ordners

---

## 8. Kurzprompt für den Telegram-Chat mit Hermes

> N7 bis N9 liegen nicht an der Abholadresse: `DATEIEN.txt` ist Byte für Byte dieselbe wie beim letzten Abruf, 54 Zeilen statt 55, Prüfsumme `c5b53d54…` statt der gemeldeten `54dc6b3f…`, und `NACHGANG.md` trägt weiter den Titel „Nachgang N1 bis N6" ohne N7, N8, N9 — bitte prüfen, ob der Upload durchlief, und danach Dateiliste und Ordnerprüfsumme neu schreiben, damit die gemeldete Summe die des ausgelieferten Ordners ist. Inhaltlich ist N7 aus den vorhandenen Belegen gestützt (nur zwei Freigabedateien in Lauf 23, Generationen 1 und 5), und mein Befund „Generation 6 ist gescheitert" war meine Überlesung — richtig ist: nie begonnen, Aufruf nach Sättigung abgewiesen. Offen bleibt N10: N8 rechnet jetzt 1 bestätigt + 1 Behebungsnachweis + 1 Norm, das sind drei erzeugte Einträge, während Zeile 8 mit zwei rechnet und Durchgerutscht über zwei gemessen wurde — alles Weitere in `PRUEFUNG3_Vorbedingung-1_2026-09-20.md`.
````

### V0428 · 20.09.2026 02:26:07 CEST · Hermes-Zwischentext · Nachricht id 2936 · Sitzung `20260918_225920_3e614670` · 194 B

```text
Der Ablieferungsbefund ist ernst. Ich prüfe zuerst, was tatsächlich auf der Platte liegt — die Datei könnte geschrieben, aber die Prüfsumme über einen anderen Stand gerechnet worden sein.
```

### V0429 · 20.09.2026 02:26:18 CEST · Hermes-Zwischentext · Nachricht id 2938 · Sitzung `20260918_225920_3e614670` · 166 B

```text
Die Dateien liegen korrekt auf der Platte — 55 Zeilen, Prüfsumme stimmt, N7–N9 vorhanden. Also liefert die Auslieferung einen alten Stand. Ich prüfe über HTTP.
```

### V0430 · 20.09.2026 02:26:30 CEST · Hermes-Zwischentext · Nachricht id 2940 · Sitzung `20260918_225920_3e614670` · 235 B

```text
Der Server liefert den **aktuellen** Stand: 55 Zeilen, `54dc6b3f…`, `no-store`. Die Prüfung sah also eine zwischengespeicherte Kopie — aber ein echter Mangel bleibt: Der **Titel** sagt „N1 bis N6", obwohl N7–N9 enthalten sind.
```

### V0431 · 20.09.2026 02:27:03 CEST · Hermes-Zwischentext · Nachricht id 2942 · Sitzung `20260918_225920_3e614670` · 163 B

```text
Bestätigt: zwei Wahrheiten im selben Dokument. Zeile 173 sagt „sechs", Zeile 284 berichtigt auf „neun". Zuerst N10 — die Frage, ob zwei oder drei Einträge.
```

### V0432 · 20.09.2026 02:27:27 CEST · Hermes-Zwischentext · Nachricht id 2946 · Sitzung `20260918_225920_3e614670` · 199 B

```text
Zwei Widersprüche in meiner eigenen Ausgabe: `aegis_k2500_preise` gilt jetzt als durchgerutscht (vorher nein), und der Schlusssatz behauptet „erfüllt" bei Ergebnis 2. Ich prüfe den Vorrat exakt.
```

### V0433 · 20.09.2026 02:27:50 CEST · Hermes-Zwischentext · Nachricht id 2948 · Sitzung `20260918_225920_3e614670` · 208 B

```text
Jetzt ist die Lage eindeutig, und sie geht gegen mein Bauteil: **Beide Behauptungen standen im Vorrat**, wurden aber nie angesagt — die Tests entstanden aus Angriffen, die etwas anderes angekündigt hatten.
```

### V0434 · 20.09.2026 02:28:19 CEST · Hermes-Zwischentext · Nachricht id 2952 · Sitzung `20260918_225920_3e614670` · 110 B

```text
Jetzt Auflage A: Bericht auf einen widerspruchsfreien Stand bringen, Titel korrigieren, N10 und N11 aufnehmen.
```

### V0435 · 20.09.2026 02:29:07 CEST · Hermes-Zwischentext · Nachricht id 2956 · Sitzung `20260918_225920_3e614670` · 102 B

```text
Die kopierte Datei hat Rechte `640` — über HTTP nicht lesbar. Ich korrigiere das und versiegle neu.
```

### V0436 · 20.09.2026 02:29:49 CEST · Hermes · Nachricht id 2962 · Sitzung `20260918_225920_3e614670` · 2565 B

```text
**Vorbedingung 1 ist nicht erfüllt — und zwar in der Sache, nicht nur in der Ablieferung. Ich beantrage keine Abnahme.**

Nachgangsbericht (alle drei Nachgänge, Titel jetzt „N1 bis N11"):

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/NACHGANG.md

Dateiliste:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN.txt

Ordnerprüfsumme:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER.txt

Prüfsumme (57 Dateien): `6060c93c49f32f9918f6e3ea991784d5148d345dbdce257d32572d70b456a81f`
Auslieferung gegen Platte geprüft: alle drei Dateien **byteidentisch**, Header `no-store`.

**N10 — die Antwort geht gegen mein Bauteil.** Lauf 24 erzeugte **3 Einträge: 2 Funde + 1 Norm-Eintrag**. Für Zeile 8 bleibt die Bezugsgröße 2 (ein Norm-Eintrag ist kein erzeugter Fund). Aber **Durchgerutscht ist 2, nicht 0** — der Maßstab ist gerissen.

Beide Behauptungen standen im übernommenen Vorrat, und für **keine gab es eine Ansage**: `aegis_k2500_preise` (`preis_fuer|GtE:zahl`) entstand aus einem Angriff, der `aufnehmen|raises:ValueError` angekündigt hatte; `norm_k2458_lager` ohne Ansage dieser Behauptung.

**Meine Messung in N3 war zu eng gefasst:** Ich prüfte nur, ob ein Test die *eigene* Ansage wiederholt, und übersah den Fall, dass er eine *andere vorhandene* Behauptung wiederholt. Das ist der sechste Zählfehler in dieser Vorbedingung — und der erste, der das Ergebnis umdreht.

**Was das Bauteil wirklich leistet:** Es sperrt zuverlässig, *was angesagt wird* (Fehlalarm 0 von 10), aber nicht, *was geschrieben wird*. Damit ist V9 nicht nur Vorbedingung für Tor 4, sondern die Behebung genau dieses Befunds.

**N11 — `#13339` liegt jetzt im Ordner** (`ausgaben/20-fremdbeleg-…`, HTTP 200), dazu die Fremdadresse im Bericht.

**Auflage A:** Auf Platte und über HTTP lagen die N7–N9-Dateien korrekt; ich kann den gemeldeten alten Stand nicht reproduzieren — vermutlich ein Zwischenspeicher auf dem Abrufweg. **Ein echter Mangel lag aber bei mir:** Der Titel sagte „N1 bis N6", obwohl N7–N9 enthalten waren. Berichtigt. N2 und N5 tragen jetzt Berichtigungsvermerke mit Verweis auf den maßgeblichen Abschnitt.

Nächster Schritt: V9 bauen (Ansage gegen Ausführung prüfen), dann Filtergüte neu messen. Das ist eine Messgerätänderung, also ein neuer Lauf. Kosten bisher unverändert 0,91 € von 3 €.
```

### V0437 · 20.09.2026 02:29:50 CEST · Philipp · Nachricht id 2963 · Sitzung `20260918_225920_3e614670` · 935 B

```text
N7 bis N9 liegen nicht an der Abholadresse: DATEIEN.txt ist Byte für Byte dieselbe wie beim letzten Abruf, 54 Zeilen statt 55, Prüfsumme c5b53d54… statt der gemeldeten 54dc6b3f…, und NACHGANG.md trägt weiter den Titel „Nachgang N1 bis N6" ohne N7, N8, N9 — bitte prüfen, ob der Upload durchlief, und danach Dateiliste und Ordnerprüfsumme neu schreiben, damit die gemeldete Summe die des ausgelieferten Ordners ist. Inhaltlich ist N7 aus den vorhandenen Belegen gestützt (nur zwei Freigabedateien in Lauf 23, Generationen 1 und 5), und mein Befund „Generation 6 ist gescheitert" war meine Überlesung — richtig ist: nie begonnen, Aufruf nach Sättigung abgewiesen. Offen bleibt N10: N8 rechnet jetzt 1 bestätigt + 1 Behebungsnachweis + 1 Norm, das sind drei erzeugte Einträge, während Zeile 8 mit zwei rechnet und Durchgerutscht über zwei gemessen wurde — alles Weitere in PRUEFUNG3_Vorbedingung-1_2026-09-20.md.
```

### V0438 · 20.09.2026 02:30:08 CEST · Hermes-Zwischentext · Nachricht id 2964 · Sitzung `20260918_225920_3e614670` · 160 B

```text
Die Nachricht ist der Kurzprompt aus Prüfung 3 — N10 und N11 habe ich inzwischen beantwortet. Ich prüfe die Auslieferung erneut, diesmal mit Cache-Umgehung.
```

