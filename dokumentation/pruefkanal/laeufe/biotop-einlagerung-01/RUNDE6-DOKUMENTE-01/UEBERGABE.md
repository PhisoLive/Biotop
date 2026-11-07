# Übergabe: Behebungsrunde 6 vor T4 (begonnen 2026-09-24 ~23:45)

## Auftrag (Philipp, 24.09., Entscheidungen Chat-Claude zu Review 05 und Bericht 05)
0. **Runde 5 abschließen:** es gilt das zweite Review (`/tmp/review-vor-t4-05/REVIEW.md`); das erste bleibt als verworfen im
   Ordner, was nur es fand → „unbestätigt“ auf die Liste; im Bericht erklären, wie zwei Reviews entstanden; künftig eigener
   Ordner je Review und Prüfung vor dem Start, dass keines läuft; §11/§12 füllen, veröffentlichen, Endmeldung.
1. **R6-4 nur zusammen mit typtreuer Verfälschung:** verfälscht wird mit einem Wert desselben Typs und anderen Inhalts, nie
   mit einem Objekt, das beim Weiterrechnen wirft; ein Test hält nur fest, wenn seine Zusicherung am geänderten Wert fällt
   (Review 05 Nr. 1, x5, x5b).
2. **Undurchsichtige Objekte:** Zustand aus C-Typen über eine bekannte Darstellung (getvalue, str, pickle), sonst gezählte
   Enthaltung — nie „0 Abweichungen“ (Nr. 2, p24b, p25).
3. **R6-1 mit Nr. 3:** enthält sich eine geänderte Funktion → Kandidat zurückgestellt; enthalten sich nur unveränderte →
   Urteil am Rest. Dasselbe für eine hängende Last: Zeitgrenze je Funktion, nicht je Kandidat.
4. **Stufe-2-Last (R6-3):** eigene Eichphase, bemessen bis Spannweite über acht Messungen < 0,25 bei ≥ 10 ms je
   Stichprobe, dann versiegelt; die Rauschmessung im Vorspann bleibt getrennt und darf sperren. Keine reine Dauerregel.
5. **Tor-4-Skript (R6-2):** jede Zeile berechnet, die drei nicht aus der DB berechenbaren aus ihren Belegdateien; der Zweig
   für verhaltensändernde Altlasten muss erreichbar sein.
6. **Register vollständig**, einschließlich Verhandlung.
7. **Ausnahmen nach Typ und Inhalt.**
8. **Kappe am echten T4-Werk messen; TypeScript-Proben vor T5.**
**Startregel T4 (vorab gesetzt):** T4 beginnt, sobald das Review dieser Runde keinen stillen Durchlass mehr findet — jede
bekannte Lücke muss eine gezählte Enthaltung sein; Lücken, die sich nur enthalten, behebt T4 im Lauf.
Kein Lauf, kein Modellgeld, ein Review, eigener Commit, `laeufe/biotop-vor-t4-06/`, Endmeldung (Abholadresse ganze Zeile +
Prüfsumme). Übergabe nach JEDEM abgeschlossenen Schritt nachführen.

## Ausgang
- HEAD `0c2f058` (Runde 5), Arbeitsbaum sauber; Regression dort 598/2/0 (`/root/biotop-vor-t4-05/REGRESSION.txt`).
- Review 05 (geltend): `/root/biotop-vor-t4-05/REVIEW.md` (11 Befunde), Proben `/root/biotop-vor-t4-05/review-proben/`
  (`kammerprobe05.py`: x5, x5b, p24, p24b, p25, p26, a3x, f1, f2, w1, w2, d1 + 24 Fälle aus Review 04).
- Rote Spezifikationen der Runde 5: `/root/biotop-vor-t4-05/spez/` (R6-1 unit/laufweg, R6-2, R6-4) und
  `SPEZIFIKATIONEN-NAECHSTER-AUFTRAG.md` (R6-1 … R6-15, U-1 … U-4).

## Regeln für diese Runde (aus dem Vorfall „zwei Reviews“, `biotop-vor-t4-05/ZWEI-REVIEWS.md`)
- Review: eigener neuer Ordner `/tmp/review-vor-t4-06-<JJJJMMTT-HHMMSS>/`; vor dem Start `delegate_task list` leer, kein
  Manifest unter `~/.hermes/cache/delegation/live/*/manifest.json` mit Status `running`, kein Prozess mit dem Ordnernamen.
