"""Generation 0, Lauf 37: Ursache der zwei Messdurchläufe „0 von 100 gefangen“.

Die Ursache wird im Code gelesen, in den Aufzeichnungen gezählt und am Messweg nachgestellt. Es gibt keinen
Modellaufruf. Die Lauf-DB wird nur als Schnappschuss mit WAL geöffnet (mode=ro).

Teil A: Lauf 37 je Messdurchlauf. Die Neutralzähler von generation0._testlauf werden den Zeitmarken der
generation0.*-Protokolleinträge zugeordnet.
Teil B: Nachstellung am Messweg. G0.messen ist die Funktion, die lauf.generation0 für jeden Durchlauf ruft. Sie läuft an
einer Kopie von lauf38-gen0 mit 5 aufgezeichneten Mutanten, in drei Fällen: (1) sauber; (2) mit einer Testdatei, die
unter Vitest besteht, aber den Typbau bricht (tsc über src UND tests); (3) die Datei wieder entfernt. Dazu kommen
typescript.testlauf, die Rundenprüfung in lauf.generation0, und typescript.baulauf, der Typbau je Mutant.
"""
import json
import shutil
import sqlite3
import sys
import tarfile
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.kern import datenbank, typescript  # noqa: E402
from biotop.organe import generation0 as G0  # noqa: E402
from biotop.organe import kammer, lazarus  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
S = '/root/biotop-t3/schnappschuss-abschluss3/t3.db'
AUS = Path('/root/biotop-t3/abschluss3/GEN0-URSACHE.json')
c = sqlite3.connect(f'file:{S}?mode=ro', uri=True)
c.row_factory = sqlite3.Row
aus = {}

print('======== A. Lauf 37: Messdurchläufe der Generation 0 (Neutralzähler je Durchlauf) ========')
marken = [dict(r) for r in c.execute(
    "SELECT nr, zeit, art, inhalt FROM protokoll WHERE art IN ('generation0.begonnen','generation0.aequivalenz',"
    "'generation0.vorher','generation0.nachher','generation0.ergebnis') AND json_extract(inhalt,'$.lauf_id')=37 ORDER BY nr")]
namen = {'generation0.aequivalenz': 'Äquivalenzprüfung', 'generation0.vorher': 'vorher'}
zeilen, start, nachher_i = [], None, 0
for m in marken:
    if m['art'] == 'generation0.begonnen':
        start = m['zeit']
        continue
    if m['art'] == 'generation0.ergebnis':
        continue
    inhalt = json.loads(m['inhalt'])
    if m['art'] == 'generation0.nachher':
        nachher_i += 1
    name = namen.get(m['art']) or (f'nachher Runde {nachher_i}' if nachher_i <= 3 else 'nachher Abschluss')
    z = {r['art']: r['n'] for r in c.execute(
        "SELECT art, COUNT(*) n FROM neutralzaehler WHERE lauf_id=37 AND organ='generation0._testlauf' "
        "AND zeit > ? AND zeit <= ? GROUP BY art", (start, m['zeit']))}
    gruende = {r['grund']: r['n'] for r in c.execute(
        "SELECT grund, COUNT(*) n FROM neutralzaehler WHERE lauf_id=37 AND organ='generation0._testlauf' AND art='neutral' "
        "AND zeit > ? AND zeit <= ? GROUP BY grund", (start, m['zeit']))}
    blind = inhalt.get('blind')
    zeile = {'durchlauf': name, 'ende_nr': m['nr'], 'ende_zeit': m['zeit'], 'geurteilt': z.get('geurteilt', 0),
             'neutral': z.get('neutral', 0), 'neutral_gruende': gruende, 'gefangen': inhalt.get('gefangen'),
             'blind': len(blind) if isinstance(blind, list) else blind}
    zeilen.append(zeile)
    print(f"  {name:22} bis nr {m['nr']} ({m['zeit'][11:19]} UTC): geurteilt {zeile['geurteilt']:>3}, neutral {zeile['neutral']:>3} "
          f"{gruende or ''}; Protokoll: gefangen {zeile['gefangen']}, blind {zeile['blind']}")
    start = m['zeit']
aus['lauf37_durchlaeufe'] = zeilen
g0k = {lauf: tuple(c.execute("SELECT COUNT(*), ROUND(SUM(kosten_eur),6) FROM kasse WHERE lauf_id=? AND zweck LIKE 'generation0%'",
                             (lauf,)).fetchone()) for lauf in (37, 38)}
tk = {lauf: c.execute("SELECT COUNT(*) FROM protokoll WHERE art='generation0.testkandidat' AND json_extract(inhalt,'$.lauf_id')=?",
                      (lauf,)).fetchone()[0] for lauf in (37, 38)}
erg = {lauf: json.loads(c.execute("SELECT inhalt FROM protokoll WHERE art='generation0.ergebnis' AND json_extract(inhalt,'$.lauf_id')=?",
                                  (lauf,)).fetchone()[0]) for lauf in (37, 38)}
for lauf in (37, 38):
    e = erg[lauf]
    print(f"  Lauf {lauf}: Kasse Generation 0 {g0k[lauf][0]} Buchungen, {g0k[lauf][1]} €; Testkandidaten {tk[lauf]}; "
          f"gefangen {e.get('gefangen_vorher')} → {e.get('gefangen_nachher')} von {e.get('nicht_aequivalent')}; "
          f"neue Testdateien {e.get('neue_tests') if isinstance(e.get('neue_tests'), int) else len(e.get('neue_tests') or [])}; Runden {e.get('runden')}")
