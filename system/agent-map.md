# AI PRODUCT FACTORY — AGENT ARCHITECTURE MAP

The factory employs 13 specialized agents coordinated by the Master Agent.

---

## 1. Master Agent
- **File:** `.agents/agents/master/agent.md`
- **Role:** Orchestrator, final decision-maker, and repository quality custodian.
- **Responsibilities:** Owns `state.json`, memory updates, worker delegation, human approval gates, audit verification, and final shipment.
- **Authority:** Coordinates all subagents. Subagents cannot override the Master.

---

## 2. Discovery & Validation Team
1. **`scout`** (`.agents/agents/scout/agent.md`)
   - *Role:* Harvests raw, unprompted customer pain signals from public communities.
   - *Inputs:* Search queries, industry parameters.
   - *Outputs:* `research/raw/`, `memory/sources.csv`.
2. **`research`** (`.agents/agents/research/agent.md`)
   - *Role:* Investigates domain context, incumbent categories, macro trends, and quantitative benchmarks.
   - *Inputs:* Industry keywords, workflow descriptions.
   - *Outputs:* `research/verified/`.
3. **`pain-miner`** (`.agents/agents/pain-miner/agent.md`)
   - *Role:* Synthesizes raw signals into structured pain clusters, jobs-to-be-done, and root problems.
   - *Inputs:* `research/raw/`, `memory/sources.csv`.
   - *Outputs:* `research/synthesis/pain-clusters.md`.
4. **`source-auditor`** (`.agents/agents/source-auditor/agent.md`)
   - *Role:* Adversarial fact-checker evaluating claim support against the 5-tier source hierarchy.
   - *Inputs:* Claims in research, opportunities, and product files.
   - *Outputs:* `research/verified/source-audit.md`, updates to `memory/sources.csv`.
5. **`competitor`** (`.agents/agents/competitor/agent.md`)
   - *Role:* Maps incumbent solutions, pricing, failure modes, and customer complaints to reveal exploitable gaps.
   - *Inputs:* Incumbent names, community reviews.
   - *Outputs:* `research/synthesis/competitive-analysis.md`.
6. **`opportunity-analyst`** (`.agents/agents/opportunity-analyst/agent.md`)
   - *Role:* Translates validated problem clusters into scored, ranked commercial opportunity hypotheses.
   - *Inputs:* `pain-clusters.md`, `competitive-analysis.md`, `source-audit.md`, `system/scoring.md`.
   - *Outputs:* `memory/opportunities.csv`, `research/synthesis/opportunities/<id>.md`.

---

## 3. Product Engineering & Quality Team
7. **`product-strategist`** (`.agents/agents/product-strategist/agent.md`)
   - *Role:* Transforms approved opportunities into detailed, modular product blueprints and specifications.
   - *Inputs:* Approved opportunity dossier.
   - *Outputs:* `products/<product_id>/specification.json`, `products/<product_id>/strategy.md`.
8. **`product-builder`** (`.agents/agents/product-builder/agent.md`)
   - *Role:* Constructs actionable, high-utility product content, fillable templates, tools, and assembled deliverables.
   - *Inputs:* `specification.json`, supporting research.
   - *Outputs:* `products/<product_id>/content/`, `products/<product_id>/assets/`, `products/<product_id>/final/`.
9. **`design-director`** (`.agents/agents/design-director/agent.md`)
   - *Role:* Establishes and enforces the visual design system, layout hierarchy, and presentation polish.
   - *Inputs:* `products/<product_id>/specification.json`, raw deliverable drafts.
   - *Outputs:* `design/<product_id>/design-system.md`, visual formatting in `products/<product_id>/final/`.
10. **`packaging`** (`.agents/agents/packaging/agent.md`)
    - *Role:* Crafts truthful, high-converting product descriptions, offer stacks, landing page copy, and mockups based strictly on the finished product.
    - *Inputs:* Assembled deliverables in `products/<product_id>/final/`, `design-system.md`.
    - *Outputs:* Assets under `packaging/<product_id>/`.
11. **`critic`** (`.agents/agents/critic/agent.md`)
    - *Role:* Independent red-team auditor that actively seeks reasons not to ship.
    - *Inputs:* All product deliverables, design systems, and packaging.
    - *Outputs:* `products/<product_id>/audit/audit.json`, `products/<product_id>/audit/report.md`.

---

## 4. Distribution Team
12. **`distribution`** (`.agents/agents/distribution/agent.md`)
    - *Role:* Vets prospective creator partners and generates tailored collaboration outreach packs.
    - *Inputs:* `products/<product_id>/final/`, `packaging/<product_id>/`, `memory/customers.json`.
    - *Outputs:* `distribution/<product_id>/creator-shortlist.md`, `distribution/<product_id>/outreach/`.

---

## 5. Master Delegation Rules
- Workers are specialized tools. Master invokes subagents via `invoke_subagent` and monitors outputs.
- Subagents do not delegate to other subagents.
- All persistent work must be written to designated file paths rather than remaining in conversation history.
