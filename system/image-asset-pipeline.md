# AI PRODUCT FACTORY — IMAGE & VISUAL ASSET PRODUCTION PIPELINE

Visual assets are not random decorative filler; they are engineered functional components of the product experience.

The **Image & Visual Asset Pipeline** governs the planning, sourcing, generation, rights verification, visual quality auditing, and artifact integration of all visual elements across the product factory.

```text
PRODUCT STRATEGY
  → CREATIVE DIRECTION
  → ASSET REQUIREMENTS MATRIX
  → IMAGE / ASSET RESEARCH & SOURCING
  → DETERMINISTIC GENERATION (OR LICENSED ASSET RETRIEVAL)
  → RIGHTS & PROVENANCE AUDIT
  → ASSET QA (ISOLATION)
  → INTEGRATION INTO ARTIFACT
  → FINAL ARTIFACT RENDER
  → VISUAL QA (CONTEXTUAL IN-LAYOUT)
```

---

## 1. The 17-Point Asset Record Specification

Every visual asset integrated into any product deliverable or packaging asset must be cataloged in `products/<product_id>/assets/asset-manifest.json` following this authoritative schema:

| Field | Type | Description / Constraints |
|---|---|---|
| `asset_id` | String | Unique identifier: `ast-<kebab-name>-v<N>` (e.g. `ast-hero-flight-deck-v1`). |
| `name` | String | Human-readable title of the asset. |
| `role` | String | Enum: `cover`, `chapter_opener`, `editorial_diagram`, `ui_mockup`, `device_frame`, `icon_set`, `background_texture`, `social_thumbnail`, `creator_promo`. |
| `placement` | String | File and selector/page location where the asset appears (e.g. `final/playbook.html#chapter-1-hero`). |
| `type` | String | Enum: `svg`, `png`, `jpg`, `webp`. (SVGs required for diagrams/icons; PNG for screenshots/mockups; WebP/JPG for raster artwork). |
| `source` | String | Enum: `generated`, `licensed_stock`, `public_domain`, `custom_vector_code`, `screenshot`. |
| `generated_or_sourced` | String | Name of engine or repository (e.g. `generate_image`, `open-icon-library`, `local-render`). |
| `prompt_or_source_ref` | String | Exact generative text prompt OR canonical URL / source archive path. |
| `license_status` | String | Enum: `factory_original`, `cc0`, `mit`, `commercial_royalty_free`, `editorial_reference_only`. |
| `aspect_ratio` | String | Standard ratio: `1:1`, `16:9`, `4:3`, `3:2`, `2:3`, `3:4`, `9:16`. |
| `dimensions` | Object | Width and height in pixels: `{ "width": 1920, "height": 1080 }`. |
| `resolution_dpi` | Integer | Minimum 300 DPI for print deliverables; 72–144 DPI for web/digital screens. |
| `color_profile` | String | `sRGB` (digital) or `CMYK-compatible` (print). |
| `version` | Integer | Monotonically increasing revision integer (`1`, `2`, ...). |
| `approved` | Boolean | True only after passing both Asset QA and Visual QA. |
| `used_in` | Array | Array of deliverable paths utilizing this asset. |
| `attribution_req` | String | Required attribution string if licensed (or `null` if public domain/factory original). |

---

## 2. Visual Continuity & Anti-"AI Slop" System

A product containing visuals must look like it was created by a single art director, not an assorted grab-bag of disparate AI generations.

For every product with visual assets, the `creative-director` must establish the **Visual Continuity Spec** in `design/<product_id>/visual-continuity.md` defining:
1. **Color Palette Mapping:** Exact hex tokens allowed in imagery (e.g. Deep Slate `#0f172a`, Blueprint Blue `#2563eb`, Accent Amber `#d97706`).
2. **Lighting & Atmosphere:** Lighting direction, shadow softness, and ambient temperature (e.g. "Low-angle directional morning light, sharp architectural shadows, cool neutral temperature").
3. **Rendering & Texture Style:** Vector blueprint, technical schematic, isometric line-art, or high-contrast duotone. (Strictly prohibited: cartoonish 3D clay figures, generic purple AI neon, or oversaturated plastic skins).
4. **Perspective & Framing:** Standard camera elevation (e.g. "Strict isometric 30-degree orthographic" or "Eye-level editorial landscape with shallow depth of field").
5. **Subject Treatment:** How humans, interfaces, or systems are depicted.
6. **Recurring Motifs:** Explicit graphical recurring elements (e.g. subtle 5mm technical grid lines, hairline borders, precision callout crosshairs).

---

## 3. External Asset Research & Provenance Verification

When an asset is sourced from external repositories rather than created in-house:
- **Strict Verification Protocol:**
  1. Record primary provenance URL in `memory/sources.csv`.
  2. Verify explicit commercial-use licensing (`CC0`, `MIT`, `Apache 2.0`, or purchased commercial license).
  3. Reject assets with ambiguous licensing, "free for personal use only" tags, or missing copyright holder statements.
  4. Ensure any attribution requirements are embedded in the deliverable colophon and `delivery-manifest.json`.
- **Reference vs. Production Isolation:** External images used as creative inspiration or moodboard references must be stored in `research/moodboards/` and must **NEVER** be packaged or shipped into `final/` customer deliverables.

---

## 4. Two-Stage Asset Quality Assurance (QA)

### Stage 1: Isolation QA (`asset-director`)
Before any visual asset is integrated into HTML/PDF/Software:
- [ ] Correct pixel dimensions matching aspect ratio specification.
- [ ] Resolution meets minimum threshold ($\ge 300\text{ DPI}$ for print, $\ge 1080p$ for desktop screens).
- [ ] Visual consistency with the Visual Continuity Spec.
- [ ] Zero unwanted AI visual artifacts (mangled hands, garbled text glyphs, bizarre edge melting).
- [ ] Zero accidental text embedded inside raster images (all typography must be real semantic text or vector SVG).
- [ ] Clean transparency channels (no jagged white halos on PNG icons).
- [ ] Aspect ratio preserved without horizontal or vertical stretching.

### Stage 2: In-Context Visual QA (`taste-reviewer` & `artifact-qa`)
After the asset is placed inside the rendered artifact:
- [ ] Asset serves information hierarchy and does not distract from core copy.
- [ ] Image does not push critical text or worksheet handwriting rules across awkward page breaks.
- [ ] Colors harmonize with adjacent body typography and container borders.
- [ ] In monochrome print preview: Asset maintains high clarity and contrast when rendered in 100% grayscale.
