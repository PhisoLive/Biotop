"""Behebungsrunde 4 vor T4 — Fehler im Commit 1d9a5aa (eigener Fehler, gefunden durch die Nachspiele D1–D3):
In nachspiel.vorbereiten band `from .organe import eichung, vorspann` den Namen `eichung` neu — er hielt vorher die
Maßeichung (dict) des Falls. Der Fall trug danach das Modul statt der Eichung, und `spielen` brach ab:
„AttributeError: module 'biotop.organe.eichung' has no attribute 'get'“ — 7 von 7 Nachspielen, kein Urteil.
Behebung: das Organ unter eigenem Namen importieren. Alles-oder-nichts.
"""
import py_compile
from pathlib import Path

N = Path('/root/biotop/biotop/nachspiel.py')
s = N.read_text()
ops = [
    ("""        from .organe import eichung, vorspann
        r2 = eichung.rauschmessung(con, lauf_id, werk["id"], ziel, bereiche, paket, tausch["_referenzlast_laufzeit"],
                                   eichung.laufzeit_einmal)""",
     """        # eigener Name: `eichung` ist in dieser Funktion die Maßeichung des Falls (Fehler in 1d9a5aa: der Import
        # überschrieb sie, alle Nachspiele D1–D3 brachen ab)
        from .organe import eichung as eichung_organ, vorspann
        r2 = eichung_organ.rauschmessung(con, lauf_id, werk["id"], ziel, bereiche, paket, tausch["_referenzlast_laufzeit"],
                                         eichung_organ.laufzeit_einmal)"""),
]
fehl = [a[:60] for a, b in ops if s.count(a) != 1]
if fehl:
    raise SystemExit(f'Anker fehlen, nichts geschrieben: {fehl}')
for a, b in ops:
    s = s.replace(a, b)
N.write_text(s)
py_compile.compile(str(N), doraise=True)
# Probe: der Name `eichung` wird in vorbereiten nirgends mehr durch einen Import gebunden
import ast
baum = ast.parse(s)
fn = next(k for k in baum.body if isinstance(k, ast.FunctionDef) and k.name == 'vorbereiten')
gebunden = [a.asname or a.name for n in ast.walk(fn) if isinstance(n, (ast.Import, ast.ImportFrom)) for a in n.names]
assert 'eichung' not in gebunden, gebunden
print('nachspiel.py: 1 von 1 Ersetzung, kompiliert; Importe in vorbereiten:', gebunden)
