# Eigene Evidenz für das unabhängige Review #33

Bewertung und stabile Finding-IDs stehen im
[versionierten Bericht](../../../docs/reviews/independent-interim-after-feet.md).
Baseline `ee48046b792e3647f454bc4223788271283542b9`, aktuelle Szene
`owli_feet_v01.blend`, SHA256
`0fb1512b3a27c4ebe5b7cbdebf520643b7208f2c74f8a847545ffc51dda66797`.

## Belege

- `VAL_*.png`, Vergleichsboards und `contact_sheet.png`: frische tatsächliche
  1024px-Szenenansichten, dieselben vier Kameras. Boards nutzen bestehende
  freigegebene Referenzen mit Rang/Panel-Zuordnung, keine neuen Konzepte.
- `toes/`, `blink/`, `beak_open/`: ergänzende Isolation bzw. echte Bewegungsproben,
  weiterhin dieselben vier Kameras. Isolation ersetzt keine neutrale Gesamtansicht.
- `scene-inspection.json`: unabhängiges Cage-/Evaluated-Inventar, Transforms,
  Ressourcen, Collections, Studio, Framing, neutraler Pair-BVH-Scan, Foot-Checks.
- `movement-probes.json`: tatsächliche begrenzte Kopf/Root/Blink/Aim/Beak-Proben.
- `independent-comparison.json`: zwei frische neutrale Prozesse und akzeptierte
  Bilder pixelgleich. `feet-*checks.json`, `feet-comparison.json`,
  `feet-commands.json`: vollständige unabhängige Scratch-#5-Reproduktion/Reloads.
- `history-audit-evidence.json`: echter Git-Vorgängerbytevergleich, alle JSON-Diffs,
  unveränderte Assets und kontrollierte Gate-Omission-/Korruptionsproben.
- `coarse-dispatch.json`: archive/current Dispatch im scratch Blender identisch.
- `parameter-corners.json`: zusätzlich vier erlaubte Ecken, Mittelpunkt und vier
  außerhalb liegende Werte. `command-results.json` und `logs/`: ausgeführte Befehle.
  Logs sind als UTF-8 mit LF gespeichert; Meldungsinhalte bleiben erhalten.
- `evidence-manifest.json`: SHA256s eigener Belege und der gelesenen Baselinequellen.
  Dies ist eine Provenienzliste, kein automatischer Designapproval-Validator.

## Reproduktion in PowerShell

Von der angegebenen Baseline im Repository arbeiten. `tmp/` ist Scratch.
Die Produktionsdateien werden von diesen Review-Befehlen nicht gespeichert.
Keine der existierenden milestone review build/publication Funktionen aufrufen.

```powershell
python scripts/project.py doctor
python scripts/project.py validate
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/project.py smoke

$reviewEvidence = Join-Path (Get-Location) 'validation/reviews/independent_interim_after_feet'
$reviewBlender = 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe'
$reviewScene = Join-Path (Get-Location) 'blender/scene/owli_feet_v01.blend'

$env:OWLI_INTERIM_MODE = 'neutral'
$env:OWLI_INTERIM_OUTPUT = Join-Path (Get-Location) 'tmp/independent-review-33/recheck-a'
& $reviewBlender --background $reviewScene --python-exit-code 1 --python (Join-Path $reviewEvidence 'inspect_scene.py')
$env:OWLI_INTERIM_OUTPUT = Join-Path (Get-Location) 'tmp/independent-review-33/recheck-b'
& $reviewBlender --background $reviewScene --python-exit-code 1 --python (Join-Path $reviewEvidence 'inspect_scene.py')
$env:OWLI_INTERIM_MODE = 'probes'
$env:OWLI_INTERIM_OUTPUT = Join-Path (Get-Location) 'tmp/independent-review-33/recheck-probes'
& $reviewBlender --background $reviewScene --python-exit-code 1 --python (Join-Path $reviewEvidence 'inspect_scene.py')

# --output must be a new directory; an existing one is refused.
python validation/reviews/independent_interim_after_feet/reproduce_feet.py --output tmp/independent-review-33/feet-recheck
python validation/reviews/independent_interim_after_feet/history_audit.py
& $reviewBlender --background $reviewScene --python-exit-code 1 --python (Join-Path $reviewEvidence 'parameter_corners.py')
```

`history_audit.py` writes `tmp/history-audit-evidence.json` and creates/deletes
only its own temporary copied fixtures. Git history including `84bee42` must be
available. `parameter_corners.py` writes scratch parameters/results under
`tmp/independent-review-33/`; it never saves the loaded accepted scene.

For coarse dispatch, create a scratch directory with copies of `design/` and
`validation/reference_views.json`, then invoke the absolute script path with that
directory as CWD:

```powershell
python -c "from pathlib import Path; import shutil; p=Path('tmp/independent-review-33/coarse-recheck'); p.mkdir(parents=True,exist_ok=True); shutil.copytree('design',p/'design',dirs_exist_ok=True); (p/'validation').mkdir(exist_ok=True); shutil.copy2('validation/reference_views.json',p/'validation/reference_views.json')"
Push-Location tmp/independent-review-33/coarse-recheck
& $reviewBlender --background --factory-startup --python-exit-code 1 --python (Join-Path $reviewEvidence 'history_coarse.py')
Pop-Location
```

Read `coarse-dispatch.json` there. Compare neutral JSONs and raw decoded RGBA pixel
bytes with the other fresh process and accepted #5 PNGs; do not infer equality
from filenames. `reproduce_feet.py` performs its own strict accepted-data/pixel
comparisons. Arbitrary saved Blend container bytes need not be deterministic.

These drivers only gather evidence or make assertions. The visual interpretation,
scope limitations, intentional contacts and deferred work remain the written
reviewer's responsibility. Separate motion probes are not a complete avatar rig.
