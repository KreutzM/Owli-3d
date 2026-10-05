# Independent technical review — Goal #18 / F-01

The actual delivered candidate passes independent technical review for assigned
non-eye materials, editable forehead/perch geometry and the F-01 chest changes.
This verdict applies to Blend SHA256
`ca5522b3948e2d3501eb47c0b0f3099a7ca9d7e596e8e9af5b9f6128353acaa3`.
Final publication/evidence bindings are recorded in the companion machine evidence.
Eyes/F-03 remain #19; nostrils/F-02 remain #40. This is an intermediate production
goal and grants no full avatar, rig, animation or final topology acceptance.

## Independent actual artifact work

The reviewer followed AGENTS' eight-source reading order, handoff, continuation
plan and current #18/#40 issues and actually viewed references 00, 07 and 08.
Forensic scratch writes stayed under `tmp/goal18-technical/`; the reviewer also
wrote the two named final technical report/evidence files. Accepted history and production code were
read-only; the final Blend was copied into an isolated review directory. A fresh
Blender 5.2.1 process captured a separately authored state snapshot, followed by
another fresh process on the exact final published scene actually executing `materials_checks.inspect/exercise`
and the additional probes described below. Scene bytes were never saved or changed.

The result contains 117 objects, 103 actual meshes, 14 saved materials, no armature
and no actions. The three unused predecessor diagnostic materials are pruned on
save; all four diagnostic materials assigned to the eight eye layers are intact.
The live repeat build has 17 materials before unused datablocks are pruned.

The independently authored geometry snapshot and the production helper produce
the same geometry-only digests. All 78 retained predecessor mesh states are exact:
vertices, edges, polygons, smooth flags, world/parent-inverse transforms, parents,
groups/weights, modifiers and collections. The only changed old cages are the
eight named CreamUpper/Middle/Lower and Orange leaves. All nine old BLK forehead
guides are replaced by the 17 commissioned TECH meshes. Five original pivots,
four cameras and five lights remain exactly unchanged.

All eight globe/iris/pupil/cornea objects, meshes, material slots, polygon slot
indices and assigned diagnostic material/node states match the independent
accepted-scene snapshot. The iris retains its original two slots. Datablock user
counts are excluded as bookkeeping, not authored shader settings. All 18 actual
inspection/function fields independently reproduced the final published canonical worker data exactly.

## Materials, editable geometry and actual function

Every visible non-eye mesh has actual MAT slots with valid polygon indices and
an active, connected, unmuted Principled/output graph. Authored feather UV maps
exist, cover the complete V range and contain finite coordinates in [0,1]. The
ten role graphs include actual connected grain/bump treatment; perch grain and
anisotropy are present. Palette and gradient colors use explicit sRGB-to-linear
conversion. Feathers/body are nonmetallic, satin/matte; cream roughness is 0.64,
beak/claw keratin roughness 0.30, perch metallic 0.85/roughness 0.30, and cyan
emission strength 2.0. Separate eye shaders remain diagnostic for the next goal.

Seven forehead nodes, six seated links and four perch rings are separate editable
meshes. Their cages and evaluated surfaces pass connected/manifold, outward,
nondegenerate, duplicate-vertex and interior-triangle/coplanar audits. The four
closed rings correctly have genus one/Euler zero, rather than a sphere topology
claim. Five paired TECH surfaces are actual exact reflections; every new mesh
has measured support proximity. All 48 feather roots and original gesture/root
bindings remain checked, including the eight intentionally reshaped chest leaves.

The independently executed function dataset includes the actual full 41-state
blink, 10,034 full-closure rays, zero meeting-seam gap and 1.024827mm minimum
lid/cornea clearance; four ±12° gaze endpoints; 41 beak states over 0–18°; and six
isolated/combined half/full gestures. The original 51 feathers and every one of
the 17 new TECH meshes are enumerated as moving-face/wing collision targets.
TECH coverage includes 2,788 lid pairs, 1,394 beak pairs, 136 eye pairs per gaze
state and 238 wing pairs per gesture. Exactly 3+1 toe branches on each actual foot,
eight claw/bar contacts, supporting pads and 45 independent foot collision pairs
remain unchanged. Every neutral restoration is exact.

Additional reviewer probes check all 51 FTH surfaces against all 13 foot/perch
and 17 TECH surfaces at neutral (1,530 pairs), plus five quarter/mixed gestures
at (.25,0), (0,.25), (.25,.75), (.75,.25), (.75,.75), each with 420 wing/foot/TECH
pairs. No intersections were detected. The reviewer actually viewed all four canonical run02 images; each published
image has exactly matching decoded RGBA pixels. Independent visual acceptance
is a separate review.

## Gate and historical evidence review

An independent script compared all 548 protected entries against actual Git
`a8634936494512d64e311149f20ed4e24ea492ac` blobs or true LFS OIDs/sizes and the
current materialized bytes: zero failures. The archived original stage50 is
separately required to match its exact predecessor Git blob. No historical
scene, source, image, approval or source-bound proof was rewritten.

Independent adversarial checks reject 7,998 nested dictionary-field omissions,
1,316 sequence truncations and 27 meaningful shader/assignment/eye/anatomy/
topology/support/studio/function corruptions on the actual build dataset.
G18-TECH-01 found that a contradictory negative per-sample blink clearance could
previously pass while its aggregate minimum stayed positive. The gate now requires
all 164 actual sample minima to meet 0.30mm and the aggregate to agree with their
true minimum within 1 nanometer. The unchanged real scene passes; the negative
case and inconsistent aggregate case are rejected. This finding is closed.

## Reproduction and limits

The companion evidence binds the exact read-only review commands, independently
produced snapshot/check/history/gate evidence and final published scene/views.
The scratch command is:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe' --background tmp/goal18-technical/final-run03/candidate.blend --python-exit-code 1 --python tmp/goal18-technical/fresh_review.py -- tmp/goal18-technical/final-run03/fresh-review.json
python tmp/goal18-technical/history_audit.py tmp/goal18-technical/final-run02/history-548.json --materials
python tmp/goal18-technical/negative_worker_audit.py
```

Historical triangle-interior tolerances remain relative inset 1e-3, coplanar area
1e-12m² and plane distance 1e-8m. Intended support embedding and inter-layer
overlap are classified attachments, not zero overlap throughout the avatar.
Finite pose samples are not arbitrary combined rig or animation safety proof.
Full topology/combined deformation QA belongs #20–#24. F-02 and F-03 remain open.

Final delivery is `blender/scene/owli_materials_v01.blend`, 1793740 bytes. The companion `independent-technical-evidence.json` has SHA256 `84aa2680a7479d7fb3b24d79839b485d506c02e5eb44f476289dd70f1bbc1579`. It records the actual final-scene runtime data, complete independent Git/LFS audit, own negative checks, source/reference/artifact hashes and four decoded RGBA comparisons.