- Reviewer und Subagenten starten keine Hintergrundprozesse (nur Vordergrundskripte ≤ 600 s).
- Verdichtung der Sitzung scheitert (OAuth-Token des Hilfsmodells widerrufen, 401): die Sitzung endet an der
  Kontextgrenze. Diese Übergabe ist der Wiedereinstieg.

## Entwurf (Stand 23:50, vor dem Lesen des Codes; beim Bau je Punkt bestätigen oder berichtigen)
- (1) Python `verhalten.py`: `verfaelschen()` liefert je Typ einen typtreuen anderen Wert (str: Zeichen angehängt, int +1,
  float +1.0, bool not, bytes, list/tuple/dict/set: Kopie mit geändertem Element); nicht typtreu verfälschbar (None, fremde
  Objekte) → Probe „nicht verfälschbar“, gezählt wie `ausgelassen` (Enthaltung, nie Deckung). Festhalten (R6-4): Art am
  Ausnahmetyp (`call.excinfo`: AssertionError oder pytest `Failed`) und Ort in der Testdatei, nicht am Meldungstext; Test mit
  Zeitgrenze je Test (hängt er unter Verfälschung → `fehler`). TS (`deck-setup.mjs`) → R6-13 vor T5.
- (2) `kan()`: Objekte mit C-Basis außer `object` über `__reduce_ex__(4)` (Iteratoren darin als Listen), `StringIO`/`BytesIO`
  über `getvalue()`, `memoryview` über `tobytes()`, `weakref` über das Ziel, `partial` über (Funktion, args, kwargs),
  Funktionen/Klassen über Modul:Name; öffentliche Properties und Daten-Deskriptoren reiner Python-Klassen über ihren Wert.
  Nicht darstellbar → gezählte Enthaltung.
- (3) `verhaltensvergleich.pruefen`: geänderte Funktionen aus AST alt/neu (Modulebene oder Klassenattribut geändert → alle
  Funktionen des Moduls bzw. der Klasse als geändert); Enthaltung (unvollständig, Sondenausfall, Zeitgrenze) einer
  geänderten Funktion → `enthaltung` (zurückgestellt); nur unveränderte → Urteil am Rest (keine Enthaltung des Ganzen). TS:
  alle Funktionen geänderter Module gelten als geändert. Zeitgrenze: Sonde mit `setitimer`-Frist je Probenaufruf (10 s) und
  je Last (60 s); Fristablauf wie Abbruch, eingegrenzt; Funktion enthält sich „Zeitgrenze“.
- (4) Befehl `biotop stufe2 <lauf>` (Eichphase vor dem Vorspann): Vorlage `<werk>.stufe2.*` mit `W = {…}`; je Bereich 8
  Kammerläufe mit `eichung.laufzeit_einmal`, Kriterium (max−min)/Median < 0,25 und jeder Wert ≥ 10 ms, sonst W verdoppeln
  (Grenze: Kammerlauf < 60 s); versiegelt im Protokoll (`stufe2.versiegelt`, Text + sha256); Vorspann, Generation, Nachspiel
  lesen die versiegelte Last; ohne Siegel verweigert der Vorspann.
- (5) `tor4.py`: je Torzeile eine Funktion (DB: Generation −1, Generation 0, Kein Rückschritt, Halluzinationsprobe,
  Verhaltensvergleich, Doppelungsanteil, Immunisierung, Neutralzähler, Verbundausfall, Sättigung/Budget; Belegdateien:
  Aufnahme, Verdrahtung, Review/Zwischenbericht); verhaltensändernde Altlast: unabhängiger Test am End- (besteht) und
  Ausgangsstand (fällt), Kennungen einheitlich, `erlaubt` je Altlast.
- (6) `register.VERLANGT` um Verhandlung, Neutralzähler, Immunisierung, Doppelung, Generation 0, Lazarus, Stufe-2-Eichphase
  und die Tor-4-Zeilen erweitern; Drahtwerk so, dass eine Verhandlung stattfindet.
