# import cv2
# from fox_submission_solver import generate_message_array

# carrier_img = cv2.imread("./fox_data/encoded.png")
# real_msg = "psuedocodeofduty"

# msgs = generate_message_array(real_msg,carrier_img)

# for i in range(3):
#     for j in range(3):
#         print(f"P{i}-C{j}: ",end="")
#         msgs[i][j].serialize()

import torch
print(torch.cuda.is_available())