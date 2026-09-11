# AI PRODUCT FACTORY — MODALITY-SPECIFIC QUALITY CHECKLISTS

Before and during product construction, the Master Agent, builder subagents, QA subagents, and Critic must enforce the modality-specific checklist corresponding to the approved product format.

---

## 1. BOOKS, EBOOKS, WHITE PAPERS & PLAYBOOKS
*Target Archetypes: Executive Playbooks, Industry Manuals, Thought Leadership Ebooks, White Papers*

- [ ] **Book Architecture & Sequence:** Complete structural flow:
  - Outer Front Cover (Title, Subtitle, Byline, Brand Mark).
  - Half-Title Page.
  - Colophon / Copyright & Provenance Page (Version, Date, Sources Citation).
  - Table of Contents (Hierarchical, page-numbered, dot leaders).
  - Chapter Openers with Chapter Number, Title, Epigraph/Takeaway, and 3-line Drop Cap.
  - Structured Narrative with Alternating Visual Rhythm.
  - Back Matter (Appendix, Glossary, Provenance Registry, Back Cover).
- [ ] **Measure & Line Length:** Body text strictly bounded between **45 and 75 characters per line** (ideal: 65ch). Never span unconstrained across full-width page.
- [ ] **Visual Pacing & Anti-Fatigue:** No unbroken text blocks exceeding 350 words. Interleaved with callouts, pull quotes, metric pills, tables, or schematics.
- [ ] **Callout Taxonomy:** Distinct styling for Core Principles (Blue), Warnings (Amber), Action Checks (Emerald), and Formulas (Slate).
- [ ] **Information Design in Tables:** Header distinction (tinted, bold 8pt uppercase), right-aligned numbers, left-aligned text, explicit column widths.
- [ ] **Print Geometry & Binding Gutters:** Standard trim sizes (A4, US Letter, 7x10 Crown). Inside gutter margin &ge; 22mm for physical binding; outer margins &ge; 18mm.
- [ ] **Anti-Collision & Page Breaks:** Headings avoid page breaks (`break-after: avoid;`). Widow/orphan control (`orphans: 3; widows: 3;`).
- [ ] **Monochrome & Grayscale Legibility:** Tested in grayscale; high contrast body text (&ge;75% black); zero unreadable faint gray text.
- [ ] **PDF Outlines & Metadata:** Compiled PDF contains interactive hierarchical bookmarks (H1/H2) and standard document metadata (Title, Author, Subject).
- [ ] **Verified Provenance:** Every statistic, benchmark, and empirical claim maps directly to `memory/sources.csv`. Zero AI platitudes.

---

## 2. WORKBOOKS, PLANNERS & GUIDED JOURNALS
*Target Archetypes: Guided Implementation Workbooks, 90-Day Planners, Diagnostic Field Journals*

- [ ] **The 8mm Rule (Handwriting Ergonomics):** Ruled writing lines must have **minimum 8.0mm to 9.5mm** (24pt – 28pt) vertical spacing. Reject 14pt lines as physically unusable.
- [ ] **Anatomy of Worksheets:** Every exercise spread contains: Context Header &rarr; Visual Framework/Example &rarr; Numbered Sub-Prompts &rarr; Ergonomic Workspace &rarr; Commitment/Validation Sign-off.
- [ ] **Dual-Mode Digital & Print Utility:**
  - In print mode: Clean horizontal rules and framed writing boxes.
  - In digital PDF viewing: Interactive, editable `<input>` and `<textarea>` fields allowing typed notes.
- [ ] **Crisp Checkboxes:** Checkboxes are exactly 14px – 16px squares with clean 1.5pt borders, vertically aligned with text baselines.
- [ ] **Habit & Activity Trackers:** Weekly tables feature 7 explicit day columns (`M`, `T`, `W`, `T`, `F`, `S`, `S`) with generous check circles (20px) and weekly score totals.
- [ ] **Visual Fatigue Prevention:** Never exceed 3 consecutive high-density worksheets without an intervening summary page, case breakdown, or visual roadmap.
- [ ] **Scorecards & Rubrics:** Section-ending rubrics feature clear numerical scoring (1–5 Likert bubbles) and diagnostic maturity criteria.