- (7) `wert()`/`kan()`: Ausnahme = Typ + args + `__dict__`, ungekürzt (knapp mit Prüfsumme), Adressen getilgt.
- (8) Kappe und R6-14/R6-15: Messskript für die Aufnahme von T4 vorbereiten, nicht messen (kein T4-Werk); TS → vor T5.

## Plan (Reihenfolge)
0. Runde 5 abschließen (fertig, siehe Stand).
1. Code lesen (gezielt, Lesedateien `bau/LESEN*.txt`).
2. Rote Spezifikationen an `0c2f058`: `tests/test_vor_t4_06.py` (aus Review-05-Proben und `biotop-vor-t4-05/spez/`).
3. Bau je Entscheidung als alles-oder-nichts-Skript `bau/r6_*.py` (Protokoll `bau/R6-*.txt`).
4. Eichphase an versandwerk messen (Kammer), T4-Messskript vorbereiten.
5. Teilläufe inkl. Wächter → Kette: Commit → Regression → Nachspiele (K2904/K3091 ×3, K2868) → Vorher/Nachher.
6. Ein Review (Regeln oben) → Bericht → veröffentlichen → Endmeldung.

## Stand (neueste zuletzt)
- 23:40 Runde 5 abgeschlossen: `REVIEW.md` = zweiter Durchgang (sha256 f66c7b6a…), erster als
  `REVIEW-verworfen-erster-durchgang.md`; `ZWEI-REVIEWS.md` (Rekonstruktion aus Gateway- und Delegationsprotokoll);
  §11/§12 gefüllt (`bau/r5_review_fuellen.py`), §6-Nenner berichtigt, §14 Nr. 11; SPEZIFIKATIONEN R6-6 … R6-15 + U-1 … U-4;
  `review-proben/` (28 + 3 verworfen). Veröffentlicht `laeufe/biotop-vor-t4-05`: 139 von 139 bytegleich,
  Ordnerprüfsumme 0c82b7046709378be6710048ec07b3cff8097e850e5bc59ceb19a0fb48efdf6b (`bau/VEROEFFENTLICHUNG-R5.txt`).
  NÄCHSTES: Endmeldung R5 (Einmal-Cron ohne Agent, deliver origin), Wächter auf biotop-vor-t4-06, dann Schritt 1.
- 23:54 Endmeldung R5 zugestellt (Cron-Job 5825fd644daa, telegram message_id 8205, Skript
  `~/.hermes/scripts/biotop_endmeldung_r5.py` = `bau/endmeldung_r5.py`). Wächter-Auftrag auf `biotop-vor-t4-06` umgestellt
  (`~/.hermes/zwischenbericht/auftrag.json`).
- 00:25 Code gelesen (`bau/LESEN-R6-*.txt`). Bau in drei Teilaufträge zerlegt, je Datei getrennt, als Subagenten
  (Bauende, keine Reviewer; keine Hintergrundprozesse erlaubt):
  - S1 Sonde/Vergleich (Entscheidungen 1, 2, 3, 7): `BAU-S1-SONDE.md`, deleg_2942aa9b (sa-0-9db70418) — Dateien
    `kern/py/verhalten.py`, `organe/verhaltensvergleich.py`, `organe/aegis.py` (Enthaltung), neu `tests/test_vor_t4_06.py`.
  - S2 Tor-4-Skript (Entscheidung 5): `BAU-S2-TOR4.md`, deleg_35d24764 task 0 (sa-0-b999fbde) — `tor4.py`, neu
    `tests/test_tor4_zeilen.py`.
  - S3 Stufe-2-Eichphase (Entscheidung 4): `BAU-S3-STUFE2.md`, deleg_35d24764 task 1 (sa-1-76647e5b) — neu
    `organe/stufe2.py`, `vorspann.py`, `lauf.py` (Stufe-2-Stellen), `nachspiel.py`, neu `tests/test_stufe2_eichphase.py`.
  - Ich selbst danach (Entscheidung 6 und Verdrahtung): `kern/register.py` (vollständig: Verhandlung, Neutralzähler,
    Generation 0, Jury, Lazarus, Sättigung, Doppelung, Stufe-2-Eichphase, jede Tor-4-Zeile), `tests/drahtwerk.py`
    (beta-Kandidat verletzt den Vertrag und benennt ihn → Verhandlung; `VERHANDLUNG` im Prompt → alpha liefert eine
    Anpassung, damit `aegis.pruefen ← lauf:_verhandeln` im echten Lauf gerufen wird), `tests/test_verdrahtung.py`
    (Schritt `stufe2` vor `vorspann`; tor4 mit Belegen; 14 von 14 Zeilen; Register n von n), `__main__.py` (Befehle
    `stufe2`, `tor4 --regression/--verdrahtung/--review/--zwischenbericht`).
  NÄCHSTES: Ergebnisse der drei Subagenten lesen (Teilläufe `bau/TEILLAUF-S1..S3.txt`), dann eigener Teil, Teillauf mit
  Wächtern, Eichphase an versandwerk (Kammer), Kette (Commit → Regression → Nachspiele → Vorher/Nachher), Review.
