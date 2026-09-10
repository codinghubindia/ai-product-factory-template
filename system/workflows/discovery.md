# DISCOVERY & VALIDATION WORKFLOW

This workflow guides the transition through canonical stages: `discovery` → `research` → `validation` → `opportunity_selection` (Gate 1).

---

## Stage 1: Discovery (Raw Problem Signals)

1. **State Update:**
   - `workflow.stage = "discovery"`
   - `workflow.status = "running"`
   - `workflow.next_required_action = "Scouting public problem signals and community evidence"`
2. **Worker Delegation:**
   - Launch `scout` agent to harvest raw customer language, complaints, workarounds, and frustration signals across public communities (Reddit, niche forums, app reviews).
3. **Artifacts Produced:**
   - Raw source records in `memory/sources.csv`
   - Unfiltered community notes in `research/raw/`
4. **Safety Check:**
   - No fabricated quotes, post counts, or fake URLs permitted.

---

## Stage 2: Contextual Research

1. **State Update:**
   - `workflow.stage = "research"`
   - `workflow.last_completed_stage = "discovery"`
   - `workflow.next_required_action = "Investigating market context, workflows, and domain benchmarks"`
2. **Worker Delegation:**
   - Launch `research` agent to investigate industry dynamics, existing solution categories, terminology, technical constraints, and macro trends.
3. **Artifacts Produced:**
   - Contextual and domain reports in `research/verified/`
4. **Safety Check:**
   - Prioritize Tier 1 and Tier 2 sources for factual and benchmark data.

---

## Stage 3: Validation, Clustering & Gap Analysis

1. **State Update:**
   - `workflow.stage = "validation"`
   - `workflow.last_completed_stage = "research"`
   - `workflow.next_required_action = "Clustering pain, auditing source evidence, and analyzing competitor gaps"`
2. **Worker Delegation (Synthesis Sequence):**
   - **Step 3A (Pain Miner):** Clusters raw signals into discrete pain patterns, jobs-to-be-done, root problems, and workarounds. Writes `research/synthesis/pain-clusters.md`.
   - **Step 3B (Source Auditor):** Audits all key claims and sources against Tier 1–5 hierarchy, flagging unsupported assertions or stale data. Writes `research/verified/source-audit.md`.
   - **Step 3C (Competitor):** Maps incumbent solutions, pricing, strengths, weaknesses, and customer complaints to isolate unserved gaps. Writes `research/synthesis/competitive-analysis.md`.
3. **Safety Check:**
   - Never assume social post volume equals commercial demand. Ensure independent user corroboration.

---

## Stage 4: Opportunity Scoring & Selection (GATE 1)

1. **State Update:**
   - `workflow.stage = "opportunity_selection"`
   - `workflow.last_completed_stage = "validation"`
   - `workflow.next_required_action = "Scoring opportunities and awaiting Human Approval Gate 1"`
2. **Worker Delegation:**
   - Launch `opportunity-analyst` to apply the transparent weighted scoring model from `system/scoring.md` across all 12 dimensions.
   - Separate Opportunity Attractiveness from Evidence Confidence.
   - Apply Risk Penalties and verify Confidence Gates.
3. **Artifacts Produced:**
   - Update `memory/opportunities.csv`
   - Detailed opportunity records in `research/synthesis/opportunities/<id>.md`
4. **Master Review:**
   - Master reviews rankings, confirms evidence backing, rejects speculative scores, and formats the opportunity presentation.
5. **HUMAN APPROVAL GATE 1:**
   - Master pauses and invokes `ask_question` for the human to select or approve the winning opportunity ID.
   - Update `state.json` (`opportunity.selected_id`, `opportunity.name`, `opportunity.status = "selected"`).
   - Update `memory/decisions.md` with selected opportunity rationale.
   - Record non-selected candidate ideas in `memory/rejected-ideas.md` with specific reasons.
   - Do **NOT** proceed to product building without explicit human approval.
