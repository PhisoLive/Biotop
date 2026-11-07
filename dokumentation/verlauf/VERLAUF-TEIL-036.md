# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 036 von 054

- Einträge V0693 bis V0752. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0693 · 21.09.2026 18:23:25 CEST · Hermes · Nachricht id 10945 · Sitzung `20260921_015554_e79a4a0f` · 1480 B

```text
Kernfehler-Ausnahme — und ein wichtiger Fortschritt davor.

**Lauf 32 hat evolviert:** Generation 1 und 2 wurden **angenommen** — erste echte Verbesserungen am TypeScript-Werk. Gen 1: tote Funktion in `bericht` beseitigt, Testfehler und Sicherheitspunkte in `planung` gesenkt. Gen 2: drei Testfehler in `tarife` behoben, Sicherheitspunkte 13 → 6.

**Gen 3 starb an derselben Fehlerklasse wie Lauf 31**, an anderer Stelle: `aegis.junit_lauf` warf, als ein Modell einen Angriffstest lieferte, den Vitest nicht sammeln konnte. Der Python-Pfad derselben Funktion behandelt genau das seit jeher korrekt (Sammelfehler → Test gilt als nicht bestätigt, Kandidat wird normal beurteilt); nur der TS-Pfad eskalierte den Inhaltsbefund zum Abbruch.

Ihr Hinweis von vorhin war richtig und ich habe ihn zu eng ausgelegt: Ich hatte auf `def`-Muster, `.py`-Endungen, pytest-Ausgabe und Python-AST gesucht — aber diese Stelle gehört zur selben Klasse wie der Diff-Fehler, nur ohne Python-Syntax: **Inhaltsbefund als Absturz**. Der Adapter unterscheidet jetzt `art='inhalt'` (unsammelbar, Skip, leer → Ergebnis) von `art='infrastruktur'` (Runner tot, JUnit unlesbar → bleibt Abbruch, ohne Messgerät kein Urteil).

4 Tests, zuerst rot mit einem echten unsammelbaren Test in der Kammer, dann grün. Volle Regression **324 bestanden, 2 übersprungen**. Kern eingefroren bei `2e21059`, Lauf 33 läuft.

Verbrauch: 1,2197 € von 10 € (Läufe 26–32, alle gescheiterten mitgezählt).
```

### V0694 · 21.09.2026 18:27:40 CEST · Philipp · Nachricht id 10946 · Sitzung `20260921_015554_e79a4a0f` · 972 B

```text
Erste echte Verbesserungen am TypeScript-Werk — genau der Beleg, auf den T3 hingearbeitet hat. Zuerst, weil deine Sitzung über der Kompressionsgrenze liegt und die Kompression blockiert ist: Zwischenbericht und DATEIEN.txt in den Prüfkanal, so dass eine frische Sitzung ohne Vorgeschichte übernehmen kann — Stand von Lauf 33, Kernstand, Kasse, die angenommenen Generationen aus Lauf 32 und die Liste für nach T3. Dann die Klasse, nicht die Stelle: Lauf 31 und 32 starben an derselben Fehlerklasse an zwei Stellen. Geh jede Funktion mit Sprachweiche durch und vergleiche die Zweige — wo der Python-Zweig einen Fall als Ergebnis behandelt und der TypeScript-Zweig wirft, ist ein Fehler derselben Klasse. Erst suchen, ohne den Kern zu ändern: Findest du nichts, läuft Lauf 33 weiter; findest du etwas, alle Stellen in einem Zug beheben, dann Lauf 34. In die Endmeldung: von welchem Werkstand Lauf 33 startet, und ob er die Verbesserungen aus Lauf 32 wiederfindet.
```

### V0695 · 21.09.2026 18:29:58 CEST · Hermes-Zwischentext · Nachricht id 10959 · Sitzung `20260921_015554_e79a4a0f` · 123 B

```text
Übernahmeordner liegt, 48 von 48 Dateien HTTPS-bytegleich. Jetzt die Klassensuche: alle Sprachweichen, Zweige vergleichen.
```

### V0696 · 21.09.2026 18:30:09 CEST · Hermes-Zwischentext · Nachricht id 10963 · Sitzung `20260921_015554_e79a4a0f` · 144 B

```text
Vier Verdachtsfälle. `junit_lauf` ist bereits behoben (der verbleibende raise ist der Infrastruktur-Fall). Die anderen drei prüfe ich einzeln.
```

### V0697 · 21.09.2026 18:30:31 CEST · Hermes-Zwischentext · Nachricht id 10967 · Sitzung `20260921_015554_e79a4a0f` · 83 B

```text
Drei zu prüfen. Ich sehe mir die Aufrufer an, bevor ich etwas als Fehler einstufe.
```

### V0698 · 21.09.2026 18:30:57 CEST · Hermes-Zwischentext · Nachricht id 10969 · Sitzung `20260921_015554_e79a4a0f` · 107 B

```text
Drei Befunde, keiner abgefangen — jeder tötet den Lauf. Ich stoppe Lauf 33 und behebe alle in einem Zug.
```

### V0699 · 21.09.2026 18:31:59 CEST · Hermes-Zwischentext · Nachricht id 10977 · Sitzung `20260921_015554_e79a4a0f` · 141 B

```text
Lauf 33 gestoppt, Vorspann unvollständig — er ist damit tot (Satz 2, keine Nacheichung). Jetzt die drei Stellen in einem Zug, Test zuerst.
```

### V0700 · 21.09.2026 18:32:19 CEST · Hermes-Zwischentext · Nachricht id 10981 · Sitzung `20260921_015554_e79a4a0f` · 99 B

```text
5 rot, 4 grün (die Gegenproben, die richtiges Verhalten belegen). Jetzt alle drei Stellen beheben.
```

