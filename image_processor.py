import cv2
import consts
import numpy as np
from PIL import Image as PILImage


class Image:
    """Class for handling image processing operations."""
    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(path)

    def resize(self, width=None, height=None):
        """Resize the image to the specified width and height."""
        if width is not None and height is not None:
            self.image = cv2.resize(self.image, (width, height))
        elif width is not None:
            ratio = width / self.image.shape[1]
            self.image = cv2.resize(self.image, (width, int(self.image.shape[0] * ratio)))
        elif height is not None:
            ratio = height / self.image.shape[0]
            self.image = cv2.resize(self.image, (int(self.image.shape[1] * ratio), height))

    def to_binary(self, threshold=200):
        """Convert the image to binary using Otsu's thresholding after Gaussian filtering."""
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (1, 1), 10)
        _, self.image = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    def denoise(self):
        """Apply fast Nl means denoising."""
        self.image = cv2.fastNlMeansDenoisingColored(self.image, None, 10, 10, 7, 21)

    def invert(self):
        """Invert the colors of the image."""
        self.image = cv2.bitwise_not(self.image)

    def deskew(self):
        """Correct alignment of the image."""
        coords = np.column_stack(np.where(self.image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = self.image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        self.image = cv2.warpAffine(self.image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    def convert_to_pil(self):
        """Convert OpenCV image to a PIL image."""
        return PILImage.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))

    def crop_to_receipt(self):
        """Crop the image to the bounding box of the largest contour, which should be the receipt."""
        # Find contours
        contours, _ = cv2.findContours(self.image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Assume the largest contour is the receipt
        largest_contour = max(contours, key=cv2.contourArea)

        # Get bounding box of the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Crop the image to the bounding box
        self.image = self.image[y:y + h, x:x + w]


def processor(path) -> PILImage:

    img = Image(path)
    img.denoise()
    img.to_binary()
    img.crop_to_receipt()
    pil_image = img.convert_to_pil()
    return img.image, pil_image


# Example usage
if __name__ == "__main__":
    processor(consts.ExampleImage)
