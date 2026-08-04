#!/usr/bin/env python3
"""Report basic PPTX page, transition, media, and external-link health."""
from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from inspect_pptx import inspect, rel_targets

P_NS = "{http://schemas.openxmlformats.org/presentationml/2006/main}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    media_report = inspect(args.pptx)
    with zipfile.ZipFile(args.pptx) as zf:
        names = set(zf.namelist())
        slides = []
        external = []
        for name in sorted((n for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)), key=lambda n: int(re.search(r"slide(\d+)", n).group(1))):
            page = int(re.search(r"slide(\d+)", name).group(1))
            root = ET.fromstring(zf.read(name))
            transition = root.find(f"{P_NS}transition")
            rel_name = f"ppt/slides/_rels/slide{page}.xml.rels"
            rels = rel_targets(zf, rel_name) if rel_name in names else {}
            for rel in rels.values():
                if rel["mode"] == "External":
                    external.append({"page": page, **rel})
            slides.append({
                "page": page,
                "transition": list(transition)[0].tag.split("}")[-1] if transition is not None and list(transition) else None,
                "has_timing": root.find(f"{P_NS}timing") is not None,
            })
        result = {
            "pptx": str(args.pptx),
            "slide_count": len(slides),
            "embedded_media_count": len(media_report["media"]),
            "video_count": sum(1 for m in media_report["media"] if m["extension"] in {".mp4", ".mov", ".wmv", ".avi"}),
            "external_relationships": external,
            "slides": slides,
            "status": "review_required" if external else "no_external_relationships_detected",
        }
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
