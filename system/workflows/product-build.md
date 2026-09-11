# PRODUCT BUILD & QUALITY WORKFLOW

This workflow guides execution from opportunity approval through product strategy, modality decision, technical architecture, software and artifact construction, design, modality-specific QA, packaging, red-team audit, release engineering, pre-ship verification, and revision loops.

> **CORE INVARIANTS:**
> 1. Never assume the solution is a document. Dynamically select the appropriate agent routing based on the required customer transformation.
> 2. The Master INVOKES agents using `invoke_subagent`. The Master does not produce worker outputs itself.
> 3. Every agent invocation must be recorded in the delegation log with artifact verification status.

---

## Stage 4: Product Strategy & Modality Decision (GATE 2)

### State Update
```json
{
  "workflow.stage": "product_strategy",
  "workflow.last_completed_stage": "opportunity_selection",
  "workflow.next_required_action": "Invoking product-strategist; then awaiting Human Approval Gate 2"
}
```

### Required Agent Invocation

| Agent | Task | Required Artifacts | Dependency |
|---|---|---|---|
| `product-strategist` (**REQUIRED**) | Translate approved opportunity into product specification and positioning | `products/<product_id>/specification.json` (conforming to `system/schemas/product.schema.json`) | Approved opportunity ID in state.json |

**Skill references to pass:** `system/product-types.md`, `system/quality-checklists.md`, `system/scoring.md`

### Invocation Protocol
```
INVOKE product-strategist
  PASS: approved opportunity ID, pain-clusters.md, competitive-analysis.md, source-audit.md
  PASS: system/product-types.md, system/quality-checklists.md
  PASS: modality comparison requirement (simplest / best CX / higher complexity)
  → WAIT for response
  → VERIFY: products/<product_id>/specification.json exists and non-empty
  → VALIDATE: specification.json against system/schemas/product.schema.json
  → Record invocation in delegation log
```

### HUMAN APPROVAL GATE 2 (MANDATORY — DO NOT BYPASS)
```
PRESENT: specification.json via ask_question
  Show: product modality, core promise, transformation scope, pricing tier estimate
INVOKE ask_question → Human approves before construction
RECORD: state.json (product.id, product.name, product.type, product.modality, status = "specified")
→ Do NOT begin construction without explicit human approval
```

---

## Stage 5: Technical Architecture (When Required)

**Applicability:** Software, web, mobile, desktop, interactive tools, APIs, databases, automations, and hybrids. Skip for validated simple documents or spreadsheets.

### State Update
```json
{
  "workflow.stage": "architecture",
  "architecture.status": "in_progress"
}
```

### Required Agent Invocation (CONDITIONAL)

| Agent | Task | Required Artifacts | Condition |
|---|---|---|---|
| `solution-architect` (**REQUIRED** for software/hybrid) | Define system topology, data schemas, API endpoints, auth, and security baseline | `products/<product_id>/architecture.md` | Only when modality is software, web, mobile, API, database, or hybrid |

### Invocation Protocol
```
IF modality requires architecture:
  INVOKE solution-architect
    PASS: specification.json, product.id, relevant skill (api-development, database-engineering, web-app-development, or mobile-app-development)
    → WAIT for response
    → VERIFY: products/<product_id>/architecture.md exists and non-empty
    → Record invocation in delegation log
    → UPDATE: state.json (architecture.status = "complete")
ELSE:
    UPDATE: state.json (architecture.status = "not_applicable")
```

---

## Stage 6: Creative Concept & Signature Mechanism

### State Update
```json
{
  "workflow.stage": "creative_concept"
}
```

### Required Agent Invocation

| Agent | Task | Required Artifacts | Dependency |
|---|---|---|---|
| `creative-director` (**REQUIRED**) | Define product personality, visual metaphor, emotional arc, signature mechanism, and customer wow moments | `products/<product_id>/creative-concept.md` | specification.json must exist |

**Skill references to pass:** `system/creative-product-concept.md`, `system/customer-wow.md`, `.agents/skills/creative-direction/`

