"""Create a minimal avatar rig scaffold. No flight rig."""
from pathlib import Path
import bpy, json

ROOT=Path.cwd()
cfg=json.loads((ROOT/"design"/"rig_spec.json").read_text())

old=bpy.data.objects.get("Owli_Rig")
if old:
    bpy.data.objects.remove(old,do_unlink=True)

arm=bpy.data.armatures.new("Owli_RigData")
rig=bpy.data.objects.new("Owli_Rig",arm)
bpy.data.collections["RIG"].objects.link(rig)
bpy.context.view_layer.objects.active=rig
rig.select_set(True)
bpy.ops.object.mode_set(mode="EDIT")

def bone(name,head,tail,parent=None):
    b=arm.edit_bones.new(name)
    b.head=head; b.tail=tail
    if parent:
        b.parent=arm.edit_bones.get(parent)
    return b

bone("root",(0,0,0),(0,0,0.05))
bone("body",(0,0,0.12),(0,0,0.30),"root")
bone("neck",(0,0,0.30),(0,0,0.35),"body")
bone("head",(0,0,0.35),(0,0,0.44),"neck")
bone("wing_L",(-0.07,0,0.29),(-0.14,0,0.20),"body")
bone("wing_R",(0.07,0,0.29),(0.14,0,0.20),"body")
bone("leg_L",(-0.05,0,0.15),(-0.05,0,0.10),"body")
bone("leg_R",(0.05,0,0.15),(0.05,0,0.10),"body")
bone("beak",(0,0.09,0.36),(0,0.14,0.35),"head")

bpy.ops.object.mode_set(mode="OBJECT")
rig["target"]="avatar_v1_perched"
rig["flight_rig"]=False
rig["required_controls"]=",".join(cfg["required_controls"])
rig["foot_rule"]="4 toes per foot: 3 forward + 1 rear"
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/"blender"/"scene"/"owli.blend"))
print("Created minimal perched-avatar rig scaffold. Weighting and facial controls remain to be implemented.")
