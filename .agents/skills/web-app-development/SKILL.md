---
name: web-app-development
description: Architecture, coding standards, responsive layouts, client-side state management, and build protocols for commercial web applications.
---

# Web Application Development Skill

This skill governs the end-to-end development of web applications, client portals, SaaS interfaces, authenticated dashboards, and interactive calculators.

## 1. Core Invariants

- **Runnable Codebase:** Never stop at mockups or UI snippets. Generate complete source files (`index.html`, CSS, JS, bundle scripts, tests).
- **Zero Dead Navigation:** Every button, tab, link, and modal trigger must perform its intended action or be clearly disabled.
- **Zero Placeholders:** No `lorem ipsum`, dummy buttons, non-functional fake links (`href="#"`), or `TODO` comment blocks in production UI.
- **State Persistence:** User input and workflow state must persist across page refreshes (via `localStorage`, IndexedDB, or backend API).
- **Responsive by Default:** Must render cleanly without horizontal scrollbars on mobile (375px), tablet (768px), and desktop (1280px).
- **Error Boundaries:** Any unhandled exception must display a friendly fallback screen with a "Reset App" or "Retry" button, rather than a white screen of death.

## 2. Recommended Application Architecture

### Directory Structure
```text
products/<product_id>/software/
├── index.html            # Semantic HTML shell, viewport meta, SEO tags
├── css/
│   ├── reset.css         # Modern CSS reset
│   ├── variables.css     # Design tokens (colors, spacing, typography)
│   └── app.css           # Component and layout styling
├── js/
│   ├── state.js          # Reactive state store with event listeners
│   ├── router.js         # Client-side hash or history router
│   ├── storage.js        # Local persistence layer
│   ├── components/       # Reusable UI component renderers
│   └── app.js            # Main bootstrap entry point
├── tests/
│   ├── unit.test.js      # Core logic and calculation tests
│   └── routes.test.js    # Link and navigation tests
├── package.json          # Dependency and script definitions
└── README.md             # Local setup, run, and build instructions
```

## 3. Production Procedure

### Step 1: Starter Scaffolding
1. Inspect `templates/web-app/` for the proven web application starter.
2. Adapt the starter tokens in `variables.css` to match `design/<product_id>/design-system.md`.

### Step 2: Information Architecture & Routing
1. Set up view routes (e.g. `#/dashboard`, `#/calculator`, `#/settings`).
2. Ensure active navigation links have `aria-current="page"` and distinct active styling.
3. Add a default route fallback that redirects unrecognized hashes to the main view.

### Step 3: Core Workflow Implementation
1. Implement the user transformation workflow.
2. Provide immediate, deterministic feedback for every user interaction (e.g., toast notification, status badge update).
3. Implement loading skeletons or spinners during asynchronous operations.
4. Provide realistic initial sample data so the application looks populated and alive on first launch.

### Step 4: Verification & Link Check
1. Execute `python system/scripts/link_checker.py products/<product_id>/software/`.
2. Verify all buttons have registered `click` handlers.
3. Test layout at 375px width in browser or via test runner.
