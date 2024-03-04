import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import joblib
import os

if os.name == "nt":
    MODEL_PATH = "riddles/ml/AdaBoostModel_win.joblib"
elif os.name == "posix":
    MODEL_PATH = "riddles/ml/AdaBoostModel_linux.joblib"
else:
    raise ValueError("Unsupported operating system")


class ml_medium:
    # Load the model
    def load_model(self, model_filename=MODEL_PATH):
        return joblib.load(model_filename)

    def solve(self, new_point):
        loaded_model = joblib.load(MODEL_PATH)
        predicted_label = loaded_model.predict([new_point])[0]
        return int(predicted_label)
