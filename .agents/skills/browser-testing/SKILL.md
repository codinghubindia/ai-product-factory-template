---
name: browser-testing
description: Procedures and automated scripts for interactive browser verification, responsive viewport inspection, console error logging, and form interaction testing.
---

# Browser & UI Testing Skill

This skill governs interactive, in-browser verification of web applications, client dashboards, interactive calculators, and responsive digital products.

## 1. Core Principle: No Blind Source Inspection

Static code review cannot detect visual clipping, overlapping absolute divs, z-index glitches, unstyled form elements, or mobile viewport overflow. Browser-based products must be launched and inspected at actual browser viewport dimensions.

## 2. Tested Viewport Breakpoints

Every browser product must be tested at three canonical viewport widths:
1. **Mobile Phone:** `375px x 667px` or `390px x 844px`
   - Test touch targets, Hamburger/drawer menu, horizontal scrollbar absence, form input legibility, single-column stacking.
2. **Tablet:** `768px x 1024px`
   - Test 2-column grid reflow, sidebar collapse/expand, table horizontal scrolling/card transformation.
3. **Desktop Widescreen:** `1280px x 800px` or `1440px x 900px`
   - Test container max-width constraints, multi-column cards, modal dialog positioning.

## 3. Automated Browser Verification Protocol

### Test Areas Covered
1. **Page Load & HTTP Status:** Initial HTTP status 200, fast time-to-interactive, all linked stylesheets and scripts loaded.
2. **Console Error Detection:** Collect `console.error` and `window.onerror` logs. Zero uncaught runtime errors allowed.
3. **Navigation & Route Traversal:** Click through every internal route, nav link, tab, and breadcrumb. Verify URL state updates and active class toggles.
4. **Interactive Controls:**
   - Click all primary action buttons.
   - Fill out all form inputs with valid and invalid data.
   - Trigger modal open/close actions and verify escape-key handler.
5. **Horizontal Overflow Check:**
   - Execute DOM check: `document.documentElement.scrollWidth <= window.innerWidth`.
   - Any horizontal scrollbar on mobile views is an automatic layout defect.
6. **Network & Asset Validation:**
   - Confirm 0 `404 Not Found` errors for images, favicons, fonts, or APIs.

## 4. Execution Commands & Scripts

- Automated Script: `python system/scripts/ui_test_runner.py --dir products/<product_id>/software/ --port 8080`
- Broken-Link Tool: `python system/scripts/link_checker.py products/<product_id>/software/`
- Output: Appended to `products/<product_id>/audit/software-qa.json` under `browser_testing` block.
