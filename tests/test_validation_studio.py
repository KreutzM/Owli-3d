"""Config safety and integrity checks for the actual stored Blender evidence."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from setup_review import image_metrics
from validation_config import validate_studio


class ValidationStudioTests(unittest.TestCase):
    def setUp(self):
        self.cfg = json.loads((ROOT / "validation/reference_views.json").read_text(encoding="utf-8"))
        self.manifest = json.loads((ROOT / "references/manifest.json").read_text(encoding="utf-8"))
        self.hierarchy = json.loads((ROOT / "design/reference_hierarchy.json").read_text(encoding="utf-8"))

    def test_reference_crop_and_rank_errors_rejected(self):
        cfg = copy.deepcopy(self.cfg)
        cfg["views"][0]["reference_rank"] = 5
        cfg["views"][1]["reference_panel"]["crop_px"] = [0, 0, 9999, 650]
        errors = validate_studio(cfg, self.manifest, self.hierarchy)
        self.assertTrue(any("authority hierarchy" in error for error in errors))
        self.assertTrue(any("exceeds source dimensions" in error for error in errors))

    def test_invalid_projection_and_clip_range_rejected(self):
        cfg = copy.deepcopy(self.cfg)
        cfg["views"][0]["camera"]["projection"] = "PERSP"
        cfg["views"][1]["camera"]["clip_start_m"] = 1000
        errors = validate_studio(cfg)
        self.assertTrue(any("expected ORTHO" in error for error in errors))
        self.assertTrue(any("clipping range is reversed" in error for error in errors))

    def test_blank_and_overexposed_evidence_rejected(self):
        with tempfile.TemporaryDirectory() as scratch:
            path = Path(scratch) / "test.png"
            Image.new("RGB", (1024, 1024), "#363636").save(path)
            with self.assertRaisesRegex(RuntimeError, "blank"):
                image_metrics(path)
            image = Image.new("RGB", (1024, 1024), "#363636")
            image.paste("white", (100, 100, 924, 924))
            image.save(path)
            with self.assertRaisesRegex(RuntimeError, "overexposed"):
                image_metrics(path)

    def check_stored_review(self, milestone, scene):
        review = ROOT / "validation/reviews" / milestone
        verification = json.loads((review / "verification.json").read_text(encoding="utf-8"))
        manifest = json.loads((review / "render_manifest.json").read_text(encoding="utf-8"))
        digest = hashlib.sha256((ROOT / "validation/reference_views.json").read_bytes()).hexdigest()
        self.assertEqual(verification["config_sha256"], digest, "Regenerate setup-review after changing the studio")
        self.assertEqual(manifest["config_sha256"], digest)
        self.assertEqual(hashlib.sha256((ROOT / "blender/scene" / scene).read_bytes()).hexdigest(), verification["scene_sha256"])
        for name, expected in verification["fixture_sources"].items():
            self.assertEqual(hashlib.sha256((ROOT / "scripts/blender" / name).read_bytes()).hexdigest(), expected, name)
        for path, expected in verification["recipe_sources"].items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), expected, path)
        for name, expected in verification["design_sources"].items():
            self.assertEqual(hashlib.sha256((ROOT / "design" / name).read_bytes()).hexdigest(), expected, name)
        for file, expected in verification["reference_sha256"].items():
            self.assertEqual(hashlib.sha256((ROOT / "references/approved" / file).read_bytes()).hexdigest(), expected, file)
        for view in self.cfg["views"]:
            path = review / (view["name"] + ".png")
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), manifest["render_sha256"][view["name"]])
            self.assertEqual(image_metrics(path)["size"], [1024, 1024])
            self.assertTrue(verification["render_metrics"][view["name"]]["reload_pixels_identical"])
        self.assertTrue(verification["reload_before_identical"])
        self.assertTrue(verification["reload_after_identical"])
        self.assertFalse(verification["design_approval"])

    def test_stored_setup_matches_current_sources_and_pixels(self):
        self.check_stored_review('setup', 'owli_validation_setup.blend')

    def test_stored_blockout_matches_current_sources_and_pixels(self):
        self.check_stored_review('blockout_v01', 'owli_blockout_v01.blend')
        proof = json.loads((ROOT/'validation/reviews/blockout_v01/verification.json').read_text())
        self.assertTrue(proof['repeated_build_identical'])
        self.assertTrue(proof['repeated_datablock_counts_identical'])
        self.assertEqual(set(proof['blockout_checks']), {
            'separate_spherical_eyes', 'mask_and_tuft_volumes', 'toe_rule_3_plus_1',
            'rear_guides_behind_perch', 'all_toes_wrap_below_bar', 'no_toe_bar_intersection',
            'no_rig_or_duplicate_geometry', 'eye_spacing_depth_parameters_effective',
            'beak_wing_tail_parameters_effective', 'global_scale_all_geometry_effective', 'probe_restore_identical'})
        self.assertTrue(all(proof['blockout_checks'].values()))
        self.assertTrue(all(proof['reloaded_blockout_checks'].values()))
