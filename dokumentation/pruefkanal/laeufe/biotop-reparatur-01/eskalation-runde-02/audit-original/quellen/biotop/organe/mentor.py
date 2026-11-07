"""Organ 3.4 — Mentor: Richtungen setzen, bevor gearbeitet wird (schwerer Aufruf).

Ausgang: 3–5 Entwicklungsrichtungen, je mit Ertrag (welches Maß würde steigen), Risiko (welche Verträge und Bereiche
berührt), Aufwand in Generationen, berührte Bereiche, und — wo vorhanden — dem Verweis auf einen Eintrag des
Artgedächtnisses ([A<id>]). Philipp wählt; das Biotop empfiehlt nur. Für Übungswerke wählt Hermes unter Vollmacht
(protokolliert). Die gewählte Richtung wird dem Schwarm jeder Generation als Auftrag mitgegeben (laeufe.richtung).

Das Modell erhält: Landkarte Stufe 0/1, Verfassung, Maßstand je Bereich, explizite Verträge (Namen), das Archiv offener
Funde, das Artgedächtnis (mit Kennungen) und die Entropie des Werks (falls ein Vorlauf gesättigt war).
Mechanisch geprüft wird: JSON-Form, 3–5 Richtungen, Pflichtfelder, Artgedächtnis-Kennungen existieren wirklich.
"""

from __future__ import annotations

import json
import re
import sqlite3

from ..anbieter import AnbieterFehler, aufrufen
from ..kern import messgeraet, protokoll
from ..kern.datenbank import j, lj, transaktion
from . import gedaechtnis, landkarte, verfassung, vertraege

MODELL = ("openrouter", "anthropic/claude-sonnet-5")  # schwerer Aufruf (Abschnitt 6), zweck-Präfix schwer.

SYSTEM = """Du bist der Mentor eines Biotops, das Software-Werke in Generationen messbar hebt. Du setzt die Richtung, bevor gearbeitet wird:
nicht „was ist kaputt“, sondern „was könnte dieses Werk werden“ — und was davon ein hartes Maß hebt.
Harte Maße: Kernmaß je Bereich = −(fehlgeschlagene Tests) − Sicherheitspunkte − tote Funktionen (Höchstwert 0); Grenzmaße Laufzeit/größte Funktion;
Pareto je Test; Verträge an den Grenzen. Bestandene Tests zählen nicht; Umformung ohne Maßgewinn wird abgelehnt.
Du bekommst das Artgedächtnis (Erfahrungen aus anderen Werken/Läufen mit Kennungen [A<id>]). Wo eine Erfahrung passt, verweise
AUSDRÜCKLICH auf ihre Kennung im Feld "artgedaechtnis" — nur echte Kennungen aus der Liste, keine erfundenen.
Einträge des EIGENEN Werks sind Projektgedächtnis, kein Artgedächtnis: trage sie unter "projektgedaechtnis" ein; unter "artgedaechtnis" stehen nur Einträge ANDERER Werke (werkübergreifende Erfahrung).
Antworte NUR mit JSON:
{"richtungen": [{"name": "...", "ziel": "1–2 Sätze", "ertrag": "welches Maß steigt (konkret, mit erwarteter Zahl)", "risiko": "welche Verträge/Bereiche berührt, was brechen kann",
  "aufwand_generationen": <int>, "bereiche": ["..."], "vertraege": ["test_vertrag_..." oder leer], "artgedaechtnis": ["A12", ...] oder [], "projektgedaechtnis": ["A7", ...] oder [], "nische": "sicher|schnell|elegant|wild"}],
 "empfehlung": "<name>", "begruendung": "2–3 Sätze"}
3 bis 5 Richtungen, jedes Textfeld höchstens 2 Sätze (die Antwort muss vollständig sein). Wenn das Werk am Höchstwert des Kernmaßes steht, sag das und nenne Richtungen, die Grenzmaße (Laufzeit) oder neue harte Maße betreffen — und eine Richtung „Sättigung anerkennen“ ist zulässig."""


def _tabelle(con):
    con.executescript("""CREATE TABLE IF NOT EXISTS mentor (id INTEGER PRIMARY KEY, lauf_id INTEGER, werk_id INTEGER, richtungen TEXT, empfehlung TEXT,
        begruendung TEXT, modell TEXT, gewaehlt TEXT, gewaehlt_von TEXT, erstellt_am TEXT);""")


