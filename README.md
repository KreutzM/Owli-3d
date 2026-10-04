# Owli 3D

Produktions-Repository für **Owli**, die kleine Tech-Eule und das Brand-/Mascottchen von Owli-AI.

Ziel ist ein sauber modellierter, riggbarer und später animierbarer 3D-Avatar in Blender. Die erste Version sitzt auf einer Stange; Fliegen ist ausdrücklich **nicht** Teil von V1.

## Produktionsprinzip

- Original-Logo = Markenidentität.
- Finales technisches Turnaround = primäre Form-/Silhouettenreferenz.
- Finales Parts-/Lookdev-Sheet = primäre Detail-/Materialreferenz.
- Beauty-Views = Stil, Charakter und Look.
- Frühere Concept-Sheets dürfen finale technische Sheets nicht überstimmen.
- 3D-Entscheidungen werden dokumentiert; neue Konzeptbilder nur bei echten offenen Designfragen.

## Start für GPT-6.1-Sol

1. `AGENTS.md` lesen.
2. Die Pflichtlektüre in der Reihenfolge aus `AGENTS.md` lesen, beginnend mit `DESIGN_FREEZE.md`.
3. `python scripts/project.py doctor` ausführen.
4. `python scripts/project.py smoke` ausführen.
5. Erst Blockout, dann Silhouette-Review, dann Federn/Materialien, dann Rig.

## Kernreferenzen

Die freigegebenen Referenzen sind in `references/manifest.json` mit Dateiname, Abmessungen und SHA-256 fixiert.
Die eigentlichen PNG-Dateien sollen unter `references/approved/` liegen.

## Ziel für V1

- sitzende Owli auf moderner Tech-Stange;
- klare Wiedererkennbarkeit zum Logo;
- bewegliche Augen;
- Blinzeln;
- Kopf-/Körperbewegung;
- einfacher Schnabel für Sprache;
- Flügelgesten;
- pro Fuß **4 Zehen/Krallen: 3 vorne + 1 hinten**;
- kein Flug-Rig.

## Workflow

```bash
python -m pip install -r requirements.txt
python scripts/project.py validate
```

Blender (Windows/PowerShell und Linux; kein Make erforderlich):
```bash
python scripts/project.py scene
python scripts/project.py blockout
python scripts/project.py feet
python scripts/project.py render
```

Der Runner arbeitet immer vom Repository-Verzeichnis aus. Er findet Blender im PATH
oder unter Windows in `Program Files/Blender Foundation` (höchste Versionsnummer).
Ziel ist Blender 5.x; die Engine-Auswahl berücksichtigt auch Blender 4.2+.
Eine bestimmte Installation kann über `--blender "C:/.../blender.exe"` oder
`BLENDER_EXECUTABLE` gewählt werden. `scene` verweigert das Überschreiben einer
vorhandenen Produktionsszene. Python-Fehler in Blender ergeben einen Fehlerstatus.

`doctor` prüft Python, Pillow, Git, Git LFS, Blender und die Referenzen.
`smoke` führt alle vorhandenen Blender-Skripte und vier 64px-Test-Renderings in einem
temporären Arbeitsverzeichnis aus; die Produktionsszene bleibt erhalten.
Dieser technische Test ersetzt keine Silhouettenprüfung anhand der Referenzen.
Die CI prüft strikte Referenzvalidierung, Python-Syntax und Tooling-Regressionschecks
unter Windows und Linux; der Blender-Smoke-Test läuft lokal.

Der feste Vieransichten-Aufbau ist in `validation/reference_views.json`
parametrisiert. Mit `python scripts/project.py setup-review` entstehen dauerhafte
1024px-Nachweise samt gespeichertem Studio-Blend und einem Vergleich nach erneutem
Öffnen. Anleitung und Referenzzuordnung: [Validierungsworkflow](docs/validation-workflow.md).
Technischer Review: [Setup-Bericht](validation/reviews/setup/report.md).

## Aktueller Arbeitsstand

Alle neun Referenz-PNGs sind vorhanden. Blockout und grobe Silhouette (#3) sind
abgeschlossen. #15 liefert eine zusammenhängende, bearbeitbare Kopf-/Hals-/Torsofläche
und symmetrische grobe Brow-/Ohrbüschelformen. Augen/Maske/Lider (#16), Schnabel (#17)
und zusammenhängende Füße/Krallen mit Stangengriff (#5) haben eigene geprüfte
Meilensteine. Flügeltopologie, Materialien, Rig und Animationen folgen unter Epic #11.

Große Blender-/3D-Artefakte sind für Git LFS vorgesehen.

Der parametrisierte grobe Blockout für Issue #13 wird mit
`python scripts/project.py blockout-review` reproduziert. Maße stehen in
[`design/proportions.json`](design/proportions.json); der gespeicherte LFS-Stand
liegt in `blender/scene/owli_blockout_v01.blend`. Vier feste Ansichten und
Referenzvergleiche: [`Blockout-Review`](validation/reviews/blockout_v01/report.md).
Der grobe Silhouetten-Freeze aus Issue #14 ist in
[`design/silhouette_freeze.json`](design/silhouette_freeze.json) dokumentiert.
Alle zwölf Checklistenbefunde und die Iterationen stehen im Blockout-Review.

Der Kopf-/Körper-Meilenstein wird mit `python scripts/head_body_review.py`
reproduziert. Parameter: [`design/head_body.json`](design/head_body.json).
Gespeicherter LFS-Stand: `blender/scene/owli_head_body_v01.blend`.
Vieransichten-, Topologie- und Verformungsnachweise:
[`Head-/Body-Review`](validation/reviews/head_body_v01/report.md).
Der ursprüngliche Blockout bleibt als eingefrorener Vergleichsstand erhalten.

Augen, Gesichtsmaske und geometrische Blinkproben (#16) entstehen mit
`python scripts/face_review.py`. Der eigene Meilenstein
`blender/scene/owli_face_v01.blend` enthält getrennte Augen-/Iris-/Cornea-Meshes,
Blick-Pivots und parametrische Lider. Dauerhafte Nachweise und Grenzen stehen in
[validation/reviews/face_v01/report.md](validation/reviews/face_v01/report.md).
Finale Augenshader und animierbare Rig-Controls folgen separat.

Ober-/Unterschnabel und Öffnungsproben (#17) entstehen mit
`python scripts/beak_review.py`. `blender/scene/owli_beak_v01.blend` enthält die
getrennten Schnabelteile mit dokumentiertem Unterkiefer-Pivot; der geschlossene
Zustand erhält den geprüften Umriss. Nachweise und Grenzen stehen im
[Schnabel-Review](validation/reviews/beak_v01/report.md).

Füße, acht getrennte Krallen und die abgerundete Stange (#5) entstehen mit
`python scripts/feet_review.py` aus dem geprüften Schnabelstand. Parameter:
[`design/feet.json`](design/feet.json). LFS-Szene: `blender/scene/owli_feet_v01.blend`.
Der [Fuß-Review](validation/reviews/feet_v01/report.md) enthält vier unveränderte
Ansichten, Griffdetails, echte Kontakt-/Topologieprüfungen und Grenzen des
Meilensteins. `40_feet_perch.py` baut nach #4 die Produktionsfüße; frühere
Blockout-Szenen verwenden weiterhin den archivierten groben Zehenguide-Stand.
Die Herkunft der alten Review-Nachweise bleibt über
[historische Bindungen](validation/history/pre_feet_v01/README.md) nachvollziehbar.
