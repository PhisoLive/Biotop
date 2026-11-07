# Zwischenbericht — automatisch ausgelöst (biotop-vor-t4-02)

Ausgelöst 2026-09-24T02:07:08+02:00 vom Zwischenbericht-Wächter (Cron, ohne Modell). Sitzung `20260923_194003_92313ee1`, Werkzeugrunde **1 von 150** (Schwelle –).
Anlass: Verdichtung gescheitert 2026-09-24T02:05:46+02:00 (summary_generation_aborted, agent.log (Verdichter-Telemetrie)): Error code: 401 - {'type': 'error', 'error': {'type': 'authentication_error', 'message': 'OAuth access token has been revoked.'}, 'request_id': None}. Further summary attempts paused for 60 seconds..
Regel (Philipp, 23.09.2026): Zwischenbericht spätestens bei 120 von 150 Aufrufen — ausgelöst, nicht erinnert.
Die Übergabedateien sind der zuletzt vom Agenten geschriebene Stand; alle übrigen Abschnitte sind in diesem Augenblick mechanisch gelesen.

## Auftrag dieses Turns (Nachricht 14975, 2026-09-24T02:05:46+02:00)

```
[ASYNC DELEGATION BATCH COMPLETE — deleg_ce891021]
A background fan-out unit you dispatched earlier — 1 subagent(s) — has finished; its consolidated results are below. Any other units from the same delegate_task call report separately as they finish. You may have moved on since dispatching — act on these or re-dispatch if things have changed. If you are still waiting on siblings, end your turn after acting on this one.

Dispatched: 2026-09-24 00:38:14 (1h27m ago)
Role: leaf   Model: ?   Total duration: 5250.45s

--- ✓ TASK 1/1: Führe genau EINEN unabhängigen Reviewdurchgang für die 'Behebungsrunde 2 vor T4' des Biotop-Projekts durch und schreibe das Ergebnis nach /root/biotop-vor-t4-02/REVIEW.md. Der vollständige Prüfauftrag steht in /root/biotop-vor-t4-02/REVIEW-AUFTRAG.md — lies ihn zuerst und halte dich wörtlich an ihn (Gegenstand, Prüfpunkte a–g, harte Regeln, Ausgabeformat).  (status=completed, api_calls=50, 5249.95s) ---
Der Reviewdurchgang ist fertig und steht in `/root/biotop-vor-t4-02/REVIEW.md`: 22 Befunde, davon 6 hoch, 9 mittel und 7 niedrig. Das Urteil des Berichts, „nicht abgenommen“, bestätige ich. K2904 und K3091 sind nur in 2 von 3 Durchgängen gleich entschieden. Auch die Zahlen zu S1 (Lauf 38 3 von 5, Lauf 37 2 von 5), Nachspiel und Regression stimmen mit ihren Quellen. In der Regression sind 493 bestanden und 2 übersprungen, davon 18 von 18 in `test_vor_t4_02`.

**Die sechs hohen Befunde**, gemessen an eigenen Proben in der echten Kammer, erst nach Ende des Jobs:
- **Generatoren:** Eine geänderte Ausgabe eines Generators ergibt 0 Abweichungen und gilt als „1 von 1 beobachtet“.
- **Änderung an den Eingaben:** Eine Funktion, die ihr Argument an Ort und Stelle anders sortiert, ergibt ebenfalls 0 Abweichungen.
- **Nenner „x von y“:** Eine Funktion gilt als beobachtet, auch wenn jeder Aufruf auf beiden Seiten mit demselben Fehler endet. Die tatsächliche Änderung bleibt dann unsichtbar.
- **Fehlalarm durch die Kammer:** Ohne feste Hash-Reihenfolge (`PYTHONHASHSEED`) erzeugen Mengen 22 falsche Abweichungen. Das trat in 2 von 2 Wiederholungen auf, jeweils mit Ablehnung.
- **Zwischenspeicher per Dekorator:** Funktionen mit `@lru_cache` werden nicht eingewickelt. Ergebnis: 16 von 16 Abweichungen „ungedeckt“ und eine Ablehnung, obwohl sich das Verhalten nicht ändert.
- **Deckung praktisch unerreichbar:** Mit der Regel „dieselbe Eingabe je Muster“ deckt ein richtiger Test auf dem Lastpfad nur 2 von 28 Abweichungen.

**Weitere wichtige Befunde:**
- Die Gegenprobe zu K2868 trennt den erweiterten Korpus nicht von der neuen Deckungsregel. Die Angabe „20 von 20 `~form`“ ergibt sich nur aus Sortierung und Kürzung der Liste.
- Ein Test kann eine Abweichung decken, die er gar nicht zusichert. Umgekehrt gehen echte Deckungen verloren: bei Standardparametern und bei `export const`, wo 0 Aufrufe aufgezeichnet werden.
- Die Bestätigungsmessung ist nie mit echter Messung auf dem Laufweg gelaufen: In 0 von 7 Nachspiel-Entscheidungen trat ein Laufzeitris
```

## Übergabe (vom Agenten gepflegt)

- `/root/biotop-vor-t4-02/UEBERGABE.md` — Stand 2026-09-24T01:10:51+02:00, als eigene Datei im Ordner

## Letzte Äußerungen des Agenten in diesem Turn (neueste zuletzt)


## Repositories

`/root/biotop`:
```
6243377 Vor T4, Runde 2: Python-Sonde, Deckung je Abweichung, Formvarianten, bestätigte Laufzeitrisse
330b4ec Vor T4: Review-Befunde eingearbeitet (ein Reviewdurchgang zu 58bd9f9)
58bd9f9 Vor T4: Behebungsrunde — Vorbedingungen 1–11 aus Masterprompt Fassung 8
(Arbeitsbaum sauber)
```

## Seit Turnbeginn geänderte Dateien (neueste zuerst)

- (keine)

## Laufende Prozesse (Auszug)

```
(keine)
```
