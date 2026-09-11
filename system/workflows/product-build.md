# PRODUCT BUILD & QUALITY WORKFLOW

This workflow guides execution from opportunity approval through product strategy, modality decision, technical architecture, software and artifact construction, design, modality-specific QA, packaging, red-team audit, release engineering, pre-ship verification, and revision loops.

> **CORE INVARIANT:** Never assume the solution is a document. Dynamically select the appropriate agent routing based on the required customer transformation.

---

## Stage 5: Product Strategy & Modality Decision (GATE 2)

1. **State Update:**
   - `workflow.stage = "product_strategy"`
   - `workflow.last_completed_stage = "opportunity_selection"`
   - `workflow.next_required_action = "Formulating product specification, evaluating modality tradeoffs, and awaiting Human Approval Gate 2"`
2. **Worker Delegation:**
   - Launch `product-strategist` to translate approved opportunity into `products/<product_id>/specification.json` (complying with `system/schemas/product.schema.json`) and `products/<product_id>/strategy.md`.
   - **Modality Comparison Required:** Explicitly compare (1) Simplest Valid Solution, (2) Best CX Solution, and (3) Higher-Complexity Solution.
   - Reference `system/quality-checklists.md` for target modality standards.
3. **HUMAN APPROVAL GATE 2:**
   - Master presents specification via `ask_question` for user approval of product modality, core promise, and transformation scope.
   - Update `state.json` (`product.id`, `product.name`, `product.type`, `product.modality`, `product.status = "specified"`).

---

## Stage 6: Technical Architecture (When Required)

1. **Applicability:** Executed for software, web, mobile, desktop, interactive tools, APIs, databases, automations, and hybrids. Skipped for validated simple documents or spreadsheets.
2. **State Update:**
   - `workflow.stage = "architecture"`
   - `architecture.status = "in_progress"`
3. **Worker Delegation:**
   - Launch `solution-architect` to produce `products/<product_id>/architecture.md` and `architecture.json`.
   - Defines system topology, frontend reactivity, data schemas, API endpoints, authentication, and security baseline.
   - Update `architecture.status = "complete"`.

---

## Stage 7: Product Construction & Build

1. **State Update:**
   - `workflow.stage = "product_build"`
   - `workflow.last_completed_stage = "architecture"`
   - `workflow.next_required_action = "Executing skill-first and template-first modality-directed build"`
2. **Skill-First & Template-First Mandate:**
   - Inspect `.agents/skills/` for relevant modality skills.
   - Inspect `templates/` for starter projects, schemas, and layouts.
3. **Dynamic Build Routing:**
   - **Documents & Workbooks:** `product-builder` (content in `products/<id>/content/`) &rarr; `artifact-builder` (compiles via `system/scripts/document_builder.py` to `products/<id>/final/` & `artifact-manifest.json`).
   - **Spreadsheets & Financial Models:** `product-builder` &rarr; `artifact-builder` (compiles via `system/scripts/spreadsheet_builder.py` to `.xlsx` / `.csv`).
   - **Software, Web, Mobile, API, Database:** `software-builder` (source in `products/<id>/software/`, verified via `run_command`).
   - **Hybrid:** Coordinated parallel builds across `software-builder` and `artifact-builder`.

---

## Stage 8: Design System (GATE 3)

1. **State Update:** `workflow.stage = "design"`
2. **Worker Delegation:**
   - Launch `design-director` to establish `design/<product_id>/design-system.md` (typography, 8px/4px grid, color tokens, button states, WCAG AA contrast).
   - Prohibit generic neon gradients, glassmorphism, random cards, and excessive shadows.
3. **HUMAN APPROVAL GATE 3:**
   - Master presents design direction via `ask_question`. User approves visual theme, components, and typography.
   - Update `state.json` (`design.theme`, `design.status = "approved"`).

---

## Stage 9: Commercial Packaging & Release Preparation

1. **State Update:** `workflow.stage = "packaging"`
2. **Packaging Agent:**
   - Inspects actual finished deliverables.
   - Produces truthful landing page copy (`packaging/<id>/landing-page.md`), offer structure (`offer-structure.md`), and creator one-sheet (`creator-brief.md`).
3. **Release Engineer:**
   - Assembles release archive (`release/<id>-v<version>.zip`) via `system/scripts/archive_builder.py`.
   - Generates `delivery-manifest.json` with file hashes and sizes.
   - Evaluates production readiness state in `state.json`.

---

## Stage 10: Adversarial Quality Audit (Red Team)

1. **State Update:** `workflow.stage = "audit"`
2. **Modality-Specific Verification:**
   - `artifact-qa`: Inspects physical files via `system/scripts/artifact_inspector.py`. Checks formatting, page breaks, zero placeholders, and formula errors (`#REF!`). (`artifact-qa.json`).
   - `software-qa`: Executes the 12-Step Software Testing Protocol, runs `link_checker.py`, runs `ui_test_runner.py`, and checks responsive viewports (375px/768px/1280px). (`software-qa.json`).
   - `critic`: Adversarial red-team audit answering: "Why should a customer NOT buy this?" Checks evidence in `memory/sources.csv` and verifies against `system/quality-checklists.md`. (`audit.json`).
3. **Audit Gating Rule:**
   - If `critical_issues > 0` or any un-waived `high_issues > 0`, audit status is `FAIL`. Proceed immediately to Revision Loop.

---

## Stage 11: Revision Loop

```text
BUILD → TEST → REVIEW → FIX → TEST AGAIN → REVIEW AGAIN → PASS
```
1. Master routes defects to designated owners (`product-builder`, `software-builder`, `artifact-builder`, `design-director`, `packaging`, `release-engineer`).
2. Fixes must be re-tested with actual verification commands. Never hide failed tests or declare PASS prematurely.
3. Once all defects are resolved, re-run QA and Critic audit.

---

## Stage 12: Final Pre-Ship Check & Human Gate 4

1. **Pre-Ship Verification:**
   - Master verifies 100% completion of `system/pre-ship-checklist.md`.
2. **HUMAN APPROVAL GATE 4:**
   - Master presents verified deliverables, delivery manifest, critic audit report, and creator outreach brief via `ask_question`.
   - User grants final sign-off for release and distribution.
3. **State Update:**
   - `workflow.stage = "distribution"` (or `complete`)
   - `product.production_readiness = "PRODUCTION_READY"`
