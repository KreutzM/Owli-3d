"""Bind #16's saved geometry, actual Blender probes and manual reference review."""
import copy
import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from delivery_gates import validate_delivery


class FaceReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        folder=ROOT/'validation/reviews/face_v01'
        cls.proof=json.loads((folder/'verification.json').read_text())
        cls.decision=json.loads((folder/'review.json').read_text())

    def test_current_saved_face_and_full_goal_review_are_proved(self):
        self.assertEqual(validate_delivery(ROOT,self.decision,self.proof),[])

    def test_missing_goal_criterion_is_rejected(self):
        decision=copy.deepcopy(self.decision)
        decision['criteria'].pop()
        self.assertIn('Missing/reordered goal criterion',validate_delivery(ROOT,decision,self.proof))

    def test_stale_source_and_review_evidence_are_rejected(self):
        proof=copy.deepcopy(self.proof)
        proof['source_sha256']['design/face.json']='0'*64
        decision=copy.deepcopy(self.decision)
        decision['evidence_sha256']['verification.json']='0'*64
        errors=validate_delivery(ROOT,decision,proof)
        self.assertTrue(any('design' in e and 'face.json' in e for e in errors))
        self.assertTrue(any('verification.json' in e for e in errors))

    def test_insufficient_clearance_or_unclosed_eye_is_rejected(self):
        proof=copy.deepcopy(self.proof)
        proof['build']['probes']['minimum_clearance_m']=-.001
        proof['build']['probes']['closed_coverage_rays']=0
        errors=validate_delivery(ROOT,self.decision,proof)
        self.assertIn('Lid clearance failed',errors)
        self.assertIn('Full closed-eye coverage not proved',errors)
