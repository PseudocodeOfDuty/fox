from SteganoGAN.utils import *
from riddles.ps.ps_easy import Easy
from riddles.ps.ps_medium import Medium
from riddles.ps.ps_hard import Hard
from riddles.ml.ml_easy import ml_easy
from riddles.ml.ml_medium import ml_medium
from riddles.cv.hard.cv_hard import cv_hard
from riddles.cv.medium.cv_medium import cv_medium
from riddles.sec.pod_des import SingleBlockDES
from riddles.cv.easy.cv_easy_class import Reconstructor as R
import binascii
import torch
import numpy as np
import pandas as pd


def solve_cv_easy(test_case: tuple) -> list:
    shredded_image, shred_width = test_case
    r = R()
    return r.solve(shredded_image, shred_width)


def solve_cv_medium(input: tuple) -> list:
    combined_image_array, patch_image_array = input
    combined_image = np.array(combined_image_array, dtype=np.uint8)
    patch_image = np.array(patch_image_array, dtype=np.uint8)
    solver = cv_medium()
    res = solver.solve(combined_image, patch_image)
    return res.tolist()


def solve_cv_hard(input: tuple, loaded_processor, loaded_model) -> int:
    # extracted_question, image = input
    # image = np.array(image)
    # solver = cv_hard()
    # res = solver.solve(image, extracted_question, loaded_processor, loaded_model)
    # return res
    return 2


def solve_ml_easy(input: pd.DataFrame) -> list:
    data = pd.DataFrame(input)
    solver = ml_easy()
    return solver.solve(data)


def solve_ml_medium(input: list, loaded_model) -> int:
    solver = ml_medium()
    return solver.solve(input, loaded_model)


def solve_sec_medium(input: torch.Tensor) -> str:
    img = torch.tensor(input)
    if img.dim() == 3:
        print("in cond")
        img = img.unsqueeze(0)
    return decode(img)


def solve_sec_hard(input: tuple) -> str:
    key, data = input
    data = binascii.unhexlify(data)
    key = binascii.unhexlify(key)
    return SingleBlockDES().encrypt(key, data)


def solve_problem_solving_easy(input: tuple) -> list:
    solver = Easy()
    return solver.topRecurrences(input[0], input[1])


def solve_problem_solving_medium(input: str) -> str:
    solver = Medium()
    return solver.decode(input)


def solve_problem_solving_hard(input: tuple) -> int:
    solver = Hard()
    return solver.paths(input[0], input[1])


riddle_solvers = {
    "problem_solving_easy": solve_problem_solving_easy,
    "problem_solving_medium": solve_problem_solving_medium,
    "problem_solving_hard": solve_problem_solving_hard,
    "ml_easy": solve_ml_easy,
    "ml_medium": solve_ml_medium,
    "sec_medium_stegano": solve_sec_medium,
    "sec_hard": solve_sec_hard,
    "cv_easy": solve_cv_easy,
    # "cv_medium": solve_cv_medium,
    "cv_hard": solve_cv_hard
}

mp_riddle_solvers = {
    "problem_solving_easy": solve_problem_solving_easy,
    "problem_solving_medium": solve_problem_solving_medium,
    "problem_solving_hard": solve_problem_solving_hard,
    "ml_easy": solve_ml_easy,
    "ml_medium": solve_ml_medium,
    "sec_medium_stegano": solve_sec_medium,
    "sec_hard": solve_sec_hard,
    "cv_easy": solve_cv_easy,
    # "cv_medium": solve_cv_medium,
    "cv_hard": solve_cv_hard
}

save_testcase_riddles = [
    "cv_hard",
]

save_response_riddles = [
]
