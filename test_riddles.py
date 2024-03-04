from riddle_solvers import *
from riddles.cv.medium.ssim_test import *
import numpy as np
import pandas as pd
import cv2
from riddle_solvers import solve_sec_medium
from PIL import Image
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from math import sqrt
import requests
import unittest
import time

class TestCVFunctions(unittest.TestCase):
    def test_solve_cv_easy(self):
        image_path = "./riddles/cv/easy/shredded.jpg"
        img = cv2.imread(image_path)
        st = time.time()
        res = solve_cv_easy((img,64))
        ed = time.time()
        print(f"test_solve_cv_easy time: {ed-st}")
        self.assertEqual(res,[0, 11, 7, 1, 8, 9, 3, 5, 6, 4, 10, 2])

    def test_solve_cv_medium(self):
        rgb_template = cv2.imread("./riddles/cv/medium/patch.png")
        rgb_target = cv2.imread("./riddles/cv/medium/large.png")
        real_image = cv2.imread("./riddles/cv/medium/real.png")

        input_data = (list(rgb_target), list(rgb_template))

        st = time.time()
        res = solve_cv_medium(input_data)
        ed = time.time()
        print(f"test_solve_cv_medium time: {ed-st}")

        res_np = np.array(res, dtype=np.uint8)
        self.assertIsInstance(res, list)  # Check if res is a list
        self.assertEqual(res_np.ndim, 3)  # Check if res is a 3D array
        self.assertEqual(res_np.shape, rgb_target.shape)
        self.assertGreaterEqual(matching_degree(res_np, real_image), 0.85)

        # Plotting the result (uncomment if needed)
        # fig, axs = plt.subplots(1, 1)
        # axs.imshow(cv2.cvtColor(res_np, cv2.COLOR_RGB2BGR))
        # axs.set_title("Result Image")
        # axs.axis("off")
        # plt.show()


class TestMLFunctions(unittest.TestCase):

    def test_solve_ml_easy(self):
        input_data = pd.read_csv("riddles/ml/series_data.csv")

        st = time.time()
        res = solve_ml_easy(input_data)
        ed = time.time()
        print(f"test_solve_ml_easy time: {ed-st}")

        self.assertIsInstance(res, list)  # Check if res is a list
        self.assertEqual(len(res), 50)  # Check if the length of the list is 30

        # Calculate RMSE
        with open("riddles/ml/result.txt", "r") as file:
            content = file.read()
            # Extract values from the content string
            actual = [
                float(value)
                for value in content.replace("[", "").replace("]", "").split(",")
            ]

        MSE = np.square(np.subtract(actual, res)).mean()
        rmse = sqrt(MSE)
        self.assertLessEqual(rmse, 35)  # Check if RMSE is less than or equal to 35

    def test_solve_ml_medium(self):
        input_data = [0, 0]

        st = time.time()
        res = solve_ml_medium(input_data)
        ed = time.time()
        print(f"test_solve_ml_medium time: {ed-st}")

        self.assertIsInstance(res, int)  # Check if res is an integer
        self.assertIn(res, [0, -1])  # Check if res is either 0 or -1
        self.assertEqual(res, 0)


class TestSecurityFunctions(unittest.TestCase):

    def test_solve_sec_medium(self):
        image_path = "SteganoGAN/sample_example/encoded.png"
        image = Image.open(image_path)
        preprocess = transforms.Compose([
            transforms.ToTensor(),
        ])
        image_tensor = preprocess(image)
        image_tensor = image_tensor.unsqueeze(0).tolist()

        st = time.time()
        res = solve_sec_medium(image_tensor)
        ed = time.time()
        print(f"test_solve_sec_medium time: {ed-st}")

        self.assertIsInstance(res, str)  # Adjust based on the expected type
        self.assertEqual(res, "Beyond The Obvious.")

    def test_solve_sec_hard(self):
        input_data = ("266200199BBCDFF1", "0123456789ABCDEF")

        st = time.time()
        res = solve_sec_hard(input_data)
        ed = time.time()
        print(f"test_solve_sec_hard time: {ed-st}")

        self.assertIsInstance(res, str)  # Check if res is a string
        self.assertEqual(res, "4E0E6864B5E1CA52")


class TestProblemSolvingFunctions(unittest.TestCase):

    def test_solve_problem_solving_easy(self):
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
        input_data = (q, x)

        st = time.time()
        res = solve_problem_solving_easy(input_data)
        ed = time.time()
        print(f"test_solve_ps_easy time: {ed-st}")

        self.assertIsInstance(res, list)  # Check if res is a list
        self.assertEqual(res, ["pharaoh", "sphinx", "nile"])

    def test_solve_problem_solving_medium(self):
        input_data = "3[d1[e2[l]]]"

        st = time.time()
        res = solve_problem_solving_medium(input_data)
        ed = time.time()
        print(f"test_solve_ps_medium time: {ed-st}")

        self.assertIsInstance(res, str)  # Check if res is a string
        self.assertEqual(res, "delldelldell")

    def test_solve_problem_solving_hard(self):
        m = 3
        n = 2
        input_data = (m, n)

        st = time.time()
        res = solve_problem_solving_hard(input_data)
        ed = time.time()
        print(f"test_solve_ps_hard time: {ed-st}")

        self.assertIsInstance(res, int)  # Check if res is an integer
        self.assertEqual(res, 3)


if __name__ == "__main__":
    unittest.main()
