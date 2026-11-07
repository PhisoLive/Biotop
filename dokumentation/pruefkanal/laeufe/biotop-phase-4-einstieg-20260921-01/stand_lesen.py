"""Nur lesen: Quellen, Dateibestand, Kassen und bestehende Sitzungsbindung.
Keine Biotop-Imports, Tests, Modellaufrufe, Neustarts oder Konfigurationsänderungen.
"""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
from collections import Counter
import hashlib
import json
import os
import sqlite3
import subprocess
import urllib.request
from concurrent.futures import ThreadPoolExecutor

P = Path(__file__).resolve().parent
R = Path('/root/biotop')
PUB = Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe')
URL = 'https://milieulux-reinigung-muenchen.de/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/'
STAMM = 'biotop-phase-4-vorbedingung-1/nach-reparatur-02/'
MASTER = 'biotop-wiedereinstieg-2026-09-20-01/INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6-01.md'
DBS = {'produktiv': Path('/root/biotop/daten/biotop.db'), 'privat_lauf26': Path('/root/phase-4-vorbedingung-1/privat/biotop.db')}

def sha(b):
    return hashlib.sha256(b).hexdigest()

def cmd(*args):
    env = dict(os.environ, GIT_OPTIONAL_LOCKS='0', PYTHONDONTWRITEBYTECODE='1')
    r = subprocess.run(args, capture_output=True, text=True, timeout=40, env=env)
    return {'befehl': list(args), 'exit_code': r.returncode, 'stdout': r.stdout, 'stderr': r.stderr}

