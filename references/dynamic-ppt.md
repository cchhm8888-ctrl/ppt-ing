# Dynamic PPT

## Media first, overlays second

1. Embed the approved MP4 in the target slide; never depend on a local external path.
2. Set mute, crop, and loop explicitly. Record the source or prompt.
3. Put editable title, labels, paths, nodes, and page markers on separate objects above the media.
4. Start the video and first editorial effect with `With Previous`.
5. Chain later editorial effects `After Previous`; finish all required motion inside the video’s effective duration.
6. End on a stable state. Do not leave text still moving after the video ends.

## Motion plan fields

`slide, object_name, layer, trigger, effect, start_s, duration_s, end_s, rationale`.

Use semantic object names such as `P12_VIDEO`, `P12_TITLE`, `P12_PATH_01`, `P12_NODE_01`. This makes media replacement and animation-window edits maintainable.

## Existing final PPTX as source

When the user says “use the videos in this final PPT,” treat its `ppt/media/` files and slide relationship files as authoritative. Run:

```text
python scripts/inspect_pptx.py final.pptx --json media-map.json
python scripts/extract_pptx_media.py final.pptx exported-media --json media-map.json
python scripts/audit_presentation.py final.pptx --json audit.json
```

Name exports by slide, not only `media1.mp4`. If two slides use the same media, record both mappings rather than duplicating silently.

## Compatibility guardrail

PowerPoint native animation XML and WPS support differ. Verify in the target playback application. If an automation library cannot preserve native motion, create the static editable deck plus `motion-plan.json`; do not pretend it is a finished dynamic deck.
