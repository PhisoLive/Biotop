# Spezifikationen für den nächsten Auftrag (aus der Behebungsrunde 3 vor T4, Review und eigene offene Punkte)

Stand: Kern-Commit `0aac612` (Code wie `d54bf2f`). Nach „ein Review, keine Fix-Kaskade“ ist nach dem Review kein Code
gebaut. R4-1 … R4-7 sind **gemessen** (Proben des Prüfers in der Kammer; Skripte und Ausgaben im Abschlussordner als
`review_*`); die übrigen sind gelesen oder eigene offene Punkte. Erster Schritt des nächsten Auftrags: jede Probe als
pytest-Spezifikation fassen (rot an `0aac612`, Gegenprobe grün).

| Nr | Spezifikation | Beleg an `0aac612` | Gegenprobe |
|---|---|---|---|
| R4-1 | Merkmale feiner: Weißraum je Zeichen (`tab`, `zeilenumbruch`, `cr`, `nbsp`, `doppelleer`), gleich in Sonde und Aufzeichner, passend zu den Formvarianten. Ein Test mit doppeltem Leerzeichen deckt keinen Tab-/LF-Rückschritt | Review Nr. 1: x1 überlebt, 14 von 14 `ValueError` gedeckt | x1k: ohne den Test abgelehnt |
| R4-2 | Verfälschung je Aufruf mit dem Muster der Abweichung (nicht je Funktion); nur Fehlschläge in der `call`-Phase zählen; Klassen je Test und Funktion im Urteil | Review Nr. 2: x2 überlebt, 6 von 6 gedeckt | x2k: ohne den Tab-Aufruf abgelehnt |
| R4-3 | Nur echte Generatoren auslesen und ersetzen; andere Iterator-Objekte durchreichen, als Enthaltung „Iterator-Objekt“ zählen; Lastabbruch unter der Sonde, während das Messgerät die Last fehlerfrei lief = Messgerätausfall | Review Nr. 3: p18 0 Abweichungen, tragfähig | p18b: 6 Abweichungen |
| R4-4 | Zustand nach dem Aufruf auch für `__slots__` und `dataclass(slots=True)` (`_veraenderlich`, `schnappschuss`, `zuruecksetzen`, `_stoeren`) | Review Nr. 4: p19/p20 0 Abweichungen | p19b: 28 |
| R4-5 | Instanz aus der Signatur: weitere Argumentlisten versuchen, bis ein Methodenaufruf inhaltlich ist; eigener Enthaltungsgrund „Instanz ohne inhaltlichen Aufruf“ | Review Nr. 6: p16 0, „1 von 2“ | p16b: 4 |
| R4-6 | Koroutinen mit eigener Ereignisschleife beobachten; sonst: ist eine *geänderte* Funktion unbeobachtet, enthält sich das Urteil statt „tragfähig“ | Review Nr. 7: p13 tragfähig | — |
| R4-7 | K2868 mit gestelltem deckendem Test je Muster nachspielen (mit und ohne doppeltes Leerzeichen, mit und ohne `gewicht: 0`); Klassen der aufgezeichneten Aufrufe im Beleg | Review Nr. 8; BERICHT §3 (`null_zahl` in 40 von 40) | — |
| R4-8 | Annahmegrund nur mit bestätigten Gewinnbereichen | Review Nr. 11: K2904 D1 `bericht` −20 % → Nachmessung −8,4 % | — |
| R4-9 | Test: ungültige Gewinn-Nachmessung → zurückgestellt (Annahmepfad) bzw. Messgerätausfall (Generalprobe) | Review Nr. 12: 0 Tests | — |
| R4-10 | Kommentare in `aegis.py` an den Code angleichen (gepoolt; Deckung je Muster) | Review Nr. 13 | — |
| R4-11 | Verdrahtungslast mit einem Kandidaten im Gewinnband; `gewinn` ≠ `None` verlangen (Generalprobe einmal wirklich ausführen) | Review Nr. 9c, 14: 0 von 16 | — |
| R4-12 | Kappe für Verfälschungsproben mit gezählter Enthaltung; Zahl der Kammerläufe je Kandidat im Urteil | Review Nr. 15 | — |
| R4-13 | Iterator-Kappe als Teil-Enthaltung zählen („mehr“) | Review Nr. 16: p14 0, „1 von 1“ | — |
| R4-14 | Formart nur ergänzen, wenn `klassen_von` sie für den Wert liefert; instabile Funktionen aus „beobachtet“ nehmen | Review Nr. 17 (gelesen) | — |
| R4-15 | Vergleichslast der Nische „schnell“ vergrößern, bis K2904/K3091 3 von 3 gleich entschieden werden (Streuung der Quote < Abstand zur Schwelle) | BERICHT §4: K3091 3 von 9 über 0,85, s = 0,035 | K2904 0 von 9 |
| R4-16 | Muster: Merkmale nicht variierter Argumente — Entscheidung Philipp/Chat-Claude vor dem Bau | BERICHT §3, §14 Nr. 2 | — |
| R4-17 | Methoden von Klassen in TypeScript (Entscheidung 3) | BERICHT §2 | — |
| R4-18 | Doppelprüfung der Gegenzeugen verbindlich einhängen (Versiegelung/Aufnahme künftiger Testwerke) | BERICHT §5, §14 Nr. 4 | — |
| R4-19 | S-12 und S-3 (Wurzelmodul) durch den Laufweg belegen | BERICHT §6 | — |
| R4-20 | Vom Kandidaten mitgebrachte Tests als deckende Tests: zulassen oder ausschließen? Mit ihnen kann ein Kandidat R4-1/R4-2 selbst ausnutzen | BERICHT §10 (gelesen, nicht gemessen: `aegis.py:873, 985, 1059`) | — |
