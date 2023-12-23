import cv2
import argparse


class Image:
    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(path)

    def show(self, window_name="Image"):
        cv2.imshow(window_name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def resize(self, width=None, height=None):
        if width is not None and height is not None:
            self.image = cv2.resize(self.image, (width, height))
        elif width is not None:
            ratio = width / self.image.shape[1]
            self.image = cv2.resize(self.image, (width, int(self.image.shape[0] * ratio)))
        elif height is not None:
            ratio = height / self.image.shape[0]
            self.image = cv2.resize(self.image, (int(self.image.shape[1] * ratio), height))

    def to_binary(self, threshold):
        _, self.image = cv2.threshold(self.image, threshold, 255, cv2.THRESH_BINARY)

    def invert(self):
        self.image = cv2.bitwise_not(self.image)


def uploader(image_path):
    # Load the image using OpenCV
    opencv_image = cv2.imread(image_path)

    # Create an Image object and pass the OpenCV image to it
    image = Image(image_path)
    image.image = opencv_image  # Replace the Image's image data with the loaded image

    return image


def parse_arguments():
    parser = argparse.ArgumentParser(description="Image Processing Script")

    image_path = 'C:\\Users\\kobis\\OneDrive\\Pictures\\20230813_202253.jpg'

    parser.add_argument("-i", "--image", type=str, default=image_path, help="Path to the image file")
    parser.add_argument("-t", "--threshold", type=int, default=130, help="Threshold value for binary conversion")

    args = parser.parse_args()

    # Create a dictionary to store the arguments
    arguments = {
        "image_path": args.image,
        "threshold": args.threshold
    }

    return arguments


if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_arguments()

    # Get the image path and threshold from the parsed arguments
    image_path = args["image_path"]
    threshold = args["threshold"]

    # Call the uploader function with the provided image path
    image = uploader(image_path)

    # Example usage of the Image class methods:
    # image.show()
    image.resize(width=500)
    image.to_binary(threshold=threshold)  # Use the threshold from parsed arguments

    # Show the modified image
    image.show()
