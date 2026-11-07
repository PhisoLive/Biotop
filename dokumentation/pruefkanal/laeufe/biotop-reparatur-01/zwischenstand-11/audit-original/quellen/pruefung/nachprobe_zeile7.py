"""Nachprobe Tor 2 Zeile 7 (Masterprompt v4, Abschnitt 8): Vertragsprobe mit Kernmaßgewinn — läuft als echte Generation.

Fehler im Werk (durch Ausführung bestätigt, Abschnitt 0 der Ausgabe): `bericht.lagerwert()` summiert `Artikel.grundpreis`
über alle Artikel, obwohl `Artikel.waehrung` je Artikel verschieden sein kann (Katalog kennt EUR/USD/CHF, preise hat
`umrechnen`). Bei einem USD-Artikel zu 100 USD weist der Lagerwert 100,00 aus statt 92,59 EUR. Anhang A Satz 5:
„bericht ist Ausgabe, keine Logik" — bericht darf die Umrechnung nicht selbst nachrechnen; die Zusicherung muss
vom Lieferanten preise kommen. Das ist eine Vertragsänderung an der Grenze bericht → preise:
neue Zusicherung `Katalog.wert(nummer, menge) -> float` (Wert in EUR, Grundpreis × Menge, umgerechnet nach EUR,
auf Cent gerundet), aufgenommen in tests/vertraege/test_vertrag_bericht_preise.py.

Fall 1a (ohne Anpassung des Nachbarn, Vertrag NICHT benannt, Vertragsdatei geändert) → abgelehnt (3.8 Schritt 2:
        Vertragsdatei ohne Benennung).
Fall 1b (ohne Anpassung, Vertrag nicht benannt, Vertragsdatei nicht geändert) → abgelehnt (bericht ruft Katalog.wert,
        das es nicht gibt → Regression je Test).
Fall 2  (Vertrag benannt) → Verhandlung: der Schwarm von preise (Nische sicher) baut `Katalog.wert`; das Paar
        (bericht-Kandidat + preise-Anpassung + neue Vertragsfassung) wird gemeinsam geprüft. Der Kandidat bringt einen
        Immuntest mit explizitem Verweis (F4 Norm-Regel) auf den neuen Vertragstest und auf Anhang A Satz 5: an der
        Vorgeneration fällt er (100,00 statt 92,59), am Paar besteht er → Kernmaß +1 → Generalprobe → Schnappschuss →
        Freigabe (Vollmacht) → im Werk.

Aufruf: nachprobe_zeile7.py <lauf_id> <ausgaben-dir> vorbereiten   → schreibt 10-nachprobe-z7-kandidaten.json
        danach: python3 -m biotop generation <lauf> --einschleusen <json einzelner Fall>
"""
import difflib, json, sys
from pathlib import Path
sys.path.insert(0, "/root/biotop")
from biotop.kern.datenbank import verbinden
from biotop.kern import protokoll
from biotop.organe import kammer
from biotop import lauf as L

LAUF = int(sys.argv[1]); A = Path(sys.argv[2])
con = verbinden()
lauf = L._lauf(con, LAUF); werk = L._werk(con, lauf["werk_id"]); pfad = Path(werk["pfad"])
out = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)
def lies(rel): return (pfad / rel).read_text() if (pfad / rel).exists() else ""
def voll_diff(rel, neu):
    return "".join(difflib.unified_diff(lies(rel).splitlines(keepends=True), neu.splitlines(keepends=True), fromfile="a/" + rel, tofile="b/" + rel, n=3))

p("# Nachprobe Tor 2 Zeile 7 (v4) — Vorbereitung: Vertragsänderung bericht→preise, die eine Fehlerbehebung ermöglicht")
p("Zeit:", protokoll.jetzt(), f"| Lauf {LAUF} | Basis Generation {L.letzte_angenommene(con, LAUF)['nummer']} | Werk {pfad}")

