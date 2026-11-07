# Organbetrieb — gebaut, benutzt, laufend sind drei verschiedene Aussagen

**Laufend zum gemessenen Zeitpunkt: kein Biotop-Prozess.** Die Prozesslesung erfasste 148 von 148 PID-Verzeichnissen, davon 0 Biotop-Treffer und 0 Lesefehler; System- und Benutzer-`biotop.service` melden `LoadState=not-found`, Docker meldet 0 laufende Container. Andere Webdienste auf dem Wirt sind nicht das Biotop. Beleg: `20-betrieb-mit-bezugsgroesse.json` mit Zeitpunkt. Spätere Kurzprüfcontainer dieser Bestandsaufnahme sind keine produktiven Hebungsläufe.

Die folgenden 15 Sollorgane entsprechen den Abschnitten 3.1–3.15. Kein pauschales „15 von 15 fertig“: ein vorhandener Aufrufpfad ist nicht die Erfüllung aller Anforderungen. Historische Zähler enthalten ausdrücklich auch Proben, abgebrochene und verworfene Läufe. Die hier ausgewählten Ereignisarten sind Belege, keine disjunkte Zerlegung; deshalb werden sie nicht zu einer Gesamtzahl von Organaufrufen addiert.

| F6-Organ | Implementierung relativ zu biotop/ | historischer Beleg | Befund |
|---|---|---|---|
| 3.1 Aufnahme | `organe/aufnahme.py` | `aufnahme`: 23 von 16030 Protokollzeilen, #4–#15234 | Historisch benutzt; nur schmale Python-Paketform, kein allgemeiner Bau-/Abhängigkeitsweg; Startschutz unvollständig. A01–A04. |
| 3.2 Landkarte | `organe/landkarte.py, organe/vertraege.py` | `landkarte.gebaut`: 23 von 16030 Protokollzeilen, #37–#15267 | Historisch benutzt; Zoom-/Vertragsdaten vorhanden, Graph und Suche eingeschränkt. A05–A07. |
| 3.3 Werkverfassung | `organe/verfassung.py` | `verfassung.eingelegt`: 18 von 16030 Protokollzeilen, #838–#15268 | Texte/Regeln werden eingelegt und gelesen; kein eingebauter Entwurfsweg, Schutz vor nachträglichem Austausch schwach. C02, A09. |
| 3.4 Mentor | `organe/mentor.py` | `mentor.richtungen`: 13 von 16030 Protokollzeilen, #7565–#15276 | Historisch benutzt; Richtungswahl vorhanden, aber Schema und eigener Lauf je neuer Richtung nicht erzwungen. B-17. |
| 3.5 Maß, Messgerät, Jury | `kern/messgeraet.py; organe/generation0.py, eichung.py, eichproben.py, eichgegenstand.py, jury.py` | `mass.eingefroren`: 23 von 16030 Protokollzeilen, #40–#15271 | Historisch benutzt, kein bloßer Stub. Pflichtvorspann fehlt in Laufsteuerung; Eich-/Norm-/Mutantenlücken. A08–A16. Jury und ihre historische Mechanikbelege nicht mit laufendem Dienst verwechseln. |
| 3.6 Genesis / Nischen | `organe/genesis.py, organe/nischen.py` | `schwarm.kandidat`: 2633 von 16030 Protokollzeilen, #44–#16004 | Historisch erzeugt und gewichtet; vier Nischen gebaut. Artmuster fehlen in Schwarmvorlage, Bandit nicht werkklassenbezogen. B-13/B-16. |
| 3.7 Aegis | `organe/aegis.py` | `aegis.urteil`: 2608 von 16030 Protokollzeilen, #48–#16030 | Historisch zentral benutzt; Ansage A später vorhanden, Aufnahmesperre C später vorhanden, deren Selbstsperre nicht sauber integrierter Erfolg. A33/B-11; historische Änderungen B-01. |
| 3.8 Nexus | `lauf.py, insbesondere generation und _verhandeln` | `generation.ergebnis`: 116 von 16030 Protokollzeilen, #79–#16008 | Existiert als Laufsteuerung, nicht eigenes Nexus-Modul. Historisch Generalproben und Verhandlungen; serieller Ablauf, kein verlangter Wiederholungsautomat, Vertragslücken. B-18/B-19. |
| 3.9 Lazarus | `organe/lazarus.py` | `lazarus.schnappschuss`: 71 von 16030 Protokollzeilen, #39–#15660 | Historisch benutzt; Schnappschussereignisse nicht mit Zahl aktueller Archivzeilen gleichsetzen. Ausschlüsse, überschreibbare Generationstags, unvollständige Rückkehr. A30/A31. |
| 3.10 Immunisierung | `organe/aegis.py, organe/fundpruefung.py; lauf.py` | `immun.gefunden`: 230 von 16030 Protokollzeilen, #51–#16029 | Historisch Funde und Übernahmen; Fund-Neubewertung separat aufrufbar, nicht erzwungen. Archivierung nur nach Generalprobe. A14/B-09/B-10/B-12/B-20. |
| 3.11 Entropie | `organe/entropie.py` | `entropie.generation`: 43 von 16030 Protokollzeilen, #7758–#16009 | Historisch benutzt, Sättigungsmeldungen existieren; Verschiedenheit verwendet Mengen geänderter Textzeilen und filtert Proben am Namen statt am Merkmal. B-24. |
| 3.12 Drei Gedächtnisse | `organe/gedaechtnis.py` | `gedaechtnis.wiederholung`: 128 von 16030 Protokollzeilen, #7988–#16005 | Persistente Daten und aktive Wiederholungssperre; Art nicht im Schwarm, Mindestanteil in einem Branch falsch, Geschmack ohne Entscheidertrennung. B-13–B-15. |
| 3.13 Kammer | `organe/kammer.py, kammer/Dockerfile` | `kammer.probe`: 1 von 16030 Protokollzeilen, #445–#445 | Historisch und in dieser Bestandsaufnahme benutzt; kurzlebige Docker-Container mit Netzsperre, Limits und separatem Arbeitsbestand. Fester Sicherheitsnachweis aller Pfade fehlt; A04/A27. |
| 3.14 Kasse | `kern/kasse.py; anbieter/__init__.py` | `modell.antwort`: 4070 von 16030 Protokollzeilen, #3–#16003 | Historisch zentral benutzt; Token-Kosten gespeichert. Budgetautomat in Fehlerpfaden unvollständig, Kontingent und Adapter nur teilweise. A22/A23/A24. |
| 3.15 Oberfläche | `dienst.py, oberflaeche.py` | `anmeldung.token`: 4 von 16030 Protokollzeilen, #447–#7509 | Gebaut, Authentifizierungsaktionen historisch belegt; das ist kein Nachweis, dass heute eine Web-Oberfläche erreichbar ist. Kein aktiver Biotop-Dienst. HTTP-Abbruch defekt, Maßerklärungen veraltet. A29/B-23/C01. |

