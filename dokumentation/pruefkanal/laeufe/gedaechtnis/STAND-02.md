# Stand · Fassung 02 · 25.09.2026 (Auftrag BIOTOP-LAGE-01)

- **Schreibrolle:** HERMES-1; HERMES-2 und HERMES-3 lesen nur.
- **Ablage:** Dauerhafte Ablage nach V19 ist dieser Prüfkanal.
- **Verhältnis zu STAND-01 (20.09.):** STAND-01 bleibt unverändert, gilt aber nicht mehr als aktueller Stand. Er nennt als nächsten Schritt noch das Handelssystem, das am 21.09. gestrichen wurde.

## Verweis auf den Abschlussordner

Der ganze Stand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/START-03.md
Kurzlage und offene Fragen:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/LAGE-TEIL1-01.md

## Stand in Kürze (Quelle je Punkt im Abschlussordner)

- **Masterprompt:** Es gilt Fassung 8 vom 23.09.2026, 15:53:53 CEST (MASTERPROMPT-GUELTIG-TEIL1-01.md).
- **Phase 4 (Breitentest):** T3 (`versandwerk-t3-02`, TypeScript) lief in den Läufen 26–38 für 9,728638 € von 10 € und ist nicht abgenommen. T4, T5 und T6 sind nicht begonnen.
- **Behebungsrunden 1–6 vor T4:** ohne Lauf und ohne Modellgeld, keine abgenommen. Letzter Commit ist `0c2f058` aus Runde 5.
- **Runde 6 zum Stich:**
  - Gebaut sind S2, S3, S4, S1b und S1c A–F; nichts davon ist eingecheckt (25 Einträge).
  - **Befund G ist offen:** ein stiller Durchlass beim Schreiben in fremde Module; es gibt nur rote Spezifikationen `test_w_g_*`.
  - T4 ist nach der Startregel nicht frei. Runde 6 ruht, bis Philipp entscheidet.
- **Kasse:** 6.919 Buchungen, 18,814735 €. Seit dem 22.09. um 21:26:08 gab es keine Biotop-Buchung.
- **Sicherung:** `/root/sicherung/biotop-lage-01/biotop-sicherung-2026-09-25-01.tar.gz`, 790.821.244 B, SHA-256 `03340fdbece5cc4254b54d285b36b1d9640eaa590649f9e1007b95fa2881af73`. Wiederherstellung geprüft. Das Archiv liegt nur auf diesem Server.

## Regeln

- **Philipps Arbeitsregel vom 23.09.** gilt: Weiterarbeiten ist der Normalfall; Anhalten nur an drei harten Linien. Wortlaut in ENTSCHEIDUNGEN-TEIL3-01.md (FK18).
- **REGELN-01** ist in Teilen überholt, bei den Freigaben und beim Handelssystem. **REGELN-02 fehlt** (Lücke LU02).
- **Datenbanken des Biotops** nur mit `mode=ro&immutable=1` oder als Kopie lesen. Bloßes `mode=ro` schreibt die `-shm` (Abweichung A6).

## Offen bei Philipp (FK47, P1–P4)

1. Gilt das Budget von 0,00 € auch für Verdichtungen über OpenRouter?
2. `ZWISCHENBERICHT.md` mit der Telegram-Kennung (A4): löschen oder freigeben?
3. Runde 6 weiterführen, also Befund G bauen?
4. Ablage 2 für das Sicherungsarchiv.
