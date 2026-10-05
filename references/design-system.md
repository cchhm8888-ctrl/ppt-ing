# Page, Layout, Typography, Shape System

## Page roles

`cover`, `index`, `section-divider`, `content`, `summary`, `closing` are mandatory for 12+ slides unless explicitly waived. `content` may specialize as `product-hero`, `architecture`, `process`, `system`, `scenario`, `comparison`, `data-proof`, `roadmap`, `case`, or `quote`.

## Layout families

Select 5–7 families and compile unique variants:

1. full-bleed cinematic image with safe-zone veil;
2. asymmetric editorial split;
3. image crop ribbon or collage;
4. type/image overlap and oversized statement;
5. product hero or exploded architecture;
6. process ribbon, timeline, or day/night transition;
7. system map, spatial plan, or module reconfiguration;
8. component annotation or scenario comparison;
9. data proof, chart backplane, or metric ladder;
10. index, chapter poster, summary manifesto, closing.

For 15+ slides, use at least 8 `layout_variant_id` values. Variants differ in composition geometry, not just color or asset replacement.

## Typography slots

Every slot records:

`role / element_ids / font_key / size_pt / weight / color_token / line_height / tracking_pt / max_lines / alignment / effect / frame / text_safe_zone_id`

Roles: `Display`, `Section`, `Title`, `Body`, `Caption`, `Numeral`.

Recommended preset families:

- `TYPE-HERO`: 60–96pt display, split or overlap, 1–3 lines.
- `TYPE-SECTION`: 72–110pt section numeral/word with small narrative kicker.
- `TYPE-EDITORIAL`: 34–52pt title, controlled asymmetry, color-highlighted keyword.
- `TYPE-PRODUCT`: 36–48pt title plus 56–84pt numeral/Latin anchor.
- `TYPE-DATA`: 28–40pt conclusion with 48–84pt numerals and compact captions.
- `TYPE-MANIFESTO`: one emotional serif keyword plus sans-serif statement.

Allowed native effects: keyword color, low-opacity backword, gentle gradient text, 0.5–0.75pt outline, soft offset shadow, restrained glow, emphasis plate, vertical/rotated label, image overlap. At most one primary and one support effect per slide. Never use heavy outline, 3D/emboss, whole-deck glow, or art fonts for body/data labels.

## Shape and mask recipes

- image-filled rounded rectangle, circle, arch, chamfer, polygon, or brand contour;
- repeated crop windows using one source image;
- transparent or gradient veil for copy safety;
- editable cutout window, slice, ribbon, or spatial partition;
- type/shape overlap with native text;
- semantic line, light ribbon, anchor, node, or wave only when it expresses direction or connection;
- glass panel with restrained border/highlight/shadow only when it groups information.

Each shape records `shape_id, role, geometry, fill_type, fill_color_or_asset, transparency, gradient, crop, focal_point, mask_or_overlay, border, shadow, z_order, text_safe_zone, editable_status`.

## Design commitments

A commitment is an approved visual fact such as “title crosses the image edge,” “three vertical product windows,” “numeral 02 occupies the left third,” or “signal ribbon connects four modules.” It must reference expected object IDs and an acceptance check. Simplifying it requires user approval.