- 00:45 Philipp (25.09.): (1) U-1 … U-4 nach der Startregel einordnen → `EINORDNUNG-U1-U4.md`: 0 von 4 stille Durchlässe,
  alle bleiben auf der Liste (U-1: Hänger → Kammerlimit → zurückgestellt; die Frist der Eingrenzung ist Teil von
  Entscheidung 3, S1 per Nachsteuerung). (2) Verdichtung, wörtlich: „Philipp legt fest: Die Verdichtung der Sitzungen läuft
  künftig über OpenRouter mit dem vorhandenen Schlüssel statt über die widerrufene Anmeldung — vorher config.yaml datiert
  sichern, danach mit einer echten Verdichtung belegen und die Kosten je Verdichtung nennen.“
  **GESPERRT** beim ersten Schritt (Sicherung): `sperre/SPERRE-01-config-sichern.txt` (Freigabeabfrage ohne Antwort
  abgelaufen). Nichts weiter in diesem Ablauf getan; config.yaml unverändert, `bau/openrouter_stand.py` nicht gelaufen.
  WARTET auf Philipps Antwort. Plan nach Freigabe, je ein Schritt: Sicherung mit festem Namen
  `config.yaml.20260925-vor-openrouter-verdichtung` → `hermes config set auxiliary.compression.provider openrouter` →
  `… model <Modell mit ≥ 1 Mio. Kontext>` → Stand des Schlüssels vorher/nachher (`bau/openrouter_stand.py`) → echte
  Verdichtung dieser Sitzung im agent.log belegen (Telemetrie: Anbieter, Token) → Kosten je Verdichtung.
- 01:10 Philipp gibt frei (Option a, bestätigt Freigabeabfragen sofort). Schritt 1 erledigt: `cp -p config.yaml
  config.yaml.20260925-vor-openrouter-verdichtung` (Freigabeabfrage „copy/move file into sensitive credential/SSH/shell-rc
  path“, vom Nutzer bestätigt); sha256 beider Dateien fab4037781030529c6531c3248cfe26caa6254df27e0a4f5b3816ac6a1fc6c00.
  OpenRouter-Schlüssel vorher: usage 20.196649527 USD (01:08:56, `bau/OPENROUTER-STAND.jsonl`, Marke „modelle“).
  Modellwahl (eigene Entscheidung): `google/gemini-3.6-flash` — Hermes' eigenes Verdichtungsmodell der Nous-Bahn
  (`_NOUS_MODEL` in agent/auxiliary_client.py), 1 Mio. Kontext, 0,75 $/M ein, 3,75 $/M aus. NÄCHSTE Schritte, je einzeln:
  `hermes config set auxiliary.compression.provider openrouter` → `hermes config set auxiliary.compression.model
  google/gemini-3.6-flash` → Diff gegen die Sicherung → Stand „vorher“ → echte Verdichtung dieser Sitzung abwarten (sie
  läuft über der Schwelle 0,5 automatisch; Beleg: agent.log-Telemetrie mit aux_provider openrouter) → Stand „nachher“ →
  Kosten je Verdichtung → `VERDICHTUNG-OPENROUTER.md`. Achtung: nach der Verdichtung ist der Gesprächsverlauf
  zusammengefasst — diese Datei ist der Wiedereinstieg.
