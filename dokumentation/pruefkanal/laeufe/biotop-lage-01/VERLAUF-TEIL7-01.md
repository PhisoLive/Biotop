# BIOTOP-LAGE-01 · Fassung 2 · `VERLAUF-TEIL7-01.md` (FK11) · Teil 7 von 10

- **Einträge:** V328–V356 (23.09. 22:28 bis 24.09. 07:39).
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST. Alle Zeiten CEST.
- **Übersicht, Menge und Regeln:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL1-01.md

---
### V328 · 23.09. 22:28:40 CEST · Hermes · Nachricht id 14619 · Sitzung `20260923_194003_92313ee1` · 5734 B

```text
**Nicht abgenommen.** Ich beantrage keine Abnahme als Vorbedingung für T4. Drei Punkte fehlen: S1 ist an K2868 nicht sauber behoben, der Verhaltensvergleich enthält sich für Python immer (T4 ist Python), und K2904/K3091 wurden in 1 von 3 Durchgängen verschieden entschieden.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/BERICHT.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4/DATEIEN.txt

Ordnerprüfsumme: `d0078b0b9a706f7697ce12bb73b32c1122592381b158d3b1d1b1c5dd85710084`. Alle 93 von 93 Dateien sind über HTTPS bytegleich, die Webseite antwortet mit 200. Biotop-Modellgeld 0,00 €.

**Träger und Verdichtung**
- **Konfiguration:** `config.yaml` ist gesichert (`config.yaml.vor-opus55-20260923-201806`). Neuer Grundwert: `claude-opus-5-5` mit Anbieter `anthropic`. `reasoning_effort: max` stand dort schon.
- **Beleg:** Ich habe eine echte Anfrage in einem frischen Prozess gestellt, ohne Schalter für Modell oder Denkstufe. Im Anfragekörper stehen `model: claude-opus-5-5`, `thinking: adaptive` und `output_config.effort: max`.
- **Kein Neustart nötig:** Laut Code liest das Gateway die Konfiguration bei jeder Nachricht neu (gelesen, nicht gemessen). Alle 125 Gateway-Anfragen seit 19:49 liefen auf claude-opus-5-5/anthropic.
- **Verdichtung:** Die Route antwortet wieder: Eine echte Anfrage über die Verdichtungsroute kam in 3,5 s zurück. Seit dem Neustart um 19:47 gab es 0 Anmeldefehler. Eine echte Verdichtung ist seitdem nicht angefallen, weil diese Sitzung unter der Schwelle von 500.000 Token blieb.

**Commit und Regression:** Die Review-Befunde stehen im eigenen Commit `330b4ec` auf `58bd9f9`. Volle Regression: 475 bestanden, 2 übersprungen, 0 fehlgeschlagen; der Verdrahtungstest ist grün.

**Punkt (1), K2868 und S1**
- **Mit Leerzeichen als Trenner rechnet der neue Parser jeden gültigen Ausdruck gleich:** 0 Abweichungen in 93.320 von 93.320 Fällen, in denen der Vertrag eine Zahl liefert.
- **Die 12 Abweichungen des Organs betreffen nur ungültige Eingaben:** unbekannte Bezeichner wie `a`. Die Vorgeneration führte diesen Text als Programm aus (3 von 3 Markerzugriffe), der neue Parser nicht (0 von 3). Für jede Abweichung gibt es jetzt einen deckenden Test: 4 von 4 Tests fallen an der Vorgeneration und bestehen am Kandidaten.
- **Aber:** Mit Tab oder Zeilenumbruch als Trenner weist der neue Parser 12.206 von 16.166 Ausdrücken ab. Diese Ausdrücke berechnen die Vorgeneration und die versiegelte Normalversion gleich. Nach deinem Maßstab ist S1 damit nicht sauber behoben.
- **Zusätzlich im Organ:** Der Verhaltensvergleich deckt je Funktion, nicht je Abweichung. Grundsatz 11 ist damit nicht wörtlich umgesetzt.

**Punkt (2), Gedächtnissperre-Test:** Er kann weiter rot werden, und zwar an der vorgesehenen Zusicherung.
- Rot wird er, wenn die Regel immer oder nie sperrt, und wenn Schreib- und Lesestelle beide fehlen.
- Fehlt nur die Schreibstelle, bleibt er grün (5 von 5), weil die Lesestelle allein hält.
- Ohne das TypeScript-Kammerimage werden 4 von 4 Fällen übersprungen. In der Regression liefen alle 4 und bestanden.

**Zwischenbericht-Wächter:** Er löst jetzt zusätzlich bei 80 % Kontextfüllung und bei der ersten gescheiterten Verdichtung aus, je Turn einmal.
- Tests: 12 von 12 grün.
- Gegenproben: 10 von 10 scheitern an der vorab benannten Zusicherung.
- Nachspiel an der gestorbenen Sitzung: Der neue Wächter hätte um 16:01 (Verdichtung gescheitert) und um 16:48 (80,6 % Kontext) ausgelöst. Der Rundenauslöser löste dort nie aus (höchstens 77 von 150 Runden).
- Der Zeitplan ruft die neue Fassung auf. In dieser Sitzung hat der Rundenauslöser um 22:00 bei Runde 110 echt ausgelöst.

**Nach dem Commit neu gefunden**
- **K2904:** Im zweiten Durchgang am Commit wurde er abgelehnt, wegen eines Laufzeitrisses im Bereich `eingang`, den er nicht berührt (×1,224). Im ersten und dritten Durchgang überlebt er.
- **Gepaarte Laufzeitmessung:** Fehlen dem Kandidaten Werte in einzelnen Bereichen, meldet die Messung trotzdem „gültig“. Gemessen an einem Python-Kandidaten mit Syntaxfehler: 3 von 4 Bereichen ohne Wert. Dafür liegt eine rote Spezifikation im Ordner, die an `330b4ec` fällt.

**Eigene Entscheidungen**
- Den Grundwert habe ich in die Datei geschrieben. Dein `/model` galt nur für die Unterhaltung: Nach dem Zurücksetzen lief die Anfrage um 19:45 wieder über moa und endete mit HTTP 429.
- Den Beleg habe ich an einem frischen Prozess geführt statt am Gateway. Ein Mitschnitt im Gateway hätte jede Anfrage samt Verlauf auf die Platte geschrieben.
- Ob Weißraum „gültig“ ist, habe ich an der versiegelten Normalversion entschieden, weil der Vertrag schweigt.
- Nach dem einen Review habe ich keinen neuen Code mehr geschrieben. Die offenen Code-Befunde liegen stattdessen als rote Spezifikationen im Ordner.

**Sperren:** keine. Die Ausführungsschicht lehnte einmal einen Hintergrundstart mit `nohup` ab; derselbe Befehl lief dann als verfolgter Hintergrundprozess, wie die Meldung es verlangte. Drei Lesebefehle markierte der Sicherheitsscan, die automatische Freigabe ließ sie durch.

**Offen für dich**
1. Gehört Weißraum außer dem Leerzeichen zur Tarifsprache?
2. Soll vor T4 eine Python-Sonde für den Verhaltensvergleich gebaut werden, oder wird die Torzeile angepasst?
3. Die Laufzeitgrenze trifft auch Bereiche, die der Kandidat nicht berührt. Soll sie auf den Wirkungskreis beschränkt werden, oder soll ein Riss vor der Ablehnung einmal gepaart bestätigt werden?
4. Soll der Verhaltensvergleich je Abweichung statt je Funktion decken?
5. Soll der Wächter je Turn oder je Sitzung einmal auslösen?
```

