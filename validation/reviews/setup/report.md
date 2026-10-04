# Owli — technischer Studio-Review (refresh für Issue #14)

Datum: 2026-10-03. Blender 5.2.1 LTS. Der feste Studio-Aufbau aus #12 bleibt
unverändert; die Testgeometrie wurde für #14 mit den aktuellen groben Formen
ersetzt und neutral grau gerendert. Keine Silhouetten- oder Materialfreigabe.

46 Geometrieobjekte, 4 Kameras, 5 Lichter: 55 Szenenobjekte. Vier 1024px-Ansichten,
minimale konservative Bildrandabstände Front 2,697%, Links 2,393%, Rücken 2,794%, 3/4 17,384%.
Kamerapositionen, Targets, 0,58-m-Orthoscale, 65-mm-Linse und Studio-Lichter bleiben
fest. Alle Objekte halten den 2%-Rahmen und die Clip-Distanzen ein. Absichtlich
verschobene Geometrie und ungültige Far-Clip-Distanz werden abgewiesen.

Wiederholte Geometrie-/Studio-Aufbauten erhalten Digest und Objekt-/Datablockzahlen.
Speichern und erneutes Öffnen in einem frischen Blender-Prozess erhalten Studio,
Geometrie und alle vier Bilder pixelgenau. Eigene Tests prüfen separate kugelförmige
Augen, Masken-/Büschelvolumen und 3+1-Griffguides einschließlich hinterer Lage,
Griff unter die Stangenmitte und Abstand zum Metall. Parameterprobes prüfen
Augenabstand/-tiefe, Schnabel, Flügel, Schwanz und globale Skalierung; der Basisstand
wird vor dem Rendering wiederhergestellt. Debug-Materialslots sind für diese
neutrale Testszene geleert.

| Ansicht | Original / Referenzvergleich | Sichtbare grobe Formen |
|---|---|---|
| Front | [Original](VAL_FRONT.png) / [Board](VAL_FRONT_comparison.png) | Kopf, Augen, Maske/Brow/Büschel, Flügel, Schnabel, je drei Frontzehen |
| Linksprofil | [Original](VAL_LEFT.png) / [Board](VAL_LEFT_comparison.png) | Kopf-/Augentiefe, Schnabel, Flügel, Schwanz und vorderer/hinterer Griff |
| Rücken | [Original](VAL_BACK.png) / [Board](VAL_BACK_comparison.png) | Symmetrische Flügel/Büschel, mittiger Schwanz und Rearguides |
| 3/4 vorne | [Original](VAL_3Q.png) / [Board](VAL_3Q_comparison.png) | Gesicht und räumliche Sitzhaltung; technisches Panel und Beauty unterstützen unterschiedliche Aufgaben |

[Übersicht](contact_sheet.png), [Manifest](render_manifest.json),
[Verifikation](verification.json),
[gespeicherter LFS-Blend](../../../blender/scene/owli_validation_setup.blend).
Quell-/Design-/Referenzhashes sowie Blend-/Bildhashes sind dokumentiert.
Reproduktion: `python scripts/project.py setup-review`; ergänzend `validate`,
`python -m unittest discover -s tests -v`, `python -m compileall -q scripts` und
`python scripts/project.py smoke`. Produktionsdatei `owli.blend` wird nicht erzeugt
oder überschrieben.

Referenzhierarchie bleibt Logo 00 (1), Turnaround 07 (2), Parts 08 (3), Beauty (4).
Die technische 3/4-Referenz zeigt die andere laterale Seite; kein Spiegeln oder
metrisches Overlay. Die schriftliche 3+1-Anatomie und Stirnplatzierung gewinnen
gegen uneindeutige Zeichnungen. Die graue Testszene belegt Studio/Geometrie,
der [separate farbige Blockout-Review](../blockout_v01/report.md) dokumentiert
Gesichts-/Farblektüre und grobe Modellgrenzen. Der grobe Freeze aus #14 steht in design/silhouette_freeze.json; dieser technische Bericht vergibt keine eigene visuelle Freigabe.
Blender-Factory-Brush-Pfadwarnungen betreffen ungenutzte Assets. Pixelidentität gilt
innerhalb derselben Blender-/Renderumgebung.
