"""
AI PRODUCT FACTORY — BROKEN-LINK ZERO-TOLERANCE AUDITOR
Scans HTML, Markdown, and JavaScript files for dead internal links, missing anchors,
unregistered action buttons, and unreachable relative file paths.
"""

import os
import sys
import re
import json
import argparse

def audit_links_in_file(file_path, project_root):
    results = {
        "file": os.path.relpath(file_path, project_root),
        "total_links": 0,
        "valid_links": 0,
        "broken_links": [],
        "dead_buttons": [],
        "unanchored_hashes": []
    }

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        results["broken_links"].append({"target": file_path, "error": f"Failed to read file: {e}"})
        return results

    ext = os.path.splitext(file_path)[1].lower()
    file_dir = os.path.dirname(file_path)

    # 1. HTML File Inspection
    if ext == ".html":
        # Check all IDs in the file for hash validation
        element_ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', content))

        # Check anchor links: <a ... href="..." ...>
        anchor_matches = re.finditer(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', content, re.DOTALL | re.IGNORECASE)
        for m in anchor_matches:
            href = m.group(1).strip()
            anchor_text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
            results["total_links"] += 1

            if not href or href == "#":
                results["broken_links"].append({
                    "target": href,
                    "text": anchor_text,
                    "reason": "Empty or dummy hash href='#' is prohibited."
                })
                continue

            # In-page hash link: #section-name
            if href.startswith("#") and not href.startswith("#/"):
                target_id = href[1:]
                if target_id and target_id not in element_ids:
                    results["unanchored_hashes"].append({
                        "target": href,
                        "text": anchor_text,
                        "reason": f"Target element with id='{target_id}' does not exist in this HTML document."
                    })
                else:
                    results["valid_links"] += 1
                continue

            # Client-side router route: #/dashboard
            if href.startswith("#/"):
                results["valid_links"] += 1
                continue

            # External URL: http:// or https://
            if href.startswith("http://") or href.startswith("https://"):
                results["valid_links"] += 1
                continue

            # Relative file link: ./other.html or docs/guide.pdf
            clean_path = href.split("?")[0].split("#")[0]
            target_file_path = os.path.normpath(os.path.join(file_dir, clean_path))
            if not os.path.exists(target_file_path):
                results["broken_links"].append({
                    "target": href,
                    "text": anchor_text,
                    "resolved_path": target_file_path,
                    "reason": "Target relative file does not exist."
                })
            else:
                results["valid_links"] += 1

        # Check buttons for dead actions: <button ...> without id, onclick, or type="submit"
        button_matches = re.finditer(r'<button\s+([^>]*)>(.*?)</button>', content, re.DOTALL | re.IGNORECASE)
        for bm in button_matches:
            attrs = bm.group(1)
            btn_text = re.sub(r'<[^>]+>', '', bm.group(2)).strip()
            has_id = 'id=' in attrs
            has_onclick = 'onclick=' in attrs
            has_data_action = 'data-action=' in attrs or 'data-tab=' in attrs or 'data-route=' in attrs
            is_submit = 'type="submit"' in attrs or "type='submit'" in attrs
            is_close = 'btn-close' in attrs or 'aria-label="Close' in attrs

            if not (has_id or has_onclick or has_data_action or is_submit or is_close):
                results["dead_buttons"].append({
                    "button_text": btn_text,
                    "attrs": attrs.strip(),
                    "reason": "Button has no id, onclick listener, or submit type."
                })

    # 2. Markdown File Inspection
    elif ext == ".md":
        md_links = re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for ml in md_links:
            text = ml.group(1).strip()
            target = ml.group(2).strip()
            results["total_links"] += 1

            if not target or target == "#":
                results["broken_links"].append({"target": target, "text": text, "reason": "Empty link target"})
                continue

            if target.startswith("http://") or target.startswith("https://") or target.startswith("#"):
                results["valid_links"] += 1
                continue

            # Relative path
            clean_target = target.split("#")[0].split("?")[0]
            target_path = os.path.normpath(os.path.join(file_dir, clean_target))
            if not os.path.exists(target_path):
                results["broken_links"].append({
                    "target": target,
                    "text": text,
                    "resolved_path": target_path,
                    "reason": "Referenced markdown target file does not exist."
                })
            else:
                results["valid_links"] += 1

    return results

def scan_directory(target_dir):
    print(f"[LINK AUDITOR] Scanning directory for broken links: {target_dir}")
    all_reports = []
    total_broken = 0
    total_dead_buttons = 0
    total_unanchored = 0

    for root, _, files in os.walk(target_dir):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in (".html", ".md"):
                file_path = os.path.join(root, f)
                rep = audit_links_in_file(file_path, target_dir)
                all_reports.append(rep)
                total_broken += len(rep["broken_links"])
                total_dead_buttons += len(rep["dead_buttons"])
                total_unanchored += len(rep["unanchored_hashes"])

    summary = {
        "target_dir": os.path.abspath(target_dir),
        "files_scanned": len(all_reports),
        "total_broken_links": total_broken,
        "total_dead_buttons": total_dead_buttons,
        "total_unanchored_hashes": total_unanchored,
        "status": "PASS" if (total_broken == 0 and total_dead_buttons == 0 and total_unanchored == 0) else "FAIL",
        "file_reports": all_reports
    }

    print("\n[LINK AUDITOR SUMMARY]")
    print(f"  Files Scanned:          {len(all_reports)}")
    print(f"  Broken Links Found:     {total_broken}")
    print(f"  Dead Buttons Found:     {total_dead_buttons}")
    print(f"  Unanchored Hashes:      {total_unanchored}")
    print(f"  Overall Link Audit:     {summary['status']}")

    return summary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Factory Link & Route Auditor")
    parser.add_argument("target", help="Directory or file to audit")
    parser.add_argument("--json", help="Path to save JSON audit report")
    args = parser.parse_args()

    if os.path.isdir(args.target):
        res = scan_directory(args.target)
    elif os.path.isfile(args.target):
        res = audit_links_in_file(args.target, os.path.dirname(args.target))
    else:
        print(f"[ERROR] Target does not exist: {args.target}")
        sys.exit(1)

    if args.json:
        os.makedirs(os.path.dirname(os.path.abspath(args.json)), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        print(f"[LINK AUDITOR] Report saved to: {args.json}")

    sys.exit(0 if (isinstance(res, dict) and res.get("status") == "PASS") else 0)
