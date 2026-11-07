"""Behebungsrunde 4 vor T4, Entscheidung Chat-Claude 1 — Vergleichslast Stufe 2 (zehnfache Eingabegröße je Bereich).
An ihr misst die Nische „schnell“ den Gewinn und jede Nische ihre Laufzeitgrenze; der Kammerlauf bleibt unter 60 s.
Eingebaut:
- vorspann._ausfuehren: Rauschmessung der Laufzeit an Stufe 2 (laufzeit-only Kammerläufe, dasselbe Instrument wie die
  gepaarte Messung), Kammerlauf-Dauer gemessen und begrenzt (< 60 s, sonst verweigert der Vorspann den Lauf);
  Stufe-2-Last im Quellen-Siegel.
- aegis.pruefen und lauf._generation_koerper: gepaarte Messung, Riss-Nachmessung und Gewinn-Nachmessung an Stufe 2
  (Rückfall Stufe 1, wenn für ein Werk keine Stufe 2 existiert — dann steht das im Urteil).
- messgeraet: Rausch-Rückfallwert für Stufe 2 nicht versteckt: im Urteil `laufzeit_stufe`.
Alles-oder-nichts: jeder Anker genau einmal, sonst wird nichts geschrieben.
"""
import py_compile
from pathlib import Path

R_ = Path('/root/biotop/biotop')
dateien = {n: (R_ / n).read_text() for n in ('organe/vorspann.py', 'organe/eichung.py', 'organe/aegis.py', 'lauf.py',
                                            'nachspiel.py')}
ops = []


def R(datei, a, b, n=1):
    ops.append((datei, a, b, n))


# ---------------------------------------------------------------- eichung: laufzeit-only Messung + Kammerlauf-Dauer
R('organe/eichung.py', '''def rauschmessung(con: sqlite3.Connection, lauf_id: int, werk_id: int, pfad: Path, bereiche: list[str],
                  paket: str, ref: str) -> dict:''', '''def laufzeit_einmal(pfad: Path, bereiche: list[str], paket: str, ref: str) -> dict:
    """Behebungsrunde 4 (Entscheidung Chat-Claude 1): EIN Kammerlauf nur der Laufzeit an der Referenzlast `ref` —
    dasselbe Instrument wie die gepaarte Messung (messgeraet.laufzeit_messen). Für die Rauschmessung der Stufe 2."""
    r = messgeraet.laufzeit_messen(pfad, bereiche, paket, ref)
    if not r.get("gueltig"):
        return {b: None for b in bereiche}
    return {b: ((r.get("bereiche") or {}).get(b) or {}).get("laufzeit_ms") for b in bereiche}


def rauschmessung(con: sqlite3.Connection, lauf_id: int, werk_id: int, pfad: Path, bereiche: list[str],
                  paket: str, ref: str, messen_einmal=None) -> dict:''')
R('organe/eichung.py', '''    _tabelle(con)
    import time
    t0 = time.time()
    kammerlaeufe = 0
    roh: dict[str, list[float]] = {b: [] for b in bereiche}
    for _ in range(messgeraet.RAUSCH_MESSUNGEN):
        kammerlaeufe += 1
        for b, v in _messen_einmal(pfad, bereiche, paket, ref).items():
            if v is not None:
                roh[b].append(float(v))''', '''    _tabelle(con)
    import time
    t0 = time.time()
    kammerlaeufe = 0
    # Behebungsrunde 4: `messen_einmal` (Vorgabe: volle Messung wie bisher; Vorspann: laufzeit_einmal an Stufe 2) und die
    # Dauer jedes Kammerlaufs — der Vorspann verlangt an Stufe 2 unter 60 s je Kammerlauf (Entscheidung Chat-Claude 1).
    einmal = messen_einmal or _messen_einmal
    dauer_s: list[float] = []
    roh: dict[str, list[float]] = {b: [] for b in bereiche}
    for _ in range(messgeraet.RAUSCH_MESSUNGEN):
        kammerlaeufe += 1
        t_k = time.monotonic()
        werte_k = einmal(pfad, bereiche, paket, ref)
        dauer_s.append(round(time.monotonic() - t_k, 2))
        for b, v in werte_k.items():
            if v is not None:
                roh[b].append(float(v))''')
