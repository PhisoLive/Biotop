# Kasse Behebungsrunde 4 vor T4

- **Biotop-Modellgeld: 0,00 €.** Kein Aufruf eines Modellanbieters durch Biotop. In allen Proben, Tests und
  Nachspielen ist die Anbietergrenze gestellt:
  - Proben: `aegis.aufrufen` → „KEIN ANGRIFF“;
  - Nachspiele: aufgezeichnete Ansagen (`nachspiel.AufgezeichneteGrenze`).
- Verdrahtungstest am Commit: `modellkosten_eur` 0.0 an `1d9a5aa` und an `43b8fad` (`VERDRAHTUNG-BELEG-REGRESSION.json`).
- **Kein Lauf.** Nur netzlose Kammerläufe, und zwar für:
  - Tests, Proben und Nachspiele;
  - die Stufe-2-Zeitmessung (`proben/STUFE2-ZEITEN*`).
- **T3-Lauf-DB nur gelesen.** Die Nachspiele und `proben/stufe2_zeiten.py` arbeiten an Kopien unter `/tmp`. Jeder
  Nachspielbeleg trägt `quelle_db_sha256_vorher` = `quelle_db_sha256_nachher` (15 von 15);
  `STUFE2-ZEITEN.json` trägt `t3_db_vorher` = `t3_db_nachher`.
- **Versiegelter Ordner** `/root/versiegelt/t3-versandwerk/` wurde in dieser Runde nicht berührt. Die
  Torzeile-Auswertung liest nur die unversiegelten Messungen der Vorrunden.
- Nicht in dieser Kasse: die Tokens von Hermes selbst (Arbeit und Review). Das ist kein Biotop-Modellgeld.
