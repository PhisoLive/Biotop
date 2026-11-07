"""Verbindliche Generation minus eins; ein Kernpfad für CLI und Prüfskript."""
from __future__ import annotations

import hashlib
import math
import re
import subprocess
import time
from pathlib import Path

from ..kern import messgeraet, protokoll
from ..kern.datenbank import j, lj, transaktion
from . import eichgegenstand, eichproben, eichung, fundpruefung, landkarte, verfassung, vertraege, kammer

WURZEL = Path(__file__).resolve().parents[2]


class VorspannFehler(RuntimeError):
    pass


def _tabelle(con):
    con.execute("""CREATE TABLE IF NOT EXISTS vorspann_nachweise (
        lauf_id INTEGER PRIMARY KEY, status TEXT NOT NULL, ergebnis TEXT,
        nachweis_sha256 TEXT, protokoll_nr INTEGER, mass_sha256 TEXT)""")


def _sha(obj):
    return hashlib.sha256(j(obj).encode()).hexdigest()


def _infrastruktur():
    p = subprocess.run(['docker', 'image', 'inspect', '--format', '{{.Id}}', kammer.IMAGE],
                       capture_output=True, text=True, timeout=15)
    image_id = p.stdout.strip()
    if p.returncode != 0 or not re.fullmatch(r'sha256:[0-9a-f]{64}', image_id):
        raise ValueError(f'Kammer-Image nicht identifizierbar: {kammer.IMAGE}: {p.stderr}')
    return {'image':kammer.IMAGE, 'image_id':image_id,
            'speicher':kammer.SPEICHER, 'zeitlimit_s':kammer.ZEITLIMIT_S}


def _quellen(con, lauf_id):
    from .. import lauf as L
    lauf = L._lauf(con, lauf_id)
    werk = L._werk(con, lauf['werk_id'])
    paket = lj(werk['bericht'])['paket']
    ref = L._referenzlast(werk['name'], paket)
    if not ref:
        raise ValueError('Referenzlast fehlt')
    dateien = {str(p.relative_to(WURZEL)):hashlib.sha256(p.read_bytes()).hexdigest()
               for p in sorted((WURZEL / 'biotop').rglob('*.py'))}
    dateien['kammer/Dockerfile'] = hashlib.sha256((WURZEL / 'kammer/Dockerfile').read_bytes()).hexdigest()
    instrument = {'dateien':dateien, 'infrastruktur':_infrastruktur()}
    return {'instrument':instrument, 'instrument_sha256':_sha(instrument),
            'werk':{k:werk[k] for k in ('id','name','pfad','bericht')},
            'bereiche':landkarte.bereiche_finden(Path(werk['pfad']), paket),
            'verfassung':verfassung.lesen(con, werk['id']),
            'referenzlast':{'sha256':hashlib.sha256(ref.encode()).hexdigest(),
                           'suche':[werk['name'],paket], 'wurzel':str(L.REFERENZLAST.resolve())}}


def _fehler(lauf_id, grund):
    return VorspannFehler(f'Vorspann Lauf {lauf_id}: {grund} — neuer Lauf erforderlich (Satz 2), keine Nacheichung')


def _qualitaet(p):
    erwartet = {'nebenwirkung', 'regression', 'norm', 'vertrag'}
    zahlen = {}
    for gruppe, soll, name in (('proben', True, 'positive'), ('gegenproben', False, 'negative')):
        es = p.get(gruppe) or {}
        zahlen[name] = sum(isinstance(e, dict) and e.get('ausgefuehrt') is True
                           and e.get('pruefbar') is True and e.get('bestanden') is soll
                           for e in es.values())
        if set(es) != erwartet or zahlen[name] != 4:
            raise ValueError(f'{gruppe}: nicht genau vier ausgeführte, prüfbare Kontrollen mit Sollurteil {soll}')
    if p.get('bestanden') is not True:
        raise ValueError('Eichproben-Gesamturteil nicht bestanden')
    return dict(zahlen, erwartet_je=4)


