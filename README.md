# AI Product Factory

An autonomous, multi-agent digital product studio operating inside **Google Antigravity CLI (`agy`)**.

The AI Product Factory converts empirical customer pain into commercially viable, high-utility digital products (templates, frameworks, workbooks, guides, toolkits), crafts functional design systems, generates truthful packaging copy, performs adversarial red-team quality audits, and prepares targeted creator-driven distribution campaigns.

---

## 1. What This Project Is

The AI Product Factory is a production-ready repository template for disciplined multi-agent orchestration. Instead of generating generic, ungrounded content with a single prompt, the factory uses a team of 13 specialized agents coordinated by a Master orchestrator. 

All agents operate under strict epistemic invariants, write durable artifacts to the repository, adhere to JSON schemas, and pause for human validation at four strategic decision gates.

### The Problem It Solves

* **Hallucinated Research & Market Demand:** Many AI workflows mistake keyword search volume or social mentions for true willingness to pay. The factory requires primary source provenance registered in `memory/sources.csv` before scoring any opportunity.
* **Superficial "AI Filler":** Conventional LLM products often output shallow lists and generic advice. The factory enforces concrete frameworks, fillable worksheets, decision trees, and step-by-step implementation workflows.
* **Exaggerated Packaging Claims:** Marketing copy often promises transformations that the product does not deliver. The packaging agent works exclusively from inspected, completed deliverables.
* **Lack of Quality Control:** The factory includes an independent adversarial red-team auditor (`critic`) that actively searches for reasons *not* to ship before release.
* **Context Window Bloat:** Rather than running one massive monolithic prompt, 13 scoped custom agents execute targeted roles with dedicated tool sets.

---

## 2. Architecture & Multi-Agent Orchestration

The workspace organizes 13 custom agents into three functional hubs under the leadership of the Master Agent:

### Overall AI Product Factory Architecture

The following diagram illustrates the relationship between the Master Agent, the functional worker hubs, persistent memory, and final outputs:

```mermaid
flowchart TD
    User(["User / Human Operator"]) -->|Goal & Directives| Master["Master Agent\n(Orchestrator & State Custodian)"]
    
    subgraph DiscoveryHub ["1. Discovery & Validation Hub"]
        Scout["scout\n(Raw Signals)"]
        Research["research\n(Context & Benchmarks)"]
        PainMiner["pain-miner\n(JTBD & Problem Clusters)"]
        SourceAuditor["source-auditor\n(Fact-Checking & Provenance)"]
        Competitor["competitor\n(Gap Analysis & Pricing)"]
        OppAnalyst["opportunity-analyst\n(12-Dimension Scoring)"]
    end

    subgraph BuildHub ["2. Product Engineering Hub"]
        Strategist["product-strategist\n(Blueprint & Specs)"]
        Builder["product-builder\n(Tools & Deliverables)"]
        Design["design-director\n(Visual System)"]
        Packaging["packaging\n(Truthful Copy & Mockups)"]
        Critic["critic\n(Adversarial Red Team)"]
    end

    subgraph DistHub ["3. Distribution Hub"]
        DistAgent["distribution\n(Creator Vetting & Outreach)"]
    end

    subgraph MemoryLayer ["Durable Memory & State"]
        StateFile[("state.json\nRuntime State")]
        SourcesLedger[("memory/sources.csv\nEvidence Provenance")]
        OppLedger[("memory/opportunities.csv\nScored Concepts")]
        DecisionLog[("memory/decisions.md\nAppend-Only Log")]
    end

    Master <--> DiscoveryHub
    Master <--> BuildHub
    Master <--> DistHub
    Master <--> MemoryLayer
    User <-->|Approval Gates| Master
```

*Text Summary:* The Master Agent acts as the central coordinator between the user, the Discovery Hub, the Product Engineering Hub, the Distribution Hub, and persistent repository memory.

---

### Multi-Agent Orchestration Model

The Master Agent coordinates workers using Antigravity's subagent delegation mechanism (`invoke_subagent`). Independent tasks run concurrently, while dependent tasks wait for prerequisite artifacts:

