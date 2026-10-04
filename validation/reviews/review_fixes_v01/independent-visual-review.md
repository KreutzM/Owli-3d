# Independent visual and targeted technical review: Goal #37

Reviewer: `/root/goal37_visual_review`, 2026-10-04. The reviewer did not implement
or modify the scene, parameters, production scripts or Git state. This report is
the only file written by this reviewer.

**Verdict: pass for the #37 primary facial-form scope. IR-01 is materially
resolved in the inspected current scene; residual facial feather flow and cream
boundary finishing remain explicitly assigned to #6. This is not final V1 approval.**

## Exact reviewed inputs

| Input | SHA-256 |
|---|---|
| `tmp/review-fixes-37/run05/candidate.blend` | `f6f3e176f02bcb4dffb2ae208f85b604e4773fdc7a9a3fbad9f7a3414f89906a` |
| `scripts/blender/review_fixes_geometry.py` | `cb8f557dbbb7c825d11264fb59856e43d3c9f079e71d8d94156d5f83f4662c5d` |
| `design/review_fixes.json` | `59dc780738e4e0a26e3e430ecc4c14cf3eda36b6d29cf4689f7ccaecb9824c3a` |
| `scripts/blender/review_fixes_checks.py` | `8f1e0d3c8bc2f636b6999960e61cced361e1eb427bfee4d4a9b822f6a86e5de6` |
| `run05/renders/neutral/VAL_FRONT.png` | `88592551cbd55a9261e0733f8d17b6deadb8e6084b2a80a839d0b53a46d42bf4` |
| `run05/renders/neutral/VAL_LEFT.png` | `aeceab711202a226f12b6cb12bfe36e22d167bd685230371244b95fe67c55777` |
| `run05/renders/neutral/VAL_BACK.png` | `1e526f4df0b6fb6dbe5d425b2fa26b284ded32b791cd87a55dcd33333bcdbef0` |
| `run05/renders/neutral/VAL_3Q.png` | `2e183b9c6a8eda29632ba3408b80f576092ead29c3a571ae17cc8732d85a277b` |

The four PNG paths above share prefix `tmp/review-fixes-37/`. The scratch
`run05/design/review_fixes.json` was separately hashed and matches the repository
parameter hash above.

## Visual review actually performed

Read the eight required design documents in order, the current handoff, IR-01 in
`docs/reviews/independent-interim-after-feet.md`, the new geometry recipe and
parameters. Actually viewed approved references 00, 07 and 08; all four accepted
`validation/reviews/feet_v01/VAL_*.png`; all four earlier 64% previews; and all four
current 1024px images listed above. Current images supersede the provisional
preview assessment.

Authority: logo 00 determines identity and face language; 07 determines volume
and profile; 08 supports part construction. Their differences were not averaged.

- **Front:** broad cream cheeks now extend beyond the narrow circular sockets;
  the lower central cream connection and wider upper center create a coherent
  facial area. Raised, tapered brows remove the former horizontal stern bars.
  Large blue/cyan eyes remain dominant. Neutral expression is more attentive and
  friendly. Functional inner eye/lid rings are still visible, but no longer form
  the entire white facial silhouette.
- **Left:** cream surface sweeps backward into the actual head rather than ending
  as the previous thick, nearly vertical ring. The visible lateral boundary is
  still abrupt, and this smooth primary surface is not a finished feather face.
  It is nevertheless a genuine volume and attachment correction, not a shader
  promise.
- **3Q:** broad cheek area, central cream connection and receding lateral root
  materially reduce the detachable-goggle read. Beak projection and both eyes
  retain clear volume. The cheek/bridge junction remains visible and needs the
  explicitly assigned large facial feather flow from #6.
- **Back:** head/body/wing/tail hierarchy and perched pose remain visually stable.
  No new rear facial protrusion or flight geometry is apparent. This image
  comparison alone does not prove byte-equivalent geometry.

