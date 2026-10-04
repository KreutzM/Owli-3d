"""#37 own delivery regressions, including actual worker and view evidence binding."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from review_fixes_gate import validate_review_fixes


class ReviewFixesGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        folder = ROOT/'validation/reviews/review_fixes_v01'
        cls.proof = json.loads((folder/'verification.json').read_bytes())
        cls.decision = json.loads((folder/'review.json').read_bytes())

    def test_current_exact_scene_and_all_findings_are_supported(self):
        self.assertEqual(validate_review_fixes(ROOT,self.proof,self.decision),[])

    def test_omitted_inventory_fields_and_each_required_key_fail(self):
        for field in ('source_sha256','reference_sha256','reloaded','protected_predecessor_sha256'):
            proof = copy.deepcopy(self.proof)
            proof[field] = {}
            self.assertTrue(validate_review_fixes(ROOT,proof,self.decision))
            for key in self.proof[field]:
                with self.subTest(field=field,key=key):
                    proof = copy.deepcopy(self.proof)
                    del proof[field][key]
                    self.assertTrue(validate_review_fixes(ROOT,proof,self.decision))

    def test_matched_empty_reload_values_cannot_replace_real_worker_evidence(self):
        for field in self.proof['reloaded']:
            for empty in (None,{},[]):
                proof = copy.deepcopy(self.proof)
                proof['build'][field] = copy.deepcopy(empty)
                proof['reloaded'][field] = copy.deepcopy(empty)
                self.assertTrue(validate_review_fixes(ROOT,proof,self.decision))

    def test_claims_of_unsafe_blink_beak_and_wrong_meshes_fail(self):
        for mutation in ('blink','beak','mesh'):
            proof = copy.deepcopy(self.proof)
            if mutation=='blink':
                proof['build']['movement']['blink_and_gaze']['closed_coverage_rays']=0
            elif mutation=='beak':
                proof['build']['movement']['beak_opening']['minimum_sampled_mask_clearance_m']=-.001
            else:
                proof['build']['geometry_sha256']['GRP_Claw_L_Rear_1']='0'*64
            self.assertTrue(validate_review_fixes(ROOT,proof,self.decision))

    def test_missing_motion_view_or_findings_review_binding_fails(self):
        proof = copy.deepcopy(self.proof)
        del proof['evidence_sha256']['evidence/blink/VAL_FRONT.png']
        self.assertTrue(validate_review_fixes(ROOT,proof,self.decision))
        decision = copy.deepcopy(self.decision)
        del decision['findings']['IR-04']
        self.assertTrue(validate_review_fixes(ROOT,self.proof,decision))

    def test_repeated_corner_and_empty_rejection_claims_do_not_prove_parameter_rectangle(self):
        proof = copy.deepcopy(self.proof)
        proof['foot_corners']['allowed'] = [copy.deepcopy(proof['foot_corners']['allowed'][0]) for _ in range(5)]
        proof['foot_corners']['rejected'] = [{} for _ in range(4)]
        errors = validate_review_fixes(ROOT,proof,self.decision)
        self.assertTrue(any('Foot-corner sample inventory' in e for e in errors),errors)
        self.assertTrue(any('out-of-range Foot sample' in e for e in errors),errors)

    def test_declared_image_dimensions_and_mode_must_match_actual_pixels(self):
        proof = copy.deepcopy(self.proof)
        proof['render_comparison']['VAL_FRONT']['size'] = []
        proof['render_comparison']['VAL_FRONT']['mode'] = 'invented'
        self.assertTrue(any('view metadata differs' in e for e in validate_review_fixes(ROOT,proof,self.decision)))

    def test_manual_review_must_name_the_exact_scene_and_reference_ranks(self):
        decision = copy.deepcopy(self.decision)
        decision['scene_sha256'] = '0'*64
        decision['reference_authority'][0]['rank'] = 5
        errors = validate_review_fixes(ROOT,self.proof,decision)
        self.assertIn('Visual decision names a different #37 scene',errors)
        self.assertIn('Wrong #37 visual reference authority',errors)
