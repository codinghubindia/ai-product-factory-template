---
name: database-engineering
description: Schema design standards, migration frameworks, foreign key integrity, indexing strategies, seed data generation, and verification scripts for SQLite and SQL databases.
---

# Database Engineering Skill

This skill governs data architecture, relational schema creation, migration management, integrity enforcement, and seed population for database products and application backends.

## 1. Core Invariants

- **Relational Integrity:** Foreign keys must always be enabled and enforced (`PRAGMA foreign_keys = ON;`).
- **Data Normalization:** Structure schemas in Third Normal Form (3NF) unless explicit denormalization is required and documented for analytical read performance.
- **Explicit Constraints:**
  - Primary keys on all tables (`id INTEGER PRIMARY KEY AUTOINCREMENT` or `UUID`).
  - `NOT NULL` constraints on all required fields.
  - `CHECK` constraints on bounded values (e.g. `CHECK (status IN ('active', 'archived', 'pending'))`).
  - `UNIQUE` constraints on natural keys (e.g. email, slug, SKU).
- **Indexing Strategy:** Create explicit indexes on all foreign key columns, join targets, and frequently filtered or sorted columns.
- **Migration Discipline:** All schema changes must be applied via sequential migration scripts with reversible rollbacks (`001_initial.sql`, `002_add_index.sql`).

## 2. Tools & Templates

- Starter: `templates/database/`
- Schema: `templates/database/schema.sql`
- Migrator: `templates/database/migrate.py`
- Integrity Verifier: `templates/database/verify_integrity.py`
- Seed Script: `templates/database/seed.sql`

## 3. Production Procedure

### Step 1: Entity-Relationship Modeling
1. Identify entities, relationships (1:1, 1:N, N:M with junction tables), and attributes.
2. Include audit columns on all primary entities:
   - `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL`
   - `updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL`

### Step 2: DDL Scripting & Migrations
1. Write schema in `schema.sql`.
2. Ensure tables are created in dependency order (parent tables before child tables with foreign keys).
3. Add triggers for auto-updating `updated_at` timestamps on row updates.

### Step 3: Realistic Seed Population
1. Create `seed.sql` with rich, realistic domain data.
2. Never use meaningless dummy text (`foo`, `test`, `asdf`). Populate with realistic names, verified industry metrics, real categories, and coherent dates.

### Step 4: Automated Integrity Verification
Run verification script:
```bash
python templates/database/verify_integrity.py --db products/<product_id>/database.sqlite
```
The script validates:
- `PRAGMA integrity_check;` returns `ok`.
- `PRAGMA foreign_key_check;` returns 0 violations.
- Row counts on all seeded tables are non-zero.
- Query performance check on key join queries.
