"""Behebungsrunde 4 vor T4 — Umbau der Python-Sonde (biotop/kern/py/verhalten.py). Alles-oder-nichts: jeder Anker muss
genau einmal vorkommen, sonst wird nichts geschrieben.
- Entscheidung 2 / R4-1: Merkmale je Formvariante (Weißraum je Zeichen, Rand vorn/hinten, Zahlform vorn/hinten).
- Entscheidung 3 / R4-16: Muster nur aus den Argumenten, die die Sonde verändert hat (Randfall: Merkmale des veränderten
  Werts; Formvariante: die von der Umformung eingeführten Merkmale; Grundliste und Lastaufrufe: gewöhnlich).
- R4-2: Verfälschung je Merkmal (nur Aufrufe, deren Eingabe das Merkmal trägt); Aufbau-/Abbaufehler und Skips = 'fehler'.
- R4-3: nur Generatoren und eingebaute Iteratoren auslesen/ersetzen; Iterator-Objekte des Werks bleiben (gezählt).
- R4-4: Zustand von Objekten mit __slots__ (auch dataclass(slots=True)).
- R4-5: Instanz aus der Signatur erproben (bis ein Methodenaufruf inhaltlich ist), sonst gezählt „ohne Inhalt“.
- R4-6: Koroutinen mit eigener Ereignisschleife beobachten, wenn keine läuft.
- R4-13: Iterator-Kappe als Teil-Enthaltung zählen (`teilweise`).
"""
import py_compile
from pathlib import Path

P = Path('/root/biotop/biotop/kern/py/verhalten.py')
s = P.read_text()
ops = []


def R(a, b, n=1):
    ops.append((a, b, n))


R("import ast  # noqa: E402\n", "import ast  # noqa: E402\nimport asyncio  # noqa: E402\n")
R("musterkarte, kopien, inhalt, unvergleichbar, instanzen = {}, {}, {}, {}, {}\n",
  "musterkarte, kopien, inhalt, unvergleichbar, instanzen = {}, {}, {}, {}, {}\n"
  "teilweise = {}          # Behebungsrunde 4: je Funktion gezählte Teil-Enthaltungen (Iterator-Kappe, Iterator-Objekt)\n")
# ---- Merkmale je Formvariante
R("""def klassen_von(werte):""", '''WEISS_SONST = set('\\x0b\\x0c\\u2028\\u2029\\u3000\\u2009')


def _text_merkmale(x):
    """Merkmale einer Zeichenkette — je Formvariante der Sonde ein eigenes Merkmal (Entscheidung Chat-Claude 2,
    Behebungsrunde 4; Review 03 Nr. 1: ein gemeinsames `weissraum` ließ einen Test mit doppeltem Leerzeichen einen
    Tab-/Zeilenumbruch-Rückschritt decken). Dieselben Namen in kern/ts/kanon.mjs."""
    m = set()
    ohne_crlf = x.replace('\\r\\n', '')
    if '\\r\\n' in x:
        m.add('crlf')
    if '\\r' in ohne_crlf:
        m.add('cr')
    if '\\n' in ohne_crlf:
        m.add('zeilenumbruch')
    if '\\t' in x:
        m.add('tab')
    if '\\u00a0' in x:
        m.add('nbsp')
    if any(c in WEISS_SONST for c in x):
        m.add('weissraum_sonst')
    if '  ' in x:
        m.add('doppelleer')
    if x != x.lstrip():
        m.add('rand_vorn')
    if x != x.rstrip():
        m.add('rand_hinten')
    if any(c.isupper() for c in x):
        m.add('gross')
    if any(c.isalpha() for c in x) and x == x.lower() and x != x.upper():
        m.add('klein')
    if re.search(r'(?<![\\d.])0\\d', x):
        m.add('zahlform_null_vorn')
    if re.search(r'\\d\\.\\d*0(?!\\d)', x):
        m.add('zahlform_null_hinten')
    if len(x) >= 40:
        m.add('lang')
    if any(ord(c) > 127 and c not in WEISS for c in x):
        m.add('nichtascii')
    return m


def klassen_von(werte):''')
R("""            if any(c in WEISS for c in x) or '  ' in x:
                out.add('weissraum')
            if x != x.strip():
                out.add('randweissraum')
            if any(c.isupper() for c in x):
                out.add('gross')
            if any(c.isalpha() for c in x) and x == x.lower() and x != x.upper():
                out.add('klein')
            if re.search(r'(?<![\\d.])0\\d|\\d\\.\\d*0(?!\\d)', x):
                out.add('zahlform')
            if len(x) >= 40:
                out.add('lang')
            if any(ord(c) > 127 and c not in WEISS for c in x):
                out.add('nichtascii')
""", """            out.update(_text_merkmale(x))
""")
R("""        elif _instanz(x):
            for v in list(vars(x).values())[:40]:
                geh(v, t + 1)
    for w in werte:
        geh(w, 0)
    return out""", """        elif _instanz(x):
            for v in list(_felder(x).values())[:40]:
                geh(v, t + 1)
    for w in werte:
        geh(w, 0)
    return out""")
