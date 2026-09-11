#!/usr/bin/env python3
"""
AI Product Factory — Factory Health Check
==========================================
Version: 0.3.0

Validates the factory template is in a clean, correctly configured state.
Checks agent definitions, schemas, workflows, scripts, state.json,
delegation log structure, and absence of product contamination.

Usage:
    python system/scripts/factory_health_check.py

Returns:
    Exit code 0 = PASS
    Exit code 1 = FAIL (one or more checks failed)
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]

# Expected agents (must all exist)
REQUIRED_AGENTS = [
    "master", "scout", "research", "pain-miner", "source-auditor",
    "competitor", "opportunity-analyst", "product-strategist",
    "creative-director", "solution-architect", "product-builder",
    "software-builder", "artifact-builder", "design-director",
    "asset-director", "software-qa", "artifact-qa", "taste-reviewer",
    "critic", "marketing-strategist", "packaging", "release-engineer",
    "distribution",
]

# Required schemas
REQUIRED_SCHEMAS = [
    "artifact-manifest.schema.json",
    "asset-manifest.schema.json",
    "audit.schema.json",
    "creative-concept.schema.json",
    "customer.schema.json",
    "delivery-manifest.schema.json",
    "delegation-log.schema.json",
    "opportunity.schema.json",
    "product.schema.json",
    "source.schema.json",
]

# Required workflow documents
REQUIRED_WORKFLOWS = [
    "discovery.md",
    "product-build.md",
    "distribution.md",
]

# Required system scripts
REQUIRED_SCRIPTS = [
    "archive_builder.py",
    "artifact_inspector.py",
    "asset_pipeline.py",
    "document_builder.py",
    "factory_health_check.py",
    "link_checker.py",
    "pdf_compiler.py",
    "software_runner.py",
    "spreadsheet_builder.py",
    "taste_checker.py",
    "template_usability_tester.py",
    "tooling_manager.py",
    "ui_test_runner.py",
    "visual_regression_diff.py",
]

# Required top-level directories
REQUIRED_DIRS = [
    "memory", "products", "research", "design", "packaging",
    "distribution", "system", "templates", ".agents/agents", ".agents/skills",
]

# Required top-level files
REQUIRED_FILES = [
    "state.json",
    "AGENTS.md",
    "README.md",
    "memory/customers.json",
    "memory/opportunities.csv",
    "memory/sources.csv",
    "memory/decisions.md",
    "memory/rejected-ideas.md",
    "system/agent-map.md",
]

# Strings that must NOT appear in factory-level files when template is clean
# (product-specific contamination markers)
FORBIDDEN_PRODUCT_STRINGS = [
    "scope-shield",
    "scope_shield",
    "Scope Shield",
    "The Client Scope Shield",
    "OPP-001",
    "OPP-002",
    "OPP-003",
    "S.H.I.E.L.D. System",
    "Swiss Operational Modernism",
]

# Factory-level files to check for product contamination (not inside products/ dir)
CONTAMINATION_SCAN_FILES = [
    "state.json",
    "AGENTS.md",
    "README.md",
    "memory/customers.json",
    "memory/opportunities.csv",
    "memory/sources.csv",
    "memory/decisions.md",
    "memory/rejected-ideas.md",
    "system/agent-map.md",
]

# Clean state.json expected values
EXPECTED_STATE = {
    "workflow.stage": "idle",
    "workflow.status": "waiting_for_user",
    "opportunity.selected_id": None,
    "product.id": None,
    "product.name": None,
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

class CheckResult:
    def __init__(self):
        self.passes: List[str] = []
        self.failures: List[str] = []
        self.warnings: List[str] = []

    def ok(self, msg: str):
        self.passes.append(msg)

    def fail(self, msg: str):
        self.failures.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    @property
    def passed(self) -> bool:
        return len(self.failures) == 0


def get_nested(d: dict, dotted_key: str):
    """Retrieve a value from a nested dict using dot-notation key."""
    keys = dotted_key.split(".")
    current = d
    for k in keys:
        if not isinstance(current, dict) or k not in current:
            return "__MISSING__"
        current = current[k]
    return current


# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------

def check_required_directories(r: CheckResult):
    """Verify all required directories exist."""
    for d in REQUIRED_DIRS:
        path = REPO_ROOT / d
        if path.is_dir():
            r.ok(f"Directory exists: {d}")
        else:
            r.fail(f"MISSING directory: {d}")


def check_required_files(r: CheckResult):
    """Verify all required top-level files exist."""
    for f in REQUIRED_FILES:
        path = REPO_ROOT / f
        if path.is_file():
            r.ok(f"File exists: {f}")
        else:
            r.fail(f"MISSING file: {f}")


def check_agent_definitions(r: CheckResult):
    """Verify all 23 required agents have an agent.md file with YAML frontmatter."""
    agents_dir = REPO_ROOT / ".agents" / "agents"
    for agent_name in REQUIRED_AGENTS:
        agent_file = agents_dir / agent_name / "agent.md"
        if not agent_file.is_file():
            r.fail(f"MISSING agent definition: .agents/agents/{agent_name}/agent.md")
            continue

        content = agent_file.read_text(encoding="utf-8")

        # Check YAML frontmatter exists
        if not content.startswith("---"):
            r.fail(f"Agent '{agent_name}' agent.md lacks YAML frontmatter (must start with ---)")
            continue

        # Check required frontmatter fields
        for field in ["name:", "description:"]:
            if field not in content:
                r.fail(f"Agent '{agent_name}' missing frontmatter field: {field}")

        r.ok(f"Agent defined correctly: {agent_name}")


def check_schemas(r: CheckResult):
    """Verify all required JSON schemas exist and are valid JSON."""
    schemas_dir = REPO_ROOT / "system" / "schemas"
    for schema_file in REQUIRED_SCHEMAS:
        path = schemas_dir / schema_file
        if not path.is_file():
            r.fail(f"MISSING schema: system/schemas/{schema_file}")
            continue
        try:
            with open(path, encoding="utf-8") as f:
                json.load(f)
            r.ok(f"Schema valid JSON: {schema_file}")
        except json.JSONDecodeError as e:
            r.fail(f"Schema invalid JSON: {schema_file} — {e}")


def check_workflows(r: CheckResult):
    """Verify all required workflow documents exist and are non-empty."""
    workflows_dir = REPO_ROOT / "system" / "workflows"
    for wf in REQUIRED_WORKFLOWS:
        path = workflows_dir / wf
        if not path.is_file():
            r.fail(f"MISSING workflow: system/workflows/{wf}")
        elif path.stat().st_size == 0:
            r.fail(f"EMPTY workflow: system/workflows/{wf}")
        else:
            r.ok(f"Workflow present: {wf}")


def check_scripts(r: CheckResult):
    """Verify all required factory scripts exist."""
    scripts_dir = REPO_ROOT / "system" / "scripts"
    for script in REQUIRED_SCRIPTS:
        path = scripts_dir / script
        if not path.is_file():
            r.fail(f"MISSING script: system/scripts/{script}")
        else:
            r.ok(f"Script present: {script}")


def check_state_json(r: CheckResult):
    """Verify state.json is valid JSON and has clean initial values."""
    state_path = REPO_ROOT / "state.json"
    if not state_path.is_file():
        r.fail("state.json does not exist")
        return

    try:
        with open(state_path, encoding="utf-8") as f:
            state = json.load(f)
    except json.JSONDecodeError as e:
        r.fail(f"state.json is invalid JSON: {e}")
        return

    r.ok("state.json is valid JSON")

    for dotted_key, expected_value in EXPECTED_STATE.items():
        actual = get_nested(state, dotted_key)
        if actual == "__MISSING__":
            r.fail(f"state.json missing required key: {dotted_key}")
        elif actual != expected_value:
            r.fail(
                f"state.json dirty: {dotted_key} = {repr(actual)!r} "
                f"(expected {repr(expected_value)!r})"
            )
        else:
            r.ok(f"state.json clean: {dotted_key} = {repr(expected_value)!r}")


def check_delegation_log_schema(r: CheckResult):
    """Verify delegation-log.schema.json exists with required field definitions."""
    schema_path = REPO_ROOT / "system" / "schemas" / "delegation-log.schema.json"
    if not schema_path.is_file():
        r.fail("MISSING delegation-log.schema.json")
        return

    try:
        with open(schema_path, encoding="utf-8") as f:
            schema = json.load(f)
    except json.JSONDecodeError as e:
        r.fail(f"delegation-log.schema.json invalid JSON: {e}")
        return

    # Check required top-level fields in schema
    required_schema_props = ["stage", "required_agents", "invocations", "stage_status"]
    stage_record = (
        schema.get("definitions", {}).get("StageRecord", {}).get("properties", {})
    )
    for prop in required_schema_props:
        if prop in stage_record:
            r.ok(f"Delegation log schema has required property: StageRecord.{prop}")
        else:
            r.fail(f"Delegation log schema MISSING required property: StageRecord.{prop}")

    invocation = (
        schema.get("definitions", {}).get("Invocation", {}).get("properties", {})
    )
    required_invocation_props = [
        "agent", "task_id", "invocation_status", "start_time", "end_time",
        "result_artifact", "artifact_verified", "failure_reason",
    ]
    for prop in required_invocation_props:
        if prop in invocation:
            r.ok(f"Delegation log schema has required property: Invocation.{prop}")
        else:
            r.fail(f"Delegation log schema MISSING required property: Invocation.{prop}")


def check_product_contamination(r: CheckResult):
    """Scan factory-level files for forbidden product-specific strings."""
    for rel_path in CONTAMINATION_SCAN_FILES:
        path = REPO_ROOT / rel_path
        if not path.is_file():
            continue  # Missing file handled elsewhere
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            r.warn(f"Could not read file for contamination check: {rel_path}")
            continue

        found_contamination = False
        for forbidden in FORBIDDEN_PRODUCT_STRINGS:
            if forbidden in content:
                r.fail(
                    f"PRODUCT CONTAMINATION in {rel_path}: "
                    f"contains forbidden string '{forbidden}'"
                )
                found_contamination = True

        if not found_contamination:
            r.ok(f"No product contamination found in: {rel_path}")


def check_no_product_directories(r: CheckResult):
    """Verify no product-specific directories exist outside products/ sub-directories."""
    # Check design/ has no product subdirs (only README.md and empty dirs are fine)
    design_dir = REPO_ROOT / "design"
    if design_dir.is_dir():
        for child in design_dir.iterdir():
            if child.is_dir():
                r.fail(
                    f"Product directory still present in design/: design/{child.name} "
                    f"(product design systems belong to products/<id>/)"
                )

    # Check packaging/ has no product content files
    packaging_dir = REPO_ROOT / "packaging"
    if packaging_dir.is_dir():
        for child in packaging_dir.iterdir():
            if child.is_file() and child.suffix in [".md", ".json", ".html"] and child.name != "README.md":
                r.fail(
                    f"Product file still present in packaging/: packaging/{child.name}"
                )

    # Check distribution/ has no product content files
    dist_dir = REPO_ROOT / "distribution"
    if dist_dir.is_dir():
        for child in dist_dir.iterdir():
            if child.is_file() and child.suffix in [".md", ".json", ".html"] and child.name != "README.md":
                r.fail(
                    f"Product file still present in distribution/: distribution/{child.name}"
                )

    r.ok("Checked design/, packaging/, distribution/ for product contamination")


def check_memory_csv_headers(r: CheckResult):
    """Verify CSV memory files have correct headers and no product data rows."""
    files_headers = {
        "memory/opportunities.csv": "id,name,industry,customer,problem,overall_score",
        "memory/sources.csv": "source_id,url,title,author,published_at,retrieved_at",
    }
    for rel_path, expected_header_start in files_headers.items():
        path = REPO_ROOT / rel_path
        if not path.is_file():
            r.fail(f"MISSING memory file: {rel_path}")
            continue
        lines = path.read_text(encoding="utf-8").strip().splitlines()
        if not lines:
            r.fail(f"EMPTY memory file (needs at least header row): {rel_path}")
            continue
        if not lines[0].startswith(expected_header_start):
            r.fail(f"Wrong header in {rel_path}: got '{lines[0][:60]}...'")
        else:
            r.ok(f"CSV header correct: {rel_path}")
        if len(lines) > 1:
            # Has data rows — warn
            r.warn(f"{rel_path} has {len(lines) - 1} data row(s). Verify these are not leftover product data.")


def check_agent_map(r: CheckResult):
    """Verify agent-map.md exists and contains mandatory invocation rule."""
    agent_map_path = REPO_ROOT / "system" / "agent-map.md"
    if not agent_map_path.is_file():
        r.fail("MISSING system/agent-map.md")
        return
    content = agent_map_path.read_text(encoding="utf-8")
    checks = [
        ("MANDATORY INVOCATION RULE", "mandatory invocation rule"),
        ("invoke_subagent", "invoke_subagent reference"),
        ("STAGE COMPLETION GATES", "stage completion gates"),
        ("PARALLELIZATION", "parallelization rules"),
        ("WORKER TRUST RULE", "worker trust rule"),
    ]
    for keyword, label in checks:
        if keyword in content:
            r.ok(f"agent-map.md contains: {label}")
        else:
            r.fail(f"agent-map.md MISSING required section: {label}")


def check_readme_has_diagram(r: CheckResult):
    """Verify README.md contains a Mermaid diagram and delegation architecture description."""
    readme_path = REPO_ROOT / "README.md"
    if not readme_path.is_file():
        r.fail("MISSING README.md")
        return
    content = readme_path.read_text(encoding="utf-8")
    if "```mermaid" in content:
        r.ok("README.md contains Mermaid diagram")
    else:
        r.fail("README.md MISSING Mermaid diagram")
    if "invoke_subagent" in content or "MASTER" in content:
        r.ok("README.md describes Master/worker delegation architecture")
    else:
        r.warn("README.md may not describe delegation architecture clearly")


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_all_checks() -> Tuple[CheckResult, int]:
    r = CheckResult()

    print("=" * 60)
    print("AI PRODUCT FACTORY — HEALTH CHECK")
    print(f"Repository: {REPO_ROOT}")
    print("=" * 60)

    checks = [
        ("Required Directories",        check_required_directories),
        ("Required Files",              check_required_files),
        ("Agent Definitions",           check_agent_definitions),
        ("JSON Schemas",                check_schemas),
        ("Workflow Documents",          check_workflows),
        ("Factory Scripts",             check_scripts),
        ("state.json",                  check_state_json),
        ("Delegation Log Schema",       check_delegation_log_schema),
        ("Product Contamination Scan",  check_product_contamination),
        ("Product Directories",         check_no_product_directories),
        ("Memory CSV Headers",          check_memory_csv_headers),
        ("Agent Map",                   check_agent_map),
        ("README Diagram",              check_readme_has_diagram),
    ]

    for section_name, check_fn in checks:
        print(f"\n── {section_name} ──")
        check_fn(r)
        # Print results for this section
        for msg in r.passes[-20:]:  # show recent passes (simple approach)
            pass  # Will print summary at end

    # Print full summary
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)

    if r.failures:
        print(f"\n❌ FAILURES ({len(r.failures)}):")
        for f in r.failures:
            print(f"  FAIL  {f}")

    if r.warnings:
        print(f"\n⚠️  WARNINGS ({len(r.warnings)}):")
        for w in r.warnings:
            print(f"  WARN  {w}")

    print(f"\n✅ PASSES ({len(r.passes)})")

    print("\n" + "=" * 60)
    if r.passed:
        print("OVERALL: ✅ PASS")
        print("The factory template is in a clean, correctly configured state.")
    else:
        print(f"OVERALL: ❌ FAIL ({len(r.failures)} failure(s))")
        print("Resolve the listed failures before deploying this template.")
    print("=" * 60)

    return r, (0 if r.passed else 1)


if __name__ == "__main__":
    result, exit_code = run_all_checks()
    sys.exit(exit_code)