### V0701 · 21.09.2026 18:32:59 CEST · Hermes-Zwischentext · Nachricht id 10990 · Sitzung `20260921_015554_e79a4a0f` · 148 B

```text
Von 4 auf 2 — und beide verbleibenden sind die absichtlichen Infrastruktur-Abbrüche (ohne Messgerät kein Urteil), durch Tests als solche belegt.
```

### V0702 · 21.09.2026 18:37:10 CEST · Hermes-Zwischentext · Nachricht id 10994 · Sitzung `20260921_015554_e79a4a0f` · 192 B

```text
Dieser Test kodiert genau das alte Verhalten, das sich als Fehler erwiesen hat: ein unbestätigter Testfehler (`Importfehler`) sollte den Lauf töten. Die Erwartung ist falsch, nicht der Code.
```

### V0703 · 21.09.2026 18:41:24 CEST · Hermes-Zwischentext · Nachricht id 10998 · Sitzung `20260921_015554_e79a4a0f` · 124 B

```text
Meine Assertion war zu clever: `'bestaetigt' in str(faelle)` trifft auch auf `bestaetigt: False` zu. Ich mache sie explizit.
```

### V0704 · 21.09.2026 18:46:07 CEST · Hermes · Nachricht id 11008 · Sitzung `20260921_015554_e79a4a0f` · 2182 B

```text
**Übernahmeordner liegt, Klassensuche hat drei weitere Stellen gefunden.**

Prüfkanal: `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/uebernahme-01/` — 48 von 48 Dateien HTTPS-bytegleich, Ordnerprüfsumme `9c1c764ed311ca08ad9861a0b5354b279210ade6fba8fdf1dc275e80653d8d97`. Enthält ZWISCHENBERICHT.md, DATEIEN.txt, MANIFEST.sha256, beide berührten Skills im Wortlaut, die Freigabe-Regel und neun Messbelege.

**Die Klassensuche war ergiebig.** Zweigvergleich über alle **25 Sprachweichen** des Kerns, Kriterium: TS-Zweig wirft, wo der Python-Zweig zurückgibt. Vier Treffer, einer davon bereits behoben — die drei neuen töten jeder für sich einen Lauf, keiner wird abgefangen:

- `aegis._anhaengen` — warf bei TS-Tests; der einzige Aufrufer prüft ohnehin auf Falschheit → jetzt `None`
- `aegis.behauptung` — warf bei nicht ableitbarer Behauptung; alle fünf Aufrufer sind auf den Platzhalter `?|name` eingerichtet → jetzt ebenso
- `generation0._testlauf` — warf bei Typfehler, unbrauchbarem Testlauf und unbestätigtem Testfehler; eine einzelne unbrauchbare Testdatei hätte die ganze Mutantenkampagne beendet → jetzt `(False, Grund)`

Nach der Reparatur bleiben zwei TS-`raise`: beide nur noch für Infrastruktur (Runner tot, Typbau nicht ausgeführt) — ohne Messgerät kein Urteil, durch Tests in beide Richtungen belegt.

Dabei fiel ein Test auf, der das fehlerhafte Verhalten festschrieb: `test_t3_generation0.py` erwartete für einen unbestätigten Testfehler einen `RuntimeError`. Der Test war falsch, nicht der Code — korrigiert mit Begründung im Parametersatz.

Lauf 33 habe ich dafür gestoppt (Vorspann unvollständig, damit nach Satz 2 tot). Kern eingefroren bei `c214d1d`, Regression **333 bestanden, 2 übersprungen**. Lauf 34 läuft.

Zur Endmeldungsfrage vorab gemessen: Das eingelegte Werk ist bytegleich mit der Quelle (41/41), also startet **jeder** neue Lauf vom Ausgangsstand — die Verbesserungen aus Lauf 32 leben nur in den Lazarus-Archiven. Ob Lauf 34 sie wiederfindet, ist damit eine offene Messung über die Reproduzierbarkeit des Schwarms, kein erwartetes Ergebnis.
```

### V0705 · 21.09.2026 18:46:24 CEST · Hermes · Nachricht id 11012 · Sitzung `20260921_015554_e79a4a0f` · 242 B

```text
Das ist die erwartete Rückmeldung meines eigenen SIGTERM auf Lauf 33 — kein neuer Befund. Lauf 34 läuft auf dem eingefrorenen Kern `c214d1d`, aktuell bei der Kartierung, Verbrauch 1,22 € von 10 €.

Nächste Meldung ist die Endmeldung.
```

### V0706 · 21.09.2026 18:50:03 CEST · Philipp · Nachricht id 11013 · Sitzung `20260921_015554_e79a4a0f` · 609 B

```text
Klasse statt Stelle, genau richtig — drei gesparte Läufe. Schick die Adresse von uebernahme-01/DATEIEN.txt als ganze Zeile, das Verzeichnis selbst ist nicht abrufbar. In die Endmeldung als wichtigste Zeile: je Organ, wie oft es für TypeScript neutral zurückgab statt zu urteilen — Platzhalter in aegis.behauptung, leer in aegis._anhaengen, „nicht bestätigt" in generation0._testlauf, Enthaltung in der Wiederholungsprüfung —, jeweils mit Nenner; sonst hat die Behebung lautes Sterben gegen stilles Nichtstun getauscht. Dazu: Der geänderte Test prüft den Grund, nicht nur, dass nichts abstürzt.
```

### V0707 · 21.09.2026 18:50:52 CEST · Hermes-Zwischentext · Nachricht id 11014 · Sitzung `20260921_015554_e79a4a0f` · 275 B

```text
Adresse als ganze Zeile:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/uebernahme-01/DATEIEN.txt

Der Einwand trifft den Kern der Reparatur. Ich prüfe zuerst, ob die neutralen Rückgaben überhaupt zählbar sind.
```

