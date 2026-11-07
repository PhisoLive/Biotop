"""Nachspiel des Annahmepfads: aufgezeichnete Kandidaten durch genau die Funktion, die ein Lauf zur Annahme ruft.

Anlass (T3, Lauf 38): `verhaltensvergleich` und `masseichung` waren gebaut, getestet und gegen das Modul
gegengeprüft — und nirgends eingehängt. Die Gegenproben liefen gegen das Modul, nicht durch den Lauf. Ein
Nachspiel ruft deshalb `aegis.pruefen` mit dem Aufbau, den `lauf.generation()` dafür herstellt
(`lauf.annahme_tausch`, `lauf.bestwert_des_laufs`, `lauf.letzte_angenommene`, `lauf._referenzlast`) — keine
Nachbildung davon.

Woher jede Eingabe kommt:
- Kandidat (Diff, Nische, Bereich, Verträge): aus der Lauf-DB; Status in der KOPIE auf „erzeugt" zurückgesetzt.
- Vorgeneration: Lazarus-Schnappschuss über `lazarus.rueckkehr(ziel=…)`; weicht die Prüfsumme von der DB ab,
  bricht das Nachspiel ab.
- Maß, Rauschtoleranzen, Eichausgang: eingefrorenes Maß und versiegelter Vorspann-Nachweis des Laufs (gelesen,
  nicht über `vorspann.verlangen` — das würde den Nachweis wegen des seither geänderten Kerns zu Recht verwerfen).
- Maßeichung: `masseichung.eichen(nachweis.basis, masseichung.sauberer_bereich(verfassung))` — dieselben zwei
  Aufrufe wie im Vorspann, an der dort versiegelten Ausgangsmessung. Läufe vor dem Einbau tragen die Eichung nicht
  im Nachweis; sie wird dann aus denselben Daten gebildet und so gekennzeichnet (`eichung_herkunft`).
- Bestwert/Vorgeneration: aus der DB-Kopie, in der Generationen ab der Kandidatengeneration ausgeblendet sind.
- Offene Immuntests des Bereichs: genau die, die das aufgezeichnete Urteil vorlegte (tests_offen, immun_bestanden),
  ohne den eigenen Fund des Kandidaten — der entstand erst in dessen Angriff.
- Anbietergrenze: ersetzt. Aufgezeichnet ist je Kandidat nur die Ansage des Anklägers, nie der Angriffstext.
  Lautete sie „KEIN ANGRIFF", liefert die Grenze genau diese Antwort (0 Token, gekennzeichnet). Sonst bricht sie
  mit benannter Meldung ab; der Ankläger bucht das als Ausfall und urteilt ohne neuen Angriffstest — das steht im
  Beleg. Ein erfundener Angriff wird nicht eingesetzt.
- Kammer: echt (Docker, netzlos). Netz im Prozess gesperrt.

Die Original-DB wird nur gelesen (`mode=ro`); gearbeitet wird an einer Sicherungskopie in einem Wegwerfordner.
"""
from __future__ import annotations

import json
import socket
import sqlite3
from contextlib import contextmanager
from pathlib import Path

from . import anbieter
from . import lauf as L
from .kern import datenbank, messgeraet
from .kern.datenbank import lj, transaktion
from .organe import aegis, kammer, landkarte, lazarus, masseichung, verfassung

KENNUNG = "nachspiel: aufgezeichnete Ansage, kein Modellaufruf"
AUSGESCHALTET = "nachspiel_ausgeblendet"


class NachspielFehler(RuntimeError):
    """Das Nachspiel kann den Entscheidungszustand nicht belegt herstellen — kein Urteil, laut."""


class AufgezeichneteGrenze:
    """Ersetzt den Anbieter-Adapter. Antwortet nur, was aufgezeichnet ist: die Ansage „KEIN ANGRIFF"."""

    def __init__(self, ansage_kein_angriff: bool):
        self.kein_angriff = ansage_kein_angriff
        self.anfragen: list[dict] = []
        self._melder = None

    def senden(self, modell, system, nutzer, max_tokens, temperatur):
        ansage = system == aegis.ANSAGE_SYSTEM
        self.anfragen.append({"modell": modell, "art": "ansage" if ansage else "anderer Aufruf",
                              "beantwortet": bool(ansage and self.kein_angriff)})
        if ansage and self.kein_angriff:
            return "KEIN ANGRIFF", 0, 0
        raise anbieter.AnbieterFehler(
            "Nachspiel: Antwort nicht aufgezeichnet (" + ("Ansage mit Behauptung" if ansage else "Angriff/anderer Aufruf")
            + ") — kein echter Aufruf, kein Ersatztext", verbrauch=(0, 0), ausfallart="nachspiel")


