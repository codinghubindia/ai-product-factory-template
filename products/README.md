# Products Workspace

Each approved product occupies a dedicated subdirectory named after its unique product ID (`products/<product_id>/`).

---

## Directory Conventions for Each Product

```
products/<product_id>/
├── specification.json       # Formal product spec adhering to system/schemas/product.schema.json
├── strategy.md              # Detailed strategic rationale, transformation, and positioning
├── content/                 # Modular drafted content, chapters, and worksheets
├── assets/                  # Diagrams, schemas, illustrations, or code snippets
├── final/                   # Assembled, formatted, and complete deliverable suite
└── audit/
    ├── audit.json           # Machine-readable audit adhering to system/schemas/audit.schema.json
    └── report.md            # Red-team review and verdict (PASS/FAIL) by Critic agent
```
