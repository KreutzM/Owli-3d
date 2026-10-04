# Design Freeze — Owli V1

## Status

The 2D design exploration phase is considered sufficient for 3D blockout.

Do not continue generating general concept images after this point unless a concrete modeling ambiguity is identified.

## Reference hierarchy

1. **00_original_logo.png**
   - authoritative for brand identity;
   - face language;
   - main color identity;
   - overall emotional tone.

2. **07_turnaround_technical.png**
   - authoritative for V1 body silhouette, profile and back interpretation;
   - use as a design guide, not a metrically exact orthographic drawing.

3. **08_parts_lookdev_technical.png**
   - authoritative for part construction and material intent;
   - eye, beak, forehead symbol, feather groups, foot/claw logic, perch material.

4. **01–04 beauty references**
   - authoritative for character/readability/style;
   - secondary for exact geometry.

5. **05–06 earlier sheets**
   - supporting references only.

## Locked decisions

- perched pose for V1;
- no flight requirement;
- organic stylized owl rather than robot;
- 4 toes per foot: **3 forward + 1 rear**;
- large separate eyeballs suitable for gaze control;
- folded wings designed to become gesture controls later;
- large feather groups instead of literal full-feather simulation;
- cyan emissive forehead network motif;
- modern metal perch with minimal cyan accents.

## Still adjustable during blockout

- exact head/body ratio;
- exact eye depth;
- beak projection;
- torso depth;
- wing thickness;
- tail length;
- perch diameter;
- exact number of modeled feather groups.

Adjustments must improve consistency across the approved views and must be documented.

## Coarse 3D silhouette decision (#14)

The reviewed coarse V1 envelope and face arrangement are recorded in
[design/silhouette_freeze.json](design/silhouette_freeze.json), with all twelve
checklist findings and four-view comparisons in
[the blockout report](validation/reviews/blockout_v01/report.md).
This is a coarse silhouette freeze, separate from production topology, final
feather layers, materials, rig and animation. Changes to the frozen large forms
require a new documented four-view review. The record binds the exact parameter,
reference, Blend and image hashes; stale evidence must not imply continued approval.
