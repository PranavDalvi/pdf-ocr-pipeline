from src.pdf_converter import PDFToImages
from src.ocr import OCRProcessor
from src.extractor import DataExtractor
from src.exporter import ExcelExporter

class PDFToExcelPipeline:
    def __init__(self):
        self.pdf_converter = PDFToImages()
        self.ocr = OCRProcessor()
        self.extractor = DataExtractor()
        self.exporter = ExcelExporter()

    def run(self, pdf_path: str, output_path: str) -> None:
        images = self.pdf_converter.convert(pdf_path)
        text = self.ocr.extract_text(images)
        df = self.extractor.to_dataframe(text)
        self.exporter.export(df, output_path)

# Internal Testing
# if __name__ == "__main__":
#     pipeline = PDFToExcelPipeline()
#     pipeline.run("HR_Email_List.pdf", "emails.xlsx")
