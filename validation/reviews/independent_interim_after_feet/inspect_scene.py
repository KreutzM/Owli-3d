"""Read-only #33 scene review; all mutations stay in the process or scratch copy.

Run from the repository with OWLI_INTERIM_OUTPUT set to a fresh scratch directory.
This supplements milestone checks; it never grants visual design approval.
"""
import hashlib
import json
import os
from pathlib import Path
import sys

import bmesh
import bpy
from mathutils import Vector

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / 'scripts/blender'))
from primary_geometry import source_tree
from validation_setup import read_config, setup, studio_snapshot, frame_bounds
from verify_face import audit, digest_part, exercise as face_exercise
from verify_beak import exercise as beak_exercise
from verify_primary import audit_mesh, exercise as primary_exercise, rejection_probes
from verify_feet import inspect as feet_inspect

OUT = Path(os.environ['OWLI_INTERIM_OUTPUT'])
OUT.mkdir(parents=True, exist_ok=True)
MODE = os.environ.get('OWLI_INTERIM_MODE', 'neutral')


def write(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8', newline='\n')


def topology(data):
    bm = bmesh.new()
    try:
        bm.from_mesh(data)
        bm.verts.ensure_lookup_table()
        remaining = set(bm.verts)
        sizes = []
        while remaining:
            pending = [next(iter(remaining))]
            count = 0
            while pending:
                v = pending.pop()
                if v not in remaining:
                    continue
                remaining.remove(v)
                count += 1
                pending.extend(e.other_vert(v) for e in v.link_edges)
            sizes.append(count)
        return dict(vertices=len(bm.verts), edges=len(bm.edges), faces=len(bm.faces),
                    nonmanifold_edges=sum(not e.is_manifold for e in bm.edges),
                    inconsistent_edges=sum(e.is_manifold and not e.is_contiguous for e in bm.edges),
                    loose_vertices=sum(not v.link_edges for v in bm.verts),
                    loose_edges=sum(not e.link_faces for e in bm.edges),
                    degenerate_faces=sum(f.calc_area() <= 1e-12 for f in bm.faces),
                    signed_volume_m3=bm.calc_volume(signed=True), connected_component_sizes=sizes,
                    polygon_sizes=sorted(set(len(f.verts) for f in bm.faces)))
    finally:
        bm.free()


def render_set(folder, names=None):
    # Use saved cameras and scene settings directly. Only output path/visibility changes.
    folder = OUT / folder
    folder.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    saved = {o.name: o.hide_render for o in scene.objects if o.type == 'MESH'}
    transparent = scene.render.film_transparent
    if names is not None:
        scene.render.film_transparent = True
        for name in saved:
            bpy.data.objects[name].hide_render = name not in names
    try:
        for name in ('VAL_FRONT', 'VAL_LEFT', 'VAL_BACK', 'VAL_3Q'):
            scene.camera = bpy.data.objects[name]
            scene.render.filepath = str((folder / (name + '.png')).resolve())
            bpy.ops.render.render(write_still=True)
    finally:
        for name, hidden in saved.items():
            bpy.data.objects[name].hide_render = hidden
        scene.render.film_transparent = transparent


scene = bpy.context.scene
before_hash = hashlib.sha256(Path(bpy.data.filepath).read_bytes()).hexdigest()
before_parts = {o.name: digest_part(o) for o in scene.objects if o.type == 'MESH'}
before_studio = studio_snapshot()
cfg = read_config(ROOT)
cameras = [bpy.data.objects[v['name']] for v in cfg['views']]
framing = frame_bounds(cfg, cameras)
setup(ROOT)
assert before_studio == studio_snapshot(), 'Saved studio differs from documented canonical setup'
assert before_parts == {o.name: digest_part(o) for o in scene.objects if o.type == 'MESH'}

if MODE == 'neutral':
    records = {}
    depsgraph = bpy.context.evaluated_depsgraph_get()
    meshes = sorted((o for o in scene.objects if o.type == 'MESH'), key=lambda o: o.name)
    for obj in sorted(scene.objects, key=lambda o: o.name):
        record = dict(type=obj.type, collections=[c.name for c in obj.users_collection],
                      location=list(obj.location), rotation=list(obj.rotation_euler), scale=list(obj.scale),
                      matrix_world=[list(row) for row in obj.matrix_world], parent=obj.parent.name if obj.parent else None,
                      hide_render=obj.hide_render, hide_viewport=obj.hide_viewport, hidden=obj.hide_get())
        if obj.type == 'MESH':
            record.update(topology=topology(obj.data), digest=digest_part(obj),
                          materials=[m.name for m in obj.data.materials],
                          groups=[g.name for g in obj.vertex_groups],
                          modifiers=[dict(name=m.name, type=m.type, levels=getattr(m, 'levels', None),
                                          render_levels=getattr(m, 'render_levels', None)) for m in obj.modifiers])
            evaluated = obj.evaluated_get(depsgraph)
            data = evaluated.to_mesh()
            try:
                record['evaluated_topology'] = topology(data)
                points = [obj.matrix_world @ v.co for v in data.vertices]
                record['evaluated_world_bounds_m'] = [[min(p[i] for p in points) for i in range(3)],
                                                     [max(p[i] for p in points) for i in range(3)]]
            finally:
                evaluated.to_mesh_clear()
        records[obj.name] = record
    collisions = []
    trees = {o.name: source_tree(o)[0] for o in meshes}
    for i, a in enumerate(meshes):
        for b in meshes[i + 1:]:
            pairs = trees[a.name].overlap(trees[b.name])
            if pairs:
                collisions.append(dict(a=a.name, b=b.name, triangle_pairs=len(pairs)))
    result = dict(scene_path=bpy.data.filepath, scene_sha256=before_hash, blender_version=bpy.app.version_string,
                  objects=records, object_count=len(scene.objects), mesh_count=len(meshes),
                  collections={c.name: [o.name for o in c.objects] for c in bpy.data.collections},
                  scene_units=dict(system=scene.unit_settings.system, scale_length=scene.unit_settings.scale_length),
                  datablocks=dict(objects=len(bpy.data.objects), meshes=len(bpy.data.meshes),
                                  orphan_meshes=[m.name for m in bpy.data.meshes if m.users == 0],
                                  objects_outside_scene=[o.name for o in bpy.data.objects if o.name not in scene.objects],
                                  actions=[a.name for a in bpy.data.actions],
                                  libraries=[dict(name=l.name, path=l.filepath) for l in bpy.data.libraries],
                                  images=[dict(name=im.name, path=im.filepath, packed=bool(im.packed_file),
                                               source=im.source) for im in bpy.data.images]),
                  studio_before=before_studio, canonical_studio_identical=True, framing=framing,
                  evaluated_surface_intersections=collisions, feet=feet_inspect(ROOT),
                  material_nodes={m.name: [n.type for n in m.node_tree.nodes] if m.use_nodes else [] for m in bpy.data.materials})
    write('scene-inspection.json', result)
    render_set('neutral')
    render_set('toes', {o.name for o in meshes if o.name.startswith(('GRP_Foot', 'GRP_Claw'))})
else:
    result = {'primary': {}, 'face_meshes': {}, 'beak_meshes': {}}
    for obj in scene.objects:
        if obj.name.startswith('PRI_'):
            result['primary'][obj.name] = audit_mesh(obj.data, obj.name, symmetry=obj.name == 'PRI_HeadNeckTorso')
        elif obj.type == 'MESH' and obj.name.startswith('FAC_'):
            result['face_meshes'][obj.name] = audit(obj)
        elif obj.type == 'MESH' and obj.name.startswith('BAK_'):
            result['beak_meshes'][obj.name] = audit(obj)
    # Reuse specific compatible checks; historical full inspectors expect replaced guides.
    result['head_neck_wing_root_probes'] = primary_exercise(ROOT)
    result['primary_negative_probes'] = rejection_probes()
    result['blink_gaze_probes'] = face_exercise(ROOT)
    result['beak_open_probes'] = beak_exercise(ROOT)
    result['feet'] = feet_inspect(ROOT)
    from face_geometry import set_blink
    from beak_geometry import set_open
    set_blink(ROOT, 1)
    render_set('blink')
    set_blink(ROOT, 0)
    set_open(ROOT, 1)
    render_set('beak_open')
    set_open(ROOT, 0)
    assert before_parts == {o.name: digest_part(o) for o in scene.objects if o.type == 'MESH'}, 'Probe did not restore neutral'
    write('movement-probes.json', result)

assert hashlib.sha256(Path(bpy.data.filepath).read_bytes()).hexdigest() == before_hash, 'Source blend changed'
print('INDEPENDENT INTERIM INSPECTION OK:', MODE)