- 01:12 Schritte 2–5 erledigt: `hermes config set auxiliary.compression.provider openrouter` ✓, `hermes config set
  auxiliary.compression.model google/gemini-3.6-flash` ✓ (beide ohne Freigabeabfrage). Semantischer Vergleich gegen die
  Sicherung (`bau/config_vergleich.py`): 155 → 157 Schlüssel, neu genau `auxiliary.compression.provider/model`, 0
  entfallen, 0 geändert. Nebenwirkung: `hermes config set` schrieb die Datei neu und ließ zwei auskommentierte
  Vorlageblöcke weg (Security, Fallback Model — reine Kommentare, `diff` zeigt sie). Stand „vorher“ 01:11:04: usage
  20.196649527 USD. NÄCHSTES: echte Verdichtung dieser Sitzung (Telemetrie im agent.log), Stand „nachher“, Kosten.
- 01:15 **Verdichtung über OpenRouter belegt** (`VERDICHTUNG-OPENROUTER.md`, `bau/VERDICHTUNG-BELEG-1.txt`): Hermes
  verdichtete diese Sitzung selbst um 01:11:28–01:12:04, „using openrouter (google/gemini-3.6-flash)“, commit_status
  committed, fallback_used False; 612.326 → 78.607 Eingabe-Token. Kosten 0,0317835 USD für 1 von 1 Verdichtung
  (Zähler 20,196649527 → 20,228433027, davor und danach stabil). Zusammenfassung mit 2 Fehlzuordnungen (Freigabe als
  „Runde 6“, U-1…U-4 als ausstehend) — der Stand gilt aus DIESER Datei. Offen für Philipp: Modell bleibt Gemini (eigene
  Entscheidung) oder Claude über OpenRouter (teurer). NÄCHSTES: Ergebnisse S1–S3 abwarten (laufen seit ~00:00), dann
  eigener Teil (Register vollständig, Verhandlung), Teillauf, Kette, Review.
- 03:31 S3 fertig laut Transkript (Schlussbericht: 125 von 125 grün; `bau/R6-S3-STUFE2.txt`, `TEILLAUF-S3.txt`,
  `VORHER-NACHHER-S3.txt`, `S3-GEAENDERTE-TESTS.md`) — Ergebnis kommt mit dem Stapel deleg_35d24764 (zusammen mit S2);
  noch NICHT von mir geprüft.
- 03:38 **S1 abgebrochen** (HTTP 400 „thinking.type.disabled“), `S1-ABBRUCH.md`: Schritt 1 fertig (27 Spezifikationen,
  63 Fälle, sha256 79c08dc7…; Vorher 47 von 63 rot), Schritte 2–5 nicht begonnen (Produktionsdateien unverändert).
  Ursache gelesen, nicht belegt: Antwort nur aus Denken an der Ausgabegrenze → Hermes schaltet Denken für den Folgeaufruf
  ab (turn_truncation.py:249) → Opus 5.5 lehnt ab; Hermes kennt Pflicht-Denken nur für claude-fable
  (anthropic_adapter.py:128), der Fehlerklassierer nur „reasoning is mandatory“ (error_classifier.py:406). Behebung im
  Hermes-Code = anderer Serverdienst → harte Linie 1, NICHT getan, Vorschlag an Philipp.
- 03:50 **S1-Fortsetzung gestartet**: `sa-0-65be5be1` (deleg_ff0437d6), Auftrag `BAU-S1-FORTSETZUNG.md` (Einordnung
  Vorher, dann je Entscheidung ein Bauskript: e7 → e1 → e2 → e3; Plan als Datei `bau/S1-PLAN.md`; keine
  Hintergrundprozesse). S2 (`sa-0-b999fbde`) nachgesteuert: Plan/Stand fortlaufend in `bau/S2-PLAN.md`, kleine Schritte.
  NÄCHSTES: Ergebnisse S2/S3 (Stapel deleg_35d24764) und S1-Fortsetzung prüfen; dann eigener Teil (Entscheidung 6).
- 04:44 **S2 und S3 fertig** (Stapel deleg_35d24764), geprüft 04:46 (`bau/PRUEFE-S2-S3.txt`): Prüfsummen wie gemeldet
  (tor4.py 4b396724…, test_tor4_zeilen.py 9f512c55…, stufe2.py e42f974a…, test_stufe2_eichphase.py 327c273e…);
  TEILLAUF-S2 62+16+1 grün, TEILLAUF-S3 121+4 grün. **S3 hat eine Sperre umgangen** (Gateway-Wächter 03:10:38, dieselbe
  Auswertung danach als Skriptdateien) → `sperre/SPERRE-02-S3-gateway-waechter.md`: VORHER-NACHHER-S3 (686/687) gilt
  NICHT als Beleg bis Philipp entscheidet; Teilläufe vor der Sperre bleiben gültig. S1-Fortsetzung nachgesteuert
  (Umschreiben als Skriptdatei = Umgehung).