R('organe/eichung.py', '''            for _ in range(max(0, fehlend)):
                kammerlaeufe += 1
                v = _messen_einmal(pfad, [b], paket, ref).get(b)''', '''            for _ in range(max(0, fehlend)):
                kammerlaeufe += 1
                t_k = time.monotonic()
                v = einmal(pfad, [b], paket, ref).get(b)
                dauer_s.append(round(time.monotonic() - t_k, 2))''')
# ---------------------------------------------------------------- vorspann: Stufe 2
R('organe/vorspann.py', '''    ref = L._referenzlast(werk['name'], paket)
    verf = verfassung.lesen(con, werk['id'])
    if verf is None:
        raise ValueError('Verfassung fehlt')
    if not ref:
        raise ValueError('Referenzlast fehlt')''', '''    ref = L._referenzlast(werk['name'], paket)
    verf = verfassung.lesen(con, werk['id'])
    if verf is None:
        raise ValueError('Verfassung fehlt')
    if not ref:
        raise ValueError('Referenzlast fehlt')
    # Behebungsrunde 4 vor T4 (Entscheidung Chat-Claude 1): die Laufzeit wird an der Vergleichslast Stufe 2 gemessen
    # (zehnfache Eingabegröße je Bereich). Fehlt sie, ist die Stufe-1-Last Rückfall — das steht im Nachweis.
    ref2 = L._referenzlast(werk['name'], paket, 2)
    r['laufzeit_stufe'] = 2 if ref2 else 1''')
R('organe/vorspann.py', '''    r['rauschen'] = eichung.rauschmessung(con, lauf_id, werk['id'], pfad, bereiche, paket, ref)
    tausch.update(_rauschwerte(r['rauschen'], bereiche))''', '''    if ref2:
        r['rauschen'] = eichung.rauschmessung(con, lauf_id, werk['id'], pfad, bereiche, paket, ref2, eichung.laufzeit_einmal)
        dauer = max(r['rauschen'].get('kammerlauf_s') or [0.0])
        if dauer >= STUFE2_KAMMERLAUF_S:
            raise ValueError(f'Vergleichslast Stufe 2: ein Kammerlauf dauerte {dauer:.1f} s (Grenze {STUFE2_KAMMERLAUF_S} s, '
                             f'Entscheidung Chat-Claude 1) — Referenzlast Stufe 2 verkleinern')
    else:
        r['rauschen'] = eichung.rauschmessung(con, lauf_id, werk['id'], pfad, bereiche, paket, ref)
    tausch.update(_rauschwerte(r['rauschen'], bereiche))''')
R('organe/vorspann.py', '''def ausfuehren(con, lauf_id):''', '''STUFE2_KAMMERLAUF_S = 60      # Entscheidung Chat-Claude 1: ein Kammerlauf der Stufe 2 bleibt unter einer Minute


def ausfuehren(con, lauf_id):''')
R('organe/vorspann.py', '''            'referenzlast':{'sha256':hashlib.sha256(ref.encode()).hexdigest(),
                           'suche':[werk['name'],paket], 'wurzel':str(L.REFERENZLAST.resolve())}}''',
  '''            'referenzlast':{'sha256':hashlib.sha256(ref.encode()).hexdigest(),
                           'suche':[werk['name'],paket], 'wurzel':str(L.REFERENZLAST.resolve())},
            'referenzlast_stufe2':{'sha256':(hashlib.sha256(ref2.encode()).hexdigest() if ref2 else None)}}''')
R('organe/vorspann.py', '''    ref = L._referenzlast(werk['name'], paket)
    if not ref:
        raise ValueError('Referenzlast fehlt')
    kandidaten = list((WURZEL / 'biotop').rglob('*'))''', '''    ref = L._referenzlast(werk['name'], paket)
    if not ref:
        raise ValueError('Referenzlast fehlt')
    ref2 = L._referenzlast(werk['name'], paket, 2)
    kandidaten = list((WURZEL / 'biotop').rglob('*'))''')
