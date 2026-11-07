# Kasse — Behebungsrunde 2 vor T4

Biotop-Modellgeld: **0,00 €**. Dieser Auftrag hat keinen Lauf gestartet und kein Modell für das Biotop aufgerufen.

- **Lauf-DB T3:** nur gelesen (`mode=ro`), sha256 von `t3.db` vor und nach der S1-Messung gleich
  (`7a31b8a3…`, `s1/S1-STAENDE.json` → `_meta`). Die Nachspiele arbeiten an einer Kopie unter /tmp; die Belege tragen
  `quelle_db_sha256_vorher/nachher` und `modellaufrufe_echt`.
- **Nachspiele:** gestellte Anbietergrenze, die nur aufgezeichnete Ansagen beantwortet. Der Prozess hat kein Netz.
- **Einheits-, Kammer- und Verdrahtungstests:** gesperrtes Netz, gestellte Grenze (`tests/conftest.py`).
- **Kammerläufe (Docker, netzlos):** kein Modellgeld, nicht gezählt.
- **Review:** ein Unteragent des Trägers (Anthropic-Anmeldung des Trägers, nicht Biotop-Budget), ohne Modellaufrufe
  für das Biotop. Der Betrag ist nicht beziffert.

Stand des Auftrags T3 (unverändert): 9,728638 € von 10,00 €.
