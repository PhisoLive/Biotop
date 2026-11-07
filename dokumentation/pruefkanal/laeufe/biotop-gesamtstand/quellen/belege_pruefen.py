"""Nur lesende Belegprüfung mit derselben Protokollfunktion; keine Biotop-Schreibverbindung."""
from pathlib import Path
import json,os,sys,sqlite3,datetime,hashlib,subprocess,collections
sys.dont_write_bytecode=True
sys.path.insert(0,'/root/biotop')
from biotop.kern.protokoll import pruefen
A=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand/ausgaben')
c=sqlite3.connect('file:/root/gesamtstand-01/bestand.db?mode=ro',uri=True);c.row_factory=sqlite3.Row
out={'hashkette':{'funktion':'biotop.kern.protokoll.pruefen','ergebnis':pruefen(c),'bezugszeilen':c.execute('SELECT count(*) FROM protokoll').fetchone()[0]},'tabellen_ohne_geheimnisse':{}}
for t in ('werke','eichkosten','eichung','eichgegenstand','jury','mentor','entropie'):
    out['tabellen_ohne_geheimnisse'][t]=[dict(r) for r in c.execute('SELECT * FROM '+t)]
p=[dict(r) for r in c.execute('SELECT * FROM protokoll WHERE art IN (\'modell.aufruf\',\'modell.antwort\',\'modell.fehler\') ORDER BY nr')]
aufrufe={r['nr']:r for r in p if r['art']=='modell.aufruf'};buchungen={r['protokoll_nr'] for r in c.execute('SELECT protokoll_nr FROM kasse')};fehler={json.loads(r['inhalt'])['aufruf_nr'] for r in p if r['art']=='modell.fehler'}
out['aufrufabgleich']={'anfragen':len(aufrufe),'gebucht':len(buchungen),'fehler':len(fehler),'ohne_antwort_oder_fehler':[r for n,r in aufrufe.items() if n not in buchungen and n not in fehler], 'gebucht_ohne_anfrage':sorted(buchungen-aufrufe.keys()),'doppelt_antwort_und_fehler':sorted(buchungen&fehler)}
(A/'19-belegpruefung.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
proc=[];bad=[];nr=0;hits=[]
for p in Path('/proc').iterdir():
    if not p.name.isdigit():continue
    nr+=1
    try:
        cmd=(p/'cmdline').read_bytes().replace(b'\0',b' ').decode(errors='replace');proc.append(p.name)
        if 'biotop' in cmd and not any(x in cmd for x in ('gesamtstand','python3 -c','sa-0-','sa-1-')):hits.append({'pid':p.name,'befehl':cmd})
    except (OSError,PermissionError) as e:bad.append({'pid':p.name,'fehler':type(e).__name__})
state={'zeit':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid_verzeichnisse':nr,'gelesen':len(proc),'nicht_gelesen':bad,'biotop_treffer':hits,'dienst_namentlich':{}}
for name,args in [('system',['systemctl','show','biotop.service','--property=LoadState,ActiveState,SubState,FragmentPath']),('benutzer',['systemctl','--user','show','biotop.service','--property=LoadState,ActiveState,SubState,FragmentPath']),('port',['ss','-ltnp']),('docker',['docker','ps','--format','{{.ID}} {{.Names}} {{.Image}}'])]:
    r=subprocess.run(args,capture_output=True,text=True);state['dienst_namentlich'][name]={'befehl':args,'rc':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
(A/'20-betrieb-mit-bezugsgroesse.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'hashkette':out['hashkette'],'aufrufabgleich':out['aufrufabgleich'],'prozesslesung':state},ensure_ascii=False,indent=2))
