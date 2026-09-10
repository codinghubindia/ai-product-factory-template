# AI PRODUCT FACTORY — PRODUCT MODALITY ENGINE & TAXONOMY

This document defines the canonical taxonomy of digital product modalities supported by the AI Product Factory. The factory never presumes that every solution is a document or report. Instead, the factory selects the appropriate product modality and architecture based strictly on:
\\text{CUSTOMER PROBLEM} \\longrightarrow \\text{DESIRED TRANSFORMATION} \\longrightarrow \\text{OPPORTUNITY} \\longrightarrow \\text{PRODUCT STRATEGY} \\longrightarrow \\text{PRODUCT MODALITY}

The factory prefers the simplest solution capable of delivering the required customer transformation with high fidelity and low operational friction.

---

## 1. Modality Categories & Artifact Profiles

### 1. DOCUMENTS
- **Supported Formats:** PDF, DOCX, EPUB, Markdown, HTML documents, workbooks, manuals, playbooks, reports, guides, checklists, planners.
- **When to Use:** When the transformation requires conceptual mastery, mental models, decision frameworks, compliance checklists, or linear reading/instruction.
- **Output Artifacts:** Formatted .pdf, editable .docx, e-reader .epub, clean structured .md, standalone single-file .html.
- **Builder / Roles:** product-strategist, product-builder, design-director, rtifact-builder, rtifact-qa.

### 2. TEMPLATES
- **Supported Formats:** Notion templates, Excel/spreadsheets, CSV structures, Google Sheets/Docs templates (when integration exists), Canva/Figma templates (when integration exists), presentation templates, website templates, email templates, proposal templates, CRM templates, project-management templates, workflow templates, database templates, AI prompt/workflow templates.
- **When to Use:** When the customer needs repeatable operational scaffolding, pre-configured data schemas, or standardized communication without building from scratch.
- **Output Artifacts:** Template files (.xlsx, .csv, .notion export, .json prompt pack, markdown schema, design template links/files).
- **Builder / Roles:** product-strategist, product-builder, design-director, rtifact-builder, rtifact-qa.

### 3. PRODUCTIVITY ARTIFACTS
- **Supported Formats:** XLSX, XLSM (macro-enabled, only where strictly justified with security audit), CSV, DOCX, PPTX, ODP (OpenDocument Presentation), PDF forms, printable packages, form packages.
- **When to Use:** When customers perform recurring numerical modeling, financial projections, client proposals, boardroom presentations, or standardized physical printing/paper forms.
- **Output Artifacts:** Validated workbook files (.xlsx), interactive slide decks (.pptx), fillable PDF forms.
- **Builder / Roles:** product-strategist, product-builder, rtifact-builder, rtifact-qa.

### 4. INTERACTIVE TOOLS
- **Supported Formats:** Calculators, estimators, pricing calculators, ROI calculators, scoring tools, assessments, quizzes, diagnostics, decision trees, planners, configurators, simulators, generators, converters, interactive checklists, dashboards, search tools, visualization tools.
- **When to Use:** When the user needs dynamic evaluation, personalized numerical outputs based on input variables, self-assessments, or instant algorithmic guidance.
- **Output Artifacts:** Self-contained client-side web apps (HTML/CSS/JS or React/Vue), standalone desktop widgets, or lightweight interactive embeds.
- **Builder / Roles:** product-strategist, solution-architect (if complex), software-builder, software-qa, rtifact-builder, rtifact-qa.

### 5. WEB APPLICATIONS & SITES
- **Supported Formats:** Static websites, landing pages, marketing websites, documentation sites, interactive websites, web applications, responsive web applications, Progressive Web Apps (PWAs), client portals, dashboards, directories, marketplaces, communities, authenticated applications, SaaS, micro-SaaS, subscription applications, database-backed applications.
- **When to Use:** When users require multi-device access, persistent remote data, real-time collaboration, continuous updates, user authentication, or server-side computation.
- **Output Artifacts:** Deployable static bundles (dist/), full-stack application repos, Dockerfiles, serverless deployment configs.
- **Builder / Roles:** product-strategist, solution-architect, design-director, software-builder, software-qa, 
elease-engineer.

### 6. MOBILE & TABLET
- **Supported Formats:** iOS applications, Android applications, cross-platform mobile apps (React Native, Flutter, Expo, Capacitor), phone applications, tablet-optimized applications, mobile web, PWAs.
- **When to Use:** When customer workflows occur on the move, require device sensors (camera, GPS, haptics), offline mobile access, or tablet-first touch/stylus interaction.
- **Output Artifacts:** PWA manifests/service workers, buildable mobile project repos, APK/AAB build configurations, Expo snack/bundles.
- **Builder / Roles:** product-strategist, solution-architect, design-director, software-builder, software-qa, 
elease-engineer.

