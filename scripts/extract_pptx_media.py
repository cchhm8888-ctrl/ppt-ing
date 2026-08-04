#!/usr/bin/env python3
"""Export embedded PPTX media with slide-prefixed filenames and a JSON manifest."""
from __future__ import annotations

import argparse
import json
import shutil
import zipfile
from collections import defaultdict
from pathlib import Path

from inspect_pptx import inspect


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    report = inspect(args.pptx)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pages_by_media: dict[str, list[int]] = defaultdict(list)
    for slide in report["slides"]:
        for item in slide["media"]:
            if slide["page"] not in pages_by_media[item["path"]]:
                pages_by_media[item["path"]].append(slide["page"])

    exported = []
    with zipfile.ZipFile(args.pptx) as zf:
        for item in report["media"]:
            path = item["path"]
            pages = pages_by_media.get(path, [])
            prefix = "_".join(f"P{page:02d}" for page in pages) or "UNUSED"
            destination = args.output_dir / f"{prefix}_{Path(path).name}"
            with zf.open(path) as source, destination.open("wb") as target:
                shutil.copyfileobj(source, target)
            exported.append({"source": path, "pages": pages, "export": destination.name, "bytes": item["bytes"]})

    manifest = {"pptx": str(args.pptx), "output_dir": str(args.output_dir), "exports": exported}
    text = json.dumps(manifest, ensure_ascii=False, indent=2)
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
