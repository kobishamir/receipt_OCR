import cv2


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

    def to_binary(self, threshold):
        """Convert the image to binary using the specified threshold."""
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, self.image = cv2.threshold(self.image, threshold, 255, cv2.THRESH_BINARY)

    def invert(self):
        """Invert the colors of the image."""
        self.image = cv2.bitwise_not(self.image)



# Commenting out function calls to comply with the instruction of development phase
# img = Image("path_to_image.jpg")
# img.resize(width=500)
# img.to_binary(threshold=130)
# show_image(img.image, dimensions="Width: 500", threshold=130)