import cv2
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

    def to_binary(self, threshold=128):
        """Convert the image to binary using Otsu's thresholding after Gaussian filtering."""
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
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


# Example usage
if __name__ == "__main__":
    img = Image("C:\\Users\\kobis\\OneDrive\\Pictures\\20230813_202253.jpg")
    img.resize(width=500)
    img.denoise()
    img.to_binary()
    img.deskew()
    pil_image = img.convert_to_pil()
    pil_image.show()