### V329 · 23.09. 22:29:14 CEST · Hermes · Nachricht id 14623 · Sitzung `20260923_194003_92313ee1` · 879 B

```text
Die beiden Meldungen kommen von Läufen, deren Ergebnisse schon im Bericht stehen. Am Ergebnis ändert sich nichts.

- **`proc_69ef4dafef08`** war der erste Wächterlauf mit dem 19:21-Fehlauslöser, den ich danach behoben habe. Veröffentlicht ist der korrigierte Lauf: letzter Ordner `…-192500-r3-verdichtung`, echter Wächterzustand unberührt. Das habe ich eben über HTTPS nachgeprüft.
- **`proc_96f705bab38f`** war der Commit- und Regressionsjob. Sein Ergebnis (475 bestanden, 2 übersprungen, 0 fehlgeschlagen) steht schon im Bericht.

Die Freigabeabfrage eben hat meine Nachprüfung ausgelöst: ein reiner Lesebefehl, `curl … | python3`, eingeordnet als Freigabe und von dir erteilt. Ich schlage dafür keine Dauerfreigabe vor, weil das Muster „Download direkt in einen Interpreter“ zu Recht gesperrt ist. Künftig lade ich zuerst in eine Datei und lese sie dann.
```

### V330 · 23.09. 22:32:40 CEST · Philipp · Nachricht id 14624 · Sitzung `20260923_194003_92313ee1` · 1804 B

