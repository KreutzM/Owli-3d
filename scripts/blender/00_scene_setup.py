from pathlib import Path
import sys
import bpy

ROOT=Path.cwd()
SCENE=ROOT/"blender"/"scene"/"owli.blend"

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
for datablocks in (bpy.data.cameras, bpy.data.lights):
    for data in list(datablocks):
        if data.users == 0:
            datablocks.remove(data)

scene=bpy.context.scene
scene.unit_settings.system="METRIC"
scene.unit_settings.length_unit="METERS"
scene.unit_settings.scale_length=1.0
scene.render.engine="BLENDER_EEVEE" if bpy.app.version >= (5, 0, 0) else "BLENDER_EEVEE_NEXT"
scene.render.resolution_x=1024
scene.render.resolution_y=1024
scene.render.resolution_percentage=100

collections=[
    "BLOCKOUT","PRIMARY_FORM","EYES","BEAK","WINGS","FEATHERS",
    "FEET","CLAWS","PERCH","TECH","RIG","CAMERAS","LIGHTS","REFERENCE"
]
for name in collections:
    if name not in bpy.data.collections:
        col=bpy.data.collections.new(name)
        scene.collection.children.link(col)

scene["project"]="Owli 3D avatar"
scene["version_target"]="V1 perched"
scene["axis_convention"]="X left/right, Y front/back, Z up; +Y is Owli front"
scene["foot_rule"]="4 toes per foot: 3 forward + 1 rear"
scene["flight_required"]=False

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validation_setup import setup
setup(ROOT)

SCENE.parent.mkdir(parents=True,exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(SCENE))
print("Saved",SCENE)
