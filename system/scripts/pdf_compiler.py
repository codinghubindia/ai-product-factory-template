"""
AI PRODUCT FACTORY — PUBLICATION-GRADE PDF COMPILER
Multi-Stage Deliberate Layout, ReportLab & Headless Browser Support, Bookmarking & Metadata Injection
"""

import os
import sys
import re
import argparse
import subprocess
from html.parser import HTMLParser

# Ensure system/vendor is available for local libraries
vendor_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "vendor"))
if os.path.exists(vendor_dir) and vendor_dir not in sys.path:
    sys.path.insert(0, vendor_dir)

class SimpleHTMLDocParser(HTMLParser):
    """Extracts semantic flow elements and headings from publication HTML."""
    def __init__(self):
        super().__init__()
        self.elements = []
        self.headings = []
        self._current_tag = None
        self._current_attrs = {}
        self._buffer = []
        self._in_table = False
        self._table_data = []
        self._current_row = []

    def handle_starttag(self, tag, attrs):
        self._current_tag = tag.lower()
        self._current_attrs = dict(attrs)
        if self._current_tag == 'table':
            self._in_table = True
            self._table_data = []
        elif self._current_tag == 'tr' and self._in_table:
            self._current_row = []
        elif self._current_tag in ('th', 'td') and self._in_table:
            self._buffer = []
        elif self._current_tag in ('h1', 'h2', 'h3', 'p', 'li', 'blockquote', 'div'):
            self._buffer = []

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        text = "".join(self._buffer).strip()
        text = re.sub(r'\s+', ' ', text)

        if tag_lower in ('th', 'td') and self._in_table:
            self._current_row.append(text)
            self._buffer = []
        elif tag_lower == 'tr' and self._in_table:
            if self._current_row:
                self._table_data.append(self._current_row)
                self._current_row = []
        elif tag_lower == 'table' and self._in_table:
            self._in_table = False
            if self._table_data:
                self.elements.append({"type": "table", "data": self._table_data})
            self._table_data = []
        elif tag_lower in ('h1', 'h2', 'h3'):
            if text:
                level = int(tag_lower[1])
                self.elements.append({"type": f"h{level}", "text": text})
                self.headings.append({"level": level, "title": text})
            self._buffer = []
        elif tag_lower == 'p':
            if text:
                is_callout = 'callout' in self._current_attrs.get('class', '')
                self.elements.append({"type": "callout" if is_callout else "p", "text": text})
            self._buffer = []
        elif tag_lower == 'blockquote':
            if text:
                self.elements.append({"type": "pullquote", "text": text})
            self._buffer = []
        self._current_tag = None

    def handle_data(self, data):
        self._buffer.append(data)

def compile_pdf_reportlab(html_content, output_pdf_path, title="Product Deliverable", author="AI Product Factory", subject="Publication"):
    """Compiles publication-grade PDF using ReportLab with custom page geometry and styles."""
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
    from reportlab.pdfgen import canvas

    parser = SimpleHTMLDocParser()
    parser.feed(html_content)

    class NumberedCanvas(canvas.Canvas):
        """Two-pass canvas for total page count, running headers, and running footers."""
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._saved_page_states = []

        def showPage(self):
            self._saved_page_states.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            num_pages = len(self._saved_page_states)
            for state in self._saved_page_states:
                self.__dict__.update(state)
                if self._pageNumber > 1: # Suppress headers on cover
                    self.saveState()
                    self.setFont("Helvetica", 7.5)
                    self.setFillColor(colors.HexColor("#64748b"))
                    # Running Header
                    self.drawString(54, 842 - 36, title.upper())
                    self.drawRightString(595 - 54, 842 - 36, "EXECUTIVE DELIVERABLE")
                    self.setStrokeColor(colors.HexColor("#e2e8f0"))
                    self.setLineWidth(0.5)
                    self.line(54, 842 - 42, 595 - 54, 842 - 42)

                    # Running Footer
                    self.line(54, 45, 595 - 54, 45)
                    self.drawString(54, 32, "CONFIDENTIAL & PROPRIETARY • AI PRODUCT FACTORY")
                    page_str = f"Page {self._pageNumber} of {num_pages}"
                    self.drawRightString(595 - 54, 32, page_str)
                    self.restoreState()
                super().showPage()
            super().save()

    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=A4,
        leftMargin=54, # ~19mm
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='CoverTitle',
        fontName='Helvetica-Bold',
        fontSize=28,
        leading=34,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=15
    ))
    styles.add(ParagraphStyle(
        name='CoverSubtitle',
        fontName='Helvetica',
        fontSize=13,
        leading=18,
        textColor=colors.HexColor("#475569"),
        spaceAfter=30
    ))
    styles.add(ParagraphStyle(
        name='PubH1',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=26,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=22,
        spaceAfter=10,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='PubH2',
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1e293b"),
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='PubBody',
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=10
    ))
    styles.add(ParagraphStyle(
        name='CalloutBox',
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#1e293b"),
        backColor=colors.HexColor("#eff6ff"),
        borderColor=colors.HexColor("#3b82f6"),
        borderWidth=1,
        borderPadding=10,
        spaceBefore=12,
        spaceAfter=14
    ))
    styles.add(ParagraphStyle(
        name='PullQuote',
        fontName='Helvetica-Oblique',
        fontSize=11.5,
        leading=16,
        textColor=colors.HexColor("#0f172a"),
        backColor=colors.HexColor("#f8fafc"),
        borderColor=colors.HexColor("#94a3b8"),
        borderWidth=1,
        borderPadding=12,
        spaceBefore=14,
        spaceAfter=14
    ))

    story = []

    # 1. Front Cover Section
    story.append(Spacer(1, 100))
    story.append(Paragraph("AI PRODUCT FACTORY OFFICIAL PUBLICATION", ParagraphStyle('Badge', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor("#2563eb"), spaceAfter=15)))
    story.append(Paragraph(title, styles['CoverTitle']))
    story.append(Paragraph(subject, styles['CoverSubtitle']))
    story.append(Spacer(1, 180))
    story.append(Paragraph(f"Author: <b>{author}</b>", styles['PubBody']))
    story.append(Paragraph("Autonomous Digital Publishing Division • Production Standards", ParagraphStyle('Sub', fontName='Helvetica', fontSize=8.5, textColor=colors.HexColor("#64748b"))))
    story.append(PageBreak())

    # 2. Body Elements
    for el in parser.elements:
        t = el["type"]
        if t == "h1":
            story.append(Paragraph(el["text"], styles['PubH1']))
        elif t == "h2":
            story.append(Paragraph(el["text"], styles['PubH2']))
        elif t == "p":
            story.append(Paragraph(el["text"], styles['PubBody']))
        elif t == "callout":
            story.append(Paragraph(el["text"], styles['CalloutBox']))
        elif t == "pullquote":
            story.append(Paragraph(f'"{el["text"]}"', styles['PullQuote']))
        elif t == "table":
            table_rows = []
            for r in el["data"]:
                row_cells = [Paragraph(str(c), ParagraphStyle('Cell', fontName='Helvetica', fontSize=8.5, leading=11)) for c in r]
                table_rows.append(row_cells)
            if table_rows:
                t_obj = Table(table_rows, colWidths=[487 / len(table_rows[0])] * len(table_rows[0]))
                t_obj.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#0f172a")),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                    ('TOPPADDING', (0, 0), (-1, -1), 6),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
                ]))
                story.append(Spacer(1, 8))
                story.append(t_obj)
                story.append(Spacer(1, 12))

    doc.build(story, canvasmaker=NumberedCanvas)
    return parser.headings

