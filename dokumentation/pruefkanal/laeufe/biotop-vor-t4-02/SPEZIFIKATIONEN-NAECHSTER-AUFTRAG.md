# Spezifikationen für den nächsten Auftrag (aus der Behebungsrunde 2 vor T4, Review und Gegenproben)

Stand: Kern-Commit `6243377`. Jede Zeile ist an diesem Commit **gemessen rot**:
- entweder als ausgeführte Kammerprobe des Gutachtens (`review-proben/sondenprobe*.py`, Ausgaben `SONDENPROBE*.txt`),
- oder als pytest-Spezifikation (`spez/`).

Die Proben des Gutachtens sind noch **keine** pytest-Spezifikationen. Sie so zu fassen (rot an `6243377`, Gegenprobe
grün), ist der erste Schritt des nächsten Auftrags. Neuen Code nach dem Review habe ich nach der Regel „ein Review“
nicht gebaut.

| Nr | Spezifikation | Rot an 6243377 (Beleg) | Gegenprobe |
|---|---|---|---|
| S-1 | Generator- und Koroutinen-Ausgaben werden verglichen (erste N Elemente), sonst Enthaltung je Funktion, nicht „beobachtet“ | p1: 0 Abweichungen bei geänderter Ausgabe | p0: 14 |
| S-2 | Der Zustand der Argumente nach jedem Aufruf ist eine eigene Beobachtung (beide Sprachen) | p2: in-place-Sortierung umgedreht, 0 | — |
| S-3 | Als beobachtet zählt nur eine Funktion mit mindestens einem fehlerfreien, inhaltlichen Ergebnis auf beiden Seiten. Klassen mit geänderten Methoden und Wurzelmodule gehen in y ein; `nicht_eingewickelt` steht im gespeicherten Urteil | p4, p3, Wurzelmodul-Aufruf | — |
| S-4 | Festes `PYTHONHASHSEED` für Sonde und Aufzeichner; instabile Beobachtungen der Vorgeneration (zweimal beobachten) sind Enthaltung | p5: 22 Fehlalarme, 2 von 2 | — |
| S-5 | Aufrufbare Objekte mit `__wrapped__` (u. a. `lru_cache`) werden eingewickelt; eine fehlende Beobachtung wegen gescheiterten Einwickelns ist Enthaltung oder Messgerätausfall, nie „ungedeckt“ | p12: 16 von 16, Ablehnung | — |
| S-6 | Deckung: Eingaben über `inspect.signature(...).bind().apply_defaults()` vereinheitlicht; TS-Aufzeichner wickelt `export const`; Deckung nur, wenn der Test beim Verfälschen des Ergebnisses fällt | p10 (0 gedeckt), p8 (0 Aufrufe), p6 (Beifang deckt 4) | p10b: 2 gedeckt |
| S-7 | Getrennte Gegenprobe K2868: erweiterter Korpus mit alter Deckungsregel; K2868 muss allein an `~form` scheitern; die 40 Abweichungen ungekürzt aufgeschlüsselt | nicht gemessen | — |
| S-8 | Formvarianten auch aus Randwerten mit Leerzeichen (z. B. `'a b'`); Zählung „Funktionen ohne Formvariante: x von y“ | p4, p8: 0 Formvarianten | — |
| S-9 | Gewinnschwelle der Nische schnell in beiden Richtungen bestätigt; `laufzeitrisse` aus einer Liste statt aus dem Text; Nachmessung im Verdrahtungsbeleg und im Nachspiel | `spez/test_spez_gewinnschwelle_nachmessung.py`: 2 von 4 rot; p9 | 2 Gegenproben grün |
| S-10 | Vertragsprobe prüfbar, wenn die Referenzlast die erste Funktion von A ruft | `bau/diagnose_eichproben.py` (erste REF_PAAR-Fassung) | — |
| S-11 | `test_vorspann`: `lz_angefordert` im Fall `nur_gesperrtes_rauschen` nicht leer | gelesen | — |
| S-12 | Zeitlimit am Kandidaten bei gültiger Vorgeneration ist ein Inhaltsbefund; Aufzeichnerlauf mit 0 Aufrufen trotz betroffener Tests ist eine Enthaltung | gelesen | — |
| S-13 | Deckungsregel und Gewinnschwelle: Entscheidung Philipp (BERICHT §12 Nr. 7, 8) vor dem Bau | — | — |
