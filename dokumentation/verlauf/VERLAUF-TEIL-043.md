# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 043 von 054

- Einträge V0877 bis V0888. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0877 · 23.09.2026 22:28:40 CEST · Hermes · Nachricht id 14619 · Sitzung `20260923_194003_92313ee1` · 5734 B

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

### V0878 · 23.09.2026 22:29:14 CEST · Hermes · Nachricht id 14623 · Sitzung `20260923_194003_92313ee1` · 879 B

```text
Die beiden Meldungen kommen von Läufen, deren Ergebnisse schon im Bericht stehen. Am Ergebnis ändert sich nichts.

- **`proc_69ef4dafef08`** war der erste Wächterlauf mit dem 19:21-Fehlauslöser, den ich danach behoben habe. Veröffentlicht ist der korrigierte Lauf: letzter Ordner `…-192500-r3-verdichtung`, echter Wächterzustand unberührt. Das habe ich eben über HTTPS nachgeprüft.
- **`proc_96f705bab38f`** war der Commit- und Regressionsjob. Sein Ergebnis (475 bestanden, 2 übersprungen, 0 fehlgeschlagen) steht schon im Bericht.

Die Freigabeabfrage eben hat meine Nachprüfung ausgelöst: ein reiner Lesebefehl, `curl … | python3`, eingeordnet als Freigabe und von dir erteilt. Ich schlage dafür keine Dauerfreigabe vor, weil das Muster „Download direkt in einen Interpreter“ zu Recht gesperrt ist. Künftig lade ich zuerst in eine Datei und lese sie dann.
```

### V0879 · 23.09.2026 22:32:40 CEST · Philipp · Nachricht id 14624 · Sitzung `20260923_194003_92313ee1` · 1804 B

