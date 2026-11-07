"""Aktuelle echte Vorspann-CLI im frischen Privatbestand; keine Evolution/Modelle."""
from pathlib import Path
import os,sys,sqlite3,json,hashlib,subprocess,time,datetime
sys.path.insert(0,'/root/biotop');sys.dont_write_bytecode=True
from biotop.organe import kammer,vorspann
P=Path('/root/reparatur-01');N=sys.argv[1];assert '/' not in N
W=P/('privat-'+N);W.mkdir(exist_ok=False)
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
for suffix in ('.json','.stdout.txt','.stderr.txt','-kammer.json','-plan.json'):assert not (O/(N+suffix)).exists()
D=P/'ausgang.db';Q=P/'teil-eichung/werk-lauf25-kopie'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def baum(p):return {str(f.relative_to(p)):sha(f) for f in sorted(p.rglob('*')) if f.is_file()}
def bestand(db):
    with sqlite3.connect(f'file:{db}?mode=ro',uri=True) as c:return hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
prod_db='/root/biotop/daten/biotop.db';vor_prod=bestand(prod_db);vor_sicherung=sha(D);vor_quelle=baum(Q)
con=sqlite3.connect(W/'privat.db',isolation_level=None);con.row_factory=sqlite3.Row
with sqlite3.connect(f'file:{D}?mode=ro&immutable=1',uri=True) as c:c.backup(con)
os.chmod(W/'privat.db',0o600)
prod_werk=Path(con.execute('SELECT pfad FROM werke WHERE id=22').fetchone()[0]);vor_prodwerk=baum(prod_werk)
kammer._kopie(Q,W/'werk');vor_werk=baum(W/'werk')
con.execute('UPDATE werke SET pfad=? WHERE id=22',(str(W/'werk'),))
lid=con.execute('SELECT max(id)+1 FROM laeufe').fetchone()[0]
con.execute("INSERT INTO laeufe(id,werk_id,status,budget_eur,mass,begonnen_am) VALUES(?,22,'kartiert',0,NULL,?)",(lid,datetime.datetime.now(datetime.timezone.utc).isoformat()))
max_kasse=con.execute('SELECT max(id) FROM kasse').fetchone()[0]
cmd=['/root/reparatur-01/venv/bin/python',str(P/'cli_gate_kind.py'),'vorspann',str(lid)]
env=dict(os.environ,BIOTOP_DB=str(W/'privat.db'),BIOTOP_KAMMERBELEG=str(O/(N+'-kammer.json')),PYTHONPATH='/root/biotop',PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(P/'eltern-temp'))
plan={'art':'Reparatur-Abnahme am frischen Privatbestand, keine natürliche Messkampagne','befehl':cmd,'privater_arbeitsordner':str(W),'lauf_id_nur_privat':lid,'budget_eur':0,'db_quelle_sha256':vor_sicherung,'produktiver_bestand_vorher':vor_prod,'kein_retry_unter_dieser_id':True,'verlangt':'Reale CLI, reale Rauschmessung/Fundneubewertung/vier Paare; nach Erfolg originalen gen0-Gate-Nachweis verlangen; keine Gen0-Mutantenkampagne/Evolution starten','quellen_sha256':{str(f.relative_to('/root/biotop')):sha(f) for f in sorted(Path('/root/biotop/biotop').rglob('*.py'))}}
(O/(N+'-plan.json')).write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
t=time.monotonic();p=subprocess.run(cmd,env=env,cwd='/root/biotop',capture_output=True,text=True,timeout=500)
(O/(N+'.stdout.txt')).write_text(p.stdout);(O/(N+'.stderr.txt')).write_text(p.stderr)
zaehler=json.loads((O/(N+'-kammer.json')).read_text())
row0=con.execute('SELECT * FROM vorspann_nachweise WHERE lauf_id=?',(lid,)).fetchone();row=dict(row0) if row0 else None
freigabe=False
if p.returncode==0:freigabe=bool(vorspann.verlangen(con,lid,'gen0')['nachweis_sha256'])
raw=[dict(z) for z in con.execute('SELECT * FROM eichkosten WHERE lauf_id=? ORDER BY id',(lid,))]
kasse=[dict(z) for z in con.execute('SELECT * FROM kasse WHERE id>?',(max_kasse,))]
schutz={'produktive_db_unveraendert':bestand(prod_db)==vor_prod,'sicherung_unveraendert':sha(D)==vor_sicherung,'werkquelle_unveraendert':baum(Q)==vor_quelle,'produktives_werk_unveraendert':baum(prod_werk)==vor_prodwerk,'privates_werk_unveraendert':baum(W/'werk')==vor_werk,'produktquellen_unveraendert':all(sha(Path('/root/biotop')/f)==h for f,h in plan['quellen_sha256'].items())}
r={**plan,'rc':p.returncode,'dauer_s':round(time.monotonic()-t,3),'nachweis':row,'gen0_nachweis_verwendbar':freigabe,'kammerlaeufe':len(zaehler),'eichkosten':raw,'neue_modellbuchungen':kasse,'schutz':schutz,'gebuchte_kammern':sum(z['kammerlaeufe'] for z in raw)}
(O/(N+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
ergebnis=json.loads(row['ergebnis']) if row else {}
print(json.dumps({'rc':p.returncode,'status':row['status'] if row else None,'gen0_nachweis_verwendbar':freigabe,'qualitaet':ergebnis.get('qualitaet'),'rauschen':ergebnis.get('rauschen'),'kammerlaeufe':len(zaehler),'gebuchte_kammern':r['gebuchte_kammern'],'neue_modellbuchungen':len(kasse),'schutz':schutz,'stderr':p.stderr},ensure_ascii=False,indent=2))
assert all(schutz.values()) and not kasse
if p.returncode==0:assert r['gebuchte_kammern']==len(zaehler),'Kammerbuchungen müssen mit tatsächlichen Ausführungen aufgehen'
con.close();sys.exit(p.returncode)
