from flask import Flask, request, jsonify
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

app = Flask(__name__)

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

# Create a route to handle user input
@app.route('/predict', methods=['POST'])
def predict():
    study_hours = request.json['study_hours']
    prediction = model.predict(np.array([[study_hours]]))
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