@contextmanager
def _grenze(g: AufgezeichneteGrenze):
    alt_adapter, alt_connect, alt_create = anbieter.adapter, socket.socket.connect, socket.create_connection

    def gesperrt(*a, **k):
        raise AssertionError("Netzaufruf im Nachspiel gesperrt")

    anbieter.adapter = lambda name: g
    socket.socket.connect = gesperrt
    socket.create_connection = gesperrt
    try:
        yield g
    finally:
        anbieter.adapter = alt_adapter
        socket.socket.connect = alt_connect
        socket.create_connection = alt_create


def _kopie(quelle_db: Path, ziel: Path) -> sqlite3.Connection:
    src = sqlite3.connect(f"file:{quelle_db}?mode=ro", uri=True)
    dst = sqlite3.connect(ziel)
    src.backup(dst)
    src.close()
    dst.close()
    return datenbank.verbinden(ziel)


def _urteile(con, kandidat_id: int) -> list[tuple[int, dict]]:
    return [(z["nr"], lj(z["inhalt"])) for z in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.urteil' ORDER BY nr")
            if lj(z["inhalt"]).get("kandidat") == kandidat_id]


def _ansage_vor(con, kandidat_id: int, bis_nr: int) -> dict | None:
    letzte = None
    for z in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='aegis.ansage' AND nr<? ORDER BY nr", (bis_nr,)):
        i = lj(z["inhalt"])
        if i.get("kandidat") == kandidat_id:
            letzte = {"nr": z["nr"], **i}
    return letzte


def _vorgelegte_immuntests(urteil: dict, kandidat_id: int) -> list[str]:
    namen = set()
    for p in list(urteil.get("tests_offen") or []) + [f"_immun_{n}" for n in (urteil.get("immun_bestanden") or [])]:
        if "_immun_" not in p or "_immun_befundklasse_" in p:
            continue
        n = p.split("_immun_", 1)[1]
        for endung in (".test.ts", ".py"):
            n = n.removesuffix(endung)
        if f"k{kandidat_id}_" not in n:
            namen.add(n)
    return sorted(namen)


