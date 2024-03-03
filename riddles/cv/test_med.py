import cv2
import numpy as np
import matplotlib.pyplot as plt
from cv_medium import cv_medium
import ssim_test
import time

# Load images
rgb_template = cv2.imread("./riddles/cv/patch.png")
rgb_target = cv2.imread("./riddles/cv/large.png")
real_image = cv2.imread("./riddles/cv/real.png")

c = cv_medium()
s = time.time()
inpainted = c.solve(rgb_target, rgb_template)
res = list(inpainted)
e = time.time()
print(e - s)
# print(res)

# Plot results using Matplotlib
print(np.array(res).shape)
# fig, axs = plt.subplots(2, 2)

print(ssim_test.matching_degree(np.array(res), real_image))

# axs[0][0].imshow(img_matches)
# axs[0][0].set_title("Matches")
# axs[0][0].axis("off")

# axs[0][1].imshow(warped_template, cmap="gray")
# axs[0][1].set_title("Warped Template")
# axs[0][1].axis("off")

# axs[1][0].imshow(cv2.cvtColor(inpainted, cv2.COLOR_RGB2BGR))
# axs[1][0].set_title("final result")
# axs[1][0].axis("off")

# axs[1][1].imshow(cv2.cvtColor(real_image, cv2.COLOR_RGB2BGR))
# axs[1][1].set_title("final result")
# axs[1][1].axis("off")

# plt.show()
