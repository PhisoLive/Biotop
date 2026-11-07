"""Explizite Verträge (Phase 2, 3.2/3.7 Schritt 2/3.8 Verhandlung).

Ein expliziter Vertrag ist eine ausführbare Zusicherung an einer Grenze zwischen
zwei Bereichen: ein pytest-Test in `tests/vertraege/test_vertrag_<A>_<B>.py`,
der vom Konsumenten A aus die Schnittstelle des Lieferanten B prüft (Signatur,
Rückgabetyp, Randverhalten). Er wird aus den Docstring-Verträgen und den
öffentlichen Signaturen der Landkarte abgeleitet und von Philipp/Chat-Claude
bestätigt (hier: aus Anhang A Satz 3–5 plus Signaturen, eingelegt durch Hermes).

Prüfung (Schritt 2): Die Vertragstests laufen paarweise mit. Fällt ein
Vertragstest am Kandidaten, der an der Vorgeneration bestand, ist das eine
Vertragsverletzung — der Kandidat ist tot, AUSSER er hat den Vertrag unter
VERTRÄGE benannt; dann wird der Nachbar gefragt (Verhandlung, 3.8 Schritt 2):
Der Schwarm des Nachbarn bekommt den Diff und erzeugt seine Anpassung;
Kandidat + Anpassung werden zusammen gemessen. Besteht das Paar (kein
Vertragstest fällt, der zuvor bestand — oder der Vertragstest wird vom Paar
gemeinsam angepasst und die Vertragsdatei ist Teil des Paares), ist die
Vertragsänderung angenommen; sonst nicht.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from ..kern import protokoll
from ..kern.datenbank import transaktion

VERTRAGS_DIR = "tests/vertraege"


def _tabelle(con):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS vertraege_explizit (werk_id INTEGER, von_bereich TEXT, nach_bereich TEXT, pfad TEXT, code TEXT,
        quelle TEXT, eingelegt_am TEXT, PRIMARY KEY (werk_id, von_bereich, nach_bereich));""")


def einlegen(con: sqlite3.Connection, werk_id: int, werk: Path, vertraege: dict[tuple[str, str], str], quelle: str) -> list[str]:
    """vertraege: {(von, nach): pytest-code}. Schreibt die Dateien ins Werk (sie sind Teil des Werks) und merkt sie in der DB."""
    _tabelle(con)
    pfade = []
    (werk / VERTRAGS_DIR).mkdir(parents=True, exist_ok=True)
    (werk / VERTRAGS_DIR / "__init__.py").write_text("")
    with transaktion(con):
        for (a, b), code in vertraege.items():
            pfad = f"{VERTRAGS_DIR}/test_vertrag_{a}_{b}.py"
            (werk / pfad).write_text(code)
            con.execute("INSERT OR REPLACE INTO vertraege_explizit(werk_id, von_bereich, nach_bereich, pfad, code, quelle, eingelegt_am) VALUES (?,?,?,?,?,?,?)",
                        (werk_id, a, b, pfad, code, quelle, protokoll.jetzt()))
            pfade.append(pfad)
    protokoll.schreiben(con, "vertraege.eingelegt", werk_id=werk_id, anzahl=len(pfade), pfade=pfade, quelle=quelle)
    return pfade


def fuer_bereich(con: sqlite3.Connection, werk_id: int, bereich: str) -> list[dict]:
    """Alle expliziten Verträge, an denen `bereich` beteiligt ist (als Lieferant oder Konsument)."""
    _tabelle(con)
    return [dict(z) for z in con.execute("SELECT * FROM vertraege_explizit WHERE werk_id=? AND (von_bereich=? OR nach_bereich=?)", (werk_id, bereich, bereich))]


def alle(con: sqlite3.Connection, werk_id: int) -> list[dict]:
    _tabelle(con)
    return [dict(z) for z in con.execute("SELECT * FROM vertraege_explizit WHERE werk_id=?", (werk_id,))]


def text_fuer_bereich(con, werk_id, bereich) -> str:
    teile = []
    for v in fuer_bereich(con, werk_id, bereich):
        rolle = "Lieferant" if v["nach_bereich"] == bereich else "Konsument"
        teile.append(f"- {v['pfad']} ({v['von_bereich']} → {v['nach_bereich']}; du bist {rolle}):\n```python\n{v['code'][:1800]}\n```")
    return "\n".join(teile)


def nachbar_von(con, werk_id, bereich, pfad) -> str | None:
    """Zu einer Vertragsdatei der andere Bereich."""
    for v in fuer_bereich(con, werk_id, bereich):
        if v["pfad"] == pfad:
            return v["von_bereich"] if v["nach_bereich"] == bereich else v["nach_bereich"]
    return None


def verletzt(fehl_basis: set[str], fehl_kand: set[str]) -> list[str]:
    """Vertragstests (Datei unter tests/vertraege), die an der Vorgeneration bestanden und am Kandidaten fallen."""
    return sorted(f for f in (fehl_kand - fehl_basis) if f.startswith("test_vertrag_"))