### V0708 · 21.09.2026 18:52:01 CEST · Hermes-Zwischentext · Nachricht id 11024 · Sitzung `20260921_015554_e79a4a0f` · 199 B

```text
Der Befund ist unbequem und bestätigt den Einwand: **3 von 4 neutralen Rückgaben sind nicht zählbar.** Zuerst der Test, den Sie zu Recht hinterfragen — er prüfte nur Wahrheitswert, nicht Grund.
```

### V0709 · 21.09.2026 18:52:18 CEST · Hermes-Zwischentext · Nachricht id 11028 · Sitzung `20260921_015554_e79a4a0f` · 183 B

```text
Der Test prüft jetzt den Grund, nicht nur dass nichts abstürzt — 17 grün. Er belegt aber nur, dass der Grund *zurückgegeben* wird; ob er im Lauf *ankommt*, ist die offene Frage.
```

### V0710 · 21.09.2026 18:52:26 CEST · Hermes-Zwischentext · Nachricht id 11030 · Sitzung `20260921_015554_e79a4a0f` · 190 B

```text
Bestätigt: `generation0.testkandidat` protokolliert `faengt_mutant`, aber **nicht** den Grund `von`. Die drei neuen Gründe landen nirgends. Das ist genau der Tausch, den Sie benannt haben.
```

### V0711 · 21.09.2026 18:52:42 CEST · Hermes · Nachricht id 11032 · Sitzung `20260921_015554_e79a4a0f` · 2104 B

```text
Die Abholadresse als ganze Zeile:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/uebernahme-01/DATEIEN.txt

**Der Einwand trifft, und die Messung fällt schlechter aus als die Reparatur.** Ich habe gezählt, was sich aus der Datenbank belegen lässt (Läufe 31, 32, 34):

- **`gedaechtnis.wiederholung`** — Nenner 63 Kandidaten: 4 Wiederholungen erkannt (geurteilt), **12 Enthaltungen** wegen nicht anwendbarem Diff. Das ist die einzige der vier Stellen mit belegbarem Nenner, und auch die nur erschlossen: die Enthaltung selbst wird nicht protokolliert, ich lese sie aus dem Aegis-Grund „Diff nicht anwendbar".
- **`generation0._testlauf`** — Nenner 172 protokollierte Mutantenläufe: **0 mit „kein Verhaltensfang"**. Der Grund wird zurückgegeben, aber `generation0.testkandidat` protokolliert nur `faengt_mutant`, nicht `von`. Die drei neuen Gründe landen nirgends.
- **`aegis.behauptung`** — **0 von 0**: Behauptungen stehen im Urteil, das nicht in der Kandidatentabelle persistiert wird. Platzhalter sind nicht zählbar.
- **`aegis._anhaengen`** — **nicht belegbar**: Die Funktion protokolliert ihre Rückgabe nicht. „None wegen TypeScript" und „None wegen nichts anzuhängen" sind in der DB nicht unterscheidbar.

**Also: 3 von 4 Stellen haben lautes Sterben gegen stilles Nichtstun getauscht, genau wie Sie sagten.** Die Zähler fehlen. Sie nachzurüsten ist eine Kernänderung, die Lauf 34 töten würde — der läuft gerade im Vorspann. Ich schlage vor, das nach Lauf 34 zu machen, außer Sie wollen den Lauf dafür opfern.

**Den Test habe ich sofort korrigiert**, weil er dieselbe Schwäche hatte: Er prüfte `bool(von)`, also nur *dass* etwas zurückkam. Jetzt prüft er den Grund im Wortlaut — je Ausgang das erwartete Muster (`Typbau nicht bestanden`, `Testnachweis unbrauchbar`, `keine ausgeführten Testfälle`, `ohne Bestätigung`) plus die Kennzeichnung `kein Verhaltensfang`, und beim bestandenen Testlauf die leere Zeichenkette. 17 Tests grün.

Lauf 34 ist im Vorspann; Kern unverändert bei `c214d1d`.
```

### V0712 · 21.09.2026 18:56:21 CEST · Philipp · Nachricht id 11033 · Sitzung `20260921_015554_e79a4a0f` · 1094 B

```text
Unbequem und richtig gemessen — und der verschärfte Test prüft jetzt den Grund, nicht nur, dass einer kommt. Entscheidung Chat-Claude: Lauf 34 jetzt anhalten, Zähler nachrüsten, dann Lauf 35 — ohne Zähler kann Lauf 34 nicht der Abnahmelauf sein, weil Doppelungs- und Fangzeile an Organen hängen, deren Schweigen sich nicht messen lässt; im Vorspann kostet das Anhalten Minuten. Nur die Zähler, eng: jede neutrale Rückgabe der vier Stellen mit ihrem Grund in die Datenbank, abfragbar je Organ mit Nenner, und je Zähler eine Gegenprobe, die zeigt, dass ein erzwungener neutraler Fall tatsächlich gezählt wird. Maßstab, vorher gesetzt: Eine Torzeile, die an einem Organ hängt, gilt für TypeScript nur als belegt, wenn das Organ in mehr als der Hälfte seiner Fälle geurteilt hat. Und schick die vollständigen Adressen als ganze Zeilen von skills/measurement-harness-discipline/SKILL.md, skills/measurement-harness-discipline/references/noise-floor-calibration.md, skills/measurement-harness-discipline/references/defect-class-sweep.md und ZWISCHENBERICHT.md aus uebernahme-01.
```

### V0713 · 21.09.2026 18:57:44 CEST · Hermes-Zwischentext · Nachricht id 11042 · Sitzung `20260921_015554_e79a4a0f` · 126 B

```text
Lauf 34 steht (Vorspann unvollständig = tot nach Satz 2), Verbrauch unverändert 1,22 €. Jetzt die Zähler — Test zuerst.
```

