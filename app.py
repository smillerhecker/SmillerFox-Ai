from flask import Flask, request, jsonify
from model import predict  # Fixed incorrect import

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_route():
    try:
        study_hours = float(request.json.get('study_hours', 0))  # Ensure study_hours is a float
        prediction = predict(study_hours)
        return jsonify({'prediction': f"You will {'pass' if prediction else 'fail'}."})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