```text
Richtig, nicht abgenommen — und die fehlende Python-Sonde ist der wichtigste Fund: T4 wäre gegen „schneller, aber falsch" ungeschützt gewesen. Entscheidungen Chat-Claude zu deinen fünf Fragen: (1) Weißraum gehört zur Tarifsprache, soweit die versiegelte Normalversion ihn rechnet — S1 ist an K2868 damit nicht sauber behoben, das korrigiert den T3-Befund, und mein Prüfstein „K2868 muss bestehen" war falsch; prüf dasselbe an K3044, der S1-Behebung aus Lauf 38, und korrigiere die Schwächenzählung von Lauf 38, falls nötig. (2) Python-Sonde vor T4, die Torzeile bleibt — Grundsatz 11 gilt für jede Sprache. (3) Kein Wirkungskreis, der selbst noch nicht verlässlich ist; stattdessen wird jeder Laufzeitriss vor der Ablehnung einmal gepaart nachgemessen, und nur ein bestätigter Riss lehnt ab. (4) Deckung je Abweichung, wie Grundsatz 11 es sagt. (5) Wächter je Turn. Auftrag Behebungsrunde 2 vor T4: Python-Sonde im selben Umfang wie die TypeScript-Sonde (einzeln, Folge, Alias, Mutation, Rücksetzung); Korpus aus den Verträgen mit Randfällen und Varianten der Eingabeform — die Weißraumlücke zeigt, dass Randwerte allein nicht reichen; Deckung je Abweichung; Bestätigungsmessung vor jeder Laufzeitablehnung; eine gepaarte Messung mit fehlenden Werten ist ungültig, deine rote Spezifikation wird grün; die vier Gedächtnissperre-Tests werden ohne Kammerimage rot statt übersprungen. Gegenproben durch den Laufweg: K2868 wird mit dem erweiterten Korpus abgelehnt; K2904 und K3091 werden in drei von drei Durchgängen gleich entschieden; an einem Python-Prüfwerk scheitert ein eingebauter Zwischenspeicher-Fehler. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, Abschlussordner laeufe/biotop-vor-t4-02/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

### V0880 · 23.09.2026 23:53:57 CEST · Hermes-Zwischentext · Nachricht id 14718 · Sitzung `20260923_194003_92313ee1` · 140 B

```text
Jetzt der erste echte Kammerlauf der Python-Sonde am Prüfwerk, direkt über `verhaltensvergleich.pruefen` (Diagnose vor den Laufweg-Tests).
```

### V0881 · 24.09.2026 00:18:47 CEST · Hermes-Zwischentext · Nachricht id 14796 · Sitzung `20260923_194003_92313ee1` · 101 B

```text
Während die Vorprüfung läuft: der Bericht wird vorbereitet (mit Platzhaltern), dazu die Übergabe.
```

### V0882 · 24.09.2026 00:29:27 CEST · Hermes-Zwischentext · Nachricht id 14815 · Sitzung `20260923_194003_92313ee1` · 135 B

```text
Alle 18 Laufweg- und Kammertests grün. Jetzt Gegenprobe der vier Gedächtnissperre-Tests ohne Image, dann Commit und volle Regression.
```

### V0883 · 24.09.2026 00:31:07 CEST · Hermes-Zwischentext · Nachricht id 14825 · Sitzung `20260923_194003_92313ee1` · 147 B

```text
Commit `6243377` steht; die volle Regression läuft (~25 min), danach drei Nachspiel-Durchgänge. Inzwischen der Prüfauftrag für das eine Review.
```

### V0884 · 24.09.2026 00:38:48 CEST · Hermes · Nachricht id 14856 · Sitzung `20260923_194003_92313ee1` · 318 B

```text
Commit `6243377` steht. Die volle Regression mit anschließend drei Nachspiel-Durchgängen läuft im Hintergrund (`proc_72cfe583df40`), das Review ebenfalls (`deleg_ce891021`). Beide melden sich, wenn sie fertig sind; dann fülle ich die Platzhalter in `BERICHT.md` und veröffentliche nach `laeufe/biotop-vor-t4-02/`.
```

### V0885 · 24.09.2026 01:10:58 CEST · Hermes · Nachricht id 14919 · Sitzung `20260923_194003_92313ee1` · 1067 B

```text
Die volle Regression an `6243377` ist fertig: 493 bestanden, 2 übersprungen, 0 fehlgeschlagen, Verdrahtungstest grün.

Eine Gegenprobe des Auftrags ist gescheitert. K2904 und K3091 wurden nur in 2 von 3 Durchgängen gleich entschieden. K3091 wurde im dritten Durchgang abgelehnt, weil `planung` nur um 13,7 % statt der geforderten 15 % schneller war. Ich habe die Nachmessung vor der Ablehnung nur für Laufzeitrisse gebaut, nicht für diese Gewinnschwelle; dafür liegt jetzt ein roter Test im Ordner, der an `6243377` scheitert.

K2868 wird am Commit wie verlangt abgelehnt: 40 von 40 Abweichungen ungedeckt.

Die Verdichtung scheitert im Gateway weiter: „Error code: 401 … OAuth access token has been revoked“. Meine Aussage aus der Vorrunde, sie laufe wieder, war falsch; sie stimmte nur für einen frischen Prozess. Ein Neustart des Gateways von außen dürfte das beheben.

