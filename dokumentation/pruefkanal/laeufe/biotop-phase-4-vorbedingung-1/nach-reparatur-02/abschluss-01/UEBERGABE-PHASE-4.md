# UEBERGABE PHASE 4 — selbständig lesbarer Stand

Quellenabfrage abgeschlossen: 2026-09-20T20:25:28.180233+00:00. Autor: Hermes, Ausführender. Auftraggeber und Freigabe ab dem echten Werk: Philipp Zöllisch. Chat-Claude prüft den Abschlussordner, nicht eine Chat-Zusammenfassung.

## Sofort lesen: kein automatischer Start

Lauf 26 ist nach Generation 5 natürlich gesättigt und beendet. Die geforderte Doppelungsquote ist 1 von 11 = 9.09 %; der lagerhaus-Mentor nennt in 3 von 5 Richtungen echte werkübergreifende Verweise. Trotzdem keine uneingeschränkte Abnahme der gesamten Immunisierungszeile: K2689 hat einen roten Ausführungsnachweis, neue bestätigte Behebungen traten nicht auf. Status und Entscheidung nicht zu „Phase 4 freigegeben“ hochrechnen. Siehe ERGEBNIS-DETAIL.md, TORZEILEN.json und REVIEW.json derselben Lieferung.

Nächster fachlicher Schritt in einer **frischen Sitzung**: Vorbedingung 2 aus Fassung 6, die Verfassung des Handelssystems. Philipp schreibt/entscheidet; Hermes darf den Entwurf vorbereiten, nicht die Freigabe ersetzen. Fehlende Freigabe dieser Vorbedingung 1 bzw. der F7-Restbefund bleiben Entscheidungspunkte, kein automatischer Reparatur- oder Hebungsauftrag.

Diese Übergabe ersetzt den Sitzungskontext, nicht den Masterprompt. Maßgeblich sind Fassung 6 sowie Philipps nachstehende F7-/Verfahrensentscheidungen. Ältere Skills behaupten teils 11/11 für Tor 2 und sind dafür keine Autorität.[1][7][8]

## (a) Was das Biotop heute ist

Ein Python-System zur kontrollierten Evolution eingelegter Software-Werke: Aufnahme → Landkarte/Verfassung/Verträge → Pflichtvorspann (Rauschen, versiegelte Eichproben und Fund-Neubewertung) → Generation 0 → eingefrorenes Maß → Schwarm/Ankläger/Generalprobe → Freigabe und Lazarus. Modelle erzeugen Vorschläge; harte Messungen entscheiden. Das Biotop bearbeitet ein getrennt eingelegtes Werk, nicht seinen eigenen laufenden Quellstand.[1]

**Heute gezählter Python-Quellumfang:** 104 von 104 Dateien, 13948 physische Zeilen. Davon 11165 Token-belegte Codezeilen, 370 reine Kommentarzeilen, 1056 reine Docstringzeilen und 1357 Leerzeilen; disjunkte Summe = 13948. Definition: splitlines, Python-Tokenizer plus AST-Docstrings; Code-Strings zählen als Code, keine pygount-SLOC-Behauptung. Gezählt werden biotop/, tests/ und pruefung/ ohne Caches/Abhängigkeiten. Git-Innereien, Laufdaten, Archive, fremde Werke und andere Dateiformate sind nicht in dieser Python-Zahl. Beleg: BESTAND.json samt vollständiger Dateiliste und bestand_erheben.py im Quellarchiv.

- `biotop/`: 36 von 104 Pythondateien; 7237 von 13948 physischen Zeilen; 5615 von 11165 Codezeilen.

- `tests/`: 14 von 104 Pythondateien; 2483 von 13948 physischen Zeilen; 2074 von 11165 Codezeilen.

- `pruefung/`: 54 von 104 Pythondateien; 4228 von 13948 physischen Zeilen; 3476 von 11165 Codezeilen.

**Gesamtsicht eigener Quellen über alle Formate:** 129 von 129 Dateien und 14501 physische Zeilen, ermittelt mit git ls-files --cached --others --exclude-standard und anschließendem Lesen aller Dateien. Davon 111 Git-erfasst; zusätzlich 18 nicht ignorierte unversionierte Dateien. Das ist ein anderer, ausdrücklich größerer Zuschnitt als die 104 Python-Kern-/Prüfquellen oben: er enthält auch die Werk-Vertragsbeispiele unter verfassungen/, Shellskripte und Konfiguration/Dokumentation. Kein Vermischen mit laufenden Werk-Kopien oder mit ausgeführten Testfällen. Vollständige Liste und disjunkte Gruppensummen in BESTAND.json.

- Gesamtsicht `biotop`: 36 von 129 Dateien, 7237 von 14501 physischen Zeilen.

