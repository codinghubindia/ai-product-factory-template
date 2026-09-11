---
name: editorial-design
description: Comprehensive editorial design standards covering publication-grade books, ebooks, executive playbooks, guides, workbooks, and whitepapers.
---

# Editorial Design Skill

Editorial design is the art and engineering of structuring, styling, and pacing long-form written and visual content so that it delivers maximum comprehension, visual authority, and reading delight.

The AI Product Factory rejects "content generation" (dumping raw markdown blocks or generic web cards). Every publication deliverable must be engineered with intentional **Information Architecture**, **Typographic Hierarchy**, and **Visual Rhythm**.

---

## 1. The 24 Dimensions of Commercial Editorial Design

1. **Book Architecture & Anatomy:** Complete structural sequence:
   - Outer Front Cover (Title, Subtitle, Authority Byline, Brand Mark).
   - Inside Front / Half-Title Page.
   - Colophon / Copyright & Provenance Page (Version, Date, ISBN/SKU, Disclaimers, Sources Citation).
   - Executive Summary / Transformation Promise.
   - Table of Contents (Hierarchical, page-numbered, dot leaders).
   - Part / Module Dividers (for publications > 30 pages).
   - Chapter Openers (Number, Title, Subtitle, Chapter Epigraph or Key Takeaway, Estimated Read/Completion Time).
   - Core Body Content (with structured rhythm).
   - Section Summaries & Action Items.
   - Worksheets & Implementation Tools.
   - Appendix / Glossaries / Source Provenance Register.
   - Back Cover / Next Steps & Ecosystem Map.

2. **Typographic Scale & Harmony:**
   - Single scale ratio (Major Third 1.250 or Perfect Fourth 1.333).
   - Standard scale:
     - Document Title (H1 / Cover): 28pt – 36pt (Bold / Black).
     - Chapter Title (H1): 22pt – 26pt.
     - Section Heading (H2): 16pt – 18pt (Semibold / Bold).
     - Subsection Heading (H3): 12pt – 14pt (Semibold).
     - Body Text: 10pt – 11pt (Regular, 1.45 – 1.65 line-height).
     - Captions, Footnotes, Folios: 8pt – 9pt.
   - Maximum 2 font families: One Editorial Display (e.g. Serif like Merriweather, Georgia, Playfair, or Clean Sans like Inter Display, Cabinet Grotesk) and one Workhorse Body (e.g. Inter, Newsreader, Source Sans, Charter).

3. **Measure & Line Length (The Golden Reading Zone):**
   - Body measure must strictly sit between **45 and 75 characters per line** (ideal: 65 characters).
   - Full-width text spanning across an entire Letter/A4 page (> 90 characters) causes severe reading fatigue and line re-reading errors. Multi-column or indented margins must be used when page width exceeds 600px of text space.

4. **Paragraph Rhythm & Indentation:**
   - Either block paragraphs (paragraph gap of 0.6em – 0.8em, zero indent) OR indented paragraphs (0.25in – 0.35in indent, zero gap). Never mix both randomly.
   - The first paragraph immediately following a heading or chapter opener must NEVER be indented.

5. **Drop Caps & Chapter Openings:**
   - Chapter openers should feature an intentional first-paragraph drop cap (2 or 3 lines deep) or an oversized lead paragraph (12pt – 13pt italic/medium) to visually invite the reader into the chapter.

6. **Running Headers & Section Trackers:**
   - Running heads appear at the top margin (outside or centered).
   - Verso (left page): Document / Book Title or Part Title.
   - Recto (right page): Current Chapter or Current Section Name.
   - Suppressed on Cover, Half-Title, Blank, and Chapter Opener pages.

7. **Folios (Pagination):**
   - Folios (page numbers) must be unambiguous: either centered at the bottom or set flush to the outside margin.
   - Front matter uses lowercase Roman numerals (`i`, `ii`, `iii`, `iv`); main body starts at Arabic numeral `1`.

8. **Visual Pacing & Rhythm:**
   - Long stretches of continuous text must be intentionally broken every 250–350 words by a visual element:
     - Pull quote.
     - Key Takeaway callout box.
     - Data summary / Metric pill.
     - Diagram / Schematic illustration.
     - Structured comparison table.
     - Reflection prompt / Worksheet field.

9. **Pull Quotes & Marginalia:**
   - Pull quotes must highlight pivotal insights or contrarian truths, set in 14pt – 18pt italic with an intentional accent border or oversized quotation glyphs.
   - Sourced quotes must include the speaker's name and role in 9pt small caps or muted text.

10. **Callout Boxes & Information Badges:**
    - High-utility containers categorized by intent:
      - `Concept / Core Principle` (Soft Blue / Navy accent).
      - `Warning / Common Pitfall` (Soft Amber / Ochre accent).
      - `Executive Action / Fast-Track` (Soft Emerald / Forest accent).
      - `Deep Dive / Advanced Formula` (Neutral Slate / Bordered).
    - Every callout must have an explicit header badge and padding (16px – 24px) with rounded or sharp editorial borders.

