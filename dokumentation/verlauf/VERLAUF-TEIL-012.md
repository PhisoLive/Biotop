# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 012 von 054

- Einträge V0162 bis V0220. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0162 · 19.09.2026 16:44:37 CEST · Hermes · Nachricht id 1893 · Sitzung `20260918_225920_3e614670` · 3824 B

```text
**Zwischenstand Phase 3 — Bau abgeschlossen, Läufe noch nicht gestartet, Abschlussordner noch nicht versiegelt.**

Ich habe die Werkzeug-Iterationsgrenze dieser Sitzung erreicht. Der Ordner `laeufe/biotop-phase-3/` liegt im Prüfkanal, ist aber unvollständig (kein `BERICHT.md`, keine `DATEIEN.txt`/Prüfsumme). Alles Folgende ist Stand der Datenbank und der Ausgabedateien, nicht versiegelt.

**Nachprobe Zeile 7 — bestanden (`ausgaben/14-nachprobe-z7-ergebnis.txt`):**
- Lauf 16, Ausgang Lauf 13 Gen 13 (Prüfsumme `0992e698…` bestätigt). Fehler durch Ausführung belegt: `bericht.lagerwert` summiert Fremdwährung ungerechnet (100 USD → 100,00 statt 92,59 EUR).
- Fall 1a (Vertragsdatei ohne Benennung) abgelehnt; Fall 1b (ohne Nachbar) abgelehnt an Regression — 2 von 2.
- Fall 2: Kandidat K1164 benennt den Vertrag bericht→preise (neue Zusicherung `Katalog.wert` in EUR), Schwarm von preise liefert K1165, Paar bestanden (Protokoll #7500), Kernmaß −2 → 0, Gen 3 **angenommen und im Werk** (Tag `lauf16-gen3`, 103 von 103 Tests, lagerwert = 192,59) — 1 von 1.
- Ehrlicher Befund: K1165 rechnet Staffel- statt Grundpreis; der Vertragstest hat das nicht festgenagelt (kein Staffelfall) — Liste für danach.
- Läufe 14 und 15 verworfen nach Satz 2 F4 (Messgerät bzw. Ankläger-Ablauf während des Laufs geändert), je protokolliert.

**Zerlegung Lauf 13 (`00-lauf13-zerlegung-470.txt`):** 470 = 240 abgelehnt + 196 leer + 9 angenommen + 8 probe_abgelehnt + 6 probe_verworfen + 5 verhandlung + 5 überlebt + **1 erzeugt (K1159)** — die fehlende Eins war die zweite, nie geprüfte Verhandlungs-Anpassung (deepseek), weil K1158 zuerst bestand. Ablehnungen 240 = 110 + 64 + 53 + 8 + 4 + 1.

**Gebaut (Commit `d0d02e5`):** F4-Änderungen (Grenzmaße gegen Bestwert, Norm-Regel mit explizitem Verweis, Bandit KEIN VORSCHLAG neutral, äquivalente Mutanten vorab mit Raster-Beleg, zwei Testbau-Durchläufe, Archivierung offener Funde, Proben als echte Generation); drei Gedächtnisse (`organe/gedaechtnis.py`, mechanische Wiederholungsprüfung), Mentor (`mentor.py`, schweres Modell), Entropie (`entropie.py`), Jury (`jury.py`), Web-Oberfläche (`oberflaeche.py` + `dienst.py`); Übungswerk 2 `logmuehle` (482 Zeilen, 42 Tests, 3 versiegelte Schwächen, Prüfsumme `f004e959…`), Verfassungsentwurf, 4 Vertragsdateien, Referenzlast, Befundklasse B602.

**Tor-3-Zeilen bereits mit Ausgabe:**
- Nachprobe Z7: bestanden.
- Oberfläche (`70-tor3-oberflaeche.txt`): 18 von 18 Routen ohne Token wie gefordert, 18 von 18 Bedienelemente mit Dateipfad:Zeile, Kostenstand und Kurve über Routen sichtbar.
- Geschmack (`21-tor3-geschmack.txt`): versiegelte Regel P1 (`eed64ca5…`), 20 gelernt, **10 von 10** Hold-out richtig.
- Mentor (`40-mentor-lauf16/17.json`): Lauf 16 4 Richtungen mit 21 echten Artgedächtnis-Verweisen (0 erfundene), Lauf 17 5 Richtungen; Richtungen gewählt (Vollmacht, `41-…`).
- Gen 0 logmuehle: 42 von 42 nicht-äquivalenten Biotop-Mutanten gefangen; Kernmaß-Ausgang filtern −12, zaehlen −1 (wie versiegelt erwartet).

**Offen (nicht ausgeführt):** Generationen an Lauf 16 (Sättigung am gesättigten lagerhaus, Zeile Entropie), Lauf 17 (logmuehle, Artgedächtnis-Nachweis beim dritten Lauf, Jury-Fälle, Archivierungszählung), Projektgedächtnis-Vergleich der Kandidatenlisten, Kurven beider Werke, BERICHT.md, KASSE.md, Archive, Ordnerprüfsumme. Vorbereitet: `PREFIX=4g pruefung/generationen.sh 16 4 12 <ausgaben>` und `PREFIX=5g pruefung/generationen.sh 17 1 10 <ausgaben>`.

**Kasse Phase 3 bis jetzt:** Läufe 14–17 ≈ 0,15 € von 15 € (zwei schwere Mentor-Aufrufe ≈ 0,08 €; genaue Summe steht in der DB, nicht im Bericht).

Nächster Schritt auf dein Wort: Läufe 16/17 starten, Tor-3-Auswertung, Ordner versiegeln, Endmeldung mit Abholadresse und Prüfsumme.
```

### V0163 · 19.09.2026 16:44:37 CEST · Hermes-Zwischentext · Nachricht id 1895 · Sitzung `20260918_225920_3e614670` · 197 B

