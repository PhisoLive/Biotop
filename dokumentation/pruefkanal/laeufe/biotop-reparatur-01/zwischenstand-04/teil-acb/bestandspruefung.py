"""Deterministischer Bestands-Replay. KEINE Modell-/Kammerausführung.

Aufruf: venv/bin/python bestandspruefung.py <ergebnis.json>
Siehe MESSPLAN.md. Original-DB wird nur mode=ro&immutable=1 geöffnet.
"""
from __future__ import annotations

import ast
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import socket
import sqlite3
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'repo'))
from biotop import anbieter
from biotop.kern import protokoll
from biotop.organe import aegis, gedaechtnis, kammer

DB = Path('/root/reparatur-01/ausgang.db')

def forbidden(*a, **k):
    raise AssertionError('VERBOTEN: Modell/Anbieter/Netz/Kammer im Bestands-Replay')

socket.create_connection = forbidden
socket.socket.connect = forbidden
anbieter.aufrufen = anbieter.adapter = forbidden
kammer.ausfuehren = forbidden
aegis.aufrufen = gedaechtnis.aufrufen = forbidden
# Nur erzeugte Replay-Protokollzeilen deterministisch; Originalzeiten bleiben erhalten.
protokoll.jetzt = lambda: '2099-01-01T00:00:00.000+00:00'