---

## 3. SPREADSHEETS & FINANCIAL MODELS
*Target Archetypes: SaaS Unit Economics, Cash Flow Models, Operational Trackers, Pricing Simulators*

- [ ] **Automated Usability Audit:** Executes `system/scripts/template_usability_tester.py` with 100% `PASS`.
- [ ] **Formula Integrity:** Absolutely zero `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`, or circular references across all sheets.
- [ ] **Orientation & Instructions Tab:** Dedicated "Instructions" or "Assumptions" sheet explaining model architecture, drivers, and version history.
- [ ] **Frozen Panes:** Top header rows and primary row labels frozen (`freeze_panes`) on all calculation sheets.
- [ ] **Cell Architecture & Palette:** Visual distinction between User Input cells (e.g. soft blue tint) and Automated Calculations (white/gray).
- [ ] **Explicit Number Formatting:** All numbers explicitly formatted as Currency (`$#,##0`), Percentage (`0.0%`), or Dates (`YYYY-MM-DD`). Zero raw floats.
- [ ] **Auto-Fitted Columns:** Column widths padded (+3 chars) to completely eliminate `###` numeric display overflow.
- [ ] **Realistic Domain Data:** Pre-populated with rich, cohesive, non-trivial domain numbers (no placeholder zeroes or test strings).

---

## 4. PRESENTATIONS & SLIDE DECKS
*Target Archetypes: Pitch Decks, Executive Briefings, Masterclasses, Visual Keynotes*

- [ ] **Widescreen Ratio:** Engineered in standard 16:9 widescreen format (`1920x1080` / `16:9`).
- [ ] **Action Titles:** Every slide title asserts a complete, declarative insight (e.g. "CAC Increased 42% While LTV Remained Flat"), never a passive topic label.
- [ ] **One Core Idea per Slide:** Slides focus exclusively on a single strategic message.
- [ ] **Visual Balance & Scannability:** Maximum 4–5 core items per slide. Zero walls of bullet points.
- [ ] **Typographic Legibility:** Major headings &ge; 28pt; body and key takeaways &ge; 14pt; high visual contrast.
- [ ] **Presenter Notes & Timing:** Slide specs include contextual presenter talking points and estimated delivery duration.

---

## 5. WEB APPLICATIONS
*Target Archetypes: SaaS Portals, Interactive Calculators, Directories, Client Dashboards*

- [ ] **Information Architecture:** Intuitive page hierarchy, persistent navigation bar, contextual breadcrumbs.
- [ ] **Responsive Breakpoints:** Fully functional and polished across:
  - Mobile: 375px &bull; Tablet: 768px &bull; Desktop: 1280px.
- [ ] **Loading States:** Skeleton loaders or disabled buttons with spinners during async execution.
- [ ] **Empty States:** Friendly empty states with illustrative icon, explanation, and primary action CTA.
- [ ] **Error Boundaries:** Catches unexpected errors with user-friendly recovery ("Retry" or "Reset State").
- [ ] **Accessibility:** Semantic HTML landmarks (`<nav>`, `<main>`, `<footer>`), form `<label>` associations, WCAG AA contrast.
- [ ] **Navigation & Links:** Zero dead links (`404`), zero buttons that do nothing, active navigation indicators.
- [ ] **Interactions & Feedback:** Immediate deterministic feedback (toast alerts, status badges) on every action.
- [ ] **Mobile Touch Behavior:** No horizontal scrollbar on mobile views (`scrollWidth <= innerWidth`).

---

## 6. MOBILE & TABLET PRODUCTS
*Target Archetypes: Responsive Touch Apps, Field Companion PWAs, Touch Tools*