## 18 physische Organmodule — nicht 18 Sollorgane

- `biotop/organe/aegis.py` — 699 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/aufnahme.py` — 176 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/eichgegenstand.py` — 199 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/eichproben.py` — 249 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/eichung.py` — 239 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/entropie.py` — 103 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/fundpruefung.py` — 128 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/gedaechtnis.py` — 511 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/generation0.py` — 261 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/genesis.py` — 145 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/jury.py` — 62 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/kammer.py` — 98 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/landkarte.py` — 255 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/lazarus.py` — 110 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/mentor.py` — 136 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/nischen.py` — 122 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/verfassung.py` — 67 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.
- `biotop/organe/vertraege.py` — 84 physische Zeilen; Zuordnung oben und zusätzliche Eich-/Fundmodule unten.

## Gebaut und historisch aufgerufen, aber nur optional angebunden

- `eichung.rauschmessung`: 10 von 16030 Protokollzeilen, #12362–#12518.
- `eichprobe.ergebnis`: 17 von 16030 Protokollzeilen, #12406–#12543.
- `eichgegenstand.versiegelt`: 16 von 16030 Protokollzeilen, #12372–#12519.
- `immun.neubewertet`: 6 von 16030 Protokollzeilen, #11417–#15273.
- `generation0.ergebnis`: 6 von 16030 Protokollzeilen, #2706–#7554.
- `jury.urteil`: 7 von 16030 Protokollzeilen, #8853–#13539.
- `mentor.gewaehlt`: 11 von 16030 Protokollzeilen, #7569–#15277.
- `entropie.saettigung`: 6 von 16030 Protokollzeilen, #8686–#14430.
- `immun.archiviert`: 1 von 16030 Protokollzeilen, #13340–#13340.
- `immun.archivierung_zurueckgenommen`: 1 von 16030 Protokollzeilen, #13341–#13341.

