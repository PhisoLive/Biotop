"""Gegenproben des erweiterten Wächters: je eine Kopie mit genau EINEM Ausschalter; die Testdatei läuft gegen die Kopie
(WAECHTER_SKRIPT). Vorab festgelegt: welcher Test fallen muss und an welcher Zusicherung (Zeile + Text im Fehlerbericht).
Grundsatz 8: fällt eine Gegenprobe nicht — oder an einer anderen Stelle —, ist die Probe kaputt."""
import json
import os
import re
import subprocess
from pathlib import Path

S = Path('/root/.hermes/scripts/zwischenbericht_waechter.py').read_text()
T = '/root/.hermes/zwischenbericht/test_waechter.py'
AUS = Path('/root/biotop-vor-t4/waechter')

# name: (anker, ersatz, {test: erwarteter Text der fallenden Zusicherung})
FAELLE = {
    'kontext_schwelle_aus': ('KONTEXT_ANTEIL = 0.80', 'KONTEXT_ANTEIL = 2.0',
                             {'test_kontext_unter_80_still_ab_80_genau_einmal': "'Kontextfüllung 80.0 % (800000 von 1000000 Token' in aus",
                              'test_runden_verdichtung_und_kontext_zusammen_ein_ordner': "'Kontextfüllung 85.0 %' in aus"}),
    'kontext_grenzfall_echt_groesser': ("ks['anteil_roh'] >= KONTEXT_ANTEIL", "ks['anteil_roh'] > KONTEXT_ANTEIL",
                                        {'test_kontext_unter_80_still_ab_80_genau_einmal': "'Kontextfüllung 80.0 % (800000 von 1000000 Token' in aus"}),
    'kontext_mehrfach': ("""and f"{s['id']}:{turn_id}:kontext80" not in zustand:""", ':',
                         {'test_kontext_unter_80_still_ab_80_genau_einmal': "len(_ordner(uk)) == 1"}),
    'kontext_fremde_sitzung': ("if f'[{sid}]' in z and (m := API_RE.search(z)):", 'if (m := API_RE.search(z)):',
                               {'test_kontext_gegenprobe_fremde_sitzung_und_unbekannte_grenze': "_lauf(uk) == ''"}),
    'verdichtung_aus': ('def verdichtung_fehlschlag(con, zeilen: list, sid: str, ab: float, jetzt: float):\n',
                        'def verdichtung_fehlschlag(con, zeilen: list, sid: str, ab: float, jetzt: float):\n    return None\n',
                        {'test_erste_gescheiterte_verdichtung_genau_einmal': "'Verdichtung gescheitert' in aus",
                         'test_runden_verdichtung_und_kontext_zusammen_ein_ordner': "'Verdichtung gescheitert' in aus",
                         'test_nachspiel_sitzung_die_erst_nach_jetzt_endete_zaehlt': "'Verdichtung gescheitert' in _lauf"}),
    'verdichtung_vor_turnbeginn': ('        if t < ab:\n            continue\n', '',
                                   {'test_erste_gescheiterte_verdichtung_genau_einmal': "_lauf(uk) == ''"}),
    'verdichtung_fremde_sitzung': ("""if 'compression attempt telemetry' in z and f'"session_id":"{sid}"' in z:""",
                                   "if 'compression attempt telemetry' in z:",
                                   {'test_erste_gescheiterte_verdichtung_genau_einmal': "_lauf(uk) == ''"}),
    'verdichtung_mehrfach': ("""if vf and f"{s['id']}:{turn_id}:verdichtung" not in zustand:""", 'if vf:',
                             {'test_erste_gescheiterte_verdichtung_genau_einmal': "len(_ordner(uk)) == 1"}),
    'sperrkonflikt_als_scheitern': ("NICHT_GESCHEITERT = {'lock_contended'}", 'NICHT_GESCHEITERT = set()',
                                    {'test_sperrkonflikt_ist_kein_scheitern': "_lauf(uk) == ''"}),
    'nachspiel_beendete_sitzung': ('WHERE (ended_at IS NULL OR ended_at > ?) ', 'WHERE (ended_at IS NULL OR ended_at > ? - 1e12) ',
                                   {'test_nachspiel_sitzung_die_erst_nach_jetzt_endete_zaehlt': "_lauf(uk, '--jetzt', str(damals)) == ''"}),
}

ergebnis = {}
for name, (anker, ersatz, erwartet) in FAELLE.items():
    assert S.count(anker) == 1, (name, S.count(anker))
    kopie = Path(f'/tmp/waechter-gegenprobe-{name}.py')
    kopie.write_text(S.replace(anker, ersatz))
    junit = Path(f'/tmp/waechter-gegenprobe-{name}.xml')
    p = subprocess.run(['/root/biotop-t3/venv/bin/python', '-m', 'pytest', T, '-q', '-p', 'no:cacheprovider', '--tb=long',
                        f'--junitxml={junit}'], capture_output=True, text=True, env=dict(os.environ, WAECHTER_SKRIPT=str(kopie)),
                       cwd='/tmp', timeout=300)
    x = junit.read_text()
    gefallen = {}
    for m in re.finditer(r'<testcase [^>]*name="([^"]+)"[^>]*?(?:/>|>(.*?)</testcase>)', x, re.S):
        if m.group(2) and ('<failure' in m.group(2) or '<error' in m.group(2)):
            gefallen[m.group(1)] = m.group(2)
    zeilen = {}
    ok = set(gefallen) == set(erwartet)
    for t, text in erwartet.items():
        body = gefallen.get(t, '')
        # die fallende Zeile ist die mit '>' im Traceback des Tests selbst
        fallend = [z for z in re.findall(r'^&gt;\s+(.*)$', body, re.M) if 'assert' in z]
        zeile = next((z for z in fallend if 'rc == rc_erwartet' not in z), fallend[0] if fallend else '')
        treffer = any(text.replace("'", '&apos;') in z or text in z or text.replace("'", '&#39;') in z for z in fallend)
        ok = ok and treffer and 'AssertionError' in body
        zeilen[t] = {'fallende_zusicherung': zeile[:220], 'erwartet_enthalten': text, 'getroffen': treffer}
    ergebnis[name] = {'rc': p.returncode, 'gefallen': sorted(gefallen), 'erwartet': sorted(erwartet), 'an_der_vorgesehenen_stelle': ok,
                      'zeilen': zeilen, 'zusammenfassung': p.stdout.strip().splitlines()[-1] if p.stdout.strip() else p.stderr[-300:]}
    print(f"{name:32} {'OK ' if ok else 'NEIN'} rc={p.returncode} gefallen={sorted(gefallen)} | {ergebnis[name]['zusammenfassung']}")
    for t, z in zeilen.items():
        print(f"    {t}: {z['getroffen']} :: {z['fallende_zusicherung'][:150]}")
(AUS / 'GEGENPROBEN.json').write_text(json.dumps(ergebnis, ensure_ascii=False, indent=1))
print('gesamt:', sum(v['an_der_vorgesehenen_stelle'] for v in ergebnis.values()), 'von', len(ergebnis))
