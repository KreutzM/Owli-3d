.PHONY: setup validate doctor smoke scene blockout validation-render

setup:
	python -m pip install -r requirements.txt

validate:
	python scripts/project.py validate

doctor:
	python scripts/project.py doctor

smoke:
	python scripts/project.py smoke

scene:
	python scripts/project.py scene

blockout:
	python scripts/project.py blockout

validation-render:
	python scripts/project.py render
