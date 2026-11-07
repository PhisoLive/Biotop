"""Behebungsrunde 4 vor T4 — Deckung und Annahmepfad (alles-oder-nichts über drei Dateien):
- verhaltensvergleich.py: Verfälschung je MERKMAL (R4-2: (f, art, merkmal); bei gewöhnlichem Muster alle Aufrufe);
  Kappe der Verfälschungsläufe je Kandidat mit gezählter Auslassung (R4-12); Klassen je Test im Beleg (R4-7);
  instabile Funktionen nicht „beobachtet“ (R4-14); Teil-Enthaltungen der Sonde im Urteil (R4-13); Docstring.
- aegis.py: Entscheidung 4 — vom Kandidaten mitgebrachte (neue oder geänderte) Tests decken nicht; Annahmegrund nur mit
  bestätigten Gewinnbereichen (R4-8); Kommentare an den Code angeglichen (R4-10).
- messgeraet.py: gewinn_bestaetigen nennt die bestätigten Bereiche (R4-8).
"""
import py_compile
from pathlib import Path

B = Path('/root/biotop/biotop')
dateien = {n: (B / n).read_text() for n in ('organe/verhaltensvergleich.py', 'organe/aegis.py', 'kern/messgeraet.py', 'lauf.py')}
ops = []


def R(d, a, b, n=1):
    ops.append((d, a, b, n))