# ---- Iteratoren und Koroutinen
R("""def _iter_art(v):
    if inspect.iscoroutine(v) or inspect.isasyncgen(v) or inspect.isawaitable(v):
        return 'async'
    if isinstance(v, (str, bytes, bytearray, list, tuple, dict, set, frozenset, range)) or not hasattr(v, '__next__'):
        return None
    return 'iter'""", """def _iter_art(v):
    if inspect.iscoroutine(v) or inspect.isasyncgen(v) or inspect.isawaitable(v):
        return 'async'
    if isinstance(v, (str, bytes, bytearray, list, tuple, dict, set, frozenset, range)) or not hasattr(v, '__next__'):
        return None
    # Behebungsrunde 4 (Review 03 Nr. 3): nur Generatoren und Iteratoren der Standardbibliothek auslesen und ersetzen.
    # Ein Iterator-Objekt des Werks (eigene Klasse, eigene Attribute) bleibt unverändert — der Aufrufer liest womöglich
    # Attribute (gemessen: die Last brach sonst still ab, eine spätere Änderung blieb unsichtbar).
    if inspect.isgenerator(v) or type(v).__module__ in ('builtins', 'itertools', 'collections', '_collections', 'csv'):
        return 'iter'
    return 'objekt'


def _teil(name, art):
    if name:
        d = teilweise.setdefault(name, {})
        d[art] = d.get(art, 0) + 1


def _koroutine_ausfuehren(v):
    \"\"\"Koroutine in einer eigenen Ereignisschleife ausführen, wenn keine läuft (Review 03 Nr. 7). Rückgabe
    (ergebnis, fehler) oder None, wenn eine Schleife läuft (dann bleibt es bei „unvergleichbar“).\"\"\"
    try:
        asyncio.get_running_loop()
        return None
    except RuntimeError:
        pass
    schleife = asyncio.new_event_loop()
    try:
        try:
            return schleife.run_until_complete(v), None
        except BaseException as e:  # noqa: B902 — ein Fehler der Koroutine ist beobachtetes Verhalten
            return None, e
    finally:
        schleife.close()


async def _fertig(ergebnis, fehler):
    if fehler is not None:
        raise fehler
    return ergebnis""")
R("""    art = _iter_art(v)
    if art == 'async':
        if name:
            unvergleichbar[name] = unvergleichbar.get(name, 0) + 1
        return {'text': '__async', 'roh': v, 'inhaltlich': False}""", """    art = _iter_art(v)
    if art == 'async' and inspect.iscoroutine(v):
        r = _koroutine_ausfuehren(v)
        if r is not None:
            ergebnis, fehler = r
            if fehler is not None:
                return {'text': 'Fehler:' + type(fehler).__name__, 'roh': _fertig(None, fehler), 'inhaltlich': False}
            try:
                text = text_von({'__async': ergebnis})
            except Exception as e:  # noqa: BLE001
                return {'text': '__unkanonisch:' + type(e).__name__, 'roh': _fertig(ergebnis, None), 'inhaltlich': False}
            if name:
                inhalt[name] = inhalt.get(name, 0) + 1
            return {'text': text, 'roh': _fertig(ergebnis, None), 'inhaltlich': True}
    if art == 'async':
        if name:
            unvergleichbar[name] = unvergleichbar.get(name, 0) + 1
        return {'text': '__async', 'roh': v, 'inhaltlich': False}
    if art == 'objekt':
        _teil(name, 'iterator_objekt')
        try:
            text = text_von({'__iterator_objekt': v})
        except Exception as e:  # noqa: BLE001
            return {'text': '__unkanonisch:' + type(e).__name__, 'roh': v, 'inhaltlich': False}
        if name:
            inhalt[name] = inhalt.get(name, 0) + 1
        return {'text': text, 'roh': v, 'inhaltlich': True}""")
