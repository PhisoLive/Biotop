# BIOTOP-LAGE-01 · Fassung 2 · `ENTSCHEIDUNGEN-TEIL1-01.md`

- **Inhalt:** FK15–FK19, FK21 · Entwurf A, Stück 1 von 4
- **Stichzeitpunkt:** 25.09.2026 17:29:59 CEST (Ende des Baus S1c). Der Entwurf beschreibt den Stand zur Zeit seines Lesens; was sich bis zum Stich geändert hat, steht im Nachtrag unten.
- **Verfasser:** Subagent Teil A, Arbeitszeit 25.09.2026 16:10:47–17:47:01 CEST (Delegationsbuch, R193). Eingesetzt von Hermes.
- **Quelle:** `/root/sicherung/biotop-lage-01/entwurf/entscheidungen/ENTSCHEIDUNGEN-TEIL1.md` · 27229 B · SHA-256 `110ce77fbce04429f253b3e60b8fac37992ef5d2e40185f07bb300ee575f1278`. Änderungen beim Einsetzen: nur dieser Kopf und `{LAEUFE}` → `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe` (9 Stellen).
- **Prüfung durch Hermes und Rohbelege je Datei:** https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-lage-01/VOLLSTAENDIGKEIT-TEIL1-01.md
- **Nachtrag Hermes:** Endstand zum Stichzeitpunkt 25.09.2026 17:29:59 CEST: Der Bau S1c der Behebungsrunde 6 endete an seiner Grenze von 250 Werkzeugaufrufen, mit Schlussbericht (R175). Runde 6 ist damit nicht abgeschlossen. Seit Commit `0c2f058` gibt es keinen neuen Commit; nicht eingecheckt sind 25 Einträge (R191). Ein Review fehlt. S1c meldet einen neuen stillen Durchlass (Befund G) und hat 10 rote Tests `test_w_g_*` im Baum gelassen (R170). T4 ist nicht frei. **Nachrichten Philipps zum Stich:** 114 mit Text, davon 44 ab dem 21.09. (START-02 Abschnitt C, R160). Nennt ein Entwurf „114, davon 43 ab 21.09.“, so zählt er nach dem Verzeichnis v2, das bis 16:41:36 reicht. Diese 114 sind 113 Nachrichten mit Text plus die Zeile id 7468 ohne Text (R198). Neu bis zum Stich ist nur die Nachsteuerung (id 24300, 17:08:20). Einzelheiten zum Endstand stehen in LAGE-TEIL1-01.md.

---
# ENTSCHEIDUNGEN — Teil 1 von 4: FK15 (Fassungsverzeichnis)

Offenlegung BIOTOP-LAGE-01 Fassung 2 · Entwurfsteil A · geschrieben im Namen von Hermes (HERMES-1) von einem Subagenten.
**Stand des Lesens:** 25.09.2026, 16:10–17:30 CEST. Der Stichzeitpunkt steht noch nicht fest; den Endstand von S1c und Runde 6 trägt Hermes nach.

- **Teil 1:** FK15 · **Teil 2:** FK16, FK17 · **Teil 3:** FK18 · **Teil 4:** FK19, FK21, Lücken, Widersprüche.
- **Quellen:** unter `/root/sicherung/biotop-lage-01/`: Rohbelege `rohbelege/R00nn.txt` (hier „R<n>“), `arbeit/dokumente/`, `arbeit/fassungen/`, `arbeit/lesen/`, `arbeit/verlauf/v2/`. Adressen im Prüfkanal stehen als `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/…`.
- **Kennzeichnung:** Zahlen sind *abgelesen*, außer sie sind als *gerechnet* markiert. Eigene Wertungen stehen nur als „Auslegung Hermes“.
- **Absender:** Nach der Berichtigung durch Hermes (R84, R85, R88, R89) gilt `arbeit/verlauf/v2/nachrichten.jsonl`. Philipp hat ab 18.09. **114** Nachrichten zum Biotop geschickt (abgelesen: 114 Zeilen mit `"absender": "Philipp", "biotop": "ja"`). Die 6 Einträge 655, 657, 1959, 3559, 16285 und 16712 in `arbeit/lesen/philipp-ab-2026-09-18.md` stammen nicht von Philipp und werden in keinem Teil als seine Entscheidung geführt.

---

## FK15 — Fassungsverzeichnis v1 bis v8

**Frage:** Fassungsverzeichnis von v1 bis zur gültigen. Je Fassung Datum, Pfad, SHA-256 und das Änderungsverzeichnis im Wortlaut.

### 15.1 Eingang, Stand-Zeile, Umfang

- **Original** jeder Fassung ist die Nachricht in der Sitzungsdatenbank `/root/.hermes/state.db` (Tabelle `messages`, Nachrichten-id laut R15 Z. 72–90).
- **Arbeitskopie** jeder Fassung liegt unter `arbeit/dokumente/<Eingang>_INFINITE-EVOLUTION-BIOTOP-Masterprompt-vN.md`, ohne abschließenden Zeilenumbruch (R17 Z. 10–12).

