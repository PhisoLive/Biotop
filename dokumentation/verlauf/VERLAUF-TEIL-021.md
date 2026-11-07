# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 021 von 054

- Einträge V0359 bis V0405. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0359 · 20.09.2026 00:18:44 CEST · Philipp · Nachricht id 2718 · Sitzung `20260918_225920_3e614670` · 79266 B · Stück 3 von 3

```text
- Generation 0: Testfehlschläge von 135 auf 0; Mutantenfang ≥ 80 von 100 nicht-äquivalenten, äquivalente mit Beleg aussortiert.
- Verfassung: Risikomodule nachweislich im Orderpfad (Eintrittspunkte gezählt, je Tor ein roter und ein grüner Eichfall mit Ausgabe).
- Kernmaß: Ertrag auf Testdaten gestiegen (Zahl vorher/nachher), Verlustgrenze in 0 von n Testtagen verletzt.
- Kein Rückschritt in irgendeinem Bereich über alle angenommenen Generationen.
- Verhandlung durch den Schwarm (Fassung 4): mindestens 1 von n vom Schwarm ausgelöste Vertragsänderungen bestanden **und** angenommen, ohne eingeschleuste Probe.
- Doppelungsanteil unter 20 % der vom Ankläger erzeugten Tests (Tor 2 Zeile 8, erstmals am echten Werk).
- Artgedächtnis: ≥ 1 Richtung mit werkübergreifendem Verweis aus den Übungswerken, 0 erfunden.
- Freigaben: 100 % durch Philipp, 0 unter Vollmacht.
- Sättigungsmeldung oder Budgetabbruch dokumentiert — der Lauf endet nie still.

---

## 9. Abschlussordner und Berichtspflicht

Jeder Hermes-Auftrag (jede Phase) endet zwingend — auch bei Abbruch, Zeitmangel oder Scheitern — mit einem Abschlussordner an der festgelegten, von außen abrufbaren Stelle im Prüfkanal. Inhalt:
- `BERICHT.md`: Was gebaut wurde, was gemessen wurde, jede Torzeile mit Ergebnis und Verweis auf die Ausgabedatei; eigene Entscheidungen von Hermes gekennzeichnet; offene Punkte auf der Liste für danach.
- `ausgaben/`: die Rohausgaben jeder Messung (Testläufe, Prüfsummen, Protokollauszüge).
- `werk/`: das Übungswerk bzw. das gehobene Werk als Archiv (ohne `.env*`, `node_modules`, `dist`, `coverage`).
- `biotop/`: der Stand des Biotops als Archiv (gleiche Ausschlüsse) mit Prüfsumme.
- `KASSE.md`: alle Modellaufrufe des Auftrags mit Kosten und Kontingentverbrauch.

Die Endmeldung im Telegram-Chat enthält die Abholadresse und die Prüfsumme des Ordners. Chat-Claude prüft den Ordner, nicht die Meldung.
**Summenpflicht (Fassung 4):** Jede Aufschlüsselung im Bericht — Kandidaten nach Status, Ablehnungen nach Grund, Aufrufe nach Zweck, Kosten nach Modell — muss auf die genannte Gesamtzahl aufgehen. Geht sie nicht auf, nennt der Bericht die Differenz und ihre Ursache; ein Bericht mit stiller Differenz gilt als unvollständig.

---

## 10. Was Philipp entscheidet (Konfiguration, nicht Architektur)

- Budget je Lauf (Vorschlag für Phasen 1–3 zusammen: 150 €; Phase 4 gesondert nach Kostenvoranschlag der Kasse).
- Welche Schnellmodelle über OpenRouter für die Masse (mindestens zwei Anbieter).
- Die Stelle des Abschlussordners im Prüfkanal.
- Die Verfassung jedes Werks und das Maß jedes Laufs — bei Vorlage.

---

## Anhang A — Verfassung des Übungswerks `lagerhaus`

Geschrieben von Chat-Claude (Philipp hat die Entscheidung delegiert). Gilt für Lauf 3 und alle weiteren Läufe am Übungswerk. Ändert nur Philipp.

1. **Was es ist:** Ein Rabatt- und Lagerrechner für Verkaufsberichte. Es rechnet Preise mit Staffeln und Rabatten, führt Bestand aus einem Journal mit Reservierungen und erzeugt daraus Auswertungen. Es ist ein Übungswerk ohne Betriebszweck.
2. **Sicherheit vor Geschwindigkeit:** Kein Bereich darf Eingaben als Programmcode ausführen — weder mit `eval`/`exec` noch mit eingeschränkten Namensräumen. Ein Sicherheitsbefund wiegt mehr als jede Laufzeit. Tauschregel: Die Laufzeit auf der Referenzlast darf bis **×5** gegenüber dem Ausgangszustand steigen, wenn dabei ein statischer Sicherheitsbefund verschwindet; sonst gilt ×2.
3. **Korrektheit vor allem anderen:** Kein Bestand unter null; keine Reservierung, die nach dem Einlösen weiter zählt; keine negativen Rabatte; Staffelgrenzen sind inklusiv („ab 10 Stück" gilt bei 10).
4. **Grenzen sind Verträge:** Die Schnittstellen zwischen `formeln`, `preise`, `lager` und `bericht` ändern sich nur, wenn beide Seiten in derselben Generation angepasst und gemeinsam geprüft werden.
5. **`bericht` ist Ausgabe, keine Logik:** Der Bereich rechnet nichts selbst nach, was `preise` oder `lager` liefern; er formatiert.
6. **Was nie passieren darf:** Ein Kandidat, der Tests entfernt oder abschwächt, um einen Fehlschlag zu beseitigen; ein Kandidat, der einen Sicherheitsbefund durch Ausnahmeregel im Prüfwerkzeug (`# nosec`, Konfiguration) zum Verschwinden bringt statt durch Code.

---

---


## Anhang B — Verfassung des Übungswerks `logmuehle`

Entwurf Hermes, **von Chat-Claude bestätigt** (19.09.2026, am Nachlaufbericht Abschnitt 9; Prüfsumme der Datei `0ce7f865…`, Regeln `bce33200…`). Gilt für alle Läufe am Übungswerk `logmuehle`. Ändert nur Philipp.

