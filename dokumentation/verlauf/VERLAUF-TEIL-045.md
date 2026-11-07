# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 045 von 054

- Einträge V0902 bis V0913. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0902 · 24.09.2026 05:30:29 CEST · Hermes · Nachricht id 15678 · Sitzung `20260923_194003_92313ee1` · 6955 B

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

### V0903 · 24.09.2026 06:12:27 CEST · Hermes · Nachricht id 15772 · Sitzung `20260923_194003_92313ee1` · 336 B

```text
Die Behebungsrunde 3 ist noch nicht fertig. Die Gruppen B und F, also Deckung je Muster und Gegenzeugen, sind jetzt grün: 12 von 12. Gerade laufen die übrigen Tests (Eichproben, Verdrahtung, Vorspann), danach automatisch Commit, volle Regression, Nachspiele und das Review. Die Endmeldung mit Abholadresse und Prüfsumme folgt danach.
```

### V0904 · 24.09.2026 06:17:10 CEST · Hermes · Nachricht id 15783 · Sitzung `20260923_194003_92313ee1` · 1577 B

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

### V0905 · 24.09.2026 07:39:20 CEST · Hermes · Nachricht id 15818 · Sitzung `20260923_194003_92313ee1` · 2550 B

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

### V0906 · 24.09.2026 08:01:21 CEST · Hermes · Nachricht id 15881 · Sitzung `20260923_194003_92313ee1` · 1995 B

```text
Noch nicht geliefert. Das Review läuft noch. Veröffentlichung und Endmeldung kommen, sobald ich seine Befunde eingearbeitet habe.

**Nachtrag `0aac612`:**
- Volle Regression: 533 bestanden, 2 übersprungen, 0 fehlgeschlagen.
- Verdrahtungstest grün: 23 von 23 Organen gerufen, 0,00 € Modellkosten.
- Unter `biotop/` ist der Code unverändert gegenüber `d54bf2f`.

**Die fünf Lücken der Python-Sonde, vorher und nachher gemessen:** Es sind dieselben 17 Testfälle, einmal am alten Code `6243377` und einmal am neuen Code `0aac612`.

- **Zusicherungen:** Am neuen Code halten alle 17 von 17. Am alten Code hält nur 1 von 17; 2 weitere brechen ab, weil es die neuen Felder dort nicht gibt.
- **Geänderte Generator-Ausgabe:**
  - vorher unentdeckt (0 zusätzliche Abweichungen);
  - jetzt abgelehnt, 20 Abweichungen.
- **Nebenwirkung an der Eingabe:**
  - vorher unentdeckt;
  - jetzt abgelehnt, 36 Abweichungen.
- **Funktion ohne Annotation:**
  - vorher unentdeckt;
  - jetzt abgelehnt, 32 Abweichungen.
- **Mengenreihenfolge:**
  - vorher 36 Fehlalarme, abgelehnt;
  - jetzt überlebt, 0 Abweichungen.
- **`lru_cache`:**
  - vorher 16 zusätzliche Fehlalarme, abgelehnt;
  - jetzt überlebt, 0 Abweichungen.
- **Methoden:** Die Instanz kommt aus dem Vertragstest. Eine geänderte Methode wird abgelehnt (80 Abweichungen), ebenso ein nur veränderter Zustand von `self` (56 Abweichungen).
- **Deckung je Muster:**
  - Die richtige Behebung überlebt, 52 von 52 Abweichungen sind gedeckt.
  - Fehlen die Tests für das Weißraum-Muster, wird sie abgelehnt.
  - Ein Test, der die Funktion nur nebenbei ruft, deckt nichts.

**Das Urteil im Bericht steht auf „nicht abgenommen“**:
- K2904 und K3091 wurden nur in 2 von 3 Durchgängen gleich entschieden. Nach Chat-Claudes Vorgabe liegt das an der Größe der Vergleichslast.
- Methoden werden nur in Python beobachtet, nicht in TypeScript.
- Die Spezifikationen S-12 und S-3 (Wurzelmodul) sind nur am Organ belegt, nicht auf dem Laufweg.
```

### V0907 · 24.09.2026 08:50:22 CEST · Hermes · Nachricht id 15961 · Sitzung `20260923_194003_92313ee1` · 5445 B

