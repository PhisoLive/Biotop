# Bauauftrag S2 (Runde 6, Entscheidung 5): Tor-4-Skript berechnet jede Torzeile

Du baust einen Teil der Behebungsrunde 6 vor T4 des Biotop-Projekts. Antworte und schreibe auf Deutsch. Du setzt NUR das
Folgende um, committest nichts und startest keine Hintergrundprozesse (nur Vordergrundbefehle ≤ 600 s).

## Umgebung
- Code `/root/biotop` (git, HEAD `0c2f058`, NICHT committen), Python `/root/biotop-t3/venv/bin/python`,
  Tests `cd /root/biotop && /root/biotop-t3/venv/bin/python -m pytest <datei> -q -p no:cacheprovider -rfE`.
- Arbeitsordner `/root/biotop-vor-t4-06/` (Unterordner `bau/`), eigener Temp-Ordner `/tmp/r6-s2/` (setze `TMPDIR`).
- Parallel arbeiten zwei andere Bauende im selben Baum: fasse NUR deine Dateien an (unten). Kein Modellaufruf, kein Netz.
- Lange oder mehrteilige Befehle als Skript unter `/tmp/r6-s2/`. Wird ein Befehl gesperrt (Sicherheitssperre,
  Freigabeabfrage), hältst du an und berichtest Befehl und Meldung wörtlich.

## Deine Dateien (nur diese)
- `biotop/tor4.py` (vorhanden, 145 Zeilen: berechnet bisher nur „Schwächen“, übrige Zeilen „nicht berechnet“).
- neu `tests/test_tor4_zeilen.py`.
- Nicht anfassen: `biotop/__main__.py` (die Befehlszeile verdrahte ich), `tests/test_verdrahtung.py`, `tests/drahtwerk.py`.

## Auftrag (Entscheidung Chat-Claude 5, 24.09.)
„Tor-4-Skript: jede Zeile berechnet, die drei nicht aus der Datenbank berechenbaren aus ihren Belegdateien; der Zweig
für verhaltensändernde Altlasten muss erreichbar sein.“ Die meisten Berichtsfehler in T3 waren Torzeilen von Hand.

Tor 4 (Masterprompt Fassung 8, Wortlaut in `/root/biotop-vor-t4-05/bau/MASTERPROMPT-V8-TOR4.txt`, Zeilen 3–17), 14 Zeilen:
1 Aufnahme · 2 Generation minus eins · 3 Generation 0 · 4 Schwächen (schon gebaut) · 5 Kein Rückschritt ·
6 Halluzinationsprobe · 7 Verhaltensvergleich · 8 Doppelungsanteil · 9 Immunisierung · 10 Neutralzähler ·
11 Verbundausfall · 12 Verdrahtung · 13 Sättigung oder Budgetabbruch · 14 Reviewdurchgang und Zwischenbericht.
- Aus der Datenbank: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13.
- Aus Belegdateien: 1 (Altlastenliste mit Bezugsgröße + Aufnahmebericht des Werks in `werke.bericht`), 12 (JUnit-XML der
  vollen Regression + Verdrahtungsbeleg-JSON), 14 (`REVIEW.md` + Zwischenbericht-Nachweis).

## Schnittstelle (fest, ich verdrahte danach Befehlszeile und Verdrahtungstest)
- `ausfuehren(con, lauf_id, altlasten_pfad, belege: dict | None = None) -> dict`; `belege` mit optionalen Schlüsseln
  `regression` (Pfad JUnit-XML), `verdrahtung` (Pfad JSON), `review` (Pfad REVIEW.md), `zwischenbericht` (Pfad einer
  JSON- oder Textdatei mit den Zwischenbericht-Nachweisen). Fehlt ein Beleg: Zeile berechnet mit `erfuellt: None` und
  Grund „Beleg fehlt: …“ — nie erfüllt.