- Gesamtsicht `kammer`: 1 von 129 Dateien, 4 von 14501 physischen Zeilen.

- Gesamtsicht `pruefung`: 63 von 129 Dateien, 4422 von 14501 physischen Zeilen.

- Gesamtsicht `tests`: 14 von 129 Dateien, 2483 von 14501 physischen Zeilen.

- Gesamtsicht `verfassungen`: 11 von 129 Dateien, 295 von 14501 physischen Zeilen.

- Gesamtsicht `wurzel`: 4 von 129 Dateien, 60 von 14501 physischen Zeilen.

**Quellbindung:** Arbeitsbaum /root/biotop; Git-HEAD `b42dc941e7fcb66632ba6a0e13b8df106a270a31`. HEAD allein bindet den uncommitteten Reparaturstand nicht: 104 von 104 Pythonquellen stimmen per SHA mit dem Auftragsausgang nach Reparatur 02 überein. Keine neue, fehlende oder geänderte Pythonquelle in diesem Auftrag. QUELLSTAND.tar.gz und ARCHIV-INHALT.json binden die tatsächlich verwendeten Bytes.

Eigene Biotop-Tests sind nicht Werk-Tests: aktuell gezielte Bauteilprüfung 33 von 33 ausgeführt/bestanden; letzte vollständige Abnahme aus Reparatur 02: 305 von 305, mit 4 von 4 positiven und 4 von 4 gültigen Gegenproben, echte Vorspann-CLI Exit 0. Diese Vollsuite wurde für die Übergabe nicht unnötig erneut gefahren. Das natürliche Werk in Lauf 26 hat in Gen0/Gen1/Gen3 je 104 von 104 Tests bestanden.[2]

**Betrieb zum Stand 2026-09-20T20:37:24.500072+00:00:** 0 Biotop-/Messprozess-Treffer unter 140 von ps erfassten Prozesszeilen; PID 1921606 zusätzlich einzeln geprüft und beendet. biotop.service: LoadState=not-found, inactive/dead. Docker ps liefert keine laufenden Container. Das ist eine zeitpunktbezogene Systemabfrage, keine Behauptung über die Erreichbarkeit beliebig benannter fremder Dienste. Die Web-Oberfläche wurde in diesem Auftrag nicht gestartet oder per Anmeldung getestet.

Die 15 fachlichen Organe (F6 3.1–3.15) sind nicht dasselbe wie die 19 physischen Python-Organmodule. Folgende Zuordnung nennt vorhandene Pfade und **belegte Aufrufe**, nicht pauschal vollständig erfüllte Anforderungen. Ereigniszähler überlappen fachlich und werden nicht addiert.[1]

- **3.1 Aufnahme:** `biotop/organe/aufnahme.py`. In Lauf 26 1 von 1021 Protokollzeilen vom Typ `aufnahme`.

- **3.2 Landkarte und Straßen:** `biotop/organe/landkarte.py; organe/vertraege.py`. In Lauf 26 1 von 1021 Protokollzeilen vom Typ `landkarte.gebaut`.

- **3.3 Werkverfassung:** `biotop/organe/verfassung.py`. In Lauf 26 1 von 1021 Protokollzeilen vom Typ `verfassung.eingelegt`.

- **3.4 Mentor:** `biotop/organe/mentor.py`. In Lauf 26 1 von 1021 Protokollzeilen vom Typ `mentor.richtungen`.

- **3.5 Maß, Messgerät und Vorstufen:** `biotop/kern/messgeraet.py; organe/vorspann.py, eichung.py, eichgegenstand.py, eichproben.py, generation0.py, jury.py`. In Lauf 26 1 von 1021 Protokollzeilen vom Typ `mass.eingefroren`.

- **3.6 Genesis/Schwarm/Nischen:** `biotop/organe/genesis.py; organe/nischen.py`. In Lauf 26 168 von 1021 Protokollzeilen vom Typ `schwarm.kandidat`.

- **3.7 Aegis/Ankläger:** `biotop/organe/aegis.py`. In Lauf 26 160 von 1021 Protokollzeilen vom Typ `aegis.urteil`.

- **3.8 Nexus/Generalprobe/Verhandlung:** `biotop/lauf.py, insbesondere generation und _verhandeln (kein eigenes Nexus-Modul)`. In Lauf 26 5 von 1021 Protokollzeilen vom Typ `generation.ergebnis`.

- **3.9 Lazarus:** `biotop/organe/lazarus.py`. In Lauf 26 3 von 1021 Protokollzeilen vom Typ `lazarus.schnappschuss`.

- **3.10 Immunisierung:** `biotop/organe/aegis.py; organe/fundpruefung.py; lauf.py`. In Lauf 26 3 von 1021 Protokollzeilen vom Typ `immun.norm`.

