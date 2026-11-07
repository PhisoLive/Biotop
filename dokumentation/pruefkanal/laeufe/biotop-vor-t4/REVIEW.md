# Review: Behebungsrunde vor T4 (ein Durchgang)

Gegenstand: `BERICHT.md` (Stand 18:18), Kern-Commit `58bd9f9` (Vorgänger `f821707`), Belege unter `/root/biotop-vor-t4/`.
Auftrag: `REVIEW-AUFTRAG-VOR-T4.md`, Maßstab Masterprompt Fassung 8, Abschnitt 8, Vorbedingungen 1–11.
Eigene Skripte und Ausgaben: `/tmp/review-vor-t4/` (`greps1–5.sh`, `spec_vergleich.sh`, `tests_gezielt.sh`, `nachrechnen*.py`,
`messung2–5.py` mit `messung3.txt`, `messung4.txt`, `messung5.txt`, `pytest_vor_t4.txt`).

Rahmen:
- Kein Modellaufruf, kein Netz, kein Geld.
- Keine Laufzeitmessung in der Kammer, kein Verdrahtungstest, keine volle Regression.
- Die Kammer lief nur für TS-Parsing: `test_9`, `test_10` und eine Anhänge-Probe (`messung3.py`). Die Kammerstarts habe ich nicht gezählt.
- Lauf-DB nur als Schnappschuss mit `mode=ro`.
- Keine Befehlsblockade. Einen Aufruf mit Zeitlimit 900 s hat die Ausführungsschicht als Hintergrundprozess gestartet (Obergrenze 600 s); ich habe sein Ergebnis abgewartet.

**Kurzergebnis:** 15 Befunde: 2 hoch, 9 mittel, 4 niedrig.
- Die beiden hohen Befunde sind Code-Fehler im neuen TS-Pfad. Sie können eine Annahmeentscheidung verfälschen. Im T3-Werk treten sie nicht auf, deshalb zeigt sie kein Nachspiel.
- Die Nachspielzahlen des Berichts stimmen mit den Belegen.
- Die neun Spezifikationen sind textgleich übernommen und grün.
- Mehrere Nachweise laufen nur am isolierten Modul, nicht durch den Laufweg.
- Für T4 (Python) wirken Nr. 2 und Nr. 6 nicht, und der Python-Pfad von Nr. 1 ist nicht belegt. Der Bericht sagt das nicht.

## 1. Befunde