R("""        mehr = fehler is None and len(elemente) > ITER_KAPPE
""", """        mehr = fehler is None and len(elemente) > ITER_KAPPE
        if mehr:
            _teil(name, 'iterator_gekappt')         # Review 03 Nr. 16: ab Element ITER_KAPPE + 1 unsichtbar — gezählt
""")
# ---- Objekte mit __slots__
R("""def _instanz(x):
    return hasattr(x, '__dict__') and not isinstance(""", """def _slotnamen(x):
    namen = []
    for k in type(x).__mro__:
        s = k.__dict__.get('__slots__', ())
        if isinstance(s, str):
            s = (s,)
        namen += [n for n in s if n not in ('__dict__', '__weakref__') and n not in namen]
    return namen


def _felder(x):
    \"\"\"Zustand eines Objekts: __dict__ UND __slots__ (Review 03 Nr. 4: Slot-Klassen und dataclass(slots=True) hatten
    keinen Zustandsvergleich — 0 statt 28 Abweichungen).\"\"\"
    d = dict(vars(x)) if hasattr(x, '__dict__') else {}
    for n in _slotnamen(x):
        if n not in d and hasattr(x, n):
            d[n] = getattr(x, n)
    return d


def _felder_setzen(x, d):
    slots = _slotnamen(x)
    if hasattr(x, '__dict__'):
        vars(x).clear()
    for n in slots:
        if n not in d and hasattr(x, n):
            try:
                object.__delattr__(x, n)
            except Exception:  # noqa: BLE001
                pass
    for k, v in d.items():
        try:
            if k in slots or not hasattr(x, '__dict__'):
                object.__setattr__(x, k, v)
            else:
                vars(x)[k] = v
        except Exception:  # noqa: BLE001 — eingefroren oder schreibgeschützt: bleibt, wie es ist
            pass


def _instanz(x):
    return (hasattr(x, '__dict__') or bool(_slotnamen(x))) and not isinstance(""")
R("""        elif _instanz(x):
            seen.add(id(x)); log.append((x, dict(vars(x)), 'obj'))
            for v in list(vars(x).values()):
                geh(v, t + 1)""", """        elif _instanz(x):
            seen.add(id(x)); log.append((x, _felder(x), 'obj'))
            for v in list(_felder(x).values()):
                geh(v, t + 1)""")
R("""            else:
                d = vars(o); d.clear(); d.update(kopie)""", """            else:
                _felder_setzen(o, kopie)""")
R("""            for k, v in list(vars(x).items()):
                if _zahl(v):""", """            for k, v in list(_felder(x).items()):
                if _zahl(v):""")
R("""        KONSTRUKTION[n] = {'art': 'zustand', 'z': {k: pack(v) for k, v in vars(obj).items()}, 'herkunft': 'last_zustand'}""",
  """        KONSTRUKTION[n] = {'art': 'zustand', 'z': {k: pack(v) for k, v in _felder(obj).items()}, 'herkunft': 'last_zustand'}""")
R("""        o = cls.__new__(cls)
        o.__dict__.update({k: unpack(v) for k, v in r['z'].items()})
        return o""", """        o = cls.__new__(cls)
        _felder_setzen(o, {k: unpack(v) for k, v in r['z'].items()})
        return o""")
# ---- Koroutinenfunktionen bleiben als solche erkennbar
R("""def _metadaten(w, orig):
    try:
        functools.update_wrapper(w, orig)
    except Exception:  # noqa: BLE001
        w.__wrapped__ = orig
    return w""", """def _metadaten(w, orig):
    try:
        functools.update_wrapper(w, orig)
    except Exception:  # noqa: BLE001
        w.__wrapped__ = orig
    if inspect.iscoroutinefunction(orig):
        inspect.markcoroutinefunction(w)
    return w""")
# ---- Entscheidung 3: Lastaufrufe gewöhnlich
R("""        # Muster = Merkmalsklassen ALLER vereinheitlichten Argumente — dieselbe Rechnung wie im Aufzeichner der
        # deckenden Tests (deck_wickeln), damit „Test ruft dasselbe Muster“ auf beiden Seiten gleich gemessen ist.
        kl = _klassen_sicher(lambda: klassen_von(_gebunden(orig, args, kwargs, ohne_erstes)))
        erst = muster(f'{name}#{i}', args, kwargs, orig, name, kl=kl)""", """        # Lastaufruf: die Sonde hat kein Argument verändert — Muster gewöhnlich (Entscheidung Chat-Claude 3,
        # Behebungsrunde 4: Merkmale nicht veränderter Argumente gehören nicht zum Muster).
        erst = muster(f'{name}#{i}', args, kwargs, orig, name, kl=[])""")
