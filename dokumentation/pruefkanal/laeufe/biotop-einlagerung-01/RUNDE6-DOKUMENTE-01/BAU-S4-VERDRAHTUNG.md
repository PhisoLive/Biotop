# Bauauftrag S4 (Runde 6, Entscheidung 6 und die offenen Verdrahtungspunkte aus S2/S3)

Du baust einen Teil der Behebungsrunde 6 vor T4 des Biotop-Projekts. Antworte und schreibe auf Deutsch. Du setzt nur
diesen Teil um. S1 baut noch im selben Baum, S2 und S3 sind fertig.

## Umgebung
- **Code-Baum:** `/root/biotop` (git, HEAD `0c2f058`). Kein Commit; den macht der Auftraggeber nach allen Teilen.
- **Python und Tests:** `/root/biotop-t3/venv/bin/python`. Tests laufen aus `/root/biotop` heraus (`pytest.ini` dort).
  TypeScript läuft in der Kammer (Image `biotop-kammer:ts1`).
- **Ordner:** Arbeitsordner ist `/root/biotop-vor-t4-06/` mit Unterordner `bau/`. Dein Temp-Ordner ist `/tmp/r6-s4/`;
  setze `TMPDIR` darauf.
- **Erlaubt und verboten:** Die Kammer (docker) ist erlaubt. Kein Modellaufruf (der Verdrahtungstest nutzt die gestellte
  Grenze), kein Netz, kein Commit, keine Hintergrundprozesse (kein `background`, kein `notify`).
- **Sperren:** Wird ein Befehl gesperrt oder läuft eine Freigabeabfrage ohne Antwort ab, wartet genau diese Handlung.
  - Du formulierst nicht um, teilst nicht auf und schreibst den Befehl nicht als Skriptdatei neu. Du holst dasselbe
    Ergebnis auch nicht auf anderem Weg.
  - Befehl und Meldung trägst du wörtlich in `bau/S4-PLAN.md` und in den Schlussbericht ein, dann machst du nur mit
    Unabhängigem weiter.
  - Vorbeugung ist erwünscht: Mehrteilige Befehle (Heredoc, Pipes, mehrere Teile) schreibst du von Anfang an als
    Skriptdatei.

## Arbeitsweise (verbindlich)
- **Hintergrund:** Ein anderer Bauender brach ab, weil eine Antwort nur aus Denken bestand
  (`/root/biotop-vor-t4-06/S1-ABBRUCH.md`). Plane deshalb nie den ganzen Umbau in einem Denkschritt.
- **Plan als Datei:** Plan, Stand und Zwischenüberlegungen stehen fortlaufend in `bau/S4-PLAN.md`, so aktuell, dass ein
  Nachfolger übernehmen kann.
- **Bauskripte:** je Aufgabe ein eigenes Bauskript `bau/r6_s4_<aufgabe>.py`, danach laufen die zugehörigen Tests, dann
  kommt das nächste Skript.
- **Alles oder nichts, mit zwei Lesungen:** Anker prüfen (jeder genau einmal), dann `--trocken`, dann unmittelbar vor
  dem Schreiben neu lesen, neu prüfen und schreiben. Neue Dateien legst du exklusiv an. Protokolle nach `bau/R6-S4-*.txt`.

## Deine Dateien (nur diese)
- `biotop/__main__.py`, `biotop/kern/register.py`, `tests/test_verdrahtung.py`, `tests/drahtwerk.py`.
- `biotop/lauf.py`: nur der Befehl `generation0` (Protokoll `generation0.begonnen`, Aufgabe 5).
- `biotop/organe/vorspann.py`: nur die Stelle `stufe2_kern_wie_vorspann` (Aufgabe 6).
- `tests/test_nachweis_verbraucher.py`: nur die Fixture `fund_vorspann` (Aufgabe 7).
- Neu `tests/test_vor_t4_06_register.py` für deine Unit-Tests.
- **Nicht anfassen:**
  - `biotop/kern/py/*`, `biotop/organe/verhaltensvergleich.py`, `biotop/organe/aegis.py`, `tests/test_vor_t4_06.py`,
    `tests/test_vor_t4_05.py` (gehören S1, das noch baut);
  - `biotop/tor4.py`, `tests/test_tor4_zeilen.py` (S2);
  - `biotop/organe/stufe2.py`, `tests/test_stufe2_eichphase.py` (S3).

  Brauchst du dort eine Änderung, hältst du sie als offenen Punkt mit Grund fest, statt sie zu machen.