V = 'organe/verhaltensvergleich.py'
R(V, '''- `korpus_erweitert` / `deckungsregel` ('muster' | 'funktion') schalten für die getrennte Messung von K2868 (S-7) auf
  den Korpus bzw. die Deckungsregel von 330b4ec zurück; der Lauf nutzt immer die Vorgabe.
"""''', '''- `korpus_erweitert` / `deckungsregel` ('muster' | 'funktion') schalten für die getrennte Messung von K2868 (S-7) auf
  den Korpus bzw. die Deckungsregel von 330b4ec zurück; der Lauf nutzt immer die Vorgabe.

Behebungsrunde 4 vor T4 (Entscheidungen Chat-Claude 24.09.2026, Review 03):
- Merkmale je Formvariante (Entscheidung 2): Tab, Zeilenumbruch, CR, CRLF, NBSP, doppeltes Leerzeichen, Rand vorn/hinten,
  Groß, Klein, Zahlform vorn/hinten, Zahltyp, Behälter, Schlüsselfolge — ein Test mit doppeltem Leerzeichen deckt keinen
  Tab-Rückschritt mehr (Review 03 Nr. 1).
- Muster nur aus veränderten Argumenten (Entscheidung 3): das Muster einer Beobachtung sind die Merkmale, die die
  Formvariante der Sonde eingeführt hat; Randfälle und Lastaufrufe haben kein Formvarianten-Merkmal (gewöhnlich).
- Verfälschung je Merkmal (Review 03 Nr. 2): der Aufzeichner verfälscht nur Aufrufe, deren Eingabe das Merkmal trägt;
  ein Fehler in Aufbau/Abbau zählt nicht als „fällt“. Höchstens VERFAELSCHUNG_KAPPE Läufe je Kandidat, der Rest gezählt.
- Vom Kandidaten mitgebrachte Tests decken nicht (Entscheidung 4, in aegis.pruefen: `behoben` ohne sie).
"""''')
R(V, '''KAPPE = 8   # je Funktion die ersten äußeren Aufrufe mit Alias-, Mutations- und Rücksetzmuster''',
  '''KAPPE = 8   # je Funktion die ersten äußeren Aufrufe mit Alias-, Mutations- und Rücksetzmuster
VERFAELSCHUNG_KAPPE = 24   # Behebungsrunde 4 (Review 03 Nr. 15): höchstens so viele Verfälschungsläufe je Kandidat''')
R(V, '''def _merkmal_treffer(p: set[str], je: dict, f: str, zugelassen: set[str] | None = None) -> list[str] | None:
    """Deckung je Muster, je MERKMAL gelesen (eigene Festlegung vor der Messung, Behebungsrunde 3): das Muster p einer
    Abweichung von f ist gedeckt, wenn JEDES seiner Merkmale (weissraum, gross, lang …) von mindestens einem Test
    getroffen wird, der f mit einer Eingabe dieses Merkmals ruft — „ein Test je Muster“. Alle Merkmale in einem
    einzigen Aufruf zu verlangen, käme der zu feinen Regel „je Eingabe“ nahe. Das gewöhnliche Muster (leer) deckt jeder
    Test, der f ruft. `zugelassen`: nur diese Tests (die f festhalten). Rückgabe: deckende Tests oder None."""
    tests = [t for t, fs in je.items() if fs.get(f) and (zugelassen is None or t in zugelassen)]
    if not tests:
        return None
    if not p:
        return sorted(tests)
    treffer: set[str] = set()
    for c in sorted(p):
        tc = {t for t in tests if any(c in kl for kl in je[t][f])}
        if not tc:
            return None
        treffer |= tc
    return sorted(treffer)''', '''def _merkmal_treffer(p: set[str], je: dict, f: str, haelt_f: dict[str, set[str]] | None = None) -> list[str] | None:
    """Deckung je Muster, je MERKMAL gelesen (Behebungsrunde 3): das Muster p einer Abweichung von f ist gedeckt, wenn
    JEDES seiner Merkmale (tab, zeilenumbruch, gross …) von mindestens einem Test getroffen wird, der f mit einer Eingabe
    dieses Merkmals ruft UND f für genau dieses Merkmal festhält (Behebungsrunde 4, Review 03 Nr. 2: `haelt_f[merkmal]`
    — Tests, die fallen, wenn nur die Aufrufe mit diesem Merkmal verfälscht werden). Das gewöhnliche Muster (leer) deckt
    jeder Test, der f ruft und f festhält (`haelt_f['']`, alle Aufrufe verfälscht). `haelt_f` None: ohne
    Festhalte-Bedingung (Bedarfsrechnung). Rückgabe: deckende Tests oder None."""
    tests = [t for t, fs in je.items() if fs.get(f)]
    if not tests:
        return None
    if not p:
        tr = [t for t in tests if haelt_f is None or t in (haelt_f.get('') or set())]
        return sorted(tr) or None
    treffer: set[str] = set()
    for c in sorted(p):
        tc = {t for t in tests if any(c in kl for kl in je[t][f]) and (haelt_f is None or t in (haelt_f.get(c) or set()))}
        if not tc:
            return None
        treffer |= tc
    return sorted(treffer)''')
R(V, '''def verfaelschungsbedarf(abweichungen: list[str], aufrufe: list[dict], muster: dict,
                         nicht_deckbar: set[str]) -> set[tuple[str, str]]:
    """(Funktion, Art) je Abweichung, für die ein Kandidatentest mit passendem Muster existiert — nur für diese muss
    der Aufzeichner die Verfälschungsprobe fahren."""
    je = _je_test(aufrufe)
    out = set()
    for k in abweichungen:
        f = _deckungsfunktion(k)
        if not f or k in nicht_deckbar or _aufruf(k) not in (muster or {}):
            continue
        if _merkmal_treffer(set(muster[_aufruf(k)] or []), je, f) is not None:
            out.add((f, _verfaelschungsart(k)))
    return out''', '''def verfaelschungsbedarf(abweichungen: list[str], aufrufe: list[dict], muster: dict,
                         nicht_deckbar: set[str]) -> set[tuple[str, str, str]]:
    """(Funktion, Art, Merkmal) je Abweichung, für die ein deckender Test jedes Merkmal des Musters trifft — nur für diese
    fährt der Aufzeichner die Verfälschungsprobe (Merkmal '' = gewöhnliches Muster: alle Aufrufe verfälscht)."""
    je = _je_test(aufrufe)
    out = set()
    for k in abweichungen:
        f = _deckungsfunktion(k)
        if not f or k in nicht_deckbar or _aufruf(k) not in (muster or {}):
            continue
        p = set(muster[_aufruf(k)] or [])
        if _merkmal_treffer(p, je, f) is not None:
            for c in (sorted(p) or ['']):
                out.add((f, _verfaelschungsart(k), c))
    return out''')
