# Bauauftrag S1b (Runde 6): Abschluss von S1 und der letzte gemessene stille Durchlass (M2(b))

Du setzt den Bau S1 der Behebungsrunde 6 vor T4 fort. Antworte und schreibe auf Deutsch. Der Vorgänger (S1-Fortsetzung)
hat an der Iterationsgrenze aufgehört. Sein Stand ist unten gemessen. Seine Überlegungen stehen in
`/root/biotop-vor-t4-06/bau/S1-PLAN.md`; lies dort vor allem die Abschnitte ab „Grenzen gemessen (07:15)“ bis zum Ende.

## Stand (gemessen 25.09. 08:34, `bau/PRUEFE-S1.txt`)
- **Gebaut:** die Entscheidungen 7, 1, 2 und 3 samt Nachträgen.
- **Prüfsummen im Baum:**
  - `biotop/kern/py/verhalten.py` `c4071c40…`
  - `biotop/organe/verhaltensvergleich.py` `7d87cc1b…`
  - `tests/test_vor_t4_06.py` `ec60919a…` (74 Fälle)
- **Teillauf Durchgang 3** (`bau/TEILLAUF-S1.txt`): Aufrufe 1–8 mit 288 von 288 grün. Stück 9
  (`tests/test_tor4_zeilen.py`) fehlt.
- **Vorher an `0c2f058`:** 57 von 74 rot. Das umfasst 47 von 63 ursprünglichen Fällen und 10 von 11 `test_u2n_*`.
- **Fehlende Lieferteile:**
  - `bau/S1-UMSETZUNG.md`
  - die Zusammenfassung von Durchgang 3 in `bau/TEILLAUF-S1.txt`
  - die Einordnung der `u2n`-Fälle in `bau/S1-VORHER-EINORDNUNG.md`
  - `bau/S1-GRENZEN-MESSUNG.txt`
- **Offen, gemessen um 07:42 an der Kopie nach E3 — ein stiller Durchlass:** Eine öffentliche Funktion liefert die
  Instanz einer privaten Klasse, der Kandidat ändert `_Konto.buchen`. Ergebnis: „keine Verhaltensabweichung (1 von 1
  Funktionen beobachtet)“, tragfähig. Die Ausgabedatei ist überschrieben; neu messen.
- **Andere Bauende im selben Baum:** S4 baut noch. Nicht anfassen: `biotop/__main__.py`, `biotop/kern/register.py`,
  `biotop/lauf.py`, `biotop/organe/vorspann.py`, `tests/test_verdrahtung.py`, `tests/drahtwerk.py`,
  `tests/test_nachweis_verbraucher.py`, `tests/test_vor_t4_06_register.py`. Ebenso die fertigen Dateien von S2
  (`biotop/tor4.py`, `tests/test_tor4_zeilen.py`) und S3 (`biotop/organe/stufe2.py`, `tests/test_stufe2_eichphase.py`).

## Warum M2(b) in diese Runde gehört (Entscheidung Hermes, nach der Startregel)
- **Startregel für T4**, vorab gesetzt: „T4 beginnt, sobald das Review dieser Runde keinen stillen Durchlass mehr findet
  — jede bekannte Lücke muss eine gezählte Enthaltung sein; Lücken, die sich nur enthalten, behebt T4 im Lauf.“
- **Philipp, 25.09.:** Ein stiller Durchlass „gehört mit Gegenprobe in diese Runde“.
- **Grundlage:** Vorbedingung 2 aus Masterprompt v8 lautet „unbeobachtet = Enthaltung“. Entscheidung 3 von Chat-Claude
  lautet „Enthält sich eine geänderte Funktion, wird der Kandidat zurückgestellt“.
- **Mein Fehler:** Der erste Bauauftrag engte das auf „unvollständig erfasst, Sondenausfall, Zeitgrenze“ ein. Diese
  Engführung hebe ich hier auf.

## Teil B — M2(b) bauen (zuerst Spezifikation, dann Bau)
**Regel:** Grundlage ist die Festlegung „M2(b) (07:55)“ in `S1-PLAN.md`, mit einer Klarstellung.
- **D** sind die direkt geänderten Funktionen:
  - eigener Knoten verschieden oder neu;
  - Klassenrest geändert → alle Methoden der Klasse;
  - Modulrest geändert → alle Funktionen des Moduls;
  - entfernte Funktionen zählen nicht.
