# AI PRODUCT FACTORY — ARTIFACT PRODUCTION GUIDELINES

This guide defines the engineering standards and procedures for producing genuine, customer-facing digital artifacts in the factory.

> **CORE INVARIANT:** The factory never produces "documentation only" when an actual file, software, or template is required. Products must be executable, downloadable, or immediately usable.

---

## 1. Supported Artifact Types & Generation Strategy

| Artifact Category | Formats | Production Engine | QA Standards |
| :--- | :--- | :--- | :--- |
| **Documents** | PDF, HTML, DOCX, EPUB | `system/scripts/document_builder.py` | Zero text clipping, proper fonts, formatted tables, clean page breaks, zero raw markdown |
| **Spreadsheets** | XLSX, XLSM, CSV | `system/scripts/spreadsheet_builder.py` | Frozen headers, formatted currency/percentages, zero formula error codes (`#REF!`) |
| **Presentations** | PPTX, HTML slides | `templates/presentations/slide-deck-spec.md` | High-contrast, branded masters, margin padding, no text overflow, 14pt+ body font |
| **Software Builds** | Runnable repo, PWA, Web App | `software-builder`, npm/pip build scripts | Runnable builds, dependencies verified, zero hardcoded secrets, zero broken links |
| **Extensions** | Chrome/Firefox Manifest V3 | `system/scripts/archive_builder.py` | Manifest validation, sandbox compliance, clean background workers |
| **Databases** | SQLite (.sqlite), SQL dumps | `templates/database/migrate.py` | Integrity checks pass, foreign keys enforced, realistic domain seed data |

---

## 2. Manifest Integration

For every artifact generation run, the `artifact-builder` and `release-engineer` update:
- `products/<product_id>/artifact-manifest.json` (detailing every physical file, format, size, build status, QA status)
- `products/<product_id>/delivery-manifest.json` (establishing exactly what the customer downloads or accesses, SHA-256 hashes, and production readiness state)
