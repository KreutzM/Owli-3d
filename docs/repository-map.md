# Repo-Karte für die Fortsetzung

Einstieg und aktueller Status: [Agent-Übergabe](agent-handoff.md).
Die Tabelle beschreibt die Zuständigkeit; Existenz einer Datei beweist nicht,
dass ihr Produktionsgoal abgeschlossen ist.

| Pfad | Funktion |
|---|---|
| `AGENTS.md`, `DESIGN_FREEZE.md`, `CHARACTER.md` | Auftrag, Referenzautorität, Anatomie, Iterationsvertrag |
| `design/reference_hierarchy.json`, `references/manifest.json` | Referenzränge, Dateien, Abmessungen und Hashes |
| `references/approved/` | neun tatsächlich vorhandene freigegebene PNGs |
| `design/character_spec.json`, `materials.json`, `rig_spec.json` | Zielmaß, Anatomie, Material-/Rig-Anforderungen |
| `design/proportions.json` | eingefrorene grobe Maße und Ringschemata |
| `design/silhouette_freeze.json` | manuelle grobe Vieransichtenentscheidung mit Quellenbindungen |
| `design/head_body.json`, `face.json`, `beak.json`, `feet.json` | implementierte Meilensteinparameter |
| `blender/scene/` | akzeptierte und technische LFS-Szenen; aktuelle Fortsetzung ist `owli_feet_v01.blend` |
| `validation/reference_views.json`, `checklist.json` | Studio und unveränderte Pflichtansichten / visuelle Checks |
| `validation/reviews/<milestone>/` | dauerhafte Szenen-/Quellen-/Rendernachweise und separate manuelle Entscheidung |
| `validation/history/pre_feet_v01/` | bytegenaue Original-Metadaten und geprüfte historische Quellenumbindung |
| `docs/decisions.md` | zeitlicher Verlauf von Geometrieentscheidungen, Konflikten und Grenzen |
| `scripts/project.py`, `validate_project.py` | CLI, Doctor, strikte Assetvalidierung und isolierter Gesamtsmoke |
| `scripts/setup_review.py`, `silhouette_review.py` | Studio-/Blockout-Runner, Bildmetriken, Vergleichstafeln und Freeze-Validierer |
| `scripts/head_body_review.py`, `face_review.py`, `beak_review.py`, `feet_review.py` | isolierte Build-/Fresh-Reload-Übergaben mit aktuellen Artefaktvalidierern |
| `scripts/history_bindings.py` | beweist, dass die bisherige Migration nur Pfade/abhängige Hashes änderte |
| `scripts/blender/blockout_geometry.py`, `primary_geometry.py` | gemeinsame Mesh-/Material-/Skalierungs-/BVH- und Quad-Cap-Helfer; bereits hashgebunden |
| `scripts/blender/00_scene_setup.py`, `10_blockout.py`, `20_head_body.py`, `21_eyes_mask.py`, `22_beak.py` | implementierte Stufen bis #4 |
| `scripts/blender/40_feet_perch.py`, `feet_geometry.py`, `verify_feet.py`, `feet_probe.py`, `feet_evidence.py` | #5 Produktion, echte Mesh-/Kontaktprüfungen und isolierte Evidenzerzeugung |
| `scripts/blender/30_wings_feathers.py` | Gerüst, nur Metadaten; muss für #6 durch reale Geometrie ergänzt werden |
| `scripts/blender/50_materials.py`, `60_rig.py` | Materialbibliothek bzw. Rig-Gerüst; keine fertige Zuordnung/Deformation |
| `scripts/blender/90_validation.py`, `validation_setup.py`, `verify_validation_setup.py` | feste Kameras/Lichter, Framing, Rendering und Studio-Prüfung |
| `scripts/blender/legacy/40_feet_perch.py` | ursprünglicher Guide-Code, unverändert für ältere Blockout-Rezepte |
| `scripts/legacy/project.py` | historische CLI-Quellensicherung; nicht als aktuellen Runner verwenden |
| `tests/`, `.github/workflows/validate.yml`, `requirements.txt`, `.gitattributes` | 25 aktuelle Tests, Windows/Ubuntu-CI, Python-Abhängigkeiten, LF-/LFS-Regeln |

## Nachweise lesen, ohne sie neu zu erzeugen

```powershell
python scripts/project.py validate
python -m unittest discover -s tests -v
python -c "import sys; sys.path.insert(0,'scripts'); from feet_review import validate_feet_delivery; print(validate_feet_delivery())"
```

Eine leere Fehlerliste bedeutet, dass die gespeicherten Liefernachweise zu den
aktuellen Dateien passen. Sie ersetzt weder die visuelle Prüfung eines neuen
Modells noch einen tatsächlichen Blender-Test nach einer Modelländerung.

## Neue Übergabe strukturieren

Für #6 sind `design/wings_feathers.json`, ein Geometry-/Verifier-/Evidence-Helfer,
`scripts/wings_feathers_review.py`, `blender/scene/owli_feathers_v01.blend` und
`validation/reviews/feathers_v01/` sinnvolle **vorgeschlagene** Namen. Diese Dateien
existieren am dokumentierten Ausgangsstand noch nicht. Im Bericht und Issue die
letztlich gewählten Namen festhalten. Bestehende akzeptierte Artefakte erhalten.
