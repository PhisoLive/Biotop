#!/usr/bin/env python3
"""Belegzitate direkt aus den lokalen Quellen anheften; keine freien Zitate."""
import json,pathlib,re,subprocess,urllib.parse
O=pathlib.Path(__file__).resolve().parent
S=pathlib.Path('/root/.hermes/skills/research/grounded-citations/scripts/sources.py')
base=['python3','-B',str(S),'--ledger',str(O/'quellenledger.json')]
cited=sorted({int(i) for i in re.findall(r'\[(\d+)\]',(O/'STATUS-24-25.md').read_text().split('## Sources')[0])})
ledger=json.loads((O/'quellenledger.json').read_text());sources={r['id']:r for r in ledger['sources']}
anchors={1:'"id": 4317',2:'"id": 24',3:'"id": 136',5:'"24": {',6:'"werk_id": 21',7:'"diff_produktiv_lauf24',8:'"id": 337',9:'"lauf24_25"',10:'Abgenommen ist:',11:'Durchgerutscht: über alle',12:'54.5',14:'### A33',15:'### B-01',18:'aegis._angriff =',19:'aegis._angriff =',20:'ABBRUCH:',21:'"sha256"',22:'SELECT * FROM laeufe',23:'"id": 3695',28:'# Direkte Prüfung',29:'"pro_lauf"',30:'schon = bisherige_behauptungen',31:'GEZEIGT =',32:'masse',33:'def _angriff(',34:'"verbindliche_wertungen"',35:'"nr": 16026',36:'"alle_pruefungen_ok": true',37:'-- 1.'}
quotes=[]
for sid in cited:
 path=pathlib.Path(urllib.parse.unquote(urllib.parse.urlparse(sources[sid]['url']).path))
 text=path.read_text();anchor=anchors[sid];pos=text.find(anchor)
 if pos<0:raise ValueError((sid,anchor))
 start=text.rfind('\n',0,pos)+1;end=min(len(text),start+1200)
 if end<len(text):end=text.rfind('\n',start,end)
 fragment=text[start:end]
 if sid==1:
  fragment=next(line for line in text.splitlines() if '"content":' in line)
 r=subprocess.run(base+['quote',str(sid),'--text',fragment,'--from',str(path)],check=True,capture_output=True,text=True)
 quotes.append({'id':sid,'quelle':str(path),'zeichen':len(fragment)})
print(json.dumps({'quellen_mit_verbatimbeleg':quotes},ensure_ascii=False,indent=2))
r=subprocess.run(base+['render','--replace-in',str(O/'STATUS-24-25.md')],check=True,capture_output=True,text=True);print(r.stdout.strip())
r=subprocess.run(base+['verify',str(O/'STATUS-24-25.md'),'--evidence','--min-coverage','0.5'],capture_output=True,text=True)
(O/'ZITATPRUEFUNG.txt').write_text(r.stdout+r.stderr+f'\nexit_code={r.returncode}\n')
print(r.stdout);print(r.stderr)
raise SystemExit(r.returncode)
