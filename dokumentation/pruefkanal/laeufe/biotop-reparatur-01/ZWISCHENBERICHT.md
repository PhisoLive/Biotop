# Reparatur 01 — Zwischenstand 2026-09-20T13:55:53.926356+00:00

**Nicht abgeschlossen, keine neue Messfreigabe.**

- 49 von 49 bisher integrierten Eigen-Tests bestanden (28-eigentests-zwischenstand.txt/.xml); dies ist NICHT die Vollständigkeit des Reparaturauftrags.
- Drei von drei ausdrücklich gestellten Gegenmutanten in privaten Codekopien machen die zugehörigen Tests rot (27-gegenmutanten.json). Keine normale Generation, keine echte-Bestandsprüfung damit behauptet.
- Die ersten Sperren vor generation/gen0/mass sind rot reproduziert und anschließend grün geprüft. Der noch unfertige Vorspann sperrt im aktuellen Arbeitsstand alles; eine funktionierende Freigaberoute wird separat implementiert und darf nicht als fertig gelten.
- Rauschfehler rot/grün belegt: genau fünf Werte verlangen, ungültige Werte abweisen, Aussetzer ungerundet entfernen, nach erfolglosem einmaligem Ersatz sperren, gemessene Toleranz bis ins Urteil durchreichen, bereichsbezogene Sperre statt globale Blindheit.

## Offen
Norm-Reparatur samt vier Proben und vier echten Gegenproben integrieren/ausführen; Doppelung-/Norm-Eigen-Tests integrieren; vollständigen Pflichtvorspann samt CLI und positiver Route integrieren; A/C und B anhand echter Datensätze gegenprüfen; Lauf24/25 und A/B/C abschließend zuordnen; unabhängige Codeprüfung; vollständige Tests; endgültiger Abschlussordner.

## Kosten
0 neue Biotop-Buchungen, 0 € gegen 5,00 € Budget. Kasse aus Datenbank: KASSE-02.md und ausgaben/29-kasse-zwischenstand.json. Kein neuer Biotop-Modellaufruf gestartet.

## Eigene Verfahrensgrenze
Der neue Auftrag läuft entgegen V17 in derselben Hermes-Elternsitzung wie die Bestandsaufnahme. Kein bewusster Reset erfolgt; die Aufträge und Ergebnisse werden hier über getrennte Ordner/Zeitgrenzen getrennt, nicht durch eine behauptete neue Sitzung.

Bericht: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ZWISCHENBERICHT-02.md
Dateiliste: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/DATEIEN-02.txt
Prüfsumme: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/PRUEFSUMME-02.txt
Kasse: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/KASSE-02.md