Der Bericht ist fertig bis auf den Review-Abschnitt. Sobald das Review zurück ist, arbeite ich es ein, veröffentliche nach `laeufe/biotop-vor-t4-02/` und schicke die Endmeldung.
```

### V0886 · 24.09.2026 02:10:34 CEST · Hermes · Nachricht id 14991 · Sitzung `20260923_194003_92313ee1` · 5006 B

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

### V0887 · 24.09.2026 02:14:45 CEST · Philipp · Nachricht id 15154 · Sitzung `20260923_194003_92313ee1` · 3490 B · 2 gleiche Zeilen zusammengefasst

```text
Richtig nicht abgenommen, und die Lücken der Python-Sonde gehören zu den wichtigsten Befunden vor T4. Entscheidungen Chat-Claude: (1) Deckung je Muster (deine Option 1) — je Eingabe ist zu fein, ein richtiger Test deckt 2 von 28; je Funktion zu grob, dahinter lag die Weißraum-Lücke. Gegenproben: K2868 scheitert am ungedeckten Weißraum-Muster; eine richtige Behebung mit einem Test je Muster kommt durch; K2868 wird einmal nur mit erweitertem Korpus und einmal nur mit neuer Deckungsregel gemessen, damit getrennt ist, was was bewirkt. (2) Gewinnschwelle der Nische „schnell" in beiden Richtungen nachmessen, nur innerhalb der Rauschtoleranz um die Schwelle; Gegenprobe K2904/K3091 drei von drei gleich — kippt es trotzdem, meld es, dann liegt es an der Größe der Vergleichslast. (3) Methoden von Klassen vor T4 beobachten, Instanzen aus den Verträgen, Zustand von self vor und nach dem Aufruf verglichen; Enthaltung nur für wirklich Unbeobachtbares, gezählt. (4) S1 nicht neu versiegeln — nach der Messung ändert man kein Kriterium; für jedes künftige Testwerk prüft jeder Gegenzeuge zweierlei: Schwäche weg und gültiges Verhalten gegen die Normalversion unverändert. Auftrag Behebungsrunde 3: deine 13 Spezifikationen aus SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md plus diese vier Entscheidungen, jede mit Gegenprobe durch den Laufweg; die fünf Lücken der Python-Sonde je mit einem Fall, der vorher unentdeckt blieb oder Fehlalarm gab. Der Reviewer ist an dieselbe Regel gebunden wie du: bei einer Sicherheitssperre anhalten und melden, nie auf anderem Weg lesen. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, Abschlussordner laeufe/biotop-vor-t4-03/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.Richtig nicht abgenommen, und die Lücken der Python-Sonde gehören zu den wichtigsten Befunden vor T4. Entscheidungen Chat-Claude: (1) Deckung je Muster (deine Option 1) — je Eingabe ist zu fein, ein richtiger Test deckt 2 von 28; je Funktion zu grob, dahinter lag die Weißraum-Lücke. Gegenproben: K2868 scheitert am ungedeckten Weißraum-Muster; eine richtige Behebung mit einem Test je Muster kommt durch; K2868 wird einmal nur mit erweitertem Korpus und einmal nur mit neuer Deckungsregel gemessen, damit getrennt ist, was was bewirkt. (2) Gewinnschwelle der Nische „schnell" in beiden Richtungen nachmessen, nur innerhalb der Rauschtoleranz um die Schwelle; Gegenprobe K2904/K3091 drei von drei gleich — kippt es trotzdem, meld es, dann liegt es an der Größe der Vergleichslast. (3) Methoden von Klassen vor T4 beobachten, Instanzen aus den Verträgen, Zustand von self vor und nach dem Aufruf verglichen; Enthaltung nur für wirklich Unbeobachtbares, gezählt. (4) S1 nicht neu versiegeln — nach der Messung ändert man kein Kriterium; für jedes künftige Testwerk prüft jeder Gegenzeuge zweierlei: Schwäche weg und gültiges Verhalten gegen die Normalversion unverändert. Auftrag Behebungsrunde 3: deine 13 Spezifikationen aus SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md plus diese vier Entscheidungen, jede mit Gegenprobe durch den Laufweg; die fünf Lücken der Python-Sonde je mit einem Fall, der vorher unentdeckt blieb oder Fehlalarm gab. Der Reviewer ist an dieselbe Regel gebunden wie du: bei einer Sicherheitssperre anhalten und melden, nie auf anderem Weg lesen. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, Abschlussordner laeufe/biotop-vor-t4-03/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

### V0888 · 24.09.2026 02:15:47 CEST · Hermes · Nachricht id 14993 · Sitzung `20260923_194003_92313ee1` · 83 B

```text
Your request was not processed. Send it again if you still want me to carry it out.
```

