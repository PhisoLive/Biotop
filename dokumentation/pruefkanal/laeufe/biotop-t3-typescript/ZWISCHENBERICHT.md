# T3 — TypeScript-Breitentest (in Arbeit)

Auftrag Philipp, 21.09.2026, Masterprompt Fassung 7. Ausschließlich T3; kein Handelssystem und kein automatischer T4-Start. Budget 10 EUR über sämtliche T3-Läufe, einschließlich Eichkosten und gescheiterter Versuche. Der abgenommene Bestand bleibt Grundlage; keine erneute Gesamtbestandsaufnahme.

Eigene Arbeitsentscheidung: eigene Datenbankkopie, keine Änderung historischer Werk-/Laufdaten in der produktiven DB. Vorhandene uncommittete Quellen sind gesichert und werden nicht verworfen.

## Tor 4
1. Aufnahme/Bau/Tests/Versiegelung: offen.
2. Generation minus eins, 4 Proben + 4 gültige Gegenproben: offen.
3. Generation 0, mindestens 80 von 100 nicht-äquivalenten Mutanten: offen.
4. Mindestens 80 Prozent der versiegelten Schwächen behoben: offen.
5. Kein Rückschritt in angenommenen Generationen: offen.
6. Vergleichsbereich ohne angenommene Änderung ohne Maßgewinn: offen.
7. Doppelungsanteil unter 20 Prozent erzeugter Angriffstests: offen.
8. Sättigung oder Budgetabbruch: offen.
9. Verbundausfall im tatsächlich verwendeten Beitragspfad: offen; kein Nachweis über Hermes-Träger-MoA behauptet.
10. Genau ein abgeschlossener Reviewdurchgang: noch nicht begonnen.

## Verfassung
T3-Verfassung muss als Entwurf vorgelegt und vor dem evolutionären Lauf gültig bestätigt sein; Hermes-Vollmacht für Generationen und Mentorwahl ist keine erfundene Bestätigung durch Chat-Claude.

## Bauzwischenstand 21.09.2026
Fassung 7 vollständig gelesen (512 Zeilen); kein evolutionärer Lauf begonnen. Philipp hat die Verfassungsbestätigung ausdrücklich bei Chat-Claude belassen und parallel Bau/Eichung erlaubt. Vollständiger Entwurf mit Dateiliste und Manifest unter `verfassung-entwurf-01/`; Manifest-SHA-256 `dc556d9c4a53fe099877694310e7af6d6dfbb2b4632d2674cf5d83a1c0952406`, fünf von fünf Dateien per HTTPS bytegleich. Diese Freigabe ist noch offen.

Zwei getrennte Bauhelfer bearbeiten Werk und TypeScript-Kammeradapter; kein Review beauftragt. Die Elternintegration hat 39 von 39 fokussierten Eigen-Tests ausgeführt bestanden (`/root/biotop-t3/kernintegration-02.txt` und XML, noch privat). Das sind überwiegend kontrollierte Unit-/Integrationsfälle, keine T3-Torbelege. Erster gemeinsamer Durchlauf: 38 von 39 bestanden, ein Regexfehler in der Testhülle (`Vertrag` statt `Verträge`); behoben und erneut ausgeführt. Der anschließende Regressionslauf ohne die parallel in Arbeit befindlichen Adaptertests ist fehlgeschlagen: 338 von 344 gesammelten Fällen bestanden, vier fehlgeschlagen, zwei private Bestandsfälle übersprungen (342 tatsächlich ausgeführte Fälle). Historische Ausgabe bleibt `regression-01.txt/.xml`. Die vier Fehlschläge wurden gezielt geklärt: drei kontrollierte Vertrags-Fixtures lieferten nur einen String statt der nun gelesenen Vertragsstruktur; eine Erwartungsliste band noch ausschließlich Python. Angepasst wurden die Fixtures/Erwartungen, nicht die strengere Produktprüfung. Genau diese vier Fälle wurden danach ausgeführt: vier von vier bestanden (`regressionskorrektur-01.txt/.xml`). Zusätzliche Charakterisierungen führen geänderte mjs-/Lockbytes durch den ursprünglichen Nachweisleser: vier von vier Bindungsfälle bestanden (`bindung-gegenproben-01.txt/.xml`). Das ersetzt keinen abschließenden Regressionslauf am stabilen Integrationsstand.

Gestellter Anbietertransport wurde durch tatsächliche Antwortauswertung, Genesis, Kasse und Protokoll geführt: ein Ausfall und ein erzeugter Kandidat bei zwei vorgesehenen Mitgliedern, mit gültiger Antwort als Positivkontrolle. Geltungsbereich: Biotop-OpenRouter-Schwarm, nicht Hermes-Träger-MoA; dessen Opus-Ausfallbehandlung bleibt offen. Die Verbrauchsangaben dieser Probe sind gestellt und nur in einer isolierten Prüf-DB verbucht, keine echten Anbieterbuchungen.

Neue TypeScript-Sprachwege sind in Aufnahme, Landkarte, Messgerät, Testzulassung und Generation 0 integriert, aber noch nicht zusammen mit dem fertigen Werk in der Kammer belegt. Die vier TypeScript-Eichpaare sind noch zu bauen. Bekannte Freeze-/Wirkungskreislücken wurden mit gezielten roten Fällen angegangen; keine pauschale Entwarnung für historische Außenleser.

Kasse: weiterhin kein echter Biotop-Modellaufruf dieses T3-Auftrags; 10 EUR bleiben die gesamte harte Auftragsgrenze. Träger-/Host-/Abo-Verbrauch monetär nicht ermittelt. Private T3-DB und Ausgangssicherung unverändert als Grundlage, keine neue fachliche Torwertung.

## Ende dieses Stands
Noch keine Abnahmevorlage. Alle nicht ausgeführten Zeilen bleiben offen/rot. Der Abschluss wird im selben, bisher unversiegelten Ordner ergänzt.