- **3.11 Entropie:** `biotop/organe/entropie.py`. In Lauf 26 1 von 1021 Protokollzeilen vom Typ `entropie.saettigung`.

- **3.12 Drei Gedächtnisse:** `biotop/organe/gedaechtnis.py; Mentor und Laufsteuerung als Leser`. In Lauf 26 17 von 1021 Protokollzeilen vom Typ `gedaechtnis.wiederholung`.

- **3.13 Ausführungskammer:** `biotop/organe/kammer.py; kammer/Dockerfile`. In Lauf 26 335 von 335 Kammeraufrufen im separaten Mitschnitt, kein dauerhafter Dienst.

- **3.14 Kasse:** `biotop/kern/kasse.py; anbieter/__init__.py`. In Lauf 26 246 von 1021 Protokollzeilen vom Typ `modell.antwort`.

- **3.15 Web-Oberfläche und Anmeldung:** `biotop/dienst.py; oberflaeche.py; kern/anmeldung.py`. Gebaut; in Lauf 26 nicht aufgerufen. Historische Oberflächenabnahme siehe Phase 3; aktuell kein neuer HTTP-/Login-Beleg.

Vorstufen/Eichproben sind über 06-vorspann (4+4) und 07-gen0 in CLI-AUSGABEN.json belegt, nicht allein über ein direktes Eichproben-Ereignis in der Haupt-DB. Artmuster wurden tatsächlich dem Mentor vorgelegt (7 fremde, 18 eigene), Projektwiederholungen tatsächlich gesperrt. Geschmack existiert und wurde historisch als Mechanik geprüft; dieser Lauf ist kein Nachweis von Philipps echtem Geschmack. Jury wurde einmal aufgerufen; das ist keine neue Gesamt-Abnahme der Jury. Lazarus-Schnappschüsse sind belegt, eine neue vollständige Rückholkampagne fand nicht statt.

**Physische Organmodule: 19 von 19 (ohne __init__.py):** aegis.py (733 Zeilen), aufnahme.py (176 Zeilen), eichgegenstand.py (199 Zeilen), eichproben.py (591 Zeilen), eichung.py (241 Zeilen), entropie.py (103 Zeilen), fundpruefung.py (177 Zeilen), gedaechtnis.py (515 Zeilen), generation0.py (261 Zeilen), genesis.py (145 Zeilen), jury.py (62 Zeilen), kammer.py (122 Zeilen), landkarte.py (255 Zeilen), lazarus.py (110 Zeilen), mentor.py (136 Zeilen), nischen.py (122 Zeilen), verfassung.py (67 Zeilen), vertraege.py (84 Zeilen), vorspann.py (264 Zeilen).

„Nur existent“ ist keine zulässige Schlussfolgerung aus einem fehlenden Modulnamen oder fehlenden direkten Ereignissen. Der aktuelle Lauf belegt die genannten Funktionswege; die einzelnen Sollfunktionen sind damit nicht alle fertig. Besonders Oberfläche, echte Geschmacksentscheidungen, vollständige Rückkehr, robuste Fremdsprachenaufnahme und die unten genannten Mechanismen erhalten durch diese Übergabe keine neue Abnahme.

## (b) Phasenstand und versiegelte Quellen

Die folgenden Zahlen sind **heute aus den Quellen nachgelesene Prüferwertungen**, keine in dieser Sitzung wiederholten historischen Messungen. Historische Wertung, heutiger Reparaturnachweis und Freigabe sind getrennt. Die F6-Zeilen werden nicht selbständig neu addiert oder verbessert.[1]

- **Phase 1:** Erstausgang Lauf 2: 7 von 9; gültiger Nachlaufstand Lauf 9: **9 von 9 bestanden**, Phase 1 abgeschlossen.[1]

- **Phase 2:** F6 führt **9 von 11**. Zeile 7 war am ursprünglichen Paar nicht angenommen/im Werk und wurde später nachbelegt; die historischen Nebenwirkungs-/Regressions-/Norm-/Vertragsproben stehen in F6 als 4 von 4 wieder belegt. Zeile 8 im historischen Hauptlauf: 68,5 % bei 54 erzeugten Tests, Grenze 20 %, gerissen. Die jetzigen 1 von 11 ändern diesen historischen Lauf nicht und erteilen keine neue Gesamtwertung 11/11.[1]

- **Phase 3:** F6 führt ausdrücklich **8 von 11 voll, 1 teilweise, 2 im Nachlauf erledigt**. Nicht zu 11/11 glätten. Projektgedächtnis erfüllt; Jury teilweise; Artgedächtnis und Archivierung im Nachlauf nach den dort benannten natürlichen bzw. gestellten Belegen. Historische Urteile bleiben als solche erhalten, nicht als aktuelle Komplettprüfung des reparierten Systems.[1]

