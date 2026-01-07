from PIL.Image import Image

from src.pdf_converter import PDFToImages


def test_pdf_to_images_conversion():
    converter = PDFToImages(dpi=300)
    images = converter.convert("HR_Email_List.pdf")

    assert isinstance(images, list)
    assert len(images) > 0
    assert all(isinstance(img, Image) for img in images)
