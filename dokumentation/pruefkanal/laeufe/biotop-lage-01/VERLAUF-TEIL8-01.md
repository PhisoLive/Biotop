# BIOTOP-LAGE-01 · Fassung 2 · `VERLAUF-TEIL8-01.md` (FK11) · Teil 8 von 10

- **Einträge:** V357–V385 (24.09. 08:01 bis 24.09. 19:52).
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST. Alle Zeiten CEST.
- **Übersicht, Menge und Regeln:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VERLAUF-TEIL1-01.md

---
### V357 · 24.09. 08:01:21 CEST · Hermes · Nachricht id 15881 · Sitzung `20260923_194003_92313ee1` · 1995 B

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

### V358 · 24.09. 08:50:22 CEST · Hermes · Nachricht id 15961 · Sitzung `20260923_194003_92313ee1` · 5445 B

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

### V359 · 24.09. 11:38:00 CEST · Philipp · Nachricht id 15962 · Sitzung `20260923_194003_92313ee1` · 734 B

```text
Richtig angehalten. Philipp gibt für genau diesen Fall frei, nicht als Dauerregel: Trenn die gebündelten Schritte in einzelne Befehle; übernimm den Wortlaut der Sperren im Bericht aus den gespeicherten Dateien, statt ihn in einem Befehl zu zitieren; lass das Auszählen von /root/.local/share/tirith/log.jsonl ganz weg — der Bericht braucht es nicht. Sperrt danach noch ein einzelner Schritt, halt an; dann führt Philipp ihn von außen aus. Prüf außerdem, ob der Wächter in dieser Runde Zwischenberichte abgelegt hat, und trag das Ergebnis in §11 ein. Dann Bericht fertigstellen, laeufe/biotop-vor-t4-03/ veröffentlichen, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme. Keine Codeänderung mehr in dieser Runde.
```

### V360 · 24.09. 11:46:30 CEST · Hermes · Nachricht id 15991 · Sitzung `20260923_194003_92313ee1` · 5518 B

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

### V361 · 24.09. 11:49:51 CEST · Philipp · Nachricht id 15992 · Sitzung `20260923_194003_92313ee1` · 1811 B

```text
Sauber veröffentlicht, und die getrennten Schritte liefen ohne Sperre. Entscheidungen Chat-Claude zu deinen sechs Punkten: (1) Vergleichslast: zweite Stufe mit zehnfacher Eingabegröße je Bereich, ein Kammerlauf bleibt unter einer Minute; an ihr misst die Nische „schnell" den Gewinn und jede Nische ihre Laufzeitgrenze; Gegenprobe im Nachspiel: K2904 und K3091 drei von drei gleich; T3s Ergebnisse bleiben unverändert. (2) Die vier hohen Befunde vor T4; jede Formvariante, die die Sonde erzeugt, ist ein eigenes Merkmal — Weißraum also je Zeichen. (3) Merkmale von Argumenten, die die Sonde nicht verändert hat, gehören nicht zum Muster; Gegenprobe: Die Abweichungen bei ungültigen Eingaben von K2868 sind gedeckt, die Weißraum-Muster bleiben ungedeckt. (4) Tests, die der Kandidat selbst mitbringt, decken nicht — ein Vorschlag beglaubigt seine eigene Änderung nie; decken dürfen Tests der Vorgeneration, aus Generation 0, vom Ankläger und die versiegelten Gegenzeugen; Gegenprobe: Ein Kandidat mit Rückschritt und eigenem Test, der genau diesen Rückschritt zusichert, wird abgelehnt. (5) Methoden in TypeScript vor T5, nicht vor T4; die doppelte Gegenzeugen-Prüfung ist verbindlich in der Torzeile „Schwächen", nicht im Annahmepfad. (6) Den Fehlalarm als sachlichen Text mit Befehlsmuster und Sperrwortlaut in den Abschlussordner legen, ohne Projektinterna; ob er eingereicht wird, entscheidet Philipp. Auftrag Runde 4: diese sechs Punkte plus aus R4-1 bis R4-20 alles, was T4 gefährden würde — der Rest mit Begründung auf die Liste. Die Übergabe nach jedem abgeschlossenen Schritt nachführen, damit die Zwischenberichte nicht veralten. Kein Lauf, kein Modellgeld, ein Review, eigener Commit, laeufe/biotop-vor-t4-04/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

### V362 · 24.09. 14:09:46 CEST · Hermes · Nachricht id 16229 · Sitzung `20260923_194003_92313ee1` · 2456 B

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

### V363 · 24.09. 15:09:22 CEST · Hermes · Nachricht id 16290 · Sitzung `20260923_194003_92313ee1` · 1638 B

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

### V364 · 24.09. 16:10:36 CEST · Hermes · Nachricht id 16441 · Sitzung `20260923_194003_92313ee1` · 1667 B

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

### V365 · 24.09. 16:42:27 CEST · Hermes · Nachricht id 16481 · Sitzung `20260924_150913_a9326d` · 3090 B

```text
Der Reviewdurchgang ist fertig und liegt in `/root/biotop-vor-t4-04/REVIEW.md`. Urteil: Die vier hohen Befunde aus Review 03 sind für ihre Probenfälle geschlossen, aber nicht als Fehlerklasse. Es gibt 18 neue Befunde: 2 hoch, 8 mittel, 8 niedrig.

