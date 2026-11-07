"""Kern: Datenbank (SQLite, Transaktionen).

Alle Gedächtnisse liegen hier, dauerhaft auf dem Server (Verfassungssatz 9).
Phase 1: eine Datei, ein Prozess. Rollentrennung (eigener Kern-Prozess mit
ausschließlichem Schreibrecht) steht auf der Liste für danach.
"""

from __future__ import annotations

import json
import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PFAD = Path(os.environ.get("BIOTOP_DB", "/root/biotop/daten/biotop.db"))

SCHEMA = """
CREATE TABLE IF NOT EXISTS werke (
  id INTEGER PRIMARY KEY, name TEXT UNIQUE, pfad TEXT, quelle TEXT,
  aufgenommen_am TEXT, bericht TEXT, sprache TEXT, status TEXT);
CREATE TABLE IF NOT EXISTS laeufe (
  id INTEGER PRIMARY KEY, werk_id INTEGER, budget_eur REAL, status TEXT,
  begonnen_am TEXT, beendet_am TEXT, mass TEXT, grund TEXT, richtung TEXT,
  freigabe TEXT);
CREATE TABLE IF NOT EXISTS generationen (
  id INTEGER PRIMARY KEY, lauf_id INTEGER, nummer INTEGER, status TEXT,
  masse TEXT, tag TEXT, pruefsumme TEXT, grund TEXT, erstellt_am TEXT,
  freigabe_am TEXT, freigabe_grund TEXT, kandidaten TEXT,
  UNIQUE(lauf_id, nummer));
CREATE TABLE IF NOT EXISTS kandidaten (
  id INTEGER PRIMARY KEY, lauf_id INTEGER, generation INTEGER, bereich TEXT,
  nische TEXT, anbieter TEXT, modell TEXT, diff TEXT, begruendung TEXT,
  status TEXT, grund TEXT, masse TEXT, wirkungskreis TEXT, erstellt_am TEXT,
  ist_probe INTEGER DEFAULT 0);
CREATE TABLE IF NOT EXISTS protokoll (
  nr INTEGER PRIMARY KEY, zeit TEXT, art TEXT, inhalt TEXT,
  hash_vor TEXT, hash TEXT);
CREATE TABLE IF NOT EXISTS kasse (
  id INTEGER PRIMARY KEY, lauf_id INTEGER, zeit TEXT, anbieter TEXT,
  modell TEXT, tokens_ein INTEGER, tokens_aus INTEGER, kosten_eur REAL,
  zweck TEXT, kontingent INTEGER, protokoll_nr INTEGER);
CREATE TABLE IF NOT EXISTS landkarte (
  id INTEGER PRIMARY KEY, werk_id INTEGER, stufe INTEGER, schluessel TEXT,
  inhalt TEXT, pruefsumme TEXT, erstellt_am TEXT, herkunft TEXT,
  UNIQUE(werk_id, stufe, schluessel));
CREATE TABLE IF NOT EXISTS strassen (
  id INTEGER PRIMARY KEY, werk_id INTEGER, von TEXT, nach TEXT, art TEXT,
  UNIQUE(werk_id, von, nach, art));
CREATE TABLE IF NOT EXISTS vertraege (
  id INTEGER PRIMARY KEY, werk_id INTEGER, bereich TEXT, text TEXT,
  herkunft TEXT, quelle TEXT);
CREATE TABLE IF NOT EXISTS immunsystem (
  id INTEGER PRIMARY KEY, werk_id INTEGER, lauf_id INTEGER, bereich TEXT,
  name TEXT UNIQUE, code TEXT, ursprung TEXT, status TEXT, erstellt_am TEXT,
  generation INTEGER);
CREATE TABLE IF NOT EXISTS benutzer (
  name TEXT PRIMARY KEY, salz TEXT, hash TEXT, erstellt_am TEXT);
CREATE TABLE IF NOT EXISTS tokens (
  token_hash TEXT PRIMARY KEY, benutzer TEXT, erstellt_am TEXT);
CREATE TABLE IF NOT EXISTS lazarus (
  id INTEGER PRIMARY KEY, lauf_id INTEGER, generation INTEGER, tag TEXT,
  archiv TEXT, pruefsumme TEXT, masse TEXT, erstellt_am TEXT,
  UNIQUE(lauf_id, generation));
"""


def verbinden(pfad: Path | None = None) -> sqlite3.Connection:
    p = pfad or DB_PFAD
    p.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(p), isolation_level=None, timeout=30)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA foreign_keys=ON")
    con.executescript(SCHEMA)
    # Spalten, die nach Phase 1 hinzukamen (SQLite: ADD COLUMN ist idempotent über try)
    for spalte in ("vertraege TEXT",):
        try:
            con.execute(f"ALTER TABLE kandidaten ADD COLUMN {spalte}")
        except sqlite3.OperationalError:
            pass
    return con


@contextmanager
def transaktion(con: sqlite3.Connection):
    con.execute("BEGIN IMMEDIATE")
    try:
        yield con
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise


def j(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True)


def lj(text: str | None):
    return json.loads(text) if text else None
