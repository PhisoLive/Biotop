"""Befehlszeile des Biotops (Phase 1: einzige Oberfläche).

  biotop lauf anlegen --budget 30
  biotop einlegen <lauf> <name> <quelle>
  biotop kartieren <lauf>
  biotop vorspann <lauf>            (Generation minus eins, vor gen0 und mass)
  biotop gen0 <lauf>
  biotop mass <lauf> --bestaetigt-von Philipp
  biotop generation <lauf>
  biotop freigabe <lauf> <nummer> frei|ablehnen --grund "..." --von Philipp
  biotop abbrechen <lauf> --grund "..." --von "..." [--art satz2|budget|philipp|sonst]   (Pflicht, nie gesperrt)
  biotop lazarus liste|rueckkehr <lauf> [nummer] [--ziel PFAD]
  biotop kasse <lauf>
  biotop protokoll [--ab N] [--art X]
  biotop benutzer <name>            (Kennwort über Umgebungsvariable BIOTOP_KENNWORT)
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

from . import lauf as L
from .kern import anmeldung, kasse, protokoll
from .kern.datenbank import verbinden
from .organe import lazarus


def _p(obj):
    print(json.dumps(obj, ensure_ascii=False, indent=1, default=str))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="biotop")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("lauf"); s.add_argument("aktion", choices=["anlegen"]); s.add_argument("--budget", type=float, required=True)
    s = sub.add_parser("einlegen"); s.add_argument("lauf", type=int); s.add_argument("name"); s.add_argument("quelle")
    s = sub.add_parser("kartieren"); s.add_argument("lauf", type=int)
    s = sub.add_parser("vorspann"); s.add_argument("lauf", type=int)
    s = sub.add_parser("mass"); s.add_argument("lauf", type=int); s.add_argument("--bestaetigt-von", required=True)
    s = sub.add_parser("generation"); s.add_argument("lauf", type=int); s.add_argument("--einschleusen", help="JSON-Datei mit Proben-Kandidaten [{bereich, diff, begruendung, vertraege, probe}]")
    s = sub.add_parser("abbrechen"); s.add_argument("lauf", type=int); s.add_argument("--grund", required=True)
    s.add_argument("--von", required=True); s.add_argument("--art", choices=["satz2", "budget", "philipp", "sonst"], default="satz2")
    s = sub.add_parser("freigabe"); s.add_argument("lauf", type=int); s.add_argument("nummer", type=int)
    s.add_argument("entscheidung", choices=["frei", "ablehnen"]); s.add_argument("--grund", default=""); s.add_argument("--von", required=True)
    s = sub.add_parser("lazarus"); s.add_argument("aktion", choices=["liste", "rueckkehr"]); s.add_argument("lauf", type=int)
    s.add_argument("nummer", type=int, nargs="?"); s.add_argument("--ziel")
    s = sub.add_parser("kasse"); s.add_argument("lauf", type=int, nargs="?")
    s = sub.add_parser("protokoll"); s.add_argument("--ab", type=int, default=0); s.add_argument("--art"); s.add_argument("--limit", type=int, default=200)
    s = sub.add_parser("protokoll-pruefen")
    s = sub.add_parser("benutzer"); s.add_argument("name")
    s = sub.add_parser("verfassung"); s.add_argument("lauf", type=int); s.add_argument("text_md"); s.add_argument("regeln_json"); s.add_argument("--von", required=True)
    s = sub.add_parser("gen0"); s.add_argument("lauf", type=int); s.add_argument("--mutanten", help="JSON-Datei mit von Hermes gesetzten Mutanten"); s.add_argument("--ziel", type=float, default=0.8, help="absolute Zahl oder Anteil ≤ 1 (Vorgabe 0,8)")
    s = sub.add_parser("vertraege"); s.add_argument("lauf", type=int); s.add_argument("verzeichnis"); s.add_argument("--von", required=True)
    s = sub.add_parser("kurve"); s.add_argument("lauf", type=int); s.add_argument("--testbestand-von-lauf", type=int)
    s = sub.add_parser("mentor"); s.add_argument("lauf", type=int)
    s = sub.add_parser("richtung"); s.add_argument("lauf", type=int); s.add_argument("name"); s.add_argument("--von", required=True)
    s = sub.add_parser("gedaechtnis"); s.add_argument("aktion", choices=["import", "art", "projekt", "geschmack"]); s.add_argument("lauf", type=int, nargs="?"); s.add_argument("--bereich")
    s = sub.add_parser("entropie"); s.add_argument("lauf", type=int)
    s = sub.add_parser("dienst"); s.add_argument("--port", type=int, default=8642); s.add_argument("--host", default="127.0.0.1")
    s = sub.add_parser("oberflaeche-belege")
    a = ap.parse_args(argv)
    con = verbinden()
    try:
        if a.cmd == "lauf":
            _p({"lauf": L.anlegen(con, a.budget), "budget_eur": a.budget})
        elif a.cmd == "einlegen":
            _p(L.einlegen(con, a.lauf, a.name, a.quelle))
        elif a.cmd == "kartieren":
            _p(L.kartieren(con, a.lauf))
        elif a.cmd == "vorspann":
            _p(L.vorspann.ausfuehren(con, a.lauf))
        elif a.cmd == "mass":
            r = L.mass_einfrieren(con, a.lauf, a.bestaetigt_von)
            _p({"mass": r["mass"], "kernmass": r["messung"]["kernmass"], "bereiche": {b: {k: v for k, v in m.items() if not isinstance(v, (list, dict))} for b, m in r["messung"]["bereiche"].items()}, "schnappschuss": r["schnappschuss"]})
        elif a.cmd == "generation":
            ein = json.loads(Path(a.einschleusen).read_text()) if a.einschleusen else None
            r = L.generation(con, a.lauf, einschleusen=ein)
            m = r.get("messung")
            _p({"nummer": r["nummer"], "status": r["status"], "grund": r["grund"], "kandidaten": r["kandidaten"],
                "kernmass": m["kernmass"] if m else None, "schnappschuss": r.get("schnappschuss"), "kasse": kasse.stand(con, a.lauf)})
        elif a.cmd == "abbrechen":
            _p(L.abbrechen(con, a.lauf, a.grund, a.von, a.art))
        elif a.cmd == "freigabe":
            _p(L.freigabe(con, a.lauf, a.nummer, a.entscheidung, a.grund, a.von))
        elif a.cmd == "lazarus":
            if a.aktion == "liste":
                _p(lazarus.liste(con, a.lauf))
            else:
                werk = L._werk(con, L._lauf(con, a.lauf)["werk_id"])
                _p(lazarus.rueckkehr(con, a.lauf, a.nummer, Path(werk["pfad"]), Path(a.ziel) if a.ziel else None))
        elif a.cmd == "kasse":
            if a.lauf:
                _p(kasse.stand(con, a.lauf))
            print(kasse.bericht_md(con, a.lauf))
        elif a.cmd == "protokoll":
            for z in protokoll.lesen(con, a.ab, a.art, a.limit):
                print(f"#{z['nr']} {z['zeit']} {z['art']} {z['inhalt']}")
        elif a.cmd == "protokoll-pruefen":
            ok, n = protokoll.pruefen(con)
            _p({"kette_in_ordnung": ok, "geprueft": n})
        elif a.cmd == "verfassung":
            from .organe import verfassung as V
            lauf = L._lauf(con, a.lauf)
            V.einlegen(con, lauf["werk_id"], Path(a.text_md).read_text(), json.loads(Path(a.regeln_json).read_text()), f"{a.text_md} + {a.regeln_json}", a.von)
            _p({"werk_id": lauf["werk_id"], "eingelegt": True})
        elif a.cmd == "gen0":
            _p(L.generation0(con, a.lauf, a.mutanten, a.ziel))
        elif a.cmd == "vertraege":
            from .organe import vertraege as VT
            lauf = L._lauf(con, a.lauf); werk = L._werk(con, lauf["werk_id"])
            vs = {}
            for f in sorted(Path(a.verzeichnis).glob("test_vertrag_*.py")):
                a_, b_ = f.stem.replace("test_vertrag_", "").split("_", 1)
                vs[(a_, b_)] = f.read_text()
            _p({"eingelegt": VT.einlegen(con, werk["id"], Path(werk["pfad"]), vs, f"{a.verzeichnis} ({a.von})")})
        elif a.cmd == "kurve":
            _p(L.kurve_nachrechnen(con, a.lauf, a.testbestand_von_lauf))
        elif a.cmd == "mentor":
            from .organe import mentor as M
            _p(M.richtungen(con, a.lauf))
        elif a.cmd == "richtung":
            from .organe import mentor as M
            _p(M.waehlen(con, a.lauf, a.name, a.von))
        elif a.cmd == "gedaechtnis":
            from .organe import gedaechtnis as G
            if a.aktion == "import":
                werk = L._werk(con, L._lauf(con, a.lauf)["werk_id"])
                _p({"lauf": a.lauf, "projekt_importiert": G.projekt_import(con, a.lauf, Path(werk["pfad"])), "art_importiert": G.art_import(con, a.lauf)})
            elif a.aktion == "art":
                _p(G.art_zusammenfassung(con))
            elif a.aktion == "projekt":
                werk = L._werk(con, L._lauf(con, a.lauf)["werk_id"])
                _p(G.gescheiterte_wege(con, werk["id"], a.bereich, 200) if a.bereich else [dict(z) for z in con.execute("SELECT werk, bereich, grundklasse, COUNT(*) n FROM projektgedaechtnis GROUP BY werk, bereich, grundklasse")])
            else:
                _p([dict(z) for z in con.execute("SELECT werk, quelle, entscheidung, COUNT(*) n FROM geschmack GROUP BY werk, quelle, entscheidung")])
        elif a.cmd == "entropie":
            from .organe import entropie as E
            _p({"verlauf": E.verlauf(con, a.lauf), "saettigung": E.saettigung(con, a.lauf)})
        elif a.cmd == "oberflaeche-belege":
            from . import oberflaeche as O
            _p(O.belege())
        elif a.cmd == "dienst":
            from . import dienst as D
            D.starten(a.host, a.port)
        elif a.cmd == "benutzer":
            anmeldung.benutzer_anlegen(con, a.name, os.environ.get("BIOTOP_KENNWORT", ""))
            _p({"benutzer": a.name, "angelegt": True})
        return 0
    except (L.LaufFehler, L.vorspann.VorspannFehler, kasse.BudgetErschoepft) as e:
        print(f"ABBRUCH: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
