---
name: ppt-ing
description: Create, redesign, extend, reconstruct, or audit editable PPT/PPTX presentations with one-shot intake, Pinterest research, proposal approval, reference-locked visual realization, template/component packs, art-directed typography, native shape masks, PowerPoint motion, and rendered QA.
---

# PPT-ING Presentation Engine v5

Build the smallest auditable system that preserves the approved design. Do not replace an approved composition with a generic grid, repeated cards, or title-left/image-right fallback.

## Route requests first

| Route | Trigger | Required behavior |
| --- | --- | --- |
| `proposal-first` | New deck, redesign, expansion, or multi-slide visual change | One intake → research → proposal → approval → visual-target choice → production → QA. |
| `direct` | User explicitly says direct/no questions/no confirmation | Infer the full brief internally and default to `layout-reconstruction`; interrupt only for irreducible facts/files or a mandatory FigEdit extraction choice. |
| `lightweight` | Audit, export, typo fix, or bounded mechanical edit | Skip intake, Pinterest, image generation, and visual redesign. Validate only the affected scope. |

Urgency such as “赶时间” does not imply `direct`.

## Ask once

For `proposal-first`, show one eight-item block. Offer `全部推荐`; omitted design preferences use recommended defaults and are written as assumptions. Do not ask a second preference questionnaire.

1. Goal, scene, audience.
2. Source content, facts, existing files.
3. Slide count, ratio, language, target PowerPoint environment.
4. Copy type, tone, density.
5. Visual language: `商务克制 / 编辑式平衡（推荐） / 高表现艺术化 / 系统决定`; optional keywords such as image masks, geometric composition, magazine, spatial, material.
6. Color direction, brand colors, forbidden colors.
7. Layout direction, image/data proportion, density.
8. Motion: `A 静态 / B 克制讲述（推荐） / C 叙事连贯 Morph / D 沉浸背景视频 / E 自定义 / F 系统决定`.

At the end, add one optional attachment line, not question 9: up to one PPTX/POTX, five image/PDF/link references, and one brand pack. Unmarked templates are style references; reuse theme/masters only when explicitly requested.

Read [intake-and-approval.md](references/intake-and-approval.md).

## Research before proposal

After intake, inspect the optional reference pack, then search Pinterest for 3–5 transferable signals. Record URLs, titles, access dates, and signals only: composition, crop rhythm, typography, color relationship, shape language, material, and pacing. Do not download or imitate a Pin. Research refines the proposal; it does not silently change user constraints.

## Proposal approval gate

Output one complete versioned proposal containing:

1. Copy and narrative.
2. Visual language and selected template pack.
3. Color system with HEX and ratios.
4. Page-role map, layout families, variants, grid, density rhythm.
5. Component and native shape/mask system.
6. Motion profile and per-role recipes.
7. Imagery and asset strategy.
8. Six typography roles, named presets, and art effects.
9. Special effects and editability limits.

Include a complete slide table. Until the user confirms, do not create Image2 references, production assets, PPTX objects, or renders. Revisions update the proposal without repeating intake.

## Mandatory document grammar

For 12+ slides, the approved slide table must follow:

`cover → index → section-divider(s) → content → summary → closing`

- 12–14 slides: at least 2 section dividers.
- 15–24 slides: 2–4 section dividers and at least 8 distinct layout variants.
- Every slide records `page_role`, `section_id`, `narrative_job`, and `layout_variant_id`.
- A user-approved exception must be explicit in `deck_structure.approved_exceptions`.

Read [design-system.md](references/design-system.md) and [template-library.md](references/template-library.md).

## Choose the visual-target path after proposal approval

Offer exactly:

- `A 不生成逐页图` → `plan-native` + `page_reference_mode: none`.
- `B 无文字版式图（推荐）` → `layout-reconstruction` + `page_reference_mode: no-text-layout`.
- `C 带文字信息全页面图` → `figedit-decomposition` + `page_reference_mode: full-page-ai-copy`.

The selector is a stage gate, not another intake.

### Route B: reference bundle, not PNG guessing

For each approved slide, compile a four-file reference bundle before construction:

1. `visual_plate.png` — no readable text; imagery, material, light, color, depth.
2. `layout_blueprint.svg` — measured vector frames, masks, crop windows, shape geometry, safe zones, baselines, and IDs.
3. `layout_map.json` — canonical copy bindings, coordinates, z-order, typography slots, asset IDs, crop/focal data, and design commitments.
4. `composite_preview.png` — plate + approved copy + blueprint, used for user approval and render comparison.

Generate the SVG/JSON from measured layouts or authorized editable templates. Never auto-trace a raster preview and call it an editable design. Confirm the entire set before construction.

