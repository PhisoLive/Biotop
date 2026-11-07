"""Validate review references and source preservation, then seal deliverables."""
import hashlib
import json
from pathlib import Path

out = Path(__file__).resolve().parent
src = Path('/root/reparatur-01/review-01/repo')
review = json.loads((out/'REVIEW.json').read_text())
proof = json.loads((out/'BELEGE.json').read_text())
before = json.loads((out/'repo-vorher.json').read_text())
actual = {p.relative_to(src).as_posix():{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                                       'bytes':p.stat().st_size,'mtime_ns':p.stat().st_mtime_ns,
                                       'lines':len(p.read_bytes().splitlines())}
          for p in sorted(src.rglob('*')) if p.is_file()}
assert before == actual, 'Source snapshot changed'
copy = out/'arbeitskopie'
for rel, record in before.items():
    assert hashlib.sha256((copy/rel).read_bytes()).hexdigest() == record['sha256'], rel
assert review['passed'] is False and review['logic_errors'] and not review['security_concerns']
assert len({e['id'] for e in review['logic_errors']}) == len(review['logic_errors'])
changes = {r['path']:r for r in proof['diff_inventory']}
refs = []
for e in review['logic_errors']:
    path = Path(e['file'])
    rel = path.relative_to(src).as_posix()
    assert e['line'] in changes[rel]['added_line_numbers'], e['id']
    assert 1 <= e['line'] <= e['end_line'] <= len(path.read_text().splitlines())
    refs.append({'id':e['id'],'primary_location_in_added_diff_lines':True})
for s in proof['test_results']:
    assert s['collected_and_executed'] == sum(s['outcomes'].values())
    assert not s['outcomes'].get('error')
    assert s['stderr_bytes'] == 0
    assert '[truncated]' not in (out/(s['suite']+'.stdout.txt')).read_text()
own = [c for r in proof['test_results'] if r['suite'] != 'provided-unit' for c in r['cases']]
assert len(own) == len({r['id'] for r in own})
assert sum(r['outcome']=='failure' for r in own) == len(review['logic_errors'])
validation = {'valid_json':True, 'fail_closed_consistent':True, 'findings_in_added_diff_lines':refs,
              'source_files_unchanged_sha256_size_mtime':len(before),
              'execution_copy_files_identical_to_snapshot':len(before),
              'independent_unique_test_cases':len(own),
              'independent_failures':sum(r['outcome']=='failure' for r in own),
              'independent_passes':sum(r['outcome']=='passed' for r in own),
              'all_reported_outputs_preserved_without_truncation':True,
              'output_stderr_empty_for_each_recorded_pytest_command':True,
              'no_repository_implementation':True}
(out/'VERIFIKATION.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2))
files = sorted(p for p in out.rglob('*') if p.is_file()
               and p.relative_to(out).parts[0] != 'tmp'
               and '__pycache__' not in p.parts
               and p.name not in ('DATEIEN.txt','SHA256SUMS.txt'))
listing = [p.relative_to(out).as_posix() for p in files] + ['DATEIEN.txt','SHA256SUMS.txt']
(out/'DATEIEN.txt').write_text('\n'.join(sorted(listing))+'\n')
files.append(out/'DATEIEN.txt')
lines = [hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(out).as_posix() for p in sorted(files)]
(out/'SHA256SUMS.txt').write_text('\n'.join(lines)+'\n')
# Read back every target checksum; the manifest does not hash itself.
for line in lines:
    digest, rel = line.split('  ',1)
    assert hashlib.sha256((out/rel).read_bytes()).hexdigest() == digest
print(json.dumps({'review':str(out/'REVIEW.json'),
                  'review_sha256':hashlib.sha256((out/'REVIEW.json').read_bytes()).hexdigest(),
                  'manifest':str(out/'SHA256SUMS.txt'),
                  'manifest_sha256':hashlib.sha256((out/'SHA256SUMS.txt').read_bytes()).hexdigest(),
                  'files_covered_by_manifest':len(files), 'validation':validation},ensure_ascii=False))
