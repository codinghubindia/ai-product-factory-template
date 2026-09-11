# DISCOVERY & VALIDATION WORKFLOW

This workflow guides the transition through canonical stages: `discovery` → `research` → `validation` → `opportunity_selection` (Gate 1).

> **Reminder:** The Master INVOKES agents using `invoke_subagent`. The Master does not perform the work of these agents itself.

---

## Stage 1: Discovery (Raw Problem Signals)

### State Update
```json
{
  "workflow.stage": "discovery",
  "workflow.status": "running",
  "workflow.next_required_action": "Invoking scout, research, and competitor concurrently"
}
```

### Required Agent Invocations (PARALLEL — invoke all three simultaneously)

| Agent | Task | Required Artifact |
|---|---|---|
| `scout` (**REQUIRED**) | Harvest raw customer language, complaints, workarounds, and frustration signals across public communities (Reddit, niche forums, app reviews, GitHub issues) | `research/raw/community-signals.md` |
| `research` (**REQUIRED**) | Investigate industry dynamics, existing solution categories, terminology, technical constraints, and macro trends | `research/verified/market-context.md` |
| `competitor` (**REQUIRED**) | Map incumbent solutions, pricing, strengths, weaknesses, and customer complaint patterns | `research/synthesis/competitive-analysis.md` |

**Parallelization:** All three may be invoked simultaneously as they have no shared input dependencies at stage start.

### Invocation Protocol
```
INVOKE scout, research, competitor (simultaneously via invoke_subagent)
  → WAIT for all three to return
  → VERIFY: research/raw/community-signals.md exists and non-empty
  → VERIFY: research/verified/market-context.md exists and non-empty
  → VERIFY: research/synthesis/competitive-analysis.md exists and non-empty
  → Record all three invocations in delegation log
  → INTEGRATE findings: note patterns, surface contradictions
  → UPDATE state.json (stage = "discovery", status = "complete")
  → Advance to Stage 2
```

### Skill References to Pass to Agents
- Scout: no specialized skill required; instruct on verbatim quote extraction, forbidden fabrication
- Research: no specialized skill required; prioritize Tier 1 and Tier 2 sources
- Competitor: no specialized skill required; map gap opportunities explicitly

### Safety Invariants
- Zero fabricated quotes, post counts, or fake URLs permitted in any output.
- Scout must record source URLs in `memory/sources.csv` as it works.
- Research must distinguish verified benchmarks from estimates.

---

## Stage 2: Validation, Clustering & Gap Analysis

### State Update
```json
{
  "workflow.stage": "validation",
  "workflow.last_completed_stage": "discovery",
  "workflow.next_required_action": "Invoking pain-miner and source-auditor"
}
```

### Required Agent Invocations

**Step 2A — Pain Clustering (REQUIRED first):**

| Agent | Task | Required Artifact | Dependency |
|---|---|---|---|
| `pain-miner` (**REQUIRED**) | Cluster raw signals from `research/raw/community-signals.md` into discrete pain patterns, JTBD, root problems, and workarounds | `research/synthesis/pain-clusters.md` | community-signals.md must exist |

**Invocation Protocol for Step 2A:**
```
INVOKE pain-miner
  → WAIT for response
  → VERIFY: research/synthesis/pain-clusters.md exists and non-empty
  → Record invocation in delegation log
```

**Step 2B — Source Audit (may run concurrently with 2A once sources.csv has entries):**

| Agent | Task | Required Artifact | Dependency |
|---|---|---|---|
| `source-auditor` (**REQUIRED**) | Audit all key claims in `memory/sources.csv` against Tier 1–5 hierarchy; flag unsupported assertions and stale data | `research/verified/source-audit.md` | sources.csv must have entries |

**Invocation Protocol for Step 2B:**
```
INVOKE source-auditor
  → WAIT for response
  → VERIFY: research/verified/source-audit.md exists and non-empty
  → Record invocation in delegation log
```

### Master Integration After Stage 2
```
READ: pain-clusters.md, source-audit.md, competitive-analysis.md
IDENTIFY: contradictions between pain clusters and competitive analysis
RESOLVE: contradictions by cross-referencing source-audit findings
UPDATE: state.json (stage = "validation", status = "complete")
ADVANCE to Stage 3
```

---

## Stage 3: Opportunity Scoring (GATE 1)

### State Update
```json
{
  "workflow.stage": "opportunity_selection",
  "workflow.last_completed_stage": "validation",
  "workflow.next_required_action": "Invoking opportunity-analyst; then awaiting Human Approval Gate 1"
}
```

### Required Agent Invocation

| Agent | Task | Required Artifacts | Dependency |
|---|---|---|---|
| `opportunity-analyst` (**REQUIRED**) | Apply 12-dimension weighted scoring model from `system/scoring.md` across all identified pain clusters; separate Opportunity Attractiveness from Evidence Confidence; apply Risk Penalties | `memory/opportunities.csv` + `research/synthesis/opportunities/<id>.md` for each opportunity | pain-clusters.md + source-audit.md must exist |

### Invocation Protocol
```
INVOKE opportunity-analyst
  → WAIT for response
  → VERIFY: memory/opportunities.csv has new data rows
  → VERIFY: research/synthesis/opportunities/ contains at least one OPP-XXX.md
  → Record invocation in delegation log
  → READ scores; reject any speculative scores unsupported by source evidence
  → INTEGRATE into ranked presentation
```

### HUMAN APPROVAL GATE 1 (MANDATORY — DO NOT BYPASS)
```
PRESENT: ranked opportunity scores with evidence backing
INVOKE ask_question → Human selects or approves opportunity ID
RECORD: state.json (opportunity.selected_id, opportunity.name, opportunity.status = "selected")
RECORD: memory/decisions.md (selected opportunity rationale)
RECORD: memory/rejected-ideas.md (non-selected candidates with specific reasons)
→ Do NOT proceed to product strategy without explicit human approval response
```

---

*Workflow version: 0.3.0 — Updated 2026-09-11: Replaced vague "launch agent" instructions with explicit INVOKE → WAIT → VERIFY → INTEGRATE → UPDATE protocol. Added parallel invocation specification, dependency mapping, and delegation log requirements.*
