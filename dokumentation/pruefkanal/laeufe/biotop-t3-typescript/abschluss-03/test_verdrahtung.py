"""Verdrahtungsnachweis: Jedes Organ unter biotop/organe/ muss in einem echten Lauf aufgerufen werden.

Anlass (T3, Lauf 38): `verhaltensvergleich` und `masseichung` waren gebaut, mit 18 grünen Tests belegt und gegen
das Modul gegengeprüft — und von keinem Laufpfad aufgerufen. Die Regel „eine Zählstelle, die buchen kann, ist
nicht ein Lauf, der bucht" stand schon in den Notizen; sie hat zweimal nicht gereicht. Deshalb ein Test statt einer
Regel: Ein Organ, das existiert und nie gerufen wird, macht die Regression rot.

Wie: Ein vollständiger Lauf über die Befehlszeile, wie ihn die Laufskripte fahren (lauf anlegen → einlegen →
verfassung → vertraege → kartieren → vorspann → gen0 → mass → generation → freigabe), am kleinsten Prüfwerk
(tests/drahtwerk.py). Vorher wird jede Funktion jedes Organmoduls mit einem Aufzeichner umhüllt; die Organliste
kommt aus dem Verzeichnis, ein neues Organ ist also automatisch erfasst.

Grenzen des Nachspiels, alle an der Grenze und nicht am Organ:
- Kammer: echt (Docker, netzlos, Image biotop-kammer:ts1).
- Anbieter: ersetzt durch eine gestellte Grenze, die feste Texte liefert (0 Token, 0 €). Netz ist gesperrt
  (conftest). Zwei Schwarmantworten entfernen dieselbe tote Funktion — gleich gut, also entscheidet die Jury.
- Ablageorte (Werke, Lazarus-Archiv, Referenzlast, Datenbank) liegen im Testverzeichnis: Ein Nachspiel darf
  keinen echten Schnappschuss überschreiben (lauf1-gen0 gibt es in daten/lazarus schon).
"""
from __future__ import annotations

import functools
import importlib
import importlib.util
import inspect
import json
import os
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import drahtwerk  # noqa: E402

ORGANE = Path(__file__).resolve().parents[1] / "biotop" / "organe"
# Die Funktion, die ein Lauf je Kandidat zur Annahme ruft (lauf._generation_koerper und lauf._verhandeln).
ANNAHMEPFAD = "biotop.organe.aegis:pruefen"
PFLICHT_IM_ANNAHMEPFAD = ("masseichung.anwenden", "verhaltensvergleich.pruefen")


# ---------------------------------------------------------------- Prüfwerkzeug (Wurzel als Argument)
def organe_finden(wurzel: Path) -> list[str]:
    """Alle Organmodule eines Verzeichnisses (ohne __init__)."""
    return sorted(p.stem for p in Path(wurzel).glob("*.py") if p.stem != "__init__")


def aufzeichnen(module: dict, monkeypatch, kanten: set | None = None) -> dict[str, str]:
    """Umhüllt jede im Modul definierte Funktion. Rückgabe: {organ: erster Aufrufer} — füllt sich beim Laufen.

    Mit `kanten` wird zusätzlich jede Aufrufkante „organ.funktion ← aufrufendes_modul:funktion" gesammelt (der
    Aufrufer ist der erste Rahmen außerhalb des Organs). Daran lässt sich prüfen, WER ein Organ ruft — nicht nur, ob.
    """
    gerufen: dict[str, str] = {}

    def huelle(organ: str, name: str, f):
        @functools.wraps(f)
        def aufgezeichnet(*a, **k):
            if organ not in gerufen or kanten is not None:
                rahmen = sys._getframe(1)
                aufrufer = "?"
                while rahmen is not None:
                    mod = rahmen.f_globals.get("__name__", "")
                    # Organinterne Rahmen und die Rahmen dieser Aufzeichnerhüllen selbst überspringen — sonst hieße
                    # der Aufrufer einer organinternen Hilfsfunktion „aufgezeichnet" statt des echten Aufrufers.
                    if (mod != module[organ].__name__ and rahmen.f_code is not aufgezeichnet.__code__
                            and not mod.startswith(("functools", "contextlib"))):
                        aufrufer = f"{mod}:{rahmen.f_code.co_name}"
                        break
                    rahmen = rahmen.f_back
                gerufen.setdefault(organ, f"{organ}.{name} ← {aufrufer}")
                if kanten is not None:
                    kanten.add(f"{organ}.{name} ← {aufrufer}")
            return f(*a, **k)
        return aufgezeichnet

    for organ, mod in module.items():
        for name, obj in list(vars(mod).items()):
            if inspect.isfunction(obj) and obj.__module__ == mod.__name__:
                monkeypatch.setattr(mod, name, huelle(organ, name, obj))
    return gerufen