```text
Richtig, nicht abgenommen — und die fehlende Python-Sonde ist der wichtigste Fund: T4 wäre gegen „schneller, aber falsch" ungeschützt gewesen. Entscheidungen Chat-Claude zu deinen fünf Fragen: (1) Weißraum gehört zur Tarifsprache, soweit die versiegelte Normalversion ihn rechnet — S1 ist an K2868 damit nicht sauber behoben, das korrigiert den T3-Befund, und mein Prüfstein „K2868 muss bestehen" war falsch; prüf dasselbe an K3044, der S1-Behebung aus Lauf 38, und korrigiere die Schwächenzählung von Lauf 38, falls nötig. (2) Python-Sonde vor T4, die Torzeile bleibt — Grundsatz 11 gilt für jede Sprache. (3) Kein Wirkungskreis, der selbst noch nicht verlässlich ist; stattdessen wird jeder Laufzeitriss vor der Ablehnung einmal gepaart nachgemessen, und nur ein bestätigter Riss lehnt ab. (4) Deckung je Abweichung, wie Grundsatz 11 es sagt. (5) Wächter je Turn. Auftrag Behebungsrunde 2 vor T4: Python-Sonde im selben Umfang wie die TypeScript-Sonde (einzeln, Folge, Alias, Mutation, Rücksetzung); Korpus aus den Verträgen mit Randfällen und Varianten der Eingabeform — die Weißraumlücke zeigt, dass Randwerte allein nicht reichen; Deckung je Abweichung; Bestätigungsmessung vor jeder Laufzeitablehnung; eine gepaarte Messung mit fehlenden Werten ist ungültig, deine rote Spezifikation wird grün; die vier Gedächtnissperre-Tests werden ohne Kammerimage rot statt übersprungen. Gegenproben durch den Laufweg: K2868 wird mit dem erweiterten Korpus abgelehnt; K2904 und K3091 werden in drei von drei Durchgängen gleich entschieden; an einem Python-Prüfwerk scheitert ein eingebauter Zwischenspeicher-Fehler. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, Abschlussordner laeufe/biotop-vor-t4-02/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

### V331 · 23.09. 23:53:57 CEST · Hermes-Zwischentext · Nachricht id 14718 · Sitzung `20260923_194003_92313ee1` · 140 B

```text
Jetzt der erste echte Kammerlauf der Python-Sonde am Prüfwerk, direkt über `verhaltensvergleich.pruefen` (Diagnose vor den Laufweg-Tests).
```

### V332 · 24.09. 00:18:47 CEST · Hermes-Zwischentext · Nachricht id 14796 · Sitzung `20260923_194003_92313ee1` · 101 B

```text
Während die Vorprüfung läuft: der Bericht wird vorbereitet (mit Platzhaltern), dazu die Übergabe.
```

### V333 · 24.09. 00:29:27 CEST · Hermes-Zwischentext · Nachricht id 14815 · Sitzung `20260923_194003_92313ee1` · 135 B

```text
Alle 18 Laufweg- und Kammertests grün. Jetzt Gegenprobe der vier Gedächtnissperre-Tests ohne Image, dann Commit und volle Regression.
```

### V334 · 24.09. 00:31:07 CEST · Hermes-Zwischentext · Nachricht id 14825 · Sitzung `20260923_194003_92313ee1` · 147 B

```text
Commit `6243377` steht; die volle Regression läuft (~25 min), danach drei Nachspiel-Durchgänge. Inzwischen der Prüfauftrag für das eine Review.
```

### V335 · 24.09. 00:38:48 CEST · Hermes · Nachricht id 14856 · Sitzung `20260923_194003_92313ee1` · 318 B

```text
Commit `6243377` steht. Die volle Regression mit anschließend drei Nachspiel-Durchgängen läuft im Hintergrund (`proc_72cfe583df40`), das Review ebenfalls (`deleg_ce891021`). Beide melden sich, wenn sie fertig sind; dann fülle ich die Platzhalter in `BERICHT.md` und veröffentliche nach `laeufe/biotop-vor-t4-02/`.
```

### V336 · 24.09. 01:10:58 CEST · Hermes · Nachricht id 14919 · Sitzung `20260923_194003_92313ee1` · 1067 B

```text
Die volle Regression an `6243377` ist fertig: 493 bestanden, 2 übersprungen, 0 fehlgeschlagen, Verdrahtungstest grün.

Eine Gegenprobe des Auftrags ist gescheitert. K2904 und K3091 wurden nur in 2 von 3 Durchgängen gleich entschieden. K3091 wurde im dritten Durchgang abgelehnt, weil `planung` nur um 13,7 % statt der geforderten 15 % schneller war. Ich habe die Nachmessung vor der Ablehnung nur für Laufzeitrisse gebaut, nicht für diese Gewinnschwelle; dafür liegt jetzt ein roter Test im Ordner, der an `6243377` scheitert.

K2868 wird am Commit wie verlangt abgelehnt: 40 von 40 Abweichungen ungedeckt.

Die Verdichtung scheitert im Gateway weiter: „Error code: 401 … OAuth access token has been revoked“. Meine Aussage aus der Vorrunde, sie laufe wieder, war falsch; sie stimmte nur für einen frischen Prozess. Ein Neustart des Gateways von außen dürfte das beheben.

Der Bericht ist fertig bis auf den Review-Abschnitt. Sobald das Review zurück ist, arbeite ich es ein, veröffentliche nach `laeufe/biotop-vor-t4-02/` und schicke die Endmeldung.
```

### V337 · 24.09. 02:10:34 CEST · Hermes · Nachricht id 14991 · Sitzung `20260923_194003_92313ee1` · 5006 B

```text
**Nicht abgenommen.** Eine Gegenprobe des Auftrags ist gescheitert: K2904 und K3091 wurden nur in 2 von 3 Durchgängen gleich entschieden. Außerdem hat das Review an der neuen Python-Sonde fünf Lücken gemessen, durch die T4 weiter nicht gegen „schneller, aber falsch“ geschützt ist.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-02/BERICHT.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-02/DATEIEN.txt

Ordnerprüfsumme: `6076535a348704b4a4ba6fad58508ff1a57e8eb0f726e659c1e514636e9178a0`. Alle 59 von 59 Dateien sind über HTTPS bytegleich, die Webseite antwortet mit 200. Biotop-Modellgeld 0,00 €. Der Code liegt im Commit `6243377` auf `330b4ec`. Volle Regression: 493 bestanden, 2 übersprungen, 0 fehlgeschlagen; der Verdrahtungstest ist grün.

**Bitte starte das Gateway von außen neu.** Die Verdichtung scheitert dort weiterhin mit „Error code: 401 … 'OAuth access token has been revoked.'“, zuletzt um 01:08:49. Meine Aussage in der Vorrunde, sie laufe wieder, war falsch; sie stimmte nur für einen frischen Prozess, nicht für das Gateway. Der Wächter hat den Fehlschlag erkannt und Zwischenberichte abgelegt.

**Zu deinen Punkten**
- **S1 an K3044:** ebenfalls nicht sauber behoben. K3044 nimmt Tab an, weist aber alle 12.206 Ausdrücke mit Zeilenumbruch ab, die die Normalversion rechnet; K2868 weist Tab und Zeilenumbruch ab. Neue Schwächenzählung:
  - Lauf 38: 3 von 5 = 60 % statt 80 %, die Schwelle von 80 % ist damit nicht erreicht.
  - Lauf 37: 2 von 5 = 40 % statt 60 %.