```text
Vier Bedingungen zuerst: K1165-Fund als Immuntest ins Immunsystem (Satz 7), Mentor-Verweise werkübergreifend trennen, Zerlegung mit Phase-2-Kategorien, Richtungswahl unter Vollmacht protokolliert.
```

### V0164 · 19.09.2026 16:44:37 CEST · Hermes-Zwischentext · Nachricht id 1901 · Sitzung `20260918_225920_3e614670` · 127 B

```text
Nun (4) Richtungswahl Lauf 16 unter Vollmacht, Zwischenbericht schreiben, dann beide Läufe starten (nacheinander, Kammer-CPU).
```

### V0165 · 19.09.2026 16:44:37 CEST · Hermes-Zwischentext · Nachricht id 1911 · Sitzung `20260918_225920_3e614670` · 195 B

```text
Gen 5 crashed on `gedaechtnis.wiederholung(... lauf_id)` kwargs collision. The runner moved on to Lauf 17 already. Fix the bug, reset Gen 5, and check that Gen 4 didn't already trigger this path.
```

### V0166 · 19.09.2026 16:44:37 CEST · Hermes-Zwischentext · Nachricht id 1913 · Sitzung `20260918_225920_3e614670` · 83 B

```text
The pkill killed my own shell (pattern matched). Redo the fix and reset separately.
```

### V0167 · 19.09.2026 16:44:37 CEST · Hermes-Zwischentext · Nachricht id 1917 · Sitzung `20260918_225920_3e614670` · 128 B

```text
Interessant: Lauf 17 Gen 1 hatte schon 5 überlebte Kandidaten (logmuehle liefert Gewinne). Neustart beider Läufe nacheinander.
```

### V0168 · 19.09.2026 16:44:37 CEST · Hermes-Zwischentext · Nachricht id 1933 · Sitzung `20260918_225920_3e614670` · 164 B

```text
Der Befehl (Prozesse beenden + Lauf 16 verwerfen) wurde vom Freigabe-Gate blockiert; nichts davon ist ausgeführt. Ich stoppe hier und schreibe den Zwischenbericht.
```

### V0169 · 19.09.2026 16:44:37 CEST · Hermes · Nachricht id 1937 · Sitzung `20260918_225920_3e614670` · 2834 B

```text
**Anhaltepunkt — ich brauche deine Entscheidung, bevor ich weiterlaufe.**

**Erledigt (deine vier Bedingungen):**
1. K1165-Fund als Immuntest im Immunsystem (offen, preise, Lauf 16 Gen 3; fällt am Werk: 1 failed — Protokoll `immun.fund`). Mentor Lauf 16 neu: Empfehlung „Hermes-Fund K1165 beheben“, als Richtung gewählt.
2. Mentor trennt jetzt Verweise: werkübergreifend (Artgedächtnis) vs. eigenes Werk (Projektgedächtnis). Lauf 16 neu ausgewiesen: **0 werkübergreifende**, 29 eigene, 0 erfundene — erwartbar, weil logmuehle noch keinen Lauf hatte. Der Tor-Nachweis kommt beim dritten Lauf.
3. Zerlegung Lauf 13 mit den Phase-2-Kategorien: 470 aufgehend; Ablehnungen 80/64/51/29/8/4 exakt wie Phase 2, **„sonst“ 3 statt 4** — Abweichung offen ausgewiesen (`00-lauf13-zerlegung-470.txt`), die vierte „sonst“-Zeile von Phase 2 kann ich aus der DB nicht reproduzieren.
4. Richtungswahl unter Vollmacht protokolliert (`mentor.gewaehtl` #7569, #7570, #7577).

**Was beim Lauf passierte:**
- Gen 5 Lauf 16: Absturz durch einen Protokoll-Bug (`lauf_id` doppelt) — reine Protokollierung, kein Messgerät; korrigiert, Gen 5 als abgebrochen markiert, protokolliert.
- **Messgerät-Fund in Gen 4:** Der Ankläger schrieb an K1191 einen Test, der `Katalog.wert == Staffelpreis` (den K1165-Fehler!) als Norm festlegt; weil er *am Kandidaten* fiel, wurde er als Fund gebucht — und tötet seither jede Behebung per Pareto je Test (Gen 4/6: alle sechs Behebungsversuche „Regression je Test“). Das ist genau die Lücke aus Lauf 7, nur spiegelverkehrt: F4 3.7 sagt „jeder neue Test“, mein Ankläger prüfte den Verweis nur bei Tests, die an der *Vorgeneration* fallen.
- Korrektur geschrieben (Norm-Regel auch für Angriffstests am Kandidaten), liegt als `git stash`, **nicht aktiv**. Nach Satz 2 F4 ist das ein neuer Lauf. Mein Versuch, Lauf 16 zu stoppen und zu verwerfen, wurde vom Freigabe-Gate blockiert — daher läuft Lauf 16 noch (Gen 8, alter Ablauf, Kernmaß bleibt 0, ≈0,07 €/Gen).

**Ich schlage vor:** Lauf 16 anhalten und verwerfen (Nachprobe Gen 1–3 bleibt gültig, sie lief vor der Änderung), Korrektur aktivieren, **Lauf 18** vom Ausgang Lauf 16 Gen 3 (mit dem offenen K1165-Fund) als Sättigungs-/Behebungslauf, dann Lauf 17 (logmuehle), dann Tor 3. Alternativ: Lauf 16 zu Ende laufen lassen (Sättigungsmeldung kommt so oder so, aber mit vergiftetem Immunsystem) — das hielte ich für falsch.

**Kosten Phase 3:** 294 Aufrufe, 0,73 € von 15 €.

**Ordner:** `…/laeufe/biotop-phase-3/ZWISCHENBERICHT.md`, 89 Dateien, Prüfsumme `e561cbeb823fc188fad8567318c30c54a4f9590aa4ba70b243b66d07f9481bfe`. Offen: Läufe 17/18, Zeilen Projektgedächtnis/Artgedächtnis/Entropie/Jury/Archivierung, Kurven, BERICHT.md.

Sag „Lauf 16 verwerfen, Lauf 18“ oder anders — dann geht es weiter.
```