- **Phase 4:** Echtes Werk noch nicht bearbeitet und nicht freigegeben. Vorbedingung 1 hat jetzt einen neuen vollständigen natürlichen Lauf 26: beide geforderten Zahlen erreicht, aber F7-Restbefund K2689 und kein neuer Behebungs-/Immunisierungsgegenstand. **Keine uneingeschränkte Tor-2-Zeile-8-/Phase-4-Abnahme durch Hermes.** Vorbedingungen 2–5 sind in diesem Auftrag nicht ausgeführt. Im F6 gibt es keine spätere Phase mit einem belegten Torstand.[1]

- **Reparatur 01:** ursprüngliche Gesamtfreigabe zurückgenommen; letzter enger Schlussstand negativ, 303 von 305; keine Abnahme daraus. **Reparatur 02:** von Philipp abgenommen, 305 von 305, 4 von 4 positive + 4 von 4 gültige Gegenfälle, CLI Exit 0. Sie repariert KERN-01/02/03, nicht die Außenorte oder vier Phase-4-Lücken.[2][4]

Ein Nachweis aus einem Lauf mit Messgerätwechsel ist kein freigegebener Neustart unter derselben Kennung. Die Bestandsaufnahme belegt insbesondere für Lauf-IDs 22 und 23 Änderungen am Anklägerablauf bei anschließender Fortsetzung; ihr alter natürlicher Wirkungsbeleg steht deshalb unter Satz-2-Vorbehalt. Er wird durch die Reparatur nicht rückwirkend gültig. Die früher zeitweise grüne Norm-Eichwertung war ebenfalls kein gültiger Normnachweis (masse statt mass, norm=[]). Insbesondere diese alten Zahlen nicht als Wirkung des heutigen Quellstands verwenden.[6] Maßgeblich ist die Bindung jedes Belegs an seinen unveränderten Lauf.[1]

### Abholadressen und heute nachgerechnete Prüfsummen

Alle nachstehenden Hüllen wurden gelesen; die von ihnen bezeichnete Dateiliste bzw. das Inhaltsmanifest wurde lokal gehasht und über HTTPS bytegleich nachgelesen. Das ist keine erneute fachliche Prüfung sämtlicher historischer Nutzdateien. Vollständige Einzelabgleiche: PHASEN-QUELLEN.json.

**biotop-phase-1**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/DATEIEN.txt

SHA-256 von `DATEIEN.txt`: `1f71e3293eacee94f1778ccf9b3fc38a2576e31a4b7fe83ec050ff908dd8f299`.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/PRUEFSUMME-ORDNER.txt

**biotop-phase-1-nachlauf**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/DATEIEN.txt

SHA-256 von `DATEIEN.txt`: `eefa6ae7b2cb2b2641506e915500b9c766bac36e5e9fad3d2daa62a57d25488d`.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1-nachlauf/PRUEFSUMME-ORDNER.txt

**biotop-phase-2**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/DATEIEN.txt

SHA-256 von `DATEIEN.txt`: `6b1e7f6a3e27a8830008f787c2e1fdddb62df90237555828767ea7e5d2b277a7`.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-2/PRUEFSUMME-ORDNER.txt

**biotop-phase-3**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/DATEIEN.txt

SHA-256 von `DATEIEN.txt`: `a2b2cee98ecdea5724bc8969721f41ea5b44ffdb037bc3427489cc9ee6f737fb`.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3/PRUEFSUMME-ORDNER.txt

**biotop-phase-3-nachlauf**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/DATEIEN.txt

SHA-256 von `DATEIEN.txt`: `a8bf8eb381e5e28c2fc30153933834a56f2d4f127964e6490aef72f2ce02ece1`.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-3-nachlauf/PRUEFSUMME-ORDNER.txt

**biotop-phase-4-vorbedingung-1** — historischer Vorbedingung-1-Bauteilabschluss, nicht Lauf 26.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/DATEIEN-06.txt

SHA-256 von `DATEIEN-06.txt`: `89a68d30e3539866f7fe1df0575bcb03974f8b5061cb6b6b9362f2359629a239`.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/PRUEFSUMME-ORDNER-06.txt

**biotop-reparatur-01/eskalation-runde-02**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/eskalation-runde-02/DATEIEN.txt

SHA-256 von `MANIFEST.sha256`: `d30b4a46d5251b8bfcfe321f1bc4461642301f88b073c52d816d2243e1d6ff64`.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/eskalation-runde-02/PRUEFSUMME-ORDNER.txt

**biotop-reparatur-02**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/DATEIEN.txt

SHA-256 von `MANIFEST.sha256`: `fa8e5f142d1f6b15e7aef453642874723fe40172ae539aba5cf630fc6dd3f6aa`.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/PRUEFSUMME-ORDNER.txt