# 0. Fehler an der Basis, in der Kammer ausgeführt
probe = ("import sys; sys.path.insert(0,'/werk')\n"
         "from lagerhaus.preise import Artikel, Katalog, umrechnen\nfrom lagerhaus.lager import Lager\nfrom lagerhaus.bericht import lagerwert, textbericht\n"
         "k=Katalog(); k.aufnehmen(Artikel('E','e',100.0)); k.aufnehmen(Artikel('U','u',100.0, waehrung='USD'))\n"
         "l=Lager(); l.zugang('E',1); l.zugang('U',1)\n"
         "w=lagerwert(l,k)\nprint('lagerwert:', w.gesamt, w.je_artikel, '| 100 USD in EUR laut preise.umrechnen:', umrechnen(100.0,'USD','EUR'), '| erwartet gesamt:', 100.0+umrechnen(100.0,'USD','EUR'))\n"
         "print(textbericht(l,k))\n")
e = kammer.ausfuehren(pfad, ["python", "_probe.py"], zeitlimit_s=60, dateien={"_probe.py": probe})
p("\n0. Fehler an der Basis (Kammer, rc=%d):\n   " % e.rc + e.stdout.strip().replace("\n", "\n   "))

# 1. Kandidat bericht: lagerwert nutzt Katalog.wert (EUR) statt grundpreis × menge
alt = lies("lagerhaus/bericht/auswertung.py")
alt_block = '''        wert = runde_cent(katalog.holen(nummer).grundpreis * menge)
        je_artikel[nummer] = wert'''
neu_block = '''        # Vertrag test_vertrag_bericht_preise::test_katalog_wert_in_eur: preise liefert den Wert in EUR (Anhang A Satz 5)
        wert = katalog.wert(nummer, menge)
        je_artikel[nummer] = wert'''
assert alt_block in alt, "Anker in bericht/auswertung.py nicht gefunden"
neu = alt.replace(alt_block, neu_block)
neu = neu.replace('''    """Bewertet den Bestand zum Grundpreis des Katalogs.

    Artikel ohne Katalogeintrag zählen 0 und erscheinen in `fehlende`.
    """''', '''    """Bewertet den Bestand in EUR über `Katalog.wert` (Grundpreis × Menge, in EUR umgerechnet).

    Artikel ohne Katalogeintrag zählen 0 und erscheinen in `fehlende`.
    """''')
diff_bericht = voll_diff("lagerhaus/bericht/auswertung.py", neu)

# 2. Neue Vertragsfassung bericht→preise (Zusicherung Katalog.wert)
vt_alt = lies("tests/vertraege/test_vertrag_bericht_preise.py")
vt_neu = vt_alt.replace("Zusicherungen: preis_fuer ≥ 0 auf Cent gerundet;", "Zusicherungen: Katalog.wert(nummer, menge) = Grundpreis × Menge in EUR (umgerechnet, Cent-gerundet); preis_fuer ≥ 0 auf Cent gerundet;") + '''

def test_katalog_wert_in_eur():
    """Vertragsänderung (Anhang A Satz 4/5): bericht rechnet nicht selbst um; preise liefert Katalog.wert(nummer, menge)
    in EUR — Grundpreis × Menge, mit umrechnen(waehrung → EUR), auf Cent gerundet."""
    k = Katalog(); k.aufnehmen(Artikel("E", "e", 100.0)); k.aufnehmen(Artikel("U", "u", 100.0, waehrung="USD"))
    assert k.wert("E", 2) == 200.0
    assert k.wert("U", 1) == runde_cent(100.0 / 1.08)
    with pytest.raises(UnbekannterArtikel):
        k.wert("nix", 1)
'''
diff_vertrag = voll_diff("tests/vertraege/test_vertrag_bericht_preise.py", vt_neu)

