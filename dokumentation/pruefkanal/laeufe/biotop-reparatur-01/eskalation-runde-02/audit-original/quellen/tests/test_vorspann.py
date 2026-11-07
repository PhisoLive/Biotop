"""Sperren müssen vor jeder Übergabe an die nächste Stufe wirken."""
import pytest
from biotop.organe import generation0 as G0
from biotop import lauf as L
from biotop.organe import vorspann as V, eichung, eichgegenstand, eichproben, fundpruefung, verfassung, vertraege
from biotop.kern.datenbank import j, lj
from pathlib import Path
import copy
import hashlib


@pytest.fixture
def unit_vorspann(db_lauf, monkeypatch, messung):
    """Gate-UNIT-Test: Messung/Proben kontrolliert ersetzt, KEINE echte Eichung."""
    monkeypatch.setattr(V, '_infrastruktur', lambda: {'image':'unit:1','image_id':'sha256:' + 'a'*64}, raising=False)
    con = db_lauf
    con.execute("DELETE FROM generationen")
    con.execute("UPDATE laeufe SET mass=NULL, status='kartiert'")
    pfad = Path(L._werk(con, 1)['pfad'])
    (pfad / 'paket' / 'beta').mkdir()
    (pfad / 'paket' / 'beta' / '__init__.py').write_text('')
    verfassung.einlegen(con, 1, 'alpha nutzt beta; Satz 2: Messgerät bleibt fest.',
                       {'uebungswerk': True, 'tragender_pfad': [['alpha','beta']]}, 'Unit-Verfassung', 'Eigen-Test')
    vertraege.einlegen(con, 1, pfad, {('alpha','beta'): 'def test_vertrag():\n    assert True\n'}, 'Unit-Vertrag')
    con.execute("INSERT INTO landkarte(werk_id,stufe,schluessel,inhalt) VALUES(1,1,'unit','{}')")
    reihenfolge = []
    raw = {
        'rauschen': {'toleranz': {'alpha':1.2,'beta':1.3}, 'gesperrt': [], 'lauf_startet':True,
                     'bereiche': {b:{'toleranz':t, 'gesperrt':False, 'werte':[100,100,100,110,120], 'meldung':None}
                                  for b,t in [('alpha',1.2),('beta',1.3)]}},
        'funde': {'geprueft':0, 'geaendert':0, 'kammerlaeufe':0, 'ergebnisse':[], 'bezugsgroesse':'0 von 0'},
        'proben': {'bestanden':True,
                   'proben': {n:{'ausgefuehrt':True, 'pruefbar':True, 'bestanden':True, 'grund':'Unit-Positivkontrolle', 'kammerlaeufe':2, 'modellaufrufe':0, 'kosten_eur':0.0, 'dauer_s':0.1} for n in eichproben.PROBEN},
                   'gegenproben': {n:{'ausgefuehrt':True, 'pruefbar':True, 'bestanden':False, 'grund':'Unit-Negativkontrolle', 'kammerlaeufe':3, 'modellaufrufe':0, 'kosten_eur':0.0, 'dauer_s':0.1} for n in eichproben.PROBEN}},
        'reihenfolge': reihenfolge, 'probe_aufrufe': [],
    }
    def rauschen(*a, **kw):
        reihenfolge.append('rauschen')
        return copy.deepcopy(raw['rauschen'])
    sichern = eichgegenstand.sichern
    def gegenstand(*a, **kw):
        reihenfolge.append('gegenstand')
        return sichern(*a, **kw)
    def funde(*a, **kw):
        reihenfolge.append('funde')
        return copy.deepcopy(raw['funde'])
    def proben(*a, **kw):
        reihenfolge.append('proben')
        raw['probe_aufrufe'].append((a, kw))
        return dict(copy.deepcopy(raw['proben']), gegenstand=eichgegenstand.lesen(con, 1))
    monkeypatch.setattr(eichung, 'rauschmessung', rauschen)
    monkeypatch.setattr(eichgegenstand, 'sichern', gegenstand)
    monkeypatch.setattr(fundpruefung, 'bewerten', funde)
    monkeypatch.setattr(eichproben, 'proben', proben)
    monkeypatch.setattr(L, '_referenzlast', lambda *a: '# Unit-Referenzlast')
    monkeypatch.setattr(L.messgeraet, 'messen', lambda *a, **kw: messung())
    return con, raw


