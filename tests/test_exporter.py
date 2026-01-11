import pandas as pd
from src.exporter import ExcelExporter

def test_excel_export(tmp_path):
    df = pd.DataFrame({
        "Company": ["Kpmg", "EY"],
        "Email": ["a@kpmg.com", "b@ey.com"]
    })

    output_file = tmp_path / "output.xlsx"
    exporter = ExcelExporter()
    exporter.export(df, output_file)

    assert output_file.exists()