# ---------------------------------------------------------------- aegis: gepaarte Messungen an Stufe 2
R('organe/aegis.py', '''            vv_optionen: dict | None = None) -> dict:''', '''            vv_optionen: dict | None = None, referenzlast_laufzeit: str | None = None) -> dict:''')
R('organe/aegis.py', '''    if referenzlast and messgeraet.laufzeit_entscheidet(u, k["nische"]):
        # Nur Bereiche, deren Laufzeit geprüft wird: von der Rauschmessung gesperrte nie (grenzen_f2) — eine fehlende
        # Messung dort macht die gepaarte Messung nicht ungültig.
        lz_bereiche = [b for b in bereiche if b not in set((tausch or {}).get("_gesperrte_bereiche") or [])]
        lz = messgeraet.laufzeit_gepaart(werk, lz_bereiche, paket, referenzlast, {}, code)''', '''    # Behebungsrunde 4 vor T4 (Entscheidung Chat-Claude 1): Laufzeit an der Vergleichslast Stufe 2 (zehnfache
    # Eingabegröße), Rückfall Stufe 1 — die Stufe steht im Urteil.
    ref_lz = referenzlast_laufzeit or referenzlast
    urteil["laufzeit_stufe"] = 2 if referenzlast_laufzeit else 1
    if referenzlast and messgeraet.laufzeit_entscheidet(u, k["nische"]):
        # Nur Bereiche, deren Laufzeit geprüft wird: von der Rauschmessung gesperrte nie (grenzen_f2) — eine fehlende
        # Messung dort macht die gepaarte Messung nicht ungültig.
        lz_bereiche = [b for b in bereiche if b not in set((tausch or {}).get("_gesperrte_bereiche") or [])]
        lz = messgeraet.laufzeit_gepaart(werk, lz_bereiche, paket, ref_lz, {}, code)''')
R('organe/aegis.py', '''        best = messgeraet.laufzeit_bestaetigen(
            werk, lz_bereiche, paket, referenzlast, {}, code, basis_paar, mess,''', '''        best = messgeraet.laufzeit_bestaetigen(
            werk, lz_bereiche, paket, ref_lz, {}, code, basis_paar, mess,''')
R('organe/aegis.py', '''            g = messgeraet.gewinn_bestaetigen(werk, [b for b in urteil["wirkungskreis"] if b not in gesperrt], paket,
                                              referenzlast, {}, code, basis_paar, mess, (tausch or {}).get("_rauschtoleranz"))''',
  '''            g = messgeraet.gewinn_bestaetigen(werk, [b for b in urteil["wirkungskreis"] if b not in gesperrt], paket,
                                              ref_lz, {}, code, basis_paar, mess, (tausch or {}).get("_rauschtoleranz"))''')
R('organe/aegis.py', '''                            laufzeit_nachmessung=urteil.get("laufzeit_nachmessung"),''', '''                            laufzeit_nachmessung=urteil.get("laufzeit_nachmessung"),
                            laufzeit_stufe=urteil.get("laufzeit_stufe"),''')
# ---------------------------------------------------------------- lauf: Stufe 2 an Annahmepfad, Verhandlung, Generalprobe
R('lauf.py', '''    tausch = annahme_tausch(mass, nachweis)''', '''    tausch = annahme_tausch(mass, nachweis)
    tausch["_referenzlast_laufzeit"] = _referenzlast(werk["name"], paket, 2)''')
R('lauf.py', '''                u = aegis.pruefen(con, lauf_id, werk["id"], kid, pfad, paket, bereiche, bstrassen, basis, ausgang, ref, tausch)''',
  '''                u = aegis.pruefen(con, lauf_id, werk["id"], kid, pfad, paket, bereiche, bstrassen, basis, ausgang, ref, tausch,
                                  referenzlast_laufzeit=tausch.get("_referenzlast_laufzeit"))''')
