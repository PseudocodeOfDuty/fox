import cv2
import numpy as np


class inpainter:
    def inpaint_box(self, image, corners):
        # Create a mask for the box region
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        # cv2.fillConvexPoly(mask, corners, 255)
        cv2.fillPoly(mask, [corners.astype(int)], 255)

        # Inpaint the image using the created mask
        inpainted_image = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

        return inpainted_image

    def solve(self, image, corners):
        inpainted_image = self.inpaint_box(image, corners)

        return inpainted_image