11. **Tables as Information Design:**
    - Tables must not look like raw spreadsheets.
    - Header rows must have clear visual distinction (tinted background, bold uppercase 8.5pt text, subtle border).
    - Numeric data must be right-aligned; text left-aligned; status pills/badges centered.
    - Subtle alternating row striping or clean border rules (`border-bottom: 1px solid #e2e8f0`).
    - Explicit column widths to prevent awkward word wrapping.

12. **Diagrams, Schematics & Process Flows:**
    - Linear processes must use numbered sequential steps (1 -> 2 -> 3) with clear connector graphics.
    - Matrices (e.g. 2x2 grids, quadrant frameworks) must have labeled axes and quadrant descriptors.

13. **Bullet Lists & Ordered Lists:**
    - Lists must never be unstructured wall-of-bullet dumps.
    - Each bullet item must begin with a **Bold Lead-in Phrase** (2–4 words) followed by an explanatory clause.

14. **Footnotes & Citations:**
    - Empirical claims, statistical benchmarks, and case evidence must carry numerical superscript citations (`[1]`, `[2]`) linked to page-bottom footnotes or the end-matter provenance register.

15. **Editorial Voice & Tone Consistency:**
    - Authoritative, actionable, precise, and respectful of the reader's time.
    - Zero generic AI fluff ("In today's fast-paced world...", "It's important to remember...").

16. **Whitespace as an Active Design Element:**
    - Generous margins (minimum 0.75in / 20mm; inside gutter 0.85in – 1.0in for print).
    - Whitespace creates hierarchy, focus, and prestige. A crowded page signals amateur production.

17. **Contrast & Hierarchy Clarity:**
    - Text contrast ratio against page background must meet or exceed WCAG AAA (7:1) for body text and 4.5:1 for large headings.
    - Body text: `#1e293b` (Slate 800) or `#111827` (Gray 900) on pure white `#ffffff` or ivory `#fdfcf7`.

18. **Page Break Discipline & Anti-Collision:**
    - Headings must never break across a page or sit stranded at the bottom (`break-after: avoid;`).
    - Tables and callout cards must never split awkwardly in half unless exceeding a full page (`break-inside: avoid;`).
    - Strict widow and orphan suppression (`orphans: 3; widows: 3;`).

19. **Formulas & Code Blocks:**
    - Monospace fonts (Fira Code, JetBrains Mono, Consolas).
    - High-contrast syntax container with soft background, rounded corners, and clear language label.

20. **Checklists & Rubrics:**
    - Checklists must feature crisp, printable squares (`[ ]` or SVG 14x14px rounded rects).
    - Rubrics must include explicit scoring criteria and scoring totals.

21. **Action Guides & Playbook Cards:**
    - Step-by-step SOPs structured with:
      - Objective.
      - Required Inputs / Tools.
      - Exact Procedure (numbered).
      - Expected Output / Deliverable.
      - Quality Gate / Verification Check.

22. **Interactive Elements (Digital PDF):**
    - Clickable Table of Contents links with bookmarks.
    - Hyperlinks styled with subtle underline and external icon.
    - Interactive fillable form fields when delivered as a digital workbook.

23. **Front and Back Matter Coherence:**
    - Front matter establishes authority, context, and orientation.
    - Back matter provides implementation roadmaps, glossary, acknowledgments, and next actions.

24. **Multi-Format Export Readiness:**
    - Clean semantic markup allowing compilation into interactive HTML, print-ready PDF, or ebook formats without rewriting.

---

## 2. Editorial Layout Archetypes

Publications should alternate between these proven editorial page archetypes to maintain engagement:

| Archetype | Description | Primary Use Case |
|---|---|---|
| **A. The Grand Opener** | Full bleed or oversized header, chapter number, compelling title, 3-line drop cap lead, chapter outline pill. | Beginning of every chapter or major module. |
| **B. The Deep Narrative** | Single column with comfortable margins (60-68 chars measure), section headings, pull quotes in outer margins. | Core explanations, analytical breakdowns, strategic concepts. |
| **C. The Analytical Matrix** | Comparison tables, pros/cons columns, 2x2 frameworks, evaluation rubrics. | Decision frameworks, tool comparisons, audit scorecards. |
| **D. The Step-by-Step SOP** | Numbered sequence badges, bold action leads, code/formula snippets, expected outputs. | Practical implementation, workflows, tactical execution. |
| **E. The Executive Takeaway** | Full-width summary card, 3 key metrics or bulleted directives, callout box for immediate action. | Chapter ends, module conclusions, executive summaries. |
| **F. The Implementation Worksheet** | Generous ruled lines (8mm spacing), checkboxes, structured prompt boxes, reflection prompts. | Workbooks, planners, coaching guides, interactive exercises. |
