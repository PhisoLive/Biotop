"""Vorgabe Philipp 19.09.2026: Lauf 16 verwerfen (Satz 2 F4), K1191-Staffelpreis-Test auf offen_norm zurückstufen,
K1165-Test bleibt offen (Vertrag bericht→preise trägt ihn). Lauf 18 vom Stand Lauf 16 Gen 3."""
import sys
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden, transaktion
from biotop.kern import protokoll
con = verbinden()
with transaktion(con):
    con.execute("UPDATE laeufe SET status='verworfen', beendet_am=? WHERE id=16", (protokoll.jetzt(),))
    con.execute("UPDATE immunsystem SET status='offen_norm', ursprung=ursprung || ? WHERE werk_id=14 AND name='aegis_k1191_preise' AND status IN ('gefunden','offen')",
                (" | zurückgestuft auf offen_norm (Vorgabe Philipp 19.09.2026, F4 3.7: Angriffstest ohne Absturz/Verweis, der am Kandidaten fällt, ist Norm, kein Fund; kodierte den K1165-Fehler als Norm)",))
    con.execute("UPDATE immunsystem SET status='offen' WHERE werk_id=14 AND status='gefunden'")
protokoll.schreiben(con, "lauf.verworfen", lauf_id=16, von="Philipp (19.09.2026)",
                    grund="Verfassungssatz 2 F4: Ankläger-Ablauf korrigiert — Pareto je Test gilt für Tests im Werk, Verträge und Verfassung; ein neuer Angriffstest, der an der Vorgeneration besteht und am Kandidaten fällt, tötet nur bei Absturz des Kandidaten oder explizitem Vertrags-/Verfassungsverweis, sonst offen, 0 Punkte, kein Kill. Lauf 16 Gen 4–9 unter altem Ablauf gemessen. Nachprobe Zeile 7 (Lauf 16 Gen 1–3) bleibt gültig und wird als eigener Lauf mit ihrem Messgerät-Stand ausgewiesen (Commit ccb55d2/791aae5). Lauf 18 startet vom Stand Lauf 16 Gen 3.",
                    immunsystem="aegis_k1191_preise → offen_norm; hermes_k1165_wert_grundpreis bleibt offen")
protokoll.schreiben(con, "biotop.regel", von="Philipp (19.09.2026)", regel="Abbrüche nach Verfassungssatz 2 (Lauf anhalten/verwerfen wegen Messgerät-Änderung) sind vom Freigabe-Gate ausgenommen — immer erlaubt, immer protokolliert (lauf.verworfen).")
print({r[0]: r[1] for r in con.execute("SELECT status, COUNT(*) FROM immunsystem WHERE werk_id=14 GROUP BY status")})
print(dict(con.execute("SELECT id, status FROM laeufe WHERE id=16").fetchone()))