def vorbereiten(quelle_db: Path, kandidat_id: int, arbeit: Path, *, urteil_nr: int | None = None,
                partner_id: int | None = None, masseichung_an: bool = True) -> dict:
    """Stellt den Zustand her, in dem der Lauf über den Kandidaten entschied. Rückgabe: Fall mit allen Eingaben."""
    arbeit.mkdir(parents=True, exist_ok=True)
    con = _kopie(Path(quelle_db), arbeit / "nachspiel.db")
    k = con.execute("SELECT * FROM kandidaten WHERE id=?", (kandidat_id,)).fetchone()
    if k is None:
        raise NachspielFehler(f"Kandidat {kandidat_id} fehlt in {quelle_db}")
    lauf_id, gen = k["lauf_id"], k["generation"]
    urteile = _urteile(con, kandidat_id)
    if not urteile:
        raise NachspielFehler(f"K{kandidat_id}: kein aufgezeichnetes Urteil")
    if urteil_nr is None:
        urteil_nr, urteil = urteile[-1]
    else:
        urteil = dict(urteile)[urteil_nr]
    ansage = _ansage_vor(con, kandidat_id, urteil_nr)
    lauf = L._lauf(con, lauf_id)
    werk = L._werk(con, lauf["werk_id"])
    mass = lj(lauf["mass"])
    paket, bereiche = mass["paket"], mass["bereiche"]
    with transaktion(con):
        con.execute(f"UPDATE generationen SET status='{AUSGESCHALTET}' WHERE lauf_id=? AND nummer>=?", (lauf_id, gen))
    basis_gen = L.letzte_angenommene(con, lauf_id)
    ziel = arbeit / "werk"
    r = lazarus.rueckkehr(con, lauf_id, basis_gen["nummer"], Path(werk["pfad"]), ziel)
    if not r["stimmt"]:
        raise NachspielFehler(f"Lazarus Lauf {lauf_id} Gen {basis_gen['nummer']}: Prüfsumme weicht ab "
                              f"({r['pruefsumme_gemessen']} statt {r['pruefsumme_erwartet']})")
    z = con.execute("SELECT ergebnis, nachweis_sha256 FROM vorspann_nachweise WHERE lauf_id=?", (lauf_id,)).fetchone()
    nachweis = dict(lj(z["ergebnis"]), nachweis_sha256=z["nachweis_sha256"])
    verf = verfassung.lesen(con, werk["id"])
    if "masseichung" in nachweis:
        eichung, herkunft = nachweis["masseichung"], "aus dem versiegelten Vorspann-Nachweis"
    else:
        eichung = masseichung.eichen(nachweis["basis"], masseichung.sauberer_bereich(verf))
        herkunft = ("im Nachspiel gebildet: masseichung.eichen(nachweis.basis, sauberer_bereich(verfassung)) — "
                    "der Lauf lag vor dem Einbau, sein Nachweis trägt keine Eichung")
    if not masseichung_an:
        eichung, herkunft = None, "GEGENPROBE: Maßeichung abgeklemmt (Zustand der Läufe 37/38)"
    tausch = L.annahme_tausch(mass, {**nachweis, "masseichung": eichung})
    ref = L._referenzlast(werk["name"], paket)
    import hashlib
    ref_sha = hashlib.sha256(ref.encode()).hexdigest() if ref else None
    kanten = [(x["von"], x["nach"], x["art"]) for x in con.execute("SELECT von, nach, art FROM strassen WHERE werk_id=?", (werk["id"],))]
    vorgelegt = _vorgelegte_immuntests(urteil, kandidat_id)
    with transaktion(con):
        con.execute(f"UPDATE immunsystem SET status='{AUSGESCHALTET}' WHERE werk_id=? AND bereich=? AND status IN ('gefunden','offen')",
                    (werk["id"], k["bereich"]))
        for n in vorgelegt:
            con.execute("UPDATE immunsystem SET status='offen' WHERE werk_id=? AND name=?", (werk["id"], n))
        con.execute("UPDATE kandidaten SET status='erzeugt', grund='', masse=NULL WHERE id=?", (kandidat_id,))
    extra = None
    if partner_id is not None:
        pd = con.execute("SELECT diff FROM kandidaten WHERE id=?", (partner_id,)).fetchone()["diff"]
        d = aegis.kandidat_dateien(ziel, pd)
        if not d:
            raise NachspielFehler(f"Partner K{partner_id}: Diff an der Vorgeneration nicht anwendbar")
        extra = {p: (i if i is not None else "") for p, i in d.items()}
    return {"con": con, "kandidat": kandidat_id, "partner": partner_id, "lauf_id": lauf_id, "generation": gen,
            "werk_id": werk["id"], "werk": ziel, "paket": paket, "bereiche": bereiche,
            "bstrassen": landkarte.bereichs_strassen(kanten, paket), "basis": lj(basis_gen["masse"]),
            "basis_generation": basis_gen["nummer"], "ausgang": L.bestwert_des_laufs(con, lauf_id, bereiche),
            "ref": ref, "ref_sha256": ref_sha,
            "ref_wie_im_lauf": ref_sha == ((nachweis.get("quellen") or {}).get("referenzlast") or {}).get("sha256"),
            "tausch": tausch, "eichung": eichung, "eichung_herkunft": herkunft, "extra": extra,
            "urteil_nr": urteil_nr, "urteil_aufgezeichnet": urteil, "ansage_aufgezeichnet": ansage,
            "immun_vorgelegt": vorgelegt, "lazarus": {k2: r[k2] for k2 in ("tag", "pruefsumme_erwartet", "pruefsumme_gemessen", "stimmt", "dateien")}}


def _kernmass_beleg(masse: dict, eichung: dict | None) -> dict:
    """Kernmaß der vom Annahmepfad gespeicherten Messung, roh und geeicht, mit den nicht gezählten Regeln."""
    still = set((eichung or {}).get("stillgelegt") or [])
    zeilen, roh, geeicht, im_mass = {}, 0, 0, []
    for b, m in (masse.get("bereiche") or {}).items():
        gezaehlt = [x.get("test") for x in m.get("sicherheit_befunde") or []]
        ruht = [x.get("test") for x in m.get("sicherheit_stillgelegt") or []]
        p_roh = m.get("sicherheit_punkte_roh", m.get("sicherheit_punkte"))
        zeilen[b] = {"punkte_gezaehlt": m.get("sicherheit_punkte"), "punkte_roh": p_roh,
                     "regeln_gezaehlt": sorted(set(gezaehlt)), "regeln_stillgelegt": sorted(set(ruht))}
        im_mass += [r for r in gezaehlt if r in still]
        roh += -m["tests_fehlgeschlagen"] - p_roh - m["tote_funktionen"]
        geeicht += -m["tests_fehlgeschlagen"] - m["sicherheit_punkte"] - m["tote_funktionen"]
    return {"kernmass_gespeichert": messgeraet.kernmass_f2(masse), "kernmass_roh": roh, "kernmass_geeicht": geeicht,
            "stillgelegte_regel_im_mass": sorted(set(im_mass)), "bereiche": zeilen}


