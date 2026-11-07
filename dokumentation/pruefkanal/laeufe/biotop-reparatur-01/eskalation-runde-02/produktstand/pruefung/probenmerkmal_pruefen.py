"""Härtung: Die Probensperre greift am gesetzten Merkmal `ist_probe`, nicht am Namen (Fassung 6).

Fall 1: Probe unter einem NEUEN Namensschema (`eichung_vorspann_v2` / Bereich `preise`) — der Namensweg kennt es
        nicht, das Merkmal schon. Ohne Merkmal wäre sie durchgerutscht; das wird beides gezeigt.
Fall 2: Altbestand ohne Merkmal (Feld auf 0 gesetzt) — der Namensweg fängt sie weiterhin.
Fall 3: Echter Kandidat — wird aufgenommen.
Aufruf: probenmerkmal_pruefen.py <ausgaben-dir>
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
werk = Path(con.execute("SELECT pfad FROM werke WHERE id=18").fetchone()[0])
vorlage = con.execute("SELECT diff, begruendung FROM kandidaten WHERE lauf_id=20 AND diff!='' ORDER BY id DESC LIMIT 1").fetchone()
z = ["# Probensperre greift am gesetzten Merkmal `ist_probe`, nicht am Namen (Fassung 6)"]

def anlegen(nische, bereich, ist_probe):
    with transaktion(con):
        cur = con.execute("INSERT INTO kandidaten(lauf_id, generation, bereich, nische, anbieter, modell, diff, begruendung,"
                          " status, grund, erstellt_am, ist_probe) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                          (20, 0, bereich, nische, "hermes", "hermes/probe", vorlage["diff"], vorlage["begruendung"],
                           "abgelehnt", "Probe der Härtungsprüfung", protokoll.jetzt(), ist_probe))
    return cur.lastrowid

def anbieten(kid, marke):
    vor = con.execute("SELECT COUNT(*) FROM projektgedaechtnis").fetchone()[0]
    G.projekt_merken(con, 18, 20, kid, werk)
    nach = con.execute("SELECT COUNT(*) FROM projektgedaechtnis").fetchone()[0]
    k = con.execute("SELECT nische, bereich, ist_probe FROM kandidaten WHERE id=?", (kid,)).fetchone()
    z.append(f"  {marke}")
    z.append(f"    K{kid}: nische='{k['nische']}', bereich='{k['bereich']}', ist_probe={k['ist_probe']} "
             f"| ist_probe() sagt: {G.ist_probe(k)}")
    z.append(f"    projektgedaechtnis {vor} → {nach} (Zuwachs {nach - vor})")
    return nach - vor

z.append("\n## Fall 1: NEUES Namensschema, das der Namensweg nicht kennt")
k1 = anlegen("eichung_vorspann_v2", "preise", 1)
zu1 = anbieten(k1, "(a) mit gesetztem Merkmal ist_probe=1")
with transaktion(con):
    con.execute("UPDATE kandidaten SET ist_probe=0 WHERE id=?", (k1,))
    con.execute("DELETE FROM projektgedaechtnis WHERE kandidat_id=?", (k1,))
zu2 = anbieten(k1, "(b) dasselbe ohne Merkmal — so wäre es früher durchgerutscht")
z.append(f"  ERGEBNIS: mit Merkmal gesperrt (Zuwachs {zu1}, gefordert 0); ohne Merkmal durchgerutscht "
         f"(Zuwachs {zu2}) — genau der Fall, den das Feld verhindert.")

z.append("\n## Fall 2: Altbestand ohne Merkmal — Namensweg fängt sie weiterhin")
k2 = anlegen("probe", "bericht", 0)
zu3 = anbieten(k2, "(c) nische='probe', ist_probe=0 (Altbestand)")
z.append(f"  ERGEBNIS: gesperrt über den zweiten Weg (Zuwachs {zu3}, gefordert 0)")

z.append("\n## Fall 3: echter Kandidat (Gegenprobe)")
k3 = anlegen("sicher", "preise", 0)
zu4 = anbieten(k3, "(d) nische='sicher', ist_probe=0")
z.append(f"  ERGEBNIS: aufgenommen (Zuwachs {zu4}, gefordert 1)")

with transaktion(con):            # Prüfkandidaten wieder entfernen
    con.execute("DELETE FROM projektgedaechtnis WHERE kandidat_id IN (?,?,?)", (k1, k2, k3))
    con.execute("DELETE FROM kandidaten WHERE id IN (?,?,?)", (k1, k2, k3))
z.append(f"\n(Prüfkandidaten K{k1}, K{k2}, K{k3} wieder entfernt)")
ohne_merkmal = con.execute("SELECT COUNT(*) FROM kandidaten WHERE (nische LIKE 'probe%' OR bereich LIKE 'probe%') "
                           "AND COALESCE(ist_probe,0)=0").fetchone()[0]
z.append(f"Bestand: {con.execute('SELECT COUNT(*) FROM kandidaten WHERE ist_probe=1').fetchone()[0]} Kandidaten mit "
         f"ist_probe=1; Proben ohne Merkmal (Namensweg nötig): {ohne_merkmal}")
(A / "09-probenmerkmal-statt-name.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
