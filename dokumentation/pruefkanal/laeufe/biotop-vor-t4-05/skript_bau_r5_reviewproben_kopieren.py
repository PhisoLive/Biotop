"""Legt die Review-Proben des geltenden (zweiten) Durchgangs der Runde 5 nach biotop-vor-t4-05/review-proben/ und die
Proben, die nur der verworfene erste Durchgang hatte, nach review-proben/verworfen/. Nur Kopieren."""
import shutil
from pathlib import Path

Q = Path('/tmp/review-vor-t4-05')
Z = Path('/root/biotop-vor-t4-05/review-proben')
GELTEND = ['kammerprobe05.py', 'kammerprobe05.out.txt', 'KAMMERPROBE05.json', 'lokal_b.py', 'lokal_b.out.txt',
           'lokal_ts.mjs', 'lokal_ts.out.txt', 'letzte.py', 'letzte.out.txt', 'n_auswerten.py', 'n_auswerten.out.txt',
           'verdrahtung_lesen.py', 'quellen1.sh', 'quellen2.sh', 'quellen3.sh', 'quellen4.sh', 'quellen5.sh',
           'quellen6.sh', 'belege1.sh', 'belege2.sh', 'belege3.sh', 'umgebung.sh', 'status.sh', 'warte.sh', 'warte2.sh',
           'wer.sh', 'abschluss.sh']
VERWORFEN = ['e2b_probe.py', 'e2b_probe.out.txt', 'bericht_neu.sh']
(Z / 'verworfen').mkdir(parents=True, exist_ok=False)
n = 0
for name in GELTEND:
    shutil.copy2(Q / name, Z / name)
    n += 1
for name in VERWORFEN:
    shutil.copy2(Q / name, Z / 'verworfen' / name)
    n += 1
print('kopiert', n, 'Dateien; fehlend:', [x for x in GELTEND + VERWORFEN if not (Q / x).exists()])