def richtungen(con: sqlite3.Connection, lauf_id: int) -> dict:
    _tabelle(con)
    lauf = con.execute("SELECT * FROM laeufe WHERE id=?", (lauf_id,)).fetchone()
    werk = con.execute("SELECT * FROM werke WHERE id=?", (lauf["werk_id"],)).fetchone()
    b = lj(werk["bericht"]) or {}
    paket = b.get("paket")
    bereiche = landkarte.bereiche_finden(__import__("pathlib").Path(werk["pfad"]), paket)
    sicht = "\n".join(f"Stufe {z['stufe']} {z['schluessel']}: {z['inhalt'][:600]}" for z in con.execute("SELECT stufe, schluessel, inhalt FROM landkarte WHERE werk_id=? AND stufe<=1 ORDER BY stufe, schluessel", (werk["id"],)))
    verf = verfassung.lesen(con, werk["id"])
    g0 = con.execute("SELECT masse FROM generationen WHERE lauf_id=? AND status='angenommen' ORDER BY nummer DESC LIMIT 1", (lauf_id,)).fetchone()
    masse = {}
    if g0 and g0["masse"]:
        m = lj(g0["masse"])
        masse = {bb: {k: v for k, v in messgeraet.bereich_masse(m, bb).items() if not isinstance(v, (list, dict))} for bb in bereiche}
    vt = [v["pfad"] for v in vertraege.alle(con, werk["id"])]
    offen = [dict(z) for z in con.execute("SELECT bereich, name, status, substr(ursprung,1,160) u FROM immunsystem WHERE werk_id=? AND status IN ('offen','offen_norm','archiviert') LIMIT 30", (werk["id"],))]
    art = gedaechtnis.art_text(con, werk["id"])
    ent = ""
    for z in con.execute("SELECT grund FROM laeufe WHERE werk_id=? AND status='gesaettigt'", (werk["id"],)):
        ent += "\n- " + (z["grund"] or "")[:300]
    nutzer = (f"WERK {werk['name']} (Paket {paket}, Werkklasse {gedaechtnis.werkklasse(con, werk['id'])})\n\nLANDKARTE (Stufe 0/1):\n{sicht}\n\n"
              f"VERFASSUNG:\n{(verf or {}).get('text', '(keine)')}\n\nMASSSTAND JE BEREICH (aktuell): {j(masse)}\n\nEXPLIZITE VERTRÄGE: {vt}\n\n"
              f"OFFENE/ARCHIVIERTE FUNDE DES IMMUNSYSTEMS: {j(offen)}\n\nARTGEDÄCHTNIS:\n{art}\n\nFRÜHERE SÄTTIGUNGSMELDUNGEN AN DIESEM WERK:{ent or ' keine'}")
    try:
        a = aufrufen(con, lauf_id, MODELL[0], MODELL[1], SYSTEM, nutzer, zweck="schwer.mentor", max_tokens=6000, temperatur=0.4)
    except AnbieterFehler as e:
        protokoll.schreiben(con, "mentor.fehler", lauf_id=lauf_id, fehler=str(e)[:300])
        raise
    text = a.text.strip()
    m = re.search(r"\{.*\}", text, re.S)
    try:
        d = json.loads(m.group(0) if m else text)
    except json.JSONDecodeError:
        protokoll.schreiben(con, "mentor.fehler", lauf_id=lauf_id, fehler="kein JSON", antwort=text[:500])
        raise RuntimeError("Mentor: Antwort ist kein JSON (laut scheitern)")
    rs = d.get("richtungen") or []
    eigenes = gedaechtnis.werkname(con, werk["id"])
    werk_von = {f"A{z['id']}": z["werk"] for z in con.execute("SELECT id, werk FROM artgedaechtnis")}
    # Tor 3 (Vorgabe Philipp 19.09.2026): Artgedächtnis-Verweise zählen nur WERKÜBERGREIFEND; Verweise auf das eigene Werk sind Projektgedächtnis
    pruefung = {"anzahl": len(rs), "anzahl_ok": 3 <= len(rs) <= 5, "pflichtfelder_ok": [], "artgedaechtnis_werkuebergreifend": [], "eigenes_werk_projektgedaechtnis": [], "erfundene_verweise": [],
                "richtungen_mit_werkuebergreifendem_verweis": 0}
    for r in rs:
        pruefung["pflichtfelder_ok"].append(all(k in r and r[k] not in (None, "") for k in ("name", "ertrag", "risiko", "aufwand_generationen", "bereiche")))
        fremd = []
        for k in list(r.get("artgedaechtnis") or []) + list(r.get("projektgedaechtnis") or []):
            if k not in werk_von:
                pruefung["erfundene_verweise"].append(k)
            elif werk_von[k] == eigenes:
                pruefung["eigenes_werk_projektgedaechtnis"].append(k)
            else:
                pruefung["artgedaechtnis_werkuebergreifend"].append(k); fremd.append(k)
        r["_verweise_werkuebergreifend"] = fremd
        r["_verweise_eigenes_werk"] = [k for k in list(r.get("artgedaechtnis") or []) + list(r.get("projektgedaechtnis") or []) if werk_von.get(k) == eigenes]
        pruefung["richtungen_mit_werkuebergreifendem_verweis"] += bool(fremd)
    with transaktion(con):
        cur = con.execute("INSERT INTO mentor(lauf_id, werk_id, richtungen, empfehlung, begruendung, modell, erstellt_am) VALUES (?,?,?,?,?,?,?)",
                          (lauf_id, werk["id"], j(rs), d.get("empfehlung"), d.get("begruendung"), MODELL[1], protokoll.jetzt()))
    protokoll.schreiben(con, "mentor.richtungen", lauf_id=lauf_id, mentor_id=cur.lastrowid, anzahl=len(rs), empfehlung=d.get("empfehlung"),
                        pruefung=pruefung, richtungen=[{k: r.get(k) for k in ("name", "ertrag", "aufwand_generationen", "bereiche", "artgedaechtnis", "projektgedaechtnis", "_verweise_werkuebergreifend", "_verweise_eigenes_werk", "nische")} for r in rs])
    return {"mentor_id": cur.lastrowid, "richtungen": rs, "empfehlung": d.get("empfehlung"), "begruendung": d.get("begruendung"), "pruefung": pruefung, "modell": MODELL[1]}


