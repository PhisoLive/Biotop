# Referenzlast für das Werk „lagerhaus" — Teil des Messgeräts (Kern).
# Je Bereich eine Funktion last_<bereich>(), die eine feste Arbeit ausführt.
# Wird in der Kammer ausgeführt; Ergebnis ist die Laufzeit in ms (min aus 3).

import sys
sys.path.insert(0, "/werk")


def last_formeln():
    from lagerhaus.formeln import auswerten
    for i in range(3000):
        auswerten("min(summe * 0.05, 20) + max(menge, 3)", i % 50, 9.99, float(i))


def last_preise():
    from lagerhaus.preise import Artikel, Katalog, Rabattregel, Staffel, rabatt_anwenden
    k = Katalog()
    for i in range(200):
        k.aufnehmen(Artikel(f"A{i}", "x", 1.0 + i, [Staffel(10, 0.9), Staffel(100, 0.8)]))
    regeln = [Rabattregel("a", "summe >= 100", "summe * 0.05"), Rabattregel("b", "menge >= 50", "10")]
    for i in range(2000):
        s = k.preis_fuer(f"A{i % 200}", 1 + i % 150)
        rabatt_anwenden(s, regeln, 1 + i % 150, s)


def last_lager():
    from lagerhaus.lager import Lager
    l = Lager()
    for i in range(1500):
        l.zugang(f"A{i % 20}", 3)
        if i % 3 == 0:
            l.entnehmen(f"A{i % 20}", 1)
        l.verfuegbar(f"A{i % 20}")
    l.inventur()


def last_bericht():
    from lagerhaus.bericht import textbericht, bewegungsbericht
    from lagerhaus.lager import Lager
    from lagerhaus.preise import Artikel, Katalog
    k = Katalog(); l = Lager()
    for i in range(30):
        k.aufnehmen(Artikel(f"A{i}", "x", 1.5))
        l.zugang(f"A{i}", 10 + i)
    for _ in range(60):
        textbericht(l, k)
        bewegungsbericht(l.journal)


