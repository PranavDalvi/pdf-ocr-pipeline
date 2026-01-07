from typing import List

from pdf2image import convert_from_path
from PIL.Image import Image


class PDFToImages:
    def __init__(self, dpi: int = 300):
        self.dpi = dpi

    def convert(self, pdf_path: str) -> List[Image]:
        """
        Convert PDF pages to images.

        Args:
            pdf_path (str): Path to the PDF file

        Returns:
            List[PIL.Image]: List of page images
        """
        images = convert_from_path(pdf_path, dpi=self.dpi)
        return images


# Internal Testing:
# if __name__ == "__main__":
#     converter = PDFToImages(dpi=300)
#     images = converter.convert("Path of the PDF")

#     print(f"Total pages converted: {len(images)}")
