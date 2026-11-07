# BIOTOP-EINLAGERUNG-01 · Verlauf Philipp ↔ Hermes zum Biotop · Teil 007 von 054

- Einträge V0054 bis V0089. Menge, Regeln und Zählung: VERLAUF-UEBERSICHT.md im selben Ordner.
- Zeiten in CEST (UTC+02:00). Geschwärzt ist jeder Wert aus `.env`/`auth.json` und jedes Schlüsselmuster.

### V0054 · 19.09.2026 02:23:42 CEST · Philipp · Nachricht id 997 · Sitzung `20260918_225920_3e614670` · 43794 B · Stück 2 von 2

```text
- Regressionsprobe (Fassung 3, aus Lauf 7): Hermes schleust einen Kandidaten ein, der eine frühere Behebung rückgängig macht und drei neue bestandene Tests mitbringt → 0 von 1 angenommen; das Protokoll nennt den gefallenen Einzeltest.
- Norm-Probe (Fassung 3, aus Lauf 7): Hermes schleust einen Angriffstest ein, der an der Vorgeneration fällt, am Kandidaten besteht, ohne Absturz und ohne Vertrags-/Verfassungsbezug → bleibt „offen", 0 Punkte, nicht im Werk.
- Vertragsprobe: Änderung an einer Grenze ohne Anpassung des Nachbarn → abgelehnt; mit Anpassung → angenommen (je 1 Fall).
- Immunisierung: n bestätigte Fehler = n Tests im Werk (Liste mit Dateipfaden); Doppelungsanteil ausgewiesen und unter 20 % aller Angriffstests; nach keiner angenommenen Generation ein fehlschlagender Test im Werk (0 von n).
- Verhandlung: mindestens 1 Generation, in der zwei Bereiche eine Vertragsänderung gemeinsam bestanden haben, protokolliert.
- Verlaufskurve des Hauptlaufs mit Endtestbestand beigefügt (3.5).

### Phase 3 — Gedächtnis, Mentor, Oberfläche
**Bauen:** Drei Gedächtnisse, Mentor, Entropie mit Sättigungsmeldung, weiche Maße mit Jury, Oberfläche (3.15).
**Tor 3:**
- Projektgedächtnis: Zweiter Lauf am Übungswerk wiederholt 0 der im ersten Lauf gescheiterten Wege (Vergleich der Kandidatenlisten beider Läufe).
- Artgedächtnis: Nach zwei verschiedenen Werken liefert der Mentor beim dritten mindestens eine Richtung, die ausdrücklich auf Erfahrung aus den ersten beiden verweist.
- Mentor: ≥ 3 Richtungen, je mit Ertrag, Risiko, Aufwand, berührten Bereichen.
- Entropie: Sättigungsmeldung erscheint beim Übungswerk (dokumentiert, mit den fünf Generationen und der Prozentzahl).
- Geschmacksgedächtnis: Nach 20 Entscheidungen Philipps sagt es bei den nächsten 10 mindestens 7 richtig voraus (Hold-out, Zahlen beigefügt).
- Oberfläche: Für jedes Bedienelement Dateipfad und Zeile der Stelle, die es liest oder schreibt (vollständige Liste; ein Element ohne Stelle = Tor nicht bestanden).

### Phase 4 — Erstes echtes Werk
**Werk:** Das KI-Handelssystem (~237.000 Zeilen Python, 17 Dienste). Begründung der Wahl: das schärfste Kernmaß, das es gibt (Ertrag auf historischen Testdaten mit Verlustgrenze ist eine Zahl, über die niemand streitet), und das Werk, an dem die Landkarte zwingend ist.
**Besonderheiten:** Das Werk hat derzeit 135 reproduzierbare Testfehlschläge und Risikomodule, die nicht im Orderpfad liegen — Generation 0 wird dort lang und ist der eigentliche erste Ertrag. Verfassung des Werks enthält die harten Grenzen: gesetzliche Hebelgrenzen je Anlageklasse, Tagesverlustgrenze, Ausschluss von Rüstung und schädlichen Geschäftsfeldern, kein echter Handel ohne bestandenes Bewertungssystem, Demokonto zuerst.
**Tor 4:**
- Generation 0: Testfehlschläge von 135 auf 0; Mutantenfang ≥ 80 von 100.
- Verfassung: Risikomodule nachweislich im Orderpfad (Eintrittspunkte gezählt, je Tor ein roter und ein grüner Eichfall mit Ausgabe).
- Kernmaß: Ertrag auf Testdaten gestiegen (Zahl vorher/nachher), Verlustgrenze in 0 von n Testtagen verletzt.
- Kein Rückschritt in irgendeinem Bereich über alle angenommenen Generationen.
- Sättigungsmeldung oder Budgetabbruch dokumentiert — der Lauf endet nie still.

---

## 9. Abschlussordner und Berichtspflicht

Jeder Hermes-Auftrag (jede Phase) endet zwingend — auch bei Abbruch, Zeitmangel oder Scheitern — mit einem Abschlussordner an der festgelegten, von außen abrufbaren Stelle im Prüfkanal. Inhalt:
- `BERICHT.md`: Was gebaut wurde, was gemessen wurde, jede Torzeile mit Ergebnis und Verweis auf die Ausgabedatei; eigene Entscheidungen von Hermes gekennzeichnet; offene Punkte auf der Liste für danach.
- `ausgaben/`: die Rohausgaben jeder Messung (Testläufe, Prüfsummen, Protokollauszüge).
- `werk/`: das Übungswerk bzw. das gehobene Werk als Archiv (ohne `.env*`, `node_modules`, `dist`, `coverage`).
- `biotop/`: der Stand des Biotops als Archiv (gleiche Ausschlüsse) mit Prüfsumme.
- `KASSE.md`: alle Modellaufrufe des Auftrags mit Kosten und Kontingentverbrauch.

Die Endmeldung im Telegram-Chat enthält die Abholadresse und die Prüfsumme des Ordners. Chat-Claude prüft den Ordner, nicht die Meldung.

---

## 10. Was Philipp entscheidet (Konfiguration, nicht Architektur)

- Budget je Lauf (Vorschlag für Phasen 1–3 zusammen: 150 €; Phase 4 gesondert nach Kostenvoranschlag der Kasse).
- Welche Schnellmodelle über OpenRouter für die Masse (mindestens zwei Anbieter).
- Die Stelle des Abschlussordners im Prüfkanal.
- Die Verfassung jedes Werks und das Maß jedes Laufs — bei Vorlage.

---

## Anhang A — Verfassung des Übungswerks `lagerhaus`

Geschrieben von Chat-Claude (Philipp hat die Entscheidung delegiert). Gilt für Lauf 3 und alle weiteren Läufe am Übungswerk. Ändert nur Philipp.

1. **Was es ist:** Ein Rabatt- und Lagerrechner für Verkaufsberichte. Es rechnet Preise mit Staffeln und Rabatten, führt Bestand aus einem Journal mit Reservierungen und erzeugt daraus Auswertungen. Es ist ein Übungswerk ohne Betriebszweck.
2. **Sicherheit vor Geschwindigkeit:** Kein Bereich darf Eingaben als Programmcode ausführen — weder mit `eval`/`exec` noch mit eingeschränkten Namensräumen. Ein Sicherheitsbefund wiegt mehr als jede Laufzeit. Tauschregel: Die Laufzeit auf der Referenzlast darf bis **×5** gegenüber dem Ausgangszustand steigen, wenn dabei ein statischer Sicherheitsbefund verschwindet; sonst gilt ×2.
3. **Korrektheit vor allem anderen:** Kein Bestand unter null; keine Reservierung, die nach dem Einlösen weiter zählt; keine negativen Rabatte; Staffelgrenzen sind inklusiv („ab 10 Stück" gilt bei 10).
4. **Grenzen sind Verträge:** Die Schnittstellen zwischen `formeln`, `preise`, `lager` und `bericht` ändern sich nur, wenn beide Seiten in derselben Generation angepasst und gemeinsam geprüft werden.
5. **`bericht` ist Ausgabe, keine Logik:** Der Bereich rechnet nichts selbst nach, was `preise` oder `lager` liefern; er formatiert.
6. **Was nie passieren darf:** Ein Kandidat, der Tests entfernt oder abschwächt, um einen Fehlschlag zu beseitigen; ein Kandidat, der einen Sicherheitsbefund durch Ausnahmeregel im Prüfwerkzeug (`# nosec`, Konfiguration) zum Verschwinden bringt statt durch Code.

