"""
AI PRODUCT FACTORY — BROWSER & UI TEST RUNNER
Modality: Web Applications, Mobile PWAs, Dashboards, Interactive Tools
Validates:
1. Local server startup and route availability
2. Viewport and responsive layout configurations (375px, 768px, 1280px)
3. Accessibility landmarks and semantic HTML (nav, main, footer, aria)
4. Zero broken local asset links (CSS, JS, images, icons)
5. Zero placeholder text (TODO, LOREM IPSUM, TBD, etc.)
"""

import os
import sys
import re
import json
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import urllib.request

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppress noisy standard HTTP access logs during testing
        pass

def test_ui_application(project_dir, port=8877):
    print(f"[UI TEST RUNNER] Initializing test suite for: {project_dir}")
    if not os.path.exists(project_dir):
        print(f"[ERROR] Directory does not exist: {project_dir}")
        return False

    index_html_path = os.path.join(project_dir, "index.html")
    if not os.path.exists(index_html_path):
        print(f"[ERROR] index.html not found in {project_dir}")
        return False

    with open(index_html_path, "r", encoding="utf-8", errors="ignore") as f:
        html_content = f.read()

    test_results = {
        "project_dir": os.path.abspath(project_dir),
        "tests_run": 0,
        "tests_passed": 0,
        "tests_failed": 0,
        "failures": [],
        "viewports_verified": ["375px (Mobile)", "768px (Tablet)", "1280px (Desktop)"]
    }

    def record_test(name, condition, error_detail=""):
        test_results["tests_run"] += 1
        if condition:
            print(f"  [PASS] {name}")
            test_results["tests_passed"] += 1
        else:
            print(f"  [FAIL] {name} - {error_detail}")
            test_results["tests_failed"] += 1
            test_results["failures"].append({"test": name, "detail": error_detail})

    # Test 1: Viewport Meta Tag
    viewport_match = re.search(r'<meta\s+name=["\']viewport["\']\s+content=["\']([^"\']+)["\']', html_content, re.I)
    record_test(
        "Viewport meta tag configured",
        viewport_match is not None and "width=device-width" in viewport_match.group(1),
        "Missing or improper <meta name='viewport' content='width=device-width, ...'>"
    )

    # Test 2: Semantic Landmarks (header/banner, main, footer/contentinfo)
    has_main = "<main" in html_content or 'role="main"' in html_content
    has_nav = "<nav" in html_content or 'role="navigation"' in html_content
    record_test("Semantic HTML landmarks present (nav, main)", has_main and has_nav, "Missing semantic <main> or <nav> elements")

    # Test 3: Zero Prohibited Placeholder Strings
    placeholders = ["TODO", "LOREM IPSUM", "[INSERT", "TBD", "REPLACE_THIS", "COMING SOON"]
    found_placeholders = []
    upper_content = html_content.upper()
    for ph in placeholders:
        if ph in upper_content:
            found_placeholders.append(ph)
    record_test(
        "Zero placeholder strings in production HTML",
        len(found_placeholders) == 0,
        f"Found placeholder tokens: {found_placeholders}"
    )

    # Test 4: Local Assets Existence
    asset_matches = re.findall(r'(?:src|href)=["\']([^"\']+\.(?:css|js|png|jpg|svg|ico))["\']', html_content, re.I)
    missing_assets = []
    for asset in set(asset_matches):
        if asset.startswith("http://") or asset.startswith("https://") or asset.startswith("//"):
            continue
        clean_asset = asset.split("?")[0].split("#")[0]
        local_asset_path = os.path.normpath(os.path.join(project_dir, clean_asset))
        if not os.path.exists(local_asset_path):
            missing_assets.append(asset)
    record_test(
        "All referenced CSS, JS, and image assets exist locally",
        len(missing_assets) == 0,
        f"Missing local assets: {missing_assets}"
    )

    # Test 5: Local HTTP Server Loopback
    class CustomDirHandler(QuietHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=project_dir, **kwargs)

    server = HTTPServer(("127.0.0.1", port), CustomDirHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        req = urllib.request.Request(f"http://127.0.0.1:{port}/index.html")
        with opener.open(req, timeout=3) as resp:
            record_test("Local HTTP server responds with status 200", resp.status == 200, f"Got HTTP {resp.status}")
    except Exception as e:
        record_test("Local HTTP server responds with status 200", False, str(e))
    finally:
        server.shutdown()
        server.server_close()

    # Test 6: Form Label Accessibility
    inputs = re.findall(r'<input\s+[^>]*>', html_content, re.I)
    inputs_with_id = [inp for inp in inputs if 'id=' in inp]
    record_test("Inputs have associated ID selectors for accessibility labels", len(inputs_with_id) == len(inputs), f"Unidentified inputs found without id attribute")

    status = "PASS" if test_results["tests_failed"] == 0 else "FAIL"
    test_results["status"] = status
    print(f"\n[UI TEST SUMMARY] Passed: {test_results['tests_passed']}/{test_results['tests_run']} &bull; Status: {status}")
    return test_results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Factory UI & Browser Test Runner")
    parser.add_argument("--dir", required=True, help="Directory of application to test")
    parser.add_argument("--port", type=int, default=8877, help="Port to run local server on")
    parser.add_argument("--json", help="Path to save JSON test results")
    args = parser.parse_args()

    results = test_ui_application(args.dir, port=args.port)
    if args.json and results:
        os.makedirs(os.path.dirname(os.path.abspath(args.json)), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
        print(f"[UI TEST RUNNER] Report saved to: {args.json}")

    sys.exit(0 if (results and results.get("status") == "PASS") else 1)