- **X aus D ist nicht beobachtet**, wenn die Sonde auf mindestens einer Seite keine Beobachtung von X hat (nicht in
  `inhalt`), gleich ob eingewickelt oder nicht. Darunter fallen also auch:
  - Methoden privater Klassen und Dunder-Methoden;
  - private Funktionen;
  - eine öffentliche Funktion, die weder Korpus noch Last erreichen.
- **X ist gedeckt**, wenn alle vier Bedingungen gelten:
  - X ist privat (`_x`) und keine Dunder-Methode;
  - X wird auf Modul- oder Klassenebene nicht genannt (weder als Name noch in Zeichenketten);
  - jede Aufruferin im Modul, deren Körper den Kurznamen nennt, ist beobachtet oder gedeckt;
  - es gibt mindestens eine solche Aufruferin (ein Zyklus zählt als nicht gedeckt).
- **Folge:** Ist X nicht beobachtet und nicht gedeckt, wird es eine gezählte Enthaltung mit dem Grund „betroffen, von der
  Sonde nicht beobachtet (<Grund>)“. Der Vergleich enthält sich (`grund_art` `betroffene_funktion_enthaelt_sich`), und
  `aegis.pruefen` stellt zurück.
- **Wie bisher:** Eine ungedeckte Abweichung lehnt immer ab.
- **Unverändert:** Ist eine unveränderte Funktion nicht erreicht, wird das gezählt und am Rest geurteilt.
- **Transitiv Betroffene** (nur Aufruferinnen) bleiben wie gebaut.

**Spezifikationen** (anhängen an `tests/test_vor_t4_06.py`, Präfix `test_m2_`). Wo das Organ im Annahmepfad wirkt:
durch `aegis.pruefen` in der echten Kammer, wie die bestehenden Fälle.

| Fall | Soll |
|---|---|
| `verdeckt`: öffentliche Funktion liefert eine `_Konto`-Instanz, Kandidat ändert `_Konto.buchen`, die Last ruft `buchen` | zurückgestellt |
| `verdeckt_gegen`: Kandidat ändert nur eine andere öffentliche Funktion, Verhalten gleich | geurteilt, tragfähig |
| `dunder`: `Geld.__add__` geändert, Last `Geld(1) + Geld(2)` | zurückgestellt |
| `dunder_gegen`: nur eine andere Funktion geändert | tragfähig |
| `helfer_gedeckt`: privater Helfer, gerufen von einer beobachteten öffentlichen Funktion, Änderung ohne Verhaltensänderung | tragfähig |
| `helfer_sichtbar`: derselbe Helfer mit Verhaltensänderung | abgelehnt (Abweichung an der Aufruferin) |
| `nicht_erreicht`: geänderte öffentliche Funktion, die Korpus und Last nicht erreichen | zurückgestellt |
| `nicht_erreicht_gegen`: unveränderte, nicht erreichte Funktion | gezählt, tragfähig |
| `wert_verdeckt`: privater Helfer, als Wert zurückgegeben (etwa `_schluessel`), geändert | zurückgestellt |

**Vorher** läuft am aktuellen Baum (nach E3 und den Nachträgen) und an `0c2f058`. Erwartet: Proben rot an ihrer
Zusicherung, Gegenproben grün. Hänge das Ergebnis an `bau/S1-VORHER-0c2f058.txt` an und ordne es in
`bau/S1-VORHER-EINORDNUNG.md` ein.

**Bau:** `bau/r6_s1b_m2b.py`, alles oder nichts, mit zwei Lesungen. Erst an einer eigenen Kopie
(`/tmp/r6-s1b/bau`, `git archive HEAD` plus der aktuelle Stand deiner Dateien), dann am Baum. Danach vergleichst du
die Dateien von Kopie und Baum.

**Kosten** (`bau/S1B-KOSTEN-M2B.txt`, Sonde an der Vorgeneration, Kopie):
- **Übungswerke:** `lagerhaus`, `logmuehle` und das Werk in `/root/uebungswerk-p2`.
- **Je Werk:** x von y Funktionen beobachtet, gedeckt und „würde bei Änderung zurückstellen“, dazu die Liste der
  letzten Art.
