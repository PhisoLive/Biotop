"""Read-only provenance, reconciled LOC and actual result accounting."""
import ast
from collections import Counter
import hashlib
import io
import json
from pathlib import Path
import re
import tokenize
import xml.etree.ElementTree as ET

out = Path(__file__).resolve().parent
src = Path('/root/reparatur-01/review-01/repo')
review = src.parent
before = json.loads((out/'repo-vorher.json').read_text())
files = sorted(p for p in src.rglob('*') if p.is_file())
after = {p.relative_to(src).as_posix(): {'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                                      'bytes':p.stat().st_size, 'mtime_ns':p.stat().st_mtime_ns,
                                      'lines':len(p.read_bytes().splitlines())} for p in files}
(out/'repo-nachher.json').write_text(json.dumps(after, indent=2))
changes = {k:{'before':before.get(k), 'after':after.get(k)} for k in sorted(set(before)|set(after)) if before.get(k)!=after.get(k)}

def code_lines(path):
    text = path.read_text()
    all_lines = text.splitlines()
    if path.suffix != '.py':
        return None
    root = ast.parse(text)
    docs = set()
    for node in ast.walk(root):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.body:
            first = node.body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
                docs.update(range(first.lineno, first.end_lineno+1))
    lines = set()
    for token in tokenize.generate_tokens(io.StringIO(text).readline):
        if token.type in (tokenize.ENDMARKER, tokenize.ENCODING, tokenize.INDENT,
                          tokenize.DEDENT, tokenize.NEWLINE, tokenize.NL, tokenize.COMMENT):
            continue
        lines.update(i for i in range(token.start[0], token.end[0]+1) if i not in docs and all_lines[i-1].strip())
    return len(lines)

inventory = []
for p in files:
    rel = p.relative_to(src).as_posix()
    inventory.append({'path':rel, 'physical_lines':after[rel]['lines'],
                      'nonblank_lines':sum(bool(s.strip()) for s in p.read_text().splitlines()),
                      'python_code_lines_token_method':code_lines(p),
                      'bytes':after[rel]['bytes'], 'sha256':after[rel]['sha256']})
diff = (review/'AENDERUNGEN.diff').read_text()
file_stats = {}
current = None
old_line = new_line = None
for number, line in enumerate(diff.splitlines(), 1):
    if line.startswith('diff --git '):
        current = None
    elif line.startswith('+++ b/'):
        current = line[len('+++ b/'):]
        file_stats[current] = {'path':current, 'added':0, 'deleted':0,
                               'hunks':[], 'added_line_numbers':[], 'diff_header_line':number}
    elif line.startswith('@@') and current:
        m = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', line)
        assert m, line
        old_line, new_line = int(m[1]), int(m[3])
        file_stats[current]['hunks'].append({'diff_line':number, 'header':line,
                                            'new_start':new_line, 'new_count':int(m[4] or 1)})
    elif current and old_line is not None:
        if line.startswith('+'):
            file_stats[current]['added'] += 1
            file_stats[current]['added_line_numbers'].append(new_line)
            new_line += 1
        elif line.startswith('-'):
            file_stats[current]['deleted'] += 1
            old_line += 1
        elif line.startswith(' '):
            old_line += 1
            new_line += 1
for rel, stat in file_stats.items():
    stat['new_physical_lines'] = after[rel]['lines']
    stat['new_bytes'] = after[rel]['bytes']
    stat['new_sha256'] = after[rel]['sha256']

results = []
for name in ('provided-unit', 'independent-review', 'supplemental'):
    root = ET.parse(out/(name+'.xml')).getroot()
    cases = list(root.iter('testcase'))
    counts = Counter('failure' if case.find('failure') is not None else 'error' if case.find('error') is not None
                     else 'skipped' if case.find('skipped') is not None else 'passed' for case in cases)
    results.append({'suite':name, 'collected_and_executed':len(cases), 'outcomes':dict(counts),
                    'cases':[{'id':case.get('classname','')+'::'+case.get('name',''),
                              'outcome':'failure' if case.find('failure') is not None else 'error' if case.find('error') is not None else 'skipped' if case.find('skipped') is not None else 'passed'} for case in cases],
                    'stdout_bytes':(out/(name+'.stdout.txt')).stat().st_size,
                    'stderr_bytes':(out/(name+'.stderr.txt')).stat().st_size})

local_runs = json.loads((out/'contract-local-pytest-raw.json').read_text())
for run in local_runs:
    m = re.search(r'@@J@@(.*)@@E@@', run['stdout'], re.S)
    xml = ET.fromstring(m[1])
    run['junit_results'] = [dict(s.attrib) for s in xml.iter('testsuite')]
    run['testcases'] = [{'name':c.get('name'), 'failure':c.find('failure').get('message') if c.find('failure') is not None else None} for c in xml.iter('testcase')]
# Store structured extracts in addition to untouched original stdout records.
(out/'contract-junit-summary.json').write_text(json.dumps(local_runs, ensure_ascii=False, indent=2))
summary = {'source_root':str(src), 'source_file_count':len(files),
           'source_unchanged_content_size_mtime':not changes, 'source_changes':changes,
           'total_physical_lines':sum(r['physical_lines'] for r in inventory),
           'total_bytes':sum(r['bytes'] for r in inventory),
           'python_files':sum(r['python_code_lines_token_method'] is not None for r in inventory),
           'python_code_lines_token_method':sum(r['python_code_lines_token_method'] or 0 for r in inventory),
           'loc_definition':'Physical: splitlines including final non-newline. Python code: union of nonblank physical rows occupied by non-comment/non-layout tokens, excluding AST docstrings; multiline non-docstring literals count as code rows. No dependency/generated-artifact exclusions were necessary in this 125-file source snapshot.',
           'diff_files':len(file_stats), 'diff_added_lines':sum(r['added'] for r in file_stats.values()),
           'diff_deleted_lines':sum(r['deleted'] for r in file_stats.values()),
           'diff_physical_lines':len(diff.splitlines()),
           'inputs':{p.name:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes':p.stat().st_size} for p in [review/'AENDERUNGEN.diff', review/'STATIK.json']},
           'test_results':results,
           'source_inventory':inventory, 'diff_inventory':list(file_stats.values()),
           'local_trusted_pytest_wrappers':len(local_runs),
           'docker_runs':0, 'network_calls':0, 'paid_model_calls':0,
           'limitations':['No actual Docker calibration or production-store replay was performed. Four-pair Docker acceptance remains with the parent.',
                          'Gate and area-lock results are UNIT evidence with explicit controlled measurement values, not runtime-performance measurements.',
                          'Contract generator witnesses are actual local pytest executions of a trusted synthetic review fixture. Predicate envelope is a declared unit input.']}
(out/'BELEGE.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2))
print(json.dumps({k:v for k,v in summary.items() if k not in ('source_inventory','diff_inventory','test_results')}, ensure_ascii=False))
print(json.dumps([{'suite':r['suite'],'cases':r['collected_and_executed'],'outcomes':r['outcomes']} for r in results]))
