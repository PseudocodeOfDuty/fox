import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import joblib


class ml_medium:
    # Load the model
    def load_model(self, model_filename="riddles/ml/AdaBoostModel.joblib"):
        return joblib.load(model_filename)

    def solve(self, new_point):
        loaded_model = joblib.load("riddles/ml/AdaBoostModel.joblib")
        predicted_label = loaded_model.predict([new_point])[0]
        return int(predicted_label)
