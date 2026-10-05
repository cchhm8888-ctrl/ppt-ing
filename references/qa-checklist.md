# QA and Acceptance

## Structural

- 12+ slides contain cover, index, section divider, content, summary, and closing unless an approved exception exists.
- 15–24 slides use 2–4 dividers and at least 8 variants.
- No identical composition occurs three consecutive times.
- Card-like pages ≤35%; repeated title geometry ≤40%.

## Typography

- Six roles resolve through the font registry and measured frames.
- 15+ slides use at least 4 named presets and 3 purposeful treatments.
- Body, caption, page number, and chart labels have no heavy outline, shadow, glow, or decorative font.
- No overflow, orphan character, unsafe line break, or fallback-induced reflow.

## Composition and editability

- Every page has a visual anchor and purposeful reading path.
- Every commitment and expected object exists.
- Images are independent resources; text/data/labels/charts/semantic shapes are native.
- Masks preserve focal subjects and copy-safe areas.
- No empty card, line, ring, capsule, border, shadow, or glow exists only to fill space.

## Reference fidelity

- B pages contain the four-file bundle and approved revision.
- C pages contain full-page approval and FigEdit extraction evidence.
- PPTX render matches composite/reference in frame geometry, baselines, crop/focal, whitespace, masks, hierarchy, component count, and color.
- Reference PNG is never called the final PPT preview.

## Motion

- Real PowerPoint timeline inspected.
- Morph anchors exist in both adjacent slides with the same semantic role.
- Background media is sequence item 1 at t=0, muted, looping, bottommost.
- Editable reveals use `With Previous` and absolute delays.
- Manual advance and static fallback are valid.

## Final proof

Render all pages from the delivered PPTX revision. Inspect page PNGs and a contact sheet, perform at least one correction/re-render cycle, then run deterministic structure and motion audits. Static images alone cannot pass motion QA.
