"""Validiert ausschließlich das lesende Auditpaket, führt kein Biotop aus."""
from pathlib import Path
import collections
import hashlib
import json
import datetime

A = Path(__file__).resolve().parent
Q = A.parent / 'QUELLEN.json'
REF = Path('/root/reparatur-01/review-02/repo')

def load(name):
    return json.loads((A / name).read_text())

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    q = json.loads(Q.read_text())
    f = load('DATEIPRUEFUNG.json')
    s = load('LESESTELLEN.json')
    b = load('BEFUNDE.json')
    c = load('KANDIDATEN-OFFEN.json')
    outside = load('AUSSERHALB-KERN-BESTAETIGT-OFFEN.json')
    p4 = load('P4-BESTEHEND-OFFEN.json')
    h = load('SUCHTREFFER-ZUORDNUNG.json')
    cov = load('ABDECKUNG.json')
    assignment = load('KERN-NACHWEISZUORDNUNG.json')
    expected_groups = {'produkt':36, 'pruefskript':63, 'eigentest':11, 'vertrag_fixture':7, 'konfiguration_oder_dokument':9}
    assert len(q) == len(f) == 126
    assert len({x['pfad'] for x in q}) == len(q)
    assert [x['pfad'] for x in q] == [x['pfad'] for x in f]
    assert dict(collections.Counter(x['gruppe'] for x in f)) == expected_groups
    sm = {x['id']:x for x in s}
    bm = {x['id']:x for x in b}
    fm = {x['pfad']:x for x in f}
    assert len(sm) == len(s) == cov['semantische_lesebloecke']
    assert len(bm) == len(b) == cov['deduplizierte_bestaetigte_mechanismen']
    assert len({x['dedup_mechanismus'] for x in b}) == len(b)
    original_ok = 0
    source_lines = {}
    for x in q:
        p = x['pfad']
        assert sha(A/'quellen'/p) == sha(REF/p) == x['sha256'] == fm[p]['sha256'], p
        assert (A/'quellen'/p).stat().st_size == fm[p]['bytes'] == x['bytes'], p
        original_ok += 1
        source_lines[p] = (A/'quellen'/p).read_text().splitlines()
        assert fm[p]['gelesen'] is True
        assert fm[p]['relevant'] == bool(fm[p]['lesestellen'])
        assert all(sm[i]['pfad'] == p for i in fm[p]['lesestellen'])
    for x in s:
        lines = source_lines[x['pfad']]
        lo, hi = x['zeile_von'], x['zeile_bis']
        assert 1 <= lo <= hi <= len(lines), x['id']
        expected = '\n'.join(f'{i}|{lines[i-1]}' for i in range(lo,hi+1))
        assert x['quellbeleg'] == expected, x['id']
        assert x['kernpfadbezug']['konkreter_aufruf_oder_datenfluss']
        assert x['ausgefuehrt_im_audit'] is False
        assert x['nachweiszuordnung']['testausfuehrung_im_audit'] is False
        assert all(x['id'] in bm[i]['lesestellen'] for i in x['befunde'])
    for x in b:
        assert all(i in sm for i in x['lesestellen'])
        assert x['unabhaengige_Testausfuehrung_dieses_Audits'] is False
        assert set(x['kern_orte']).isdisjoint(x['aussen_bestaetigt_offene_orte'])
        assert set(x['kern_orte']) | set(x['aussen_bestaetigt_offene_orte']) == set(x['lesestellen'])
    assert len(c) == cov['offene_semantische_kandidaten']
    assert all(x['status'] == 'ungeprueft_unvollstaendig_nicht_bestaetigt' for x in c)
    assert len(p4) == 4 and {x['id'] for x in p4} == {'P4-01','P4-02','P4-03','P4-04'}
    assert all(x['status'] == 'bestehend_offen' for x in p4)
    assert all(x['fixpflicht_in_dieser_Runde'] is False for x in outside)
    assert {i for x in outside for i in x['lesestellen']} == {i for x in b for i in x['aussen_bestaetigt_offene_orte']}
    assert all(sm[i]['kernpfadbezug']['klasse'] == 'ausserhalb_kern' for x in outside for i in x['lesestellen'])
    rawhits = json.loads((A.parent/'SUCHTREFFER.json').read_text())
    assert len(h) == len(rawhits) == 661
    for x, original in zip(h, rawhits):
        assert all(x[k] == original[k] for k in ('pfad','zeile','code','gruppe'))
        assert source_lines[x['pfad']][x['zeile']-1] == x['code']
        assert all(i in sm for i in x['lesestellen'])
    assert dict(collections.Counter(x['status'] for x in h)) == cov['kandidatenzeilen_status']
    core = {x['id'] for x in s if x['kernpfadbezug']['klasse'] != 'ausserhalb_kern'}
    assert {x['id'] for x in assignment} == core
    assert cov['vollstaendige_semantische_Suche_bewiesen'] is False
    after = load('NACHAUDIT-ORIGINAL.json')
    assert len(after['dateien']) == 4
    assert sum(x['im_originalinventar'] for x in after['dateien']) == 3
    assert after['aendert_original_nenner'] is False
    assert len([x for x in b if x['kern_orte'] and x['aussen_bestaetigt_offene_orte']]) == 2
    result = {
        'auditpaket_validiert':True,
        'zeit_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'original_dateien_bytegleich':original_ok,
        'inventar_dateien':len(f),
        'gruppen':expected_groups,
        'semantische_lesebloecke_zeilengleich':len(s),
        'kernleser_mit_zuordnung_oder_explizit_offener_pflicht':len(core),
        'befundmechanismen':len(b),
        'aussen_bestaetigte_orte':len({i for x in outside for i in x['lesestellen']}),
        'offene_semantische_kandidaten':len(c),
        'offene_regex_feinzuordnungen':sum(x['status']=='Feinzuordnung_offen' for x in h),
        'suchkandidaten_reconciled':len(h),
        'phase4_offen':len(p4),
        'produktcode_oder_produkttests_ausgefuehrt':False,
        'semantische_suchvollstaendigkeit_bewiesen':False,
    }
    (A/'VALIDIERUNG.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    excluded = {'SHA256SUMS','SHA-PRUEFUNG.json'}
    paths = sorted(p for p in A.rglob('*') if p.is_file() and p.relative_to(A).as_posix() not in excluded)
    rows = [(sha(p),p.relative_to(A).as_posix()) for p in paths]
    assert rows and len({p for _,p in rows}) == len(rows)
    (A/'SHA256SUMS').write_text(''.join(f'{digest}  {p}\n' for digest,p in rows))
    print(json.dumps({**result,'sha_manifest_eintraege':len(rows)},ensure_ascii=False))

if __name__ == '__main__':
    main()