````text
**Behebungsrunde 3 ist nicht geliefert.** Ich habe an Linie 3 angehalten: Zwei Sicherheitssperren haben meine Abschlussschritte blockiert, ich habe keine davon umgangen. Der Bericht trägt deshalb noch zwei Platzhalter (§10 Review, §11 Sperren). Das Veröffentlichungsskript bricht bei Platzhaltern ab, deshalb warten Veröffentlichung und Endmeldung.

**Sperre 1:** terminal, gegen 08:40
```
mkdir -p /root/biotop-vor-t4-03/review-proben && cd /tmp/review-vor-t4-03 && for f in *.py *.json *.txt *.sh; do cp -p "$f" /root/biotop-vor-t4-03/review-proben/; done; cd /root/biotop-vor-t4-03/review-proben && ls | wc -l && for f in *; do [ "$(sha256sum < $f)" = "$(sha256sum < /tmp/review-vor-t4-03/$f)" ] || echo "ABWEICHUNG $f"; done; echo "kopien geprueft"; /root/biotop-t3/venv/bin/python - <<'EOF'
…liest /root/.local/share/tirith/log.jsonl (Zahl der Einträge)…
EOF
```
„Blocked: command or referenced script cannot restart, stop, or uninstall the gateway from inside the gateway process. The gateway would kill this command before it could complete (SIGTERM propagates to child processes). Run `hermes gateway restart` from a separate shell outside the running gateway.“

**Sperre 2:** execute_code, kurz nach 08:44. Das Skript sollte den Bericht fertigstellen: §10/§11 füllen und die Befunde des Reviews einarbeiten. Außerdem sollte es die Datei `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md` anlegen und zwei Einträge in `veroeffentlichen.py` ergänzen.
„Blocked: cannot restart or stop the gateway from inside the gateway process. The gateway would kill this script before it could complete (SIGTERM propagates to child processes). Run the lifecycle command from a shell outside the gateway.“

**Einordnung:**
- Beide Male Sicherheitsfilter, Linie 3. Keiner der Befehle ruft das Gateway auf.
- Bei Sperre 2 vermute ich als Auslöser, dass das Skript die Meldung von Sperre 1 samt `hermes gateway restart` zitiert. Das ist nicht geprüft. Bei Sperre 1 kenne ich den Auslöser nicht.
- Nachgeprüft: nichts kopiert, nichts geschrieben.
- Mein Fehler: Ich habe zweimal unabhängige Handlungen in einen Befehl gebündelt.
- Belege mit vollem Wortlaut stehen in `sperre/SPERRE-KOPIE-GUTACHTERPROBEN.txt` und `sperre/SPERRE-2-BERICHT-ABSCHLUSS.txt`. Eine unveränderte Abschrift von Skript 2 liegt in `bau/bericht_abschluss_gesperrt.py`; ausgeführt habe ich sie nicht.

**Zu entscheiden:** Gibst du beide Handlungen frei? Dann führe ich die Abschrift unverändert aus, kopiere die Proben und veröffentliche `laeufe/biotop-vor-t4-03/`. Die Endmeldung kommt mit Abholadresse und Prüfsumme.

**Fertig und gemessen**
- **Commits:** `d54bf2f` auf `6243377`, dazu Nachtrag `0aac612` (nur Sprachweichen-Register). Die Geschichte ist nicht umgeschrieben.
- **Volle Regression an `0aac612`:** 533 bestanden, 2 übersprungen, 0 fehlgeschlagen. Verdrahtungstest grün, 23 von 23 Organen gerufen. Biotop-Modellgeld 0,00 €.
- **Fünf Lücken der Python-Sonde, gemessen an denselben 17 Fällen:** Am alten Code `6243377` halten 1 von 17 Zusicherungen, am neuen 17 von 17.
  - Generator: 20 Abweichungen, abgelehnt.
  - Nebenwirkung an der Eingabe: 36 Abweichungen, abgelehnt.
  - Funktion ohne Annotation: 32 Abweichungen, abgelehnt.
  - Die Fehlalarme sind weg: Mengenreihenfolge und `lru_cache` ergeben je 0 Abweichungen, der Kandidat überlebt.
