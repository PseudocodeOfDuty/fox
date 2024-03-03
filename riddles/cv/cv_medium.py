import cv2
import numpy as np
import matplotlib.pyplot as plt
from cv.inpainter import *


class cv_medium:

    def solve(self, rgb_target, rgb_template):
        target = cv2.cvtColor(rgb_target, cv2.COLOR_RGB2GRAY)
        template = cv2.cvtColor(rgb_template, cv2.COLOR_RGB2GRAY)

        # Create SIFT detector
        sift = cv2.SIFT_create()

        # Find keypoints and descriptors
        keypoints_template, descriptors_template = sift.detectAndCompute(template, None)
        keypoints_target, descriptors_target = sift.detectAndCompute(target, None)

        # Create a brute force matcher
        bf = cv2.BFMatcher()

        # Match descriptors
        matches = bf.knnMatch(descriptors_template, descriptors_target, k=2)

        # Apply ratio test
        good_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good_matches.append(m)

        # Draw matches
        # matched_img = cv2.drawMatches(
        #     template,
        #     keypoints_template,
        #     target,
        #     keypoints_target,
        #     good_matches,
        #     None,
        #     flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
        # )

        # Extract matched keypoints
        src_pts = np.float32(
            [keypoints_template[m.queryIdx].pt for m in good_matches]
        ).reshape(-1, 1, 2)
        dst_pts = np.float32(
            [keypoints_target[m.trainIdx].pt for m in good_matches]
        ).reshape(-1, 1, 2)

        # Estimate homography
        H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)

        # Warp template image        # warped_template = cv2.warpPerspective(
        #     template, H, (target.shape[1], target.shape[0])
        # )

        h, w = template.shape
        corners = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(
            -1, 1, 2
        )

        # Transform corners
        warped_corners = cv2.perspectiveTransform(corners, H)

        ip = inpainter()
        inpainted = ip.solve(rgb_target, warped_corners)

        return inpainted
