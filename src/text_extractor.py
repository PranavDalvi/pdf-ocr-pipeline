from typing import List

import pdfplumber


class TextExtractor:
    def extract_text(self, pdf_path: str) -> List[str]:
        """
        Extract text directly from PDF without OCR.

        Returns:
            List[str]: text per page
        """
        pages_text = []

        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                pages_text.append(text or "")

        return pages_text
