import cv2
from fox_submission_solver import *
import time
from riddle_solvers import solve_cv_medium

# carrier_img = cv2.imread("SteganoGAN\sample_example\encoded.png")
# real_msg = "psuedocodeofduty"

# msgs = generate_message_array(real_msg,carrier_img)

# submit_fox_attempt(1)

rgb_template = cv2.imread("./riddles/cv/medium/patch.png")
rgb_target = cv2.imread("./riddles/cv/medium/large.png")
input_data = (list(rgb_target), list(rgb_template))


st = time.time()
solution = solve_cv_medium(input_data)
ed = time.time()
print(f"took {ed-st} sec")
solve_riddle(TEAM_ID,solution)
