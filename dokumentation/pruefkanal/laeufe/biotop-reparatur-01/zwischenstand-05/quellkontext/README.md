# Biotop — INFINITE EVOLUTION

Der Python-Code liegt in `biotop/`, die eigene automatisierte Testsuite in `tests/`.
Das sind **Tests des Biotops**, nicht die Tests eingespielter Übungswerke.

## Eigen-Tests ausführen

```sh
uv venv .venv
uv pip install --python .venv/bin/python -r requirements-test.txt
.venv/bin/python -m pytest --collect-only -q
.venv/bin/python -m pytest -q
```

`pytest.ini` macht `tests/` vom Repository-Stamm aus auffindbar. Laufdaten,
Archive und historische Prüfskripte werden nicht versehentlich gesammelt.
Die Eigen-Tests verwenden temporäre Datenbanken. Netzaufrufe sind standardmäßig
im Testprozess gesperrt; es werden keine Modellkosten durch Eigen-Tests erzeugt.

Echte Kammer-/Eichungsprüfungen benötigen Docker und das Image `biotop-kammer:1`.
Unit-Test-Doubles sind kein Nachweis einer solchen Ausführung; deren Rohdaten
werden im jeweiligen Prüfkanalauftrag gesondert geliefert.

## Messungen und Startvoraussetzungen

Ein Maß-/Messgerätwechsel darf keine alte Lauf-ID fortsetzen. Abfolge:
Aufnahme → Landkarte/Verfassung/Verträge → verbindlicher Vorspann → Generation 0
→ Maß einfrieren → Generationen. `python -m biotop --help` zeigt die CLI.
Das harte Auftragsbudget gilt über alle zum Auftrag gehörenden Läufe,
nicht erneut je Einzelversuch.