```mermaid
flowchart TD
    StartStep["Stage Initiation"] --> CheckState["Read state.json & AGENTS.md"]
    CheckState --> IdentifyTasks{"Task Independence?"}
    
    IdentifyTasks -->|Independent Tasks| ConcurrentExec["Launch Subagents Concurrently\n(e.g., pain-miner, source-auditor, competitor)"]
    IdentifyTasks -->|Sequential Tasks| SeqWait["Wait for Prerequisite Artifact\n(e.g., wait for spec before build)"]
    
    ConcurrentExec --> Consolidate["Consolidate Returned Findings"]
    SeqWait --> Consolidate
    
    Consolidate --> VerifyContradictions{"Contradictions or\nWeak Evidence?"}
    VerifyContradictions -->|Discrepancy Found| Challenge["Challenge Worker / Request Deepening"]
    Challenge --> ConcurrentExec
    
    VerifyContradictions -->|Consistent & Verified| ApprovalGate{"Human Approval Gate\nRequired?"}
    ApprovalGate -->|Yes| AskUser["Halt & Prompt Human Operator\n(ask_question)"]
    ApprovalGate -->|No| AdvanceState["Update state.json & Advance Stage"]
    
    AskUser -->|Approved| AdvanceState
    AskUser -->|Revision Requested| ModifyScope["Adjust Directives & Rerun"]
    ModifyScope --> CheckState
```

*Text Summary:* The Master checks prerequisites, runs independent subagents concurrently, consolidates outputs, cross-checks for contradictions, and pauses for explicit human approval before advancing stages.

---

## 3. Agent Roster & Roles

All 13 custom agents are defined in `.agents/agents/{name}/agent.md`:

| Agent Name | Model | Type | Role & Responsibility | Key Deliverables |
| :--- | :--- | :--- | :--- | :--- |
| **`master`** | `pro` | Main / Subagent | Repository orchestrator, human gatekeeper, state manager, and final quality custodian. | `state.json`, `memory/decisions.md` |
| **`scout`** | `flash` | Worker | Discovers unprompted customer pain signals across Reddit, forums, and reviews. | `research/raw/`, `memory/sources.csv` |
| **`research`** | `pro` | Worker | Investigates domain context, industry workflows, incumbent models, and benchmarks. | `research/verified/` |
| **`pain-miner`** | `pro` | Worker | Clusters raw signals into jobs-to-be-done, root problems, and workarounds. | `research/synthesis/pain-clusters.md` |
| **`source-auditor`**| `pro` | Worker | Adversarial fact-checker auditing claims against the 5-tier source hierarchy. | `research/verified/source-audit.md` |
| **`competitor`** | `pro` | Worker | Maps incumbents, customer complaints, and churn drivers to isolate market gaps. | `research/synthesis/competitive-analysis.md` |
| **`opportunity-analyst`**| `pro` | Worker | Evaluates clusters using the 12-dimensional weighted rubric in `system/scoring.md`. | `memory/opportunities.csv`, `opportunities/<id>.md` |
| **`product-strategist`**| `pro` | Worker | Formulates full product specification, unique mechanism, format, and transformation. | `products/<id>/specification.json`, `strategy.md` |
| **`product-builder`**| `pro` | Worker | Constructs actionable content, fillable templates, checklists, and tools. | `products/<id>/final/` |
| **`design-director`**| `pro` | Worker | Creates and enforces visual systems adhering to the 6 Pillars of Premium Design. | `design/<id>/design-system.md` |
| **`packaging`** | `pro` | Worker | Crafts truthful sales copy, offer stack, bonuses, and landing page content. | `packaging/<id>/` |
| **`critic`** | `pro` | Worker | Red-team auditor finding reasons NOT to ship (`critical`, `high`, `medium`, `low`). | `products/<id>/audit/audit.json`, `report.md` |
| **`distribution`** | `pro` | Worker | Vets prospective creator partners and generates tailored collaboration packs. | `distribution/<id>/creator-shortlist.md` |

---

## 4. End-to-End Product Workflow

The factory runtime state machine tracks progression across **14 canonical stages**:

