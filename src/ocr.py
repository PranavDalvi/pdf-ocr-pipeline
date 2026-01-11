from typing import List

import pytesseract
from PIL.Image import Image


class OCRProcessor:
    def __init__(self, lang: str = "eng"):
        self.lang = lang

    def extract_text(self, images: List[Image]) -> List[str]:
        """
        Extract text from a list of images using OCR.

        Args:
            images (List[Image]): List of page images

        Returns:
            List[str]: Extracted text per page
        """

        text_block = []

        for img in images:
            text = pytesseract.image_to_string(img, lang=self.lang)
            text_block.append(text)
        return text_block


# Internal testing
# from pdf_converter import PDFToImages
# if __name__ == "__main__":
#     images = PDFToImages().convert("HR_Email_List.pdf")
#     texts = OCRProcessor().extract_text(images)

#     print(texts[0][:500])