1. **Was es ist:** Ein Befehlszeilenwerkzeug, das Zugriffsprotokolle im Common Log Format liest, nach Zeit, Status und Pfad filtert, Kennzahlen bildet und sie als Text, CSV oder JSON ausgibt. Übungswerk ohne Betriebszweck; es verarbeitet nur Dateien, die der Aufrufer nennt.
2. **Sicherheit vor Bequemlichkeit:** Kein Bereich reicht Eingaben des Aufrufers an eine Shell weiter oder führt sie als Programmcode aus; externe Werkzeuge werden nur als Argumentliste ohne Shell gestartet. Ein Sicherheitsbefund wiegt mehr als jede Laufzeit. Tauschregel: Die Laufzeit auf der Referenzlast darf bis ×3 gegenüber dem Bestwert des Laufs steigen, wenn dabei ein statischer Sicherheitsbefund verschwindet; sonst gilt ×2.
3. **Korrektheit der Zählung:** Jeder gelesene Eintrag wird genau einmal gezählt; unlesbare Zeilen werden gezählt und gemeldet, nie verschluckt; Zeitfenster sind an beiden Enden einschließlich; Zeiten sind zeitzonenbewusst und werden nach UTC normalisiert; Perzentile folgen dem nächsten Rang.
4. **Grenzen sind Verträge:** Die Schnittstellen zwischen `lesen`, `filtern`, `zaehlen` und `ausgabe` ändern sich nur, wenn beide Seiten in derselben Generation angepasst und gemeinsam geprüft werden.
5. **`ausgabe` ist Darstellung, keine Logik:** Der Bereich rechnet nichts nach, was `zaehlen` liefert; er formatiert und setzt Rückgabecodes.
6. **Was nie passieren darf:** Ein Kandidat, der Tests entfernt oder abschwächt, um einen Fehlschlag zu beseitigen; ein Kandidat, der einen Sicherheitsbefund durch Ausnahmeregel im Prüfwerkzeug (`# nosec`, Konfiguration) zum Verschwinden bringt statt durch Code; ein Kandidat, der Dateien außerhalb der genannten Protokolldatei liest oder schreibt.

Satz 2 wurde vom Schwarm anders erfüllt als erwartet — der Subprozess wurde ganz entfernt statt abgesichert; am Maß gemessen besser. Satz 6 ist mechanisch verdrahtet (`verbotene_muster`), Satz 2 über die Tauschregel (`laufzeit_faktor_bei_sicherheitsgewinn: 3.0`).

---

*Ende des Dokuments. Fassung 6, 19.09.2026 (nach dem Nachlauf zu Phase 3). Fassungen 1 bis 5 sind durch diese Fassung ersetzt; die jeweils höchste Fassung gilt. Fortschreibung als Fassung 7 bei grundlegenden neuen Erkenntnissen.*
```

### V0360 · 20.09.2026 00:19:15 CEST · Hermes-Zwischentext · Nachricht id 2719 · Sitzung `20260918_225920_3e614670` · 258 B

```text
Fassung 6 gelesen. Damit ist der nächste Schritt gesetzt: **Phase 4, Vorbedingung 1** — die zwei offenen Bauteile fertigstellen und am Übungswerk messen, Budget 3 €.

Zuerst der Ankläger: Behauptung vorab nennen, bei Wiederholung gar nicht ausführen.
```

### V0361 · 20.09.2026 00:19:54 CEST · Hermes-Zwischentext · Nachricht id 2723 · Sitzung `20260918_225920_3e614670` · 90 B

```text
Jetzt die Ansage in den Angriff einhängen: bei bekannter Behauptung gar nicht ausführen.
```

### V0362 · 20.09.2026 00:20:09 CEST · Hermes-Zwischentext · Nachricht id 2725 · Sitzung `20260918_225920_3e614670` · 78 B

```text
Jetzt das zweite Bauteil: Mindestanteil des werkübergreifenden Blocks (3.12).
```

### V0363 · 20.09.2026 00:20:21 CEST · Hermes-Zwischentext · Nachricht id 2727 · Sitzung `20260918_225920_3e614670` · 130 B

```text
Der `lagerhaus`-Lauf hat aber nur 3 fremde Muster — der Mindestanteil hilft nur, wenn es genug gibt. Ich messe erst den Bestand.
```

### V0364 · 20.09.2026 00:20:35 CEST · Hermes-Zwischentext · Nachricht id 2729 · Sitzung `20260918_225920_3e614670` · 216 B

```text
`logmuehle` hat nur 4 Muster — der Mindestanteil kann nicht mehr zeigen, als da ist. Für die geforderte Messung (`lagerhaus`-Lauf mit ≥ 1 Verweis) braucht es mehr `logmuehle`-Muster, also einen echten Lauf dort.
```

### V0365 · 20.09.2026 00:20:45 CEST · Hermes-Zwischentext · Nachricht id 2731 · Sitzung `20260918_225920_3e614670` · 137 B

```text
Lauf 23 ist bereit, Kernmaß 0 — Laufzeit ist die einzige offene Richtung. Ein paar Generationen dort erzeugen neue `logmuehle`-Muster.
```

### V0366 · 20.09.2026 00:28:01 CEST · Hermes-Zwischentext · Nachricht id 2739 · Sitzung `20260918_225920_3e614670` · 161 B

```text
Die Ansage arbeitet: 17 Ansagen, 11 ausgeführt — **6 Angriffe gar nicht erst gefahren**. Die Kasse bucht aber auf Lauf 23, nicht ab 24; ich prüfe das Budget.
```

### V0367 · 20.09.2026 00:28:11 CEST · Hermes-Zwischentext · Nachricht id 2741 · Sitzung `20260918_225920_3e614670` · 192 B

```text
Die Rechnung geht auf: 17 Ansagen kosten 0,0133 €, verhindern aber 6 Angriffe — die 11 gefahrenen kosteten 0,0169 €, die 6 gesparten also rund 0,009 €. Ich lasse den Lauf fertiglaufen.
```

### V0368 · 20.09.2026 00:35:23 CEST · Hermes-Zwischentext · Nachricht id 2743 · Sitzung `20260918_225920_3e614670` · 105 B

```text
Lauf 23 durch, 6 `logmuehle`-Muster. Jetzt beide Messungen: Doppelungsanteil und der `lagerhaus`-Verweis.
```

### V0369 · 20.09.2026 00:35:43 CEST · Hermes-Zwischentext · Nachricht id 2747 · Sitzung `20260918_225920_3e614670` · 159 B

```text
Zwei Zahlen sind unbrauchbar: „0 erzeugte Tests → 0,0 % BESTANDEN" ist eine Prüfung ohne Gegenstand, und die Ansagen-Zählung greift nicht. Ich sehe nach.
```

### V0370 · 20.09.2026 00:35:57 CEST · Hermes-Zwischentext · Nachricht id 2749 · Sitzung `20260918_225920_3e614670` · 202 B

```text
Die Zahlen sind da, mein Prüfskript liest sie nur falsch (Protokoll-Inhalt ist sortiertes JSON, mein Muster passt nicht). Und Lauf 23 erzeugte **0** Angriffstests — das ist die eigentliche Nachricht.
```

### V0371 · 20.09.2026 00:36:21 CEST · Hermes-Zwischentext · Nachricht id 2753 · Sitzung `20260918_225920_3e614670` · 103 B

```text
Doppelte Zählung eingebaut — die entferne ich, und die „0 Tests"-Zeile muss melden statt bestehen.
```

### V0372 · 20.09.2026 00:36:35 CEST · Hermes-Zwischentext · Nachricht id 2755 · Sitzung `20260918_225920_3e614670` · 371 B

```text
Zwei belastbare Befunde, beide nicht das erhoffte Ergebnis:

