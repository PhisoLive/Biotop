"""Nur lesend: Nachspiel-Belege n1..n3 (+ Vorprobe), Vorher/Nachher-Einzelfälle, Verdrahtungskosten."""
import json
from pathlib import Path

A = Path('/root/biotop-vor-t4-05')
for d in ('n1', 'n2', 'n3', 'vorprobe'):
    for f in sorted((A / 'nachspiel' / d).glob('*.json')):
        j = json.loads(f.read_text())
        flach = json.dumps(j, ensure_ascii=False)
        db_gleich = j.get('quelle_db_sha256_vorher') == j.get('quelle_db_sha256_nachher') and bool(j.get('quelle_db_sha256_vorher'))
        tz = j.get('toleranz') or (j.get('rauschen') or {}).get('toleranz')
        v = j.get('verhalten') or (j.get('urteil') or {}).get('verhalten') or {}
        print(f"{d}/{f.name}: status={j.get('status')} aufgez={j.get('status_aufgezeichnet')} stufe={j.get('laufzeit_stufe')} "
              f"code={j.get('code_stand') or j.get('head') or j.get('commit')} sauber={j.get('arbeitsbaum_sauber')} "
              f"db_gleich={db_gleich} modell={j.get('modellaufrufe_echt')} gesperrt={j.get('gesperrte_bereiche', j.get('gesperrt'))} "
              f"eingang_tol={(tz or {}).get('eingang') if isinstance(tz, dict) else tz}")
        if 'k2868' in f.name:
            print('   ungedeckt_aufschl', json.dumps(v.get('ungedeckt_aufschluesselung') or j.get('ungedeckt'), ensure_ascii=False)[:900])
            dz = v.get('deckung_zaehlung') or {}
            print('   deckung', {k: dz.get(k) for k in ('tests', 'verfaelschungen', 'ausgelassen', 'kappe')},
                  'gedeckt', len(v.get('gedeckt') or {}), 'unvollst', v.get('unvollstaendig'), 'ausfall', v.get('sonde_ausfall'))
        if d == 'n1' and 'k2904' in f.name:
            print('   schluessel', sorted(j)[:60])
d = json.loads((A / 'VERDRAHTUNG-BELEG-REGRESSION.json').read_text())
print('verdrahtung modellkosten_eur', d.get('modellkosten_eur'), 'anbietergrenze', str(d.get('anbietergrenze'))[:200])
for n in ('VORHER-43b8fad', 'NACHHER-HEAD'):
    for f in sorted((A / 'proben').glob(n + '*')):
        if f.suffix == '.txt':
            print('==', f.name)
            print(f.read_text()[:4200])
