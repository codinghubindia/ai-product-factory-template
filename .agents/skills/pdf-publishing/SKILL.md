---
name: pdf-publishing
description: Guidelines and automated pipelines for compiling high-resolution, print-ready, pagination-perfect PDF deliverables from HTML/CSS or Pandoc engines.
---

# PDF Publishing Skill

This skill governs the compilation of publication-grade PDF deliverables from structured source files (HTML/CSS, Markdown, or docx), ensuring pixel-accurate typography, pagination, vector diagrams, and metadata.

## 1. Core Invariants

- **Page Geometry & Margins:** Use standard ISO A4 (`210mm x 297mm`) or US Letter (`8.5in x 11in`) with minimum `20mm` (0.75in) outer margins.
- **Orphan & Widow Control:** Headings must never appear alone at the bottom of a page (`break-after: avoid; orphans: 3; widows: 3;`).
- **Running Headers & Footers:** Every page (except the title cover) must include a discreet running header (document title/section) and running footer (page number, copyright/confidentiality note).
- **High-DPI Visuals:** All embedded images, charts, and brand marks must be at least 300 DPI or vector format (SVG).
- **Embedded Fonts:** Fonts must be embedded or cross-platform safe system fonts (e.g., Inter, Merriweather, Georgia, Helvetica Neue, Segoe UI) with proper weight variants.

## 2. Tools & Engines

- Primary Engine: Headless Chrome / Puppeteer / Playwright printing or `system/scripts/document_builder.py`.
- Alternative Engine: Weasyprint (`python -m weasyprint`) or Pandoc (`pandoc -o output.pdf`).
- Verification Tool: `system/scripts/artifact_inspector.py` and `pypdf` / `pikepdf`.

## 3. PDF Layout CSS Specification

Every PDF-targeted HTML template must include `@page` CSS:
```css
@page {
  size: A4 portrait;
  margin: 20mm 15mm 20mm 15mm;
  @top-left {
    content: "Document Title";
    font-size: 8pt;
    color: #64748b;
  }
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-size: 8pt;
    color: #64748b;
  }
}
@page:first {
  @top-left { content: normal; }
  @bottom-right { content: normal; }
}
h1, h2, h3 {
  break-after: avoid;
  page-break-after: avoid;
}
table, figure, .callout-card, .metric-box {
  break-inside: avoid;
  page-break-inside: avoid;
}
```

## 4. Step-by-Step Procedure

1. **Source Inspection:** Verify source HTML or markdown has semantic tags (`<h1>`, `<h2>`, `<p>`, `<table>`, `<blockquote>`).
2. **CSS Injection:** Attach print stylesheet with `@page` definitions and `@media print` rules.
3. **Execution:**
   - Execute PDF rendering via `system/scripts/document_builder.py --input <source.html> --output <final.pdf> --pdf`.
4. **PDF QA Audit:**
   - Inspect total page count and verify page 1 is the cover/hero.
   - Verify page numbers are sequential and footer metadata is intact.
   - Check tables for column clipping or horizontal overflow.
   - Validate file size (non-zero, under 25MB for easy customer download).
