# Reparatur A/C und B – isolierter Teilauftrag

## Ergebnis und Beweisart

- **42 gesammelte und ausgeführte pytest-Eigentests bestanden**; ursprüngliche Rot/Grün-Ausgaben liegen unverändert in `ausgaben/`.
- A/C: ausschließlich die Protokollnummer der aktuellen eigenen Ansage ausgenommen, nicht der Behauptungsschlüssel. Fund- und Norm-Eintritt erhalten dieselbe Kennung. Frühere eigene/fremde Ansagen sowie bereits im selben Angriff aufgenommene Immuntests bleiben sperrend.
- B: ungerades Fenster aufrunden; fremde Population vor jeder Mengenbegrenzung auswählen und vollständig deduplizieren. Keine Pflichtverweise.
- **Bestandsnachweis = deterministischer Replay/Organaufruf, kein Live-Lauf.** Die A/C-Selbstansage wird zusätzlich ausdrücklich als Rollenrekonstruktion ausgewiesen; sie ist keine historisch bewiesene Ansage–Kandidaten-Verknüpfung.
- **Originalrepo-Unveränderlichkeit NICHT erfüllt:** Die Endprüfung fand Änderungen außerhalb dieses Teilpatches (Details unten). Dieser Teilauftrag änderte Produktionscode ausschließlich in seiner Quellkopie und nahm keine fremden Änderungen zurück. Die private Ausgangs-DB blieb nachweislich unverändert.
- Keine Modell-, Anbieter-, Netzwerk- oder Kammerausführung. Netz/Anbieter/Kammer sind im Harness und in den Eigentests gesperrt.

## Vollständige Populationen und Bezugsgrößen

- Kandidaten: 2679 = 2633 natürlich + 46 gestellt. Jeder Kandidat steht mit Kennung in der JSON und in `KANDIDATEN-ABDECKUNG.csv`.
- Immunsystem: 379 Zeilen = 346 natürliche + 33 gestellte. Natürliche: 242 Originalaufnahmen + 104 Übernahmen; Übernahmen bleiben zeitgerecht Vorrat, werden nicht als neue Angriffe gezählt.
- Natürliche Kandidatenabdeckung: {"kein_gespeicherter_Angriffstest_oder_kein_Urteil": 2097, "Immuntestcode_replaybar": 239, "Angriff_protokolliert_aber_kein_Immuntestcode_gespeichert": 297}. Die nicht gespeicherten Angriffscodes sind **nicht replaybar**; keine künstlichen Ersatztests. Mehrere Urteile je Kandidat bleiben über ihre Protokollnummern getrennt.
- Artgedächtnis: 699 Einträge, alle per Kandidatenkennung natürlich zuordenbar. Keine Bereinigung entfernt einen Art-Eintrag.
- Ansagen: 90, sämtlich ohne Kandidatenkennung. Keine Paarung mit Urteilen nach Reihenfolge. Ihre Aufnahmeentscheidungen können ohne zusätzliche Belege nicht historischen Kandidaten zugewiesen werden.

## C: gesamter rekonstruierter Entscheidungsvorrat

426 reale gespeicherte Testfunktionen aus 242 natürlichen Originalaufnahmen wurden Alt/Neu durch `aufnahmesperre` geprüft. Vollständige Einzelzeilen: `C-ENTSCHEIDUNGEN.csv` und JSON `c_historischer_vorrat_replay`.

| Kategorie | Testentscheidungen |
|---|---:|
| Schlüssel bereits durch natürlichen Immuntest im Vorbestand belegt | 214 |
| Nur früherer gleichartiger Test innerhalb derselben gespeicherten Aufnahmegruppe | 51 |
| Nur Ansage ohne beweisbare Kandidatenbindung (historisch unentscheidbar) | 1 |
| Neu gegen gesamten rekonstruierten Vorrat und Aufnahmegruppe | 160 |
| Summe | 426 |

Der Vollvorrats-Replay sperrt 266 und lässt 160 passieren. Darin ist die unentscheidbare Ansage-Zeile enthalten; **nicht** als bewiesene historische Doppelung ausgeben. Alt und Neu ohne rekonstruierte aktuelle Eigenansage haben auf diesem Bestand dieselben Entscheidungen.

