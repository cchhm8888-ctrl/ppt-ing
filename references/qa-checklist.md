# QA Checklist

## Content and editability

- Slide order, page numbers, section labels, facts, dates, and source claims agree.
- No placeholders, hidden planning notes, duplicated copy, accidental date, or image-baked editable text remains.
- Titles, body, labels, lines, charts, page markers, and diagrams are editable native objects.

## Visual

- Render every slide and inspect full size.
- Check text overflow, cropping, low contrast, margins, alignment, rhythm, font fallbacks, and repeated-layout fatigue.
- Check image generation artifacts: accidental words, watermarks, broken perspective, distorted people, and duplicated details.

## Dynamic

- Confirm slide count, embedded media count, media-to-slide mapping, duration, crop, mute, loop, and external-link absence.
- Confirm the video and first editable layer start together; remaining effects follow a readable sequence; editable overlays finish within the effective media window.
- Confirm transitions and autoplay behavior in the target application.

## Closeout

1. Render → inspect → list issues.
2. Fix the issues.
3. Re-render affected slides.
4. Run `audit_presentation.py` and review its output.
5. Deliver the PPTX plus only the requested supporting files.
