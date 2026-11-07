"""Rauchprobe TS-Seite (biotop-kammer:ts1): Einwickeln am Syntaxbaum (export function / export const / Generator /
Klasse), Runner mit Muster, Kopien, Iterator, >args; Deckungsaufzeichner mit Klassen und Verfälschung — über
verhaltensvergleich.beobachten / deckende_aufrufe. Nur Diagnose während des Baus."""
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.organe import kammer  # noqa: E402
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
W = Path('/tmp/r3-rauch-ts/werk')
shutil.rmtree(W.parent, ignore_errors=True)
(W / 'src' / 'm').mkdir(parents=True)
(W / 'tests').mkdir()
(W / 'package.json').write_text('{"type":"module"}')
(W / 'src' / 'm' / 'a.ts').write_text('''export function f(x: string): string {
  return x;
}

export const g = (x: string): string => x.trim();

export function* zahlen(n: number): Generator<number> {
  for (let i = 0; i < n; i++) yield i;
}

export function sortiere(xs: number[]): void {
  xs.sort((a, b) => a - b);
}

export class Rechner {
  doppelt(x: number): number { return 2 * x; }
}

export const KONSTANTE = 3;
''')
(W / 'tests' / 'test_m.test.ts').write_text('''import { test, expect } from 'vitest';
import { f, g } from '../src/m/a.js';

test('f_gross', () => {
  expect(f('a')).toBe('A');
});

test('g_nebenbei', () => {
  g(' x ');
  expect(1).toBe(1);
});
''')
REF = '''import { f, g, zahlen, sortiere } from './dist/m/a.js';
export function last_m() { f('z y'); g(' q '); [...zahlen(3)]; sortiere([3, 1, 2]); }
'''
d = vv.beobachten(W, {}, REF, ['m/a'], ['m'])
print('gueltig', d.get('gueltig'), str(d.get('grund'))[:800])
if d.get('gueltig'):
    print('eingewickelt', d.get('eingewickelt'), 'nicht', d.get('nicht_eingewickelt'))
    print('signaturen', d.get('signaturen'))
    print('inhalt', d.get('inhalt'), 'unvergleichbar', d.get('unvergleichbar'))
    b = d['beobachtungen']
    for k in sorted(b):
        if any(x in k for x in ('zahlen#0', 'sortiere#0', 'g#0', 'g~form#0', 'f~rand#3')):
            print(' ', k, '=', b[k][:90], '| muster', (d.get('muster') or {}).get(k))
    print('muster-arten', sorted({x for v in (d.get('muster') or {}).values() for x in v}))
    print('kopien', list((d.get('kopien') or {}).items())[:3])
code = {'src/m/a.ts': (W / 'src' / 'm' / 'a.ts').read_text().replace('return x;', 'return x.toUpperCase();')}
dk = vv.deckende_aufrufe(W, code, {}, {'test_m.test.ts::f_gross', 'test_m.test.ts::g_nebenbei'})
print('deckung', {k: v for k, v in dk.items() if k != 'haelt'})
print('haelt f', dk['haelt']('m/a:f', 'rueckgabe'), 'haelt g', dk['haelt']('m/a:g', 'rueckgabe'))
