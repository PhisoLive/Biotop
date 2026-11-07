"""Behebungsrunde 2 vor T4 — Laufzeit: (a) gepaarte Messung mit fehlenden Werten ist ungültig; (b) jeder Laufzeitriss
wird vor der Ablehnung einmal gepaart nachgemessen, nur ein bestätigter lehnt ab (Entscheidung Chat-Claude 23.09.);
(c) aegis.pruefen und die Generalprobe benutzen das; die Deckung je Abweichung wird in aegis angeschlossen;
(d) conftest: TS-Kammertests ohne Image rot statt übersprungen. Ersetzt benannte Anker (je genau einmal)."""
from pathlib import Path

R = Path('/root/biotop')


def datei(rel):
    return R / rel


def ersetze(p, alt, neu):
    s = p.read_text()
    assert s.count(alt) == 1, (p.name, s.count(alt), alt[:100])
    p.write_text(s.replace(alt, neu))


M = datei('biotop/kern/messgeraet.py')
ersetze(M, '''    Rückgabe {"gueltig", "n", "bereiche": {b: {"basis", "kandidat", "basis_werte", "kandidat_werte"}}, "grund", "seite"}."""''',
        '''    Rückgabe {"gueltig", "n", "bereiche": {b: {"basis", "kandidat", "basis_werte", "kandidat_werte"}}, "grund", "seite"}.
    Behebungsrunde 2 vor T4: Fehlt in einer Messung der Wert eines angeforderten Bereichs (z. B. `last_<b>` wirft am
    Kandidaten), ist die gepaarte Messung UNGÜLTIG (`seite`, `bereich`) — bisher blieb sie gültig mit `kandidat: None`,
    und `laufzeit_einsetzen` überging den Bereich still (gemessen an 330b4ec: Python-Kandidat mit Syntaxfehler, 3 von 4
    Bereichen ohne Wert, `gueltig True`). Bereiche, deren Laufzeit gar nicht geprüft wird (von der Rauschmessung
    gesperrt), fordert der Aufrufer nicht an."""''')
ersetze(M, '''            for b in bereiche:
                v = (r["bereiche"].get(b) or {}).get("laufzeit_ms")
                if v is not None:
                    werte[b][seite].append(float(v))''', '''            for b in bereiche:
                x = r["bereiche"].get(b) or {}
                v = x.get("laufzeit_ms")
                if v is None or not isinstance(v, (int, float)) or v != v or v <= 0:
                    return {"gueltig": False, "n": n, "bereiche": {}, "seite": seite, "bereich": b,
                            "grund": f"Laufzeitmessung {seite}, Durchgang {i + 1} von {n}: kein Wert für {b} "
                                     f"({str(x.get('laufzeit_fehler') or 'fehlt')[:300]})"}
                werte[b][seite].append(float(v))''')
