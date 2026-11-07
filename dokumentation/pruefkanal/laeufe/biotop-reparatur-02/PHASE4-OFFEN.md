# Vier bestehende Phase-4-Mechanismen bleiben offen

Keine Abschlussprüfung/Implementierung dieser Punkte im Inventaraudit. Nicht pauschal aus dem Kernpfad ausgeklammert; Überschneidung präzise statt als repariert bezeichnet.

## P4-01 — Wirkungskreis/Transitivität
- Quellen: `biotop/organe/landkarte.py:112-125`, `biotop/organe/aegis.py:518-519`, `biotop/lauf.py:513-595`, `biotop/lauf.py:314-346`
Die Quelle besitzt eine transitive Rückwärtsclosure. Das beweist noch nicht, dass fachlich alle richtigen Kanten/Partner/Datenflüsse erfasst sind. Neue Guards für ids=[] oder mass=None beweisen nur tatsächlich geprüfte Ergebnisse für bereits gewählte Nachbarn, NICHT Wirkungskreisvollständigkeit. Keine Wiederabnahme hier.

## P4-02 — Vertragsaustausch
- Quellen: `biotop/organe/aegis.py:525-534`, `biotop/organe/aegis.py:698-725`, `biotop/lauf.py:513-595`
Benennung einer geänderten Vertragsdatei und bestandene Tests beweisen nicht die Erhaltung des bisherigen Vertrags. Ausführungsbelege verhindern skipped/fehlend, nicht inhaltliche Schwächung/Austausch. Nicht repariert und nicht pauschal aus dem Kern entfernt.

## P4-03 — NaN/Null-Collector
- Quellen: `biotop/kern/messgeraet.py:142-166`, `biotop/kern/messgeraet.py:236-256`, `biotop/kern/messgeraet.py:381-448`, `biotop/organe/eichung.py:111-150`
Numerische Unitguards existieren; sie beweisen die komplette Collector->Ersatzwert->F2-/Rauschgrenzen-Kette nicht. Scanner-Fehler->0 B04 und fehlende Testausführung B03 sind konkrete jetzige Nachweisgrenzen. Dadurch ist diese ältere numerische Ende-zu-Ende-Frage nicht erledigt.

## P4-04 — Generation-0-Erfolgsbindung beim Freeze
- Quellen: `biotop/organe/vorspann.py:217-229`, `biotop/lauf.py:80-120`, `biotop/lauf.py:599-660`
Original verlangt Existenz eines generation0.ergebnis-Ereignisses nach dem Vorspann, nicht erreicht=True. Unterschied: B06/B07/B11/B12 betreffen falsche Gen0-Belegentstehung; P4-04 erlaubt Freeze sogar bei korrekt als erreicht=False gemeldetem Ergebnis. Ein Fangparserfix schließt diese Bindung nicht.