def _rauschwerte(r, bereiche):
    """Vollständige, endliche Bereichswerte; keine Rückfalltoleranz im Lauf."""
    gesperrt = r.get('gesperrt') or []
    toleranz = r.get('toleranz') or {}
    es = r.get('bereiche') or {}
    if (set(es) != set(bereiche) or len(gesperrt) != len(set(gesperrt))
            or not set(gesperrt) <= set(bereiche)
            or set(toleranz) != set(bereiche) - set(gesperrt)):
        raise ValueError('Rauschmessung unvollständig oder widersprüchlich')
    for b, e in es.items():
        if e.get('gesperrt') is not (b in gesperrt):
            raise ValueError(f'Rauschmessung {b}: widersprüchliche Sperre')
        if b in gesperrt:
            continue
        t = toleranz[b]
        werte = e.get('werte') or []
        if (type(t) not in (int, float) or not math.isfinite(t) or not 1.15 <= t <= 1.5
                or t != e.get('toleranz') or e.get('meldung') or e.get('nachmessen')
                or len(werte) != 5 or any(type(w) not in (int, float) or not math.isfinite(w) or w <= 0 for w in werte)):
            raise ValueError(f'Rauschmessung {b}: keine brauchbare Toleranz samt fünf Rohwerten')
    if not toleranz or r.get('lauf_startet') is not True:
        raise ValueError('Rauschmessung: alle Bereiche gesperrt oder Start verweigert')
    return {'_rauschtoleranz': dict(toleranz), '_gesperrte_bereiche': sorted(gesperrt)}


def ausfuehren(con, lauf_id):
    """Eichen vor gen0 und Maß. Rohdaten bleiben im Nachweis und im Protokoll."""
    _tabelle(con)
    with transaktion(con):
        if con.execute('SELECT 1 FROM vorspann_nachweise WHERE lauf_id=?', (lauf_id,)).fetchone():
            raise _fehler(lauf_id, 'bereits ein Eichversuch unter dieser ID')
        con.execute("INSERT INTO vorspann_nachweise(lauf_id,status) VALUES(?,'laeuft')", (lauf_id,))
    r = {'lauf_id':lauf_id, 'generation':-1, 'erstellt_am':protokoll.jetzt(),
         'regel':'F6 3.5; Verfassungssatz 2: neues Messgerät verlangt neuen Lauf'}
    try:
        return _ausfuehren(con, lauf_id, r)
    except Exception as e:
        with transaktion(con):
            con.execute("UPDATE vorspann_nachweise SET status='gescheitert',ergebnis=?,nachweis_sha256=NULL WHERE lauf_id=?",
                        (j(r), lauf_id))
        protokoll.schreiben(con, 'vorspann.gescheitert', lauf_id=lauf_id, grund=str(e), ergebnis=r)
        raise _fehler(lauf_id, str(e)) from e


