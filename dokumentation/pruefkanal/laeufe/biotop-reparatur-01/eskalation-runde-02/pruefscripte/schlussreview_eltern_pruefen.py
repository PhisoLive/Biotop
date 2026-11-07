"""Schlussreview read-only nachprüfen; nur Ausgabepfad des synthetischen Repros umlenken."""
from pathlib import Path
import hashlib,json,subprocess,datetime,difflib
P=Path('/root/reparatur-01');S=P/'review-03';D=S/'pruefer';W=P/'schlussreview-eltern';W.mkdir(mode=0o700,exist_ok=False)
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def lade(f):return json.loads(f.read_text())
def schreibe(n,z):(W/n).write_text(json.dumps(z,ensure_ascii=False,indent=2)+'\n')
manifest=lade(S/'QUELLHASHES.json')
assert sha(D/'SHA256SUMS')=='0398ba175bcc6d3f89a3088885b9120675770ae49c6de3a1f8e0530403240f6b'
liefer=[]
for line in (D/'SHA256SUMS').read_text().splitlines():
 h,f=line.split(None,1);f=f.strip().removeprefix('*');assert (D/f).resolve().is_relative_to(D.resolve()) and sha(D/f)==h;liefer.append({'datei':f,'sha256':h})
assert len(liefer)==8
vor=[dict(pfad=z['pfad'],sha256=sha(S/'repo'/z['pfad']),bytes=(S/'repo'/z['pfad']).stat().st_size,mtime_ns=(S/'repo'/z['pfad']).stat().st_mtime_ns) for z in manifest]
assert vor==manifest
aktuell={z['pfad']:sha(Path('/root/biotop')/z['pfad']) for z in manifest};assert all(aktuell[z['pfad']]==z['sha256'] for z in manifest)
schreibe('QUELLEN-VORHER.json',{'quellen':vor,'zeit':datetime.datetime.now(datetime.timezone.utc).isoformat()})
original=(D/'PRUEFUNG.py').read_text();alt="OUT = ROOT / 'pruefer'";neu="OUT = Path('/root/reparatur-01/schlussreview-eltern')";assert original.count(alt)==1
angepasst=original.replace(alt,neu);(W/'PRUEFUNG.py').write_text(angepasst);(W/'AUSGABEPFAD.diff').write_text(''.join(difflib.unified_diff(original.splitlines(True),angepasst.splitlines(True),fromfile='pruefer/PRUEFUNG.py',tofile='schlussreview-eltern/PRUEFUNG.py')))
cmd=['python3','-B',str(W/'PRUEFUNG.py')];r=subprocess.run(cmd,capture_output=True,text=True,timeout=40)
(W/'stdout.txt').write_text(r.stdout);(W/'stderr.txt').write_text(r.stderr);assert r.returncode==0,(r.returncode,r.stderr)
unit=lade(W/'UNIT-GRENZE.json');assert unit==lade(D/'UNIT-GRENZE.json');assert lade(W/'BELEGABGLEICH.json')==lade(D/'BELEGABGLEICH.json')
assert unit['tatsaechliches_urteil']['ok'] is True and unit['kontrolle_mit_eindeutigen_ids']['ok'] is False
assert unit['fund_fehlattribution']['absturz_im_werk'] is True and unit['fund_fehlattribution']['erwartet_absturz_im_werk'] is False
assert not lade(W/'QUELLEN-NACHHER.json')['vorher_nachher_abweichungen']
assert aktuell=={z['pfad']:sha(Path('/root/biotop')/z['pfad']) for z in manifest}
for z in liefer:assert sha(D/z['datei'])==z['sha256']
result={'befehl':cmd,'rc':r.returncode,'grenze':'Nur vorhandene Rohdaten nachgezählt und originaler AST mit explizit synthetischem XML/I-O ausgeführt; keine neuen pytest-/Werk-/Kammer-/DB-/Modellläufe. Kein Produktfix.','pruefer_manifest':sha(D/'SHA256SUMS'),'pruefer_manifest_eintraege':len(liefer),'quelle_anzahl':len(manifest),'quellhashes_groessen_mtime_unveraendert':True,'produktdateihashes_unveraendert':True,'eigenes_unit_ergebnis_identisch_mit_review':True,'eigener_belegabgleich_identisch_mit_review':True,'pareto_falsch_freigegeben':unit['tatsaechliches_urteil']['ok'],'kontrolle_mit_eindeutigen_ids_freigegeben':unit['kontrolle_mit_eindeutigen_ids']['ok'],'testeigener_nameerror_falsch_werkabsturz':unit['fund_fehlattribution']['absturz_im_werk'],'eigene_dockerkammern':0,'eigene_biotop_modellaufrufe':0}
schreibe('ELTERNPRUEFUNG.json',result)
files=sorted(f for f in W.iterdir() if f.is_file());(W/'SHA256SUMS').write_text(''.join(sha(f)+'  '+f.name+'\n' for f in files))
print(json.dumps(result,ensure_ascii=False,indent=2))
