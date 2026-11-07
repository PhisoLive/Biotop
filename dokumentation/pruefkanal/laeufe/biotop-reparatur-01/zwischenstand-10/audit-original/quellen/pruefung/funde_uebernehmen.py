"""Funde aus Werk 11 (Lauf-13-Stand, 48 Ankläger-Tests) in das neue Werk übernehmen — mit erzwungener
Neubewertung nach F5 3.10 (Organ fundpruefung.uebernehmen).

Zweck: Zeile 8 (Doppelungsanteil) braucht einen Ankläger mit gefülltem Behauptungsvorrat. Werk 11 ist der
Stand, an dem acht Tests dasselbe über `lager/reserviert` behaupteten.
Aufruf: funde_uebernehmen.py <ausgaben-dir> <von_werk> <nach_werk> <lauf>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden
from biotop.organe import aegis, fundpruefung

A = Path(sys.argv[1]); VON = int(sys.argv[2]); NACH = int(sys.argv[3]); LAUF = int(sys.argv[4])
con = verbinden()
pfad = Path(con.execute("SELECT pfad FROM werke WHERE id=?", (NACH,)).fetchone()[0])
vorher = con.execute("SELECT COUNT(*) FROM immunsystem WHERE werk_id=?", (VON,)).fetchone()[0]

e = fundpruefung.uebernehmen(con, VON, NACH, LAUF, pfad)
z = [f"# Funde aus Werk {VON} in Werk {NACH} übernommen — mit erzwungener Neubewertung (F5 3.10)",
     f"Bestand Werk {VON}: {vorher} Einträge | übernommen: {e['uebernommen']}",
     f"Neubewertung: {e['bezugsgroesse']}, {e['kammerlaeufe']} Kammerläufe"]
for r in e["ergebnisse"]:
    if r["geaendert"]:
        z.append(f"  {r['name']}: {r['alt']} → {r['neu']} (besteht {r['besteht_am_ausgang']}, "
                 f"Absturz {r['absturz_im_werk']}, Verweis {r['vertragsverweis']})")
z.append("")
z.append("## Behauptungsvorrat des Anklägers nach der Übernahme")
for b in ("bericht", "formeln", "lager", "preise"):
    bb = aegis.bisherige_behauptungen(con, NACH, b)
    z.append(f"  {b}: {len(bb)} Behauptungen — {', '.join(bb[:6])}{' …' if len(bb) > 6 else ''}")
z.append("")
z.append(f"Immunsystem Werk {NACH}: " +
         str({r[0]: r[1] for r in con.execute("SELECT status, COUNT(*) FROM immunsystem WHERE werk_id=? GROUP BY status", (NACH,))}))
(A / "10-funde-uebernommen.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
