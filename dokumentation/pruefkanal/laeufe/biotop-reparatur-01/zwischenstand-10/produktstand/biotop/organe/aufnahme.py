"""Organ 3.1: Aufnahme — Werk entgegennehmen, erkennen, erster Testlauf,
ethische Prüfung. Kein Fremdcode außerhalb der Kammer.

Regel: ohne Tests oder ohne bauenden Zustand → „Messgerät fehlt“, kein Lauf.
"""

from __future__ import annotations

import re
import shutil
import sqlite3
import subprocess
import zipfile
from pathlib import Path

from ..anbieter import aufrufen
from ..kern import protokoll
from ..kern.datenbank import j, transaktion
from . import kammer

WERKE = Path("/root/biotop/daten/werke")
ENDUNGEN = {".py": "Python", ".js": "JavaScript", ".ts": "TypeScript", ".go": "Go", ".rs": "Rust",
            ".java": "Java", ".rb": "Ruby", ".sh": "Shell", ".md": "Markdown", ".toml": "TOML", ".json": "JSON"}
AUSSCHLUSS = {".git", "node_modules", "__pycache__", ".pytest_cache", "dist", "coverage", ".venv", "venv"}
ETHIK_WOERTER = ["weapon", "missile", "munition", "rüstung", "waffe", "kriegsger", "surveillance", "überwachung",
                 "tracking of persons", "facial recognition", "gesichtserkennung", "phishing", "betrug", "scam", "fraud kit",
                 "keylogger", "stalkerware", "exploit kit", "credential harvest"]
MODELL_ETHIK = ("openrouter", "openai/gpt-5.6-luna")


class MessgeraetFehlt(RuntimeError):
    pass


def _holen(quelle: str, ziel: Path) -> str:
    if ziel.exists():
        shutil.rmtree(ziel)
    q = Path(quelle)
    if quelle.startswith(("http://", "https://", "git@")) or quelle.endswith(".git"):
        subprocess.run(["git", "clone", "-q", "--depth", "1", quelle, str(ziel)], check=True, timeout=300)
        shutil.rmtree(ziel / ".git", ignore_errors=True)
        return "git"
    if q.is_file() and q.suffix == ".zip":
        with zipfile.ZipFile(q) as z:
            for m in z.namelist():
                if m.startswith("/") or ".." in m.split("/"):
                    raise ValueError(f"unsicherer Pfad im Archiv: {m}")
            z.extractall(ziel)
        # ein einzelnes Wurzelverzeichnis flach machen
        inhalt = [p for p in ziel.iterdir()]
        if len(inhalt) == 1 and inhalt[0].is_dir():
            for p in inhalt[0].iterdir():
                shutil.move(str(p), ziel / p.name)
            inhalt[0].rmdir()
        return "zip"
    if q.is_dir():
        shutil.copytree(q, ziel, ignore=shutil.ignore_patterns(*AUSSCHLUSS, ".env*"))
        return "ordner"
    raise ValueError(f"Quelle nicht erkannt: {quelle}")


def _zaehlen(werk: Path) -> dict:
    dateien = 0
    zeilen: dict[str, int] = {}
    testdateien = []
    for p in werk.rglob("*"):
        if any(t in AUSSCHLUSS for t in p.parts) or not p.is_file():
            continue
        dateien += 1
        sprache = ENDUNGEN.get(p.suffix)
        if sprache:
            try:
                n = sum(1 for _ in p.open(errors="replace"))
            except Exception:  # noqa: BLE001
                n = 0
            zeilen[sprache] = zeilen.get(sprache, 0) + n
        rel = str(p.relative_to(werk))
        if re.match(r"(^|.*/)(tests?/.*|test_[^/]+\.py|[^/]+_test\.py|[^/]+\.test\.[jt]s)$", rel):
            testdateien.append(rel)
    return {"dateien": dateien, "zeilen_je_sprache": zeilen, "testdateien": sorted(testdateien)}


def _paket(werk: Path) -> str | None:
    for p in sorted(werk.iterdir()):
        if p.is_dir() and (p / "__init__.py").exists() and p.name not in ("tests", "test"):
            return p.name
    return None


def _ethik(con: sqlite3.Connection, lauf_id: int, werk: Path, zahlen: dict) -> dict:
    """Stichwortsuche über alle Textdateien + eine Modellbewertung der Werkbeschreibung.
    Das Werk selbst beantwortet die Frage nicht; bewertet wird, was das Werk tut."""
    treffer = []
    for p in werk.rglob("*"):
        if p.is_file() and p.suffix in ENDUNGEN and not any(t in AUSSCHLUSS for t in p.parts):
            text = p.read_text(errors="replace").lower()
            for w in ETHIK_WOERTER:
                if w in text:
                    treffer.append(f"{p.relative_to(werk)}: „{w}“")
    beschreibung = ""
    for name in ("README.md", "README", "readme.md", "pyproject.toml", "package.json"):
        if (werk / name).exists():
            beschreibung += f"\n--- {name} ---\n" + (werk / name).read_text(errors="replace")[:3000]
    dateiliste = "\n".join(str(p.relative_to(werk)) for p in sorted(werk.rglob("*.py"))[:80])
    a = aufrufen(
        con, lauf_id, *MODELL_ETHIK,
        system="Du prüfst, ob ein Software-Werk schädlichen Zwecken dient: Rüstung, Kriegsgerät, Überwachung von Menschen, Betrug. "
               "Antworte in genau zwei Zeilen: Zeile 1 „UNBEDENKLICH“ oder „BEDENKLICH“, Zeile 2 eine Begründung in einem Satz.",
        nutzer=f"Beschreibung:{beschreibung or ' (keine)'}\n\nDateien:\n{dateiliste}\n\nStichworttreffer: {treffer or 'keine'}",
        zweck="aufnahme.ethik", max_tokens=120, temperatur=0.0,
    )
    zeilen = a.text.strip().splitlines()
    urteil = "BEDENKLICH" if zeilen and "BEDENKLICH" in zeilen[0].upper() and "UNBEDENKLICH" not in zeilen[0].upper() else "UNBEDENKLICH"
    return {"urteil": urteil, "begruendung": zeilen[1] if len(zeilen) > 1 else "", "stichworttreffer": treffer[:20], "modell": MODELL_ETHIK[1]}


