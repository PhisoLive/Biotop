"""Seal deliverables; omit caches, never include a database or secret store."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
excluded = {'__pycache__', '.pytest_cache', '.git'}
files = sorted(p for p in root.rglob('*') if p.is_file() and not (set(p.parts) & excluded)
               and p.name not in {'DATEIEN.txt', 'PRUEFSUMMEN.txt'})
assert not any(p.suffix in {'.db','.sqlite','.sqlite3'} for p in files)
index = root / 'DATEIEN.txt'
checks = root / 'PRUEFSUMMEN.txt'
index.write_text('\n'.join(str(p) for p in sorted(files + [index, checks])) + '\n')
items = sorted(files + [index])
checks.write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(root)}\n' for p in items))
# Verify the sealed bytes rather than claiming success just because writing succeeded.
for line in checks.read_text().splitlines():
    digest, name = line.split('  ', 1)
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
print(json.dumps({'manifest_entries':len(items), 'index_entries':len(files)+2,
                  'manifest':str(checks),'manifest_sha256':hashlib.sha256(checks.read_bytes()).hexdigest(),
                  'report':str(root/'BERICHT.md'),'report_sha256':hashlib.sha256((root/'BERICHT.md').read_bytes()).hexdigest(),
                  'diff_sha256':hashlib.sha256((root/'reparatur-acb.diff').read_bytes()).hexdigest()},indent=2))
