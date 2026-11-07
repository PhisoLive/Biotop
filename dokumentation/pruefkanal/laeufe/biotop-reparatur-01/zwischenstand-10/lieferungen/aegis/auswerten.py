"""Belege dieser Eigentümerlieferung zählen, Quellen vergleichen und Diff prüfen."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import shutil
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
REPO, OUT = ROOT / 'repo', ROOT / 'lieferung'

def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


baseline = json.loads((ROOT / 'ELTERN-AUSGANG.json').read_text())
allowed = set(json.loads((ROOT / 'GRENZE.json').read_text())['erlaubt'])
state = {p.relative_to(REPO).as_posix(): dict(sha256=sha(p), size=p.stat().st_size,
                                           mtime_ns=p.stat().st_mtime_ns)
         for p in sorted(REPO.rglob('*')) if p.is_file()}
changed = sorted(p for p in baseline if state.get(p) != baseline[p])
added = sorted(set(state) - set(baseline))
missing = sorted(set(baseline) - set(state))
assert not missing and set(changed + added) <= allowed
integrity = dict(checked_at=datetime.now(timezone.utc).isoformat(),
                 basis='ELTERN-AUSGANG.json: SHA256, Größe, mtime_ns und Pfadbestand',
                 baseline_files=len(baseline), final_files=len(state), changed=changed, added=added,
                 missing=missing, unchanged_count=len(baseline) - len(changed),
                 outside_allowlist_changed=[], unchanged=[p for p in baseline if p not in changed])
dump(OUT / 'QUELLEN-VERGLEICH.json', integrity)
manifest, diff = [], []
for name in sorted(changed + added):
    target = OUT / 'dateien' / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO / name, target)
    old = OUT / 'vorher' / name
    if name in baseline:
        assert sha(old) == baseline[name]['sha256']
    before = old.read_text().splitlines(keepends=True) if old.exists() else []
    after = target.read_text().splitlines(keepends=True)
    delta = list(difflib.unified_diff(before, after, fromfile='a/' + name if before else '/dev/null',
                                    tofile='b/' + name))
    diff += ['diff --git a/' + name + ' b/' + name + '\n']
    if name in added:
        diff.append('new file mode 100644\n')
    diff += delta
    manifest.append(dict(path=name, status='geändert' if name in baseline else 'neu',
                         before_sha256=baseline.get(name, {}).get('sha256'), sha256=sha(target),
                         size=target.stat().st_size, lines=len(after),
                         inserted=sum(l.startswith('+') and not l.startswith('+++') for l in delta),
                         deleted=sum(l.startswith('-') and not l.startswith('---') for l in delta)))
(OUT / 'AENDERUNGEN.diff').write_text(''.join(diff))
dump(OUT / 'DATEIMANIFEST.json', manifest)
checkdir = OUT / 'patchpruefung'
if checkdir.exists():
    shutil.rmtree(checkdir)
for name in changed:
    target = checkdir / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(OUT / 'vorher' / name, target)
check = subprocess.run(['git', 'apply', '--check', str(OUT / 'AENDERUNGEN.diff')],
                       cwd=checkdir, capture_output=True, text=True)
dump(OUT / 'DIFF-PRUEFUNG.json', dict(command=check.args, cwd=str(checkdir), rc=check.returncode,
                                    stdout=check.stdout, stderr=check.stderr))
assert check.returncode == 0
shutil.rmtree(checkdir)

runs, containers, timeout_containers, all_rows = [], [], [], []
for path in sorted((OUT / 'laeufe').iterdir()):
    meta = json.loads((path / 'execution.json').read_text())
    calls = json.loads((path / 'kammer.json').read_text())
    tcs = list(ET.parse(path / 'junit.xml').getroot().iter('testcase'))
    counts = dict(tests=len(tcs), failures=sum(t.find('failure') is not None for t in tcs),
                  errors=sum(t.find('error') is not None for t in tcs),
                  skipped=sum(t.find('skipped') is not None for t in tcs))
    counts['passed'] = counts['tests'] - counts['failures'] - counts['errors'] - counts['skipped']
    ids = [c['container'] for c in calls]
    assert len(calls) == meta['kammerlaeufe'] == meta['unique_containers'] == len(set(ids))
    assert not meta['blocked_attempts']
    containers.extend(ids)
    timeout_containers.extend(c['container'] for c in calls if c['zeitlimit'])
    rows = [(str(p.relative_to(OUT)), json.loads(p.read_text()))
            for p in sorted((path / 'vertragszeilen').glob('*.json'))]
    all_rows.extend(rows)
    runs.append(dict(run=path.name, exit_code=meta['exit_code'], **counts,
                     chambers=len(calls), timeout_chambers=sum(c['zeitlimit'] for c in calls),
                     duration_s=meta['duration_s'], start=meta['started'], finish=meta['finished']))
assert len(containers) == len(set(containers))
current = subprocess.run(['docker', 'ps', '-a', '--format', '{{.Names}}'],
                         capture_output=True, text=True, check=True)
left = sorted(set(containers) & set(current.stdout.splitlines()))
assert not left
costs = dict(budget_gesamt_eur=5, biotop_modellaufrufe_erlaubt=0,
             biotop_modellaufrufe=sum(row['modellaufrufe'] for _, row in all_rows),
             biotop_kosten_eur=sum(row['kosten_eur'] for _, row in all_rows),
             abgerechnete_privat_db_zeilen=len(all_rows),
             docker_kammerlaeufe=len(containers), unique_containers=len(set(containers)),
             timeout_kammerlaeufe=len(timeout_containers),
             verbleibende_eigene_container=left, containerkontrolle=current.args,
             sonstiges_docker='Vorab eine Image-Inspektion; Docker-kill/rm bei Timeout sind keine neuen Kammerläufe.',
             summe_prueflauf_wandzeit_s=sum(r['duration_s'] for r in runs),
             externe_bezahlte_biotop_oder_netzaufrufe=0,
             traegerkosten_eur=None, cpu_hostkosten_eur=None,
             gesamtbudget_einhaltung_messbar=False,
             grenze='Biotop-Verbrauch aus privaten Zeilen; Anbieterzugriff/Netz im Prüfprozess gesperrt. '
                    'Träger- und Hostkosten nicht monetär erfasst, deshalb kein gemessenes Gesamt-0 und '
                    'keine numerische Bestätigung der 5-EUR-Gesamtkostengrenze.')
assert costs['biotop_modellaufrufe'] == costs['biotop_kosten_eur'] == 0
summary = dict(runs=runs, final_run=runs[-1], source_changes=manifest,
               unchanged_source_files=integrity['unchanged_count'], costs=costs)
dump(OUT / 'AUSWERTUNG.json', summary)
dump(OUT / 'KOSTEN.json', costs)
print(json.dumps(summary, ensure_ascii=False, indent=2))