### V0170 · 19.09.2026 16:44:37 CEST · Hermes · Nachricht id 1939 · Sitzung `20260918_225920_3e614670` · 332 B

```text
Das war der erste Läufer (vor dem Protokoll-Fix), den ich vorhin beendet habe — erwartet. Der zweite Läufer (`proc_08a35ebaa790`, Lauf 16 Gen 8) läuft weiter, bis du entscheidest.

Stand unverändert: warte auf dein Wort zu **„Lauf 16 verwerfen, Korrektur aktivieren, Lauf 18“** (mein Vorschlag) oder eine andere Anweisung.
```

### V0171 · 19.09.2026 16:44:37 CEST · Hermes · Nachricht id 1947 · Sitzung `20260918_225920_3e614670` · 1920 B

```text
**Beide Läufe sind fertig — gesättigt, unter dem alten Ankläger-Ablauf.** Stand (aus der DB):

**Lauf 17, logmuehle (Übungswerk 2):**
- Gen 2: filtern Fehlschläge 6 → 0 und Sicherheit gesenkt; Gen 3: Sicherheitspunkte 2 → 0 (W1 `shell=True` weg — kein `shell=True`/`subprocess.run` mehr in `extern.py`, 1 Immuntest im Werk); Gen 4: ausgabe-Test behoben; Gen 5: Laufzeit ausgabe/lesen/zaehlen −29 bis −47 %.
- Kernmaß −12 → **0 in allen vier Bereichen**, 62 von 62 Tests; Sättigungsmeldung Gen 4–8, Verbesserung 0,00 %, Doppelgänger 9 %, Lauf beendet sich selbst.
- Ob W2/W3 nach versiegeltem Kriterium behoben sind, prüfe ich in der Tor-Auswertung, noch nicht gewertet.

**Lauf 16, lagerhaus:**
- Gen 8: formeln 130 → 1,9 ms, preise 97 → 13 ms (Nische schnell). Sättigung Gen 4–9, Kernmaß 0 = Höchstwert.
- **K1165-Fund bleibt offen** — jede Behebung stirbt am K1191-Angriffstest (Norm des Fehlers, per Pareto je Test). Das ist der Messgerät-Fehler, dessen Korrektur im Stash liegt.

**Weitere Zahlen:** Jury 2 Fälle, 2 einstimmig (Fall ohne Einstimmigkeit fehlt noch); Projektgedächtnis 38 Wiederholungen ohne Kammerlauf verworfen; Archivierungen 0 (kein offener Fund hat 5 angenommene Generationen erlebt); 618 Aufrufe, 1,61 € von 15 €.

**Ordner:** ZWISCHENBERICHT.md aktualisiert, 111 Dateien, Prüfsumme `c4e35588f656321bf0b93a147d450865b00f1353ca03c6677bdcb26d365851c6`.

**Entscheidung offen (dein Wort):**
- **A (mein Vorschlag):** Korrektur aktivieren → **Lauf 18** vom Ausgang Lauf 16 Gen 3 (K1165 offen), ≈ 6–8 Generationen ≈ 0,5 €; ist zugleich der „dritte Lauf“ für den werkübergreifenden Artgedächtnis-Nachweis (logmuehle-Einträge liegen jetzt vor). Lauf 16 bleibt als verworfen dokumentiert, Nachprobe Gen 1–3 gültig.
- **B:** Tor 3 auf diesem Stand auswerten; K1165 dann offen ausgewiesen (Satz 7 verletzt), Artgedächtnis-Nachweis fehlt.
```

### V0172 · 19.09.2026 16:44:37 CEST · Hermes-Zwischentext · Nachricht id 1949 · Sitzung `20260918_225920_3e614670` · 177 B

```text
Lauf 16 ist bereits von selbst beendet (gesättigt, kein Prozess mehr aktiv) — ich verwerfe ihn jetzt in der DB, aktiviere die Korrektur in deiner Fassung und lege Lauf 18 an.
```

### V0173 · 19.09.2026 16:44:51 CEST · Hermes-Zwischentext · Nachricht id 1984 · Sitzung `20260918_225920_3e614670` · 246 B

```text
Artgedächtnis ist gefüllt (89 logmuehle-Einträge) und wird dem Mentor gezeigt — er zitiert nur nichts davon. Die abgelehnten Einträge stehen vorn; ich sortiere die angenommenen voran (Mentor ist kein Messgerät, Lauf 18 hat 0 Generationen).
```

### V0174 · 19.09.2026 16:46:50 CEST · Hermes-Zwischentext · Nachricht id 2002 · Sitzung `20260918_225920_3e614670` · 195 B

```text
Artgedächtnis-Block ist jetzt sichtbar (angenommene logmuehle-Einträge zuerst), der Mentor zitiert trotzdem keinen — das messe ich so und melde es. Jetzt Richtung wählen und Lauf 18 starten.
```

### V0175 · 19.09.2026 16:57:15 CEST · Hermes-Zwischentext · Nachricht id 2012 · Sitzung `20260918_225920_3e614670` · 128 B

```text
Gen 1 angenommen (Laufzeit formeln −98 %, preise −86 %). Ich lasse weiterlaufen und schreibe inzwischen den Zwischenbericht.
```

### V0176 · 19.09.2026 17:04:13 CEST · Hermes-Zwischentext · Nachricht id 2016 · Sitzung `20260918_225920_3e614670` · 145 B

