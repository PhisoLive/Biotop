# BIOTOP-LAGE-01 · Fassung 2 · `INVENTAR-TEIL3-01.md`

- **Inhalt:** Abschnitt 5 · Entwurf I, Stück 3 von 3
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Skript `entwurf/inventar/inventar.py` (Subagent Teil I), ausgeführt von Hermes zum Stichzeitpunkt (R191). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/inventar/lauf-stich-v3/INVENTAR-TEIL3.md` · 2050 B · SHA-256 `71b6aa7e6e3de8e843dc248f64925563f5282f60d983653a25cdbf730ab73b15`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (0 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
> INVENTAR Teil 3 von 3 (INVENTAR-TEIL1.md … INVENTAR-TEIL3.md)

## 11. Lückenvorschläge und Widersprüche

Mechanisch aus den Abgleichen; Kennung LV-I-nn nur für diesen Entwurf (die Lückenliste LU.. vergibt Hermes).

| Kennung | was fehlt | warum | was es schließt | wer |
|---|---|---|---|---|
| LV-I-01 | 1 Werkordner ohne Kasseneintrag (versandwerk-t3) | weder Pfad noch Quelle eines Werks der vier Zweige | Herkunft je Ordner klären (Ausgang eines Laufs, Zwischenstand, Kopie) und in FK25 nennen | Hermes |
| LV-I-02 | 11 in Ordnertexten genannte Laufnummern ohne Lauf in einer Kasse (0, 52, 53, 59, 60, 62, 66, 84, 128, 848, 991) | mechanisch nicht unterscheidbar: Zahl anderer Bedeutung, anderer Nummernkreis oder Lauf außerhalb der vier Zweige | Fundstellen lesen und je Nummer einordnen (Ordner: `LISTEN`, Abschnitt 2) | Hermes |
| LV-I-03 | 54 Aufträge/Anweisungen Philipps ohne Status | Status nur aus der Chronik übernehmbar | Chronik mit Nachrichten-id oder Zeit je Zeile; inventar.py erneut ausführen | Hermes |
| LV-I-04 | 5 Aufträge Hermes→Subagent vor Beginn BIOTOP-LAGE-01 ohne Schlussbericht in der Sitzung | Abbruch, Zeitüberschreitung, Bericht nur als Delegationsergebnis beim Auftraggeber, oder Einordnung des Absenders | je Nachrichten-id Verlauf der Sitzung lesen (LISTEN, Abschnitt 3) | Hermes |
| LV-I-05 | Differenz Kasse ↔ OpenRouter nicht einzeln erklärt | Nutzungsanzeige ohne Einzelposten; derselbe Schlüssel außerhalb des Biotops genutzt | Einzelaufrufe bei OpenRouter abrufen (Aktivitätsliste) oder getrennte Schlüssel je Vorhaben | Hermes (Abfrage) oder Philipp (Konto) |

**Widersprüche zwischen Quellen (beide Belege):**

| Nr | Widerspruch | Beleg 1 | Beleg 2 |
|---|---|---|---|
| 1 | Kasse führt 3 Läufe als „laeuft“ (T3/31, T3/32, T3/36), letzte Buchung jeweils Tage vor dem Stich | Kasse T3, Tabelle laeufe (status, beendet_am) | R2 (Schritt 1, 25.09. 14:49 CEST): keine Prozesse mit „biotop“, „pytest“, „kammer“, „vitest“ oder „tsc“ im Befehl, 0 Container |
