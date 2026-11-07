# Bestätigte Reviewbefunde

6 Befund-IDs, 5 zusammengeführte Fehlermechanismen. Beide Wirkungskreiswege bleiben eigene Prüffälle; die Zusammenführung löscht keinen Befund.

## EICH-1 — Rauschgesperrter Bereich lässt sich durch einen anders deklarierten Kandidaten verändern
Mechanismusgruppe: tatsaechlicher_wirkungskreis.
Status: am Elterncode bestätigt, Nachbesserung delegiert, noch nicht integriert oder abgenommen.

## EICH-2 — Fehlgeschlagene Generation 0 erfüllt die neue Maß-Vorbedingung
Mechanismusgruppe: gen0_erfolg.
Status: am Elterncode bestätigt, Nachbesserung delegiert, noch nicht integriert oder abgenommen.

## EICH-3 — Eichvertrag kann nach dem Vorspann ohne Invalidierung ausgetauscht werden
Mechanismusgruppe: eichgegenstand_bindung.
Status: am Elterncode bestätigt, Nachbesserung delegiert, noch nicht integriert oder abgenommen.

## EICH-4 — Vertragsgegenprobe kann an ihrem eigenen kopierten Test scheitern und trotzdem als gültig falsch zählen
Mechanismusgruppe: vertrag_zeugengueltigkeit.
Status: am Elterncode bestätigt, Nachbesserung delegiert, noch nicht integriert oder abgenommen.

## MASS-01 — Die neue Rauschsperre übersieht den Wirkungskreis verhandelter Anpassungen
Mechanismusgruppe: tatsaechlicher_wirkungskreis.
Status: am Elterncode bestätigt, Nachbesserung delegiert, noch nicht integriert oder abgenommen.

## MASS-02 — Neue Wertevalidierung bricht die gesamte Rauschkalibrierung statt nur des ungültigen Bereichs ab
Mechanismusgruppe: rauschfehler_bereichsweise.
Status: am Elterncode bestätigt, Nachbesserung delegiert, noch nicht integriert oder abgenommen.

## Elternausführung
7 von 16 Zusatztests fehlgeschlagen; 9 von 16 bestanden; keine Collection-/Setup-Errors und keine Skips. Jeder Name und Assertiontext steht in ELTERN-REPRODUKTION.json.
- 43-review-eichung-eltern-rot: 4 von 11 fehlgeschlagen, Exit 1.
- 44-review-mass-eltern-rot: 3 von 5 fehlgeschlagen, Exit 1.

## Grenzen und Empfehlungen
Die ursprünglichen Reviewer-Suiten und Eltern-Repros sind unterschiedliche Ausführungen derselben bzw. ergänzender Fälle. Ihre Zahlen werden nicht addiert und nicht als echte Kammerabnahme dargestellt. Die drei früheren Kern-Gegenmutanten, acht Maßreview-Mutanten und vier Eichpaare bleiben jeweils eigene Nachweisgruppen.
Die nicht blockierenden Empfehlungen EICH-S1/S2/S3 (strengere Qualitätsstruktur, weitere Normgegenklasse, vollständiger Vorspann-Rohbeleg) bleiben sichtbar in REVIEW.json, ohne aus ihnen ungemessene zusätzliche native Umgehungen zu behaupten. MASS-S1/S2 sind Regressionstests zu den bereits gezählten MASS-Befunden und im Fixauftrag enthalten.
