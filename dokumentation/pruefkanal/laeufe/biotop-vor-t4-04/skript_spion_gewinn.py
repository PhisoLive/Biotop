"""pytest-Plugin (Probe, Behebungsrunde 4 vor T4): zählt, wie oft `messgeraet.gewinn_bestaetigen` aus der Generalprobe
(lauf._generation_koerper) und aus aegis.pruefen gerufen wird, und schreibt je Aufruf Ergebnis und Aufrufer nach
$SPION_AUS (JSON-Zeilen). Ändert kein Verhalten: die Originalfunktion wird unverändert gerufen.
Aufruf: PYTHONPATH=<dieser Ordner>:/root/biotop SPION_AUS=<datei> pytest -p spion_gewinn …"""
import json
import os
import sys


def pytest_configure(config):
    from biotop.kern import messgeraet
    original = messgeraet.gewinn_bestaetigen
    ziel = os.environ.get("SPION_AUS", "/tmp/spion_gewinn.jsonl")

    def spion(*a, **k):
        r = original(*a, **k)
        aufrufer = sys._getframe(1).f_code
        with open(ziel, "a", encoding="utf-8") as f:
            f.write(json.dumps({"aufrufer": f"{aufrufer.co_filename.split('/biotop/')[-1]}:{aufrufer.co_name}",
                                "ergebnis": r.get("ergebnis"), "gewinn": r.get("gewinn"),
                                "nachgemessen": r.get("nachgemessen")}, ensure_ascii=False) + "\n")
        return r
    messgeraet.gewinn_bestaetigen = spion
