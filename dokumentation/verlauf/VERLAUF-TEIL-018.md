# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 018 von 054

- Einträge V0352 bis V0358. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0352 · 19.09.2026 23:42:31 CEST · Hermes · Nachricht id 2687 · Sitzung `20260918_225920_3e614670` · 2027 B

```text
**Punkt 6 erledigt: Archivierung nach der neuen Zeile** (`ausgaben/24-archivierung-neue-zeile.txt`).

**Warum Phase 3 null Archivierungen hatte** — jetzt mit Zahlen belegt:

| Lauf | Generationen | davon angenommen | alte Zählung | neue Zählung |
|---|---|---|---|---|
| 16 | 8 | 2 | erreicht 5 nie | erreicht 5 |
| 17 | 7 | 4 | nie | erreicht 5 |
| 19 | 5 | 1 | nie | erreicht 5 |
| 20 | 5 | 1 | nie | erreicht 5 |
| 22 | 4 | 0 | nie | nein (nur 4) |

Vier von fünf Läufen hätten nach der neuen Zählung archiviert; nach der alten **kein einziger**.

**Mechanikprüfung** an einem erzeugten offenen Fund, ausdrücklich als solche gekennzeichnet: nach 3 und 4 Generationen offen, nach 5 archiviert; der Status steht auf `archiviert`, der Ursprung nennt Regel und Anlass. Archivierte Funde werden späteren Kandidaten nicht mehr vorgelegt, bleiben aber in der Datenbank (nicht gelöscht).

**Ein eigener Fehler, korrigiert und protokolliert:** Meine Prüfung löste die echte Regel am echten Bestand aus und archivierte dabei **zwei echte Normtests** mit (`norm_k2081_bericht`, `norm_k2082_bericht`) — sie erfüllten die Bedingung ebenfalls. Das ist ein Nebeneffekt der Messung, kein Laufergebnis; beide auf `offen_norm` zurückgesetzt (`immun.archivierung_zurueckgenommen`). Lehre für Fassung 6, im Beleg notiert: **Eine Mechanikprüfung, die eine echte Regel am echten Bestand auslöst, muss ihren Wirkungsbereich vorher eingrenzen — sonst verändert die Messung den gemessenen Gegenstand.**

**Deine Bezugsgröße zu den Doppelungen** ist im Beleg `18-anklaeger-vielfalt.txt` nachgetragen, mit Warnhinweis zur Vergleichbarkeit: Lauf 20 → 0 erkannt / 7 unbemerkt, größte Gruppe **5**; Lauf 22 → 6 erkannt / 0 unbemerkt, größte Gruppe **1**. Zeile bleibt gerissen, Grenze bleibt bei 20 %.

Kosten 0,42 € von 10 €. Zwischenbericht: 45 Dateien, Prüfsumme `01ba7297b7dea138fa7f05168c7f583ce680cf2e3a9c4be48b81dcf4d15239d8`.

Weiter mit Punkt 7: Projektgedächtnis-Differenz an den drei strittigen Fällen.
```

### V0353 · 19.09.2026 23:55:26 CEST · Philipp · Nachricht id 2688 · Sitzung `20260918_225920_3e614670` · 915 B

```text
Dein Fehler bei der Mechanikprüfung ist dieselbe Klasse wie der Probenabfall in den Gedächtnissen, eine Ebene höher: Prüfung und Betrieb teilen denselben Raum, und die Messung hat ihren Gegenstand verändert. Für Fassung 6 fasse ich beides in einen Satz: Eine Prüfung darf den geprüften Bestand nicht verändern — ihr Wirkungsbereich wird vorher eingegrenzt, und was sie hinterlässt, wird vor der nächsten Messung zurückgenommen und protokolliert. Dass du die zwei Normtests zurückgesetzt und das protokolliert hast, statt es stillschweigend zu lassen, ist der Unterschied zwischen einem Fehler und einem verdeckten Fehler. Die Archivierungszahlen belegen die Änderung sauber — 4 von 5 Läufen nach neuer Zählung, 0 nach alter, und Lauf 22 mit 0 angenommenen Generationen zeigt am deutlichsten, warum der alte Bezug an einem Werk nahe dem Höchstwert nie greifen konnte. Weiter mit Punkt 7, dann 8.
```

### V0354 · 19.09.2026 23:55:40 CEST · Hermes-Zwischentext · Nachricht id 2689 · Sitzung `20260918_225920_3e614670` · 117 B