**biotop-gesamtstand**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/DATEIEN.txt

SHA-256 von `PRUEFSUMMEN.sha256`: `26163d9ed64c101a27a7bd77d5f0d8755f4ab789c25e8b8c10f36eba158b87f4`.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/PRUEFSUMME-ORDNER.txt

**biotop-wiedereinstieg-2026-09-20-01**

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/DATEIEN-01.txt

SHA-256 von `DATEIEN-01.txt`: `14d6e8740132e5da5177ae78c1987f4753f5f6a6596f5e6967527f7b2201d4ac`.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/PRUEFSUMME-ORDNER-01.txt

Aktuelle Lieferung einschließlich dieser Übergabe:

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-01/DATEIEN.txt

Die eigene Versiegelung steht in PRUEFSUMME-ORDNER.txt und bindet über MANIFEST.sha256 auch dieses Dokument. Sie steht nicht als sich selbst verändernder Hash in der Übergabe.

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-01/PRUEFSUMME-ORDNER.txt

## (c) Offen — nicht durch die Übergabe erledigt

**19 von 19 bestätigten Außenleserorten in 14 Dateien bleiben offen:** 11 Orte in 11 historischen Prüfskripten plus 8 Orte in 3 Produktdateien. Bestätigungsart war teils statischer Kontrollfluss, nicht für jeden Ort ein neuer ausgeführter Produktfall. Die Zeilenangaben unten gehören zum ursprünglichen Auditstand, nicht zu einem neu durchgeführten Außenscan.[3][4]

- `B05:O01` — `biotop/organe/aufnahme.py:133–160`: Positive Text-/Messmarker werden trotz fehlendem Laufabschluss verwertet. Offen.[3]

- `B05:P11` — `pruefung/funde_neubewerten.py:23–43`: Positive Text-/Messmarker werden trotz fehlendem Laufabschluss verwertet. Offen.[3]

- `B05:P37` — `pruefung/tor1_f2.py:24–71`: Positive Text-/Messmarker werden trotz fehlendem Laufabschluss verwertet. Offen.[3]

- `B06:G01` — `biotop/organe/generation0.py:108–113`: Beliebiger Fehlerexit zählt als gefangener Mutant. Offen.[3]

- `B06:G03` — `biotop/organe/generation0.py:180–200`: Beliebiger Fehlerexit zählt als gefangener Mutant. Offen.[3]

- `B06:G04` — `biotop/organe/generation0.py:243–255`: Beliebiger Fehlerexit zählt als gefangener Mutant. Offen.[3]

- `B07:G02` — `biotop/organe/generation0.py:151–174`: Keine Äquivalenzbeobachtung wird als identischer Beobachtungsnachweis gelesen. Offen.[3]

- `B08:L06` — `biotop/lauf.py:554–560`: Leere Nachbarantwortliste zählt als einstimmige Bestätigung. Offen.[3]

- `B09:P41` — `pruefung/verhandlungsprobe.py:57–75`: Fehlendes Paarmaß/Vertragsergebnis zählt als bestanden. Offen.[3]

- `B09:P46` — `pruefung/proben_tor2.py:196–215`: Fehlendes Paarmaß/Vertragsergebnis zählt als bestanden. Offen.[3]

- `B11:L08` — `biotop/lauf.py:634–644`: Gen0-Original-Gegenlauf wird nach Fehler ohne Testzuordnung fortgesetzt. Offen.[3]

- `B12:L09` — `biotop/lauf.py:646–659`: Gen0-Ziel erreicht bei leerer nichtäquivalenter Population. Offen.[3]

- `B13:P02` — `pruefung/anklaeger_vielfalt.py:34–54`: Leere Prüfpoulation erfüllt historisches lokales Gütekriterium. Offen.[3]

- `B13:P29` — `pruefung/nachgang_n2_n3.py:117–168`: Leere Prüfpoulation erfüllt historisches lokales Gütekriterium. Offen.[3]

- `B13:P27` — `pruefung/nachgang_n10.py:49–99`: Leere Prüfpoulation erfüllt historisches lokales Gütekriterium. Offen.[3]

- `B14:P16` — `pruefung/lauf25_auswertung.py:37–108`: Nicht ausgeführte Durchrutscherprüfung wird als gemessen ausgegeben. Offen.[3]

- `B15:P08` — `pruefung/eichung_falld.py:34–41`: Fehlmessung kann historische negative Eichkontrolle erfüllen. Offen.[3]

- `B15:P09` — `pruefung/eichung_pruefen.py:19–50`: Fehlmessung kann historische negative Eichkontrolle erfüllen. Offen.[3]

- `B16:P38` — `pruefung/tor2.py:39–112`: Historische rote-Testzählung verdeckt nicht ausgeführte Tests. Offen.[3]