| Nr | Schwere | Befund | Beleg | Vorschlag |
|---|---|---|---|---|
| 1 | hoch | **Randfall-Korpus (Nr. 2) lehnt verhaltensgleiche Kandidaten ab.** Manche exportierte Funktion erfasst `einwickeln` nicht, etwa `export const f = (…) => …`; dem Regex nach auch `export function f<T>(…)`. Eine solche Funktion gilt am Kandidaten als „entfernt“. Ihre Randfälle werden nur auf der Seite der Vorgeneration gestrichen, auf der Kandidatenseite bleiben sie. Dort stehen sie gegen `<nicht beobachtet>` als ungedeckte Abweichung → Ablehnung „Verhaltensvergleich:“. Das gilt auch, wenn der Kandidat diese Funktion gar nicht berührt. Außerdem fehlen solche Funktionen im Nenner von „x von y“. | `verhaltensvergleich.pruefen` lief unverändert, gestellt war nur die Kammer (`beobachten`). (a) f wird zum const-Pfeil, Werte gleich: `tragfaehig False`, ungedeckt `alpha/a:f~rand#0` und `…@alias`. (b) Unveränderter const-Pfeil f, geändert ist nur g: `tragfaehig False`, `entfernte_funktionen ['alpha/a:f']` (`messung4.txt`, `messung5.txt`). Ursache im Code: `neu_exporte` kommt aus `neu["eingewickelt"]`. Der Regex von `einwickeln` lautet `^export (async )?function (\w+)\s*\(`. `signaturen_lesen` nimmt dagegen jede exportierte Funktion (ast.mjs `exportiert`), und der Randfall-Läufer ruft `mod[f]` auch ungewickelt. Im T3-Werk: 123 `export function`, 0 `export const … =>` (`versandwerk-t3-02/src`). | „Entfernt“ aus den Signaturen bzw. Exporten des Kandidatenstands bestimmen, oder Randfall-Schlüssel entfernter Funktionen auf beiden Seiten streichen. y aus den Signaturen bilden. Gegenprobe mit einem Pfeil-Export im Drahtwerk. |
| 2 | hoch | **TS-Anhängen (Nr. 9) erzeugt bei erweiterter Importzeile eine doppelte Bindung.** Die kaputte Datei wird als „geurteilt“ gezählt und kommt in den Testbestand. Folgekette, aus dem Code gelesen, in der Kammer nicht ausgeführt: `testbestand[p] = g` → `basis_paar = messen(…, dateien=testbestand)` → `messen.mjs` fängt den Sammelfehler ab (`gueltig:false`) → `aegis.pruefen` stellt den Kandidaten als „Messgerätausfall … Kammer (Vorgeneration)“ zurück, statt ihn zu urteilen. Der Inhaltsfehler der Zusammenführung erscheint so als Messgerätausfall. Die Torzeile 3.10 F3 zählt dabei einen Fall mit. | `aegis._anhaengen`, echte Kammer, nur Parsing: alt `import { plus } …`, neu `import { plus, halb } …`. Das Ergebnis enthält beide Importzeilen, der Neutralzähler bucht „geurteilt +1“ (`messung3.txt`). Dieselbe Form unter node: „SyntaxError: Identifier 'plus' has already been declared“ (rc 1). Ursache: `_IMPORT_TS` vergleicht ganze Zeilen, und die Schlussprüfung vergleicht nur Testnamen. Häufigkeit in T3: 0 von 10 Diff-Blöcken, die eine vorhandene `tests/*.test.ts` ändern, änderten eine Importzeile (`t3.db`, Läufe ≥ 26). | Importe nach Bindungen zusammenführen (Syntaxbaum) und das Ergebnis parsen oder typprüfen. Bei Konflikt neutral „zusammenfuegen_gescheitert“. Gegenprobe mit erweitertem Import. |
| 3 | mittel | **Zurückgestellte Kandidaten zählen in der Generation als nicht überlebt.** Überlebt kein Kandidat, endet die Generation „abgelehnt … (0 von N)“, wobei N die Zurückgestellten enthält. Sie geht dann mit 0 % Verbesserung in Entropie und Sättigung ein. Hält der Messgerätausfall an, endet der Lauf nach 5 Generationen als „gesättigt“ statt anzuhalten. Nur die Generalprobe bricht ab („abgebrochen“, Lauf bereit). | `lauf.py`: `urteile[b].append(u)` für jeden Status; `if not gewaehlt: return abschluss("abgelehnt", "kein Kandidat hat den Ankläger überlebt (0 von %d)")` (Z. 343). `abschluss` ruft `entropie.messen` (bei „abgelehnt“ gilt `k_neu = k_alt`) und `pruefen_und_beenden` (Fenster 5, Schwelle 0,5 %). Code gelesen, nicht ausgeführt. | Zurückgestellte getrennt zählen und ausweisen. Eine Generation mit Zurückstellungen nicht als „abgelehnt“ in die Entropie buchen. Ab einer Schwelle anhalten, wie in der Generalprobe. |
| 4 | mittel | **Nr. 3 ist am Laufweg nur für 1 von 3 Ausfallarten belegt.** Belegt ist die Sonde mit Zeitlimit durch `aegis.pruefen`. Ohne Test sind: der Messausfall der Vorgeneration (Zurückstellen); der Ausfall der gepaarten Laufzeit in `aegis.pruefen` (belegt nur an `laufzeit_gepaart` isoliert); das Auslassen von Bandit und Gedächtnissen in `_generation_koerper`; der Abbruch der Generalprobe. Die Formulierung „gestellt ist nur die Kammergrenze“ ist zu stark. | `test_vor_t4.py`: nur `test_3_sondenausfall_am_laufweg…`. Außerhalb von `test_vor_t4.py` findet grep in `tests/` keinen Test zu `ZURUECKGESTELLT` oder „Kammer (Vorgeneration)“. `_pruefen_bis_zur_sonde` stellt mehr als die Kammer: `messgeraet.messen` (das ganze Messgerät), `laufzeit_messen`, `aufrufen` (Modell) und `beobachten`. | Je Ausfallart ein Test durch `aegis.pruefen` und einer durch `_generation_koerper`: 0 Bandit-Zeilen, 0 Gedächtniszeilen, Generation „abgebrochen“, Lauf „bereit“. Formulierung berichtigen. |
| 5 | mittel | **Mehrere Nachweise laufen nur am isolierten Modul oder fehlen.** Der Bericht führt sie in derselben Tabelle wie die Laufweg-Nachspiele, ohne das zu kennzeichnen. Nach dem Maßstab erfüllt ein Modulnachweis „durch den Laufweg“ nicht. | Nr. 1: Gegenprobe „echte Verschlechterung“ an `urteil_f2` direkt, Ausfall an `laufzeit_gepaart` direkt; die gepaarte Generalprobe hat keinen Test. Nr. 4: `paar_bestanden` direkt, `_verhandeln` nie. Nr. 8: Die Felder `kernmass_f2_roh` und `kernmass_messgeraet_roh` in `generation.ergebnis`/`mass.eingefroren` liest kein Test. Nr. 9: Behauptungen für alle Angriffstests ohne Probe und Gegenprobe; `test_t3_behauptungen_protokoll.py` kennt `behauptungen_treffer` nicht, und in 8 von 8 Nachspiel-JSON ist `behauptungen` None. Nr. 11: Schreiber (`anbieter.aufrufen` → „anbieter.gedrosselt“) und Leser (`nischen.waehlen`) laufen nie zusammen. Die Bandit-Gegenprobe `COUNT(*)=0` gilt trivial, weil der Test nichts bucht. Rohwerte der Rauschmessung ohne Test. | In Tabelle §1 je Zeile „Laufweg“ oder „Modul“ ausweisen. Fehlende Proben durch `_generation_koerper` bzw. `_verhandeln` ergänzen oder als offen führen. |
| 6 | mittel | **Die Gegenprobe „phase“ (Nr. 7) prüft die Wirkung, nicht die Phasenbindung.** `_masseichung=None` lässt die Kante `masseichung.anwenden ← aegis:pruefen @ generation` bestehen. Die phasengebundene Pflicht-Zusicherung bleibt also erfüllt; der Test scheitert an „Maßeichung wirkt nicht in der Generation“. Die Phasenbindung selbst hat keine Laufweg-Gegenprobe. | `VERDRAHTUNG-ROT-phase.json`, Kanten: beide Pflichtkanten sind vorhanden, `@ generation` und `@ vorspann`. Die Phase prüft nur die schnelle Probe mit handgeschriebenen Kanten (`test_pruefwerkzeug_verlangt_den_aufruf_aus_der_annahmefunktion`). | Gegenprobe in „wirkung“ umbenennen. Für die Phasenbindung eine Laufweg-Gegenprobe bauen, oder im Bericht sagen, dass sie nur am Prüfwerkzeug belegt ist. |
| 7 | mittel | **Die Nachspiele zu Nr. 1 und Nr. 2 sind nicht an `58bd9f9` gebunden.** Sie liefen in einem Prozess von 16:54:09 bis 17:09:14; die Module wurden beim Start importiert. Danach wurden noch geändert: `messgeraet.py` (17:01:03) und `aegis.py` (17:13:49). Der Commit folgte um 17:32:34. Die JSON-Belege tragen keinen Code-Stand. Nur K2868 Durchgang 2 (18:09) liegt am Commit (Arbeitsbaum = HEAD, `git status` leer). Die §2-Behebung betrifft die sechs übrigen Fälle nicht (je nur ein Bereich); das Ergebnis dürfte gleich sein, gemessen ist es nicht. | mtimes (`greps3.sh`, `greps5.sh`); `job_nachspiel.sh` (ein Python-Aufruf für 7 Fälle); `nachspiel/*.json` ohne Commit- oder Hash-Feld. | Code-Stand der Nachspiele im Bericht nennen, oder sie am Commit wiederholen. Commit-Hash ins Nachspiel-JSON schreiben. |
| 8 | mittel | **Für T4 (Python) sind Teile der Vorbedingungen nicht gebaut oder nicht belegt; der Bericht nennt das nicht.** (a) Verhaltensvergleich: Für Python enthält sich das Organ immer (`sprache_ohne_sonde`, `tragfaehig True`), also besteht jeder Python-Kandidat. Die Tor-4-Zeile „Enthaltungen zählen nicht als bestanden“ und Grundsatz 11 sind für T4 so nicht erfüllbar. (b) Gepaarte Laufzeit: Der Python-Zweig (`LAUFZEITSKRIPT` über `laufzeit_messen`) lief in keinem Test und keinem Nachspiel. (c) Mehrheitsregel für Generation 0: `_testlauf_urteil` meldet für Python nie „neutral“. Wegen `gefangen = e.rc != 0` zählen Sammelfehler (rc 2) und „keine Tests“ (rc 5) als Fang. Die Regel kann für Python also nie greifen. | `verhaltensvergleich.pruefen` (Zweig `ist_typescript`). grep `LAUFZEITSKRIPT`, `laufzeit_messen`, `laufzeit_gepaart` in `tests/`: nur `test_vor_t4.py`, und dort ist `laufzeit_messen` immer gestellt; alle Nachspiele sind TS. Diff `generation0.py`, Python-Zweig. „Alle elf Vorbedingungen sind gebaut“ gilt für den TS-Pfad. | Geltungsbereich TS ausdrücklich nennen. Vor T4 entscheiden lassen (Philipp oder Chat-Claude): Python-Sonde bauen oder Torzeile anpassen. Den Python-Zweig der gepaarten Laufzeit einmal in der Kammer ausführen. G0 für Python: rc außer 0 und 1 als neutral werten. |
| 9 | mittel | **Nr. 6, „Typbau zwischen den Runden“, hat weder Probe noch Gegenprobe.** Das ist genau die Stelle in `lauf.generation0`, die nach `testlauf` `typescript.baulauf(pfad)` ruft und die Ergänzung zurücknimmt. Der Bericht belegt Nr. 6 mit `_tests_typescript` (je Testkandidat) und `G0.messen`, nicht mit dieser Stelle. | Diff `lauf.py` (`bau = typescript.baulauf(pfad)` … `LaufFehler(… bricht den Typbau …)`). Kein Test ruft `lauf.generation0` mit brechendem Typbau. | Test durch `lauf.generation0` mit gestelltem `baulauf`: baut False → `LaufFehler`, Ergänzung zurückgenommen; Gegenprobe baut True → weiter. |
| 10 | mittel | **Zwei Zahlen ohne Beleg.** (a) „Vorgeneration 4,80“ in der Gegenprobe zu Nr. 1 ist ein im Test gesetzter Wert. Er wird aber als Messung zu K3121 gelesen; der Docstring sagt „obwohl die Vorgeneration derselben Sitzung 4,80 ms lief“. (b) „etwa 1 min Kammerzeit je gepaartem Kandidaten“: Die Nachspiel-JSON tragen keine Zeit für den gepaarten Teil. | (a) `test_vor_t4.py:25`. In `ABSCHLUSS-03.md`, `REVIEW-03.md`, `AUSWERTUNG-ABSCHLUSS3.txt/.json` und `t3.db` nicht gefunden. Gemessen im Nachspiel vor T4: `bericht` bei K3121 gepaart 3,9975 → 3,9712 ms, keine Grenze gerissen. (b) Nur Gesamtdauern liegen vor, z. B. K2904: 131,8 s bei 14 Kammerläufen, davon 10 gepaart. | (a) Den Wert als gestellt kennzeichnen oder die gemessene Vorgeneration nennen. (b) Dauer je `laufzeit_messen` protokollieren und dann beziffern. |
| 11 | mittel | **Ältere Laufzeit-Einträge im Projektgedächtnis sperren weiter.** Die neue Regel wirkt nur beim Schreiben. Die Lesewege (`wiederholung`, `gescheiterte_wege`) filtern nach der gespeicherten `grundklasse`. Im Schnappschuss stehen 141 Einträge der Klasse „grenzmass“ mit Laufzeitriss (versandwerk 75, lagerhaus 56, logmuehle 10). Nach `laufzeit_sperrt` sperren 141 von 141 nicht, gespeichert sind sie aber sperrend. Für T4, ein neues Werk, hat das keine Wirkung; nimmt man eines der drei Werke wieder auf, verletzt es „Risse in unberührten Bereichen nie“. | `nachrechnen.py` (t3.db, mode=ro). | Die Regel auch beim Lesen anwenden, oder die Einträge über einen protokollierten Vorgang umklassifizieren. |
| 12 | niedrig | **`_anhaengen_ts` bucht einen Kammerausfall als Inhalt.** Scheitert das Lesen der alten Testnamen an der Kammer, zählt der Neutralzähler den Fall als „syntaxfehler“. | Gestellter Kammerabbruch → Rückgabe `None`, Gründe `{'syntaxfehler': 1}` (`messung3.txt`). | `TypeScriptFehler` ohne Syntaxfehler weiterreichen oder als „kammer“ zählen. |
| 13 | niedrig | **`tests/test_vor_t4.py` hängt am Kammer-Image `biotop-kammer:ts1`.** Mit dem Standard (`kammer.IMAGE = biotop-kammer:1`) sind 33 von 38 grün; 5 scheitern mit „Kammerabbruch … "node": executable file not found“, ohne Hinweis und ohne Skip. | `pytest_vor_t4.txt` (Standard: 5 failed, 33 passed); mit `BIOTOP_KAMMER_IMAGE=biotop-kammer:ts1` sind die 5 grün (`tests_gezielt.sh`). Der Regressionsjob setzt ts1. | Das Image im `conftest` prüfen und sonst mit Grund überspringen. Die Aufrufumgebung im Bericht nennen. |
| 14 | niedrig | **Zwei Tests prüfen Quelltext statt Verhalten.** `test_geeicht_lesen…` und `test_befundklassen…` vergleichen `inspect.getsource`-Zeichenketten. Der zweite rechnet die Bereichsauswahl im Test selbst nach. Die Wirkung belegt nur das Nachspiel K2868 (Laufweg). | `test_vor_t4.py:302–330`. | Als Strukturtest kennzeichnen oder durch einen Aufruf von `aegis.pruefen` mit zwei geänderten Bereichen ersetzen. |
| 15 | niedrig | **Unerreichbare Zeile in `generation0._testlauf_urteil`.** Nach dem neuen `return {…}` steht noch das alte `return gefangen, …`. | Diff `generation0.py`, Python-Zweig. | Entfernen. |

