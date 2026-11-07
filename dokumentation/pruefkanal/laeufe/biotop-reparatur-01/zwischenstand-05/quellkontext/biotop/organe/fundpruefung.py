"""Organ „Fund-Neubewertung" (Fassung 5, 3.10) — offene Funde beim Übergang in einen neuen Lauf mechanisch
neu bewerten, statt ihren alten Status zu übernehmen.

Regel: Ein Fund-Test, der am NEUEN AUSGANG besteht (also das dortige Verhalten festschreibt) und dabei weder eine
Ausnahme im Werk auslöst noch einen Vertrag oder Verfassungssatz durch explizite Kennung nennt, ist **Norm**, kein
Fund. Er darf nicht in den gemessenen Testbestand, sonst tötet er jede spätere Behebung per Pareto je Test.

Grund (gemessen in Phase 3, Lauf 19): Beim Übertragen der Funde aus einem verworfenen Lauf hatte Hermes die alten
Stati blind übernommen. Sechs Ankläger-Tests, die denselben Fehler als Norm festschrieben, standen dadurch als
Funde im Testbestand und töteten jede Behebung — bis sie einzeln in der Kammer nachgemessen wurden.

Das Organ benutzt die **Ankläger-Logik selbst** (`aegis._nennt_vertrag`), nicht einen eigenen Verweis-Regex:
Zwei Wahrheitsbegriffe für dieselbe Frage sind genau die Fehlerklasse, die diese Regel behebt.
"""
from __future__ import annotations

import ast
import sqlite3
from pathlib import Path

from ..kern import protokoll
from ..kern.datenbank import transaktion
from . import aegis, kammer, verfassung


def _testnamen(code: str) -> list[str]:
    try:
        baum = ast.parse(code)
    except SyntaxError:
        return []
    return [k.name for k in baum.body if isinstance(k, ast.FunctionDef) and k.name.startswith("test_")]


def _ausfuehren(pfad: Path, name: str, code: str) -> tuple[bool, bool, str]:
    """(besteht, absturz_im_werk, Ausgabe) — ein Kammerlauf je Fund."""
    datei = f"tests/test_neubewertung_{name}.py"
    e = kammer.ausfuehren(pfad, ["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", datei],
                          dateien={datei: code}, zeitlimit_s=90)
    aus = (e.stdout or "") + (e.stderr or "")
    besteht = " passed" in aus and " failed" not in aus and " error" not in aus.lower()
    # Absturz im Werk = eine Ausnahme, die NICHT aus einer Zusicherung des Tests stammt.
    absturz = (not besteht) and ("Error" in aus or "Exception" in aus) and "AssertionError" not in aus
    return besteht, absturz, aus[-400:]