- **Python-Sonde:** im Umfang der TypeScript-Sonde gebaut. Am Python-Prüfwerk gilt durch den Annahmepfad:
  - Der eingebaute Zwischenspeicher-Fehler scheitert.
  - Derselbe Speicher am Inhalt überlebt.
  - Die Weißraum-Änderung scheitert an einer Formvariante.
- **Lücken der Python-Sonde laut Review, jede in der Kammer gemessen:**
  - Generatoren: eine geänderte Ausgabe ergibt 0 Abweichungen.
  - Änderungen an den Eingaben an Ort und Stelle: 0 Abweichungen.
  - Funktionen, deren Aufrufe nur Fehler liefern, gelten trotzdem als beobachtet.
  - Zufällige Hash-Reihenfolge erzeugt 22 Fehlalarme.
  - `@lru_cache` wird nicht eingewickelt: 16 von 16 Fehlalarme.
- **Deckung je Abweichung:** gebaut, mit Probe und Gegenprobe. Gemessen deckt ein richtiger Test damit aber nur 2 von 28 Abweichungen. Behebungen auf dem Lastpfad sind so praktisch nicht annehmbar.
- **K2868:** mit dem erweiterten Korpus abgelehnt, 40 von 40 Abweichungen ungedeckt. Ob der Korpus allein das bewirkt oder die neue Deckungsregel, ist nicht getrennt gemessen.
- **Bestätigungsmessung:** gebaut für Laufzeitrisse; die Probe durch den Annahmepfad ist grün. Mit echter Messung lief sie nie, weil in 0 von 7 Nachspielen ein Riss auftrat.
- **Nicht gebaut: die Nachmessung vor der Gewinnschwelle der Nische „schnell“.** K3091 wurde im dritten Durchgang genau dort abgelehnt, mit −13,7 % statt mindestens 15 %. Das ist der Grund für die gescheiterte Gegenprobe. Dafür gibt es rote Spezifikationen: 2 von 4 Tests scheitern an `6243377`, beide Gegenproben sind grün.
- **Fehlende Werte:** Eine gepaarte Messung mit fehlendem Wert ist jetzt ungültig. Die rote Spezifikation der Vorrunde ist grün, auch an einem echten Python-Werk nachgemessen.
- **Gedächtnissperre-Tests:** ohne Kammerimage 4 von 4 rot, mit Image 4 von 4 grün.
- **Wächter:** löst je Turn aus.

**Eigene Entscheidungen**
- Nach dem einen Review habe ich keinen Code mehr geändert. Die 22 Befunde, davon 6 hoch, stehen als 13 Spezifikationen in `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`.
- S1 gilt als sauber behoben nur, wenn der Marker nicht ausgeführt wird und jeder Ausdruck, den die Normalversion rechnet, gleich gerechnet wird, mit Leerzeichen, Tab und Zeilenumbruch.
- Nicht bestätigte Laufzeitrisse nehme ich aus dem Urteil aus; bei „nicht bestätigt“ bleibt die erste Messung die Grundlage.

**Sperren:** Bei mir gab es keine; drei Befehle hast du freigegeben. Der Reviewer hatte eine Formatsperre und eine Sicherheitssperre auf ein nur lesendes Skript. Danach hat er Teile derselben Daten auf anderem Weg gelesen und das selbst als Verstoß gegen die Regel „keinen anderen Weg suchen“ gemeldet. Aus diesem Teil übernehme ich keine Zahl, die nicht auch aus den veröffentlichten Belegen folgt.