### Invocation Protocol
```
INVOKE creative-director
  PASS: specification.json, system/creative-product-concept.md, system/customer-wow.md
  PASS: .agents/skills/creative-direction/SKILL.md
  → WAIT for response
  → VERIFY: products/<product_id>/creative-concept.md exists and non-empty
  → VERIFY: creative-concept.md contains signature mechanism specification
  → VALIDATE: no generic AI clichés or ungrounded claims detected
  → Record invocation in delegation log
  → UPDATE: state.json (creative_concept.status = "completed")
```

---

## Stage 7: Design System (GATE 3)

### State Update
```json
{
  "workflow.stage": "design"
}
```

### Required Agent Invocation

| Agent | Task | Required Artifacts | Dependency |
|---|---|---|---|
| `design-director` (**REQUIRED**) | Establish typography, 8px/4px grid, color tokens, button states, WCAG AA contrast, and component rules | `design/<product_id>/design-system.md` | creative-concept.md must exist |

**Skill references to pass:** `.agents/skills/ui-ux-design/`, `.agents/skills/editorial-design/`, `.agents/skills/workbook-planner-design/` (as applicable)

### Invocation Protocol
```
INVOKE design-director
  PASS: creative-concept.md, specification.json, relevant design skill(s)
  PROHIBIT: generic neon gradients, glassmorphism, random cards, excessive shadows
  → WAIT for response
  → VERIFY: design/<product_id>/design-system.md exists and non-empty
  → Record invocation in delegation log
```

### HUMAN APPROVAL GATE 3 (MANDATORY — DO NOT BYPASS)
```
PRESENT: design-system.md via ask_question
  Show: visual theme, palette, typography, layout rules, component decisions
INVOKE ask_question → Human approves before full asset production
RECORD: state.json (design.theme, design.status = "approved")
→ Do NOT begin asset generation without explicit human approval
```

---

## Stage 8: Asset Pipeline

### State Update
```json
{
  "workflow.stage": "asset_pipeline"
}
```

### Required Agent Invocation

| Agent | Task | Required Artifacts | Dependency |
|---|---|---|---|
| `asset-director` (**REQUIRED**) | Plan, generate, rights-check, and catalog all visual assets per design system | `products/<product_id>/assets/asset-manifest.json` | design-system.md must be approved |

**Skill references to pass:** `.agents/skills/asset-generation/SKILL.md`, `system/image-asset-pipeline.md`

### Invocation Protocol
```
INVOKE asset-director
  PASS: design-system.md, creative-concept.md, .agents/skills/asset-generation/SKILL.md
  REQUIRE: 17-point asset catalog records in asset-manifest.json
  REQUIRE: verified commercial licensing for every asset
  → WAIT for response
  → VERIFY: products/<product_id>/assets/asset-manifest.json exists and non-empty
  → VERIFY: asset licensing fields are populated (not null)
  → Record invocation in delegation log
  → UPDATE: state.json (asset_pipeline.status = "completed")
```

---

## Stage 9: Product Construction & Build

### State Update
```json
{
  "workflow.stage": "product_build",
  "workflow.next_required_action": "Executing modality-directed build with skill-first and template-first approach"
}
```

### Skill-First & Template-First Mandate
```
BEFORE INVOKING any builder:
  1. Inspect .agents/skills/ for the relevant modality skill
  2. Inspect templates/ for starter layouts and schemas
  3. Inspect system/scripts/ for required build scripts
  4. Pass these explicitly to the builder agent
```

### Dynamic Build Routing (select based on approved modality)

**DOCUMENTS & WORKBOOKS:**
```
INVOKE product-builder
  PASS: specification.json, creative-concept.md, design-system.md
  PASS: .agents/skills/premium-document-production/SKILL.md (or workbook-planner-design/)
  PASS: templates/documents/ or templates/workbooks/
  REQUIRED ARTIFACT: products/<product_id>/content/ (populated with modules)
  → WAIT → VERIFY content/ exists with non-empty files → Record → Advance

INVOKE artifact-builder
  PASS: products/<product_id>/content/, design-system.md, asset-manifest.json
  PASS: .agents/skills/pdf-publishing/SKILL.md, system/scripts/document_builder.py
  REQUIRED ARTIFACT: products/<product_id>/deliverables/ (PDF + HTML)
  → WAIT → VERIFY deliverables exist and are non-empty → Record → Advance
```