R(V, '''            festhaltend = set(haelt.get((f, _verfaelschungsart(k))) or ())
            treffer = _merkmal_treffer(set(muster[_aufruf(k)] or []), je, f, festhaltend) or []''',
  '''            p = set(muster[_aufruf(k)] or [])
            art = _verfaelschungsart(k)
            haelt_f = {c: set(haelt.get((f, art, c)) or ()) for c in (sorted(p) or [''])}
            treffer = _merkmal_treffer(p, je, f, haelt_f) or []''')
R(V, '''    `haelt`: {(funktion, art): {tests}} — Tests, die fallen, wenn der Aufzeichner das Ergebnis ('rueckgabe') bzw. den
    Argumentzustand ('zustand') dieser Funktion verfälscht. `nicht_deckbar`: zustandsabhängige Abweichungen.''',
  '''    `haelt`: {(funktion, art, merkmal): {tests}} — Tests, die fallen, wenn der Aufzeichner das Ergebnis ('rueckgabe')
    bzw. den Argumentzustand ('zustand') dieser Funktion an den Aufrufen mit diesem Merkmal verfälscht ('' = an allen).
    `nicht_deckbar`: zustandsabhängige Abweichungen.''')
R(V, '''def _haelt_lesen(d: dict, bedarf: set[tuple[str, str]]) -> dict[tuple[str, str], set[str]]:
    """Verfälschungsproben ausführen (d['haelt'] aufrufbar) oder aus einer festen Tabelle {'f|art': [tests]} lesen."""
    h = d.get("haelt")
    out = {}
    for f, art in sorted(bedarf):
        if callable(h):
            out[(f, art)] = set(h(f, art))
        else:
            out[(f, art)] = set((h or {}).get(f"{f}|{art}") or ())
    return out''', '''def _haelt_lesen(d: dict, bedarf: set[tuple[str, str, str]], kappe: int | None = None
                 ) -> tuple[dict[tuple[str, str, str], set[str]], list[tuple[str, str, str]]]:
    """Verfälschungsproben ausführen (d['haelt'] aufrufbar: h(f, art, merkmal), ein Kammerlauf je Probe) oder aus einer
    festen Tabelle lesen ({'f|art|merkmal': [tests]}; eine Zeile 'f|art' gilt für jedes Merkmal). Höchstens `kappe`
    Läufe; die übrigen Proben entfallen und werden zurückgegeben (gezählt, ihre Abweichungen bleiben ungedeckt)."""
    h = d.get("haelt")
    out, ausgelassen = {}, []
    for i, (f, art, c) in enumerate(sorted(bedarf)):
        if callable(h):
            if kappe is not None and i >= kappe:
                ausgelassen.append((f, art, c))
                continue
            out[(f, art, c)] = set(h(f, art, c))
        else:
            t = h or {}
            out[(f, art, c)] = set(t.get(f"{f}|{art}|{c}") or t.get(f"{f}|{art}") or ())
    return out, ausgelassen''')
R(V, '''    def haelt(f: str, art: str) -> list[str]:
        v = _aufzeichnen(werk, dateien, module, pfade, {"f": f, "art": art})
        z = v.get("zustand") or {}
        return sorted(t for t in behoben if z.get(t) == "fail")''', '''    def haelt(f: str, art: str, merkmal: str = "") -> list[str]:
        # 'fail' = die Zusicherung im Test fällt; 'fehler' (Aufbau/Abbau, Skip) hält nichts fest (Review 03 Nr. 2).
        v = _aufzeichnen(werk, dateien, module, pfade, {"f": f, "art": art, "merkmal": merkmal})
        z = v.get("zustand") or {}
        return sorted(t for t in behoben if z.get(t) == "fail")''')