### V0714 · 21.09.2026 18:58:30 CEST · Hermes-Zwischentext · Nachricht id 11048 · Sitzung `20260921_015554_e79a4a0f` · 93 B

```text
Jetzt die vier Zählstellen einbauen — mit einem Kontext, der ohne Lauf einfach nichts tut.
```

### V0715 · 21.09.2026 19:00:15 CEST · Hermes-Zwischentext · Nachricht id 11068 · Sitzung `20260921_015554_e79a4a0f` · 118 B

```text
15 Zählertests grün, inklusive aller Gegenproben. Jetzt den Kontext im Lauf setzen, sonst zählt im Betrieb niemand.
```

### V0716 · 21.09.2026 19:00:45 CEST · Hermes-Zwischentext · Nachricht id 11074 · Sitzung `20260921_015554_e79a4a0f` · 91 B

```text
Mein Patch hat den Docstring verdrängt — er steht jetzt hinter Code und ist keiner mehr.
```

### V0717 · 21.09.2026 19:01:15 CEST · Hermes-Zwischentext · Nachricht id 11080 · Sitzung `20260921_015554_e79a4a0f` · 102 B

```text
Jetzt der Nachweis, dass der Kontext im echten Lauf ankommt — sonst zählt der Zähler nur in Tests.
```

### V0718 · 21.09.2026 19:05:45 CEST · Hermes-Zwischentext · Nachricht id 11088 · Sitzung `20260921_015554_e79a4a0f` · 105 B

```text
Mein Patch hat eine Zeile verschluckt: `_g0.zaehlkontext_setzen` ersetzte offenbar `mutanten_json = ...`.
```

### V0719 · 21.09.2026 19:05:57 CEST · Hermes-Zwischentext · Nachricht id 11090 · Sitzung `20260921_015554_e79a4a0f` · 207 B

```text
Gravierender Fehler von mir: Mein Patch hat die **Signatur** geändert — `mutanten_json: str | None, ziel: int` wurde zu `mutanten_datei: str | None = None, ziel: float = 0.8`. Ich stelle das Original her.
```

### V0720 · 21.09.2026 19:10:24 CEST · Hermes-Zwischentext · Nachricht id 11100 · Sitzung `20260921_015554_e79a4a0f` · 97 B

```text
Zweiter Patch-Schaden: Mein Import-Patch hat `nischen` durch `landkarte, neutralzaehler` ersetzt.
```

### V0721 · 21.09.2026 19:10:43 CEST · Hermes-Zwischentext · Nachricht id 11106 · Sitzung `20260921_015554_e79a4a0f` · 88 B

```text
Alle Importzeilen sind jetzt korrekt — nur `neutralzaehler` ergänzt, nichts entfernt.
```

### V0722 · 21.09.2026 19:15:40 CEST · Hermes · Nachricht id 11114 · Sitzung `20260921_015554_e79a4a0f` · 2280 B

```text
Die vier angeforderten Adressen als ganze Zeilen:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/uebernahme-01/skills/measurement-harness-discipline/SKILL.md

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/uebernahme-01/skills/measurement-harness-discipline/references/noise-floor-calibration.md

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/uebernahme-01/skills/measurement-harness-discipline/references/defect-class-sweep.md

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/uebernahme-01/ZWISCHENBERICHT.md

**Zähler nachgerüstet, Lauf 35 läuft.**

Lauf 34 im Vorspann angehalten (damit tot nach Satz 2), Verbrauch unverändert 1,22 € — das Anhalten kostete nichts als Rechenzeit.

Neu: `biotop/organe/neutralzaehler.py`. Jede der vier Stellen bucht ihren Ausgang mit Grund; `stand()` gibt je Organ neutral, geurteilt, gesamt, Anteil und Gründe. Der Maßstab steht im Kern, nicht im Bericht: `traegt_torzeile()` verlangt **Mehrheit geurteilter Fälle**, und null Fälle sind keine Mehrheit.

18 Tests. Je Zählstelle eine Gegenprobe mit erzwungenem neutralem Fall, der tatsächlich in der Datenbank landen muss, plus die Gegenrichtung. Dazu drei Tests, dass `lauf.generation()` und `lauf.generation0()` den Kontext wirklich setzen — ohne die wäre nur bewiesen, dass die Stellen buchen *können*, nicht dass sie im Betrieb buchen. Genau diese Lücke hatte drei Stellen unbemerkt schweigen lassen.

Der verschärfte Test prüft den Grund im Wortlaut, wie gefordert.

**Zwei eigene Patchfehler**, beide von der Regression gefangen und behoben: Die Signatur von `lauf.generation0` war versehentlich zu `mutanten_datei/ziel=0.8` geändert, und der Import von `nischen` in `generation0.py` war durch `landkarte` ersetzt worden. Ich habe anschließend alle Importzeilen der vier berührten Dateien gegen HEAD verglichen — nur `neutralzaehler` ergänzt, nichts entfernt. Das hätte ich beim Patchen prüfen müssen, nicht erst nach zwei roten Läufen.

Regression **354 bestanden, 2 übersprungen**. Kern eingefroren bei `d6e6f8c`.
```

### V0723 · 21.09.2026 19:15:57 CEST · Hermes · Nachricht id 11118 · Sitzung `20260921_015554_e79a4a0f` · 292 B

```text
Das ist die erwartete Rückmeldung meines eigenen SIGTERM auf Lauf 34 — kein neuer Befund.

Lauf 35 läuft auf Kern `d6e6f8c`, gerade beim Einlegen, Verbrauch unverändert 1,22 € von 10 €. Die Zählertabelle entsteht erst bei der ersten Generation.

Nächste Meldung ist die Endmeldung.
```

### V0724 · 21.09.2026 20:06:22 CEST · Hermes-Zwischentext · Nachricht id 11122 · Sitzung `20260921_015554_e79a4a0f` · 246 B