aus['kasse_generation0'] = {str(k): v for k, v in g0k.items()}
aus['testkandidaten'] = {str(k): v for k, v in tk.items()}
leer = c.execute("SELECT COUNT(*) FROM neutralzaehler WHERE lauf_id=37 AND organ='generation0._testlauf' AND art='neutral' "
                 "AND (einzelheit IS NULL OR einzelheit='')").fetchone()[0]
print(f'  Neutralfälle Lauf 37 ohne gespeicherte Einzelheit (tsc-Meldung): {leer} von 200')
aus['neutral_ohne_einzelheit'] = leer

print('\n======== B. Nachstellung am Messweg (Kopie von lauf38-gen0, 5 aufgezeichnete Mutanten) ========')
z = c.execute('SELECT archiv, pruefsumme FROM lazarus WHERE lauf_id=38 AND generation=0').fetchone()
basis = Path('/tmp/gen0-ursache')
shutil.rmtree(basis, ignore_errors=True)
werk = basis / 'werk'
werk.mkdir(parents=True)
with tarfile.open(z['archiv']) as t:
    t.extractall(werk, filter='data')
ps, n = lazarus.pruefsumme_werk(werk)
print(f'lauf38-gen0: Prüfsumme {"stimmt" if ps == z["pruefsumme"] else "WEICHT AB"} ({n} Dateien)')
if ps != z['pruefsumme']:
    raise SystemExit('Werkstand weicht von der DB ab — keine Nachstellung')
alle = [dict(r) for r in c.execute("SELECT nummer, datei, zeile, art, beschreibung, code FROM mutanten WHERE lauf_id=38 "
                                   "AND gefangen_vorher=1 ORDER BY nummer")]
wahl = [alle[i * (len(alle) - 1) // 4] for i in range(5)]
mut = [{'datei': m['datei'], 'zeile': m['zeile'], 'art': m['art'], 'beschreibung': m['beschreibung'], 'code': m['code'],
        'quelle': 'nachstellung'} for m in wahl]
print('Mutanten:', [f"#{m['nummer']} {m['datei']}:{m['zeile']} {m['beschreibung']}" for m in wahl])
con = datenbank.verbinden(basis / 'probe.db')
G0.zaehlkontext_setzen(con, 1)
PROBE = 'tests/test_typfehler_probe.test.ts'
PROBE_CODE = ("import { test, expect } from 'vitest';\n\n"
              "test('probe_typfehler_nur_im_typbau', () => {\n"
              "  const werte: number[] = ['1', '2'] as unknown as string[];\n"
              "  expect(werte.length).toBe(2);\n"
              "});\n")


def durchlauf(name, phase):
    vorher_id = con.execute("SELECT COALESCE(MAX(id),0) FROM neutralzaehler").fetchone()[0] if con.execute(
        "SELECT name FROM sqlite_master WHERE name='neutralzaehler'").fetchone() else 0
    r = G0.messen(con, 1, 1, werk, mut, phase)
    nz = {f"{x['art']}:{x['grund'] or ''}": x['n'] for x in con.execute(
        "SELECT art, grund, COUNT(*) n FROM neutralzaehler WHERE id>? GROUP BY art, grund", (vorher_id,))}
    print(f"  {name:48} G0.messen: gefangen {r['gefangen']} von {r['gesamt']}, blind {len(r['blind'])}; Neutralzähler {nz}")
    return {'gefangen': r['gefangen'], 'gesamt': r['gesamt'], 'blind': len(r['blind']), 'neutralzaehler': nz}


b = {'mutanten': [m['nummer'] for m in wahl]}
b['bau_sauber'] = {k: typescript.baulauf(werk).get(k) for k in ('gueltig', 'baut')}
print('  Typbau sauber:', b['bau_sauber'])
b['1_sauber'] = durchlauf('(1) sauber', 'vorher')
(werk / PROBE).write_text(PROBE_CODE)
t = typescript.testlauf(werk)
faelle = t.get('faelle') or {}
b['rundenpruefung_mit_probe'] = {'gueltig': t.get('gueltig'), 'faelle': len(faelle),
                                 'alle_ok': bool(faelle) and all(x['ok'] for x in faelle.values()),
                                 'probe_fall': {k: v for k, v in faelle.items() if 'typfehler' in k}}
print('  Rundenprüfung (typescript.testlauf) mit Probe-Datei:', {k: v for k, v in b['rundenpruefung_mit_probe'].items() if k != 'probe_fall'},
      '| Probe-Fall:', b['rundenpruefung_mit_probe']['probe_fall'])
bau = typescript.baulauf(werk)
b['typbau_mit_probe'] = {'gueltig': bau.get('gueltig'), 'baut': bau.get('baut'),
                         'meldung': [zl for zl in str((bau.get('prozess') or {}).get('stdout') or bau.get('grund') or bau.get('roh') or '').splitlines() if 'error TS' in zl][:5]}
print('  Typbau (typescript.baulauf) mit Probe-Datei:', b['typbau_mit_probe'])
b['2_mit_probe'] = durchlauf('(2) mit Probe-Datei (Vitest grün, Typbau rot)', 'nachher')
(werk / PROBE).unlink()
b['3_entfernt'] = durchlauf('(3) Probe-Datei entfernt (Gegenprobe)', 'nachher')
aus['nachstellung'] = b
AUS.write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
print('\nBeleg:', AUS)
