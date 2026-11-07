#!/usr/bin/env python3
"""Abschluss des lokalen Teilpakets, ohne Produkt- oder DB-Schreibzugriff."""
import hashlib,json,pathlib,re,subprocess,urllib.parse,datetime
O=pathlib.Path(__file__).resolve().parent
r=subprocess.run(['python3','-B',str(O/'lieferung_pruefen.py')],capture_output=True,text=True)
(O/'lieferpruefung.log').write_text(r.stdout+r.stderr)
if r.returncode:raise SystemExit(r.returncode)
S='/root/.hermes/skills/research/grounded-citations/scripts/sources.py'
r=subprocess.run(['python3','-B',S,'--ledger',str(O/'quellenledger.json'),'verify',str(O/'STATUS-24-25.md'),'--evidence','--min-coverage','0.5'],capture_output=True,text=True)
(O/'ZITATPRUEFUNG.txt').write_text(r.stdout+r.stderr+f'\nexit_code={r.returncode}\n')
if r.returncode:raise SystemExit(r.returncode)
print(r.stdout.strip())
body=(O/'STATUS-24-25.md').read_text().split('## Sources')[0]
cited={int(x) for x in re.findall(r'\[(\d+)\]',body)}
ledger=json.loads((O/'quellenledger.json').read_text())
sources=[]
for s in ledger['sources']:
 if s['id'] not in cited:continue
 p=pathlib.Path(urllib.parse.unquote(urllib.parse.urlparse(s['url']).path));data=p.read_bytes()
 sources.append({'id':s['id'],'datei':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(O/'quellen-integritaet-final.json').write_text(json.dumps({'zeit_utc':datetime.datetime.now(datetime.UTC).isoformat(),'hinweis':'Endstand der zitierten Quellen. quellen-integritaet.json dokumentiert die frühere Arbeitsaufnahme vor internen Exportkorrekturen.','quellen':sources},ensure_ascii=False,indent=2)+'\n')
excluded={'DATEIEN.txt','PRUEFSUMMEN.sha256','PRUEFSUMME-ORDNER.txt'}
payload=sorted(p for p in O.rglob('*') if p.is_file() and str(p.relative_to(O)) not in excluded)
for p in payload:
 if p.suffix=='.json':json.loads(p.read_text())
names=sorted([str(p.relative_to(O)) for p in payload]+list(excluded))
(O/'DATEIEN.txt').write_text('\n'.join(names)+'\n')
sealed=sorted(payload+[O/'DATEIEN.txt'])
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(O))+'\n' for p in sealed)
(O/'PRUEFSUMMEN.sha256').write_text(manifest)
mhash=hashlib.sha256((O/'PRUEFSUMMEN.sha256').read_bytes()).hexdigest()
(O/'PRUEFSUMME-ORDNER.txt').write_text(f'SHA-256 von PRUEFSUMMEN.sha256: {mhash}\nVersiegelte Dateien: {len(sealed)}\nDateien im Lieferordner einschließlich Hashmanifest und dieser Hülle: {len(names)}\nDas Hashmanifest und diese Hülle sind wegen Selbstreferenz nicht in ihrem eigenen Manifest enthalten.\n')
verified=0
for line in (O/'PRUEFSUMMEN.sha256').read_text().splitlines():
 h,name=line.split('  ',1)
 assert hashlib.sha256((O/name).read_bytes()).hexdigest()==h
 verified+=1
actual=sorted(str(p.relative_to(O)) for p in O.rglob('*') if p.is_file())
assert actual==names
v=json.loads((O/'VERIFIKATION.json').read_text())
print(json.dumps({'bericht':str(O/'STATUS-24-25.md'),'bericht_sha256':hashlib.sha256((O/'STATUS-24-25.md').read_bytes()).hexdigest(),'status_json':str(O/'STATUS-24-25.json'),'status_json_sha256':hashlib.sha256((O/'STATUS-24-25.json').read_bytes()).hexdigest(),'manifest_sha256':mhash,'dateien_insgesamt':len(names),'manifestdateien_nachgerechnet':verified,'chronologie_ereignisse':len(json.loads((O/'chronologie.json').read_text())),'laeufe':2,'bauteile':['A','B','C'],'integritaetspruefungen':len(v['checks']),'integritaet_ok':v['alle_pruefungen_ok'],'sql_abfragen':v['sql_abfragen'],'db_sha256':v['snapshot_db_sha256'],'arbeitsbaum_drift_vorgefunden':not v['arbeitsbaum_unveraendert']},ensure_ascii=False,indent=2))