def spielen(fall: dict, *, verhaltensvergleich_an: bool = True) -> dict:
    """Ruft `aegis.pruefen` — die Funktion, die ein Lauf zur Annahme ruft — mit dem hergestellten Zustand."""
    con = fall["con"]
    kein_angriff = bool(fall["ansage_aufgezeichnet"]) and fall["ansage_aufgezeichnet"].get("behauptung") is None \
        and "KEIN ANGRIFF" in str(fall["ansage_aufgezeichnet"].get("grund"))
    g = AufgezeichneteGrenze(kein_angriff)
    aegis.zaehlkontext_setzen(con, fall["lauf_id"])
    nz0 = con.execute("SELECT COALESCE(MAX(id),0) FROM neutralzaehler").fetchone()[0] if con.execute(
        "SELECT name FROM sqlite_master WHERE name='neutralzaehler'").fetchone() else 0
    abgeklemmt = None
    if not verhaltensvergleich_an:
        # GEGENPROBE: der Zustand von Lauf 38 — das Organ existiert, der Annahmepfad ruft es nicht.
        abgeklemmt = aegis.verhaltensvergleich.pruefen
        aegis.verhaltensvergleich.pruefen = lambda *a, **k: {"ausgefuehrt": False, "geurteilt": False, "tragfaehig": True,
                                                             "grund_art": "gegenprobe_abgeklemmt",
                                                             "grund": "GEGENPROBE: Verhaltensvergleich abgeklemmt"}
    try:
        with _grenze(g), kammer.zaehlung() as kammerlaeufe:
            u = aegis.pruefen(con, fall["lauf_id"], fall["werk_id"], fall["kandidat"], fall["werk"], fall["paket"],
                              fall["bereiche"], fall["bstrassen"], fall["basis"], fall["ausgang"], fall["ref"],
                              fall["tausch"], extra_code=fall["extra"])
    finally:
        if abgeklemmt is not None:
            aegis.verhaltensvergleich.pruefen = abgeklemmt
        aegis.zaehlkontext_setzen(None, None)
    kz = con.execute("SELECT status, grund, masse FROM kandidaten WHERE id=?", (fall["kandidat"],)).fetchone()
    masse = lj(kz["masse"]) or {}
    bp = masse.get("_basis_paar") or {}
    laufzeit = {b: {"bestwert": ((fall["ausgang"].get("bereiche") or {}).get(b) or {}).get("laufzeit_ms"),
                    "vorgeneration": ((bp.get("bereiche") or {}).get(b) or {}).get("laufzeit_ms"),
                    "kandidat": ((masse.get("bereiche") or {}).get(b) or {}).get("laufzeit_ms")}
                for b in fall["bereiche"]}
    zaehler = [dict(z) for z in con.execute("SELECT organ, art, grund, einzelheit FROM neutralzaehler WHERE id>?", (nz0,))]
    beleg = {"kandidat": fall["kandidat"], "partner": fall["partner"], "lauf": fall["lauf_id"], "generation": fall["generation"],
             "vorgeneration": fall["basis_generation"], "lazarus": fall["lazarus"],
             "verhaltensvergleich_an": verhaltensvergleich_an, "masseichung_an": fall["eichung"] is not None,
             "eichung_herkunft": fall["eichung_herkunft"],
             "stillgelegt": (fall["eichung"] or {}).get("stillgelegt") or [],
             "status": u["status"], "grund": u["grund"],
             "status_aufgezeichnet": fall["urteil_aufgezeichnet"].get("status"),
             "grund_aufgezeichnet": fall["urteil_aufgezeichnet"].get("grund"),
             "mass": {k2: (u.get("mass") or {}).get(k2) for k2 in ("ok", "kern_basis", "kern_kandidat", "zuwachs",
                                                                  "pareto_besser", "pareto_schlechter", "grenzen_gerissen",
                                                                  "laufzeit_gewinne")},
             "verhalten": u.get("verhalten"),
             "laufzeit_ms": laufzeit,
             "kernmass_kandidat": _kernmass_beleg(masse, fall["eichung"]) if masse.get("bereiche") else None,
             "kernmass_vorgeneration": _kernmass_beleg(masse.get("_basis_paar") or {}, fall["eichung"])
             if (masse.get("_basis_paar") or {}).get("bereiche") else None,
             "neutralzaehler": zaehler, "anbietergrenze": g.anfragen, "anbietergrenze_kennung": KENNUNG,
             "ansage_aufgezeichnet": fall["ansage_aufgezeichnet"], "urteil_nr_aufgezeichnet": fall["urteil_nr"],
             "immun_vorgelegt": fall["immun_vorgelegt"], "tests_offen": u.get("tests_offen"),
             "referenzlast_sha256": fall["ref_sha256"], "referenzlast_wie_im_lauf": fall["ref_wie_im_lauf"],
             "kammerlaeufe": len(kammerlaeufe),
             "modellaufrufe_echt": 0}
    return json.loads(json.dumps(beleg, ensure_ascii=False, default=str))