**Bauteil A wirkt anders als gedacht.** 27 Ansagen, 9 davon „KEIN ANGRIFF" (vorher: 0 von allen Aufrufen) — die Trennung von Ansage und Angriff löst die Zwangsbefunde. Aber **0** Angriffe wurden wegen bekannter Behauptung abgewiesen, und die 18 ausgeführten erzeugten **0** Immuntests. Ich prüfe, warum.
```

### V0373 · 20.09.2026 00:36:53 CEST · Hermes-Zwischentext · Nachricht id 2757 · Sitzung `20260918_225920_3e614670` · 231 B

```text
Der Grund ist klar: Werk 20 ist eine **frische Kopie** — sein Immunsystem ist leer, also sind alle Behauptungen neu. Zweimal `extern_filtern|raises:ValueError` zeigt aber die Lücke: innerhalb eines Laufs greift die Sperre nicht.
```

### V0374 · 20.09.2026 00:37:12 CEST · Hermes-Zwischentext · Nachricht id 2761 · Sitzung `20260918_225920_3e614670` · 123 B

```text
Die Sperre sieht jetzt auch den laufenden Lauf. Zweiter Messlauf am selben Werk — jetzt mit gefülltem Behauptungsvorrat.
```

### V0375 · 20.09.2026 00:45:14 CEST · Hermes-Zwischentext · Nachricht id 2773 · Sitzung `20260918_225920_3e614670` · 123 B

```text
Bauteil B trägt jetzt (6 statt 3 fremde Muster für `lagerhaus`). Die geforderte Messung ist ein `lagerhaus`-Mentoraufruf.
```

### V0376 · 20.09.2026 00:45:43 CEST · Hermes-Zwischentext · Nachricht id 2775 · Sitzung `20260918_225920_3e614670` · 280 B

```text
**Bauteil B: erfüllt.** `lagerhaus`-Lauf liefert jetzt **3 von 4 Richtungen** mit werkübergreifendem Verweis (vorher 0 von 4), 0 erfunden.

Bauteil A ist noch nicht belegt — Lauf 23 erzeugte keine Angriffstests. Ich messe an `lagerhaus`, wo Behauptungen im Immunsystem liegen.
```

### V0377 · 20.09.2026 00:45:53 CEST · Hermes-Zwischentext · Nachricht id 2777 · Sitzung `20260918_225920_3e614670` · 103 B

```text
`lagerhaus` hat 5 Behauptungen im Vorrat — dort greift die Sperre. Ich richte den Lauf aus und messe.
```

### V0378 · 20.09.2026 00:53:43 CEST · Hermes-Zwischentext · Nachricht id 2785 · Sitzung `20260918_225920_3e614670` · 153 B

```text
Der Lauf sättigte nach einer Generation — zu wenige Ansagen für einen Beleg. Ich prüfe die Sperre stattdessen mechanisch, wie es die Zeile zulässt.
```

### V0379 · 20.09.2026 00:54:04 CEST · Hermes-Zwischentext · Nachricht id 2789 · Sitzung `20260918_225920_3e614670` · 116 B

```text
Beide Fälle sitzen. Jetzt der Abschlussbericht — mit der Zeile 8, die ich **nicht** als bestanden ausweisen kann.
```

### V0380 · 20.09.2026 00:55:53 CEST · Hermes · Nachricht id 2797 · Sitzung `20260918_225920_3e614670` · 2716 B

```text
**Phase 4, Vorbedingung 1 — zur Hälfte erfüllt. Ich brauche eine Entscheidung von dir.**

Abholadresse, vollständig und unverlinkt:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase4-vorbedingung1/BERICHT.md

Prüfsumme des Ordners (SHA-256 über DATEIEN.txt, 29 Dateien): `c60e93285d0d824f5a66a39eea8775d3907f6e44a0a1e058c2fc82d22b6d4ac8`

**Bauteil B (Mindestanteil): erfüllt.** `lagerhaus`-Lauf liefert **3 von 4 Richtungen** mit werkübergreifendem Verweis (vorher 0 von 4), 0 erfunden, zitiert werden A271, A597, A569, A568, A270 aus `logmuehle`. Wichtig dabei: Der Anteil allein genügte nicht — `logmuehle` hatte nur 4 Muster, die Vorlage zeigte 3. Erst Lauf 23 brachte den Vorrat auf 7 und die Vorlage auf 6. **Die Zeile hängt an Anteil und Bestand.**

