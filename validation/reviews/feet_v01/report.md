# #5 — Connected feet, four claws and opposed perch grip

Production foot geometry is accepted for this milestone. The scene is
`blender/scene/owli_feet_v01.blend`, built from the accepted #17 scene through
`scripts/blender/40_feet_perch.py`. The permanent hash-bound Blender evidence is
`verification.json`; the visual decision is `review.json`.

Each foot is one closed connected all-quad skin with an ankle, pad, three forward
branches and one rear branch. Eight separately editable closed claw meshes meet
the matching terminal caps. Each skin has 4,482 vertices / 4,480 quads; each claw
has 354 vertices / 352 quads. No duplicate vertices, disconnected surfaces,
self intersections or inward/inconsistent faces were found. The three rounded
perch components each have 3,202 vertices / 3,200 quads.

## Reference decision and four unchanged views

Logo 00 remains authoritative for the orange/navy brand palette. Turnaround 07
governs the perched envelope and profile; parts sheet 08 governs thick orange
toes and dark hooked claws. The explicit 3-front-plus-1-rear rule governs any
ambiguous overlapping digits in the drawings. Beauty 01 supports the 3/4 styling
but cannot overrule the technical geometry. No new concept art was generated.

| View | Visible finding | Permanent evidence |
|---|---|---|
| Front | Three distinct front digits per foot, dark hooked ends, compact symmetric pads; perch remains below and secondary to the character. | `VAL_FRONT_comparison.png`, `VAL_FRONT_grip_detail.png` |
| Left profile | Front and rear digits oppose one another around the bar; the rear hook turns behind and below it. Pad rests at the bar crown. | `VAL_LEFT_comparison.png`, `VAL_LEFT_grip_detail.png` |
| Back | One rear digit per foot is visible beside the compact tail; there is no duplicated front-row arrangement. Tail/body envelope is unchanged. | `VAL_BACK_comparison.png`, `VAL_BACK_grip_detail.png` |
| 3/4 front | Three front hooks and the rear digit bases remain distinct. The bar naturally occludes the lowest rear tips; the isolated toe view exposes their complete opposed path without moving the camera. | `VAL_3Q_comparison.png`, `VAL_3Q_grip_detail.png`, `evidence/candidate/toes/VAL_3Q.png` |

All full-character images use the original four orthographic cameras and fixed
studio. The four detail images are documented pixel crops enlarged three times;
their exact source rectangles are in the verification record. The additional
isolated `feet` views retain the bar; `toes` views remove the other meshes only
to inspect branching and normally occluded anatomy. They are explicitly separate
from the full production views.

The smoother final skin is a designed primary surface rather than literal scale
sculpting. Refinement is confined to the feet and perch. All 37 other predecessor
mesh geometries, transforms, material assignments, weights and modifiers, and
all three eye/jaw pivot matrices, are unchanged. The existing wing, feather,
eye-lookdev and rig differences from the drawings remain their separately planned
goals; they are not changed or approved by this foot review.

## Actual contact and mechanical support

The nominal bar radius is 18.5 mm (diameter 37 mm); foot centers are X = ±55 mm.
The pad center is Z = 123.5 mm, with 15 mm vertical radius, so its underside
contacts the Z = 108.5 mm crown. This lowers the previous guide pad by 1.5 mm to
remove its support gap. The skin reaches 101.25 degrees around the bar; the dark
claw continues to 157.5 degrees. Rear branches use the opposing negative angles.

Toe/claw rings align with the actual 128-sided bar facets. Verification clips
every actual foot/claw triangle against the bar's straight-section interior, checks
nearest-surface contact for all eight anatomical branches and claws, and verifies
support vertices at the crown. The tolerance is 0.2 micrometers for Blender float
precision. All 45 independent foot/claw collision pairs pass. Matching toe/claw
terminal caps and their common boundary are deliberate contact; ankle/body and
bar/stem/base overlaps are intentional attachment joints.

`design/feet.json` exposes the radius, foot spacing, transition, skin/claw split
and mesh settings. Radius 16–22 mm and half spacing 50–62 mm are tested at both
limits. The pad rises with radius to retain crown support. These ranges describe
valid construction; changing them still requires a new four-view visual review.

## Reproduction and validation

Run from the repository root, with Blender 5.2.1 LTS available:

```powershell
python scripts/feet_review.py
python scripts/project.py validate
python -m compileall -q scripts
python -m unittest discover -s tests
python scripts/project.py smoke
```

The review command copies the accepted predecessor into an isolated workspace,
executes the production stage, repeats the build, checks half/double global scale
and the permitted parameter limits, and rejects floating, penetrating and front-
displaced rear claws. It then saves and opens the scene in two fresh Blender
processes. All four reload renders are pixel-identical; actual geometry, contact,
studio and framing checks match the build. The stage smoke now runs the actual
foot inspector instead of checking guide names.

Local results: all 25 Python tests passed, strict project/reference validation
passed, Python compilation passed, and the complete Blender stage smoke passed.

The legacy guide stage and CLI source are preserved byte-for-byte. Historical
review dependencies are relocated with snapshots and an audited manifest under
`validation/history/pre_feet_v01/`. Their scene bytes, pixels and criterion
decisions are unchanged; this does not extend their approval to the new feet.

## Boundaries and next work

The neutral gray perch shader is an inspection treatment that makes dark claws
legible. Brushed metal, cyan lighting accents and final keratin shaders belong to
the existing #18 surface/lookdev goal. Toe vertex groups identify real connected
branches for later controls; no toe animation or final avatar rig is claimed here.
The rear tips' natural front-view occlusion is documented above. No other blocking
geometry finding remains for #5.