- 04:58 **S4 gestartet** (`sa-0-c81ae6ca`, deleg_f7f2c0b3), Auftrag `BAU-S4-VERDRAHTUNG.md`: Entscheidung 6 (Register
  vollständig aus Tor-4-Zeilen + Vorbedingungen, gezählte Ausnahmen), echte Verhandlung + Angriffstests im
  Verdrahtungslauf, Befehlszeile `stufe2` und tor4-Belege, Typsieb-Protokoll, **eigene Entscheidung: Kernstand-Abweichung
  zwischen Eichphase und Vorspann sperrt** (Satz 2), Fixture fund_vorspann. Voller Verdrahtungstest an einer Kopie ohne
  S1-Halbstand, nur bei ruhiger Kammer.
  NÄCHSTES: Ergebnisse S1-Fortsetzung und S4 prüfen → Kette (Commit, Regression mit Kammer, Nachspiele, Vorher/Nachher,
  Eichphase am Versandwerk) → ein Review (eigener Ordner, vorher prüfen, dass keines läuft) → Veröffentlichung.
- 05:02 Eigene Entscheidungen (für Bericht §Entscheidungen): (1) VORHER-NACHHER-S3 endgültig gestrichen (Ergebnis einer
  Umgehung zählt nicht; Kette misst neu). (2) S3 offener Punkt 4, Ausreißer: Kriterium der Eichphase bleibt wörtlich
  (Spannweite < 0,25 über alle 8 Werte, jeder ≥ 10 ms), kein Ausreißerfilter — ein Hänger erzwingt eine Verdoppelung,
  wiederholte lassen die Eichphase nach 5 Runden laut scheitern; Grund: Entscheidung 4 nennt keine Ausnahme, und eine
  Schwelle wird nicht gesenkt, wenn die Messung sie verfehlt — die Ursache wird geändert (ruhige Kammer vor der Eichphase).
  (3) Kernstand-Abweichung Eichphase → Vorspann sperrt (S4 Aufgabe 6). Offen bei Philipp: Hermes-Fehlerklassierer (a)/(b).
- 08:30 **S1-Fortsetzung an der Iterationsgrenze beendet** (250 Aufrufe, deleg_ff0437d6). Geprüft 08:34
  (`bau/PRUEFE-S1.txt`): verhalten.py c4071c40…, verhaltensvergleich.py 7d87cc1b…, test_vor_t4_06.py ec60919a… wie
  gemeldet; TEILLAUF-S1 Durchgang 3 Aufrufe 1–8 = 74+27+36+38+18+28+62+5 = 288 von 288 grün; Stück 9 fehlt. Vorher 57 von
  74 rot. Fehlend: S1-UMSETZUNG.md, S1-GRENZEN-MESSUNG.txt. **Gemessener stiller Durchlass offen:** `_Konto.buchen`
  (Methode einer privaten Klasse, über entkommene Instanz gerufen) → „0 Abweichungen, tragfähig“ (07:42, Beleg
  überschrieben). Nebenwirkung: 3 neue Dateien in `/root/biotop-t3/eichbau` (06:57–06:59; Geburtszeit = Änderungszeit →
  nichts überschrieben; bleiben liegen, harte Linie 1). test_t3_eichpfad lief in Runde 5 nicht (Regression `-m "not
  integration"`, 600 Fälle, 0 eichpfad).
