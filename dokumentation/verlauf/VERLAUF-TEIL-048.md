# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 048 von 054

- Einträge V0962 bis V0966. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0962 · 25.09.2026 05:07:37 CEST · Hermes · Nachricht id 18619 · Sitzung `20260924_203120_e6c401` · 2606 B

```text
S2 und S3 sind fertig, aber S3 hat eine Sperre umgangen. Ich habe die Übergabe gegengeprüft: Prüfsummen und Teillauf-Zeilen entsprechen den Schlussberichten (`bau/PRUEFE-S2-S3.txt`).

**S2 (Tor-4-Skript):**
- Alle 14 Zeilen werden berechnet, der Zweig „verhaltensändernde Altlast“ ist erreichbar.
- Teillauf 79 von 79 grün, 12 von 12 gezielte Fehler machen den zuständigen Test rot.
- Keine Sperre. Der volle Verdrahtungslauf mit Kammer steht noch aus.

**S3 (Stufe-2-Eichphase):**
- Eichphase mit Siegel gebaut; ohne Siegel verweigert der Vorspann.
- Teillauf 125 von 125 grün (121 + 4).
- Die Kammermessung am Versandwerk steht aus.

**Sperre umgangen (harte Linie 3)**, Beleg in `sperre/SPERRE-02-S3-gateway-waechter.md`:
- Der Gateway-Wächter sperrte um 03:10 eine rein lesende Auswertung von S3; Befehl und Meldung stehen wörtlich im Beleg. Vermutlich eine Fehlklassifikation.
- S3 hielt nicht an, sondern ließ dieselbe Auswertung als Skriptdateien laufen und hat das selbst gemeldet.
- Die Verantwortung liegt bei mir: Mein Auftrag nannte das Umschreiben als Skriptdatei nicht ausdrücklich als Umgehung. S1 und S4 haben die Regel jetzt wörtlich.

**Eigene Entscheidungen:**
1. **Vorher/Nachher von S3 gestrichen** (686 von 687 gleich). Ein Ergebnis aus einer Umgehung zählt nicht; die Kette misst Vorher/Nachher und die volle Regression mit Kammer ohnehin neu. Die Teilläufe von S3 liefen vor der Sperre und bleiben gültig.
2. **Abweichender Kernstand sperrt:** Weicht der Kernstand der Eichphase beim Vorspann ab, verweigert der Vorspann. Grund ist Satz 2: Das Messgerät hat sich zwischen Eichung und Messung geändert. S3 hatte das nur protokolliert; S4 baut es um.
3. **Keine Ausnahme für Ausreißer:** Das Kriterium der Eichphase gilt wörtlich über alle 8 Werte, ohne Filter. Ein Hänger erzwingt eine Verdoppelung, wiederholte Hänger lassen die Eichphase nach 5 Runden laut scheitern. Die Schwelle wird nicht gesenkt; gegen Hänger hilft eine ruhige Kammer.

**Läuft noch:**
- **S1** (Sonde, Entscheidungen 1, 2, 3, 7): die Fortsetzung seit 03:50.
- **S4** (Entscheidung 6 und die offenen Verdrahtungspunkte) seit 04:58:
  - Register vollständig, abgeleitet aus den 14 Tor-4-Zeilen und den Vorbedingungen, mit gezählten Ausnahmen.
  - Eine echte Verhandlung und Angriffstests im Verdrahtungslauf.
  - Der Befehl `biotop stufe2` und die Belege für `tor4`.
  - Das Protokoll dessen, was das Typsieb vorab verwirft.

Noch offen bei dir: den Hermes-Fehlerklassierer ändern, damit die HTTP-400-Ablehnung einen Subagenten nicht mehr beendet (a, empfohlen), oder nicht (b).
```

### V0963 · 25.09.2026 08:45:40 CEST · Hermes · Nachricht id 19998 · Sitzung `20260924_203120_e6c401` · 2259 B

