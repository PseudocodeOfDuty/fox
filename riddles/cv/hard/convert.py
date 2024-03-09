import cv2
import json 
import numpy as np

with open("riddles\cv\hard\images\cv_hard_testcase4.json", "r") as f:
    data = json.load(f)
    print(data[0])
    cv2.imwrite("test4.jpg", np.array(data[1], dtype="uint8"))