```text
Zwei Blockaden: Projektgedächtnis zitiert den **verworfenen** Lauf 16, und ein Immuntest im Werk verursacht Pareto-Regression. Ich messe beides.
```

### V0177 · 19.09.2026 17:04:45 CEST · Hermes-Zwischentext · Nachricht id 2020 · Sitzung `20260918_225920_3e614670` · 247 B

```text
Gefunden: Lauf 18 stirbt an Einträgen im Projektgedächtnis, die aus dem **verworfenen** Lauf 16 stammen (K1202, Ähnlichkeit 1.0 — damals nur durch den fehlerhaften Ankläger abgelehnt). Ein verworfener Lauf darf kein Gedächtnis hinterlassen.
```

### V0178 · 19.09.2026 17:05:39 CEST · Hermes-Zwischentext · Nachricht id 2032 · Sitzung `20260918_225920_3e614670` · 203 B

```text
Zweiter Fund: Auch `gescheiterte_wege`/`wiederholung` sind Teil des Messgeräts (sie verwerfen Kandidaten ohne Kammerlauf). Nach Satz 2 F4 verwerfe ich Lauf 18 und starte Lauf 19 vom Stand Lauf 18 Gen 1.
```

### V0179 · 19.09.2026 17:05:50 CEST · Hermes-Zwischentext · Nachricht id 2036 · Sitzung `20260918_225920_3e614670` · 129 B

```text
Vor Lauf 19 prüfe ich, ob der K1321-Immuntest (Staffel) den Fix wirklich blockiert — sonst stirbt Lauf 19 an derselben Stelle.
```

### V0180 · 19.09.2026 17:06:05 CEST · Hermes-Zwischentext · Nachricht id 2040 · Sitzung `20260918_225920_3e614670` · 93 B

```text
Der Test ist sauber (nennt den Vertrag explizit, kollidiert nicht mit K321). Lauf 19 anlegen.
```

### V0181 · 19.09.2026 17:07:21 CEST · Hermes-Zwischentext · Nachricht id 2044 · Sitzung `20260918_225920_3e614670` · 188 B

```text
Der Mentor zitiert konsequent nur das eigene Werk — 3 Läufe in Folge 0 werkübergreifende Verweise. Das ist Tor-3-Zeile „Artgedächtnis"; ich messe die Ursache, statt es zu behaupten.
```

### V0182 · 19.09.2026 17:07:29 CEST · Hermes-Zwischentext · Nachricht id 2046 · Sitzung `20260918_225920_3e614670` · 188 B

```text
Beide Blöcke sind gleich groß und sichtbar — das Modell wählt die eigenen Einträge, weil sie konkreter passen. Ich starte Lauf 19 und werte die Zeile ehrlich als gemessenes Ergebnis.
```

### V0183 · 19.09.2026 17:21:23 CEST · Hermes-Zwischentext · Nachricht id 2056 · Sitzung `20260918_225920_3e614670` · 185 B

```text
Zwei Generationen an derselben Stelle abgelehnt: Grenzmaß `bericht.laufzeit_ms`. Ich messe, ob das echte Verschlechterung oder Rauschen ist — fünf Läufe am **unveränderten** Werk.
```

### V0184 · 19.09.2026 17:22:20 CEST · Hermes-Zwischentext · Nachricht id 2070 · Sitzung `20260918_225920_3e614670` · 238 B

```text
Gemessen: die Ablehnungen sind echt (Rauschen max. 8,46 ms gegen 12,10/14,78) — das Grenzmaß arbeitet korrekt. Bei `formeln` ist die 15-%-Toleranz allerdings zu eng (47 % Eigenrauschen); das notiere ich als Fund. Lauf 19 läuft weiter.
```

### V0185 · 19.09.2026 17:29:45 CEST · Hermes-Zwischentext · Nachricht id 2076 · Sitzung `20260918_225920_3e614670` · 111 B

```text
K1165 ist bis Gen 4 noch offen (Test fällt weiter). Ich lasse Lauf 19 laufen und schreibe den Zwischenbericht.
```

### V0186 · 19.09.2026 17:30:07 CEST · Hermes · Nachricht id 2078 · Sitzung `20260918_225920_3e614670` · 2762 B

