# Unterbau — Fassung 01 · 2026-09-20T03:17:33.347176+00:00
Umfang: gemessener Ausschnitt dieser Maschine/Instanz für W4; kein vollständiges Inventar aller Profile oder Dienste.

## Fehlgeschlagener Nachweis am Erzeugnis
**Kein erfolgreicher Trägername am Erzeugnis belegt.** Datum des CLI-Teststarts aus Sitzungskennung: 20.09.2026; rohe Zeitstempel in `belege/SITZUNGSKASSE-01.json`.
Kommando (ohne Modell-/Provider-Override):
```
hermes --ignore-rules -z 'Nur deine Modellkennung. Keine Werkzeuge.' --usage-file /root/wiedereinstieg-01/traegernachweis/VERBRAUCH-01.json
```
Eigene Sicherheitsmaßnahme: prozesslokale HTTP-Wache über `PYTHONPATH`, um weitere POSTs vor dem Netz abzulehnen; kein dauerhafter Hermes-Patch. Die Wache liest die Antwort, verändert Modellwahl und Antwortinhalt nicht. `--ignore-rules` blendet lokale Regeln/Gedächtnis für den kurzen Test aus; dieser Test ist deshalb kein identischer Nachbau der Telegram-Sitzung.

**stdout wörtlich:** leer (Datei enthält keine Bytes).
**stderr wörtlich:** leer (Datei enthält keine Bytes).
**HTTP-Antwort wörtlich, am Erzeugnis belegt: HTTP 429, nicht erfolgreicher Trägernachweis:**
```json
{"type":"error","error":{"type":"rate_limit_error","message":"This request would exceed your account's rate limit. Please try again later."},"request_id":"req_011CfDxPDupGEFD9kTrgzCeZ"}
```
Danach Timeout des Wrappers; keine erfolgreiche Abschlussantwort, keine Verbrauchsdatei. Nicht als bestanden formulieren. Kein Wiederholungsaufruf.

## Drei getrennte Aussagen zur Modellwahl
1. **Soll, Konfigurationsabfrage:** `hermes config get model`:
```
default: claude-fable-5.1
provider: anthropic
```
2. **Tatsächlich angefragter CLI-Modellparameter:** HTTP-Wache protokolliert POST an `api.anthropic.com/v1/messages` mit `model=claude-fable-5-1`; der Unterschied Punkt/Bindestrich wird hier ausdrücklich erhalten, nicht still normalisiert. Kein erfolgreicher Modellname zurückgeliefert.
3. **Laufende Telegram-Sitzung, DB-Metadatum:** `20260920_045023_5299d50d`, `model=gpt-6-astra`. Unterschied zu CLI-Voreinstellung vorhanden. Nicht durch den CLI-Test als echte Anbieterantwort validiert. Andere Population, keine Gleichsetzung der beiden Wege.

## Gemessene Pfade und Dienst
- `hermes config path` liefert `/root/.hermes/config.yaml`.
- `shutil.which('hermes')` liefert `/usr/local/lib/hermes-agent/venv/bin/hermes`; das tatsächliche Shell-Ziel ist damit nicht allein durch die im Brief genannte Abkürzung `/root/.local/bin/hermes` beschrieben. Existenz und Auflösung beider Pfade in `PFADE-01.json`.
- `hermes --version`: Hermes Agent v0.21.2 (2026.9.11), Installationsverzeichnis `/usr/local/lib/hermes-agent`, Python 3.12.3. Vollständige Werkzeugausgabe beigelegt; keine Aktualisierung ausgeführt.
- `systemctl --user show hermes-gateway.service --property=ActiveState,SubState,FragmentPath,ExecStart`: aktiv/laufend; Unit `/root/.config/systemd/user/hermes-gateway.service`; Start über `/usr/local/lib/hermes-agent/venv/bin/python -m hermes_cli.main gateway run`.
- `systemctl show hermes.service --property=LoadState,ActiveState`: `not-found`, `inactive`. Das ist eine Abfrage des Systemdienstes, keine Behauptung über alle Benutzerdienste.
- `HERMES_HOME=/root/.hermes` in dieser Prozessumgebung; kein `HERMES_PROFILE`-Wert gesetzt. Schreibrolle HERMES-1 ist vom Auftraggeber zugewiesen, kein gemessener eigenständiger Programmname. HERMES-2/HERMES-3 nicht untersucht oder verändert.
- Biotop-Code `/root/biotop`, Kasse `/root/biotop/daten/biotop.db`; Hermes-Sitzungsdatenbank `/root/.hermes/state.db`. Existenz mit `Path.exists()` geprüft; Datenbanken mit SQLite `mode=ro` gelesen.

## Anmeldungen: Metadaten, keine Zugangsdaten
Abfrage: `hermes auth list`; vollständige nicht geheime CLI-Ausgabe in `belege/ANMELDUNGEN-01.txt`.
- Anthropic: Eintrag `claude_code` (OAuth, als rate-limited angezeigt) und `ANTHROPIC_API_KEY` (API-Key-Eintrag).
- OpenAI Codex: `device_code` (OAuth-Eintrag).
- OpenRouter: `OPENROUTER_API_KEY` (API-Key-Eintrag).
Diese Liste beweist gespeicherte Einträge, **nicht** erfolgreiche Anmeldung/Abrechnungsfähigkeit jedes Anbieters. Keine Schlüsselwerte veröffentlicht, keine Authentifizierung geändert.

## Prüfkanal und Belege
Dateisystem:
`/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe`

Alle zu diesem Unterbau ausgeführten Abfragen und Ausgaben:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/DATEIEN-01.txt

Abbruch und offene Arbeit:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/ZWISCHENBERICHT.md

Kassenblatt:
https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/KASSE-01.md

Eigene Domain für den Prüfkanal bleibt offen. Der Kanal liegt weiterhin auf der MilieuLux-Kundenseite.
