import pytesseract
from PIL import Image
import os


def perform_ocr(image_path, language='heb'):  # Default to Hebrew; change as needed
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang=language)
    return text


if __name__ == "__main__":
    # Example using Hebrew
    extracted_text = perform_ocr("C:\\Users\\kobis\\OneDrive\\Pictures\\20230813_202253.jpg", 'heb')
    print("OCR Results:")
    print(extracted_text)
