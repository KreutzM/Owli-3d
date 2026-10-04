"""Regression tests for the actual IR-02 omissions, not self-declared inventories."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from delivery_gates import validate_milestone
from evidence_contracts import DELIVERY_INVENTORIES


class DeliveryV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = {}
        for name in DELIVERY_INVENTORIES:
            folder = ROOT / 'validation/reviews' / name
            cls.fixtures[name] = (json.loads((folder / 'verification.json').read_bytes()),
                                  json.loads((folder / 'review.json').read_bytes()))

    def test_real_existing_deliveries_pass_current_gates(self):
        for name, (proof, decision) in self.fixtures.items():
            with self.subTest(name=name):
                self.assertEqual(validate_milestone(name, ROOT, proof, decision), [])

    def test_empty_missing_wrong_type_and_each_omitted_key_fail(self):
        for name, contract in DELIVERY_INVENTORIES.items():
            original, decision = self.fixtures[name]
            for field, required in contract.items():
                for replacement in ({}, None, [], 'invalid'):
                    with self.subTest(name=name, field=field, replacement=replacement):
                        proof = copy.deepcopy(original)
                        proof[field] = replacement
                        self.assertTrue(validate_milestone(name, ROOT, proof, decision))
                proof = copy.deepcopy(original)
                del proof[field]
                self.assertTrue(validate_milestone(name, ROOT, proof, decision))
                for key in required:
                    with self.subTest(name=name, field=field, key=key):
                        proof = copy.deepcopy(original)
                        del proof[field][key]
                        errors = validate_milestone(name, ROOT, proof, decision)
                        self.assertTrue(any(field in e and key in e for e in errors), errors)

    def test_each_reload_value_and_missing_corresponding_build_key_fail(self):
        for name, (original, decision) in self.fixtures.items():
            for key in DELIVERY_INVENTORIES[name]['reloaded']:
                with self.subTest(name=name, key=key):
                    proof = copy.deepcopy(original)
                    proof['reloaded'][key] = {'invented': 'not equivalent'}
                    self.assertTrue(validate_milestone(name, ROOT, proof, decision))
                    proof = copy.deepcopy(original)
                    del proof['build'][key]
                    self.assertTrue(validate_milestone(name, ROOT, proof, decision))

    def test_complete_inventories_do_not_hide_wrong_source_or_reference_hashes(self):
        for name, (original, decision) in self.fixtures.items():
            for field in ('source_sha256', 'reference_sha256'):
                proof = copy.deepcopy(original)
                key = next(iter(proof[field]))
                proof[field][key] = '0' * 64
                errors = validate_milestone(name, ROOT, proof, decision)
                self.assertTrue(any(key in e.replace('\\', '/') for e in errors), errors)

    def test_matched_null_empty_and_nested_omitted_reload_claims_fail(self):
        for name, (original, decision) in self.fixtures.items():
            for key in DELIVERY_INVENTORIES[name]['reloaded']:
                for empty in (None, {}, [], ''):
                    with self.subTest(name=name, key=key, empty=empty):
                        proof = copy.deepcopy(original)
                        proof['build'][key] = copy.deepcopy(empty)
                        proof['reloaded'][key] = copy.deepcopy(empty)
                        self.assertTrue(validate_milestone(name, ROOT, proof, decision))
            proof = copy.deepcopy(original)
            nested = next(iter(proof['reloaded']['studio']))
            del proof['reloaded']['studio'][nested]
            del proof['build']['studio'][nested]
            self.assertTrue(validate_milestone(name, ROOT, proof, decision))

    def test_matched_invalid_geometry_digest_is_rejected(self):
        for name, (original, decision) in self.fixtures.items():
            proof = copy.deepcopy(original)
            value = proof['build']['geometry_sha256']
            if isinstance(value, str):
                proof['build']['geometry_sha256'] = proof['reloaded']['geometry_sha256'] = 'not-a-sha256'
            else:
                key = next(iter(value))
                proof['build']['geometry_sha256'][key] = proof['reloaded']['geometry_sha256'][key] = 'not-a-sha256'
            self.assertTrue(validate_milestone(name, ROOT, proof, decision))
