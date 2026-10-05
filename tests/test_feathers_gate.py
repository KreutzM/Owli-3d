"""#6 inventories and recursive omission/type regressions; no synthetic approval."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from feathers_contracts import (ARCHIVED_STAGE_SHA256, PROTECTED_SHA256, SOURCES,
                                REFERENCE_NAMES, RELOAD_FIELDS, REVIEW_PATH)
from feathers_gate import (expected_mesh_names, validate_shape, worker_shape,
                           validate_worker_structure, proof_shape, DECISION_SHAPE, load_json,
                           validate_feathers)


def typed_fixture(schema):
    """Only a type/coverage fixture; values deliberately do not prove semantics."""
    if isinstance(schema, str):
        return {'str': 'fixture', 'sha256': 'a'*64, 'int': 2, 'float': .2,
                'number': .5, 'bool': True, 'NoneType': None}[schema]
    if 'dict' in schema:
        return {key: typed_fixture(value) for key, value in schema['dict'].items()}
    if 'keys' in schema:
        return {key: typed_fixture(schema['values']) for key in schema['keys']}
    items = schema['items']
    return [typed_fixture(items[0] if len(items) == 1 else items[index])
            for index in range(schema['list'])]


class FeathersStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg = json.loads((ROOT/'design/wings_feathers.json').read_bytes())
        cls.baseline = json.loads((ROOT/'validation/reviews/review_fixes_v01/reload_b_checks.json').read_bytes())
        cls.schema = worker_shape(cls.cfg, cls.baseline)
        cls.fixture = typed_fixture(cls.schema)

    def test_code_owned_history_anchors_match_materialized_git_lfs_bytes(self):
        self.assertEqual(len(PROTECTED_SHA256), 462)
        for name, digest in PROTECTED_SHA256.items():
            with self.subTest(path=name):
                self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(), digest)
        self.assertEqual(hashlib.sha256((ROOT/'scripts/blender/legacy/30_wings_feathers.py').read_bytes()).hexdigest(),
                         ARCHIVED_STAGE_SHA256)

    def test_sources_include_previous_contract_and_every_new_producer(self):
        from review_fixes_review import SOURCES as old_sources
        self.assertTrue(set(old_sources).issubset(SOURCES))
        self.assertEqual(len(REFERENCE_NAMES), 9)
        self.assertEqual(len(set(SOURCES)), len(SOURCES))
        self.assertEqual(set(RELOAD_FIELDS), set(self.schema['dict']))
        self.assertIn('scripts/blender/feathers_checks.py', SOURCES)
        self.assertIn('scripts/feathers_review.py', SOURCES)

    def test_typed_fixture_has_complete_structure_without_claiming_admission(self):
        self.assertEqual(validate_worker_structure(self.fixture, self.cfg, self.baseline), [])

    def test_each_required_region_and_whole_reload_field_cannot_be_empty_or_removed(self):
        for field in self.schema['dict']:
            for bad in (None, {}, []):
                with self.subTest(field=field, bad=bad):
                    candidate = copy.deepcopy(self.fixture)
                    candidate[field] = bad
                    self.assertTrue(validate_worker_structure(candidate, self.cfg, self.baseline))
        for family in ('wing_layers', 'back_layers', 'chest_layers', 'tail_layers', 'face_layers', 'central_layers'):
            cfg = copy.deepcopy(self.cfg)
            cfg[family] = []
            with self.subTest(family=family), self.assertRaises(ValueError):
                expected_mesh_names(cfg)

    def test_center_groups_have_exact_required_ids_and_unsuffixed_editable_meshes(self):
        names = expected_mesh_names(self.cfg)
        for identifier in ('HeadCenter', 'BodyCenter', 'ChestCenter'):
            self.assertIn('FTH_'+identifier, names)
            self.assertNotIn('FTH_'+identifier+'_L', names)
            self.assertNotIn('FTH_'+identifier+'_R', names)
        cfg = copy.deepcopy(self.cfg)
        cfg['central_layers'][0]['id'] = 'WrongCenter'
        with self.assertRaises(ValueError):
            expected_mesh_names(cfg)

    def test_nested_underfields_and_required_mesh_entries_cannot_disappear(self):
        def visit(value, schema, path):
            if 'dict' in schema or 'keys' in schema:
                required = schema.get('dict')
                if required is None:
                    required = {key: schema['values'] for key in schema['keys']}
                for key, child in required.items():
                    omission = dict(value)
                    del omission[key]
                    self.assertTrue(validate_shape(omission, schema, path), path+'/'+key)
                    if not isinstance(child, str):
                        visit(value[key], child, path+'/'+key)
            else:
                items = schema['items']
                if value:
                    self.assertTrue(validate_shape(value[:-1], schema, path), path)
                for index, item in enumerate(value):
                    child = items[0] if len(items) == 1 else items[index]
                    if not isinstance(child, str):
                        visit(item, child, path+'/'+str(index))
        visit(self.fixture, self.schema, 'worker')

    def test_scalar_types_nonfinite_and_invalid_digests_fail(self):
        for number in (float('nan'), float('inf'), float('-inf'), True, '0'):
            with self.subTest(value=repr(number)):
                self.assertTrue(validate_shape(number, 'float'))
                self.assertTrue(validate_shape(number, 'number'))
        self.assertTrue(validate_shape(True, 'int'))
        self.assertTrue(validate_shape(1, 'bool'))
        self.assertTrue(validate_shape('', 'str'))
        for digest in ('', 'a'*63, 'A'*64, None, {}):
            self.assertTrue(validate_shape(digest, 'sha256'))

    def test_json_duplicates_and_nonfinite_tokens_cannot_hide_missing_evidence(self):
        for raw in (b'{"view": 1, "view": 2}', b'{"distance": NaN}', b'{"distance": Infinity}'):
            with self.subTest(raw=raw), patch.object(Path, 'read_bytes', return_value=raw):
                with self.assertRaises(ValueError):
                    load_json(Path('fixture.json'))

    def test_binding_nulls_and_empty_sequences_are_allowed_only_in_their_typed_locations(self):
        wing = next(name for name in self.fixture['bindings'] if name.startswith('FTH_Wing'))
        candidate = copy.deepcopy(self.fixture)
        candidate['bindings'][wing]['parent'] = None
        self.assertTrue(validate_worker_structure(candidate, self.cfg, self.baseline))
        leaf = next(name for name in self.fixture['bindings'] if not name.startswith('FTH_Wing'))
        candidate = copy.deepcopy(self.fixture)
        candidate['bindings'][leaf]['vertex_groups'] = ['invented']
        self.assertTrue(validate_worker_structure(candidate, self.cfg, self.baseline))

    def test_every_proof_inventory_is_code_owned_and_cannot_be_shrunk(self):
        schema = proof_shape(self.cfg, self.baseline)
        proof = typed_fixture(schema)
        self.assertEqual(validate_shape(proof, schema, 'proof'), [])
        for field in ('source_sha256', 'reference_sha256', 'protected_predecessor_sha256',
                      'evidence_sha256', 'reloaded', 'render_comparison'):
            table = proof[field]
            self.assertTrue(validate_shape({}, schema['dict'][field], field))
            for key in table:
                omission = dict(table)
                del omission[key]
                with self.subTest(field=field, key=key):
                    self.assertTrue(validate_shape(omission, schema['dict'][field], field))

    def test_manual_review_requires_all_views_criteria_and_bound_reports(self):
        decision = typed_fixture(DECISION_SHAPE)
        self.assertEqual(validate_shape(decision, DECISION_SHAPE, 'decision'), [])
        for field in ('views', 'criteria', 'evidence_sha256'):
            for key in decision[field]:
                omission = dict(decision[field])
                del omission[key]
                with self.subTest(field=field, key=key):
                    self.assertTrue(validate_shape(omission, DECISION_SHAPE['dict'][field], field))
        decision['blocking_findings'] = ['unresolved']
        self.assertTrue(validate_shape(decision, DECISION_SHAPE, 'decision'))

    def test_wrong_lengths_extra_fields_and_null_nested_values_cannot_compare_equal(self):
        for field in ('new_meshes', 'bindings', 'symmetry', 'root_contacts', 'leaf_roots',
                      'feet', 'studio', 'framing', 'movement'):
            table = self.fixture[field]
            for key in table:
                candidate = dict(table)
                candidate[key] = None
                with self.subTest(field=field, key=key):
                    self.assertTrue(validate_shape(candidate, self.schema['dict'][field], field))
        candidate = copy.deepcopy(self.fixture)
        candidate['movement']['wing_gestures']['states'] = candidate['movement']['wing_gestures']['states'][:1]
        self.assertTrue(validate_worker_structure(candidate, self.cfg, self.baseline))
        candidate = copy.deepcopy(self.fixture)
        candidate['invented'] = {}
        self.assertTrue(validate_worker_structure(candidate, self.cfg, self.baseline))


class FeathersDeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.proof = load_json(ROOT/REVIEW_PATH/'verification.json')
        cls.decision = load_json(ROOT/REVIEW_PATH/'review.json')

    def test_current_exact_delivery_has_real_bound_workers_and_views(self):
        self.assertEqual(validate_feathers(ROOT, self.proof, self.decision), [])

    def test_equal_nested_claims_cannot_replace_actual_worker_measurements(self):
        proof = copy.deepcopy(self.proof)
        name = next(iter(proof['build']['new_meshes']))
        for field in ('build', 'reloaded'):
            proof[field]['new_meshes'][name]['cage']['volume_m3'] *= 1.01
        errors = validate_feathers(ROOT, proof, self.decision)
        self.assertTrue(any('actual bound worker JSON' in error for error in errors), errors)

    def test_missing_feather_targets_repeated_gestures_and_wrong_motion_counts_fail(self):
        for mutation in ('targets', 'gestures', 'beak', 'blink', 'gaze'):
            proof = copy.deepcopy(self.proof)
            for field in ('build', 'reloaded'):
                movement = proof[field]['movement']
                function = movement['feather_function']
                if mutation == 'targets':
                    function['target_meshes'][0] = function['target_meshes'][1]
                elif mutation == 'gestures':
                    movement['wing_gestures']['states'][1] = copy.deepcopy(movement['wing_gestures']['states'][0])
                elif mutation == 'beak':
                    movement['beak_opening']['collision_checks'] -= 1
                elif mutation == 'blink':
                    function['blink_collision_checks'] -= 1
                else:
                    function['gaze_probes'][0]['collision_checks'] -= 1
            with self.subTest(mutation=mutation):
                self.assertTrue(validate_feathers(ROOT, proof, self.decision))

    def test_actual_decoded_pixels_are_compared_even_when_metadata_claims_equality(self):
        from PIL import Image
        real_open = Image.open
        changed = ROOT/REVIEW_PATH/'evidence/reload_b/VAL_FRONT.png'
        def different_pixels(path, *args, **kwargs):
            im = real_open(path, *args, **kwargs)
            if Path(path) == changed:
                im.load()
                pixel = im.getpixel((5, 5))
                im.putpixel((5, 5), ((pixel[0]+1) % 256, *pixel[1:]))
            return im
        with patch('feathers_gate.Image.open', side_effect=different_pixels):
            errors = validate_feathers(ROOT, self.proof, self.decision)
        self.assertTrue(any('Actual canonical build/two reload PNG pixels differ' in error for error in errors), errors)

    def test_manual_review_must_name_current_scene_and_primary_reference_ranks(self):
        decision = copy.deepcopy(self.decision)
        decision['scene_sha256'] = '0'*64
        decision['reference_authority'][0]['rank'] = 5
        errors = validate_feathers(ROOT, self.proof, decision)
        self.assertIn('Manual #6 decision names another scene', errors)
        self.assertIn('Wrong #6 visual reference hierarchy', errors)

    def test_preserved_hash_claims_cannot_change_unrelated_head_or_feet(self):
        proof = copy.deepcopy(self.proof)
        for field in ('build', 'reloaded'):
            proof[field]['geometry_sha256']['PRI_HeadNeckTorso'] = '0'*64
        self.assertTrue(validate_feathers(ROOT, proof, self.decision))

    def test_each_new_leaf_requires_actual_sampled_embedded_root_not_a_support_label(self):
        name = next(iter(self.proof['build']['leaf_roots']))
        for key, invalid in (('samples', 1), ('embedded_back_samples', 0),
                             ('maximum_front_root_distance_m', .008),
                             ('minimum_back_signed_distance_m', .001)):
            proof = copy.deepcopy(self.proof)
            for field in ('build', 'reloaded'):
                proof[field]['leaf_roots'][name][key] = invalid
            with self.subTest(field=key):
                errors = validate_feathers(ROOT, proof, self.decision)
                self.assertTrue(any('actual feather root' in error for error in errors), errors)
        proof = copy.deepcopy(self.proof)
        for field in ('build', 'reloaded'):
            del proof[field]['leaf_roots'][name]
        self.assertTrue(validate_feathers(ROOT, proof, self.decision))
        proof = copy.deepcopy(self.proof)
        for field in ('build', 'reloaded'):
            proof[field]['leaf_roots'][name]['support'] = 'BAK_Lower'
        errors = validate_feathers(ROOT, proof, self.decision)
        self.assertTrue(any('actual supporting primary' in error for error in errors), errors)


if __name__ == '__main__':
    unittest.main()