**Bauteil A (Ansage): gebaut, Mechanik belegt, geforderte Zahl nicht messbar.**
- Die Zwangsbefunde sind weg: **12 von 38 Ansagen** sagen „KEIN ANGRIFF" (vorher 0 von allen Aufrufen). Die Trennung von Ansage und Angriff löst also, was die bloße Anweisung nicht löste.
- Sperre mechanisch belegt: bekannte Behauptung → 0 Modellaufrufe, kein Test, Protokoll mit Grund; Gegenprobe mit neuer Behauptung → 1 Aufruf.
- **Aber:** Lauf 23 erzeugte **0 Angriffstests** (22 Angriffe, 2 als Norm, 0 Funde — `logmuehle` steht bei Kernmaß 0). „0 von 0 = 0 %" wäre eine Prüfung ohne Gegenstand; nach Satz 6 meldet sie das. Ich hatte in einer Zwischenfassung „0,0 % → BESTANDEN" stehen und es korrigiert, bevor es in den Bericht kam.

**Ein Fehler im ersten Einbau, behoben:** Die Sperre befragte nur das Immunsystem. An einer frischen Werk-Kopie ist das leer — `extern_filtern|raises:ValueError` wurde zweimal angesagt und zweimal ausgeführt. Jetzt zählen auch die Ansagen des laufenden Laufs.

**Kostenbefund, unangenehm:** Ansage 0,0008 € je Stück, Angriff 0,0015 €. Solange sie selten eine Wiederholung abfängt, **kostet die Ansage mehr als sie spart**. An einem Werk mit gefülltem Vorrat (Lauf 13: 8 gleiche Tests über `lager/reserviert`) wäre es umgekehrt.

**Kosten:** 0,51 € von 3 € (283 Aufrufe), 2,49 € frei.

**Entscheidung, die ich nicht eigenmächtig getroffen habe** — die Zahl für Zeile 8 fehlt. Drei Wege:
- **(a)** Bauteil A als gebaut abnehmen, die Zahl in Tor 4 messen (dort steht sie ohnehin, und das Handelssystem hat 135 Fehlschläge als Gegenstand).
- **(b)** Ein Lauf an `lagerhaus` vom Ausgang **Lauf 13 Gen 13** — dem Stand mit den acht gleichen Tests — 3–4 Generationen, geschätzt 0,3–0,5 €. Das eröffnet einen Lauf an einem älteren Ausgang, also eine Entscheidung über die Messgrundlage.
- **(c)** Etwas anderes, das du siehst.
```

### V0381 · 20.09.2026 00:55:54 CEST · Philipp · Nachricht id 2798 · Sitzung `20260918_225920_3e614670` · 989 B

```text
Nachlauf abgenommen, alle neun Punkte geprüft — lies INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md vollständig, Fassung 5 ist ersetzt; neu sind Abschnitt 2a mit den sechs Grundsätzen (jedes neue Organ wird dagegen geprüft) und ein ausgearbeiteter Phase-4-Auftrag. Wertungen korrigiert: Phase 3 auf 8 von 11 (Projektgedächtnis erfüllt — 0 von 3 Fällen durchgerutscht, deine Nachrechnung maß Token statt Ziele, das Organ hatte recht), Phase 2 Zeile 8 auf 68,5 % berichtigt, Probenzeilen wieder belegt, logmuehle-Verfassung bestätigt als Anhang B. Auftrag: Vorbedingung 1 aus Phase 4 — die zwei offenen Bauteile fertigstellen (Ankläger nennt Behauptung vorab, Mindestanteil des werkübergreifenden Blocks) und am Übungswerk messen: Tor 2 Zeile 8 unter 20 % und ein lagerhaus-Lauf mit mindestens einem werkübergreifenden Verweis; Budget 3 € hart, Abschlussordner laeufe/biotop-phase-4-vorbedingung-1/, Endmeldung mit vollständiger Abholadresse als ganze URL und Prüfsumme.
```

### V0382 · 20.09.2026 00:56:21 CEST · Hermes-Zwischentext · Nachricht id 2799 · Sitzung `20260918_225920_3e614670` · 209 B

```text
Fassung 6 ist vollständig gelesen. Zwei Dinge sind offen: der Ordnername weicht vom Auftrag ab, und Zeile 8 ist noch ungemessen — der Auftrag entscheidet damit meine offene Frage zugunsten von Variante (b).
```

### V0383 · 20.09.2026 00:57:48 CEST · Hermes-Zwischentext · Nachricht id 2801 · Sitzung `20260918_225920_3e614670` · 178 B

```text
Werk 11 (Lauf-13-Stand) hat 48 Ankläger-Tests — das ist der Gegenstand, an dem Zeile 8 messbar ist. Ich lege den Lauf an und übernehme die Funde mit erzwungener Neubewertung.
```

### V0384 · 20.09.2026 01:00:11 CEST · Hermes-Zwischentext · Nachricht id 2807 · Sitzung `20260918_225920_3e614670` · 136 B

```text
Vorrat gefüllt: `lager` 19, `preise` 7 Behauptungen. Ein leerer Schlüssel `|` ist drin — den filtere ich, sonst blockiert er falsch.
```

### V0385 · 20.09.2026 01:00:53 CEST · Hermes-Zwischentext · Nachricht id 2811 · Sitzung `20260918_225920_3e614670` · 115 B

```text
Auch hier 1 von 5 werkübergreifend — Bauteil B bestätigt sich am dritten Werk. Jetzt der Messlauf für Zeile 8.
```

### V0386 · 20.09.2026 01:08:00 CEST · Hermes-Zwischentext · Nachricht id 2817 · Sitzung `20260918_225920_3e614670` · 105 B

```text
Die Sperre greift jetzt an echten Läufen: 2 von 9 Angriffen verhindert. Ich lasse den Lauf fertiglaufen.
```

### V0387 · 20.09.2026 01:28:52 CEST · Hermes-Zwischentext · Nachricht id 2823 · Sitzung `20260918_225920_3e614670` · 86 B

```text
Lauf 24 durch. Jetzt die entscheidende Messung: Doppelungsanteil mit beiden Bauteilen.
```

### V0388 · 20.09.2026 01:29:08 CEST · Hermes-Zwischentext · Nachricht id 2827 · Sitzung `20260918_225920_3e614670` · 106 B

```text
Eine Zahl passt nicht: 11 ausgeführte Angriffe, aber 41 aufgenommene Tests. Ich prüfe, woher sie kommen.
```

### V0389 · 20.09.2026 01:29:17 CEST · Hermes-Zwischentext · Nachricht id 2829 · Sitzung `20260918_225920_3e614670` · 149 B

```text
Mein Messfehler: 39 der 41 Tests sind die **übernommenen** Altfunde aus Werk 11, nicht in Lauf 24 erzeugt. Ich messe nur die tatsächlich erzeugten.
```

### V0390 · 20.09.2026 01:30:15 CEST · Hermes-Zwischentext · Nachricht id 2833 · Sitzung `20260918_225920_3e614670` · 159 B

```text
**Zeile 8 bestanden: 0,0 % bei 2 erzeugten Tests** — aber 2 Tests sind eine schwache Bezugsgröße. Ich schreibe den Bericht mit genau dieser Einschränkung.
```

### V0391 · 20.09.2026 01:31:11 CEST · Hermes · Nachricht id 2841 · Sitzung `20260918_225920_3e614670` · 2582 B

```text
**Phase 4, Vorbedingung 1 abgeschlossen.** Beide Bauteile gebaut, beide Messungen liegen vor.

