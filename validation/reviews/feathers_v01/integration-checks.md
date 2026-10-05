# Final local integration checks — 2026-10-05

All commands below actually exited 0 on the final run12 production sources and
parameters. The smoke used its isolated working directory; it did not overwrite
the accepted scenes. Production source/scene hashes were checked after tests.

| Command | Result | Actual normalized UTF-8/LF log SHA256 |
|---|---|---|
| `python scripts/project.py validate` | PASS | `134e362fa4246889321d8c8f96f2fe6596562ae03b695b7d9839b0d6ef8155ae` (`logs/final-validate.log`) |
| `python scripts/feathers_gate.py` | PASS: final exact-scene decision and all predecessor gates | `f8940c90185c1e6b9d30feec9002cc7ff517ed203157e896f808ea74e259d60b` (`logs/final-gate.log`) |
| `python -m unittest discover -s tests -v` | PASS: 64 tests | `8989ff264fc1b4138c5038510952600734e422076a1557a820b80a925d6e3cce` (`logs/final-tests.log`) |
| `python -m compileall -q scripts` | PASS | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` (`logs/final-compile.log`) |
| `python scripts/project.py doctor` | PASS: Blender 5.2.1 LTS and nine references | `ed7329977d8b398bb545a6be22d3e92fdc8af94bda8568165e1a423c05e51f7f` (`logs/final-doctor.log`) |
| `python scripts/project.py smoke` | PASS: complete stages00..90, actual stage30, feet and four renders | `49ee90d641660b6087196bda818258972c2c8668f6ceb74dcf1dab53c5ee080a` (`logs/final-smoke.log`) |


The 64-test suite includes 19 new feathers structure/delivery tests plus the
45 historical checks. It verifies incomplete inventories, nested missing values,
physical root claims, false pose/geometry claims, exact manual-review bindings
and actual pixel corruption. Blender runtime checks and two independent reviews
are separate real evidence, not assertions supplied by the Python unit tests.

External Windows/Ubuntu CI and the exact-head PR merge are recorded in the
GitHub PR/issue delivery; this local file does not pre-claim their result.
