# AI Product Factory

An autonomous, disciplined multi-agent system designed to discover empirical customer pain, validate commercial viability, engineer high-utility digital products, establish authentic creative concepts, curate licensed visual assets, enforce publication-grade taste standards, and prepare creator-driven distribution.

Operated via the **Antigravity CLI** (`agy`).

---

## 1. Factory Architecture

The factory orchestrates **23 specialized worker agents** under the sovereign direction of the **Master Agent**, organized across 6 functional hubs.

```mermaid
flowchart TD
    User["Human Operator (Gatekeeper)"] <--> Master["Master Orchestrator (State & Quality Custodian)"]

    subgraph Hub1["1. Discovery & Validation"]
        Scout["scout"] --> Research["research"]
        Research --> Auditor["source-auditor"]
        Auditor --> Miner["pain-miner"]
        Miner --> Comp["competitor"]
        Comp --> OppAnalyst["opportunity-analyst"]
    end

    subgraph Hub2["2. Strategy & Creative Concept"]
        Strat["product-strategist"] --> CreativeDir["creative-director"]
        CreativeDir --> Arch["solution-architect"]
    end

    subgraph Hub3["3. Engineering & Assets"]
        DesignDir["design-director"]
        AssetDir["asset-director"]
        ProdBuilder["product-builder"]
        SoftBuilder["software-builder"]
        ArtBuilder["artifact-builder"]
    end

    subgraph Hub4["4. Quality & Taste Audit"]
        SoftQA["software-qa"]
        ArtQA["artifact-qa"]
        TasteRev["taste-reviewer"]
        Critic["critic (Red Team)"]
    end

    subgraph Hub5["5. Merchandising & Distribution"]
        MktgStrat["marketing-strategist"]
        Packaging["packaging"]
        RelEng["release-engineer"]
        Distrib["distribution"]
    end

    Master --> Hub1
    Hub1 --> Master
    Master --> Hub2
    Hub2 --> Master
    Master --> Hub3
    Hub3 --> Hub4
    Hub4 --> Master
    Master --> Hub5
    Hub5 --> Master
```

The Master Agent enforces state transitions recorded in `state.json`, durable repository memory (`memory/`), and four mandatory human approval gates using interactive decision prompts.

---

## 2. Creator-Led Opportunity Discovery

Raw signals are harvested from verbatim discussions and filtered through a multi-stage evidence sieve before human selection.

```mermaid
flowchart LR
    A["Raw Web Signal (Reddit, GitHub, Reviews)"] --> B["source-auditor (Provenance Tiering 1-5)"]
    B --> C["pain-miner (JTBD & Friction Clusters)"]
    C --> D["competitor (Incumbent Gap Analysis)"]
    D --> E["opportunity-analyst (12-Dimension Scoring)"]
    E --> F["memory/opportunities.csv"]
    F --> G["GATE 1: Human Approval (Opportunity Selection)"]
```

- **Verbatim Evidence:** Every pain hypothesis requires direct quotations from practitioners.
- **Provenance Tiering:** Sources must meet Tier 1 (primary documentation) or Tier 2 (practitioner consensus) standards; anonymous blog hearsay is rejected.
- **Transparent Scoring:** Opportunities are ranked across 12 commercial and technical dimensions including Pain Severity, Market Viability, and Demonstration Feasibility.

---

## 3. Product Modality Selection

The factory rejects the assumption that every digital product should be a PDF or an ebook. It systematically evaluates three solution levels across 21+ supported modalities:

```mermaid
flowchart TD
    In["Validated Opportunity (Gate 1 Approved)"] --> Eval["product-strategist (Modality Evaluation)"]

    Eval --> OptA["Level 1: Simplest Valid Solution (Checklist, Model, SOP Playbook)"]
    Eval --> OptB["Level 2: Best CX Solution (Interactive PWA, Responsive Calculator, Tool)"]
    Eval --> OptC["Level 3: Higher-Complexity Solution (Full-Stack Web App, Native Mobile, API)"]

    OptA --> Select["Decision Gate: Select Simplest Mechanism that Delivers Full Transformation"]
    OptB --> Select
    OptC --> Select

    Select --> Spec["products/product_id/specification.json"]
    Spec --> Gate2["GATE 2: Human Approval (Modality & Strategy)"]
```

Supported modalities include:
- **Documents & Publishing:** Executive Playbooks, Manuals, Whitepapers, Workbooks.
- **Templates & Calculators:** Financial Models, Spreadsheets, Diagnostic Rubrics.
- **Software Applications:** Progressive Web Apps, Single-Page Apps, CLI Utilities, Desktop Tools.
- **Backend & Data:** REST APIs, Curated SQLite Databases, Automation Scripts, Webhooks.
- **Hybrid Suites:** Multi-tier coordinated bundles combining software, playbooks, and templates.

---

## 4. Creative Concept & Signature Mechanism Layer

