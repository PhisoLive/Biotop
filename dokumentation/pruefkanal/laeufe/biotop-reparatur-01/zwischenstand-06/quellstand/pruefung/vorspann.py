"""Kompatibler Berichts-Wrapper: vorspann.py <ausgaben-dir> <lauf_id>.

Kein zweiter Eichpfad: delegiert ausschließlich an `biotop vorspann <lauf>`.
"""
import argparse
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
import sys

# Diese Kopie, niemals ein fest verdrahtetes produktives Repository.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from biotop.__main__ import main as biotop_main


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ausgaben', type=Path)
    parser.add_argument('lauf', type=int)
    args = parser.parse_args(argv)
    args.ausgaben.mkdir(parents=True, exist_ok=True)
    out, err = StringIO(), StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        rc = biotop_main(['vorspann', str(args.lauf)])
    (args.ausgaben / f'15-vorspann-lauf{args.lauf}.txt').write_text(out.getvalue() + err.getvalue())
    print(out.getvalue(), end='')
    print(err.getvalue(), end='', file=sys.stderr)
    return rc


if __name__ == '__main__':
    sys.exit(main())
