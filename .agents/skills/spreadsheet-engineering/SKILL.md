---
name: spreadsheet-engineering
description: Engineering guidelines, formula validation protocols, visual formatting rules, and generation scripts for professional Excel and CSV spreadsheet deliverables.
---

# Spreadsheet Engineering Skill

This skill governs the construction of commercial-grade spreadsheet products (.xlsx, .xlsm, .csv), including financial models, ROI calculators, operational planners, benchmark directories, and workflow trackers.

## 1. Core Invariants

- **Formula Integrity:** Absolutely zero `#REF!`, `#VALUE!`, `#DIV/0!`, `#N/A`, `#NAME?`, or circular reference errors.
- **Formula vs Hardcoded Distinction:**
  - Hardcoded user input cells must be visually distinguished (e.g., light blue/cream background or border).
  - Calculated output cells must use native spreadsheet formulas (e.g., `SUM`, `AVERAGE`, `IF`, `VLOOKUP`/`XLOOKUP`, `INDEX/MATCH`, `NPV`, `IRR`). Never paste precomputed static numbers where a dynamic formula belongs.
- **Header Ergonomics:** Top row / column headers must be frozen (`freeze_panes`) so headers stay visible upon scrolling.
- **Explicit Number Formatting:** Every numeric cell must have explicit formatting:
  - Currency: `$#,##0` or `$#,##0.00`
  - Percentage: `0.0%` or `0%`
  - Dates: `YYYY-MM-DD`
  - Integer / Count: `#,##0`
- **Multi-Tab Architecture:**
  1. `README / Instructions`: How to use, assumptions, legend, author/version.
  2. `Summary / Dashboard`: Key KPIs, high-level rollups, scenario selectors.
  3. `Data / Engine`: Detailed modeling tables, lookup arrays, calculations.
  4. `Raw Reference`: Benchmark data or static code lists.

## 2. Tools & Scripts

- Generator: `system/scripts/spreadsheet_builder.py` (uses `openpyxl` when available, with structured CSV fallback).
- Template: `templates/spreadsheets/financial-model-template.py`
- Verification: `system/scripts/artifact_inspector.py`

## 3. Production Procedure

### Step 1: Data Model Architecture
1. Define entities, inputs, variables, formulas, and desired outputs in a schema.
2. Separate assumptions from calculation engines.

### Step 2: Generation Script Execution
1. Utilize `templates/spreadsheets/financial-model-template.py` or customize generation script.
2. Ensure columns have explicit auto-adjusted widths (`column_width = max(len(val)) + 3`) to prevent `###` overflow display errors.
3. Apply styling:
   - Header fill: Dark neutral or brand theme (e.g. `#1e293b`).
   - Header text: Bold, white font (`#ffffff`).
   - Gridlines enabled explicitly (`ws.views.sheetView[0].showGridLines = True`).
   - Total/Summary rows: Top thin border, bottom double border.

### Step 3: Automated Formula & Data Verification
1. Run spreadsheet verification:
   - Load generated workbook with `openpyxl.load_workbook(data_only=False)` and verify formula strings.
   - Load with `data_only=True` after evaluation or run Python check to verify valid evaluation.
2. Confirm example data is realistic and non-trivial (no dummy `Test 1`, `Foo`, `Bar`).
3. Check duplicate/reset experience: Provide clear instructions for duplicating worksheets for new periods.
