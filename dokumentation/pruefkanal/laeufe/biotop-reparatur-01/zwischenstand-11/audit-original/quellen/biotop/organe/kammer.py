"""Organ 3.13: Ausführungskammer.

Jeder Bau, Testlauf, jede Messung läuft in einem Docker-Container:
- kein Netz (--network none),
- eigenes Dateisystem je Kandidat (Kopie des Werks, danach verworfen),
- Zeit- und Speicherlimit,
- unprivilegierter Benutzer, read-only Wurzel, PID-Limit.

Fremdcode wird nie auf dem Wirt ausgeführt. Ein Lauf, der das Limit reißt,
gilt als gescheitert (Rückgabe `zeitlimit=True`, rc=124).
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import uuid
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import asdict, dataclass
from pathlib import Path

IMAGE = os.environ.get("BIOTOP_KAMMER_IMAGE", "biotop-kammer:1")
ZEITLIMIT_S = int(os.environ.get("BIOTOP_KAMMER_ZEITLIMIT", "120"))
SPEICHER = os.environ.get("BIOTOP_KAMMER_SPEICHER", "512m")


@dataclass
class Ergebnis:
    rc: int
    stdout: str
    stderr: str
    dauer_s: float
    zeitlimit: bool
    container: str


def _kopie(werk: Path, ziel: Path) -> None:
    shutil.copytree(
        werk, ziel, symlinks=False,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache", "node_modules", ".env*"),
    )


def _ausfuehren(werk: Path, befehl: list[str], zeitlimit_s: int | None = None,
               dateien: dict[str, str] | None = None) -> Ergebnis:
    """Kopiert `werk` in ein Wegwerfverzeichnis, legt optional `dateien`
    (Pfad → Inhalt, relativ zum Werk) hinein und führt `befehl` im Container aus.
    """
    zeit = zeitlimit_s or ZEITLIMIT_S
    name = f"biotop-{uuid.uuid4().hex[:12]}"
    tmp = Path(tempfile.mkdtemp(prefix="kammer-"))
    try:
        arbeit = tmp / "werk"
        _kopie(werk, arbeit)
        for rel, inhalt in (dateien or {}).items():
            p = arbeit / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(inhalt)
        # Der Kammer-Benutzer (uid 10001) braucht Schreibrecht für pytest-Artefakte.
        subprocess.run(["chown", "-R", "10001:10001", str(arbeit)], check=True)
        cmd = [
            "docker", "run", "--rm", "--name", name,
            "--network", "none",
            "--memory", SPEICHER, "--memory-swap", SPEICHER,
            "--cpus", "1", "--pids-limit", "256",
            "--read-only", "--tmpfs", "/tmp:rw,size=64m",
            "--security-opt", "no-new-privileges",
            "--cap-drop", "ALL",
            "-v", f"{arbeit}:/werk:rw",
            "-w", "/werk",
            "-e", "PYTHONDONTWRITEBYTECODE=1", "-e", "HOME=/tmp",
            IMAGE, *befehl,
        ]
        import time
        t0 = time.monotonic()
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=zeit + 5)
            dauer = time.monotonic() - t0
            return Ergebnis(p.returncode, p.stdout[-20000:], p.stderr[-20000:], dauer, False, name)
        except subprocess.TimeoutExpired as e:
            dauer = time.monotonic() - t0
            subprocess.run(["docker", "kill", name], capture_output=True)
            subprocess.run(["docker", "rm", "-f", name], capture_output=True)
            out = (e.stdout or b"")
            err = (e.stderr or b"")
            out = out.decode(errors="replace") if isinstance(out, bytes) else out
            err = err.decode(errors="replace") if isinstance(err, bytes) else err
            return Ergebnis(124, out[-20000:], err[-20000:] + f"\n[Kammer] Zeitlimit {zeit}s überschritten, Container {name} getötet", dauer, True, name)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


_ZAEHLUNGEN: ContextVar[tuple] = ContextVar("kammerzaehlungen", default=())


@contextmanager
def zaehlung():
    """Kontextlokale Rohbelege aller tatsächlichen Kammeraufrufe, auch verschachtelt."""
    aufrufe = []
    token = _ZAEHLUNGEN.set((*_ZAEHLUNGEN.get(), aufrufe))
    try:
        yield aufrufe
    finally:
        _ZAEHLUNGEN.reset(token)


def ausfuehren(werk: Path, befehl: list[str], zeitlimit_s: int | None = None,
               dateien: dict[str, str] | None = None) -> Ergebnis:
    ergebnis = _ausfuehren(werk, befehl, zeitlimit_s, dateien)
    for zaehler in _ZAEHLUNGEN.get():
        zaehler.append({**asdict(ergebnis), "befehl": list(befehl)})
    return ergebnis


def bereit() -> tuple[bool, str]:
    p = subprocess.run(["docker", "image", "inspect", IMAGE], capture_output=True, text=True)
    if p.returncode != 0:
        return False, f"Kammer-Image {IMAGE} fehlt"
    return True, IMAGE
