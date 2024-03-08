import os
import glob
from riddles.cv.hard.cv_hard import cv_hard
import json
from fox_handlers.fox_models_handler import *
import numpy as np


def test(folder_path):
    solver = cv_hard()
    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Iterate over files in the folder
    for file_path in glob.glob(os.path.join(folder_path, "*.json")):
        with open(file_path, "r") as f:
            data = json.load(f)
            res = solver.solve(
                np.array(data[1], dtype="uint8"),
                data[0],
                loaded_processor_cv_hard,
                loaded_model_cv_hard,
            )
            print(res)


# Specify the folder path
folder_path = "riddles/cv/hard/images"

# Call the function to print .jpg paths
test(folder_path)
