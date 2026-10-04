"""Inspect delivered control/evaluated surfaces and exercise their actual soft weights."""
import json
import math
from pathlib import Path
import bmesh
import bpy
from mathutils import Matrix, Vector
from mathutils.kdtree import KDTree
from mathutils.bvhtree import BVHTree
from blockout_geometry import parameters
from primary_geometry import source_tree


def audit_mesh(data, name, symmetry=False):
    bm = bmesh.new()
    bm.from_mesh(data)
    bm.verts.ensure_lookup_table()
    bm.faces.ensure_lookup_table()
    bm.normal_update()
    try:
        assert all(e.is_manifold for e in bm.edges), f'{name}: open/nonmanifold edge'
        assert all(len(f.verts)==4 and f.calc_area()>1e-12 for f in bm.faces), f'{name}: bad quad/degenerate face'
        assert all(e.is_contiguous for e in bm.edges), f'{name}: inconsistent normals'
        assert bm.calc_volume(signed=True) > 0, f'{name}: inward surface'
        assert len(bm.verts)-len(bm.edges)+len(bm.faces)==2, f'{name}: unexpected genus/shells'
        pending, visited = [bm.verts[0]], set()
        while pending:
            v=pending.pop()
            if v.index in visited: continue
            visited.add(v.index)
            pending.extend(e.other_vert(v) for e in v.link_edges)
        assert len(visited)==len(bm.verts), f'{name}: disconnected surfaces/interior caps'
        tree = KDTree(len(bm.verts))
        for v in bm.verts: tree.insert(v.co, v.index)
        tree.balance()
        for v in bm.verts:
            assert len(tree.find_range(v.co, 1e-7))==1, f'{name}: duplicate vertices'
            if symmetry:
                distance=tree.find(Vector((-v.co.x,v.co.y,v.co.z)))[2]
                assert distance<1e-6, f'{name}: symmetry lost {tuple(v.co)} delta={distance}'
        assert max(len(v.link_edges) for v in bm.verts)<=5, f'{name}: high-valence pole'
        # Reject nonlocal self intersections, allowing only adjacent polygons sharing vertices.
        tree = BVHTree.FromBMesh(bm)
        overlaps = [(a,b) for a,b in tree.overlap(tree) if a<b and
                    not (set(bm.faces[a].verts)&set(bm.faces[b].verts))]
        assert not overlaps, f'{name}: self intersections {overlaps[:5]}'
        return {'vertices':len(bm.verts),'edges':len(bm.edges),'quads':len(bm.faces),
                'euler_characteristic':2,'connected_closed_shell':True,'consistent_outward_normals':True,
                'duplicate_vertices':0,'self_intersections':0,'maximum_valence':max(len(v.link_edges) for v in bm.verts),
                'volume_m3':bm.calc_volume(signed=True)}
    finally:
        bm.free()


def inspect(root):
    cfg,scale = parameters(root)
    policy=json.loads((Path(root)/'design/head_body.json').read_text())
    names={o.name for o in bpy.data.objects if o.name.startswith('PRI_')}
    assert names=={'PRI_HeadNeckTorso','PRI_Brow_L','PRI_Brow_R','PRI_Tuft_L','PRI_Tuft_R'}, names
    assert not any(o.name.startswith(('BLK_Head','BLK_Body','BLK_Tuft_','BLK_Brow_','_PRI_SOURCE_')) for o in bpy.data.objects)
    assert not any(o.type=='ARMATURE' for o in bpy.data.objects), 'Probe must not leave a rig'
    result={}
    for name in sorted(names):
        obj=bpy.data.objects[name]
        assert tuple(obj.location)==(0,0,0) and tuple(obj.scale)==(1,1,1)
        assert all(abs(v)<1e-7 for v in obj.rotation_euler)
        assert len(obj.modifiers)==1 and obj.modifiers[0].type=='SUBSURF'
        result[name]=audit_mesh(obj.data,name,symmetry=name=='PRI_HeadNeckTorso')
        evaluated=obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
        data=evaluated.to_mesh()
        try: audit_mesh(data,name+' evaluated',symmetry=name=='PRI_HeadNeckTorso')
        finally: evaluated.to_mesh_clear()
    for kind in ('Brow','Tuft'):
        left,right=[bpy.data.objects[f'PRI_{kind}_{side}'].data for side in ('L','R')]
        kd=KDTree(len(right.vertices))
        for v in right.vertices: kd.insert(v.co,v.index)
        kd.balance()
        assert len(left.vertices)==len(right.vertices)
        assert all(kd.find(Vector((-v.co.x,v.co.y,v.co.z)))[2]<1e-6 for v in left.vertices)
    for side in ('L','R'):
        names={o.name for o in bpy.data.objects if o.name.startswith('GUIDE_Toe_'+side+'_')}
        assert names=={f'GUIDE_Toe_{side}_Front_{i}' for i in (1,2,3)}|{f'GUIDE_Toe_{side}_Rear_1'}
        assert bpy.data.objects['BLK_Eye_'+side].dimensions.x==bpy.data.objects['BLK_Eye_'+side].dimensions.z
    shell=bpy.data.objects['PRI_HeadNeckTorso']
    a,b=[v*scale for v in policy['head_weight_band_m']]
    levels={round(v.co.z/scale,6) for v in shell.data.vertices if a<v.co.z<b}
    assert len(levels)>=12,'Insufficient deforming neck loops'
    for vertex in shell.data.vertices:
        body=shell.vertex_groups['body'].weight(vertex.index)
        head=shell.vertex_groups['head_neck'].weight(vertex.index)
        assert abs(body+head-1)<1e-6
    return {'primary_meshes':result,'symmetry':True,'identity_transforms':True,'neck_loops':len(levels),
            'body_head_weights_partition_unity':True,'toe_rule_3_plus_1':True,'deferred_parts_unchanged':True,'no_rig':True}