```mermaid
flowchart LR
    S1["1. idle"] --> S2["2. discovery"]
    S2 --> S3["3. research"]
    S3 --> S4["4. validation"]
    S4 --> S5["5. opportunity_selection\n★ GATE 1"]
    
    S5 --> S6["6. product_strategy\n★ GATE 2"]
    S6 --> S7["7. product_build"]
    S7 --> S8["8. design\n★ GATE 3"]
    S8 --> S9["9. packaging"]
    S9 --> S10["10. audit\n(Critic Red Team)"]
    
    S10 -->|FAIL| S11["11. revision\n(Fix Defects)"]
    S11 --> S7
    
    S10 -->|PASS| S12["12. distribution\n★ GATE 4"]
    S12 --> S13["13. complete"]
    
    S2 -.->|Blocker| S14["14. blocked"]
    S6 -.->|Blocker| S14
    S10 -.->|Blocker| S14
```

*Text Summary:* Progression moves linearly from discovery through research, validation, opportunity selection, strategy, build, design, packaging, and audit. If the audit fails, execution loops back to revision until all critical/high issues are cleared.

---

## 5. Opportunity Discovery Pipeline

The discovery cycle follows a strict empirical progression from raw signals to human selection:

```mermaid
flowchart TD
    Seed["User Topic / Domain Seed"] --> ScoutStep["scout:\nHarvest public complaints & friction points\n(Reddit, forums, reviews)"]
    ScoutStep --> ResearchStep["research:\nMap domain workflows & benchmarks\n(Tier 1 & 2 authoritative sources)"]
    
    ScoutStep --> SourcesLog[("Log primary URLs in\nmemory/sources.csv")]
    ResearchStep --> SourcesLog
    
    ScoutStep --> PainStep["pain-miner:\nCluster friction into JTBD & root problems\n(research/synthesis/pain-clusters.md)"]
    ResearchStep --> GapStep["competitor:\nAnalyze incumbent flaws & pricing gaps\n(research/synthesis/competitive-analysis.md)"]
    SourcesLog --> AuditStep["source-auditor:\nVerify claim support & freshness\n(research/verified/source-audit.md)"]
    
    PainStep --> ScoreStep["opportunity-analyst:\nApply 12-dimension weighted scoring\n(system/scoring.md)"]
    GapStep --> ScoreStep
    AuditStep --> ScoreStep
    
    ScoreStep --> CandidateRegistry[("Update memory/opportunities.csv &\ncreate dossiers in opportunities/")]
    CandidateRegistry --> Gate1{{"★ HUMAN APPROVAL GATE 1\nUser selects opportunity ID"}}
    Gate1 --> ApprovedOpp["Approved Opportunity -> Product Strategy"]
```

*Text Summary:* Problem signals gathered by `scout` and `research` are processed into pain clusters by `pain-miner`, audited by `source-auditor`, and matched with competitor gaps by `competitor`. `opportunity-analyst` then scores and ranks them for human approval.

---

## 6. Product Creation Pipeline

Once an opportunity is approved, it is transformed into an engineered digital deliverable:

```mermaid
flowchart TD
    ApprovedOpp["Approved Opportunity\n(From Gate 1)"] --> StrategistStep["product-strategist:\nDraft product specification & positioning\n(specification.json & strategy.md)"]
    StrategistStep --> Gate2{{"★ HUMAN APPROVAL GATE 2\nUser approves format, promise, and scope"}}
    
    Gate2 --> BuilderPlan["product-builder:\nCreate content plan & module architecture\n(products/<id>/content/)"]
    BuilderPlan --> BuilderBuild["product-builder:\nWrite high-utility frameworks, fillable worksheets,\ntools, and decision trees"]
    
    Gate2 --> DesignStep["design-director:\nEstablish design system: typography, palette,\ngrid, component styles (design-system.md)"]
    DesignStep --> Gate3{{"★ HUMAN APPROVAL GATE 3\nUser approves visual theme and aesthetic"}}
    
    BuilderBuild --> Assemble["Assemble complete deliverables\n(products/<id>/final/)"]
    Gate3 --> ApplyDesign["Apply design system styling\nto final deliverables"]
    Assemble --> ApplyDesign
    
    ApplyDesign --> PackagingStep["packaging:\nInspect actual finished deliverables;\ncraft truthful landing page copy, mockups, & offer"]
    PackagingStep --> AuditHandoff["Submit completed package to Critic"]
```

