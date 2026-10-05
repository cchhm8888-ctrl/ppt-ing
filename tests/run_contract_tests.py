import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
brief = json.loads((root / "schemas" / "presentation-brief.schema.json").read_text(encoding="utf-8"))
spec = json.loads((root / "schemas" / "slide-spec.schema.json").read_text(encoding="utf-8"))
skill = (root / "SKILL.md").read_text(encoding="utf-8")

assert brief["$schema"].endswith("2020-12/schema")
assert spec["$schema"].endswith("2020-12/schema")
assert brief["properties"]["version"]["const"] == 5
assert spec["properties"]["version"]["const"] == 5
assert {"page_role", "layout_variant_id", "design_commitments", "expected_object_ids"} <= set(brief["$defs"]["briefSlide"]["required"])
assert {"typography_slots", "shape_composition", "reference_bundle", "reference_mapping"} <= set(spec["$defs"]["slide"]["required"])
assert {"visual_plate_png", "layout_blueprint_svg", "layout_map_json", "composite_preview_png"} <= set(spec["$defs"]["referenceBundle"]["required"])
for term in ("visual_plate.png", "layout_blueprint.svg", "layout_map.json", "composite_preview.png", "expected_object_ids", "Card-like pages ≤35%"):
    assert term in skill, term
print("PASS: PPT-ING v5 contracts")
