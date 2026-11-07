"""ZWISCHENBERICHT.md + DATEIEN.txt + PRUEFSUMME-ORDNER.txt für den Phase-3-Ordner — Kosten aus der Datenbank, Stand der Läufe,
Liste des Offenen. Regel Philipp 19.09.2026: vor jedem Sitzungsende; ein Ordner ohne Bericht gilt als nicht abgeliefert.
Aufruf: zwischenbericht.py <ordner> [Hinweis-Text]"""
import hashlib, os, subprocess, sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden
from biotop.kern import protokoll

B = Path(sys.argv[1]); hinweis = sys.argv[2] if len(sys.argv) > 2 else ""
con = verbinden()
z = []
z.append(f"# Biotop Phase 3 — ZWISCHENBERICHT (automatisch, {protokoll.jetzt()})")
z.append("Kein Abschluss. Zahlen aus der Datenbank; jede Zahl mit Bezugsgröße. Endgültiger Bericht: BERICHT.md (fehlt er, ist die Phase nicht abgeschlossen).")
if hinweis: z.append(f"\n**Hinweis:** {hinweis}")
z.append("\n## Läufe der Phase 3 (ab Lauf 14)")
z.append("| Lauf | Werk | Status | Budget € | Generationen (angenommen/abgelehnt/offen) | Aufrufe | Kosten € |"); z.append("|---|---|---|---|---|---|---|")
for l in con.execute("SELECT l.id, l.status, l.budget_eur, w.name werk FROM laeufe l LEFT JOIN werke w ON w.id=l.werk_id WHERE l.id>=14 ORDER BY l.id"):
    g = {r[0]: r[1] for r in con.execute("SELECT status, COUNT(*) FROM generationen WHERE lauf_id=? AND nummer>0 GROUP BY status", (l["id"],))}
    k = con.execute("SELECT COUNT(*), COALESCE(SUM(kosten_eur),0) FROM kasse WHERE lauf_id=?", (l["id"],)).fetchone()
    z.append(f"| {l['id']} | {l['werk']} | {l['status']} | {l['budget_eur']:.2f} | {g.get('angenommen',0)}/{g.get('abgelehnt',0)}/{g.get('vorgelegt',0)+g.get('laeuft',0)} | {k[0]} | {k[1]:.4f} |")
k = con.execute("SELECT COUNT(*), COALESCE(SUM(kosten_eur),0), COALESCE(SUM(tokens_ein),0), COALESCE(SUM(tokens_aus),0) FROM kasse WHERE lauf_id>=14").fetchone()
ks = con.execute("SELECT COUNT(*), COALESCE(SUM(kosten_eur),0) FROM kasse WHERE lauf_id>=14 AND zweck LIKE 'schwer.%'").fetchone()
z.append(f"\n**Kosten Phase 3 gesamt: {k[0]} Aufrufe, {k[1]:.4f} € von 15,00 € (hart); Token {k[2]} ein / {k[3]} aus; schwere Aufrufe {ks[0]} = {ks[1]:.4f} €.**")
z.append("\n## Tor 3 — Stand je Zeile (erledigt = Ausgabedatei liegt vor; Wertung im BERICHT.md)")
A = B / "ausgaben"
zeilen = [("Nachprobe Zeile 7", "14-nachprobe-z7-ergebnis.txt"), ("Projektgedächtnis (Lauf 16 vs 13)", "60-tor3-projektgedaechtnis.txt"), ("Artgedächtnis (dritter Lauf, werkübergreifend)", "81-mentor-lauf18.json"),
          ("Mentor ≥ 3 Richtungen je Werk", "40-mentor-lauf17.json"), ("Entropie (Sättigung lagerhaus)", "63-entropie-lauf16.json"), ("Jury", "61-tor3-jury.txt"), ("Geschmack (Mechanik, Regel P1)", "21-tor3-geschmack.txt"),
          ("Archivierung offener Funde", "62-tor3-archivierung.txt"), ("Oberfläche", "70-tor3-oberflaeche.txt"), ("Kandidatenaufschlüsselung je Lauf", "65-tor3-zerlegungen.txt"), ("Kurven beider Werke", "64-kurve-lauf17.json")]
for n, f in zeilen:
    z.append(f"- {n}: {'erledigt (' + f + ')' if (A / f).exists() else 'OFFEN'}")
z.append("\n## Offen")
for n, f in zeilen:
    if not (A / f).exists(): z.append(f"- {n}")
if not (B / "BERICHT.md").exists() or "im Aufbau" in (B / "BERICHT.md").read_text()[:200]: z.append("- BERICHT.md (Endbericht) — noch nicht geschrieben")
z.append("- Ordner-Versiegelung (DATEIEN.txt/PRUEFSUMME sind Zwischenstand, werden beim Abschluss neu geschrieben)")
z.append(f"\nBiotop-Commit: {subprocess.run(['git','rev-parse','--short','HEAD'],cwd='/root/biotop',capture_output=True,text=True).stdout.strip()} · Protokoll bis #{con.execute('SELECT MAX(nr) FROM protokoll').fetchone()[0]}")
(B / "ZWISCHENBERICHT.md").write_text("\n".join(z) + "\n")
# DATEIEN + Prüfsumme
dateien = sorted(p for p in B.rglob("*") if p.is_file() and p.name not in ("DATEIEN.txt", "PRUEFSUMME-ORDNER.txt"))
liste = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(B)}\n" for p in dateien)
(B / "DATEIEN.txt").write_text(liste)
ps = hashlib.sha256(liste.encode()).hexdigest()
(B / "PRUEFSUMME-ORDNER.txt").write_text(ps + "\n")
subprocess.run(["chown", "-R", "root:caddy", str(B)]); subprocess.run(["bash", "-c", f"find {B} -type d -exec chmod 750 {{}} \\; ; find {B} -type f -exec chmod 640 {{}} \\;"])
print(f"ZWISCHENBERICHT geschrieben: {len(dateien)} Dateien, Ordnerprüfsumme {ps}")
