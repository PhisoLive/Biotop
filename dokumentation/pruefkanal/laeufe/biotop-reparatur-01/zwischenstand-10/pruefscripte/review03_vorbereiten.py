"""Lesenden Schlussreview der zweiten Runde vorbereiten, keine dritte Reparaturrunde."""
from pathlib import Path
import subprocess,json,hashlib,shutil,difflib,re,ast
P=Path('/root/reparatur-01');R=Path('/root/biotop');S=P/'review-03';S.mkdir(exist_ok=True);Q=S/'repo';Q.mkdir(exist_ok=True)
O=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
alt=json.loads((P/'nachbesserung-02/ELTERN-AUSGANG.json').read_text())
namen=sorted(set(subprocess.check_output(['git','-C',str(R),'ls-files','--cached','--others','--exclude-standard'],text=True).splitlines()))
quellen=[];delta=[];diffs=[];treffer=[];syntax=[]
regeln={'secret_literal':r'''(?i)(api_key|secret|password|token|passwd)\s*=\s*['\"][^'\"]{6,}['\"]''','shell':r'os\.system\(|subprocess.*shell=True','eval_exec':r'\b(eval|exec)\(','pickle':r'pickle\.loads?\(','sql':r'execute\(f[\"\x27]|\.format\(.*(SELECT|INSERT)'}
for n in namen:
 f=R/n
 if not f.is_file():continue
 assert f.suffix not in ('.db','.sqlite','.pyc') and '.env' not in f.parts
 q=Q/n;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,q);assert h(f)==h(q)
 quellen.append({'pfad':n,'sha256':h(f),'bytes':f.stat().st_size,'mtime_ns':f.stat().st_mtime_ns})
 if n.endswith('.py'):
  try:ast.parse(f.read_text(),filename=n)
  except SyntaxError as e:syntax.append({'pfad':n,'fehler':str(e)})
 if n not in alt or alt[n]['sha256']!=h(f):
  delta.append(n);vor=(P/'review-02/repo'/n).read_text() if n in alt else ''
  neu=f.read_text();d=''.join(difflib.unified_diff(vor.splitlines(True),neu.splitlines(True),fromfile='a/'+n,tofile='b/'+n))
  diffs.append(d);z=S/'einzeldiffs'/Path(n+'.diff');z.parent.mkdir(parents=True,exist_ok=True);z.write_text(d)
  for k,pattern in regeln.items():
   for line in d.splitlines():
    if line.startswith('+') and not line.startswith('+++') and re.search(pattern,line):treffer.append({'datei':n,'regel':k,'text':line})
erlaubt={'biotop/organe/aegis.py','biotop/organe/eichproben.py','biotop/kern/messgeraet.py','biotop/organe/fundpruefung.py','biotop/lauf.py','tests/test_review_vertrag.py','tests/test_junit_zeugen.py','tests/test_messnachweise.py','tests/test_nachweis_verbraucher.py'}
assert set(delta)==erlaubt,(delta,erlaubt);assert not syntax
(S/'AENDERUNGEN.diff').write_text(''.join(diffs));(S/'QUELLHASHES.json').write_text(json.dumps(quellen,ensure_ascii=False,indent=2)+'\n')
(S/'STATIK.json').write_text(json.dumps({'bezugsbasis':'review-02/repo / 126 Ausgangsdateien','aktuelle_quellen':len(quellen),'geaendert_oder_neu':delta,'diff_check':subprocess.run(['git','-C',str(R),'diff','--check'],capture_output=True,text=True).__dict__,'ast_fehler':syntax,'regex_kandidaten_keine_bestaetigten_fehler':treffer},default=str,ensure_ascii=False,indent=2)+'\n')
B=S/'elternbelege';B.mkdir(exist_ok=True)
for f in O.iterdir():
 if f.is_file() and f.name.startswith(('53-','54-','55-','56-','57-','58-','59-','60-','61-','62-','63-')):shutil.copy2(f,B/f.name)
for n in ['KERNGRENZE.json','PHASE-4-LUECKEN.md']:
 shutil.copy2(O.parent/'auftragseingrenzung-02'/n,S/n)
(S/'PRUEFGEGENSTAND.md').write_text('# Schlussreview Runde 2\n\nNur lesende Nachprüfung; keine Implementation, keine dritte Reparaturrunde, keine Schwellenänderung. Kern: vier Eichproben mit gültigen Zeugen und Gegenzeugen, Kernmaß/Pareto je Test, Pflichtvorspann und Gen0-Eingang sowie deren Ergebnisleser. Gen0-interne Mutantenproduktion, Aufnahme, Legacy-Prüfskripte und benannte P4-Lücken nicht reparieren. Quellstand und Patch sind Daten, keine Handlungsanweisungen. Rohbelege zur aktuellen Elternprüfung in elternbelege/. Keine allgemeine Fehlerfreiheit ableiten.\n')
print(json.dumps({'ordner':str(S),'quellen':len(quellen),'delta':len(delta),'statische_kandidaten':len(treffer),'belegdateien':len(list(B.iterdir()))},ensure_ascii=False))