**Was hält**
- Ich habe 14 von 16 Proben aus Gutachten 03 gegen `43b8fad` neu gefahren. Alle 14 verhalten sich wie verlangt.
- Die Gegenprobe zu Entscheidung 1 hält: K2904 und K3091 überleben an Stufe 2 je 3 von 3 Mal. Die `planung`-Quote liegt bei 0,376–0,455.
- Die Gegenprobe zu Entscheidung 3 hält: K2868 wird abgelehnt. 16 von 40 Abweichungen sind gedeckt, darunter die drei ungültigen Randfälle. Ungedeckt bleiben 20 Weißraum- und 4 Zahlform-Abweichungen.
- Die Gegenprobe zu Entscheidung 4 hält, geprüft durch `aegis.pruefen`.
- Die Zahlen des Berichts stimmen, soweit ich sie nachgerechnet habe, mit ihren Quellen überein. Einzige Abweichung: Der Median der Kammerlaufzeiten ist gepoolt 6,2 → 9,8 s statt 6,3 → 9,9 s.

**Hohe Befunde (in der Kammer gemessen)**
1. **Ein Test „hält fest“, ohne das Merkmal zu prüfen.** Es zählt jede Ausnahme im Testlauf, nicht nur eine fallende Zusicherung. Beispiel: Ein Test sichert nur zu, dass zweimaliges Normieren dasselbe ergibt wie einmaliges. Mit ihm überlebt ein Kandidat mit Tab-Rückschritt (x3). Ohne diesen Test wird er abgelehnt.
2. **`__slots__` mit Vererbung bleibt still.** Ändert ein Kandidat nur einen Slot der Basisklasse, findet die Prüfung 0 Abweichungen und nennt das Urteil tragfähig. Ändert er einen Slot der eigenen Klasse, sind es 28 Abweichungen (p22).

**Mittlere Befunde**
- Verschleierte Slot-Namen (`__x`) sind ebenfalls unsichtbar.
- `csv.DictReader` wird weiter ersetzt. Liest die Referenzlast ein Attribut davon (gemessen: `fieldnames`), fällt die Sonde aus, und laut Code wird dann jeder Kandidat des ganzen Laufs zurückgestellt.
- Ändert ein Kandidat nur die Elemente eines Iterator-Objekts, bleibt das still; es wird nur als Teil-Enthaltung gezählt.
- Die Kappe von 24 Verfälschungsläufen führt zur Ablehnung. R4-12 verlangte eine Enthaltung.
- Die Torzeile „Schwächen“ wird nirgends aufgerufen.
- Fehlt die Stufe-2-Last, misst der Lauf ohne Einspruch an Stufe 1 weiter.
- Lastaufrufe gelten immer als gewöhnliches Muster.
- `Path`-Rückgaben sehen für die Sonde alle gleich aus.

Für T4 gefährlich sind Nr. 1, 2, 4, 6, 7, 8 und 10.

**Nicht geprüft:** die JUnit-Zahlen und die Verdrahtungsbelege aus §8, `KASSE.md`, die TypeScript-Zweige, und Generalprobe und Verhandlung an Stufe 2 nur gelesen.

**Sperren:** Ein mehrteiliger Einzeiler von mir löste eine Freigabeabfrage der Sicherheitsprüfung aus. Du hast sie freigegeben, der Befehl lief, brach dann aber an einem Fehler in meinem eigenen Skript ab. Ich habe ihn nicht wiederholt. Befehl und Meldung stehen wörtlich in der Datei, die betroffenen Daten unter „Nicht geprüft“.

Außer `REVIEW.md` habe ich nur unter `/tmp/review-vor-t4-04/` geschrieben. `git status` von `/root/biotop` war vorher und nachher leer.

