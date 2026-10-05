# Startplan für Goal #18 — Materialien und Tech-Motive

Auftrag: [Issue #18](https://github.com/KreutzM/Owli-3d/issues/18), Parent #7,
Epic #11. Nach der Integration von #6 ist dies das nächste Produktionsgoal.
AGENTS-Pflichtlektüre in Reihenfolge, danach aktuelle Übergabe und dieses Issue
lesen. Referenzen 00 > 07 > 08 tatsächlich ansehen; bestehende Meilensteine
bewahren und aus einer Kopie weiterarbeiten.

## Geprüfter Einstieg

Szene `blender/scene/owli_feathers_v01.blend`, 1.385.718 Bytes, SHA256
`76ee3f1c0f8b4314aee40585445c14e3b2d193b7aa04c7e2c86e6f810f576b0a`.
Produktionscommit im #6-PR/Git-Verlauf prüfen; neueren main berücksichtigen.
109 Objekte, 95 Meshes, 48 breite Federgruppen, fünf Pivots, vier Kameras,
fünf Lichter. Keine Armature/Actions. Alle Gesichtsfunktionen und 3+1-Griff
wurden auf diesem Stand neu geprüft. [Bericht](../validation/reviews/feathers_v01/report.md).

Die sieben vorhandenen Materialien sind Diagnosefarben, Cornea-Prüfmaterial
und Stangen-Diagnosematerial. Stirnnetz ist noch `BLK_ForeheadNode/Link_*`;
Stange hat keine finalen Cyan-Akzente. `50_materials.py` erstellt nur eine
Bibliothek, weist sie nicht vollständig zu und speichert fest nach `owli.blend`.
Die dortige hex-RGB-Funktion führt noch keine sRGB-Linear-Umrechnung aus.
Dieses Gerüst ist nicht die fertige Materialproduktion.

## Vollständiger Umfang

- Alle sichtbaren Nicht-Augen-Meshes tatsächlich mit passenden Materialien
  versehen: Navy/Blue/Cyan-Federn, Cream-Maske/Brust, Orange-Schnabel/Zehen,
  dunkle Krallen und gebürstete Metallstange.
- Farben korrekt von sRGB nach linear ins Shading überführen; Federn satin/matt
  und nichtmetallisch, Schnabel/Krallen keratinartig mit maßvollem Glanz.
- Zentriertes Cyan-Netzwerksymbol und dezente Stangenakzente als eigene
  bearbeitbare Geometrie liefern. Gesicht und Cream-Maske lesbar halten.
- Parameter in JSON und ausführbaren Skripten; Materialslots/Nodes und alle
  neuen Objekte in echten frischen Blender-Prozessen prüfen.
- Alle vier festen Ansichten sowie Funktions-/Griffproben nach betroffenen
  Geometrieänderungen prüfen. Auge/Cornea nicht stillschweigend umgestalten:
  deren finale Tiefe, Iris-Netzwerk und Lookdev gehören #19.

## Nachweise und sichere Fortsetzung

```powershell
git status --short --branch
python scripts/project.py doctor
python scripts/project.py validate
python scripts/feathers_gate.py
python -m unittest discover -s tests -v
```

Eigener Branch, eigene Szene und eigener Review-Ordner. Mit separaten visuellen
und technischen Sub-Agents prüfen; pro Produktionsdatei einen Schreiber.
Alle alten source-bound Helfer/Belege erhalten. 462 geschützte Vorgängerbytes
und die neue #6-Lieferung für die nächste History-Kette berücksichtigen.
`feathers_gate.py` bleibt zusätzlich zur historischen CLI erforderlich.

Der generische Renderer und Material-/Rig-Gerüste können geladene/feste Dateien
speichern: nur in isolierten Arbeitskopien einsetzen. Neue Produktion muss
explizite eigene Ausgabepfade und echte Materialzuordnung nachweisen. Keine
neuen allgemeinen Konzepte, Flugdetails oder Einzelfeder-Simulation.

Abschluss: eigene LFS-Szene, feste Vieransichten, separate manuelle Entscheidung,
unabhängige Berichte, vollständige eigene Quellen-/Referenz-/Worker-Inventare,
Material-/Tech-Bericht mit Befehlen und Grenzen, Validate/Gates/Tests/Compileall/
Blender-Smoke, eigener grüner PR. Issue erst nach erfüllter Lieferung schließen;
Übergabe und Epic auf #19 aktualisieren. Finales Rig/Animation bleiben #20–#24.

## Lieferung aus diesem Startplan

Der ausgeführte #18-Stand liegt getrennt in `owli_materials_v01.blend`,
SHA256 `ca5522b3948e2d3501eb47c0b0f3099a7ca9d7e596e8e9af5b9f6128353acaa3`, 1.793.740 Bytes.
[Materialbericht](../validation/reviews/materials_v01/report.md) und separate
Abnahme unter `materials_v01/`. Brust-F01 ist integriert; F02-Nasenlöcher
bleibt #40, F03-Augen bleibt #19. Nächster [Startplan #19](next-goal-19.md);
Integration/CI und Issue-Abschluss anhand des #18-PR prüfen.
