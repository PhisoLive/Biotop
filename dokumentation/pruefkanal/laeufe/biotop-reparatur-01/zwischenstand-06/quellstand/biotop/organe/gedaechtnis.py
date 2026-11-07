"""Organ 3.12 — Die drei Gedächtnisse (Phase 3). Alle dauerhaft in der Datenbank, alle vor jeder Generation gelesen.

Projektgedächtnis (je Werk): jeder gescheiterte Weg (Kandidat abgelehnt) mit Bereich, Änderungsziel (berührte Funktionen
    je Datei), Ansatz (Token der hinzugefügten Zeilen), Grund. Werkidentität = Paketname (lagerhaus, logmuehle), damit ein
    zweiter Lauf am selben Werk (neue werk_id) dieselben Wege sieht. Der Schwarm bekommt die Liste vor jeder Generation;
    zusätzlich prüft das Biotop jeden neuen Kandidaten mechanisch: gleicher Bereich, überlappende Funktionen und
    Ansatz-Ähnlichkeit (Jaccard der Token der hinzugefügten Zeilen) ≥ SCHWELLE gegen einen gescheiterten Weg → Wiederholung,
    wird ohne Kammerlauf verworfen und protokolliert (immun.wiederholung).
Artgedächtnis (über alle Werke): je angenommenem Kandidaten (und je Generation) ein Eintrag: Werkklasse (Sprache/Größe/Bauart),
    Art der Änderung (Nische, Kategorie), Bereichsrolle, Ertrag (Kernmaß-Zuwachs, Laufzeit-%). Mentor und Schwarm lesen es.
Geschmacksgedächtnis (Philipp): jede Freigabe/Ablehnung mit Begründung und den Merkmalen der Vorlage; ab 20 Entscheidungen
    ein Vorhersagemodell (Naive Bayes über diskretisierte Merkmale, stdlib), das der Vorlage beigelegt wird.
"""

from __future__ import annotations

import ast
import json
import math
import re
import sqlite3
from collections import Counter, defaultdict

from ..anbieter import AnbieterFehler, aufrufen
from ..kern import protokoll
from ..kern.datenbank import j, lj, transaktion

SCHWELLE_WIEDERHOLUNG = 0.5  # Jaccard der Token hinzugefügter Zeilen

SCHEMA = """
CREATE TABLE IF NOT EXISTS projektgedaechtnis (
  id INTEGER PRIMARY KEY, werk TEXT, werk_id INTEGER, lauf_id INTEGER, generation INTEGER, kandidat_id INTEGER,
  bereich TEXT, nische TEXT, dateien TEXT, funktionen TEXT, ansatz TEXT, grund TEXT, grundklasse TEXT, begruendung TEXT, erstellt_am TEXT,
  UNIQUE(kandidat_id));
CREATE TABLE IF NOT EXISTS artgedaechtnis (
  id INTEGER PRIMARY KEY, werk TEXT, werkklasse TEXT, lauf_id INTEGER, generation INTEGER, kandidat_id INTEGER,
  bereich TEXT, bereichsrolle TEXT, nische TEXT, kategorie TEXT, ergebnis TEXT, zuwachs INTEGER, laufzeit_prozent REAL,
  beschreibung TEXT, muster TEXT, muster_von TEXT, erstellt_am TEXT, UNIQUE(kandidat_id, ergebnis));
CREATE TABLE IF NOT EXISTS geschmack (
  id INTEGER PRIMARY KEY, werk TEXT, lauf_id INTEGER, generation INTEGER, kandidat_id INTEGER, entscheidung TEXT,
  grund TEXT, von TEXT, merkmale TEXT, quelle TEXT, erstellt_am TEXT, UNIQUE(lauf_id, generation, kandidat_id, quelle));
"""


def tabellen(con: sqlite3.Connection) -> None:
    con.executescript(SCHEMA)
    # Neue Spalten an bestehenden Tabellen: CREATE TABLE IF NOT EXISTS ergänzt keine (F5 3.12, Muster).
    vorhanden = {d[1] for d in con.execute("PRAGMA table_info(artgedaechtnis)")}
    for spalte in ("muster", "muster_von"):
        if spalte not in vorhanden:
            con.execute(f"ALTER TABLE artgedaechtnis ADD COLUMN {spalte} TEXT")