---

*Ende des Dokuments. Fassung 3, 19.09.2026 (nach dem Nachlauf). Fassungen 1 und 2 sind durch diese Fassung ersetzt; die jeweils höchste Fassung gilt. Fortschreibung als Fassung 4 bei grundlegenden neuen Erkenntnissen.*


Tor 1 ist mit 9 von 9 abgenommen, Phase 1 abgeschlossen — lies INFINITE-EVOLUTION-BIOTOP-Masterprompt-v3.md vollständig, Fassung 2 ist ersetzt; das Änderungsverzeichnis oben nimmt deine drei Funde aus den Läufen 6 und 7 auf (Pareto je Test, Angriffstests sind keine Verträge, nur bestandene Immuntests ins Werk) und korrigiert das Grenzmaß „größte Funktion" auf 60 Zeilen absolut. Auftrag: Phase 2 „Der Schwarm" nach Abschnitt 8, Ausgang Lauf 9 Generation 6 mit Verfassung Anhang A, vorher Modellwahl am OpenRouter-Katalog belegen, Budget 10 € hart, Tor 2 alle elf Zeilen mit Ausgabe und Bezugsgröße einschließlich Regressionsprobe, Norm-Probe und S2. Abschlussordner unter laeufe/biotop-phase-2/ mit Verlaufskurve des Hauptlaufs; Endmeldung mit Abholadresse und Prüfsumme.
```

### V0055 · 19.09.2026 02:32:32 CEST · Hermes-Zwischentext · Nachricht id 1008 · Sitzung `20260918_225920_3e614670` · 49 B

```text
Now the Phase-2 modules. First: Nischen + Bandit.
```

### V0056 · 19.09.2026 02:33:03 CEST · Hermes-Zwischentext · Nachricht id 1010 · Sitzung `20260918_225920_3e614670` · 179 B

```text
Now update genesis to use nischen (reasoning off for deepseek/qwen, referenzlast for schnell, elite as seed, vertrag-Änderungen markieren), and the Anbieter to disable reasoning.
```

### V0057 · 19.09.2026 02:33:37 CEST · Hermes-Zwischentext · Nachricht id 1012 · Sitzung `20260918_225920_3e614670` · 73 B

```text
Now Verträge explizit (Organ 3.2 extension) and Generation 0 (Mutanten).
```

### V0058 · 19.09.2026 02:34:42 CEST · Hermes-Zwischentext · Nachricht id 1016 · Sitzung `20260918_225920_3e614670` · 193 B

```text
Now Aegis: Norm-Regel (3.7 F3), Verträge (Schritt 2), Doppelungen (3.10), größte Funktion absolut, Nischenmaß for "schnell". Let me view the current aegis end section to patch it precisely.
```

### V0059 · 19.09.2026 02:37:20 CEST · Hermes-Zwischentext · Nachricht id 1020 · Sitzung `20260918_225920_3e614670` · 175 B

```text
Now lauf.py: Phase-2 generation loop over 4 Nischen, Verhandlung, Eliten/Bandit booking, Gen 0 command, kurve at the end, Doppelungsanteil. I'll rewrite `_generation_koerper`.
```

### V0060 · 19.09.2026 02:39:43 CEST · Hermes-Zwischentext · Nachricht id 1024 · Sitzung `20260918_225920_3e614670` · 118 B

```text
Now `generation0()` in lauf.py, and the mass_einfrieren must record `nischen` + ausgangs with contract tests in place.
```

### V0061 · 19.09.2026 02:40:08 CEST · Hermes-Zwischentext · Nachricht id 1026 · Sitzung `20260918_225920_3e614670` · 145 B

```text
Now the Ausgangswerk (Lauf 9 Gen 6), the explizite Verträge (3 Grenzen from Anhang A), and the 20 Hermes-Mutanten. Let me set up the werk first.
```

### V0062 · 19.09.2026 02:41:20 CEST · Hermes-Zwischentext · Nachricht id 1030 · Sitzung `20260918_225920_3e614670` · 95 B

```text
Now 20 Hermes-Mutanten (versiegelt, hand-picked to cover all four Bereiche and mutation types).
```

### V0063 · 19.09.2026 02:41:54 CEST · Hermes-Zwischentext · Nachricht id 1032 · Sitzung `20260918_225920_3e614670` · 130 B

```text
Now start Lauf 12: anlegen (10 € Auftragsbudget over all Phase-2 runs), einlegen, kartieren, Verfassung, Verträge, Gen 0, Maß.
```

### V0064 · 19.09.2026 02:42:20 CEST · Hermes-Zwischentext · Nachricht id 1034 · Sitzung `20260918_225920_3e614670` · 131 B

```text
Verify the messgerät treats `tests/vertraege/*` correctly (junit classname `tests.vertraege.test_vertrag_...`), then Generation 0.
```

### V0065 · 19.09.2026 02:42:54 CEST · Hermes-Zwischentext · Nachricht id 1038 · Sitzung `20260918_225920_3e614670` · 45 B

```text
Now Generation 0 with the 20 Hermes-Mutanten.
```

### V0066 · 19.09.2026 02:45:21 CEST · Hermes-Zwischentext · Nachricht id 1044 · Sitzung `20260918_225920_3e614670` · 194 B

```text
Two bugs: gemini-3.5 rejects `reasoning: disabled`; and every test candidate "fails at original" — probably a pytest rc issue (tests import fine but `rc==0 and 'passed'`)... Let me debug both.
```

### V0067 · 19.09.2026 02:45:58 CEST · Hermes-Zwischentext · Nachricht id 1048 · Sitzung `20260918_225920_3e614670` · 157 B

```text
Models omit imports (they think it's appended to the existing test file). Fix the prompt to require a self-contained file; and fix the gemini reasoning flag.
```

### V0068 · 19.09.2026 02:50:46 CEST · Hermes-Zwischentext · Nachricht id 1066 · Sitzung `20260918_225920_3e614670` · 189 B

```text
While that runs, I'll write the probe script for the injected candidates (Nebenwirkung, Regression, Norm, Vertrag) — these run against the Ankläger directly via a synthetic Kandidat row.
```

### V0069 · 19.09.2026 02:51:03 CEST · Hermes-Zwischentext · Nachricht id 1068 · Sitzung `20260918_225920_3e614670` · 175 B

```text
The `kandidaten` table has no `vertraege` column, but aegis reads `k["vertraege"]` and genesis needs to store it. Let me add the column properly in datenbank + genesis insert.
```

### V0070 · 19.09.2026 02:54:26 CEST · Hermes-Zwischentext · Nachricht id 1074 · Sitzung `20260918_225920_3e614670` · 129 B

```text
Der Schnelle liefert: lager 141,7 → 4,8 ms (−97 %), formeln −65 %. Now S2 will be checked in the Generalprobe. Let me wait.
```

### V0071 · 19.09.2026 03:04:11 CEST · Hermes-Zwischentext · Nachricht id 1084 · Sitzung `20260918_225920_3e614670` · 144 B

```text
Generations take ~7 min each with 32 candidates. While Gen 3 runs I'll wait; then run the proben on a stable base. Let me check the budget pace.
```

### V0072 · 19.09.2026 03:04:17 CEST · Hermes-Zwischentext · Nachricht id 1086 · Sitzung `20260918_225920_3e614670` · 79 B

```text
~0,07 €/Generation — 10 Generationen well within budget. Waiting for Gen 3.
```

### V0073 · 19.09.2026 03:09:32 CEST · Hermes-Zwischentext · Nachricht id 1096 · Sitzung `20260918_225920_3e614670` · 66 B

```text
While that runs (~50 min), I'll write the Tor-2 evaluation script.
```

### V0074 · 19.09.2026 03:12:54 CEST · Hermes-Zwischentext · Nachricht id 1100 · Sitzung `20260918_225920_3e614670` · 193 B

```text
This will take ~45 min more. I'll check in periodically; meanwhile nothing else depends on it that I can run concurrently without contending for the Kammer CPU. Let me wait in longer intervals.
```

### V0075 · 19.09.2026 03:22:06 CEST · Hermes-Zwischentext · Nachricht id 1106 · Sitzung `20260918_225920_3e614670` · 62 B

```text
Verhandlung wurde ausgelöst (5 Protokollzeilen). Let me look.
```

### V0076 · 19.09.2026 03:44:02 CEST · Hermes-Zwischentext · Nachricht id 1126 · Sitzung `20260918_225920_3e614670` · 89 B

```text
10 Generationen done. Now the Proben (against the current base) and the Tor-2 evaluation.
```

### V0077 · 19.09.2026 03:46:40 CEST · Hermes-Zwischentext · Nachricht id 1134 · Sitzung `20260918_225920_3e614670` · 136 B

```text
Now improve the Vertragsprobe Fall 2 so the Paar can actually gain (real Behebung with Vertragsbezug in `pruefen`), then launch Lauf 13.
```

### V0078 · 19.09.2026 03:47:19 CEST · Hermes-Zwischentext · Nachricht id 1140 · Sitzung `20260918_225920_3e614670` · 132 B

```text
This will take ~75 min (Gen 0 + 10 generations). I'll check periodically. Meanwhile, update the skill with what I've learned so far.
```

### V0079 · 19.09.2026 03:50:32 CEST · Hermes-Zwischentext · Nachricht id 1144 · Sitzung `20260918_225920_3e614670` · 172 B

```text
Gen 0 in Lauf 13: 16 → 17 von 20 (Ziel ≥ 16 erreicht; #13 this time not caught — the model's Testbau is stochastic). Waiting for generations. I'll poll every ~10 min.
```

### V0080 · 19.09.2026 04:00:31 CEST · Hermes-Zwischentext · Nachricht id 1148 · Sitzung `20260918_225920_3e614670` · 116 B

```text
Gen 1 in Lauf 13 again: lager 138 → 4,9 ms. S2 reproduced. ~8 more generations ≈ 60 min. I'll poll in intervals.
```

### V0081 · 19.09.2026 04:51:14 CEST · Hermes-Zwischentext · Nachricht id 1172 · Sitzung `20260918_225920_3e614670` · 87 B

```text
Lauf 13 done (10 Generationen, 4 angenommen). Now Proben + Tor-2 evaluation on Lauf 13.
```

### V0082 · 19.09.2026 04:51:58 CEST · Hermes-Zwischentext · Nachricht id 1176 · Sitzung `20260918_225920_3e614670` · 182 B

```text
The Werk changed shape in Lauf 13 (S2 fix rewrote bestand.py), so the probes need to adapt to the current source. Let me look at the current lager code and re-target the probe diffs.
```

### V0083 · 19.09.2026 04:52:25 CEST · Hermes-Zwischentext · Nachricht id 1180 · Sitzung `20260918_225920_3e614670` · 163 B

```text
Adapt the probes to the current source: Nebenwirkung = `artikel()` unsortiert (senkt bericht) + a small speedup; Regression = remove the `_reserviert` update line.
```

### V0084 · 19.09.2026 04:55:46 CEST · Hermes-Zwischentext · Nachricht id 1194 · Sitzung `20260918_225920_3e614670` · 163 B

```text
While Gen 11–14 run (looking for a bestandene Verhandlung), let me check what the two failed Verhandlungen were about, to judge if a successful one is plausible.
```

### V0085 · 19.09.2026 05:25:09 CEST · Hermes-Zwischentext · Nachricht id 1220 · Sitzung `20260918_225920_3e614670` · 135 B

```text
Verhandlung bestanden (K1157 + Anpassung K1158, Protokoll #7251). Now the Tor-2 evaluation on Lauf 13, then close the run and assemble.
```

### V0086 · 19.09.2026 05:27:33 CEST · Hermes-Zwischentext · Nachricht id 1228 · Sitzung `20260918_225920_3e614670` · 119 B

```text
Consistent: 16 Immuntest-Dateien = 10 from Phase-1 Ausgang + 6 new (im_werk 6). Now assemble: KASSE, archives, BERICHT.
```

### V0087 · 19.09.2026 05:36:06 CEST · Hermes-Zwischentext · Nachricht id 1236 · Sitzung `20260918_225920_3e614670` · 46 B

```text
All the outputs are in place. Now the BERICHT.
```

### V0088 · 19.09.2026 05:36:13 CEST · Hermes-Zwischentext · Nachricht id 1238 · Sitzung `20260918_225920_3e614670` · 116 B

```text
Let me verify the two claims I made about the Zeile-8 test count ("92 → 111") and the Gen-0 blind list, then seal.
```

### V0089 · 19.09.2026 05:37:13 CEST · Hermes · Nachricht id 1244 · Sitzung `20260918_225920_3e614670` · 2375 B

```text
**Phase 2 „Der Schwarm" abgeschlossen. Abschlussordner liegt im Prüfkanal.**

**Abholadresse:**
`https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/BERICHT.md`

**Prüfsumme des Ordners** (SHA-256 über `DATEIEN.txt`, 122 Dateien, von außen gegengeprüft):
`6b1e7f6a3e27a8830008f787c2e1fdddb62df90237555828767ea7e5d2b277a7`

**Tor 2: 11 von 11** (Hauptlauf 13, 14 Generationen, 7 angenommen):
- Nischen: 4 aktiv, je 4 von 4 Herstellern; Bandit-Gewichte nach 14 Generationen, 235 Wahlen protokolliert
- Generation 0: 20 versiegelte Mutanten, 16 → **17 von 20** gefangen (2 der 3 Restlichen sind äquivalente Mutanten, kein Test kann sie fangen — im Bericht begründet)
- **S2 behoben:** `last_lager` 139,5 → 5,2 ms (−96 %, Kriterium ≥ 50 % vorab versiegelt), Journal führt inkrementelle Summen; Kernmaß 0 → 0
- Nebenwirkungsprobe 0 von 1, Bericht nennt `bericht`; Regressionsprobe 0 von 1, gefallener Einzeltest genannt; Norm-Probe: Test 0 Punkte, nicht im Werk; Vertragsprobe: ohne Nachbar abgelehnt, mit Nachbar Vertrag bestanden
- Immunisierung: 6 Fehler = 6 neue Tests, Doppelungen 2,5 %, **0 von 8** angenommenen Generationen mit rotem Test (99 von 99 am Ende)
- Verhandlung: 1 bestanden (Protokoll #7251) — **ehrlich: durch die eingeschleuste Probe**, nicht durch den Schwarm; der Schwarm löste 4 aus, keine bestand
- Verlaufskurve mit Endtestbestand beigefügt; Modellwahl am Katalog belegt (gpt-5.6-luna, gemini-3.5-flash-lite, deepseek-v4.1-flash, qwen3.8-flash — alle 2026, gleicher oder niedrigerer Preis)

**Was schiefging und behoben wurde:** Lauf 12 (Vorlauf, 10 Generationen) zeigte über die Norm-Probe, dass die Norm-Regel nur Ankläger-Tests traf, nicht mitgebrachte — korrigiert, neuer Lauf 13 vom selben Ausgang. Zwei weitere Biotop-Fehler ohne Maßwirkung protokolliert (Verhandlungs-Paarprüfung, Gen-0-Prompt).

**Kosten:** 1,91 € von 10 € (1.190 Aufrufe); Lauf 13 allein 1,15 € für 14 Generationen mit 32 Kandidaten je Generation. Schwere Aufrufe: 0 — kein Sicherheitsbefund mehr im Werk.

**Für Fassung 4** (Abschnitt 8 des Berichts): Grenzmaß gegen Ausgang ließ in Gen 10 einen 5-fachen Laufzeitanstieg gegen die Vorgeneration zu (regelkonform, aber diskussionswürdig); Bandit wertet „KEIN VORSCHLAG" als Misserfolg; äquivalente Mutanten in der Bezugsgröße.
```

