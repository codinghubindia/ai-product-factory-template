# DISTRIBUTION & COMPLETION WORKFLOW

This workflow guides the preparation of targeted creator distribution partnerships and the final definition of done.

> **Reminder:** The Master INVOKES `distribution` using `invoke_subagent`. The Master does not research, vet, or write creator outreach materials itself.

---

## Stage 16: Distribution Strategy & Creator Partnerships

### State Update
```json
{
  "workflow.stage": "distribution",
  "workflow.last_completed_stage": "release",
  "workflow.status": "running",
  "workflow.next_required_action": "Invoking distribution agent for creator fit analysis"
}
```

### Prerequisite Verification
```
Before invoking distribution, Master must verify:
  ✓ products/<product_id>/manifest.json exists
  ✓ audit.json exists with audit.status = "PASS"
  ✓ packaging/<product_id>/landing-page.md exists
  ✓ Human Gate 4 has been approved
```

### Required Agent Invocation

| Agent | Task | Required Artifacts | Dependency |
|---|---|---|---|
| `distribution` (**REQUIRED**) | Discover and vet creator collaboration channels by audience problem alignment, content format compatibility, demonstration feasibility, creator credibility | `distribution/<product_id>/creator-outreach-pack.md` | manifest.json + Gate 4 approval |

### Invocation Protocol
```
INVOKE distribution
  PASS: specification.json, creative-concept.md, landing-page.md, merchandising.json
  PASS: .agents/skills/creative-marketing/SKILL.md
  PASS: target customer profile from memory/customers.json
  REQUIRE: ranked creator shortlist with evidence-backed rationale
  REQUIRE: personalized collaboration packs for top candidates
  PROHIBIT: ranking creators purely by follower count
  PROHIBIT: fabricated email addresses, engagement statistics, or past sponsorship claims
  → WAIT for response
  → VERIFY: distribution/<product_id>/creator-outreach-pack.md exists and non-empty
  → READ: verify creator vetting rationale is evidence-backed (not invented)
  → Record invocation in delegation log
  → UPDATE: state.json (distribution.status = "completed")
```

### Required Outreach Pack Contents
Each creator outreach pack must include:
- Specific collaboration angle and personalized hook (no generic templates)
- Concise value proposition tailored to the creator's audience
- 3 concrete short-form content ideas or demonstration scripts
- Suggested call-to-action (CTA) and lead magnet
- Proposed commercial structure (affiliate rev-share, upfront sponsorship hypothesis, or co-branded bonus)

---

## Stage 17: Factory Completion (Definition of Done)

### Final Verification Checklist (Master performs this integration check)

```
UPDATE state.json:
  workflow.stage = "complete"
  workflow.last_completed_stage = "distribution"
  workflow.status = "complete"
  workflow.next_required_action = "Project fully completed; ready for market launch or new project"
  workflow.current_blocking_issue = null
```

### Completion Gate — ALL items must be verified:

| Item | Verification |
|---|---|
| Product specification satisfied | `products/<product_id>/specification.json` exists |
| High-utility deliverables assembled | `products/<product_id>/deliverables/` has non-empty files |
| All claims backed by audited evidence | `memory/sources.csv` entries correspond to all quantitative claims |
| Design system applied | `design/<product_id>/design-system.md` exists |
| QA passed | `artifact-qa.json` and/or `software-qa.json` show PASS |
| Taste review passed | `taste-review.md` shows PASS |
| Critic audit passed | `audit.json` shows 0 critical, 0 un-waived high issues |
| Truthful packaging ready | `packaging/<product_id>/landing-page.md` exists |
| Creator outreach generated | `distribution/<product_id>/creator-outreach-pack.md` exists |
| Delegation log complete | All required agents recorded with `invocation_status: "completed"` |
| Decision log updated | `memory/decisions.md` has Gate 4 approval entry |
| state.json complete | All fields reflect final state |

### After Completion

The template resets for the next project:
1. `products/<product_id>/` directory is preserved as project archive.
2. `state.json` is reset to `idle` state for new project.
3. `memory/opportunities.csv` and `memory/sources.csv` are preserved as project-specific references.
4. Run `system/scripts/factory_health_check.py` to verify template cleanliness before the next project.

---

*Workflow version: 0.3.0 — Updated 2026-09-11: Added explicit INVOKE → WAIT → VERIFY protocol, prerequisite verification, delegation log recording, outreach pack content requirements, and post-completion template reset instructions.*
