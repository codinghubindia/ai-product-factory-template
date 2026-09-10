# DISTRIBUTION & COMPLETION WORKFLOW

This workflow guides the preparation of targeted creator distribution partnerships and the final definition of done.

---

## Stage 12: Distribution Strategy & Creator Partnerships

1. **State Update:**
   - `workflow.stage = "distribution"`
   - `workflow.last_completed_stage = "audit"`
   - `workflow.status = "running"`
   - `workflow.next_required_action = "Analyzing creator fit and generating collaboration outreach assets"`
2. **Inputs Read:**
   - Final product deliverables in `products/<product_id>/final/`
   - Customer profile in `memory/customers.json`
   - Approved packaging assets in `packaging/<product_id>/`
   - Passed audit report in `products/<product_id>/audit/report.md`
3. **Worker Delegation:**
   - Launch `distribution` agent to discover and vet creator collaboration channels.
   - **Vetting Criteria:**
     - Audience problem alignment (does their audience actively experience this pain?)
     - Content format compatibility (tutorials, teardowns, workflow tours, short-form tips)
     - Product demonstration feasibility (can the transformation be visually demonstrated in <60 seconds?)
     - Creator credibility and trust in the target domain
     - Commercial compatibility (history of relevant tools or digital products)
     - **Strict Invariant:** Do not rank creators purely by follower count. Zero tolerance for fabricated email addresses, engagement statistics, or past sponsorship claims.
4. **Artifacts Produced:**
   - `distribution/<product_id>/creator-shortlist.md` (ranked candidates with evidence-backed rationale)
   - `distribution/<product_id>/outreach/` containing tailored collaboration packs for top candidates:
     - Specific collaboration angle and personalized hook
     - Concise value proposition for the creator's audience
     - 3 concrete short-form content ideas / demonstration scripts
     - Suggested call-to-action (CTA) and lead magnet
     - Proposed commercial structure (affiliate rev-share, upfront sponsorship hypothesis, or co-branded bonus)
5. **Master Review:**
   - Master reviews creator alignment and collaboration packs for realism and brand consistency.
   - Update `state.json` (`distribution.status = "ready"`).

---

## Stage 13: Factory Completion (Definition of Done)

1. **State Update:**
   - `workflow.stage = "complete"`
   - `workflow.last_completed_stage = "distribution"`
   - `workflow.status = "complete"`
   - `workflow.next_required_action = "Project fully completed; ready for market launch or new project"`
   - `workflow.current_blocking_issue = null`
2. **Final Verification Checklist:**
   - [x] Product specification fully satisfied (`products/<product_id>/specification.json`)
   - [x] High-utility, usable final deliverables assembled (`products/<product_id>/final/`)
   - [x] All claims backed by audited evidence in `memory/sources.csv`
   - [x] Cohesive design system applied (`design/<product_id>/design-system.md`)
   - [x] Truthful packaging and landing page assets ready (`packaging/<product_id>/`)
   - [x] Critic audit passed with 0 critical defects (`products/<product_id>/audit/audit.json`)
   - [x] Creator outreach materials generated (`distribution/<product_id>/`)
   - [x] Project state (`state.json`) and decision log (`memory/decisions.md`) up to date
