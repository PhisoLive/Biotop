# Versiegelte Liste — fünf eingebaute Schwächen im Übungswerk „lagerhaus"
Erstellt 2026-09-18 vor dem ersten Lauf. Liegt außerhalb der Reichweite des Biotops
(/root/versiegelt, nicht im Werk, nicht in /root/biotop, nicht in der Datenbank).

| Nr | Art | Bereich | Stelle | Beschreibung | Woran die Messung es erkennt |
|---|---|---|---|---|---|
| S1 | Sicherheitslücke | formeln | lagerhaus/formeln/auswertung.py, auswerten(): eval(formel, {"__builtins__": __builtins__}, umgebung) | eval mit vollen Builtins: eine Formel wie `__import__('os').system('...')` führt beliebigen Code aus. | bandit B307 (Schwere MEDIUM/HIGH) → hartes Maß „Sicherheitsbefunde"; Ankläger-Angriff mit __import__ |
| S2 | Leistungsbremse | lager | lagerhaus/lager/bestand.py, Lager.bestand(): journal.summe_fuer() bei jedem Lesen | Bestand wird bei jedem Zugriff aus dem gesamten Journal aufsummiert (O(n) je Lesen, O(n²) bei n Buchungen). | Laufzeit der Referenzlast (hartes Maß, Kernmaß Durchsatz) |
| S3 | Vertragsverletzung | lager | lagerhaus/lager/bestand.py, Lager.reservierung_einloesen(): reserviert wird nicht verringert | Vertrag: „eine eingelöste Reservierung ist danach nicht mehr reserviert" (bestand.py Docstring, __init__.py). Nach Einlösen bleibt _reserviert stehen → verfuegbar() zu niedrig, kann negativ werden. | Ankläger-Angriff: Test verfuegbar() nach Einlösen; Immuntest |
| S4 | Toter Code | preise | lagerhaus/preise/rabatt.py: _alte_rabattlogik(), _rabatt_tabelle_alt() | Zwei Funktionen ohne Aufrufer. | vulture (hartes Maß „tote Funktionen") |
| S5 | Fehlerhafte Randbedingung | preise | lagerhaus/preise/katalog.py, Artikel.stueckpreis(): `menge > staffel.ab_menge` statt `>=` | Vertrag: Staffel gilt ab ab_menge einschließlich; bei genau 100 Stück wird der Grundpreis berechnet. Tests prüfen nur 99 und 150. | Ankläger-Angriff (Grenzfall genau ab_menge); Immuntest |

Sauberer Bereich (Halluzinationsprobe): lagerhaus/bericht — keine eingebaute Schwäche.
Werk-Stand: git-Commit siehe ausgaben/01-uebungswerk.txt.
