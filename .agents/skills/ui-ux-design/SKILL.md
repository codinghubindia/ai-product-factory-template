---
name: ui-ux-design
description: Design principles, layout systems, component patterns, accessibility standards, and responsive rules for crafting intentional, premium user interfaces.
---

# UI/UX Design Skill

This skill governs visual and interactive interface design for software, web apps, mobile apps, dashboards, and digital tools created by the factory.

## 1. Core Principles

- **Audience & Context First:** Design begins from target customer sophistication, viewing device, and emotional context—not decorative impulses.
- **Intentional Aesthetics:** Every visual element must serve clarity, ergonomics, or trust.
- **Prohibited Aesthetics:**
  - Banned: Generic multi-color neon gradients.
  - Banned: Unreadable glassmorphism on text content.
  - Banned: Random disconnected card piles.
  - Banned: Heavy, muddy box shadows (`box-shadow: 0 20px 50px rgba(0,0,0,0.5)`).
  - Banned: Jarring, gratuitous animations that delay user interaction.
- **Clean Restraint:** A crisp, high-contrast, typographic design system with generous whitespace looks more expensive and trustworthy than decorative visual noise.

## 2. The Functional Design System Baseline

### Spacing & Grid System
- Use an 8px / 4px base spacing scale:
  - `space-1`: 4px (tight padding, badge gaps)
  - `space-2`: 8px (icon margins, input padding)
  - `space-3`: 12px (form element gap)
  - `space-4`: 16px (card padding, standard component gap)
  - `space-6`: 24px (section margins)
  - `space-8`: 32px (container padding)
  - `space-12`: 48px (page section spacing)

### Typography Scale
- Font Stack: Modern sans-serif system fonts:
  `font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, Helvetica, Arial, sans-serif;`
- Scale:
  - Display / Hero: 32px – 40px (Bold)
  - Page Title (H1): 24px – 28px (Bold)
  - Section Header (H2): 20px – 22px (Semi-bold)
  - Card Header (H3): 16px – 18px (Semi-bold)
  - Body Text: 14px – 15px (Regular, line-height 1.5 - 1.6)
  - Small / Metadata: 12px – 13px (Regular, line-height 1.4)
  - Micro / Badges: 10px – 11px (Medium / Uppercase)

### Color Palette Architecture
Define semantic variables:
- Neutral Light / Background: `#f8fafc` / `#ffffff`
- Neutral Dark / Text Primary: `#0f172a` (Never pure black `#000000`)
- Text Secondary: `#475569`
- Text Muted: `#94a3b8`
- Surface / Card: `#ffffff` with subtle border `#e2e8f0`
- Primary Brand: Solid, accessible tone (e.g. `#2563eb` or `#0f766e`)
- Success: `#16a34a` (green)
- Warning: `#d97706` (amber)
- Danger / Error: `#dc2626` (red)
- Contrast: All text against background must achieve minimum 4.5:1 ratio (WCAG AA).

## 3. Mandatory Component States

Every interactive component must define 5 states:
1. **Default:** Clean, clearly interactive, identifiable role.
2. **Hover:** Subtle background shift or border color enhancement (`transition: 0.15s ease`).
3. **Active / Pressed:** Visual depression or subtle scale shift.
4. **Focus:** Unmistakable focus ring for accessibility (`outline: 2px solid #3b82f6; outline-offset: 2px`).
5. **Disabled:** Reduced opacity (`opacity: 0.5`), `cursor: not-allowed`, no hover effects.

## 4. UI Layout Hygiene Checklist

- [ ] All inputs have explicit `<label>` elements linked via `id`.
- [ ] Every form button shows a loading state (spinner/disabled) during submission.
- [ ] Tables include sticky/frozen headers for lists over 10 rows.
- [ ] Empty states contain an icon, a clear description of why it is empty, and a primary CTA.
- [ ] Error messages clearly explain the issue and provide immediate recovery action.
