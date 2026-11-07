"""Tor 2 — Auswertung der Zeilen, die aus dem Hauptlauf kommen: Nischen/Bandit, S2, Immunisierung/Doppelungen/rote Tests,
Verhandlung, Kurve. Aufruf: tor2.py <lauf_id> <ausgaben-dir>"""
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.kern import protokoll, messgeraet
from biotop.organe import kammer, nischen
from biotop import lauf as L

LAUF = int(sys.argv[1]); A = Path(sys.argv[2])
con = verbinden()
lauf = L._lauf(con, LAUF); werk = L._werk(con, lauf["werk_id"]); wid = werk["id"]; pfad = Path(werk["pfad"])
mass = lj(lauf["mass"]); bereiche = mass["bereiche"]
gens = [dict(r) for r in con.execute("SELECT nummer, status, masse, grund, kandidaten FROM generationen WHERE lauf_id=? ORDER BY nummer", (LAUF,))]
ang = [g for g in gens if g["status"] == "angenommen"]
out = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

p(f"# Tor 2 — Auswertung Hauptlauf {LAUF} ({werk['name']}, werk_id {wid})"); p("Zeit:", protokoll.jetzt())
p(f"Generationen gestartet: {len(gens)-1}; angenommen: {len(ang)-1} {[g['nummer'] for g in ang[1:]]}; abgelehnt: {len(gens)-len(ang)}")

# ---- Nischen & Bandit
p("\n## Zeile 1 — Nischen: 4 aktiv, je ≥ 2 Anbieter; Bandit-Gewichte nach 10 Generationen")
n_gen = gens[-1]["nummer"]
for n in nischen.NISCHEN:
    hers = [r[0] for r in con.execute("SELECT DISTINCT substr(modell,1,instr(modell,'/')-1) FROM kandidaten WHERE lauf_id=? AND nische=? AND status NOT LIKE 'probe%'", (LAUF, n))]
    cnt = con.execute("SELECT COUNT(*), SUM(status IN ('ueberlebt','angenommen')) FROM kandidaten WHERE lauf_id=? AND nische=? AND status NOT LIKE 'probe%' AND status<>'verhandlung'", (LAUF, n)).fetchone()
    p(f"  {n:8} Hersteller genutzt: {sorted(hers)} ({len(hers)} von 4) | Kandidaten {cnt[0]}, überlebt/angenommen {cnt[1] or 0}")
gw = nischen.gewichte(con, LAUF)
p(f"Bandit-Gewichte nach Generation {n_gen} (Beta-Erwartungswert (erfolge+1)/(versuche+2); Protokoll 'bandit.wahl' je Wahl):")
for n, hs in gw.items():
    p(f"  {n:8} " + "; ".join(f"{h}: {v['erfolge']}/{v['versuche']} → {v['gewicht']}" for h, v in sorted(hs.items())))
