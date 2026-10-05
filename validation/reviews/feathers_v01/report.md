# Goal #6 — folded wings and broad feather geometry

The geometry milestone is accepted for `owli_feathers_v01.blend` after the
independent visual and technical reviews. Six coarse guides were replaced by
three editable primary meshes and 48 broad, closed quad feather groups. The
organic #37 mask, brows, eyes, beak and perched 3+1 feet remain unchanged.
Final materials, complete rig controls and animation retain their later goals.

## Exact delivered scene and authority

- Scene: `blender/scene/owli_feathers_v01.blend`, 1,385,718 bytes.
- SHA256: `76ee3f1c0f8b4314aee40585445c14e3b2d193b7aa04c7e2c86e6f810f576b0a`.
- Predecessor: Git `966b7f02489ebad4890ba17a6c64f4c03adc2803`, accepted #37 scene
  SHA256 `8685fc054428ec848f20a922c995487f9ac4a2797cbe3713eaeb5e364b02e8fb`.
- Reference authority: original logo 00 for brand/cream face, technical turnaround
  07 for side/back silhouette and compact folded wings/tail, parts sheet 08 for
  directional layering. Beauty references are supporting. No new concept art.
- Four unchanged cameras: `VAL_FRONT`, `VAL_LEFT`, `VAL_BACK`, `VAL_3Q`.
  Their transforms, lighting, rendering settings and 0.45m reference scale are
  inherited exactly. All published canonical images are 1024x1024 RGBA.

The final scene contains 109 objects: 95 meshes, five empties, four cameras and
five lights. There are seven diagnostic materials, no armature and no actions.
This is an intermediate geometric delivery in Epic #11.

## Components and gesture preparation

| Region | Actual delivered geometry |
|---|---|
| Wings | Two closed quad primaries and 12 broad upper/lower layers |
| Back | Six mirrored head/body tiers, 12 leaves |
| Chest/flanks | Three cream tiers, orange accents and blue flanks, 10 leaves |
| Center foundations | Head, body and chest center groups, three leaves |
| Tail | Closed primary plus center and two mirrored pairs, five leaves |
| Face finish | Mirrored outer-mask, cheek and bridge sweeps, six leaves |

All 51 new meshes are editable actual geometry. `design/wings_feathers.json`
defines dimensions, depth spines, rooting and layer layout; stage30 builds it
through `feathers_geometry.py`. Paired meshes are exact reflections, with measured
maximum mirror deviation below 2 micrometers. No feather simulation is involved.

The two `FTH_WingRoot_L/R` empties own each primary and its visible layers.
`set_gesture(root,left,right)` accepts 0..1 and applies a shared nonlinear vertex
field up to 12 degrees. It blends over 45mm at the shoulder; vertices above
335mm stay fixed. Durable `fth_rest` mesh coordinates restore exact neutral.
This proves combined wing/layer motion; final animator controls belong to #23.

Root seating is measured on actual supporting meshes. All 48 leaves have nine
front/back root samples. Maximum front-root distance is 0.780121mm against a
1.5mm limit; every leaf has a back-root sample at least 0.131826mm inside support.
Face and tail curves anchor to actual support ray hits and ease into the authored
spines. Root embedding and designed layer overlap are intentional attachments.

## Four-view visual decision

The primary agent inspected the actual final four canonical views and movement
endpoints against references 00, 07 and 08. An independent visual agent inspected
all four canonical views, comparisons and all 20 pose images, then freshly opened
the exact scene. Its separately bound report records the final verdict.

| View | Final finding |
|---|---|
| Front | Continuous cream mask-to-chest read, visible broad V layers, restrained paired orange accents; folded wings frame the body and feet |
| Left profile | Wing tiers lie against the primary, cream roots return to the mask/head, compact tail fans backward; perch grip remains readable |
| Back | Mirrored descending tiers and center foundations overlap; primary skin is deliberately visible between the few broad groups; compact centered tail |
| 3/4 front | Mask, cheek/bridge finish, wing thickness and chest layering read together; gesture endpoints move each primary and its layers coherently |

The layer count intentionally abstracts the dense illustrated plumage into broad
groups over clean primary surfaces, following the repository modeling policy.
Diagnostic swatches do not reproduce the final gradients, eye depth or satin
look. These material differences belong to #18/#19 and are not hidden by camera
changes. The forehead network and perch still use their predecessor geometry.

## Review findings resolved

| Finding | Concrete correction and final check |
|---|---|
| V6-01 | Central cream gap and floating neck read: seated face roots plus a recessed center foundation; broad cream V tips remain visible |
| V6-02 | Isolated back pairs: narrower recessed center groups and inward middle tips establish tier overlap while retaining broad group construction |
| V6-03 | Raised outer cream crescent: actual mask-ray root anchor, smooth authored spine; independent profile check passes |
| G6-TECH-01 | Floating face/tail roots despite an old blanket property: actual support anchoring and per-leaf front/back measurements replace that unsupported claim |

