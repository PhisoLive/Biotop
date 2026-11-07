"""Behebungsrunde 4 vor T4 — Nachtrag nach dem Commit 1d9a5aa (alles-oder-nichts, erst NACH dem Ende des Commit-Jobs):
1. R4-3 zweiter Teil (Review 03 Nr. 3, hoch): bricht die Referenzlast UNTER DER SONDE an der Vorgeneration ab, hat die
   Sonde sie gestört — ohne Sonde lief sie (die Messung der Vorgeneration verlangt einen Laufzeitwert je Bereich).
   Bisher still; jetzt Messgerätausfall (SondeAusgefallen → zurückgestellt, gezählt). Ein Abbruch nur am Kandidaten
   bleibt eine Abweichung (Befund über den Kandidaten). Zwei Tests (Probe, Gegenprobe).
2. Entscheidung 5: Tests für kern/gegenzeugen.torzeile_schwaechen (die Funktion kam im Commit ohne eigenen Test):
   80 % erfüllt, eine verändertes Normalverhalten kippt die Zeile, nicht beurteilbar zählt nie als behoben, null
   Schwächen sind nicht erfüllt.
"""
import py_compile
from pathlib import Path

V = Path('/root/biotop/biotop/organe/verhaltensvergleich.py')
T = Path('/root/biotop/tests/test_vor_t4_04.py')
v, t = V.read_text(), T.read_text()
alt = '''    gleich = dict(signaturen=alt.get("signaturen"), beispiele=alt.get("beispiele"), konstruktion=alt.get("konstruktion"),
                  korpus_erweitert=korpus_erweitert)'''
neu = '''    # Behebungsrunde 4 (R4-3, Review 03 Nr. 3): eine Bereichslast, die unter der Sonde an der VORGENERATION abbricht, hat
    # die Sonde gestört (ohne Sonde lief sie — die Messung der Vorgeneration verlangt einen Laufzeitwert je Bereich):
    # Messgerätausfall statt stiller Lücke.
    b_alt = alt.get("beobachtungen") or {}
    abbruch = sorted(k for k, w in b_alt.items() if k.startswith("korpus:last_") and str(w).startswith("Fehler"))
    if abbruch:
        raise SondeAusgefallen("Referenzlast bricht unter der Sonde an der Vorgeneration ab ("
                               + ", ".join(f"{k} {b_alt.get(k)}" for k in abbruch[:3])
                               + ") — die Sonde stört die Last; ohne Sonde lief sie")
    gleich = dict(signaturen=alt.get("signaturen"), beispiele=alt.get("beispiele"), konstruktion=alt.get("konstruktion"),
                  korpus_erweitert=korpus_erweitert)'''
if v.count(alt) != 1:
    raise SystemExit('Anker fehlt, nichts geschrieben')
v = v.replace(alt, neu)
t += '''

# ================================================================ Nachtrag: R4-3 zweiter Teil — Lastabbruch unter der Sonde
def _gestellt(tmp_path, monkeypatch, alt_last, neu_last):
    w = tmp_path / "w"
    (w / "paket").mkdir(parents=True)
    alt = {"gueltig": True, "beobachtungen": {"korpus:last_paket": alt_last, "paket.a:f#0": "1"}, "inhalt": {"paket.a:f": 1},
           "eingewickelt": {"paket.a": ["f"]}}
    neu = {"gueltig": True, "beobachtungen": {"korpus:last_paket": neu_last, "paket.a:f#0": "1"}, "inhalt": {"paket.a:f": 1},
           "eingewickelt": {"paket.a": ["f"]}}
    folge = iter([alt, alt, neu])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: dict(next(folge)))
    return w


def test_r43_lastabbruch_unter_der_sonde_an_der_vorgeneration_ist_ausfall(tmp_path, monkeypatch):
    """Review 03 Nr. 3: an 0aac612 fehlten die Lastbeobachtungen still, die Änderung blieb unsichtbar."""
    w = _gestellt(tmp_path, monkeypatch, "Fehler:AttributeError", "Fehler:AttributeError")
    with pytest.raises(vv.SondeAusgefallen, match="bricht unter der Sonde"):
        vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {})


def test_r43_gegenprobe_abbruch_nur_am_kandidaten_ist_befund(tmp_path, monkeypatch):
    w = _gestellt(tmp_path, monkeypatch, "ok", "Fehler:AttributeError")
    r = vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {})
    assert r["tragfaehig"] is False and "korpus:last_paket" in r["abweichungen"], r


# ================================================================ Nachtrag: Entscheidung 5 — Torzeile „Schwächen“
from biotop.kern import gegenzeugen  # noqa: E402

_WEG = {"verletzt": False}
_DA = {"verletzt": True}
_GLEICH = {"faelle": 100, "abweichungen": 0}
_ANDERS = {"faelle": 100, "abweichungen": 7}


@pytest.mark.parametrize("schwaechen,behoben,erfuellt", [
    ({f"S{i}": {"schwaeche": _WEG, "normal": _GLEICH} for i in range(1, 5)} | {"S5": {"schwaeche": _DA, "normal": _GLEICH}},
     4, True),                                                  # 4 von 5 doppelt behoben = 80 % → erfüllt
    ({f"S{i}": {"schwaeche": _WEG, "normal": _GLEICH} for i in range(1, 4)} | {"S4": {"schwaeche": _WEG, "normal": _ANDERS},
     "S5": {"schwaeche": _DA, "normal": _GLEICH}}, 3, False),   # Gegenprobe: S4 weg, aber Verhalten verändert → 3 von 5
    ({f"S{i}": {"schwaeche": _WEG, "normal": _GLEICH} for i in range(1, 4)} | {"S4": {"schwaeche": _WEG, "normal": None},
     "S5": {"schwaeche": _DA, "normal": _GLEICH}}, 3, False),   # nicht beurteilbar zählt nie als behoben
    ({}, 0, False),                                             # null Schwächen: nicht erfüllt
])
def test_torzeile_schwaechen_verlangt_beide_pruefungen(schwaechen, behoben, erfuellt):
    z = gegenzeugen.torzeile_schwaechen(schwaechen)
    assert len(z["behoben"]) == behoben and z["erfuellt"] is erfuellt, z["zeile"]
'''
V.write_text(v)
T.write_text(t)
py_compile.compile(str(V), doraise=True)
py_compile.compile(str(T), doraise=True)
print('Nachtrag: verhaltensvergleich 1 Ersetzung; 6 Tests angehängt (2 Lastabbruch, 4 Torzeile); kompiliert')
