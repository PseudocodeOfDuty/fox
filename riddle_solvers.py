from SteganoGAN.utils import *
from riddles.ps.ps_easy import Easy
from riddles.ps.ps_medium import Medium
from riddles.ps.ps_hard import Hard
from riddles.ml.ml_easy import ml_easy
from riddles.cv.cv_medium import cv_medium
from riddles.sec.pod_des import SingleBlockDES
import binascii
import torch
import numpy as np
import pandas as pd


def solve_cv_easy(test_case: tuple) -> list:
    shredded_image, shred_width = test_case
    shredded_image = np.array(shredded_image)
    """
    This function takes a tuple as input and returns a list as output.

    Parameters:
    input (tuple): A tuple containing two elements:
        - A numpy array representing a shredded image.
        - An integer representing the shred width in pixels.

    Returns:
    list: A list of integers representing the order of shreds. When combined in this order, it builds the whole image.
    """
    return []


def solve_cv_medium(input: tuple) -> list:
    combined_image_array, patch_image_array = input
    combined_image = np.array(combined_image_array, dtype=np.uint8)
    patch_image = np.array(patch_image_array, dtype=np.uint8)
    """
    This function takes a tuple as input and returns a list as output.

    Parameters:
    input (tuple): A tuple containing two elements:
        - A numpy array representing the RGB base image.
        - A numpy array representing the RGB patch image.

    Returns:
    list: A list representing the real image.
    """
    solver = cv_medium()
    res = solver.solve(combined_image, patch_image)
    return list(res)


def solve_cv_hard(input: tuple) -> int:
    extracted_question, image = input
    image = np.array(image)
    """
    This function takes a tuple as input and returns an integer as output.

    Parameters:
    input (tuple): A tuple containing two elements:
        - A string representing a question about an image.
        - An RGB image object loaded using the Pillow library.

    Returns:
    int: An integer representing the answer to the question about the image.
    """
    return 0


def solve_ml_easy(input: pd.DataFrame) -> list:
    data = pd.DataFrame(input)

    """
    This function takes a pandas DataFrame as input and returns a list as output.

    Parameters:
    input (pd.DataFrame): A pandas DataFrame representing the input data.

    Returns:
    list: A list of floats representing the output of the function.
    """
    solver = ml_easy()
    return solver.solve(data)


def solve_ml_medium(input: list) -> int:
    """
    This function takes a list as input and returns an integer as output.

    Parameters:
    input (list): A list of signed floats representing the input data.

    Returns:
    int: An integer representing the output of the function.
    """
    return 0


def solve_sec_medium(input: torch.Tensor) -> str:
    img = torch.tensor(input)
    return decode(img)


def solve_sec_hard(input: tuple) -> str:
    key, data = input
    data = binascii.unhexlify(data)
    key = binascii.unhexlify(key)
    return SingleBlockDES().encrypt(key, data)


def solve_problem_solving_easy(input: tuple) -> list:
    """
    This function takes a tuple as input and returns a list as output.

    Parameters:
    input (tuple): A tuple containing two elements:
        - A list of strings representing a question.
        - An integer representing a key.

    Returns:
    list: A list of strings representing the solution to the problem.
    """
    solver = Easy()
    return solver.topRecurrences(input[0], input[1])


def solve_problem_solving_medium(input: str) -> str:
    """
    This function takes a string as input and returns a string as output.

    Parameters:
    input (str): A string representing the input data.

    Returns:
    str: A string representing the solution to the problem.
    """
    solver = Medium()
    return solver.decode(input)


def solve_problem_solving_hard(input: tuple) -> int:
    """
    This function takes a tuple as input and returns an integer as output.

    Parameters:
    input (tuple): A tuple containing two integers representing m and n.

    Returns:
    int: An integer representing the solution to the problem.
    """
    solver = Hard()
    return solver.paths(input[0], input[1])


riddle_solvers = {
    "cv_easy": solve_cv_easy,
    "cv_medium": solve_cv_medium,
    "cv_hard": solve_cv_hard,
    "ml_easy": solve_ml_easy,
    "ml_medium": solve_ml_medium,
    "sec_medium_stegano": solve_sec_medium,
    "sec_hard": solve_sec_hard,
    "problem_solving_easy": solve_problem_solving_easy,
    "problem_solving_medium": solve_problem_solving_medium,
    "problem_solving_hard": solve_problem_solving_hard,
}
