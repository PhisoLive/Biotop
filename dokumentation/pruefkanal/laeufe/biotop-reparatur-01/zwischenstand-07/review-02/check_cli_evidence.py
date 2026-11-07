"""Added parent CLI evidence: read-only reconciliation, no live DB access."""
from pathlib import Path
import hashlib,json,re,shutil,xml.etree.ElementTree as ET
from biotop.organe import eichproben, vorspann
ROOT=Path(__file__).resolve().parent
SRC=ROOT.parent/'repo'
IN=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
OUT=ROOT/'elternbelege'
for name in ['49-vorspann-kernabschluss.json','49-vorspann-kernabschluss.stdout.txt','49-vorspann-kernabschluss.stderr.txt','49-vorspann-kernabschluss-kammer.json','50-vorspann-cli-sperre.json']:
    shutil.copyfile(IN/name,OUT/name)
a=json.loads((OUT/'49-vorspann-kernabschluss.json').read_text())
raw=json.loads((OUT/'49-vorspann-kernabschluss-kammer.json').read_text())
proof=json.loads(a['nachweis']['ergebnis'])
stdout=json.loads((OUT/'49-vorspann-kernabschluss.stdout.txt').read_text())
digest=vorspann._sha(proof)
assert digest==a['nachweis']['nachweis_sha256']==stdout.pop('nachweis_sha256')
assert stdout==proof
assert a['nachweis']['status']=='bestanden' and a['rc']==0
assert (OUT/'49-vorspann-kernabschluss.stderr.txt').read_text()==''
assert a['gen0_nachweis_verwendbar'] is True
assert a['nachweis']['mass_sha256'] is None
source=[]
for p,h in proof['quellen']['instrument']['dateien'].items():
    actual=hashlib.sha256((SRC/p).read_bytes()).hexdigest()
    assert actual==h,(p,actual,h)
    source.append(p)
by_id={r['container']:r for r in raw}
assert len(raw)==len(by_id)==a['kammerlaeufe']==proof['kosten']['kammerlaeufe']
assert sum(x['kammerlaeufe'] for x in a['eichkosten'])==len(raw)
assert a['neue_modellbuchungen']==[]
assert vorspann._qualitaet(proof['eichproben'])==proof['qualitaet']
assert vorspann._rauschwerte(proof['rauschen'],proof['quellen']['bereiche'])
pairs=[]
for group,expected in [('proben',True),('gegenproben',False)]:
    for name,row in proof['eichproben'][group].items():
        assert row['ausgefuehrt'] is row['pruefbar'] is True
        assert row['bestanden'] is expected
        assert eichproben._bestanden(name,row['belege']) is expected
        assert len(row['kammer'])==row['kammerlaeufe']
        assert all(by_id[r['container']]==r for r in row['kammer'])
        info=dict(group=group,name=name,valid=row['pruefbar'],predicate=row['bestanden'],chambers=row['kammerlaeufe'])
        if name=='vertrag':
            b=row['belege']; target=str(Path(b['vertragspfad']).parent)+'/'+b['vertragstest']
            assert eichproben._vertrag_pruefbar(b,not expected)
            witnesses=[]
            for r in row['kammer']:
                match=re.search(r'@@J@@(.*)@@E@@',r['stdout'],re.S)
                if match:
                    for tc in ET.fromstring(match.group(1)).iter('testcase'):
                        node=(tc.get('classname') or '').replace('.','/')+'.py::'+tc.get('name')
                        if node==target:
                            witnesses.append(dict(container=r['container'],nodeid=node,skipped=tc.find('skipped') is not None,
                                                  failure=tc.find('failure') is not None,error=tc.find('error') is not None))
            assert len(witnesses)==1 and not witnesses[0]['skipped'] and not witnesses[0]['error']
            assert witnesses[0]['failure'] is expected
            info['named_contract']=witnesses
        pairs.append(info)
b=json.loads((OUT/'50-vorspann-cli-sperre.json').read_text())
for row in b['faelle']:
    for suffix in ('.stdout.txt','.stderr.txt','-kammer.json'):
        name='50-vorspann-cli-sperre-'+row['phase']+suffix
        shutil.copyfile(IN/name,OUT/name)
    assert (OUT/('50-vorspann-cli-sperre-'+row['phase']+'.stderr.txt')).read_text()==row['stderr']
    assert json.loads((OUT/('50-vorspann-cli-sperre-'+row['phase']+'-kammer.json')).read_text())==[]
assert b['gesperrt']==b['von']==len(b['faelle'])==3
assert all(x['rc']==1 and x['kammerlaeufe']==0 and 'Nachweis fehlt oder unbrauchbar' in x['stderr'] for x in b['faelle'])
assert b['neue_modellbuchungen']==0 and b['lauf_nachher']['mass'] is None
result=dict(boundary='Supplied parent CLI records reconciled; reviewer did not execute Docker/CLI against a real Werk or access the database',
 real_vorspann_rc=a['rc'],proof_hash=digest,proof_stdout_database_record_equal=True,source_hash_count=len(source),source_files=source,
 recorded_gen0_proof_usable=a['gen0_nachweis_verwendbar'],real_gen0_not_executed=True,mass_not_frozen=True,
 chamber_count=len(raw),costs=proof['kosten'],pairs=pairs,model_charges=a['neue_modellbuchungen'],
 real_missing_proof_refusals=b['faelle'],productive_state_unchanged='Parent-reported protection flags only; no live DB/production access by reviewer')
(ROOT/'cli-belegabgleich.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('costs','pairs','source_files')},ensure_ascii=False,indent=2))