def test_unit_erfolgreicher_vorspann_vor_gen0_und_mass(unit_vorspann):
    con, raw = unit_vorspann
    assert callable(getattr(V, 'ausfuehren', None)), 'Start-Gate braucht ausführbaren Kernpfad'
    r = V.ausfuehren(con, 1)
    assert raw['reihenfolge'] == ['rauschen','gegenstand','funde','proben']
    assert raw['probe_aufrufe'][0][1]['generation'] == -1
    assert L._lauf(con, 1)['mass'] is None
    assert con.execute('SELECT count(*) FROM generationen').fetchone()[0] == 0
    assert r['qualitaet'] == {'positive':4, 'negative':4, 'erwartet_je':4}
    assert r['rauschen'] == raw['rauschen']
    assert len(r['nachweis_sha256']) == 64
    assert V.verlangen(con, 1, 'gen0')['nachweis_sha256'] == r['nachweis_sha256']
    e = con.execute("SELECT inhalt FROM protokoll WHERE art='vorspann.bestanden'").fetchone()
    assert lj(e[0])['nachweis_sha256'] == r['nachweis_sha256']


@pytest.mark.parametrize('fehler', ['positiv_rot','gegen_gruen','gegen_fehlend','nicht_ausgefuehrt','nicht_pruefbar','gesamt_rot','zusaetzlich','kein_gegenstand'])
def test_unit_unvollstaendige_eichung_liefert_keinen_nachweis_oder_retry(unit_vorspann, monkeypatch, fehler):
    con, raw = unit_vorspann
    p = raw['proben']
    if fehler == 'positiv_rot': p['proben']['norm']['bestanden'] = False
    elif fehler == 'gegen_gruen': p['gegenproben']['norm']['bestanden'] = True
    elif fehler == 'gegen_fehlend': del p['gegenproben']['norm']
    elif fehler == 'nicht_ausgefuehrt': p['gegenproben']['norm']['ausgefuehrt'] = False
    elif fehler == 'nicht_pruefbar': p['gegenproben']['norm']['pruefbar'] = False
    elif fehler == 'gesamt_rot': p['bestanden'] = False
    elif fehler == 'zusaetzlich': p['gegenproben']['fuenfte'] = dict(p['gegenproben']['norm'])
    else: monkeypatch.setattr(eichgegenstand, 'sichern', lambda *a: {'gegenstand':None, 'befund':'fehlt'})
    with pytest.raises(V.VorspannFehler, match='Vorspann.*neue[rn]? Lauf'):
        V.ausfuehren(con, 1)
    with pytest.raises(V.VorspannFehler, match='Vorspann'):
        V.verlangen(con, 1, 'gen0')
    anzahl = len(raw['reihenfolge'])
    with pytest.raises(V.VorspannFehler, match='neue[rn]? Lauf'):
        V.ausfuehren(con, 1)
    assert len(raw['reihenfolge']) == anzahl, 'kein Grünfischen unter derselben Lauf-ID'
    assert con.execute("SELECT count(*) FROM protokoll WHERE art='vorspann.bestanden'").fetchone()[0] == 0
    e = lj(con.execute("SELECT inhalt FROM protokoll WHERE art='vorspann.gescheitert'").fetchone()[0])
    assert e['ergebnis']['rauschen'] == raw['rauschen']
    assert e['grund']


@pytest.mark.parametrize('alt', ['mass','generation','gen0','beendet'])
def test_unit_alte_laeufe_nicht_nachtraeglich_eichen(unit_vorspann, alt):
    con, raw = unit_vorspann
    if alt == 'mass': con.execute("UPDATE laeufe SET mass='{}'")
    elif alt == 'generation': con.execute("INSERT INTO generationen(lauf_id,nummer,status) VALUES(1,0,'angenommen')")
    elif alt == 'gen0': L.protokoll.schreiben(con, 'generation0.begonnen', lauf_id=1)
    else: con.execute("UPDATE laeufe SET status='beendet'")
    with pytest.raises(V.VorspannFehler, match='neue[rn]? Lauf'):
        V.ausfuehren(con, 1)
    assert raw['reihenfolge'] == []


