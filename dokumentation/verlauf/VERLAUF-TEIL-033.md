# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 033 von 054

- Einträge V0576 bis V0576. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0576 · 21.09.2026 04:13:12 CEST · Hermes-Zwischentext · Nachricht id 9867 · Sitzung `20260921_015554_e79a4a0f` · 40022 B · Stück 1 von 2

````text
[PRIOR CONTEXT — for reference only; not a new message]


[END OF PRIOR CONTEXT — COMPACTION SUMMARY BELOW]

[CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Respond ONLY to the latest user message that appears AFTER this summary — that message is the single source of truth for what to do right now. If no user message appears AFTER this summary, do nothing: do not resume, wrap up, or continue work from '## Historical Task Snapshot' or any other section, do not call tools, and wait for a new user message. This handoff must never become the active turn by itself. (Exception: if tool results or your own tool calls appear after this summary, you are mid-way through an in-flight exchange — continue that exchange normally.) Topic overlap with the summary does NOT mean you should resume its task: even on similar topics, the latest user message WINS. Treat ONLY the latest message as the active task and discard stale items from '## Historical Task Snapshot' entirely — do not 'wrap up' or 'finish' work described there unless the latest message explicitly asks for it. Reverse signals in the latest message (e.g. 'stop', 'undo', 'roll back', 'just verify', 'don't do that anymore', 'never mind', a new topic) must immediately end any in-flight work described in the summary; do not re-surface it in later turns. IMPORTANT: Your persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active — never ignore or deprioritize memory content due to this compaction note. None of the above restricts HOW you work: your tools remain fully active — keep calling them normally for the active task (edit files, run commands, search) instead of merely narrating what you would do. The current session state (files, config, etc.) may reflect work described here — avoid repeating it:
## Historical Task Snapshot
User asked (deterministic, from compacted turns): "[The user sent a text document: 'INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_3c96ba267e1c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md] [Content of INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md]: # INFINITE EVOLUTION — Das Biotop **Übergabedokument und Masterprompt für Hermes** Stand: 21.09.2026 · Fassung 7 · Auftraggeber: Philipp Zöllisch · Prüfer: Chat-Claude **Änderungen gegenüber Fassung 6** (aus der Abnahme von Vorbedingung 1 und Philipps Richtungsentscheidung vom 21.09.2026): - **Phase 4 ist neu gefasst: Breitentest an mehreren Testwerken statt einem großen echten Werk.** Grund: Philipps Entscheidung — das Biotop soll für jeden Anwendungszweck taugen und dafür in allen Bereichen geprüft sein. Das Handelssystem stand in den Fassungen 1 bis 6 als Phase-4-Werk, war aber eine nie bestätigte Vorentscheidung von Chat-Claude; alle darauf bezogenen Bezugsgrößen (237.000 Zeilen, 17 Dienste, 135 Testfehlschläge) sind gestrichen. **Fehler von Chat-Claude:** eine Vorentscheidung sechs Fassungen lang wie eine Entscheidung geführt. - **Phase 5 neu: erstes echtes Werk**, ohne benanntes Werk — die Wahl trifft Philipp nach dem Breitentest, nach den Kriterien in Abschnitt 8. - 2a: Zwei Grundsätze ergänzt (7: Ein Nachweis zählt nur, wenn er ausgeführt wurde. 8: Jede Probe brauc ...[truncated]"
Historical only; newer protected-tail messages after this summary win.

## Goal
T3 als selbst gebautes TypeScript-Testwerk durch den bestehenden Biotop-Kern führen und damit den werkübergreifenden Breitentest von Fassung 7 voranbringen. Das konkrete Werk heißt **`versandwerk`**, hat fünf Bereiche und soll Vitest, eigene Statik und versiegelte Schwächen besitzen. Vollständige Tor-4-Nachweise einschließlich Verbundausfall, tatsächlicher Ausführung und Gegenproben sind erforderlich; Abschluss mit überprüfbarem HTTPS-Abholort und Prüfsumme.

## Constraints & Preferences
- Maßgeblich ist **Fassung 7 vom 21.09.2026**, nicht Fassung 6.
- Nutzerkorrektur wörtlich: „Das Handelssystem ist als Phase-4-Werk gestrichen: Es war eine nie bestätigte Vorentscheidung von mir, und alle Bezugsgrößen daraus (237.000 Zeilen, 17 Dienste, 135 Testfehlschläge) sind ungültig.“
- Auftragsumfang: „T3 — ein TypeScript- oder JavaScript-Werk, 1.500–2.500 Zeilen, 4–5 Bereiche, eigene Testsammlung (vitest oder jest), eigenes statisches Prüfwerkzeug, mit versiegelten Schwächen wie bei lagerhaus“.
- Prüfdisziplin: „Kernpfad reparieren, Außenliegendes benennen und listen, ein Reviewdurchgang.“
- Budget/Abgabe: „Budget 10 € hart, Abschlussordner laeufe/biotop-t3-typescript/, Endmeldung mit vollständiger Abholadresse als ganze URL und Prüfsumme.“
- „Abnahme nach der Sättigungsregel in Abschnitt 8 — nicht nach einer festen Zahl.“
- Nur T3 bearbeiten, nicht automatisch das nächste Testwerk beginnen.
- Der Assistent band die 10 € als gemeinsame Grenze auch über abgebrochene/neue Läufe hinweg.
- Verfassungsbestätigung ist von Generationen- und Mentorvollmacht getrennt. Im dokumentierten Ablauf wartete sie auf Chat-Claude; Bau und Eichung liefen parallel, Evolution blieb gesperrt.
- Fassung 7: Ein Nachweis zählt nur nach Ausführung; jede Probe braucht eine fehlschlagende Gegenprobe; Prüfaufwand muss zum Gegenstand passen.
- Ein ausgefallenes Verbundmitglied zählt nie als Beitrag. Gestellte HTTP-Antworten sind keine echten Anbieteraufrufe.
- Keine Abschwächung von Prüfbedingungen zur Reparatur roter Tests.
- Bestehender Checkout war bereits verändert; Ausgangsänderungen nicht überschreiben. Implementierende Unteragenten sind kein Abschlussreview.
- Zugangsdaten beziehungsweise zugangsbezogene Schlüssel waren im Kontext vorhanden; Werte werden nicht erhalten: **[REDACTED]**. Auch der zugangsbezogene Aktenpfad wird hier redigiert.

## Completed Actions
Alle nachfolgend datierten Arbeiten fanden am **21.09.2026** statt.

1. READ Fassung 7 aus `/root/.hermes/cache/documents/doc_3c96ba267e1c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md` vollständig — laut Arbeitsstand 512 Zeilen; Fassung 6 wurde als Grundlage abgelöst. [tool: read_file]
2. INSPECT bestehender Kern `/root/biotop` — Aufnahme, Kammer, Messgerät, Kasse, Datenbank, Landkarte, Laufsteuerung, Genesis, Generation 0, Vorspann, Eichproben, Eichgegenstand, Verfassung, Aegis, Verträge, Gedächtnis und Fundprüfung gelesen. [tool: read_file, search_files]
3. CREATE `/root/biotop-t3/vorbereiten.py`, anschließend ausgeführt — Arbeitsstand meldet Abschlussordner, Ausgangssicherung und private Auftragskasse angelegt; vollständige Scriptausgabe ist nicht überliefert. Die kombinierte erste Umgebungsprüfung endete mit Exit 127. [tool: write_file, terminal]
4. CREATE `/root/biotop-t3/VERFASSUNG-T3-ENTWURF.md` — Entwurf für `versandwerk`, ausdrücklich ohne vorweggenommene Freigabe. [tool: write_file]
5. ASK Freigabeweg — Nutzer wählte Bestätigung durch Chat-Claude statt unmittelbarer Bestätigung. [tool: clarify]
6. PUBLISH Entwurf mit `/root/biotop-t3/verfassung_veroeffentlichen.py` — Script Exit 0; anschließend **5 von 5 Dateien über HTTPS bytegleich** gemeldet, Entwurf-URL, `DATEIEN.txt`, `MANIFEST.sha256` und Ordnerprüfsumme geliefert. [tool: write_file, terminal]
7. CREATE `/root/biotop-t3/ARBEITSTEILUNG.md` und `kammer/typescript/package.json`; SPAWN zwei Implementierungsaufträge: TypeScript-Adapter/Kammerimage sowie Werkbau `versandwerk`. [tool: write_file, delegate_task]
8. CREATE Python-Testumgebung `/root/biotop-t3/venv` mit `uv`, Testabhängigkeiten aus `/root/biotop/requirements-test.txt` installiert. [tool: terminal]
9. PATCH Anbieteradapter und Kasse — Ausfälle klassifizieren; belegten Verbrauch buchen; fehlenden Verbrauch als Budgetrisiko behandeln; leere/refusierte Antworten nicht als Beiträge werten. Fokussierte Tests erst rot, dann **7 passed**, später mit Genesis-Integration **8 passed**. [tool: patch, terminal]
10. CREATE `biotop/kern/sprachprofil.py`, PATCH bestehende Organe für TypeScript-Dateien und Testkonventionen — **4 Sprachwegtests bestanden**. [tool: write_file, execute_code, terminal]
11. PATCH Dispatch in bestehendem Kern für TypeScript-Messung/Integration — **4 Integrationstests bestanden**. [tool: execute_code, terminal]
12. PATCH Kernschutz/Freigabe — TypeScript-Prüfkonfigurationen schützen und Generation-0-Erfolg vor Freeze verlangen; **4 Kernsperrentests bestanden**. [tool: execute_code, terminal]
13. PATCH Aegis-Testoperationen für TypeScript — **3 Tests bestanden**. [tool: execute_code, terminal]
14. PATCH Instrumentbindung, TypeScript-Modellvorlagen, Generation-0-Sprachwege; gemeinsamer Zwischenlauf — **31 passed in 0.57s**. [tool: execute_code, patch, terminal]
15. PATCH `_tokens_schaetzen` — `len(text.encode("utf-8")) + 256` statt `max(1, len(text) // 3)`; Unicode-Budgetgegenprobe und Schwarm-Ausfalltests zusammen **3 passed in 0.11s**. [tool: patch, terminal]
16. PATCH Generation 0 — `_aequivalenz_typescript` und `_tests_typescript` ergänzt, Vitest-Testbau und Referenzbelege angebunden; zugehörige kombinierte Prüfung **10 passed in 0.21s**. [tool: patch, terminal]
17. PATCH Aegis — `wirkungskreis_dateien` berücksichtigt tatsächliche Änderungsdateien, zusätzliche Dateien und transitive Nutzer. [tool: patch]
18. PATCH Vorspann — `_vertraege_aktuell` bindet aktuelle Vertragsbytes und DB-Identität vor Freeze; fokussierte Suite nach Korrektur einer Regex **39 passed in 0.75s**, JUnit geschrieben. [tool: execute_code, terminal]
19. RUN vollständige vorhandene Tests ohne `tests/test_typescript_adapter.py` — **338 passed, 4 failed, 2 skipped**, Prozess nach 303,20 s beendet. [tool: terminal]
20. READ Regression und betroffene Tests; PATCH drei Vorspann-Verbraucher-Testfixtures sowie erwartete Instrumentdateiliste — vier gezielte Regressionstests **4 passed in 1.50s**. [tool: read_file, execute_code, terminal]
21. ADD Gegenproben für Änderung von TypeScript-Instrumentdatei und Lockfile nach Versiegelung — **4 passed in 0.22s**, JUnit `/root/biotop-t3/bindung-gegenproben-01.xml`. [tool: patch, terminal]
22. CREATE und RUN `tests/test_t3_fundpruefung.py` — neue Prüfung der TypeScript-Fundneubewertung **rot, Exit 1**; noch keine zugehörige Reparatur dokumentiert. [tool: write_file, terminal]

## Active State
- **Arbeitsverzeichnis:** `/root/biotop`; separater Auftragsbereich `/root/biotop-t3`.
- Branch nicht überliefert. Checkout hatte vor Arbeitsbeginn uncommittete Änderungen; Sicherung wurde laut Arbeitsstand angelegt.
- Maßgebliche Normdatei:
  `/root/.hermes/cache/documents/doc_3c96ba267e1c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md`.
- Python:
  `/root/biotop-t3/venv/bin/python`, Aufrufe mit `PYTHONPATH=/root/biotop`.
- Zwei Unteragenten wurden gestartet:
  - Adapter/Image, bekannte ID **`sa-0-eba8fb38`**.
  - Werkbau `versandwerk`, ID nicht in sichtbaren Resultaten.
  - Keine abschließenden Agentenergebnisse überliefert. Mehrere `steer`-Resultate waren nur `[Duplicate tool output — same content as a more recent call]`.
- Der Regressionshintergrundprozess **`proc_711f5813ec7a`**, PID **2009072**, ist beendet, Exit 1. Kein anderer laufender Prozess sicher belegt.
- Zuletzt bestätigte fokussierte Gesamtsuite: **39 bestanden**, vor weiteren Bindungs- und Fundprüfungstests.
- Gesamtregression: **338 bestanden, 4 fehlgeschlagen, 2 übersprungen**; vier Fehler anschließend einzeln grün, aber kein neuer vollständiger Lauf.
- Aktueller roter TDD-Schritt:
  ```bash
  set -o pipefail; PYTHONPATH=/root/biotop /root/biotop-t3/venv/bin/python -m pytest tests/test_t3_fundpruefung.py -q 2>&1 | tee /root/biotop-t3/fundpruefung-ts-rot.txt
  ```
  Exit 1; vollständige Fehlermeldung noch lesen.
- Noch kein belegter evolutionärer T3-Lauf, keine Torfreigabe, kein Abschlussreview.
- Letzter Todo-Stand:
  - `grundlage`: completed.
  - `werk`: in_progress; Verfassung wartet laut dokumentiertem Stand auf Chat-Claude.
  - `adapter`: pending; Teilintegration bereits implementiert.
  - `lauf`: pending.
  - `abschluss`: pending.

## Blocked
1. **Verfassung/Freigabe:** Sichtbarer Ablauf belegt nur `verfassung-entwurf-01`, keine umgesetzte `verfassung-02`. Die in Fokusmetadaten genannten drei Auflagen sind nicht ausgeschrieben. Ohne diese keine verlässliche Umsetzung oder Laufentscheidung rekonstruierbar.
2. **Aktuell rote Fundprüfung:** `tests/test_t3_fundpruefung.py` Exit 1; Ausgabe liegt in `/root/biotop-t3/fundpruefung-ts-rot.txt`. Ziel: TypeScript-Testnamen und Ergebnisse nicht als Python behandeln.
3. **Vollständige Regression offen:** Die vier bisherigen Fehler sind nur gezielt nachgetestet. TypeScript-Adaptertests waren vom großen Lauf ausgeschlossen.
4. **Zwei übersprungene echte Prüfungen:**
   - `tests/test_eichproben.py:224: Private Werk-/DB-Kopie nicht angegeben`
   - `tests/test_review_vertrag.py:229: Private Werk-/DB-Kopie nicht angegeben`
5. **Echte Adapter-/Kammer-/Werkresultate fehlen:** Subagenten-Endresultate, reale TypeScript-Messungen, Generation −1/0, Hebungslauf und Tor-4-Abschluss sind nicht belegt.
6. **Harte Budgetkontrolle:** Unbekannter Anbieter-Verbrauch soll weitere Aufrufe sperren, statt bei einer neuen Lauf-ID umgangen zu werden. Auftragsweite Wirkung und tatsächliche Abrechnung müssen im realen Lauf nachgewiesen werden.

## Key Decisions
- **Breitentest statt Handelssystem:** Fassung 7 korrigierte die unbestätigte alte Werkfestlegung. Phase 5 ist erst das erste echte Werk, von Philipp nach dem Breitentest zu wählen.
- **Bestehender Kern statt Ersatzdemo:** TypeScript wird in vorhandene Organe integriert; keine separate Scheinpipeline als Tor-Nachweis.
- **`versandwerk` als Übungswerk:** Fünf Bereiche, gewünschter Quellumfang 1.500–2.500 physische TS-Zeilen ohne Tests/Konfiguration/Lockfiles.
- **Verfassung separat bestätigen:** Bau/Eichung parallel erlaubt; Evolution nicht durch die allgemeine Bauvollmacht freigegeben.
- **TDD und explizite Gegenproben:** Jede neue Naht zunächst mit rotem Test; gestellte Adapterantworten klar von realer Kammerausführung getrennt.
- **Ausfall ist null Beitrag:** Leere Ausgabe, Refusal, Inhaltsfilter und missgebildete Antworten dürfen nicht als neutraler Verzicht oder erfolgreiche Modellarbeit zählen.
- **Verbrauch bleibt Verbrauch:** Bei Refusal mit belegter Usage Kosten buchen; bei unbekannter Usage konservativ stoppen.
- **Semantische Äquivalenz nicht aus endlichem Raster ableiten:** Gleiche Referenzwerte allein reichen nicht; Codebeleg erforderlich.
- **Generation-0-Freeze:** Erfolgsflag allein reicht nicht; die geforderte 80-%-Schwelle muss erfüllt sein.
- **Instrument vollständig versiegeln:** Nicht nur Python und Haupt-Dockerfile, auch TS-Skripte und Werkzeug-Lockfiles gehören in die Bindung.
- **Wirkungskreis anhand tatsächlicher Dateien:** Deklarierter Bereich allein ist unzureichend.
- **Kein Abschlussreview vorziehen:** Implementierung und laufende Regression zählen nicht als der vereinbarte eine Abschlussreviewdurchgang.

## Errors & Fixes
- Alter Bestandspfad `/root/.hermes/hermes-agent/gateway` war falsch:
  `Path not found: /root/.hermes/hermes-agent/gateway`.
  Tatsächlicher untersuchter Pfad war `/usr/local/lib/hermes-agent/gateway`.
- Alte fachliche Fortsetzung „Vorbedingung 2 / Verfassung des Handelssystems“ wurde durch die wörtliche Nutzerkorrektur zu Fassung 7 aufgehoben; keine Handelswerk-Arbeit weiterführen.
- Erste kombinierte Vorbereitung/Umgebungsprüfung endete **Exit 127**; `/root/biotop/.venv/bin/python` wurde dabei geprüft. Später eigene venv mit `uv` erfolgreich angelegt.
- Anbieteradapter akzeptierte zuvor leere Inhaltsantworten als `""`; Tests machten dies rot. `AnbieterFehler` bekam `verbrauch` und `ausfallart`; Refusal/Leertext wurden als Ausfall behandelt.
- `_tokens_schaetzen` mit Zeichen/3 unterschätzte Unicode; durch UTF-8-Bytes plus Nachrichtenreserve ersetzt.
- In `lauf.py` wurde eine beim Sprachnahtumbau erzeugte überzählige schließende Klammer bei `_immun_`-/Testendung-Verarbeitung korrigiert.
- Gegenprobe in `test_t3_vorfreeze_vertrag.py` hatte unpassende Regex:
  `match='Eichgegenstand|Vertrag'` wurde auf `match='Eichgegenstand|Verträg'` geändert. Danach 39 fokussierte Tests grün.
- Große Regression:
  ```
  FAILED tests/test_nachweis_verbraucher.py::test_pflichtvorspann_fundskip_stoppt_vor_proben_und_freigabe
  FAILED tests/test_nachweis_verbraucher.py::test_pflichtvorspann_ausgefuehrter_fund_erreicht_proben
  FAILED tests/test_nachweis_verbraucher.py::test_pflichtvorspann_leerer_fundbestand_ist_keine_fehlende_pruefung
  FAILED tests/test_vorspann.py::test_unit_nachweis_bindet_vollstaendiges_instrument_und_quellen
  ```
  - Bei letzterem erwartete der Test nur Pythondateien und `kammer/Dockerfile`; tatsächliche Bindung enthielt zusätzliche TypeScript-Werkzeugdateien.
  - Exakter sichtbarer Fehler:
    ```
    > assert q['instrument']['dateien'] == erwartet
    E AssertionError: assert ...
    E Left contains 9 more items:
    ```
  - Testfixtures/Erwartung aktualisiert, nicht Schutz abgeschwächt; alle vier gezielt bestanden.
- Aktuell offen: TypeScript-Fundprüfungstest rot; Fehlerdetails noch nicht ausgelesen.

## Resolved Questions
- **Welche Fassung gilt?** Fassung 7 ersetzt Fassungen 1–6.
- **Ist das Handelssystem T3 oder Phase-4-Werk?** Nein; alte Bezugsgrößen ungültig.
- **Wer bestätigt die T3-Verfassung?** Im sichtbaren Nutzerentscheid Chat-Claude nach Abschnitt 3.3 für Übungswerke.
- **Ist der Entwurf veröffentlicht?** Ja, `verfassung-entwurf-01`; 5/5 Dateien über HTTPS bytegleich gemeldet, Dateiliste und Manifest veröffentlicht.
- **Ist ein fehlgeschlagenes Verbundmitglied ein Beitrag?** Nein; lokale gestellte Gegenproben wurden implementiert. Das ersetzt keinen vollständigen realen Tor-Nachweis.
- **War `/status` ausgeführt?** Nein. Die frühere Sitzungsverifikation beruhte auf Sitzungsdaten, nicht einem Telegram-`/status`-Aufruf. Für T3 nicht nochmals nötig.

## Relevant Files
**Norm und Fortsetzung**
- `/root/.hermes/cache/documents/doc_3c96ba267e1c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md` — vollständige aktuelle Norm.
- `/root/biotop-t3/STAND-ARBEIT.md` — Fortsetzungsstand, 43 Zeilen; kein Abschluss.
- `/root/biotop-t3/ARBEITSTEILUNG.md` — Zuständigkeiten, 26 Zeilen.
- `/root/biotop-t3/vorbereiten.py` — Vorbereitung/Sicherung/Kasse, 60 Zeilen.
- `/root/biotop-t3/VERFASSUNG-T3-ENTWURF.md` — 13-zeiliger Entwurf.
- `/root/biotop-t3/verfassung_veroeffentlichen.py` — Veröffentlichung/HTTPS-Verifikation, 38 Zeilen.

**Geänderter Kern**
- `/root/biotop/biotop/anbieter/__init__.py` — Ausfallklassifikation, Verbrauch, konservative Tokenreservierung.
- `/root/biotop/biotop/kern/kasse.py` — Sperre bei unbekanntem Verbrauch.
- `/root/biotop/biotop/kern/sprachprofil.py` — neue Sprachnaht.
- `/root/biotop/biotop/kern/messgeraet.py` — TypeScript-Dispatch.
- `/root/biotop/biotop/organe/aufnahme.py`, `landkarte.py`, `vertraege.py` — Sprachwege.
- `/root/biotop/biotop/organe/genesis.py` — `SYSTEM_TYPESCRIPT`, `antwortstatus`, Schwarmverarbeitung.
- `/root/biotop/biotop/organe/generation0.py` — TypeScript-Mutanten-, Äquivalenz- und Testbaupfade.
- `/root/biotop/biotop/organe/aegis.py` — TypeScript-Testoperationen und `wirkungskreis_dateien`.
- `/root/biotop/biotop/organe/verfassung.py` — geschützte TypeScript-Prüfkonfiguration.
- `/root/biotop/biotop/organe/vorspann.py` — Instrument-/Vertragsbindung und Freeze-Sperren.
- `/root/biotop/biotop/lauf.py` — Sprachintegration/Schwarmbeiträge.
- `/root/biotop/biotop/organe/fundpruefung.py` — gelesen; aktuell zur TypeScript-Reparatur anstehend.
- `/root/biotop/biotop/kern/typescript...` und `/root/biotop/biotop/kern/ts/` — Adapterunteragent, vollständiger Stand nachlesen.
- `/root/biotop/kammer/typescript/package.json` — fest versionierte Werkzeugabhängigkeiten.

**Tests**
Unter `/root/biotop/tests/` neu:
`test_t3_verbundausfall.py`, `test_t3_sprachwege.py`, `test_t3_integration_dispatch.py`, `test_t3_kernsperren.py`, `test_t3_testoperationen.py`, `test_t3_bindung.py`, `test_t3_modellvorlagen.py`, `test_t3_generation0.py`, `test_t3_budgetgrenze.py`, `test_t3_ausfall_schwarm.py`, `test_t3_aequivalenz.py`, `test_t3_wirkungskreis.py`, `test_t3_vorfreeze_vertrag.py`, `test_t3_fundpruefung.py`.
Bestehende Testdateien nachgezogen: `test_nachweis_verbraucher.py`, `test_vorspann.py`.

**Belege**
- `/root/biotop-t3/VERBUNDAUSFALL.json` — lokale gestellte Adapter-/Genesis-Ausfallprobe.
- `/root/biotop-t3/kernintegration-02.txt`, `kernintegration-02.xml` — 39 grüne Tests.
- `/root/biotop-t3/regression-01.txt`, `regression-01.xml` — große rote Regression.
- `/root/biotop-t3/bindung-gegenproben-01.txt`, `bindung-gegenproben-01.xml` — grüne Instrumentgegenproben.
- `/root/biotop-t3/fundpruefung-ts-rot.txt` — aktuell rote Prüfung.
- Zahlreiche weitere `*-rot.txt`/`*-gruen.txt` im Auftragsbereich dokumentieren TDD-Zwischenschritte.

## Critical Context
- Fassung-7-SHA256 laut Arbeitsstand:
  `a3b3ac0c17371306b027591110f528018f62d5c2feb4ad82dc21823f14bd76ed`.
- Veröffentlichter Entwurfsordner:
  `laeufe/biotop-t3-typescript/verfassung-entwurf-01/`.
- Gemeldete Ordnerprüfsumme:
  `dc556d9c4a53fe099877694310e7af6d6dfbb2b4632d2674cf5d83a1c0952406`.
- Öffentlicher lokaler Abschlussbereich:
  `/var/pruefkanal/oeffentlich/_akte/[REDACTED]/laeufe/biotop-t3-typescript/`.
- Entwurf-Abholadresse, zugangsbezogener Bestandteil redigiert:
  `https://milieulux-reinigung-muenchen.de/_akte/[REDACTED]/laeufe/biotop-t3-typescript/verfassung-entwurf-01/VERFASSUNG-T3-ENTWURF.md`.
- Dateiliste:
  `https://milieulux-reinigung-muenchen.de/_akte/[REDACTED]/laeufe/biotop-t3-typescript/verfassung-entwurf-01/DATEIEN.txt`.
- Manifest:
  `https://milieulux-reinigung-muenchen.de/_akte/[REDACTED]/laeufe/biotop-t3-typescript/verfassung-entwurf-01/MANIFEST.sha256`.
- Werkzeugversionen aus angelegtem `package.json`:
  - TypeScript `5.7.3`
  - Vitest `2.1.8`
  - ESLint `9.17.0`
  - `typescript-eslint` `8.18.2`
  - `eslint-plugin-security` `3.0.1`
  - `knip` `5.41.1`
  - `tsx` `4.19.2`
  - Paket `biotop-typescript-werkzeuge`, Version `1.0.0`, `private: true`, `type: module`.
- Neue Adapter-Schnittstellenwünsche an Unteragent:
  - `ref_beobachten` → `{'gueltig': bool, 'sha256': str, 'anzahl': int, 'grund': str, 'roh': ...}`.
  - Kanonisches JSON für Referenzbeobachtung, keine float-Zeitwerte im Hash.
  - Ein zusammenhängender Containerlauf für `messen()` bevorzugt, weil Eichkosten bislang einen Kammeraufruf je Messung voraussetzen.
  - Echter Typbau je Mutant vor Behavioral-Catch, z. B. `testlauf(..., bauen=True)` oder `baulauf(...)` mit `{'gueltig','baut','rc','roh'}`.
- Masterprompt-V7-Änderungen:
  - Vorbedingung 1 abgenommen am 21.09.2026; Tor 2 Zeile 8 **9,09 %**; Artgedächtnis **3 von 5 Richtungen** mit werkübergreifendem Verweis.
  - Gültiger damaliger Kassenstand aus Datenbank **8,64 €**, nicht aus Berichten summierte **7,82 €**. Das ist nicht automatisch T3-Verbrauch.
  - Bekannter Opus-Vorfall: `stop_reason: refusal`, Kategorie `cyber`, HTTP 200 ohne Ausgabetext.
- Viele Toolresultate waren komprimiert oder Scriptinhalte abgeschnitten. Bei Bedarf Dateien lesen; keine vollständige Implementierung aus verkürzten Aufrufen rekonstruieren.

## Detailed Session Log (oldest first)
- **21.09.2026:** Hermes-Slashcommand-/MOA-Referenzen und Gatewaycode untersucht. Falscher Pfad `/root/.hermes/hermes-agent/gateway`; anschließend `/usr/local/lib/hermes-agent/gateway/slash_commands_status.py` und `control_socket.py` gelesen. Sitzungswechsel `20260920_063003_896e94ff` → `20260921_015554_e79a4a0f`, Modell `astra-opus-max (moa)` aus Sitzungsdaten bestätigt; `/status` nicht ausgeführt.
- Zwischenbericht, Übergabe aus `uebergabe-abnahme-01` und Masterprompt v6 wurden gelesen. Damalige Fortsetzung war Handelssystem-Verfassung; später ausdrücklich durch v7 überholt.
- Nutzer lieferte `INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md` und T3-Auftrag. Assistent begrenzte Arbeit auf T3 und 10 € gemeinsame Grenze über Laufabbrüche.
- Skills zu TDD, Messdisziplin, JUnit, Codeinspektion und systematischem Debugging geladen. Todo mit `grundlage`, `werk`, `adapter`, `lauf`, `abschluss` angelegt.
- Vollständiger Masterprompt aus Cache gelesen; vorhandene Biotop-Pfade, Dockerimages, Gitstatus und DB-Struktur abgefragt. Ergebnisse teils nur als verkürzte Toolresultate erhalten.
- Kernorgane umfassend gelesen; insbesondere `messgeraet.py`, `lauf.py`, `generation0.py`, `vorspann.py`, `eichproben.py`, `eichgegenstand.py`, `aegis.py` und `fundpruefung.py`.
- `/root/biotop-t3/vorbereiten.py` angelegt/ausgeführt. Erste kombinierte Prüfung mit `/root/biotop/.venv/bin/python` endete Exit 127. Später:
  ```bash
  uv venv /root/biotop-t3/venv &&
  uv pip install --python /root/biotop-t3/venv/bin/python -r /root/biotop/requirements-test.txt
  ```
  erfolgreich.
- Entwurf `VERFASSUNG-T3-ENTWURF.md` angelegt; `versandwerk`, fünf Bereiche, Vitest und eigene Statik angekündigt. `clarify` bot direkte Bestätigung, Warten auf Chat-Claude oder Änderung; Nutzer wählte Option 2.
- Veröffentlichungsscript `verfassung_veroeffentlichen.py` angelegt und mit Timeout 160 s ausgeführt, Exit 0. Assistent meldete „5 von 5 Dateien“ HTTPS-bytegleich und lieferte Entwurf, Dateiliste, Manifest und SHA `dc556d9c4a53fe099877694310e7af6d6dfbb2b4632d2674cf5d83a1c0952406`. Evolution blieb gesperrt.
- `ARBEITSTEILUNG.md` geschrieben. Unteragenten gestartet:
  - Adapter/Kammerimage: TDD, kein Review, enges Dateieigentum.
  - Werkbau: genau fünf Bereiche, 1.500–2.500 physische TS-Quellzeilen ohne Tests/Konfiguration/Lockfiles, fünf versiegelte Schwächen.
- Anbieter-Ausfall-TDD:
  - `test_t3_verbundausfall.py` zuerst rot.
  - `AnbieterFehler(RuntimeError)` erhielt `verbrauch=None`, `ausfallart="infrastruktur"`.
  - HTTP-Antworten mit Leertext, Whitespace, `refusal`, `content_filter` werden als Ausfall behandelt.
  - Belegter Verbrauch aus nichtnegativen Integer-Usage-Feldern wird bei Fehlern gebucht.
  - Protokollierter Ausfall enthält null Beiträge; unbekannter Verbrauch sperrt weitere Budgetprüfung.
  - 7 Tests grün; mit Genesis-Mischfall gültiger Nachbar/ausgefallenes Mitglied 8 Tests grün.
- `test_t3_sprachwege.py` rot → `sprachprofil.py` eingeführt; Erkennung anhand Paket und echten Quellen statt Werkname oder Torflag. `aufnahme.py` und weitere Sprachwege angepasst; 4 Tests grün.
- `test_t3_integration_dispatch.py` rot → TypeScript-Dispatch am bestehenden Mess-/Organpfad; 4 Tests grün.
- `test_t3_kernsperren.py` rot → TS-Prüfanker geschützt, Generation-0-Erfolg vor Freeze erzwungen; 4 Tests grün.
- `test_t3_testoperationen.py` rot → Aegis-Funktionsauswahl/Testzulassung sprachfähig; 3 Tests grün.
- `test_t3_bindung.py` rot → `vorspann.py` bindet TS-Werkzeugkette mit ein.
- `test_t3_modellvorlagen.py` rot → `genesis.SYSTEM_TYPESCRIPT` und passende Aegis-Vorlagen; Vitest/`.test.ts` statt pytest; Testcodeblöcke sprachgerecht.
- `test_t3_generation0.py` rot → Generation-0-Sprachnaht, Abgrenzung Verhaltensfang/Runnerabbruch. Gemeinsame damalige Suite **31 passed in 0.57s**.
- `test_t3_budgetgrenze.py` rot für `'🧪漢字' * 100` → `_tokens_schaetzen` von Zeichen/3 auf UTF-8-Bytezahl plus 256 geändert.
- `test_t3_ausfall_schwarm.py` rot → `genesis.antwortstatus` trennt expliziten Verzicht, brauchbare Antwort und missgebildete Ausgabe; zusammen mit Budgettests **3 passed in 0.11s**.
- Adapter-Unteragent `sa-0-eba8fb38` erhielt Schnittstellenhinweise zu Referenzhash, Einzelcontainer-Messung und Typbau vor Mutantenbewertung; vollständige Rückmeldungen nicht überliefert.
- `test_t3_aequivalenz.py` zunächst rot. Erwartung bewusst verschärft: gleiche endliche Rasterwerte sind kein semantischer Beweis. `_aequivalenz_typescript` ergänzt.
- Generation-0-Vitest-Testbau `_tests_typescript` ergänzt; gültiges ausgeführtes Original/Mutant-Paar erforderlich. Kombinierte Suite Generation 0, Äquivalenz, Vorlagen und Bindung **10 passed in 0.21s**.
- `test_t3_wirkungskreis.py` rot → `aegis.wirkungskreis_dateien` ergänzt, danach realen `pruefen`-Pfad mit `{**dateien, **(extra_code or {})}` angebunden.
- `test_t3_vorfreeze_vertrag.py` rot → `vorspann._vertraege_aktuell` ergänzt, Vertragsbytes und DB-Identität vor Freeze gebunden. Test-Regex wegen tatsächlichem Wortstamm `Verträg` korrigiert.
- `STAND-ARBEIT.md` geschrieben. Fokussierte Suite:
  ```bash
  set -o pipefail; PYTHONPATH=/root/biotop /root/biotop-t3/venv/bin/python -m pytest tests/test_t3_*.py -q --junitxml=/root/biotop-t3/kernintegration-02.xml 2>&1 | tee /root/biotop-t3/kernintegration-02.txt
  ```
  Ergebnis **39 passed in 0.75s**.
- Gesamtregression gestartet:
  ```bash
  set -o pipefail; PYTHONPATH=/root/biotop /root/biotop-t3/venv/bin/python -m pytest tests -q --ignore=tests/test_typescript_adapter.py --junitxml=/root/biotop-t3/regression-01.xml 2>&1 | tee /root/biotop-t3/regression-01.txt
  ```
  Prozess `proc_711f5813ec7a`, PID 2009072.
- Öffentlichen `ZWISCHENBERICHT.md` unter `laeufe/biotop-t3-typescript/` aktualisiert; kein Abschluss. Todo-Grundlage abgeschlossen, Werkbau laufend.
- Nutzer übermittelte Hintergrundabschluss: **4 failed, 338 passed, 2 skipped in 303.20s (0:05:03)**.
- Bei `tests/test_vorspann.py:171` zeigte die Instrumentbindung neun zusätzliche Dateien. Sichtbare Beispiele:
  - `biotop/kern/ts/ast.mjs`: `f09a730dbb3e2a49a70caef151bfa006349c59aec9e777c7ae315f2b82372871`
  - `biotop/kern/ts/bau.mjs`: `5c978d43d84ed354b8a01e85313779050865032d68c326780140e4238d9e7619`
  - `biotop/kern/ts/main.mjs`: `5e0982f56a2beec5e143b7a907c81bc0d54b141c383962819e0df8f44c575723`
  - `biotop/kern/ts/reporter.mjs`: `1d530dcb0bb73b33d7f77198582a1d36dffaff0b408c8d22c5726286ecba4c49`
- Assistent erklärte ausdrücklich: „ohne Prüfbedingungen abzuschwächen“, kein Abschlussreview und keine Torfreigabe.
- `regression-01.txt`, `tests/test_nachweis_verbraucher.py` und `tests/test_vorspann.py` gelesen. Testfixtures und Erwartungsmenge angepasst. Vier zuvor fehlgeschlagene Tests gezielt **4 passed in 1.50s**.
- Zwei Bindungsgegenproben hinzugefügt für:
  `biotop/kern/ts/messen.mjs` und `kammer/typescript/package-lock.json`.
  Ziel: Änderung nach Versiegelung invalidiert Nachweis. `test_t3_bindung.py` **4 passed in 0.22s**.
- Zuletzt `tests/test_t3_fundpruefung.py` geschrieben, 31 Zeilen, Beschreibung:
  `"""TS-Fundneubewertung darf Testnamen/Ergebnisse nicht als Python lesen."""`
- Letzte Aktion: Ausführung dieser neuen Tests, Protokoll `/root/biotop-t3/fundpruefung-ts-rot.txt`, **Exit 1**. Noch kein Lesen der vollständigen Ausgabe und keine Implementierungsreparatur dokumentiert.

## Pruned Skills
[SKILL_PRUNED: content lost in compression; reload with skill_view(name='hermes-agent')]

[SKILL_PRUNED: content lost in compression; reload with skill_view(name='test-driven-development')]

[SKILL_PRUNED: content lost in compression; reload with skill_view(name='measurement-harness-discipline')]

[SKILL_PRUNED: content lost in compression; reload with skill_view(name='codebase-inspection')]

[SKILL_PRUNED: content lost in compression; reload with skill_view(name='systematic-debugging')]

[SKILL_PRUNED: content lost in compression; reload with skill_view(name='measurement-harness-discipline')]

## Anchor Index (mechanically extracted, exact)
branches: docs/llms.txt, docs/user-guide/slash-commands
files: root/biotop/biotop/organe/generation0.py(x5), root/biotop/biotop/anbieter/__init__.py(x5), root/biotop/tests/test_vorspann.py(x4), root/biotop/biotop/organe/aegis.py(x4), root/biotop/biotop/lauf.py(x4), root/biotop/tests/test_t3_verbundausfall.py(x4), tests/test_nachweis_verbraucher.py(x3), root/biotop/biotop/organe/gedaechtnis.py(x3), tmp/biotop-phase4-lektuere-mm6_llag/Masterprompt-v6.md(x3), root/biotop/tests/test_t3_bindung.py(x2), tests/test_vorspann.py(x2), root/biotop/tests/test_t3_vorfreeze_vertrag.py(x2), root/biotop/tests/test_t3_wirkungskreis.py(x2), root/biotop/tests/test_t3_generation0.py(x2), root/biotop/tests/test_t3_aequivalenz.py(x2), root/biotop/tests/test_t3_kernsperren.py(x2), root/biotop/tests/test_t3_integration_dispatch.py(x2), root/biotop/biotop/organe/eichproben.py(x2), root/biotop/biotop/kern/kasse.py(x2), root/biotop-t3/verfassung_veroeffentlichen.py(x2), root/biotop-t3/VERFASSUNG-T3-ENTWURF.md(x2), root/biotop-t3/vorbereiten.py(x2), var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-einstieg-20260921-01/BESTAND-AKTUELL.json(x2), root/.hermes/cache/documents/doc_3c96ba267e1c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md(x2), root/biotop/tests/test_t3_fundpruefung.py, root/biotop/tests/test_nachweis_verbraucher.py, tests/test_review_vertrag.py, tests/test_eichproben.py, tests/test_typescript_adapter.py, var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/ZWISCHENBERICHT.md, root/biotop-t3/STAND-ARBEIT.md, root/biotop/biotop/kern/befundklassen.py, root/biotop/tests/test_t3_ausfall_schwarm.py, root/biotop/tests/test_t3_budgetgrenze.py, root/biotop/tests/test_t3_modellvorlagen.py, root/biotop/biotop/organe/eichung.py, root/biotop/tests/test_t3_testoperationen.py, root/biotop/biotop/kern/sprachprofil.py, root/biotop/tests/test_t3_sprachwege.py, root/biotop/biotop/kern/protokoll.py, root/biotop/biotop/organe/fundpruefung.py, root/biotop/biotop/__main__.py, root/biotop/tests/conftest.py, root/biotop/kammer/typescript/package.json, root/biotop-t3/ARBEITSTEILUNG.md, milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-entwurf-01/VERFASSUNG-T3-ENTWURF.md, root/biotop/biotop/organe/vertraege.py, root/biotop/biotop/organe/verfassung.py, root/biotop/README.md, root/biotop/biotop/organe/eichgegenstand.py, root/biotop/biotop/organe/genesis.py, root/biotop/biotop/organe/vorspann.py, root/biotop/biotop/kern/messgeraet.py, root/biotop/biotop/kern/datenbank.py, root/biotop/biotop/organe/landkarte.py, root/biotop/biotop/organe/kammer.py, root/biotop/biotop/organe/aufnahme.py, usr/local/lib/hermes-agent/gateway/control_socket.py, usr/local/lib/hermes-agent/gateway/slash_commands_status.py, usr/local/lib/hermes-agent/gateway/run.py
errors: AssertionError, AssertionError: assert {'biotop/__in...4a20d23', ...} == {'biotop/dien...f88642f', ...}, AppError`, `normalizeError`, Logger mit Redaction)
urls: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/verfassung-(x3), https://milieulux-reinigung-mue...`, https://hermes-agent.nousresearch.com/docs/llms.txt, https://hermes-agent.nousresearch.com/docs/user-guide/slash-commands
(Exact identifiers from the compacted region — use these verbatim, and as session_search query anchors to recover their full context.)

## User Messages (verbatim, newest first)
> [The user sent a text document: 'INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md'. Its content has been included below. The file is also saved at: /root/.hermes/cache/documents/doc_3c96ba267e1c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md]
> 
> [Content of INFINITE-EVOLUTION-BIOTOP-Masterprompt-v7.md]:
> # INFINITE EVOLUTION — Das Biotop
> 
> **Übergabedokument und Masterprompt für Hermes**
> Stand: 21.09.2026 · Fassung 7 · Auftraggeber: Philipp Zöllisch · Prüfer: Chat-Claude
> 
> **Änderungen gegenüber Fassung 6** (aus der Abnahme von Vorbedingung 1 und Philipps Richtungsentscheidung vom 21.09.2026):
> - **Phase 4 ist neu gefasst: Breitentest an mehreren Testwerken statt einem großen echten Werk.** Grund: Philipps Entscheidung — das Biotop soll für jeden Anwendungszweck taugen und dafür in allen Bereichen geprüft sein. Das Handelssystem stand in den Fassungen 1 bis 6 als Phase-4-Werk, war aber eine nie bestätigte Vorentscheidung von Chat-Claude; alle darauf bezogenen Bezugsgrößen (237.000 Zeilen, 17 Dienste, 135 Testfehlschläge) sind gestrichen. **Fehler von Chat-Claude:** eine Vorentscheidung sechs Fassungen lang wie eine Entscheidung geführt.
````