## 2. Geprüft und bestätigt

Geprüft wurden 35 Punkte: 20 sind bestätigt (unten), 15 sind Befunde (Tabelle).

1. **Commit:** 26 Dateien, +1391/−160, Vorgänger `f821707`. `COMMIT-STAT.txt` stimmt mit `git show --stat` überein. Der Arbeitsbaum an HEAD `58bd9f9` ist sauber.
2. **Neun rote Spezifikationen:** 8 Testfunktionen mit 9 Fällen stehen per AST-Vergleich textgleich in `tests/test_t3_*.py` (8 von 8 identisch). Beide Dateien sind an `58bd9f9` grün, 34 von 34 Tests, ohne Kammer. „An `f821707` 9 von 9 rot“ habe ich nur am Beleg `T4-SPEZIFIKATION-ROT.txt` geprüft.
3. **`tests/test_vor_t4.py`:** 38 von 38 grün mit Image ts1 (33 ohne Kammer, 5 mit Kammer-Parsing).
4. **Nr. 1, Zahlen gegen die Belege:**
   - K2904 `planung`: 9,4637 → 7,7147 ms (−18 %). K3091: 9,6077 → 7,7393 ms (−19 %). Beide überleben, Bezug „gepaart, Median aus 5 je Seite“.
   - Je Paar liegt das Verhältnis Kandidat/Vorgeneration bei 0,767–0,837 (K2904) und 0,738–0,842 (K3091). Das sind 10 von 10 Paaren unter 0,85: „gleich entschieden“ hängt nicht an einem einzelnen Median.
   - Beide ändern im T3-Schnappschuss dieselbe Datei `src/planung/pruefen.ts`.