def deform(root, probe):
    policy=json.loads((Path(root)/'design/head_body.json').read_text())
    _,scale=parameters(root)
    obj=bpy.data.objects['PRI_HeadNeckTorso']
    original=[v.co.copy() for v in obj.data.vertices]
    pivot=Vector(policy['neck_pivot_m'])*scale
    if probe in ('head_tilt','head_turn'):
        rotation=Matrix.Rotation(math.radians(policy['deformation_probes'][probe+'_deg']),3,'Y' if probe=='head_tilt' else 'Z')
        for v in obj.data.vertices:
            w=obj.vertex_groups['head_neck'].weight(v.index)
            v.co=v.co.lerp(pivot+rotation@(v.co-pivot),w)
    else:
        side=probe[-1]
        for v in obj.data.vertices:
            w=obj.vertex_groups['wing_root_'+side].weight(v.index)
            v.co.x+=(1 if side=='R' else -1)*w*policy['deformation_probes']['wing_root_displacement_m']*scale
    obj.data.update()
    bpy.context.view_layer.update()
    return original


def exercise(root):
    obj=bpy.data.objects['PRI_HeadNeckTorso']
    result={}
    for probe in ('head_tilt','head_turn','wing_root_L','wing_root_R'):
        original=deform(root,probe)
        try:
            result[probe]=audit_mesh(obj.data,probe)
            evaluated=obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
            data=evaluated.to_mesh()
            try: result[probe]['evaluated']=audit_mesh(data,probe+' evaluated')
            finally: evaluated.to_mesh_clear()
            edges=obj.data.edges
            ratios=[]
            for edge in edges:
                a,b=edge.vertices
                before=(original[a]-original[b]).length
                ratios.append((obj.data.vertices[a].co-obj.data.vertices[b].co).length/before)
            assert min(ratios)>.65 and max(ratios)<1.5,(probe,min(ratios),max(ratios))
            result[probe]['edge_length_ratio_range']=[min(ratios),max(ratios)]
            result[probe]['maximum_displacement_m']=max((v.co-p).length for v,p in zip(obj.data.vertices,original))
            assert result[probe]['maximum_displacement_m']>.005
        finally:
            for v,p in zip(obj.data.vertices,original): v.co=p
            obj.data.update()
            bpy.context.view_layer.update()
    return result


def envelope_deviation(root, sources):
    """Measure evaluated primary vertices against the corresponding frozen surfaces."""
    policy=json.loads((Path(root)/'design/head_body.json').read_text())
    _,scale=parameters(root)
    result={}
    for name,trees in sources.items():
        obj=bpy.data.objects[name]
        evaluated=obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
        data=evaluated.to_mesh()
        try:
            distances=[min(tree.find_nearest(v.co)[3] for tree in trees) for v in data.vertices]
            maximum=max(distances)
            worst=tuple(data.vertices[distances.index(maximum)].co)
            assert maximum <= policy['surface_tolerance_m']*scale,(name,maximum,policy['surface_tolerance_m']*scale,worst)
            result[name]={'evaluated_vertices_measured':len(distances),'maximum_distance_m':maximum,
                          'mean_distance_m':sum(distances)/len(distances),'tolerance_m':policy['surface_tolerance_m']*scale}
        finally:
            evaluated.to_mesh_clear()
    return result


def rejection_probes():
    """Demonstrate that audits reject broken delivered geometry, not just valid fixtures."""
    original=bpy.data.objects['PRI_HeadNeckTorso'].data
    result={}
    for kind in ('open_surface','reversed_face','disconnected_vertex','asymmetric_vertex'):
        data=original.copy()
        bm=bmesh.new()
        try:
            bm.from_mesh(data)
            bm.faces.ensure_lookup_table()
            bm.verts.ensure_lookup_table()
            if kind=='open_surface': bmesh.ops.delete(bm,geom=[bm.faces[0]],context='FACES_ONLY')
            elif kind=='reversed_face': bm.faces[0].normal_flip()
            elif kind=='disconnected_vertex': bm.verts.new((0,0,1))
            else: bm.verts[0].co.x+=.001
            bm.to_mesh(data)
            try: audit_mesh(data,kind,symmetry=True)
            except AssertionError: result[kind+'_rejected']=True
            else: raise AssertionError('Invalid geometry passed: '+kind)
        finally:
            bm.free()
            bpy.data.meshes.remove(data)
    return result