def old_module(name):
    spec = importlib.util.spec_from_file_location('biotop.organe.' + name + '_baseline', ROOT / 'baseline/biotop/organe' / (name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.aufrufen = forbidden
    return mod

old_a, old_g = old_module('aegis'), old_module('gedaechtnis')
source = sqlite3.connect(f'file:{DB}?mode=ro&immutable=1', uri=True)
source.row_factory = sqlite3.Row

def rows(table):
    return [dict(r) for r in source.execute(f'SELECT * FROM {table}')]

ks = {r['id']: r for r in rows('kandidaten')}
works = {r['id']: r for r in rows('werke')}
runs = {r['id']: r for r in rows('laeufe')}
im = sorted(rows('immunsystem'), key=lambda r: r['id'])
arts = sorted(rows('artgedaechtnis'), key=lambda r: r['id'])
logs = [dict(r) for r in source.execute("SELECT * FROM protokoll WHERE art IN ('aegis.ansage','immun.aufnahme_geprueft','immun.aufnahme_gesperrt','aegis.urteil') ORDER BY nr")]
for r in logs:
    r['d'] = json.loads(r['inhalt'])
ansages = [r for r in logs if r['art'] == 'aegis.ansage']

def candidate_kind(k):
    if k is None:
        return 'nicht_zuordenbar'
    text = ((k.get('anbieter') or '') + '/' + (k.get('modell') or '')).lower()
    if gedaechtnis.ist_probe(k) or any(x in text for x in ('hermes', 'probe', 'eich')):
        return 'gestellt'
    return 'natuerlich'


def immun_info(r):
    ids = {int(x) for x in re.findall(r'Kandidat (\d+)', r['ursprung'] or '')}
    kid = next(iter(ids)) if len(ids) == 1 else None
    imported = bool(re.search(r'uebernommen|übernommen', r['ursprung'] or '', re.I))
    if 'hermes' in (r['name'] + ' ' + (r['ursprung'] or '')).lower():
        kind = 'gestellt'
    else:
        kind = candidate_kind(ks.get(kid))
    try:
        names = sorted(n.name for n in ast.walk(ast.parse(r['code'] or ''))
                       if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name.startswith('test'))
        error = None
    except SyntaxError as e:
        names, error = [], str(e)
    return {'id': r['id'], 'name': r['name'], 'kandidat': kid, 'werk_id': r['werk_id'], 'lauf_id': r['lauf_id'],
            'bereich': r['bereich'], 'generation': r['generation'], 'erstellt_am': r['erstellt_am'],
            'kategorie': kind, 'uebernommen': imported, 'testnamen': names, 'syntaxfehler': error}

infos = {r['id']: immun_info(r) for r in im}
natural_im = [r for r in im if infos[r['id']]['kategorie'] == 'natuerlich']
original_im = [r for r in natural_im if not infos[r['id']]['uebernommen']]

# Vollständiges SQLite-Backup in RAM; keine Credential-/Token-Daten werden ausgegeben.
# Die Kopie enthält alle eigentlichen Bestandstabellen. Zugangstabellen werden darin entfernt.
base = sqlite3.connect(':memory:', isolation_level=None)
base.row_factory = sqlite3.Row
source.backup(base)
base.executescript('DROP TABLE IF EXISTS benutzer; DROP TABLE IF EXISTS tokens;')
base.execute('DELETE FROM immunsystem')
base.execute('DELETE FROM protokoll')


def insert(c, table, items):
    for row in items:
        keys = [k for k in row if k != 'd']
        c.execute(f"INSERT INTO {table}({','.join(keys)}) VALUES({','.join('?' for k in keys)})", [row[k] for k in keys])


def snapshot(prior_im, prior_a):
    c = sqlite3.connect(':memory:', isolation_level=None)
    c.row_factory = sqlite3.Row
    base.backup(c)
    insert(c, 'immunsystem', prior_im)
    insert(c, 'protokoll', prior_a)
    return c


def population_before(r):
    # Time first; IDs disambiguate a tie only within this single table's insertion order.
    ii = [q for q in natural_im if (q['erstellt_am'], q['id']) < (r['erstellt_am'], r['id'])]
    aa = [q for q in ansages if q['zeit'] < r['erstellt_am']]
    return ii, aa


def sources_for(prior_im, prior_a, wid, lid, bereich):
    # Reuse the organ's derivation for each source. No second parser of stored key syntax.
    result = {}
    small = sqlite3.connect(':memory:', isolation_level=None)
    small.row_factory = sqlite3.Row
    for table in ('immunsystem', 'protokoll'):
        sql = source.execute('SELECT sql FROM sqlite_master WHERE name=?', (table,)).fetchone()[0]
        small.execute(sql)
    for table, entries, idfield, prefix in [('immunsystem', prior_im, 'id', 'I'), ('protokoll', prior_a, 'nr', 'P')]:
        for r in entries:
            if table == 'immunsystem' and (r['werk_id'] != wid or r['bereich'] != bereich):
                continue
            if table == 'protokoll' and (r['d'].get('lauf_id') != lid or r['d'].get('bereich') != bereich):
                continue
            insert(small, table, [r])
            for key in aegis.bisherige_behauptungen(small, wid, bereich, lid, limit=None):
                result.setdefault(key, []).append(prefix + str(r[idfield]))
            small.execute(f'DELETE FROM {table}')
    small.close()
    return result


def gate(mod, c, r, names, own=None):
    kw = {'eigene_ansage_nr': own} if mod is aegis else {}
    keep, block = mod.aufnahmesperre(c, r['werk_id'], r['lauf_id'], r['bereich'], r['code'], names,
                                    gedaechtnis.werkname(c, r['werk_id']), infos[r['id']]['kandidat'],
                                    'norm' if r['name'].startswith('norm_') else 'fund', **kw)
    reasons = [json.loads(z['inhalt']) for z in c.execute("SELECT inhalt FROM protokoll WHERE art='immun.aufnahme_gesperrt'")]
    for reason in reasons:
        assert reason['gegenstueck'] in ('bereits im Vorrat des Bereichs', 'zweiter Test derselben Behauptung in diesem Kandidaten')
    assert len(keep) + len(block) == len(names)
    return {'aufnehmen': [list(x) for x in keep], 'sperren': [list(x) for x in block],
            'sperrgruende': [{'test': d['test'], 'gegenstueck': d['gegenstueck']} for d in reasons]}


def c_replay():
    out, roles = [], []
    for r in original_im:
        info = infos[r['id']]
        ii, aa = population_before(r)
        src = sources_for(ii, aa, r['werk_id'], r['lauf_id'], r['bereich'])
        results = {}
        for name, mod in [('alt', old_a), ('neu', aegis)]:
            c = snapshot(ii, aa)
            results[name] = gate(mod, c, r, info['testnamen'])
            c.close()
        seen = set()
        tests = []
        for test in info['testnamen']:
            key = aegis.behauptung(r['code'], test)
            witnesses = src.get(key, [])
            expected = bool(witnesses) or key in seen
            tests.append({'test': test, 'schluessel': key, 'zeugen': witnesses,
                          'gleicher_schluessel_frueher_im_batch': key in seen,
                          'sicherer_immuntest_vorbestand': any(w.startswith('I') for w in witnesses),
                          'nur_unzugeordnete_ansage': bool(witnesses) and all(w.startswith('P') for w in witnesses),
                          'erwartet_sperren_mit_vollstaendigem_rekonstruiertem_vorrat': expected})
            actual = [test, key] in results['neu']['sperren']
            assert actual == expected
            seen.add(key)
            # Rollenrekonstruktion je ECHTER Testfunktion, nicht als historische Zuordnung ausgegeben.
            role = {'immun_id': r['id'], 'kandidat': info['kandidat'], 'test': test, 'schluessel': key,
                    'zeugen_vor_aktueller_ansage': witnesses, 'erwartet_sperren': bool(witnesses),
                    'herkunft_eigene_ansage': 'aus realem Testschluessel rekonstruierte aktuelle Rolle; NICHT historisch zugeordnet'}
            for name, mod in [('alt', old_a), ('neu', aegis)]:
                c = snapshot(ii, aa)
                nr = protokoll.schreiben(c, 'aegis.ansage', lauf_id=r['lauf_id'], werk_id=r['werk_id'],
                                        bereich=r['bereich'], kandidat=info['kandidat'], behauptung=key,
                                        ausgefuehrt=True, replay_rolle=True)
                verdict = gate(mod, c, r, [test], nr)
                role[name + '_gesperrt'] = bool(verdict['sperren'])
                role[name + '_grund'] = verdict['sperrgruende']
                c.close()
            assert role['neu_gesperrt'] == role['erwartet_sperren']
            roles.append(role)
        out.append({**info, 'vorrat_immun_ids': [q['id'] for q in ii if q['werk_id'] == r['werk_id'] and q['bereich'] == r['bereich']],
                    'vorrat_ansage_nrn': [q['nr'] for q in aa if q['d'].get('lauf_id') == r['lauf_id'] and q['d'].get('bereich') == r['bereich']],
                    'tests': tests, **results})
    return out, roles


class TestgenerierungErreicht(Exception):
    pass


def a_replay():
    out = []
    for r in ansages:
        d = r['d']
        lid = d.get('lauf_id')
        wid = runs.get(lid, {}).get('werk_id')
        if wid is None:
            out.append({'nr': r['nr'], 'kategorie': 'unbekannter_lauf', 'inhalt': d})
            continue
        ii = [q for q in natural_im if q['erstellt_am'] < r['zeit']]
        aa = [q for q in ansages if q['nr'] < r['nr']]
        src = sources_for(ii, aa, wid, lid, d['bereich'])
        entry = {'nr': r['nr'], 'zeit': r['zeit'], 'lauf_id': lid, 'werk_id': wid, 'bereich': d['bereich'],
                 'behauptung': d.get('behauptung'), 'historisch_ausgefuehrt': d.get('ausgefuehrt'),
                 'kandidat': d.get('kandidat'), 'kategorie': candidate_kind(ks.get(d.get('kandidat'))),
                 'zeugen': src.get(d.get('behauptung'), [])}
        for name, mod in [('alt', old_a), ('neu', aegis)]:
            c = snapshot(ii, aa)
            original_ansage, original_aufrufen = mod._ansage, mod.aufrufen
            mod._ansage = lambda *a, **kw: (d.get('behauptung'), False)
            def stop(*a, **kw):
                assert kw['zweck'].startswith('aegis.angriff.')
                raise TestgenerierungErreicht()
            mod.aufrufen = stop
            try:
                mod._angriff(c, lid, wid, 'replay_ohne_quellwerk', d['bereich'], '', {}, ROOT / 'kein_werk', [])
                entry[name] = 'abstinent' if d.get('behauptung') is None else 'gesperrt'
            except TestgenerierungErreicht:
                entry[name] = 'Testgenerierung_erreicht_aber_nicht_ausgefuehrt'
            finally:
                mod._ansage, mod.aufrufen = original_ansage, original_aufrufen
                c.close()
        out.append(entry)
    return out


def b_replay():
    out = []
    for cleaned in (False, True):
        c = sqlite3.connect(':memory:', isolation_level=None)
        c.row_factory = sqlite3.Row
        source.backup(c)
        c.executescript('DROP TABLE IF EXISTS benutzer; DROP TABLE IF EXISTS tokens;')
        excluded = [a['id'] for a in arts if candidate_kind(ks.get(a['kandidat_id'])) != 'natuerlich'] if cleaned else []
        c.executemany('DELETE FROM artgedaechtnis WHERE id=?', [(i,) for i in excluded])
        all_art = [dict(r) for r in c.execute('SELECT * FROM artgedaechtnis ORDER BY id DESC')]
        indexed = {a['id']: a for a in all_art}
        for wid in sorted(works):
            family = gedaechtnis.werkname(c, wid)
            foreign = [a for a in all_art if a['werk'] != family and a['ergebnis'] == 'angenommen' and (a['muster'] or '').strip()]
            unique, seen = [], set()
            for a in foreign:
                key = a['muster'].lower()[:80]  # declared existing renderer's grouping, no new grouping
                if key not in seen:
                    seen.add(key)
                    unique.append(a['id'])
            item = {'werk_id': wid, 'familie': family, 'population': 'natuerlich_bereinigt' if cleaned else 'roh_unveraendert',
                    'ausgeschlossene_art_ids': excluded, 'eigene_pool_ids': [a['id'] for a in all_art if a['werk'] == family],
                    'fremde_muster_roh_ids': [a['id'] for a in foreign], 'fremde_muster_eindeutig_ids': unique}
            for name, mod in [('alt', old_g), ('neu', gedaechtnis)]:
                text = mod.art_text(c, wid)
                ids = [int(i) for i in re.findall(r'\[A(\d+)\]', text)]
                own = [i for i in ids if indexed[i]['werk'] == family]
                other = [i for i in ids if indexed[i]['werk'] != family]
                required = min(len(unique), max(5, (len(ids) + 1) // 2))
                item[name] = {'gezeigt_ids': ids, 'eigene_ids': own, 'fremde_ids': other,
                              'gesamt': len(ids), 'eigene': len(own), 'fremde': len(other),
                              'fremd_mindestzahl': required, 'erfuellt': len(other) >= required,
                              'vorlagentext': text}
            assert item['neu']['erfuellt']
            out.append(item)
        c.close()
    return out


def main():
    before = hashlib.sha256(DB.read_bytes()).hexdigest()
    candidates = [{'id': k['id'], 'lauf_id': k['lauf_id'], 'generation': k['generation'], 'bereich': k['bereich'],
                   'kategorie': candidate_kind(k), 'ist_probe': k['ist_probe'], 'modell': k['modell'], 'nische': k['nische'],
                   'status': k['status']} for k in ks.values()]
    c, roles = c_replay()
    a = a_replay()
    b = b_replay()
    # Reconcile every retained candidate via explicit candidate IDs, never stream order.
    urteile = []
    for r in logs:
        if r['art'] != 'aegis.urteil':
            continue
        d = r['d']
        k = ks.get(d.get('kandidat'))
        urteile.append({'nr': r['nr'], 'kandidat': d.get('kandidat'), 'lauf_id': d.get('lauf_id'),
                        'kategorie': candidate_kind(k), 'nische': d.get('nische'), 'bereich': d.get('bereich'),
                        'angriff': d.get('angriff'), 'immun': d.get('immun'), 'norm': d.get('norm'),
                        'doppelungen': d.get('doppelungen')})
    coverage = []
    for k in candidates:
        rr = [r for r in urteile if r['kandidat'] == k['id'] and r['lauf_id'] == k['lauf_id']]
        ii = [r for r in infos.values() if r['kandidat'] == k['id'] and not r['uebernommen']]
        attacks = [r for r in rr if (r.get('angriff') or {}).get('gesamt', 0)]
        coverage.append({'kandidat': k['id'], 'kategorie': k['kategorie'], 'urteil_nrn': [r['nr'] for r in rr],
                         'angriff_mit_testanzahl_nrn': [r['nr'] for r in attacks],
                         'immuneintrag_ids': [r['id'] for r in ii],
                         'abdeckung': ('Immuntestcode_replaybar' if ii else
                                      'Angriff_protokolliert_aber_kein_Immuntestcode_gespeichert' if attacks else
                                      'kein_gespeicherter_Angriffstest_oder_kein_Urteil')})
    admission_events = []
    for r in logs:
        if not r['art'].startswith('immun.aufnahme_'):
            continue
        d = r['d']
        k = ks.get(d.get('kandidat'))
        kind = candidate_kind(k)
        # K1 in a fixture's nonexistent run is NOT the real K1.
        if k is not None and k['lauf_id'] != d.get('lauf_id'):
            kind = 'nicht_zuordenbar_lauf_passt_nicht'
        matching = [u for u in urteile if u['kandidat'] == d.get('kandidat') and u['lauf_id'] == d.get('lauf_id')]
        if matching and all((u['nische'] or '').startswith('probe') for u in matching):
            kind = 'gestellt_belegt_durch_urteil_nische'
        admission_events.append({'nr': r['nr'], 'art': r['art'], 'kategorie': kind, 'inhalt': d,
                                 'zugehoerige_urteil_nrn': [u['nr'] for u in matching]})
    art_inventory = [{'id': x['id'], 'kandidat': x['kandidat_id'], 'werk': x['werk'], 'lauf_id': x['lauf_id'],
                      'ergebnis': x['ergebnis'], 'hat_muster': bool((x['muster'] or '').strip()),
                      'kategorie': candidate_kind(ks.get(x['kandidat_id']))} for x in arts]
    summary = {
        'kandidaten': dict(Counter(x['kategorie'] for x in candidates)),
        'natuerliche_kandidaten_abdeckung': dict(Counter(x['abdeckung'] for x in coverage if x['kategorie']=='natuerlich')),
        'immunsystem': dict(Counter(x['kategorie'] for x in infos.values())),
        'natuerliche_original_immuneintraege': len(c),
        'natuerliche_uebernommene_immuneintraege': sum(x['kategorie']=='natuerlich' and x['uebernommen'] for x in infos.values()),
        'c_testentscheidungen': sum(len(x['tests']) for x in c),
        'c_neu_sperren': sum(len(x['neu']['sperren']) for x in c),
        'c_neu_aufnehmen': sum(len(x['neu']['aufnehmen']) for x in c),
        'c_sicherer_immuntest_vorbestand': sum(t['sicherer_immuntest_vorbestand'] for x in c for t in x['tests']),
        'c_nur_unzugeordnete_ansage': sum(t['nur_unzugeordnete_ansage'] for x in c for t in x['tests']),
        'testschluessel_mit_fragezeichen': [{'immun_id': x['immun_id'], 'test': x['test'], 'schluessel': x['schluessel']}
                                           for x in roles if '?' in x['schluessel']],
        'rollenrekonstruktion_tests': len(roles),
        'rollenrekonstruktion_alt_falsche_sperren': sum(x['alt_gesperrt'] and not x['erwartet_sperren'] for x in roles),
        'rollenrekonstruktion_neu_falsche_sperren': sum(x['neu_gesperrt'] and not x['erwartet_sperren'] for x in roles),
        'rollenrekonstruktion_neu_durchrutscher': sum(not x['neu_gesperrt'] and x['erwartet_sperren'] for x in roles),
        'ansagen': len(a), 'ansage_kandidatenbindung': dict(Counter(x['kategorie'] for x in a)),
        'a_neu': dict(Counter(x.get('neu') for x in a)),
        'artgedaechtnis': dict(Counter(x['kategorie'] for x in art_inventory)),
        'b_werk_population_kombinationen': len(b),
        'b_alt_verletzungen': sum(not x['alt']['erfuellt'] for x in b),
        'b_neu_verletzungen': sum(not x['neu']['erfuellt'] for x in b),
        'historische_c_ereignisse': dict(Counter(x['kategorie'] for x in admission_events)),
        'netz_anbieter_modell_kammer_aufrufe': 0,
        'kasse_zeilen_unveraendert': source.execute('SELECT count(*) FROM kasse').fetchone()[0],
    }
    after = hashlib.sha256(DB.read_bytes()).hexdigest()
    assert before == after
    result = {'typ': 'deterministischer Replay/Organaufruf auf echtem eingefrorenem Bestand; KEIN Live-Lauf',
              'db_sha256_vorher': before, 'db_sha256_nachher': after, 'summary': summary,
              'kandidaten': candidates, 'kandidaten_abdeckung': coverage, 'urteile': urteile,
              'immunsystem': list(infos.values()), 'ansagen': a,
              'c_historischer_vorrat_replay': c, 'ac_aktuelle_eigene_ansage_rollenrekonstruktion': roles,
              'artgedaechtnis': art_inventory, 'b_organaufruf': b, 'historische_c_ereignisse': admission_events}
    Path(sys.argv[1]).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print('DB sha256 unverändert:', before)

if __name__ == '__main__':
    main()