`pruefung/vorspann.py` ruft Rauschmessung → Eichgegenstand → Fund-Neubewertung → vier Proben auf; schon diese Reihenfolge weicht von F6 ab, das die Fund-Neubewertung nach den Proben fordert. Die normale CLI verlangt ihn nicht vor `mass`, `gen0` oder `generation`. Das Wort „vor jedem Lauf“ in einem Skriptkommentar stellt noch kein Start-Gate her. Nicht „tot“ nennen: diese Organe haben reale historische Aufrufe, sind aber für die Laufsteuerung umgehbar.

## Nur vorhanden / nicht allgemein verdrahtet

- `adapter()` akzeptiert nur `openrouter`; keine weiteren nutzbaren Direktadapter oder eigener Aboanbieter-Port implementiert. A24.
- `kontingent` ist ein optionales Kassenfeld, aber keine im Aufrufweg geprüfte eigene Kontingentgrenze. A24.
- Kernprozesstrennung, Schreibrollen, allgemeines Klassenmaß, allgemeiner Verfassungsentwurf, vollständiger Wiederholungs-/Rollbackautomat und Aktenschrank-Suche: fehlen oder sind unvollständig; keine unbelegten „Organe im Leerlauf“. A07/A19/A26/A31, B-19, C02.
- Kein laufender Timer/Scheduler oder Biotop-Systemdienst ist durch die Prozess-/Dienstabfrage belegt. Das Skriptangebot allein ist kein autonomer Betrieb.

## Ablösungen und gefährlicher Altbestand

| Bestandteil | Einstufung | Warum / heutiger Weg |
|---|---|---|
| `pruefung/funde_neubewerten.py` | Historisches Schreib-/Auswertungsskript, fachlich abgelöst; nicht gefahrlos tot | Andere Ableitung über flache AST-Suche/Meldungen; erkennt nicht dieselben Fälle wie `organe/fundpruefung.py` mit Aegis-Helfern. Noch manuell ausführbar, verändert echten Bestand. A/B-Befund B-09. |
| `pruefung/lauf16_verwerfen.py`, `lauf18_verwerfen.py`, `lauf19_verwerfen.py` | Historische Einmalschreiber | Feste IDs/Notbehelfe aus der Zeit vor dem benannten Abbruchweg. Kein aktueller Laufautomat; Wiederholung wäre kein legitimer neuer Abbruchnachweis. |
| `pruefung/proben_tor2.py` und alte Tor-/Kurvenscripte | Historische Prüfstände, nicht allgemeine Regressionstests | Werk-/Laufbindungen und alte Textanker. Der spätere Syntaxbaum-Vorspann löst nur einen Teil ab; auch dort ist die Normzeile falsch. A11/B-05. |
| `pruefung/tor3_oberflaeche.py` | Weiter ausführbarer Prüfer mit echter Nebenwirkung | Überschreibt ein reales Konto; finally stoppt den Server, stellt Konto/Tokenbestand nicht wieder her. Nicht ausgeführt. B-22. |
| `pruefung/tor3_gedaechtnis_jury.py` | Historische, bestandsverändernde Mechanikprobe | Geschmack-/Jurydatensätze landen in produktiven Tabellen; spätere Probensperre bereinigt nicht jede Trainingsvermischung. B-15. |
| Die F1-Berechnung in `kern/messgeraet.py` und der alte `vergleichen`-Pfad | F1 ist als aktuelle Auswahl abgelöst, als Historienrechnung noch benutzt | `lauf.py:463–468` rechnet F1 ausdrücklich nach; deshalb nicht pauschal als toten Code löschen. Die heutige Auswahl verwendet F2. |
| `organe/genesis.py::gescheiterte_wege` | Parallelpfad zum neuen Projektgedächtnis, kein toter Code | Genesis zeigt sowohl den laufbezogenen Altweg als auch die neue werkbezogene Ableitung; Pflege zweier Ableitungen bleibt nötig. B-13. |
| `biotop/oberflaeche.py` / `organe/genesis.py` alte F2-Erklärtexte | Aktive veraltete Anleitung, nicht bloß Kommentaraltlast | Gegenstand und Grenzen der wirksamen Auswahl werden nicht korrekt erklärt. B-23. |

Die referenzsuchende Zählung `15-pruefskript-referenzen.json` findet nur explizite Dateinamenverweise. **Null Treffer beweisen keinen toten Code:** manuelle CLI-Aufrufe und dynamische Aufrufe bleiben möglich. Deshalb keine angeblich vollständige Zahl „toter Dateien“.
