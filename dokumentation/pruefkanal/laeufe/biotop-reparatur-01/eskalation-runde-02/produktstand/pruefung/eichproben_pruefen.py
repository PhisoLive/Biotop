"""Führt den Vorspann (vier Eichproben am versiegelten Gegenstand) an einem echten Werk aus.
Aufruf: eichproben_pruefen.py <ausgaben-dir> <lauf_id>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.organe import eichproben, eichung, landkarte
from biotop import lauf as L

A = Path(sys.argv[1]); LAUF = int(sys.argv[2])
con = verbinden()
lauf = L._lauf(con, LAUF); werk = L._werk(con, lauf["werk_id"]); pfad = Path(werk["pfad"])
mass = lj(lauf["mass"]); paket, bereiche = mass["paket"], mass["bereiche"]
ref = L._referenzlast(werk["name"], paket)
basis_gen = L.letzte_angenommene(con, LAUF); basis = lj(basis_gen["masse"])
ausgang = lj(con.execute("SELECT masse FROM generationen WHERE lauf_id=? AND nummer=0", (LAUF,)).fetchone()["masse"])
kanten = [(z["von"], z["nach"], z["art"]) for z in con.execute("SELECT von, nach, art FROM strassen WHERE werk_id=?", (werk["id"],))]
bstr = landkarte.bereichs_strassen(kanten, paket)

e = eichproben.proben(con, LAUF, werk["id"], pfad, paket, bereiche, bstr, basis, ausgang, ref,
                      mass.get("grenzen") or {}, generation=basis_gen["nummer"])
z = [f"# Vorspann „Generation minus eins“ — vier Eichproben, Lauf {LAUF}, Werk {werk['name']}"]
z += eichproben.text(e)
z.append("")
z += eichung.kosten_text(eichung.kosten(con, LAUF), bereiche=len(bereiche))
(A / "10-eichproben-vorspann.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
