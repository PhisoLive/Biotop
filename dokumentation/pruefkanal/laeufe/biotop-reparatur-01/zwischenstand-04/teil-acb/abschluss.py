"""Build local deliverables from captured outputs; never modify source repo/DB."""
from collections import Counter
import csv
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

R = Path(__file__).resolve().parent
repo = R / 'repo'
data = json.loads((R / 'bestandspruefung-02.json').read_text())
assert (R / 'bestandspruefung-02.json').read_bytes() == (R / 'bestandspruefung-03.json').read_bytes()
s = data['summary']
xml = ET.parse(R / 'ausgaben/eigentests.xml')
tests = list(xml.iter('testcase'))
assert all(t.find('failure') is None and t.find('error') is None for t in tests)

before = json.loads((R / 'schutz-vorher.json').read_text())
after = {p: {'sha256': hashlib.sha256(Path(p).read_bytes()).hexdigest(), 'mtime_ns': Path(p).stat().st_mtime_ns,
             'size': Path(p).stat().st_size} for p in before}
changed = [p for p in before if before[p] != after[p]]
assert before['/root/reparatur-01/ausgang.db'] == after['/root/reparatur-01/ausgang.db']
head = subprocess.check_output(['git', '-C', '/root/biotop', 'rev-parse', 'HEAD'], text=True).strip()
status = subprocess.check_output(['git', '-C', '/root/biotop', 'status', '--porcelain=v1'], text=True)
assert head == 'b42dc941e7fcb66632ba6a0e13b8df106a270a31'

(R / 'schutz-nachher.json').write_text(json.dumps(after, indent=2) + '\n')
protection = {'geschuetzte_dateien': len(before), 'geaendert': changed, 'git_head': head, 'git_status_porcelain': status,
              'db': after['/root/reparatur-01/ausgang.db'], 'db_identisch': True,
              'vorher_nachher_identisch': before == after,
              'hinweis': 'Originalrepo wurde waehrend des Teilauftrags ausserhalb dieses Teilpatches veraendert. Keine Ruecknahme fremder Aenderungen.'}
(R / 'schutz-ergebnis.json').write_text(json.dumps(protection, indent=2) + '\n')

files = ['biotop/organe/aegis.py', 'biotop/organe/gedaechtnis.py', 'pytest.ini',
         'tests/conftest.py', 'tests/test_ansage_aufnahme.py', 'tests/test_artvorlage.py', 'tests/test_doppelungsschluessel.py']
diff = ''
for f in files:
    oldpath = R / 'baseline' / f
    old = oldpath.read_text() if oldpath.exists() else ''
    new = (repo / f).read_text()
    diff += ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                        fromfile='a/' + f if oldpath.exists() else '/dev/null', tofile='b/' + f))
(R / 'reparatur-acb.diff').write_text(diff)
(R / 'QUELLDATEIEN.txt').write_text('\n'.join(str(repo / f) for f in files) + '\n')

security = []
patterns = {'secret': r'(?i)(api_key|secret|password|token|passwd)\s*=\s*[\"\'][^\"\']{6,}',
            'shell': r'os\.system\(|shell\s*=\s*True', 'eval_exec': r'\b(?:eval|exec)\(', 'pickle': r'pickle\.loads?\('}
for n,line in enumerate(diff.splitlines(), 1):
    if line.startswith('+') and not line.startswith('+++'):
        for label,pattern in patterns.items():
            if re.search(pattern, line):
                security.append({'line': n, 'type': label})
assert not security, security
(R / 'ausgaben/19-statische-pruefung.json').write_text(json.dumps({'added_lines_security_hits': security,
    'independent_reviewer': 'nicht ausgeführt: keine zusätzlichen Modellaufrufe autorisiert; Integration/Review beim Parent',
    'changed_files': files}, indent=2) + '\n')

def csvfile(name, entries):
    with (R / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(entries[0]))
        w.writeheader()
        for r in entries:
            w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()})

