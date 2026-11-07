"""Organ 3.5 — Jury für weiche Maße (Lesbarkeit, Eleganz).

Nur zwischen Kandidaten desselben Bereichs, die ALLE harten Maße bestehen und gleiches Kernmaß (und gleichen
Laufzeit-Befund) haben. Mindestens drei Modelle verschiedener Hersteller urteilen unabhängig mit Begründung; nur bei
Einstimmigkeit entscheidet die Jury den Gleichstand; sonst kein Urteil (protokolliert) und die bisherige mechanische
Reihung (kleinster Diff) bleibt. Weiche Maße beweisen nichts; sie brechen Gleichstände.
"""

from __future__ import annotations

import json
import re
import sqlite3

from ..anbieter import AnbieterFehler, aufrufen
from ..kern import protokoll
from ..kern.datenbank import j, lj, transaktion

JUROREN = [("openrouter", "openai/gpt-5.6-luna"), ("openrouter", "google/gemini-3.5-flash-lite"), ("openrouter", "deepseek/deepseek-v4.1-flash")]

SYSTEM = """Du bist Juror in einem Biotop, das Software-Werke hebt. Zwei Kandidaten (Diffs) für denselben Bereich bestehen alle harten Maße gleich gut.
Du beurteilst NUR weiche Maße: Lesbarkeit, Klarheit der Struktur, Eleganz (weniger Sonderfälle, sprechende Namen, keine unnötige Komplexität).
Nicht beurteilen: Korrektheit, Leistung, Sicherheit — das hat die Messung schon entschieden.
Antworte NUR mit JSON: {"wahl": "A" oder "B", "begruendung": "2–3 Sätze"}"""


def _tabelle(con):
    con.executescript("""CREATE TABLE IF NOT EXISTS jury (id INTEGER PRIMARY KEY, lauf_id INTEGER, generation INTEGER, bereich TEXT, kandidat_a INTEGER, kandidat_b INTEGER,
        urteile TEXT, einstimmig INTEGER, gewinner INTEGER, erstellt_am TEXT);""")


def gleichstand(u_a: dict, u_b: dict) -> bool:
    ma, mb = u_a.get("mass") or {}, u_b.get("mass") or {}
    return (u_a.get("status") == u_b.get("status") == "ueberlebt" and ma.get("zuwachs") == mb.get("zuwachs")
            and len(ma.get("laufzeit_gewinne") or []) == len(mb.get("laufzeit_gewinne") or []))


def entscheiden(con: sqlite3.Connection, lauf_id: int, generation: int, bereich: str, kid_a: int, kid_b: int) -> dict:
    _tabelle(con)
    a = con.execute("SELECT diff, begruendung FROM kandidaten WHERE id=?", (kid_a,)).fetchone()
    b = con.execute("SELECT diff, begruendung FROM kandidaten WHERE id=?", (kid_b,)).fetchone()
    nutzer = (f"BEREICH {bereich}\n\nKANDIDAT A (Begründung: {a['begruendung'][:300]}):\n```diff\n{a['diff'][:6000]}\n```\n\n"
              f"KANDIDAT B (Begründung: {b['begruendung'][:300]}):\n```diff\n{b['diff'][:6000]}\n```")
    urteile = []
    for anbieter, modell in JUROREN:
        try:
            r = aufrufen(con, lauf_id, anbieter, modell, SYSTEM, nutzer, zweck=f"jury.{bereich}.gen{generation}", max_tokens=400, temperatur=0.2)
            m = re.search(r"\{.*\}", r.text, re.S)
            d = json.loads(m.group(0)) if m else {}
            wahl = str(d.get("wahl", "")).strip().upper()[:1]
            urteile.append({"modell": modell, "wahl": wahl if wahl in ("A", "B") else None, "begruendung": str(d.get("begruendung", ""))[:400]})
        except (AnbieterFehler, json.JSONDecodeError) as e:
            urteile.append({"modell": modell, "wahl": None, "begruendung": f"Fehler: {str(e)[:120]}"})
    wahlen = [u["wahl"] for u in urteile]
    einstimmig = len(urteile) >= 3 and all(w == wahlen[0] and w is not None for w in wahlen)
    gewinner = (kid_a if wahlen[0] == "A" else kid_b) if einstimmig else None
    with transaktion(con):
        con.execute("INSERT INTO jury(lauf_id, generation, bereich, kandidat_a, kandidat_b, urteile, einstimmig, gewinner, erstellt_am) VALUES (?,?,?,?,?,?,?,?,?)",
                    (lauf_id, generation, bereich, kid_a, kid_b, j(urteile), int(einstimmig), gewinner, protokoll.jetzt()))
    protokoll.schreiben(con, "jury.urteil", lauf_id=lauf_id, generation=generation, bereich=bereich, kandidat_a=kid_a, kandidat_b=kid_b,
                        urteile=urteile, einstimmig=einstimmig, gewinner=gewinner)
    return {"urteile": urteile, "einstimmig": einstimmig, "gewinner": gewinner}
