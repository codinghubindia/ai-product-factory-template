# Durable Project Memory

This directory holds persistent, append-oriented project memory that survives individual agent sessions.

---

## Memory Registries

1. **`sources.csv`**
   - Provenance registry for all inspected evidence sources across communities, industry analyses, and documentation.
   - Conforms to `system/schemas/source.schema.json`.
   - Tracks Source ID, canonical URL, tier (1–5), verification status, supporting claims, independent corroboration, and confidence.

2. **`opportunities.csv`**
   - Registry of all formulated and scored opportunities.
   - Tracks 12-dimensional scores, overall weighted score, evidence confidence, risk status, and stage status.

3. **`decisions.md`**
   - Append-only decision log recording strategic choices, human approvals, architectural pivots, format justifications, and documented audit waivers.

4. **`rejected-ideas.md`**
   - Record of explored ideas that failed validation, were superseded, or were rejected, including exact reasons to prevent redundant rediscovery.

5. **`customers.json`**
   - Reusable customer personas, jobs-to-be-done, acute pains, workarounds, and channel behaviors conforming to `system/schemas/customer.schema.json`.

---

## Memory Invariants
- Memory files must never be silently overwritten or wiped.
- Memory entries are decision-support indexes and audit trails, never a substitute for primary source evidence.
