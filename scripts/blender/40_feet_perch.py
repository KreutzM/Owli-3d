"""Create foot/toe guide objects enforcing Owli's locked 3+1 anatomy."""
from pathlib import Path
import bpy, math, json

ROOT=Path.cwd()
spec=json.loads((ROOT/"design"/"character_spec.json").read_text())
feet=spec["anatomy"]["feet"]
assert feet["forward_toes"]==3 and feet["rear_toes"]==1

S=float(spec["production_scale"]["character_height_m"])/0.45

def collection(name): return bpy.data.collections[name]

def move_to(obj,name):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    collection(name).objects.link(obj)

def capsule(name,loc,scale,rot=(0,0,0),collection_name="FEET"):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24,ring_count=12,location=loc,rotation=rot)
    o=bpy.context.object
    o.name=name
    o.scale=scale
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    bpy.ops.object.shade_smooth()
    move_to(o,collection_name)
    o["status"]="anatomy_guide"
    return o

for obj in list(bpy.data.objects):
    if obj.name.startswith(("GUIDE_Foot","GUIDE_Toe","GUIDE_Claw")):
        bpy.data.objects.remove(obj,do_unlink=True)

for side,sx in (("L",-1),("R",1)):
    fx=0.052*S*sx
    capsule(f"GUIDE_Foot_{side}",(fx,0.014*S,0.112*S),(0.035*S,0.026*S,0.022*S))

    # Three forward toes: spread across X and extend toward +Y.
    for i,dx in enumerate((-0.019,0.0,0.019),1):
        capsule(f"GUIDE_Toe_{side}_Front_{i}",(fx+dx*S,0.045*S,0.098*S),
                (0.009*S,0.036*S,0.010*S),(0,0,dx*7),"FEET")

    # One rear toe: centered behind perch, extends toward -Y.
    capsule(f"GUIDE_Toe_{side}_Rear_1",(fx,-0.030*S,0.098*S),
            (0.010*S,0.032*S,0.011*S),(0,0,0),"FEET")

for o in collection("FEET").objects:
    if o.name.startswith("GUIDE_Toe"):
        o["locked_toe_rule"]="3 forward + 1 rear per foot"

bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/"blender"/"scene"/"owli.blend"))
print("Created foot anatomy guides: exactly 3 forward + 1 rear toe per foot.")
