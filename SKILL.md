---
name: ppt-ing
description: Create, redesign, extend, or audit editable static and dynamic PPT/PPTX decks from briefs, documents, data, templates, visual references, images, or video. Use for presentation story mapping, layout/theme selection, image and chart composition, native editable slide building, image2 preview-to-editable reconstruction, background-video decks, animation timing, embedded-media extraction, and delivery-package QA.
---

# PPT-ING — Presentation Engine V2

Build a presentation as a **story + layout system + editable source file**, not as a stack of screenshots. Default to the shortest safe route and only ask a question when the answer changes facts, the visual direction, or the delivery format.

## Route first

Classify the request before working:

| Route | Use when | Output |
|---|---|---|
| `rapid-static` | A topic/outline and a clear style/reference already exist | Editable PPTX, source map, QA |
| `studio-static` | The user explicitly requests image2 previews, options, or visual approval | 1–3 representative previews → editable PPTX → QA |
| `dynamic` | The user requests video, motion, autoplay, a dynamic template, or synchronization with an existing PPT | Editable PPTX, media map, motion plan, QA, deliverable media |

If the user provides a decisive reference or template, follow it and do **not** ask layout/color follow-ups. If direction is open, ask one compact question: editorial, structured information, or visual narrative. Read [layout-selection.md](references/layout-selection.md) only for that case.

## Required integrations

- Use `presentations:Presentations` for PPTX generation, rendering, and static verification.
- Use `powerpoint` for existing PPTX inspection/editing and Office-native fidelity checks.
- Use `imagegen` only when the user asks for image2/generation or a visual preview.
- Use `documents:documents`, `pdf:pdf`, or `spreadsheets:Spreadsheets` when the supplied source requires it.
- Use `scripts/inspect_pptx.py`, `scripts/extract_pptx_media.py`, and `scripts/audit_presentation.py` for deterministic media inspection, export, and pre-delivery checks.

## One-pass operating model

1. **Read**: inventory the supplied facts, references, templates, assets, and output requirement. Use the latest user-confirmed file as the source of truth.
2. **Map**: create a concise slide map: `page / job / message / layout / visual / source / motion`. Keep unsupported claims out.
3. **Build**: apply one selected theme and a small set of page types. Keep all text, lines, charts, labels, numbers, and page markers editable.
4. **Verify**: render and inspect; repair issues; verify again. For dynamic work, audit media relationships and timing before delivery.

Create a `presentation-brief.json` using [presentation-brief.schema.json](schemas/presentation-brief.schema.json) whenever the deck has 8+ slides, dynamic media, or a delivery package. This replaces scattered planning notes.

## Static deck rules

- Use the smallest number of page types that tells the story well; do not manufacture a 100-layout library per deck.
- Select page types from [page-types.md](references/page-types.md) based on the information job, not at random.
- Select theme, type scale, imagery, and charts using [engine-rules.md](references/engine-rules.md).
- Treat image2 output as a visual reference only: rebuild titles, body text, labels, lines, page numbers, and diagrams as editable PPT objects.
- Generate a full deck directly in `rapid-static`; only pause for preview approval in `studio-static` or when the user explicitly requests it.

## Dynamic deck rules

Read [dynamic-ppt.md](references/dynamic-ppt.md) before adding video or motion.

- Start from a working editable static deck. Add video as a replaceable media layer; never bake editable text into a video or background image.
- Produce a `media-map`: `slide / embedded media / exported filename / duration / crop / mute / loop / prompt or source`.
- Define a `motion-plan`: `object / trigger / effect / start / duration / end state`. Use one reading path; background/media first, then title, detail, diagrams, and footer.
- For autoplay, set the first editorial object to `With Previous` with the video, then chain the remaining editorial objects `After Previous`; finish their sequence inside the video’s effective duration.
- Use PowerPoint/WPS-native effects where available. If the runtime cannot create or preserve a native animation, deliver the editable static source plus the motion specification and state that limitation; never claim a non-existent animation.
- Prefer one restrained transition family per deck. Use Fade as the default; use stronger transitions only when they communicate a structural shift.
- If the user supplies a final PPTX, export media **from that PPTX**, not from earlier folders. Use `extract_pptx_media.py` and package the exported media with its mapping.

## Delivery modes

| Request | Deliver |
|---|---|
| Static PPT | editable PPTX + optional PDF/PNGs + brief + QA record |
| Dynamic PPT | editable PPTX + exported embedded media + media map + motion plan + prompts/source notes + QA record |
| Image2 split | editable single/multi-page PPTX + separated image/text/shape layers + reconstruction notes |
| Existing-deck audit | audit JSON/TXT + corrected PPTX only if requested |

Use [delivery-package.md](references/delivery-package.md) to structure packages. Keep prior versions unless the user explicitly requests replacement.

## Non-negotiables

- Never invent names, numbers, dates, achievements, source claims, or project facts.
- Never flatten editable textual or diagrammatic content into a background image.
- Never overwrite the user’s master deck without explicit permission.
- Never reuse a mismatched video folder when the final PPT embeds a different media file.
- Never deliver from the first render; complete one inspect → fix → re-verify loop.
- Do not make users approve redundant intermediate steps when they have already chosen the style and content direction.

## Read as needed

- [production-workflow.md](references/production-workflow.md) — route-specific execution.
- [page-types.md](references/page-types.md) — 18 reusable static/dynamic page types.
- [engine-rules.md](references/engine-rules.md) — story, theme, typography, image, chart, motion, transition rules.
- [dynamic-ppt.md](references/dynamic-ppt.md) — video synchronization, editable overlays, media extraction.
- [qa-checklist.md](references/qa-checklist.md) — visual, content, and technical QA.
- [delivery-package.md](references/delivery-package.md) — package contents and names.
