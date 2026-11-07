"""Organ 3.2: Landkarte — Zoomstufen, Straßen, abgeleitete Verträge.

Struktur und Aufrufe aus Syntaxbäumen (Python `ast`; tree-sitter steht auf der
Liste für danach, weil Phase 1 nur Python-Werke hat — Entscheidung Hermes).
Zusammenfassungen je Stufe durch ein Modell, in der Datenbank mit Prüfsumme
der Quelldatei; veraltete Zusammenfassungen werden neu erzeugt.

Stufen: 0 Werk (ein Absatz) · 1 Bereich (ein Absatz) · 2 Datei (ein Satz)
· 3 Funktion (Signatur + Zweck, aus dem Code ohne Modell).
Straßen: gerichtete Kanten von Modul zu Modul (Import) und von Funktion zu
Funktion (Aufruf, soweit statisch auflösbar).
"""

from __future__ import annotations

import ast
import hashlib
import sqlite3
from pathlib import Path

from ..anbieter import aufrufen
from ..kern import protokoll
from ..kern.datenbank import j, lj, transaktion

MODELL_ZUSAMMENFASSUNG = ("openrouter", "google/gemini-3.1-flash-lite")


def pruefsumme(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


# ---------------------------------------------------------------- Struktur
def bereiche_finden(werk: Path, paket: str) -> list[str]:
    wurzel = werk / paket
    return sorted(p.name for p in wurzel.iterdir() if p.is_dir() and (p / "__init__.py").exists())


def dateien_je_bereich(werk: Path, paket: str, bereich: str) -> list[Path]:
    return sorted((werk / paket / bereich).rglob("*.py"))


def funktionen(datei: Path) -> list[dict]:
    baum = ast.parse(datei.read_text())
    out = []
    for kn in ast.walk(baum):
        if isinstance(kn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = [a.arg for a in kn.args.args]
            doc = (ast.get_docstring(kn) or "").strip().splitlines()
            out.append({
                "name": kn.name, "zeile": kn.lineno, "ende": kn.end_lineno,
                "signatur": f"{kn.name}({', '.join(args)})",
                "zweck": doc[0] if doc else "",
            })
    return out


def _modulname(werk: Path, datei: Path) -> str:
    return ".".join(datei.relative_to(werk).with_suffix("").parts).removesuffix(".__init__")


def strassen(werk: Path, paket: str, bereiche: list[str]) -> list[tuple[str, str, str]]:
    """Kanten (von, nach, art). art = 'import' (Modul→Modul) oder 'aufruf' (Funktion→Funktion)."""
    kanten: set[tuple[str, str, str]] = set()
    module: dict[str, Path] = {}
    for b in bereiche:
        for d in dateien_je_bereich(werk, paket, b):
            module[_modulname(werk, d)] = d
    # Funktionsnamen je Modul für Aufruf-Auflösung
    fn_index: dict[str, str] = {}
    for m, d in module.items():
        for f in funktionen(d):
            fn_index.setdefault(f["name"], m)
    for m, d in module.items():
        baum = ast.parse(d.read_text())
        pkg_parts = m.split(".")
        for kn in ast.walk(baum):
            if isinstance(kn, ast.ImportFrom):
                if kn.level:  # relativ
                    basis = pkg_parts[: len(pkg_parts) - kn.level + (0 if d.name != "__init__.py" else 1)]
                    ziel = ".".join(basis + ([kn.module] if kn.module else []))
                else:
                    ziel = kn.module or ""
                if ziel.startswith(paket):
                    # auf das nächste bekannte Modul abbilden
                    kandidaten = [x for x in module if ziel == x or ziel.startswith(x + ".")]
                    if not kandidaten:
                        kandidaten = [x for x in module if x.startswith(ziel + ".") and x.endswith(".__init__")]
                    ziel_mod = max(kandidaten, key=len) if kandidaten else ziel
                    if ziel_mod != m:
                        kanten.add((m, ziel_mod, "import"))
            elif isinstance(kn, ast.Import):
                for a in kn.names:
                    if a.name.startswith(paket) and a.name != m:
                        kanten.add((m, a.name, "import"))
    return sorted(kanten)


def bereich_von(modul: str, paket: str) -> str | None:
    teile = modul.split(".")
    return teile[1] if len(teile) > 1 and teile[0] == paket else None


def bereichs_strassen(kanten: list[tuple[str, str, str]], paket: str) -> list[tuple[str, str]]:
    s = set()
    for v, n, _ in kanten:
        a, b = bereich_von(v, paket), bereich_von(n, paket)
        if a and b and a != b:
            s.add((a, b))
    return sorted(s)


def wirkungskreis(bereich: str, bstrassen: list[tuple[str, str]]) -> list[str]:
    """Alle Bereiche, die (transitiv) von `bereich` abhängen — plus er selbst."""
    rueck: dict[str, set[str]] = {}
    for a, b in bstrassen:
        rueck.setdefault(b, set()).add(a)
    kreis = {bereich}
    stapel = [bereich]
    while stapel:
        k = stapel.pop()
        for a in rueck.get(k, ()):
            if a not in kreis:
                kreis.add(a)
                stapel.append(a)
    return sorted(kreis)


# ---------------------------------------------------------------- Verträge
def vertraege_ableiten(werk: Path, paket: str, bereich: str) -> list[dict]:
    """Liest Zusicherungen aus Docstrings („Vertrag“-Abschnitte) und leitet aus
    den öffentlichen Signaturen abgeleitete Verträge ab."""
    out = []
    for d in dateien_je_bereich(werk, paket, bereich):
        baum = ast.parse(d.read_text())
        doc = ast.get_docstring(baum) or ""
        if "Vertrag" in doc:
            block = doc[doc.index("Vertrag"):]
            for zeile in block.splitlines()[1:]:
                z = zeile.strip()
                if z.startswith("- "):
                    out.append({"text": z[2:], "herkunft": "docstring", "quelle": f"{d.relative_to(werk)}"})
                elif z and out and out[-1]["herkunft"] == "docstring" and out[-1]["quelle"] == str(d.relative_to(werk)):
                    out[-1]["text"] += " " + z  # Fortsetzungszeile
                elif not z:
                    break
        for f in funktionen(d):
            if not f["name"].startswith("_") and d.name != "__init__.py":
                out.append({"text": f"{f['signatur']}: {f['zweck'] or 'ohne Beschreibung'}",
                            "herkunft": "abgeleitet", "quelle": f"{d.relative_to(werk)}:{f['zeile']}"})
    return out


# ---------------------------------------------------------------- Aufbau
def bauen(con: sqlite3.Connection, werk_id: int, lauf_id: int, werk: Path, paket: str) -> dict:
    """Baut/aktualisiert die Landkarte. Modellaufrufe nur für Stufe 0–2 und nur
    bei geänderter Prüfsumme. Rückgabe: Kennzahlen."""
    bereiche = bereiche_finden(werk, paket)
    kanten = strassen(werk, paket, bereiche)
    zahlen = {"bereiche": len(bereiche), "strassen": len(kanten), "dateien": 0, "funktionen": 0,
              "modellaufrufe": 0, "vertraege": 0}
    with transaktion(con):
        con.execute("DELETE FROM strassen WHERE werk_id=?", (werk_id,))
        for v, n, a in kanten:
            con.execute("INSERT OR IGNORE INTO strassen(werk_id, von, nach, art) VALUES (?,?,?,?)", (werk_id, v, n, a))
        con.execute("DELETE FROM vertraege WHERE werk_id=?", (werk_id,))
        for b in bereiche:
            for vt in vertraege_ableiten(werk, paket, b):
                con.execute("INSERT INTO vertraege(werk_id, bereich, text, herkunft, quelle) VALUES (?,?,?,?,?)",
                            (werk_id, b, vt["text"], vt["herkunft"], vt["quelle"]))
                zahlen["vertraege"] += 1

    def eintrag(stufe: int, schluessel: str, inhalt: dict, ps: str, herkunft: str):
        with transaktion(con):
            con.execute(
                "INSERT INTO landkarte(werk_id, stufe, schluessel, inhalt, pruefsumme, erstellt_am, herkunft) "
                "VALUES (?,?,?,?,?,?,?) ON CONFLICT(werk_id, stufe, schluessel) DO UPDATE SET "
                "inhalt=excluded.inhalt, pruefsumme=excluded.pruefsumme, erstellt_am=excluded.erstellt_am, herkunft=excluded.herkunft",
                (werk_id, stufe, schluessel, j(inhalt), ps, protokoll.jetzt(), herkunft))

    def vorhanden(stufe: int, schluessel: str, ps: str) -> dict | None:
        z = con.execute("SELECT inhalt, pruefsumme FROM landkarte WHERE werk_id=? AND stufe=? AND schluessel=?",
                        (werk_id, stufe, schluessel)).fetchone()
        return lj(z["inhalt"]) if z and z["pruefsumme"] == ps else None

    def zusammenfassen(zweck: str, auftrag: str, text: str, max_tokens: int = 300) -> str:
        zahlen["modellaufrufe"] += 1
        a = aufrufen(con, lauf_id, *MODELL_ZUSAMMENFASSUNG,
                     system="Du bist Kartograph eines Software-Werks. Antworte auf Deutsch, knapp, sachlich, ohne Einleitung.",
                     nutzer=f"{auftrag}\n\n{text[:12000]}", zweck=zweck, max_tokens=max_tokens, temperatur=0.1)
        return a.text.strip()

    # Stufe 3 + 2 je Datei
    bereich_texte: dict[str, list[str]] = {}
    for b in bereiche:
        for d in dateien_je_bereich(werk, paket, b):
            quelle = d.read_text()
            ps = pruefsumme(quelle)
            rel = str(d.relative_to(werk))
            fns = funktionen(d)
            zahlen["dateien"] += 1
            zahlen["funktionen"] += len(fns)
            eintrag(3, rel, {"funktionen": fns}, ps, "ast")
            s2 = vorhanden(2, rel, ps)
            if s2 is None:
                satz = zusammenfassen("landkarte.stufe2", f"Beschreibe die Datei {rel} in genau einem Satz.", quelle, 120)
                s2 = {"satz": satz}
                eintrag(2, rel, s2, ps, MODELL_ZUSAMMENFASSUNG[1])
            bereich_texte.setdefault(b, []).append(f"{rel}: {s2['satz']}")
    # Stufe 1 je Bereich
    werk_texte = []
    for b in bereiche:
        text = "\n".join(bereich_texte.get(b, []))
        ps = pruefsumme(text)
        s1 = vorhanden(1, b, ps)
        if s1 is None:
            absatz = zusammenfassen("landkarte.stufe1", f"Beschreibe den Bereich „{b}“ in einem Absatz (3–5 Sätze): Aufgabe, Hauptbegriffe, Abhängigkeiten.", text, 250)
            s1 = {"absatz": absatz}
            eintrag(1, b, s1, ps, MODELL_ZUSAMMENFASSUNG[1])
        werk_texte.append(f"Bereich {b}: {s1['absatz']}")
    # Stufe 0
    text = "\n".join(werk_texte) + "\nStraßen zwischen Bereichen: " + ", ".join(f"{a}→{b}" for a, b in bereichs_strassen(kanten, paket))
    ps = pruefsumme(text)
    if vorhanden(0, paket, ps) is None:
        absatz = zusammenfassen("landkarte.stufe0", "Beschreibe das gesamte Werk in einem Absatz (3–5 Sätze): Was es ist, wofür, wie die Bereiche zusammenhängen.", text, 250)
        eintrag(0, paket, {"absatz": absatz}, ps, MODELL_ZUSAMMENFASSUNG[1])
    protokoll.schreiben(con, "landkarte.gebaut", werk_id=werk_id, **zahlen)
    return zahlen


def sicht(con: sqlite3.Connection, werk_id: int, paket: str, bereich: str) -> str:
    """Die einzige Sicht des Schwarms: Stufe 0 + Stufe 1 (alle) + Stufe 3 des
    Bereichs + Verträge des Bereichs und seiner Nachbarn."""
    teile = []
    z = con.execute("SELECT inhalt FROM landkarte WHERE werk_id=? AND stufe=0", (werk_id,)).fetchone()
    if z:
        teile.append("WERK: " + lj(z["inhalt"])["absatz"])
    for r in con.execute("SELECT schluessel, inhalt FROM landkarte WHERE werk_id=? AND stufe=1 ORDER BY schluessel", (werk_id,)):
        teile.append(f"BEREICH {r['schluessel']}: {lj(r['inhalt'])['absatz']}")
    teile.append(f"\nFUNKTIONEN IM BEREICH {bereich}:")
    for r in con.execute("SELECT schluessel, inhalt FROM landkarte WHERE werk_id=? AND stufe=3 AND schluessel LIKE ? ORDER BY schluessel",
                         (werk_id, f"{paket}/{bereich}/%")):
        for f in lj(r["inhalt"])["funktionen"]:
            teile.append(f"  {r['schluessel']}:{f['zeile']} {f['signatur']} — {f['zweck']}")
    nachbarn = {bereich}
    for r in con.execute("SELECT von, nach FROM strassen WHERE werk_id=?", (werk_id,)):
        a, b = bereich_von(r["von"], paket), bereich_von(r["nach"], paket)
        if a == bereich and b:
            nachbarn.add(b)
        if b == bereich and a:
            nachbarn.add(a)
    teile.append("\nVERTRÄGE (docstring = im Werk zugesichert, abgeleitet = aus dem Code gelesen):")
    for r in con.execute("SELECT bereich, text, herkunft, quelle FROM vertraege WHERE werk_id=? AND herkunft='docstring' ORDER BY bereich", (werk_id,)):
        if r["bereich"] in nachbarn:
            teile.append(f"  [{r['bereich']}] {r['text']}  ({r['quelle']})")
    return "\n".join(teile)