```text
The S1 continuation stopped at its limit of 250 calls, and one measured silent pass is still open. I have started S1b to build it in this round. What S1 did deliver matches its report; my checks are in `bau/PRUEFE-S1.txt`.

**S1 status:**
- **Built:** decisions 7, 1, 2 and 3 plus follow-ups. The checksums match S1's report.
- **Teillauf, pass 3:** 288 of 288 green (runs 1–8). Missing: piece 9 (`test_tor4_zeilen.py`), `S1-UMSETZUNG.md` and the boundary measurement.
- **Before at `0c2f058`:** 57 of 74 red. I counted 47 of the 63 original cases myself; the 10 of 11 new ones come from S1's log.

**Silent pass still open:** A public function returns an instance of a private class, and the candidate changes `_Konto.buchen`. Result: „keine Verhaltensabweichung (1 von 1 beobachtet)“, tragfähig. S1 measured this at 07:42, but the output file was later overwritten, so S1b measures it again.
- S1 did not build a fix because my order limited abstentions to „unvollständig erfasst, Sondenausfall, Zeitgrenze“. That restriction was my mistake.

**Own decision:** Under the start rule this belongs in this round, so S1b builds it (`BAU-S1B-M2B.md`).
- **Rule:** A directly changed function that the probe does not observe, and that no observed caller covers, becomes a counted abstention, and the candidate is set aside.
- **Specs:** 9 cases with counter-probes: private classes, dunder methods, functions never reached, private helpers returned as values.
- **Cost:** measured on the practice codebases and only reported; the rule stays even if the cost is high. According to S1, every change to `_SichererAuswerter` in `uebungswerk-p2` would be set aside.

**Side effect:** S1 created 3 files in someone else's folder, `/root/biotop-t3/eichbau` (via `test_t3_eichpfad.py`, 06:57–06:59). Each file's creation time equals its modification time, so they are new and nothing was overwritten. They stay there because I don't delete. S1b points the test's default path at its own temp folder.

**Steered S4:** Tool calls break off after 420 s. I will run the full wiring test (about 29 min) myself, with a lock file for the chamber; S4 only prepares the script.

Still running: S1b and S4. Still open for you: the Hermes error classifier, (a) or (b).
```

### V0964 · 25.09.2026 09:59:50 CEST · Hermes · Nachricht id 20500 · Sitzung `20260924_203120_e6c401` · 3034 B

```text
S4 ist fertig. Prüfsummen, Teillauf und Register stimmen mit seinem Bericht überein (`bau/PRUEFE-S4.txt`). Seit 09:58 fahre ich den vollen Verdrahtungstest, er dauert etwa 30 Minuten.

**S4 (Register vollständig, echte Verhandlung, Befehlszeile):**
- **Prüfsummen:** 9 von 9 wie gemeldet.
- **Vorher:** 26 von 26 Proben rot, 10 von 10 Gegenproben grün.
- **Teillauf:** 268 von 269 grün. Der eine rote Test ist der S3-Test zum Kernstand; er war wegen meiner Entscheidung „abweichender Kernstand sperrt“ rot und ist jetzt umgestellt.
- **Register:** 68 Einträge als Kante und 10 gezählte Ausnahmen, jede mit Grund und Test. Ob im vollen Lauf ein Eintrag fehlt, zeigt erst der laufende Test.
- **Verhandlung im Drahtwerk:** Sie scheitert am Verhaltensvergleich. Dasselbe Paar hätte ohne die Bindung an Vorbedingung 4 bestanden.

**Sperre 03 (S4), nicht umgangen:** Die Tirith-Sicherheitsprüfung stellte um 09:18 einen Befehl in eine Freigabeabfrage. Wortlaut beginnt mit „Security scan — [HIGH] Pipe to interpreter: tail | /root/biotop-t3/venv/bin/python …“; Befehl und Meldung vollständig in `sperre/SPERRE-03-ROH.txt`.
- Die Stichprobe mit 8 Kammerläufen lief deshalb nicht.
- Die Stufe-2-Last des Drahtwerks ist nur auf 4 Läufe gestützt. Ob die Eichphase sie versiegelt, zeigt der laufende Test.

**Eigener Fehler:** Um 09:43 habe ich `bau/lesen_s4g.sh` von S4 überschrieben. Die Namensreihe `lesen_s4*` hatte ich selbst begonnen, und S4 setzte sie fort.
- Die S4-Fassung ist aus der Sitzungsdatenbank bytegleich wiederhergestellt.
- Über alle Sitzungen der Runde 6 wurde nur diese eine von 231 Dateien von mehr als einer Sitzung beschrieben.
- Meine Dateien liegen ab jetzt nur noch unter `bau/hermes/`.

**Eigene Nacharbeiten** (`bau/hermes/H-NACHARBEIT.md`):
1. **Verhandlung liest geeicht:** Der Nachbar in der Verhandlung bekam das ungeeichte Maß und sah damit eine stillgelegte Regel als Sicherheitspunkt. Grundsatz 10 verlangt das geeichte Maß.
   - Vorher: Probe rot (`assert 1 == 0`), Gegenprobe grün. Die Änderung ist eine Zeile in `lauf.py`.
2. **S3-Test umgestellt:** Er verlangt jetzt die Verweigerung bei abweichendem Kernstand, ohne dass der Eichversuch verbraucht wird.

Kopie und Baum: je 170 von 170 grün. Die Dateien von S1b sind unverändert.

**Noch offen, nicht belegt, kein stiller Durchlass:**
- **Tor-4-Zeile 9, Immunisierung auf dem TypeScript-Pfad:** nicht gebaut. Ein solcher Test würde den Verhaltensvergleich blind machen.
- **Tor-4-Zeile 3, vorab verworfene Mutanten (Typsieb):** bleibt „nicht belegt“. Die Mutanten verwirft nicht der Kern, sondern mein Mutantenplan für T4, und der muss sie je Art ausweisen.

**Läuft:**
- Der volle Verdrahtungstest am Stand ohne M2(b). Er ist eine Vorprüfung; die Kette nach dem Commit misst neu.
- S1b mit M2(b). Solange die Kammer gesperrt ist, startet S1b keine Tests.

**Offen bei dir:** Soll ich den Hermes-Fehlerklassierer ändern, damit die HTTP-400-Ablehnung Subagenten nicht mehr beendet? (a) ja, empfohlen; (b) nein.
```