def _ausfuehren(con, lauf_id, r):
    from .. import lauf as L
    lauf = L._lauf(con, lauf_id)
    alt = con.execute('SELECT 1 FROM generationen WHERE lauf_id=?', (lauf_id,)).fetchone()
    gen0_alt = any(lj(z['inhalt']).get('lauf_id') == lauf_id for z in con.execute(
        "SELECT inhalt FROM protokoll WHERE art LIKE 'generation0.%'"))
    if lauf['mass'] is not None or alt or gen0_alt or lauf['status'] not in ('aufgenommen', 'kartiert'):
        raise ValueError('kein frischer Lauf vor Generation minus eins')
    werk = L._werk(con, lauf['werk_id'])
    pfad = Path(werk['pfad'])
    paket = lj(werk['bericht'])['paket']
    bereiche = landkarte.bereiche_finden(pfad, paket)
    ref = L._referenzlast(werk['name'], paket)
    verf = verfassung.lesen(con, werk['id'])
    if verf is None:
        raise ValueError('Verfassung fehlt')
    if not ref:
        raise ValueError('Referenzlast fehlt')
    if not bereiche or not con.execute('SELECT 1 FROM landkarte WHERE werk_id=?', (werk['id'],)).fetchone():
        raise ValueError('Landkarte fehlt')
    if not vertraege.alle(con, werk['id']):
        raise ValueError('Verträge fehlen')
    kanten = [tuple(z) for z in con.execute('SELECT von,nach,art FROM strassen WHERE werk_id=?', (werk['id'],))]
    tausch = dict(verf['regeln'].get('tausch') or {})
    r['werk_id'] = werk['id']
    r['quellen'] = _quellen(con, lauf_id)
    r['rauschen'] = eichung.rauschmessung(con, lauf_id, werk['id'], pfad, bereiche, paket, ref)
    tausch.update(_rauschwerte(r['rauschen'], bereiche))
    r['gegenstand'] = eichgegenstand.sichern(con, werk['id'], lauf_id, pfad)
    if not r['gegenstand'].get('gegenstand'):
        raise ValueError('Eichgegenstand fehlt: ' + str(r['gegenstand'].get('befund')))
    t0 = time.monotonic()
    r['funde'] = fundpruefung.bewerten(con, werk['id'], lauf_id, pfad)
    eichung.kosten_buchen(con, lauf_id, werk['id'], 'fundpruefung', r['funde']['kammerlaeufe'],
                         time.monotonic()-t0, modellaufrufe=0, kosten_eur=0.0)
    t0 = time.monotonic()
    r['basis'] = messgeraet.messen(pfad, bereiche, paket, ref)
    # messen() führt genau einen Kammeraufruf aus; keine Modelle. Auch ungültige Rückgaben kosten diesen Lauf.
    eichung.kosten_buchen(con, lauf_id, werk['id'], 'eichausgang', 1, time.monotonic()-t0,
                         modellaufrufe=0, kosten_eur=0.0)
    if r['basis'].get('gueltig') is not True or r['basis'].get('werk', {}).get('baut') is not True:
        raise ValueError('Messung des Eich-Ausgangs ungültig: ' + str(r['basis'].get('grund')))
    r['eichproben'] = eichproben.proben(con, lauf_id, werk['id'], pfad, paket, bereiche,
                                      landkarte.bereichs_strassen(kanten, paket), r['basis'], r['basis'], ref,
                                      tausch, generation=-1)
    p = r['eichproben']
    # Proben isolieren ihre Datenbank; die gemessenen Kosten kommen als Rohdaten zurück.
    for gruppe, prefix in (('proben', 'probe'), ('gegenproben', 'gegenprobe')):
        for name, e in (p.get(gruppe) or {}).items():
            eichung.kosten_buchen(con, lauf_id, werk['id'], f'{prefix}.{name}', e['kammerlaeufe'],
                                 e['dauer_s'], modellaufrufe=e['modellaufrufe'], kosten_eur=e['kosten_eur'])
    gegenstand = r['gegenstand']['gegenstand']
    datei = pfad / gegenstand['vertrag_pfad']
    if (p.get('gegenstand') != gegenstand or eichgegenstand.lesen(con, werk['id']) != gegenstand
            or not datei.is_file() or hashlib.sha256(datei.read_bytes()).hexdigest() != gegenstand['vertrag_pruefsumme']):
        raise ValueError('Eichgegenstand während der Proben verändert oder andere Probequelle')
    r['qualitaet'] = _qualitaet(p)
    if _quellen(con, lauf_id) != r['quellen']:
        raise ValueError('Messgerät/Quellen während der Eichung verändert (Satz 2)')
    r['kosten'] = eichung.kosten(con, lauf_id)
    digest = _sha(r)
    nr = protokoll.schreiben(con, 'vorspann.bestanden', lauf_id=lauf_id, nachweis_sha256=digest, ergebnis=r)
    with transaktion(con):
        con.execute("UPDATE vorspann_nachweise SET status='bestanden',ergebnis=?,nachweis_sha256=?,protokoll_nr=? WHERE lauf_id=?",
                    (j(r), digest, nr, lauf_id))
    return dict(r, nachweis_sha256=digest)


def mass_binden(con, lauf_id, mass):
    """In derselben Transaktion wie laeufe.mass schreiben: genau einmal, nie ersetzen."""
    digest = _sha(mass)
    cur = con.execute("""UPDATE vorspann_nachweise SET mass_sha256=?
        WHERE lauf_id=? AND status='bestanden' AND mass_sha256 IS NULL AND nachweis_sha256=?
        AND NOT EXISTS(SELECT 1 FROM laeufe WHERE id=? AND mass IS NOT NULL)""",
        (digest, lauf_id, mass['vorspann_sha256'], lauf_id))
    if cur.rowcount != 1:
        raise _fehler(lauf_id, 'Maß bereits gebunden oder Nachweis fehlt')
    return digest


