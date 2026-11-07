"""Kern: Anmeldung — Benutzer, Kennwort, Token. Fest verdrahtet, nicht abschaltbar.
Alle Routen des Dienstes (dienst.py) verlangen einen gültigen Token.
"""

from __future__ import annotations

import hashlib
import hmac
import os
import secrets
import sqlite3

from . import protokoll
from .datenbank import transaktion


def _hash(kennwort: str, salz: str) -> str:
    return hashlib.pbkdf2_hmac("sha256", kennwort.encode(), bytes.fromhex(salz), 200_000).hex()


def benutzer_anlegen(con: sqlite3.Connection, name: str, kennwort: str) -> None:
    if len(kennwort) < 12:
        raise ValueError("Kennwort muss mindestens 12 Zeichen haben")
    salz = secrets.token_hex(16)
    with transaktion(con):
        con.execute("INSERT OR REPLACE INTO benutzer(name, salz, hash, erstellt_am) VALUES (?,?,?,?)",
                    (name, salz, _hash(kennwort, salz), protokoll.jetzt()))
    protokoll.schreiben(con, "anmeldung.benutzer", name=name)


def anmelden(con: sqlite3.Connection, name: str, kennwort: str) -> str | None:
    """Prüft Benutzer und Kennwort; liefert einen neuen Token oder None."""
    z = con.execute("SELECT salz, hash FROM benutzer WHERE name=?", (name,)).fetchone()
    if not z or not hmac.compare_digest(_hash(kennwort, z["salz"]), z["hash"]):
        protokoll.schreiben(con, "anmeldung.fehlgeschlagen", name=name)
        return None
    token = secrets.token_urlsafe(32)
    with transaktion(con):
        con.execute("INSERT INTO tokens(token_hash, benutzer, erstellt_am) VALUES (?,?,?)",
                    (hashlib.sha256(token.encode()).hexdigest(), name, protokoll.jetzt()))
    protokoll.schreiben(con, "anmeldung.token", name=name)
    return token


def pruefen(con: sqlite3.Connection, token: str | None) -> str | None:
    """Liefert den Benutzernamen zu einem gültigen Token, sonst None."""
    if not token:
        return None
    z = con.execute("SELECT benutzer FROM tokens WHERE token_hash=?", (hashlib.sha256(token.encode()).hexdigest(),)).fetchone()
    return z["benutzer"] if z else None
