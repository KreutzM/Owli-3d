.PHONY: setup validate scene blockout validation-render

setup:
	python -m pip install -r requirements.txt

validate:
	python scripts/validate_project.py

scene:
	blender --background --python scripts/blender/00_scene_setup.py

blockout:
	blender blender/scene/owli.blend --background --python scripts/blender/10_blockout.py

validation-render:
	blender blender/scene/owli.blend --background --python scripts/blender/90_validation.py