| Fassung | Eingang (CEST) | Nachrichten-id | Sitzung | „Stand:“-Zeile (R30 Z. 69–76) | Bytes | Zeilen |
|---|---|---|---|---|---|---|
| v1 | 18.09.2026 20:59:08 | 629 | 20260918_205818_3767d1c9 | Stand: 18.09.2026 · Fassung 1 | 28.754 | 289 |
| v2 | 19.09.2026 00:36:30 | 831 | 20260918_225920_3e614670 | Stand: 19.09.2026 · Fassung 2 | 37.835 | 331 |
| v3 | 19.09.2026 02:23:42 | 997 | 20260918_225920_3e614670 | Stand: 19.09.2026 (nach dem Nachlauf) · Fassung 3 | 43.497 | 347 |
| v4 | 19.09.2026 12:39:25 | 1393 | 20260918_225920_3e614670 | Stand: 19.09.2026 (nach Phase 2) · Fassung 4 | 53.416 | 374 |
| v5 | 19.09.2026 19:35:53 | 2232 | 20260918_225920_3e614670 | Stand: 19.09.2026 (nach Phase 3) · Fassung 5 | 64.873 | 406 |
| v6 | 20.09.2026 00:18:44 | 2718 | 20260918_225920_3e614670 | Stand: 19.09.2026 (nach dem Nachlauf zu Phase 3) · Fassung 6 | 78.968 | 470 |
| v7 | 21.09.2026 02:14:34 | 9105 | 20260921_015554_e79a4a0f | Stand: 21.09.2026 · Fassung 7 | 85.728 | 512 |
| v8 | 23.09.2026 15:53:53 | 13998 | 20260921_015554_e79a4a0f | Stand: 23.09.2026 · Fassung 8 | 94.876 | 551 |

- Jede Stand-Zeile geht weiter mit „· Auftraggeber: Philipp Zöllisch · Prüfer: Chat-Claude“ (R30 Z. 69–76).
- Eingang, id und Bytes stammen aus R15, die Zeilen aus R17.
- **v8 ist die jüngste Fassung.** Eine spätere Fassung gibt es nicht; siehe 15.5.
- Bei v6 liegt das Datum der Stand-Zeile (19.09.) einen Tag vor dem Eingang (20.09. 00:18:44). Auslegung Hermes: Die Stand-Zeile gibt den Inhaltsstand an, nicht den Versand.

### 15.2 SHA-256

Werte aus R17 Z. 62–197. Der Wert „ohne Zeilenumbruch“ ist derselbe wie in R15, also der SHA-256 des Wortlauts in state.db. Er gilt auch für die Arbeitskopie in `arbeit/dokumente/`. Der Wert „mit Zeilenumbruch“ gilt für die Plattenkopien, soweit es welche gibt (15.3).

| Fassung | SHA-256 ohne abschließenden Zeilenumbruch (Original, Arbeitskopie) | SHA-256 mit abschließendem Zeilenumbruch (Plattenkopien) |
|---|---|---|
| v1 | `93d358cdda6473f91fda795392e509212f75f1f9678bef31593cad9104fe1ea8` | `a7a949d24dab5c5b42c7a7d93f244a898eb88bd3007ec8cee19481cb46193959` |
| v2 | `acc42ad73f6111a3922993aaadb94ebb12aaeeb995f445f3fe7e8abaab1b4b9d` | `5e5a3e5766b4eafbc02e51411fb236f772f97729dee6915275ecb5d70029a588` |
| v3 | `ca74ed53c33fd68f1ce1a5b172262197a173c118b1099a991a7dac0f350373a2` | `e8657bca0ac35ecd3ac1b74e811757a5292a772410d519f412846b8cd0989863` |
| v4 | `ff1cda438d09c1b440d32700d1723b8e8df0daf6f45a7e2251372e035042e886` | `612f5e53969a3f6efd030555185385756eb82bf9e30f60b1d430777334d230ed` |
| v5 | `a34d7e1ad4532fc1ea11fb805b3ef56d2ec09b0b1febad3dc3af1854f9f5035e` | `df4709b0d2d6f3808e71f2ca284c16682eb18bfb061803aa77cfd2c87eef6422` |
| v6 | `3f63dec2a7d6f82e932699907dab42d71148fe84ba907a13c505fa2c010bd483` | `effefeec0fe2ea0621d4fdca0f27bdd3dae981fd289f1e0b5d56da5aca81aefd` |
| v7 | `0d3a07327b05da232adc49d56cf98e1369f04693c9e857b9e8199d558d38c6c1` | `a3b3ac0c17371306b027591110f528018f62d5c2feb4ad82dc21823f14bd76ed` |
| v8 | `4168a35ede38c31fe4fad21844105a148da5b5aa0d69d2672f29b774b7a67cc9` | `0c7961e1d2b7eeeb7a6982e419905c54e93a9b12bfa5bea7e6326c0ef58a5d94` |

