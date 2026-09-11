---
name: workbook-planner-design
description: Design principles, handwriting ergonomics, and technical specifications for engineering commercial workbooks, guided journals, implementation planners, and fillable PDF forms.
---

# Workbook & Planner Design Skill

A commercial workbook or planner is an interactive cognitive workspace, not a passive text document with empty lines tacked onto the end.

This skill establishes the production standard for engineering workbooks, guided journals, operational planners, and field manuals that deliver genuine behavioural change and delightful handwriting ergonomics.

---

## 1. Physical Handwriting Ergonomics

Human handwriting with pens, pencils, or stylus markers requires substantially more vertical clearance than printed text.

- **The 8mm Rule (Rule Line Spacing):**
  - Standard printed body text has a line-height of 14pt – 16pt (4.5mm – 5.5mm).
  - Physical handwriting requires **minimum 8.0 mm to 9.5 mm** (24pt to 28pt) between horizontal ruled lines.
  - Designing writing lines at 14pt makes them completely unusable for physical writing.
- **Dot Grid & Graph Standards:**
  - Dot grids must use **5.0 mm** (approx. 14.17pt) spacing between dot centers.
  - Dots must be rendered in subtle slate (`#cbd5e1` / 40% gray) with a diameter of `0.75pt` to `1.0pt`.
- **Boxed Text Areas:**
  - Short-answer fields: minimum 40px (10mm) height.
  - Extended reflection / brainstorm boxes: minimum 120px to 240px (30mm to 60mm) height with subtle interior faint guide rules.
- **Margin Clearance:**
  - Leave at least `12mm` padding inside any framed writing box so writing does not bump against container borders.

---

## 2. Anatomy of a High-Utility Worksheet Page

Every workbook exercise or planner spread must follow a deliberate 5-part architecture:

1. **Context Header:**
   - Exercise Number & Title.
   - Core Objective (1 sentence explaining *why* this exercise matters).
   - Time Estimate (e.g. "Estimated Time: 15–20 minutes").
2. **Framework / Guiding Principle:**
   - A brief, punchy visual anchor (a mini 2x2 matrix, a 3-step formula, or a concrete reference example).
   - *Crucial Rule:* Never require the user to flip back 10 pages to remember how to fill out the exercise.
3. **Structured Prompt Sequence:**
   - Broken into distinct, numbered sub-questions rather than 1 giant open-ended question.
   - Clear placeholder prompt (e.g. "Trigger Event:", "Immediate Response:", "Desired Alternative:").
4. **Ergonomic Workspace:**
   - Clean 8mm horizontal rules or structured columnar cards with ample handwriting space.
5. **Commitment & Validation Footer:**
   - Action Milestone checkbox: `[ ] Implementation completed and logged`.
   - Date / Sign-off field (`Completed on: _______ | Reviewed by: _______`).

---

## 3. Checkboxes, Rating Scales & Trackers

- **Checkboxes:**
  - Dimensions: Exactly `14px x 14px` to `16px x 16px` (approx. 4mm – 4.5mm).
  - Border: 1.5pt solid `#64748b` or `#475569`.
  - Border-radius: 3px (subtle rounded square for a modern, tactile feel).
  - Baseline Alignment: Perfectly vertically centered with the first line of accompanying text.
- **Rating Scales & Scoring Rubrics:**
  - Likert scales must use distinct circular or pill-shaped numbered bubbles (1 to 5 or 1 to 10) with explicit polar labels (e.g. `1 = Severe Friction` ... `5 = Frictionless Flow`).
- **Habit & Weekly Trackers:**
  - Weekly tables must feature 7 explicit day columns (`M`, `T`, `W`, `T`, `F`, `S`, `S`) with generous completion circles or check cells (minimum 20px x 20px).
  - Monthly habit grids must include 31 compact tracking cells with week-separator lines.

---

## 4. Dual-Mode Digital + Print Utility (Fillable PDFs)

Commercial digital workbooks are used in two ways:
1. Printed on home/office paper for physical handwriting.
2. Opened in PDF viewers (Adobe Acrobat, GoodNotes, Apple Books, Chrome) for digital typing.

Every workbook HTML template must include dual-mode form architecture:
- Text inputs and textareas styled with clean border rules and readable fonts.
- In digital viewing, these inputs are interactive and editable.
- In print mode, inputs automatically render as clean empty ruled lines or framed answer boxes.

```css
/* Interactive & Printable Form Fields */
.fillable-line {
  width: 100%;
  border: none;
  border-bottom: 1.5px solid #cbd5e1;
  background: transparent;
  font-family: inherit;
  font-size: 11pt;
  line-height: 28pt; /* 8.5mm handwriting height */
  margin-bottom: 8px;
  outline: none;
}
.fillable-box {
  width: 100%;
  min-height: 120px;
  border: 1.5px solid #e2e8f0;
  border-radius: 6px;
  background: #f8fafc;
  padding: 12px;
  font-family: inherit;
  font-size: 10pt;
  resize: vertical;
}
@media print {
  .fillable-box {
    background: #ffffff;
    border-color: #cbd5e1;
  }
}
```

---

## 5. Visual Pacing & Fatigue Prevention

Working through exercises is cognitively demanding. To prevent user drop-off and mental fatigue:

- **The Rule of 3 Exercises:** Never place more than 3 consecutive high-density worksheets without an intervening summary page, case example, or visual roadmap.
- **Progress Badges:** Include visual milestone badges (e.g., `Phase 1: Diagnostic [Complete]`, `Phase 2: Strategy [In Progress]`).
- **Scorecards & Audits:** Conclude each major section with a quantified scoring matrix that gives the user a tangible score or diagnostic maturity level.

---

## 6. Workbook Quality Audit Gates

Before certifying a workbook or planner:
- [ ] Handwriting space verified: ruled lines are at least 8mm (24pt) apart.
- [ ] Checkboxes have minimum 14x14px hit area and 1.5pt crisp borders.
- [ ] Dot grids use 5mm spacing in subtle gray (`#cbd5e1`).
- [ ] Form fields tested interactively: typing works in PDF viewers and rules display cleanly when printed.
- [ ] Page breaks respect worksheets: no exercise prompt is separated from its answer space across a page break.
- [ ] Every exercise includes an explicit objective and time estimate.
