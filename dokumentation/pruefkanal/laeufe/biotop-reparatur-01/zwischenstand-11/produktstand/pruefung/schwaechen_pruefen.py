"""Prüft die drei versiegelten Schwächen von logmuehle gegen den Endstand des Werks (Lauf 17) —
ohne Annahme, je mit Ausgabe. Aufruf: schwaechen_pruefen.py <ausgaben-dir>"""
import subprocess, sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj

A = Path(sys.argv[1])
con = verbinden()
w = Path(con.execute("SELECT pfad FROM werke WHERE id=15").fetchone()[0])
m_a = lj(con.execute("SELECT masse FROM lazarus WHERE lauf_id=17 AND generation=0").fetchone()["masse"])
m_e = lj(con.execute("SELECT masse FROM lazarus WHERE lauf_id=17 ORDER BY generation DESC LIMIT 1").fetchone()["masse"])
z = ["# Die drei versiegelten Schwächen von logmuehle — Ausgang (Lauf 17 Gen 0) gegen Endstand, gemessen"]
for b in ("filtern", "zaehlen", "lesen", "ausgabe"):
    a, e = m_a["bereiche"][b], m_e["bereiche"][b]
    z.append(f"{b}: Sicherheitspunkte {a['sicherheit_punkte']} → {e['sicherheit_punkte']} | Testfehlschläge {a['tests_fehlgeschlagen']} → {e['tests_fehlgeschlagen']} | tote Funktionen {a['tote_funktionen']} → {e['tote_funktionen']}")
z.append("")
q = (w / "logmuehle/filtern/extern.py").read_text()
z.append(f"W1 (Shell-Aufruf in filtern/extern.py): 'shell=True' im Endstand: {'shell=True' in q} | 'subprocess.run' mit Liste: {'subprocess.run(' in q}")
z.append(f"   Ausschnitt: " + " / ".join(l.strip() for l in q.splitlines() if "subprocess" in l or "shell" in l)[:300])
k = (w / "logmuehle/zaehlen/kennzahlen.py").read_text()
z.append(f"W3 (tote Funktion _median_alt): im Endstand vorhanden: {'_median_alt' in k}")
r = subprocess.run(["docker", "run", "--rm", "--network", "none", "-v", f"{w}:/werk:ro", "-w", "/werk",
                    "biotop-kammer:1", "python", "-m", "pytest", "-q", "-p", "no:cacheprovider"], capture_output=True, text=True)
z.append(f"W2 (perzentil an der Kante) — voller Testlauf am Endstand: {r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]}")
z.append(f"Kernmaß F2: Ausgang {m_a.get('kernmass_f2')} → Endstand {m_e.get('kernmass_f2')}")
(A / "97-schwaechen-logmuehle-geprueft.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
