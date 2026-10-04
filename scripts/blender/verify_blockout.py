"""Inspect real milestone geometry and exercise parameters in an isolated build."""
import copy
import json
from pathlib import Path
import runpy
import bpy
from mathutils import Vector
from blockout_geometry import parameters
from validation_setup import geometry_objects, read_config
from verify_validation_setup import geometry_digest


def inspect(root):
    cfg, scale = parameters(root)
    for side, sign in (('L', -1), ('R', 1)):
        eye = bpy.data.objects['BLK_Eye_' + side]
        assert len(eye.data.vertices) > 100
        assert all(abs(v-2*cfg['eyes']['radius']*scale) < 1e-6 for v in eye.dimensions)
        assert abs(eye.location.x-sign*cfg['eyes']['half_spacing']*scale) < 1e-6
        assert abs(eye.location.y-cfg['eyes']['depth']*scale) < 1e-6
        assert bpy.data.objects['BLK_Mask_'+side].dimensions.z > eye.dimensions.z
        assert bpy.data.objects['BLK_Tuft_'+side].dimensions.z > .05*scale
        names = {o.name for o in bpy.data.objects if o.name.startswith('GUIDE_Toe_'+side+'_')}
        assert names == {f'GUIDE_Toe_{side}_Front_{i}' for i in (1, 2, 3)} | {f'GUIDE_Toe_{side}_Rear_1'}
        bar = cfg['perch']['bar']
        for name in names:
            obj = bpy.data.objects[name]
            centers = json.loads(obj['guide_centerline'])
            rear = '_Rear_' in name
            assert all((p[1]-bar['center'][1]*scale)*(-1 if rear else 1) > 0 for p in centers)
            assert centers[-1][2] < bar['center'][2]*scale < centers[0][2]
            expected = (bar['radius']+cfg['feet']['path_clearance'])*scale
            for center in centers:
                distance = ((center[1]-bar['center'][1]*scale)**2+(center[2]-bar['center'][2]*scale)**2)**.5
                assert abs(distance-expected) < 1e-7
            # No guide vertices pass through the metal support cylinder.
            for vertex in obj.data.vertices:
                world = obj.matrix_world @ vertex.co
                distance = ((world.y-bar['center'][1]*scale)**2+(world.z-bar['center'][2]*scale)**2)**.5
                assert distance >= bar['radius']*scale-1e-6
    assert not any(o.type == 'ARMATURE' for o in bpy.data.objects)
    assert not any('.00' in o.name for o in geometry_objects(read_config(root)))
    return {'separate_spherical_eyes': True, 'mask_and_tuft_volumes': True,
            'toe_rule_3_plus_1': True, 'rear_guides_behind_perch': True,
            'all_toes_wrap_below_bar': True, 'no_toe_bar_intersection': True,
            'no_rig_or_duplicate_geometry': True}


def exercise(root):
    """Controlled parameter probes, never published as design iterations."""
    root = Path(root)
    scripts = Path(__file__).resolve().parent
    path = root/'design/proportions.json'
    source = path.read_text()
    cfg = json.loads(source)
    spec_path = root/'design/character_spec.json'
    spec_source = spec_path.read_text()
    studio = read_config(root)
    baseline = geometry_digest(studio)

    def build():
        for name in ('10_blockout.py', '40_feet_perch.py'):
            runpy.run_path(str(scripts/name), run_name='__main__')

    def bounds(name):
        obj = bpy.data.objects[name]
        return [tuple(obj.matrix_world @ Vector(p)) for p in obj.bound_box]

    try:
        changed = copy.deepcopy(cfg)
        changed['eyes']['half_spacing'] += .008
        changed['eyes']['depth'] += .01
        changed['beak'] = [[z, x, y+.009, rx, ry] for z,x,y,rx,ry in cfg['beak']]
        changed['wing'] = [[z, x+.007, y, rx*1.1, ry] for z,x,y,rx,ry in cfg['wing']]
        changed['tail'] = [[z, x, y-.012, rx, ry] for z,x,y,rx,ry in cfg['tail']]
        before = {name: bounds(name) for name in ('BLK_Beak','BLK_Wing_R','BLK_Tail')}
        path.write_text(json.dumps(changed))
        build()
        inspect(root)
        assert all(bounds(name) != old for name, old in before.items())
        assert abs(bpy.data.objects['BLK_Beak'].bound_box[0][1] - before['BLK_Beak'][0][1]-.009) < 1e-6
        path.write_text(source)
        build()
        assert geometry_digest(studio) == baseline
        original = {o.name: bounds(o.name) for o in geometry_objects(studio)}
        spec = json.loads(spec_source)
        spec['production_scale']['character_height_m'] *= .8
        spec_path.write_text(json.dumps(spec))
        build()
        inspect(root)
        for name, points in original.items():
            for old, new in zip(points, bounds(name)):
                assert all(abs(a*.8-b) < 1e-6 for a,b in zip(old,new)), name
    finally:
        path.write_text(source)
        spec_path.write_text(spec_source)
        build()
    assert geometry_digest(studio) == baseline
    return {'eye_spacing_depth_parameters_effective': True, 'beak_wing_tail_parameters_effective': True,
            'global_scale_all_geometry_effective': True, 'probe_restore_identical': True}