### 7. DESKTOP
- **Supported Formats:** Windows, macOS, Linux, cross-platform desktop applications (Tauri, Electron, PyQt, native CLI/GUI), local offline-first applications, desktop utilities, desktop automation.
- **When to Use:** When operations require deep local OS integration, offline data privacy, high CPU/GPU compute, file-system access, or low-latency background monitoring.
- **Output Artifacts:** Executable installers (.msi, .dmg, .AppImage), portable ZIP binaries, packaged Tauri/Electron builds.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, software-qa, 
elease-engineer.

### 8. BROWSER EXTENSIONS
- **Supported Formats:** Chrome extensions (Manifest V3), Chromium extensions, Edge extensions, Firefox extensions, browser add-ons, bookmarklets.
- **When to Use:** When the transformation injects utility directly into the user's web-browsing workflow (scraping, modifying DOM, autofilling, analyzing active tabs, AI assistant overlays).
- **Output Artifacts:** Packaged extension directory, zipped crx/xpi-ready archives (extension.zip), manifest.json, background/content scripts.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, software-qa, 
elease-engineer.

### 9. CLI & DEVELOPER TOOLS
- **Supported Formats:** CLI tools, SDKs, client libraries, packages (PyPI, npm, crates.io), code generators, scaffolding tools, developer automation utilities.
- **When to Use:** When target users are software developers, DevOps engineers, or system administrators who work inside terminals, build pipelines, or codebases.
- **Output Artifacts:** Installable packages (setup.py / pyproject.toml, package.json), executable CLI scripts, manpages, comprehensive developer docs.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, software-qa, 
elease-engineer.

### 10. APIS & BACKEND SERVICES
- **Supported Formats:** REST APIs, GraphQL services, webhook handlers, data APIs, AI proxy APIs, backend processing microservices, integration services.
- **When to Use:** When programmatic access, headless operation, or multi-system data synchronization is the core customer value.
- **Output Artifacts:** OpenAPI 3.0 / Swagger specs, Postman/curl collections, runnable backend service, unit/integration test suites, container definitions.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, software-qa, 
elease-engineer.

### 11. DATABASE PRODUCTS & STRUCTURED DATA
- **Supported Formats:** SQLite databases, PostgreSQL/MySQL schemas and seeds, cloud database configurations, searchable databases, CRM-like systems, knowledge bases, inventory systems, curated datasets, benchmark databases, research databases, structured data packs.
- **When to Use:** When the core transformation comes from pre-aggregated, cleaned, organized, and indexed high-value proprietary information.
- **Output Artifacts:** Validated .sqlite files, SQL dump scripts, structured JSON/Parquet/CSV bundles, query recipes, data dictionaries.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, rtifact-builder, software-qa, rtifact-qa.

### 12. AUTOMATION & WORKFLOWS
- **Supported Formats:** Workflow automation (n8n, Make, Zapier configs), scheduled automation scripts, webhook pipelines, reporting automation, notification systems, document processing pipelines, AI workflows, multi-agent pipelines, content pipelines.
- **When to Use:** When the customer's primary pain is repetitive manual glue-work across multiple disconnected tools.
- **Output Artifacts:** Runnable automation scripts (Python/Node.js), importable workflow JSON files (n8n, GitHub Actions), environment variable templates, runbooks.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, software-qa, 
elease-engineer.

### 13. AI PRODUCTS & ASSISTANTS
- **Supported Formats:** AI assistants, AI web applications, AI mobile/desktop tools, AI APIs, AI workflows, multi-agent systems, Retrieval-Augmented Generation (RAG) applications, document Q&A tools, AI analysis/synthesis tools, AI generators, recommendation and classification engines.
- **When to Use:** When complex natural language understanding, reasoning over unstructured corpora, or generative transformations are fundamentally required.
- **Output Artifacts:** Full software repo, prompt templates, vector store configuration, evaluation test suite, API integration layer, safe error handling and fallback logic.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, software-qa, 
elease-engineer.

