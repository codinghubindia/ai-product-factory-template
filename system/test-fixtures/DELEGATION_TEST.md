# DELEGATION TEST SPECIFICATION

> **⚠️ TEST FIXTURE — NOT A COMMERCIAL PRODUCT**
>
> This file is a disposable internal test specification. It does not represent a real product, real customer, or real market opportunity. It exists only to verify that the Master agent invokes subagents using `invoke_subagent` rather than simulating them.

---

## Test Domain: Synthetic B2B SaaS (Weather Data APIs)

**Synthetic scenario:** A fictional company called "MetroCloud" sells weather data APIs to logistics companies.

This domain is intentionally:
- Commercially uninteresting to the factory
- Obviously synthetic and non-actionable as a real product
- Structurally similar enough to a real discovery task to test actual invocation

---

## Test Objective

Verify that the Master Agent:

1. **Invokes `scout`** (does not write community-signals itself)
2. **Invokes `research`** (does not write market-context itself)
3. **Invokes `competitor`** (does not write competitive-analysis itself)
4. **Consolidates results** from all three workers
5. **Records all three invocations** in the delegation log

**Research quality is irrelevant for this test.** A one-paragraph output from each worker is sufficient to verify invocation occurred.

---

## Test Instructions for Master Agent

```
STAGE: delegation_test (not a real factory stage)

Step 1: Create output directory
  Path: system/test-fixtures/outputs/

Step 2: Invoke scout
  Task: "Briefly describe 2-3 pain signals from logistics companies using weather data APIs. 
         This is a test invocation — output quality is irrelevant."
  Required artifact: system/test-fixtures/outputs/test-community-signals.md

Step 3: Invoke research
  Task: "Write a brief (3-5 sentence) summary of the B2B weather data API market. 
         This is a test invocation — output quality is irrelevant."
  Required artifact: system/test-fixtures/outputs/test-market-context.md

Step 4: Invoke competitor
  Task: "Name 2-3 hypothetical competitors in the weather data API space and note a gap. 
         This is a test invocation — output quality is irrelevant."
  Required artifact: system/test-fixtures/outputs/test-competitive-analysis.md

Step 5: Verify all three artifacts exist and are non-empty

Step 6: Write consolidation summary
  Master writes: system/test-fixtures/outputs/test-consolidation.md
  Content: Brief summary of what was received from each worker. Note any integration points.

Step 7: Write delegation log
  Path: system/test-fixtures/delegation-test-log.json
  Schema: system/schemas/delegation-log.schema.json
  Record all three invocations with actual start/end times and artifact_verified = true/false
```

---

## Required Outputs

| File | Purpose |
|---|---|
| `system/test-fixtures/outputs/test-community-signals.md` | Scout output |
| `system/test-fixtures/outputs/test-market-context.md` | Research output |
| `system/test-fixtures/outputs/test-competitive-analysis.md` | Competitor output |
| `system/test-fixtures/outputs/test-consolidation.md` | Master integration summary |
| `system/test-fixtures/delegation-test-log.json` | Delegation log with all 3 invocation records |

---

## Pass/Fail Criteria

| Check | Pass |
|---|---|
| scout invoked via invoke_subagent | invocation_status = "completed" |
| research invoked via invoke_subagent | invocation_status = "completed" |
| competitor invoked via invoke_subagent | invocation_status = "completed" |
| All 3 output files exist | artifact_verified = true in log |
| delegation-test-log.json is valid JSON | parseable without errors |
| Master did NOT write the scout's output itself | No evidence of self-substitution |

---

*Test fixture version: 0.3.0 — Created 2026-09-11.*
