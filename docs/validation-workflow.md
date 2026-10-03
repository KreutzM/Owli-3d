# Fixed four-view validation studio

The authoritative recipe is `validation/reference_views.json`: cameras, five
neutral white area lights, world, color management, resolution and reference
panels. Coordinates use meters and +Y faces Owli's front. The existing camera
locations, targets, 0.58 m orthographic scale and 65 mm perspective lens are
preserved. No view uses automatic fitting or view-dependent lighting.

## Reproduce the technical setup evidence

From the repository root, with Python dependencies installed:

```powershell
python scripts/project.py validate
python scripts/project.py setup-review
python -m unittest discover -s tests -v
```

`setup-review` uses the existing coarse blockout and 3+1 foot guide scripts in
an isolated temporary directory. It renders four 1024 x 1024 PNGs, saves the
studio, opens that Blend in a fresh Blender process, and repeats the four renders.
It checks exact pixel identity, geometry identity, scene/object/datablock counts,
canonical saved 1024px settings, repeated setup, image framing and depth clipping.
Deliberately shifted geometry and an invalid far plane must be rejected. The
gray technical fixture must retain visible shading without overexposure.

After all checks pass, it replaces only these dedicated evidence artifacts:

- `blender/scene/owli_validation_setup.blend` (Git LFS).
- `validation/reviews/setup/VAL_*.png`: original four 1024px renders.
- `validation/reviews/setup/VAL_*_comparison.png`: aspect-preserving reference pairs.
- `validation/reviews/setup/contact_sheet.png`: four-view overview.
- `validation/reviews/setup/render_manifest.json`: studio, reference map, projected
  bounds and render hashes.
- `validation/reviews/setup/verification.json`: save/reload checks, source/config
  hashes, unchanged geometry digest and image metrics.

The manually inspected technical findings are recorded in
`validation/reviews/setup/report.md`. This file is deliberately not overwritten
by generation; review it again after regenerating evidence. These images and the
Blend are setup evidence, not an approved Owli modeling milestone.

Select a specific Blender installation using `--blender "C:/.../blender.exe"`
or `BLENDER_EXECUTABLE`. The complete integration check runs locally; CI verifies
config validity, reference hashes/dimensions, Python tests and stored evidence
integrity under Windows/Linux.

## Render an existing working scene

```powershell
python scripts/project.py render
python scripts/project.py render --scene blender/scene/owli_validation_setup.blend --output validation/renders/setup-check
```

The default scene is `blender/scene/owli.blend`. `--scene` and `--output` apply
only to `render`; they never redirect other modeling stages. Rendering stores
the fixed cameras/lights in the loaded scene and writes a `render_manifest.json`
beside the PNGs. Output and smoke-resolution overrides are not saved as production
defaults. The saved default camera is `VAL_FRONT`, with a portable relative output
path and canonical 1024px resolution.

For each production milestone, retain the PNGs and manifest under
`validation/reviews/<milestone>/` with a written review. The setup-only comparison
boards can serve as the example for its reference pairing; do not label technical
fixture results as milestone approval.

## Framing and reference rules

Evaluated object bounding boxes in the character/perch collections must stay at
least 2% inside all image edges and between camera clip planes. The test includes
the support/base and rear toe guides. It fails rather than moving the cameras.
Unexpected visible non-studio lights also fail validation, so a beauty lighting
rig cannot silently affect technical comparisons.

Front, left profile and back pair with their labeled panels in the rank-2
technical turnaround. The 3/4 camera pairs with the rank-4 beauty view for style
and also shows the rank-2 technical 3/4 panel for geometry. Full-source filenames,
crop rectangles and ranks are versioned; crops are excerpts without warping or
mirroring. The technical 3/4 panel depicts the opposite lateral side from the
existing +X/+Y camera. Preserve both and assess symmetric volume/readability;
do not treat the pair as a metric overlay. AI-generated reference panels are
design guides, not exact orthographic measurements.

The original logo remains rank 1 for brand/face/color, and the parts/lookdev sheet
rank 3 for construction/material intent. Image ambiguities do not override the
explicit 3 forward + 1 rear rule. Findings, deviations and any justified future
projection/scale change belong in `docs/decisions.md`.
