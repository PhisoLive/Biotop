"""Behebungsrunde 2 vor T4 — TypeScript-Seite der Sonde: Formvarianten, Argumente je Beobachtung (für die Deckung je
Abweichung), Aufzeichner-Lauf der deckenden Tests. Ersetzt nur benannte Anker; jeder muss genau einmal vorkommen."""
from pathlib import Path

TS = Path('/root/biotop/biotop/kern/ts')
r = (TS / 'verhalten-runner.mjs').read_text()


def ersetze(text, alt, neu):
    assert text.count(alt) == 1, (text.count(alt), alt[:90])
    return text.replace(alt, neu)


# 1. kan/knapp in ein gemeinsames Modul (Sonde und Aufzeichner kanonisieren gleich)
anfang = r.index('function kan(x, anc) {')
ende = r.index('function wert(f) {')
kan_code = r[anfang:ende]
k_anfang = r.index('function knapp(t) {')
k_ende = r.index('function schlicht(x) {')
knapp_code = r[k_anfang:k_ende]
(TS / 'kanon.mjs').write_text(
    "// Kanonische Form beobachteter Werte — gemeinsam für die Verhaltenssonde (verhalten-runner.mjs) und den\n"
    "// Aufzeichner der deckenden Tests (deck-setup.mjs), damit beide Seiten Argumente gleich schreiben.\n"
    "import {createHash} from 'node:crypto';\n\nexport " + kan_code.rstrip() + "\n\nexport " + knapp_code.rstrip() + "\n")
r = r.replace(kan_code, '').replace(knapp_code, '')
r = ersetze(r, "import {createHash} from 'node:crypto';\n", "import {kan, knapp} from './kanon.mjs';\n")

# 2. Argumente je Beobachtung
r = ersetze(r, "const beob = {}, zaehler = {}, zaehlerRand = {}, beispiele = {};",
            "const beob = {}, argtext = {}, zaehler = {}, zaehlerRand = {}, zaehlerForm = {}, beispiele = {};\n"
            "const FORM_KAPPE = req.form_kappe ?? 16;")
r = ersetze(r, "  try {\n    const erst = wert(() => call(...args));\n    beob[schluessel] = knapp(erst.text);",
            "  try {\n    try { argtext[schluessel] = knapp(JSON.stringify(kan(args, new Set()))); } catch { argtext[schluessel] = '__unkanonisch'; }\n"
            "    const erst = wert(() => call(...args));\n    beob[schluessel] = knapp(erst.text);")

# 3. Formvarianten (Entscheidung Chat-Claude: Korpus mit Randfällen UND Varianten der Eingabeform)
r = ersetze(r, "function argumentlisten(typen, beispiel) {", """// Dieselbe Eingabe in anderer Form: Weißraum (Tab, Zeilenumbruch, doppelt, CRLF, NBSP, am Rand), Groß/Klein,
// Zahlform im Text (führende Null, nachgestellte Null), Schlüsselfolge und Textfelder von Objekten.
function textFormen(s) {
  const out = [];
  if (s.includes(' ')) for (const r of ['\\t', '\\n', '  ', '\\r\\n', '\\u00a0']) out.push(s.split(' ').join(r));
  out.push(' ' + s, s + ' ', '\\t' + s + '\\n');
  if (s.toUpperCase() !== s) out.push(s.toUpperCase());
  if (s.toLowerCase() !== s) out.push(s.toLowerCase());
  const m = s.match(/\\d+(?:\\.\\d+)?/);
  if (m) { const z = m[0], a = s.slice(0, m.index), e = s.slice(m.index + z.length); out.push(a + '0' + z + e, a + z + (z.includes('.') ? '0' : '.0') + e); }
  return out;
}
function formWerte(p) {
  const out = [];
  if (typeof p === 'string' && p.length) out.push(...textFormen(p));
  else if (p && typeof p === 'object' && '__obj' in p) {
    const keys = Object.keys(p.__obj);
    if (keys.length > 1) { const o = {}; for (const k of [...keys].reverse()) o[k] = p.__obj[k]; out.push({__obj: o}); }
    let n = 0;
    for (const k of keys) {
      const v = p.__obj[k];
      if (typeof v === 'string' && v.length && n < 2) { n++; for (const w of textFormen(v).slice(0, 6)) out.push({__obj: {...p.__obj, [k]: w}}); }
    }
  }
  const s0 = JSON.stringify(p);
  return out.filter(v => JSON.stringify(v) !== s0 || (p && typeof p === 'object' && '__obj' in p));
}
function formvarianten(grund) {
  const listen = [];
  grund.forEach((p, j) => { for (const v of formWerte(p)) { const l = grund.slice(); l[j] = v; listen.push(l); } });
  const gesehen = new Set();
  return listen.filter(l => { const s = JSON.stringify(l) + '|' + JSON.stringify(l.map(x => x && x.__obj ? Object.keys(x.__obj) : null));
                              if (gesehen.has(s)) return false; gesehen.add(s); return true; }).slice(0, FORM_KAPPE);
}
function argumentlisten(typen, beispiel) {""")
r = ersetze(r, """      argumentlisten(typen ?? [], (quelleBeispiele ?? {})[name] ?? undefined).forEach((liste, i) => {
        const erst = muster(`${name}~rand#${i}`, unpack(liste), (...a) => fn(...a));
        if (!erst.fehler) zaehlerRand[name] = (zaehlerRand[name] ?? 0) + 1;
      });""", """      const listen = argumentlisten(typen ?? [], (quelleBeispiele ?? {})[name] ?? undefined);
      listen.forEach((liste, i) => {
        const erst = muster(`${name}~rand#${i}`, unpack(liste), (...a) => fn(...a));
        if (!erst.fehler) zaehlerRand[name] = (zaehlerRand[name] ?? 0) + 1;
      });
      formvarianten(listen[0] ?? []).forEach((liste, j) => {
        const erst = muster(`${name}~form#${j}`, unpack(liste), (...a) => fn(...a));
        if (!erst.fehler) zaehlerForm[name] = (zaehlerForm[name] ?? 0) + 1;
      });""")
