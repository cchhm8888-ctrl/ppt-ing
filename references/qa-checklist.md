# QA Checklist

## Content

- Slide order matches the approved outline.
- Section numbers, page numbers, contents page, and internal references agree.
- Names, titles, dates, metrics, course names, awards, and contact details match sources.
- No placeholders, duplicated paragraphs, unsupported claims, or internal planning notes remain.
- Every researched claim and external asset has source provenance where required.

## Typography and layout

- Required fonts are explicitly assigned and available, or documented fallbacks are used.
- Titles do not wrap unexpectedly.
- Body text meets the minimum size required by `presentations:Presentations`.
- Paragraphs, captions, and labels have consistent line spacing and hierarchy.
- No text, image, shape, footer, or page marker exceeds the slide canvas.
- No unintended overlaps, clipped crops, stretched portraits, or low-contrast text remain.
- Adjacent slides vary in composition while preserving the design system.

## Images and data

- Images are clear at final display size and cropped naturally.
- The same image is not reused unless intentionally used as a background or motif.
- Charts and tables match the underlying data and remain editable when practical.
- Generated visuals do not contain accidental text, watermarks, or misleading details.

## Verification loop

1. Render every slide from the final PPTX.
2. Inspect every slide individually at full size.
3. Record and fix all issues found.
4. Re-render every affected slide.
5. Run overflow and content extraction checks.
6. Confirm no new issue appears after the fix.

Do not mark the deck complete before at least one fix-and-reverify cycle.
