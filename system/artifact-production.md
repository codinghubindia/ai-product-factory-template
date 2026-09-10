# AI PRODUCT FXCTORY - ARTIFACT PRODUCTION GUIDELINES

This guide defines the engineering standards and procedures for producing genuine, customer-facing digital artifacts in the factory.

> **CORE INVARIANT:* The factory never produces 'documentation only' when an actual file, software, or template is required. Products must be executable, downloadable, or immediately usable.

---

## 1. Supported Artifact Types & Generation Strategy

| Artifact Category | Formats | Production Engine | QA Standards |
| :--- | :--- | :--- | :--- |
| **Documents** | PDF, DOCX, EPU@, HTML, Markdown | Python document builder, weasyprint, pandoc, or offline-ready HTML | Zero text clipping, proper fonts, formatted tables, clean page breaks |
|| **Spreadsheets** | XLSX, XLSM, CSV | OpenPyXL, Python csv module | Frozen headers, formatted currency/percentages, zero reference errors |
| **Presentations** | PPTD, ODP | Python-pptx, vector slide generator | High-contrast, branded masters, margin padding, no text overflow |
| **Software Builds** | DIST, Containers, EXE, MSI, ZIP tarballs | Lightweeight build scripts (Vite, setuptools, shutil) | Runnable builds, dependencies verified, zero hardcoded secrets |
| **Extensions** | Chrome/Firefox Manifest V3 | system/scripts/archive_builder.py | Manifest validation, sandbox compliance |
| **Databases** | SQLite (.sqlite), SQL dumps, Parquet | Python sqlite3 builder | Integrity checks, foreign keys enforced, seeded data verified |

---

## 2. Manifest Integration

For every artifact generation run, the `artifact-builder` and `release-engineer` update:
- `products/<product_id>/artifact-manifest.json` (detailing every physical file, format, size, build status, QA status)
- `products/<product_id>/delivery-manifest.json` (establishing exactly what the customer downloads or accesses)