R(V, '''def _enthaltungsgrund(x: str, a: dict, n: dict, alt: dict, neu: dict, eigene: set[str]) -> str:
    if x not in eigene:
        return "nicht erreicht"''', '''def _enthaltungsgrund(x: str, a: dict, n: dict, alt: dict, neu: dict, eigene: set[str],
                      instabil_fn: set[str] | None = None) -> str:
    if x not in eigene and x in (instabil_fn or set()):
        return "instabil (Vorgeneration schwankt)"
    if x not in eigene:
        return "nicht erreicht"''')
R(V, '''    blind: list[str] = []
    deckung_zaehlung = {"tests": 0, "aufrufe": 0, "verfaelschungen": 0}''', '''    blind: list[str] = []
    deckung_zaehlung = {"tests": 0, "aufrufe": 0, "verfaelschungen": 0, "kappe": VERFAELSCHUNG_KAPPE, "ausgelassen": 0}''')
R(V, '''        haelt = {}
        if deckungsregel == "muster":
            bedarf = verfaelschungsbedarf(roh["abweichungen"], aufrufe, muster, nicht_deckbar)
            haelt = _haelt_lesen(d, bedarf)
        deckung_zaehlung = {"tests": len(tests), "aufrufe": len(aufrufe), "verfaelschungen": len(haelt),
                            "festhaltend": {f"{f}|{art}": sorted(t) for (f, art), t in haelt.items()}}''', '''        haelt, ausgelassen = {}, []
        if deckungsregel == "muster":
            bedarf = verfaelschungsbedarf(roh["abweichungen"], aufrufe, muster, nicht_deckbar)
            haelt, ausgelassen = _haelt_lesen(d, bedarf, VERFAELSCHUNG_KAPPE)
        klassen_je_test: dict[str, dict[str, list]] = {}
        for c in aufrufe[:400]:
            klassen_je_test.setdefault(c.get("test", ""), {}).setdefault(c.get("f", ""), []).append(sorted(c.get("klassen") or []))
        deckung_zaehlung = {"tests": len(tests), "aufrufe": len(aufrufe), "verfaelschungen": len(haelt),
                            "kappe": VERFAELSCHUNG_KAPPE, "ausgelassen": len(ausgelassen),
                            "ausgelassen_beispiele": [f"{f}|{art}|{c}" for f, art, c in ausgelassen[:10]],
                            "festhaltend": {f"{f}|{art}|{c}": sorted(t) for (f, art, c), t in haelt.items()},
                            "klassen_je_test": klassen_je_test}''')
R(V, '''    ia, in_ = alt.get("inhalt"), neu.get("inhalt")
    eigene = _funktionen_in(a) | _funktionen_in(n)
    if ia is not None and in_ is not None:
        beobachtet = {x for x in alle if ia.get(x) and in_.get(x)}''', '''    ia, in_ = alt.get("inhalt"), neu.get("inhalt")
    eigene = _funktionen_in(a) | _funktionen_in(n)
    instabil_fn = {mf for k in instabil if (mf := funktion_von(k))}
    if ia is not None and in_ is not None:
        # Behebungsrunde 4 (Review 03 Nr. 17): eine Funktion, deren Beobachtungen alle schwanken, gilt nicht als beobachtet.
        beobachtet = {x for x in alle if ia.get(x) and in_.get(x) and (x in eigene or x not in instabil_fn)}''')
R(V, '''    enthaltungen = {x: _enthaltungsgrund(x, a, n, alt, neu, eigene) for x in alle if x not in beobachtet}''',
  '''    enthaltungen = {x: _enthaltungsgrund(x, a, n, alt, neu, eigene, instabil_fn) for x in alle if x not in beobachtet}''')
