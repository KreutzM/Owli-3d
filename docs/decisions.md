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
