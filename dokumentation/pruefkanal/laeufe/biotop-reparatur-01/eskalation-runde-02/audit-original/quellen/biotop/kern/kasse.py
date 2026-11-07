"""Kern: Kasse — zählt jeden Modellaufruf und führt ihn gegen das Laufbudget.

Regel (3.14, Verfassungssatz 8): VOR jedem Aufruf wird geprüft, ob der Aufruf
das Budget überschreiten würde. Wenn ja: BudgetErschoepft, kein Aufruf.

Preistabelle: Teil des unantastbaren Kerns (Abschnitt 5). Preise in USD je
Million Token laut OpenRouter-Katalog vom 18.09.2026; Umrechnung mit fest
hinterlegtem Kurs. Beides ändert nur Philipp.
"""

from __future__ import annotations

import sqlite3

from . import protokoll
from .datenbank import transaktion

# Fester Wechselkurs für die Kasse (Entscheidung Hermes, 18.09.2026, EZB-Referenz
# gerundet; konservativ leicht zugunsten höherer Euro-Kosten).
USD_JE_EUR = 1.08

# USD je Million Token: (eingabe, ausgabe). Quelle: openrouter.ai/api/v1/models, 18.09.2026.
PREISE_USD_JE_MIO = {
    "openai/gpt-4.1-mini": (0.40, 1.60),
    "google/gemini-2.5-flash": (0.30, 2.50),
    "google/gemini-2.5-flash-lite": (0.10, 0.40),
    "deepseek/deepseek-chat-v3.1": (0.25, 0.95),
    "qwen/qwen3-coder": (0.30, 1.00),
    "mistralai/mistral-small-3.2-24b-instruct": (0.09, 0.25),
    "openai/gpt-4o-mini": (0.15, 0.60),
    "openai/gpt-5-mini": (0.25, 2.00),
    "anthropic/claude-haiku-4.5": (1.00, 5.00),
    # schweres Modell für Sicherheitsangriffe (3.7 F2); tokenabgerechnet über OpenRouter, weil der
    # Anthropic-Träger des Teams unangetastet bleibt (Vorgabe Philipp 18.09.2026). Eigene Zählung: zweck-Präfix "schwer.".
    "anthropic/claude-sonnet-4.5": (3.00, 15.00),
    # Phase 2 (Masterprompt v3, Abschnitt 10): Katalogprüfung 19.09.2026 — neuere Modelle gleicher Hersteller zu gleichem/niedrigerem Preis
    "openai/gpt-5.6-luna": (0.20, 1.20),            # ersetzt gpt-4.1-mini (0.40/1.60)
    "google/gemini-3.5-flash-lite": (0.30, 2.50),   # ersetzt gemini-2.5-flash (0.30/2.50), gleicher Preis
    "google/gemini-3.1-flash-lite": (0.25, 1.50),
    "deepseek/deepseek-v4.1-flash": (0.15, 0.60),   # dritter Hersteller
    "qwen/qwen3.8-flash": (0.15, 0.47),             # vierter Hersteller
    "anthropic/claude-sonnet-5": (2.00, 10.00),     # schweres Modell, ersetzt sonnet-4.5 (3.00/15.00)
}

# Auftragsbudget über mehrere Läufe (Phase-Budget „hart“): Summe aller Läufe ab AUFTRAG_LAUF_AB gegen AUFTRAG_BUDGET_EUR.
import os as _os
AUFTRAG_LAUF_AB = int(_os.environ.get("BIOTOP_AUFTRAG_LAUF_AB", "0") or 0)
AUFTRAG_BUDGET_EUR = float(_os.environ.get("BIOTOP_AUFTRAG_BUDGET_EUR", "0") or 0)


def auftrag_stand(con: sqlite3.Connection) -> float:
    if not AUFTRAG_LAUF_AB:
        return 0.0
    return con.execute("SELECT COALESCE(SUM(kosten_eur),0) FROM kasse WHERE lauf_id>=?", (AUFTRAG_LAUF_AB,)).fetchone()[0]


class BudgetErschoepft(RuntimeError):
    """Der nächste Aufruf würde das Laufbudget überschreiten."""


def kosten_eur(modell: str, tokens_ein: int, tokens_aus: int) -> float:
    if modell not in PREISE_USD_JE_MIO:
        raise KeyError(f"kein Preis hinterlegt für {modell}")
    p_ein, p_aus = PREISE_USD_JE_MIO[modell]
    usd = tokens_ein / 1e6 * p_ein + tokens_aus / 1e6 * p_aus
    return usd / USD_JE_EUR