R(V, '''             "ungedeckt_aufschluesselung": dict(sorted(aufschl.items())), "blind": blind}''',
  '''             "ungedeckt_aufschluesselung": dict(sorted(aufschl.items())), "blind": blind,
             # Behebungsrunde 4 (Review 03 Nr. 3, 16): gezählte Teil-Enthaltungen der Sonde je Funktion
             "teilweise": {s: {**(alt.get("teilweise") or {}).get(s, {}), **(neu.get("teilweise") or {}).get(s, {})}
                           for s in sorted(set(alt.get("teilweise") or {}) | set(neu.get("teilweise") or {}))}}''')
R(V, '''                  "ungedeckt_aufschluesselung", "blind", "deckungsregel", "korpus_erweitert", "werkzeugdateien",''',
  '''                  "ungedeckt_aufschluesselung", "blind", "deckungsregel", "korpus_erweitert", "werkzeugdateien",
                  "teilweise", "eigene_tests_ausgeschlossen",''')
# ---------------------------------------------------------------- aegis
A_ = 'organe/aegis.py'
R(A_, '''def _namen(r: dict, praefix: str, **filt) -> set[str]:''', '''def _testquellen(code: str | None) -> dict[str, str]:
    """{testname: quelltext} — Python per ast (auch Methoden von Test-Klassen als 'Klasse::methode'), TypeScript über
    den Syntaxbaum der Kammer (typescript.testfunktionen)."""
    if not code:
        return {}
    if sprachprofil.tests_ist_ts(code):
        from ..kern import typescript
        return {t["name"]: t.get("code") or "" for t in typescript.testfunktionen(code)}
    try:
        baum = ast.parse(code)
    except SyntaxError:
        return {}
    out = {}
    for k in baum.body:
        if isinstance(k, (ast.FunctionDef, ast.AsyncFunctionDef)) and k.name.startswith("test_"):
            out[k.name] = ast.get_source_segment(code, k) or ""
        elif isinstance(k, ast.ClassDef) and k.name.startswith("Test"):
            for m in k.body:
                if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef)) and m.name.startswith("test_"):
                    out[f"{k.name}::{m.name}"] = ast.get_source_segment(code, m) or ""
    return out


def eigene_tests(werk: Path, tests_kandidat: dict, vertrag_dateien: dict) -> set[str]:
    """Entscheidung Chat-Claude 4 (Behebungsrunde 4 vor T4): ein Vorschlag beglaubigt seine eigene Änderung nie. IDs
    'datei::name' der Tests, die der Kandidat NEU mitbringt oder deren Quelltext er gegenüber der Vorgeneration ÄNDERT
    (Testdateien und Vertragsdateien des Diffs) — sie decken keine Abweichung. Decken dürfen Tests der Vorgeneration
    (auch aus Generation 0), des Anklägers (Immun- und Befundklassen-Tests) und die versiegelten Gegenzeugen."""
    out = set()
    for p, inhalt in {**(tests_kandidat or {}), **(vertrag_dateien or {})}.items():
        if inhalt is None:
            continue
        alt_p = Path(werk) / p
        alt = _testquellen(alt_p.read_text()) if alt_p.is_file() else {}
        for n, q in _testquellen(inhalt).items():
            if alt.get(n) != q:
                out.add(f"{Path(p).name}::{n}")
    return out


def _namen(r: dict, praefix: str, **filt) -> set[str]:''')
R(A_, '''    # Behebungsrunde 4 vor T4 (Entscheidung Chat-Claude 1): Laufzeit an der Vergleichslast Stufe 2 (zehnfache''',
  '''    # Behebungsrunde 4 vor T4 (Entscheidung Chat-Claude 1): Laufzeit an der Vergleichslast Stufe 2 (zehnfache''')
