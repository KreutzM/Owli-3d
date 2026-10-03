"""Regression checks for setup failures that previously went unnoticed."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("project", ROOT / "scripts/project.py")
project = importlib.util.module_from_spec(spec)
spec.loader.exec_module(project)


class ToolingTests(unittest.TestCase):
    def test_invalid_explicit_blender_does_not_fall_back(self):
        with patch.object(project.shutil, "which", return_value=None):
            with self.assertRaises(RuntimeError):
                project.find_blender(str(ROOT / "missing-blender"))

    def test_subprocess_failure_propagates(self):
        with self.assertRaises(subprocess.CalledProcessError):
            project.run([sys.executable, "-c", "raise SystemExit(7)"])

    def test_scene_command_preserves_existing_file(self):
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            scene = root / "blender/scene/owli.blend"
            scene.parent.mkdir(parents=True)
            scene.write_bytes(b"existing production scene")
            with patch.object(project, "ROOT", root), patch.object(sys, "argv", ["project.py", "scene"]):
                self.assertEqual(project.main(), 1)
            self.assertEqual(scene.read_bytes(), b"existing production scene")

    def test_reference_priority_and_required_views_rejected(self):
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            shutil.copytree(ROOT / "design", root / "design")
            shutil.copytree(ROOT / "validation", root / "validation", ignore=shutil.ignore_patterns("renders"))
            shutil.copytree(ROOT / "references", root / "references")
            (root / "scripts").mkdir()
            shutil.copy2(ROOT / "scripts/validate_project.py", root / "scripts")
            hierarchy_path = root / "design/reference_hierarchy.json"
            hierarchy = json.loads(hierarchy_path.read_text(encoding="utf-8"))
            hierarchy["hierarchy"][0]["rank"] = 5
            hierarchy_path.write_text(json.dumps(hierarchy), encoding="utf-8")
            views_path = root / "validation/reference_views.json"
            views = json.loads(views_path.read_text(encoding="utf-8"))
            views["views"][1]["name"] = "VAL_FRONT"
            views_path.write_text(json.dumps(views), encoding="utf-8")
            result = subprocess.run([sys.executable, str(root / "scripts/validate_project.py"), "--strict-assets"],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("reference hierarchy rank 1", result.stdout)
            self.assertIn("left profile", result.stdout)