@pytest.mark.parametrize('fehlt', ['Verfassung','Landkarte','Referenzlast','Verträge'])
def test_unit_voraussetzungen_vor_erster_messung(unit_vorspann, monkeypatch, fehlt):
    con, raw = unit_vorspann
    if fehlt == 'Verfassung': con.execute('DELETE FROM verfassung_werk')
    elif fehlt == 'Landkarte': con.execute('DELETE FROM landkarte')
    elif fehlt == 'Referenzlast': monkeypatch.setattr(L, '_referenzlast', lambda *a: None)
    else: con.execute('DELETE FROM vertraege_explizit')
    with pytest.raises(V.VorspannFehler, match=fehlt):
        V.ausfuehren(con, 1)
    assert raw['reihenfolge'] == []


def _unit_sperre(raw, bereich):
    r = raw['rauschen']
    r['gesperrt'].append(bereich)
    r['toleranz'].pop(bereich)
    r['bereiche'][bereich].update(toleranz=1.7, gesperrt=True, meldung='Unit: Messproblem')
    r['lauf_startet'] = len(r['gesperrt']) < len(r['bereiche'])


def test_unit_teilrauschen_wird_an_eichproben_weitergegeben(unit_vorspann):
    con, raw = unit_vorspann
    _unit_sperre(raw, 'beta')
    r = V.ausfuehren(con, 1)
    tausch = raw['probe_aufrufe'][0][0][10]
    assert tausch['_rauschtoleranz'] == {'alpha':1.2}
    assert tausch['_gesperrte_bereiche'] == ['beta']
    assert r['rauschen']['bereiche']['beta']['toleranz'] == 1.7


@pytest.mark.parametrize('fehler', ['alle','fehlt','nan','inf','bool','negativ','zu_gross','zu_klein','widerspruch','zu_wenig_rohwerte','aussetzer','basis'])
def test_unit_unbrauchbare_messung_liefert_keinen_nachweis(unit_vorspann, monkeypatch, fehler):
    con, raw = unit_vorspann
    r = raw['rauschen']
    if fehler == 'alle':
        _unit_sperre(raw, 'alpha'); _unit_sperre(raw, 'beta')
    elif fehler == 'fehlt': r['toleranz'].pop('beta')
    elif fehler in ('nan','inf','bool','negativ','zu_gross','zu_klein'):
        r['toleranz']['alpha'] = {'nan':float('nan'),'inf':float('inf'),'bool':True,'negativ':-1,'zu_gross':1.51,'zu_klein':1.1}[fehler]
    elif fehler == 'widerspruch': r['bereiche']['alpha']['gesperrt'] = True
    elif fehler == 'zu_wenig_rohwerte': r['bereiche']['alpha']['werte'].pop()
    elif fehler == 'aussetzer': r['bereiche']['alpha']['nachmessen'] = True
    else: monkeypatch.setattr(L.messgeraet,'messen',lambda *a,**kw: {'gueltig':False,'grund':'Unit-Kammerfehler'})
    with pytest.raises(V.VorspannFehler, match='Rausch|Messung'):
        V.ausfuehren(con, 1)
    assert raw['probe_aufrufe'] == []
    with pytest.raises(V.VorspannFehler): V.verlangen(con, 1, 'gen0')


def test_unit_nachweis_bindet_vollstaendiges_instrument_und_quellen(unit_vorspann):
    con, raw = unit_vorspann
    r = V.ausfuehren(con, 1)
    q = r['quellen']
    root = Path(L.__file__).resolve().parents[1]
    erwartet = {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
                for p in (root / 'biotop').rglob('*.py')}
    erwartet['kammer/Dockerfile'] = hashlib.sha256((root / 'kammer/Dockerfile').read_bytes()).hexdigest()
    assert q['instrument']['dateien'] == erwartet
    assert q['instrument']['infrastruktur']['image_id'] == 'sha256:' + 'a'*64
    assert q['werk']['id'] == 1
    assert q['verfassung']['quelle'] == 'Unit-Verfassung'
    assert q['referenzlast']['sha256'] == hashlib.sha256(b'# Unit-Referenzlast').hexdigest()


