# AI PRODUCT FACTORY — CANONICAL AGENT MAP

**Version:** 0.3.0  
**Status:** Authoritative reference. All workflow documentation and the Master agent must align to this map.

> **Core Principle:** The Master is an orchestrator. The Master does NOT perform a worker's primary task when a responsible specialist exists. Every stage must show real invocation evidence in the delegation log.

---

## THE MASTER ORCHESTRATOR

**Agent file:** `.agents/agents/master/agent.md`

**Permitted Master actions:**
- Understand requirements and plan stage execution
- Select which agents to invoke (and whether to parallelize)
- Invoke specialist agents via `invoke_subagent`
- Coordinate and sequence dependent work
- Read and evaluate worker outputs critically
- Verify required artifacts exist and conform to schema
- Identify contradictions across worker outputs and resolve them
- Integrate results into coherent state
- Update `state.json` and `memory/decisions.md`
- Enforce human approval gates via `ask_question`
- Perform final cross-cutting review (not replacing specialist QA)
- Decide next steps and advance stage

**Prohibited Master actions (self-substitution is forbidden):**
- Directly executing web research when `scout` or `research` is assigned
- Directly auditing sources when `source-auditor` is assigned
- Directly clustering pain when `pain-miner` is assigned
- Directly designing the product when `design-director` is assigned
- Directly building content when `product-builder` is assigned
- Directly building code when `software-builder` is assigned
- Directly building PDFs/DOCX/HTML artifacts when `artifact-builder` is assigned
- Declaring QA complete without invoking `artifact-qa` or `software-qa`
- Declaring taste review passed without invoking `taste-reviewer`
- Declaring the audit passed without invoking `critic`
- Simulating a worker's output internally as a substitute for actual invocation

---

## MANDATORY INVOCATION RULE

> **When a workflow stage assigns a task to a specialized agent, the Master MUST invoke that agent using `invoke_subagent`. Describing the delegation, simulating the worker, or producing the worker's output internally does NOT constitute delegation.**

**If invocation fails:**
1. STOP the stage.
2. Log the failure in the delegation log under `invocation_status: "failed"`.
3. Report the failure to the human.
4. Do NOT silently perform the task yourself.

---

## STAGE → REQUIRED AGENTS MAP

### STAGE: discovery
**Required agents (must all be invoked; may parallelize):**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `scout` | `research/raw/community-signals.md` | ✅ REQUIRED |
| `research` | `research/verified/market-context.md` | ✅ REQUIRED |
| `competitor` | `research/synthesis/competitive-analysis.md` | ✅ REQUIRED |

**Parallelization:** Scout, Research, and Competitor may run concurrently (no shared input dependencies at stage start).

---

### STAGE: validation
**Required agents:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `pain-miner` | `research/synthesis/pain-clusters.md` | ✅ REQUIRED |
| `source-auditor` | `research/verified/source-audit.md` | ✅ REQUIRED |
| `competitor` | `research/synthesis/competitive-analysis.md` | ✅ REQUIRED (may reuse from discovery if fresh) |

**Dependency:** Pain-miner requires community-signals.md. Source-auditor requires sources.csv entries. Competitor requires market-context.md. Sequence accordingly.

---

### STAGE: opportunity_selection
**Required agents:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `opportunity-analyst` | `memory/opportunities.csv` + `research/synthesis/opportunities/<id>.md` | ✅ REQUIRED |

**Gate:** HUMAN APPROVAL GATE 1 — Master must invoke `ask_question`. Stage does not advance without explicit human selection.

---

### STAGE: product_strategy
**Required agents:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `product-strategist` | `products/<product_id>/specification.json` | ✅ REQUIRED |

**Gate:** HUMAN APPROVAL GATE 2 — Master presents specification. Human must approve modality, transformation, and scope.

---

### STAGE: creative_concept
**Required agents:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `creative-director` | `products/<product_id>/creative-concept.md` | ✅ REQUIRED |
| `marketing-strategist` | `products/<product_id>/customer-wow.md` | ⚠️ OPTIONAL (recommended for consumer products) |

---

### STAGE: architecture
**Condition:** Only for software, web, mobile, API, database, or hybrid products.

| Agent | Primary Output Artifact | Required |
|---|---|---|
| `solution-architect` | `products/<product_id>/architecture.md` | ✅ REQUIRED (when applicable) |

---

### STAGE: design
**Required agents:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `design-director` | `design/<product_id>/design-system.md` | ✅ REQUIRED |

**Gate:** HUMAN APPROVAL GATE 3 — Human must approve visual tone, palette, typography, and layout before full asset production.

---

### STAGE: asset_pipeline
**Required agents:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `asset-director` | `products/<product_id>/assets/asset-manifest.json` | ✅ REQUIRED |

---

### STAGE: product_build
**Routing — choose based on approved modality:**

**Document / Workbook:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `product-builder` | `products/<product_id>/content/` | ✅ REQUIRED |
| `artifact-builder` | `products/<product_id>/deliverables/` | ✅ REQUIRED |

**Spreadsheet / Financial Model:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `product-builder` | content modules | ✅ REQUIRED |
| `artifact-builder` | `.xlsx` / `.csv` output | ✅ REQUIRED |

**Software / Web / Mobile / API / Database:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `software-builder` | `products/<product_id>/software/` | ✅ REQUIRED |

**Hybrid:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `software-builder` | software components | ✅ REQUIRED |
| `artifact-builder` | physical deliverable components | ✅ REQUIRED |

**Parallelization:** Independent modules (e.g., separate document chapters, independent software services) may be built concurrently. Do not allow concurrent writes to the same shared output file.