def verlangen(con, lauf_id, phase):
    """Jeder Eingang verlangt den versiegelten Nachweis und protokolliert seine Verweigerung."""
    try:
        return _verlangen(con, lauf_id, phase)
    except VorspannFehler as e:
        protokoll.schreiben(con, 'vorspann.verweigert', lauf_id=lauf_id, phase=phase, grund=str(e))
        raise


def _verlangen(con, lauf_id, phase):
    from .. import lauf as L
    _tabelle(con)
    z = con.execute('SELECT * FROM vorspann_nachweise WHERE lauf_id=?', (lauf_id,)).fetchone()
    if z is None or z['status'] != 'bestanden' or not z['nachweis_sha256']:
        raise _fehler(lauf_id, f'Nachweis fehlt oder unbrauchbar — {phase} startet nicht')
    lauf = L._lauf(con, lauf_id)
    if phase not in ('gen0', 'mass', 'generation'):
        raise _fehler(lauf_id, f'unbekannte Phase {phase}')
    if phase in ('gen0', 'mass'):
        if lauf['mass'] is not None or z['mass_sha256'] or con.execute(
                'SELECT 1 FROM generationen WHERE lauf_id=?', (lauf_id,)).fetchone():
            raise _fehler(lauf_id, f'{phase} nach eingefrorenem Maß/Generation verboten')
        if phase == 'mass' and not any(lj(e['inhalt']).get('lauf_id') == lauf_id for e in con.execute(
                "SELECT inhalt FROM protokoll WHERE art='generation0.ergebnis' AND nr>?", (z['protokoll_nr'],))):
            raise _fehler(lauf_id, 'Generation 0 vor dem Maß nicht abgeschlossen')
    if phase == 'generation' and lauf['mass'] is None:
        raise _fehler(lauf_id, 'eingefrorenes Maß fehlt')
    try:
        r = lj(z['ergebnis'])
        if _sha(r) != z['nachweis_sha256'] or r['lauf_id'] != lauf_id:
            raise ValueError('Nachweis-Prüfsumme oder Laufzuordnung verändert')
        e = con.execute('SELECT * FROM protokoll WHERE nr=?', (z['protokoll_nr'],)).fetchone()
        if (not e or e['art'] != 'vorspann.bestanden' or not protokoll.pruefen(con)[0]
                or lj(e['inhalt']).get('ergebnis') != r
                or lj(e['inhalt']).get('nachweis_sha256') != z['nachweis_sha256']):
            raise ValueError('Protokollquelle des Nachweises fehlt oder verändert')
        if _quellen(con, lauf_id) != r['quellen']:
            raise ValueError('Messgerät/Quellen verändert; alter Nachweis ungültig')
        if _qualitaet(r['eichproben']) != r['qualitaet']:
            raise ValueError('Qualitätsbeleg verändert')
        _rauschwerte(r['rauschen'], r['quellen']['bereiche'])
        if phase == 'generation':
            mass = lj(lauf['mass'])
            if (not z['mass_sha256'] or _sha(mass) != z['mass_sha256']
                    or mass.get('vorspann_sha256') != z['nachweis_sha256']):
                raise ValueError('eingefrorenes Maß fehlt, wurde ersetzt oder verändert')
            gebunden = any(lj(e['inhalt']).get('lauf_id') == lauf_id
                           and lj(e['inhalt']).get('mass_sha256') == z['mass_sha256']
                           and lj(e['inhalt']).get('vorspann_sha256') == z['nachweis_sha256']
                           for e in con.execute("SELECT inhalt FROM protokoll WHERE art='mass.eingefroren' AND nr>?",
                                                (z['protokoll_nr'],)))
            if not gebunden:
                raise ValueError('Quellbeleg der Maßbindung fehlt')
    except Exception as e:
        with transaktion(con):
            con.execute("UPDATE vorspann_nachweise SET status='ungueltig' WHERE lauf_id=?", (lauf_id,))
        protokoll.schreiben(con, 'vorspann.ungueltig', lauf_id=lauf_id, phase=phase, grund=str(e),
                            nachweis_sha256=z['nachweis_sha256'], regel='Satz 2: neuer Lauf, keine Nachkorrektur')
        raise _fehler(lauf_id, str(e)) from e
    return dict(r, nachweis_sha256=z['nachweis_sha256'])
