"""Organ 3.6 (Phase 2): Nischen, Bandit-Gewichtung, Eliten (MAP-Elites).

Nischen: sicher, schnell, elegant, wild — je mindestens zwei Hersteller.
Bandit: je (Lauf, Nische, Hersteller) werden Versuche und Erfolge (= Kandidat
überlebt den Ankläger) geführt; die Wahl der zwei Hersteller je Nische und
Generation erfolgt per Thompson-Stichprobe aus Beta(erfolge+1, misserfolge+1),
Hersteller paarweise verschieden. Gewichte = Erwartungswert der Beta-Verteilung.
Eliten: je (Nische, Bereich) bleibt der beste überlebende Kandidat am Leben und
wird dem Schwarm der Nische in der nächsten Generation als Ausgangspunkt gezeigt.

Modelle (Katalogprüfung 19.09.2026, ausgaben/00-openrouter-katalog-schnellmodelle.txt):
  openai/gpt-5.6-luna 0.20/1.20 · google/gemini-3.5-flash-lite 0.30/2.50 ·
  deepseek/deepseek-v4.1-flash 0.15/0.60 · qwen/qwen3.8-flash 0.15/0.47  (USD/Mio)
"""

from __future__ import annotations

import random
import sqlite3

from ..kern import protokoll
from ..kern.datenbank import j, transaktion

HERSTELLER_MODELLE = {
    "openai": "openai/gpt-5.6-luna",
    "google": "google/gemini-3.5-flash-lite",
    "deepseek": "deepseek/deepseek-v4.1-flash",
    "qwen": "qwen/qwen3.8-flash",
}

NISCHEN = {
    "sicher": {
        "temperatur": 0.2, "ziel": "kernmass",
        "auftrag": "Du bist „Der Sichere“: Beseitige Fehler, Vertragsverletzungen und Sicherheitsbefunde; härte Verträge; wage nichts Neues; "
                   "verändere keine öffentliche Signatur. Ein Vorschlag zählt nur, wenn er einen bestätigten Fehler behebt (mit Test, der an der "
                   "Vorgeneration fällt und einen Vertrag oder Verfassungssatz nennt) oder einen statischen Befund/tote Funktion entfernt.",
    },
    "schnell": {
        "temperatur": 0.3, "ziel": "laufzeit",
        "auftrag": "Du bist „Der Schnelle“: Senke die Laufzeit auf der Referenzlast (Quelltext der Referenzlast wird mitgegeben) — Algorithmus, "
                   "Datenstruktur, Zwischenspeicher, unnötige Kopien. Verhalten und Verträge bleiben exakt gleich; alle Tests müssen bestehen. "
                   "Dein Vorschlag wird angenommen, wenn die Laufzeit des Bereichs um mindestens 15 % sinkt und das Kernmaß gleich bleibt oder steigt. "
                   "Suche zuerst nach O(n²)-Mustern: Summen über ganze Listen bei jedem Lesen, wiederholtes Parsen derselben Eingabe, Sortieren in Schleifen.",
    },
    "elegant": {
        "temperatur": 0.4, "ziel": "kernmass",
        "auftrag": "Du bist „Der Elegante“: weniger Code bei gleicher Funktion, klarere Struktur, tote Zweige entfernen, Doppelungen zusammenführen. "
                   "Verträge bleiben exakt gleich. Gemessen wird nur hart: Ein Vorschlag zählt, wenn er tote Funktionen entfernt oder einen "
                   "Fehler behebt; reine Umformung ohne Maßgewinn wird abgelehnt — dann antworte lieber KEIN VORSCHLAG.",
    },
    "wild": {
        "temperatur": 0.9, "ziel": "kernmass",
        "auftrag": "Du bist „Der Wilde“: Schlage vor, was niemand erwartet — eine andere Datenstruktur, ein anderer Algorithmus, eine Grenze, die "
                   "in Frage gestellt gehört. Du darfst Verträge in Frage stellen (dann nenne sie unter VERTRÄGE; der Nachbar wird gefragt). "
                   "Gemessen wird trotzdem hart: kein Test darf fallen, Grenzmaße gelten, das Kernmaß darf nicht sinken.",
    },
}