Before visual design or software construction, the `creative-director` establishes the product's emotional core, visual metaphor, and proprietary mechanism.

```mermaid
flowchart TD
    Strategy["Product Strategy (Target Audience & Transformation)"] --> Concept["creative-director (Creative Product Concept)"]

    subgraph CoreConcept["Creative Dimensions"]
        Personality["Product Personality & Archetype"]
        Metaphor["Visual Metaphor & Mental Model"]
        Mechanism["Signature Mechanism (Proprietary Engine)"]
        Wow["Customer Wow Moment (TTFR < 180s)"]
        World["Visual World (Palette, Typography, Texture)"]
    end

    Concept --> CoreConcept
    CoreConcept --> Doc["products/product_id/creative-concept.md"]
    Doc --> Gate3["GATE 3: Human Approval (Major Design System)"]
```

- **The Signature Mechanism:** Every flagship deliverable must engineer an internal engine (Diagnostic Sieve, 90-Day Cadence, Scoring Rubric, or Decision Matrix) that can be demonstrated on video in under 60 seconds.
- **Customer Wow Moment:** The Time to First Useful Result (TTFR) must occur within 180 seconds of opening the deliverable, delivering an immediate micro-win without setup friction.

---

## 5. Visual Asset Generation & Provenance Pipeline

Visual assets are engineered functional components governed by a 13-step production pipeline and cataloged in a formal manifest.

```mermaid
flowchart LR
    Req["Asset Requirement (Role, Placement, Aspect Ratio)"] --> Continuity["Check Visual Continuity (Palette, Lighting, Texture)"]
    Continuity --> Gen["Generate (generate_image) or Source Licensed Vector"]
    Gen --> Rights["Audit License Status (CC0, MIT, Factory Original)"]
    Rights --> IsoQA["Isolation QA (Artifacts, Dimensions, DPI)"]
    IsoQA --> Manifest["Catalog in asset-manifest.json (17 Attributes)"]
    Manifest --> Integrate["Embed in Deliverable (HTML, PDF, App)"]
    Integrate --> LayoutQA["In-Context Layout QA"]
```

- **Zero Whitespace Fillers:** Visual assets are generated only to clarify complex architecture, establish visual anchors, or demonstrate product mechanics.
- **Visual Continuity:** All assets within a product adhere to identical lighting, perspective, rendering style, and semantic color tokens.
- **100% Provenance:** Every asset records its generator prompt or canonical source URL, licensing status, and dimensions in `products/<product_id>/assets/asset-manifest.json`.

---

## 6. Product Build, Testing & Usability QA

Products are compiled into real, executable physical files and runtimes, followed by multi-stage automated testing.

```mermaid
flowchart TD
    Design["Design Tokens & Layout Grid"] --> Builders["Builders (product-builder, software-builder, artifact-builder)"]

    subgraph BuildOutputs["Real Production Deliverables"]
        HTML["Publication HTML & ReportLab PDF"]
        XLSX["Native openpyxl Spreadsheets"]
        Code["Runnable Codebase & Dependency Manifest"]
    end

    Builders --> BuildOutputs

    BuildOutputs --> FuncQA["Functional QA (software_runner.py & Unit Tests)"]
    BuildOutputs --> FormulaQA["Usability QA (template_usability_tester.py)"]
    BuildOutputs --> LinkQA["Link Integrity (link_checker.py)"]
    BuildOutputs --> DiffQA["Visual Regression (visual_regression_diff.py)"]

    FuncQA --> QAReport["Audit Reports in products/product_id/audit/"]
    FormulaQA --> QAReport
    LinkQA --> QAReport
    DiffQA --> QAReport
```

- **Editorial Standards:** Books and guides adhere to the 24 Editorial Dimensions, 45–75 character line measures, drop caps, and 22mm print binding gutters.
- **Handwriting Ergonomics:** Workbooks feature true 8.0mm–9.5mm (24pt–28pt) rule spacing and 16px checkboxes.
- **Zero Formula Errors:** Spreadsheets are scanned for `#REF!`, `#DIV/0!`, `#VALUE!`, frozen panes, and explicit currency/percentage formatting.

---

## 7. The 6-Part Premium Review Stack

Before human release approval, the product must pass all six independent evaluation layers.

```mermaid
flowchart TD
    Deliv["Finished Deliverable & Packaging Suite"] --> Stack["The 6-Part Review Stack"]

    subgraph Reviews["Review Dimensions"]
        R1["1. UTILITY REVIEW (Functional Completeness & Test Passing)"]
        R2["2. DESIGN REVIEW (Grid Discipline & Typography Hierarchy)"]
        R3["3. TASTE REVIEW (Restraint, Anti-AI-Slop, Niche Authenticity)"]
        R4["4. PSYCHOLOGY REVIEW (TTFR < 180s, Zero Dark Patterns)"]
        R5["5. COMMERCIAL REVIEW (Price-to-Craftsmanship Justification)"]
        R6["6. CREATOR FIT REVIEW (60-Second Live Demonstration Test)"]
    end

    Stack --> Reviews
    Reviews --> Critic["critic (Adversarial Red-Team Sign-Off)"]
    Critic --> Gate4["GATE 4: Human Approval (Final Release & Distribution)"]
```

