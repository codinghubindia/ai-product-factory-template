# AI Product Factory Template

An autonomous, multi-agent digital product studio operating inside **Google Antigravity CLI (`agy`)**.

The AI Product Factory is designed to convert empirical customer pain into commercially viable, high-utility digital products (templates, frameworks, workbooks, guides, toolkits), craft functional design systems, generate truthful packaging copy, perform adversarial red-team quality audits, and prepare targeted creator-driven distribution campaigns.

---

## 1. What This Project Is

This repository provides a production-ready, persistent workspace template for multi-agent pair programming and orchestration. Unlike naive single-prompt AI generators that fabricate market demand and hallucinate statistics, the AI Product Factory enforces:
- **Strict Epistemic Boundaries:** Rigorous distinction between `FACT`, `OBSERVATION`, `INFERENCE`, `ASSUMPTION`, and `HYPOTHESIS`.
- **Primary Source Provenance:** All claims and opportunity scores must trace back to verifiable public community signals in `memory/sources.csv`.
- **Bounded Autonomous Execution:** The Master Agent coordinates workers autonomously across routine tasks, but strictly halts at **4 Strategic Human Approval Gates**.
- **Adversarial Quality Control:** Deliverables cannot ship without passing an independent red-team audit (`critic` agent) that actively seeks reasons not to ship.
- **Truthful Packaging & Creator Vetting:** Packaging claims must map directly to built deliverable components, and distribution partners are vetted by audience problem alignment rather than vanity follower counts.

---

## 2. Agent Architecture

The factory operates via **13 specialized agents** configured under `.agents/agents/` with dedicated tools, roles, and boundaries:

```
                               ┌────────────────────────────────┐
                               │          MASTER AGENT          │
                               │  Orchestration, Gates & State  │
                               └───────────────┬────────────────┘
                                               │
       ┌───────────────────────────────────────┼───────────────────────────────────────┐
       ▼                                       ▼                                       ▼
┌──────────────────────────────┐ ┌──────────────────────────────┐ ┌──────────────────────────────┐
│    DISCOVERY & VALIDATION    │ │     PRODUCT ENGINEERING      │ │         DISTRIBUTION         │
├──────────────────────────────┤ ├──────────────────────────────┤ ├──────────────────────────────┤
│ • scout (raw signals)        │ │ • product-strategist (specs) │ │ • distribution (creator fit) │
│ • research (context & benchmarks)│ • product-builder (deliverables)│ │                          │
│ • pain-miner (problem clusters)│ • design-director (visual system)│ │                          │
│ • source-auditor (fact check)│ │ • packaging (landing page/copy)│ │                          │
│ • competitor (gap analysis)  │ │ • critic (red-team audit)    │ │                              │
│ • opportunity-analyst (scores)│└──────────────────────────────┘ └──────────────────────────────┘
└──────────────────────────────┘
```

### Agent Roster

| Agent Name | Model | Role & Core Responsibility | Key Outputs |
| :--- | :--- | :--- | :--- |
| **`master`** | `pro` | Orchestrator, human gatekeeper, state manager, and final quality custodian. | `state.json`, `memory/decisions.md` |
| **`scout`** | `flash` | Harvests unprompted customer pain signals across Reddit, forums, and reviews. | `research/raw/`, `memory/sources.csv` |
| **`research`** | `pro` | Investigates industry context, workflows, incumbent categories, and benchmarks. | `research/verified/` |
| **`pain-miner`** | `pro` | Clusters raw evidence into jobs-to-be-done, root problems, and workarounds. | `research/synthesis/pain-clusters.md` |
| **`source-auditor`**| `pro` | Adversarial fact-checker evaluating claims against 5-tier source hierarchy. | `research/verified/source-audit.md` |
| **`competitor`** | `pro` | Maps incumbents, customer complaints, and churn drivers to isolate market gaps. | `research/synthesis/competitive-analysis.md` |
| **`opportunity-analyst`**| `pro` | Evaluates clusters using the 12-dimensional weighted rubric in `system/scoring.md`. | `memory/opportunities.csv`, `opportunities/<id>.md` |
| **`product-strategist`**| `pro` | Formulates full product specification, unique mechanism, and transformation. | `products/<id>/specification.json`, `strategy.md` |
| **`product-builder`**| `pro` | Constructs actionable content, fillable templates, checklists, and tools. | `products/<id>/final/` |
| **`design-director`**| `pro` | Creates and enforces visual systems adhering to the 6 Pillars of Premium Design. | `design/<id>/design-system.md` |
| **`packaging`** | `pro` | Crafts truthful sales copy, offer stack, bonuses, and landing page content. | `packaging/<id>/` |
| **`critic`** | `pro` | Red-team auditor finding reasons NOT to ship (`critical`, `high`, `medium`, `low`). | `products/<id>/audit/audit.json`, `report.md` |
| **`distribution`** | `pro` | Vets prospective creator partners and generates tailored collaboration packs. | `distribution/<id>/creator-shortlist.md` |

---

## 3. The 14-Stage Lifecycle & The 4 Human Approval Gates

The runtime state machine in `state.json` tracks project progression across 14 canonical stages:

