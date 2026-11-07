"""EICH-4 validity repro, not a real Docker/Mass campaign.
Original builder, original JUnit parser and original predicate; only Kammer I/O
is replaced by local pytest on a reviewer-owned synthetic fixture. The generated
runpy contract MUST be skipped before its body: no runpy/run_path is executed.
The local fixture deliberately has an invalid (skipped) named witness. This
must be rejected, not counted as a valid negative control.
"""
from pathlib import Path
import json, os, shutil, subprocess, sys, time, xml.etree.ElementTree as ET
from unittest.mock import patch
from biotop.organe import aegis, eichproben, verfassung, vertraege, vorspann
from biotop.kern import datenbank, messgeraet
from copy import deepcopy
from biotop.organe.kammer import Ergebnis
ROOT = Path(__file__).resolve().parent
assert Path(eichproben.__file__).resolve().is_relative_to(ROOT / 'arbeitskopie')
OUT = ROOT / 'repro-skip'
if OUT.exists():
    index = 2
    while (ROOT / f'repro-skip-{index}').exists():
        index += 1
    OUT = ROOT / f'repro-skip-{index}'
OUT.mkdir()
werk = OUT / 'eigenes-werk'
VERTRAG = 'tests/vertraege/test_vertrag_abnehmer_lieferant.py'
NAME = 'test_eichprobe_vertrag_neue_zusicherung'
files = {
    'beispiel/__init__.py': '',
    'beispiel/abnehmer/__init__.py': 'from .quelle import bericht\n',
    'beispiel/abnehmer/quelle.py': 'def bericht(zahl: float):\n    ergebnis = zahl + 1\n    return ergebnis\n',
    'beispiel/lieferant/__init__.py': 'from .quelle import wert\n',
    'beispiel/lieferant/quelle.py': 'def wert(zahl: float):\n    ergebnis = zahl * 2\n    return ergebnis\n',
    'tests/test_abnehmer.py': 'from beispiel.abnehmer import bericht\nEINGABE = 2\ndef test_bericht():\n    assert bericht(EINGABE) == 3\n',
    VERTRAG: 'from beispiel.lieferant import wert\ndef test_alt():\n    assert wert(2) == 4\n',
    'tests/conftest.py': ('import pytest, runpy\n'
        'def forbidden(*a, **kw):\n    raise AssertionError("runpy not allowed in local reviewer fixture")\n'
        'runpy.run_path = forbidden\n'
        'def pytest_runtest_setup(item):\n'
        f'    if item.name == {NAME!r}:\n'
        '        pytest.skip("reviewer: unavailable contract fixture")\n')
}
for rel, text in files.items():
    p=werk/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text)
rows=[]
def local_junit(werk, befehl, zeitlimit_s=None, dateien=None):
    assert befehl[:2] == ['python','_messgeraet/lauf.py'], befehl
    case = OUT / f'call-{len(rows)+1}'
    shutil.copytree(werk, case)
    for rel, text in (dateien or {}).items():
        p=case/rel; assert p.resolve().is_relative_to(case.resolve())
        p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text)
    xmlpath = case / 'junit.xml'
    env=dict(os.environ, PYTHONPATH=os.pathsep.join([str(ROOT/'guard'),str(case),str(ROOT/'arbeitskopie')]),
             PYTHONDONTWRITEBYTECODE='1', PYTEST_DISABLE_PLUGIN_AUTOLOAD='1', TMPDIR=str(ROOT/'tmp'))
    cmd=[sys.executable,'-m','pytest','-q','-p','no:cacheprovider','--tb=short',f'--junitxml={xmlpath}',*befehl[2:]]
    start=time.monotonic(); r=subprocess.run(cmd, cwd=case,env=env,capture_output=True,text=True,timeout=30)
    (case/'stdout.txt').write_text(r.stdout); (case/'stderr.txt').write_text(r.stderr)
    xmltext=xmlpath.read_text(); tree=ET.fromstring(xmltext)
    witnesses=[dict(classname=tc.get('classname'),name=tc.get('name'),
                    skipped=tc.find('skipped') is not None, failure=tc.find('failure') is not None,
                    error=tc.find('error') is not None) for tc in tree.iter('testcase')]
    rows.append(dict(command=cmd, cwd=str(case),rc=r.returncode, witnesses=witnesses))
    return Ergebnis(r.returncode, r.stdout+'@@J@@'+xmltext+'@@E@@',r.stderr,time.monotonic()-start,False,'LOCAL-REVIEW-NOT-DOCKER')
with patch.object(aegis.kammer,'ausfuehren',local_junit):
    diff, _, belege, _ = eichproben._vertrag_vorbereiten(werk,'beispiel','abnehmer','lieferant',VERTRAG,True)
# Propagation check at the original row producer. The Mass boundary is an
# explicit, valid-shaped UNIT input, not a measured performance observation.
unit_mass=dict(gueltig=True,bereiche={b:dict(tests_bestanden=1,tests_fehlgeschlagen=0,
    sicherheit_punkte=0,tote_funktionen=0,groesste_funktion=6,laufzeit_ms=None) for b in ('abnehmer','lieferant')},
    werk=dict(baut=True,zyklen=0,bauzeit_ms=1,tests_fehlgeschlagen_liste=[]))
con=datenbank.verbinden(OUT/'unit.db')
con.executescript(verfassung.SCHEMA)
con.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status,mass) VALUES(1,1,0,'angelegt',NULL)")
vertraege.einlegen(con,1,werk,{('abnehmer','lieferant'):(werk/VERTRAG).read_text()},'review-only')
with patch.object(aegis.kammer,'_ausfuehren',local_junit), patch.object(messgeraet,'messen',lambda *a,**kw:deepcopy(unit_mass)):
    unit_row=eichproben._einzelprobe(con,1,1,werk,'beispiel',['abnehmer','lieferant'],[],
        unit_mass,unit_mass,None,{},0,dict(von_bereich='abnehmer',nach_bereich='lieferant',vertrag_pfad=VERTRAG),'vertrag',True)
con.close()
recorded=json.loads((ROOT/'elternbelege'/'48-gesamtsuite-kernabschluss-eichpaare.json').read_text())
recorded['gegenproben']['vertrag']=unit_row
consumer_replay=dict(boundary='Consumer UNIT replay: seven supplied recorded rows plus this local counter-row; NOT a fresh eight-probe run',
                    battery_complete=eichproben._vollstaendig(recorded['proben'],recorded['gegenproben']),
                    quality=vorspann._qualitaet(recorded))
target=VERTRAG+'::'+NAME
result=dict(boundary='Local pytest only at Kammer I/O; no models, no Docker, no real Mass campaign; original builder/parser/predicate',
            unit_mass_boundary=unit_mass,original_einzelprobe_unit_row=unit_row,consumer_unit_replay=consumer_replay,
            source=str(eichproben.__file__), runs=rows, belege=belege, diff=diff,
            target=target, raw_target_skipped=next(x['skipped'] for x in rows[-1]['witnesses'] if x['name']==NAME),
            parsed_target=belege['kandidat_tests'][target],
            accepted_as_valid_countercase=eichproben._vertrag_pruefbar(belege,True))
(OUT/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
assert result['raw_target_skipped'] is True
assert result['accepted_as_valid_countercase'] is False, 'Skipped named contract is incorrectly accepted as executed/passing negative control'