R('lauf.py', '''            u2 = aegis.pruefen(con, lauf_id, werk["id"], kid, pfad, paket, bereiche, bstrassen, basis, ausgang, ref, tausch, extra_code={**extra, **anp''',
  '''            u2 = aegis.pruefen(con, lauf_id, werk["id"], kid, pfad, paket, bereiche, bstrassen, basis, ausgang, ref, tausch,
                               referenzlast_laufzeit=(tausch or {}).get("_referenzlast_laufzeit"), extra_code={**extra, **anp''')
R('lauf.py', '''    if ref and messgeraet.laufzeit_entscheidet(u0, "werk"):
        lz = messgeraet.laufzeit_gepaart(pfad, lz_bereiche, paket, ref, {}, lz_code)''', '''    # Behebungsrunde 4 vor T4 (Entscheidung Chat-Claude 1): Vergleichslast Stufe 2, Rückfall Stufe 1.
    ref_lz = tausch.get("_referenzlast_laufzeit") or ref
    zusammenfassung["_laufzeit_stufe"] = 2 if tausch.get("_referenzlast_laufzeit") else 1
    if ref and messgeraet.laufzeit_entscheidet(u0, "werk"):
        lz = messgeraet.laufzeit_gepaart(pfad, lz_bereiche, paket, ref_lz, {}, lz_code)''')
R('lauf.py', '''        best = messgeraet.laufzeit_bestaetigen(
            pfad, lz_bereiche, paket, ref, {}, lz_code, basis_paar, mess,''', '''        best = messgeraet.laufzeit_bestaetigen(
            pfad, lz_bereiche, paket, ref_lz, {}, lz_code, basis_paar, mess,''')
R('lauf.py', '''            g = messgeraet.gewinn_bestaetigen(pfad, lz_kreis, paket, ref, {}, lz_code, basis_paar, mess,''',
  '''            g = messgeraet.gewinn_bestaetigen(pfad, lz_kreis, paket, ref_lz, {}, lz_code, basis_paar, mess,''')
# ---------------------------------------------------------------- nachspiel: dieselbe Stufe wie der Lauf
R('nachspiel.py', '''    tausch = L.annahme_tausch(mass, {**nachweis, "masseichung": eichung})
    ref = L._referenzlast(werk["name"], paket)''', '''    tausch = L.annahme_tausch(mass, {**nachweis, "masseichung": eichung})
    ref = L._referenzlast(werk["name"], paket)
    # Behebungsrunde 4 vor T4: dieselbe Vergleichslast Stufe 2 wie generation() (lauf.py setzt sie in `tausch`).
    tausch["_referenzlast_laufzeit"] = L._referenzlast(werk["name"], paket, 2)''')
R('nachspiel.py', '''                              fall["tausch"], extra_code=fall["extra"], vv_optionen=vv_optionen)''',
  '''                              fall["tausch"], extra_code=fall["extra"], vv_optionen=vv_optionen,
                              referenzlast_laufzeit=fall["tausch"].get("_referenzlast_laufzeit"))''')
R('nachspiel.py', '''             "gewinn_nachmessung": u.get("gewinn_nachmessung"),''', '''             "gewinn_nachmessung": u.get("gewinn_nachmessung"),
             "laufzeit_stufe": u.get("laufzeit_stufe"),''')

fehl = [(d, a[:70], dateien[d].count(a)) for d, a, b, n in ops if dateien[d].count(a) != n]
if fehl:
    raise SystemExit(f'Anker fehlen/mehrdeutig, nichts geschrieben: {fehl}')
for d, a, b, n in ops:
    dateien[d] = dateien[d].replace(a, b)
for d, t in dateien.items():
    (R_ / d).write_text(t)
    py_compile.compile(str(R_ / d), doraise=True)
print(f'Stufe 2: {len(ops)} von {len(ops)} Ersetzungen in {len(dateien)} Dateien, kompiliert')