crows = []
for r in data['c_historischer_vorrat_replay']:
    for t in r['tests']:
        item = {'entscheidung': f"I{r['id']}::{t['test']}", 'immun_id': r['id'], 'kandidat': r['kandidat'],
                'lauf_id': r['lauf_id'], 'werk_id': r['werk_id'], 'bereich': r['bereich'], 'zeitpunkt': r['erstellt_am'],
                **t, 'alt_gesperrt': [t['test'], t['schluessel']] in r['alt']['sperren'],
                'neu_gesperrt': [t['test'], t['schluessel']] in r['neu']['sperren']}
        crows.append(item)
csvfile('C-ENTSCHEIDUNGEN.csv', crows)
csvfile('A-ANSAGEN.csv', [{k:r.get(k) for k in ('nr','zeit','lauf_id','werk_id','bereich','kandidat','kategorie','behauptung','zeugen','historisch_ausgefuehrt','alt','neu')} for r in data['ansagen']])
csvfile('B-VORLAGEN.csv', [{'werk_id': r['werk_id'], 'familie': r['familie'], 'population': r['population'],
    'fremde_muster_eindeutig_ids': r['fremde_muster_eindeutig_ids'], 'alt_gezeigt': r['alt']['gezeigt_ids'],
    'neu_gezeigt': r['neu']['gezeigt_ids'], 'alt_fremd': r['alt']['fremde'], 'neu_fremd': r['neu']['fremde'],
    'alt_eigen': r['alt']['eigene'], 'neu_eigen': r['neu']['eigene'], 'neu_mindestzahl': r['neu']['fremd_mindestzahl']}
    for r in data['b_organaufruf']])
csvfile('KANDIDATEN-ABDECKUNG.csv', data['kandidaten_abdeckung'])

ambiguous = [r for r in crows if r['nur_unzugeordnete_ansage']]
within_only = [r for r in crows if r['gleicher_schluessel_frueher_im_batch'] and not r['zeugen']]
new = [r for r in crows if not r['erwartet_sperren_mit_vollstaendigem_rekonstruiertem_vorrat']]
roles = data['ac_aktuelle_eigene_ansage_rollenrekonstruktion']
assert len(crows) == len(roles)
assert len(data['kandidaten']) == sum(s['kandidaten'].values())
assert len(data['immunsystem']) == sum(s['immunsystem'].values())
assert len(crows) == s['c_sicherer_immuntest_vorbestand'] + len(ambiguous) + len(within_only) + len(new)
role_pairs = Counter((r['erwartet_sperren'],r['alt_gesperrt'],r['neu_gesperrt']) for r in roles)
assert role_pairs[(False,True,False)] > 0
assert role_pairs[(True,True,True)] > 0
brows = [r for r in data['b_organaufruf'] if r['population']=='natuerlich_bereinigt' and r['werk_id'] in (20,22)]

