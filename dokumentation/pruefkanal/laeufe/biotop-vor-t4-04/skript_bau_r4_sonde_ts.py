"""Behebungsrunde 4 vor T4 — TypeScript-Seite der Sonde und des Aufzeichners, gleich der Python-Seite:
- Entscheidung 2 / R4-1: Merkmale je Formvariante (kanon.mjs textMerkmale, dieselben Namen wie verhalten.py).
- Entscheidung 3: Muster nur aus den veränderten Argumenten (Lastaufrufe gewöhnlich; Randfall: Merkmale des veränderten
  Werts; Formvariante: von der Umformung eingeführte Merkmale).
- R4-2: Verfälschung nur an Aufrufen, deren Eingabe das Merkmal trägt; Aufbau-/Abbaufehler zählen nicht als „fällt“.
- R4-3: nur Generatoren auslesen; andere Iterator-Objekte bleiben (gezählt als Teil-Enthaltung).
- R4-13: Iterator-Kappe gezählt.
Alles-oder-nichts: jeder Anker genau einmal.
"""
import subprocess
from pathlib import Path

T = Path('/root/biotop/biotop/kern/ts')
dateien = {n: (T / n).read_text() for n in ('kanon.mjs', 'verhalten-runner.mjs', 'deck-setup.mjs', 'deckung.mjs')}
ops = []


def R(d, a, b, n=1):
    ops.append((d, a, b, n))


R('kanon.mjs', '''const WEISS = /[\\t\\n\\r\\v\\f\\u00a0\\u2028\\u2029\\u3000\\u2009]/;
export function klassenVon(werte) {''', '''const WEISS = /[\\t\\n\\r\\v\\f\\u00a0\\u2028\\u2029\\u3000\\u2009]/;
const WEISS_SONST = /[\\v\\f\\u2028\\u2029\\u3000\\u2009]/;
// Merkmale einer Zeichenkette — je Formvariante der Sonde ein eigenes Merkmal (Entscheidung Chat-Claude 2,
// Behebungsrunde 4; Review 03 Nr. 1). Dieselben Namen wie kern/py/verhalten.py::_text_merkmale.
export function textMerkmale(x) {
  const m = new Set();
  const ohneCrlf = x.split('\\r\\n').join('');
  if (x.includes('\\r\\n')) m.add('crlf');
  if (ohneCrlf.includes('\\r')) m.add('cr');
  if (ohneCrlf.includes('\\n')) m.add('zeilenumbruch');
  if (x.includes('\\t')) m.add('tab');
  if (x.includes('\\u00a0')) m.add('nbsp');
  if (WEISS_SONST.test(x)) m.add('weissraum_sonst');
  if (x.includes('  ')) m.add('doppelleer');
  if (x !== x.replace(/^\\s+/, '')) m.add('rand_vorn');
  if (x !== x.replace(/\\s+$/, '')) m.add('rand_hinten');
  if (/\\p{Lu}/u.test(x)) m.add('gross');
  if (/\\p{L}/u.test(x) && x === x.toLowerCase() && x !== x.toUpperCase()) m.add('klein');
  if (/(?<![\\d.])0\\d/.test(x)) m.add('zahlform_null_vorn');
  if (/\\d\\.\\d*0(?!\\d)/.test(x)) m.add('zahlform_null_hinten');
  if (x.length >= 40) m.add('lang');
  if ([...x].some(c => c.charCodeAt(0) > 127 && !WEISS.test(c))) m.add('nichtascii');
  return m;
}
export function klassenVon(werte) {''')
R('kanon.mjs', '''      if (WEISS.test(x) || x.includes('  ')) out.add('weissraum');
      if (x !== x.trim()) out.add('randweissraum');
      if (/\\p{Lu}/u.test(x)) out.add('gross');
      if (/\\p{L}/u.test(x) && x === x.toLowerCase() && x !== x.toUpperCase()) out.add('klein');
      if (/(?<![\\d.])0\\d|\\d\\.\\d*0(?!\\d)/.test(x)) out.add('zahlform');
      if (x.length >= 40) out.add('lang');
      if ([...x].some(c => c.charCodeAt(0) > 127 && !WEISS.test(c))) out.add('nichtascii');
      return;''', '''      for (const m of textMerkmale(x)) out.add(m);
      return;''')
