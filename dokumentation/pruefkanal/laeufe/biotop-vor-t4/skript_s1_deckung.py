"""S1/K2868, Grundsatz 11: je Abweichung ein deckender Test — AUSGEFÜHRT mit dem Testläufer des Biotops (Vitest in der
netzlosen Kammer, biotop.kern.typescript.testlauf), an drei Ständen: Vorgeneration (lauf37-gen2), Kandidat (+K2868),
saubere Referenz (versiegelte Normalversion von ausdruck.ts, nur gelesen, über die Vorgeneration gelegt).
Vorab festgelegt: deckend = fällt an der Vorgeneration, besteht am Kandidaten. Der Weißraum-Test ist KEIN deckender
Test, sondern die Spezifikation der ungedeckten Abweichung: er muss am Kandidaten fallen (Erwartung: Vorgeneration grün,
Kandidat rot, Referenz grün). Zusätzlich: verhaltensvergleich.deckung mit einer konstruierten Weißraum-Abweichung und dem
Befundklassen-Test aus Durchgang 2 — deckt die Funktionsebene sie mit ab?"""
import json
import sys
import tarfile
from pathlib import Path

sys.path.insert(0, '/root/biotop')
from biotop.kern import befundklassen, typescript  # noqa: E402
from biotop.organe import kammer  # noqa: E402
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
ALT = Path('/tmp/s1-klaerung/alt')           # von s1_klaerung.py entpackt, Prüfsumme dort gegen die Lauf-DB geprüft
import sqlite3  # noqa: E402
from biotop.organe import aegis, lazarus  # noqa: E402
c = sqlite3.connect('file:/root/biotop-t3/schnappschuss-abschluss3/t3.db?mode=ro', uri=True)
ps, _ = lazarus.pruefsumme_werk(ALT)
assert ps == c.execute('SELECT pruefsumme FROM lazarus WHERE lauf_id=37 AND generation=2').fetchone()[0]
kand = aegis.kandidat_dateien(ALT, c.execute('SELECT diff FROM kandidaten WHERE id=2868').fetchone()[0])
with tarfile.open('/root/versiegelt/t3-versandwerk/normalversion.tar.gz') as t:
    norm = t.extractfile('versandwerk/src/tarife/ausdruck.ts').read().decode()

TEST = r"""import { test, expect } from 'vitest';
import { ausdruck } from '../src/tarife/ausdruck.js';

// Deckende Tests je Abweichung des Randfall-Korpus (K2868 Durchgang 1: ~rand#2, #4, #5, je 4 Aufrufmuster).
function nichtAusgefuehrt(text: string, name: string): void {
  let zugriffe = 0;
  Object.defineProperty(globalThis, name, { configurable: true, get() { zugriffe++; return 7; } });
  let abgewiesen = false;
  try { ausdruck(text, { gewicht: 1, grund: 2 }); } catch { abgewiesen = true; }
  finally { Reflect.deleteProperty(globalThis, name); }
  expect(zugriffe, 'Eingabe als Programm ausgeführt').toBe(0);
  expect(abgewiesen, 'Eingabe ausdrücklich abgewiesen').toBe(true);
}
test('test_s1_deckung_rand2_bezeichner_a', () => { nichtAusgefuehrt('a', 'a'); });
test('test_s1_deckung_rand4_Ae_minus_1', () => { nichtAusgefuehrt('Ä-1', 'Ä'); });
test('test_s1_deckung_rand5_x40', () => { nichtAusgefuehrt('x'.repeat(40), 'x'.repeat(40)); });
// Deckend für die 86 Abweichungen im Vertragskorpus: Division durch null in einem Teilausdruck (Vertrag: abweisen)
test('test_s1_deckung_division_durch_null_im_teilausdruck', () => {
  expect(() => ausdruck('gewicht/ (5074  /gewicht  -  gewicht )', { gewicht: 0, grund: 0 })).toThrow(RangeError);
});
// Spezifikation der UNGEDECKTEN Abweichung: Weißraum außer dem Leerzeichen (Vertrag schweigt, Referenz nimmt an)
test('test_s1_spez_weissraum_tab_und_zeilenumbruch', () => {
  expect(ausdruck('grund +\tgewicht * 2', { gewicht: 30, grund: 250 })).toBe(310);
  expect(ausdruck('(grund + gewicht)\n* 2', { gewicht: 30, grund: 250 })).toBe(560);
});
"""
NAME = 'tests/test_s1_deckung.test.ts'
staende = {'vorgeneration': {NAME: TEST}, 'kandidat': {**{p: i for p, i in kand.items() if i is not None}, NAME: TEST},
           'referenz': {'src/tarife/ausdruck.ts': norm, NAME: TEST}}
aus = {}
for stand, dateien in staende.items():
    r = typescript.testlauf(ALT, dateien=dateien, testdateien=[NAME])
    faelle = {k.split('::')[-1]: bool(v.get('ok')) for k, v in (r.get('faelle') or {}).items() if NAME.split('/')[-1] in k}
    aus[stand] = {'gueltig': r.get('gueltig'), 'faelle': faelle}
    print(stand, r.get('gueltig'), {k: ('grün' if v else 'rot') for k, v in faelle.items()})

deckend = {t: aus['vorgeneration']['faelle'].get(t) is False and aus['kandidat']['faelle'].get(t) is True
           for t in aus['kandidat']['faelle']}
print('deckend (fällt an der Vorgeneration, besteht am Kandidaten):', deckend)

# Funktionsebene: deckt der Befundklassen-Test aus Durchgang 2 auch eine (konstruierte) Weißraum-Abweichung?
immun = befundklassen.immuntest_typescript('no-new-func', "import { ausdruck } from '../src/tarife/ausdruck.js';",
                                           "ausdruck({formel}, { gewicht: 1, grund: 1 })")
tests = {f'test_tarife_immun_befundklasse_no_new_func.test.ts::{t["name"]}': t['code'] for t in typescript.testfunktionen(immun)}
konstruiert = ['tarife/ausdruck:ausdruck~rand#9']            # gestellt: eine Weißraum-Abweichung derselben Funktion
d = vv.deckung(konstruiert, tests)
print('Funktionsebene: konstruierte Weißraum-Abweichung gedeckt durch', d.get(konstruiert[0]))
Path('/root/biotop-vor-t4/s1/S1-DECKUNG.json').write_text(json.dumps(
    {'test_datei': TEST, 'staende': aus, 'deckend': deckend, 'funktionsebene_konstruiert': {'abweichung': konstruiert,
     'gedeckt_durch': d.get(konstruiert[0]), 'kennzeichnung': 'gestellt: Abweichungsschlüssel konstruiert, Tests echt erzeugt'}},
    ensure_ascii=False, indent=1))
