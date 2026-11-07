"""Diagnose der T4-Größen-Messung (nur lesen und messen, kein Eingriff in den Commit): warum bleiben ohne Kappe 168 von
324 Abweichungen ungedeckt? Derselbe Aufbau wie t4_groesse.py (importiert), ohne Kappe; schreibt Aufschlüsselung,
festhaltend und Klassen je Test. Aufruf: python t4_diagnose.py <baumkopie> > T4-DIAGNOSE.txt"""
import json
import sqlite3
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

sys.argv = [sys.argv[0], sys.argv[1]]
sys.path.insert(0, str(Path(__file__).parent))
import t4_groesse as T  # noqa: E402

geaendert = {f'm{m}_f{f}' for m in range(T.N_MODULE) for f in range(T.F_JE_MODUL)}
geaendert = set(sorted(geaendert)[:T.G_GEAENDERT * 2:2])
with tempfile.TemporaryDirectory(dir='/tmp') as d:
    w = Path(d) / 'werk'
    code = T.anlegen(w, geaendert)
    con = sqlite3.connect(':memory:', isolation_level=None)
    con.row_factory = sqlite3.Row
    con.executescript(T.datenbank.SCHEMA)
    con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,'werk','sicher','erzeugt',?)",
                (T.diff(w, code),))
    T.aegis.aufrufen = lambda *a, **k: SimpleNamespace(text='KEIN ANGRIFF')
    basis = T.messgeraet.messen(w, ['werk'], T.PAKET, T.REF)
    T.messgeraet.laufzeit_messen = lambda werk, bereiche, paket, ref, dateien=None, zeitlimit_s=150: \
        {'gueltig': True, 'grund': '', 'bereiche': {b: {'laufzeit_ms': 5.0} for b in bereiche}}
    T.vv.VERFAELSCHUNG_KAPPE = 10 ** 6
    u = T.aegis.pruefen(con, 1, 1, 7, w, T.PAKET, ['werk'], [], basis, basis, T.REF, {'_rauschtoleranz': {'werk': 1.2}},
                        referenzlast_laufzeit=T.REF)
    z = con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr DESC LIMIT 1").fetchone()
    v = json.loads(z[0]).get('verhalten') or {}
    dz = v.get('deckung_zaehlung') or {}
    print('status', u['status'], '|', str(u['grund'])[:200])
    print('tests_fehlgeschlagen basis:', len(basis['werk']['tests_fehlgeschlagen_liste']))
    print('deckende_tests:', len(v.get('deckende_tests') or []))
    print('ungedeckt_aufschluesselung:')
    for k2, n in sorted((v.get('ungedeckt_aufschluesselung') or {}).items()):
        print(f'   {n:4}  {k2}')
    print('festhaltend (Schlüssel → Anzahl Tests):')
    for k2, t in sorted((dz.get('festhaltend') or {}).items()):
        print(f'   {len(t):3}  {k2}')
    kj = dz.get('klassen_je_test') or {}
    print('klassen_je_test (Auszug m0_f2, m0_f4):')
    for t, fs in sorted(kj.items()):
        for f, kl in fs.items():
            if f.endswith(('m0_f2', 'm0_f4')):
                print(f'   {t} → {f}: {kl}')
    print('eingaben (erste ungedeckte):', json.dumps(v.get('eingaben'), ensure_ascii=False)[:600])
    print('werte (erste):', json.dumps(v.get('werte'), ensure_ascii=False)[:600])
