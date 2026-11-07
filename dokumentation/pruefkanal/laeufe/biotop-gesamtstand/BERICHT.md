# Biotop-Gesamtstand — unabhängig gemessene Bestandsaufnahme

**Kein Lauf, keine Code-/Datenreparatur.** Quellstand `b42dc941e7fcb66632ba6a0e13b8df106a270a31`. Bestandsstichtag 2026-09-20T04:43:06.119737+00:00; Schlussprüfung 2026-09-20T05:52:01.964233+00:00. Auftrag: vor Vorbedingung 1 den tatsächlichen Bauzustand offenlegen, nicht alte Abschlussberichte wiederholen.

## Ergebnis zu den fünf verlangten Teilen

1. **Umfang:** **111 eigene versionierte Dateien / 11119 physische Zeilen**; davon **35 produktive Python-Dateien / 6370 Zeilen**, **18 physische Organmodule** für die **15 Sollorganabschnitte**. Hauptdatenbank **29659136 Bytes**, **27 Tabellen**. Eigene pytest-Sammlung: **0 Testfälle**, Exit 5, kein grüner Lauf. Prüfscripte und Werk-Vertragstests sind getrennt gezählt. → `UMFANG-01.md`.
2. **Betrieb:** Zum ausgewiesenen Prozessstichtag **0 Biotop-Treffer bei 148 von 148 gelesenen PID-Verzeichnissen**, kein vorhandener Biotop-System-/Benutzerdienst, keine laufenden Container. Viele Organe wurden historisch tatsächlich benutzt; das ist kein heutiger Dauerbetrieb. Optionale Pflichtorgane, fehlende Pfade und gefährliche Altscripte sind getrennt. → `ORGANBETRIEB-01.md`.
3. **F6-Abgleich:** **470 von 470 Solltextzeilen** einzeln adressiert; **35 von 35 produktiven Python-Dateien / 6370 von 6370 Zeilen** in den kombinierten Leseabdeckungen. **49 redaktionelle Befundgruppen**, keine doppelte Fehlerzahl aus überlappenden Prüferlisten; zwei überholte historische Kritiken separat. Jede Gruppe mit konkreten Quell-/Sollzeilen und Beweisgrenze. → `MASTERPROMPT-ZEILEN-01.csv`, `ABWEICHUNGEN-01.md`, Prüfungsanhänge.
4. **Läufe/Kosten:** **23 von 23 Läufen** mit DB-Status, Werk, historischen und heutigen Buchungen tabelliert. **7,37 € stimmt als Summe der fünf auf Cent gerundeten Abschnittsbeträge.** Die rekonstruierte Rohsumme ist `7.362027175925925413687` €; heutige Buchungen derselben IDs ergeben `7.852498092592592039347` €. Spätere Buchungen auf alten IDs und Rundung sind getrennt erklärt, nicht still verrechnet. → `LAEUFE-01.md`.
5. **Sechs Grundsätze:** Konkrete Eigenverstöße bei Norm-/Fundbeweisen, Befehlswirkung, Prüfnebenwirkungen, Nachrechnungsableitungen und Ersatzmerkmalen. Die Median-/Streuungsebenen sind heute grundsätzlich getrennt; ich behaupte dort nicht erneut den alten Fehler. → `GRUNDSAETZE-2a-01.md`.

## Die entscheidenden Gegenbefunde zu meiner bisherigen Arbeit

- Die Norm-Eichprobe konnte ohne Normprüfung grün werden (`masse` statt `mass`; historische Ergebnisse mit `norm=[]`, `zuwachs=None`). Ein früheres „vier bestanden“ beweist diese Torzeile nicht.
- Unter den IDs 22 und 23 wurde der Anklägerablauf geändert und weitergearbeitet. Reale Protokollübergänge belegen den Satz-2-Verstoß; Gitdatum oder Kostenanstieg allein wären kein Beweis.
- Das spätere C kann die eigene gerade protokollierte Ansage als Doppelung sperren. Die gestellten Pfadproben beweisen nicht die korrekte A→C-Integration.
- Der gebaute B-Mindestanteil hat einen Branch mit 12 fremden von 25 Einträgen. „Bauteil vorhanden“ ist nicht „Regel für jeden Bestand erfüllt“.
- Keine isolierte, automatisch auffindbare pytest-Eigen-Testsuite; kein erzwungener vollständiger Vorspann; keine technische Kern-Schreibrolle. Das ist kein für ein beliebiges echtes Werk betriebsfertiges System.

## Ausführung und Grenzen

Messungen stammen aus Dateien/AST, Git und read-only SQLite. Hashkette mit der Originalfunktion geprüft: **16030 von 16030 Protokollzeilen**. Dateiinhalte am Ende **3216 von 3216 unverändert**, keine Datei hinzugefügt/entfernt, Git sauber (`26-bestand-unveraendert.json`). Die öffentliche Protokollkopie entfernt Anmeldeinhalte und ist deshalb nicht selbst die unveränderte Gesamthashkette.

Neu ausgeführt: Inventar-/SQL-/Rechenprüfungen, pytest-Sammlung (kein Fall), vorhandene Rauschbeispiele. **Zusatz-Gegenfallprüfung fehlgeschlagen**, Exit 1 im eigenen Testgerüst; Wiederholung vom Tool blockiert und nicht umgangen. **0 von 4 vorgesehenen neuen Gegenfällen vollständig bestätigt gemeldet.** Statische und historische Befunde stehen unabhängig davon mit ihrer tatsächlichen Beweisgrenze im Bericht. Keine erfundenen Ausführungsausgaben.

**Kosten:** 0 neue Biotop-Kassenbuchungen / 0,00 € zusätzliche Biotop-Modellkosten von 1,00 € Budget. Drei Hermes-Prüfsitzungen laut `state.db` im Abo enthalten, keine bekannte Einzelrechnung; Details und Abfrageschnitt in `KASSE.md`.

**Eigener Lieferfehler:** Bei der Zwischenmeldung vor Rückkehr der delegierten Prüfungen lag zwar `ZWISCHENBERICHT.md`, aber noch kein `DATEIEN.txt` im Ordner. Damit war die Zwischenlieferpflicht nicht vollständig erfüllt. Die Abschlusslieferung behebt das; der Zwischenstand wird nicht rückwirkend als vollständig bezeichnet.

## Versions- und Fortsetzungsgrenze

Der tatsächliche Ist-Stand liegt bereits nach früheren Arbeiten an Vorbedingung 1: Lauf 24/25 und A/B/C existieren. Diese Bestandsaufnahme setzt sie weder zurück noch erklärt sie rückwirkend als ungearbeitet. Kein neuer Lauf wurde gestartet. **Ein neuer Reparaturauftrag ist vor dem gewünschten erneuten Vorbedingungs-Lauf erforderlich**, weil die gefundenen Messgerätfehler sonst die nächste Messung entwerten. Offene Punkte und Entscheidung: `OFFENE-PUNKTE-01.md`.

## Abholung / Prüfbarkeit

`DATEIEN.txt` listet den gesamten Ordner. `PRUEFSUMME-ORDNER.txt` nennt die SHA-256 des sortierten `PRUEFSUMMEN.sha256`-Manifests; dessen Einträge versiegeln die Nutzdateien einschließlich dieses Berichts, Rohdaten, Quellen und Einzelprüfungen. Das abschließende Abrufprotokoll liegt außerhalb dieses Manifests, um keine Selbstreferenz zu erzeugen. Eine gültige Lieferung wird erst nach bytegleichem HTTPS-Abruf aller Manifestdateien gemeldet.
