# BIOTOP-LAGE-01 · Fassung 2 · `LAGE-TEIL5-01.md`

- **Inhalt:** FK39 · Entwurf H, Stück 2 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil H, Arbeitszeit 25.09.2026 16:10:47–17:46:54 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/lage-offen/LAGE-BAUSTEINE-H-TEIL2.md` · 15160 B · SHA-256 `6798d5949be785fd9b0952a0e8768f50a635bac9dd2a1a95f9147b85bde7861e`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (4 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# LAGE-Bausteine H, Teil 2 von 3: FK39 — Offene Punkte

Entwurfsteil H der Offenlegung BIOTOP-LAGE-01 (Fassung 2), Baustein für `LAGE`. Quellen, Zeitzone und Zitierweise wie in
Teil 1. **Stand des Lesens:** 25.09.2026, 17:25 CEST. HEAD in `/root/biotop` ist zu diesem Zeitpunkt `0c2f058` vom 24.09.
20:24 (Runde 5); die Runde 6 ist nicht committet (`git log`, 17:22). Den Endstand von S1c und der Runde 6 trägt Hermes nach.

## Wie gezählt wurde

- **„Blockiert“** heißt hier: blockiert den nächsten Schritt, also den Abschluss der Runde 6 und den Start von T4 nach der
  Startregel. Wortlaut der Startregel, vorab gesetzt von Philipp: „T4 beginnt, sobald das Review dieser Runde keinen
  stillen Durchlass mehr findet — jede bekannte Lücke muss eine gezählte Enthaltung sein; Lücken, die sich nur enthalten,
  behebt T4 im Lauf.“ (UEBERGABE Runde 6, Z. 21–22). Was Hermes als nächsten Schritt vorschlägt, steht in FK46.
- **„Blockiert nicht“ im Wortlaut:** In keiner Biotop-Quelle gefunden. Gesucht wurde am 25.09. in allen `.md`-Dateien
  unter `/root` und im Prüfkanal nach „blockiert nicht“, „blockiert T4 nicht“, „blockiert keinen“ und „nicht
  blockierend“. Die Treffer liegen in anderen Vorhaben und in diesem Auftrag; im Biotop gibt es genau einen:
  `/root/reparatur-01/zwischenstand-05-entwurf/BEFUNDE.md`, Z. 36 („Die nicht blockierenden Empfehlungen
  EICH-S1/S2/S3 …“), veröffentlicht als `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-05/BEFUNDE.md`.
- **Die Berichte reichen offene Punkte mit anderen Wörtern weiter:** „auf der Liste“, „Liste nach T3“, „vor T5“, „nicht
  vor T4“, „bleiben offen“, „unbestätigt“, „nicht entschieden“. Auslegung Hermes: Gezählt wird je Punkt, wie viele
  Dokumente ihn mit einem solchen Vermerk weiterreichen, ohne ihn zu erledigen. Philipps Nachrichten zählen getrennt.
- **Kennungen „LU“ aus früheren Aufträgen:** NICHT GEFUNDEN (Suche nach „LU“ mit Ziffer in `/root/sicherung/biotop-lage-01/`
  und in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/OFFENE-PUNKTE-01.md`). LU01 usw. sind Kennungen dieses Auftrags (Auftrag v2, Z. 9).
- **Grundlage ist R52:** 52 Dokumente, nämlich Berichte, Übergaben, Spezifikationen, Einordnung und Nachgänge der Runden 1
  bis 6, dazu T3, Vorbedingung 1, Gesamtstand, Reparaturen und Gedächtnis. Veröffentlichte Kopien der Runden sind nicht
  doppelt gezählt. R52 zählt mechanisch und trifft auch Fehlwörter, etwa „Liste“ als Datentyp („Zahl, Liste,
  Wahrheitswert“). Die Zahlen unten hat Hermes je Fundstelle geprüft; der Rohwert aus R52 steht in Klammern, wo er
  abweicht.

## A. Runde 6: Bauteile vor T4 (in Arbeit)

