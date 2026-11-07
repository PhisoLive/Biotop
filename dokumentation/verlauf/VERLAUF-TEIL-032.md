# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 032 von 054

- Einträge V0563 bis V0575. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0563 · 21.09.2026 02:14:34 CEST · Philipp · Nachricht id 9105 · Sitzung `20260921_015554_e79a4a0f` · 86026 B · Stück 3 von 3

```text
**Zweck:** Das Biotop soll an jedem Werk arbeiten können, nicht nur an Python-Werken, die Hermes selbst geschrieben hat. Bisher kennt es zwei Werke derselben Art: `lagerhaus` (856 Zeilen) und `logmuehle` (482 Zeilen), beide Python, beide pytest, beide klein, beide aus Hermes' Feder, beide reine Ablauflogik ohne Oberfläche und ohne Zustand. Jedes Mal, wenn eine neue Werkart dazukam, traten sofort neue Messgerätfehler auf. Der Breitentest holt diese Fehler dort ein, wo sie nichts kosten — statt sie alle auf einmal an einem echten Werk zu treffen.

**Was universell heißt und was nicht (Fassung 7):** Keine endliche Zahl von Testwerken beweist, dass das nächste funktioniert. Erreichbar ist belegte Breite: In welchen Arten von Werken trägt das Biotop nachweislich? Eine Behauptung über alle Werke wird nie aufgestellt, auch nicht nach dem letzten Testwerk.

**Herkunft der Werke:** Hermes baut alle Testwerke selbst (Entscheidung Philipps, 21.09.2026), mit versiegelten Schwächen wie bei `lagerhaus` und `logmuehle`. Ausnahme in T4, siehe dort.

**Die vier Dimensionen, die bisher ungeprüft sind**, und das Werk, das sie abdeckt:

**T3 — andere Sprache und andere Werkzeugkette.** TypeScript oder JavaScript, ~1.500–2.500 Zeilen, 4–5 Bereiche, eigene Testsammlung (vitest oder jest), eigenes statisches Prüfwerkzeug. Betrifft: Syntaxbaum-Zerlegung, Mutantenerzeugung, Testläufer-Anbindung, Ergebnisleser (die JUnit-Parser, in denen bereits zwei Nachweislücken saßen), Sicherheitsprüfung ohne Bandit, Kammer mit anderer Laufzeitumgebung. **Das ist der größte Sprung und kommt zuerst**, weil er die meisten Organe berührt.

**T4 — Größe, fremder Stil, fehlende Tests, echte Altlasten.** Python, ~6.000–10.000 Zeilen, 8–12 Bereiche, **ohne vorhandene Testsammlung**, mit gewachsenen Altlasten (toter Code, Doppelungen, uneinheitliche Muster) statt nur versiegelter Einzelschwächen. Hermes erzeugt es über ein anderes Modell als sein eigenes, damit Stil und Struktur nicht seine sind. Betrifft: Landkarte in Zoomstufen (bisher nie nötig — beide Übungswerke passten ganz in einen Aufruf), Generation 0 mit echter Arbeit (bisher fing sie 40 von 40 und 42 von 42, weil die Werke bereits dicht getestet waren), Vertragsableitung an fremden Mustern, Kosten bei größerem Kontext.

**T5 — Werk mit Oberfläche.** HTML, CSS und JavaScript ohne Rahmenwerk, ~1.000–1.800 Zeilen. Betrifft: Was ist „besser", wenn Laufzeit fast nichts aussagt? Hier tragen zum ersten Mal die weichen Maße und die Jury die Entscheidung — bisher waren alle fünf Jury-Fälle einstimmig und die Uneinigkeit musste gestellt werden. Auch: Wie misst man ein Werk, das man ansehen muss?

**T6 — Zustand und Außenwelt.** Python, ~2.000–3.000 Zeilen, mit SQLite-Datenbank, Dateiablage und einer Schnittstelle nach außen, die in der Kammer stillgelegt ist. Betrifft: Kammer-Abschottung (kein Netz), Wiederholbarkeit der Messung bei Zustand, Referenzlast mit Vorbedingungen, und die bereichsweise Rauschmessung an einem Werk, dessen Laufzeit von Datenbankzugriffen abhängt.

**Reihenfolge:** T3, T4, T5, T6 — vom größten Bruch zum kleinsten. Jedes Werk ist ein eigener Auftrag mit eigenem Abschlussordner.

**Was nach jedem Testwerk zu erwarten ist:** Neue Messgerätfehler. Das ist der Zweck, kein Scheitern. Sie werden nach den Grundsätzen 7 bis 9 behandelt: reparieren, was im Kernpfad liegt; benennen und listen, was außerhalb liegt; ein Reviewdurchgang.

**Tor 4 — je Testwerk:**
- Aufnahme: Werk gebaut, Bau- und Testlauf, versiegelte Schwächen hinterlegt (bei T4 stattdessen eine unabhängig erhobene Liste der Altlasten mit Bezugsgröße).
- Generation minus eins: Rauschmessung mit Sperren je Bereich, Eichgegenstand gewählt und versiegelt, 4 von 4 Proben bestanden **und 4 von 4 Gegenproben an der vorgesehenen Zusicherung fehlgeschlagen** (Grundsatz 8), Eichkosten getrennt ausgewiesen.
- Generation 0: Mutantenfang ≥ 80 von 100 nicht-äquivalenten, äquivalente vorab mit Beleg aussortiert. Bei T4 zusätzlich: die Testsammlung wird erst erzeugt — Zahl der Tests vorher/nachher.
- Schwächen: ≥ 80 % der versiegelten Schwächen behoben nach „behoben heißt verschwunden" (3.5); bei T4 stattdessen Kernmaß vorher/nachher an der Altlastenliste.
- Kein Rückschritt: 0 von n angenommenen Generationen mit gesunkenem hartem Maß.
- Halluzinationsprobe: im unveränderten Vergleichsbereich 0 angenommene Änderungen ohne Maßgewinn.
- Doppelungsanteil unter 20 % der vom Ankläger erzeugten Tests.
- Sättigung oder Budgetabbruch dokumentiert — der Lauf endet nie still.
- Verbundausfall (Fassung 7): Fällt ein Modell des Verbunds aus (Ablehnung, Zeitüberschreitung, leere Antwort), wird das als Ausfall gezählt und **nie als Beitrag**; belegt an mindestens einem echten oder gestellten Ausfall je Testwerk, mit der Ausfallmeldung im Protokoll.
- Ein Reviewdurchgang; Abschlussordner trägt die Torzeilen, nicht jede Zwischenstufe.

**Abnahme des Breitentests — die Sättigungsregel (Entscheidung Chat-Claude, 21.09.2026):** Philipp hat die Zahl der Testwerke offengelassen. Eine feste Zahl wäre willkürlich; deshalb entscheidet dasselbe Prinzip, nach dem das Biotop selbst aufhört: **Der Breitentest ist abgeschlossen, wenn zwei aufeinanderfolgende Testwerke neuer Art durchlaufen, ohne einen neuen Messgerätfehler zu erzeugen.** Erzeugt T3 noch Fehler und T4 und T5 keine mehr, ist nach T5 Schluss; erzeugen alle vier weiterhin Fehler, kommen T7 und T8 dazu — Hermes schlägt die nächste ungeprüfte Dimension vor, Philipp entscheidet. Die Zahl wird nicht vorher festgelegt und nachher nicht verhandelt.

**Budget:** je Testwerk 10 €, hart. Schätzung nach den bisherigen Messungen: T3 und T5 je 1–4 €, T4 5–15 € wegen Größe und Generation 0, T6 2–6 €. Alle Zahlen sind Schätzungen und werden am Werk gemessen; die bisherigen Schätzungen von Chat-Claude lagen durchweg zu hoch.

### Phase 5 — Erstes echtes Werk

**Werk: noch nicht bestimmt.** Die Wahl trifft Philipp nach dem Breitentest. Kriterien, die sich aus Phase 1 bis 4 ergeben haben:
- **Es steht still.** Niemand baut parallel daran, solange das Biotop daran arbeitet — sonst ist das eingefrorene Maß am ersten Tag überholt, und weder Lazarus noch die Prüfsummen fangen das auf.
- **Es hat Tests, oder es lässt sich welche bauen.** Ohne Messgerät kein Lauf (Satz 6).
- **Sein Maß ist klar.** Je mehr vom Kernmaß auf harte Zahlen entfällt und je weniger auf Geschmack, desto belastbarer der Lauf.
- **Ein Fehlschlag ist nicht teuer.** Kein laufender Betrieb, keine Kunden, kein Geld im Spiel — beim ersten echten Werk noch nicht.
- **Seine Art ist im Breitentest belegt.** Ein Werk in einer Sprache oder Bauart, die das Biotop noch nie gesehen hat, ist kein erstes echtes Werk.

**Vorbedingungen, wenn das Werk gewählt ist:**
1. **Verfassung des Werks** — schreibt Philipp; Hermes legt einen Entwurf vor. Sie enthält, was das Werk ist, wofür es da ist, was nie passieren darf, die Tauschregeln und den **tragenden Pfad** für den Eichgegenstand (3.5). Ohne diesen Eintrag wartet das Organ und der Lauf beginnt nicht.
2. **Aufnahme und Landkarte** als eigener Abschnitt mit eigenem Bericht, bevor eine Generation läuft — hier zeigt sich, ob die Landkarte bei der Größe dieses Werks trägt.
3. **Generation minus eins** und **Generation 0** als eigene Abschnitte mit eigenen Budgets.
4. **Freigaben ausschließlich durch Philipp**; die Vollmacht für Übungswerke gilt hier nicht. Hier beginnt das echte Geschmacksgedächtnis.

**Tor 5** wird gesetzt, wenn das Werk feststeht — Kernmaß, harte Grenzen und Bezugsgrößen hängen am Werk und werden nicht vorher erfunden.

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

*Ende des Dokuments. Fassung 7, 21.09.2026. Fassungen 1 bis 6 sind durch diese Fassung ersetzt; die jeweils höchste Fassung gilt. Fortschreibung als Fassung 8 bei grundlegenden neuen Erkenntnissen.*
```

