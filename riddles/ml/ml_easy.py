import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing


class ml_easy:

    def train_and_forecast(self,time_series_data, forecast_steps=50):
        try:
            # Use only the 'visits' column for simplicity
            data = time_series_data['visits']

            # Fit Simple Exponential Smoothing model
            model = SimpleExpSmoothing(data)
            fit_model = model.fit()

            # Predict the next 50 days using the loaded model
            predictions = fit_model.forecast(steps=forecast_steps).round(2).tolist()  # Round to two decimal places and convert to list

            return predictions
        except Exception as e:
            print(f"Error training and forecasting: {e}")
            return None

    def solve(self, data: pd.DataFrame):
        # Forecast future values using the loaded model and test data
        forecast_values = self.train_and_forecast(data)
        return forecast_values
