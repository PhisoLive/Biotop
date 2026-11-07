"""S1-Klärung K2868 (Auftrag Philipp, Punkt 1): Wertet der Parser des Kandidaten GÜLTIGE Ausdrücke anders aus als die
Vorgeneration? Oder betreffen die 12 Abweichungen am Randfall-Korpus nur ungültige Eingaben?

Vorab festgelegt (vor der Ausführung, hier niedergeschrieben):
  Gültig = Ausdruck aus der Grammatik des Grenzvertrags (tests/vertraege/VERTRAEGE.md Z. 22): nichtnegative
  Dezimalzahlen, `gewicht`, `grund`, + - * /, Klammern, ≤ 160 Zeichen, Leerzeichen zwischen Zeichen.
  Korpus K: die 8 Vertragsbeispiele aus tests/test_tarife.test.ts + 20.000 verschiedene zufällige Ausdrücke dieser
  Grammatik (fester Keim 20260923, Tiefe ≤ 4, Zahlen mit 0–3 Nachkommastellen), je 6 Kontexte. Einschließlich der
  Fälle, die der Vertrag abweist (Division durch null, negatives Ergebnis): auch dort muss das Urteil gleich sein.
  Regel: 0 Abweichungen alt↔neu in K (Wert per Object.is, Fehler per Fehlerklasse) ⇒ „gültige Ausdrücke gleich
  ausgewertet“; jede Abweichung in K ⇒ S1 nicht sauber behoben (Philipps Satz), Beispiele werden ausgewiesen.
  Zusätzlich je Seite gegen den Vertrag (unabhängige Auswertung nach Rangfolge) und neu gegen die versiegelte
  Normalversion (Autorenreferenz, nur gelesen).
  Korpus R: Schreibweisen außerhalb der Grammatik oder vom Vertrag nicht festgelegt — ausgewiesen, nicht Teil der Regel.
  Korpus O: die Eingaben des Organs (~rand#1..#5), mit globalem Marker: wird der Text als Programm ausgeführt?
Stände: Vorgeneration = Lazarus lauf37-gen2 (Prüfsumme gegen die Lauf-DB), Kandidat = Vorgeneration + Diff K2868
(aegis.kandidat_dateien, dieselbe Ableitung wie das Organ), Normalversion = /root/versiegelt/t3-versandwerk/normalversion.tar.gz.
Ausführung: netzlose Kammer (biotop.organe.kammer, Image biotop-kammer:ts1), kein Modellaufruf.
"""
import hashlib
import io
import json
import sqlite3
import sys
import tarfile
import time
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.organe import aegis, kammer, lazarus  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
A = Path('/root/biotop-vor-t4/s1')
DB = '/root/biotop-t3/schnappschuss-abschluss3/t3.db'
db_vorher = hashlib.sha256(Path(DB).read_bytes()).hexdigest()
c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
c.row_factory = sqlite3.Row
z = c.execute('SELECT archiv, pruefsumme FROM lazarus WHERE lauf_id=37 AND generation=2').fetchone()
alt_werk = Path('/tmp/s1-klaerung/alt')
import shutil  # noqa: E402
shutil.rmtree('/tmp/s1-klaerung', ignore_errors=True)
alt_werk.mkdir(parents=True)
with tarfile.open(z['archiv']) as t:
    t.extractall(alt_werk, filter='data')
ps, _ = lazarus.pruefsumme_werk(alt_werk)
assert ps == z['pruefsumme'], 'Vorgeneration weicht von der Lauf-DB ab'
diff = c.execute('SELECT diff FROM kandidaten WHERE id=2868').fetchone()[0]
kand = aegis.kandidat_dateien(alt_werk, diff)
assert kand and 'src/tarife/ausdruck.ts' in kand, kand and list(kand)

REL = ['src/tarife/ausdruck.ts', 'src/tarife/modell.ts', 'src/zahlen/pruefen.ts']
dateien = {}
for r in REL:
    dateien[f'alt/{r}'] = (alt_werk / r).read_text()
    dateien[f'neu/{r}'] = kand.get(r) if kand.get(r) is not None else (alt_werk / r).read_text()
