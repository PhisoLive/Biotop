"""Unabhängigen Prüfstand versiegeln; nur erlaubte Quell-/Testdateien kopieren."""
from pathlib import Path
import subprocess,hashlib,json,re,shutil
R=Path('/root/biotop'); O=Path('/root/reparatur-01/review-02'); O.mkdir(exist_ok=False)
def git(*args):return subprocess.check_output(['git','-C',str(R),*args]).decode()
dateien=git('ls-files','-z').rstrip('\0').split('\0')
neue=git('ls-files','--others','--exclude-standard','-z').rstrip('\0').split('\0')
dateien=sorted(set(dateien+[f for f in neue if f]))
assert not any(f.startswith('daten/') or '/.env' in f for f in dateien)
sha={}
for f in dateien:
    p=O/'repo'/f;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(R/f,p)
    sha[f]=hashlib.sha256(p.read_bytes()).hexdigest()
diff=git('diff','HEAD','--')
for f in neue:
    if not f:continue
    r=subprocess.run(['git','diff','--no-index','--','/dev/null',str(R/f)],capture_output=True,text=True)
    assert r.returncode in (0,1)
    diff+=r.stdout.replace('b'+str(R)+'/', 'b/')
(O/'AENDERUNGEN.diff').write_text(diff)
regeln={'secret':r'(?:api_key|secret|password|token|passwd)\s*=','shell':r'os\.system\(|shell\s*=\s*True','eval_exec':r'\b(?:eval|exec)\(','pickle':r'pickle\.loads?\(','sql_format':r'execute\(f'}
befunde=[];pfad=None;nr=0
for line in diff.splitlines():
    if line.startswith('+++ '):pfad=line[4:]
    if line.startswith('@@ '):
        m=re.search(r'\+(\d+)',line);nr=int(m[1]) if m else 0
    elif line.startswith('+') and not line.startswith('+++'):
        for regel,muster in regeln.items():
            if re.search(muster,line,re.I):befunde.append({'pfad':pfad,'zeile':nr,'regel':regel,'code':line[1:]})
        nr+=1
    elif line.startswith(' '):nr+=1
(O/'STATIK.json').write_text(json.dumps({'umfang':'Nur neue Zeilen des Reparaturdiffs; Treffer sind Prüfhinweise, keine automatische Schwerewertung','treffer':befunde},ensure_ascii=False,indent=2)+'\n')
(O/'QUELLHASHES.json').write_text(json.dumps(sha,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'review':str(O),'dateien':len(dateien),'diff_bytes':len(diff.encode()),'statik_treffer':befunde},ensure_ascii=False))