lines = [
'# Reparatur A/C und B – isolierter Teilauftrag',
'',
'## Ergebnis und Beweisart',
'',
f'- **{len(tests)} gesammelte und ausgeführte pytest-Eigentests bestanden**; ursprüngliche Rot/Grün-Ausgaben liegen unverändert in `ausgaben/`.',
'- A/C: ausschließlich die Protokollnummer der aktuellen eigenen Ansage ausgenommen, nicht der Behauptungsschlüssel. Fund- und Norm-Eintritt erhalten dieselbe Kennung. Frühere eigene/fremde Ansagen sowie bereits im selben Angriff aufgenommene Immuntests bleiben sperrend.',
'- B: ungerades Fenster aufrunden; fremde Population vor jeder Mengenbegrenzung auswählen und vollständig deduplizieren. Keine Pflichtverweise.',
'- **Bestandsnachweis = deterministischer Replay/Organaufruf, kein Live-Lauf.** Die A/C-Selbstansage wird zusätzlich ausdrücklich als Rollenrekonstruktion ausgewiesen; sie ist keine historisch bewiesene Ansage–Kandidaten-Verknüpfung.',
'- **Originalrepo-Unveränderlichkeit NICHT erfüllt:** Die Endprüfung fand Änderungen außerhalb dieses Teilpatches (Details unten). Dieser Teilauftrag änderte Produktionscode ausschließlich in seiner Quellkopie und nahm keine fremden Änderungen zurück. Die private Ausgangs-DB blieb nachweislich unverändert.',
'- Keine Modell-, Anbieter-, Netzwerk- oder Kammerausführung. Netz/Anbieter/Kammer sind im Harness und in den Eigentests gesperrt.',
'',
'## Vollständige Populationen und Bezugsgrößen',
'',
f'- Kandidaten: {len(data["kandidaten"])} = {s["kandidaten"]["natuerlich"]} natürlich + {s["kandidaten"]["gestellt"]} gestellt. Jeder Kandidat steht mit Kennung in der JSON und in `KANDIDATEN-ABDECKUNG.csv`.',
f'- Immunsystem: {len(data["immunsystem"])} Zeilen = {s["immunsystem"]["natuerlich"]} natürliche + {s["immunsystem"]["gestellt"]} gestellte. Natürliche: {s["natuerliche_original_immuneintraege"]} Originalaufnahmen + {s["natuerliche_uebernommene_immuneintraege"]} Übernahmen; Übernahmen bleiben zeitgerecht Vorrat, werden nicht als neue Angriffe gezählt.',
f'- Natürliche Kandidatenabdeckung: {json.dumps(s["natuerliche_kandidaten_abdeckung"],ensure_ascii=False)}. Die nicht gespeicherten Angriffscodes sind **nicht replaybar**; keine künstlichen Ersatztests. Mehrere Urteile je Kandidat bleiben über ihre Protokollnummern getrennt.',
f'- Artgedächtnis: {len(data["artgedaechtnis"])} Einträge, alle per Kandidatenkennung natürlich zuordenbar. Keine Bereinigung entfernt einen Art-Eintrag.',
f'- Ansagen: {s["ansagen"]}, sämtlich ohne Kandidatenkennung. Keine Paarung mit Urteilen nach Reihenfolge. Ihre Aufnahmeentscheidungen können ohne zusätzliche Belege nicht historischen Kandidaten zugewiesen werden.',
'',
'## C: gesamter rekonstruierter Entscheidungsvorrat',
'',
f'{len(crows)} reale gespeicherte Testfunktionen aus {len(data["c_historischer_vorrat_replay"])} natürlichen Originalaufnahmen wurden Alt/Neu durch `aufnahmesperre` geprüft. Vollständige Einzelzeilen: `C-ENTSCHEIDUNGEN.csv` und JSON `c_historischer_vorrat_replay`.',
'',
'| Kategorie | Testentscheidungen |', '|---|---:|',
f'| Schlüssel bereits durch natürlichen Immuntest im Vorbestand belegt | {s["c_sicherer_immuntest_vorbestand"]} |',
f'| Nur früherer gleichartiger Test innerhalb derselben gespeicherten Aufnahmegruppe | {len(within_only)} |',
f'| Nur Ansage ohne beweisbare Kandidatenbindung (historisch unentscheidbar) | {len(ambiguous)} |',
f'| Neu gegen gesamten rekonstruierten Vorrat und Aufnahmegruppe | {len(new)} |',
f'| Summe | {len(crows)} |',
'',
f'Der Vollvorrats-Replay sperrt {s["c_neu_sperren"]} und lässt {s["c_neu_aufnehmen"]} passieren. Darin ist die unentscheidbare Ansage-Zeile enthalten; **nicht** als bewiesene historische Doppelung ausgeben. Alt und Neu ohne rekonstruierte aktuelle Eigenansage haben auf diesem Bestand dieselben Entscheidungen.',
'',
'Natürliche konkrete Doppelungszeugen (keine Seed-/Pfadproben):',
]
for r in data['c_historischer_vorrat_replay']:
    if r['id'] in (337,338):
        for t in r['tests']:
            lines.append(f'- I{r["id"]}, K{r["kandidat"]}, `{r["name"]}::{t["test"]}` → `{t["schluessel"]}`; frühere natürliche Gegenstücke: {", ".join(w for w in t["zeugen"] if w.startswith("I"))}; Alt/Neu gesperrt.')