def bewerten(con: sqlite3.Connection, werk_id: int, lauf_id: int, pfad: Path, bereiche: list[str] | None = None,
             schreiben: bool = True) -> dict:
    """Alle offenen Funde des Werks am aktuellen Ausgang nachmessen und neu einstufen."""
    verf = verfassung.lesen(con, werk_id)
    funde = [dict(z) for z in con.execute(
        "SELECT id, name, bereich, code, status FROM immunsystem WHERE werk_id=? AND status IN ('offen','offen_norm')"
        " ORDER BY name", (werk_id,))]
    ergebnisse, kammerlaeufe = [], 0
    for f in funde:
        namen = _testnamen(f["code"])
        besteht, absturz, ausgabe = _ausfuehren(pfad, f["name"], f["code"])
        kammerlaeufe += 1
        # Verweis mit der Ankläger-Logik prüfen — nicht mit einem zweiten Regex.
        bezug = any(aegis._nennt_vertrag(f["code"], t, verf, con, werk_id, f["bereich"], None) for t in namen)
        # Einstufung (F5 3.10 in Verbindung mit 3.7). Grundsatz (Fassung 6, Chat-Claude):
        #   **Ein fallender Test beweist eine Abweichung, nie ihre Richtung — welche Seite recht hat,
        #   entscheidet nur ein Absturz oder ein Vertrag.**
        #   besteht am Ausgang, kein Absturz, kein Verweis  → Norm (schreibt das jetzige Verhalten fest)
        #   fällt am Ausgang MIT Absturz oder MIT Verweis    → Fund (beweist einen echten Fehler)
        #   fällt am Ausgang OHNE beides                     → bleibt, was es war: Fallen allein macht keinen Fund,
        #       sonst würde jeder Normtest, den eine spätere Generation ins Fallen bringt, stillschweigend zum Fund
        #       und könnte per Pareto je Test Behebungen töten (gemessen: 9 von 20 Normtests am Werk 18).
        #       Das ist Lauf 16 von der anderen Seite: dort machte Fallen am KANDIDATEN aus einem Normtest einen Fund.
        if besteht and not absturz and not bezug:
            neu = "offen_norm"
        elif not besteht and (absturz or bezug):
            neu = "offen"
        else:
            neu = "offen_norm" if f["status"] == "offen_norm" else "offen"
        ergebnisse.append({"id": f["id"], "name": f["name"], "bereich": f["bereich"], "alt": f["status"], "neu": neu,
                           "besteht_am_ausgang": besteht, "absturz_im_werk": absturz, "vertragsverweis": bezug,
                           "geaendert": neu != f["status"], "testnamen": namen})
    geaendert = [e for e in ergebnisse if e["geaendert"]]
    if schreiben and geaendert:
        with transaktion(con):
            for e in geaendert:
                con.execute("UPDATE immunsystem SET status=?, ursprung=ursprung || ? WHERE id=?",
                            (e["neu"], f" | neubewertet in Lauf {lauf_id} (F5 3.10): besteht am Ausgang="
                                       f"{e['besteht_am_ausgang']}, Absturz={e['absturz_im_werk']}, "
                                       f"Vertragsverweis={e['vertragsverweis']} → {e['neu']}", e["id"]))
    protokoll.schreiben(con, "immun.neubewertet", lauf_id=lauf_id, werk_id=werk_id, geprueft=len(ergebnisse),
                        geaendert=len(geaendert), kammerlaeufe=kammerlaeufe,
                        aenderungen=[f"{e['name']}: {e['alt']} → {e['neu']}" for e in geaendert],
                        regel="F5 3.10: Offene Funde werden beim Übergang in einen neuen Lauf mechanisch neu bewertet "
                              "(am neuen Ausgang ausgeführt), nicht mit ihrem alten Status übernommen.")
    return {"geprueft": len(ergebnisse), "geaendert": len(geaendert), "kammerlaeufe": kammerlaeufe,
            "ergebnisse": ergebnisse,
            "bezugsgroesse": f"{len(geaendert)} von {len(ergebnisse)} offenen Funden neu eingestuft"}


def uebernehmen(con: sqlite3.Connection, von_werk_id: int, nach_werk_id: int, lauf_id: int, pfad: Path) -> dict:
    """Funde eines Werks in ein neues Werk desselben Ausgangs übernehmen UND dabei neu bewerten.

    Das ist der Weg, den Hermes in Phase 3 von Hand ging — und dabei die alten Stati mitnahm. Als Organ wird die
    Neubewertung erzwungen: Übernahme ohne Nachmessung gibt es nicht mehr."""
    alt = [dict(z) for z in con.execute(
        "SELECT bereich, name, code, ursprung, status FROM immunsystem WHERE werk_id=? AND status IN ('offen','offen_norm')",
        (von_werk_id,))]
    n = 0
    for z in alt:
        name = z["name"].split("_w")[0] + f"_w{nach_werk_id}"
        with transaktion(con):
            con.execute("INSERT OR IGNORE INTO immunsystem(werk_id, lauf_id, bereich, name, code, ursprung, status,"
                        " erstellt_am, generation) VALUES (?,?,?,?,?,?,?,?,0)",
                        (nach_werk_id, lauf_id, z["bereich"], name, z["code"],
                         z["ursprung"] + f" | übernommen aus Werk {von_werk_id} (Lauf {lauf_id})", z["status"],
                         protokoll.jetzt()))
        n += 1
    protokoll.schreiben(con, "immun.uebernommen", lauf_id=lauf_id, werk_id=nach_werk_id, aus_werk_id=von_werk_id,
                        anzahl=n, hinweis="Neubewertung folgt unmittelbar (F5 3.10) — kein Status wird blind übernommen")
    b = bewerten(con, nach_werk_id, lauf_id, pfad)
    b["uebernommen"] = n
    return b


def text(e: dict) -> list[str]:
    z = [f"Fund-Neubewertung (F5 3.10): {e['bezugsgroesse']}, {e['kammerlaeufe']} Kammerläufe"]
    for r in e["ergebnisse"]:
        marke = "  ← geändert" if r["geaendert"] else ""
        z.append(f"  {r['name']:<40} {r['alt']:<10} → {r['neu']:<10} "
                 f"(besteht am Ausgang {r['besteht_am_ausgang']}, Absturz {r['absturz_im_werk']}, "
                 f"Vertragsverweis {r['vertragsverweis']}){marke}")
    return z
