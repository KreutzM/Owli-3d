**Final scoped result: PASS.** All findings G37-GATE-01–05 and the image-metadata consistency point below are independently resolved on the final delivered state. Earlier sections record prior review cycles and superseded source hashes. This is technical gate acceptance for #37; visual geometry acceptance remains the separate visual review.

# Independent technical gate review — Goal #37

Reviewed branch `fix/37-review-findings` against accepted merge `473f8726d32ac7852ef93884b3010b52b8836521`. This review covers `scripts/evidence_contracts.py`, `scripts/delivery_gates.py`, `scripts/history_gate.py`, the `scripts/validate_project.py` integration and changed/new Python tests. It does not approve visual geometry, a future runner or unfinished deliverables.

## Finding G37-GATE-01 — incomplete matched reload values remain accepted

`validate_milestone` enforces complete reload key names and equality with corresponding build values, but does not establish that those values contain the expected evidence. On independent deep copies of the actual accepted proofs, assigning both `proof['build'][key] = None` and `proof['reloaded'][key] = None` returns `[]` for these fields:

- Face: `eye_centers_m`, `collision_pairs`, `toe_rule`, `geometry_sha256`, `studio`, `framing`.
- Beak: `lower_pivot_m`, `opening_axis`, `maximum_open_degrees`, `upper_cap_boundary_vertices`, `lower_cap_boundary_vertices`, `geometry_sha256`, `studio`, `framing`.
- Feet: `geometry_sha256`, `studio`, `framing`.

This is an in-memory omission probe, not a claim that current saved historical proofs are corrupted. The saved proofs contain populated values. Equal missing evidence should be rejected before treating the reload comparisons as complete. Add explicit code-owned field schemas for both build and reload values, including appropriate expected types, nonempty required structures and valid geometry digests, with matched-null and matched-empty negative tests. Existing tests mutate only reload values or delete the build key, so they miss this case.

## Verified strengths and evidence

- `python -m unittest discover -s tests -v`: 35 tests, 36.089 seconds, exit 0, all pass.
- `python scripts/project.py validate`: exit 0, project validation passes with the v2 gates integrated.
- Independently ran raw-byte `git show 84bee42c19e12af090b5d1d741dccf81f7fee800:<path>` for all 14 `PREDECESSOR_SHA256` entries. All SHA-256 values match the actual predecessor Git objects.
- Independently compared 385 protected historical tracked source, scene, render, reference and proof files against merge `473f8726d32ac7852ef93884b3010b52b8836521`. No differences. Real Blend files match their historical LFS pointer SHA-256 OIDs rather than pointer bytes.
- Required inventories exactly match current complete proofs: Face 18 sources / 9 references / 8 reload fields; Beak 20 / 9 / 12; Feet 24 / 9 / 11.
- `history_gate.validate_history` walks the external code-owned inventory even for an empty submitted manifest, verifies byte-exact predecessor archives and snapshots, binds the relocated current bytes, and limits semantic relocation to the known top-level dependency maps. Historical criteria/prose/nested fields stay unchanged. The history omission/corruption tests exercise those cases on real isolated fixture copies.
- Historical producer/validator files remain byte-exact and are explicitly treated as v1 evidence; the current project entry point supplements them with v2 admission gates.

## Reviewed hashes

| File | SHA-256 |
|---|---|
| `scripts/evidence_contracts.py` | `ae6051be976ae5072afde9290a33ee1c16c88280ecf40e7fb693f2fd9f5430b2` |
| `scripts/delivery_gates.py` | `6fcc7dc797bc485c75866c4c0ca364c1a1d6a4875a45f6a9910264ea1c338536` |
| `scripts/history_gate.py` | `f5afb5a9f5dac6b64a556ddc02bf010dee45feb48ef9643d84cd28d8c2e5f32b` |
| `scripts/validate_project.py` | `ae8e28aaaef7828ae84dde6c6f59edeb268c590968d9e404478b3c9faf043d6a` |
| `tests/test_delivery_gates.py` | `4fdcf7538bb8e34841801f7aae3fc15faba8fe749e8720d86dda66397cb6f3a6` |
| `tests/test_history_gate.py` | `48917671eb4c75b8cf16c800d7186e11d3a9407b2687fdf902482b16002e150a` |

