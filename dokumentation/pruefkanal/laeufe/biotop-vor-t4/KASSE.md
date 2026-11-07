# Kasse — Behebungsrunde vor T4

Modellgeld: **0,00 €**. Dieser Auftrag hat keinen Lauf gestartet und kein Modell aufgerufen.

- **Lauf-DB T3:** Sie wurde nicht beschrieben; sha256 von t3.db und t3.db-wal sind gleich wie beim Schnappschuss vom 23.09.
  (t3.db 99a4c7863278ecf3…, t3.db-wal 429866997c07eaaa…).
- **Nachspiele:** Sie liefen gegen eine Kopie des Schnappschusses unter /tmp, bei gesperrtem Netz. Alle Anbieteranfragen
  gingen an eine gestellte Grenze, die nur aufgezeichnete Ansagen beantwortet.
- **Einheits- und Verdrahtungstests:** Sie arbeiten ebenfalls mit gesperrtem Netz und gestellter Grenze
  (`tests/conftest.py`, `GestellteGrenze`).
- **Kammerläufe (Docker, netzlos):** Sie kosten kein Modellgeld. Ihre Zahl ist nicht gezählt.

Stand des Auftrags T3 (unverändert): 9,728638 € von 10,00 €.

## Zweite Sitzung (23.09., 19:40–22 Uhr)

- Biotop-Modellgeld: **0,00 €**. Kein Lauf; die Nachspiele am Commit gingen an die gestellte Anbietergrenze (`modellaufrufe_echt` 0 in den Belegen), t3.db unverändert in 7 von 7 Nachspielen.
- Träger (nicht Biotop): 2 echte Anfragen für den Konfigurationsbeleg (`hermes chat --oneshot`, Verdichtungsroute `call_llm`), über die Anthropic-Anmeldung des Trägers; nicht aus dem Biotop-Budget, Betrag nicht beziffert.
- Kammerläufe (S1-Klärung 2, S1-Deckung 3, Regression, Nachspiele, Python-Laufzeit): kein Modellgeld, nicht gezählt.
