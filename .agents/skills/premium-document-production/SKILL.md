---
name: premium-document-production
description: Production standard and procedure for engineering publication-grade executive documents, playbooks, manuals, and workbooks with semantic layout, typography hierarchy, and zero AI filler.
---

# Premium Document Production Skill

This skill governs the end-to-end creation of publication-grade digital documents, including executive playbooks, implementation manuals, standard operating procedures (SOPs), frameworks, and customer-facing workbooks.

## 1. Core Invariants

- **Zero Markdown Dumps:** A raw `.md` file or basic unstyled HTML file wrapped in `<pre>` is never a final customer deliverable.
- **Evidence-Backed Content:** Every factual benchmark, metric, formula, or quote must cite a verified record in `memory/sources.csv`.
- **Zero AI Filler:** Prohibit circular restatements, vague platitudes ("leverage synergies"), generic introductions, and speculative case studies. Deliver concrete, fillable tools, step-by-step decision trees, and quantitative frameworks.
- **Strict Visual Hierarchy:** Every document must enforce typographic rhythm, clear page composition, standardized margins, callout boxes, and formatted data tables.

## 2. Tools & Engines

- Template engine: `templates/documents/executive-playbook.html`
- Generator script: `system/scripts/document_builder.py`
- Formats: Clean standalone semantic HTML with responsive and `@page` print CSS, downloadable PDF via headless browser or Weasyprint, and DOCX when required.

## 3. Production Procedure

### Step 1: Modality & Structure Architecture
1. Confirm the document archetype:
   - **Executive Playbook:** Strategic, decision-oriented, KPI summaries, callout boxes, phased implementation roadmap.
   - **Technical Manual:** Step-by-step procedures, code/schema snippets, prerequisite checklists, verification commands, troubleshooting trees.
   - **Workbook / Field Guide:** Self-assessments, fillable exercises, scorecards, decision matrices.
2. Outline modules adhering to `products/<product_id>/specification.json`.

### Step 2: Content Engineering
1. Draft actionable core content in `products/<product_id>/content/`.
2. Format tables with explicit column headers, unit labels, and alternating row styling.
3. Integrate visual callouts for:
   - `Key Insight / Principle`
   - `Implementation Warning`
   - `Action Item / Checklist`
   - `Metric & Formula Definition`
4. Verify all factual references against `memory/sources.csv`.

### Step 3: Layout & Typography Integration
1. Apply the visual theme defined in `design/<product_id>/design-system.md`.
2. Use modular typography:
   - Font scale: Title (28-36pt), H1 (20-24pt), H2 (16-18pt), H3 (13-14pt), Body (10-11pt), Captions/Footnotes (8-9pt).
   - Line height: 1.5 - 1.6 for body text, 1.2 - 1.3 for headings.
   - Running header with document title and running footer with dynamic page numbering ("Page X of Y").
   - Page-break controls: `break-inside: avoid` on callouts, tables, and metric cards; `break-before: page` on major chapters.

### Step 4: Deliverable Compilation
Execute `system/scripts/document_builder.py` to assemble:
- Standalone HTML deliverable: `products/<product_id>/final/<slug>.html`
- Print/PDF deliverable: `products/<product_id>/final/<slug>.pdf`

### Step 5: Verification & QA
1. Run `python system/scripts/artifact_inspector.py products/<product_id>/final/<slug>.html`.
2. Verify:
   - [ ] No placeholder text (`TODO`, `LOREM IPSUM`, `[INSERT]`).
   - [ ] Zero unformatted markdown syntax in HTML output.
   - [ ] Table cells are aligned and numeric values right-aligned.
   - [ ] Page breaks do not cut through callout boxes or headings (no orphan headings).
