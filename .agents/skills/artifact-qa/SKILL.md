---
name: artifact-qa
description: Quality assurance protocols for inspecting compiled digital deliverables (PDF, DOCX, XLSX, PPTX, HTML, ZIP) for format integrity, formulas, clipping, and placeholders.
---

# Artifact Quality Assurance Skill

This skill governs the physical inspection and validation of generated digital files (.pdf, .xlsx, .docx, .pptx, .html, .sqlite, .zip) before any product can proceed to packaging or release.

## 1. Core Invariants

- **Non-Empty Deliverables:** Deliverable files must physically exist, be non-zero in size, and have valid magic byte signatures.
- **Zero Placeholder Text:** Strictly ban placeholder tokens across all files:
  `TODO`, `LOREM IPSUM`, `[INSERT`, `TBD`, `REPLACE_THIS`, `COMING SOON`, `DRAFT ONLY`.
- **Accurate Metadata:** Author, title, creation timestamp, and version must be properly set in document and archive properties.
- **Manifest Integrity:** Every deliverable in `products/<product_id>/final/` must match an entry in `products/<product_id>/artifact-manifest.json` with file size, extension, and build status.

## 2. Format-Specific Inspection Checklists

### PDF & HTML Documents
- [ ] No awkward page breaks cutting across headings, code blocks, or callout cards.
- [ ] Running headers and footers contain proper title and dynamic page numbers ("Page X of Y").
- [ ] All table columns fit within printable margins; no horizontal overflow clipping.
- [ ] High-contrast readability (black/dark-slate text on white/light background).
- [ ] Zero unrendered raw Markdown syntax (e.g. leftover `###` or unparsed `[link]()`).

### Spreadsheets (XLSX / CSV)
- [ ] Zero formula error codes (`#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`).
- [ ] Top headers are frozen (`freeze_panes`) for scrollability.
- [ ] Explicit number formatting applied ($ / % / commas / dates).
- [ ] Column widths auto-fit data length with margin padding (no `###` truncation).
- [ ] Instructions tab explains model structure and color-coded input legend.

### Presentations (PPTX)
- [ ] 16:9 widescreen layout standard.
- [ ] Zero text boxes overlapping slide margins or spilling off screen.
- [ ] Legible font sizes (Title >= 28pt, Body >= 14pt).
- [ ] High-contrast contrast ratios between text and background.

### Release ZIP Archives
- [ ] Unzips cleanly without path traversal vulnerabilities (no `../` in archive paths).
- [ ] Contains customer onboarding `README.md` and `LICENSE`.
- [ ] File permissions are safe (no unnecessary executable flags on data files).

## 3. Automated Inspection Tooling

Run the artifact inspector script:
```bash
python system/scripts/artifact_inspector.py products/<product_id>/final/
```
Output results are written to `products/<product_id>/audit/artifact-qa.json` and summarized in `artifact-qa-report.md`.
