"""Patchvergleich, Umfangsnachweis, Prüfsummen und vollständiges Fixpaket."""
import ast
import hashlib
import json
import shutil
import subprocess
import tarfile
from pathlib import Path

ROOT = Path('/root/reparatur-01/nachbesserung-01/vertrag')
OUT = ROOT / 'lieferung'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

p = subprocess.run(['/root/reparatur-01/venv/bin/python', str(ROOT/'werkzeuge/liefern.py')],
                   cwd=ROOT/'repo', capture_output=True, text=True)
(ROOT/'packen.stdout.txt').write_text(p.stdout)
(ROOT/'packen.stderr.txt').write_text(p.stderr)
assert p.returncode == 0, p.stderr

patchroot = ROOT/'patchnachweis'
shutil.copytree(ROOT/'ausgang-repo',patchroot)
commands = []
for args in (['git','apply','--check',str(OUT/'AENDERUNGEN.diff')], ['git','apply',str(OUT/'AENDERUNGEN.diff')]):
    p = subprocess.run(args,cwd=patchroot,capture_output=True,text=True)
    commands.append(dict(argv=args,cwd=str(patchroot),rc=p.returncode,stdout=p.stdout,stderr=p.stderr))
    assert p.returncode == 0, p.stderr

def inv(path):
    return {p.relative_to(path).as_posix():sha(p) for p in path.rglob('*') if p.is_file()}
assert inv(patchroot) == inv(ROOT/'repo')
old, new = [ast.parse((ROOT/d/'biotop/organe/eichproben.py').read_text()) for d in ('ausgang-repo','repo')]
changed_functions=[]
old_f={n.name:n for n in old.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
new_f={n.name:n for n in new.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
for n in old_f.keys() | new_f.keys():
    if n not in old_f or n not in new_f or ast.dump(old_f[n])!=ast.dump(new_f[n]):
        changed_functions.append(n)
assert set(changed_functions)=={'_bestanden','_einzelprobe','_vertrag_vorbereiten','_vertrag_pruefbar'}
for tree in (old_f['_bestanden'],new_f['_bestanden']):
    tree.body=[n for n in tree.body if not (isinstance(n,ast.If) and ast.unparse(n.test)=="name == 'vertrag'")]
assert ast.dump(old_f['_bestanden']) == ast.dump(new_f['_bestanden'])
old_tests=ast.parse((ROOT/'ausgang-repo/tests/test_eichproben.py').read_text())
new_tests=ast.parse((ROOT/'repo/tests/test_eichproben.py').read_text())
old_names={n.name for n in old_tests.body if isinstance(n,ast.FunctionDef)}
new_names={n.name for n in new_tests.body if isinstance(n,ast.FunctionDef)}
assert old_names == new_names
image = subprocess.run(['docker','image','inspect','biotop-kammer:1','--format','{{.Id}}'],capture_output=True,text=True,check=True).stdout.strip()
assert image == 'sha256:ce7bbe9441182aea532f147defd99ca757a95d4cb3ff7c3f5c5d9a64965643ee'
(OUT/'PATCHPRUEFUNG.json').write_text(json.dumps(dict(befehle=commands, angewandt_bytegleich=True,
    geaenderte_funktionen=sorted(changed_functions), andere_bestanden_zweige_ast_identisch=True,
    vorhandene_testnamen_unveraendert=True, image=image,
    produktionssha256=sha(ROOT/'repo/biotop/organe/eichproben.py')),ensure_ascii=False,indent=2))

entries=[]
for p in sorted(OUT.rglob('*')):
    if p.is_file() and p.name not in ('DATEIEN.json','PRUEFSUMMEN.sha256'):
        entries.append({'relativ':p.relative_to(OUT).as_posix(),'pfad':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
(OUT/'DATEIEN.json').write_text(json.dumps({'bestandteile_ohne_manifest_und_summen':len(entries),'dateien':entries},ensure_ascii=False,indent=2))
checks = entries + [{'relativ':'DATEIEN.json','sha256':sha(OUT/'DATEIEN.json')}]
(OUT/'PRUEFSUMMEN.sha256').write_text(''.join(f"{e['sha256']}  {e['relativ']}\n" for e in checks))
assert all(sha(OUT/e['relativ'])==e['sha256'] for e in checks)
archive=ROOT/'EICH-4-fixpaket.tar.gz'
with tarfile.open(archive,'w:gz') as tar:
    tar.add(OUT,arcname='lieferung')
with tarfile.open(archive,'r:gz') as tar:
    members=[m for m in tar.getmembers() if m.isfile()]
    for m in members:
        data=tar.extractfile(m).read()
        assert hashlib.sha256(data).hexdigest()==sha(ROOT/m.name)
archive_sha=sha(archive)
(ROOT/'EICH-4-fixpaket.tar.gz.sha256').write_text(f'{archive_sha}  {archive.name}\n')
print(json.dumps({'archiv':str(archive),'sha256':archive_sha,'dateien_im_archiv':len(members),
                  'manifest_bestandteile':len(entries),'gepruefte_summen':len(checks),
                  'patch_sha256':sha(OUT/'AENDERUNGEN.diff'),'quelle_sha256':sha(ROOT/'repo/biotop/organe/eichproben.py'),
                  'patch_bytegleich':True,'image':image},indent=2))
