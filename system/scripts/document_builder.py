"""
AI PRODUCT FACTORY — PUBLICATION-GRADE DOCUMENT BUILDER
Modality: Documents, Playbooks, Manuals, Workbooks
Converts Markdown and structured content into semantic, publication-ready HTML/PDF
with executive typography, KPI cards, tables, callouts, and print pagination.
"""

import os
import sys
import re
import argparse
import subprocess
import shutil

def markdown_to_semantic_html(md_text):
    """Parses standard markdown syntax into semantic HTML elements."""
    lines = md_text.splitlines()
    html_lines = []
    in_code_block = False
    code_buffer = []
    code_lang = ""
    in_list = False
    list_type = "ul"
    in_table = False
    table_headers = []
    table_rows = []

    def close_list():
        nonlocal in_list, list_type
        if in_list:
            html_lines.append(f"</{list_type}>")
            in_list = False

    def close_table():
        nonlocal in_table, table_headers, table_rows
        if in_table:
            html_lines.append("<table>")
            if table_headers:
                html_lines.append("<thead><tr>")
                for th in table_headers:
                    html_lines.append(f"<th>{th.strip()}</th>")
                html_lines.append("</tr></thead>")
            html_lines.append("<tbody>")
            for row in table_rows:
                html_lines.append("<tr>")
                for cell in row:
                    html_lines.append(f"<td>{cell.strip()}</td>")
                html_lines.append("</tr>")
            html_lines.append("</tbody></table>")
            in_table = False
            table_headers = []
            table_rows = []

    for line in lines:
        stripped = line.strip()

        # 1. Code Block Fence
        if stripped.startswith("```"):
            close_list()
            close_table()
            if in_code_block:
                escaped = "\n".join(code_buffer).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                html_lines.append(f"<pre><code>{escaped}</code></pre>")
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
                code_lang = stripped[3:].strip()
            continue

        if in_code_block:
            code_buffer.append(line)
            continue

        # Blank line closes lists and tables
        if not stripped:
            close_list()
            close_table()
            continue

        # 2. Tables (| cell | cell |)
        if stripped.startswith("|") and stripped.endswith("|"):
            close_list()
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(re.match(r"^:?-+:?$", c) for c in cells):
                # Header separator line, ignore
                continue
            if not in_table:
                in_table = True
                table_headers = cells
            else:
                table_rows.append(cells)
            continue
        else:
            close_table()

        # 3. Headings
        if stripped.startswith("### "):
            close_list()
            html_lines.append(f"<h3>{format_inline(stripped[4:])}</h3>")
            continue
        if stripped.startswith("## "):
            close_list()
            html_lines.append(f"<h2>{format_inline(stripped[3:])}</h2>")
            continue
        if stripped.startswith("# "):
            close_list()
            html_lines.append(f"<h1>{format_inline(stripped[2:])}</h1>")
            continue

        # 4. Blockquotes / Callout Cards
        if stripped.startswith("> "):
            close_list()
            quote_text = stripped[2:].strip()
            badge = "Key Principle"
            if quote_text.startswith("**WARNING:**") or quote_text.startswith("WARNING:"):
                html_lines.append(f'<div class="callout warning"><div class="callout-title">Operational Warning</div><p>{format_inline(quote_text)}</p></div>')
            elif quote_text.startswith("**NOTE:**") or quote_text.startswith("NOTE:"):
                html_lines.append(f'<div class="callout info"><div class="callout-title">Strategic Note</div><p>{format_inline(quote_text)}</p></div>')
            else:
                html_lines.append(f'<div class="callout info"><div class="callout-title">{badge}</div><p>{format_inline(quote_text)}</p></div>')
            continue

        # 5. Lists
        if stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list or list_type != "ul":
                close_list()
                in_list = True
                list_type = "ul"
                html_lines.append("<ul>")
            html_lines.append(f"<li>{format_inline(stripped[2:])}</li>")
            continue

        numbered_match = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if numbered_match:
            if not in_list or list_type != "ol":
                close_list()
                in_list = True
                list_type = "ol"
                html_lines.append("<ol>")
            html_lines.append(f"<li>{format_inline(numbered_match.group(2))}</li>")
            continue

        close_list()

        # 6. Horizontal Rule
        if stripped in ("---", "***", "___"):
            html_lines.append("<hr style='border: none; border-top: 1px solid var(--color-border); margin: 32px 0;'>")
            continue

        # 7. Standard Paragraph
        html_lines.append(f"<p>{format_inline(stripped)}</p>")

    close_list()
    close_table()
    return "\n".join(html_lines)

def format_inline(text):
    """Formats bold, italic, code, and links in a string."""
    # Escape basic HTML first
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Inline code: `code`
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # Bold: **bold** or __bold__
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", text)
    # Italic: *italic* or _italic_
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"_([^_]+)_", r"<em>\1</em>", text)
    # Links: [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    return text