### Route C: full-page reference and FigEdit

Image-generated text is visual evidence only. Canonical copy and facts always come from the approved Brief/Slide Spec. Use FigEdit to extract the accepted page; rebuild every title, body, number, label, chart, and semantic connector natively. Ask `full-extract / selective / flatten` only when the background extraction gate requires it.

Read [reference-locked-reconstruction.md](references/reference-locked-reconstruction.md).

## Compile before build

Create schema-valid `presentation-brief.json` and `slide-spec.json` for 8+ slides. Every slide must include:

- role, section, narrative job, family, variant, visual anchor;
- `design_commitments` describing the approved composition features that may not be simplified;
- `expected_object_ids` for every promised text, image, chart, component, shape, mask, connector, and Morph anchor;
- six-role typography slots with exact frame, font key, size, weight, color, leading, tracking, maximum lines, alignment, effect, and safe zone;
- shape/mask recipes with geometry, fill, crop, focal point, transparency, border, shadow, z-order, and editability;
- structured motion groups and asset provenance;
- reference bundle and approval evidence for routes B/C.

Missing mandatory visual assets trigger `imagegen` for conceptual visuals. Never fabricate real people, products, events, cases, results, certificates, screenshots, or factual evidence.

## Build faithfully

- Use `presentations:Presentations` for A/B and `figedit` for C.
- Reuse authorized user-template components through parameterized recipes; raster screenshots remain style signals.
- Images stay independent assets. Text, data, diagrams, masks, labels, and semantic shapes stay native editable objects.
- Every `design_commitment` and `expected_object_id` must exist before render.
- Do not silently replace a complex approved composition with cards, generic columns, or a new visual metaphor.

## Design contract

- Default intensity: editorial-balanced D3–D4.
- 10+ slides: 5–7 layout families; 15+ slides: at least 8 variants.
- No family may repeat more than 3 consecutive pages; no identical composition more than 2 consecutive pages.
- Card-like pages ≤35%; repeated title geometry ≤40%.
- Six typography roles: `Display / Section / Title / Body / Caption / Numeral`.
- 15+ slides: at least 4 named typography presets and 3 purposeful treatments.
- Each page: at most one primary type effect and one support effect.
- Use full-bleed image, editorial crop, type/image overlap, split statement, product hero, exploded architecture, process ribbon, system map, spatial plan, module reconfiguration, scenario comparison, data proof, summary, and closing intentionally—not as random variety.
- Shapes must focus, carry copy, organize information, express relationships, or create rhythm. Empty lines, rings, capsules, frames, shadows, or glow fail critique.

## Motion contract

Use `M0 Static`, `M1 Calm Reveal`, `M2 Narrative Continuity`, or `M3 Video Synced` from [motion-system.md](references/motion-system.md).

- Title/art word: start 0.10s, duration 0.30–0.34s.
- Body: 0.48–0.52s, about 0.28s.
- First information group: 0.84–0.90s; add 0.36–0.42s per group; last by 2.20s.
- Editable effects use `With Previous` plus absolute delay.
- Morph only same-name, same-semantic native anchors across adjacent slides.
- Different backgrounds fade; foreground ribbon/node/module/mask/title anchors may Morph.
- Approved background video is bottommost, timeline item 1, t=0, muted, looping. Do not auto-generate video, export video, or create a delivery package unless separately requested.

## QA hard gates

Render the current PPTX in real PowerPoint and inspect every page plus contact sheet. Static PNGs do not prove motion.

Fail when:

- required page roles, families, variants, typography presets, or visual anchors are missing;
- a commitment or expected object is absent;
- text hierarchy is generic or the same title geometry dominates;
- the render diverges from the approved composite blueprint/reference;
- subjects are cropped, text crosses unsafe regions, or masks obscure meaning;
- full-page screenshots replace editable structure;
- meaningless decoration, repeated cards, excessive shadow/glow, or fake Morph appears;
- the PowerPoint timeline, media order, Morph anchors, manual advance, or static fallback is invalid.

Repair the Slide Spec/native objects, re-render, and pass [qa-checklist.md](references/qa-checklist.md). The final preview must come from the delivered PPTX revision.

## Canonical files

- [intake-and-approval.md](references/intake-and-approval.md)
- [template-library.md](references/template-library.md)
- [design-system.md](references/design-system.md)
- [reference-locked-reconstruction.md](references/reference-locked-reconstruction.md)
- [motion-system.md](references/motion-system.md)
- [qa-checklist.md](references/qa-checklist.md)
- [production-workflow.md](references/production-workflow.md)
- [presentation-brief.schema.json](schemas/presentation-brief.schema.json)
- [slide-spec.schema.json](schemas/slide-spec.schema.json)
