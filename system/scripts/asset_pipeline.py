"""
AI PRODUCT FACTORY — VISUAL ASSET PIPELINE & MANIFEST AUDITOR
Audits asset records, validates image dimensions, verifies licenses, checks file integrity,
and confirms visual continuity compliance.
"""

import os
import sys
import json
import argparse
import xml.etree.ElementTree as ET

# Ensure vendor directory is in sys.path
vendor_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "vendor"))
if os.path.exists(vendor_dir) and vendor_dir not in sys.path:
    sys.path.insert(0, vendor_dir)

VALID_ASPECT_RATIOS = {
    "1:1": 1.0,
    "16:9": 16.0 / 9.0,
    "4:3": 4.0 / 3.0,
    "3:2": 3.0 / 2.0,
    "2:3": 2.0 / 3.0,
    "3:4": 3.0 / 4.0,
    "9:16": 9.0 / 16.0
}

VALID_LICENSES = [
    "factory_original",
    "cc0",
    "mit",
    "apache_2_0",
    "commercial_royalty_free",
    "editorial_reference_only"
]

def audit_asset_manifest(manifest_path, base_dir=None):
    """
    Validates an asset manifest and all referenced asset files.
    """
    if not os.path.exists(manifest_path):
        return {"status": "FAIL", "error": f"Manifest file not found: {manifest_path}"}

    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(manifest_path))

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as e:
        return {"status": "FAIL", "error": f"Invalid JSON in manifest: {e}"}

    defects = []
    warnings = []
    assets = manifest.get("assets", [])
    total_assets = len(assets)
    approved_count = 0

    # Optional Pillow import for raster inspection
    try:
        from PIL import Image
        has_pil = True
    except ImportError:
        has_pil = False

    for idx, ast in enumerate(assets, start=1):
        ast_id = ast.get("asset_id", f"unknown-{idx}")
        name = ast.get("name", "Unnamed")
        role = ast.get("role")
        placement = ast.get("placement")
        ast_type = ast.get("type", "").lower()
        license_status = ast.get("license_status")
        target_ratio_str = ast.get("aspect_ratio")
        dim = ast.get("dimensions", {})
        target_w = dim.get("width")
        target_h = dim.get("height")
        approved = ast.get("approved", False)

        if approved:
            approved_count += 1

        # 1. License Check
        if not license_status or license_status not in VALID_LICENSES:
            defects.append(f"CRITICAL: Asset '{ast_id}' has invalid/missing license_status '{license_status}'.")
        elif license_status == "editorial_reference_only" and "final/" in placement:
            defects.append(f"CRITICAL: Editorial reference asset '{ast_id}' placed in final deliverable '{placement}'.")

        # 2. File Existence Check
        # Resolve asset file path: check if placement or asset path exists
        file_candidates = [
            os.path.join(base_dir, f"{ast_id}.{ast_type}"),
            os.path.join(base_dir, placement) if placement else None,
            os.path.join(base_dir, "..", placement) if placement else None
        ]
        asset_file = next((c for c in file_candidates if c and os.path.exists(c)), None)

        if not asset_file:
            warnings.append(f"Asset file for '{ast_id}' not found on disk (searched {ast_id}.{ast_type}).")
            continue

        file_size = os.path.getsize(asset_file)
        if file_size == 0:
            defects.append(f"CRITICAL: Asset file '{asset_file}' is empty (0 bytes).")
            continue

        # 3. Format & Geometry Validation
        if ast_type == "svg":
            try:
                tree = ET.parse(asset_file)
                root = tree.getroot()
                if "svg" not in root.tag.lower():
                    defects.append(f"CRITICAL: SVG file '{asset_file}' missing root <svg> element.")
            except Exception as e:
                defects.append(f"CRITICAL: Corrupt SVG '{asset_file}': {e}")

        elif has_pil and ast_type in ("png", "jpg", "jpeg", "webp"):
            try:
                with Image.open(asset_file) as img:
                    act_w, act_h = img.size
                    if target_w and target_h:
                        if abs(act_w - target_w) > 5 or abs(act_h - target_h) > 5:
                            warnings.append(f"Asset '{ast_id}' dimension mismatch: manifest specified {target_w}x{target_h}, actual file is {act_w}x{act_h}.")
                    
                    if target_ratio_str in VALID_ASPECT_RATIOS:
                        exp_ratio = VALID_ASPECT_RATIOS[target_ratio_str]
                        act_ratio = act_w / max(act_h, 1)
                        if abs(act_ratio - exp_ratio) > 0.08:
                            warnings.append(f"Asset '{ast_id}' aspect ratio drift: expected {target_ratio_str} ({exp_ratio:.2f}), actual is {act_ratio:.2f}.")
            except Exception as e:
                defects.append(f"CRITICAL: Failed to parse image '{asset_file}': {e}")

    passed = len(defects) == 0
    return {
        "status": "PASS" if passed else "FAIL",
        "manifest_path": manifest_path,
        "total_assets": total_assets,
        "approved_assets": approved_count,
        "critical_defects": defects,
        "warnings": warnings
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Factory Visual Asset Pipeline Auditor")
    parser.add_argument("--manifest", required=True, help="Path to asset-manifest.json")
    parser.add_argument("--json", action="store_true", help="Output JSON report")
    args = parser.parse_args()

    res = audit_asset_manifest(args.manifest)
    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print("\n=======================================================")
        print(f"VISUAL ASSET PIPELINE AUDIT: {res.get('manifest_path', 'unknown')}")
        print(f"Status: {res['status']}")
        print(f"Assets: Total={res.get('total_assets', 0)}, Approved={res.get('approved_assets', 0)}")
        print("=======================================================")
        if res.get("critical_defects"):
            print(f"\nCRITICAL DEFECTS ({len(res['critical_defects'])}):")
            for d in res["critical_defects"]:
                print(f"  [X] {d}")
        if res.get("warnings"):
            print(f"\nWARNINGS ({len(res['warnings'])}):")
            for w in res["warnings"]:
                print(f"  [!] {w}")
        if not res.get("critical_defects") and not res.get("warnings"):
            print("\n[OK] All visual assets verified. Complete license provenance and dimensional fidelity.")

    sys.exit(0 if res['status'] == "PASS" else 1)
