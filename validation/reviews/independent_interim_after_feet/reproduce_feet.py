"""Independently rerun the complete accepted #5 recipe in a persistent scratch dir.

Unlike feet_review.build_review, this never replaces repository delivery artifacts.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'scripts'))
from project import find_blender


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--blender')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    scratch = args.output.resolve()
    scratch.mkdir(parents=True, exist_ok=False)
    shutil.copytree(ROOT / 'design', scratch / 'design')
    (scratch / 'validation').mkdir()
    shutil.copy2(ROOT / 'validation/reference_views.json', scratch / 'validation/reference_views.json')
    scene = scratch / 'tmp/feet/prototype.blend'
    scene.parent.mkdir(parents=True)
    shutil.copy2(ROOT / 'blender/scene/owli_beak_v01.blend', scene)
    env = dict(os.environ)
    env.pop('OWLI_RENDER_SIZE', None)
    env.pop('OWLI_VALIDATION_OUTPUT', None)
    commands = []
    for mode in ('build', 'reload_a', 'reload_b'):
        env['OWLI_FEET_MODE'] = mode
        command = [find_blender(args.blender), '--background', str(scene), '--python-exit-code', '1',
                   '--python', str(ROOT / 'scripts/blender/feet_evidence.py')]
        with (scratch / (mode + '.log')).open('w', encoding='utf-8') as log:
            process = subprocess.run(command, cwd=scratch, env=env, stdout=log, stderr=subprocess.STDOUT)
        commands.append(dict(command=command, cwd=str(scratch), mode=mode, exit_code=process.returncode))
        (scratch / 'commands.json').write_text(json.dumps(commands, indent=2) + '\n', encoding='utf-8', newline='\n')
        if process.returncode:
            raise RuntimeError(f'{mode} failed; inspect {scratch / (mode + ".log")}')
    build, a, b = [json.loads((scratch / (n + '_checks.json')).read_text(encoding='utf-8'))
                   for n in ('build', 'reload_a', 'reload_b')]
    accepted = json.loads((ROOT / 'validation/reviews/feet_v01/verification.json').read_text(encoding='utf-8'))
    assert a == b and all(build[k] == v for k, v in a.items())
    assert build == accepted['build'], 'Fresh reproduction differs from accepted build checks'
    result = dict(reload_checks_identical=True, accepted_build_checks_identical=True, pixels={})
    for view in ('VAL_FRONT', 'VAL_LEFT', 'VAL_BACK', 'VAL_3Q'):
        paths = [scratch / 'validation' / mode / (view + '.png') for mode in ('reload_a', 'reload_b')]
        paths.append(ROOT / 'validation/reviews/feet_v01' / (view + '.png'))
        with Image.open(paths[0]) as im_a, Image.open(paths[1]) as im_b, Image.open(paths[2]) as im_c:
            assert im_a.tobytes() == im_b.tobytes() == im_c.tobytes(), view
        result['pixels'][view] = dict(reload_pixels_identical=True, accepted_pixels_identical=True)
    (scratch / 'comparison.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8', newline='\n')
    print('INDEPENDENT FEET REPRODUCTION OK:', scratch)


if __name__ == '__main__':
    main()
