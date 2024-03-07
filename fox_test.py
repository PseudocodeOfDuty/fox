import cv2
from fox_submission_solver import generate_message_array

carrier_img = cv2.imread("./fox_handlers/encoded.png")
real_msg = "psuedocodeofduty"

msgs = generate_message_array(real_msg,carrier_img)
