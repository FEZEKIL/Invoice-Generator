import pandas as pd
import glob

filepath = glob.glob("invoices/*.xlsx")

for filepath in filepath:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