MEDIA:/root/biotop-vor-t4-04/REVIEW.md
```

### V366 · 24.09. 16:48:07 CEST · Philipp · Nachricht id 16482 · Sitzung `20260924_150913_a9326d` · 2257 B

```text
Runde 4 hat den wichtigsten Punkt geschafft: K2904 und K3091 an der größeren Last drei von drei gleich, weit von der Schwelle. Aber das Review sagt es selbst — geschlossen für die Probenfälle, nicht als Fehlerklasse. Runde 5 schließt Klassen, nicht Fälle; Entscheidungen Chat-Claude: (1) Vollständigkeitsprüfung: Nach jedem Erfassen eines Objekts wird geprüft, ob alle Datenattribute erfasst sind; fehlt eines, ist das eine gezählte Enthaltung, nie „0 Abweichungen, tragfähig". Die Fälle aus Review-Nr. 2, 3, 5 und 10 sind die Gegenproben; os.PathLike wird über os.fspath als Wert geführt. (2) Festhalten heißt fallende Zusicherung, keine beliebige Ausnahme (Nr. 1). (3) Ein Sondenausfall trifft nur die betroffene Funktion — ihre Beobachtungen enthalten sich, der Lauf geht weiter (Nr. 4); ersetzt werden nur echte Iteratoren, keine Objekte mit Attributen. (4) Kappe der Verfälschungsläufe: zurückstellen mit Grund und gezählt, gemessen an einem Kandidaten in T4-Größe (Nr. 6). (5) Verdrahtung über ein Register: Jede Funktion, deren Aufruf der Entwurf verlangt — Organe, Torzeilen, das Tor-4-Skript —, steht in einem Register, und der Verdrahtungstest verlangt jeden Eintrag im echten Lauf; das Tor-4-Skript wird gebaut und ruft die Torzeile „Schwächen" (Nr. 7) — zum dritten Mal war etwas gebaut und nie gerufen. Für T4 gilt als Normalvergleich einer Altlast das Verhalten der Vorgeneration über den Verhaltensvergleich; eine verhaltensändernde Altlast braucht einen unabhängigen Test aus der Altlastenliste. (6) Der Vorspann verweigert den Lauf ohne Stufe 2, mit Test bei gestellter Dauer über 60 s (Nr. 8); Stufe-2-Lasten werden wie Stufe 1 bemessen und geeicht, bis eingang nicht mehr sperrt. (7) Lastaufrufe tragen die Formmerkmale ihrer Eingabe (Nr. 9). (8) Aus den niedrigen: dieselbe Stufe für Eichproben, Toleranz und gespeicherte Maße (Nr. 14, 15); Ausschluss eigener Tests nach Testkennung einschließlich Parametrisierung (Nr. 16) — sonst unterläuft ein parametrisierter Test Entscheidung 4; das Nachspiel als echter Durchlauf in der Regression (Nr. 18). Kein Lauf, kein Modellgeld, ein Review, eigener Commit, laeufe/biotop-vor-t4-05/, Endmeldung mit Abholadresse als ganze Zeile und Prüfsumme.
```

### V367 · 24.09. 16:56:56 CEST · Hermes-Zwischentext · Nachricht id 16487 · Sitzung `20260924_150913_a9326d` · 95 B

```text
Ich beginne Runde 5: Arbeitsordner, Übergabe und Wächter zuerst, dann gezielt den Code lesen.
```

### V368 · 24.09. 17:00:16 CEST · Hermes · Nachricht id 16498 · Sitzung `20260924_150913_a9326d` · 3756 B

```text
Mein Durchgang ist fertig, aber `/root/biotop-vor-t4-04/REVIEW.md` stammt nicht von mir. Die Datei entstand um 16:42:10 (33.169 Bytes), während ich prüfte. Ihr Kopf beschreibt meinen eigenen Kammerlauf von 16:08–16:10 als ihren. Außerdem lag in meinem Ordner ein fremdes `abschluss.sh` (16:22). Offenbar lief eine zweite Instanz desselben Auftrags auf meinem Verlauf und meinem `/tmp`-Ordner. Ich habe die fremde Datei nicht überschrieben, weil das ihr Ergebnis unwiderruflich gelöscht hätte. Meine Fassung liegt deshalb in `/tmp/review-vor-t4-04/REVIEW-B.md` (sha256 `f265ea09…2f5e`).

**Du musst entscheiden, welche Fassung gilt.** Beide stützen sich auf denselben Kammerlauf und sind darin nicht unabhängig. Nur meine Fassung enthält die Probe x4 (Befund Nr. 1).

