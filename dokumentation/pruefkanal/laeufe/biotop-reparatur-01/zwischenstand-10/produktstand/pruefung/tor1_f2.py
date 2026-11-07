"""Tor 1 Zeilen 1–4 (Fassung 2) für einen Nachlauf auswerten. Aufruf: tor1_f2.py <lauf_id> <ausgaben-dir>"""
import json, subprocess, sys, tarfile, tempfile
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.kern import befundklassen, messgeraet, protokoll
from biotop.organe import kammer
from biotop import lauf as L

LAUF = int(sys.argv[1]); A = Path(sys.argv[2])
con = verbinden()
lauf = L._lauf(con, LAUF); werk = L._werk(con, lauf["werk_id"]); wid = werk["id"]; pfad = Path(werk["pfad"])
print(f"# Tor 1 Zeilen 1–4 (Maß Fassung 2) — Lauf {LAUF}, Werk {werk['name']} (werk_id {wid})"); print("Zeit:", protokoll.jetzt())

print("\n## Zeile 1 — Landkarte")
ber = [r[0] for r in con.execute("SELECT DISTINCT schluessel FROM landkarte WHERE werk_id=? AND stufe=1 ORDER BY 1", (wid,))]
n_b = con.execute("SELECT COUNT(*) FROM strassen WHERE werk_id=?", (wid,)).fetchone()[0]
n_h = len(Path("/var/pruefkanal/oeffentlich/_akte/3qfc8gxpdvjsqxcbuj39mupe92a82agy/laeufe/biotop-phase-1/ausgaben/12-strassen-hermes-grep.txt").read_text().splitlines())
print(f"Bereiche: {ber} → {len(ber)} von 4; Straßen: Biotop {n_b} von Hermes-Zählung {n_h} (grep-Liste aus Phase 1, Werk-Commit 058b33e unverändert)")

print("\n## Zeile 2 — Schwächen (Fassung 2: behoben = Befund tritt nicht mehr ein; S1 zusätzlich: statischer Befund weg + Umgehungs-Immuntest im Werk)")
gens = [dict(r) for r in con.execute("SELECT nummer, status, masse, tag FROM generationen WHERE lauf_id=? ORDER BY nummer", (LAUF,))]
ang = [g for g in gens if g["status"] == "angenommen"]
m0 = lj(ang[0]["masse"]); mN = lj(ang[-1]["masse"])
print(f"Generationen gestartet: {len(gens)-1}, angenommen: {len(ang)-1} {[g['nummer'] for g in ang[1:]]}, abgelehnt: {len(gens)-len(ang)}")
def hat(pat, datei):
    return subprocess.run(["grep", "-c", pat, f"{pfad}/{datei}"], capture_output=True, text=True).stdout.strip() or "0"
