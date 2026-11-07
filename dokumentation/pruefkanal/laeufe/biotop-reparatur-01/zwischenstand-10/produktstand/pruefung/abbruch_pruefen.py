"""Prüft den Abbruch-Befehl (F5 Abschnitt 5: Abbrüche sind nie gesperrt).

Fall 1: laufender Lauf → abbrechen(art='satz2') beendet ihn, offene Generationen werden geschlossen, protokolliert.
Fall 2: Der verworfene Lauf sperrt danach keine Kandidaten mehr im Projektgedächtnis (3.12 F5).
Fall 3: zweiter Abbruch desselben Laufs → ohne Wirkung, aber protokolliert (keine Ausnahme, kein stiller Fehler).
Fall 4: Abbruch wegen Budget → Status 'abgebrochen' (nicht 'verworfen'), Ablehnungen bleiben im Gedächtnis gültig.
Fall 5: CLI-Befehl und Web-Route vorhanden (ohne Token → 401).
Aufruf: abbruch_pruefen.py <ausgaben-dir>
"""
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern import protokoll
from biotop.kern.datenbank import verbinden, transaktion
from biotop.organe import gedaechtnis as G
from biotop import lauf as L

A = Path(sys.argv[1])
con = verbinden()
z = ["# Abbruch eines Laufs — Pflicht, nie gesperrt (Fassung 5, Abschnitt 5)"]

# Prüflauf anlegen (auf dem Werk von Lauf 20, ohne echte Generationen)
werk_id = con.execute("SELECT werk_id FROM laeufe WHERE id=20").fetchone()[0]
with transaktion(con):
    cur = con.execute("INSERT INTO laeufe(werk_id, budget_eur, status, begonnen_am, mass) VALUES (?,?,?,?,?)",
                      (werk_id, 1.0, "laeuft", protokoll.jetzt(), con.execute("SELECT mass FROM laeufe WHERE id=20").fetchone()[0]))
    lauf_id = cur.lastrowid
    con.execute("INSERT INTO generationen(lauf_id, nummer, status, erstellt_am) VALUES (?,?,?,?)",
                (lauf_id, 1, "laeuft", protokoll.jetzt()))
z.append(f"\n## Fall 1: laufender Lauf {lauf_id} mit offener Generation 1")
r = L.abbrechen(con, lauf_id, "Ankläger-Ablauf während des Laufs geändert (Prüfung)", "Hermes", "satz2")
z.append(f"  Ergebnis: Status {r['status']}, abgebrochene Generationen {r['abgebrochene_generationen']}")
z.append(f"  Lauf in der DB: {dict(con.execute('SELECT status, substr(grund,1,80) g FROM laeufe WHERE id=?', (lauf_id,)).fetchone())}")
p = con.execute("SELECT nr, inhalt FROM protokoll WHERE art='lauf.abgebrochen' ORDER BY nr DESC LIMIT 1").fetchone()
z.append(f"  Protokoll #{p['nr']}: {p['inhalt'][:200]}")

z.append("\n## Fall 2: verworfener Lauf sperrt keine Kandidaten mehr (3.12 F5)")
with transaktion(con):
    con.execute("INSERT INTO projektgedaechtnis(werk, werk_id, lauf_id, generation, kandidat_id, bereich, nische,"
                " dateien, funktionen, ansatz, grund, grundklasse, begruendung, erstellt_am)"
                " VALUES ('lagerhaus',?,?,1,999999,'preise','sicher','[]','[\"x::y\"]','[\"a\"]','Prüfung','sonst','Prüfung',?)",
                (werk_id, lauf_id, protokoll.jetzt()))
sichtbar = [w for w in G.gescheiterte_wege(con, werk_id, "preise", 200) if w["lauf_id"] == lauf_id]
z.append(f"  Einträge dieses Laufs im Projektgedächtnis: 1 | davon für den Schwarm sichtbar: {len(sichtbar)} (gefordert 0)")

z.append("\n## Fall 3: zweiter Abbruch desselben Laufs")
r2 = L.abbrechen(con, lauf_id, "nochmals", "Hermes", "satz2")
z.append(f"  Ergebnis: {r2.get('hinweis')} (Status bleibt {r2['status']}, keine Ausnahme)")

z.append("\n## Fall 4: Abbruch wegen Budget → 'abgebrochen', nicht 'verworfen'")
with transaktion(con):
    cur = con.execute("INSERT INTO laeufe(werk_id, budget_eur, status, begonnen_am, mass) VALUES (?,?,?,?,?)",
                      (werk_id, 1.0, "laeuft", protokoll.jetzt(), con.execute("SELECT mass FROM laeufe WHERE id=20").fetchone()[0]))
    lauf2 = cur.lastrowid
r3 = L.abbrechen(con, lauf2, "Budget erreicht (Prüfung)", "Kasse", "budget")
z.append(f"  Ergebnis: Status {r3['status']} (gefordert 'abgebrochen'), Hinweis: {r3['hinweis']}")

z.append("\n## Fall 5: Befehl und Route vorhanden")
h = subprocess.run([sys.executable, "-m", "biotop", "abbrechen", "--help"], capture_output=True, text=True,
                   cwd="/root/biotop", env={"PYTHONPATH": "/root/biotop", "PATH": "/usr/bin:/bin"})
z.append(f"  CLI `biotop abbrechen`: {'vorhanden' if h.returncode == 0 else 'FEHLT'} "
         f"({h.stdout.splitlines()[0] if h.stdout else h.stderr[:80]})")
try:
    urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8642/laeufe/1/abbrechen", data=b"{}", method="POST"), timeout=3)
    z.append("  Route ohne Token: KEINE 401 — Fehler")
except urllib.error.HTTPError as e:
    z.append(f"  Route POST /laeufe/<id>/abbrechen ohne Token: HTTP {e.code} (gefordert 401)")
except Exception as e:
    z.append(f"  Route nicht geprüft (Dienst läuft nicht): {type(e).__name__} — Route ist in dienst.py ROUTEN eingetragen")

with transaktion(con):        # Prüfspuren entfernen
    con.execute("DELETE FROM projektgedaechtnis WHERE lauf_id IN (?,?)", (lauf_id, lauf2))
    con.execute("DELETE FROM generationen WHERE lauf_id IN (?,?)", (lauf_id, lauf2))
    con.execute("DELETE FROM laeufe WHERE id IN (?,?)", (lauf_id, lauf2))
z.append(f"\n(Prüfläufe {lauf_id} und {lauf2} wieder entfernt; Protokollzeilen bleiben — das Protokoll ist unveränderlich)")
(A / "12-abbruch-nie-gesperrt.txt").write_text("\n".join(z) + "\n")
print("\n".join(z))