lines += [
'',
'**Historische Zuordnungsgrenze:** I339 / K2526, `gesamtmenge|Eq:zahl`, trifft ausschließlich P15143 (Ansage vor Aufnahme). P15143 trägt keine Kandidatenkennung. Wäre dies die aktuelle Eigenansage, wäre die richtige neue Entscheidung Aufnahme; wäre es eine echte frühere Ansage, wäre Sperren richtig. Beides wird nicht durch Reihenfolge entschieden. Der konservative Vollvorrats-Replay belässt P15143 im Vorrat und nennt die Zeile unentscheidbar.',
'',
'## A/C: aktuelle eigene Ansage als explizite Rollenrekonstruktion',
'',
f'Pro realer Testfunktion wird auf derselben zeitlichen Kopie ausschließlich eine aktuelle Eigenansage aus ihrem tatsächlichen AST-Schlüssel eingetragen. Die Testcodes, Kandidaten-IDs und Vorratszeilen bleiben real. Jede der {len(roles)} Rollenentscheidungen ist in der JSON vollständig bezeichnet; keine davon wird als neu beobachteter natürlicher Angriff verkauft.',
'',
'| Erwartung gegen Vorrat vor der rekonstruierten Eigenansage | Alt | Neu | Anzahl |',
'|---|---|---|---:|',
]
for (expected, old, neu), n in sorted(role_pairs.items()):
    lines.append(f'| {"sperren" if expected else "aufnehmen"} | {"gesperrt" if old else "aufgenommen"} | {"gesperrt" if neu else "aufgenommen"} | {n} |')
lines += [
'',
f'Relativ zu dieser deklarierten Rollenrekonstruktion: falsche Sperrungen {s["rollenrekonstruktion_alt_falsche_sperren"]}/{len(roles)} → {s["rollenrekonstruktion_neu_falsche_sperren"]}/{len(roles)}; neue Durchrutscher {s["rollenrekonstruktion_neu_durchrutscher"]}/{len(roles)}. Das ist ein Mechaniknachweis am realen gespeicherten Material, **keine historische Falschpositivrate**. Die innerhalb eines ursprünglichen Testbatches wiederholten Tests werden hier absichtlich einzeln auf ihrem jeweiligen Vorbestand geprüft; ihre Batch-Doppelung steht separat in C.',
'',
'## A: Ansage-Replay',
'',
f'Alle {s["ansagen"]} aufgezeichneten Ansagen durch die echte `_angriff`-Entscheidung, am Generator-Eintritt ausdrücklich angehalten: {json.dumps(s["a_neu"],ensure_ascii=False)}. Alt/Neu gleich; keine zusätzliche Einsparungswirkung am eingefrorenen Bestand behauptet. `A-ANSAGEN.csv` enthält jede P-Nummer. Die fehlende Kandidatenbindung betrifft alle Ansagen.',
'',
'## B: echte Vorlagen Alt/Neu',
'',
'| Werkfamilie / repräsentatives Werk | verfügbare eindeutige fremde Muster | Alt fremd/eigen | Neu fremd/eigen |',
'|---|---:|---:|---:|',
]
for r in brows:
    lines.append(f'| {r["familie"]} / W{r["werk_id"]} | {len(r["fremde_muster_eindeutig_ids"])} | {r["alt"]["fremde"]}/{r["alt"]["eigene"]} | {r["neu"]["fremde"]}/{r["neu"]["eigene"]} |')
    (R / f'B-W{r["werk_id"]}-ALT.txt').write_text(r['alt']['vorlagentext']+'\n')
    (R / f'B-W{r["werk_id"]}-NEU.txt').write_text(r['neu']['vorlagentext']+'\n')
lines += ['', 'Gezeigte echte fremde IDs:']
for r in brows:
    lines.append(f'- W{r["werk_id"]}: Alt {r["alt"]["fremde_ids"]}; Neu {r["neu"]["fremde_ids"]}. Eigene IDs und sämtliche verfügbaren fremden IDs: JSON/B-VORLAGEN.csv; gerenderte Texte: `B-W{r["werk_id"]}-ALT.txt` / `B-W{r["werk_id"]}-NEU.txt`.')
