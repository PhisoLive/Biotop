"""Organ „Generation minus eins" — das Messgerät eichen, BEVOR ein Lauf beginnt (Fassung 5 Abschnitt 3.5,
Rauschregeln nach Fassung 6, Festlegung Chat-Claude 19.09.2026).

Teil 1 (hier): Rauschmessung je Bereich mit bereichsweiser Sperre.
  - fünf Werte je Bereich; ein Einzelwert über dem Fünffachen des Medians ist ein Maschinenaussetzer, wird
    verworfen und EINMAL nachgemessen (protokolliert);
  - Toleranz = getrimmte Spannweite (höchster und niedrigster gestrichen) + 10 Prozentpunkte, mindestens 1,15,
    höchstens 2,0;
  - Toleranz über 1,5 = Messproblem: DIESER Bereich wird gesperrt, seine Kandidaten werden nicht erzeugt, die
    Sperre steht mit Zahl im Bericht. Melden ALLE Bereiche ein Problem, startet der Lauf nicht.
  - Ein gesperrter Bereich wird vor jedem weiteren Lauf neu gemessen. Meldet derselbe Bereich dreimal
    hintereinander, ist das ein Befund über seine REFERENZLAST, nicht über die Maschine — er wird als solcher
    ausgewiesen (`befund_referenzlast`).

Teil 2 (eichproben): die vier Proben aus Tor 2 als Vorspann jedes Laufs — siehe `proben()`.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

from ..kern import messgeraet, protokoll
from ..kern.datenbank import lj, transaktion

SPERR_MELDUNGEN_BIS_BEFUND = 3


def _minuten(von: str, bis: str) -> float:
    """Abstand zweier ISO-Zeitstempel in Minuten; bei unlesbaren Stempeln 0."""
    from datetime import datetime
    try:
        return abs((datetime.fromisoformat(bis) - datetime.fromisoformat(von)).total_seconds()) / 60.0
    except Exception:
        return 0.0


def _tabelle(con):
    con.executescript("""CREATE TABLE IF NOT EXISTS eichung (
        id INTEGER PRIMARY KEY, lauf_id INTEGER, werk_id INTEGER, bereich TEXT, toleranz REAL, spannweite REAL,
        median REAL, werte TEXT, aussetzer TEXT, nachgemessen INTEGER, gesperrt INTEGER, meldung TEXT, erstellt_am TEXT);
        CREATE TABLE IF NOT EXISTS eichkosten (
        id INTEGER PRIMARY KEY, lauf_id INTEGER, werk_id INTEGER, teil TEXT, kammerlaeufe INTEGER,
        modellaufrufe INTEGER, kosten_eur REAL, dauer_s REAL, erstellt_am TEXT);""")


ZWECK = "eichung."   # jeder Modellaufruf der Eichung trägt diesen Zweck-Vorsatz → in der Kasse trennbar


def kosten_buchen(con, lauf_id: int, werk_id: int, teil: str, kammerlaeufe: int, dauer_s: float,
                  modellaufrufe: int | None = None, kosten_eur: float | None = None) -> None:
    """Eichkosten getrennt führen (Festlegung Chat-Claude, Fassung 6): Kammerläufe und Modellaufrufe einzeln,
    nicht in der Gesamtsumme des Laufs.

    `modellaufrufe`/`kosten_eur` werden vom Aufrufer gemessen (Kassenstand vor/nach der Probe) — der Zweck-Vorsatz
    `eichung.` allein trägt nicht, weil die Proben den echten Ankläger aufrufen und dessen Aufrufe unter ihrem
    eigenen Zweck laufen sollen; sonst wäre der Anklägeraufruf einer Probe im Kassenblatt nicht als solcher
    erkennbar. Fehlen die Angaben, wird über den Zweck-Vorsatz nachgerechnet (Differenz zum bereits Verbuchten).

    Ein bereits vorhandener Eintrag desselben Teils im selben Lauf wird ERSETZT, nicht ergänzt — sonst summieren
    wiederholte Läufe des Prüfskripts sich auf und die Zahl im Bericht wächst ohne Grund."""
    _tabelle(con)
    if modellaufrufe is None or kosten_eur is None:
        z = con.execute("SELECT COUNT(*) n, COALESCE(SUM(kosten_eur),0) c FROM kasse WHERE lauf_id=? AND zweck LIKE ?",
                        (lauf_id, ZWECK + "%")).fetchone()
        v = con.execute("SELECT COALESCE(SUM(modellaufrufe),0) n, COALESCE(SUM(kosten_eur),0) c FROM eichkosten"
                        " WHERE lauf_id=? AND teil!=?", (lauf_id, teil)).fetchone()
        modellaufrufe = max(0, z["n"] - v["n"])
        kosten_eur = round(max(0.0, z["c"] - v["c"]), 6)
    with transaktion(con):
        con.execute("DELETE FROM eichkosten WHERE lauf_id=? AND teil=?", (lauf_id, teil))
        con.execute("INSERT INTO eichkosten(lauf_id, werk_id, teil, kammerlaeufe, modellaufrufe, kosten_eur, dauer_s, erstellt_am)"
                    " VALUES (?,?,?,?,?,?,?,?)",
                    (lauf_id, werk_id, teil, kammerlaeufe, modellaufrufe, round(kosten_eur, 6),
                     round(dauer_s, 1), protokoll.jetzt()))


def kosten(con, lauf_id: int) -> dict:
    """Eichkosten eines Laufs, getrennt nach Teil — für den Bericht und für die Phase-4-Schätzung."""
    _tabelle(con)
    teile = [dict(z) for z in con.execute(
        "SELECT teil, SUM(kammerlaeufe) kammerlaeufe, SUM(modellaufrufe) modellaufrufe, SUM(kosten_eur) kosten_eur,"
        " SUM(dauer_s) dauer_s FROM eichkosten WHERE lauf_id=? GROUP BY teil ORDER BY teil", (lauf_id,))]
    return {"teile": teile,
            "kammerlaeufe": sum(t["kammerlaeufe"] or 0 for t in teile),
            "modellaufrufe": sum(t["modellaufrufe"] or 0 for t in teile),
            "kosten_eur": round(sum(t["kosten_eur"] or 0.0 for t in teile), 6),
            "dauer_s": round(sum(t["dauer_s"] or 0 for t in teile), 1)}


def kosten_text(k: dict, bereiche: int) -> list[str]:
    """Berichtszeilen: Eichkosten GETRENNT von der Laufsumme, Kammerläufe und Modellaufrufe einzeln.

    Keine lineare Hochrechnung auf die Bereichszahl: Die Rauschmessung misst ALLE Bereiche in einem Kammerlauf
    (fünf Läufe, unabhängig davon, ob vier oder siebzehn Bereiche gemessen werden). Was mit der Bereichszahl
    wächst, ist die DAUER je Lauf, nicht ihre Zahl. Eine Zeile „× 17 Dienste" wäre hier eine erfundene Zahl.
    """
    z = ["Eichkosten (Generation minus eins) — getrennt ausgewiesen, nicht in der Laufsumme enthalten:"]
    for t in k["teile"]:
        z.append(f"  {t['teil']:<22} {t['kammerlaeufe'] or 0:>4} Kammerläufe | {t['modellaufrufe'] or 0:>3} Modellaufrufe "
                 f"| {t['kosten_eur'] or 0.0:.4f} € | {t['dauer_s'] or 0:.0f} s")
    z.append(f"  {'SUMME':<22} {k['kammerlaeufe']:>4} Kammerläufe | {k['modellaufrufe']:>3} Modellaufrufe "
             f"| {k['kosten_eur']:.4f} € | {k['dauer_s']:.0f} s")
    if bereiche:
        z.append(f"  Bezugsgröße: {bereiche} Bereiche, {k['dauer_s']/max(1,k['kammerlaeufe']):.1f} s je Kammerlauf. "
                 f"Die Zahl der Kammerläufe hängt NICHT an der Bereichszahl (alle Bereiche werden je Lauf zusammen "
                 f"gemessen) — mit mehr Bereichen wächst die Dauer je Lauf, nicht ihre Zahl. Für Phase 4 ist daher "
                 f"die Dauer je Kammerlauf am dortigen Werk zu messen, nicht von hier hochzurechnen.")
    return z


def _messen_einmal(pfad: Path, bereiche: list[str], paket: str, ref: str) -> dict:
    m = messgeraet.messen(pfad, bereiche, paket, ref)
    return {b: (m["bereiche"].get(b) or {}).get("laufzeit_ms") for b in bereiche}


def rauschmessung(con: sqlite3.Connection, lauf_id: int, werk_id: int, pfad: Path, bereiche: list[str],
                  paket: str, ref: str) -> dict:
    """Fünf Messungen am UNVERÄNDERTEN Werk; je Bereich Toleranz, Sperre und Vorgeschichte.
    Rückgabe: {"toleranz": {bereich: faktor}, "gesperrt": [...], "bereiche": {...}, "lauf_startet": bool}."""
    _tabelle(con)
    import time
    t0 = time.time()
    kammerlaeufe = 0
    roh: dict[str, list[float]] = {b: [] for b in bereiche}
    for _ in range(messgeraet.RAUSCH_MESSUNGEN):
        kammerlaeufe += 1
        for b, v in _messen_einmal(pfad, bereiche, paket, ref).items():
            if v is not None:
                roh[b].append(float(v))

    ergebnis, toleranz, gesperrt = {}, {}, []
    for b in bereiche:
        e = messgeraet.rauschtoleranz_aus_werten(roh[b])
        # Aussetzer: einmal nachmessen, damit wieder fünf brauchbare Werte vorliegen (Fassung 6).
        if e.get("nachmessen") and e.get("aussetzer"):
            fehlend = messgeraet.RAUSCH_MESSUNGEN - len([w for w in roh[b] if w not in e["aussetzer"]])
            nach = []
            for _ in range(max(0, fehlend)):
                kammerlaeufe += 1
                v = _messen_einmal(pfad, [b], paket, ref).get(b)
                if v is not None:
                    nach.append(float(v))
            protokoll.schreiben(con, "eichung.aussetzer", lauf_id=lauf_id, bereich=b, verworfen=e["aussetzer"],
                                nachgemessen=[round(x, 2) for x in nach],
                                regel="Einzelwert über dem Fünffachen des Medians ist ein Maschinenaussetzer (Fassung 6)")
            behalten = [w for w in roh[b] if w not in e["aussetzer"]] + nach
            e = messgeraet.rauschtoleranz_aus_werten(behalten)
            e["nachgemessen"] = True
        if e.get("nachmessen") and not e.get("meldung"):
            e["meldung"] = "Rauschmessung nach einmaligem Nachmessen weiterhin unvollständig oder mit Aussetzer — Bereich gesperrt"

        # Vorgeschichte: wie oft hat dieser Bereich UNMITTELBAR zuvor hintereinander gemeldet — und wann?
        # Der Zeitraum gehört zum Befund: drei Meldungen in einer Sitzung deuten auf die Maschine (fremde Last,
        # Container-Hänger), drei an verschiedenen Tagen auf die Referenzlast selbst (Festlegung Chat-Claude, F6).
        vorher = [dict(z) for z in con.execute(
            "SELECT gesperrt, erstellt_am FROM eichung WHERE werk_id=? AND bereich=? ORDER BY id DESC LIMIT 10",
            (werk_id, b))]
        serie_vorher, zeiten = 0, []
        for x in vorher:                       # jüngste zuerst; beim ersten nicht gesperrten Lauf endet die Serie
            if not x["gesperrt"]:
                break
            serie_vorher += 1
            zeiten.append(x["erstellt_am"])
        jetzt = protokoll.jetzt()
        serie = serie_vorher + 1 if e.get("meldung") else 0
        e["serie"] = serie
        e["serie_zeitraum"] = [min(zeiten + [jetzt]), max(zeiten + [jetzt])] if e.get("meldung") else None
        e["befund_referenzlast"] = bool(e.get("meldung")) and serie >= SPERR_MELDUNGEN_BIS_BEFUND
        if e["befund_referenzlast"]:
            von, bis = e["serie_zeitraum"]
            tage = len({t[:10] for t in zeiten + [jetzt]})
            spanne_min = _minuten(von, bis)
            if tage >= 2:
                deutung = (f"an {tage} verschiedenen Tagen ({von[:16]} bis {bis[:16]}) — das deutet auf die "
                           f"REFERENZLAST von `{b}`: sie misst etwas Unstetes, unabhängig vom Zustand der Maschine")
            else:
                deutung = (f"innerhalb einer Sitzung ({von[:16]} bis {bis[:16]}, {spanne_min:.0f} Minuten) — das deutet "
                           f"eher auf die MASCHINE (fremde Last, Container-Hänger) als auf die Referenzlast; "
                           f"vor einem Befund über `{b}` an einem anderen Tag nachmessen. "
                           f"VORBEHALT: Eine unruhige Maschine verfälscht JEDE Laufzeitmessung dieses Zeitraums — "
                           f"alle Grenzmaßzahlen, die zwischen {von[:16]} und {bis[:16]} entstanden sind, stehen unter "
                           f"Vorbehalt, nicht nur die des gesperrten Bereichs `{b}`; der Bericht muss das aussprechen.")
            e["serie_deutung"] = "referenzlast" if tage >= 2 else "maschine"
            if e["serie_deutung"] == "maschine":
                e["vorbehalt_zeitraum"] = {
                    "von": von, "bis": bis,
                    "gilt_fuer": "alle Laufzeitmessungen dieses Zeitraums, nicht nur den gesperrten Bereich",
                    "satz": (f"Vorbehalt: Zwischen {von[:16]} und {bis[:16]} war die Maschine unruhig ({serie} Sperrmeldungen "
                             f"in Folge in einer Sitzung). Jede Laufzeit- und Grenzmaßzahl aus diesem Zeitraum steht unter "
                             f"Vorbehalt — auch die der nicht gesperrten Bereiche.")}
            e["meldung"] += f" — {serie}. Meldung dieses Bereichs in Folge, {deutung}."
        e["gesperrt"] = bool(e.get("meldung"))
        if e["gesperrt"]:
            gesperrt.append(b)
        else:
            toleranz[b] = e["toleranz"]
        ergebnis[b] = e
        with transaktion(con):
            con.execute("INSERT INTO eichung(lauf_id, werk_id, bereich, toleranz, spannweite, median, werte, aussetzer,"
                        " nachgemessen, gesperrt, meldung, erstellt_am) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                        (lauf_id, werk_id, b, e["toleranz"], e.get("spannweite"), e.get("median"),
                         str(e.get("werte")), str(e.get("aussetzer")), int(bool(e.get("nachgemessen"))),
                         int(e["gesperrt"]), e.get("meldung"), protokoll.jetzt()))

    startet = len(gesperrt) < len(bereiche)
    kosten_buchen(con, lauf_id, werk_id, "rauschmessung", kammerlaeufe, time.time() - t0)
    protokoll.schreiben(con, "eichung.rauschmessung", lauf_id=lauf_id, werk_id=werk_id,
                        toleranz=toleranz, gesperrt=gesperrt, lauf_startet=startet,
                        bereiche={b: {k: ergebnis[b].get(k) for k in ("toleranz", "spannweite", "median", "werte",
                                                                      "aussetzer", "serie", "befund_referenzlast")}
                                  for b in bereiche},
                        regel="Fassung 6: 5 Werte, getrimmte Spannweite, Deckel 2,0, Meldeschwelle 1,5, "
                              "Aussetzer über 5x Median verworfen und einmal nachgemessen; Sperre bereichsweise")
    if not startet:
        protokoll.schreiben(con, "eichung.lauf_startet_nicht", lauf_id=lauf_id,
                            grund=f"alle {len(bereiche)} Bereiche melden ein Messproblem — kein Bereich hat eine "
                                  f"brauchbare Rauschtoleranz (Satz 6: laut scheitern, nie still)")
    return {"toleranz": toleranz, "gesperrt": gesperrt, "bereiche": ergebnis, "lauf_startet": startet,
            "bezugsgroesse": f"{len(gesperrt)} von {len(bereiche)} Bereichen gesperrt"}


def text(ergebnis: dict) -> list[str]:
    """Berichtszeilen — jede Sperre mit Zahl, wie vom Auftraggeber verlangt."""
    z = [f"Rauschmessung: {ergebnis['bezugsgroesse']}"]
    vorbehalte = []
    for b, e in ergebnis["bereiche"].items():
        if e["gesperrt"]:
            z.append(f"  Bereich {b} ÜBERSPRUNGEN, Toleranz {e['toleranz']:.2f} (Spannweite {100*(e.get('spannweite') or 0):.0f} %, "
                     f"Median {e.get('median')} ms, Werte {e.get('werte')}, Meldung {e['serie']} in Folge)"
                     + ("  ← BEFUND ÜBER DIE REFERENZLAST" if e.get("serie_deutung") == "referenzlast" else "")
                     + ("  ← BEFUND ÜBER DIE MASCHINE" if e.get("serie_deutung") == "maschine" else ""))
            if e.get("vorbehalt_zeitraum"):
                vorbehalte.append(e["vorbehalt_zeitraum"]["satz"])
        else:
            z.append(f"  Bereich {b}: Toleranz {e['toleranz']:.2f} (Spannweite {100*(e.get('spannweite') or 0):.0f} %, "
                     f"Median {e.get('median')} ms{', Aussetzer ' + str(e['aussetzer']) + ' verworfen und nachgemessen' if e.get('aussetzer') else ''})")
    for s in dict.fromkeys(vorbehalte):        # ein Zeitraum, ein Satz — auch wenn mehrere Bereiche ihn auslösen
        z.append(f"  {s}")
    if not ergebnis["lauf_startet"]:
        z.append("  LAUF STARTET NICHT: alle Bereiche melden ein Messproblem.")
    return z