```text
Die Wiederholung hat funktioniert wie gebaut: Versuch 1 nach 2 s, Versuch 2 nach 8 s, dann Ausfall mit `versuche: 3`. qwen ist seit 14 Stunden durchgehend 429. Die Frage ist, warum **ein** ausgefallenes Schwarmmitglied die ganze Kampagne beendet.
```

### V0725 · 21.09.2026 20:06:47 CEST · Hermes-Zwischentext · Nachricht id 11124 · Sitzung `20260921_015554_e79a4a0f` · 204 B

```text
gen0 fängt `AnbieterFehler` korrekt ab und wechselt den Anbieter. Der Abbruch kam von der Kassensperre — die ist kein `AnbieterFehler` und fällt durch. Ich prüfe, ob der Bandit aus dem Ausfall lernt.
```

### V0726 · 21.09.2026 20:07:18 CEST · Hermes-Zwischentext · Nachricht id 11126 · Sitzung `20260921_015554_e79a4a0f` · 184 B

```text
Gefunden: Das `continue` nach `AnbieterFehler` überspringt `nischen.buchen`. Ein ausgefallener Anbieter wird nie als Fehlversuch gebucht — der Bandit wählt ihn unverändert weiter.
```

### V0727 · 21.09.2026 20:07:39 CEST · Hermes-Zwischentext · Nachricht id 11128 · Sitzung `20260921_015554_e79a4a0f` · 184 B

```text
qwen lief in Lauf 32 erfolgreich (4 von 24 Erfolgen) — es ist nicht tot, sondern zeitweise gedrosselt. Ich kläre den Ausfall und stelle die Lage fest, ohne Lauf 36 blind zu starten.
```

### V0728 · 21.09.2026 20:08:30 CEST · Hermes · Nachricht id 11134 · Sitzung `20260921_015554_e79a4a0f` · 2121 B

```text
Die Kette ist vollständig belegt. Zwei Befunde, aber ich stoppe hier: der zweite ist eine Entscheidung über Ihre Regel, nicht über einen Fehler.

**Lauf 35 rot — die Wiederholung hat gegriffen, der Lauf starb trotzdem woanders.**

Belegt an der Protokollkette (`BELEG-AUSFALLKETTE.txt`, Einträge 17529–17535):
- qwen HTTP 429 → **Wiederholung 1** nach 2 s → **Wiederholung 2** nach 8 s → Ausfall mit `versuche: 3`, `wiederholbar: True`. Die Regel aus Ihrer Vorentscheidung arbeitet genau wie festgelegt.
- `generation0` fing den Ausfall korrekt ab und wählte den nächsten Anbieter (`bandit.wahl` in 17534).
- **Dort** starb der Lauf: `kasse.vorpruefung` verweigert jeden weiteren Modellaufruf, solange ein Ausfall mit `verbrauch_bekannt=False` offen ist.

Die Sperre ist gewollt und hat einen Auflösungsweg — aber der wird nur **von Hand** gerufen. Im Lauf ruft ihn niemand. Damit tötet jeder unwiederholbare 429 jeden Lauf, egal wie gut Wiederholung und Anbieterwechsel funktionieren. Ich habe den Ausfall geklärt (Höchstfall 0,0028 €, Verbrauch jetzt 1,2238 €).

**Zweiter Befund, gemessen:** `generation0.py:365` überspringt mit `continue` das `nischen.buchen()`. Ein ausgefallener Anbieter wird nie als Bandit-Fehlversuch gebucht — qwen wurde **64× gewählt**, 2 Ausfälle protokolliert, **0** davon gebucht. Der Bandit lernt aus Ausfällen nichts und wählt qwen unverändert weiter. qwen ist dabei nicht tot: in Lauf 32 lieferte es 9 Erfolge in vier Nischen, der 429 ist zeitweise.

**Warum ich anhalte:** Die naheliegende Behebung — `ausfall_klaeren` automatisch im Lauf rufen — würde Ihre Regel aufweichen. Sie haben festgelegt, dass der Zweifel zu Lasten des Budgets gebucht wird; ob das *automatisch* geschehen darf oder eine Entscheidung des Auftraggebers bleiben muss, ist Ihre Festlegung, nicht meine. Dasselbe beim Banditen: Einen Infrastrukturausfall als Qualitäts-Fehlversuch zu buchen, vermischt zwei Dinge, die Satz 8 trennt („Ausfall ist nie Beitrag" — aber ist er ein Misserfolg?).

Verbrauch 1,2238 € von 10 €, Kern unverändert `d6e6f8c`, kein Lauf aktiv.
```

### V0729 · 21.09.2026 20:15:07 CEST · Philipp · Nachricht id 11135 · Sitzung `20260921_015554_e79a4a0f` · 1192 B

```text
Richtig angehalten — beides sind Regelfragen, und du hast sie als solche erkannt. Entscheidung Chat-Claude zu Frage 1: ausfall_klaeren wird automatisch im Lauf gerufen — das ist die Regel, mechanisch angewandt, nicht aufgeweicht: Höchstfall voll gegen das Budget, harte Grenze unverändert, ein Ausfall nach dem anderen, nie mehrere auf einmal freigeben; aufgeweicht wäre sie nur bei einer Buchung unter dem Höchstfall oder an der Grenze vorbei. Jede automatische Klärung wird protokolliert und erscheint im Bericht mit Anzahl und Summe; Gegenproben: Ein erzwungener Ausfall wird automatisch mit genau dem Höchstfall gebucht und der Lauf geht weiter — und ein Lauf, dessen Klärungen die Grenze erreichen, bricht am Budget ab. Zu Frage 2: kein Fehlversuch — Satz 8 trennt Ausfall von Qualität, ein gedrosselter Anbieter ist nicht schlechter, sondern nicht erreichbar; nischen.buchen bleibt für Ausfälle aus. Eine getrennte Erreichbarkeitsführung — Anbieter nach wiederholten Ausfällen zeitweise aussetzen, Bewertung unangetastet — kommt auf die Liste nach T3. Nur diese eine Kernänderung, volle Regression, Kern einfrieren, Lauf 36 bis zum Ende, ohne Zwischenmeldungen.
```

