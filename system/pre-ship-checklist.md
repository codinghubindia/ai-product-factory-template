# AI PRODUCT FACTORY — FINAL PRE-SHIP VERIFICATION CHECKLIST

Every product must achieve 100% verification across all seven categories before the Master Agent can request Human Approval Gate 4 or mark the lifecycle stage as `complete`.

---

## 1. PRODUCT VALUE & CREATIVE CONCEPT
- [ ] **Solves Intended Problem:** Directly alleviates the empirical customer friction identified in discovery.
- [ ] **Signature Mechanism Operational:** Distinctive internal mechanism (diagnostic, rubric, ladder, or decision engine) documented, named, and functioning.
- [ ] **Creative Concept Aligned:** Personality, visual metaphor, and emotional arc defined in `creative-concept.md`.
- [ ] **Customer Wow Moment Verified:** Time to First Useful Result (TTFR) is under **180 seconds**; first successful action succeeds without friction.
- [ ] **60-Second Creator Demonstration:** Core workflow and transformation demonstrated on video in under 60 seconds without hand-waving.

---

## 2. ACTUAL BUILD & FILE VERIFICATION
- [ ] **Actual Product Exists:** Real, executable deliverables exist in `products/<product_id>/final/` or `products/<product_id>/software/` (never stop at specs or mockups).
- [ ] **Required Files Exist:** All files specified in `specification.json` and `artifact-manifest.json` are present and non-empty.
- [ ] **Software Compiles Cleanly:** Zero compilation or syntax errors when executing build command.
- [ ] **Dependencies Documented & Localized:** Reproducible dependency manifests provided (`package.json`, `requirements.txt`, etc.).

---

## 3. DESIGN, TASTE & ERGONOMICS
- [ ] **Design System Coherent:** Adheres strictly to `design/<product_id>/design-system.md` (typography, palette, grid).
- [ ] **Visual Continuity Preserved:** All visual assets adhere to `design/<product_id>/visual-continuity.md`.
- [ ] **Taste Review is PASS:** Passed `taste_checker.py` with zero AI clichés, zero neon gradients, and score $\ge 4.0/5.0$.
- [ ] **Handwriting Ergonomics Verified:** Workbooks possess minimum 8.0mm to 9.5mm (24pt–28pt) rule spacing and 16px checkboxes.
- [ ] **Responsive Viewports Verified:** Checked across Mobile (375px), Tablet (768px), and Desktop (1280px).
- [ ] **Zero Placeholder Content:** Clean scan with zero `TODO`, `LOREM IPSUM`, `[INSERT`, or dummy buttons.

---

## 4. VISUAL ASSET PIPELINE & LICENSING
- [ ] **Asset Manifest Complete:** `products/<product_id>/assets/asset-manifest.json` tracks all 17 attributes per asset.
- [ ] **Asset Pipeline Script PASS:** `python system/scripts/asset_pipeline.py --manifest ...` exits with code 0.
- [ ] **Verified Licenses:** 100% of assets have explicit commercial licensing (`factory_original`, `cc0`, `mit`, etc.).
- [ ] **Zero Editorial Leaks:** No reference moodboard images placed in `final/` deliverables.

---

## 5. TESTING & SPREADSHEET AUDITING
- [ ] **Automated Tests Run:** Unit, contract, and integration tests have executed and passed with 100% assertion success.
- [ ] **Spreadsheet Formulas Audited:** Passed `template_usability_tester.py` with zero `#REF!`, `#DIV/0!`, `#VALUE!`, or unformatted numbers.
- [ ] **Zero Broken Links:** All internal routes, external URLs, and anchor tags audited with `link_checker.py`.
- [ ] **All Buttons Functional:** Every button, tab, and CTA has an active event handler or is intentionally disabled.
- [ ] **Error & Empty States Handled:** Informative error boundaries and helpful empty states implemented.
- [ ] **Actual Artifacts Inspected:** Rendered PDF/HTML inspected visually and checked with `artifact_inspector.py`.

---

## 6. PACKAGING, MERCHANDISING & NO DARK PATTERNS
- [ ] **Merchandising Blueprint Complete:** Offer structure, tiering, promise, and objections documented in `merchandising.json`.
- [ ] **Truthful Packaging:** Every claim, benefit, and screenshot maps to an inspected, functioning feature in the product.
- [ ] **Zero Dark Patterns:** Absolute zero fake scarcity ("Only 3 copies left"), zero fake countdown timers, zero fake reviews, zero hidden costs.
- [ ] **Installation / Onboarding Guide:** Clear `README.md` with prerequisites, setup steps, and troubleshooting.
- [ ] **Delivery Manifest Accurate:** `delivery-manifest.json` accurately lists all deliverables, sizes, and SHA-256 hashes.
- [ ] **Creator Promotion Pack:** One-sheet briefing pack with 60-second video demo script and talking points ready.

---

## 7. SOVEREIGN QUALITY GATE (CRITIC & REVIEW STACK)
- [ ] **The 6-Part Review Stack PASS:** Utility, Design, Taste, Psychology, Commercial, and Creator Fit reviews completed.
- [ ] **Zero Critical Defects:** 0 unresolved critical issues.
- [ ] **Zero High Defects:** 0 unresolved high issues (or explicit written justification recorded in `memory/decisions.md`).
- [ ] **Zero Fabricated Claims:** All factual assertions backed by verified Tier 1/2 records in `memory/sources.csv`.
- [ ] **Zero Secrets:** Scanned for and verified zero API keys, private tokens, or sensitive credentials in repo.