### V0564 · 21.09.2026 02:14:40 CEST · Philipp · Nachricht id 9106 · Sitzung `20260921_015554_e79a4a0f` · 1145 B

```text
Phase 4 ist neu gefasst — lies INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md vollständig, Fassung 6 ist ersetzt. Das Handelssystem ist als Phase-4-Werk gestrichen: Es war eine nie bestätigte Vorentscheidung von mir, und alle Bezugsgrößen daraus (237.000 Zeilen, 17 Dienste, 135 Testfehlschläge) sind ungültig. Stattdessen Breitentest an mehreren Testwerken, die du selbst baust (Entscheidung Philipps), Abnahme nach der Sättigungsregel in Abschnitt 8 — nicht nach einer festen Zahl. Auftrag: T3 — ein TypeScript- oder JavaScript-Werk, 1.500–2.500 Zeilen, 4–5 Bereiche, eigene Testsammlung (vitest oder jest), eigenes statisches Prüfwerkzeug, mit versiegelten Schwächen wie bei lagerhaus; dann der vollständige Durchlauf nach Tor 4 je Testwerk, einschließlich der neuen Zeile zum Verbundausfall. Erwarte neue Messgerätfehler — das ist der Zweck, kein Scheitern; behandle sie nach den Grundsätzen 7 bis 9: Kernpfad reparieren, Außenliegendes benennen und listen, ein Reviewdurchgang. Budget 10 € hart, Abschlussordner laeufe/biotop-t3-typescript/, Endmeldung mit vollständiger Abholadresse als ganze URL und Prüfsumme.
```