# Endwerk in der Kammer: kompletter Testlauf + Befundklassen-Umgehungen
e = kammer.ausfuehren(pfad, ["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=no"], zeitlimit_s=120)
tail = e.stdout.strip().splitlines()[-1] if e.stdout.strip() else ""
print(f"Endwerk-Testlauf in der Kammer: {tail}")
regeln = json.load(open("/root/biotop/verfassungen/lagerhaus.regeln.json"))["einstiege"]["B307"]["formeln"]
bk_code = befundklassen.immuntest_code("B307", regeln["import"], regeln["aufruf"], regeln["fehler_import"], regeln["fehler"])
e2 = kammer.ausfuehren(pfad, ["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=line", "tests/_probe_B307.py"], zeitlimit_s=60, dateien={"tests/_probe_B307.py": bk_code})
bk_tail = e2.stdout.strip().splitlines()[-1] if e2.stdout.strip() else ""
f0, fN = m0["bereiche"]["formeln"], mN["bereiche"]["formeln"]
im_werk_bk = (pfad / "tests" / "test_formeln_immun_befundklasse_B307.py").exists()
eval_im_werk = hat("eval(", "lagerhaus/formeln/auswertung.py")
s1 = fN["sicherheit_punkte"] == 0 and im_werk_bk and "passed" in bk_tail and "failed" not in bk_tail
print(f"S1 Sicherheitslücke (formeln, eval): bandit-Punkte {f0['sicherheit_punkte']} → {fN['sicherheit_punkte']} (Befunde jetzt: {fN['sicherheit_befunde']}); 'eval(' im Quelltext: {eval_im_werk} Treffer; Befundklassen-Immuntest im Werk: {im_werk_bk}; Umgehungen am Endwerk frisch ausgeführt: {bk_tail} → {'BEHOBEN (verschwunden + Umgehungen abgewiesen)' if s1 else 'NICHT BEHOBEN'}")
l0, lN = m0["bereiche"]["lager"]["laufzeit_ms"], mN["bereiche"]["lager"]["laufzeit_ms"]
s2 = hat("self._bestand", "lagerhaus/lager/bestand.py") != "0"
print(f"S2 Leistungsbremse (lager, Bestand aus Journal O(n²)): laufzeit lager {l0} → {lN} ms; Bestandsführung geändert: {s2} → {'BEHOBEN' if s2 and lN < l0*0.5 else 'NICHT BEHOBEN'}")
s3 = hat("self._reserviert\\[artikel\\] = self.reserviert(artikel) - menge", "lagerhaus/lager/bestand.py") != "0"
probe3 = kammer.ausfuehren(pfad, ["python", "-c", "from lagerhaus.lager import Lager\nl=Lager(); l.zugang('A',10); l.reservieren('A',5); l.reservierung_einloesen('A',5); print('reserviert_nach_einloesen=', l.reserviert('A'))"], zeitlimit_s=30)
print(f"S3 Vertragsverletzung (Reservierung nach Einlösen): Fix im Code: {s3}; Probe am Endwerk: {probe3.stdout.strip()} → {'BEHOBEN' if 'reserviert_nach_einloesen= 0' in probe3.stdout else 'NICHT BEHOBEN'}")
t0, tN = m0["bereiche"]["preise"]["tote_funktionen"], mN["bereiche"]["preise"]["tote_funktionen"]
print(f"S4 Toter Code (preise): tote_funktionen {t0} → {tN}; '_alte_rabattlogik' im Werk: {hat('_alte_rabattlogik', 'lagerhaus/preise/rabatt.py')} Treffer → {'BEHOBEN' if tN == 0 else 'NICHT BEHOBEN'}")
probe5 = kammer.ausfuehren(pfad, ["python", "-c", "from lagerhaus.preise import Artikel, Katalog, Staffel\nk=Katalog(); k.aufnehmen(Artikel('A','a',1.0,[Staffel(10,0.5)])); print('preis_bei_10=', k.preis_fuer('A',10))"], zeitlimit_s=30)
print(f"S5 Randbedingung (Staffel inklusiv): '>=' im Code: {hat('menge >= staffel.ab_menge', 'lagerhaus/preise/katalog.py')}; Probe am Endwerk: {probe5.stdout.strip()} (Soll 5.0) → {'BEHOBEN' if 'preis_bei_10= 5.0' in probe5.stdout else 'NICHT BEHOBEN'}")
k0, kN = messgeraet.kernmass_f2(m0), messgeraet.kernmass_f2(mN)
print(f"Kernmaß F2 (je Generation mit eigenem Testbestand): Gen 0 = {k0}, Gen {ang[-1]['nummer']} = {kN}")

print("\n## Zeile 3 — Kein Rückschritt (paarweise, Pareto-Maße + Grenzmaße gegen Ausgang)")
rs = 0
for g in ang[1:]:
    m = lj(g["masse"]); u = m.get("_urteil_f2") or {}
    bp = m.get("_basis_paar") or {}
    print(f"Gen {g['nummer']}: Kernmaß paarweise {u.get('kern_basis')} → {u.get('kern_kandidat')} (+{u.get('zuwachs')}); Pareto schlechter: {u.get('pareto_schlechter') or 'nichts'}; Grenzen gerissen: {u.get('grenzen_gerissen') or 'keine'}; Testbestand {len(m.get('_testbestand') or [])} Dateien")
    rs += bool(u.get("pareto_schlechter")) or bool(u.get("grenzen_gerissen"))
print("Rohwerte je angenommene Generation (Bereich: fehl/sicherheit/tot/laufzeit_ms/groesste_fn):")
for g in ang:
    m = lj(g["masse"]); print(f"  Gen {g['nummer']}: " + "; ".join(f"{b}: {x['tests_fehlgeschlagen']}/{x['sicherheit_punkte']}/{x['tote_funktionen']}/{x['laufzeit_ms']}/{x['groesste_funktion']}" for b, x in m["bereiche"].items()))
print(f"ERGEBNIS Zeile 3: in {rs} von {len(ang)-1} angenommenen Generationen ein Pareto-Maß gesunken oder Grenzmaß gerissen")

print("\n## Zeile 4 — Halluzinationsprobe (bericht)")
kb = [dict(r) for r in con.execute("SELECT id, generation, modell, status, grund FROM kandidaten WHERE lauf_id=? AND bereich='bericht' ORDER BY id", (LAUF,))]
for k in kb: print(f"  K{k['id']} Gen {k['generation']} {k['modell'].split('/')[1]}: {k['status']} — {k['grund'][:100]}")
n_ang = sum(1 for k in kb if k["status"] == "angenommen")
d = subprocess.run(["git", "diff", "--stat", f"lauf{LAUF}-gen0", "HEAD", "--", "lagerhaus/bericht"], cwd=pfad, capture_output=True, text=True).stdout.strip()
print(f"ERGEBNIS Zeile 4: {n_ang} von {len(kb)} Kandidaten im Bereich bericht angenommen; git diff gen0..HEAD -- lagerhaus/bericht: '{d or 'leer (0 Dateien geändert)'}'")