@pytest.mark.parametrize('geaendert', ['python','neue_datei','dockerfile','image','referenzlast','verfassung','werk','daten','protokoll'])
def test_unit_messgeraetwechsel_oder_manipulation_sperrt_dauerhaft(unit_vorspann, monkeypatch, tmp_path, geaendert):
    import shutil
    con, raw = unit_vorspann
    root = tmp_path / 'instrument'
    source = Path(L.__file__).resolve().parents[1]
    shutil.copytree(source / 'biotop', root / 'biotop')
    shutil.copytree(source / 'kammer', root / 'kammer')
    monkeypatch.setattr(V, 'WURZEL', root, raising=False)
    r = V.ausfuehren(con, 1)
    datei = None
    if geaendert in ('python','neue_datei','dockerfile'):
        datei = root / {'python':'biotop/organe/aegis.py','neue_datei':'biotop/zusaetzlich.py','dockerfile':'kammer/Dockerfile'}[geaendert]
        alt = datei.read_text() if datei.exists() else None
        datei.write_text((alt or '') + '\n# Unit-Aenderung\n')
    elif geaendert == 'image': monkeypatch.setattr(V, '_infrastruktur', lambda: {'image':'unit:1','image_id':'sha256:'+'b'*64})
    elif geaendert == 'referenzlast': monkeypatch.setattr(L,'_referenzlast',lambda *a:'# andere Last')
    elif geaendert == 'verfassung': con.execute("UPDATE verfassung_werk SET regeln='{}'")
    elif geaendert == 'werk': con.execute("UPDATE werke SET pfad=pfad || '/anderes'")
    elif geaendert == 'daten':
        z = lj(con.execute('SELECT ergebnis FROM vorspann_nachweise').fetchone()[0]); z['rauschen']['toleranz']['alpha'] = 1.4
        con.execute('UPDATE vorspann_nachweise SET ergebnis=?', (j(z),))
    else: con.execute("UPDATE protokoll SET inhalt='{}' WHERE art='vorspann.bestanden'")
    with pytest.raises(V.VorspannFehler, match='Satz 2'):
        V.verlangen(con, 1, 'gen0')
    if datei:
        if alt is None: datei.unlink()
        else: datei.write_text(alt)
    with pytest.raises(V.VorspannFehler, match='neue[rn]? Lauf'):
        V.verlangen(con, 1, 'gen0')
    with pytest.raises(V.VorspannFehler, match='neue[rn]? Lauf'):
        V.ausfuehren(con, 1)


def test_unit_quellenwechsel_waehrend_der_eichung_erzeugt_keinen_nachweis(unit_vorspann, monkeypatch):
    con, raw = unit_vorspann
    original = eichproben.proben
    def veraendert(*a, **kw):
        r = original(*a, **kw)
        monkeypatch.setattr(L, '_referenzlast', lambda *a:'# waehrend Eichung geaendert')
        return r
    monkeypatch.setattr(eichproben, 'proben', veraendert)
    with pytest.raises(V.VorspannFehler, match='Satz 2'): V.ausfuehren(con, 1)
    with pytest.raises(V.VorspannFehler): V.verlangen(con, 1, 'gen0')


@pytest.mark.parametrize('image_id,rc', [('sha256:'+'c'*64,0),('',1),('not-an-id',0)])
def test_unit_kammer_image_id_wird_tatsaechlich_abgefragt(monkeypatch, image_id, rc):
    import subprocess
    from types import SimpleNamespace
    calls = []
    def inspect(cmd, **kw):
        calls.append((cmd,kw))
        return SimpleNamespace(returncode=rc, stdout=image_id+'\n', stderr='Unit-Docker')
    monkeypatch.setattr(subprocess, 'run', inspect)
    assert callable(getattr(V, '_infrastruktur', None)), 'Image-ID-Bindung fehlt'
    if rc or not image_id.startswith('sha256:'):
        with pytest.raises(ValueError, match='Kammer'): V._infrastruktur()
    else:
        assert V._infrastruktur()['image_id'] == image_id
    assert calls[0][0][:3] == ['docker','image','inspect']
    assert calls[0][1]['timeout'] > 0


@pytest.fixture
def unit_laufstufen(unit_vorspann, monkeypatch, request):
    """Nur Ablauf-UNIT-Test, weder Mutantenfang noch Kammer-Schnappschuss."""
    con, raw = unit_vorspann
    mutanten = [{'quelle':'Unit','datei':'paket/alpha/__init__.py','zeile':1,'beschreibung':str(i)} for i in range(5)]
    monkeypatch.setattr(G0,'erzeugen',lambda *a:copy.deepcopy(mutanten))
    monkeypatch.setattr(G0,'aequivalenz_pruefen',lambda *a:None)
    monkeypatch.setattr(G0,'messen',lambda *a: {'nicht_aequivalent':5,'gefangen':5,'blind':[]})
    monkeypatch.setattr(L.lazarus,'schnappschuss',lambda *a: {'tag':'Unit','pruefsumme':'0'*64})
    raw['generation_koerper'] = L._generation_koerper
    monkeypatch.setattr(L,'_generation_koerper',lambda *a,**kw: {'unit_generation_betreten':True})
    for b in getattr(request, 'param', []): _unit_sperre(raw, b)
    V.ausfuehren(con, 1)
    return con, raw


