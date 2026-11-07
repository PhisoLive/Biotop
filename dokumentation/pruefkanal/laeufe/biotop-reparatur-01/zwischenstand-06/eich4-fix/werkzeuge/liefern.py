"""Lieferartefakte aus echten Rohbelegen; keine Ergebnisse synthetisieren."""
import csv
import difflib
import hashlib
import importlib.util
import json
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path('/root/reparatur-01/nachbesserung-01/vertrag')
OUT = ROOT / 'lieferung'
OUT.mkdir(exist_ok=True)
CHANGED = ['biotop/organe/eichproben.py', 'tests/test_eichproben.py', 'tests/test_review_vertrag.py']

def files(root):
    return {p.relative_to(root).as_posix(): p for p in root.rglob('*') if p.is_file()}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

before, after = files(ROOT / 'ausgang-repo'), files(ROOT / 'repo')
changed = sorted(p for p in before.keys() | after.keys()
                 if p not in before or p not in after or sha(before[p]) != sha(after[p]))
assert changed == sorted(CHANGED), changed
parts = []
for rel in CHANGED:
    src, dst = ROOT / 'ausgang-repo' / rel, ROOT / 'repo' / rel
    target = OUT / 'dateien' / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(dst, target)
    if src.exists():
        target = OUT / 'basis' / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)
    parts.append(''.join(difflib.unified_diff(src.read_text().splitlines(True) if src.exists() else [],
                 dst.read_text().splitlines(True), fromfile='a/'+rel if src.exists() else '/dev/null', tofile='b/'+rel)))
(OUT / 'AENDERUNGEN.diff').write_text(''.join(parts))

spec = importlib.util.spec_from_file_location('sichern', ROOT / 'werkzeuge/sichern.py')
sichern = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sichern)
vor = json.loads((ROOT / 'ausgaben/quellschutz-vorher.json').read_text())
nach = sichern.inventar()
(ROOT / 'ausgaben/quellschutz-nachher.json').write_text(json.dumps(nach, indent=2))
bewegung = {p: {'vorher':vor.get(p), 'nachher':nach.get(p)} for p in vor.keys() | nach.keys() if vor.get(p) != nach.get(p)}
byteaenderungen = {p:d for p,d in bewegung.items() if not d['vorher'] or not d['nachher']
                  or d['vorher']['sha256'] != d['nachher']['sha256'] or d['vorher']['bytes'] != d['nachher']['bytes']}
assert not byteaenderungen, byteaenderungen
assert sha(ROOT / 'privat.db') == sha(ROOT / 'privat-sicherung.db')

runs = []
for p in sorted((ROOT / 'ausgaben').glob('*.json')):
    d = json.loads(p.read_text())
    if not isinstance(d,dict) or 'label' not in d:
        continue
    assert len(d['kammer']) == d['kammerlaeufe']
    assert not d['bezahlte_versuche']
    xml = ET.parse(p.with_suffix('.xml'))
    cases = []
    for tc in xml.iter('testcase'):
        status = next((s for s in ('failure','error','skipped') if tc.find(s) is not None), 'passed')
        cases.append({'klasse':tc.get('classname'), 'test':tc.get('name'), 'status':status})
    runs.append({k:d[k] for k in ('label','rc','argv','cwd','dauer_s','kammerlaeufe','kosten_eur','quell_sha256')} | {
        'tests':cases, 'junit':p.with_suffix('.xml').name, 'stdout':p.stem+'.stdout.txt', 'stderr':p.stem+'.stderr.txt',
        'zeugenlaeufe':sum(c['befehl'][1:2] == ['_messgeraet/lauf.py'] for c in d['kammer']),
        'uebrige_kammerlaeufe':sum(c['befehl'][1:2] != ['_messgeraet/lauf.py'] for c in d['kammer'])})
allcalls = [c['container'] for p in sorted((ROOT/'ausgaben').glob('*.json'))
            for d in [json.loads(p.read_text())] if isinstance(d,dict) and 'label' in d for c in d['kammer']]
assert len(allcalls) == len(set(allcalls))
assert sum(r['kammerlaeufe'] for r in runs) == len(allcalls)