ersetze(M, '''def laufzeit_entscheidet(u: dict, nische: str | None) -> bool:''', '''def laufzeitrisse(u: dict) -> list[str]:
    """Bereiche, deren Laufzeitgrenze im Urteil `u` gerissen ist (aus `grenzen_gerissen`)."""
    import re as _re
    return sorted({m.group(1) for g in (u.get("grenzen_gerissen") or []) if (m := _re.match(r"(\\w+)\\.laufzeit_ms:", g))})


def laufzeit_bestaetigen(werk: Path, bereiche: list[str], paket: str, referenzlast: str | None,
                         dateien_basis: dict | None, dateien_kandidat: dict | None, basis: dict, kandidat: dict,
                         urteilen, n: int | None = None) -> dict:
    """Entscheidung Chat-Claude (23.09.2026): Jeder Laufzeitriss wird vor der Ablehnung einmal GEPAART NACHGEMESSEN;
    nur ein bestätigter Riss lehnt ab. Befund vor T4: K2904 (S2-Behebung, ändert nur `planung`) wurde in 1 von 3
    Durchgängen an `eingang` ×1,224 abgelehnt, in den beiden anderen ×1,096 und ×1,012 — dieselbe Änderung, verschieden
    entschieden (Grundsatz 14).
    `urteilen(basis, kandidat, ausnehmen)` bildet das Urteil (urteil_f2) mit gepaarten Laufzeiten; `ausnehmen` =
    Bereiche, deren Riss die Nachmessung nicht bestätigt hat. Rückgabe {"urteil", "basis", "kandidat", "nachmessung"}:
    `nachmessung` None (kein Riss), sonst {"risse", "bestaetigt", "nicht_bestaetigt", "messung"}; ist die Nachmessung
    selbst ungültig, steht `ungueltig` darin (Messgerätausfall — der Aufrufer stellt zurück, er lehnt nicht ab)."""
    u = urteilen(basis, kandidat, [])
    risse = laufzeitrisse(u)
    if not risse:
        return {"urteil": u, "basis": basis, "kandidat": kandidat, "nachmessung": None}
    nm = laufzeit_gepaart(werk, risse, paket, referenzlast, dateien_basis, dateien_kandidat, n=n)
    if not nm["gueltig"]:
        return {"urteil": u, "basis": basis, "kandidat": kandidat,
                "nachmessung": {"risse": risse, "ungueltig": True, "grund": nm["grund"], "messung": nm}}
    b2, k2 = laufzeit_einsetzen(basis, kandidat, nm)
    u2 = urteilen(b2, k2, [])
    bestaetigt = sorted(set(risse) & set(laufzeitrisse(u2)))
    nicht = sorted(set(risse) - set(bestaetigt))
    if bestaetigt:
        # Bestätigt: Ablehnung mit den Werten beider Messungen; nicht bestätigte Risse zählen nicht mit.
        u3 = urteilen(b2, k2, nicht)
    else:
        # Nicht bestätigt: die erste gepaarte Messung bleibt Grundlage des übrigen Urteils (Gewinne, Nischenmaß), nur
        # die Laufzeitgrenze der nicht bestätigten Bereiche entfällt.
        b2, k2 = basis, kandidat
        u3 = urteilen(basis, kandidat, nicht)
    return {"urteil": u3, "basis": b2, "kandidat": k2,
            "nachmessung": {"risse": risse, "bestaetigt": bestaetigt, "nicht_bestaetigt": nicht,
                            "erste": {b: (kandidat["bereiche"][b].get("laufzeit_ms"), basis["bereiche"][b].get("laufzeit_ms"))
                                      for b in risse},
                            "zweite": {b: ((nm["bereiche"].get(b) or {}).get("kandidat"), (nm["bereiche"].get(b) or {}).get("basis"))
                                       for b in risse},
                            "messung": {k: v for k, v in nm.items() if k != "regel"}}}


def laufzeit_entscheidet(u: dict, nische: str | None) -> bool:''')
ersetze(M, '''               laufzeit_pruefen: bool = True) -> list[str]:
    """Grenzmaße gegen den Bezug `ausgang`''', '''               laufzeit_pruefen: bool = True, laufzeit_ausnehmen: list[str] | tuple = ()) -> list[str]:
    """Grenzmaße gegen den Bezug `ausgang`''')
ersetze(M, '''        if laufzeit_pruefen and b not in gesperrt and lz_a.get("laufzeit_ms") and k.get("laufzeit_ms"):''',
        '''        if laufzeit_pruefen and b not in gesperrt and b not in laufzeit_ausnehmen and lz_a.get("laufzeit_ms") and k.get("laufzeit_ms"):''')
ersetze(M, '''              tausch: dict | None = None, nische: str | None = None, laufzeit_pruefen: bool = True) -> dict:
    """Vollständiges Maß-Urteil Fassung 2. Rückgabe mit 'ok', 'zuwachs', 'grund', Belegen."""''',
        '''              tausch: dict | None = None, nische: str | None = None, laufzeit_pruefen: bool = True,
              laufzeit_ausnehmen: list[str] | tuple = ()) -> dict:
    """Vollständiges Maß-Urteil Fassung 2. Rückgabe mit 'ok', 'zuwachs', 'grund', Belegen.
    `laufzeit_ausnehmen`: Bereiche, deren Laufzeitriss die gepaarte Nachmessung nicht bestätigt hat (laufzeit_bestaetigen)."""''')