def test_unit_vollstaendiger_ablauf_bis_generation(unit_laufstufen):
    con, raw = unit_laufstufen
    assert L.generation0(con, 1, None, .8)['erreicht'] is True
    r = L.mass_einfrieren(con, 1, 'Unit')
    z = con.execute('SELECT * FROM vorspann_nachweise').fetchone()
    assert r['mass']['vorspann_sha256'] == z['nachweis_sha256']
    assert z['mass_sha256'] == hashlib.sha256(j(r['mass']).encode()).hexdigest()
    assert L.generation(con, 1)['unit_generation_betreten'] is True


@pytest.mark.parametrize('falsch', ['mass_vor_gen0','gen0_nach_mass','mass_zweimal','mass_geaendert','mass_ohne_bindung'])
def test_unit_stufenfolge_und_eingefrorenes_mass_sind_verbindlich(unit_laufstufen, falsch):
    con, raw = unit_laufstufen
    if falsch != 'mass_vor_gen0':
        L.generation0(con, 1, None, .8)
        L.mass_einfrieren(con, 1, 'Unit')
    if falsch == 'mass_geaendert':
        m = lj(L._lauf(con,1)['mass']); m['grenzen']['laufzeit_faktor'] = 100
        con.execute('UPDATE laeufe SET mass=?', (j(m),))
    if falsch == 'mass_ohne_bindung': con.execute('UPDATE vorspann_nachweise SET mass_sha256=NULL')
    vorher = L._lauf(con, 1)['mass']
    with pytest.raises(L.LaufFehler, match='Vorspann'):
        if falsch == 'gen0_nach_mass': L.generation0(con,1,None,.8)
        elif falsch.startswith('mass_vor') or falsch == 'mass_zweimal': L.mass_einfrieren(con,1,'Unit-erneut')
        else: L.generation(con,1)
    assert L._lauf(con, 1)['mass'] == vorher


@pytest.mark.parametrize('unit_laufstufen', [['beta']], indirect=True)
def test_unit_generation_reicht_validierte_rauschwerte_durch(unit_laufstufen, monkeypatch):
    con, raw = unit_laufstufen
    L.generation0(con,1,None,.8); L.mass_einfrieren(con,1,'Unit')
    gesehen = []
    def koerper(*args):
        gesehen.append(args[12]); return {}
    monkeypatch.setattr(L, '_generation_koerper', koerper)
    L.generation(con,1)
    assert gesehen[0]['_rauschtoleranz'] == {'alpha':1.2}
    assert gesehen[0]['_gesperrte_bereiche'] == ['beta']


@pytest.mark.parametrize('unit_laufstufen', [['beta']], indirect=True)
def test_unit_gesperrter_bereich_erzeugt_keine_kandidaten_und_protokolliert_skip(unit_laufstufen, monkeypatch):
    con, raw = unit_laufstufen
    L.generation0(con,1,None,.8); L.mass_einfrieren(con,1,'Unit')
    monkeypatch.setattr(L, '_generation_koerper', raw['generation_koerper'])
    erzeugt = []
    monkeypatch.setattr(L.genesis, 'erzeugen', lambda *a,**kw: erzeugt.append(a[6]) or [])
    monkeypatch.setattr(L.entropie, 'messen', lambda *a: {})
    monkeypatch.setattr(L.entropie, 'pruefen_und_beenden', lambda *a: None)
    L.generation(con,1)
    assert erzeugt and set(erzeugt) == {'alpha'}
    skips = [lj(z[0]) for z in con.execute("SELECT inhalt FROM protokoll WHERE art='generation.bereich_uebersprungen'")]
    assert len(skips) == 1 and skips[0]['bereich'] == 'beta'
    assert skips[0]['toleranz'] == 1.7
    assert len(skips[0]['nachweis_sha256']) == 64


