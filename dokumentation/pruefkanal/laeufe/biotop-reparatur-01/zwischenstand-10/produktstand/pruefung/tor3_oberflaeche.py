"""Tor 3 — Zeile Oberfläche: Dienst starten, jede Route ohne Token → 401 (Liste), HTML-Seite ohne Daten, Anmeldung,
Kostenstand und Kurve über die Routen sichtbar, Freigabe/Richtung über die Oberflächen-Routen wirksam (Kernstelle).
Aufruf: tor3_oberflaeche.py <ausgaben-dir> <lauf_id>"""
import json, os, subprocess, sys, time, urllib.request, urllib.error
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden
from biotop.kern import anmeldung
from biotop import dienst, oberflaeche

A = Path(sys.argv[1]); LAUF = int(sys.argv[2]); PORT = 8653
out = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)

con = verbinden()
os.environ["BIOTOP_KENNWORT"] = "pruef-" + os.urandom(8).hex()
anmeldung.benutzer_anlegen(con, "philipp", os.environ["BIOTOP_KENNWORT"])
con.close()
env = {**os.environ, "PYTHONPATH": "/root/biotop"}
srv = subprocess.Popen([sys.executable, "-m", "biotop", "dienst", "--port", str(PORT)], cwd="/root/biotop", env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
time.sleep(1.2)

def anfrage(m, pfad, token=None, body=None):
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}{pfad}", method=m, data=json.dumps(body).encode() if body is not None else None)
    req.add_header("Content-Type", "application/json")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read(); ct = r.headers.get("Content-Type", "")
            return r.status, (json.loads(raw) if "json" in ct else raw.decode()), ct
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw), e.headers.get("Content-Type", "")
        except Exception:
            return e.code, raw.decode(errors="replace"), ""