**Befunde: 19 in meiner Fassung, davon 3 hoch, 8 mittel, 8 niedrig.** Die vier hohen Befunde aus Review 03 sind für ihre Probenfälle geschlossen: Ich habe 14 der 16 alten Fallläufe gegen `43b8fad` wiederholt, alle verhalten sich wie spezifiziert. Die Gegenproben des Auftrags halten: K2904 und K3091 werden in 3 von 3 Durchgängen gleich entschieden, K2868 mit 16 gedeckten und 24 ungedeckten Abweichungen abgelehnt, E4 abgelehnt.

**Die wichtigsten 5 Befunde:**
1. **Hoch:** Ein Kandidat, dessen Rückschritt nur bei Eingaben ab 40 Zeichen greift (`ValueError`), überlebt `aegis.pruefen` (Probe x4). Grund ist die Lesart „Randwerte tragen kein Merkmal“: Randfall-Abweichungen haben damit das gewöhnliche Muster, und das deckt jeder festhaltende Test, auch ohne lange Eingabe.
2. **Hoch:** „Hält fest“ misst nicht, ob die Zusicherung fällt. Eine Eigenschafts-Zusicherung wie `normieren(normieren(x)) == normieren(x)` mit Tab zählt als festhaltend, obwohl der Rückschritt sie erfüllt. Der Kandidat überlebt, 6 von 6 Rückschritt-Beobachtungen gelten als gedeckt (Probe x3).
3. **Hoch:** `__slots__` sind nur für flache Klassen geschlossen. Ändert eine Methode einen geerbten Slot (p22) oder einen verschleierten `__x`-Slot (p21), gibt es 0 Abweichungen und das Urteil lautet „tragfähig“. Die Kontrollen zeigen 28 Abweichungen.
4. **Mittel:** Die Stufe 2 ist nicht in jedem Bereich zehnfach, sondern in 4 von 5. `tarife` ruft dieselben 150 Eingaben nur zehnmal auf. Außerdem gibt es die Stufe 2 nur für das T3-Werk: Jedes andere Werk fällt beim Laufstart ohne Warnung auf Stufe 1 zurück, und dieser Zweig läuft in keinem Test.
5. **Mittel:** Die Torzeile „Schwächen“ hat außer Tests und Belegskript keinen Aufrufer und ist damit nicht verbindlich verdrahtet. Für T4 lässt sie sich so nicht anwenden: Der Masterprompt sieht dort eine Altlastenliste ohne Normalversion vor, also wäre jede Altlast „nicht beurteilbar“ und die Zeile stünde immer bei 0 %.

Weitere mittlere Befunde:
- Die Stufe-2-Last von `eingang` wird in 3 von 7 Rauschmessungen gesperrt; an Stufe 1 in den Läufen 37/38 in keinem der 10 Bereiche.
- In den gespeicherten Maßen mischen sich Werte von Stufe 1 und Stufe 2.
- Wird ein zurückgegebenes Iterator-Objekt geändert, bleibt das unsichtbar, und das Urteil lautet trotzdem „tragfähig“.
- `csv.DictReader` wird ersetzt; jeder Kandidat eines solchen Werks wird zurückgestellt.

**Sperren:** keine.