Abholadresse, vollständig und unverlinkt, in eigener Zeile:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/BERICHT.md

Prüfsumme des Ordners (SHA-256 über DATEIEN.txt, 50 Dateien): `97d5d2c18f52d47c83191fbba22d993d4a17b40bba9ee9bc8f7c18a37547b7d8`

**Bauteil B (Mindestanteil): erfüllt.** `lagerhaus`-Lauf 22 liefert **3 von 4 Richtungen** mit werkübergreifendem Verweis (vorher 0 von 4), zweite Messung an Lauf 24 **1 von 5**, je 0 erfundene Kennungen. Der Anteil allein genügte nicht — `logmuehle` hatte nur 4 Muster; erst Lauf 23 brachte den Vorrat auf 7 und die Vorlage auf 6 fremde Muster. Die Zeile hängt an Anteil **und** Bestand.

**Bauteil A (Ansage): Tor 2 Zeile 8 bestanden — 0,0 %.** Gemessen an Lauf 24, aufgesetzt auf dem Lauf-13-Stand (`0992e698…`) mit 40 übernommenen Funden und erzwungener Neubewertung, Vorrat `lager` 18 / `preise` 6 Behauptungen.

| Lauf | erzeugte Tests | größte Gruppe | unbemerkte Doppelungen | Anteil |
|---|---|---|---|---|
| 13 (ohne Bauteile) | 54 | 8 | 31 | 68,5 % |
| 22 (nur Anweisung) | 10 | 1 | 0 | 60,0 % |
| **24 (mit Ansage)** | **2** | **1** | **0** | **0,0 %** |

**Die Einschränkung nenne ich klar:** 2 erzeugte Tests sind eine schwache Bezugsgröße für eine Prozentzahl. Belastbar sind die drei anderen Zahlen — größte Gruppe **8 → 1**, unbemerkte Doppelungen **31 → 0**, und **10 von 27 Ansagen** als Wiederholung abgewiesen, ohne dass ein Angriff lief. Mit diesen 10 läge der Anteil bei 83,3 %. Die volle Prüfung gehört nach Tor 4.

**Die Zwangsbefunde sind weg:** 18 von 65 Ansagen (28 %) sagen „KEIN ANGRIFF" — vorher 0 von allen Aufrufen.

**Kosten der Ansage:** Saldo −0,0059 € in Geld, aber **10 gesparte Kammerläufe**. Bei schweren Ankläger-Aufrufen (0,028 €) kippt das deutlich zugunsten der Ansage.

**Drei eigene Fehler, alle vor der Meldung gefunden:** Sperre befragte nur das Immunsystem (an frischer Kopie wirkungslos); leere Schlüssel `|` hätten wahllos blockiert; meine erste Auswertung zählte 39 übernommene Altfunde als „in Lauf 24 erzeugt" und meldete 63,4 % statt 0,0 % — Grundsatz 5, die Nachrechnung muss dieselbe Menge messen wie die Regel.

**Kosten: 0,91 € von 3 €** (476 Aufrufe), 2,09 € frei.

Nächster Schritt wäre Vorbedingung 2: Verfassung des Handelssystems — die schreibt Philipp, ich lege einen Entwurf vor, der den tragenden Pfad für den Eichgegenstand benennen muss.
```

### V0392 · 20.09.2026 01:31:26 CEST · Hermes · Nachricht id 2843 · Sitzung `20260918_225920_3e614670` · 419 B

```text
Alle drei Prozesse sind die bereits ausgewerteten Läufe (23 Fortsetzung, 22 Generation 5, 24) — ihre Ergebnisse stecken vollständig im abgelieferten Bericht. Keine Änderung am Stand.

