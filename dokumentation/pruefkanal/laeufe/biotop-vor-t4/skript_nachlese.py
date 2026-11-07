"""Nachlese nach dem Commit-Job (Befunde, die erst die Nachspiele am Commit zeigten):
1. Restrauschen der gepaarten Messung in UNBERÜHRTEN Bereichen, erster Durchgang (nachspiel/, 58bd9f9-Arbeitsbaum) gegen
   zweiten (nachspiel2/, Commit 330b4ec) — dieselbe Rechnung wie das Review (Verhältnis Kandidat/Vorgeneration).
2. Python-Gegenprobe der gepaarten Laufzeit mit vollem Rückgabewert (Lauf 2 speicherte nur gueltig/seite).
3. Rote Spezifikation: Teilausfall einer Seite (ein Bereich ohne Wert) muss ein Messgerätausfall sein — an 330b4ec ausgeführt.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

A = Path('/root/biotop-vor-t4')
sys.path.insert(0, '/root/biotop')
aus = {}

# ---- 1. Restrauschen unberührter Bereiche
def beruehrt(diff):
    return {m.group(1) for d in re.findall(r'^\+\+\+ b/(\S+)', diff or '', re.M) if (m := re.match(r'src/([^/]+)/', d))}

import sqlite3  # noqa: E402
c = sqlite3.connect('file:/root/biotop-t3/schnappschuss-abschluss3/t3.db?mode=ro', uri=True)
rausch = {}
for ordner in ('nachspiel', 'nachspiel2'):
    werte = []
    for p in sorted((A / ordner).glob('*.json')):
        if p.name == 'k2868-durchgang1.json' and ordner == 'nachspiel':
            pass
        d = json.loads(p.read_text())
        lz = (d.get('laufzeit_gepaart') or {}).get('bereiche') or {}
        diffs = ''.join(c.execute('SELECT diff FROM kandidaten WHERE id=?', (k,)).fetchone()[0] or ''
                        for k in (d.get('kandidat'), d.get('partner')) if k)
        b_ber = beruehrt(diffs)
        for b, x in lz.items():
            if b not in b_ber and x.get('basis') and x.get('kandidat'):
                werte.append((round(x['kandidat'] / x['basis'], 3), p.stem, b))
    werte.sort(reverse=True)
    rausch[ordner] = {'vergleiche': len(werte), 'ueber_1_10': sum(v > 1.10 for v, *_ in werte),
                      'ueber_1_15': sum(v > 1.15 for v, *_ in werte), 'groesste': werte[:4]}
aus['restrauschen_unberuehrt'] = rausch
print('Restrauschen unberührter Bereiche:', json.dumps(rausch, ensure_ascii=False))

# ---- 2. Python-Gegenprobe, voller Rückgabewert
from biotop import lauf as L  # noqa: E402
from biotop.kern import messgeraet  # noqa: E402
from biotop.organe import kammer, landkarte  # noqa: E402
kammer.IMAGE = 'biotop-kammer:1'
W = Path('/root/uebungswerk-p2')
bereiche = landkarte.bereiche_finden(W, 'lagerhaus')
ref = L._referenzlast('lagerhaus', 'lagerhaus')
ziel = W / 'lagerhaus' / 'formeln' / 'auswertung.py'
g = messgeraet.laufzeit_gepaart(W, bereiche, 'lagerhaus', ref, None, {'lagerhaus/formeln/auswertung.py': ziel.read_text() + '\ndef kaputt(:\n'})
roh = messgeraet.laufzeit_messen(W, bereiche, 'lagerhaus', ref, {'lagerhaus/formeln/auswertung.py': ziel.read_text() + '\ndef kaputt(:\n'})
aus['python_gegenprobe_voll'] = {'gepaart': {k: v for k, v in g.items() if k != 'regel'}, 'einzelmessung_kandidat': roh}
print('Python-Gegenprobe gepaart:', json.dumps({k: v for k, v in g.items() if k in ('gueltig', 'seite', 'grund')}, ensure_ascii=False),
      {b: (x.get('basis'), x.get('kandidat'), len(x.get('kandidat_werte') or [])) for b, x in (g.get('bereiche') or {}).items()})
print('Einzelmessung Kandidat:', json.dumps(roh, ensure_ascii=False)[:500])

# ---- 3. Rote Spezifikation Teilausfall
spez = A / 'spez'
spez.mkdir(exist_ok=True)
(spez / 'test_spez_laufzeit_gepaart_teilausfall.py').write_text('''"""Rote Spezifikation (nächster Auftrag): Fehlt einer Seite in einem Bereich der Wert (laufzeit_ms None, z. B.
`last_<bereich>` wirft), ist die gepaarte Messung ein Messgerätausfall (gueltig False, seite) — nicht gültig mit
`kandidat: None`, das `laufzeit_einsetzen` stillschweigend überspringt. Gemessen an 330b4ec: Python-Kandidat mit
Syntaxfehler in lagerhaus/formeln/auswertung.py → gueltig True (PYTHON-LAUFZEIT-PROBE, NACHLESE.json)."""
from biotop.kern import messgeraet


def test_teilausfall_kandidat_ist_messgeraetausfall(monkeypatch):
    def messen(werk, bereiche, paket, ref, dateien, zeitlimit_s=150):
        kand = dateien is not None
        return {"gueltig": True, "grund": "", "bereiche": {
            "a": {"laufzeit_ms": 1.0}, "b": ({"laufzeit_ms": None, "laufzeit_fehler": "SyntaxError"} if kand else {"laufzeit_ms": 2.0})}}
    monkeypatch.setattr(messgeraet, "laufzeit_messen", messen)
    r = messgeraet.laufzeit_gepaart(".", ["a", "b"], "p", "last", None, {"x": "y"}, n=3)
    assert r["gueltig"] is False and r.get("seite") == "kandidat", r


def test_gegenprobe_vollstaendige_messung_bleibt_gueltig(monkeypatch):
    monkeypatch.setattr(messgeraet, "laufzeit_messen", lambda *a, **k: {"gueltig": True, "grund": "", "bereiche": {
        "a": {"laufzeit_ms": 1.0}, "b": {"laufzeit_ms": 2.0}}})
    r = messgeraet.laufzeit_gepaart(".", ["a", "b"], "p", "last", None, {"x": "y"}, n=3)
    assert r["gueltig"] is True and r["bereiche"]["b"]["kandidat"] == 2.0, r
''')
p = subprocess.run(['/root/biotop-t3/venv/bin/python', '-m', 'pytest', str(spez / 'test_spez_laufzeit_gepaart_teilausfall.py'), '-q',
                    '-p', 'no:cacheprovider', '--rootdir', str(spez), '--tb=line'], capture_output=True, text=True,
                   env=dict(os.environ, PYTHONPATH='/root/biotop'), cwd=str(spez), timeout=120)
kopf = subprocess.run(['git', '-C', '/root/biotop', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
aus['spez_teilausfall'] = {'commit': kopf, 'rc': p.returncode, 'ausgabe': p.stdout.strip()[-800:]}
print(f'Spezifikation an {kopf}: rc={p.returncode}', p.stdout.strip().splitlines()[-3:])
(A / 'NACHLESE.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1, default=str))
