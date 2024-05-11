import argparse
import consts
from image_processor import Image
from display_utils import show_image
from ocr_processor import perform_ocr_and_display  # Assuming your OCR function is updated and named correctly

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
    image = Image(args.image)
    if args.width:
        image.resize(width=args.width)
    if args.threshold:
        image.to_binary(threshold=args.threshold)

    # Optionally display the image
    if args.display:
        show_image(image.image)

    # Perform OCR if requested
    if args.ocr:
        ocr_results = perform_ocr_and_display(args.image)  # Assuming you will update this function to just return results if needed
        print("OCR Results:", ocr_results)
        # if args.google_sheet:
        #     update_sheet(ocr_results)

if __name__ == "__main__":
    main()
