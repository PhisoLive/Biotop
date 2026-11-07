"""Tor 3, Jury-Zeile: Beleg für den Fall OHNE Einstimmigkeit. Die drei Juroren bekommen zwei Kandidaten, die sich in
Lesbarkeit/Eleganz in gegensätzliche Richtungen unterscheiden (kurz+dicht gegen lang+explizit) — darüber gehen
Geschmäcker auseinander. Kein Eingriff ins Messgerät: die Jury läuft mit ihrem echten Ablauf (organe/jury.entscheiden),
nur die beiden Kandidaten stellt Hermes; sie werden als Kandidaten der Probe in die Datenbank gelegt.
Aufruf: jury_probe.py <ausgaben-dir> <lauf_id>
"""
import sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, transaktion
from biotop.kern import protokoll
from biotop.organe import jury

A = Path(sys.argv[1]); LAUF = int(sys.argv[2])
con = verbinden()

DIFF_A = """--- a/logmuehle/lesen/eintrag.py
+++ b/logmuehle/lesen/eintrag.py
@@
-def zeit_lesen(text):
-    teile = text.split(" ")
-    zeitpunkt = datetime.strptime(teile[0], "%d/%b/%Y:%H:%M:%S")
-    return zeitpunkt.replace(tzinfo=_tz(teile[1]))
+def zeit_lesen(text):
+    return datetime.strptime(text[:20], "%d/%b/%Y:%H:%M:%S").replace(tzinfo=_tz(text[21:]))
"""
DIFF_B = """--- a/logmuehle/lesen/eintrag.py
+++ b/logmuehle/lesen/eintrag.py
@@
-def zeit_lesen(text):
-    teile = text.split(" ")
-    zeitpunkt = datetime.strptime(teile[0], "%d/%b/%Y:%H:%M:%S")
-    return zeitpunkt.replace(tzinfo=_tz(teile[1]))
+def zeit_lesen(text):
+    roh, _, zone = text.partition(" ")
+    try:
+        zeitpunkt = datetime.strptime(roh, "%d/%b/%Y:%H:%M:%S")
+    except ValueError as fehler:
+        raise LeseFehler(f"Zeitangabe nicht lesbar: {text!r}") from fehler
+    if not zone:
+        raise LeseFehler(f"Zeitzone fehlt in {text!r}")
+    return zeitpunkt.replace(tzinfo=_tz(zone))
"""
ids = []
with transaktion(con):
    for diff, begr in ((DIFF_A, "Eine Zeile: strptime auf den Zeitanteil, Zeitzone direkt angehaengt. Kuerzest moegliche Fassung, keine eigene Fehlerbehandlung."),
                       (DIFF_B, "Neun Zeilen: fangt ValueError und fehlende Zeitzone ab und meldet beides als LeseFehler mit dem strittigen Text.")):
        cur = con.execute("INSERT INTO kandidaten(lauf_id, generation, bereich, nische, modell, diff, begruendung, status, grund, erstellt_am, ist_probe) "
                          "VALUES (?,?,?,?,?,?,?,?,?,?,1)",
                          (LAUF, 0, "probe_jury_hermes", "elegant", "probe/hermes", diff, begr, "probe", "Probe Hermes fuer die Jury-Zeile (Tor 3), nie im Werk", protokoll.jetzt()))
        ids.append(cur.lastrowid)
e = jury.entscheiden(con, LAUF, 0, "probe_jury_hermes", ids[0], ids[1])
zeilen = ["# Tor 3 — Jury, Fall OHNE Einstimmigkeit (Probe von Hermes; Jury laeuft mit ihrem echten Ablauf organe/jury.entscheiden)",
          f"Kandidat A (K{ids[0]}): eine Zeile, keine Fehlerbehandlung. Kandidat B (K{ids[1]}): neun Zeilen, zwei eigene Fehlermeldungen. Zielkonflikt Kuerze gegen Fehlermeldungsqualitaet.",
          f"Einstimmig: {bool(e.get('einstimmig'))} | Gewinner: {e.get('gewinner')} (None = kein Urteil)"]
for u in e.get("urteile", []):
    zeilen.append(f"  {u.get('modell')}: waehlt {u.get('wahl')} — {(u.get('begruendung') or '')[:220]}")
zeilen.append(f"ERGEBNIS dieser Probe: {'kein Urteil, protokolliert' if not e.get('einstimmig') else 'einstimmig'}")
alle = [dict(r) for r in con.execute("SELECT lauf_id, generation, bereich, einstimmig, gewinner FROM jury ORDER BY id")]
zeilen.append(f"Jury-Faelle insgesamt: {len(alle)} — einstimmig {sum(1 for x in alle if x['einstimmig'])}, ohne Einstimmigkeit {sum(1 for x in alle if not x['einstimmig'])}")
for x in alle:
    zeilen.append(f"   Lauf {x['lauf_id']} Gen {x['generation']} {x['bereich']}: einstimmig {bool(x['einstimmig'])}, Gewinner {x['gewinner']}")
(A / "95-tor3-jury-uneinig2.txt").write_text("\n".join(zeilen) + "\n")
print("\n".join(zeilen))