- **K2904/K3091: wieder nur 2 von 3.** K3091 lag in Durchgang 2 zusammengerechnet bei −14,8 % gegen die Schwelle −15 %. Über 9 Messungen streut seine Quote mit 3,5 Punkten und liegt nur 2 Punkte von der Schwelle entfernt. Nach eurer Vorgabe liegt es damit an der Größe der Vergleichslast.
- **K2868, getrennt gemessen (2×2):**

  | Korpus | Regel je Funktion | Regel je Muster |
  |---|---|---|
  | alt | 12 Abweichungen, alle gedeckt, überlebt | 12 von 12 ungedeckt, abgelehnt |
  | erweitert | 40 Abweichungen, alle gedeckt, überlebt | 40 von 40 ungedeckt, abgelehnt |

  Die Ablehnung kommt damit von der neuen Deckungsregel.
- **Methoden von Klassen:** in Python gebaut, die Instanz kommt aus dem Vertrag. In TypeScript nicht gebaut.
- **Gegenzeugen prüfen zweierlei:** Die Normalversion gilt als behoben. K3044, beide Endstände und K2868 gelten nicht als behoben: Die Schwäche ist weg, aber das Verhalten weicht von der Normalversion ab.

**Review (ein Durchgang): 18 Befunde, 4 hoch, 5 mittel, 9 niedrig.** Alle nachgerechneten Zahlen sind bestätigt. Die vier hohen Befunde, alle in der Kammer gemessen:
1. Ein Test mit doppeltem Leerzeichen deckt einen Rückschritt bei Tab und Zeilenumbruch. Das ist die K2868-Lage, und der Kandidat überlebt. Grund: Alle Weißraumarten fallen in ein Merkmal.
2. Ein Test deckt auch mit einem Aufruf, den er nicht zusichert. Grund: Die Verfälschungsprobe verfälscht jeden Aufruf der Funktion, nicht nur den mit dem passenden Muster.
3. Die Sonde ersetzt jedes Iterator-Objekt durch einen Generator. Die Last bricht dann still ab, eine spätere Änderung bleibt unsichtbar.
4. Bei `__slots__`-Klassen wird der Zustand von `self` nach dem Aufruf nicht verglichen: 0 statt 28 Abweichungen.

Gelesen, nicht gemessen: Auch Tests, die ein Kandidat mitbringt, können decken. Ein Kandidat kann die Befunde 1 und 2 also selbst ausnutzen. Nach dem Review habe ich keinen Code mehr gebaut. Im Bericht steht deshalb „nicht abgenommen“, und die Aussage zu den fünf Lücken ist dort auf „für ihre Probenfälle geschlossen“ zurückgenommen.
````

### V0908 · 24.09.2026 11:38:00 CEST · Philipp · Nachricht id 15962 · Sitzung `20260923_194003_92313ee1` · 734 B

```text
Richtig angehalten. Philipp gibt für genau diesen Fall frei, nicht als Dauerregel: Trenn die gebündelten Schritte in einzelne Befehle; übernimm den Wortlaut der Sperren im Bericht aus den gespeicherten Dateien, statt ihn in einem Befehl zu zitieren; lass das Auszählen von /root/.local/share/tirith/log.jsonl ganz weg — der Bericht braucht es nicht. Sperrt danach noch ein einzelner Schritt, halt an; dann führt Philipp ihn von außen aus. Prüf außerdem, ob der Wächter in dieser Runde Zwischenberichte abgelegt hat, und trag das Ergebnis in §11 ein. Dann Bericht fertigstellen, laeufe/biotop-vor-t4-03/ veröffentlichen, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme. Keine Codeänderung mehr in dieser Runde.
```

### V0909 · 24.09.2026 11:46:30 CEST · Hermes · Nachricht id 15991 · Sitzung `20260923_194003_92313ee1` · 5518 B