**Vier von vier Phase-4-Lücken bleiben offen**, einschließlich der engeren Pflicht aus Philipps Auftragsliste:[5]

1. **P4-01 / EICH-1 + MASS-01:** Wirkungskreis aller tatsächlich angewandten Änderungen, transitive Folgen und kumulativ verhandelte Anpassungen. Vorhandene Closure und Einzelguards beweisen keine Vollständigkeit. Einstieg: landkarte.py, aegis.py, lauf.py/_verhandeln.[5]

2. **P4-02 / EICH-3:** Verfassungs-/Vertragsidentität zwischen Vorspann und Maß-Freeze an die versiegelte Datei binden; spätere legitim gemeinsam angenommene Vertragsentwicklung unterscheiden. Ein bestandener Test beweist nicht, dass sein Vertrag nicht abgeschwächt wurde. Einstieg: vorspann.py, lauf.py und aegis.py.[5]

3. **P4-03 / MASS-02:** NaN, Null und andere ungültige Rausch-/Collectorwerte bereichsweise behandeln; gesunde Nachbarn und Verbrauchsbelege bewahren. Vorhandene numerische Unitguards sind kein vollständiger Ende-zu-Ende-Nachweis. Einstieg: kern/messgeraet.py und organe/eichung.py.[5]

4. **P4-04 / EICH-2:** Gen0-Erfolg am Maß-Freeze binden, nicht nur ein vorhandenes generation0.ergebnis-Ereignis. Die Auftragssteuerung von Lauf 26 prüft erreicht=True zusätzlich; das ist kein Fix des Produkt-Gates. Einstieg: organe/vorspann.py und lauf.py.[5]

**Suche unvollständig:** Acht semantische Kandidaten und 45 breite, noch nicht fein zugeordnete Kandidatenzeilen bleiben offen. Das sind verschiedene Suchpopulationen, nicht weitere 53 bestätigte Fehler. Die ursprünglichen 661 Suchzeilen sind ebenfalls keine Fehleranzahl. Kein neuer Außenscan, keine Aussage „keine weiteren gefunden“.[4]

**Tor 2 Zeile 8 bleibt präzise getrennt:** historischer Hauptlauf gerissen; aktuelle vollständige Erzeugungsquote 1/11 unter 20 %; Vollausführung des Angriffstestbestands wegen K2689 nicht durchgehend; neue bestätigte Immunisierung ohne Gegenstand. Am echten Werk ist dieselbe Quote erneut zu messen, nicht aus lagerhaus zu übernehmen.[1]

**Zusätzlicher aktueller Befund, nicht still in die 19 hineingezählt:** K2689, ImportError durch FormelFehemer, zweimal Sammlung mit Exit 2; Anklägerprotokoll meldet gesamt=0 statt eines belastbaren ausgeführten Angriffs. Belege in ABLEHNUNGEN-UND-VERWEISE.json und MESSBELEGE.tar.gz. Keine neue Reparatur, kein Neustart, keine zweite Reviewrunde.

Die größere Bestandsaufnahme enthält weitere benannte Anforderungsabweichungen. Diese Übergabe erklärt sie nicht für erledigt. Für deren damalige Reichweite die unveränderten Berichte im Ordner biotop-gesamtstand lesen; dortige alte Implementierungsbefunde nicht ungeprüft auf den heutigen Reparaturstand übertragen.[6]

## (d) Abschnitt 2a und F7 — unverändert zu übernehmen

Wörtliche sechs Grundsätze aus Fassung 6, Abschnitt 2a; Herkunft und Volltext im Begleitarchiv, Quell-SHA-256 `effefeec0fe2ea0621d4fdca0f27bdd3dae981fd289f1e0b5d56da5aca81aefd`.[1]

1. **Ein fallender Test beweist eine Abweichung, nie ihre Richtung** — welche Seite recht hat, entscheidet nur ein Absturz oder ein Vertrag. (Lauf 16: Fallen am Kandidaten machte aus einem Normtest einen Fund. Nachlauf: Fallen am Ausgang hätte dasselbe getan, 9 von 20.)[1]

2. **Für jede Pflicht muss es einen benannten Befehl geben.** Eine Pflicht, die nur über Notbehelfe erreichbar ist, wird entweder blockiert oder umgeht den Schutz. (Der Abbruch nach Satz 2 war nicht vom Gate gesperrt — es gab ihn schlicht nicht.)[1]

3. **Streuung wird immer zwischen Messungen gebildet, nie innerhalb einer.** Der Median glättet innerhalb, die Streuung misst zwischen; wer beides auf derselben Ebene bildet, misst die Glättung statt der Sache. Gilt für jede Kennzahl über wiederholte Messungen.[1]

