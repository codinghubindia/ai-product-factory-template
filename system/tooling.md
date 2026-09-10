# AI PRODUCT FACTORY — TOOLING CAPABILITY & RUNTIME REGISTRY

This registry tracks detected host system capabilities, installed runtime versions, package managers, and dynamic installation protocols.

> **CRITICAL FACTORY RULE:** Never fabricate environment capabilities. Only record tools that actually exist on the host machine or are explicitly documented as unavailable. Do not install every conceivable framework upfront; install dependencies dynamically based on approved product requirements.

---

## 1. Detected Host Environment (Verified Live)

| Category | Tool / Binary | Status | Version | Verified Path |
| :--- | :--- | :--- | :--- | :--- |
| **Operating System** | Windows 64-bit | VERIFIED | Windows 10/11 (NT) | C:\WINDOWS |
| **Shell** | PowerShell | VERIFIED | WindowsPowerShell v1.0 / 5.1 | C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.EXE |
| **Version Control** | Git | VERIFIED | 2.55.0.windows.3 | C:\Program Files\Git\cmd\git.EXE |
| **Primary Runtime** | Python | VERIFIED | 3.14.7 | C:\Users\maxxc\AppData\Local\Programs\Python\Python314\python.EXE |
| **Web Runtime** | Node.js | VERIFIED | v24.19.0 | C:\Program Files\nodejs\node.EXE |
| **Node Package Manager** | npm | VERIFIED | Built-in with Node | C:\Program Files\nodejs\npm.CMD |
| **System Utilities** | curl | VERIFIED | Windows built-in | C:\WINDOWS\system32\curl.EXE |
| **System Utilities** | tar | VERIFIED | Windows built-in | C:\WINDOWS\system32\tar.EXE |

---

## 2. Tools & Runtimes Requiring Dynamic Installation

The following capabilities are currently **NOT INSTALLED** globally. When an approved product requires one of these tools, the factory must follow the dynamic installation protocol documented below:

| Tool / Framework | Target Modality | Status | Dynamic Installation Command | Validation Command |
| :--- | :--- | :--- | :--- | :--- |
| **pandoc** | Documents (Markdown to PDF/DOCX/EPUB) | UNAVAILABLE | winget install --id JohnMacFarlane.Pandoc -e | pandoc --version |
| **weasyprint** | Documents (HTML/CSS to PDF) | UNAVAILABLE | python -m pip install weasyprint | python -m weasyprint --version |
| **libreoffice** | Headless document conversion | UNAVAILABLE | winget install --id TheDocumentFoundation.LibreOffice -e | soffice --version |
| **openpyxl** | Spreadsheet generation (.xlsx) | UNAVAILABLE | python -m pip install openpyxl | python -c  import openpyxl |
| **python-pptx** | Presentation deck generation (.pptx) | UNAVAILABLE | python -m pip install python-pptx | python -c import pptx |
| **python-docx** | Word document generation (.docx) | UNAVAILABLE | python -m pip install python-docx | python -c import docx |
| **reportlab** | Programmatic PDF/vector generation | UNAVAILABLE | python -m pip install reportlab | python -c import reportlab |
| **pnpm / yarn** | Fast Node package management | UNAVAILABLE | 
pm install -g pnpm | pnpm --version |
| **docker** | Containerized builds / local databases | UNAVAILABLE | winget install --id Docker.DockerDesktop -e | docker --version |
| **cargo / rust** | High-performance CLI / Tauri desktop | UNAVAILABLE | winget install --id Rustlang.Rustup -e | cargo --version |

---

## 3. Dynamic Tooling Installation Protocol

When an approved product reaches the product_build or rchitecture stage:
1. **Inspect Host:** The solution-architect or software-builder runs an environment check against this registry.
2. **Project-Local First:** Prefer project-local dependencies (e.g., 
pm install --save-dev, local Python virtual environment env) over global system modifications.
3. **Escalate Global Requirements:** If a tool requires global machine installation (e.g., winget install pandoc), Master notifies the operator before executing.
4. **Record Changes:** Newly installed tools and libraries must be appended to this file under a Newly Installed In Project section.
5. **Deterministic Verification:** Every installed tool must immediately execute its validation command. If the validation command fails, halt and report a blocker in state.json.
