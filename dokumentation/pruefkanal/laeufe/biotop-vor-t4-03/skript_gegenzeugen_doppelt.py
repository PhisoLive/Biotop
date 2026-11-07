"""Entscheidung Chat-Claude 4 am T3-Versandwerk (S1 NICHT neu versiegelt): jeder Gegenzeuge prüft zweierlei — Schwäche
weg UND gültiges Verhalten gegen die Normalversion unverändert —; das Urteil fällt biotop.kern.gegenzeugen.doppelurteil.
Gemessen in der Kammer (biotop-kammer:ts1) mit s1_harness.mjs (unverändert aus laeufe/biotop-vor-t4/s1):
  normalversion  Gegenprobe: die Normalversion selbst als Stand — beide Prüfungen müssen halten → behoben
  ursprung       Gegenprobe: das Werk mit der versiegelten Schwäche (/root/versandwerk-t3-02) → Schwäche da → nicht behoben
Vorgeneration (alt) ist in beiden Fällen der Ursprung. Übernommen (nicht neu gemessen) aus
laeufe/biotop-vor-t4-02/s1/S1-STAENDE.json: k3044, endstand38, endstand37, k2868. Kein Modellaufruf, versiegelter Ordner
nur gelesen (sha256 vorher/nachher)."""
import hashlib
import json
import sys
import tarfile
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.kern import gegenzeugen
from biotop.organe import kammer  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
A = Path('/root/biotop-vor-t4-03/s1')
SIEGEL = Path('/root/versiegelt/t3-versandwerk')
HARNESS = Path('/root/biotop-vor-t4/s1/s1_harness.mjs').read_text()
REL = ['src/tarife/ausdruck.ts', 'src/tarife/modell.ts', 'src/zahlen/pruefen.ts']


def siegel_sha():
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(SIEGEL.glob('*')) if p.is_file()}


vorher = siegel_sha()
with tarfile.open(SIEGEL / 'normalversion.tar.gz') as t:
    norm = {r: t.extractfile(f'versandwerk/{r}').read().decode() for r in REL}
urs = {r: (Path('/root/versandwerk-t3-02') / r).read_text() for r in REL}
leer = Path('/tmp/s1-doppelt-leer')
leer.mkdir(parents=True, exist_ok=True)
aus = {'_meta': {'harness_sha256': hashlib.sha256(HARNESS.encode()).hexdigest(), 'kammer': kammer.IMAGE,
                 'modellaufrufe': 0}}
for name, neu in (('normalversion', norm), ('ursprung', urs)):
    dateien = {**{f'alt/{r}': urs[r] for r in REL}, **{f'neu/{r}': neu[r] for r in REL},
               **{f'norm/{r}': norm[r] for r in REL}, 's1_harness.mjs': HARNESS}
    e = kammer.ausfuehren(leer, ['node', 's1_harness.mjs'], zeitlimit_s=300, dateien=dateien)
    if e.rc != 0 or e.zeitlimit:
        aus[name] = {'fehler': f'rc={e.rc} zeitlimit={e.zeitlimit} {(e.stderr or "")[-1500:]}'}
        print(name, 'FEHLER', aus[name]['fehler'][:600])
        continue
    d = json.loads(e.stdout)
    mess = {'marker_neu_gesamt': sum(o['neu']['markerzugriffe'] for o in d['O']), 'K': d['K'], 'W': d['W']}
    aus[name] = {'messung': {'marker_neu_gesamt': mess['marker_neu_gesamt'],
                             'K': {k: d['K'][k] for k in ('faelle', 'vertrag_zahl', 'neu_ungleich_norm')},
                             'W': {w: {k: v[k] for k in ('ausdruecke', 'norm_zahl', 'neu_zahl', 'neu_weist_ab_alt_und_norm_zahl')}
                                   for w, v in d['W'].items()}},
                 'urteil': gegenzeugen.doppelurteil(*gegenzeugen.s1_aus_messung(mess)), 'herkunft': 'gemessen (Runde 3)'}
alt = json.loads(Path('/root/biotop-vor-t4-02/s1/S1-STAENDE.json').read_text())
for name in ('k3044', 'endstand38', 'endstand37', 'k2868'):
    aus[name] = {'urteil': gegenzeugen.doppelurteil(*gegenzeugen.s1_aus_messung(alt[name])),
                 'kriterium_runde2_sauber': alt[name]['S1_sauber_nach_entscheidung'],
                 'herkunft': 'übernommen aus laeufe/biotop-vor-t4-02/s1/S1-STAENDE.json'}
aus['_meta']['siegel_unveraendert'] = siegel_sha() == vorher
(A / 'GEGENZEUGEN-DOPPELT.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1))
for name, v in aus.items():
    if name != '_meta':
        u = v.get('urteil') or {}
        print(f"{name:14} behoben={u.get('behoben')!s:5} | {u.get('grund') or v.get('fehler')} | {v.get('herkunft', '')}")
print('Erwartung: normalversion True, ursprung False, k3044/endstand38/endstand37/k2868 False')
print('Siegelordner unverändert:', aus['_meta']['siegel_unveraendert'])