Natürliche konkrete Doppelungszeugen (keine Seed-/Pfadproben):
- I337, K2458, `norm_k2458_lager::test_reservierung_einloesen_wirft_nicht_genug_bestand_bei_ueberschreitung` → `reservierung_einloesen|raises:NichtGenugBestand`; frühere natürliche Gegenstücke: I315, I331; Alt/Neu gesperrt.
- I338, K2500, `aegis_k2500_preise::test_artikel_negativer_grundpreis_erlaubt_bypass` → `preis_fuer|GtE:zahl`; frühere natürliche Gegenstücke: I336; Alt/Neu gesperrt.

**Historische Zuordnungsgrenze:** I339 / K2526, `gesamtmenge|Eq:zahl`, trifft ausschließlich P15143 (Ansage vor Aufnahme). P15143 trägt keine Kandidatenkennung. Wäre dies die aktuelle Eigenansage, wäre die richtige neue Entscheidung Aufnahme; wäre es eine echte frühere Ansage, wäre Sperren richtig. Beides wird nicht durch Reihenfolge entschieden. Der konservative Vollvorrats-Replay belässt P15143 im Vorrat und nennt die Zeile unentscheidbar.

## A/C: aktuelle eigene Ansage als explizite Rollenrekonstruktion

Pro realer Testfunktion wird auf derselben zeitlichen Kopie ausschließlich eine aktuelle Eigenansage aus ihrem tatsächlichen AST-Schlüssel eingetragen. Die Testcodes, Kandidaten-IDs und Vorratszeilen bleiben real. Jede der 426 Rollenentscheidungen ist in der JSON vollständig bezeichnet; keine davon wird als neu beobachteter natürlicher Angriff verkauft.

| Erwartung gegen Vorrat vor der rekonstruierten Eigenansage | Alt | Neu | Anzahl |
|---|---|---|---:|
| aufnehmen | gesperrt | aufgenommen | 211 |
| sperren | gesperrt | gesperrt | 215 |

Relativ zu dieser deklarierten Rollenrekonstruktion: falsche Sperrungen 211/426 → 0/426; neue Durchrutscher 0/426. Das ist ein Mechaniknachweis am realen gespeicherten Material, **keine historische Falschpositivrate**. Die innerhalb eines ursprünglichen Testbatches wiederholten Tests werden hier absichtlich einzeln auf ihrem jeweiligen Vorbestand geprüft; ihre Batch-Doppelung steht separat in C.

## A: Ansage-Replay

Alle 90 aufgezeichneten Ansagen durch die echte `_angriff`-Entscheidung, am Generator-Eintritt ausdrücklich angehalten: {"Testgenerierung_erreicht_aber_nicht_ausgefuehrt": 34, "abstinent": 22, "gesperrt": 34}. Alt/Neu gleich; keine zusätzliche Einsparungswirkung am eingefrorenen Bestand behauptet. `A-ANSAGEN.csv` enthält jede P-Nummer. Die fehlende Kandidatenbindung betrifft alle Ansagen.

## B: echte Vorlagen Alt/Neu

| Werkfamilie / repräsentatives Werk | verfügbare eindeutige fremde Muster | Alt fremd/eigen | Neu fremd/eigen |
|---|---:|---:|---:|
| logmuehle / W20 | 15 | 12/13 | 13/12 |
| lagerhaus / W22 | 7 | 7/18 | 7/18 |

Gezeigte echte fremde IDs:
- W20: Alt [623, 454, 416, 360, 359, 249, 175, 141, 132, 68, 61, 33]; Neu [623, 454, 416, 360, 359, 249, 175, 141, 132, 68, 61, 33, 15]. Eigene IDs und sämtliche verfügbaren fremden IDs: JSON/B-VORLAGEN.csv; gerenderte Texte: `B-W20-ALT.txt` / `B-W20-NEU.txt`.
- W22: Alt [597, 569, 568, 296, 281, 271, 270]; Neu [597, 569, 568, 296, 281, 271, 270]. Eigene IDs und sämtliche verfügbaren fremden IDs: JSON/B-VORLAGEN.csv; gerenderte Texte: `B-W22-ALT.txt` / `B-W22-NEU.txt`.

