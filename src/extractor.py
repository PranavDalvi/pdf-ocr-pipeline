import re
from typing import List

import pandas as pd


class DataExtractor:
    EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

    def __init__(self, headers=None):
        self.headers = headers or ["Company", "Email"]

    def to_dataframe(self, text_blocks: List[str]) -> pd.DataFrame:
        rows = []

        for block in text_blocks:
            for line in block.split("\n"):
                line = line.strip()
                if not line:
                    continue

                email_match = self.EMAIL_REGEX.search(line)
                if not email_match:
                    continue

                email = email_match.group()
                company = line.replace(email, "").strip()

                rows.append([company, email])

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