```text
**Nicht abgenommen.** K2904 und K3091 wurden wieder nur in 2 von 3 Durchgängen gleich entschieden. Außerdem hat das Review vier neue schwere Lücken gemessen: zwei in der Deckungsregel je Muster, zwei in der Python-Sonde.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-03/BERICHT.md
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-03/DATEIEN.txt

Ordnerprüfsumme: `2b88a6c7e0a0bb3e31f580971dd88e70d22bc7d830be8bbe84b1a3b4249e973a`. Alle 85 von 85 Dateien sind über HTTPS bytegleich, die Webseite antwortet mit 200. Biotop-Modellgeld 0,00 €.

Der Code liegt in `d54bf2f` auf `6243377`, dazu der Nachtrag `0aac612`. Volle Regression an `0aac612`: 533 bestanden, 2 übersprungen, 0 fehlgeschlagen; der Verdrahtungstest ist grün. An `d54bf2f` war 1 Test rot: Im Sprachweichen-Register fehlten zwei neue Funktionen der Sonde. Ursache und Nachtrag stehen in §8. Code habe ich nicht mehr geändert, `/root/biotop` steht sauber auf `0aac612`.

**Zu deinen Punkten**
- **Getrennte Schritte:** keine weitere Sperre. Einzeln ausgeführt:
  - Proben des Prüfers kopiert, 17 von 17 bytegleich, im Ordner als `review_*`.
  - Bericht per Skript fertiggestellt. Den Wortlaut beider Sperren liest das Skript aus den gespeicherten Belegen.
  - Spezifikationen angelegt und Quellenliste ergänzt, dann veröffentlicht.
  - Das Protokoll der Ausführungsschicht habe ich nicht ausgezählt.
- **Wächter (§11):** Er hat in dieser Runde zwei Zwischenberichte abgelegt, beide im ersten Turn:
  - 05:11 bei Werkzeugrunde 113 von 150;
  - 05:19 bei Werkzeugrunde 141 von 150.

  Beide sind mit 5 von 5 Dateien bytegleich und in `DATEIEN.txt` verlinkt. Wegen Kontextfüllung oder gescheiterter Verdichtung hat der Wächter nicht ausgelöst: Von 8 Einträgen in seiner Liste stammen 2 aus dieser Runde, beide von den Rundenschwellen. Mein Fehler: Beide Zwischenberichte tragen die Übergabe vom Stand 03:40.

**Ergebnis der Runde**
- **Fünf Lücken der Python-Sonde:** An denselben 17 Fällen hielten am alten Code 1 von 17 Zusicherungen, am neuen 17 von 17. Geschlossen sind sie damit für diese Probenfälle.
- **K3091, Durchgang 2:** zusammengerechnet −14,8 % gegen die Schwelle von −15 %, also abgelehnt. Über 9 Messungen streut die Quote um 3,5 Punkte, der Median liegt nur 2 Punkte vor der Schwelle. Nach Chat-Claudes Vorgabe liegt das an der Größe der Vergleichslast.
- **K2868, getrennt gemessen:** Die Ablehnung bewirkt die Deckungsregel je Muster, nicht der erweiterte Korpus.
  - Mit der neuen Regel sind 12 von 12 bzw. 40 von 40 Abweichungen ungedeckt.
  - Mit der alten Regel ist alles gedeckt, K2868 überlebt.
- **Methoden:** In Python werden sie beobachtet, die Instanz kommt aus dem Vertrag, der Zustand von `self` wird verglichen. In TypeScript ist das nicht gebaut.
- **Gegenzeugen mit doppelter Prüfung:** Die Normalversion gilt als behoben. K3044, beide Endstände und K2868 nicht: Die Schwäche ist weg, aber das Verhalten weicht ab.
- **Bestätigungsmessung:** Sie lief zum ersten Mal echt auf dem Laufweg. Der Riss wurde bestätigt und abgelehnt, die Gegenprobe überlebt.

**Review:** 18 Befunde, 4 hoch, 5 mittel, 9 niedrig. Alle nachgerechneten Zahlen sind bestätigt. Die vier hohen, alle in der Kammer gemessen:
1. Ein Test mit doppeltem Leerzeichen deckt einen Rückschritt bei Tab und Zeilenumbruch. Die K2868-Lage überlebt damit.
2. Ein Test deckt mit einem Aufruf, den er gar nicht zusichert. Grund: Die Verfälschungsprobe verfälscht jeden Aufruf der Funktion, nicht nur den mit passendem Muster.
3. Die Sonde ersetzt zurückgegebene Iterator-Objekte durch Generatoren. Die Last bricht dann still ab, und eine Änderung bleibt unsichtbar.
4. Bei `__slots__`-Klassen wird der Zustand von `self` nicht verglichen: 0 statt 28 Abweichungen.

Nach dem Review habe ich keinen Code mehr gebaut. Alles steht als R4-1 bis R4-20 in `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`.

**Eigene Entscheidungen** (Auswahl, vollständig in §12)
- Die Deckung habe ich „je Merkmal“ gelesen. Zusammen mit dem groben Weißraum-Merkmal führt das zu Befund 1.
- Widersprechen sich zwei Gewinnmessungen, entscheidet der gemeinsame Median beider Messungen.
- Den Registerfehler habe ich mit einem Nachtrag-Commit behoben statt `d54bf2f` zu ändern, danach lief die volle Regression erneut.
- Die Zwischenberichte des Wächters sind in `DATEIEN.txt` verlinkt, aber nicht im Manifest, weil sie eigene Prüfsummen haben.

**Offen für Philipp**
1. Vergleichslast der Nische „schnell“ vergrößern. Ohne das bleibt „3 von 3 gleich“ für K3091 Zufall.
2. Die vier hohen Befunde vor T4 beheben. Dazu die Frage: Soll Weißraum je Zeichen getrennt werden (Tab, Zeilenumbruch, CR, NBSP, doppeltes Leerzeichen)?
3. Gehören Merkmale von Argumenten, die die Sonde nicht verändert hat, zum Muster? Bei K2868 verlangt jedes der 40 Muster das Merkmal `null_zahl`.
4. Dürfen Tests decken, die der Kandidat selbst mitbringt? Nach dem Code (gelesen, nicht gemessen) ja; damit kann ein Kandidat Befund 1 und 2 selbst ausnutzen.
5. Methoden in TypeScript bauen; und festlegen, wo die doppelte Prüfung der Gegenzeugen verbindlich laufen soll.
6. Die Gateway-Sperre hat zweimal Befehle ohne Gateway-Bezug getroffen. Soll ich das als Fehlalarm melden?

Die Lehre aus den zwei Sperren steht jetzt im Skill `audit-channel-delivery`: ein Schritt je Befehl, und den Wortlaut einer Sperre nur aus ihrer Belegdatei übernehmen.
```

