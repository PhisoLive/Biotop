"""Einzelheiten zu den Nachspielen N1–N3 (nur lesend): die eine Laufzeit-Nachmessung (Riss) im Nachspiel, gesperrte
Bereiche der Rauschmessung an Stufe 2 je Fall, Gewinnband je Fall, Datenbank-Prüfsummen aller Nachspiel-Belege dieser
Runde (d1–d3 am Commit 1d9a5aa, n1–n3 am Nachtrag, probe-arbeitsbaum). Aufruf: python einzelheiten.py > EINZELHEITEN.txt"""
import json
from pathlib import Path

A = Path('/root/biotop-vor-t4-04/nachspiel')
gleich = gesamt = 0
for d in ('d1', 'd2', 'd3', 'probe-arbeitsbaum', 'n1', 'n2', 'n3'):
    for f in sorted((A / d).glob('*.json')):
        b = json.loads(f.read_text())
        gesamt += 1
        gleich += b.get('quelle_db_sha256_vorher') == b.get('quelle_db_sha256_nachher') and b.get('quelle_db_sha256_vorher') is not None
        if d.startswith('n') or d == 'probe-arbeitsbaum':
            g = b.get('gewinn_nachmessung') or {}
            print(f"{d:17} {f.stem:9} gesperrt={b.get('gesperrte_bereiche')} toleranz={b.get('rauschtoleranz')} "
                  f"erste={g.get('erste')} band={g.get('band')} bestaetigt={g.get('bestaetigte_bereiche')}")
            nm = b.get('laufzeit_nachmessung')
            if nm:
                print('   LAUFZEIT-NACHMESSUNG:', json.dumps({k: nm.get(k) for k in ('risse', 'bestaetigt', 'nicht_bestaetigt', 'erste', 'zweite')},
                                                               ensure_ascii=False))
        else:
            print(f"{d:17} {f.stem:9} fehler={str(b.get('fehler'))[:110]}")
print(f'Datenbank vorher = nachher: {gleich} von {gesamt} Nachspiel-Belegen')
