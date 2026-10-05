# Independent technical acceptance — Goal #6

**PASS for the actual corrected run12 feather geometry and technical evidence.**
G6-TECH-01 is independently resolved by changed geometry and measured root seats.
No open technical blocking findings remain in the reviewed #6 scope.

Final reviewed scene: `blender/scene/owli_feathers_v01.blend`, **1,385,718 bytes**,
SHA256 `76ee3f1c0f8b4314aee40585445c14e3b2d193b7aa04c7e2c86e6f810f576b0a`.
The reviewer copied the actual run12 scene to its own scratch directory and
executed fresh read-only Blender 5.2.1 LTS (build `9e2066aef7ef`) inspections and
functional probes. No scene save or production file edit occurred.

## Actual independently executed checks

- Fresh `feathers_checks.inspect` and `exercise` both pass. The complete
  independently produced runtime dataset exactly equals the published
  saved-build, reload-A, reload-B and declared canonical dataset.
- Actual scene: 109 objects, 95 meshes, 51 new meshes, 48 broad closed quad feather
  groups, no armature/actions. Commissioned wing, body, tail and six cream-face
  regions are real editable geometry; three center groups close central gaps.
  Mirrored pairs are actually measured against reflected vertex coordinates.
- All 44 retained #37 meshes match the independently inspected baseline digests
  exactly. Retained parents, vertex-group names, collection memberships and world
  matrices, including all original pivots, remain exact.
- Every new cage/evaluated surface is closed, connected, outward, nondegenerate
  and passes adjacent/coplanar triangle-interior checks. Actual maximum new cage
  triangle inset is 11.747 micrometers. Wing primaries have real shoulder seats,
  each with 465 fixed vertices and measured intended torso embedding.
- Six actual isolated/combined half/full gestures execute. Every assigned wing
  and layer responds, fixed shoulder vertices stay fixed and neutral returns
  exactly. Five independently added quarter/three-quarter/mixed states confirm
  the common nonlinear deformation field at every actual wing/layer vertex.
- All 41 nonlinear blink states pass, with 1.024827mm minimum actual lid/cornea
  clearance, 10,034 full-close coverage rays and zero front/back meeting-seam gap.
  Four actual X/Z +/-12-degree gaze states pass. All 41 actual beak states cover
  0–18 degrees, preserve the upper jaw and visibly lower the hinged jaw.
  Existing mask/jaw sampled clearance is 7.247007mm across 2,091 old-part pairs.
- Expanded checks against every one of the 51 new meshes pass: 8,364 lid/feather
  checks, 4,182 beak/feather checks, and 408 eye/feather checks per gaze state.
  This includes the changed cream roots and three new central groups.
- Real foot verification preserves exactly three front/one rear connected
  branches per foot, all eight claw/bar contacts, supporting pads and 45
  independent foot pairs. Additional independent neutral checks cover all 48
  feather groups against all 13 actual foot/perch surfaces with no intersections.
  Each of the six gesture states checks all 14 wing meshes against those surfaces.
- All four published/neutral/reload-A/reload-B images independently decode as
  1024x1024 RGBA with identical pixels per fixed view. This independently compares
  actual image data, not metadata assertions. No independent render is claimed.

## G6-TECH-01 resolved through actual attachment geometry

Run09 had raised face root rows and wholly separated tail leaves despite a
blanket root-embedded property. That finding was sent before acceptance. Run12
anchors the authored face/tail spines to actual support ray hits and smoothly
eases their shape away from the seated roots. Actual supporting object names
are retained and checked in the proof.

All 48 leaves now have measured front root samples within the 1.5mm limit and
actual back-root embedding beyond 0.1mm. The worst front-root distance across
all leaves is **0.780121mm**; the least deeply embedded leaf still has a back
sample **0.131826mm** inside its real support. Independently rechecked outer
cream roots are at most 0.211038mm/0.193128mm from the accepted right/left support,
cheek roots at most 0.321422mm, bridge roots at most 0.378311mm. Every tail leaf
now seats on the actual tail primary. These checks also cover the three center
groups; the previous floating-root discrepancy is closed.

## History and admission evidence

The reviewer independently fetched actual Git blobs at accepted predecessor
`966b7f02489ebad4890ba17a6c64f4c03adc2803` and compared all **462** protected
current files against raw blobs or true LFS OIDs/sizes. All pass. Old stage30
archive matches its actual Git blob byte-for-byte; the old interim provenance
manifest and prior approval data remain untouched.

All **59 source / nine reference / 57 own evidence** hashes match actual bytes.
Declared build equals actual worker JSON; three canonical JSON files equal each
other and the independently executed fresh Blender dataset. The new admission
schema rejects **7,122** independently traversed nested-key/sequence omissions.
Eleven independent semantic corruptions reject: duplicated gesture, missing
target, stationary primary, root drift, incomplete collision count, altered old
mesh, malformed hash, floating leaf root, zero embedded samples, wrong support
and shortened root samples. Complete inventories are code-owned and recursively
typed, including legitimate null parents/empty modifier lists.

This report is the independent technical acceptance artifact. The final combined
admission call, full suite, CI and exact-scene visual decision are owned by the
primary agent and must be bound after these review reports are copied; no claim
that those later integration steps had already completed is made here.

## Independent evidence and reproducible commands

Reviewer's scratch directory: `tmp/goal6-technical/`.
Actual run12 evidence: `run12/independent-scene-evidence.json`,
`run12/independent-attachments.json`, `run12/independent-delivery-evidence.json`,
`run12/blender-inspect.log`. JSON records name the exact scene, reviewed source
hashes, all runtime data, Git/LFS anchors, decoded pixel hashes and negative errors.

Commands actually executed on the separate copy:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe' --background tmp/goal6-technical/run12/candidate.blend --python-exit-code 1 --python tmp/goal6-technical/final_inspect.py
& 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe' --background tmp/goal6-technical/run12/candidate.blend --python-exit-code 1 --python tmp/goal6-technical/attachments_inspect.py
python tmp/goal6-technical/audit_delivery.py run12
```

All exit 0. Copied scene bytes remain unchanged. The completed run12 fresh process handle was revalidated after the session usage reset; the actual independent dataset and exact scene/source hashes match the current final delivery. The changes to central widths, depth offsets and middle-layer tips were included in that complete fresh inspect/exercise, root/foot checks and current pixel audit. Consolidated durable machine evidence is `independent-technical-evidence.json`; it contains all actual records and reviewer script hashes.

## Limits and later assigned scope

This is technical acceptance of a geometric feather milestone; visual reference
acceptance is separate. Inherited triangle-audit tolerances remain 1e-3 relative
median inset, 1e-12m2 coplanar overlap area and 1e-8m plane tolerance. Inter-part
root seating and designed feather overlaps are intentional, not a claim that the
whole avatar contains zero intersecting surfaces. New function probes detect
actual surface intersections; inherited minimum-clearance numbers apply to the
original lid/cornea and mask/beak relationships, not an unmeasured universal
clearance for every added leaf.

Root seating is geometric attachment, not pressure physics. Sampled wing gestures
and nonlinear lids are probe APIs with rest geometry, not final avatar controls
or an arbitrary combined animation proof. Body/tail/face rig bindings, full
combined deformation, complete topology, shaders and animation retain their
assigned #18–#24 owners. Existing old CLI/source helpers remain byte-exact;
new `feathers_gate.py` supplements historical `project.py validate` in CI.
