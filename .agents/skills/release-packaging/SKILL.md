---
name: release-packaging
description: Standards for customer delivery bundling, delivery manifest compilation, checksum generation, onboarding README authoring, and deployment readiness gating.
---

# Release Packaging Skill

This skill governs the packaging, archiving, customer onboarding documentation, and release verification for all completed digital products.

## 1. Core Invariants

- **The Actual Deliverable:** The package must contain the genuine, finished product—never just marketing copy, specs, or development repos.
- **Truthful Packaging:** Every claim, benefit, and screenshot in packaging materials must correspond to an inspected, verified capability of the delivered product.
- **Production Readiness State Enforced:** The release engineer must explicitly classify and record the product readiness state in `state.json` and `delivery-manifest.json`:
  `PROTOTYPE` | `BUILDABLE` | `FUNCTIONAL` | `TESTED` | `RELEASE_CANDIDATE` | `DEPLOYABLE` | `DEPLOYED` | `PUBLISHED` | `PRODUCTION_READY`
- **Zero Secrets in Release Bundle:** Scan all files for API keys, private tokens, passwords, `.env` files, or development test credentials before bundling.

## 2. Release Bundle Architecture

A standard release bundle (`release/<product_id>-v<version>.zip`) must include:
```text
release_bundle/
├── deliverables/           # The actual final products (.pdf, .xlsx, software build, sqlite, etc.)
├── docs/                   # User guide, quickstart manual, API references
├── templates/              # Any companion worksheets, blank templates, or starter presets
├── README.md               # Immediate customer onboarding & quickstart
├── LICENSE                 # Explicit commercial usage terms
└── delivery-manifest.json  # Machine-readable inventory with file hashes and sizes
```

## 3. Step-by-Step Procedure

### Step 1: Assembly & Staging
1. Create staging directory `release/staging/<product_id>/`.
2. Copy verified deliverables from `products/<product_id>/final/` or `products/<product_id>/software/dist/`.
3. Generate customer-facing `README.md` adapting `templates/packaging/README.template.md`.
4. Include `LICENSE` file.

### Step 2: Delivery Manifest Generation
1. Calculate SHA-256 checksums and file byte sizes for every deliverable.
2. Compile `delivery-manifest.json` adhering to `system/schemas/delivery-manifest.schema.json`.
3. Record customer access instructions and support contact.

### Step 3: Archive Compression
1. Run `system/scripts/archive_builder.py` to create the clean release archive:
   ```bash
   python system/scripts/archive_builder.py --source release/staging/<product_id> --output release/<product_id>-v<version>.zip
   ```

### Step 4: Pre-Ship Gate Verification
Verify all items in `system/pre-ship-checklist.md` before notifying the Master Agent for Human Approval Gate 4.
