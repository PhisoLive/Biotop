# Kasse Behebungsrunde 5 vor T4

- **Biotop-Modellgeld: 0,00 €.** Kein Aufruf eines Modellanbieters durch Biotop. In allen Proben, Tests und
  Nachspielen ist die Anbietergrenze gestellt:
  - Proben und Tests: `aegis.aufrufen` → „KEIN ANGRIFF“;
  - Nachspiele: aufgezeichnete Ansagen (`nachspiel.AufgezeichneteGrenze`);
  - Verdrahtungstest: gestellte Grenze (`GestellteGrenze`).
- Verdrahtungstest am Commit: `modellkosten_eur` 0.0 an `0c2f058` (Regression) und am Arbeitsbaum (`VERDRAHTUNG-BELEG-TEILLAUF3.json`) (`VERDRAHTUNG-BELEG-REGRESSION.json`).
- **Kein Lauf.** Nur netzlose Kammerläufe, und zwar für:
  - Tests, Proben und Nachspiele;
  - die Bemessung der Stufe-2-Last (`proben/STUFE2-EICHUNG.*`);
  - die Messung in T4-Größe (`proben/T4-GROESSE.txt`).
- **T3-Lauf-DB nur gelesen.** Die Nachspiele und die Stufe-2-Eichung arbeiten an Kopien unter `/tmp`.
  `STUFE2-EICHUNG.txt` meldet „t3.db unverändert: True“. Jeder Nachspielbeleg trägt `quelle_db_sha256_vorher` und
  `quelle_db_sha256_nachher`: vorher = nachher in 8 von 8 Belegen dieser Runde (n1–n3 am Commit, Vorprobe am Arbeitsbaum).
- **Versiegelter Ordner** `/root/versiegelt/` wurde in dieser Runde nicht berührt.
- Nicht in dieser Kasse: die Tokens von Hermes selbst (Arbeit und Review). Das ist kein Biotop-Modellgeld.
