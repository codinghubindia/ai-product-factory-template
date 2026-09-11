---
name: software-testing
description: Comprehensive 12-step software testing protocol, automated test runners, edge-case validation, failure path testing, and defect classification.
---

# Software Testing Skill

This skill governs the rigorous verification of all software codebases, applications, tools, and scripts produced by the AI Product Factory.

## 1. Core Rule: "Build Succeeded" Is Not QA

Never declare PASS merely because a build command exited with code 0 or source files exist. Every software product must execute real tests against real test runners and verify actual runtime workflows.

## 2. The 12-Step Software Testing Protocol

For every software product:
1. **Clean Installation:** Install dependencies cleanly (`npm install` or `pip install -r requirements.txt`). Confirm zero unhandled dependency conflicts.
2. **Compilation / Build:** Execute build script (`npm run build` or `python setup.py build`). Ensure zero syntax errors, missing asset references, or bundling crashes.
3. **Automated Unit Tests:** Run test runner (`npm test` or `pytest`). Ensure 100% of test assertions pass.
4. **Runtime Launch:** Start application server or binary locally. Verify it binds to port and responds to initial HTTP/socket request.
5. **Primary User Journey:** Execute the core transformation journey from start to finish (e.g., input data -> trigger calculation -> view rendered results -> save state).
6. **Edge Cases & Boundary Conditions:** Test extreme inputs: empty strings, zero values, maximum numbers, special characters (`<>&"'`), unicode emojis, and unusually large inputs.
7. **Failure Paths & Error Handling:** Test network disconnection, invalid file uploads, malformed JSON, and non-existent IDs. Verify friendly user messages and zero unhandled exceptions.
8. **Data Persistence:** Enter data, trigger persistence, restart application or refresh page, and verify all user data is faithfully restored.
9. **API / Database Integrity:** Verify schema migrations run without errors, seed data loads, foreign keys are enforced, and query execution is fast.
10. **Responsive Viewport Testing:** Test UI layout across:
    - Mobile: 375px width
    - Tablet: 768px width
    - Desktop: 1280px width
11. **Platform / Environment Testing:** Check terminal behavior across PowerShell, bash, and standard browser engines.
12. **UI Polish & Console Hygiene:** Inspect running app in browser or headless inspector. Confirm zero JavaScript console errors (`TypeError`, `Uncaught ReferenceError`), zero broken images, and zero dead links.

## 3. Defect Classification Hierarchy

- **CRITICAL:** Application crashes, core flow blocked, compilation fails, auth bypass, SQL injection, hardcoded secret. Blocks shipping unconditionally.
- **HIGH:** Secondary feature broken, responsive layout completely broken on phone/tablet, missing error boundary, failing integration test. Blocks shipping unless formally waived with written justification in `memory/decisions.md`.
- **MEDIUM:** Minor styling inconsistency, missing input validation on optional field, minor performance lag. Remediation recommended.
- **LOW:** Code formatting nitpicks, non-blocking deprecation warning.

## 4. Execution Tools

- Test Runner: `system/scripts/software_runner.py`
- Link Validator: `system/scripts/link_checker.py`
- Machine-Readable Report: `products/<product_id>/audit/software-qa.json`
- Human-Readable Report: `products/<product_id>/audit/software-qa-report.md`