### V0910 · 24.09.2026 11:49:51 CEST · Philipp · Nachricht id 15992 · Sitzung `20260923_194003_92313ee1` · 1811 B

```text
Sauber veröffentlicht, und die getrennten Schritte liefen ohne Sperre. Entscheidungen Chat-Claude zu deinen sechs Punkten: (1) Vergleichslast: zweite Stufe mit zehnfacher Eingabegröße je Bereich, ein Kammerlauf bleibt unter einer Minute; an ihr misst die Nische „schnell" den Gewinn und jede Nische ihre Laufzeitgrenze; Gegenprobe im Nachspiel: K2904 und K3091 drei von drei gleich; T3s Ergebnisse bleiben unverändert. (2) Die vier hohen Befunde vor T4; jede Formvariante, die die Sonde erzeugt, ist ein eigenes Merkmal — Weißraum also je Zeichen. (3) Merkmale von Argumenten, die die Sonde nicht verändert hat, gehören nicht zum Muster; Gegenprobe: Die Abweichungen bei ungültigen Eingaben von K2868 sind gedeckt, die Weißraum-Muster bleiben ungedeckt. (4) Tests, die der Kandidat selbst mitbringt, decken nicht — ein Vorschlag beglaubigt seine eigene Änderung nie; decken dürfen Tests der Vorgeneration, aus Generation 0, vom Ankläger und die versiegelten Gegenzeugen; Gegenprobe: Ein Kandidat mit Rückschritt und eigenem Test, der genau diesen Rückschritt zusichert, wird abgelehnt. (5) Methoden in TypeScript vor T5, nicht vor T4; die doppelte Gegenzeugen-Prüfung ist verbindlich in der Torzeile „Schwächen", nicht im Annahmepfad. (6) Den Fehlalarm als sachlichen Text mit Befehlsmuster und Sperrwortlaut in den Abschlussordner legen, ohne Projektinterna; ob er eingereicht wird, entscheidet Philipp. Auftrag Runde 4: diese sechs Punkte plus aus R4-1 bis R4-20 alles, was T4 gefährden würde — der Rest mit Begründung auf die Liste. Die Übergabe nach jedem abgeschlossenen Schritt nachführen, damit die Zwischenberichte nicht veralten. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, laeufe/biotop-vor-t4-04/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

### V0911 · 24.09.2026 14:09:46 CEST · Hermes · Nachricht id 16229 · Sitzung `20260923_194003_92313ee1` · 2456 B

```text
Runde 4 ist noch nicht fertig und nicht geliefert. Commit `1d9a5aa` liegt auf `0aac612`. Die volle Regression läuft, danach im selben Job die Nachspiele und der Vorher/Nachher-Vergleich; anschließend startet automatisch ein Nachtrag.

