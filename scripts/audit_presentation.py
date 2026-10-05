#!/usr/bin/env python3
"""Audit basic editable-PPTX structure without Office automation."""
from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"p": P_NS, "a": A_NS}


def slide_number(name: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", name)
    if not match:
        raise ValueError(f"Not a slide path: {name}")
    return int(match.group(1))


def inspect_relationships(zf: zipfile.ZipFile, rel_name: str, page: int) -> list[dict[str, str | int]]:
    if rel_name not in zf.namelist():
        return []
    root = ET.fromstring(zf.read(rel_name))
    external = []
    for item in root.findall(f"{{{REL_NS}}}Relationship"):
        if item.attrib.get("TargetMode") == "External":
            external.append(
                {
                    "page": page,
                    "relationship_id": item.attrib.get("Id", ""),
                    "type": item.attrib.get("Type", ""),
                    "target": item.attrib.get("Target", ""),
                }
            )
    return external


def audit(pptx: Path) -> dict:
    if not pptx.is_file():
        raise FileNotFoundError(pptx)
    with zipfile.ZipFile(pptx) as zf:
        names = set(zf.namelist())
        slide_names = sorted(
            (name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=slide_number,
        )
        slides = []
        external_relationships = []
        for name in slide_names:
            page = slide_number(name)
            root = ET.fromstring(zf.read(name))
            text_runs = [node.text or "" for node in root.findall(".//a:t", NS)]
            shape_count = len(root.findall(".//p:sp", NS))
            picture_count = len(root.findall(".//p:pic", NS))
            graphic_count = len(root.findall(".//p:graphicFrame", NS))
            transition = root.find("p:transition", NS)
            timing = root.find("p:timing", NS)
            rel_name = f"ppt/slides/_rels/slide{page}.xml.rels"
            external_relationships.extend(inspect_relationships(zf, rel_name, page))
            slides.append(
                {
                    "page": page,
                    "shape_count": shape_count,
                    "picture_count": picture_count,
                    "graphic_count": graphic_count,
                    "text_run_count": len(text_runs),
                    "text_character_count": sum(len(text) for text in text_runs),
                    "has_transition": transition is not None,
                    "has_timing": timing is not None,
                    "possibly_empty": shape_count + picture_count + graphic_count == 0,
                }
            )

        empty_pages = [slide["page"] for slide in slides if slide["possibly_empty"]]
        issues = []
        if external_relationships:
            issues.append("external_relationships")
        if empty_pages:
            issues.append("possibly_empty_slides")
        return {
            "pptx": str(pptx),
            "slide_count": len(slides),
            "external_relationships": external_relationships,
            "possibly_empty_pages": empty_pages,
            "slides": slides,
            "status": "review_required" if issues else "structure_ok",
            "issues": issues,
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = audit(args.pptx)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()