"""Goal 18 exact inventories, recursive omissions, and actual corruptions."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from materials_contracts import (
    ARCHIVED_STAGE_SHA256, PROTECTED_SHA256, SOURCES, REFERENCE_NAMES,
    REVIEW_PATH, SCENE_PATH, MODES, EVIDENCE_NAMES,
)
from materials_review import checked_paths, compare_pixels
from materials_gate import (
    worker_shape, proof_shape, validate_shape, validate_worker_structure,
    validate_material_semantics, DECISION_SHAPE, RELOAD_FIELDS,
)


def typed_fixture(schema):
    """A structural fixture deliberately does not claim production semantics."""
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


class MaterialsInventoryTests(unittest.TestCase):
    def test_all_548_git_lfs_predecessor_bytes_remain_immutable(self):
        self.assertEqual(len(PROTECTED_SHA256), 548)
        for name, digest in PROTECTED_SHA256.items():
            with self.subTest(path=name):
                self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(), digest)
        self.assertEqual(hashlib.sha256((ROOT/'scripts/blender/legacy/50_materials.py').read_bytes()).hexdigest(),
                         ARCHIVED_STAGE_SHA256)

    def test_sources_extend_complete_goal_6_inventory_and_require_own_producers(self):
        from feathers_contracts import SOURCES as previous
        self.assertTrue(set(previous).issubset(SOURCES))
        self.assertEqual(len(REFERENCE_NAMES), 9)
        self.assertEqual(len(SOURCES), len(set(SOURCES)))
        for name in ('design/materials_lookdev.json', 'scripts/blender/50_materials.py',
                     'scripts/blender/materials_checks.py', 'scripts/blender/materials_evidence.py',
                     'scripts/blender/legacy/50_materials.py', 'scripts/materials_gate.py'):
            self.assertIn(name, SOURCES)
        self.assertIn('design/materials.json', PROTECTED_SHA256)
        for mode in MODES:
            self.assertIn(mode+'_checks.json', EVIDENCE_NAMES)

    def test_producer_accepts_only_fresh_explicit_tmp_and_fixed_own_output(self):
        with tempfile.TemporaryDirectory() as parent:
            root = Path(parent)
            (root/'tmp').mkdir()
            work = root/'tmp/fresh'
            self.assertEqual(checked_paths(work, root/REVIEW_PATH, root/SCENE_PATH, root),
                             (work, root/REVIEW_PATH, root/SCENE_PATH))
            for wrong_work in (root/'tmp', root/'outside', root/'tmp/../outside'):
                with self.subTest(work=wrong_work), self.assertRaises(ValueError):
                    checked_paths(wrong_work, root/REVIEW_PATH, root/SCENE_PATH, root)
            for wrong_target in ('blender/scene/owli_feathers_v01.blend',
                                 'blender/scene/owli.blend'):
                with self.subTest(target=wrong_target), self.assertRaises(ValueError):
                    checked_paths(work, root/REVIEW_PATH, root/wrong_target, root)
            with self.assertRaises(ValueError):
                checked_paths(work, root/'validation/reviews/feathers_v01', root/SCENE_PATH, root)
            work.mkdir()
            with self.assertRaises(ValueError):
                checked_paths(work, root/REVIEW_PATH, root/SCENE_PATH, root)

    def test_runner_reads_actual_canonical_pixels_and_rejects_corruption(self):
        from materials_contracts import VIEWS
        with tempfile.TemporaryDirectory() as parent:
            work = Path(parent)
            for label in ('neutral', 'reload_a', 'reload_b'):
                folder = work/'renders'/label
                folder.mkdir(parents=True)
                for view in VIEWS:
                    with Image.new('RGBA', (1024, 1024), (2, 7, 13, 255)) as im:
                        im.putpixel((4, 4), (24, 31, 49, 255))
                        im.save(folder/(view+'.png'))
            self.assertEqual(set(compare_pixels(work)), set(VIEWS))
            changed = work/'renders/reload_b/VAL_FRONT.png'
            with Image.open(changed) as im:
                im.putpixel((5, 5), (3, 7, 13, 255))
                im.save(changed)
            with self.assertRaisesRegex(ValueError, 'Canonical rendered pixels differ'):
                compare_pixels(work)

    def test_runner_rejects_wrong_canonical_mode_even_if_all_three_match(self):
        from materials_contracts import VIEWS
        with tempfile.TemporaryDirectory() as parent:
            work = Path(parent)
            for label in ('neutral', 'reload_a', 'reload_b'):
                folder = work/'renders'/label
                folder.mkdir(parents=True)
                for view in VIEWS:
                    with Image.new('RGB', (1024, 1024), (2, 7, 13)) as im:
                        im.save(folder/(view+'.png'))
            with self.assertRaisesRegex(ValueError, 'Canonical render dimensions/mode differ'):
                compare_pixels(work)


class MaterialsStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg = json.loads((ROOT/'design/materials_lookdev.json').read_bytes())
        cls.baseline = json.loads((ROOT/'validation/reviews/feathers_v01/reload_b_checks.json').read_bytes())
        cls.schema = worker_shape(cls.cfg, cls.baseline)
        cls.fixture = typed_fixture(cls.schema)

    def test_code_owned_recursive_worker_inventory_has_all_18_reload_fields(self):
        self.assertEqual(set(self.schema['dict']), set(RELOAD_FIELDS))
        self.assertEqual(len(RELOAD_FIELDS), 18)
        self.assertEqual(validate_worker_structure(self.fixture, self.cfg, self.baseline), [])
        self.assertEqual(len(self.schema['dict']['assignments']['dict']), 103)
        self.assertEqual(len(self.schema['dict']['tech_meshes']['dict']), 17)
        self.assertEqual(len(self.schema['dict']['materials']['dict']), 10)

    def test_none_empty_or_removed_whole_reload_field_is_rejected(self):
        for field in RELOAD_FIELDS:
            for invalid in (None, {}, []):
                candidate = copy.deepcopy(self.fixture)
                candidate[field] = invalid
                with self.subTest(field=field, invalid=invalid):
                    self.assertTrue(validate_worker_structure(candidate, self.cfg, self.baseline))
            candidate = copy.deepcopy(self.fixture)
            del candidate[field]
            self.assertTrue(validate_worker_structure(candidate, self.cfg, self.baseline))

    def test_every_nested_worker_field_and_sequence_requires_recursive_coverage(self):
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
                # Uniform arrays share a code-owned item schema. One occurrence
                # exercises every item type without iterating all cage polygons.
                for index in range(len(value) if len(items) != 1 else min(1, len(value))):
                    child = items[0] if len(items) == 1 else items[index]
                    if not isinstance(child, str):
                        visit(value[index], child, path+'/'+str(index))
        visit(self.fixture, self.schema, 'worker')

    def test_empty_or_shrunken_source_reference_evidence_history_inventories_fail(self):
        schema = proof_shape(self.cfg, self.baseline)
        fixture = typed_fixture(schema)
        for field in ('source_sha256', 'reference_sha256', 'evidence_sha256', 'protected_predecessor_sha256'):
            value, table = fixture[field], schema['dict'][field]
            self.assertTrue(validate_shape({}, table))
            for key in value:
                omission = dict(value)
                del omission[key]
                with self.subTest(field=field, key=key):
                    self.assertTrue(validate_shape(omission, table))
        for field in ('views', 'criteria', 'evidence_sha256'):
            self.assertTrue(validate_shape({}, DECISION_SHAPE['dict'][field]))

    def test_required_families_cannot_shrink_parameterized_geometry_scope(self):
        from materials_gate import expected_tech_names
        for field in ('nodes', 'links'):
            cfg = copy.deepcopy(self.cfg)
            cfg['forehead'][field] = {}
            with self.subTest(field=field), self.assertRaises(ValueError):
                expected_tech_names(cfg)
        for field in ('perch_rings', 'chest_overrides'):
            cfg = copy.deepcopy(self.cfg)
            cfg[field] = []
            with self.subTest(field=field), self.assertRaises(ValueError):
                expected_tech_names(cfg)

    def test_typed_empty_ramps_do_not_allow_missing_connected_shader_fields(self):
        self.assertEqual(self.fixture['materials']['Tech_Cyan']['ramps'], {})
        for role in self.fixture['materials']:
            data = copy.deepcopy(self.fixture['materials'][role])
            del data['principled_inputs']['base_color']
            self.assertTrue(validate_material_semantics(data, role, self.cfg))
        data = copy.deepcopy(self.fixture['materials']['Feather_Warm'])
        data['ramps']['WarmDiagonal']['stops'][0][1] = []
        self.assertTrue(validate_material_semantics(data, 'Feather_Warm', self.cfg))


class MaterialsDeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from materials_gate import load_json
        cls.proof = load_json(ROOT/REVIEW_PATH/'verification.json')
        cls.decision = load_json(ROOT/REVIEW_PATH/'review.json')

    def test_exact_current_assigned_material_delivery_passes(self):
        from materials_gate import validate_materials
        self.assertEqual(validate_materials(ROOT, self.proof, self.decision), [])

    def test_assignment_missing_polygon_or_wrong_material_is_rejected(self):
        from materials_gate import validate_materials
        for mutation in ('slots', 'unassigned', 'distribution', 'polygon_count'):
            proof = copy.deepcopy(self.proof)
            for field in ('build', 'reloaded'):
                data = proof[field]['assignments']['PRI_HeadNeckTorso']
                if mutation == 'slots':
                    data['slots'][0] = 'BLK_Swatch_mid_blue'
                elif mutation == 'unassigned':
                    data['unassigned_polygons'] = 1
                elif mutation == 'distribution':
                    data['polygon_material_indices'][0] = 1-data['polygon_material_indices'][0]
                else:
                    data['polygon_material_indices'].pop()
            with self.subTest(mutation=mutation):
                self.assertTrue(validate_materials(ROOT, proof, self.decision))

    def test_equal_forged_shader_claims_fail_real_semantics(self):
        from materials_gate import validate_materials
        for mutation in ('metallic', 'linear', 'emission', 'graph', 'ramp', 'fingerprint'):
            proof = copy.deepcopy(self.proof)
            for field in ('build', 'reloaded'):
                materials = proof[field]['materials']
                if mutation == 'metallic':
                    materials['Feather_Navy']['principled_inputs']['metallic'] = .85
                elif mutation == 'linear':
                    materials['Feather_Blue']['principled_inputs']['base_color'][0] = 36/255
                elif mutation == 'emission':
                    materials['Tech_Cyan']['principled_inputs']['emission_strength'] = 40.0
                elif mutation == 'graph':
                    materials['Perch_Metal']['links'][0][0] = 'SurfaceGrain'
                elif mutation == 'ramp':
                    materials['Feather_Warm']['ramps']['WarmDiagonal']['stops'][3][1] = [1.0, 0.5, 0.1, 1.0]
                else:
                    materials['Feather_Cream']['shader_sha256'] = '0'*64
            with self.subTest(mutation=mutation):
                self.assertTrue(validate_materials(ROOT, proof, self.decision))

    def test_equal_omitted_tech_target_or_incomplete_pose_counts_do_not_prove_function(self):
        from materials_gate import validate_materials
        for mutation in ('target', 'blink', 'gaze', 'beak', 'wing', 'neutral'):
            proof = copy.deepcopy(self.proof)
            for field in ('build', 'reloaded'):
                probes = proof[field]['movement']['tech_function']
                if mutation == 'target':
                    probes['target_meshes'][0] = probes['target_meshes'][1]
                elif mutation == 'blink':
                    probes['blink_collision_checks'] -= 1
                elif mutation == 'gaze':
                    probes['gaze_probes'][0]['collision_checks'] -= 1
                elif mutation == 'beak':
                    probes['beak_collision_checks'] -= 1
                elif mutation == 'wing':
                    probes['wing_states'][1] = copy.deepcopy(probes['wing_states'][0])
                else:
                    probes['neutral_restored'] = False
            with self.subTest(mutation=mutation):
                self.assertTrue(validate_materials(ROOT, proof, self.decision))

    def test_an_unsafe_actual_blink_sample_cannot_hide_behind_a_safe_global_minimum(self):
        from materials_gate import validate_materials
        for mutation in ('negative_sample', 'inconsistent_global'):
            proof = copy.deepcopy(self.proof)
            for field in ('build', 'reloaded'):
                face = proof[field]['movement']['blink_and_gaze']
                if mutation == 'negative_sample':
                    face['minimum_triangle_clearance_m']['0.000/Upper/L'] = -.01
                else:
                    face['minimum_clearance_m'] = min(face['minimum_triangle_clearance_m'].values())+.0001
            with self.subTest(mutation=mutation):
                errors = validate_materials(ROOT, proof, self.decision)
                self.assertTrue(any('Incomplete/unsafe full actual blink/gaze trajectory' in e for e in errors), errors)

    def test_stale_original_anatomy_eye_shader_and_floating_tech_are_rejected(self):
        from materials_gate import validate_materials
        for mutation in ('body', 'eyes', 'foot', 'root', 'symmetry'):
            proof = copy.deepcopy(self.proof)
            for field in ('build', 'reloaded'):
                data = proof[field]
                if mutation == 'body':
                    data['shape_sha256']['PRI_HeadNeckTorso'] = '0'*64
                elif mutation == 'eyes':
                    data['eye_state_sha256']['FAC_Cornea_L'] = '0'*64
                elif mutation == 'foot':
                    data['feet']['independent_surface_collision_pairs'] = 44
                elif mutation == 'root':
                    data['tech_seats']['TECH_ForeheadNode_Hub']['maximum_surface_distance_m'] = .03
                else:
                    data['tech_symmetry']['TECH_PerchRing_End_R']['maximum_mirror_deviation_m'] = .03
            with self.subTest(mutation=mutation):
                self.assertTrue(validate_materials(ROOT, proof, self.decision))

    def test_gate_decodes_actual_pixels_even_when_metadata_claims_equal(self):
        from materials_gate import validate_materials
        real_open = Image.open
        changed = ROOT/REVIEW_PATH/'evidence/reload_b/VAL_FRONT.png'
        def corrupt(path, *args, **kwargs):
            im = real_open(path, *args, **kwargs)
            if Path(path) == changed:
                im.load()
                pixel = im.getpixel((5, 5))
                im.putpixel((5, 5), ((pixel[0]+1) % 256, *pixel[1:]))
            return im
        with patch('materials_gate.Image.open', side_effect=corrupt):
            errors = validate_materials(ROOT, self.proof, self.decision)
        self.assertTrue(any('Actual canonical build/two reload PNG pixels differ' in error for error in errors), errors)

    def test_final_manual_f01_glare_view_or_reference_findings_cannot_be_omitted(self):
        from materials_gate import validate_materials
        decision = copy.deepcopy(self.decision)
        decision['scene_sha256'] = '0'*64
        decision['reference_authority'][0]['rank'] = 5
        decision['criteria']['F01_cream_v_warm_diagonals']['status'] = 'fail'
        decision['criteria']['restrained_cyan_accents']['reason'] = ''
        self.assertTrue(validate_materials(ROOT, self.proof, decision))


if __name__ == '__main__':
    unittest.main()
