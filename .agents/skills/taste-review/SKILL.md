---
name: taste-review
description: Independent artistic and aesthetic critique evaluating visual originality, restraint, editorial maturity, niche authenticity, and eliminating generic AI appearance.
---

# Taste Review Skill

A product can pass automated unit tests, compile without syntax errors, and satisfy basic WCAG accessibility while still looking and feeling completely generic, uninspired, or unmistakably "AI-generated."

The **Taste Review** is an adversarial aesthetic and creative audit. Its primary mandate is to detect and reject products that are **technically competent but creatively sterile**.

---

## 1. The Core Taste Standard

> **The Taste Invariant:** If a knowledgeable practitioner in the target niche glances at the deliverable and immediately thinks *"an AI made this in 30 seconds"*, the product **FAILS** taste review unconditionally.

The product must exhibit the quiet confidence, disciplined restraint, and deep domain authenticity of an artifact crafted by senior industry professionals.

---

## 2. The Twelve Dimensions of Taste

The `taste-reviewer` rigorously scores the product across 12 criteria (1 to 5 scale, minimum 4.0 average required to pass):

1. **Restraint & Elimination of Noise:**
   - Are visual elements limited strictly to those that clarify meaning?
   - Has all gratuitous decoration (random card piles, neon gradients, meaningless background blobs) been ruthlessly removed?

2. **Visual Hierarchy & Flow:**
   - Does the eye naturally travel from primary anchor to secondary detail without disorientation?
   - Is there clear typographic contrast between titles, section headers, body copy, and captions?

3. **Typographic Maturity:**
   - Are font sizes, weights, and leading disciplined?
   - Is the line length measure strictly within the 45–75 character sweet spot?
   - Are there zero orphaned headings or widowed words?

4. **Authenticity to the Niche:**
   - Does the visual and verbal vocabulary feel native to the professional tribe?
   - Or does it look like an outsider’s caricature of the industry?

5. **Originality & Distinctiveness:**
   - Does the product possess an unmistakable personality and visual metaphor?
   - Or does it look like a standard off-the-shelf Tailwind/Bootstrap template?

6. **Coherence Across Media:**
   - Do the document PDFs, spreadsheet tabs, web screens, and packaging mockups look like they share the exact same visual DNA?

7. **Subtlety & Color Restraint:**
   - Is the color palette purposeful and semantic?
   - Are backgrounds clean and high-contrast, avoiding muddy pastels or unreadable low-contrast grays?

8. **Image & Diagram Quality:**
   - Are diagrams crisp vector graphics with clear labels?
   - Are any raster assets free of AI distortions, melted fingers, or bizarre hallucinated artifacts?

9. **Handwriting & Interactive Ergonomics:**
   - In workbooks: Do handwriting lines have true 8mm vertical clearance?
   - Are form inputs and checkboxes tactile and cleanly aligned with text baselines?

10. **Information Density & Rhythm:**
    - Does the layout alternate comfortably between dense explanatory sections, structured comparison tables, and expansive reflection/action spaces?
    - Does it prevent visual fatigue?

11. **Absence of Cliché & Platitude:**
    - Is the copy free of generic AI tropes ("In today's fast-paced world...", "Empower your workflow...", "Revolutionize your team...")?
    - Is every sentence sharp, actionable, and concrete?

12. **Perceived Craftsmanship & Prestige:**
    - Would a customer feel proud sharing this deliverable with their boss, executive team, or peers?

---

## 3. Red Flags: Automatic Failures in Taste Review

A product receives an immediate **FAIL** if any of the following are detected:
- [ ] **The "AI Neon" Symptom:** Random purple-to-cyan or pink-to-blue gradient overlays with no semantic meaning.
- [ ] **The Floating Card Avalanche:** Splitting continuous narrative content into 15 floating rounded boxes.
- [ ] **Microscopic Writing Rules:** Presenting a "workbook" with 12pt–14pt line spacing that no human can physically write on with a pen.
- [ ] **Wall-of-Bullets Disease:** More than 5 unformatted bullet points in a row without bold lead-in phrases or structural groupings.
- [ ] **Unformatted Numbers:** Spreadsheets with raw floating-point numbers (`14.285714%` or `$1245.892`) rather than explicit formatting.
- [ ] **Mismatched Visual Assets:** Combining flat 2D line-art icons with glossy 3D isometric illustrations in the same chapter.

---

## 4. The 6-Part Master Review Stack

Taste Review is one layer in the Factory's final sign-off stack:

$$\text{UTILITY} + \text{DESIGN} + \text{TASTE} + \text{PSYCHOLOGY} + \text{COMMERCIAL} + \text{CREATOR FIT}$$

The output of this audit is written to `products/<product_id>/audit/taste-review.md`.
