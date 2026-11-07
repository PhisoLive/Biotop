# Kassenblatt — Fassung 01 · 2026-09-20T03:17:33.347176+00:00

## Auftrag W1/W2/W4, getrennt von Biotop-Läufen
Zweck `W4.einmaliger_traegernachweis`, Sitzung `20260920_050847_fa0691`.
- Zugelassene HTTP-Modell-POSTs: 1 von 1 freigegebenen; Antwort HTTP 429.
- Erfolgreiche Modellantworten: 0 von 1 zugelassenen Versuchen.
- Zusätzlich versuchter POST: 1 von 1 vor dem Netz gesperrt; nicht als ausgelieferter Modellaufruf gezählt.
- DB-Zähler des Tests: 0 API-Aufrufe, 0 Eingabe- und 0 Ausgabetoken erfasst. Die DB hat den HTTP-Fehlversuch nicht als erfolgreichen Verbrauch verbucht. Kein Nachweis kostenfreier Verarbeitung.
- `estimated_cost_usd`, `actual_cost_usd`, `cost_status`, `cost_source`: jeweils `null`. Kosten **unbekannt**. Kein EUR-Wert erfunden, keine Umrechnung ohne Quelle.
- Verbrauchsdatei fehlt nach Timeout; stderr und stdout sind leer. Kein Wiederholungsaufruf.
- Keine neue Zeile in Biotop `kasse`; Vorher/Nachher unverändert: 4070 Zeilen, höchste ID 4070, gespeicherte Summe 8,639304768518517 €.

Abfragen: `belege/KASSENABFRAGEN-01.json`, `belege/KASSE-NACHHER-01.json`, `belege/SITZUNGSKASSE-01.json`.
HTTP-Belege: `traegernachweis/HTTP-WACHE-01.jsonl`, `traegernachweis/HTTP-ANTWORT-01.txt`, `traegernachweis/ABBRUCH-01.json`.
Die laufende Telegram-Unterhaltung ist **nicht** in diesen Zusatztest hineingerechnet; ihre momentanen Sitzungsfelder sind in der DB-Abfrage als getrennte Zeile gekennzeichnet. Das Kassenblatt behauptet keine vollständige Anbieterrechnung der Unterhaltung.

## Vorbedingung 1 nach V20 — Rechenabgrenzung, vollständig für diesen Schnitt
- Lauf 22 insgesamt: 233 Zeilen, 0,5166083055555555 €; davon Abzug erste Etappe: 189 Zeilen, 0,39776329629629625 €; verbleibend 44 Zeilen, 0,11884500925925925 €.
- Lauf 23: 239 Zeilen, 0,393614287037037 €.
- Lauf 24: 193 Zeilen, 0,39687799999999995 €.
- Lauf 25: 183 Zeilen, 0,3899286759259259 €.
- Vor Abzug: 848 Zeilen. Nach Abzug: 659 Zeilen; Einzelzeilen gehen auf diese Summe auf.
- Netto aus einzelnen gespeicherten Buchungen: 1.29926597222222211151 €. Frei gegen 3 €: 1.70073402777777788849 €.
- **Geführter Stand laut Entscheidung V20: rund 1,299 € von 3 €, frei rund 1,701 €.** Kein weiterer Abzug ohne ausdrückliche neue Abgrenzung.

Die Fehlerklärung und die noch offene mögliche Überschneidung von Lauf 23 stehen im Zwischenbericht. Die ursprünglichen Kassenblätter bleiben unverändert; dieses Blatt führt keine stillschweigende rückwirkende Umbuchung durch.
