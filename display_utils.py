import cv2


def show_image(image, window_name="Image", dimensions=None, threshold=None):
    """Display the image with optional text overlays for dimensions and threshold."""
    display_image = image.copy()
    if dimensions:
        cv2.putText(display_image, dimensions, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    if threshold is not None:
        cv2.putText(display_image, f"Binary threshold: {threshold}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow(window_name, display_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()