def nie_gerufen(organe: list[str], gerufen: dict) -> list[str]:
    return sorted(o for o in organe if o not in gerufen)


def nicht_im_annahmepfad(kanten: set, annahmepfad: str, pflicht: tuple[str, ...]) -> list[str]:
    """Pflichtfunktionen, die in keinem Aufruf aus der Annahmefunktion vorkommen (irgendwo anders gerufen zählt nicht)."""
    return sorted(p for p in pflicht if not any(k == f"{p} ← {annahmepfad}" for k in kanten))


# ---------------------------------------------------------------- Gegenproben des Prüfwerkzeugs (schnell)
def _modul_aus_datei(pfad: Path):
    spec = importlib.util.spec_from_file_location(f"verdrahtung_probe_{pfad.stem}", pfad)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_pruefwerkzeug_meldet_organ_das_existiert_und_nie_gerufen_wird(tmp_path, monkeypatch):
    """Gegenprobe: ohne sie bestünde auch ein Prüfwerkzeug, das nie etwas meldet."""
    wurzel = tmp_path / "organe"
    wurzel.mkdir()
    (wurzel / "__init__.py").write_text("")
    (wurzel / "wach.py").write_text("def arbeiten(x):\n    return _hilfe(x)\n\ndef _hilfe(x):\n    return x + 1\n")
    (wurzel / "geist.py").write_text("def pruefen(x):\n    return x\n")
    organe = organe_finden(wurzel)
    assert organe == ["geist", "wach"]
    module = {o: _modul_aus_datei(wurzel / f"{o}.py") for o in organe}
    kanten: set = set()
    gerufen = aufzeichnen(module, monkeypatch, kanten)
    assert module["wach"].arbeiten(1) == 2
    assert nie_gerufen(organe, gerufen) == ["geist"]
    assert gerufen["wach"].startswith("wach.arbeiten ← ")
    # Kanten: der Aufrufer ist der erste Rahmen außerhalb des Organs — auch für die interne Hilfsfunktion.
    hier = f"{__name__}:test_pruefwerkzeug_meldet_organ_das_existiert_und_nie_gerufen_wird"
    assert kanten == {f"wach.arbeiten ← {hier}", f"wach._hilfe ← {hier}"}, kanten
    module["geist"].pruefen(3)
    assert nie_gerufen(organe, gerufen) == []
    assert f"geist.pruefen ← {hier}" in kanten


def test_pruefwerkzeug_verlangt_den_aufruf_aus_der_annahmefunktion():
    """Gegenprobe zur Pflicht im Annahmepfad: gerufen, aber nur von anderswo (Zustand Lauf 38: masseichung.eichen
    lief im Vorspann, anwenden nie im Annahmepfad) muss gemeldet werden; der Aufruf aus der Annahmefunktion nicht."""
    pfad = "biotop.organe.aegis:pruefen"
    pflicht = ("masseichung.anwenden", "verhaltensvergleich.pruefen")
    nur_anderswo = {"masseichung.eichen ← biotop.organe.vorspann:_ausfuehren",
                    "masseichung.anwenden ← biotop.lauf:mass_einfrieren",
                    "verhaltensvergleich.pruefen ← nachspiel_gegenproben:main"}
    assert nicht_im_annahmepfad(nur_anderswo, pfad, pflicht) == ["masseichung.anwenden", "verhaltensvergleich.pruefen"]
    halb = nur_anderswo | {f"masseichung.anwenden ← {pfad}"}
    assert nicht_im_annahmepfad(halb, pfad, pflicht) == ["verhaltensvergleich.pruefen"]
    voll = halb | {f"verhaltensvergleich.pruefen ← {pfad}"}
    assert nicht_im_annahmepfad(voll, pfad, pflicht) == []