### 15.3 Kopien außerhalb der Sitzungsdatenbank

- **v1 bis v5: keine Plattenkopie gefunden.**
  - R17 gleicht nur die Kopien ab, die R11 gefunden hat; das sind die zu v6 und v7.
  - Eigene Suche am 25.09. um etwa 17:05 CEST mit `search_files` unter `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe`, Muster `^Stand: 1[89]\.09\.2026.{0,45}Fassung [1-5] · Auftraggeber`: 0 Dateien.
  - Außerhalb des Prüfkanals ist für v1 bis v5 nicht gesucht → **UNBEKANNT**. Weg zur Klärung: dieselbe Suche über `/root` und `/tmp`, nach Ende von S1c.
- **v6: 4 Plattenkopien.** Jede hat 78.969 Bytes und den SHA-256 `effefeec…`, ist also das Original mit abschließendem Zeilenumbruch (R17 Z. 141–144):
  - `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6-01.md` (geändert 20.09. 05:01:44 CEST, R79 Z. 90)
  - `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/quellen/MASTERPROMPT-FASSUNG-6.md`
  - `/root/phase-4-vorbedingung-1/uebergabe-quellen/MASTERPROMPT-FASSUNG-6.md`
  - `/tmp/biotop-phase4-lektuere-mm6_llag/Masterprompt-v6.md`
- **v7: 1 Plattenkopie**, `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-t3-typescript/MASTERPROMPT-v7.md`. Sie hat 85.729 Bytes und den SHA-256 `a3b3ac0c…`, ist also das Original mit Zeilenumbruch (R17 Z. 180). Geändert am 21.09. um 02:24:28 CEST (R79 Z. 88).
- **v8: keine vollständige Kopie außerhalb der Sitzungsdatenbank.**
  - Die Stand-Zeile „Stand: 23.09.2026 · Fassung 8“ steht in 0 Dateien unter `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe`, `/root/biotop-vor-t4*`, `/root/biotop-t3` und `/root/.hermes/cache` (R53 Abschnitt 4).
  - Es gibt nur einen Auszug `MASTERPROMPT-V8-TOR4.txt`, in `/root/biotop-vor-t4-05/bau/` und in `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-vor-t4-05/`. Er hat 8.912 Bytes und den SHA-256 `888ab89a27871f31f099aee733f57f42af0789975b92c6272fa2979c0732067e`. Seine erste Zeile ist „Quelle: messages / content“. Von 49 nichtleeren Zeilen stehen 48 wörtlich in v8 (R53; R79 Z. 89).
  - Laut `/root/biotop-vor-t4-05/REVIEW-AUFTRAG.md` Z. 38–39 wurde der Auszug „aus der Sitzungsdatenbank gelesen; die frühere Cache-Datei existiert nicht mehr“. → Lücke L-1.
- **Bytezahlen der Lesefassung:** `arbeit/lesen/philipp-ab-2026-09-18.md` nennt für v7 86.026 Bytes (Z. 368) und für v8 95.174 Bytes (Z. 440). R15 und R17 nennen 85.728 und 94.876. Die Lesefassung liegt also je 298 Bytes höher (*gerechnet*). Die Ursache ist nicht geprüft. Auslegung Hermes: Die Lesefassung zählt die Hülle der Dokumentnachricht mit. → Widerspruch W-1.

### 15.4 Bruchstücke vom 19.09.2026 14:01:46 (keine Fassungen)

Beide Dateien stammen aus der Nachricht id 1892 in der Sitzung 20260918_225920_3e614670 (R15 Z. 76–77):

| Datei in `arbeit/dokumente/` | Bytes | Zeilen | SHA-256 ohne Zeilenumbruch | SHA-256 mit Zeilenumbruch |
|---|---|---|---|---|
| `2026-09-19_140146_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v1.md` | 4.672 | 52 | `9f931fca28205438d9e2557a6be48b708a4af7d3c0747c04b4ae3cfeacfc84f9` | `98b61d826f770a383b7c6d5a8b6efe3f34de7c3c3bb3d2774de468d2a024a764` |
| `2026-09-19_140146_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v4.md` | 1.500 | 12 | `31ebecd20f1776ff8cdf321ea996c0f6c57ab3e26c126b57fa155aed886153ed` | `fe2bc422c2c0d06a8cb56331b0c03e17e7482af3b719f8b6e345f46ed7d625f8` |