batterie = json.loads((ROOT/'ausgaben/08-vierpaare-bestand.json').read_text())
paare = []
for n in ('nebenwirkung','regression','norm','vertrag'):
    for gruppe, erwartet in [('proben',True),('gegenproben',False)]:
        e = batterie[gruppe][n]
        assert e['ausgefuehrt'] is True and e['pruefbar'] is True and e['bestanden'] is erwartet
        assert e['kammerlaeufe'] == len(e['kammer'])
        paare.append({'probe':n,'gruppe':gruppe, 'pruefbar':e['pruefbar'],'bestanden':e['bestanden'],
                      'kammerlaeufe':len(e['kammer']), 'zeugenlaeufe':sum(c['befehl'][1:2]==['_messgeraet/lauf.py'] for c in e['kammer']),
                      'grund':e['grund']})
assert sum(e['kammerlaeufe'] for e in paare) == batterie['kosten']['kammerlaeufe']
assert batterie['abnahme']['werk_sha256_vor'] == batterie['abnahme']['werk_sha256_nach']
assert batterie['abnahme']['db_sha256_vor'] == batterie['abnahme']['db_sha256_nach']

vertragszeugen = []
for gruppe in ('proben','gegenproben'):
    e = batterie[gruppe]['vertrag']
    b=e['belege']
    ziel=f"{Path(b['vertragspfad']).parent.as_posix()}/{b['vertragstest']}"
    vertragszeugen.append({'gruppe':gruppe, 'vertragstest':ziel, 'vertrag':b['kandidat_tests'][ziel],
        'verbrauchertest':b['verbrauchertest'], 'verbraucher':b['kandidat_tests'][b['verbrauchertest']],
        'basis_verbraucher':b['basis_tests'][b['verbrauchertest']], 'aegis_verletzt':b['urteil']['vertrag_verletzt'],
        'pruefbar':e['pruefbar'], 'bestanden':e['bestanden'], 'grund':e['grund']})

bericht = {'dateien_geaendert':changed, 'source_sha256':{p:sha(ROOT/'repo'/p) for p in CHANGED},
           'versuche':runs, 'kammerlaeufe_alle_versuche':len(allcalls),
           'bezahlte_biotop_aufrufe':0, 'kosten_eur':0,
           'batterie':{'quelle':'ausgaben/08-vierpaare-bestand.json','gegenstand':batterie['gegenstand'],
                       'paare':paare, 'kosten':batterie['kosten'], 'vertragszeugen':vertragszeugen},
           'quellschutz':{'dateien':len(vor), 'bytes_unveraendert':not byteaenderungen,
                         'metadaten_unveraendert':not bewegung, 'aenderungen':bewegung,
                         'private_db_sha256':sha(ROOT/'privat.db'), 'db_sicherung_sha256':sha(ROOT/'privat-sicherung.db')},
           'stderr_nichtleer':[p.name for p in (ROOT/'ausgaben').glob('*.stderr.txt') if p.stat().st_size]}
(OUT/'BELEGE.json').write_text(json.dumps(bericht,ensure_ascii=False,indent=2))
with (OUT/'KOSTEN.csv').open('w') as f:
    w=csv.writer(f)
    w.writerow(['versuch','rc','pytest_faelle','kammerlaeufe','junit_zeugenlaeufe','uebrige_kammerlaeufe','bezahlte_biotop_aufrufe','eur'])
    for r in runs:
        w.writerow([r['label'],r['rc'],len(r['tests']),r['kammerlaeufe'],r['zeugenlaeufe'],r['uebrige_kammerlaeufe'],0,0])
    w.writerow(['SUMME_ALLE_VERSUCHE','',sum(len(r['tests']) for r in runs),len(allcalls),sum(r['zeugenlaeufe'] for r in runs),sum(r['uebrige_kammerlaeufe'] for r in runs),0,0])
    w.writerow(['TEILMENGE_BATTERIE_BESTAND_08','',8,sum(e['kammerlaeufe'] for e in paare),sum(e['zeugenlaeufe'] for e in paare),sum(e['kammerlaeufe']-e['zeugenlaeufe'] for e in paare),0,0])
for name in ('ausgaben','werkzeuge','guard'):
    shutil.copytree(ROOT/name,OUT/name,dirs_exist_ok=True)
print(json.dumps({'runs':[(r['label'],len(r['tests']),r['rc'],r['kammerlaeufe']) for r in runs],
                  'gesamt':len(allcalls),'batterie':bericht['batterie'],'quellschutz':bericht['quellschutz'],
                  'stderr':bericht['stderr_nichtleer']},ensure_ascii=False,indent=2))
