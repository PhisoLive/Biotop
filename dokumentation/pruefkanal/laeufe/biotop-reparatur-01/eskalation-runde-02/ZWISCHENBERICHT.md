# Biotop Reparatur01 — Eskalation nach zweiter und letzter Runde

2026-09-20T18:01:19.243760+00:00

**Kernabnahme gescheitert. Zweite und letzte automatische Runde beendet; Entscheidung liegt bei Philipp.**

Keine Abnahme erbeten, keine natürliche Messfreigabe, keine dritte automatische Reparaturrunde. Die Schwellen und geforderten Sollurteile bleiben unverändert.

## Gemessener aktueller Stand

- **Vollsuite62 fehlgeschlagen: 303 von 305 Fällen bestanden, 2 von 305 Assertionfehler, 0 von 305 Errors, 0 von 305 Skips; äußerer Exit1.** Die 15 Kernmaß-/Paretofälle wurden tatsächlich zuerst ausgeführt und sind bestanden. Rohtext, JUnit, Quellhashes und 345 Kammerdatensätze liegen unter `ausgaben/62-*`.
- Fehlgeschlagen: `test_eichproben::test_vier_paare_am_kopierten_pruefwerk` und `test_review_vertrag::test_benannter_vertrag_am_kopierten_pruefwerk`. Keine Herabsetzung der Erwartungen oder neuer Produktpatch nach dieser roten Abnahme.
- **Eichbatterie62: 1 von 4 positiven Fällen gültig mit Sollurteil True, 3 von 4 positiven Fällen unprüfbar; 4 von 4 Gegenfällen gültig mit Sollurteil False.** Nebenwirkung und Regression werden durch den neuen Vollständigkeitswächter abgebrochen. Beim positiven Vertrag fehlt der angeforderte Laufzeitnachweis `bericht`. Diese Gründe belegen die Sperre, noch keine vollständig isolierte Wurzelursache. Insbesondere ist ein falsches Prädikat eines unprüfbaren positiven Falls keine erfolgreiche Gegenprobe.
- **Echte Pflichtvorspann-CLI63 fehlgeschlagen: Exit1, privater Status `gescheitert`, Gen0-Eingangsnachweis nicht verwendbar.** Wieder 1 von 4 gültigen positiven und 4 von 4 gültigen falschen Gegenfällen. 83 von 83 tatsächlichen Kammern mit Privatbuchungen abgeglichen; keine Modellbuchung. Die Rauschkalibrierung sperrte 0 von 4 Bereichen — das heilt die unbrauchbare Batterie nicht. Rohdaten einschließlich stderr unter `ausgaben/63-*`.
- Die 103 neuen Messgeräte-/Verbraucher-Eigenfälle waren in Eltern58 gegen den vorherigen Stand zu 82 von 103 rot, in Eltern59 zu 103 von 103 grün. Das ist ein isolierter Integrationsnachweis, **kein Ersatz** für die fehlgeschlagene Gesamtprüfung. Exakte Einzelzählungen in `ABNAHME.json`.
- Die F7-Anpassung des alten Vertrags-Eigentests ist als eigene Parent-Entscheidung dokumentiert: `INTEGRATIONSENTSCHEIDUNG-RUNDE2.md`. In Eltern60 scheiterten die drei veralteten Messhüllen-Erwartungen; in61 sind 6 von 6 Fälle grün. Positive Bestandsproben wurden dadurch nicht umdefiniert.

## Lieferumfang und Grenze

Vier ursprüngliche Arbeitspakete sind mit ihren unveränderten Prüfsummen aufgenommen: Aegis-Zeugenfix, Messgerät, Kernverbraucher und lesendes Originalaudit. Integration ausschließlich der erlaubten Kernpfade: 6 geänderte von 126 Ausgangsdateien, 3 neue Eigentestdateien, 120 von 126 Ausgangsdateien bytegleich. Aktueller vollständiger Quellstand: 129 Dateien. In `lauf.py` ist der AST außerhalb `_verhandeln` identisch. Gen0-/Aufnahme-/Legacy-Außenfixes nicht integriert; die quarantänisierte Arbeit bleibt sichtbar und im Aufwand.

Der grüne Aegis-Teilstand57 (202 von202, vier gültige Paare) bleibt historisch richtig, ist aber **nicht** der aktuelle Gesamtstand. Er gilt nicht als Freigabe nach Messgeräte-/Verbraucherintegration. Kein veröffentlichter Vorgänger wurde geändert.

