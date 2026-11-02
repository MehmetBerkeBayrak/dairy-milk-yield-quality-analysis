# Reproduce the analysis

From the project root:
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/analyze.py
```
The script rebuilds CSVs, SVG figures and validation results without changing the raw workbook. Validated dependency versions are in requirements-validated.txt.

PostgreSQL: create an empty database, run sql/00_tablo_yapisi.sql, then import data/processed/sut_verisi.csv using client-side psql (not pgAdmin's Query Tool):
```text
\copy public.sut_ham FROM 'PROJECT_PATH/data/processed/sut_verisi.csv' WITH (FORMAT CSV, HEADER TRUE, ENCODING 'UTF8');
```
Run 01_analiz_gorunumleri.sql, then 02–08. Do not import twice into an already populated raw table. Expected row counts: raw 750, animal-condition 150, group-condition 15, paired animals 50.

Power BI: the design copy retains only the animal-change model. Desktop opening/rendering has not been tested and the file is a draft. Load the supplied group summary/composition CSVs for the wider report. CSVs use UTF-8, comma delimiter and dot decimals; use English (United States) locale for numeric conversion. Percentage values are already on the 0–100 scale. Keep IDs as text. Repoint any existing personal CSV source path before refresh. See powerbi/REPORT_GUIDE_TR_EN.md.
