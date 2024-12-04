from flask import Flask, request, jsonify
from machine_learning import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_route():
    study_hours = request.json['study_hours']
    prediction = predict(study_hours)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
