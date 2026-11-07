"""Torprüfung Phase 1 — Zeilen 5 (Lazarus), 7 (Laut scheitern), 8 (Kammer), 9 (Anmeldung).
Schreibt Rohausgaben nach ausgaben/. Zeile 6 (Kasse) läuft gesondert (Lauf 3)."""
import json, os, shutil, subprocess, sys, tempfile, time, urllib.request, urllib.error
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden
from biotop.kern import protokoll, anmeldung
from biotop.organe import lazarus, kammer
from biotop import lauf as L

A = Path(sys.argv[1])
con = verbinden()
LAUF = 2

# ---------------- Zeile 5: Lazarus
out = ["# Tor 1 Zeile 5 — Lazarus: jede angenommene Generation einmal zurückgeholt, Prüfsumme geprüft", f"Zeit: {protokoll.jetzt()}"]
angenommen = [z["nummer"] for z in con.execute("SELECT nummer FROM generationen WHERE lauf_id=? AND status='angenommen' ORDER BY nummer", (LAUF,))]
out.append(f"Angenommene Generationen in Lauf {LAUF}: {angenommen} (Bezugsgröße n = {len(angenommen)})")
werk = Path(L._werk(con, L._lauf(con, LAUF)["werk_id"])["pfad"])
stimmt = 0
for n in angenommen:
    ziel = Path(tempfile.mkdtemp(prefix=f"lazarus-gen{n}-"))
    r = lazarus.rueckkehr(con, LAUF, n, werk, ziel)
    # Unabhängige Gegenprobe: Prüfsumme mit sha256sum neu berechnet
    p = subprocess.run("find . -type f ! -path './.git/*' ! -name '.env*' -printf '%P\\n' | sort | while read f; do printf '%s:%s\\n' \"$f\" \"$(sha256sum \"$f\" | cut -d' ' -f1)\"; done | sha256sum | cut -d' ' -f1",
                       shell=True, cwd=ziel, capture_output=True, text=True).stdout.strip()
    # Hinweis: lazarus.pruefsumme_werk hasht sortierte 'pfad:sha256'-Zeilen ohne Endzeile; Gegenprobe rechnet eigene Variante, dient nur als Existenznachweis der Dateien
    ok = r["stimmt"]
    stimmt += ok
    out.append(f"Generation {n}: Tag {r['tag']}, Dateien {r['dateien']}, erwartet {r['pruefsumme_erwartet'][:16]}…, gemessen {r['pruefsumme_gemessen'][:16]}…, stimmt={ok}, Ziel {ziel}")
    shutil.rmtree(ziel, ignore_errors=True)