n_ok = sum(1 for n in nischen.NISCHEN if len({r[0].split('/')[0] for r in con.execute('SELECT modell FROM kandidaten WHERE lauf_id=? AND nische=?', (LAUF, n))}) >= 2)
p(f"ERGEBNIS Zeile 1: {n_ok} von 4 Nischen mit ≥ 2 Herstellern; Gewichte nach {n_gen} Generationen protokolliert ({'ja' if n_gen >= 10 else 'NEIN, erst ' + str(n_gen)})")
gwz = [dict(lj(z["inhalt"]), nr=z["nr"]) for z in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='bandit.wahl' AND inhalt LIKE ?", (f'%"lauf_id": {LAUF},%',))]
p(f"bandit.wahl-Protokollzeilen: {len(gwz)}")
(A / "60-tor2-nischen-bandit.txt").write_text("\n".join(out) + "\n"); out.clear()

# ---- S2
p("# Tor 2 — Zeile 3: S2 (Leistungsbremse) nach dem Kriterium der versiegelten Liste")
m0 = lj(ang[0]["masse"]); mN = lj(ang[-1]["masse"])
l0, lN = m0["bereiche"]["lager"]["laufzeit_ms"], mN["bereiche"]["lager"]["laufzeit_ms"]
best = (pfad / "lagerhaus/lager/bestand.py").read_text(); jour = (pfad / "lagerhaus/lager/journal.py").read_text()
krit_a = ("summe_fuer" not in best.split("def bestand")[1].split("def ")[0]) or ("_summen" in jour or "_bestand" in best)
p(f"Kriterium (a) — bestand() summiert nicht mehr das ganze Journal je Lesen: {'erfüllt' if krit_a else 'NICHT erfüllt'}")
p("  bestand():", best.split("def bestand")[1].split("def ")[0].strip().replace("\n", " ")[:160])
p("  journal.summe_fuer():", jour.split("def summe_fuer")[1].split("def ")[0].strip().replace("\n", " ")[:160])
p(f"Kriterium (b) — Laufzeit last_lager um ≥ 50 % gesunken: Ausgang {l0} ms → Ende {lN} ms = {(1 - lN / l0) * 100:.1f} % {'erfüllt' if lN <= l0 * 0.5 else 'NICHT erfüllt'}")
# frische Gegenmessung Ausgang vs Ende (3 Messungen je, in der Kammer)
import tarfile, tempfile
ref = L._referenzlast(werk["name"], mass["paket"])
tmp = Path(tempfile.mkdtemp()); tarfile.open(con.execute("SELECT archiv FROM lazarus WHERE lauf_id=? AND generation=0", (LAUF,)).fetchone()[0]).extractall(tmp, filter="data")
frisch = []
for name, w in (("Ausgang", tmp), ("Ende", pfad)):
    ls = []
    for _ in range(3):
        m = messgeraet.messen(w, bereiche, mass["paket"], ref)
        ls.append(m["bereiche"]["lager"]["laufzeit_ms"])
    frisch.append((name, ls))
p("Frische Gegenmessung lager.laufzeit_ms (3× je Stand, Kammer):", frisch)
kern0, kernN = messgeraet.kernmass_f2(m0), messgeraet.kernmass_f2(mN)
p(f"Kernmaß F2 Ausgang {kern0} → Ende {kernN} (Nischenmaß: unverändert oder gestiegen → {'ja' if kernN >= kern0 else 'NEIN'})")
p(f"ERGEBNIS Zeile 3: S2 {'BEHOBEN' if krit_a and lN <= l0 * 0.5 and kernN >= kern0 else 'NICHT behoben'} — {l0} → {lN} ms ({(1 - lN / l0) * 100:.0f} %), Kernmaß {kern0} → {kernN}")
(A / "61-tor2-s2.txt").write_text("\n".join(out) + "\n"); out.clear()

# ---- Immunisierung / Doppelungen / rote Tests
p("# Tor 2 — Zeile 8: Immunisierung — n bestätigte Fehler = n Tests im Werk; Doppelungsanteil < 20 %; nach keiner angenommenen Generation ein roter Test")
im = [dict(r) for r in con.execute("SELECT name, bereich, status, ursprung FROM immunsystem WHERE werk_id=? ORDER BY id", (wid,))]
im_werk = [x for x in im if x["status"] == "im_werk"]
dateien = sorted(str(f.relative_to(pfad)) for f in (pfad / "tests").glob("test_*_immun_*.py"))
p(f"Immunsystem-Einträge: {len(im)} — im_werk {len(im_werk)}, offen {sum(1 for x in im if x['status'] in ('offen','gefunden'))}, offen_norm {sum(1 for x in im if x['status']=='offen_norm')}")
p(f"Immuntest-Dateien im Werk (git): {len(dateien)}")
for f in dateien: p("  ", f)
# Doppelungen aus Protokoll
d_ges = 0; d_dop = 0; d_norm = 0
for z in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' AND inhalt LIKE ?", (f'%"lauf_id": {LAUF},%',)):
    d = lj(z["inhalt"]); a = d.get("angriff") or {}
    if isinstance(a, dict) and "gesamt" in a:
        d_ges += a.get("gesamt", 0); d_dop += len(d.get("doppelungen") or []); d_norm += len(d.get("norm") or [])
p(f"Angriffstests gesamt (Lauf {LAUF}): {d_ges}; als Doppelung gekennzeichnet: {d_dop} → Anteil {100 * d_dop / max(1, d_ges):.1f} % (Soll < 20 %); als Norm (offen, 0 Punkte): {d_norm}")
# rote Tests je angenommener Generation: aus Lazarus holen und Testlauf
rot = []
for g in ang:
    arch = con.execute("SELECT archiv FROM lazarus WHERE lauf_id=? AND generation=?", (LAUF, g["nummer"])).fetchone()[0]
    t = Path(tempfile.mkdtemp()); tarfile.open(arch).extractall(t, filter="data")
    e = kammer.ausfuehren(t, ["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=no"], zeitlimit_s=120)
    tail = e.stdout.strip().splitlines()[-1] if e.stdout.strip() else "?"
    rot.append((g["nummer"], tail, e.rc))
    p(f"  Gen {g['nummer']}: {tail}")
p(f"ERGEBNIS Zeile 8: rote Tests nach angenommenen Generationen: {sum(1 for _, _, rc in rot if rc != 0)} von {len(rot)}; Doppelungsanteil {100 * d_dop / max(1, d_ges):.1f} %; Immuntests im Werk {len(dateien)} (Einträge im_werk {len(im_werk)})")
(A / "62-tor2-immunisierung.txt").write_text("\n".join(out) + "\n"); out.clear()

# ---- Verhandlung
p("# Tor 2 — Zeile 9: Verhandlung — mindestens 1 Generation, in der zwei Bereiche eine Vertragsänderung gemeinsam bestanden")
vh = [dict(lj(z["inhalt"]), art=z["art"], nr=z["nr"]) for z in con.execute("SELECT nr, art, inhalt FROM protokoll WHERE art LIKE 'verhandlung.%' AND inhalt LIKE ? ORDER BY nr", (f'%"lauf_id": {LAUF},%',))]
for v in vh: p("  ", v["nr"], v["art"], {k: v[k] for k in v if k not in ("art", "nr", "lauf_id")})
best_vh = [v for v in vh if v["art"] == "verhandlung.bestanden"]
p(f"ERGEBNIS Zeile 9: {len(best_vh)} Verhandlungen bestanden (Generationen {[v['generation'] for v in best_vh]}); begonnen {sum(1 for v in vh if v['art']=='verhandlung.begonnen')}, gescheitert {sum(1 for v in vh if v['art']=='verhandlung.gescheitert')}")
(A / "63-tor2-verhandlung.txt").write_text("\n".join(out) + "\n"); out.clear()

# ---- Verlaufskurve
p("# Tor 2 — Zeile 10: Verlaufskurve des Hauptlaufs mit Endtestbestand (3.5 F3)")
k = L.kurve_nachrechnen(con, LAUF)
p(f"Endtestbestand: {len(k['testbestand'])} Dateien aus {k['testbestand_aus']}")
p("| Gen | Tests eigen | F2 (eigene Tests) | F2 (Endtestbestand) | fehl / sicherheit / tot (Endtests, je Bereich) | Laufzeit ms (b/f/l/p) |")
p("|---|---|---|---|---|---|")
for z in k["kurve"]:
    b = z["bereiche_endtests"] or {}
    p(f"| {z['generation']} | {z['tests_eigen']} | {z['f2_eigen']} | {z['f2_endtests']} | " + "; ".join(f"{n}: {x['tests_fehlgeschlagen']}/{x['sicherheit_punkte']}/{x['tote_funktionen']}" for n, x in b.items()) + " | " + "/".join(str(b[n]["laufzeit_ms"]) for n in ("bericht", "formeln", "lager", "preise") if n in b) + " |")
(A / "64-tor2-kurve.txt").write_text("\n".join(out) + "\n"); (A / "64-tor2-kurve.json").write_text(json.dumps(k, ensure_ascii=False, indent=1))
