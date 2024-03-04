import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import joblib
import os


# Step 1: Load the Data
# Assuming your data is in a CSV file with columns 'x_', 'y_', and 'class'
data = pd.read_csv('MlMediumTrainingData.csv')

# Step 2: Preprocess the Data
features = data[['x_', 'y_']]
labels = data['class']

# Step 3: Train AdaBoost Model
base_classifier = DecisionTreeClassifier(max_depth=1)  # You can adjust max_depth as needed
adaboost_model = AdaBoostClassifier(base_classifier, n_estimators=50, random_state=42)
adaboost_model.fit(features, labels)

# Step 4: Save the Model
if os.name == 'nt':
    joblib.dump(adaboost_model, 'AdaBoostModel_win.joblib')
elif os.name == 'posix':  
    joblib.dump(adaboost_model, 'AdaBoostModel_linux.joblib')
else:
    raise ValueError("Unsupported operating system")