def waehlen(con: sqlite3.Connection, lauf_id: int, name: str, von: str) -> dict:
    """Philipp (oder Hermes unter Vollmacht bei Übungswerken) wählt eine Richtung; sie wird dem Lauf zugeordnet."""
    _tabelle(con)
    z = con.execute("SELECT * FROM mentor WHERE lauf_id=? ORDER BY id DESC LIMIT 1", (lauf_id,)).fetchone()
    if not z:
        raise RuntimeError("keine Richtungen vorhanden — zuerst `biotop mentor <lauf>`")
    rs = lj(z["richtungen"])
    r = next((x for x in rs if x.get("name") == name), None)
    if not r:
        raise RuntimeError(f"Richtung {name!r} nicht unter {[x.get('name') for x in rs]}")
    lauf = con.execute("SELECT werk_id FROM laeufe WHERE id=?", (lauf_id,)).fetchone()
    verf = verfassung.lesen(con, lauf["werk_id"])
    uebungswerk = bool(((verf or {}).get("regeln") or {}).get("uebungswerk"))
    if not von.lower().startswith("philipp") and not uebungswerk:
        raise RuntimeError("Richtung eines Werks mit Betriebszweck wählt nur Philipp (3.4)")
    with transaktion(con):
        con.execute("UPDATE mentor SET gewaehlt=?, gewaehlt_von=? WHERE id=?", (name, von, z["id"]))
        con.execute("UPDATE laeufe SET richtung=? WHERE id=?", (j(r), lauf_id))
    protokoll.schreiben(con, "mentor.gewaehlt", lauf_id=lauf_id, richtung=name, von=von,
                        vollmacht=("Vollmacht Abschnitt 4 (Übungswerk)" if uebungswerk and not von.lower().startswith("philipp") else None), empfehlung=z["empfehlung"])
    return {"gewaehlt": r, "von": von}


def richtung_text(con, lauf_id: int) -> str:
    z = con.execute("SELECT richtung FROM laeufe WHERE id=?", (lauf_id,)).fetchone()
    r = lj(z["richtung"]) if z and z["richtung"] else None
    if not r:
        return ""
    return (f"\n\nRICHTUNG DIESES LAUFS (vom Mentor gesetzt, gewählt): {r.get('name')} — {r.get('ziel', '')} Ertrag: {r.get('ertrag', '')} "
            f"Bereiche: {r.get('bereiche')}. Arbeite in dieser Richtung; anderes nur, wenn es ein Maß messbar hebt.")