def beobachten():
    """F4 3.5 (Äquivalenz-Beleg): beobachtbare Ausgaben des Werks auf einem festen Eingaberaster — jede Zeile ein
    Wert. Gleiche Prüfsumme dieser Folge bei Original und Mutant = verhaltensgleich auf dem Raster."""
    from lagerhaus.formeln import auswerten, pruefen, FormelFehler
    from lagerhaus.formeln.auswertung import formel_beschreibung
    from lagerhaus.preise import Artikel, Katalog, Rabattregel, Staffel, rabatt_anwenden, rabatt_betrag, runde_cent, umrechnen
    from lagerhaus.lager import Lager, NichtGenugBestand
    from lagerhaus.bericht import textbericht, bewegungsbericht, lagerwert
    out = []
    for f in ("summe * 0.05", "menge >= 10", "min(summe, 20)", "max(menge, 7)", "abs(0 - 3)", "summe / 0", "rabatt * 2", "", "1 +", "round(summe * 0.333, 1)", "menge > 0 and summe < 5"):
        for menge, preis, summe in ((0, 0.0, 0.0), (1, 1.0, 1.0), (9, 9.99, 89.91), (10, 9.99, 99.9), (11, 2.5, 27.5), (100, 0.5, 50.0)):
            try:
                out.append(("auswerten", f, menge, preis, summe, auswerten(f, menge, preis, summe)))
            except FormelFehler as e:
                out.append(("auswerten", f, "FormelFehler", str(e)[:40]))
            except Exception as e:
                out.append(("auswerten", f, type(e).__name__))
        out.append(("pruefen", f, pruefen(f))); out.append(("beschreibung", formel_beschreibung(f)))
    for b in (0.0, 0.005, 0.015, 1.005, 2.675, 2.5, -1.235, 99.995, 1234.5678):
        out.append(("runde", b, runde_cent(b)))
        for von, nach in (("EUR", "EUR"), ("EUR", "USD"), ("USD", "EUR"), ("EUR", "CHF"), ("CHF", "EUR"), ("EUR", "GBP")):
            try:
                out.append(("umrechnen", b, von, nach, umrechnen(b, von, nach)))
            except Exception as e:
                out.append(("umrechnen", b, von, nach, type(e).__name__))
    k = Katalog()
    for i, (gp, st) in enumerate(((1.0, [Staffel(10, 0.9), Staffel(100, 0.8)]), (0.333, []), (5.0, [Staffel(1, 4.0)]), (2.0, [Staffel(50, 1.0), Staffel(20, 1.5)]))):
        k.aufnehmen(Artikel(f"A{i}", "x", gp, st))
    for i in range(4):
        for menge in (1, 9, 10, 11, 19, 20, 21, 49, 50, 51, 99, 100, 101, 1000):
            out.append(("preis_fuer", i, menge, k.preis_fuer(f"A{i}", menge)))
        for menge in (0, -1):
            try:
                out.append(("preis_fuer", i, menge, k.preis_fuer(f"A{i}", menge)))
            except Exception as e:
                out.append(("preis_fuer", i, menge, type(e).__name__))
    out.append(("alle", [a.nummer for a in k.alle()], k.anzahl(), k.enthaelt("A1"), k.enthaelt("Z")))
    regeln = [Rabattregel("a", "summe >= 100", "summe * 0.05"), Rabattregel("b", "menge >= 50", "10"), Rabattregel("c", "summe > 0", "summe * 3"), Rabattregel("d", "summe > 0", "0 - 5"), Rabattregel("e", "menge >= 10", "summe"),
              Rabattregel("f", "menge >= 0", "1 / summe")]  # Regel nach Nullstellung: teilt durch summe (Rest 0 → FormelFehler, falls die Kette weiterläuft)
    for summe in (0.0, 0.01, 9.99, 10.0, 99.99, 100.0, 100.01, 250.0, 1e6):
        for menge in (1, 9, 10, 49, 50, 51):
            for r in regeln:
                try:
                    out.append(("rabatt_betrag", r.name, summe, menge, rabatt_betrag(r, summe, menge, 1.0)))
                except FormelFehler as e:
                    out.append(("rabatt_betrag", r.name, summe, menge, "FormelFehler", str(e)[:40]))
            for rs in (regeln[:2], regeln[2:3], regeln[3:4], regeln[4:5], regeln[:5], [regeln[2], regeln[5]], [regeln[4], regeln[5]]):
                try:
                    out.append(("rabatt_anwenden", [r.name for r in rs], summe, menge, rabatt_anwenden(summe, rs, menge, 1.0)))
                except FormelFehler as e:
                    out.append(("rabatt_anwenden", [r.name for r in rs], summe, menge, "FormelFehler", str(e)[:40]))
    l = Lager()
    schritte = [("zugang", "A", 10), ("zugang", "B", 5), ("reservieren", "A", 4), ("entnehmen", "A", 6), ("entnehmen", "A", 1), ("reservierung_einloesen", "A", 4),
                ("reservierung_einloesen", "A", 1), ("freigeben", "A", 1), ("zugang", "A", 0), ("zugang", "A", -1), ("entnehmen", "B", 5), ("entnehmen", "B", 1),
                ("reservieren", "B", 1), ("zugang", "C", 1), ("reservieren", "C", 1), ("reservierung_einloesen", "C", 1), ("zugang", "A", 3), ("reservieren", "A", 3), ("entnehmen", "A", 1),
                ("reservierung_einloesen", "A", 5), ("freigeben", "A", 4),
                ("zugang", "D", 5), ("reservieren", "D", 2), ("freigeben", "D", 3), ("freigeben", "D", 2), ("freigeben", "D", 1),  # Freigabe um genau 1 zu viel
                ("zugang", "E", 5), ("reservieren", "E", 2), ("freigeben", "E", 2), ("freigeben", "E", 1), ("reservieren", "E", 5), ("reservieren", "E", 6),
                ("entnehmen", "E", 0), ("reservieren", "E", 0), ("freigeben", "E", 0), ("reservierung_einloesen", "E", 0)]
    for op, a, n in schritte:
        try:
            out.append((op, a, n, getattr(l, op)(a, n)))
        except (ValueError, NichtGenugBestand) as e:
            out.append((op, a, n, type(e).__name__))
        out.append(("zustand", a, l.bestand(a), l.reserviert(a), l.verfuegbar(a)))
    out.append(("artikel", l.artikel(), l.inventur(), l.gesamtmenge(), l.journal.anzahl(), [(b.nummer, b.artikel, b.menge) for b in l.journal.alle()]))
    k2 = Katalog(); k2.aufnehmen(Artikel("A", "a", 1.5)); k2.aufnehmen(Artikel("C", "c", 2.0))
    out.append(("lagerwert", lagerwert(l, k2))); out.append(("bewegungen", bewegungsbericht(l.journal))); out.append(("text", textbericht(l, k2)))
    out.append(("bewegungen_leer", bewegungsbericht(Lager().journal)))
    return out