try:
    p("# Tor 3 — Oberfläche: Anmeldezwang, Sichtbarkeit, Wirkung")
    p("Dienst: 127.0.0.1:%d, Routen laut dienst.ROUTEN: %d" % (PORT, len(dienst.ROUTEN)))
    # 1. Jede Route ohne Token
    p("\n1. Jede Route OHNE Token:")
    n401 = 0; gesamt = 0
    wid = verbinden().execute("SELECT werk_id FROM laeufe WHERE id=?", (LAUF,)).fetchone()[0]
    for methode, muster in dienst.ROUTEN:
        pfad = muster.strip("^$").replace("(\\d+)", str(LAUF)).replace("\\", "")
        if "/werke/" in pfad:
            pfad = pfad.replace(f"/werke/{LAUF}", f"/werke/{wid}")
        if pfad == "/anmelden":
            st, body, ct = anfrage("POST", pfad, body={"name": "philipp", "kennwort": "falsch"})
            p(f"   {methode:4s} {pfad:32s} → HTTP {st} (falsches Kennwort; einzige Route ohne Token-Pflicht)"); gesamt += 1; n401 += (st == 401); continue
        if pfad == "/":
            st, body, ct = anfrage("GET", pfad)
            # Datenprobe: echte Werte aus der Datenbank dürfen in der Seite ohne Token nicht vorkommen
            c0 = verbinden(); ps = c0.execute("SELECT pruefsumme FROM generationen WHERE lauf_id=? AND pruefsumme IS NOT NULL LIMIT 1", (LAUF,)).fetchone()
            ks = c0.execute("SELECT diff FROM kandidaten WHERE lauf_id=? AND diff!='' LIMIT 1", (LAUF,)).fetchone(); c0.close()
            hat_daten = (ps and ps[0][:16] in body) or (ks and ks[0][:80] in body) or "verhandlung.bestanden" in body
            p(f"   {methode:4s} {pfad:32s} → HTTP {st} {ct.split(';')[0]} (Anmeldemaske, {len(body)} Zeichen, enthält Daten: {hat_daten}) — Seite ohne Daten, alle Daten-Routen unten 401"); gesamt += 1; n401 += (st == 200 and not hat_daten); continue
        st, body, ct = anfrage(methode, pfad, body={} if methode == "POST" else None)
        p(f"   {methode:4s} {pfad:32s} → HTTP {st}"); gesamt += 1; n401 += (st == 401)
    p(f"   ERGEBNIS: {n401} von {gesamt} Routen antworten ohne Token wie gefordert (401; '/' = Maske ohne Daten; /anmelden = 401 bei falschem Kennwort)")
    # 2. Anmeldung + Sichtbarkeit
    st, body, _ = anfrage("POST", "/anmelden", body={"name": "philipp", "kennwort": os.environ["BIOTOP_KENNWORT"]})
    tok = body.get("token"); p(f"\n2. Anmeldung mit richtigem Kennwort → HTTP {st}, Token erhalten: {bool(tok)}")
    st, k, _ = anfrage("GET", f"/laeufe/{LAUF}/kasse", tok)
    p(f"   Kostenstand (Element #kasse, #kasse-kopf → kern/kasse.py:stand): HTTP {st}, {k['stand']['ausgegeben_eur']:.4f} € von {k['stand']['budget_eur']:.2f} €, {k['stand']['aufrufe']} Aufrufe")
    st, g, _ = anfrage("GET", f"/laeufe/{LAUF}/generationen", tok)
    ang = [x for x in g if x["status"] == "angenommen"]
    p(f"   Kurve (Element #kurve → GET /laeufe/<id>/generationen): HTTP {st}, {len(g)} Generationen, {len(ang)} angenommen mit Maßen je Bereich: {list((ang[-1]['bereiche'] or {}).keys()) if ang else []}")
    for pf in ("vorlage", "entropie", "mentor", "immunsystem", "verfassung", "lazarus", "kandidaten"):
        st, d, _ = anfrage("GET", f"/laeufe/{LAUF}/{pf}", tok)
        p(f"   GET /laeufe/{LAUF}/{pf} → HTTP {st}, {len(d) if isinstance(d, list) else list(d)[:6]}")
    st, d, _ = anfrage("GET", f"/werke/{wid}/landkarte", tok)
    p(f"   GET /werke/{wid}/landkarte → HTTP {st}, Stufen {len(d['stufen'])}, Straßen {len(d['strassen'])}, Verträge {len(d['vertraege'])}")
    # 3. Wirkung: Freigabe-Route ohne wartende Generation → 409 (Kernstelle lauf.freigabe wird erreicht, keine Scheinwirkung)
    st, d, _ = anfrage("POST", f"/laeufe/{LAUF}/freigabe", tok, body={"entscheidung": "frei", "grund": "Probe"})
    p(f"\n3. Wirkung: POST /laeufe/{LAUF}/freigabe ohne wartende Generation → HTTP {st} {d} (Element #freigabe-frei → lauf.py:freigabe; nur wirksam, wenn eine Generation 'vorgelegt' ist)")
    st, d, _ = anfrage("POST", f"/laeufe/{LAUF}/richtung", tok, body={"name": "gibt-es-nicht"})
    p(f"   POST /laeufe/{LAUF}/richtung mit unbekanntem Namen → HTTP {st} {str(d)[:160]} (Element #richtung-waehlen → organe/mentor.py:waehlen)")
    # 4. Belege je Element
    bel = oberflaeche.belege()
    p(f"\n4. Bedienelemente mit Kernstelle (Dateipfad:Zeile): {sum(b['belegt'] for b in bel)} von {len(bel)}")
    for b in bel:
        p(f"   #{b['element']:20s} {b['methode']:4s} {b['route']:32s} HTML-Zeile {b['html_zeile_oberflaeche_py']!s:4s} → {b['kernstelle']:40s} {b['wirkung']}")
    (A / "70-tor3-oberflaeche-belege.json").write_text(json.dumps(bel, ensure_ascii=False, indent=1))
finally:
    srv.terminate(); srv.wait(timeout=5)
(A / "70-tor3-oberflaeche.txt").write_text("\n".join(out) + "\n")