# 3. Immuntest des Kandidaten (fällt an der Basis: 100.00 statt 92.59; expliziter Verweis nach F4)
test_neu = '''"""Immuntest zur Vertragsänderung test_vertrag_bericht_preise::test_katalog_wert_in_eur (Anhang A Satz 5)."""
from lagerhaus.bericht import lagerwert
from lagerhaus.lager import Lager
from lagerhaus.preise import Artikel, Katalog, runde_cent


def test_lagerwert_rechnet_fremdwaehrung_um_test_vertrag_bericht_preise():
    """Vertrag test_vertrag_bericht_preise::test_katalog_wert_in_eur, Anhang A Satz 5: Der Lagerwert eines
    USD-Artikels wird in EUR ausgewiesen (Vorgeneration: 100,00 statt 92,59 — bericht summierte Fremdwährung ungerechnet)."""
    k = Katalog(); k.aufnehmen(Artikel("E", "e", 100.0)); k.aufnehmen(Artikel("U", "u", 100.0, waehrung="USD"))
    l = Lager(); l.zugang("E", 1); l.zugang("U", 1)
    w = lagerwert(l, k)
    assert w.je_artikel["U"] == runde_cent(100.0 / 1.08)
    assert w.gesamt == runde_cent(100.0 + runde_cent(100.0 / 1.08))
'''
diff_test = voll_diff("tests/test_bericht_immun_lagerwert_waehrung.py", test_neu)

begr = ("Behebt: lagerwert summiert Fremdwährungs-Grundpreise ungerechnet (Ausführung: 100 USD → 100,00 statt 92,59 EUR). "
        "Nach Anhang A Satz 5 rechnet bericht nicht selbst um; preise liefert Katalog.wert(nummer, menge) in EUR — neue Zusicherung im Vertrag bericht→preise.")
vertraege_txt = ("tests/vertraege/test_vertrag_bericht_preise.py — neue Zusicherung test_katalog_wert_in_eur: Katalog.wert(nummer, menge) -> float in EUR "
                 "(Grundpreis × Menge, umrechnen(waehrung, 'EUR'), Cent-gerundet; UnbekannterArtikel bei unbekannter Nummer). Der Nachbar preise (Lieferant) muss die Methode bereitstellen.")
faelle = {
    "1a": [{"bereich": "bericht", "diff": diff_bericht + diff_test + diff_vertrag, "begruendung": begr + " [Fall 1a: Vertragsdatei geändert, Vertrag NICHT benannt]", "vertraege": "keine", "probe": "nachprobe-z7-1a-ohne-nachbar-unbenannt"}],
    "1b": [{"bereich": "bericht", "diff": diff_bericht + diff_test, "begruendung": begr + " [Fall 1b: ohne Vertragsänderung, ohne Nachbar]", "vertraege": "keine", "probe": "nachprobe-z7-1b-ohne-nachbar"}],
    "2":  [{"bereich": "bericht", "diff": diff_bericht + diff_test + diff_vertrag, "begruendung": begr + " [Fall 2: Vertrag benannt → Verhandlung mit preise]", "vertraege": vertraege_txt, "probe": "nachprobe-z7-2-mit-nachbar"}],
}
for k, v in faelle.items():
    (A / f"10-nachprobe-z7-fall{k}.json").write_text(json.dumps(v, ensure_ascii=False, indent=1))
p("\nKandidat bericht: Diff auswertung.py %d Zeilen; neuer Immuntest %d Zeilen; neue Vertragsfassung %d Zeilen (nur Fall 1a/2)" % (len(diff_bericht.splitlines()), len(diff_test.splitlines()), len(diff_vertrag.splitlines())))
p("Diff auswertung.py (±):\n   " + "\n   ".join(l for l in diff_bericht.splitlines() if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))))
p("Vertragsänderung (±):\n   " + "\n   ".join(l for l in diff_vertrag.splitlines() if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))))
(A / "10-nachprobe-z7-vorbereitung.txt").write_text("\n".join(out) + "\n")