## Hintergrund (lies zuerst)
- **Lücke:** Review 05 Nr. 7 (`/root/biotop-vor-t4-05/REVIEW.md`, Zeile „| 7 |“). Das Register hat 10 Einträge statt
  „jede Funktion, deren Aufruf der Entwurf verlangt“.
  - Es fehlen die Verhandlung (Vorbedingung 4), der Neutralzähler, die Immunisierung, die Doppelungs-Behauptung aller
    Angriffstests und Generation 0.
  - Im Verdrahtungsbeleg ruft kein Rahmen `lauf._verhandeln` die Funktion `aegis.pruefen`.
  - Vorschlag des Reviews: das Register aus den Tor-4-Zeilen und den Vorbedingungen ableiten und eine Verhandlung im
    Verdrahtungstest auslösen.
- **Maßstab:** Tor 4 und Vorbedingungen 1–11 stehen in `/root/biotop-vor-t4-05/bau/MASTERPROMPT-V8-TOR4.txt`, Zeilen
  1–45.
- **Register und Aufzeichner:** `biotop/kern/register.py`; Aufzeichner `aufzeichnen()` in `tests/test_verdrahtung.py`.
  Als Aufrufer zählt der erste Rahmen außerhalb des Moduls der Funktion. Modulinterne Aufrufe erscheinen daher mit dem
  äußeren Aufrufer.
- **Letzter Beleg:** `/root/biotop-vor-t4-05/VERDRAHTUNG-BELEG-TEILLAUF3.json`, 497 Kanten. `aegis.behauptung` wird dort
  nur aus dem Vorspann gerufen, weil die gestellte Grenze auf jede Ansage „KEIN ANGRIFF“ antwortet.
- **Verhandlung:** Bedingungen in `biotop/lauf.py` um Zeile 320–326, `_verhandeln` (um 660–748), `paar_bestanden` (um
  766). Grenzvertrag des Drahtwerks: `tests/drahtwerk.py` `VERTRAG`, zählt zu beta. Der Nachbar bekommt
  `genesis.erzeugen(..., nische="sicher")` mit dem Auftrag „VERHANDLUNG (3.8 Schritt 2)“.

### Offene Punkte der fertigen Bauenden (wörtlich aus ihren Schlussberichten)
S2 (Tor-4-Skript):
1. „Verteilung des vorab Verworfenen (Typsieb): Der Kern schreibt sie nicht ins Protokoll. Solange `generation0.begonnen`
   kein `vorab_verworfen` je Art trägt, bleibt Zeile 3 nicht belegt.“
2. „Belege in der Befehlszeile: `__main__.py` übergibt noch keine `belege`. Bis du `--regression/--verdrahtung/--review/
   --zwischenbericht` verdrahtest, stehen die Zeilen 12 und 14 auf ‚Beleg fehlt‘.“
3. „Kernstand für Zeile 12: Der Verdrahtungsbeleg trägt noch kein `kern_commit`, deshalb ist der Kernstand nicht belegt.“
4. „Aufrufkanten für das Register: Der Aufzeichner in `test_verdrahtung.py` überspringt Aufrufe innerhalb desselben
   Moduls. Eine Kante `tor4.zeile_* ← biotop.tor4:ausfuehren` entsteht so nicht.“
5. „Voller Verdrahtungslauf: Den Lauf mit Kammer habe ich nicht gefahren.“

S3 (Eichphase Stufe 2):
1. „Befehlszeile: `biotop stufe2 <lauf>` → `stufe2.eichen(con, lauf)`. `stufe2.Stufe2Fehler` muss ins `except` von
   `main`, sonst endet der Befehl mit Traceback statt mit Exit 1.“
