# Native Motion System

## Profiles

- `M0-static`: no entrance animation.
- `M1-calm-reveal`: semantic groups reveal in reading order.
- `M2-narrative-continuity`: M1 plus same-semantic native Morph anchors.
- `M3-video-synced`: M2 plus approved looping background video.

## Absolute timeline

| Group | Start | Duration |
| --- | ---: | ---: |
| title/art word | 0.10s | 0.30–0.34s |
| body | 0.48–0.52s | ~0.28s |
| information 1 | 0.84–0.90s | 0.24–0.30s |
| later groups | +0.36–0.42s | 0.24–0.30s |

Last semantic reveal should normally finish by 2.20s. Use `With Previous` and absolute delays, never `After Previous` chains tied to a video duration.

## Composition-aware motion

- Treat split titles, art words, outlines, gradients, and vertical labels as one title group; never reveal character by character.
- Image panels and modular components reveal as semantic units.
- A process connector may wipe once in reading direction, then nodes fade.
- Editorial crops and texture fields stay static.
- A slide has one principal action and at most one secondary reveal family; maximum five semantic groups.

## Morph

Morph only native objects with the same name and logical role across adjacent pages: title, numeral, navigation, product module, light ribbon, node, or mask. Changing meaning means Fade. Different images, video assets, and image-internal subjects do not Morph.

## Video

An approved background video is bottommost and has exactly one media play effect at sequence position 1, t=0, muted, looping. Editable text and shapes use the same absolute timeline. Static fallback frames remain readable.

Ban random fly-ins, bounce, spin, loader animations, HUD scans, full-screen background entrance, and animated decorative lines.
