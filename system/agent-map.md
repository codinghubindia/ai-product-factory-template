# AI PRODUCT FACTORY — MASTER AGENT ARCHITECTURE MAP

The factory deploys **23 specialized custom agents** coordinated by the Master Orchestrator across 6 functional hubs.

---

## 1. Master Orchestrator
- **File:** `.agents/agents/master/agent.md`
- **Role:** Repository orchestrator, quality custodian, state manager, dispute resolver, and gatekeeper for the 4 mandatory human approval gates.

---

## 2. Discovery & Validation Hub
1. **`scout`**: Harvests raw, verbatim community pain signals (Reddit, forums, reviews, GitHub issues). (`memory/sources.csv`, `research/raw/`)
2. **`research`**: Investigates domain workflows, incumbent categories, and quantitative benchmarks. (`research/verified/`)
3. **`pain-miner`**: Clusters raw signals into JTBD, root problems, and friction patterns. (`research/synthesis/pain-clusters.md`)
4. **`source-auditor`**: Adversarial fact-checker evaluating claims against 5-tier source hierarchy. (`research/verified/source-audit.md`)
5. **`competitor`**: Maps incumbent gaps, data deficiencies, and alternative failure modes. (`research/synthesis/competitive-analysis.md`)
6. **`opportunity-analyst`**: Scores and ranks clusters using the 12-dimension rubric. (`memory/opportunities.csv`)

---

## 3. Product Strategy & Creative Direction Hub
7. **`product-strategist`**: Translates approved opportunities into product specifications, transformations, modality decisions, and signature mechanism scope. (`products/<product_id>/specification.json`)
8. **`creative-director`**: Owns creative concept, product personality, emotional arc, visual worldbuilding, visual metaphor, and customer wow moments. (`products/<product_id>/creative-concept.md`)
9. **`solution-architect`**: Designs implementation-ready software, API, database, security, and deployment architectures. (`products/<product_id>/architecture.md`, `architecture.json`)

---

## 4. Engineering & Visual Assets Hub
10. **`product-builder`**: Crafts modular content, worksheets, fillable tools, and editorial chapters. (`products/<product_id>/content/`)
11. **`software-builder`**: Builds actual, live, executable codebases (PWA, web, mobile, CLI, extensions, APIs, databases, automations). (`products/<product_id>/software/`)
12. **`artifact-builder`**: Compiles real, downloadable files (PDF, XLSX, PPTX, DOCX, HTML, SQLite, ZIP archives). (`products/<product_id>/final/`, `artifact-manifest.json`)
13. **`design-director`**: Creates design systems (fonts, palette, 8px/4px grid, hierarchy) and CSS tokens for all product modalities. (`design/<product_id>/design-system.md`)
14. **`asset-director`**: Owns image/visual asset planning, generation, licensing rights verification, isolation QA, and asset manifest cataloging. (`products/<product_id>/assets/asset-manifest.json`)

---

## 5. Quality Assurance, Taste & Red Team Hub
15. **`software-qa`**: Executes the 12-step software testing protocol, automated test suites, link audit, and responsive viewports. (`products/<product_id>/audit/software-qa.json`)
16. **`artifact-qa`**: Deep inspection of physical files for formatting, clipping, margin padding, formula errors (`#REF!`), and placeholders. (`products/<product_id>/audit/artifact-qa.json`)
17. **`taste-reviewer`**: Independent aesthetic gatekeeper evaluating visual restraint, editorial maturity, niche authenticity, and eliminating generic AI appearance. (`products/<product_id>/audit/taste-review.md`)
18. **`critic`**: Adversarial red-team auditor disproving the product across buyer objections, usability, false claims, differentiation, and commercial viability. (`products/<product_id>/audit/audit.json`)

---

## 6. Commercial Experience & Distribution Hub
19. **`marketing-strategist`**: Owns ethical customer psychology, product merchandising, commercial offer architecture, positioning, and creative marketing funnels. (`products/<product_id>/merchandising.json`)
20. **`packaging`**: Crafts truthful product naming, descriptions, benefit mapping, mockups, and landing pages based strictly on finished deliverables. (`packaging/<product_id>/`)
21. **`release-engineer`**: Packages deployable builds, ZIP archives, outputs delivery manifest, and enforces production readiness classification. (`products/<product_id>/delivery-manifest.json`)
22. **`distribution`**: Vets creators by audience pain alignment, demonstration feasibility, and creates demonstration packs and creator-specific presentation versions. (`distribution/<product_id>/`)