The remaining upper contour peaks, outer cream edge and cheek/bridge transition
are appropriate named finishing work. `docs/review-fixes-qa-followup.md` assigns
large editable facial feather groups and edge/flow finishing to #6 while
preserving the new primary mask and rechecking blink/gaze/beak. The associated
continuation plan was read. Final shaders and full body feathering remain later
milestones; their absence does not invalidate this primary-form review.

## Independent Blender execution actually performed

A separate Blender 5.2.1 LTS process (build `9e2066aef7ef`) opened the exact
candidate, imported current `review_fixes_checks`, and ran `inspect(root)` plus
`exercise(root)` with `root=tmp/review-fixes-37/run05`. Exit code **0**. The process
did not save the scene or render new images. Before/after assertions proved all
50 mesh digests restored, studio snapshot unchanged, and candidate file SHA-256
unchanged.

Executed from the repository with the following Python expression supplied to
Blender's `--python-expr`; this is executable reviewer provenance, not a claim
that a new test algorithm was independently designed:

```python
import sys, json, hashlib
from pathlib import Path
import bpy
sys.path.insert(0, str(Path("scripts/blender").resolve()))
from review_fixes_checks import inspect, exercise
from verify_face import digest_part
from validation_setup import studio_snapshot
root = Path("tmp/review-fixes-37/run05").resolve()
scene = Path(bpy.data.filepath)
original = hashlib.sha256(scene.read_bytes()).hexdigest()
before = {o.name: digest_part(o) for o in bpy.context.scene.objects if o.type == "MESH"}
studio = studio_snapshot()
result = inspect(root)
movement = exercise(root)
assert before == {o.name: digest_part(o) for o in bpy.context.scene.objects if o.type == "MESH"}
assert studio == studio_snapshot()
assert original == hashlib.sha256(scene.read_bytes()).hexdigest()
print(json.dumps(dict(scene_sha256=original, mesh_count=len(before),
                     changed_mesh_audits=result["changed_meshes"],
                     attachment_contacts=result["attachment_contacts"],
                     feet=result["feet"], movement=movement,
                     geometry_restored=True, studio_unchanged=True,
                     scene_bytes_unchanged=True)))
```

Launch used `C:/Program Files/Blender Foundation/Blender 5.2/blender.exe
--background tmp/review-fixes-37/run05/candidate.blend --python-exit-code 1
--python-expr ...`. Tool session 15791 completed successfully. The original
machine output was 4,786 tokens; displayed output was truncated, so this report
does not pretend to preserve its complete JSON.

Successful assertions cover five changed closed connected outward-facing
meshes, cage and evaluated triangle interior/coplanar checks, mask root-distance
limits, and the existing actual 3+1 foot/contact inspector. Blink probe ran 41
states: minimum clearance **1.0248268 mm**, **10,034** closed-coverage rays, zero
front/back closure seam gap, and four ±12-degree gaze probes. Beak probe ran 41
opening states with **2,337** collision checks; minimum sampled mask clearance
**7.2470065 mm**, fixed upper jaw, maximum lower-jaw displacement **21.5019036 mm**.

## Limits

The current visual verdict applies only to the exact hashes above. A later
geometry or parameter change requires another actual render review. Reused probe
algorithms have documented finite-sample, inset and tolerance limits; this is not
a universal self-intersection/continuous-pose/physics proof. No complete final
rig, shader, animation, Linux runtime, history migration, gate mutation or fresh
build reproduction was independently audited by this reviewer. Those scopes
require the parent review's own evidence. No Git/GitHub state was changed here.

## Final artifact acceptance after gate-source regeneration

The host regenerated the delivery as `run06` after gate-only source hardening.
This changed the saved Blend container. The previously reviewed `run05` container
remains the record of the independently executed 41-state probe session above;
its hash must not be presented as the final delivered file hash.