## Independent follow-up — recursive schema correction

The added code-owned `delivery_shapes.py` contracts and recursive checks now reject all 124 independently repeated matched-null/matched-empty whole-field mutations (Face 32, Beak 48, Feet 44). Independent removal of every nested dictionary field was also rejected by the recursive schema: Face 1,316, Beak 989, Feet 1,181. The real populated proof shapes are accepted. G37-GATE-01's matched omission case is corrected.

Two remaining follow-up findings were sent to the author:

1. **G37-GATE-02:** matched scalar `geometry_sha256 = 'not-a-sha256'` still returns `[]` for Face and Beak. The digest check looks for `/geometry_sha256/`, but scalar paths terminate at `/geometry_sha256`. Use path components (or an equivalent explicit field contract) and add a matched malformed scalar-digest test. This does not affect nested Feet geometry digests.
2. The full suite currently fails `test_stationary_or_unsafe_opening_is_rejected`: its mutation assigns integer `0` to a float field, so the new shape check rejects before the intended unsafe-opening semantic check. Preserve the semantic assertion and mutate to `0.0` to exercise that check. Full-suite result: 36 tests in 14.776 seconds, exit 1, one failure.

Follow-up reviewed hashes: `delivery_gates.py` = `57fec809dd0244a5adbf157cd2a0310c6a22929ffcbedd1eeda342701a251d61`; `delivery_shapes.py` = `7e68b681b9b375fb09dcecf0efb5fbea49e4c52a5ee3b6d154ca031bc75e3eda`; `tests/test_delivery_gates.py` = `72f00b5c28998c57d92bd6bb2778d4c28013836c240df8e9af696e2c3fd18e83`. Other listed gate source hashes are unchanged.

## Second follow-up — Gate v2 resolved and exact #37 delivery inspected

G37-GATE-02 was corrected using path components for digest-field detection, with matched invalid scalar/map digest negative tests. The Beak semantic regression uses `0.0` and preserves the semantic assertion. Independent focused runs passed all six `test_delivery_gates` tests and all three `test_beak_review` tests.

The new actual #37 scene is a real 1,068,103-byte Blend, SHA-256 `f6f3e176f02bcb4dffb2ae208f85b604e4773fdc7a9a3fbad9f7a3414f89906a`. Independent direct reads confirmed all 50 source, nine reference, 384 protected predecessor and 47 own evidence bindings. All declared build/check data equals the actual worker JSON. Saved-build and both fresh reload snapshots are equal, and match their corresponding build fields. Pillow independently decoded all twelve neutral/reload PNGs: all four views have identical 1024×1024 RGBA pixels across the three fresh processes.

The Git/LFS audit executed independently into `tmp/goal37-gate-independent-history.json`: 14 pre-feet anchors and all 384 protected review files pass against actual predecessor Git objects and actual LFS OID/size bytes. Current actual corner data has all four radius/spacing corners, the midpoint, and all four documented outside-range rejections. The five worker modes all record exit 0. Current movement data contains 41 blink states (minimum clearance 1.024827 mm, 10,034 coverage rays), all ±12° X/Z gaze probes and 41 Beak states (2,337 collision checks, 7.247007 mm mask clearance). All eight claw contacts, two rear claws and 45 independent foot collision pairs are present. Both feet contain pad-support coordinates. All five changed cage/evaluated surfaces have zero reported interior crossings; the four actual adjacency/degeneracy/fold fixtures were rejected.

The current real manual decision passes the new #37 gate and names the correct scene and canonical reference ranks. These current disk artifacts are complete. New gate omissions reproduced on controlled in-memory copies still require correction:

