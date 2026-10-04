"""Real archived fixtures: omissions and changed criteria must fail closed."""
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from evidence_contracts import HISTORY_CONTRACT
from history_gate import validate_history, relocated_metadata


class HistoryV2Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        names = ['validation/history/pre_feet_v01/manifest.json']
        names += [item['path'] for item in HISTORY_CONTRACT['source_relocations'].values()]
        names += [item['snapshot'] for item in HISTORY_CONTRACT['metadata_relocations'].values()]
        names += list(HISTORY_CONTRACT['metadata_relocations'])
        for name in names:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

    def write_manifest(self, manifest):
        (self.root / 'validation/history/pre_feet_v01/manifest.json').write_text(json.dumps(manifest), encoding='utf-8')

    def test_complete_git_anchored_history_passes(self):
        self.assertEqual(validate_history(self.root), [])

    def test_empty_and_every_shortened_map_fails(self):
        for field in ('source_relocations', 'metadata_relocations'):
            modified = copy.deepcopy(HISTORY_CONTRACT)
            modified[field] = {}
            self.write_manifest(modified)
            self.assertTrue(validate_history(self.root))
            for key in HISTORY_CONTRACT[field]:
                with self.subTest(field=field, key=key):
                    modified = copy.deepcopy(HISTORY_CONTRACT)
                    del modified[field][key]
                    self.write_manifest(modified)
                    self.assertTrue(validate_history(self.root))
        self.write_manifest({'source_relocations': {}, 'metadata_relocations': {}})
        self.assertTrue(validate_history(self.root))

    def test_each_missing_snapshot_reports_error_without_exception(self):
        for key, record in HISTORY_CONTRACT['metadata_relocations'].items():
            with self.subTest(key=key):
                path = self.root / record['snapshot']
                original = path.read_bytes()
                path.unlink()
                errors = validate_history(self.root)
                self.assertTrue(any(record['snapshot'] in e for e in errors), errors)
                path.write_bytes(original)

    def test_changed_archive_even_with_empty_manifest_fails(self):
        self.write_manifest({'source_relocations': {}, 'metadata_relocations': {}})
        for record in HISTORY_CONTRACT['source_relocations'].values():
            path = self.root / record['path']
            path.write_bytes(path.read_bytes() + b'\n# unauthorized edit\n')
        errors = validate_history(self.root)
        self.assertEqual(sum('source differs' in e for e in errors), 2)

    def test_changed_historical_criterion_cannot_be_rebound_by_manifest(self):
        path = self.root / 'design/silhouette_freeze.json'
        modified = json.loads(path.read_bytes())
        modified['checks'][0]['reason'] = 'Invented retroactive acceptance'
        path.write_text(json.dumps(modified), encoding='utf-8')
        errors = validate_history(self.root)
        self.assertTrue(any('non-dependency' in e for e in errors), errors)
        self.assertTrue(any('historical bytes changed' in e for e in errors), errors)

    def test_hash_looking_criterion_and_nested_fields_are_not_rewritten(self):
        record = next(iter(HISTORY_CONTRACT['metadata_relocations'].values()))
        original = {'source_sha256': {'evidence.json': record['before_sha256']},
                    'criteria': [{'reason': record['before_sha256'],
                                  'source_sha256': {'evidence.json': record['before_sha256']}}]}
        result = relocated_metadata(original)
        self.assertEqual(result['criteria'], original['criteria'])
        self.assertEqual(result['source_sha256']['evidence.json'], record['after_sha256'])
        with self.assertRaises(ValueError):
            relocated_metadata({'source_sha256': {'nested': {'hash': record['before_sha256']}}})
