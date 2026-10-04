# Owli head / neck / torso primary topology — #15

Date: 2026-10-04. Reviewer: Codex, direct visual inspection of the four fixed
reference comparisons, primary wire views and deformation diagnostics.
Scope: #15; parent #4; epic #11. Dependency #3 is merged and closed.

**Decision: the editable primary topology meets #15.** The frozen coarse envelope
is preserved within the documented small topology-refinement tolerances. This
does not approve the final avatar, facial construction, final rig or lookdev.

## Deliverables and reproduction

- [`owli_head_body_v01.blend`](../../../blender/scene/owli_head_body_v01.blend), Git LFS.
- [`20_head_body.py`](../../../scripts/blender/20_head_body.py) and
  [`primary_geometry.py`](../../../scripts/blender/primary_geometry.py).
- [`head_body.json`](../../../design/head_body.json): ring density, envelope blend,
  subdivision, weights, pivot, movement probes and comparison limits.
- [Four-view contact sheet](contact_sheet.png), four original 1024px renders,
  reference comparison boards and [render manifest](render_manifest.json).
- [Verification](verification.json): actual mesh audits, rebuild/scale/deformation
  checks, unchanged-part hashes, fresh-open checks, silhouettes and source hashes.
- [Manual decision](review.json): all three #15 criteria with reasons and hashed
  visible evidence; CI rejects a stale or incomplete decision.
- `evidence/topology/VAL_*.png`: isolated primary control cage in all four cameras.
- `evidence/head_tilt/`, `head_turn/`, `wing_root_L/`, `wing_root_R/`: four fixed
  wire views for each actual cage deformation test. These are diagnostic poses,
  not alternate approved character designs.
- `evidence/baseline/{full,primary}/` and `evidence/candidate/{full,primary}/`:
  alpha images for bidirectional frozen-envelope silhouette comparison.

Run from repository root:

```powershell
python scripts/head_body_review.py
python scripts/project.py validate
python -m compileall -q scripts
python -m unittest discover -s tests -v
python scripts/project.py smoke
```

Blender 5.2.1 LTS, Python 3.11.9, Pillow 12.2.0. The runner also accepts
`--blender "C:/.../blender.exe"` or `BLENDER_EXECUTABLE`. It verifies the #14
freeze before building, works in an isolated fixture, and publishes after real
Blender checks and independent fresh scene openings pass. No old blockout/studio
artifact is replaced. Reports and manual decisions are not auto-approved.

## Acceptance audit

| #15 criterion | Decision and direct evidence |
| --- | --- |
| Clean symmetric primary forms, meaningful topology, consistent scale/orientation, no unintended inner surfaces or duplicate vertices | Pass. One 4,480-quad connected head/neck/torso shell replaces the two internally capped overlapping source masses. Four additional closed quad brow/tuft forms total 3,520 quads. Control and subdivided meshes pass manifold, genus-zero connectivity, outward winding, nonlocal self-intersection and duplicate-vertex checks. All five forms have identity transforms and maximum valence four. Symmetry is checked in the actual coordinates. Rebuilding retains geometry and datablock counts; a full 0.8 global resize is checked and restored. [Front wire](evidence/topology/VAL_FRONT.png), [back wire](evidence/topology/VAL_BACK.png), verification JSON. |
| Neck and wing roots allow later motion without a rigid robot shell | Pass. The shell has 22 distinct ring levels in the broad body/head transition. Body/head weights sum to one at every vertex. Weighted head tilt 15 degrees, turn 20 degrees and each wing-root displacement 12 mm pass control/evaluated mesh audits without nonlocal self intersections. Edge-length ratios across all probes range 0.7565–1.2503. Wing-root masks affect a soft surface region, without socket cuts. [Tilt](evidence/head_tilt/VAL_FRONT.png), [turn](evidence/head_turn/VAL_3Q.png), [left root](evidence/wing_root_L/VAL_BACK.png), [right root](evidence/wing_root_R/VAL_BACK.png). |
| Four views retain the documented freeze; changes justified | Pass. All four original cameras/light settings remain unchanged. Full and isolated-primary alpha silhouettes pass >=0.99 IoU and <=5-pixel bidirectional axis-distance gates at 1024px. The primary-only minimum IoU is 0.99445; full-character minimum is 0.99818. Dense evaluated primary vertices lie <=1.820 mm from their corresponding frozen surfaces, below the 2.5 mm reference-scale gate. Small cap/neck smoothing and source symmetry noise are documented in decisions.md; no new large-form design decision is introduced. Four reference boards below were directly inspected. |