- **G37-GATE-03:** replace the declared allowed corner list with five copies of its first entry and replace the rejection list with four empty objects: `[]`. The gate checks list lengths and positive counters but does not compare the declared corners with the actual bound `foot_corners.json` or enforce distinct required parameter pairs. Require actual-file equality and exact expected allowed/rejected parameter tuples with rejection reasons.
- **G37-GATE-04:** change manual decision `scene_sha256` to 64 zeros: `[]`. Require equality with the accepted proof's actual scene hash.
- **G37-GATE-05:** change the original logo's declared reference authority rank to 5: `[]`. Require canonical 00/07/08 ranks 1/2/3, as the existing Feet gate does.
- Minor metadata consistency: declared render-comparison `size=[]` and `mode='invented'` are accepted even though actual canonical pixels are recomputed correctly. Bind declared mode/size to the actual decoded image metadata.

Status: original Gate v2 findings G37-GATE-01/02 are independently resolved; current #37 disk evidence is complete; G37-GATE-03/04/05 remain semantic admission-gate defects awaiting correction. No visual acceptance is implied by this technical review.


## Final independent acceptance — exact regenerated delivery

Final current scene: `blender/scene/owli_review_fixes_v01.blend`, **1,068,215 bytes**, SHA-256 **`580b44f0d72be095f90705cf374654a6f6005d368ffe3170803528533a2d8359`**. Proof and real visual decision name that same actual scene hash.

Independent current verification:

- `python -m unittest discover -s tests -v`: **45 tests**, 28.401 seconds, exit 0, all pass.
- `python scripts/project.py validate`: exit 0, passes current historical v2 and own #37 admission gates.
- Direct `validate_review_fixes` using current saved proof and current real saved decision returns `[]`.
- Independently repeated all **124 matched-null/empty** historical reload-field mutations: all rejected. Matched malformed geometry digests reject for Face, Beak and Feet.
- Independently repeated every remaining prior own-gate omission: duplicate corners plus empty rejection records, invented image dimensions/mode, wrong visual scene hash and wrong logo authority rank: all reject with the intended semantic errors.
- All **50 source / nine reference / 384 protected predecessor / 48 own evidence** hashes match current bytes. Every real manual-decision evidence binding also matches current bytes.
- Actual build, saved-build, reload A and reload B JSON equal the declared data and corresponding build fields. Current bound `foot_corners.json` equals the declaration; all five exact allowed tuples and four exact rejected tuples/reasons are present.
- Independently decoded neutral / reload A / reload B images remain identical RGBA pixels at 1024×1024 for all four fixed views. Declared image dimensions and mode now match those opened images.
- Current protected predecessor files still have their code-owned exact hashes; the earlier independently executed actual Git/LFS audit establishes their 14 pre-feet anchors and 384 real predecessor files. No protected historical sources/proofs/scenes/approved images were modified.

The own runner is restricted to a fresh explicit `tmp/` work directory, new #37 evidence directory and new #37 scene path. It preserves protected historical inputs before/after execution, records all five worker exit codes, and distinguishes live diagnostic renders from the canonical fresh saved-build renders. The supplied exact final delivery demonstrates those worker/build/reload/pixel checks; this review did not rerun Blender or approve aesthetics.

Final evidence file: `tmp/goal37-gate-final-evidence.json` contains direct mutation errors, binding counts, exact decoded pixel hashes and the hashes below. Scope excludes final rig/physics/lookdev/animation and does not supersede the independent visual review.

### Final reviewed source hashes

