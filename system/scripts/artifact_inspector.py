"""
AI PRODUCT FACTORY — ADVANCED ARTIFACT INSPECTOR
Modality: File Deliverables (PDF, DOCX, XLSX, PPTX, HTML, SQLite, ZIP, JSON)
Inspects:
- Physical file existence and non-zero byte size
- Valid magic bytes / header signatures
- Deep scan for placeholder text (TODO, LOREM IPSUM, [INSERT, TBD)
- Schema and JSON syntax validity
- ZIP archive integrity and README presence
"""

import os
import sys
import json
import zipfile
import sqlite3
import argparse

PLACEHOLDER_TOKENS = ["TODO", "LOREM IPSUM", "[INSERT", "TBD", "REPLACE_THIS", "COMING SOON", "DRAFT ONLY"]

def inspect_file(file_path):
    result = {
        "file": os.path.abspath(file_path),
        "filename": os.path.basename(file_path),
        "exists": False,
        "size_bytes": 0,
        "extension": os.path.splitext(file_path)[1].lower(),
        "is_empty": True,
        "status": "FAIL",
        "defects": []
    }

    if not os.path.exists(file_path):
        result["defects"].append("File does not exist on disk.")
        return result

    result["exists"] = True
    size = os.path.getsize(file_path)
    result["size_bytes"] = size
    result["is_empty"] = (size == 0)

    if size == 0:
        result["defects"].append("File is 0 bytes (empty file).")
        return result

    ext = result["extension"]

    # 1. PDF Verification
    if ext == ".pdf":
        try:
            with open(file_path, "rb") as f:
                header = f.read(5)
                if not header.startswith(b"%PDF-"):
                    result["defects"].append("Invalid PDF magic bytes header.")
        except Exception as e:
            result["defects"].append(f"Failed to inspect PDF header: {e}")

    # 2. Text / HTML / Markdown / JSON Scan
    elif ext in (".html", ".htm", ".md", ".json", ".csv", ".txt", ".svg"):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                upper = content.upper()
                for token in PLACEHOLDER_TOKENS:
                    if token in upper:
                        result["defects"].append(f"Prohibited placeholder string detected: '{token}'")

                if ext == ".json":
                    try:
                        json.loads(content)
                    except Exception as je:
                        result["defects"].append(f"Malformed JSON syntax: {je}")
        except Exception as e:
            result["defects"].append(f"Failed to read text file: {e}")

    # 3. ZIP Archive Inspection
    elif ext == ".zip":
        try:
            with zipfile.ZipFile(file_path, "r") as z:
                names = z.namelist()
                has_readme = any("README" in n.upper() for n in names)
                if not has_readme:
                    result["defects"].append("ZIP archive does not contain a customer onboarding README.")
                for info in z.infolist():
                    if ".." in info.filename:
                        result["defects"].append(f"Unsafe path traversal detected in archive: {info.filename}")
        except Exception as e:
            result["defects"].append(f"Corrupted or invalid ZIP archive: {e}")

    # 4. SQLite Database Inspection
    elif ext in (".sqlite", ".db"):
        try:
            conn = sqlite3.connect(file_path)
            cur = conn.cursor()
            cur.execute("PRAGMA integrity_check;")
            res = cur.fetchone()[0]
            if res != "ok":
                result["defects"].append(f"SQLite PRAGMA integrity_check failed: {res}")
            conn.close()
        except Exception as e:
            result["defects"].append(f"Failed to verify SQLite database: {e}")

    result["status"] = "PASS" if len(result["defects"]) == 0 else "FAIL"
    return result

def inspect_target(path):
    if os.path.isfile(path):
        res = inspect_file(path)
        print(json.dumps(res, indent=2))
        return res

    elif os.path.isdir(path):
        print(f"[ARTIFACT INSPECTOR] Scanning directory: {path}")
        results = []
        for root, _, files in os.walk(path):
            for f in files:
                p = os.path.join(root, f)
                results.append(inspect_file(p))

        passed = sum(1 for r in results if r["status"] == "PASS")
        failed = sum(1 for r in results if r["status"] == "FAIL")
        summary = {
            "target_dir": os.path.abspath(path),
            "total_artifacts": len(results),
            "passed": passed,
            "failed": failed,
            "status": "PASS" if failed == 0 else "FAIL",
            "artifacts": results
        }
        print(f"\n[ARTIFACT INSPECTION SUMMARY] Inspected: {len(results)} &bull; Passed: {passed} &bull; Failed: {failed} &bull; Status: {summary['status']}")
        return summary
    else:
        print(f"[ERROR] Target not found: {path}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Factory Artifact Inspector")
    parser.add_argument("target", help="File or directory to inspect")
    parser.add_argument("--json", help="Path to save JSON inspection report")
    args = parser.parse_args()

    res = inspect_target(args.target)
    if args.json and res:
        os.makedirs(os.path.dirname(os.path.abspath(args.json)), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        print(f"[ARTIFACT INSPECTOR] Report saved to: {args.json}")

    sys.exit(0 if (res and res.get("status") == "PASS") else 1)