# ---- R4-2: Verfälschung je Merkmal
R("""        if vf:
            if vf.get('f') != name:
                return orig(*args, **kwargs)
            if vf.get('art') == 'zustand':""", """        if vf:
            if vf.get('f') != name:
                return orig(*args, **kwargs)
            # Behebungsrunde 4 (Review 03 Nr. 2): nur Aufrufe verfälschen, deren Eingabe das Merkmal des Musters trägt —
            # sonst „hält“ ein Test fest, der das Merkmal nur nebenbei ruft und etwas anderes zusichert.
            m = vf.get('merkmal') or ''
            if m and m not in _klassen_sicher(lambda: klassen_von(_gebunden(orig, args, kwargs, ohne_erstes))):
                return orig(*args, **kwargs)
            if vf.get('art') == 'zustand':""")
R("""            def pytest_runtest_logreport(self, report):
                datei, _, rest = report.nodeid.partition('::')
                tid = os.path.basename(datei) + '::' + rest
                if report.when == 'call' or report.outcome != 'passed':
                    ZUSTAND[tid] = 'pass' if report.outcome == 'passed' and ZUSTAND.get(tid, 'pass') == 'pass' else 'fail'""",
  """            def pytest_runtest_logreport(self, report):
                datei, _, rest = report.nodeid.partition('::')
                tid = os.path.basename(datei) + '::' + rest
                # Behebungsrunde 4 (Review 03 Nr. 2): festhalten heißt „die Zusicherung im Test fällt“ — ein Fehler in
                # Aufbau/Abbau (Fixture) oder ein Skip ist 'fehler', kein 'fail'.
                if report.when == 'call' and ZUSTAND.get(tid) != 'fehler':
                    ZUSTAND[tid] = 'pass' if report.outcome == 'passed' else ('fail' if report.outcome == 'failed' else 'fehler')
                elif report.when != 'call' and report.outcome != 'passed':
                    ZUSTAND[tid] = 'fehler'""")
# ---- Entscheidung 3 im Korpus: Muster aus den veränderten Argumenten
R("""def formvarianten(quellen):""", """def _muster_von(liste, bezug, korpusart):
    \"\"\"Muster eines Korpusaufrufs (Entscheidung Chat-Claude 3, Behebungsrunde 4): nur die Argumente, die die Sonde
    gegenüber `bezug` verändert hat. Randfall: die Merkmale der veränderten Werte; Formvariante: die Merkmale, die die
    Umformung eingeführt hat (Merkmale danach minus davor). Keine Veränderung (Grundliste): gewöhnlich, [].\"\"\"
    var = [j for j in range(len(liste)) if j >= len(bezug) or _json(liste[j]) != _json(bezug[j])]
    if not var:
        return []
    try:
        neu = klassen_von([unpack(liste[j]) for j in var])
        if korpusart == 'form':
            neu = neu - klassen_von([unpack(bezug[j]) for j in var if j < len(bezug)])
        return sorted(neu)
    except Exception:  # noqa: BLE001
        return ['__unbestimmt']


def formvarianten(quellen):""")
R("""                listen.append((grund[:j] + [v] + grund[j + 1:], art))
    gesehen, out = set(), []
    for l, art in listen:
        s = _json(l)
        if s not in gesehen:
            gesehen.add(s); out.append((l, art))
    return out[:FORM_KAPPE]""", """                listen.append((grund[:j] + [v] + grund[j + 1:], art, grund))
    gesehen, out = set(), []
    for l, art, q in listen:
        s = _json(l)
        if s not in gesehen:
            gesehen.add(s); out.append((l, art, q))
    return out[:FORM_KAPPE]""")
R("""            laeufe = [('rand', i, l, None) for i, l in enumerate(listen)] + [('form', j, l, a) for j, (l, a) in enumerate(formen)]
            for korpusart, i, liste, formart in laeufe:""", """            laeufe = ([('rand', i, l, None, grund) for i, l in enumerate(listen)]
                      + [('form', j, l, a, q) for j, (l, a, q) in enumerate(formen)])
            for korpusart, i, liste, formart, bezug in laeufe:""")
R("""                # Muster = Merkmalsklassen aller Argumente (wie im Aufzeichner), bei Formvarianten zusätzlich die Formart.
                kl = _klassen_sicher(lambda: klassen_von(_gebunden(fn, voll, {}, art not in ('fn', 'static'))))
                if korpusart == 'form':
                    kl = sorted(set(kl) | {formart})
                erst = muster(schl, voll, {}, fn, name, kl=kl)""", """                erst = muster(schl, voll, {}, fn, name, kl=_muster_von(liste, bezug, korpusart))""")
