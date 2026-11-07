"""Reale CLI-Eingänge ohne Pflichtvorspann; keine Gen0-Freeze-Erfolgspolitik."""
from pathlib import Path
import os,sys,sqlite3,json,subprocess,hashlib,datetime
P=Path('/root/reparatur-01');W=P/'eltern-vorspann-sperre-01';W.mkdir(exist_ok=False)
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben');N='50-vorspann-cli-sperre'
assert not (O/(N+'.json')).exists()
D=P/'ausgang.db';vor=hashlib.sha256(D.read_bytes()).hexdigest()
c=sqlite3.connect(W/'privat.db',isolation_level=None);c.row_factory=sqlite3.Row
with sqlite3.connect(f'file:{D}?mode=ro&immutable=1',uri=True) as a:a.backup(c)
os.chmod(W/'privat.db',0o600)
lid=c.execute('SELECT max(id)+1 FROM laeufe').fetchone()[0]
c.execute("INSERT INTO laeufe(id,werk_id,status,budget_eur,mass,begonnen_am) VALUES(?,22,'kartiert',0,NULL,?)",(lid,datetime.datetime.now(datetime.timezone.utc).isoformat()))
# Selbst bei Regression im Gate soll keinerlei produktives Werk angefasst werden.
from sys import path;path.insert(0,'/root/biotop')
from biotop.organe import kammer
kammer._kopie(P/'teil-eichung/werk-lauf25-kopie',W/'werk')
c.execute('UPDATE werke SET pfad=? WHERE id=22',(str(W/'werk'),))
vor_werk={str(p.relative_to(W/'werk')):hashlib.sha256(p.read_bytes()).hexdigest() for p in (W/'werk').rglob('*') if p.is_file()}
kasse=c.execute('SELECT count(*) FROM kasse').fetchone()[0]
result=[]
for phase,args in [('gen0',[]),('mass',['--bestaetigt-von','Reparatur-Kernabnahme']),('generation',[])]:
 name=N+'-'+phase
 beleg=O/(name+'-kammer.json')
 cmd=['/root/reparatur-01/venv/bin/python',str(P/'cli_gate_kind.py'),phase,str(lid),*args]
 env=dict(os.environ,BIOTOP_DB=str(W/'privat.db'),BIOTOP_KAMMERBELEG=str(beleg),PYTHONPATH='/root/biotop',PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(P/'eltern-temp'))
 r=subprocess.run(cmd,cwd='/root/biotop',env=env,capture_output=True,text=True,timeout=30)
 (O/(name+'.stdout.txt')).write_text(r.stdout);(O/(name+'.stderr.txt')).write_text(r.stderr)
 daten=json.loads(beleg.read_text());z={'phase':phase,'befehl':cmd,'rc':r.returncode,'kammerlaeufe':len(daten),'stderr':r.stderr}
 result.append(z)
 assert r.returncode!=0 and 'Vorspann' in r.stderr and 'Nachweis fehlt' in r.stderr and not daten,z
assert c.execute('SELECT count(*) FROM kasse').fetchone()[0]==kasse
row=dict(c.execute('SELECT status,mass FROM laeufe WHERE id=?',(lid,)).fetchone());assert row=={'status':'kartiert','mass':None}
assert c.execute('SELECT count(*) FROM generationen WHERE lauf_id=?',(lid,)).fetchone()[0]==0
assert vor_werk=={str(p.relative_to(W/'werk')):hashlib.sha256(p.read_bytes()).hexdigest() for p in (W/'werk').rglob('*') if p.is_file()}
assert hashlib.sha256(D.read_bytes()).hexdigest()==vor
r={'art':'Drei reale CLI-Eingänge verweigern bei fehlendem Generation-minus-eins-Nachweis. Kein Test der ausdrücklich nach Phase4 verschobenen Gen0-Erfolgsbindung. Alle Writes privat.','lauf_id_nur_privat':lid,'faelle':result,'gesperrt':len(result),'von':len(result),'neue_modellbuchungen':0,'werk_unveraendert':True,'snapshot_unveraendert':True,'lauf_nachher':row}
(O/(N+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False))