def test_organliste_kommt_aus_dem_verzeichnis():
    """Ein neues Organ ist ohne Eintrag erfasst; die beiden Organe aus Lauf 38 stehen darin."""
    organe = organe_finden(ORGANE)
    assert {"verhaltensvergleich", "masseichung", "aegis", "genesis", "jury", "mentor"} <= set(organe)
    assert "__init__" not in organe


# ---------------------------------------------------------------- Gestellte Anbietergrenze
class GestellteGrenze:
    """Feste Antworten je Systemtext. Zählt jede Anfrage; macht nie einen echten Aufruf."""

    def __init__(self):
        from biotop.organe import aegis, gedaechtnis, genesis, jury
        self.aegis, self.gedaechtnis, self.genesis, self.jury = aegis, gedaechtnis, genesis, jury
        self.anfragen: list[str] = []
        self.schwarm: dict[tuple[str, str], int] = {}
        self._melder = None

    def senden(self, modell, system, nutzer, max_tokens, temperatur):
        if system == self.genesis.SYSTEM_TYPESCRIPT:
            bereich = re.search(r"HARTE MASSE DES BEREICHS (\w+)", nutzer)
            nische = "sicher" if "„Der Sichere“" in nutzer else "andere"
            schluessel = (bereich.group(1) if bereich else "?", nische)
            n = self.schwarm[schluessel] = self.schwarm.get(schluessel, 0) + 1
            self.anfragen.append(f"schwarm {schluessel} #{n}")
            if schluessel == ("alpha", "sicher") and n <= 2:
                return ("BEGRÜNDUNG: Entfernt die nie aufgerufene Funktion; tote_funktionen sinkt.\nVERTRÄGE: keine\n"
                        f"```diff\n{drahtwerk.toter_code_entfernt(n)}```\n", 0, 0)
            return "KEIN VORSCHLAG — in diesem Bereich hebt nichts ein Maß.", 0, 0
        if system == self.aegis.ANSAGE_SYSTEM:
            self.anfragen.append("ansage")
            return "KEIN ANGRIFF", 0, 0
        if system == self.jury.SYSTEM:
            self.anfragen.append("jury")
            return '{"wahl": "A", "begruendung": "Beide gleich; A ist kürzer beschrieben."}', 0, 0
        if system == self.gedaechtnis.MUSTER_SYSTEM:
            self.anfragen.append("muster")
            return "eine nie aufgerufene Funktion entfernen, wenn kein Pfad sie erreicht", 0, 0
        if "schädlichen Zwecken" in system:
            self.anfragen.append("ethik")
            return "UNBEDENKLICH\nPrüfwerk ohne Betriebszweck.", 0, 0
        if system.startswith("Du bist Kartograph"):
            self.anfragen.append("kartograph")
            return "Summiert Zahlenlisten.", 0, 0
        self.anfragen.append("sonst")
        return "KEIN VORSCHLAG", 0, 0