ersetze(M, '''                         laufzeit_pruefen=laufzeit_pruefen)
    r = {"kern_basis": k0,''', '''                         laufzeit_pruefen=laufzeit_pruefen, laufzeit_ausnehmen=laufzeit_ausnehmen)
    r = {"kern_basis": k0,''')

A = datei('biotop/organe/aegis.py')
ersetze(A, '''    if referenzlast and messgeraet.laufzeit_entscheidet(u, k["nische"]):
        lz = messgeraet.laufzeit_gepaart(werk, bereiche, paket, referenzlast, {}, code)
        urteil["laufzeit_gepaart"] = lz
        if not lz["gueltig"]:
            return _zurueckstellen(fertig, kandidat_id, "Laufzeitmessung gepaart: " + lz["grund"])
        basis_paar, mess = messgeraet.laufzeit_einsetzen(basis_paar, mess, lz)
        u = messgeraet.urteil_f2(basis_paar, mess, ausgang, bereiche, urteil["wirkungskreis"], tausch, nische=k["nische"])''',
        '''    if referenzlast and messgeraet.laufzeit_entscheidet(u, k["nische"]):
        # Nur Bereiche, deren Laufzeit geprüft wird: von der Rauschmessung gesperrte nie (grenzen_f2) — eine fehlende
        # Messung dort macht die gepaarte Messung nicht ungültig.
        lz_bereiche = [b for b in bereiche if b not in set((tausch or {}).get("_gesperrte_bereiche") or [])]
        lz = messgeraet.laufzeit_gepaart(werk, lz_bereiche, paket, referenzlast, {}, code)
        urteil["laufzeit_gepaart"] = lz
        if not lz["gueltig"]:
            return _zurueckstellen(fertig, kandidat_id, "Laufzeitmessung gepaart: " + lz["grund"])
        basis_paar, mess = messgeraet.laufzeit_einsetzen(basis_paar, mess, lz)
        # Entscheidung Chat-Claude (23.09.): jeder Laufzeitriss wird einmal gepaart nachgemessen; nur ein bestätigter lehnt ab.
        best = messgeraet.laufzeit_bestaetigen(
            werk, lz_bereiche, paket, referenzlast, {}, code, basis_paar, mess,
            lambda b_, k_, aus_: messgeraet.urteil_f2(b_, k_, ausgang, bereiche, urteil["wirkungskreis"], tausch,
                                                      nische=k["nische"], laufzeit_ausnehmen=aus_))
        urteil["laufzeit_nachmessung"] = best["nachmessung"]
        if best["nachmessung"] and best["nachmessung"].get("ungueltig"):
            return _zurueckstellen(fertig, kandidat_id, "Laufzeit-Nachmessung gepaart: " + best["nachmessung"]["grund"])
        u, basis_paar, mess = best["urteil"], best["basis"], best["kandidat"]''')
ersetze(A, '''    behoben = fb - fk
    try:
        vv = verhaltensvergleich.pruefen(
            werk, code, referenzlast, bereiche,
            lambda: verhaltensvergleich.deckende_tests(werk, testbestand_mit_vertraegen, behoben))''',
        '''    behoben = fb - fk
    try:
        # Deckung je Abweichung (Grundsatz 11): die Tests aus `behoben` laufen am Kandidaten mit Aufzeichner; eine
        # Abweichung ist gedeckt, wenn einer von ihnen die Funktion mit derselben Eingabe (und im selben Muster) ruft.
        vv = verhaltensvergleich.pruefen(
            werk, code, referenzlast, bereiche,
            lambda abw: verhaltensvergleich.deckende_aufrufe(werk, code, testbestand_mit_vertraegen, behoben))''')

L = datei('biotop/lauf.py')
ersetze(L, '''    lz = None
    if ref and messgeraet.laufzeit_entscheidet(u0, "werk"):
        lz = messgeraet.laufzeit_gepaart(pfad, bereiche, paket, ref, {},
                                         {p: i for p, i in dateien.items() if not p.startswith("tests/")})''',
        '''    lz = None
    lz_code = {p: i for p, i in dateien.items() if not p.startswith("tests/")}
    lz_bereiche = [b for b in bereiche if b not in set(tausch.get("_gesperrte_bereiche") or [])]
    nachmessung = None
    if ref and messgeraet.laufzeit_entscheidet(u0, "werk"):
        lz = messgeraet.laufzeit_gepaart(pfad, lz_bereiche, paket, ref, {}, lz_code)''')