def compile_pdf(html_path, output_pdf_path, title=None, author="AI Product Factory", subject="Executive Product Deliverable"):
    """
    Compiles publication-grade PDF using native ReportLab engine,
    then injects pikepdf metadata and document bookmarks.
    """
    html_abs = os.path.abspath(html_path)
    pdf_abs = os.path.abspath(output_pdf_path)
    os.makedirs(os.path.dirname(pdf_abs), exist_ok=True)

    with open(html_abs, "r", encoding="utf-8") as f:
        html_content = f.read()

    if not title:
        title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else "Official Product Deliverable"

    print(f"[PDF COMPILER] Building publication PDF via ReportLab Engine: {pdf_abs}")
    headings = compile_pdf_reportlab(html_content, pdf_abs, title=title, author=author, subject=subject)

    # Inject metadata & bookmarks using pikepdf
    try:
        import pikepdf
        pdf = pikepdf.open(pdf_abs, allow_overwriting_input=True)
        with pdf.open_metadata() as meta:
            meta['dc:title'] = title
            meta['dc:creator'] = [author]
            meta['dc:description'] = subject
            meta['pdf:Producer'] = "AI Product Factory Publication Engine v2.0"

        with pdf.open_outline() as outline:
            current_h1 = None
            for h in headings:
                dest = pikepdf.Array([pdf.pages[0].obj, pikepdf.Name.Fit])
                item = pikepdf.OutlineItem(h["title"], dest)
                if h["level"] == 1:
                    outline.root.append(item)
                    current_h1 = item
                elif h["level"] == 2 and current_h1:
                    current_h1.children.append(item)
                else:
                    outline.root.append(item)

        pdf.save(pdf_abs)
        print(f"[PDF COMPILER] Metadata & {len(headings)} outline bookmarks injected.")
    except Exception as e:
        print(f"[PDF COMPILER NOTE] Pikepdf post-processing note: {e}")

    # Inspect results
    import pypdf
    reader = pypdf.PdfReader(pdf_abs)
    num_pages = len(reader.pages)
    file_size_kb = os.path.getsize(pdf_abs) / 1024
    print(f"[PDF COMPILER SUCCESS] Generated: {pdf_abs} | Pages: {num_pages} | Size: {file_size_kb:.1f} KB")

    return {
        "pdf_path": pdf_abs,
        "pages": num_pages,
        "size_kb": file_size_kb,
        "headings_count": len(headings)
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Product Factory Publication PDF Compiler")
    parser.add_argument("--html", required=True, help="Input HTML file")
    parser.add_argument("--output", required=True, help="Output PDF file")
    parser.add_argument("--title", default=None, help="Document title")
    parser.add_argument("--author", default="AI Product Factory", help="Author")
    parser.add_argument("--subject", default="Executive Product Deliverable", help="Subject")
    args = parser.parse_args()

    compile_pdf(args.html, args.output, title=args.title, author=args.author, subject=args.subject)
