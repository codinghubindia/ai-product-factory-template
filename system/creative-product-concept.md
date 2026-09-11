# AI PRODUCT FACTORY — CREATIVE PRODUCT CONCEPT STAGE

The **Creative Product Concept** stage sits directly between **Product Strategy** and **Design / Build**.

```text
PRODUCT STRATEGY
  → CREATIVE PRODUCT CONCEPT
  → PRODUCT MODALITY & ARCHITECTURE
  → DESIGN & ASSET GENERATION
  → BUILD
```

Strategy defines *what* is being built, for *whom*, and *why* it solves commercial pain.  
The **Creative Product Concept** defines *how the product feels, speaks, resonates, and lodges itself permanently in the customer's mind*.

Without this stage, the factory falls into the trap of technical competence without soul—producing functionally adequate products that look like generic, disposable AI output.

---

## 1. The Creative Concept Formula

The creative concept must never be invented in a vacuum or chosen because a visual trend is popular on social media. It must be strictly derived from:

$$\text{AUDIENCE} + \text{NICHE} + \text{PROBLEM} + \text{TRANSFORMATION} + \text{CREATOR CONTEXT}$$

### Prohibited Creative Shortcuts
- **Strictly Prohibited:** Adopting a visual style merely because it is trendy (e.g. gratuitous brutalism, dark-mode cyberpunk, pastel neomorphism).
- **Strictly Prohibited:** Copying a competitor or partner creator's exact visual identity, brand mark, or naming conventions.
- **Strictly Prohibited:** Superficial cosmetic decoration that does not serve customer utility, trust, or comprehension.

---

## 2. The Twelve Core Dimensions of Creative Direction

Every product must document its creative concept in `products/<product_id>/creative-concept.md` across twelve explicit dimensions:

### 1. Product Personality
The human archetype and behavioral persona embodied by the product.  
*Archetype examples:* The Dispassionate Chief Risk Officer; The Relentless Precision Machinist; The Calm, Methodical Senior Architect; The Grounded Field Veteran.  
*Tone Attributes:* Define 3 primary tone adjectives and 3 anti-tone adjectives (e.g. "Authoritative, Rigorous, Reassuring" — NOT "Playful, Hype-driven, Verbose").

### 2. Emotional Direction & Arc
The emotional progression of the customer through their product lifecycle:
- **Arrival Emotion:** What the user feels upon landing (e.g. relief that their chaos is recognized; confidence that an adult is in the room).
- **In-Work Emotion:** What the user feels during core usage (e.g. calm mastery, focused clarity, momentum).
- **Completion Emotion:** What the user feels upon achieving the transformation (e.g. bulletproof readiness, genuine professional pride).

### 3. Audience Identity & Cultural Codes
The cultural vernacular, professional rituals, status symbols, and implicit values of the target audience.
- What jargon is authentic vs. what sounds like outsider corporate posturing?
- What does "premium" mean to this specific customer? (e.g. to a quantitative developer, premium means clean terminal output, zero UI bloat, and fast keybindings; to an executive, premium means crisp editorial spacing, clear summaries, and 65ch line lengths).

### 4. Visual Metaphor
A unifying physical or conceptual mental model that anchors all illustrations, diagrams, and UI interactions.
- *Examples:* The Flight Deck; The Structural Load-Bearing Blueprint; The Cleanroom Pipeline; The Command Console.
- The metaphor dictates how states are represented (e.g. warning lights vs. structural stress fractures).

### 5. Narrative Concept & Origin Story
The philosophical premise of the product:
- What orthodoxy in the industry does this product reject?
- What contrarian truth does it defend?
- Why was this tool inevitable given the shift in customer reality?

### 6. Signature Mechanism
The branded, proprietary intellectual framework or internal operating engine that delivers the transformation (see Section 3).

### 7. Memorable Terminology & Product Lexicon
A disciplined vocabulary unique to the product. Replace generic industry terms with crisp, evocative proprietary names:
- Instead of "Settings" $\rightarrow$ "Runtime Parameters"
- Instead of "Dashboard" $\rightarrow$ "Triage Deck"
- Instead of "Action Plan" $\rightarrow$ "72-Hour Remediation Cadence"

### 8. Product Ritual & Onboarding Gateway
The ceremonial first action that marks the customer's transition from passive observer to active practitioner.
- *Examples:* Completing the 2-minute diagnostic benchmark; generating their baseline friction score; signing the implementation commitment nameplate.

### 9. Perceived Value Strategy
The tangible, sensory, and structural signals that make the customer recognize high craftsmanship:
- Typographic discipline (custom font pairing, perfect leading, zero widows).
- Physicality and weight (subtle bordered frames, tactile toggle buttons, print-ready binding gutters).
- Deep domain completeness (thoughtful edge-case handling, pre-populated realistic datasets).

### 10. Commercial Differentiation
The unmistakable wedge that separates this product from alternatives:
- "Competitor A gives you 400 blank Notion pages; we give you a 14-day deterministic decision tree."
- "Competitor B gives you a 10-hour lecture course; we give you a 60-second interactive diagnostic engine."

### 11. Visual World & Aesthetic Universe
The unified rules governing palette, typography, texture, lighting, framing, and iconography:
- Color palette mapped to semantic utility (Primary Brand, Canvas, Surface, Border, Status Accents).
- Layout architecture (monastic white space, high-density HUD, or publication editorial).
- Image & illustration treatment rules (vector blueprints, duotone photography, or minimalist schematics).

### 12. Creator-Content Compatibility
How the product naturally performs on screen in creator media:
- Can the transformation be demonstrated in under 60 seconds?
- Is there a high-contrast visual payoff (a chart updating live, a scorecard calculating instantly, a clean worksheet printout)?
- Does the creator look smart, credible, and helpful by showcasing it?

---

## 3. The Signature Mechanism Rule

Every approved product must engineer and document a **Signature Mechanism**.

A product without a mechanism is just a commodity file. A product with a signature mechanism is an authoritative methodology.

### Canonical Mechanism Types
1. **The Diagnostic Engine:** Quantifies an invisible bottleneck into a concrete numerical baseline (e.g. *The Pipeline Drag Index*).
2. **The Scoring Rubric:** A multi-axis evaluation matrix establishing objective maturity tiers.
3. **The Transformation Ladder:** A sequential stage-gate methodology moving the user from vulnerability to resilience.
4. **The Decision Matrix:** A deterministic logic tree eliminating cognitive choice fatigue during high-stress workflows.
5. **The Operating Cadence:** A synchronized time-blocked ritual for daily, weekly, or sprint execution.
6. **The Root-Cause Sieve:** A systematic elimination protocol isolating the true constraint.

### Documentation Requirements
In `products/<product_id>/creative-concept.md`:
- **Mechanism Name:** Distinctive, evocative, trademarkable.
- **Mechanism Purpose:** The exact friction it resolves.
- **How It Works:** Step-by-step logic, calculations, or progression.
- **Why It Is Different:** Contrast against generic competitor advice.
- **Customer Transformation:** The measurable difference in outcome.
- **Creator Demonstration:** The 30-to-60 second visual showcase.

---

## 4. Gate Verification

Before transitioning from `creative_concept` to `architecture` or `build`:
- [ ] Creative concept document exists at `products/<product_id>/creative-concept.md`.
- [ ] Creative Director and Product Strategist sign off.
- [ ] Signature mechanism is fully specified and demonstrable.
- [ ] Visual world tokens are passed to `design-system.md`.
- [ ] Zero generic AI clichés, neon gradients, or ungrounded claims detected.
