"""Review guard: no network, Docker, git, production database, or source writes."""
import os
import socket
import sys
from pathlib import Path

OUT = Path('/root/reparatur-01/eltern-reviewpruefung/pruefer-eichung').resolve()
SOURCE = Path('/root/reparatur-01/eltern-reviewpruefung/repo').resolve()

def deny(*args, **kwargs):
    raise AssertionError('Review guard: network forbidden')

socket.socket.connect = deny
socket.socket.connect_ex = deny
socket.create_connection = deny

def audit(event, args):
    if event == 'sqlite3.connect':
        raw = str(args[0])
        if raw != ':memory:':
            if raw.startswith('file:'):
                raw = raw[5:].split('?', 1)[0]
            path = Path(raw).resolve()
            if not path.is_relative_to(OUT):
                raise AssertionError('Review guard: DB outside review output: ' + str(path))
    elif event == 'subprocess.Popen':
        executable = Path(str(args[0])).name
        if not executable.startswith(('python', 'pytest')):
            raise AssertionError('Review guard: external command forbidden: ' + str(args[0]))
    elif event == 'open':
        path, mode, flags = args
        if isinstance(path, (str, bytes)):
            path = Path(os.fsdecode(path)).resolve()
            writing = flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
            if writing and path.is_relative_to(SOURCE):
                raise AssertionError('Review guard: source write forbidden: ' + str(path))
    elif event in ('os.remove', 'os.rmdir', 'os.mkdir', 'os.chmod', 'os.utime'):
        raw = args[0]
        if isinstance(raw, (str, bytes)) and Path(os.fsdecode(raw)).resolve().is_relative_to(SOURCE):
            raise AssertionError('Review guard: source mutation forbidden: ' + event)
    elif event == 'os.rename':
        if any(isinstance(raw, (str, bytes)) and Path(os.fsdecode(raw)).resolve().is_relative_to(SOURCE) for raw in args[:2]):
            raise AssertionError('Review guard: source rename forbidden')

sys.addaudithook(audit)
