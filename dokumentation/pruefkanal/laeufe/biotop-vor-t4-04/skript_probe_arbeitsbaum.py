"""Probe vor dem Nachtrag-Commit: EIN Nachspiel (K2904) am Arbeitsbaum nach der Behebung in nachspiel.py — erreicht
es ein Urteil? (Die Nachspiele D1–D3 am Commit 1d9a5aa brachen alle mit AttributeError ab.) Beleg in
nachspiel/probe-arbeitsbaum/. Kein Modellaufruf."""
import os
import subprocess
import sys

A = '/root/biotop-vor-t4-04'
os.makedirs(f'{A}/nachspiel/probe-arbeitsbaum', exist_ok=True)
r = subprocess.run([sys.executable, f'{A}/nachspiel/nachspiel_vor_t4_04.py', 's2_k2904'],
                   env={**os.environ, 'NACHSPIEL_AUS': f'{A}/nachspiel/probe-arbeitsbaum', 'BIOTOP_KAMMER_IMAGE': 'biotop-kammer:ts1'},
                   capture_output=True, text=True, timeout=1200)
print('rc', r.returncode)
print(r.stdout[-3000:])
print(r.stderr[-1500:])