Belege aus R53 Abschnitt 1, dass es Bruchstücke sind:
- **Jede Zeile beginnt mit „> “.** Beide Dateien sind also Zitate.
- **v1-Bruchstück:** 0 von 49 nichtleeren Zeilen stehen wörtlich in der vollen v1. Nach Abschnitt 3 bricht es mit „…[truncated]“ ab. Danach folgt Text einer Verlaufsverdichtung, etwa „The 343 compacted message(s) remain fully preserved …“ und „You've reached the maximum number of tool-calling iterations allowed …“.
- **v4-Bruchstück:** 3 von 11 nichtleeren Zeilen stehen wörtlich in der vollen v4. Es enthält den Kopf und die ersten vier Punkte des Änderungsverzeichnisses, gekürzt.
- **Zeitstempel:** Die id 1892 liegt zwischen den ids 1750 (16:04:33) und 1959 (16:39:00), trägt aber die Zeit 14:01:46 (Kopfzeilen der Lesefassung, R15). Auslegung Hermes: Die Nachricht wurde bei einer Verdichtung nachträglich eingefügt.

### 15.5 Verweise auf fehlende Fassungen

- **Suche (R53 Abschnitt 3)** in 3.626 Dateien:
  - `arbeit/lesen/*.md`,
  - Berichte unter `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-*/` und `https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/` (`*.md`, `*.txt`, je < 2 MB),
  - `/root/biotop-vor-t4*/` (`*.md`).
- **Muster:** „Fassung 9“ bis „Fassung 19“, „Masterprompt … v9“ bis „v19“ und Buchstabenfassungen wie „Fassung 7b“ oder „v7b“.
- **Ergebnis:** 0 Treffer je Muster. Kein Bericht und keine Nachricht verweist auf eine Fassung, die fehlt.
- **Verwandter Fund, keine fehlende Fassung:**
  - `REGELN-01.md` Z. 5 (20.09.) sagt: „Die vollständige Sammlung steht im Änderungsverzeichnis Fassung 7.“ Gemeint ist die Liste in `arbeit/dokumente/2026-09-20_045016_ABNAHME_Vorbedingung-1_2026-09-20.md` §7 „Änderungsverzeichnis für Fassung 7“ (Z. 115).
  - Das Änderungsverzeichnis der tatsächlichen v7 (21.09.) enthält diese Sammlung nicht (15.6).
  - → FK18, Widerspruch W-2.

### 15.6 Änderungsverzeichnisse im Wortlaut

