---
name: ppt-ing
description: Use when a user asks to generate a presentation, PPT, PPTX, or slide deck from an outline, source files, reference PDF/PPTX, documents, or mixed assets, including requests for style matching, visual previews, editable text, layout selection by answering options, or Canva follow-up.
---

# PPT-ING

## Overview

Turn user-provided facts and assets into a coherent, editable presentation. Treat content structure, visual direction, user approval, and rendered-slide QA as separate gates.

## Required Skills

- **REQUIRED:** Use `presentations:Presentations` for local PPTX planning, generation, rendering, and verification.
- Use `pdf:pdf` for PDF references and `documents:documents` for DOCX sources.
- Use `imagegen` when the user requests image2/image generation, visual previews, or generated artwork.
- Use `powerpoint` when inspecting or modifying an existing PPTX with its utilities.
- **OPTIONAL CANVA ROUTE:** Use `canva:canva-branded-presentation` for a new Canva deck and `canva:canva-edit-design` for edits to an existing Canva design.

## Workflow

1. Inventory all supplied files before drafting. Extract facts, images, tables, names, dates, metrics, and source provenance.
2. Inspect every page or slide of any visual reference. Separate its narrative logic, layout grammar, typography, color, imagery, and recurring page types from its original wording.
3. Define audience, purpose, aspect ratio, language, slide count, and deliverables. Ask only for missing decisions that materially change the result.
4. Build a slide-by-slide content map from verified source material. Mark unsupported claims instead of inventing them.
5. Establish a design brief under `presentations:Presentations`. When visual direction is open, offer the user a compact option-based layout selection before making previews; use [Layout Selection](references/layout-selection.md). Do not ask again when the user has already specified a reference, template, or layout direction.
6. If preview approval is requested or the design direction remains uncertain, generate representative image2 previews and pause for explicit approval. Translate the selected option(s) into a written layout, type, color, and image-hierarchy specification; do not treat preview artwork as a flattened slide.
7. Create the editable PPTX only after the content map and visual direction are accepted. Keep titles, body text, page numbers, charts, and factual labels editable.
8. Offer the Canva branch after a coherent draft exists. Preserve the local PPTX and follow [Canva Handoff](references/canva-handoff.md).
9. Render every final slide, inspect at full size, run overflow and content checks, fix issues, and re-render affected slides.
10. Deliver the final PPTX plus the Canva link only when that branch was selected. Keep scratch files and preview assets out of the final deliverables.

Read [Production Workflow](references/production-workflow.md) before executing a new deck. Use [QA Checklist](references/qa-checklist.md) before claiming completion.

## Non-Negotiable Gates

- Never fabricate names, course titles, awards, statistics, dates, or outcomes.
- Never use generated preview images as flattened replacements for editable slide text.
- Never bypass preview confirmation when the user explicitly requests approval before production.
- Never overwrite an existing deck unless the user explicitly asks.
- Never deliver from the first render; complete at least one inspect, fix, and re-verify cycle.

## Option-Based Layout Selection

- Ask one to three short, mutually exclusive option questions only when the user has not supplied a decisive visual reference or explicitly asks to choose a layout.
- Ask the most consequential choice first: select one layout route. Then ask only necessary follow-ups for information density and imagery.
- Present two to four concrete options, label one as recommended, and describe the visible result rather than abstract design jargon.
- Carry the user's selections into a design brief covering page types, grid, type hierarchy, color system, image hierarchy, and charts/tables. Apply it consistently, but vary page composition within the selected route.
- When a supplied reference conflicts with an option choice, let the explicit reference control typography, color, and page rhythm; use the choice to resolve only the undecided parts.

## Quick Reference

| Input or request | Required response |
|---|---|
| Outline or mixed documents | Extract, normalize, and map each claim to a source |
| Reference PDF/PPTX | Inspect all pages and reproduce its logic, not its wording |
| “让我选排版” or no visual direction | Offer compact layout options, record the answers, then build the design brief |
| “先看预览” or image2 | Generate representative page types and wait for approval |
| Editable PPT | Build native text and data objects in PPTX |
| Canva refinement | Use the optional Canva route without replacing the local master |
| Final delivery | Render, inspect, fix, verify, then return only final artifacts |

## Common Mistakes

- Starting slide production before the narrative and page types are stable.
- Matching colors while missing the reference deck's pacing and image hierarchy.
- Shrinking text instead of editing content or changing the layout.
- Treating Canva as a guaranteed PPTX import/edit API.
- Claiming success from a contact sheet without inspecting full-size slides.