- [ ] **Touch Targets:** All clickable and interactive elements meet minimum `44px x 44px` target area with &ge;8px spacing.
- [ ] **Phone Navigation:** Sticky bottom tab navigation bar (3-5 items) or top app bar with slide drawer.
- [ ] **Tablet Ergonomics:** Responsive multi-pane layout utilizing widescreen tablet space effectively.
- [ ] **Keyboard Behavior:** Correct input types (`email`, `tel`, `number`, `decimal`) to summon appropriate native virtual keyboard.
- [ ] **Safe-Area Insets:** Hardware notches and bottom home indicators respected (`env(safe-area-inset-bottom)`).
- [ ] **Offline Behavior:** PWA manifest and service worker cache core assets with offline status banner.
- [ ] **State Persistence:** User workflow progress persists in local storage across browser exits and reloads.

---

## 7. SOFTWARE & DEVELOPER TOOLS
*Target Archetypes: CLI Utilities, Desktop Tools, Automation Bots, Backend Packages*

- [ ] **Architecture:** Clean separation of concerns (CLI interface, core logic, persistence, error handling).
- [ ] **Build & Compilation:** Reproducible build with documented dependencies (`package.json`, `requirements.txt`).
- [ ] **Runtime Stability:** Graceful exit codes (`0` for success, non-zero for errors) and informative stderr messages.
- [ ] **Error Handling:** Safe error traps; zero unhandled stack traces leaked to user.
- [ ] **Persistence & Storage:** Clean file I/O with path normalization and atomic file writing.
- [ ] **Security Baseline:** Zero hard-coded credentials, private tokens, or secrets. Strict input sanitization.
- [ ] **Automated Tests:** Comprehensive unit and integration test suite executing with 100% pass rate.
- [ ] **Local Run Guide:** `README.md` containing prerequisite listing, installation command, and example execution.

---

## 8. API PRODUCTS
*Target Archetypes: Headless Microservices, Developer APIs, Webhook Handlers*

- [ ] **Interface Specification:** Authoritative OpenAPI 3.1 schema defining routes, query params, bodies, and responses.
- [ ] **Input Validation:** Strict payload validation; extra unmapped fields rejected or stripped.
- [ ] **Standard Envelopes:** Uniform JSON envelopes (`{ "success": true, "data": ... }` and `{ "success": false, "error": { "code", "message" } }`).
- [ ] **HTTP Status Codes:** Accurate semantic status codes (`200`, `201`, `400`, `401`, `403`, `404`, `422`, `500`).
- [ ] **Authentication & Security:** Secure token handling, CORS headers configured, rate limit headers included.
- [ ] **Health Endpoint:** Dedicated `GET /health` endpoint returning status and uptime.
- [ ] **Contract Tests:** Automated test suite verifying both valid payloads and negative failure conditions.

---

## 9. DATABASE PRODUCTS
*Target Archetypes: SQLite Deliverables, Curated Datasets, Reference Schema Packages*

- [ ] **Relational Integrity:** Foreign key constraints enabled and enforced (`PRAGMA foreign_keys = ON;`).
- [ ] **Normalization:** Tables normalized to 3NF; junction tables used for N:M relationships.
- [ ] **Explicit Constraints:** Primary keys, `NOT NULL`, and `CHECK` constraints on bounded enum values.
- [ ] **Indexing Strategy:** Explicit indexes on foreign keys, lookups, and sorting columns.
- [ ] **Data Integrity Check:** Automated script passes `PRAGMA integrity_check;` and `PRAGMA foreign_key_check;`.
- [ ] **Realistic Domain Seeds:** Non-trivial, verified dataset records included with real domain statistics.

---

## 10. HYBRID PRODUCTS
*Target Archetypes: Multi-tier Packages (e.g. Web App + Executive Playbook + Workbook + Financial Model)*

- [ ] **Component Quality:** Every individual constituent component passes its respective modality checklist.
- [ ] **Inter-Component Cohesion:** Unified terminology, matching color palettes, and identical typography styles.
- [ ] **Unified Onboarding:** Single centralized `README.md` guiding the customer across all deliverables.
- [ ] **Seamless Packaging:** Single organized ZIP bundle with clean folder structure and accurate delivery manifest.