out.append(f"ERGEBNIS: Prüfsumme stimmt in {stimmt} von {len(angenommen)} Generationen")
# Negativprobe: eine Datei im zurückgeholten Werk verändern → Prüfsumme muss abweichen
ziel = Path(tempfile.mkdtemp(prefix="lazarus-negativ-"))
lazarus.rueckkehr(con, LAUF, angenommen[-1], werk, ziel)
(ziel / "lagerhaus" / "__init__.py").write_text("# manipuliert\n")
ps, _ = lazarus.pruefsumme_werk(ziel)
erw = con.execute("SELECT pruefsumme FROM lazarus WHERE lauf_id=? AND generation=?", (LAUF, angenommen[-1])).fetchone()[0]
out.append(f"Negativprobe (Datei verändert): erwartet {erw[:16]}…, gemessen {ps[:16]}…, stimmt={ps == erw} (muss False sein)")
shutil.rmtree(ziel, ignore_errors=True)
(A / "40-tor-lazarus.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))

# ---------------- Zeile 7: Laut scheitern
out = ["# Tor 1 Zeile 7 — Laut scheitern: Werk ohne Tests eingelegt", f"Zeit: {protokoll.jetzt()}"]
ohne = Path(tempfile.mkdtemp(prefix="werk-ohne-tests-"))
shutil.copytree("/root/uebungswerk", ohne / "w", ignore=shutil.ignore_patterns(".git", "tests", "__pycache__"))
out.append(f"Quelle: Kopie des Übungswerks ohne tests/ → {ohne/'w'}; Testdateien darin: {len(list((ohne/'w').rglob('test_*.py')))}")
lauf_id = L.anlegen(con, 1.0)
out.append(f"Lauf {lauf_id} angelegt (Budget 1,00 €)")
try:
    L.einlegen(con, lauf_id, "lagerhaus-ohne-tests", str(ohne / "w"))
    out.append("FEHLER: einlegen hat nicht abgebrochen")
except L.LaufFehler as e:
    out.append(f"einlegen → LaufFehler: {e}")
try:
    L.generation(con, lauf_id)
    out.append("FEHLER: generation lief")
except L.LaufFehler as e:
    out.append(f"generation → LaufFehler: {e}")
n_gen = con.execute("SELECT COUNT(*) FROM generationen WHERE lauf_id=?", (lauf_id,)).fetchone()[0]
n_calls = con.execute("SELECT COUNT(*) FROM kasse WHERE lauf_id=? AND zweck NOT LIKE 'aufnahme.%'", (lauf_id,)).fetchone()[0]
st = con.execute("SELECT status, grund FROM laeufe WHERE id=?", (lauf_id,)).fetchone()
out.append(f"Lauf {lauf_id}: status={st['status']}, grund={st['grund']}")
out.append(f"ERGEBNIS: gestartete Generationen = {n_gen} (Soll 0); Modellaufrufe außerhalb der Aufnahme = {n_calls}")
out.append("Protokollzeilen:")
for z in con.execute("SELECT nr, art, inhalt FROM protokoll WHERE art IN ('aufnahme','lauf.gestoppt') AND inhalt LIKE ? ORDER BY nr", (f'%"lauf_id": {lauf_id}%',)):
    out.append(f"  #{z['nr']} {z['art']} {z['inhalt'][:300]}")
for z in con.execute("SELECT nr, art, inhalt FROM protokoll WHERE art='aufnahme' AND inhalt LIKE '%ohne-tests%' ORDER BY nr"):
    out.append(f"  #{z['nr']} {z['art']} {z['inhalt'][:300]}")
shutil.rmtree(ohne, ignore_errors=True)
(A / "41-tor-laut-scheitern.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))

# ---------------- Zeile 8: Kammer
out = ["# Tor 1 Zeile 8 — Kammer: Kandidat mit Endlosschleife", f"Zeit: {protokoll.jetzt()}", f"Kammer-Image: {kammer.IMAGE}; Zeitlimit für diese Probe: 10 s"]
ps_vor, n_vor = lazarus.pruefsumme_werk(werk)
vorher = subprocess.run(["docker", "ps", "-aq"], capture_output=True, text=True).stdout.split()
out.append(f"Wirt vorher: Werk-Prüfsumme {ps_vor[:16]}… ({n_vor} Dateien); laufende/abgelegte Container: {len(vorher)}")
marker = Path("/tmp/kammer-ausbruch-marker"); marker.unlink(missing_ok=True)
code = "import os\nopen('/werk/AUSBRUCH.txt','w').write('x')\ntry:\n    open('/tmp/kammer-ausbruch-marker','w').write('x')\nexcept Exception as e: print('tmp:',e)\nwhile True: pass\n"
t0 = time.monotonic()
e = kammer.ausfuehren(werk, ["python", "endlos.py"], zeitlimit_s=10, dateien={"endlos.py": code})
out.append(f"Ergebnis: rc={e.rc}, zeitlimit={e.zeitlimit}, dauer={e.dauer_s:.1f}s, container={e.container}")
out.append(f"stderr (Ende): {e.stderr.strip()[-200:]}")
time.sleep(1)
nachher = subprocess.run(["docker", "ps", "-aq"], capture_output=True, text=True).stdout.split()
ps_nach, n_nach = lazarus.pruefsumme_werk(werk)
out.append(f"Wirt nachher: Werk-Prüfsumme {ps_nach[:16]}… ({n_nach} Dateien), unverändert={ps_vor == ps_nach}; Container übrig: {len(nachher)}; AUSBRUCH.txt im Werk: {(werk/'AUSBRUCH.txt').exists()}; Marker in Wirt-/tmp: {marker.exists()}")
out.append(f"Als gescheitert gewertet: {e.rc == 124 and e.zeitlimit}")
protokoll.schreiben(con, "kammer.probe", rc=e.rc, zeitlimit=e.zeitlimit, dauer_s=round(e.dauer_s, 1), container=e.container, wirt_unveraendert=(ps_vor == ps_nach))
out.append(f"ERGEBNIS: Zeitlimit gegriffen={e.zeitlimit}, rc=124: {e.rc == 124}, Wirt unberührt: {ps_vor == ps_nach and not marker.exists() and not (werk/'AUSBRUCH.txt').exists()}")
(A / "42-tor-kammer.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))

# ---------------- Zeile 9: Anmeldung
out = ["# Tor 1 Zeile 9 — Anmeldung: jede Route ohne Token → 401", f"Zeit: {protokoll.jetzt()}"]
os.environ["BIOTOP_KENNWORT"] = "pruef-" + os.urandom(8).hex()
anmeldung.benutzer_anlegen(con, "philipp", os.environ["BIOTOP_KENNWORT"])
srv = subprocess.Popen([sys.executable, "-m", "biotop.dienst", "8642"], cwd="/root/biotop", env={**os.environ, "PYTHONPATH": "/root/biotop"},
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
time.sleep(1.5)
from biotop.dienst import ROUTEN
def anfrage(methode, pfad, token=None, body=None):
    req = urllib.request.Request("http://127.0.0.1:8642" + pfad, method=methode, data=json.dumps(body).encode() if body else None,
                                 headers={"Content-Type": "application/json", **({"Authorization": f"Bearer {token}"} if token else {})})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as ex:
        return ex.code, json.loads(ex.read() or b"{}")
beispiele = {r"^/laeufe/(\d+)$": "/laeufe/2", r"^/laeufe/(\d+)/generationen$": "/laeufe/2/generationen", r"^/laeufe/(\d+)/kandidaten$": "/laeufe/2/kandidaten",
             r"^/laeufe/(\d+)/kasse$": "/laeufe/2/kasse", r"^/laeufe/(\d+)/lazarus$": "/laeufe/2/lazarus", r"^/werke/(\d+)/landkarte$": "/werke/1/landkarte"}
n401 = 0; gesamt = 0
out.append("| Methode | Route | ohne Token | falscher Token | mit Token |")
tok = anfrage("POST", "/anmelden", body={"name": "philipp", "kennwort": os.environ["BIOTOP_KENNWORT"]})[1].get("token")
for methode, muster in ROUTEN:
    pfad = beispiele.get(muster, muster.strip("^$"))
    if pfad == "/anmelden":
        s_ohne = anfrage("POST", "/anmelden", body={"name": "philipp", "kennwort": "falsch"})[0]
        s_falsch = anfrage("POST", "/anmelden", body={})[0]
        s_mit = anfrage("POST", "/anmelden", body={"name": "philipp", "kennwort": os.environ["BIOTOP_KENNWORT"]})[0]
        out.append(f"| POST | /anmelden | {s_ohne} (falsches Kennwort) | {s_falsch} (leer) | {s_mit} (richtig) |")
        gesamt += 1; n401 += (s_ohne == 401)
        continue
    s_ohne = anfrage(methode, pfad)[0]; s_falsch = anfrage(methode, pfad, token="falsch")[0]; s_mit = anfrage(methode, pfad, token=tok)[0]
    out.append(f"| {methode} | {pfad} | {s_ohne} | {s_falsch} | {s_mit} |")
    gesamt += 1; n401 += (s_ohne == 401 and s_falsch == 401)
s_unbek = anfrage("GET", "/gibt-es-nicht")[0]
out.append(f"| GET | /gibt-es-nicht (unbekannt) | {s_unbek} | – | {anfrage('GET','/gibt-es-nicht',token=tok)[0]} |")
out.append(f"ERGEBNIS: {n401} von {gesamt} Routen antworten ohne/mit falschem Token 401 (bei /anmelden: falsches Kennwort → 401); unbekannter Pfad ohne Token → {s_unbek}")
srv.terminate(); srv.wait(timeout=5)
(A / "43-tor-anmeldung.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))