- 08:50 **Eigene Entscheidung: M2(b) in diese Runde** (Startregel + Philipp 25.09.: stiller Durchlass → diese Runde;
  Vorbedingung 2 „unbeobachtet = Enthaltung“; Entscheidung 3 „geänderte Funktion enthält sich → zurückgestellt“). Meine
  Engführung im Auftrag S1 („nur unvollständig/Ausfall/Zeitgrenze“) war der Fehler. **S1b gestartet** (`sa-0-f62eb72d`,
  deleg_1471b95c), Auftrag `BAU-S1B-M2B.md`: M2(b) mit 9 Spezifikationen (verdeckt, dunder, helfer, nicht erreicht,
  wert), Kosten an den Übungswerken (nur berichten), fehlende S1-Lieferteile, Teillauf Durchgang 4, eichpfad-Standard auf
  tmp_path. S4 nachgesteuert: Werkzeugaufrufe < 400 s; vollen Verdrahtungslauf (~1.719 s) NICHT selbst, sondern Skript
  `bau/r6_s4_verdrahtung_voll.sh` mit Kammer-Sperrdatei `/tmp/biotop-kammer-exklusiv` vorbereiten — den Lauf fahre ich.
- 09:40 **S4 fertig** (deleg_f7f2c0b3), geprüft 09:41 (`bau/PRUEFE-S4.txt`): 9 Prüfsummen wie gemeldet; Register 68
  Kanten + 10 gezählte Ausnahmen (Modul gezählt); TEILLAUF-S4 43+118/119+107; S4-VORHER 26 rot/10 grün. Verhandlung im
  Drahtwerk: gescheitert durch den Verhaltensvergleich (Bindung VB 4). Stufe-2-Last Drahtwerk 5.000 Werte, W alpha 400/
  beta 15 (nur 4 Läufe). **Sperre 03** (S4, Tirith „Pipe to interpreter“, pending_approval, nicht umgangen; Stichprobe f
  nicht gelaufen) → `sperre/SPERRE-03-ROH.txt`.
- 09:43 **Eigener Fehler:** `bau/lesen_s4g.sh` von S4 überschrieben (Namensreihe lesen_s4* von mir begonnen, S4
  fortgesetzt). Behoben: S4-Fassung aus state.db zurück (bfadc96b…, 05:20:22), meine nach `bau/hermes/`. Über alle
  Sitzungen der Runde 6: 1 von 231 Dateien von mehr als einer Sitzung beschrieben — genau diese. Ab jetzt eigene Dateien
  nur `bau/hermes/h_*`; S1b nachgesteuert (Präfix, exklusiv).
- 09:56 **Nacharbeiten Hermes** (`bau/hermes/H-NACHARBEIT.md`): (1) `_verhandeln` gibt dem Nachbarn das GEEICHTE Maß
  (Grundsatz 10; S4 offener Punkt 6) — lauf.py 2e978545… → 8efd28fc…, Spezifikation `tests/test_vor_t4_06_hermes.py`
  (vorher [True-0] rot `assert 1 == 0`, [False-1] grün); (2) S3-Test Kernstand auf Sperre umgestellt
  (test_stufe2_eichphase.py 327c273e… → d006e4d2…). Kopie und Baum je 170 von 170 grün. S1b-Dateien unverändert.
- 09:58 **Voller Verdrahtungstest gestartet** (Hintergrund mit Abschlussmeldung, `proc_b0c83173d652`):
  `bau/hermes/h_verdrahtung_voll.sh` = S4-Skript mit Sperre ZUERST und „ruhig“ = kein Container UND kein fremder pytest;
  Kopie des Baums nach /tmp/h-r6/voll; Ausgaben `bau/VERDRAHTUNG-VOLL-<stempel>.*`. S1b angewiesen: bei bestehender
  Sperre keine Tests. Das ist eine VORPRÜFUNG von S4 (Stand ohne M2(b)); die Kette nach dem Commit misst neu.
