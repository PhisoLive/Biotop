"""Prüft die Sperre „Probenkandidaten kommen in kein Gedächtnis" (Fassung 6, Festlegung Chat-Claude)
und räumt den Altbestand aus Phase 3 aus (die Sperre gab es damals nicht).

Fall 1: Altbestand — welche Probenkandidaten liegen in den drei Gedächtnissen? Werden entfernt, protokolliert.
Fall 2: Ein Probenkandidat wird allen drei Gedächtnissen angeboten → keines nimmt ihn, je eine Protokollzeile.
Fall 3: Ein echter Kandidat wird angeboten → wird aufgenommen (die Sperre trifft nur Proben).
Fall 4: Sichtbarkeit — der Probenkandidat steht weiter in `kandidaten` und ist im Bericht auffindbar.
Aufruf: proben_ausserhalb_gedaechtnis.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern import protokoll
from biotop.kern.datenbank import verbinden, transaktion
from biotop.organe import gedaechtnis as G

A = Path(sys.argv[1])
con = verbinden()
G.tabellen(con)
z = ["# Probenkandidaten kommen in kein Gedächtnis (Fassung 6)"]

# --- Fall 1: Altbestand aus Phase 3 ausräumen
z.append("\n## Fall 1: Altbestand aus Phase 3 (Sperre gab es damals nicht)")
alt = [dict(x) for x in con.execute(
    "SELECT id, lauf_id, kandidat_id, bereich, nische FROM projektgedaechtnis WHERE nische LIKE 'probe%' OR bereich LIKE 'probe%'")]
for a in alt:
    z.append(f"  projektgedaechtnis #{a['id']}: Lauf {a['lauf_id']}, K{a['kandidat_id']}, {a['bereich']}/{a['nische']}")
if alt:
    with transaktion(con):
        con.execute("DELETE FROM projektgedaechtnis WHERE nische LIKE 'probe%' OR bereich LIKE 'probe%'")
    protokoll.schreiben(con, "gedaechtnis.probenabfall_entfernt", anzahl=len(alt), gedaechtnis="projekt",
                        eintraege=[f"K{a['kandidat_id']} ({a['bereich']}/{a['nische']}, Lauf {a['lauf_id']})" for a in alt],
                        grund="Fassung 6: Probenkandidaten gehören in kein Gedächtnis; Altbestand aus Phase 3 entfernt")
art_rest = con.execute("SELECT COUNT(*) FROM artgedaechtnis WHERE nische LIKE 'probe%' OR bereich LIKE 'probe%'").fetchone()[0]
ges_rest = con.execute("SELECT COUNT(*) FROM geschmack WHERE kandidat_id IN "
                       "(SELECT id FROM kandidaten WHERE nische LIKE 'probe%' OR bereich LIKE 'probe%')").fetchone()[0]
z.append(f"  entfernt: {len(alt)} Einträge aus projektgedaechtnis | artgedaechtnis-Rest: {art_rest} | geschmack-Rest: {ges_rest}")

# --- Fall 2: Probenkandidat allen drei Gedächtnissen anbieten
probe_id = con.execute("SELECT id FROM kandidaten WHERE nische LIKE 'probe%' AND status='abgelehnt' AND diff!='' ORDER BY id DESC LIMIT 1").fetchone()
echt_id = con.execute("SELECT id FROM kandidaten WHERE lauf_id=20 AND nische NOT LIKE 'probe%' AND status='abgelehnt' AND diff!='' ORDER BY id DESC LIMIT 1").fetchone()
werk = Path(con.execute("SELECT pfad FROM werke WHERE id=18").fetchone()[0])
vor = {t: con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in ("projektgedaechtnis", "artgedaechtnis", "geschmack")}

z.append("\n## Fall 2: Probenkandidat wird allen drei Gedächtnissen angeboten")
if probe_id:
    k = dict(con.execute("SELECT id, bereich, nische, status FROM kandidaten WHERE id=?", (probe_id[0],)).fetchone())
    z.append(f"  angeboten: K{k['id']} ({k['bereich']}/{k['nische']}, Status {k['status']})")
    G.projekt_merken(con, 18, 20, k["id"], werk)
    G.art_merken(con, 18, 20, k["id"], "abgelehnt")
    G.geschmack_merken(con, 18, 20, 0, k["id"], "abgelehnt", "Probe", "Hermes", quelle="probe")
    nach = {t: con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in vor}
    for t in vor:
        z.append(f"  {t}: {vor[t]} → {nach[t]} (Zuwachs {nach[t]-vor[t]}, gefordert 0)")
    p = [dict(x) for x in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='gedaechtnis.probe_uebersprungen' ORDER BY nr DESC LIMIT 3")]
    for x in reversed(p):
        z.append(f"  Protokoll #{x['nr']}: {x['inhalt'][:150]}")
else:
    z.append("  KEIN Probenkandidat mit Diff gefunden — Prüfung nicht durchführbar")

# --- Fall 3: echter Kandidat wird aufgenommen
z.append("\n## Fall 3: echter Kandidat (Gegenprobe — die Sperre trifft nur Proben)")
if echt_id:
    vor2 = con.execute("SELECT COUNT(*) FROM projektgedaechtnis").fetchone()[0]
    k2 = dict(con.execute("SELECT id, bereich, nische FROM kandidaten WHERE id=?", (echt_id[0],)).fetchone())
    con.execute("DELETE FROM projektgedaechtnis WHERE kandidat_id=?", (k2["id"],))
    vor2 = con.execute("SELECT COUNT(*) FROM projektgedaechtnis").fetchone()[0]
    G.projekt_merken(con, 18, 20, k2["id"], werk)
    nach2 = con.execute("SELECT COUNT(*) FROM projektgedaechtnis").fetchone()[0]
    z.append(f"  angeboten: K{k2['id']} ({k2['bereich']}/{k2['nische']}) → projektgedaechtnis {vor2} → {nach2} "
             f"(Zuwachs {nach2-vor2}, gefordert 1)")

# --- Fall 4: Sichtbarkeit bleibt
z.append("\n## Fall 4: Proben bleiben sichtbar (Datenbank und Bericht)")
n = con.execute("SELECT COUNT(*) FROM kandidaten WHERE nische LIKE 'probe%' OR bereich LIKE 'probe%'").fetchone()[0]
z.append(f"  Probenkandidaten in `kandidaten`: {n} — unverändert einsehbar, nur die Gedächtnisse lesen sie nicht")
(A / "08-proben-ausserhalb-gedaechtnis.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
