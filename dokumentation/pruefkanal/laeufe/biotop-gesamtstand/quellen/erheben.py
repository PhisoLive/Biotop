"""Nur lesende Bestandsaufnahme; eigene Ausgaben außerhalb Biotop."""
import ast, collections, csv, datetime, hashlib, io, json, os, pathlib, sqlite3, subprocess, tarfile, tokenize
from decimal import Decimal
R=pathlib.Path('/root/biotop')
W=pathlib.Path('/root/gesamtstand-01')
O=pathlib.Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-gesamtstand')
for d in ('ausgaben','biotop','werk','quellen'): (O/d).mkdir(exist_ok=True)
def speichern(name,obj):
    (O/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def befehl(args):
    r=subprocess.run(args,capture_output=True,text=True); return {'befehl':args,'rc':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
def bestandszustand():
    out={}; fehler=[]
    for p in sorted(R.rglob('*')):
        if p.is_file() and not p.is_symlink():
            try:
                s=p.stat(); out[str(p.relative_to(R))]={'bytes':s.st_size,'mtime_ns':s.st_mtime_ns,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
            except Exception as e: fehler.append({'pfad':str(p),'fehler':str(e)})
    return {'zeit':datetime.datetime.now(datetime.timezone.utc).isoformat(),'dateien':out,'fehler':fehler}
if not (W/'vorher.json').exists():
    zustand=bestandszustand(); (W/'vorher.json').write_text(json.dumps(zustand)); speichern('ausgaben/01-zustand-vorher.json',zustand)
live=sqlite3.connect('file:/root/biotop/daten/biotop.db?mode=ro',uri=True)
if not (W/'bestand.db').exists():
    b=sqlite3.connect(W/'bestand.db'); live.backup(b); b.close(); os.chmod(W/'bestand.db',0o600)
c=sqlite3.connect(f'file:{W}/bestand.db?mode=ro',uri=True); c.row_factory=sqlite3.Row
zahlen={t[0]:c.execute('SELECT count(*) FROM "'+t[0]+'"').fetchone()[0] for t in c.execute("SELECT name FROM sqlite_master WHERE type='table'")}
speichern('ausgaben/02-datenbank.json',{'tabellen':zahlen,'page_size':c.execute('PRAGMA page_size').fetchone()[0],'page_count':c.execute('PRAGMA page_count').fetchone()[0],'freelist_count':c.execute('PRAGMA freelist_count').fetchone()[0],'integrity_check':[list(r) for r in c.execute('PRAGMA integrity_check')],'live_dateien':{str(p.name):{'bytes':p.stat().st_size,'belegt_bytes':p.stat().st_blocks*512} for p in R.glob('daten/biotop.db*')},'kasse':{'anzahl':zahlen['kasse'],'max_id':c.execute('SELECT max(id) FROM kasse').fetchone()[0],'summe_eur':str(sum((Decimal(str(r[0])) for r in c.execute('SELECT kosten_eur FROM kasse')),Decimal(0)))}})
git=befehl(['git','-C',str(R),'ls-files','-z']); files=git['stdout'].rstrip('\0').split('\0'); reihen=[]; symbole=[]
for f in files:
    p=R/f; b=p.read_bytes(); txt=b.decode('utf8'); ls=txt.splitlines(); cat=f.split('/')[0] if '/' in f else 'wurzel'
    row={'pfad':f,'gruppe':cat,'bytes':len(b),'zeilen':len(ls),'leer':sum(not x.strip() for x in ls),'sha256':hashlib.sha256(b).hexdigest()}
    if f.endswith('.py'):
        tree=ast.parse(txt); tokens=list(tokenize.generate_tokens(io.StringIO(txt).readline)); code=set(); kommentare=set(); docs=set()
        for n in ast.walk(tree):
            if isinstance(n,(ast.Module,ast.ClassDef,ast.FunctionDef,ast.AsyncFunctionDef)) and n.body and isinstance(n.body[0],ast.Expr) and isinstance(n.body[0].value,ast.Constant) and isinstance(n.body[0].value.value,str): docs.update(range(n.body[0].lineno,n.body[0].end_lineno+1))
            if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): symbole.append({'pfad':f,'name':n.name,'art':type(n).__name__,'von':n.lineno,'bis':n.end_lineno,'asserts':sum(isinstance(x,ast.Assert) for x in ast.walk(n))})
        for t in tokens:
            if t.type==tokenize.COMMENT: kommentare.update(range(t.start[0],t.end[0]+1))
            elif t.type not in (tokenize.ENCODING,tokenize.ENDMARKER,tokenize.NEWLINE,tokenize.NL,tokenize.INDENT,tokenize.DEDENT): code.update(range(t.start[0],t.end[0]+1))
        row.update({'python_codezeilen':len(code-docs),'python_dokumentationszeilen':len((docs|kommentare)- (code-docs)),'assert_anweisungen':sum(isinstance(n,ast.Assert) for n in ast.walk(tree)),'test_funktionen':sum(isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and n.name.startswith('test_') for n in ast.walk(tree))})
    reihen.append(row)
speichern('ausgaben/03-dateien.json',reihen); speichern('ausgaben/04-symbole.json',symbole)
gruppen={}
for g in sorted(set(r['gruppe'] for r in reihen)):
    a=[r for r in reihen if r['gruppe']==g]; gruppen[g]={'dateien':len(a),'zeilen':sum(r['zeilen'] for r in a),'bytes':sum(r['bytes'] for r in a),'python_dateien':sum(r['pfad'].endswith('.py') for r in a),'assert_anweisungen':sum(r.get('assert_anweisungen',0) for r in a),'test_funktionen':sum(r.get('test_funktionen',0) for r in a)}
speichern('ausgaben/05-umfang.json',{'definition':'Git-verfolgte Dateien am Arbeitsstand; Daten/Werke/Git-Objekte/Caches separat, keine Abhängigkeiten als eigener Code. Zeilen=splitlines, einschließlich letzter Zeile ohne LF. Python Code mittels tokenize ohne reine Kommentare/Docstrings. Kein pygount installiert; keine Installation am Wirt. AST-assert ist keine ausgeführte Testzahl.','gruppen':gruppen,'gesamt':{'dateien':len(reihen),'zeilen':sum(r['zeilen'] for r in reihen)},'organ_module':[r for r in reihen if r['pfad'].startswith('biotop/organe/') and not r['pfad'].endswith('__init__.py')]})
# Rohbuchungen vollständig, ohne Anmeldetabellen oder Geheimnisse.
kasse=[dict(r) for r in c.execute('SELECT * FROM kasse ORDER BY id')]; speichern('ausgaben/06-kassenbuchungen.json',kasse)
runs=[]
for r in c.execute('SELECT l.*,w.name werkname,w.quelle werkquelle FROM laeufe l LEFT JOIN werke w ON w.id=l.werk_id ORDER BY l.id'):
    d=dict(r); ks=[x for x in kasse if x['lauf_id']==d['id']]; d['aufrufe']=len(ks); d['kosten_eur']=str(sum((Decimal(str(x['kosten_eur'])) for x in ks),Decimal(0))); d['kasse_ids']=[x['id'] for x in ks]; d['generationen_status']={x[0]:x[1] for x in c.execute('SELECT status,count(*) FROM generationen WHERE lauf_id=? GROUP BY status',(d['id'],))}; d['kandidaten_status']={x[0]:x[1] for x in c.execute('SELECT status,count(*) FROM kandidaten WHERE lauf_id=? GROUP BY status',(d['id'],))}; runs.append(d)
speichern('ausgaben/07-laeufe.json',runs)
protokoll=[dict(r) for r in c.execute('SELECT * FROM protokoll ORDER BY nr')]
# Protokoll nur fachliche Daten veröffentlichen; Anmeldungen enthalten keine für diese Prüfung nötigen Inhalte.
for r in protokoll:
    if r['art'].startswith('anmeldung.'): r['inhalt']='[Anmeldeereignis: Inhalt nicht veröffentlicht]'
speichern('ausgaben/08-protokoll.json',protokoll)
speichern('ausgaben/09-protokollarten.json',[dict(r) for r in c.execute('SELECT art,count(*) anzahl,min(nr) erste_nr,max(nr) letzte_nr FROM protokoll GROUP BY art')])
# Unveränderte Quelle als eigenständig nachprüfbarer Stand.
with tarfile.open(O/'biotop/QUELLSTAND-01.tar.gz','w:gz') as tar:
    for f in files: tar.add(R/f,arcname='biotop/'+f,recursive=False)
mp=pathlib.Path('/root/.hermes/cache/documents/doc_8d640daa6c3c_INFINITE-EVOLUTION-BIOTOP-Masterprompt-v6.md')
(O/'quellen/MASTERPROMPT-FASSUNG-6.md').write_bytes(mp.read_bytes())
speichern('ausgaben/10-git.json',{k:befehl(['git','-C',str(R),*v]) for k,v in {'stand':['rev-parse','HEAD'],'status':['status','--porcelain=v1'],'historie':['log','--format=%H %aI %s'],'diff':['diff','--stat']}.items()})
# Nur prüfrelevante Dienste/Prozesse, keine Umgebungsvariablen.
proz=[]; unlesbar=[]
for p in pathlib.Path('/proc').iterdir():
    if not p.name.isdigit(): continue
    try:
        cmd=(p/'cmdline').read_bytes().replace(b'\0',b' ').decode(errors='replace')
        if 'biotop' in cmd and 'erheben.py' not in cmd and 'python3 -c' not in cmd: proz.append({'pid':p.name,'cmd':cmd})
    except (FileNotFoundError,PermissionError) as e: unlesbar.append({'pid':p.name,'fehler':type(e).__name__})
speichern('ausgaben/11-betrieb.json',{'zeit':datetime.datetime.now(datetime.timezone.utc).isoformat(),'prozesse_biotop':proz,'prozess_lesefehler':unlesbar,'systemdienst':befehl(['systemctl','show','biotop.service','--property=ActiveState,SubState,FragmentPath,ExecStart']),'benutzerdienst':befehl(['systemctl','--user','show','biotop.service','--property=ActiveState,SubState,FragmentPath,ExecStart']),'docker':befehl(['docker','ps','--format','{{.Names}} {{.Status}} {{.Image}}']),'ports':befehl(['ss','-ltnp'])})
print(json.dumps({'umfang':gruppen,'summe_dateien':len(reihen),'summe_zeilen':sum(r['zeilen'] for r in reihen),'tabellen':zahlen,'kosten1bis23':str(sum((Decimal(r['kosten_eur']) for r in runs if r['id']<=23),Decimal(0))),'kosten24bis25':str(sum((Decimal(r['kosten_eur']) for r in runs if r['id']>23),Decimal(0)))},ensure_ascii=False,indent=2))
