"""
AI PRODUCT FACTORY — TASTE & AESTHETIC AUDITOR
Scans deliverables for generic AI clichés, unformatted numbers, neon gradients,
glassmorphism, wall-of-bullets, and unergonomic writing spaces.
"""

import os
import sys
import re
import argparse
import json

AI_CLICHE_PATTERNS = [
    r"\bin today's (?:fast-paced|dynamic|digital|ever-changing) world\b",
    r"\bdelve into\b",
    r"\ba testament to\b",
    r"\brevolutionize your (?:workflow|business|life|process)\b",
    r"\bempower your (?:team|organization|journey)\b",
    r"\bgame-changer\b",
    r"\bharness(?:ing)? the power of\b",
    r"\bseamless(?:ly)? integrat(?:e|ion|ed)\b",
    r"\bcutting-edge\b",
    r"\bunleash your potential\b",
    r"\bit's important to remember that\b",
    r"\bfirst and foremost\b",
    r"\blasting impression\b"
]

def audit_taste_and_aesthetics(target_path):
    """
    Audits an HTML, Markdown, or text file for taste, editorial maturity, and anti-AI-slop compliance.
    """
    if not os.path.exists(target_path):
        return {"status": "FAIL", "error": f"Target path not found: {target_path}"}

    defects = []
    warnings = []
    metrics = {"cliches_found": 0, "unformatted_floats": 0, "styling_violations": 0}

    with open(target_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # 1. AI Cliché & Platitude Scan
    for pat in AI_CLICHE_PATTERNS:
        matches = list(re.finditer(pat, content, re.IGNORECASE))
        if matches:
            metrics["cliches_found"] += len(matches)
            for m in matches[:3]: # Cap reporting
                start = max(0, m.start() - 30)
                end = min(len(content), m.end() + 30)
                snippet = content[start:end].replace("\n", " ")
                warnings.append(f"Generic AI trope detected: '{m.group(0)}' in: \"...{snippet}...\"")

    # 2. Raw Unformatted Floating Point Numbers in HTML/text (>3 decimals)
    float_matches = re.findall(r'>\s*(\d+\.\d{3,})\s*<', content)
    if float_matches:
        metrics["unformatted_floats"] += len(float_matches)
        warnings.append(f"Found {len(float_matches)} unformatted float(s) (e.g. '{float_matches[0]}'). Apply explicit currency, percentage, or rounded formatting.")

    # 3. CSS Styling Red Flags (Neon Gradients, Glassmorphism, Unconstrained Measure)
    if "linear-gradient" in content:
        # Check for neon gradients
        if re.search(r'#(?:ff00|00ff|ff00ff|00ffff)', content, re.IGNORECASE):
            defects.append("CRITICAL: Prohibited neon gradient detected. Use disciplined semantic palette tokens.")
            metrics["styling_violations"] += 1

    if "backdrop-filter: blur" in content and ("p {" in content or "<p" in content):
        warnings.append("Glassmorphism detected on text containers; verify readability against WCAG AA standards.")
        metrics["styling_violations"] += 1

    # 4. Handwriting Line Spacing in Workbooks
    if "handwriting" in content or "workbook" in content:
        line_height_match = re.search(r'--rule-height:\s*(\d+)pt', content)
        if line_height_match:
            pt_val = int(line_height_match.group(1))
            if pt_val < 24: # Less than 8mm
                defects.append(f"CRITICAL: Workbook rule height is {pt_val}pt (< 24pt/8mm). Physically unergonomic for handwriting.")

    # 5. Wall of Bullets Scan (> 6 consecutive <li> without bold lead-ins)
    li_matches = re.findall(r'<li>(.*?)</li>', content, re.DOTALL)
    unstructured_lis = 0
    for li in li_matches:
        text = li.strip()
        if not text.startswith("<strong>") and not text.startswith("<b>"):
            unstructured_lis += 1
    if unstructured_lis > 8:
        warnings.append(f"Found {unstructured_lis} bullet points without bold lead-in phrases. Use structured formatting for readability.")

    passed = len(defects) == 0
    return {
        "status": "PASS" if passed else "FAIL",
        "file": target_path,
        "metrics": metrics,
        "critical_defects": defects,
        "warnings": warnings
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Factory Taste & Anti-AI-Slop Auditor")
    parser.add_argument("--input", required=True, help="Path to file to audit")
    parser.add_argument("--json", action="store_true", help="Output JSON report")
    args = parser.parse_args()

    res = audit_taste_and_aesthetics(args.input)
    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print("\n=======================================================")
        print(f"TASTE & AESTHETIC AUDIT: {res['file']}")
        print(f"Status: {res['status']}")
        print(f"Metrics: Clichés={res['metrics']['cliches_found']}, Unformatted Floats={res['metrics']['unformatted_floats']}, Style Violations={res['metrics']['styling_violations']}")
        print("=======================================================")
        if res.get("critical_defects"):
            print(f"\nCRITICAL DEFECTS ({len(res['critical_defects'])}):")
            for d in res["critical_defects"]:
                print(f"  [X] {d}")
        if res.get("warnings"):
            print(f"\nTASTE & STYLE WARNINGS ({len(res['warnings'])}):")
            for w in res["warnings"]:
                print(f"  [!] {w}")
        if not res.get("critical_defects") and not res.get("warnings"):
            print("\n[OK] Deliverable demonstrates high editorial maturity, restraint, and zero AI clichés.")

    sys.exit(0 if res['status'] == "PASS" else 1)
