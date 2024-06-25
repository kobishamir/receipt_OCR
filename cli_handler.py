import argparse
import consts
from image_processor import processor
from ocr_processor import perform_ocr_and_display


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Process images from command line.")
    parser.add_argument("-i", "--image", default=consts.ExampleImage,
                        help="Path to the image file.")
    parser.add_argument("-w", "--width", type=int, help="Width to resize the image.")
    parser.add_argument("-t", "--threshold", type=int, help="Threshold for binary conversion.")
    parser.add_argument("-d", "--display", action='store_true', help="Display the processed image.")
    parser.add_argument("-o", "--ocr", action='store_true', help="Perform OCR on the image.")
    parser.add_argument("-g", "--google_sheet", action='store_true', help="Update Google Sheet with OCR results.")
    return parser.parse_args()


def main():

    args = parse_arguments()

    # Load and process the image
    processed_image_pil_cv2, processed_image_pil = processor(args.image)

    if args.display:
        processed_image_pil.show()

    if args.ocr:
        ocr_results = perform_ocr_and_display(processed_image_pil_cv2, processed_image_pil)
        print("OCR Results:", ocr_results)


if __name__ == "__main__":
    main()