**Final accepted artifact:** `blender/scene/owli_review_fixes_v01.blend`,
**1,068,215 bytes**, SHA-256
**`580b44f0d72be095f90705cf374654a6f6005d368ffe3170803528533a2d8359`**.

The reviewer independently performed the following additional checks, all exit 0:

1. Hashed the actual published artifact, checked its size, and compared its bytes
   directly with `tmp/review-fixes-37/run06/candidate.blend`: identical.
2. Compared the complete parsed `run05/reload_b_checks.json` against both
   `run06/reload_b_checks.json` and the published verification's `reloaded` data:
   exactly equal, including all 50 mesh digests, changed surface/attachment/feet
   checks, studio, pivots, framing and complete movement results. Published proof
   hash and size also match the actual artifact.
3. Compared all four canonical PNGs by decoded RGBA dimensions and bytes against
   both `run06/renders/neutral` and published `validation/reviews/review_fixes_v01`:
   all eight comparisons exactly equal to the four images actually inspected
   above. This is an actual pixel comparison, not reliance on metadata.
4. Compared repository geometry script, geometric check script and parameters to
   the reviewer-captured SHA-256 values above: unchanged. Parameter bytes also
   match both scratch runs.
5. Opened the actual published Blend in a new separate Blender 5.2.1 process and
   computed actual mesh digests, actual studio snapshot and actual Empty-pivot
   matrices. All 50 digests, the entire studio snapshot and all pivot matrices
   exactly match the independently exercised `run05` data. The process did not
   save or modify the artifact.

The final artifact therefore receives the same **pass for #37 primary facial
form / IR-01** as the reviewed run05 scene. Different saved container bytes and
working paths do not establish a model difference; actual loaded geometry and
studio, parameters, complete probe datasets and decoded rendered pixels establish
equivalence here. The reviewer did not rerun the full 41-state movement suite a
second time on run06. Actual loaded model equality, unchanged geometric check
source/parameters and exact complete probe equality support carrying over that
review without claiming a second full probe execution.

Residual #6 face-feather finishing and the broader production/QA limitations
above remain in force. Gate/schema/history completeness is outside this visual
review; this addendum verifies the delivered geometry and evidence continuity.

## Authoritative final artifact: run07 publication cleanup

This addendum supersedes the run06 final-container identification above. A final
producer run07 bound publication whitespace cleanup and normalized durable logs.
The reviewer independently confirms the currently published artifact:

**`blender/scene/owli_review_fixes_v01.blend`: 1,068,211 bytes, SHA-256
`8685fc054428ec848f20a922c995487f9ac4a2797cbe3713eaeb5e364b02e8fb`.**

Actual artifact bytes exactly equal `run07/candidate.blend`; published proof
scene hash and size match them. The reviewer separately opened that exact run07
container in a fresh Blender 5.2.1 process without saving. All 50 actual mesh
digests, actual studio snapshot and all actual Empty-pivot matrices equal the
independently exercised run05 data; exit **0**. After publication, direct byte
comparison proves the published file is the same container just opened.

Complete run07 saved-build and reload-b datasets, and current published
`verification.json`'s `reloaded` dataset, exactly equal the prior reviewed run05
reload dataset, including geometry, attachments, feet, framing and movement.
All four canonical and all four published images were independently compared
against the actually viewed run05 images by decoded RGBA dimensions and bytes:
all **eight** comparisons identical. Geometry recipe, geometric checks and
parameters still have the captured source hashes above; repository and both
scratch parameter files remain byte-identical.

The **pass for #37 primary facial form / IR-01** therefore applies to this final
run07 artifact and its current published images. The run05 full movement suite
was actually executed once by this reviewer; run06/run07 equivalence checks do
not claim additional executions of that suite. Container save changes and
publication cleanup are acknowledged rather than hidden. Deferred #6 face-edge
and feather-flow finishing, final V1 production work and the review scope limits
remain unchanged. Only this temporary review document was modified here.
