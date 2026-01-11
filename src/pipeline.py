from src.exporter import ExcelExporter
from src.extractor import DataExtractor
from src.ocr import OCRProcessor
from src.pdf_converter import PDFToImages
from src.text_extractor import TextExtractor


class PDFToExcelPipeline:
    TEXT_THRESHOLD = 500

    def __init__(self):
        self.pdf_converter = PDFToImages()
        self.ocr = OCRProcessor()
        self.extractor = DataExtractor()
        self.text_extractor = TextExtractor()
        self.exporter = ExcelExporter()

    def run(self, pdf_path: str, output_path: str) -> None:
        # Try text-based extraction
        text_blocks = self.text_extractor.extract_text(pdf_path)
        total_text_length = sum(len(t) for t in text_blocks)
        # Decide To use OCR or not
        if total_text_length < self.TEXT_THRESHOLD:
            images = self.pdf_converter.convert(pdf_path)
            text_blocks = self.ocr.extract_text(images)
        # Parse + export
        df = self.extractor.to_dataframe(text_blocks)
        self.exporter.export(df, output_path)


# Internal Testing
# if __name__ == "__main__":
#     pipeline = PDFToExcelPipeline()
#     pipeline.run("HR_Email_List.pdf", "emails.xlsx")
