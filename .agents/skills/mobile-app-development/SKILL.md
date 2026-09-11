---
name: mobile-app-development
description: Touch-first UI guidelines, PWA manifests, offline caching protocols, viewport configurations, and build patterns for mobile and tablet applications.
---

# Mobile Application Development Skill

This skill governs mobile-first digital products, progressive web apps (PWAs), responsive tablet tools, and cross-platform mobile application packages.

## 1. Core Invariants

- **Touch Ergonomics:** Every interactive element (button, icon, table row, input) must have a minimum touch target size of `44px x 44px` with at least `8px` separation.
- **Safe Area Insets:** Layouts must account for mobile hardware notches and home indicators:
  ```css
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  ```
- **Viewport Meta Configuration:** Prevent unwanted auto-zooming on inputs and ensure mobile layout lock:
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  ```
- **Offline Capability:** A PWA or mobile app must include a valid `manifest.json` and a registered Service Worker caching core assets for full offline functionality.
- **Native-Feeling Navigation:**
  - Phone: Sticky bottom navigation bar (3-5 primary tabs) or top app bar with slide-out drawer.
  - Tablet: Persistent left sidebar navigation with multi-pane content layout.

## 2. Tools & Starters

- Starter: `templates/mobile-app/`
- Manifest: `manifest.json` with app name, icons (192px, 512px), background_color, theme_color, and `display: "standalone"`.
- Service Worker: `sw.js` with Cache-First or Stale-While-Revalidate caching strategy.

## 3. Step-by-Step Procedure

### Step 1: Touch-First Interface Architecture
1. Design the layout using `templates/mobile-app/`.
2. Ensure input fields have appropriate HTML input types (`type="email"`, `type="tel"`, `type="number"`, `inputmode="decimal"`) to trigger the correct native virtual keyboard.
3. Eliminate hover-dependent tooltips; use tap-to-reveal modals or expandable accordions instead.

### Step 2: Service Worker & Offline Persistence
1. Register `sw.js` in the main script.
2. Store user inputs and settings in `localStorage` or `IndexedDB`.
3. Add an offline status banner that indicates when network connection is lost, while ensuring local functionality remains available.

### Step 3: Mobile Verification
1. Test viewport breakpoints:
   - Small phone: 375px width (iPhone SE / iPhone 13 mini)
   - Standard phone: 390px - 414px width
   - Tablet portrait: 768px width (iPad Mini)
   - Tablet landscape: 1024px width
2. Verify touch scroll smoothness (`-webkit-overflow-scrolling: touch`).
3. Verify that virtual keyboard popping up does not obscure active form inputs or cause page jumping.