@pytest.mark.parametrize('unit_laufstufen', [['beta']], indirect=True)
@pytest.mark.parametrize('fall', ['nachbarfehler', 'nur_gesperrtes_rauschen'])
def test_unit_generalprobe_nimmt_wirkungskreisunion_aber_pareto_alle_bereiche(unit_laufstufen, monkeypatch, messung, fall):
    con, raw = unit_laufstufen
    L.generation0(con,1,None,.8); L.mass_einfrieren(con,1,'Unit')
    monkeypatch.setattr(L, '_generation_koerper', raw['generation_koerper'])
    monkeypatch.setattr(L.entropie, 'messen', lambda *a: {})
    monkeypatch.setattr(L.entropie, 'pruefen_und_beenden', lambda *a: None)
    def einzel(*a, **kw):
        kid = a[3]
        m = messung(); m['_dateien'] = {}
        con.execute("UPDATE kandidaten SET status='ueberlebt',masse=?,wirkungskreis=? WHERE id=?", (j(m),j(['alpha']),kid))
        return {'kandidat':kid, 'status':'ueberlebt','grund':'Unit-Einzelurteil', 'mass':{'zuwachs':1}, 'wirkungskreis':['alpha']}
    monkeypatch.setattr(L.aegis, 'pruefen', einzel)
    basis = messung(sicherheit_punkte=2)
    kandidat = messung(sicherheit_punkte=1); kandidat['bereiche']['beta']['tests_fehlgeschlagen'] = 1
    if fall == 'nur_gesperrtes_rauschen':
        basis = messung(); kandidat = messung(); kandidat['bereiche']['beta']['laufzeit_ms'] = 50
    paar = iter([basis, kandidat])
    monkeypatch.setattr(L.messgeraet, 'messen', lambda *a,**kw: next(paar))
    gesehen = []
    echt = L.messgeraet.urteil_f2
    def urteil(*a, **kw):
        gesehen.append(a); return echt(*a,**kw)
    monkeypatch.setattr(L.messgeraet, 'urteil_f2', urteil)
    r = L.generation(con,1, einschleusen=[{'bereich':b,'diff':'Unit-ersetzt Einzelprüfung'} for b in ['alpha','beta']])
    assert gesehen[0][3] == ['alpha','beta'], 'Pareto darf Nebenbereiche nicht ausblenden'
    assert gesehen[0][4] == ['alpha'], 'nicht pauschal alle Bereiche als Wirkungskreis'
    assert r['status'] == 'abgelehnt'
    assert ('beta.tests_fehlgeschlagen' if fall == 'nachbarfehler' else 'Kernmaß unverändert') in r['grund']
    assert con.execute("SELECT count(*) FROM kandidaten WHERE bereich='beta'").fetchone()[0] == 0


def test_unit_verhandlung_erzeugt_keine_kandidaten_im_gesperrten_nachbarn(unit_vorspann, monkeypatch, messung):
    con, raw = unit_vorspann
    con.execute("INSERT INTO kandidaten(id,lauf_id,bereich,diff,begruendung,vertraege,status) VALUES(1,1,'alpha','Unit','Unit','test_vertrag_alpha_beta','abgelehnt')")
    def verboten(*a,**kw): pytest.fail('Schwarm darf im gesperrten Nachbarn keine Modelle rufen')
    monkeypatch.setattr(L.genesis, 'erzeugen', verboten)
    monkeypatch.setattr(L.aegis, 'kandidat_dateien', lambda *a:{})
    werk = L._werk(con,1)
    tausch = {'_gesperrte_bereiche':['beta'], '_rauschtoleranz':{'alpha':1.2}}
    u = {'status':'abgelehnt','grund':'Vertrag verletzt', 'vertrag_verletzt':['test_vertrag_alpha_beta.py::test_vertrag']}
    r = L._verhandeln(con,1,werk,1,Path(werk['pfad']),'paket',['alpha','beta'],[],messung(),messung(),None,tausch,'alpha',1,u)
    assert r['status'] == 'abgelehnt' and 'gesperrt' in r['grund']
    assert con.execute("SELECT count(*) FROM protokoll WHERE art='generation.bereich_uebersprungen'").fetchone()[0] == 1


