# PRODUCT BUILD & QUALITY WORKFLOW

This workflow guides execution from opportunity approval through strategy, construction, design, packaging, red-team audit, and revision loops.

---

## Stage 5: Product Strategy & Specification (GATE 2)

1. **State Update:**
   - `workflow.stage = "product_strategy"`
   - `workflow.last_completed_stage = "opportunity_selection"`
   - `workflow.next_required_action = "Formulating product specification and awaiting Human Approval Gate 2"`
2. **Worker Delegation:**
   - Launch `product-strategist` to translate approved opportunity into `products/<product_id>/specification.json` and `products/<product_id>/strategy.md` complying with `system/schemas/product.schema.json`.
   - Defines target customer, core problem, job-to-be-done, transformation (`from_state` → `to_state`), promise, unique mechanism, format rationale, modules, templates, bonuses, and quality criteria.
3. **HUMAN APPROVAL GATE 2:**
   - Master reviews specification and pauses to invoke `ask_question` for user approval of product format, promise, and scope.
   - Update `state.json` (`product.id`, `product.name`, `product.type`, `product.status = "specified"`).
   - Log decision in `memory/decisions.md`.

---

## Stage 6: Product Construction

1. **State Update:**
   - `workflow.stage = "product_build"`
   - `workflow.last_completed_stage = "product_strategy"`
   - `workflow.next_required_action = "Constructing modular product content, tools, and templates"`
2. **Worker Delegation:**
   - Launch `product-builder` following the approved sequence:
     `SPECIFICATION → CONTENT PLAN → CONTENT → STRUCTURE → TOOLS/TEMPLATES → ASSEMBLY → SELF-CHECK`.
   - Writes working files to `products/<product_id>/content/` and `products/<product_id>/assets/`.
   - Compiles final usable deliverable under `products/<product_id>/final/`.
3. **Safety & Integrity Invariants:**
   - Zero generic AI filler, fake case studies, or unverified claims.
   - All factual assertions must cite IDs in `memory/sources.csv`.
   - **Escalation Trigger:** If builder discovers a strategic contradiction or missing evidence, it must halt and escalate to Master rather than improvising.

---

## Stage 7: Design System & Visual Execution (GATE 3)

1. **State Update:**
   - `workflow.stage = "design"`
   - `workflow.last_completed_stage = "product_build"`
   - `workflow.next_required_action = "Developing visual design system and awaiting Human Approval Gate 3"`
2. **Worker Delegation:**
   - Launch `design-director` to establish `design/<product_id>/design-system.md` defining typography, spacing, color palette, component patterns, worksheets, presentation slide standards, and layout grids.
3. **HUMAN APPROVAL GATE 3:**
   - Master presents core visual direction and theme for user approval.
   - Once approved, `design-director` applies the design system to format the deliverables in `products/<product_id>/final/`.
   - Update `state.json` (`design.theme`, `design.status = "applied"`).

---

## Stage 8: Commercial Packaging

1. **State Update:**
   - `workflow.stage = "packaging"`
   - `workflow.last_completed_stage = "design"`
   - `workflow.next_required_action = "Creating truthful product packaging, mockups, and landing page copy"`
2. **Worker Delegation:**
   - Launch `packaging` agent to inspect the completed final product in `products/<product_id>/final/` and create:
     - Title treatment and cover/hero visual direction
     - Product mockups specification
     - Concise product description and benefit breakdown
     - Offer structure, bonuses, and FAQ
     - Landing page copy and call-to-action
     - Short-form promotional visual hooks
   - Writes assets into `packaging/<product_id>/`.
3. **Truthfulness Rule:**
   - Packaging claims must directly map to existing, inspected product components. No exaggerated outcomes or invented testimonials.

---

## Stage 9: Adversarial Quality Audit

1. **State Update:**
   - `workflow.stage = "audit"`
   - `workflow.last_completed_stage = "packaging"`
   - `workflow.next_required_action = "Conducting adversarial red-team audit"`
2. **Worker Delegation:**
   - Launch `critic` agent to perform an adversarial evaluation against `system/schemas/audit.schema.json`.
   - The Critic actively seeks reasons NOT to ship across: Problem-Solution Fit, Factual Accuracy, Usability, Differentiation, Design Quality, Commercial Readiness, and Distribution Compatibility.
3. **Artifacts Produced:**
   - `products/<product_id>/audit/audit.json`
   - `products/<product_id>/audit/report.md`
4. **Audit Gate Evaluation:**
   - Update `state.json` (`audit.status`, `audit.last_run`, `audit.critical_issues`, `audit.high_issues`).
   - If `critical_issues > 0` or `high_issues > 0`: Status is `FAIL`. Proceed immediately to Stage 10 (Revision Loop).
   - If `critical_issues == 0` and all `high_issues` are resolved or explicitly waived by Master with recorded justification: Status is `PASS`.

---

## Stage 10: Revision Loop (If Audit Fails)

1. **State Update:**
   - `workflow.stage = "revision"`
   - `workflow.status = "running"`
   - `workflow.next_required_action = "Remediating audit findings by assigned owners"`
2. **Remediation Routing:**
   - Master reviews findings in `audit.json` and routes each defect to its designated owner:
     - Factual / usability defects → `product-builder`
     - Visual / layout defects → `design-director`
     - Copy / claim mismatches → `packaging`
     - Structural / positioning gaps → `product-strategist`
3. **Verification:**
   - Remediation owners fix only the affected components without modifying unrelated project files.
   - Master triggers `critic` to rerun the audit.
   - Repeat until audit status is `PASS`.

---

## Stage 11: Final Product Approval (GATE 4)

1. After audit passes, Master pauses and presents the final product package for **HUMAN APPROVAL GATE 4**.
2. Upon user approval:
   - Advance to Distribution workflow (`system/workflows/distribution.md`).