5. **Nr. 2, Zahlen:**
   - K3106: 8 von 8 ungedeckt, 5 von 7 beobachtet, `tabellenbreiten` „[0,0]“ → „[]“.
   - K2934 und K3121: je 25 von 25 ungedeckt, 7 von 7 beobachtet.
   - K3324: 0 Abweichungen, 7 von 7 beobachtet.
6. **§2, K2868:**
   - Durchgang 1: abgelehnt, 12 ungedeckt; Werte ReferenceError → SyntaxError.
   - Durchgang 2: überlebt, 12 von 12 gedeckt durch `test_tarife_immun_befundklasse_no_new_func…::test_umgehung_0–2`.
   - Kernmaß −13 → 0: 3 fehlgeschlagene Tests + 10 Sicherheitspunkte = 13, geht auf.
7. **Kein Modellgeld:** `modellaufrufe_echt` ist 0 in 8 von 8 Nachspiel-JSON. Die DB-Prüfsumme vorher und nachher ist gleich in 4 von 4 geprüften JSON.
8. **Restrauschen der gepaarten Messung:**
   - 34 Vergleiche unberührter Bereiche aus 9 Nachspielzeilen.
   - Größter Anstieg ×1,127 (K2868 Durchgang 1, `bericht`).
   - 1 von 34 liegt über 1,10, 0 von 34 über 1,15 (Mindesttoleranz). Das stützt Nr. 1.
