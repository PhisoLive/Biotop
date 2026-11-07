"""Reviewer: prohibit Docker/network; allow only private local work."""
import os, socket, sys
from pathlib import Path
ROOT = Path('/root/reparatur-01/review-02/pruefer-kern')
SNAP = ROOT / 'arbeitskopie'
def blocked(*a, **kw):
    raise RuntimeError('Reviewer scope: network disabled')
socket.socket.connect = blocked
socket.create_connection = blocked
def audit(event, args):
    if event == 'subprocess.Popen':
        executable, argv, cwd, env = args
        words = argv if isinstance(argv, (tuple, list)) else [argv]
        if any(Path(str(w)).name in ('docker','curl','wget') for w in words):
            raise RuntimeError('Reviewer scope: Docker/network subprocess forbidden')
    if event == 'sqlite3.connect' and args[0] != ':memory:':
        p = Path(str(args[0]))
        if str(p).startswith('file:') or not p.resolve().is_relative_to(ROOT):
            raise RuntimeError('Reviewer scope: nonprivate database forbidden')
sys.addaudithook(audit)
