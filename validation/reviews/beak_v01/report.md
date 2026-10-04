# #17 — Separate hooked upper beak and hinged lower jaw

Accepted for #17 geometry scope after comparing the four fixed neutral views
with approved references and inspecting the opening probes. Starting point is
the merged #16 face. Final controllers and speech synchronization follow separately.

## Three goal criteria and reference decision

1. **Separate named jaws and reference-consistent closed shape — pass.** `BAK_Upper` and `BAK_Lower` are distinct closed meshes. The fixed upper part retains the distal hook; the smaller posterior lower jaw sits behind it. [Front](VAL_FRONT_comparison.png) preserves the orange center landmark from logo 00. [Left profile](VAL_LEFT_comparison.png) retains the frozen projection governed by turnaround 07; parts 08 informs the hooked construction. The new closed surface is clipped directly from the accepted envelope. All exterior vertices deviate by at most 0.000015 mm from that evaluated surface. A 0.4 mm physical mouth seam separates the jaws without changing their outer shape.
2. **Plausible opening without mask penetration — pass.** The [open profile](evidence/open/full/VAL_LEFT.png) exposes a lower jaw rotating down behind the fixed upper hook. The [3/4 opening](evidence/open/full/VAL_3Q.png) shows the dark mouth-facing surfaces inside the orange exterior. [Isolated open jaws](evidence/open/beak/VAL_LEFT.png) reveal both parts without face occlusion. Forty-one opening positions from 0 to 18 degrees pass 2,337 actual BVH collision checks against the other jaw, facial layers, head, chest and forehead geometry. Two-way vertex-to-surface samples find at least 5.614 mm mask clearance; these samples supplement surface-intersection tests and are not claimed as an exact continuous minimum distance. The lower front vertex drops 10.958 mm; maximum lower vertex travel is 21.502 mm. The upper mesh remains fixed throughout.
3. **Documented base/pivot and consistent four views — pass.** `design/beak.json` specifies the split, neutral seam, hinge and opening range. The pivot is (0, 0.095, 0.398) m at reference scale, on the extended separation plane and behind the complete cut boundary. Negative local X rotation opens the jaw. [Back](VAL_BACK_comparison.png) and [3/4](VAL_3Q_comparison.png) preserve the accepted head/eyes/mask/body; [overview](contact_sheet.png) retains all four unchanged cameras. The forehead symbol stays clear and all 50 unrelated meshes preserve geometry, transforms, material assignments, weights and subdivision settings.

Reference priority is logo 00 for identity/orange face language, technical
turnaround 07 for volume/profile and technical parts 08 for beak construction.
Beauty references remain supporting. No reference was averaged into new
proportions and no new concept art was generated. Neutral front and profile
retain the existing coarse freeze while making the jaw mechanically separable.

## Construction and reusable probe

`scripts/blender/22_beak.py` invokes `beak_geometry.build(root)` with reusable
parameters from `design/beak.json`. The evaluated frozen loft is sampled at
reference scale, divided by a plane at (0, 0.105, 0.386) m with normal (0, 1.2, 1),
closed with opposed planar inner caps and then uniformly scaled. The underlying
coarse frozen parameters and all old milestone artifacts remain unchanged.

`beak_geometry.set_open(root,value)` accepts [0,1], mapping to 0–18 degrees of
actual lower-jaw hinge rotation. It changes a documented geometry-probe pivot,
not a finished animatable controller. Future `beak_open` controls should reuse
this articulation and preserve the tested range until combined rig validation.
Planar interior caps are rigid surfaces and intentionally need no deforming quad
lattice. Orange exterior and deep navy mouth-facing diagnostic swatches reuse
the existing palette; final keratin/gloss tuning belongs to later lookdev.

An initial forward pivot caused upper/lower surface collisions while opening.
Moving it behind every cut vertex on the extended separation plane fixes the
actual geometry. A too-small first lower division read as a thin sliver; the
revised division has about 15% of the upper-jaw volume and retains a real closed
volumetric jaw. Reference-scale clipping avoids scale-dependent vertex ordering.
These choices and uncertainties are also recorded in `docs/decisions.md`.

## Blender evidence and delivery

`python scripts/beak_review.py` ran in Blender 5.2.1 LTS. It validates the current
#16 scene and complete visual-review hashes, works in an isolated copy, and
publishes only after topology, opening, rebuild, scale and fresh-open checks.
Both jaws are closed and connected, consistently outward, without duplicate
vertices or nonlocal self intersections. The lower-jaw pivot and stationary upper
hook are checked against the documented parameters. Exact 3-forward/1-rear toe
guides per foot are retained; no flight geometry or armature is introduced.

Negative probes reject an open jaw, reversed face, forward hinge collision and
invalid opening range. Repeated builds produce identical geometry and stable
counts (64 objects, 52 mesh datablocks, 6 materials). Building jaws/pivot at 80%
scale preserves vertex correspondence and restores the neutral cage exactly.
Full-character and isolated-jaw alpha silhouettes pass all four views: full
IoU is about 0.999988 or higher and isolated beak IoU at least 0.999231, with a maximum
allowed three-pixel bidirectional silhouette distance. The narrow seam is a real
separation; neither cameras nor lighting were changed to conceal it.

Two independent fresh Blender openings repeat all live checks and produce
pixel-identical 1024px canonical neutral images. Closed/half/open full-character
and isolated-jaw images are available in all four views. Probe states are never
saved over the neutral delivery. Machine measurements, scene/source/reference
and image hashes live in [verification.json](verification.json). A separately
authored [review.json](review.json) binds these three visual criteria to the
current report and images; automated `design_approval=false` does not grant
visual approval by itself.

LFS delivery: `blender/scene/owli_beak_v01.blend`. Geometry and checks live in
`beak_geometry.py`, `verify_beak.py` and `beak_evidence.py`; isolated publication
and fresh-view comparison are in `scripts/beak_review.py`.

## Limits and routine validation

The large upper hook hides much of the lower jaw in front view, as expected for
this construction; profile/3/4 and isolated views prove the separate opening.
The tested range is 0–18 degrees. Wider opening, combined head/face poses, final
rig attachments, tongue/throat detailing and speech synchronization are later
work. The planar caps and diagnostic interior color expose the split without
claiming final mouth lookdev. Parent #4 and the production character epic remain
open for other work.

```powershell
python scripts/project.py validate
python scripts/project.py smoke
python -m compileall -q scripts
python -m unittest discover -s tests -v
```

All commands passed: nine verified references, locked 3+1/no-flight invariants,
complete Blender scaffold smoke and four renders, syntax compilation and all
21 tests. A separate fresh Blender process opened the published LFS scene directly,
repeated the complete saved-scene check set and compared it to the stored reload
proof: identical. It also rehashed all 50 unaffected meshes inside that delivered
file and matched the original accepted-face snapshot. No temporary smoke rig or
open probe state is present in the neutral delivery.
