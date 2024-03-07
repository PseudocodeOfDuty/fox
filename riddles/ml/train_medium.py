import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib
import numpy as np

data = pd.read_csv('./riddles/ml/MlMediumTrainingData.csv')

X = data[['x_', 'y_']]
y = data['class']

knn_model = KNeighborsClassifier(n_neighbors=1) 
knn_model.fit(X, y)

# Step 3: Save the KNN model
joblib.dump(knn_model, 'KNNModel.joblib')

# Step 4: Load the KNN model
loaded_knn_model = joblib.load('KNNModel.joblib')

# Step 5: Function to get predicted label
def predict_label_with_model(new_data, model):
    predicted_label = model.predict([new_data])[0]
    return predicted_label

# Example usage with a single new data point using the loaded model
new_data_point = [-21.36385118, 0.973601638]
predicted_label = predict_label_with_model(new_data_point, loaded_knn_model)

print("Predicted label:", predicted_label)