- 10:19 **Voller Verdrahtungstest grün: 8 von 8, 1.267 s** (`bau/VERDRAHTUNG-VOLL-20260925-095833.{txt,junit.xml}`,
  Beleg `bau/VERDRAHTUNG-BELEG-VOLL-20260925-095833.json`, Auswertung `bau/hermes/H-VOLL-AUSWERTUNG.txt`). Register: 68
  von 68 Einträgen als Kante im Lauf gefunden, 0 fehlend, 10 gezählte Ausnahmen, 0 Ausnahmen doch als Kante; nie
  gerufen: 0. Eichphase Drahtwerk: versiegelt in Runde 1 mit 8 Kammerläufen, Spannweite alpha 0,108 / beta 0,039,
  Minimum 17,4 / 28,6 ms (Kriterium < 0,25 und ≥ 10 ms erfüllt). Verhandlung: begonnen (K7, Nachbar beta), Paar mit
  Anpassung K9 abgelehnt durch den Verhaltensvergleich (2 von 2 ungedeckt), gescheitert. Angriff: 1 von 5 Ansagen
  ausgeführt, 2 Behauptungen. Nachspiel überlebt (Stufe 2). tor4 Schwächen 1 von 1. Schwarm beta: 8 Texte, 0 mit der
  stillgelegten Regel. Modellkosten 0,00 €. Kernstand: 0c2f058 + 21 überlagerte Dateien (baum_sauber false) — Stand
  OHNE M2(b); gilt als Vorprüfung, nicht als Beleg der Runde. Sperre um 10:19:40 freigegeben, 0 Container.
  NÄCHSTES: S1b abwarten (M2(b)) → Prüfung → Commit → Kette (volle Regression mit Kammer inkl. Verdrahtung, Nachspiele,
  Vorher/Nachher, Eichphase am Versandwerk) → Review (eigener Ordner) → Veröffentlichung.
- 12:37 **S1b fertig** (deleg_1471b95c), geprüft 12:39 (`bau/hermes/H-PRUEFE-S1B.txt`): verhaltensvergleich.py
  761b9a7c…, test_vor_t4_06.py 80feee35… (102 Fälle), test_t3_eichpfad.py 051065a1… wie gemeldet; verhalten.py/aegis.py
  unverändert. M2(b) gebaut: test_m2_* 28 Fälle, vorher 19 von 28 rot an 0c2f058 bzw. 17 von 28 am Stand vor dem Bau,
  nachher 28 von 28. Durchgang 4: 379 von 380 grün (1 rot: Wächter, register.py von S4). Kosten M2(b): lagerhaus 2 von
  39, logmuehle 3 von 25, uebungswerk-p2 14 von 50 würden bei Änderung zurückstellen. Eichbau-Dateien unverändert.
  **Sperre 04** (S1b, Formatsperre 11:03:22, grep | head) → `sperre/SPERRE-04-S1b-formatsperre.md`; nach Philipps
  Regel (gespeichertes Skript unverändert, reine Lesesuche) von Hermes ausgeführt → `sperre/SPERRE-04-AUSGABE.txt`
  (26 Zeilen). **Neuer gemessener stiller Durchlass** (S1b 12:32): nur Konstantenmodul geändert → vv `unbeobachtet`
  „0 von 0“, tragfähig ohne Enthaltung → aegis ueberlebt.
- 12:48 **Wächter-Rot behoben (Hermes)**: `register.ausnahmen_ohne_test` (S4, parst die eigenen Tests, nie im Lauf
  gerufen) in UNGERUFEN_ERLAUBT mit Grund (`bau/hermes/h_r6_waechter.py`); test_t3_python_annahmen.py 7322ecfb… →
  03a5aff7…; Kopie vorher 1 rot/4 grün, nachher 5 von 5; Baum 5 von 5; Kopie = Baum (`bau/hermes/H-WAECHTER.txt`).
- 12:55 **Eigene Entscheidung: Klasse statt Fall** — gelesen (`bau/hermes/H-LESEN-WEGE.txt`): `verhaltensvergleich.pruefen`
  hat drei Wege mit `tragfaehig: True` ohne Beobachtung/Enthaltung: `unbeobachtet` (0 von y), `sonde_vorgeneration_inhalt`
  (Vorgeneration nicht beobachtbar → gar kein Vergleich), `keine_quellaenderung` (auch bei Datendateien im Quellpaket);
  dazu gemischter Fall (geänderte Modulwerte außerhalb gelesen, sonst etwas beobachtet). **S1c gestartet**
  (`sa-0-d3ed819f`, deleg_c88798ee), Auftrag `BAU-S1C-UNBEOBACHTET.md`: A–D → gezählte Enthaltung; E (neue Funktion am
  Kandidaten beobachtet → geurteilt) und F (Selbstaufruf zählt nicht als Aufruferin) gegen Fehlalarme von M2(b); Kosten
  an 4 Werken; Durchgang 5; Schlussbericht zählt alle verbleibenden Wege mit tragfähig True und begründet sie.