R(A_, '''        # Entscheidung Chat-Claude 2 (24.09.): entscheidet allein die Gewinnschwelle der Nische schnell, wird sie in der
        # Rauschtoleranz um die Schwelle in beiden Richtungen nachgemessen; widersprechen sich die Messungen, weder
        # Annahme noch Ablehnung (zurückgestellt).''', '''        # Entscheidung Chat-Claude 2 (24.09.): entscheidet allein die Gewinnschwelle der Nische schnell, wird sie in der
        # Rauschtoleranz um die Schwelle in beiden Richtungen nachgemessen; widersprechen sich die Messungen, entscheidet
        # der Median über beide Messungen (gepoolt, messgeraet.gewinn_bestaetigen); eine ungültige Nachmessung stellt
        # zurück. Behebungsrunde 4 (Review 03 Nr. 13): Kommentar an den Code angeglichen.''')
R(A_, '''            if g["ergebnis"] == "gepoolt":
                # Uneinig: die gepoolten Mediane beider Messungen entscheiden (messgeraet.gewinn_bestaetigen).
                basis_paar, mess = messgeraet.laufzeit_einsetzen(basis_paar, mess, g["einsetzen"])
                u = messgeraet.urteil_f2(basis_paar, mess, ausgang, bereiche, urteil["wirkungskreis"], tausch,
                                         nische=k["nische"], laufzeit_ausnehmen=(best["nachmessung"] or {}).get("nicht_bestaetigt") or ())''',
  '''            if g["ergebnis"] == "gepoolt":
                # Uneinig: die gepoolten Mediane beider Messungen entscheiden (messgeraet.gewinn_bestaetigen).
                basis_paar, mess = messgeraet.laufzeit_einsetzen(basis_paar, mess, g["einsetzen"])
                u = messgeraet.urteil_f2(basis_paar, mess, ausgang, bereiche, urteil["wirkungskreis"], tausch,
                                         nische=k["nische"], laufzeit_ausnehmen=(best["nachmessung"] or {}).get("nicht_bestaetigt") or ())
            elif g.get("gewinn") and u.get("ok"):
                # Behebungsrunde 4 (Review 03 Nr. 11): im Annahmegrund nur die Bereiche, deren Gewinn bestätigt ist (klar
                # unter dem Band oder in beiden Messungen) — nicht ein Bereich, dessen Gewinn die Nachmessung verwarf.
                u = messgeraet.gewinne_beschraenken(u, g.get("bestaetigte_bereiche") or [])''')
R(A_, '''    # Verhaltensvergleich (T3, K2934/K3121): Nur wer das Maß besteht, wird zusätzlich gegen „schneller,
    # aber falsch" geprüft — Vorgeneration und Kandidat laufen durch dieselbe Sonde. Jede Abweichung braucht
    # einen Test, der an der Vorgeneration fällt, am Kandidaten besteht und die Funktion aufruft.
    behoben = fb - fk''', '''    # Verhaltensvergleich (T3, K2934/K3121): Nur wer das Maß besteht, wird zusätzlich gegen „schneller,
    # aber falsch" geprüft — Vorgeneration und Kandidat laufen durch dieselbe Sonde. Jede Abweichung braucht
    # einen Test, der an der Vorgeneration fällt, am Kandidaten besteht, die Funktion im Muster der Abweichung ruft und
    # sie festhält (Deckung je Muster, Verfälschungsprobe je Merkmal).
    # Entscheidung Chat-Claude 4 (Behebungsrunde 4 vor T4): Tests, die der Kandidat selbst mitbringt oder ändert, decken
    # nicht — ein Vorschlag beglaubigt seine eigene Änderung nie.
    eigene = eigene_tests(werk, tests_kandidat, vertrag_dateien_kandidat)
    behoben = (fb - fk) - eigene
    eigene_ausgeschlossen = sorted((fb - fk) & eigene)''')
R(A_, '''        # Deckung je Abweichung (Grundsatz 11): die Tests aus `behoben` laufen am Kandidaten mit Aufzeichner; eine
        # Abweichung ist gedeckt, wenn einer von ihnen die Funktion mit derselben Eingabe (und im selben Muster) ruft.''',
  '''        # Deckung je Muster (Grundsatz 11, Entscheidungen Chat-Claude): die Tests aus `behoben` laufen am Kandidaten mit
        # Aufzeichner; die Zuordnung Abweichung → Test und die Verfälschungsproben macht verhaltensvergleich.pruefen.''')
