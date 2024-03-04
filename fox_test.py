import cv2
from fox_submission_solver import *

carrier_img = cv2.imread("SteganoGAN\sample_example\encoded.png")
real_msg = "psuedocodeofduty"

msgs = generate_message_array(real_msg,carrier_img)

# submit_fox_attempt(1)