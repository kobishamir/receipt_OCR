import pytesseract
import consts
import matplotlib.pyplot as plt
import cv2


def perform_ocr_and_display(image_cv, image_pil, language='heb'):
    try:
        # Perform OCR on the PIL image
        text = pytesseract.image_to_string(image_pil, lang=language)

        # Draw rectangles on the OpenCV image
        boxes = pytesseract.image_to_boxes(image_pil, lang=language)
        for box in boxes.splitlines():
            b = box.split()
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            y = image_cv.shape[0] - y
            h = image_cv.shape[0] - h
            cv2.rectangle(image_cv, (x, h), (w, y), (0, 0, 255), 1)

        # Display the original and annotated images side by side
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))
        plt.title('Annotated Image')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(image_pil, cmap='gray')
        plt.title('Processed Image')
        plt.axis('off')

        plt.show()

        return text

    except Exception as e:
        print(f"Error occurred while processing: {e}")
        return ""


if __name__ == "__main__":
    from image_processor import processor

    _, cv2_image, pil_image = processor(consts.ExampleImage)
    perform_ocr_and_display(cv2_image, pil_image)
