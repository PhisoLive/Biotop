from pathlib import Path
import os, subprocess, json
from datetime import datetime, timezone
W=Path('/root/wiedereinstieg-01')
B=W/'belege'
R=W/'traegernachweis'
R.mkdir(exist_ok=False)
cmd=['hermes','--ignore-rules','-z','Nur deine Modellkennung. Keine Werkzeuge.','--usage-file',str(R/'VERBRAUCH-01.json')]
env=os.environ.copy()
env['PYTHONPATH']=str(W/'aufrufwache')+os.pathsep+env.get('PYTHONPATH','')
env['W4_WACHE_VERZEICHNIS']=str(R)
start=datetime.now(timezone.utc).isoformat()
# Keine Wiederholung bei Fehler. Die Wache laesst genau einen POST ins Netz.
with (R/'AUSGABE-01.txt').open('xb') as out, (R/'AUSGABE-01.err').open('xb') as err:
    p=subprocess.run(cmd,env=env,stdout=out,stderr=err,timeout=240,cwd='/root')
ende=datetime.now(timezone.utc).isoformat()
(R/'AUFRUF-01.json').write_text(json.dumps({'zweck':'W4.einmaliger_traegernachweis','kommando':cmd,'start_utc':start,'ende_utc':ende,'exit_code':p.returncode,'prozesslokale_wache':str(W/'aufrufwache/sitecustomize.py'),'modell_provider_ueberschrieben':False,'regeln_ausgeblendet':True,'maximale_post_uebertragungen':1},indent=2))
for name in ['AUFRUF-01.json','AUSGABE-01.txt','AUSGABE-01.err','VERBRAUCH-01.json','HTTP-WACHE-01.jsonl']:
    f=R/name
    print('\n###',name,'\n',f.read_text() if f.exists() else 'FEHLT')
f=R/'HTTP-ANTWORT-01.txt'
if f.exists():
    texte=f.read_text()
    daten=[]
    try: daten=[json.loads(texte)]
    except json.JSONDecodeError:
        for line in texte.splitlines():
            if line.startswith('data: '):
                try: daten.append(json.loads(line[6:]))
                except json.JSONDecodeError: pass
    print('API-MODELLMETADATEN',[(d.get('model'),d.get('message',{}).get('model'),d.get('usage')) for d in daten if d.get('model') or d.get('message',{}).get('model') or d.get('usage')])