*Text Summary:* Product development proceeds from specification (`product-strategist`) to human approval, modular construction (`product-builder`), visual design system (`design-director`), assembly, and truthful packaging (`packaging`).

---

## 7. Quality Control & Revision Loop

The Critic agent acts as an independent red team. A deliverable cannot ship without passing this gate:

```mermaid
flowchart TD
    Deliverables["Completed Deliverables\n(final/, packaging/, design-system.md)"] --> CriticAudit["critic:\nAdversarial inspection across 12 dimensions\n(problem-fit, factual accuracy, usability, visual quality)"]
    
    CriticAudit --> GenReport["Generate audit.json & report.md\nCounts: critical, high, medium, low"]
    GenReport --> Evaluate{"Audit Status?"}
    
    Evaluate -->|FAIL:\ncritical > 0 or un-waived high > 0| RevisionStage["workflow.stage = 'revision'\nRoute defects to designated owners"]
    
    RevisionStage --> FactualFix["Factual / Usability issues\n-> product-builder"]
    RevisionStage --> VisualFix["Visual / Layout issues\n-> design-director"]
    RevisionStage --> CopyFix["Copy / Claim discrepancies\n-> packaging"]
    RevisionStage --> ScopeFix["Positioning / Structural gaps\n-> product-strategist"]
    
    FactualFix --> ReAudit["Re-run Critic Audit"]
    VisualFix --> ReAudit
    CopyFix --> ReAudit
    ScopeFix --> ReAudit
    ReAudit --> CriticAudit
    
    Evaluate -->|PASS:\n0 critical, 0 un-waived high| Gate4{{"★ HUMAN APPROVAL GATE 4\nUser signs off on final product"}}
    Gate4 --> DistWorkflow["Advance to Distribution Stage"]
```

*Text Summary:* The Critic inspects deliverables and classifies defects. Any critical or un-waived high defect triggers the revision loop, assigning fixes to the responsible agent before re-auditing.

---

## 8. Persistent Repository Memory

The factory preserves institutional memory across sessions using dedicated, structured files:

* **`state.json`:** Single source of truth for runtime project state, active stage, and blockers.
* **`memory/sources.csv`:** Central source provenance ledger. Every claim in research, specs, or sales copy must trace back to a valid source ID with assigned tier (1–5) and confidence.
* **`memory/opportunities.csv`:** Complete registry of all evaluated opportunities, tracking 12-dimensional scores, overall weighted score, and status.
* **`memory/decisions.md`:** Append-only log recording strategic choices, human approvals, architectural pivots, and audit waivers.
* **`memory/rejected-ideas.md`:** Catalog of dismissed ideas and explicit reasons for rejection, preventing repetitive discovery loops.
* **`memory/customers.json`:** Reusable customer profiles complying with `system/schemas/customer.schema.json`.

---

## 9. Strategic Human Approval Gates

The Master Agent operates with bounded autonomy. It halts and prompts the operator via `ask_question` at exactly four gates:

1. **Gate 1 — Opportunity Selection:** After opportunities are scored and ranked. The human selects the opportunity ID before product strategy begins.
2. **Gate 2 — Product Strategy & Specification:** After `specification.json` is generated. The human approves the product format, core promise, scope, and transformation.
3. **Gate 3 — Major Design Direction:** After `design-system.md` is drafted. The human approves the visual tone, palette, and typography before full visual formatting.
4. **Gate 4 — Final Product & Distribution Approval:** After all Critic audit issues are resolved. The human gives final approval before packaging release and creator outreach.

---

## 10. How Custom Agents Are Discovered

Antigravity CLI discovers custom agents by scanning the project workspace for `.agents/agents/{agent_name}/agent.md`.

For an agent to be discovered:
1. **Directory Structure:** Must reside in `.agents/agents/{name}/agent.md`.
2. **Valid YAML Frontmatter:** Must include standard fields:
   * `name`: Matching the folder identifier.
   * `description`: Explaining the agent's specialized role.
   * `tools`: List of valid Antigravity tool identifiers.
   * `subagent: true`: Allows the agent to be invoked via `invoke_subagent`.
   * `mainAgent: true` (for `master` only) or `mainAgent: false` (for workers).
   * `model`: Model tier (`pro`, `flash`, or `inherit`).
   * `commandExecutionPolicy: sandbox`: Standard execution security mode.

