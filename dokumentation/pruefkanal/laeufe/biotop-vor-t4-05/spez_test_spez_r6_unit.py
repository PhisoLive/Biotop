"""Rote Spezifikationen für den nächsten Auftrag (aus der Behebungsrunde 5, Hinweise Philipp 24.09.) — Organ und Modul,
ohne Kammer. Rot am Commit 0c2f058; die Gegenproben sind dort grün und müssen es bleiben.

R6-1 Enthaltung je Beobachtung: die Enthaltung des GANZEN Vergleichs bei unvollständiger Erfassung widerspricht
     Entscheidung 3 und schafft denselben Totalausfall wie Review 04 Nr. 4 — ein einziges schwer erfassbares Objekt
     stellt jeden Kandidaten zurück. Enthalten muss sich nur die betroffene Beobachtung; der übrige Vergleich urteilt.
R6-2 Das Tor-4-Skript berechnet jede Torzeile, die aus der Datenbank berechenbar ist (die meisten Berichtsfehler in T3
     waren Torzeilen von Hand).
Aufruf: /root/biotop-t3/venv/bin/python -m pytest spez/test_spez_r6_unit.py -q -p no:cacheprovider (cwd Arbeitsordner)"""
import sys

import pytest

sys.path.insert(0, "/root/biotop")
from biotop.organe import verhaltensvergleich as vv  # noqa: E402

G_UNVOLL = {"paket.a:g": {"StringIO: Iterator-Objekt, Elemente nicht erfasst": 1}}


def _stand(unvollstaendig: bool, f_wert: str = "1") -> dict:
    return {"gueltig": True,
            "beobachtungen": {"paket.a:f#0": f_wert, "paket.a:g#0": '{"__iterator_objekt": {"__objekt": "StringIO"}}'},
            "inhalt": {"paket.a:f": 1, "paket.a:g": 1}, "eingewickelt": {"paket.a": ["f", "g"]},
            "unvollstaendig": dict(G_UNVOLL) if unvollstaendig else {}}


def _pruefen(tmp_path, monkeypatch, unvollstaendig: bool, f_neu: str = "1") -> dict:
    """Gestellte Sonde je Stand: Vorgeneration zweimal (S-4), dann der Kandidat. Nur g ist schwer erfassbar."""
    w = tmp_path / "w"
    (w / "paket").mkdir(parents=True)
    folge = iter([_stand(unvollstaendig), _stand(unvollstaendig), _stand(unvollstaendig, f_neu)])
    monkeypatch.setattr(vv, "beobachten", lambda *a, **k: next(folge))
    return vv.pruefen(w, {"paket/a.py": "x"}, "last", ["paket"], {"tests": [], "aufrufe": []})


def test_r6_1_nur_die_betroffene_beobachtung_enthaelt_sich(tmp_path, monkeypatch):
    """ROT an 0c2f058: grund_art 'unvollstaendig_erfasst' — der ganze Vergleich enthält sich, aegis stellt zurück,
    obwohl nur g schwer erfassbar ist und keine Beobachtung abweicht. Soll: geurteilt, tragfähig, g als Enthaltung
    gezählt (1 von 2 beobachtet)."""
    r = _pruefen(tmp_path, monkeypatch, True)
    assert r["geurteilt"] is True and r["tragfaehig"] is True, (r.get("grund_art"), r.get("grund"))
    assert r["beobachtete_funktionen"] == "1 von 2", r["beobachtete_funktionen"]
    assert r["enthaltungen"].get("paket.a:g", "").startswith("unvollständig erfasst"), r["enthaltungen"]


def test_r6_1_gegenprobe_ohne_unvollstaendige_erfassung(tmp_path, monkeypatch):
    """GRÜN an 0c2f058 und danach: dieselben Stände ohne unvollständige Erfassung — geurteilt, tragfähig, 2 von 2."""
    r = _pruefen(tmp_path, monkeypatch, False)
    assert r["geurteilt"] is True and r["tragfaehig"] is True and r["beobachtete_funktionen"] == "2 von 2", r


def test_r6_1_gegenprobe_echte_abweichung_lehnt_weiter_ab(tmp_path, monkeypatch):
    """GRÜN an 0c2f058 und danach: weicht f ungedeckt ab, lehnt der Vergleich ab — die Enthaltung von g verschluckt
    keine Abweichung einer vollständig erfassten Beobachtung."""
    r = _pruefen(tmp_path, monkeypatch, True, f_neu="2")
    assert r["tragfaehig"] is False and "paket.a:f#0" in (r.get("ungedeckt") or []), r


# Zeilen von Tor 4 (Fassung 8), deren Zahlen die Lauf-Datenbank trägt (vorspann_nachweise, protokoll, generationen,
# kandidaten, immunsystem, neutralzaehler, kasse, laeufe). Nicht darunter: Aufnahme (Werk und Altlastenliste — zu
# prüfen), Verdrahtung (Regression), Reviewdurchgang und Zwischenbericht.
DB_BERECHENBAR = ("Generation minus eins", "Generation 0", "Kein Rückschritt", "Halluzinationsprobe",
                  "Verhaltensvergleich", "Doppelungsanteil", "Immunisierung", "Neutralzähler", "Verbundausfall",
                  "Sättigung oder Budgetabbruch")


def test_r6_2_tor4_berechnet_jede_aus_der_datenbank_berechenbare_zeile():
    """ROT an 0c2f058: tor4 berechnet nur „Schwächen“ und führt die übrigen Zeilen als „nicht berechnet“."""
    from biotop import tor4
    offen = sorted(set(DB_BERECHENBAR) & set(tor4.NICHT_BERECHNET))
    assert not offen, f"Tor-4-Skript berechnet nicht (aus der Datenbank berechenbar): {offen}"