- **Taste Invariant:** A product fails taste review if a practitioner would judge it to look like generic, uninspired AI output.
- **Absolute Ban on Dark Patterns:** Zero fake scarcity, zero countdown timers, zero fabricated social proof, and zero hidden costs.

---

## 8. Creator-Audience Marketing Funnel

Marketing assets emerge directly from the product's signature mechanism and verified transformation.

```mermaid
flowchart LR
    Hook["1. Creator Hook (Pattern Interrupt)"] --> Recog["2. Problem Recognition (Shared Pain)"]
    Recog --> Demo["3. 60s Video Demo (Signature Mechanism in Action)"]
    Demo --> Proof["4. Empirical Proof (Sources & Benchmarks)"]
    Proof --> Land["5. Clean Landing Page (Zero Deception)"]
    Land --> Checkout["6. Transparent Checkout (No Hidden Fees)"]
    Checkout --> TTFR["7. First Value in < 180s"]
    TTFR --> Share["8. Reusable Output Shared with Team"]
```

- **The 60-Second Rule:** If a product cannot be demonstrated live on screen in under 60 seconds, its transformation is refined until it can.
- **Creator-Specific Presentation Layer:** The core product engine remains modular while presentation layers customize welcome notes, niche example data, and partner branding.

---

## 9. Product Merchandising & Offer Ecosystem

The factory structures deliverables into calibrated commercial tiers based on customer economics rather than forced funnels.

```mermaid
flowchart TD
    Entry["Free Entry Asset (Interactive Diagnostic / 1-Page Checklist)"] --> LowTicket["Low-Ticket Utility ($19-$49: Tactical Template / Playbook)"]
    LowTicket --> Core["Core Flagship Product ($79-$199: Complete Operating System)"]
    Core --> Bundle["Premium Professional Bundle ($249-$499: Suite + Architecture Blueprints)"]
    Core -.-> Continuity["Optional Software / Data Continuity (Justified Compute/Updates Only)"]
```

Every offer documents customer problem, promise, transformation, contents, empirical proof, reason to believe, objection refutations, and next logical offer in `merchandising.json`.

---

## 10. Repository Structure

```text
├── .agents/
│   ├── agents/              # 23 specialized agent prompts
│   └── skills/              # Reusable engineering and creative skills
├── design/                  # Design systems and visual continuity specifications
├── memory/                  # Persistent repository memory (sources.csv, opportunities.csv)
├── packaging/               # Landing pages, creator briefs, and offer structures
├── products/                # Product specifications, content, software, and final builds
├── research/                # Raw community signals, verified evidence, and synthesis
├── system/
│   ├── schemas/             # Authoritative JSON schemas (product, asset, audit, etc.)
│   ├── scripts/             # Deterministic Python build and verification tools
│   ├── vendor/              # Local, reproducible dependencies (openpyxl, reportlab, pillow)
│   └── workflows/           # Canonical stage-gate operating workflows
├── templates/               # Reusable starter architectures for all product modalities
├── AGENTS.md                # Governing workspace constitution
├── README.md                # System overview and architecture
└── state.json               # Single source of truth for runtime project state
```

---

## 11. Command Line Interface Reference

The factory operates via the `system/scripts/` toolchain:

```bash
# 1. Inspect host environment and tooling
python system/scripts/tooling_manager.py --inspect

# 2. Compile publication-grade document and PDF with outline bookmarks
python system/scripts/pdf_compiler.py --html <path_to_html> --output <path_to_pdf>

# 3. Audit spreadsheet formulas, error tokens, and frozen panes
python system/scripts/template_usability_tester.py --input <path_to_xlsx_or_csv>

# 4. Audit visual asset manifest, licensing, and image dimensions
python system/scripts/asset_pipeline.py --manifest <path_to_asset_manifest.json>

# 5. Audit deliverables for generic AI clichés, neon gradients, and formatting
python system/scripts/taste_checker.py --input <path_to_file>

# 6. Audit internal routes, hyperlinks, and button actions
python system/scripts/link_checker.py <target_directory>

# 7. Check for layout drift and visual regressions between builds
python system/scripts/visual_regression_diff.py --base <baseline.pdf> --new <new.pdf>

# 8. Inspect compiled artifacts for placeholders and header validity
python system/scripts/artifact_inspector.py <target_directory>
```

---

## 12. Licensing & Governance

All agents operating in this repository are bound by the constitution in [AGENTS.md](AGENTS.md). All product claims, benchmarks, and citations must trace to empirical records in `memory/sources.csv`.