### V0565 · 21.09.2026 02:20:28 CEST · Hermes-Zwischentext · Nachricht id 9107 · Sitzung `20260921_015554_e79a4a0f` · 371 B

```text
Fassung 7 ersetzt Fassung 6; der Auftrag ist jetzt ausschließlich T3, nicht das Handelssystem und nicht automatisch der nächste Breitentest. Ich führe T3 durch den bestehenden Biotop-Kern, halte die 10 € als gemeinsame Grenze über mögliche Laufabbrüche hinweg und dokumentiere neue Messgerätfehler sowie jede offene oder gescheiterte Torzeile im Abschlussordner.
```

### V0566 · 21.09.2026 02:25:39 CEST · Hermes-Zwischentext · Nachricht id 9151 · Sitzung `20260921_015554_e79a4a0f` · 295 B

```text
T3 wird `versandwerk`: ein TypeScript-Übungswerk mit fünf Bereichen, Vitest und eigener statischer Prüfung. Die Generationen- und Mentor-Vollmacht gilt dafür; die Verfassungsbestätigung ist davon getrennt und liegt mir für T3 noch nicht vor.

MEDIA:/root/biotop-t3/VERFASSUNG-T3-ENTWURF.md
```

### V0567 · 21.09.2026 02:29:00 CEST · Hermes-Zwischentext · Nachricht id 9157 · Sitzung `20260921_015554_e79a4a0f` · 756 B

