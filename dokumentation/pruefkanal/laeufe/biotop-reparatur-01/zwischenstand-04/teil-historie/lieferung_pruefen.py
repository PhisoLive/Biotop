#!/usr/bin/env python3
"""Verifiziert Lieferdaten/SELECTs, NICHT Biotop-Verhalten oder Tests.
Kein Import aus dem Produkt. Schreibziele nur im Lieferordner.
"""
import collections,datetime,hashlib,json,pathlib,sqlite3,subprocess
from decimal import Decimal
O=pathlib.Path(__file__).resolve().parent
R=pathlib.Path('/root/biotop');DB=pathlib.Path('/root/reparatur-01/ausgang.db')
def read(n):return json.loads((O/n).read_text())
def save(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def snap(p):
 s=p.stat();return {'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':s.st_size,'mtime_ns':s.st_mtime_ns}
def git(*args):return subprocess.run(['git','--no-optional-locks','-C',str(R),*args],capture_output=True,text=True,check=True).stdout
c=sqlite3.connect(DB.as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('PRAGMA query_only=ON')
before=read('zustand-vorher.json')
started=datetime.datetime.now(datetime.UTC).isoformat()
now={'zeit_utc':started,'db':snap(DB),'git_head':git('rev-parse','HEAD').strip(),'git_status':git('status','--porcelain=v1'),'tracked_files':{f:snap(R/f) for f in before['tracked_files'] if (R/f).is_file()},'counters':{t:dict(c.execute(f'SELECT count(*) anzahl,max({pk}) letzte_id FROM {t}').fetchone()) for t,pk in [('laeufe','id'),('kasse','id'),('protokoll','nr'),('generationen','id')]}}
save('zustand-nachher.json',now)
delta=[{'pfad':f,'vorher':old,'nachher':now['tracked_files'].get(f)} for f,old in before['tracked_files'].items() if old!=now['tracked_files'].get(f)]
# Exec nur SELECT; Autorisierung blockiert dennoch jeden SQL-Schreibversuch.
allowed={sqlite3.SQLITE_SELECT,sqlite3.SQLITE_READ,sqlite3.SQLITE_FUNCTION,sqlite3.SQLITE_RECURSIVE}
c.set_authorizer(lambda action,*args:sqlite3.SQLITE_OK if action in allowed else sqlite3.SQLITE_DENY)
raw='\n'.join(line for line in (O/'status-abfragen.sql').read_text().splitlines() if not line.lstrip().startswith('--'))
statements=[s.strip() for s in raw.split(';') if s.strip()]
sqlresults=[]
for i,statement in enumerate(statements,1):
 assert statement.upper().startswith('SELECT')
 rows=[dict(row) for row in c.execute(statement)]
 sqlresults.append({'abfrage':i,'sql':statement,'zeilen':len(rows),'ergebnisse':rows})
save('SQL-resultate.json',sqlresults)
status=read('STATUS-24-25.json')
checks=[]
def check(name,condition,detail=None):
 checks.append({'pruefung':name,'ok':bool(condition),'detail':detail})
check('Gefrorene DB in Inhalt, Größe, mtime unverändert',before['db']==now['db'])
check('Snapshot-Zähler unverändert',before['counters']==now['counters'])
check('HEAD fixiert',now['git_head']==status['umfang']['quellstand'])
check('Zwei Statusläufe exakt 24 und 25',[r['lauf_id'] for r in status['laeufe']]==[24,25])
for run in status['laeufe']:
 lid=run['lauf_id']; generations=run['generationen']; costs=run['kosten']; A=run['A']; mdl=run['modellaufrufe']
 check(f'Lauf {lid} DB bereit/ohne Ende',run['db_status']=='bereit' and run['beendet_am'] is None)
 check(f'Lauf {lid} genau Gen0 und Gen1-4',[g['nummer'] for g in generations]==[0,1,2,3,4])
 check(f'Lauf {lid} A-Aufrechnung',A['gesamt']==A['ausgefuehrt']+A['gesperrt']+A['ohne_behauptung'])
 check(f'Lauf {lid} Kassen-/Aufrufreferenzen',costs['anzahl']==mdl['versuche']==mdl['antworten']==mdl['antworten_mit_echter_aufruf_id'] and not mdl['unbeantwortet'] and not mdl['fremde_antwortreferenzen'])
 check(f'Lauf {lid} Geldgrenze',Decimal(costs['summe_eur_decimal'])<Decimal(costs['budget_eur']),{'prozent_auf_1_nachkommastelle':str(Decimal(costs['anteil_prozent']).quantize(Decimal('.1')))})
 check(f'Lauf {lid} keine Eichung/Eichprobe im Laufnachweis',not run['eichereignisse'] and run['eichung_tabellenzahl']==run['eichkosten_tabellenzahl']==0)
check('A: 50 Entscheidungen/26 echte Schlüssel-Sperrungen',sum(r['A']['gesamt'] for r in status['laeufe'])==50 and sum(r['A']['gesperrt'] for r in status['laeufe'])==26)
check('C: fünf Aufrufe, neun Testdurchläufe, fünf Sperren',tuple(status['laeufe'][1]['gestellte_C_proben'][key] for key in ('C_pruefungen_anzahl','C_testdurchlaeufe','C_sperrungen_anzahl'))==(5,9,5))
check('C: zwei Schlüsselfälle, drei Stellenkombinationen',len(status['laeufe'][1]['gestellte_C_proben']['verschiedene_schluesselfaelle'])==2 and len(status['laeufe'][1]['gestellte_C_proben']['verschiedene_stelle_schluessel_kombinationen'])==3)
check('C: sechs historische Urteile, alle abgelehnt',len(status['laeufe'][1]['gestellte_C_proben']['verdict_ereignisse'])==6 and all(e['inhalt']['status']=='abgelehnt' for e in status['laeufe'][1]['gestellte_C_proben']['verdict_ereignisse']))
check('Probe K2680 im Snapshot nicht mehr gespeichert',c.execute('SELECT COUNT(*) FROM kandidaten WHERE id=2680').fetchone()[0]==0)
check('Fünfzehn err-Dateien, eine mit Inhalt',len(read('runner-stderr.json'))==15 and sum(bool(r['bytes']) for r in read('runner-stderr.json'))==1)
cas=read('kasse.json')
sum24=sum((Decimal(str(r['kosten_eur'])) for r in cas if r['lauf_id'] in (24,25)),Decimal(0))
allcost=sum((Decimal(str(r['kosten_eur'])) for r in cas),Decimal(0))
check('Kasse 24+25 Rohsumme',str(sum24)=='0.78680667592592585586')
check('Kasse 22-25 Rohsumme',str(allcost)=='1.69702926851851837427' and len(cas)==848)
source_files=[]
for cp in sorted((O/'quellen').rglob('*.py')):
 relative=cp.relative_to(O/'quellen');ref=relative.parts[0];source='/'.join(relative.parts[1:])
 data=subprocess.run(['git','--no-optional-locks','-C',str(R),'show',ref+':'+source],check=True,capture_output=True).stdout
 okay=cp.read_bytes()==data
 source_files.append({'datei':str(relative),'identisch_zu_git_blob':okay,'sha256':hashlib.sha256(data).hexdigest()})
check('Alle mitgelieferten Originalquellen bytegleich mit Git-Blobs',all(x['identisch_zu_git_blob'] for x in source_files),source_files)
# Zahlen des Berichts sind Quellenzählungen; dies ist keine dynamische Produktprüfung.
jsonfiles=sorted(f for f in O.rglob('*.json') if f.name not in ('VERIFIKATION.json',))
for f in jsonfiles: json.loads(f.read_text())
check('Alle Liefer-JSON-Dateien lesbar',True,{'dateien':len(jsonfiles)})
# Nur Formatindikatoren prüfen; niemals potentielle Secret-Werte in den Bericht ausgeben.
import re
secret_patterns={'private_key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----','openrouter_secret':r'sk-or-v1-[A-Za-z0-9]{20,}','bearer_value':r'(?i)authorization\s*[:=]\s*[\"\x27]?bearer\s+[a-z0-9._-]{20,}'}
secret_hits=[]
for f in O.rglob('*'):
 if not f.is_file() or f.name=='lieferung_pruefen.py':continue
 try:text=f.read_text()
 except UnicodeError:continue
 for name,pattern in secret_patterns.items():
  if re.search(pattern,text):secret_hits.append({'datei':str(f.relative_to(O)),'indikator':name})
check('Keine Secret-Format-Treffer im Teilpaket',not secret_hits,secret_hits)
report={'beginn_utc':started,'ende_utc':datetime.datetime.now(datetime.UTC).isoformat(),'art':'Prüfung von Lieferartefakten/SQL/Quellidentität, keine Biotop-Funktionstests','checks':checks,'alle_pruefungen_ok':all(x['ok'] for x in checks),'produktdaten_geaendert_durch_dieses_script':False,'arbeitsbaum_unveraendert':not delta and not now['git_status'],'arbeitsbaum_drift':delta,'arbeitsbaum_status_nachher':now['git_status'],'drift_einordnung':'Extern während paralleler Arbeit vorgefundene Änderungen. Dieses Teilpaket bewertet ausschließlich Git-Blobs am fixierten HEAD und die gefrorene DB. Keine Rücksetzung oder Beurteilung dieser neuen Reparaturen.','interner_zaehlversuch':'Ein erster Ad-hoc-Kandidatenabgleich scheiterte an unhashable dict (Generationslisten enthalten Objekte). Korrigiert durch Zugriff auf kandidat-Feld; keine Produkt-/Probeausführung.', 'sql_abfragen':len(statements),'sql_zeilen':[r['zeilen'] for r in sqlresults],'snapshot_db_sha256':now['db']['sha256']}
save('VERIFIKATION.json',report)
print(json.dumps({'alle_pruefungen_ok':report['alle_pruefungen_ok'],'pruefungen':len(checks),'sql_abfragen':len(statements),'arbeitsbaum_unveraendert':report['arbeitsbaum_unveraendert'],'veraenderte_vorher_erfasste_dateien':[r['pfad'] for r in delta],'git_status':now['git_status'],'snapshot_unveraendert':before['db']==now['db'],'originalquellen':source_files},ensure_ascii=False,indent=2))
if not report['alle_pruefungen_ok']:raise SystemExit(1)
