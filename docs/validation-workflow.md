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

## Parameterized coarse blockout (#13)

```powershell
python scripts/project.py blockout-review
```

Builds scene setup, coarse volumes and 3+1 gripping foot guides in isolation.
Rebuilds must preserve geometry and object/mesh/material counts. Parameter probes
exercise eye spacing/depth, beak projection, wing mass, tail position and global
character/perch scale; probes are restored before rendering. The saved milestone
is reopened in a fresh Blender process, inspected and rerendered. All four 1024px
images must be pixel-identical within the same render environment.

Outputs: `blender/scene/owli_blockout_v01.blend` (LFS), four renders, reference
comparison boards, contact sheet, manifest and verification under
`validation/reviews/blockout_v01/`. Manually reviewed findings belong in its
`report.md`, which generation preserves. The production file is unaffected.
`design/proportions.json` stores all dimensions at reference height in meters;
`character_spec.json` scales the complete scene. Ring schemas and provisional
choices are documented in `docs/decisions.md`. Both stages preserve a loaded
Blend's filename when saving, so milestone edits remain in the selected scene.

`setup-review` refreshes the neutral studio fixture from the same coarse forms,
clearing its debug material slots. Its evidence also includes the model probes
and design-source hashes. It remains a studio check, separate from silhouette
approval in #14. Neither command creates final materials, rig or flight geometry.

## Manual silhouette decision (#14)

`design/silhouette_freeze.json` is manually authored after inspecting all four
fixed views. It records each exact `validation/checklist.json` item with a reason,
authoritative references and visible evidence. `scripts/silhouette_review.py`
checks completeness and hashes; it never grants visual approval. The automation's
`design_approval=false` means that automation does not replace this visual decision.

After rebuilding or changing the frozen forms, old hashes intentionally become
stale. Review the four images again and write a new decision; do not automatically
refresh approval hashes. Run `python -m unittest discover -s tests -v` to check
both studio/model evidence and the current manual freeze. Historical candidates
under `blockout_v01/iterations/` document rejected findings and remain historical;
the active artifact is `blender/scene/owli_blockout_v01.blend`.

## Editable head/neck/torso milestone (#15)

```powershell
python scripts/head_body_review.py
python -m compileall -q scripts
python -m unittest discover -s tests -v
```

The dedicated runner first verifies the current #14 freeze. It builds in an
isolated directory and runs `20_head_body.py`, using `design/head_body.json`.
It preserves all deferred geometry and the old blockout evidence. Delivery is
`blender/scene/owli_head_body_v01.blend` (LFS), with durable evidence under
`validation/reviews/head_body_v01/`. The report is manually written and preserved.

Checks inspect control and subdivided surfaces for connected closed quad shells,
outward winding, duplicate vertices, nonlocal self intersections, symmetry,
distributed pole valence and identity transforms. Real weighted head tilt/turn
and left/right wing-root displacement probes inspect the resulting meshes;
they are topology tests, not a finished avatar rig. Deliberately opened, reversed,
disconnected and asymmetric meshes must fail. Repeated builds, datablock counts,
unchanged deferred-part hashes and global resizing are checked separately.

All five primary surfaces are measured against the evaluated frozen envelopes.
Transparent fixed-camera images compare both the whole character and the primary
surfaces alone, preventing unchanged wings/face from hiding a topology silhouette
change. IoU and bidirectional silhouette-distance gates are in the parameter file.
Wire and deformation views expose the primary cage without face/wing occlusion.
Four standard 1024px comparison boards retain the original approved reference map.

Canonical standard renders come from opening the saved scene in a fresh Blender
process. A second independent opening repeats geometry, deformation and studio
checks and must yield pixel-identical canonical renders. Build-process render
cache output is not the canonical delivery. The automated `design_approval=false`
does not grant visual approval; the written report records the four-view decision,
remaining overlaps and deferred work. CI binds stored proofs to current sources,
LFS scene and images and recomputes the silhouette gates from their alpha images.

## Layered eyes, mask and geometric blink (#16)

```powershell
python scripts/face_review.py
python scripts/project.py validate
python scripts/project.py smoke
python -m compileall -q scripts
python -m unittest discover -s tests -v
```

The dedicated runner validates the #14 freeze and current #15 source/artifact hashes,
copies the accepted primary scene into an isolated workspace, and builds the face
from `design/face.json`. `21_eyes_mask.py` is the reusable production stage. The
LFS output is `blender/scene/owli_face_v01.blend`; permanent neutral reference boards,
separate layers/cornea, half/full blink, unilateral blink and four gaze probes live
under `validation/reviews/face_v01/`. All probes use the same four fixed cameras.

Live Blender checks inspect every new surface for closure, connectedness, normal
winding, duplicate vertices and nonlocal self intersections. Spherical iris/pupil/
cornea shells are distinct meshes parented to eye-center aim pivots. Pairwise BVH
checks reject eye-layer intersections and mask intersections with either eye or
the existing beak. The mask is a thick annulus with a real opening, not a closed
ellipsoid covering the eyeball. Genus-one iris/mask shells and rigid spherical
pole fans are intentional; deforming lid cages are all quads.

`face_geometry.set_blink(root, value)` reconstructs the actual lid cage on its
clearance sphere for values in [0,1]; a dictionary permits independent L/R values.
It is a geometric probe API, not a final rig controller. Linear shape-key blending
would cut through the eye, so the future rig must use nonlinear reconstruction or
an equivalent sphere-constrained deformation. The verifier exercises 41 positions,
calculates the exact closest point on every rendered lid triangle, checks BVH
collisions and audits each resulting shell. At closure, front and back meeting
edges coincide exactly and over 10,000 rays cover the whole cornea aperture.

Repeated builds must preserve geometry and datablock counts. New face geometry is
also rebuilt at 80% scale and compared in world coordinates. All 36 unaffected
meshes retain geometry, transforms, material assignments, weights and subdivision
settings. Deliberately open/reversed lids, unsafe clearance and the rejected folded
canthus construction must fail. Two fresh Blender processes inspect the saved
neutral scene, repeat all blink/gaze checks and produce identical canonical pixels.

CI verifies current source, scene, reference and evidence hashes plus a separately
authored four-criterion `review.json`. `design_approval=false` in automated output
does not grant visual acceptance. Final glossy shaders/network iris motifs and
animatable controls remain in later goals; the transparent cornea inspection
material reveals geometry beneath it without implying final lookdev approval.
