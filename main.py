import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepath = glob.glob("invoices/*.xlsx")

for filepath in filepath:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDF's/{filename}.pdf")
