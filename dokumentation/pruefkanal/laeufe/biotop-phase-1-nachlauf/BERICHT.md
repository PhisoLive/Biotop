# Biotop — Phase 1 Nachlauf (Lauf 3 laut Masterprompt v2, Abschnitt 8) — BERICHT

**Auftrag:** Masterprompt v2 (19.09.2026), Abschnitt 8 „Nachlauf zu Tor 1 — Lauf 3 (Bedingung für Phase 2)"
**Auftraggeber:** Philipp Zöllisch · **Ausführung:** Hermes · **Prüfer:** Chat-Claude · **Budget:** 5 € hart
**Zeitraum:** 2026-09-19 00:38 – 02:20 CEST · **Status:** abgeschlossen. **Tor 1: 9 von 9 Zeilen bestanden** (Zeilen 1–4 neu gemessen in Lauf 9; Zeile 6 neu gemessen in Lauf 10, weil `kasse.py` geändert wurde; Zeilen 5, 7, 8, 9 gelten weiter — Organ-Prüfsummen unverändert). Zusatzzeile (Kurve Lauf 2 mit F2) beigefügt.

„Lauf 3" des Masterprompts ist in der Datenbank **Lauf 9** — davor liegen drei abgebrochene Versuche (Läufe 6, 7, 8), die jeweils einen Mangel im Messgerät aufdeckten. Alle fünf Läufe (6–10) starten vom Lauf-2-Ausgangszustand (Werk-Prüfsumme `d74391bfa4db4d1c…`, identisch mit `lauf2-gen0`) und sind vollständig in der Datenbank und in `ausgaben/`. Nichts wurde gelöscht.

Belegregeln: jede Zahl mit Bezugsgröße; „bestätigt durch Ausführung" nur mit Datei in `ausgaben/`; Entscheidungen von Hermes mit **[Entscheidung Hermes]**.

---

## 1. Tor 1 — Zeilen mit Ergebnis

| Nr | Zeile | Ergebnis | Bezugsgröße | Ausgabe |
|---|---|---|---|---|
| 1 | Landkarte: alle Bereiche, alle Straßen | **bestanden** | 4 von 4 Bereiche; 13 von 13 Straßen (Hermes-Zählung aus Phase 1, Werk unverändert, Commit 058b33e) | `ausgaben/97-tor-zeilen-1-bis-4-lauf9.txt`, `92-landkarte.json` |
| 2 | Schwächen ≥ 4 von 5 behoben; S1 nach „behoben heißt verschwunden" | **bestanden** | **4 von 5** (S1, S3, S4, S5). S1: bandit B307 3 → 0 Punkte, `eval(` 0 Treffer im Quelltext, Befundklassen-Immuntest (6 Umgehungen) im Werk und am Endwerk frisch ausgeführt 6 von 6 bestanden. S2 offen. Kernmaß F2 −5 → 0 (Höchstwert) | `97-…`, `01-befundklasse-B307-umgehungen-lauf2.txt`, `92-gen2.json` |
| 3 | Kein Rückschritt | **bestanden** | 0 von 4 angenommenen Generationen (1, 2, 5, 6) mit gesunkenem Pareto-Maß oder gerissenem Grenzmaß; paarweise gemessen; je Test geprüft | `97-…` Abschnitt Zeile 3; `9N-genN.json` |
| 4 | Halluzinationsprobe | **bestanden** | 0 von 12 Kandidaten im Bereich `bericht` angenommen; `git diff gen0..HEAD -- lagerhaus/bericht` leer | `97-…` Abschnitt Zeile 4 |
| 5 | Lazarus | **gilt weiter** | `lazarus.py` Prüfsumme `fbc538b4…` vorher = nachher | `00-organ-pruefsummen-vorher.txt`, `50-organ-pruefsummen-nachher.txt` |
| 6 | Kasse 0,10 € → Abbruch vor der nächsten Generation | **neu gemessen, bestanden** | `kasse.py` geändert (Preistabelle + claude-sonnet-4.5; Diff in `50-…`). Lauf 10: Abbruch vor Generation 2, Protokoll #2623, 0 Buchungen und 0 `modell.aufruf` danach; 0,0948 € von 0,10 € | `51-tor-kasse-neu.txt` |
| 7 | Laut scheitern | **gilt weiter** | `aufnahme.py` `75b2e96d…` unverändert | `00-…`, `50-…` |
| 8 | Kammer | **gilt weiter** | `kammer.py` `f3197bf1…` unverändert | `00-…`, `50-…` |
| 9 | Anmeldung | **gilt weiter** | `anmeldung.py` `e3145bc0…`, `dienst.py` `7b6618a0…` unverändert | `00-…`, `50-…` |
| Z | Verlaufskurve Lauf 2 mit F2 und Endtestbestand | **beigefügt** | siehe Abschnitt 3 | `40-kurve-lauf2-f2.txt`, `.json` |

