# Übergabe: Behebungsrunde vor T4 (Stand 2026-09-23, ca. 21:42, Sitzung 20260923_194003_92313ee1)

Auftrag (Philipp, 23.09., zweite Fassung nach Kontextüberlauf): Träger Opus 5.5 + Denkstufe max als Grundwert, belegt am
Anfragekörper; Verdichtung prüfen. Review-Befunde → eigener Commit nach 58bd9f9 mit voller Regression. Geklärt in den
Bericht: (1) K2868/S1, (2) Gegenprobe Gedächtnissperre-Test. Wächter: Auslöser 80 % Kontext + gescheiterte Verdichtung,
mit Gegenprobe. Dann laeufe/biotop-vor-t4/ veröffentlichen, Endmeldung mit Abholadresse + Prüfsumme.

## Erledigt
- Träger: traeger/TRAEGER-BELEG.json (config gesichert, model.default claude-opus-5-5/anthropic, effort max; Anfragekörper
  model claude-opus-5-5, thinking adaptive, output_config.effort max; Verdichtungsroute ok). Kein Neustart nötig
  (Gateway liest config je Turn); der laufende Chat hat zusätzlich einen persistierten /model-Override (gleiches Modell).
- S1: s1/S1-KLAERUNG.json, s1/S1-DECKUNG.json. Grammatik mit Leerzeichen: 0 Abweichungen bei 93.320 Fällen mit Wert;
  86 nur bei Division durch null (alt vertragswidrig). Tab/Zeilenumbruch: neu weist 12.206 von 16.166 ab, die alt und
  Normalversion gleich rechnen → S1 NICHT sauber behoben. Deckende Tests: 4 von 4 (alt rot, neu grün); Weißraum-Spez:
  alt grün, neu rot, Referenz grün. Funktionsebene deckt eine konstruierte Weißraum-Abweichung mit (Lücke Grundsatz 11).
- Sperre: sperre/SPERRE-GEGENPROBE.json — schreib_aus allein grün (blind, Lesestelle hält), lese_aus rot (review11),
  beide_aus rot (test_10 2 Zeilen + review11), immer/nie rot, ohne ts-Image 4 von 4 übersprungen.
- Wächter: ~/.hermes/scripts/zwischenbericht_waechter.py erweitert (Sicherung *.vor-kontext-20260923-212241),
  Tests 12 von 12 grün, Gegenproben 10 von 10 an der vorgesehenen Stelle (waechter/GEGENPROBEN.json), Nachspiel echte
  Sitzung (waechter/NACHSPIEL-ECHTE-SITZUNG.json): erster Auslöser 16:01 (Verdichtung), 16:48 (80,6 %); alter Auslöser
  (Runden) nie (höchste Runde 77 von 150). Herzschlag vom cron.scheduler zeigt kontext-Feld (21:35).
- Commit 330b4ec (Review-Befunde) auf 58bd9f9, COMMIT2-STAT.txt, KERN-COMMIT2.patch.txt.

## Läuft (erledigt, Ergebnisse im BERICHT eingetragen)
- job_commit2_regression.sh (proc_96f705bab38f): volle Regression an 330b4ec → REGRESSION2-VOR-T4.txt/.junit.xml,
  dann Nachspiele am Commit → nachspiel2/ + NACHSPIEL2-AM-COMMIT.txt, dann PYTHON-LAUFZEIT-PROBE.json.

## Offen
1. Ergebnisse eintragen, BERICHT.md fertig (‹…›-Platzhalter), veroeffentlichen.py QUELLEN ergänzen, veröffentlichen.
2. Endmeldung: BERICHT.md- und DATEIEN.txt-URL je als ganze Zeile + Ordnerprüfsumme.

## Stand 22:30
- Alles gemessen und im BERICHT eingetragen (0 Platzhalter). Nachlese: K2904 in Durchgang 2 abgelehnt (eingang ×1,224,
  unberührt), Durchgang 3 überlebt; Python-Teilausfall der gepaarten Messung → rote Spezifikation spez/.
- Nächster Schritt: `python3 veroeffentlichen.py` (Ziel laeufe/biotop-vor-t4/, enthält nur zwischenbericht-*-Ordner),
  dann Endmeldung mit BERICHT.md- und DATEIEN.txt-URL als ganze Zeilen + PRUEFSUMME-ORDNER.