- Die Kosten werden nur berichtet. Die Regel ändert sich nicht, wenn die Zahl hoch ist.

## Teil A — fehlende Lieferteile des Vorgängers
1. **Messung der Grenzen:** `bau/S1-GRENZEN-MESSUNG.txt` enthält `verdeckt` und `dunder` am Stand vor deinem Bau, also
   die neue Vorher-Messung aus Teil B, mit Ausgabe.
2. **Teillauf:** Nach Teil B laufen alle Stücke 1–9 von `/tmp/r6-s1/teillauf.sh` neu, als Durchgang 4 in
   `bau/TEILLAUF-S1.txt` mit Zusammenfassung.
3. **Umsetzungsbericht:** `bau/S1-UMSETZUNG.md` enthält je Entscheidung (7, 1, 2, 3, M2(b)) Umsetzung, Nachweis
   (Test und Laufweg), Grenzen und Kosten.
4. **Geänderte Tests:** `bau/S1-GEAENDERTE-TESTS.md` wird ergänzt.

## Teil C — Nebenwirkung abstellen (Entscheidung Hermes)
- `tests/test_t3_eichpfad.py` schreibt ohne `T3_EICH_BELEGE` nach `/root/biotop-t3/eichbau`. Ändere nur den Standard
  auf den `tmp_path` des Tests; die Zusicherungen bleiben unverändert. Einen Grund trägst du in die Liste der geänderten
  Tests ein.
- Die drei Dateien, die dein Vorgänger dort am 25.09. um 06:57–06:59 neu angelegt hat, bleiben liegen (harte Linie 1:
  nichts löschen). Die Geburtszeit (`stat %w`) gleich der Änderungszeit belegt, dass nichts überschrieben wurde.

## Arbeitsweise (verbindlich)
- **Denken:** Plane nie den ganzen Umbau in einem Denkschritt. Plan und Stand stehen fortlaufend in `bau/S1B-PLAN.md`,
  so aktuell, dass ein Nachfolger übernehmen kann. Je Schritt ein Skript, danach die zugehörigen Tests.
- **Laufzeiten:** keine Hintergrundprozesse. Jeder Werkzeugaufruf bleibt unter 400 s; das Werkzeug bricht nach 420 s ab.
  Teile Testläufe in Stücke.
- **Kammer:** Vor jedem Stück mit Kammer prüfst du, dass `/tmp/biotop-kammer-exklusiv` nicht existiert. Existiert es,
  wartest du in Aufrufen unter 400 s.
- **Umgebung:** `TMPDIR=/tmp/r6-s1b`. `T3_EICH_BELEGE` lenkst du immer nach `/tmp/r6-s1b/…`. Python ist
  `/root/biotop-t3/venv/bin/python`, Tests laufen aus `/root/biotop` heraus.
- **Befehle und Sperren:**
  - Mehrteilige Befehle schreibst du von Anfang an als Skriptdatei.
  - Wird ein Befehl gesperrt oder läuft eine Freigabeabfrage ab, wartet genau diese Handlung. Du formulierst nicht um,
    teilst nicht auf, schreibst nicht als Skriptdatei neu und nimmst keinen anderen Weg.
  - Befehl und Meldung trägst du wörtlich in `bau/S1B-PLAN.md` und in den Schlussbericht ein.
- **Verboten:** kein Commit, kein Modellaufruf, kein Netz.
- **Deine Dateien:**
  - `biotop/kern/py/verhalten.py` und `biotop/organe/verhaltensvergleich.py`;
  - `biotop/organe/aegis.py`, nur die Behandlung der Enthaltung;
  - `tests/test_vor_t4_06.py`, nur anhängen und patchen;
  - `tests/test_t3_eichpfad.py`, nur den Standardpfad;
  - in `tests/test_vor_t4_05.py`/`_04.py` nur eigene Tests, wenn sich deren Spezifikation ändert, jeweils mit Grund.

## Schlussbericht (deine letzte Antwort)
- geänderte Dateien mit sha256;
- Vorher der `test_m2_*` (x von y rot);
- Teststand Durchgang 4 (x von y);
- Kosten je Übungswerk (x von y würden zurückstellen);
- offene Punkte;
- Sperren (wörtlich).
