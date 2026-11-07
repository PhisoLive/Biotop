"""Diagnose: welche der vier Eichproben/Gegenproben am Python-Paar (test_eichproben.py::paar) nach dem Umbau anders
entscheidet — und warum (Grund, Verhaltensurteil). Nur Lesen/Ausgeben, echte Kammer, kein Modell."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, '/root/biotop')
sys.path.insert(0, '/root/biotop/tests')
import test_eichproben as T  # noqa: E402
from biotop.kern import datenbank, messgeraet  # noqa: E402
from biotop.organe import eichproben, kammer, vertraege, verfassung  # noqa: E402

kammer.IMAGE = 'biotop-kammer:ts1'
tmp = Path(tempfile.mkdtemp(prefix='eich-diag-'))
werk = tmp / 'werk'
for rel, code in {
    "beispiel/__init__.py": "", "beispiel/lieferant/__init__.py": "from .rechnung import wert\n",
    "beispiel/lieferant/rechnung.py": '"""Ein kleiner Lieferant im kopierten Prüfwerk."""\ndef wert(zahl: float) -> float:\n    """Verdoppelt eine Zahl."""\n    ergebnis = zahl * 2\n    return ergebnis\n',
    "tests/test_lieferant.py": "from beispiel.lieferant import wert\n\ndef test_wert():\n    assert wert(2) == 4\n",
    "beispiel/abnehmer/__init__.py": "from .ausgabe import bericht\n",
    "beispiel/abnehmer/ausgabe.py": 'def bericht(zahl: float) -> float:\n    """Berichtet einen Zahlenwert."""\n    ergebnis = zahl + 1\n    return ergebnis\n',
    "tests/test_abnehmer.py": "from beispiel.abnehmer import bericht\n\ndef test_bericht():\n    assert bericht(2) == 3\n"}.items():
    (werk / rel).parent.mkdir(parents=True, exist_ok=True)
    (werk / rel).write_text(code)
con = datenbank.verbinden(tmp / 'paar.db')
con.executescript(verfassung.SCHEMA)
con.execute("INSERT INTO laeufe(id,werk_id,budget_eur,status,mass) VALUES(1,1,0,'angelegt',NULL)")
vertragsdatei = vertraege.einlegen(con, 1, werk, {("abnehmer", "lieferant"): "from beispiel.lieferant import wert\n\ndef test_grenzwert():\n    assert wert(2) == 4\n"}, "isolierte Testfixture")[0]
bereiche = ["abnehmer", "lieferant"]
basis = messgeraet.messen(werk, bereiche, "beispiel", None)
e = eichproben.proben(con, 1, 1, werk, "beispiel", bereiche, [], basis, basis, T.REF_PAAR, {})
for art in ('proben', 'gegenproben'):
    for n, p in e[art].items():
        v = ((p.get('belege') or {}).get('urteil') or {}).get('verhalten') or {}
        print(f"{art:11} {n:12} bestanden={p.get('bestanden')!s:5} pruefbar={p.get('pruefbar')!s:5} status={p.get('status')} | "
              f"{str(p.get('grund'))[:180]} | vv={v.get('grund_art')} {str(v.get('grund'))[:200]}")
