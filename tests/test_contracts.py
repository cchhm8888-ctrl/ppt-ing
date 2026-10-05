import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))


def test_schemas_are_valid_json_schema():
    for name in ("presentation-brief.schema.json", "slide-spec.schema.json"):
        Draft202012Validator.check_schema(load(name))


def test_brief_v5_has_page_grammar_and_commitments():
    schema = load("presentation-brief.schema.json")
    assert schema["properties"]["version"]["const"] == 5
    assert "deck_structure" in schema["required"]
    required = set(schema["$defs"]["briefSlide"]["required"])
    assert {"page_role", "section_id", "layout_variant_id", "design_commitments", "expected_object_ids"} <= required


def test_slide_v5_has_executable_typography_shapes_and_reference_bundle():
    schema = load("slide-spec.schema.json")
    required = set(schema["$defs"]["slide"]["required"])
    assert {"typography_slots", "shape_composition", "reference_bundle", "reference_mapping"} <= required
    slot_required = set(schema["$defs"]["typographySlot"]["required"])
    assert {"role", "font_key", "size_pt", "line_height", "tracking_pt", "frame", "text_safe_zone_id"} <= slot_required
    bundle_required = set(schema["$defs"]["referenceBundle"]["required"])
    assert {"visual_plate_png", "layout_blueprint_svg", "layout_map_json", "composite_preview_png"} <= bundle_required


def test_skill_uses_reference_bundle_not_png_guessing():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for term in ("visual_plate.png", "layout_blueprint.svg", "layout_map.json", "composite_preview.png"):
        assert term in text
    assert "expected_object_ids" in text
    assert "Card-like pages ≤35%" in text
