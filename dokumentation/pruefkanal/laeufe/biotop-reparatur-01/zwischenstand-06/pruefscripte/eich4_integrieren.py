"""Nur EICH-4 integrieren; Phase-4-Teilkopien nicht übernehmen."""
from pathlib import Path
import hashlib,json,sys,subprocess,tarfile,csv,datetime
P=Path('/root/reparatur-01');R=Path('/root/biotop');D=P/'nachbesserung-01/vertrag/lieferung'
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
phase=sys.argv[1];assert phase in ('tests','produkt')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
man=json.loads((D/'DATEIEN.json').read_text());pruef=[]
for e in man['dateien']:
 p=D/e['relativ'];assert p.resolve().is_relative_to(D.resolve())
 pruef.append({'datei':e['relativ'],'gleich':sha(p)==e['sha256'] and p.stat().st_size==e['bytes']})
assert len(pruef)==man['bestandteile_ohne_manifest_und_summen'] and all(x['gleich'] for x in pruef)
archiv=P/'nachbesserung-01/vertrag/EICH-4-fixpaket.tar.gz'
assert sha(archiv)=='47fa5f5bef621dcc3d85e54ee551492ae0c333d70367816f40c2fa2efacf6501'
with tarfile.open(archiv) as t:
 members=[m for m in t.getmembers() if m.isfile()]
 for m in members:
  rel=Path(m.name);assert not rel.is_absolute() and '..' not in rel.parts
  parts=rel.parts[1:] if rel.parts[0]=='lieferung' else rel.parts
  p=D.joinpath(*parts);assert p.is_file(),str(p)
  assert hashlib.sha256(t.extractfile(m).read()).hexdigest()==sha(p)
allowed=['biotop/organe/eichproben.py','tests/test_eichproben.py','tests/test_review_vertrag.py']
vorher={p:sha(R/p) if (R/p).exists() else None for p in allowed}
if phase=='tests':
 for p in allowed:
  base=D/'basis'/p
  if base.exists():assert vorher[p]==sha(base),p
  else:assert not (R/p).exists(),p
 include=['--include=tests/test_eichproben.py','--include=tests/test_review_vertrag.py']
else:
 assert vorher['biotop/organe/eichproben.py']==sha(D/'basis/biotop/organe/eichproben.py')
 for p in allowed[1:]:assert vorher[p]==sha(D/'dateien'/p)
 include=['--include=biotop/organe/eichproben.py']
cmd=['git','-C',str(R),'apply',*include,str(D/'AENDERUNGEN.diff')]
subprocess.run(cmd[:4]+['--check']+cmd[4:],check=True)
subprocess.run(cmd,check=True)
for p in allowed:
 if (phase=='tests' and p.startswith('tests/')) or phase=='produkt':assert sha(R/p)==sha(D/'dateien'/p),p
subprocess.run(['git','-C',str(R),'diff','--check'],check=True)
base=json.loads((P/'nachbesserung-01/ELTERN-AUSGANG.json').read_text())
ab=[p for p,x in base.items() if sha(R/p)!=x['sha256'] and p not in allowed]
assert not ab,ab
rows=list(csv.DictReader((D/'KOSTEN.csv').open()))
versuche=[r for r in rows if r['versuch'][0].isdigit()]
gesamt=next(r for r in rows if r['versuch']=='SUMME_ALLE_VERSUCHE')
for k in ['kammerlaeufe','junit_zeugenlaeufe','uebrige_kammerlaeufe','bezahlte_biotop_aufrufe']:
 assert sum(int(x[k]) for x in versuche)==int(gesamt[k])
bericht={'zeit':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':phase,'integration_nur':allowed,'vorher':vorher,'nachher':{p:sha(R/p) for p in allowed},'uebriger_elternstand_unveraendert':not ab,'liefermanifest_geprueft':len(pruef),'archivdateien_bytegleich':len(members),'csv_kosten_abgeglichen':True,'lieferung_kammergesamt':int(gesamt['kammerlaeufe'])}
name='46-eich4-tests-integriert.json' if phase=='tests' else '47-eich4-produkt-integriert.json'
ziel=O/name;assert not ziel.exists();ziel.write_text(json.dumps(bericht,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(bericht,ensure_ascii=False))
