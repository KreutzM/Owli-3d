"""Create a deliberately simple Owli blockout.

Run only after 00_scene_setup.py. This is a starting volume model, not an approved final mesh.
"""
from pathlib import Path
import bpy, json, math

ROOT=Path.cwd()
spec=json.loads((ROOT/"design"/"character_spec.json").read_text())
H=float(spec["production_scale"]["character_height_m"])
S=H/0.45

def col(name): return bpy.data.collections[name]

def move_to(obj,name):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col(name).objects.link(obj)

def clean_prefix(prefix="BLK_"):
    for obj in list(bpy.data.objects):
        if obj.name.startswith(prefix):
            bpy.data.objects.remove(obj,do_unlink=True)

def ellipsoid(name,loc,dims,collection="BLOCKOUT"):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, location=loc)
    o=bpy.context.object
    o.name=name
    o.scale=(dims[0]/2,dims[1]/2,dims[2]/2)
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    bpy.ops.object.shade_smooth()
    move_to(o,collection)
    return o

def cylinder(name,loc,radius,depth,axis="Z",collection="BLOCKOUT"):
    rot=(0,0,0)
    if axis=="X": rot=(0,math.pi/2,0)
    bpy.ops.mesh.primitive_cylinder_add(vertices=48,radius=radius,depth=depth,location=loc,rotation=rot)
    o=bpy.context.object; o.name=name; bpy.ops.object.shade_smooth(); move_to(o,collection); return o

clean_prefix()

# Perch first: visual reference/support, not part of Owli anatomy.
cylinder("BLK_PerchBar",(0,0,0.09*S),0.018*S,0.43*S,"X","PERCH")
cylinder("BLK_PerchStem",(0,0,0.045*S),0.014*S,0.08*S,"Z","PERCH")
cylinder("BLK_PerchBase",(0,0,0.008*S),0.075*S,0.016*S,"Z","PERCH")

# Main organic volumes.
ellipsoid("BLK_Body",(0,0,0.235*S),(0.235*S,0.19*S,0.265*S))
ellipsoid("BLK_Head",(0,0.012*S,0.365*S),(0.285*S,0.215*S,0.215*S))

# Eyes are true volume objects from the start.
eye_r=0.055*S
for side,x in (("L",-0.065*S),("R",0.065*S)):
    ellipsoid(f"BLK_Eye_{side}",(x,0.103*S,0.382*S),(eye_r*2,eye_r*0.92*2,eye_r*2),"EYES")

# Beak placeholder.
bpy.ops.mesh.primitive_cone_add(vertices=4,radius1=0.043*S,radius2=0.012*S,depth=0.075*S,
                                location=(0,0.135*S,0.345*S),rotation=(math.pi/2,0,math.pi/4))
beak=bpy.context.object
beak.name="BLK_Beak"
move_to(beak,"BEAK")

# Folded wing masses.
for side,x,rz in (("L",-0.112*S,-0.10),("R",0.112*S,0.10)):
    wing=ellipsoid(f"BLK_Wing_{side}",(x,-0.004*S,0.235*S),(0.105*S,0.105*S,0.245*S),"WINGS")
    wing.rotation_euler[1]=rz

# Tail volume.
ellipsoid("BLK_Tail",(0,-0.02*S,0.135*S),(0.12*S,0.11*S,0.17*S))

# Store provisional status.
for o in bpy.data.objects:
    if o.name.startswith("BLK_"):
        o["status"]="provisional_blockout"
        o["reference_basis"]="approved Owli design sheets; not metric orthographic data"

bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/"blender"/"scene"/"owli.blend"))
print("Owli blockout created. Review silhouettes before detail modeling.")