4. **Eine Prüfung darf den geprüften Bestand nicht verändern.** Ihr Wirkungsbereich wird vorher eingegrenzt; was sie hinterlässt, wird vor der nächsten Messung zurückgenommen und protokolliert. (Probenabfall in den Gedächtnissen; eine Mechanikprüfung archivierte zwei echte Normtests mit.)[1]

5. **Eine Nachrechnung muss dieselbe Ableitung verwenden wie das geprüfte Organ**, sonst misst sie etwas anderes und erzeugt eine Scheindifferenz. (Drei strittige Projektgedächtnis-Fälle, alle drei aus der Ableitung, keiner aus der Sache.)[1]

6. **Prüfe die Sache, nicht ihre Erscheinung:** Behauptung statt Fundstelle, gesetztes Merkmal statt Name, Verfassung statt Vertragsgröße, Syntaxbaum statt Textanker. (Doppelungserkennung, Probenerkennung, Eichgegenstand, Eichproben — vier Organe, dieselbe Fehlerklasse.)[1]

**F7, Ausführung:** „Ein Nachweis zählt nur, wenn er ausgeführt wurde — übersprungen, abgebrochen, leer oder fehlend gilt als rot, nie als grün.“[7]

**F7, Gegenprobe (direkte Festlegung Philipps im aktuellen Auftrag):** „Jede Probe braucht eine Gegenprobe, die fehlschlagen muss.“ Die Gegenprobe muss gültig ausgeführt sein und dasselbe Bestehensprädikat falsch machen; ein Import-/Infrastrukturabbruch ist nicht die erfolgreiche Gegenprobe. AUFTRAG-REGELN.md bewahrt den Nutzertext, keine erfundene Fassung 7.

Dazu Satz 2: Maß und Messgerät während des Laufs unverändert. Jede Änderung beendet den Lauf; ein neuer beginnt nur ausdrücklich vom gleichen Ausgang, nicht still unter alter Kennung. Keine Schwellenverschiebung wegen eines Fehlschlags. Jede Zahl mit Bezugsgröße; Ausführungsbehauptungen nur mit Rohbeleg. Eigene Entscheidung als eigene bezeichnen.[1][8]

## (e) Verfahrensgrenze

**Aktueller Reviewstatus: ABGEBROCHEN, keine fachliche Reviewabnahme.** Einer von einem beauftragten Durchgängen wurde gestartet; null von einem ist vollständig durch einen unabhängigen Ergebnisbericht belegt. Das selbst gesetzte Zeitlimit betrug 180 Sekunden. Bei der Steuerungskontrolle waren bereits 202,7 Sekunden gemeldet; danach wurde der Stopp angefordert. Die Zeitgrenze wurde von Hermes zu spät kontrolliert. REVIEW.json dieser Lieferung ist ausdrücklich eine Abbruchnotiz der Auftragssteuerung, kein erfundenes unabhängiges Urteil. Kein Ersatzreview und keine Fixrunde. Dieser Verfahrensrest bleibt zusätzlich zum roten F7-Befund offen; die Versiegelung bescheinigt nur die unveränderliche Lieferung, keine Abnahme.

Ein Auftrag, genau ein begrenzter unabhängiger Reviewdurchgang. Keine Fixagenten-Kaskade, kein Audit der Audits, kein doppeltes Elternrepro. Nach einem negativen Schlussreview rote Befunde und Entscheidungspunkte liefern, nicht eigenmächtig weitere Runden anfangen. Der Abschlussordner trägt die vereinbarten Torzeilen; Arbeitszwischenstufen werden nicht komplett gespiegelt. Kosten aller Versuche bleiben abgegrenzt erhalten. Dies ist Philipps direkte Verfahrensfestlegung, nicht aus einer Dateizahl abgeleitet.

Vor jedem Sitzungsende ZWISCHENBERICHT.md und DATEIEN.txt, auch bei Abbruch. Vollständige HTTPS-Abholadresse und Prüfsumme. Alte ausgelieferte Bytes nicht überschreiben; neue nummerierte Revision. Diese Lieferung liegt deshalb unter nach-reparatur-02/abschluss-01; die früheren Statusadressen und der versiegelte Stamm bleiben erhalten.[1][8]

Fachliches dauerhaftes Gedächtnis liegt im Prüfkanal unter laeufe/gedaechtnis/, nicht in einem Obsidian-Tresor. Nur HERMES-1 schreibt dort, HERMES-2/3 lesen. Diese Übergabe ist der aktuelle auftragsbezogene Stand; STAND-01 im Gedächtnisordner ist älter und darf die heutigen Belege nicht ersetzen.[8]

## (f) Nächster Schritt: Vorbedingung 2, Verfassung des Handelssystems