# ---------------------------------------------------------------- Runner
R('verhalten-runner.mjs', '''function istIterator(v) {
  return v && typeof v === 'object' && typeof v.next === 'function' && typeof v[Symbol.iterator] === 'function'
    && !Array.isArray(v) && !(v instanceof Map) && !(v instanceof Set);
}''', '''const GENERATOR_PROTO = Object.getPrototypeOf(function* () {}).prototype;
const ITER_PROTO = Object.getPrototypeOf(GENERATOR_PROTO);
function istIterator(v) {
  return v && typeof v === 'object' && typeof v.next === 'function' && typeof v[Symbol.iterator] === 'function'
    && !Array.isArray(v) && !(v instanceof Map) && !(v instanceof Set);
}
// Behebungsrunde 4 (Review 03 Nr. 3): nur Generatoren und eingebaute Iteratoren (Array-, Map-, Set-, String-Iteratoren)
// auslesen und ersetzen; ein Iterator-Objekt des Werks bleibt unverändert, der Aufrufer liest womöglich Felder.
function istEingebautOderGenerator(v) {
  const p = Object.getPrototypeOf(v);
  return GENERATOR_PROTO.isPrototypeOf(v) || p === ITER_PROTO || (p && Object.getPrototypeOf(p) === ITER_PROTO && !Object.hasOwn(p, 'constructor'));
}
const teilweise = {};
function teil(name, art) { if (name) { const d = teilweise[name] ??= {}; d[art] = (d[art] ?? 0) + 1; } }''')
R('verhalten-runner.mjs', '''  if (istIterator(v)) {
    const el = []; let fehler = null;
    try { for (const x of v) { el.push(x); if (el.length > ITER_KAPPE) break; } } catch (e) { fehler = e; }
    const mehr = !fehler && el.length > ITER_KAPPE;''', '''  if (istIterator(v) && !istEingebautOderGenerator(v)) {
    teil(name, 'iterator_objekt');
    let text;
    try { text = JSON.stringify(kan({__iterator_objekt: v}, new Set())); } catch { return {text: '__unkanonisch', roh: v, inhaltlich: false}; }
    if (name) inhalt[name] = (inhalt[name] ?? 0) + 1;
    return {text, roh: v, inhaltlich: true};
  }
  if (istIterator(v)) {
    const el = []; let fehler = null;
    try { for (const x of v) { el.push(x); if (el.length > ITER_KAPPE) break; } } catch (e) { fehler = e; }
    const mehr = !fehler && el.length > ITER_KAPPE;
    if (mehr) teil(name, 'iterator_gekappt');''')
R('verhalten-runner.mjs', '''function textFormen(s) {
  const out = [];
  if (s.includes(' ')) for (const r of ['\\t', '\\n', '  ', '\\r\\n', '\\u00a0']) out.push([s.split(' ').join(r), 'weissraum']);
  out.push([' ' + s, 'randweissraum'], [s + ' ', 'randweissraum'], ['\\t' + s + '\\n', 'randweissraum']);''', '''function textFormen(s) {
  const out = [];
  if (s.includes(' ')) for (const [r, a] of [['\\t', 'tab'], ['\\n', 'zeilenumbruch'], ['  ', 'doppelleer'], ['\\r\\n', 'crlf'], ['\\u00a0', 'nbsp']]) out.push([s.split(' ').join(r), a]);
  out.push([' ' + s, 'rand_vorn'], [s + ' ', 'rand_hinten'], ['\\t' + s + '\\n', 'rand_tab_zeilenumbruch']);''')
R('verhalten-runner.mjs', '''function formvarianten(quellen) {
  const listen = [];
  for (const grund of quellen) grund.forEach((p, j) => { for (const [v, art] of formWerte(p)) { const l = grund.slice(); l[j] = v; listen.push([l, art]); } });''',
  '''function formvarianten(quellen) {
  const listen = [];
  for (const grund of quellen) grund.forEach((p, j) => { for (const [v, art] of formWerte(p)) { const l = grund.slice(); l[j] = v; listen.push([l, art, grund]); } });''')
