from riddle_solvers import *
from riddles.cv.ssim_test import *
import numpy as np
import pandas as pd
import cv2
from riddle_solvers import solve_sec_medium
from PIL import Image
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from math import sqrt
import requests

print("......................testing cv easy..........................")
img = cv2.imread("./riddles/cv/shredded.jpg")
test_case = (img.tolist(), 64)

res = solve_cv_easy(test_case)
print(type(res))  # should be list
print(res)  # should be list of the correct order of the shreds --> acceptance = 100%

print("......................testing cv medium..........................")
rgb_template = cv2.imread("./riddles/cv/patch.png")
rgb_target = cv2.imread("./riddles/cv/large.png")
real_image = cv2.imread("./riddles/cv/real.png")
input = (list(rgb_target), list(rgb_template))

res = solve_cv_medium(input)
print(type(res))  # should be list
print(np.array(res).ndim)
# print("ssim is: ", matching_degree(np.array(res), real_image))
# print(
#     res
# )  # should be list of the representing the real image --> accept = gte(85%) ssim
fig, axs = plt.subplots(1, 1)
payload = {"solution": res}
response = requests.post(
    "http://localhost:5000/eagle/solve-riddle",
    json=payload,
    headers={"content-type": "application/json"},
)


axs.imshow(cv2.cvtColor(np.array(res), cv2.COLOR_RGB2BGR))
axs.set_title("real")
axs.axis("off")

plt.show()
print("......................testing cv hard..........................")
# res = solve_cv_medium(input)
# print(type(res))  # should be int
# print(res)  # should be list of the correct order of the shreds --> acceptance = 100%

print("......................testing ML easy..........................")
input = pd.read_csv("riddles/ml/series_data.csv")

res = solve_ml_easy(input)
print(type(res))  # should be list
print(len(res))  # should be list
print(res)  # should be list of 30 days forecasting --> acceptance <= 35
with open("riddles/ml/result.txt", "r") as file:
    content = file.read()
    # Extract values from the content string
    actual = [
        float(value) for value in content.replace("[", "").replace("]", "").split(",")
    ]

# Calculate RMSE
MSE = np.square(np.subtract(actual, res)).mean()
rmse = sqrt(MSE)
print("Root Mean Squared Error (RMSE):", rmse)

print("......................testing ML medium..........................")
input = [0, 0]
res = solve_ml_medium(input)
print(type(res))  # should be int
print(res)  # should be 0 or -1 --> acceptance = 100%


print("......................testing security medium..........................")

image_path = "SteganoGAN/sample_example/encoded.png"
image = Image.open(image_path)
preprocess = transforms.Compose(
    [
        transforms.ToTensor(),
    ]
)
image_tensor = preprocess(image)
print(type(image_tensor))
result = solve_sec_medium(image_tensor)
print(type(result))
print(result)

print("......................testing security hard..........................")
input = ("266200199BBCDFF1", "0123456789ABCDEF")

res = solve_sec_hard(input)
print(type(res))  # should be string
print(res)  # should be string of the encoded message --> accept = 100%

print("......................testing PS easy..........................")
q = [
    "pharaoh",
    "sphinx",
    "pharaoh",
    "pharaoh",
    "nile",
    "sphinx",
    "pyramid",
    "pharaoh",
    "sphinx",
    "sphinx",
]
x = 3
input = (q, x)

res = solve_problem_solving_easy(input)
print(type(res))  # should be list
print(res)  # should be list of the top x --> accept = 100%

print("......................testing PS medium..........................")
input = "3[d1[e2[l]]]"

res = solve_problem_solving_medium(input)
print(type(res))  # should be a string
print(res)  # should be the decoded string --> accept = 100%

print("......................testing PS hard..........................")
m = 3
n = 2
input = (m, n)

res = solve_problem_solving_hard(input)
print(type(res))  # should be an int
print(res)  # should be no of unique paths --> accept = 100%
