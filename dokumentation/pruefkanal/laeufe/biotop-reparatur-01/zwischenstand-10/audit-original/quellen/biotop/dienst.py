"""HTTP-Dienst des Biotops (nur lesend in Phase 1, Bindung an 127.0.0.1).

Anmeldezwang fest verdrahtet: JEDE Route außer POST /anmelden verlangt
`Authorization: Bearer <token>`; ohne gültigen Token → 401. Es gibt keinen
Schalter, der das abstellt.

Routen:
  POST /anmelden                      {name, kennwort} → {token}
  GET  /laeufe                        alle Läufe
  GET  /laeufe/<id>                   Lauf mit Maß und Kasse
  GET  /laeufe/<id>/generationen      Generationen mit Maßen
  GET  /laeufe/<id>/kandidaten        Kandidaten
  GET  /laeufe/<id>/kasse             Kassenstand
  GET  /laeufe/<id>/lazarus           Schnappschüsse
  GET  /werke                         Werke
  GET  /werke/<id>/landkarte          Landkarte (Stufen 0–3, Straßen, Verträge)
  GET  /protokoll                     Protokoll (letzte 200)
"""

from __future__ import annotations

import json
import re
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

from .kern import anmeldung, kasse, protokoll
from .kern.datenbank import lj, verbinden
from . import lauf as L
from . import oberflaeche
from .organe import entropie, gedaechtnis, mentor, verfassung

ROUTEN = [
    ("GET", r"^/$"),  # Oberfläche (HTML); ohne Token wird nur die Anmeldemaske geliefert, alle Daten-Routen bleiben 401
    ("POST", r"^/anmelden$"),
    ("POST", r"^/laeufe/(\d+)/abbrechen$"),   # Pflicht, nie gesperrt (F5 Abschnitt 5)
    ("POST", r"^/laeufe/(\d+)/freigabe$"),
    ("POST", r"^/laeufe/(\d+)/richtung$"),
    ("GET", r"^/laeufe/(\d+)/vorlage$"),
    ("GET", r"^/laeufe/(\d+)/entropie$"),
    ("GET", r"^/laeufe/(\d+)/mentor$"),
    ("GET", r"^/laeufe/(\d+)/immunsystem$"),
    ("GET", r"^/laeufe/(\d+)/verfassung$"),
    ("GET", r"^/laeufe$"),
    ("GET", r"^/laeufe/(\d+)$"),
    ("GET", r"^/laeufe/(\d+)/generationen$"),
    ("GET", r"^/laeufe/(\d+)/kandidaten$"),
    ("GET", r"^/laeufe/(\d+)/kasse$"),
    ("GET", r"^/laeufe/(\d+)/lazarus$"),
    ("GET", r"^/werke$"),
    ("GET", r"^/werke/(\d+)/landkarte$"),
    ("GET", r"^/protokoll$"),
]


def _rows(con, q, p=()):
    return [dict(z) for z in con.execute(q, p)]