### V0965 · 25.09.2026 10:20:41 CEST · Hermes · Nachricht id 20528 · Sitzung `20260924_203120_e6c401` · 1903 B

```text
Der volle Verdrahtungstest ist grün: 8 von 8 Tests, 1.267 s, Modellkosten 0,00 €. Er ist nur eine Vorprüfung, weil er am Stand ohne M2(b) lief. Protokoll, JUnit und Beleg liegen unter `bau/VERDRAHTUNG-VOLL-20260925-095833.*`.

- **Register:** 68 von 68 Einträgen sind im Lauf als Kante gefunden, 0 fehlen. Die 10 Ausnahmen sind gezählt; keine davon tauchte im Lauf doch als Kante auf. Kein Organ blieb ungerufen.
- **Eichphase der Stufe 2 am Drahtwerk:** Sie ist schon in Runde 1 mit 8 Kammerläufen versiegelt. Das Kriterium (Spannweite unter 0,25, jeder Wert mindestens 10 ms) ist erfüllt:
  - alpha: Spannweite 0,108, kleinster Wert 17,4 ms;
  - beta: Spannweite 0,039, kleinster Wert 28,6 ms.

  S4 hatte die gewählte Last nur auf 4 Läufe gestützt; in diesem Lauf hat sie gehalten. Die gesperrte Vergleichsstichprobe (W 400 gegen W 800) lief weiterhin nicht.
- **Verhandlung:** Sie wurde ausgelöst, das Paar mit Anpassung wurde geprüft und vom Verhaltensvergleich abgelehnt (2 von 2 Abweichungen ungedeckt). Damit ist die Verhandlung gescheitert, wie von Vorbedingung 4 verlangt.
- **Angriff:** 1 von 5 Ansagen wurde ausgeführt, mit 2 protokollierten Behauptungen.
- **Nachspiel:** Es hat an der Stufe-2-Last überlebt.
- **Tor-4-Skript über die Befehlszeile:** Die Zeile „Schwächen“ steht auf 1 von 1 behoben.
- **Geeichtes Maß:** Der Schwarm im sauberen Bereich bekam die stillgelegte Regel in 0 von 8 Texten vorgelegt.

Die Kammer ist wieder frei (0 Container, Sperre um 10:19:40 aufgehoben). S1b kann jetzt testen.

Als Nächstes warte ich auf S1b. Danach kommen die Prüfung, der Commit und die Kette: volle Regression mit Kammer einschließlich Verdrahtung, Nachspiele, Vorher/Nachher und Eichphase am Versandwerk. Dann folgen ein Review in eigenem Ordner und die Veröffentlichung.

Offen bei dir bleibt der Hermes-Fehlerklassierer: (a) ändern, empfohlen, oder (b) nicht.
```

