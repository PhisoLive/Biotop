"""Seal review artifacts; do not touch the inspected repository."""
from pathlib import Path
import hashlib,json,shutil,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'eingang'; INPUT.mkdir(exist_ok=True)
SCOPE=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/auftragseingrenzung-01')
for p in [ROOT.parent/'AENDERUNGEN.diff',ROOT.parent/'STATIK.json',*(SCOPE/name for name in ['AUFTRAGGEBER-WORTLAUT.txt','AUFTRAGSGRENZE.md','PHASE-4-LUECKEN.md'])]:
    shutil.copyfile(p,INPUT/p.name)
review=json.loads((ROOT/'REVIEW.json').read_text())
assert review['passed'] is False and len(review['logic_errors'])==1 and not review['security_concerns']
assert len(review['deferred_findings'])==4
assert json.loads((ROOT/'quellzustand-vergleich.json').read_text())['unchanged'] is True
repro=json.loads((ROOT/'repro-skip-2/result.json').read_text())
assert repro['raw_target_skipped'] is True and repro['accepted_as_valid_countercase'] is True
assert repro['original_einzelprobe_unit_row']['pruefbar'] is True
assert repro['consumer_unit_replay']['battery_complete'] is True
missing=[]
def check_refs(x):
    if isinstance(x,dict):
        for k,v in x.items():
            if k=='file' and isinstance(v,str) and v.startswith('/') and not Path(v).is_file(): missing.append(v)
            check_refs(v)
    elif isinstance(x,list):
        for v in x: check_refs(v)
check_refs(review)
assert not missing,missing
counts={}
for name in ['core-unit.xml','gen0-route.xml','sensitivity-kern-belohnt-gruen.xml','sensitivity-pareto-ohne-einzeltest.xml']:
    cases=list(ET.parse(ROOT/name).getroot().iter('testcase'))
    counts[name]=dict(tests=len(cases),failures=sum(x.find('failure') is not None for x in cases),errors=sum(x.find('error') is not None for x in cases),skipped=sum(x.find('skipped') is not None for x in cases))
assert counts['core-unit.xml']==dict(tests=37,failures=0,errors=0,skipped=0)
assert counts['gen0-route.xml']==dict(tests=2,failures=0,errors=0,skipped=0)
assert counts['sensitivity-kern-belohnt-gruen.xml']['failures']==3
assert counts['sensitivity-pareto-ohne-einzeltest.xml']['failures']==1
validation=dict(review_schema_valid=True,fail_closed_consistent=True,logic_errors=1,deferred_findings=4,source_snapshot_unchanged=True,
               named_evidence_files_exist=True,own_pytest_counts=counts,ordinary_own_tests_passed=sum(counts[n]['tests'] for n in ('core-unit.xml','gen0-route.xml')),
               repro_expected_assertion_failure_verified=True,scope_excluded_from_manifest=['arbeitskopie/','tmp/'],
               manifest_does_not_hash_itself_or_its_checksum=True)
(ROOT/'ABSCHLUSSPRUEFUNG.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
ignored={'arbeitskopie','tmp'}
files=sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(s in ignored for s in p.relative_to(ROOT).parts) and p.name not in {'SHA256SUMS','MANIFEST.sha256','DATEIEN.txt'})
index=sorted([str(p.relative_to(ROOT)) for p in files]+['DATEIEN.txt','SHA256SUMS','MANIFEST.sha256'])
(ROOT/'DATEIEN.txt').write_text('\n'.join(index)+'\n')
files.append(ROOT/'DATEIEN.txt'); files.sort()
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(ROOT))+'\n' for p in files)
(ROOT/'SHA256SUMS').write_text(manifest)
hash_=hashlib.sha256((ROOT/'SHA256SUMS').read_bytes()).hexdigest()
(ROOT/'MANIFEST.sha256').write_text(hash_+'  SHA256SUMS\n')
# Verify every entry, including the local JUnit and the copied parent originals.
for line in manifest.splitlines():
    h,p=line.split('  ',1)
    assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
print(json.dumps(dict(passed=False,artifact_dir=str(ROOT),manifest_entries=len(files),index_entries=len(index),manifest_sha256=hash_,all_manifest_hashes_verified=True,counts=counts),ensure_ascii=False,indent=2))
