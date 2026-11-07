"""Nur Original-Replay: versiegeltes eigenes Ausgangsmodul, keine Produktion."""
import hashlib
import importlib.util
from pathlib import Path
import sys

import biotop.kern

pfad = Path(__file__).parent / "roh" / "messgeraet.original.py"
spec = importlib.util.spec_from_file_location("biotop.kern.messgeraet", pfad)
modul = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modul)
sys.modules["biotop.kern.messgeraet"] = modul
biotop.kern.messgeraet = modul


def pytest_report_header():
    return "ORIGINAL-REPLAY " + str(pfad) + " sha256=" + hashlib.sha256(pfad.read_bytes()).hexdigest()