**Zu entscheiden, bevor die nächste Runde baut**
1. Welche Deckungsregel soll gelten: dieselbe Eingabe je Muster, Deckung je Eingabe ohne Muster, oder eine Verfälschungsprobe (der Test muss fallen, wenn das aufgezeichnete Ergebnis verfälscht wird)?
2. Soll die Gewinnschwelle der Nische „schnell“ in beiden Richtungen nachgemessen werden, also vor einer Ablehnung und vor einer Annahme?
3. Sollen Methoden von Klassen vor T4 beobachtet werden, oder gelten sie als benannte Grenze mit Enthaltung?
4. Soll S1 neu versiegelt werden, damit das Kriterium Weißraum einschließt? Bisher prüft es nur den Marker.
```

### V338 · 24.09. 02:14:45 CEST · Philipp · Nachricht id 15154 · Sitzung `20260923_194003_92313ee1` · 3490 B

```text
Richtig nicht abgenommen, und die Lücken der Python-Sonde gehören zu den wichtigsten Befunden vor T4. Entscheidungen Chat-Claude: (1) Deckung je Muster (deine Option 1) — je Eingabe ist zu fein, ein richtiger Test deckt 2 von 28; je Funktion zu grob, dahinter lag die Weißraum-Lücke. Gegenproben: K2868 scheitert am ungedeckten Weißraum-Muster; eine richtige Behebung mit einem Test je Muster kommt durch; K2868 wird einmal nur mit erweitertem Korpus und einmal nur mit neuer Deckungsregel gemessen, damit getrennt ist, was was bewirkt. (2) Gewinnschwelle der Nische „schnell" in beiden Richtungen nachmessen, nur innerhalb der Rauschtoleranz um die Schwelle; Gegenprobe K2904/K3091 drei von drei gleich — kippt es trotzdem, meld es, dann liegt es an der Größe der Vergleichslast. (3) Methoden von Klassen vor T4 beobachten, Instanzen aus den Verträgen, Zustand von self vor und nach dem Aufruf verglichen; Enthaltung nur für wirklich Unbeobachtbares, gezählt. (4) S1 nicht neu versiegeln — nach der Messung ändert man kein Kriterium; für jedes künftige Testwerk prüft jeder Gegenzeuge zweierlei: Schwäche weg und gültiges Verhalten gegen die Normalversion unverändert. Auftrag Behebungsrunde 3: deine 13 Spezifikationen aus SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md plus diese vier Entscheidungen, jede mit Gegenprobe durch den Laufweg; die fünf Lücken der Python-Sonde je mit einem Fall, der vorher unentdeckt blieb oder Fehlalarm gab. Der Reviewer ist an dieselbe Regel gebunden wie du: bei einer Sicherheitssperre anhalten und melden, nie auf anderem Weg lesen. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, Abschlussordner laeufe/biotop-vor-t4-03/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.Richtig nicht abgenommen, und die Lücken der Python-Sonde gehören zu den wichtigsten Befunden vor T4. Entscheidungen Chat-Claude: (1) Deckung je Muster (deine Option 1) — je Eingabe ist zu fein, ein richtiger Test deckt 2 von 28; je Funktion zu grob, dahinter lag die Weißraum-Lücke. Gegenproben: K2868 scheitert am ungedeckten Weißraum-Muster; eine richtige Behebung mit einem Test je Muster kommt durch; K2868 wird einmal nur mit erweitertem Korpus und einmal nur mit neuer Deckungsregel gemessen, damit getrennt ist, was was bewirkt. (2) Gewinnschwelle der Nische „schnell" in beiden Richtungen nachmessen, nur innerhalb der Rauschtoleranz um die Schwelle; Gegenprobe K2904/K3091 drei von drei gleich — kippt es trotzdem, meld es, dann liegt es an der Größe der Vergleichslast. (3) Methoden von Klassen vor T4 beobachten, Instanzen aus den Verträgen, Zustand von self vor und nach dem Aufruf verglichen; Enthaltung nur für wirklich Unbeobachtbares, gezählt. (4) S1 nicht neu versiegeln — nach der Messung ändert man kein Kriterium; für jedes künftige Testwerk prüft jeder Gegenzeuge zweierlei: Schwäche weg und gültiges Verhalten gegen die Normalversion unverändert. Auftrag Behebungsrunde 3: deine 13 Spezifikationen aus SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md plus diese vier Entscheidungen, jede mit Gegenprobe durch den Laufweg; die fünf Lücken der Python-Sonde je mit einem Fall, der vorher unentdeckt blieb oder Fehlalarm gab. Der Reviewer ist an dieselbe Regel gebunden wie du: bei einer Sicherheitssperre anhalten und melden, nie auf anderem Weg lesen. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, Abschlussordner laeufe/biotop-vor-t4-03/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

### V339 · 24.09. 02:15:47 CEST · Hermes · Nachricht id 14993 · Sitzung `20260923_194003_92313ee1` · 83 B

*Wiederholung von V032* (gleicher Absender, gleicher Wortlaut).

### V340 · 24.09. 02:15:47 CEST · Hermes-Zwischentext · Nachricht id 14995 · Sitzung `20260923_194003_92313ee1` · 22462 B

*Nicht abgedruckt:* Verdichtungszusammenfassung, ein Systemtext mit Kontextmarken und keine Nachricht an Philipp (R208). Der Wortlaut steht in der Sitzungsdatenbank, die gesichert ist (SICHERUNG).

### V341 · 24.09. 02:15:47 CEST · Hermes-Zwischentext · Nachricht id 15001 · Sitzung `20260923_194003_92313ee1` · 140 B

*Wiederholung von V331* (gleicher Absender, gleicher Wortlaut).

### V342 · 24.09. 02:15:47 CEST · Hermes-Zwischentext · Nachricht id 15079 · Sitzung `20260923_194003_92313ee1` · 101 B

*Wiederholung von V332* (gleicher Absender, gleicher Wortlaut).

### V343 · 24.09. 02:15:47 CEST · Hermes-Zwischentext · Nachricht id 15098 · Sitzung `20260923_194003_92313ee1` · 135 B

*Wiederholung von V333* (gleicher Absender, gleicher Wortlaut).

### V344 · 24.09. 02:15:47 CEST · Hermes-Zwischentext · Nachricht id 15108 · Sitzung `20260923_194003_92313ee1` · 147 B

*Wiederholung von V334* (gleicher Absender, gleicher Wortlaut).

### V345 · 24.09. 02:15:47 CEST · Hermes · Nachricht id 15123 · Sitzung `20260923_194003_92313ee1` · 318 B

*Wiederholung von V335* (gleicher Absender, gleicher Wortlaut).

### V346 · 24.09. 02:15:47 CEST · Hermes · Nachricht id 15136 · Sitzung `20260923_194003_92313ee1` · 1067 B

*Wiederholung von V336* (gleicher Absender, gleicher Wortlaut).

### V347 · 24.09. 02:15:47 CEST · Hermes · Nachricht id 15153 · Sitzung `20260923_194003_92313ee1` · 5006 B

*Wiederholung von V337* (gleicher Absender, gleicher Wortlaut).

### V348 · 24.09. 02:20:51 CEST · Hermes-Zwischentext · Nachricht id 15171 · Sitzung `20260923_194003_92313ee1` · 74 B

```text
Jetzt den Code der Sonde neu lesen (die Zusammenfassung trägt ihn nicht).
```