### 14. MULTIMEDIA & CREATIVE ASSETS
- **Supported Formats:** Structured video course scripts, audio course outlines, tutorial libraries, curated image packs, SVG icon packs, illustration sets, animation packs, motion graphics templates, social-media asset bundles, sound assets.
- **When to Use:** When auditory, visual, or sensory learning and branded creative building blocks are the deliverable.
- **Output Artifacts:** Clean media asset folders, SVG/PNG asset directories, structured Markdown course curricula, audio/video script files with timestamp cues.
- **Builder / Roles:** product-strategist, design-director, rtifact-builder, rtifact-qa.

### 15. EDUCATION & TRAINING SYSTEMS
- **Supported Formats:** Interactive courses, cohort/self-paced programs, learning systems, quizzes, diagnostics, assessments, training portals, educational applications.
- **When to Use:** When structured skill acquisition and verified competency milestones are required.
- **Output Artifacts:** Course manifests, modular learning units, assessment rubrics, interactive quiz modules, progress tracking tools.
- **Builder / Roles:** product-strategist, product-builder, software-builder (if interactive), design-director, critic.

### 16. GAMES & INTERACTIVE EXPERIENCES
- **Supported Formats:** Browser games, educational games, simulation engines, interactive experiences, gamified training systems.
- **When to Use:** When learning through play, mechanics-based simulations, or behavioral conditioning delivers the transformation.
- **Output Artifacts:** HTML5 canvas/WebGL bundle, game logic scripts, asset bundles, documentation.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, design-director, software-qa.

### 17. PLUGINS & PLATFORM INTEGRATIONS
- **Supported Formats:** Figma plugins, WordPress plugins, CMS plugins, CRM integrations, Slack apps/integrations, Discord bots, Notion integrations, Google Workspace add-ons, Microsoft 365 add-ins, payment/storage integrations.
- **When to Use:** When the customer already lives inside an existing platform ecosystem and will not adopt a standalone destination app.
- **Output Artifacts:** Platform manifest, plugin bundle, authorization/OAuth flow handler, distribution listing pack.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, software-qa, 
elease-engineer.

### 18. BOTS & CONVERSATIONAL INTERFACES
- **Supported Formats:** Slack bots, Discord bots, Telegram bots, WhatsApp bots, notification bots, support bots, workflow conversational agents.
- **When to Use:** When conversational command-and-control, instant notifications, or team-channel collaboration is the optimal interface.
- **Output Artifacts:** Bot codebase, webhook endpoints, command handlers, deployment configuration.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, software-qa, 
elease-engineer.

### 19. DEVICE & EMBEDDED COMPANIONS
- **Supported Formats:** Companion applications, device dashboards, configuration utilities, local-control software (IoT / hardware tools).
- **When to Use:** When interfacing with local network hardware, microcontrollers, or physical accessories.
- **Output Artifacts:** Local web dashboard or desktop controller, communication protocol scripts.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, software-qa.

### 20. XR & 3D EXPERIENCES
- **Supported Formats:** WebXR experiences, 3D interactive viewers, AR filters, 3D product configurators.
- **When to Use:** When spatial visualization, 3D inspection, or immersive depth is essential.
- **Output Artifacts:** 3D web bundle (Three.js, Babylon.js), GLTF/GLB models, interactive viewport controls.
- **Builder / Roles:** product-strategist, solution-architect, software-builder, software-qa.

### 21. HYBRID PRODUCTS
- **Supported Formats:** Cohesive multi-modality bundles (e.g., Web Application + Printable Strategy Playbook + Excel Financial Model + Creator Video Guides).
- **When to Use:** When a single modality cannot fulfill the complete transformation, and a combined system creates unbeatable commercial defensibility.
- **Output Artifacts:** Unified product directory containing all audited components, coordinated delivery manifest, cross-referenced documentation.
- **Builder / Roles:** Full cross-functional coordination: product-strategist, solution-architect, product-builder, software-builder, design-director, rtifact-builder, software-qa, rtifact-qa, packaging, 
elease-engineer, critic.

---

## 2. Modality Decision Hierarchy

The Product Strategist must evaluate candidate modalities using the following decision rules:
1. **Rule of Least Mechanism:** Can this transformation be reliably achieved with a document or structured spreadsheet? If yes, do NOT build a full SaaS application.
2. **Rule of Interaction Necessity:** Does the problem require custom calculations, real-time feedback, user inputs, or database persistence? If yes, elevate to an Interactive Tool or Web Application.
3. **Rule of Platform Gravity:** Where does the customer already spend 80% of their working hours? If in Notion, build a Notion system. If in Figma, build a Figma plugin. If on mobile, build a PWA or mobile app.
4. **Rule of Operational Cost:** Never commit to high server or maintenance costs unless the monetization model and customer willingness to pay explicitly justify it.
