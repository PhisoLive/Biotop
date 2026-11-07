# Unveränderte Originalnamen wiederherstellen

Punktdateien lieferten bei der HTTPS-Abholung404. Deshalb liegen ihre unveränderten Bytes unter expliziten PUNKTDATEI-Aliasnamen und zusätzlich mit den Originalnamen im PUNKTDATEIEN.tar.gz. DOWNLOAD-ZUORDNUNG.json bindet Originalpfad, abholbaren Alias und SHA256. Keine Quelldatei wurde inhaltlich verändert.

Für einen lokalen Originalbaum: im heruntergeladenen Ordner `tar -xzf PUNKTDATEIEN.tar.gz` ausführen. Danach sind die Originalpfade wieder vorhanden; auch audit-original/SHA256SUMS kann dann unverändert geprüft werden. Das äußere Manifest bindet weiterhin die Aliasdateien und das Archiv.