### V349 · 24.09. 03:31:25 CEST · Hermes-Zwischentext · Nachricht id 15235 · Sitzung `20260923_194003_92313ee1` · 162 B

```text
Umfang ist groß; ich schreibe zuerst die Python-Sonde neu (eigene Datei aus Runde 2, daher Vollersatz statt Ankerpatches), dann Host-Seite, TS-Seite, Messgerät.
```

### V350 · 24.09. 04:36:34 CEST · Hermes-Zwischentext · Nachricht id 15283 · Sitzung `20260923_194003_92313ee1` · 65 B

```text
Jetzt die TS-Seite (Runner, Aufzeichner, Kanon) im selben Umfang.
```

### V351 · 24.09. 05:05:12 CEST · Hermes-Zwischentext · Nachricht id 15361 · Sitzung `20260923_194003_92313ee1` · 125 B

```text
Teillauf grün (rc 0, 103 Fälle). Jetzt die Laufweg-Tests der Runde 3: fünf Lücken, Entscheidungen 1–4, Spezifikationen.
```

### V352 · 24.09. 05:10:02 CEST · Hermes · Nachricht id 15368 · Sitzung `20260923_194003_92313ee1` · 5006 B

*Wiederholung von V337* (gleicher Absender, gleicher Wortlaut).

### V353 · 24.09. 05:30:29 CEST · Hermes · Nachricht id 15678 · Sitzung `20260923_194003_92313ee1` · 6955 B

```text
**Runde 3 ist nicht fertig und nicht geliefert.** Dieser Turn hat die Höchstzahl an Werkzeugaufrufen erreicht. Es gibt noch keinen Commit, keine volle Regression, kein Review und keinen Ordner `laeufe/biotop-vor-t4-03/`, deshalb auch keine Abholadresse und keine Prüfsumme.

**Repo:** HEAD ist unverändert `6243377`, alle Änderungen liegen uncommittet im Arbeitsbaum. Git-Geschichte, versiegelter Ordner und Webseite habe ich nicht angefasst.

**Gebaut, noch nicht committet**
- **Python-Sonde, neu geschrieben.** Sie vergleicht:
  - Generator-Ausgaben;
  - den Zustand der Argumente nach dem Aufruf;
  - Ergebnisse gegen eine Kopie derselben Eingabe, um Zwischenspeicher zu erkennen.

  Dazu:
  - feste Hash-Saat (`PYTHONHASHSEED=0`);
  - Einwickeln über `__wrapped__`, damit auch `lru_cache`-Funktionen erfasst werden;
  - Methoden und Eigenschaften von Klassen, mit Instanzen aus den Vertragstests und dem Zustand von `self` nach dem Aufruf.

  Als „beobachtet“ zählt eine Funktion nur, wenn beide Seiten ein inhaltliches Ergebnis liefern.
- **Vergleich:**
  - Eine Abweichung gilt nur als gedeckt, wenn der Test sein Muster trifft und fällt, sobald das Ergebnis verfälscht wird.
  - Die Vorgeneration wird zweimal beobachtet; was dabei schwankt, zählt als Enthaltung.
  - Zweimal Zeitlimit am Kandidaten ist ein Befund; ein Aufzeichner, der nichts aufzeichnet, ist ein Messgerätausfall.
  - Schalter, mit denen K2868 einmal nur mit erweitertem Korpus und einmal nur mit neuer Deckungsregel läuft.
- **TypeScript-Seite** im selben Umfang; neu ist `einwickeln.mjs`, das auch `export const` erfasst.
- **Gewinnschwelle „schnell“:** Nachmessung in beiden Richtungen, nur im Rauschband um die Schwelle.
- **Spezifikationen:**
  - S-9: Laufzeitrisse als Liste.
  - S-10: Die Vertragsprobe setzt ihre Zusicherung in eine Funktion, die die Referenzlast nicht erreicht.
  - S-11: zusätzliche Zusicherung in `test_vorspann`.

**Gemessen** (Belege in `/root/biotop-vor-t4-03/bau/`)
- **Rauchproben** der Sonde, Python und TypeScript: grün.
- **`TEILLAUF-1`**, drei bestehende Testdateien des Vergleichs: 103 von 103 grün, allerdings am Stand vor den letzten Änderungen. Dafür habe ich 3 Testdateien geändert, jede Stelle ist im Test begründet:
  - 15 Stellen: Die gestellte Kammer antwortet je Stand statt je Aufruf, weil die Vorgeneration jetzt zweimal beobachtet wird.
  - 6 Stellen: Deckungstests auf die Muster-Regel umgestellt.
- **`TEILLAUF-2`**, neue `tests/test_vor_t4_03.py` mit 30 Tests:
  - 15 rot, alle mit echter Kammer. Sie brachen schon bei der Basismessung ab, weil meinem Prüfwerk der Bereichsordner fehlte (Bandit: „No such file or directory“). Behoben.
  - Die übrigen 15 standen nicht in der Fehlerliste: Gewinnschwelle in 6 Fällen durch `aegis.pruefen` mit gestellter Kammer, S-3, S-9, S-12 und zwei Gegenproben am Vergleich selbst.
- **`TEILLAUF-3`**, die 17 Tests der Gruppen A, B und D: 8 rot, 9 nicht in der Fehlerliste. Eine Zeile mit der Zahl bestandener Tests habe ich in keinem der Läufe gesehen. Nicht rot sind unter anderem:
  - `lru_cache` ohne Fehlalarm, ein falscher Zwischenspeicher wird weiter abgelehnt;
  - Mengenreihenfolge ohne Fehlalarm;
  - eine Funktion ohne Annotation wird gesehen;
  - ein geänderter Zustand von `self` wird abgelehnt;
  - Methoden zählen im Nenner mit.
- **Die 8 roten:**
  - **3 abgelehnt, aber nicht vom Vergleich:** Generator (A1), Sortierung an Ort und Stelle (A2) und geänderte Methode (D).
    - Bei A1 und A2 fängt ein vorhandener Werkstest die Änderung über das Pareto-Maß.
    - Bei D habe ich die Ursache nicht nachgelesen.
    - Die Fälle „vorher unentdeckt“ muss ich so bauen, dass kein Werkstest sie sieht. Damit ist „Instanz aus dem Vertrag“ noch unbelegt.
  - **4 Deckungsfälle der Gruppe B:** Einen habe ich nachgelesen: Die Verfassung lehnt ab, weil neue Testdateien `tests/test_werk_…` heißen müssen. Die anderen drei haben dieselben Dateinamen.
  - **1 offen:** Die A2-Gegenprobe (`xs[:] = sorted(xs)` statt `xs.sort()`) wird an `~form#0` abgelehnt.
    - Vermutlich ist es die Behälter-Variante, also ein Tupel statt einer Liste: Beide Stände werfen, aber mit verschiedenem Fehlertyp. Das habe ich aus Schlüssel und Code geschlossen, nicht nachgemessen.
    - Nach deiner Regel aus Runde 1 brauchen auch Abweichungen bei ungültigen Eingaben einen deckenden Test. Dann ist meine Gegenprobe falsch gebaut, nicht die Sonde.