# ---------------------------------------------------------------- Hilfen: Änderungsziel und Ansatz aus einem Diff
def _funktionen(code: str) -> dict[str, str]:
    try:
        baum = ast.parse(code)
    except SyntaxError:
        return {}
    out = {}
    for kn in ast.walk(baum):
        if isinstance(kn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out[kn.name] = ast.unparse(kn)
    return out


def aenderungsziel(werk_pfad, diff: str, dateien_neu: dict | None) -> tuple[list[str], list[str], list[str]]:
    """(dateien, funktionen, ansatz-token). funktionen = je Datei 'datei::name' mit geändertem/neuem/entferntem Körper;
    ansatz = Token der hinzugefügten Zeilen (ohne Kommentare, ≥ 3 Zeichen)."""
    dateien = sorted(set(re.findall(r"^\+\+\+ b/(\S+)", diff, re.M)))
    funktionen: list[str] = []
    for d in dateien:
        alt = (werk_pfad / d)
        alt_f = _funktionen(alt.read_text()) if alt.exists() else {}
        neu_f = _funktionen((dateien_neu or {}).get(d) or "") if dateien_neu else {}
        if not dateien_neu:
            # ohne angewandten Diff: Funktionsnamen aus Hunk-Kopf/Kontext
            for m in re.finditer(r"^@@.*@@\s*(?:async\s+)?def\s+(\w+)", diff, re.M):
                funktionen.append(f"{d}::{m.group(1)}")
            continue
        for n in set(alt_f) | set(neu_f):
            if alt_f.get(n) != neu_f.get(n):
                funktionen.append(f"{d}::{n}")
    plus = [l[1:] for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++")]
    token = set()
    for l in plus:
        l = l.split("#", 1)[0]
        token |= {t.lower() for t in re.findall(r"[A-Za-z_][A-Za-z_0-9]{2,}", l)}
    return dateien, sorted(set(funktionen)), sorted(token)


def _jaccard(a: list[str], b: list[str]) -> float:
    sa, sb = set(a), set(b)
    return len(sa & sb) / len(sa | sb) if (sa | sb) else 0.0


def grundklasse(grund: str) -> str:
    g = grund or ""
    if g.startswith("Diff nicht anwendbar") or g.startswith("Diff ändert nichts") or g.startswith("Diff berührt"):
        return "technisch"
    if "unverändert" in g:
        return "kein_massgewinn"
    if "Pareto" in g or "Regression" in g:
        return "regression"
    if "Vertrag" in g:
        return "vertrag"
    if "Grenz" in g:
        return "grenzmass"
    if "Verfassung" in g:
        return "verfassung"
    if "schnell" in g or "Laufzeit" in g:
        return "kein_laufzeitgewinn"
    if "eigene Tests" in g:
        return "eigene_tests_rot"
    return "sonst"


# ---------------------------------------------------------------- Probenkandidaten: von allen Gedächtnissen fern
PROBEN_NISCHEN = ("probe", "probe_jury_hermes", "probe_jury_mechanik")
PROBEN_MARKE = "probe"


def ist_probe(k) -> bool:
    """Probenkandidaten (Eichproben des Vorspanns, eingeschleuste Proben) gehören in KEIN Gedächtnis (Fassung 6).

    Grund: Der Vorspann läuft ab Fassung 5 vor JEDEM Lauf. Ein eingeschleuster Regressionskandidat würde im
    Projektgedächtnis später echte Kandidaten sperren, ein Probenmuster im Artgedächtnis als Erfahrung an fremde
    Werke weitergereicht, eine Probenentscheidung im Geschmacksgedächtnis als Philipps Geschmack gelernt.
    In Phase 2 genügte die Kennzeichnung `nische='probe'`, weil es die Gedächtnisse noch nicht gab.

    **Grundlage ist das gesetzte Merkmal `kandidaten.ist_probe`**, das der Erzeuger der Probe setzt — nicht der
    Name. Namen sind eine Verabredung, die ein späterer Einbau anders schreibt: Die Jury-Proben liefen unter
    eigenen Bereichsmarken und wären bei reiner Nischenprüfung durchgerutscht — dieselbe Fehlerklasse wie die
    Doppelungserkennung, die auf den Ort statt auf die Behauptung sah.
    Nische und Bereichsname bleiben als ZWEITER Weg für Altbestand aus Phase 2/3, in dem das Feld noch fehlt.

    Die Proben bleiben in der Datenbank und im Bericht sichtbar — nur die Gedächtnisse lesen sie nicht.
    """
    if k is None:
        return False
    schluessel = k.keys()
    if "ist_probe" in schluessel and k["ist_probe"]:
        return True                                     # gesetztes Merkmal — die Grundlage
    nische = (k["nische"] if "nische" in schluessel else None) or ""
    bereich = (k["bereich"] if "bereich" in schluessel else None) or ""
    return nische in PROBEN_NISCHEN or nische.startswith(PROBEN_MARKE) or bereich.startswith(PROBEN_MARKE)


# ---------------------------------------------------------------- Projektgedächtnis
def werkname(con, werk_id: int) -> str:
    z = con.execute("SELECT bericht FROM werke WHERE id=?", (werk_id,)).fetchone()
    b = lj(z["bericht"]) if z and z["bericht"] else {}
    return (b or {}).get("paket") or "werk"


def projekt_merken(con, werk_id: int, lauf_id: int, kandidat_id: int, werk_pfad, dateien_neu: dict | None = None) -> None:
    """Nach einer Ablehnung: den gescheiterten Weg aufnehmen. Probenkandidaten NICHT (Fassung 6)."""
    tabellen(con)
    k = con.execute("SELECT * FROM kandidaten WHERE id=?", (kandidat_id,)).fetchone()
    if not k or k["status"] not in ("abgelehnt",) or not k["diff"]:
        return
    if ist_probe(k):
        protokoll.schreiben(con, "gedaechtnis.probe_uebersprungen", lauf_id=lauf_id, kandidat=kandidat_id,
                            gedaechtnis="projekt", nische=k["nische"], bereich=k["bereich"],
                            grund="Probenkandidat — kommt in kein Gedächtnis (Fassung 6); bleibt in der Datenbank sichtbar")
        return
    dateien, funktionen, ansatz = aenderungsziel(werk_pfad, k["diff"], dateien_neu)
    with transaktion(con):
        con.execute("INSERT OR IGNORE INTO projektgedaechtnis(werk, werk_id, lauf_id, generation, kandidat_id, bereich, nische, dateien, funktionen, ansatz, grund, grundklasse, begruendung, erstellt_am) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (werkname(con, werk_id), werk_id, lauf_id, k["generation"], kandidat_id, k["bereich"], k["nische"], j(dateien), j(funktionen), j(ansatz),
                     (k["grund"] or "")[:400], grundklasse(k["grund"]), (k["begruendung"] or "")[:400], protokoll.jetzt()))


def gescheiterte_wege(con, werk_id: int, bereich: str, limit: int = 15) -> list[dict]:
    """Alle gescheiterten Wege dieses Werks (über alle Läufe) im Bereich, jüngste zuerst; technische Fehler ausgenommen.
    Läufe, die nach Verfassungssatz 2 VERWORFEN wurden, zählen nicht: ihre Ablehnungen wurden mit einem Messgerät
    gemessen, das als falsch erkannt wurde (Lauf 18 Gen 2/3: 12 Kandidaten wurden als Wiederholung von Lauf-16-Wegen
    verworfen, obwohl Lauf 16 genau wegen des fehlerhaften Anklägers verworfen worden war)."""
    tabellen(con)
    return [dict(z) for z in con.execute(
        "SELECT p.* FROM projektgedaechtnis p JOIN laeufe l ON l.id = p.lauf_id "
        "WHERE p.werk=? AND p.bereich=? AND p.grundklasse!='technisch' AND l.status != 'verworfen' ORDER BY p.id DESC LIMIT ?",
        (werkname(con, werk_id), bereich, limit))]


def gescheiterte_wege_text(con, werk_id: int, bereich: str) -> str:
    wege = gescheiterte_wege(con, werk_id, bereich)
    if not wege:
        return "keine"
    return "\n".join(f"- [Lauf {w['lauf_id']} Gen {w['generation']}, {w['nische']}] Ziel {', '.join(lj(w['funktionen']) or lj(w['dateien']))}: {w['begruendung'][:160]} → {w['grund'][:160]}" for w in wege)


def wiederholung(con, werk_id: int, bereich: str, werk_pfad, diff: str, dateien_neu: dict | None, lauf_id: int) -> dict | None:
    """Mechanische Prüfung: Ist der neue Kandidat eine Wiederholung eines gescheiterten Wegs (anderer Lauf oder derselbe)?
    Gleicher Bereich, mindestens eine gemeinsame berührte Funktion (oder gleiche Datei ohne Funktionsinfo) UND Ansatz-Jaccard ≥ SCHWELLE."""
    tabellen(con)
    dateien, funktionen, ansatz = aenderungsziel(werk_pfad, diff, dateien_neu)
    beste = None
    for w in con.execute("SELECT p.* FROM projektgedaechtnis p JOIN laeufe l ON l.id = p.lauf_id "
                         "WHERE p.werk=? AND p.bereich=? AND p.grundklasse!='technisch' AND l.status != 'verworfen'",
                         (werkname(con, werk_id), bereich)):
        wf, wd, wa = set(lj(w["funktionen"]) or []), set(lj(w["dateien"]) or []), lj(w["ansatz"]) or []
        ziel_gleich = bool(wf & set(funktionen)) or (not wf and not funktionen and bool(wd & set(dateien)))
        if not ziel_gleich:
            continue
        aehnlich = _jaccard(ansatz, wa)
        if aehnlich >= SCHWELLE_WIEDERHOLUNG and (beste is None or aehnlich > beste["aehnlichkeit"]):
            beste = {"weg_id": w["id"], "lauf_id": w["lauf_id"], "generation": w["generation"], "kandidat_id": w["kandidat_id"],
                     "aehnlichkeit": round(aehnlich, 3), "gemeinsame_funktionen": sorted(wf & set(funktionen)), "grund_damals": w["grund"][:200]}
    return beste


def projekt_import(con, lauf_id: int, werk_pfad) -> int:
    """Rückwirkend: alle abgelehnten Kandidaten eines Laufs ins Projektgedächtnis (für Läufe vor Phase 3)."""
    tabellen(con)
    lauf = con.execute("SELECT werk_id FROM laeufe WHERE id=?", (lauf_id,)).fetchone()
    n = 0
    for k in con.execute("SELECT id FROM kandidaten WHERE lauf_id=? AND status='abgelehnt' AND diff!=''", (lauf_id,)):
        projekt_merken(con, lauf["werk_id"], lauf_id, k["id"], werk_pfad)
        n += 1
    return n


# ---------------------------------------------------------------- Artgedächtnis
def werkklasse(con, werk_id: int) -> str:
    z = con.execute("SELECT bericht, sprache FROM werke WHERE id=?", (werk_id,)).fetchone()
    b = lj(z["bericht"]) if z and z["bericht"] else {}
    zeilen = sum((b.get("zeilen_je_sprache") or {}).values()) if isinstance(b.get("zeilen_je_sprache"), dict) else b.get("zeilen", 0) or 0
    groesse = "klein" if zeilen < 3000 else "mittel" if zeilen < 50000 else "gross"
    bauart = "cli" if any("befehl" in (d or "") or "cli" in (d or "") for d in (b.get("dateien_liste") or [])) else (b.get("bauart") or "bibliothek")
    return f"{(z['sprache'] or 'Python').lower()}/{groesse}/{bauart}"


def kategorie(nische: str, urteil: dict | None, begruendung: str) -> str:
    u = urteil or {}
    if u.get("laufzeit_gewinne"):
        return "laufzeit"
    b = (begruendung or "").lower()
    besser = " ".join(u.get("pareto_besser") or [])
    if "sicherheit" in besser or "bandit" in b or "shell" in b or "eval" in b:
        return "sicherheit"
    if "tote_funktionen" in besser or "tote" in b or "unbenutzt" in b:
        return "toter_code"
    if "vertrag" in b or "vertr" in besser:
        return "vertrag"
    if "tests_fehlgeschlagen" in besser:
        return "fehlerbehebung"
    return "sonst"


MUSTER_MODELL = ("openrouter", "openai/gpt-5.6-luna")   # Masse-Modell; ein Aufruf je angenommener Generation
MUSTER_SYSTEM = """Du abstrahierst eine angenommene Code-Änderung zu einem übertragbaren MUSTER.

Ein Muster sagt, WAS getan wurde und WARUM es wirkte — ohne Werk-, Datei-, Funktions- oder Variablennamen.
Falsch: „in logmuehle bekam filtern() einen Index"
Richtig: „wiederholtes Durchsuchen durch eine mitgeführte Struktur ersetzen, wenn dieselbe Menge mehrfach gelesen wird"

Antworte mit EINEM Satz, höchstens 200 Zeichen, ohne Namen aus dem Werk, ohne Anführungszeichen, ohne Vorrede.
Ist die Änderung zu werkspezifisch, um übertragbar zu sein, antworte genau: NICHT ÜBERTRAGBAR"""


def muster_bilden(con, kandidat_id: int, bereich: str, kategorie: str, begruendung: str, diff: str,
                  lauf_id: int) -> tuple[str | None, str]:
    """Aus einer angenommenen Änderung den abstrahierten Satz gewinnen (Fassung 5, 3.12).

    Grund: Instanzen gelten am fremden Werk nicht, und das Modell übergeht sie zu Recht — gemessen 0
    werkübergreifende Verweise bei 12 Richtungen in drei Läufen. Nur Muster werden werkübergreifend vorgelegt;
    die Instanz bleibt als Beleg daneben stehen.
    """
    try:
        a = aufrufen(con, lauf_id, *MUSTER_MODELL, MUSTER_SYSTEM,
                     f"BEREICHSART: {bereich}\nKATEGORIE: {kategorie}\n\nBEGRÜNDUNG DES KANDIDATEN:\n{begruendung[:800]}\n\nDIFF:\n```diff\n{diff[:3000]}\n```",
                     zweck=f"gedaechtnis.muster.{kategorie}", max_tokens=200, temperatur=0.2)
    except AnbieterFehler as e:
        # Ein Aufruffehler ist NICHT „nicht übertragbar" — er wird als Fehler zurückgegeben, damit der Aufrufer
        # ihn nicht als inhaltliches Urteil zählt (sonst stünde „0 Muster, 19 nicht übertragbar" für 19 Abstürze).
        protokoll.schreiben(con, "gedaechtnis.muster_fehler", lauf_id=lauf_id, kandidat=kandidat_id, fehler=str(e)[:200])
        raise
    text = " ".join(a.text.strip().split())
    if not text or text.upper().startswith("NICHT ÜBERTRAGBAR"):
        return None, MUSTER_MODELL[1]
    return text[:300], MUSTER_MODELL[1]


def art_merken(con, werk_id: int, lauf_id: int, kandidat_id: int, ergebnis: str, bereichsrolle: str = "") -> None:
    tabellen(con)
    k = con.execute("SELECT * FROM kandidaten WHERE id=?", (kandidat_id,)).fetchone()
    if not k:
        return
    if ist_probe(k):        # Fassung 6: kein Probenmuster als Erfahrung an fremde Werke
        protokoll.schreiben(con, "gedaechtnis.probe_uebersprungen", lauf_id=lauf_id, kandidat=kandidat_id,
                            gedaechtnis="art", nische=k["nische"], bereich=k["bereich"],
                            grund="Probenkandidat — kommt in kein Gedächtnis (Fassung 6); bleibt in der Datenbank sichtbar")
        return
    m = lj(k["masse"]) or {}
    u = m.get("_urteil_f2") or {}
    lz = None
    for g in u.get("laufzeit_gewinne") or []:
        try:
            lz = max(lz or 0.0, float(g.split("−")[1].split("%")[0].strip()))
        except Exception:
            pass
    kat = kategorie(k["nische"], u, k["begruendung"])
    # Fassung 5 (3.12): Nur ANGENOMMENE Änderungen werden zum Muster abstrahiert — ein zusätzlicher Aufruf je
    # angenommener Generation. Abgelehnte Wege bleiben Instanz (sie gelten ohnehin nur für ihr Werk).
    muster, muster_von = (None, "")
    if ergebnis == "angenommen" and (k["diff"] or "").strip():
        muster, muster_von = muster_bilden(con, kandidat_id, k["bereich"], kat, k["begruendung"] or "", k["diff"], lauf_id)
    with transaktion(con):
        con.execute("INSERT OR IGNORE INTO artgedaechtnis(werk, werkklasse, lauf_id, generation, kandidat_id, bereich, bereichsrolle, nische, kategorie, ergebnis, zuwachs, laufzeit_prozent, beschreibung, muster, muster_von, erstellt_am) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (werkname(con, werk_id), werkklasse(con, werk_id), lauf_id, k["generation"], kandidat_id, k["bereich"], bereichsrolle, k["nische"],
                     kat, ergebnis, int(u.get("zuwachs") or 0), lz, (k["begruendung"] or "")[:300], muster, muster_von, protokoll.jetzt()))


