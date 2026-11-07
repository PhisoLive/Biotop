"""Assemble the fail-closed review from retained tool/test evidence."""
import json
import shlex
from pathlib import Path

out = Path(__file__).resolve().parent
src = Path('/root/reparatur-01/review-01/repo')
proof = json.loads((out/'BELEGE.json').read_text())

def location(rel, start, end=None):
    return {'file':str(src/rel), 'line':start, 'end_line':end or start}

def reproduction(test):
    env = {'PYTHONPATH':str(out/'guard')+':'+str(out/'arbeitskopie'),
           'PYTHONDONTWRITEBYTECODE':'1', 'TMPDIR':str(out/'tmp'),
           'BIOTOP_DB':str(out/'tmp/repro-unused.db'), 'PYTEST_DISABLE_PLUGIN_AUTOLOAD':'1'}
    return ' '.join([f'{k}={shlex.quote(v)}' for k,v in env.items()] +
                    [shlex.quote(s) for s in ['/root/reparatur-01/venv/bin/python','-m','pytest','-q','-s',
                                             '-c',str(out/'arbeitskopie/pytest.ini'),str(out/'test_review.py')+'::'+test]])

def evidence(line):
    return {'file':str(out/'independent-review.stdout.txt'), 'line':line,
            'note':'Vollständige unveränderte stdout-Datei; der Datei-Reader kann lange Einzelzeilen nur in der Darstellung kürzen.'}

