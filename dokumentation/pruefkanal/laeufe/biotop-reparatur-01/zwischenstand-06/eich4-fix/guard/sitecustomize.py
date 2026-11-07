"""EICH-4: Netz gesperrt; DB/Writes/Docker ausschließlich im Teilordner."""
import os
import socket
import sys
from pathlib import Path

ROOT = Path('/root/reparatur-01/nachbesserung-01/vertrag').resolve()
TMP = ROOT / 'tmp'


def privat(raw):
    return Path(os.fsdecode(raw)).resolve().is_relative_to(ROOT)


def deny(*args, **kwargs):
    raise AssertionError('EICH-4: Netz-/Modellaufrufe gesperrt')


socket.socket.connect = deny
socket.socket.connect_ex = deny
socket.create_connection = deny


def audit(event, args):
    if event == 'sqlite3.connect':
        raw = str(args[0])
        if raw == ':memory:':
            return
        if raw.startswith('file:'):
            raw = raw[5:].split('?', 1)[0]
        assert privat(raw), 'EICH-4: DB außerhalb Teilordner: ' + raw
    elif event == 'subprocess.Popen':
        cmd = args[1]
        assert isinstance(cmd, (list, tuple)), 'EICH-4: keine Shell'
        name = Path(str(cmd[0])).name
        if name == 'chown':
            assert len(cmd) == 4 and cmd[1:3] == ['-R', '10001:10001'] and Path(cmd[3]).resolve().is_relative_to(TMP)
        elif name == 'docker':
            if cmd[1] == 'run':
                assert cmd[cmd.index('--network')+1] == 'none'
                assert 'biotop-kammer:1' in cmd and '--read-only' in cmd
                mount = cmd[cmd.index('-v')+1]
                assert mount.endswith(':/werk:rw') and Path(mount[:-9]).resolve().is_relative_to(TMP)
            else:
                assert cmd[1] in ('kill', 'rm') and cmd[-1].startswith('biotop-')
        else:
            assert name.startswith(('python', 'pytest')), 'EICH-4: fremder Prozess: ' + name
    elif event == 'open':
        p, mode, flags = args
        if isinstance(p, (str, bytes)) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
            assert str(p) == '/dev/null' or privat(p), 'EICH-4: Write außerhalb Teilordner: ' + str(p)
    elif event in ('os.remove', 'os.rmdir', 'os.mkdir', 'os.chmod', 'os.utime', 'os.rename'):
        for p in args[:2] if event == 'os.rename' else args[:1]:
            if isinstance(p, (str, bytes)) and os.path.isabs(p):
                assert privat(p), 'EICH-4: Mutation außerhalb Teilordner: ' + str(p)


assert os.environ['TMPDIR'] == str(TMP)
sys.addaudithook(audit)