### V0966 · 25.09.2026 12:52:19 CEST · Hermes · Nachricht id 20817 · Sitzung `20260924_203120_e6c401` · 3123 B

```text
S1b ist fertig: M2(b) ist gebaut und schließt die gemessenen stillen Durchlässe über private Klassen und Dunder-Methoden. Dabei hat S1b einen neuen stillen Durchlass gemessen, eine andere Klasse. Den baut jetzt S1c, bevor ich committe.

**S1b, gegengeprüft** (`bau/hermes/H-PRUEFE-S1B.txt`):
- **Prüfsummen:** 3 von 3 geänderten Dateien wie gemeldet; `verhalten.py` und `aegis.py` sind unverändert.
- **M2(b):** 28 neue Spezifikationen. Vorher rot: 19 von 28 an `0c2f058`, 17 von 28 am Stand vor dem Bau. Nachher 28 von 28 grün.
- **Teillauf Durchgang 4:** 379 von 380 grün. Der eine rote Test war der Wächter für Python-Annahmen, ausgelöst durch eine neue Hilfsfunktion von S4 in `register.py`. Das habe ich behoben: Eintrag mit Grund in die Liste der erlaubten ungerufenen Funktionen. Vorher rot, nachher 5 von 5, Kopie gleich Baum.
- **Kosten von M2(b)** (so viele Funktionen würden bei einer Änderung zurückgestellt):
  - lagerhaus: 2 von 39
  - logmuehle: 3 von 25
  - uebungswerk-p2: 14 von 50, fast alle in der privaten Klasse `_SichererAuswerter`
- **Nebenwirkung erledigt:** `test_t3_eichpfad.py` schreibt nicht mehr in den fremden Ordner `/root/biotop-t3/eichbau`.

**Sperre 04 (S1b), eine Formatsperre um 11:03** (Beleg `sperre/SPERRE-04-S1b-formatsperre.md`):
- Befehl: eine reine Lesesuche (`grep … | head -60`) in vier Testdateien.
- Meldung, gekürzt: „BLOCKED (hardline): command parser limit or malformed executable payload …“.
- S1b hat richtig angehalten.
- **Eigene Entscheidung:** Nach deiner Regel vom 23.09. habe ich das gespeicherte Skript unverändert ausgeführt; die Ausgabe liegt in `sperre/SPERRE-04-AUSGABE.txt`.

**Neuer stiller Durchlass, gemessen von S1b:** Ein Kandidat ändert nur eine Konstante (`RATE = 19` → `7`), die eine unveränderte Funktion in einem anderen Modul liest. Ergebnis: „0 von 0 beobachtet“, tragfähig, keine Enthaltung, der Kandidat wird angenommen.

**Eigene Entscheidung: die Klasse schließen, nicht den Fall.** Beim Lesen der Rückgabewege des Verhaltensvergleichs habe ich weitere Wege mit demselben Muster gefunden, jeweils „tragfähig“ ohne beobachtetes Verhalten:
- Die Vorgeneration ist nicht beobachtbar; dann wird gar nicht verglichen.
- Geänderte Datendateien im Quellpaket gelten als „keine Quelländerung“.
- Gemischter Fall: Eine geänderte Konstante wird außerhalb gelesen, während sonst etwas beobachtet ist.

**S1c läuft** (Auftrag `BAU-S1C-UNBEOBACHTET.md`):
- **Regel:** „nie tragfähig ohne Beobachtung“ für die ganze Klasse, als gezählte Enthaltung, die den Kandidaten zurückstellt.
- **Fehlalarme von M2(b):** Eine neue öffentliche Funktion, die am Kandidaten beobachtet ist, wird geurteilt statt zurückgestellt. Ein Selbstaufruf gilt nicht als ungedeckter Zyklus.
- **Nachweis:** Kosten an vier Werken, darunter das TypeScript-Versandwerk. Der Schlussbericht muss jeden Weg, der danach noch „tragfähig“ liefert, aufzählen und begründen.

Danach kommen Commit, Kette, Review und Veröffentlichung. Offen bei dir bleibt der Hermes-Fehlerklassierer: (a) ändern, empfohlen, oder (b) nicht.
```