R('verhalten-runner.mjs', '''const klSicher = (werte, extra = []) => { try { return [...new Set([...extra, ...klassenVon(werte)])]; } catch { return ['__unbestimmt']; } };''',
  '''// Muster eines Korpusaufrufs (Entscheidung Chat-Claude 3, Behebungsrunde 4): nur die Argumente, die die Sonde gegenüber
// `bezug` verändert hat — Randfall: deren Merkmale; Formvariante: die von der Umformung eingeführten Merkmale.
function musterVon(liste, bezug, form) {
  const varJ = liste.map((v, j) => (j >= bezug.length || JSON.stringify(v) !== JSON.stringify(bezug[j])) ? j : -1).filter(j => j >= 0);
  if (!varJ.length) return [];
  try {
    const neu = new Set(klassenVon(varJ.map(j => unpack(liste[j]))));
    if (form) for (const m of klassenVon(varJ.filter(j => j < bezug.length).map(j => unpack(bezug[j])))) neu.delete(m);
    return [...neu].sort();
  } catch { return ['__unbestimmt']; }
}''')
R('verhalten-runner.mjs', '''  const erst = muster(`${name}#${i}`, args, call, name, klSicher(args));''',
  '''  const erst = muster(`${name}#${i}`, args, call, name, []);      // Lastaufruf: kein Argument verändert — gewöhnlich''')
R('verhalten-runner.mjs', '''        const erst = muster(`${name}~rand#${i}`, args, (...a) => fn(...a), name, klSicher(args));''',
  '''        const erst = muster(`${name}~rand#${i}`, args, (...a) => fn(...a), name, musterVon(liste, grund, false));''')
R('verhalten-runner.mjs', '''      formvarianten(quellen).forEach(([liste, art], j) => {
        const args = unpack(liste);
        const erst = muster(`${name}~form#${j}`, args, (...a) => fn(...a), name, klSicher(args, [art]));''',
  '''      formvarianten(quellen).forEach(([liste, art, bezug], j) => {
        const args = unpack(liste);
        const erst = muster(`${name}~form#${j}`, args, (...a) => fn(...a), name, musterVon(liste, bezug, true));''')
# ---------------------------------------------------------------- Aufzeichner
R('deck-setup.mjs', '''globalThis.__vvDeck = (name, args, call) => {
  if (vf) {
    if (vf.f !== name) return call(...args);''', '''globalThis.__vvDeck = (name, args, call) => {
  if (vf) {
    if (vf.f !== name) return call(...args);
    // Behebungsrunde 4 (Review 03 Nr. 2): nur Aufrufe verfälschen, deren Eingabe das Merkmal des Musters trägt.
    if (vf.merkmal) { let kl = []; try { kl = klassenVon(args); } catch { kl = []; } if (!kl.includes(vf.merkmal)) return call(...args); }''')
R('deckung.mjs', '''    for (const t of n.tests ?? []) zustand[path.basename(t.id.split('::')[0]) + '::' + t.id.split('::').slice(1).join('::')] = t.state;''',
  '''    // Behebungsrunde 4 (Review 03 Nr. 2): festhalten heißt „die Zusicherung im Test fällt“ — ein Fehler in einem
    // Aufbau-/Abbau-Haken (beforeEach/afterEach …) ist 'fehler', kein 'fail'.
    for (const t of n.tests ?? []) {
      const haken = Object.values(t.hooks ?? {}).some(s => s === 'fail');
      zustand[path.basename(t.id.split('::')[0]) + '::' + t.id.split('::').slice(1).join('::')] = haken ? 'fehler' : t.state;
    }''')

fehl = [(d, a[:70], dateien[d].count(a)) for d, a, b, n in ops if dateien[d].count(a) != n]
if fehl:
    raise SystemExit(f'Anker fehlen/mehrdeutig, nichts geschrieben: {fehl}')
for d, a, b, n in ops:
    dateien[d] = dateien[d].replace(a, b)
for d, t in dateien.items():
    (T / d).write_text(t)
    r = subprocess.run(['node', '--check', str(T / d)], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f'{d}: node --check {r.stderr[:500]}')
print(f'TS: {len(ops)} von {len(ops)} Ersetzungen in {len(dateien)} Dateien, node --check ok')
