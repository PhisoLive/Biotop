# BIOTOP-LAGE-01 · Fassung 2 · `SOLL-IST-TEIL4-01.md`

- **Inhalt:** FK30 · Entwurf E, Stück 4 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil E, Arbeitszeit 25.09.2026 16:10:47–18:55:32 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/soll-ist/SOLL-IST-TEIL4.md` · 8858 B · SHA-256 `daf4a701d16a4bc5fd7b249fc96c7d68e5a57b2d3a410514b7728667344ac03f`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (2 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# SOLL-IST — Abgleich gegen Masterprompt Fassung 8 (FK30) · Teil 4 von 4

Dieser Teil enthält die UNKLAR-Punkte für FK47, die Lücken, die Widersprüche und den Prüfbeleg dieses Entwurfs. Kürzel und Lesart stehen in Teil 1. Stand des Lesens: 25.09.2026, 16:05 bis 18:30 CEST.

## 1. UNKLAR-Punkte für FK47

Jeder Eintrag mit Status `UNKLAR` steht hier mit Frage, Adressat und Weg zur Klärung.

| Nr. | Kennung | Frage | an | Weg zur Klärung |
|---|---|---|---|---|
| U-E1 | MP3.4.2, MP4.3 | In den T3-Läufen 26–38 lief kein Mentor, also gab es auch keine Richtungswahl (R157). Gelten Z. 167 und Z. 281 für die Testwerke des Breitentests? Wer hat entschieden, T3 ohne Mentor zu fahren? | Philipp, Chat-Claude | Der Auftrag T3 (`PH` Z. 371) nennt keinen Mentor. Die Meldungen vom 21. und 22.09. in `HP` nach „Mentor“ durchsehen. |
| U-E2 | MP3.5.4 | Z. 176 verlangt als Bezug der Grenzmaße den Bestwert des Laufs und Laufzeiten als Median aus drei Durchläufen. Grundsatz 14 (Z. 131) und Vorbedingung T4 Nr. 1 (Z. 464) verlangen die gepaarte Messung. Welche Stelle gilt? | Chat-Claude | Berichtigung in Fassung 9; Widerspruch W-E1. |
| U-E3 | MP3.8.3 | Ist „höchstens dreimal, dann Meldung an Philipp“ gebaut? Ersetzt die Sättigungsmeldung (3.11) diese Regel? | Hermes, Chat-Claude | `__main__.py` und `tor4.py` lesen. |
| U-E4 | MP3.9.3 | Ist die Wiederholung der Generationen n bis n+k nach einer Rückkehr gebaut, und trat der Fall je ein? | Hermes | Aufrufer von `lazarus.rueckkehr` lesen; Protokollarten `lazarus.*` in einer Kopie der Datenbank zählen. |
| U-E5 | MP4.5 | Die Freigaben in T3 folgten jeweils Sekundenbruchteile nach dem Ende der Generation, immer mit demselben Grundtext (MP4.5). Ist das eine Freigabe unter Vollmacht (Z. 288) oder Vollautomatik (Z. 287)? Vollautomatik kommt nach Z. 287 erst nach drei Werken ohne unbemerkten Rückschritt und nur auf Philipps Satz. | Philipp, Chat-Claude | Den Wortlaut der Freigabe für T3 (`PH` Z. 377) gegen Z. 287 legen. |
| U-E6 | MP6.2 | Schwere Aufrufe laufen tokenabgerechnet über OpenRouter (R103), nicht über die schweren Modelle des bestehenden Teams mit eigener Kontingentgrenze. Gilt Philipps Satz vom 18.09. noch („schwere Aufrufe über das bestehende Team“, `PH` Z. 20)? Wer hat den Weg über OpenRouter entschieden? | Philipp | `HP` ab 18.09. nach „schwer“ und „Team“ durchsehen; Antwort Philipps. |
| U-E7 | MP6.4 | Gilt das Budget, das Philipp je Auftrag setzt, als Bestätigung „vor jedem Lauf“? | Philipp | Antwort Philipps; die Beträge stehen in `CHRONIK`. |
| U-E8 | MP7.1, MP7.2, MP7.3, MP7.4, MP7.5 | Den Vorgänger `infinite-evolution-ai` gibt es auf der Maschine nicht (`HP` Z. 21); das Biotop ist ein Neubau in Python. Gilt „Übernehmen“ in Abschnitt 7 noch? Wenn nicht: Was davon bleibt als eigene Forderung (Aktenschrank in der Landkarte, CI mit gitleaks, Schwärzung im Protokoll)? | Philipp, Chat-Claude | Entscheidung für Fassung 9. |
| U-E9 | MP9.7 | Nennt jede Endmeldung die ganze Abholadresse und die Prüfsumme des Ordners? | Hermes | `HP` je Abschlussordner durchsehen. |
| U-E10 | MP9.8 | Gehen die Aufschlüsselungen der Berichte ab dem Nachlauf zu Phase 3 auf ihre Gesamtzahlen auf? | Hermes | Nachrechnen in Teil C `TORE` und Teil F `CHRONIK`. |

**Weitere Fragen für FK47 ohne eigenen Eintrag:**
- Zu MP3.5.17, an Philipp: Deckt die Vollmacht für Übungswerke auch die Bestätigung des Maßes? Lauf 26 im Zweig VB1 trägt „Hermes unter Übungswerk-Vollmacht“ (R66). Z. 288 nennt nur Freigabe und Richtungswahl.
- Zu MP8.38, an Philipp: Die Vollmacht gilt für „Werke ohne Betriebszweck, die Hermes selbst erzeugt hat“ (Z. 288). T4 erzeugt Hermes „über ein anderes Modell als sein eigenes“ (Z. 426). Gilt die Vollmacht für T4? Bezug: FK19 in `ENTSCHEIDUNGEN`.

## 2. Lücken (Vorschlag für die Lückenliste)

| Nr. | Kennung | Lücke | Beleg |
|---|---|---|---|
| L-E1 | MPK.2 | Die Zwischenbericht-Pflicht steht nur im Änderungsverzeichnis (Z. 43), nicht in Abschnitt 9 (Z. 497–507). | v8 |
| L-E2 | MP3.5.7 | Für T3 ist keine Verlaufskurve auffindbar, obwohl ein Abschlussordner ohne Kurve unvollständig ist. | R103; Dateinamen in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/` |
| L-E3 | MP5.2 | Die technische Trennung des Kerns (eigener Prozess, eigene Datenbank-Rolle) steht seit Phase 1 auf der Liste für danach. Keine Fassung hat sie gestrichen oder einer Phase zugeordnet. | `P1B` Z. 91; `kern/datenbank.py:4–5` |
| L-E4 | MP3.14.4, MP6.2 | Es gibt keine eigene Grenze für Kontingent-Aufrufe und keinen Adapter für die schweren Modelle des Teams. | `P1B` Z. 111; R83; R103 |
| L-E5 | MP3.2.4 | Die Landkarte hat keine Stichwort- und Bedeutungssuche (Aktenschrank). | R76 |
| L-E6 | MP7.3, MP7.9, MP7.11 | Es gibt kein CI, kein gitleaks und keine Abhängigkeitsprüfung als hartes Maß. | R76 |
| L-E7 | MP2a.1 | Eine Prüfung der Organe gegen die Grundsätze 7–14 fehlt. Die vorhandene Prüfung umfasst die Grundsätze 1–6, Maßstab Fassung 6. | `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/GRUNDSAETZE-2a-01.md` |
| L-E8 | MP8.45 | Erzeugt der Kern die Mutanten selbst, weist er die Verteilung des Typsiebs nicht aus. Der Code sagt selbst, Tor-4-Zeile 3 bleibe dann „nicht belegt“. | `lauf.py:843–847` |
| L-E9 | MP8.58 | Für „Grenzanzeige ohne irreführende Rundung“ gibt es in den Runden 1 bis 5 keinen Beleg. | `R1B` bis `R5B` |
| L-E10 | MP3.5.17 | Bei den Läufen 2, 4 und 5 und bei Lauf 26 im Zweig VB1 fehlt Philipps Bestätigung des Maßes. | R66 |
| L-E11 | MP4.4 | Der Ablehnungsweg der Freigabe ist gebaut, lief aber nie. Die Übergabe einer Ablehnung an die Immunisierung habe ich im Code nicht gefunden. | R83; R126; `lauf.py:595–605` |
| L-E12 | MP3.9.2 | Bei der Rückkehr stellt Lazarus die Landkarte nicht zurück, sondern markiert sie als veraltet. | `lazarus.py:98` |
| L-E13 | MP4.3 | Tor 4 hat keine Zeile zu Mentor und Richtungswahl; in T3 lief kein Mentor. | v8 Z. 436–450; R157 |
| L-E14 | — | Die Übergabe der Runde 6 (`R6U`) liegt nicht im Prüfkanal. Chat-Claude kann den Stand der Runde 6 dort nur aus dem Zwischenbericht lesen. | R150; R67 |

