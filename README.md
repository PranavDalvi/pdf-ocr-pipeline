# PDF OCR Pipeline

An end-to-end Python OCR pipeline that transforms PDF documents into structured Excel files using a modular, testable architecture.

## Features
- PDF → Image conversion
- OCR using Tesseract
- Text parsing and validation
- Deduplication logic
- Excel export
- CLI support
- Unit tests per stage

## Usage
```bash
python main.py input.pdf output.xlsx
```

## Architecture
PDF → Images → OCR → DataFrame → Excel

## Limitations
- OCR accuracy depends on document quality
- Best suited for text-based PDFs

### Class Diagram (High-level)
```bash
+----------------------+
| PDFToExcelPipeline   |
+----------------------+
| - pdf_converter      |
| - ocr                |
| - extractor          |
| - exporter           |
+----------------------+
| + run(pdf, xlsx)     |
+----------------------+
        |
        | uses
        v
+------------------+    +------------------+
| PDFToImages      |    | OCRProcessor     |
+------------------+    +------------------+
| + convert(pdf)   |    | + extract_text() |
+------------------+    +------------------+

+------------------+    +------------------+
| DataExtractor    |    | ExcelExporter    |
+------------------+    +------------------+
| + to_dataframe() |    | + export()       |
+------------------+    +------------------+
```

```bash
pdf_to_excel/
│
├── src/
│   ├── __init__.py
│   ├── pipeline.py          # Orchestrator
│   ├── pdf_converter.py     # PDF → Images
│   ├── ocr.py               # Images → Text
│   ├── extractor.py         # Text → DataFrame
│   ├── exporter.py          # DataFrame → Excel
│
├── tests/
│   ├── test_pdf_converter.py
│   ├── test_ocr.py
│   ├── test_extractor.py
│   ├── test_exporter.py
│
└── main.py              # Entry point
```
## System Dependency:
- Poppler (for PDF rendering)
- Tesseract OCR
``` bash
sudo apt install poppler-utils tesseract-ocr
```

## Design Principles
- Modular, stage-based pipeline
- Single Responsibility Principle
- Clear separation of OCR, parsing, and persistence
- External dependencies mocked in unit tests
