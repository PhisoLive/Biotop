"""Konsistenter Lese-Schnappschuss von t3.db einschließlich WAL (SQLite-Backup-API) — und Nachweis, was die
`immutable=1`-Lesung übersehen hat. Das Original wird nur gelesen (mode=ro); Prüfsummen vorher/nachher belegen das."""
import hashlib
import json
import sqlite3
from pathlib import Path

Q = Path('/root/biotop-t3/t3.db')
WAL = Path('/root/biotop-t3/t3.db-wal')
Z = Path('/root/biotop-t3/schnappschuss-abschluss3/t3.db')


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def zustand():
    return {p.name: {'sha256': sha(p), 'bytes': p.stat().st_size, 'mtime_ns': p.stat().st_mtime_ns} for p in (Q, WAL)}


vorher = zustand()
Z.parent.mkdir(exist_ok=True)
if Z.exists():
    Z.unlink()
src = sqlite3.connect(f'file:{Q}?mode=ro', uri=True)
dst = sqlite3.connect(Z)
src.backup(dst)
src.close()
dst.close()
nachher = zustand()
print(json.dumps({'original_vorher': vorher, 'original_nachher': nachher, 'original_unveraendert': vorher == nachher,
                  'schnappschuss': str(Z), 'schnappschuss_sha256': sha(Z), 'schnappschuss_bytes': Z.stat().st_size},
                 indent=1))

alt = sqlite3.connect(f'file:{Q}?mode=ro&immutable=1', uri=True)
neu = sqlite3.connect(f'file:{Z}?mode=ro&immutable=1', uri=True)
print('\nGegenüberstellung immutable-Lesung (ohne WAL) gegen Schnappschuss (mit WAL):')
for q in ("SELECT COUNT(*), MAX(nr), MAX(zeit) FROM protokoll",
          "SELECT COUNT(*), MAX(id) FROM kandidaten",
          "SELECT COUNT(*) FROM kasse",
          "SELECT COUNT(*) FROM immunsystem",
          "SELECT COUNT(*) FROM generationen WHERE lauf_id=38",
          "SELECT nummer, status, freigabe_am FROM generationen WHERE lauf_id=38 AND nummer>=16 ORDER BY nummer",
          "SELECT nummer FROM generationen WHERE lauf_id=38 AND status='angenommen' ORDER BY nummer"):
    a = alt.execute(q).fetchall()
    n = neu.execute(q).fetchall()
    print(f'  {q}\n     immutable   : {a}\n     schnappschuss: {n}\n     gleich: {a == n}')
