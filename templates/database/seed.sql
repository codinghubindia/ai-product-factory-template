-- ============================================================================
-- AI PRODUCT FACTORY — VERIFIED REALISTIC DOMAIN SEED DATA
-- ============================================================================

INSERT OR IGNORE INTO workspaces (id, name, slug, tier) VALUES
('WS-001', 'Enterprise Cloud Security Lab', 'cloud-sec-lab', 'ENTERPRISE'),
('WS-002', 'Fintech Analytics Studio', 'fintech-analytics', 'PRO');

INSERT OR IGNORE INTO products (id, workspace_id, name, modality, production_readiness, version, metadata_json) VALUES
('PROD-001', 'WS-001', 'Multi-Cloud Compliance Sentinel', 'web_application', 'TESTED', '1.0.0', '{"primary_channel":"creator_partnerships"}'),
('PROD-002', 'WS-001', 'IAM Privilege Drift Playbook', 'document', 'RELEASE_CANDIDATE', '1.2.0', '{"pages":42}'),
('PROD-003', 'WS-002', 'SaaS Unit Economics Model', 'spreadsheet', 'PRODUCTION_READY', '2.0.0', '{"tabs":4}');

INSERT OR IGNORE INTO audit_records (id, product_id, auditor, status, critical_defects, high_defects, report_path) VALUES
('AUD-101', 'PROD-001', 'critic', 'PASS', 0, 0, 'products/PROD-001/audit/audit.json'),
('AUD-102', 'PROD-002', 'artifact-qa', 'PASS', 0, 0, 'products/PROD-002/audit/artifact-qa.json'),
('AUD-103', 'PROD-003', 'critic', 'PASS', 0, 0, 'products/PROD-003/audit/audit.json');