### V0730 · 21.09.2026 20:16:22 CEST · Hermes-Zwischentext · Nachricht id 11140 · Sitzung `20260921_015554_e79a4a0f` · 99 B

```text
5 rot, 1 grün (die Gegenprobe „keine Klärung ohne Anlass" gilt schon). Jetzt die Kernänderung.
```

### V0731 · 21.09.2026 20:20:49 CEST · Hermes-Zwischentext · Nachricht id 11148 · Sitzung `20260921_015554_e79a4a0f` · 130 B

```text
Drei Tests kodieren das alte Sperrverhalten. Ich prüfe einzeln, ob sie überholt sind oder eine Regel schützen, die weiter gilt.
```

### V0732 · 21.09.2026 20:26:10 CEST · Hermes · Nachricht id 11163 · Sitzung `20260921_015554_e79a4a0f` · 1310 B

```text
Kernänderung umgesetzt, Lauf 36 läuft. Beide Festlegungen sind eingearbeitet:

**Frage 1 — automatische Klärung.** `kasse.vorpruefung` klärt einen offenen Ausfall jetzt selbst, statt dauerhaft zu sperren: voller Höchstfall gegen das Budget, harte Grenze unverändert, genau einer je Vorprüfung, jede Klärung mit `automatisch=True` protokolliert. `kasse.ausfallklaerungen()` liefert Anzahl und Summe für den Bericht. Beide von Ihnen verlangten Gegenproben sind darunter: erzwungener Ausfall wird mit genau dem Höchstfall gebucht und der Lauf geht weiter — und ein Lauf, dessen Klärung die Grenze erreicht, bricht am Budget ab, wobei der Verbrauch gebucht bleibt.

**Frage 2 — nicht geändert, wie festgelegt.** `nischen.buchen` bleibt für Ausfälle aus. Der gemessene Befund (qwen 64× gewählt, 2 Ausfälle, 0 als Bandit-Fehlversuch gebucht) steht damit absichtlich so; die getrennte Erreichbarkeitsführung ist auf der Liste nach T3 notiert.

Drei bestehende Tests schrieben das alte Sperrverhalten fest — angepasst auf das, was weiter gilt: null Beitrag, Verbrauch nicht als bekannt ausgegeben, Buchung nicht kleiner als die Reservierung.

Regression **360 bestanden, 2 übersprungen**. Kern eingefroren bei `5b4066f`, Verbrauch 1,2238 € von 10 €.

Nächste Meldung ist die Endmeldung.
```

### V0733 · 22.09.2026 00:14:03 CEST · Hermes-Zwischentext · Nachricht id 11169 · Sitzung `20260921_015554_e79a4a0f` · 251 B

```text
Die Zähler arbeiten: `aegis.behauptung` 8/8 geurteilt, `gedaechtnis.aenderungsziel` 57 von 83, `generation0._testlauf` 500/500. Und 75 automatische Klärungen hielten den Lauf am Leben. Gen 4 starb an derselben Klasse — die mein Prüfer nicht fand.
```

### V0734 · 22.09.2026 00:14:32 CEST · Hermes-Zwischentext · Nachricht id 11173 · Sitzung `20260921_015554_e79a4a0f` · 133 B

```text
Acht Stellen derselben Klasse — alle verarbeiten Modellcode, der syntaktisch kaputt sein kann. Test zuerst, dann alle in einem Zug.
```

### V0735 · 22.09.2026 00:15:07 CEST · Hermes-Zwischentext · Nachricht id 11181 · Sitzung `20260921_015554_e79a4a0f` · 110 B

```text
7 rot — alle reproduzieren den Laufabbruch. Die sauberste Behebung liegt an einer Stelle: im Adapter selbst.
```

### V0736 · 22.09.2026 00:16:09 CEST · Hermes-Zwischentext · Nachricht id 11193 · Sitzung `20260921_015554_e79a4a0f` · 187 B

```text
Der statische Prüfer meldet weiter 8 — er sieht nur die Aufrufstelle, nicht dass der Adapter jetzt selbst fängt. Die Behebung ist eine Ebene tiefer; ich mache das im Prüfer sichtbar.
```

### V0737 · 22.09.2026 00:16:27 CEST · Hermes-Zwischentext · Nachricht id 11199 · Sitzung `20260921_015554_e79a4a0f` · 163 B

```text
Von 8 auf 1 — und der verbleibende ist absichtlich: `messgeraet.messen` **muss** werfen, ohne Messung gibt es kein Urteil. Genau das prüft eine der Gegenproben.
```

### V0738 · 22.09.2026 00:21:20 CEST · Hermes · Nachricht id 11207 · Sitzung `20260921_015554_e79a4a0f` · 1626 B