- **Danach geändert, noch nicht gelaufen:**
  - Bisher kam das Muster einer Beobachtung nur aus den variierten Stellen, und Aufrufe aus der Last hatten gar keins. Ein gewöhnlicher Test hätte so auch eine Last-Beobachtung mit Weißraum gedeckt, also genau die Lücke, die Entscheidung 1 schließen soll.
  - Jetzt zählen die Merkmale aller Argumente, gerechnet wie im Aufzeichner. Der Code kompiliert, ist aber ungetestet und kann das Ergebnis von `TEILLAUF-1` ändern.
  - Ebenfalls noch nicht gelaufen: die S-11-Zusicherung.

**Eigene Entscheidungen**
- **Rauschband:** 0,85 geteilt bzw. mal die gemessene Rauschtoleranz des Bereichs. Das ist derselbe Faktor, mit dem die Grenzmaße Rauschen tolerieren.
- **Widersprechen sich Erst- und Nachmessung**, entscheidet der Median über beide. Sonst bliebe der Grenzfall unentschieden, und nach Grundsatz 14 bekommt dieselbe Änderung dasselbe Urteil.
- **Deckung je Merkmal:** vor der Messung festgelegt, aber noch nicht gebaut; im Code steht bisher die Kombination.
  - Ein Muster gilt als gedeckt, wenn jedes seiner Merkmale von einem Test getroffen wird, der das Ergebnis der Funktion festhält.
  - Grund: Die Formarten der Sonde sind einzelne Merkmale, „ein Test je Muster“ heißt dann ein Test je Merkmal.
  - Die Kombination käme der zu feinen Regel „je Eingabe“ nahe.
  - Prüfmaß ist derselbe Fall wie in Runde 2, wo ein richtiger Test nur 2 von 28 Abweichungen deckte.

**Noch nicht begonnen**
- Doppelprüfung der Gegenzeugen (Entscheidung 4). Das versiegelte Skript bleibt unverändert, die Prüfung kommt daneben.
- Nachspiele: K2868 getrennt nach Korpus und Deckungsregel, K2904 und K3091 je dreimal.
- Die `REF_PAAR`-Umgehung zurücknehmen; die roten Spezifikationen aus Runde 2 am neuen Stand laufen lassen.
- Volle Regression, Commit, ein Review, Veröffentlichung, Endmeldung.

**Sonst**
- Die Verdichtung läuft seit deinem Gateway-Neustart um 02:14:04 wieder: 02:14:47–02:15:47 erfolgreich, 532 → 163 Nachrichten.
- **Mein Versäumnis:** `UEBERGABE.md` steht auf 03:40. Der Umbau des Prüfwerks, `TEILLAUF-2` und `TEILLAUF-3` sowie die Musteränderung stehen nur in dieser Nachricht und im Verlauf.
- Einen Zwischenbericht dieser Runde habe ich nicht geschrieben; ob der Wächter einen abgelegt hat, habe ich nicht geprüft.
- Biotop-Modellgeld: 0,00 €, das Modell war in allen Proben gestellt. Keine Sperren.

Mit deinem nächsten „weiter“ lasse ich zuerst die Teilläufe nach der Musteränderung neu laufen.
```

### V354 · 24.09. 06:12:27 CEST · Hermes · Nachricht id 15772 · Sitzung `20260923_194003_92313ee1` · 336 B

```text
Die Behebungsrunde 3 ist noch nicht fertig. Die Gruppen B und F, also Deckung je Muster und Gegenzeugen, sind jetzt grün: 12 von 12. Gerade laufen die übrigen Tests (Eichproben, Verdrahtung, Vorspann), danach automatisch Commit, volle Regression, Nachspiele und das Review. Die Endmeldung mit Abholadresse und Prüfsumme folgt danach.
```

### V355 · 24.09. 06:17:10 CEST · Hermes · Nachricht id 15783 · Sitzung `20260923_194003_92313ee1` · 1577 B

```text
Noch nicht geliefert. Die Doppelprüfung der Gegenzeugen (Entscheidung 4) ist durchgelaufen:

