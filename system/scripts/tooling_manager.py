"""
AI PRODUCT FACTORY — TOOLING MANAGER & RUNTIME REGISTRY CONTROLLER
Governs tool autonomy, environment inspection, dynamic dependency resolution,
and deterministic installation verification.
"""

import os
import sys
import shutil
import subprocess
import argparse

REGISTRY = {
    "openpyxl": {
        "type": "python",
        "install_cmd": "python -m pip install openpyxl",
        "verify_cmd": 'python -c "import openpyxl; print(openpyxl.__version__)"'
    },
    "python-pptx": {
        "type": "python",
        "install_cmd": "python -m pip install python-pptx",
        "verify_cmd": 'python -c "import pptx; print(pptx.__version__)"'
    },
    "python-docx": {
        "type": "python",
        "install_cmd": "python -m pip install python-docx",
        "verify_cmd": 'python -c "import docx; print(docx.__version__)"'
    },
    "weasyprint": {
        "type": "python",
        "install_cmd": "python -m pip install weasyprint",
        "verify_cmd": "python -m weasyprint --version"
    },
    "pandoc": {
        "type": "system",
        "install_cmd": "winget install --id JohnMacFarlane.Pandoc -e",
        "verify_cmd": "pandoc --version"
    },
    "pnpm": {
        "type": "node",
        "install_cmd": "npm install -g pnpm",
        "verify_cmd": "pnpm --version"
    }
}

def inspect_environment():
    tools = {
        "python": shutil.which("python"),
        "node": shutil.which("node"),
        "npm": shutil.which("npm"),
        "git": shutil.which("git"),
        "pandoc": shutil.which("pandoc"),
        "curl": shutil.which("curl"),
        "tar": shutil.which("tar"),
        "powershell": shutil.which("powershell")
    }

    # Python library checks
    for py_pkg in ["openpyxl", "python-docx", "python-pptx", "pillow", "pypdf", "pikepdf"]:
        mod_name = "PIL" if py_pkg == "pillow" else py_pkg.replace("-", "_")
        try:
            __import__(mod_name)
            tools[f"py:{py_pkg}"] = "INSTALLED (Python Module)"
        except ImportError:
            tools[f"py:{py_pkg}"] = None

    print("[TOOLING AUDIT] Detected Environment Capabilities:")
    for t, path in tools.items():
        status = f"FOUND: {path}" if path else "NOT FOUND / UNAVAILABLE"
        print(f"  - {t:16}: {status}")

    return tools

def check_tool(tool_name):
    tool_lower = tool_name.lower()
    # Check if executable
    which_path = shutil.which(tool_lower)
    if which_path:
        print(f"[TOOL CHECK] '{tool_name}' is available on PATH: {which_path}")
        return True

    # Check if Python module
    py_mod = tool_lower.replace("-", "_")
    try:
        __import__(py_mod)
        print(f"[TOOL CHECK] '{tool_name}' is available as Python package.")
        return True
    except ImportError:
        pass

    print(f"[TOOL CHECK] '{tool_name}' is currently NOT INSTALLED.")
    return False

def install_tool(tool_name):
    tool_lower = tool_name.lower()
    if tool_lower not in REGISTRY:
        print(f"[TOOLING ERROR] '{tool_name}' is not in the recognized factory registry.")
        print(f"Available tools in registry: {list(REGISTRY.keys())}")
        return False

    spec = REGISTRY[tool_lower]
    print(f"[TOOLING INSTALL] Installing '{tool_name}' via: {spec['install_cmd']}")
    res = subprocess.run(spec["install_cmd"], shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[TOOLING INSTALL ERROR] Failed to install {tool_name}:\n{res.stderr}")
        return False

    print(f"[TOOLING INSTALL] Verifying installation with: {spec['verify_cmd']}")
    vres = subprocess.run(spec["verify_cmd"], shell=True, capture_output=True, text=True)
    if vres.returncode == 0:
        print(f"[TOOLING INSTALL SUCCESS] '{tool_name}' verified successfully!\nOutput: {vres.stdout.strip()}")
        return True
    else:
        print(f"[TOOLING INSTALL ERROR] Verification command failed:\n{vres.stderr}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Factory Tooling Manager")
    parser.add_argument("--inspect", action="store_true", help="Inspect all detected tools")
    parser.add_argument("--check", help="Check if a specific tool is installed")
    parser.add_argument("--install", help="Install a registered tool")
    args = parser.parse_args()

    if args.check:
        check_tool(args.check)
    elif args.install:
        install_tool(args.install)
    else:
        inspect_environment()