```text
Der vollständige Entwurf liegt jetzt im Prüfkanal; **5 von 5 Dateien** wurden über HTTPS bytegleich abgerufen.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/VERFASSUNG-T3-ENTWURF.md

Dateiliste:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/DATEIEN.txt

Manifest:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/MANIFEST.sha256

Ordnerprüfsumme: `dc556d9c4a53fe099877694310e7af6d6dfbb2b4632d2674cf5d83a1c0952406`

Bau und Eichung gehen weiter; der evolutionäre Lauf bleibt bis zur Bestätigung gesperrt.
```

### V0568 · 21.09.2026 03:15:37 CEST · Hermes · Nachricht id 9547 · Sitzung `20260921_015554_e79a4a0f` · 171 B

```text
Werk- und Adapterbau laufen weiter; die Verfassung liegt Chat-Claude vollständig im Prüfkanal vor, und der evolutionäre Lauf bleibt bis zu seiner Bestätigung gesperrt.
```

### V0569 · 21.09.2026 03:22:29 CEST · Hermes-Zwischentext · Nachricht id 9600 · Sitzung `20260921_015554_e79a4a0f` · 306 B

```text
Der Regressionslauf ist rot: **338 von 344 gesammelten Tests bestanden, 4 fehlgeschlagen, 2 übersprungen**; die TypeScript-Adaptertests waren ausgenommen. Ich kläre die vier Fehlschläge am vorhandenen Output, ohne Prüfbedingungen abzuschwächen; das ist noch kein Abschlussreview und keine Torfreigabe.
```

### V0570 · 21.09.2026 03:30:21 CEST · Hermes · Nachricht id 9678 · Sitzung `20260921_015554_e79a4a0f` · 229 B

```text
Die vier Regressionsfehler sind geklärt und gezielt erneut ausgeführt: **4 von 4 bestanden**, ohne Produktsperren abzuschwächen; der vollständige Integrationsnachweis bleibt offen, ebenso Chat-Claudes Verfassungsbestätigung.
```

### V0571 · 21.09.2026 03:32:41 CEST · Philipp · Nachricht id 9686 · Sitzung `20260921_015554_e79a4a0f` · 365 B · 2 gleiche Zeilen zusammengefasst

```text
Die Abholadresse des Verfassungsentwurfs fehlt weiterhin — schick sie als ganze URL in eigener Zeile (laeufe/biotop-t3-typescript/verfassung-entwurf-01/, mit DATEIEN.txt und Prüfsumme). Ohne sie kann Chat-Claude nichts bestätigen, und der evolutionäre Lauf bleibt gesperrt. Bau, Eichung und Integrationsnachweis von versandwerk laufen davon unabhängig weiter.
```

### V0572 · 21.09.2026 03:34:30 CEST · Hermes · Nachricht id 9694 · Sitzung `20260921_015554_e79a4a0f` · 966 B

```text
**Vollständiger Verfassungsentwurf:**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/VERFASSUNG-T3-ENTWURF.md

**Dateiliste:**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/DATEIEN.txt

**Manifest:**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/MANIFEST.sha256

**Prüfsummendatei:**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/PRUEFSUMME-ORDNER.txt

**Ordnerprüfsumme — SHA-256 des Manifests:**
`dc556d9c4a53fe099877694310e7af6d6dfbb2b4632d2674cf5d83a1c0952406`

Der evolutionäre Lauf bleibt bis zu Chat-Claudes Bestätigung gesperrt; Bau, Eichung und Integrationsnachweis von `versandwerk` gehen unabhängig davon weiter.
```

