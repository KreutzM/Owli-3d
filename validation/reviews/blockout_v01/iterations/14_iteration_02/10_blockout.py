"""Build the parameterized perched coarse volumes, before topology/lookdev/rig."""
from pathlib import Path
import sys
import math
import bpy
sys.path.insert(0, str(Path(__file__).resolve().parent))
from blockout_geometry import parameters, clean, swatch, finish, ellipsoid, loft, cap, save

ROOT = Path.cwd()
cfg, S = parameters(ROOT)
clean('BLK_')
colors = {key: swatch(ROOT, key) for key in ('deep_navy', 'mid_blue', 'cyan_reference', 'cream', 'orange_reference')}
navy, blue, cyan, cream, orange = [colors[key] for key in colors]
for key, name, group, material in (
    ('body', 'BLK_Body', 'BLOCKOUT', blue), ('head', 'BLK_Head', 'BLOCKOUT', navy),
    ('tail', 'BLK_Tail', 'BLOCKOUT', navy), ('beak', 'BLK_Beak', 'BEAK', orange),
    ('mask_bridge', 'BLK_MaskBridge', 'BLOCKOUT', cream), ('chest', 'BLK_Chest', 'BLOCKOUT', cream)):
    loft(name, cfg[key], S, group, material)
for key, p in cfg['perch'].items():
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=p['radius']*S, depth=p['length']*S,
        location=[v*S for v in p['center']], rotation=(0, math.pi/2 if p['axis']=='X' else 0, 0))
    finish(bpy.context.object, 'BLK_Perch'+key.title(), 'PERCH', navy)
for side, sign in (('L', -1), ('R', 1)):
    loft('BLK_Wing_'+side, cfg['wing'], S, 'WINGS', blue, sign)
    loft('BLK_Tuft_'+side, cfg['tuft'], S, 'BLOCKOUT', navy, sign)
    loft('BLK_ChestAccent_'+side, cfg['chest_accent'], S, 'BLOCKOUT', orange, sign)
    for key in ('mask', 'brow'):
        p = cfg[key]
        center = [sign*p['center'][0], *p['center'][1:]]
        obj = ellipsoid('BLK_'+key.title()+'_'+side, center, p['dimensions'], S, 'BLOCKOUT', cream if key=='mask' else navy)
        if key=='brow':
            obj.rotation_euler.y = sign*p['tilt_y']
    p = cfg['eyes']
    center = [sign*p['half_spacing'], p['depth'], p['height']]
    ellipsoid('BLK_Eye_'+side, center, [2*p['radius']]*3, S, 'EYES', navy)
    cap('BLK_IrisGuide_'+side, center, p['radius']+p['cap_offset'], p['iris_angle'], S, cyan)
    cap('BLK_PupilGuide_'+side, center, p['radius']+2*p['cap_offset'], p['pupil_angle'], S, navy)
# Coarse logo landmark: reserves forehead placement, without lookdev or feather detail.
from mathutils import Vector
p = cfg['forehead_guide']
points = [Vector(p['center']) + Vector(local) for local in p['nodes']]
for i, point in enumerate(points):
    diameter = p['center_diameter'] if i == 0 else p['node_diameter']
    obj = ellipsoid('BLK_ForeheadNode_'+str(i), point, [diameter]*3, S, 'TECH', cyan)
    obj['status'] = p['status']
for i, (a, b) in enumerate(p['edges']):
    direction = points[b]-points[a]
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=p['line_radius']*S,
        depth=direction.length*S, location=(points[a]+points[b])*S/2)
    obj = finish(bpy.context.object, 'BLK_ForeheadLink_'+str(i), 'TECH', cyan)
    obj.rotation_euler = direction.to_track_quat('Z', 'Y').to_euler()
    obj['status'] = p['status']
bpy.context.scene['blockout_parameters'] = 'design/proportions.json'
bpy.context.scene['blockout_design_approval'] = False
save(ROOT)
print('Parameterized coarse blockout; no silhouette or material approval.')