**SPREADSHEETS & FINANCIAL MODELS:**
```
INVOKE product-builder → artifact-builder
  PASS: .agents/skills/spreadsheet-engineering/SKILL.md
  PASS: system/scripts/spreadsheet_builder.py
  REQUIRED ARTIFACT: products/<product_id>/deliverables/*.xlsx
```

**SOFTWARE / WEB / MOBILE / API / DATABASE:**
```
INVOKE software-builder
  PASS: architecture.md, specification.json, design-system.md
  PASS: relevant skill (.agents/skills/web-app-development/, mobile-app-development/, api-development/, database-engineering/)
  PASS: templates/<modality>/
  REQUIRED ARTIFACT: products/<product_id>/software/ (runnable source code)
  → WAIT → VERIFY source code exists → RUN verification command → Record → Advance
```

**HYBRID:**
```
IDENTIFY independent components (no shared output files)
INVOKE software-builder AND artifact-builder simultaneously (parallel)
  → WAIT for both to complete
  → VERIFY both required artifacts exist
  → INTEGRATE components
  → Record both invocations in delegation log
```

### Build Parallelization
Independent content modules or software microservices may be built concurrently. Do not allow concurrent writes to the same shared output file. Coordinate via explicit task assignment in invocation prompts.

---

## Stage 10: Quality Assurance

### State Update
```json
{
  "workflow.stage": "qa"
}
```

### Required Agent Invocations (PARALLEL where applicable)

| Agent | Task | Required Artifacts | Applies To |
|---|---|---|---|
| `artifact-qa` (**REQUIRED** for doc/hybrid) | Inspect physical files via `system/scripts/artifact_inspector.py`: formatting, page breaks, zero placeholders, formula errors | `products/<product_id>/audit/artifact-qa.json` | Documents, workbooks, hybrid |
| `software-qa` (**REQUIRED** for software/hybrid) | Execute 12-Step Software Testing Protocol, run `link_checker.py`, `ui_test_runner.py`, check responsive viewports 375px/768px/1280px | `products/<product_id>/audit/software-qa.json` | Software, web, mobile, hybrid |
| `taste-reviewer` (**REQUIRED** — all products) | Independent aesthetic evaluation: visual restraint, editorial maturity, niche authenticity, anti-AI-slop | `products/<product_id>/audit/taste-review.md` | ALL products |

**Parallelization:** Invoke all applicable QA agents simultaneously on the frozen build output.

### Invocation Protocol
```
INVOKE artifact-qa (if applicable) + software-qa (if applicable) + taste-reviewer (always)
  PASS to artifact-qa: deliverables path, system/scripts/artifact_inspector.py
  PASS to software-qa: software path, system/scripts/link_checker.py, ui_test_runner.py
  PASS to taste-reviewer: .agents/skills/taste-review/SKILL.md, product deliverables
  → WAIT for all to complete
  → VERIFY each required artifact-qa.json, software-qa.json, taste-review.md exists
  → READ each result
  → UPDATE state.json (qa fields)
  → Record all invocations in delegation log
```

### QA Gating Rule
```
IF artifact_qa_status = "FAIL" OR software_qa_status = "FAIL":
  Proceed to Revision Loop (Stage 11)
  Do NOT advance to Packaging
IF taste_review_status = "FAIL":
  Proceed to Revision Loop (Stage 11)
  Do NOT advance to Packaging
IF critical_issues > 0:
  Proceed to Revision Loop (Stage 11)
```

---

## Stage 11: Revision Loop

```text
BUILD → QA → FAIL → REVISE → QA AGAIN → PASS
```

### Routing
```
Master routes each defect to the designated owner:
  Design defects → design-director
  Content defects → product-builder
  Code defects → software-builder
  File/format defects → artifact-builder
  Packaging defects → packaging

INVOKE designated owner with specific defect list
  → WAIT for fix
  → RE-INVOKE QA agents on fixed output
  → VERIFY QA now passes
  → Record all re-invocations in delegation log
```

**Never hide failed tests or declare PASS prematurely.**

---

## Stage 12: Commercial Packaging & Merchandising