errors = [
    {'id':'EICH-1', 'severity':'high', 'priority':'P1',
     'title':'Rauschgesperrter Bereich lässt sich durch einen anders deklarierten Kandidaten verändern',
     **location('biotop/kern/messgeraet.py',432,432),
     'related_locations':[location('biotop/kern/messgeraet.py',463,465), location('biotop/lauf.py',325,330),
                          location('biotop/organe/aegis.py',518,525)],
     'new_or_regressed':'Der Diff setzt Laufzeitgrenzen gesperrter Bereiche außer Kraft und ersetzt den Generalproben-Wirkungskreis durch die Vereinigung gespeicherter Kandidaten-Wirkungskreise. Diese stammen weiterhin nur aus dem deklarierten Bereich, nicht aus den tatsächlich geänderten Dateien.',
     'explanation':'Ein Kandidat für alpha kann zusätzlich paket/beta ändern. Bei unabhängigen Bereichen bleibt sein Wirkungskreis [alpha]. Ist beta rauscherbedingt gesperrt, entfallen jetzt dessen Zeitgrenze und die Wirkungskreissperre zugleich. Der echte Aegis-/Generalprobenpfad legt den Kandidaten vor und schreibt beta. Das ist nicht bloß das zulässige Ignorieren unberührten Nachbarrauschens.',
     'minimal_reproduction':{
        'test':'test_blocked_area_must_include_actual_diff_targets',
        'command':reproduction('test_blocked_area_must_include_actual_diff_targets'),
        'steps':['Frischen privaten Unit-Lauf durch Vorspann → gen0 → mass führen; beta im Vorspann sperren.',
                 'Kandidaten unter bereich=alpha einschleusen, dessen angewandter Diff alpha und beta ändert.',
                 'An der Messgrenze explizite Unit-Werte liefern: alpha.tote_funktionen 1→0, beta.laufzeit_ms 100→10000; übrige Maße unverändert.',
                 'L.generation mit echtem Aegis, Originalurteilen und Generalprobe ausführen; nur Modell-/Mess-/Snapshotgrenzen sind ersetzt.'],
        'expected':'abgelehnt, weil der wirkliche Diff den gesperrten Bereich beta erreicht; kein Schreiben nach beta.',
        'actual':'status=vorgelegt; wirkungskreis=[alpha]; paket/beta/__init__.py wurde im privaten Werk auf return 2 geändert. Derselbe Messinput ohne neuen Rausch-Skip wird wegen beta.laufzeit_ms 10000 > 200 abgelehnt.',
        'evidence_level':'Ausgeführter Unit-Durchlauf bis zur tatsächlichen Dateischreibstelle an synthetischem Werk. Zahlen sind kontrollierte Testeingaben, keine gemessenen Laufzeiten.'},
     'evidence':[evidence(13)],
     'suggested_fix':'Wirkungskreis aus allen angewandten Code-/Anpassungsdateien plus deren Abhängigkeiten ableiten und vor Einzelprüfung sowie Generalprobe mit den gesperrten Bereichen schneiden; nicht bloß der Bereichsdeklaration vertrauen.'},
    {'id':'EICH-2', 'severity':'high', 'priority':'P1',
     'title':'Fehlgeschlagene Generation 0 erfüllt die neue Maß-Vorbedingung',
     **location('biotop/organe/vorspann.py',227,229),
     'related_locations':[location('biotop/lauf.py',83,83), location('biotop/lauf.py',108,116),
                          location('biotop/lauf.py',652,660),location('biotop/__main__.py',110,111)],
     'new_or_regressed':'Die neu eingeführte Stufensperre prüft nur, ob nach dem Vorspann irgendein generation0.ergebnis für die Lauf-ID existiert; den Ergebnisinhalt prüft sie nicht. Die bereits vorher vorhandene CLI-Erfolgsrückgabe wird nicht als separate Regression gezählt.',
     'explanation':'generation0.ergebnis wird auch mit erreicht=false geschrieben. Damit bescheinigt die neue Sperre einen nicht bestandenen Mutantenfang als ausreichende Vorstufe, friert das Maß ein und setzt status=bereit. Der Abschluss eines fehlgeschlagenen Versuchs ist kein erfolgreicher Eignungsnachweis.',
     'minimal_reproduction':{
        'test':'test_failed_gen0_must_block_mass_and_cli',
        'command':reproduction('test_failed_gen0_must_block_mass_and_cli'),
        'steps':['Privaten frischen Unit-Lauf mit kontrolliert grünem Vorspann anlegen.',
                 'Original-CLI gen0 aufrufen: ein nichtäquivalenter Mutant, gefangen=0, Testbau liefert keine neuen Tests.',
                 'Original-CLI mass 1 --bestaetigt-von Review-Unit aufrufen.'],
        'expected':'Maß-Gate lehnt erreicht=false ab, mass bleibt NULL, kein gebundener Generation-0-Schnappschuss.',
        'actual':'Gen0 erfasst erreicht=false, ziel=1, gefangen_nachher=0. mass gibt dennoch rc=0, bindet mass_sha256 und setzt den Lauf auf bereit; stderr bleibt leer.',
        'evidence_level':'Ausgeführte CLI-/DB-/Protokollmechanik im Unit-Prozess; Mutantenmessung, Modelltestbau und Snapshot sind explizite Doubles.'},
     'evidence':[evidence(9)],
     'suggested_fix':'Einen gültigen, erfolgreichen Gen0-Quellbeleg verlangen: erreicht is True und belastbare positive Bezugsgröße/Zielerfüllung. Neueren gescheiterten oder abgebrochenen Versuch nicht durch einen beliebigen älteren Ergebnisdatensatz überdecken.'},
    {'id':'EICH-3', 'severity':'high', 'priority':'P1',
     'title':'Eichvertrag kann nach dem Vorspann ohne Invalidierung ausgetauscht werden',
     **location('biotop/organe/vorspann.py',241,245),
     'related_locations':[location('biotop/organe/vorspann.py',54,59), location('biotop/organe/vorspann.py',176,180),
                          location('biotop/organe/vertraege.py',38,51)],
     'new_or_regressed':'Die neue Nachweisbindung überprüft den versiegelten Gegenstand am Ende der Batterie, aber nicht an den späteren Eingängen. _quellen enthält weder aktuelle Vertragsdateien noch die Eichgegenstandsidentität/-prüfsumme.',
     'explanation':'Mit der regulären Verträge-Aufnahme lässt sich die tatsächlich geeichte Vertragsdatei zwischen Vorspann und Gen0 ersetzen. Quell-/Nachweis-Hashes und Protokollkette bleiben für das Gate gültig, weil es nur den historischen Nachweis und eine unvollständige aktuelle Quellenmenge vergleicht. Der gespeicherte Eichgegenstand trägt dann eine andere Prüfsumme als seine reale Datei.',
     'minimal_reproduction':{
        'test':'test_sealed_contract_replacement_after_vorspann_must_invalidate',
        'command':reproduction('test_sealed_contract_replacement_after_vorspann_must_invalidate'),
        'steps':['V.ausfuehren an frischem privatem Unit-Lauf abschließen.',
                 'vertraege.einlegen für dasselbe Paar aufrufen und den Vertragsinhalt ändern; keine Nachweis-/Hashzeile manipulieren.',
                 'V.verlangen(gen0), L.generation0, L.mass_einfrieren und V.verlangen(generation) ausführen.'],
        'expected':'Mindestens vor Gen0/Freeze den geänderten Eichgegenstand erkennen, Nachweis invalidieren und neuen Lauf verlangen.',
        'actual':'Alle genannten Eingänge akzeptieren. proof_status=bestanden, run_status=bereit, hash_chain_valid=true; gespeicherte Vertragssumme eef7c5d03a3d4fa3d872a2505f030e1329a684f1caace0516e208ca61ee0bf2d, tatsächliche Summe 013afbc9971d951c8a013af2bc8319420e2a7b98839a74d0ccffa997e9077824.',
        'evidence_level':'Ausgeführte echte Vertragsdatei-/DB-/Hashkettenoperationen nur an Unit-Beständen; Eichung/Messung sind kontrollierte Doubles.'},
     'evidence':[evidence(11)],
     'suggested_fix':'Den versiegelten Gegenstand an den Vorstufeneingängen gegen aktuellen Datensatz und Datei prüfen. Legitime spätere Vertragsänderungen durch Verhandlung von nicht legitimierten Austauschoperationen unterscheiden; nicht pauschal jede normale Werkentwicklung verbieten.'},
    {'id':'EICH-4', 'severity':'high', 'priority':'P1',
     'title':'Vertragsgegenprobe kann an ihrem eigenen kopierten Test scheitern und trotzdem als gültig falsch zählen',
     **location('biotop/organe/eichproben.py',349,360),
     'related_locations':[location('biotop/organe/eichproben.py',239,246), location('biotop/organe/eichproben.py',416,418),
                          location('biotop/organe/eichproben.py',431,436)],
     'new_or_regressed':'Der neue AST-Testklon übernimmt nur Importknoten und die Testfunktion. Benötigte Modulkonstanten/Hilfsdefinitionen werden nicht übernommen und nicht als fehlende Voraussetzung erkannt. Die neue Kontrollwertung prüft nur Verbraucherzeugen, nicht die Ausführbarkeit des geklonten Vertragstests.',
     'explanation':'Ein regulärer Verbraucher-Test assert bericht(EINGABE) == 3 mit EINGABE=2 auf Modulebene erfüllt die Auswahlbedingungen. Im geklonten Vertrag fehlt EINGABE. Positiv- und Gegenprobe fallen daher beide im Test mit NameError, bevor der Verbraucher im Vertrag aufgerufen wird. Der separate originale Verbrauchertest fällt positiv wegen fehlender Zusicherung und besteht nach Anpassung. Genau deshalb wird das all(...)-Prädikat True/False, obwohl derselbe benannte Vertrag in beiden Fällen defekt bleibt. Zwei gültige Messhüllen machen diesen Fixturefehler derzeit nicht unprüfbar.',
     'minimal_reproduction':{
        'test':'test_contract_countercase_is_not_allowed_to_fail_inside_cloned_test',
        'command':reproduction('test_contract_countercase_is_not_allowed_to_fail_inside_cloned_test'),
        'steps':['Kleines eigenes Beispielwerk: bericht(zahl) liefert zahl+1; Testmodul importiert bericht, setzt EINGABE=2 und prüft bericht(EINGABE)==3.',
                 '_vertrag_vorbereiten jeweils mit gegenprobe=False/True aufrufen.',
                 'Generierten Vertrag und originalen Verbraucher über den originalen JUnit-Parser mit lokalem pytest an der ausschließlich selbst geschriebenen Fixture ausführen.',
                 '_bestanden(vertrag, ...) mit den realen Verbraucherzeugen und ausdrücklich gestellter Unit-Messeinbettung auswerten.'],
        'expected':'Angepasste Gegenprobe besteht den konkret benannten Vertrag; andernfalls pruefbar=false, keine gültige Negativkontrolle. Positivprobe muss den Vertragsbruch statt eines NameError des Tests belegen.',
        'actual':'Beide generierten Vertragstests liefern NameError: name EINGABE is not defined, bestaetigt=false, Ort tests/vertraege/test_vertrag_abnehmer_lieferant.py. Originaler Verbraucher: positiv AttributeError im Werk, negativ bestanden. Original-Prädikat mit expliziter Unit-Messhülle: positiv=true, negativ=false.',
        'evidence_level':'Tatsächlich ausgeführte lokale pytest-Zeugen am eigenen synthetischen Werk, kein Docker. Prädikat-Messeinbettung ist ein gekennzeichneter Unit-Input; keine behauptete Ausführung der vollständigen Eichbatterie.'},
     'evidence':[evidence(15), {'file':str(out/'contract-local-pytest-raw.json'),'line':26,'end_line':73},
                 {'file':str(out/'contract-junit-summary.json')}],
     'suggested_fix':'Abhängigkeiten des übernommenen Tests mitnehmen oder eine nicht eigenständig ausführbare Fixture ausdrücklich unprüfbar machen. Zusätzlich den benannten Vertragstest selbst paarweise ausführen und eine gültige Gegenprobe nur dann anerkennen, wenn dessen spezifischer Bruch tatsächlich verschwindet und kein Fixture-/Sammelfehler vorliegt.'},
]
suggestions = [
    {'id':'EICH-S1','title':'Qualitätsgrenze unabhängig von Erfolgsflags härten', **location('biotop/organe/vorspann.py',66,78),
     'explanation':'_qualitaet akzeptiert acht Bool-Hüllen ohne belege/mass/kammer und ohne Ausführungsrohbeleg; im Unit-Test erhält dieser Input positive=4, negative=4. Das allein beweist keinen zusätzlichen nativen End-to-End-Bypass und wird deshalb nicht als eigener Blocker gezählt. Die Grenze sollte Mindeststruktur und Mechanikbelege prüfen, statt lediglich den Produzentenflags zu vertrauen.',
     'evidence':[evidence(17)], 'minimal_reproduction':reproduction('test_proof_quality_needs_mechanism_not_boolean_envelope')},
    {'id':'EICH-S2','title':'Normkontrolle um echte kontrakt-/absturzgestützte Gegenklasse ergänzen', **location('biotop/organe/eichproben.py',284,288),
     'explanation':'Die vorhandene Gegenprobe entfernt Normtest und Angriff vollständig aus dem Anklagepfad. Das ist brauchbar gegen den früheren Null-/Leerobjekt-Grünpfad, prüft aber nicht, ob ein ausgeführter berechtigter Test aus der Normklasse herauskommt. Ergänzend einen tatsächlich übergebenen, gültigen Vertrag-/Absturzfall durch denselben Klassifikator schicken. Keine Behauptung, dass diese zusätzliche Gegenklasse hier ausgeführt wurde.'},
    {'id':'EICH-S3','title':'Rohbelege aller Vorspannstufen behalten', **location('biotop/organe/vorspann.py',151,164),
     'explanation':'Die Proben sammeln Kammerergebnisse, Rauschmessung/Fund-Neubewertung werden im neuen Pflichtpfad aber ohne solche Rohaufzeichnung aufgerufen. _messen_einmal gibt nur Bereichszeiten zurück; fundpruefung.bewerten verwirft ausgabe. Für die gesamte Pflichtvorspann-Abnahme fehlen dadurch im Nachweis der originale stdout/stderr/rc dieser Stufen. Vorgelagerte Hilfsfunktionen sind Bestandsbestand, deshalb hier Transparenz-/Härtungsempfehlung statt eigenständiger neuer Logikblocker.',
     'related_locations':[location('biotop/organe/eichung.py',111,113),location('biotop/organe/fundpruefung.py',55,77)]},
]
probe_assessment = [
    {'name':'nebenwirkung', 'read_locations':[location('biotop/organe/eichproben.py',217,222),location('biotop/organe/eichproben.py',291,310)],
     'positive':'Realer privater Ausgangsdefekt in A wird rückgängig gemacht und B geschädigt; Prädikat verlangt Gewinn in A und Verlust in B.',
     'counter':'B-Schaden aus dem Diff entfernen, A-Reparatur behalten.', 'actual_docker_pair_executed_by_this_review':False},
    {'name':'regression', 'read_locations':[location('biotop/organe/eichproben.py',223,235),location('biotop/organe/eichproben.py',313,332)],
     'positive':'Vorher grüner konkreter B-Test wird als bestätigter Fehler nachgewiesen; drei triviale grüne Tests werden separat ausgeführt, ursprüngliche Regression-je-Test-Zeile ist Pflicht.',
     'counter':'B unverändert, grüne Zugaben bleiben.', 'actual_docker_pair_executed_by_this_review':False},
    {'name':'norm', 'read_locations':[location('biotop/organe/eichproben.py',247,288)],
     'positive':'Vorhandene importierbare Funktion; bestätigte Assertion vor Änderung, grüner Test danach, kein Verweis, konkreter offen_norm-Eintrag, expliziter Nullzuwachs und Ausschluss aus finalem Dateisatz.',
     'counter':'Gleiche Verhaltensänderung und externe Zeugen, aber Test/Angriff fehlt im Anklagepfad; Einschränkung EICH-S2.', 'actual_docker_pair_executed_by_this_review':False},
    {'name':'vertrag', 'read_locations':[location('biotop/organe/eichproben.py',335,374)],
     'positive':'Neue Zusicherung wird im vorhandenen Verbraucher benutzt, Nachbar bleibt unverändert.',
     'counter':'Nachbar liefert die neue Zusicherung; Gegenprobe ist wegen EICH-4 nicht generell brauchbar.',
     'actual_docker_pair_executed_by_this_review':False, 'additional_local_executed_countercase':'EICH-4'}]