lines += [
'',
f'Alle {len(data["b_organaufruf"]) // 2} Werk-IDs wurden roh und natürlich bereinigt geprüft ({s["b_werk_population_kombinationen"]} Werk/Populationskombinationen; keine unabhängigen Wiederholungsproben). B-Verletzungen Alt {s["b_alt_verletzungen"]}, Neu {s["b_neu_verletzungen"]}. Lagerhaus kann mangels weiterer fremder Muster den Halbanteil nicht erreichen; alle verfügbaren werden gezeigt. Der Gesamtlimit-Fehler oberhalb des alten Fensters wird durch rote/grüne Unitfälle nachgewiesen, **nicht** durch diesen kleineren realen angenommenen Bestand. Keine Konsumentenzitate gemessen.',
'',
'## TDD, Artefakte und Grenzen',
'',
'| Vertikaler TDD-Schritt | ursprüngliches Rot | ursprüngliches Grün |', '|---|---|---|',
'| A/C eigene Ansage, beide Eintrittsstellen | `01-ac-rot.txt` | `02-ac-gruen.txt` |',
'| B ungerades Fenster | `03-b-haelfte-rot.txt` | `04-b-haelfte-gruen.txt` |',
'| B fremder Vorrat nicht im Gesamtfenster verstecken | `05-b-vorrat-rot.txt` | `06-b-vorrat-gruen.txt` |',
'| C vollständiger Vorrat statt begrenzter Fenster | `07-c-vorrat-rot.txt` | `08-c-vorrat-gruen.txt` |',
'| A Entscheidung nicht am Promptfenster abschneiden | `09-a-vorrat-rot.txt` | `10-a-vorrat-gruen.txt` |',
'| Ansage-Kandidatenbindung auch für Sperre/Abstinenz | `11-ansagebindung-rot.txt` | `12-eigentests-gruen.txt` |',
'',
'- Weitere bereits grüne Charakterisierungstests decken unveränderte AST-Schlüsselregeln und Randfälle ab; sie werden nicht als neue Rot→Grün-Reparaturen ausgegeben.',
'- `pytest.ini` macht die isolierten Eigentests über `python -m pytest` auffindbar. Werk-Vertragsschablonen unter `verfassungen/` sind keine Biotop-Eigentests und werden nicht ungeprüft als Suite gezählt.',
'- Test-/Ausführungsaußenwelt der gestellten Integrationstests ersetzt; Aufnahmeentscheidungen/Schlüssel/SQLite-Schreiben bleiben echt. Hauptnachweis ist der getrennte echte Bestands-Replay.',
'- Zeitliche Transformationen stehen vorab in MESSPLAN.md: SQLite-Backup in RAM, Zugangstabellen nur dort entfernt, Immunsystem/Ansagevorrat auf Entscheidungszeit rekonstruiert. Keine private DB-Kopie wird ausgeliefert.',
'- Nachträglich zurückgeschriebene Schlüssel (P12476) beschreiben die damals vorhandenen Tests retrospektiv. Gelöschte historische Einträge, ursprüngliche Generatorantworten und damalige Quellwerk-Ausführungen sind nicht rekonstruierbar.',
f'- Unvollständige bestehende AST-Schlüssel mit `?`: {json.dumps(s["testschluessel_mit_fragezeichen"],ensure_ascii=False)}. Diese Semantik ist nicht Teil der Reparatur; daraus keine vollständige semantische Doppelungsgarantie ableiten.',
f'- Historische C-Ereignisse: {json.dumps(s["historische_c_ereignisse"],ensure_ascii=False)}. Keine natürliche Live-C-Wirksamkeit daraus abgeleitet. Die gelöschte K2680-Probe ist durch explizite Protokoll-Kandidaten-ID plus Probe-Nische belegt, nicht durch die Reihenfolge.',
'- Die Bestandsdatei `bestandspruefung-01.json` und Ausgabe 14 sind eine frühere Erfassung ohne die spätere Kandidaten-Abdeckung/Probe-Aufschlüsselung; **maßgeblich sind 02/03**. Die Entscheidungen selbst blieben gleich.',
'- Kein unabhängiger zusätzlicher Modellreview ausgeführt; Parent soll die Integration gegen seine parallel bearbeitete Aegis-Prüfsignatur prüfen. Kein Commit und keine produktive Integration erfolgt.',
'',
'## Reproduktion und Integrationsoberfläche',
'',
'```sh', f'cd {repo}', '/root/reparatur-01/venv/bin/python -m pytest -vv',
 f'cd {R}', '/root/reparatur-01/venv/bin/python bestandspruefung.py neuer-replay.json', '```',
'',
'- Diff: `reparatur-acb.diff`; Quellpfade: `QUELLDATEIEN.txt`.',
'- `_angriff` behält seine Dreier-Rückgabe; zusätzliche optionale Schlüsselwortparameter `kandidat_id` und `ansage_kontext`. `pruefen`-Signatur unverändert. Beide C-Aufnahmestellen erhalten `eigene_ansage_nr=ansage_kontext.get("nr")`.',
'- `bisherige_behauptungen`: `limit=None` für vollständige Entscheidungsmenge, `ohne_ansage_nr` für genau eine Zeile. A-Modellprompt bleibt auf sein bisheriges Fenster beschränkt, mechanische Entscheidung nicht.',
'- `art_lesen`: `limit=None` und optionales `fremd_zu`; bestehende Aufrufpositionen bleiben kompatibel.',
'- In diesem Teilpatch nicht geändert: lauf.py, __main__.py, messgeraet.py, eichung.py und eichproben.py. Zusätzlich wurde die allgemeine Replay-Vorgehensweise als Skill-Referenz im aktiven Hermes-Profil dokumentiert; keine andere Profilkonfiguration geändert.',
'',
'## Unveränderlichkeit, Kosten und Reproduzierbarkeit',
'',
f'- {len(before)} Dateien geprüft (Originalrepo plus private Ausgangs-DB). {len(changed)} Originalrepo-Dateien haben abweichende Inhalte/mtime: {changed}. Zusätzlich zeigt `git status` neue ungetrackte Dateien (vollständig in schutz-ergebnis.json). Die Änderungen liegen NICHT im A/C/B-Teilpatch; Urheberschaft nicht aus der Dateiprüfung ableitbar. **Keine Behauptung eines unveränderten Originalrepos.** Original-Git HEAD blieb {head}. Einzelbelege: `schutz-vorher.json`, `schutz-nachher.json`, `schutz-ergebnis.json`.',
f'- DB-SHA256: `{data["db_sha256_vorher"]}`.',
f'- Bestands-Replay 02 und 03 bytegleich, SHA256 `{hashlib.sha256((R/"bestandspruefung-02.json").read_bytes()).hexdigest()}`. Beide enthalten vollständige ID-Listen und dieselben Entscheidungen.',
f'- Kasse: {s["kasse_zeilen_unveraendert"]} unveränderte Bestandszeilen; keine Biotop-Modell-/Anbieterausführung. Kosten des übergeordneten Assistenten führt der Parent, nicht dieses Ledger.',
'',
'## Vollständige Abholpfade',
'',
]
for name in ['BERICHT.md','reparatur-acb.diff','QUELLDATEIEN.txt','bestandspruefung.py','MESSPLAN.md','bestandspruefung-02.json','bestandspruefung-03.json','C-ENTSCHEIDUNGEN.csv','A-ANSAGEN.csv','B-VORLAGEN.csv','KANDIDATEN-ABDECKUNG.csv','ausgaben/17-fulltests.txt','ausgaben/eigentests.xml','DATEIEN.txt','PRUEFSUMMEN.txt','KASSE.md']:
    lines += [str(R/name), '']
(R / 'BERICHT.md').write_text('\n'.join(lines)+'\n')
(R / 'KASSE.md').write_text('# Lokale Kostenabgrenzung\n\nKeine Biotop-Modell-, Anbieter-, Netzwerk- oder Kammerausführung. Netzwerk/Anbieter/Kammer-Abwehr ist im Harness und in den Eigentests installiert. Keine Anbieterantwort wird im Replay erfunden; A hält vor Testgenerierung an. Original-DB inklusive Kasse ist bytegleich.\n\nAssistenten-/Subagent-Budget führt der Parent gesondert. Keine Aussage „Gesamtauftrag 0 €“.\n')
print(json.dumps({'tests_passed':len(tests),'source_files':len(files),'protected_files':len(before),
                  'c_rows':len(crows),'c_within_only':len(within_only),'c_unknown':len(ambiguous),'report':str(R/'BERICHT.md')},indent=2))