Alle Punkte dieses Abschnitts sind **blockierend**. Philipp hat sie mit „Vor T4“ oder als Entscheidung für die Runde 6
angeordnet (24.09. 23:15:27, id 16901; UEBERGABE Runde 6, Z. 3–22). Gemeinsamer Stand um 12:52 (UEBERGABE Runde 6,
Z. 138–231): teils gebaut von S1 bis S4, geprüft von Hermes, nicht committet, ohne Review, nicht veröffentlicht; S1c baut.
Weitergereicht mit Aufschubvermerk wurde keiner dieser Punkte (0 Dokumente).

| Kennung | Was | Beleg | Folge, falls offen |
|---|---|---|---|
| R6-1, R6-8, R6-10 | Enthaltung je Beobachtung statt je Vergleich; enthält sich eine geänderte Funktion, wird der Kandidat zurückgestellt; Zeitgrenze je Funktion (Entscheidung 3) | SPEZ Runde 5, Z. 9, 16, 18; Philipp 24.09. 21:00:41 (id 16769) | Ein einziges schwer erfassbares Objekt stellt jeden Kandidaten zurück; eine hängende Last trifft den ganzen Kandidaten |
| R6-2 | Das Tor-4-Skript berechnet jede aus der Datenbank berechenbare Zeile (Entscheidung 5) | SPEZ Z. 10; gebaut von S2, geprüft 04:46 (UEBERGABE Z. 151–153) | Torzeilen von Hand, laut SPEZ Z. 10 die Quelle der meisten T3-Berichtsfehler |
| R6-3 | Stufe-2-Last in eigener Eichphase, versiegelt (Entscheidung 4) | SPEZ Z. 11; gebaut von S3 (UEBERGABE Z. 151–153) | Last nach Sperrzahl statt nach Maß |
| R6-4, R6-6 | Festhalten ohne Anführungszeichen, nur mit typtreuer Verfälschung (Entscheidung 1) | SPEZ Z. 12, 14 | Laut BERICHT Runde 5 §15 Nr. 1 hält für 5 von 8 geänderten Funktionen kein Test fest; auch richtige Behebungen würden abgelehnt |
| R6-7 | Undurchsichtige Objekte (Entscheidung 2) | SPEZ Z. 15 | „0 Abweichungen“ ohne Beobachtung |
| R6-9 | Ausnahmen nach Typ und Inhalt (Entscheidung 7) | SPEZ Z. 17 | Verschiedene Fehlermeldungen gelten als gleich |
| R6-11 | Register vollständig, einschließlich Verhandlung (Entscheidung 6) | SPEZ Z. 19; gebaut von S4; voller Verdrahtungstest 8 von 8 nur als Vorprüfung, am Stand ohne M2(b) (UEBERGABE Z. 202–210) | Eine gebaute Funktion wird nie gerufen |
| R6-12 | Verhaltensändernde Altlast erreichbar (Entscheidung 5) | SPEZ Z. 20 | Der Zweig für Altlasten bleibt unerreichbar |
| ohne Kennung | **Stiller Durchlass „unbeobachtet“ („0 von 0“):** Ein Kandidat ändert nur ein Konstantenmodul; der Verhaltensvergleich meldet „tragfähig“ ohne Enthaltung, `aegis.pruefen` lässt ihn „ueberlebt“. S1c schließt die Klasse (Wege A bis D) | `BAU-S1C-UNBEOBACHTET.md`, Z. 8–12 und 27–32; `/tmp/r6-s1b/befund-unbeobachtet.txt` (25.09. 12:32); Meldung 12:52:19 (id 20817) | Kandidaten, die nur Modulwerte oder Datendateien ändern, werden ohne Beobachtung angenommen. Nach der Startregel beginnt T4 nicht |
| ohne Kennung | Stiller Durchlass über `_Konto.buchen` (Methode einer privaten Klasse) | UEBERGABE Z. 173–175 | Laut Meldung 12:52:19 durch M2(b) geschlossen; ohne Review nicht bestätigt |
| ohne Kennung | Abschluss der Runde 6: Commit, Kette (volle Regression mit Kammer, Nachspiele, Vorher/Nachher), ein Review, Veröffentlichung, Endmeldung | UEBERGABE Z. 23–24 und 211–212 | Ohne Abschluss kein Start von T4 (FK05) |

## B. Punkte für die Aufnahme von T4 (nicht blockierend)

