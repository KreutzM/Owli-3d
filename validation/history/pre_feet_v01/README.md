# Historical bindings before goal #5

Goal #5 replaces the coarse foot stage and strengthens the project smoke check.
The exact prior stage is preserved in `scripts/blender/legacy/40_feet_perch.py`;
the old CLI source is preserved in `scripts/legacy/project.py` for provenance.
Historical evidence now binds those unchanged bytes instead of today's production
entry points. The coarse branch of today's stage executes the archived foot stage,
so the earlier scene and blockout recipes retain their original geometry.

The manifest records original and relocated metadata hashes. Every changed JSON
record has a byte-exact snapshot here. `scripts/history_bindings.py` proves that
the only JSON changes are source path relocations and the consequent metadata
dependency hashes. Scenes, images, parameters, criterion text, findings and review
decisions are unchanged. This bookkeeping does not approve the new foot geometry;
that requires the separate `feet_v01` review.

The archived CLI is a source snapshot, not the current executable entry point.
Use `scripts/project.py` for current project commands.
