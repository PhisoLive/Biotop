# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 039 von 054

- Einträge V0848 bis V0853. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0848 · 23.09.2026 15:03:47 CEST · Philipp · Nachricht id 13912 · Sitzung `20260921_015554_e79a4a0f` · 1233 B

```text
Zwei Entscheidungen von Chat-Claude, damit du ohne Warten fertig wirst. Sperre 3: nicht auflösen — miss S1 bis S5 selbst nach, die Dateien des Unteragenten brauchst du nicht. Laufzeit-Grenzmaß: Entscheidung ja — Median mehrerer Messungen je Seite statt einer Einzelmessung, Schwelle unverändert; nicht mehr in T3, sondern als erste Änderung vor T4, mit der Gegenprobe, dass K2904 und K3091 als dieselbe Änderung danach gleich entschieden werden. In abschluss-03 zusätzlich: (1) ob die 49 wegen der WAL übersehenen Kassenzeilen in 9,7286 € enthalten sind, nachgezählt am Schnappschuss — die harte Grenze ist 10 €; (2) dein Schluss zu Generation 0 in Lauf 37 — zweimal „0 von 100 gefangen", daraufhin Tests für alle 100 —, an der Ursache gelesen statt aus den Zählern geschlossen; bestätigt er sich, gehört er als Messgerätbefund in den Bericht: Ein Durchlauf, in dem jeder Fall neutral ausgeht, heißt „nicht gemessen", nicht „nichts gefangen". Dauerhaft: Zwischenbericht in den Prüfkanal spätestens bei 120 von 150 Aufrufen einer Sitzung — nicht erinnern, sondern auslösen, dieselbe Lehre wie beim Verdrahtungstest. Dann abschluss-03 wie geplant, mit Abholadresse als ganze Zeile und Prüfsumme.
```

### V0849 · 23.09.2026 15:24:32 CEST · Hermes-Zwischentext · Nachricht id 13951 · Sitzung `20260921_015554_e79a4a0f` · 160 B

```text
Tests des Wächters sind grün (6 von 6). Jetzt wird er wirklich scharf geschaltet: als Cron-Job ohne Modell, und dazu ein echter Zwischenbericht im Prüfkanal.
```

### V0850 · 23.09.2026 15:47:22 CEST · Hermes-Zwischentext · Nachricht id 13991 · Sitzung `20260921_015554_e79a4a0f` · 96 B

```text
Die Haltegrenze prüft vor jeder Generation, wie im Bericht beschrieben. Jetzt veröffentlichen.
```

### V0851 · 23.09.2026 15:47:53 CEST · Hermes · Nachricht id 13993 · Sitzung `20260921_015554_e79a4a0f` · 3404 B

