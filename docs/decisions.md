# Decision log

## 2026-10-03 — Design image phase frozen

The current approved logo, technical turnaround, technical parts/lookdev sheet and selected beauty views are sufficient to begin 3D blockout.

New general concept images are no longer created by default.

## 2026-10-03 — Perched V1

Owli V1 sits on a modern cylindrical tech perch. Flight is deferred.

## 2026-10-03 — Organic tech character

Owli is modeled as a living stylized owl with integrated digital motifs, not as a metallic robot owl.

## 2026-10-03 — Foot anatomy

Each foot has exactly 4 toes/claws: 3 forward and 1 rear.

## 2026-10-03 — Feather strategy

Use clean body/wing volumes plus major stylized feather groups. Do not build full realistic feather simulation for V1.

## 2026-10-03 — Animation-first topology

Eyes, beak, wing roots, neck and feet must be designed with future avatar deformation in mind from the beginning.

## 2026-10-03 — Fixed validation studio (issue #12)

Camera locations/targets, 0.58 m orthographic scale and the 65 mm 3/4 lens from
the original renderer remain unchanged. Camera/light/render/reference parameters
now live in validation/reference_views.json. Five fixed neutral white area lights,
an explicit neutral world and Standard color management replace the unlit default.
Light power was reduced after visual review found clipped white fixture surfaces.
The saved studio uses 1024px renders, zero exposure compensation and no automatic
fitting. Object bounds must keep a 2% margin; invalid image/depth framing fails.

The validation Blend uses only existing coarse volumes and exactly 3+1 toe guides
as a technical fixture. No anatomy, material-design or silhouette decisions are
introduced. Geometry identity and four exact pixel comparisons after save/reload
are checked. The production scene is not created or overwritten by setup-review.

Front/profile/back use labeled technical turnaround panels. The 3/4 board shows
both the original beauty reference (style, rank 4) and technical 3/4 panel (geometry,
rank 2). The technical 3/4 panel depicts the opposite lateral side to the preserved
+X/+Y camera; it is not mirrored and is not interpreted as a metric alignment.
The back panel's drawn cyan crown motif does not authorize a second rear symbol;
the logo and written specification require a centered forehead motif. Visual
ambiguity in claw drawings cannot overrule the explicit 3+1 foot specification.

The coarse fixture still lacks the approved brow/ear silhouette, cream mask,
layered eyes, tech motif and real gripping toes. Its proportions, tail and beak
remain provisional. These existing modeling limitations are assigned to #13/#14
and later production goals; this setup review grants no silhouette approval.

## 2026-10-03 — Parameterized coarse blockout (issue #13)

All authored dimensions now live in design/proportions.json. Values are meters at
reference_height_m=0.45; character_spec.production_scale applies uniformly to every
character and perch vertex. Ring rows are [z, center_x, center_y, radius_x, radius_y].
Lofts represent primary head/body, folded wings, compact centered tail, mask bridge,
chest, hooked beak and one broad swept tuft on each side. Two spherical eyes remain
separate; iris/pupil caps are positioning guides. Deterministic sphere construction
avoids Blender operator polygon-order variation on repeated builds.

The logo controls face/color identity; technical turnaround 07 controls compact
perched volume and side/back interpretation; parts sheet 08 controls the hooked
beak and gripping foot intent. A broad navy brow and cream cheek/bridge volumes
reserve the feather mass without modeling individual feathers. The reference's
layered crest is represented by one editable volume per side. No conflicting old
concept proportions were averaged in. Fixed #12 camera and light parameters are
unchanged; the opposite-side technical 3/4 panel remains unmirrored.

Perch bar length is 0.37 m rather than the former 0.43 m, radius is 0.0185 m.
The ear tips reach 0.53 m above the base; the nominal 0.45 m character scale is a
provisional recipe scale, not a strict foot-to-crown metrology guarantee. The
body tapers into the seat; visible leg/pad guides connect it to the bar. Each foot
has exactly three forward curves and one rear curve around the bar, with tips
below its center. Rear centers remain strictly behind the bar. Dark toe tips are
part of each guide mesh; they are not additional anatomical toes or final claws.
Final foot topology and grip articulation belong to #5.

Simple rough, nonmetallic debug swatches use the unchanged existing logo palette
with explicit sRGB-to-linear conversion. These provide mask/eye/beak readability;
they do not replace the material specification. Glossy layered eyes, orange chest
feather accents, cyan plumage layers, forehead network geometry/emission and metal
perch finishing remain in #6/#16/#18/#19 and later production steps. The forehead
motif is not inferred on the back from turnaround 07's ambiguous crown drawing.
No new concepts, flight geometry, rig or fine feathers were added.

Four fixed views were inspected against their approved reference panels. The
blockout establishes the required anatomy and primary masses, but the mask/brow
transitions are separate overlapping volumes; ear tips remain broad, neck seams
and chest/tail ends pinch, and the cyan eye guides lack eyelids, cornea and final
iris depth. These are explicit coarse-stage limitations. Relative head/body,
beak, tail and wing proportions still require the separate #14 silhouette review.
This milestone grants no silhouette freeze or production-readiness approval.

The neutral setup evidence is refreshed using the current coarse anatomy with
material slots cleared. Its cameras/lights are identical to #12; the colored
blockout evidence and saved milestone are delivered separately. Integration
checks repeat builds without object/mesh/material leaks, probe eye spacing/depth,
beak/wing/tail edits and uniform scale, restore the baseline, render four views,
then reopen and rerender in a fresh Blender process. Controlled parameter probes
are tests, not new design iterations or alternate approved character designs.

