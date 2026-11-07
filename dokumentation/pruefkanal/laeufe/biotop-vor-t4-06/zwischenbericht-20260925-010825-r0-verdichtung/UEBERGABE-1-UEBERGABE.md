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