To verify discovery, run `/agents` inside the Antigravity CLI. All 13 custom agents will appear in the panel.

---

## 11. Workspace Setup & Installation

### Prerequisites
* **Google Antigravity CLI (`agy`)** installed and authenticated.
* **Git** installed on your system.

### Option A: Use as a GitHub Template (Recommended)
1. Click the **"Use this template"** button at the top of the GitHub repository.
2. Select **"Create a new repository"**.
3. Name your repository (e.g., `my-product-factory`) and clone it locally:
   ```bash
   git clone https://github.com/<your-username>/my-product-factory.git
   cd my-product-factory
   ```

### Option B: Clone Directly
```bash
git clone https://github.com/codinghubindia/ai-product-factory-template.git my-product-factory
cd my-product-factory
```

---

## 12. How to Start Antigravity & Begin a Project

1. **Launch Antigravity:**
   From the repository root, start the Antigravity CLI:
   ```bash
   agy
   ```

2. **Verify Agent Discovery:**
   Type `/agents` in the prompt. You should see `master` and all 12 worker agents listed.

3. **Select the Master Agent:**
   Select `master` from the panel, or start directly with:
   ```bash
   agy --agent master
   ```

4. **Initiate Product Discovery:**
   Provide a target domain, market, or audience pain point to the Master Agent:
   ```text
   Master, start discovery in the creator economy space focusing on workflow bottlenecks for video editors handling client revisions.
   ```

5. **Participate at Approval Gates:**
   The Master Agent will orchestrate the workers, harvest evidence, cluster pain, and halt at **Gate 1** with ranked opportunities for your approval.

---

## Repository Structure

```
├── .agents/agents/         # 13 Antigravity custom agent definitions
│   ├── master/agent.md     # Master orchestrator
│   ├── scout/agent.md      # Raw signal harvesting
│   ├── research/agent.md   # Domain & benchmark investigation
│   ├── pain-miner/agent.md # Problem clustering & JTBD
│   ├── source-auditor/agent.md # Evidence fact-checking
│   ├── competitor/agent.md # Competitor gap analysis
│   ├── opportunity-analyst/agent.md # 12-dimension scoring
│   ├── product-strategist/agent.md  # Product specification
│   ├── product-builder/agent.md     # Deliverables construction
│   ├── design-director/agent.md     # Visual design system
│   ├── packaging/agent.md           # Truthful sales copy & mockups
│   ├── distribution/agent.md        # Creator vetting & outreach
│   └── critic/agent.md              # Adversarial red-team audit
├── design/                 # Per-product design systems and visual standards
├── distribution/           # Creator shortlists, vetting notes, and outreach packs
├── memory/                 # Durable project memory
│   ├── sources.csv         # Evidence provenance registry
│   ├── opportunities.csv   # Scored opportunity candidates
│   ├── decisions.md        # Strategic decision log
│   ├── rejected-ideas.md   # Record of rejected concepts
│   └── customers.json      # Target customer persona profiles
├── packaging/              # Commercial landing page copy, offer structures, and mockups
├── products/               # Specifications, content drafts, assets, final deliverables, and audits
├── research/               # Raw evidence, verified domain notes, and synthesized problem clusters
│   ├── raw/                # Scrapes and unfiltered notes (.gitkeep)
│   ├── verified/           # Fact-checked benchmarks and claim audits (.gitkeep)
│   └── synthesis/          # Pain clusters and competitive gaps (.gitkeep)
│       └── opportunities/  # Individual opportunity dossiers (.gitkeep)
├── system/                 # Schemas, transparent scoring rubrics, and detailed workflows
│   ├── schemas/            # JSON schemas (audit, customer, opportunity, product, source)
│   ├── workflows/          # Execution workflows (discovery, product-build, distribution)
│   └── scoring.md          # 12-dimensional weighted scoring system & rubrics
├── state.json              # Runtime state machine tracking current lifecycle stage and blockers
├── AGENTS.md               # Master governing constitution and epistemic rules
└── README.md               # Canonical project documentation and guide
```

---

## License

MIT License. Free to use, adapt, and build upon.

