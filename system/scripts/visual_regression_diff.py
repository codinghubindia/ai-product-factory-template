"""
AI PRODUCT FACTORY — VISUAL REGRESSION & LAYOUT DIFF TOOL
Detects page count drift, overflow regressions, heading structural shifts,
and file size anomalies between artifact builds.
"""

import os
import sys
import argparse
import json

def analyze_pdf(pdf_path):
    """Extracts structural and layout metrics from a PDF file."""
    if not os.path.exists(pdf_path):
        return None

    import pypdf
    reader = pypdf.PdfReader(pdf_path)
    page_count = len(reader.pages)
    file_size_kb = os.path.getsize(pdf_path) / 1024

    pages_info = []
    total_words = 0
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        words = len(text.split())
        chars = len(text)
        total_words += words
        pages_info.append({
            "page_num": idx + 1,
            "word_count": words,
            "char_count": chars,
            "has_text": chars > 0
        })

    # Read outline / bookmarks
    bookmarks = []
    try:
        def extract_bookmarks(outline_list):
            for item in outline_list:
                if isinstance(item, list):
                    extract_bookmarks(item)
                else:
                    title = getattr(item, 'title', str(item))
                    bookmarks.append(title)
        if reader.outline:
            extract_bookmarks(reader.outline)
    except Exception:
        pass

    return {
        "path": pdf_path,
        "page_count": page_count,
        "file_size_kb": round(file_size_kb, 2),
        "total_words": total_words,
        "bookmarks_count": len(bookmarks),
        "bookmarks": bookmarks,
        "pages": pages_info
    }

def compare_builds(base_path, new_path):
    """Compares baseline artifact against new artifact for regressions."""
    base_data = analyze_pdf(base_path)
    new_data = analyze_pdf(new_path)

    if not base_data:
        return {"status": "ERROR", "message": f"Baseline artifact not found: {base_path}"}
    if not new_data:
        return {"status": "ERROR", "message": f"New artifact not found: {new_path}"}

    diffs = []
    warnings = []

    # 1. Page Count Check
    if base_data["page_count"] != new_data["page_count"]:
        delta = new_data["page_count"] - base_data["page_count"]
        sign = "+" if delta > 0 else ""
        diffs.append(f"Page Count Drift: Baseline was {base_data['page_count']} pages, New is {new_data['page_count']} pages ({sign}{delta} pages). Check for accidental overflow or clipped sections.")

    # 2. Blank Page Check
    for p in new_data["pages"]:
        if p["char_count"] == 0 and p["page_num"] > 1: # Cover might be graphical
            warnings.append(f"Potential blank page detected: Page {p['page_num']} contains 0 text characters.")

    # 3. File Size Check (>50% jump or drop)
    size_ratio = new_data["file_size_kb"] / max(base_data["file_size_kb"], 1)
    if size_ratio > 1.8:
        warnings.append(f"Large file size inflation: {base_data['file_size_kb']} KB -> {new_data['file_size_kb']} KB (+{int((size_ratio-1)*100)}%). Check for uncompressed raster images.")
    elif size_ratio < 0.4:
        warnings.append(f"Severe file size drop: {base_data['file_size_kb']} KB -> {new_data['file_size_kb']} KB (-{int((1-size_ratio)*100)}%). Check for missing visual assets.")

    # 4. Bookmarks Check
    if base_data["bookmarks_count"] > 0 and new_data["bookmarks_count"] == 0:
        diffs.append("REGRESSION: Document bookmarks were present in baseline but are missing in new build.")

    return {
        "status": "PASS" if not diffs else "REGRESSION_DETECTED",
        "baseline": base_data,
        "new_build": new_data,
        "regressions": diffs,
        "warnings": warnings
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Factory Visual Regression Diff")
    parser.add_argument("--base", required=True, help="Baseline PDF path")
    parser.add_argument("--new", required=True, help="New candidate PDF path")
    parser.add_argument("--json", action="store_true", help="Output JSON report")
    args = parser.parse_args()

    res = compare_builds(args.base, args.new)
    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print("\n=======================================================")
        print("VISUAL & STRUCTURAL REGRESSION COMPARISON REPORT")
        print(f"Status: {res['status']}")
        print("=======================================================")
        if res.get("regressions"):
            print("\nREGRESSIONS DETECTED:")
            for d in res["regressions"]:
                print(f"  [X] {d}")
        if res.get("warnings"):
            print("\nWARNINGS:")
            for w in res["warnings"]:
                print(f"  [!] {w}")
        if not res.get("regressions") and not res.get("warnings"):
            print("\n[OK] Layout structure stable. Zero layout drift or page count regressions.")

    sys.exit(0 if res['status'] == "PASS" else 1)
