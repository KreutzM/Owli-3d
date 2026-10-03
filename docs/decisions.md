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
