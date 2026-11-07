"""Kern: Protokoll — jeder Aufruf, jedes Ergebnis, unveränderlich, fortlaufend
nummeriert. Jede Zeile trägt den Hash der Vorzeile (Kette); eine nachträgliche
Änderung bricht die Kette und ist mit `pruefen()` nachweisbar.
"""

from __future__ import annotations

import hashlib
import sqlite3
from datetime import datetime, timezone

from .datenbank import j, transaktion


def jetzt() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def schreiben(con: sqlite3.Connection, art: str, **inhalt) -> int:
    """Hängt eine Zeile an. Rückgabe: laufende Nummer."""
    with transaktion(con):
        letzte = con.execute("SELECT hash FROM protokoll ORDER BY nr DESC LIMIT 1").fetchone()
        hash_vor = letzte["hash"] if letzte else "0" * 64
        zeit = jetzt()
        inhalt_s = j(inhalt)
        h = hashlib.sha256(f"{hash_vor}|{zeit}|{art}|{inhalt_s}".encode()).hexdigest()
        cur = con.execute(
            "INSERT INTO protokoll(zeit, art, inhalt, hash_vor, hash) VALUES (?,?,?,?,?)",
            (zeit, art, inhalt_s, hash_vor, h),
        )
        return cur.lastrowid


def pruefen(con: sqlite3.Connection) -> tuple[bool, int]:
    """Prüft die Hash-Kette. Rückgabe (in Ordnung, geprüfte Zeilen)."""
    vor = "0" * 64
    n = 0
    for z in con.execute("SELECT * FROM protokoll ORDER BY nr"):
        n += 1
        erwartet = hashlib.sha256(
            f"{z['hash_vor']}|{z['zeit']}|{z['art']}|{z['inhalt']}".encode()
        ).hexdigest()
        if z["hash_vor"] != vor or z["hash"] != erwartet:
            return False, n
        vor = z["hash"]
    return True, n


def lesen(con: sqlite3.Connection, ab: int = 0, art: str | None = None, limit: int = 200):
    q = "SELECT * FROM protokoll WHERE nr > ?"
    p: list = [ab]
    if art:
        q += " AND art = ?"
        p.append(art)
    q += " ORDER BY nr LIMIT ?"
    p.append(limit)
    return [dict(z) for z in con.execute(q, p)]
