"""Gegenstand der Eichproben — je Werk EINMAL gewählt, versiegelt, danach unverändert
(Festlegung Chat-Claude 19.09.2026, Fassung 6).

Warum versiegelt: Jede Eichprobe braucht einen Gegenstand — ein Bereichspaar mit Vertrag, an dem sie ansetzt.
Wählt jeder Lauf seinen Gegenstand neu, misst jede Eichung etwas anderes und ist mit der vorigen nicht
vergleichbar; die Zahlen aus Lauf n und Lauf n+1 stehen dann nebeneinander, ohne dasselbe zu bedeuten.
Genau daran scheiterten die Proben in Phase 2/3 mehrfach: Sie hingen an Textankern im Quelltext, die eine
angenommene Generation verschob — dann zielten sie stillschweigend woanders hin.

Fällt der versiegelte Gegenstand durch eine Änderung des Werks weg (Bereich entfernt, Vertragsdatei gelöscht,
Vertrag umgeschrieben), ist das ein BEFUND: Er wird protokolliert, gemeldet, und es wird ein neuer Gegenstand
versiegelt — nie stillschweigend ein anderer genommen.
"""
from __future__ import annotations

import hashlib
import sqlite3
from pathlib import Path

from ..kern import protokoll
from ..kern.datenbank import lj, transaktion


def _tabelle(con):
    con.executescript("""CREATE TABLE IF NOT EXISTS eichgegenstand (
        id INTEGER PRIMARY KEY, werk_id INTEGER, von_bereich TEXT, nach_bereich TEXT, vertrag_pfad TEXT,
        vertrag_pruefsumme TEXT, begruendung TEXT, versiegelt_am TEXT, abgeloest_am TEXT, abloesegrund TEXT);""")


