"""Artefaktindex und SHA-Manifest der fertigen Eigentümerlieferung."""
from pathlib import Path
import hashlib
import json
import subprocess

out = Path(__file__).resolve().parent
excluded = {'DATEIEN.txt', 'SHA256SUMS', 'MANIFEST.sha256'}
files = sorted(p.relative_to(out).as_posix() for p in out.rglob('*')
               if p.is_file() and p.relative_to(out).as_posix() not in excluded)
index = sorted([*files, *excluded])
assert len(index) == len(set(index))
(out / 'DATEIEN.txt').write_text('\n'.join(index) + '\n')
covered = sorted([*files, 'DATEIEN.txt'])
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
(out / 'SHA256SUMS').write_text(''.join(f'{sha(out / p)}  {p}\n' for p in covered))
manifest_sha = sha(out / 'SHA256SUMS')
(out / 'MANIFEST.sha256').write_text(f'{manifest_sha}  SHA256SUMS\n')
for command in (['sha256sum', '--quiet', '-c', 'SHA256SUMS'], ['sha256sum', '-c', 'MANIFEST.sha256']):
    result = subprocess.run(command, cwd=out, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr + result.stdout
    print(json.dumps(dict(command=command, rc=result.returncode, stdout=result.stdout,
                          stderr=result.stderr), ensure_ascii=False))
actual = sorted(p.relative_to(out).as_posix() for p in out.rglob('*') if p.is_file())
assert actual == index
print(json.dumps(dict(delivery=str(out), artifact_files=len(actual),
                      sha256_covered_files=len(covered), manifest_sha256=manifest_sha,
                      changed_files=json.loads((out / 'DATEIMANIFEST.json').read_text())),
                 ensure_ascii=False, indent=2))