## 2026-10-04 — Four-view coarse silhouette freeze (#14)

The #13 baseline was reviewed simultaneously against logo 00 (face/brand/color),
technical turnaround 07 (volume/profile/back), and parts 08 (beak/feet). It showed
undersized eye read, an oversized shield-like cream chest, exposed leg columns,
and a tail terminating too high in the back. Parameters now cover more of the
legs with the lower body, shorten the cream chest into a tapered V, add two broad
orange chest masses, enlarge eyes from 0.086 to 0.098 m diameter, move their centers
from Y=0.096 to Y=0.074, widen/shorten the coarse beak projection, lower wing tips,
and extend the centered tail below the perch bar. Tufts now sweep inward at their
tips, and the brow tilt is reduced from 0.20 to 0.08 rad after a stern-expression
finding. Mask lobes are narrowed to avoid broad cream side protrusions in back.

Iterations are retained under validation/reviews/blockout_v01/iterations/:
13_baseline, 14_iteration_01 and 14_iteration_02. Each includes four original
renders and reference boards, parameters and verification. Iteration 01 was
rejected for excessive eye projection; iteration 02 for stern brows and broad
cream temple edges. The final iteration resolves these coarse placement blockers.
Tiny cream temple seams remain a topology/feather integration task, not a large
volume error. Overlapping component joins and smooth bulb-like primary masses
are intentionally coarse; later topology must preserve the frozen outer envelope.

Two orange chest masses are color/volume guides, not individual detailed feathers.
A single sparse cyan graph reserves the forehead motif's position from logo/parts
references. It is a matte geometry guide, not the finished emissive tech asset.
Upper points can be visible above the head from back/profile; there is no second
rear symbol. Final feather integration, emission and node styling belong to #18.
No new design art, flight geometry, fine feather layers or rig was introduced.

The coarse silhouette and face arrangement are frozen to the explicit hashes and
12 reasoned checklist results in design/silhouette_freeze.json, with visible
findings in validation/reviews/blockout_v01/report.md. This freezes the large
head/body/wing/tail/beak envelope, seated pose and eye/mask placement. It does not
approve production topology, deformation, final materials, eyelids, cornea,
individual feather groups, final claw mechanics or animation. Those goals must
respect this envelope; a later substantial silhouette change requires a new
four-view review and an updated freeze decision, rather than changing cameras.

The fixed studio remains unchanged. Technical verification never grants visual
approval automatically: its design_approval=false refers to the automated check.
The separately authored silhouette_freeze.json is the visual decision. It binds
current parameters, checklist, camera recipe, reference hierarchy, source images,
saved Blend and four final images. CI rejects missing checklist entries, blocking
findings, wrong reference ranks or changed/stale freeze artifacts. The neutral
setup fixture is refreshed separately from the same current primary volumes.

## 2026-10-04 — Editable primary head/neck/torso topology (#15)

The #14 outer envelopes remain authoritative. Stage 20 samples evaluated head and
torso envelopes and replaces both closed overlapping coarse objects with one
closed, continuous quad shell. Horizontal circumferential loops pass through
the neck; there are no hidden head-bottom/body-top caps inside this shell.
Distributed quad-disk caps avoid high-valence polar fans. Brow and swept ear-tuft
masses become separate closed quad primary volumes, mirrored in X. Their deliberate
closed attachment roots still overlap the head, as the design calls for feather
groups; joining those feather roots is separate from eliminating torso/head
internal surfaces. Face mask, lids, eyes, beak, wings, chest guides, tail and 3+1
feet are preserved byte-for-byte at mesh/matrix level for their own goals.

Reference authority remains logo 00 for face/color identity, turnaround 07 for
outer volumes and parts 08 for construction intent. No camera, illumination,
reference crop, material palette, anatomy or perched/no-flight decision changed.
The small shape adjustment from replacing coarse subdivision caps and smoothing
the envelope junction is measured against the old evaluated surfaces and checked
in full and isolated-primary silhouettes. This is topology refinement within the
existing freeze, not a new general design or concept-art phase.

Numerical ray/quad tessellation noise in the coarse source is not interpreted as
an asymmetric design. Paired torso rings are symmetrized, and the right tuft is
constructed from the left by reflection and reversed winding. Sampling occurs
at reference scale and the completed cage is uniformly scaled afterward, avoiding
scale-dependent BVH tessellation. Additional end loops prevent subdivision pulling
the seated lower-body envelope inward; small insets at the extrema avoid microscopic
sliver caps. Early diagnostic builds exposed symmetry, cap and scale problems;
these were fixed before accepting or publishing the milestone.

Body/head weights partition unity with a broad soft transition from Z=0.265 to
0.385 m; the neck pivot is Z=0.325 m. Independent left/right wing-root masks provide
soft attachment regions rather than cut-out sockets or a rigid shell. Head tilt
15 degrees, turn 20 degrees and each wing-root displacement 12 mm are exercised
on the actual cage and subdivided result. Weights are preparation, not final rig
approval: facial/tuft attachments, wing deformation, final bone layout and volume
preservation still require their subsequent production goals. Rigging should reuse
the editable cage/loops and refine these initial weights in combined pose tests.

The full avatar retains intentional coarse face/chest/wing overlaps. Neck/body
continuity is delivered here; face-mask/eyelid construction belongs to #16, beak
articulation to #17, feathers to #6 and final surface/tech treatment to #18/#19.
The navy/blue boundary is a debug material assignment, not a seam in the new mesh.
Do not mistake the matte diagnostic palette or four-view topology acceptance for
completion of the production character. The LFS milestone, fresh-open verification,
fixed-view reference comparisons and limits are documented in its review report.