# ---- Text-Formvarianten mit eigenen Arten (Beschriftung; das Muster rechnet _muster_von)
R("""        out += [(s.replace(' ', r), 'weissraum') for r in ('\\t', '\\n', '  ', '\\r\\n', '\\u00a0')]
    out += [(' ' + s, 'randweissraum'), (s + ' ', 'randweissraum'), ('\\t' + s + '\\n', 'randweissraum')]""",
  """        out += [(s.replace(' ', r), a) for r, a in (('\\t', 'tab'), ('\\n', 'zeilenumbruch'), ('  ', 'doppelleer'),
                                                     ('\\r\\n', 'crlf'), ('\\u00a0', 'nbsp'))]
    out += [(' ' + s, 'rand_vorn'), (s + ' ', 'rand_hinten'), ('\\t' + s + '\\n', 'rand_tab_zeilenumbruch')]""")
# ---- R4-5: Instanz aus der Signatur erproben
R("""def korpus_randfaelle(module, signaturen):""", """def instanz_erproben(n, signaturen):
    \"\"\"Behebungsrunde 4 (Review 03 Nr. 6): ohne Rezept aus Vertrag oder Last baute die Sonde die Instanz nur mit der
    ersten Argumentliste der Signatur von __init__ (ohne Annotation: 'a b') — jede Methode warf, eine geänderte Methode
    blieb still. Jetzt die Argumentlisten der Reihe nach, bis eine Instanz entsteht, an der mindestens eine öffentliche
    Methode oder Eigenschaft mit ihrer Grundliste fehlerfrei antwortet; diese Liste wird Rezept (Herkunft
    'signatur_erprobt', gilt für beide Stände). Keine solche Liste: 'signatur_ohne_inhalt' (gezählter Enthaltungsgrund).\"\"\"
    cls = KLASSEN[n]
    modul, _, klasse = n.partition(':')
    try:
        ps = [p for p in list(inspect.signature(cls).parameters.values())
              if p.default is inspect.Parameter.empty and p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)]
    except (TypeError, ValueError):
        ps = []
    typen = ['' if p.annotation is inspect.Parameter.empty else
             (p.annotation if isinstance(p.annotation, str) else getattr(p.annotation, '__name__', str(p.annotation)))
             for p in ps]
    listen = argumentlisten(typen, None)[:12] if typen else [[]]
    mitglieder = [(f, t) for f, t in (signaturen.get(modul) or {}).items() if f.startswith(klasse + '.')]
    TIEFE[0] += 1
    try:
        for liste in listen:
            try:
                o = cls(*[unpack(v) for v in liste])
            except BaseException:  # noqa: B902
                continue
            for f, t in mitglieder:
                z = _ziel(modul, f)
                if z is None or z[1] not in ('inst', 'prop', 'cprop'):
                    continue
                grund = (argumentlisten(t or [], None) or [[]])[0]
                try:
                    wert_ = z[0](o, *[unpack(v) for v in grund])
                    if inspect.iscoroutine(wert_):
                        wert_.close()
                        continue
                    text_von(wert_)
                except BaseException:  # noqa: B902
                    continue
                KONSTRUKTION[n] = {'art': 'aufruf', 'args': [pack(v) for v in liste], 'kwargs': {},
                                   'herkunft': 'signatur_erprobt'}
                return True
    finally:
        TIEFE[0] -= 1
    instanzen[n] = 'signatur_ohne_inhalt'
    return False


def korpus_randfaelle(module, signaturen):""")
R("""    for n in sorted(KLASSEN):
        instanzen.setdefault(n, ((REQ.get('konstruktion') or KONSTRUKTION).get(n) or {}).get('herkunft') or 'signatur')""",
  """    if REQ.get('konstruktion') is None:
        for n in sorted(KLASSEN):
            if n not in KONSTRUKTION:
                instanz_erproben(n, signaturen)
    for n in sorted(KLASSEN):
        instanzen.setdefault(n, ((REQ.get('konstruktion') or KONSTRUKTION).get(n) or {}).get('herkunft') or 'signatur')""")
R("""           'korpus_erweitert': ERWEITERT[0], 'nicht_ladbar': nicht_ladbar, 'erreicht': erreicht}""",
  """           'korpus_erweitert': ERWEITERT[0], 'nicht_ladbar': nicht_ladbar, 'erreicht': erreicht, 'teilweise': teilweise}""")

fehl = [(a[:70], s.count(a)) for a, b, n in ops if s.count(a) != n]
if fehl:
    raise SystemExit(f'Anker fehlen/mehrdeutig, nichts geschrieben: {fehl}')
for a, b, n in ops:
    s = s.replace(a, b)
P.write_text(s)
py_compile.compile(str(P), doraise=True)
print(f'verhalten.py: {len(ops)} von {len(ops)} Ersetzungen, {len(s.splitlines())} Zeilen, kompiliert')
