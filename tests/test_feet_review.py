"""Bind the complete foot delivery and reject missing anatomy/contact evidence."""
import copy
import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from feet_review import validate_feet_delivery


class FeetReviewTests(unittest.TestCase):
    def setUp(self):
        folder=ROOT/'validation/reviews/feet_v01'
        self.proof=json.loads((folder/'verification.json').read_text())
        self.decision=json.loads((folder/'review.json').read_text())

    def test_current_saved_feet_and_all_goal_criteria_are_proved(self):
        self.assertEqual(validate_feet_delivery(ROOT,self.proof,self.decision),[])

    def test_floating_contact_missing_rear_and_missing_support_are_rejected(self):
        for mutation in ('floating','missing_rear','unsupported'):
            proof=copy.deepcopy(self.proof)
            if mutation=='floating':proof['build']['contacts']['GRP_Claw_L_Rear_1']['nearest_surface_distance_m']=.01
            elif mutation=='missing_rear':del proof['build']['toe_branches']['GRP_Foot_L']['toe_Rear_1']
            else:proof['build']['pad_support_contact_m']={}
            self.assertTrue(validate_feet_delivery(ROOT,proof,self.decision),mutation)

    def test_stale_source_and_unapproved_reference_decision_are_rejected(self):
        proof=copy.deepcopy(self.proof)
        proof['source_sha256']['design/feet.json']='0'*64
        self.assertTrue(validate_feet_delivery(ROOT,proof,self.decision))
        decision=copy.deepcopy(self.decision)
        decision['criteria'][0]['references'][0]['rank']=5
        self.assertTrue(validate_feet_delivery(ROOT,self.proof,decision))
