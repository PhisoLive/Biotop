#!/usr/bin/env python3
"""Exportiert bestehende Git-Blobs bytegenau in den Lieferordner.
Kein Checkout, kein Import, kein Produkt-Schreibzugriff.
"""
import json,pathlib,subprocess
O=pathlib.Path(__file__).resolve().parent
first=O/'VERIFIKATION-ERSTVERSUCH.json'
if not first.exists() and (O/'VERIFIKATION.json').exists():
 first.write_bytes((O/'VERIFIKATION.json').read_bytes())
rows=[]
for p in sorted((O/'quellen').rglob('*.py')):
 r=p.relative_to(O/'quellen');ref=r.parts[0];source='/'.join(r.parts[1:])
 blob=subprocess.run(['git','--no-optional-locks','-C','/root/biotop','show',ref+':'+source],check=True,capture_output=True).stdout
 old=p.read_bytes()
 rows.append({'datei':str(r),'bytes_aus_terminal_text':len(old),'original_bytes':len(blob),'ursache_final_newline_im_textkanal_entfernt':old==blob.rstrip(b'\n'),'vorher_bytegleich':old==blob})
 p.write_bytes(blob)
(O/'quellenexport-korrektur.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'originalquellen_bytegenau_exportiert':len(rows),'nur_lieferordner':True},ensure_ascii=False))
