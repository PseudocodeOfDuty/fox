import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import joblib


class ml_easy:
    # Load the model
    def load_model(self, model_filename="ml/forecasting_model.joblib"):
        return joblib.load(model_filename)

    # Forecast future values
    def forecast_future_values(self, model, new_data, forecast_steps=50):
        # Convert 'timestamp' to datetime format
        new_data["timestamp"] = pd.to_datetime(new_data["timestamp"])

        # Set 'timestamp' as the index
        new_data.set_index("timestamp", inplace=True)

        # Forecast future periods
        forecast = model.get_forecast(steps=forecast_steps, exog=new_data)
        forecast_values = list(forecast.predicted_mean.round(2))

        return forecast_values

    def solve(self, data: pd.DataFrame):
        # Load the model
        loaded_model = self.load_model()

        # Forecast future values using the loaded model and test data
        forecast_values = self.forecast_future_values(loaded_model, data)

        return forecast_values