def _pruefsumme(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _kandidatenpaare(con, werk_id: int, pfad: Path) -> list[dict]:
    """Alle Bereichspaare mit explizitem Vertrag, deren Vertragsdatei im Werk liegt. Sortiert = deterministisch."""
    _tabelle(con)
    aus = []
    for z in con.execute("SELECT von_bereich, nach_bereich, pfad FROM vertraege_explizit WHERE werk_id=? "
                         "ORDER BY von_bereich, nach_bereich", (werk_id,)):
        datei = pfad / z["pfad"]
        if datei.exists():
            aus.append({"von_bereich": z["von_bereich"], "nach_bereich": z["nach_bereich"], "vertrag_pfad": z["pfad"],
                        "zeilen": len(datei.read_text().splitlines())})
    return aus


def _tragende_paare(con, werk_id: int, paare: list[dict]) -> tuple[dict, str]:
    """Welche Bereichspaare liegen auf dem von der Verfassung als tragend benannten Pfad? (Fassung 6)

    Reihenfolge der Quellen — nie geraten, immer benannt:
    1. Ausdrückliche Angabe in den Regeln des Werks: {"tragender_pfad": [["bericht","preise"], ...]}.
       Beim Handelssystem ist das der Orderpfad mit Risikomodulen und Verlustgrenze; Philipp setzt ihn in der
       Verfassung, zusammen mit Verlustgrenze und Hebelgrenzen.
    2. NUR BEI ÜBUNGSWERKEN: abgeleitet aus dem Verfassungstext — ein Paar gilt als tragend, wenn beide Bereiche
       in EINEM Satz gemeinsam genannt werden, gewichtet nach der Zahl solcher Sätze.
       Diese Ableitung ist eine **Wortstatistik**: Sie findet, was oft zusammen genannt wird, nicht was trägt.
       Für ein Werk mit Betriebszweck ist das zu wenig — dort entscheidet sie unter Umständen über den Orderpfad.
       Fehlt bei einem solchen Werk die ausdrückliche Angabe, wird NICHT abgeleitet: das Organ meldet und wartet
       (wie beim fehlenden Bereichspaar, Satz 6 „laut scheitern, nie still").
    3. Keine Verfassung / keine Nennung bei einem Übungswerk: leeres Ergebnis, dann entscheidet die Vertragsgröße.

    Rückgabe: ({(von, nach): gewicht}, Herkunft als Text). Ein `fehlt_ausdruecklich`-Vermerk in der Herkunft
    signalisiert dem Aufrufer, dass er anhalten muss.
    """
    z = con.execute("SELECT text, regeln FROM verfassung_werk WHERE werk_id=?", (werk_id,)).fetchone()
    if not z:
        return {}, "keine Verfassung hinterlegt"
    regeln = lj(z["regeln"]) or {}
    ausdruecklich = regeln.get("tragender_pfad")
    if ausdruecklich:
        g = {}
        for eintrag in ausdruecklich:
            g[(eintrag[0], eintrag[1])] = 100
        return g, "ausdrückliche Angabe in den Regeln des Werks (tragender_pfad)"

    if not regeln.get("uebungswerk"):
        return {}, ("FEHLT_AUSDRUECKLICH: Werk mit Betriebszweck ohne `tragender_pfad` in den Regeln. Die Ableitung "
                    "aus dem Verfassungstext ist eine Wortstatistik (sie findet, was oft zusammen genannt wird, nicht "
                    "was trägt) und ist hier nicht zulässig — der tragende Pfad muss ausdrücklich in der Verfassung "
                    "stehen, beim Handelssystem der Orderpfad mit Risikomodulen und Verlustgrenze.")

    text = z["text"] or ""
    bereiche = {p["von_bereich"] for p in paare} | {p["nach_bereich"] for p in paare}
    gewicht: dict = {}
    for satz in [s for s in text.splitlines() if s.strip()]:
        genannt = {b for b in bereiche if b in satz}
        if len(genannt) < 2:
            continue
        for p in paare:
            if p["von_bereich"] in genannt and p["nach_bereich"] in genannt:
                gewicht[(p["von_bereich"], p["nach_bereich"])] = gewicht.get((p["von_bereich"], p["nach_bereich"]), 0) + 1
    if gewicht:
        return gewicht, ("abgeleitet (nur zulässig bei Übungswerken; Wortstatistik): beide Bereiche in einem Satz "
                         "der Verfassung gemeinsam genannt")
    return {}, "Verfassung nennt kein Bereichspaar gemeinsam (Übungswerk)"


def lesen(con, werk_id: int) -> dict | None:
    _tabelle(con)
    z = con.execute("SELECT * FROM eichgegenstand WHERE werk_id=? AND abgeloest_am IS NULL ORDER BY id DESC LIMIT 1",
                    (werk_id,)).fetchone()
    return dict(z) if z else None


def sichern(con: sqlite3.Connection, werk_id: int, lauf_id: int, pfad: Path) -> dict:
    """Beim ersten Lauf wählen und versiegeln; bei jedem weiteren prüfen, dass er noch trägt.

    Rückgabe: {"gegenstand": {...}, "neu": bool, "befund": str|None, "geprueft": "unveraendert"|"neu versiegelt"|...}
    """
    _tabelle(con)
    alt = lesen(con, werk_id)
    paare = _kandidatenpaare(con, werk_id, pfad)

    if alt:
        datei = pfad / alt["vertrag_pfad"]
        if not datei.exists():
            befund = (f"Der versiegelte Eichgegenstand {alt['von_bereich']}→{alt['nach_bereich']} ist weggefallen: "
                      f"Vertragsdatei `{alt['vertrag_pfad']}` liegt nicht mehr im Werk.")
        elif _pruefsumme(datei) != alt["vertrag_pruefsumme"]:
            befund = (f"Der versiegelte Eichgegenstand {alt['von_bereich']}→{alt['nach_bereich']} hat sich geändert: "
                      f"Vertragsdatei `{alt['vertrag_pfad']}` hat eine andere Prüfsumme als bei der Versiegelung "
                      f"({alt['vertrag_pruefsumme'][:16]} → {_pruefsumme(datei)[:16]}). Eine Eichung an diesem "
                      f"Gegenstand ist mit den vorigen nicht mehr vergleichbar.")
        else:
            return {"gegenstand": alt, "neu": False, "befund": None, "geprueft": "unveraendert"}
        # Befund: ablösen und neu versiegeln, nie stillschweigend wechseln
        with transaktion(con):
            con.execute("UPDATE eichgegenstand SET abgeloest_am=?, abloesegrund=? WHERE id=?",
                        (protokoll.jetzt(), befund, alt["id"]))
        protokoll.schreiben(con, "eichgegenstand.weggefallen", lauf_id=lauf_id, werk_id=werk_id, befund=befund,
                            alter_gegenstand=f"{alt['von_bereich']}→{alt['nach_bereich']} ({alt['vertrag_pfad']})",
                            regel="Fassung 6: Fällt der versiegelte Gegenstand weg, ist das ein Befund und ein neuer "
                                  "versiegelter Gegenstand — protokolliert, nie still gewechselt.")
    else:
        befund = None

    if not paare:
        protokoll.schreiben(con, "eichgegenstand.fehlt", lauf_id=lauf_id, werk_id=werk_id,
                            grund="kein Bereichspaar mit vorhandener Vertragsdatei — die Eichproben haben keinen "
                                  "Gegenstand (Satz 6: laut scheitern, nie still bestehen)")
        return {"gegenstand": None, "neu": False, "befund": befund or "kein Bereichspaar mit Vertrag im Werk",
                "geprueft": "ohne Gegenstand"}

    # Wahl (Fassung 6): Erst der von der Verfassung als tragend benannte Pfad, DANN die Vertragsgröße.
    # Grund: Bei siebzehn Diensten ist der umfangreichste Vertrag nicht der aussagekräftigste; eine Eichung an
    # einem Nebenpfad übersieht Messgerätfehler im Kern (beim Handelssystem: Orderpfad mit Risikomodulen und
    # Verlustgrenze). Die Vertragsgröße entscheidet nur noch innerhalb der tragenden Paare — oder wenn die
    # Verfassung keines benennt.
    tragend, herkunft = _tragende_paare(con, werk_id, paare)
    # Werk mit Betriebszweck ohne ausdrücklichen tragenden Pfad: melden und warten, nicht ableiten (Fassung 6).
    if herkunft.startswith("FEHLT_AUSDRUECKLICH"):
        protokoll.schreiben(con, "eichgegenstand.wartet", lauf_id=lauf_id, werk_id=werk_id, grund=herkunft,
                            erwartet="Regeln des Werks um {\"tragender_pfad\": [[\"von\",\"nach\"], ...]} ergänzen — "
                                     "beim Handelssystem der Orderpfad mit Risikomodulen und Verlustgrenze; setzt Philipp.",
                            auswahl_aus=[f"{p['von_bereich']}→{p['nach_bereich']} ({p['zeilen']} Z.)" for p in paare])
        return {"gegenstand": None, "neu": False, "befund": herkunft, "geprueft": "wartet auf tragenden Pfad",
                "wartet": True}
    w = sorted(paare, key=lambda p: (-tragend.get((p["von_bereich"], p["nach_bereich"]), 0),
                                     -p["zeilen"], p["von_bereich"], p["nach_bereich"]))[0]
    ist_tragend = tragend.get((w["von_bereich"], w["nach_bereich"]), 0) > 0
    datei = pfad / w["vertrag_pfad"]
    ps = _pruefsumme(datei)
    if ist_tragend:
        begruendung = (f"liegt auf dem von der Verfassung als tragend benannten Pfad ({herkunft}, Gewicht "
                       f"{tragend[(w['von_bereich'], w['nach_bereich'])]}); unter den tragenden Paaren der "
                       f"umfangreichste Vertrag ({w['zeilen']} Zeilen). Verfassung geht der Vertragsgröße vor, "
                       f"weil eine Eichung an einem Nebenpfad Messgerätfehler im Kern übersieht.")
    else:
        begruendung = (f"Verfassung benennt kein tragendes Bereichspaar ({herkunft}) — daher nach Vertragsgröße: "
                       f"umfangreichster expliziter Vertrag ({w['zeilen']} Zeilen) von {len(paare)} Paaren mit Vertrag; "
                       f"deterministisch (Zeilenzahl, dann alphabetisch)")
    with transaktion(con):
        cur = con.execute("INSERT INTO eichgegenstand(werk_id, von_bereich, nach_bereich, vertrag_pfad, "
                          "vertrag_pruefsumme, begruendung, versiegelt_am) VALUES (?,?,?,?,?,?,?)",
                          (werk_id, w["von_bereich"], w["nach_bereich"], w["vertrag_pfad"], ps, begruendung,
                           protokoll.jetzt()))
    neu = lesen(con, werk_id)
    protokoll.schreiben(con, "eichgegenstand.versiegelt", lauf_id=lauf_id, werk_id=werk_id,
                        gegenstand=f"{w['von_bereich']}→{w['nach_bereich']}", vertrag=w["vertrag_pfad"],
                        pruefsumme=ps, begruendung=begruendung, ausloeser="Befund" if befund else "erster Lauf",
                        tragender_pfad={f"{a}→{b}": g for (a, b), g in tragend.items()}, herkunft_tragend=herkunft,
                        auswahl_aus=[f"{p['von_bereich']}→{p['nach_bereich']} ({p['zeilen']} Z., tragend "
                                     f"{tragend.get((p['von_bereich'], p['nach_bereich']), 0)})" for p in paare])
    return {"gegenstand": neu, "neu": True, "befund": befund,
            "geprueft": "neu versiegelt nach Befund" if befund else "erstmals versiegelt"}


def text(ergebnis: dict) -> list[str]:
    g = ergebnis.get("gegenstand")
    if ergebnis.get("wartet"):
        return [f"Eichgegenstand: WARTET — {ergebnis['befund']}",
                "  Kein Lauf ohne tragenden Pfad: bei einem Werk mit Betriebszweck wird er nicht abgeleitet."]
    if not g:
        return [f"Eichgegenstand: KEINER — {ergebnis.get('befund')}"]
    z = [f"Eichgegenstand (versiegelt {g['versiegelt_am'][:16]}): {g['von_bereich']}→{g['nach_bereich']}, "
         f"Vertrag `{g['vertrag_pfad']}`, Prüfsumme {g['vertrag_pruefsumme'][:16]} — {ergebnis['geprueft']}"]
    if ergebnis.get("befund"):
        z.append(f"  BEFUND: {ergebnis['befund']}")
    return z