| Kennung | Was | Beleg | Folge, falls offen | weitergereicht |
|---|---|---|---|---|
| R6-5 | Kappe der Verfälschungsläufe am echten T4-Werk messen (Entscheidung 8) | SPEZ Z. 13; UEBERGABE Z. 20 und 66: „Messskript für die Aufnahme von T4 vorbereiten, nicht messen (kein T4-Werk)“ | Die Kappe bleibt ungemessen; es gilt Zurückstellen mit Grund (Entscheidung 4 der Runde 5) | 1: UEBERGABE Runde 6, Z. 66 (R52: 0, weil die Zeile „Kappe“ sagt, nicht R6-5) |
| R6-14 | Unvollständig erfasste Funktionen an der Vorgeneration des T4-Werks zählen | SPEZ Z. 22 | Die Erfassungslücke im T4-Werk bleibt unbekannt | 2: EINORDNUNG Z. 10, UEBERGABE Z. 66 |
| R6-15 | `ITER_KAPPE` an der T4-Last messen | SPEZ Z. 23; BERICHT Runde 5, Z. 489 („auf der Liste: an der T4-Last messen“) | Das Vorauslesen ist nur gerechnet, nicht gemessen | 2: BERICHT Runde 5, Z. 489; UEBERGABE Z. 66 |

## C. Vor T5 (nicht blockierend für T4, das ein Python-Werk ist)

| Kennung | Was | Beleg | Folge, falls offen | weitergereicht |
|---|---|---|---|---|
| R6-13 | TS-Kanon: blinde Arten, Fehlalarme, TS-Proben zu den Entscheidungen 2 und 3 (Entscheidung 8) | SPEZ Z. 21 („Vor T5“) | Der TypeScript-Weg bleibt ohne eigene Kammerprobe | 3: BERICHT Runde 5, Z. 488; SPEZ Z. 21; UEBERGABE Z. 45 |
| R4-17 | Methoden von Klassen in TypeScript | BERICHT Runde 4, Z. 180 und 211 („vor T5, nicht vor T4“); Philipp 24.09. 11:49:51 (id 15992), Nr. 5 | TS-Methoden werden nicht beobachtet | 1 Dokument, 2 Zeilen: BERICHT Runde 4. Vorher als offene Frage in BERICHT Runde 3, §14 Nr. 3 |

## D. Unbestätigte Befunde aus dem verworfenen Review der Runde 5 (nicht blockierend)

Quelle aller vier: `/root/biotop-vor-t4-05/REVIEW-verworfen-erster-durchgang.md`, gelesen, nicht gemessen. Einordnung
nach der Startregel am Code von `0c2f058`: „0 von 4 sind stille Durchlässe. Alle vier bleiben auf der Liste.“
(EINORDNUNG-U1-U4, Z. 15). Philipp hatte angeordnet: „die übrigen bleiben auf der Liste“ (25.09. 00:27:35, id 17217).

| Kennung | Was | Folge, falls offen (EINORDNUNG) | weitergereicht |
|---|---|---|---|
| U-1 | `os.fork` in einem Werk mit laufenden Threads kann das Kind der Eingrenzung verklemmen | Hänger bis zum Kammerlimit, dann Zurückstellen; die Frist baut Entscheidung 3. Bei der Aufnahme von T4 prüfen, ob das Werk beim Import Threads startet | 4 |
| U-2 | Lastaufrufe tragen auch `klein`/`gross` (Überstrenge) | Fehlalarm: Richtige Behebungen werden abgelehnt, nie ein falscher Kandidat angenommen | 4 (R52: 1) |
| U-3 | Der TS-Weg prüft nicht „ohne Sonde“ | Überzählige Enthaltung; vor T5 | 4 (R52: 1) |
| U-4 | Die Stufen-Zusicherung im Verdrahtungstest filtert `None` | Gespeicherte Maße ohne Stufenkennzeichnung; für „Kein Rückschritt“ nur Werte mit Stufe 2 vergleichen | 4 (R52: 2) |

Die 4 Dokumente sind jeweils: SPEZ Runde 5 (Z. 25–32, „Unbestätigt“), BERICHT Runde 5 (Z. 491), EINORDNUNG-U1-U4 und
UEBERGABE Runde 6 (Z. 104). R52 zählt weniger, weil diese Stellen „U-1 … U-4“ oder „alle vier“ schreiben.

## E. Ältere offene Punkte ohne Entscheidung