Alle 22 Werk-IDs wurden roh und natürlich bereinigt geprüft (44 Werk/Populationskombinationen; keine unabhängigen Wiederholungsproben). B-Verletzungen Alt 4, Neu 0. Lagerhaus kann mangels weiterer fremder Muster den Halbanteil nicht erreichen; alle verfügbaren werden gezeigt. Der Gesamtlimit-Fehler oberhalb des alten Fensters wird durch rote/grüne Unitfälle nachgewiesen, **nicht** durch diesen kleineren realen angenommenen Bestand. Keine Konsumentenzitate gemessen.

## TDD, Artefakte und Grenzen

| Vertikaler TDD-Schritt | ursprüngliches Rot | ursprüngliches Grün |
|---|---|---|
| A/C eigene Ansage, beide Eintrittsstellen | `01-ac-rot.txt` | `02-ac-gruen.txt` |
| B ungerades Fenster | `03-b-haelfte-rot.txt` | `04-b-haelfte-gruen.txt` |
| B fremder Vorrat nicht im Gesamtfenster verstecken | `05-b-vorrat-rot.txt` | `06-b-vorrat-gruen.txt` |
| C vollständiger Vorrat statt begrenzter Fenster | `07-c-vorrat-rot.txt` | `08-c-vorrat-gruen.txt` |
| A Entscheidung nicht am Promptfenster abschneiden | `09-a-vorrat-rot.txt` | `10-a-vorrat-gruen.txt` |
| Ansage-Kandidatenbindung auch für Sperre/Abstinenz | `11-ansagebindung-rot.txt` | `12-eigentests-gruen.txt` |

- Weitere bereits grüne Charakterisierungstests decken unveränderte AST-Schlüsselregeln und Randfälle ab; sie werden nicht als neue Rot→Grün-Reparaturen ausgegeben.
- `pytest.ini` macht die isolierten Eigentests über `python -m pytest` auffindbar. Werk-Vertragsschablonen unter `verfassungen/` sind keine Biotop-Eigentests und werden nicht ungeprüft als Suite gezählt.
- Test-/Ausführungsaußenwelt der gestellten Integrationstests ersetzt; Aufnahmeentscheidungen/Schlüssel/SQLite-Schreiben bleiben echt. Hauptnachweis ist der getrennte echte Bestands-Replay.
- Zeitliche Transformationen stehen vorab in MESSPLAN.md: SQLite-Backup in RAM, Zugangstabellen nur dort entfernt, Immunsystem/Ansagevorrat auf Entscheidungszeit rekonstruiert. Keine private DB-Kopie wird ausgeliefert.
- Nachträglich zurückgeschriebene Schlüssel (P12476) beschreiben die damals vorhandenen Tests retrospektiv. Gelöschte historische Einträge, ursprüngliche Generatorantworten und damalige Quellwerk-Ausführungen sind nicht rekonstruierbar.
- Unvollständige bestehende AST-Schlüssel mit `?`: [{"immun_id": 135, "test": "test_reservierung_einloesen_ohne_vorherige_reservierung_bricht_vertrag", "schluessel": "AssertionError|?"}, {"immun_id": 178, "test": "test_reservierung_einloesen_ohne_reservierung_gibt_keinen_fehler", "schluessel": "reservierung_einloesen|?"}, {"immun_id": 181, "test": "test_entnehmen_ohne_vorherigen_zugang_ueber_bestands_dict", "schluessel": "fail|?"}]. Diese Semantik ist nicht Teil der Reparatur; daraus keine vollständige semantische Doppelungsgarantie ableiten.
- Historische C-Ereignisse: {"nicht_zuordenbar": 3, "nicht_zuordenbar_lauf_passt_nicht": 1, "gestellt_belegt_durch_urteil_nische": 10}. Keine natürliche Live-C-Wirksamkeit daraus abgeleitet. Die gelöschte K2680-Probe ist durch explizite Protokoll-Kandidaten-ID plus Probe-Nische belegt, nicht durch die Reihenfolge.
- Die Bestandsdatei `bestandspruefung-01.json` und Ausgabe 14 sind eine frühere Erfassung ohne die spätere Kandidaten-Abdeckung/Probe-Aufschlüsselung; **maßgeblich sind 02/03**. Die Entscheidungen selbst blieben gleich.
- Kein unabhängiger zusätzlicher Modellreview ausgeführt; Parent soll die Integration gegen seine parallel bearbeitete Aegis-Prüfsignatur prüfen. Kein Commit und keine produktive Integration erfolgt.