def build_document(title, markdown_path, output_path, generate_pdf=False, subtitle="Executive Product Playbook"):
    if not os.path.exists(markdown_path):
        print(f"[DOCUMENT BUILDER ERROR] Input markdown not found: {markdown_path}")
        return False

    with open(markdown_path, "r", encoding="utf-8") as f:
        raw_md = f.read()

    body_html = markdown_to_semantic_html(raw_md)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    :root {{
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      --color-primary: #0f172a;
      --color-accent: #2563eb;
      --color-accent-subtle: #eff6ff;
      --color-text-main: #1e293b;
      --color-text-muted: #64748b;
      --color-border: #e2e8f0;
      --color-bg-canvas: #f8fafc;
      --color-bg-card: #ffffff;
      --radius-md: 8px;
    }}
    @page {{
      size: A4 portrait;
      margin: 20mm 15mm;
      @top-left {{ content: "{title}"; font-size: 8pt; color: #64748b; font-family: var(--font-sans); }}
      @bottom-right {{ content: "Page " counter(page) " of " counter(pages); font-size: 8pt; color: #64748b; font-family: var(--font-sans); }}
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: var(--font-sans);
      color: var(--color-text-main);
      background-color: var(--color-bg-canvas);
      line-height: 1.65;
      font-size: 11pt;
      padding: 40px 20px;
    }}
    .doc-wrapper {{
      max-width: 860px;
      margin: 0 auto;
      background: var(--color-bg-card);
      padding: 56px 64px;
      border-radius: var(--radius-md);
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
      border: 1px solid var(--color-border);
    }}
    .doc-header {{
      border-bottom: 2px solid var(--color-border);
      padding-bottom: 28px;
      margin-bottom: 36px;
    }}
    .badge {{
      display: inline-block;
      font-size: 8.5pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--color-accent);
      background: var(--color-accent-subtle);
      padding: 4px 10px;
      border-radius: 4px;
      margin-bottom: 12px;
    }}
    h1 {{ font-size: 26pt; font-weight: 800; color: var(--color-primary); line-height: 1.2; margin-bottom: 10px; }}
    .subtitle {{ font-size: 12.5pt; color: var(--color-text-muted); margin-bottom: 18px; }}
    h2 {{ font-size: 16pt; font-weight: 700; color: var(--color-primary); margin-top: 36px; margin-bottom: 14px; border-bottom: 1px solid var(--color-border); padding-bottom: 6px; break-after: avoid; }}
    h3 {{ font-size: 12.5pt; font-weight: 600; color: #334155; margin-top: 24px; margin-bottom: 8px; break-after: avoid; }}
    p {{ margin-bottom: 14px; }}
    ul, ol {{ margin: 12px 0 16px 24px; }}
    li {{ margin-bottom: 6px; }}
    pre {{
      background: #0f172a;
      color: #f8fafc;
      padding: 16px;
      border-radius: 6px;
      overflow-x: auto;
      font-family: var(--font-mono);
      font-size: 9.5pt;
      margin: 18px 0;
      break-inside: avoid;
    }}
    code {{ font-family: var(--font-mono); font-size: 9.5pt; background: #f1f5f9; padding: 2px 5px; border-radius: 3px; color: #0f172a; }}
    pre code {{ background: transparent; padding: 0; color: inherit; }}
    .callout {{
      background: var(--color-accent-subtle);
      border-left: 4px solid var(--color-accent);
      padding: 16px 20px;
      border-radius: 6px;
      margin: 22px 0;
      break-inside: avoid;
    }}
    .callout.warning {{
      background: #fffbeb;
      border-color: #d97706;
      color: #92400e;
    }}
    .callout-title {{ font-weight: 700; font-size: 10pt; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.05em; }}
    table {{ width: 100%; border-collapse: collapse; margin: 24px 0; font-size: 9.5pt; break-inside: avoid; }}
    th, td {{ border: 1px solid var(--color-border); padding: 10px 14px; text-align: left; }}
    th {{ background: #f8fafc; color: var(--color-primary); font-weight: 700; }}
    tr:nth-child(even) td {{ background-color: #fafbfc; }}
    @media print {{
      body {{ background: #ffffff; padding: 0; }}
      .doc-wrapper {{ box-shadow: none; border: none; padding: 0; max-width: 100%; }}
    }}
  </style>
</head>
<body>
  <div class="doc-wrapper">
    <header class="doc-header">
      <span class="badge">Official Product Deliverable</span>
      <h1>{title}</h1>
      <p class="subtitle">{subtitle}</p>
    </header>
    <main>
      {body_html}
    </main>
    <footer style="margin-top: 48px; padding-top: 20px; border-top: 1px solid var(--color-border); font-size: 8.5pt; color: var(--color-text-muted);">
      <div>AI Product Factory &bull; Publication-Grade Document &bull; Verified Provenance Standards</div>
    </footer>
  </div>
</body>
</html>"""

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"[DOCUMENT BUILDER] Successfully assembled publication-grade HTML: {output_path}")

    # Optional PDF compilation
    if generate_pdf:
        pdf_path = os.path.splitext(output_path)[0] + ".pdf"
        # Check for headless Edge/Chrome on Windows
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        browser_bin = edge_path if os.path.exists(edge_path) else (chrome_path if os.path.exists(chrome_path) else None)

        if browser_bin:
            try:
                cmd = f'"{browser_bin}" --headless --disable-gpu --print-to-pdf="{pdf_path}" "{os.path.abspath(output_path)}"'
                res = subprocess.run(cmd, shell=True, capture_output=True)
                if res.returncode == 0 and os.path.exists(pdf_path):
                    print(f"[DOCUMENT BUILDER] Compiled print-ready PDF via headless browser: {pdf_path}")
            except Exception as e:
                print(f"[DOCUMENT BUILDER WARNING] Headless PDF compilation failed: {e}")

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Factory Document Builder")
    parser.add_argument("--title", required=True, help="Title of document")
    parser.add_argument("--input", required=True, help="Path to input Markdown file")
    parser.add_argument("--output", required=True, help="Path to output HTML file")
    parser.add_argument("--subtitle", default="Executive Product Deliverable", help="Subtitle")
    parser.add_argument("--pdf", action="store_true", help="Compile to PDF as well")
    args = parser.parse_args()

    build_document(args.title, args.input, args.output, generate_pdf=args.pdf, subtitle=args.subtitle)
