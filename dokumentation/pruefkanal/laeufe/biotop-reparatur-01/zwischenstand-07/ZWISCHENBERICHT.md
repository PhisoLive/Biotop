# Reparatur01 — Zwischenstand07: Kernreview fehlgeschlagen

2026-09-20T16:19:08.710223+00:00

**Keine Kernfreigabe, kein Reparaturabschluss.** Das unabhängige Review02 meldet passed=false wegen eines belegten Kernfehlers. Der Elternrepro52 bestätigt ihn am derzeitigen Elterncode. Zweite gezielte Nachbesserungsrunde ist isoliert beauftragt, noch nicht integriert.

## Kernfehler und eigener Nachweis

KERN-EICH4-SKIP: `aegis.py:89–95` ignoriert JUnit-`skipped` und liefert `ok=true`. `_vertrag_pruefbar` akzeptiert diesen benannten, nicht ausgeführten Vertragszeugen als gültige Gegenprobe.

Elternrepro52: **Exit 1, Soll-Assertion fehlgeschlagen**. Ein tatsächlich übersprungener Pflichtzeuge wurde als gültig akzeptiert; die Originalproduzentenzeile meldete pruefbar=true. Die Fortleitung durch den Originalproduzenten nutzt ausdrücklich gestellte Maß-Unit-Eingaben, der Batterieverbraucher sieben gespeicherte gültige Elternzeilen plus diese eine Zeile. Kein Nachweis einer frischen falschen Docker-Vollbatterie. Der direkte Originalparser-/Prädikatrepro braucht diese Maßhülle nicht.

Befehl, stdout/stderr und Ergebnis: ausgaben/52-skip-eltern-rot.*. Vollständige private Quellfixture, reales JUnit und Reproskript: eltern-repro/. Die ausschließlich private Repro-DB ist nicht veröffentlicht; sie wird vom gelieferten Skript erzeugt.

## Was gültig bleibt

Das Review hat die vier positiven und vier negativen Elternprädikate48/49 samt konkreten Vertragszeugen nachgerechnet; dort kein übersprungener Pflichtzeuge. Suite48 bleibt als ausgeführter Beleg **188 von188 bestanden**, nicht als Nachweis allgemeiner Prüferkorrektheit. Kernmaß/Pareto und beide Eingangsrichtungen bleiben durch die in review-02/REVIEW.json einzeln benannten Kontrollen belegt. Gen0 selbst wurde im Eltern-CLI49 nicht ausgeführt; sein Eingangsnachweis war verwendbar. Der zusätzlich geprüfte Gen0-Rumpfeintritt des Reviewers ist als kontrollierter Unit-Pfad gekennzeichnet.

## Integration und Restarbeit

- 126 von126 geprüften Elternquellen unverändert seit Beauftragung dieses Fixzyklus. Keine Skip-Korrektur vorweg als integriert behauptet.
- Fix deleg_52027b88: ausschließlich Skip/xfail-Zeugengültigkeit, direkte Passkontrolle und auffindbare Eigentests. TDD-Rot vor Produktkorrektur, keine Schwelle senken.
- Offen: Fixrücklauf, selektive Integration, derselbe Elternrepro grün, aktuelle Vollsuite/echte Probenpaare und CLI-Freigaberoute, unabhängige Nachprüfung, finale Versiegelung.
- **Zweite und letzte automatische Fix-/Reviewrunde.** Bei erneutem Kernfehler nach dieser Runde Entscheidung an Philipp, keine unbegrenzte Schleife und kein versteckter Abschluss.
- Vier Phase-4-Lücken bleiben unverändert offen; PHASE-4-LUECKEN.md und wörtliche Auftragseingrenzung liegen bei. Keine Wiederaufnahme der gestoppten Fixes, keine produktive DB-Änderung oder natürliche Evolution beauftragt; Lauf24/25 nicht fortgesetzt.

## Integrität und Kasse

167 von167 Dateien des Reviewmanifests gegen SHA-256 geprüft und unverändert übernommen. Alte versiegelte Lieferungen erneut inhaltlich geprüft; INTEGRITAET.json enthält die Nenner. Frühere negative breite Reviews bleiben negativ. KORREKTUR-02.md ordnet den Übergang ein, ohne alte Bytes zu überschreiben.

Neue Biotop-Modellkosten: 0 € von5,00 €, 0 neue Buchungen. Träger-/CPU-Grenze und alle historischen Versuchszahlen nicht mit Null weggebucht; Details KASSE.md/.json.

Bericht: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-07/ZWISCHENBERICHT.md
Dateien: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-07/DATEIEN.txt
Manifest: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-07/MANIFEST.sha256
Prüfsumme: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-07/PRUEFSUMME-ORDNER.txt
Kasse: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/zwischenstand-07/KASSE.md
