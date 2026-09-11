"""
AI PRODUCT FACTORY — FINANCIAL MODEL & WORKBOOK STARTER TEMPLATE
Modality: Spreadsheet / Financial Model / Calculator
Output: .xlsx (or .csv fallback) with frozen panes, formula calculations, and explicit formatting.
"""

import os
import sys

# Ensure local system vendor packages (openpyxl, et_xmlfile) are discoverable
vendor_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "system", "vendor"))
if os.path.exists(vendor_dir) and vendor_dir not in sys.path:
    sys.path.insert(0, vendor_dir)

def build_financial_model(output_path, project_name="SaaS Unit Economics Model"):
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    try:
        import openpyxl
        from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
        from openpyxl.utils import get_column_letter

        wb = openpyxl.Workbook()
        
        # -------------------------------------------------------------
        # 1. TAB: Instructions / Assumptions
        # -------------------------------------------------------------
        ws_info = wb.active
        ws_info.title = "Instructions & Assumptions"
        ws_info.views.sheetView[0].showGridLines = True
        
        ws_info["A1"] = project_name.upper()
        ws_info["A1"].font = Font(size=16, bold=True, color="1E293B")
        ws_info["A2"] = "Authoritative Model & Assumptions Reference"
        ws_info["A2"].font = Font(size=11, italic=True, color="64748B")
        
        assumptions = [
            ("Assumptions & Drivers", "Value", "Unit", "Notes"),
            ("Target Customer ACV", 1200, "USD / year", "Annual Contract Value baseline"),
            ("Monthly Churn Rate", 0.02, "% per month", "Industry standard for SMB SaaS"),
            ("Customer Acquisition Cost (CAC)", 350, "USD", "Blended paid & organic"),
            ("Gross Margin", 0.82, "%", "Hosting & direct software delivery"),
            ("Sales Cycle Length", 14, "Days", "Self-serve + creator-driven inbound"),
        ]
        
        header_fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
        header_font = Font(color="FFFFFF", bold=True, size=11)
        
        for r_idx, row in enumerate(assumptions, start=4):
            for c_idx, val in enumerate(row, start=1):
                cell = ws_info.cell(row=r_idx, column=c_idx, value=val)
                if r_idx == 4:
                    cell.fill = header_fill
                    cell.font = header_font
                else:
                    if c_idx == 2 and isinstance(val, float):
                        cell.number_format = "0.0%"
                    elif c_idx == 2 and isinstance(val, int) and val > 100:
                        cell.number_format = "$#,##0"
        
        ws_info.freeze_panes = "A5"

        # -------------------------------------------------------------
        # 2. TAB: 12-Month Projection Engine
        # -------------------------------------------------------------
        ws_model = wb.create_sheet(title="12-Month Projections")
        ws_model.views.sheetView[0].showGridLines = True
        
        ws_model["A1"] = "12-MONTH REVENUE & UNIT ECONOMICS PROJECTION"
        ws_model["A1"].font = Font(size=14, bold=True, color="0F172A")
        
        months = ["Metric / Month"] + [f"Month {m}" for m in range(1, 13)] + ["Total / Avg"]
        for c_idx, header in enumerate(months, start=1):
            cell = ws_model.cell(row=3, column=c_idx, value=header)
            cell.fill = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
            cell.font = Font(color="FFFFFF", bold=True, size=10)
            cell.alignment = Alignment(horizontal="center" if c_idx > 1 else "left")

        metrics = [
            ("New Customers Acquired", [15 + i*5 for i in range(12)], "count"),
            ("Active Customers (Cumulative)", None, "count_formula"),
            ("Gross Monthly Revenue", None, "rev_formula"),
            ("Direct COGS (18%)", None, "cogs_formula"),
            ("Gross Profit", None, "gp_formula"),
            ("Customer Acquisition Cost", None, "cac_formula"),
            ("Net Operating Contribution", None, "net_formula")
        ]

        row_cursor = 4
        for name, data, metric_type in metrics:
            ws_model.cell(row=row_cursor, column=1, value=name).font = Font(bold=True if "Total" in name or "Net" in name or "Gross Profit" in name else False)
            
            if metric_type == "count":
                for col_idx, val in enumerate(data, start=2):
                    c = ws_model.cell(row=row_cursor, column=col_idx, value=val)
                    c.number_format = "#,##0"
                tot_col = get_column_letter(14)
                ws_model.cell(row=row_cursor, column=14, value=f"=SUM(B{row_cursor}:M{row_cursor})").number_format = "#,##0"
                
            elif metric_type == "count_formula":
                # Month 1 = New customers in month 1
                ws_model.cell(row=row_cursor, column=2, value=f"=B4").number_format = "#,##0"
                for m in range(3, 14):
                    prev_col = get_column_letter(m - 1)
                    curr_col = get_column_letter(m)
                    ws_model.cell(row=row_cursor, column=m, value=f"=ROUND({prev_col}{row_cursor}*0.98 + {curr_col}4, 0)").number_format = "#,##0"
                ws_model.cell(row=row_cursor, column=14, value=f"=AVERAGE(B{row_cursor}:M{row_cursor})").number_format = "#,##0"
                
            elif metric_type == "rev_formula":
                for m in range(2, 14):
                    col = get_column_letter(m)
                    ws_model.cell(row=row_cursor, column=m, value=f"={col}5 * ('Instructions & Assumptions'!$B$5 / 12)").number_format = "$#,##0"
                ws_model.cell(row=row_cursor, column=14, value=f"=SUM(B{row_cursor}:M{row_cursor})").number_format = "$#,##0"
                
            elif metric_type == "cogs_formula":
                for m in range(2, 14):
                    col = get_column_letter(m)
                    ws_model.cell(row=row_cursor, column=m, value=f"={col}6 * 0.18").number_format = "$#,##0"
                ws_model.cell(row=row_cursor, column=14, value=f"=SUM(B{row_cursor}:M{row_cursor})").number_format = "$#,##0"
                
            elif metric_type == "gp_formula":
                for m in range(2, 14):
                    col = get_column_letter(m)
                    ws_model.cell(row=row_cursor, column=m, value=f"={col}6 - {col}7").number_format = "$#,##0"
                    ws_model.cell(row=row_cursor, column=m).font = Font(bold=True)
                ws_model.cell(row=row_cursor, column=14, value=f"=SUM(B{row_cursor}:M{row_cursor})").number_format = "$#,##0"
                ws_model.cell(row=row_cursor, column=14).font = Font(bold=True)
                
            elif metric_type == "cac_formula":
                for m in range(2, 14):
                    col = get_column_letter(m)
                    ws_model.cell(row=row_cursor, column=m, value=f"={col}4 * 'Instructions & Assumptions'!$B$7").number_format = "$#,##0"
                ws_model.cell(row=row_cursor, column=14, value=f"=SUM(B{row_cursor}:M{row_cursor})").number_format = "$#,##0"
                
            elif metric_type == "net_formula":
                top_border = Border(top=Side(style='thin', color='CBD5E1'), bottom=Side(style='double', color='0F172A'))
                for m in range(2, 14):
                    col = get_column_letter(m)
                    c = ws_model.cell(row=row_cursor, column=m, value=f"={col}8 - {col}9")
                    c.number_format = "$#,##0"
                    c.font = Font(bold=True, color="0F172A")
                    c.border = top_border
                tot = ws_model.cell(row=row_cursor, column=14, value=f"=SUM(B{row_cursor}:M{row_cursor})")
                tot.number_format = "$#,##0"
                tot.font = Font(bold=True, color="0F172A")
                tot.border = top_border

            row_cursor += 1

        ws_model.freeze_panes = "B4"

        # Auto-adjust column widths
        for ws in [ws_info, ws_model]:
            for col in ws.columns:
                max_len = 0
                col_letter = get_column_letter(col[0].column)
                for cell in col:
                    if cell.value:
                        max_len = max(max_len, len(str(cell.value)))
                ws.column_dimensions[col_letter].width = max(max_len + 3, 12)

        wb.save(output_path)
        print(f"[SPREADSHEET ENGINE] Successfully generated professional financial model: {output_path}")
        return True

    except ImportError:
        # Fallback to structured CSV format
        csv_path = os.path.splitext(output_path)[0] + ".csv"
        import csv
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["AI Product Factory - Spreadsheet Deliverable"])
            writer.writerow(["Model", project_name])
            writer.writerow([])
            writer.writerow(["Metric", "Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6", "Total"])
            writer.writerow(["New Customers", 15, 20, 25, 30, 35, 40, 165])
            writer.writerow(["MRR ($)", 1500, 3500, 6000, 9000, 12500, 16500, 49000])
            writer.writerow(["Gross Profit ($)", 1230, 2870, 4920, 7380, 10250, 13530, 40180])
            writer.writerow(["Net Contribution ($)", 180, 870, 1920, 3180, 4750, 6530, 17430])
        print(f"[SPREADSHEET ENGINE] openpyxl not installed. Generated structured CSV fallback: {csv_path}")
        return True

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "output_model.xlsx"
    build_financial_model(out)
