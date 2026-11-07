# Kasse Behebungsrunde 3 vor T4

- **Biotop-Modellgeld: 0,00 €.** Kein Aufruf eines Modellanbieters durch Biotop: In allen Proben, Tests und Nachspielen ist
  die Anbietergrenze gestellt (Proben: `aegis.aufrufen` → „KEIN ANGRIFF“; Nachspiele: aufgezeichnete Ansagen,
  `nachspiel.AufgezeichneteGrenze`). Verdrahtungstest am Commit `d54bf2f`: `modellkosten_eur` 0.0
  (`VERDRAHTUNG-BELEG-REGRESSION.json`).
- **Kein Lauf.** Nur Kammerläufe (netzlos) für Tests, Proben, Nachspiele und Gegenzeugen.
- **T3-Lauf-DB nur gelesen:** Die Nachspiele arbeiten an Kopien unter `/tmp`; jeder der 10 Nachspiel-Belege trägt
  `quelle_db_sha256_vorher` = `quelle_db_sha256_nachher` (10 von 10 gleich).
- **Versiegelter Ordner** `/root/versiegelt/t3-versandwerk/` nur gelesen: sha256 aller Dateien vorher = nachher
  (`GEGENZEUGEN-DOPPELT.json`, `_meta.siegel_unveraendert`).
- Nicht in dieser Kasse: die Tokens von Hermes selbst (Arbeit und Review) — kein Biotop-Modellgeld.
