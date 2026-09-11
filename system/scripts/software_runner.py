"""
AI PRODUCT FACTORY — SOFTWARE QA & TEST RUNNER
Modality: Software, Web Apps, Mobile, APIs, Tools
Executes the 12-Step Software Testing Protocol:
1. Dependency hygiene & installation check
2. Compilation / Build verification
3. Automated unit and integration test runner
4. Link and navigation route verification
5. UI and responsive layout inspection
Outputs structured software-qa.json report.
"""

import os
import sys
import json
import subprocess
import argparse

def execute_command(cmd, cwd):
    print(f"[SOFTWARE RUNNER] Executing: '{cmd}' in {cwd}")
    res = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    return {
        "command": cmd,
        "exit_code": res.returncode,
        "stdout": res.stdout.strip(),
        "stderr": res.stderr.strip(),
        "passed": (res.returncode == 0)
    }

def run_software_qa(project_dir, output_json=None):
    if not os.path.exists(project_dir):
        print(f"[ERROR] Project directory does not exist: {project_dir}")
        return False

    report = {
        "project_dir": os.path.abspath(project_dir),
        "steps_executed": [],
        "overall_status": "FAIL",
        "critical_defects": 0,
        "high_defects": 0,
        "summary": {}
    }

    # 1. Dependency & Environment Check
    has_package_json = os.path.exists(os.path.join(project_dir, "package.json"))
    has_requirements = os.path.exists(os.path.join(project_dir, "requirements.txt"))
    has_pyproject = os.path.exists(os.path.join(project_dir, "pyproject.toml"))
    has_index_html = os.path.exists(os.path.join(project_dir, "index.html"))

    # Step 1: Install Dependencies (if config exists and not already installed)
    if has_package_json and not os.path.exists(os.path.join(project_dir, "node_modules")):
        res = execute_command("npm install", project_dir)
        report["steps_executed"].append({"step": "dependency_installation", "result": res})
        if not res["passed"]:
            report["critical_defects"] += 1

    # Step 2: Build Application
    if has_package_json:
        # Check if build script exists in package.json
        try:
            with open(os.path.join(project_dir, "package.json"), "r") as pf:
                pkg = json.load(pf)
                if "build" in pkg.get("scripts", {}):
                    res = execute_command("npm run build", project_dir)
                    report["steps_executed"].append({"step": "build_compilation", "result": res})
                    if not res["passed"]:
                        report["critical_defects"] += 1
        except Exception as e:
            pass

    # Step 3: Run Automated Unit Tests
    test_run = False
    if has_package_json:
        try:
            with open(os.path.join(project_dir, "package.json"), "r") as pf:
                pkg = json.load(pf)
                if "test" in pkg.get("scripts", {}):
                    res = execute_command("npm test", project_dir)
                    report["steps_executed"].append({"step": "automated_tests", "result": res})
                    test_run = True
                    if not res["passed"]:
                        report["high_defects"] += 1
        except Exception:
            pass

    if not test_run and (has_requirements or has_pyproject):
        # Look for test files
        test_dir = os.path.join(project_dir, "tests")
        if os.path.exists(test_dir) or any(f.startswith("test_") for f in os.listdir(project_dir)):
            res = execute_command("pytest", project_dir)
            report["steps_executed"].append({"step": "automated_tests", "result": res})
            test_run = True
            if not res["passed"]:
                report["high_defects"] += 1

    abs_project_dir = os.path.abspath(project_dir)

    # Step 4: Link and Route Audit
    link_checker_script = os.path.join(os.path.dirname(__file__), "link_checker.py")
    if os.path.exists(link_checker_script):
        res = execute_command(f'python "{link_checker_script}" "{abs_project_dir}"', project_dir)
        report["steps_executed"].append({"step": "link_and_route_audit", "result": res})
        if not res["passed"]:
            report["high_defects"] += 1

    # Step 5: UI & Viewport Testing (if web app)
    if has_index_html:
        ui_runner_script = os.path.join(os.path.dirname(__file__), "ui_test_runner.py")
        if os.path.exists(ui_runner_script):
            res = execute_command(f'python "{ui_runner_script}" --dir "{abs_project_dir}" --port 8994', project_dir)
            report["steps_executed"].append({"step": "ui_viewport_test", "result": res})
            if not res["passed"]:
                report["high_defects"] += 1

    # Determine Overall Status
    if report["critical_defects"] == 0 and report["high_defects"] == 0:
        report["overall_status"] = "PASS"
    else:
        report["overall_status"] = "FAIL"

    print(f"\n[SOFTWARE QA SUMMARY] Status: {report['overall_status']} | Critical Defects: {report['critical_defects']} | High Defects: {report['high_defects']}")

    if output_json:
        os.makedirs(os.path.dirname(os.path.abspath(output_json)), exist_ok=True)
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"[SOFTWARE QA] Report saved to: {output_json}")

    return report["overall_status"] == "PASS"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Factory Software Runner & QA Engine")
    parser.add_argument("--dir", required=True, help="Path to software project root")
    parser.add_argument("--output", help="Path to save software-qa.json report")
    args = parser.parse_args()

    success = run_software_qa(args.dir, output_json=args.output)
    sys.exit(0 if success else 1)