9. **Code Nr. 1:**
   - Die Messung wechselt ab (B K, K B …), Median je Seite.
   - Nur die Laufzeit wird gegen die gepaarte Vorgeneration gemessen.
   - `laufzeit_entscheidet` misst nicht bei Pareto-Verletzung, Bau, Sperre oder einer anderen gerissenen Grenze. Sonst misst es in schnell/werk bei Zuwachs ≥ 0, ansonsten bei Zuwachs > 0.
   - Die Anzeige hat 3 Nachkommastellen.
   - Nische schnell mit gesunkenem Kernmaß wird ohne Messung abgelehnt.
   - Die Generalprobe misst nur Code, `tests/` ist ausgenommen.
10. **Code Nr. 2:**
    - Beide Seiten erhalten Signaturen und Beispiele der Vorgeneration.
    - 0 beobachtete Funktionen ergeben eine Enthaltung.
    - „x von y“ steht im Grund (mit der Einschränkung aus Befund 1).
11. **Code Nr. 3:**
    - Ein zurückgestellter Kandidat geht nicht in den Bandit (`lauf.py:306`) und nicht in `projekt_merken`/`art_merken`.
    - In der Verhandlung wird die Anpassung als zurückgestellt gebucht, und `paar_bestanden` ist False (`lauf.py:631–634`, `665`).
    - Ein Inhaltsbefund am Kandidaten bleibt eine Ablehnung (Test grün).
