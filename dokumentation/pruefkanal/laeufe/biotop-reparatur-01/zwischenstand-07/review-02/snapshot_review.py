from pathlib import Path
import hashlib, json, os, shutil, sys
ROOT = Path('/root/reparatur-01/review-02')
SRC = ROOT / 'repo'
OUT = ROOT / 'pruefer-kern'
def snapshot():
    rows = []
    for p in sorted(SRC.rglob('*')):
        s = p.lstat()
        rows.append(dict(path=str(p.relative_to(SRC)), kind='symlink' if p.is_symlink() else 'dir' if p.is_dir() else 'file', size=s.st_size, mtime_ns=s.st_mtime_ns, sha256=hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() and not p.is_symlink() else None, link=os.readlink(p) if p.is_symlink() else None))
    return rows
rows = snapshot()
phase = sys.argv[1]
(OUT / f'quellzustand-{phase}.json').write_text(json.dumps(rows, indent=2) + '\n')
if phase == 'vorher':
    if any(r['kind'] == 'symlink' for r in rows):
        raise RuntimeError('Inspect symlinks before copy')
    shutil.copytree(SRC, OUT / 'arbeitskopie')
    (OUT / 'tmp').mkdir(exist_ok=True)
    print(json.dumps(dict(entries=len(rows), files=sum(r['kind']=='file' for r in rows), copied=str(OUT/'arbeitskopie'))))
else:
    before = json.loads((OUT / 'quellzustand-vorher.json').read_text())
    result = dict(unchanged=before == rows, entries=len(rows), files=sum(r['kind']=='file' for r in rows), added_removed_or_changed=[r for r in rows if r not in before] + [r for r in before if r not in rows])
    (OUT / 'quellzustand-vergleich.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    assert before == rows