The cap audit deliberately rejects open meshes, reversed faces, disconnected
vertices and asymmetric cages. All forty deferred mesh/matrix digests remain
unchanged. Exactly three front and one rear toe per foot remain in the delivered
scene. There is no armature, flight geometry or new concept art in this milestone.

## Four-view visual findings and reference authority

Original logo **00, rank 1** remains authoritative for face identity, cream/navy,
large cyan/blue eyes, orange accents and centered forehead landmark. Turnaround
**07, rank 2** governs the silhouette/profile/back envelope. Parts **08, rank 3**
supports organic grouped-feather construction, separate eyes/beak and explicit
3+1 feet. Beauty **01, rank 4** supports the 3/4 character read only. References
are design guides; no view is warped or treated as a metrically exact overlay.

| View | Visual finding |
| --- | --- |
| [Front](VAL_FRONT_comparison.png) | The wide head, swept tuft pair, large eye guides and cream mask keep the frozen face placement. Torso tapers into the seated lower mass; the feet remain exposed appropriately. Wire view exposes an uninterrupted symmetric neck band beneath the face. Brow and mask/chest shading boundaries remain coarse attachments, not neck cuts. |
| [Left profile](VAL_LEFT_comparison.png) | Rounded head depth, beak projection, folded wing envelope, compact tail and rear grip remain at their frozen positions. The neck joins the torso continuously behind the mask. No helmet-like cut or visible hollow socket was introduced. Separate tuft root remains a planned feather attachment. |
| [Back](VAL_BACK_comparison.png) | The head/torso shell now continues through the neck; the navy/blue debug boundary is material indexing, not separate overlapping body geometry. Tufts, wings, central tail and rear toes remain symmetric. Existing cream temple edges await #16/feather integration. |
| [3/4 front](VAL_3Q_comparison.png) | Head/torso volume stays coherent with both fixed-camera reference panels. The opposite lateral technical panel remains unmirrored as specified by the studio. Facial components remain individually editable for the next goal. Small wing/body/chest contact seams are unchanged deferred-volume overlaps. |

All neutral primary wire views show a continuous quad shell and a distributed
cap layout. Tilt/turn views expose bending in the transition rather than rotating
two intersecting closed body parts. Pose diagnostics deform the shell only;
brow/tuft attachment parenting and the full face/wing/perch pose test belong to
the production rig and subsequent geometry stages.

## Verification and limits

The saved scene is opened and inspected in two independent Blender processes.
Both retain identical geometry, studio, topology and deformation reports and
produce pixel-identical canonical four-view renders. The canonical PNGs are
fresh-open renders; an initial in-memory EEVEE build render is not used as the
pixel-identity baseline. The source geometry hash still matches before and after
the review visualizations, which leave no wire modifiers, diagnostic materials,
test poses or rig in the delivered Blend.

Fourteen Python tests, syntax compilation, strict reference validation and the
full scaffold smoke pass. CI repeats stored evidence integrity and silhouette
gates under Windows/Linux; local real-Blender integration provides the topology
and deformation evidence. A green scaffold check alone does not establish this
milestone's visual/topology decision.

Known limits: broad feather roots and brow meshes deliberately overlap the head;
the closed roots are intentional attachment volumes, not unwanted torso/head
inner caps. Mask/eye/lid construction is #16; beak articulation is #17. Wings,
cream chest, orange guides, tail, feet and perch remain coarse. Final feather
layer integration, surface materials, forehead emission and rig are follow-up
goals. These initial soft weights require combined-pose refinement with attached
eyes/mask/brows/tufts/wings; no finished rig or extreme motion range is claimed.
No UVs or final textures are delivered by #15. There are no unresolved blocking
findings within its primary-topology scope.