def stand(con: sqlite3.Connection, lauf_id: int) -> dict:
    z = con.execute(
        "SELECT COALESCE(SUM(kosten_eur),0) k, COUNT(*) n, COALESCE(SUM(tokens_ein),0) e, "
        "COALESCE(SUM(tokens_aus),0) a, COALESCE(SUM(kontingent),0) q FROM kasse WHERE lauf_id=?",
        (lauf_id,),
    ).fetchone()
    lauf = con.execute("SELECT budget_eur FROM laeufe WHERE id=?", (lauf_id,)).fetchone()
    return {
        "ausgegeben_eur": round(z["k"], 6),
        "budget_eur": lauf["budget_eur"] if lauf else None,
        "auftrag_ausgegeben_eur": round(auftrag_stand(con), 6) if AUFTRAG_LAUF_AB else None,
        "auftrag_budget_eur": AUFTRAG_BUDGET_EUR or None,
        "aufrufe": z["n"],
        "tokens_ein": z["e"],
        "tokens_aus": z["a"],
        "kontingent_aufrufe": z["q"],
    }


def vorpruefung(
    con: sqlite3.Connection, lauf_id: int, modell: str, tokens_ein_geschaetzt: int,
    max_tokens_aus: int, zweck: str,
) -> float:
    """Wirft BudgetErschoepft, wenn bisher + Schätzung > Budget. Rückgabe: Schätzung in €."""
    s = stand(con, lauf_id)
    schaetzung = kosten_eur(modell, tokens_ein_geschaetzt, max_tokens_aus)
    if AUFTRAG_BUDGET_EUR and AUFTRAG_LAUF_AB and lauf_id >= AUFTRAG_LAUF_AB:
        a = auftrag_stand(con)
        if a + schaetzung > AUFTRAG_BUDGET_EUR:
            nr = protokoll.schreiben(con, "kasse.abbruch", lauf_id=lauf_id, modell=modell, zweck=zweck, auftrag_ausgegeben_eur=round(a, 6),
                                     schaetzung_eur=round(schaetzung, 6), auftrag_budget_eur=AUFTRAG_BUDGET_EUR,
                                     meldung="AUFTRAGSBUDGET erschöpft — Aufruf NICHT ausgeführt")
            with transaktion(con):
                con.execute("UPDATE laeufe SET status='abgebrochen', grund=? WHERE id=?", (f"Auftragsbudget erschöpft vor Aufruf (Protokoll #{nr})", lauf_id))
            raise BudgetErschoepft(f"Auftragsbudget {AUFTRAG_BUDGET_EUR:.2f} € erschöpft: {a:.4f} € + {schaetzung:.4f} €. Protokoll #{nr}.")
    if s["budget_eur"] is not None and s["ausgegeben_eur"] + schaetzung > s["budget_eur"]:
        nr = protokoll.schreiben(
            con, "kasse.abbruch", lauf_id=lauf_id, modell=modell, zweck=zweck,
            ausgegeben_eur=s["ausgegeben_eur"], schaetzung_eur=round(schaetzung, 6),
            budget_eur=s["budget_eur"], aufrufe_bisher=s["aufrufe"],
            meldung="Budget erschöpft — Aufruf NICHT ausgeführt",
        )
        with transaktion(con):
            con.execute(
                "UPDATE laeufe SET status='abgebrochen', grund=? WHERE id=?",
                (f"Budget erschöpft vor Aufruf (Protokoll #{nr})", lauf_id),
            )
        raise BudgetErschoepft(
            f"Budget {s['budget_eur']:.2f} € erschöpft: ausgegeben {s['ausgegeben_eur']:.4f} € "
            f"+ Schätzung {schaetzung:.4f} € für {modell} ({zweck}). Aufruf nicht ausgeführt. "
            f"Protokoll #{nr}."
        )
    return schaetzung


def buchen(
    con: sqlite3.Connection, lauf_id: int, anbieter: str, modell: str,
    tokens_ein: int, tokens_aus: int, zweck: str, protokoll_nr: int, kontingent: bool = False,
) -> float:
    k = 0.0 if kontingent else kosten_eur(modell, tokens_ein, tokens_aus)
    with transaktion(con):
        con.execute(
            "INSERT INTO kasse(lauf_id, zeit, anbieter, modell, tokens_ein, tokens_aus, "
            "kosten_eur, zweck, kontingent, protokoll_nr) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (lauf_id, protokoll.jetzt(), anbieter, modell, tokens_ein, tokens_aus, k,
             zweck, 1 if kontingent else 0, protokoll_nr),
        )
    return k


