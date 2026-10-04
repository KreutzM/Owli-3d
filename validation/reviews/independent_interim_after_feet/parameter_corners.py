"""Independent permitted rectangle and invalid configuration checks; never save scene."""
import json
import sys
from pathlib import Path
import bpy

repo = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(repo / 'scripts/blender'))
from feet_geometry import build, config
from verify_feet import inspect

scratch = repo / 'tmp/independent-review-33/parameter-corners'
scratch.mkdir(exist_ok=True)
import shutil
shutil.copytree(repo / 'design', scratch / 'design', dirs_exist_ok=True)
path = scratch / 'design/feet.json'
original = json.loads(path.read_text(encoding='utf-8'))
results = {'allowed': [], 'rejected': []}
for radius, spacing in [(0.016, 0.05), (0.016, 0.062), (0.022, 0.05), (0.022, 0.062), (0.019, 0.056)]:
    cfg = dict(original, bar_radius_m=radius, foot_half_spacing_m=spacing)
    path.write_text(json.dumps(cfg), encoding='utf-8', newline='\n')
    build(scratch)
    proof = inspect(scratch)
    results['allowed'].append({'bar_radius_m': radius, 'foot_half_spacing_m': spacing, 'contacts': len(proof['contacts']), 'collision_pairs': proof['independent_surface_collision_pairs'], 'valid': True})
    print('CORNER PASS', radius, spacing, flush=True)
for key, value in [('bar_radius_m', 0.0159), ('bar_radius_m', 0.0221), ('foot_half_spacing_m', 0.0499), ('foot_half_spacing_m', 0.0621)]:
    cfg = dict(original)
    cfg[key] = value
    path.write_text(json.dumps(cfg), encoding='utf-8', newline='\n')
    try:
        config(scratch)
    except AssertionError as exc:
        results['rejected'].append({'parameter': key, 'value': value, 'reason': str(exc)})
    else:
        raise AssertionError(f'Invalid parameter accepted: {key}={value}')
(repo / 'tmp/independent-review-33/parameter-corners.json').write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8', newline='\n')
print('INDEPENDENT PARAMETER CORNERS OK', flush=True)
