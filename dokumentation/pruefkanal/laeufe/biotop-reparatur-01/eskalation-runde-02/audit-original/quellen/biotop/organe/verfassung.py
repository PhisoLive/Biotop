"""Organ 3.3: Verfassung des Werks — Sätze, Tauschregeln, Einstiege für
Befundklassen-Immuntests, Betriebszweck (für die Vollmacht nach Abschnitt 4).

Phase 1 Nachlauf: Die Verfassung wird eingelegt (Text + maschinenlesbarer Teil),
nicht vom Biotop entworfen (Entwurf durch Modell = Phase 2/3). Der Ankläger prüft
die mechanisch prüfbaren Sätze (Anhang A Satz 6: keine Tests entfernen/abschwächen,
kein `# nosec`/Prüfwerkzeug-Konfiguration).
"""

from __future__ import annotations

import json
import sqlite3

from ..kern import protokoll
from ..kern.datenbank import lj, transaktion

SCHEMA = """
CREATE TABLE IF NOT EXISTS verfassung_werk (
  werk_id INTEGER PRIMARY KEY, text TEXT, regeln TEXT, quelle TEXT, eingelegt_am TEXT, eingelegt_von TEXT);
"""


def einlegen(con: sqlite3.Connection, werk_id: int, text: str, regeln: dict, quelle: str, von: str) -> None:
    """regeln: {"uebungswerk": bool, "tausch": {...}, "einstiege": {"B307": {...}}, "verbotene_muster": [...]}"""
    con.executescript(SCHEMA)
    with transaktion(con):
        con.execute("INSERT OR REPLACE INTO verfassung_werk(werk_id, text, regeln, quelle, eingelegt_am, eingelegt_von) VALUES (?,?,?,?,?,?)",
                    (werk_id, text, json.dumps(regeln, ensure_ascii=False), quelle, protokoll.jetzt(), von))
    protokoll.schreiben(con, "verfassung.eingelegt", werk_id=werk_id, quelle=quelle, von=von, saetze=text.count("\n") + 1,
                        uebungswerk=regeln.get("uebungswerk", False), tausch=regeln.get("tausch"))


def lesen(con: sqlite3.Connection, werk_id: int) -> dict | None:
    con.executescript(SCHEMA)
    z = con.execute("SELECT * FROM verfassung_werk WHERE werk_id=?", (werk_id,)).fetchone()
    if not z:
        return None
    d = dict(z)
    d["regeln"] = lj(d["regeln"]) or {}
    return d


VERBOTENE_MUSTER_VORGABE = ["# nosec", "#nosec", "noqa: S", ".bandit", "bandit.yaml", "bandit.yml", "[bandit]", "skips", "exclude_dirs"]


def mechanisch_pruefen(verf: dict | None, diff: str, dateien: dict[str, str | None], paket: str, bereich: str) -> list[str]:
    """Mechanisch prüfbare Verfassungssätze. Rückgabe: Liste der Verstöße (leer = keiner)."""
    verstoesse = []
    regeln = (verf or {}).get("regeln", {})
    muster = regeln.get("verbotene_muster", VERBOTENE_MUSTER_VORGABE)
    for pfad, inhalt in dateien.items():
        if pfad.startswith("tests/test_") and not pfad.startswith(f"tests/test_{bereich}_"):
            verstoesse.append(f"verändert vorhandene Testdatei {pfad} (Anhang A Satz 6: keine Tests entfernen oder abschwächen)")
        if inhalt is None and pfad.startswith("tests/"):
            verstoesse.append(f"löscht Testdatei {pfad}")
        if pfad.split("/")[-1] in (".bandit", "bandit.yaml", "bandit.yml", "pyproject.toml", "setup.cfg", "tox.ini") and not pfad.startswith(f"{paket}/{bereich}/"):
            verstoesse.append(f"ändert Prüfwerkzeug-Konfiguration {pfad}")
    for zeile in diff.splitlines():
        if zeile.startswith("+") and not zeile.startswith("+++"):
            for m in muster:
                if m in zeile:
                    verstoesse.append(f"fügt verbotenes Muster „{m}“ ein: {zeile[:80]}")
                    break
    if regeln.get("kein_eval_exec") and bereich in regeln.get("kein_eval_exec_bereiche", [bereich]):
        pass  # wird über den statischen Befund (B307/B102) und die Befundklassen-Immuntests gemessen, nicht per Text
    return sorted(set(verstoesse))
