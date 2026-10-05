# Reference-Locked Reconstruction

## Principle

An approved page image is not a license to redesign. Reconstruction must preserve composition, hierarchy, crop, whitespace, typography geometry, masks, and component relationships while rebuilding semantic content as editable objects.

## Route B reference bundle

Each page requires:

- `visual_plate.png`: no readable text; imagery, material, lighting, color, and depth.
- `layout_blueprint.svg`: measured vector boxes, baselines, shape paths, masks, crop windows, safe zones, and stable IDs.
- `layout_map.json`: canonical copy bindings, asset IDs, coordinates, z-order, crop/focal data, typography slots, design commitments, and expected object IDs.
- `composite_preview.png`: approved copy composited with the plate and blueprint.

The SVG/JSON are compiled from measurements or an authorized editable template. Do not trace a raster design blindly. PNG remains useful as appearance evidence; SVG/JSON provide geometry and object identity.

## Route C boundary

The full-page Image2 reference may contain approximate glyphs only for visual composition. Canonical text, data, charts, labels, and facts come from the approved Brief/Slide Spec. FigEdit extraction must not turn OCR into the content source.

## Reference mapping

Every slide stores:

`reference_asset_id, reference_revision, plan_version, canvas, visual_zones, object_mappings, fidelity_strategy, comparison_contract, editable_scope, approval_evidence`

Each object mapping binds one blueprint/reference ID to one PPT object ID and records target frame, source asset, crop/focal point, z-order, typography slot, and editability.

## Fidelity comparison

After construction, render the working PPTX and compare it to `composite_preview.png` using an overlay and contact sheet. Check:

- major frame displacement;
- title/body baseline and line breaks;
- focal subject and crop;
- negative-space ratio;
- mask geometry and safe zones;
- component count, grouping, and z-order;
- color/contrast and typography treatment.

If a mismatch exists, modify the Slide Spec or native objects and re-render. Never repair the preview PNG.
