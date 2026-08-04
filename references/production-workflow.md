# Production Workflow

## 0. Select the minimum route

- Use `rapid-static` when content and visual direction are already clear. Do not create previews first.
- Use `studio-static` only for explicit preview/image2 approval or genuinely undecided visual direction.
- Use `dynamic` whenever the request includes video, animation, automatic playback, media replacement, or a dynamic reference PPT.

Ask at most one decision question when no reference determines the answer. Infer aspect ratio, language, page count, and delivery from supplied files when reasonable; list assumptions in the brief.

## 1. Read and map

Create `presentation-brief.json` and a slide map. Each slide needs one communication job, one dominant visual hierarchy, and a verified source. For existing decks, preserve page count, visual rules, and named objects unless the requested change says otherwise.

## 2. Build static first

Build native editable objects: text, labels, data, diagrams, paths, numbers, footers, and page markers. Use raster assets only for the visual/media layer. Select 3–6 compatible page types; do not force every slide into the same composition.

## 3. Add motion only when requested

Create `media-map.json` and `motion-plan.json`. Embed media, set crop/mute/loop behavior, and synchronize editable overlays to the effective video window. When a dynamic deck is based on a final PPTX, extract the PPTX’s embedded media and make that export the delivery source.

## 4. Verify and package

Render every slide. Inspect full-size pages, fix defects, and rerender the affected slides. Run `audit_presentation.py`. Package only the requested artifact set plus the minimum evidence required to reproduce or audit media and AI-generated assets.
