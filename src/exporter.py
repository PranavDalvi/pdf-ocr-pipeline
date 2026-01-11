import pandas as pd


class ExcelExporter:
    def export(self, dataframe: pd.DataFrame, output_path: str) -> None:
        """
        Export DataFrame to an Excel file.

        Args:
            dataframe (pd.DataFrame): Structured data
            output_path (str): Path to output .xlsx file
        """

        dataframe.to_excel(output_path, index=False)
