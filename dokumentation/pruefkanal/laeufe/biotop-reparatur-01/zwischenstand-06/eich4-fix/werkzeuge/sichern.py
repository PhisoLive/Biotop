"""Privater Ausgang + Quellschutzinventar, ohne produktive DB-Verbindung."""
import hashlib
import json
import shutil
import sqlite3
from pathlib import Path

ROOT = Path('/root/reparatur-01/nachbesserung-01/vertrag')
ROOT.mkdir(exist_ok=True)
for name in ('ausgaben', 'tmp', 'guard'):
    (ROOT / name).mkdir(exist_ok=True)


def inventar():
    result = {}
    for root in (Path('/root/biotop'), Path('/root/reparatur-01/teil-eichung/werk-lauf25-kopie'),
                 Path('/root/reparatur-01/ausgang.db')):
        files = sorted(root.rglob('*')) if root.is_dir() else [root]
        for p in files:
            if p.is_file():
                s = p.stat()
                result[str(p)] = dict(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                                      bytes=s.st_size, mtime_ns=s.st_mtime_ns)
    return result


if __name__ == '__main__':
    assert not (ROOT / 'ausgang-repo').exists()
    (ROOT / 'ausgaben/quellschutz-vorher.json').write_text(json.dumps(inventar(), indent=2))
    shutil.copytree(ROOT / 'repo', ROOT / 'ausgang-repo')
    shutil.copytree('/root/reparatur-01/teil-eichung/werk-lauf25-kopie', ROOT / 'werk-lauf25-kopie')
    with sqlite3.connect('file:/root/reparatur-01/ausgang.db?mode=ro', uri=True) as src:
        with sqlite3.connect(ROOT / 'privat.db') as dst:
            src.backup(dst)
    (ROOT / 'privat.db').chmod(0o600)
    shutil.copy2(ROOT / 'privat.db', ROOT / 'privat-sicherung.db')
    print('Ausgangskopie und private DB-Sicherung angelegt; Schutzinventar:', len(inventar()), 'Dateien')
