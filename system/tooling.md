# AI PRODUCT FACTORY — TOOLING CAPABILITY & RUNTIME REGISTRY

This registry tracks detected host system capabilities, installed runtime versions, package managers, and dynamic installation protocols.

> **CRITICAL FACTORY RULE:** Never fabricate environment capabilities. Only record tools that actually exist on the host machine or are explicitly documented as unavailable. Do not install every conceivable framework upfront; install dependencies dynamically based on approved product requirements.

---

## 1. Detected Host Environment (Verified Live)

| Category | Tool / Binary | Status | Version | Verified Path |
| :--- | :--- | :--- | :--- | :--- |
| **Operating System** | Windows 64-bit | VERIFIED | Windows 10/11 (NT) | `C:\WINDOWS` |
| **Shell** | PowerShell | VERIFIED | WindowsPowerShell v5.1 | `C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.EXE` |
| **Version Control** | Git | VERIFIED | 2.55.0.windows.3 | `C:\Program Files\Git\cmd\git.EXE` |
| **Primary Runtime** | Python | VERIFIED | 3.14.7 | `C:\Users\maxxc\AppData\Local\Programs\Python\Python314\python.EXE` |
| **Web Runtime** | Node.js | VERIFIED | v24.19.0 | `C:\Program Files\nodejs\node.EXE` |
| **Node Package Manager** | npm | VERIFIED | Built-in with Node | `C:\Program Files\nodejs\npm.CMD` |
| **Python PDF Libs** | pypdf, pikepdf, pillow, reportlab | VERIFIED | Built-in & system/vendor | Verified in Python 3.14 |
| **Spreadsheet Libs** | openpyxl, et-xmlfile | VERIFIED | 3.1.5 (system/vendor) | `python -c "import sys; sys.path.insert(0,'system/vendor'); import openpyxl"` |
| **System Utilities** | curl, tar | VERIFIED | Windows NT built-in | Verified on PATH |

---

## 2. Tools & Runtimes Available In Local Vendor (`system/vendor/`)

| Library / Tool | Version | Status | Location | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **openpyxl** | 3.1.5 | VERIFIED | `system/vendor/openpyxl` | Native Excel (.xlsx) generation with formulas & styling |
| **et_xmlfile** | 2.0.0 | VERIFIED | `system/vendor/et_xmlfile` | XML engine for openpyxl |
| **reportlab** | 5.0.1 | VERIFIED | `system/vendor/reportlab` | Publication-grade PDF engine with custom canvases |
| **pillow** | 12.3.0 | VERIFIED | `system/vendor/PIL` | Image inspection, raster validation, and metadata extraction |
| **charset-normalizer**| 3.5.1 | VERIFIED | `system/vendor/charset_normalizer`| Universal charset detection |

---

## 3. Tools Requiring Dynamic Project-Local Installation When Needed

| Tool / Framework | Target Modality | Status | Dynamic Installation Command | Validation Command |
| :--- | :--- | :--- | :--- | :--- |
| **python-docx** | Word documents (.docx) | UNAVAILABLE | `python -m pip install --target system/vendor python-docx` | `python -c "import sys; sys.path.insert(0,'system/vendor'); import docx"` |
| **python-pptx** | Presentations (.pptx) | UNAVAILABLE | `python -m pip install --target system/vendor python-pptx` | `python -c "import sys; sys.path.insert(0,'system/vendor'); import pptx"` |
| **pandoc** | Document format conversions | UNAVAILABLE | `winget install --id JohnMacFarlane.Pandoc -e` | `pandoc --version` |
| **pnpm** | Fast Node package management | UNAVAILABLE | `npm install -g pnpm` | `pnpm --version` |

---

## 3. Dynamic Tooling Installation Protocol

When an approved product reaches the `product_build` or `architecture` stage:
1. **Inspect Host:** The `solution-architect` or `software-builder` runs `python system/scripts/tooling_manager.py --inspect`.
2. **Project-Local First:** Prefer project-local dependencies (e.g. `npm install --save-dev`, local Python virtual environment) over global system modifications.
3. **Record Changes:** Newly installed tools and libraries must be appended to this file under a `Newly Installed In Project` section.
4. **Deterministic Verification:** Every installed tool must immediately execute its validation command. If the validation command fails, halt and report a blocker in `state.json`.