**Gebaut**
- **Vergleichslast Stufe 2:** Jeder Bereich läuft mit zehnfacher Eingabegröße, Stufe 1 bleibt unverändert.
  - Ein Kammerlauf dauert jetzt 8,6 bis 11,7 s, alle 12 von 12 Läufen unter 60 s.
  - Die `planung`-Quote sinkt dort auf etwa 0,40. An Stufe 1 lag sie direkt an der Schwelle 0,85: bei K3091 mit 0,839 knapp darunter, bei K2904 mit 0,851 knapp darüber.
  - Die erste Fassung der Last überschritt den Wertebereich des Werks. Das ist korrigiert und belegt.
- **Die vier hohen Review-Befunde:**
  - Jede Formvariante ist ein eigenes Merkmal, in Python und TypeScript nachweislich gleich gerechnet.
  - Die Verfälschungsprobe gilt je Merkmal. Fixture-Fehler zählen nicht mehr als Festhalten.
  - Nur echte Generatoren werden ersetzt.
  - Klassen mit `__slots__` werden jetzt verglichen.
  - Der Lastabbruch unter der Sonde folgt im Nachtrag.
- **Muster:** zählen nur Merkmale, die die Sonde selbst verändert hat.
- **Eigene Tests des Kandidaten decken nicht mehr.** Liegt derselbe Test schon in der Vorgeneration, deckt er (Gegenprobe).
- **Doppelprüfung der Gegenzeugen:** jetzt verbindlich in der Torzeile „Schwächen“. Am T3-Werk ergibt sie 0 von 5, S2 bis S4 sind nicht beurteilbar, weil ihr Normalverhalten nie gemessen wurde. Der versiegelte Gegenzeuge allein ergab 4 von 5. Das ist eine Feststellung, keine Neubewertung von T3.
- **Fehlalarm des Sicherheitsfilters:** als sachlicher Text ohne Projektinterna im Abschlussordner.

**Tests**
- Breiter Teillauf: 347 grün, 1 übersprungen, 3 rot. Die 3 roten Tests setzten das alte gemeinsame Weißraum-Merkmal voraus und sind angepasst, mit Notiz an jeder Stelle.
- Mein Fehler: Der Teillauf vor dem Commit schloss die neue Testdatei `test_vor_t4_04.py` per Filter versehentlich aus. Voll gelaufen ist sie nur im breiten Teillauf, ab jetzt in der Regression.

**Formatsperre:** ein lesender Sammelbefehl wurde gesperrt. Nach der Regel habe ich das gespeicherte Skript unverändert ausgeführt; der Beleg liegt in `sperre/`.

Als Nächstes laufen der Nachtrag mit eigener Regression und das eine Review. Danach fülle ich den Bericht, veröffentliche `laeufe/biotop-vor-t4-04/` und schicke die Endmeldung mit Abholadresse und Prüfsumme.
```

### V0912 · 24.09.2026 15:09:22 CEST · Hermes · Nachricht id 16290 · Sitzung `20260923_194003_92313ee1` · 1638 B

```text
Runde 4 ist noch nicht geliefert: Die Regression am Nachtrag läuft, danach wiederholen sich die Nachspiele, und das eine Review ist gestartet.

