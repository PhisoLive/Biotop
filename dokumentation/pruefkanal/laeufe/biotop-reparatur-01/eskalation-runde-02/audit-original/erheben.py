"""Read-only source audit collector. Never imports or runs Biotop code."""
from pathlib import Path
import ast, collections, datetime, hashlib, json, os, subprocess
ROOT = Path('/root/biotop')
OUT = Path('/root/reparatur-01/nachweis-leserpruefung-02/audit')
INPUT = OUT.parent

def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def state(p):
    b = p.read_bytes()
    return {'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b), 'mtime_ns': p.stat().st_mtime_ns, 'zeilen': len(b.decode().splitlines())}

def collect():
    inventory = json.loads((INPUT / 'QUELLEN.json').read_text())
    assert len(inventory) == 126 and len({x['pfad'] for x in inventory}) == 126
    entries=[]; scopes=[]
    for row in inventory:
        p = ROOT / row['pfad']
        s = state(p)
        dest = OUT / 'quellen' / row['pfad']
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(p.read_bytes())
        assert state(dest)['sha256'] == s['sha256']
        entries.append({**row, 'erhoben': s, 'manifest_identisch': all(s[k] == row[k] for k in ('sha256','bytes','mtime_ns'))})
        if p.suffix == '.py':
            text = dest.read_text()
            tree = ast.parse(text, filename=row['pfad'])
            for n in ast.walk(tree):
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    scopes.append({'pfad':row['pfad'],'name':n.name,'typ':type(n).__name__,'von':n.lineno,'bis':n.end_lineno})
                if isinstance(n, ast.Constant) and isinstance(n.value,str) and len(n.value.splitlines()) > 8:
                    scopes.append({'pfad':row['pfad'],'name':'multiline_string','typ':'str','von':n.lineno,'bis':n.end_lineno,'inhaltzeilen':len(n.value.splitlines())})
    env = {**os.environ, 'GIT_OPTIONAL_LOCKS':'0'}
    git = {cmd:subprocess.run(['git','-C',str(ROOT),*cmd.split()],env=env,capture_output=True,text=True).stdout for cmd in ('rev-parse HEAD','status --porcelain=v1','ls-files')}
    dump('QUELLZUSTAND-vorher.json', {'zeit':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inventar':entries,'gruppen':dict(collections.Counter(x['gruppe'] for x in entries)),'git':git})
    dump('AST-UMFANG.json',scopes)
    dump('EINGABE-SUCHTREFFER.json',json.loads((INPUT/'SUCHTREFFER.json').read_text()))
    print(json.dumps({'files':len(entries),'gruppen':dict(collections.Counter(x['gruppe'] for x in entries)),'manifestabweichungen':[r['pfad'] for r in entries if not r['manifest_identisch']],'zeilen':sum(r['erhoben']['zeilen'] for r in entries),'scopes':len(scopes),'git':git},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    collect()
