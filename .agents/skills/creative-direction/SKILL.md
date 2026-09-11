---
name: creative-direction
description: Guides the creation of distinctive, emotionally resonant, and culturally authentic product experiences, art direction, and visual worldbuilding.
---

# Creative Direction Skill

Creative Direction is the discipline of translating customer psychology, market positioning, and functional utility into a cohesive, memorable, and visually authoritative product experience.

The AI Product Factory requires that an explicit **Creative Direction** be established **BEFORE** detailed production or software coding commences.

---

## 1. The Creative Concept Formula

Every product's creative identity must be synthesized from:
$$\text{AUDIENCE} + \text{NICHE} + \text{PROBLEM} + \text{TRANSFORMATION} + \text{CREATOR CONTEXT}$$

Creative direction is not superficial styling applied at the end; it shapes the structure, language, interaction pace, visual metaphor, and emotional arc of the entire deliverable.

---

## 2. Core Operational Procedures

### Step 1: Establish Product Personality & Voice
- Define the human archetype of the product (e.g. The Seasoned Staff Engineer, The Meticulous Chief Operating Officer, The Grounded Field Specialist).
- Formulate 3 Positive Voice Attributes and 3 Negative Voice Boundaries:
  - *Example Positive:* "Direct, Mathematically Grounded, Methodical."
  - *Example Negative:* "Never hyperbolic, never playful, never hand-waving."

### Step 2: Uncover Audience Cultural Cues & Visual References
- Inspect the physical and digital environments where the customer works (e.g. CAD terminals, IDEs, Bloomberg terminals, cleanroom whiteboards, legal briefs).
- Extract genuine cultural artifacts, trusted layout archetypes, and authentic typography conventions native to that professional tribe.
- Reject tourist styling (superficial caricatures of an industry).

### Step 3: Architect the Visual Metaphor
- Anchor the product in a single, robust mental model that makes complex ideas intuitive.
- *Examples:*
  - A risk-analysis tool designed as an **Aviation Pre-Flight Checklist**.
  - A team workflow system designed as an **Industrial Conveyor Pipeline**.
  - A financial model styled with the restraint and precision of an **Architectural Blueprint**.

### Step 4: Define Art Direction & Visual Worldbuilding
In `design/<product_id>/creative-direction.md`, document the exact visual specifications:
- **Composition & Layout Grid:** Asymmetric editorial columns, precision HUD metrics, or monastic single-column reading flow (65ch measure).
- **Typographic Expression:** Font pairing that establishes gravitas:
  - Heading Display (Editorial Serif or Technical Grotesk).
  - Body Workhorse (High-legibility sans or newsprint serif).
  - Data & Code (Tabular figures monospace).
- **Color Palette & Contrast Architecture:**
  - Semantic roles: Canvas, Surface, Border, Primary Brand, and State Accents.
  - Strict WCAG AA contrast ($\ge 4.5:1$ for body, $\ge 3.0:1$ for headers).
  - High grayscale contrast: must remain 100% readable when printed in monochrome laser.
- **Image & Illustration Style:** Technical line-art, vector blueprints, duotone photography, or minimalist schematics. (Strictly prohibited: cartoon 3D clay characters, airbrushed neon gradients, and generic AI stock aesthetics).
- **Texture & Materiality:** Subtle 0.5pt hairline rules, dot-matrix guides, or clean matte surfaces. Zero heavy drop-shadows or murky glassmorphism.
- **Iconography System:** Unified stroke width (1.5pt or 2.0pt), 24x24px grid, consistent corner curvature, and semantic alignment.

### Step 5: Design the Interaction Personality & Motion
- Digital interfaces must possess a defined physical feel:
  - Snappy, instant state transitions ($< 150\text{ms}$).
  - Purposeful feedback (subtle active state depression, tactile toggle states).
  - Motion strictly reserved for communicating spatial hierarchy or layout change; zero gratuitous bouncy decorative animations.

### Step 6: Engineer the Perceived Value Strategy
- Craftsmanship signals that elevate perceived worth:
  - Zero typo tolerance, zero widowed lines, zero overflowing table cells.
  - Realistic, rich example data pre-populated.
  - Tangible structural weight: bordered frames, clear section tabs, and verified checksums.

---

## 3. Creative Direction Deliverable Contract

Before `product-builder` or `software-builder` begins work, verify that `products/<product_id>/creative-concept.md` and `design/<product_id>/creative-direction.md` are approved by the Creative Director and satisfy all quality standards.