12. **Nr. 4/5:** `paar_bestanden` verlangt einen tragfähigen Verhaltensvergleich. `anwenden` wirft bei anderer oder leerer Eichung und ist bei gleicher idempotent (Spezifikation grün).
13. **Nr. 6:** `G0.messen` wirft `NichtGemessen`, wenn neutral · 2 > n. `lauf.generation0` wandelt das an 3 von 3 Aufrufstellen in einen `LaufFehler`. Die tsc-Meldung (erste 3 „error TS“-Zeilen) steht im Neutralzähler (Test grün).
14. **Nr. 7:**
    - Die Gegenprobe „vv“ scheitert an der vorgesehenen Zusicherung: „Ungedeckte Abweichung am Laufweg nicht abgelehnt“; die Variante überlebte mit „Nische schnell: Kernmaß -1 → 0“.
    - Im Drahtwerk schlägt die Regel im sauberen Bereich `beta` an (roh 1) und ist stillgelegt (0); belegt in `VERDRAHTUNG-ROT-vv.json` und `-schwarm.json`.
    - Die blinde Schwarm-Gegenprobe ist offen berichtet (§3).
15. **Nr. 10:** `laufzeit_sperrt` und die Klasse `laufzeit_unbestaetigt` sind in beiden Lesewegen ausgenommen. `test_10`: 9 von 9 Fällen grün.
16. **Nr. 11:**
    - `_beschleunigen` ist entfernt (nur noch in einem Kommentar und einem Test genannt).
    - Die Verfallsbedingung hat eine Gegenprobe.
    - Die Rohwerte gehen ungerundet ins Protokoll.
    - `ausgesetzt` liest nur den eigenen Lauf, und `modell.antwort` unterbricht die Folge.