def schreiben(name, obj):
    (P / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def signatur(path):
    if not path.is_file():
        return {'vorhanden': False}
    s = path.stat()
    return {'vorhanden': True, 'bytes': s.st_size, 'mtime_ns': s.st_mtime_ns, 'sha256': sha(path.read_bytes())}

zeit = datetime.now(timezone.utc).isoformat()
tracked = cmd('git','-C',str(R),'ls-files','-z')
alle = cmd('git','-C',str(R),'ls-files','--cached','--others','--exclude-standard','-z')
assert tracked['exit_code'] == alle['exit_code'] == 0
tracked_set = set(tracked['stdout'].split('\0')) - {''}
namen = sorted(set(alle['stdout'].split('\0')) - {''})
schutzpfade = [R / n for n in namen] + [Path('/root/.hermes/config.yaml')]
for db in DBS.values():
    schutzpfade.extend([db, Path(str(db)+'-wal'), Path(str(db)+'-shm')])
vorher = {str(p):signatur(p) for p in schutzpfade}

dateien, unlesbar = [], []
for name in namen:
    f = R / name
    if f.name.startswith('.env'):
        unlesbar.append({'pfad':name,'grund':'Geheimnisdatei nicht gelesen'})
        continue
    try:
        b = f.read_bytes()
        text = b.decode()
    except (OSError, UnicodeError) as e:
        unlesbar.append({'pfad':name,'grund':type(e).__name__})
        continue
    dateien.append({'pfad':name,'sha256':sha(b),'physische_zeilen':len(text.splitlines()),
                    'gruppe':name.split('/')[0] if '/' in name else 'wurzel','git_erfasst':name in tracked_set})
python_namen = sorted(str(p.relative_to(R)) for t in ('biotop','tests','pruefung') for p in (R/t).rglob('*.py')
    if not any(x in ('__pycache__','.venv','venv','node_modules') for x in p.relative_to(R).parts))
python_dateien = [{'pfad':n,'sha256':sha((R/n).read_bytes()),'physische_zeilen':len((R/n).read_text().splitlines())} for n in python_namen]
alt = json.loads(Path('/root/phase-4-vorbedingung-1/belege/BESTAND.json').read_text())
alt_py = {r['pfad']:r['sha256'] for r in alt['dateien']}
neu_py = {r['pfad']:r['sha256'] for r in python_dateien}
alt_gesamt = {r['pfad']:r['sha256'] for r in alt['gesamtsicht_eigene_quellen']['dateiliste']}
neu_gesamt = {r['pfad']:r['sha256'] for r in dateien}

def vergleich(a,b):
    gleich = [n for n in a.keys() & b.keys() if a[n] == b[n]]
    return {'alt':len(a),'neu':len(b),'sha256_gleich':len(gleich),'geaendert':[n for n in sorted(a.keys() & b.keys()) if a[n]!=b[n]],'fehlend':sorted(a.keys()-b.keys()),'zusaetzlich':sorted(b.keys()-a.keys())}

bestand = {'zeit_utc':zeit,'definition':'Wie die Übergabe: eigene Dateien aus git ls-files --cached --others --exclude-standard; Python separat unter biotop/tests/pruefung, ohne Abhängigkeiten/Caches. Physische Zeilen per splitlines, keine SLOC-Behauptung.',
    'git_head':cmd('git','-C',str(R),'rev-parse','HEAD'),'git_status':cmd('git','-C',str(R),'status','--porcelain=v1'),
    'eigene_dateien':len(dateien),'erfasste_pfade':len(namen),'physische_zeilen':sum(r['physische_zeilen'] for r in dateien),
    'git_erfasst':sum(r['git_erfasst'] for r in dateien),'unlesbar':unlesbar,'dateien':dateien,
    'python_dateien':len(python_dateien),'python_physische_zeilen':sum(r['physische_zeilen'] for r in python_dateien),
    'python_dateiliste':python_dateien,'vergleich_python_zur_uebergabe':vergleich(alt_py,neu_py),'vergleich_gesamt_zur_uebergabe':vergleich(alt_gesamt,neu_gesamt),
    'organmodule_ohne_init':[str(p.relative_to(R)) for p in sorted((R/'biotop/organe').glob('*.py')) if p.name!='__init__.py']}
bestand['gruppen']={g:{'dateien':sum(r['gruppe']==g for r in dateien),'physische_zeilen':sum(r['physische_zeilen'] for r in dateien if r['gruppe']==g)} for g in sorted({r['gruppe'] for r in dateien})}
assert sum(g['dateien'] for g in bestand['gruppen'].values()) == len(dateien)
schreiben('BESTAND-AKTUELL.json',bestand)

kassen = {}
rohdaten = {}
for name, db in DBS.items():
    c=sqlite3.connect('file:'+str(db)+'?mode=ro',uri=True)
    c.row_factory=sqlite3.Row
    c.execute('PRAGMA query_only=ON')
    c.execute('BEGIN')
    rows=[dict(r) for r in c.execute('SELECT id,lauf_id,zeit,anbieter,modell,tokens_ein,tokens_aus,kosten_eur,zweck,kontingent,protokoll_nr FROM kasse ORDER BY id')]
    rohdaten[name]=rows
    kassen[name]={'datei':str(db),'buchungen':len(rows),'erste_id':rows[0]['id'] if rows else None,'letzte_id':rows[-1]['id'] if rows else None,
        'summe_eur_sqlite':c.execute('SELECT SUM(kosten_eur) FROM kasse').fetchone()[0],
        'summe_eur_decimal':str(sum((Decimal(str(r['kosten_eur'])) for r in rows),Decimal(0))),
        'zeilen_sha256':sha(json.dumps(rows,sort_keys=True,ensure_ascii=False).encode()),
        'letzte_laeufe':[dict(r) for r in c.execute('SELECT id,werk_id,status,budget_eur,begonnen_am,beendet_am FROM laeufe ORDER BY id DESC LIMIT 3')]}
    if name=='privat_lauf26':
        kassen[name]['lauf26']=dict(c.execute('SELECT id,werk_id,status,budget_eur,begonnen_am,beendet_am,grund FROM laeufe WHERE id=26').fetchone())
        kassen[name]['generationen26']=[dict(r) for r in c.execute('SELECT nummer,status,grund FROM generationen WHERE lauf_id=26 ORDER BY nummer')]
    c.rollback()
    c.close()
prod = {r['id']:r for r in rohdaten['produktiv']}
priv = {r['id']:r for r in rohdaten['privat_lauf26']}
gemeinsam=set(prod)&set(priv)
neu = [r for r in rohdaten['privat_lauf26'] if r['id']>4070]
assert len(gemeinsam)==len(prod)
assert all(prod[i]==priv[i] for i in gemeinsam)
assert set(priv)-set(prod) == {r['id'] for r in neu}
assert all(r['lauf_id']==26 for r in neu)
assert Decimal(kassen['produktiv']['summe_eur_decimal'])+sum((Decimal(str(r['kosten_eur'])) for r in neu),Decimal(0))==Decimal(kassen['privat_lauf26']['summe_eur_decimal'])
kassen['abgleich']={'gemeinsame_identische_zeilen':len(gemeinsam),'produktive_zeilen':len(prod),'zusaetzliche_private_zeilen':len(neu),
    'ids_neuer_buchungen':[r['id'] for r in neu],'kosten_neu_eur_decimal':str(sum((Decimal(str(r['kosten_eur'])) for r in neu),Decimal(0))),
    'grenze':'Produktive und private Gesamtbeträge überlappen. Nicht addieren. Keine neue Budgetfreigabe.'}
schreiben('KASSE-AKTUELL.json',kassen)
schreiben('LAUF26-BUCHUNGEN.json',neu)

quellen=[STAMM+r+'/UEBERGABE-PHASE-4.md' for r in ('uebergabe-abnahme-01','abschluss-01','abschluss-02')]+[MASTER,STAMM+'abschluss-02/OFFEN.md',STAMM+'abschluss-02/KASSE.md',STAMM+'abschluss-02/MANIFEST.sha256',STAMM+'uebergabe-abnahme-01/MANIFEST.sha256']
def holen(rel):
    local=(PUB/rel).read_bytes()
    with urllib.request.urlopen(URL+rel,timeout=30) as r:
        remote=r.read(); code=r.status
    return {'pfad':rel,'url':URL+rel,'http_status':code,'bytes':len(remote),'zeilen':len(remote.decode().splitlines()),'sha256':sha(remote),'https_lokal_bytegleich':remote==local}
with ThreadPoolExecutor(max_workers=4) as pool:
    herkunft=list(pool.map(holen,quellen))
assert all(r['https_lokal_bytegleich'] and r['http_status']==200 for r in herkunft)
pruefungen=[]
for revision in ('abschluss-02','uebergabe-abnahme-01'):
    base=PUB/STAMM/revision
    mf=(base/'MANIFEST.sha256').read_bytes()
    rows=[]
    for line in mf.decode().splitlines():
        digest,name=line.split(maxsplit=1)
        name=name.lstrip('*')
        p=(base/name).resolve()
        assert p.is_relative_to(base.resolve())
        actual=sha(p.read_bytes())
        rows.append({'datei':name,'soll':digest,'ist':actual,'gleich':digest==actual})
    pruefungen.append({'revision':revision,'manifest_sha256':sha(mf),'geprueft':len(rows),'gleich':sum(r['gleich'] for r in rows),'dateien':rows})
assert all(r['geprueft']==r['gleich'] for r in pruefungen)
review=json.loads((PUB/STAMM/'abschluss-02/REVIEW.json').read_text())
schreiben('QUELLEN-UND-ABNAHME.json',{'https_quellen':herkunft,'manifeste':pruefungen,'review_urteil':{k:review[k] for k in ('passed','abgeschlossen','status','umfang') if k in review},'review_feldnamen':list(review),'geltung':'Abnahme durch Philipp steht in uebergabe-abnahme-01. Ältere rote Wertungen und der erste Reviewabbruch bleiben historisch.'})

sid=os.environ.get('HERMES_SESSION_ID')
sk=os.environ.get('HERMES_SESSION_KEY')
sd=json.loads(Path('/root/.hermes/sessions/sessions.json').read_text())
entry=sd.get('sessions',sd).get(sk,{})
c=sqlite3.connect('file:/root/.hermes/state.db?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('PRAGMA query_only=ON')
row=c.execute('SELECT id,source,model,billing_provider,started_at,ended_at,api_call_count FROM sessions WHERE id=?',(sid,)).fetchone()
sitzung=dict(row) if row else None;c.close()
traeger={'zeit_utc':datetime.now(timezone.utc).isoformat(),'aktuelle_sitzung':sitzung,
    'routing':{k:entry[k] for k in ('session_id','created_at','updated_at','model_override','is_fresh_reset','was_auto_reset','prev_session_id') if k in entry},
    'gateway':cmd('systemctl','--user','show','hermes-gateway.service','-p','MainPID','-p','ExecMainStartTimestamp'),
    'moa_trace_fuer_diese_sitzung_vorhanden':(Path('/root/.hermes/moa-traces')/(str(sid)+'.jsonl')).exists(),
    'config_get':{key:cmd('hermes','config','get',key) for key in ('model.default','model.provider','agent.reasoning_effort','moa.active_preset','moa.presets.astra-opus-max')},
    'grenze':'Sitzungsbindung und vorhandener Laufzeitkontext, keine neue Inferenzprobe. Kein neuer Wire-Nachweis von max oder 900k. Die alte Sitzungs-ID darf nicht als frischer Kontextreset bezeichnet werden.'}
schreiben('TRAEGER-AKTUELL.json',traeger)

ps=cmd('ps','-eo','pid=,ppid=,comm=,args=')
prozesse=[]
for line in ps['stdout'].splitlines():
    parts=line.strip().split(None,3)
    if len(parts)==4:
        prozesse.append({'pid':int(parts[0]),'ppid':int(parts[1]),'comm':parts[2],'args':parts[3]})
pp={r['pid']:r['ppid'] for r in prozesse}
ignore=set(); pid=os.getpid()
while pid and pid not in ignore:
    ignore.add(pid);pid=pp.get(pid,0)
markers=('-m biotop','/root/biotop/','phase-4-vorbedingung-1/messen.py','phase-4-vorbedingung-1/lauf_kommando.py')
hits=[r for r in prozesse if r['pid'] not in ignore and any(m in r['args'] for m in markers)]
schreiben('BETRIEB-AKTUELL.json',{'zeit_utc':datetime.now(timezone.utc).isoformat(),'ps_zeilen':len(prozesse),'eigene_ahnen_ausgeschlossen':sorted(ignore),'biotop_marker_treffer':hits,
    'marker':markers,'alte_pid_1921606':cmd('ps','-p','1921606','-o','pid=,stat=,etime=,args='),
    'biotop_dienst':cmd('systemctl','show','biotop.service','-p','LoadState','-p','ActiveState','-p','SubState','-p','MainPID'),
    'docker_laufend':cmd('docker','ps','--format','{{.ID}} {{.Image}} {{.Names}}'),
    'grenze':'Begrenzte Prozess-/Dienstabfrage, keine Prüfung der Web-Anmeldung und kein Start inaktiver Dienste.'})
nachher={str(p):signatur(p) for p in schutzpfade}
aenderungen=[{'pfad':n,'vorher':vorher[n],'nachher':nachher[n]} for n in vorher if vorher[n]!=nachher[n]]
schreiben('LESEGRENZE.json',{'beginn_utc':zeit,'ende_utc':datetime.now(timezone.utc).isoformat(),'erfasste_pfade':len(vorher),'unveraendert':len(vorher)-len(aenderungen),'aenderungen':aenderungen,'vorher':vorher,'nachher':nachher,'scope':'Quellen, config.yaml und beide Biotop-DBs samt ggf. vorhandenen WAL/SHM-Dateien. Hermes-Sitzungszähler ändern sich durch den laufenden Träger und gehören nicht zum Biotop-Schreibverbot.'})
print(json.dumps({'zeit_utc':zeit,'bestand':{k:bestand[k] for k in ('eigene_dateien','erfasste_pfade','physische_zeilen','git_erfasst','python_dateien','python_physische_zeilen','vergleich_python_zur_uebergabe','vergleich_gesamt_zur_uebergabe')},
    'organmodule':len(bestand['organmodule_ohne_init']),'kassen':{k:{kk:vv for kk,vv in v.items() if kk not in ('ids_neuer_buchungen',)} for k,v in kassen.items()},
    'quellen':herkunft,'abnahme_manifeste':[{k:v for k,v in m.items() if k!='dateien'} for m in pruefungen],
    'traeger':traeger,'biotop_prozesstreffer':len(hits),'prozesszeilen':len(prozesse),'unveraendert_von':[len(vorher)-len(aenderungen),len(vorher)],'veraenderte_pfade':[r['pfad'] for r in aenderungen]},ensure_ascii=False,indent=2))
