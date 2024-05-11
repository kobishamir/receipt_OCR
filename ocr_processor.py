import pytesseract
import consts
from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFilter
import matplotlib.pyplot as plt


def perform_ocr_and_display(image_path, language='heb'):
    try:
        # Open image and copy for preprocessing display
        img = Image.open(image_path)
        img = img.rotate(270, expand=True)  # Rotate 90 degrees clockwise (270 degrees in PIL)
        preprocessed_img = img.copy()

        # Preprocessing
        preprocessed_img = preprocessed_img.convert('L')  # Convert to grayscale
        preprocessed_img = ImageOps.autocontrast(preprocessed_img)  # Automatically adjust image contrast
        preprocessed_img = preprocessed_img.resize([2 * s for s in preprocessed_img.size],
                                                   Image.LANCZOS)  # Scale up the image
        preprocessed_img = preprocessed_img.filter(
            ImageFilter.MedianFilter())  # Apply a median filter for noise reduction

        # Perform OCR
        text = pytesseract.image_to_string(preprocessed_img, lang=language)

        # Display the preprocessed image
        plt.figure(figsize=(12, 8))
        plt.subplot(1, 2, 1)
        plt.imshow(preprocessed_img, cmap='gray')
        plt.title('Pre-processed Image')
        plt.axis('off')

        # Draw rectangles and display the annotated image
        draw = ImageDraw.Draw(img)
        boxes = pytesseract.image_to_boxes(preprocessed_img, lang=language)
        for box in boxes.splitlines():
            b = box.split()
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            y = preprocessed_img.height - y
            h = preprocessed_img.height - h
            draw.rectangle(((x, h), (w, y)), outline="red")

        # Print OCR results
        print("OCR Results:")
        print(text)

        plt.subplot(1, 2, 2)
        plt.imshow(img, cmap='gray')
        plt.title('Annotated Image')
        plt.axis('off')
        plt.show()
        return text  # Optionally return text if you want to use it elsewhere

    except Exception as e:
        print(f"Error occurred while processing {image_path}: {e}")
        return ""


if __name__ == "__main__":
    # Example path, can be adjusted to be dynamic as needed
    image_path = consts.ExampleImage
    perform_ocr_and_display(image_path)
