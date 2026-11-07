#!/usr/bin/env python3
"""Nur lesende historische SQL-Auswertung; schreibt nur in diesen Lieferordner.
Keine Biotop-Imports, Modellaufrufe, Produktiv-CLI oder Tests.
"""
import collections
import datetime
import hashlib
import json
import pathlib
import sqlite3
import subprocess
from decimal import Decimal

OUT = pathlib.Path(__file__).resolve().parent
DB = pathlib.Path('/root/reparatur-01/ausgang.db')
REPO = pathlib.Path('/root/biotop')
AKTE = pathlib.Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe')

def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def git(*args):
    return subprocess.run(['git', '--no-optional-locks', '-C', str(REPO), *args], check=True, capture_output=True, text=True).stdout

def snap(path):
    s = path.stat()
    return {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': s.st_size, 'mtime_ns': s.st_mtime_ns}

c = sqlite3.connect(DB.as_uri() + '?mode=ro', uri=True)
c.row_factory = sqlite3.Row
c.execute('PRAGMA query_only=ON')

def rows(sql):
    return [dict(r) for r in c.execute(sql)]

queries = {
    'laeufe': 'SELECT * FROM laeufe WHERE id IN (22,23,24,25) ORDER BY id',
    'werke': 'SELECT id,name,pfad,quelle,aufgenommen_am,sprache,status FROM werke WHERE id IN (11,19,20,21,22) ORDER BY id',
    'generationen': 'SELECT * FROM generationen WHERE lauf_id IN (22,23,24,25) ORDER BY lauf_id,nummer',
    'kandidaten': 'SELECT id,lauf_id,generation,bereich,nische,anbieter,modell,status,grund,erstellt_am,ist_probe FROM kandidaten WHERE lauf_id IN (22,23,24,25) ORDER BY id',
    'kasse': 'SELECT * FROM kasse WHERE lauf_id IN (22,23,24,25) ORDER BY id',
    'immunsystem': 'SELECT id,werk_id,lauf_id,bereich,name,ursprung,status,erstellt_am,generation FROM immunsystem WHERE werk_id IN (11,19,20,21,22) ORDER BY id',
    'lazarus': 'SELECT id,lauf_id,generation,tag,archiv,pruefsumme,erstellt_am FROM lazarus WHERE lauf_id IN (22,23,24,25) ORDER BY id',
    'eichung': 'SELECT * FROM eichung WHERE lauf_id IN (22,23,24,25) ORDER BY id',
    'eichkosten': 'SELECT * FROM eichkosten WHERE lauf_id IN (22,23,24,25) ORDER BY id',
    'mentor': 'SELECT * FROM mentor WHERE lauf_id IN (22,23,24,25) ORDER BY id',
    'protokoll_sicher': "SELECT nr,zeit,art,inhalt FROM protokoll WHERE nr>=12400 AND art NOT LIKE 'anmeldung.%' AND art NOT LIKE 'benutzer.%' AND art NOT LIKE 'token.%' ORDER BY nr",
}
# Authentication tables and hash-chain links are deliberately not exported.
tracked = git('ls-files', '-z').split('\0')
initial = {'zeit_utc': datetime.datetime.now(datetime.UTC).isoformat(), 'db': snap(DB), 'git_head': git('rev-parse', 'HEAD').strip(), 'git_status': git('status', '--porcelain=v1'), 'tracked_files': {p: snap(REPO/p) for p in tracked if p and (REPO/p).is_file()}, 'counters': {t: rows(f'SELECT count(*) anzahl,max({pk}) letzte_id FROM {t}')[0] for t, pk in [('laeufe','id'),('kasse','id'),('protokoll','nr'),('generationen','id')]}}
if not (OUT/'zustand-vorher.json').exists():
    dump('zustand-vorher.json', initial)

all_data = {}
for name, sql in queries.items():
    data = rows(sql)
    if name == 'protokoll_sicher':
        for r in data:
            r['inhalt'] = json.loads(r['inhalt'])
    elif name in ('laeufe','generationen','mentor'):
        for r in data:
            for field in ('mass','masse','kandidaten','richtung','freigabe','richtungen','gewaehlt'):
                if isinstance(r.get(field), str):
                    try:
                        r[field] = json.loads(r[field])
                    except (ValueError, TypeError):
                        pass
    all_data[name] = data
    dump(name+'.json', data)
(OUT/'abfragen.sql').write_text('-- Ausschließlich SELECT auf eingefrorener SQLite, zu öffnen mit mode=ro.\n\n'+'\n\n'.join('-- '+name+'\n'+sql+';' for name,sql in queries.items())+'\n')

def summe(rs):
    return str(sum((Decimal(str(r['kosten_eur'])) for r in rs), Decimal('0')))

summary = {}
for lauf in (22,23,24,25):
    k = [r for r in all_data['kasse'] if r['lauf_id']==lauf]
    g = [r for r in all_data['generationen'] if r['lauf_id']==lauf]
    candidates = [r for r in all_data['kandidaten'] if r['lauf_id']==lauf]
    run_row = [r for r in all_data['laeufe'] if r['id']==lauf][0]
    candidates_events = [r for r in all_data['protokoll_sicher'] if r['inhalt'].get('lauf')==lauf or r['inhalt'].get('lauf_id')==lauf]
    events = [r for r in candidates_events if r['zeit'] >= run_row['begonnen_am']]
    a = [r for r in events if r['art']=='aegis.ansage']
    summary[lauf] = {
        'lauf': [r for r in all_data['laeufe'] if r['id']==lauf][0],
        'generationen': [{key:r.get(key) for key in ('id','nummer','status','tag','pruefsumme','grund','erstellt_am','freigabe_am','freigabe_grund')} | {'auswahl': (r.get('kandidaten') or {}).get('_gewaehlt')} for r in g],
        'kasse': {'anzahl':len(k), 'summe_eur_decimal':summe(k), 'erste_id':min(r['id'] for r in k),'letzte_id':max(r['id'] for r in k), 'erste_zeit':min(r['zeit'] for r in k),'letzte_zeit':max(r['zeit'] for r in k)},
        'kandidaten_gruppiert': [{'generation': key[0], 'nische':key[1], 'ist_probe':key[2], 'status':key[3], 'anzahl':n} for key,n in sorted(collections.Counter((r['generation'],r['nische'],r['ist_probe'],r['status']) for r in candidates).items())],
        'ansagen': {'gesamt':len(a), 'ausgefuehrt':sum(bool(r['inhalt'].get('ausgefuehrt')) for r in a), 'event_ids':[r['nr'] for r in a]},
        'ereignisarten_mit_explizitem_laufbezug': dict(collections.Counter(r['art'] for r in events)),
    }
dump('auswertung.json', summary)
err = []
for f in sorted((AKTE/'biotop-phase-4-vorbedingung-1/ausgaben').glob('*.err')):
    err.append({'datei':str(f),'bytes':f.stat().st_size,'inhalt':f.read_text()})
dump('runner-stderr.json',err)
print(json.dumps({l:{'status':s['lauf']['status'],'generationen':s['generationen'],'kasse':s['kasse'],'ansagen':s['ansagen'],'eventarten':s['ereignisarten_mit_explizitem_laufbezug']} for l,s in summary.items()},ensure_ascii=False,indent=2))