### V0573 · 21.09.2026 03:35:35 CEST · Philipp · Nachricht id 9696 · Sitzung `20260921_015554_e79a4a0f` · 1617 B · 2 gleiche Zeilen zusammengefasst

```text
Verfassung bestätigt mit drei Auflagen, die vor dem Lauf einzuarbeiten und als verfassung-02 zu versiegeln sind — danach ist der evolutionäre Lauf freigegeben, ohne weitere Rückfrage. Der Entwurf ist an der entscheidenden Stelle besser als die Vorgänger: Satz 2 nennt die TypeScript-eigenen Wege (Function, globale Objekte, Prototype) statt die Python-Verfassung zu übersetzen. Auflage 1 zu Satz 4: Ergänze das Verbot geteilter Veränderung — kein Bereich verändert Object.prototype, eingebaute Prototypen oder gemeinsam genutzte Standardwerte, auch nicht innerhalb des eigenen Bereichs; Satz 2 deckt nur den Eingabeweg, und ein Bereich, der einen anderen über einen geteilten Prototyp still beeinflusst, ist genau die Nebenwirkung über Bereichsgrenzen, die Tor 4 fangen soll. Auflage 2 zu Satz 3: „Ganze Cent" legt die Einheit fest, nicht die Richtung — setz das Rundungsverfahren fest (welche Richtung, an welcher Stelle der Rechnung, und dass Zwischenergebnisse nicht mehrfach gerundet werden); ohne diese Festlegung kann jede Generation anders runden und jedes Mal „korrekt" sein, und genau daran ist der lagerhaus-Vertrag über Staffel- und Grundpreis gescheitert. Auflage 3 zu Satz 8: Nimm den Verbundausfall auf — Ablehnung, Zeitüberschreitung oder leere Antwort eines Modells zählt als Ausfall und nie als Beitrag, belegt an mindestens einem echten oder gestellten Ausfall in diesem Testwerk (Tor 4, Fassung 7). Satz 6 ohne Sicherheits-Tauschregel bleibt wie von dir gewählt — strenger als bei lagerhaus und logmuehle, konsistent begründet, das ist deine Entscheidung und sie steht.
```

### V0574 · 21.09.2026 03:39:46 CEST · Hermes-Zwischentext · Nachricht id 9714 · Sitzung `20260921_015554_e79a4a0f` · 507 B · 2 gleiche Zeilen zusammengefasst

```text
Ich arbeite die drei Auflagen in `verfassung-02` ein und lasse den veröffentlichten Entwurf unverändert. Als Rundungsregel lege ich fest: einmaliges Half-up auf ganze Cent am Endpreis jeder Sendung nach allen Zuschlägen und Rabatten, keine Zwischenrundung, Sammelsummen aus den gerundeten Sendungsendpreisen; Satz 6 bleibt wörtlich unverändert. Nach der Versiegelung entfällt die Verfassungs-Wartesperre — der Lauf beginnt erst, wenn auch die technischen Startbedingungen ausgeführt bestanden sind.
```

### V0575 · 21.09.2026 03:43:00 CEST · Hermes-Zwischentext · Nachricht id 9729 · Sitzung `20260921_015554_e79a4a0f` · 875 B · 2 gleiche Zeilen zusammengefasst

```text
`verfassung-02` ist versiegelt: **6 von 6 Dateien per HTTPS bytegleich**, die Sätze 3, 4 und 8 geändert, Satz 6 unverändert.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-02/VERFASSUNG-T3.md

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-02/DATEIEN.txt

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-02/MANIFEST.sha256

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-02/PRUEFSUMME-ORDNER.txt

**Ordnerprüfsumme:** `b6cd20338db3eea15cf9d6009aa02e4d50ca537626ceb87f255df79329ccce2e`

Die Verfassungsfreigabe ist damit erfüllt; die technischen Startnachweise bleiben noch zu erbringen.
```

