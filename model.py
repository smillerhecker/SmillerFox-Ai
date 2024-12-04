import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def predict(study_hours):
    # Load the dataset
    data = {
        "Study Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    }
    df = pd.DataFrame(data)

    # Split the data into features and labels
    X = df[["Study Hours"]]
    y = df["Pass"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make a prediction
    prediction = model.predict(np.array([[study_hours]]))
    return int(prediction[0])