- Rückgabe behält die bisherigen Schlüssel (`lauf`, `endstand`, `schwaechen`, `altlastenliste`) und ersetzt
  `nicht_berechnet` durch `zeilen`: `{name: {"zeile": str, "erfuellt": True|False|None, "nenner": str, "quelle": str,
  "einzelheiten": {...}}}` für ALLE 14 Zeilen (Namen wie oben, z. B. "Generation minus eins"). Dazu `"nicht_berechnet": []`
  (leer — der Verdrahtungstest verlangt das) und `"gesamt": {"erfuellt": x, "nicht_erfuellt": y, "nicht_belegt": z}`.
- Protokoll: zusätzlich `protokoll.schreiben(con, "tor4.zeilen", lauf_id=…, zeilen=…)`.
- Je Zeile eine eigene Funktion `zeile_<kurzname>(con, lauf_id, …)`; ich trage sie ins Register der verlangten Aufrufe ein
  (Aufrufer `biotop.tor4:ausfuehren`, Phase `tor4`) — rufe sie also direkt aus `ausfuehren` auf.
- Regel für jede Zeile: fehlt die Datengrundlage (z. B. keine Generation 0 im Lauf), ist das `erfuellt: None` mit Grund,
  nie `True`. Jede Zahl mit Nenner („x von y“). Null Fälle sind keine Mehrheit und kein Erfolg.

## Zeilendefinitionen (Vorschlag; wo die Daten es nicht hergeben, begründet abweichen und in der Definitionsdatei nennen)
Lies zuerst: `biotop/kern/datenbank.py` (Schema), `biotop/organe/vorspann.py` (Nachweis in `vorspann_nachweise.ergebnis`),
`biotop/organe/generation0.py` (Protokollart `generation0.ergebnis` u. a.), `biotop/organe/neutralzaehler.py`
(`stand`, `traegt_torzeile`), `biotop/organe/eichung.py` (Tabelle `eichkosten`), `pruefung/tor2.py`, `pruefung/tor3.py`
(frühere Torskripte als Vorbild), `biotop/organe/aegis.py` (Protokoll `aegis.urteil` mit `verhalten`, `laufzeit_gepaart`,
Behauptungen, `immun.*`), `biotop/lauf.py` (`freigabe`, `letzte_angenommene`, Entropie/Sättigung, Kasse).
- 2 Generation minus eins: Vorspann-Nachweis `bestanden`; Rauschmessung mit Sperren je Bereich ausgewiesen; Maßeichung
  vorhanden, stillgelegte Regeln mit Befundzahl; Eichgegenstand versiegelt; Eichproben 4 von 4 bestanden und 4 von 4
  Gegenproben gescheitert; Eichkosten getrennt gebucht (Tabelle `eichkosten`).
- 3 Generation 0: Mutantenfang ≥ 80 von 100 nicht-äquivalenten (je Art ausgewiesen, Verteilung des vorab Verworfenen);
  kein Durchlauf mit überwiegend neutralem Urteil geht ein (Neutralzähler je Durchlauf).
- 5 Kein Rückschritt: 0 von n angenommenen Generationen mit gesunkenem hartem Maß je Maßfeld einschließlich Laufzeit
  (gepaart gemessen, `aegis.urteil`/`generationen.masse`).
- 6 Halluzinationsprobe (streng): im sauberen Vergleichsbereich (Verfassung/Maßeichung) keine angenommene Änderung, außer
  belegt durch einen Test, der an der Vorgeneration fällt und am Kandidaten besteht.
- 7 Verhaltensvergleich: jede angenommene Generation hat ihn durchlaufen (je gewähltem Kandidaten `verhalten.geurteilt`),
  je Urteil „x von y Funktionen beobachtet“; Enthaltungen zählen nicht als bestanden.
- 8 Doppelungsanteil < 20 %: alle erzeugten Angriffstests, geurteilt nach ihrer geschriebenen Behauptung (Protokoll der
  Behauptungen, vgl. `pruefung/doppelungen_neu.py`).
- 9 Immunisierung: für die Sprache des Werks auf dem tatsächlichen Pfad gezählt; 0 Fälle = nicht belegt.
- 10 Neutralzähler: jedes Organ mit Nenner; eine Torzeile, die an einem Organ hängt, gilt nur bei Mehrheit geurteilter
  Fälle — je Durchlauf.
