"""Bind actual #17 jaw opening and reference proof, rejecting stale/incomplete delivery."""
import copy
import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from delivery_gates import validate_beak_delivery


class BeakReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        folder=ROOT/'validation/reviews/beak_v01'
        cls.proof=json.loads((folder/'verification.json').read_text())
        cls.decision=json.loads((folder/'review.json').read_text())

    def test_current_saved_beak_and_three_criteria_are_proved(self):
        self.assertEqual(validate_beak_delivery(ROOT,self.proof,self.decision),[])

    def test_missing_criterion_and_stale_geometry_are_rejected(self):
        proof=copy.deepcopy(self.proof)
        proof['source_sha256']['design/beak.json']='0'*64
        decision=copy.deepcopy(self.decision)
        decision['criteria'].pop()
        errors=validate_beak_delivery(ROOT,proof,decision)
        self.assertIn('Missing goal criterion',errors)
        self.assertTrue(any('beak.json' in e for e in errors))

    def test_stationary_or_unsafe_opening_is_rejected(self):
        proof=copy.deepcopy(self.proof)
        proof['build']['opening_probes']['front_lower_vertex_drop_m']=0.0
        proof['build']['opening_probes']['minimum_sampled_mask_clearance_m']=-.001
        self.assertIn('Invalid visible opening or mask clearance',validate_beak_delivery(ROOT,proof,self.decision))
