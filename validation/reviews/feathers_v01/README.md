# #6 — broad feather geometry evidence

This directory is the new feather milestone, starting from the accepted #37
scene. Acceptance requires `verification.json`, the separately written
`review.json`, the report and two independent review reports. File existence
alone is not acceptance; check the current gate and recorded review status.

Reproduce only into a new explicit scratch directory:

```powershell
python scripts/feathers_review.py --work tmp/goal6/reproduce-new --output validation/reviews/feathers_v01 --scene-output blender/scene/owli_feathers_v01.blend
python scripts/project.py validate
python scripts/feathers_gate.py
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/project.py smoke
```

The producer opens a copy of `blender/scene/owli_review_fixes_v01.blend`, verifies
462 protected predecessor files before and after, and publishes only its own
named new scene/evidence. It refuses an existing work directory or any other
publish target. Do not render accepted scenes through the generic renderer.

Four Blender processes build and exercise the actual geometry, then reopen the
saved neutral scene three times. Actual worker JSON and canonical decoded RGBA
pixels must agree. In-process live/pose images are retained separately; they are
not claimed identical to canonical fresh renders. Every image uses the same four
fixed cameras and lighting. `evidence/` includes the predecessor, neutral, full
blink, open beak and left/right/both maximum wing gestures.

`project.py validate` keeps verifying the historical deliveries. The additional
`feathers_gate.py` verifies #6, including complete code-owned source/reference/
protected/evidence inventories, recursive nonempty typed schemas, real worker
data and pixels, and a final exact-scene manual decision. Both run in CI. Historical
source helpers remain byte-exact. The replaced metadata-only stage30 is archived
under `scripts/blender/legacy/30_wings_feathers.py`, anchored to Git `966b7f0`.

Production parameters are in `design/wings_feathers.json`. `feathers_geometry`
builds closed broad quad groups and mirrors their actual geometry. The geometry
probe `set_gesture(root,left,right)` uses values 0..1, up to12 degrees, with the
same nonlinear root field for the primary and visible layers. Neutral comes from
the durable `fth_rest` mesh attribute. This is the preparation for final controls
in #23; materials, complete rig and animation remain their later goals.
