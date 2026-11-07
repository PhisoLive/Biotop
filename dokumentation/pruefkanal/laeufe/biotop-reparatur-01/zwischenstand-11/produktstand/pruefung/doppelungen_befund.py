"""Befund (Vorgabe Philipp 19.09.2026): Die Doppelungserkennung (3.10) vergleicht Meldungsklasse und ORT, nicht die
BEHAUPTUNG. Deshalb kamen sechs Tests einzeln ins Immunsystem, die dieselbe Behauptung an derselben Stelle aufstellen.
Dieses Skript weist den Befund mechanisch nach und rechnet den Doppelungsanteil aus Phase 2 mit der Behauptungs-Lesart neu.
KEINE Codeänderung am Messgerät (Korrektur erst Fassung 5).

Lesart „Behauptung": (aufgerufene Funktion des Werks, Art der Zusicherung) — abgeleitet aus dem Testcode:
  Ziel   = die im Test aufgerufene Werk-Funktion (z. B. Katalog.wert)
  Aussage= die Vergleichsseite der assert-Zeile, auf Namen normiert (grundpreis/stueckpreis/staffel…)
Zwei Tests behaupten dasselbe, wenn Ziel und Aussage übereinstimmen.

Aufruf: doppelungen_befund.py <ausgaben-dir>
"""
import re, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj

A = Path(sys.argv[1])
con = verbinden()

def behauptung(code: str) -> tuple[str, str]:
    """(Ziel, Aussage) aus dem Testcode: aufgerufene Werk-Methode + normierte Vergleichsseite der ersten assert-Zeile."""
    ziele = re.findall(r"\.(\w+)\s*\(", code)
    werkzeug = {"aufnehmen", "append", "raises", "pytest", "assert"}
    ziel = next((z for z in ziele if z not in werkzeug), "?")
    for zeile in code.splitlines():
        if zeile.strip().startswith("assert"):
            rechts = zeile.split("==")[-1] if "==" in zeile else zeile
            zahlen = re.findall(r"\d+\.?\d*", rechts)
            worte = [w for w in re.findall(r"[a-z_]{4,}", rechts.lower()) if w not in ("assert", "runde_cent")]
            return ziel, "|".join(worte) or "|".join(zahlen)
    return ziel, "?"

zeilen = ["# Befund (Vorgabe Philipp 19.09.2026): Doppelungserkennung 3.10 vergleicht Meldungsklasse+Ort, nicht die Behauptung",
          "# Nachweis an den sechs Norm-Tests des Werks lagerhaus (Bereich preise/bericht), die einzeln ins Immunsystem kamen:"]
tests = [dict(r) for r in con.execute("SELECT name, code, bereich FROM immunsystem WHERE werk_id=18 AND name LIKE 'aegis_k%' ORDER BY name")]
gruppen = {}
for t in tests:
    b = behauptung(t["code"])
    gruppen.setdefault(b, []).append(t["name"])
    zeilen.append(f"  {t['name']:<34} Bereich {t['bereich']:<8} Behauptung: Ziel={b[0]}  Aussage={b[1][:60]}")
zeilen.append("")
for b, namen in sorted(gruppen.items(), key=lambda x: -len(x[1])):
    zeilen.append(f"Behauptung (Ziel={b[0]}, Aussage={b[1][:50]}): {len(namen)} Tests — {', '.join(namen)}")
mehrfach = sum(len(v) - 1 for v in gruppen.values() if len(v) > 1)
zeilen.append(f"BEFUND (Lesart A, Ziel+Wert): {len(tests)} Ankläger-Tests des Werks stellen {len(gruppen)} verschiedene Behauptungen auf; "
              f"{mehrfach} von {len(tests)} wären Doppelungen.")
# Lesart B (Philipps Lesart): gleiche Behauptung = gleiche Ziel-Funktion des Werks, unabhängig vom eingesetzten Zahlenwert
gruppen_b = {}
for t in tests:
    gruppen_b.setdefault((t["bereich"], behauptung(t["code"])[0]), []).append(t["name"])
mehrfach_b = sum(len(v) - 1 for v in gruppen_b.values() if len(v) > 1)
for (ber, ziel), namen in sorted(gruppen_b.items(), key=lambda x: -len(x[1])):
    zeilen.append(f"  Lesart B — {ber}/{ziel}(): {len(namen)} Tests — {', '.join(namen)}")