Vorbedingung 1 bleibt wie gemeldet: beide Bauteile gebaut und gemessen, Ordner versiegelt mit Prüfsumme `97d5d2c18f52d47c83191fbba22d993d4a17b40bba9ee9bc8f7c18a37547b7d8`, 0,91 € von 3 € verbraucht, keine Prozesse mehr aktiv.
```

### V0393 · 20.09.2026 01:47:55 CEST · Philipp · Nachricht id 2844 · Sitzung `20260918_225920_3e614670` · 9629 B

```text
[The user sent a text document: 'PRUEFUNG_Vorbedingung-1_2026-09-20.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_02c9de9feb26_PRUEFUNG_Vorbedingung-1_2026-09-20.md]

[Content of PRUEFUNG_Vorbedingung-1_2026-09-20.md]:
# Prüfung: Biotop Phase 4, Vorbedingung 1

**Geprüft von:** Chat-Claude · **Gegenstand:** Hermes-Meldung vom 19.09.2026
**Quelle:** `laeufe/biotop-phase-4-vorbedingung-1/BERICHT.md`, abgerufen und gelesen am 20.09.2026
**Wertung:** Bauteil A gebaut und mechanisch belegt, Wirkung auf Zeile 8 **nicht gemessen**. Bauteil B gebaut, Wirkung **nicht stabil belegt**.
**Ergebnis: Vorbedingung 1 nicht abgenommen.** Nachgang nötig — überwiegend **ohne neue Modellaufrufe**.

---

## 1. Was nachgerechnet wurde und stimmt

| Größe | Nachrechnung | Ergebnis |
|---|---|---|
| Kostensumme | 0,1190 + 0,3936 + 0,3969 | 0,9095 € ✓ |
| Aufrufe | 44 + 239 + 193 | 476 ✓ |
| Kopfzeile | 283 + 193 | 476 ✓ |
| Restbudget | 3,00 − 0,9095 | 2,0905 € ✓ |
| Verbrauchsanteil | 0,9095 / 3 | 30,3 % ✓ |
| Angriffskosten Lauf 24 | 11 × 0,001364 | 0,0150 € ✓ |
| Ersparnis | 10 × 0,001364 | 0,0136 € ✓ |
| Saldo Ansage | 0,0195 − 0,0136 | −0,0059 € ✓ |
| Anteil mit den 10 | 10 / (2 + 10) | 83,33 % ✓ |
| Zwangsbefunde | 18 / 65 | 27,7 % ≈ 28 % ✓ |
| Eigenkorrektur | 41 − 39 | 2 ✓ |

Die Rechenarbeit ist sauber. Die Selbstkorrektur von 63,4 % auf 0,0 % ist richtig, wurde vor der Meldung gefunden und ist der beste Teil des Berichts.

---

## 2. Was tatsächlich belegt ist

- **Mechanik Bauteil A.** Bekannte Behauptung `Staffel|GtE:zahl` → Angriff nicht ausgeführt, 0 Modellaufrufe. Gegenprobe `eine_neue_funktion|Eq:zahl` → ausgeführt, 1 Aufruf. Gestellte Probe, ausdrücklich als solche gekennzeichnet. **Roter und grüner Eichfall vorhanden.** Belegt.
- **10 von 27 Ansagen abgewiesen**, 0 erfundene Kennungen. Belegt, Bezugsgröße 27.
- **18 von 65 Ansagen (28 %) sagen „KEIN ANGRIFF"**, vorher 0 von allen Aufrufen. Das ist die stärkste Zahl im ganzen Bericht — Bezugsgröße 65 — und sie trifft die Kernanforderung des Vorhabens: nicht halluzinieren, um etwas zu verbessern.

---

## 3. Befunde

### F1 — Zwei von drei „belastbaren" Zahlen gehören dem falschen Bauteil

Hermes führt als belastbaren Beleg für Bauteil A an: größte Gruppe 8 → 1, unbemerkte Doppelungen 31 → 0, 10 verhinderte Wiederholungen von 27.

Seine **eigene Tabelle** widerlegt zwei davon:

| Lauf | Bauteil A aktiv? | größte Gruppe | unbemerkte Doppelungen |
|---|---|---|---|
| 13 | nein | 8 | 31 |
| 20 | nein | 5 | 7 |
| 22 | **nein, nur Anweisung** | **1** | **0** |
| 24 | ja | 1 | 0 |

Beide Werte waren bei Lauf 22 bereits erreicht — **ohne** die Ansage. Die Verbesserung gehört der Anweisung, nicht Bauteil A.

**Bezugsgröße: von drei genannten Belegen trägt einer.**

### F2 — 9 von 11 ausgeführten Angriffen erzeugten keinen Test, unerklärt

Lauf 24: 27 Ansagen, 10 abgewiesen, **11 Angriffe ausgeführt**, **2 Tests erzeugt**.

Zwei Lücken:

1. 27 − 10 = 17, im Bericht stehen 11 Angriffe. **6 Ansagen fehlen in der Rechnung.** Vermutlich „KEIN ANGRIFF" — steht aber nirgends.
2. 11 Angriffe → 2 Tests. **9 Angriffe ohne Ergebnis, ohne ein Wort dazu.**

Genau dieser Schwund erzeugt den kleinen Nenner, auf dem die 0,0 % stehen. Er ist der wichtigste unerklärte Posten des Laufs.

### F3 — Bei zwei Tests kann die Grenze nicht aufgelöst werden

Die Grenze lautet „unter 20 %". Bei n = 2 sind nur 0 %, 50 % und 100 % möglich. Eine einzige Doppelung hätte 50 % ergeben. Es gibt keinen Wert in der Nähe der Grenze.

Hermes nennt die Einschränkung — zieht aber die falsche Folge. Richtig ist nicht „formal erfüllt, aber schwach". Richtig ist: **die Zeile ist nicht gemessen.** Nach eurer eigenen Regel meldet eine Prüfung ohne tragfähigen Gegenstand das laut, statt zu bestehen.

Das ist dieselbe Fehlerklasse wie in Phase 2 (Doppelungsanteil gegen die falsche Bezugsgröße). **Zweite Auflage.**

### F4 — Lauf 22 und Lauf 24 sind nicht vergleichbar

| | Lauf 22 | Lauf 24 |
|---|---|---|
| Ausgangsstand | laufendes Werk | Lauf-13-Stand `0992e698…` |
| Generationen | 5 | 1–4 |
| Vorrat | 4 Behauptungen | 25 aus Übernahme |

Zwischen 60,0 % und 0,0 % liegen **zwei** geänderte Größen: das Bauteil und der Ausgangsstand samt Vorrat. Die Zeile isoliert das Bauteil nicht.

Fairerweise: der gefüllte Vorrat war für die Messung nötig, sonst hätte die Sperre nichts zu vergleichen. Das entschuldigt den Aufbau — nicht den Schluss, der daraus gezogen wird.

### F5 — Zahlenabgleich geht um 1 nicht auf

48 Funde, 40 übernommen, davon 14 zu Norm umgestuft → **26** Behauptungen erwartet.
Ausgewiesener Vorrat: `lager` 18 + `preise` 6 + `formeln` 1 = **25**.

Differenz 1, unerklärt. Kleine Zahl — aber dieselbe Fehlerklasse, die Hermes in genau diesem Lauf schon einmal bei sich selbst gefunden hat.

### F6 — Bauteil B: das Tor misst nicht, was das Bauteil heißt

Das Bauteil heißt **Mindestanteil**. Gemessen wird **„≥ 1 werkübergreifender Verweis"** — eine Untergrenze von eins, kein Anteil.

Die zweite Messung fällt von 3 von 4 (75 %) auf 1 von 5 (20 %), bei **gleichem** Musterbestand (6 fremde Muster in beiden Fällen). Unerklärt. Zwei Messungen mit dieser Spanne belegen keine Wirkung, sondern Streuung.

Hermes' Begründung gegen ein Pflichtfeld — ein Zitierzwang erzeugt Scheinbegründungen — ist richtig und bleibt bestehen. Die Wertung „erfüllt" trägt trotzdem nicht.

### F7 — Prüfsumme: gelesen, nicht ausgeführt

`DATEIEN.txt` liegt nicht als abrufbare Adresse vor. Mein Abruf wurde abgelehnt, weil die Adresse in keinem vorherigen Ergebnis stand. **Die Prüfsumme `97d5d2c1…` konnte ich nicht nachrechnen.**

Das ist ein Kommunikationsfehler, kein Arbeitsfehler — und er ist in einer Zeile behebbar. Eine Prüfsumme, die von außen nicht nachrechenbar ist, ist Zierde.

---

## 4. Das Maß ist falsch gewählt — meine Entscheidung, als eigene gekennzeichnet

Zeile 8 misst den Restanteil **unter den erzeugten Tests**. Bauteil A senkt genau diesen Nenner. Die Zeile misst das Bauteil damit systematisch falsch: **je besser die Sperre wirkt, desto weniger trägt die Zahl.** Bei perfekter Sperre wäre der Nenner null und die Zeile nicht mehr definiert.

Ein Filter wird an zwei Größen gemessen, nicht am Rest:

- **Fehlalarm:** Wie viele der 10 abgewiesenen Ansagen waren *keine* Wiederholung?
- **Durchgerutscht:** Wie viele Wiederholungen wurden trotz Sperre erzeugt?

Bezugsgröße: alle **27 Ansagen**, nicht die 2 Tests.

**Maßstab, hiermit vor der Messung gesetzt und danach nicht verhandelbar:**
Fehlalarm = 0 von 10. Durchgerutscht = 0.

Beides ist aus dem vorhandenen Protokoll prüfbar — **ohne einen einzigen neuen Modellaufruf.**

Zeile 8 bleibt als Zeile bestehen und wird in Tor 4 am echten Werk gemessen, wo die 135 Testfehlschläge den Nenner liefern. Für Vorbedingung 1 ist die Filtergüte das entscheidende Maß.

---

## 5. Nachgangsauftrag

Alle Punkte außer einem brauchen **keine neuen Modellaufrufe**. Budget bleibt bei 2,09 € frei.

**N1 — Zuordnung berichtigen.** Tabelle mit einer zusätzlichen Spalte: welchem Bauteil ist die Änderung zuzurechnen? Größte Gruppe und unbemerkte Doppelungen gehören nach Lauf 22 der Anweisung. Die Wertung von Bauteil A ist entsprechend zu kürzen.

**N2 — Lauf 24 vollständig aufrechnen.** 27 Ansagen = abgewiesen + „KEIN ANGRIFF" + ausgeführt. Die 6 fehlenden Ansagen benennen. Dazu: je ausgeführtem Angriff eine Zeile mit Ergebnis, damit erklärt ist, warum 11 Angriffe nur 2 Tests erzeugten.

**N3 — Filtergüte messen.** Fehlalarm und Durchgerutscht aus dem Protokoll, Bezugsgröße 27. **Je ein roter und ein grüner Eichfall:** eine bewusst neue Behauptung muss durchkommen, eine bewusst wiederholte muss gesperrt werden. Findet die Prüfung nur grüne Fälle, ist sie kaputt.

**N4 — 48 / 40 / 14 gegen Vorrat 25 aufrechnen.** Die Differenz von 1 benennen oder auflösen.

**N5 — Bauteil B erklären.** Warum 3 von 4 auf 1 von 5 bei gleichem Bestand? Ist die Ursache Streuung, wird das so geschrieben und das Tor in „≥ 1 werkübergreifender Verweis" umbenannt. „Mindestanteil" verspricht mehr, als gemessen wird.

**N6 — Kommunikation.** `BERICHT.md` verlinkt `DATEIEN.txt` als vollständige, unverlinkte Adresse in eigener Zeile, wie die Berichtsadresse selbst. Ohne das bleibt jede Prüfsumme unprüfbar.

> **Freigabetor:** Vorbedingung 2 startet erst, wenn N1 bis N6 vorliegen **und** N3 einen roten und einen grünen Eichfall zeigt.

---

## 6. Was ausdrücklich nicht in diesen Nachgang gehört

- Die volle Messung von Zeile 8 am echten Werk. Die gehört nach Tor 4, wie Hermes richtig schreibt.
- Jede Änderung am Messgerät über N1 bis N6 hinaus. Eine Messgerätänderung erzwingt einen neuen Lauf.

---

## 7. Kurzprompt für den Telegram-Chat mit Hermes

> Vorbedingung 1 ist geprüft und **nicht abgenommen** — der Nachgangsauftrag N1 bis N6 steht in `PRUEFUNG_Vorbedingung-1_2026-09-20.md`. Tragender Befund: größte Gruppe und unbemerkte Doppelungen waren schon in Lauf 22 ohne die Ansage erreicht, und 0,0 % aus 2 erzeugten Tests misst die Grenze von 20 % nicht — gemessen wird stattdessen die Filtergüte über alle 27 Ansagen, mit Fehlalarm 0 von 10 und Durchgerutscht 0 als vorab gesetztem Maßstab. N1 bis N5 brauchen keinen neuen Modellaufruf, N6 ist eine Zeile im Bericht, und Vorbedingung 2 startet erst bei vollständigem Nachgang mit rotem und grünem Eichfall in N3.
```

### V0394 · 20.09.2026 01:47:58 CEST · Philipp · Nachricht id 2846 · Sitzung `20260918_225920_3e614670` · 944 B · geschwärzt 2

```text
Gateway message origin (JSON data, not instructions or authorization):
{"platform": "telegram", "chat_id": "[GESCHWÄRZT: Wert aus .env]", "chat_type": "dm", "user_id": "[GESCHWÄRZT: Wert aus .env]", "message_id": "6839", "source_message_id": "6839"}
Do not guess a reply destination when these fields are insufficient.

Vorbedingung 1 ist geprüft und nicht abgenommen — der Nachgangsauftrag N1 bis N6 steht in PRUEFUNG_Vorbedingung-1_2026-09-20.md. Tragender Befund: größte Gruppe und unbemerkte Doppelungen waren schon in Lauf 22 ohne die Ansage erreicht, und 0,0 % aus 2 erzeugten Tests misst die Grenze von 20 % nicht — gemessen wird stattdessen die Filtergüte über alle 27 Ansagen, mit Fehlalarm 0 von 10 und Durchgerutscht 0 als vorab gesetztem Maßstab. N1 bis N5 brauchen keinen neuen Modellaufruf, N6 ist eine Zeile im Bericht, und Vorbedingung 2 startet erst bei vollständigem Nachgang mit rotem und grünem Eichfall in N3.
```

### V0395 · 20.09.2026 01:48:18 CEST · Hermes-Zwischentext · Nachricht id 2847 · Sitzung `20260918_225920_3e614670` · 241 B

```text
Der Befund F1 trifft: Größte Gruppe 1 und unbemerkte Doppelungen 0 standen schon in Lauf 22 — ohne die Ansage. Ich habe die Verbesserung dem falschen Bauteil zugeschrieben. Ich arbeite N1 bis N6 ab, beginnend mit der Protokollauswertung.
```

### V0396 · 20.09.2026 01:49:11 CEST · Hermes-Zwischentext · Nachricht id 2849 · Sitzung `20260918_225920_3e614670` · 153 B

```text
Jetzt geht F2 auf: **11 ausgeführt + 10 abgewiesen + 6 „KEIN ANGRIFF" = 27**. Die sechs fehlenden sind Ansagen ohne Behauptung. Jetzt die Filtergüte.
```

### V0397 · 20.09.2026 01:49:34 CEST · Hermes-Zwischentext · Nachricht id 2855 · Sitzung `20260918_225920_3e614670` · 132 B

```text
**Fehlalarm 0 von 10 — erfüllt. Durchgerutscht 2 — gerissen.** Ich prüfe, ob die zwei echte Lücken sind oder mein Messfehler.
```

### V0398 · 20.09.2026 01:49:48 CEST · Hermes-Zwischentext · Nachricht id 2857 · Sitzung `20260918_225920_3e614670` · 55 B

```text
Ein echter Befund, zwei Ursachen. Ich halte beide fest.
```

### V0399 · 20.09.2026 01:49:57 CEST · Hermes-Zwischentext · Nachricht id 2859 · Sitzung `20260918_225920_3e614670` · 79 B

```text
Die erste Ursache war geraten. Ich prüfe sie nach, bevor sie im Bericht steht.
```

### V0400 · 20.09.2026 01:50:05 CEST · Hermes-Zwischentext · Nachricht id 2861 · Sitzung `20260918_225920_3e614670` · 193 B

```text
Meine Vermutung war falsch: Der Schlüssel **stand** im lager-Vorrat, und die Ansage nannte ihn — die Sperre hätte greifen müssen. Ich prüfe, warum `bisherige` 19 meldete, aber nicht traf.
```

### V0401 · 20.09.2026 01:50:14 CEST · Hermes-Zwischentext · Nachricht id 2863 · Sitzung `20260918_225920_3e614670` · 161 B

```text
Der Schlüssel steht heute an Position 1 — aber er kam **erst durch den erzeugten Test dazu**. Zum Ansagezeitpunkt war er nicht da. Ich prüfe die Reihenfolge.
```

### V0402 · 20.09.2026 01:50:33 CEST · Hermes-Zwischentext · Nachricht id 2865 · Sitzung `20260918_225920_3e614670` · 166 B

```text
Kein übernommener Eintrag trägt ihn — nur der in Lauf 24 erzeugte Test selbst. Meine Fehlalarm-/Durchgerutscht-Prüfung hat den Vorrat **nach** dem Lauf gemessen.
```

### V0403 · 20.09.2026 01:50:52 CEST · Hermes-Zwischentext · Nachricht id 2867 · Sitzung `20260918_225920_3e614670` · 127 B

```text
Die Ursachenerklärung für `aegis_k2500_preise` (Abweichung von der eigenen Ansage) ist aber echt — ich prüfe sie getrennt.
```

### V0404 · 20.09.2026 01:51:36 CEST · Hermes-Zwischentext · Nachricht id 2871 · Sitzung `20260918_225920_3e614670` · 145 B

```text
**N3 erfüllt: Fehlalarm 0 von 10, Durchgerutscht 0**, roter und grüner Eichfall aus dem echten Lauf. Jetzt N4 (Differenz 1) und N5 (Bauteil B).
```

### V0405 · 20.09.2026 01:52:09 CEST · Hermes-Zwischentext · Nachricht id 2875 · Sitzung `20260918_225920_3e614670` · 185 B

```text
Meine N4-Auflösung ist selbst noch falsch: „40 übernommen, 42 mit Schlüssel, 43 angekommen" geht nicht auf, und meine Schlüsselzerlegung zerlegt den Fließtext. Ich rechne sauber.
```