def art_lesen(con, werkklasse_filter: str | None = None, limit: int | None = 40, werk: str | None = None,
              nur_angenommen: bool = False, *, fremd_zu: str | None = None) -> list[dict]:
    tabellen(con)
    b = []
    p: list = []
    if werkklasse_filter: b.append("werkklasse=?"); p.append(werkklasse_filter)
    if werk: b.append("werk=?"); p.append(werk)
    if fremd_zu is not None: b.append("werk!=?"); p.append(fremd_zu)
    if nur_angenommen: b.append("ergebnis='angenommen'")
    q = "SELECT * FROM artgedaechtnis" + (" WHERE " + " AND ".join(b) if b else "") + " ORDER BY id DESC LIMIT ?"
    return [dict(z) for z in con.execute(q, (*p, -1 if limit is None else limit))]


def art_zusammenfassung(con) -> list[dict]:
    """Je (Werkklasse, Nische, Kategorie): angenommen/abgelehnt, mittlerer Zuwachs, mittlerer Laufzeitgewinn, Werke."""
    tabellen(con)
    out = []
    for z in con.execute("""SELECT werkklasse, nische, kategorie, SUM(ergebnis='angenommen') an, SUM(ergebnis!='angenommen') ab,
                            AVG(CASE WHEN ergebnis='angenommen' THEN zuwachs END) zw, AVG(laufzeit_prozent) lz, GROUP_CONCAT(DISTINCT werk) werke,
                            MIN(id) erster, MAX(id) letzter FROM artgedaechtnis GROUP BY werkklasse, nische, kategorie ORDER BY an DESC"""):
        out.append(dict(z))
    return out


