#!/usr/bin/env python3
"""Erfasst lokale Belegadressen mit dem gelieferten Citation-Ledger."""
from pathlib import Path
import subprocess
import json
import hashlib
O=Path(__file__).resolve().parent
A=Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe')
S=Path('/root/.hermes/skills/research/grounded-citations/scripts/sources.py')
paths=[
 O/'nutzerentscheidungen.json', O/'laeufe.json', O/'generationen.json', O/'ereignisse-belegauswahl.json',
 O/'nachrechnung.json', O/'werkstaende.json', O/'quellstaende.json', O/'immun-schluessel.json', O/'kosten-abgrenzung.json',
 Path('/root/.hermes/cache/documents/doc_f18e4c5d9f14_ABNAHME_Vorbedingung-1_2026-09-20.md'),
 A/'biotop-phase-4-vorbedingung-1/NACHGANG-03.md',
 A/'biotop-phase-4-vorbedingung-1/ausgaben/03-vorbedingung1-messung.txt',
 A/'biotop-gesamtstand/BERICHT.md', A/'biotop-gesamtstand/pruefungen/pruefung-a/BEFUND.md',
 A/'biotop-gesamtstand/pruefungen/pruefung-b/BEFUND.md',
 Path('/root/biotop/biotop/organe/aegis.py'),Path('/root/biotop/biotop/organe/gedaechtnis.py'),
 Path('/root/biotop/pruefung/lauf25_pfadnachweis.py'),Path('/root/biotop/pruefung/nachgang_n13_n14.py'),
 O/'runner-stderr.json', O/'zustand-vorher.json', O/'abfragen.sql', O/'kasse.json',
 A/'biotop-phase-4-vorbedingung-1/NACHGANG-05.md', A/'biotop-phase-4-vorbedingung-1/NACHGANG-06.md',
 A/'biotop-phase-4-vorbedingung-1/NACHGANG-04.md',O/'protokoll_sicher.json',O/'vertiefen.py'
]
base=['python3','-B',str(S),'--ledger',str(O/'quellenledger.json')]
subprocess.run(base+['reset'],check=True,capture_output=True,text=True)
manifest=[]
for p in paths:
    result=subprocess.run(base+['add',p.as_uri(),'--title',p.name],check=True,capture_output=True,text=True)
    print(result.stdout.strip())
    manifest.append({'datei':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(O/'quellen-integritaet.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
