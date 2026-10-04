"""Validate a manually authored silhouette freeze against its actual evidence.

This does not judge visual design or automatically grant approval.
"""
import hashlib
import json
from pathlib import Path


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_review(root, review):
    root = Path(root)
    errors = []
    checklist = json.loads((root/'validation/checklist.json').read_text(encoding='utf-8'))
    expected = checklist['checks']
    entries = review.get('checks', [])
    if [item.get('check') for item in entries] != expected:
        errors.append('Review must cover every checklist item in its original order')
    if review.get('status') != 'silhouette_frozen' or review.get('blocking_findings') != []:
        errors.append('Silhouette freeze requires an explicit decision and no blocking findings')
    if review.get('scope') != 'coarse_volumes_face_placement_perched_pose':
        errors.append('Freeze scope must remain coarse geometry')
    hierarchy = json.loads((root/'design/reference_hierarchy.json').read_text(encoding='utf-8'))
    ranks = {}
    for record in hierarchy['hierarchy']:
        for file in record.get('files', [record.get('file')]):
            ranks[file] = record['rank']
    for item in entries:
        if item.get('result') != 'pass' or not item.get('reason', '').strip():
            errors.append('Every checklist item needs a reasoned pass before freezing')
        refs = item.get('references', [])
        if not refs or any(ranks.get(ref.get('file')) != ref.get('rank') for ref in refs):
            errors.append('Every checklist item needs references with correct authority ranks')
        evidence = item.get('evidence', [])
        if not evidence or not any(path.endswith('.png') for path in evidence) or any(path not in review.get('evidence_sha256', {}) for path in evidence):
            errors.append('Every checklist item needs hashed visible evidence')
    required = {'design/proportions.json', 'validation/checklist.json',
                'validation/reference_views.json', 'design/reference_hierarchy.json',
                'blender/scene/owli_blockout_v01.blend'}
    required.update('references/approved/'+ref['file'] for item in entries for ref in item.get('references', []))
    required.update(f'validation/reviews/blockout_v01/{name}.png' for name in
                    ('VAL_FRONT', 'VAL_LEFT', 'VAL_BACK', 'VAL_3Q'))
    hashes = review.get('evidence_sha256', {})
    if not required.issubset(hashes):
        errors.append('Freeze must bind parameters, checklist, cameras, Blend and all four views')
    for path, expected_hash in hashes.items():
        target = (root/path).resolve()
        if not target.is_relative_to(root.resolve()) or not target.is_file():
            errors.append(f'Missing/invalid evidence: {path}')
        elif sha256(target) != expected_hash:
            errors.append(f'Stale freeze evidence; repeat visual review: {path}')
    return errors