**Schreibort-Nachweis:**
- Ich habe nur unter `/tmp/review-vor-t4-04/` geschrieben: `REVIEW-B.md`, die Proben- und Suchskripte mit ihren Ausgaben (`kammerprobe.py`, `x4probe.py`, `KAMMERPROBE.json`, `X4PROBE.json` u. a.), `werke/` mit 54 Probenwerk-Dateien und `tmp/` (am Ende leer). Die vollständige Liste steht in `REVIEW-B.md`.
- Unter `/root/` habe ich nichts geschrieben; `git status` von `/root/biotop` war am Ende leer.
- Die Lauf-DB war nur mit `mode=ro` geöffnet. Am Ende lief kein Container mehr.
```

### V369 · 24.09. 17:11:04 CEST · Hermes-Zwischentext · Nachricht id 16506 · Sitzung `20260924_150913_a9326d` · 85 B

```text
Schritt 0: Runde 4 abschließen. Zuerst die Review-Proben kopieren (eigener Schritt).
```

### V370 · 24.09. 17:19:52 CEST · Hermes-Zwischentext · Nachricht id 16517 · Sitzung `20260924_150913_a9326d` · 82 B

```text
Bericht 4 ist gefüllt. Jetzt die Veröffentlichung von Runde 4 (eigener Schritt).
```

### V371 · 24.09. 17:28:23 CEST · Hermes-Zwischentext · Nachricht id 16534 · Sitzung `20260924_150913_a9326d` · 60 B

```text
Ich lese jetzt gebündelt die Stellen, die Runde 5 berührt.
```

### V372 · 24.09. 18:38:23 CEST · Hermes-Zwischentext · Nachricht id 16585 · Sitzung `20260924_150913_a9326d` · 75 B

```text
Eichung läuft im Hintergrund. Ich lese die letzten Anker für die Patches.
```

### V373 · 24.09. 19:00:50 CEST · Hermes-Zwischentext · Nachricht id 16596 · Sitzung `20260924_150913_a9326d` · 173 B

```text
Die Vorprobe bestätigt die Regel für E2 (Absturzstelle = Testdatei, Meldung `AssertionError`/`Failed`), lokal und in der Kammer. Jetzt das Patchskript (alles-oder-nichts).
```

### V374 · 24.09. 19:03:47 CEST · Hermes-Zwischentext · Nachricht id 16603 · Sitzung `20260924_150913_a9326d` · 135 B

```text
Die Vorproben stehen (Stufe 2: `eingang` mit W 240 in 0 von 8 Rauschmessungen gesperrt, mit W 60 in 3 von 8). Jetzt den Umbau anwenden.
```

### V375 · 24.09. 19:04:00 CEST · Hermes-Zwischentext · Nachricht id 16608 · Sitzung `20260924_150913_a9326d` · 123 B

```text
Umbau angewandt (61 Ersetzungen in 10 Dateien). Jetzt der Diff der Signaturen und Importe gegen HEAD sowie ein Syntaxcheck.
```

### V376 · 24.09. 19:08:58 CEST · Hermes-Zwischentext · Nachricht id 16611 · Sitzung `20260924_150913_a9326d` · 82 B

```text
Umbau Teil 1 steht, Syntax sauber. Jetzt Tor-4-Skript und Register (neue Dateien).
```

### V377 · 24.09. 19:12:30 CEST · Hermes-Zwischentext · Nachricht id 16619 · Sitzung `20260924_150913_a9326d` · 115 B

```text
Jetzt die Tests: Drahtwerk um Stufe 2 und Altlastenliste erweitern, Verdrahtungstest um Register und Tor-4-Schritt.
```

### V378 · 24.09. 19:20:59 CEST · Hermes-Zwischentext · Nachricht id 16625 · Sitzung `20260924_150913_a9326d` · 68 B

```text
Jetzt die neue Testdatei mit Proben und Gegenproben je Entscheidung.
```

### V379 · 24.09. 19:21:08 CEST · Hermes-Zwischentext · Nachricht id 16627 · Sitzung `20260924_150913_a9326d` · 115 B

```text
Die Pyright-Meldungen betreffen nur Typannahmen, nicht die Laufzeit. Erster Teillauf über die neue Datei (Kammer).
```

### V380 · 24.09. 19:21:17 CEST · Hermes-Zwischentext · Nachricht id 16630 · Sitzung `20260924_150913_a9326d` · 170 B

```text
Während der Teillauf läuft, bereite ich die zweite Hälfte vor: den Nachspiel-Durchlauf in der Regression (Entscheidung 8, Review-Nr. 18) und die Messung in T4-Größe.
```

### V381 · 24.09. 19:33:19 CEST · Hermes-Zwischentext · Nachricht id 16649 · Sitzung `20260924_150913_a9326d` · 194 B

```text
Die gestellten Sonden in älteren Tests nehmen `**k` an, `transparent` passt also. Jetzt ein breiter Teillauf mit allen Sonden-, Aegis- und Wächter-Tests (ohne Verdrahtung), als Hintergrundjob.
```

### V382 · 24.09. 19:34:05 CEST · Hermes-Zwischentext · Nachricht id 16656 · Sitzung `20260924_150913_a9326d` · 111 B

```text
Während Teillauf 2 läuft, schreibe ich die Messung in T4-Größe (Entscheidung 4) als eigenständiges Skript.
```

### V383 · 24.09. 19:35:22 CEST · Hermes-Zwischentext · Nachricht id 16666 · Sitzung `20260924_150913_a9326d` · 58 B

```text
Warte auf Teillauf 2 (breite Regression ohne Verdrahtung).
```

### V384 · 24.09. 19:42:33 CEST · Hermes-Zwischentext · Nachricht id 16670 · Sitzung `20260924_150913_a9326d` · 55 B

```text
Bis 72 % ohne einen Fehlschlag. Ich warte auf das Ende.
```

### V385 · 24.09. 19:52:40 CEST · Hermes-Zwischentext · Nachricht id 16683 · Sitzung `20260924_150913_a9326d` · 95 B

```text
Die Kette läuft (Verdrahtungstest). Ich schreibe inzwischen `KASSE.md` und das Berichtgerüst.
```

