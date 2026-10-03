"""Create/render standard Owli validation cameras."""
from pathlib import Path
import bpy, math, os
from mathutils import Vector

ROOT=Path.cwd()
OUT=ROOT/"validation"/"renders"
OUT.mkdir(parents=True,exist_ok=True)

def look_at(obj,target):
    direction=Vector(target)-obj.location
    obj.rotation_euler=direction.to_track_quat("-Z","Y").to_euler()

def camera(name,loc,target=(0,0,0.27),ortho=True,ortho_scale=0.58):
    data=bpy.data.cameras.get(name+"_Data") or bpy.data.cameras.new(name+"_Data")
    cam=bpy.data.objects.get(name) or bpy.data.objects.new(name,data)
    if cam.name not in bpy.data.collections["CAMERAS"].objects:
        if not cam.users_collection:
            bpy.data.collections["CAMERAS"].objects.link(cam)
    cam.location=loc
    look_at(cam,target)
    data.type="ORTHO" if ortho else "PERSP"
    if ortho:
        data.ortho_scale=ortho_scale
    else:
        data.lens=65
    return cam

cams=[
    camera("VAL_FRONT",(0,1.6,0.30)),
    camera("VAL_LEFT",(-1.6,0,0.30)),
    camera("VAL_BACK",(0,-1.6,0.30)),
    camera("VAL_3Q",(1.15,1.15,0.36),ortho=False),
]

scene=bpy.context.scene
scene.render.engine="BLENDER_EEVEE" if bpy.app.version >= (5, 0, 0) else "BLENDER_EEVEE_NEXT"
scene.render.resolution_x=int(os.environ.get("OWLI_RENDER_SIZE", "1024"))
scene.render.resolution_y=scene.render.resolution_x
scene.render.resolution_percentage=100

# Neutral world.
scene.world.color=(0.045,0.055,0.08)

for cam in cams:
    scene.camera=cam
    scene.render.filepath=str(OUT/f"{cam.name}.png")
    bpy.ops.render.render(write_still=True)
    print("rendered",cam.name)
