# Integrationshinweis – Fassung 7 / Messgerät

`roh/27-lokale-regression/`: **1 fehlgeschlagen, 129 bestanden, 2 skipped**; 237 tatsächlich gezählte Kammeraufrufe. Kein grüner Gesamtbeleg.

- Fehlgeschlagen: `tests/test_review_vertrag.py::test_test_eigener_fehler_ist_keine_pruefbare_vertragsgegenprobe[setup]`, Zeile 103 der zugeteilten Kopie.
- Alte Erwartung: außer Sammlung sei die spätere Messhülle gültig. Tatsächlicher neuer Beleg: Setup wirft vor dem Testkörper, call-Nachweis fehlt; `messen.gueltig=False`, `pruefbar=False`, `bestanden=False` in beiden Richtungen. Fassung 7 verlangt diese Sperre.
- Nötige Anpassung durch Parent im bereits exklusiv anderweitig bearbeiteten Testfile: Gültigkeit bei nicht ausgeführten Setup-/Skip-/Xfail-Proben nicht fordern, sondern den echten Ausführungsstatus und den originalen ungültigen Messnachweis prüfen. **Keine Assertion hier geändert.** Ausgeführte AssertionError-/Call-Fehlschläge bleiben bewertbare Messungen (eigene Positivpaare).
- Die beiden Skips betreffen `tests/test_eichproben.py:224` und `tests/test_review_vertrag.py:155`, jeweils fehlende private Werk-/DB-Kopie. Nicht ausgeführt, daher kein Nachweis. Produktion/Parent wurden nicht dafür gelesen.
- Die neue eigene Datei `tests/test_messnachweise.py` ist in diesem Lauf vollständig ausgeführt und grün (57 Testfälle; nach JUnit nachrechenbar).

Die endgültige vollständige Suite, aktualisierte Aegis-Tests und CLI verbleiben beim Parent. Historische 188/188 werden nicht umgedeutet.