with tarfile.open('/root/versiegelt/t3-versandwerk/normalversion.tar.gz') as t:
    for r in REL:
        dateien[f'norm/{r}'] = t.extractfile(f'versandwerk/{r}').read().decode()
dateien['s1_harness.mjs'] = (A / 's1_harness.mjs').read_text()
leer = Path('/tmp/s1-klaerung/leer')
leer.mkdir()
t0 = time.monotonic()
e = kammer.ausfuehren(leer, ['node', 's1_harness.mjs'], zeitlimit_s=300, dateien=dateien)
dauer = round(time.monotonic() - t0, 1)
if e.rc != 0 or e.zeitlimit:
    (A / 'S1-KLAERUNG-FEHLER.txt').write_text(f'rc={e.rc} zeitlimit={e.zeitlimit}\n{e.stdout[-3000:]}\n{e.stderr[-6000:]}')
    sys.exit(f'Kammer rc={e.rc}: {e.stderr[-1500:]}')
d = json.loads(e.stdout)
d['meta'] = {'vorgeneration': {'lazarus': 'lauf37-gen2', 'pruefsumme': ps, 'stimmt': True},
             'kandidat': 'K2868 (Diff aus t3.db, aegis.kandidat_dateien)',
             'sha256': {k: hashlib.sha256(v.encode()).hexdigest()[:16] for k, v in dateien.items() if k.endswith('ausdruck.ts')},
             'kammer_image': kammer.IMAGE, 'kammer_dauer_s': dauer, 'modellaufrufe': 0,
             't3_db_sha256_vorher': db_vorher, 't3_db_sha256_nachher': hashlib.sha256(Path(DB).read_bytes()).hexdigest()}
(A / 'S1-KLAERUNG.json').write_text(json.dumps(d, ensure_ascii=False, indent=1))
K = d['K']
print(f"K: {K['ausdruecke']} Ausdrücke, {K['faelle']} Fälle, Längen {K['laengen']}; Abweichungen alt↔neu {K['abweichungen']} "
      f"{K['je_art']}; alt vertragswidrig {K['alt_vertragswidrig']}, neu vertragswidrig {K['neu_vertragswidrig']}, "
      f"neu≠Normalversion {K['neu_ungleich_norm']}")
print(f"K: Fälle mit Vertragswert {K['vertrag_zahl']} von {K['faelle']}, Abweichungen dort {K['abw_bei_vertrag_zahl']}; "
      f"Abweichungen je Meldung des Kandidaten {K['abw_neu_meldung']}")
for name, w in d['W'].items():
    print(f"W[{name}] (nachträglich): {w['ausdruecke']} Ausdrücke, alt Zahl {w['alt_zahl']}, neu Zahl {w['neu_zahl']}, "
          f"Normalversion Zahl {w['norm_zahl']}, neu weist ab wo alt=Normalversion Zahl: {w['neu_weist_ab_alt_und_norm_zahl']}")
for b in K['beispiele_abweichung'][:3]:
    print('  K-Abweichung', json.dumps(b, ensure_ascii=False)[:300])
print(f"R: {len(d['R'])} Eingaben, gleich {sum(x['gleich'] for x in d['R'])}; neu wie Normalversion "
      f"{sum(x['neu_wie_norm'] for x in d['R'])}, alt wie Normalversion {sum(x['alt_wie_norm'] for x in d['R'])}")
for x in d['R']:
    if False:
        print('  R', x['gruppe'], repr(x['text']), '| alt', json.dumps(x['alt'], ensure_ascii=False)[:90], '| neu',
              json.dumps(x['neu'], ensure_ascii=False)[:90], '| norm', json.dumps(x['norm'], ensure_ascii=False)[:70])
for o in d['O']:
    print('  O', o['rand'], o['text'], {s: (o[s]['markerzugriffe'], o[s]['mit_marker'], o[s]['ohne_marker'].get('e') or o[s]['ohne_marker'].get('v')) for s in ('alt', 'neu', 'norm')})
print('db unverändert', d['meta']['t3_db_sha256_vorher'] == d['meta']['t3_db_sha256_nachher'], 'dauer', dauer)