No blocking findings remain for #6. Corrections changed actual geometry; no
physical admission threshold was weakened. Reports bind the final run12 scene.

## Actual Blender and preservation checks

The producer executed four fresh Blender 5.2.1 LTS processes: build, saved-build,
reload-A and reload-B. All exited 0. Repeated construction is identical without
datablock leaks. The saved neutral geometry, bindings, studio, framing, feet and
functional data match exactly on three fresh opens; decoded canonical pixels
are identical for every required view. Live/pose renders remain separate because
in-process Eevee caches can differ slightly from fresh canonical rendering.

Every new cage/evaluated surface is connected, closed, outward and nondegenerate.
Triangle-interior checks include adjacent and coplanar cases. Exactly 44 retained
#37 meshes and original pivots remain unchanged. Removed guides are the two
`BLK_Wing` meshes, tail, chest and two chest accents. History is protected by
462 code-owned Git/LFS anchors, independently compared to actual predecessor
bytes. The old metadata-only stage30 is archived byte-exact under `legacy/`.
Historical source helpers, images, scenes and approvals were not regenerated.

Actual functional checks on the new scene:

- 41 full-range blink states, 10,034 closed-lid coverage rays, zero meeting-seam
  gap and 1.024827mm minimum inherited lid/cornea clearance.
- Four actual gaze states, X/Z at +/-12 degrees, plus 408 eye/new-mesh checks
  in each state; 8,364 lid/new-mesh checks across the blink range.
- 41 beak states, 0..18 degrees, fixed upper jaw, 2,091 old-part checks and
  4,182 beak/new-mesh checks. No detected intersections.
- Six isolated/combined half/full wing gestures: all 14 wing meshes move as
  assigned, fixed root drift is zero, neutral restores exactly, feet/perch clear.
- Exactly three front and one rear branch per foot, eight actual claw/bar
  contacts, supporting pads and 45 independent foot collision pairs remain.
- Independent technical review repeated the complete actual runtime dataset,
  added five quarter/mixed gesture states and checked all 48 neutral leaves
  against all 13 foot/perch surfaces.

`verification.json` records 59 source files, nine references and 57 own evidence
files. The additional strict gate checks complete typed recursive inventories,
actual worker JSON equality and decoded image bytes. Independent omission tests
rejected 7,122 nested omissions and eleven semantic corruptions. The separate
`review.json` binds 17 final report/check/view files and every commissioned
criterion; automatic proof retains `design_approval=false`.

## Reproduction and integration

Run from the repository root with Blender installed and LFS materialized:

```powershell
python scripts/feathers_review.py --work tmp/goal6/reproduce-new --output validation/reviews/feathers_v01 --scene-output blender/scene/owli_feathers_v01.blend
python scripts/project.py validate
python scripts/feathers_gate.py
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/project.py doctor
python scripts/project.py smoke
```

The first command deliberately publishes new own evidence; use a new work
directory and independently review/rebind any regenerated delivery. It protects
all predecessors and refuses other publish targets. Read-only admission and
tests do not require rerendering historical scenes. The generic complete smoke
runs stages00..90 in an isolated directory, including actual stage30 before feet.
The dedicated #6 producer instead starts from the accepted #37 scene.

Final local integration results and logs are recorded in `integration-checks.md`.
Windows/Ubuntu CI additionally runs the new feathers gate with prior validation,
tests and compileall; it does not install Blender. PR/merge references are the
published GitHub delivery record, rather than an invented commit inside proof.

## Limits and next goal

Mesh audits retain relative median triangle inset 1e-3, coplanar overlap area
1e-12m2 and plane tolerance 1e-8m. Intended inter-part overlap is not an assertion
of zero intersections throughout the avatar. Root seating and pad contacts are
geometric checks, not pressure physics. Pose samples do not establish arbitrary
combined animation safety. Full combined topology/rig QA remains #20–#24.

Next is #18: actual assigned non-eye materials, editable forehead motif and
restrained perch accents. Eyes follow #19; rig and animation follow later.
The current scene retains diagnostic materials and geometric probe APIs.

## Additional independently produced machine evidence

The final manual decision binds this report, which records these actual-byte
SHA256 anchors for the published independent and integration evidence:

- `independent-technical-evidence.json`: `d50f70cd38df065e0eeb92c3123e53042e1f044d1726767045782254a6070c60`.
- `run12-review-bindings.json`: `583174488046fd7ae8662f25427d05d88715f2c12fd806bc2697199469b3eddf`.
- `run12-readonly-open.json`: `e9eb9b0968754623f2452c744c0d599e74771f233c8a7b9a5e53f49135cb36e5`.
- `integration-checks.md`: `7dfea3dcaabec1b6b6b5b88a4f020d651684c5f3ee5e3a78be2017ee98ecc3c3`.
