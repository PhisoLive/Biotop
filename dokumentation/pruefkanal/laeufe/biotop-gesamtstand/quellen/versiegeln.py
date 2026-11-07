"""Versiegelt ausschließlich den beauftragten Prüfkanalordner und liest jedes Ziel per HTTPS zurück."""
from pathlib import Path
import hashlib,json,datetime,os,grp,re,urllib.request,urllib.parse,concurrent.futures
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand')
URL='https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/'
excluded={'PRUEFSUMMEN.sha256','PRUEFSUMME-ORDNER.txt','ABRUF-01.json'}
# Keine Voll-DB und keine Schlüsseldateien veröffentlichen; hochspezifischer Zusatzscan.
for p in O.rglob('*'):
 if p.is_file():assert not(p.suffix=='.db' or p.name.startswith('.env')),str(p)
patterns=[r'\bsk-(?:or-v1-|ant-)?[A-Za-z0-9_-]{24,}',r'\bAIza[0-9A-Za-z_-]{30,}',r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
hits=[]
for p in O.rglob('*'):
 if p.is_file() and p.suffix not in ['.gz','.zip']:
  text=p.read_text(errors='replace')
  for pattern in patterns:
   if re.search(pattern,text):hits.append(str(p.relative_to(O)))
assert not hits,{'geheimnisverdacht_dateien':hits}
# DATEIEN ist Teil des Inhaltsmanifests. Metadateien nennen wir vor ihrer Erzeugung.
names=sorted({str(p.relative_to(O)) for p in O.rglob('*') if p.is_file()}|excluded|{'DATEIEN.txt'})
(O/'DATEIEN.txt').write_text('Biotop-Gesamtstand — vollständiges Dateiverzeichnis\nAbholbasis: '+URL+'\nStart: '+URL+'BERICHT.md\n\nOrdnerprüfsumme = SHA-256 von PRUEFSUMMEN.sha256.\nPRUEFSUMMEN.sha256 versiegelt alle Nutzdateien einschließlich DATEIEN.txt.\nPRUEFSUMME-ORDNER.txt und ABRUF-01.json sind äußere Belege, nicht selbst im Inhaltsmanifest (keine Hash-Selbstreferenz).\n\n'+ '\n'.join(names)+'\n')
payload=sorted(p for p in O.rglob('*') if p.is_file() and str(p.relative_to(O)) not in excluded)
entries={str(p.relative_to(O)):hashlib.sha256(p.read_bytes()).hexdigest() for p in payload}
manifest=''.join(f'{digest}  {name}\n' for name,digest in entries.items())
(O/'PRUEFSUMMEN.sha256').write_text(manifest)
folder_hash=hashlib.sha256(manifest.encode()).hexdigest()
(O/'PRUEFSUMME-ORDNER.txt').write_text(f'{folder_hash}  PRUEFSUMMEN.sha256\n\nBedeutung: SHA-256 des sortierten Inhaltsmanifests; dessen Zeilen versiegeln {len(entries)} Nutzdateien.\nÄußere Belege: PRUEFSUMME-ORDNER.txt und ABRUF-01.json.\nAbholung: {URL}DATEIEN.txt\n')
gid=grp.getgrnam('caddy').gr_gid
for p in [O]+list(O.rglob('*')):
 os.chown(p,0,gid);os.chmod(p,0o750 if p.is_dir() else 0o640)
def fetch(item):
 name,digest=item;url=URL+urllib.parse.quote(name,safe='/')
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Biotop-Gesamtstand-HTTPS-Pruefung/1'})
  with urllib.request.urlopen(req,timeout=60) as r: data=r.read();status=r.status
  got=hashlib.sha256(data).hexdigest()
  return {'datei':name,'url':url,'http':status,'bytes':len(data),'soll_sha256':digest,'ist_sha256':got,'bytegleich':got==digest}
 except Exception as e:return {'datei':name,'url':url,'http':None,'bytegleich':False,'fehler':str(e)}
checks=dict(entries)
for name in ['PRUEFSUMMEN.sha256','PRUEFSUMME-ORDNER.txt']:checks[name]=hashlib.sha256((O/name).read_bytes()).hexdigest()
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(fetch,checks.items()))
ok=sum(r['bytegleich'] and r['http']==200 for r in results)
report={'zeit':datetime.datetime.now(datetime.timezone.utc).isoformat(),'abholbasis':URL,'ordner_sha256':folder_hash,'manifestdateien':len(entries),'mit_manifest_und_pruefsummentext_geprueft':len(results),'http200_und_bytegleich':ok,'fehler':[x for x in results if not(x['bytegleich'] and x['http']==200)],'abrufe':results,'geheimnisscan':'Keine Voll-DB/.env-Datei, kein Treffer hochspezifischer Schlüsselmuster; kein formaler Geheimnisfreiheitsbeweis.'}
p=O/'ABRUF-01.json';p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');os.chown(p,0,gid);os.chmod(p,0o640)
selfcheck=fetch(('ABRUF-01.json',hashlib.sha256(p.read_bytes()).hexdigest()))
print(json.dumps({'ordner_sha256':folder_hash,'manifest_dateien':len(entries),'geprueft':len(results),'http200_und_bytegleich':ok,'abrufbericht_selbst':selfcheck,'fehler':report['fehler'],'dateien_url':URL+'DATEIEN.txt','bericht_url':URL+'BERICHT.md'},ensure_ascii=False,indent=2))
assert ok==len(results) and selfcheck['bytegleich'] and selfcheck['http']==200, 'Auslieferung NICHT vollständig nachgewiesen'
