"""Replace the frozen coarse head/body with editable continuous primary topology."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from primary_geometry import build
from blockout_geometry import save

ROOT = Path.cwd()
build(ROOT)
save(ROOT)
print('PRIMARY FORMS BUILT: continuous quad torso/neck/head; symmetric brow/tufts. Rig/lookdev follow separately.')
