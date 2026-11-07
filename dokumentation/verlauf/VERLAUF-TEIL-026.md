# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 026 von 054

- Einträge V0491 bis V0499. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0491 · 20.09.2026 05:39:38 CEST · Philipp · Nachricht id 3219 · Sitzung `20260920_052507_2f047335` · 8726 B

````text
[The user sent a text document: 'PRUEFUNG_Wiedereinstieg_2026-09-20.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_053b25077f1c_PRUEFUNG_Wiedereinstieg_2026-09-20.md]

[Content of PRUEFUNG_Wiedereinstieg_2026-09-20.md]:
# Prüfung: Wiedereinstieg, Gedächtnis und Trägernachweis

**Geprüft von:** Chat-Claude · **Abruf:** 20.09.2026
**Kern:** Die Ablieferung trägt. Der Trägernachweis ist gescheitert — und das ist ein Gewinn, kein Verlust.

---

## 1. Bestätigt durch Ausführung

```
Gedächtnisordner, Dateiliste:     3 Nutzdateien
SHA-256 Ist:  20ffc24c09285e843a43fe46758e5f10a2b113640f9e28f0558f328373e7ed10
SHA-256 Soll: 20ffc24c09285e843a43fe46758e5f10a2b113640f9e28f0558f328373e7ed10
```

**Kleiner offener Punkt:** 32 + 3 = **35 Nutzdateien**, geprüft gemeldet sind **40 von 40**. Die Differenz von 5 sind vermutlich die Listen- und Prüfsummendateien beider Ordner. Gehört benannt, ist aber kein Befund — Regel 10.

`UNTERBAU-01.md` ist die sauberste Datei, die bisher aus diesem Vorhaben gekommen ist. Drei getrennte Aussagen zur Modellwahl, jede mit ihrer Menge. Punkt gegen Bindestrich (`claude-fable-5.1` gegen `claude-fable-5-1`) ausdrücklich **nicht still normalisiert**. Und der Satz, auf den es ankommt: `--ignore-rules` macht den Test zu **keinem** identischen Nachbau der Telegram-Sitzung — also hätte er den Träger auch bei Erfolg nicht bewiesen.

---

## 2. Meine Fehlerbilanz — fünf in drei Runden, alle derselben Art

| # | Behauptung von mir | Wirklichkeit | gefunden von |
|---|---|---|---|
| 1 | Der Obsidian-Tresor existiert | existiert nicht | Hermes |
| 2 | `hermes -z` kostet nichts | ist ein Modellaufruf | Hermes |
| 3 | Die 0,0002 € sind „nur Rundung" | **falsch** — die alte Fortsetzungszahl war falsch | Hermes |
| 4 | Ein CLI-Test belegt den Träger | zwei Betriebswege, zwei Träger | Hermes |
| 5 | Hermes liegt unter `/root/.local/bin/hermes` | `/usr/local/lib/hermes-agent/venv/bin/hermes` | Hermes |

Alle fünf sind dieselbe Art: **Ich habe eine Lücke mit einer plausiblen Geschichte gefüllt, statt sie zu messen oder als Lücke zu kennzeichnen.**

Nummer 3 ist die unangenehmste. Ich habe gerechnet, dass Rundung die 0,0002 € erzeugen *könnte*, und daraus geschlossen, dass sie es *getan hat*. Das ist Erwartetes statt Abgelesenes — mein eigener Prüfsatz, gegen mich selbst. Die Zahl 1,299 € steht weiterhin. Aber sie stand aus dem falschen Grund. **Richtige Zahl, falsche Begründung** — genau das Muster, das ich bei Hermes unter 2 → 0 → 2 beanstandet habe.

### Die Ursache und die Regel dagegen

Ich habe **kein Messgerät für diese Maschine**. Ich kann ausschließlich lesen, was Hermes abliefert. Jedes Mal, wenn ich über den Server, seine Pfade, seine Kosten oder sein Verhalten eine Aussage treffe, ist das eine Vermutung im Gewand einer Feststellung.

> **Fassung 7, Regel 27:** Jede Aussage von Chat-Claude über die Maschine ist eine **Frage an Hermes**, keine Feststellung. Steht sie ohne beigefügte Messung in einem Auftrag, wird sie als „zu prüfen" gekennzeichnet.

---

## 3. Der gescheiterte Trägernachweis ist der Gewinn dieser Runde

Er hat nichts bewiesen, was er beweisen sollte — und dabei zwei Dinge aufgedeckt, die vorher niemand wusste:

**Erstens: Es gibt zwei Betriebswege mit verschiedenen Trägern.**

| Weg | Träger | Stand |
|---|---|---|
| CLI, Konfiguration | `claude-fable-5.1` bei `anthropic` | Soll, nicht am Erzeugnis belegt |
| CLI, tatsächlich angefragt | `model=claude-fable-5-1` an `api.anthropic.com` | angefragt, keine Antwort |
| **Telegram-Sitzung** (der Weg, den du benutzt) | **`gpt-6-astra`** | DB-Metadatum, nicht am Erzeugnis belegt |

Mein W4 zielte auf den falschen Weg. Der Träger, der deine Aufträge tatsächlich ausführt, ist nicht der, den ich prüfen ließ.

**Zweitens — und das steht in `UNTERBAU-01.md`, ohne dass seine Meldung es aufgreift:**

`hermes auth list` zeigt bei Anthropic **zwei** Einträge: `claude_code` (OAuth, **als rate-limited angezeigt**) **und `ANTHROPIC_API_KEY`**.

Dieser Schlüssel wurde am 18./19.09. **absichtlich entfernt**, mit genannter Begründung: Er verdrängt die OAuth-Anmeldung des Trägers, und der Schlüssel war ohne Workspace-Zuordnung erzeugt — Anthropic verlangt eine `anthropic-workspace-id`. Ein künftiger Schlüssel sollte im Workspace erzeugt und unter eigenem Namen abgelegt werden, etwa `BIOTOP_ANTHROPIC_API_KEY`.

**Er ist wieder da.** Und der Testaufruf lief gegen `api.anthropic.com` und bekam HTTP 429.

**Als meine Überlegung gekennzeichnet, nicht als Befund:** Ob der Schlüssel das 429 verursacht hat oder ob die OAuth-Kontingentgrenze unabhängig davon erschöpft ist, kann ich von hier nicht entscheiden. Beides ist möglich. Was feststeht: Die Lage, die vor zwei Tagen mit Begründung beseitigt wurde, besteht wieder — und der Träger meldet Rate-Limit.

**Warum das jetzt zählt:** Vorbedingung 2 braucht Modellaufrufe. Läuft der Träger gegen eine verdrängte oder kontingentierte Anmeldung, stockt die Arbeit an einer Stelle, an der niemand danach sucht.

### Zu den Kosten des Fehlversuchs

Hermes schreibt „Kosten unbekannt". Das ist richtig so. **Meine Einschätzung, ausdrücklich als Einschätzung:** Ein 429 weist die Anfrage ab, bevor sie bearbeitet wird; ein Verbrauch ist damit unwahrscheinlich. Gemessen ist das nicht, und es gibt keine Verbrauchsdatei. „Unbekannt" bleibt stehen.

---

## 4. Was Hermes richtig gemacht hat

- Keine Wiederholung nach dem 429. Keine Modellkonfiguration geändert. Beides richtig — bei unklarer Lage nichts verstellen.
- Die HTTP-Wache war prozesslokal, kein dauerhafter Eingriff, und sie verändert Modellwahl und Antwort nicht. Sauber abgegrenzt.
- `stdout` und `stderr` wörtlich als **leer** ausgewiesen, statt die Leere zu verschweigen.
- „Nicht als bestanden formulieren." Sein Satz, nicht meiner.
- Meine Kassenerklärung berichtigt, obwohl sie ihm recht gegeben hätte.

---

## 5. Aufträge

**W5 — Anthropic-Anmeldung klären. 0 Modellaufrufe.**
1. Steht `ANTHROPIC_API_KEY` in `/root/.hermes/.env` oder in der Prozessumgebung? Wer hat ihn wann gesetzt, soweit aus Zeitstempeln ablesbar?
2. Ist der Schlüssel im Workspace erzeugt, trägt er also eine `anthropic-workspace-id`?
3. Verdrängt er die OAuth-Anmeldung? Was sagt `hermes auth list` zur Rangfolge?
4. Ist die OAuth-Rate-Limit-Anzeige ein Zeitfenster oder eine harte Sperre?

**Nichts ändern.** Nur messen und melden. Die Entscheidung trifft Philipp.

**W6 — die fünf Dateien benennen.** 32 + 3 = 35 Nutzdateien, geprüft gemeldet 40. Welche fünf?

**Sitzungsreset:** Ja. `/new` senden. Die Sitzung hat geliefert, das Gedächtnis steht und ist nachgerechnet. Der nächste Wiedereinstieg liest `STAND-01.md`, `REGELN-01.md` und `UNTERBAU-01.md` — er braucht keinen Brief mehr.

**Fassung 7:** Die Adresse von Fassung 6 liegt jetzt vor. Das Ausschreiben ist meine Arbeit und braucht keinen einzigen Modellaufruf von Hermes — es läuft unabhängig von der Anmeldelage.

---

## 6. Kurzprompt für den Telegram-Chat mit Hermes

> Ablieferung geprüft und tragfähig: Gedächtnisordner mit `20ffc24c…` selbst nachgerechnet, Soll gleich Ist bei 3 Nutzdateien, und `UNTERBAU-01.md` ist die sauberste Datei, die bisher aus diesem Vorhaben kam — drei getrennte Aussagen zur Modellwahl mit je eigener Menge, Punkt gegen Bindestrich nicht still normalisiert, und dein Satz, dass `--ignore-rules` den Test zu keinem Nachbau der Telegram-Sitzung macht, trifft den Kern: Mein W4 zielte auf den falschen Betriebsweg. **Deine Berichtigungen stimmen alle** — meine Rundungserklärung war falsch, und ich führe jetzt fünf eigene Fehler dieser Art in drei Runden, alle gleich gebaut: Lücke mit plausibler Geschichte gefüllt statt gemessen; ab sofort gilt Regel 27, jede Aussage von mir über die Maschine ist eine Frage an dich, keine Feststellung. Ein Befund aus deiner eigenen Datei, den deine Meldung nicht aufgreift: `hermes auth list` zeigt bei Anthropic **sowohl** `claude_code` (OAuth, rate-limited) **als auch `ANTHROPIC_API_KEY`** — und genau dieser Schlüssel wurde am 18./19.09. absichtlich entfernt, weil er die OAuth-Anmeldung des Trägers verdrängt und ohne Workspace-Zuordnung erzeugt war; **W5, 0 Modellaufrufe, nichts ändern:** messen, ob der Schlüssel gesetzt ist, ob er eine Workspace-Zuordnung trägt, ob er OAuth verdrängt und ob das Rate-Limit ein Zeitfenster oder eine harte Sperre ist, dazu **W6**: welche fünf Dateien die Differenz zwischen 35 Nutzdateien und den geprüften 40 ausmachen — danach `/new`, der Reset ist richtig, alles steht in `PRUEFUNG_Wiedereinstieg_2026-09-20.md`.
````

### V0492 · 20.09.2026 05:39:43 CEST · Hermes · Nachricht id 3222 · Sitzung `20260920_052507_2f047335` · 22 B

```text
Operation interrupted.
```

### V0493 · 20.09.2026 05:39:43 CEST · Philipp · Nachricht id 3223 · Sitzung `20260920_052507_2f047335` · 1546 B

```text
Ablieferung geprüft und tragfähig: Gedächtnisordner mit 20ffc24c… selbst nachgerechnet, Soll gleich Ist bei 3 Nutzdateien, und UNTERBAU-01.md ist die sauberste Datei, die bisher aus diesem Vorhaben kam — drei getrennte Aussagen zur Modellwahl mit je eigener Menge, Punkt gegen Bindestrich nicht still normalisiert, und dein Satz, dass --ignore-rules den Test zu keinem Nachbau der Telegram-Sitzung macht, trifft den Kern: Mein W4 zielte auf den falschen Betriebsweg. Deine Berichtigungen stimmen alle — meine Rundungserklärung war falsch, und ich führe jetzt fünf eigene Fehler dieser Art in drei Runden, alle gleich gebaut: Lücke mit plausibler Geschichte gefüllt statt gemessen; ab sofort gilt Regel 27, jede Aussage von mir über die Maschine ist eine Frage an dich, keine Feststellung. Ein Befund aus deiner eigenen Datei, den deine Meldung nicht aufgreift: hermes auth list zeigt bei Anthropic sowohl claude_code (OAuth, rate-limited) als auch ANTHROPIC_API_KEY — und genau dieser Schlüssel wurde am 18./19.09. absichtlich entfernt, weil er die OAuth-Anmeldung des Trägers verdrängt und ohne Workspace-Zuordnung erzeugt war; W5, 0 Modellaufrufe, nichts ändern: messen, ob der Schlüssel gesetzt ist, ob er eine Workspace-Zuordnung trägt, ob er OAuth verdrängt und ob das Rate-Limit ein Zeitfenster oder eine harte Sperre ist, dazu W6: welche fünf Dateien die Differenz zwischen 35 Nutzdateien und den geprüften 40 ausmachen — danach /new, der Reset ist richtig, alles steht in PRUEFUNG_Wiedereinstieg_2026-09-20.md.
```

### V0494 · 20.09.2026 05:42:49 CEST · Hermes · Nachricht id 3248 · Sitzung `20260920_052507_2f047335` · 65 B

```text
Operation interrupted: waiting for model response (2.6s elapsed).
```

### V0495 · 20.09.2026 05:46:41 CEST · Philipp · Nachricht id 3249 · Sitzung `20260920_052507_2f047335` · 416 B

```text
Ich will auf gpt-6-astra wechseln, komme aber nicht weg von claude-fable-5.1. Ohne Modellaufruf und ohne etwas zu ändern: zeig mir hermes auth list, hermes config get model, hermes config get fallback und hermes doctor — und sag mir, ob die Codex-Anmeldung für Astra noch gültig ist oder abgelaufen, und ob eine Rückfallregel mich auf Fable zurückzieht. Erst danach stellen wir um und starten den Gateway neu.
```

### V0496 · 20.09.2026 05:57:03 CEST · Hermes · Nachricht id 3338 · Sitzung `20260920_052507_2f047335` · 5560 B · geschwärzt 4

````text
Nichts geändert. Alle vier Ausgaben liegen wörtlich in `/root/w7/`.

## 1. `hermes auth list` (`01-auth-list.txt`)

```
anthropic (2 credentials):
  #1  claude_code        oauth   priority=0  rate-limited (429) (37m 54s left)
  #2  ANTHROPIC_API_KEY  api_key priority=1  [GESCHWÄRZT: Wert aus auth.json]

[GESCHWÄRZT: Wert aus auth.json] (1):  device_code  oauth  priority=0  ←
openrouter (1):    OPENROUTER_API_KEY  api_key  priority=0  ←
```

## 2. `hermes config get model` (`02-…`)

```
default: claude-fable-5.1
provider: anthropic
```

## 3. Rückfall (`03-…`, `04-…`, `11-…`)

- `config get fallback` → **Exit 1, „Config key not set: fallback"**
- `config get fallback_model` → **Exit 1, nicht gesetzt**
- `fallback list` → **„No fallback providers configured."**

## 4. `hermes doctor` (`06-doctor.txt`, 143 Zeilen, Exit 0)

2 Befunde, beide npm-Abhängigkeiten (agent-browser 2, web-workspace 6). Auth-Abschnitt: „OpenAI Codex auth (logged in)" ✓. API-Konnektivität: nur OpenRouter geprüft ✓.

---

## Deine zwei Fragen

**Ist die Codex-Anmeldung für Astra gültig? — Ja, gültig.**

Aus dem Token selbst gelesen (`07-codex-token.txt`, kein Netzaufruf):
- `access_token`: exp **2026-09-26 23:46:57**, also noch **161,98 h** gültig, Plan `pro`
- `refresh_token` vorhanden, Poolstatus `ok`, `last_error_code=null`
- `id_token` ist seit 05.09. abgelaufen — das ist der Identitätsnachweis der Anmeldung, nicht der API-Token; er wird für Aufrufe nicht verwendet. **Als meine Einordnung gekennzeichnet, nicht als Messung.**

Bestätigt durch Ausführung: `gpt-6-astra` hat heute zwischen 04:50 und 05:24 **31 Aufrufe** über `[GESCHWÄRZT: Wert aus auth.json]` abgesetzt (Sitzung `20260920_045023`), keiner mit Fehlerstatus.

**Zieht dich eine Rückfallregel auf Fable? — Nein. Es ist der Reset.**

Keine Fallback-Regel existiert (drei getrennte Belege oben). Die Ursache ist eine andere, und sie ist belegt:

`claude-fable-5.1` ist der **Grundwert** in `config.yaml`. `/model` schreibt nur einen **Sitzungs-Override** (`model_override`). Bei `/new` räumt `_handle_reset_command` die Liste `_CONVERSATION_SCOPED_STATE` ab — und deren erster Eintrag ist `_session_model_overrides` (`gateway/run.py:2199`, `slash_commands_session.py:171`). Der Override wird also mit der Sitzung gelöscht, der Grundwert bleibt.

Die Spur in `agent.log` zeigt genau das:
- 05:25:07 `/new` → neue Sitzung, erste zwei Turns laufen mit **`claude-fable-5-1`** (Zeilen 17063, 17112)
- 05:39 Umschaltung → `claude-opus-5` (Zeile 17212)
- 04:50:23 Auto-Reset nach Kompressionsabbruch → 04:54 musste erneut auf `gpt-6-astra` geschaltet werden (Zeile 16858)

Jedes `/new` wirft dich auf Fable zurück, weil Fable in der Konfiguration steht. Die dauerhafte Umstellung ist `model.default` + `model.provider` in `config.yaml`, nicht `/model`.

**Ob dafür ein Gateway-Neustart nötig ist, habe ich nicht gemessen** — der Turn liest die Config zur Laufzeit, aber das habe ich nicht belegt.

---

## Nebenbefund, der W5 berichtigt

`ANTHROPIC_API_KEY` **ist nicht gesetzt**. Gemessen:
- `.env`: enthält `ANTHROPIC_TOKEN` mit **Länge 0**, kein `ANTHROPIC_API_KEY` (Zeile 549)
- Prozessumgebungen: **0 Treffer von 28 lesbaren Prozessen** (107 von 135 PIDs waren zwischenzeitlich beendet); Gateway-PID 1001385 gezielt geprüft: keine `ANTHROPIC*`-Variable
- Der Pooleintrag in `auth.json` hat **kein `access_token`-Feld**, nur einen `secret_fingerprint`. `credential_pool.py:1819` überspringt jeden api_key-Eintrag ohne `runtime_api_key`.

Er verdrängt OAuth also nicht — er ist nicht leasbar. Was wieder da ist, ist die **Zeile in der Anzeige**, nicht der Schlüssel. Chat-Claudes Befund unter Regel 27 zutreffend als Frage gestellt; die Antwort ist nein.

**Rate-Limit: Zeitfenster, keine harte Sperre.** `last_status_at` = 05:25:17, `last_error_reset_at` = `null` (Anthropic lieferte keinen Zeitpunkt) → Standard-TTL `EXHAUSTED_TTL_429_SECONDS = 3600`, Ende **06:25:17**. Status ist `exhausted`, nicht `DEAD`; DEAD wäre die harte Sperre.

---

## Kosten und Eingriffe dieser Runde

- Modellaufrufe durch die Messbefehle: **0** — keine neue Sitzung seit 05:30 angelegt; der Zuwachs 1514 → 1551 entfällt vollständig auf `claude-opus-5` in dieser laufenden Telegram-Sitzung, also auf meine eigenen Antwortschritte.
- Kosten in der Datenbank: `estimated_cost_usd = 0.0`, `actual_cost_usd = 0.0` über alle 32 Zeilen. **Die Kassenspalten sind leer, nicht null Euro** — ich kann aus dieser Quelle keine Kosten beziffern.
- `.env` unverändert (mtime 18.09. 23:13:29), `auth.json` unverändert (05:25:17, gleiche Prüfsumme vor und nach).
- **`config.yaml` hat sich geändert**: mtime 05:41:29. Nicht durch einen Schreibbefehl von mir, sondern durch deinen Telegram-Knopf „Immer erlauben" um 05:41:29 (Gateway-Log), der einen Eintrag in `command_allowlist` schrieb. Gehört gemeldet, auch wenn „nichts ändern" galt.

**W6 bleibt offen und ich fülle die Lücke nicht mit einer Geschichte:** Gemessen enthält der Vorbedingungsordner **97 Dateien rekursiv** (Manifest `DATEIEN-06.txt`: 87), der Gedächtnisordner **5** (Manifest: 3). Die Zahlen 32 und 40 kann ich aus dem heutigen Ordnerstand nicht reproduzieren. Chat-Claudes Vermutung „die 5 sind die Listen- und Prüfsummendateien" stimmt aber nicht: davon gibt es **12** (10 im Vorbedingungsordner, 2 im Gedächtnisordner).

Sag Bescheid, wenn ich umstellen soll — ich schlage `model.default: gpt-6-astra`, `model.provider: [GESCHWÄRZT: Wert aus auth.json]` vor.
````

### V0497 · 20.09.2026 06:00:00 CEST · Philipp · Nachricht id 3339 · Sitzung `20260920_052507_2f047335` · 428 B · geschwärzt 1

```text
Stell um: model.default: gpt-6-astra, model.provider: [GESCHWÄRZT: Wert aus auth.json], und die Stufe auf max — die genaue Schlüsselschreibweise dafür prüfst du selbst, ich kenne sie nicht auswendig. Danach /new und sag mir, welches Modell den ersten Turn beantwortet und in welcher Stufe — am Erzeugnis, nicht aus der Konfiguration. Zeigt es noch Fable oder eine andere Stufe, starte den Gateway neu und prüfe nochmal.
```

### V0498 · 20.09.2026 06:10:44 CEST · Hermes · Nachricht id 3428 · Sitzung `20260920_052507_2f047335` · 4065 B · geschwärzt 1

````text
Umgestellt. Zwei von drei Punkten sind am Erzeugnis belegt, der dritte braucht deine `/new`.

## Die Schlüsselschreibweise

`agent.reasoning_effort` — geprüft, nicht geraten:
- Zulässige Werte: `hermes_constants.py:927` → `minimal, low, medium, high, xhigh, max, ultra`
- Gelesen wird der Schlüssel in `hermes_constants.resolve_reasoning_config()`, dem „single chokepoint für jede Oberfläche (CLI, gateway, TUI, cron, /model)"
- Astra akzeptiert davon `low, medium, high, xhigh, max` (`agent/reasoning_effort.py:36`) — `max` ist die höchste und wird **nicht heruntergestuft**: `clamp_effort('max', …) → 'max'`

**`hermes config set` warnt trotzdem:** „`agent.reasoning_effort` is not a recognized config key — it was saved anyway". Die Warnung ist falsch, und ich belege es dreifach statt sie wegzudeuten: der Schlüssel stand schon vor meinem Eingriff mit `high` in der Datei; `gateway/slash_commands_model.py:596` schreibt genau diesen Pfad beim `/reasoning`-Befehl; und der Katalog `DEFAULT_CONFIG["agent"]` listet 40 Unterschlüssel, `reasoning_effort` ist keiner davon. Es ist eine Lücke im Katalog, kein Funktionsfehler.

## Gesetzt (Sicherung: `config.yaml.vor-astra-20260920-060104`)

```
model.default:           claude-fable-5.1 → gpt-6-astra
model.provider:          anthropic        → [GESCHWÄRZT: Wert aus auth.json]
agent.reasoning_effort:  high             → max
```

## Am Erzeugnis gemessen — aber auf dem CLI-Weg

Ich habe einen echten Aufruf gemacht (`hermes -z`, 1 Modellaufruf, bewusst) mit `HERMES_DUMP_REQUESTS=1`. Das ist die Anfrage, die tatsächlich auf die Leitung ging:

```
url:        https://chatgpt.com/backend-api/codex/responses
model:      "gpt-6-astra"
reasoning:  {"effort": "max", "summary": "auto"}
```

Kosten dieses Aufrufs aus der Datenbank: 12.307 Eingabe-, 22 Ausgabe-, 15 Reasoning-Token, `billing_mode = subscription_included`, Kostenspalten `0.0` — **also leer, nicht null Euro**.

Beides steht wörtlich in `/root/w7/20-cli-wire-felder.txt`.

## Was ich nach `/new` messen kann — und was nicht

**Das Modell: ja.** `agent.log` schreibt je Turn `model=… provider=…`, dazu die Zeile in `session_model_usage`. Das ist das Erzeugnis des Turns, nicht die Konfiguration.

**Die Stufe: nein, nicht auf dem Telegram-Weg.** Gemessen: CLI-Sitzungen tragen `reasoning_config: {enabled: true, effort: max}` in `model_config`; die letzten drei Telegram-Sitzungen tragen dort nur `model`, `provider`, `gateway_runtime` — **kein `reasoning_config`**. Auch `reasoning_tokens` belegt nur, *dass* gedacht wurde, nicht *wie tief*. Ein Request-Dump entsteht im Gateway nur bei Fehlern oder mit `HERMES_DUMP_REQUESTS=1` — und diese Variable liest der Gateway beim Start, nicht pro Turn.

**Das ist der Entscheidungspunkt, und er gehört dir:** Soll ich den Gateway jetzt mit gesetztem `HERMES_DUMP_REQUESTS=1` neu starten, bekomme ich für den ersten Turn nach `/new` denselben Wire-Beleg wie oben — Modell **und** Stufe. Dann ist aber der Neustart Teil der Messung, und deine Frage „reicht `/new` allein?" ist nicht mehr beantwortbar. Ohne Neustart kann ich dir das Modell belegen und die Stufe nur als **ungemessen** ausweisen.

Ich habe **nicht** neu gestartet und **nicht** gemessen, ob der Gateway die geänderte Konfiguration ohne Neustart übernimmt. Der Code spricht dafür (`_load_gateway_config()` wird pro Nachricht aufgerufen, der Cache ist mtime-geschlüsselt) — **das ist Codelektüre, keine Messung**, und genau der Typ Lücke, den ich nicht mit einer plausiblen Geschichte fülle.

## Nebenbefund dieser Runde

Um 05:58 hat ein Aufruf dieser Telegram-Sitzung an `api.anthropic.com` einen `ValueError: control character found while parsing a string` geworfen (`request_dump_…_055836.json`). Kein 429, kein Anmeldeproblem — ein Zeichenkettenfehler in meinem eigenen Turn. Gemeldet, weil er in der Ablage liegt und sonst jemand darüber stolpert.

Schick `/new` und dann irgendeine Nachricht. Ich lese Modell und Träger am Turn ab und sage dir sofort, ob Fable weg ist.
````

### V0499 · 20.09.2026 06:40:15 CEST · Philipp · Nachricht id 3429 · Sitzung `20260920_063003_896e94ff` · 994 B · 2 gleiche Zeilen zusammengefasst

```text
Vor Vorbedingung 1 einen Gesamtstand — aber keine Wiederholung der Abschlussberichte, die habe ich alle selbst geholt und nachgerechnet. Liefere, was dort nicht steht: (1) Umfang des gebauten Biotops, gemessen — Dateien, Zeilen, Organe, eigene Tests, Datenbankgröße; (2) welche Organe wirklich laufen und welche nur existieren, dazu abgelöste oder tote Bestandteile (pruefung/funde_neubewerten.py hattest du selbst genannt); (3) wo der Code vom Masterprompt Fassung 6 abweicht — Zeile für Zeile durchgehen, jede Abweichung benennen, auch die zu deinen Ungunsten; (4) alle Läufe 1 bis 23 mit Status, Werk und Kosten in einer Tabelle, Summe gegen meine Rechnung von 7,37 €; (5) das Biotop gegen die sechs Grundsätze aus Abschnitt 2a geprüft — wo verstößt dein eigener Code dagegen? Das ist eine Bestandsaufnahme, kein Lauf: Budget 1 €, Abschlussordner laeufe/biotop-gesamtstand/, Endmeldung mit vollständiger Abholadresse als ganze URL und Prüfsumme. Danach Vorbedingung 1.
```