```text
Punkt 7: die drei strittigen Fälle. Beide Ableitungen auf denselben Kandidatensatz anwenden und einzeln entscheiden.
```

### V0355 · 19.09.2026 23:56:46 CEST · Hermes-Zwischentext · Nachricht id 2699 · Sitzung `20260918_225920_3e614670` · 161 B

```text
Alle drei Fälle sind jetzt entscheidbar. Ich prüfe den dritten genauer — dort sind sich beide Ableitungen einig, und das Biotop hat ihn trotzdem ausgeführt.
```

### V0356 · 19.09.2026 23:57:14 CEST · Hermes-Zwischentext · Nachricht id 2703 · Sitzung `20260918_225920_3e614670` · 92 B

```text
Punkt 7 entschieden. Jetzt Punkt 8: den `logmuehle`-Verfassungsentwurf im Bericht abdrucken.
```

### V0357 · 19.09.2026 23:57:34 CEST · Hermes-Zwischentext · Nachricht id 2707 · Sitzung `20260918_225920_3e614670` · 68 B

```text
Alle acht Punkte erledigt. Jetzt der Abschlussbericht des Nachlaufs.
```

### V0358 · 20.09.2026 00:00:28 CEST · Hermes · Nachricht id 2717 · Sitzung `20260918_225920_3e614670` · 2529 B

```text
**Nachlauf zu Phase 3 abgeschlossen.** Alle neun Punkte abgearbeitet, Ordner versiegelt und von außen abrufbar (HTTP 200 geprüft).

Abholadresse, vollständig und unverlinkt, in eigener Zeile:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/BERICHT.md

Prüfsumme des Ordners (SHA-256 über DATEIEN.txt, 52 Dateien): `a8bf8eb381e5e28c2fc30153933834a56f2d4f127964e6490aef72f2ce02ece1`

**Die neun Punkte:**
1. **Vier Eichproben** am versiegelten Gegenstand, mechanisch über den Syntaxbaum — 4 von 4 bestanden.
2. **Fund-Neubewertung** als Organ, mit der Ankläger-Logik statt eigenem Regex; Übernahme erzwingt Nachmessung.
3. **Abbruch** als benannter Befehl (CLI + Route, 401 ohne Token) — nicht als Gate-Ausnahme.
4. **Doppelungsschlüssel = Behauptung**; Zeile 8 neu gemessen: 68,5 % (Lauf 13), 63,6 % (20), **54,5 %** (22) — **bleibt gerissen**, Grenze bleibt 20 %.
5. **Artgedächtnis speichert Muster**; 18 Muster nachabstrahiert für 0,003 € — **Torzeile erfüllt**, 2 von 5 Richtungen in Lauf 23, 0 erfunden.
6. **Archivierung nach Generationen**: 4 von 5 Läufen hätten archiviert, nach alter Zählung keiner; Mechanikprüfung belegt.
7. **Die drei strittigen Fälle: 0 von 3 durchgerutscht.** Zwei beruhten auf meiner gröberen Ableitung, einer auf einem Weg aus dem verworfenen Lauf 16. **Die Zahl des Biotops war richtig, meine Nachrechnung war falsch** — die Torzeile Projektgedächtnis aus Phase 3 ist erfüllt, nicht „teilweise".
8. **Verfassungsentwurf `logmuehle`** vollständig im Bericht (Abschnitt 9), Prüfsumme `0ce7f865…`, zur Bestätigung.
9. **Vier Tor-2-Probenzeilen** nachgemessen: 4 von 4, mit gehärteten Proben.

**Eigene Fehler, alle gefunden bevor sie als Ergebnis galten:** erste Regelfassung der Fundprüfung hätte 9 von 20 Normtests zu Funden hochgestuft (Lauf 16 von der anderen Seite); geratener Anbietername ließ 19 Abstürze als „nicht übertragbar" erscheinen; die Archivierungs-Mechanikprüfung archivierte zwei echte Normtests mit (zurückgesetzt, protokolliert); der erste Probendurchlauf zeigte vier „bestanden" aus drei falschen Gründen.

**Kosten: 0,44 € von 10 € (207 Aufrufe).** Vorspann je Lauf gemessen: 9 Kammerläufe, 4 Modellaufrufe, 0,0057 €, 44 s.

**Offen für Fassung 6:** Zeile 8 (Ankläger nennt Behauptung vorab, bei Wiederholung kein Angriff), werkübergreifender Mindestanteil im Artgedächtnis-Block. Sechs Sätze aus diesem Nachlauf stehen in Abschnitt 12 des Berichts.
```

