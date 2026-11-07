"""Behebungsrunde 4 vor T4 — Wächtertest gegen den Fehler aus 1d9a5aa (Nachspiel): in nachspiel.vorbereiten darf kein
Import einen Namen binden, den die Funktion auch als Wert benutzt (dort überschrieb `from .organe import eichung` die
Maßeichung des Falls; 7 von 7 Nachspielen brachen ab). Die volle Regression enthält kein Nachspiel — der eigentliche
Beleg sind die Nachspiele N1–N3 am Nachtrag-Commit; dieser Test hält nur die Stelle fest. Alles-oder-nichts."""
import py_compile
from pathlib import Path

T = Path('/root/biotop/tests/test_vor_t4_04.py')
t = T.read_text()
zusatz = '''

# ================================================================ Nachtrag: Nachspiel — Import überschreibt keine Fallvariable
def test_nachspiel_vorbereiten_import_ueberschreibt_keine_variable():
    """Fehler in 1d9a5aa: `from .organe import eichung` in nachspiel.vorbereiten band den Namen der Maßeichung des Falls
    neu; alle Nachspiele brachen mit AttributeError ab. Kein Import in vorbereiten darf einen Namen binden, dem die
    Funktion auch einen Wert zuweist. Gegenprobe: die fehlerhafte Fassung wird von derselben Prüfung erkannt."""
    import ast

    def konflikte(quelle: str) -> set[str]:
        fn = next(k for k in ast.parse(quelle).body if isinstance(k, ast.FunctionDef) and k.name == "vorbereiten")
        importiert = {a.asname or a.name.split(".")[0] for n in ast.walk(fn) if isinstance(n, (ast.Import, ast.ImportFrom))
                      for a in n.names}
        zugewiesen = {z.id for n in ast.walk(fn) if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign))
                      for z in ast.walk(n) if isinstance(z, ast.Name) and isinstance(z.ctx, ast.Store)}
        return importiert & zugewiesen
    quelle = (Path(__file__).parent.parent / "biotop/nachspiel.py").read_text()
    assert konflikte(quelle) == set(), konflikte(quelle)
    kaputt = quelle.replace("from .organe import eichung as eichung_organ, vorspann", "from .organe import eichung, vorspann")
    assert kaputt != quelle and konflikte(kaputt) == {"eichung"}
'''
if 'def test_nachspiel_vorbereiten_import_ueberschreibt_keine_variable' in t:
    raise SystemExit('schon vorhanden, nichts geschrieben')
T.write_text(t + zusatz)
py_compile.compile(str(T), doraise=True)
print('Wächtertest angehängt')
