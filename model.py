import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings('ignore')  # Suppress warnings during model fitting

def predict(study_hours):
    data = {
        "Study Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    }
    
    X = np.array(data["Study Hours"]).reshape(-1, 1)
    y = np.array(data["Pass"])

    model = LogisticRegression()
    model.fit(X, y)

    study_hours = np.array([[study_hours]])  # Ensure input is a 2D array
    prediction = model.predict(study_hours)
    return int(prediction[0])
