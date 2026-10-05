# Materials milestone evidence

Read `report.md` for scope, actual checks and limits. `verification.json` binds
the exact scene, 68 sources, nine references, 548 predecessor files and 58
producer evidence files. `review.json` is the separate manual scene decision.
Independent visual/technical reports and machine evidence describe actual
fresh Blender review work.

Four canonical PNGs and their reference boards use the fixed validation studio.
`chest_before_after.png` adds same-crop F-01 comparison against00/08.
`evidence/` preserves baseline, live neutral, blink, beak open, wing gestures,
saved-build neutral and two fresh reload views. Canonical neutral/reload RGBA
pixels are exactly equal; live cache-dependent images remain distinct evidence.
Raw JSON/log commands identify real scratch processes, not future instructions.

Default verification is read-only:

```powershell
python scripts/project.py validate
python scripts/feathers_gate.py
python scripts/materials_gate.py
python -m unittest discover -s tests -v
```

F-02 nostrils and F-03 eye lookdev remain open; this is not final avatar approval.