Auslieferungskorrektur gegenüber Zwischenstand10: seine beiden `.gitignore`-Adressen lieferten404. Dieser neue Ordner hält die Originalbytes unter benannten Downloadaliasen und mit Originalpfaden in `PUNKTDATEIEN.tar.gz`; siehe `AUSLIEFERUNGSKORREKTUR.md`, `DOWNLOAD-ZUORDNUNG.json` und `PUNKTDATEIEN-WIEDERHERSTELLEN.md`. Der alte Fehlversuch bleibt benannt; keine Serverregel wurde gelockert.

## Suchabdeckung und offene Außenliste

Originalaudit: 126 von 126 inventarisierten Dateien als gelesen dokumentiert, 145 Leserblöcke, 16 Mechanismusgruppen. Parent prüfte die Quellhashes aller Dateien und die exakten Quellzitate aller Leserblöcke sowie alle ID-Verweise und disjunkten Summen. Das beweist Integrität der Auditzuordnung, nicht lückenlose semantische Fehlerfreiheit.

**Suche weiterhin unvollständig:** acht semantische Kandidaten und45 breite Kandidatenzeilen ohne abgeschlossene Feinzuordnung bleiben offen. Diese beiden Populationen sind nicht zu einer Fehlerzahl zu addieren. Die661 ursprünglichen Suchzeilen sind keine661 Fehler. Keine Entwarnung aus Abwesenheit weiterer Funde.

`AUSSERHALB-KERN-BESTAETIGT-OFFEN.md/.json` enthält **19 bestätigte Leserorte**, ausdrücklich offen: die ursprünglichen11 Orte in11 nichtproduktiven Prüfskripten plus8 weitere Orte in3 Produktdateien, die nach der Nutzergrenze außerhalb dieser Reparatur bleiben. Statische Bestätigung wird nicht als ausgeführter Repro ausgegeben. Originalkategorien bleiben unverändert; die engere Parent-Arbeitszuordnung steht daneben in `audit-elternabgleich/`, inklusive Verbraucher-Aliassen statt Doppelzählung.

Die vier früheren Phase4-Lücken bleiben ausdrücklich ungelöst und sind separat in `PHASE-4-LUECKEN.md` erhalten. Keine Behauptung, sie seien widerlegt oder repariert.

## Unabhängige Nachprüfung und Entscheidung

Der separate Schlussbefund liegt unter schlussreview/; passed=false. Zusätzlich zur realen Abnahmeverfehlung KERN-01 sind KERN-02 (kollidierende Klassen-Testidentitäten im Paretovergleich) und KERN-03 (testinterner NameError ohne Ortsnachweis als Werkabsturz gewertet) an ausdrücklich synthetischen Parser-/Verbrauchergrenzen belegt. Der Parent hat diese Kontrollen und die Belegnachzählung identisch wiederholt: schlussreview-eltern/. Keine neuen realen Kammern oder DB-Fälle daraus behauptet. Drei offene Kernbefundgruppen stehen in KERNBEFUNDE.md/.json. Ein möglicher Statuswechsel durch KERN-03 ist statisch abgeleitet, nicht an einem realen Fund ausgeführt. Dies war nur die unabhängige Nachprüfung, kein weiterer Fixzyklus.

**Eigene Empfehlung des Parents für die Entscheidung:** einen getrennten, eng begrenzten Folgeauftrag ausschließlich für die drei offenen Kernbefundgruppen freigeben; erst danach dieselbe Bestandsbatterie und Pflichtvorspannroute erneut abnehmen. Kein Schwellenabbau, keine automatische Wahl eines bequemeren Prüfgegenstands und keine pauschale Ausweitung auf die Außenliste. Ohne Freigabe keine weitere automatische Produktänderung.

Kasse: 0 € von5,00 € gebuchte Biotop-Modellkosten, 0 neue Buchungen. Sonstige Kosten nicht als Null behauptet; KASSE.md/.json und KAMMERBILANZ.json enthalten Schnitt und Lücken.

Dateien: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/eskalation-runde-02/DATEIEN.txt
Bericht: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/eskalation-runde-02/ZWISCHENBERICHT.md
Manifest: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/eskalation-runde-02/MANIFEST.sha256
Prüfsumme: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/eskalation-runde-02/PRUEFSUMME-ORDNER.txt
Kasse: https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/eskalation-runde-02/KASSE.md