```text
T3 ist **nicht abgenommen**. abschluss-03 liegt im Prüfkanal: 78 von 78 Dateien sind über HTTPS bytegleich abrufbar, die Webseite antwortet mit HTTP 200. Kosten 0,00 €, kein Modellaufruf.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-03/ABSCHLUSS-03.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-03/DATEIEN.txt
Prüfsumme (sha256 über MANIFEST.sha256): `441f489a54d43a7c84e7f0c94a36561c5d9fe40f58649e091571b92e6b76c5dc`

**Deine zwei Zusatzfragen:**
- **Kasse:** Die 49 Zeilen aus der WAL sind in 9,728638 € enthalten. Sie gehören alle zu Lauf 38, Generation 17, und kosten zusammen 0,245512 €. Ohne WAL waren es 2554 Zeilen mit 9,483126 €, zusammen also 2603 Zeilen und 9,728638 €. Die 10-€-Grenze ist eingehalten, Rest 0,271362 €.
- **Generation 0 in Lauf 37:** Mein Schluss stimmt, und ich habe die Ursache nachgewiesen.
  - Vor jedem Mutanten prüft Generation 0 die Typen über `src/` und `tests/`. Eine Testdatei, die in Vitest besteht, aber diese Prüfung bricht, macht jeden Mutanten neutral, und neutral wurde als „blind“ gezählt.
  - Nachgestellt habe ich das mit 5 Mutanten: 5 von 5 gefangen, mit einer solchen Testdatei 0 von 5, nach dem Entfernen wieder 5 von 5. Die Prüfung zwischen den Runden (Vitest) ließ genau diese Datei durch.
  - Folge in Lauf 37: zweimal „gefangen 0“, obwohl nichts gemessen wurde, und danach 93 statt 10 neue Testdateien. Das steht jetzt als Messgerätbefund in §5: „nicht gemessen“, nicht „nichts gefangen“.

**Weitere Ergebnisse:**
- **S1 bis S5, selbst gemessen:** Lauf 38 behebt 4 von 5 (80 %), Lauf 37 3 von 5. S5 bleibt in beiden offen. Welche Änderung welche Schwäche behoben hat, ist ebenfalls gemessen.
- **Review:** ein Durchgang mit 21 Befunden, davon 3 hoch.
  - K3091 wurde in Lauf 38 wegen Fehlalarm-Punkten angenommen, bei nur −11,2 % Laufzeit. Die S2-Vorgabe gilt damit als **nicht belastbar**, bis der Median-Umbau vor T4 kommt.
  - Der Verhaltensvergleich urteilt auch, wenn er gar nichts beobachtet hat: K3106 blieb bei 0 von 7 beobachteten Funktionen unentdeckt.
  - Fällt die Sonde aus, wird der Kandidat abgelehnt.
- **Eigene Entscheidung:** Die Code-Befunde behebe ich nicht mehr in T3, denn das wäre ungeprüfter Code nach dem einzigen Review. Sie liegen als 9 Tests für T4 vor, am Commit `f821707` alle 9 rot. Das Repository steht wieder auf dem geprüften Stand.
- **Zwischenbericht:** Ein minütlicher Cron-Job ohne Modell (`26fbb1513a1a`) löst ihn bei 110 und 140 von 150 Runden aus. 110 statt 120 ist meine Entscheidung, damit der Bericht trotz des Minutentakts sicher bis 120 im Prüfkanal liegt. 6 von 6 Tests sind grün. Eine echte Auslösung liegt im Prüfkanal, und das Protokoll zeigt, dass der Zeitplan den Job wirklich aufruft.
- **Sperren:** Der Prüfer lief im Review in eine Formatsperre. Ich habe das gespeicherte Skript gelesen: Es enthielt nur `grep`, `sha256sum` und `ls`. Nach deiner Regel habe ich es unverändert ausgeführt, und es bestätigte die Zählung des Prüfers. Keine harte Linie berührt.

**Offen für dich:**
- Bestwert als Minimum;
- ob Laufzeit-Ablehnungen im Gedächtnis sperren sollen;
- ob Schwarm und Ankläger die rohe oder die geeichte Messung lesen;
- ein größerer Korpus für den Verhaltensvergleich.
```

### V0852 · 23.09.2026 15:48:04 CEST · Hermes · Nachricht id 13995 · Sitzung `20260921_015554_e79a4a0f` · 460 B

```text
Das Review ist vollständig in abschluss-03 eingearbeitet (§9); die gemeldete Fassung ist die veröffentlichte. Sie wurde nach dem Abschluss des Prüfers nicht mehr geändert, ihre Prüfsumme ist `0fb2e3bb…`. An der Lieferung ändert sich nichts:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/abschluss-03/DATEIEN.txt
Prüfsumme `441f489a54d43a7c84e7f0c94a36561c5d9fe40f58649e091571b92e6b76c5dc`
```

### V0853 · 23.09.2026 15:48:13 CEST · Hermes · Nachricht id 13997 · Sitzung `20260921_015554_e79a4a0f` · 123 B

```text
Nichts Neues: Die Ergebnisse von Job 5 (Ursache in Generation 0, Umformungen) stehen bereits in abschluss-03, §4b und §5.
```

