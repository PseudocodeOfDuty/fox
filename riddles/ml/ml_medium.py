import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import joblib
import os


class ml_medium:

    def solve(self, new_point, loaded_model):
        predicted_label = loaded_model.predict([new_point])[0]
        return int(predicted_label)