def aufnehmen(con: sqlite3.Connection, name: str, quelle: str, lauf_id: int, referenzlast: str | None = None) -> dict:
    """Nimmt ein Werk auf. Rückgabe: Aufnahmebericht. Wirft MessgeraetFehlt bei
    fehlenden Tests oder nicht bauendem Zustand — nach dem Schreiben des Berichts."""
    WERKE.mkdir(parents=True, exist_ok=True)
    ziel = WERKE / name
    art = _holen(quelle, ziel)
    zahlen = _zaehlen(ziel)
    paket = _paket(ziel)
    bericht = {"name": name, "quelle": quelle, "art": art, "pfad": str(ziel), "paket": paket, **zahlen}
    bereiche = []
    if paket:
        bereiche = sorted(p.name for p in (ziel / paket).iterdir() if p.is_dir() and (p / "__init__.py").exists())
    bericht["bereiche_schaetzung"] = bereiche
    sprache = max(zahlen["zeilen_je_sprache"], key=zahlen["zeilen_je_sprache"].get) if zahlen["zeilen_je_sprache"] else "unbekannt"
    bericht["sprache"] = sprache

    # Erster Testlauf in der Kammer (nur wenn Tests vorhanden)
    testlauf = {"bestanden": 0, "gesamt": 0, "rc": None, "ausgabe": ""}
    if zahlen["testdateien"] and sprache == "Python":
        e = kammer.ausfuehren(ziel, ["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=line"], zeitlimit_s=120)
        m = re.search(r"(\d+) passed", e.stdout)
        f = re.search(r"(\d+) failed", e.stdout)
        err = re.search(r"(\d+) error", e.stdout)
        b = int(m.group(1)) if m else 0
        g = b + (int(f.group(1)) if f else 0) + (int(err.group(1)) if err else 0)
        testlauf = {"bestanden": b, "gesamt": g, "rc": e.rc, "ausgabe": e.stdout[-1500:], "zeitlimit": e.zeitlimit}
    bericht["erster_testlauf"] = testlauf
    baut = None
    if paket and sprache == "Python":
        e = kammer.ausfuehren(ziel, ["python", "-c", f"import {paket}"], zeitlimit_s=60)
        baut = e.rc == 0
        bericht["bau_ausgabe"] = (e.stdout + e.stderr)[-800:]
    bericht["baut"] = baut

    bericht["ethik"] = _ethik(con, lauf_id, ziel, zahlen)

    status = "aufgenommen"
    grund = ""
    if bericht["ethik"]["urteil"] == "BEDENKLICH":
        status, grund = "abgelehnt", "ethische Prüfung: " + bericht["ethik"]["begruendung"]
    elif not zahlen["testdateien"] or testlauf["gesamt"] == 0:
        status, grund = "messgeraet_fehlt", "Messgerät fehlt: keine Tests gefunden (0 Testdateien mit ausführbaren Tests). Vorschlag: mit Generation 0 (Tests erzeugen) beginnen."
    elif baut is False:
        status, grund = "messgeraet_fehlt", "Messgerät fehlt: Werk baut nicht."
    bericht["status"], bericht["grund"] = status, grund

    with transaktion(con):
        con.execute(
            "INSERT INTO werke(name, pfad, quelle, aufgenommen_am, bericht, sprache, status) VALUES (?,?,?,?,?,?,?) "
            "ON CONFLICT(name) DO UPDATE SET pfad=excluded.pfad, quelle=excluded.quelle, aufgenommen_am=excluded.aufgenommen_am, "
            "bericht=excluded.bericht, sprache=excluded.sprache, status=excluded.status",
            (name, str(ziel), quelle, protokoll.jetzt(), j(bericht), sprache, status))
    werk_id = con.execute("SELECT id FROM werke WHERE name=?", (name,)).fetchone()["id"]
    bericht["werk_id"] = werk_id
    protokoll.schreiben(con, "aufnahme", werk_id=werk_id, name=name, status=status, grund=grund,
                        dateien=zahlen["dateien"], zeilen=zahlen["zeilen_je_sprache"], testdateien=len(zahlen["testdateien"]),
                        testlauf=f"{testlauf['bestanden']} von {testlauf['gesamt']}", ethik=bericht["ethik"]["urteil"])
    if status != "aufgenommen":
        raise MessgeraetFehlt(grund)
    return bericht