R(A_, '''    urteil["verhalten"] = verhaltensvergleich.kurz(vv)''', '''    urteil["verhalten"] = verhaltensvergleich.kurz(vv)
    urteil["verhalten"]["eigene_tests_ausgeschlossen"] = eigene_ausgeschlossen''')
# ---------------------------------------------------------------- messgeraet
M = 'kern/messgeraet.py'
R(M, '''    klar_gewinn = [b for b, q in q1.items() if q < band[b][0]]
    im_band = [b for b, q in q1.items() if band[b][0] <= q <= band[b][1]]
    if klar_gewinn or not im_band:
        return {**aus, "ergebnis": "klar", "gewinn": bool(klar_gewinn)}''', '''    klar_gewinn = [b for b, q in q1.items() if q < band[b][0]]
    im_band = [b for b, q in q1.items() if band[b][0] <= q <= band[b][1]]
    if klar_gewinn or not im_band:
        return {**aus, "ergebnis": "klar", "gewinn": bool(klar_gewinn), "bestaetigte_bereiche": sorted(klar_gewinn)}''')
R(M, '''    if g1 & g2:
        return {**aus, "ergebnis": "bestaetigt", "gewinn": True}''', '''    if g1 & g2:
        return {**aus, "ergebnis": "bestaetigt", "gewinn": True, "bestaetigte_bereiche": sorted(g1 & g2)}''')
R(M, '''def laufzeit_bestaetigen(werk: Path, bereiche: list[str], paket: str, referenzlast: str | None,''', '''def gewinne_beschraenken(u: dict, bereiche: list[str]) -> dict:
    """Behebungsrunde 4 (Review 03 Nr. 11): Laufzeitgewinne im Urteil nur für die bestätigten Bereiche; der Grund wird
    neu geschrieben. Ohne bestätigten Bereich bleibt das Urteil unverändert (dann entscheidet gewinn_bestaetigen)."""
    alle = list(u.get("laufzeit_gewinne") or [])
    behalten = [g for g in alle if g.split(".laufzeit_ms")[0] in set(bereiche)]
    if not behalten or behalten == alle:
        return u
    return {**u, "laufzeit_gewinne": behalten, "laufzeit_gewinne_unbestaetigt": [g for g in alle if g not in behalten],
            "grund": f"Nische schnell: {'; '.join(behalten)} Kernmaß {u.get('kern_basis')} → {u.get('kern_kandidat')} "
                     f"(nur bestätigte Gewinne)"}


def laufzeit_bestaetigen(werk: Path, bereiche: list[str], paket: str, referenzlast: str | None,''')
# ---------------------------------------------------------------- lauf (Generalprobe: nur bestätigte Gewinne)
L_ = 'lauf.py'
R(L_, '''            if not g["gewinn"]:
                gew = []''', '''            if not g["gewinn"]:
                gew = []
            elif g["ergebnis"] in ("klar", "bestaetigt"):
                # Behebungsrunde 4 (Review 03 Nr. 11): nur bestätigte Gewinnbereiche im Annahmegrund.
                gew = [x for x in gew if x.split(":")[0] in set(g.get("bestaetigte_bereiche") or [])] or gew''')

fehl = [(d, a[:70], dateien[d].count(a)) for d, a, b, n in ops if dateien[d].count(a) != n]
if fehl:
    raise SystemExit(f'Anker fehlen/mehrdeutig, nichts geschrieben: {fehl}')
for d, a, b, n in ops:
    dateien[d] = dateien[d].replace(a, b)
for d, t in dateien.items():
    (B / d).write_text(t)
    py_compile.compile(str(B / d), doraise=True)
print(f'Deckung/Annahme: {len(ops)} von {len(ops)} Ersetzungen in {len(dateien)} Dateien, kompiliert')