zeilen.append(f"BEFUND (Lesart B, Ziel-Funktion = Philipps Lesart 'gleiche Behauptung, gleiche Stelle'): {mehrfach_b} von {len(tests)} sind Doppelungen "
              f"— sechs Tests behaupten dasselbe über Katalog.wert (Staffelpreis statt Grundpreis), nur mit anderen Zahlen.")
zeilen.append("Eigene Kennzeichnung (Hermes): Lesart A und B sind meine Auslegungen der Regel 3.10; die Regel selbst nennt nur 'gleiche Ausnahme/Zusicherung an derselben Stelle'.")
zeilen.append("Die gemeldete Doppelungserkennung greift hier nicht, weil sie (Meldungsklasse, Ort) vergleicht: "
              "alle Tests melden 'AssertionError' an unterschiedlichen Zeilen ihrer eigenen Testdatei — also nie derselbe Ort.")

# --- Phase-2-Anteil mit beiden Lesarten
zeilen += ["", "# Doppelungsanteil Phase 2 (Lauf 13) — gemeldete Lesart (Meldungsklasse+Ort) gegen Behauptungs-Lesart"]
p2 = [dict(r) for r in con.execute("SELECT name, code, bereich FROM immunsystem WHERE lauf_id=13")]
gemeldet_doppel = 0
for z in con.execute("SELECT inhalt FROM protokoll WHERE art='aegis.urteil' AND inhalt LIKE '%\"lauf_id\": 13,%'"):
    gemeldet_doppel += len(lj(z["inhalt"]).get("doppelungen") or [])
gefunden_13 = len(p2)
g2 = {}
g2b = {}
for t in p2:
    g2.setdefault((t["bereich"], behauptung(t["code"])), []).append(t["name"])
    g2b.setdefault((t["bereich"], behauptung(t["code"])[0]), []).append(t["name"])
doppel_neu = sum(len(v) - 1 for v in g2.values() if len(v) > 1)
doppel_neu_b = sum(len(v) - 1 for v in g2b.values() if len(v) > 1)
gesamt_neu = gefunden_13 + gemeldet_doppel
zeilen.append(f"Lauf 13: {gefunden_13} Tests kamen als eigenständige Funde ins Immunsystem; {gemeldet_doppel} wurden als Doppelung verworfen "
              f"→ gemeldeter Anteil {gemeldet_doppel}/{gesamt_neu} = {100*gemeldet_doppel/max(1,gesamt_neu):.1f} %.")
zeilen.append(f"ACHTUNG Bezugsgröße: der Phase-2-Bericht nannte 2,5 % — das war {gemeldet_doppel} Doppelungen gegen ALLE 240 Ablehnungen des Laufs, "
              f"nicht gegen die {gesamt_neu} vom Ankläger erzeugten Tests. Gegen die Tests sind es {100*gemeldet_doppel/max(1,gesamt_neu):.1f} %.")
zeilen.append(f"Lesart A (Ziel+Wert): {gefunden_13} aufgenommene Tests = {len(g2)} Behauptungen → zusätzlich {doppel_neu} Doppelungen, "
              f"Anteil ({gemeldet_doppel}+{doppel_neu})/{gesamt_neu} = {100*(gemeldet_doppel+doppel_neu)/max(1,gesamt_neu):.1f} %.")
zeilen.append(f"Lesart B (Ziel-Funktion, Philipps Lesart): {len(g2b)} Behauptungen → zusätzlich {doppel_neu_b} Doppelungen, "
              f"Anteil ({gemeldet_doppel}+{doppel_neu_b})/{gesamt_neu} = {100*(gemeldet_doppel+doppel_neu_b)/max(1,gesamt_neu):.1f} %.")
for (ber, ziel), namen in sorted(g2b.items(), key=lambda x: -len(x[1]))[:6]:
    if len(namen) > 1:
        zeilen.append(f"   Lesart B mehrfach ({ber}/{ziel}()): {len(namen)} Tests — {', '.join(namen[:8])}{' …' if len(namen) > 8 else ''}")
zeilen.append("Korrektur erst in Fassung 5 (Vorgabe Philipp): der Schlüssel muss die Behauptung sein (Ziel-Funktion + Zusicherung), nicht Meldungsklasse+Ort.")
(A / "94-befund-doppelungen.txt").write_text("\n".join(zeilen) + "\n")
print("\n".join(zeilen))
