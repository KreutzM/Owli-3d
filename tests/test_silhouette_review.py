"""The freeze must become stale when evidence changes or a gate is incomplete."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from silhouette_review import validate_review


class SilhouetteReviewTests(unittest.TestCase):
    def setUp(self):
        self.review = json.loads((ROOT/'design/silhouette_freeze.json').read_text(encoding='utf-8'))

    def test_freeze_matches_every_current_gate_and_artifact(self):
        self.assertEqual(validate_review(ROOT, self.review), [])

    def test_incomplete_or_blocked_review_cannot_freeze(self):
        review = copy.deepcopy(self.review)
        review['checks'].pop()
        review['blocking_findings'] = ['unresolved face placement']
        errors = validate_review(ROOT, review)
        self.assertTrue(any('every checklist item' in error for error in errors))
        self.assertTrue(any('blocking findings' in error for error in errors))

    def test_changed_view_and_wrong_reference_authority_rejected(self):
        review = copy.deepcopy(self.review)
        review['evidence_sha256']['validation/reviews/blockout_v01/VAL_FRONT.png'] = '0'*64
        review['checks'][0]['references'][0]['rank'] = 5
        errors = validate_review(ROOT, review)
        self.assertTrue(any('Stale freeze evidence' in error for error in errors))
        self.assertTrue(any('authority ranks' in error for error in errors))