class Handler(BaseHTTPRequestHandler):
    con = None

    def _senden(self, code: int, obj):
        body = json.dumps(obj, ensure_ascii=False, default=str).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):  # kein Zugriffsprotokoll auf stderr
        pass

    def _benutzer(self) -> str | None:
        h = self.headers.get("Authorization", "")
        if not h.startswith("Bearer "):
            return None
        return anmeldung.pruefen(self.con, h[7:].strip())

    def _json_body(self):
        n = int(self.headers.get("Content-Length", "0"))
        try:
            return json.loads(self.rfile.read(n) or b"{}")
        except json.JSONDecodeError:
            return None

    def do_POST(self):
        if self.path == "/anmelden":
            d = self._json_body()
            if d is None:
                return self._senden(400, {"fehler": "kein JSON"})
            token = anmeldung.anmelden(self.con, str(d.get("name", "")), str(d.get("kennwort", "")))
            if not token:
                return self._senden(401, {"fehler": "Anmeldung fehlgeschlagen"})
            return self._senden(200, {"token": token})
        benutzer = self._benutzer()
        if not benutzer:
            return self._senden(401, {"fehler": "Anmeldung erforderlich"})
        d = self._json_body()
        if d is None:
            return self._senden(400, {"fehler": "kein JSON"})
        m = re.match(r"^/laeufe/(\d+)/abbrechen$", self.path)
        if m:
            lauf_id = int(m.group(1))
            d = self._json()
            try:
                r = L.abbrechen(self.con, lauf_id, str(d.get("grund", "")), f"{benutzer} (Oberfläche)",
                                str(d.get("art", "satz2")))
            except Exception as e:
                return self._senden(400, {"fehler": str(e)})
            return self._senden(200, r)
        m = re.match(r"^/laeufe/(\d+)/freigabe$", self.path)
        if m:
            # Bedienelement freigabe-frei / freigabe-ablehnen → lauf.freigabe (Kern); `von` ist der angemeldete Benutzer
            lauf_id = int(m.group(1))
            g = self.con.execute("SELECT nummer FROM generationen WHERE lauf_id=? AND status='vorgelegt'", (lauf_id,)).fetchone()
            if not g:
                return self._senden(409, {"fehler": "keine Generation wartet auf Freigabe"})
            try:
                r = L.freigabe(self.con, lauf_id, g["nummer"], str(d.get("entscheidung", "")), str(d.get("grund", "")), f"{benutzer} (Oberfläche)")
            except L.LaufFehler as e:
                return self._senden(409, {"fehler": str(e)})
            return self._senden(200, r)
        m = re.match(r"^/laeufe/(\d+)/richtung$", self.path)
        if m:
            try:
                return self._senden(200, mentor.waehlen(self.con, int(m.group(1)), str(d.get("name", "")), f"{benutzer} (Oberfläche)"))
            except RuntimeError as e:
                return self._senden(409, {"fehler": str(e)})
        return self._senden(404, {"fehler": "unbekannt"})

    def _html(self, text: str):
        body = text.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'unsafe-inline'; style-src 'unsafe-inline'")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        pfad = self.path.split("?")[0]
        if pfad == "/":
            # Die Seite selbst enthält keine Daten; sie zeigt ohne Token nur die Anmeldemaske. Jede Daten-Route unten verlangt den Token.
            return self._html(oberflaeche.HTML)
        # Anmeldezwang VOR jeder Routenauflösung — auch unbekannte Pfade antworten 401 ohne Token.
        if not self._benutzer():
            return self._senden(401, {"fehler": "Anmeldung erforderlich"})
        con = self.con
        m = re.match(r"^/laeufe/(\d+)/vorlage$", pfad)
        if m:
            lauf_id = int(m.group(1))
            g = con.execute("SELECT nummer, grund, kandidaten, masse FROM generationen WHERE lauf_id=? AND status='vorgelegt'", (lauf_id,)).fetchone()
            if not g:
                return self._senden(200, {"generation": None, "kandidaten": []})
            gew = (lj(g["kandidaten"]) or {}).get("_gewaehlt") or {}
            ks = []
            for b, kid in gew.items():
                k = con.execute("SELECT id, bereich, nische, modell, begruendung, diff, masse, wirkungskreis FROM kandidaten WHERE id=?", (kid,)).fetchone()
                km = lj(k["masse"]) or {}
                ks.append({"id": k["id"], "bereich": k["bereich"], "nische": k["nische"], "modell": k["modell"], "begruendung": k["begruendung"], "diff": k["diff"],
                           "urteil": km.get("_urteil_f2"), "anklaeger": {kk: km.get(kk) for kk in ("angriff", "tests_neu", "tests_offen", "norm", "doppelungen", "vertrag_verletzt", "wirkungskreis") if km.get(kk) is not None},
                           "geschmack": gedaechtnis.geschmack_vorhersage(con, kid)})
            gm = lj(g["masse"]) or {}
            return self._senden(200, {"generation": {"nummer": g["nummer"], "grund": g["grund"], "generalprobe": gm.get("_urteil_f2")}, "kandidaten": ks})
        m = re.match(r"^/laeufe/(\d+)/entropie$", pfad)
        if m:
            return self._senden(200, {"verlauf": entropie.verlauf(con, int(m.group(1))), "saettigung": entropie.saettigung(con, int(m.group(1)))})
        m = re.match(r"^/laeufe/(\d+)/mentor$", pfad)
        if m:
            mentor._tabelle(con)
            z = con.execute("SELECT * FROM mentor WHERE lauf_id=? ORDER BY id DESC LIMIT 1", (m.group(1),)).fetchone()
            if not z:
                return self._senden(200, {"richtungen": []})
            d = dict(z); d["richtungen"] = lj(d["richtungen"])
            return self._senden(200, d)
        m = re.match(r"^/laeufe/(\d+)/immunsystem$", pfad)
        if m:
            lz = con.execute("SELECT werk_id FROM laeufe WHERE id=?", (m.group(1),)).fetchone()
            return self._senden(200, _rows(con, "SELECT bereich, name, status, generation, lauf_id, substr(ursprung,1,200) ursprung FROM immunsystem WHERE werk_id=? ORDER BY id", (lz["werk_id"],)) if lz else [])
        m = re.match(r"^/laeufe/(\d+)/verfassung$", pfad)
        if m:
            lz = con.execute("SELECT werk_id FROM laeufe WHERE id=?", (m.group(1),)).fetchone()
            v = verfassung.lesen(con, lz["werk_id"]) if lz else None
            return self._senden(200, {k: v[k] for k in ("text", "quelle", "regeln", "bestaetigt_von", "eingelegt_am") if v and k in v} if v else {})
        m = re.match(r"^/laeufe$", pfad)
        if m:
            return self._senden(200, _rows(con, "SELECT id, werk_id, budget_eur, status, begonnen_am, beendet_am, grund FROM laeufe"))
        m = re.match(r"^/laeufe/(\d+)$", pfad)
        if m:
            z = con.execute("SELECT * FROM laeufe WHERE id=?", (m.group(1),)).fetchone()
            if not z:
                return self._senden(404, {"fehler": "Lauf unbekannt"})
            d = dict(z); d["mass"] = lj(d["mass"]); d["kasse"] = kasse.stand(con, int(m.group(1)))
            return self._senden(200, d)
        m = re.match(r"^/laeufe/(\d+)/generationen$", pfad)
        if m:
            out = []
            for z in _rows(con, "SELECT nummer, status, grund, tag, pruefsumme, erstellt_am, freigabe_am, freigabe_grund, masse FROM generationen WHERE lauf_id=? ORDER BY nummer", (m.group(1),)):
                mm = lj(z.pop("masse"))
                z["kernmass"] = mm["kernmass"] if mm else None
                z["bereiche"] = {b: {k: v for k, v in bm.items() if not isinstance(v, (list, dict))} for b, bm in mm["bereiche"].items()} if mm else None
                out.append(z)
            return self._senden(200, out)
        m = re.match(r"^/laeufe/(\d+)/kandidaten$", pfad)
        if m:
            return self._senden(200, _rows(con, "SELECT id, generation, bereich, nische, anbieter, modell, status, grund, begruendung, wirkungskreis, erstellt_am FROM kandidaten WHERE lauf_id=? ORDER BY id", (m.group(1),)))
        m = re.match(r"^/laeufe/(\d+)/kasse$", pfad)
        if m:
            return self._senden(200, {"stand": kasse.stand(con, int(m.group(1))), "aufrufe": _rows(con, "SELECT * FROM kasse WHERE lauf_id=? ORDER BY id", (m.group(1),))})
        m = re.match(r"^/laeufe/(\d+)/lazarus$", pfad)
        if m:
            return self._senden(200, _rows(con, "SELECT generation, tag, pruefsumme, archiv, erstellt_am FROM lazarus WHERE lauf_id=? ORDER BY generation", (m.group(1),)))
        if pfad == "/werke":
            return self._senden(200, _rows(con, "SELECT id, name, pfad, quelle, aufgenommen_am, sprache, status FROM werke"))
        m = re.match(r"^/werke/(\d+)/landkarte$", pfad)
        if m:
            wid = m.group(1)
            return self._senden(200, {
                "stufen": [{**z, "inhalt": lj(z["inhalt"])} for z in _rows(con, "SELECT stufe, schluessel, inhalt, pruefsumme, herkunft FROM landkarte WHERE werk_id=? ORDER BY stufe, schluessel", (wid,))],
                "strassen": _rows(con, "SELECT von, nach, art FROM strassen WHERE werk_id=? ORDER BY von, nach", (wid,)),
                "vertraege": _rows(con, "SELECT bereich, text, herkunft, quelle FROM vertraege WHERE werk_id=? ORDER BY bereich, id", (wid,)),
            })
        if pfad == "/protokoll":
            mq = re.search(r"limit=(\d+)", self.path)
            return self._senden(200, protokoll.lesen(con, 0, None, min(int(mq.group(1)), 500) if mq else 200))
        return self._senden(404, {"fehler": "unbekannt"})


def starten(host: str = "127.0.0.1", port: int = 8642):
    Handler.con = verbinden()
    srv = HTTPServer((host, port), Handler)
    print(f"Biotop-Dienst auf {host}:{port} — {len(ROUTEN)} Routen, Anmeldezwang aktiv", flush=True)
    srv.serve_forever()


def main(port: int = 8642):
    starten("127.0.0.1", port)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8642)