2. „Verdrahtung: In `tests/drahtwerk.py` hat `REFERENZLAST_STUFE2` keine W-Zeile, damit scheitert `stufe2` dort laut.
   Außerdem fehlt der Schritt `["stufe2","1"]` vor dem Vorspann, sonst verweigert der Vorspann. Für das Register schlage
   ich vor: `stufe2.eichen ← biotop.__main__:main @ stufe2` und `eichung.laufzeit_einmal ← biotop.organe.stufe2:eichen
   @ stufe2`.“
3. Fixture `fund_vorspann` in `tests/test_nachweis_verbraucher.py` ohne Siegel. Ein dreizeiliger Vorschlag steht in
   `bau/S3-GEAENDERTE-TESTS.md`.

## Aufgaben
1. **Befehlszeile**
   - `biotop stufe2 <lauf>` ruft `stufe2.eichen(con, lauf)`. `stufe2.Stufe2Fehler` kommt ins `except` von `main`
     (Exit 1 mit Meldung).
   - `biotop tor4 <lauf> --altlasten … [--regression …] [--verdrahtung …] [--review …] [--zwischenbericht …]` reicht
     `belege` an `tor4.ausfuehren`. Die Schlüssel entnimmst du `biotop/tor4.py`.
   - Dazu Unit-Tests: Exit-Codes, Meldungen, Belege kommen an.
2. **Drahtwerk und Verdrahtungslauf**
   - `REFERENZLAST_STUFE2` bekommt eine W-Zeile (Format siehe `biotop/organe/stufe2.py`). Der Schritt `["stufe2", "1"]`
     kommt vor `["vorspann", "1"]`.
   - **Eine echte Verhandlung.** Die gestellte Grenze erzeugt einen Kandidaten, der einen Vertrag benennt und die
     Verhandlung auslöst. Der Nachbar antwortet auf „VERHANDLUNG (3.8 Schritt 2)“ mit einer Anpassung, sodass
     `aegis.pruefen` das Paar aus `lauf._verhandeln` prüft. Der Test sichert zu:
     - `verhandlung.begonnen`;
     - `verhandlung.paar` mit Anpassung und Urteil;
     - danach `verhandlung.bestanden` oder `verhandlung.gescheitert`. Welches von beiden, legst du fest und begründest es.
     - Das Urteil des Paars hat den Verhaltensvergleich durchlaufen (Vorbedingung 4).
   - **Angriffstests in der Generation** (Vorbedingung 9, Tor-4-Zeile 8): Für mindestens einen Kandidaten antwortet die
     gestellte Grenze auf Ansage und Angriff mit einem TypeScript-Angriffstest, sodass `aegis.behauptung` in der Phase
     `generation` läuft. Einen Fund mit Immuntest auf dem TypeScript-Pfad (Tor-4-Zeile 9) baust du, wenn er ohne
     Schwächung einer bestehenden Zusicherung geht. Sonst wird er ein offener Punkt mit Grund.
   - **Bestehende Zusicherungen** bleiben: Jury-Gleichstand, Ablehnung von `gesamt_leer_falsch` durch den
     Verhaltensvergleich, A1, Nachspiel, tor4 über die Befehlszeile. Jede Änderung steht mit Grund in
     `bau/S4-GEAENDERTE-TESTS.md`.
   - **Verdrahtungsbeleg:** Er trägt zusätzlich `kern_commit` (`git rev-parse HEAD`) und `baum_sauber` (ob
     `git status --porcelain` leer ist).
3. **Register vollständig (Entscheidung 6)**
   - **Ableitung:** Das Register folgt aus den 14 Tor-4-Zeilen und den Vorbedingungen 1–11: je verlangter Funktion eine
     Kante „funktion ← aufrufer @ phase“. Mindestens enthalten sind:
     - die Verhandlung: `aegis.pruefen ← biotop.lauf:_verhandeln @ generation`;
     - Generation 0 (Mutantenfang, Typbau, Neutralzähler), der Neutralzähler je Organ, die Behauptung aller
       Angriffstests, die Immunisierung;
     - die Eichphase: S3-Vorschlag oben, am tatsächlichen Aufrufer geprüft;
     - jede der 14 Zeilenfunktionen des Tor-4-Skripts.
   - **Modulinterne Aufrufe:** Du entscheidest und begründest, ob das Register den äußeren Aufrufer nennt (etwa
     `tor4.zeile_aufnahme ← biotop.__main__:main @ tor4`) oder ob der Aufzeichner zusätzlich direkte modulinterne Kanten
     schreibt.
   - **Ausnahmen:** Was im Verdrahtungslauf keine Kante sein kann, etwa ein reiner Ausfallweg, steht als gezählte
     Ausnahme mit Grund und Unit-Test in `register.py`, nie still weggelassen. Der Beleg nennt „x Einträge als Kante,
     y als Ausnahme“.
   - **Gegenprobe:** je Art von Eintrag ein gestellter Wegfall (Aufruf entfernt). Der Test meldet genau diesen Eintrag.
