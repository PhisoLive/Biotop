"""Echte Rissprobe durch den Annahmepfad (Behebungsrunde 3 vor T4; Review 02: „Die Bestätigungsmessung ist nie echt auf
dem Laufweg gelaufen — 0 von 7 Nachspiel-Entscheidungen hatten einen Riss“).

aegis.pruefen am Python-Prüfwerk aus tests/test_vor_t4_03.py in der echten Kammer (biotop-kammer:1), Nische 'sicher';
gestellt ist NUR das Modell (KEIN ANGRIFF). Laufzeit, Maß, Verhaltensvergleich: echt.
  riss        Kandidat entfernt toten Code (_alt → Kernmaß +1) UND macht `quadrat` langsam (Rechenschleife) —
              Erwartung: Laufzeitriss, gepaarte Nachmessung läuft wirklich, Riss bestätigt → abgelehnt (Grenzmaß)
  gegenprobe  derselbe Kandidat ohne Verlangsamung — Erwartung: kein Riss, keine Nachmessung, überlebt
Kein Modellgeld. Aufruf: python rissprobe_echt.py > RISSPROBE-ECHT.txt"""
import json
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, '/root/biotop')
sys.path.insert(0, '/root/biotop/tests')
from biotop.kern import datenbank, messgeraet  # noqa: E402
from biotop.organe import aegis, kammer  # noqa: E402
import test_vor_t4_03 as t  # noqa: E402

kammer.IMAGE = 'biotop-kammer:1'
aegis.aufrufen = lambda *a, **k: SimpleNamespace(text='KEIN ANGRIFF')
TOT = '''def _alt(text: str) -> str:
    """Frühere Fassung, nirgends aufgerufen (toter Code — Vulture zählt ihn)."""
    return text.strip()


'''
assert t.QUELLE.count(TOT) == 1
ohne_tot = t.QUELLE.replace(TOT, '')
langsam = ohne_tot.replace('    return x * x\n', '    s = 0\n    for i in range(300000):\n        s += i % 3\n    return x * x + 0 * s\n')
assert langsam != ohne_tot
head = subprocess.run(['git', '-C', '/root/biotop', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
st = subprocess.run(['git', '-C', '/root/biotop', 'status', '--short', '--', 'biotop', 'tests'], capture_output=True, text=True).stdout.strip()
aus = {'_meta': {'commit': head, 'arbeitsbaum_sauber': st == '', 'kammer': kammer.IMAGE, 'modellaufrufe': 0}}
for name, neu, erwartung in (('riss', langsam, 'abgelehnt'), ('gegenprobe', ohne_tot, 'ueberlebt')):
    with tempfile.TemporaryDirectory() as d:
        w = Path(d) / 'werk'
        t._anlegen(w)
        con = sqlite3.connect(':memory:', isolation_level=None)
        con.row_factory = sqlite3.Row
        con.executescript(datenbank.SCHEMA)
        con.execute("INSERT INTO kandidaten(id,lauf_id,generation,bereich,nische,status,diff) VALUES(7,1,1,'werk','sicher','erzeugt',?)",
                    (t._diff(t.QUELLE, neu),))
        basis = messgeraet.messen(w, ['werk'], t.PAKET, t.REFERENZLAST)
        assert basis['gueltig'], basis.get('grund')
        zaehl = {'gepaart': 0}
        orig = messgeraet.laufzeit_gepaart

        def gepaart(*a, **k):
            zaehl['gepaart'] += 1
            return orig(*a, **k)
        messgeraet.laufzeit_gepaart = gepaart
        try:
            u = aegis.pruefen(con, 1, 1, 7, w, t.PAKET, ['werk'], [], basis, basis, t.REFERENZLAST,
                              {'_rauschtoleranz': {'werk': 1.2}})
        finally:
            messgeraet.laufzeit_gepaart = orig
        z = json.loads(con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr DESC LIMIT 1").fetchone()[0])
        nm = z.get('laufzeit_nachmessung')
        aus[name] = {'status': u['status'], 'grund': u['grund'][:600], 'erwartung': erwartung,
                     'erwartung_erfuellt': u['status'] == erwartung, 'gepaarte_messungen': zaehl['gepaart'],
                     'laufzeit_nachmessung': nm, 'kernmass_basis': messgeraet.kernmass(basis),
                     'verhalten': {k: (z.get('verhalten') or {}).get(k) for k in ('grund_art', 'anzahl_abweichungen', 'beobachtete_funktionen')}}
        print(f"{name:10} status={u['status']:10} erwartet={erwartung:10} erfüllt={u['status'] == erwartung} "
              f"gepaart={zaehl['gepaart']} nachmessung={json.dumps(nm, ensure_ascii=False)[:500]} | {u['grund'][:300]}", flush=True)
Path(__file__).with_name('RISSPROBE-ECHT.json').write_text(json.dumps(aus, ensure_ascii=False, indent=1))
print('meta', aus['_meta'])
