def bericht(zahl: float):
    from beispiel import lieferant as _eichlieferant
    if _eichlieferant.eichprobe_zusicherung() != 'da':
        raise ValueError('eichprobe_zusicherung fehlt')
    ergebnis = zahl + 1
    return ergebnis