def bericht_md(con: sqlite3.Connection, lauf_id: int | None = None) -> str:
    q = "SELECT * FROM kasse"
    p: tuple = ()
    if lauf_id is not None:
        q += " WHERE lauf_id=?"
        p = (lauf_id,)
    zeilen = ["| Nr | Lauf | Zeit | Anbieter | Modell | Ein | Aus | € | Zweck | Protokoll |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    summe = 0.0
    n = 0
    for z in con.execute(q + " ORDER BY id", p):
        n += 1
        summe += z["kosten_eur"]
        zeilen.append(
            f"| {z['id']} | {z['lauf_id']} | {z['zeit']} | {z['anbieter']} | {z['modell']} | "
            f"{z['tokens_ein']} | {z['tokens_aus']} | {z['kosten_eur']:.5f} | {z['zweck']} | #{z['protokoll_nr']} |"
        )
    zeilen.append(f"\n**Summe: {n} Aufrufe, {summe:.4f} €** (Kurs {USD_JE_EUR} USD/EUR, Kontingent-Aufrufe: "
                  f"{con.execute('SELECT COALESCE(SUM(kontingent),0) FROM kasse').fetchone()[0]})")
    return "\n".join(zeilen)


def generationskosten(con: sqlite3.Connection, lauf_id: int) -> dict[int, float]:
    """Kosten je abgeschlossener Generation, aus dem Protokoll (Buchungen zwischen begonnen und ergebnis)."""
    out: dict[int, float] = {}
    beg = {}
    for z in con.execute("SELECT nr, art, inhalt FROM protokoll WHERE art IN ('generation.begonnen','generation.ergebnis') AND inhalt LIKE ? ORDER BY nr",
                         (f'%"lauf_id": {lauf_id},%',)):
        import json
        d = json.loads(z["inhalt"])
        if d.get("lauf_id") != lauf_id:
            continue
        if z["art"] == "generation.begonnen":
            beg[d["nummer"]] = z["nr"]
        elif d["nummer"] in beg:
            k = con.execute("SELECT COALESCE(SUM(kosten_eur),0) FROM kasse WHERE lauf_id=? AND protokoll_nr BETWEEN ? AND ?",
                            (lauf_id, beg[d["nummer"]], z["nr"])).fetchone()[0]
            out[d["nummer"]] = k
    return out


def generation_vorpruefung(con: sqlite3.Connection, lauf_id: int, nummer: int) -> float:
    """Vor dem ersten Aufruf einer Generation: bisher + Kostenvoranschlag (teuerste bisherige Generation) > Budget → Abbruch."""
    s = stand(con, lauf_id)
    gk = generationskosten(con, lauf_id)
    voranschlag = max(gk.values()) if gk else 0.0
    if s["budget_eur"] is not None and voranschlag > 0 and s["ausgegeben_eur"] + voranschlag > s["budget_eur"]:
        nr = protokoll.schreiben(
            con, "kasse.abbruch", lauf_id=lauf_id, generation=nummer, zweck="generation.vorpruefung",
            ausgegeben_eur=s["ausgegeben_eur"], voranschlag_eur=round(voranschlag, 6), budget_eur=s["budget_eur"],
            aufrufe_bisher=s["aufrufe"], grundlage={str(k): round(v, 6) for k, v in gk.items()},
            meldung=f"Budget reicht nicht für Generation {nummer} — kein Modellaufruf ausgeführt",
        )
        with transaktion(con):
            con.execute("UPDATE laeufe SET status='abgebrochen', grund=?, beendet_am=? WHERE id=?",
                        (f"Budget erschöpft vor Generation {nummer} (Protokoll #{nr})", protokoll.jetzt(), lauf_id))
        raise BudgetErschoepft(
            f"Budget {s['budget_eur']:.2f} € reicht nicht für Generation {nummer}: ausgegeben {s['ausgegeben_eur']:.4f} € "
            f"+ Voranschlag {voranschlag:.4f} € (teuerste bisherige Generation). Kein Modellaufruf ausgeführt. Protokoll #{nr}."
        )
    return voranschlag
