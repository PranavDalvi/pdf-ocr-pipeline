import argparse
from src.pipeline import PDFToExcelPipeline

def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert PDF to Excel using OCR"
    )

    parser.add_argument(
        "pdf_path",
        help="Path to input PDF file"
    )

    parser.add_argument(
            "output_path",
            help="Path to output Excel file (.xlsx)"
        )

    return parser.parse_args()

def main():
    args = parse_args()

    pipeline = PDFToExcelPipeline()
    pipeline.run(args.pdf_path, args.output_path)

    print("PDF successfully converted to Excel.")

if __name__ == "__main__":
    main()