### State Update
```json
{
  "workflow.stage": "packaging"
}
```

### Required Agent Invocations (may parallelize with audit prep)

| Agent | Task | Required Artifacts | Dependency |
|---|---|---|---|
| `packaging` (**REQUIRED**) | Inspect finished deliverables; produce truthful landing page, offer structure, creator one-sheet | `packaging/<product_id>/landing-page.md` | QA must have passed |
| `marketing-strategist` (**REQUIRED**) | Ethical customer psychology, offer architecture, merchandising | `products/<product_id>/merchandising.json` | specification.json must exist |

### Invocation Protocol
```
INVOKE packaging AND marketing-strategist (simultaneously)
  PASS to packaging: actual finished deliverables, specification.json, creative-concept.md
  PASS to marketing-strategist: .agents/skills/creative-marketing/SKILL.md, customer psychology skill
  → WAIT for both
  → VERIFY landing-page.md exists and contains ZERO fabricated capabilities
  → VERIFY merchandising.json exists and conforms to system/schemas (if applicable)
  → Record both invocations in delegation log
```

---

## Stage 13: Red-Team Audit

### State Update
```json
{
  "workflow.stage": "audit"
}
```

### Required Agent Invocation

| Agent | Task | Required Artifacts | Dependency |
|---|---|---|---|
| `critic` (**REQUIRED**) | Adversarial red-team: "Why should a customer NOT buy this?" Verify evidence in sources.csv, check against quality-checklists.md | `products/<product_id>/audit/audit.json` (conforming to `system/schemas/audit.schema.json`) | QA passed, packaging complete |

### Invocation Protocol
```
INVOKE critic
  PASS: all deliverables, specification.json, sources.csv, merchandising.json, quality-checklists.md
  PASS: .agents/skills/ relevant skills
  → WAIT for response
  → VERIFY: audit.json exists and conforms to schema
  → READ: critical_issues count, high_issues count
  → IF critical_issues > 0 OR un-waived high_issues > 0:
      UPDATE state.json (audit.status = "FAIL")
      Route to Revision Loop (Stage 11)
  → ELSE:
      UPDATE state.json (audit.status = "PASS")
  → Record invocation in delegation log
```

---

## Stage 14: Release Bundle Assembly

### State Update
```json
{
  "workflow.stage": "release"
}
```

### Required Agent Invocation

| Agent | Task | Required Artifacts | Dependency |
|---|---|---|---|
| `release-engineer` (**REQUIRED**) | Assemble release archive, delivery manifest with file hashes, installation guide | `products/<product_id>/manifest.json` | Audit PASS required |

**Scripts to pass:** `system/scripts/archive_builder.py`

### Invocation Protocol
```
INVOKE release-engineer
  PASS: all verified deliverables, audit.json, specification.json
  PASS: system/scripts/archive_builder.py, .agents/skills/release-packaging/SKILL.md
  → WAIT for response
  → VERIFY: products/<product_id>/manifest.json exists
  → VERIFY: ZIP archive or equivalent bundle exists with file hashes
  → Record invocation in delegation log
```

---

## Stage 15: Pre-Ship Verification & Human Gate 4

### Master Pre-Ship Checklist
```
Master verifies ALL items from system/pre-ship-checklist.md before Gate 4.
This is a Master-level integration review — not a worker task.
```

### HUMAN APPROVAL GATE 4 (MANDATORY — DO NOT BYPASS)
```
PRESENT via ask_question:
  - Final deliverables list with file sizes
  - Delivery manifest path
  - Critic audit report (0 critical, 0 high issues)
  - Creator outreach brief
  - QA status summary
INVOKE ask_question → Human gives final sign-off
RECORD: state.json (product.production_readiness = "PRODUCTION_READY")
→ Do NOT deploy or distribute without explicit human approval
```

---

*Workflow version: 0.3.0 — Updated 2026-09-11: Replaced all vague "launch/ask/have" instructions with explicit INVOKE → WAIT → VERIFY → INTEGRATE → UPDATE protocols. Added dependency mapping, skill references, build routing tables, parallel invocation specification, and delegation log recording requirements. Distinguished REQUIRED from OPTIONAL agents.*
