from src.extractor import DataExtractor
import pandas as pd


def test_text_to_dataframe():
    text_blocks = [
        "Kpmg hr@kpmg.com\nEY hr@kpmg.com\nEY hr@ey.com\nInvalid line"
    ]

    extractor = DataExtractor()
    df = extractor.to_dataframe(text_blocks)

    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["Company", "Email"]
    assert len(df) == 2
    assert df.iloc[0]["Company"] == "Kpmg"
    assert "hr@kpmg.com" in df["Email"].values