Fassung 6 verlangt diese Reihenfolge: erst Vorbedingung 1 abnehmen/Restbefunde entscheiden, dann die Werkverfassung; danach getrennt Aufnahme/Landkarte, Generation minus eins und Generation 0. Keine dieser nachfolgenden Messungen in der alten Sitzung beginnen.[1]

Philipp schreibt und entscheidet die Verfassung, Hermes legt in der frischen Sitzung einen Entwurf vor. Mindestens aufzunehmen: gesetzliche Hebelgrenzen je Anlageklasse; Tagesverlustgrenze; Ausschluss schädlicher Geschäftsfelder, Rüstung ausdrücklich; kein echter Handel ohne bestandenes Bewertungssystem; Demokonto zuerst; **tragender Orderpfad mit den Risikomodulen und der Verlustgrenze** für den Eichgegenstand. Keine rechtlichen Grenzwerte oder technischen Eintrittspunkte ohne aktuelle Quellen erfinden.[1]

Die Pfadangabe muss in den Regeln ausdrücklich stehen: Eintrittspunkte und Übergänge des tatsächlichen Orderpfads, Risikoprüfungen und Verlustgrenze sowie das geeignete Bereichspaar mit Vertrag. Nicht aus Funktionsnamen, Wortüberdeckung oder Projektgröße erraten. Fehlt der Eintrag, wartet das Organ und kein Lauf beginnt. Hermes darf keine Übungswerk-Vollmacht auf echten Handel übertragen; Freigaben am echten Werk ausschließlich Philipp.[1]

Die in Fassung 6 genannten rund 237.000 Pythonzeilen, 17 Dienste und 135 Testfehlschläge des Handelssystems sind **historische Ausgangsangaben**, in diesem Auftrag nicht am echten Werk nachgemessen. Vor Aufnahme aktuell erheben, nicht als heutige Messwerte übernehmen. Die späteren Budgets 20 EUR für Aufnahme/Landkarte und 5 EUR für Generation minus eins sind F6-Abschnittsvorgaben, keine Freigabe dieses Auftrags; Generation-0-Budget setzt Philipp erst nach dem Voranschlag.[1]

### Arbeitsorte und sichere Startgrenze

- Produktquelle: `/root/biotop`; Pythonumgebung der belegten Ausführung: `/root/reparatur-01/venv/bin/python`. Nicht blind ein neues Environment oder neue Modelle installieren. `README.md` und `requirements-test.txt` beschreiben Eigen-Tests; die belegte Vollsuite/CLI bleibt im Reparatur-02-Ordner.

- Produktiv-DB: `/root/biotop/daten/biotop.db` — nur lesend, keine Initialisierungs-/Migrationshilfe für eine Bestandsabfrage aufrufen. Privater abgeschlossener Lauf 26: `/root/phase-4-vorbedingung-1/privat/biotop.db`; dort ist Werk-ID 23, nicht in der Produktiv-DB. Alte Lauf-IDs 24/25/26 nicht als neue Messung fortsetzen.

- Aktueller Arbeits-/Belegordner: `/root/phase-4-vorbedingung-1`. Produktiv-DB, produktives Werk, ursprüngliche Werkquelle und 104 Pythonquellen wurden gegen den Auftragsausgang unverändert nachgerechnet (TORZEILEN.json, schutz).

- Docker-Kammerimage: `biotop-kammer:1`, gemessene ID `sha256:ce7bbe9441182aea532f147defd99ca757a95d4cb3ff7c3f5c5d9a64965643ee`. Keine Website-/Serverneustarts und keine Anmelde-/API-Geheimnisse in Berichten oder Archiven.

- Keine Generation starten, um den Stand zu lesen. Direkte sqlite3-Verbindung mit `mode=ro` verwenden; SCHLUSSSTATUS.json und schlussdiagnose.py zeigen die verwendeten Abfragen. Erst nach Philipps Entscheidung einen neuen, ausdrücklich begrenzten Auftrag in frischer Sitzung ausführen.

### Abholung dieser vollständigen Übergabe

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-01/UEBERGABE-PHASE-4.md

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-01/DATEIEN.txt

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-01/MANIFEST.sha256

https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-4-vorbedingung-1/nach-reparatur-02/abschluss-01/KASSE.md

## Sources

[1] https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-wiedereinstieg-2026-09-20-01/INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6-01.md
[2] https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/ZWISCHENBERICHT.md
[3] https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/eskalation-runde-02/AUSSERHALB-KERN-BESTAETIGT-OFFEN.md
[4] https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/eskalation-runde-02/ZWISCHENBERICHT.md
[5] https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-02/PHASE4-OFFEN.md
[6] https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/BERICHT.md
[7] https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/eskalation-runde-02/FASSUNG-7-SATZ.md
[8] https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/gedaechtnis/REGELN-01.md