- **Normalversion:** behoben = ja, 0 Abweichungen.
- **Ursprung** mit versiegelter Schwäche: behoben = nein, der Marker schlägt weiter an.
- **K3044, beide Endstände und K2868:** behoben = nein. Die Schwäche ist zwar weg, aber das Verhalten weicht von der Normalversion ab, vor allem bei Ausdrücken mit Zeilenumbruch.
- Der versiegelte Ordner ist unverändert.

Die Summe „x von 117.732“ in dieser Ausgabe hat eine falsche Bezugsgröße. Der Leerzeichen-Teil zählte nur die gültigen Ausdrücke als Nenner, die Abweichungen aber über alle Fälle; der Nenner sind jetzt alle Fälle. Deshalb weist das Urteil jeden Teil einzeln als „x von y“ aus. Am Commit wird die Doppelprüfung mit dieser Rechnung neu gemessen.

Im Hintergrund läuft der Rest der Teilprüfung. Die Tests zu Deckung je Muster und Gegenzeugen sind schon grün (12 von 12), offen sind noch Eichproben, Verdrahtung und Vorspann. Sind sie grün, startet automatisch der Commit-Job:

1. Commit auf `6243377` und volle Regression.
2. Drei Nachspieldurchgänge: K2904/K3091 dreimal, K2868 in vier Fassungen (erweiterter Korpus und neue Deckungsregel je an oder aus).
3. Echte Rissprobe und Doppelprüfung der Gegenzeugen am Commit.
4. Neu: dieselben Fälle der Sonden-Lücken am alten Code von `6243377`. Damit wird gemessen, dass sie dort unentdeckt blieben oder Fehlalarm gaben.

Wenn der Job fertig ist, schreibe ich den Bericht und starte das eine Review. Danach folgen Veröffentlichung und Endmeldung.
```

### V356 · 24.09. 07:39:20 CEST · Hermes · Nachricht id 15818 · Sitzung `20260923_194003_92313ee1` · 2550 B

```text
Noch nicht geliefert. Commit `d54bf2f` liegt auf `6243377`, das eine Review läuft.

**Ergebnisse am Commit**
- **Gegenprobe K2904/K3091 wieder nur 2 von 3, damit gemeldet, wie du verlangt hast.**
  - Die Nachmessung an der Gewinnschwelle lief in 6 von 6 dieser Entscheidungen.
  - K2904 überlebt 3 von 3.
  - K3091 wurde in Durchgang 2 abgelehnt: erste Messung −12,7 %, Nachmessung −22,2 %, zusammen −14,8 % bei einer Schwelle von −15 %.
  - Über alle 9 gepaarten Messungen liegt K3091 im Median bei −17,0 % und in 3 von 9 über der Schwelle. Die Streuung (3,5 Punkte) ist größer als der Abstand zur Schwelle (2 Punkte). Nach deiner Vorgabe liegt es damit an der Größe der Vergleichslast.
- **K2868, getrennt gemessen:** Die Ablehnung kommt von der neuen Deckungsregel, nicht vom erweiterten Korpus.
  - Die neue Regel allein lehnt ab (12 von 12 Abweichungen ungedeckt).
  - Der erweiterte Korpus allein nicht: Nach alter Regel sind alle 40 gedeckt.
  - Mit beidem abgelehnt, 40 von 40 ungedeckt, davon 20 mit Weißraum-Muster.
  - Offen: In allen 40 Mustern steckt auch das Merkmal „Null“ aus einem Argument, das die Sonde gar nicht verändert hat. Ein deckender Test müsste es mittreffen.
- **Fünf Lücken der Python-Sonde, am alten Code `6243377` gemessen.** Dort waren Generator, Nebenwirkung an der Eingabe und Funktion ohne Annotation unentdeckt (0 zusätzliche Abweichungen). Die Mengenreihenfolge gab 36 Fehlalarme, `lru_cache` 16 weitere. Die Messung am neuen Code läuft noch.
- **Echte Rissprobe:** Die Nachmessung lief zum ersten Mal auf dem Laufweg; der bestätigte Riss wurde abgelehnt. Die Gegenprobe überlebt.
- **Gegenzeugen am Commit:**
  - Normalversion behoben, Ursprung nicht behoben.
  - K3044, beide Endstände und K2868 nicht behoben: Die Schwäche ist weg, aber das Verhalten weicht ab.
  - Der Siegelordner ist unverändert.
- **Regression am Commit: 532 bestanden, 2 übersprungen, 1 rot.** Rot ist die Sprachweichen-Prüfung (`test_t3_python_annahmen.py`): Zwei neue Funktionen der Sonde fehlten in ihrem Register. Die Datei war in keinem meiner Teilläufe, das ist mein Fehler.
  - Nachtrag-Commit `0aac612` ergänzt die beiden Einträge; am Code unter `biotop/` ändert er nichts.
  - Die volle Regression am Nachtrag läuft gerade.
- **Methoden von Klassen** werden in Python beobachtet, in TypeScript nicht. Das steht als offener Punkt im Bericht.

Danach arbeite ich die Review-Befunde ein, veröffentliche `laeufe/biotop-vor-t4-03/` und schicke die Endmeldung mit Abholadresse und Prüfsumme.
```

