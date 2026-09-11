---
name: print-production
description: Specifications and technical rules for physical print geometry, trim sizes, gutter margins, bleeds, safe zones, monochrome contrast, PDF metadata, and vector assets.
---

# Print Production Skill

This skill governs the physical print engineering and commercial output standards for all printed and printable deliverables (books, workbooks, planners, guides, cheatsheets, and executive reports).

Digital PDFs intended for print must not be designed like web screens. Physical paper imposes hard constraints of binding, trim variation, ink absorption, and monochrome home-printing realities.

---

## 1. Standard Physical Trim Sizes

The factory targets four standard commercial print formats:

| Format Name | Dimensions (inches) | Dimensions (mm) | Recommended Deliverable Types | Gutter Margin (Inside) | Outer Margin |
|---|---|---|---|---|---|
| **US Letter** | 8.5" x 11.0" | 215.9 x 279.4 mm | Standard US Reports, Corporate Playbooks, Forms | 0.85 in (22mm) | 0.75 in (19mm) |
| **ISO A4** | 8.27" x 11.69" | 210.0 x 297.0 mm | International Reports, Workbooks, Executive Briefs | 24 mm | 20 mm |
| **US Executive / Crown** | 7.0" x 10.0" | 177.8 x 254.0 mm | Executive Manuals, Premium Handbooks, Planners | 0.80 in (20mm) | 0.65 in (16.5mm) |
| **Trade Paperback** | 6.0" x 9.0" | 152.4 x 228.6 mm | Non-fiction Books, Thought Leadership Ebooks | 0.75 in (19mm) | 0.55 in (14mm) |

---

## 2. Print Geometry: Bleed, Trim & Safe Zones

When engineering print-ready deliverables:

1. **Trim Box:** The final trimmed physical page boundary.
2. **Bleed Area:** Background colors, full-page imagery, or edge banners that extend to the page edge must bleed **0.125 inches (3.175 mm)** beyond the trim line on all outer edges.
3. **Safe Margin Zone:** No critical content (text, icons, table cells, folios) may sit closer than **0.375 inches (9.5 mm)** to any trim edge.
4. **Binding Gutter (Inside Margin):**
   - For saddle-stitched or spiral-bound workbooks: Minimum `0.75 in` (19mm).
   - For perfect-bound books (> 60 pages): Add `0.002 in` per leaf to account for the spine curve; minimum `0.85 in` – `1.0 in` (22mm – 25mm).
   - CSS representation:
     ```css
     @page :left {
       margin-left: 20mm;  /* outer */
       margin-right: 25mm; /* gutter (inside) */
     }
     @page :right {
       margin-left: 25mm;  /* gutter (inside) */
       margin-right: 20mm; /* outer */
     }
     ```

---

## 3. The Monochrome & Grayscale Print Rule

Over 60% of customers who print digital deliverables print them on **black-and-white laser or inkjet printers**.

- **Contrast Invariant:** Every visual element must maintain high readability when converted to pure grayscale.
- **Prohibited:**
  - Light gray text (`#94a3b8` or `#cbd5e1`) for body or instructional text; it becomes illegible or washes out entirely on 600 DPI monochrome laser printers.
  - Relying exclusively on color to convey meaning (e.g. green vs. red status without icons or text labels).
  - Pale pastel backgrounds with white text.
- **Enforced:**
  - Body text must be high-contrast dark: minimum 75% black (`#1e293b` or `#111827`).
  - Table borders and dividing lines must be at least 1pt solid with `#cbd5e1` or `#94a3b8` for clear reproduction.
  - Fillable writing lines must be clean rules (minimum 0.75pt `#cbd5e1` or `#94a3b8`), never faint watermark dots that disappear.

---

## 4. Typography & Font Embedding

- **Vector Precision:** All typography must be rendered as clean vector outlines or embedded TrueType / OpenType fonts (WOFF2/TTF/OTF).
- **Minimum Printable Font Sizes:**
  - Major Titles: 24pt – 36pt.
  - Section Headings: 14pt – 18pt.
  - Body Text: 10pt – 11pt.
  - Captions & Table Data: 8.5pt – 9pt.
  - Absolute Minimum (disclaimers/folios): 7.5pt. Never use sub-7pt text in any print deliverable.
- **Systematic Line Spacing:**
  - Body text line-height: `1.45` to `1.65` (15pt – 18pt leading on 10.5pt text) to prevent colliding ascenders and descenders.

---

## 5. Vector Assets & Resolution Standards

- **Raster Images:** Any photo, screenshot, or raster asset included in a printable product must be **300 DPI** at the physical dimensions it occupies on the page.
  - Example: A 4" x 3" image must be at least 1200 x 900 pixels.
- **Diagrams & Icons:** Must use resolution-independent **vector SVG** format. SVGs scale infinitely without pixelation or blurriness on 1200+ DPI commercial printing plates.

---

## 6. PDF Structural Metadata & Bookmarks

Every release-grade PDF compiled by the factory must contain complete document catalog metadata:

- `Title`: Exact commercial product title.
- `Author`: Publishing authority / brand name.
- `Subject`: Comprehensive product transformation description.
- `Keywords`: Key topic tags, industry terms, and modality tags.
- `Creator`: `AI Product Factory (Publication Engine v2.0)`.
- `Producer`: Headless Print Engine + Pikepdf.
- **Document Outlines (Bookmarks):** Multi-level clickable outline tree corresponding directly to H1, H2, and H3 headers so PDF reader applications (Acrobat, Apple Books, Chrome PDF) provide an interactive navigation panel.

---

## 7. Pre-Flight Print Checklist

Before shipping any printable deliverable:
- [ ] Trim size confirmed (US Letter, A4, or 7x10).
- [ ] Gutter margins configured for recto/verso binding.
- [ ] Zero widows (single words isolated on the last line of a paragraph).
- [ ] Zero orphans (single lines stranded at the top/bottom of a page).
- [ ] Zero headless sections (headings stranded at the bottom with no body text).
- [ ] Tested under Grayscale conversion: All text, charts, and lines remain 100% legible.
- [ ] All images tested >= 300 DPI; icons are vector SVGs.
- [ ] PDF document metadata and outlines verified using `system/scripts/artifact_inspector.py`.
