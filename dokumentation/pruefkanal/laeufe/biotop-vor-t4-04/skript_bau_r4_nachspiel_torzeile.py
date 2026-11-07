"""Behebungsrunde 4 vor T4 — Nachspiel an Stufe 2 und Torzeile „Schwächen“ (alles-oder-nichts):
- nachspiel.vorbereiten: die Läufe lagen vor der Stufe 2; ihr Vorspann trägt nur die Rauschmessung der Stufe 1. Wie ein
  Lauf mit dem neuen Instrument misst das Nachspiel die Rauschtoleranz an Stufe 2 selbst (fünf Kammerläufe an der
  Vorgeneration, eichung.rauschmessung mit laufzeit_einmal) und setzt sie in `tausch` — Herkunft im Beleg.
- kern/gegenzeugen.py: torzeile_schwaechen() — Entscheidung Chat-Claude 5: die doppelte Prüfung ist VERBINDLICH in der
  Torzeile „Schwächen“ (nicht im Annahmepfad): behoben zählt nur mit doppelurteil True; nicht beurteilbar zählt nicht.
"""
import py_compile
from pathlib import Path

B = Path('/root/biotop/biotop')
dateien = {n: (B / n).read_text() for n in ('nachspiel.py', 'kern/gegenzeugen.py')}
ops = []


def R(d, a, b, n=1):
    ops.append((d, a, b, n))


R('nachspiel.py', '''    # Behebungsrunde 4 vor T4: dieselbe Vergleichslast Stufe 2 wie generation() (lauf.py setzt sie in `tausch`).
    tausch["_referenzlast_laufzeit"] = L._referenzlast(werk["name"], paket, 2)''', '''    # Behebungsrunde 4 vor T4: dieselbe Vergleichslast Stufe 2 wie generation() (lauf.py setzt sie in `tausch`).
    tausch["_referenzlast_laufzeit"] = L._referenzlast(werk["name"], paket, 2)
    rauschen_herkunft = "aus dem versiegelten Vorspann-Nachweis (Stufe 1)"
    if tausch["_referenzlast_laufzeit"] and rauschen_stufe2:
        # Der Lauf lag vor der Stufe 2; sein Vorspann trägt die Rauschmessung der Stufe 1. Wie ein Lauf mit dem neuen
        # Instrument (vorspann: Rauschmessung an Stufe 2) wird die Toleranz hier an Stufe 2 gemessen — an der
        # Vorgeneration, fünf Kammerläufe, dieselbe Regel (eichung.rauschmessung, vorspann._rauschwerte).
        from .organe import eichung, vorspann
        r2 = eichung.rauschmessung(con, lauf_id, werk["id"], ziel, bereiche, paket, tausch["_referenzlast_laufzeit"],
                                   eichung.laufzeit_einmal)
        tausch.update(vorspann._rauschwerte(r2, bereiche))
        tausch["_rauschbelege"] = r2["bereiche"]
        rauschen_herkunft = (f"im Nachspiel an Stufe 2 gemessen (Vorgeneration, {len(r2.get('kammerlauf_s') or [])} "
                             f"Kammerläufe, längster {max(r2.get('kammerlauf_s') or [0]):.1f} s)")''')
R('nachspiel.py', '''def vorbereiten(quelle_db: Path, kandidat_id: int, arbeit: Path, *, urteil_nr: int | None = None,
                partner_id: int | None = None, masseichung_an: bool = True) -> dict:''', '''def vorbereiten(quelle_db: Path, kandidat_id: int, arbeit: Path, *, urteil_nr: int | None = None,
                partner_id: int | None = None, masseichung_an: bool = True, rauschen_stufe2: bool = True) -> dict:''')
R('nachspiel.py', '''            "tausch": tausch, "eichung": eichung, "eichung_herkunft": herkunft, "extra": extra,''',
  '''            "tausch": tausch, "eichung": eichung, "eichung_herkunft": herkunft, "extra": extra,
            "rauschen_herkunft": rauschen_herkunft,''')
R('nachspiel.py', '''             "laufzeit_stufe": u.get("laufzeit_stufe"),''', '''             "laufzeit_stufe": u.get("laufzeit_stufe"),
             "rauschen_herkunft": fall.get("rauschen_herkunft"),
             "rauschtoleranz": (fall.get("tausch") or {}).get("_rauschtoleranz"),
             "gesperrte_bereiche": (fall.get("tausch") or {}).get("_gesperrte_bereiche"),''')
R('kern/gegenzeugen.py', '''def s1_aus_messung(e: dict) -> tuple[dict, dict]:''', '''def torzeile_schwaechen(schwaechen: dict[str, dict], schwelle: float = 0.8) -> dict:
    """Torzeile „Schwächen“ (Tor 4, Fassung 8: ≥ 80 % der versiegelten Schwächen behoben) — Entscheidung Chat-Claude 5
    (Behebungsrunde 4 vor T4): die doppelte Gegenzeugen-Prüfung ist hier VERBINDLICH, nicht im Annahmepfad.
    `schwaechen`: {Kennung: {"schwaeche": {...}, "normal": {...}}} — je Schwäche beide Prüfungen (doppelurteil).
    Behoben zählt eine Schwäche nur mit doppelurteil True; nicht beurteilbar (eine Prüfung fehlt) zählt NICHT als
    behoben und wird eigens gezählt. Rückgabe {"behoben", "gesamt", "anteil", "erfuellt", "je_schwaeche",
    "nicht_beurteilbar", "zeile"}. Ohne Schwäche: nicht erfüllt (null Fälle sind keine Mehrheit)."""
    je = {k: doppelurteil((v or {}).get("schwaeche"), (v or {}).get("normal")) for k, v in sorted(schwaechen.items())}
    behoben = sorted(k for k, u in je.items() if u["behoben"] is True)
    offen = sorted(k for k, u in je.items() if u["behoben"] is None)
    n = len(je)
    anteil = len(behoben) / n if n else 0.0
    return {"behoben": behoben, "gesamt": n, "anteil": round(anteil, 4), "erfuellt": bool(n) and anteil >= schwelle,
            "je_schwaeche": je, "nicht_beurteilbar": offen,
            "zeile": (f"Schwächen: {len(behoben)} von {n} behoben nach doppelter Prüfung (Schwäche weg UND Verhalten gegen "
                      f"die Normalversion unverändert) = {anteil * 100:.0f} %, Schwelle {schwelle * 100:.0f} % — "
                      f"{'erfüllt' if bool(n) and anteil >= schwelle else 'nicht erfüllt'}"
                      + (f"; nicht beurteilbar: {', '.join(offen)}" if offen else ""))}


def s1_aus_messung(e: dict) -> tuple[dict, dict]:''')

fehl = [(d, a[:70], dateien[d].count(a)) for d, a, b, n in ops if dateien[d].count(a) != n]
if fehl:
    raise SystemExit(f'Anker fehlen/mehrdeutig, nichts geschrieben: {fehl}')
for d, a, b, n in ops:
    dateien[d] = dateien[d].replace(a, b)
for d, t in dateien.items():
    (B / d).write_text(t)
    py_compile.compile(str(B / d), doraise=True)
print(f'Nachspiel/Torzeile: {len(ops)} von {len(ops)} Ersetzungen, kompiliert')
