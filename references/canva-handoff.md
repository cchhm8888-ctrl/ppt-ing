# Canva Handoff

## Route selection

Use Canva only when the user selects it or explicitly mentions `@canva`.

### Create a new Canva presentation

Use **REQUIRED SUB-SKILL:** `canva:canva-branded-presentation`.

1. Reuse the approved brief, source facts, slide map, and visual rules.
2. List available brand kits. Use the only kit automatically; ask the user to choose when several exist.
3. Generate Canva presentation candidates and show them before creating the editable design.
4. Create the selected candidate and return its Canva link.
5. Keep the original local PPTX unchanged.

### Edit an existing Canva presentation

Use **REQUIRED SUB-SKILL:** `canva:canva-edit-design`.

Follow its transaction protocol exactly:

1. Start an editing transaction and show returned thumbnails.
2. Batch supported operations.
3. Show the changed preview and summarize the edits.
4. Obtain explicit approval before committing.
5. Commit and return the Canva link, or cancel when rejected.

## Capability boundaries

Do not promise a direct round-trip between PPTX and Canva through the connector unless the available Canva tools explicitly support it.

The Canva edit route cannot reliably:

- Change font family
- Add new text elements
- Add, remove, or reorder slides
- Change backgrounds, animations, or transitions

When these changes are required, create a new Canva candidate from the approved brief or tell the user which manual Canva-editor action is needed.

## Handoff package

Pass only approved, source-grounded material:

- Presentation brief
- Slide-by-slide plan
- Brand/style rules
- Final copy
- Selected images and generated visuals
- Local PPTX link or path for reference

Treat Canva as a second layout environment, not as permission to rewrite facts or remove source traceability.
