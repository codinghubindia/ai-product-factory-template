---
name: presentation-design
description: Guidelines and specifications for engineering professional 16:9 widescreen presentation slide decks, pitch frameworks, and visual training curricula.
---

# Presentation Design Skill

This skill governs the design, structure, and compilation of presentation decks (.pptx, .pdf slides, or HTML slide decks), ensuring strong visual hierarchy, executive scannability, and high-impact communication.

## 1. Core Invariants

- **Aspect Ratio:** Standard 16:9 widescreen (`13.33in x 7.5in` / `1920x1080px`). Never use legacy 4:3.
- **One Core Idea Per Slide:** Every slide must have a single clear takeaway expressed in the slide title (Action Title).
- **Action Titles:** Use complete declarative sentences rather than vague topic labels.
  - *Bad:* "Market Trends"
  - *Good:* "Enterprise Cloud Budgets Shifted 40% Toward Security in 2025"
- **Typography Scale:**
  - Slide Title: 28pt – 36pt Bold.
  - Subtitle / Context: 16pt – 18pt Regular.
  - Body & Bullets: 14pt – 18pt (Never below 12pt).
  - Captions / Footnotes: 10pt – 12pt.
- **Strict Color Discipline:** Max 3 core colors (Primary Brand, Background/Canvas, Accent for emphasis). High contrast (WCAG AA compliant).
- **Whitespace & Margin Safety:** Maintain minimum `0.8in` (50px) margin clearance around all borders. No text or shapes overflowing the canvas.

## 2. Standard Slide Archetypes

1. **Title / Hero Slide:** Document title, subtitle/transformation, author/organization, date.
2. **Executive Problem / Friction:** 3-column card comparison showing current pain points with source citations.
3. **Framework / Architecture Diagram:** Modular flow or pyramid showing the transformation methodology.
4. **Data / Metrics Grid:** 3 to 4 large KPI callout blocks (e.g. `$4.2M`, `+185%`, `3.2x`) with concise explanatory labels.
5. **Comparison Matrix:** Side-by-side feature or scenario table with checkmarks/crosses.
6. **Execution Roadmap:** Phased horizontal timeline (Phase 1, Phase 2, Phase 3).
7. **Call-to-Action / Conclusion:** Next steps, ownership, and resource links.

## 3. Production Procedure

1. **Slide Blueprint:** Map out slide narrative in `products/<product_id>/content/slides.md`.
2. **Template Application:** Use `templates/presentations/slide-deck-spec.md` for styling and component layout.
3. **Generation:**
   - For `.pptx`: Generate using `python-pptx` with consistent slide master layout coordinates.
   - For HTML slides / PDF: Generate using Marp or styled HTML deck template.
4. **Visual & Layout Inspection:**
   - Verify slide titles do not wrap into 3+ lines.
   - Verify bullet points are concise (under 15 words per bullet).
   - Ensure diagrams have clear legends and legible labels.
   - Check contrast on dark-background slides.
