-- ============================================================================
-- AI PRODUCT FACTORY — REFERENCE SQLITE DATABASE SCHEMA
-- Modality: Database / Data Product / Persistence Tier
-- Features: Foreign Key Constraints, Check Constraints, Automatic Timestamps, Indexes.
-- ============================================================================

PRAGMA foreign_keys = ON;

-- 1. Organizations / Workspaces
CREATE TABLE IF NOT EXISTS workspaces (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    tier TEXT NOT NULL CHECK (tier IN ('FREE', 'PRO', 'ENTERPRISE')) DEFAULT 'PRO',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- 2. Products / Deliverables
CREATE TABLE IF NOT EXISTS products (
    id TEXT PRIMARY KEY,
    workspace_id TEXT NOT NULL,
    name TEXT NOT NULL,
    modality TEXT NOT NULL,
    production_readiness TEXT NOT NULL CHECK (
        production_readiness IN (
            'PROTOTYPE', 'BUILDABLE', 'FUNCTIONAL', 'TESTED',
            'RELEASE_CANDIDATE', 'DEPLOYABLE', 'DEPLOYED', 'PUBLISHED', 'PRODUCTION_READY'
        )
    ) DEFAULT 'PROTOTYPE',
    version TEXT NOT NULL DEFAULT '1.0.0',
    metadata_json TEXT DEFAULT '{}',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (workspace_id) REFERENCES workspaces(id) ON DELETE CASCADE
);

-- 3. Audit Records & Defect Ledger
CREATE TABLE IF NOT EXISTS audit_records (
    id TEXT PRIMARY KEY,
    product_id TEXT NOT NULL,
    auditor TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('PASS', 'FAIL', 'WAIVED')),
    critical_defects INTEGER DEFAULT 0 CHECK (critical_defects >= 0),
    high_defects INTEGER DEFAULT 0 CHECK (high_defects >= 0),
    report_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Indexes for Fast Query Performance
CREATE INDEX IF NOT EXISTS idx_products_workspace ON products(workspace_id);
CREATE INDEX IF NOT EXISTS idx_products_modality ON products(modality);
CREATE INDEX IF NOT EXISTS idx_products_readiness ON products(production_readiness);
CREATE INDEX IF NOT EXISTS idx_audit_product ON audit_records(product_id);
CREATE INDEX IF NOT EXISTS idx_audit_status ON audit_records(status);

-- Automatic Timestamp Update Trigger
CREATE TRIGGER IF NOT EXISTS trg_workspaces_updated
AFTER UPDATE ON workspaces
FOR EACH ROW
BEGIN
    UPDATE workspaces SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER IF NOT EXISTS trg_products_updated
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
