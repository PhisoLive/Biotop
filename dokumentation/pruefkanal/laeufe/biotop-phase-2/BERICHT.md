# Biotop — Phase 2 „Der Schwarm" — BERICHT

**Auftrag:** Masterprompt v3 (19.09.2026), Abschnitt 8 Phase 2 · **Auftraggeber:** Philipp Zöllisch · **Ausführung:** Hermes · **Prüfer:** Chat-Claude
**Ausgang:** Übungswerk `lagerhaus` im Zustand Lauf 9 Generation 6 (Lazarus-Archiv `lauf9-gen6.tar.gz`, `ausgaben/03-ausgang.txt`), Verfassung Anhang A
**Budget:** 10 € hart (Auftragsbudget über alle Phase-2-Läufe, `kasse.AUFTRAG_BUDGET_EUR`) · **Zeitraum:** 19.09.2026 03:30 – 05:35 CEST
**Status:** abgeschlossen. **Tor 2: 11 von 11 Zeilen bestanden**, alle mit Ausgabe und Bezugsgröße. Hauptlauf = **Lauf 13** (14 Generationen, 7 angenommen). Davor: Lauf 11 (Rauchtest Modellwahl) und Lauf 12 (Vorlauf, 10 Generationen, aufgedeckt: Norm-Regel galt nur für Ankläger-Tests — korrigiert, neuer Lauf). Nichts gelöscht; alle drei Läufe in der Datenbank und in `ausgaben/`.

Belegregeln: jede Zahl mit Bezugsgröße; „bestätigt durch Ausführung" nur mit Datei in `ausgaben/`; Entscheidungen von Hermes mit **[Entscheidung Hermes]**; eingeschleuste Proben-Kandidaten sind im Protokoll (`probe.eingeschleust`) und in der Kandidatentabelle (`nische='probe'`, Status `probe_*`) gekennzeichnet und kamen nie ins Werk.

---

## 1. Tor 2 — Zeilen mit Ergebnis