```
[1. idle] ──► [2. discovery] ──► [3. research] ──► [4. validation] ──► [5. opportunity_selection]
                                                                                │
                                                                       ★ HUMAN APPROVAL GATE 1
                                                                                │
[9. packaging] ◄── [8. design] ◄── [7. product_build] ◄── [6. product_strategy] ◄┘
       │                 ▲
       │          ★ HUMAN APPROVAL GATE 3
       ▼                 │
[10. audit] (Critic)     │
       │                 │
       ├─► FAIL ──► [11. revision] (Remediate defects)
       │                 ▲
       ▼ PASS            │
★ HUMAN APPROVAL GATE 4 ──┘
       │
       ▼
[12. distribution] ──► [13. complete]
                         (or [14. blocked] if unresolved dependency)
```

### The 4 Human Approval Gates
1. **Gate 1 (Opportunity Selection):** Human approves the scored opportunity ID before product strategy begins.
2. **Gate 2 (Product Strategy & Specification):** Human approves product format, core promise, scope, and transformation.
3. **Gate 3 (Major Design Direction):** Human approves visual aesthetic, palette, typography, and component styling.
4. **Gate 4 (Final Product & Distribution Approval):** Human grants final sign-off after all red-team audit defects are resolved.

---

## 4. Workspace Setup

### Prerequisites
- **Google Antigravity CLI (`agy`)** installed and authenticated.
- **Git** installed on your operating system.
- Node.js / Python (optional, for running local scripts if required).

### Clone & Initialize
```bash
# Clone the template
git clone https://github.com/codinghubindia/ai-product-factory-template.git my-product-factory
cd my-product-factory
```

---

## 5. How to Start Antigravity

Launch the interactive Antigravity CLI from the repository root:

```bash
agy
```

The Antigravity CLI will detect workspace rules in `AGENTS.md` and custom agents in `.agents/agents/`.

---

## 6. How to Use the Master Agent

Once inside `agy`, select or invoke the Master Agent:
- Use `/agents` and select **`master`**, or run `agy --agent master`.
- The Master Agent is instructed to inspect `AGENTS.md`, `state.json`, and `memory/` on every invocation before taking action.
- The Master coordinates subagents via parallel background delegation, evaluates outputs against schemas, and automatically prompts you when reaching an Approval Gate using interactive questions.

---

## 7. How to Begin a Discovery Cycle

To kick off a fresh product discovery cycle, prompt the Master Agent with an industry, audience, or problem space:

> *"Master, start discovery in the creator economy space focusing on workflow bottlenecks for video editors handling client revisions."*

### What Happens Next
1. Master transitions `state.json` to `discovery`.
2. `scout` searches public forums (Reddit, communities) for authentic frustration language and logs findings to `memory/sources.csv` and `research/raw/`.
3. `research` maps out industry standards, benchmarks, and incumbent solutions into `research/verified/`.
4. `pain-miner`, `source-auditor`, and `competitor` synthesize the evidence into pain clusters and gap analyses.
5. `opportunity-analyst` scores opportunities via the 12-dimensional rubric in `system/scoring.md`.
6. Master stops and presents ranked opportunities at **Human Approval Gate 1** for your selection.

---

## 8. How Persistent Memory Works

The AI Product Factory preserves institutional memory across sessions using dedicated, append-oriented files in `memory/`:

- **`memory/sources.csv`:** Central source provenance ledger. Every claim made in research, specs, or sales copy must trace back to a valid source ID with assigned tier (1–5) and confidence.
- **`memory/opportunities.csv`:** Complete registry of all evaluated opportunities, tracking 12-dimensional scores, overall weighted score, and status.
- **`memory/decisions.md`:** Append-only log recording strategic choices, human approvals, architectural pivots, and audit waivers.
- **`memory/rejected-ideas.md`:** Catalog of dismissed ideas and explicit reasons for rejection, preventing agents from falling into repetitive discovery loops.
- **`memory/customers.json`:** Reusable customer profiles complying with `system/schemas/customer.schema.json`.
- **`state.json`:** Runtime state machine tracking current stage, active project IDs, and blocking issues.

---

## Repository Structure

```
├── .agents/agents/       # 13 Antigravity custom agent definitions
├── design/               # Per-product design systems and visual standards
├── distribution/         # Creator shortlists, vetting notes, and outreach packs
├── memory/               # Durable project memory (sources.csv, opportunities.csv, decisions.md, customers.json)
├── packaging/            # Commercial landing page copy, offer structures, and mockups
├── products/             # Product specifications, content drafts, assets, final deliverables, and audits
├── research/             # Raw evidence, verified domain notes, and synthesized problem clusters
│   ├── raw/              # Scrapes and unfiltered notes (.gitkeep)
│   ├── verified/         # Fact-checked benchmarks and claim audits (.gitkeep)
│   └── synthesis/        # Pain clusters and competitive gaps (.gitkeep)
│       └── opportunities/ # Individual opportunity dossiers (.gitkeep)
├── system/               # Schemas, transparent scoring rubrics, and detailed workflows
│   ├── schemas/          # JSON schemas for audits, customers, opportunities, products, sources
│   ├── workflows/        # Step-by-step stage execution guides
│   └── scoring.md        # 12-dimensional weighted scoring system & rubrics
├── state.json            # Runtime state machine tracking current lifecycle stage and blockers
├── AGENTS.md             # Master governing constitution and epistemic rules
└── README.md             # Canonical project documentation and guide
```

---

## License

MIT License. Free to use, adapt, and build upon.