review = {'passed':False, 'security_concerns':[], 'logic_errors':errors, 'suggestions':suggestions,
          'summary':'Nicht freigabefähig: vier neu eingeführte/regressierte Logikfehler mit ausgeführten isolierten Repros; keine Repositoryänderung.',
          'scope':{'diff':str(src.parent/'AENDERUNGEN.diff'),'static_scan':str(src.parent/'STATIK.json'),
                   'source_context_only':str(src),'output':str(out),
                   'implementation_performed':False,'source_repository_modified':False,
                   'semantic_focus':'Vier Eichproben/Gegenproben, Pflichtvorspann, CLI, Stufenfolge, Satz-2-Bindung und tatsächliche Wirkung der Rauschbereichssperre.'},
          'static_scan_disposition':[{'file':str(src/'biotop/organe/kammer.py'),'line':103,'rule':'secret',
                                      'false_positive':True,'reason':'token ist der von ContextVar.set gelieferte Rücksetz-Token; finally ruft _ZAEHLUNGEN.reset(token) auf. Kein Zugangstoken, kein Geheimnisliteral.'}],
          'positive_verified_properties':['Echter Gate-/Bindungs-Unitpfad erreicht nach Vorspann → erfolgreicher Gen0 → Freeze den Generationskörper und übergibt die kalibrierten Toleranzen.',
                                          'Fehlender Vorspann, Maß vor Gen0, spätes Gen0, wiederholtes Maß, manipuliertes Instrument/Verfassung/Nachweis sowie ungültige Rauschstrukturen werden in den ausgeführten Unit-Fällen gesperrt.',
                                          'Explizit nicht ausgeführte oder nicht prüfbare Gegenproben werden für alle vier Namen von _vollstaendig abgelehnt.',
                                          '_privat isoliert DB- und Werkwrites in der zusätzlichen eigenen Unit-Prüfung; Originalfixture bleibt bytegleich.'],
          'four_probe_assessment':probe_assessment,
          'execution_evidence':{'runs':json.loads((out/'executions.json').read_text()),
                                'test_summary':[{'suite':s['suite'],'cases':s['collected_and_executed'],'outcomes':s['outcomes']} for s in proof['test_results']],
                                'source_unchanged':proof['source_unchanged_content_size_mtime'],
                                'source_inventory_before':str(out/'repo-vorher.json'),'source_inventory_after':str(out/'repo-nachher.json'),
                                'docker_runs':0,'network_calls':0,'paid_model_calls':0,
                                'note':'Grüne Unit-Anzahl wird nicht als bestandenes Vier-Paare-Kammerverfahren ausgegeben. Die sechs lokalen pytest-Wrapper in EICH-4 sind Unterprozesse innerhalb eines Repros, keine sechs zusätzlichen vollständigen Eichproben.'},
          'loc':{k:proof[k] for k in ('source_file_count','total_physical_lines','python_files','python_code_lines_token_method','diff_files','diff_added_lines','diff_deleted_lines','diff_physical_lines','loc_definition')},
          'full_loc_and_output_accounting':str(out/'BELEGE.json'),
          'limitations':['Keine Docker-Kammerläufe parallel zur Elternabnahme; die vollständigen vier Positiv-/Gegenpaare wurden hier deshalb nicht als echte Kammerabnahme ausgeführt und erhalten kein Abnahmegrün.',
                         'Keine produktive DB, keine produktiven Werke und kein Bestandsreplay. Alle Prüfskript-/DB-/Werk-/Berichtsschreiboperationen betreffen nur pruefer-eichung. Separat wurde eine allgemeine Methodenregel im Agent-Skill measurement-harness-discipline/references/self-check-battery.md ergänzt; kein Repositorycode wurde geändert.',
                         'EICH-1 bis EICH-3 sind Unit-Belege mit ausdrücklich ersetzten Mess-/Modell-/Infrastrukturgrenzen. EICH-4 führt eigene synthetische Tests lokal real aus, seine Prädikat-Messhülle bleibt Unit-Input.',
                         'Kein globaler Neuauftrag: nicht geänderte Grundprobleme werden nicht als neue Blocker gezählt.']}
