"""Reconcile named parent evidence against this exact read-only snapshot."""
from pathlib import Path
import hashlib, json, re, shutil, xml.etree.ElementTree as ET
from biotop.organe import eichproben, vorspann
ROOT=Path(__file__).resolve().parent
SRC=ROOT.parent/'repo'
IN=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
OUT=ROOT/'elternbelege'; OUT.mkdir(exist_ok=True)
for suffix in ('.json','.xml','.txt','-eichpaare.json','-kammer.json'):
    name='48-gesamtsuite-kernabschluss'+suffix
    shutil.copyfile(IN/name,OUT/name)
suite=json.loads((OUT/'48-gesamtsuite-kernabschluss.json').read_text())
pairs=json.loads((OUT/'48-gesamtsuite-kernabschluss-eichpaare.json').read_text())
raw=json.loads((OUT/'48-gesamtsuite-kernabschluss-kammer.json').read_text())
tree=ET.parse(OUT/'48-gesamtsuite-kernabschluss.xml').getroot()
cases=list(tree.iter('testcase'))
counts=dict(tests=len(cases),failures=sum(c.find('failure') is not None for c in cases),errors=sum(c.find('error') is not None for c in cases),skipped=sum(c.find('skipped') is not None for c in cases))
assert all(counts[k]==int(suite['testsuites'][0][k]) for k in counts)
source_checks=[dict(path=p,expected=h,actual=hashlib.sha256((SRC/p).read_bytes()).hexdigest()) for p,h in suite['quellen_sha256'].items()]
assert all(c['expected']==c['actual'] for c in source_checks)
by_container={r['container']:r for r in raw}
assert len(raw)==len(by_container)==suite['kammerlaeufe']==suite['verschiedene_container']
summary=[]
for group,expected in [('proben',True),('gegenproben',False)]:
    assert set(pairs[group])==set(eichproben.PROBEN)
    for name,row in pairs[group].items():
        assert row['ausgefuehrt'] is True and row['pruefbar'] is True
        assert row['bestanden'] is expected
        assert eichproben._bestanden(name,row['belege']) is expected
        assert len(row['kammer'])==row['kammerlaeufe']
        assert all(by_container[r['container']]==r for r in row['kammer'])
        assert all(r['zeitlimit'] is False for r in row['kammer'])
        d=dict(group=group,name=name,expected_predicate=expected,recalculated_predicate=eichproben._bestanden(name,row['belege']),
               pruefbar=row['pruefbar'],kammerlaeufe=row['kammerlaeufe'],modellaufrufe=row['modellaufrufe'],kosten_eur=row['kosten_eur'],
               mass=row['belege']['urteil']['mass'],reason=row['grund'],
               containers=[r['container'] for r in row['kammer']])
        junit=[]
        for r in row['kammer']:
            match=re.search(r'@@J@@(.*)@@E@@',r['stdout'],re.S)
            if not match: continue
            t=ET.fromstring(match.group(1)); xs=list(t.iter('testcase'))
            junit.append(dict(container=r['container'],tests=len(xs),skipped=sum(x.find('skipped') is not None for x in xs),
                errors=sum(x.find('error') is not None for x in xs),failures=sum(x.find('failure') is not None for x in xs)))
        d['raw_junit_runs']=junit
        if name=='vertrag':
            b=row['belege']; target=str(Path(b['vertragspfad']).parent)+'/'+b['vertragstest']
            d.update(named_contract=target,consumer=b['verbrauchertest'],named_validity=eichproben._vertrag_pruefbar(b,not expected),
                     candidate_contract=b['kandidat_tests'][target],candidate_consumer=b['kandidat_tests'][b['verbrauchertest']])
            assert d['named_validity'] is True
            # Match the candidate witnesses by stable container ID, not sequence.
            witnesses=[]
            for rr in row['kammer']:
                m=re.search(r'@@J@@(.*)@@E@@',rr['stdout'],re.S)
                if m:
                    for tc in ET.fromstring(m.group(1)).iter('testcase'):
                        n=(tc.get('classname') or '').replace('.','/')+'.py::'+tc.get('name')
                        if n==target:
                            witnesses.append(dict(container=rr['container'],nodeid=n,xml=ET.tostring(tc,encoding='unicode'),
                                skipped=tc.find('skipped') is not None,failure=tc.find('failure') is not None,error=tc.find('error') is not None))
            assert len(witnesses)==1 and not witnesses[0]['skipped']
            assert witnesses[0]['failure'] is expected and witnesses[0]['error'] is False
            d['raw_named_witnesses']=witnesses
        summary.append(d)
sums={k:sum(r[k] for g in ('proben','gegenproben') for r in pairs[g].values()) for k in ('kammerlaeufe','modellaufrufe','kosten_eur','dauer_s')}
assert sums==pairs['kosten'],(sums,pairs['kosten'])
assert pairs['abnahme']['werk_sha256_vor']==pairs['abnahme']['werk_sha256_nach']
assert pairs['abnahme']['db_sha256_vor']==pairs['abnahme']['db_sha256_nach']
core_indices=[i for i,c in enumerate(cases) if c.get('classname')=='tests.test_kernmass_pareto']
others=[i for i,c in enumerate(cases) if c.get('classname')!='tests.test_kernmass_pareto']
assert max(core_indices)<min(others)
result=dict(boundary='Recalculation of provided parent evidence; no new Kammer campaign; no implementer testimony',
 suite_counts=counts,raw_chambers=len(raw),unique_containers=len(by_container),source_checks=source_checks,
 core_test_count=len(core_indices),core_priority_verified=True,core_test_ids=[cases[i].get('name') for i in core_indices],
 pair_count=len(summary),pair_sums=sums,pairs=summary,quality=vorspann._qualitaet(pairs),
 werk_and_database_isolation_in_supplied_evidence=True)
(ROOT/'belegabgleich.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('source_checks','pairs')},ensure_ascii=False,indent=2))