4. **Aufzeichnung:** Module, deren Funktionen das Register verlangt, kommen in `register.MODULE`. Belege mit einem Test,
   dass die Aufzeichnung den Lauf nicht verändert (gleiche Schritte, gleiche rc).
5. **Typsieb (Tor-4-Zeile 3):** Stelle fest, wo Mutanten vorab verworfen werden: im Kern oder im Mutantenplan, den
   Hermes setzt.
   - Die Verteilung je Art kommt als `vorab_verworfen` (dict je Art) in `generation0.begonnen`; so liest es
     `tor4.zeile_generation_0`.
   - Ohne Angabe steht dort `vorab_verworfen: null` mit Grund. Zeile 3 bleibt dann „nicht belegt“, nie erfüllt.
6. **Kernstand zwischen Eichphase und Vorspann (Entscheidung Hermes).** Weicht der Kernstand beim Vorspann vom
   Kernstand der Eichphase ab, **verweigert** der Vorspann, statt nur zu protokollieren.
   - Begründung: Satz 2, eine Messgerätänderung zwischen Eichung und Messung.
   - Die Verweigerung kommt vor jeder Messung und verbraucht den Eichversuch nicht, wie die Verweigerung ohne Siegel.
   - Dazu ein Test mit Gegenprobe (gleicher Kernstand: kein Einwand).
7. **Fixture `fund_vorspann`:** versiegeln nach S3s Vorschlag, mit Grund.

## Rote Spezifikationen, Teillauf, Lieferung
1. **Zuerst die Spezifikationen** für die Aufgaben 1, 3, 5 und 6 in `tests/test_vor_t4_06_register.py`. Den Vorher-Lauf
   fährst du an einer Kopie von HEAD `0c2f058` mit S2 und S3, Ausgabe `bau/S4-VORHER.txt`. Erwartet: jede Probe ist rot
   an ihrer Zusicherung, jede Gegenprobe grün.
2. **Umbau** mit den Bauskripten `bau/r6_s4_*.py`.
3. **Teillauf** (`bau/TEILLAUF-S4.txt`):
   - im echten Baum: deine Unit-Tests, die schnellen Tests von `tests/test_verdrahtung.py`, dazu `test_vorspann.py`,
     `test_stufe2_eichphase.py`, `test_tor4_zeilen.py` und `test_nachweis_verbraucher.py`;
   - der **volle Verdrahtungstest** an einer Kopie: `git archive HEAD` plus die fertigen Dateien von S2, S3 und dir,
     ohne den halben Stand von S1, und ohne `tests/test_vor_t4_06.py`.
   - **Kammer ruhig:** Vor dem vollen Verdrahtungstest prüft ein Skript, dass kein fremder Container läuft
     (`docker ps`), und schreibt das ins Protokoll. Läuft einer, wartest du im Vordergrund in Stücken unter 600 s,
     höchstens 30 min. Grund: Rauschmessung und Eichphase messen Zeiten.
   - Alles grün, oder jede Abweichung ist erklärt.
4. **Weitere Dateien:**
   - `bau/S4-UMSETZUNG.md`: je Aufgabe Umsetzung, Nachweis und Grenzen;
   - `bau/S4-GEAENDERTE-TESTS.md`;
   - `bau/S4-PLAN.md`.
5. **Schlussbericht** (deine letzte Antwort):
   - geänderte Dateien mit sha256;
   - Vorher (x von y rot);
   - Teststand x von y;
   - Register: Einträge als Kante und als Ausnahme, fehlend im vollen Lauf;
   - offene Punkte;
   - Sperren (wörtlich).
