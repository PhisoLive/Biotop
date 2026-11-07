"""Organ 3.9: Lazarus — jede angenommene Generation ist ein vollständiger,
rückholbarer Zustand.

Technik: Git-Tag je Generation im Werk-Repository plus Archiv (tar.gz) des
vollständigen Werks mit Prüfsumme über alle Dateien (sortierte Liste
Pfad:SHA256, davon SHA256) und dem Maßstand.
Rückkehr zu Generation n stellt Werk, Landkarte (Prüfsummen erzwingen Neuaufbau)
und Maß-Verlauf (Generationen > n werden als „verworfen_durch_rueckkehr“ markiert,
nicht gelöscht) zurück. Nichts wird gelöscht.
"""

from __future__ import annotations

import hashlib
import shutil
import sqlite3
import subprocess
import tarfile
from pathlib import Path

from ..kern import protokoll
from ..kern.datenbank import j, lj, transaktion

ARCHIV = Path("/root/biotop/daten/lazarus")
AUSSCHLUSS = {".git", "__pycache__", ".pytest_cache", "node_modules", "dist", "coverage", ".tools"}


def pruefsumme_werk(werk: Path) -> tuple[str, int]:
    """SHA256 über die sortierte Liste „relpfad:sha256(inhalt)“. Rückgabe (hash, dateien)."""
    zeilen = []
    for p in sorted(werk.rglob("*")):
        if not p.is_file() or any(t in AUSSCHLUSS for t in p.parts) or p.name.startswith(".env"):
            continue
        zeilen.append(f"{p.relative_to(werk)}:{hashlib.sha256(p.read_bytes()).hexdigest()}")
    return hashlib.sha256("\n".join(zeilen).encode()).hexdigest(), len(zeilen)


def _git(werk: Path, *args: str) -> str:
    p = subprocess.run(["git", "-c", "user.name=biotop", "-c", "user.email=biotop@local", *args],
                       cwd=werk, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {p.stderr.strip()}")
    return p.stdout.strip()


def sicherstellen_repo(werk: Path) -> None:
    if not (werk / ".git").exists():
        _git(werk, "init", "-q", "-b", "main")
        (werk / ".gitignore").write_text("__pycache__/\n*.pyc\n.pytest_cache/\n.env*\n")
        _git(werk, "add", "-A")
        _git(werk, "commit", "-qm", "Biotop: Aufnahme")


def schnappschuss(con: sqlite3.Connection, lauf_id: int, generation: int, werk: Path, masse: dict) -> dict:
    sicherstellen_repo(werk)
    tag = f"lauf{lauf_id}-gen{generation}"
    _git(werk, "add", "-A")
    st = _git(werk, "status", "--porcelain")
    if st:
        _git(werk, "commit", "-qm", f"Biotop Lauf {lauf_id} Generation {generation}")
    _git(werk, "tag", "-f", tag)
    ps, n = pruefsumme_werk(werk)
    ARCHIV.mkdir(parents=True, exist_ok=True)
    archiv = ARCHIV / f"{tag}.tar.gz"
    with tarfile.open(archiv, "w:gz") as t:
        for p in sorted(werk.rglob("*")):
            if p.is_file() and not any(x in AUSSCHLUSS for x in p.parts) and not p.name.startswith(".env"):
                t.add(p, arcname=str(p.relative_to(werk)))
    with transaktion(con):
        con.execute(
            "INSERT INTO lazarus(lauf_id, generation, tag, archiv, pruefsumme, masse, erstellt_am) VALUES (?,?,?,?,?,?,?) "
            "ON CONFLICT(lauf_id, generation) DO UPDATE SET tag=excluded.tag, archiv=excluded.archiv, pruefsumme=excluded.pruefsumme, "
            "masse=excluded.masse, erstellt_am=excluded.erstellt_am",
            (lauf_id, generation, tag, str(archiv), ps, j(masse), protokoll.jetzt()))
    protokoll.schreiben(con, "lazarus.schnappschuss", lauf_id=lauf_id, generation=generation, tag=tag, pruefsumme=ps, dateien=n)
    return {"tag": tag, "pruefsumme": ps, "dateien": n, "archiv": str(archiv)}


def liste(con: sqlite3.Connection, lauf_id: int) -> list[dict]:
    return [dict(z) for z in con.execute("SELECT * FROM lazarus WHERE lauf_id=? ORDER BY generation", (lauf_id,))]


def rueckkehr(con: sqlite3.Connection, lauf_id: int, generation: int, werk: Path, ziel: Path | None = None) -> dict:
    """Stellt Generation `generation` her — in `werk` (Standard) oder in `ziel`
    (für Prüfungen ohne Eingriff ins laufende Werk). Rückgabe: Prüfergebnis."""
    z = con.execute("SELECT * FROM lazarus WHERE lauf_id=? AND generation=?", (lauf_id, generation)).fetchone()
    if not z:
        raise KeyError(f"kein Schnappschuss für Lauf {lauf_id} Generation {generation}")
    ziel = ziel or werk
    if ziel == werk:
        # Arbeitskopie aus dem Git-Tag, Landkarte/Verlauf danach markieren
        _git(werk, "checkout", "-q", "-f", z["tag"])
        _git(werk, "checkout", "-q", "-B", "main")
        _git(werk, "clean", "-qfd")
        with transaktion(con):
            con.execute("UPDATE generationen SET status='verworfen_durch_rueckkehr' WHERE lauf_id=? AND nummer>? AND status='angenommen'", (lauf_id, generation))
            werk_id = con.execute("SELECT werk_id FROM laeufe WHERE id=?", (lauf_id,)).fetchone()["werk_id"]
            con.execute("UPDATE landkarte SET pruefsumme='veraltet' WHERE werk_id=? AND stufe<=2", (werk_id,))
    else:
        if ziel.exists():
            shutil.rmtree(ziel)
        ziel.mkdir(parents=True)
        with tarfile.open(z["archiv"]) as t:
            t.extractall(ziel, filter="data")
    ps, n = pruefsumme_werk(ziel)
    stimmt = ps == z["pruefsumme"]
    protokoll.schreiben(con, "lazarus.rueckkehr", lauf_id=lauf_id, generation=generation, tag=z["tag"],
                        ziel=str(ziel), pruefsumme_erwartet=z["pruefsumme"], pruefsumme_gemessen=ps, stimmt=stimmt, dateien=n)
    return {"generation": generation, "tag": z["tag"], "pruefsumme_erwartet": z["pruefsumme"], "pruefsumme_gemessen": ps,
            "stimmt": stimmt, "dateien": n, "masse": lj(z["masse"])}
