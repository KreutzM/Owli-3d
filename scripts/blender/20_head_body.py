"""Primary-form stage scaffold.

Run only after blockout silhouette approval. This stage should replace the blockout head/body with
clean editable topology while preserving the approved multi-view silhouette.
"""
import bpy

required=["BLK_Head","BLK_Body"]
missing=[n for n in required if n not in bpy.data.objects]
if missing:
    raise RuntimeError(f"Missing approved blockout objects: {missing}")

for name in required:
    bpy.data.objects[name]["next_stage"]="retopologize_or_rebuild_as_clean_PRIMARY_FORM_mesh"

print("Head/body stage prepared. Do not add fine feathers before silhouette approval.")
