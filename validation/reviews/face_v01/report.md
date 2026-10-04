# #16 — Layered eyes, readable mask and geometric blink

Accepted for the scope of #16 after inspecting the fixed front, left profile,
back and 3/4 views against the approved reference hierarchy. This milestone
delivers editable geometry and neutral fit, not final eye shaders or rig controls.

## Evidence and reference decision

- [Four-view overview](contact_sheet.png) and [front reference comparison](VAL_FRONT_comparison.png): both large blue/cyan eyes remain the primary facial feature. The cream cheek rings and central bridge preserve a broad bright mask. Symmetry, open neutral eyelids and the existing orange beak keep an attentive expression. Logo 00 governs identity; parts 08 governs separate eye-layer construction.
- [Left reference comparison](VAL_LEFT_comparison.png): volumetric eye depth and beak projection are visible without changing the camera. The socket fits the frozen head envelope. Turnaround 07 governs profile placement; its feather styling is deferred rather than introduced as unapproved eye placement.
- [Back reference comparison](VAL_BACK_comparison.png): the head, tufts, folded wings, body, tail and perch remain the accepted #15 forms. The narrow cream outer cheek edge is visible at the sides; no rear eye geometry protrudes through the head.
- [3/4 reference comparison](VAL_3Q_comparison.png): both eyes retain depth and the mask remains readable around both sockets. The separate iris and pupil surfaces are curved, rather than the old flat guides. Cream surfaces do not cover the orange beak.

Technical references are not exact metric orthographic projections. Frozen eye
centers and globe size take precedence over visually averaging the beauty views.
No new concept image was generated. Final feather layers, glossy gradients,
highlights and iris network motif remain later work; their absence in diagnostic
renders does not change the geometry acceptance scope of this issue.

## Construction and pivots

`design/face.json` and `scripts/blender/21_eyes_mask.py` reproduce the construction.
`FAC_EyeAim_L/R` sit at (-/+0.064, 0.074, 0.409) m at reference scale. The local
forward axis is +Y, with X horizontal and Z up. Globe, iris, pupil and cornea are
distinct closed meshes parented to each pivot. Globe radius remains 0.049 m;
surface radii are 0.04965 m for iris, 0.04995 m for pupil and 0.0508 m for cornea.
The eye layers are separate radial shells with no pairwise surface intersections.
[Isolated face layers](evidence/layers/VAL_3Q.png) and
[opaque cornea geometry inspection](evidence/cornea_geometry/VAL_3Q.png) expose
the parts hidden by the normal transparent inspection material.

Mask cheeks are thick annuli with real eye openings; the bridge stays behind
the unchanged coarse beak. Lids are separate closed quad patches. Their outer
radius is 0.0538 m and thickness 0.0012 m. The fixed outer arcs attach at the
socket; moving inner arcs meet on the same sphere at full closure. The nominal
clearance sphere is not sufficient proof by itself: the verifier measures the
closest point on every actual rendered triangle throughout the blink trajectory.

`face_geometry.set_blink(root, value)` accepts 0 (open) through 1 (closed), or a
dictionary with separate L/R values. It recomputes the nonlinear spherical cage.
The future rig must use the same constraint or an equivalent deformation; linear
shape-key interpolation would cut through the eyeball. No final drivers,
armature, facial UI or speech animation are delivered here.

## Actual Blender verification

`python scripts/face_review.py` ran successfully with Blender 5.2.1 LTS. It uses
an isolated copy of the hash-verified #15 scene and publishes only after passing:

- All 15 new meshes are closed, connected and consistently outward; no duplicate vertices, degenerate faces or nonlocal self intersections. Deforming lid cages are all quads; the annular iris/mask shells intentionally have genus one. Rigid globe/pupil/cornea pole fans do not deform for eye aiming.
- All eye layers are separate and collision-free. Both cheek masks and the bridge have no BVH surface intersections with either eye's globe/iris/pupil/cornea or the existing beak.
- Forty-one actual blink states pass mesh audits and cornea intersection checks. Minimum triangle-to-cornea clearance is **1.0248 mm**, above the required **0.3 mm**. At full closure the front and back meeting edges coincide exactly; **10,034** rays over the two complete cornea apertures find covering lid geometry.
- [Half blink](evidence/half/VAL_FRONT.png), [full blink front](evidence/closed/VAL_FRONT.png), [profile](evidence/closed/VAL_LEFT.png), [back](evidence/closed/VAL_BACK.png) and [3/4](evidence/closed/VAL_3Q.png) show no exposed iris or open split at closure. The shared contact line is a visible eyelid seam, not an open gap. [Unilateral blink](evidence/wink_L/VAL_FRONT.png) demonstrates independent sides.
- Actual eye pivots turn +/-12 degrees in pitch and yaw. Both eyes' child meshes follow their sphere-center pivots; cornea surfaces remain clear of lids and masks. Each gaze state has all four fixed-camera images.
- Deliberately opened/reversed lid meshes, unsafe lid thickness and the rejected folded canthus construction fail their gates.
- Rebuilding twice gives identical geometry and stable datablock counts (62 objects, 51 mesh datablocks, 6 materials). Rebuilding the new face at 80% scale reproduces uniformly scaled world coordinates and restores exactly afterward.
- All 36 unaffected meshes preserve control geometry, matrices, material assignments, weights and subdivision settings. The 3-forward/1-rear toe guides per foot are retained. No flight rig or flight geometry is added.
- Two independent fresh Blender openings repeat the geometry, blink, gaze, fixed studio and framing checks; canonical 1024px renders are pixel-identical in all four views. Probe states and temporary cornea inspection swatches are not saved into the neutral delivery.

Machine-readable measurements, source/reference/image hashes and reload results
are in [verification.json](verification.json). `design_approval=false` identifies
the automated evidence; the separate [review.json](review.json) binds this written
four-criterion visual decision to current evidence. CI rejects stale hashes or
missing criteria and does not synthesize visual approval.

## Delivery and limits

Saved LFS milestone: `blender/scene/owli_face_v01.blend`, neutral eyes/lids and
the unchanged four-camera studio. Construction lives in `face_geometry.py`,
actual checks in `verify_face.py`, probe rendering in `face_evidence.py`, and
isolated build/reload/publication in `scripts/face_review.py`.

The smooth cream sockets retain visible canthus seams and a narrow center bridge.
Designed facial feather groups will soften their primary-volume appearance.
The completely transparent cornea inspection shader and matte iris/pupil palette
are temporary. Closed lids use a straight shared meeting edge; later expression
shaping and head attachment must preserve closure and clearance. +/-12 degrees
is the tested gaze range, not a promise of unrestricted aiming. Optional combined
head/beak/wing poses need later rig validation. The coarse beak remains #17 work.

Routine checks accompanying this milestone:

```powershell
python scripts/project.py validate
python scripts/project.py smoke
python -m compileall -q scripts
python -m unittest discover -s tests -v
```

All commands passed: reference validation confirms nine reference records and
the 3+1/no-flight invariants; all scaffold stages and four smoke renders succeed;
syntax compilation passes; all 18 tests pass, including the existing #14/#15
evidence gates. A separate fresh process opened the published
`owli_face_v01.blend` directly, reran `face_evidence.checks(root)` and compared the
entire result with `verification.json/reloaded`: identical (15 meshes, 1.0248 mm
minimum clearance, 10,034 closed-coverage rays). The smoke rig is confined to its
temporary fixture; the delivered #16 scene has no armature.

This report concerns the geometry milestone. Parent #4 and the production Owli
epic remain open for the remaining character work.
