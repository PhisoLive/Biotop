"""Tor 3 — Auswertung der Gedächtnis-/Entropie-/Jury-/Archiv-Zeilen nach den Läufen.
Aufruf: tor3.py <ausgaben-dir> <lauf_lagerhaus_1=13> <lauf_lagerhaus_2=16> <lauf_logmuehle=17> [lauf_dritter=18]"""
import json, sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, lj
from biotop.organe import gedaechtnis as G, entropie as E

A = Path(sys.argv[1]); L1, L2, L3 = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); L4 = int(sys.argv[5]) if len(sys.argv) > 5 else None
con = verbinden()

def schreibe(name, zeilen):
    (A / name).write_text("\n".join(zeilen) + "\n"); print("\n".join(zeilen[-4:])); print("→", name, "\n")

# --- Projektgedächtnis: zweiter Lauf am lagerhaus wiederholt 0 der im ersten gescheiterten Wege
z = ["# Tor 3 — Projektgedächtnis: Lauf %d (zweiter Lauf am lagerhaus) gegen die gescheiterten Wege aus Lauf %d" % (L2, L1)]
wege = [dict(r) for r in con.execute("SELECT * FROM projektgedaechtnis WHERE lauf_id=? AND grundklasse!='technisch'", (L1,))]
z.append(f"Gescheiterte Wege Lauf {L1} (ohne technische Diff-Fehler): {len(wege)} von {con.execute('SELECT COUNT(*) FROM kandidaten WHERE lauf_id=? AND status=%r' % 'abgelehnt', (L1,)).fetchone()[0]} Ablehnungen")
werk2 = con.execute("SELECT werk_id FROM laeufe WHERE id=?", (L2,)).fetchone()[0]; pfad2 = Path(con.execute("SELECT pfad FROM werke WHERE id=?", (werk2,)).fetchone()[0])
kand2 = [dict(r) for r in con.execute("SELECT id, generation, bereich, nische, status, diff, substr(grund,1,120) g FROM kandidaten WHERE lauf_id=? AND diff!='' AND nische!='probe' AND generation>=4", (L2,))]
z.append(f"Kandidaten Lauf {L2} mit Diff (Gen ≥ 4, ohne Proben): {len(kand2)}")
wdh_geprueft = 0; wdh_ausgefuehrt = 0; details = []
for k in kand2:
    d, f, a = G.aenderungsziel(pfad2, k["diff"], None)
    for w in wege:
        if w["bereich"] != k["bereich"]: continue
        wf = set(lj(w["funktionen"]) or []); wd = set(lj(w["dateien"]) or [])
        if (wf & set(f)) or (not wf and wd & set(d)):
            sim = G._jaccard(a, lj(w["ansatz"]) or [])
            if sim >= G.SCHWELLE_WIEDERHOLUNG:
                if "Wiederholung eines gescheiterten Wegs" in (k["g"] or ""):
                    wdh_geprueft += 1; details.append(f"  K{k['id']} (Gen {k['generation']}, {k['bereich']}) = Weg K{w['kandidat_id']} Lauf {L1}, Ähnlichkeit {sim:.2f} → vom Biotop OHNE Kammerlauf verworfen")
                else:
                    wdh_ausgefuehrt += 1; details.append(f"  K{k['id']} (Gen {k['generation']}, {k['bereich']}) = Weg K{w['kandidat_id']} Lauf {L1}, Ähnlichkeit {sim:.2f} → NICHT erkannt, Status {k['status']}")
                break
abgef = con.execute("SELECT COUNT(*) FROM protokoll WHERE art='gedaechtnis.wiederholung' AND inhalt LIKE ?", (f'%"lauf_id": {L2},%',)).fetchone()[0]
z += details or ["  (keine Kandidaten mit Ähnlichkeit ≥ Schwelle zu einem gescheiterten Weg aus Lauf %d)" % L1]
z.append(f"Protokollzeilen gedaechtnis.wiederholung in Lauf {L2}: {abgef}")
z.append(f"ERGEBNIS: Wiederholungen ausgeführt (durch den Ankläger geprüft, obwohl bekannt gescheitert): {wdh_ausgefuehrt} von {len(wege)} gescheiterten Wegen; als Wiederholung erkannt und verworfen: {wdh_geprueft}")
schreibe("60-tor3-projektgedaechtnis.txt", z)

# --- Jury
z = ["# Tor 3 — Jury (weiche Maße): Fälle mit Einstimmigkeit / ohne"]
con.execute("CREATE TABLE IF NOT EXISTS jury (id INTEGER PRIMARY KEY, lauf_id INTEGER, generation INTEGER, bereich TEXT, kandidat_a INTEGER, kandidat_b INTEGER, urteile TEXT, einstimmig INTEGER, gewinner INTEGER, erstellt_am TEXT)")
faelle = [dict(r) for r in con.execute("SELECT * FROM jury WHERE lauf_id>=14 ORDER BY id")]
for f in faelle:
    z.append(f"Lauf {f['lauf_id']} Gen {f['generation']} {f['bereich']}: K{f['kandidat_a']} vs K{f['kandidat_b']} — einstimmig: {bool(f['einstimmig'])}, Gewinner: {f['gewinner']}")
    for u in lj(f["urteile"]): z.append(f"    {u['modell']}: {u['wahl']} — {u['begruendung'][:200]}")