- **v1 hat kein Änderungsverzeichnis.** `arbeit/fassungen/aenderungen-v1.md` hat 1 Byte. R30 Z. 69 sagt für v1: „Kopf 174 Zeichen, Blöcke 0, eigenes Verzeichnis 0 Zeichen“.
- **Spätere Fassungen enthalten die früheren Verzeichnisse wörtlich** (R53 Abschnitt 2): Von v2 bis v6 steht jede Zeile in jeder späteren Fassung. Vom Verzeichnis v7 stehen 6 von 7 Zeilen in v8. v8 Z. 13 ändert die Kopfzeile zu „**Änderungen gegenüber Fassung 7 — Ende. Änderungen gegenüber Fassung 6** (aus der Abnahme …“.
- **Die Blöcke unten** sind wörtlich aus `arbeit/fassungen/aenderungen-vN.md` übernommen, per Skript eingesetzt und gegengeprüft (R146: je Datei alle nichtleeren Zeilen, etwa v5 14 von 14).

#### v1 — eingegangen 18.09.2026 20:59:08 CEST · Quelle `arbeit/fassungen/aenderungen-v1.md` (1 Bytes)

Kein Änderungsverzeichnis: Die Datei enthält kein Zeichen außer dem Zeilenumbruch (R53 §2); R30 Z. 69: „Kopf 174 Zeichen, Blöcke 0, eigenes Verzeichnis 0 Zeichen“.

#### v2 — eingegangen 19.09.2026 00:36:30 CEST · Quelle `arbeit/fassungen/aenderungen-v2.md` (1185 Bytes)

> **Änderungen gegenüber Fassung 1** (aus der Prüfung des Abschlussordners Phase 1, Lauf 2):
> - 3.5: Kernmaß-Formel festgelegt — bestandene Tests zählen nicht, nur Fehlschläge zählen negativ, paarweise Messung; Grenzmaße statt Punkte für Leistung; „behoben heißt verschwunden" für Sicherheitsbefunde. Grund: In Lauf 2 stammten 10 von 12 Punkten Zuwachs aus hinzugefügten Tests, und eine Scheinlösung (`__builtins__` leeren vor `eval`) wurde als Behebung angenommen.
> - 3.3: Verfassung auch für Übungswerke; Verfassung des Übungswerks `lagerhaus` im Anhang A.
> - 3.6: Neuschreibungsregel für kleine Dateien gelockert (Kandidat K35 wurde zu Unrecht verworfen).
> - 3.7: Ankläger erhält bei Sicherheitsbefunden die Befundklasse und muss deren bekannte Umgehungen angreifen.
> - 4: Vollmacht für Übungswerke (Freigaben durch Hermes mit Protokoll; echte Werke nur durch Philipp).
> - 6: Kostenschätzung korrigiert — gemessen 0,40 € statt geschätzt 20–60 € für das Übungswerk.
> - 8, Phase 1: Tor-Zeile 2 präzisiert; Nachlauf (Lauf 3) als Bedingung für Phase 2 aufgenommen. Wertung Lauf 2 durch Chat-Claude: 7 von 9 Zeilen, nicht 8 von 9 — S1 nicht behoben.
>
> ---

#### v3 — eingegangen 19.09.2026 02:23:42 CEST · Quelle `arbeit/fassungen/aenderungen-v3.md` (1847 Bytes)

> **Änderungen gegenüber Fassung 2** (aus der Prüfung des Abschlussordners Phase 1 Nachlauf, Läufe 6–10):
> - 3.5: Pareto **je Test** statt je Zahl — ein Test, der an der Vorgeneration besteht und am Kandidaten fällt, tötet den Kandidaten unabhängig von jeder Summe. Grund: Lauf 7 nahm einen Kandidaten an, der eine Behebung rückgängig machte, weil drei neue Tests eine Regression aufwogen. Fehler von Chat-Claude in Fassung 2 (dort als Summe formuliert).
> - 3.5: Grenzmaß „größte Funktion" absolut (Vorgabe 60 Zeilen) statt relativ +25 %. Grund: 11 von 35 Ablehnungen in Lauf 9 trafen Kandidaten, die zwei Zeilen Fehlerprüfung ergänzten. Fehler von Chat-Claude in Fassung 2.
> - 3.7: Ein Angriffstest zählt als Nachweis einer Behebung nur, wenn die Vorgeneration dabei abstürzt oder Vertrag/Verfassung ihr Verhalten als falsch ausweisen; sonst bleibt er offen und bringt 0. Grund: Lauf 7, zweite Ursache — Ankläger-Tests schrieben das Fehlverhalten des Kandidaten als Norm fest.
> - 3.10: Ins Werk kommen nur Immuntests, die der angenommene Kandidat besteht; offene Funde bleiben im Immunsystem und werden späteren Kandidaten paarweise vorgelegt. Grund: Lauf 6 endete mit 19 von 95 Tests rot. Dazu Doppelungsregel.
> - 3.5: Verlaufskurve mit Endtestbestand ist Pflichtbestandteil jedes Abschlussordners, nicht nur für Lauf 2.
> - 6: Nachlauf gemessen 1,79 € (542 Aufrufe); schwere Ankläger-Aufrufe 5 % der Aufrufe, 36 % der Kosten.
> - 8, Phase 1: **bestanden, 9 von 9** (Lauf 9, 19.09.2026, 02:20). Phase 2 freigegeben; Tor 2 um Regressionsprobe, Norm-Probe, S2 und Doppelungsanteil ergänzt; Budget 10 €.
> - 10: Hermes prüft vor Phase 2 den OpenRouter-Katalog auf aktuellere Schnellmodelle gleicher Hersteller zu gleichem oder niedrigerem Preis (Vorentscheidung Chat-Claude; die in Phase 1 genutzten Modelle stammen aus 2025).

#### v4 — eingegangen 19.09.2026 12:39:25 CEST · Quelle `arbeit/fassungen/aenderungen-v4.md` (2952 Bytes)

> **Änderungen gegenüber Fassung 3** (aus der Prüfung des Abschlussordners Phase 2, Läufe 11–13):
> - 3.5: Grenzmaße messen gegen den **Bestwert des Laufs** (beste angenommene Generation je Maß), nicht gegen den Laufausgang; ohne Kernmaßgewinn nur Rauschtoleranz +15 %, mit Kernmaßgewinn Tauschregel (Vorgabe ×2). Grund: Gen 10 hob `formeln` gegenüber der Vorgeneration um ×5 und `preise` um ×3, regelkonform gegen den Ausgang. Fehler von Chat-Claude in Fassung 2/3.
> - 3.5: Generation 0 — äquivalente Mutanten werden vor der Zählung mit Beleg aussortiert; Bezugsgröße „von n nicht-äquivalenten"; zwei Testbau-Durchläufe je blindem Mutanten. Grund: 2 von 3 ungefangenen Mutanten in Lauf 13 waren beweisbar äquivalent; der Testbau ist stochastisch (Lauf 12 fing 18, Lauf 13 17).
> - 3.6: „KEIN VORSCHLAG" ist für die Bandit-Gewichtung neutral, kein Misserfolg. Grund: Ein ehrliches „nichts gefunden" wurde wie ein Fehlschlag gebucht — das züchtet Scheinvorschläge.
> - 3.7: Norm-Regel gilt für **alle** Tests, die mit einem Kandidaten neu ins Spiel kommen (Ankläger-Tests und mitgebrachte Tests); Vertrags-/Verfassungsbezug nur durch expliziten Verweis (Vertragstest-Kennung oder Verfassungssatz-Nummer), nicht durch Wortüberdeckung. Grund: Lauf 12 zeigte die Lücke bei mitgebrachten Tests (Fehler von Chat-Claude in Fassung 3, zu eng formuliert); Wortüberdeckung ist manipulierbar.
> - 3.10: Offene Funde werden nach 5 Generationen ohne Behebung archiviert (nicht gelöscht) und nicht mehr vorgelegt. Grund: 42 offene Ankläger-Meinungen kosteten je Kandidat einen Kammerlauf.
> - 2, Satz 2 und 5: Jede Änderung am Messgerät während eines Laufs ist ein neuer Lauf — ohne Ermessen darüber, ob sie „Maßwirkung" hat. Grund: Zwei Korrekturen während Lauf 13 „ohne Maßwirkung", beurteilt vom Ausführenden.
> - 9: Die Kandidatenaufschlüsselung eines Laufs muss auf die Gesamtzahl aufgehen; ein Bericht mit offener Differenz ist unvollständig. Grund: Lauf 13 wies 470 Kandidaten aus, die Zerlegung ergibt 469.
> - 8, Phase 2: Wertung Chat-Claude **10 von 11** — Zeile 7 (Vertragsprobe „→ angenommen") nicht erfüllt: das Probenpaar bestand die Vertragsprüfung, brachte aber 0 Kernmaß und kam nie ins Werk; „angenommen" wurde zu „bestanden" umgedeutet. Zeile präzisiert (Probe mit Kernmaßgewinn), Nachprobe als Vorbedingung von Phase 3. Zeile 9 erfüllt wie geschrieben, aber von Chat-Claude falsch geschrieben — der gemeinte Nachweis (Schwarm bringt selbst eine Vertragsänderung durch) steht in Tor 4.
> - 8, Phase 3: Tor 3 überarbeitet — zweites Übungswerk für das Artgedächtnis; Geschmacksgedächtnis mechanisch mit versiegelter Regel geprüft (Philipps echte Entscheidungen erst ab Phase 4); Oberfläche als Web-Oberfläche mit Anmeldung; Sättigungsmeldung am gesättigten `lagerhaus` messbar; Budget 15 €.
> - 6: Phase 2 gemessen 1,91 € (Schätzung 2–8 € war zu hoch); Phase-3-Schätzung.

#### v5 — eingegangen 19.09.2026 19:35:53 CEST · Quelle `arbeit/fassungen/aenderungen-v5.md` (3519 Bytes)

> **Änderungen gegenüber Fassung 4** (aus der Prüfung des Abschlussordners Phase 3, Läufe 14–20):
> - 3.12: Das **Artgedächtnis speichert Muster, keine Instanzen**. Zu jeder angenommenen Generation schreibt ein zusätzlicher Aufruf den abstrahierten Satz ohne Werk-, Datei- oder Funktionsnamen; nur diese Sätze werden werkübergreifend vorgelegt. Grund: 0 werkübergreifende Verweise bei 12 Richtungen in drei Läufen — das Modell übergeht zu Recht Sätze, die an seinem Werk nicht gelten. Die Torzeile bleibt unverändert; erzwungene Verweise wären Scheinbegründungen.
> - 3.10: **Doppelungsschlüssel ist die Behauptung** (Ziel-Funktion + Zusicherung), nicht (Meldungsklasse, Ort). Der Anteil wird gegen die **erzeugten Angriffstests** ausgewiesen, nicht gegen Ablehnungen. Grund: Sechs Tests derselben Behauptung kamen einzeln ins Immunsystem und hielten einen Fehler am Leben; gemeldet waren 2,5 %, bei richtiger Bezugsgröße 10,9 %, bei der gemeinten Lesart 83,6 %.
> - 3.5: **Rauschtoleranz wird gemessen, nicht gesetzt.** Vor jedem Lauf fünf Messungen am unveränderten Ausgang je Bereich; Toleranz = gemessene Spannweite + 10 Prozentpunkte, mindestens 15 %. Laufzeiten werden als Median aus drei Durchläufen gemessen. Grund: feste 15 % gegen 47 % Eigenrauschen bei `formeln` — Kandidaten starben an Rauschen. Fehler von Chat-Claude in Fassung 4.
> - 3.12: **Gescheiterte Wege aus verworfenen Läufen zählen nicht** im Projektgedächtnis; es verwirft Kandidaten ohne Kammerlauf und ist damit Teil des Messgeräts. Grund: Lauf 18 begründete 12 von 13 Verwerfungen mit Lauf 16, dessen Ankläger als falsch erkannt war.
> - 3.10: **Fund-Übernahme zwischen Läufen wiederholt die Norm-Prüfung mechanisch** (jeder offene Fund wird am neuen Ausgang in der Kammer nachgemessen), statt den alten Status zu übernehmen. Grund: sechs Normtests standen nach der Übernahme als Funde im Testbestand.
> - 3.7: Pareto je Test gilt für Tests im Werk, Verträge und Verfassung; ein **neuer** Angriffstest, der an der Vorgeneration besteht und am Kandidaten fällt, tötet nur bei Absturz des Kandidaten oder bei explizitem Vertrags-/Verfassungsverweis — sonst offen, 0 Punkte, kein Kill. Grund: Lauf 16, der Ankläger schrieb den Fehler als Norm fest und tötete jede Behebung.
> - 2, Satz 5 und 4: **Abbrüche nach Satz 2 sind vom Freigabe-Gate ausgenommen** — immer erlaubt, protokolliert. Grund: Hermes konnte Lauf 16 nicht stoppen und er lief weiter.
> - 3.5: **Generation minus eins — Messgerät-Eichung vor jedem Lauf.** Nebenwirkungs-, Regressions-, Norm- und Vertragsprobe laufen als Vorspann jedes Laufs, nicht nur einmal als Abnahme. Grund: fünf von sieben Läufen in Phase 3 starben, weil das Messgerät erst im Lauf als kaputt auffiel; Kosten 1,41 € von 2,83 €.
> - 9: **Zwischenbericht-Pflicht** — vor jedem Sitzungsende `ZWISCHENBERICHT.md` und `DATEIEN.txt` im Ordner; ein Ordner ohne Bericht gilt als nicht abgeliefert. Endmeldungen nennen die vollständige Abholadresse als ganze URL.
> - 4: **Richtungswahl unter Vollmacht** bei Übungswerken (protokolliert); bei Werken mit Betriebszweck wählt Philipp.
> - 8, Phase 2: Zeile 8 **rückwirkend gerissen** (Doppelungsanteil 83,6 % gegen Grenze 20 %) — Wertung **9 von 11**. Gebaut bleibt gebaut; die Zahl wird nicht verhandelt.
> - 8, Phase 3: Wertung Chat-Claude **7 von 11** (in Übereinstimmung mit Hermes). Torzeilen für Jury und Archivierung umformuliert, Artgedächtnis-Zeile unverändert.
> - 6: Phase 3 gemessen 2,83 €; Phase-4-Schätzung.

#### v6 — eingegangen 20.09.2026 00:18:44 CEST · Quelle `arbeit/fassungen/aenderungen-v6.md` (2624 Bytes)

> **Änderungen gegenüber Fassung 5** (aus der Prüfung des Abschlussordners Phase-3-Nachlauf, Läufe 21–23):
> - **Abschnitt 2a neu: sechs Grundsätze**, die aus wiederkehrenden Fehlerklassen gefasst wurden. Sie stehen vor den Organen, weil jeder von ihnen an mehr als einer Stelle greift.
> - 3.7: Der **Ankläger nennt seine Behauptung vorab**; ist sie im Bereich schon aufgestellt, wird der Angriff gar nicht erst ausgeführt. Grund: Die bloße Anweisung, eine andere zu finden, senkte die größte Gruppe von 5 auf 1, aber nicht den Anteil unter 20 % — und **0 Aufrufe** antworteten mit „KEIN ANGRIFF", obwohl das ausdrücklich erlaubt ist. Die Rolle des Gegners erzeugt Zwangsbefunde; die Entscheidung wird dem Modell abgenommen, statt sie ihm anzutragen. Spart zusätzlich Aufrufe.
> - 3.12: Der werkübergreifende Block des Artgedächtnisses bekommt einen **festen Mindestanteil an der Vorlage** (Vorgabe: die Hälfte der gezeigten Einträge, mindestens fünf, sofern vorhanden). Grund: Ein `logmuehle`-Lauf sah 13 fremde Muster und lieferte 2 von 5 Verweisen, ein `lagerhaus`-Lauf sah 3 und lieferte 0 — bei 17 Diensten verdrängt die Masse eigener Einträge fremde Muster allein durch Menge.
> - 3.5: **Generation minus eins** ist vollständig beschrieben (Rauschmessung mit Ausreißerbehandlung, bereichsweise Sperre, Serienzähler mit Zeitraum-Deutung, die vier Proben am versiegelten Eichgegenstand, Fund-Neubewertung). Gemessene Kosten: 9 Kammerläufe, 4 Modellaufrufe, 0,0057 €, 44 s je Lauf.
> - 3.5 neu: **Versiegelter Eichgegenstand** je Werk — ein Bereichspaar mit Vertrag, beim ersten Lauf gewählt, danach unverändert; bei Werken mit Betriebszweck muss der tragende Pfad ausdrücklich in den Regeln stehen, sonst wartet das Organ.
> - 3.10: **Probensperre für alle drei Gedächtnisse**, erkannt am gesetzten Merkmal `ist_probe`, nicht am Namen.
> - 8, Phase 3: Wertung **auf 8 von 11 korrigiert** — die Torzeile Projektgedächtnis ist erfüllt, nicht „teilweise": 0 von 3 strittigen Fällen sind durchgerutschte Wiederholungen; Hermes' Nachrechnung maß Token statt Ziele und hatte den Filter für verworfene Läufe nicht angewandt. Die Zahl des Organs war richtig.
> - 8, Phase 2: Zeilen Nebenwirkung, Regression, Norm, Vertrag **wieder belegt** (4 von 4 mit gehärteten Proben); Zeile 8 bleibt gerissen, Zahl berichtigt auf 68,5 % (gemessen statt geschätzt).
> - Anhang B neu: **Verfassung des Übungswerks `logmuehle`**, von Chat-Claude bestätigt.
> - 6: Nachlauf gemessen 0,44 € von 10 €.
> - 8, Phase 4: Auftrag ausgearbeitet — Vorbedingungen, Reihenfolge, Budget je Abschnitt, Tor 4 erweitert.

#### v7 — eingegangen 21.09.2026 02:14:34 CEST · Quelle `arbeit/fassungen/aenderungen-v7.md` (1563 Bytes)

> **Änderungen gegenüber Fassung 6** (aus der Abnahme von Vorbedingung 1 und Philipps Richtungsentscheidung vom 21.09.2026):
> - **Phase 4 ist neu gefasst: Breitentest an mehreren Testwerken statt einem großen echten Werk.** Grund: Philipps Entscheidung — das Biotop soll für jeden Anwendungszweck taugen und dafür in allen Bereichen geprüft sein. Das Handelssystem stand in den Fassungen 1 bis 6 als Phase-4-Werk, war aber eine nie bestätigte Vorentscheidung von Chat-Claude; alle darauf bezogenen Bezugsgrößen (237.000 Zeilen, 17 Dienste, 135 Testfehlschläge) sind gestrichen. **Fehler von Chat-Claude:** eine Vorentscheidung sechs Fassungen lang wie eine Entscheidung geführt.
> - **Phase 5 neu: erstes echtes Werk**, ohne benanntes Werk — die Wahl trifft Philipp nach dem Breitentest, nach den Kriterien in Abschnitt 8.
> - 2a: Zwei Grundsätze ergänzt (7: Ein Nachweis zählt nur, wenn er ausgeführt wurde. 8: Jede Probe braucht eine Gegenprobe, die fehlschlagen muss) und einer (9: Der Prüfaufwand muss zum Gegenstand passen).
> - 3.6: Ausfall eines Verbundmitglieds zählt nie als Beitrag — mit Torzeile, weil die Regel noch nicht nachgewiesen ist (Opus hat eine große Eingabe mit `stop_reason: refusal`, Kategorie `cyber`, abgelehnt; HTTP 200 ohne Ausgabetext).
> - 8: Vorbedingung 1 **abgenommen** (21.09.2026): Tor 2 Zeile 8 erfüllt mit 9,09 %, Artgedächtnis 3 von 5 Richtungen mit werkübergreifendem Verweis.
> - 6: Kassenstand aus der Datenbank 8,64 € statt der aus Berichten summierten 7,82 € — die Datenbank ist die gültige Quelle.

#### v8 — eingegangen 23.09.2026 15:53:53 CEST · Quelle `arbeit/fassungen/aenderungen-v8.md` (1608 Bytes)

> **Änderungen gegenüber Fassung 7** (aus T3 `versandwerk`, Läufe 26–38, `abschluss-03`, nicht abgenommen):
> - **2a: fünf Grundsätze neu (10–14).** T3 hat gezeigt, dass das Biotop die Messung optimiert, wo sie von der Sache abweicht: Fehlalarme weggeräumt, Zwischenspeicher mit falschen Ergebnissen eingebaut, eine unbeobachtete Funktion verändert. Nach Generation 1 hat in keinem der beiden Läufe eine angenommene Generation das bereinigte Maß bewegt.
> - **Tor 4 neu gefasst:** Halluzinationsprobe streng („sauberer Bereich bleibt unberührt" statt „keine Änderung ohne Maßgewinn" — der alte Wortlaut von Chat-Claude ließ beide Scheinverbesserungen durch); Doppelungsanteil ausdrücklich nach der Methode aus Vorbedingung 1; neue Zeilen für Verhaltensvergleich, Maßeichung, Verdrahtung und „nicht gemessen je Durchlauf".
> - **Phase 4: T3 eingetragen,** Vorbedingungen für T4 festgelegt, vier offene Messfragen von Chat-Claude entschieden (Abschnitt 8, T4).
> - **Fehler von Chat-Claude in T3, benannt:** (1) die Abwehr für wirksam erklärt, weil Gegenproben gegen das Modul liefen statt durch den Lauf; (2) die Sperrquote der Aufnahmesperre (14 %) als erfüllte Doppelungs-Torzeile bestätigt — sie ist eine Diagnose; (3) den Doppelungsvergleich 35 % gegen 9 % auf zwei verschiedene Größen gestützt; (4) für `bericht` in Lauf 28 Aufwärmung vermutet, wo die Messreihe Drift zeigt; (5) die Musterliste der Fehlerklassen-Suche nur aus Python-Syntax vorgegeben.
> - Kasse: Gesamtstand 18,81 € (Stamm 8,64 € + Vorbedingung 1 0,45 € + T3 9,73 €, ohne Doppelzählung der Zweige).