@pytest.mark.parametrize('wechsel', ['anderes_probenziel','datei_geaendert'])
def test_unit_eichgegenstand_bleibt_waehrend_proben_versiegelt(unit_vorspann, monkeypatch, wechsel):
    con, raw = unit_vorspann
    original = eichproben.proben
    def verschoben(*a, **kw):
        r = original(*a, **kw)
        if wechsel == 'anderes_probenziel': r['gegenstand']['vertrag_pruefsumme'] = 'f'*64
        else:
            werk = Path(L._werk(con,1)['pfad'])
            (werk / r['gegenstand']['vertrag_pfad']).write_text('# verändert während Eichung')
        return r
    monkeypatch.setattr(eichproben, 'proben', verschoben)
    with pytest.raises(V.VorspannFehler, match='Eichgegenstand'):
        V.ausfuehren(con,1)
    with pytest.raises(V.VorspannFehler): V.verlangen(con,1,'gen0')


def test_unit_eichausgang_wird_getrennt_in_eichkosten_erfasst(unit_vorspann):
    con, raw = unit_vorspann
    r = V.ausfuehren(con,1)
    zeile = con.execute("SELECT * FROM eichkosten WHERE lauf_id=1 AND teil='eichausgang'").fetchone()
    assert zeile is not None, 'zusätzliche Basis-Messung darf nicht aus der Eichkostenbilanz fallen'
    assert zeile['kammerlaeufe'] == 1
    assert zeile['modellaufrufe'] == 0 and zeile['kosten_eur'] == 0.0
    assert r['kosten'] == eichung.kosten(con,1)


def test_unit_probenkosten_aus_privater_rueckgabe_werden_getrennt_gebucht(unit_vorspann):
    con, raw = unit_vorspann
    r = V.ausfuehren(con,1)
    erfasst = {z['teil']:dict(z) for z in con.execute("SELECT * FROM eichkosten WHERE teil LIKE 'probe.%' OR teil LIKE 'gegenprobe.%'")}
    erwartet = {f'{prefix}.{name}':e for gruppe,prefix in [('proben','probe'),('gegenproben','gegenprobe')]
                for name,e in raw['proben'][gruppe].items()}
    assert set(erfasst) == set(erwartet)
    for teil,e in erwartet.items():
        assert erfasst[teil]['kammerlaeufe'] == e['kammerlaeufe']
        assert erfasst[teil]['kosten_eur'] == e['kosten_eur']
    assert r['kosten']['kammerlaeufe'] == 1 + sum(e['kammerlaeufe'] for e in erwartet.values())


def test_referenzlast_gehoert_zur_geladenen_repositorykopie():
    assert L.REFERENZLAST == Path(L.__file__).resolve().parent / 'kern/referenzlast'


def test_gate_verweigerung_hat_phasenbezogenen_protokollbeleg(db_lauf):
    with pytest.raises(V.VorspannFehler): V.verlangen(db_lauf,1,'gen0')
    e = db_lauf.execute("SELECT inhalt FROM protokoll WHERE art='vorspann.verweigert'").fetchone()
    assert e is not None
    assert lj(e[0])['phase'] == 'gen0' and lj(e[0])['lauf_id'] == 1
    assert 'Nachweis fehlt' in lj(e[0])['grund']


def test_generation_ohne_vorspann_startet_nicht(db_lauf, monkeypatch):
    betreten = []
    monkeypatch.setattr(L, "_generation_koerper", lambda *a, **kw: betreten.append(True))
    with pytest.raises(L.LaufFehler, match="Vorspann"):
        L.generation(db_lauf, 1)
    assert betreten == []
    assert db_lauf.execute("SELECT count(*) FROM generationen WHERE nummer>0").fetchone()[0] == 0


@pytest.mark.parametrize("phase", ["mass", "gen0"])
def test_vorstufen_ohne_vorspann_starten_nicht(db_lauf, monkeypatch, phase):
    def unerlaubt(*args, **kwargs):
        pytest.fail("Messung ohne gültigen Vorspann begonnen")
    monkeypatch.setattr(L, "_referenzlast", lambda *a: "# Referenzlast")
    monkeypatch.setattr(L.messgeraet, "messen", unerlaubt)
    monkeypatch.setattr(G0, "erzeugen", unerlaubt)
    with pytest.raises(L.LaufFehler, match="Vorspann"):
        if phase == "mass":
            L.mass_einfrieren(db_lauf, 1, "Eigen-Test")
        else:
            L.generation0(db_lauf, 1, None, 0.8)