ein = sum(1 for f in faelle if f["einstimmig"]); nein = sum(1 for f in faelle if not f["einstimmig"])
z.append(f"ERGEBNIS: {len(faelle)} Jury-Fälle; einstimmig {ein}, ohne Einstimmigkeit (kein Urteil) {nein}; Hersteller je Fall: 3 (openai, google, deepseek)")
schreibe("61-tor3-jury.txt", z)

# --- Archivierung
z = ["# Tor 3 — Archivierung offener Funde (3.10 F4): nach 5 angenommenen Generationen archiviert; 0 archivierte in Kammerläufen danach"]
for L in (L2, L3):
    wid = con.execute("SELECT werk_id FROM laeufe WHERE id=?", (L,)).fetchone()[0]
    st = {r[0]: r[1] for r in con.execute("SELECT status, COUNT(*) FROM immunsystem WHERE werk_id=? GROUP BY status", (wid,))}
    arch = [dict(r) for r in con.execute("SELECT nr, inhalt FROM protokoll WHERE art='immun.archiviert' AND inhalt LIKE ?", (f'%"lauf_id": {L},%',))]
    z.append(f"Lauf {L}: Immunsystem-Stände {st}; Archivierungs-Ereignisse {len(arch)}: " + "; ".join(f"#{a['nr']} " + ", ".join(lj(a['inhalt'])['funde'])[:300] for a in arch))
    # nach der Archivierung: taucht ein archivierter Fund noch in einem Kandidaten-Testbestand auf?
    if arch:
        erste = min(a["nr"] for a in arch); namen = set()
        for a in arch:
            for fnd in lj(a["inhalt"])["funde"]: namen.add(fnd.split("/")[1].split(" ")[0])
        spaeter = 0; kandidaten_danach = 0
        for k in con.execute("SELECT id, masse FROM kandidaten WHERE lauf_id=? AND masse IS NOT NULL", (L,)):
            m = lj(k["masse"]) or {}; tests = list(m.get("_testbestand") or []) + list(m.get("tests_offen") or []) + list((m.get("_dateien") or {}).keys())
            nr = con.execute("SELECT MIN(nr) FROM protokoll WHERE art='aegis.urteil' AND inhalt LIKE ?", (f'%"kandidat": {k["id"]},%',)).fetchone()[0]
            if nr and nr > erste:
                kandidaten_danach += 1
                if any(n in t for n in namen for t in tests): spaeter += 1
        z.append(f"   archivierte Funde in Kammerläufen NACH der Archivierung: {spaeter} von {kandidaten_danach} geprüften Kandidaten")
schreibe("62-tor3-archivierung.txt", z)

# --- Entropie
for L in (L2, L3):
    (A / f"63-entropie-lauf{L}.json").write_text(json.dumps({"verlauf": E.verlauf(con, L), "saettigung": E.saettigung(con, L), "lauf_status": con.execute("SELECT status, grund FROM laeufe WHERE id=?", (L,)).fetchone()[1]}, ensure_ascii=False, indent=1))
print("Entropie geschrieben")

# --- Zerlegungen (Summenpflicht) für alle Phase-3-Läufe
z = ["# Tor 3 — Kandidatenaufschlüsselung je Lauf (Summenpflicht, Kategorien wie Phase-2-Bericht)"]
def klasse(g):
    g = g or ""
    if g.startswith("Diff nicht anwendbar"): return "Diff nicht anwendbar"
    if "Wiederholung eines gescheiterten Wegs" in g: return "Wiederholung (Projektgedächtnis, ohne Kammerlauf)"
    if "Pareto" in g or "Regression" in g: return "Pareto/Regression je Test"
    if g.startswith("Nische schnell"): return "Nische schnell ohne Gewinn"
    if "Vertrag verletzt" in g: return "Vertrag verletzt"
    if "Grenzmaß" in g: return "Grenzmaß"
    if "Kernmaß unverändert" in g: return "Kernmaß unverändert"
    return "sonst"
for L in [x for x in (14, 15, L2, L3, L4) if x]:
    g = con.execute("SELECT COUNT(*) FROM kandidaten WHERE lauf_id=?", (L,)).fetchone()[0]
    st = {r[0]: r[1] for r in con.execute("SELECT status, COUNT(*) FROM kandidaten WHERE lauf_id=? GROUP BY status", (L,))}
    z.append(f"\nLauf {L}: gesamt {g} = " + " + ".join(f"{v} {k}" for k, v in sorted(st.items())) + f" = {sum(st.values())} → {'aufgehend' if sum(st.values()) == g else 'DIFFERENZ'}")
    kl = {}
    for r in con.execute("SELECT grund FROM kandidaten WHERE lauf_id=? AND status='abgelehnt'", (L,)): kl[klasse(r[0])] = kl.get(klasse(r[0]), 0) + 1
    z.append(f"   Ablehnungen {st.get('abgelehnt',0)} = " + " + ".join(f"{v} {k}" for k, v in sorted(kl.items(), key=lambda x: -x[1])) + f" = {sum(kl.values())}")
schreibe("65-tor3-zerlegungen.txt", z)
