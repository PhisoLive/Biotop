"""Behebungsrunde 4 vor T4 — Nachtrag zum Muster (eigene Lesart der Entscheidungen 2 und 3, vor der Messung festgelegt):
Merkmale sind die Formvarianten der Sonde (Entscheidung 2: „jede Formvariante, die die Sonde erzeugt, ist ein eigenes
Merkmal“) — Tab, Zeilenumbruch, CR/CRLF, NBSP, sonstiger Weißraum, doppeltes Leerzeichen, Rand vorn/hinten, Groß,
Klein, Zahlform vorn/hinten, Zahltyp, Behälter, Schlüsselfolge. Randwerte (leer, None, 0, negativ, lang, nicht-ASCII,
nicht endlich) sind keine Formvarianten und tragen kein Merkmal. Das Muster einer Beobachtung sind die Merkmale, die die
Veränderung der Sonde an einem Argument EINFÜHRT (danach minus davor; Entscheidung 3: Merkmale nicht veränderter
Argumente — und nicht veränderte Merkmale — gehören nicht dazu). Beide Sprachen gleich. Alles-oder-nichts.
"""
import py_compile
import subprocess
from pathlib import Path

PY = Path('/root/biotop/biotop/kern/py/verhalten.py')
TS = Path('/root/biotop/biotop/kern/ts/verhalten-runner.mjs')
py, ts = PY.read_text(), TS.read_text()
ops_py = [
("""def _muster_von(liste, bezug, korpusart):
    \"\"\"Muster eines Korpusaufrufs (Entscheidung Chat-Claude 3, Behebungsrunde 4): nur die Argumente, die die Sonde
    gegenüber `bezug` verändert hat. Randfall: die Merkmale der veränderten Werte; Formvariante: die Merkmale, die die
    Umformung eingeführt hat (Merkmale danach minus davor). Keine Veränderung (Grundliste): gewöhnlich, [].\"\"\"
    var = [j for j in range(len(liste)) if j >= len(bezug) or _json(liste[j]) != _json(bezug[j])]
    if not var:
        return []
    try:
        neu = klassen_von([unpack(liste[j]) for j in var])
        if korpusart == 'form':
            neu = neu - klassen_von([unpack(bezug[j]) for j in var if j < len(bezug)])
        return sorted(neu)
    except Exception:  # noqa: BLE001
        return ['__unbestimmt']""",
"""FORM_MERKMALE = frozenset({'tab', 'zeilenumbruch', 'crlf', 'cr', 'nbsp', 'weissraum_sonst', 'doppelleer', 'rand_vorn',
                           'rand_hinten', 'gross', 'klein', 'zahlform_null_vorn', 'zahlform_null_hinten', 'zahltyp',
                           'behaelter', 'schluesselfolge'})


def _muster_von(liste, bezug, korpusart):
    \"\"\"Muster eines Korpusaufrufs (Entscheidungen Chat-Claude 2 und 3, Behebungsrunde 4): die Formvarianten-Merkmale,
    die die Veränderung der Sonde an einem Argument einführt — Merkmale danach minus davor, nur an den veränderten
    Argumenten, nur Merkmale aus FORM_MERKMALE (Randwerte wie leer, None, lang, nicht-ASCII sind keine Formvarianten).
    Keine Veränderung (Grundliste) oder nichts eingeführt: gewöhnlich, []. `korpusart` nur zur Beschriftung.\"\"\"
    var = [j for j in range(len(liste)) if j >= len(bezug) or _json(liste[j]) != _json(bezug[j])]
    if not var:
        return []
    try:
        neu = klassen_von([unpack(liste[j]) for j in var]) - klassen_von([unpack(bezug[j]) for j in var if j < len(bezug)])
        return sorted(neu & FORM_MERKMALE)
    except Exception:  # noqa: BLE001
        return ['__unbestimmt']"""),
]
ops_ts = [
("""function musterVon(liste, bezug, form) {
  const varJ = liste.map((v, j) => (j >= bezug.length || JSON.stringify(v) !== JSON.stringify(bezug[j])) ? j : -1).filter(j => j >= 0);
  if (!varJ.length) return [];
  try {
    const neu = new Set(klassenVon(varJ.map(j => unpack(liste[j]))));
    if (form) for (const m of klassenVon(varJ.filter(j => j < bezug.length).map(j => unpack(bezug[j])))) neu.delete(m);
    return [...neu].sort();
  } catch { return ['__unbestimmt']; }
}""",
"""// Merkmale sind die Formvarianten der Sonde (Entscheidung Chat-Claude 2); Randwerte (leer, null, lang, nicht-ASCII …)
// tragen keines. Muster = die Formvarianten-Merkmale, die die Veränderung einführt (danach minus davor) — wie Python.
const FORM_MERKMALE = new Set(['tab', 'zeilenumbruch', 'crlf', 'cr', 'nbsp', 'weissraum_sonst', 'doppelleer', 'rand_vorn',
  'rand_hinten', 'gross', 'klein', 'zahlform_null_vorn', 'zahlform_null_hinten', 'zahltyp', 'behaelter', 'schluesselfolge']);
function musterVon(liste, bezug, form) {
  const varJ = liste.map((v, j) => (j >= bezug.length || JSON.stringify(v) !== JSON.stringify(bezug[j])) ? j : -1).filter(j => j >= 0);
  if (!varJ.length) return [];
  try {
    const neu = new Set(klassenVon(varJ.map(j => unpack(liste[j]))));
    for (const m of klassenVon(varJ.filter(j => j < bezug.length).map(j => unpack(bezug[j])))) neu.delete(m);
    return [...neu].filter(m => FORM_MERKMALE.has(m)).sort();
  } catch { return ['__unbestimmt']; }
}"""),
]
fehl = [a[:60] for a, b in ops_py if py.count(a) != 1] + [a[:60] for a, b in ops_ts if ts.count(a) != 1]
if fehl:
    raise SystemExit(f'Anker fehlen, nichts geschrieben: {fehl}')
for a, b in ops_py:
    py = py.replace(a, b)
for a, b in ops_ts:
    ts = ts.replace(a, b)
PY.write_text(py)
TS.write_text(ts)
py_compile.compile(str(PY), doraise=True)
r = subprocess.run(['node', '--check', str(TS)], capture_output=True, text=True)
if r.returncode:
    raise SystemExit('node --check: ' + r.stderr[:400])
print('Muster: 2 von 2 Ersetzungen, kompiliert')