def art_text(con, werk_id: int) -> str:
    """Für Mentor/Schwarm: eigenes Werk als Instanzen (Projektgedächtnis), andere Werke als MUSTER (Fassung 5, 3.12).

    Werkübergreifend werden nur die abstrahierten Sätze vorgelegt — ohne Werk-, Datei- und Funktionsnamen.
    Grund: Instanzen gelten am fremden Werk nicht, und das Modell übergeht sie zu Recht (gemessen: 0
    werkübergreifende Verweise bei 12 Richtungen in drei Läufen, obwohl 25 Instanzen im Fenster standen).
    Die Instanz bleibt als Beleg in der Datenbank, wird aber nicht als Vorlage gezeigt.
    Ein werkübergreifender Verweis wird nie erzwungen: Ein Pflichtfeld erzeugt Scheinbegründungen.
    """
    kl = werkklasse(con, werk_id)
    eigen_werk = werkname(con, werk_id)

    def zeile_instanz(e):
        return (f"[A{e['id']}] Lauf {e['lauf_id']} Gen {e['generation']}, Bereich {e['bereich']}, Nische {e['nische']}, "
                f"Kategorie {e['kategorie']}: {e['ergebnis']}, Zuwachs {e['zuwachs']}, "
                f"Laufzeit −{e['laufzeit_prozent'] or 0:.0f} % — {e['beschreibung'][:140]}")

    def zeile_muster(e):
        lz = f", Laufzeit −{e['laufzeit_prozent']:.0f} %" if e["laufzeit_prozent"] else ""
        return (f"[A{e['id']}] Werkklasse {e['werkklasse']}, Kategorie {e['kategorie']}, Zuwachs {e['zuwachs']}{lz}: "
                f"{e['muster']}")

    # Eigenes Werk: Instanzen, angenommene zuerst.
    eigen = [e for e in art_lesen(con, None, 30, werk=eigen_werk, nur_angenommen=True)]
    eigen += [e for e in art_lesen(con, None, 60, werk=eigen_werk) if e["ergebnis"] != "angenommen"]
    gesehen, eigen_liste = set(), []
    for e in eigen:
        if e["id"] in gesehen:
            continue
        gesehen.add(e["id"]); eigen_liste.append(e)

    # Andere Werke: nur Muster, jedes Muster einmal (gleiche Sätze zusammengefasst).
    fremd, muster_gesehen = [], set()
    # Erst die fremde Population auswählen, dann deduplizieren; kein vorgelagertes
    # Gesamtfenster darf ältere, aber verfügbare fremde Muster unsichtbar machen.
    for e in art_lesen(con, None, None, nur_angenommen=True, fremd_zu=eigen_werk):
        if e["werk"] == eigen_werk or not (e.get("muster") or "").strip():
            continue
        schl = (e["muster"] or "").lower()[:80]
        if schl in muster_gesehen:
            continue
        muster_gesehen.add(schl); fremd.append(e)

    # Mindestanteil des werkübergreifenden Blocks (Fassung 6, 3.12): Der fremde Block belegt mindestens die
    # Hälfte der gezeigten Einträge, mindestens fünf — sofern so viele fremde Muster vorhanden sind.
    # Grund: Ein logmuehle-Lauf sah 13 fremde Muster und lieferte 2 von 5 Verweisen, ein lagerhaus-Lauf sah 3
    # und lieferte 0. Bei 17 Diensten verdrängt die Masse eigener Einträge die fremden allein durch Menge.
    # Der Anteil steuert, WAS GEZEIGT wird, nicht was zitiert werden muss — ein Pflichtfeld erzeugt Scheinbegründungen.
    GEZEIGT = 25
    fremd_min = min(len(fremd), max(5, (GEZEIGT + 1) // 2))
    eigen_max = max(0, GEZEIGT - fremd_min)
    fremd_zeigen = fremd[:max(fremd_min, GEZEIGT - min(len(eigen_liste), eigen_max))]
    eigen_zeigen = eigen_liste[:eigen_max]

    teile = [f"EIGENES WERK {eigen_werk} (= Projektgedächtnis, nicht werkübergreifend; Instanzen):"]
    teile += [zeile_instanz(e) for e in eigen_zeigen] or ["(noch keine Einträge)"]
    teile += ["", "ANDERE WERKE (= Artgedächtnis, werkübergreifend; MUSTER ohne Werk-, Datei- und Funktionsnamen):"]
    teile += [zeile_muster(e) for e in fremd_zeigen] or ["(noch keine Muster)"]
    return "\n".join(teile)


def art_import(con, lauf_id: int) -> int:
    """Rückwirkend: angenommene/überlebte/abgelehnte Kandidaten eines Laufs (mit Maß) ins Artgedächtnis (Läufe vor Phase 3)."""
    tabellen(con)
    lauf = con.execute("SELECT werk_id FROM laeufe WHERE id=?", (lauf_id,)).fetchone()
    n = 0
    for k in con.execute("SELECT id, status, bereich FROM kandidaten WHERE lauf_id=? AND masse IS NOT NULL AND nische!='probe' AND status IN ('angenommen','ueberlebt','abgelehnt')", (lauf_id,)):
        art_merken(con, lauf["werk_id"], lauf_id, k["id"], k["status"], bereichsrolle=k["bereich"])
        n += 1
    return n


# ---------------------------------------------------------------- Geschmacksgedächtnis
def merkmale_kandidat(con, kandidat_id: int) -> dict:
    k = con.execute("SELECT * FROM kandidaten WHERE id=?", (kandidat_id,)).fetchone()
    m = lj(k["masse"]) or {}
    u = m.get("_urteil_f2") or {}
    diff = k["diff"] or ""
    plus = sum(1 for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++"))
    minus = sum(1 for l in diff.splitlines() if l.startswith("-") and not l.startswith("---"))
    dateien = set(re.findall(r"^\+\+\+ b/(\S+)", diff, re.M))
    return {
        "nische": k["nische"], "bereich": k["bereich"], "hersteller": (k["modell"] or "/").split("/")[0],
        "zuwachs": int(u.get("zuwachs") or 0), "laufzeit_gewinn": bool(u.get("laufzeit_gewinne")),
        "diff_zeilen": plus + minus, "diff_klasse": "klein" if plus + minus <= 20 else "mittel" if plus + minus <= 60 else "gross",
        "netto_zeilen": plus - minus, "wird_kleiner": plus < minus,
        "dateien": len(dateien), "aendert_tests": any(d.startswith("tests/") for d in dateien),
        "vertragsaenderung": bool((k["vertraege"] or "").strip()) and (k["vertraege"] or "").strip().lower() != "keine",
        "neue_funktion": "+def " in diff, "kommentare_hinzu": sum(1 for l in diff.splitlines() if l.startswith("+") and l[1:].strip().startswith("#")),
    }


def geschmack_merken(con, werk_id: int, lauf_id: int, generation: int, kandidat_id: int | None, entscheidung: str, grund: str, von: str, quelle: str = "freigabe") -> None:
    tabellen(con)
    if kandidat_id:         # Fassung 6: keine Probenentscheidung als Geschmack lernen
        k = con.execute("SELECT nische, bereich, ist_probe FROM kandidaten WHERE id=?", (kandidat_id,)).fetchone()
        if ist_probe(k):
            protokoll.schreiben(con, "gedaechtnis.probe_uebersprungen", lauf_id=lauf_id, kandidat=kandidat_id,
                                gedaechtnis="geschmack", nische=k["nische"], bereich=k["bereich"],
                                grund="Probenkandidat — kommt in kein Gedächtnis (Fassung 6); bleibt in der Datenbank sichtbar")
            return
    merk = merkmale_kandidat(con, kandidat_id) if kandidat_id else {}
    with transaktion(con):
        con.execute("INSERT OR IGNORE INTO geschmack(werk, lauf_id, generation, kandidat_id, entscheidung, grund, von, merkmale, quelle, erstellt_am) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (werkname(con, werk_id), lauf_id, generation, kandidat_id, entscheidung, grund[:400], von, j(merk), quelle, protokoll.jetzt()))


def _diskret(merk: dict) -> list[str]:
    f = []
    for k, v in merk.items():
        if isinstance(v, bool):
            f.append(f"{k}={v}")
        elif isinstance(v, (int, float)):
            if k in ("zuwachs", "netto_zeilen", "dateien", "kommentare_hinzu"):
                f.append(f"{k}={'neg' if v < 0 else '0' if v == 0 else '1' if v == 1 else 'viele'}")
            elif k == "diff_zeilen":
                f.append(f"{k}={'klein' if v <= 20 else 'mittel' if v <= 60 else 'gross'}")
        else:
            f.append(f"{k}={v}")
    return f


class Vorhersage:
    """Naive Bayes mit Laplace-Glättung über diskretisierte Merkmale."""

    def __init__(self, eintraege: list[dict]):
        self.n = Counter(); self.z = defaultdict(Counter); self.merkmale = set()
        for e in eintraege:
            ent = e["entscheidung"]; self.n[ent] += 1
            for f in _diskret(lj(e["merkmale"]) if isinstance(e["merkmale"], str) else e["merkmale"]):
                self.z[ent][f] += 1; self.merkmale.add(f.split("=")[0])
        self.gesamt = sum(self.n.values())

    def vorhersagen(self, merk: dict) -> tuple[str, float, list[str]]:
        fs = _diskret(merk)
        punkte = {}
        for ent, n in self.n.items():
            lp = math.log((n + 1) / (self.gesamt + len(self.n)))
            for f in fs:
                lp += math.log((self.z[ent][f] + 1) / (n + 2))
            punkte[ent] = lp
        beste = max(punkte, key=punkte.get)
        s = sum(math.exp(v - punkte[beste]) for v in punkte.values())
        # die drei Merkmale mit dem größten Beitrag zur Entscheidung
        beitraege = []
        for f in fs:
            andere = [e for e in self.n if e != beste]
            if andere:
                a = andere[0]
                b = math.log((self.z[beste][f] + 1) / (self.n[beste] + 2)) - math.log((self.z[a][f] + 1) / (self.n[a] + 2))
                beitraege.append((b, f))
        beitraege.sort(reverse=True)
        return beste, round(1 / s, 3), [f for _, f in beitraege[:3]]


def geschmack_modell(con, werk: str | None = None, quelle: str | None = None, hoechstens: int | None = None) -> Vorhersage | None:
    tabellen(con)
    q = "SELECT * FROM geschmack WHERE kandidat_id IS NOT NULL"; p: list = []
    if werk:
        q += " AND werk=?"; p.append(werk)
    if quelle:
        q += " AND quelle=?"; p.append(quelle)
    q += " ORDER BY id"
    rows = [dict(z) for z in con.execute(q, p)]
    if hoechstens:
        rows = rows[:hoechstens]
    if len(rows) < 20:
        return None
    return Vorhersage(rows)


def geschmack_vorhersage(con, kandidat_id: int, quelle: str | None = None) -> dict | None:
    m = geschmack_modell(con, quelle=quelle)
    if not m:
        return None
    ent, p, gruende = m.vorhersagen(merkmale_kandidat(con, kandidat_id))
    return {"vorhersage": ent, "sicherheit": p, "merkmale": gruende, "gelernt_aus": m.gesamt}