def _tabelle(con: sqlite3.Connection) -> None:
    con.executescript("""
    CREATE TABLE IF NOT EXISTS bandit (lauf_id INTEGER, nische TEXT, hersteller TEXT, versuche INTEGER DEFAULT 0, erfolge INTEGER DEFAULT 0,
        PRIMARY KEY (lauf_id, nische, hersteller));
    CREATE TABLE IF NOT EXISTS eliten (lauf_id INTEGER, nische TEXT, bereich TEXT, kandidat_id INTEGER, generation INTEGER, zuwachs INTEGER,
        laufzeit_gewinn REAL, diff TEXT, begruendung TEXT, PRIMARY KEY (lauf_id, nische, bereich));
    """)


def waehlen(con: sqlite3.Connection, lauf_id: int, nische: str, anzahl: int = 2, rng: random.Random | None = None) -> list[tuple[str, str]]:
    """Wählt `anzahl` Hersteller (paarweise verschieden) per Thompson-Stichprobe. Rückgabe [(hersteller, modell)]."""
    _tabelle(con)
    rng = rng or random.Random()
    proben = []
    for h in HERSTELLER_MODELLE:
        z = con.execute("SELECT versuche, erfolge FROM bandit WHERE lauf_id=? AND nische=? AND hersteller=?", (lauf_id, nische, h)).fetchone()
        v, e = (z["versuche"], z["erfolge"]) if z else (0, 0)
        proben.append((rng.betavariate(e + 1, v - e + 1), h))
    proben.sort(reverse=True)
    gewaehlt = [(h, HERSTELLER_MODELLE[h]) for _, h in proben[:anzahl]]
    protokoll.schreiben(con, "bandit.wahl", lauf_id=lauf_id, nische=nische, proben={h: round(p, 3) for p, h in proben}, gewaehlt=[h for h, _ in gewaehlt])
    return gewaehlt


def buchen(con: sqlite3.Connection, lauf_id: int, nische: str, hersteller: str, erfolg: bool) -> None:
    _tabelle(con)
    with transaktion(con):
        con.execute("INSERT INTO bandit(lauf_id, nische, hersteller, versuche, erfolge) VALUES (?,?,?,1,?) "
                    "ON CONFLICT(lauf_id, nische, hersteller) DO UPDATE SET versuche=versuche+1, erfolge=erfolge+excluded.erfolge",
                    (lauf_id, nische, hersteller, 1 if erfolg else 0))


def gewichte(con: sqlite3.Connection, lauf_id: int) -> dict:
    _tabelle(con)
    out: dict = {}
    for z in con.execute("SELECT nische, hersteller, versuche, erfolge FROM bandit WHERE lauf_id=? ORDER BY nische, hersteller", (lauf_id,)):
        out.setdefault(z["nische"], {})[z["hersteller"]] = {"versuche": z["versuche"], "erfolge": z["erfolge"],
                                                             "gewicht": round((z["erfolge"] + 1) / (z["versuche"] + 2), 3)}
    return out


def elite_setzen(con: sqlite3.Connection, lauf_id: int, nische: str, bereich: str, kandidat_id: int, generation: int,
                 zuwachs: int, laufzeit_gewinn: float, diff: str, begruendung: str) -> bool:
    """Ersetzt die Elite der Nische im Bereich, wenn der Kandidat besser ist (Zuwachs, dann Laufzeitgewinn)."""
    _tabelle(con)
    z = con.execute("SELECT zuwachs, laufzeit_gewinn FROM eliten WHERE lauf_id=? AND nische=? AND bereich=?", (lauf_id, nische, bereich)).fetchone()
    if z and (z["zuwachs"], z["laufzeit_gewinn"]) >= (zuwachs, laufzeit_gewinn):
        return False
    with transaktion(con):
        con.execute("INSERT OR REPLACE INTO eliten(lauf_id, nische, bereich, kandidat_id, generation, zuwachs, laufzeit_gewinn, diff, begruendung) VALUES (?,?,?,?,?,?,?,?,?)",
                    (lauf_id, nische, bereich, kandidat_id, generation, zuwachs, laufzeit_gewinn, diff, begruendung))
    return True


def elite(con: sqlite3.Connection, lauf_id: int, nische: str, bereich: str) -> dict | None:
    _tabelle(con)
    z = con.execute("SELECT * FROM eliten WHERE lauf_id=? AND nische=? AND bereich=?", (lauf_id, nische, bereich)).fetchone()
    return dict(z) if z else None


def eliten_liste(con: sqlite3.Connection, lauf_id: int) -> list[dict]:
    _tabelle(con)
    return [dict(z) for z in con.execute("SELECT nische, bereich, kandidat_id, generation, zuwachs, laufzeit_gewinn FROM eliten WHERE lauf_id=? ORDER BY nische, bereich", (lauf_id,))]
