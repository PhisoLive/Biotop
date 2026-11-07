"""Behebungsrunde 5 — t4_groesse.py korrigieren (vor seinem Lauf in der Kette): Bereich `werk` als Unterpaket
(grosswerk/werk/m*.py), Testdateien `tests/test_werk_*` (Zuordnung des Messgeräts zum Bereich über den Dateinamen);
ohne das baute der Stand nicht (`import grosswerk.werk`)."""
from pathlib import Path

p = Path('/root/biotop-vor-t4-05/proben/t4_groesse.py')
t = p.read_text()
ERS = [
    ("            out[f'tests/test_{n}_{k}.py'] = (f'from {PAKET}.m{m} import {n}\\n\\n\\ndef test_{n}_{k}():\\n'",
     "            out[f'tests/test_werk_{n}_{k}.py'] = (f'from {PAKET}.werk.m{m} import {n}\\n\\n\\ndef test_{n}_{k}():\\n'"),
    ("    (w / PAKET).mkdir(parents=True)\n", "    (w / PAKET / 'werk').mkdir(parents=True)\n"),
    ("    (w / PAKET / '__init__.py').write_text('')\n",
     "    (w / PAKET / '__init__.py').write_text('')\n    (w / PAKET / 'werk' / '__init__.py').write_text('')\n"),
    ("    (w / 'tests' / 'test_grund.py').write_text('def test_grund():\\n    assert True\\n')\n",
     "    (w / 'tests' / 'test_werk_grund.py').write_text('def test_werk_grund():\\n    assert True\\n')\n"),
    ("        (w / PAKET / f'm{m}.py').write_text(modul_quelle(m, set()))\n        code[f'{PAKET}/m{m}.py'] = modul_quelle(m, geaendert)\n",
     "        (w / PAKET / 'werk' / f'm{m}.py').write_text(modul_quelle(m, set()))\n        code[f'{PAKET}/werk/m{m}.py'] = modul_quelle(m, geaendert)\n"),
    ("       + ''.join(f'    from {PAKET}.m{m} import '", "       + ''.join(f'    from {PAKET}.werk.m{m} import '"),
]
for alt, neu in ERS:
    assert t.count(alt) == 1, alt[:80]
for alt, neu in ERS:
    t = t.replace(alt, neu)
p.write_text(t)
print('t4_groesse.py korrigiert,', len(ERS), 'Ersetzungen')