17. **`VERDRAHTUNG-GRUEN.txt`:** Vorspann-Abbruch „Messgerät/Quellen während der Eichung verändert (Satz 2)“. `aegis.py` wurde um 17:13:49 geändert, also innerhalb des Laufs (17:09:15 bis etwa 17:18:52). Die Erklärung des Berichts passt zu den Zeitstempeln.
18. **§4:** Die 6 geänderten älteren Testdateien sind geändert wie beschrieben (`git diff`).
19. **Eigene Entscheidung 4** (Auslegung „Korpus aus den Verträgen“) ist als Auslegung gekennzeichnet und zur Bestätigung vorgelegt.
20. **Grenzen:** Der Bericht sagt, dass die Nachspiele „überlebt `aegis.pruefen`“ belegen und nicht „angenommen“.

## 3. Nicht geprüft

- **Platzhalter:** ‹REGRESSION›, ‹SCHWARM›, ‹VERDRAHTUNG›, ‹SCHWARM2X2›, ‹REGRESSIONSDETAIL›, ‹REVIEW›. Sie laufen noch oder entstehen erst nach diesem Review (Vorgabe).
  - `JOB-SCHWARM.txt` ist leer.
  - `REGRESSION-VOR-T4.txt` stand beim Lesen bei 63 %.
- **Nicht selbst gefahren:** grüner Verdrahtungstest an `58bd9f9`, volle Regression, 2×2-Gegenprobe. Grund: keine parallelen Kammerläufe mit Zeitmessung.
- **Keine eigene Laufzeitmessung;** die Nachspiele habe ich nicht am Commit wiederholt (Befund 7).
- **Python-Zweig der gepaarten Laufzeit** nicht ausgeführt (Befund 8).
- **Rot an `f821707`** für die 9 Spezifikationen nicht wiederholt.
- **Befund 1:** Häufigkeit generischer `export function f<T>(` im T3-Werk nicht gezählt; diesen Teil habe ich nur am Code gelesen.
- **Befund 2:** Die Folgekette ab `messen` habe ich nicht in der Kammer ausgeführt.
- **Wortlaut der vier Messfragen-Entscheidungen** von Chat-Claude: nur über den Masterprompt geprüft (Grundsätze 10, 11, 14 und die Vorbedingungen); ein eigenes Dokument dazu habe ich nicht gefunden.
- **`KASSE.md`:** sha256 von `t3.db` und `t3.db-wal` nicht nachgerechnet. Die Zahl der Kammerläufe ist ungezählt, wie im Bericht.
- **Nicht Gegenstand:** `veroeffentlichen.py`, `UEBERGABE.md`, Prüfkanal.
- **Deckung im Verhaltensvergleich auf Funktionsebene** (ein Test deckt jede Abweichung derselben Funktion): Bauart aus T3, hier nicht bewertet.