```text
Zwischenstand, alles gemessen:

**Prozessprüfung beim Wiedereinstieg:** keine Biotop-Prozesse, keine Container — bestätigt per `ps` und `docker ps`, bevor ich etwas gestartet habe.

**Gemessene Abweichung vom Auftragstext:** Lauf 16 stand noch auf `gesaettigt`, die Korrektur war nicht committet, K1191 noch auf `offen`. Der vorige Turn wurde vor der Ausführung abgebrochen. Jetzt erledigt:
- Regel in deinem Wortlaut gefasst (Pareto je Test für Werk-Tests, Verträge, Verfassung; neuer Angriffstest tötet nur bei Absturz oder explizitem Verweis, sonst offen/0 Punkte), Commit `8205574`.
- Lauf 16 verworfen, K1191 auf `offen_norm` zurückgestuft, K1165 bleibt offen (`lauf.verworfen` protokolliert).
- Regel „Abbrüche nach Satz 2 sind vom Freigabe-Gate ausgenommen" als `biotop.regel` protokolliert.

**Lauf 18** (Ausgang Lauf 16 Gen 3, Prüfsumme `e4f48583`): Gen 1 angenommen (formeln 123,19 → 1,87 ms, preise 92,12 → 13,26 ms). Dann **zweiter Messgerät-Fund, gemessen**: 12 von 13 Kandidaten wurden als „Wiederholung eines gescheiterten Wegs" ohne Kammerlauf verworfen — mit Verweis auf **Lauf 16**, also auf Ablehnungen des als falsch erkannten Anklägers. Das Projektgedächtnis ist Teil des Messgeräts. Korrektur: Wege aus verworfenen Läufen zählen nicht (`gedaechtnis.gescheiterte_wege` + `wiederholung` filtern `status != 'verworfen'`); Lauf 18 nach Satz 2 verworfen, Gen 1 bleibt als Schnappschuss.

**Lauf 19** (Ausgang Lauf 18 Gen 1, `4f3427cb`) läuft: Gen 1/2 abgelehnt am Grenzmaß `bericht.laufzeit_ms`, Gen 3 angenommen (formeln 1,88 → 1,31 ms), Gen 4 abgelehnt, Gen 5 läuft. **K1165 noch offen** — Immuntest fällt weiter gegen den aktuellen Stand (`stueckpreis(menge)` statt Grundpreis), gerade eben in der Kammer geprüft.

**Rauschprobe** (5 Messungen am unveränderten Werk, `92-rauschprobe-lauf19.txt`): bericht 7,90–8,46 ms → die Ablehnungen bei 12,10 und 14,78 ms sind echte Verschlechterung, kein Rauschen. Nebenbefund: formeln rauscht mit 47 % (1,66–2,44 ms) weit über die 15-%-Toleranz — Fund für Fassung 5.

**Artgedächtnis-Zeile, gemessen statt behauptet:** Der Block „ANDERE WERKE" enthält 25 logmuehle-Einträge, angenommene zuerst (nach meiner Korrektur). Der Mentor zitierte trotzdem in Lauf 18 und 19 **0 werkübergreifende** Verweise, nur eigene (10 bzw. 4). Die Tor-3-Zeile ist damit nach aktuellem Stand **nicht erfüllt**; ich werte sie so, wenn kein späterer Mentor-Aufruf einen liefert.

**Kasse:** 955 Aufrufe, 2,33 € von 15 €.

**Ordner:** ZWISCHENBERICHT.md + DATEIEN.txt aktuell, 155 Dateien, Prüfsumme `aa31d2bc44506e3b8280a1f43fcd817b562a7ee956023e0e2a70472ee579660c`.

Offen: Lauf 19 zu Ende, Tor 3 alle elf Zeilen, Kurven beider Werke, Ordner versiegeln, Endmeldung.
```

### V0187 · 19.09.2026 17:30:25 CEST · Hermes · Nachricht id 2082 · Sitzung `20260918_225920_3e614670` · 311 B

```text
Das war der Lauf-18-Läufer, den ich beim Verwerfen nach Satz 2 selbst beendet habe — erwartet, exit 143 = mein SIGTERM.

Lauf 19 läuft unberührt weiter (Prozess aktiv, Gen 5 in Arbeit; Gen 1/2 abgelehnt am Grenzmaß, Gen 3 angenommen, Gen 4 abgelehnt). Ich melde mich, wenn er durch ist oder sich sättigt.
```

### V0188 · 19.09.2026 17:34:43 CEST · Hermes-Zwischentext · Nachricht id 2086 · Sitzung `20260918_225920_3e614670` · 80 B

```text
Lauf 19 gesättigt, K1165 weiter offen. Ich messe, woran die Behebung scheitert.
```

### V0189 · 19.09.2026 17:35:00 CEST · Hermes-Zwischentext · Nachricht id 2088 · Sitzung `20260918_225920_3e614670` · 176 B

```text
Der Blocker ist sichtbar: `test_preise_immun_aegis_k1195_preise_w17` — ein Zwilling des K1191-Normtests, der den Fehler als Norm festschreibt. Ich messe, ob er im Werk liegt.
```

### V0190 · 19.09.2026 17:35:53 CEST · Hermes-Zwischentext · Nachricht id 2090 · Sitzung `20260918_225920_3e614670` · 327 B

```text
Gefunden: fünf Zwillinge des K1191-Normtests (K1195, K1200, K1201, K1296, K1374 — alle `test_katalog_wert_ignoriert_staffelpreise…`) stehen auf `offen` statt `offen_norm`. Ich habe bei der Übernahme aus dem verworfenen Lauf 16 die alten Stati blind mitgenommen. Diesmal prüfe ich mechanisch, bevor ich einen Lauf starte.
```

### V0191 · 19.09.2026 17:39:12 CEST · Hermes-Zwischentext · Nachricht id 2100 · Sitzung `20260918_225920_3e614670` · 157 B

```text
Sauber getrennt: 6 von 7 sind Norm, K1165 bleibt als einziger echter Fund (fällt am Werk, nennt den Vertrag). Ich schreibe das in die DB und starte Lauf 20.
```

### V0192 · 19.09.2026 17:39:38 CEST · Hermes-Zwischentext · Nachricht id 2102 · Sitzung `20260918_225920_3e614670` · 167 B

```text
Norm und Fund sind jetzt getrennt (1 Fund, 13 Norm). Das ändert den gemessenen Testbestand → nach Satz 2 ein neuer Lauf. Lauf 19 verwerfen, Lauf 20 vom Stand Gen 3.
```

### V0193 · 19.09.2026 17:39:48 CEST · Hermes-Zwischentext · Nachricht id 2106 · Sitzung `20260918_225920_3e614670` · 122 B

```text
Lauf 19 ist bereits verworfen; nur das Entpacken scheiterte (Feld heißt anders). Ich hole den Schnappschuss Gen 3 direkt.
```

### V0194 · 19.09.2026 17:41:36 CEST · Hermes-Zwischentext · Nachricht id 2118 · Sitzung `20260918_225920_3e614670` · 126 B

```text
Lauf 20 läuft mit sauberem Immunsystem (1 Fund, 13 Norm). Während er arbeitet, baue ich die Kurven und die Tor-3-Auswertung.
```

### V0195 · 19.09.2026 17:55:30 CEST · Hermes-Zwischentext · Nachricht id 2130 · Sitzung `20260918_225920_3e614670` · 148 B

