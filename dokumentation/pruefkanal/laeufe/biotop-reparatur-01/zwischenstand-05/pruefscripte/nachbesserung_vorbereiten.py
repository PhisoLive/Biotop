"""Isolierte Nachbesserungen, erster Review-Fix-Zyklus, keine Bestandswrites."""
from pathlib import Path
import subprocess,shutil,hashlib,json
R=Path('/root/biotop');O=Path('/root/reparatur-01/nachbesserung-01');O.mkdir(exist_ok=False)
files=sorted(set(p for p in subprocess.check_output(['git','-C',str(R),'ls-files','--cached','--others','--exclude-standard','-z']).decode().split('\0') if p))
assert not any(p.startswith('daten/') or Path(p).name.startswith('.env') for p in files)
manifest={}
for name in files:
 p=R/name;manifest[name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size':p.stat().st_size,'mtime_ns':p.stat().st_mtime_ns}
 for teil in ['vorstufen','wirkungskreis','vertrag']:
  z=O/teil/'repo'/name;z.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,z)
(O/'ELTERN-AUSGANG.json').write_text(json.dumps(manifest,indent=2)+'\n')
berichte=[json.loads(Path(p).read_text()) for p in ['/root/reparatur-01/review-01/pruefer-eichung/REVIEW.json','/root/reparatur-01/review-01/pruefer-mass/ERGEBNIS.json']]
fehler=[e['id'] for d in berichte for e in d['logic_errors']]
zuordnung={'EICH-1':'tatsaechlicher_wirkungskreis','MASS-01':'tatsaechlicher_wirkungskreis','EICH-2':'gen0_erfolg','EICH-3':'eichgegenstand_bindung','EICH-4':'vertrag_zeugengueltigkeit','MASS-02':'rauschfehler_bereichsweise'}
assert set(fehler)==set(zuordnung)
(O/'BEFUNDE.json').write_text(json.dumps({'review_fix_zyklus':1,'review_befunde':fehler,'gemeinsame_mechanismen':len(set(zuordnung.values())),'zuordnung':zuordnung,'abnahme':'offen, keine Messfreigabe'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'quell_dateien':len(files),'befunde':len(fehler),'mechanismen':len(set(zuordnung.values())),'teile':['vorstufen','wirkungskreis','vertrag']},ensure_ascii=False))