r = ersetze(r, "  if (req.module?.length) korpus.push('randfaelle');",
            "  if (req.module?.length) korpus.push('randfaelle', 'formvarianten');")
r = ersetze(r, "  out = {gueltig: true, beobachtungen: beob, korpus, aufgerufen: zaehler, aufgerufen_rand: zaehlerRand,\n"
               "         kappe: KAPPE, rand_kappe: RAND_KAPPE,",
            "  out = {gueltig: true, beobachtungen: beob, argumente: argtext, korpus, aufgerufen: zaehler, aufgerufen_rand: zaehlerRand,\n"
            "         aufgerufen_form: zaehlerForm, kappe: KAPPE, rand_kappe: RAND_KAPPE, form_kappe: FORM_KAPPE,")
(TS / 'verhalten-runner.mjs').write_text(r)

# 4. Aufzeichner-Lauf der deckenden Tests (Vitest mit Einwickel-Plugin)
(TS / 'deckung.mjs').write_text("""// Deckung je Abweichung (Grundsatz 11, Entscheidung Chat-Claude 23.09.): die deckenden Tests am Kandidaten mit einem
// Aufzeichner ausführen. Das Vite-Plugin in vitest.deck.config.mjs wickelt die exportierten Funktionen der geänderten
// Module ein; deck-setup.mjs hält je Test jeden Aufruf fest (Funktion, kanonische Argumente, Identität und Inhalt
// der Objektargumente). Die Zuordnung Abweichung → Test macht Python (verhaltensvergleich.deckung_je_abweichung).
import fs from 'node:fs';
import {lauf} from './testlauf.mjs';
export function deckung(req) {
  fs.rmSync('/tmp/ts-deck.jsonl', {force: true});
  const p = lauf('node', ['/opt/biotop-ts/node_modules/vitest/vitest.mjs', 'run', '--config', '_messgeraet/ts/vitest.deck.config.mjs']);
  const aufrufe = fs.existsSync('/tmp/ts-deck.jsonl')
    ? fs.readFileSync('/tmp/ts-deck.jsonl', 'utf8').split('\\n').filter(Boolean).map(z => JSON.parse(z)) : [];
  return {gueltig: !p.fehler && !p.signal && [0, 1].includes(p.rc), rc: p.rc, aufrufe: aufrufe.slice(0, 20000),
          grund: p.rc === 0 || p.rc === 1 ? '' : 'Vitest-Abbruch rc=' + p.rc + ' ' + String(p.stderr).slice(-600)};
}
""")
(TS / 'vitest.deck.config.mjs').write_text("""import fs from 'node:fs';
const req = JSON.parse(fs.readFileSync(new URL('./anfrage.json', import.meta.url), 'utf8'));
const module = new Set((req.module ?? []).map(m => '/werk/src/' + m + '.ts'));
// Wie verhalten.mjs/einwickeln, aber am TypeScript-Quelltext (vor esbuild): `export (async) function f<…>(` wird
// umbenannt und durch einen gleichnamigen Export ersetzt, der über globalThis.__vvDeck aufzeichnet.
function einwickeln(code, modul) {
  const namen = [];
  const neu = code.replace(/^export (async )?function (\\w+)\\s*(<[^>()]*>)?\\s*\\(/gm, (m, asy, name, gen) => {
    namen.push(name);
    return `${asy || ''}function __vv_orig_${name}${gen || ''}(`;
  });
  let anhang = '\\n// --- Deckungsaufzeichner (nur in der Kammer) ---\\n';
  for (const n of namen) {
    anhang += `export function ${n}(...a: any[]): any { return (globalThis as any).__vvDeck(${JSON.stringify(modul + ':' + n)}, a, (...b: any[]) => (__vv_orig_${n} as any)(...b)); }\\n`;
  }
  return neu + anhang;
}
export default {
  root: '/werk', cacheDir: '/tmp/ts-vite-deck',
  plugins: [{name: 'vv-deck', enforce: 'pre', transform(code, id) {
    const p = id.split('?')[0];
    if (!module.has(p)) return null;
    return {code: einwickeln(code, p.slice('/werk/src/'.length, -3)), map: null};
  }}],
  test: {include: req.testdateien ?? [], exclude: [], globals: false, environment: 'node', pool: 'forks',
    poolOptions: {forks: {singleFork: true}}, fileParallelism: false, allowOnly: false, bail: 0, testTimeout: 8000,
    hookTimeout: 8000, setupFiles: ['/werk/_messgeraet/ts/deck-setup.mjs'], reporters: ['default'], watch: false,
    passWithNoTests: false, cache: false},
};
""")
(TS / 'deck-setup.mjs').write_text("""import {beforeEach, afterAll} from 'vitest';
import fs from 'node:fs';
import path from 'node:path';
import {kan, knapp} from './kanon.mjs';
const aufrufe = [];
let aktuell = '';
const ids = new WeakMap();
let naechste = 1;
const kennung = x => (x === null || typeof x !== 'object') ? null : (ids.has(x) ? ids.get(x) : (ids.set(x, naechste), naechste++));
const text = x => { try { return knapp(JSON.stringify(kan(x, new Set()))); } catch { return '__unkanonisch'; } };
globalThis.__vvDeck = (name, args, call) => {
  try {
    aufrufe.push({test: aktuell, f: name, args: text(args), ids: args.map(kennung),
                  inhalt: args.map(a => (a !== null && typeof a === 'object') ? text(a) : null)});
  } catch { /* der Aufzeichner darf den Test nie beeinflussen */ }
  return call(...args);
};
beforeEach((ctx) => {
  const t = ctx.task, namen = [];
  let s = t.suite;
  while (s && !('filepath' in s)) { if (s.name) namen.unshift(s.name); s = s.suite; }
  aktuell = path.basename(t.file?.name ?? t.file?.filepath ?? '') + '::' + [...namen, t.name].join(' > ');
});
afterAll(() => {
  if (aufrufe.length) fs.appendFileSync('/tmp/ts-deck.jsonl', aufrufe.map(a => JSON.stringify(a)).join('\\n') + '\\n');
  aufrufe.length = 0;
});
""")
m = (TS / 'main.mjs').read_text()
m = ersetze(m, "import {verhalten} from './verhalten.mjs';\n", "import {verhalten} from './verhalten.mjs';\nimport {deckung} from './deckung.mjs';\n")
m = ersetze(m, "  else if(req.aktion==='verhalten') result={ergebnis:verhalten(req)};\n",
            "  else if(req.aktion==='verhalten') result={ergebnis:verhalten(req)};\n  else if(req.aktion==='deckung') result={ergebnis:deckung(req)};\n")
(TS / 'main.mjs').write_text(m)
v = (TS / 'verhalten.mjs').read_text()
v = ersetze(v, "  fs.writeFileSync('/tmp/ts-vv-anfrage.json', JSON.stringify({bereiche: req.bereiche, kappe: req.kappe ?? 8,",
            "  fs.writeFileSync('/tmp/ts-vv-anfrage.json', JSON.stringify({bereiche: req.bereiche, kappe: req.kappe ?? 8, form_kappe: req.form_kappe ?? 16,")
(TS / 'verhalten.mjs').write_text(v)
print('TS-Seite geschrieben:', sorted(p.name for p in TS.iterdir()))