```text
**K1165 ist behoben** — Gen 1 angenommen, `preise.tests_fehlgeschlagen: 1 → 0`, Fund-Status `im_werk`. Satz 7 erfüllt. Ich verifiziere am Werk.
```

### V0196 · 19.09.2026 17:55:41 CEST · Hermes-Zwischentext · Nachricht id 2132 · Sitzung `20260918_225920_3e614670` · 141 B

```text
`stueckpreis(menge)` → `grundpreis`, Immuntest im Werk, 104 von 104 grün. Ich schreibe den Zwischenbericht und lasse Lauf 20 weiterlaufen.
```

### V0197 · 19.09.2026 17:55:56 CEST · Hermes · Nachricht id 2134 · Sitzung `20260918_225920_3e614670` · 1769 B

```text
**K1165 ist behoben — Satz 7 erfüllt, in der Kammer bestätigt.**

Lauf 20, Gen 1 angenommen: `preise.tests_fehlgeschlagen 1 → 0`. Am Werk nachgemessen: `Katalog.wert` nutzt jetzt `artikel.grundpreis * menge` statt `stueckpreis(menge)`, der Immuntest `test_preise_immun_hermes_k1165_wert_grundpreis_w18.py` liegt im Werk, Fund-Status `im_werk`, 104 von 104 Tests grün.

**Der Weg dahin war ein dritter Messgerät-Fund, mechanisch belegt** (`93-funde-neubewertung-werk17.txt`): Bei der Übernahme der Funde aus den verworfenen Läufen hatte ich die alten Stati blind mitgenommen. Sechs Ankläger-Tests (K1195, K1200, K1201, K1265, K1296, K1374 — alle Varianten von „`wert` ignoriert Staffelpreise") standen als *Fund* im Testbestand und schrieben den Fehler als Norm fest; jede Behebung starb an Pareto je Test. Ich habe alle offenen Funde in der Kammer nachgemessen: 6 von 7 bestehen am Werk, ohne Absturz, ohne Vertragsverweis → Norm. Nur K1165 fällt am Werk und nennt den Vertrag → echter Fund. Lauf 19 nach Satz 2 verworfen (Testbestand geändert), Lauf 20 vom Stand Gen 3 gestartet — und dort fiel der Fehler in der ersten Generation.

**Läufe:** 14, 15, 16, 18, 19 verworfen (je nach Satz 2 mit protokolliertem Grund), 17 gesättigt, 20 läuft (Gen 2).

**Kurve logmuehle** liegt vor (`kurve-logmuehle.svg/.txt`): Kernmaß −13 → 0 über Gen 0/2/3/4/5, Tests 56 → 62, Laufzeiten am Ende ausgabe 10,25 / filtern 24,71 / lesen 14,83 / zaehlen 11,00 ms.

**Kasse:** 1.046 Aufrufe, 2,50 € von 15 €.

**Ordner:** ZWISCHENBERICHT.md + DATEIEN.txt aktuell, 174 Dateien, Prüfsumme `3b48ecec7f92b69ce5efcc5b8288babe6beb7eb32dcf090c7d1952f473b964a5`.

Offen: Lauf 20 zu Ende, Kurve lagerhaus, Tor 3 alle elf Zeilen, Ordner versiegeln, Endmeldung.
```

### V0198 · 19.09.2026 18:08:27 CEST · Philipp · Nachricht id 2135 · Sitzung `20260918_225920_3e614670` · 965 B

```text
Weiter mit Lauf 20 — keine Messgerätänderung jetzt, sonst stirbt der Lauf nach Satz 2; die folgenden Punkte gehören in den Bericht, nicht in den Code. Erstens: Die sechs Norm-Tests waren nach 3.10 Doppelungen (gleiche Behauptung, gleiche Stelle) und hätten nie einzeln ins Immunsystem gedurft — die Doppelungserkennung vergleicht Meldungsklasse und Ort statt der Behauptung; als Befund ausweisen, Doppelungsanteil aus Phase 2 mit dieser Lesart neu rechnen, Korrektur erst in Fassung 5. Zweitens: Lauf 20 ist der erste Lauf, in dem werkübergreifende Artgedächtnis-Verweise aus logmuehle möglich sind — Mentor-Verweise getrennt ausweisen (werkübergreifend / eigenes Werk / erfunden) für die Tor-3-Zeile. Drittens im Bericht vermerken, dass der tragende Vertrag bericht→preise von dir stammt, nicht von Philipp. Dann Lauf 20 zu Ende, Kurve lagerhaus, Tor 3 alle elf Zeilen, Ordner versiegeln, Endmeldung mit vollständiger Abholadresse und Prüfsumme.
```

### V0199 · 19.09.2026 18:08:36 CEST · Hermes-Zwischentext · Nachricht id 2136 · Sitzung `20260918_225920_3e614670` · 131 B

```text
Verstanden — keine Messgerätänderung mehr in Lauf 20. Ich sammle die drei Punkte als Bericht-Befunde und lasse den Lauf laufen.
```

### V0200 · 19.09.2026 18:09:09 CEST · Hermes-Zwischentext · Nachricht id 2138 · Sitzung `20260918_225920_3e614670` · 129 B

```text
Bestätigt: Schlüssel ist `(Meldungsklasse, Ort)`, nicht die Behauptung. Ich messe den Befund und rechne den Phase-2-Anteil neu.
```

### V0201 · 19.09.2026 18:09:35 CEST · Hermes-Zwischentext · Nachricht id 2142 · Sitzung `20260918_225920_3e614670` · 170 B

```text
Meine Heuristik gruppiert nach Ziel **und Zahlenwert** — das trennt Tests, die dieselbe Sache behaupten. Ich rechne beide Lesarten aus, sonst ist die Zahl irreführend.
```