**Ergebnisse des Commit-Jobs**
- **Volle Regression an `1d9a5aa`:** 562 bestanden, 2 übersprungen, 0 fehlgeschlagen.
- **Nachspiele an `1d9a5aa` fehlgeschlagen:** Alle 7 von 7 brachen ohne Urteil ab: „AttributeError: module 'biotop.organe.eichung' has no attribute 'get'“.
  - Ursache war mein Fehler: In `nachspiel.vorbereiten` hat ein Import die Maßeichung des Falls überschrieben.
  - Die Regression konnte das nicht fangen, weil sie keine Nachspiele enthält.
  - Behoben und durch einen Wächtertest abgesichert. Eine Probe am Arbeitsbaum läuft jetzt durch: K2904 überlebt an Stufe 2 mit `bericht` −29 % und `planung` −59 %.
- **Vorher/Nachher an denselben 23 Testfällen:** am alten Code `0aac612` 6 von 23 grün, am neuen `1d9a5aa` 23 von 23. Damit ist gemessen, dass die vier hohen Befunde vorher bestanden und jetzt geschlossen sind.
- **Torzeile „Schwächen“ am T3-Werk:** unverändert 0 von 5. Das ist eine Feststellung, keine Neubewertung von T3.

**Nachtrag-Commit `43b8fad` auf `1d9a5aa`:**
- Nachspiel repariert.
- Bricht die Last unter der Sonde ab, zählt das jetzt als Messgerätausfall.
- Tests für die Torzeile ergänzt.
- Teillauf 64 von 64 grün.
- Regression am Nachtrag und danach die Nachspiele N1 bis N3 laufen. Sie liefern die eigentliche Gegenprobe: K2904 und K3091 gleich in 3 von 3 Durchgängen, außerdem K2868.

Danach fülle ich den Bericht und veröffentliche `laeufe/biotop-vor-t4-04/`. Die Endmeldung kommt mit Abholadresse und Prüfsumme.
```

### V0913 · 24.09.2026 16:10:36 CEST · Hermes · Nachricht id 16441 · Sitzung `20260923_194003_92313ee1` · 1667 B

```text
Noch nicht geliefert: Das eine Review läuft noch. Veröffentlichung und Endmeldung folgen danach.

**Nachtrag `43b8fad`:**
- Volle Regression: 569 bestanden, 2 übersprungen, 0 fehlgeschlagen. Verdrahtungstest grün, 0,00 € Modellgeld.
- **Gegenprobe K2904/K3091 erfüllt:** In 3 von 3 Durchgängen haben beide Kandidaten überlebt. An der neuen Vergleichslast (zehnfache Eingabegröße) liegt die `planung`-Quote bei 0,38 bis 0,46. Jeder Gewinn liegt damit klar unter der Schwelle, eine Nachmessung war nie nötig.
- **Bestätigungsmessung erstmals in einem Nachspiel wirksam:** Bei K3091 riss im dritten Durchgang die Laufzeit in zwei Bereichen, die der Kandidat nicht berührt. Die Nachmessung bestätigte keinen der beiden Risse, der Kandidat überlebte.
- **K2868 abgelehnt, 24 von 40 Abweichungen ungedeckt:**
  - Gedeckt sind jetzt die ungültigen Eingaben (Anforderung aus Entscheidung 3) und die Großschreibung.
  - Ungedeckt bleiben 20 Weißraum-Varianten wie verlangt, dazu 4 mit führender Null.
  - Die Normalversion nimmt eine führende Null an; welche Werte K2868 dort liefert, steht nicht im Beleg.
- **Fehler von mir:** An `1d9a5aa` brachen alle 7 Nachspiele ohne Urteil ab. Ein Import hatte im Nachspiel die Maßeichung überschrieben, und die Regression prüft keine Nachspiele. Der Nachtrag behebt das und sichert es mit einem Test ab, der die fehlerhafte Fassung erkennt.
- **Offener Punkt:** Die Last des Bereichs `eingang` streut an Stufe 2 so stark, dass die Rauschmessung ihn in 3 von 6 Nachspielen von K2904/K3091 gesperrt hat. Die beiden ändern `eingang` nicht. Ein Kandidat, der `eingang` ändert, würde aber an der Sperre scheitern.
```

