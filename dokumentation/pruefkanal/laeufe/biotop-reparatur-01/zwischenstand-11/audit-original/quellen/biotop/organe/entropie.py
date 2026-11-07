"""Organ 3.11 — Entropie: Sättigungsmeldung.

Je Generation zwei Zahlen: (1) Verbesserung des Kernmaßes gegenüber der Vorgeneration in Prozent des möglichen Abstands
zum Höchstwert 0 (Kernmaß F2 ist ≤ 0; „Verbesserung %" = (k_neu − k_alt) / |k_alt| · 100, bei k_alt = 0 und k_neu = 0: 0 %);
(2) Verschiedenheit der Schwarmvorschläge: Anteil der Kandidaten einer Generation, die sich in weniger als 10 % der
geänderten Zeilen von einem anderen Kandidaten derselben Generation unterscheiden (Doppelgänger-Anteil).
Regel: Bringen fünf aufeinanderfolgende Generationen zusammen < 0,5 % Verbesserung des Kernmaßes, meldet das Biotop die
Sättigung mit Bezugsgröße und beendet den Lauf (Status 'gesaettigt'); Weg zurück zum Mentor wird genannt. Nie „perfekt".
Am Höchstwert 0 ist jede Generation 0 % — die Meldung erscheint dann spätestens nach der fünften Generation.
"""

from __future__ import annotations

import re
import sqlite3

from ..kern import messgeraet, protokoll
from ..kern.datenbank import j, lj, transaktion

FENSTER = 5
SCHWELLE_PROZENT = 0.5
AEHNLICH_ANTEIL = 0.10


def _plus_minus(diff: str) -> set[str]:
    return {l for l in (diff or "").splitlines() if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))}


def verschiedenheit(con, lauf_id: int, nummer: int) -> dict:
    """Anteil der Kandidaten der Generation, die einem anderen Kandidaten derselben Generation in ≥ 90 % der geänderten Zeilen gleichen."""
    ks = [dict(z) for z in con.execute("SELECT id, bereich, diff FROM kandidaten WHERE lauf_id=? AND generation=? AND diff!='' AND nische!='probe'", (lauf_id, nummer))]
    zeilen = {k["id"]: _plus_minus(k["diff"]) for k in ks}
    doppel = set()
    for i, a in enumerate(ks):
        for b in ks[i + 1:]:
            if a["bereich"] != b["bereich"]:
                continue
            za, zb = zeilen[a["id"]], zeilen[b["id"]]
            if not za or not zb:
                continue
            unterschied = len(za ^ zb) / max(len(za | zb), 1)
            if unterschied < AEHNLICH_ANTEIL:
                doppel |= {a["id"], b["id"]}
    return {"kandidaten_mit_diff": len(ks), "doppelgaenger": len(doppel), "anteil": round(len(doppel) / len(ks), 3) if ks else 0.0}


def verbesserung_prozent(k_alt: int, k_neu: int) -> float:
    if k_alt == 0:
        return 0.0 if k_neu <= 0 else 0.0
    return round((k_neu - k_alt) / abs(k_alt) * 100.0, 3)


def messen(con, lauf_id: int, nummer: int) -> dict:
    """Entropie-Zahlen der Generation `nummer` (nach ihrem Abschluss) — protokolliert und in generationen.entropie abgelegt."""
    g = con.execute("SELECT status, masse FROM generationen WHERE lauf_id=? AND nummer=?", (lauf_id, nummer)).fetchone()
    vor = con.execute("SELECT nummer, masse FROM generationen WHERE lauf_id=? AND nummer<? AND status='angenommen' ORDER BY nummer DESC LIMIT 1", (lauf_id, nummer)).fetchone()
    k_alt = messgeraet.kernmass_f2(lj(vor["masse"])) if vor else None
    if g["status"] in ("angenommen", "vorgelegt") and g["masse"]:
        k_neu = messgeraet.kernmass_f2(lj(g["masse"]))
    else:
        k_neu = k_alt  # abgelehnt: Kernmaß bleibt beim Stand der Vorgeneration
    prozent = verbesserung_prozent(k_alt, k_neu) if k_alt is not None and k_neu is not None else 0.0
    v = verschiedenheit(con, lauf_id, nummer)
    e = {"generation": nummer, "status": g["status"], "kernmass_vor": k_alt, "kernmass_nach": k_neu, "verbesserung_prozent": prozent, "verschiedenheit": v}
    con.execute("CREATE TABLE IF NOT EXISTS entropie (lauf_id INTEGER, generation INTEGER, inhalt TEXT, PRIMARY KEY (lauf_id, generation))")
    with transaktion(con):
        con.execute("INSERT OR REPLACE INTO entropie(lauf_id, generation, inhalt) VALUES (?,?,?)", (lauf_id, nummer, j(e)))
    protokoll.schreiben(con, "entropie.generation", lauf_id=lauf_id, **e)
    return e


def verlauf(con, lauf_id: int) -> list[dict]:
    con.execute("CREATE TABLE IF NOT EXISTS entropie (lauf_id INTEGER, generation INTEGER, inhalt TEXT, PRIMARY KEY (lauf_id, generation))")
    return [lj(z["inhalt"]) for z in con.execute("SELECT inhalt FROM entropie WHERE lauf_id=? ORDER BY generation", (lauf_id,))]


def saettigung(con, lauf_id: int) -> dict | None:
    """Prüft das Fenster der letzten FENSTER Generationen (≥ 1). Rückgabe: Meldung oder None."""
    vl = [e for e in verlauf(con, lauf_id) if e["generation"] >= 1]
    if len(vl) < FENSTER:
        return None
    fenster = vl[-FENSTER:]
    summe = sum(e["verbesserung_prozent"] for e in fenster)
    if summe >= SCHWELLE_PROZENT:
        return None
    x, y = fenster[0]["generation"], fenster[-1]["generation"]
    vers = round(sum(e["verschiedenheit"]["anteil"] for e in fenster) / FENSTER, 3)
    k = fenster[-1]["kernmass_nach"]
    meldung = (f"In dieser Richtung gesättigt: Generationen {x}–{y}, Verbesserung {summe:.2f} % (Schwelle {SCHWELLE_PROZENT} % über {FENSTER} Generationen), "
               f"Kernmaß {k}{' = Höchstwert' if k == 0 else ''}, Doppelgänger-Anteil der Vorschläge im Fenster {vers * 100:.0f} %. "
               f"Weiter nur mit anderer Richtung (zurück zum Mentor: `biotop mentor <lauf>`) oder anderem Maß (neuer Lauf).")
    return {"generationen": [x, y], "verbesserung_prozent": round(summe, 3), "verschiedenheit_anteil": vers, "kernmass": k, "meldung": meldung}


def pruefen_und_beenden(con, lauf_id: int) -> dict | None:
    """Nach jeder abgeschlossenen Generation: bei Sättigung Lauf beenden (Status 'gesaettigt'), Meldung protokollieren."""
    s = saettigung(con, lauf_id)
    if not s:
        return None
    with transaktion(con):
        con.execute("UPDATE laeufe SET status='gesaettigt', beendet_am=?, grund=? WHERE id=?", (protokoll.jetzt(), s["meldung"], lauf_id))
    protokoll.schreiben(con, "entropie.saettigung", lauf_id=lauf_id, **s)
    return s
