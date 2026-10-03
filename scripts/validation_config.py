"""Validate the versioned studio recipe without requiring Blender."""
import math


def valid_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def vector(value, size=3):
    return isinstance(value, list) and len(value) == size and all(valid_number(v) for v in value)


def validate_studio(cfg, manifest=None, hierarchy=None):
    errors = []
    views = cfg.get("views", [])
    names = [view.get("name") for view in views]
    if len(names) != 4 or set(names) != {"VAL_FRONT", "VAL_LEFT", "VAL_BACK", "VAL_3Q"}:
        errors.append("studio needs exactly front, left profile, back and 3/4 cameras")
    if cfg.get("render", {}).get("resolution") != 1024:
        errors.append("canonical studio resolution must be 1024")
    margin = cfg.get("framing", {}).get("minimum_margin")
    if not valid_number(margin) or not 0 < margin < 0.5:
        errors.append("studio framing margin must be finite and between 0 and 0.5")
    records = {r["file"]: r for r in manifest.get("references", [])} if manifest else {}
    ranks = {}
    if hierarchy:
        for item in hierarchy.get("hierarchy", []):
            for file in ([item["file"]] if "file" in item else item.get("files", [])):
                ranks[file] = item["rank"]

    def reference(file, rank, crop, label):
        if records and file not in records:
            errors.append(f"{label}: reference absent from manifest: {file}")
        if ranks and ranks.get(file) != rank:
            errors.append(f"{label}: reference rank disagrees with authority hierarchy")
        if crop is not None:
            if not vector(crop, 4) or not all(isinstance(n, int) for n in crop) or not (0 <= crop[0] < crop[2] and 0 <= crop[1] < crop[3]):
                errors.append(f"{label}: invalid reference crop")
            elif file in records and (crop[2] > records[file]["width"] or crop[3] > records[file]["height"]):
                errors.append(f"{label}: reference crop exceeds source dimensions")

    for view in views:
        name = view.get("name")
        camera = view.get("camera", {})
        if not vector(camera.get("location")) or not vector(camera.get("target")) or camera.get("location") == camera.get("target"):
            errors.append(f"{name}: camera location/target must be distinct finite 3D vectors")
        expected = "PERSP" if name == "VAL_3Q" else "ORTHO"
        if camera.get("projection") != expected:
            errors.append(f"{name}: expected {expected} projection")
        for key in ("ortho_scale", "lens_mm", "clip_start_m", "clip_end_m"):
            if not valid_number(camera.get(key)) or camera[key] <= 0:
                errors.append(f"{name}: {key} must be finite and positive")
        if valid_number(camera.get("clip_start_m")) and valid_number(camera.get("clip_end_m")) and camera["clip_start_m"] >= camera["clip_end_m"]:
            errors.append(f"{name}: camera clipping range is reversed")
        reference(view.get("reference"), view.get("reference_rank"), view.get("reference_panel", {}).get("crop_px"), name)
        if "geometry_reference" in view:
            geom = view["geometry_reference"]
            reference(geom.get("file"), geom.get("rank"), geom.get("crop_px"), f"{name} geometry")
    lighting = cfg.get("lighting", {})
    lights = lighting.get("lights", [])
    light_names = [light.get("name") for light in lights]
    if len(lights) < 3 or len(set(light_names)) != len(light_names) or any(not n for n in light_names) or set(names) & set(light_names):
        errors.append("studio light names must be unique; at least three area lights are required")
    if not vector(lighting.get("target")) or not vector(lighting.get("color_linear")):
        errors.append("studio lighting target/color must be finite 3D vectors")
    for light in lights:
        if not vector(light.get("location")):
            errors.append(f"{light.get('name')}: invalid light position")
        for key in ("energy_w", "size_m"):
            if not valid_number(light.get(key)) or light[key] <= 0:
                errors.append(f"{light.get('name')}: {key} must be finite and positive")
    for ref in cfg.get("shared_references", []):
        reference(ref.get("file"), ref.get("rank"), None, "shared reference")
    return errors
