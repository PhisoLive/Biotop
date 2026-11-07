"""Ablauf eines Laufs (Abschnitt 4) — Phase 1: Aufnahme → Landkarte → Maß
(eingefroren) → Generationen (Schwarm → Ankläger → Zusammensetzen →
Generalprobe → Pareto → Schnappschuss → Freigabe durch Philipp).

Die Messung entscheidet; kein Modell beurteilt einen Vorschlag.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from .kern import kasse, messgeraet, protokoll
from .kern.datenbank import j, lj, transaktion
from .organe import aegis, aufnahme, entropie, gedaechtnis, genesis, jury, kammer, landkarte, lazarus, mentor, nischen, verfassung, vertraege, vorspann

REFERENZLAST = Path(__file__).resolve().parent / "kern/referenzlast"


class LaufFehler(RuntimeError):
    pass


def _lauf(con, lauf_id) -> dict:
    z = con.execute("SELECT * FROM laeufe WHERE id=?", (lauf_id,)).fetchone()
    if not z:
        raise LaufFehler(f"Lauf {lauf_id} unbekannt")
    return dict(z)


def _werk(con, werk_id) -> dict:
    z = con.execute("SELECT * FROM werke WHERE id=?", (werk_id,)).fetchone()
    return dict(z)


def _referenzlast(name: str, paket: str | None = None) -> str | None:
    """Referenzlast je Werk (Kern). Suche: Werkname, dann Paketname (ein Werk unter neuem Namen misst dieselbe Last)."""
    for n in (name, paket):
        if n and (REFERENZLAST / f"{n}.py").exists():
            return (REFERENZLAST / f"{n}.py").read_text()
    return None


def anlegen(con: sqlite3.Connection, budget_eur: float) -> int:
    """Legt einen Lauf mit Budget an (vor der Aufnahme, weil schon die Aufnahme Modellaufrufe macht)."""
    with transaktion(con):
        cur = con.execute("INSERT INTO laeufe(budget_eur, status, begonnen_am) VALUES (?,?,?)",
                          (budget_eur, "angelegt", protokoll.jetzt()))
    lauf_id = cur.lastrowid
    protokoll.schreiben(con, "lauf.angelegt", lauf_id=lauf_id, budget_eur=budget_eur)
    return lauf_id


def einlegen(con: sqlite3.Connection, lauf_id: int, name: str, quelle: str) -> dict:
    ok, meld = kammer.bereit()
    if not ok:
        raise LaufFehler(meld)
    try:
        bericht = aufnahme.aufnehmen(con, name, quelle, lauf_id)
    except aufnahme.MessgeraetFehlt as e:
        with transaktion(con):
            con.execute("UPDATE laeufe SET status='gestoppt', grund=?, beendet_am=? WHERE id=?", (str(e), protokoll.jetzt(), lauf_id))
        protokoll.schreiben(con, "lauf.gestoppt", lauf_id=lauf_id, grund=str(e), generationen=0)
        raise LaufFehler(f"Messgerät fehlt — Lauf {lauf_id} gestoppt, 0 Generationen gestartet. {e}") from e
    with transaktion(con):
        con.execute("UPDATE laeufe SET werk_id=?, status='aufgenommen' WHERE id=?", (bericht["werk_id"], lauf_id))
    return bericht


def kartieren(con: sqlite3.Connection, lauf_id: int) -> dict:
    lauf = _lauf(con, lauf_id)
    werk = _werk(con, lauf["werk_id"])
    paket = lj(werk["bericht"])["paket"]
    z = landkarte.bauen(con, werk["id"], lauf_id, Path(werk["pfad"]), paket)
    with transaktion(con):
        con.execute("UPDATE laeufe SET status='kartiert' WHERE id=?", (lauf_id,))
    return z


def mass_einfrieren(con: sqlite3.Connection, lauf_id: int, bestaetigt_von: str) -> dict:
    """Misst Generation 0 (Ausgangszustand), friert das Maß ein, legt Schnappschuss 0 an."""
    lauf = _lauf(con, lauf_id)
    nachweis = _vorspann_verlangen(con, lauf_id, "mass")
    werk = _werk(con, lauf["werk_id"])
    b = lj(werk["bericht"])
    paket = b["paket"]
    bereiche = landkarte.bereiche_finden(Path(werk["pfad"]), paket)
    ref = _referenzlast(werk["name"], paket)
    if ref is None:
        raise LaufFehler(f"Referenzlast für {werk['name']}/{paket} fehlt im Kern — ohne sie kein Grenzmaß Laufzeit (laut scheitern)")
    mess = messgeraet.messen(Path(werk["pfad"]), bereiche, paket, ref)
    if not mess["gueltig"]:
        raise LaufFehler(f"Ausgangsmessung ungültig: {mess['grund']}")
    verf = verfassung.lesen(con, werk["id"])
    if verf is None:
        raise LaufFehler("Verfassung des Werks fehlt (3.3 F2) — vor dem Maß einlegen: biotop verfassung <lauf> <datei.md> <regeln.json>")
    tausch = (verf.get("regeln") or {}).get("tausch") or {}
    mess["kernmass_f2"] = messgeraet.kernmass_f2(mess)
    mass = {"fassung": 2, "vorspann_sha256": nachweis["nachweis_sha256"],
            "kernmass": "je Bereich: −tests_fehlgeschlagen − sicherheit_punkte(10·HIGH+3·MEDIUM+1·LOW) − tote_funktionen; Höchstwert 0; bestandene Tests zählen nicht; paarweise Messung mit dem Testbestand des Kandidaten",
            "pareto": list(messgeraet.PARETO_F2) + ["baut"],
            "grenzen": {"laufzeit_faktor": tausch.get("laufzeit_faktor", 2.0), "laufzeit_faktor_bei_sicherheitsgewinn": tausch.get("laufzeit_faktor_bei_sicherheitsgewinn", tausch.get("laufzeit_faktor", 2.0)),
                        "sonst_faktor": tausch.get("sonst_faktor", 1.25), "groesste_funktion_absolut": 60, "rauschtoleranz_ohne_kernmassgewinn": messgeraet.RAUSCH_F4, "bezug": "Bestwert des Laufs (F4: beste angenommene Generation je Maß, einschließlich Generation 0)"},
            "tausch_quelle": verf["quelle"], "bereiche": bereiche, "paket": paket, "referenzlast": f"{werk['name']}.py",
            "nischen": list(__import__("biotop.organe.nischen", fromlist=["NISCHEN"]).NISCHEN), "groesste_funktion_absolut": 60,
            "pareto_je_test": True, "norm_regel": "3.7 F4 (alle neuen Tests, expliziter Verweis)", "bandit_kein_vorschlag": "neutral (3.6 F4)", "archivierung_offener_funde": "nach 5 Generationen (3.10 F4)", "immunisierung": "3.10 F3 (nur bestandene, Doppelungen gekennzeichnet)",
            "bestaetigt_von": bestaetigt_von, "eingefroren_am": protokoll.jetzt()}
    _vorspann_verlangen(con, lauf_id, "mass")  # auch nach der langen Messung unverändert
    with transaktion(con):
        try:
            mass_sha256 = vorspann.mass_binden(con, lauf_id, mass)
        except vorspann.VorspannFehler as e:
            raise LaufFehler(str(e)) from e
        con.execute("UPDATE laeufe SET mass=?, status='bereit' WHERE id=?", (j(mass), lauf_id))
        con.execute("INSERT INTO generationen(lauf_id, nummer, status, masse, erstellt_am, grund) VALUES (?,?,?,?,?,?)",
                    (lauf_id, 0, "angenommen", j(mess), protokoll.jetzt(), "Ausgangszustand"))
    s = lazarus.schnappschuss(con, lauf_id, 0, Path(werk["pfad"]), mess)
    with transaktion(con):
        con.execute("UPDATE generationen SET tag=?, pruefsumme=? WHERE lauf_id=? AND nummer=0", (s["tag"], s["pruefsumme"], lauf_id))
    protokoll.schreiben(con, "mass.eingefroren", lauf_id=lauf_id, mass_sha256=mass_sha256, vorspann_sha256=nachweis["nachweis_sha256"], fassung=2, kernmass_f2=mess["kernmass_f2"], kernmass_f1=mess["kernmass"], grenzen=mass["grenzen"], bestaetigt_von=bestaetigt_von)
    return {"mass": mass, "messung": mess, "schnappschuss": s}


def bestwert_des_laufs(con, lauf_id, bereiche) -> dict:
    """F4 3.5: Bezug der Grenzmaße = je Maß und Bereich der beste Wert aller angenommenen Generationen einschließlich
    Generation 0. Gekennzeichnet mit bezug='bestwert' (grenzen_f2 schreibt den Bezug in die Begründung)."""
    ms = [lj(z["masse"]) for z in con.execute("SELECT masse FROM generationen WHERE lauf_id=? AND status='angenommen' ORDER BY nummer", (lauf_id,))]
    b = messgeraet.bestwerte(ms, bereiche)
    b["bezug"] = "bestwert"
    b["_aus_generationen"] = [z["nummer"] for z in con.execute("SELECT nummer FROM generationen WHERE lauf_id=? AND status='angenommen' ORDER BY nummer", (lauf_id,))]
    return b


def letzte_angenommene(con, lauf_id) -> dict:
    z = con.execute("SELECT * FROM generationen WHERE lauf_id=? AND status='angenommen' ORDER BY nummer DESC LIMIT 1", (lauf_id,)).fetchone()
    return dict(z)


def _vorspann_verlangen(con, lauf_id, phase):
    try:
        return vorspann.verlangen(con, lauf_id, phase)
    except vorspann.VorspannFehler as e:
        raise LaufFehler(str(e)) from e


def generation(con: sqlite3.Connection, lauf_id: int, einschleusen: list[dict] | None = None) -> dict:
    """Eine Generation: je Bereich Schwarm → Ankläger; Zusammensetzen der Überlebenden;
    Generalprobe; Pareto gegen die letzte angenommene Generation; Schnappschuss.
    Rückgabe: Ergebnis der Generation (Status 'vorgelegt' oder 'abgelehnt').
    `einschleusen` (Proben, Tor-Zeilen): Liste {bereich, diff, begruendung, vertraege, probe}. Dann erzeugt kein Schwarm;
    die eingeschleusten Kandidaten (nische='probe', Modell 'hermes/probe-…') durchlaufen denselben Ankläger, dieselbe
    Verhandlung und dieselbe Generalprobe wie Schwarm-Kandidaten. Protokolliert als probe.eingeschleust; Bandit bucht sie nicht."""
    lauf = _lauf(con, lauf_id)
    nachweis = _vorspann_verlangen(con, lauf_id, "generation")
    if lauf["status"] not in ("bereit", "laeuft"):
        raise LaufFehler(f"Lauf {lauf_id} ist im Zustand {lauf['status']}, nicht bereit")
    offen = con.execute("SELECT nummer FROM generationen WHERE lauf_id=? AND status='vorgelegt'", (lauf_id,)).fetchone()
    if offen:
        raise LaufFehler(f"Generation {offen['nummer']} wartet auf Freigabe durch Philipp")
    werk = _werk(con, lauf["werk_id"])
    mass = lj(lauf["mass"])
    paket, bereiche = mass["paket"], mass["bereiche"]
    pfad = Path(werk["pfad"])
    ref = _referenzlast(werk["name"], paket)
    basis_gen = letzte_angenommene(con, lauf_id)
    basis = lj(basis_gen["masse"])
    nummer = con.execute("SELECT COALESCE(MAX(nummer),0)+1 FROM generationen WHERE lauf_id=?", (lauf_id,)).fetchone()[0]
    kanten = [(z["von"], z["nach"], z["art"]) for z in con.execute("SELECT von, nach, art FROM strassen WHERE werk_id=?", (werk["id"],))]
    bstrassen = landkarte.bereichs_strassen(kanten, paket)
    # Kassen-Vorprüfung auf Generationsebene: Kostenvoranschlag = teuerste bisherige Generation dieses Laufs.
    # Reicht das Budget dafür nicht, wird die Generation gar nicht erst begonnen (kein einziger Modellaufruf).
    rausch = nachweis["rauschen"]
    gesperrt = rausch["gesperrt"]
    for b in gesperrt:
        protokoll.schreiben(con, "generation.bereich_uebersprungen", lauf_id=lauf_id, generation=nummer,
                            bereich=b, toleranz=rausch["bereiche"][b]["toleranz"],
                            grund=rausch["bereiche"][b].get("meldung"), nachweis_sha256=nachweis["nachweis_sha256"])
    if not set(bereiche) - set(gesperrt):
        raise LaufFehler("Vorspann: alle Bereiche gesperrt — kein Kandidat wird erzeugt")
    kasse.generation_vorpruefung(con, lauf_id, nummer)
    with transaktion(con):
        con.execute("UPDATE laeufe SET status='laeuft' WHERE id=?", (lauf_id,))
        con.execute("INSERT INTO generationen(lauf_id, nummer, status, erstellt_am) VALUES (?,?,?,?)", (lauf_id, nummer, "laeuft", protokoll.jetzt()))
    protokoll.schreiben(con, "generation.begonnen", lauf_id=lauf_id, nummer=nummer, basis=basis_gen["nummer"], kasse=kasse.stand(con, lauf_id))
    ausgang = bestwert_des_laufs(con, lauf_id, bereiche)  # F4: Grenzmaße gegen den Bestwert aller angenommenen Generationen
    tausch = dict(mass.get("grenzen") or {})
    tausch.update(_rauschtoleranz=dict(rausch["toleranz"]), _gesperrte_bereiche=list(gesperrt),
                  _rauschbelege=rausch["bereiche"], _vorspann_sha256=nachweis["nachweis_sha256"])
    try:
        return _generation_koerper(con, lauf_id, nummer, werk, mass, paket, bereiche, pfad, ref, basis, bstrassen, ausgang, tausch, einschleusen)
    except kasse.BudgetErschoepft:
        with transaktion(con):
            con.execute("UPDATE generationen SET status='abgebrochen', grund='Budget erschöpft während der Generation' WHERE lauf_id=? AND nummer=?", (lauf_id, nummer))
        raise


def _generation_koerper(con, lauf_id, nummer, werk, mass, paket, bereiche, pfad, ref, basis, bstrassen, ausgang, tausch, einschleusen=None):

    def abschluss(status, grund, mess=None, kandidaten=None):
        with transaktion(con):
            con.execute("UPDATE generationen SET status=?, grund=?, masse=?, kandidaten=? WHERE lauf_id=? AND nummer=?",
                        (status, grund, j(mess) if mess else None, j(kandidaten or {}), lauf_id, nummer))
            if status == "abgelehnt":
                con.execute("UPDATE laeufe SET status='bereit' WHERE id=?", (lauf_id,))
        protokoll.schreiben(con, "generation.ergebnis", lauf_id=lauf_id, nummer=nummer, status=status, grund=grund[:400],
                            kernmass_f2=messgeraet.kernmass_f2(mess) if mess else None, kernmass_f1=mess["kernmass"] if mess else None, kasse=kasse.stand(con, lauf_id))
        r = {"nummer": nummer, "status": status, "grund": grund, "messung": mess, "kandidaten": kandidaten}
        # 3.11 Entropie: je Generation zwei Zahlen; Sättigung beendet den Lauf (bei 'vorgelegt' erst nach der Freigabe, s. freigabe())
        if status == "abgelehnt":
            r["entropie"] = entropie.messen(con, lauf_id, nummer)
            s_ = entropie.pruefen_und_beenden(con, lauf_id)
            if s_:
                r["saettigung"] = s_
        return r

    # 1. Schwarm je Bereich und Nische (Phase 2: vier Nischen, je zwei per Bandit gewählte Hersteller), 2. Ankläger je Kandidat
    aktive_nischen = list(nischen.NISCHEN) if mass.get("nischen") is None else mass["nischen"]
    urteile: dict[str, list[dict]] = {}
    # Eingeschleuste Proben (Tor-Zeilen): statt Schwarm die von Hermes gestellten Kandidaten — gekennzeichnet, Bandit-neutral
    probe_ids: dict[str, list[int]] = {}
    for e in (einschleusen or []):
        if e["bereich"] in tausch.get("_gesperrte_bereiche", []):
            continue
        with transaktion(con):
            cur = con.execute("INSERT INTO kandidaten(lauf_id, generation, bereich, nische, anbieter, modell, diff, begruendung, status, grund, erstellt_am, vertraege, ist_probe) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,1)",
                              (lauf_id, nummer, e["bereich"], "probe", "hermes", "hermes/probe-" + e.get("probe", "probe"), e["diff"], e.get("begruendung", ""), "erzeugt", "", protokoll.jetzt(), e.get("vertraege", "keine")))
        probe_ids.setdefault(e["bereich"], []).append(cur.lastrowid)
        protokoll.schreiben(con, "probe.eingeschleust", lauf_id=lauf_id, generation=nummer, kandidat=cur.lastrowid, probe=e.get("probe"), bereich=e["bereich"], vertraege=e.get("vertraege"))
    for b in bereiche:
        urteile[b] = []
        if b in tausch.get("_gesperrte_bereiche", []):
            continue
        befunde = [{k: v for k, v in f.items() if k in ("test", "schwere", "zeile", "text")} for f in basis["bereiche"][b].get("sicherheit_befunde", [])]
        vt_text = vertraege.text_fuer_bereich(con, werk["id"], b)
        for nische in (["probe"] if einschleusen is not None else aktive_nischen):
            if nische == "probe":
                ids = probe_ids.get(b, [])
            else:
                ids = genesis.erzeugen(con, lauf_id, werk["id"], nummer, pfad, paket, b, messgeraet.bereich_masse(basis, b), nische=nische,
                                       befunde=befunde, referenzlast=ref, vertraege_text=vt_text)
            for kid in ids:
                # 3.12 Projektgedächtnis: Wiederholung eines gescheiterten Wegs → ohne Kammerlauf verworfen (mechanisch, protokolliert)
                kz0 = con.execute("SELECT status, diff FROM kandidaten WHERE id=?", (kid,)).fetchone()
                if kz0["status"] == "erzeugt" and nische != "probe":
                    dn = aegis.kandidat_dateien(pfad, kz0["diff"])
                    w = gedaechtnis.wiederholung(con, werk["id"], b, pfad, kz0["diff"], {p: (i or "") for p, i in (dn or {}).items()} if dn else None, lauf_id)
                    if w:
                        with transaktion(con):
                            con.execute("UPDATE kandidaten SET status='abgelehnt', grund=? WHERE id=?",
                                        (f"Wiederholung eines gescheiterten Wegs (Projektgedächtnis): Lauf {w['lauf_id']} Gen {w['generation']} K{w['kandidat_id']}, Ähnlichkeit {w['aehnlichkeit']}, Funktionen {w['gemeinsame_funktionen']}; damals: {w['grund_damals'][:120]}", kid))
                        protokoll.schreiben(con, "gedaechtnis.wiederholung", lauf_id=lauf_id, generation=nummer, kandidat=kid, bereich=b, weg={k: v for k, v in w.items()})
                u = aegis.pruefen(con, lauf_id, werk["id"], kid, pfad, paket, bereiche, bstrassen, basis, ausgang, ref, tausch)
                # 3.8 Schritt 2 — Verhandlung: (a) Vertrag verletzt UND unter VERTRÄGE benannt → Nachbar fragen;
                # (b) F4/Anhang A Satz 4: eine geänderte Vertragsdatei geht NIE einseitig ins Werk — auch wenn kein Vertragstest
                # fällt, wird der Nachbar gefragt und das Paar gemeinsam geprüft (Lücke bis Lauf 15: einseitige Vertragsänderung).
                # 3.8 Schritt 2 gilt für die BENENNUNG: Wer einen Vertrag ändern will, bekommt den Nachbarn gefragt — auch wenn seine
                # Seite allein nicht besteht (eigene Tests fallen, weil die Nachbarseite fehlt) oder wenn kein Vertragstest fällt
                # (geänderte Vertragsdatei, Anhang A Satz 4). Nicht verhandelt wird bei Diff-/Verfassungsfehlern und unbenannter Vertragsdatei.
                benannt = u.get("vertraege_benannt", "").strip().lower() not in ("", "keine")
                nicht_verhandelbar = u["grund"].startswith(("Diff nicht anwendbar", "Diff ändert nichts", "Verfassung verletzt", "ändert Vertragsdatei", "Kammer"))
                if benannt and not nicht_verhandelbar and (u["status"] == "abgelehnt" or (u["status"] == "ueberlebt" and u.get("vertrag_dateien"))):
                    u = _verhandeln(con, lauf_id, werk, nummer, pfad, paket, bereiche, bstrassen, basis, ausgang, ref, tausch, b, kid, u)
                kz = con.execute("SELECT modell, status FROM kandidaten WHERE id=?", (kid,)).fetchone()
                hersteller = (kz["modell"] or "/").split("/")[0]
                # Bandit (3.6 F4): „KEIN VORSCHLAG" (status leer) ist neutral — keine Wahl, kein Misserfolg; Proben zählen nicht
                if nische != "probe" and kz["status"] != "leer":
                    nischen.buchen(con, lauf_id, nische, hersteller, u["status"] == "ueberlebt")
                if u["status"] == "ueberlebt":
                    kd = con.execute("SELECT diff, begruendung FROM kandidaten WHERE id=?", (kid,)).fetchone()
                    lg = 0.0
                    for g in (u.get("mass") or {}).get("laufzeit_gewinne", []):
                        try: lg = max(lg, float(g.split("−")[1].split("%")[0]))
                        except Exception: pass
                    nischen.elite_setzen(con, lauf_id, nische, b, kid, nummer, (u.get("mass") or {}).get("zuwachs", 0), lg, kd["diff"], kd["begruendung"])
                urteile[b].append(u)
                # 3.12: Gedächtnisse schreiben — gescheiterter Weg ins Projektgedächtnis, Ergebnis ins Artgedächtnis
                if u["status"] == "abgelehnt":
                    gedaechtnis.projekt_merken(con, werk["id"], lauf_id, kid, pfad)
                if u["status"] in ("abgelehnt", "ueberlebt") and nische != "probe":
                    gedaechtnis.art_merken(con, werk["id"], lauf_id, kid, "ueberlebt" if u["status"] == "ueberlebt" else "abgelehnt", bereichsrolle=b)

    # 3. Je Bereich der beste Überlebende (Messung entscheidet: größter Kernmaß-Zuwachs, dann Laufzeitgewinn, dann kleinster Diff)
    gewaehlt: dict[str, int] = {}
    for b, us in urteile.items():
        ueberlebende = [u for u in us if u["status"] == "ueberlebt"]
        if not ueberlebende:
            continue
        def wert(u):
            k = con.execute("SELECT masse, diff FROM kandidaten WHERE id=?", (u["kandidat"],)).fetchone()
            return ((u.get("mass") or {}).get("zuwachs", 0), len((u.get("mass") or {}).get("laufzeit_gewinne", [])), -len(k["diff"]))
        ueberlebende.sort(key=wert, reverse=True)
        best = ueberlebende[0]
        # 3.5 weiche Maße: Gleichstand in allen harten Maßen zwischen den zwei Besten → Jury (nur bei Einstimmigkeit)
        if len(ueberlebende) >= 2 and jury.gleichstand(ueberlebende[0], ueberlebende[1]) and wert(ueberlebende[0])[:2] == wert(ueberlebende[1])[:2]:
            ju = jury.entscheiden(con, lauf_id, nummer, b, ueberlebende[0]["kandidat"], ueberlebende[1]["kandidat"])
            if ju["einstimmig"] and ju["gewinner"]:
                best = next(u for u in ueberlebende if u["kandidat"] == ju["gewinner"])
        gewaehlt[b] = best["kandidat"]
    zusammenfassung = {b: [{"kandidat": u["kandidat"], "status": u["status"], "grund": u["grund"][:200], "nische": con.execute("SELECT nische FROM kandidaten WHERE id=?", (u["kandidat"],)).fetchone()[0]} for u in us] for b, us in urteile.items()}
    zusammenfassung["_gewaehlt"] = gewaehlt
    zusammenfassung["_bandit"] = nischen.gewichte(con, lauf_id)
    if not gewaehlt:
        return abschluss("abgelehnt", "kein Kandidat hat den Ankläger überlebt (0 von %d)" % sum(len(u) for u in urteile.values()), None, zusammenfassung)

    # 4. Zusammensetzen + Immuntests der gewählten Kandidaten
    dateien: dict[str, str] = {}
    for b, kid in gewaehlt.items():
        km = lj(con.execute("SELECT masse FROM kandidaten WHERE id=?", (kid,)).fetchone()["masse"]) or {}
        # Der Ankläger hat den endgültigen Dateisatz des Kandidaten festgelegt (Code + nur die Tests, die am
        # Ausgangszustand fehlschlugen + bestandene Immuntests). Nichts anderes kommt ins Werk.
        for p, inhalt in (km.get("_dateien") or {}).items():
            dateien[p] = inhalt

    # 5. Generalprobe (F2): Vorgeneration und Gesamtkandidat paarweise mit dem Testbestand des Gesamtkandidaten
    testbestand = {p: i for p, i in dateien.items() if p.startswith("tests/")}
    basis_paar = messgeraet.messen(pfad, bereiche, paket, ref, dateien=testbestand)
    mess = messgeraet.messen(pfad, bereiche, paket, ref, dateien=dateien)
    if not basis_paar["gueltig"] or not mess["gueltig"] or not mess["werk"]["baut"]:
        return abschluss("abgelehnt", "Generalprobe: " + (mess.get("grund") or basis_paar.get("grund") or mess["werk"]["bau_fehler"][-300:]), mess, zusammenfassung)
    mess["kernmass_f2"] = messgeraet.kernmass_f2(mess)
    mess["_basis_paar"] = {"kernmass_f2": messgeraet.kernmass_f2(basis_paar), "bereiche": {b: messgeraet.bereich_masse(basis_paar, b) for b in bereiche}}
    mess["_testbestand"] = sorted(testbestand)

    # 6. Pareto + Grenzen + Zuwachs (F2)
    wirkungskreis = set()
    for b, kid in gewaehlt.items():
        kz = con.execute("SELECT wirkungskreis FROM kandidaten WHERE id=?", (kid,)).fetchone()
        wirkungskreis.update(lj(kz["wirkungskreis"]) or landkarte.wirkungskreis(b, bstrassen))
    wirkungskreis = sorted(wirkungskreis)
    u = messgeraet.urteil_f2(basis_paar, mess, ausgang, bereiche, wirkungskreis, tausch)
    # Nischenmaß auf Werkebene: Gesamtkandidat mit reinem Laufzeitgewinn (Kernmaß gleich) ist zulässig
    if not u["ok"] and u["grund"].startswith("Kernmaß unverändert"):
        gew = [f"{b}: {basis_paar['bereiche'][b]['laufzeit_ms']} → {mess['bereiche'][b]['laufzeit_ms']}" for b in wirkungskreis
               if b not in tausch.get('_gesperrte_bereiche', []) and basis_paar["bereiche"][b].get("laufzeit_ms") and mess["bereiche"][b].get("laufzeit_ms") and mess["bereiche"][b]["laufzeit_ms"] <= basis_paar["bereiche"][b]["laufzeit_ms"] * 0.85]
        if gew:
            u = {**u, "ok": True, "grund": "Laufzeit gesunken (Nischenmaß), Kernmaß unverändert: " + "; ".join(gew), "laufzeit_gewinne": gew}
    vv = vertraege.verletzt(set(basis_paar["werk"]["tests_fehlgeschlagen_liste"]), set(mess["werk"]["tests_fehlgeschlagen_liste"]))
    if vv:
        u = {**u, "ok": False, "grund": "Generalprobe: Vertrag verletzt " + ", ".join(vv)}
    mess["_urteil_f2"] = u
    zusammenfassung["_generalprobe"] = u
    if not u["ok"]:
        for b, kid in gewaehlt.items():
            with transaktion(con):
                con.execute("UPDATE kandidaten SET status='abgelehnt', grund=? WHERE id=?", ("Generalprobe: " + u["grund"], kid))
        return abschluss("abgelehnt", "Generalprobe: " + u["grund"], mess, zusammenfassung)
    gestiegen = u["pareto_besser"] or u.get("laufzeit_gewinne") or []

    # 7. In das Werk schreiben + Schnappschuss (die Freigabe entscheidet, ob es bleibt)
    for p, inhalt in dateien.items():
        f = pfad / p
        f.parent.mkdir(parents=True, exist_ok=True)
        if inhalt == "" and f.exists() and not p.endswith(".py"):
            f.unlink()
        else:
            f.write_text(inhalt)
    with transaktion(con):
        for b, kid in gewaehlt.items():
            con.execute("UPDATE kandidaten SET status='angenommen' WHERE id=?", (kid,))
    for b, kid in gewaehlt.items():
        gedaechtnis.art_merken(con, werk["id"], lauf_id, kid, "angenommen", bereichsrolle=b)
    with transaktion(con):
        for p in dateien:
            if "_immun_" in p:
                con.execute("UPDATE immunsystem SET status='im_werk' WHERE werk_id=? AND name=?", (werk["id"], p.split("_immun_")[1][:-3]))
        con.execute("UPDATE immunsystem SET status='offen' WHERE werk_id=? AND status='gefunden'", (werk["id"],))
    # 3.10 F5: Offene Funde, die nach 5 GENERATIONEN kein Kandidat besteht, werden archiviert (bleiben in der DB,
    # werden nicht mehr vorgelegt, kosten keinen Kammerlauf mehr). Bezug sind GENERATIONEN, nicht angenommene
    # Generationen — sonst tritt der Fall an einem gesättigten Werk nie ein (gemessen Phase 3: 0 Archivierungen
    # in 5 Läufen, weil Lauf 20 nur 1 angenommene Generation hatte).
    archiviert = []
    for z in con.execute("SELECT id, name, bereich, generation, lauf_id FROM immunsystem WHERE werk_id=? AND status IN ('offen','offen_norm')", (werk["id"],)):
        seit = con.execute("SELECT COUNT(*) FROM generationen WHERE lauf_id=? AND nummer>? AND nummer<=? AND status!='abgebrochen'",
                           (lauf_id, z["generation"] if z["lauf_id"] == lauf_id else -1, nummer)).fetchone()[0]
        if seit >= 5:
            archiviert.append(f"{z['bereich']}/{z['name']} (Fund Gen {z['generation']}, Lauf {z['lauf_id']}; {seit} Generationen ohne Behebung)")
            with transaktion(con):
                con.execute("UPDATE immunsystem SET status='archiviert', ursprung=ursprung || ? WHERE id=?",
                            (f" | archiviert nach {seit} Generationen (3.10 F5), Lauf {lauf_id} Gen {nummer}", z["id"]))
    if archiviert:
        protokoll.schreiben(con, "immun.archiviert", lauf_id=lauf_id, generation=nummer, anzahl=len(archiviert), funde=archiviert,
                            regel="F5 3.10: Bezug sind Generationen, nicht angenommene Generationen")
    s = lazarus.schnappschuss(con, lauf_id, nummer, pfad, mess)
    with transaktion(con):
        con.execute("UPDATE generationen SET tag=?, pruefsumme=? WHERE lauf_id=? AND nummer=?", (s["tag"], s["pruefsumme"], lauf_id, nummer))
    r = abschluss("vorgelegt", "gestiegen: " + "; ".join(map(str, gestiegen)), mess, zusammenfassung)
    r["schnappschuss"] = s
    r["gestiegen"] = gestiegen
    return r


def abbrechen(con: sqlite3.Connection, lauf_id: int, grund: str, von: str, art: str = "satz2") -> dict:
    """Einen Lauf sofort beenden — Pflicht, keine Freigabe (Fassung 5, Abschnitt 5).

    **Abbrüche sind nie gesperrt.** Ein Abbruch nach Verfassungssatz 2 (Messgerätänderung) oder wegen des Budgets
    ist eine Pflicht, kein Ermessen; das Freigabe-Gate darf ihn nicht blockieren. Er ist immer erlaubt und wird
    immer protokolliert.

    Grund (Phase 3, gemessen): Es gab keinen Abbruch-Befehl. Hermes musste den als falsch erkannten Lauf 16 mit
    `pkill` und Ad-hoc-SQL stoppen — Muster, die das Werkzeug-Gate zu Recht blockierte. Der Lauf lief weiter und
    kostete, bis jemand antwortete. Die Lehre ist nicht „weniger Gate", sondern: für eine Pflicht muss es einen
    benannten, harmlosen Befehl geben, der nicht wie ein Massenlöschen aussieht.

    `art`: satz2 (Messgerätänderung) · budget · philipp · sonst. Bei satz2 gilt der Lauf als verworfen; seine
    Ablehnungen zählen dann nicht mehr im Projektgedächtnis (3.12 F5).
    """
    lauf = _lauf(con, lauf_id)
    if lauf["status"] in ("verworfen", "beendet", "gesaettigt", "abgebrochen"):
        return {"lauf": lauf_id, "status": lauf["status"], "unveraendert": True,
                "hinweis": "Lauf war bereits beendet — Abbruch ohne Wirkung, trotzdem protokolliert"}
    status_neu = "verworfen" if art == "satz2" else "abgebrochen"
    offen = [dict(z) for z in con.execute(
        "SELECT nummer, status FROM generationen WHERE lauf_id=? AND status IN ('laeuft','vorgelegt')", (lauf_id,))]
    with transaktion(con):
        con.execute("UPDATE generationen SET status='abgebrochen', grund=? WHERE lauf_id=? AND status IN ('laeuft','vorgelegt')",
                    (f"Lauf abgebrochen ({art}): {grund}"[:400], lauf_id))
        con.execute("UPDATE laeufe SET status=?, beendet_am=?, grund=? WHERE id=?",
                    (status_neu, protokoll.jetzt(), f"{von} ({art}): {grund}"[:400], lauf_id))
    protokoll.schreiben(con, "lauf.abgebrochen", lauf_id=lauf_id, abbruchart=art, von=von, grund=grund,
                        status=status_neu, offene_generationen=[o["nummer"] for o in offen],
                        regel="Fassung 5 Abschnitt 5: Abbrüche nach Satz 2 oder Budget sind vom Freigabe-Gate "
                              "ausgenommen — immer erlaubt, immer protokolliert.")
    return {"lauf": lauf_id, "status": status_neu, "art": art, "von": von, "grund": grund,
            "abgebrochene_generationen": [o["nummer"] for o in offen],
            "hinweis": ("Nach Satz 2 verworfen: die Ablehnungen dieses Laufs zählen nicht mehr im Projektgedächtnis"
                        if art == "satz2" else None)}


def freigabe(con: sqlite3.Connection, lauf_id: int, nummer: int, entscheidung: str, grund: str, von: str) -> dict:
    """Philipp gibt frei oder lehnt ab. Ablehnung → Rückkehr zur Vorgeneration (Lazarus), Grund ins Gedächtnis."""
    g = con.execute("SELECT * FROM generationen WHERE lauf_id=? AND nummer=?", (lauf_id, nummer)).fetchone()
    if not g or g["status"] != "vorgelegt":
        raise LaufFehler(f"Generation {nummer} ist nicht vorgelegt (Status: {g['status'] if g else 'fehlt'})")
    werk = _werk(con, _lauf(con, lauf_id)["werk_id"])
    verf = verfassung.lesen(con, werk["id"])
    uebungswerk = bool(((verf or {}).get("regeln") or {}).get("uebungswerk"))
    if entscheidung == "frei" and not von.lower().startswith("philipp") and not uebungswerk:
        raise LaufFehler("Freigabe eines Werks mit Betriebszweck nur durch Philipp (Abschnitt 4 F2) — Vollmacht gilt nur für Übungswerke")
    vollmacht = "Vollmacht Abschnitt 4 F2 (Übungswerk ohne Betriebszweck, Verfassung regeln.uebungswerk=true)" if (uebungswerk and not von.lower().startswith("philipp")) else None
    gewaehlt_k = ((lj(g["kandidaten"]) or {}).get("_gewaehlt") or {})
    if entscheidung == "frei":
        with transaktion(con):
            con.execute("UPDATE generationen SET status='angenommen', freigabe_am=?, freigabe_grund=? WHERE lauf_id=? AND nummer=?",
                        (protokoll.jetzt(), f"{von}: {grund}", lauf_id, nummer))
            con.execute("UPDATE laeufe SET status='bereit' WHERE id=?", (lauf_id,))
        g_m = lj(g["masse"]) or {}
        protokoll.schreiben(con, "freigabe.frei", lauf_id=lauf_id, nummer=nummer, von=von, grund=grund, vollmacht=vollmacht,
                            kernmass_f2=g_m.get("kernmass_f2"), urteil=g_m.get("_urteil_f2"))
        for b, kid in gewaehlt_k.items():
            gedaechtnis.geschmack_merken(con, werk["id"], lauf_id, nummer, kid, "frei", grund, von)
        r = {"nummer": nummer, "status": "angenommen", "entropie": entropie.messen(con, lauf_id, nummer)}
        s_ = entropie.pruefen_und_beenden(con, lauf_id)
        if s_:
            r["saettigung"] = s_
        return r
    for b, kid in gewaehlt_k.items():
        gedaechtnis.geschmack_merken(con, werk["id"], lauf_id, nummer, kid, "ablehnen", grund, von)
    vorherige = con.execute("SELECT MAX(nummer) FROM generationen WHERE lauf_id=? AND nummer<? AND status='angenommen'", (lauf_id, nummer)).fetchone()[0]
    r = lazarus.rueckkehr(con, lauf_id, vorherige, Path(werk["pfad"]))
    with transaktion(con):
        con.execute("UPDATE generationen SET status='abgelehnt_philipp', freigabe_am=?, freigabe_grund=? WHERE lauf_id=? AND nummer=?",
                    (protokoll.jetzt(), f"{von}: {grund}", lauf_id, nummer))
        con.execute("UPDATE kandidaten SET status='abgelehnt', grund=? WHERE lauf_id=? AND generation=? AND status='angenommen'",
                    (f"Philipp: {grund}", lauf_id, nummer))
        con.execute("UPDATE laeufe SET status='bereit' WHERE id=?", (lauf_id,))
    protokoll.schreiben(con, "freigabe.abgelehnt", lauf_id=lauf_id, nummer=nummer, von=von, grund=grund, rueckkehr=r)
    return {"nummer": nummer, "status": "abgelehnt_philipp", "rueckkehr": r}


def kurve_nachrechnen(con: sqlite3.Connection, lauf_id: int, testbestand_von_lauf: int | None = None) -> dict:
    """Verlaufskurve eines Laufs mit Formel F2 und dem Endtestbestand nachgerechnet (3.5 F2):
    jede angenommene Generation wird aus dem Lazarus-Archiv geholt, der Testbestand der
    letzten angenommenen Generation (oder des angegebenen Laufs) darübergelegt, in der Kammer
    gemessen. Zeigt, wie viel des alten Zuwachses Werk war und wie viel Tests."""
    import shutil, tarfile, tempfile
    lauf = _lauf(con, lauf_id)
    werk = _werk(con, lauf["werk_id"])
    mass = lj(lauf["mass"])
    paket, bereiche = mass["paket"], mass["bereiche"]
    ref = _referenzlast(werk["name"], paket)
    gens = [dict(z) for z in con.execute("SELECT generation, tag, archiv, pruefsumme FROM lazarus WHERE lauf_id=? ORDER BY generation", (lauf_id,))]
    quelle_lauf = testbestand_von_lauf or lauf_id
    letzte = con.execute("SELECT archiv, generation FROM lazarus WHERE lauf_id=? ORDER BY generation DESC LIMIT 1", (quelle_lauf,)).fetchone()
    tmp = Path(tempfile.mkdtemp(prefix="kurve-"))
    try:
        end = tmp / "end"; end.mkdir()
        with tarfile.open(letzte["archiv"]) as t:
            t.extractall(end, filter="data")
        testbestand = {str(p.relative_to(end)): p.read_text() for p in (end / "tests").glob("test_*.py")}
        zeilen = []
        for g in gens:
            ziel = tmp / f"gen{g['generation']}"; ziel.mkdir()
            with tarfile.open(g["archiv"]) as t:
                t.extractall(ziel, filter="data")
            eigene = sorted(str(p.relative_to(ziel)) for p in (ziel / "tests").glob("test_*.py"))
            m_alt = messgeraet.messen(ziel, bereiche, paket, ref)                       # eigener Testbestand (wie damals)
            m_end = messgeraet.messen(ziel, bereiche, paket, ref, dateien=testbestand)  # Endtestbestand (paarweise)
            z = {"generation": g["generation"], "tag": g["tag"], "tests_eigen": len(eigene),
                 "f1_eigen": m_alt["kernmass"] if m_alt["gueltig"] else None,
                 "f2_eigen": messgeraet.kernmass_f2(m_alt) if m_alt["gueltig"] else None,
                 "f2_endtests": messgeraet.kernmass_f2(m_end) if m_end["gueltig"] else None,
                 "bereiche_endtests": {b: messgeraet.bereich_masse(m_end, b) for b in bereiche} if m_end["gueltig"] else None,
                 "fehlgeschlagen_endtests": m_end["werk"]["tests_fehlgeschlagen_liste"] if m_end["gueltig"] else None}
            zeilen.append(z)
        r = {"lauf": lauf_id, "testbestand": sorted(testbestand), "testbestand_aus": f"Lauf {quelle_lauf} Generation {letzte['generation']}", "kurve": zeilen}
        protokoll.schreiben(con, "kurve.nachgerechnet", lauf_id=lauf_id, testbestand=len(testbestand),
                            f1=[(z["generation"], z["f1_eigen"]) for z in zeilen], f2_end=[(z["generation"], z["f2_endtests"]) for z in zeilen])
        return r
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _verhandeln(con, lauf_id, werk, nummer, pfad, paket, bereiche, bstrassen, basis, ausgang, ref, tausch, bereich, kid, u):
    """3.8 Schritt 2: Der Kandidat verletzt einen expliziten Vertrag und hat ihn benannt. Der Schwarm des Nachbarn
    (Nische sicher) erzeugt die Anpassung seiner Seite; Kandidat + Anpassung werden zusammen geprüft.
    Vertragsdatei darf vom Paar geändert werden (dann Teil des Paares). Rückgabe: neues Urteil."""
    verl = u.get("vertrag_verletzt") or []
    nachbarn = {vertraege.nachbar_von(con, werk["id"], bereich, "tests/vertraege/" + v.split("::")[0]) for v in verl}
    nachbarn |= {vertraege.nachbar_von(con, werk["id"], bereich, p) for p in (u.get("vertrag_dateien") or [])}
    # benannte Verträge (Text unter VERTRÄGE) → Nachbar über den Dateinamen
    kd0 = con.execute("SELECT vertraege FROM kandidaten WHERE id=?", (kid,)).fetchone()
    for v in vertraege.fuer_bereich(con, werk["id"], bereich):
        if Path(v["pfad"]).stem in (kd0["vertraege"] or ""):
            nachbarn.add(v["von_bereich"] if v["nach_bereich"] == bereich else v["nach_bereich"])
    nachbarn.discard(None)
    if not nachbarn:
        return u
    einseitig_ok = u["status"] == "ueberlebt" and not verl  # (b): kein Test fällt — der Nachbar bestätigt oder passt an
    kd = con.execute("SELECT diff, begruendung, vertraege FROM kandidaten WHERE id=?", (kid,)).fetchone()
    protokoll.schreiben(con, "verhandlung.begonnen", lauf_id=lauf_id, generation=nummer, kandidat=kid, bereich=bereich, nachbarn=sorted(nachbarn), verletzt=verl)
    extra: dict[str, str] = {}
    anpassungen = []
    for nb in sorted(nachbarn):
        if nb in tausch.get("_gesperrte_bereiche", []):
            grund = f"Verhandlung nicht ausführbar: Nachbar {nb} wegen Rauschmessung gesperrt"
            protokoll.schreiben(con, "generation.bereich_uebersprungen", lauf_id=lauf_id, generation=nummer,
                                bereich=nb, kandidat=kid, grund=grund,
                                toleranz=(tausch.get("_rauschbelege", {}).get(nb) or {}).get("toleranz"),
                                nachweis_sha256=tausch.get("_vorspann_sha256"))
            with transaktion(con):
                con.execute("UPDATE kandidaten SET status='abgelehnt',grund=? WHERE id=?", (grund, kid))
            return {**u, "status":"abgelehnt", "grund":grund}
        vt = vertraege.text_fuer_bereich(con, werk["id"], nb)
        # Der Nachbar sieht die vom Kandidaten geänderte Vertragsdatei (neue Zusicherungen), nicht nur den alten Vertrag
        kdat = aegis.kandidat_dateien(pfad, kd["diff"]) or {}
        neue_vertraege = "\n".join(f"- {p} (Fassung des Kandidaten):\n```python\n{(i or '')[:3000]}\n```" for p, i in kdat.items() if p.startswith("tests/vertraege/"))
        auftrag = (f"VERHANDLUNG (3.8 Schritt 2): Der Nachbarbereich „{bereich}“ will einen Vertrag an eurer Grenze ändern. Sein Diff:\n```diff\n{kd['diff'][:4000]}\n```\n"
                   f"Begründung: {kd['begruendung'][:500]}\nBenannte Verträge: {kd['vertraege']}\nDurch die Änderung fallen diese Vertragstests: {verl or 'keine'}\n"
                   f"Ergebnis der Einzelprüfung des Kandidaten (ohne deine Seite): {u['status']} — {u['grund'][:300]}\n"
                   + (f"Geänderte Vertragsdatei(en):\n{neue_vertraege}\n" if neue_vertraege else "")
                   + f"\nErzeuge die Anpassung DEINER Seite ({nb}), damit die geänderte Vertragsdatei und alle Tests des Werks bestehen — und, falls die Vertragsdatei "
                   f"tests/vertraege/... selbst noch geändert werden muss, den Diff dafür (Pfad tests/vertraege/...). Nenne unter VERTRÄGE denselben Vertrag. "
                   f"Ist auf deiner Seite nichts anzupassen, antworte mit KEIN VORSCHLAG. Alle übrigen Tests müssen weiter bestehen.")
        ids = genesis.erzeugen(con, lauf_id, werk["id"], nummer, pfad, paket, nb, messgeraet.bereich_masse(basis, nb), nische="sicher",
                               befunde=[], referenzlast=None, vertraege_text=vt + "\n\n" + auftrag)
        if einseitig_ok and all(con.execute("SELECT status FROM kandidaten WHERE id=?", (aid,)).fetchone()["status"] == "leer" for aid in ids):
            # Nachbar bestätigt („KEIN VORSCHLAG“ von allen), kein Vertragstest fällt: Paar = Kandidat allein, gemeinsam geprüft
            protokoll.schreiben(con, "verhandlung.paar", lauf_id=lauf_id, generation=nummer, kandidat=kid, anpassung=None, nachbar=nb, status=u["status"], grund="Nachbar: keine Anpassung nötig (KEIN VORSCHLAG)", vertrag_verletzt=[])
            anpassungen.append(None)
            continue
        for aid in ids:
            az = con.execute("SELECT diff, status FROM kandidaten WHERE id=?", (aid,)).fetchone()
            if az["status"] != "erzeugt":
                continue
            d = aegis.kandidat_dateien(pfad, az["diff"])
            if not d:
                continue
            anp = {p: (i if i is not None else "") for p, i in d.items()}
            # Paar prüfen: Kandidat + Anpassung. Der Kandidat trägt schon 'abgelehnt' aus der Einzelprüfung — für die
            # Paarprüfung zurück auf 'erzeugt' (sonst liefert pruefen() nur das gespeicherte Urteil; Fehler bis Lauf 13 Gen 10).
            with transaktion(con):
                con.execute("UPDATE kandidaten SET status='erzeugt', grund='' WHERE id=?", (kid,))
            u2 = aegis.pruefen(con, lauf_id, werk["id"], kid, pfad, paket, bereiche, bstrassen, basis, ausgang, ref, tausch, extra_code=anp)
            with transaktion(con):
                con.execute("UPDATE kandidaten SET status=?, grund=? WHERE id=?", ("verhandlung", f"Anpassung für Kandidat {kid} ({bereich}): Paar {u2['status']}", aid))
            protokoll.schreiben(con, "verhandlung.paar", lauf_id=lauf_id, generation=nummer, kandidat=kid, anpassung=aid, nachbar=nb,
                                status=u2["status"], grund=u2["grund"][:300], vertrag_verletzt=u2.get("vertrag_verletzt"))
            # Verhandlung bestanden (3.8 Schritt 2): das Paar verletzt keinen Vertrag und keine Pareto-Regel mehr.
            # Ob das Paar dann auch einen Kernmaßgewinn hat (Annahme), entscheidet das Maß wie bei jedem Kandidaten.
            mass = u2.get("mass")
            paar_ok = (isinstance(mass, dict) and type(mass.get("ok")) is bool
                       and isinstance(mass.get("grund"), str) and bool(mass["grund"])
                       and all(type(mass.get(k)) in (int, float) for k in ("kern_basis", "kern_kandidat", "zuwachs"))
                       and u2.get("vertrag_verletzt") == []
                       and mass.get("pareto_schlechter") == [] and mass.get("grenzen_gerissen") == [])
            if paar_ok:
                extra.update(anp); anpassungen.append(aid)
                u = u2
                break
        else:
            protokoll.schreiben(con, "verhandlung.gescheitert", lauf_id=lauf_id, generation=nummer, kandidat=kid, nachbar=nb)
            with transaktion(con):
                con.execute("UPDATE kandidaten SET status='abgelehnt', grund=? WHERE id=? AND status IN ('erzeugt','ueberlebt')", (u["grund"] + " | Verhandlung gescheitert (Vertragsänderung ohne bestandene Anpassung des Nachbarn, Anhang A Satz 4)", kid))
            return {**u, "status": "abgelehnt", "grund": u["grund"] + " | Verhandlung gescheitert"}
    if anpassungen:
        # die Anpassung ist Teil des Kandidaten-Dateisatzes (bereits in _dateien über extra_code enthalten); None = Nachbar bestätigte ohne Änderung
        protokoll.schreiben(con, "verhandlung.bestanden", lauf_id=lauf_id, generation=nummer, kandidat=kid, bereich=bereich, anpassungen=[a for a in anpassungen if a], nachbar_bestaetigt_ohne_aenderung=[n for n, a in zip(sorted(nachbarn), anpassungen) if a is None], nachbarn=sorted(nachbarn))
        with transaktion(con):
            con.execute("UPDATE kandidaten SET grund=? WHERE id=?", (u["grund"] + f" | Verhandlung bestanden mit {sorted(nachbarn)} (Anpassung {anpassungen})", kid))
        u = {**u, "verhandlung_bestanden": True, "anpassungen": anpassungen}
    return u


def generation0(con: sqlite3.Connection, lauf_id: int, mutanten_json: str | None, ziel: int) -> dict:
    """Generation 0 (3.5): Mutanten messen, blinde Flecken durch Testbau schließen, erneut messen.
    Läuft VOR dem Einfrieren des Maßes (die Tests des Werks dürfen evolutionieren; das Messgerät nicht).
    mutanten_json: von Hermes gesetzte Mutanten [{datei, zeile, art, beschreibung, code}] (Tor 2) — sonst erzeugt das Biotop eigene."""
    import json as _json
    from .organe import generation0 as G0
    lauf = _lauf(con, lauf_id)
    _vorspann_verlangen(con, lauf_id, "gen0")
    werk = _werk(con, lauf["werk_id"]); pfad = Path(werk["pfad"])
    b = lj(werk["bericht"]); paket = b["paket"]
    bereiche = landkarte.bereiche_finden(pfad, paket)
    if mutanten_json:
        mutanten = _json.loads(Path(mutanten_json).read_text())
        for m in mutanten:
            m.setdefault("quelle", "hermes")
    else:
        mutanten = G0.erzeugen(pfad, paket, bereiche)
    nummern = {id(m): i for i, m in enumerate(mutanten, 1)}
    protokoll.schreiben(con, "generation0.begonnen", lauf_id=lauf_id, mutanten=len(mutanten), quelle=mutanten[0].get("quelle") if mutanten else None)
    # F4: äquivalente Mutanten VOR der Zählung mit Beleg aussortieren
    ref = _referenzlast(werk["name"], paket)
    G0.aequivalenz_pruefen(con, lauf_id, pfad, ref, mutanten)
    vorher = G0.messen(con, lauf_id, werk["id"], pfad, mutanten, "vorher")
    if ziel <= 1:  # Anteil (3.5: ≥ 80 von 100 nicht-äquivalenten) statt absoluter Zahl
        import math as _math
        ziel = _math.ceil(ziel * vorher["nicht_aequivalent"])
    runde = 0; neue_gesamt: dict[str, str] = {}
    blind = vorher["blind"]
    while blind and runde < 3:
        runde += 1
        r = G0.tests_evolutionieren(con, lauf_id, werk["id"], pfad, paket, blind, nummern)
        if not r["neue_tests"]:
            break
        for p, c in r["neue_tests"].items():
            (pfad / p).write_text(c); neue_gesamt[p] = c
        # Gegenprobe: neuer Testbestand am unmutierten Werk grün?
        e = kammer.ausfuehren(pfad, ["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=line"], zeitlimit_s=120)
        if e.rc != 0:
            # Tests, die am Original fallen, wieder entfernen (laut scheitern, nicht still)
            for p in list(r["neue_tests"]):
                if p.split("/")[-1] in e.stdout:
                    (pfad / p).unlink(missing_ok=True); neue_gesamt.pop(p, None)
        zwischen = G0.messen(con, lauf_id, werk["id"], pfad, mutanten, "nachher")
        blind = zwischen["blind"]
        protokoll.schreiben(con, "generation0.runde", lauf_id=lauf_id, runde=runde, gefangen=zwischen["gefangen"], gesamt=len(mutanten), neue_tests=sorted(r["neue_tests"]))
        if zwischen["gefangen"] >= ziel and not blind:
            break
    nachher = G0.messen(con, lauf_id, werk["id"], pfad, mutanten, "nachher")
    if neue_gesamt:
        lazarus.sicherstellen_repo(pfad)
        lazarus._git(pfad, "add", "-A")
        if lazarus._git(pfad, "status", "--porcelain"):
            lazarus._git(pfad, "commit", "-qm", f"Biotop Lauf {lauf_id} Generation 0: {len(neue_gesamt)} Tests aus Mutantenfang")
    r = {"mutanten": len(mutanten), "nicht_aequivalent": nachher["nicht_aequivalent"],
         "aequivalent": [f"#{nummern[id(m)]} {m['aequivalenz_beleg']}" for m in mutanten if m.get("aequivalent")],
         "gefangen_vorher": vorher["gefangen"], "gefangen_nachher": nachher["gefangen"], "ziel": ziel,
         "bezugsgroesse": f"gefangen: {nachher['gefangen']} von {nachher['nicht_aequivalent']} nicht-äquivalenten (von {len(mutanten)} gesetzten)",
         "erreicht": nachher["gefangen"] >= ziel, "neue_tests": sorted(neue_gesamt), "runden": runde,
         "blind_vorher": [f"#{nummern[id(m)]} {m['datei']}:{m['zeile']} {m['beschreibung']}" for m in vorher["blind"]],
         "blind_nachher": [f"#{nummern[id(m)]} {m['datei']}:{m['zeile']} {m['beschreibung']}" for m in nachher["blind"]]}
    protokoll.schreiben(con, "generation0.ergebnis", lauf_id=lauf_id, **{k: v for k, v in r.items() if k not in ("blind_vorher",)})
    return r