# ---------------------------------------------------------------- Der Nachweis am ganzen Lauf
def test_jedes_organ_wird_im_lauf_aufgerufen(tmp_path, monkeypatch, capsys):
    from biotop import __main__ as cli
    from biotop import anbieter
    from biotop import lauf as L
    from biotop.kern import kasse
    from biotop.organe import aufnahme, kammer, lazarus

    monkeypatch.setattr(kammer, "IMAGE", "biotop-kammer:ts1")
    ok, meldung = kammer.bereit()
    if not ok:
        pytest.fail("Kammer nicht bereit — der Verdrahtungsnachweis braucht die echte Kammer: " + meldung)
    d = drahtwerk.anlegen(tmp_path / "vorlage")
    monkeypatch.setattr(aufnahme, "WERKE", tmp_path / "werke")
    monkeypatch.setattr(lazarus, "ARCHIV", tmp_path / "lazarus")
    monkeypatch.setattr(L, "REFERENZLAST", d["referenzlast"])
    monkeypatch.setattr(kasse, "AUFTRAG_LAUF_AB", 1)
    monkeypatch.setattr(kasse, "AUFTRAG_BUDGET_EUR", 1.0)
    grenze = GestellteGrenze()
    monkeypatch.setattr(anbieter, "adapter", lambda name: grenze)

    organe = organe_finden(ORGANE)
    module = {o: importlib.import_module(f"biotop.organe.{o}") for o in organe}
    kanten: set = set()
    gerufen = aufzeichnen(module, monkeypatch, kanten)

    schritte = [
        ["lauf", "anlegen", "--budget", "1"],
        ["einlegen", "1", drahtwerk.NAME, str(d["werk"])],
        ["verfassung", "1", str(d["verfassung"]), str(d["regeln"]), "--von", "Verdrahtungsnachweis"],
        ["vertraege", "1", str(d["vertraege"]), "--von", "Verdrahtungsnachweis"],
        ["kartieren", "1"],
        ["vorspann", "1"],
        ["gen0", "1", "--mutanten", str(d["mutanten"])],
        ["mass", "1", "--bestaetigt-von", "Verdrahtungsnachweis"],
        ["generation", "1"],
    ]
    protokoll = []
    for s in schritte:
        rc = cli.main(s)
        aus = capsys.readouterr()
        protokoll.append({"schritt": s[0], "rc": rc, "stderr": aus.err[-1500:]})
        assert rc == 0, f"Schritt {s} scheiterte: {aus.err[-3000:]}\n{aus.out[-3000:]}"
    from biotop.kern.datenbank import verbinden
    con = verbinden()
    g = con.execute("SELECT nummer, status FROM generationen WHERE lauf_id=1 ORDER BY nummer DESC LIMIT 1").fetchone()
    assert tuple(g) == (1, "vorgelegt"), tuple(g)
    rc = cli.main(["freigabe", "1", "1", "frei", "--von", "Verdrahtungsnachweis", "--grund", "Nachspiel"])
    capsys.readouterr()
    assert rc == 0

    fehlend = nie_gerufen(organe, gerufen)
    jury_zeilen = con.execute("SELECT einstimmig, gewinner FROM jury").fetchall()
    annahmepfad = sorted(k for k in kanten if k.endswith("← " + ANNAHMEPFAD))
    beleg = {"organe": len(organe), "gerufen": len(organe) - len(fehlend), "nie_gerufen": fehlend,
             "erster_aufruf": dict(sorted(gerufen.items())), "annahmepfad": annahmepfad,
             "kanten": sorted(kanten), "schritte": protokoll,
             "anbietergrenze": grenze.anfragen, "jury": [tuple(z) for z in jury_zeilen],
             "modellkosten_eur": con.execute("SELECT COALESCE(SUM(kosten_eur),0) FROM kasse").fetchone()[0]}
    ziel = os.environ.get("T3_VERDRAHTUNG_BELEG")
    if ziel:
        Path(ziel).write_text(json.dumps(beleg, ensure_ascii=False, indent=1))
    assert fehlend == [], f"Organ existiert und wird im Lauf nie gerufen: {fehlend} (gerufen {len(organe) - len(fehlend)} von {len(organe)})"
    # Gerufen irgendwo genügt für die zwei Abwehrorgane nicht: Sie müssen in der Funktion laufen, die über die
    # Annahme entscheidet (Befund Lauf 38 — gebaut, getestet, aber nirgends im Annahmepfad).
    fehlt_im_pfad = nicht_im_annahmepfad(kanten, ANNAHMEPFAD, PFLICHT_IM_ANNAHMEPFAD)
    assert fehlt_im_pfad == [], f"{fehlt_im_pfad} wird nicht aus {ANNAHMEPFAD} gerufen — Kanten dort: {annahmepfad}"
    assert beleg["modellkosten_eur"] == 0
    assert jury_zeilen, "Die Jury hat nicht entschieden — der Gleichstand kam nicht zustande"