| Kennung | Was | Beleg | Folge, falls offen | blockiert | weitergereicht |
|---|---|---|---|---|---|
| vier Phase-4-Lücken | Wirkungskreis mit transitiven Folgen; Vertragsaustausch zwischen Vorspann und Freeze; NaN/Null in Rauschwerten; Vorstufenbindung beim Maß-Freeze | Philipp 20.09. 17:34:38 (id 6108): „Auf die Liste für Phase 4 […] sie werden am Handelssystem gegen echte Fälle gebaut“; `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/PHASE4-OFFEN.md` | Das Ziel ist entfallen, weil das Handelssystem gestrichen ist (Teil 1, FK08 D). Auslegung Hermes: Philipps Begründung, die Lücken könnten an einem Werk mit 4 Bereichen und 856 Zeilen nicht eintreten, trägt für T4 nicht mehr; BERICHT Runde 2 (§12 Nr. 1) erwartet 6.000–10.000 Zeilen | nicht entschieden; in den Runden 1–6 nicht geführt | 4 bis 21.09.: UEBERGABE-PHASE-4 in abschluss-01 (Z. 233) und in uebergabe-abnahme-01 (Z. 33), ZWISCHENBERICHT reparatur-02 (Z. 28), T3 `MESSGERAETFEHLER.md` (Z. 3: „nicht pauschal als behoben geführt“) |
| 19 Außenorte | offene Außenleser | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/AUSSEN-19-OFFEN.md`; ZWISCHENBERICHT reparatur-02, Z. 28: „keine erneute Außensuche, keine Vollständigkeitsentwarnung“ | Stellen außerhalb des Kernpfads bleiben ungeprüft | nicht entschieden; in den Runden 1–6 nicht geführt | 4: ZWISCHENBERICHT abschluss-02 (Z. 23, 31), uebergabe-abnahme-01 (Z. 33), reparatur-02 (Z. 28), T3 `MESSGERAETFEHLER.md` (Z. 3) |
| Ansageabweichungen | 9 von 11 Angriffstests weichen von ihrer eigenen Ansage ab (Vorbedingung 1) | Philipp 20.09. 22:55:04 (id 8461): „auf die Liste […] gehört aber in einen eigenen Auftrag nach Vorbedingung 2“; `TORZEILEN.json` abschluss-02, Z. 28–35 | Laut Philipp ist die Vorab-Ansage als Filter entwertet. Vorbedingung 2 war die Verfassung des Handelssystems (Philipp 21.09. 00:07:30, id 8749); der Anlass ist entfallen. Verwandt, aber nicht dasselbe: der Ansagefilter in T3 (ABSCHLUSS-03 §4e) | nicht entschieden | 3: ZWISCHENBERICHT abschluss-02, uebergabe-abnahme-01 (Z. 33), `TORZEILEN.json` |
| R5-14 | Koroutine, gebunden an Objekte einer fremden Ereignisschleife (Review 04 Nr. 17, gelesen, nicht gemessen) | BERICHT Runde 4, Z. 264; SPEZ Runde 4, Z. 24: „nicht entschieden: Liste“ | Kann ein T4-Werk mit asyncio treffen (Auslegung Hermes) | nicht entschieden; eine Entscheidung: NICHT GEFUNDEN (0 Treffer für „Koroutine“, „Ereignisschleife“, „R5-14“ in `arbeit/verlauf/v2/wortlaut.jsonl`) | 2; danach nur als Sammelnennung „R5-1 … R5-14“ (BERICHT Runde 5, Z. 61) |
| R4-19 | S-12 und S-3 (Wurzelmodul) durch den Laufweg | BERICHT Runde 3, §14 Nr. 5; BERICHT Runde 4, Z. 213 („Liste“) | Nur am Organ belegt, nicht durch den Laufweg | nicht entschieden | 2; danach in den Offen-Abschnitten nicht mehr geführt, ob erledigt: UNBEKANNT |
| ohne Kennung | Gewinn-Nachmessung in `lauf._generation_koerper` nur gelesen, nicht ausgeführt | BERICHT Runde 2, §12 Nr. 5; BERICHT Runde 3, §14 Nr. 6 | Ungeprüfter Laufweg | nicht entschieden | 2; danach NICHT GEFUNDEN |
| ohne Kennung | K2868, führende Null („007“) | BERICHT Runde 4, §14 Nr. 4; BERICHT Runde 5, Z. 39 (ungedeckt „Weißraum und führende Null“) | Ist `007` gültig, ist das ein weiterer Rückschritt von K2868 | nicht entschieden | 2 |
| ohne Kennung | Gateway-Dump als Beleg am Gateway; Bauzeit gepaart messen | BERICHT Runde 1, §12 Nr. 5 und 6 | — | unbeantwortet; Philipps Entscheidungen vom 23.09. 22:32:40 (id 14624) betreffen die Fragen 1 bis 4 und den Wächter | 1; danach in den Offen-Abschnitten nicht mehr geführt, ob erledigt: UNBEKANNT |
| EICH-S1/S2/S3 | „nicht blockierende Empfehlungen“ aus Reparatur 01: strengere Qualitätsstruktur, weitere Normgegenklasse, vollständiger Vorspann-Rohbeleg | `BEFUNDE.md` (siehe oben), Z. 36 | — | „nicht blockierend“ (wörtlich) | 1 (die einzige wörtliche Fundstelle); Verbleib danach NICHT GEFUNDEN |
| ohne Kennung | Aus STAND-01: „Vor weiterem Betrieb die Trägerordnung klären. Eigene Domain für Prüfkanal als späterer offener Punkt. Sitzungsreset nach Ablieferung über `/new`, noch nicht als ausgeführt belegt.“ | R31, Z. 171 | Prüfkanal weiter unter der Website-Domain (FK43 Nr. 2) | nein | 1; in den Runden nicht geführt (R54: „Domain“ 0 Treffer) |

## F. Offen bei Philipp (nicht blockierend, Auslegung Hermes)

| Punkt | Beleg | Stand |
|---|---|---|
| Modell der Verdichtung: Gemini bleibt (Entscheidung Hermes) oder Claude über OpenRouter (teurer) | UEBERGABE Runde 6, Z. 135–136 | ohne Antwort |
| Hermes-Fehlerklassierer (a)/(b): Abbruch von S1 mit HTTP 400; eine Behebung berührt die Hermes-Installation, also harte Linie 1 | UEBERGABE Z. 141–146 und 169; `S1-ABBRUCH.md`, Z. 38 | ohne Antwort. Folge: Lange Subagenten mit Pflicht-Denken können wieder abbrechen |
| Einreichung des Fehlalarm-Texts zum Sicherheitsfilter | Philipp 24.09. 11:49:51 (id 15992), Nr. 6; `/root/biotop-vor-t4-04/FEHLALARM-SICHERHEITSFILTER.md` | Text liegt vor; Philipps Entscheidung: NICHT GEFUNDEN |
| Sperre 03 (S4, „Pipe to interpreter“, pending_approval, nicht umgangen) | UEBERGABE Z. 188–189; `sperre/SPERRE-03-ROH.txt` | Die Stichprobe f ist nicht gelaufen |
| Widerrufenes OAuth-Token des Hilfsmodells der Verdichtung | `ZWEI-REVIEWS.md`, Z. 59–60 | Umgangen durch die Umstellung auf OpenRouter (25.09. 01:15, UEBERGABE Z. 131–134); die Anmeldung selbst bleibt widerrufen (Auslegung Hermes) |

## Nicht mehr offen, aber mehrfach weitergereicht (zur Einordnung der Zählung)

- **„Liste nach T3“:** Erreichbarkeitsführung, Verfallsbedingung der Wächter-Ausnahmeliste, `_beschleunigen` entfernen,
  Rauschrohwerte speichern. Angeordnet von Philipp am 21.09. um 12:05:50 (id 10669), 16:58:53 (id 10903) und 20:15:07
  (id 11135). Weitergereicht in 3 Dokumenten: T3 `abschluss-01/ABSCHLUSSBERICHT.md` (Z. 178),
  `uebernahme-01/ZWISCHENBERICHT.md` (Z. 132) und `abschluss-03/ABSCHLUSS-03.md` (Z. 451–455, „Weiter offen aus der Liste
  nach T3“). Erledigt als Vorbedingung 11 in Runde 1 mit Laufweg-Proben (BERICHT Runde 1, Z. 59).
- **U-1 bis U-4** sind eingeordnet (Abschnitt D), aber nicht behoben.
