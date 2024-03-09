from skimage.metrics import structural_similarity as compare_ssim
import cv2


def matching_degree(x, y):
    """
    Calculate the Structural Similarity Index (SSIM) between two grayscale images x and y.
    """
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    y = cv2.cvtColor(y, cv2.COLOR_BGR2GRAY)
    return compare_ssim(x, y)