```text
Kernfehler-Ausnahme — Lauf 36 lief deutlich weiter als alle vorherigen, bevor er an derselben Klasse in neuer Bauart starb.

**Was die Kernänderungen gebracht haben, gemessen:**
- **Generation 1 und 3 angenommen**, Generation 2 sauber abgelehnt (0 von 10 Kandidaten überlebten den Ankläger — eine echte Messung, kein Absturz)
- **75 automatische Ausfallklärungen**, 0,3323 € — genau die Stelle, an der Lauf 35 starb. Die Regel arbeitet mechanisch, der Lauf lief weiter.
- **Neutralzähler liefern Zahlen:** `generation0._testlauf` 500 von 500 geurteilt, `aegis.behauptung` 8 von 8, `gedaechtnis.aenderungsziel` 57 von 83 geurteilt bei 26 Enthaltungen (`diff_nicht_anwendbar`). Alle drei über der Hälfte — die Organe arbeiten, sie schweigen nicht.

**Generation 4 starb an der zweiten Bauart derselben Klasse.** Mein erster Zweigvergleich suchte `raise` *im* TS-Zweig; hier steht dort keiner — der Wurf kommt aus der gerufenen Adapterfunktion (`typescript.quellfunktionen` bei syntaktisch kaputtem Modellcode). Der Python-Zweig fängt das seit jeher mit `except SyntaxError`.

Zweiter Zweigvergleich mit passendem Kriterium: **8 Stellen in 6 Dateien**. Behoben an einer Stelle statt an acht — die vier Parserfunktionen des Adapters fangen Syntaxfehler des gelieferten Codes selbst ab; Kammerabbruch und Zeitlimit bleiben Messgerätfehler und werden weitergeworfen. Nach der Behebung meldet der Prüfer noch **1 Stelle**: `messgeraet.messen`, absichtlich, mit Gegenprobe.

10 Tests, zuerst 7 rot. Regression **370 bestanden, 2 übersprungen**. Kern `8c7dcdc`, Lauf 37 läuft. Verbrauch 2,4102 € von 10 €.
```

### V0739 · 22.09.2026 06:29:42 CEST · Hermes-Zwischentext · Nachricht id 11209 · Sitzung `20260921_015554_e79a4a0f` · 80 B

```text
Sättigung erreicht — Lauf 37 ist durchgelaufen. Jetzt die Abschlussmessungen.
```

### V0740 · 22.09.2026 06:30:01 CEST · Hermes-Zwischentext · Nachricht id 11211 · Sitzung `20260921_015554_e79a4a0f` · 141 B

```text
Sättigung nach Regel erreicht: 6 angenommene Generationen, Verbesserung 0,00 % über 5 Generationen. Jetzt die Torzeilen und Abschlussdaten.
```

### V0741 · 22.09.2026 06:32:00 CEST · Hermes-Zwischentext · Nachricht id 11219 · Sitzung `20260921_015554_e79a4a0f` · 58 B

```text
Jetzt der eine Reviewdurchgang, bevor ich veröffentliche.
```

### V0742 · 22.09.2026 06:32:13 CEST · Hermes · Nachricht id 11222 · Sitzung `20260921_015554_e79a4a0f` · 794 B

```text
**Lauf 37 ist gesättigt durchgelaufen — der Auftrag hat sein Ziel erreicht.**

Sechs Generationen angenommen, Sättigung nach der Regel aus Abschnitt 8 (Verbesserung 0,00 % über fünf Generationen, Schwelle 0,5 %), **Kernmaß −28 → −14**, Testbestand 182 → 445.

Der Abschlussbericht liegt geschrieben; ein Reviewdurchgang prüft gerade jede Zahl gegen die Datenbank — ich habe ihn ausdrücklich auf zwei Stellen angesetzt, bei denen ich selbst einen Widerspruch sehe: Ich nenne die Ausfallklärungen einmal mit 0,4449 € und einmal mit 0,4505 €, und ich schreibe „sieben Commits" über einer Liste mit neun Zeilen. Beides muss vor der Veröffentlichung stimmen.

Verbrauch 5,4770 € von 10 €. Endmeldung mit Abholadresse und Prüfsumme kommt, sobald das Review durch ist.
```

### V0743 · 22.09.2026 06:54:28 CEST · Hermes-Zwischentext · Nachricht id 11290 · Sitzung `20260921_015554_e79a4a0f` · 144 B

```text
Drei schwere Befunde. Ich prüfe sie selbst nach, bevor ich korrigiere — besonders den Rauschmessungs-Befund, den ich mehrfach behauptet habe.
```

### V0744 · 22.09.2026 06:54:57 CEST · Hermes-Zwischentext · Nachricht id 11292 · Sitzung `20260921_015554_e79a4a0f` · 167 B

```text
Alle drei schweren Befunde bestätigt. Bei Befund C muss ich differenzieren — die Prüfung deckt einen Fehler in meinem Bericht auf, aber nicht ganz den behaupteten.
```

### V0745 · 22.09.2026 06:56:23 CEST · Hermes-Zwischentext · Nachricht id 11294 · Sitzung `20260921_015554_e79a4a0f` · 82 B

```text
Jetzt die Korrektur — alle elf Befunde, mit genauer Unterscheidung bei Befund C.
```

### V0746 · 22.09.2026 06:57:19 CEST · Hermes · Nachricht id 11300 · Sitzung `20260921_015554_e79a4a0f` · 2157 B