## 3. Widersprüche zwischen Quellen

| Nr. | Beleg A | Beleg B | Betroffen |
|---|---|---|---|
| W-E1 | v8 Z. 176: „Bezug ist der Bestwert des Laufs“; „Laufzeiten werden grundsätzlich als Median aus drei Durchläufen gemessen, nie als Einzelwert.“ | v8 Z. 131: „Laufzeit wird gepaart und robust verglichen, nie gegen ein historisches Minimum.“ Z. 464: „Median mehrerer Messungen je Seite; kein historisches Minimum als Bezug“. Z. 461 nennt „Median aus drei“ unter den gefundenen Messgerätfehlern. | MP3.5.4 |
| W-E2 | v8 Z. 387: „Der Nachweis, dass der Schwarm selbst eine sinnvolle Vertragsänderung durchbringt, … steht in Tor 4.“ Ebenso Z. 57. | v8 Z. 436–450: Tor 4 (Fassung 8) hat keine solche Zeile. | MP8.22 und MP8.43 bis MP8.56 |
| W-E3 | v8 Z. 390: Die Zeilen Nebenwirkung, Regression, Norm und Vertrag „sind im Nachlauf zu Phase 3 mit gehärteten Proben wieder belegt, 4 von 4“. | `PH` Z. 317: „die Norm-Zeile aus Tor 2 und „4 von 4 bestanden" aus dem Nachlauf waren ein leerer Durchlauf (masse statt mass, norm=[])“. Neu belegt erst in Reparatur 02 (`PH` Z. 341: „alle vier Torzeilen erfüllt“); das erwähnt v8 nicht. | MP8.17 bis MP8.20 |
| W-E4 | v8 Z. 405: „Philipps echte Entscheidungen gibt es erst ab Phase 4.“ | v8 Z. 491 (Phase 5): „Hier beginnt das echte Geschmacksgedächtnis.“ In Phase 4 gibt Hermes unter Vollmacht frei (R111). | MP3.12.5, MP8.32 |
| W-E5 | v8 Z. 206 (seit Fassung 7, in Fassung 8 unverändert): „Belegt ist dieses Verhalten noch nicht; es hat deshalb eine eigene Torzeile in Phase 4.“ | `T3A` Z. 81: „Verbundausfall (Auflage 3) — belegt an … echten Ausfällen, nicht gestellt“. Die Zahl steht in `TORE`. | MP3.6.3, MP8.53 |

## 4. Prüfbeleg

- Das Skript `entwurf/soll-ist/e13_pruefen.py` wird über `rb.py` ausgeführt. Es liest nur die vier Teile und v8, keine Datenbank.
- Es prüft je Eintrag:
  - Die Kennung ist eindeutig.
  - Es gibt genau einen Status aus der Liste von FK30.
  - Jedes Stück des Wortlauts (getrennt an „…“) steht in v8 in den angegebenen Zeilen. Verglichen wird ohne die Zeichen `*`.
  - Jede Kennung mit Status `UNKLAR` steht in Abschnitt 1 dieses Teils.
  - Jeder Verweis auf eine Kennung trifft einen Eintrag.
  - Die Zählzeilen im Kopf von Teil 1 stimmen mit der Zählung überein.
  - Keine Datei hat mehr als 34.000 Bytes.
- Frühere Läufe: R165 (vor dem Eintragen der Zählung in Teil 1) und R166 (mit Prüfung der Zählzeilen), je 196 Einträge und 0 Fehler. Danach sind noch Formulierungen geändert worden.
- Den Lauf auf dem Endstand nennt `STAND.md` dieses Ordners. Seine Nummer entsteht erst beim Ausführen, also nach dem letzten Schreiben dieser Datei.
