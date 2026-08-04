#!/usr/bin/env python3
"""Inspect slide-to-media relationships inside a PPTX without Office automation."""
from __future__ import annotations

import argparse
import json
import posixpath
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

REL_NS = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def rel_targets(zf: zipfile.ZipFile, rel_name: str) -> dict[str, dict[str, str]]:
    root = ET.fromstring(zf.read(rel_name))
    return {
        item.attrib["Id"]: {
            "target": item.attrib.get("Target", ""),
            "type": item.attrib.get("Type", ""),
            "mode": item.attrib.get("TargetMode", ""),
        }
        for item in root.findall(f"{REL_NS}Relationship")
    }


def inspect(pptx: Path) -> dict:
    with zipfile.ZipFile(pptx) as zf:
        names = set(zf.namelist())
        media = []
        for name in sorted(n for n in names if n.startswith("ppt/media/") and not n.endswith("/")):
            info = zf.getinfo(name)
            media.append({"path": name, "bytes": info.file_size, "extension": Path(name).suffix.lower()})

        slides = []
        for slide_name in sorted(
            (n for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
            key=lambda n: int(re.search(r"slide(\d+)", n).group(1)),
        ):
            page = int(re.search(r"slide(\d+)", slide_name).group(1))
            rel_name = f"ppt/slides/_rels/slide{page}.xml.rels"
            mapped = []
            if rel_name in names:
                for rel_id, rel in rel_targets(zf, rel_name).items():
                    target = rel["target"]
                    resolved = posixpath.normpath(posixpath.join("ppt/slides", target))
                    if "/media/" in resolved or rel["type"].endswith(("/video", "/audio", "/media")):
                        mapped.append({"relationship_id": rel_id, "path": resolved, **rel})
            slides.append({"page": page, "media": mapped})
        return {"pptx": str(pptx), "media": media, "slides": slides}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    report = inspect(args.pptx)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
