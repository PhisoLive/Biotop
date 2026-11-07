"""Tor-4-Skript (Behebungsrunde 5 vor T4, Entscheidung Chat-Claude 5, 24.09.2026).

Anlass: zum dritten Mal war etwas gebaut und nie gerufen (Review 04 Nr. 7: `gegenzeugen.torzeile_schwaechen` hatte
keinen Aufrufer). Deshalb steht dieses Skript im Register der verlangten Aufrufe (`kern/register.py`), und der
Verdrahtungstest verlangt den Aufruf im echten Lauf (`biotop tor4 <lauf> --altlasten <liste.json>`).

Torzeile „Schwächen“ für T4 (Fassung 8, Tor 4): statt versiegelter Schwächen eine unabhängig erhobene Altlastenliste.
Je Altlast die doppelte Prüfung (kern/gegenzeugen.torzeile_schwaechen, verbindlich in der Torzeile, nicht im
Annahmepfad):
  (a) Schwäche weg — der Gegenzeuge der Altlast (ein Test aus der Liste) läuft am Endstand (letzte angenommene
      Generation, aus Lazarus in einen Wegwerfordner) in der Kammer; besteht er, ist die Altlast weg.
  (b) Normalvergleich — für T4 das Verhalten der Vorgeneration über den Verhaltensvergleich (Entscheidung 5): die
      aufgezeichneten Urteile der angenommenen Kandidaten, deren Wirkungskreis den Bereich der Altlast enthält. Jede
      Abweichung zählt, außer sie ist durch einen unabhängigen Test aus der Altlastenliste gedeckt; eine
      verhaltensändernde Altlast braucht einen solchen Test (fehlt er: nicht beurteilbar, nie behoben).

Die übrigen Torzeilen von Tor 4 berechnet dieses Skript (noch) nicht; es nennt sie als „nicht berechnet“ — nie als
erfüllt.

Altlastenliste (JSON): {"werk", "quelle", "bezugsgroesse", "altlasten": [{"kennung", "beschreibung", "bereich",
"verhaltensaendernd": bool, "unabhaengiger_test": "datei::name" | null,
"gegenzeuge": {"datei": "tests/…", "code": "…"}}]}
"""
from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

from . import lauf as L
from .kern import gegenzeugen, protokoll
from .kern.datenbank import lj
from .organe import aegis, lazarus

NICHT_BERECHNET = ("Aufnahme", "Generation minus eins", "Generation 0", "Kein Rückschritt", "Halluzinationsprobe",
                   "Verhaltensvergleich", "Doppelungsanteil", "Immunisierung", "Neutralzähler", "Verbundausfall",
                   "Verdrahtung", "Sättigung oder Budgetabbruch")


class Tor4Fehler(L.LaufFehler):
    """Die Torzeile kann nicht belegt berechnet werden (Liste unbrauchbar, Endstand nicht herstellbar) — laut."""


def liste_lesen(pfad: str | Path) -> dict:
    d = json.loads(Path(pfad).read_text())
    alt = d.get("altlasten")
    if not isinstance(alt, list) or not alt:
        raise Tor4Fehler("Altlastenliste ohne Einträge — null Altlasten sind keine Torzeile")
    kennungen = [a.get("kennung") for a in alt]
    if len(set(kennungen)) != len(kennungen) or not all(isinstance(k, str) and k for k in kennungen):
        raise Tor4Fehler(f"Altlastenliste: Kennungen fehlen oder doppelt ({kennungen})")
    for a in alt:
        g = a.get("gegenzeuge") or {}
        if not a.get("bereich") or not isinstance(a.get("verhaltensaendernd"), bool) \
                or not str(g.get("datei", "")).startswith("tests/") or not g.get("code"):
            raise Tor4Fehler(f"Altlast {a.get('kennung')}: bereich, verhaltensaendernd und gegenzeuge {{datei, code}} "
                             f"sind Pflicht")
    return d


def gegenzeuge_am_endstand(ziel: Path, paket: str, a: dict) -> dict | None:
    """(a) Der Gegenzeuge der Altlast am Endstand. {"verletzt": bool, "faelle", "roh"}; None: nicht gemessen."""
    g = a["gegenzeuge"]
    r = aegis.junit_lauf(ziel, paket, {g["datei"]: g["code"]}, [g["datei"]])
    faelle = {k: v for k, v in r.items() if k.startswith(g["datei"] + "::")}
    if not faelle or any(k.endswith("::*") for k in faelle) or any(v.get("uebersprungen") for v in faelle.values()):
        return None
    return {"verletzt": not all(v.get("ok") for v in faelle.values()), "faelle": len(faelle),
            "roh": {k: {"ok": v.get("ok"), "meldung": v.get("meldung", "")[:200]} for k, v in faelle.items()}}


def _urteil(con, kid: int) -> dict | None:
    letzte = None
    for (inhalt,) in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr"):
        z = json.loads(inhalt)
        if z.get("kandidat") == kid:
            letzte = z
    return letzte


