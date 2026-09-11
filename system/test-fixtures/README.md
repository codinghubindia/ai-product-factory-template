# Delegation Test Fixture

> **PURPOSE:** This directory contains a disposable, internal delegation test used to verify that the Master agent actually invokes subagents rather than simulating them.
>
> **IMPORTANT:** This is NOT a commercial product. It contains no real research, no real customer data, and no commercially usable output. It exists solely to test the invocation mechanism.
>
> **CLEANUP:** Delegation test outputs in this directory may be deleted at any time. The schemas and scripts here are test infrastructure only.

---

## What the Delegation Test Does

The delegation test verifies:
1. Master invokes `scout` → receives a result (content irrelevant)
2. Master invokes `research` → receives a result (content irrelevant)
3. Master invokes `competitor` → receives a result (content irrelevant)
4. Master consolidates the results
5. All three invocations are recorded in the delegation log

**The test domain is synthetic:** "A fictional B2B SaaS company selling weather data APIs." This domain was chosen because it is:
- Commercially uninteresting to the factory
- Obviously synthetic and non-actionable
- Unlikely to be confused with a real product run

---

## How to Run the Delegation Test

Instruct the Master agent:

```
Run a delegation test using system/test-fixtures/DELEGATION_TEST.md as the test specification.
Do NOT produce a commercial product.
The purpose is to verify actual agent invocation — not research quality.
```

---

## Expected Delegation Log Output

After the test, a file should exist at:
`system/test-fixtures/delegation-test-log.json`

It should contain three invocation records with `invocation_status: "completed"` for scout, research, and competitor.

---

## Test Pass Criteria

| Criterion | Pass Condition |
|---|---|
| scout invoked | `invocation_status: "completed"` in log |
| research invoked | `invocation_status: "completed"` in log |
| competitor invoked | `invocation_status: "completed"` in log |
| All artifacts written | Each agent wrote a non-empty output file |
| Master did NOT self-substitute | No log entry shows Master producing the worker's content |
| Delegation log exists | `system/test-fixtures/delegation-test-log.json` present and valid JSON |

---

*This fixture was created 2026-09-11 as part of the factory architecture enforcement update (v0.3.0).*