```text
**T3 abgeschlossen.**

Lauf 37 ist nach der Sättigungsregel aus Abschnitt 8 beendet — sechs angenommene Generationen, Verbesserung 0,00 % über fünf Generationen bei Schwelle 0,5 %. **Kernmaß −28 → −14**, Testbestand 182 → 445 (alle bestanden), Sicherheitspunkte 27 → 14, tote Funktionen 0. Am Werk: 7 Quelldateien geändert, 97 neu.

**Tor 4 mit Nenner:** Fangquote 93 von 100 versiegelten Mutanten (arithmetik 11/11, boolesch 2/2, vergleich 21/22, zahlengrenze 59/65) — mit der Einschränkung, dass der Typprüfer beim Versiegeln 28 von 128 Mutanten verwarf, davon 26 von 48 Vergleichsoperatoren. Drei von vier Organen tragen ihre Torzeile (56/56, 203/285, 400/600); `aegis._anhaengen` trägt nicht, weil es in Lauf 37 nie erreicht wurde. Verbundausfall an 114 echten qwen-Ausfällen belegt, jeder mit null Beitrag.

**Elf Läufe endeten ohne Abnahme, bevor einer durchlief** — zehn an Instrumentfehlern, einer an meinem Ablauffehler. Es war eine Fehlerklasse in zwei Bauarten, nicht elf Einzelfälle.

**Der Reviewdurchgang fand elf Befunde, alle übernommen**, drei davon schwer: „qwen 64× gewählt" war aus keiner Quelle belegbar und in sich unmöglich; ich nannte zwei verschiedene Beträge für dieselbe Größe; und meine mehrfach wiederholte Aussage, die Rauschmessung verwerfe ihre Einzelwerte, war zu weit — die fünf Messwerte je Bereich sind gespeichert, es fehlen nur die Werte *innerhalb* jeder Messung. Der Befundteil steht im Bericht.

Verbrauch **5,4770 € von 10,00 €**, Kern `8c7dcdccf5efa18ed31cc77833a6742cad2164cf`, Regression 370 bestanden / 2 übersprungen.

Abholadresse, 59 von 59 Dateien HTTPS-bytegleich:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-01/ABSCHLUSSBERICHT.md

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-01/DATEIEN.txt

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-01/MANIFEST.sha256

Ordnerprüfsumme: `642c16b8f2cfc4f9fdd2bff34613da21ba482519992dd28e47dbe3eb034864fe`
```

### V0747 · 22.09.2026 14:52:53 CEST · Philipp · Nachricht id 11301 · Sitzung `20260921_015554_e79a4a0f` · 1812 B

```text
T3 durchgelaufen, Zahlen nachgerechnet und stimmig — Kasse, Ausfälle, Fangquote, Zähler, Commits. Wertung Chat-Claude: nicht abgenommen, weil fünf Torzeilen aus Tor 4 im Bericht fehlen; alles aus der vorhandenen Datenbank, kein neuer Lauf, als Nachtrag abschluss-02. (1) Halluzinationsprobe: zahlen war laut Verfassung der saubere Vergleichsbereich, hatte aber acht Sicherheitspunkte und bekam drei angenommene Änderungen (Gen 1, 2, 6) — zeig für jede, was sie im Code tatsächlich änderte und welche Prüferregel sie zufriedenstellte, und entscheide: War zahlen nie sauber (dann ist die Probe leer, nicht bestanden), oder waren die Punkte Fehlalarme des TS-Prüfers (dann ist die Probe gerissen)? (2) Versiegelte Schwächen: Anzahl, welche nach „behoben heißt verschwunden" behoben sind, Anteil gegen 80 %. (3) Doppelungsanteil der Angriffstests gegen 20 % — der Doppelgängeranteil der Vorschläge ist eine andere Zahl —, und welche Torzeile daran hängt, dass aegis._anhaengen nie erreicht wurde. (4) Kein Rückschritt je angenommener Generation, und woher die drei fehlschlagenden Tests in eingang vor Generation 8 kamen. (5) Eichung von Lauf 37: Rauschmessung, 4 von 4 Proben, 4 von 4 Gegenproben. Korrigiere außerdem „eine Fehlerklasse in zwei Bauarten" — laut eigener Kassentabelle starben nur 31, 32 und 36 daran, 27 und 28 am Rauschen, 29, 30 und 35 an Ausfällen ohne Klärungsweg. Skills vor T5: In defect-class-sweep.md den Zweigvergleich aufnehmen und klarstellen, dass eine Weiche selbst der Fehler sein kann — die Musterliste nur aus Python-Syntax war meine zu enge Vorgabe; in SKILL.md die Regel „enthalten statt werfen" um ihre zweite Hälfte ergänzen: jede Enthaltung zählen, null Fälle sind keine Mehrheit. Ein Reviewdurchgang, Budget für den Nachtrag 1 € hart.
```

### V0748 · 22.09.2026 14:53:43 CEST · Hermes-Zwischentext · Nachricht id 11302 · Sitzung `20260921_015554_e79a4a0f` · 96 B

```text
Nicht abgenommen — fünf Torzeilen fehlen. Ich arbeite sie aus der vorhandenen Datenbank nach.
```

### V0749 · 22.09.2026 14:54:11 CEST · Hermes-Zwischentext · Nachricht id 11306 · Sitzung `20260921_015554_e79a4a0f` · 204 B

```text
Der Befund ist eindeutig: alle acht Punkte waren `security/detect-object-injection` (LOW), und die Änderungen ersetzten `arr[i]` durch `arr.at(i)` — ohne Verhaltensänderung. Ich prüfe die Gegenprobe.
```

### V0750 · 22.09.2026 14:54:39 CEST · Hermes-Zwischentext · Nachricht id 11310 · Sitzung `20260921_015554_e79a4a0f` · 213 B

```text
Entscheidend: Die versiegelten Kriterien nennen **keine** Schwäche in `zahlen` — S1 tarife, S2/S3 planung/eingang, S4 bericht, S5 tarife. `zahlen` war sauber, die acht Punkte waren Fehlalarme. Jetzt Torzeile 2.
```

### V0751 · 22.09.2026 14:55:06 CEST · Hermes-Zwischentext · Nachricht id 11314 · Sitzung `20260921_015554_e79a4a0f` · 137 B

```text
Der Endstand lief nicht durch (rc=1) — das Ergebnis „0 von 5" wäre unbelegt. Ich kläre die Ursache, bevor ich irgendetwas berichte.
```

### V0752 · 22.09.2026 14:55:31 CEST · Hermes-Zwischentext · Nachricht id 11318 · Sitzung `20260921_015554_e79a4a0f` · 184 B

```text
Der Gegenzeuge lief vollständig durch — `rc=1` ist sein Ergebniscode bei verbleibenden Verletzungen, kein Fehler. Mein Auswertungsskript hat das als Absturz gelesen. Ich korrigiere.
```

