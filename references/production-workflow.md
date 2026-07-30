# Production Workflow

## 1. Establish the brief

Confirm or infer from the request:

- Audience and presentation setting
- Communication goal and desired action
- Language, aspect ratio, slide count, and deadline
- Required output: PPTX, PDF, preview PNGs, Canva design, or combinations
- Whether the user requires approval before full production

Record assumptions in a temporary `.txt` file. Ask one concise question only when a missing answer would change the story, factual accuracy, or visual route.

## 2. Build a source manifest

List every source file and classify it as:

- Factual content
- Visual reference
- Reusable image or media
- Brand asset
- Existing deck/template
- Feedback or correction

Extract content with the matching document skill. Keep a source note for each non-trivial claim and each externally sourced asset. When sources conflict, prefer explicit revision files and the latest dated source, then flag the decision.

Do not invent unsupported content. Use neutral placeholders only in an internal draft, never in the delivered deck.

## 3. Reverse-engineer references

Inspect every page of a reference PDF or slide of a reference PPTX. Capture:

- Story arc and section order
- Recurring page types
- Title hierarchy and typography pairing
- Grid, margins, alignment, spacing, and page markers
- Image ratios, crop behavior, collage logic, and visual density
- Section-divider rhythm and ending treatment

Translate these observations into reusable layout rules. Do not copy the reference's original wording or unsupported claims.

## 4. Create the content architecture

Draft a slide map containing:

- Slide number
- Section
- Audience-facing title
- Communication job
- Verified content points
- Proposed visual
- Layout type
- Source references

Use a progressive story such as context, proposition, evidence, application, outcomes, and close. Match slide count to content depth instead of compressing all facts into a fixed template.

## 5. Preview gate

When the user requests visual confirmation, select 4-6 representative page types, usually:

- Cover
- Content introduction
- Overview or framework
- Detail or direction page
- Team or profile page
- Results or closing page

Use image2/image generation to explore composition. Prompt for the target aspect ratio and reserve readable zones for later editable text. Use real source images when available.

Show previews as previews, state which layout rules they establish, and wait for explicit approval before producing the complete deck. Iterate only the rejected page types.

## 6. Generate the editable PPTX

Follow `presentations:Presentations` and its selected visual route. Use the local `@oai/artifact-tool` workflow required by that skill.

Build a semantic style system for:

- Deck title
- Slide title
- Section title
- Body text
- Caption and metadata
- Decorative typography

Keep factual text, page numbers, labels, tables, and charts editable. Use generated raster artwork only as visual media. Preserve source decks and export revisions to new filenames.

## 7. Optional Canva branch

After a coherent draft or approved slide plan exists, ask whether the user wants:

- Local PPTX only
- Canva refinement only
- Both local PPTX and Canva refinement

If Canva is selected, follow [Canva Handoff](canva-handoff.md). The local PPTX remains the controlled master unless the user explicitly designates Canva as the new master.

## 8. Verification and delivery

Render all slides from the final PPTX. Inspect each at full size and use a montage only for overall pacing. Run overflow, placeholder, font, content-order, and source checks. Fix problems and re-render affected slides.

Use [QA Checklist](qa-checklist.md). Deliver only final artifacts requested by the user. Preserve earlier versions when the user has asked for alternatives or staged approval.
