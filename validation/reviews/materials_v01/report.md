# Goal #18 — Nicht-Augen-Materialien, Tech und Brustkorrektur F-01

Gelieferte Szene: `blender/scene/owli_materials_v01.blend`, 1,793,740 Bytes,
SHA256 `ca5522b3948e2d3501eb47c0b0f3099a7ca9d7e596e8e9af5b9f6128353acaa3`. Branch `feat/18-materials-lookdev`,
[Auftrag #18](https://github.com/KreutzM/Owli-3d/issues/18), Parent #7/Epic #11.
Vorgänger #6/PR #39: Git `a8634936494512d64e311149f20ed4e24ea492ac`,
Blend SHA `76ee3f1c0f8b4314aee40585445c14e3b2d193b7aa04c7e2c86e6f810f576b0a`.
Die Abnahme gilt für #18; eine vollständige Avatarfreigabe steht noch aus.

## Ergebnis

Alle 95 sichtbaren Nicht-Augen-Meshes besitzen tatsächlich passende Slots;
kein sichtbares Polygon ist unzugewiesen. Zehn eigene Shader liefern matte/
satinierte Navy/Blue/Cyan/Cream-Federn, integrierte warme Brustverläufe,
orange/dunkles Keratin, matte Mundinnenfläche, gebürstetes Metall und Cyan-Emission.
IEC-sRGB→linear wird vor der Zuweisung angewendet. Die ursprüngliche
`design/materials.json` bleibt bytegenau erhalten; Lookdev-Parameter stehen in
`design/materials_lookdev.json`. Nodes und Feinrauschen sind bearbeitbar.
Roughness: Federn .56, Cream .64, Keratin/Metall .30; nur die Stange ist
metallisch (.85, Anisotropic .65). Cyan-Emission 2.0. Die gespeicherte Szene
enthält 14 Materialien: zehn eigene und vier unveränderte Augendiagnosematerialien.
Der wiederholte Build hält zusätzlich drei unbenutzte Vorgängermaterialien;
Blender lässt diese beim erneuten Öffnen weg.

F-01 aus [#40](https://github.com/KreutzM/Owli-3d/issues/40) ist im Umfang von
#18 erledigt: sechs Cream-Gruppen bilden eine breitere, nach unten verjüngte
Brustmitte; zwei warme Gruppen verlaufen mit nach außen versetztem Ansatz und
nach innen gerichteter Spitze diagonal. Orange/Gold bleibt lokal und geht in
Cream/Blue über. Orange-Root (.069,.337), Tip (.023,.247), Half-width .016 m.
Front/3Q zeigen keine homogenen Kragen-/Gürtelflächen mehr. Die Vergleichstafel
`chest_before_after.png` zeigt gleiche Bildausschnitte vor/nachher mit 00/08.
Die wenigen breiten, teilweise geschuppten Gruppen bleiben eine bewusst grobe
Geometriestrategie; sie reproduzieren keine dichte illustrierte Einzelfederung.

Neun alte Stirn-Guides wurden durch sieben sitzende Knoten und sechs Linien
ersetzt. Vier schmale, bearbeitbare Stangenringe ergänzen zurückhaltende Cyan-
Akzente. Hub: Radius 4.8 mm, Tiefe 3 mm, Höhe 470 mm; Terminals 1.8 mm;
Linienradius .55 mm, Ringstärke .5–.6 mm. Der zentrale Knoten ist frontal lesbar;
Stirnkrümmung verkürzt das Motiv in Profil/3Q. Diese Grenze ist dokumentiert,
Kameras bleiben fest. Die optionale Entfernung des Basisrings wurde bewertet;
der kleine Akzent bleibt visuell untergeordnet. Tech ist noch nicht final geriggt.

## Referenzen, Erhaltung und tatsächliche Prüfung

Feste Front/Links/Rücken/3Q wurden tatsächlich gegen 00 > 07 > 08 und
unterstützende Beauty-Ansichten geprüft. 00 bestimmt Marke/Cream/Farbidentität,
07 die erhaltenen Volumen, 08 die Material-/Brust-/Tech-Details. Keine neue
Konzeptkunst, Fluggeometrie oder undokumentierte Anatomie.

Genau 78 bestehende Cages stimmen mit unabhängigen Vorgängerdigests überein:
Matrix, Parent, Vertices/Edges/Faces, Smoothing, Gruppen/Gewichte, Modifier und
Collections. Nur acht F-01-Cages ändern sich; neun Guides entfallen, 17 TECH-
Meshes kommen hinzu. Alle acht Augen behalten Cage, Slots, Polygonindizes und
vollständige zugewiesene Nodegraphs. Fünf Pivots, vier Kameras, fünf Lichter,
World und Renderkonfiguration bleiben unverändert.

Vier tatsächliche Blender-5.2.1-Worker prüfen Build/Wiederholung/Speichern und
frisches Öffnen. Die kompletten kanonischen Laufzeitdaten stimmen überein;
die vier 1024-RGBA-Pixelpuffer sind zwischen saved_build/reload_a/reload_b exakt
gleich. Live-Eevee-Bilder bleiben separat, da Cache-Unterschiede möglich sind.
Die Szene hat 117 Objekte/103 Meshes, keine Armature/Actions.

Alle 51 FTH- und 17 TECH-Flächen bestehen Cage-/evaluierte Triangle-Prüfungen
mit adjazenten und coplanaren Innenflächen. Torusringe haben Euler 0, sonstige
Tech-Flächen Euler 2. Fünf Tech-Paare sind exakt gespiegelt. Größter gemessener
Stirn-Surface-Abstand: 3.19999 mm am sitzenden Hub. Alle 48 Federwurzelproben
bestehen. Die alten Schulter-BVH-Messwerte unterscheiden sich bei identischen
Cages um rund 19 nm; der Vergleich toleriert 2e-7 m Messabweichung. Alle neuen
Worker-Datensätze bleiben untereinander exakt gleich.

Tatsächliche 41 Blink-, 41 Schnabelzustände, ±12° Gaze, sechs Halb-/Vollgesten
und Neutral-Rückkehr bestehen. Alle 51 FTH und alle 17 TECH sind explizite
Kollisionsziele; TECH: 2,788 Lid-, 1,394 Schnabelpaare, 136 Paare je Blickprobe,
238 je Gestenzustand. Unveränderte 45 unabhängige Fußpaare, acht Krallen-/Bar-
Kontakte und exakt 3+1 Zehen/Krallen je Fuß bestehen ebenfalls.

Der unabhängige technische Reviewer öffnet/probt selbst und ergänzt UV-Prüfung,
1,530 neutrale Feder-Fuß/Tech-Paare und fünf weitere Viertel-/Mischgesten.
Der visuelle Reviewer rendert selbst vier Ansichten, prüft exakte kanonische
RGBA-Gleichheit und die tatsächlichen Endposen. Separate Berichte/Maschinenbelege
sind an die endgültige Szene, Quellen und Bilder gebunden.

V18-01 (vertikale warme Zierstreifen) und V18-02 (flacher/verdeckter Hub)
wurden in Preview01 gefunden und durch Kontur/Gradient sowie Sitz/Domform
behoben. Eine echte Symmetrieprobe verwarf 11 µm Linienabweichung; exakte
Rechts→Links-Spiegelung korrigierte die Geometrie ohne lockerere Toleranz.
G18-TECH-01 war eine Prüflücke für widersprüchliche einzelne Blink-Abstände:
jetzt müssen alle 164 Werte sicher sein und dem globalen Minimum entsprechen;
gezielte Negativtests belegen die Korrektur. Keine offenen #18-Blocker.

548 tatsächliche Vorgänger-Git/LFS-Hashes, 68 Quellen und neun Referenzen sind
gebunden. Der ursprüngliche Stage50 ist bytegenau archiviert; alte Szenen,
Bilder und Approvals wurden weder neu erzeugt noch auf neue Quellen umgeschrieben.
Der strenge Gate prüft komplette typisierte Inventare, Graph-Fingerprints,
echte Worker-JSONs/Logs/Pixels/Slots/Probeanzahl und die separate `review.json`.

## Reproduktion und Grenzen

```powershell
python scripts/materials_review.py --work tmp/goal18/new_unique_run --output validation/reviews/materials_v01 --scene-output blender/scene/owli_materials_v01.blend
python scripts/project.py doctor
python scripts/project.py validate
python scripts/feathers_gate.py
python scripts/materials_gate.py
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/project.py smoke
```

Alle 83 Python-Tests, Material-Gate, Doctor/Strictvalidate/Compileall und der
vollständige isolierte Blender-Smoke bestehen. Windows/Ubuntu-CI wird im PR
vor Integration geprüft. Der Hauptagent ergänzt sechs tatsächliche Artefakt-
Manipulationen in einer isolierten Kopie: neu gebundene falsche kanonische Pixel,
Worker-Drift, widersprüchliche Blink-Abstände, fehlender Completion-Log, geänderte
historische Palette und fehlendes manuelles F-01-Kriterium werden verworfen.
Historische Produktionsbytes bleiben nach diesen ergänzenden Checks unverändert.
Producer benötigt einen neuen Scratchpfad und überschreibt nur seinen eigenen
benannten Meilenstein. Zum Prüfen bestehender Lieferungen die read-only Gates
nutzen. Stage50 speichert im Gerüst-Smoke scratch-relativ nach `owli.blend`;
alte vollständige Verifier erwarten teils ersetzte Guides. Nicht-Augen-UVs
ändern keine erhaltenen Cages. Triangle-Toleranzen begrenzen sehr kleine Details;
Federwurzel-/Ring-Sitz und Nachbarüberlappung sind beabsichtigte Befestigungen,
keine Druckphysik. Gesamte Topologie/Rig/Animation bleiben #20–#24.

**F-02 Nasenlöcher bleibt #40, F-03 Augen bleibt #19.** Die Diagnoseaugen sind
noch keine finale Referenztreue. #40 bleibt bis zur gemeinsamen Erledigung aller
drei Findings offen; Nasenlöcher müssen vor #20 umgesetzt werden.