| Nr | Zeile | Ergebnis | Bezugsgröße | Ausgabe |
|---|---|---|---|---|
| 1 | Nischen: 4 aktiv, je ≥ 2 Anbieter; Bandit-Gewichte nach 10 Generationen | **bestanden** | 4 von 4 Nischen, je 4 von 4 Herstellern genutzt (openai, google, deepseek, qwen); Gewichte nach 14 Generationen protokolliert; 235 `bandit.wahl`-Protokollzeilen | `60-tor2-nischen-bandit.txt` |
| 2 | Generation 0: 20 Hermes-Mutanten, Biotop meldet ungefangene; danach ≥ 16 von 20 | **bestanden** | vorher 16 von 20 gefangen (blind: #4, #7, #13, #19); nach Gen 0: **17 von 20** (Lauf 13; Lauf 12: 18 von 20); #7 und #19 sind äquivalente Mutanten (semantisch nicht unterscheidbar, s. Abschnitt 5) | `45-generation0.json`, `20-generation0.txt` (Lauf 12, mit Tabelle je Mutant), `02-versiegelt-MUTANTEN-phase2-entsiegelt.json` (sha256 `eeb3de60…` vorher: `02-versiegelt-pruefsummen-vorher.txt`) |
| 3 | S2 behoben nach versiegeltem Kriterium; Kernmaß unverändert oder gestiegen | **bestanden** | Kriterium (a) erfüllt: Journal führt inkrementelle Summen (`_summen`), `bestand()` summiert nicht mehr; (b) `last_lager` **139,5 → 5,2 ms (−96 %)**, Soll ≥ 50 %; frische Gegenmessung 3× je Stand: 134–135 ms vs. 4,9–5,3 ms; Kernmaß F2 0 → 0 | `61-tor2-s2.txt`, `02-versiegelt-SCHWAECHEN-entsiegelt.md` (Kriterium vor Lauf 12 festgelegt, sha256 `7ca81c3c…`) |
| 4 | Nebenwirkungsprobe: A hebt, B senkt → 0 von 1; Bericht nennt B | **bestanden** | K1016 (lager: `inventur()` schneller, `artikel()` unsortiert): 0 von 1 angenommen; Grund: Vertrag `test_vertrag_bericht_lager::test_artikel_sortiert…` verletzt; Wirkungskreis [bericht, lager]; Pareto nennt `bericht.tests_fehlgeschlagen 0 → 5` | `50-nebenwirkungsprobe.txt` |
| 5 | Regressionsprobe: frühere Behebung rückgängig + 3 grüne Tests → 0 von 1; Einzeltest genannt | **bestanden** | K1017 (S3 rückgängig + 3 bestehende Tests): 0 von 1 angenommen; 3 mitgebrachte Tests verworfen („besteht schon an der Vorgeneration"); Protokoll nennt Regression je Test: `test_lager_immun_aegis_k311_lager::…`, `test_vertrag_bericht_lager::test_eingeloeste_reservierung_zaehlt_nicht_weiter` | `51-regressionsprobe.txt` |
| 6 | Norm-Probe: Test fällt an Vorgeneration, besteht am Kandidaten, ohne Absturz/Vertragsbezug → offen, 0 Punkte, nicht im Werk | **bestanden** | K1018: mitgebrachter Test als „Norm ohne Absturz/Vertragsbezug — 0 Punkte" verworfen; Zuwachs −1 (nicht +1); nicht ins Werk; Kandidat abgelehnt (bricht `test_beschreibung_kuerzt`). In Lauf 12 war dieselbe Probe **rot** (Test wäre ins Werk gekommen) → Messgerät korrigiert, Lauf 13 | `52-normprobe.txt`; Lauf 12: `lauf12-vorlauf/52-normprobe.txt` |
| 7 | Vertragsprobe: ohne Anpassung des Nachbarn abgelehnt; mit Anpassung angenommen (je 1 Fall) | **bestanden** | ohne: K1019/K1020 abgelehnt am Vertrag `test_vertrag_preise_formeln::test_konsument_preise_uebergibt_waehrung`; mit Anpassung (rabatt.py übergibt `waehrung`): 0 Vertragstests verletzt, 0 Pareto-Verstöße, **Verhandlung bestanden** (K1157 + Anpassung K1158, Protokoll #7251). Das Paar hatte keinen Kernmaßgewinn und wurde deshalb nach 3.5 nicht ins Werk übernommen — die Zeile misst den Vertrag, nicht das Kernmaß (Lesart Hermes, s. Abschnitt 6) | `53-vertragsprobe.txt`, `54-verhandlungsprobe.txt` |
| 8 | Immunisierung: n Fehler = n Tests im Werk; Doppelungsanteil < 20 %; 0 rote Tests nach angenommenen Generationen | **bestanden** | 6 bestätigte Fehler → 6 Immuntest-Dateien neu im Werk (16 gesamt inkl. 10 aus Phase 1; Liste in `62-…`); 237 Angriffstests, 6 Doppelungen = **2,5 %**; 1 Norm-Test offen; rote Tests nach angenommenen Generationen: **0 von 8** (jede aus Lazarus geholt, in der Kammer ausgeführt: 93 → 99 von 99 grün) | `62-tor2-immunisierung.txt` |
| 9 | Verhandlung: ≥ 1 Generation mit gemeinsam bestandener Vertragsänderung protokolliert | **bestanden** (mit Einschränkung) | 1 bestanden (Gen 13, `verhandlung.bestanden` #7251) — **durch die von Hermes eingeschleuste Vertragsprobe**, nicht durch einen Schwarm-Kandidaten; 4 begonnen, 3 gescheitert (Schwarm-Kandidaten in Gen 2/6/9/10 brachen Verträge ohne tragfähige Anpassung des Nachbarn). Ehrliche Lesart: der Mechanismus funktioniert nachweislich; der Schwarm selbst hat in 14 Generationen keine Vertragsänderung durchgebracht | `63-tor2-verhandlung.txt`, `54-verhandlungsprobe.txt` |
| 10 | Verlaufskurve des Hauptlaufs mit Endtestbestand | **beigefügt** | 8 angenommene Generationen aus Lazarus, Endtestbestand 21 Dateien (Gen 13), F2 je Generation + Laufzeiten | `64-tor2-kurve.txt`, `.json` |
| 11 | Modellwahl am OpenRouter-Katalog belegt | **bestanden** | Katalog 19.09.2026 geprüft; neuere Modelle gleicher Hersteller zu gleichem/niedrigerem Preis gewählt (Tabelle Abschnitt 2); Rauchtest je Modell mit Diff-Aufgabe (Lauf 11, 0,0016 €) | `00-openrouter-katalog-schnellmodelle.txt`, `01-modellwahl-rauchtest.txt` |

---

## 2. Modellwahl (Abschnitt 10 v3)

| Rolle | Phase 1 | Phase 2 | Preis USD/Mio (ein/aus) | Grund |
|---|---|---|---|---|
| Masse (Schwarm) | openai/gpt-4.1-mini (04/2025) | **openai/gpt-5.6-luna** (07/2026) | 0,20 / 1,20 (vorher 0,40 / 1,60) | neuer, halber Preis |
| Masse | google/gemini-2.5-flash (06/2025) | **google/gemini-3.5-flash-lite** (07/2026) | 0,30 / 2,50 (gleich) | neuer, gleicher Preis (gemini-3.x-flash kostet 0,75/3,75 → nicht) |
| Masse (3. Hersteller) | — | **deepseek/deepseek-v4.1-flash** (09/2026) | 0,15 / 0,60 | dritter Anbieter |
| Masse (4. Hersteller) | — | **qwen/qwen3.8-flash** (08/2026) | 0,15 / 0,47 | vierter Anbieter |
| Landkarte | gemini-2.5-flash-lite | google/gemini-3.1-flash-lite | 0,25 / 1,50 | billiger |
| Angriff (leicht) | gemini-2.5-flash | gemini-3.5-flash-lite | 0,30 / 2,50 | |
| Angriff (schwer) | claude-sonnet-4.5 | anthropic/claude-sonnet-5 | 2,00 / 10,00 (vorher 3,00 / 15,00) | neuer, billiger; in Phase 2 nicht aufgerufen (kein statischer Befund mehr) |

Rauchtest-Fund: deepseek und qwen liefern bei `max_tokens=200` leere/abgeschnittene Antworten, weil eingebautes Denken das Budget füllt → `reasoning: {enabled: false}` für alle Nicht-Anthropic-Modelle; gemini-3.x lehnt das ab („Reasoning is mandatory", HTTP 400) → dort `effort: minimal`. Beides in `biotop/anbieter/__init__.py`, belegt in `01-…` und im Protokoll (`modell.fehler` #2694, #2704).

---

## 3. Was gebaut wurde (Phase 2)

| Punkt (v3) | Umsetzung | Stelle |
|---|---|---|
| Vier Nischen | sicher (T 0,2), schnell (T 0,3, Ziel Laufzeit, bekommt die Referenzlast), elegant (T 0,4), wild (T 0,9, darf Verträge benennen); je Generation und Bereich 2 Hersteller je Nische → 32 Kandidaten je Generation | `biotop/organe/nischen.py` `NISCHEN`, `genesis.erzeugen` |
| Bandit-Gewichtung | Thompson-Stichprobe Beta(erfolge+1, misserfolge+1) je (Lauf, Nische, Hersteller); Erfolg = Kandidat überlebt den Ankläger; jede Wahl protokolliert (`bandit.wahl`); Gewichte = (e+1)/(v+2) | `nischen.waehlen`, `nischen.buchen`, `nischen.gewichte` |
| MAP-Elites | je (Nische, Bereich) bleibt der beste Überlebende als Elite; der Schwarm der Nische bekommt ihn in der nächsten Generation als Ausgangspunkt | `nischen.elite_setzen`, `genesis.erzeugen` (elite_text) |
| Generation 0 | Mutanten aus dem Syntaxbaum (5 Arten) oder von Hermes gesetzt (JSON); Messung je Mutant in der Kammer; Testbau durch Schwarm (Nische sicher) für blinde Flecken: ein Test kommt nur ins Werk, wenn er am Original besteht UND den Mutanten fängt; Gegenprobe am unmutierten Werk; git-Commit | `biotop/organe/generation0.py`, `lauf.generation0`, CLI `gen0` |
| Verträge explizit | ausführbare Vertragstests `tests/vertraege/test_vertrag_<konsument>_<lieferant>.py` (3 Grenzen, 17 Tests, aus Anhang A Satz 3–5 + Docstring-Verträgen; Teil des Werks); zählen beim Lieferanten; Schwarm bekommt seine Verträge mit | `biotop/organe/vertraege.py`, `verfassungen/vertraege-lagerhaus/`, `ausgaben/12-test_vertrag_*.py` |
| Ankläger Schritt 2 | Vertragstest, der an der Vorgeneration besteht und am Kandidaten fällt = Vertragsverletzung → tot, außer der Kandidat hat den Vertrag unter VERTRÄGE benannt → Verhandlung. Vertragsdateien darf nur ändern, wer den Vertrag benennt | `aegis.pruefen` Schritt 2, `vertraege.verletzt` |
| Ankläger Schritt 3 | Verfassung mechanisch (Satz 6: `# nosec`, Werkzeug-Konfiguration, Testdateien ändern/löschen) — aus Nachlauf | `verfassung.mechanisch_pruefen` |
| Norm-Regel 3.7 F3 | Test, der an der Vorgeneration fällt und am Kandidaten besteht, zählt nur bei (a) Ausnahme im Werk an der Vorgeneration oder (b) Vertrags-/Verfassungsbezug (Wortüberdeckung ≥ 4 Wörter ≥ 5 Zeichen mit einem Vertragstext/Verfassungssatz); sonst `offen_norm`, 0 Punkte, nicht ins Werk. Gilt für Ankläger-Tests **und** mitgebrachte Tests (Letzteres seit Lauf 13) | `aegis._nennt_vertrag`, Schritt c und Schritt 4 |
| Pareto je Test | ein Test, der an der Vorgeneration besteht und am Kandidaten fällt → tot | `messgeraet.pareto_f2` (Nachlauf) |
| Immunisierung 3.10 F3 | ins Werk nur, was der angenommene Kandidat besteht; offene Funde bleiben und werden paarweise vorgelegt; Doppelung = gleiche Meldungsklasse@Ort (auch gegen vorhandene Funde), gekennzeichnet, nicht übernommen; Anteil ausgewiesen | `aegis._doppelungen`, `aegis.pruefen` |
| Grenzmaß größte Funktion | absolut 60 Zeilen; +25 % nur, wenn der Ausgang schon darüber lag | `messgeraet.grenzen_f2` |
| Nischenmaß schnell | angenommen nur bei Laufzeit ≥ −15 % in einem Bereich des Wirkungskreises und Kernmaß ≥; Generalprobe erlaubt reinen Laufzeitgewinn bei unverändertem Kernmaß | `messgeraet.urteil_f2(nische=)`, `lauf._generation_koerper` |
| Verhandlung 3.8 | bei benanntem, verletztem Vertrag: Schwarm des Nachbarn (Nische sicher, 2 Hersteller) erzeugt Anpassung; Paar (Kandidat + Anpassung) wird vom Ankläger geprüft; bestanden = 0 Vertragsverletzungen, 0 Pareto-Verstöße, 0 gerissene Grenzen; Annahme entscheidet dann das Maß | `lauf._verhandeln` |
| Verlaufskurve je Lauf | Pflichtbestandteil (`biotop kurve`) | `lauf.kurve_nachrechnen` |
| Auftragsbudget | 10 € hart über alle Läufe der Phase, Vorprüfung vor jedem Aufruf zusätzlich zum Laufbudget | `kasse.vorpruefung`, `AUFTRAG_BUDGET_EUR` |

Biotop-Code: Commit `9f78b4c` (Archiv `biotop/biotop-9f78b4c.tar.gz`), ~3.900 Zeilen Python.

---

## 4. Was gemessen wurde — Hauptlauf 13

Ausgang (Lauf 9 Gen 6 + 17 Vertragstests + 1 Gen-0-Test): Kernmaß F2 = 0 in allen Bereichen (Höchstwert), 93 von 93 Tests; Laufzeiten bericht/formeln/lager/preise = 25 / 90 / 140 / 73 ms.

| Gen | Status | Angenommen (Nische) | Kernmaß F2 paarweise | Laufzeit ms b/f/l/p |
|---|---|---|---|---|
| 1 | angenommen | lager: Journal führt inkrementelle Summen (schnell, gpt-5.6-luna); formeln: AST-Cache (schnell); bericht: Bestände einmal lesen (schnell) | 0 → 0 | 8,9 / 29 / **4,9** / 34,5 |
| 3 | angenommen | lager: `artikel()` aus `_summen` (schnell) | 0 → 0 | 9,1 / 30,5 / 5,0 / 37,3 |
| 5, 6 | angenommen | bericht: Berichts-Cache (schnell) | 0 → 0 | 7,2 / 31,4 / 4,8 / 37,1 |
| 10 | angenommen | formeln: `pruefen()` prüft Namen laut Docstring-Vertrag (**wild**, deepseek) + 2 Ankläger-Tests mit Vertragsbezug | −2 → 0 (+2) | 6,6 / **157** / 5,1 / 117 |
| 11, 13 | angenommen | formeln: Auswertungs-Cache (schnell) | 0 → 0 | 6,8 / 126 / 5,2 / 99,5 |
| 2, 4, 7, 8, 9, 12, 14 | abgelehnt | 0 von 32 überlebt (8: Generalprobe Kernmaß unverändert) | | |

Kandidaten Lauf 13: 470 — angenommen 9, überlebt-nicht-gewählt 5, Verhandlungs-Anpassungen 5, „KEIN VORSCHLAG" 196 (42 %), abgelehnt 240 (Kernmaß unverändert 80, Pareto/Regression je Test 64, Diff nicht anwendbar 51, Nische schnell ohne Gewinn 29, Vertrag verletzt 8, Grenzmaß 4, sonst 4), Proben 14. Angenommen je Nische: schnell 7, sicher 1, wild 1, elegant 0. Endwerk: **99 von 99 Tests**, 0 bandit-Befunde, 0 tote Funktionen.

**S2 im Detail** (`61-…`): Gen 1, Kandidat der Nische schnell (gpt-5.6-luna): `Journal` führt `_summen: defaultdict(int)`, `summe_fuer()` ist O(1); `bestand()` unverändert `journal.summe_fuer()` — Kriterium (a) erfüllt, weil das Journal nicht mehr summiert. Laufzeit 139,5 → 5,2 ms (−96 %; Kriterium ≥ 50 %). Frische Gegenmessung 3× je Stand in der Kammer: 134,1/135,3/134,4 vs. 5,1/5,3/4,9 ms. Kernmaß 0 → 0.

**Gen 10 — Hinweis (`65-…`):** Der wild-Kandidat K994 behebt einen echten Vertragsbruch (`pruefen` prüfte keine Namen; Docstring sagt „nur bekannte Namen"), aber sein AST-Durchlauf je Aufruf erhöht formeln von 30 auf 154 ms. Grenzmaß: Ausgang 89,6 × 2 = 179 ms → nicht gerissen, Kernmaß +2 → angenommen. Gen 11/13 holen 30 ms davon zurück. Das Grenzmaß ist gegen den **Ausgang** definiert (3.5), nicht gegen die Vorgeneration — der Kandidat hat Regel-konform einen Teil des Laufzeitgewinns von Gen 1 für Korrektheit eingetauscht. Für Fassung 4 zu erwägen: Grenze gegen das Beste des Laufs statt gegen den Ausgang.

---

## 5. Verlaufskurve (Zeile 10, `64-tor2-kurve.txt`)

Endtestbestand 21 Dateien (Gen 13), jede angenommene Generation aus Lazarus:

| Gen | F2 (eigene Tests) | F2 (Endtestbestand) | fehl/sich/tot je Bereich (Endtests) | Laufzeit ms b/f/l/p |
|---|---|---|---|---|
| 0 | 0 | **−2** | formeln 2/0/0 | 24,5 / 89,8 / 139,8 / 84,1 |
| 1 | 0 | −2 | formeln 2/0/0 | 17,4 / 56,3 / 9,3 / 35,8 |
| 3 | 0 | −2 | formeln 2/0/0 | 10,0 / 32,7 / 5,1 / 36,0 |
| 5 | 0 | −2 | formeln 2/0/0 | 13,5 / 38,0 / 5,0 / 37,2 |
| 6 | 0 | −2 | formeln 2/0/0 | 6,6 / 30,6 / 5,0 / 36,0 |
| 10 | 0 | **0** | alle 0 | 6,8 / 147,4 / 4,9 / 111,7 |
| 11 | 0 | 0 | alle 0 | 10,5 / 155,7 / 4,9 / 90,3 |
| 13 | 0 | 0 | alle 0 | 6,6 / 123,8 / 4,9 / 94,9 |

Lesart: Mit dem Endtestbestand zeigt der Ausgang −2 — der `pruefen`-Vertragsbruch, den erst Gen 10 fand und bewies. Der Laufzeitgewinn (Gen 1–6) trägt keinen Punkt (Nischenmaß, nicht Kernmaß), ist aber in der Kurve als Grenzmaß sichtbar.

---

## 6. Eigene Entscheidungen von Hermes

1. **Lauf 12 abgebrochen, Lauf 13 vom selben Ausgang** (Maßänderung → neuer Lauf, Satz 2): die Norm-Probe zeigte, dass die Norm-Regel nur auf Ankläger-Tests wirkte; ein mitgebrachter Norm-Test wäre ins Werk gekommen (`lauf12-vorlauf/52-normprobe.txt`). Lauf 12 selbst: 10 Generationen, 4 angenommen, inhaltlich gleiche Funde (S2 −97 %), vollständig erhalten.
2. **Verhandlung: „bestanden" = Paar ohne Vertrags-/Pareto-/Grenzverletzung**; ob es angenommen wird, entscheidet danach das Maß. Erste Fassung verlangte „ueberlebt" (inkl. Kernmaßgewinn) — damit wäre eine reine Vertragsänderung nie „bestanden" gewesen, obwohl 3.8 Schritt 2 nur die gemeinsame Prüfung verlangt (`54a-…` vs `54-…`).
3. **Zwei Biotop-Fehler während Lauf 13 korrigiert, ohne Maßwirkung**, protokolliert (`biotop.korrektur`): Paarprüfung in der Verhandlung las nur das gespeicherte Einzelurteil (Status nicht zurückgesetzt) — betraf 4 Verhandlungen in Lauf 12/13, alle wären auch danach gescheitert (Anpassungen brachten den Vertragstest nicht zum Bestehen); Gen-0-Testbau ohne Imports (Prompt).
4. **Mutanten**: 20 handgesetzt, versiegelt vor Lauf 12 (`/root/versiegelt/MUTANTEN-phase2.json`, sha256 `eeb3de60…`), verteilt 9 preise / 7 lager / 2 formeln / 2 bericht, Arten vergleich 6 / rueckgabe 8 / grenze 4 / arithmetik 2. #7 (`rest <= 0` → `< 0` in `rabatt_anwenden`) und #19 (`menge > 0` → `>= 0` in `bewegungsbericht`) sind **äquivalente Mutanten**: bei `rest == 0` liefert der nächste Schritt ebenfalls 0.0, und `Journal` lässt `menge == 0` nicht zu. Kein Test kann sie fangen; das Biotop meldet sie korrekt als blind. Für Fassung 4: Mutanten sollten vor Zählung auf Äquivalenz geprüft werden (oder die Bezugsgröße lautet „von n nicht-äquivalenten").
5. **S2-Kriterium** vor Lauf 12 versiegelt festgelegt (zwei Bedingungen, s. Zeile 3).
6. **Vertragstests** (17) von Hermes aus Anhang A + Docstrings abgeleitet — Philipp/Chat-Claude bestätigen sie bei Vorlage.
7. **Lauf 13 nach Gen 14 beendet** (Sättigung ist Phase 3; 7 von 7 Freigaben unter Vollmacht Abschnitt 4).
8. Proben laufen gegen den jeweils letzten angenommenen Stand und werden mit `nische='probe'`/`status='probe_*'` gekennzeichnet; sie schreiben nie ins Werk.

---

## 7. Kosten

Phase 2 gesamt (Läufe 11–13): **1.190 Aufrufe, 1,905 €** von 10,00 € (19 %). Lauf 13 allein: 704 Aufrufe, 1,145 € — ≈ 0,07–0,09 € je Generation mit 32 Kandidaten. Schwere Aufrufe: 0 (kein statischer Sicherheitsbefund mehr im Werk). Größter Posten: Schwarm schnell/sicher/elegant/wild je ≈ 0,2–0,3 €, Ankläger ≈ 0,3 €. OpenRouter-Konto gesamt seit Phase 1: 4,30 USD. Details `KASSE.md`.

Für Abschnitt 6: die Schätzung „2–8 € je Lauf" für Phase 2 lag zu hoch — gemessen 1,15 € für 14 Generationen mit vier Nischen. Der teuerste Faktor bleibt der schwere Ankläger, der hier nicht anfiel.

---

## 8. Grenzen, offene Punkte, Liste für danach

- **Zeile 9 nur durch die eingeschleuste Probe erfüllt.** Der Schwarm hat in 14 Generationen 4 Verhandlungen ausgelöst und keine bestanden. Ursache: die wild-Kandidaten brachen Verträge, die inhaltlich gelten sollen (z. B. kaufmännische Rundung), und der Nachbar konnte nur „anpassen", indem er den Vertrag selbst umging. Das ist richtig so — aber der Nachweis, dass der Schwarm selbst eine sinnvolle Vertragsänderung durchbringt, steht aus.
- **42 % „KEIN VORSCHLAG"**: elegant und sicher finden an einem Werk mit Kernmaß 0 nichts mehr — erwartbar; die Sättigungsmeldung (Phase 3) würde das ab Gen 6 melden.
- **Bandit-Gewichte trennen nur schwach** (0,03–0,17), weil fast alle Nischen fast nur Misserfolge buchen. Die Buchung zählt „überlebt", nicht „KEIN VORSCHLAG" als neutral — ein ehrliches „nichts gefunden" wird wie ein Fehlschlag gewertet. Für Fassung 4: leere Antworten nicht als Versuch buchen.
- **Gen-0-Testbau ist stochastisch**: Lauf 12 fing #13 (18 von 20), Lauf 13 nicht (17 von 20). Mehr als 2 Versuche je Mutant oder ein zweiter Durchlauf würden helfen; bei 20 Mutanten kostet ein Durchlauf 0,01 €.
- **Ankläger-Tests ohne Vertragsbezug häufen sich als „offen"** (42 Einträge), hauptsächlich Meinungen über `reservierung_einloesen` bei Unterdeckung. Sie kosten je Kandidat einen Kammerlauf. Dedup nach Ort ist da (2,5 %), aber die Norm-Sperre lässt sie im Immunsystem stehen. Für Phase 3: offene Funde nach n Generationen ohne Behebung archivieren.
- **Grenzmaß gegen Ausgang** ließ in Gen 10 einen 5-fachen Laufzeitanstieg gegenüber der Vorgeneration zu (Abschnitt 4). Regelkonform, aber für Fassung 4 zu prüfen.
- **Speicher-Grenzmaß, Kern-Prozesstrennung, tree-sitter**: unverändert Liste für danach. **Entropie/Sättigung, Gedächtnisse, Mentor, Jury, Oberfläche**: Phase 3.

---

## 9. Inhalt dieses Ordners

- `BERICHT.md`, `KASSE.md`
- `ausgaben/` — 80 Dateien + `lauf12-vorlauf/` (28): Katalog & Rauchtest (00–01), Versiegeltes (02), Ausgang (03), Lauf 12 (10–21, 20a), Lauf 13 (40–46, 4gN je Generation + Freigaben), Proben (50–54, 54a), Tor-2-Auswertung (60–65), Übersicht aller Läufe (97), Protokoll vollständig 7.253 Zeilen mit geprüfter Hash-Kette (98), OpenRouter-Gegenprobe (99)
- `werk/` — Ausgang (Lauf 9 Gen 6), gehobenes Werk Lauf 13 Gen 13 mit git-Tags, Lazarus-Archive Gen 0/1/3/5/6/10/11/13
- `biotop/` — Code (Commit 9f78b4c), Datenbank (alle Läufe 1–13), `PRUEFSUMMEN.txt`
- `DATEIEN.txt`, `PRUEFSUMME-ORDNER.txt`

Abholadresse: `https://milieulux-reinigung-muenchen.de/_akte/<schlüssel>/laeufe/biotop-phase-2/` (kein Listing; Einstieg über `BERICHT.md`, `DATEIEN.txt`).
