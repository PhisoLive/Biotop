"""Review vor T4-04 — N1-Belege auswerten (nur lesen): K2868 Deckung/Muster, K2904/K3091 Quoten, Stufe, Rauschen."""
import json
from pathlib import Path

A = Path('/root/biotop-vor-t4-04/nachspiel')
for d in ('n1', 'n2', 'n3'):
    for f in sorted((A / d).glob('*.json')):
        b = json.loads(f.read_text())
        v = b.get('verhalten') or {}
        lz = b.get('laufzeit_gepaart') or {}
        g = b.get('gewinn_nachmessung') or {}
        print(f'--- {d}/{f.name}: status={b.get("status")} erwartet={b.get("erwartung")} erfuellt={b.get("erwartung_erfuellt")} '
              f'stufe={b.get("laufzeit_stufe")} code={b.get("code_stand_beim_import", {}).get("commit", "")[:7]} '
              f'sauber={b.get("code_stand_beim_import", {}).get("arbeitsbaum_sauber")} db_gleich={b.get("quelle_db_sha256_vorher") == b.get("quelle_db_sha256_nachher")} '
              f'modell={b.get("modellaufrufe_echt")} fehler={str(b.get("fehler"))[:120]}')
        q = {}
        for bb, x in (lz.get('bereiche') or {}).items():
            if x.get('basis') and x.get('kandidat'):
                q[bb] = round(x['kandidat'] / x['basis'], 4)
        print('    quoten', q, '| gewinn', g.get('ergebnis'), g.get('bestaetigte_bereiche'), '| toleranz', b.get('rauschtoleranz'), 'gesperrt', b.get('gesperrte_bereiche'))
        print('    rauschen', b.get('rauschen_herkunft'), '| grund', str(b.get('grund'))[:160])
        if f.name == 'k2868.json':
            auf = v.get('ungedeckt_aufschluesselung') or {}
            print('    abw', v.get('anzahl_abweichungen'), 'ungedeckt', len(v.get('ungedeckt') or []), 'gedeckt', len(v.get('gedeckt') or {}))
            print('    ungedeckt_aufschluesselung', json.dumps(auf, ensure_ascii=False))
            dz = v.get('deckung_zaehlung') or {}
            print('    deckung_zaehlung', json.dumps({k: dz.get(k) for k in ('tests', 'aufrufe', 'verfaelschungen', 'kappe', 'ausgelassen')}, ensure_ascii=False))
            print('    festhaltend', json.dumps(dz.get('festhaltend'), ensure_ascii=False)[:900])
            print('    klassen_je_test', json.dumps(dz.get('klassen_je_test'), ensure_ascii=False)[:900])
            ged = v.get('gedeckt') or {}
            print('    gedeckt (Schlüssel)', sorted(ged)[:20])
            print('    eigene_tests_ausgeschlossen', v.get('eigene_tests_ausgeschlossen'), '| teilweise', v.get('teilweise'))
            print('    eingaben', json.dumps(v.get('eingaben') or b.get('eingaben'), ensure_ascii=False)[:600])
