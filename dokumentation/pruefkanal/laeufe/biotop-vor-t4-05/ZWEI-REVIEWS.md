# Wie zwei Reviewdurchgänge der Runde 5 entstanden

Stand 2026-09-24, nachträglich rekonstruiert aus den Protokollen des Gateways und der Delegation (`bau/ZWEI-REVIEWS-ROH.txt`,
nicht veröffentlicht, weil es Chat-Kennungen enthält; hier maskiert als `[chat]`) und dem Delegationsprotokoll des ersten
Durchgangs (`bau/REVIEW1-DELEGATIONSPROTOKOLL.txt`, maskiert durch `bau/r5_protokoll_maskieren.py`; das Skript selbst ist
nicht veröffentlicht, weil es die Kennung als Suchwort enthält).

## Ablauf

| Zeit | Ereignis | Beleg |
|---|---|---|
| 20:31:20 | Die Hauptsitzung (`…150913_a9326d`) startet **genau einen** Review-Subagenten, asynchron (`deleg_b1c00361`). Er läuft in der Sitzung `…203120_e6c401` (`platform=subagent`), Ordner `/tmp/review-vor-t4-05/`. | `agent.log`: „Dispatched async delegation batch deleg_b1c00361 (1 task(s)…)“ |
| 20:31:43 | Das Gateway findet die Hauptsitzung „ended in state.db but still live in sessions.json“ und stellt die Weiterleitung des Chats neu her. | `gateway.log` (#54878) |
| 20:31–21:44 | Die Hauptsitzung steht am Kontextrand (≈ 1.010.887 Token geschätzt); jede Verdichtung scheitert: „OAuth access token has been revoked“ (Hilfsmodell der Verdichtung, 401), 7 Versuche. | `agent.log`, `context compression attempt telemetry` |
| 21:41:02 | Der Reviewer startet seine Kammerprobe als **Hintergrundprozess mit Abschlussmeldung** (`proc_0423d3933e03`, `notify_on_complete: true`). Der Prozess trägt den Sitzungsschlüssel des Telegram-Chats (`agent:main:telegram:dm:[chat]`), Eigentümer `sa-0-816c6469`, Elternsitzung `…203120_e6c401`. | `logs/process-results/proc_0423d3933e03.json` |
| 21:51:24 | Die Abschlussmeldung wird als Nachricht in den Chat eingespeist. Das Gateway „Pinned async-delegation completion to owning session …203120_e6c401 (was …150913_a9326d)“ und verwirft den Agenten der Hauptsitzung. Die Hauptsitzung endet (`session_switch`). **Ab hier beantwortet eine zweite Instanz den Chat — auf der Sitzung des Reviewers, mit dessen bisherigem Verlauf.** | `gateway.log` (#57498, #54878 × #54947); `state.db`: `ended_at` 21:51:24 |
| 21:52–22:04 | **Instanz A** (der ursprüngliche Subagent) arbeitet weiter: 21:52:25 `abschluss.sh` geschrieben und ausgeführt, 21:52:35 `bericht_neu.sh`, 21:56:47 `e2b_probe.py`, 22:03:48 schreibt `/root/biotop-vor-t4-05/REVIEW.md`, 22:04:07 fertig. | Delegationsprotokoll |
| 22:02–22:20 | **Instanz B** (Chat-Instanz) setzt denselben Verlauf fort: 22:02:32 überschreibt sie `abschluss.sh` (Werkzeughinweis: „modified by sibling subagent 'sa-0-816c6469'“), findet `REVIEW.md` vor, schreibt ihren Durchgang deshalb nach `/tmp/review-vor-t4-05/REVIEW.md`. | Zeitstempel der Dateien; Verlauf der Sitzung |
| 22:04:08 | Das Ergebnis von A wird nicht zugestellt: „Async delegation deleg_b1c00361 targets permanently-gone session …150913_a9326d; terminally dropping delivery“. | `gateway.log` |

## Was beide Durchgänge teilen und was nicht

- **Gemeinsam** (vor der Teilung um 21:51:24): alle Kammerläufe (36 Fälle, 21:41–21:48, `KAMMERPROBE05.json`), die lokalen
  Proben `lokal_b` und `lokal_ts`, die Auswertungen der Belege. Beide Durchgänge zitieren dieselben Messungen.
- **Nur A:** `e2b_probe` (21:56, lokale pytest-Probe zu R6-4).
- **Nur B:** `letzte.py` (Nachrechnung der Stufe-2-Dauern über 24 Messungen, Code-Stempel der Nachspiele, 22:1x).
- **Überschriebenes Skript:** A führte `abschluss.sh` um 21:52:25 aus; B überschrieb die Datei um 22:02:32. Danach führte A
  kein Skript aus dem Ordner mehr aus (nächste und letzte Aktion: 22:03:48 `REVIEW.md` schreiben). Das Skript las nur
  Dateilisten und Zeitstempel.

## Entscheidung

Philipp, 24.09.: **Es gilt der zweite Durchgang** (B, jetzt `REVIEW.md`). Der erste bleibt als
`REVIEW-verworfen-erster-durchgang.md` im Ordner; was nur er fand, steht als „unbestätigt“ auf der Liste
(`SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md`, U-1 … U-4).

Zur Begründung, gemessen: Laut Delegationsprotokoll hat der erste Durchgang das überschriebene Skript nicht ausgeführt,
und die Messungen beider Durchgänge sind dieselben (siehe oben). Die Wahl bleibt bestehen; ihre Begründung „nicht
auszuschließen“ trifft nach dem Protokoll nicht zu.

## Ursachen

1. **Hintergrundprozess mit Abschlussmeldung in einem Subagenten.** Der Prozess erbte den Sitzungsschlüssel des Chats;
   seine Meldung wurde in den Chat geleitet und band den Chat an die Sitzung des Reviewers. Das Werkzeug hatte beim Start
   gewarnt, die Meldung erreiche den Elternagenten nicht — sie erreichte stattdessen den Chat.
2. **Die Hauptsitzung war am Ende.** Kontext über der Grenze, Verdichtung gescheitert (widerrufenes OAuth-Token des
   Hilfsmodells); das Gateway hatte sie als beendet geführt und leitete den Chat auf die jüngste Sitzung um.
3. **Ein gemeinsamer Ordner.** Beide Instanzen arbeiteten in `/tmp/review-vor-t4-05/`; so konnte B eine Datei von A
   überschreiben.

## Regeln ab Runde 6

1. Jedes Review bekommt einen **eigenen, neuen Ordner** `/tmp/review-<auftrag>-<JJJJMMTT-HHMMSS>/`; existiert er, bricht
   der Start ab.
2. **Vor dem Start** prüfe ich, dass kein Review läuft: `delegate_task list` leer; kein Delegationsprotokoll mit Status
   `running` unter `~/.hermes/cache/delegation/live/*/manifest.json`; kein Prozess mit dem Ordnernamen.
3. Reviewer und umsetzende Subagenten starten **keine Hintergrundprozesse**; lange Läufe nur als Vordergrundskript
   (≤ 600 s) oder im Job des Auftragnehmers.
4. Offen für Philipp (nicht in meiner Hand): Das Token des Hilfsmodells für die Verdichtung ist widerrufen. Ohne
   Verdichtung endet jede lange Sitzung an der Kontextgrenze.