def normalvergleich(con, lauf_id: int, a: dict, liste: dict) -> tuple[dict | None, str]:
    """(b) Normalvergleich der Altlast über den Verhaltensvergleich (Entscheidung 5). Rückgabe (normal | None, grund)."""
    erlaubt = {x.get("unabhaengiger_test") for x in liste["altlasten"]
               if x.get("verhaltensaendernd") and x.get("unabhaengiger_test")}
    if a["verhaltensaendernd"] and not a.get("unabhaengiger_test"):
        return None, "verhaltensändernde Altlast ohne unabhängigen Test aus der Altlastenliste — nicht beurteilbar"
    kands = []
    for z in con.execute("SELECT k.id, k.bereich, k.wirkungskreis FROM kandidaten k JOIN generationen g "
                         "ON g.lauf_id=k.lauf_id AND g.nummer=k.generation WHERE k.lauf_id=? AND k.status='angenommen' "
                         "AND g.status='angenommen' AND COALESCE(k.ist_probe,0)=0 ORDER BY k.id", (lauf_id,)):
        kreis = lj(z["wirkungskreis"]) or []
        if a["bereich"] == z["bereich"] or a["bereich"] in kreis:
            kands.append(z["id"])
    if not kands:
        return None, f"kein angenommener Kandidat im Bereich {a['bereich']} — Verhalten nicht verglichen"
    faelle = abweichungen = gedeckt_unabhaengig = 0
    for kid in kands:
        v = (_urteil(con, kid) or {}).get("verhalten") or {}
        if not v.get("geurteilt") or not isinstance(v.get("beobachtungen"), int):
            return None, f"K{kid}: Verhaltensvergleich ohne Urteil ({v.get('grund_art')}) — nicht beurteilbar"
        faelle += v["beobachtungen"]
        gedeckt = v.get("gedeckt") or {}
        frei = sum(1 for tests in gedeckt.values() if set(tests or []) & erlaubt)
        gedeckt_unabhaengig += frei
        abweichungen += int(v.get("anzahl_abweichungen") or 0) - frei
    return ({"faelle": faelle, "abweichungen": abweichungen,
             "aufschluesselung": {"Kandidaten": f"{len(kands)} ({', '.join(f'K{k}' for k in kands)})",
                                  "durch unabhängigen Test gedeckt": str(gedeckt_unabhaengig)}},
            f"{len(kands)} angenommene(r) Kandidat(en) im Bereich {a['bereich']}")


def ausfuehren(con, lauf_id: int, altlasten_pfad: str | Path) -> dict:
    """Tor-4-Skript: berechnet die Torzeile „Schwächen“ mit doppelter Prüfung je Altlast und schreibt sie ins Protokoll."""
    liste = liste_lesen(altlasten_pfad)
    lauf = L._lauf(con, lauf_id)
    werk = L._werk(con, lauf["werk_id"])
    paket = (lj(lauf["mass"]) or {}).get("paket") or lj(werk["bericht"])["paket"]
    end = L.letzte_angenommene(con, lauf_id)
    if end is None:
        raise Tor4Fehler(f"Lauf {lauf_id}: keine angenommene Generation — kein Endstand")
    tmp = Path(tempfile.mkdtemp(prefix="tor4-"))
    try:
        ziel = tmp / "werk"
        r = lazarus.rueckkehr(con, lauf_id, end["nummer"], Path(werk["pfad"]), ziel)
        if not r["stimmt"]:
            raise Tor4Fehler(f"Endstand Generation {end['nummer']}: Prüfsumme weicht ab")
        schwaechen, gruende = {}, {}
        for a in liste["altlasten"]:
            s = gegenzeuge_am_endstand(ziel, paket, a)
            n, grund = normalvergleich(con, lauf_id, a, liste)
            schwaechen[a["kennung"]] = {"schwaeche": s, "normal": n}
            gruende[a["kennung"]] = grund
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    zeile = gegenzeugen.torzeile_schwaechen(schwaechen)
    for k, g in gruende.items():
        zeile["je_schwaeche"][k]["normalvergleich"] = g
    protokoll.schreiben(con, "tor4.schwaechen", lauf_id=lauf_id, endstand=end["nummer"], zeile=zeile["zeile"],
                        behoben=zeile["behoben"], gesamt=zeile["gesamt"], nicht_beurteilbar=zeile["nicht_beurteilbar"],
                        je_schwaeche=zeile["je_schwaeche"], quelle=liste.get("quelle"))
    return {"lauf": lauf_id, "endstand": end["nummer"], "schwaechen": zeile,
            "altlastenliste": {"quelle": liste.get("quelle"), "bezugsgroesse": liste.get("bezugsgroesse"),
                               "eintraege": len(liste["altlasten"])},
            "nicht_berechnet": list(NICHT_BERECHNET)}