| File | SHA-256 |
|---|---|
| `scripts/evidence_contracts.py` | `ae6051be976ae5072afde9290a33ee1c16c88280ecf40e7fb693f2fd9f5430b2` |
| `scripts/delivery_gates.py` | `7c1473bd6a272a0f0451f859b74935235b3b247c721d5166b32046dff7251bcc` |
| `scripts/delivery_shapes.py` | `7e68b681b9b375fb09dcecf0efb5fbea49e4c52a5ee3b6d154ca031bc75e3eda` |
| `scripts/history_gate.py` | `f5afb5a9f5dac6b64a556ddc02bf010dee45feb48ef9643d84cd28d8c2e5f32b` |
| `scripts/validate_project.py` | `9a427188d6e806cd930a95dec7ddb2b7769d7696657dfbfc32a1dc33398b9a20` |
| `tests/test_delivery_gates.py` | `7688e4c66e3cae606c25606d9693d2bcd6445b90d3661942ebd593b2f1a6221b` |
| `tests/test_history_gate.py` | `48917671eb4c75b8cf16c800d7186e11d3a9407b2687fdf902482b16002e150a` |
| `tests/test_beak_review.py` | `cec24d51bcb888310393881543984a5881efa08472c823c1017a610597542f2d` |
| `scripts/review_fixes_gate.py` | `caf23e02d9966ddb00da92f5f631e07b3e080ca2790b8db89e7189d1a148ebef` |
| `scripts/review_fixes_review.py` | `25bf69656b82c2ed595bef83ba8f6948730315990d45e578f1c3099e51696592` |
| `scripts/review_fixes_contracts.py` | `4db816a2136acf6f281beca2122ee94ce646fa32cfa086ad556255312bb58ddb` |
| `scripts/audit_review_fixes_history.py` | `d48b1bc3e15f208dffb3ca7b99167292af3154e987886c1bf782de6ce90cdcc2` |
| `tests/test_review_fixes_gate.py` | `1f17aeaf3348b7d2f3f3a765c17b4b6113b4db62bf0aec1a52afd3bffa1a0d2a` |
| `scripts/blender/review_fixes_checks.py` | `8f1e0d3c8bc2f636b6999960e61cced361e1eb427bfee4d4a9b822f6a86e5de6` |
| `scripts/blender/review_fixes_evidence.py` | `4e8cd5a7e420303264041981297fc273303460127b23ec4d965baaa46f56c431` |

**Final status: PASS for the requested technical gate scope of Issue #37. No remaining blocking gate findings.**


## Final publication addendum — complete actual run07

**PASS remains valid on the final published scene:** `8685fc054428ec848f20a922c995487f9ac4a2797cbe3713eaeb5e364b02e8fb`, **1,068,211 bytes**. This replaces the run06 file hash above. The host producer completed a full new build/saved-build/two-reload/corner run to bind the updated publication sources; no historical approval proof was rehashed.

Independent direct verification after run07 publication:

- Current own gate returns `[]`; `python scripts/project.py validate` exits 0.
- Current source/reference/protected/evidence bindings all match actual bytes: **50 / 9 / 384 / 53**. The evidence count includes subsequently added own independent log artifacts. All **18** current manual-review evidence bindings also match actual bytes.
- All five actual worker JSON files are **byte-identical to the independently recorded run06 worker JSON**. Each current build/reload declaration equals its actual JSON file.
- All four decoded 1024×1024 RGBA neutral/reload pixel arrays are identical across the three fresh processes **and identical to the independently recorded run06 decoded pixel hashes**.
- All five recorded command modes name `run07` and have exit 0. Every published worker `.log` is valid UTF-8 with LF, a final newline and no trailing line whitespace.
- Source cleanup is independently proven exact by hashes: adding one LF to current `evidence_contracts.py` reproduces its prior reviewed hash; removing only the new host log-publication normalization block reproduces the previously reviewed host-runner hash. All other 13 recorded gate/worker/test source hashes are unchanged. Geometry/check/gate semantics therefore remain unchanged.
- The four previously reported own-gate omissions were independently repeated once more and all reject. The full root run07 suite log was independently inspected: **45 tests**, 29.148 seconds, terminal `OK`. The earlier independent full-suite run also passed all 45 tests on the same unchanged gate/test semantics.

Final recorded changed source hashes:

| File | SHA-256 |
|---|---|
| `scripts/evidence_contracts.py` | `8155c2dc1ace94fa1e3dfdfa8afc1ec115708f2918f047da438a2f64ef9d1627` |
| `scripts/review_fixes_review.py` | `cf271609451f48d40d383734d4742b0e4752b76fd82c46695c21711382f544ef` |

`tmp/goal37-gate-final-evidence.json` contains the final run07 addendum, exact source/worker/pixel/proof hashes and current mutation errors. Its earlier sections preserve the prior review cycle. This remains scoped technical gate acceptance; the separate visual review owns aesthetic approval.

**Final publication status: PASS. No remaining blocking technical gate findings for #37.**
