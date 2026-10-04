"""Execute historical coarse feet and current coarse dispatch on scratch scenes."""
import hashlib
import json
from pathlib import Path
import runpy
import sys
import bpy

SOURCE=Path(__file__).resolve().parents[3]/'scripts/blender'
sys.path.insert(0,str(SOURCE))
from verify_validation_setup import geometry_digest
from validation_setup import read_config

for stage in ('00_scene_setup.py','10_blockout.py','legacy/40_feet_perch.py'):
    runpy.run_path(str(SOURCE/stage),run_name='__main__')
bpy.context.view_layer.update()

def signature():
    data={}
    for obj in sorted(bpy.data.objects,key=lambda o:o.name):
        state={'type':obj.type,'matrix':[list(row) for row in obj.matrix_world],
               'collection':sorted(c.name for c in obj.users_collection),
               'props':{k:obj[k] for k in obj.keys()}}
        if obj.type=='MESH':
            state.update(vertices=[list(v.co) for v in obj.data.vertices],
                         polygons=[list(p.vertices) for p in obj.data.polygons],
                         normals=[list(p.normal) for p in obj.data.polygons],
                         smooth=[p.use_smooth for p in obj.data.polygons],
                         assignments=[p.material_index for p in obj.data.polygons],
                         materials=[m.name for m in obj.data.materials],
                         modifiers=[(m.name,m.type) for m in obj.modifiers])
        data[obj.name]=state
    return hashlib.sha256(json.dumps(data,sort_keys=True).encode()).hexdigest()

before=signature()
before_geometry=geometry_digest(read_config(Path.cwd()))
counts=(len(bpy.data.objects),len(bpy.data.meshes),len(bpy.data.materials))
runpy.run_path(str(SOURCE/'40_feet_perch.py'),run_name='__main__')
bpy.context.view_layer.update()
after=signature()
report={'archived_coarse_signature':before,'current_dispatch_signature':after,
        'archived_coarse_geometry':before_geometry,
        'current_dispatch_geometry':geometry_digest(read_config(Path.cwd())),
        'before_counts':counts,'after_counts':(len(bpy.data.objects),len(bpy.data.meshes),len(bpy.data.materials)),
        'identical':before==after}
assert before==after,report
Path('coarse-dispatch.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(report))