- 11 Verbundausfall: als Ausfall gezählt, nie als Beitrag; belegt an mindestens einem echten oder gestellten Ausfall.
- 13 Sättigung oder Budgetabbruch dokumentiert (Protokoll `entropie.saettigung`, `kasse.abbruch`, `lauf.abgebrochen` …).
- 1 Aufnahme: Werk gebaut, Bau- und Testlauf (Aufnahmebericht), Altlastenliste mit Bezugsgröße und ≥ 1 Eintrag.
- 12 Verdrahtung: JUnit ohne failure/error, mit `tests/test_verdrahtung.py`; Verdrahtungsbeleg `nie_gerufen` leer und
  `register.fehlend` leer; Kernstand: trägt der Beleg `kern_commit`, muss er zum Lauf passen (Lauf-Kernstand aus dem
  Vorspann-Nachweis `quellen`, falls ableitbar; sonst Grund nennen).
- 14 Reviewdurchgang und Zwischenbericht: `REVIEW.md` vorhanden mit Befundtabelle; Zwischenbericht-Nachweis vorhanden.

## Zweig „verhaltensändernde Altlast“ (Review 05 Nr. 8: heute unerreichbar)
- Der unabhängige Test der Altlast (`unabhaengiger_test`: `{"datei": "tests/…", "code": "…"}` ODER eine Kennung eines
  Tests aus der Liste) läuft in der Kammer am Endstand (muss bestehen) und am Ausgangsstand (Lazarus-Generation 0, muss
  fallen). Nur dann gilt die Verhaltensänderung als durch ihn gedeckt; `normal` zählt die Abweichungen der angenommenen
  Kandidaten, die NICHT durch diesen Test der eigenen Altlast gedeckt sind (`erlaubt` je Altlast, nicht über alle).
- Kennungen einheitlich vergleichen (`tests/test_x.py::name` und `test_x.py::name` sind dieselbe).
- Ohne unabhängigen Test: nicht beurteilbar (wie bisher). Nicht verhaltensändernd: wie bisher.
- `aegis.junit_lauf(ziel, paket, {datei: code}, [datei])` ist der Kammerlauf; in Unit-Tests darfst du ihn stellen.

## Tests (`tests/test_tor4_zeilen.py`, ohne Modell; Kammer nur, wo nötig)
- Je Zeile: ein erfüllter Fall, ein nicht erfüllter Fall, ein Fall ohne Datengrundlage (→ `None`), an einer synthetischen
  DB (`datenbank.SCHEMA` + nötige Tabellen/Protokolleinträge).
- Altlast-Zweig: verhaltensändernd mit unabhängigem Test (am Ende besteht, am Anfang fällt) → behoben; ohne Test → nicht
  beurteilbar; Test fällt auch am Ende → nicht behoben; Kennungsform mit und ohne `tests/`.
- `ausfuehren` liefert 14 von 14 Zeilen, `nicht_berechnet == []`.

## Lieferung
- Umbau als alles-oder-nichts-Skript `bau/r6_s2_tor4.py` (liest, ersetzt/schreibt, bricht ohne Schreiben ab, wenn ein
  Anker fehlt; Protokoll `bau/R6-S2-TOR4.txt`). Neue Dateien darf das Skript anlegen.
- Testlauf `tests/test_tor4_zeilen.py` und `tests/test_vor_t4_05.py -k "register or tor4"`-freie Dateien wie
  `tests/test_gegenzeugen*.py` (falls vorhanden), Ausgabe nach `bau/TEILLAUF-S2.txt` (ein `-q`, `-rfE`).
- `bau/TOR4-ZEILEN-DEFINITION.md`: je Zeile Definition, Datenquelle, Nenner, Abweichungen vom Vorschlag mit Grund.
- Schlussbericht (deine letzte Antwort): geänderte Dateien, Teststand x von y, offene Punkte, Sperren (oder „keine“).
