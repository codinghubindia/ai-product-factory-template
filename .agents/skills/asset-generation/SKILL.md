---
name: asset-generation
description: Systematic planning, generation, inspection, metadata cataloging, and artifact integration of visual assets adhering to visual continuity and commercial publishing standards.
---

# Asset Generation & Visual Production Skill

This skill governs the production of intentional, high-craft visual assets using available generative tools, vector engines, and screenshot utilities.

**The Golden Rule:** Never generate an image simply to fill empty whitespace. Every visual asset must clarify a concept, anchor information hierarchy, or make a core mechanism tangible.

---

## 1. The 13-Step Asset Generation Funnel

Before generating or integrating any visual asset into a product deliverable, execute this strict 13-step sequence:

```text
1. PURPOSE DETERMINATION
  → 2. PLACEMENT SPECIFICATION
  → 3. ASPECT RATIO & GEOMETRY
  → 4. RESOLUTION & DPI TARGETING
  → 5. SEMANTIC VISUAL ROLE
  → 6. CREATIVE DIRECTION CONFORMANCE
  → 7. CONTINUITY SPEC VERIFICATION
  → 8. GENERATION EXECUTION
  → 9. ISOLATION INSPECTION
  → 10. TARGETED REVISION (IF DEFECTIVE)
  → 11. METADATA CATALOGING IN ASSET MANIFEST
  → 12. ARTIFACT INTEGRATION
  → 13. IN-CONTEXT VISUAL RE-RENDER & QA
```

### Detailed Operational Steps

1. **Why is the image needed?** (e.g. "To illustrate the 3-tier communication bottleneck architecture in Chapter 1").
2. **Where will it appear?** Exact file path and container selector (e.g. `final/book-system.html#fig-bottleneck-matrix`).
3. **Aspect Ratio:** Match layout grid (`16:9` for widescreen headers, `1:1` for badges, `4:3` for editorial figures, `9:16` for mobile mockups).
4. **Resolution & DPI:** Minimum $300\text{ DPI}$ for print documents (e.g. $2400 \times 1800\text{px}$ for an $8 \times 6\text{ inch}$ print area); $1080p+$ for web displays.
5. **Visual Role:** Categorized into supported taxonomies (see Section 2).
6. **Creative Direction:** Verify alignment with `products/<product_id>/creative-concept.md`.
7. **Continuity Requirements:** Verify strict alignment with palette, lighting, texture, and framing rules in `design/<product_id>/visual-continuity.md`.
8. **Generation:** Execute using available tooling (e.g. `generate_image` or local Python Pillow/SVG scripting).
9. **Inspection:** Audit for common generative defects: garbled text glyphs, distorted hands/faces, melted edges, muddy colors, or unsharp borders.
10. **Revision:** Prompt adjustment or localized cleanup if defects are detected.
11. **Store Metadata:** Write full 17-point asset record to `products/<product_id>/assets/asset-manifest.json`.
12. **Integration:** Embed asset into source HTML/PDF/Software using clean relative paths and semantic `<figure>` tags with descriptive captions and alt-text.
13. **Final Render:** Re-compile the document/app and inspect in layout.

---

## 2. Supported Asset Categories

The factory formally recognizes and supports 20 visual asset categories:

1. **Outer Covers:** High-impact book, guide, and report covers.
2. **Chapter & Section Artwork:** Visual chapter opener banners and module divider spreads.
3. **Editorial Diagrams:** Conceptual flowcharts, process maps, and systems topologies (prefer clean SVG vector code).
4. **Infographics & Charts:** Data visualizations with explicit axes, units, and high-contrast callouts.
5. **UI Illustrations:** Stylized user interface flows and dashboard component mockups.
6. **Device Mockups:** Photorealistic, cleanly framed desktop, tablet, or phone frames showcasing the product.
7. **Software Screenshots:** Actual, un-distorted screenshots of running software with callout highlights.
8. **Technical Icons:** Pixel-snapped $24 \times 24\text{px}$ SVG icon sets with unified stroke weights.
9. **Product Packaging Mockups:** 3D rendered boxes, workbooks, spiral notebooks, or digital bundle boxes.
10. **Background Textures:** Subtle mathematical grids, architectural blueprint lines, or dot-matrices.
11. **Hero Imagery:** Primary landing page or portal headers conveying the core transformation.
12. **Onboarding Visuals:** Step-by-step walkthrough cards guiding initial configuration.
13. **Educational Schematics:** Explanatory mechanical or operational blueprints.
14. **Decision Trees & Matrices:** 2x2 framework graphics and branching logic flows.
15. **Scorecards & Badges:** Diagnostic tier emblems and achievement seals.
16. **Social Assets:** Open Graph (OG) social share cards ($1200 \times 630\text{px}$).
17. **Creator Promotion Assets:** YouTube thumbnails, slide deck inserts, and visual one-sheets.
18. **Before / After Splits:** High-contrast side-by-side visual demonstrations of customer transformation.
19. **App-Store Style Screenshots:** Mobile application feature showcases with descriptive caption banners.
20. **Micro-Visuals / Pills:** Status indicators, checkmark badges, and metric pills.

---

## 3. Visual Continuity & Anti-"AI Slop" Protocol

To prevent products from looking like an amateur collage of random AI art:
- **Unified Palette:** All generated assets must sample exclusively from the product's approved semantic color tokens.
- **Lighting Direction:** Maintain uniform light angles across all 3D or photographic visuals (e.g. top-left directional soft light).
- **Perspective Consistency:** Do not mix 2D flat line-art with 3D glossy isometric renders within the same deliverable. Choose one visual language and maintain it throughout.
- **No Embedded Text in Rasters:** Never ask an image generator to render complex body text or fine data labels into a JPEG. Render the visual container as a clean image, then overlay real HTML/SVG typography.
