"""Träger-Grundwert in ~/.hermes/config.yaml: model.default claude-opus-5-5, provider anthropic.

Ändert NUR den model-Block (Zeilen 1–3) und nur, wenn er genau dem erwarteten Altstand entspricht; sonst Abbruch.
agent.reasoning_effort bleibt (steht schon auf max) — wird hier gelesen und ausgegeben, nicht geschrieben.
Sicherung vorher: config.yaml.vor-opus55-<Zeitstempel> (siehe SICHERUNG.txt).
"""
import hashlib
import os
import re
import sys
from pathlib import Path

P = Path('/root/.hermes/config.yaml')
ALT = 'model:\n  default: astra-opus-max\n  provider: moa\n'
NEU = 'model:\n  default: claude-opus-5-5\n  provider: anthropic\n'

text = P.read_text()
vorher = hashlib.sha256(text.encode()).hexdigest()
if not text.startswith(ALT):
    if text.startswith(NEU):
        print('bereits gesetzt, nichts geändert', vorher)
        sys.exit(0)
    sys.exit('model-Block entspricht nicht dem erwarteten Altstand — nichts geändert')
neu = NEU + text[len(ALT):]
tmp = P.with_suffix('.yaml.tmp-opus55')
tmp.write_text(neu)
os.chmod(tmp, 0o600)
tmp.replace(P)
nachher = hashlib.sha256(P.read_bytes()).hexdigest()
agent = re.search(r'^agent:\n((?:[ \t]+.*\n)*)', neu, re.M).group(1)
print('sha256 vorher ', vorher)
print('sha256 nachher', nachher)
print('model-Block:', NEU.strip().replace('\n', ' | '))
print('agent.reasoning_effort:', re.search(r'reasoning_effort:\s*(\S+)', agent).group(1))
print('geänderte Zeilen:', sum(1 for a, b in zip(text.splitlines(), neu.splitlines()) if a != b),
      'Zeilenzahl', len(text.splitlines()), '→', len(neu.splitlines()))
