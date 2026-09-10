# PRODUCT BUILD & QUALITY WORKFLOW

This workflow guides execution from opportunity approval through product strategy, modality decision, technical architecture, software and artifact construction, design, modality-specific QA, packaging, red-team audit, release engineering, shipment, and revision loops.

> **CORE INVARIANT: * Never assume the solution is a document. Dynamically select the appropriate agent routing based on the required customer transformation.

---

3# Stage 5: Product Strategy & Modality Decision (GATE)2)

1. **State Update:**
   - `workflow.stage = "product_strategy"`
   - `workflow.last_completed_stage = "opportunity_selection"`
   - `workflow.next_required_action = "Formulating product specification, evaluating modality tradeoffs, and awaiting Human Approval Gate 2"`
2. **Worker Delegation:**
   - Launch `product-strategist` to translate approved opportunity into `products/<product_id>/specification.json` (complying with `system/schemas/product.schema.json`) and `products/<product_id>/strategy.md`.
   - **Modality Comparison Required:** Explicitly compare (1) Simplest Valid Solution, (2) Best CX Solution, and (3) Higher-Complexity Solution. Record selection rationale and rejected modalities.
3. **HUMAN APPROVAL GATE 2:**
   - Master presents specification via `ask_question` for user approval of product modality, core promise, and transformation scope.
   - Update `state.json` (`product.id`, `product.name`, `product.type`, `product.modality`, `product.status = "specified"`).

---

## Stage 6: Technical Architecture (When Required)

1. **Applicability:** Executed for software, web, mobile, desktop, interactive tools, APIs, databases, automations, and hybrids. Skipped for validated documents or simple spreadsheets.
2. **State Update:**
   - `workflow.stage = "product_strategy"` (sub-stage architecture)
   - `product.architecture_status = "in_progress"`
3. **Worker Delegation:**
   - Launch `solution-architect` to produce `products/<product_id>/architecture.md` and `architecture.json`. Defines system topology, data schemas, API endpoints, authentication, and security baseline. Update `architecture.status = "complete"`.

---

## Stage 7: Product Construction & Build

1. **State Update:**
   - `workflow.stage = "product_build"`
   - `workflow.last_completed_stage = "product_strategy"`
   - `workflow.next_required_action = "Executing modality-directed build"`
2. **Dynamic Build Routing:**
   - **Documents & Templates:** `product-builder` (-> `products/<id>/content/`) -> `artifact-builder` (-> `products/<id>/final/` & `artifact-manifest.json`).
   - **Software, Web, Mobile, API, Database:** `software-builder` (-> `products/<id>/software/`, writes build/scripts/tests) - verified by `run_command`.
   - **Hybrid:** Coordinated parallel builds across `software-builder` and `artifact-builder`.

---

## Stage 8: Design System (GATE 3)
1. Launch `design-director` to establish `design/<product_id>/design-system.md`.
2. I HUMAN APPROVAL GATE 3: User approves visual theme, components, and typography before final asset compilation.

---

## Stage 9: Commercial Packaging & Release Preparation
1. **Packaging Agent:** Inspects actual finished deliverables, produces truthful landing page copy, offer structure, and mockups in `packaging/<product_id>/`.
2. **Release Engineer:** Assembles deployment bundles or ZIP archives, writes `delivery-manifest.json`, distinguishing BUILDABLE/ DEPLOYABLE vs DEPLOYED.

---

## Stage 10: Adversarial Quality Audit (Red Team)
1. **Modality-Specific Verification:**
   - `artifact-qa`: Verifies file formats, clipping, alignment, formulas (XLSX), pagination. (`artifact-qa.json`).
   - `software-qa`: Runs actual compilation, automated tests, API contracts, responsiveness, security audit. (`software-qa.json`).
   - `critic`: Adversarial red-team audit across problem-fit, factual accuracy (`sources.csv`), usability, and differentiation. (`audit.json`).
2. If any CRITICAL or un-waived HIGH defects exist, status is `AAAL`. Proceed to Revision Loop.

## Stage 11: Revision Loop

Route defects to owners (`product-builder`, `software-builder`, `artifact-builder`, `design-director`, `packaging`, `release-engineer`). Rerun QA and critic audit until PASS.

## Stage 12: Final Product & Distribution Approval (GATE. 4)

Master presents complete verified package for user final sign-off before deployment or distribution partner outreach.