---

### STAGE: qa
**Required agents (may parallelize where inputs allow):**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `artifact-qa` | `products/<product_id>/audit/artifact-qa.json` | ✅ REQUIRED (document/hybrid products) |
| `software-qa` | `products/<product_id>/audit/software-qa.json` | ✅ REQUIRED (software products) |
| `taste-reviewer` | `products/<product_id>/audit/taste-review.md` | ✅ REQUIRED (all products) |

**Parallelization:** `artifact-qa`, `software-qa`, and `taste-reviewer` may run concurrently on the completed build output.

---

### STAGE: packaging
**Required agents:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `packaging` | `packaging/<product_id>/landing-page.md` | ✅ REQUIRED |
| `marketing-strategist` | `products/<product_id>/merchandising.json` | ✅ REQUIRED |

---

### STAGE: audit
**Required agents (may parallelize):**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `critic` | `products/<product_id>/audit/audit.json` | ✅ REQUIRED |

**Parallelization:** Critic may run concurrently with packaging preparation.

---

### STAGE: release
**Required agents:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `release-engineer` | `products/<product_id>/manifest.json` | ✅ REQUIRED |

**Gate:** HUMAN APPROVAL GATE 4 — Final sign-off required before deployment and creator outreach.

---

### STAGE: distribution
**Required agents:**
| Agent | Primary Output Artifact | Required |
|---|---|---|
| `distribution` | `distribution/<product_id>/creator-outreach-pack.md` | ✅ REQUIRED |

---

## PRODUCT BUILD ROUTING SUMMARY

```
DOCUMENT PRODUCT:
  product-strategist → creative-director → design-director
  → product-builder → asset-director → artifact-builder
  → artifact-qa + taste-reviewer (parallel)
  → packaging + marketing-strategist
  → critic → release-engineer → distribution

TEMPLATE PRODUCT:
  product-strategist → creative-director → design-director
  → artifact-builder (or external integration)
  → artifact-qa + taste-reviewer (parallel)
  → packaging → critic → release-engineer → distribution

SOFTWARE PRODUCT:
  product-strategist → solution-architect → creative-director
  → design-director → software-builder
  → software-qa + artifact-qa + taste-reviewer (parallel)
  → release-engineer → packaging + marketing-strategist
  → critic → distribution

HYBRID PRODUCT:
  product-strategist → solution-architect (if required)
  → parallel: software-builder + artifact-builder (independent components only)
  → integration point → unified QA
  → taste-reviewer → packaging → release-engineer → critic → distribution
```

---

## PARALLELIZATION RULES

**Independent tasks SHOULD be invoked concurrently:**
- Discovery: scout + research + competitor (stage start — no shared input dependencies)
- Validation: source-auditor (while pain-miner runs if inputs are available)
- QA: artifact-qa + software-qa + taste-reviewer
- Audit: critic (may overlap with packaging prep if build is frozen)
- Product build: independent content modules, independent software microservices

**Never parallelize:**
- Tasks where Agent B requires Agent A's output as direct input
- Tasks where both agents write to the same shared artifact (coordination required)
- Gate-guarded stages — always complete the gate before advancing

---

## WORKER COMPLETION REQUIREMENTS

Every worker invocation must return:

| Field | Description |
|---|---|
| `result` | Summary of what was accomplished |
| `artifacts_created` | List of file paths written |
| `sources_used` | Source IDs from memory/sources.csv |
| `assumptions` | Any assumptions made during execution |
| `uncertainties` | Unresolved questions that may affect downstream stages |
| `risks` | Known risks in the output |
| `confidence` | Numerical score 0–100 |
| `recommended_next_step` | Worker's suggestion for next action |

**The Master must verify:**
1. The required artifact file exists and is non-empty.
2. The artifact conforms to its schema (where applicable).
3. No required fields are missing or placeholder-only.
4. The worker's confidence level is appropriate for stage advancement.
5. Any flagged risks or contradictions are resolved before advancing.

---

## WORKER TRUST RULE

The Master treats worker output as **evidence to be evaluated**, not truth to be accepted.

After every worker returns:
1. Read the output and required artifacts.
2. Check artifact existence and non-empty content.
3. Validate against expected schema.
4. Identify any internal contradictions or conflicts with other workers.
5. Resolve conflicts — do not silently ignore them.
6. Perform integration into coherent state.
7. Update `state.json` with stage progress.
8. Log the invocation result in the delegation log.

---

## STAGE COMPLETION GATES

A stage may advance to the next stage ONLY when ALL of the following are true:

- [ ] All required agent invocations recorded in delegation log with `invocation_status: "completed"`
- [ ] All required artifact files exist at expected paths and are non-empty
- [ ] Schema validation passes for all structured output artifacts
- [ ] Worker-reported contradictions have been resolved and documented
- [ ] Stage-specific QA or gate criteria have been satisfied
- [ ] `state.json` has been updated to reflect stage completion
- [ ] If a human approval gate is required: `ask_question` was called and human approved

---

## SKILL-FIRST ENFORCEMENT

Before any specialist executes, the Master must:
1. Identify the relevant skill(s) in `.agents/skills/`
2. Identify relevant templates in `templates/`
3. Identify required tools (`system/scripts/`)
4. Pass those resources explicitly to the worker in the invocation prompt
5. After completion, verify the worker used them (artifact must reflect skill standards)

Do not force workers to recreate capabilities already encoded in existing skills.

---

*Last updated: 2026-09-11 — Template reset and architecture enforcement added.*