---

## 2. Was umgesetzt wurde (Masterprompt v2)

| Punkt | Umsetzung | Stelle |
|---|---|---|
| 3.5 F2 Kernmaß | je Bereich `−fehlgeschlagen − 10·HIGH − 3·MEDIUM − 1·LOW − tote_funktionen`, Höchstwert 0; bestandene Tests zählen nicht | `biotop/kern/messgeraet.py` `kernmass_f2_bereich` |
| 3.5 F2 paarweise Messung | Vorgeneration und Kandidat werden mit dem Testbestand des Kandidaten gemessen (vorhandene Tests + gültige neue + offene Immuntests + Befundklassen-Tests + bestätigte Angriffstests); Zuwachs = Differenz | `biotop/organe/aegis.py` `pruefen()` Schritt 5; Generalprobe in `biotop/lauf.py` |
| 3.5 F2 Pareto-Maße | fehlgeschlagene Tests, Sicherheitspunkte, tote Funktionen, baut — **je Test**: ein Test, der an der Vorgeneration besteht und am Kandidaten fällt, tötet den Kandidaten unabhängig von der Summe **[Entscheidung Hermes nach Lauf 7, s. u.]** | `messgeraet.pareto_f2` |
| 3.5 F2 Grenzmaße | gegen den Ausgangszustand des Laufs: Laufzeit ×2 (×5 bei Sicherheitsgewinn im Bereich, Tauschregel Anhang A Satz 2), größte Funktion / Zyklen / Bauzeit +25 %. Speicher: nicht gemessen (Liste für danach) | `messgeraet.grenzen_f2`, `urteil_f2` |
| 3.5 F2 „behoben heißt verschwunden" | Befundklassen-Katalog (B307, B102) mit 6 bekannten Umgehungen als Immuntest (Introspektion `__subclasses__`, `__mro__`, `__globals__`, Format-String, Import über `BuiltinImporter` mit Nebenwirkungs-Marker, getattr-Kette); Test misst **Ausführung**, nicht nur Abweisung. Wird jedem Kandidaten eines Bereichs mit statischem Befund paarweise mitgegeben | `biotop/kern/befundklassen.py`; `aegis.befundklassen_tests` |
| 3.3 Verfassung des Übungswerks | Anhang A eingelegt (Text + maschinenlesbare Regeln: Tauschregel, verbotene Muster, Einstiege für Befundklassen, `uebungswerk=true`); Ankläger prüft Satz 6 mechanisch (`# nosec`, Prüfwerkzeug-Konfiguration, Testdateien ändern/löschen) — in Lauf 9 zweimal gegriffen (K126 in Lauf 6, K340) | `biotop/organe/verfassung.py`; `verfassungen/lagerhaus.md` + `.regeln.json`; `ausgaben/13-…` |
| 3.6 Neuschreibung | erlaubt, wenn Datei < 100 Zeilen (`auswertung.py` hat 68) — der S1-Fix kam als Neuschreibung | `biotop/kern/diffwerk.py` `NEUSCHREIBUNG_KLEINE_DATEI` |
| 3.7 Sicherheitsangriff | Berührt der Kandidat einen Bereich mit statischem Befund, bekommt der Ankläger Befundklasse + Beschreibung und läuft mit `anthropic/claude-sonnet-4.5` (Zweck-Präfix `schwer.`, eigene Zählung in KASSE.md); 27 schwere Aufrufe in Läufen 6–10 | `aegis._angriff`, `MODELL_ANGRIFF_SCHWER` |
| 4 Vollmacht | Freigabe durch Hermes nur, wenn `regeln.uebungswerk=true`; sonst `LaufFehler` („Freigabe eines Werks mit Betriebszweck nur durch Philipp"). Jede Freigabe protokolliert mit `vollmacht=…` und dem Maß-Urteil | `biotop/lauf.py` `freigabe()`; Protokoll `freigabe.frei` |
| Kurve nachrechnen | `biotop kurve <lauf>`: holt jede angenommene Generation aus Lazarus, legt den Endtestbestand darüber, misst in der Kammer | `biotop/lauf.py` `kurve_nachrechnen` |

Biotop-Code: Commit `01d196c`, Archiv `biotop/biotop-01d196c.tar.gz`.

---

## 3. Zusatzzeile — Verlaufskurve Lauf 2 mit Formel F2 (`ausgaben/40-kurve-lauf2-f2.txt`)

Endtestbestand = 10 Testdateien aus Lauf 2 Generation 5. Jede angenommene Generation aus dem Lazarus-Archiv geholt, in der Kammer gemessen.

| Gen | Tests eigen | F1 alt | F2 (eigene Tests) | F2 (Endtestbestand, paarweise) | Fehlschläge mit Endtests |
|---|---|---|---|---|---|
| 0 | 4 Dateien | 39 | −5 | **−15** | 10 |
| 1 | 4 | 41 | −3 | −13 | 10 |
| 3 | 9 | 49 | −3 | −5 | 2 |
| 5 | 10 | 51 | −3 | **−3** | 0 |

Lesart: F1 stieg um 12 Punkte (39 → 51). Mit F2 und dem Endtestbestand stieg das Werk ebenfalls um 12 (−15 → −3) — aber die Zerlegung zeigt, was das war: 10 Punkte sind behobene Fehlschläge (S3, S5 und die Builtins-Tests von S1), 2 Punkte tote Funktionen (S4). **Die 3 Sicherheitspunkte (B307) blieben in allen Generationen stehen: F2 Gen 5 = −3, nicht 0.** Damit sagt die neue Kurve, was Chat-Claude festgestellt hat: S1 war in Lauf 2 nicht behoben. Der Endwert −3 statt 0 ist der offene Befund. In Lauf 9 endet dieselbe Größe bei 0.

---

## 4. Was gemessen wurde — Lauf 9 (der „Lauf 3" des Masterprompts)

Ausgang: Kernmaß F2 = −5 (formeln −3 wegen B307, preise −2 wegen toter Funktionen); 50 von 50 Tests.

| Gen | Status | F2 paarweise | Angenommen |
|---|---|---|---|
| 1 | angenommen | −6 → −3 (+3) | lager: `reservierung_einloesen` senkt die Reservierung (S3) + Ankläger-Test; preise: 2 tote Funktionen entfernt (S4) |
| 2 | angenommen | −11 → 0 (+11) | formeln: `eval` ersetzt durch ast-Auswerter mit Knoten-Whitelist (S1; bandit 3 → 0; 6 Befundklassen-Umgehungen abgewiesen; Laufzeit 69 → 84 ms, innerhalb ×5); preise: Staffel `>=` (S5) |
| 3, 4 | abgelehnt | — | 0 von 8 Kandidaten überlebt |
| 5 | angenommen | −9 → 0 (+9) | lager: `reservierung_einloesen` nutzt `entnehmen` (NichtGenugBestand statt negativer Bestand) + 2 Ankläger-Tests; preise: negative Staffelpreise abgewiesen + Ankläger-Tests |
| 6 | angenommen | −4 → 0 (+4) | preise: Typprüfung + Ankläger-Tests |

Kandidaten Lauf 9: 48 — angenommen 7, überlebt-nicht-gewählt 3, leer („KEIN VORSCHLAG") 3, abgelehnt 35 (Kernmaß unverändert 14, Grenzmaß gerissen 11, Pareto verletzt 8, Diff nicht anwendbar 1, Verfassung 1). Endwerk: 75 von 75 Tests, 0 bandit-Befunde, 0 tote Funktionen, `eval` 0 Treffer. Kosten 0,3233 € in 108 Aufrufen (Budget 2 €).

**Zeile 2 im Detail (`97-tor-zeilen-1-bis-4-lauf9.txt`):**
- S1 BEHOBEN: `sicherheit_punkte` formeln 3 → 0; `tests/test_formeln_immun_befundklasse_B307.py` im Werk (6 Tests); am Endwerk frisch ausgeführt: 6 von 6 bestanden; direkte Probe an Lauf-2-Ausgang und Lauf-2-Gen-5 (`01-…`): dort 5 von 6 Umgehungen **erfolgreich** (159 Klassen über `__subclasses__` erreichbar, `os` über `BuiltinImporter` importiert und Marker gesetzt) — bestätigt Chat-Claudes Befund.
- S2 NICHT BEHOBEN: Laufzeit lager 135,4 → 135,4 ms; Bestandsführung unverändert. Keine Nische für Geschwindigkeit in Phase 1.
- S3 BEHOBEN: Probe am Endwerk `reserviert_nach_einloesen= 0`.
- S4 BEHOBEN: tote_funktionen 2 → 0, 0 Treffer `_alte_rabattlogik`.
- S5 BEHOBEN: Probe `preis_fuer('A', 10)` bei Staffel ab 10 = 5.0.

---

## 5. Die drei abgebrochenen Versuche — was das Messgerät gelernt hat

Alle **[Entscheidung Hermes]**, jeweils Maßänderung → neuer Lauf vom selben Ausgang (Verfassungssatz 2), protokolliert (`lauf.abgebrochen` #1424, #1720, #2164).

**Lauf 6 (12 Generationen, 6 angenommen, 0,75 €)** — Ergebnis inhaltlich gut (S1 in Gen 9 verschwunden, alle Befundklassen-Umgehungen abgewiesen), aber die Immunisierung schrieb Angriffstests, die der angenommene Kandidat *nicht* besteht, ins Werk: 19 von 95 Tests rot am Ende. Ursache: Satz 7 („jeder Fehler wird zu einem Test") war umgesetzt als „jeder Test kommt ins Werk". Korrektur: ins Werk kommt nur, was der Kandidat besteht; nicht bestandene Funde bleiben im Immunsystem als `offen` und werden späteren Kandidaten des Bereichs paarweise vorgelegt. Beleg: `30-lauf6-uebersicht.txt`.

**Lauf 7 (4 Generationen, 3 angenommen, 0,22 €)** — Generation 4 (K231) machte den S3-Fix aus Generation 1 rückgängig und wurde **angenommen**. Zwei Ursachen: (a) Pareto verglich die *Zahl* der Fehlschläge je Bereich — die Regression eines vorhandenen Immuntests wurde von drei neuen Ankläger-Tests aufgewogen; (b) Ankläger-Tests, die nur an der Vorgeneration fallen, brachten dem Kandidaten +3, obwohl sie sein Fehlverhalten als Vertrag kodierten. Korrektur: Pareto **je Test** (ein an der Vorgeneration bestehender Test, der am Kandidaten fällt, ist eine Regression — Kandidat tot). Beleg mit Diff, Testbestand und Zahlen: `79-lauf7-abbruch-k231-beleg.txt`. Das ist der wichtigste Fund des Nachlaufs: **das Werk ist gegen den Ankläger zu schützen, nicht nur gegen den Schwarm.**

**Lauf 8 (8 Generationen, 3 angenommen, 0,41 €)** — S1, S4, S5 behoben, aber S3 nicht, obwohl 13 von 16 lager-Kandidaten den richtigen Fix vorschlugen: Nach Lauf 7 hatte ich die Fundregel auf „nur Tests, die am Kandidaten fallen" verengt — damit zählte der Nachweis einer Behebung (fällt an der Vorgeneration, besteht am Kandidaten) nicht mehr, und Kandidaten ohne eigenen Test blieben bei „Kernmaß unverändert". Das widersprach 3.5 F2 („Ein Immuntest, der einen echten Fehler beweist, schlägt an der Vorgeneration fehl und besteht am Kandidaten — die Behebung bringt +1"). Korrektur: Fundregel auf 3.5 F2 zurück; der Schutz gegen den K231-Fall ist die Pareto-Prüfung je Test aus Lauf 7, die bleibt. Beleg: `90-tor-zeilen-1-bis-4-lauf8.txt`.

Zusätzlich vor Lauf 6: (1) erster Befundklassen-Katalog prüfte nur „wirft FormelFehler" und bestand fälschlich, weil `auswerten()` das Ergebnis *nach* der Ausführung verwirft — auf Zahl-Ergebnisse und Nebenwirkungs-Marker umgestellt (`01-…`); (2) Referenzlast war nur unter dem Werknamen hinterlegt, erste Ausgangsmessung ohne Laufzeit → verworfen, Suche um Paketnamen erweitert, vor der ersten Generation neu gemessen (`14a-…`, Protokoll `mass.verworfen`).

---

## 6. Kosten

Nachlauf gesamt (Läufe 6–10): **542 Aufrufe, 1,7903 €** von 5,00 € (36 %). Davon schwere Aufrufe (claude-sonnet-4.5): 27 Aufrufe, 0,65 € — der Sicherheitsangriff ist mit Abstand der teuerste Posten je Aufruf. Der „Lauf 3" des Masterprompts (Lauf 9) allein: 0,32 €. OpenRouter-Konto gesamt (Phase 1 + Nachlauf): 2,31 USD. Details `KASSE.md`.

Für Abschnitt 6 des Masterprompts: Phase-2-Schätzung „2–8 € je Lauf" für das Übungswerk ist mit vier Nischen und Generation 0 plausibel; ein Lauf mit einer Nische und schwerem Ankläger kostet gemessen 0,3–0,75 €.

---

## 7. Eigene Entscheidungen von Hermes

1. Pareto **je Test** (nicht in v2 wörtlich; Folge aus Lauf 7). Vorschlag für Fassung 3.
2. Ins Werk nur bestandene Immuntests; nicht bestandene bleiben `offen` im Immunsystem (Folge aus Lauf 6). Vorschlag für Fassung 3: 3.10 präzisieren.
3. Befundklassen-Katalog als Teil des Messgeräts (`befundklassen.py`), Umgehungen für B307/B102; Einstieg je Werk in der Verfassung (`regeln.einstiege`). Katalog nur von Philipp zu ändern.
4. Schweres Modell über OpenRouter (claude-sonnet-4.5), nicht über den Anthropic-Träger, wegen der Vorgabe „Träger bleibt unangetastet"; getrennt gezählt.
5. Lauf 9 nach Generation 6 beendet (Kernmaß F2 = 0 = Höchstwert in allen Bereichen; kein Sättigungsorgan in Phase 1).
6. Freigaben in Läufen 6–10 unter Vollmacht Abschnitt 4 (17 Freigaben, je mit `vollmacht`-Feld und Maß-Urteil im Protokoll).
7. Wechselkurs 1,08 fest; Toleranzen aus Phase 1 durch F2-Grenzmaße ersetzt.

---

## 8. Grenzen und offene Punkte

- **S2 bleibt offen** (Phase 2, Nische „Der Schnelle"). Die Referenzlast misst es (lager 135 ms); niemand schlägt vor, den Bestand zu cachen, weil die einzige Nische Fehler sucht.
- **Der Ankläger erzeugt viele redundante Tests** (Lauf 9: 10 Immuntest-Dateien für 4 Fehler). Satz 7 ist in Richtung ≥ erfüllt. Dedup: Liste für danach.
- **Ankläger-Tests kodieren manchmal Erwartungen, die kein Vertrag deckt** (z. B. „Artikel mit Bestand 0 werden gelistet") — sie fallen dann an Vorgeneration *und* Kandidat, bleiben `offen` und schaden nicht mehr, kosten aber Aufrufe. Schritt 2 (explizite Verträge, Phase 2) wird das eingrenzen.
- **Grenzmaß `groesste_funktion` +25 %** verwarf 11 Kandidaten in Lauf 9, darunter korrekte S3-Fixe mit Fehlerprüfung (14 statt 12 Zeilen). Die Grenze ist Vorgabe von 3.5 F2; die Verfassung kann sie je Werk anders setzen.
- **Laufzeit-Rauschen** in der Kammer bleibt (±15 %); die ×2-Grenze fängt es ab.
- **Kern-Prozesstrennung, Speicher-Grenzmaß, tree-sitter, Nischen 2–4, Generation 0, Verträge/Verhandlung, Gedächtnisse, Mentor, Oberfläche**: unverändert Liste für danach.
- Zwei Skriptfehler in Auswertezeilen (Formatstring in `51-…`, `98-…`) — nachgetragen, keine Messung betroffen.

---

## 9. Inhalt dieses Ordners

- `BERICHT.md`, `KASSE.md`
- `ausgaben/` — 121 Dateien: Organ-Prüfsummen vorher/nachher (00, 50), Befundklassen-Probe (01), Verfassung (13), je Lauf Aufnahme/Landkarte/Maß/Generationen/Freigaben (Lauf 6: 10–29, Lauf 7: 60–79, Lauf 8: 80–88, Lauf 9: 90–97, Lauf 10: 51 + K*), Kurve Lauf 2 (40), Übersicht aller Läufe (98), Protokoll vollständig 2.623 Zeilen mit geprüfter Hash-Kette (99)
- `werk/` — Ausgangswerk (= Lauf-2-Ausgang), gehobenes Werk Lauf 9 Gen 6 mit git-Tags, Lazarus-Archive Gen 0/1/2/5/6
- `biotop/` — Code (Commit 01d196c), Datenbank (alle Läufe 1–10), `PRUEFSUMMEN.txt`
- `DATEIEN.txt`, `PRUEFSUMME-ORDNER.txt`

Abholadresse: `https://milieulux-reinigung-muenchen.de/_akte/<schlüssel>/laeufe/biotop-phase-1-nachlauf/` (kein Listing; Einstieg über `BERICHT.md`, `DATEIEN.txt`).
