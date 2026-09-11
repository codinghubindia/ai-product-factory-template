---
name: visual-quality-review
description: Visual inspection criteria, layout auditing procedures, rendering defect detection, and design polish reviews for digital products before customer shipment.
---

# Visual Quality Review Skill

This skill governs the visual review and aesthetic inspection of rendered deliverables, software interfaces, presentation slides, and marketing packaging assets.

## 1. Core Rule: Render & Inspect

Never evaluate visual quality from Markdown, CSS rules, or JSX source code alone. The artifact or software must be rendered into its actual visual form and inspected as a human customer would experience it.

## 2. The Visual Defect Taxonomy

During visual inspection, look specifically for:
1. **Alignment & Grid Drift:** Elements that are misaligned by a few pixels; ragged left margins; unaligned form labels.
2. **Typography Clutter & Hierarchy Gaps:**
   - Too many font families (max 2: one for headings, one for body/mono).
   - Inconsistent line heights causing cramped lines or floating headings.
   - Orphan headers resting at the bottom of pages or columns.
3. **Clipping & Truncation:**
   - Text overflowing containers with `overflow: hidden` cutting off text descenders (`g`, `y`, `p`).
   - Long labels in tables getting truncated with `...` without tooltip or expander.
4. **Contrast & Readability Failures:**
   - Light gray text (`#cbd5e1`) on white backgrounds.
   - Text over busy photographic backgrounds without high-contrast scrims.
5. **Asset Degradation:**
   - Low-resolution raster images (pixelated or blurry logos/screenshots).
   - Distorted aspect ratios (stretched or squashed icons/diagrams).
6. **Gratuitous Noise:**
   - Excessive rainbow gradients.
   - Heavy drop shadows that dirty the page.
   - Flashing animations or hover effects that cause layout shifts (CLS).

## 3. Step-by-Step Inspection Procedure

1. **Artifact Rendering:**
   - For documents: Render HTML in browser or compile to PDF.
   - For software: Launch running server and open in browser across mobile, tablet, and desktop viewports.
   - For slides: View in full-screen 16:9 presentation mode.
2. **Systematic Walkthrough:**
   - Inspect the Cover / Landing Screen: Does it look intentionally designed by an enterprise agency?
   - Inspect Data Displays: Are table headers distinct, numbers readable, and cell padding generous?
   - Inspect Edge States: Trigger empty state, loading state, error alert, and modal dialog.
3. **Scorecard & Findings Log:**
   - Log visual defects in `products/<product_id>/audit/visual-review.md`.
   - Assign severity:
     - `CRITICAL`: Unreadable text, completely broken layout, obscured core data.
     - `HIGH`: Major misalignments, low-res hero assets, clipping on standard viewports.
     - `MEDIUM`: Minor spacing inconsistencies, suboptimal padding.
     - `LOW`: Polish opportunities.
4. **Approval Gate:**
   - Zero `CRITICAL` and zero un-waived `HIGH` visual defects allowed for Gate 4 approval.
