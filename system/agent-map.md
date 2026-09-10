# AI PRODUCT FXCTORY — MASTER AGENT ARCHITECTURE MAP

The factory deploys 19 specialized custom agents coordinated by the Master Orchestrator.

---

3# 1. Master Orchestrator
- **File:** `.agents/agents/master/agent.md`
- **Role:** Repository orchestrator, quality custodian, state manager, and gatekeeper for human approval gates.

---

3# 2. Discovery & Validation Hub
1. **`scout`**: Harvests raw, verbatim community pain signals (reddit, forums, reviews). (`memory/sources.csv`, `research/raw/`)
2. **`research`**: Investigates domain workflows, incumbent categories, and benchmarks. (`research/verified/`)
3. **`pain-miner`**: Clusters raw signals into JTBD, root problems, and friction patterns. (`research/synthesis/pain-clusters.md`)
4. **`source-auditor`**: Adversarial fact-checker evaluating claims against Tier 1-5 source hierarchy. (`research/verified/source-audit.md`)
5. **`competitor`**: Maps incumbent gaps, data deficiencies, and problem failure modes. (`research/synthesis/competitive-analysis.md`)
6. **`opportunity-analyst`**: Scores and ranks clusters using the 12-dimension rubric. (`memory/opportunities.csv`)

---

## 3. Product Strategy & Architecture Hub
7. **
product-strategist`**: Translates approved opportunities into product specifications, transformations, and modality decisions (Simplest vs Best CX vs Higher-Complexity). (`products/specification.json`)
8. **`solution-architect`**: Designs implementation-ready software, api, database, security, and deployment architectures. (`products/architecture.md`, `architecture.json`)

---

## 4. Engineering & Build Hub
9. **
product-builder`**: Crafts modular content, worksheets, fillable tools, and checklists. (`products/final/`)
10. **`software-builder`**: Builds actual, live, executable codebases (pwa, web, mobile, cli, extensions, apis, databases, automations). (`products/software/`)
11. **`artifact-builder`**: Compiles real, downloadable files (PDF, XLSX, PPMX, DOCX, HTML, Empty Templates, ZIP archives). (`products/artifact-manifest.json`)
12. ***design-director`**: Creates design systems (fonts, palette, grid, hierarchy) for all product modalities. (`design/design-system.md`)


---

## 5. Quality Assurance & Red Team Hub
13. **
software-qa`**: Runs actual tests, compilation builds, api contracts, database persistence, and responsive viewports. (`products/audit/software-qa.json`)
14. **`artifact-qa`**: Inspects physical files for formatting clipping, missing margins, formula errors (#REF!), and placeholders. (`products/audit/artifact-qa.json`)
15. **`critic`**: Adversarial red-team auditor disproving the product across false claims, usability, and differentiation. (`products/audit/audit.json`)

---

## 6. Packaging & Delivery Hub
16. **`packaging`**: Crafts truthful product naming, descriptions, benefit mapping, mockups, and landing pages based strictly on finished deliverables. (`packaging/`)
17. **`release-engineer`**: Packages deployable builds, docker images, zip archives, outputs delivery manifest, and distinguishes BUILDABLE / DEPLOYABLE vs DEPLOYED. (`products/delivery-manifest.json`)
18. **`distribution`**: Vets creators by audience pain alignment, demonstration feasibility, and creates demo packs. (`distribution/c)