### V0202 · 19.09.2026 18:10:06 CEST · Hermes-Zwischentext · Nachricht id 2148 · Sitzung `20260918_225920_3e614670` · 100 B

```text
Vor dem Lauf prüfe ich die 2,5-%-Behauptung aus Phase 2 an der Datenbank, statt sie zu übernehmen.
```

### V0203 · 19.09.2026 18:10:22 CEST · Hermes-Zwischentext · Nachricht id 2154 · Sitzung `20260918_225920_3e614670` · 161 B

```text
Die 2,5 % aus Phase 2 waren gegen die 240 Ablehnungen gerechnet, nicht gegen die erzeugten Tests — meine Bezugsgröße war irreführend. Ich halte beides fest.
```

### V0204 · 19.09.2026 18:10:30 CEST · Hermes-Zwischentext · Nachricht id 2156 · Sitzung `20260918_225920_3e614670` · 50 B

```text
Beide Lesarten liegen vor. Lauf 20 weiter prüfen.
```

### V0205 · 19.09.2026 18:24:07 CEST · Hermes-Zwischentext · Nachricht id 2162 · Sitzung `20260918_225920_3e614670` · 96 B

```text
Lauf 20 gesättigt, K1165 behoben. Jetzt Kurve lagerhaus und die vollständige Tor-3-Auswertung.
```

### V0206 · 19.09.2026 18:24:26 CEST · Hermes-Zwischentext · Nachricht id 2168 · Sitzung `20260918_225920_3e614670` · 103 B

```text
Elf Tor-3-Zeilen bestätigt. Ich prüfe die Jury (Fall ohne Einstimmigkeit fehlt) und die Archivierung.
```

### V0207 · 19.09.2026 18:24:46 CEST · Hermes-Zwischentext · Nachricht id 2170 · Sitzung `20260918_225920_3e614670` · 147 B

```text
Jury: 3 Fälle, alle einstimmig — der Fall *ohne* Einstimmigkeit fehlt. Ich prüfe das mit einer Probe (kein Messgeräteingriff, eigener Aufruf).
```

### V0208 · 19.09.2026 18:25:45 CEST · Hermes-Zwischentext · Nachricht id 2178 · Sitzung `20260918_225920_3e614670` · 202 B

```text
Auch die Probe wurde einstimmig — die Jury ist einiger als erwartet. Ein zweiter Versuch mit echtem Zielkonflikt (Kürze gegen Fehlermeldungsqualität), dann werte ich die Zeile so, wie sie ausfällt.
```

### V0209 · 19.09.2026 18:26:13 CEST · Hermes-Zwischentext · Nachricht id 2180 · Sitzung `20260918_225920_3e614670` · 211 B

```text
5 von 5 einstimmig — die Zeile verlangt aber einen Fall *ohne* Einstimmigkeit. Ich werte sie als nicht belegt und halte den Grund fest; die Mechanik (kein Urteil bei Uneinigkeit) prüfe ich separat mechanisch.
```

### V0210 · 19.09.2026 18:26:27 CEST · Hermes-Zwischentext · Nachricht id 2184 · Sitzung `20260918_225920_3e614670` · 145 B

```text
Mechanik belegt (kein Urteil, protokolliert) — aber mit gestellter Gegenstimme, das weise ich so aus. Jetzt die vollständige Tor-3-Auswertung.
```

### V0211 · 19.09.2026 18:27:22 CEST · Hermes-Zwischentext · Nachricht id 2192 · Sitzung `20260918_225920_3e614670` · 195 B

```text
Differenz geklärt: Meine Nachrechnung leitet Funktionen aus Hunk-Köpfen ab, das Biotop aus dem angewandten Diff — gröber, daher 2 Treffer mehr. Ich weise beide Zahlen aus. Jetzt der Bericht.
```

### V0212 · 19.09.2026 18:30:08 CEST · Hermes-Zwischentext · Nachricht id 2198 · Sitzung `20260918_225920_3e614670` · 51 B

```text
Alle Zahlen liegen vor. Jetzt der Abschlussbericht.
```

### V0213 · 19.09.2026 18:30:24 CEST · Hermes-Zwischentext · Nachricht id 2200 · Sitzung `20260918_225920_3e614670` · 150 B

```text
Vor dem Versiegeln prüfe ich die Berichtszahlen gegen die Datenbank — besonders die W1–W3-Behauptungen, die ich noch nicht einzeln gemessen habe.
```

### V0214 · 19.09.2026 18:30:50 CEST · Hermes-Zwischentext · Nachricht id 2206 · Sitzung `20260918_225920_3e614670` · 165 B

```text
W1 wurde radikaler gelöst als von mir erwartet: der Subprozess wurde ganz entfernt und grep intern nachgebildet. Ich korrigiere die Berichtszeile auf das Gemessene.
```

### V0215 · 19.09.2026 18:30:57 CEST · Hermes-Zwischentext · Nachricht id 2208 · Sitzung `20260918_225920_3e614670` · 44 B

```text
Jetzt Archive, Kassenblatt und Versiegelung.
```

### V0216 · 19.09.2026 18:31:21 CEST · Hermes-Zwischentext · Nachricht id 2212 · Sitzung `20260918_225920_3e614670` · 128 B

```text
Der Bericht sagt „schwere Aufrufe = Mentor" — gemessen sind 15 der 24 der Ankläger bei `filtern`. Ich korrigiere die Zeile.
```

### V0217 · 19.09.2026 18:31:36 CEST · Hermes-Zwischentext · Nachricht id 2216 · Sitzung `20260918_225920_3e614670` · 92 B

```text
Der Bericht nennt „96 Rohausgaben", gemessen sind 167. Ich korrigiere und versiegle final.
```

### V0218 · 19.09.2026 18:37:34 CEST · Hermes · Nachricht id 2224 · Sitzung `20260918_225920_3e614670` · 3113 B

