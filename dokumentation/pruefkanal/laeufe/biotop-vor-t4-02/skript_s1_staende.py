"""S1 nach Entscheidung Chat-Claude (1): Weißraum gehört zur Tarifsprache, soweit die versiegelte Normalversion ihn rechnet.
Dieselbe Messung wie laeufe/biotop-vor-t4/s1 (s1_harness.mjs unverändert übernommen), jetzt für:
  k3044        Vorgeneration lauf38-gen0  gegen  lauf38-gen0 + Diff K3044 (S1-Behebung Lauf 38, Gen 1)
  endstand38   lauf38-gen0                gegen  lauf38-gen16 (Endstand Lauf 38)
  endstand37   lauf37-gen2                gegen  lauf37-gen8  (Endstand Lauf 37)
  k2868        lauf37-gen2                gegen  lauf37-gen2 + Diff K2868 (Wiederholung der Vorrunde, Gleichheitsprobe)
Regel (vorab, aus der Entscheidung): S1 gilt an einem Stand als sauber behoben nur, wenn (a) der versiegelte Marker
0-mal ausgeführt wird (O) und (b) der Stand jeden Ausdruck, den die Normalversion rechnet, gleich rechnet — gemessen an
K (Leerzeichen) und W (Tab, Zeilenumbruch). Kein Modellaufruf; t3.db nur gelesen (sha256 vorher/nachher).
Aufruf: python s1_staende.py [fall …]"""
import hashlib
import json
import shutil
import sqlite3
import sys
import tarfile
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.organe import aegis, kammer, lazarus  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
A = Path('/root/biotop-vor-t4-02/s1')
HARNESS = Path('/root/biotop-vor-t4/s1/s1_harness.mjs').read_text()
DB = '/root/biotop-t3/schnappschuss-abschluss3/t3.db'
REL = ['src/tarife/ausdruck.ts', 'src/tarife/modell.ts', 'src/zahlen/pruefen.ts']
FAELLE = {'k3044': ((38, 0), (38, 0), 3044), 'endstand38': ((38, 0), (38, 16), None),
          'endstand37': ((37, 2), (37, 8), None), 'k2868': ((37, 2), (37, 2), 2868)}
db_vorher = hashlib.sha256(Path(DB).read_bytes()).hexdigest()
c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
c.row_factory = sqlite3.Row
with tarfile.open('/root/versiegelt/t3-versandwerk/normalversion.tar.gz') as t:
    norm = {r: t.extractfile(f'versandwerk/{r}').read().decode() for r in REL}


def stand(lauf, gen):
    z = c.execute('SELECT archiv, pruefsumme FROM lazarus WHERE lauf_id=? AND generation=?', (lauf, gen)).fetchone()
    ziel = Path(f'/tmp/s1-staende/lauf{lauf}-gen{gen}')
    if not ziel.exists():
        ziel.mkdir(parents=True)
        with tarfile.open(z['archiv']) as t:
            t.extractall(ziel, filter='data')
    ps, _ = lazarus.pruefsumme_werk(ziel)
    assert ps == z['pruefsumme'], f'lauf{lauf}-gen{gen} weicht von der Lauf-DB ab'
    return ziel, ps


ergebnis = {}
for name in (sys.argv[1:] or list(FAELLE)):
    (la, ga), (ln, gn), kid = FAELLE[name]
    alt, ps_a = stand(la, ga)
    neu_w, ps_n = stand(ln, gn)
    neu = {r: (neu_w / r).read_text() for r in REL}
    if kid:
        d = aegis.kandidat_dateien(neu_w, c.execute('SELECT diff FROM kandidaten WHERE id=?', (kid,)).fetchone()[0])
        assert d and 'src/tarife/ausdruck.ts' in d, (kid, d and list(d))
        neu.update({r: d[r] for r in REL if d.get(r) is not None})
    dateien = {f'alt/{r}': (alt / r).read_text() for r in REL}
    dateien.update({f'neu/{r}': neu[r] for r in REL})
    dateien.update({f'norm/{r}': norm[r] for r in REL})
    dateien['s1_harness.mjs'] = HARNESS
    leer = Path('/tmp/s1-staende/leer')
    leer.mkdir(parents=True, exist_ok=True)
    e = kammer.ausfuehren(leer, ['node', 's1_harness.mjs'], zeitlimit_s=300, dateien=dateien)
    if e.rc != 0 or e.zeitlimit:
        ergebnis[name] = {'fehler': f'rc={e.rc} {e.stderr[-1500:]}'}
        print(name, 'FEHLER', e.stderr[-800:])
        continue
    d = json.loads(e.stdout)
    K, W, O = d['K'], d['W'], d['O']
    marker_neu = sum(o['neu']['markerzugriffe'] for o in O)
    w_ab = {k: v['neu_weist_ab_alt_und_norm_zahl'] for k, v in W.items()}
    sauber = marker_neu == 0 and K['neu_ungleich_norm'] == 0 and all(v == 0 for v in w_ab.values())
    ergebnis[name] = {'alt': f'lauf{la}-gen{ga} ({ps_a[:12]})', 'neu': f'lauf{ln}-gen{gn}' + (f' + K{kid}' if kid else '') + f' ({ps_n[:12]})',
                      'sha256_ausdruck_neu': hashlib.sha256(neu['src/tarife/ausdruck.ts'].encode()).hexdigest()[:16],
                      'K': {k: K[k] for k in ('faelle', 'vertrag_zahl', 'abweichungen', 'abw_bei_vertrag_zahl', 'je_art',
                                              'alt_vertragswidrig', 'neu_vertragswidrig', 'neu_ungleich_norm')},
                      'K_beispiele_neu_ungleich_norm': K['beispiele_neu_ungleich_norm'][:4],
                      'W': W, 'O': [{'rand': o['rand'], 'marker_alt': o['alt']['markerzugriffe'], 'marker_neu': o['neu']['markerzugriffe'],
                                     'marker_norm': o['norm']['markerzugriffe']} for o in O],
                      'R_neu_wie_norm': f"{sum(x['neu_wie_norm'] for x in d['R'])} von {len(d['R'])}",
                      'marker_neu_gesamt': marker_neu, 'S1_sauber_nach_entscheidung': sauber}
    print(f"{name:11} neu={ergebnis[name]['neu']:34} marker_neu={marker_neu} K_neu≠norm={K['neu_ungleich_norm']} "
          f"K_abw_bei_wert={K['abw_bei_vertrag_zahl']} W_weist_ab={w_ab} (von {W['tab']['ausdruecke']}) → S1 sauber: {sauber}")
ergebnis['_meta'] = {'t3_db_vorher': db_vorher, 't3_db_nachher': hashlib.sha256(Path(DB).read_bytes()).hexdigest(),
                     'harness_sha256': hashlib.sha256(HARNESS.encode()).hexdigest(), 'kammer': kammer.IMAGE, 'modellaufrufe': 0}
A.mkdir(parents=True, exist_ok=True)
(A / 'S1-STAENDE.json').write_text(json.dumps(ergebnis, ensure_ascii=False, indent=1))
print('t3.db unverändert:', ergebnis['_meta']['t3_db_vorher'] == ergebnis['_meta']['t3_db_nachher'])
