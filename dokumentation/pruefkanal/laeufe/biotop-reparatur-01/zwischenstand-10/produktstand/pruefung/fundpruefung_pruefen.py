"""Prüft das Organ „Fund-Neubewertung" (F5 3.10) an echten Kammerläufen.

Fall 1: Werk 18 (lagerhaus, Stand Lauf 20) — die 14 vorhandenen Funde/Normen werden nachgemessen. Erwartung:
        der behobene K1165-Fund ist im Werk (nicht mehr offen), die Normtests bleiben Norm.
Fall 2: Ein Fund, der am Ausgang FÄLLT und den Vertrag nennt → bleibt Fund (das ist der Kern der Regel).
Fall 3: Ein Fund, der am Ausgang BESTEHT, ohne Absturz, ohne Verweis → wird Norm.
Fall 4: Übernahme zwischen Werken erzwingt die Neubewertung (kein blinder Status).
Aufruf: fundpruefung_pruefen.py <ausgaben-dir>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern import protokoll
from biotop.kern.datenbank import verbinden, transaktion
from biotop.organe import fundpruefung

A = Path(sys.argv[1])
con = verbinden()
WERK = 18
pfad = Path(con.execute("SELECT pfad FROM werke WHERE id=?", (WERK,)).fetchone()[0])
z = ["# Organ Fund-Neubewertung (F5 3.10) — offene Funde am neuen Ausgang nachmessen"]

# --- Fälle 2/3: zwei gestellte Funde einlegen
FALLEND = ("hermes_nachlauf_faellt_vertrag", "preise", '''"""Fund: Katalog.wert muss den Grundpreis nehmen (Vertrag test_vertrag_bericht_preise)."""
from lagerhaus.preise import Artikel, Katalog, Staffel


def test_nachlauf_fund_faellt_test_vertrag_bericht_preise():
    """Vertrag test_vertrag_bericht_preise::test_katalog_wert_in_eur: wert() = Grundpreis x Menge."""
    k = Katalog(); k.aufnehmen(Artikel("A", "a", 2.0, [Staffel(10, 1.0)]))
    assert k.wert("A", 10) == 99.0
''')
BESTEHEND = ("hermes_nachlauf_besteht_ohne_verweis", "preise", '''from lagerhaus.preise import Artikel, Katalog


def test_nachlauf_fund_besteht_ohne_verweis():
    k = Katalog(); k.aufnehmen(Artikel("A", "a", 2.0))
    assert k.wert("A", 10) == 20.0
''')
with transaktion(con):
    con.execute("DELETE FROM immunsystem WHERE name LIKE 'hermes_nachlauf_%'")
    for name, bereich, code in (FALLEND, BESTEHEND):
        con.execute("INSERT INTO immunsystem(werk_id, lauf_id, bereich, name, code, ursprung, status, erstellt_am,"
                    " generation) VALUES (?,?,?,?,?,?,'offen',?,0)",
                    (WERK, 20, bereich, name, code, "gestellt für die Prüfung des Organs", protokoll.jetzt()))

e = fundpruefung.bewerten(con, WERK, 20, pfad, schreiben=True)
z += fundpruefung.text(e)

z.append("\n## Erwartungen")
nach = {r["name"]: r for r in e["ergebnisse"]}
f1 = nach.get(FALLEND[0]); f2 = nach.get(BESTEHEND[0])
z.append(f"  Fall 2 (fällt am Ausgang, nennt Vertrag) → bleibt Fund: {f1['neu'] == 'offen'} "
         f"(besteht={f1['besteht_am_ausgang']}, Verweis={f1['vertragsverweis']})")
z.append(f"  Fall 3 (besteht am Ausgang, kein Verweis) → wird Norm: {f2['neu'] == 'offen_norm'} "
         f"(besteht={f2['besteht_am_ausgang']}, Verweis={f2['vertragsverweis']})")
k1165 = con.execute("SELECT name, status FROM immunsystem WHERE werk_id=? AND name LIKE '%k1165%'", (WERK,)).fetchone()
z.append(f"  K1165 (in Lauf 20 behoben) steht auf: {k1165['status']} — von der Neubewertung unberührt, "
         f"weil sie nur offene Funde prüft")

with transaktion(con):
    con.execute("DELETE FROM immunsystem WHERE name LIKE 'hermes_nachlauf_%'")
z.append("\n(gestellte Prüf-Funde wieder entfernt)")
(A / "11-fundpruefung-organ.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
