import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from history_bindings import validate_history


class HistoricalBindingsTests(unittest.TestCase):
    def test_original_sources_and_decisions_were_preserved(self):
        self.assertEqual(validate_history(ROOT),[])