ersetze(L, '''        basis_paar, mess = messgeraet.laufzeit_einsetzen(basis_paar, mess, lz)
    mess["kernmass_f2"] = messgeraet.kernmass_f2(mess)''', '''        basis_paar, mess = messgeraet.laufzeit_einsetzen(basis_paar, mess, lz)
        # Entscheidung Chat-Claude (23.09.): auch in der Generalprobe lehnt nur ein gepaart bestätigter Laufzeitriss ab.
        best = messgeraet.laufzeit_bestaetigen(
            pfad, lz_bereiche, paket, ref, {}, lz_code, basis_paar, mess,
            lambda b_, k_, aus_: messgeraet.urteil_f2(b_, k_, ausgang, bereiche, wirkungskreis, tausch, laufzeit_ausnehmen=aus_))
        nachmessung = best["nachmessung"]
        zusammenfassung["_laufzeit_nachmessung"] = nachmessung
        if nachmessung and nachmessung.get("ungueltig"):
            with transaktion(con):
                for b, kid in gewaehlt.items():
                    con.execute("UPDATE kandidaten SET status=?, grund=? WHERE id=?",
                                (aegis.ZURUECKGESTELLT, "Generalprobe: Messgerätausfall (Laufzeit-Nachmessung) — " + nachmessung["grund"][:300], kid))
            return _messgeraet_ausfall(con, lauf_id, nummer, abschluss, zusammenfassung,
                                       "Generalprobe: Messgerätausfall (Laufzeit-Nachmessung) — " + nachmessung["grund"], mess)
        basis_paar, mess = best["basis"], best["kandidat"]
    mess["kernmass_f2"] = messgeraet.kernmass_f2(mess)''')
ersetze(L, '''    u = messgeraet.urteil_f2(basis_paar, mess, ausgang, bereiche, wirkungskreis, tausch, laufzeit_pruefen=lz is not None)''',
        '''    u = messgeraet.urteil_f2(basis_paar, mess, ausgang, bereiche, wirkungskreis, tausch, laufzeit_pruefen=lz is not None,
                             laufzeit_ausnehmen=(nachmessung or {}).get("nicht_bestaetigt") or ())''')

C = datei('tests/conftest.py')
ersetze(C, '''    """Review vor T4 Nr. 13: Tests, die TypeScript in der Kammer parsen, brauchen das Kammerimage mit node
    (biotop-kammer:ts1). Ohne es scheiterten sie mit „executable file not found“ ohne Hinweis. Jetzt übersprungen mit
    Grund — sichtbar im Bericht der Regression, nie still."""
    import os
    from biotop.organe import kammer
    image = os.environ.get("BIOTOP_KAMMER_IMAGE") or kammer.IMAGE
    if "ts" not in image.split(":")[-1]:
        pytest.skip(f"TypeScript-Kammer nötig: BIOTOP_KAMMER_IMAGE=biotop-kammer:ts1 setzen (aktuell {image})")''',
        '''    """Tests, die TypeScript in der Kammer ausführen, brauchen das Kammerimage mit node (biotop-kammer:ts1).
    Review vor T4 Nr. 13 hatte sie ohne Image überspringen lassen; Entscheidung Chat-Claude (23.09.): ROT statt
    übersprungen — ein übersprungener Test prüft nichts (Grundsatz 7). Die Meldung nennt die Ursache."""
    import os
    from biotop.organe import kammer
    image = os.environ.get("BIOTOP_KAMMER_IMAGE") or kammer.IMAGE
    if "ts" not in image.split(":")[-1]:
        pytest.fail(f"TypeScript-Kammer nötig: BIOTOP_KAMMER_IMAGE=biotop-kammer:ts1 setzen (aktuell {image}) — "
                    f"ohne sie prüft dieser Test nichts; übersprungen gilt als rot (Grundsatz 7)", pytrace=False)''')
print('Laufzeit, aegis, lauf, conftest umgebaut')
