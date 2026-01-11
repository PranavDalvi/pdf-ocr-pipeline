from unittest.mock import patch

from PIL import Image


from src.ocr import OCRProcessor


def test_ocr_extract_text():
    fake_image = Image.new("RGB", (100, 100))
    ocr = OCRProcessor()

    with patch("pytesseract.image_to_string", return_value="Hello World"):
        result = ocr.extract_text([fake_image])

        assert result == ["Hello World"]
