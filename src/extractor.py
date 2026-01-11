import re
from typing import List

import pandas as pd


class DataExtractor:
    EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    COMPANY_REGEX = re.compile(r"Company\s+Name\s*[–-]\s*(.+)", re.IGNORECASE)

    def __init__(self, headers=None):
        self.headers = headers or ["Company", "Email"]

    def to_dataframe(self, text_blocks: List[str]) -> pd.DataFrame:
        rows = []
        current_company = ""

        for block in text_blocks:
            for line in block.split("\n"):
                line = line.strip()
                if not line:
                    continue

                company_match = self.COMPANY_REGEX.search(line)
                if company_match:
                    current_company = company_match.group(1).strip()
                    continue

                email_match = self.EMAIL_REGEX.search(line)
                if email_match:
                    rows.append([current_company, email_match.group()])

        df = pd.DataFrame(rows, columns=self.headers)

        return self._validate(df)

    def _validate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Validation rules:
            - Remove duplicate emails
            - keep first occurence
        """
        df = df.drop_duplicates(subset="Email", keep="first")
        df = df.reset_index(drop=True)
        return df
