"""Gleichen Skip-Repro gegen Elterncode ausführen, Rohdaten unveränderlich sichern."""
from pathlib import Path
import os, sys, subprocess, json, hashlib, time
P = Path('/root/reparatur-01')
E = P / 'eltern-skip-repro'
O = Path('/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-reparatur-01/ausgaben')
name = sys.argv[1]
assert '/' not in name
for s in ('.json', '.stdout.txt', '.stderr.txt'):
    assert not (O / (name+s)).exists()
env = dict(os.environ, PYTHONPATH=str(E/'guard')+':/root/biotop', PYTHONDONTWRITEBYTECODE='1', PYTEST_DISABLE_PLUGIN_AUTOLOAD='1', TMPDIR=str(E/'tmp'), BIOTOP_DB=str(E/'tmp/unused.db'))
cmd = ['/root/reparatur-01/venv/bin/python', str(E/'repro_skip_vertragszeuge.py')]
t0 = time.monotonic()
r = subprocess.run(cmd, cwd=E, env=env, text=True, capture_output=True, timeout=120)
(O / (name+'.stdout.txt')).write_text(r.stdout)
(O / (name+'.stderr.txt')).write_text(r.stderr)
result = json.loads(r.stdout)
info = {'rc': r.returncode, 'befehl': cmd, 'dauer_s': time.monotonic()-t0, 'grenze': result['boundary'], 'quellen': {f: hashlib.sha256((Path('/root/biotop')/f).read_bytes()).hexdigest() for f in ('biotop/organe/aegis.py','biotop/organe/eichproben.py')}, 'repro_sha256': hashlib.sha256((E/'repro_skip_vertragszeuge.py').read_bytes()).hexdigest(), 'roher_zeuge_uebersprungen': result['raw_target_skipped'], 'geparster_zeuge': result['parsed_target'], 'als_gueltig_akzeptiert': result['accepted_as_valid_countercase'], 'produzent_pruefbar': result['original_einzelprobe_unit_row']['pruefbar'], 'verbraucher': result['consumer_unit_replay']}
(O / (name+'.json')).write_text(json.dumps(info, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(info, ensure_ascii=False)); print(r.stderr)
sys.exit(r.returncode)
