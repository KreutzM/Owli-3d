# Owli 3D — GPT-6.1-Sol instructions

## Mission

Create a production-ready stylized 3D character of **Owli**, the Owli-AI brand mascot, in Blender.

V1 is a perched avatar. Owli does not need to fly.

## Required reading order

1. `DESIGN_FREEZE.md`
2. `CHARACTER.md`
3. `design/reference_hierarchy.json`
4. `design/character_spec.json`
5. `design/materials.json`
6. `design/rig_spec.json`
7. `references/manifest.json`
8. `validation/checklist.json`

After this required sequence, read `docs/agent-handoff.md` for the latest accepted
scene, remaining goals, reproduction commands and historical evidence constraints.
For the next open production goal, also read its linked GitHub issue and the
corresponding continuation plan; do not restart completed milestones from scratch.

## Sub-agent workflow

Use sub-agents for independent visual and technical reviews of substantial
modeling, lookdev, rigging, animation, and milestone-QA goals. This is an explicit
delegation instruction for those goals, within the active session's capabilities
and higher-priority rules. The primary agent chooses the task split and timing.

- Assign separate visual and technical reviewers before milestone acceptance.
  The visual reviewer checks the actual four required views against the approved
  reference hierarchy. The technical reviewer checks relevant geometry/function
  probes, reproducibility, evidence bindings, and preservation of historical
  artifacts. Both return concrete findings, supporting evidence, and limitations.
- Give each sub-agent a bounded task, the accepted scene/commit, relevant goal
  criteria, and explicit file ownership. Each must follow the required reading
  order and continuation plan. Reviewers inspect actual artifacts independently
  and write only their own reports or scratch outputs unless separately assigned
  implementation work.
- Delegate implementation only when tasks have clearly separate files or
  artifacts. Keep one writer per Blend file and production script at a time;
  coordinate ownership before transferring work. Use separate working copies
  and scratch directories for Blender probes and renders.
- The primary agent integrates changes, evaluates and resolves findings, runs
  the combined checks, and owns the final acceptance and handoff. A sub-agent's
  verdict does not replace reference comparison or the iteration requirements.
  Bind reviews to the final delivered artifacts; recheck affected scope after
  subsequent changes and document any remaining work in a named goal.

Small, isolated edits do not require delegation. If sub-agents are unavailable,
document the review limitation without claiming an independent review occurred.

## Reference authority

When visual references disagree, use this priority:

1. Original logo: brand identity, face language, color identity.
2. Final technical turnaround: body volume, silhouette, side/back interpretation.
3. Final technical parts/lookdev sheet: eyes, beak, claws, feather layering, material intent.
4. Approved beauty views: character, styling, 3/4 read.
5. Older concept sheets: supporting only.

Do not average conflicting references. Follow the higher-ranked source and document the choice.

## Character invariants

- Owli is a small, friendly, intelligent tech owl.
- Organic/stylized owl first; technology is integrated, not a robot shell.
- Large expressive blue/cyan eyes are the primary facial feature.
- White/cream facial mask must remain strongly readable.
- Deep navy + blue/cyan feather family.
- Orange beak and controlled orange chest accents.
- Cyan emissive network symbol centered on forehead.
- Wings rest against the body and must later support simple explanatory gestures.
- Each foot has exactly **4 toes/claws: 3 forward + 1 rear**.
- V1 sits naturally on a perch.
- No flight geometry/rig complexity unless explicitly requested later.

## Modeling policy

Work coarse-to-fine:

1. scene and scale;
2. head/body blockout;
3. eyes and beak;
4. wing masses;
5. feet and perch;
6. silhouette validation;
7. large feather layers;
8. materials;
9. clean topology;
10. rig;
11. expressions/animation.

Do not model hundreds of individual feathers. Use clean primary volumes plus designed feather groups/layers.

## Geometry

Prefer:
- clean editable topology;
- symmetry while the design is symmetric;
- separate eyes, cornea/iris components, beak, wings, feet, claws, forehead-tech geometry;
- grouped feather cards/meshes for major visible layers;
- topology that deforms cleanly around eyelids, beak base, wing root and neck.

Do not hide design decisions only inside manual Blender state. Put reusable parameters in scripts or documented JSON.

## Materials

Use physically plausible stylized materials:
- feathers: satin/matte, not plastic;
- eyes: glossy, layered, deep;
- beak/claws: keratin-like semi-gloss;
- forehead symbol: subtle cyan emission;
- perch: brushed metal with restrained cyan light accents.

Avoid excessive metallic surfaces on Owli herself.

## Rigging requirements for V1

Required:
- root/body;
- head/neck;
- left/right eye aim;
- blink/eyelid control;
- beak open/close;
- left/right wing gesture controls;
- leg/foot placement;
- optional toe curl for perch grip;
- optional secondary feather motion.

Deferred:
- flight rig;
- full wing flight articulation;
- complex cloth/feather simulation.

## Validation

Every milestone must be compared against approved references using:
- front;
- left profile;
- back;
- 3/4 front.

Do not change cameras to hide modeling errors.

## Design freeze

Do not generate new concept art by default once blockout starts.
Only create a new design reference if an actual 3D ambiguity cannot be resolved from approved material.

## Iteration definition of done

An iteration is complete only when:
- scripts run without errors;
- reference hierarchy was respected;
- no undocumented anatomy/material changes were introduced;
- 3+1 toe rule is preserved;
- silhouette was checked in the required views;
- uncertainties and deviations are written down.