```text
Phase 3 abgeschlossen. Abschlussordner liegt im Prüfkanal, von außen abrufbar (HTTP 200 geprüft).

**Abholadresse:**
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/BERICHT.md

**Prüfsumme des Ordners** (SHA-256 über DATEIEN.txt, 198 Dateien):
`a2b2cee98ecdea5724bc8969721f41ea5b44ffdb037bc3427489cc9ee6f737fb`

**Tor 3: 7 von 11 voll, 2 teilweise, 2 nicht belegt** — meine Wertung, jede Zeile mit Ausgabedatei:
- **erfüllt:** Nachprobe Z7 (angenommen und im Werk, Lauf 16 Gen 3), Mentor (5 Aufrufe, 4–5 Richtungen, Pflichtfelder vollständig), Entropie (Sättigung nach Gen 5 am gesättigten lagerhaus, Lauf endet selbst), Geschmack (10 von 10, versiegelte Regel, als Mechanikprüfung gekennzeichnet), Oberfläche (18 von 18 Routen 401, 18 von 18 Elemente mit Datei:Zeile), Zerlegung (172 und 245 gehen auf, Phase-2-Kategorien unverändert), Kurven beider Werke.
- **teilweise:** Projektgedächtnis — 9 Kandidaten ohne Kammerlauf verworfen, aber meine Nachrechnung findet 2 von 187 ausgeführte Wiederholungen; die Differenz kommt aus zwei verschiedenen Ableitungen der berührten Funktionen und ist im Bericht offen ausgewiesen, nicht wegerklärt. Jury — 3 einstimmige Fälle mit je drei Begründungen belegt; der Fall ohne Einstimmigkeit **nicht** mit echtem Dissens (5 von 5 einstimmig, auch bei zwei gestellten Zielkonflikten), nur die Mechanik mit gestellter Gegenstimme.
- **nicht belegt:** Artgedächtnis — 0 werkübergreifende Verweise in drei Läufen nach beiden Werken (bei 0 erfundenen); das Artgedächtnis wird vorgelegt, das Modell zitiert das eigene Werk. Archivierung — 0 Archivierungen, weil kein Fund 5 angenommene Generationen erlebte.

**Satz 7 erfüllt:** K1165 (Bestandsbewertung zum Staffelpreis statt Grundpreis) wurde als Immuntest eingelegt und in Lauf 20 Gen 1 behoben — `preise.tests_fehlgeschlagen` 1 → 0, Test im Werk, 104 von 104 grün.

**Was schiefging:** drei Messgerät-Fehler, fünf verworfene Läufe (14, 15, 16, 18, 19), je mit Protokollzeile. Der Ankläger buchte einen Test, der den Fehler als Norm festschrieb, als Fund; das Projektgedächtnis zitierte einen verworfenen Lauf; sechs Normtests standen als Funde im Testbestand (mein Fehler beim Übertragen). Die verworfenen Läufe kosteten 1,41 € — die Hälfte der Phase.

**Deine drei Punkte im Bericht:** Doppelungs-Befund mit neu gerechnetem Anteil (2,5 % war gegen 240 Ablehnungen gerechnet statt gegen 55 erzeugte Tests — richtig sind 10,9 % bei gleicher Lesart, 83,6 % bei deiner Lesart „gleiche Behauptung"); Mentor-Verweise getrennt ausgewiesen; der Vertrag `bericht→preise` als von mir stammend gekennzeichnet, gleich in der Vorbemerkung.

**Kosten:** 2,83 € von 15 € (1.225 Aufrufe). Schwere Aufrufe 24 — davon 15 Ankläger (Sicherheitsbefund `filtern`), 9 Mentor.

**Sechs Punkte für Fassung 5** stehen in Abschnitt 8, darunter: Doppelungsschlüssel auf die Behauptung umstellen, Grenzmaß-Toleranz aus einer Rauschmessung ableiten (formeln rauscht 47 % bei 15 % Toleranz), Artgedächtnis- und Jury-Zeile umformulieren.
```

### V0219 · 19.09.2026 18:37:51 CEST · Hermes · Nachricht id 2228 · Sitzung `20260918_225920_3e614670` · 550 B

```text
Das war der Lauf-20-Läufer, der sich nach der Sättigungsmeldung selbst beendet hat — seine Ergebnisse stecken bereits im Bericht (Gen 1 angenommen, K1165 behoben, Gen 2–5 abgelehnt, Sättigung nach Gen 5).

Nachgeprüft statt angenommen: keine Biotop-Prozesse, keine Container, und der versiegelte Ordner ist unverändert — 198 Dateien, neu berechnete Prüfsumme `a2b2cee98ecdea5724bc8969721f41ea5b44ffdb037bc3427489cc9ee6f737fb` identisch mit der versiegelten.

Phase 3 bleibt wie gemeldet abgeschlossen. Ich warte auf Chat-Claudes Prüfung.
```

### V0220 · 19.09.2026 19:25:47 CEST · Philipp · Nachricht id 2229 · Sitzung `20260918_225920_3e614670` · 579 B

```text
Die Abschlussmeldung zu Phase 3 ist hier nie angekommen — mein letzter Stand ist der Zwischenbericht mit 174 Dateien und Prüfsumme 3b48ecec…, Lauf 20 bei Generation 2. Schick die Abschlussmeldung noch einmal vollständig: die Wertung aller elf Tor-3-Zeilen mit Ergebnis und Bezugsgröße, die Endkosten, und vor allem die vollständige Abholadresse des Berichts (ganze URL mit Schlüssel, nicht gekürzt) — ohne sie kann Chat-Claude den Ordner nicht öffnen und nichts prüfen. Am Ordner selbst nichts mehr ändern; die Versiegelung ist bestätigt und bleibt, wie sie ist.
```