## Reproduktion und Integrationsoberfläche

```sh
cd /root/reparatur-01/teil-acb/repo
/root/reparatur-01/venv/bin/python -m pytest -vv
cd /root/reparatur-01/teil-acb
/root/reparatur-01/venv/bin/python bestandspruefung.py neuer-replay.json
```

- Diff: `reparatur-acb.diff`; Quellpfade: `QUELLDATEIEN.txt`.
- `_angriff` behält seine Dreier-Rückgabe; zusätzliche optionale Schlüsselwortparameter `kandidat_id` und `ansage_kontext`. `pruefen`-Signatur unverändert. Beide C-Aufnahmestellen erhalten `eigene_ansage_nr=ansage_kontext.get("nr")`.
- `bisherige_behauptungen`: `limit=None` für vollständige Entscheidungsmenge, `ohne_ansage_nr` für genau eine Zeile. A-Modellprompt bleibt auf sein bisheriges Fenster beschränkt, mechanische Entscheidung nicht.
- `art_lesen`: `limit=None` und optionales `fremd_zu`; bestehende Aufrufpositionen bleiben kompatibel.
- In diesem Teilpatch nicht geändert: lauf.py, __main__.py, messgeraet.py, eichung.py und eichproben.py. Zusätzlich wurde die allgemeine Replay-Vorgehensweise als Skill-Referenz im aktiven Hermes-Profil dokumentiert; keine andere Profilkonfiguration geändert.

## Unveränderlichkeit, Kosten und Reproduzierbarkeit

- 112 Dateien geprüft (Originalrepo plus private Ausgangs-DB). 4 Originalrepo-Dateien haben abweichende Inhalte/mtime: ['/root/biotop/.gitignore', '/root/biotop/biotop/kern/messgeraet.py', '/root/biotop/biotop/lauf.py', '/root/biotop/biotop/organe/eichung.py']. Zusätzlich zeigt `git status` neue ungetrackte Dateien (vollständig in schutz-ergebnis.json). Die Änderungen liegen NICHT im A/C/B-Teilpatch; Urheberschaft nicht aus der Dateiprüfung ableitbar. **Keine Behauptung eines unveränderten Originalrepos.** Original-Git HEAD blieb b42dc941e7fcb66632ba6a0e13b8df106a270a31. Einzelbelege: `schutz-vorher.json`, `schutz-nachher.json`, `schutz-ergebnis.json`.
- DB-SHA256: `711b2bbdca478f7f0de941a88cc51e72c46c9c7a20a3a908065f42861520fe14`.
- Bestands-Replay 02 und 03 bytegleich, SHA256 `94649b7f95981f6eb123638c80446251ac9ebecb3086302c01a27d134abd04be`. Beide enthalten vollständige ID-Listen und dieselben Entscheidungen.
- Kasse: 4070 unveränderte Bestandszeilen; keine Biotop-Modell-/Anbieterausführung. Kosten des übergeordneten Assistenten führt der Parent, nicht dieses Ledger.

## Vollständige Abholpfade

/root/reparatur-01/teil-acb/BERICHT.md

/root/reparatur-01/teil-acb/reparatur-acb.diff

/root/reparatur-01/teil-acb/QUELLDATEIEN.txt

/root/reparatur-01/teil-acb/bestandspruefung.py

/root/reparatur-01/teil-acb/MESSPLAN.md

/root/reparatur-01/teil-acb/bestandspruefung-02.json

/root/reparatur-01/teil-acb/bestandspruefung-03.json

/root/reparatur-01/teil-acb/C-ENTSCHEIDUNGEN.csv

/root/reparatur-01/teil-acb/A-ANSAGEN.csv

/root/reparatur-01/teil-acb/B-VORLAGEN.csv

/root/reparatur-01/teil-acb/KANDIDATEN-ABDECKUNG.csv

/root/reparatur-01/teil-acb/ausgaben/17-fulltests.txt

/root/reparatur-01/teil-acb/ausgaben/eigentests.xml

/root/reparatur-01/teil-acb/DATEIEN.txt

/root/reparatur-01/teil-acb/PRUEFSUMMEN.txt

/root/reparatur-01/teil-acb/KASSE.md