assert review['passed'] is False and len(review['logic_errors']) == 4
(out/'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=2))

# Complete source excerpts, with exact line numbers, for every cited code range.
locations = []
for item in errors + suggestions:
    locations.append({k:item[k] for k in ('file','line','end_line')})
    locations.extend(item.get('related_locations', []))
unique = {(r['file'],r['line'],r['end_line']) for r in locations}
excerpts = []
for filename,start,end in sorted(unique):
    lines = Path(filename).read_text().splitlines()
    excerpts += [f'\n### {filename}:{start}-{end}\n']
    excerpts += [f'{i}|{lines[i-1]}' for i in range(max(1,start-2),min(len(lines),end+2)+1)]
(out/'CODEBELEGE.txt').write_text('\n'.join(excerpts)+'\n')

report = f'''# Unabhängige Eichungsprüfung: NICHT BESTANDEN

**passed=false. Vier Logikfehler; keine bestätigten neuen Sicherheitsfunde.**
`kammer.py:103 token=_ZAEHLUNGEN.set(...)` ist ein ContextVar-Rücksetz-Token,
kein Zugangstoken. Keine Implementierung, kein Schreibzugriff auf das geprüfte Repository.

## Blocker

1. **EICH-1 — Bereichssperre umgehbar.** `biotop/kern/messgeraet.py:432,463–465`
   und `biotop/lauf.py:325–330` prüfen den deklarierten statt des tatsächlichen
   Änderungsbereichs. Ein als **alpha** geführter Diff verändert **beta**, obwohl
   beta gesperrt ist. Der ausgeführte Unit-Durchlauf endet **vorgelegt** und
   schreibt beta. Ohne den neuen Skip lehnt derselbe Messinput die Zeitgrenze ab.
2. **EICH-2 — Gen0-Fehlschlag gilt als Vorbedingung.**
   `biotop/organe/vorspann.py:227–229` verlangt nur einen Ergebnisdatensatz.
   Im Repro: `erreicht=false`, **0 von 1** Mutanten gefangen; danach trotzdem
   CLI-`mass` **rc=0**, Maß gebunden, Lauf **bereit**.
3. **EICH-3 — Eichvertrag nachträglich austauschbar.**
   `biotop/organe/vorspann.py:54–59,241–245` bindet die aktuelle Vertragsdatei
   nicht. Reguläres `vertraege.einlegen` nach dem Vorspann ändert die Prüfsumme;
   Gen0, Freeze und Generationsgate akzeptieren weiter **bestanden** bei gültiger
   Protokollkette. Kein nachträgliches Manipulieren des Nachweises nötig.
4. **EICH-4 — unbrauchbare Vertragsgegenprobe.**
   `biotop/organe/eichproben.py:349–360` kopiert Imports und Testfunktion, aber
   keine benötigte Modulkonstante. Ein normaler Test mit `EINGABE=2` erzeugt
   dadurch in **beiden** Vertragsvarianten einen `NameError` im Test selbst.
   Der ursprüngliche Verbraucher besteht nach Anpassung; deshalb ergibt das
   Originalprädikat dennoch **True/False**, obwohl der benannte Vertrag weiter
   defekt ist. Lokale pytest-Rohbelege liegen bei; die Prädikat-Messhülle ist
   ausdrücklich ein Unit-Input, keine vorgetäuschte Docker-Messung.

## Verifiziert und begrenzt

- Mitgelieferte fokussierte Suite: **116/116 Unit-Fälle bestanden**.
- Eigene Repros: **4 Fehler / 2 bestandene Fälle**; zusätzlicher Isolations- und
  Nichtausführungscheck: **5/5 bestanden**. Einzelne IDs und Ergebnisse in `BELEGE.json`.
- Positive Route Vorspann → Gen0 → Freeze → Generationskörper ausgeführt;
  fehlende Reihenfolge, Instrument-/Maßmanipulation und fehlende Kontrollen geprüft.
- Vier Probeprädikate und ihre Konstruktion gelesen. Die vollständigen vier
  Dockerpaare **nicht ausgeführt**; fehlende Ausführung wird nicht als negative
  Gegenprobe oder Abnahmegrün gezählt. Normkontrolle ohne Klassifikatoreingabe,
  reine Bool-Hüllen am Qualitätsgate und lückenhafte Rohbelege weiterer
  Vorspannstufen stehen als Empfehlungen in `REVIEW.json`.
- **0 Dockerläufe, 0 Netzaufrufe, 0 bezahlte Modellaufrufe.** Nur selbst angelegte
  synthetische Fixtures/private Datenbanken; kein produktiver Bestand verwendet.
- Alle **{proof['source_file_count']} Quelldateien** sind nach Inhalt, Größe und mtime unverändert.
  Diff: **{proof['diff_files']} Dateien, +{proof['diff_added_lines']}/−{proof['diff_deleted_lines']} Zeilen**.
  Quellsnapshot: **{proof['total_physical_lines']} physische Zeilen**; vollständige
  Dateiliste, Token-LOC-Definition, Prüfsummen und Outputzählung in `BELEGE.json`.

## Dateien und Wiederholung

- Ergebnis mit exakten Fundstellen und minimalen Repro-Befehlen:
  `{out/'REVIEW.json'}`
- Vollständige LOC-/Test-/Quellbelege: `{out/'BELEGE.json'}`
- Ungekürzte Ausgaben: `provided-unit.stdout.txt`, `independent-review.stdout.txt`,
  `supplemental.stdout.txt`, jeweilige stderr- und JUnit-Dateien.
- Vertragszeugen: `contract-local-pytest-raw.json`, `contract-junit-summary.json`.
- Repros: `test_review.py`; sichere Auswahlaufrufe vollständig in `REVIEW.json`.
- Manifest: `{out/'SHA256SUMS.txt'}`

Die vier roten eigenen Tests prüfen die geforderte Sperrwirkung; ihr Exit 1
ist der reproduzierte Produktbefund, kein Sammel-/Importfehler. Unveränderte
Altprobleme werden nicht als zusätzliche Reparaturblocker gezählt.
'''
(out/'BERICHT.md').write_text(report)
print(json.dumps({'passed':review['passed'],'security_concerns':len(review['security_concerns']),
                  'logic_errors':len(errors),'suggestions':len(suggestions),
                  'review':str(out/'REVIEW.json'),'report':str(out/'BERICHT.md')},ensure_ascii=False))
